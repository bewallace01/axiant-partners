#!/usr/bin/env python3
"""One-time helper: replace https://www.axiantpartners.com with https://axiantpartners.com in text assets."""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OLD = "https://www.axiantpartners.com"
NEW = "https://axiantpartners.com"
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".cursor"}
EXT = {".html", ".xml", ".js", ".py", ".md", ".css", ".txt", ".json", ".webmanifest", ".csv"}


def main():
    n_files = n_repl = 0
    for path in BASE.rglob("*"):
        if not path.is_file():
            continue
        if any(p in path.parts for p in SKIP_DIRS):
            continue
        if path.suffix.lower() not in EXT and path.name not in ("robots.txt",):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if OLD not in text:
            continue
        new_text = text.replace(OLD, NEW)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            n_files += 1
            n_repl += text.count(OLD)
    print(f"Updated {n_files} files ({n_repl} replacements)")


if __name__ == "__main__":
    main()
