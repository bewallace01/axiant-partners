#!/usr/bin/env python3
"""Minify CSS and JS for production. Run from project root."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def minify_css(src: Path, dst: Path) -> None:
    import csscompressor
    out = csscompressor.compress(src.read_text(encoding="utf-8", errors="replace"))
    dst.write_text(out, encoding="utf-8")

def minify_js(src: Path, dst: Path) -> None:
    import rjsmin
    out = rjsmin.jsmin(src.read_text(encoding="utf-8", errors="replace"))
    dst.write_text(out, encoding="utf-8")

def main():
    for path in [ROOT / "critical.css", ROOT / "styles.css"]:
        if path.exists():
            import csscompressor
            out = csscompressor.compress(path.read_text(encoding="utf-8", errors="replace"))
            path.write_text(out, encoding="utf-8")
            print(f"Minified {path.name} ({len(out)} bytes)")
    for path in [ROOT / "language-switcher.js", ROOT / "script.js"]:
        if path.exists():
            import rjsmin
            out = rjsmin.jsmin(path.read_text(encoding="utf-8", errors="replace"))
            path.write_text(out, encoding="utf-8")
            print(f"Minified {path.name} ({len(out)} bytes)")

if __name__ == "__main__":
    main()
