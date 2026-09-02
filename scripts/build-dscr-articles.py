# -*- coding: utf-8 -*-
"""
Build the DSCR article cluster on the current v2 article shape.

WHY NOT article_engine.py, which the brief asked for: it cannot run. process()
opens equipment-financing/articles/medical-imaging-financing-radiology-practices/
index.html and string-replaces inside it, and that file was consolidated away --
_redirects line 72 now 301s it to patient-financing-imaging-centers. Even with
the template restored it emits the v1 blog-post-main layout, which only 12
pages on the site still use; every article built since the v2 rebuild uses the
shape below. So this is not a new template, it is the existing one: hero-compact
-> intro band -> article-grid (article-body + article-rail), modelled on
sba-loans/articles/how-long-sba-loan-approval/.

One thing is deliberately NOT copied from those articles. They declare
speakable cssSelector ".quick-answer" while the markup writes
<div class="callout" id="quick-answer"> -- so the selector matches no element
on any of them. These carry both the class and the id, so the schema resolves.

No hero <figure>: there is no DSCR image in assets/ and the brief says to record
the need rather than ship a broken img. See claude/images-needed.md.
"""
import os, re, sys, json, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://axiantpartners.com"
HUB = "dscr-loans/articles"
TODAY = datetime.date.today()


def version():
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r"axiant-v2\.css\?v=([0-9A-Za-z]+)", s)
    return m.group(1) if m else "1"


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def render(a, v, header, footer):
    url = f"{BASE}/{HUB}/{a['slug']}/"
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

    def strip(t):
        return " ".join(html.unescape(re.sub(r"<[^>]+>", "", t)).split())

    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "DSCR Loans", "item": f"{BASE}/dscr-loans.html"},
            {"@type": "ListItem", "position": 3, "name": "Articles", "item": f"{BASE}/{HUB}/"},
            {"@type": "ListItem", "position": 4, "name": a["crumb"], "item": url}]},
        {"@context": "https://schema.org", "@type": "Article",
         "headline": a["headline"], "description": a["article_desc"],
         "url": url, "datePublished": TODAY.isoformat(), "dateModified": TODAY.isoformat(),
         "author": {"@type": "Organization", "name": "Axiant Partners", "url": BASE},
         "publisher": {"@id": f"{BASE}/#organization"},
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "articleSection": "DSCR Loans", "keywords": a["keywords"]},
        {"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#webpage",
         "url": url, "name": a["title"],
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".quick-answer"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip(ans)}}
            for q, ans in a["faqs"]]},
        {"@context": "https://schema.org", "@type": "Organization",
         "@id": f"{BASE}/#organization", "name": "Axiant Partners", "url": BASE + "/",
         "logo": {"@type": "ImageObject", "url": f"{BASE}/logo-horizontal-transparent.png"},
         "telephone": "+1-561-268-0465",
         "address": {"@type": "PostalAddress", "addressLocality": "Boca Raton",
                     "addressRegion": "FL", "addressCountry": "US"},
         "areaServed": {"@type": "Country", "name": "United States"}},
    ]
    ld_html = "\n".join(
        '<script type="application/ld+json">%s</script>' % json.dumps(x, separators=(",", ":"))
        for x in ld)

    related = "\n".join(f'<li><a href="{h}">{html.escape(t)}</a></li>'
                        for h, t in a["related"])

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
<a class="crumb" href="../">&larr; Back to DSCR Loan Articles</a>
</div>
<p class="dateline">Updated {TODAY.strftime('%B %-d, %Y') if os.name != 'nt' else TODAY.strftime('%B %d, %Y').replace(' 0', ' ')}</p>
<div class="callout quick-answer" id="quick-answer">
<p class="eyebrow">Quick answer</p>
<div class="prose">
<p>{a['quick_answer']}</p>
<p><a href="/match.html">Get matched with DSCR lenders &rarr;</a></p>
</div>
</div>
<nav aria-label="Breadcrumb" class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/dscr-loans.html">DSCR Loans</a> &rsaquo; <a href="/{HUB}/">Articles</a> &rsaquo; <span aria-current="page">{html.escape(a['crumb'])}</span></nav>
{body}
<h2 id="faq">Frequently Asked Questions</h2>
<div class="faq">
{faq_html}
</div>
<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>
<ul>
{chr(10).join(f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{n}</a> &mdash; {d}</li>' for u, n, d in a["sources"])}
</ul>
<p>Figures above describe ranges commonly seen across DSCR lenders and reflect published guidance as of the date on this page. Confirm current terms with the cited source or your lender before acting.</p>
<p class="cta-actions cta-actions-left"><a class="btn btn-primary" href="/match.html">Get Matched for a DSCR Loan</a></p>
</div>
<aside class="article-rail">
<div class="rail-actions">
<a class="btn btn-quiet" href="#quick-answer">Quick answer</a>
<a class="btn btn-primary" href="/match.html">Get Matched for a DSCR Loan</a>
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


def main(apply_changes, only=None):
    from dscr_articles_batch1 import ARTICLES
    v = version()
    header = open(os.path.join(ROOT, "_components", "header-v2.html"),
                  encoding="utf-8").read().strip().replace("{{VERSION}}", v)
    footer = open(os.path.join(ROOT, "_components", "footer-v2.html"),
                  encoding="utf-8").read().strip()
    print("APPLIED" if apply_changes else "DRY RUN")
    for a in ARTICLES:
        if only and a["slug"] not in only:
            continue
        out = render(a, v, header, footer)
        words = len(re.sub(r"<[^>]+>", " ",
                    re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", out,
                           flags=re.S | re.I)).split())
        d = os.path.join(ROOT, HUB.replace("/", os.sep), a["slug"])
        if apply_changes:
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w",
                      encoding="utf-8", newline="") as fh:
                fh.write(out)
        print(f"  {a['slug']:44} {words:5} words  {len(a['faqs'])} faqs  "
              f"{len(a['sections'])} sections  {len(out)} bytes")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main("--apply" in sys.argv))
