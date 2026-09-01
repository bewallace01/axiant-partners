#!/usr/bin/env python3
"""
Business term loan articles: strip batch24 if present, insert WebP lead visual, bump dates.

Run: python tools/business_term_loans_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "business-term-loans" / "articles"
MODIFIED = "2026-04-06"

SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "business-term-loan-requirements": (
        "btl-intro-800w.webp",
        "Business term loan requirements: revenue, credit, and documentation",
        800,
        450,
    ),
    "business-term-loan-vs-line-of-credit": (
        "btl-multiple-structures-800w.webp",
        "Term loan versus business line of credit: structure and use cases",
        800,
        450,
    ),
    "how-fast-can-you-get-business-term-loan": (
        "btl-speed-funding-800w.webp",
        "How quickly business term loan funds can reach your account",
        800,
        450,
    ),
    "how-much-can-you-qualify-for-business-term-loan": (
        "btl-amounts-industry-800w.webp",
        "How lenders size business term loan offers by industry and cash flow",
        800,
        450,
    ),
    "secured-business-loan-approval-timeline": (
        "btl-predictable-payments-800w.webp",
        "Timeline for secured business term loan approval and closing",
        800,
        450,
    ),
    "secured-vs-unsecured-business-term-loan": (
        "btl-refinancing-800w.webp",
        "Secured compared with unsecured business term loans",
        800,
        450,
    ),
    "term-loan-for-business-acquisition": (
        "btl-acquisition-800w.webp",
        "Term financing for buying a business or ownership interest",
        800,
        450,
    ),
    "term-loan-for-manufacturing-expansion": (
        "btl-equipment-800w.webp",
        "Term loans funding manufacturing capacity and equipment expansion",
        800,
        450,
    ),
    "term-loan-for-multi-unit-restaurant-expansion": (
        "btl-expansion-scene-800w.webp",
        "Multi-unit restaurant growth funded with business term debt",
        800,
        450,
    ),
    "term-loan-mistakes-cost-thousands": (
        "btl-conserve-capital-800w.webp",
        "Costly mistakes to avoid on business term loan applications",
        800,
        450,
    ),
    "what-credit-score-needed-business-term-loan": (
        "btl-amounts-industry-560w.webp",
        "Typical credit score expectations for business term loans",
        560,
        315,
    ),
    "what-do-lenders-look-for-business-term-loan": (
        "btl-hero-800w.webp",
        "What lenders underwrite on business term loan requests",
        800,
        450,
    ),
    "when-is-business-term-loan-not-right-option": (
        "btl-multiple-structures-560w.webp",
        "When a term loan is the wrong product for your capital need",
        560,
        315,
    ),
    "why-business-term-loan-application-stuck": (
        "btl-speed-funding-560w.webp",
        "Why business term loan applications stall in underwriting",
        560,
        315,
    ),
    "why-term-loan-funding-keeps-getting-pushed-back": (
        "btl-renovation-800w.webp",
        "Delays to term loan funding and how to close on schedule",
        800,
        450,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("btl-intro-800w.webp", "Business term loans for expansion, equipment, and working capital", 800, 450),
    ("btl-expansion-800w.webp", "Growth and expansion financed with term debt", 800, 450),
    ("btl-marketing-800w.webp", "Investing in growth with structured term financing", 800, 450),
    ("btl-conserve-capital-800w.webp", "Preserving cash while funding large purchases", 800, 450),
    ("btl-acquisition-scene-800w.webp", "Acquisition and buyout financing with term loans", 800, 450),
    ("btl-equipment-800w.webp", "Equipment and asset purchases via term loans", 800, 450),
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
