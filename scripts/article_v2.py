# -*- coding: utf-8 -*-
"""
Shared renderer for v2 article clusters.

Generalised out of build-dscr-articles.py once the DSCR cluster shipped, so the
remaining clusters in the build-out plan reuse one renderer rather than each
growing its own copy. The DSCR builder is the reference implementation and this
emits byte-identical structure.

WHY NOT article_engine.py: it cannot run. process() opens
equipment-financing/articles/medical-imaging-financing-radiology-practices/ and
string-replaces inside it, and that file was consolidated away - _redirects now
301s it. It also emits the v1 blog-post-main layout, which only 12 pages still
use. This emits the shape every article built since the v2 rebuild uses:
hero-compact, intro band, article-grid with article-body and article-rail,
modelled on sba-loans/articles/how-long-sba-loan-approval/.

One deliberate difference from those articles: they declare speakable
cssSelector ".quick-answer" while writing class="callout" id="quick-answer", so
the selector matches nothing on any of them. Articles from here carry both.
"""
import datetime, html, io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://axiantpartners.com"
TODAY = datetime.date.today()
TONES = ["blue", "teal", "indigo", "bronze", "rust"]


def version():
    s = io.open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r"axiant-v2\.css\?v=([0-9A-Za-z]+)", s)
    return m.group(1) if m else "1"


def chrome():
    v = version()
    head = io.open(os.path.join(ROOT, "_components", "header-v2.html"),
                   encoding="utf-8").read().strip().replace("{{VERSION}}", v)
    foot = io.open(os.path.join(ROOT, "_components", "footer-v2.html"),
                   encoding="utf-8").read().strip()
    return v, head, foot


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def _plain(t):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", t)).split())


def _dateline():
    d = TODAY.strftime("%B %d, %Y")
    return d.replace(" 0", " ", 1) if " 0" in d[:8] else d


def render(a, c, v, header, footer):
    """a = article dict, c = cluster dict."""
    hub = c["hub"]
    url = f"{BASE}/{hub}/{a['slug']}/"
    heads = [h for h, _ in a["sections"]]
    toc = "\n".join(f'<li><a href="#{slugify(h)}">{html.escape(h)}</a></li>'
                    for h in heads) + \
        '\n<li><a href="#faq">Frequently Asked Questions</a></li>'
    body = "\n".join(f'<h2 id="{slugify(h)}">{html.escape(h)}</h2>\n{md}'
                     for h, md in a["sections"])
    faq_html = "\n".join(
        f"<details>\n<summary>{html.escape(q)}</summary>\n"
        f'<div class="answer"><p>{ans}</p></div>\n</details>'
        for q, ans in a["faqs"])

    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": c["crumb"],
             "item": f"{BASE}/{c['pillar']}"},
            {"@type": "ListItem", "position": 3, "name": "Articles", "item": f"{BASE}/{hub}/"},
            {"@type": "ListItem", "position": 4, "name": a["crumb"], "item": url}]},
        {"@context": "https://schema.org", "@type": "Article",
         "headline": a["headline"], "description": a["article_desc"], "url": url,
         "datePublished": TODAY.isoformat(), "dateModified": TODAY.isoformat(),
         "author": {"@type": "Organization", "name": "Axiant Partners", "url": BASE},
         "publisher": {"@id": f"{BASE}/#organization"},
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "articleSection": c["crumb"], "keywords": a["keywords"]},
        {"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#webpage",
         "url": url, "name": a["title"],
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".quick-answer"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": _plain(ans)}}
            for q, ans in a["faqs"]]},
        {"@context": "https://schema.org", "@type": "Organization",
         "@id": f"{BASE}/#organization", "name": "Axiant Partners", "url": BASE + "/",
         "logo": {"@type": "ImageObject",
                  "url": f"{BASE}/logo-horizontal-transparent.png"},
         "telephone": "+1-561-268-0465",
         "address": {"@type": "PostalAddress", "addressLocality": "Boca Raton",
                     "addressRegion": "FL", "addressCountry": "US"},
         "areaServed": {"@type": "Country", "name": "United States"}},
    ]
    ld_html = "\n".join('<script type="application/ld+json">%s</script>'
                        % json.dumps(x, separators=(",", ":")) for x in ld)
    related = "\n".join(f'<li><a href="{h}">{html.escape(t)}</a></li>'
                        for h, t in a["related"])
    sources = "\n".join(
        f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{n}</a> &mdash; {d}</li>'
        for u, n, d in a["sources"])

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
<meta content="{html.escape(a['meta_desc'])}" name="description"/>
<meta content="index, follow, max-snippet:-1, max-image-preview:large" name="robots"/>
<link href="{url}" rel="canonical"/>
<meta content="en_US" property="og:locale"/>
<meta content="{html.escape(a['og_title'])}" property="og:title"/>
<meta content="{html.escape(a['meta_desc'])}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="{url}" property="og:url"/>
<meta content="Axiant Partners" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(a['og_title'])}" name="twitter:title"/>
<meta content="{html.escape(a['meta_desc'])}" name="twitter:description"/>
<title>{html.escape(a['title'])}</title>
{ld_html}
<link rel="preload" href="/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/playfair-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/axiant-v2.css?v={v}">
</head>
<body>
{header}

