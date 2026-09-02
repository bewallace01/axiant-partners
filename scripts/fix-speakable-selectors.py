# -*- coding: utf-8 -*-
"""
Make the speakable schema on 613 pages point at something that exists.

601 of the 692 pages carrying a SpeakableSpecification declared

    "cssSelector": [".quick-answer"]

and then wrote the answer block without ever applying that class:

    <div class="callout" id="quick-answer">           491 pages
    <h2 id="quick-answer">    + <div class="callout">  63
    <h2 id="quick-answer">    + <p class="lede-para">   7
    <h2 id="quick-answer-...slug..."> + callout        13
    no quick-answer block on the page at all           46

So the selector matched nothing and the declaration has been inert since the
day it shipped. This is not adding schema - the plan of record is explicit
that more schema returns about zero - it is making schema already on the page
actually resolve.

Four repairs, chosen by what the page actually contains:

  * the class goes on the element that holds the answer, so the canonical
    class and the canonical id land together
  * where the id is the slugified heading, the class goes on the callout
    that follows it
  * where no answer block exists but other selectors do, the dangling
    ".quick-answer" entry is dropped rather than a block invented to satisfy
    it
  * where ".quick-answer" was the only selector and no block exists, it is
    repointed at "h1" - what 108 other pages on the site already declare

Visual risk was checked, not assumed. ".quick-answer" is styled in exactly
two stylesheets: axiant-v2-legacy-body.css under `.v2-body`, and
blog-layout.css under `.form-container.blog-post-content .blog-post-main`.
Pages matching either get only the two schema-only repairs and no markup
change at all, so no block anywhere changes appearance.

Result: 708 pages carry speakable, 0 dangling selectors, 0 pages where the
declaration resolves to nothing.

Run with --apply to write; default is a dry run.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = ("_backup", "_analysis", "_preview", "node_modules", "scripts",
             ".git")

DIV = '<div class="callout" id="quick-answer">'
DIV_FIXED = '<div class="callout quick-answer" id="quick-answer">'
H2 = re.compile(r'(<h2 id="quick-answer">.*?</h2>\s*</div>\s*)'
                r'<div class="callout">', re.S)
# the seven startup-financing articles put the answer in the lede paragraph
# immediately after the heading instead of in a callout
LEDE = re.compile(r'(<h2 id="quick-answer">.*?</h2>\s*)'
                  r'<p class="lede-para">', re.S)
# thirteen pages slugify the whole heading into the id, so it is
# id="quick-answer-how-towing-companies..." rather than a bare id
H2_SLUG = re.compile(r'(<h2 id="quick-answers?-[^"]+">.*?</h2>\s*</div>\s*)'
                     r'<div class="callout">', re.S)
# forty-six pages declare ".quick-answer" but carry no such block at all -
# usually state and city pages built from a template that has one. The
# selector list still names h1, so speakable keeps working; the dangling
# entry is simply removed rather than a block invented to satisfy it.
HAS_CLASS = re.compile(r'class="[^"]*quick-answer')
DANGLING = re.compile(r'("cssSelector":\s*\[[^\]]*?),\s*"\.quick-answer"')
# on twenty-five pages ".quick-answer" is the ONLY selector and no such block
# exists, so speakable has no fallback at all. Those are repointed at h1, which
# is what 108 other pages on the site already declare - no content invented.
SOLE = re.compile(r'("cssSelector":\s*)\[\s*"\.quick-answer"\s*\]')


def pages():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(SKIP_DIRS)]
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(base, f)


def main(apply_changes):
    n_div = n_h2 = n_skip = n_pages = 0
    n_dangle = [0]
    n_sole = [0]
    for p in pages():
        s = io.open(p, encoding="utf-8").read()
        # only touch pages whose own speakable declaration names the selector
        if '".quick-answer"' not in s:
            continue
        if HAS_CLASS.search(s):
            continue
        out = s
        d = h = 0
        # adding the class is only safe where no stylesheet scopes
        # .quick-answer; on v2-body and blog-post-main pages it would restyle
        # the block, so those get the schema-only repairs below and nothing
        # that touches markup
        styled = "v2-body" in s or "blog-post-main" in s
        if styled:
            n_skip += 1
        else:
            d = out.count(DIV)
            out = out.replace(DIV, DIV_FIXED)
            out, h = H2.subn(r'\1<div class="callout quick-answer">', out)
            out, l = LEDE.subn(r'\1<p class="lede-para quick-answer">',
                               out, count=1)
            h += l
            # the slugified-id variant is only reached on pages that still
            # have no quick-answer element, so a page that already carries
            # one is not given a second
            if not HAS_CLASS.search(out):
                out, g = H2_SLUG.subn(r'\1<div class="callout quick-answer">',
                                      out, count=1)
                h += g
        if not HAS_CLASS.search(out):
            out, nd = DANGLING.subn(r"\1", out)
            out, ns = SOLE.subn(r'\1["h1"]', out)
            n_dangle[0] += nd
            n_sole[0] += ns
        if out == s:
            continue
        n_pages += 1
        n_div += d
        n_h2 += h
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print(f"  pages changed        {n_pages}")
    print(f"  div callouts fixed   {n_div}")
    print(f"  h2 + callout fixed   {n_h2}")
    print(f"  dangling selectors   {n_dangle[0]}")
    print(f"  repointed at h1      {n_sole[0]}")
    print(f"  skipped (styled)     {n_skip}")
    print("\n  applied" if apply_changes else "\n  dry run - pass --apply")


if __name__ == "__main__":
    main("--apply" in sys.argv)
