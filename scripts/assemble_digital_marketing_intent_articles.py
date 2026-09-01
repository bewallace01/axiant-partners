"""
Assembles full article pages from body fragments in digital-marketing/fragments/.
Run from repo root: python scripts/assemble_digital_marketing_intent_articles.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAG = ROOT / "digital-marketing" / "fragments"
OUT_DIR = ROOT / "digital-marketing" / "articles"

META_PATH = ROOT / "digital-marketing" / "articles_meta.json"


def word_count_html(html: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return len(text.strip().split())


def faq_json_ld(faqs: list[tuple[str, str]]) -> str:
    items = []
    for q, a in faqs:
        items.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )
    return json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items},
        ensure_ascii=False,
    )


def render_page(m: dict, body: str, wc: int) -> str:
    slug = m["slug"]
    title = m["title"]
    tagline = m["tagline"]
    description = m["description"]
    keywords = m["keywords"]
    og = m["og_image"]
    url = f"https://axiantpartners.com/digital-marketing/articles/{slug}/"
    canonical = url
    faqs = m["faqs"]
    toc = m["toc"]

    breadcrumb = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://axiantpartners.com/"},
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "Digital marketing guides",
                    "item": "https://axiantpartners.com/digital-marketing/articles/",
                },
                {"@type": "ListItem", "position": 3, "name": title, "item": url},
            ],
        },
        ensure_ascii=False,
    )

    blogposting = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "description": description,
            "image": f"https://axiantpartners.com{og}",
            "url": url,
            "datePublished": m.get("date", "2026-04-09T12:00:00-05:00"),
            "dateModified": m.get("date", "2026-04-09T12:00:00-05:00"),
            "author": {"@type": "Organization", "name": "Axiant Partners", "url": "https://axiantpartners.com/"},
            "publisher": {
                "@type": "Organization",
                "name": "Axiant Partners LLC",
                "url": "https://axiantpartners.com/",
                "logo": {"@type": "ImageObject", "url": "https://axiantpartners.com/logo-horizontal-transparent.png"},
            },
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "articleSection": "Digital Marketing",
            "keywords": keywords,
            "isAccessibleForFree": True,
            "audience": {
                "@type": "BusinessAudience",
                "audienceType": "U.S. small and mid-size business owners evaluating marketing vendors",
                "geographicArea": {"@type": "Country", "name": "United States"},
            },
            "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#quick-answer", "h1"]},
        },
        ensure_ascii=False,
    )

    toc_html = "\n".join(
        f'              <li><a href="#{tid}">{label}</a></li>' for tid, label in toc
    )

    faq_block = "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q, a in faqs)

    related = """
<section class="related-resources" aria-label="Related resources">
                <h2>Related resources</h2>
                <ul>
                    <li><a href="/digital-marketing/articles/">Digital marketing guides hub</a></li>
                    <li><a href="/business-growth/articles/">Business Growth articles</a></li>
                    <li><a href="/contact.html">Contact Axiant Partners</a></li>
                    <li><a href="/match.html">Get matched with business financing</a> when growth plans need capital</li>
                    <li><a href="/blog.html">All articles</a></li>
                </ul>
<div class="services-cta">
                <a href="/match.html" class="btn-primary">Get Matched for Business Financing</a>
            </div>
      </section>"""

    # Note: body fragment should end before FAQ if FAQ is in meta; we inject faq_block from meta for AEO consistency
    main_inner = body + "\n<h2 id=\"faq\">FAQ</h2>\n" + faq_block + """
