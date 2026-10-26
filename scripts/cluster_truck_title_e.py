# -*- coding: utf-8 -*-
"""Commercial truck title loans, articles 12-13: the companion citation pages
(AEO plan 2e). Imported by cluster_truck_title.

The money page converts but is rarely the page an assistant quotes; these two
answer the questions assistants are asked around it - what a truck title loan
costs, and how it differs from a refinance or an equipment loan.

Every range is one the site already publishes, not a new quote:
- equipment financing at roughly 7-22% APR by credit tier, used +1-3 points
  (equipment-financing/articles/typical-equipment-financing-rates-2026);
- equity loans and cash-out refinancing against owned equipment at roughly
  50-80% of forced liquidation value over 24-72 months, 600+ FICO typical
  (equipment-financing/articles/equipment-refinancing, and this cluster);
- truck purchase financing at roughly 6-15% over 24-84 months with 0-20% down
  (equipment/semi-trucks).
The consumer contrast is the CFPB's 2016 single-payment vehicle title study.
Payment figures are arithmetic on a stated illustrative rate. No named-lender
rates, no funded totals, no testimonials.
"""
from cluster_truck_title import IRS_946, FTC

CFPB_TITLE = ("https://files.consumerfinance.gov/f/documents/201605_cfpb_single-payment-vehicle-title-lending.pdf",
              "CFPB: Single-Payment Vehicle Title Lending (2016)",
              "The CFPB's study of consumer auto title loans: APRs around 300% and about "
              "one in five loan sequences ending in repossession - the product a "
              "commercial truck title loan is often confused with.")
TILA_EXEMPT = ("https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-A/section-1026.3",
               "12 CFR 1026.3: Exempt Transactions (Truth in Lending)",
               "Business-purpose credit is exempt from federal Truth in Lending "
               "disclosures, so a commercial offer may not show an APR unless you ask.")
UCC_9311 = ("https://www.law.cornell.edu/ucc/9/9-311",
            "UCC &sect; 9-311: Property Subject to Certificate-of-Title Statutes",
            "Why a lender's lien on a titled truck is noted on the title rather than "
            "filed as a UCC-1 - the same for a title loan, a refinance or a purchase loan.")


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


