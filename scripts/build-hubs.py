"""Rebuild the four index hubs (services, industries, equipment, blog) as v2
card pages, from what the site actually contains.

Card copy is never invented: each card's title is the target page's own <h1>
(trimmed to its subject) and its line is the first sentence of that page's own
meta description. Tones and symbols cycle through the v2 vocabulary. The head,
hero and chrome of the existing page are kept exactly as they are.
"""
import importlib.util, pathlib, re, sys
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

def page_bits(rel):
    f = ROOT / rel
    if not f.exists():
        return None
    o = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
    h1 = o.select_one("h1")
    title = h1.get_text(" ", strip=True) if h1 else rel
    title = re.split(r"[:—–|]", title)[0].strip()
    d = o.find("meta", attrs={"name": "description"})
    line = (d.get("content") or "").strip() if d else ""
    line = re.split(r"(?<=[.!?])\s", line)[0].strip() if line else ""
    return title, line

def cards(items, base_tone=0):
    out = []
    for n, (href, rel) in enumerate(items):
        bits = page_bits(rel)
        if not bits:
            continue
        title, line = bits
        out.append(
            '      <a class="card" data-tone="%s" href="%s">\n'
            '        <span class="card-icon">%s</span>\n'
            '        <h3>%s</h3>\n        <p>%s</p>\n'
            '        <span class="card-cta">Read &rarr;</span>\n      </a>'
            % (conv.TILE_TONES[(n + base_tone) % 5], href,
               conv.product_icon(title + " " + line[:80]), title, line))
    return out

def band(heading, cs, alt=False, tone="blue"):
    return ('<section class="section%s">\n  <div class="container">\n'
            '    <div class="group" data-tone="%s">\n'
            '      <div class="group-head"><h2>%s</h2></div>\n'
            '      <div class="cards cards-left">\n%s\n      </div>\n'
            '    </div>\n  </div>\n</section>'
            % (" section-alt" if alt else "", tone, heading, "\n".join(cs)))

GROUPS = {
    "services.html": [
        ("Working capital and growth", ["working-capital-loans", "business-line-of-credit",
                                        "business-term-loans", "revenue-based-financing",
                                        "merchant-cash-advance", "inventory-financing"]),
        ("Equipment and vehicles", ["equipment-financing", "contractor-financing"]),
        ("Property and real estate", ["commercial-real-estate-loans", "commercial-bridge-loans",
                                      "fix-and-flip"]),
        ("Cash flow and assets", ["invoice-factoring", "securities-based-lending"]),
        ("Starting out and getting clear of debt", ["startup-financing", "sba-loans",
                                                    "business-debt-relief"]),
    ],
}

def build(target):
    f = ROOT / target
    o = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
    for sec in o.select("section.section"):
        sec.decompose()
    bands = []
    if target == "services.html":
        for i, (heading, slugs) in enumerate(GROUPS[target]):
            cs = cards([("/%s.html" % s, "%s.html" % s) for s in slugs], base_tone=i)
            if cs:
                bands.append(band(heading, cs, alt=(i % 2 == 1)))
    elif target == "industries.html":
        cs = cards([("/%s.html" % s, "%s.html" % s) for s in conv.INDUSTRIES])
        bands.append(band("Financing by industry", cs))
    elif target == "equipment.html":
        cs = cards([("/equipment/%s/" % e, "equipment/%s/index.html" % e) for e in conv.EQUIPMENT])
        bands.append(band("Equipment financing guides", cs))
    elif target == "blog.html":
        hubs = [(str(p.parent.parent.name), p) for p in sorted(ROOT.glob("*/articles/index.html"))]
        cs = cards([("/%s/articles/" % name, "%s/articles/index.html" % name) for name, _ in hubs])
        cs += cards([("/articles/", "articles/index.html")], base_tone=len(cs))
        bands.append(band("Guides by program", cs))
    anchor = o.find("footer") or o.body.find_all(recursive=False)[-1]
    frag = BeautifulSoup("\n".join(bands), "html.parser")
    for node in list(frag.contents):
        anchor.insert_before(node)
    f.write_text(str(o), encoding="utf-8")
    n = len(BeautifulSoup("\n".join(bands), "html.parser").select(".card"))
    print("%-18s rebuilt: %d bands, %d cards" % (target, len(bands), n))

for t in (sys.argv[1:] or ["services.html", "industries.html", "equipment.html", "blog.html"]):
    build(t)
