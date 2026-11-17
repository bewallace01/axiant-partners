# -*- coding: utf-8 -*-
"""/equipment/backhoes/ - daily batch 2026-11-14 (render: scripts/equipment_rewrite.py).

Search Console, Oct 15 - Nov 11 2026: "backhoe financing" 23 impressions at position 69 land
on construction-heavy-equipment-financing (in the excavator split, not edited), not here;
this page is the natural owner. The old template was 44% shared with /equipment/wheel-loaders/
(simscan). Rewritten around backhoe questions: price by class, utility and municipal work,
trench protection bought with the machine (OSHA 29 CFR 1926.652), title-less collateral and
the UCC financing statement (UCC 9-502), options and attachments, used-backhoe checks, backhoe
vs mini excavator plus skid steer.

Prices are the ranges this page already published (compact $50-80K, full-size $120-180K+),
framed as typical. Removed: "50-70% of value after 5 years" (no source). Payments by pmt() at
an illustrative 8%. OSHA 1926.652(a)(1) (protective systems at 5 feet, stable rock excepted)
and UCC 9-502 read from Cornell LII / osha.gov. No named lenders or quotes.
"""
from equipment_rewrite import pay_row, pmt, table, usd

RATE = 8
mach, box = 126000, 9000  # machine and trench shield on one quote (assumptions, stated on page)
ex_fin = mach + box
ex_pmt = pmt(ex_fin, RATE, 60)
CONTRACT_MO = 7  # assumed months of work on the awarded contract

PAY = table(["Amount financed", "Term", "About per month", "Total interest"],
            [pay_row(60000, RATE, 48), pay_row(100000, RATE, 60), pay_row(150000, RATE, 60),
             pay_row(150000, RATE, 72)])

PRICES = table(["Class", "Typical use", "Typical new price"], [
    ["Compact backhoe", "Landscaping, small utility", "$50,000-$80,000"],
    ["Standard backhoe", "General contracting", "Between the two"],
    ["Full-size backhoe", "Utility, municipal, deep trench", "$120,000-$180,000+"],
])

OPTIONS = table(["Option", "Why buyers add it"], [
    ["Extendable dipper", "More dig depth and reach"],
    ["Four-wheel drive", "Traction on wet or soft sites"],
    ["Pilot controls", "Operator comfort on long days"],
    ["Hydraulic thumb", "Grabbing pipe, rock and debris"],
    ["Hammer circuit", "Running a breaker on concrete"],
])

