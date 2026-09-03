#!/usr/bin/env python3
"""Swap the hatched .aside-mark panels for real photos.

    python scripts/apply-aside-photos.py            # apply every photo that exists
    python scripts/apply-aside-photos.py --dry-run  # report only

Reads _photo-manifest/aside-photos.csv. For each row whose target_filename
exists on disk, replaces that page's Nth .aside-mark with an <img>. Slots with
no file keep the hatched fallback, so this is safe to run after generating five
photos or all 113.

Idempotent: a slot already carrying an <img> is skipped, so re-running after
adding more photos only touches the new ones.
"""
import csv, re, sys, os, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DRY  = "--dry-run" in sys.argv
MAN  = os.path.join(ROOT, "_photo-manifest", "aside-photos.csv")

rows = list(csv.DictReader(open(MAN, encoding="utf-8")))
by_page = collections.defaultdict(list)
for r in rows:
    page = r["page_url"].lstrip("/") or "index.html"
    if not page.endswith(".html"):
        page = page.rstrip("/") + "/index.html"
    by_page[page].append(r)

applied = missing = skipped = 0
for page, entries in sorted(by_page.items()):
    path = os.path.join(ROOT, page)
    if not os.path.exists(path):
        print("  page not found: " + page); continue
    s = open(path, encoding="utf-8", errors="replace").read()
    orig = s
    spans = list(re.finditer(r'<div[^>]*class="aside-mark[^"]*"[^>]*>.*?</div>', s, re.S))
    out, changed = [], 0
    for i, m in enumerate(spans):
        if i >= len(entries): break
        r = entries[i]
        img = r["target_filename"]
        if "<img" in m.group(0):
            skipped += 1; continue
        if not os.path.exists(os.path.join(ROOT, img)):
            missing += 1; continue
        alt = r["section_heading"].replace(chr(34), "&quot;")[:110]
        new = ('<div aria-hidden="true" class="aside-mark has-photo">'
               '<img src="/' + img + '" alt="' + alt + '" loading="lazy" '
               'decoding="async" width="1064" height="480"></div>')
        out.append((m.start(), m.end(), new)); changed += 1
    if out:
        buf, last = [], 0
        for a, b, n in out:
            buf.append(s[last:a]); buf.append(n); last = b
        buf.append(s[last:]); s = "".join(buf)
    if s != orig:
        applied += changed
        if not DRY:
            open(path, "w", encoding="utf-8", newline="").write(s)
        print(("  would apply " if DRY else "  applied ") + str(changed) + "  " + page)

print("")
print("photos applied          : " + str(applied))
print("slots waiting on a file : " + str(missing))
print("slots already done      : " + str(skipped))