<section class="hero-compact">
<div class="container">
<div class="inner">
<p class="eyebrow">Guide</p>
<h1>{a['h1']}</h1>
<p class="lede">{a['lede']}</p>
</div>
</div>
</section>
<section class="section section-alt section-tight">
<div class="container article-container">
<div class="article-grid">
<div class="article-body">
<div class="crumb-row">
<a class="crumb" href="../">&larr; Back to {html.escape(c['crumb'])} Articles</a>
</div>
<p class="dateline">Updated {_dateline()}</p>
<div class="callout quick-answer" id="quick-answer">
<p class="eyebrow">Quick answer</p>
<div class="prose">
<p>{a['quick_answer']}</p>
<p><a href="/match.html">{html.escape(c['cta_inline'])} &rarr;</a></p>
</div>
</div>
<nav aria-label="Breadcrumb" class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/{c['pillar']}">{html.escape(c['crumb'])}</a> &rsaquo; <a href="/{hub}/">Articles</a> &rsaquo; <span aria-current="page">{html.escape(a['crumb'])}</span></nav>
{body}
<h2 id="faq">Frequently Asked Questions</h2>
<div class="faq">
{faq_html}
</div>
<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>
<ul>
{sources}
</ul>
<p>Figures above describe ranges commonly seen across lenders and reflect published guidance as of the date on this page. Confirm current terms with the cited source or your lender before acting.</p>
<p class="cta-actions cta-actions-left"><a class="btn btn-primary" href="/match.html">{html.escape(c['cta_button'])}</a></p>
</div>
<aside class="article-rail">
<div class="rail-actions">
<a class="btn btn-quiet" href="#quick-answer">Quick answer</a>
<a class="btn btn-primary" href="/match.html">{html.escape(c['cta_button'])}</a>
</div>
<nav aria-label="On this page" class="toc">
<h3>On this page</h3>
<ul>
{toc}
</ul>
</nav>
</aside>
</div>
</div>
</section>
<section class="section">
<div class="container">
<div class="group" data-tone="blue">
<div class="group-head"><h2 id="related-resources">Related Resources</h2></div>
<div class="prose">
<ul>
{related}
</ul>
</div>
<p class="cta-actions cta-actions-left"><a class="btn btn-primary" href="/match.html">Find My Match</a></p>
</div>
</div>
</section>

{footer}
<script src="/script.js?v={v}" defer></script>
</body>
</html>
"""


def _meta_of(path):
    s = io.open(path, encoding="utf-8", errors="replace").read()
    head = s[:s.find("</head>")] if "</head>" in s else s
    t = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
    title = re.split(r"\s*\|\s*", html.unescape(t.group(1)).strip())[0] if t else ""
    d = ""
    for tag in re.findall(r"<meta[^>]*>", head, re.I):
        if re.search(r'name=["\']description["\']', tag, re.I):
            m = re.search(r'content=["\']([^"\']*)', tag, re.I)
            if m:
                d = html.unescape(m.group(1)).strip()
            break
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S | re.I)
    return (_plain(h1.group(1)) if h1 else title), d


def build_hub(c, v, header, footer):
    """Hub generated from disk so its cards cannot drift from the articles."""
    import glob
    hub = c["hub"]
    arts = []
    for p in sorted(glob.glob(os.path.join(ROOT, hub.replace("/", os.sep), "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(p))
        name, desc = _meta_of(p)
        arts.append((slug, name, desc))
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                  {"@type": "ListItem", "position": 2, "name": c["crumb"],
                   "item": f"{BASE}/{c['pillar']}"},
                  {"@type": "ListItem", "position": 3, "name": "Articles",
                   "item": f"{BASE}/{hub}/"}]}
    coll = {"@context": "https://schema.org", "@type": "CollectionPage",
            "name": c["hub_h1"], "description": c["hub_desc"], "url": f"{BASE}/{hub}/",
            "isPartOf": {"@id": f"{BASE}/#organization"},
            "hasPart": [{"@type": "Article", "headline": n, "url": f"{BASE}/{hub}/{s}/"}
                        for s, n, _ in arts]}
    cards = "\n".join(
        f'<a class="card" data-tone="{TONES[i % len(TONES)]}" href="{slug}/">\n'
        f'<h3>{html.escape(name)}</h3>\n<p>{html.escape(desc)}</p>\n'
        f'<span class="card-cta">Read more</span>\n</a>'
        for i, (slug, name, desc) in enumerate(arts))

    return len(arts), f"""<!DOCTYPE html>
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
<meta content="{html.escape(c['hub_desc'])}" name="description"/>
<meta content="index, follow, max-snippet:-1, max-image-preview:large" name="robots"/>
<link href="{BASE}/{hub}/" rel="canonical"/>
<meta content="{html.escape(c['hub_title'])}" property="og:title"/>
<meta content="{html.escape(c['hub_desc'])}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{BASE}/{hub}/" property="og:url"/>
<meta content="Axiant Partners" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{html.escape(c['hub_h1'])} | Axiant" name="twitter:title"/>
<meta content="{html.escape(c['hub_desc'])}" name="twitter:description"/>
<title>{html.escape(c['hub_title'])}</title>
<script type="application/ld+json">{json.dumps(crumbs, separators=(",", ":"))}</script>
<script type="application/ld+json">{json.dumps(coll, separators=(",", ":"))}</script>
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
<h1>{html.escape(c['hub_h1'])}</h1>
<p class="lede">{html.escape(c['hub_lede'])}</p>
</div>
</div>
</section>
<section class="section section-alt section-tight">
<div class="container">
<div class="group" data-tone="blue">
<div class="prose">
<p class="hub-back"><a href="/blog.html">&larr; All Articles</a></p>
<p class="lead">{c['hub_intro']}</p>
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
<h2 id="ready">{html.escape(c['hub_cta_h2'])}</h2>
<p>{c['hub_cta_p']}</p>
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