<h2 id="takeaway">Takeaway</h2>
""" + f"""<p>{m.get("takeaway_p1", "")}</p>
<p>{m.get("takeaway_p2", "")}</p>
<h2 id="financing-and-growth-plans">How this connects to financing readiness</h2>
<p>Strong marketing vendors document scope, KPIs, and compliance so leadership can forecast cash and margin. When you pair a clear growth plan with use-of-funds, lenders can evaluate risk more cleanly. Axiant Partners helps U.S. businesses <a href="/match.html">get matched</a> with financing options aligned to your story—not as a substitute for legal or marketing counsel.</p>
<p>If you are restructuring spend across SEO, web, and outbound, <a href="/contact.html">contact us</a> for a financing perspective on timing and liquidity.</p>
""" + related

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="theme-color" content="#0d1f3c">
<style>
  body {{ opacity: 0; }}
</style>
<script>
  document.addEventListener('DOMContentLoaded', function() {{
    document.body.style.opacity = '1';
    document.body.style.transition = 'opacity 0.2s ease';
  }});
</script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HZNSHH6NN0"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-HZNSHH6NN0');
      gtag('config', 'AW-18021105450');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="{description.replace('"', '&quot;')}">
    <meta name="keywords" content="{keywords.replace('"', '&quot;')}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{canonical}">
    <meta property="og:title" content="{title.replace('"', '&quot;')} | Axiant Partners">
    <meta property="og:description" content="{description.replace('"', '&quot;')}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="https://axiantpartners.com{og}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="Axiant Partners">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title.replace('"', '&quot;')} | Axiant Partners">
    <meta name="twitter:description" content="{description.replace('"', '&quot;')}">
    <meta property="article:published_time" content="{m.get("date", "2026-04-09T12:00:00-05:00")}">
    <meta property="article:modified_time" content="{m.get("date", "2026-04-09T12:00:00-05:00")}">
    <meta property="article:section" content="Digital Marketing">
    <title>{title.replace('"', '&quot;')} | Axiant Partners</title>
    <link rel="icon" type="image/webp" sizes="48x48" href="/favicon.webp"><link rel="icon" type="image/png" sizes="48x48" href="/favicon.png"><link rel="apple-touch-icon" href="/favicon.png">
<style>.article-quick-answer{{margin:1rem 0 1.25rem;padding:1rem 1.1rem;border-left:4px solid #2d7fb8;background:var(--bg-card, #f0f4f8);border-radius:0 8px 8px 0;font-size:1.02rem;line-height:1.55}}[data-theme="dark"] .article-quick-answer{{background:#1e293b;border-left-color:#60a5fa}}</style>
<link rel="stylesheet" href="../../../critical.css?v=2026032199">
<link rel="stylesheet" href="/blog-layout.css?v=2026033014">
<link rel="stylesheet" href="/article-rail.css?v=2026040801">
<link rel="stylesheet" href="../../../styles.css?v=2026032199" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="/article-layout.css">
    <noscript><link rel="stylesheet" href="../../../styles.css?v=2026032199"></noscript>
<script type="application/ld+json">{breadcrumb}</script>
<script type="application/ld+json">{blogposting}</script>
<script type="application/ld+json">{faq_json_ld(faqs)}</script>
<script type="application/ld+json">{json.dumps({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": "Axiant Partners", "url": "https://axiantpartners.com/"},
        "about": {"@type": "Thing", "name": "U.S. digital marketing vendor selection and business growth"},
        "spatialCoverage": {"@type": "Country", "name": "United States"},
    }, ensure_ascii=False)}</script>
</head>
<body>
    <div class="mobile-nav-overlay" id="mobileNavOverlay">
    <div class="nav-top">
        <picture><source srcset="/Axiant_light_logo.webp" type="image/webp"><img src="/Axiant_light_logo.png" alt="Axiant Partners" style="height: 40px;"></picture>
        <button class="nav-close" id="mobileNavClose" aria-label="Close menu">&#215;</button>
    </div>
    <nav class="mobile-overlay-links" id="mobileOverlayNavLinks"></nav>
</div>
<div class="container">
        <nav class="main-nav">
            <div class="nav-brand"><a href="/"><picture><source srcset="../../../logo-horizontal-transparent.webp" type="image/webp"><img src="../../../logo-horizontal-transparent.png" alt="Axiant Partners Logo" class="nav-logo nav-logo-light" width="180" height="74"></picture><picture><source srcset="../../../Axiant_light_logo.webp" type="image/webp"><img src="../../../Axiant_light_logo.png" alt="Axiant Partners Logo" class="nav-logo nav-logo-dark" width="180" height="74"></picture></a><span>Axiant Partners</span></div>
            <button class="mobile-menu-toggle" id="mobileNavToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/match.html">Find Match</a>
                <div class="nav-dropdown nav-dropdown-desktop"><button type="button" class="nav-dropdown-trigger" aria-haspopup="true" aria-expanded="false">Services</button><div class="nav-dropdown-menu"></div></div><a href="/services.html" class="nav-link-mobile">Services</a>
                <a href="/calculator.html">Calculator</a>
                <a href="/contact.html">Contact</a>
                <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"></button>
            </div>
        </nav>
        <header>
            <h1>{title.replace('"', '&quot;')}</h1>
            <p class="tagline">{tagline.replace('"', '&quot;')}</p>
        </header>
        <div class="form-container blog-post-content article-page digital-marketing-article">
    <div class="blog-post-shell">
      <aside class="blog-post-rail-left article-rail article-rail--left"><div class="article-rail__inner">
        <div class="article-rail__block">
          <p class="blog-rail-back"><a href="../">&larr; Digital marketing guides</a> | <a href="/blog.html">All Articles</a></p>
          <div class="blog-rail-meta-item"><span class="blog-rail-label">Updated</span> April 9, 2026</div>
        </div>
        <div class="article-rail__block">
          <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick answer</h3><p>{tagline.replace('"', '&quot;')}</p></div></div>
        </div>
        <div class="article-rail__block article-rail__block--cta blog-rail-cta">
          <h3>Funding growth?</h3>
          <p>Match with lenders when your plan and cash story are ready.</p>
          <a href="/match.html" class="btn-primary">Get Matched for Business Financing</a>
        </div>
      </div></aside>
      <main class="blog-post-main">
<p id="quick-answer" class="article-quick-answer" data-aeo="summary"><strong>In short:</strong> {tagline.replace('"', '&quot;')}</p>
<p class="growth-article-geo" data-geo="us-context"><strong>U.S. context:</strong> Telemarketing, texting, email, and AI-generated outreach may implicate federal and state laws (including TCPA, CAN-SPAM, state mini-TCPA, and consumer protection rules) and advertising substantiation. Website accessibility and privacy policies vary by state. This guide is educational—not legal advice. Confirm compliance with qualified counsel. Axiant Partners provides business financing education and matching, not legal or agency execution.</p>

{main_inner}

      </main>
      <aside class="blog-post-rail-right article-rail article-rail--right"><div class="article-rail__inner article-rail__inner--toc"><div class="blog-rail-toc">
          <h3>On this page</h3>
          <nav aria-label="On this page">
            <ul class="blog-post-toc-list">
{toc_html}
              <li><a href="#faq">FAQ</a></li>
              <li><a href="#takeaway">Takeaway</a></li>
              <li><a href="#financing-and-growth-plans">Financing readiness</a></li>
            </ul>
          </nav>
        </div></div></aside>
    </div></div>
    </div>
    <footer class="site-footer">
        <p>&copy; 2026 Axiant Partners. All rights reserved. | <a href="/privacy-policy.html">Privacy Policy</a> | <a href="/terms-and-conditions.html">Terms and Conditions</a> | <a href="/vendors.html">Vendors</a></p>
    </footer>
    <script src="../../../language-switcher.js?v=2026032199" defer></script>
    <script src="/script.js?v=2026032199" defer></script>
<script>
  if ('serviceWorker' in navigator) {{
    window.addEventListener('load', function() {{
      navigator.serviceWorker.register('/sw.js');
    }});
  }}
</script>
</body>
</html>
"""


