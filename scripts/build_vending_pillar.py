#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build /vending-machine-financing.html, the money page for the vending cluster (AEO
plan 2a). Articles come from scripts/cluster_vending.py; the older spoke at
equipment-financing/articles/vending-machine-financing/ stays put and is listed too.

Same builder shape as build_heavy_equity_pillar.py: the visible FAQ and the FAQPage
JSON-LD come from one list, the HowTo from the steps the page shows, and the shared
header, footer and tracking tags from _components. Rebuilding re-dates the page, so
only rebuild for a real content change.

Content rules (see cluster_vending.py): ranges match what the site already publishes
(7-22% APR by credit tier, 24-60 month terms, machine costs from the vending spoke);
payments are arithmetic on a stated illustrative rate; no named-lender rates, no
funded totals, no testimonials. One entity: Axiant Partners, (561) 268-0465, Boca
Raton.

    python scripts/build_vending_pillar.py            # dry run: word count
    python scripts/build_vending_pillar.py --apply
"""
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import article_v2 as A  # noqa: E402
import cluster_vending as C  # noqa: E402

SLUG = "vending-machine-financing.html"
URL = f"{A.BASE}/{SLUG}"
TITLE = "Vending Machine Financing: Machines & Micro-Markets | Axiant"
H1 = "Vending Machine Financing"
META = ("Finance vending machines, micro-markets and route purchases as a business. "
        "Typical rates by credit tier, what lenders check, and how signed placements "
        "change the answer.")
OG_TITLE = "Vending Machine Financing for Operators | Axiant"
OG_DESC = ("Business financing for vending machines, micro-markets and route purchases: "
           "typical rates and terms, what lenders check, and how to structure it.")
HERO = "/assets/mca-retail-1200w.webp"

QUICK = ("According to Axiant Partners, a business-loan broker in Boca Raton, vending "
         "machines are financed as small-ticket business equipment: typically "
         "<strong>7-22% APR</strong> depending on credit, over <strong>24-60 "
         "months</strong>, with machines from about <strong>$3,000</strong> and "
         "micro-markets up to about $50,000. Signed location agreements carry as much "
         "weight as credit, because the placement is what pays the loan. Buying an "
         "existing route is financed as a business acquisition.")

SPEAKABLE = ("Vending machine financing is business equipment financing for snack, drink, "
             "smart and frozen machines, micro-markets and route purchases: lenders price "
             "it by credit tier and weigh the signed placements that will earn the "
             "payment.")

ICONS = {
    "cash": '<rect height="12" rx="2" width="19" x="2.5" y="6"></rect><circle cx="12" cy="12" r="2.6"></circle><path d="M6 10v4M18 10v4"></path>',
    "clock": '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5.2l3.2 1.9"></path>',
    "shield": '<path d="M12 3.2l7 3v5.9c0 4.1-2.9 7.8-7 8.7-4.1-.9-7-4.6-7-8.7V6.2l7-3Z"></path><path d="M9.2 12.1l2 2 3.6-3.8"></path>',
    "target": '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4.5"></circle><circle cx="12" cy="12" fill="currentColor" r="1.2" stroke="none"></circle>',
    "check": '<circle cx="12" cy="12" r="9"></circle><path d="M8.2 12.3l2.6 2.6 5-5.2"></path>',
}
STATS = [
    ("blue", "cash", "7-22% APR", "typical range, set mainly by credit tier"),
    ("teal", "clock", "24-60 mo", "typical term, matched to machine life"),
    ("indigo", "target", "$3K-$50K", "one machine to a full micro-market"),
    ("bronze", "shield", "Placements", "signed site agreements support approval"),
    ("rust", "check", "Used OK", "refurbished machines finance routinely"),
]

STEPS = [
    ("List what you are buying", "Machine types, new or refurbished, and the supplier's "
     "quote - or, for a route purchase, the asking price and what it includes."),
    ("Gather the placements", "Signed location or host agreements for where the machines "
     "will go, with their term and commission."),
    ("Pull your numbers", "Recent business bank statements and, if you already run "
     "machines, sales reports from telemetry or your card processor."),
    ("Compare the offers", "Rate or APR, term, down payment, total of payments and any "
     "buyout, side by side."),
    ("Close and place", "The lender pays the supplier (or the seller) and files its lien; "
     "you place the machines and start repaying."),
]

FAQS = [
    ("How do I finance vending machines?",
     "As business equipment: an equipment loan, a $1-buyout lease or an FMV lease, "
     "usually over 24 to 60 months. Bring the supplier's quote, recent bank statements "
     "and any signed location agreements. Buying an existing route is financed as a "
     "business acquisition instead."),
    ("What credit score do I need for vending machine financing?",
     "There is no single cut-off. Rates commonly run about 7-9% APR for 720+ credit "
     "with two-plus years in business and rise to around 22% with specialty lenders "
     "below about 640. Below 580, programs are limited and usually need a larger down "
     "payment."),
    ("Can I finance vending machines with no money down?",
     "Sometimes, for strong-credit operators with established placements. Newer "
     "operators and refurbished machines commonly need 10-20% down."),
    ("Can a new vending business get financing?",
     "Yes, but a signed location agreement matters more for a new operator than for "
     "anyone else, because it shows where the payment will come from. Expect a larger "
     "down payment and a shorter term."),
    ("Can I finance used or refurbished vending machines?",
     "Yes. Refurbished machines are common in vending and finance routinely, usually at "
     "a slightly higher rate and a shorter term than new."),
    ("Is it better to lease or buy vending machines?",
     "Buy for machines you will keep in stable placements; consider an FMV lease when "
     "you want the option to return or upgrade units. Compare pay-later and lease-to-own "
     "checkout offers on total of payments, not the monthly figure."),
    ("Can I finance a micro-market?",
     "Yes. The kiosk, coolers, shelving and cameras are usually financed as one package. "
     "Lenders weigh the host agreement heavily, ideally with a term at least as long as "
     "the loan."),
    ("Can I get a loan to buy an existing vending route?",
     "Yes. Routes are financed as small business acquisitions: SBA 7(a), which requires "
     "at least a 10% equity injection for a change of ownership, or an equipment loan "
     "on the machines plus a seller note."),
]

FDA_VEND = C.FDA_VEND
SMART_SNACKS = ("https://www.ecfr.gov/current/title-7/subtitle-B/chapter-II/subchapter-A/part-210/section-210.11",
                "7 CFR 210.11: Competitive Food Service and Standards (Smart Snacks in School)",
                "USDA nutrition standards for food and drinks sold to students during the "
                "school day, including from vending machines.")
RANDOLPH_SHEPPARD = ("https://www.law.cornell.edu/uscode/text/20/107",
                     "20 U.S.C. &sect; 107: Randolph-Sheppard Act",
                     "The priority for licensed blind vendors to operate vending facilities "
                     "on federal property.")
SOURCES = [FDA_VEND, SMART_SNACKS, RANDOLPH_SHEPPARD, C.TILA_EXEMPT, C.IRS_946, C.UCC_9310]


def section(tone, alt, h2, body):
    sid = A.slugify(re.sub(r"<[^>]+>", "", h2))
    cls = "section section-alt" if alt else "section"
    return (f'<section class="{cls}">\n<div class="container">\n<div class="group" data-tone="{tone}">\n'
            f'<div class="prose">\n<h2 id="{sid}">{h2}</h2>\n{body}\n</div>\n</div>\n</div>\n</section>')


def midcta(text, label):
    return (f'<div class="ef-midcta">\n<p>{text}</p>\n'
            f'<a class="btn btn-primary" href="/match.html">{label}</a>\n</div>')


def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    # .table-wrap is the v2 table component (borders, striping, scrolls inside its own box
    # on phones). The older ba-table classes on other money pages have no CSS at all.
    return f'<div class="table-wrap">\n<table>\n<thead><tr>{th}</tr></thead>\n<tbody>{tb}</tbody>\n</table>\n</div>'


H = "/vending-machine-financing/articles"
SPOKE = "/equipment-financing/articles/vending-machine-financing/"

SECTIONS = [
    ("What Vending Operators Finance",
     "<p>Vending financing covers more than single machines. The four things operators "
     "most often finance, and how each is usually handled:</p>"
     + table(["What", "Typical cost", "Usually financed as"], [
         # first-column cells do not wrap in the v2 mobile card layout: keep them short
         ["Snack or drink machine", "$3K-$7K", "Equipment loan or lease"],
         ["Smart machine", "$5K-$12K", "Equipment loan or lease"],
         ["Batch for new placements", "Varies", "One package, or a line drawn per placement"],
         ["Micro-market", "$15K-$50K", "One equipment package"],
         ["Existing route", "Price of the business", "Business acquisition (SBA 7(a), seller note)"],
     ])
     + f"<p>Illustrative ranges, not quotes. Machine-by-machine costs are in our guide to "
     f"<a href=\"{SPOKE}\">vending machine costs and route expansion</a>.</p>"),
    ("Typical Rates and Terms",
     "<p>Lenders price vending machines like any small-ticket equipment, so the main "
     "lever is credit tier. Ranges commonly seen across lenders:</p>"
     + table(["Credit tier", "Typical APR", "Typical term", "Down payment"], [
         ["720+, 2+ yrs", "7-9%", "Up to 60 mo", "0-10%"],
         ["680-719", "10-13%", "36-60 mo", "0-10%"],
         ["640-679", "13-16%", "36-60 mo", "10-20%"],
         ["580-639", "16-22%", "24-48 mo", "15-25%"],
     ])
     + "<p>Refurbished machines commonly add one to three points, and small tickets "
     "price a little above large ones. Business-purpose credit is exempt from federal "
     "Truth in Lending disclosures, so ask every lender for the APR and the total of "
     "payments. More in <a href=\"" + H + "/typical-vending-machine-financing-rates-2026/\">"
     "typical vending machine financing rates</a>.</p>"
     + midcta("<strong>Have a supplier quote?</strong> Send it with your placements and "
              "get real terms back, not a range.", "Check My Options")),
    ("The Placement Is What Gets Approved",
     "<p>A single vending machine is cheap collateral and easy to move, which is why "
     "lenders look past it to the place it will earn. What they weigh:</p>"
     "<ul>"
     "<li><strong>Signed location agreements</strong> - an office, plant, gym, hospital "
     "or school that has agreed to host the machine, with the term and commission in "
     "writing.</li>"
     "<li><strong>Sales history</strong> - for existing operators, telemetry or "
     "card-reader reports per machine. It is the closest thing vending has to an income "
     "statement for one asset.</li>"
     "<li><strong>Deposits that match</strong> - vending still takes cash, so bank "
     "deposits should line up with the sales you report.</li>"
     "<li><strong>Credit and time in business</strong> - the usual "
     "<a href=\"/equipment-financing/articles/equipment-financing-requirements/\">equipment "
     "financing requirements</a>, applied to small tickets.</li>"
     "</ul>"
     "<p>For a new operator, one signed placement can do more than a higher credit score. "
     "Thin or damaged files can review <a href=\"/equipment-financing/articles/equipment-financing-bad-credit/\">"
     "equipment financing with bad credit</a>.</p>"),
    ("Rules That Change What a Location Is Worth",
     "<p>Three federal rules decide what you can sell, and where. Lenders rarely ask "
     "about them, but they change how much a placement will earn:</p>"
     "<ul>"
     "<li><strong>Calorie labeling at 20 machines.</strong> FDA requires operators who "
     "own or operate 20 or more food vending machines to show calories where buyers "
     "cannot see the Nutrition Facts label before purchase. Growing past 20 machines "
     "adds a compliance cost to plan for.</li>"
     "<li><strong>Schools.</strong> Food and drinks sold to students during the school "
     "day, including from vending machines, must meet USDA's Smart Snacks standards. A "
     "school placement earns on a narrower product list.</li>"
     "<li><strong>Federal buildings.</strong> Under the Randolph-Sheppard Act, licensed "
     "blind vendors have priority to operate vending facilities on federal property. A "
     "federal site may not be open to you at all.</li>"
     "</ul>"
     "<p>None of these stops a deal. They are worth knowing before you build a "
     "financing plan around a specific placement.</p>"),
    ("A Worked Example",
     "<p>Illustrative arithmetic, not a quote. An operator has signed eight new "
     "placements and finances a mix of new and refurbished machines to fill them:</p>"
     + table(["Item", "Figure"], [
         ["Eight machines", "$30,000"],
         ["Term", "48 months"],
         ["Illustrative rate", "11% APR"],
         ["Monthly payment", "About $775"],
         ["Per machine", "About $97 a month"],
     ])
     + "<p>The test is per placement: each machine has to clear about $97 a month after "
     "product cost and the location's commission. A placement that cannot is a reason "
     "to move the machine, not a reason to borrow more.</p>"
     + midcta("<strong>Signed new locations?</strong> Finance the machines to fill them "
              "without tying up the cash that buys product.", "Get Matched")),
    ("Loan, Lease or Pay-Later Checkout?",
     table(["Option", "You get", "Fits best"], [
         ["<strong>Equipment loan</strong>", "Ownership from day one; lien until paid", "Machines you will keep"],
         ["<strong>$1-buyout lease</strong>", "Ownership at the end", "Buying, with lease terms"],
         ["<strong>FMV lease</strong>", "Use, with the option to return or upgrade", "Testing new sites or models"],
         ["<strong>Pay-later checkout</strong>", "Fast approval on a supplier's site", "One small, urgent machine"],
     ])
     + "<p>Machines move between locations more than most equipment, which makes "
     "ownership - or a lease that lets you hand back the wrong model - more valuable "
     "than usual. Checkout offers are quick but can cost the most in total. See "
     "<a href=\"" + H + "/vending-machine-lease-vs-loan/\">vending machine lease vs loan vs "
     "pay-later</a>.</p>"),
    ("Micro-Markets and Buying a Route",
     "<p><strong>Micro-markets</strong> - open shelving, coolers and a self-checkout "
     "kiosk in a workplace - are financed as one equipment package. Much of the cost is "
     "installation and fixtures with little resale value, so lenders lean on the host "
     "agreement and want its term to cover the loan. See "
     "<a href=\"" + H + "/micro-market-financing/\">micro-market financing</a>.</p>"
     "<p><strong>Buying an existing route</strong> is a business acquisition: you are "
     "paying for placements and cash flow as well as machines. SBA 7(a) loans are the "
     "usual tool when the price includes real goodwill, and SBA requires at least a 10% "
     "equity injection for a change of ownership. See "
     "<a href=\"" + H + "/buying-a-vending-route/\">how to finance buying a vending "
     "route</a> and <a href=\"/business-acquisition-financing.html\">business acquisition "
     "financing</a>.</p>"),
    ("When Financing Is the Wrong Move",
     "<ul>"
     "<li><strong>No placement yet.</strong> Machines in a storage unit earn nothing and "
     "the payment starts anyway. Sign the location first.</li>"
     "<li><strong>The gap is inventory, not machines.</strong> Product, fuel and repairs "
     "between collections are a <a href=\"/working-capital-loans.html\">working "
     "capital</a> question; an equipment loan pays for machines.</li>"
     "<li><strong>The machine underperforms where it is.</strong> Move it before "
     "financing another for the same site.</li>"
     "<li><strong>A checkout offer you have not priced.</strong> Compare its total of "
     "payments with an equipment loan first.</li>"
     "</ul>"),
    ("What You Will Need to Apply",
     "<ul>"
     "<li>The supplier's quote: machine types, new or refurbished, and price</li>"
     "<li>Signed location or host agreements, where you have them</li>"
     "<li>Recent business bank statements, typically the last three to six months</li>"
     "<li>Sales reports from telemetry or your card processor, if you run machines now</li>"
     "<li>For a route purchase: the seller's sales records, location agreements and a "
     "list of the machines with serial numbers</li>"
     "</ul>"
     + midcta("<strong>Have the quote and placements?</strong> One application, real "
              "offers, and checking won't affect your credit.", "Get Matched")),
    ("What Happens After You Apply",
     "<ol>" + "".join(f"<li><strong>{n}.</strong> {t}</li>" for n, t in STEPS) + "</ol>"
     "<p>Vending machines have no title, so the lender records its lien with a UCC-1 "
     "filing and releases it when the loan is paid. Financed machines can still qualify "
     "for depreciation and Section 179 in the year they are placed in service; see "
     "IRS Publication 946 and your accountant.</p>"),
]


def build():
    v, header, footer = A.chrome()
    today = A.TODAY.isoformat()
    tones = A.TONES
    body_sections = "\n".join(section(tones[i % len(tones)], i % 2 == 0, h, b)
                              for i, (h, b) in enumerate(SECTIONS))
    stats = "\n".join(
        f'<div class="stat" data-tone="{tone}"><span class="stat-icon"><svg aria-hidden="true" fill="none" '
        f'stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" '
        f'viewbox="0 0 24 24">{ICONS[icon]}</svg></span><span class="stat-body"><span class="stat-key">{k}</span>'
        f'<span class="stat-label">{lbl}</span></span></div>'
        for tone, icon, k, lbl in STATS)
    faq_html = "\n".join(f"<h3>{html.escape(q)}</h3>\n<p>{a}</p>" for q, a in FAQS)
    sources = "\n".join(
        f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{n}</a> &mdash; {d}</li>'
        for u, n, d in SOURCES)
    guides = "\n".join(
        f'<li><strong><a href="/{C.CLUSTER["hub"]}/{a["slug"]}/">{html.escape(a["og_title"])}</a></strong> '
        f'&mdash; {html.escape(a["lede"])}.</li>' for a in C.ARTICLES)
    # the older spoke stays where Google already ranks it; list it with the cluster
    guides += (f'\n<li><strong><a href="{SPOKE}">Vending Machine Costs and Route Expansion</a></strong> '
               '&mdash; what each type of machine costs and how operators finance batches for new placements.</li>')

    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{A.BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Equipment Financing", "item": f"{A.BASE}/equipment-financing.html"},
            {"@type": "ListItem", "position": 3, "name": H1, "item": URL}]},
        {"@context": "https://schema.org", "@type": "FinancialService",
         "name": "Vending Machine Financing",
         "description": "Business-purpose financing for vending machines, smart machines, "
                        "micro-markets and the purchase of existing vending routes.",
         "url": URL, "provider": {"@id": f"{A.BASE}/#organization"}, "areaServed": "US"},
        {"@context": "https://schema.org", "@type": "WebPage", "@id": f"{URL}#webpage", "url": URL,
         "name": "Vending Machine Financing: Machines, Micro-Markets and Route Purchases",
         "datePublished": today, "dateModified": today,
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".quick-answer", ".ef-speakable"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQS]},
        {"@context": "https://schema.org", "@type": "HowTo",
         "name": "How to finance vending machines",
         "description": "Steps to finance vending machines, a micro-market or a route purchase.",
         "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t}
                  for i, (n, t) in enumerate(STEPS)]},
        {"@context": "https://schema.org", "@type": "Organization", "@id": f"{A.BASE}/#organization",
         "name": "Axiant Partners", "url": f"{A.BASE}/",
         "logo": {"@type": "ImageObject", "url": f"{A.BASE}/logo-horizontal-transparent.png"},
         "telephone": "+1-561-268-0465",
         "address": {"@type": "PostalAddress", "addressLocality": "Boca Raton", "addressRegion": "FL",
                     "addressCountry": "US"},
         "areaServed": {"@type": "Country", "name": "United States"}},
    ]
    ld_html = "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(x, separators=(",", ":"))
                        for x in ld)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
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
<meta content="{today}" property="article:modified_time"/>
<meta content="{html.escape(META)}" name="description"/>
<meta content="index, follow, max-snippet:-1, max-image-preview:large" name="robots"/>
<link href="{URL}" rel="canonical"/>
<meta content="en_US" property="og:locale"/>
<meta content="{html.escape(OG_TITLE)}" property="og:title"/>
<meta content="{html.escape(OG_DESC)}" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="{URL}" property="og:url"/>
<meta content="{A.BASE}{HERO}" property="og:image"/>
<meta content="Axiant Partners" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{A.BASE}{HERO}" name="twitter:image"/>
<meta content="{html.escape(OG_TITLE)}" name="twitter:title"/>
<meta content="{html.escape(OG_DESC)}" name="twitter:description"/>
<title>{html.escape(TITLE)}</title>
<link href="/favicon.webp" rel="icon" sizes="48x48" type="image/webp"/><link href="/favicon.png" rel="icon" sizes="48x48" type="image/png"/><link href="/favicon.png" rel="apple-touch-icon"/>
<link as="image" href="{HERO}" rel="preload" type="image/webp"/>
{ld_html}
<meta content="Axiant Partners" name="author"/>
<link href="/axiant-v2.css?v={v}" rel="stylesheet"/>
{A.tracking_tags()}
</head>
<body>{header}

<section class="hero-compact">
<div class="hero-media"><img alt="" decoding="async" fetchpriority="high" height="669" src="{HERO}" width="1200"/></div>
<div class="container">
<div class="inner">
<p class="eyebrow">Financing program</p>
<h1>{H1}</h1>
<p class="lede">Finance snack, drink and smart machines, micro-markets and route purchases, and keep your cash for product and the next placement.</p>
<ul class="hero-checks">
<li><span class="tick">✓</span><span>Business-purpose only</span></li>
<li><span class="tick">✓</span><span>New and refurbished machines</span></li>
<li><span class="tick">✓</span><span>Single machines, batches or a full micro-market</span></li>
<li><span class="tick">✓</span><span>Signed placements count, not just credit</span></li>
</ul>
<div class="actions">
<a class="btn btn-primary btn-lg" href="/match.html">See My Vending Options</a>
<span class="call">Or call <a href="tel:+15612680465">(561) 268-0465</a></span>
</div>
</div>
</div>
</section>
<section class="section section-tight">
<div class="container">
<p class="dateline">Updated {A._dateline()}</p>
<div class="callout quick-answer" id="quick-answer">
<p class="eyebrow">Quick answer</p>
<p>{QUICK}</p>
<p><a href="/match.html">Get matched for vending machine financing →</a></p>
</div>
<nav aria-label="Breadcrumb" class="ef-breadcrumb">
<ol>
<li><a href="/">Home</a></li>
<li><a href="/equipment-financing.html">Equipment Financing</a></li>
<li><span aria-current="page">{H1}</span></li>
</ol>
</nav>
</div>
</section>
<section class="section">
<div class="container">
<div class="group" data-tone="blue">
<div class="prose">
<p class="ef-speakable"><strong>{SPEAKABLE}</strong></p>
</div>
</div>
</div>
</section>
<section class="section section-alt">
<div class="container">
<div class="group" data-tone="indigo">
<div class="group-head"><h2 id="vending-machine-financing-at-a-glance">Vending Machine Financing at a Glance</h2></div>
<div class="stats">
{stats}
</div>
<p style="margin-top:12px;font-size:.9rem">Typical ranges across lenders, not a quote. Your figures depend on the machines, the placements and the business.</p>
</div>
</div>
</section>
{body_sections}
<section class="about-section" id="faq">
<div class="container">
<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>
<ul>
{sources}
</ul>
<p>Figures above describe ranges commonly seen across lenders and reflect published guidance as of the date on this page. Confirm current terms with the cited source or your lender before acting.</p>
<h2 id="vending-machine-financing-faqs">Vending Machine Financing FAQs</h2>
{faq_html}
</div>
</section>
<section class="section section-alt">
<div class="container">
<div class="group" data-tone="bronze">
<div class="prose">
<h2 id="cluster-guides">Vending Machine Financing Guides</h2>
<p>{html.escape(C.CLUSTER["hub_lede"])}. <a href="/{C.CLUSTER["hub"]}/">See all {len(C.ARTICLES)} guides</a>.</p>
<ul>
{guides}
</ul>
</div>
</div>
</div>
</section>
<section class="section">
<div class="container">
<div class="group" data-tone="rust">
<div class="prose">
<h2 id="get-matched-for-vending-financing">Get Matched for Vending Financing</h2>
<p>Tell us what you are buying and where it will go. Axiant compares loans, leases and, for a route, acquisition financing side by side, so you can pick the structure that costs least for the placements you have. One application, real offers, no obligation, and checking won't affect your credit.</p>
<div class="cta-actions">
<a class="btn btn-primary" href="/match.html">Get Matched</a>
<a class="btn btn-secondary" href="tel:+15612680465">Call (561) 268-0465</a>
</div>
</div>
</div>
</div>
</section>

{footer}
<script src="/script.js?v={A.script_version()}" defer></script>
</body>
</html>
"""


def main(apply):
    out = build()
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", out, flags=re.S)).split())
    qa_words = len(re.sub(r"<[^>]+>", " ", QUICK).split())
    print(f"{SLUG}: {words} words, quick answer {qa_words} words, title {len(TITLE)} chars, "
          f"{len(FAQS)} faqs, {len(STEPS)} steps")
    if apply:
        io.open(os.path.join(A.ROOT, SLUG), "w", encoding="utf-8", newline="").write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
