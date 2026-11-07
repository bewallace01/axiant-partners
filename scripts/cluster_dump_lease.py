# -*- coding: utf-8 -*-
"""Dump truck lease vs loan - new spoke, from the 2026-11-07 daily batch.

Search Console, Oct 7 to Nov 4 2026: "dump truck lease" 41 impressions at position 51 on the
/equipment/dump-trucks/ hub, which only mentions leases. Prices, terms and resale (50-70% after
5 years) reuse that hub; TRAC residuals of 20-40% of cost come from the site's TRAC page (linked,
not edited). Read 2026-11-07: 26 USC 4051 (12% excise tax) and IRS Form 2290 (55,000 lb). About
TRAC, excise tax and vocational wear, so its substance differs from the cargo van page. no_hub.
"""
from cluster_table import table

FET = ("https://www.law.cornell.edu/uscode/text/26/4051",
       "26 U.S.C. 4051: Imposition of tax on heavy trucks",
       "The 12% federal excise tax on the first retail sale of truck chassis and bodies over 33,000 lb gross vehicle weight.")
HVUT = ("https://www.irs.gov/forms-pubs/about-form-2290",
        "IRS: About Form 2290",
        "The heavy highway vehicle use tax on vehicles with a taxable gross weight of 55,000 lb or more.")
UCC = ("https://www.law.cornell.edu/ucc/1/1-203",
       "UCC 1-203: Lease distinguished from security interest",
       "How the law separates a true lease from a financing, including nominal purchase options.")

CLUSTER = {
    "pillar": "equipment/dump-trucks/",
    "hub": "equipment/dump-trucks",
    "no_hub": True,
    "back_href": "/equipment/dump-trucks/",
    "crumb": "Dump Truck Financing",
    "cta_inline": "Compare dump truck loan and lease offers",
    "cta_button": "Get Matched for Dump Truck Financing",
}

