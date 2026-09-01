#!/usr/bin/env python3
"""
Rebuild the right-rail 'On this page' list from <h2 id="..."> order inside
<main class="blog-post-main">. Skips the related-resources section.
Only touches pages that use article-page + blog-post-toc-list.

Usage: python tools/sync_article_toc.py
"""
from __future__ import annotations

import html as html_module
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAIN_RE = re.compile(
    r'<main\s+class="blog-post-main"[^>]*>([\s\S]*?)</main>',
    re.I,
)
H2_RE = re.compile(r'<h2\s[^>]*\bid="([^"]+)"[^>]*>([\s\S]*?)</h2>', re.I)
RELATED_RE = re.compile(
    r'<section\s+class="related-resources"[\s\S]*?</section>',
    re.I,
)
TOC_UL_RE = re.compile(
    r'(<ul class="blog-post-toc-list">)([\s\S]*?)(</ul>)',
    re.I,
)


def headings_from_main(main_inner: str) -> list[tuple[str, str]]:
    main_inner = RELATED_RE.sub("", main_inner)
    out: list[tuple[str, str]] = []
    for m in H2_RE.finditer(main_inner):
        hid, inner = m.group(1), m.group(2)
        text = re.sub(r"<[^>]+>", "", inner)
        text = html_module.unescape(text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            out.append((hid, text))
    return out


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if "article-page" not in raw or "blog-post-toc-list" not in raw:
        return False
    mm = MAIN_RE.search(raw)
    if not mm:
        return False
    items = headings_from_main(mm.group(1))
    if not items:
        return False

    lis = "\n".join(
        f'              <li><a href="#{hid}">{html_module.escape(title)}</a></li>'
        for hid, title in items
    )
    new_block = f"<ul class=\"blog-post-toc-list\">\n{lis}\n            </ul>"

    def repl(m: re.Match[str]) -> str:
        return new_block

    new_raw, n = TOC_UL_RE.subn(repl, raw, count=1)
    if n != 1 or new_raw == raw:
        return False
    path.write_text(new_raw, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("index.html")):
        if "node_modules" in path.parts:
            continue
        if process_file(path):
            print(path.relative_to(ROOT))
            changed += 1
    print(f"Done. {changed} files updated.")


if __name__ == "__main__":
    main()
