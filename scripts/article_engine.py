"""Shared engine for batch article builds. Import from this."""
import datetime, pathlib, re
REPO = pathlib.Path(__file__).resolve().parent.parent

# Default for datePublished / dateModified when a caller supplies neither.
_TODAY = datetime.date.today().isoformat()

TEMPLATE_CANONICAL = "https://axiantpartners.com/equipment-financing/articles/medical-imaging-financing-radiology-practices/"
TEMPLATE_TITLE_TAG = "Medical Imaging Financing for Radiology Practices ($50K–$2M) | Axiant"
TEMPLATE_OG_TITLE = "Medical Imaging Financing for Radiology Practices ($50K–$2M)"
TEMPLATE_OG_DESC = "Radiology practices finance MRI, CT, X-ray, and ultrasound from $50K–$2M+ via equipment loans, operating leases, or SBA 504. 24–48 hr approvals at 600+ FICO."
TEMPLATE_META_DESC = "Medical imaging financing for radiology practices: MRI, CT, X-ray, ultrasound from $50K–$2M+ via equipment loans, leases, or SBA 504. 24–48 hr approvals at 600+ FICO, 0–20% down."
TEMPLATE_TWITTER_DESC = "MRI, CT, X-ray, ultrasound financing for radiology practices: $50K–$2M+, 24–48 hr approvals, 600+ FICO, 0–20% down."
TEMPLATE_IMAGE_URL = "https://axiantpartners.com/assets/medical-imaging-equipment.webp"
TEMPLATE_H1 = "Medical Imaging Financing for Radiology Practices: MRI, CT, X-Ray, Ultrasound"
TEMPLATE_TAGLINE = "How radiology practices and imaging centers finance $50K&ndash;$2M+ equipment &mdash; loans, leases, SBA 504, and the patient-financing piece practices add on top"


def make_breadcrumb_schema(a):
    return ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":'
        '[{"@type":"ListItem","position":1,"name":"Home","item":"https://axiantpartners.com/"},'
        f'{{"@type":"ListItem","position":2,"name":"{a["breadcrumb_cluster"]}","item":"{a["breadcrumb_cluster_url"]}"}},'
        f'{{"@type":"ListItem","position":3,"name":"Articles","item":"{a["breadcrumb_articles_url"]}"}},'
        f'{{"@type":"ListItem","position":4,"name":"{a["breadcrumb_article_name"]}","item":"{a["canonical"]}"}}]}}')

def make_article_schema(a):
    # Both dates were hardcoded to "2026-05-27", so every article the engine has
    # ever emitted claims to have been published and last modified on the same
    # day in May regardless of when it was written. Left alone, a fourteen-article
    # cluster built in September would ship fourteen pages backdated four months --
    # and dateModified is the field the sitemap's lastmod is now derived from, so a
    # wrong date here propagates straight into the sitemap.
    #
    # Callers may pass either key; both fall back to today, which is the right
    # answer for a page being generated now.
    published = a.get("date_published") or _TODAY
    modified = a.get("date_modified") or published
    return ('{"@context":"https://schema.org","@type":"Article",'
        f'"headline":"{a["article_headline"]}","description":"{a["article_desc"]}",'
        f'"image":{{"@type":"ImageObject","url":"{a["image_url"]}","width":1200,"height":630}},'
        f'"url":"{a["canonical"]}","datePublished":"{published}","dateModified":"{modified}",'
        '"author":{"@type":"Organization","name":"Axiant Partners","url":"https://axiantpartners.com"},'
        '"publisher":{"@id":"https://axiantpartners.com/#organization"},'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{a["canonical"]}"}},'
        f'"articleSection":"{a["section"]}","keywords":"{a["keywords"]}"}}')

def make_faq_schema(a):
    items = ['{"@type":"Question","name":"' + q.replace('"','\\"') + '","acceptedAnswer":{"@type":"Answer","text":"' + ans.replace('"','\\"') + '"}}' for q, ans in a["faqs"]]
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(items) + "]}"

def make_webpage_schema(a):
    return ('{"@context":"https://schema.org","@type":"WebPage",'
        f'"@id":"{a["canonical"]}#webpage","url":"{a["canonical"]}","name":"{a["speakable_name"]}",'
        '"speakable":{"@type":"SpeakableSpecification","cssSelector":[".quick-answer"]}}')

def make_howto_schema(a):
    steps = ['{"@type":"HowToStep","position":' + str(i) + ',"name":"' + n.replace('"','\\"') + '","text":"' + t.replace('"','\\"') + '"}' for i, (n, t) in enumerate(a["howto_steps"], 1)]
    return ('{"@context":"https://schema.org","@type":"HowTo",'
        f'"name":"{a["howto_name"]}","description":"{a["howto_desc"]}",'
        '"totalTime":"P3D","step":[' + ",".join(steps) + "]}")


