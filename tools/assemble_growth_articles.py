# -*- coding: utf-8 -*-
"""Emit business-growth/articles/*/index.html from batch modules (SEO, AEO, GEO-ready)."""
from __future__ import annotations

import html as html_module
import json
import pathlib
import re
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "business-growth" / "articles"
TOOLS = pathlib.Path(__file__).resolve().parent
SUPP_DIR = TOOLS / "article_supplements"
INCLUDES = TOOLS / "includes"
HEAD_STYLES_PATH = INCLUDES / "article_page_head_styles.inc.html"

BASE_URL = "https://axiantpartners.com"
ARTICLE_DATE = "2026-04-09"
OG_IMAGE = f"{BASE_URL}/assets/ai-growth-1.webp"
ASSET_QUERY = "v=2026032199"

H2_RE = re.compile(r"<h2(\s[^>]*)?>([\s\S]*?)</h2>", re.I)

HEAD_TOP = """<!DOCTYPE html>
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
    <meta name="description" content="{desc_esc}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{canonical}">
    <meta property="og:title" content="{title_esc} | Axiant Partners">
    <meta property="og:description" content="{desc_esc}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="Axiant Partners">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_esc} | Axiant Partners">
    <meta name="twitter:description" content="{desc_esc}">
    <meta property="article:published_time" content="{iso_date}"><meta property="article:modified_time" content="{iso_date}">
    <meta property="article:section" content="Business Growth">
    <title>{title_esc} | Axiant Partners</title>
    <link rel="icon" type="image/webp" sizes="48x48" href="/favicon.webp"><link rel="icon" type="image/png" sizes="48x48" href="/favicon.png"><link rel="apple-touch-icon" href="/favicon.png">
<style>.article-quick-answer{{margin:1rem 0 1.25rem;padding:1rem 1.1rem;border-left:4px solid #2d7fb8;background:var(--bg-card, #f0f4f8);border-radius:0 8px 8px 0;font-size:1.02rem;line-height:1.55}}[data-theme="dark"] .article-quick-answer{{background:#1e293b;border-left-color:#60a5fa}}</style>
"""

BODY_OPEN = """</head>
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
            <h1>__HEADER_H1__</h1>
            <p class="tagline">__TAGLINE__</p>
        </header>
        <div class="form-container blog-post-content article-page growth-article-content">    <div class="blog-post-shell">
__LEFT_RAIL__
      <main class="blog-post-main">
__MAIN_INNER__
      </main>
__RIGHT_RAIL__
    </div></div>
    </div>
    <footer class="site-footer">
        <p>&copy; 2026 Axiant Partners. All rights reserved. | <a href="/privacy-policy.html">Privacy Policy</a> | <a href="/terms-and-conditions.html">Terms and Conditions</a> | <a href="/vendors.html">Vendors</a></p>
    </footer>
    <script src="../../../language-switcher.js?__ASSET_Q__" defer></script>
    <script src="/script.js?__ASSET_Q__" defer></script>
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
      navigator.serviceWorker.register('/sw.js');
    });
  }
</script>
<script>
  const prefetched = new Set();
  function prefetchPage(url) {
    if (prefetched.has(url)) return;
    prefetched.add(url);
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = url;
    document.head.appendChild(link);
  }
  document.addEventListener('mouseover', function(e) {
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel')) return;
    prefetchPage(href);
  });
  document.addEventListener('touchstart', function(e) {
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel')) return;
    prefetchPage(href);
  }, { passive: true });
</script>
<script>
  document.addEventListener('click', function(e) {
    const anchor = e.target.closest('a');
    if (!anchor) return;
    const href = anchor.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || anchor.target === '_blank') return;
    e.preventDefault();
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.15s ease';
    setTimeout(() => { window.location.href = href; }, 150);
  });
</script>
<script>
if(window.innerWidth<=768){var ls=document.querySelectorAll('.about-section,.testimonials-section,.global-bottom-cta,.site-footer-enhanced,.services-grid,.blog-grid,.steps-grid,.benefits-grid');var so=new IntersectionObserver(function(e){e.forEach(function(entry){if(entry.isIntersecting){entry.target.style.opacity='1';entry.target.style.transform='none';so.unobserve(entry.target);}});},{rootMargin:'100px'});ls.forEach(function(s){s.style.opacity='0';s.style.transition='opacity 0.3s ease';so.observe(s);});}
</script>
</body>
</html>
"""


def load_batches():
    from growth_articles_batch_01 import BATCH as b1
    from growth_articles_batch_02 import BATCH as b2
    from growth_articles_batch_03 import BATCH as b3
    from growth_articles_batch_04 import BATCH as b4

    return b1 + b2 + b3 + b4


def strip_html(s: str) -> str:
    t = re.sub(r"<[^>]+>", " ", s)
    t = re.sub(r"\s+", " ", t).strip()
    return html_module.unescape(t)


