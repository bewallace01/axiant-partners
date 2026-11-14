# -*- coding: utf-8 -*-
"""/equipment/wheel-loaders/ - daily batch 2026-11-14 (render: scripts/equipment_rewrite.py).

Search Console, Oct 15 - Nov 11 2026: "wheel loader financing" 59 impressions split between
this page (43 at position 30) and construction-heavy-equipment-financing (16 at 52; that
article sits in the excavator split and is not edited). This page is the target. Also
"finance a wheel loader" 14 at 24, "purchase heavy-duty mining loaders with financing options"
10 at 4, "loader financing" 5 at 30, "wheel loader lease" 3 at 25.

The old template was 45% shared with /equipment/backhoes/ (simscan); rewritten here around
loader-specific questions: size classes, tonnage economics, quarry and MSHA rules, tires and
buckets, used-loader checks, seasonal structures, loader vs skid steer vs backhoe.

Prices are the ranges this page already published (compact $80-130K, mid-size $150-250K,
large $250-400K+), framed as typical. Removed: "50-70% of value after 5 years" (no source;
removed from sibling pages on Nov 9) and "used costs 30-50% less" (no source). Payments
computed by pmt() at an illustrative 8%. MSHA 30 CFR 56.14100 and 56.14130 and EPA 40 CFR
1039 read from eCFR. No named lenders or quotes.
"""
from equipment_rewrite import pay_row, pmt, table, usd

RATE = 8
ex_price, ex_down = 210000, 21000
ex_fin = ex_price - ex_down
ex_pmt = pmt(ex_fin, RATE, 60)
TPH, HRS = 180, 120  # assumed tons per hour loaded and hours per month, stated on the page
per_ton = ex_pmt / (TPH * HRS)

PAY = table(["Amount financed", "Term", "About per month", "Total interest"],
            [pay_row(100000, RATE, 48), pay_row(150000, RATE, 60), pay_row(210000, RATE, 60),
             pay_row(210000, RATE, 72), pay_row(325000, RATE, 84)])

PRICES = table(["Size class", "Typical bucket", "Typical new price"], [
    ["Compact loader", "About 1-2 cu yd", "$80,000-$130,000"],
    ["Mid-size loader", "About 2-4 cu yd", "$150,000-$250,000"],
    ["Large loader", "4+ cu yd", "$250,000-$400,000+"],
])

CHOOSE = table(["Machine", "Best at", "Financing note"], [
    ["Wheel loader", "Loading trucks, stockpiles, yards", "Larger ticket; tires and bucket matter"],
    ["Skid steer", "Tight sites, attachments", "Smaller ticket; shorter terms common"],
    ["Backhoe loader", "Dig and load on one machine", "Mid-range ticket; utility work"],
])

