#!/usr/bin/env python3
"""Push _components/header-v2.html into every *-v2.html page.

The site has no build step and no include mechanism, which is why the old
nav markup is copy-pasted across 849 files and drifts (hence branches like
"fix(nav): catch ALL nav variants"). This makes the header single-source:
edit the component, run this, every v2 page updates.

Idempotent. Only touches text between the AXIANT-HEADER markers.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENT = ROOT / "_components" / "header-v2.html"
PATTERN = re.compile(
    r"<!-- AXIANT-HEADER:START.*?<!-- AXIANT-HEADER:END -->", re.S)

def main():
    if not COMPONENT.exists():
        print(f"missing component: {COMPONENT}"); return 1
    block = COMPONENT.read_text(encoding="utf-8").strip()

    # Match by MARKER, not filename. The v2 pages were renamed over the
    # originals (index-v2.html -> index.html), which silently made a
    # filename-based glob match nothing.
    pages = [p for p in ROOT.glob("**/*.html")
             if PATTERN.search(p.read_text(encoding="utf-8", errors="ignore"))]
    pages = sorted(set(p for p in pages
                      if "node_modules" not in p.parts
                      and "_components" not in p.parts
                      and "preview" not in p.parts))
    if not pages:
        print("no *-v2.html pages found"); return 1

    changed = skipped = nomarker = 0
    for p in pages:
        s = p.read_text(encoding="utf-8")
        if not PATTERN.search(s):
            print(f"  no markers, skipped: {p.relative_to(ROOT)}"); nomarker += 1; continue
        new = PATTERN.sub(lambda _: block, s)
        if new != s:
            p.write_text(new, encoding="utf-8", newline="\n"); changed += 1
            print(f"  updated: {p.relative_to(ROOT)}")
        else:
            skipped += 1
    print(f"\n{changed} updated, {skipped} already current, {nomarker} without markers")
    return 0

if __name__ == "__main__":
    sys.exit(main())
