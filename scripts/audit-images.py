"""Count unused images in assets. Images are 'used' if filename appears in HTML, JS, or CSS."""
import os
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ROOT = ASSETS.parent
EXT = (".png", ".jpg", ".jpeg", ".webp")

# Gather all image files (use base name without ext for matching - e.g. "hero-bg" matches hero-bg.png and hero-bg.webp)
image_basenames = set()
for f in ASSETS.iterdir():
    if f.is_file() and f.suffix.lower() in EXT:
        image_basenames.add(f.stem)

# Search HTML, JS, CSS for references
used = set()
for ext in ("*.html", "*.js", "*.css"):
    for path in ROOT.rglob(ext):
        if "node_modules" in str(path) or ".git" in str(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for base in image_basenames:
            if base in text:
                used.add(base)

unused = image_basenames - used
print(f"Total image files (unique basenames): {len(image_basenames)}")
print(f"Used: {len(used)}")
print(f"Unused: {len(unused)}")
if unused:
    print("\nUnused images (first 50):")
    for b in sorted(unused)[:50]:
        # List which file(s) exist for this base
        existing = [f.name for f in ASSETS.glob(f"{b}.*") if f.suffix.lower() in EXT]
        print(f"  {b} -> {existing}")
