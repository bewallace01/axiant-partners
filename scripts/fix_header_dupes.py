"""Remove duplicate dns-prefetch/theme-color blocks accidentally pasted inside <header>."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERN = re.compile(
    r"(?P<open>\n\s*<header>)\s*\n"
    r'<link rel="dns-prefetch" href="https://fonts.googleapis.com">\s*\n'
    r'<link rel="dns-prefetch" href="https://fonts.gstatic.com">\s*\n'
    r'<link rel="dns-prefetch" href="https://www.googletagmanager.com">\s*\n'
    r'<meta http-equiv="X-UA-Compatible" content="IE=edge">\s*\n'
    r'<meta name="theme-color" content="#0d1f3c">\s*\n',
    re.MULTILINE,
)


def main() -> None:
    changed = 0
    for path in ROOT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        new, n = PATTERN.subn(r"\g<open>\n", text)
        if n:
            path.write_text(new, encoding="utf-8")
            changed += n
            print(f"{path.relative_to(ROOT)}: {n}")
    print(f"Total replacements: {changed}")


if __name__ == "__main__":
    main()
