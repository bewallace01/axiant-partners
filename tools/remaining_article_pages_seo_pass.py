#!/usr/bin/env python3
"""
Long-tail article pages not covered by vertical-specific passes:
  - articles/<slug>/index.html (site-wide /articles hub)
  - equipment/<category>/<slug>/index.html (how-to / deep equipment articles)

Strips data-batch24, normalizes lead WebP after first intro block in <main class="blog-post-main">,
bumps article meta, JSON-LD Article dateModified, and rail "Updated" when present.

Run from repo root: python tools/remaining_article_pages_seo_pass.py
"""
from __future__ import annotations

import html as html_module
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MODIFIED = "2026-04-10"

# Root /articles: rotate neutral business-financing visuals (800w exists in /assets/)
ARTICLES_ROTATE: list[tuple[str, str, int, int]] = [
    ("equipment-financing-hero-800w.webp", "Business financing and equipment funding guidance", 800, 450),
    ("wcl-intro-cashflow-800w.webp", "Working capital and cash flow for small businesses", 800, 450),
    ("sba-intro-800w.webp", "SBA and small business loan programs", 800, 450),
]

# Fallback when og:image has no 800w variant on disk
EQUIP_FALLBACK_ROTATE: list[tuple[str, str, int, int]] = [
    ("equipment-financing-hero-800w.webp", "Equipment financing options for U.S. businesses", 800, 450),
    ("sba-equipment-800w.webp", "Equipment loans and leases for commercial assets", 800, 450),
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


def is_target_path(path: Path) -> bool:
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        return False
    parts = rel.parts
    # articles/<slug>/index.html (not articles/index.html — that has only 2 parts)
    if len(parts) == 3 and parts[0] == "articles":
        return True
    # equipment/<cat>/<slug>/index.html -> 4 parts
    if len(parts) == 4 and parts[0] == "equipment" and parts[3] == "index.html":
        return True
    return False


def pick_image_articles(slug: str) -> tuple[str, str, int, int]:
    i = sum(ord(c) for c in slug) % len(ARTICLES_ROTATE)
    return ARTICLES_ROTATE[i]


def pick_image_equipment(html: str, slug: str) -> tuple[str, str, int, int]:
    om = re.search(
        r'<meta\s+property="og:image"\s+content="https://axiantpartners\.com/assets/([^"]+)"',
        html,
        re.I,
    )
    am = re.search(
        r'<meta\s+property="og:image:alt"\s+content="([^"]*)"', html, re.I
    )
    alt = html_module.unescape(am.group(1).strip()) if am else "Equipment financing"
    if om:
        fname = om.group(1).strip()
        stem = Path(fname).stem
        if stem.endswith("-800w"):
            src = fname
        else:
            candidate = f"{stem}-800w.webp"
            src = candidate if (ASSETS / candidate).is_file() else fname
        return (src, alt or "Equipment financing illustration", 800, 450)
    i = sum(ord(c) for c in slug) % len(EQUIP_FALLBACK_ROTATE)
    return EQUIP_FALLBACK_ROTATE[i]


def pick_image(path: Path, html: str) -> tuple[str, str, int, int]:
    rel = path.relative_to(ROOT)
    slug = path.parent.name
    if rel.parts[0] == "articles":
        return pick_image_articles(slug)
    return pick_image_equipment(html, slug)


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


def insert_lead_figure(html: str, path: Path) -> str:
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
    src, alt, w, h = pick_image(path, html)
    fig = FIGURE.format(src=src, alt=alt.replace('"', "&quot;"), w=w, h=h)
    return html[:insert_at] + "\n" + fig + html[insert_at:]


def ensure_article_modified_meta(html: str) -> str:
    if re.search(r'<meta\s+property="article:modified_time"', html):
        return re.sub(
            r'(<meta\s+property="article:modified_time"\s+content=")[^"]*(")',
            rf"\g<1>{MODIFIED}\g<2>",
            html,
            count=1,
        )
    return re.sub(
        r'(<meta\s+property="article:published_time"\s+content="[^"]*">)',
        rf'\1\n    <meta property="article:modified_time" content="{MODIFIED}">',
        html,
        count=1,
    )


def bump_article_json_ld_line(html: str) -> str:
    lines = html.split("\n")
    out: list[str] = []
    for line in lines:
        if '"@type":"Article"' in line and '"datePublished"' in line and "schema.org" in line:
            if '"dateModified"' in line:
                line = re.sub(
                    r'"dateModified":"[^"]*"',
                    f'"dateModified":"{MODIFIED}"',
                    line,
                    count=1,
                )
            else:
                line = re.sub(
                    r'("datePublished":"[^"]*")',
                    rf'\1,"dateModified":"{MODIFIED}"',
                    line,
                    count=1,
                )
        out.append(line)
    return "\n".join(out)


def bump_rail_updated(html: str) -> str:
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
    return re.sub(
        r'(<span class="blog-rail-label">Updated</span>\s+)\w+ \d+, \d{4}',
        rf"\g<1>{label}",
        html,
        count=1,
    )


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if "article-page" not in raw or "blog-post-main" not in raw:
        return False
    new = strip_batch24(raw)
    new = LEAD_FIGURE_BLOCK.sub("\n", new, count=1)
    new = insert_lead_figure(new, path)
    new = ensure_article_modified_meta(new)
    new = bump_article_json_ld_line(new)
    new = bump_rail_updated(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("index.html")):
        if "node_modules" in path.parts:
            continue
        if not is_target_path(path):
            continue
        if process_file(path):
            changed += 1
            print("updated", path.relative_to(ROOT))
    print(f"Done. {changed} files changed.")


if __name__ == "__main__":
    main()
