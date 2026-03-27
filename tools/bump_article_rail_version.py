import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = "2026040801"
pat = re.compile(r"/article-rail\.css\?v=\d+")

def main() -> None:
    n = 0
    for p in ROOT.rglob("*.html"):
        if "node_modules" in p.parts:
            continue
        t = p.read_text(encoding="utf-8")
        u = pat.sub(f"/article-rail.css?v={VER}", t)
        if u != t:
            p.write_text(u, encoding="utf-8")
            n += 1
    print(f"Updated {n} HTML files to article-rail.css?v={VER}")


if __name__ == "__main__":
    main()
