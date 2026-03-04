#!/usr/bin/env python3
"""Fix SEO: update blog canonicals/schema/og:url and generate sitemap."""
import re
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
BLOG_DIR = BASE / "blog"
REDIRECTS = BASE / "_redirects"
SITEMAP = BASE / "sitemap.xml"
BASE_URL = "https://www.axiantpartners.com"

def load_redirect_map():
    """Parse _redirects for blog/slug.html -> /topic/articles/slug/"""
    m = {}
    with open(REDIRECTS) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2 and parts[0].startswith("/blog/"):
                src = parts[0].lstrip("/")  # blog/slug.html
                dst = parts[1]  # /topic/articles/slug/ or /working-capital-loans/
                m[src] = dst if dst.startswith("/") else "/" + dst
    return m

def fix_blog_file(blog_rel: str, canon_url: str):
    """Update canonical, og:url, and schema url in blog file."""
    p = BASE / blog_rel
    if not p.exists():
        return False
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    old_blog_url = f"{BASE_URL}/blog/{Path(blog_rel).name}"
    # canonical
    content = re.sub(
        r'<link\s+rel="canonical"\s+href="[^"]*"',
        f'<link rel="canonical" href="{canon_url}"',
        content, count=1
    )
    # og:url
    content = re.sub(
        r'<meta\s+property="og:url"\s+content="[^"]*"',
        f'<meta property="og:url" content="{canon_url}"',
        content, count=1
    )
    # schema "url" - match both "url":"..." and "url": "..."
    content = re.sub(
        r'"url"\s*:\s*"https://www\.axiantpartners\.com/blog/[^"]*"',
        f'"url":"{canon_url}"',
        content, count=1
    )
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def main():
    redirects = load_redirect_map()
    # /working-capital-loans/ redirects to /working-capital-loans/articles/
    hub_redirects = {"/working-capital-loans/": "/working-capital-loans/articles/"}
    for blog_src, dest in redirects.items():
        canon_path = hub_redirects.get(dest, dest)
        canon_url = BASE_URL + canon_path if canon_path.endswith("/") else BASE_URL + canon_path + "/"
        fix_blog_file(blog_src, canon_url)
        print(f"Fixed {blog_src} -> {canon_url}")

if __name__ == "__main__":
    main()
