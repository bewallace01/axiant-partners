# -*- coding: utf-8 -*-
"""SBA 504 loan amortization schedule - new spoke, from the 2026-11-10 daily batch.

Search Console, Oct 12 to Nov 8 2026: "sba 504 loan amortization schedule" 75 impressions at
position 57, landing on sba-504-loan-rates, which has no schedule. The fees spoke (Nov 7) has a
six-row sample; this page is the full year-by-year schedule, the 10/20/25-year comparison, the bank
piece's balloon and the debenture prepayment premium. Every payment and balance was computed by
script (monthly amortization, 12 payments a year), not by hand. Rates are assumptions inside the
~6-7% debenture range the site already publishes and the 7.75% bank rate the fees spoke uses, and
are labelled illustrative. The premium schedule and "as a whole and not in part" are read from SBA
Form 1504 (4-18), the debenture form, on 2026-11-10. Never names a lender. no_hub: the folder's
index is edited by hand.
"""
from cluster_table import table
from sba_sources import SOP, SBA_504

FORM1504 = ("https://caweb.sba.gov/library/pdf/Form_1504.pdf",
            "SBA Form 1504: Debenture",
            "The debenture form, including the repurchase premium schedule for 10-, 20- and 25-year debentures.")
CFR971 = ("https://www.law.cornell.edu/cfr/text/13/120.971",
          "13 CFR 120.971: Allowable fees paid by Borrower",
          "The servicing, late and other fees a CDC may charge over the life of the loan.")

_F1504_A = ('<a href="' + FORM1504[0] + '" rel="noopener nofollow" target="_blank">SBA Form 1504</a>')

