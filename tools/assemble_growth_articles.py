# -*- coding: utf-8 -*-
"""Emit business-growth/articles/*/index.html from batch modules (SEO, AEO, GEO-ready)."""
from __future__ import annotations

import html as html_module
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "business-growth" / "articles"
TOOLS = pathlib.Path(__file__).resolve().parent
SUPP_DIR = TOOLS / "article_supplements"

BASE_URL = "https://axiantpartners.com"
ARTICLE_DATE = "2026-04-09"

WRAPPER = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Axiant Partners</title>
<meta name="description" content="{desc_esc}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0d1f3c">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="og:title" content="{title_esc} | Axiant Partners">
<meta property="og:description" content="{desc_esc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Axiant Partners">
<meta property="article:published_time" content="{iso_date}">
<meta property="article:modified_time" content="{iso_date}">
<meta property="article:section" content="Business Growth">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_esc} | Axiant Partners">
<meta name="twitter:description" content="{desc_esc}">
{jsonld}
<style>.article-quick-answer{{margin:1rem 0 1.25rem;padding:1rem 1.1rem;border-left:4px solid #2d7fb8;background:var(--bg-card, #f0f4f8);border-radius:0 8px 8px 0;font-size:1.02rem;line-height:1.55}}[data-theme="dark"] .article-quick-answer{{background:#1e293b;border-left-color:#60a5fa}}</style>
<link rel="stylesheet" href="../../../critical.css?v=2026032199"><link rel="stylesheet" href="../../../styles.css?v=2026032199">
</head>
<body><div class="container form-container blog-post-content growth-article-content">
{body}
<p style="margin-top:2rem;"><strong>Next steps:</strong> <a href="/contact.html">Contact Axiant Partners</a> for growth strategy and capital guidance, or <a href="/match.html">get matched with lenders</a> when you are ready to fund a deliberate plan.</p>
<p><a href="/business-growth.html">Business Growth hub</a> · <a href="/business-growth/articles/">All growth articles</a> · <a href="/blog.html">Blog</a></p>
</div></body></html>
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


def extract_operator_faqs(html: str) -> list[tuple[str, str]]:
    start = html.find("<h2>Operator FAQ</h2>")
    if start < 0:
        return []
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

    # WebPage for GEO / entity clarity (complements BlogPosting)
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
    articles = load_batches()
    OUT.mkdir(parents=True, exist_ok=True)
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
        faqs = extract_operator_faqs(body)
        canonical = f"{BASE_URL}/business-growth/articles/{slug}/"
        jsonld = build_json_ld(title, desc, slug, faqs)

        html = WRAPPER.format(
            title=title,
            title_esc=html_module.escape(title),
            desc_esc=html_module.escape(desc),
            slug=slug,
            canonical=canonical,
            iso_date=f"{ARTICLE_DATE}T12:00:00-05:00",
            jsonld=jsonld,
            body=body,
        )
        (folder / "index.html").write_text(html, encoding="utf-8")
        print("wrote", slug)
    print("done", len(articles), "articles")


if __name__ == "__main__":
    main()
