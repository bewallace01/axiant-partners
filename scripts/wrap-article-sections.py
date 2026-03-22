#!/usr/bin/env python3
"""
Wrap each h2 section in blog-post-main with <section class="blog-article-card"> for card layout.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def wrap_sections(html: str) -> str:
    """Wrap each h2 + content block in blog-article-card."""
    main_m = re.search(r"<main class=\"blog-post-main\">(.*?)</main>", html, re.DOTALL)
    if not main_m:
        return html

    inner = main_m.group(1)

    # Extract related-resources and services-cta to append at end
    related = ""
    cta = ""
    related_m = re.search(
        r'\s*<section class="related-resources"[^>]*>.*?</section>\s*',
        inner,
        re.DOTALL,
    )
    if related_m:
        related = related_m.group(0)
        inner = inner[: related_m.start()] + inner[related_m.end() :]

    cta_m = re.search(
        r'\s*<div class="services-cta">.*?</div>\s*',
        inner,
        re.DOTALL,
    )
    if cta_m:
        cta = cta_m.group(0)
        inner = inner[: cta_m.start()] + inner[cta_m.end() :]

    # Split by h2 - each section starts with <h2
    parts = re.split(r"(?=<h2\s)", inner)
    wrapped = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith("<h2"):
            wrapped.append(f'<section class="blog-article-card">\n{part}\n</section>')
        else:
            wrapped.append(part)

    new_inner = "\n\n".join(wrapped) + related + cta
    new_main = f"<main class=\"blog-post-main\">{new_inner}</main>"
    html = html.replace(main_m.group(0), new_main)

    # Prevent enhanceBlogPostLayout from restructuring (we have pre-built shell)
    html = re.sub(
        r'<div class="form-container blog-post-content">',
        '<div class="form-container blog-post-content" data-blog-enhanced="1">',
        html,
        count=1,
    )
    return html


def has_blog_post(html: str) -> bool:
    return "blog-post-main" in html and "form-container blog-post-content" in html


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if not has_blog_post(content):
            continue
        if "blog-article-card" in content:
            continue  # Already wrapped
        new_content = wrap_sections(content)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  Wrapped: {path.relative_to(ROOT)}")
            count += 1
    print(f"\nDone. Wrapped {count} articles.")


if __name__ == "__main__":
    main()
