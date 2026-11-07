# -*- coding: utf-8 -*-
"""Cargo van lease vs loan - new spoke, from the 2026-11-07 daily batch.

Search Console, Oct 7 to Nov 4 2026: "cargo van lease" 32 impressions at position 58, "cargo van
lease to own" 23 at 28, "lease cargo van" 21 at 48, all on the /equipment/cargo-vans/ hub, which
gives leasing one paragraph. Prices, rates and terms reuse that hub ($35K-$75K, 6-15%, 24-72
months, 0-20% down). The 25% residual is an assumption labelled as one. Read 2026-11-07: UCC
1-203 and IRS Pub 946 (2025 edition). Not a dump truck or excavator page in new clothes: this one
is about upfit, return condition and lease-to-own. no_hub.
"""
from cluster_table import table

UCC = ("https://www.law.cornell.edu/ucc/1/1-203",
       "UCC 1-203: Lease distinguished from security interest",
       "Why a nominal purchase option generally makes a lease a security interest, and how a fair market value option differs.")
IRS = ("https://www.irs.gov/publications/p946", "IRS Publication 946",
       "Section 179 rules, including the vehicles excluded from the sport utility vehicle limit.")
FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "FTC guidance on misrepresented financing costs and terms offered to small businesses.")

CLUSTER = {
    "pillar": "equipment/cargo-vans/",
    "hub": "equipment/cargo-vans",
    "no_hub": True,
    "back_href": "/equipment/cargo-vans/",
    "crumb": "Cargo Van Financing",
    "cta_inline": "Compare van loan and lease offers",
    "cta_button": "Get Matched for Cargo Van Financing",
}

