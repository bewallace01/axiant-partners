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


def create_responsive_hero(src: Path, out_dir: Path) -> None:
    """Create 600w and 900w variants for mobile/tablet srcset."""
    if not src.exists():
        return
    try:
        img = Image.open(src)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        for target_w in (600, 900):
            if w <= target_w:
                continue
            ratio = target_w / w
            nw, nh = target_w, int(h * ratio)
            resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
            out = out_dir / (src.stem + f"-{target_w}w.webp")
            resized.save(out, "WEBP", quality=WEBP_QUALITY, method=6)
            print(f"  {out.name} ({nw}x{nh})")
    except Exception as e:
        print(f"  ERROR: {e}")


def main():
    print("Optimizing images...")
    # Priority 1: LCP hero (index.html) + responsive sizes for mobile
    hero = ASSETS / "dump-truck-excavator-hero.png"
    hero_webp = ASSETS / "dump-truck-excavator-hero.webp"
    if hero.exists():
        print("Hero (LCP):")
        convert_to_webp(hero, ASSETS, MAX_WIDTH)
        print("Hero responsive (mobile/tablet):")
        create_responsive_hero(hero_webp if hero_webp.exists() else hero, ASSETS)
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
    # Priority 5: Axel avatar (170KB PNG displayed ~40x60 - create 96px WebP)
    axel = ROOT / "axel-loan-lion.png"
    if axel.exists():
        print("Axel avatar (chatbot):")
        convert_to_webp(axel, ROOT, 96)
    # Priority 6: ai-howitworks/ai-growth small variants (displayed ~226x126 on index)
    for stem in ["ai-howitworks-1", "ai-howitworks-2", "ai-howitworks-3", "ai-howitworks-4", "ai-growth-2"]:
        src = ASSETS / f"{stem}.webp"
        if not src.exists():
            src = ASSETS / f"{stem}.png"
        if src.exists():
            create_responsive_small(src, ASSETS, 450)
    print("Done.")


def create_responsive_small(src: Path, out_dir: Path, max_w: int) -> None:
    """Create small variant for images displayed at ~226x126."""
    out = out_dir / (src.stem + f"-{max_w}w.webp")
    if out.exists():
        return
    try:
        img = Image.open(src)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        if w <= max_w:
            return
        ratio = max_w / w
        nw, nh = max_w, int(h * ratio)
        resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
        resized.save(out, "WEBP", quality=WEBP_QUALITY, method=6)
        print(f"  {out.name} ({nw}x{nh})")
    except Exception as e:
        print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
