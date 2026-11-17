# -*- coding: utf-8 -*-
"""Tractor financing - /equipment/tractors/ rewritten, daily batch 2026-11-14.

Search Console Oct 15 - Nov 11 2026: "tractor financing" 64 impressions at position 75
(54 on this page, 10 on the old new-farmers spoke, which was 301'd here in May), plus
tractor loans 17 at 46, tractor loan 13 at 64, tractor leasing 12 at 36, used tractor
financing 11 at 39, where to get tractor financing, tractor lease rates/cost, tractor loan
rates, how long can you finance a tractor for, compact tractor loans. The old template
answered none of these directly.

Numbers: price ranges are the ones this page already published (new $80K-$150K utility and
compact row-crop 80-150 HP, $150K-$400K+ large row-crop; used $25K-$200K), terms 36-84
months, credit 550+ and 6-15% typical rates are the page's published ranges. Payments are
computed by pmt() at an assumed 8%, stated as an illustration. FSA facts read from the eCFR:
7 CFR 761.8 (direct operating $400,000, direct farm ownership $600,000, guaranteed limits
indexed to the Prices Paid by Farmers Index), 764.251(a)(2) (operating loans may buy farm
equipment), 764.254 (term operating loans: useful life of the security or 7 years, whichever
is less). SBA maturity from 13 CFR 120.212 (10 years unless the asset's useful life is longer,
25-year cap). Removed: unsourced resale claims ("brands hold value"), "30-50% less used".
No named lenders or dealer programs.
"""
from equipment_rewrite import pmt, pay_row, table, usd

RATE = 8.0


def annual(principal, apr_pct, years):
    r = apr_pct / 100
    return principal * r / (1 - (1 + r) ** -years)


EX_PRICE, EX_DOWN = 160_000, 24_000
EX_FIN = EX_PRICE - EX_DOWN
EX_MO = pmt(EX_FIN, RATE, 72)
EX_YR = annual(EX_FIN, RATE, 6)

