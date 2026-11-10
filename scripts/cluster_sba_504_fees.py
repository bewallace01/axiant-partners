# -*- coding: utf-8 -*-
"""SBA 504 loan fees - new spoke, from the 2026-11-07 daily batch.

Search Console, Oct 7 to Nov 4 2026: "how much are 504 loan fees" 84 impressions at
position 72, "sba 504 loan amortization schedule" 36 at 69, "sba debenture" 33 at 45, all
landing on sba-504-loan-rates, which treats fees in one short list. Every fee is from
SOP 50 10 8.1 (Section A, Ch. 4, Para. E), 13 CFR 120.971 and 120.972, and SBA Information
Notice 5000-881796 (FY 2027), all read on 2026-11-07. Debenture rates reuse the ~6-7% range
the site already publishes and are labelled illustrative. Never names a lender. The folder's
index is not generated from this module, so no_hub.
"""
from cluster_table import table
from sba_sources import SOP, SBA_504

NOTICE = ("https://legacy.sba.gov/sites/default/files/2026-09/Information%20Notice%20-%20504%20Fees%20FY%202027.pdf",
          "SBA Information Notice 5000-881796: 504 Fees for Fiscal Year 2027",
          "The FY 2027 upfront guaranty fee and annual service fee, and the groups whose fees are waived.")
CFR971 = ("https://www.law.cornell.edu/cfr/text/13/120.971",
          "13 CFR 120.971: Allowable fees paid by Borrower",
          "Processing, closing, servicing, late and assumption fees a CDC may charge.")
CFR972 = ("https://www.law.cornell.edu/cfr/text/13/120.972",
          "13 CFR 120.972: Fees paid by Third Party Lenders and CDCs",
          "The one-time 0.5% participation fee on a senior lender and the CDC's annual fee to SBA.")

