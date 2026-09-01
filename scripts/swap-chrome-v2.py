#!/usr/bin/env python3
"""Give a legacy page the v2 header and footer without touching its body.

The calculators, the matcher, the get-matched flows and the print pieces are
hand-built and interactive: running the page converter over them stripped
their widgets, so they were restored from backup - which also restored the old
navigation. This swaps only the chrome:

  * remove the legacy .mobile-nav-overlay and nav.main-nav
  * replace footer.site-footer with the v2 footer component
  * insert the v2 header component (with its mobile menu and axiant-v2.js)
  * add axiant-v2.css LAST in <head> so it wins any tie with the old CSS

Everything else - forms, calculators, inline scripts, their own stylesheets -
is left exactly as it is. Idempotent: a page that already carries the markers
is skipped.
"""
import re, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
HEADER = (ROOT / "_components" / "header-v2.html").read_text(encoding="utf-8").strip()
FOOTER = (ROOT / "_components" / "footer-v2.html").read_text(encoding="utf-8").strip()
VERSION = re.search(r"axiant-v2\.css\?v=(\d+)", (ROOT / "index.html").read_text(encoding="utf-8"))
VERSION = VERSION.group(1) if VERSION else "1"

def swap(rel):
    f = ROOT / rel
    html = f.read_text(encoding="utf-8")
    if "AXIANT-HEADER:START" in html:
        return "skip (already v2 chrome)"
    soup = BeautifulSoup(html, "html.parser")
    if soup.body is None:
        return "skip (no <body>)"
    # An iframe payload has no chrome of its own and must not gain any:
    # calculator-embed.html is what other pages embed.
    if not soup.select("nav.main-nav") and not soup.select(".mobile-nav-overlay"):
        return "skip (embed payload - no chrome to replace)"

    removed = 0
    for sel in (".mobile-nav-overlay", "nav.main-nav", ".nav-links", ".mobile-menu-toggle"):
        for el in soup.select(sel):
            el.decompose(); removed += 1
    for foot in soup.select("footer.site-footer"):
        foot.decompose(); removed += 1

    # header first in <body>, footer last before the scripts
    head_frag = BeautifulSoup(HEADER, "html.parser")
    for node in reversed(list(head_frag.contents)):
        soup.body.insert(0, node)
    # Append at the very end. Anchoring to the first <script> child put the
    # footer above the page content on every one of these pages - they all
    # carry an analytics script near the top of <body>.
    foot_frag = BeautifulSoup(FOOTER, "html.parser")
    for node in list(foot_frag.contents):
        soup.body.append(node)

    # The old stylesheet uses !important on bare `header` inside its mobile
    # media queries, and puts an animation on <body> that makes body the
    # containing block for fixed children. axiant-v2.css is deliberately
    # !important-free, so the counter-override is scoped to these pages only.
    if soup.head is not None and "v2-legacy-chrome" not in html:
        fix = soup.new_tag("style", id="v2-legacy-chrome")
        fix.string = (
            "/* Page-scoped: this page keeps the pre-v2 stylesheet for its body, "
            "and that sheet marks `header{padding}` !important and animates <body>. */\n"
            "body > header.header{padding:0 !important;background-image:none !important;"
            "min-height:0 !important;text-align:left !important}\n"
            "body[data-menu-open=\"true\"]{transform:none !important;animation:none !important}\n"
            "body > .footer{padding:0 !important;background-image:none !important}")
        soup.head.append(fix)

    # NOT axiant-v2.css: the two sheets share generic class names (.container is
    # the white content card on these pages) and nine CSS variables, so loading
    # it flattened their layouts. axiant-v2-chrome.css carries only the header,
    # menu and footer, with tokens scoped to the chrome roots.
    if soup.head is not None and "axiant-v2-chrome.css" not in html:
        link = soup.new_tag("link", rel="stylesheet",
                            href="/axiant-v2-chrome.css?v=%s" % VERSION)
        soup.head.append(link)

    f.write_text(str(soup), encoding="utf-8")
    return "swapped (%d legacy nodes removed)" % removed

if __name__ == "__main__":
    targets = sys.argv[1:]
    if not targets:
        targets = []
        for p in sorted(ROOT.rglob("*.html")):
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith("_") or "/_" in rel or rel.startswith(("node_modules/", "tools/")):
                continue
            if "/fragments/" in rel:
                continue
            t = p.read_text(encoding="utf-8", errors="ignore")
            if "AXIANT-HEADER:START" in t:
                continue
            if "mobile-nav-overlay" in t or 'class="main-nav"' in t:
                targets.append(rel)
    for rel in targets:
        print("  %-46s %s" % (rel[:44], swap(rel)))
