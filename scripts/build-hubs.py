"""Rebuild the four index hubs (services, industries, equipment, blog) as v2
card pages, from what the site actually contains.

Card copy is never invented: each card's title is the target page's own <h1>
(trimmed to its subject), its line comes from that page's own meta description
and its photo is that page's own hero image. Tones cycle through the v2
vocabulary; a card falls back to a line symbol only when the target page has no
image. The head, hero and chrome of the existing page are kept exactly as they
are.

Two things worth not re-breaking:
  * the blurb is split on sentence boundaries, and "U.S." is a sentence
    boundary to a naive splitter. Every industry description opens with
    "<Trade> business financing for U.S. contractors: ...", so splitting on
    /(?<=[.!?])\s/ produced the card line "Roofing business financing for U.S."
    on eighteen pages. Abbreviations are masked before the split.
  * cards are links, so the photo goes in a <div class="card-media"> exactly as
    the converter emits it on program pages - not a bare <img>, which the card
    grid does not size.
"""
import importlib.util, pathlib, re, sys
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

ABBR = ["U.S.", "U.K.", "e.g.", "i.e.", "Inc.", "Ltd.", "Co.", "Corp.", "vs.",
        "No.", "St.", "Mr.", "Ms.", "Dr.", "approx.", "est.", "Jr.", "Sr."]

def blurb(desc, floor=70, ceiling=175):
    """First sentence of the description, plus the next one if the first is a
    stub. Abbreviations are masked so they do not read as sentence ends."""
    text = " ".join((desc or "").split())
    if not text:
        return ""
    masked = text
    for a in ABBR:
        masked = masked.replace(a, a.replace(".", "\x00"))
    out = ""
    for part in re.split(r"(?<=[.!?])\s+", masked):
        nxt = (out + " " + part).strip() if out else part
        if out and len(nxt) > ceiling:
            break
        out = nxt
        if len(out) >= floor:
            break
    return out.replace("\x00", ".").strip()

def hero_media(rel):
    f = ROOT / rel
    if not f.exists():
        return ""
    o = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
    img = o.select_one(".hero-media img")
    if not (img and img.get("src")):
        img = next((i for i in o.select("main img")
                    if i.get("src") and "logo" not in i["src"].lower()), None)
    if not (img and img.get("src")):
        return ""
    return ('<div class="card-media"><img alt="" decoding="async" height="%s" '
            'loading="lazy" src="%s" width="%s"/></div>'
            % (img.get("height", "1071"), img["src"], img.get("width", "1920")))

def page_bits(rel, img_from=None):
    f = ROOT / rel
    if not f.exists():
        return None
    o = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
    h1 = o.select_one("h1")
    title = h1.get_text(" ", strip=True) if h1 else rel
    title = re.split(r"[:—–|]", title)[0].strip()
    d = o.find("meta", attrs={"name": "description"})
    line = blurb(d.get("content") if d else "")
    media = hero_media(rel)
    if not media and img_from:
        # an articles hub has no hero of its own; borrow the program page's.
        media = hero_media(img_from)
    return title, line, media

def cards(items, base_tone=0):
    out = []
    for n, item in enumerate(items):
        href, rel = item[0], item[1]
        bits = page_bits(rel, item[2] if len(item) > 2 else None)
        if not bits:
            continue
        title, line, media = bits
        lead = media or ('<span class="card-icon">%s</span>'
                         % conv.product_icon(title + " " + line[:80]))
        out.append(
            '      <a class="card" data-tone="%s" href="%s">\n'
            '        %s\n'
            '        <h3>%s</h3>\n        <p>%s</p>\n'
            '        <span class="card-cta">Read &rarr;</span>\n      </a>'
            % (conv.TILE_TONES[(n + base_tone) % 5], href, lead, title, line))
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
        cs = cards([("/%s/articles/" % name, "%s/articles/index.html" % name,
                     "%s.html" % name) for name, _ in hubs])
        cs += cards([("/articles/", "articles/index.html")], base_tone=len(cs))
        bands.append(band("Guides by program", cs))
    # WHERE THE BAND GOES. The sweep above only clears section.section, which
    # is the v2 shape. industries.html and services.html carry the pre-v2 one -
    # div.container > div.form-container > div.industries-grid > a.industry-tile,
    # inside no <section> at all - so nothing was cleared and the band landed
    # before the footer instead. Both pages shipped two competing grids of the
    # same links: 20 tiles above 18 cards, 15 above 16.
    #
    # Replace the legacy grid where it stands rather than appending after it.
    # Its wrapper is deliberately left alone - it also holds the intro copy and
    # the 'more guides' link list, which are real internal links.
    frag = BeautifulSoup("\n".join(bands), "html.parser")
    legacy = o.select_one(".industries-grid")
    if legacy is not None:
        for node in list(frag.contents):
            legacy.insert_before(node)
        legacy.decompose()
    else:
        anchor = o.find("footer") or o.body.find_all(recursive=False)[-1]
        for node in list(frag.contents):
            anchor.insert_before(node)
    f.write_text(str(o), encoding="utf-8")
    n = len(BeautifulSoup("\n".join(bands), "html.parser").select(".card"))
    print("%-18s rebuilt: %d bands, %d cards" % (target, len(bands), n))

for t in (sys.argv[1:] or ["services.html", "industries.html", "equipment.html", "blog.html"]):
    build(t)
