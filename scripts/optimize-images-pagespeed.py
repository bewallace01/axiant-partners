#!/usr/bin/env python3
"""Optimize images flagged by PageSpeed: hero skyline + tile variants (lower compression)."""
from pathlib import Path
import sys

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: python -m pip install Pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# Hero skyline: compress to save ~171 KiB
SKYLINE = "ai-realestate-3"
SKYLINE_QUALITY = 78

# Tile variants to recompress (PageSpeed flagged faf-hero, equipment-financing-hero)
TILE_STEMS = [
    "equipment-financing-hero", "sba-hero", "wcl-hero-operations",
    "bloc-hero-business-office", "btl-hero", "cre-hero", "cbl-hero",
    "faf-hero", "mca-hero", "rbf-hero", "sbl-hero",
    "construction-hero-bg", "medical-practices-hero-bg", "manufacturing-hero-bg",
    "manufacturing-industry-overview", "trucking-hero-bg", "restaurants-hero-bg",
    "logistics-warehousing-hero-bg", "logistics-warehousing-industry-overview",
    "forestry-hero-bg", "agriculture-hero-bg", "landscaping-hero-bg", "auto-repair-hero-bg",
]
TILE_QUALITY = 78


def compress_webp(path: Path, quality: int, desc: str = "") -> bool:
    """Recompress WebP at lower quality. Returns True if file was updated."""
    try:
        img = Image.open(path)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        before = path.stat().st_size
        img.save(path, "WEBP", quality=quality, method=6)
        after = path.stat().st_size
        saved = (before - after) / 1024
        print(f"  {path.name}: {before/1024:.0f}KB -> {after/1024:.0f}KB (saved {saved:.0f}KB) {desc}")
        return True
    except Exception as e:
        print(f"  ERROR {path}: {e}")
        return False


def main():
    print("1. Compressing hero skyline (ai-realestate-3.webp)...")
    sky = ASSETS / f"{SKYLINE}.webp"
    if sky.exists():
        compress_webp(sky, SKYLINE_QUALITY, "hero-skyline")
    else:
        print(f"  Skip: {sky} not found")

    print("\n2. Recompressing tile variants at quality", TILE_QUALITY, "...")
    for stem in TILE_STEMS:
        for w in (560, 800):
            p = ASSETS / f"{stem}-{w}w.webp"
            if p.exists():
                compress_webp(p, TILE_QUALITY)
    print("Done.")


if __name__ == "__main__":
    main()