HUB_IMG = {
    "ai-lead-generation-what-you-are-buying": "/assets/ai-growth-1.webp",
    "ai-appointment-setting-vs-human-sdrs": "/assets/ai-growth-2.webp",
    "cold-email-ai-personalization-compliance-us": "/assets/ai-bridge-2.webp",
    "seo-cost-2026-agency-freelancer-in-house": "/assets/rbf-marketing-1200w.webp",
    "seo-agency-vs-in-house-vs-fractional-model": "/assets/business-growth-strategy-intro.webp",
    "red-flags-hiring-seo-company": "/assets/business-growth-analytics-kpis.webp",
    "website-redesign-vs-conversion-refresh-leads": "/assets/business-growth-content-marketing.webp",
    "small-business-website-pages-seo-conversion": "/assets/wcl-intro-cashflow-560w.webp",
    "lead-gen-stack-seo-website-outbound-order": "/assets/business-growth-lead-pipeline.webp",
    "rfp-template-leads-seo-website-vendor": "/assets/sbl-strategic-timing-800w.webp",
}


def write_hub_index(meta: list) -> None:
    hub_path = OUT_DIR / "index.html"
    items = []
    cards = []
    for i, m in enumerate(meta, start=1):
        slug = m["slug"]
        url = f"https://axiantpartners.com/digital-marketing/articles/{slug}/"
        items.append({"@type": "ListItem", "position": i, "url": url})
        img = HUB_IMG.get(slug, "/assets/ai-growth-1.webp")
        title_esc = m["title"].replace("&", "&amp;")
        desc_esc = m["description"].replace("&", "&amp;")
        cards.append(
            f"""                <article class="blog-card blog-card--media">
                    <a class="blog-card-media" href="{slug}/"><img src="{img}" alt="" width="640" height="360" loading="lazy" decoding="async"></a>
                    <h3 class="blog-card-title"><a href="{slug}/">{title_esc}</a></h3>
                    <p class="blog-card-excerpt">{desc_esc}</p>
                    <a href="{slug}/" class="blog-card-link">Read more</a>
                </article>"""
        )
    itemlist = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "Digital marketing intent guides",
            "numberOfItems": len(meta),
            "itemListElement": items,
        },
        ensure_ascii=False,
    )
    grid = "\n".join(cards)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="description" content="High-intent U.S. guides: AI lead generation, appointment setting, cold email compliance, SEO pricing and hiring, website IA, lead-gen sequencing, and marketing RFPs.">
