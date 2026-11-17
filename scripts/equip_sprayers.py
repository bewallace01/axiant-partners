# -*- coding: utf-8 -*-
"""Agricultural sprayer financing - /equipment/sprayers/ rewritten, daily batch 2026-11-15.

Why: 44% of its body was shared with /equipment/grain-equipment/ and 41% with
/equipment/landscape-trailers/ (simscan, 2026-11-15); grain-equipment and landscape-trailers were
43-44% shared with this page. No Search Console impressions in 28 days, so the rewrite answers
this page's own questions: pull-type vs self-propelled vs spray drones, what precision options
add, custom applicators financing on contracted acres, seasonal payment schedules, licensing and
FAA rules lenders ask about, used sprayer checks, and payments. Tractor/FSA material stays on
/equipment/tractors/ and is linked, not repeated.

Numbers: price ranges are the ones the page already published (pull-type $30K-$80K mid-size and
$80K-$150K+ large, self-propelled $250K-$400K+, terms 24-84 months, 600+ credit, 0-20% down,
6-15% rates, the page's own $150K at 8% over 60 months example, recomputed). Payments computed
by pmt() and an annual-payment formula at an assumed 8%. The custom-applicator example uses a
per-acre rate and acreage stated as assumptions for the reader to replace; arithmetic only.
Rules named for what they govern: 40 CFR part 171 (certification of pesticide applicators;
restricted-use pesticides), 14 CFR part 137 (agricultural aircraft operations, which covers
spray drones; heavier drones also need an FAA exemption). Removed: "used 30-50% less",
"5-year-old pull-type $20K-$50K", "used self-propelled $120K-$250K" and brand resale claims
(unsourced). No named lenders, dealers or manufacturers.
"""
from equipment_rewrite import pmt, pay_row, table, usd

RATE = 8.0


def annual(principal, apr_pct, years):
    r = apr_pct / 100
    return principal * r / (1 - (1 + r) ** -years)


SP_PRICE, SP_DOWN = 320_000, 48_000
SP_FIN = SP_PRICE - SP_DOWN
SP_MO = pmt(SP_FIN, RATE, 72)
SP_YR = annual(SP_FIN, RATE, 6)
ACRES, PER_ACRE = 20_000, 8
REV = ACRES * PER_ACRE

