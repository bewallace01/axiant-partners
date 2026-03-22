#!/usr/bin/env python3
"""Add 3-column layout (blog-post-shell) to article posts that use blog-post-content."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Right rail CTA - match link will be inferred from context or use default
RIGHT_RAIL_CTA = '''      <aside class="blog-post-rail-right">
        <div class="blog-rail-cta">
          <h3>Ready to Get Started?</h3>
          <p>Get matched with lenders who specialize in your industry.</p>
          <a href="/match.html" class="btn-primary">Get Matched</a>
        </div>
      </aside>'''


def has_blog_post_shell(html: str) -> bool:
    return "blog-post-shell" in html


def has_blog_post_content(html: str) -> bool:
    if 'form-container blog-post-content' not in html:
        return False
    # Exclude listing pages that use blog-grid layout (not JS references to .blog-grid)
    if re.search(r'class="[^"]*blog-grid', html):
        return False
    return True


def extract_back_link(html: str) -> str:
    """Extract blog-back paragraph content."""
    m = re.search(r'<p class="blog-back">(.*?)</p>', html, re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_byline(html: str) -> str:
    """Extract blog-byline content (text only)."""
    m = re.search(r'<p class="blog-byline">(.*?)</p>', html, re.DOTALL)
    return m.group(1).strip() if m else ""


def transform_article(html: str) -> str:
    """Wrap article content in 3-column blog-post-shell structure."""
    if has_blog_post_shell(html):
        return html

    if not has_blog_post_content(html):
        return html

    # Find the form-container blog-post-content div (flexible whitespace)
    start_m = re.search(
        r'<div\s+class="form-container\s+blog-post-content"\s*>',
        html
    )
    if not start_m:
        return html

    start_pos = start_m.end()
    back_content = extract_back_link(html)
    byline_content = extract_byline(html)

    # Build left rail
    left_rail = f'''    <div class="blog-post-shell">
      <aside class="blog-post-rail-left">
        <div class="blog-rail-card">
          <p class="blog-rail-back">{back_content}</p>'''
    if byline_content:
        left_rail += f'''
          <div class="blog-rail-meta-item"><span class="blog-rail-label">Updated</span> {byline_content.replace("Last updated: ", "")}</div>'''
    left_rail += '''
        </div>
      </aside>
      <main class="blog-post-main">'''

    # Find main content: from blog-lead (or first non-back, non-byline) to before closing </div> of form-container
    # We need to remove blog-back and blog-byline, wrap the rest in blog-post-main
    # Pattern: match from start_pos, skip blog-back and blog-byline, capture rest until we hit the closing div
    # The structure is: <p class="blog-back">...</p> maybe whitespace <p class="blog-byline">...</p> maybe whitespace then content
    content_start = start_pos
    # Remove blog-back
    blog_back_pat = re.compile(
        r'<p class="blog-back">.*?</p>\s*',
        re.DOTALL
    )
    # Remove blog-byline
    blog_byline_pat = re.compile(
        r'<p class="blog-byline">.*?</p>\s*',
        re.DOTALL
    )

    # Find where the form-container div ends - it's the one that wraps the content
    # We'll search for the pattern: content between start and </div> that closes form-container
    # The div nesting: form-container has many children. The closing </div> for form-container is before </div> for container.
    # Simpler: find the content after blog-byline until the last </div> before <footer or script
    inner = html[start_pos:]
    # Remove blog-back
    inner = blog_back_pat.sub("", inner, count=1)
    # Remove blog-byline
    inner = blog_byline_pat.sub("", inner, count=1)
    # inner now starts with the main content (blog-lead, quick-answer, etc.)
    # We need to find where the form-container's content ends
    # The form-container's closing </div> - we need to match the right one
    # Find the closing </div> that matches form-container. Track div depth.
    # We're inside form-container content, so depth starts at 1 (form-container is open).
    depth = 1
    i = 0
    main_content = ""
    rest = ""
    while i < len(inner):
        if i + 4 <= len(inner) and inner[i:i+4] == "<div":
            # Check for self-closing or opening div
            chunk = inner[i:i+100]
            if "/>" not in chunk.split(">")[0]:
                depth += 1
            i += 4
            continue
        if i + 6 <= len(inner) and inner[i:i+6] == "</div>":
            depth -= 1
            if depth == 0:
                main_content = inner[:i].strip()
                rest = inner[i:]
                break
            i += 6
            continue
        i += 1
    else:
        return html

    # Build new content
    right_rail = RIGHT_RAIL_CTA
    new_inner = left_rail + "\n" + main_content + "\n      </main>\n" + right_rail + "\n    </div>"
    new_html = html[:start_pos] + new_inner + rest
    return new_html


def ensure_blog_layout_css(html: str) -> str:
    """Ensure blog-layout.css is loaded (add before </head> if missing)."""
    if "blog-layout.css" in html:
        return html
    # Add before </head>
    if "</head>" in html and "article-layout.css" in html:
        html = html.replace(
            '<link rel="stylesheet" href="/article-layout.css">',
            '<link rel="stylesheet" href="/article-layout.css">\n    <link rel="stylesheet" href="/blog-layout.css">'
        )
    elif "</head>" in html:
        html = html.replace("</head>", '    <link rel="stylesheet" href="/blog-layout.css">\n</head>')
    return html


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            html = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if not has_blog_post_content(html):
            continue
        if has_blog_post_shell(html):
            continue
        new_html = transform_article(html)
        if new_html != html:
            new_html = ensure_blog_layout_css(new_html)
            path.write_text(new_html, encoding="utf-8")
            rel = path.relative_to(ROOT)
            print(f"  Updated: {rel}")
            count += 1
    print(f"\nDone. Updated {count} article posts with 3-column layout.")


if __name__ == "__main__":
    main()
