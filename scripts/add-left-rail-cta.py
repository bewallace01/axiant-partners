#!/usr/bin/env python3
"""
Add CTA card to the left sidebar (blog-post-rail-left) on all article pages.
The CTA appears after the Quick Facts / summary card.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Service-specific CTA text - matches path segments
CTA_BY_SERVICE = {
    "sba-loans": ("Get Matched for SBA Financing", "/match.html"),
    "equipment-financing": ("Get Matched for Equipment Financing", "/match.html"),
    "equipment": ("Get Matched for Equipment Financing", "/match.html"),
    "business-line-of-credit": ("Get Matched for a Line of Credit", "/match.html"),
    "working-capital-loans": ("Get Matched for Working Capital", "/match.html"),
    "business-term-loans": ("Get Matched for a Term Loan", "/match.html"),
    "commercial-real-estate-loans": ("Get Matched for CRE Financing", "/match.html"),
    "commercial-bridge-loans": ("Get Matched for Bridge Financing", "/match.html"),
    "fix-and-flip": ("Get Matched for Fix and Flip", "/match.html"),
    "revenue-based-financing": ("Get Matched for Revenue-Based Financing", "/match.html"),
    "securities-based-lending": ("Get Matched for Securities-Based Lending", "/match.html"),
    "merchant-cash-advance": ("Get Matched for MCA", "/match.html"),
    "construction-business-financing": ("Get Matched for Construction Financing", "/match.html"),
    "trucking-business-financing": ("Get Matched for Trucking Financing", "/match.html"),
    "articles": ("Get Matched with Lenders", "/match.html"),
}

DEFAULT_CTA = ("Get Matched", "/match.html")


def get_cta_for_path(path: Path) -> tuple:
    """Return (button_text, href) for the article path."""
    path_str = path.as_posix().lower()
    for service, (text, href) in CTA_BY_SERVICE.items():
        if f"/{service}/" in path_str or path_str.endswith(f"/{service}"):
            return (text, href)
    return DEFAULT_CTA


def has_left_rail(html: str) -> bool:
    return "blog-post-rail-left" in html


def has_left_rail_cta(html: str) -> bool:
    """Check if left rail already has a CTA."""
    left_rail = re.search(
        r'<aside class="blog-post-rail-left">(.*?)</aside>',
        html,
        re.DOTALL,
    )
    if not left_rail:
        return False
    inner = left_rail.group(1)
    return "blog-rail-cta" in inner


def add_cta_to_left_rail(html: str, cta_text: str, cta_href: str) -> str:
    """Insert CTA card after the last blog-rail-card in the left rail."""
    cta_html = f'''        <div class="blog-rail-card blog-rail-cta">
          <h3>Ready to get funded?</h3>
          <p>Get matched with lenders who fit your business.</p>
          <a href="{cta_href}" class="btn-primary">{cta_text}</a>
        </div>
'''
    # Find the left rail and insert CTA before </aside>
    pattern = r'(<aside class="blog-post-rail-left">)(.*?)(\s*</aside>)'
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        return html

    prefix, inner, suffix = match.groups()
    # Only add if not already present
    if "blog-rail-cta" in inner:
        return html
    new_inner = inner.rstrip() + "\n" + cta_html
    new_rail = prefix + new_inner + suffix
    return html[: match.start()] + new_rail + html[match.end() :]


def is_article_page(path: Path, content: str) -> bool:
    """Exclude hub pages (articles/index.html) and non-article pages."""
    if "form-container blog-post-content" not in content:
        return False
    if "blog-post-shell" not in content:
        return False
    # Exclude listing pages (class on container, not just string in scripts)
    if 'class="blog-content blog-listing"' in content or 'class="blog-listing' in content:
        return False
    return True


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        if not is_article_page(path, content):
            continue
        if not has_left_rail(content):
            continue
        if has_left_rail_cta(content):
            continue
        cta_text, cta_href = get_cta_for_path(path)
        new_content = add_cta_to_left_rail(content, cta_text, cta_href)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  Updated: {path.relative_to(ROOT)}")
            count += 1
    print(f"\nDone. Added CTA to {count} articles.")


if __name__ == "__main__":
    main()
