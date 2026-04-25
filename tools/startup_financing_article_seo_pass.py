#!/usr/bin/env python3
"""
Startup financing articles: strip batch24 if present, insert WebP lead visual, bump dates.

Run: python tools/startup_financing_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "startup-financing" / "articles"
MODIFIED = "2026-04-07"

SLUG_IMAGE: dict[str, tuple[str, str, int, int]] = {
    "best-startup-financing-options-by-stage": (
        "startup-financing-options-800w.webp",
        "Startup financing options mapped by business stage and use case",
        800,
        450,
    ),
    "build-business-credit-fast-startup": (
        "startup-financing-growth-800w.webp",
        "Building business credit early for better startup financing access",
        800,
        450,
    ),
    "estimate-startup-funding-needs-template-formula": (
        "startup-financing-intro-800w.webp",
        "Estimating how much startup funding to raise before you apply",
        800,
        450,
    ),
    "finance-inventory-new-ecommerce-startup": (
        "startup-financing-equipment-800w.webp",
        "Inventory and ecommerce startup financing strategies",
        800,
        450,
    ),
    "finance-new-business-without-giving-up-equity": (
        "startup-financing-advisor-800w.webp",
        "Debt and non-dilutive paths to fund a new business",
        800,
        450,
    ),
    "how-fast-can-startup-financing-fund": (
        "startup-financing-hero-800w.webp",
        "How quickly startup financing can fund after approval",
        800,
        450,
    ),
    "how-to-qualify-for-startup-financing": (
        "startup-financing-intro-800w.webp",
        "Qualifying for startup financing: credit, plan, and documentation",
        800,
        450,
    ),
    "sba-microloan-startup-approval-guide": (
        "startup-financing-working-capital-800w.webp",
        "SBA Microloan and small-balance startup approval considerations",
        800,
        450,
    ),
    "startup-equipment-financing-guide": (
        "startup-financing-equipment-800w.webp",
        "Equipment financing for startups and newer businesses",
        800,
        450,
    ),
    "startup-financing-application-checklist-2026": (
        "startup-financing-intro-560w.webp",
        "Checklist for a complete startup financing application",
        560,
        315,
    ),
    "startup-financing-credit-score-guide": (
        "startup-financing-advisor-560w.webp",
        "Credit scores and personal credit in startup underwriting",
        560,
        315,
    ),
    "startup-financing-denied-what-to-do": (
        "startup-financing-options-560w.webp",
        "Next steps after a startup financing decline",
        560,
        315,
    ),
    "startup-financing-documents-checklist": (
        "startup-financing-intro-800w.webp",
        "Documents lenders commonly request for startup financing",
        800,
        450,
    ),
    "startup-financing-mistakes-to-avoid": (
        "startup-financing-growth-560w.webp",
        "Mistakes that hurt startup financing approvals",
        560,
        315,
    ),
    "startup-financing-no-revenue-options": (
        "startup-financing-options-800w.webp",
        "Financing options when the business has little or no revenue yet",
        800,
        450,
    ),
    "startup-financing-rates-fees-costs": (
        "startup-financing-advisor-800w.webp",
        "Rates, fees, and total cost of startup financing products",
        800,
        450,
    ),
    "startup-financing-requirements-2026": (
        "startup-financing-hero-800w.webp",
        "Current requirements for startup financing programs",
        800,
        450,
    ),
    "startup-financing-use-of-funds-guide": (
        "startup-financing-working-capital-800w.webp",
        "Use-of-funds planning for startup loan and credit requests",
        800,
        450,
    ),
    "startup-financing-vs-line-of-credit": (
        "startup-financing-options-800w.webp",
        "Startup term financing compared with a business line of credit",
        800,
        450,
    ),
    "startup-line-of-credit-vs-term-loan": (
        "startup-financing-growth-800w.webp",
        "Choosing between a startup line of credit and a term loan",
        800,
        450,
    ),
    "startup-loan-red-flags-fees-terms-fine-print": (
        "startup-financing-advisor-560w.webp",
        "Red flags in startup loan offers and contracts",
        560,
        315,
    ),
    "startup-working-capital-loan-under-30-days": (
        "startup-financing-working-capital-800w.webp",
        "Fast working capital options for startups on tight timelines",
        800,
        450,
    ),
}

ROTATE: list[tuple[str, str, int, int]] = [
    ("startup-financing-hero-800w.webp", "Startup financing for launch and early growth", 800, 450),
    ("startup-financing-intro-800w.webp", "Founders exploring startup funding paths", 800, 450),
    ("startup-financing-growth-800w.webp", "Growth capital for early-stage businesses", 800, 450),
    ("startup-financing-options-800w.webp", "Comparing startup financing products and structures", 800, 450),
    ("startup-financing-equipment-800w.webp", "Startup equipment and asset-backed financing", 800, 450),
    ("startup-financing-working-capital-800w.webp", "Working capital for startups and new operators", 800, 450),
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
