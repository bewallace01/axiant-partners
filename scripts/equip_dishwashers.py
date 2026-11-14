# -*- coding: utf-8 -*-
"""Commercial dishwasher financing - /equipment/dishwashers-warewashing/ rewritten, batch 2026-11-14.

Why: 47% of its body was shared with /equipment/prep-equipment-restaurant/ (simscan,
2026-11-14), and ventilation-hood-systems was 40% shared with it. Demand is small
("commercial dishmachine leasing" 4 impressions), so the rewrite is about answering this
page's own questions: machine types, high-temp vs low-temp, booster heaters, chemical-supplier
rental programs vs buying, utilities, and what a financed package costs.

Numbers: price ranges are the ones the page already published (undercounter $3K-$8K,
door-type $8K-$20K+, conveyor/flight $15K-$25K+, pot sinks $1K-$5K); terms 36-60 months,
600+ credit and 0-20% down are its published ranges. Payments computed by pmt() at an
assumed 10%, stated as an illustration. FDA Food Code 2022 sections are cited for what they
govern (4-501.112 hot water sanitizing temperatures, 4-501.114 chemical sanitizer, 4-204.113
data plate); no temperatures or concentrations are quoted because the Food Code text could not
be read in this session. NSF/ANSI 3 named as the warewashing equipment standard. ENERGY STAR
linked for efficiency, no savings figures. No named brands, chemical suppliers or lenders.
"""
from equipment_rewrite import pmt, pay_row, table, usd

RATE = 10.0
EX = [("Door-type machine", 14_000), ("Booster heater", 3_500), ("Tables and installation", 2_500)]
EX_TOTAL = sum(v for _, v in EX)
EX_MO = pmt(EX_TOTAL, RATE, 48)

FDA = "https://www.fda.gov/food/fda-food-code/food-code-2022"