ARTICLES = [{
    "slug": "dump-truck-lease-vs-loan",
    "crumb": "Dump Truck Lease vs Loan",
    "title": "Dump Truck Lease vs Loan: TRAC Lease Math | Axiant",
    "og_title": "Dump Truck Lease vs Loan: TRAC Leases, Payments and Risk",
    "h1": "Dump Truck Lease vs Loan: TRAC Leases, Payments and Risk",
    "headline": "Dump Truck Lease vs Loan: TRAC Leases, Payments and Risk",
    "lede": "A dump truck lease is usually a TRAC lease, which means the residual risk stays with you. Here is the math "
            "on a $150,000 tandem",
    "meta_desc": "Dump truck lease vs loan: on a $150,000 tandem, about $3,041 a month on a loan vs $2,327-$2,633 on a TRAC lease, but you still owe the residual. See the math.",
    "article_desc": "How a dump truck TRAC lease compares with an equipment loan, including payments, the residual you "
                    "guarantee, excise tax and vocational wear.",
    "keywords": "dump truck lease, dump truck lease vs loan, trac lease dump truck, lease a dump truck, dump truck lease payment",
    "quick_answer": "On a <strong>$150,000</strong> tandem at an illustrative 8% over 60 months, a loan runs about "
                    "<strong>$3,041</strong> a month and a TRAC lease about <strong>$2,327-$2,633</strong>, depending on the "
                    "residual. The catch: on a TRAC lease you generally stand behind that residual when the term ends. Axiant "
                    "Partners, a business-loan broker in Boca Raton, compares dump truck lenders and lessors. Typical rates "
                    "run 6-15%, so these are examples, not quotes.",
    "sections": [
        ("How Dump Truck Leases Usually Work",
         "<p>When a hauler says “lease” it usually means a TRAC lease, or terminal rental adjustment clause. It sets a residual "
         "up front, and only the rest is paid down during the term. At the end, the truck is typically sold or bought. If it "
         "sells for less than the residual, you cover the difference; if it sells for more, the surplus generally comes back "
         "to you. Our <a href=\"/equipment-financing/articles/trac-lease-benefits-saves-money/\">TRAC lease guide</a> covers the "
         "structure in general, with residuals of about 20-40% of cost.</p>"
         + table(["", "Equipment loan", "TRAC lease", "FMV lease"], [
             ["Monthly payment", "Highest", "Lower", "Often lowest, when offered"],
             ["Who carries resale risk", "You", "You, through the residual", "Mostly the lessor"],
             ["Balance at end", "None", "The residual", "None, if you return it"],
             ["Hours and wear", "Your problem at resale", "Hits your residual", "Return standards apply"],
             ["Best fit", "Keep it for its life", "Replace every few years", "Light use, rarely available"],
         ])
         + "<p>Many lessors are cautious about a true walk-away lease on a truck that spends its life on rough ground, which is "
         "why TRAC is the usual offer.</p>"),
        ("Worked Example: The Math on a $150,000 Tandem",
         "<p><strong>Illustrative, not a quote.</strong> A $150,000 tandem, inside the $120,000-$180,000 we list for tandems on "
         "our <a href=\"/equipment/dump-trucks/\">dump truck financing</a> page, with nothing down, 8% and 60 months.</p>"
         + table(["Structure", "Monthly", "Paid over 60 months", "Owed at the end", "Total"], [
             ["Loan", "About $3,041", "About $182,490", "$0", "About $182,490"],
             ["TRAC, 20% residual", "About $2,633", "About $157,990", "$30,000", "About $187,990"],
             ["TRAC, 35% residual", "About $2,327", "About $139,620", "$52,500", "About $192,120"],
         ])
         + "<p>A bigger residual saves more each month and costs more overall. The higher payment on the loan buys ownership with "
         "nothing left to settle. Compare the result to what a truck might be worth: we note that vocational chassis often hold "
         "50-70% of value after five years, which would put $75,000-$105,000 against those residuals if yours holds up, and a "
         "well-kept truck would leave a surplus. Poorly kept ones are the risk.</p>"),
        ("Why Vocational Wear Changes the Risk",
         "<p>A dump truck isn't a highway tractor, and its resale value depends on things a mileage reading can't show:</p>"
         "<ul>"
         "<li><strong>Engine hours.</strong> These trucks idle on site, so hours often say more than the odometer.</li>"
         "<li><strong>Body and hoist.</strong> Abrasive loads wear floors, sidewalls and hydraulics, which buyers check.</li>"
         "<li><strong>Frame and suspension.</strong> Overloading and off-road use show up here at inspection.</li>"
         "<li><strong>Axle configuration.</strong> Bridge laws and local demand affect who can buy a given truck.</li>"
         "</ul>"
         "<p>On a TRAC lease all of that lands on you at the end, so a low residual is the safer choice if your work is hard on "
         "trucks. Keep service records in one place. They support the sale whichever structure you pick.</p>"),
        ("Excise Tax and Road Tax",
         "<p>Two federal taxes matter on larger trucks, so ask how each offer treats them.</p>"
         + table(["Tax", "What it is", "What to ask"], [
             ["Federal excise tax", "12% on the first retail sale of truck chassis and bodies over 33,000 lb GVW", "Is it in the price being financed or leased?"],
             ["Heavy vehicle use tax", "Form 2290 for vehicles with a taxable gross weight of 55,000 lb or more", "Who files and pays during the lease?"],
         ])
         + "<p>On a new $150,000 truck the excise tax can be a large line, so it has to appear in the quote you compare. See "
         '<a href="https://www.law.cornell.edu/uscode/text/26/4051" rel="noopener nofollow" target="_blank">26 U.S.C. 4051</a> and '
         '<a href="https://www.irs.gov/forms-pubs/about-form-2290" rel="noopener nofollow" target="_blank">IRS Form 2290</a>. '
         "Lease and loan payments are deducted differently, and a lease with a nominal buyout may be treated as a purchase, so "
         "ask your CPA before you choose for tax reasons alone. "
         '<a href="https://www.law.cornell.edu/ucc/1/1-203" rel="noopener nofollow" target="_blank">UCC 1-203</a> sets out the '
         "legal test for a true lease.</p>"),
        ("Matching the Structure to Your Work",
         "<ul>"
         "<li><strong>Seasonal hauling.</strong> A lower TRAC payment helps in winter, but the residual is still due. Ask about seasonal "
         "payment schedules on either structure.</li>"
         "<li><strong>A long site-work contract.</strong> If the job lasts three years and the truck stays busy after that, a loan builds "
         "equity you can use later, including by "
         '<a href="/commercial-truck-title-loan/articles/dump-truck-title-loan/">borrowing against a dump truck you own</a>.</li>'
         "<li><strong>Growing fleet.</strong> A lease may keep payments down while you add units, but each residual is a future bill, so "
         "track them together.</li>"
         "<li><strong>New company.</strong> Expect more down or a cosigner on either one. Start with "
         '<a href="/equipment/dump-trucks/used-dump-truck-financing/">used dump truck financing</a> if a new unit is out of reach.</li>'
         "</ul>"
         "<p>Keep operating costs separate: use "
         '<a href="/working-capital-loans.html">working capital</a> for fuel and payroll, and the equipment structure for the truck.</p>'),
        ("Questions to Ask Before You Sign",
         "<ol>"
         "<li><strong>Is the residual a guarantee?</strong> Ask what you owe if the truck sells below it.</li>"
         "<li><strong>Who sets the sale price?</strong> Find out how the end-of-term value is determined.</li>"
         "<li><strong>What are the end options?</strong> Buy, sell, refinance or roll into another truck.</li>"
         "<li><strong>What's in the amount financed?</strong> Excise tax, body, hoist and any upfit.</li>"
         "<li><strong>What happens if you exit early?</strong> Get the early-termination formula in writing.</li>"
         "<li><strong>What's the total?</strong> Add every payment, the residual and fees.</li>"
         "</ol>"
         '<p>Then <a href="/match.html">get matched</a> and compare a loan and a lease on the same truck. For related work see '
         '<a href="/construction-business-financing.html">construction business financing</a>. Credit and terms vary by lender, '
         "and most start around 600 credit with 0-20% down.</p>"),
    ],
    "faqs": [
        ("Is it better to lease or buy a dump truck?",
         "Buy if you'll keep it for most of its life, since a loan ends with no balance. A TRAC lease lowers the payment if you replace "
         "trucks every few years, but you generally stand behind the residual. In our $150,000 example, a 20% residual costs about "
         "$5,500 more overall than the loan."),
        ("How much is a dump truck lease per month?",
         "In one illustration, a $150,000 tandem at 8% over 60 months is about $2,633 with a 20% residual and about $2,327 with a 35% "
         "residual. Those are examples, not quotes."),
        ("What is a TRAC lease on a dump truck?",
         "It's a lease with a preset residual at the end. If the truck sells for less, you generally pay the difference. If it sells "
         "for more, the surplus generally goes to you."),
        ("Can I just return a leased dump truck?",
         "On a TRAC lease, not without settling the residual. A true fair market value lease allows a return, subject to wear standards, "
         "but those are less common on trucks used this hard."),
        ("Does the 12% excise tax apply to a dump truck?",
         "It applies to the first retail sale of truck chassis and bodies suited to a gross vehicle weight over 33,000 lb, which covers "
         "many tandems and tri-axles. Ask whether it's already in the price."),
        ("Can a new company lease a dump truck?",
         "Sometimes, but usually with more down, a cosigner or strong personal credit. Used trucks and smaller units can be easier to place."),
    ],
    "related": [
        ("/equipment/dump-trucks/", "Dump truck financing"),
        ("/equipment/dump-trucks/used-dump-truck-financing/", "Used dump truck financing"),
        ("/equipment-financing/articles/trac-lease-benefits-saves-money/", "TRAC lease benefits"),
        ("/commercial-truck-title-loan/articles/dump-truck-title-loan/", "Dump truck title loans"),
        ("/construction-business-financing.html", "Construction business financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [FET, HVUT, UCC],
}]
