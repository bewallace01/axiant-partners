#!/usr/bin/env python3
"""
Fix blurry hub images on desktop: add 1200w variants and update sizes.
Hub two-column images (ef-intro-img, ef-amounts-img, ef-card-img) were using
560w/800w with sizes=800px - on Retina/hi-DPI displays the browser needs ~1600px
and was upscaling 800w, causing blur. Add 1200w and request it on desktop.
"""
import re
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
CACHE = "v=4"
QUALITY = 85

# Match: srcset with 560w and 800w, sizes with 800px (hub images)
PATTERN = re.compile(
    r'srcset="/assets/([a-zA-Z0-9\-]+)-560w\.webp\?'
    + re.escape(CACHE)
    + r'\s+560w,\s+/assets/\1-800w\.webp\?'
    + re.escape(CACHE)
    + r'\s+800w"\s+sizes="\(max-width:\s*768px\)\s+100vw,\s*800px"',
    re.IGNORECASE,
)

HUB_SIZES = "(max-width: 768px) 100vw, 1200px"


def create_1200w(stem: str) -> bool:
    """Create 1200w variant. Returns True if created or already exists."""
    src = ASSETS / (stem + ".webp")
    out = ASSETS / (stem + "-1200w.webp")
    if out.exists():
        return True
    if not Image or not src.exists():
        return False
    try:
        img = Image.open(src)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        if w <= 800:
            return False
        target_w = min(1200, w)
        ratio = target_w / w
        nw, nh = target_w, int(h * ratio)
        resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
        resized.save(out, "WEBP", quality=QUALITY, method=6)
        print(f"  Created {out.name} ({nw}x{nh})")
        return True
    except Exception as e:
        print(f"  ERROR {stem} 1200w: {e}")
        return False


def main():
    stems = set()
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in PATTERN.finditer(content):
            stems.add(m.group(1))

    if not stems:
        print("No hub images (560w/800w, sizes=800px) found.")
        return

    print(f"Found {len(stems)} hub image stems. Creating 1200w variants...")
    for stem in sorted(stems):
        create_1200w(stem)

    def repl(m):
        stem = m.group(1)
        if (ASSETS / (stem + "-1200w.webp")).exists():
            return (
                f'srcset="/assets/{stem}-560w.webp?{CACHE} 560w, '
                f'/assets/{stem}-800w.webp?{CACHE} 800w, '
                f'/assets/{stem}-1200w.webp?{CACHE} 1200w" sizes="{HUB_SIZES}"'
            )
        return m.group(0)

    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        new_content, n = PATTERN.subn(repl, content)
        if n > 0:
            path.write_text(new_content, encoding="utf-8")
            count += n
            print(f"  Updated: {path.relative_to(ROOT)} ({n} images)")

    print(f"\nDone. Updated {count} hub image srcsets for desktop sharpness.")


if __name__ == "__main__":
    main()
