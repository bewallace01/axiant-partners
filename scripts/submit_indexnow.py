#!/usr/bin/env python3
"""Submit URLs to IndexNow so Bing, Yandex and DuckDuckGo pick up changes at once.

Matters more than Bing's own traffic share, because that index feeds Copilot and
parts of AI search - the surfaces this site is explicitly built to be cited in.

    python3 scripts/submit_indexnow.py --changed   # only pages changed in HEAD
    python3 scripts/submit_indexnow.py --changed --since HEAD~5
    python3 scripts/submit_indexnow.py             # every sitemap URL
    python3 scripts/submit_indexnow.py --dry-run   # print, submit nothing

Prefer --changed for routine deploys: IndexNow is a change-notification
protocol, and resubmitting the whole site on every push is wasteful. A full
submit is appropriate after a long gap with no submissions.
"""
import re
import sys
import subprocess
import urllib.request
import urllib.error
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SITEMAP = BASE / "sitemap.xml"
INDEXNOW_URL = "https://api.indexnow.org/indexnow"

HOST = "axiantpartners.com"
KEY = "177edbb44de64c5d8f856713891bb8dd"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

BATCH_SIZE = 500  # IndexNow allows up to 10k; smaller batches are safer


def extract_urls_from_sitemap(path: Path) -> list[str]:
    """Extract <loc> URLs from sitemap.xml."""
    text = path.read_text(encoding="utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", text)


def url_for_file(rel: str) -> str:
    """Map a repo-relative .html path to its canonical public URL."""
    rel = rel.replace("\\", "/")
    if rel == "index.html":
        return f"https://{HOST}/"
    if rel.endswith("/index.html"):
        return f"https://{HOST}/" + rel[: -len("index.html")]
    return f"https://{HOST}/" + rel


def changed_urls(since: str, sitemap_urls: list[str]) -> list[str]:
    """URLs for .html files touched since `since`, limited to sitemap members.

    Filtering against the sitemap keeps noindex pages, canonicalised duplicates
    and redirect sources out of the submission - IndexNow should only ever be
    told about URLs we actually want indexed.
    """
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACMRT", since, "HEAD"],
            cwd=BASE, capture_output=True, text=True, timeout=60, check=True,
        ).stdout
    except (OSError, subprocess.SubprocessError) as e:
        print(f"git diff failed ({e}); cannot compute changed set.")
        return []
    allowed = {u.rstrip("/") or f"https://{HOST}/" for u in sitemap_urls}
    urls, skipped = [], 0
    for line in out.split():
        if not line.endswith(".html"):
            continue
        u = url_for_file(line)
        if (u.rstrip("/") or f"https://{HOST}/") in allowed:
            urls.append(u)
        else:
            skipped += 1
    if skipped:
        print(f"  ({skipped} changed page(s) skipped - not in sitemap: noindex, "
              f"canonicalised elsewhere, or a redirect source)")
    return sorted(set(urls))


def submit_batch(url_list: list[str]) -> bool:
    """POST a batch of URLs to IndexNow. Returns True on success."""
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_URL,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            if status in (200, 202):
                return True
            print(f"  Unexpected status: {status}")
            return False
    except urllib.error.HTTPError as e:
        print(f"  HTTP error: {e.code} {e.reason}")
        try:
            body = e.read().decode("utf-8")
            print(f"  Response: {body[:500]}")
        except Exception:
            pass
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def main():
    if not SITEMAP.exists():
        print(f"Sitemap not found: {SITEMAP}")
        return 1

    sitemap_urls = extract_urls_from_sitemap(SITEMAP)
    if not sitemap_urls:
        print("No URLs found in sitemap.")
        return 1

    dry = "--dry-run" in sys.argv
    if "--changed" in sys.argv:
        since = "HEAD~1"
        if "--since" in sys.argv:
            since = sys.argv[sys.argv.index("--since") + 1]
        print(f"Changed-page mode (diff {since}..HEAD)")
        urls = changed_urls(since, sitemap_urls)
        if not urls:
            print("No indexable pages changed. Nothing to submit.")
            return 0
    else:
        urls = sitemap_urls
        print(f"Full-sitemap mode ({len(urls)} URLs)")

    if dry:
        print(f"\n[dry run] would submit {len(urls)} URL(s):")
        for u in urls[:40]:
            print(f"   {u}")
        if len(urls) > 40:
            print(f"   ... and {len(urls) - 40} more")
        return 0

    print(f"Found {len(urls)} URLs in sitemap.xml")
    print(f"Submitting to IndexNow in batches of {BATCH_SIZE}...")
    print()

    success = 0
    failed = 0
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i : i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1
        total_batches = (len(urls) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"Batch {batch_num}/{total_batches} ({len(batch)} URLs)...", end=" ")
        if submit_batch(batch):
            success += len(batch)
            print("OK")
        else:
            failed += len(batch)
            print("FAILED")

    print()
    print(f"Done. Submitted: {success}, Failed: {failed}")
    print("Check Bing Webmaster Tools to verify URLs were received.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    exit(main())
