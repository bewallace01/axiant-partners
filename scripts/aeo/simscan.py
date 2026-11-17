# -*- coding: utf-8 -*-
"""Cannibalization check: how much of a page's body text is shared with any other page.

    python scripts/aeo/simscan.py --cluster sba_100_spokes          # render a cluster module in memory
    python scripts/aeo/simscan.py hotel-financing.html foo/bar/      # pages already on disk
    python scripts/aeo/simscan.py --cluster usda --titles "usda,b&i"  # also list pages whose <title> has these words

Shared % = the page's 6-word shingles that also appear on the other page, over the page's own
shingles. Body only: text from the <h1> to "Related Resources" (or the footer), so the shared
header, footer and get-matched block don't count. The daily batches keep every touched page at
or under ~16% against its closest sibling; over 25% means two pages answer the same thing.
"""
import argparse, glob, html, importlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
N = 6
SKIP = re.compile(r"[\\/](node_modules|_analysis|_components|\.git|\.next|scripts|docs)[\\/]")


def body_text(doc):
    m = re.search(r"<h1[\s>]", doc)
    s = doc[m.start():] if m else doc
    for stop in ('id="related-resources"', "<footer", 'id="article-sources-h2"'):
        i = s.find(stop)
        if i > 0:
            s = s[:i]
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).lower()
    return re.findall(r"[a-z0-9$%.]+", s)


def shingles(words):
    return {" ".join(words[i:i + N]) for i in range(max(0, len(words) - N + 1))}


def title_of(doc):
    m = re.search(r"<title>(.*?)</title>", doc, flags=re.S | re.I)
    return html.unescape(m.group(1).strip()) if m else ""


def url_of(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    return "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)


def site_pages():
    out = {}
    for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        if SKIP.search(p):
            continue
        try:
            doc = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        out[url_of(p)] = (title_of(doc), shingles(body_text(doc)))
    return out


def rendered(cluster):
    import article_v2 as A
    mod = importlib.import_module(f"cluster_{cluster}")
    v, header, footer = A.chrome()
    hub = mod.CLUSTER["hub"].strip("/")
    for a in mod.ARTICLES:
        doc = A.render(a, mod.CLUSTER, v, header, footer)
        url = "/" + a["root_file"] if a.get("root_file") else f"/{hub}/{a['slug']}/"
        yield url, title_of(doc), shingles(body_text(doc))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", nargs="*")
    ap.add_argument("--cluster", action="append", default=[])
    ap.add_argument("--titles", default="", help="comma-separated words; list site titles containing all of any one")
    ap.add_argument("--top", type=int, default=3)
    a = ap.parse_args()
    site = site_pages()
    targets = []
    for c in a.cluster:
        targets += list(rendered(c))
    for p in a.pages:
        u = "/" + p.strip("/").replace("\\", "/") + ("" if p.endswith(".html") else "/")
        if u not in site:
            print(f"!! not found: {u}")
            continue
        targets.append((u, site[u][0], site[u][1]))
    worst = 0.0
    for url, title, sh in targets:
        if not sh:
            print(f"{url}: no body text")
            continue
        scores = sorted(((len(sh & o) / len(sh), u) for u, (_, o) in site.items() if u != url and o),
                        reverse=True)[:a.top]
        top = scores[0][0] if scores else 0
        worst = max(worst, top)
        flag = "!!" if top > 0.25 else ("? " if top > 0.16 else "  ")
        print(f"{flag} {top:5.1%}  {url}   [{title}]")
        for s, u in scores:
            print(f"        {s:5.1%}  {u}")
    if a.titles:
        print("\nExisting titles matching:")
        for grp in a.titles.split(","):
            ws = grp.lower().split()
            for u, (t, _) in sorted(site.items()):
                if all(w in t.lower() for w in ws):
                    print(f"  [{grp}] {u}  -  {t}")
    return 1 if worst > 0.25 else 0


if __name__ == "__main__":
    sys.exit(main())