_NOTICE_A = ('<a href="' + NOTICE[0] + '" rel="noopener nofollow" target="_blank">SBA\'s FY 2027 fee notice</a>')
_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>')

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans/articles",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "Compare 504 lenders and their fees",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "sba-504-loan-fees",
    "crumb": "SBA 504 Loan Fees",
    "title": "SBA 504 Loan Fees in 2026-27: Every Fee Explained | Axiant",
    "og_title": "SBA 504 Loan Fees: What Each Fee Costs and Who Pays It",
    "h1": "SBA 504 Loan Fees: What Each Fee Costs and Who Pays It",
    "headline": "SBA 504 Loan Fees: What Each Fee Costs and Who Pays It",
    "lede": "The upfront, ongoing and bank-side fees on a 504 loan, with a worked example, a sample "
            "amortization schedule and who has them waived for fiscal 2027",
    "meta_desc": "How much are SBA 504 loan fees? CDC processing up to 1.5%, 0.5% guaranty, 0.4% underwriter, 0.25% funding, plus annual fees. FY 2027 figures and a worked example.",
    "article_desc": "Every fee a 504 borrower can be charged under SOP 50 10 8.1 and SBA's FY 2027 "
                    "notice, with a worked example and a sample amortization schedule.",
    "keywords": "sba 504 loan fees, how much are 504 loan fees, sba 504 closing costs, sba debenture, "
                "sba 504 loan amortization schedule, 504 guaranty fee, cdc processing fee",
    "quick_answer": "On the debenture, expect about <strong>2.65%</strong> in upfront percentage fees: up to "
                    "1.5% CDC processing, 0.5% SBA guaranty, 0.4% underwriter and 0.25% funding, usually "
                    "financed into the loan. Ongoing, you pay at least a <strong>0.625%</strong> servicing "
                    "fee and a <strong>0.203%</strong> SBA annual fee for fiscal 2027. Manufacturers, "
                    "food-supply businesses and rural businesses have the two SBA fees waived. Axiant "
                    "Partners, a business-loan broker in Boca Raton, compares 504 lenders.",
    "sections": [
        ("Every 504 Fee in One Table",
         "<p>A 504 project has three pieces: a bank first mortgage, a Certified Development Company (CDC) "
         "loan funded by an SBA-guaranteed debenture, and your own injection. The fees below come from "
         "the table in " + _SOP_A + " and " + _NOTICE_A + ", effective for loans approved October 1, 2026 "
         "through September 30, 2027.</p>"
         + table(["Fee", "Amount", "When and to whom"], [
             ["CDC processing", "Up to 1.5% of the net debenture", "One time, to the CDC"],
             ["CDC closing", "A reasonable fee; up to $10,000 may be financed", "One time, to the CDC"],
             ["SBA guaranty", "0.50% of the net debenture for FY 2027", "One time, to SBA"],
             ["Underwriter", "0.40% on 20- and 25-year debentures; 0.375% on 10-year", "One time, to the underwriter"],
             ["Funding", "0.25% of the net debenture", "One time, for trustee and agent costs"],
             ["Participation", "0.50% of the senior mortgage", "One time; the bank, CDC or borrower may pay"],
             ["CDC servicing", "0.625% a year minimum", "Monthly, on the unpaid balance"],
             ["SBA annual", "0.203% for FY 2027", "Yearly, on the unpaid balance"],
             ["Central servicing agent", "Set by contract with SBA", "Initiation and ongoing"],
         ])
         + "<p>The servicing fee can't normally go above 1% a year, or 1.5% in rural areas, without SBA's "
         "prior approval, and 2% is the ceiling. Two other fees apply only if something happens: a late "
         "fee of 5% of the late payment or $100, whichever is greater, and an assumption fee of up to 1% "
         "of the balance. A CDC can also ask for a deposit at application of $2,500 or 1% of the net "
         "debenture, whichever is less, and it can be credited toward the processing fee.</p>"),
        ("Who Has the SBA Fees Waived for Fiscal 2027",
         "<p>" + _NOTICE_A.replace("SBA\'s FY 2027 fee notice", "The FY 2027 notice") + " waives both the "
         "upfront guaranty fee and the annual fee for three groups, including on 504 debt refinance loans:</p>"
         "<ul>"
         "<li><strong>Manufacturers</strong> in NAICS sectors 31-33.</li>"
         "<li><strong>Food supply chain businesses</strong> in the NAICS codes the notice lists, which include "
         "farming, fishing, grocery wholesale and refrigerated warehousing. Some trucking codes count only for "
         "refrigerated, farm, grain or livestock hauling.</li>"
         "<li><strong>Businesses located in a rural area.</strong></li>"
         "</ul>"
         "<p>Check your NAICS code and location with the CDC early, because the waiver changes the numbers in "
         "your quote. It doesn't touch the CDC, underwriter or funding fees. Everyone else pays 0.50% upfront "
         "and 0.203% a year. On the 504 Debt Refinance without Expansion program the annual fee is 0.204%. "
         "These amounts reset each fiscal year, and your loan keeps the rate for the year it was approved.</p>"),
        ("Worked Example: A $1,000,000 Building",
         "<p><strong>Illustrative, not a quote.</strong> Assume a standard 50/40/10 split on a $1,000,000 "
         "owner-occupied purchase, no fee waiver, and an assumed $2,500 CDC closing fee.</p>"
         + table(["Item", "Basis", "About"], [
             ["Bank first mortgage", "50% of project", "$500,000"],
             ["Net debenture", "40% of project", "$400,000"],
             ["Your injection", "10% of project", "$100,000"],
             ["CDC processing", "1.5% of net debenture", "$6,000"],
             ["Funding fee", "0.25% of net debenture", "$1,000"],
             ["CDC closing", "Assumed", "$2,500"],
             ["SBA guaranty", "0.50% of net debenture", "$2,000"],
             ["Subtotal", "Net plus the four fees above", "$411,500"],
             ["Gross debenture", "Subtotal divided by 0.996, rounded up to the next even thousand", "$414,000"],
             ["Underwriter", "0.40% of gross debenture", "$1,656"],
             ["Balance to you", "Left over from rounding up", "$844"],
             ["Participation fee", "0.50% of bank loan", "$2,500"],
         ])
         + "<p>So about <strong>$13,000</strong> of fees sits in the debenture, which is why you rarely write a "
         "check for them. The administrative costs aren't part of project cost: they're added to the net "
         "debenture to reach the gross debenture, so they don't raise your 10%. The steps follow the pricing "
         "model in the SOP. Your out-of-pocket costs are "
         "different: settlement agent fees, delivery, and required certifications, plus the appraisal, "
         "environmental report and title work any commercial purchase needs.</p>"),
        ("Sample SBA 504 Amortization Schedule",
         "<p>The debenture is fully amortizing with a fixed payment. Here is the same $414,000 over 25 years at an "
         "assumed 6.5% effective rate, inside the roughly 6-7% range on our "
         '<a href="/sba-loans/articles/sba-504-loan-rates/">SBA 504 loan rates</a> page. The payment is about '
         "<strong>$2,795 a month</strong>.</p>"
         + table(["After year", "Balance left", "Paid down"], [
             ["1", "$407,164", "$6,836"],
             ["5", "$374,927", "$39,073"],
             ["10", "$320,897", "$93,103"],
             ["15", "$246,183", "$167,817"],
             ["20", "$142,867", "$271,133"],
             ["25", "$0", "$414,000"],
         ])
         + "<p>The bank piece runs on its own schedule. It often has a 5- to 10-year reset even when it amortizes "
         "over 20 to 25 years, so model it separately. As an illustration, $500,000 at 7.75% over 25 years is "
         "about $3,777 a month, giving a combined payment near $6,572 until the bank rate changes. Run your own "
         'numbers with the <a href="/sba-loan-calculator/">SBA loan calculator</a>, or see every year, the 10- vs 25-year payments and the payoff premium on our '
         '<a href="/sba-loans/articles/sba-504-loan-amortization-schedule/">full SBA 504 amortization schedule</a>.</p>'),
        ("What an SBA Debenture Is",
         "<p>A debenture is the bond behind the CDC's loan. SBA guarantees it, and it's sold to investors, which is "
         "what lets the CDC offer a long fixed rate. The net debenture is the amount that reaches your project. "
         "The gross debenture adds the financed fees, and it's what you repay. Quotes can blur the two, so ask "
         "which one a percentage applies to. For the rate side, including how the sale sets your number, see "
         'our <a href="/sba-loans/articles/sba-504-loan-rates/">504 rates guide</a>; for the program itself, see '
         '<a href="/sba-loans/articles/what-is-an-sba-504-loan/">what an SBA 504 loan is</a>.</p>'),
        ("How 504 Fees Compare With a 7(a)",
         "<p>The two programs charge in different places, so compare total cost rather than one line. On a "
         "504, the upfront percentages apply mainly to the debenture, about 40% of the project, and the bank "
         "sets its own fees on the first mortgage. A 7(a) charges its guaranty fee on the guaranteed share of "
         "one larger loan, and it's set by its own annual notice. The right structure usually depends on "
         'whether you need more than real estate and equipment. See <a href="/sba-loans/articles/sba-7a-vs-504-loan/">'
         "SBA 7(a) vs 504</a>, and if your project needs no SBA structure at all, compare "
         '<a href="/commercial-real-estate-loans.html">commercial real estate loans</a>.</p>'),
        ("Questions to Ask Before You Sign",
         "<ol>"
         "<li><strong>What's the CDC processing fee?</strong> 1.5% is a cap on the net debenture, so ask for the actual number.</li>"
         "<li><strong>What will the closing fee be?</strong> Only $10,000 can be financed from the debenture.</li>"
         "<li><strong>What's the servicing fee?</strong> The floor is 0.625%; find out what yours is and whether it needs SBA approval.</li>"
         "<li><strong>Do I qualify for the FY 2027 waiver?</strong> Give the CDC your NAICS code and address.</li>"
         "<li><strong>Who pays the 0.50% participation fee?</strong> It may fall on the bank, the CDC or you.</li>"
         "<li><strong>What does the bank charge on its half?</strong> Those fees vary and aren't set by SBA.</li>"
         "</ol>"
         '<p>Talk to an SBA specialist at <a href="tel:+15612680465">(561) 268-0465</a>, or '
         '<a href="/match.html">get matched with SBA 504 lenders</a> and compare the bank-plus-CDC pairing '
         "instead of one rate. Fees and rates change, and approval is up to the lender and SBA.</p>"),
    ],
    "faqs": [
        ("How much are SBA 504 loan fees?",
         "Upfront percentages on the debenture total about 2.65%: up to 1.5% CDC processing, 0.5% SBA guaranty, 0.4% "
         "underwriter on 20- and 25-year debentures, and 0.25% funding. A CDC closing fee and a 0.5% participation "
         "fee on the senior mortgage also apply. Ongoing, expect at least 0.625% servicing and a 0.203% SBA annual "
         "fee for loans approved in fiscal 2027."),
        ("Are SBA 504 fees financed into the loan?",
         "Most are. SBA's rules add administrative costs to the net debenture to reach the gross debenture, so they're "
         "repaid over the term, and up to $10,000 of the CDC closing fee can be financed. Settlement, delivery, "
         "certification and third-party report costs are often out of pocket."),
        ("Who doesn't pay SBA 504 guaranty fees in 2027?",
         "For loans approved October 1, 2026 through September 30, 2027, SBA waives the upfront and annual fees for "
         "manufacturers in NAICS 31-33, listed food supply chain businesses and businesses in a rural area."),
        ("What is an SBA debenture?",
         "It's the SBA-guaranteed bond that funds the CDC's share of a 504 project, typically about 40%. It's sold to "
         "investors and carries a rate fixed for the full 10, 20 or 25 years."),
        ("Does a 504 loan have an amortization schedule?",
         "Yes. The debenture amortizes fully with a fixed payment over its term. As an illustration, $414,000 at 6.5% "
         "over 25 years is about $2,795 a month, with about $321,000 left after 10 years. The bank loan has its own "
         "schedule and may reset."),
        ("What are the late fees on a 504 loan?",
         "Payments received after the 15th of the month may be charged 5% of the late payment or $100, whichever is greater."),
    ],
    "related": [
        ("/sba-loans/articles/sba-504-loan-rates/", "SBA 504 loan rates"),
        ("/sba-loans/articles/what-is-an-sba-504-loan/", "What is an SBA 504 loan?"),
        ("/sba-loans/articles/sba-504-lenders/", "SBA 504 lenders"),
        ("/sba-loans/articles/sba-7a-vs-504-loan/", "SBA 7(a) vs 504"),
        ("/sba-loans/articles/sba-504-refinance/", "SBA 504 refinance"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, NOTICE, CFR971, CFR972, SBA_504],
}]
