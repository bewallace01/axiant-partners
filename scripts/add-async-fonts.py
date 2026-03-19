#!/usr/bin/env python3
"""Add async font loading to HTML files that include critical.css. Run once."""
import re
from pathlib import Path

FONT_LINK = (
    '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@400;600&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
    '    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@400;600&display=swap"></noscript>\n'
)
BASE = Path(__file__).resolve().parent.parent
PATTERN = re.compile(
    r'(<link rel="stylesheet" href="[^"]*critical\.css[^"]*">)',
    re.IGNORECASE
)
REPLACEMENT = FONT_LINK + r'    \1'

def main():
    count = 0
    for path in BASE.rglob("*.html"):
        if "node_modules" in str(path) or ".git" in str(path):
            continue
        text = path.read_text(encoding="utf-8")
        if "critical.css" not in text or FONT_LINK.strip()[:50] in text:
            continue
        new_text = PATTERN.sub(REPLACEMENT, text, count=1)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            count += 1
            print(path.relative_to(BASE))
    print(f"\nUpdated {count} files")

if __name__ == "__main__":
    main()