MORE = [
    # ------------------------------------------------------------------ 12
    {
        "slug": "typical-truck-title-loan-rates-2026",
        "crumb": "Typical Rates and Terms 2026",
        "title": "Truck Title Loan Rates and Terms 2026 | Axiant",
        "og_title": "Typical Truck Title Loan Rates and Terms (2026)",
        "h1": "Typical Truck Title Loan Rates and Terms (2026)",
        "headline": "Typical Commercial Truck Title Loan Rates and Terms in 2026",
        "lede": "What a business-purpose loan against a truck you own commonly costs, "
                "how much it advances, how long it runs, and why it is nothing like a "
                "consumer car title loan",
        "meta_desc": "Commercial truck title loans are priced like secured equipment "
                     "loans: roughly 7-22% APR by credit, 50-80% of liquidation value, "
                     "24-72 months. What moves the price.",
        "article_desc": "Typical rates, advance amounts and terms for commercial truck "
                        "title loans in 2026, and the factors that move them.",
        "keywords": "truck title loan rates, commercial truck title loan interest rate, "
                    "semi truck title loan terms, borrow against truck rates 2026",
        "quick_answer": "A business-purpose truck title loan is priced like a secured "
                        "equipment loan, not a consumer title loan: commonly about "
                        "<strong>7-22% APR</strong> depending on credit, an advance of "
                        "roughly <strong>50-80% of forced liquidation value</strong>, and "
                        "<strong>24-72 months</strong> to repay. Axiant Partners, a "
                        "business-loan broker in Boca Raton, sees the truck's age and "
                        "mileage move the advance most, and credit move the rate.",
        "sections": [
            ("Three Numbers Make Up the Offer",
             "<p>Every truck title loan offer comes down to three figures, and they are "
             "set by different things:</p>"
             + _table(["Term", "Typical range", "Set mainly by"], [
                 ["Advance", "50-80% of forced liquidation value", "The truck"],
                 ["Rate", "About 7-22% APR", "Your credit and the business"],
                 ["Term", "24-72 months", "The truck's age and the amount"],
             ])
             + "<p>Typical ranges across lenders, not a quote. They are the same ranges "
             "the site publishes for <a href=\"/equipment-financing/articles/equipment-refinancing/\">"
             "equipment refinancing</a> and <a href=\"/equipment-financing/articles/typical-equipment-financing-rates-2026/\">"
             "equipment financing rates</a>, because a business-purpose title loan is "
             "underwritten the same way: a titled asset with a resale market, and a "
             "business that has to carry the payment.</p>"),
            ("What Sets the Rate",
             "<p>Credit tier does most of the work. Ranges commonly seen across lenders "
             "for equipment-secured business credit:</p>"
             + _table(["Credit tier", "Typical APR", "Typical term"], [
                 ["720+, 2+ yrs in business", "7-9%", "Up to 72 mo"],
                 ["680-719", "10-13%", "36-72 mo"],
                 ["640-679", "13-16%", "36-60 mo"],
                 ["580-639", "16-22%", "24-48 mo"],
                 ["Below 580", "Limited programs", "24-36 mo"],
             ])
             + "<p>Within a tier, an older or high-mileage truck commonly adds one to "
             "three points, because there is less life left in the collateral. "
             "Cash-out against a truck you own tends to sit at the higher end of a "
             "tier than financing a purchase, since the money is not buying a new "
             "asset. Fleets borrowing against several units usually do better than a "
             "single truck; see <a href=\"../owner-operator-vs-fleet-title-loan-terms/\">"
             "owner-operator vs fleet terms</a>.</p>"),
            ("What Sets the Advance",
             "<p>The advance is a share of what the truck would bring at a quick sale, "
             "not what you paid or what a dealer is asking. What moves it:</p>"
             "<ul>"
             "<li><strong>Age and mileage</strong> - the biggest single factor on any "
             "truck.</li>"
             "<li><strong>Make, engine and spec</strong> - common tractors and straight "
             "trucks with a deep buyer pool advance higher than unusual builds.</li>"
             "<li><strong>Body and equipment</strong> - a dump body, reefer unit or "
             "wrecker is valued separately from the chassis; see the "
             "<a href=\"../dump-truck-title-loan/\">dump</a>, "
             "<a href=\"../box-truck-title-loan/\">box</a> and "
             "<a href=\"../tow-truck-title-loan/\">tow truck</a> guides.</li>"
             "<li><strong>Records</strong> - documented maintenance raises both the "
             "value and the share a lender will advance against it.</li>"
             "<li><strong>What is still owed</strong> - comes straight off the top.</li>"
             "</ul>"
             "<p>The full method is in <a href=\"../how-much-can-you-borrow-against-a-semi/\">"
             "how much you can borrow against a semi</a>.</p>"),
            ("What the Payments Look Like",
             "<p>Illustrative arithmetic, not a quote. A tractor with a forced "
             "liquidation value of $80,000, owned outright, at a 65% advance - "
             "$52,000 - over 48 months:</p>"
             + _table(["Illustrative APR", "Monthly payment", "Total of payments"], [
                 ["9%", "$1,294", "$62,113"],
                 ["13%", "$1,395", "$66,961"],
                 ["18%", "$1,527", "$73,320"],
             ])
             + "<p>The spread between the best and worst tier on the same truck is "
             "about $233 a month. Test whichever figure you are offered against a slow "
             "month, not an average one.</p>"),
            ("Why It Is Nothing Like a Consumer Car Title Loan",
             "<p>Searches for a truck title loan often land on consumer title lenders. "
             "The products share a name and little else. The CFPB's 2016 study of "
             "single-payment vehicle title loans found APRs around 300% and that about "
             "one in five loan sequences ended with the vehicle repossessed.</p>"
             + _table(["", "Consumer title loan", "Commercial truck title loan"], [
                 ["Borrower", "An individual", "A business or owner-operator"],
                 ["Typical cost", "APR around 300% (CFPB)", "About 7-22% APR"],
                 ["Repayment", "Often due in about 30 days", "Amortized over 24-72 months"],
                 ["Underwriting", "The vehicle", "The truck and the business"],
             ])
             + "<p>If an offer for a work truck is priced or structured like the left "
             "column, it is the wrong product. Business-purpose credit is also exempt "
             "from federal Truth in Lending disclosures, so ask every lender for the "
             "APR and the total of payments in writing. A short-term advance against "
             "receivables is a different comparison again: see "
             "<a href=\"../title-loan-vs-mca-for-truckers/\">title loan vs MCA</a>.</p>"),
        ],
        "faqs": [
            ("What is the interest rate on a commercial truck title loan?",
             "Business-purpose truck title loans are priced like secured equipment "
             "loans, commonly about 7-22% APR depending on credit, with older or "
             "high-mileage trucks toward the higher end. These are typical ranges "
             "across lenders, not a quote."),
            ("How much will a lender advance against my truck?",
             "Commonly about 50-80% of the truck's forced liquidation value - what it "
             "would bring at a quick sale - less anything still owed on it."),
            ("How long are truck title loan terms?",
             "Commonly 24 to 72 months with fixed monthly payments, shorter for older "
             "trucks and smaller amounts."),
            ("Is a truck title loan the same as a car title loan?",
             "No. A consumer car title loan is a short-term personal loan; the CFPB "
             "found APRs around 300%. A commercial truck title loan is business credit "
             "secured by a working truck, priced like an equipment loan and repaid over "
             "months."),
            ("Why doesn't my offer show an APR?",
             "Federal Truth in Lending disclosures do not apply to business-purpose "
             "credit. Ask for the APR and the total of payments before you sign."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../truck-title-loan-vs-refinance-vs-equipment-loan/", "Truck title loan vs refinance vs equipment loan"),
            ("/equipment-financing/articles/typical-equipment-financing-rates-2026/", "Typical equipment financing rates 2026"),
            ("/match.html", "Get matched"),
        ],
        "sources": [CFPB_TITLE, TILA_EXEMPT, FTC],
    },
    # ------------------------------------------------------------------ 13
    {
        "slug": "truck-title-loan-vs-refinance-vs-equipment-loan",
        "crumb": "Title Loan vs Refinance vs Equipment Loan",
        "title": "Truck Title Loan vs Refinance vs Equipment Loan | Axiant",
        "og_title": "Truck Title Loan vs Refinance vs Equipment Loan",
        "h1": "Truck Title Loan vs Refinance vs Equipment Loan",
        "headline": "Truck Title Loan vs Refinance vs Equipment Loan: Which One Fits",
        "lede": "Three loans that all put a lien on a truck title, what each one is "
                "for, and how to tell which one your situation calls for",
        "meta_desc": "A title loan raises cash on a truck you own, a refinance replaces "
                     "the loan on one you are paying off, and an equipment loan buys "
                     "one. How to pick.",
        "article_desc": "How a commercial truck title loan, a truck refinance and a "
                        "truck equipment loan differ, and when each one fits.",
        "keywords": "truck title loan vs refinance, truck refinance vs equipment loan, "
                    "cash out refinance semi truck, borrow against truck or refinance",
        "quick_answer": "All three put a lien on the truck's title; the difference is "
                        "what the money does. A <strong>title loan</strong> raises cash "
                        "against a truck you own. A <strong>refinance</strong> replaces "
                        "the loan on a truck you are still paying for, to cut the payment "
                        "or take cash out. An <strong>equipment loan</strong> buys a "
                        "truck. Axiant Partners, a business-loan broker in Boca Raton, "
                        "starts with one question: <strong>do you need cash, a lower "
                        "payment, or another truck?</strong>",
        "sections": [
            ("Side by Side",
             _table(["", "Title loan", "Refinance", "Equipment loan"], [
                 ["What it does", "Cash from a truck you own", "Replaces your current truck loan", "Buys a truck"],
                 ["Money goes to", "You", "Old lender (plus any cash-out to you)", "The seller"],
                 ["Sized on", "50-80% of liquidation value", "Liquidation value, less the payoff", "The purchase price"],
                 ["Typical term", "24-72 months", "24-72 months", "24-84 months"],
                 ["Typical down", "None", "None", "0-20%"],
                 ["Typical rate", "About 7-22% APR", "About 7-22% APR", "About 6-15% on trucks"],
             ])
             + "<p>Typical ranges across lenders, not quotes. Purchase financing tends "
             "to price best because the money buys a new asset at a known price; "
             "borrowing against a truck you already own prices like other equipment "
             "refinancing. See <a href=\"../typical-truck-title-loan-rates-2026/\">"
             "typical truck title loan rates</a>.</p>"),
            ("Title Loan: You Own the Truck and Need Cash",
             "<p>The truck is paid off, or nearly, and the business needs working "
             "capital - a repair, a slow month, a down payment, a contract that pays "
             "net-60. The lender values the truck, advances a share of its liquidation "
             "value, notes its lien on the title and you keep driving.</p>"
             "<p>It fits when the need is real and earns something back. It does not "
             "fix a business that cannot carry its current payments. More in "
             "<a href=\"/commercial-truck-title-loan.html\">commercial truck title "
             "loans</a>.</p>"),
            ("Refinance: You Are Still Paying for the Truck",
             "<p>Two versions, and they solve different problems:</p>"
             "<ul>"
             "<li><strong>Rate-and-term refinance.</strong> A new loan pays off the old "
             "one with a lower rate, a longer term or both. No cash to you; the point "
             "is a lower payment. It makes sense when your credit or the business has "
             "improved since you bought the truck, or the original loan was expensive.</li>"
             "<li><strong>Cash-out refinance.</strong> The new loan pays off the old one "
             "and advances the extra equity to you. On a truck you are paying for, this "
             "is effectively a title loan; see "
             "<a href=\"../title-loan-with-an-existing-lien/\">title loans with an "
             "existing lien</a>.</li>"
             "</ul>"
             "<p>Before refinancing, ask your current lender for a payoff letter and "
             "check for a prepayment penalty. A longer term lowers the payment but "
             "usually raises the total you pay.</p>"),
            ("Equipment Loan: You Need Another Truck",
             "<p>Buying a truck is purchase financing: the lender pays the seller, "
             "takes a lien on the new truck's title, and sizes the loan on the price, "
             "usually with some money down. It is generally the cheapest of the three, "
             "because the lender is financing a known asset at a known price. See "
             "<a href=\"/equipment/semi-trucks/\">semi truck financing</a>.</p>"
             "<p>The combination owner-operators ask about is using the equity in the "
             "truck they own as the down payment on the next one. It works - a title "
             "loan on truck one, an equipment loan on truck two - but it leaves you "
             "with two liens and two payments on two trucks that both have to be "
             "working. Plan for the month one of them is in the shop.</p>"),
            ("Three Owner-Operators, Three Answers",
             "<p>Illustrative situations, not quotes:</p>"
             + _table(["Situation", "Usually the fit", "Why"], [
                 ["Paid off, needs $40K", "Title loan", "Equity, no loan to replace"],
                 ["Owes $30K at a high rate", "Rate-and-term refi", "Lower payment, no new debt"],
                 ["Owes $20K, needs $25K", "Cash-out refi", "One loan pays off and funds"],
                 ["Wants a second truck", "Equipment loan", "Cheapest money for a purchase"],
             ])
             + "<p>If two of these apply at once - you want a second truck and the first "
             "one is expensive to carry - fix the first payment before adding the "
             "second.</p>"),
            ("Things That Are the Same in All Three",
             "<ul>"
             "<li><strong>The lien goes on the title.</strong> Trucks are titled "
             "vehicles, so every lender records its lien on the certificate of title "
             "rather than with a UCC filing.</li>"
             "<li><strong>Insurance naming the lender</strong> as loss payee.</li>"
             "<li><strong>A valuation</strong> from the VIN, mileage, photos and "
             "records.</li>"
             "<li><strong>Depreciation stays with the owner.</strong> Borrowing against "
             "a truck does not change who depreciates it; a purchase may qualify for "
             "Section 179 in the year it is placed in service (IRS Publication 946).</li>"
             "</ul>"
             "<p>Selling the truck and leasing it back is a fourth route with different "
             "trade-offs: see <a href=\"../truck-title-loan-vs-sale-leaseback/\">title "
             "loan vs sale-leaseback</a>.</p>"),
        ],
        "faqs": [
            ("What is the difference between a truck title loan and a refinance?",
             "A title loan raises cash against a truck you own. A refinance replaces "
             "the existing loan on a truck you are still paying for, either to lower "
             "the payment (rate-and-term) or to take equity out as cash (cash-out)."),
            ("Is a cash-out refinance the same as a title loan?",
             "On a truck that still has a loan, effectively yes: the new lender pays "
             "off the old one and advances the remaining equity to you."),
            ("Which is cheaper: a title loan or an equipment loan?",
             "Purchase financing is usually cheaper, because the lender is financing a "
             "known asset at a known price. Borrowing against a truck you already own "
             "is priced like other equipment refinancing."),
            ("Can I use my truck's equity as a down payment on another truck?",
             "Yes - a title loan on the truck you own and an equipment loan on the new "
             "one. It means two liens and two payments, so both trucks need to be "
             "earning."),
            ("When does refinancing a truck make sense?",
             "When your credit or business has improved since you bought it, or the "
             "original loan was expensive. Check the payoff and any prepayment penalty "
             "first, and remember a longer term usually raises the total cost."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../typical-truck-title-loan-rates-2026/", "Typical truck title loan rates 2026"),
            ("/equipment-financing/articles/equipment-refinancing/", "Equipment refinancing"),
            ("/equipment/semi-trucks/", "Semi truck financing"),
        ],
        "sources": [UCC_9311, IRS_946, FTC],
    },
]
