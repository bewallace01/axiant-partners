#!/usr/bin/env python3
"""
Restructure article 3-column layout:
- Move Quick Answer from center to left rail (quick facts)
- Replace right rail CTA with "On this page" TOC
"""
import html
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Section headings to exclude from TOC (structural, not content sections)
TOC_EXCLUDE = {"quick answer", "related resources"}


def slugify(text: str) -> str:
    """Convert heading text to URL-safe id."""
    # Decode HTML entities for common chars
    text = re.sub(r"&ndash;|&mdash;", "-", text)
    text = re.sub(r"&[a-z]+;|&#\d+;", "", text)
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text.strip().lower() or "section"


def has_blog_post_shell(html: str) -> bool:
    return "blog-post-shell" in html


def has_blog_post_content(html: str) -> bool:
    if "form-container blog-post-content" not in html:
        return False
    if re.search(r'class="[^"]*blog-grid', html):
        return False
    return True


def extract_quick_answer(main_html: str) -> tuple[str, str]:
    """Extract quick-answer block. Returns (quick_answer_html, main_without_quick)."""
    m = re.search(
        r'\s*<div class="quick-answer">(.*?)</div>\s*',
        main_html,
        re.DOTALL,
    )
    if not m:
        return "", main_html
    quick = m.group(1).strip()
    # Wrap in blog-rail-quick-answer div, change h2 to span or keep as h3 for semantics
    # Remove the original h2 from quick content, wrap in rail structure
    quick_inner = re.sub(r"<h2>Quick Answer</h2>\s*", "", quick)
    quick_html = f'<div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick Answer</h3>{quick_inner}</div></div>'
    main_without = main_html[: m.start()] + main_html[m.end() :]
    return quick_html, main_without


def extract_headings_and_add_ids(main_html: str) -> tuple[list[tuple[str, str]], str]:
    """
    Find h2 headings, generate ids, add ids to h2 elements.
    Returns (list of (id, text), modified_main_html).
    Excludes Quick Answer, Related Resources.
    """
    toc_items = []
    seen_slugs = {}

    def replace_h2(match):
        full_tag, content = match.group(1), match.group(2)
        text = re.sub(r"<[^>]+>", "", content).strip()
        text_lower = text.lower()
        if text_lower in TOC_EXCLUDE:
            return match.group(0)
        base_slug = slugify(text)
        slug = base_slug
        idx = 0
        while slug in seen_slugs:
            idx += 1
            slug = f"{base_slug}-{idx}"
        seen_slugs[slug] = True
        toc_items.append((slug, text))
        # Add id to h2
        if 'id="' in full_tag or "id='" in full_tag:
            return match.group(0)
        return f'<h2 id="{slug}">{content}</h2>'

    # Match <h2>content</h2> - handle nested tags in content
    pattern = re.compile(r"<h2([^>]*)>(.*?)</h2>", re.DOTALL)
    new_main = pattern.sub(replace_h2, main_html)
    return toc_items, new_main


def build_toc_html(toc_items: list[tuple[str, str]]) -> str:
    """Build On this page nav HTML."""
    if not toc_items:
        return ""
    lines = [
        '      <aside class="blog-post-rail-right">',
        '        <div class="blog-rail-toc">',
        '          <h3>On this page</h3>',
        '          <nav aria-label="On this page">',
        "            <ul class=\"blog-post-toc-list\">",
    ]
    for slug, text in toc_items:
        text_esc = html.escape(html.unescape(text))
        lines.append(f'              <li><a href="#{slug}">{text_esc}</a></li>')
    lines.extend(
        [
            "            </ul>",
            "          </nav>",
            "        </div>",
            "      </aside>",
        ]
    )
    return "\n".join(lines)


def transform_article(html: str) -> str:
    """Restructure: quick answer -> left rail, CTA -> TOC in right rail."""
    if not has_blog_post_shell(html) or not has_blog_post_content(html):
        return html

    # Find blog-post-main content
    main_m = re.search(
        r"<main class=\"blog-post-main\">(.*?)</main>",
        html,
        re.DOTALL,
    )
    if not main_m:
        return html

    main_content = main_m.group(1)

    # Extract quick answer and remove from main
    quick_html, main_without_quick = extract_quick_answer(main_content)

    # Extract headings, add ids, build TOC
    toc_items, main_with_ids = extract_headings_and_add_ids(main_without_quick)

    # Build new main
    new_main = "<main class=\"blog-post-main\">" + main_with_ids + "</main>"

    # Update left rail: add quick answer card after the first blog-rail-card
    left_rail_m = re.search(
        r"(<aside class=\"blog-post-rail-left\">)(.*?)(</aside>)",
        html,
        re.DOTALL,
    )
    if not left_rail_m:
        return html

    left_inner = left_rail_m.group(2)
    # Insert quick answer as second card after first blog-rail-card closes
    if quick_html:
        depth, i, insert_pos = 0, 0, -1
        while i < len(left_inner):
            if left_inner[i : i + 4] == "<div":
                depth += 1
                i += 4
                continue
            if left_inner[i : i + 6] == "</div>":
                if depth == 1:
                    insert_pos = i + 6
                    break
                depth -= 1
                i += 6
                continue
            i += 1
        if insert_pos > 0:
            left_inner = (
                left_inner[:insert_pos]
                + "\n        <div class=\"blog-rail-card\">\n          "
                + quick_html
                + "\n        </div>"
                + left_inner[insert_pos:]
            )
    new_left_rail = left_rail_m.group(1) + left_inner + left_rail_m.group(3)

    # Replace right rail: CTA -> TOC
    right_rail_m = re.search(
        r"<aside class=\"blog-post-rail-right\">.*?</aside>",
        html,
        re.DOTALL,
    )
    if not right_rail_m:
        return html

    new_right_rail = build_toc_html(toc_items)
    if not new_right_rail:
        # Keep CTA if no TOC items
        return html

    # Perform replacements
    html = html.replace(left_rail_m.group(0), new_left_rail)
    html = html.replace(main_m.group(0), new_main)
    html = html.replace(right_rail_m.group(0), new_right_rail)

    return html


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            html = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if not has_blog_post_content(html) or not has_blog_post_shell(html):
            continue
        new_html = transform_article(html)
        if new_html != html:
            path.write_text(new_html, encoding="utf-8")
            rel = path.relative_to(ROOT)
            print(f"  Updated: {rel}")
            count += 1
    print(f"\nDone. Restructured {count} article rails (quick facts left, TOC right).")


if __name__ == "__main__":
    main()