PAGE = {
    "path": "equipment/wheel-loaders/index.html",
    "date": "2026-11-14",
    "date_text": "November 14, 2026",
    "title": "Wheel Loader Financing: Rates, Payments and Terms | Axiant",
    "og_title": "Wheel Loader Financing: Rates, Payments and Terms | Axiant",
    "desc": (f"Wheel loader financing: prices by size class, payments from {usd(pmt(150000, RATE, 60))} a month, "
             "quarry and aggregate deals, tires and buckets, used loaders, lease or loan."),
    "h1": "Wheel Loader Financing: Loans and Leases for Contractors, Quarries and Yards",
    "lede": "Compact, mid-size and large wheel loaders typically cost $80,000-$400,000+ new. Finance the "
            "machine, the bucket and the tires on one approval. Decisions in 24-48 hours for qualified applications.",
    "checks": ["Equipment financing decisions in 24-48 hours",
               "New and used wheel loaders, buckets and couplers",
               "Typical terms 36-84 months; seasonal payment plans",
               "Credit 600+; 0-20% down payment"],
    "intro": ("<p>This page is about financing rubber-tired wheel loaders for construction, aggregates, "
              "recycling, agriculture and material yards. Dig-and-load machines are on "
              "<a href=\"/equipment/backhoes/\">backhoe financing</a>, compact track and wheeled skid steers on "
              "<a href=\"/equipment/skid-steers/\">skid steer financing</a>, and every construction product on "
              "<a href=\"/construction-business-financing.html\">construction business financing</a>.</p>"),
    "quick_answer": ("As of November 2026, wheel loader financing commonly runs 36-84 months with 0-20% down "
                     "and 600+ credit, secured by the machine. Compact loaders typically cost $80,000-$130,000 new, "
                     "mid-size $150,000-$250,000 and large units $250,000-$400,000+. At a typical 8%, a $150,000 "
                     f"loader is about <strong>{usd(pmt(150000, RATE, 60))} a month</strong> over 60 months and a "
                     f"$325,000 machine about <strong>{usd(pmt(325000, RATE, 84))}</strong> over 84. Axiant Partners, "
                     "a business-loan broker in Boca Raton, compares equipment lenders. Typical ranges, not a quote."),
    "qa_link": "Get matched for wheel loader financing",
    "glance_h2": "Wheel Loader Financing at a Glance",
    "glance": [("$80K-$400K+", "Typical new range"), ("24-48 hr", "Equipment approval"),
               ("36-84 mo", "Terms"), ("0-20%", "Down payment"), ("600+", "Credit (typical)"),
               ("50 states", "Nationwide")],
    "faq_h2": "Wheel Loader Financing FAQ",
    "sections": [
        ("Wheel Loader Prices by Size Class",
         "<div class=\"prose\">\n<p>Typical new prices before tax, freight and attachments, as this page has published "
         "them. Bucket type, cab package, high-lift arms and the engine move a machine across its range.</p>\n</div>\n"
         + PRICES +
         "\n<div class=\"prose\">\n<p>Used loaders are priced from a listing, auction results or an appraisal, so a lender "
         "works from the specific machine rather than a table. Telescopic wheel loaders, which add an extending boom, "
         "are listed on <a href=\"/equipment-for-sale/telescopic-wheel-loaders/\">telescopic wheel loaders for sale</a>.</p>\n</div>",
         None),
        ("Wheel Loader Payments by Price and Term",
         f"<div class=\"prose\">\n<p>Illustrative payments at {RATE}% before tax and fees, computed by formula:</p>\n</div>\n"
         + PAY +
         "\n<div class=\"prose\">\n<p>A longer term lowers the payment and raises total interest. Model your own numbers in "
         "the <a href=\"/calculator.html\">financing calculator</a>.</p>\n</div>",
         None),
        ("Worked Example: A Mid-Size Loader at an Aggregate Yard",
         f"<div class=\"prose\">\n<p><strong>Illustrative, not a quote.</strong> A sand and gravel yard replaces a worn "
         f"loader with a {usd(ex_price)} mid-size machine, puts 10% ({usd(ex_down)}) down and finances {usd(ex_fin)} at "
         f"{RATE}% over 60 months.</p><ul><li>Monthly payment: about <strong>{usd(ex_pmt)}</strong></li>"
         f"<li>Total interest over the term: about {usd(ex_pmt * 60 - ex_fin)}</li>"
         f"<li>At an assumed {TPH} tons loaded an hour for {HRS} hours a month, the payment works out to about "
         f"<strong>${per_ton:.2f} a ton</strong></li></ul><p>Cost per ton is how a yard owner and an underwriter both "
         "read a loader. Bring scale tickets or sales by ton, and the hours on the machine you are replacing, so the "
         "payment reads as a small share of what the loader moves.</p>\n</div>",
         "Get Matched for Wheel Loader Financing"),
        ("Quarry, Aggregate and Mining Buyers",
         "<div class=\"prose\">\n<ul><li><strong>Fixed-site contracts:</strong> a loader feeding a crusher, a transfer "
         "station or a mill under contract is strong evidence of use. Include the contract with the application.</li>"
         "<li><strong>Mine safety rules:</strong> at surface mines and quarries, wheel loaders need rollover protection "
         "and seat belts (<a href=\"https://www.ecfr.gov/current/title-30/section-56.14130\" "
         "rel=\"noopener nofollow\" target=\"_blank\">30 CFR 56.14130</a>), and the operator examines the machine before "
         "each shift (<a href=\"https://www.ecfr.gov/current/title-30/section-56.14100\" "
         "rel=\"noopener nofollow\" target=\"_blank\">30 CFR 56.14100</a>). A used machine without its ROPS is a "
         "repair to price in.</li><li><strong>Seasonal output:</strong> aggregate sales follow construction season, so "
         "six months of bank statements shows the pattern fairly, and some lenders offer payment plans that skip or "
         "reduce winter months.</li><li><strong>Bundled fleets:</strong> a loader bought with haul trucks or a crusher "
         "can go on one master lease or loan, with one credit review.</li></ul>\n</div>",
         None),
        ("Tires, Buckets and Couplers on the Deal",
         "<div class=\"prose\">\n<p>On a loader, the wear parts are big-ticket items. A full set of loader tires is a "
         "substantial cost, and an inspector checks the tread before anything else. If the machine will need tires "
         "within a year, negotiate them into the purchase so they are financed at the machine&rsquo;s rate.</p>"
         "<ul><li><strong>Buckets:</strong> general purpose, rock, light-material and high-dump buckets differ in price "
         "and in what the machine can load. Specify the bucket on the quote.</li><li><strong>Quick coupler and "
         "attachments:</strong> forks, grapples and snow pushers are financeable with the loader when they are on the "
         "same quote. Bought later, they are usually a separate small deal.</li><li><strong>Engine tier:</strong> new "
         "nonroad diesel engines are certified to EPA standards in "
         "<a href=\"https://www.ecfr.gov/current/title-40/chapter-I/subchapter-U/part-1039\" rel=\"noopener nofollow\" "
         "target=\"_blank\">40 CFR part 1039</a>; buyers working on public contracts sometimes face fleet emission "
         "requirements, so check before buying an older machine.</li></ul>\n</div>",
         None),
        ("Buying a Used Wheel Loader",
         "<div class=\"prose\">\n<p>Loaders leave quarries and recycling yards with hard hours on them. Many lenders "
         "commonly finance used loaders up to roughly 5-7 years old; older machines may need a larger down payment or "
         "a shorter term. Before you sign, check:</p><ul><li>Hour meter and service records, including fluid analysis "
         "on the transmission and axles</li><li>Articulation joint and loader linkage pins for play</li>"
         "<li>Tire condition and size, matched across the set</li><li>Bucket cutting edge and wear on the floor</li>"
         "<li>Whether a dealer or a private seller provides the bill of sale and serial number</li></ul>"
         "<p>More on age limits and inspections: <a href=\"/equipment-financing/articles/can-you-finance-used-equipment/\">can "
         "you finance used equipment</a>.</p>\n</div>",
         None),
        ("Lease, Loan or Seasonal Payments",
         "<div class=\"prose\">\n<ul><li><strong>Equipment loan or $1 buyout lease:</strong> you own the loader at the "
         "end. Fits a machine you will run until the tires and pins are on their second set.</li><li><strong>Fair "
         "market value lease:</strong> lower payment, return or upgrade at the end. Fits a high-hour application where "
         "you want a fresh machine on a cycle.</li><li><strong>Seasonal or skip payments:</strong> payments sized to "
         "the months you earn, common for aggregates, snow removal and agriculture.</li><li><strong>Rental purchase "
         "options:</strong> some dealers credit part of the rent toward a purchase; compare the total against a loan.</li></ul>"
         "<p>Purchased loaders and $1 buyout leases are generally depreciable and may qualify for Section 179 "
         "(<a href=\"https://www.irs.gov/publications/p946\" rel=\"noopener nofollow\" target=\"_blank\">IRS Publication 946</a>); "
         "confirm with your tax adviser. Compare structures on <a href=\"/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/\">equipment "
         "loan vs lease</a>.</p>\n</div>",
         None),
        ("Wheel Loader, Skid Steer or Backhoe?",
         "<div class=\"prose\">\n<p>Buy the machine for the work you do most weeks, not the busiest fortnight of the "
         "year. A loader that needs two passes to fill a truck costs operator time on every load.</p>\n</div>\n"
         + CHOOSE +
         "\n<div class=\"prose\">\n<p>Compare <a href=\"/equipment/skid-steers/\">skid steer financing</a> and "
         "<a href=\"/equipment/backhoes/\">backhoe financing</a> for the smaller machines.</p>\n</div>",
         None),
        ("Steps to Finance a Wheel Loader",
         "<div class=\"prose\">\n<ol><li><strong>Get a written quote</strong> with model, year, serial, hours, bucket "
         "and any coupler or tires.</li><li><strong>Show the work:</strong> tonnage, a site contract, or the machine "
         "being replaced.</li><li><strong>Gather the file:</strong> 3-6 months of bank statements, plus tax returns and "
         "a profit and loss statement at larger tickets.</li><li><strong>Compare offers</strong> on total cost and the "
         "payoff at year three, not only the payment.</li><li><strong>Confirm insurance</strong> and the loss-payee "
         "wording before funding day.</li></ol><p>Credit commonly starts around 600, with the best terms at 680+; see "
         "<a href=\"/equipment-financing/articles/what-credit-score-needed-equipment-financing/\">credit needed for "
         "equipment financing</a>. Own a loader outright? See <a href=\"/heavy-equipment-equity-loan.html\">borrowing "
         "against equipment you own</a>.</p>\n</div>",
         "Apply for Wheel Loader Financing"),
    ],
    "faqs": [
        ("How much is a wheel loader payment?",
         f"At a typical 8%, a $150,000 loader is about {usd(pmt(150000, RATE, 60))} a month over 60 months and a "
         f"$325,000 loader about {usd(pmt(325000, RATE, 84))} over 84 months. These are illustrations, not quotes."),
        ("Can you finance a used wheel loader?",
         "Yes. Many lenders commonly finance used loaders up to roughly 5-7 years old. Hours, service records, "
         "transmission and axle condition and the tires matter more than the year."),
        ("Can tires and buckets be included in wheel loader financing?",
         "Usually, if they are on the same quote as the machine. Tires, buckets, a quick coupler and forks bought "
         "later are normally a separate deal."),
        ("What credit score do you need to finance a wheel loader?",
         "Most lenders look for about 600 or higher, with the best terms commonly at 680+. A site contract, strong "
         "bank deposits or a larger down payment can offset a lower score."),
        ("Can a quarry get seasonal payments on a loader?",
         "Often, yes. Some equipment lenders offer payment plans that skip or reduce slow months for aggregates, snow "
         "removal and agriculture. Ask for the total cost of the seasonal plan against a level one."),
        ("Is it better to lease or buy a wheel loader?",
         "A fair market value lease suits a high-hour machine you plan to replace on a cycle. A loan or $1 buyout "
         "lease suits a loader you will keep for many years. Compare the total cost of each."),
    ],
    "sources": [
        ("https://www.ecfr.gov/current/title-30/section-56.14130",
         "MSHA 30 CFR 56.14130", "Rollover protective structures and seat belts for wheel loaders at surface mines."),
        ("https://www.ecfr.gov/current/title-30/section-56.14100",
         "MSHA 30 CFR 56.14100", "Pre-shift examination of self-propelled mobile equipment and correction of defects."),
        ("https://www.ecfr.gov/current/title-40/chapter-I/subchapter-U/part-1039",
         "EPA 40 CFR part 1039", "Emission standards for new nonroad compression-ignition (diesel) engines."),
        ("https://www.irs.gov/publications/p946", "IRS Publication 946",
         "Depreciation and the Section 179 deduction for business equipment."),
    ],
    "headline": "Wheel Loader Financing: Rates, Payments and Terms",
    "article_desc": "Financing wheel loaders: prices by size class, payments by price and term, quarry and aggregate "
                    "deals, tires and buckets, used-loader checks and lease or seasonal structures.",
}
