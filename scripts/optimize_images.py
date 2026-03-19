#!/usr/bin/env python3
"""
Optimize images for web: convert PNG to WebP, resize oversized images.
Run from project root: python scripts/optimize_images.py
"""
from pathlib import Path
import sys

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: python -m pip install Pillow")
    sys.exit(1)

# Project root (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# Quality for WebP (80-85 typical for good balance)
WEBP_QUALITY = 82

# Max dimensions - images displayed larger get capped
MAX_WIDTH = 1400  # Hero / banners
MAX_TILE = 560   # 2x for retina tiles at 280px


def convert_to_webp(src: Path, out_dir: Path, max_size: int | None = None) -> Path | None:
    """Convert PNG to WebP, optionally resize. Returns output path or None."""
    if not src.suffix.lower() in (".png", ".jpg", ".jpeg"):
        return None
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / (src.stem + ".webp")
    try:
        img = Image.open(src)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        if max_size and (w > max_size or h > max_size):
            ratio = min(max_size / w, max_size / h)
            nw, nh = int(w * ratio), int(h * ratio)
            img = img.resize((nw, nh), Image.Resampling.LANCZOS)
        img.save(out, "WEBP", quality=WEBP_QUALITY, method=6)
        orig_kb = src.stat().st_size / 1024
        new_kb = out.stat().st_size / 1024
        print(f"  {src.name} -> {out.name} ({orig_kb:.0f}KB -> {new_kb:.0f}KB)")
        return out
    except Exception as e:
        print(f"  ERROR {src.name}: {e}")
        return None


def main():
    print("Optimizing images...")
    # Priority 1: LCP hero (index.html)
    hero = ASSETS / "dump-truck-excavator-hero.png"
    if hero.exists():
        print("Hero (LCP):")
        convert_to_webp(hero, ASSETS, MAX_WIDTH)
    # Priority 2: hero-skyline background (index.html inline CSS)
    skyline = ASSETS / "ai-realestate-3.png"
    if skyline.exists():
        print("Hero skyline bg:")
        convert_to_webp(skyline, ASSETS, MAX_WIDTH)
    # Priority 3: Industry tiles (index.html)
    tiles = [
        "equipment-financing-hero.png", "sba-hero.png", "wcl-hero-operations.png",
        "bloc-hero-business-office.png", "btl-hero.png", "cre-hero.png", "cbl-hero.png",
        "faf-hero.png", "mca-hero.png", "rbf-hero.png", "sbl-hero.png",
        "construction-hero-bg.png", "medical-practices-hero-bg.png",
        "manufacturing-industry-overview.png", "trucking-hero-bg.png",
        "restaurants-hero-bg.png", "logistics-warehousing-hero-bg.png", "forestry-hero-bg.png",
    ]
    print("Industry tiles:")
    for name in tiles:
        p = ASSETS / name
        if p.exists():
            convert_to_webp(p, ASSETS, MAX_TILE)
    # Priority 4: ai-* images (match flow - huge files)
    print("ai-* visuals (match flow):")
    for p in sorted(ASSETS.glob("ai-*.png")):
        convert_to_webp(p, ASSETS, MAX_WIDTH)
    print("Done.")


if __name__ == "__main__":
    main()
