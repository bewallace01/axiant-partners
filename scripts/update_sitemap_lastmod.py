#!/usr/bin/env python3
"""Refresh <lastmod> in sitemap.xml from git history, changing nothing else.

Why not generate_sitemap.py: that script enumerates a hand-maintained page list
which has drifted 188 URLs behind the site, so running it would drop whole
sections. This edits the committed sitemap in place and asserts the URL set is
untouched.

Why it matters: 400 of 764 entries read 2026-04 while the pages themselves had
been rewritten the week before. lastmod is the main signal Google uses to decide
whether a known page is worth re-fetching, and 90 pages sitting in "Crawled -
currently not indexed" were all carrying stale dates. A sitemap that under-reports
change asks Google not to look again.

Dates come from the last commit touching each file rather than mtime, so a fresh
clone does not date the whole site to the checkout.
"""
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SITEMAP = BASE / "sitemap.xml"
APPLY = "--apply" in sys.argv


def git_dates():
    out = subprocess.run(
        ["git", "log", "--name-only", "--date=short", "--format=%ad"],
        cwd=BASE, capture_output=True, text=True, timeout=180,
    ).stdout
    dates, cur = {}, None
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) == 10 and line[4] == "-" and line[7] == "-":
            cur = line
        elif cur and line not in dates:
            dates[line] = cur      # newest-first, so the first sighting wins
    return dates


def to_file(url):
    p = re.sub(r"^https?://(www\.)?axiantpartners\.com", "", url).lstrip("/")
    if p == "":
        return "index.html"
    if p.endswith("/"):
        return p + "index.html"
    if p.endswith(".html"):
        return p
    return p + "/index.html"


raw = SITEMAP.read_bytes().decode("utf-8")
before = raw
dates = git_dates()

locs_before = re.findall(r"<loc>([^<]+)</loc>", raw)
lm_before = re.findall(r"<lastmod>([^<]+)</lastmod>", raw)
if len(locs_before) != len(lm_before):
    sys.exit(f"{len(locs_before)} <loc> but {len(lm_before)} <lastmod>; not 1:1")

changed = missing = 0
out_parts, pos = [], 0
for m in re.finditer(r"<loc>([^<]+)</loc>(\s*)<lastmod>([^<]+)</lastmod>", raw):
    url, gap, old = m.group(1), m.group(2), m.group(3)
    rel = to_file(url)
    new = dates.get(rel)
    if new is None:
        missing += 1
        continue
    if new == old:
        continue
    out_parts.append((m.start(3), m.end(3), new))
    changed += 1

for start, end, new in reversed(out_parts):
    raw = raw[:start] + new + raw[end:]

# ------------------------------------------------------------ assertions
locs_after = re.findall(r"<loc>([^<]+)</loc>", raw)
if locs_after != locs_before:
    sys.exit("URL list changed; refusing to write")
if len(re.findall(r"<lastmod>", raw)) != len(lm_before):
    sys.exit("lastmod count changed; refusing to write")
stripped_before = re.sub(r"<lastmod>[^<]+</lastmod>", "<lastmod/>", before)
stripped_after = re.sub(r"<lastmod>[^<]+</lastmod>", "<lastmod/>", raw)
if stripped_before != stripped_after:
    sys.exit("something other than lastmod changed; refusing to write")
import xml.etree.ElementTree as ET
ET.fromstring(raw)

lm_after = re.findall(r"<lastmod>([^<]+)</lastmod>", raw)
print(f"URLs                : {len(locs_after)} (unchanged)")
print(f"lastmod updated     : {changed}")
print(f"no git date found   : {missing}")
print(f"before              : {Counter(d[:7] for d in lm_before).most_common()}")
print(f"after               : {Counter(d[:7] for d in lm_after).most_common()}")
print(f"XML parses          : yes")
if APPLY:
    SITEMAP.write_bytes(raw.encode("utf-8"))
    print("  WRITTEN")
