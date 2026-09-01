#!/usr/bin/env python3
"""
Update article rails: Quick Facts left, TOC in card right, remove lead from center.
- Remove blog-lead (summary) from center content
- Add Quick Facts to left: from quick-answer (relabel) or from blog-lead
- Wrap right TOC in blog-rail-card for consistent styling
- Ensure every article has this structure
"""
import html as html_module
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOC_EXCLUDE = {"quick answer", "quick facts", "related resources"}


def slugify(text: str) -> str:
    import unicodedata
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


def transform_article(html: str) -> str:
    if not has_blog_post_shell(html) or not has_blog_post_content(html):
        return html

    main_m = re.search(r"<main class=\"blog-post-main\">(.*?)</main>", html, re.DOTALL)
    if not main_m:
        return html

    main_content = main_m.group(1)
    changed = False

    # 1. Remove blog-lead from main and capture it for Quick Facts
    lead_match = re.search(r'\s*<p class="blog-lead">(.*?)</p>\s*', main_content, re.DOTALL)
    lead_html = ""
    if lead_match:
        lead_html = lead_match.group(1).strip()
        main_content = main_content[: lead_match.start()] + main_content[lead_match.end() :]
        changed = True

    # 2. Extract quick-answer if present (we'll use it for Quick Facts, prefer over lead)
    quick_match = re.search(r'\s*<div class="quick-answer">(.*?)</div>\s*', main_content, re.DOTALL)
    quick_inner = ""
    if quick_match:
        quick_block = quick_match.group(1)
        quick_inner = re.sub(r"<h2>Quick Answer</h2>\s*", "", quick_block).strip()
        main_content = main_content[: quick_match.start()] + main_content[quick_match.end() :]
        changed = True

    # 3. Build Quick Facts content: prefer quick-answer, else blog-lead
    quick_facts_content = quick_inner if quick_inner else (f"<p>{lead_html}</p>" if lead_html else "")

    # 4. Update left rail: ensure Quick Facts card exists
    left_rail_m = re.search(r"(<aside class=\"blog-post-rail-left\">)(.*?)(</aside>)", html, re.DOTALL)
    if not left_rail_m:
        return html

    left_inner = left_rail_m.group(2)
    has_quick_facts = "blog-rail-quick-answer" in left_inner or "blog-rail-quick-content" in left_inner

    if quick_facts_content and not has_quick_facts:
        # Add Quick Facts card after first blog-rail-card
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
            qf_html = (
                '<div class="blog-rail-quick-answer">'
                '<div class="blog-rail-quick-content">'
                '<h3>Quick Facts</h3>'
                f'{quick_facts_content}'
                '</div></div>'
            )
            left_inner = (
                left_inner[:insert_pos]
                + '\n        <div class="blog-rail-card">\n          '
                + qf_html
                + '\n        </div>'
                + left_inner[insert_pos:]
            )
            changed = True
    elif has_quick_facts:
        # Change "Quick Answer" to "Quick Facts" if present
        left_inner_new = re.sub(
            r"<h3>Quick Answer</h3>",
            "<h3>Quick Facts</h3>",
            left_inner,
        )
        if left_inner_new != left_inner:
            left_inner = left_inner_new
            changed = True

    # 5. Remove blog-lead from articles that have Quick Facts from quick-answer (lead already removed above)
    # If we had lead but no quick_facts_content (quick_inner was used), we still removed lead - good.

    # 6. Extract headings for TOC, add ids
    toc_items = []
    seen_slugs = {}

    def replace_h2(match):
        content = match.group(2)
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
        if 'id="' in match.group(1) or "id='" in match.group(1):
            return match.group(0)
        return f'<h2 id="{slug}">{content}</h2>'

    h2_pattern = re.compile(r"<h2([^>]*)>(.*?)</h2>", re.DOTALL)
    main_content = h2_pattern.sub(replace_h2, main_content)

    new_main = "<main class=\"blog-post-main\">" + main_content + "</main>"

    # 7. Update right rail: wrap TOC in blog-rail-card
    right_rail_m = re.search(
        r"<aside class=\"blog-post-rail-right\">(.*?)</aside>",
        html,
        re.DOTALL,
    )
    if not right_rail_m:
        return html

    right_inner = right_rail_m.group(1)
    # Check if TOC is already wrapped in blog-rail-card
    if '<div class="blog-rail-card">' in right_inner and 'blog-rail-toc' in right_inner:
        pass  # Already wrapped
    elif 'blog-rail-toc' in right_inner and '<div class="blog-rail-card">' not in right_inner:
        # Wrap blog-rail-toc in blog-rail-card
        toc_div = re.search(r'<div class="blog-rail-toc">(.*?)</div>\s*</aside>', html, re.DOTALL)
        if toc_div:
            # Replace the right rail with card-wrapped version
            new_right = (
                '        <div class="blog-rail-card">\n'
                '        <div class="blog-rail-toc">\n'
                + toc_div.group(1) +
                '\n        </div>\n        </div>\n      '
            )
            old_right = right_rail_m.group(0)
            # Need to replace the right rail content
            right_inner_new = re.sub(
                r'<div class="blog-rail-toc">(.*?)</div>',
                r'<div class="blog-rail-card">\n        <div class="blog-rail-toc">\1</div>\n        </div>',
                right_inner,
                count=1,
                flags=re.DOTALL,
            )
            if right_inner_new != right_inner:
                right_inner = right_inner_new
                changed = True

    # Build new right rail if we have toc_items (in case we need to rebuild)
    if toc_items:
        lines = [
            '      <aside class="blog-post-rail-right">',
            '        <div class="blog-rail-card">',
            '        <div class="blog-rail-toc">',
            '          <h3>On this page</h3>',
            '          <nav aria-label="On this page">',
            '            <ul class="blog-post-toc-list">',
        ]
        for slug, text in toc_items:
            text_esc = html_module.escape(html_module.unescape(text))
            lines.append(f'              <li><a href="#{slug}">{text_esc}</a></li>')
        lines.extend([
            "            </ul>",
            "          </nav>",
            "        </div>",
            "        </div>",
            "      </aside>",
        ])
        new_right_rail = "\n".join(lines)
        # Replace existing right rail
        old_right = re.search(
            r"<aside class=\"blog-post-rail-right\">.*?</aside>",
            html,
            re.DOTALL,
        )
        if old_right:
            html = html.replace(old_right.group(0), new_right_rail)
            changed = True

    if changed:
        html = html.replace(left_rail_m.group(0), left_rail_m.group(1) + left_inner + left_rail_m.group(3))
        html = html.replace(main_m.group(0), new_main)

    return html


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if not has_blog_post_content(content) or not has_blog_post_shell(content):
            continue
        new_content = transform_article(content)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  Updated: {path.relative_to(ROOT)}")
            count += 1
    print(f"\nDone. Updated {count} articles.")


if __name__ == "__main__":
    main()
