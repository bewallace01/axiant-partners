#!/usr/bin/env python3
"""Add ?v=2 cache-busting to all hero/equipment WebP URLs in HTML files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_VERSION = "v=4"

def add_cache_bust(content: str) -> tuple[str, int]:
    """Add/update cache version on hero/equipment .webp URLs. Returns (new_content, count_changes)."""
    count = 0

    def apply_version(s: str) -> str:
        """Ensure URL has ?v=3, replacing existing ?v=X if present."""
        if f"?{CACHE_VERSION}" in s:
            return s
        if "?v=" in s:
            return re.sub(r"\?v=\d+", f"?{CACHE_VERSION}", s)
        return s.replace(".webp", f".webp?{CACHE_VERSION}")

    # Pattern 1: url('/assets/xxx.webp') or url("/assets/xxx.webp") or url('assets/xxx.webp')
    def repl_url(m):
        nonlocal count
        new = apply_version(m.group(0))
        if new != m.group(0):
            count += 1
        return new
    content = re.sub(
        r"url\(['\"]?(/?assets/[^'\)]+\.webp)(?:\?v=\d+)?['\"]?\)",
        lambda m: repl_url(m) if m else m.group(0),
        content
    )

    # Pattern 2: url('https://axiantpartners.com/assets/xxx.webp')
    def repl_abs(m):
        nonlocal count
        new = apply_version(m.group(0))
        if new != m.group(0):
            count += 1
        return new
    content = re.sub(
        r"url\(['\"]?(https://www\.axiantpartners\.com/assets/[^'\)]+\.webp)(?:\?v=\d+)?['\"]?\)",
        lambda m: repl_abs(m) if m else m.group(0),
        content
    )

    # Pattern 3: preload href="/assets/xxx.webp" or href="assets/xxx.webp" or href="https://..."
    def repl_preload(m):
        nonlocal count
        new = apply_version(m.group(0))
        if new != m.group(0):
            count += 1
        return new
    content = re.sub(
        r'href="([^"]*assets/[^"]+\.webp)(?:\?v=\d+)?"',
        lambda m: repl_preload(m) if m else m.group(0),
        content
    )

    # Pattern 4: srcset="/assets/xxx.webp" or srcset="assets/xxx.webp" (picture elements)
    def repl_srcset(m):
        nonlocal count
        new = apply_version(m.group(0))
        if new != m.group(0):
            count += 1
        return new
    content = re.sub(
        r'srcset="([^"]*assets/[^"]+\.webp)(?:\?v=\d+)?"',
        lambda m: repl_srcset(m) if m else m.group(0),
        content
    )

    return content, count


def main():
    total = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"  Skip {path}: {e}")
            continue
        new_content, count = add_cache_bust(content)
        if count > 0:
            path.write_text(new_content, encoding="utf-8")
            rel = path.relative_to(ROOT)
            print(f"  {rel}: {count} URLs updated")
            total += count
    print(f"\nDone. Updated {total} hero image URLs.")


if __name__ == "__main__":
    main()
