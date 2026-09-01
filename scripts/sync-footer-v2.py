#!/usr/bin/env python3
"""Push _components/footer-v2.html into every page carrying the footer markers.

Same single-source trick as sync-header-v2.py. Before this script existed the
footer block claimed to be "shared across v2 pages" but there was no component
and no sync -- 24 inline copies, free to drift exactly the way the old nav did.

Two extra wrinkles this handles:

1. REPAIR. 21 of the 24 pages had AXIANT-FOOTER:START but no :END, so a
   marker-pair regex matched nothing. --repair inserts the missing END
   immediately after the block's </footer>, which is where the three
   correct pages (index, industries, services) already have it.

2. equipment-for-sale/ is GENERATED. Its chrome lives in
   scripts/equipment-for-sale/_chrome.html, which carries the markers and so
   gets synced like any other page -- but the built pages must then be
   regenerated:  python scripts/equipment-for-sale/build.py

Idempotent. Only touches text between the AXIANT-FOOTER markers.
Match by MARKER, not filename -- a filename glob silently matched nothing
after the v2 pages were renamed over the originals.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENT = ROOT / "_components" / "footer-v2.html"
START = "<!-- AXIANT-FOOTER:START"
END = "<!-- AXIANT-FOOTER:END -->"
PATTERN = re.compile(r"<!-- AXIANT-FOOTER:START.*?<!-- AXIANT-FOOTER:END -->", re.S)
SKIP_PARTS = {"node_modules", "_components", "preview", "_backup-pre-v2-swap"}


def pages():
    out = []
    for p in ROOT.glob("**/*.html"):
        if SKIP_PARTS & set(p.parts):
            continue
        try:
            s = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if START in s:
            out.append(p)
    return sorted(set(out))


def repair(dry):
    fixed = already = failed = 0
    for p in pages():
        s = p.read_text(encoding="utf-8")
        if END in s:
            already += 1
            continue
        i = s.index(START)
        j = s.find("</footer>", i)
        if j == -1:
            print(f"  no </footer> after START, skipped: {p.relative_to(ROOT)}")
            failed += 1
            continue
        j += len("</footer>")
        s = s[:j] + "\n" + END + s[j:]
        if not dry:
            p.write_text(s, encoding="utf-8", newline="")
        print(f"  {'would fix' if dry else 'fixed'}: {p.relative_to(ROOT)}")
        fixed += 1
    print(f"repair: {fixed} fixed, {already} already had END, {failed} failed")
    return failed


def sync(dry):
    if not COMPONENT.exists():
        print(f"missing component: {COMPONENT}")
        return 1
    block = COMPONENT.read_text(encoding="utf-8").strip()
    changed = same = nomarker = 0
    for p in pages():
        s = p.read_text(encoding="utf-8")
        if not PATTERN.search(s):
            print(f"  no marker pair, skipped: {p.relative_to(ROOT)}")
            nomarker += 1
            continue
        new = PATTERN.sub(lambda _m: block, s, count=1)
        if new == s:
            same += 1
            continue
        if not dry:
            p.write_text(new, encoding="utf-8", newline="")
        print(f"  {'would update' if dry else 'updated'}: {p.relative_to(ROOT)}")
        changed += 1
    print(f"sync: {changed} changed, {same} already current, {nomarker} unmatched")
    if nomarker:
        print("  -> run with --repair first")
    return 0


if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    rc = 0
    if "--repair" in sys.argv:
        rc |= repair(dry)
    if "--repair-only" not in sys.argv:
        rc |= sync(dry)
    print("\nequipment-for-sale/ is generated -- if scripts/equipment-for-sale/"
          "_chrome.html changed, run:\n  python scripts/equipment-for-sale/build.py")
    sys.exit(rc)
