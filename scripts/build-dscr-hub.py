# -*- coding: utf-8 -*-
"""
Build dscr-loans/articles/index.html from whatever is on disk.

Generated rather than hand-written because the cluster is being built out over
several batches -- a hand-maintained card list is the same failure mode that
left generate_sitemap.py 188 URLs behind the site. Each card's title and blurb
come from the article's own <title> and meta description, so the hub cannot
drift from the articles it indexes.

Structure follows fix-and-flip/articles/index.html: hero-compact, an intro
band, then one .card per article inside .cards.cards-left, with the tone
cycling through the v2 palette. blog.html discovers */articles/index.html by
glob, so this appears there on the next scripts/build-hubs.py run.
"""
import os, re, sys, glob, html, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://axiantpartners.com"
HUB = "dscr-loans/articles"
TONES = ["blue", "teal", "indigo", "bronze", "rust"]

TITLE = "DSCR Loan Articles: Ratios, Rent, Requirements | Axiant"
H1 = "DSCR Loan Articles"
LEDE = ("Guides to qualifying on the property's cash flow — how the ratio is "
        "calculated, what rent counts, and what lenders require")
DESC = ("DSCR loan guides: how the ratio is calculated, what rental income "
        "underwriters count, minimum ratios by lender type, and what gets a "
        "file denied.")


def version():
    """Reuse whatever ?v= the rest of the site is on, so caches stay in step."""
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r"axiant-v2\.css\?v=([0-9A-Za-z]+)", s)
    return m.group(1) if m else "1"


def meta_of(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    head = s[:s.find("</head>")] if "</head>" in s else s
    t = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
    title = html.unescape(t.group(1)).strip() if t else ""
    # the tail after the last pipe is the brand, not the article's name
    title = re.split(r"\s*\|\s*", title)[0].strip()
    d = ""
    for tag in re.findall(r"<meta[^>]*>", head, re.I):
        if re.search(r'name=["\']description["\']', tag, re.I):
            m = re.search(r'content=["\']([^"\']*)', tag, re.I)
            if m:
                d = html.unescape(m.group(1)).strip()
            break
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S | re.I)
    h1 = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else title
    return (h1 or title), d


def articles():
    out = []
    for p in sorted(glob.glob(os.path.join(ROOT, HUB.replace("/", os.sep), "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(p))
        name, desc = meta_of(p)
        out.append((slug, name, desc))
    return out


def build():
    v = version()
    header = open(os.path.join(ROOT, "_components", "header-v2.html"),
                  encoding="utf-8").read().strip().replace("{{VERSION}}", v)
    footer = open(os.path.join(ROOT, "_components", "footer-v2.html"),
                  encoding="utf-8").read().strip()
    arts = articles()

    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                  {"@type": "ListItem", "position": 2, "name": "DSCR Loans",
                   "item": f"{BASE}/dscr-loans.html"},
                  {"@type": "ListItem", "position": 3, "name": "Articles",
                   "item": f"{BASE}/{HUB}/"}]}
    collection = {"@context": "https://schema.org", "@type": "CollectionPage",
                  "name": H1, "description": DESC, "url": f"{BASE}/{HUB}/",
                  "isPartOf": {"@id": f"{BASE}/#organization"},
                  "hasPart": [{"@type": "Article", "headline": n,
                               "url": f"{BASE}/{HUB}/{s}/"} for s, n, _ in arts]}

    cards = "\n".join(
        f'<a class="card" data-tone="{TONES[i % len(TONES)]}" href="{slug}/">\n'
        f'<h3>{html.escape(name)}</h3>\n'
        f'<p>{html.escape(desc)}</p>\n'
        f'<span class="card-cta">Read more</span>\n</a>'
        for i, (slug, name, desc) in enumerate(arts))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<link href="https://www.googletagmanager.com" rel="dns-prefetch"/>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta content="#0d1f3c" name="theme-color"/>
<script async="" src="https://www.googletagmanager.com/gtag/js?id=G-HZNSHH6NN0"></script>
<script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-HZNSHH6NN0');
      gtag('config', 'AW-18021105450');
    </script>
<meta content="{html.escape(DESC)}" name="description"/>
<meta content="index, follow, max-snippet:-1, max-image-preview:large" name="robots"/>
<link href="{BASE}/{HUB}/" rel="canonical"/>
<meta content="{html.escape(TITLE)}" property="og:title"/>
<meta content="{html.escape(DESC)}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{BASE}/{HUB}/" property="og:url"/>
<meta content="{BASE}/assets/cre-intro.webp" property="og:image"/>
<meta content="1200" property="og:image:width"/>
<meta content="630" property="og:image:height"/>
<meta content="Axiant Partners" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(H1)} | Axiant" name="twitter:title"/>
<meta content="{html.escape(DESC)}" name="twitter:description"/>
<title>{html.escape(TITLE)}</title>
<script type="application/ld+json">{json.dumps(crumbs, separators=(",", ":"))}</script>
<script type="application/ld+json">{json.dumps(collection, separators=(",", ":"))}</script>
<link rel="preload" href="/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/playfair-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/axiant-v2.css?v={v}">
</head>
<body>
{header}

<section class="hero-compact">
<div class="container">
<div class="inner">
<p class="eyebrow">Guides</p>
<h1>{html.escape(H1)}</h1>
<p class="lede">{html.escape(LEDE)}</p>
</div>
</div>
</section>
<section class="section section-alt section-tight">
<div class="container">
<div class="group" data-tone="blue">
<div class="prose">
<p class="hub-back"><a href="/blog.html">&larr; All Articles</a></p>
<p class="lead">A DSCR loan qualifies on the property's rent rather than your personal income, so the ratio does the work your tax returns would normally do. These guides cover how that ratio is calculated, which rental income underwriters actually count, and what separates an approval from a decline. Start with <a href="/dscr-loans.html">DSCR loans</a>, or check <a href="/dscr-loan-requirements.html">the requirements</a> and <a href="/dscr-loan-rates.html">how pricing is built</a> before you apply.</p>
</div>
</div>
</div>
</section>
<section class="section">
<div class="container">
<div class="group" data-tone="blue">
<div class="cards cards-left">
{cards}
</div>
</div>
</div>
</section>
<section class="section section-alt">
<div class="container">
<div class="group" data-tone="blue">
<div class="prose">
<h2 id="ready">Ready to see what the property qualifies for?</h2>
<p>Send the address, the rent and the purchase price. We place DSCR loans nationwide and will tell you plainly whether the ratio works.</p>
<p class="cta-actions cta-actions-left"><a class="btn btn-primary" href="/match.html">Find My Match</a></p>
</div>
</div>
</div>
</section>

{footer}
<script src="/script.js?v={v}" defer></script>
</body>
</html>
"""


def main(apply_changes):
    out = build()
    n = len(articles())
    path = os.path.join(ROOT, HUB.replace("/", os.sep), "index.html")
    print("APPLIED" if apply_changes else "DRY RUN")
    print(f"  articles indexed: {n}")
    print(f"  bytes: {len(out)}")
    if apply_changes:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(out)
        print(f"  wrote {HUB}/index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
