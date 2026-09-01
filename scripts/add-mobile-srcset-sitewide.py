#!/usr/bin/env python3
"""Add responsive srcset (560w/800w) to ALL picture elements sitewide for mobile performance."""
import re
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
CACHE = "v=4"
SIZES = "(max-width: 768px) 100vw, 800px"
TILE_SIZES = (560, 800)
QUALITY = 85


def collect_stems_from_html():
    """Find all unique stems used in single-source srcset (no width descriptors)."""
    stems = set()
    single_src = re.compile(r'srcset="/assets/([a-zA-Z0-9\-]+)\.webp\?' + re.escape(CACHE) + r'"')
    for path in ROOT.rglob("*.html"):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for m in single_src.finditer(content):
            stem = m.group(1)
            # Skip if this file already has responsive srcset for this stem
            if f"{stem}-560w" in content or f"{stem}-800w" in content:
                continue
            # Skip stems that are hero backgrounds used in CSS url() - those stay full-size
            stems.add(stem)
    return stems


def create_variant(src_path: Path, stem: str, target_w: int) -> bool:
    """Create 560w or 800w WebP variant. Returns True if created."""
    if not Image:
        return False
    out = ASSETS / (stem + f"-{target_w}w.webp")
    if out.exists():
        return False
    try:
        img = Image.open(src_path)
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")
        w, h = img.size
        if w <= target_w:
            return False
        ratio = target_w / w
        nw, nh = target_w, int(h * ratio)
        resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
        resized.save(out, "WEBP", quality=QUALITY, method=6)
        return True
    except Exception as e:
        print(f"  ERROR {stem} {target_w}w: {e}")
        return False


def ensure_variants(stems: set) -> set:
    """Create 560w/800w variants for stems that need them. Return stems that have both."""
    if not Image:
        print("Pillow not installed; skip variant creation. Run: python -m pip install Pillow")
        return {s for s in stems if (ASSETS / (s + "-560w.webp")).exists() and (ASSETS / (s + "-800w.webp")).exists()}
    ready = set()
    for stem in sorted(stems):
        src = ASSETS / (stem + ".webp")
        if not src.exists():
            continue
        created = False
        for tw in TILE_SIZES:
            if create_variant(src, stem, tw):
                created = True
                print(f"  Created {stem}-{tw}w.webp")
        v560 = (ASSETS / (stem + "-560w.webp")).exists()
        v800 = (ASSETS / (stem + "-800w.webp")).exists()
        if v560 and v800:
            ready.add(stem)
        elif not v560 and not v800:
            # Source may be small; use original as fallback - still add to ready for single-source upgrade
            # We'll use responsive only when both exist; otherwise skip
            pass
        elif src.stat().st_size > 0:
            # Has one but not both - create the missing one
            for tw in TILE_SIZES:
                if not (ASSETS / (stem + f"-{tw}w.webp")).exists():
                    if create_variant(src, stem, tw):
                        created = True
            if (ASSETS / (stem + "-560w.webp")).exists() and (ASSETS / (stem + "-800w.webp")).exists():
                ready.add(stem)
    return ready


def replace_srcset(content: str, stems: set) -> tuple[str, int]:
    """Replace single srcset with responsive srcset for given stems."""
    count = 0
    for stem in stems:
        old = f'srcset="/assets/{stem}.webp?{CACHE}"'
        if old not in content:
            continue
        if f"{stem}-560w" in content or f"{stem}-800w" in content:
            continue
        new = f'srcset="/assets/{stem}-560w.webp?{CACHE} 560w, /assets/{stem}-800w.webp?{CACHE} 800w" sizes="{SIZES}"'
        n = content.count(old)
        content = content.replace(old, new)
        count += n
    return content, count


def main():
    print("1. Collecting stems from HTML (single-source srcset)...")
    stems = collect_stems_from_html()
    print(f"   Found {len(stems)} unique stems")

    print("2. Ensuring 560w/800w variants exist...")
    ready = set()
    for stem in sorted(stems):
        src = ASSETS / (stem + ".webp")
        v560 = ASSETS / (stem + "-560w.webp")
        v800 = ASSETS / (stem + "-800w.webp")
        if not src.exists():
            continue
        if v560.exists() and v800.exists():
            ready.add(stem)
            continue
        if Image:
            for tw in TILE_SIZES:
                out = ASSETS / (stem + f"-{tw}w.webp")
                if not out.exists():
                    try:
                        img = Image.open(src)
                        if img.mode in ("RGBA", "LA", "P"):
                            img = img.convert("RGBA")
                        else:
                            img = img.convert("RGB")
                        w, h = img.size
                        if w > tw:
                            ratio = tw / w
                            nw, nh = tw, int(h * ratio)
                            resized = img.resize((nw, nh), Image.Resampling.LANCZOS)
                            resized.save(out, "WEBP", quality=QUALITY, method=6)
                            print(f"   Created {out.name}")
                    except Exception as e:
                        print(f"   ERROR {stem}: {e}")
            if v560.exists() and v800.exists():
                ready.add(stem)
        else:
            if v560.exists() and v800.exists():
                ready.add(stem)
    print(f"   {len(ready)} stems have 560w+800w variants")

    print("3. Replacing srcset in all HTML files...")
    total = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"   Skip {path}: {e}")
            continue
        new_content, count = replace_srcset(content, ready)
        if count > 0:
            path.write_text(new_content, encoding="utf-8")
            rel = path.relative_to(ROOT)
            print(f"   {rel}: {count} replacements")
            total += count
    print(f"\nDone. Updated {total} picture srcsets sitewide for mobile.")


if __name__ == "__main__":
    main()
