"""
Move main-column content that appears after the in-article services-cta so it sits
before <section class="related-resources">. Safe to re-run (no-op when nothing follows CTA).

Usage: python scripts/reorder_article_supplemental_before_cta.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELATED = '<section class="related-resources"'
CTA_OPEN = '<div class="services-cta">'


def reorder_main(html: str) -> tuple[str, bool]:
    main_start = html.find("<main ")
    if main_start < 0:
        main_start = html.find("<main>")
    if main_start < 0:
        return html, False

    related_start = html.find(RELATED, main_start)
    if related_start < 0:
        return html, False

    cta_start = html.find(CTA_OPEN, related_start)
    if cta_start < 0:
        return html, False

    after_a = html.find("</a>", cta_start)
    if after_a < 0:
        return html, False
    cta_end = html.find("</div>", after_a) + len("</div>")

    main_end = html.find("</main>", cta_end)
    if main_end < 0:
        return html, False

    supplemental = html[cta_end:main_end].strip()
    if not supplemental:
        return html, False

    if related_start > cta_end:
        return html, False

    new_html = (
        html[:related_start]
        + supplemental
        + "\n"
        + html[related_start:cta_end]
        + "\n"
        + html[main_end:]
    )
    return new_html, True


def main() -> None:
    changed = []
    for path in sorted(ROOT.rglob("articles/*/index.html")):
        text = path.read_text(encoding="utf-8", errors="strict")
        if RELATED not in text or CTA_OPEN not in text:
            continue
        new_text, did = reorder_main(text)
        if not did:
            continue
        path.write_text(new_text, encoding="utf-8", newline="\n")
        changed.append(path)

    print("reordered", len(changed), "files")


if __name__ == "__main__":
    main()
