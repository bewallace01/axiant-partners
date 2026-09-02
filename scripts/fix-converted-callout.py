# -*- coding: utf-8 -*-
"""
Put the breadcrumb, dateline and quick-answer callout inside the content column.

convert-legacy-page.py wrapped only the pieces that happened to be adjacent,
so the run between the hero and the first content section came out three
different ways across the 14 pages: wrapper then bare callout, wrapper with
the dateline left outside it, or no wrapper at all. Measured on the live page,
every other block sat at left 353 inside the 1200px column and the callout sat
at left 0, hard against the viewport edge.

This wraps that whole run once, whatever it contains, and strips the legacy
inline styling off it - background:var(--bg-card), the border-left, the
padding and radius on the callout, and the colour overrides on the breadcrumb
links - so the .callout and .crumbs components axiant-v2.css already defines
are what actually renders.

Run with --apply to write; default is a dry run.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERO_END = "</section>"


def fix(path, apply_changes):
    rel = os.path.relpath(path, ROOT)
    s = io.open(path, encoding="utf-8").read()

    h = s.find('<section class="hero-compact">')
    if h < 0:
        return False
    start = s.find(HERO_END, h) + len(HERO_END)
    # anchor on the first CONTENT band, not on any section: the wrapper the
    # converter already emitted is itself `section class="section
    # section-tight"`, so searching for that prefix stopped immediately on the
    # five pages that had one and skipped them
    ends = [i for i in (s.find('<section class="section">', start),
                        s.find('<section class="section section-alt', start))
            if i > 0]
    if not ends:
        return False
    end = min(ends)

    run = s[start:end]
    if not any(k in run for k in ("callout", "dateline", "crumbs")):
        return False

    # remove any wrapper the converter already placed inside this run
    run = run.replace(
        '<section class="section section-tight"><div class="container">', "")
    run = run.replace("</div></section>", "")

    # legacy inline styling, so the v2 components apply
    run = re.sub(r'(<div class="callout")\s+style="[^"]*"', r"\1", run)
    run = re.sub(r'(<nav[^>]*class="crumbs")\s+style="[^"]*"', r"\1", run)
    run = re.sub(r"(<strong)\s+style=\"[^\"]*\"", r"\1", run)
    run = re.sub(r"(<p)\s+style=\"[^\"]*\"", r"\1", run)
    run = re.sub(r"(<a[^>]*?)\s+style=\"[^\"]*\"", r"\1", run)
    run = run.strip()

    wrapped = ('<section class="section section-tight">\n'
               '<div class="container">\n' + run + "\n</div>\n</section>\n")
    out = s[:start] + "\n" + wrapped + s[end:]

    print("  %-46s wrapped %d chars" % (rel, len(run)))
    if apply_changes:
        io.open(path, "w", encoding="utf-8", newline="").write(out)
    return True


def main(argv):
    ap = "--apply" in argv
    n = 0
    for p in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        s = io.open(p, encoding="utf-8", errors="replace").read()
        if "hero-compact" in s and "ef-hero" not in s and (
                '<div class="callout"' in s or 'class="crumbs"' in s):
            n += fix(p, ap)
    print("\n  %d page(s)%s" % (n, "  applied" if ap else "  dry run"))


if __name__ == "__main__":
    main(sys.argv[1:])
