#!/usr/bin/env python3
"""
SBA loan articles: remove duplicate batch24 sections (reduces internal competition / thin repeats),
insert a WebP lead visual after the first <p> in .blog-post-main, bump modified dates.
Run from repo root: python tools/sba_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SBA_ARTICLES = ROOT / "sba-loans" / "articles"
MODIFIED = "2026-03-27"

# (filename under /assets/, alt text, width, height) — heights approximate 16:9 for non-square assets
SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "sba-loan-restaurant-acquisition": (
        "restaurants-intro-1200w.webp",
        "Restaurant owner reviewing financing options for acquisition with SBA-backed programs",
        1200,
        675,
    ),
    "sba-loan-veterinary-practice": (
        "medical-practices-sba-loans-800w.webp",
        "Veterinary practice owner exploring SBA 7(a) financing for clinic growth",
        800,
        450,
    ),
    "sba-loan-manufacturing-lost-supplier-overseas-conflict-pivot": (
        "manufacturing-sba-loans-800w.webp",
        "Manufacturing business considering SBA working capital and equipment financing",
        800,
        450,
    ),
    "sba-loan-owner-occupied-commercial-property": (
        "sba-real-estate-800w.webp",
        "Owner-occupied commercial real estate financed with SBA 504 or 7(a) structures",
        800,
        450,
    ),
    "sba-loan-franchise-acquisition": (
        "sba-use-acquisition-800w.webp",
        "Franchise buyer reviewing SBA loan structure for a qualified acquisition",
        800,
        450,
    ),
    "franchise-financing-mistakes-delay-kill-deal": (
        "sba-use-acquisition-560w.webp",
        "Franchise financing paperwork and timeline planning for SBA-backed deals",
        560,
        315,
    ),
    "can-you-use-sba-loan-to-buy-a-business": (
        "sba-acquisition-800w.webp",
        "Business buyer evaluating SBA 7(a) for an asset or stock acquisition",
        800,
        450,
    ),
    "whats-stopping-you-buying-business-sba-loan": (
        "sba-acquisition-800w.webp",
        "Entrepreneur preparing documents to qualify for an SBA acquisition loan",
        800,
        450,
    ),
    "what-credit-score-needed-sba-loan": (
        "sba-7a-800w.webp",
        "SBA 7(a) and 504 programs: credit profile and lender underwriting context",
        800,
        450,
    ),
    "how-much-down-payment-required-sba-loan": (
        "sba-lower-down-800w.webp",
        "Equity injection and down payment expectations for SBA-guaranteed loans",
        800,
        450,
    ),
    "what-documents-needed-sba-loan": (
        "sba-intro-800w.webp",
        "SBA loan application package with financial statements and forms",
        800,
        450,
    ),
    "how-long-sba-loan-approval": (
        "sba-long-terms-800w.webp",
        "SBA loan timeline from application through underwriting to closing",
        800,
        450,
    ),
    "sba-7a-vs-504-loan": (
        "sba-504-800w.webp",
        "Comparing SBA 7(a) flexibility with SBA 504 fixed-asset financing",
        800,
        450,
    ),
    "sba-loan-vs-business-line-of-credit": (
        "sba-flexible-use-800w.webp",
        "Choosing between term-style SBA financing and revolving business credit",
        800,
        450,
    ),
    "sba-loan-alternatives-when-you-dont-qualify": (
        "sba-working-capital-800w.webp",
        "Alternative small-business financing paths when SBA approval is uncertain",
        800,
        450,
    ),
    "sba-loan-denied-reasons-fix-before-reapplying": (
        "sba-amounts-800w.webp",
        "Reviewing loan amount, structure, and fixes after an SBA denial",
        800,
        450,
    ),
    "what-do-lenders-look-for-sba-loan-approval": (
        "sba-competitive-rates-800w.webp",
        "Lender review of cash flow, credit, and collateral for SBA underwriting",
        800,
        450,
    ),
    "sba-loan-mistakes-delay-kill-approval": (
        "sba-hero-800w.webp",
        "Avoiding common documentation and timing mistakes in SBA submissions",
        800,
        450,
    ),
    "red-flags-sba-loan-offers-packaging": (
        "sba-equipment-800w.webp",
        "Scrutinizing SBA loan offers, fees, and packaging before you sign",
        800,
        450,
    ),
    "sba-loan-lock-in-rates-war-inflation-good-time": (
        "sba-long-terms-560w.webp",
        "Long-term SBA financing and rate considerations during inflation cycles",
        560,
        315,
    ),
    "sba-loans-harder-wartime-economic-uncertainty": (
        "sba-intro-600w.webp",
        "SBA lending conditions during economic uncertainty and tighter underwriting",
        600,
        338,
    ),
    "reasons-sba-loan-closing-gets-pushed-back": (
        "sba-use-cre-800w.webp",
        "Closing delays on SBA real estate and acquisition loans: third-party items",
        800,
        450,
    ),
    "why-sba-loan-keeps-coming-back-for-more-documents": (
        "sba-intro-800w.webp",
        "SBA stipulations and document requests during underwriting",
        800,
        450,
    ),
    "why-sba-loan-keeps-getting-delayed": (
        "sba-long-terms-800w.webp",
        "Timeline blockers in SBA 7(a) and 504 approvals",
        800,
        450,
    ),
    "why-sba-loan-approval-taking-forever": (
        "sba-hero-800w.webp",
        "Extended SBA approval queues and how to reduce back-and-forth",
        800,
        450,
    ),
    "sba-loan-requirements": (
        "sba-flexible-use-560w.webp",
        "Overview of SBA eligibility, repayment capacity, and equity requirements",
        560,
        315,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("sba-intro-800w.webp", "U.S. small business SBA loan planning and lender matching", 800, 450),
    ("sba-7a-800w.webp", "SBA 7(a) general purpose financing for qualified small businesses", 800, 450),
    ("sba-504-800w.webp", "SBA 504 program for owner-occupied real estate and major equipment", 800, 450),
    ("sba-working-capital-800w.webp", "SBA-backed working capital and operating expense financing", 800, 450),
    ("sba-equipment-800w.webp", "Equipment purchases with SBA-guaranteed term financing", 800, 450),
    ("sba-real-estate-800w.webp", "Commercial real estate strategies using SBA loan programs", 800, 450),
]

BATCH24 = re.compile(r"<section\s[^>]*\bdata-batch24[^>]*>[\s\S]*?</section>\s*", re.I)

LEAD_FIGURE_BLOCK = re.compile(
    r"\s*<figure class=\"article-lead-visual\">[\s\S]*?</figure>\s*", re.I
)

FIGURE = """            <figure class="article-lead-visual">
              <picture>
                <source srcset="/assets/{src}" type="image/webp">
                <img src="/assets/{src}" alt="{alt}" width="{w}" height="{h}" loading="eager" decoding="async" fetchpriority="high">
              </picture>
            </figure>"""


def pick_image(slug: str) -> tuple[str, str, int, int]:
    if slug in SLUG_IMAGE:
        return SLUG_IMAGE[slug]
    i = sum(ord(c) for c in slug) % len(ROTATE)
    return ROTATE[i]


def strip_batch24(html: str) -> str:
    prev = ""
    while prev != html:
        prev = html
        html = BATCH24.sub("", html, count=1)
    return html


def _insert_offset_after_first_paragraph(chunk: str) -> int | None:
    """Return index in chunk to insert figure (0-based), or None."""
    m = re.search(r"<p\b[^>]*>[\s\S]*?</p>", chunk)
    if not m:
        return None
    after_p = chunk[m.end() :]
    ws = after_p[: len(after_p) - len(after_p.lstrip())]
    tail = after_p.lstrip()
    if tail.startswith("<ul"):
        close = tail.find("</ul>")
        if close < 0:
            return m.end()
        return m.end() + len(ws) + close + len("</ul>")
    if tail.startswith("<ol"):
        close = tail.find("</ol>")
        if close < 0:
            return m.end()
        return m.end() + len(ws) + close + len("</ol>")
    return m.end()


def insert_lead_figure(html: str, slug: str) -> str:
    marker = '<main class="blog-post-main">'
    start = html.find(marker)
    if start < 0:
        return html
    start += len(marker)
    end = html.find("</main>", start)
    if end < 0:
        return html
    chunk = html[start:end]
    off = _insert_offset_after_first_paragraph(chunk)
    if off is None:
        return html
    insert_at = start + off
    src, alt, w, h = pick_image(slug)
    fig = FIGURE.format(src=src, alt=alt.replace('"', "&quot;"), w=w, h=h)
    return html[:insert_at] + "\n" + fig + html[insert_at:]


def bump_modified(html: str) -> str:
    html = re.sub(
        r'<meta property="article:modified_time" content="[^"]*">',
        f'<meta property="article:modified_time" content="{MODIFIED}">',
        html,
        count=1,
    )
    html = re.sub(
        r'"dateModified":"[^"]*"',
        f'"dateModified":"{MODIFIED}"',
        html,
        count=1,
    )
    months = (
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    y, m, d = MODIFIED.split("-")
    label = f"{months[int(m)]} {int(d)}, {y}"
    html = re.sub(
        r'(<span class="blog-rail-label">Updated</span>\s+)\w+ \d+, \d{4}',
        rf"\g<1>{label}",
        html,
        count=1,
    )
    return html


def process_file(path: Path, slug: str) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = strip_batch24(raw)
    new = LEAD_FIGURE_BLOCK.sub("\n", new, count=1)
    new = insert_lead_figure(new, slug)
    new = bump_modified(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for d in sorted(SBA_ARTICLES.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        idx = d / "index.html"
        if not idx.is_file():
            continue
        if process_file(idx, d.name):
            changed += 1
            print("updated", d.name)
    print(f"Done. {changed} files changed.")


if __name__ == "__main__":
    main()