def slugify_heading(text: str) -> str:
    t = text.lower().strip()
    t = re.sub(r"[^a-z0-9\s-]", "", t)
    t = re.sub(r"\s+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    return t


def extract_operator_faqs(html: str) -> list[tuple[str, str]]:
    m = re.search(r"<h2[^>]*>\s*Operator FAQ\s*</h2>", html, re.I)
    if not m:
        return []
    start = m.start()
    chunk = html[start : start + 12000]
    pairs = re.findall(r"<h3>([\s\S]*?)</h3>\s*<p>([\s\S]*?)</p>", chunk)
    out = []
    for q, a in pairs:
        qs, ans = strip_html(q), strip_html(a)
        if qs and ans:
            out.append((qs, ans))
    return out[:12]


def inject_quick_answer(body: str, desc_plain: str) -> str:
    """AEO: direct answer block immediately after H1 for snippets / answer engines."""
    desc_esc = html_module.escape(desc_plain)
    m = re.search(r"(<h1>[\s\S]*?</h1>)", body, re.I)
    if not m:
        return body
    block = (
        f'\n<p id="quick-answer" class="article-quick-answer" data-aeo="summary">'
        f"<strong>In short:</strong> {desc_esc}</p>\n"
        f'<p class="growth-article-geo" data-geo="us-context"><strong>U.S. context:</strong> '
        f"Rules (calling, texting, email), payment timing, and lender norms vary by state and industry; "
        f"confirm material points with qualified legal, tax, and financing advisors.</p>\n"
    )
    return body[: m.end()] + block + body[m.end() :]


def remove_h1(body: str) -> tuple[str, str]:
    m = re.search(r"<h1[^>]*>([\s\S]*?)</h1>", body, re.I)
    if not m:
        return body, ""
    title = strip_html(m.group(1))
    return body[: m.start()] + body[m.end() :], title


def ensure_h2_ids_and_toc(html: str) -> tuple[str, list[tuple[str, str]]]:
    seen: set[str] = set()
    toc: list[tuple[str, str]] = []

    def unique_slug(base: str) -> str:
        b = base or "section"
        if b not in seen:
            seen.add(b)
            return b
        n = 2
        while f"{b}-{n}" in seen:
            n += 1
        hid = f"{b}-{n}"
        seen.add(hid)
        return hid

    def repl(m: re.Match[str]) -> str:
        attrs = m.group(1) or ""
        inner = m.group(2)
        text_plain = strip_html(inner)
        if re.search(r"\bid\s*=", attrs, re.I):
            idm = re.search(r'id\s*=\s*"([^"]*)"', attrs, re.I)
            hid = (idm.group(1) if idm else "") or unique_slug(slugify_heading(text_plain))
            if hid not in seen:
                seen.add(hid)
            toc.append((hid, text_plain))
            return m.group(0)
        base = slugify_heading(text_plain) or "section"
        hid = unique_slug(base)
        toc.append((hid, text_plain))
        attrs = attrs.strip()
        id_attr = f' id="{html_module.escape(hid)}"'
        if attrs:
            return f"<h2{attrs}{id_attr}>{inner}</h2>"
        return f"<h2{id_attr}>{inner}</h2>"

    return H2_RE.sub(repl, html), toc


def build_left_rail(desc_plain: str, updated_display: str) -> str:
    desc_esc = html_module.escape(desc_plain)
    upd_esc = html_module.escape(updated_display)
    return f"""      <aside class="blog-post-rail-left article-rail article-rail--left"><div class="article-rail__inner">
        <div class="article-rail__block">
          <p class="blog-rail-back"><a href="../">&larr; Back to Growth Articles</a> | <a href="/blog.html">All Articles</a></p>
          <div class="blog-rail-meta-item"><span class="blog-rail-label">Updated</span> {upd_esc}</div>
        </div>
        <div class="article-rail__block">
          <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content"><h3>Quick Facts</h3><p>{desc_esc}</p></div></div>
        </div>
        <div class="article-rail__block article-rail__block--cta blog-rail-cta">
          <h3>Ready to get funded?</h3>
          <p>Get matched with lenders who fit your business.</p>
          <a href="/match.html" class="btn-primary">Get Matched for Business Financing</a>
        </div>

      </div></aside>"""


def build_right_rail(toc: list[tuple[str, str]]) -> str:
    if not toc:
        return """      <aside class="blog-post-rail-right article-rail article-rail--right"><div class="article-rail__inner article-rail__inner--toc"></div></aside>"""
    items = "".join(
        f'              <li><a href="#{html_module.escape(hid)}">{html_module.escape(title)}</a></li>\n'
        for hid, title in toc
    )
    return f"""      <aside class="blog-post-rail-right article-rail article-rail--right"><div class="article-rail__inner article-rail__inner--toc"><div class="blog-rail-toc">
          <h3>On this page</h3>
          <nav aria-label="On this page">
            <ul class="blog-post-toc-list">
{items}            </ul>
          </nav>
        </div></div></aside>"""


def related_section() -> str:
    return """
<section class="related-resources" aria-label="Related resources">
                <h2>Related resources</h2>
                <ul>
                    <li><a href="/contact.html">Contact Axiant Partners</a> for growth strategy and capital guidance</li>
                    <li><a href="/match.html">Get matched with lenders</a> when you are ready to fund a deliberate plan</li>
                    <li><a href="/business-growth.html">Business Growth hub</a></li>
                    <li><a href="../">All growth articles</a></li>
                    <li><a href="/blog.html">Blog</a></li>
                </ul>
<div class="services-cta">
                <a href="/match.html" class="btn-primary">Get Matched for Business Financing</a>
            </div>
      </section>"""


def build_json_ld(
    title: str,
    desc: str,
    slug: str,
    faqs: list[tuple[str, str]],
) -> str:
    canonical = f"{BASE_URL}/business-growth/articles/{slug}/"
    iso = f"{ARTICLE_DATE}T12:00:00-05:00"

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Business Growth",
                "item": f"{BASE_URL}/business-growth.html",
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": "Growth articles",
                "item": f"{BASE_URL}/business-growth/articles/",
            },
            {"@type": "ListItem", "position": 4, "name": title, "item": canonical},
        ],
    }

    blog = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "image": OG_IMAGE,
        "url": canonical,
        "datePublished": iso,
        "dateModified": iso,
        "author": {
            "@type": "Organization",
            "name": "Axiant Partners",
            "url": f"{BASE_URL}/",
        },
        "publisher": {
            "@type": "Organization",
            "name": "Axiant Partners LLC",
            "url": f"{BASE_URL}/",
            "logo": {
                "@type": "ImageObject",
                "url": f"{BASE_URL}/logo-horizontal-transparent.png",
            },
        },
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "articleSection": "Business Growth",
        "keywords": "business growth, small business, " + slug.replace("-", " "),
        "isAccessibleForFree": True,
        "audience": {
            "@type": "BusinessAudience",
            "audienceType": "Small and mid-size business owners and operators",
            "geographicArea": {"@type": "Country", "name": "United States"},
        },
        "about": [
            {"@type": "Thing", "name": "Business growth strategy"},
            {"@type": "Thing", "name": "Small business finance and operations"},
        ],
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["#quick-answer", "h1"],
        },
    }

    parts = [
        f'<script type="application/ld+json">{json.dumps(breadcrumb, ensure_ascii=False)}</script>',
        f'<script type="application/ld+json">{json.dumps(blog, ensure_ascii=False)}</script>',
    ]

    if faqs:
        faq_page = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ],
        }
        parts.append(
            f'<script type="application/ld+json">{json.dumps(faq_page, ensure_ascii=False)}</script>'
        )

    webpage = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": "Axiant Partners", "url": f"{BASE_URL}/"},
        "about": {"@type": "Thing", "name": "U.S. business growth and financing readiness"},
        "spatialCoverage": {"@type": "Country", "name": "United States"},
    }
    parts.append(
        f'<script type="application/ld+json">{json.dumps(webpage, ensure_ascii=False)}</script>'
    )

    return "\n".join(parts)


