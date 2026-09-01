"""One-off migration: article-page markup + article-rail.css link for blog articles."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V_RAIL = "2026033015"
V_BLOG = "2026033014"
RAIL_LINK = f'<link rel="stylesheet" href="/article-rail.css?v={V_RAIL}">'
BLOG_LINK = f'<link rel="stylesheet" href="/blog-layout.css?v={V_BLOG}">'

LEFT_ASIDE = re.compile(
    r'<aside\s+class="([^"]*blog-post-rail-left[^"]*)"\s*>(.*?)</aside>',
    re.DOTALL | re.IGNORECASE,
)

RIGHT_ASIDE = re.compile(
    r'<aside\s+class="([^"]*blog-post-rail-right[^"]*)"\s*>\s*'
    r'<div\s+class="blog-rail-card"\s*>\s*'
    r'(<div\s+class="blog-rail-toc"[^>]*>.*?</div>)\s*'
    r'</div>\s*'
    r'</aside>',
    re.DOTALL | re.IGNORECASE,
)


def migrate_left_body(body: str) -> str:
    body = body.replace(
        '<div class="blog-rail-card blog-rail-cta">',
        '<div class="article-rail__block article-rail__block--cta blog-rail-cta">',
    )
    body = body.replace(
        '<div class="blog-rail-cta blog-rail-card">',
        '<div class="article-rail__block article-rail__block--cta blog-rail-cta">',
    )
    body = body.replace('<div class="blog-rail-card">', '<div class="article-rail__block">')
    return body


def migrate_left(html: str) -> tuple[str, bool]:
    m = LEFT_ASIDE.search(html)
    if not m:
        return html, False

    cls, body = m.group(1), m.group(2)
    if "article-rail__inner" in body:
        return html, False
    cls = cls.strip()
    if "article-rail--left" not in cls:
        cls = cls.replace(
            "blog-post-rail-left",
            "blog-post-rail-left article-rail article-rail--left",
            1,
        )
    body = migrate_left_body(body)
    replacement = f'<aside class="{cls}"><div class="article-rail__inner">{body}</div></aside>'
    return html[: m.start()] + replacement + html[m.end() :], True


def migrate_right(html: str) -> tuple[str, bool]:

    def repl(m: re.Match[str]) -> str:
        cls = m.group(1).strip()
        if "article-rail--right" not in cls:
            cls = cls.replace(
                "blog-post-rail-right",
                "blog-post-rail-right article-rail article-rail--right",
                1,
            )
        toc = m.group(2)
        return (
            f'<aside class="{cls}">'
            f'<div class="article-rail__inner article-rail__inner--toc">{toc}</div>'
            f"</aside>"
        )

    new_html, n = RIGHT_ASIDE.subn(repl, html, count=1)
    return new_html, n > 0


def ensure_article_page(html: str) -> str:
    if "article-page" in html and "blog-post-content article-page" in html.replace(
        "  ", " "
    ):
        return html
    return re.sub(
        r'class="form-container blog-post-content"',
        'class="form-container blog-post-content article-page"',
        html,
        count=1,
    )


def ensure_css(html: str) -> str:
    if "article-rail.css" in html:
        return html
    m = re.search(r'<link[^>]*href="[^"]*blog-layout\.css[^"]*"[^>]*>', html, re.I)
    if m:
        return html[: m.end()] + "\n" + RAIL_LINK + html[m.end() :]
    m2 = re.search(r'<link[^>]*href="[^"]*critical\.css[^"]*"[^>]*>', html, re.I)
    if m2:
        insert = f"\n{BLOG_LINK}\n{RAIL_LINK}"
        return html[: m2.end()] + insert + html[m2.end() :]
    return html


def process_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if "blog-post-rail-left" not in text:
        return "skip"
    if "article-rail__inner" in text and "article-page" in text:
        return "skip"
    orig = text
    text, left_ok = migrate_left(text)
    if not left_ok:
        return "skip_left"
    text, _ = migrate_right(text)
    text = ensure_article_page(text)
    text = ensure_css(text)
    if text != orig:
        path.write_text(text, encoding="utf-8", newline="\n")
        return "ok"
    return "unchanged"


def main() -> None:
    changed = skip = errors = 0
    for path in sorted(ROOT.rglob("index.html")):
        try:
            stat = process_file(path)
        except OSError as e:
            print(path, e, file=sys.stderr)
            errors += 1
            continue
        if stat == "ok":
            changed += 1
        elif stat == "skip":
            skip += 1
        elif stat == "skip_left":
            print("no left match:", path.relative_to(ROOT))
            errors += 1
    print(f"updated: {changed}, skipped (no rail / already done): {skip}, issues: {errors}")


if __name__ == "__main__":
    main()
