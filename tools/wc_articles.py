import pathlib, re
root = pathlib.Path(__file__).resolve().parents[1] / "business-growth" / "articles"
rows = []
for p in sorted(root.glob("*/index.html")):
    t = p.read_text(encoding="utf-8")
    m = re.search(r'form-container blog-post-content">\s*(.*?)\s*<p style="margin-top:2rem;">', t, re.S)
    if not m:
        m = re.search(r"blog-post-content\">(.*)</div></body>", t, re.S)
    text = re.sub(r"<[^>]+>", " ", m.group(1) if m else t)
    words = len([w for w in re.split(r"\s+", text) if re.search(r"[A-Za-z0-9]", w)])
    rows.append((words, p.parent.name))
for w, name in rows:
    print(w, name)
print("min", min(r[0] for r in rows), "max", max(r[0] for r in rows), "avg", sum(r[0] for r in rows) / len(rows))
