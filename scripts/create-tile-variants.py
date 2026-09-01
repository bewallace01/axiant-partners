#!/usr/bin/env python3
"""Create 560w and 800w WebP variants for industry tile images (displayed at ~280-565px)."""
from pathlib import Path
import sys

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: python -m pip install Pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
TILE_SIZES = (560, 800)  # 560w for mobile, 800w for tablet/desktop
QUALITY = 85  # Slightly lower for tiles to reduce file size

TILE_IMAGES = [
    "equipment-financing-hero", "sba-hero", "wcl-hero-operations",
    "bloc-hero-business-office", "btl-hero", "cre-hero", "cbl-hero",
    "faf-hero", "mca-hero", "rbf-hero", "sbl-hero",
    "construction-hero-bg", "medical-practices-hero-bg", "manufacturing-hero-bg",
    "manufacturing-industry-overview", "trucking-hero-bg", "restaurants-hero-bg",
    "logistics-warehousing-hero-bg", "logistics-warehousing-industry-overview",
    "forestry-hero-bg", "agriculture-hero-bg", "landscaping-hero-bg", "auto-repair-hero-bg",
]


def main():
    print("Creating tile variants (560w, 800w) for industry tiles...")
    for stem in TILE_IMAGES:
        src = ASSETS / (stem + ".webp")
        if not src.exists():
            continue
        try:
            img = Image.open(src)
            if img.mode in ("RGBA", "LA", "P"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")
            w, h = img.size
            for target_w in TILE_SIZES:
                if w <= target_w:
                    continue
                out = ASSETS / (stem + f"-{target_w}w.webp")
                ratio = target_w / w
                nw, nh = target_w, int(h * ratio)
                resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
                resized.save(out, "WEBP", quality=QUALITY, method=6)
                size_kb = out.stat().st_size / 1024
                print(f"  {out.name} ({nw}x{nh}) {size_kb:.0f}KB")
        except Exception as e:
            print(f"  ERROR {stem}: {e}")
    print("Done.")


if __name__ == "__main__":
    main()
