#!/usr/bin/env python3
"""
Root industry hub pages (*-business-financing.html): strip data-batch24, insert lead WebP
in the first intro section (after first <p> in .ef-intro-text), set article:modified_time,
and WebPage JSON-LD dateModified.

Run from repo root: python tools/industry_hub_pages_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODIFIED = "2026-03-27"

# filename -> (webp under /assets/, img alt)
HUB_LEAD: dict[str, tuple[str, str]] = {
    "agriculture-business-financing.html": (
        "agriculture-intro-800w.webp",
        "Farm and agricultural business financing overview",
    ),
    "auto-repair-business-financing.html": (
        "auto-repair-intro-800w.webp",
        "Auto repair shop and automotive service business financing",
    ),
    "construction-business-financing.html": (
        "construction-industry-overview-800w.webp",
        "Construction contractors and commercial project financing",
    ),
    "forestry-business-financing.html": (
        "forestry-intro-800w.webp",
        "Forestry, logging, and timber business financing",
    ),
    "landscaping-business-financing.html": (
        "landscaping-intro-800w.webp",
        "Landscaping and grounds maintenance business financing",
    ),
    "logistics-warehousing-business-financing.html": (
        "logistics-warehousing-intro-800w.webp",
        "Logistics, warehousing, and 3PL business financing",
    ),
    "manufacturing-business-financing.html": (
        "manufacturing-intro-800w.webp",
        "Manufacturing and production business financing",
    ),
    "medical-practices-business-financing.html": (
        "medical-practices-intro-800w.webp",
        "Medical and dental practice business financing",
    ),
    "restaurants-business-financing.html": (
        "restaurants-intro-800w.webp",
        "Restaurant and food service business financing",
    ),
    "trucking-business-financing.html": (
        "trucking-intro-800w.webp",
        "Trucking and freight business financing overview",
    ),
}

BATCH24 = re.compile(r"<section\s[^>]*\bdata-batch24[^>]*>[\s\S]*?</section>\s*", re.I)
LEAD_FIGURE_BLOCK = re.compile(
    r'\s*<figure class="article-lead-visual">[\s\S]*?</figure>\s*', re.I
)
INTRO_TEXT_BLOCK = re.compile(
    r'(<div class="ef-intro-text">)([\s\S]*?)(</div>\s*<div class="ef-intro-img")',
    re.I,
)
WEBPAGE_LD = re.compile(
    r'(<script type="application/ld\+json">\s*)'
    r'(\{"@context":"https://schema.org","@type":"WebPage","name":"[^"]*",'
    r'"description":"[^"]*","url":"https://axiantpartners.com/[^"]*"'
    r'(?:,"dateModified":"[^"]*")?\})'
    r'(\s*</script>)',
    re.I,
)

FIGURE = """                        <figure class="article-lead-visual">
                          <picture>
                            <source srcset="/assets/{src}" type="image/webp">
                            <img src="/assets/{src}" alt="{alt}" width="800" height="450" loading="eager" decoding="async" fetchpriority="high">
                          </picture>
                        </figure>"""


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


def patch_intro_text(html: str, src: str, alt: str) -> str:
    def repl(m: re.Match[str]) -> str:
        open_tag, inner, close_part = m.group(1), m.group(2), m.group(3)
        inner = LEAD_FIGURE_BLOCK.sub("\n", inner, count=1)
        off = _insert_offset_after_first_paragraph(inner)
        if off is None:
            return m.group(0)
        fig = FIGURE.format(src=src, alt=alt.replace('"', "&quot;"))
        return open_tag + inner[:off] + "\n" + fig + inner[off:] + close_part

    new_html, n = INTRO_TEXT_BLOCK.subn(repl, html, count=1)
    if n != 1:
        return html
    return new_html


def ensure_article_modified(html: str) -> str:
    if re.search(r'<meta\s+property="article:modified_time"', html):
        return re.sub(
            r'(<meta\s+property="article:modified_time"\s+content=")[^"]*(")',
            rf"\g<1>{MODIFIED}\g<2>",
            html,
            count=1,
        )
    return re.sub(
        r'(<meta\s+name="viewport"\s+content="[^"]*">)',
        rf'\1\n    <meta property="article:modified_time" content="{MODIFIED}">',
        html,
        count=1,
    )


def bump_webpage_json_ld(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        obj = m.group(2)
        if '"dateModified"' in obj:
            obj = re.sub(
                r'"dateModified":"[^"]*"',
                f'"dateModified":"{MODIFIED}"',
                obj,
                count=1,
            )
        else:
            obj = obj[:-1] + f',"dateModified":"{MODIFIED}"' + "}"
        return m.group(1) + obj + m.group(3)

    new_html, n = WEBPAGE_LD.subn(repl, html, count=1)
    if n != 1:
        return html
    return new_html


def process_file(path: Path) -> bool:
    key = path.name
    if key not in HUB_LEAD:
        return False
    src, alt = HUB_LEAD[key]
    raw = path.read_text(encoding="utf-8")
    new = strip_batch24(raw)
    new = patch_intro_text(new, src, alt)
    new = ensure_article_modified(new)
    new = bump_webpage_json_ld(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for name in sorted(HUB_LEAD):
        path = ROOT / name
        if not path.is_file():
            print("skip missing", name)
            continue
        if process_file(path):
            changed += 1
            print("updated", name)
    print(f"Done. {changed} hub pages changed.")


if __name__ == "__main__":
    main()
