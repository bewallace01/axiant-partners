#!/usr/bin/env python3
"""Report pages that BELONG in sitemap.xml but are missing, and vice versa.

`generate_sitemap.py` enumerates a hand-maintained list rather than discovering
pages, so it drifts behind the site (it currently emits ~191 fewer URLs than the
committed sitemap and refuses to run for that reason). This script does not
generate anything - it audits, so drift is visible before it costs indexing.

A page belongs in the sitemap when all of these hold:
  * it is a real page on disk (foo.html or foo/index.html)
  * robots meta does NOT contain noindex
  * it is self-canonical (a page canonicalised elsewhere is a duplicate)
  * it is not inside a private/build directory

    python3 scripts/check_sitemap_drift.py
    python3 scripts/check_sitemap_drift.py --strict   # exit 1 if drift found
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
SITE = "https://axiantpartners.com"

SKIP_DIRS = {"_analysis", "_components", "_marketing", "_outreach", "node_modules",
             "tools", "docs", "scripts", ".git", "assets", "fonts", "flyers"}
# Pages intentionally absent from the sitemap for reasons other than noindex.
KNOWN_EXCLUDED = {
    "/embed-calculator.html",        # widget shell for third-party embedding
    "/calculator-embed.html",
    "/mca-calculator-embed.html",
    "/dscr-calculator-embed.html",
}

ROBOTS_RE = re.compile(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']*)["\']', re.I)
CANON_RE = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']*)["\']', re.I)


def url_for(path):
    rel = os.path.relpath(path, BASE).replace(os.sep, "/")
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def main():
    sm_path = os.path.join(BASE, "sitemap.xml")
    sm = io.open(sm_path, encoding="utf-8").read()
    in_sitemap = {u.replace(SITE, "") for u in re.findall(r"<loc>([^<]+)</loc>", sm)}
    in_sitemap_norm = {u.rstrip("/") or "/" for u in in_sitemap}

    files = []
    for root, dirs, names in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        files += [os.path.join(root, n) for n in names if n.endswith(".html")]

    missing, noindexed, canon_elsewhere, ok = [], [], [], 0
    for f in sorted(files):
        try:
            s = io.open(f, encoding="utf-8").read()
        except Exception:
            continue
        u = url_for(f)
        if u in KNOWN_EXCLUDED:
            continue
        robots = (ROBOTS_RE.search(s).group(1) if ROBOTS_RE.search(s) else "")
        if "noindex" in robots.lower():
            noindexed.append(u)
            continue
        cm = CANON_RE.search(s)
        if cm:
            canon = cm.group(1).replace(SITE, "")
            if (canon.rstrip("/") or "/") != (u.rstrip("/") or "/"):
                canon_elsewhere.append((u, canon))
                continue
        if (u.rstrip("/") or "/") in in_sitemap_norm:
            ok += 1
        else:
            missing.append(u)

    # sitemap entries with no file behind them
    on_disk = {(url_for(f).rstrip("/") or "/") for f in files}
    orphaned = sorted(u for u in in_sitemap_norm if u not in on_disk)

    print(f"html files scanned          : {len(files)}")
    print(f"URLs in sitemap.xml         : {len(in_sitemap)}")
    print(f"indexable + self-canonical  : {ok + len(missing)}")
    print(f"  of those, in sitemap      : {ok}")
    print(f"  of those, MISSING         : {len(missing)}")
    print(f"excluded - noindex          : {len(noindexed)}")
    print(f"excluded - canonical elsewhere: {len(canon_elsewhere)}")
    print(f"sitemap entries with no file: {len(orphaned)}")

    if missing:
        print("\n=== MISSING FROM SITEMAP (indexable, self-canonical) ===")
        for u in missing:
            print(f"   {u}")
    if orphaned:
        print("\n=== IN SITEMAP BUT NO FILE ON DISK ===")
        for u in orphaned[:40]:
            print(f"   {u}")

    drift = bool(missing or orphaned)
    print("\n" + ("DRIFT FOUND" if drift else "NO DRIFT - sitemap matches the indexable page set"))
    if "--strict" in sys.argv and drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
