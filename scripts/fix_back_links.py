#!/usr/bin/env python3
"""Update *-blog.html back/related links to /topic/articles/ in blog and topic article files."""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

REPLACEMENTS = [
    ("../sba-loans-blog.html", "/sba-loans/articles/"),
    ("../equipment-financing-blog.html", "/equipment-financing/articles/"),
    ("../business-line-of-credit-blog.html", "/business-line-of-credit/articles/"),
    ("../working-capital-loans-blog.html", "/working-capital-loans/articles/"),
    ("../business-term-loans-blog.html", "/business-term-loans/articles/"),
    ("../commercial-real-estate-loans-blog.html", "/commercial-real-estate-loans/articles/"),
    ("../commercial-bridge-loans-blog.html", "/commercial-bridge-loans/articles/"),
    ("../revenue-based-financing-blog.html", "/revenue-based-financing/articles/"),
    ("../securities-based-lending-blog.html", "/securities-based-lending/articles/"),
]

def main():
    count = 0
    for html in BASE.rglob("*.html"):
        if "node_modules" in str(html):
            continue
        content = html.read_text(encoding="utf-8")
        orig = content
        for old, new in REPLACEMENTS:
            content = content.replace(old, new)
        if content != orig:
            html.write_text(content, encoding="utf-8")
            count += 1
            print(f"Updated {html.relative_to(BASE)}")
    print(f"Updated {count} files")

if __name__ == "__main__":
    main()
