#!/usr/bin/env python3
"""
Equipment financing articles: strip batch24 sections if present, insert WebP lead visual,
bump modified dates.

Run from repo root: python tools/equipment_financing_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "equipment-financing" / "articles"
MODIFIED = "2026-04-04"

SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "equipment-financing-requirements": (
        "equipment-financing-hero-800w.webp",
        "Equipment financing requirements: collateral, credit, and cash flow for business assets",
        800,
        450,
    ),
    "what-credit-score-needed-equipment-financing": (
        "medical-practices-equipment-financing-800w.webp",
        "Credit expectations for equipment financing approvals by lender and asset type",
        800,
        450,
    ),
    "how-fast-can-equipment-financing-be-approved": (
        "semi-truck-equipment-800w.webp",
        "Fast equipment financing timelines for trucks and heavy assets",
        800,
        450,
    ),
    "documents-needed-equipment-financing": (
        "forklift-logistics-equipment-800w.webp",
        "Documentation checklist for equipment financing applications",
        800,
        450,
    ),
    "do-you-need-down-payment-for-equipment-financing": (
        "sba-equipment-800w.webp",
        "Down payment and advance structures for equipment loans and leases",
        800,
        450,
    ),
    "equipment-financing-no-money-down": (
        "sba-equipment-800w.webp",
        "Low- and no-money-down equipment financing structures",
        800,
        450,
    ),
    "equipment-financing-vs-sba-loan": (
        "sba-equipment-800w.webp",
        "Equipment financing compared with SBA-guaranteed equipment structures",
        800,
        450,
    ),
    "equipment-leasing-vs-loan-which-is-better": (
        "forklift-manufacturing-equipment-800w.webp",
        "Equipment lease versus loan: manufacturing and warehouse use cases",
        800,
        450,
    ),
    "equipment-lease-traps-lock-in-cost-more": (
        "cnc-machine-equipment-600w.webp",
        "Reading equipment lease terms to avoid lock-in and surprise costs",
        600,
        338,
    ),
    "trac-lease-benefits-saves-money": (
        "semi-truck-equipment-800w.webp",
        "TRAC and structured leases for trucks and titled equipment",
        800,
        450,
    ),
    "construction-heavy-equipment-financing": (
        "excavator-equipment-800w.webp",
        "Heavy equipment financing for construction and earthmoving fleets",
        800,
        450,
    ),
    "medical-dental-equipment-financing": (
        "medical-practices-equipment-financing-800w.webp",
        "Medical and dental practice equipment financing and leasing",
        800,
        450,
    ),
    "restaurant-commercial-kitchen-equipment-financing": (
        "restaurants-equipment-financing-800w.webp",
        "Commercial kitchen and restaurant equipment financing",
        800,
        450,
    ),
    "can-you-finance-used-equipment": (
        "forklift-logistics-equipment-800w.webp",
        "Financing used forklifts, trucks, and other pre-owned equipment",
        800,
        450,
    ),
    "equipment-financing-bad-credit": (
        "auto-repair-equipment-financing-800w.webp",
        "Equipment financing options when business or personal credit is challenged",
        800,
        450,
    ),
    "equipment-financing-new-businesses": (
        "startup-financing-equipment-560w.webp",
        "Newer businesses financing equipment with revenue and collateral",
        560,
        315,
    ),
    "equipment-financing-under-12-months": (
        "startup-financing-equipment-560w.webp",
        "Equipment financing for businesses under one year in operation",
        560,
        315,
    ),
    "equipment-financing-cash-businesses": (
        "restaurants-equipment-financing-800w.webp",
        "Equipment financing for cash-heavy and high-deposit businesses",
        800,
        450,
    ),
    "equipment-financing-bank-statements-red-flags": (
        "logistics-warehousing-equipment-financing-800w.webp",
        "Bank statement review for equipment underwriting and red flags",
        800,
        450,
    ),
    "equipment-financing-tax-returns-losses": (
        "manufacturing-fleet-equipment-600w.webp",
        "Equipment approvals when tax returns show losses or thin income",
        600,
        338,
    ),
    "equipment-financing-ucc-lien-approval": (
        "forklift-manufacturing-equipment-800w.webp",
        "UCC filings and lien priority in equipment finance deals",
        800,
        450,
    ),
    "equipment-financing-pre-approval": (
        "equipment-financing-hero-800w.webp",
        "Equipment pre-approval quotes and soft underwriting steps",
        800,
        450,
    ),
    "equipment-financing-denied-reasons-fixes": (
        "diagnostic-equipment-600w.webp",
        "Common equipment financing declines and how to fix the file",
        600,
        338,
    ),
    "why-equipment-financing-application-stuck": (
        "logistics-warehousing-equipment-financing-800w.webp",
        "Why equipment financing applications stall in underwriting",
        800,
        450,
    ),
    "whats-delaying-your-equipment-financing-close": (
        "dock-equipment-logistics-800w.webp",
        "Closing delays on equipment finance: titles, UCC, and funding conditions",
        800,
        450,
    ),
    "reasons-equipment-financing-approval-drags-on": (
        "dock-equipment-logistics-800w.webp",
        "Long equipment approval cycles and how to shorten them",
        800,
        450,
    ),
    "reasons-equipment-dealer-financing-falls-through": (
        "auto-repair-equipment-financing-800w.webp",
        "When dealer-arranged equipment financing does not close",
        800,
        450,
    ),
    "reasons-lenders-say-no-equipment-deal": (
        "diagnostic-scan-tool-equipment-560w.webp",
        "Why lenders decline equipment deals and what to change",
        560,
        315,
    ),
    "red-flags-equipment-finance-agreements": (
        "diagnostic-scan-tool-equipment-560w.webp",
        "Red flags in equipment finance contracts and disclosures",
        560,
        315,
    ),
    "supplier-costs-up-equipment-financing-free-up-cash": (
        "logistics-warehousing-equipment-financing-800w.webp",
        "Using equipment financing when supplier and input costs rise",
        800,
        450,
    ),
    "war-equipment-prices-buy-now-or-wait-finance": (
        "forestry-equipment-financing-800w.webp",
        "Equipment purchase timing and financing when asset prices move",
        800,
        450,
    ),
    "equipment-financing-approved-revenue-dropped-war-inflation": (
        "trucking-equipment-financing-800w.webp",
        "Equipment financing after revenue dips or cost shocks",
        800,
        450,
    ),
    "what-are-typical-equipment-financing-rates": (
        "equipment-financing-hero-800w.webp",
        "Typical rate ranges and factors for equipment loans and leases",
        800,
        450,
    ),
    "what-benefits-does-lease-have-equipment-financing": (
        "forklift-manufacturing-equipment-800w.webp",
        "Benefits of leasing versus buying business equipment outright",
        800,
        450,
    ),
    "what-do-lenders-look-at-equipment-financing-approval": (
        "lab-equipment-medical-800w.webp",
        "What lenders evaluate on equipment financing applications",
        800,
        450,
    ),
    "whats-stopping-you-equipment-financing": (
        "pallet-racking-equipment-600w.webp",
        "Removing blockers to equipment financing approval",
        600,
        338,
    ),
    "how-to-avoid-overpaying-equipment-financing": (
        "press-brake-equipment-600w.webp",
        "Avoiding overpriced equipment finance terms and fees",
        600,
        338,
    ),
    "can-equipment-financing-help-build-business-credit": (
        "equipment-financing-hero-800w.webp",
        "Building business credit with reported equipment financing",
        800,
        450,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("equipment-financing-hero-800w.webp", "Business equipment financing for trucks, machinery, and tools", 800, 450),
    ("trucking-equipment-financing-800w.webp", "Trucking and fleet equipment financing", 800, 450),
    ("landscaping-equipment-financing-800w.webp", "Landscaping and outdoor equipment financing", 800, 450),
    ("agriculture-equipment-financing-800w.webp", "Agricultural equipment loans and leases", 800, 450),
    ("auto-repair-equipment-financing-800w.webp", "Auto repair shop equipment financing", 800, 450),
    ("forestry-equipment-financing-800w.webp", "Forestry and logging equipment financing", 800, 450),
]

BATCH24 = re.compile(r"<section\s[^>]*\bdata-batch24[^>]*>[\s\S]*?</section>\s*", re.I)
LEAD_FIGURE_BLOCK = re.compile(
    r'\s*<figure class="article-lead-visual">[\s\S]*?</figure>\s*', re.I
)
MAIN_OPEN = re.compile(r'<main\s+class="blog-post-main"[^>]*>', re.I)

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
    mo = MAIN_OPEN.search(html)
    if not mo:
        return html
    start = mo.end()
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
    for d in sorted(ARTICLES.iterdir()):
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