def main():
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    head_styles = HEAD_STYLES_PATH.read_text(encoding="utf-8")
    articles = load_batches()
    OUT.mkdir(parents=True, exist_ok=True)
    d = date.fromisoformat(ARTICLE_DATE)
    updated_display = f"{d.strftime('%B')} {d.day}, {d.year}"
    iso_full = f"{ARTICLE_DATE}T12:00:00-05:00"

    for a in articles:
        slug = a["slug"]
        folder = OUT / slug
        folder.mkdir(parents=True, exist_ok=True)
        body = a["html"].strip()
        supp = SUPP_DIR / f"{slug}.html"
        if supp.is_file():
            body = body + "\n" + supp.read_text(encoding="utf-8").strip()

        title = a["title"]
        desc = a["desc"]
        body = inject_quick_answer(body, desc)
        body, h1_title = remove_h1(body)
        header_title = h1_title or title
        body, toc = ensure_h2_ids_and_toc(body)
        body = body.strip() + "\n" + related_section()
        faqs = extract_operator_faqs(body)
        canonical = f"{BASE_URL}/business-growth/articles/{slug}/"
        jsonld = build_json_ld(title, desc, slug, faqs)

        head = HEAD_TOP.format(
            title_esc=html_module.escape(title),
            desc_esc=html_module.escape(desc),
            canonical=html_module.escape(canonical),
            og_image=html_module.escape(OG_IMAGE),
            iso_date=html_module.escape(iso_full),
        )
        head = head + head_styles + "\n" + jsonld

        left = build_left_rail(desc, updated_display)
        right = build_right_rail(toc)
        body_out = (
            BODY_OPEN.replace("__HEADER_H1__", html_module.escape(header_title))
            .replace("__TAGLINE__", html_module.escape(desc))
            .replace("__LEFT_RAIL__", left)
            .replace("__MAIN_INNER__", body)
            .replace("__RIGHT_RAIL__", right)
            .replace("__ASSET_Q__", ASSET_QUERY)
        )
        html = head + body_out
        (folder / "index.html").write_text(html, encoding="utf-8")
        print("wrote", slug)
    print("done", len(articles), "articles")


if __name__ == "__main__":
    main()
