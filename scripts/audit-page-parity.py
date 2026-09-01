#!/usr/bin/env python3
"""Prove a v2 conversion kept the content, not just the markup.

Written after a real failure on 1 Sep 2026: business-growth.html was converted,
verified (15 prose blocks, 24 cards, every link 200), shipped -- and four
sections had lost their entire body copy. 530 words gone from a page that
generates leads. Empty containers pass a structural check perfectly.

So this compares CONTENT, backup vs converted, and fails loudly:

  words        drift over the tolerance (default 2%)     FAIL
  json-ld      block count changed                       FAIL
  h1           text changed                              FAIL
  title        changed                                   FAIL
  canonical    changed                                   FAIL
  description  changed                                   FAIL
  links        an internal href present before, gone now FAIL
  h2 set       headings added or removed                 WARN (often deliberate)
  images       fewer <img> than before                   WARN

Site chrome is stripped from both sides first -- the legacy nav/footer and the
v2 nav/footer are supposed to differ, and comparing them would drown the signal.

Usage:
    python scripts/audit-page-parity.py                     # every backup pair
    python scripts/audit-page-parity.py faq.html blog.html  # named pages
    python scripts/audit-page-parity.py --tolerance 5
    python scripts/audit-page-parity.py --verbose           # list what changed

Exit code is 1 if anything FAILs, so it can gate a merge.
Standard library only -- no bs4, nothing to install.
"""
import sys, re, html
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUP = ROOT / "_backup-pre-v2-swap"

def live_for(name):
    """equipment__excavators.html in the backup is equipment/excavators/index.html live."""
    if "__" in name:
        return ROOT.joinpath(*name[:-5].split("__")) / "index.html"
    if (ROOT / name).exists():
        return ROOT / name
    if (ROOT / name[:-5] / "index.html").exists():
        return ROOT / name[:-5] / "index.html"
    return ROOT / name


# subtrees that are site chrome on either the legacy or the v2 side
CHROME_CLASSES = {
    # the pre-v2 landing and article templates
    "nv", "nv-in", "ft", "bk-foot", "topbar", "site-nav",
    # rail furniture: the quick-facts card was removed by design once every
    # article gained a quick answer saying the same thing
    "blog-rail-quick-content", "blog-rail-quick", "article-rail__block--quick",
    "main-nav", "mobile-nav-overlay", "mobile-overlay-links", "site-footer",
    "mobile-cta-bar", "nav-links", "utility", "header", "mobile-menu",
    "footer", "nav-dropdown-menu",
}
SKIP_TAGS = {"script", "style", "noscript", "svg"}
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "area", "base", "col", "embed"}


class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []            # (tag, is_chrome)
        self.depth_skip = 0        # inside chrome or script
        self.text = []
        self.links = set()
        self.h1 = []
        self.h2 = []
        self.imgs = 0
        self.jsonld = 0
        self.title = None
        self.canonical = None
        self.description = None
        self._grab = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        chrome = bool(classes & CHROME_CLASSES) or (tag == "footer" and not classes)
        if tag in SKIP_TAGS or self.depth_skip:
            if tag == "script" and a.get("type") == "application/ld+json" and not self.depth_skip:
                self.jsonld += 1
            if tag not in VOID:
                self.depth_skip += 1
                self.stack.append((tag, True))
            return
        if tag == "link" and "canonical" in (a.get("rel") or ""):
            self.canonical = (a.get("href") or "").strip()
        if tag == "meta" and (a.get("name") or "").lower() == "description":
            self.description = (a.get("content") or "").strip()
        if chrome:
            if tag not in VOID:
                self.depth_skip += 1
                self.stack.append((tag, True))
            return
        if tag == "img":
            self.imgs += 1
        if tag == "a":
            h = (a.get("href") or "").strip()
            if h and not h.startswith(("#", "mailto:", "tel:", "javascript:")):
                h = h.split("#")[0].split("?")[0]
                if h and not h.startswith(("http://", "https://")):
                    self.links.add("/" + h.lstrip("./"))
        if tag in ("h1", "h2", "title"):
            self._grab = tag
        if tag not in VOID:
            self.stack.append((tag, False))

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "title"):
            self._grab = None
        while self.stack:
            t, was_chrome = self.stack.pop()
            if was_chrome and self.depth_skip:
                self.depth_skip -= 1
            if t == tag:
                break

    def handle_data(self, d):
        if self.depth_skip:
            return
        if self._grab == "title" and self.title is None:
            self.title = " ".join(d.split())
        elif self._grab == "h1":
            self.h1.append(" ".join(d.split()))
        elif self._grab == "h2":
            self.h2.append(" ".join(d.split()))
        self.text.append(d)

    def words(self):
        return len(" ".join(" ".join(self.text).split()).split())


