#!/usr/bin/env python3
"""One-off / CI-friendly SEO inventory: titles, canonicals, descriptions, schema hints."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"node_modules", ".git", ".cursor"}

TITLE = re.compile(r"<title>([^<]*)</title>", re.I)
CANON = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', re.I
)
CANON2 = re.compile(
    r'href=["\']([^"\']+)["\'][^>]+rel=["\']canonical["\']', re.I
)
DESC = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', re.I
)
ROBOTS = re.compile(
    r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']*)["\']', re.I
)
OG_IMG = re.compile(
    r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']', re.I
)


def iter_html():
    for p in ROOT.rglob("*.html"):
        if any(x in p.parts for x in SKIP_DIRS):
            continue
        yield p


def main() -> None:
    titles: dict[str, list[str]] = defaultdict(list)
    canon_map: dict[str, list[str]] = defaultdict(list)
    missing_canon: list[str] = []
    relative_canon: list[tuple[str, str]] = []
    short_desc: list[tuple[str, int]] = []
    long_desc: list[tuple[str, int]] = []
    og_relative: list[str] = []
    faq_pages = howto_pages = article_pages = 0
    noindex_count = 0
    pages = 0

    for p in iter_html():
        raw = p.read_text(encoding="utf-8", errors="replace")
        if "<html" not in raw.lower():
            continue
        pages += 1
        rel = str(p.relative_to(ROOT))

        tm = TITLE.search(raw)
        title = tm.group(1).strip() if tm else ""
        if title:
            titles[title].append(rel)

        cm = CANON.search(raw) or CANON2.search(raw)
        if not cm:
            missing_canon.append(rel)
        else:
            u = cm.group(1).strip()
            if not u.startswith("http"):
                relative_canon.append((rel, u))
            canon_map[u].append(rel)

        dm = DESC.search(raw)
        if dm:
            d = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", dm.group(1)))
            L = len(d)
            if L < 70:
                short_desc.append((rel, L))
            if L > 200:
                long_desc.append((rel, L))

        rm = ROBOTS.search(raw)
        if rm and "noindex" in rm.group(1).lower():
            noindex_count += 1

        if '"@type":"FAQPage"' in raw or "'@type': 'FAQPage'" in raw:
            faq_pages += 1
        if '"@type":"HowTo"' in raw and "schema.org" in raw:
            howto_pages += 1
        if '"@type":"Article"' in raw:
            article_pages += 1

        ogm = OG_IMG.search(raw)
        if ogm:
            ogu = ogm.group(1).strip()
            if ogu.startswith("/") and "axiantpartners.com" not in ogu:
                og_relative.append(rel)

    dup_titles = {k: v for k, v in titles.items() if len(v) > 1}
    dup_canon = {k: v for k, v in canon_map.items() if len(v) > 1}

    print("=== SITE SEO INVENTORY ===")
    print(f"HTML files scanned: {pages}")
    print(f"Unique <title> values: {len(titles)}")
    print(f"Duplicate exact titles: {len(dup_titles)}")
    for k, v in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:20]:
        print(f"  ({len(v)}) {k[:78]}")
    print(f"Missing canonical: {len(missing_canon)}")
    if missing_canon[:12]:
        for x in missing_canon[:12]:
            print(f"  - {x}")
    print(f"Non-absolute canonical: {len(relative_canon)}")
    for rel, u in relative_canon[:8]:
        print(f"  - {rel} -> {u[:60]}")
    print(f"Duplicate canonical URL (multiple files): {len(dup_canon)}")
    for k, v in list(dup_canon.items())[:8]:
        print(f"  {k[:70]} -> {len(v)} files")
    print(f"Meta description length <70: {len(short_desc)}")
    print(f"Meta description length >200: {len(long_desc)}")
    print(f"og:image relative path (risk): {len(og_relative)}")
    for x in og_relative[:10]:
        print(f"  - {x}")
    print(f"Pages with noindex robots: {noindex_count}")
    print(f"Pages with FAQPage JSON-LD: {faq_pages}")
    print(f"Pages with HowTo JSON-LD: {howto_pages}")
    print(f"Files containing Article JSON-LD: {article_pages}")
    print()
    print("=== META DESCRIPTION OUTLIERS (sample) ===")
    for rel, L in sorted(short_desc, key=lambda x: x[1])[:25]:
        print(f"  short ({L}): {rel}")
    for rel, L in sorted(long_desc, key=lambda x: -x[1])[:25]:
        print(f"  long ({L}): {rel}")


if __name__ == "__main__":
    main()
