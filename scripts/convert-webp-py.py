"""Convert PNG/JPG/JPEG in assets/ to WebP. Skips if .webp exists."""
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    exit(1)

ASSETS = Path(__file__).resolve().parent.parent / "assets"
EXT = (".png", ".jpg", ".jpeg")
converted = 0
skipped = 0
errors = 0

for f in ASSETS.iterdir():
    if not f.is_file() or f.suffix.lower() not in EXT:
        continue
    webp = f.with_suffix(".webp")
    if webp.exists():
        skipped += 1
        continue
    try:
        img = Image.open(f)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        elif img.mode != "RGB":
            img = img.convert("RGB")
        img.save(webp, "WEBP", quality=82)
        converted += 1
        print("Created:", webp.name)
    except Exception as e:
        errors += 1
        print("Error", f.name, ":", e)

print(f"Done. Converted {converted}, skipped {skipped}, errors {errors}.")