ARTICLES = [{
    "slug": "cargo-van-lease-vs-loan",
    "crumb": "Cargo Van Lease vs Loan",
    "title": "Cargo Van Lease vs Loan: Lease to Own Compared | Axiant",
    "og_title": "Cargo Van Lease vs Loan: Payments, Lease to Own and Upfit",
    "h1": "Cargo Van Lease vs Loan: Payments, Lease to Own and Upfit",
    "headline": "Cargo Van Lease vs Loan: Payments, Lease to Own and Upfit",
    "lede": "Which structure fits a delivery or trades van, what lease to own really means, and what happens to "
            "your racks and wrap at the end",
    "meta_desc": "Should you lease a cargo van or finance it? Compare a $60,000 van: about $1,246 a month on a loan vs $1,047 on a lease, plus lease to own, upfit and return costs.",
    "article_desc": "Compare a commercial cargo van loan, fair market value lease and lease to own, with payments, "
                    "upfit and return-condition issues for business buyers.",
    "keywords": "cargo van lease, lease cargo van, cargo van lease to own, cargo van lease vs loan, commercial van "
                "lease, lease or buy cargo van",
    "quick_answer": "A loan fits a van you'll keep and upfit, while a fair market value lease fits a van you'll replace on "
                    "a schedule. On a <strong>$60,000</strong> van at an illustrative 9% over 60 months, a loan runs about "
                    "<strong>$1,246</strong> a month and a lease with a 25% residual about <strong>$1,047</strong>. Lease "
                    "to own costs about the same as the loan. Axiant Partners, a business-loan broker in Boca Raton, "
                    "compares both. These are examples, not quotes.",
    "sections": [
        ("Loan, Lease or Lease to Own",
         "<p>These three get mixed up in ads. The difference is who carries the van's value at the end of the term. All "
         "three are for business use.</p>"
         + table(["", "Equipment loan", "FMV lease", "Lease to own"], [
             ["Who owns it", "You, from the start", "The lessor", "You, at the end for a nominal price"],
             ["Monthly payment", "Highest of the three, or equal", "Lowest", "About like the loan"],
             ["End of term", "Keep it, no balance", "Return, renew or buy at market value", "Keep it"],
             ["Upfit", "Yours to change", "May need consent or removal", "Usually your choice"],
             ["Miles and wear", "No lease limits", "Limits and return charges", "Check the contract"],
             ["Best fit", "Keep for years", "Replace on a cycle", "Own it, with lease paperwork"],
         ])
         + "<p>Vans on our <a href=\"/equipment/cargo-vans/\">cargo van financing</a> page commonly run $35,000-$75,000 "
         "before upfit, with typical rates of 6-15%, terms of 24-72 months and 0-20% down, depending on credit and age.</p>"),
        ("What the Payment Difference Looks Like",
         "<p><strong>Illustrative, not a quote.</strong> Assume a $60,000 van, nothing down, a 9% rate on each structure "
         "and 60 months. The lease assumes the van is worth 25% of its price ($15,000) at the end, which is an assumption, "
         "not a market figure.</p>"
         + table(["Structure", "Monthly", "Paid over 60 months", "To keep the van"], [
             ["Equipment loan", "About $1,246", "About $74,730", "Nothing more"],
             ["FMV lease, 25% residual", "About $1,047", "About $62,800", "About $15,000 more"],
             ["Lease to own, $1 buyout", "About $1,245", "About $74,730", "$1"],
         ])
         + "<p>The lease saves about $199 a month, or 16%, which sits inside the 10-20% we describe in "
         "<a href=\"/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/\">equipment leasing vs a loan</a>. "
         "If you buy the van at the end at that price, you've paid about $77,800, which is about $3,070 more than the loan. "
         "The lease pays off if you hand the keys back and the return is clean, or if the van is worth less than the residual "
         "and that's the lessor's problem.</p>"),
        ("What Lease to Own Really Means",
         "<p>“Cargo van lease to own” generally describes a lease with a small purchase option at the end, such as $1. Legally "
         "and economically that's close to a loan. Under "
         '<a href="https://www.law.cornell.edu/ucc/1/1-203" rel="noopener nofollow" target="_blank">UCC 1-203</a>, a lease you '
         "can't cancel, with an option to own for nominal extra payment, is generally treated as a security interest, not a true "
         "lease. A fair market value option generally isn't. So:</p>"
         "<ul>"
         "<li><strong>The payment won't be much lower.</strong> You're paying for the whole van, as the table shows.</li>"
         "<li><strong>You usually can't walk away early.</strong> Read the early-termination language before you sign.</li>"
         "<li><strong>Ask how it's taxed.</strong> A lease treated as a purchase can follow purchase rules, so have your CPA check.</li>"
         "<li><strong>Be careful with weekly-pay offers.</strong> Some rent-to-own programs price high and take the van after a "
         "missed payment. Ask for the total of payments in writing.</li>"
         "</ul>"),
        ("Upfit Is Where Vans Differ",
         "<p>A van is often not finished when it leaves the lot. Racks, partitions, refrigeration, ladder racks and wraps can add "
         "real money, and they change the answer:</p>"
         + table(["Issue", "With a loan", "With an FMV lease"], [
             ["Financing the upfit", "Often can be included if on the invoice", "Ask, since it may not add resale value"],
             ["Drilling and wiring", "Your decision", "May need lessor consent"],
             ["Refrigeration", "Keep it and move it later", "Plan who owns it at return"],
             ["Vinyl wrap", "Remove it if you sell", "Removal and paint damage can be billed"],
             ["Moving racks to the next van", "Yours to move", "Check for repair charges on holes"],
         ])
         + "<p>If the van earns money because of what's built into it, such as a mobile workshop or a refrigerated route, that "
         "usually favors a loan. A plain high-roof van on a courier route that you swap on a schedule is where an FMV lease "
         "works best. See the <a href=\"/equipment/cargo-vans/sprinter-van-financing-guide/\">Sprinter van financing guide</a> for "
         "high-roof examples.</p>"),
        ("Miles, Contracts and Return Charges",
         "<p>Route work is hard on leases. Before signing, get these in writing:</p>"
         "<ul>"
         "<li><strong>Mileage allowance.</strong> The yearly limit and the charge per mile over it. Estimate from your actual route logs.</li>"
         "<li><strong>Wear standard.</strong> Dents, floors and door damage are normal on a delivery van. Find out what's billable.</li>"
         "<li><strong>Contract match.</strong> A 60-month lease on a 24-month delivery contract leaves you with payments after the "
         "work ends, so match the term or plan for a loan you can sell out of.</li>"
         "<li><strong>End options.</strong> Whether the buyout is a set price or market value at the time.</li>"
         "</ul>"
         "<p>A loan avoids those charges, but you take the resale risk. Used vans commonly trade 25-45% below comparable new prices, "
         "depending on age, miles and wear, so check whether you might owe more than a van is worth if you sell early. See "
         '<a href="/equipment-financing/articles/can-you-finance-used-equipment/">financing used equipment</a> for older vans.</p>'),
        ("Taxes: One Point Specific to Vans",
         "<p>Heavy SUVs have a lower Section 179 cap, but vans built for cargo may not fall under it. "
         '<a href="https://www.irs.gov/publications/p946" rel="noopener nofollow" target="_blank">IRS Publication 946</a> '
         "(2025 edition) excludes from that limit a vehicle with an integral enclosure around the driver and load area, no "
         "seating behind the driver's seat and a short nose, so a cargo van may qualify differently from a passenger van. On an operating lease you'd generally deduct the "
         "payments instead. Rules change and they depend on your facts, so ask your CPA before choosing a structure for the "
         "deduction.</p>"),
        ("How to Decide",
         "<ol>"
         "<li><strong>Estimate how long you'll keep it.</strong> For most of its useful life, a loan usually wins.</li>"
         "<li><strong>Total the upfit.</strong> More custom work leans toward owning.</li>"
         "<li><strong>Check your miles.</strong> High-mileage routes make lease limits costly.</li>"
         "<li><strong>Compare totals.</strong> Add down payment, all payments, buyout and likely return charges.</li>"
         "<li><strong>Get both quoted.</strong> Use one invoice with the VIN and the upfit listed.</li>"
         "</ol>"
         '<p>When you\'re ready, <a href="/match.html">get matched with van lenders and lessors</a>. For operating costs instead '
         'of the van, see <a href="/working-capital-loans.html">working capital</a>, and try the '
         '<a href="/calculator.html">payment calculator</a>.</p>'),
    ],
    "faqs": [
        ("Is it better to lease or finance a cargo van?",
         "Finance it if you'll keep it for years or add custom upfit. Lease it if you replace vans on a schedule, stay inside "
         "the mileage limit and want a lower payment. In our $60,000 example, the lease saves about $199 a month, but costs about "
         "$3,070 more if you buy the van at the end."),
        ("What is a cargo van lease to own?",
         "It's generally a lease with a nominal purchase option at the end, such as $1. The payment is close to a loan's, and the "
         "contract may be treated as a purchase rather than a true lease."),
        ("How much is a cargo van lease per month?",
         "It depends on price, rate, term and residual. In one illustration, a $60,000 van at 9% over 60 months with a 25% residual "
         "is about $1,047 a month. That's an example, not a quote."),
        ("Can I lease a used cargo van?",
         "Some lessors do, though age and miles limit the term. Many lenders finance used vans up to 5-7 model years; older vans "
         "may need more down or a shorter term."),
        ("Can a lease include racks and refrigeration?",
         "Sometimes. Put the upfit on the invoice and ask how it's treated. Also ask who owns it at the end and what removal may cost."),
        ("What credit do I need to lease a cargo van?",
         "Requirements are similar to a loan: most look for about 600 or higher, with the best terms from about 680. Newer businesses "
         "may need more down or a cosigner."),
    ],
    "related": [
        ("/equipment/cargo-vans/", "Cargo van financing"),
        ("/equipment/cargo-vans/sprinter-van-financing-guide/", "Sprinter van financing guide"),
        ("/equipment/cargo-vans/sprinter-van-financing-delivery/", "Sprinter vans for delivery businesses"),
        ("/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/", "Equipment leasing vs a loan"),
        ("/logistics-warehousing-business-financing.html", "Logistics and warehousing financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [UCC, IRS, FTC],
}]
