#!/usr/bin/env python3
"""
Industry long-form articles (construction-business-financing/, trucking-business-financing/):
strip data-batch24 if present, insert lead WebP after first intro block, bump modified dates.

Run from repo root: python tools/industry_articles_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODIFIED = "2026-03-27"


def m(src: str, alt: str, w: int = 800, h: int = 450) -> tuple[str, str, int, int]:
    return (src, alt, w, h)


CONSTRUCTION: dict[str, tuple[str, str, int, int]] = {
    "bonding-capacity-surety-cash-crunch": m(
        "construction-industry-overview-800w.webp",
        "Contractor bonding capacity, surety limits, and cash flow pressure",
    ),
    "change-orders-delaying-payments": m(
        "construction-hero-bg-800w.webp",
        "Construction change orders and delayed progress payments",
    ),
    "contractor-financing-mistakes-delay-deny-funding": m(
        "cbl-construction-800w.webp",
        "Contractor financing mistakes that delay or deny funding",
    ),
    "defense-contracts-equipment-financing-bid-axiant": m(
        "construction-industry-overview-800w.webp",
        "Defense contract bids, equipment, and contractor financing",
    ),
    "failed-inspections-punch-list-rework-delaying-payment": m(
        "construction-hero-bg-800w.webp",
        "Failed inspections, punch lists, and contractor payment timing",
    ),
    "material-deposits-supplier-cod-before-first-payment": m(
        "cbl-construction-800w.webp",
        "Material deposits, supplier COD, and cash before first draw",
    ),
    "mobilization-funding-before-first-draw": m(
        "construction-industry-overview-800w.webp",
        "Mobilization funding for contractors before the first progress draw",
    ),
    "permit-utility-deposit-cash-crunch": m(
        "construction-hero-bg-800w.webp",
        "Permits, utility deposits, and contractor cash flow gaps",
    ),
    "progress-payment-cash-flow-gaps": m(
        "construction-industry-overview-800w.webp",
        "Contractor cash flow between progress payments and draws",
    ),
    "retainage-cash-flow-gap": m(
        "cbl-construction-800w.webp",
        "Construction retainage and working capital gaps",
    ),
    "steel-lumber-prices-finance-job": m(
        "construction-hero-bg-800w.webp",
        "Steel, lumber price swings, and financing the job",
    ),
    "weather-delay-cash-crunch": m(
        "construction-industry-overview-800w.webp",
        "Weather delays, schedule slip, and contractor cash crunch",
    ),
    "working-capital-subcontractors-invoices": m(
        "cbl-construction-800w.webp",
        "Working capital for subcontractors, invoices, and pay cycles",
    ),
}

CONSTRUCTION_ROTATE: list[tuple[str, str, int, int]] = [
    m("construction-industry-overview-800w.webp", "Construction business financing and contractor operations"),
    m("construction-hero-bg-800w.webp", "Jobsite and construction industry financing context"),
    m("cbl-construction-800w.webp", "Commercial construction projects and capital needs"),
]

TRUCKING: dict[str, tuple[str, str, int, int]] = {
    "breakdown-repair-cash-crunch": m(
        "trucking-fleet-equipment-800w.webp",
        "Truck breakdowns, repair bills, and owner-operator cash flow",
    ),
    "broker-net-30-net-45-cash-gap": m(
        "trucking-working-capital-800w.webp",
        "Freight broker payment terms and trucking working capital gaps",
    ),
    "deadhead-miles-cash-drain": m(
        "trucking-amounts-800w.webp",
        "Deadhead miles, unpaid repositioning, and trucking margins",
    ),
    "detention-layover-pay-cash-crunch": m(
        "trucking-speed-funding-800w.webp",
        "Detention, layover pay, and cash timing for carriers",
    ),
    "fuel-advance-cash-crunch": m(
        "trucking-equipment-financing-800w.webp",
        "Fuel advances, diesel costs, and trucking liquidity",
    ),
    "fuel-surcharges-killing-margins-financing-owner-operators": m(
        "trucking-industry-lending-800w.webp",
        "Fuel surcharges, thin margins, and owner-operator financing",
    ),
    "ifta-quarterly-tax-bill-cash-crunch": m(
        "trucking-working-capital-800w.webp",
        "IFTA quarterly tax bills and trucking cash planning",
    ),
    "insurance-down-payment-renewal-cash-crunch": m(
        "trucking-intro-800w.webp",
        "Trucking insurance down payments, renewals, and cash crunch",
    ),
    "new-authority-cash-flow-before-first-pay": m(
        "trucking-acquisition-800w.webp",
        "New trucking authority and cash flow before first settlement",
    ),
    "truck-note-lease-payment-slow-freight-weeks": m(
        "trucking-equipment-financing-800w.webp",
        "Truck note or lease payments during slow freight weeks",
    ),
    "trucking-business-growth": m(
        "trucking-acquisition-800w.webp",
        "Growing a trucking business with the right financing mix",
    ),
    "working-capital-for-trucking": m(
        "trucking-working-capital-800w.webp",
        "Working capital for trucking companies and owner-operators",
    ),
}

TRUCKING_ROTATE: list[tuple[str, str, int, int]] = [
    m("trucking-industry-lending-800w.webp", "Trucking industry lending and fleet operations"),
    m("trucking-intro-800w.webp", "Commercial trucking and transportation financing"),
    m("trucking-working-capital-800w.webp", "Working capital for carriers and freight businesses"),
    m("trucking-equipment-financing-800w.webp", "Semi trucks and equipment financing for trucking"),
    m("trucking-fleet-equipment-800w.webp", "Fleet trucks, trailers, and asset-backed financing"),
    m("trucking-hero-bg-800w.webp", "Highway freight and trucking business context"),
]

INDUSTRY_CONFIG: list[tuple[str, dict[str, tuple[str, str, int, int]], list[tuple[str, str, int, int]]]] = [
    ("construction-business-financing", CONSTRUCTION, CONSTRUCTION_ROTATE),
    ("trucking-business-financing", TRUCKING, TRUCKING_ROTATE),
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


def pick_image(slug: str, slug_map: dict, rotate: list) -> tuple[str, str, int, int]:
    if slug in slug_map:
        return slug_map[slug]
    i = sum(ord(c) for c in slug) % len(rotate)
    return rotate[i]


def strip_batch24(html: str) -> str:
    prev = ""
    while prev != html:
        prev = html
        html = BATCH24.sub("", html, count=1)
    return html


def _insert_offset_after_first_paragraph(chunk: str) -> int | None:
    m0 = re.search(r"<p\b[^>]*>[\s\S]*?</p>", chunk)
    if not m0:
        return None
    after_p = chunk[m0.end() :]
    ws = after_p[: len(after_p) - len(after_p.lstrip())]
    tail = after_p.lstrip()
    if tail.startswith("<ul"):
        close = tail.find("</ul>")
        if close < 0:
            return m0.end()
        return m0.end() + len(ws) + close + len("</ul>")
    if tail.startswith("<ol"):
        close = tail.find("</ol>")
        if close < 0:
            return m0.end()
        return m0.end() + len(ws) + close + len("</ol>")
    return m0.end()


def insert_lead_figure(html: str, slug: str, slug_map: dict, rotate: list) -> str:
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
    src, alt, w, h = pick_image(slug, slug_map, rotate)
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
    y, mo, d = MODIFIED.split("-")
    label = f"{months[int(mo)]} {int(d)}, {y}"
    html = re.sub(
        r'(<span class="blog-rail-label">Updated</span>\s+)\w+ \d+, \d{4}',
        rf"\g<1>{label}",
        html,
        count=1,
    )
    return html


def process_file(path: Path, slug: str, slug_map: dict, rotate: list) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = strip_batch24(raw)
    new = LEAD_FIGURE_BLOCK.sub("\n", new, count=1)
    new = insert_lead_figure(new, slug, slug_map, rotate)
    new = bump_modified(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    total = 0
    for rel, slug_map, rotate in INDUSTRY_CONFIG:
        base = ROOT / rel
        if not base.is_dir():
            print("skip missing", rel)
            continue
        for d in sorted(base.iterdir()):
            if not d.is_dir() or d.name.startswith("."):
                continue
            idx = d / "index.html"
            if not idx.is_file():
                continue
            if process_file(idx, d.name, slug_map, rotate):
                total += 1
                print("updated", rel, d.name)
    print(f"Done. {total} files changed across {len(INDUSTRY_CONFIG)} industry hubs.")


if __name__ == "__main__":
    main()
