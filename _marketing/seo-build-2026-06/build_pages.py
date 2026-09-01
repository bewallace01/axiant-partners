#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO/AEO/GEO page builder for Axiant Partners — niche equipment/practice financing.
Shared boilerplate (head/nav/footer/CSS/scripts) is identical to existing
/equipment-financing/articles/ pages; ALL content (tables, sections, FAQs, HowTo,
schema) is hand-authored and unique per page. No number-swap templating.

Run from repo root:  python3 _marketing/seo-build-2026-06/build_pages.py
"""
import json, os, html

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ART_DIR = os.path.join(REPO, "equipment-financing", "articles")
TODAY = "2026-06-02"
BASE = "https://axiantpartners.com"

# ---- shared inline mobile-critical CSS (verbatim from existing article pages) ----
MOBILE_CRITICAL = """
/* Mobile critical CSS - above-the-fold only, inline for zero network requests */
:root{--bg-primary:linear-gradient(180deg,#f0f4f8 0,#e8f0f6 50%,#f5f8fb 100%);--bg-secondary:linear-gradient(180deg,#fff 0,#f8fafc 100%);--bg-nav:linear-gradient(180deg,rgba(255,255,255,0.98) 0,rgba(248,250,252,0.98) 100%);--bg-card:linear-gradient(180deg,#fff 0,#f0f4f8 100%);--text-primary:#1a1a1a;--text-secondary:#4a4a4a;--text-tertiary:#666;--border-color:rgba(45,127,184,0.2);--accent-color:#2d7fb8;--accent-dark:#1e3a5f;--shadow-color:rgba(30,58,95,0.15);--nav-shadow:rgba(30,58,95,0.1);--header-overlay:linear-gradient(135deg,rgba(30,58,95,0.85) 0,rgba(45,127,184,0.85) 100%);--pattern-opacity:.12}
[data-theme="dark"]{--bg-primary:linear-gradient(180deg,#0f172a 0,#1e293b 50%,#0f172a 100%);--bg-secondary:linear-gradient(180deg,#1e293b 0,#334155 100%);--bg-nav:linear-gradient(180deg,rgba(30,41,59,0.98) 0,rgba(15,23,42,0.98) 100%);--bg-card:linear-gradient(180deg,#1e293b 0,#0f172a 100%);--text-primary:#f1f5f9;--text-secondary:#cbd5e1;--text-tertiary:#94a3b8;--border-color:rgba(45,127,184,0.3);--accent-color:#60a5fa;--accent-dark:#3b82f6;--shadow-color:rgba(0,0,0,0.5);--nav-shadow:rgba(0,0,0,0.3);--header-overlay:linear-gradient(135deg,rgba(15,23,42,0.9) 0,rgba(30,41,59,0.9) 100%);--pattern-opacity:.15}
*{margin:0;padding:0;box-sizing:border-box}
html{margin:0;padding:0;overflow-x:hidden;font-size:14px;text-size-adjust:100%;-webkit-text-size-adjust:100%;max-width:100%;width:100%}
body{margin:0;padding:0;max-width:100%;overflow-x:hidden;font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg-primary);min-height:100vh;line-height:1.6;color:var(--text-primary);font-size:14px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;position:relative;width:100%}
body::before{content:'';position:fixed;top:0;left:0;right:0;bottom:0;background-image:radial-gradient(circle at 20% 50%,rgba(45,127,184,var(--pattern-opacity)) 0,transparent 50%),radial-gradient(circle at 80% 80%,rgba(30,58,95,var(--pattern-opacity)) 0,transparent 50%);pointer-events:none;z-index:0}
.container{width:100%;max-width:100%;margin:0;padding:0;position:relative;z-index:1;min-width:0}
.main-nav{background:var(--bg-nav);border-bottom:1px solid var(--border-color);padding:12px 16px;position:sticky;top:0;z-index:1000;width:100%;max-width:100%;display:flex;justify-content:space-between;align-items:center;min-width:0;box-sizing:border-box}
.nav-brand{display:flex;align-items:center;gap:0;font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:600;color:var(--text-primary)}
.nav-logo,.nav-logo-light,.nav-logo-dark{height:64px;width:auto;max-height:64px;object-fit:contain;object-position:left center}
.nav-brand span{display:none !important}
.nav-logo-dark{display:none !important}
html[data-theme="dark"] .main-nav .nav-logo-light{display:none !important;visibility:hidden !important;position:absolute !important;width:0 !important;height:0 !important;overflow:hidden !important}
html[data-theme="dark"] .main-nav .nav-logo-dark{display:block !important;visibility:visible !important}
.mobile-menu-toggle{display:flex;flex-direction:column;justify-content:center;align-items:center;gap:5px;min-width:48px;min-height:48px;padding:12px;border:0;background:0;cursor:pointer;color:var(--text-primary);-webkit-tap-highlight-color:transparent}
.mobile-menu-toggle span{display:block;width:22px;height:2px;background:currentColor;border-radius:1px}
.hero-grid{min-height:280px}
header{background:var(--header-overlay) center/cover no-repeat;text-align:center;color:#fff;padding:60px 20px 50px;margin:0;position:relative;overflow:hidden}
.match-hero-wrap,.calculator-hero-wrap,.contact-hero-wrap,.referral-hero-wrap{position:relative;overflow-x:visible;overflow-y:visible;width:100%;min-width:0}
.btn-primary,.btn-secondary{min-height:48px;padding:12px 20px;font-weight:600;border-radius:10px;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;text-align:center;text-decoration:none;border:2px solid;transition:all .2s ease}
.btn-primary{background:linear-gradient(135deg,var(--accent-color) 0,var(--accent-dark) 100%);color:#fff !important;border-color:transparent}
.btn-secondary{background:var(--bg-card);color:var(--accent-color) !important;border-color:var(--accent-color)}
.mobile-nav-overlay,#mobileNavOverlay{position:fixed;inset:0;z-index:9999;background:#0d1f3c;display:none;flex-direction:column;align-items:stretch;padding:1rem 1rem 1rem 1.5rem;overflow-x:hidden;overflow-y:auto;width:100%;max-width:100%;box-sizing:border-box}
.mobile-nav-overlay.open,#mobileNavOverlay.open{display:flex!important}
.mobile-nav-overlay .nav-top,#mobileNavOverlay .nav-top{display:flex;justify-content:space-between;align-items:center;width:100%;margin-bottom:1rem;min-width:0}
.mobile-nav-overlay .nav-close,#mobileNavOverlay .nav-close{background:0;border:0;color:rgba(255,255,255,.8);font-size:1.5rem;cursor:pointer;padding:8px;-webkit-tap-highlight-color:transparent}
.mobile-nav-overlay .mobile-overlay-links,#mobileNavOverlay .mobile-overlay-links{display:flex!important;flex-direction:column!important;align-items:flex-start!important;justify-content:flex-start!important;flex:0 1 auto!important;width:100%!important;min-width:0;padding-left:0;padding-top:0}
.mobile-nav-overlay .mobile-overlay-links a,#mobileNavOverlay .mobile-overlay-links a{color:#fff!important;font-size:1.1rem!important;font-weight:600!important;text-align:left!important;padding:12px 0!important;display:block!important;width:100%!important;text-decoration:none!important;border-bottom:1px solid rgba(255,255,255,.15)!important;background:0!important}
""".strip("\n")

TABLE_OPEN = '<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;"><thead><tr style="background: var(--bg-card);">'
TH = '<th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">{}</th>'
TD = '<td style="padding: 12px 16px; border: 1px solid var(--border-color);">{}</td>'

def cost_table(headers, rows):
    out = [TABLE_OPEN + "".join(TH.format(h) for h in headers) + "</tr></thead><tbody>"]
    for r in rows:
        out.append("<tr>" + "".join(TD.format(c) for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)

def build(page):
    slug = page["slug"]
    url = f"{BASE}/equipment-financing/articles/{slug}/"
    # ---- schema blocks ----
    breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"},
        {"@type":"ListItem","position":2,"name":"Equipment Financing","item":f"{BASE}/equipment-financing.html"},
        {"@type":"ListItem","position":3,"name":"Articles","item":f"{BASE}/equipment-financing/articles/"},
        {"@type":"ListItem","position":4,"name":page["breadcrumb"],"item":url}]}
    article = {"@context":"https://schema.org","@type":"Article","headline":page["breadcrumb"],
        "description":page["schema_desc"],
        "image":{"@type":"ImageObject","url":f"{BASE}/assets/equipment-financing-hero.webp","width":1200,"height":630},
        "url":url,"datePublished":TODAY,"dateModified":TODAY,
        "author":{"@type":"Organization","name":"Axiant Partners","url":BASE},
        "publisher":{"@id":f"{BASE}/#organization"},
        "mainEntityOfPage":{"@type":"WebPage","@id":url},
        "articleSection":"Equipment Financing","keywords":page["keywords"]}
    faqpage = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in page["faqs"]]}
    webpage = {"@context":"https://schema.org","@type":"WebPage","@id":f"{url}#webpage","url":url,
        "name":page["breadcrumb"],"speakable":{"@type":"SpeakableSpecification","cssSelector":[".quick-answer"]}}
    howto = {"@context":"https://schema.org","@type":"HowTo","name":page["howto_name"],
        "description":page["howto_desc"],"totalTime":"P3D","step":[
        {"@type":"HowToStep","position":i+1,"name":s[0],"text":s[1]} for i,s in enumerate(page["howto_steps"])]}

    def ld(obj):
        return '    <script type="application/ld+json">\n    ' + json.dumps(obj, ensure_ascii=False) + '\n    </script>'

    # ---- sections + TOC ----
    sections_html = []
    toc_items = []
    for sec in page["sections"]:
        sections_html.append(f'<h2 id="{sec["id"]}">{sec["h2"]}</h2>{sec["body"]}')
        toc_items.append(f'<li><a href="#{sec["id"]}">{sec["h2"]}</a></li>')
    sections_html = "\n            ".join(sections_html)
    toc_html = "\n              ".join(toc_items)

    related_html = "\n                    ".join(
        f'<li><a href="{href}">{label}</a></li>' for href,label in page["related"])

    mc = MOBILE_CRITICAL
    doc = f'''<!DOCTYPE html>
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

    <!-- Google tag (gtag.js) -->
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
    <meta name="description" content="{page['meta']}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <meta name="author" content="Axiant Partners">
    <link rel="canonical" href="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="og:title" content="{page['og_title']}">
    <meta property="og:description" content="{page['og_desc']}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{BASE}/assets/equipment-financing-hero.webp">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="Axiant Partners">
    <meta property="article:section" content="Equipment Financing">
    <meta property="article:published_time" content="{TODAY}">
    <meta property="article:modified_time" content="{TODAY}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{page['og_title']}">
    <meta name="twitter:description" content="{page['tw_desc']}">
    <title>{page['title']}</title>
    <link rel="icon" type="image/webp" sizes="48x48" href="/favicon.webp"><link rel="icon" type="image/png" sizes="48x48" href="/favicon.png"><link rel="apple-touch-icon" href="/favicon.png">
    <style id="mobile-critical">
{mc}
</style>
<link rel="stylesheet" href="../../../critical.css?v=2026032199">
<link rel="stylesheet" href="/blog-layout.css?v=2026033014">
<link rel="stylesheet" href="/article-rail.css?v=2026040801">
    <style id="mobile-critical">
{mc}
</style>
<link rel="stylesheet" href="../../../styles.css?v=2026032199" media="print" onload="this.media='all'">
    <link rel="stylesheet" href="/article-layout.css">
    <noscript><style id="mobile-critical">
{mc}
</style>
<link rel="stylesheet" href="../../../styles.css?v=2026032199"></noscript>
{ld(breadcrumb)}
{ld(article)}
{ld(faqpage)}
{ld(webpage)}
{ld(howto)}
</head>
<body>
    <div class="mobile-nav-overlay" id="mobileNavOverlay">
    <div class="nav-top">
        <picture><source srcset="/Axiant_light_logo.webp" type="image/webp"><img src="/Axiant_light_logo.png" alt="Axiant Partners" style="height: 40px;"></picture>
        <button class="nav-close" id="mobileNavClose" aria-label="Close menu">&#215;</button>
    </div>
    <nav class="mobile-overlay-links" id="mobileOverlayNavLinks">
        <!-- Links copied from main nav by JS -->
    </nav>
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
            <h1>{page['h1']}</h1>
            <p class="tagline">{page['tagline']}</p>
        </header>
        <div class="form-container blog-post-content article-page">    <div class="blog-post-shell">
      <aside class="blog-post-rail-left article-rail article-rail--left"><div class="article-rail__inner">
        <div class="article-rail__block">
          <p class="blog-rail-back"><a href="../">&larr; Back to Equipment Financing Articles</a></p>
          <div class="blog-rail-meta-item"><span class="blog-rail-label">Updated</span> June 2, 2026</div>
        </div>
        <div class="article-rail__block">
          <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick Facts</h3><p>{page['quick_facts']}</p></div></div>
        </div>
        <div class="article-rail__block article-rail__block--cta blog-rail-cta">
          <h3>{page['rail_cta_h']}</h3>
          <p>{page['rail_cta_p']}</p>
          <a href="/match.html" class="btn-primary">{page['cta_label']}</a>
        </div>


      </div></aside>
      <main class="blog-post-main">
<div class="quick-answer" style="background:var(--bg-card);border-left:4px solid var(--accent-color);padding:16px 18px;margin:0 0 28px;border-radius:10px;">
  <strong style="display:block;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent-color);margin-bottom:6px;">Quick answer</strong>
  <p style="margin:0;font-size:1rem;line-height:1.55;color:var(--text-primary);">{page['quick_answer']}</p>
  <p style="margin:12px 0 0;font-size:0.92rem;color:var(--text-secondary);"><a href="/match.html" style="color:var(--accent-color);font-weight:600;">Get matched &rarr;</a></p>
</div>
            <p>{page['intro']}</p>

            {sections_html}

<section class="related-resources" aria-label="Related resources">
                <h2>Related Resources</h2>
                <ul>
                    {related_html}
                </ul>
<div class="services-cta">
                <a href="/match.html" class="btn-primary">{page['cta_label']}</a>
            </div>
</section>
</main>
                  <aside class="blog-post-rail-right article-rail article-rail--right"><div class="article-rail__inner article-rail__inner--toc"><div class="blog-rail-toc">
          <h3>On this page</h3>
          <nav aria-label="On this page">
            <ul class="blog-post-toc-list">
              {toc_html}
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
<script>
  const prefetched = new Set();
  function prefetchPage(url) {{
    if (prefetched.has(url)) return;
    prefetched.add(url);
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = url;
    document.head.appendChild(link);
  }}
  document.addEventListener('mouseover', function(e) {{
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel')) return;
    prefetchPage(href);
  }});
  document.addEventListener('touchstart', function(e) {{
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel')) return;
    prefetchPage(href);
  }}, {{ passive: true }});
</script>
<script>
  document.addEventListener('click', function(e) {{
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || anchor.target === '_blank') return;
    e.preventDefault();
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.15s ease';
    setTimeout(() => {{ window.location.href = href; }}, 150);
  }});
</script>
<script>
if(window.innerWidth<=768){{var ls=document.querySelectorAll('.about-section,.testimonials-section,.global-bottom-cta,.site-footer-enhanced,.services-grid,.blog-grid,.steps-grid,.benefits-grid');var so=new IntersectionObserver(function(e){{e.forEach(function(entry){{if(entry.isIntersecting){{entry.target.style.opacity='1';entry.target.style.transform='none';so.unobserve(entry.target);}}}});}},{{rootMargin:'100px'}});ls.forEach(function(s){{s.style.opacity='0';s.style.transition='opacity 0.3s ease';so.observe(s);}});}}
</script>
</body>
</html>
'''
    out_dir = os.path.join(ART_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    return url

# common related-resource sets
EQ_COMMON = [
    ("/equipment-financing.html", "Equipment Financing Hub"),
    ("../equipment-financing-requirements/", "Equipment Financing Requirements"),
    ("../section-179-tax-strategy-2026/", "Section 179 Tax Strategy"),
    ("../can-you-finance-used-equipment/", "Can You Finance Used Equipment?"),
    ("../equipment-financing-vs-sba-loan/", "Equipment Financing vs SBA Loan"),
    ("/sba-loans/articles/sba-504-vs-7a-decision-tree/", "SBA 504 vs 7(a)"),
]

if __name__ == "__main__":
    import importlib, sys
    mod = sys.argv[1] if len(sys.argv) > 1 else "pages_batch1"
    sys.path.insert(0, os.path.dirname(__file__))
    PAGES = importlib.import_module(mod).PAGES  # content lives in a separate file per batch
    for p in PAGES:
        u = build(p)
        print("built:", u)