PAGE = {
    "path": "equipment/sprayers/index.html",
    "date": "2026-11-15",
    "date_text": "November 15, 2026",
    "title": "Sprayer Financing: Self-Propelled, Pull-Type, Drone | Axiant",
    "og_title": "Sprayer Financing: Self-Propelled, Pull-Type, Drone | Axiant",
    "desc": ("Sprayer financing: pull-type $30K-$150K+, self-propelled $250K-$400K+, annual or monthly payments, "
             "custom applicator deals and drone rules."),
    "headline": "Sprayer Financing: Self-Propelled, Pull-Type and Spray Drones",
    "article_desc": ("Financing an agricultural sprayer: pull-type versus self-propelled versus spray drones, precision "
                     "options, custom applicator underwriting, annual payment schedules, licensing and used sprayer checks."),
    "h1": "Sprayer Financing: Self-Propelled, Pull-Type and Spray Drones",
    "lede": ("Pull-type sprayers typically cost $30,000-$150,000+ and self-propelled machines $250,000-$400,000+. "
             "Pay monthly or once a year after harvest. Decisions in 24-48 hours for qualified applications."),
    "checks": [
        "Self-propelled, pull-type and spray drones",
        "Annual, semi-annual or monthly payments",
        "Typical terms 24-84 months",
        "Credit 600+; 0-20% down payment",
    ],
    "intro": ('<p>This page covers sprayers for row crops, specialty crops and custom application businesses. Tractors and '
              'FSA loan limits are on <a href="/equipment/tractors/">tractor financing</a>, bins and dryers on '
              '<a href="/equipment/grain-equipment/">grain equipment financing</a>, and turf spray rigs on '
              '<a href="/landscaping-business-financing.html">landscaping business financing</a>.</p>'),
    "quick_answer": (f"As of November 2026, an agricultural sprayer commonly finances over 24-84 months with 0-20% down and "
                     f"600+ credit, at rates that typically run 6-15%. Pull-type sprayers cost about $30,000-$150,000+ and "
                     f"self-propelled machines $250,000-$400,000+. At an assumed 8%, a $150,000 sprayer is about "
                     f"<strong>{usd(pmt(150_000, RATE, 60))} a month</strong> over 60 months, and {usd(SP_FIN)} financed on a "
                     f"self-propelled unit is about <strong>{usd(SP_YR)} a year</strong> on six annual payments. Axiant "
                     f"Partners, a business-loan broker in Boca Raton, compares ag equipment lenders. Typical ranges, not a quote."),
    "qa_link": "Get matched for sprayer financing",
    "glance_h2": "Sprayer Financing at a Glance",
    "glance": [("$30K-$400K+", "New sprayer range"), ("Annual", "Payments can follow harvest"), ("24-84 mo", "Typical terms"),
               ("0-20%", "Down payment"), ("600+", "Credit (typical)"), ("24-48 hr", "Equipment approval")],
    "sections": [
        ("Pull-Type, Self-Propelled or Drone",
         table(["", "Pull-type", "Self-propelled", "Spray drone"], [
             ["New price (typical)", "$30,000-$150,000+", "$250,000-$400,000+", "Varies widely by payload"],
             ["Power", "Your tractor", "Its own engine and cab", "Batteries, several packs"],
             ["Best fit", "Smaller acres, tractor already owned", "Large acres, custom work", "Spot spraying, wet or steep fields"],
             ["Extra rules", "Applicator license", "Applicator license", "License plus FAA Part 137"],
         ])
         + '\n<div class="prose">\n<p>The price ranges for pull-type and self-propelled sprayers are the ones this page '
         'publishes. Drone prices vary too much by tank size and battery count to give a range; get a dealer quote that '
         'lists the aircraft, batteries, charger or generator, and software separately.</p>\n</div>', None),
        ("Sprayer Payments, Monthly or Annual",
         f'<div class="prose">\n<p>Illustrative payments at an assumed {RATE:.0f}% before tax and fees, computed by formula. '
         'Many ag lenders let payments fall once or twice a year, after the crop is sold.</p>\n</div>\n'
         + table(["Amount financed", "Term", "About per month", "Total interest"], [
             pay_row(50_000, RATE, 48), pay_row(150_000, RATE, 60), pay_row(SP_FIN, RATE, 72), pay_row(400_000, RATE, 84)])
         + '\n<div class="prose">\n<p>Annual payment equivalents: ' + "; ".join(
             f"{usd(a)} over {y} years is about {usd(annual(a, RATE, y))} a year" for a, y in
             [(50_000, 4), (150_000, 5), (SP_FIN, 6)]) + '.</p>\n</div>', None),
        ("Worked Example: A Used Self-Propelled Sprayer",
         f'<div class="prose">\n<p><strong>Illustrative, not a quote.</strong> A grain farm buys a self-propelled sprayer for '
         f'{usd(SP_PRICE)} and puts {usd(SP_DOWN)} down, partly from a trade-in. That leaves {usd(SP_FIN)} to finance at an '
         f'assumed {RATE:.0f}%:</p>\n</div>\n'
         + table(["Schedule", "Payment", "Total interest"], [
             ["72 monthly payments", f"{usd(SP_MO)} a month", usd(SP_MO * 72 - SP_FIN)],
             ["6 annual payments", f"{usd(SP_YR)} a year", usd(SP_YR * 6 - SP_FIN)],
         ])
         + '\n<div class="prose">\n<p>Annual payments cost more interest because principal is repaid later, but they match a '
         'farm that sells most of its crop in one season. Pick the schedule your cash flow actually supports; a missed '
         'annual payment is a large one.</p>\n</div>', "Get Matched for Sprayer Financing"),
        ("Custom Applicators: Financing on Contracted Acres",
         f'<div class="prose">\n<p>Custom application businesses are underwritten on the acres they cover, not the farm they '
         f'own. Lenders ask for signed or repeat customer lists, last season&rsquo;s invoices and the acres per machine. As an '
         f'<strong>assumption to replace with your own</strong>: {ACRES:,} acres a season at {usd(PER_ACRE)} an acre is '
         f'{usd(REV)} of revenue, against the {usd(SP_YR)} annual payment above.</p>'
         '<p>Show the season, not just the total: when spraying starts, when customers pay, and fuel, chemical-handling and '
         'labor costs. A second machine is easier to finance once the first has a season of invoices.</p>\n</div>', None),
        ("Precision Options That Change the Price",
         '<div class="prose">\n<ul><li><strong>Boom section or nozzle control</strong>: shuts off over areas already sprayed.</li>'
         '<li><strong>Guidance and auto-steer</strong>: may be on the sprayer or moved from another machine.</li>'
         '<li><strong>Rate controllers and variable-rate maps</strong>.</li>'
         '<li><strong>Camera-based targeted spraying</strong>: sprays only detected weeds; often a factory option or a '
         'per-acre subscription.</li></ul>'
         '<p>Factory options on the quote are financed with the machine. Software subscriptions billed per acre or per year '
         'usually are not collateral, so budget them as an operating cost.</p>\n</div>', None),
        ("Licensing and Rules Lenders Ask About",
         '<div class="prose">\n<p>Anyone applying restricted-use pesticides, or applying for hire, generally needs state '
         'certification under the federal standards in '
         '<a href="https://www.ecfr.gov/current/title-40/chapter-I/subchapter-E/part-171" rel="noopener nofollow" target="_blank">40 CFR part 171</a>. '
         'Spray drones fly under the FAA&rsquo;s agricultural aircraft rules, '
         '<a href="https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-137" rel="noopener nofollow" target="_blank">14 CFR part 137</a>, '
         'and heavier drones also need an FAA exemption. Lenders financing a custom applicator or a drone commonly ask for '
         'the certificates and for liability insurance that covers drift.</p>\n</div>', None),
        ("Buying a Used Sprayer",
         '<div class="prose">\n<ul><li><strong>Engine and pump hours</strong>, and service records.</li>'
         '<li><strong>Boom condition</strong>: welds, breakaways, and plumbing for leaks.</li>'
         '<li><strong>Tank and rinse system</strong>: chemical residue matters if you switch crops or products.</li>'
         '<li><strong>Electronics</strong>: whether the display and rate controller are still supported.</li>'
         '<li><strong>Dealer or auction</strong>: many lenders finance used sprayers with a dealer quote; auction purchases '
         'may need an appraisal or a larger down payment.</li></ul>'
         '<p>See <a href="/equipment-financing/articles/can-you-finance-used-equipment/">financing used equipment</a> and '
         '<a href="/agriculture-business-financing.html">agriculture business financing</a>.</p>\n</div>',
         "Apply for Sprayer Financing"),
    ],
    "faq_h2": "Sprayer Financing FAQ",
    "faqs": [
        ("How much is the payment on a sprayer?",
         f"At an assumed 8%, $150,000 is about {usd(pmt(150_000, RATE, 60))} a month over 60 months, and {usd(SP_FIN)} is "
         f"about {usd(SP_MO)} a month over 72 months or {usd(SP_YR)} a year on six annual payments. Illustrations, not quotes."),
        ("Can sprayer payments be annual instead of monthly?",
         "Often. Many ag lenders schedule annual or semi-annual payments after harvest. They cost more interest than monthly "
         "payments on the same loan."),
        ("Can a custom applicator finance a self-propelled sprayer?",
         "Yes. Lenders underwrite the acres you cover: customer lists, last season's invoices and your costs. A first "
         "season with no invoices usually needs a larger down payment."),
        ("Can you finance a spray drone?",
         "Usually, with a dealer quote listing the aircraft, batteries and charging. Lenders may ask for the FAA Part 137 "
         "certificate and your applicator license."),
        ("Can you finance a used sprayer?",
         "Yes, commonly from a dealer with a written quote. Hours, boom and tank condition, and whether the electronics are "
         "still supported affect approval."),
        ("How long are sprayer financing terms?",
         "Commonly 24-84 months. Self-propelled machines tend toward the longer end."),
    ],
    "sources": [
        ("https://www.ecfr.gov/current/title-40/chapter-I/subchapter-E/part-171", "40 CFR part 171",
         "Federal standards for certifying pesticide applicators, including commercial applicators of restricted-use pesticides."),
        ("https://www.ecfr.gov/current/title-14/chapter-I/subchapter-G/part-137", "14 CFR part 137",
         "FAA rules for agricultural aircraft operations, which include spray drones."),
        ("https://www.irs.gov/publications/p946", "IRS Publication 946",
         "Depreciation and the Section 179 deduction for farm and business equipment."),
    ],
}
