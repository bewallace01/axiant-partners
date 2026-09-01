#!/usr/bin/env python3
"""Find identical FAQPage mainEntity payloads across HTML files."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>([\s\S]*?)</script>',
    re.I,
)


def main() -> None:
    faq_hashes: dict[str, list[str]] = defaultdict(list)
    for p in ROOT.rglob("*.html"):
        if "node_modules" in p.parts:
            continue
        raw = p.read_text(encoding="utf-8", errors="replace")
        for m in SCRIPT_RE.finditer(raw):
            blob = m.group(1).strip()
            if '"FAQPage"' not in blob and "'FAQPage'" not in blob:
                continue
            try:
                j = json.loads(blob)
            except json.JSONDecodeError:
                continue
            if j.get("@type") != "FAQPage":
                continue
            key = json.dumps(j.get("mainEntity", []), sort_keys=True)
            faq_hashes[key].append(str(p.relative_to(ROOT)))

    dups = {k: v for k, v in faq_hashes.items() if len(v) > 1}
    print(f"Unique FAQ mainEntity sets: {len(faq_hashes)}")
    print(f"Duplicate FAQ blocks (2+ files): {len(dups)}")
    for v in sorted(dups.values(), key=lambda x: -len(x))[:25]:
        print(f"\n--- {len(v)} files ---")
        for path in v[:6]:
            print(f"  {path}")
        if len(v) > 6:
            print(f"  ... +{len(v) - 6} more")


if __name__ == "__main__":
    main()
