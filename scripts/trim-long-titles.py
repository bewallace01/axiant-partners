# -*- coding: utf-8 -*-
"""
Get the over-long <title> tags back inside what a SERP actually shows.

283 indexable pages carry a title longer than 60 characters once HTML
entities are unescaped, which is roughly where Google's ~580px cut falls.
282 of them end in "| Axiant" or "| Axiant Partners" - a suffix that is
already being truncated away on every one of those pages, so it is costing
9-17 characters of headline and returning nothing.

The playbook is explicit that the site's number one problem is the CTR leak,
not rankings. A truncated headline is a direct CTR cost on pages that are
already earning impressions, so this is the cheapest lever available.

Stripping the suffix brings 186 titles fully inside the limit and pulls the
remaining 96 from 70-81 characters down to 61-69, where only a word or two
is at risk instead of the whole tail. Those 96 are listed at the end of the
run for a manual pass - shortening them means rewriting the headline, which
is an editorial call, not a mechanical one.

Titles already at or under 60 characters are left alone and keep their
brand suffix. og:title and twitter:title are also left alone: social cards
have far more room and the brand earns its place there.

Run with --apply to write; default is a dry run.
"""
import glob
import html
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("_backup", "_analysis", "_preview", "node_modules", "scripts",
        "tools", "_components")
LIMIT = 60
SUFFIX = re.compile(r"\s*(\||&ndash;|&mdash;|-)\s*Axiant(\s+Partners)?\s*$")


def main(apply_changes):
    trimmed = 0
    still_long = []
    for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(p, ROOT)
        if rel.startswith(SKIP):
            continue
        s = io.open(p, encoding="utf-8").read()
        if 'content="noindex' in s:
            continue
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if not m:
            continue
        raw = re.sub(r"\s+", " ", m.group(1)).strip()
        if len(html.unescape(raw)) <= LIMIT:
            continue
        new = SUFFIX.sub("", raw)
        if new == raw:
            still_long.append((len(html.unescape(raw)), rel, raw))
            continue
        trimmed += 1
        if len(html.unescape(new)) > LIMIT:
            still_long.append((len(html.unescape(new)), rel, new))
        if apply_changes:
            out = s[:m.start()] + "<title>" + new + "</title>" + s[m.end():]
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print(f"  brand suffix trimmed   {trimmed}")
    print(f"  still over {LIMIT} after    {len(still_long)}")
    print("\n  applied" if apply_changes else "\n  dry run - pass --apply")
    if still_long:
        print("\n  these need an editorial rewrite, longest first:\n")
        for n, rel, t in sorted(still_long, reverse=True):
            print(f"    {n:3}  {rel}\n         {t}")


if __name__ == "__main__":
    main("--apply" in sys.argv)
