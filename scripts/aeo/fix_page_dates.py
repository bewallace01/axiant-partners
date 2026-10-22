#!/usr/bin/env python3
"""AEO plan 1f: the visible "Updated" date and the JSON-LD dateModified must say the same thing.

87 indexable pages showed one date and declared another. For each, content_dates.py finds
the last commit that changed the page's content (not a sitewide sweep, not AEO Batch 1):

  * dateModified is not newer than that content date (83 pages): the visible "Updated"
    line is set to dateModified. Nothing claims more freshness than the history supports.
  * dateModified is newer than any content change (4 pages): both dateModified (and an
    article:modified_time meta, if present) and the visible line go back to the content date.

Never sets a date to today. Pages with no dateModified at all are left to their generator
(today: the 17 equipment-for-sale pages, which must not be rebuilt until build.py's chrome
carries the tracking tags; see AEO plan section 0.3).

    python scripts/aeo/fix_page_dates.py [--apply]
"""
import datetime
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content_dates  # noqa: E402

ROOT = content_dates.ROOT
SKIP = ("_backup", "_analysis", "_preview", "node_modules", "scripts", "tools", "_components")
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
VISIBLE = re.compile(r"((?:Updated|Last updated)\s*:?\s*(?:<[^>]+>\s*)?)((?:" + MONTHS + r") \d{1,2}, 20\d\d)")
DM = re.compile(r'("dateModified"\s*:\s*")(\d{4}-\d\d-\d\d)(")')
META = re.compile(r'(<meta[^>]+property="article:modified_time"[^>]+content=")(\d{4}-\d\d-\d\d)')


def iso(visible):
    return datetime.datetime.strptime(visible, "%B %d, %Y").date().isoformat()


def human(d):
    dt = datetime.date.fromisoformat(d)
    return f"{dt.strftime('%B')} {dt.day}, {dt.year}"


def main(apply):
    fixed_visible = fixed_both = 0
    for p in ROOT.glob("**/*.html"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP):
            continue
        s = p.read_bytes().decode("utf-8", errors="strict")
        if re.search(r'<meta[^>]+robots[^>]+noindex', s):
            continue
        dms = {m.group(2) for m in DM.finditer(s)}
        vis = {iso(m.group(2)) for m in VISIBLE.finditer(s)}
        if not dms or not vis or (vis & dms):
            continue
        dm = max(dms)
        content = content_dates.content_date(rel)
        if content and dm > content:
            target = content
            new = DM.sub(lambda m: m.group(1) + target + m.group(3), s)
            new = META.sub(lambda m: m.group(1) + target, new)
            fixed_both += 1
            what = f"dateModified {dm} -> {target}, visible -> {human(target)}"
        else:
            target, new = dm, s
            fixed_visible += 1
            what = f"visible {sorted(vis)} -> {human(target)}"
        new = VISIBLE.sub(lambda m: m.group(1) + human(target), new)
        print(f"  {rel}: {what}")
        if apply:
            p.write_bytes(new.encode("utf-8"))
    print(f"\nvisible date set to dateModified: {fixed_visible}; both set back to the content date: {fixed_both}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
