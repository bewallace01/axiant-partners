#!/usr/bin/env python3
"""Remove blog-article-card wrappers - restore main content to single block."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def unwrap_sections(html: str) -> str:
    """Remove <section class="blog-article-card"> wrappers from main content."""
    main_m = re.search(r"<main class=\"blog-post-main\">(.*?)</main>", html, re.DOTALL)
    if not main_m:
        return html

    inner = main_m.group(1)
    if "blog-article-card" not in inner:
        return html

    # Remove section wrappers: <section class="blog-article-card"> and </section>
    inner = re.sub(r'\s*<section class="blog-article-card">\s*', "\n", inner)
    inner = re.sub(r'\s*</section>\s*', "\n", inner)

    new_main = f"<main class=\"blog-post-main\">{inner}</main>"
    return html.replace(main_m.group(0), new_main)


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if "blog-article-card" not in content:
            continue
        new_content = unwrap_sections(content)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  Unwrapped: {path.relative_to(ROOT)}")
            count += 1
    print(f"\nDone. Unwrapped {count} articles.")


if __name__ == "__main__":
    main()
