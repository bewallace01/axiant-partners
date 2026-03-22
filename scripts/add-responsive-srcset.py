#!/usr/bin/env python3
"""Add responsive srcset and sizes to picture elements. Run: python scripts/add-responsive-srcset.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SIZES_CARD = '(max-width: 768px) 100vw, 800px'
SIZES_INDUSTRY = '(max-width: 768px) 100vw, 600px'

def has_variants(stem: str) -> bool:
    return (ASSETS / f"{stem}-400w.webp").exists()

def replace_source(content: str, sizes: str = SIZES_CARD) -> str:
    """Replace <source srcset="/assets/X.webp" type="image/webp"> with responsive srcset."""
    pattern = r'<source srcset="/assets/([^"]+\.webp)" type="image/webp">'
    def repl(m):
        full = m.group(1)
        if not full.endswith('.webp'):
            return m.group(0)
        stem = full[:-5]  # remove .webp
        if not has_variants(stem):
            return m.group(0)
        return (
            f'<source srcset="/assets/{stem}-400w.webp 400w, '
            f'/assets/{stem}-600w.webp 600w, /assets/{stem}-800w.webp 800w, '
            f'/assets/{full}" type="image/webp" sizes="{sizes}">'
        )
    return re.sub(pattern, repl, content)

def main():
    count = 0
    for html in ROOT.rglob("*.html"):
        content = html.read_text(encoding="utf-8")
        if 'srcset="/assets/' not in content or 'type="image/webp"' not in content:
            continue
        new_content = replace_source(content)
        if new_content != content:
            html.write_text(new_content, encoding="utf-8")
            count += 1
            print("Updated:", html.relative_to(ROOT))
    print(f"Done. Updated {count} files.")

if __name__ == "__main__":
    main()
