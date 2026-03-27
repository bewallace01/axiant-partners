#!/usr/bin/env python3
"""
Business line of credit articles: strip batch24 if present, insert WebP lead visual, bump dates.

Run: python tools/business_line_of_credit_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "business-line-of-credit" / "articles"
MODIFIED = "2026-04-05"

SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "business-line-of-credit-requirements": (
        "bloc-line-of-credit-approval-800w.webp",
        "Business line of credit requirements: revenue, time in business, and credit",
        800,
        450,
    ),
    "business-line-of-credit-for-startups": (
        "bloc-growth-800w.webp",
        "Startup and newer businesses qualifying for a business line of credit",
        800,
        450,
    ),
    "business-line-of-credit-vs-term-loan": (
        "bloc-refinancing-800w.webp",
        "Choosing between a revolving line of credit and a term loan",
        800,
        450,
    ),
    "documents-needed-business-line-of-credit": (
        "bloc-line-of-credit-approval-800w.webp",
        "Documents lenders request for a business line of credit application",
        800,
        450,
    ),
    "do-you-need-collateral-business-line-of-credit": (
        "bloc-flexible-capital-800w.webp",
        "Secured versus unsecured business lines of credit and collateral",
        800,
        450,
    ),
    "secured-vs-unsecured-business-line-of-credit": (
        "bloc-revolving-cycle-800w.webp",
        "Secured and unsecured LOC structures and pricing tradeoffs",
        800,
        450,
    ),
    "how-fast-can-you-get-approved-business-line-of-credit": (
        "bloc-fast-draw-800w.webp",
        "How quickly you can get approved and access a business line of credit",
        800,
        450,
    ),
    "line-of-credit-for-contractors": (
        "bloc-contractors-800w.webp",
        "Contractors using a line of credit for job costs and cash flow",
        800,
        450,
    ),
    "line-of-credit-for-ecommerce-inventory": (
        "bloc-seasonal-inventory-800w.webp",
        "E-commerce and inventory cycles funded with a revolving line of credit",
        800,
        450,
    ),
    "line-of-credit-for-law-firms": (
        "bloc-hero-business-office-800w.webp",
        "Professional services firms bridging receivables with a line of credit",
        800,
        450,
    ),
    "open-line-of-credit-now-before-wartime-inflation-rates-higher": (
        "bloc-emergency-800w.webp",
        "Locking in line of credit capacity before rates or conditions tighten",
        800,
        450,
    ),
    "payroll-costs-up-inflation-line-of-credit-keep-workers": (
        "bloc-payroll-operations-800w.webp",
        "Using a line of credit to smooth payroll when costs rise",
        800,
        450,
    ),
    "reasons-line-of-credit-draw-request-gets-declined": (
        "bloc-revolving-cycle-800w.webp",
        "Why draw requests on a business line of credit get declined",
        800,
        450,
    ),
    "red-flags-line-of-credit-offers": (
        "bloc-pay-only-what-you-use-800w.webp",
        "Red flags in business line of credit offers and agreements",
        800,
        450,
    ),
    "what-are-typical-business-line-of-credit-rates": (
        "bloc-line-of-credit-approval-800w.webp",
        "Typical rate ranges and pricing on business lines of credit",
        800,
        450,
    ),
    "what-credit-score-needed-business-line-of-credit": (
        "bloc-line-of-credit-approval-560w.webp",
        "Credit score bands and approval odds for a business line of credit",
        560,
        315,
    ),
    "what-do-lenders-look-for-business-line-of-credit": (
        "bloc-receivables-800w.webp",
        "What lenders underwrite on business line of credit applications",
        800,
        450,
    ),
    "whats-holding-you-back-business-line-of-credit": (
        "bloc-refinancing-800w.webp",
        "Common blockers to business line of credit approval",
        800,
        450,
    ),
    "why-business-lines-of-credit-get-cut-or-revoked": (
        "bloc-seasonal-retail-800w.webp",
        "Why lenders reduce or revoke business line of credit limits",
        800,
        450,
    ),
    "why-line-of-credit-application-keeps-pending": (
        "bloc-fast-draw-560w.webp",
        "Why a line of credit application stays in pending or review",
        560,
        315,
    ),
    "why-line-of-credit-limit-too-low": (
        "bloc-growth-560w.webp",
        "Why approved line of credit limits come in lower than requested",
        560,
        315,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("bloc-line-of-credit-approval-800w.webp", "Business line of credit approval and revolving capital", 800, 450),
    ("restaurants-line-of-credit-800w.webp", "Restaurant and retail lines of credit for operations", 800, 450),
    ("manufacturing-line-of-credit-800w.webp", "Manufacturing businesses using revolving credit", 800, 450),
    ("trucking-line-of-credit-800w.webp", "Trucking and fleet operations with a business LOC", 800, 450),
    ("logistics-warehousing-line-of-credit-800w.webp", "Logistics and warehousing working capital lines", 800, 450),
    ("bloc-flexible-capital-800w.webp", "Flexible revolving capital for small businesses", 800, 450),
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
