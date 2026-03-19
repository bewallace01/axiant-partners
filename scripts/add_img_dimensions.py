#!/usr/bin/env python3
"""Add width/height to nav logos that lack them. Run from project root."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIMS = ' width="180" height="74"'

def fix_file(p: Path) -> bool:
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text
    # Only add if not already present (avoid duplicates)
    if 'width="180" height="74"' in text:
        return False
    text = text.replace('class="nav-logo nav-logo-light">', 'class="nav-logo nav-logo-light"' + DIMS + '>')
    text = text.replace('class="nav-logo nav-logo-dark">', 'class="nav-logo nav-logo-dark"' + DIMS + '>')
    if text != orig:
        p.write_text(text, encoding="utf-8", newline="")
        return True
    return False

count = 0
for f in ROOT.rglob("*.html"):
    if fix_file(f):
        count += 1
        print(f"Updated: {f.relative_to(ROOT)}")
print(f"Done. Updated {count} files.")
