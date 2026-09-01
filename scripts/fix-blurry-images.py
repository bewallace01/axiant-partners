#!/usr/bin/env python3
"""Fix blurry hero images: upscale to 1920px width and save at high WebP quality."""
from pathlib import Path
import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("Install Pillow: python -m pip install Pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
TARGET_WIDTH = 1920  # Match common desktop width for sharp display
WEBP_QUALITY = 95    # High quality to reduce compression blur

# Hero/equipment images used as full-width backgrounds
HERO_STEMS = [
    "agriculture-hero-bg", "ai-realestate-3", "alignment-rack-equipment",
    "auto-lift-equipment", "auto-repair-hero-bg", "backhoe-equipment",
    "bloc-hero-business-office", "box-truck-equipment", "brake-lathe-equipment",
    "btl-hero", "bulldozer-equipment", "cbl-hero", "cnc-machine-equipment",
    "combine-equipment", "commercial-dishwasher-equipment", "commercial-kitchen-equipment",
    "commercial-mower-equipment", "commercial-ventilation-equipment", "construction-hero-bg",
    "conveyor-logistics-equipment", "cre-hero", "dental-equipment", "diagnostic-equipment",
    "diagnostic-scan-tool-equipment", "dump-truck-equipment", "dump-truck-excavator-hero",
    "equipment-financing-hero", "exam-equipment", "excavator-equipment", "faf-hero",
    "flatbed-truck-equipment", "forestry-bucket-truck-equipment", "forestry-hero-bg",
    "forestry-log-truck-equipment", "forklift-logistics-equipment", "forklift-manufacturing-equipment",
    "grain-equipment", "hay-baler-equipment", "industrial-robot-equipment",
    "injection-molding-equipment", "lab-equipment-medical", "landscape-trailer-equipment",
    "landscaping-hero-bg", "lathe-equipment", "logistics-warehousing-industry-overview",
    "manufacturing-hero-bg", "mca-hero", "medical-imaging-equipment", "medical-practices-hero-bg",
    "mini-excavator-equipment", "pallet-jack-equipment", "pallet-racking-equipment",
    "press-brake-equipment", "rbf-hero", "reefer-truck-equipment", "restaurant-pos-equipment",
    "restaurant-prep-equipment", "restaurants-hero-bg", "sba-hero", "sbl-hero",
    "semi-truck-equipment", "shop-tools-equipment", "skid-steer-equipment", "sprayer-equipment",
    "stump-grinder-equipment", "surgical-equipment", "tanker-truck-equipment",
    "tire-changer-equipment", "tractor-equipment", "trailer-equipment", "trucking-hero-bg",
    "warehouse-scanner-equipment", "wcl-hero-operations", "wheel-loader-equipment",
    "zero-turn-mower-equipment",
    "contact-hero", "match-hero", "calculator-hero-city", "referral-hero",
    "grain-equipment-hero-bg",
    # Below-hero intro/card images (ef-intro-img, ef-card-img, ef-amounts-img)
    "manufacturing-industry-overview", "manufacturing-intro", "trucking-intro",
    "sba-intro", "sba-7a", "sba-504",
    "faf-intro", "faf-single-family", "faf-multifamily", "faf-condo",
    "faf-purchase-rehab", "faf-distressed", "faf-draw-schedule", "faf-amounts",
    "faf-fast-close", "faf-one-loan", "faf-high-ltv",
    "manufacturing-fleet-equipment", "axiant-hero-branded",
]


def find_source(stem: str) -> Path | None:
    """Find PNG or JPG source for a stem."""
    for ext in (".png", ".jpg", ".jpeg"):
        p = ASSETS / (stem + ext)
        if p.exists():
            return p
    # Try -hero-bg for equipment (e.g. alignment-rack-equipment -> alignment-rack-hero-bg)
    if "-equipment" in stem:
        alt = stem.replace("-equipment", "-hero-bg")
        for ext in (".png", ".jpg"):
            p = ASSETS / (alt + ext)
            if p.exists():
                return p
    return None


def process_hero(stem: str) -> bool:
    """Upscale hero to 1920px width and save as WebP. Returns True if processed."""
    src = find_source(stem)
    if not src:
        return False
    out = ASSETS / (stem + ".webp")
    try:
        img = Image.open(src)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        # Upscale if smaller than target (source is often 1376x768 -> blurry when scaled by browser)
        if w < TARGET_WIDTH:
            ratio = TARGET_WIDTH / w
            nw, nh = TARGET_WIDTH, int(h * ratio)
            img = img.resize((nw, nh), Image.Resampling.LANCZOS)
            # Light sharpen to offset upscale softness
            img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=2))
        img.save(out, "WEBP", quality=WEBP_QUALITY, method=6)
        print(f"  {out.name}")
        return True
    except Exception as e:
        print(f"  ERROR {stem}: {e}")
        return False


def main():
    print("Upscaling hero images to 1920px for sharp display...")
    count = 0
    for stem in HERO_STEMS:
        if process_hero(stem):
            count += 1
    print(f"Done. Processed {count} hero images.")


if __name__ == "__main__":
    main()
