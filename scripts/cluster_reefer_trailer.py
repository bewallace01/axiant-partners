# -*- coding: utf-8 -*-
"""Reefer trailer financing - new spoke under /equipment/trailers/, from the 2026-11-11 daily batch.

Search Console, Oct 13 to Nov 9 2026: "reefer trailer financing" 21 impressions at position 23,
landing on equipment/refrigerated-trucks/reefer-truck-financing-food-transport/, which is about
straight trucks and gives trailers one paragraph. No page is about the trailer: the trailers hub
lists reefers as one type, and the refrigerated truck pages quote reefer trailer prices that
disagree with each other ($25,000-$80,000, $50,000-$80,000+, $60,000-$120,000). This page quotes
no price range of its own: the worked example uses an assumed price and says to use a dealer quote.

Facts and where they come from (read 2026-11-11):
- 21 CFR 1.908(e): carrier duties under FDA's sanitary transportation rule (pre-cool as the
  shipper specifies, show the temperature was held when asked, written procedures).
- 26 U.S.C. 7701(h): a TRAC lease applies to a motor vehicle or trailer.
- 49 CFR 396.17: every commercial motor vehicle, trailers included, needs a periodic (annual)
  inspection.
- CARB TRU page: California TRU registration and operating fees (2022 amendments, effective
  October 1, 2022).
Rates reuse the site's published equipment tiers (7-9% A-tier, 10-18% B/C) from
/business-loan-rates-2026/ (cited page, linked not edited). Payments computed by script.
Never names a lender or a reefer brand. no_hub: /equipment/trailers/ is a hand-built hub page.
"""
from cluster_table import table

FDA = ("https://www.law.cornell.edu/cfr/text/21/1.908",
       "21 CFR 1.908: Requirements for shippers, loaders, carriers and receivers",
       "FDA sanitary transportation rule: pre-cooling, holding the shipper's temperature and written procedures.")
TRAC = ("https://www.law.cornell.edu/uscode/text/26/7701",
        "26 U.S.C. 7701(h): Motor vehicle operating leases (TRAC)",
        "The tax code's terminal rental adjustment clause, which applies to a motor vehicle or trailer.")
INSP = ("https://www.law.cornell.edu/cfr/text/49/396.17",
        "49 CFR 396.17: Periodic inspection",
        "Every commercial motor vehicle, including trailers, must pass a periodic inspection at least every 12 months.")
CARB = ("https://ww2.arb.ca.gov/our-work/programs/transport-refrigeration-unit",
        "California Air Resources Board: Transport Refrigeration Units",
        "California's TRU rule, registration and operating fees for units that run in the state.")
RATES = ("https://axiantpartners.com/business-loan-rates-2026/",
         "Axiant Partners: Business loan rates 2026",
         "The equipment financing rate tiers this page's examples use (7-9% A-tier, 10-18% B/C-tier).")

CLUSTER = {
    "pillar": "equipment/trailers/",
    "hub": "equipment/trailers",
    "no_hub": True,
    "back_href": "/equipment/trailers/",
    "crumb": "Trailer Financing",
    "cta_inline": "Get matched for reefer trailer financing",
    "cta_button": "Get Matched for Trailer Financing",
}

