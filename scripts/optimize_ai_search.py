#!/usr/bin/env python3
"""
Optimize site for AI search (ChatGPT, Perplexity, Google AI Overviews).

- Adds robots meta with max-snippet, max-image-preview for AI extraction
- Ensures Article schema has image when og:image exists
- Ensures Article schema has mainEntityOfPage
- Runs across all HTML files in the project
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ROBOTS_META = 'content="index, follow, max-snippet:-1, max-image-preview:large"'


def has_robots_meta(content: str) -> bool:
    return 'max-snippet' in content or 'max-image-preview' in content


def get_og_image(content: str) -> str | None:
    m = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', content)
    return m.group(1) if m else None


def article_has_image(content: str) -> bool:
    return '"image"' in content and '"@type":"Article"' in content


def article_has_main_entity(content: str) -> bool:
    return 'mainEntityOfPage' in content


def add_robots_meta(content: str, insert_after: str) -> str:
    """Add robots meta after description meta."""
    if has_robots_meta(content):
        return content
    # Insert after first meta description
    pattern = r'(<meta\s+name="description"\s+content="[^"]*"\s*>)'
    replacement = rf'\1\n    <meta name="robots" {ROBOTS_META}>'
    return re.sub(pattern, replacement, content, count=1)


def add_article_image(content: str, image_url: str) -> str:
    """Add image to Article schema JSON-LD."""
    if article_has_image(content):
        return content
    # Find Article schema and add image before "url"
    pattern = r'("\@type"\s*:\s*"Article"[^}]*?)("url"\s*:\s*")'
    replacement = rf'\1"image":"{image_url}",\2'
    return re.sub(pattern, replacement, content, count=1)


def add_main_entity_of_page(content: str, page_url: str) -> str:
    """Add mainEntityOfPage to Article schema."""
    if article_has_main_entity(content):
        return content
    # Add after publisher in Article
    pattern = r'("publisher"\s*:\s*\{[^}]+\})(\s*\})'
    meop = f',"mainEntityOfPage":{{"@type":"WebPage","@id":"{page_url}"}}'
    replacement = rf'\1{meop}\2'
    return re.sub(pattern, replacement, content, count=1)


def get_canonical_url(content: str) -> str | None:
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', content)
    return m.group(1) if m else None


def process_file(path: Path) -> bool:
    """Process a single HTML file. Returns True if modified."""
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  Skip {path}: {e}")
        return False

    original = content

    # Add robots meta if missing (for any page with description)
    if 'meta name="description"' in content:
        content = add_robots_meta(content, "description")

    # Article-specific: add image and mainEntityOfPage
    if '"@type":"Article"' in content:
        canonical = get_canonical_url(content)
        og_image = get_og_image(content)
        if og_image and not article_has_image(content):
            content = add_article_image(content, og_image)
        if canonical and not article_has_main_entity(content):
            content = add_main_entity_of_page(content, canonical)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    count = 0
    for path in sorted(BASE.rglob("*.html")):
        rel = path.relative_to(BASE)
        if "node_modules" in str(rel) or ".git" in str(rel):
            continue
        if process_file(path):
            count += 1
            print(f"Updated: {rel}")

    print(f"\nDone. Modified {count} files.")


if __name__ == "__main__":
    main()
