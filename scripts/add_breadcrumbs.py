#!/usr/bin/env python3
"""Add BreadcrumbList schema to article hub and article pages."""
import re
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
BASE_URL = "https://axiantpartners.com"

TOPIC_NAMES = {
    "sba-loans": "SBA Loans",
    "equipment-financing": "Equipment Financing",
    "business-line-of-credit": "Business Line of Credit",
    "working-capital-loans": "Working Capital Loans",
    "business-term-loans": "Business Term Loans",
    "commercial-real-estate-loans": "Commercial Real Estate Loans",
    "commercial-bridge-loans": "Commercial Bridge Loans",
    "fix-and-flip": "Fix and Flip",
    "revenue-based-financing": "Revenue-Based Financing",
    "securities-based-lending": "Securities-Based Lending",
}

def make_breadcrumb_schema(items):
    """items: list of (name, url)"""
    elems = []
    for i, (name, url) in enumerate(items, 1):
        elems.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": BASE_URL + url
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elems
    }, separators=(',', ':'))

def add_to_hub(content, topic_slug):
    """Add BreadcrumbList to hub page (topic/articles/index.html)."""
    if '"@type":"BreadcrumbList"' in content or '"@type": "BreadcrumbList"' in content:
        return content
    topic_name = TOPIC_NAMES.get(topic_slug, topic_slug.replace("-", " ").title())
    schema = make_breadcrumb_schema([
        ("Home", "/"),
        (topic_name, f"/{topic_slug}.html"),
        ("Articles", f"/{topic_slug}/articles/")
    ])
    # Insert before existing schema (after first script tag or before </head>)
    insert = f'    <script type="application/ld+json">\n    {schema}\n    </script>\n    '
    # Find position: after last meta/link, before first existing script
    match = re.search(r'(<script type="application/ld\+json">)', content)
    if match:
        content = content[:match.start()] + insert + content[match.start():]
    return content

def add_to_article(content, topic_slug, article_slug, headline):
    """Add BreadcrumbList to article page."""
    if '"@type":"BreadcrumbList"' in content or '"@type": "BreadcrumbList"' in content:
        return content
    topic_name = TOPIC_NAMES.get(topic_slug, topic_slug.replace("-", " ").title())
    # Clean headline: remove HTML entities, truncate if needed
    schema = make_breadcrumb_schema([
        ("Home", "/"),
        (topic_name, f"/{topic_slug}.html"),
        ("Articles", f"/{topic_slug}/articles/"),
        (headline, f"/{topic_slug}/articles/{article_slug}/")
    ])
    insert = f'    <script type="application/ld+json">\n    {schema}\n    </script>\n    '
    match = re.search(r'(<script type="application/ld\+json">)', content)
    if match:
        content = content[:match.start()] + insert + content[match.start():]
    return content

def get_headline(content):
    """Extract headline from Article schema or H1."""
    m = re.search(r'"headline"\s*:\s*"([^"]+)"', content)
    if m:
        return m.group(1)
    m = re.search(r'<h1[^>]*>([^<]+)</h1>', content)
    if m:
        return m.group(1).strip()
    return "Article"

def main():
    count = 0
    for topic_slug in TOPIC_NAMES:
        hub_path = BASE / topic_slug / "articles" / "index.html"
        if hub_path.exists():
            content = hub_path.read_text(encoding="utf-8")
            new_content = add_to_hub(content, topic_slug)
            if new_content != content:
                hub_path.write_text(new_content, encoding="utf-8")
                count += 1
                print(f"Hub: {topic_slug}/articles/")

        articles_dir = BASE / topic_slug / "articles"
        if articles_dir.exists():
            for slug_dir in articles_dir.iterdir():
                if slug_dir.is_dir() and slug_dir.name != "index":
                    idx = slug_dir / "index.html"
                    if idx.exists():
                        content = idx.read_text(encoding="utf-8")
                        headline = get_headline(content)
                        new_content = add_to_article(content, topic_slug, slug_dir.name, headline)
                        if new_content != content:
                            idx.write_text(new_content, encoding="utf-8")
                            count += 1
    print(f"Added breadcrumbs to {count} files")

if __name__ == "__main__":
    main()
