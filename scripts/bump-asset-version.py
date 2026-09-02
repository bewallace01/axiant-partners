#!/usr/bin/env python3
"""Bump the ?v= cache key on axiant-v2.css / axiant-v2.js|article-toc.js across every page.

Rule 6 of the design system says to bump ?v= after editing either asset.
Skipping it is not a harmless omission: on 31 Aug the stylesheet was edited
but the pages kept the previous ?v=, so Chrome served the CACHED old CSS.
The footer markup was the new four-column one while the computed grid was
still the old five-column rule - which reads exactly like a broken build and
is very easy to spend an hour debugging.

Run this after editing axiant-v2.css or axiant-v2.js|article-toc.js, and after the sync
scripts (so component-injected tags get bumped too):

    python scripts/sync-header-v2.py
    python scripts/sync-footer-v2.py
    python scripts/bump-asset-version.py
    python scripts/equipment-for-sale/build.py

Preserves each file's existing line endings - the repo has a CRLF/LF history
and rewriting endings would create a diff of hundreds of files.
"""
import re, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"node_modules", "_backup-pre-v2-swap", ".git"}
PATTERN = re.compile(r"((?:axiant-v2|axiant-v2-chrome|axiant-v2-legacy-body|article-toc)\.(?:css|js)\?v=)[0-9A-Za-z]+")


def main():
    dry = "--dry-run" in sys.argv
    version = time.strftime("%Y%m%d%H%M")
    for a in sys.argv[1:]:
        if not a.startswith("--"):
            version = a

    changed = total = 0
    for p in sorted(ROOT.glob("**/*.html")):
        if SKIP & set(p.parts):
            continue
        raw = p.read_bytes()
        crlf = raw.count(b"\r\n")
        nl = "\r\n" if crlf > (raw.count(b"\n") - crlf) else "\n"
        s = raw.decode("utf-8", errors="ignore").replace("\r\n", "\n")
        new, n = PATTERN.subn(lambda m: m.group(1) + version, s)
        if n:
            total += n
        if n and new != s:
            if not dry:
                p.write_bytes(new.replace("\n", nl).encode("utf-8"))
            changed += 1
    verb = "would bump" if dry else "bumped"
    print("%s %d refs across %d files -> ?v=%s" % (verb, total, changed, version))
    if changed == 0 and total:
        print("  (already at that version)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