PAGE = {
    "path": "equipment/dishwashers-warewashing/index.html",
    "date": "2026-11-14",
    "date_text": "November 14, 2026",
    "title": "Commercial Dishwasher Financing: Lease, Rent or Buy | Axiant",
    "og_title": "Commercial Dishwasher Financing: Lease, Rent or Buy | Axiant",
    "desc": (f"Commercial dishwasher financing: undercounter, door-type and conveyor prices, high-temp vs "
             f"low-temp, chemical rental programs vs buying, payments from {usd(pmt(6_000, RATE, 36))} a month."),
    "headline": "Commercial Dishwasher Financing: Lease, Rent or Buy",
    "article_desc": ("Financing a commercial dishwasher: machine types and typical prices, high-temp vs low-temp "
                     "sanitizing, booster heaters, chemical-supplier rental programs versus buying, and payments."),
    "h1": "Commercial Dishwasher Financing: Lease, Rent or Buy",
    "lede": ("Commercial dishwashers typically cost $3,000 for an undercounter unit to $25,000+ for a conveyor. "
             "Finance the installed package, booster heater included, or compare a chemical-supplier rental. "
             "Decisions in 24-48 hours for qualified applications."),
    "checks": [
        "Undercounter, door-type and conveyor machines",
        "Booster heaters, tables and install on one deal",
        "Typical terms 36-60 months",
        "Credit 600+; 0-20% down payment",
    ],
    "intro": ('<p>This page is about financing warewashing: dish machines, booster heaters, pot sinks and dish '
              'tables. Cooking lines are on <a href="/equipment/commercial-kitchen/">commercial kitchen financing</a>, '
              'and mixers and slicers on <a href="/equipment/prep-equipment-restaurant/">prep equipment financing</a>.</p>'),
    "quick_answer": (f"As of November 2026, a commercial dishwasher commonly finances over 36-60 months with 0-20% "
                     f"down and 600+ credit. Undercounter machines typically cost $3,000-$8,000, door-type "
                     f"$8,000-$20,000+ and conveyor machines $15,000-$25,000+. At an assumed 10%, a "
                     f"{usd(EX_TOTAL)} door-type package with a booster heater is about <strong>{usd(EX_MO)} a "
                     f"month</strong> over 48 months and a $6,000 undercounter unit about <strong>"
                     f"{usd(pmt(6_000, RATE, 36))}</strong> over 36. Axiant Partners, a business-loan broker in Boca Raton, "
                     f"compares equipment lenders. Typical ranges, not a quote."),
    "qa_link": "Get matched for dishwasher financing",
    "glance_h2": "Commercial Dishwasher Financing at a Glance",
    "glance": [("$3K-$25K+", "Machine range"), ("24-48 hr", "Equipment approval"), ("36-60 mo", "Typical terms"),
               ("0-20%", "Down payment"), ("600+", "Credit (typical)"), ("Own or rent", "Two ways to get one")],
    "sections": [
        ("Which Dish Machine Fits Your Volume",
         '<div class="prose">\n<p>Machine size is set by how many racks the kitchen washes at its busiest hour. '
         'Typical new prices before installation, as this page publishes them; not quotes:</p>\n</div>\n'
         + table(["Machine", "Fits", "Typical price"], [
             ["Undercounter", "Bars, cafes, small dining rooms", "$3,000-$8,000"],
             ["Door-type (pass-through)", "Full-service restaurants", "$8,000-$20,000+"],
             ["Conveyor or flight", "Banquet, hospital, campus", "$15,000-$25,000+"],
             ["Pot and pan sink", "Every kitchen with a dish pit", "$1,000-$5,000"],
         ])
         + '\n<div class="prose">\n<p>Large flight machines with dryers and blowers can cost well above these ranges. '
         'Buying a machine one size too small shows up as a backed-up dish pit and overtime; one size too large wastes '
         'water, chemicals and power on every cycle.</p>\n</div>', None),
        ("High-Temp vs Low-Temp Machines",
         '<div class="prose">\n<p>The choice changes the price, the utility bill and what else you must buy.</p><ul>'
         '<li><strong>High-temperature</strong> machines sanitize with a hot water final rinse. The FDA Food Code sets the '
         f'rinse temperatures (<a href="{FDA}" rel="noopener nofollow" target="_blank">Food Code 4-501.112</a>), and most '
         'buildings need a booster heater to reach them. Dishes dry faster and there is no sanitizer to buy.</li>'
         '<li><strong>Low-temperature</strong> machines sanitize with a chemical such as chlorine at the concentration '
         f'the Food Code sets (<a href="{FDA}" rel="noopener nofollow" target="_blank">4-501.114</a>). The machine is often '
         'cheaper and needs no booster, but sanitizer is an ongoing cost.</li>'
         '<li><strong>Hoods and steam:</strong> some jurisdictions require a hood or condensate system over high-temp '
         'machines. Check with your local code official before ordering; see '
         '<a href="/equipment/ventilation-hood-systems/">ventilation hood financing</a>.</li></ul>'
         '<p>Either way the machine must carry a data plate with its operating specifications (Food Code 4-204.113), and '
         'health inspectors check it.</p>\n</div>', None),
        ("Dishwasher Payments by Package",
         f'<div class="prose">\n<p>Illustrative monthly payments at an assumed {RATE:.0f}% before tax and fees, computed by '
         'formula. Small-ticket equipment rates vary with credit and time in business.</p>\n</div>\n'
         + table(["Amount financed", "Term", "About per month", "Total interest"], [
             pay_row(6_000, RATE, 36), pay_row(EX_TOTAL, RATE, 48), pay_row(30_000, RATE, 60),
             pay_row(45_000, RATE, 60)])
         + '\n<div class="prose">\n<p>Model other amounts in the <a href="/calculator.html">financing calculator</a>.</p>\n</div>',
         None),
        ("Worked Example: Replacing a Door-Type Machine",
         f'<div class="prose">\n<p><strong>Illustrative, not a quote.</strong> A full-service restaurant&rsquo;s '
         f'door-type machine fails an inspection. The replacement package:</p>\n</div>\n'
         + table(["Item", "Price"], [[n, usd(v)] for n, v in EX] + [["Total financed", usd(EX_TOTAL)]])
         + f'\n<div class="prose">\n<p>At an assumed {RATE:.0f}% over 48 months, about <strong>{usd(EX_MO)} a month</strong> and '
         f'{usd(EX_MO * 48 - EX_TOTAL)} total interest. Quoting the booster and installation with the machine puts them '
         'on the same approval; added later, they are a second deal.</p>\n</div>', "Get Matched for Dishwasher Financing"),
        ("Chemical-Supplier Rental vs Buying",
         '<div class="prose">\n<p>Many restaurants never buy a dish machine. Chemical and service companies commonly '
         'place a low-temp machine for a monthly fee, with service included, on condition that you buy their '
         'detergent, rinse aid and sanitizer.</p>\n</div>\n'
         + table(["", "Chemical-supplier rental", "Financed purchase"], [
             ["Upfront cost", "Little or none", "0-20% down"],
             ["Monthly cost", "Fee plus required chemicals", "Loan or lease payment"],
             ["Service", "Usually included", "Your contract or call-outs"],
             ["Machine choice", "Supplier&rsquo;s models", "Any make, high or low temp"],
             ["At the end", "Machine goes back", "You own it"],
         ])
         + '\n<div class="prose">\n<p>To compare, add a year of required chemical purchases to the rental fee and set it '
         'against a loan payment plus your own chemicals and a service contract. Read the rental agreement for its '
         'term, minimum chemical volume and early-cancellation charges.</p>\n</div>', None),
        ("Water, Energy and Running Cost",
         '<div class="prose">\n<p>A dish machine runs every service, so its utility use often matters more over the term '
         'than its price. ENERGY STAR certifies commercial dishwashers that use less water and energy '
         '(<a href="https://www.energystar.gov/products/commercial_dishwashers" rel="noopener nofollow" target="_blank">ENERGY '
         'STAR</a>), and many utilities offer rebates on certified models. Commercial machines are listed to '
         '<strong>NSF/ANSI 3</strong>, the warewashing equipment standard; ask for it on the quote.</p>\n</div>', None),
        ("What Lenders Ask For",
         '<div class="prose">\n<ul><li><strong>The quote</strong> with machine, booster, tables and installation listed separately.</li>'
         '<li><strong>3-6 months of bank statements</strong>; at this ticket size that is usually the whole file.</li>'
         '<li><strong>Time in business:</strong> 1-2+ years is typical; a new restaurant may need a larger down payment '
         'or to finance the dish machine with the full kitchen build-out.</li>'
         '<li><strong>Used machines:</strong> many lenders will finance a refurbished unit from a dealer with a written '
         'quote; private sales are harder.</li></ul>'
         '<p>For a full kitchen, see <a href="/restaurants-business-financing.html">restaurant business financing</a> and '
         '<a href="/equipment-financing/articles/what-credit-score-needed-equipment-financing/">credit needed for equipment financing</a>.</p>\n</div>',
         "Apply for Dishwasher Financing"),
    ],
    "faq_h2": "Commercial Dishwasher Financing FAQ",
    "faqs": [
        ("How much does it cost to finance a commercial dishwasher?",
         f"At an assumed 10%, a {usd(EX_TOTAL)} door-type package is about {usd(EX_MO)} a month over 48 months and a "
         f"$6,000 undercounter unit about {usd(pmt(6_000, RATE, 36))} over 36 months. These are illustrations, not quotes."),
        ("Is it better to rent a dishwasher from a chemical company or buy one?",
         "Renting needs little cash and usually includes service, but you must buy the supplier's chemicals and the "
         "machine goes back. Buying costs more upfront and lets you choose any machine. Compare a year of rental fees "
         "plus required chemicals with a loan payment."),
        ("Do I need a booster heater for a commercial dishwasher?",
         "Usually for a high-temperature machine, because the building's water heater rarely reaches the Food Code's "
         "final rinse temperature. Low-temperature chemical machines do not need one."),
        ("Can a booster heater and installation be financed with the machine?",
         "Yes, when they are on the same quote. Added later, they are usually a separate deal."),
        ("Can a new restaurant finance a dishwasher?",
         "Often, as part of the kitchen package. Most lenders prefer 1-2+ years in business, so a new restaurant may "
         "need a larger down payment or a chemical-supplier rental."),
        ("How long are commercial dishwasher financing terms?",
         "Commonly 36-60 months. Smaller undercounter machines tend toward the shorter end."),
    ],
    "sources": [
        (FDA, "FDA Food Code 2022", "Warewashing rules: hot water (4-501.112) and chemical (4-501.114) sanitizing, data plates (4-204.113)."),
        ("https://www.energystar.gov/products/commercial_dishwashers", "ENERGY STAR Commercial Dishwashers",
         "Certified models and efficiency criteria for undercounter, door-type and conveyor machines."),
        ("https://www.nsf.org/knowledge-library/food-equipment-standards", "NSF food equipment standards",
         "NSF/ANSI 3 covers commercial warewashing equipment."),
        ("https://www.irs.gov/publications/p946", "IRS Publication 946",
         "Depreciation and the Section 179 deduction for business equipment."),
    ],
}