PAGE = {
    "path": "equipment/tractors/index.html",
    "date": "2026-11-14",
    "date_text": "November 14, 2026",
    "title": "Tractor Financing: Loans, Leases, Rates and Terms | Axiant",
    "og_title": "Tractor Financing: Loans, Leases, Rates and Terms | Axiant",
    "desc": (f"Tractor financing for farms and ag businesses: typical 36-84 month terms, payments from "
             f"{usd(pmt(90_000, RATE, 72))} a month, used tractors, annual payments, dealer offers and FSA loans."),
    "headline": "Tractor Financing: Loans, Leases, Rates and Terms",
    "article_desc": ("Financing farm tractors: typical prices and terms, payments by price, used tractors, "
                     "annual and seasonal payment schedules, dealer promotions, leases and FSA loans."),
    "h1": "Tractor Financing: Loans, Leases &amp; Farm Loan Programs",
    "lede": ("New tractors typically cost $80,000-$400,000+ and used ones $25,000-$200,000. Finance one with "
             "an equipment loan or lease, with payments that can follow harvest. Decisions in 24-48 hours "
             "for qualified applications."),
    "checks": [
        "Equipment financing decisions in 24-48 hours",
        "New and used row-crop, utility and compact tractors",
        "Monthly, seasonal or annual payment schedules",
        "Typical terms 36-84 months; credit 550+",
    ],
    "intro": ('<p>This page is about financing farm tractors: utility, row-crop and compact. Combines, sprayers '
              'and harvest equipment are on <a href="/equipment-financing/articles/agricultural-equipment-financing-tractors-combines/">'
              'agricultural equipment financing</a>, and operating money for the season is on '
              '<a href="/agriculture-business-financing.html">agriculture business financing</a>.</p>'),
    "quick_answer": (f"As of November 2026, tractor financing commonly runs 36-84 months with 0-20% down and "
                     f"credit from about 550, and many lenders will bill once or twice a year around harvest. "
                     f"New utility and compact row-crop tractors typically cost $80,000-$150,000 and large "
                     f"row-crop units $150,000-$400,000+. At an assumed 8%, $90,000 over 72 months is about "
                     f"<strong>{usd(pmt(90_000, RATE, 72))} a month</strong> and $150,000 over 84 months about "
                     f"<strong>{usd(pmt(150_000, RATE, 84))}</strong>. Axiant Partners, a business-loan broker in "
                     f"Boca Raton, compares equipment lenders. Typical ranges, not a quote."),
    "qa_link": "Get matched for tractor financing",
    "glance_h2": "Tractor Financing at a Glance",
    "glance": [("$25K-$400K+", "New and used range"), ("24-48 hr", "Equipment approval"),
               ("36-84 mo", "Typical terms"), ("0-20%", "Down payment"),
               ("550+", "Credit (typical)"), ("Annual", "Payments can follow harvest")],
    "sections": [
        ("Tractor Prices by Class",
         '<div class="prose">\n<p>Typical prices before tax, freight and implements. They are the ranges this page '
         'publishes, not quotes; horsepower, cab, transmission and precision guidance move a tractor across them.</p>\n</div>\n'
         + table(["Tractor", "Typical price"], [
             ["Utility or compact row-crop", "$80,000-$150,000 new (80-150 HP)"],
             ["Large row-crop", "$150,000-$400,000+ new (200-600+ HP)"],
             ["Used, any class", "$25,000-$200,000"],
         ])
         + '\n<div class="prose">\n<p>Loaders, mowers, balers and planters bought with the tractor can usually ride on '
         'the same approval if they are on the same invoice. Bought later, each is its own deal.</p>\n</div>', None),
        ("Tractor Payments by Price and Term",
         f'<div class="prose">\n<p>Illustrative monthly payments at an assumed {RATE:.0f}% before tax and fees, computed by '
         'formula. Typical equipment rates run about 6-15% depending on credit, age of the tractor and down payment.</p>\n</div>\n'
         + table(["Amount financed", "Term", "About per month", "Total interest"], [
             pay_row(40_000, RATE, 60), pay_row(90_000, RATE, 72), pay_row(150_000, RATE, 84),
             pay_row(250_000, RATE, 84)])
         + '\n<div class="prose">\n<p>Run your own numbers in the <a href="/equipment-financing/articles/farm-equipment-financing-calculator/">'
         'farm equipment financing calculator</a>.</p>\n</div>', None),
        ("Monthly, Seasonal or Annual Payments",
         '<div class="prose">\n<p>A grain or cattle operation that gets paid a few times a year does not have to carry a '
         'payment in the months it has no income. Ag lenders commonly offer:</p>\n<ul>'
         '<li><strong>Annual payments</strong>, due after the main harvest or calf sale.</li>'
         '<li><strong>Semi-annual payments</strong> for two crops or spring and fall sales.</li>'
         '<li><strong>Skip-month schedules</strong> that pause payments in the slow months.</li>'
         '<li><strong>Deferred first payment</strong>, so a tractor bought in spring is first paid for at harvest.</li></ul>'
         f'<p>An annual schedule costs a little more interest than monthly, because principal is paid down later. '
         f'Bring a year of deposits or sales receipts so the lender can see when the money arrives.</p>\n</div>',
         "Ask for a Harvest-Based Schedule"),
        ("Worked Example: A Used 200 HP Tractor",
         f'<div class="prose">\n<p><strong>Illustrative, not a quote.</strong> A row-crop farm replaces a high-hour tractor '
         f'with a used 200 HP unit priced at {usd(EX_PRICE)}. It puts 15% ({usd(EX_DOWN)}) down and finances '
         f'{usd(EX_FIN)} at an assumed {RATE:.0f}% over six years.</p><ul>'
         f'<li>Monthly over 72 months: about <strong>{usd(EX_MO)}</strong> a month, {usd(EX_MO * 72 - EX_FIN)} total interest</li>'
         f'<li>Annual over 6 payments after harvest: about <strong>{usd(EX_YR)}</strong> a year, {usd(EX_YR * 6 - EX_FIN)} total interest</li></ul>'
         '<p>The annual plan costs more interest but leaves cash in the bank from planting to harvest. The choice '
         'depends on when the farm is paid, not on which payment looks smaller.</p>\n</div>', None),
        ("Financing a Used Tractor",
         '<div class="prose">\n<ul>'
         '<li><strong>Age and hours:</strong> many lenders commonly finance used tractors up to about 7-10 years old. '
         'Hours tell the lender more than the model year; a low-hour older tractor can finance better than a worn newer one.</li>'
         '<li><strong>Term follows life:</strong> the older the tractor, the shorter the term a lender will offer.</li>'
         '<li><strong>Private sales and auctions:</strong> lenders want a bill of sale, the serial number, a lien search '
         'and often photos or an inspection. Auction purchases usually need the approval in place before bidding.</li>'
         '<li><strong>Check the drivetrain:</strong> engine, transmission, hydraulics and PTO. Repairs after funding are yours.</li>'
         '</ul>\n<p>More on older machines: <a href="/equipment-financing/articles/can-you-finance-used-equipment/">can you finance used equipment</a>.</p>\n</div>', None),
        ("Dealer Promotions vs a Bank or Equipment Lender",
         '<div class="prose">\n<p>New tractors are often sold with promotional financing from the manufacturer&rsquo;s '
         'finance arm, sometimes at low or zero rates for set terms. Before taking it:</p><ul>'
         '<li><strong>Ask for the cash price.</strong> Some promotions are offered in place of a cash discount or rebate, '
         'so the &ldquo;free&rdquo; rate is paid for in the price.</li>'
         '<li><strong>Compare total cost</strong>: the rebate plus an outside loan against the promotional rate.</li>'
         '<li><strong>Check what the promotion covers.</strong> Promotions usually apply to new units only; used '
         'tractors, mixed-brand implements and private sales are where a bank or independent equipment lender fits.</li>'
         '<li><strong>Watch the blanket lien.</strong> Some farm lenders take a lien on all equipment; a tractor-only '
         'lien keeps the rest of the fleet free to borrow against.</li></ul>\n</div>', None),
        ("Lease or Loan for a Tractor",
         '<div class="prose">\n<ul>'
         '<li><strong>Loan or $1 buyout lease:</strong> you own the tractor at the end. Fits a tractor you will run for '
         'many seasons.</li>'
         '<li><strong>Fair market value lease:</strong> lower payments and a return or trade at the end, with hour '
         'limits; extra hours are billed. Fits operations that trade every few years.</li>'
         '<li><strong>Seasonal rental:</strong> for a few weeks of extra capacity, renting can cost less than owning.</li></ul>'
         '<p>Purchased tractors and $1 buyout leases are generally depreciable, and some may qualify for Section 179 '
         '(<a href="https://www.irs.gov/publications/p946" rel="noopener nofollow" target="_blank">IRS Publication 946</a>); '
         'farm property has its own depreciation rules, so confirm with your tax adviser. See '
         '<a href="/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/">equipment loan vs lease</a>.</p>\n</div>', None),
        ("How Long Can You Finance a Tractor?",
         '<div class="prose">\n'
         + table(["Source", "Typical or maximum term"], [
             ["Equipment loan or lease", "Commonly 36-84 months"],
             ["FSA operating term loan", "Useful life or 7 years, whichever is less"],
             ["SBA 7(a)", "Up to 10 years; longer only for longer-life assets"],
         ])
         + '<p>FSA terms come from <a href="https://www.ecfr.gov/current/title-7/section-764.254" '
         'rel="noopener nofollow" target="_blank">7 CFR 764.254</a>; SBA maturities from '
         '<a href="https://www.ecfr.gov/current/title-13/section-120.212" '
         'rel="noopener nofollow" target="_blank">13 CFR 120.212</a>. A longer term lowers the payment and raises the '
         'total interest, and it can leave you owing more than the tractor is worth late in the term.</p>\n</div>', None),
        ("FSA Farm Loans as an Alternative",
         '<div class="prose">\n<p>USDA&rsquo;s Farm Service Agency lends to family farms that cannot get enough credit '
         'elsewhere, and its operating loans may be used to buy farm equipment '
         '(<a href="https://www.ecfr.gov/current/title-7/section-764.251" '
         'rel="noopener nofollow" target="_blank">7 CFR 764.251</a>).</p><ul>'
         '<li><strong>Direct operating loans:</strong> up to $400,000; direct farm ownership loans up to $600,000 '
         '(<a href="https://www.ecfr.gov/current/title-7/section-761.8" '
         'rel="noopener nofollow" target="_blank">7 CFR 761.8</a>).</li>'
         '<li><strong>Guaranteed loans</strong> are made by a bank with an FSA guarantee; their limits are raised each '
         'year with the Prices Paid by Farmers Index.</li>'
         '<li><strong>Trade-off:</strong> FSA terms can be attractive, but approval takes longer than an equipment '
         'lender&rsquo;s 24-48 hours, so it suits a planned purchase rather than a breakdown in planting season.</li></ul>\n</div>', None),
        ("Compact Tractors for Landscapers and Small Operations",
         '<div class="prose">\n<p>Landscapers, nurseries, horse farms and property-maintenance companies finance compact '
         'tractors with loaders and mowers as business equipment. Lenders look at the business&rsquo;s revenue rather than '
         'farm income, and the smaller ticket usually means a lighter file. Financing on this site is for business use '
         'only; a tractor for a personal property is a consumer purchase. Related: '
         '<a href="/equipment/skid-steers/">skid steer financing</a>.</p>\n</div>', None),
        ("Steps to Finance a Tractor",
         '<div class="prose">\n<ol><li><strong>Get a written quote</strong> with serial, hours and any implements listed.</li>'
         '<li><strong>Gather the file:</strong> 3-6 months of bank statements and, on larger deals, tax returns with Schedule F.</li>'
         '<li><strong>Pick a payment schedule</strong> that matches when you are paid.</li>'
         '<li><strong>Compare the dealer promotion</strong> with an outside offer on total cost.</li>'
         '<li><strong>Confirm insurance</strong> and the lien terms before funding.</li></ol>'
         '<p>Axiant sends one application to lenders that finance farm equipment.</p>\n</div>', "Apply for Tractor Financing"),
    ],
    "faq_h2": "Tractor Financing FAQ",
    "faqs": [
        ("How much is the payment on a financed tractor?",
         f"It depends on the price, rate and term. At an assumed 8%, $90,000 over 72 months is about "
         f"{usd(pmt(90_000, RATE, 72))} a month and $150,000 over 84 months about {usd(pmt(150_000, RATE, 84))}. "
         "These are illustrations, not quotes."),
        ("How long can you finance a tractor for?",
         "Equipment loans and leases commonly run 36-84 months. FSA operating term loans run the useful life of "
         "the tractor or 7 years, whichever is less, and SBA 7(a) loans can reach 10 years."),
        ("Can you finance a used tractor?",
         "Yes. Many lenders commonly finance used tractors up to about 7-10 years old. Hours and condition matter "
         "more than the year, and older tractors get shorter terms."),
        ("Can tractor payments be made once a year?",
         "Often, yes. Ag lenders commonly offer annual or semi-annual payments timed to harvest or livestock sales. "
         "An annual schedule costs somewhat more interest than monthly."),
        ("Is 0% dealer financing on a tractor a good deal?",
         "Sometimes. Promotions may replace a cash rebate, so compare the rebate plus an outside loan against the "
         "promotional rate on total cost. Promotions usually apply to new tractors only."),
        ("What credit score do you need for tractor financing?",
         "Many lenders look for about 550 or higher, with the best terms commonly at 680+. Farm income history and "
         "a larger down payment can offset a lower score."),
    ],
    "sources": [
        ("https://www.ecfr.gov/current/title-7/section-761.8",
         "7 CFR 761.8", "FSA loan limits: direct operating, direct farm ownership and indexed guaranteed limits."),
        ("https://www.ecfr.gov/current/title-7/section-764.251",
         "7 CFR 764.251", "Permitted uses of FSA operating loans, including farm equipment."),
        ("https://www.ecfr.gov/current/title-7/section-764.254",
         "7 CFR 764.254", "FSA operating loan terms: useful life of the security or 7 years."),
        ("https://www.ecfr.gov/current/title-13/section-120.212",
         "13 CFR 120.212", "Maximum maturities for SBA business loans."),
        ("https://www.irs.gov/publications/p946", "IRS Publication 946",
         "Depreciation and the Section 179 deduction for business equipment."),
    ],
    "drop": ["In-Depth "],
}
