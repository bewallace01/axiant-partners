#!/usr/bin/env python3
"""Push _components/get-matched.html onto the most-cited pages, right after the Quick Answer.

Same single-source idea as sync-footer-v2.py: the block lives once in the component and
every page carries a synced copy between AXIANT-GETMATCHED markers. The one per-page part
is the line under the form that points at the closest money page; it is the {{MONEY_LINE}}
placeholder, filled from PAGES below.

Why these pages: they are the top 10 by Copilot / AI Overview citations (scripts/aeo/
top25-cited.txt). Citations there build the brand but rarely turn into leads, so the block
gives a reader who arrives from an AI answer a 3-field way in, and a link to the money page
that fits a borrower who owns an asset.

First run inserts the block after the Quick Answer container. Later runs only replace what
is between the markers. Idempotent.

    python scripts/sync-get-matched.py          # write
    python scripts/sync-get-matched.py --dry    # report only
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENT = ROOT / "_components" / "get-matched.html"
PATTERN = re.compile(r"<!-- AXIANT-GETMATCHED:START.*?<!-- AXIANT-GETMATCHED:END -->", re.S)
QA_START = re.compile(
    r'<div[^>]*class="[^"]*\bquick-answer\b[^"]*"[^>]*>'
    r'|<div class="callout" id="quick">', re.S)

OWN_ASSET = ('Own a truck or property outright? You may be able to borrow against it: see '
             '<a href="/commercial-truck-title-loan.html">commercial truck title loans</a> and '
             '<a href="/real-estate-secured-business-loan.html">loans secured by real estate you own</a>.')
OWN_PROPERTY = ('Already own commercial or investment property? See '
                '<a href="/real-estate-secured-business-loan.html">borrowing against real estate you own</a>.')
PRACTICE = ('Financing equipment or expansion for the practice itself? See '
            '<a href="/medical-practices-business-financing.html">medical practice financing</a>.')

PAGES = {
    "/business-line-of-credit/articles/best-unsecured-business-lines-of-credit-2026/": OWN_ASSET,
    "/working-capital-loans/articles/best-working-capital-loans-2026/": OWN_ASSET,
    "/business-line-of-credit/articles/typical-business-line-of-credit-rates-2026/": OWN_ASSET,
    "/equipment-financing/articles/cherry-vs-carecredit/": PRACTICE,
    "/sba-loans/articles/what-is-an-sba-504-loan/": OWN_PROPERTY,
    "/commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026/": OWN_PROPERTY,
    "/business-loan-rates-2026/": OWN_ASSET,
    "/business-term-loans/articles/term-loan-vs-line-of-credit/": OWN_ASSET,
    "/commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/": OWN_PROPERTY,
    "/equipment-financing/articles/carecredit-vs-patientfi-imaging-radiology/": PRACTICE,
}


def page_file(url):
    p = ROOT / url.lstrip("/")
    return p / "index.html" if url.endswith("/") else p


def qa_end(html):
    """Index just past the </div> that closes the Quick Answer container, or None."""
    for m in QA_START.finditer(html):
        if "blog-rail" in m.group(0):
            continue
        depth, i = 1, m.end()
        tag = re.compile(r"<(/?)div\b[^>]*>", re.I)
        while depth:
            t = tag.search(html, i)
            if not t:
                return None
            depth += -1 if t.group(1) else 1
            i = t.end()
        return i
    return None


def main(dry):
    template = COMPONENT.read_text(encoding="utf-8").strip()
    bad = 0
    for url, line in PAGES.items():
        f = page_file(url)
        s = f.read_bytes().decode("utf-8")
        nl = "\r\n" if "\r\n" in s else "\n"
        block = template.replace("{{MONEY_LINE}}", line).replace("\r\n", "\n").replace("\n", nl)
        if PATTERN.search(s):
            new = PATTERN.sub(lambda _: block, s, count=1)
            action = "synced" if new != s else "same"
        else:
            end = qa_end(s)
            if end is None:
                print(f"  NO QUICK ANSWER, skipped: {url}")
                bad += 1
                continue
            new = s[:end] + nl + block + s[end:]
            action = "inserted"
        if new != s and not dry:
            f.write_bytes(new.encode("utf-8"))
        print(f"  {action}{' (dry)' if dry else ''}: {url}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--dry" in sys.argv))
