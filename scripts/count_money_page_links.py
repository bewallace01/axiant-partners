#!/usr/bin/env python3
"""Count the pages that link INTO each money page from their body copy.

Money pages convert AI-assistant traffic, so they need contextual links in from the
pages that discuss the same need. Boilerplate does not count: the shared header, the
footer, the get-matched block, the article rail and the "related" tile grids are stripped
before counting, so only links written into the body copy are left.

    python scripts/count_money_page_links.py            # counts
    python scripts/count_money_page_links.py --list     # plus the linking pages

Target (AEO plan 1c): at least 10 linking pages per money page from OUTSIDE its own
cluster directory (its own spokes link to it by construction). Exits 1 while any is short.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MONEY = [l.strip() for l in (ROOT / "scripts/aeo/money-pages.txt").read_text(encoding="utf-8").splitlines()
         if l.startswith("/")]
SKIP_PARTS = {"node_modules", "_components", "preview", "scripts", "tools", "_analysis", "_outreach", "_marketing"}
STRIP = [
    re.compile(r"<!-- AXIANT-HEADER:START.*?<!-- AXIANT-HEADER:END -->", re.S),
    re.compile(r"<!-- AXIANT-FOOTER:START.*?<!-- AXIANT-FOOTER:END -->", re.S),
    re.compile(r"<!-- AXIANT-GETMATCHED:START.*?<!-- AXIANT-GETMATCHED:END -->", re.S),
    re.compile(r"<head>.*?</head>", re.S),
    re.compile(r"<nav\b.*?</nav>", re.S),
    re.compile(r"<footer\b.*?</footer>", re.S),
    re.compile(r"<aside\b.*?</aside>", re.S),
    re.compile(r"<script\b.*?</script>", re.S),
]


def body(html):
    for p in STRIP:
        html = p.sub("", html)
    return html


def url_of(f):
    rel = "/" + f.relative_to(ROOT).as_posix()
    return rel[: -len("index.html")] if rel.endswith("/index.html") else rel


def main(show):
    pages = [p for p in ROOT.glob("**/*.html") if not (SKIP_PARTS & set(p.relative_to(ROOT).parts))
             and not any(part.startswith("_backup") for part in p.parts)]
    found = {m: [] for m in MONEY}
    for f in pages:
        u = url_of(f)
        try:
            raw = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if re.search(r'<meta[^>]+name="robots"[^>]+noindex', raw):
            continue
        b = body(raw)
        for m in MONEY:
            if u == m:
                continue
            if re.search(r'href="(?:https://axiantpartners\.com)?' + re.escape(m) + r'(?:[#?][^"]*)?"', b):
                found[m].append(u)
    short = 0
    print("all  outside-cluster  money page")
    for m, us in found.items():
        outside = [u for u in us if not u.startswith(cluster_dir(m))]
        short += len(outside) < 10
        print(f"{len(us):3d}  {len(outside):3d}              {m}")
        if show:
            for u in sorted(us):
                print(f"       {'   ' if u.startswith(cluster_dir(m)) else 'out'} {u}")
    return 1 if short else 0


def cluster_dir(money_url):
    """/towing-business-financing.html -> /towing-business-financing/ (its own spokes)."""
    return money_url[:-len(".html")] + "/" if money_url.endswith(".html") else money_url


if __name__ == "__main__":
    sys.exit(main("--list" in sys.argv))
