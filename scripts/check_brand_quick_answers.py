#!/usr/bin/env python3
"""Batch 1a acceptance check: every top-cited page and money page names Axiant in its Quick Answer.

When Copilot or an AI Overview quotes a Quick Answer, the quote is all a reader sees. If the
answer never names Axiant Partners, the citation builds no brand. This prints every listed page
whose answer paragraph lacks "Axiant" and exits 1 if there is any (expected: none).

Pages come from scripts/aeo/top25-cited.txt and money-pages.txt (one URL path per line,
# comments allowed). Refresh top25-cited.txt from the Bing AI Performance pages report.

The answer paragraph is the first non-label <p> inside the Quick Answer, which the site marks
up three ways: div.quick-answer (callout or inline-styled), the older div.callout#quick, and a
callout whose eyebrow reads "Quick answer". Money pages without one fall back to p.ef-speakable.

    python scripts/check_brand_quick_answers.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LISTS = [ROOT / "scripts/aeo/top25-cited.txt", ROOT / "scripts/aeo/money-pages.txt"]

CONTAINER = re.compile(
    r'<div[^>]*class="[^"]*\bquick-answer\b[^"]*"[^>]*>'
    r'|<div class="callout" id="quick">'
    r'|<div[^>]*>\s*<p class="eyebrow">Quick answer</p>', re.S)


def page_file(url):
    p = ROOT / url.lstrip("/")
    return p / "index.html" if url.endswith("/") else p


def answer(html):
    for m in CONTAINER.finditer(html):
        if "blog-rail" in m.group(0):
            continue
        for p in re.finditer(r"<p(?: [^>]*)?>(.*?)</p>", html[m.end():], re.S):
            if 'class="eyebrow"' not in p.group(0):
                return p.group(1)
    m = re.search(r'<p class="ef-speakable">(.*?)</p>', html, re.S)
    return m.group(1) if m else None


def main():
    urls = [line.strip() for f in LISTS for line in f.read_text(encoding="utf-8").splitlines()
            if line.startswith("/")]
    missing = 0
    for url in urls:
        f = page_file(url)
        if not f.exists():
            print(f"NO FILE          {url}")
            missing += 1
            continue
        a = answer(f.read_text(encoding="utf-8"))
        if a is None:
            print(f"NO QUICK ANSWER  {url}")
            missing += 1
        elif "Axiant" not in a:
            print(f"NO BRAND         {url}")
            missing += 1
    print(f"{len(urls)} pages checked, {missing} without Axiant in the Quick Answer")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