<meta name="keywords" content="AI lead generation, SEO cost 2026, hire SEO company, website redesign, marketing RFP, cold email compliance, SMB digital marketing">
<link rel="canonical" href="https://axiantpartners.com/digital-marketing/articles/">
<title>Digital Marketing Guides: AI Leads, SEO &amp; Web (U.S. SMB) | Axiant Partners</title>
<link rel="icon" type="image/webp" sizes="48x48" href="/favicon.webp"><link rel="icon" type="image/png" sizes="48x48" href="/favicon.png">
<link rel="stylesheet" href="../../critical.css?v=2026032199">
<link rel="stylesheet" href="../../styles.css?v=2026032199" media="print" onload="this.media='all'">
<link rel="stylesheet" href="/article-layout.css">
<link rel="stylesheet" href="/business-growth-articles-hub.css">
<noscript><link rel="stylesheet" href="../../styles.css?v=2026032199"></noscript>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://axiantpartners.com/"}},{{"@type":"ListItem","position":2,"name":"Articles","item":"https://axiantpartners.com/blog.html"}},{{"@type":"ListItem","position":3,"name":"Digital marketing guides","item":"https://axiantpartners.com/digital-marketing/articles/"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"CollectionPage","name":"Digital Marketing Guides","description":"High-intent guides for U.S. SMBs buying AI lead programs, SEO, and website work.","url":"https://axiantpartners.com/digital-marketing/articles/","isPartOf":{{"@type":"WebSite","name":"Axiant Partners","url":"https://axiantpartners.com/"}},"spatialCoverage":{{"@type":"Country","name":"United States"}}}}</script>
<script type="application/ld+json">{itemlist}</script>
</head>
<body>
<div class="container">
<nav class="main-nav">
<div class="nav-brand"><a href="/"><picture><source srcset="../../logo-horizontal-transparent.webp" type="image/webp"><img src="../../logo-horizontal-transparent.png" alt="Axiant Partners Logo" class="nav-logo nav-logo-light" width="180" height="74"></picture><picture><source srcset="../../Axiant_light_logo.webp" type="image/webp"><img src="../../Axiant_light_logo.png" alt="Axiant Partners Logo" class="nav-logo nav-logo-dark" width="180" height="74"></picture></a><span>Axiant Partners</span></div>
<button class="mobile-menu-toggle" id="mobileNavToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
<div class="nav-links">
<a href="/match.html">Find Match</a>
<a href="/">Home</a>
<a href="/services.html">Services</a>
<a href="/business-growth.html">Business Growth</a>
<a href="/contact.html">Contact</a>
<button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"></button>
</div>
</nav>
<header>
<h1>Digital Marketing Guides</h1>
<p class="tagline">High-intent playbooks for U.S. owners buying AI-assisted leads, SEO, and website work—definitions, compliance, pricing, and procurement</p>
</header>
<div class="form-container blog-content blog-listing growth-hub-listing">
<p class="blog-back"><a href="/blog.html" class="btn-secondary blog-back-btn">&larr; All Articles</a> <a href="/business-growth/articles/" class="btn-secondary blog-back-btn">Business Growth articles</a></p>
<div class="growth-hub-intro-visual">
<p class="results-intro growth-hub-intro-copy"><strong>In short:</strong> These guides target <strong>commercial investigation</strong> searches: what to buy, how to vet vendors, and how to stay compliant while scaling. Each long-form piece includes quick answers for AEO, U.S. legal context notes (not legal advice), FAQ schema, and internal links to financing resources when growth spend touches capital planning.</p>
<img src="/assets/rbf-marketing-1200w.webp" alt="Digital marketing strategy and search visibility" width="640" height="400" loading="eager" decoding="async">
</div>
<div class="blog-grid">
{grid}
</div>
<div class="services-cta">
<h3>Funding a growth plan?</h3>
<p>When your marketing scope and use of funds are clear, we can help you explore financing matches.</p>
<a href="/match.html" class="btn-primary">Get Started Now</a>
</div>
</div>
</div>
<footer class="site-footer">
<p>&copy; 2026 Axiant Partners. All rights reserved. | <a href="/privacy-policy.html">Privacy Policy</a> | <a href="/terms-and-conditions.html">Terms and Conditions</a> | <a href="/vendors.html">Vendors</a></p>
</footer>
<script src="../../language-switcher.js?v=2026032199" defer></script>
<script src="/script.js?v=2026032199" defer></script>
</body>
</html>
"""
    hub_path.write_text(html, encoding="utf-8")
    print("Wrote hub", hub_path)


def main() -> None:
    meta = json.loads(META_PATH.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_hub_index(meta)
    for m in meta:
        slug = m["slug"]
        frag_path = FRAG / f"{slug}.html"
        if not frag_path.is_file():
            raise SystemExit(f"Missing fragment: {frag_path}")
        body = frag_path.read_text(encoding="utf-8").strip()
        wc = word_count_html(body)
        if wc < 2000:
            raise SystemExit(f"{slug}: body word count {wc} < 2000")
        page = render_page(m, body, wc)
        dest = OUT_DIR / slug / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        print(f"OK {slug}: {wc} words (fragment)")


if __name__ == "__main__":
    main()
