# -*- coding: utf-8 -*-
"""
Move the two DSCR articles out of the CRE cluster and under the DSCR pillar.

They are DSCR content filed under commercial-real-estate-loans while a separate
DSCR pillar exists -- the definition of cannibalisation. Search Console says
there is nothing to protect: dscr-rental-loans-real-estate-investors sits at
position 69.5 on 204 impressions and 0 clicks, dscr-loan-vs-conventional-
mortgage at 76.0 on 1 impression, and all 25 DSCR queries rank 69-92 with zero
clicks between them. Moving cannot cost rankings that do not exist.

Four things have to move together or the pages break quietly:

  the files          -> dscr-loans/articles/<slug>/
  self-references    canonical, og:url and four JSON-LD url/@id fields per file
  the breadcrumb     "Commercial Real Estate Loans" -> "DSCR Loans", pointing at
                     /dscr-loans.html
  RELATIVE links     each file carries ../ links to CRE siblings. From the new
                     location ../ resolves to dscr-loans/articles/, so every one
                     of them would 404 while still looking fine in the markup.
                     They are rewritten to absolute /commercial-real-estate-
                     loans/articles/... paths.

Inbound links across the site are repointed, and 301s are added to _redirects
so the old URLs keep working.
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD_DIR = "commercial-real-estate-loans/articles"
NEW_DIR = "dscr-loans/articles"
SLUGS = ["dscr-loan-vs-conventional-mortgage",
         "dscr-rental-loans-real-estate-investors"]
BASE = "https://axiantpartners.com"

SKIP_DIRS = {"_backup-pre-v2-swap", "node_modules", ".git", "_preview",
             "_analysis", "_outreach", "_marketing", "_components",
             "tools", "scripts", "docs", "__pycache__"}


def sh(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)


def live_pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def move_files(apply_changes):
    moved = []
    for slug in SLUGS:
        src = os.path.join(ROOT, OLD_DIR.replace("/", os.sep), slug)
        dst = os.path.join(ROOT, NEW_DIR.replace("/", os.sep), slug)
        if not os.path.isdir(src):
            print(f"  SOURCE MISSING  {slug}")
            continue
        if os.path.isdir(dst):
            print(f"  already moved   {slug}")
            moved.append(slug)
            continue
        if apply_changes:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            r = sh("git", "mv", f"{OLD_DIR}/{slug}", f"{NEW_DIR}/{slug}")
            if r.returncode:
                print(f"  git mv FAILED   {slug}: {r.stderr.strip()[:90]}")
                continue
        moved.append(slug)
        print(f"  moved           {slug}")
    return moved


def fix_moved_file(slug, apply_changes):
    path = os.path.join(ROOT, NEW_DIR.replace("/", os.sep), slug, "index.html")
    if not os.path.exists(path):
        return "not present"
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    before = s

    # 1. relative links first -- they must become absolute BEFORE anything else
    #    rewrites paths, or they silently point into the new directory.
    s = re.sub(r'href="\.\./([^"]*)"', rf'href="/{OLD_DIR}/\1"', s)

    # 2. every self-reference: canonical, og:url, JSON-LD url / @id
    s = s.replace(f"{BASE}/{OLD_DIR}/{slug}/", f"{BASE}/{NEW_DIR}/{slug}/")

    # 3. the breadcrumb now belongs to the DSCR pillar
    s = s.replace(
        f'"name":"Commercial Real Estate Loans","item":"{BASE}/commercial-real-estate-loans.html"',
        f'"name":"DSCR Loans","item":"{BASE}/dscr-loans.html"')
    s = s.replace(
        f'"name":"Articles","item":"{BASE}/{OLD_DIR}/"',
        f'"name":"Articles","item":"{BASE}/{NEW_DIR}/"')

    if apply_changes and s != before:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(s)
    return "rewritten" if s != before else "no change needed"


def repoint_inbound(apply_changes):
    n = 0
    for path in live_pages():
        with open(path, encoding="utf-8") as fh:
            s = fh.read()
        before = s
        for slug in SLUGS:
            s = s.replace(f"{OLD_DIR}/{slug}/", f"{NEW_DIR}/{slug}/")
        if s != before:
            n += 1
            if apply_changes:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(s)
    return n


def add_redirects(apply_changes):
    p = os.path.join(ROOT, "_redirects")
    with open(p, encoding="utf-8") as fh:
        s = fh.read()
    lines = []
    for slug in SLUGS:
        old, new = f"/{OLD_DIR}/{slug}/", f"/{NEW_DIR}/{slug}/"
        if old in s:
            continue
        lines.append(f"{old}  {new}  301")
    if not lines:
        return 0
    block = ("\n# DSCR articles moved out of the CRE cluster and under the DSCR\n"
             "# pillar they belong to (de-cannibalisation). Both ranked 69+ with\n"
             "# zero clicks, so there was no equity to protect.\n"
             + "\n".join(lines) + "\n")
    if apply_changes:
        with open(p, "a", encoding="utf-8", newline="") as fh:
            fh.write(block)
    return len(lines)


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    print("\n-- move --")
    moved = move_files(apply_changes)
    print("\n-- rewrite the moved files --")
    for slug in moved:
        print(f"  {slug:46} {fix_moved_file(slug, apply_changes)}")
    print("\n-- repoint inbound links --")
    print(f"  files updated: {repoint_inbound(apply_changes)}")
    print("\n-- 301s --")
    print(f"  rules added: {add_redirects(apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
