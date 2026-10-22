#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build /heavy-equipment-equity-loan.html, the money page for the heavy equipment
equity cluster (AEO plan 2b). Articles come from scripts/cluster_heavy_equity.py.

Why a builder rather than a hand-written page: the visible FAQ and the FAQPage
JSON-LD are generated from one list, the HowTo from the same steps the page shows,
and the shared header, footer and tracking tags come from _components, so the page
can be rebuilt without drift. Rebuilding re-dates it, so only rebuild for a real
content change.

Content rules (same as the truck title cluster): ranges are conventional across
lenders and match what the site already publishes (roughly 50-80% of forced
liquidation value, 24-72 month terms); no named-lender rates, no funded totals, no
testimonials. One entity: Axiant Partners, (561) 268-0465, Boca Raton.

    python scripts/build_heavy_equity_pillar.py            # dry run: word count
    python scripts/build_heavy_equity_pillar.py --apply
"""
import html
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import article_v2 as A  # noqa: E402
import cluster_heavy_equity as C  # noqa: E402

SLUG = "heavy-equipment-equity-loan.html"
URL = f"{A.BASE}/{SLUG}"
TITLE = "Heavy Equipment Equity Loan: Cash From Iron You Own | Axiant"
H1 = "Heavy Equipment Equity Loan"
META = ("Borrow against excavators, loaders and dozers you already own. Lenders file "
        "a UCC-1, not a title, and advance a share of liquidation value. What "
        "qualifies and how much you can raise.")
OG_TITLE = "Heavy Equipment Equity Loan: Borrow Against Machines You Own | Axiant"
OG_DESC = ("Raise working capital against construction equipment you own and keep it "
           "working. What qualifies, how the lien works, and how much you can raise.")
HERO = "/assets/bulldozer-hero-bg.webp"

QUICK = ("According to Axiant Partners, a business-loan broker in Boca Raton, a heavy "
         "equipment equity loan is business-purpose financing secured by excavators, "
         "loaders, dozers or other construction machines you already own. Lenders "
         "typically advance <strong>50-80% of forced liquidation value</strong> over "
         "<strong>24-72 months</strong>, and because most yellow iron has no title, "
         "they file a <strong>UCC-1 lien</strong> instead of a title lien. You keep "
         "the machines working while you repay.")

SPEAKABLE = ("A heavy equipment equity loan is business-purpose financing secured by "
             "construction equipment you already own: the lender files a UCC-1 lien and "
             "advances a share of the machines' liquidation value, while you keep them "
             "on the job.")

ICONS = {
    "cash": '<rect height="12" rx="2" width="19" x="2.5" y="6"></rect><circle cx="12" cy="12" r="2.6"></circle><path d="M6 10v4M18 10v4"></path>',
    "clock": '<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5.2l3.2 1.9"></path>',
    "shield": '<path d="M12 3.2l7 3v5.9c0 4.1-2.9 7.8-7 8.7-4.1-.9-7-4.6-7-8.7V6.2l7-3Z"></path><path d="M9.2 12.1l2 2 3.6-3.8"></path>',
    "target": '<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4.5"></circle><circle cx="12" cy="12" fill="currentColor" r="1.2" stroke="none"></circle>',
    "check": '<circle cx="12" cy="12" r="9"></circle><path d="M8.2 12.3l2.6 2.6 5-5.2"></path>',
}
STATS = [
    ("blue", "cash", "50-80%", "of forced liquidation value, typical advance"),
    ("teal", "clock", "24-72 mo", "typical repayment term"),
    ("indigo", "shield", "UCC-1", "lien filing, not a title"),
    ("bronze", "target", "$25K+", "where the most lenders compete"),
    ("rust", "check", "Keep working", "machines stay on your jobsite"),
]

STEPS = [
    ("List the machines", "Make, model, year, serial number, hours and photos of each "
     "machine you want to borrow against, plus any service records."),
    ("Check the liens", "Note anything still owed and get payoff letters; know whether "
     "a bank, SBA lender or advance provider has a blanket UCC filing on the business."),
    ("Get a valuation", "A desktop valuation from photos and serials, or an on-site "
     "appraisal for larger amounts, establishes liquidation value."),
    ("Review the offer", "Advance amount, term, payment and any fees, stated against the "
     "valuation they come from."),
    ("Close and fund", "The lender files its UCC-1 (and pays off any existing lender), "
     "then funds. The machines never leave your jobsite."),
]

FAQS = [
    ("What is a heavy equipment equity loan?",
     "Business-purpose financing secured by construction equipment you already own, "
     "such as excavators, loaders and dozers. The lender files a lien and advances a "
     "share of the machines' liquidation value; you keep using them while you repay."),
    ("Can I get a title loan on my excavator?",
     "Not in the car-title sense. Most excavators, dozers and loaders are not covered by "
     "a state title statute, so there is no title to hold a lien. Lenders secure the "
     "loan by filing a UCC-1 financing statement instead. The effect is similar: you "
     "borrow against the machine and keep using it."),
    ("How much can I borrow against my construction equipment?",
     "A share of what the machines would bring at a quick sale. Lenders commonly advance "
     "roughly 50-80% of forced liquidation value, less anything still owed. Hours, "
     "undercarriage condition, brand, emissions tier and service records move the "
     "valuation."),
    ("Do I need to own the equipment free and clear?",
     "No, but you need real equity. If a machine still has a loan on it, the usual "
     "structure is a cash-out refinance that pays off the existing lender and advances "
     "the rest. If you owe close to what it would sell for, there is nothing to draw."),
    ("How long are the terms?",
     "Equity loans against equipment commonly run 24 to 72 months with fixed monthly "
     "payments, depending on the age of the machines and the amount."),
    ("Can I get one with bad credit?",
     "Often, because the loan is secured by equipment a lender can value and recover. "
     "Credit still affects the amount and the price, and an open bankruptcy, unresolved "
     "tax liens or disputed ownership can stop a deal regardless of score."),
    ("What equipment qualifies?",
     "Construction machines with an active resale market: excavators and mini "
     "excavators, wheel and track loaders, dozers, skid steers, backhoes, motor graders, "
     "compactors, cranes and similar. Titled units such as dump trucks and lowboy "
     "trailers also qualify but are handled through their titles."),
    ("How is this different from a sale-leaseback?",
     "An equity loan keeps the machine in your name with a lien against it. A "
     "sale-leaseback sells the machine to a lessor and leases it back, which can raise "
     "more cash but gives up ownership and can trigger tax on the sale."),
]

SOURCES = [C.UCC_9310, C.UCC_9311, C.ASA, C.IRS_946]


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


SECTIONS = [
    ("There Is No Title on Most Yellow Iron",
     "<p>People search for a <strong>title loan on an excavator</strong> because that is "
     "how a truck works. Construction equipment mostly does not. A dump truck or a lowboy "
     "trailer has a state title, and a lender notes its lien on it. An excavator, dozer or "
     "wheel loader generally does not, because off-road machines are not covered by state "
     "certificate-of-title statutes.</p>"
     + table(["Equipment", "Titled?", "How the lender records its lien"], [
         # first-column cells do not wrap in the v2 mobile card layout: keep them short
         ["Dump &amp; service trucks", "Yes", "On the title (see <a href=\"/commercial-truck-title-loan.html\">truck title loans</a>)"],
         ["Lowboy trailers", "Yes", "On the title"],
         ["Excavators, dozers", "Generally no", "UCC-1 financing statement"],
         ["Loaders, skid steers", "Generally no", "UCC-1 financing statement"],
         ["Cranes, graders, backhoes", "Generally no", "UCC-1 financing statement"],
     ])
     + "<p>The practical result is the same: you borrow against the machine and keep using "
     "it. The difference shows up in the paperwork - the lender searches and files with the "
     "secretary of state rather than the DMV - and in the most common surprise, a "
     "<strong>blanket UCC lien</strong> from another lender that already covers every "
     "machine you own.</p>"),
    ("How a Heavy Equipment Equity Loan Works",
     "<ul>"
     "<li><strong>The machines are valued.</strong> From make, model, year, hours, "
     "condition and recent auction results - a liquidation figure, not a dealer's price.</li>"
     "<li><strong>The lender advances a share of that value.</strong> Commonly in the "
     "range of 50-80% of forced liquidation value, sized so it stays covered if it ever "
     "has to sell.</li>"
     "<li><strong>A UCC-1 is filed</strong> describing the machines by serial number. "
     "Any existing lender is paid off or agrees to its position.</li>"
     "<li><strong>You keep working.</strong> The equipment stays on your jobsites. "
     "Lenders generally require insurance naming them as loss payee, and some require "
     "GPS or telematics.</li>"
     "<li><strong>You repay over a term</strong> - commonly 24 to 72 months - in fixed "
     "monthly payments, and the lien is released when the loan is paid.</li>"
     "</ul>"
     + midcta("<strong>Not sure what your machines support?</strong> Send the make, model, "
              "year and hours and get a real number back instead of a guess.",
              "Check My Equipment")),
    ("What Equipment Qualifies",
     "<p>Lenders want machines with an active resale market, because the resale market "
     "is what they are really lending against:</p>"
     "<ul>"
     "<li><strong>Excavators and mini excavators</strong> - see "
     "<a href=\"/equipment/excavators/\">excavator financing</a> for what they cost new.</li>"
     "<li><strong>Wheel loaders, track loaders and skid steers</strong></li>"
     "<li><strong>Dozers</strong> and <strong>motor graders</strong></li>"
     "<li><strong>Backhoes, compactors and telehandlers</strong></li>"
     "<li><strong>Cranes</strong> and other specialised lifting equipment, case by case</li>"
     "</ul>"
     "<p><strong>What usually stops a deal:</strong> unclear ownership or a machine titled "
     "to someone other than the business; a blanket lien that will not be released or "
     "subordinated; very high hours with no records; a niche machine with too few buyers; "
     "or an open bankruptcy or large unresolved tax lien.</p>"),
    ("How Much Can You Raise?",
     "<p>The figure comes from the machine, then the business:</p>"
     "<ul>"
     "<li><strong>Hours</strong> - the yellow-iron equivalent of mileage, and the biggest "
     "single lever.</li>"
     "<li><strong>Undercarriage</strong> - on tracked machines, remaining track and "
     "roller life comes straight off or onto the value.</li>"
     "<li><strong>Brand and dealer support</strong> - a deeper buyer pool means a higher "
     "and faster recovery.</li>"
     "<li><strong>Emissions tier</strong> - older engines can have fewer buyers, "
     "particularly where California's off-road diesel rules apply.</li>"
     "<li><strong>What is still owed</strong> - comes off the top.</li>"
     "<li><strong>Your cash flow</strong> - decides how large a payment the business can "
     "carry, even when the collateral supports more.</li>"
     "</ul>"
     "<p>Our guide to <a href=\"/heavy-equipment-equity-loan/articles/what-your-excavator-is-worth-to-a-lender/\">"
     "what your excavator is worth to a lender</a> walks through each one, and "
     "<a href=\"/equipment-appraisal.html\">equipment appraisal</a> explains the "
     "valuation itself.</p>"),
    ("A Worked Example",
     "<p>Illustrative arithmetic, not a quote. A contractor owns two machines outright "
     "and has a third with a loan on it:</p>"
     + table(["Machine", "Forced liquidation value", "Owed", "At 65% of FLV, less payoff"], [
         ["Mid-size excavator", "$96,000", "$0", "$62,400"],
         ["Wheel loader", "$70,000", "$0", "$45,500"],
         ["Dozer", "$80,000", "$38,000", "$14,000"],
         ["<strong>Total</strong>", "<strong>$246,000</strong>", "<strong>$38,000</strong>", "<strong>$121,900</strong>"],
     ])
     + "<p>Pledging all three raises more than any one alone, and the dozer's existing "
     "loan is paid off at closing. At an illustrative 12% APR over 48 months, $121,900 "
     "works out to roughly $3,200 a month - the number to test against your slowest "
     "months, not your best.</p>"
     + midcta("<strong>Own several machines?</strong> Pledging more than one usually "
              "means a better structure on the whole package.",
              "See What My Fleet Supports")),
    ("Equity Loan, Refinance, Sale-Leaseback or Sell?",
     "<p>If the goal is cash and you own the equipment, four structures compete:</p>"
     + table(["Option", "You keep / you raise", "Best when"], [
         ["<strong>Equity loan</strong>", "Keep the machine and ownership; raise a share of liquidation value; loan payment", "You own it clear"],
         ["<strong>Cash-out refinance</strong>", "Keep the machine and ownership; raise a share of value less the payoff; loan payment", "You still owe, with real equity"],
         ["<strong>Sale-leaseback</strong>", "Keep using it, give up ownership (usually with a buyout); often raises more; lease payment", "You need the maximum cash"],
         ["<strong>Sell it</strong>", "Give up the machine; raise the full sale price; no payment", "The machine sits idle"],
     ])
     + "<p>The one owners overlook is the last column. A machine that sits more than it "
     "works is often worth more sold than borrowed against. See "
     "<a href=\"/heavy-equipment-equity-loan/articles/equipment-equity-loan-vs-sale-leaseback/\">"
     "equity loan vs sale-leaseback</a> and "
     "<a href=\"/equipment-financing/articles/equipment-refinancing/\">equipment "
     "refinancing</a> for the detail.</p>"),
    ("When It Makes Sense, and When It Does Not",
     "<p><strong>It tends to make sense when:</strong> you own machines with real equity "
     "and need capital for something that earns - a bigger job, a new crew, a down "
     "payment on another machine; you are bridging slow progress payments on a contract "
     "you have already won; or you are replacing expensive short-term debt such as "
     "<a href=\"/mca-consolidation-loan.html\">stacked merchant cash advances</a> with one "
     "secured payment.</p>"
     "<p><strong>It tends not to make sense when:</strong> the equipment is the business's "
     "only asset and revenue is already unstable; the need is small and short enough that "
     "a <a href=\"/business-line-of-credit.html\">line of credit</a> would serve better; "
     "or the shortfall will recur next month regardless. Adding a secured payment to an "
     "operation that cannot carry its current payments makes the problem worse.</p>"
     "<p>Compared with an advance, see "
     "<a href=\"/heavy-equipment-equity-loan/articles/equipment-equity-loan-vs-mca/\">"
     "equity loan vs MCA</a>.</p>"),
    ("What You Will Need to Apply",
     "<ul>"
     "<li>A list of the machines: make, model, year, serial number and hours</li>"
     "<li>Photos of each - hour meter, serial plate, undercarriage, attachments, cab</li>"
     "<li>Service records where you have them</li>"
     "<li>Payoff letters for anything still financed</li>"
     "<li>Proof of insurance</li>"
     "<li>Recent business bank statements, typically the last three to six months</li>"
     "</ul>"
     "<p>Deals in this category move quickly when that list is complete. They stall on "
     "liens far more often than on credit, so knowing what is filed against the business "
     "before you apply saves the most time. See "
     "<a href=\"/heavy-equipment-equity-loan/articles/heavy-equipment-loan-with-an-existing-lien/\">"
     "borrowing with an existing lien</a>.</p>"
     + midcta("<strong>Have the list ready?</strong> One application, real offers, and "
              "checking won't affect your credit.", "Get Matched")),
    ("What Happens After You Apply",
     "<ol>" + "".join(f"<li><strong>{n}.</strong> {t}</li>" for n, t in STEPS) + "</ol>"
     "<p>If anything goes wrong later, the lender's remedies are set by the Uniform "
     "Commercial Code; <a href=\"/heavy-equipment-equity-loan/articles/what-happens-if-you-default-on-an-equipment-loan/\">"
     "what happens if you default</a> explains the sequence and where it can still be "
     "stopped.</p>"),
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

    ld = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{A.BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Equipment Financing", "item": f"{A.BASE}/equipment-financing.html"},
            {"@type": "ListItem", "position": 3, "name": H1, "item": URL}]},
        {"@context": "https://schema.org", "@type": "FinancialService",
         "name": "Heavy Equipment Equity Loan & Equipment Cash-Out Refinancing",
         "description": "Business-purpose financing secured by construction equipment the borrower "
                        "already owns, including excavators, loaders, dozers and skid steers, plus "
                        "cash-out refinancing of existing equipment loans.",
         "url": URL, "provider": {"@id": f"{A.BASE}/#organization"}, "areaServed": "US"},
        {"@context": "https://schema.org", "@type": "WebPage", "@id": f"{URL}#webpage", "url": URL,
         "name": "Heavy Equipment Equity Loan: Borrow Against Construction Equipment You Own",
         "datePublished": today, "dateModified": today,
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".quick-answer", ".ef-speakable"]}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQS]},
        {"@context": "https://schema.org", "@type": "HowTo",
         "name": "How to get a heavy equipment equity loan",
         "description": "Steps to borrow against construction equipment you already own.",
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
<div class="hero-media"><img alt="" decoding="async" fetchpriority="high" height="571" src="{HERO}" width="1024"/></div>
<div class="container">
<div class="inner">
<p class="eyebrow">Financing program</p>
<h1>{H1}</h1>
<p class="lede">Borrow against excavators, loaders, dozers and skid steers you already own, and keep them on the job while you pay it back.</p>
<ul class="hero-checks">
<li><span class="tick">✓</span><span>Business-purpose only</span></li>
<li><span class="tick">✓</span><span>Keep the machines working</span></li>
<li><span class="tick">✓</span><span>Owned outright, or cash-out refinance what you still owe</span></li>
<li><span class="tick">✓</span><span>Asset-secured, so credit carries less weight</span></li>
</ul>
<div class="actions">
<a class="btn btn-primary btn-lg" href="/match.html">See What Your Equipment Can Unlock</a>
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
<p><a href="/match.html">Get matched for an equipment equity loan →</a></p>
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
<div class="group-head"><h2 id="heavy-equipment-equity-loans-at-a-glance">Heavy Equipment Equity Loans at a Glance</h2></div>
<div class="stats">
{stats}
</div>
<p style="margin-top:12px;font-size:.9rem">Typical ranges across lenders, not a quote. Your figures depend on the machines and the business.</p>
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
<h2 id="heavy-equipment-equity-loan-faqs">Heavy Equipment Equity Loan FAQs</h2>
{faq_html}
</div>
</section>
<section class="section section-alt">
<div class="container">
<div class="group" data-tone="bronze">
<div class="prose">
<h2 id="cluster-guides">Heavy Equipment Equity Loan Guides</h2>
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
<h2 id="find-out-what-your-equipment-can-unlock">Find Out What Your Equipment Can Unlock</h2>
<p>Start with the value. Tell us what you own and Axiant shows you what an equity loan, a cash-out refinance and the other asset-backed routes would each raise against it, so you can pick the one that frees up the most cash for the lowest cost. One application, real offers, no obligation, and checking won't affect your credit.</p>
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