ARTICLES = [{
    "slug": "reefer-trailer-financing",
    "crumb": "Reefer Trailer Financing",
    "title": "Reefer Trailer Financing: Loans, Leases, Terms | Axiant",
    "og_title": "Reefer Trailer Financing: How Lenders Value the Trailer and the Unit",
    "h1": "Reefer Trailer Financing: How Lenders Value the Trailer and the Unit",
    "headline": "Reefer Trailer Financing: How Lenders Value the Trailer and the Unit",
    "lede": "Financing a refrigerated semi-trailer, new or used: why the reefer unit is underwritten on "
            "its own, which structure fits, and what a payment looks like",
    "meta_desc": "Reefer trailer financing: loans and TRAC leases for refrigerated trailers, how lenders value "
                 "the reefer unit's hours, used-trailer checks and example payments.",
    "article_desc": "How refrigerated semi-trailers are financed: how lenders value the box and the reefer unit "
                    "separately, loans vs TRAC leases, used trailer checks, food-safety and California rules, "
                    "and example payments.",
    "keywords": "reefer trailer financing, refrigerated trailer financing, used reefer trailer financing, reefer "
                "trailer loan, reefer trailer lease, refrigerated semi trailer financing",
    "quick_answer": "Reefer trailers finance like other semi-trailers, commonly over <strong>24 to 84 months</strong>, "
                    "but the lender values two things: the insulated trailer and the refrigeration unit, which "
                    "runs its own engine and hour meter. As an illustration, a $75,000 trailer with 10% down at "
                    "9% over 60 months is about <strong>$1,401 a month</strong>. These are typical ranges, not "
                    "quotes; Axiant Partners, a business-loan broker in Boca Raton, compares equipment lenders "
                    "for carriers.",
    "sections": [
        ("Why a Reefer Trailer Is Underwritten Differently",
         "<p>A dry van is a box on wheels. A reefer is a box on wheels with a diesel or electric "
         "refrigeration unit bolted to the front, and that unit wears out on a different clock. Lenders "
         "look at the trailer's age and condition and, separately, the unit's hours, service history and "
         "model year. A five-year-old trailer with a recently rebuilt unit can be easier to finance than a "
         "three-year-old one whose unit has run hard with no records.</p>"
         + table(["What the lender checks", "Why it matters"], [
             ["Reefer unit hours", "The engine-hour meter is the unit's odometer; high hours shorten the term"],
             ["Unit service records", "Proof of maintenance supports value if the trailer is repossessed and resold"],
             ["Insulation and walls", "Damaged or wet insulation lowers holding performance and resale value"],
             ["Floor and doors", "Food-grade floors and tight door seals matter to shippers and buyers"],
             ["Annual inspection", "Trailers, like trucks, need a periodic inspection at least every 12 months"],
             ["Title and liens", "The trailer has its own title; check it for existing liens before you buy"],
         ])),
        ("Loan, TRAC Lease or Dealer Program",
         "<p>Three structures cover most reefer trailer deals. The right one depends on how long you'll "
         "keep the trailer and whether you want a lower payment now or full ownership.</p>"
         + table(["Structure", "How it works", "Fits when"], [
             ["Equipment loan", "You own the trailer; the lender files a lien until it's paid", "You'll run it for years"],
             ["TRAC lease", "Lower payment with a set residual you guarantee at the end", "You trade trailers on a cycle"],
             ["$1 buyout lease", "Lease payments, then you own it for $1", "You want lease paperwork but ownership"],
             ["Dealer or manufacturer program", "Financing arranged where you buy", "A promotional rate beats outside offers"],
         ])
         + "<p>TRAC leases are available because the tax code's motor vehicle lease rule covers trailers as "
         "well as trucks. The catch is the residual: if the trailer sells for less than the residual at "
         "lease end, you pay the difference. For the general trade-offs see "
         '<a href="/equipment/trailers/">trailer financing</a>; for trucks and trailers bought together, see '
         '<a href="/equipment-financing/articles/100-percent-financing-class-8-trucks-trailers-zero-down/">100% '
         "financing for Class 8 trucks and trailers</a>.</p>"),
        ("Example Reefer Trailer Payments",
         "<p><strong>Illustrative, not quotes.</strong> Prices vary widely with length, unit, insulation and "
         "age, so use a written dealer quote. Rates below are the low and high ends of the equipment "
         'financing tiers on our <a href="/business-loan-rates-2026/">business loan rates</a> page.</p>'
         + table(["Scenario", "Amount financed", "Rate and term", "About per month"], [
             ["New trailer, assumed $75,000, 10% down", "$67,500", "9% over 60 months", "$1,401"],
             ["Same trailer, weaker credit", "$67,500", "14% over 60 months", "$1,571"],
             ["Used trailer, assumed $40,000, 15% down", "$34,000", "12% over 48 months", "$895"],
         ])
         + "<p>The gap between 9% and 14% on the same trailer is about $170 a month, or roughly $10,000 over "
         "the term. That's why a clean file and service records on the unit are worth assembling before "
         "you apply. Payments come from standard monthly amortization and are rounded.</p>"),
        ("Buying a Used Reefer Trailer",
         "<p>Used reefers are where most financing problems start, because the unit can fail long before "
         "the trailer does. Before you sign:</p>"
         "<ol>"
         "<li><strong>Get the unit's hours and service history</strong> from the seller, and have it run "
         "down to temperature while you watch.</li>"
         "<li><strong>Ask for the latest annual inspection report</strong> for the trailer.</li>"
         "<li><strong>Check the title and lien search</strong> so you aren't buying someone else's loan.</li>"
         "<li><strong>Price a unit rebuild or replacement</strong> into your offer if the hours are high, "
         "and ask the lender whether it can be financed with the trailer.</li>"
         "<li><strong>If you'll run in California</strong>, confirm the unit can be registered and operated "
         "under the state's transport refrigeration unit rules.</li>"
         "</ol>"
         '<p>More on lender limits for older equipment: <a href="/equipment-financing/articles/can-you-finance-used-equipment/">can '
         "you finance used equipment</a>.</p>"),
        ("Food Safety Rules That Affect the Deal",
         "<p>If you haul food, shippers will ask how you meet FDA's sanitary transportation rule. When a "
         "written agreement makes the carrier responsible, the carrier must pre-cool refrigerated "
         "compartments as the shipper specifies, be able to show the temperature was held during the trip "
         "when asked, and keep written procedures for cleaning and temperature control. A trailer with a "
         "working temperature recorder makes that easier, and some shippers won't load without one. "
         "Budget for the recorder and any telematics when you size the loan.</p>"
         "<p>Pulling a reefer with a truck you're also financing? Our guide to "
         '<a href="/equipment/refrigerated-trucks/reefer-truck-financing-food-transport/">reefer truck financing '
         'for food transport</a> covers straight trucks, and <a href="/trucking-business-financing.html">trucking '
         "business financing</a> covers the rest of the operation.</p>"),
        ("How to Apply",
         "<ol>"
         "<li><strong>Get a written quote</strong> with the trailer's VIN, year, length, and the unit's make, model year and hours.</li>"
         "<li><strong>Gather three to six months of bank statements</strong>, your operating authority and, for larger deals, tax returns.</li>"
         "<li><strong>Decide loan or lease</strong> based on how long you'll keep the trailer.</li>"
         "<li><strong>Compare at least two offers</strong> on rate, term, fees and any prepayment terms.</li>"
         "</ol>"
         '<p><a href="/match.html">Get matched with equipment lenders</a> or call '
         '<a href="tel:+15612680465">(561) 268-0465</a>. Approval and terms are up to the lender.</p>'),
    ],
    "faqs": [
        ("Can you finance a reefer trailer?",
         "Yes. Refrigerated semi-trailers are financed with equipment loans, TRAC leases, $1 buyout leases and "
         "dealer programs, commonly over 24 to 84 months. The lender values both the trailer and the "
         "refrigeration unit."),
        ("What credit score do you need for reefer trailer financing?",
         "It varies by lender. Stronger credit gets the lower end of equipment financing rates, around 7-9% on "
         "our published tiers, while weaker files land in the 10-18% range or need a larger down payment."),
        ("Can I finance a used reefer trailer?",
         "Yes, but expect shorter terms on older trailers and closer questions about the reefer unit's hours "
         "and service history. A recent annual inspection and maintenance records help."),
        ("What is the monthly payment on a reefer trailer?",
         "As an illustration, $67,500 financed at 9% over 60 months is about $1,401 a month, and at 14% about "
         "$1,571. Your price, down payment, rate and term set the real number."),
        ("Is a TRAC lease available on a trailer?",
         "Yes. The tax code's TRAC lease rule covers motor vehicles and trailers. It lowers the payment, but you "
         "guarantee the residual value at the end of the lease."),
    ],
    "related": [
        ("/equipment/trailers/", "Trailer financing"),
        ("/equipment/refrigerated-trucks/", "Refrigerated truck financing"),
        ("/equipment/refrigerated-trucks/reefer-truck-financing-food-transport/", "Reefer truck financing for food transport"),
        ("/equipment-financing/articles/100-percent-financing-class-8-trucks-trailers-zero-down/", "100% financing for trucks and trailers"),
        ("/trucking-business-financing.html", "Trucking business financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [FDA, TRAC, INSP, CARB, RATES],
}]