# 25-year debenture of $620,000 at an assumed 6.5% effective rate: payment $4,186.28 a month.
_YEARS = [
    (1, "$39,999", "$10,237", "$609,763"), (2, "$39,313", "$10,922", "$598,841"),
    (3, "$38,582", "$11,654", "$587,187"), (4, "$37,801", "$12,434", "$574,753"),
    (5, "$36,968", "$13,267", "$561,485"), (6, "$36,080", "$14,156", "$547,330"),
    (7, "$35,132", "$15,104", "$532,226"), (8, "$34,120", "$16,115", "$516,111"),
    (9, "$33,041", "$17,194", "$498,916"), (10, "$31,889", "$18,346", "$480,570"),
    (11, "$30,661", "$19,575", "$460,996"), (12, "$29,350", "$20,886", "$440,110"),
    (13, "$27,951", "$22,284", "$417,826"), (14, "$26,459", "$23,777", "$394,049"),
    (15, "$24,866", "$25,369", "$368,680"), (16, "$23,167", "$27,068", "$341,612"),
    (17, "$21,354", "$28,881", "$312,731"), (18, "$19,420", "$30,815", "$281,915"),
    (19, "$17,356", "$32,879", "$249,036"), (20, "$15,154", "$35,081", "$213,955"),
    (21, "$12,805", "$37,430", "$176,525"), (22, "$10,298", "$39,937", "$136,588"),
    (23, "$7,624", "$42,612", "$93,976"), (24, "$4,770", "$45,466", "$48,511"),
    (25, "$1,725", "$48,511", "$0"),
]

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans/articles",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "Compare 504 lenders and their terms",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "sba-504-loan-amortization-schedule",
    "crumb": "SBA 504 Amortization Schedule",
    "title": "SBA 504 Loan Amortization Schedule, Year by Year | Axiant",
    "og_title": "SBA 504 Loan Amortization Schedule: Payments, Balances and Payoff",
    "h1": "SBA 504 Loan Amortization Schedule: Payments, Balances and Payoff",
    "headline": "SBA 504 Loan Amortization Schedule: Payments, Balances and Payoff",
    "lede": "A full 25-year schedule for the CDC debenture, 10- vs 20- vs 25-year payments, the bank "
            "loan's balloon, and what paying off early costs",
    "meta_desc": "SBA 504 amortization schedule: a $620,000 debenture at 6.5% over 25 years is about $4,186 a month. Year-by-year balances, the bank balloon and the payoff premium.",
    "article_desc": "A year-by-year SBA 504 debenture amortization schedule with 10-, 20- and 25-year payment "
                    "comparisons, the bank loan's balloon, and the declining prepayment premium from SBA Form 1504.",
    "keywords": "sba 504 loan amortization schedule, sba 504 amortization, 504 loan payment, sba 504 loan "
                "monthly payment, 504 debenture prepayment penalty, sba 504 balloon",
    "quick_answer": "The CDC's 504 debenture amortizes fully with a fixed payment over 10, 20 or 25 years, so "
                    "there is no balloon on that piece. As an illustration, a <strong>$620,000</strong> debenture "
                    "at an assumed 6.5% over 25 years is about <strong>$4,186 a month</strong>, with about "
                    "$480,570 left after year 10. The bank's first mortgage runs on its own, often shorter, "
                    "schedule. These are typical figures, not a quote; Axiant Partners, a business-loan broker "
                    "in Boca Raton, compares 504 lenders.",
    "sections": [
        ("How a 504 Loan Amortizes",
         "<p>A 504 project has two loans with two schedules. The bank's first mortgage covers about 50% of "
         "the project. The Certified Development Company (CDC) loan covers about 40% and is funded by an "
         "SBA-guaranteed debenture. You put in about 10%. The SBA side is the predictable one: the debenture "
         "carries one fixed rate for its whole term and pays down to zero with level payments. The bank sets "
         "its own rate, amortization and maturity, and that is where a balloon or a rate reset usually comes "
         "from.</p>"
         + table(["Piece", "Share of project", "How it pays down"], [
             ["Bank first mortgage", "About 50%", "Bank's terms; often amortized 20-25 years with a 5-10 year maturity or reset"],
             ["CDC debenture", "About 40%", "Fixed rate, level payments, fully amortized over 10, 20 or 25 years"],
             ["Your injection", "About 10%", "Paid at closing; more for some startups and special-purpose buildings"],
         ])
         + "<p>The 10-year debenture is used for equipment; 20- and 25-year debentures are for real estate. "
         'For how the rate is set, see <a href="/sba-loans/articles/sba-504-loan-rates/">SBA 504 loan rates</a>, '
         'and for the program itself, <a href="/sba-loans/articles/what-is-an-sba-504-loan/">what an SBA 504 '
         "loan is</a>.</p>"),
        ("Worked Example: The Full 25-Year Debenture Schedule",
         "<p><strong>Illustrative, not a quote.</strong> Take a $1,500,000 owner-occupied building. The net CDC "
         "share is 40%, or $600,000. Financed fees are added on top, so assume a <strong>$620,000</strong> "
         'debenture (how fees are added is shown step by step on our <a href="/sba-loans/articles/sba-504-loan-fees/">'
         "504 fees</a> page). At an assumed 6.5% effective rate over 25 years, the payment is about "
         "<strong>$4,186.28 a month</strong>, or about $50,235 a year.</p>"
         + table(["Year", "Interest paid", "Principal paid", "Balance at year end"],
                 [[str(y), i, p, b] for (y, i, p, b) in _YEARS])
         + "<p>Two things stand out. In year 1, about 80% of what you pay is interest; principal doesn't pass "
         "interest until year 15. And after 10 years you still owe about 78% of the original debenture, which "
         "matters if you plan to sell or refinance. Total interest over 25 years is about $635,885 at this "
         "rate. Figures come from standard monthly amortization and are rounded to the dollar.</p>"),
        ("10 vs 20 vs 25 Years: Payment and Total Interest",
         "<p>Same $620,000 and the same assumed 6.5%, so only the term changes. In practice longer debentures "
         "often price a little differently, so treat this as a comparison of terms, not of quotes.</p>"
         + table(["Debenture term", "About per month", "Total interest"], [
             ["10 years", "$7,039.97", "$224,797"],
             ["20 years", "$4,622.55", "$489,413"],
             ["25 years", "$4,186.28", "$635,885"],
         ])
         + "<p>Going from 20 to 25 years lowers the payment by about $436 a month but adds about $146,000 of "
         "interest. The 25-year term mostly helps debt service coverage, the ratio lenders test against your "
         "cash flow. If coverage is comfortable, the 20-year term costs far less over time.</p>"),
        ("The Bank Piece and Its Balloon",
         "<p>The schedule above is only the SBA side. Keep the same project and assume the bank lends "
         "$750,000 at 7.75%, amortized over 25 years but maturing in 10. The payment is about "
         "<strong>$5,664.97 a month</strong>, so the two loans together come to about <strong>$9,851 a "
         "month</strong>.</p>"
         + table(["Bank loan", "About"], [
             ["Monthly payment", "$5,664.97"],
             ["Balance after 5 years", "$690,051"],
             ["Balance after 10 years", "$601,839"],
         ])
         + "<p>If the note matures at year 10, about $601,839 is due or has to be refinanced, while the "
         "debenture keeps paying down on schedule. Some banks reset the rate instead of maturing the loan. "
         "Ask for the bank's term, amortization and maturity in writing and model them separately. Our "
         '<a href="/sba-loans/articles/sba-504-lenders/">SBA 504 lenders</a> guide covers what to compare on '
         "the bank half.</p>"),
        ("Paying Off a 504 Debenture Early",
         "<p>The debenture can be prepaid, but " + _F1504_A + " allows it only as a whole, not in part, and adds "
         "a repurchase premium in the early years. The premium is the remaining balance times the debenture's "
         "stated interest rate times a factor that falls each year:</p>"
         + table(["Debenture term", "Factor by year", "No premium from"], [
             ["20 or 25 years", "1.00 in year 1, then down 0.10 a year to 0.10 in year 10", "Year 11"],
             ["10 years", "1.00 in year 1, then down 0.20 a year to 0.20 in year 5", "Year 6"],
         ])
         + "<p>Using the example's balance and, for simplicity, 6.5% as the stated rate: paying off in year 4 "
         "(after about $587,187 is left at the end of year 3) costs about $587,187 x 0.065 x 0.70, or "
         "<strong>$26,717</strong>. In year 7 it's about $14,231. From year 11 it's zero. The stated rate on "
         "the debenture is lower than the all-in effective rate, so a real premium would usually come in a bit "
         "under these figures. The bank loan has its own prepayment terms, which vary by lender. If a sale is "
         "likely within a few years, see "
         '<a href="/sba-loans/articles/sba-504-refinance/">SBA 504 refinance</a> and compare the premium with '
         "the rate you'd save.</p>"),
        ("How to Build Your Own 504 Schedule",
         "<ol>"
         "<li><strong>Get the gross debenture amount.</strong> Ask the CDC for the gross figure, which includes financed fees, not the net 40%.</li>"
         "<li><strong>Use the effective rate.</strong> The CDC can quote the all-in rate that includes ongoing servicing and SBA annual fees.</li>"
         "<li><strong>Pick the term.</strong> 25 or 20 years for real estate, 10 for equipment.</li>"
         "<li><strong>Model the bank loan separately.</strong> Use its rate, its amortization and its maturity date.</li>"
         "<li><strong>Add the two payments.</strong> Test the total against your cash flow, the way the lenders will.</li>"
         "</ol>"
         '<p>The <a href="/sba-loan-calculator/">SBA loan calculator</a> handles either piece. To compare real '
         'pairings of bank and CDC terms, <a href="/match.html">get matched with SBA 504 lenders</a> or call '
         '<a href="tel:+15612680465">(561) 268-0465</a>. Rates change, and approval is up to the lender and SBA.</p>'),
    ],
    "faqs": [
        ("Does an SBA 504 loan have a balloon payment?",
         "The CDC debenture doesn't: it amortizes fully over 10, 20 or 25 years with a fixed payment. The bank's "
         "first mortgage can. Many are amortized over 20 to 25 years but mature or reset after 5 to 10, so check "
         "the bank's maturity date."),
        ("What is the monthly payment on an SBA 504 loan?",
         "It depends on the debenture amount, rate and term, plus the bank loan. As an illustration, a $620,000 "
         "debenture at 6.5% is about $4,186 a month over 25 years, $4,623 over 20 and $7,040 over 10. A $750,000 "
         "bank loan at 7.75% over 25 years adds about $5,665."),
        ("How much of a 504 loan is paid off after 10 years?",
         "On a 25-year debenture at about 6.5%, roughly 22%. In the example, $620,000 falls to about $480,570 "
         "after 10 years. A 20-year debenture pays down faster because more of each payment goes to principal."),
        ("Is there a prepayment penalty on an SBA 504 loan?",
         "Yes, on the debenture for the first half of the term. SBA Form 1504 sets a premium of the balance times "
         "the stated rate times a factor: 1.00 in year 1, falling 0.10 a year to zero from year 11 on 20- and "
         "25-year debentures, and falling 0.20 a year to zero from year 6 on 10-year debentures."),
        ("Can you make extra payments on a 504 debenture?",
         "The debenture form allows repurchase as a whole, not in part, so a partial prepayment doesn't work the "
         "way it does on many bank loans. Ask the CDC how it handles extra payments. The bank loan follows the "
         "bank's own terms."),
    ],
    "related": [
        ("/sba-loans/articles/sba-504-loan-fees/", "SBA 504 loan fees"),
        ("/sba-loans/articles/sba-504-loan-rates/", "SBA 504 loan rates"),
        ("/sba-loans/articles/what-is-an-sba-504-loan/", "What is an SBA 504 loan?"),
        ("/sba-loans/articles/sba-504-lenders/", "SBA 504 lenders"),
        ("/sba-loans/articles/sba-504-refinance/", "SBA 504 refinance"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [FORM1504, SOP, SBA_504, CFR971],
}]