PAGE = {
    "path": "equipment/backhoes/index.html",
    "date": "2026-11-14",
    "date_text": "November 14, 2026",
    "title": "Backhoe Financing: Payments, Terms and Used Units | Axiant",
    "og_title": "Backhoe Financing: Payments, Terms and Used Units | Axiant",
    "desc": (f"Backhoe loader financing: prices by class, payments from {usd(pmt(100000, RATE, 60))} a month, "
             "utility and trench work, options and attachments, used backhoes, lease or loan."),
    "h1": "Backhoe Financing: Loans and Leases for Utility and Site Contractors",
    "lede": "Backhoe loaders typically cost $50,000-$180,000+ new, depending on class and options. Finance the "
            "machine, its attachments and trench protection together. Decisions in 24-48 hours for qualified applications.",
    "checks": ["Equipment financing decisions in 24-48 hours",
               "New and used backhoe loaders and attachments",
               "Typical terms 36-72 months; SBA to 10+ years",
               "Credit 600+; 0-20% down payment"],
    "intro": ("<p>This page is about financing backhoe loaders: a loader bucket on the front and a digging arm on "
              "the back. Loading-only machines are on <a href=\"/equipment/wheel-loaders/\">wheel loader financing</a>, "
              "compact diggers on <a href=\"/equipment/mini-excavators/\">mini excavator financing</a>, and every "
              "construction product on <a href=\"/construction-business-financing.html\">construction business "
              "financing</a>.</p>"),
    "quick_answer": ("As of November 2026, backhoe financing commonly runs 36-72 months with 0-20% down and 600+ "
                     "credit, secured by the machine. Compact backhoes typically cost $50,000-$80,000 new and "
                     "full-size units $120,000-$180,000+. At a typical 8%, a $100,000 backhoe is about "
                     f"<strong>{usd(pmt(100000, RATE, 60))} a month</strong> over 60 months, and a $150,000 machine "
                     f"about <strong>{usd(pmt(150000, RATE, 72))}</strong> over 72. Axiant Partners, a business-loan "
                     "broker in Boca Raton, compares equipment lenders. Typical ranges, not a quote."),
    "qa_link": "Get matched for backhoe financing",
    "glance_h2": "Backhoe Financing at a Glance",
    "glance": [("$50K-$180K+", "Typical new range"), ("24-48 hr", "Equipment approval"),
               ("36-72 mo", "Terms"), ("0-20%", "Down payment"), ("600+", "Credit (typical)"),
               ("50 states", "Nationwide")],
    "faq_h2": "Backhoe Financing FAQ",
    "sections": [
        ("Backhoe Prices by Class",
         "<div class=\"prose\">\n<p>Typical new prices before tax, freight and attachments, as this page has published "
         "them. Dig depth, drive and options decide where a machine lands.</p>\n</div>\n" + PRICES +
         "\n<div class=\"prose\">\n<p>Used backhoes sell across a wide range by hours and condition, so a lender works "
         "from the listing or an appraisal of the specific machine.</p>\n</div>",
         None),
        ("Backhoe Payments by Price and Term",
         f"<div class=\"prose\">\n<p>Illustrative payments at {RATE}% before tax and fees, computed by formula:</p>\n</div>\n"
         + PAY + "\n<div class=\"prose\">\n<p>Run other amounts in the <a href=\"/calculator.html\">financing "
         "calculator</a>.</p>\n</div>",
         None),
        ("Worked Example: A Backhoe for a Water Line Contract",
         f"<div class=\"prose\">\n<p><strong>Illustrative, not a quote.</strong> A utility contractor wins a municipal "
         f"water line replacement and quotes a {usd(mach)} full-size backhoe with a {usd(box)} trench shield on the same "
         f"invoice. It finances {usd(ex_fin)} with no money down at {RATE}% over 60 months.</p><ul>"
         f"<li>Monthly payment: about <strong>{usd(ex_pmt)}</strong></li>"
         f"<li>Total interest over the term: about {usd(ex_pmt * 60 - ex_fin)}</li>"
         f"<li>Payments during an assumed {CONTRACT_MO}-month contract: about {usd(ex_pmt * CONTRACT_MO)}</li></ul>"
         "<p>The award letter and the bid schedule are the strongest documents in this file. They show the lender "
         "that the machine has work from the day it arrives, and that the contract covers the payments while it runs. "
         "Paid on monthly progress estimates? Add a plan for the gap between "
         "<a href=\"/construction-business-financing/progress-payment-cash-flow-gaps/\">progress payments</a>.</p>\n</div>",
         "Get Matched for Backhoe Financing"),
        ("Trench Protection on the Same Deal",
         "<div class=\"prose\">\n<p>Much backhoe work is trenching, and OSHA requires a protective system &mdash; "
         "sloping, shoring or a shield &mdash; for excavations 5 feet deep or more unless they are entirely in "
         "stable rock (<a href=\"https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652\" "
         "rel=\"noopener nofollow\" target=\"_blank\">29 CFR 1926.652</a>). Trench boxes and shoring are equipment "
         "too: quoted with the backhoe, they can usually go on the same approval instead of coming out of cash.</p>"
         "<p>Lenders also ask what kind of work the machine does. Utility, municipal and public works contracts "
         "read well because the payer is stable; private residential work reads fine with steady bank deposits.</p>\n</div>",
         None),
        ("No Title: How a Lender Takes the Backhoe as Collateral",
         "<div class=\"prose\">\n<p>Unlike a truck, a backhoe has no certificate of title. The lender perfects its "
         "interest by filing a UCC financing statement that describes the collateral "
         "(<a href=\"https://www.law.cornell.edu/ucc/9/9-502\" rel=\"noopener nofollow\" target=\"_blank\">UCC "
         "9-502</a>), usually by make, model and serial number. That is why the quote has to show the serial, and "
         "why a private-party seller should provide a bill of sale and proof that any earlier lien is released. "
         "More on liens: <a href=\"/equipment-financing/articles/equipment-financing-ucc-lien-approval/\">UCC liens "
         "and equipment financing approval</a>.</p>\n</div>",
         None),
        ("Options and Attachments That Change the Price",
         "<div class=\"prose\">\n<p>Two backhoes of the same class can be far apart in price because of how they "
         "are equipped. Put the options and attachments you need on the quote, so they are financed with the machine "
         "rather than bought later on a card.</p>\n</div>\n" + OPTIONS,
         None),
        ("Buying a Used Backhoe",
         "<div class=\"prose\">\n<p>Many lenders commonly finance used backhoes up to roughly 5-7 years old; older "
         "machines may need more down or a shorter term. Check before you buy:</p><ul><li>Hours and service "
         "records</li><li>Swing frame, king post and boom for cracks or welds</li><li>Pins and bushings on both ends "
         "for play</li><li>Stabilizer cylinders and pads</li><li>Extendable dipper wear, if fitted</li></ul>"
         "<p>See <a href=\"/equipment-financing/articles/can-you-finance-used-equipment/\">financing used "
         "equipment</a> for how lenders treat age and private sales.</p>\n</div>",
         None),
        ("One Backhoe or a Mini Excavator and Skid Steer?",
         "<div class=\"prose\">\n<p>A backhoe does two jobs with one operator, one trailer and one payment. A mini "
         "excavator plus a skid steer digs and loads better in tight spaces, but means two machines, often two "
         "trailers and two payments. Price both setups as monthly payments before you decide, using "
         "<a href=\"/equipment/mini-excavators/\">mini excavator</a> and <a href=\"/equipment/skid-steers/\">skid "
         "steer</a> financing. If you mainly load trucks, a <a href=\"/equipment/wheel-loaders/\">wheel loader</a> "
         "may be the better buy.</p>\n</div>",
         None),
        ("Steps to Finance a Backhoe",
         "<div class=\"prose\">\n<ol><li><strong>Quote the machine</strong> with serial, hours, options and any "
         "attachments or trench shield.</li><li><strong>Show the work:</strong> an award letter, a bid schedule or "
         "steady deposits.</li><li><strong>Gather the file:</strong> 3-6 months of bank statements, plus tax returns "
         "at larger tickets.</li><li><strong>Compare offers</strong> on total cost, not only the payment.</li>"
         "<li><strong>Confirm insurance</strong> and the loss payee before funding.</li></ol>"
         "<p>Purchased machines are generally depreciable and may qualify for Section 179 "
         "(<a href=\"https://www.irs.gov/publications/p946\" rel=\"noopener nofollow\" target=\"_blank\">IRS "
         "Publication 946</a>). Own a backhoe outright? See <a href=\"/heavy-equipment-equity-loan.html\">borrowing "
         "against equipment you own</a>.</p>\n</div>",
         "Apply for Backhoe Financing"),
    ],
    "faqs": [
        ("How much is the payment on a backhoe?",
         f"At a typical 8%, a $100,000 backhoe is about {usd(pmt(100000, RATE, 60))} a month over 60 months and a "
         f"$60,000 compact machine about {usd(pmt(60000, RATE, 48))} over 48 months. These are illustrations, not quotes."),
        ("Can you finance a used backhoe?",
         "Yes. Many lenders commonly finance used backhoes up to roughly 5-7 years old. Hours, the swing frame and "
         "boom, and the pins and bushings matter more than the year."),
        ("Can a trench box be financed with a backhoe?",
         "Usually, if it is on the same quote. Trench shields and shoring are equipment, and OSHA requires a "
         "protective system for most trenches 5 feet or deeper."),
        ("Why does a backhoe quote need the serial number?",
         "A backhoe has no title, so the lender files a UCC financing statement describing the machine, usually by "
         "serial number. A private seller should also show any earlier lien is released."),
        ("What credit score do you need for backhoe financing?",
         "Most lenders look for about 600 or higher, with the best terms commonly at 680+. An award letter, steady "
         "deposits or a down payment can offset a lower score."),
        ("Is a backhoe or a mini excavator easier to finance?",
         "Both are common equipment deals. A backhoe is one larger payment; a mini excavator plus a skid steer is "
         "two smaller ones. Compare the combined monthly cost for the work you do."),
    ],
    "sources": [
        ("https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652", "OSHA 29 CFR 1926.652",
         "Requirements for protective systems in excavations, including the 5-foot rule."),
        ("https://www.law.cornell.edu/ucc/9/9-502", "UCC 9-502",
         "Contents of a financing statement, which is how a lender perfects a lien on untitled equipment."),
        ("https://www.irs.gov/publications/p946", "IRS Publication 946",
         "Depreciation and the Section 179 deduction for business equipment."),
    ],
    "headline": "Backhoe Financing: Payments, Terms and Used Units",
    "article_desc": "Financing backhoe loaders: prices by class, payments by price and term, a utility contract "
                    "example, trench protection, UCC collateral, options and used-backhoe checks.",
}