def parse(p: Path) -> Extract:
    e = Extract()
    e.feed(p.read_text(encoding="utf-8", errors="ignore"))
    return e


def audit(name, old_p, new_p, tol, verbose):
    o, n = parse(old_p), parse(new_p)
    fails, warns = [], []

    ow, nw = o.words(), n.words()
    drift = 0.0 if ow == 0 else (nw - ow) / ow * 100
    if abs(drift) > tol:
        fails.append("words %d -> %d (%+.1f%%)" % (ow, nw, drift))
    if o.jsonld != n.jsonld:
        fails.append("json-ld %d -> %d" % (o.jsonld, n.jsonld))
    if [x for x in o.h1 if x] != [x for x in n.h1 if x]:
        fails.append("h1 changed")
    if o.title != n.title:
        fails.append("title changed")
    if o.canonical != n.canonical:
        fails.append("canonical %s -> %s" % (o.canonical, n.canonical))
    if o.description != n.description:
        fails.append("meta description changed")
    lost = sorted(o.links - n.links)
    if lost:
        fails.append("%d internal link(s) lost" % len(lost))

    oh2, nh2 = set(filter(None, o.h2)), set(filter(None, n.h2))
    if oh2 - nh2:
        warns.append("%d h2 removed" % len(oh2 - nh2))
    if nh2 - oh2:
        warns.append("%d h2 added" % len(nh2 - oh2))
    if n.imgs < o.imgs:
        warns.append("images %d -> %d" % (o.imgs, n.imgs))

    status = "FAIL" if fails else ("warn" if warns else "ok")
    print("%-26s %-5s %6d -> %-6d %+6.1f%%  %s"
          % (name, status, ow, nw, drift, "; ".join(fails + warns) or ""))
    if verbose and (fails or warns):
        for h in sorted(oh2 - nh2):
            print("      - h2 gone:  %s" % h[:70])
        for h in sorted(nh2 - oh2):
            print("      + h2 added: %s" % h[:70])
        for l in lost[:15]:
            print("      - link:     %s" % l)
    return not fails


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verbose = "--verbose" in sys.argv
    tol = 2.0
    for a in sys.argv[1:]:
        if a.startswith("--tolerance"):
            tol = float(a.split("=")[1]) if "=" in a else float(sys.argv[sys.argv.index(a) + 1])

    if args:
        pairs = [(a, BACKUP / a, live_for(a)) for a in args]
    else:
        pairs = []
        for b in sorted(BACKUP.glob("*.html")):
            live = live_for(b.name)
            if live.exists():
                pairs.append((b.name, b, live))

    if not pairs:
        print("nothing to audit -- no backup/live pairs found in %s" % BACKUP)
        return 0

    print("%-26s %-5s %6s    %-6s %6s  %s" % ("page", "state", "words", "->", "drift", "problems"))
    print("-" * 96)
    ok = True
    for name, b, l in pairs:
        if not b.exists() or not l.exists():
            print("%-26s skip  (missing counterpart)" % name)
            continue
        ok &= audit(name, b, l, tol, verbose)
    print("-" * 96)
    print("PASS" if ok else "FAIL -- content changed on at least one page")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
