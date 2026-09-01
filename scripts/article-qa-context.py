"""Compact context for drafting a quick answer: the article's question, its
section headings, and its own sentences that carry figures or verdicts."""
import importlib.util, pathlib, re, sys
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

FACT = re.compile(r'(\$\s?[\d,]+|\d+\s?%|\b\d+\s?(?:-|–|to)\s?\d+\b|\b\d+\s?(?:days?|weeks?|months?|years?|hours?)\b)')
VERDICT = re.compile(r'^(yes|no|short answer|it depends|most |typically|generally|usually|you can|you cannot)\b', re.I)

def pending():
    out = []
    for rel in conv.article_pages():
        o = BeautifulSoup((ROOT / rel).read_text(encoding="utf-8"), "html.parser")
        if not o.select_one(".callout"):
            out.append(rel)
    return out

if __name__ == "__main__":
    start = int(sys.argv[1]); count = int(sys.argv[2])
    rels = pending()[start:start + count]
    for rel in rels:
        o = BeautifulSoup((ROOT / rel).read_text(encoding="utf-8"), "html.parser")
        h1 = o.select_one("h1")
        lede = o.select_one(".article-body p.lede-para")
        sents, seen = [], set()
        for p in o.select(".article-body p, .article-body li")[:60]:
            for sn in re.split(r'(?<=[.!?])\s+', " ".join(p.get_text(" ").split())):
                if len(sn.split()) < 6 or len(sn.split()) > 34:
                    continue
                if (FACT.search(sn) or VERDICT.match(sn)) and sn[:40] not in seen:
                    seen.add(sn[:40]); sents.append(sn)
        heads = [h.get_text(" ", strip=True) for h in o.select(".article-body h2")][:6]
        print("### %s" % rel)
        print("Q: %s" % (h1.get_text(" ", strip=True) if h1 else ""))
        if lede:
            print("LEDE: %s" % " ".join(lede.get_text(" ").split())[:190])
        print("HEADS: %s" % " | ".join(heads))
        for sn in sents[:6]:
            print("  - %s" % sn[:165])
        print()
