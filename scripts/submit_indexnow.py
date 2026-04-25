#!/usr/bin/env python3
"""Submit all sitemap URLs to IndexNow for immediate search engine indexing."""
import re
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

    urls = extract_urls_from_sitemap(SITEMAP)
    if not urls:
        print("No URLs found in sitemap.")
        return 1

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
