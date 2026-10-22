#!/usr/bin/env python3
"""The date a page's CONTENT last changed, from git, ignoring sitewide sweeps.

`git log -1` on a page is usually a sweep: a pixel install, a script.js version bump or a
footer sync that touched 800+ files and changed no words. Dating a page by that commit
asserts freshness the page did not earn, which is the signal AI assistants learn to
discount. A content commit here means one that touched at most SWEEP_LIMIT files, and is
not one of the AEO Batch 1 commits (brand clause, get-matched block, link sentences,
sources blocks, author schema), which add to a page but do not revise its content.

Used by fix_page_dates.py. Run alone to print a page's content date:
    python scripts/aeo/content_dates.py equipment/semi-trucks/index.html
"""
import functools
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SWEEP_LIMIT = 50
NOT_CONTENT = ("AEO 1", "Homepage form to CRM; first-touch attribution")


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


@functools.lru_cache(maxsize=None)
def files_in(commit):
    return len([l for l in _git("show", "--name-only", "--format=", commit).splitlines() if l.strip()])


def content_date(rel):
    """YYYY-MM-DD of the last content commit touching rel, or None."""
    for line in _git("log", "--format=%H %cs %s", "--follow", "--", rel).splitlines():
        sha, date, subject = line.split(" ", 2)
        if subject.startswith(NOT_CONTENT):
            continue
        if files_in(sha) <= SWEEP_LIMIT:
            return date
    return None


if __name__ == "__main__":
    for rel in sys.argv[1:]:
        print(content_date(rel), rel)
