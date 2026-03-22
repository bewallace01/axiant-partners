#!/usr/bin/env python3
"""Revert responsive srcset back to simple full-size webp for sharper images."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    # Match: /assets/STEM-400w.webp 400w, ... /assets/STEM-600w.webp 600w, ... /assets/STEM-800w.webp 800w, ... /assets/STEM.webp"
    pattern = re.compile(
        r'<source srcset="/assets/(.+)-400w\.webp 400w, '
        r'/assets/\1-600w\.webp 600w, /assets/\1-800w\.webp 800w, '
        r'/assets/\1\.webp" type="image/webp" sizes="[^"]*">'
    )
    def repl(m):
        return f'<source srcset="/assets/{m.group(1)}.webp" type="image/webp">'

    count = 0
    for html in ROOT.rglob("*.html"):
        content = html.read_text(encoding="utf-8")
        if '-400w.webp 400w' not in content:
            continue
        new_content = pattern.sub(repl, content)
        if new_content != content:
            html.write_text(new_content, encoding="utf-8")
            count += 1
            print("Reverted:", html.relative_to(ROOT))
    print(f"Done. Reverted {count} files.")

if __name__ == "__main__":
    main()
