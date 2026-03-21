"""Add WebP-first <source> to all picture/img elements. Keeps PNG/JPG as fallback."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
EXT_MAP = {".png": ".webp", ".jpg": ".webp", ".jpeg": ".webp"}

# Gather existing WebP files in assets
webp_stems = set()
for f in ASSETS.iterdir():
    if f.is_file() and f.suffix.lower() == ".webp":
        webp_stems.add(f.stem)

def has_webp(basename: str) -> bool:
    return basename in webp_stems

def process_html(content: str) -> tuple[str, int]:
    """Add WebP source before img when WebP exists. Returns (new_content, edit_count)."""
    count = 0

    # Pattern 1: <picture>...<img ... src="/assets/foo.png" ...> - add source before img
    # Match picture with img that has src to /assets/*.png|jpg|jpeg
    def add_source(m):
        nonlocal count
        full = m.group(0)
        src = m.group(1)  # e.g. /assets/foo.png
        path = Path(src)
        stem = path.stem
        if not has_webp(stem):
            return full
        # Already has source type="image/webp"?
        if 'type="image/webp"' in full or "type='image/webp'" in full:
            return full
        webp_src = str(path.with_suffix(".webp")).replace("\\", "/")
        picture_tag, img_tag = m.group(1), m.group(2)
        new = picture_tag + f'<source srcset="{webp_src}" type="image/webp">' + img_tag
        count += 1
        return new

    # <picture ...><img ... src="/assets/xxx.png" ...>
    # Allow flexible whitespace and attributes between picture and img
    p1 = re.compile(
        r'(<picture[^>]*>)\s*(<img\s[^>]*?src=["\'](/assets/[^"\']+\.(?:png|jpg|jpeg))["\'][^>]*>)',
        re.IGNORECASE | re.DOTALL
    )
    content = p1.sub(add_source, content)

    # Pattern 2: Standalone <img src="/assets/foo.png"> - wrap in picture. Skip if already has WebP source.
    def replace_standalone(m):
        nonlocal count
        img_tag = m.group(0)
        start = m.start()
        preceding = content[max(0,start-200):start]
        if 'type="image/webp"' in preceding and 'srcset=' in preceding:
            return img_tag  # already has webp source
        src = m.group(1)
        path = Path(src)
        stem = path.stem
        if not has_webp(stem):
            return img_tag
        webp_src = str(path.with_suffix(".webp")).replace("\\", "/")
        count += 1
        return f'<picture><source srcset="{webp_src}" type="image/webp">{img_tag}</picture>'

    p2 = re.compile(
        r'<img\s[^>]*?src=["\'](/assets/[^"\']+\.(?:png|jpg|jpeg))["\'][^>]*>',
        re.IGNORECASE
    )
    content = p2.sub(replace_standalone, content)

    # Pattern 3: preload href="/assets/foo.png" -> href="/assets/foo.webp" type="image/webp"
    def fix_preload(m):
        nonlocal count
        src = m.group(1)
        path = Path(src)
        if not has_webp(path.stem):
            return m.group(0)
        webp_src = str(path.with_suffix(".webp")).replace("\\", "/")
        count += 1
        return f'<link rel="preload" href="{webp_src}" as="image" type="image/webp">'

    p3 = re.compile(
        r'<link\s+rel="preload"\s+href="(/assets/[^"]+\.(?:png|jpg|jpeg))"\s+as="image"\s*/?>',
        re.IGNORECASE
    )
    content = p3.sub(fix_preload, content)

    # Pattern 4: CSS url('/assets/foo.png') -> image-set for WebP-first with PNG fallback
    def fix_css_url(m):
        nonlocal count
        src = m.group(1)
        path = Path(src)
        if not has_webp(path.stem):
            return m.group(0)
        webp_src = str(path.with_suffix(".webp")).replace("\\", "/")
        if "image-set" in m.group(0):
            return m.group(0)  # already done
        count += 1
        return f"image-set(url('{webp_src}') type('image/webp'), url('{src}') type('image/png'))"

    p4 = re.compile(
        r"url\('(/assets/[^']+\.(?:png|jpg|jpeg))'\)",
        re.IGNORECASE
    )
    content = p4.sub(fix_css_url, content)

    return content, count

def main():
    total = 0
    for path in ROOT.rglob("*.html"):
        if "node_modules" in str(path) or ".git" in str(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        new_text, n = process_html(text)
        if n > 0:
            path.write_text(new_text, encoding="utf-8")
            total += n
            print(f"  {path.relative_to(ROOT)}: {n} images")
    print(f"Total: {total} images updated to WebP-first")

if __name__ == "__main__":
    main()