def process(a):
    p = REPO / a["file"]
    html = p.read_text(encoding="utf-8")
    html = html.replace(f'<meta name="description" content="{TEMPLATE_META_DESC}">', f'<meta name="description" content="{a["meta_desc"]}">')
    html = html.replace(f'<link rel="canonical" href="{TEMPLATE_CANONICAL}">', f'<link rel="canonical" href="{a["canonical"]}">')
    html = html.replace(f'<meta property="og:title" content="{TEMPLATE_OG_TITLE}">', f'<meta property="og:title" content="{a["og_title"]}">')
    html = html.replace(f'<meta property="og:description" content="{TEMPLATE_OG_DESC}">', f'<meta property="og:description" content="{a["og_desc"]}">')
    html = html.replace(f'<meta property="og:url" content="{TEMPLATE_CANONICAL}">', f'<meta property="og:url" content="{a["canonical"]}">')
    html = html.replace(f'<meta property="og:image" content="{TEMPLATE_IMAGE_URL}">', f'<meta property="og:image" content="{a["image_url"]}">')
    html = html.replace('<meta property="article:section" content="Equipment Financing">', f'<meta property="article:section" content="{a["section"]}">')
    html = html.replace(f'<meta name="twitter:title" content="{TEMPLATE_OG_TITLE}">', f'<meta name="twitter:title" content="{a["og_title"]}">')
    html = html.replace(f'<meta name="twitter:description" content="{TEMPLATE_TWITTER_DESC}">', f'<meta name="twitter:description" content="{a["twitter_desc"]}">')
    html = html.replace(f'<title>{TEMPLATE_TITLE_TAG}</title>', f'<title>{a["title_tag"]}</title>')
    schemas = [make_breadcrumb_schema(a), make_article_schema(a), make_faq_schema(a), make_webpage_schema(a), make_howto_schema(a)]
    pat = re.compile(r'(<script type="application/ld\+json">\s*)([^<]*?)(\s*</script>)', re.DOTALL)
    matches = list(pat.finditer(html))
    if len(matches) >= 5:
        for i in range(min(5, len(matches)) - 1, -1, -1):
            m = matches[i]
            html = html[:m.start()] + m.group(1) + schemas[i] + m.group(3) + html[m.end():]
    html = html.replace(f'<h1>{TEMPLATE_H1}</h1>', f'<h1>{a["h1"]}</h1>')
    html = html.replace(f'<p class="tagline">{TEMPLATE_TAGLINE}</p>', f'<p class="tagline">{a["tagline"]}</p>')
    html = html.replace('<p class="blog-rail-back"><a href="../">&larr; Back to Equipment Financing Articles</a></p>', f'<p class="blog-rail-back"><a href="{a["rail_back_href"]}">&larr; {a["rail_back_text"]}</a></p>')
    html = html.replace('<div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick Facts</h3><p>$50K&ndash;$2M+ equipment range. 6&ndash;15% rates, 36&ndash;84 month terms. 0&ndash;20% down at 600+ FICO. 24&ndash;48 hr approvals from healthcare-specialty lenders. SBA 504 available on $500K+ deals.</p></div></div>', f'<div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick Facts</h3><p>{a["rail_facts"]}</p></div></div>')
    html = html.replace('<h3>Need imaging equipment funded?</h3>\n          <p>Get matched with healthcare-equipment lenders for your MRI, CT, X-ray, or ultrasound.</p>\n          <a href="/match.html" class="btn-primary">Get Matched for Imaging Financing</a>', f'<h3>{a["rail_cta_h3"]}</h3>\n          <p>{a["rail_cta_p"]}</p>\n          <a href="/match.html" class="btn-primary">{a["rail_cta_btn"]}</a>')
    related_items = "\n                    ".join(f'<li><a href="{href}">{text}</a></li>' for href, text in a["related_links"])
    new_main = ('<main class="blog-post-main">\n'
        '<div class="quick-answer" style="background:var(--bg-card);border-left:4px solid var(--accent-color);padding:16px 18px;margin:0 0 28px;border-radius:10px;">\n'
        '  <strong style="display:block;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent-color);margin-bottom:6px;">Quick answer</strong>\n'
        f'  <p style="margin:0;font-size:1rem;line-height:1.55;color:var(--text-primary);">{a["quick_answer_html"]}</p>\n'
        '  <p style="margin:12px 0 0;font-size:0.92rem;color:var(--text-secondary);"><a href="/match.html" style="color:var(--accent-color);font-weight:600;">Get matched &rarr;</a></p>\n'
        '</div>\n'
        f'            {a["intro_html"]}\n\n'
        f'            {a["body_sections_html"]}\n\n'
        '<section class="related-resources" aria-label="Related resources">\n'
        '                <h2>Related Resources</h2>\n                <ul>\n'
        f'                    {related_items}\n                </ul>\n'
        '<div class="services-cta">\n'
        f'                <a href="/match.html" class="btn-primary">{a["related_cta_text"]}</a>\n'
        '            </div>\n</section>\n</main>')
    html = re.sub(r'<main class="blog-post-main">.*?</main>', new_main, html, count=1, flags=re.DOTALL)
    toc_items = "\n              ".join(f'<li><a href="{href}">{text}</a></li>' for href, text in a["toc"])
    html = re.sub(r'<ul class="blog-post-toc-list">.*?</ul>', '<ul class="blog-post-toc-list">\n              ' + toc_items + '\n            </ul>', html, count=1, flags=re.DOTALL)
    p.write_text(html, encoding="utf-8")
    text_only = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    text_only = re.sub(r'<[^>]+>', ' ', text_only)
    return len(text_only.split())


def run(articles):
    for a in articles:
        words = process(a)
        print(f'  {a["file"]}: {words} words')
    print(f'Processed {len(articles)} articles.')
