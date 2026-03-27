#!/usr/bin/env python3
"""
Working capital loan articles: strip batch24 sections if present, insert WebP lead visual,
bump modified dates. Mirrors tools/sba_article_seo_pass.py for this vertical.

Run from repo root: python tools/working_capital_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "working-capital-loans" / "articles"
MODIFIED = "2026-04-03"

# (asset filename, alt, width, height)
SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "working-capital-loan-requirements": (
        "wcl-hero-operations-800w.webp",
        "Working capital loan requirements: cash flow, time in business, and bank statements",
        800,
        450,
    ),
    "what-is-working-capital-loan-how-does-it-work": (
        "wcl-intro-cashflow-800w.webp",
        "How working capital financing supports day-to-day business operations",
        800,
        450,
    ),
    "what-credit-score-needed-working-capital-loan": (
        "wcl-amounts-by-industry-800w.webp",
        "Credit tiers and working capital approval by industry and cash flow",
        800,
        450,
    ),
    "how-much-can-you-qualify-for-working-capital-loan": (
        "wcl-amounts-by-industry-800w.webp",
        "How lenders size working capital offers from revenue and deposits",
        800,
        450,
    ),
    "how-fast-can-you-get-working-capital-loan": (
        "wcl-speed-funding-800w.webp",
        "Fast working capital funding timelines and same-week options",
        800,
        450,
    ),
    "what-do-lenders-look-for-working-capital-loan-application": (
        "wcl-payroll-operations-800w.webp",
        "Lender underwriting focus for working capital applications",
        800,
        450,
    ),
    "working-capital-loan-vs-business-line-of-credit": (
        "wcl-flexible-use-800w.webp",
        "Comparing term working capital products with revolving business credit",
        800,
        450,
    ),
    "when-is-working-capital-loan-not-right-option": (
        "wcl-multiple-structures-800w.webp",
        "When to choose a different financing structure instead of working capital term debt",
        800,
        450,
    ),
    "emergency-business-loans-fast-funding": (
        "wcl-emergency-reserves-800w.webp",
        "Emergency business funding and fast working capital for urgent cash needs",
        800,
        450,
    ),
    "business-loans-for-bad-credit": (
        "wcl-conserve-capital-800w.webp",
        "Working capital and short-term options when business credit is challenged",
        800,
        450,
    ),
    "reasons-working-capital-loan-keeps-denied": (
        "wcl-receivables-800w.webp",
        "Common reasons working capital applications are declined and how to respond",
        800,
        450,
    ),
    "reasons-you-dont-qualify-for-working-capital-you-need": (
        "wcl-multiple-structures-560w.webp",
        "Qualification gaps for working capital and paths to improve approval odds",
        560,
        315,
    ),
    "why-your-working-capital-application-stuck-in-review": (
        "wcl-speed-funding-560w.webp",
        "Why working capital underwriting stalls and how to unblock the file",
        560,
        315,
    ),
    "working-capital-loan-mistakes-delay-deny-funding": (
        "wcl-conserve-capital-560w.webp",
        "Mistakes that delay or kill working capital approvals",
        560,
        315,
    ),
    "working-capital-loan-traps-to-avoid": (
        "wcl-flexible-use-560w.webp",
        "Fees, terms, and structures to watch in working capital offers",
        560,
        315,
    ),
    "how-to-get-out-of-bad-business-debt": (
        "wcl-receivables-560w.webp",
        "Restructuring expensive business debt and working capital strain",
        560,
        315,
    ),
    "refinancing-business-debt-mistakes-cost-you": (
        "wcl-growth-expansion-800w.webp",
        "Refinancing business debt without repeating costly mistakes",
        800,
        450,
    ),
    "whats-keeping-you-from-refinancing-business-debt": (
        "wcl-multiple-structures-1200w.webp",
        "Barriers to refinancing business debt and working capital stacks",
        1200,
        675,
    ),
    "working-capital-loan-seasonal-businesses": (
        "wcl-retail-seasonal-800w.webp",
        "Seasonal businesses using working capital for inventory and payroll cycles",
        800,
        450,
    ),
    "working-capital-loan-staffing-agencies": (
        "wcl-payroll-operations-560w.webp",
        "Staffing agencies bridging payroll and client payment timing with working capital",
        560,
        315,
    ),
    "working-capital-loan-wholesalers-distributors": (
        "logistics-warehousing-working-capital-800w.webp",
        "Wholesalers and distributors financing inventory and receivable gaps",
        800,
        450,
    ),
    "working-capital-loan-war-driven-cost-increases-trucking-construction-landscaping": (
        "trucking-working-capital-draws-800w.webp",
        "Trucking, construction, and landscaping firms managing fuel and material cost spikes",
        800,
        450,
    ),
    "war-fuel-material-costs-cash-flow-squeezed-options": (
        "manufacturing-working-capital-800w.webp",
        "Options when fuel and material costs squeeze operating cash flow",
        800,
        450,
    ),
    "war-client-slow-orders-business-loan-bridge-gap": (
        "wcl-receivables-1200w.webp",
        "Bridging cash flow when customer orders or payments slow",
        1200,
        675,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("wcl-intro-cashflow-800w.webp", "Small business working capital and operating cash flow financing", 800, 450),
    ("wcl-speed-funding-800w.webp", "Fast working capital for payroll, inventory, and short-term needs", 800, 450),
    ("wcl-flexible-use-800w.webp", "Flexible use of funds with working capital loan products", 800, 450),
    ("wcl-growth-expansion-800w.webp", "Growth and expansion supported by working capital financing", 800, 450),
    ("wcl-contractors-800w.webp", "Contractors managing job costs with working capital solutions", 800, 450),
    ("wcl-inventory-seasonal-800w.webp", "Inventory and seasonal peaks funded with working capital", 800, 450),
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
