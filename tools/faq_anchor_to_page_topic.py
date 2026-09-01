#!/usr/bin/env python3
"""
Prepend one FAQPage Q/A tied to the page topic (Article headline or <title>, plus meta description)
when the first existing question does not already overlap the topic keywords.

Idempotent: skips if the first question already starts with ANCHOR_PREFIX.

Run from repo root: python tools/faq_anchor_to_page_topic.py
"""
from __future__ import annotations

import html as html_module
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANCHOR_PREFIX = "What does this page explain"

SCRIPT_RE = re.compile(
    r'(<script\s+type=["\']application/ld\+json["\']\s*>)([\s\S]*?)(</script>)',
    re.I,
)
TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.I)
DESC_RE = re.compile(
    r'<meta\s+name=["\']description["\']\s+content="([^"]*)"', re.I
)
HEADLINE_RE = re.compile(r'"@type":"Article","headline":"([^"]*)"')

STOP = frozenset(
    """
    the and for with you your how what when why that this from are can does
    its our their business financing loan loans axiant partners guide
    """.split()
)


def significant_tokens(text: str) -> set[str]:
    words = re.findall(r"[A-Za-z0-9]+", text.lower())
    return {w for w in words if len(w) > 3 and w not in STOP}


def extract_headline(html: str) -> str | None:
    m = HEADLINE_RE.search(html)
    if not m:
        return None
    return html_module.unescape(m.group(1).strip())


def extract_title(html: str) -> str:
    m = TITLE_RE.search(html)
    if not m:
        return ""
    return html_module.unescape(m.group(1).strip())


def extract_description(html: str) -> str:
    m = DESC_RE.search(html)
    if not m:
        return ""
    t = html_module.unescape(m.group(1).strip())
    return re.sub(r"\s+", " ", t)


def topic_from_headline_or_title(headline: str | None, title: str) -> str:
    if headline:
        h = headline.strip()
        if len(h) > 90:
            h = h[:87].rsplit(" ", 1)[0] + "…"
        return h
    t = title.split("|")[0].strip()
    return t[:90] + ("…" if len(t) > 90 else "")


def should_skip(main_entity: list, topic_tokens: set[str]) -> bool:
    if not main_entity:
        return True
    first = main_entity[0]
    if not isinstance(first, dict):
        return True
    name = first.get("name", "")
    if isinstance(name, str) and name.strip().startswith(ANCHOR_PREFIX):
        return True
    q_toks = significant_tokens(name)
    overlap = len(topic_tokens & q_toks)
    return overlap >= 2


def process_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if '"FAQPage"' not in raw and "'FAQPage'" not in raw:
        return False

    title = extract_title(raw)
    desc = extract_description(raw)
    headline = extract_headline(raw)
    topic_label = topic_from_headline_or_title(headline, title)
    topic_tokens = significant_tokens(topic_label)
    if not topic_label or len(desc) < 40:
        return False

    # Only adjust the first FAQPage JSON-LD block per file (some pages have two).
    faq_state = {"handled_first_faq": False}

    def replacer(m: re.Match[str]) -> str:
        open_tag, blob, close_tag = m.group(1), m.group(2).strip(), m.group(3)
        if '"FAQPage"' not in blob:
            return m.group(0)
        try:
            data = json.loads(blob)
        except json.JSONDecodeError:
            return m.group(0)
        if data.get("@type") != "FAQPage":
            return m.group(0)
        if faq_state["handled_first_faq"]:
            return m.group(0)
        faq_state["handled_first_faq"] = True

        main_entity = data.get("mainEntity")
        if not isinstance(main_entity, list):
            return m.group(0)
        if should_skip(main_entity, topic_tokens):
            return m.group(0)

        q_text = f"{ANCHOR_PREFIX} about {topic_label}?"
        a_text = desc
        if len(a_text) > 320:
            a_text = a_text[:317].rsplit(" ", 1)[0] + "…"

        anchor = {
            "@type": "Question",
            "name": q_text,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a_text,
            },
        }
        data["mainEntity"] = [anchor] + main_entity
        new_blob = json.dumps(data, ensure_ascii=True, separators=(",", ":"))
        return open_tag + "\n    " + new_blob + "\n    " + close_tag

    new_raw = SCRIPT_RE.sub(replacer, raw)
    if new_raw == raw:
        return False
    path.write_text(new_raw, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        if process_file(path):
            changed += 1
            print("updated", path.relative_to(ROOT))
    print(f"Done. {changed} files updated.")


if __name__ == "__main__":
    main()
