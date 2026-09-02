#!/usr/bin/env python3
"""Conformance check for the Axiant v2 design system.

    python scripts/check-page.py                    # every converted page
    python scripts/check-page.py contact.html faq.html

A page is conformant when ALL of its styling comes from /axiant-v2.css.
The old 232KB stylesheet grew because pages were allowed to define their
own colours, tokens and overrides locally. This makes that drift visible.

Exit code 1 if anything fails, so it can gate a commit.
"""
import re, sys, glob, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LEGACY = re.compile(r'href="/?(?:styles|critical|blog-layout|article-rail|article-layout)\.css')

def check(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    fails, warns = [], []

    n = len(LEGACY.findall(s))
    if n: fails.append(f"{n} legacy stylesheet link(s) - must be 0")

    styles = re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)
    if styles:
        fails.append(f"{len(styles)} inline <style> block(s), {sum(len(b) for b in styles)} chars "
                     f"- move to axiant-v2.css")
        css = "".join(styles)
        hexes = set(re.findall(r"#[0-9a-fA-F]{3,8}\b", css))
        if hexes: fails.append(f"{len(hexes)} hardcoded colour(s) in inline CSS - use tokens")
        toks = set(re.findall(r"(--[\w-]+)\s*:", css))
        if toks: fails.append(f"{len(toks)} locally-defined --token(s) - the system owns tokens")

    n = len(re.findall(r"!important", s))
    if n: fails.append(f"{n} !important - must be 0")

    if "axiant-v2.css" not in s: fails.append("does not link /axiant-v2.css")
    elif not re.search(r"axiant-v2\.css\?v=\d+", s): warns.append("axiant-v2.css link has no ?v= cache-buster")

    if s.count("AXIANT-HEADER") != 2:
        fails.append("missing the AXIANT-HEADER block (sync-header-v2.py owns the nav)")
    if "<footer" not in s:
        warns.append("no footer element")
    if not re.search(r'rel="canonical"', s): fails.append("no canonical link")
    if "application/ld+json" not in s: warns.append("no JSON-LD - was it dropped in conversion?")
    if re.search(r"body\s*\{\s*opacity:\s*0", s): fails.append("body{opacity:0} FOUT hack - remove")
    if re.search(r'class="[^"]*\bmain-nav\b', s): fails.append("old .main-nav markup still present")

    return fails, warns

def main():
    args = sys.argv[1:]
    if args:
        pages = [os.path.join(ROOT, a) for a in args]
    else:
        pages = [p for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
                 if not any(x in p for x in ("node_modules","_backup","_preview","_components"))
                 # build templates are not pages: their canonical, title and
                 # meta arrive from a {{META}} placeholder at build time, so
                 # checking the template flags a canonical that is supplied
                 # 17 times over in the pages it generates
                 and "{{" not in open(p, encoding="utf-8", errors="replace").read()
                 and "axiant-v2.css" in open(p, encoding="utf-8", errors="replace").read()]

    bad = 0
    for p in sorted(pages):
        rel = os.path.relpath(p, ROOT)
        fails, warns = check(p)
        if fails:
            bad += 1
            print(f"\nFAIL  {rel}")
            for f in fails: print(f"        x {f}")
            for w in warns: print(f"        ! {w}")
        elif warns:
            print(f"\nWARN  {rel}")
            for w in warns: print(f"        ! {w}")

    total = len(pages)
    print(f"\n{total - bad}/{total} pages conformant")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
