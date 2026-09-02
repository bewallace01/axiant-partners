# -*- coding: utf-8 -*-
"""
Give the 49 indexable pages that carry no dateModified an honest one.

The site audit's GEO check wants "dateModified" inside the page's own JSON-LD
- a <meta property="article:modified_time"> does not satisfy it. 794 of 843
indexable pages have it. The 49 that do not are the nine cluster pillars, the
nine cluster hubs, the homepage, the legal and contact pages, two calculators
and the equipment-for-sale catalogue.

The date comes from git's last commit for that file, never from today's date.
Freshness that is asserted rather than earned is exactly the signal an
assistant learns to discount, and the sitemap generator already resolves
lastmod the same way, so the two agree.

Two shapes, both already used on this site:

  * a page with a WebPage or CollectionPage node gets "dateModified" added
    to that node, beside its url
  * a page with neither gets the bare node 28 other pages already carry:
    {"@context":"...","@type":"WebPage","url":"...","dateModified":"..."}

Nothing else on the page changes, and no visible text is added.

Run with --apply to write; default is a dry run.
"""
import glob
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("_backup", "_analysis", "_preview", "node_modules", "scripts",
        "tools", "_components")
SITE = "https://axiantpartners.com/"

PAGE_NODE = re.compile(r'("@type":\s*"(?:WebPage|CollectionPage)"[^{}]*?'
                       r'"url":\s*"[^"]*")')


def git_date(rel):
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
        return out or None
    except Exception:
        return None


def url_for(rel):
    u = rel.replace(os.sep, "/")
    if u.endswith("/index.html"):
        u = u[:-len("index.html")]
    return SITE + ("" if u == "index.html" else u)


def main(apply_changes):
    n_node = n_bare = n_skip = 0
    for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(p, ROOT)
        if rel.startswith(SKIP):
            continue
        s = io.open(p, encoding="utf-8").read()
        if 'content="noindex' in s or '"dateModified"' in s:
            continue
        d = git_date(rel)
        if not d:
            n_skip += 1
            print(f"  !! no git date, skipped   {rel}")
            continue
        m = PAGE_NODE.search(s)
        if m:
            out = (s[:m.end()] + f', "dateModified": "{d}"' + s[m.end():])
            n_node += 1
        else:
            node = ('<script type="application/ld+json">{"@context": '
                    '"https://schema.org", "@type": "WebPage", "url": '
                    f'"{url_for(rel)}", "dateModified": "{d}"}}</script>')
            i = s.rfind("</head>")
            if i < 0:
                n_skip += 1
                continue
            out = s[:i] + node + s[i:]
            n_bare += 1
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print(f"  added to existing node   {n_node}")
    print(f"  added as a bare node     {n_bare}")
    print(f"  skipped                  {n_skip}")
    print("\n  applied" if apply_changes else "\n  dry run - pass --apply")


if __name__ == "__main__":
    main("--apply" in sys.argv)
