#!/usr/bin/env python3
"""Add responsive srcset to industry tile images for mobile performance."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = "v=4"
SIZES = '(max-width: 768px) 100vw, 560px'

# Map base image stems to their tile variant availability
TILE_STEMS = [
    "equipment-financing-hero", "sba-hero", "wcl-hero-operations",
    "bloc-hero-business-office", "btl-hero", "cre-hero", "cbl-hero",
    "faf-hero", "mca-hero", "rbf-hero", "sbl-hero",
    "construction-hero-bg", "medical-practices-hero-bg", "manufacturing-hero-bg",
    "manufacturing-industry-overview", "trucking-hero-bg", "restaurants-hero-bg",
    "logistics-warehousing-hero-bg", "logistics-warehousing-industry-overview",
    "forestry-hero-bg", "agriculture-hero-bg", "landscaping-hero-bg", "auto-repair-hero-bg",
]


def replace_tile_srcset(content: str) -> tuple[str, int]:
    """Replace single srcset with responsive srcset for industry tiles."""
    count = 0
    for stem in TILE_STEMS:
        # Only replace if it's the simple single-source pattern (industry tile)
        # Avoid replacing if already has responsive srcset
        old = f'srcset="/assets/{stem}.webp?{CACHE}"'
        if old not in content:
            continue
        # Skip if already has 560w or 800w (responsive)
        if f"{stem}-560w" in content or f"{stem}-800w" in content:
            continue
        new = f'srcset="/assets/{stem}-560w.webp?{CACHE} 560w, /assets/{stem}-800w.webp?{CACHE} 800w" sizes="{SIZES}"'
        content = content.replace(old, new)
        count += 1
    return content, count


def main():
    total = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        new_content, count = replace_tile_srcset(content)
        if count > 0:
            path.write_text(new_content, encoding="utf-8")
            rel = path.relative_to(ROOT)
            print(f"  {rel}: {count} tiles updated")
            total += count
    print(f"\nDone. Updated {total} industry tile srcsets.")


if __name__ == "__main__":
    main()
