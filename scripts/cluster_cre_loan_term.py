# -*- coding: utf-8 -*-
"""How long are commercial real estate loans (term, amortization, balloon) - new spoke, daily batch 2026-11-15.

Search Console, Oct 16 - Nov 12 2026: "how long are commercial real estate loans" 41 impressions at
position 43, plus "how long are commercial mortgages" 7, "how long are commercial property loans" 5,
"how long is a commercial real estate loan" 5, "how long are commercial loans" 4, "commercial real
estate loan length" 3, "commercial property loan length" 2, "commercial loan term length" 1 (about 68
in all). Every one lands on how-long-close-commercial-real-estate-loan, which answers a different
question (time to close) and is a top-25 cited page, so it is linked from here and not edited. No page
answers loan length: the calculator and the balloon-refinance and red-flags articles touch balloons,
but none gives terms by lender type. Not split between our pages.

Ranges reuse what the site publishes: bank 5- or 10-year fixed with 20-25 year amortization, life
company 5-25 year terms, CMBS 10-year balloon with 25-30 year amortization, Fannie/Freddie 5-15 year
terms with 30-year amortization, FHA 223(f) 35 years fully amortizing
(typical-commercial-real-estate-loan-rates-2026, cmbs-vs-life-company-vs-agency-debt); bridge loans
6-36 months (commercial-bridge-loans.html); 504 debenture 10, 20 or 25 years with the bank loan often
amortized 20-25 years and maturing in 5-10 (sba-504-loan-amortization-schedule); 6.5-8% bank rates.
Rule text read Nov 15 2026: 13 CFR 120.212 (7(a) maturities: shortest appropriate term, 10 years
unless real estate or equipment with longer useful life, 25-year maximum plus construction time);
13 CFR 120.933 (504 maturities are published in the Federal Register); SBA Policy Notice 5000-17058
(25-year debenture added in 2018; the third-party loan with a 25-year 504 must run at least 10 years).
All payments and balloon balances computed by script at a stated 7.0% assumption. No named lenders.
"""
from cluster_table import table

RATE = 7.0
LOAN = 1_500_000


def pmt(p, apr, n):
    r = apr / 100 / 12
    return p * r / (1 - (1 + r) ** -n)


def bal(p, apr, n, k):
    r = apr / 100 / 12
    m = pmt(p, apr, n)
    return p * (1 + r) ** k - m * ((1 + r) ** k - 1) / r


def usd(x):
    return f"${x:,.0f}"


P25 = pmt(LOAN, RATE, 300)
B5, B7, B10 = (bal(LOAN, RATE, 300, y * 12) for y in (5, 7, 10))
AMORT = [(y, pmt(LOAN, RATE, y * 12), bal(LOAN, RATE, y * 12, 120)) for y in (20, 25, 30)]

R212 = ("https://www.law.cornell.edu/cfr/text/13/120.212",
        "13 CFR 120.212: SBA 7(a) loan maturities",
        "Shortest appropriate term; 10 years unless real estate or long-life equipment; 25-year maximum plus construction time.")
R933 = ("https://www.law.cornell.edu/cfr/text/13/120.933",
        "13 CFR 120.933: 504 loan maturities",
        "SBA publishes the available 504 debenture maturities in the Federal Register.")
N25 = ("https://www.sba.gov/sites/sbagov/files/2018-05/SBA%20Policy%20Notice%205000-17058%20CDC%20504%2025%20Year%20Debenture.pdf",
       "SBA Policy Notice 5000-17058: 25-year 504 debenture",
       "Adds the 25-year debenture to the 10- and 20-year terms; the third-party loan must run at least 10 years.")
HUD = ("https://www.hud.gov/program_offices/housing/mfh/progdesc/purchrefi223f",
       "HUD Section 223(f)",
       "FHA-insured loans to buy or refinance existing multifamily properties, with long fully amortizing terms.")

CLUSTER = {
    "pillar": "commercial-real-estate-loans.html",
    "hub": "commercial-real-estate-loans/articles",
    "hub_by_hand": True,
    "crumb": "Commercial Real Estate Loans",
    "cta_inline": "Compare commercial mortgage terms side by side",
    "cta_button": "Get Matched for a Commercial Real Estate Loan",
}

ARTICLES = [{
    "slug": "how-long-are-commercial-real-estate-loans",
    "crumb": "How Long Are Commercial Real Estate Loans?",
    "title": "How Long Are Commercial Real Estate Loans? Terms by Lender",
    "og_title": "How Long Are Commercial Real Estate Loans? Term, Amortization and Balloon",
    "h1": "How Long Are Commercial Real Estate Loans? Term, Amortization and Balloon",
    "headline": "How Long Are Commercial Real Estate Loans? Term, Amortization and Balloon",
    "lede": "Most commercial mortgages are paid as if they lasted 25 years but come due in 5 to 10. Typical "
            "lengths by lender, and what the balloon looks like",
    "meta_desc": "Commercial real estate loans usually run 5-10 years on a 20-30 year amortization with a balloon. "
                 "Terms at banks, CMBS, agency, life companies and SBA.",
    "article_desc": "How long commercial real estate loans last: the difference between term and amortization, "
                    "typical lengths at banks, CMBS, agency, life companies, SBA 504 and 7(a) and bridge lenders, "
                    "a computed balloon example, and how to match the term to your plan.",
    "keywords": "how long are commercial real estate loans, commercial mortgage term length, commercial loan term, "
                "commercial real estate loan length, commercial mortgage amortization, balloon commercial mortgage",
    "quick_answer": f"As of November 2026, most commercial real estate loans have a <strong>5- to 10-year term</strong> "
                    f"with payments figured over <strong>20 to 30 years</strong>, so the remaining balance comes due as a "
                    f"balloon. SBA 7(a) real estate loans can run up to 25 years fully amortized, SBA 504 debentures 20 or "
                    f"25 years, and bridge loans 6-36 months. On a {usd(LOAN)} loan at an assumed 7% over 25 years, about "
                    f"{usd(B10)} is still owed at year 10. Axiant Partners, a business-loan broker in Boca Raton, compares "
                    f"commercial mortgage lenders. Typical ranges, not a quote.",
    "sections": [
        ("Term, Amortization and Maturity",
         "<p>Three numbers describe how long a commercial mortgage lasts, and they are often different:</p><ul>"
         "<li><strong>Term (maturity):</strong> when the loan is due in full. Commonly 5, 7 or 10 years.</li>"
         "<li><strong>Amortization:</strong> the schedule used to set the payment, commonly 20, 25 or 30 years. A "
         "longer schedule means a lower payment and more principal left at maturity.</li>"
         "<li><strong>Fixed-rate period:</strong> how long the rate is locked. On some bank loans the rate resets at "
         "year 5 while the term runs on.</li></ul>"
         "<p>When the term is shorter than the amortization, the unpaid principal at maturity is the "
         "<strong>balloon</strong>. A homeowner&rsquo;s 30-year mortgage is fully amortizing; most commercial loans "
         "are not. How long a loan takes to <em>close</em> is a separate question: see "
         "<a href=\"/commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/\">how long it "
         "takes to close a commercial real estate loan</a>.</p>"),
        ("Typical Lengths by Lender Type",
         table(["Lender", "Typical term", "Amortization", "Balloon?"], [
             ["Bank or credit union", "5 or 10 years", "20-25 years", "Yes"],
             ["CMBS conduit", "10 years", "25-30 years", "Yes"],
             ["Fannie Mae / Freddie Mac (multifamily)", "5-15 years", "30 years", "Usually"],
             ["Life insurance company", "5-25 years", "25-30 years or full", "Sometimes"],
             ["FHA 223(f) (multifamily)", "35 years", "35 years", "No"],
             ["SBA 7(a) (real estate)", "Up to 25 years", "Same as term", "No"],
             ["SBA 504 debenture", "20 or 25 years", "Same as term", "No (the bank piece may)"],
             ["Bridge lender", "6-36 months", "Often interest-only", "Yes"],
         ])
         + "<p>These are the ranges this site publishes on its "
         "<a href=\"/commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026/\">commercial "
         "real estate rates</a> and <a href=\"/commercial-real-estate-loans/articles/cmbs-vs-life-company-vs-agency-debt/\">CMBS "
         "vs life company vs agency</a> pages; individual lenders vary. Agency and FHA programs are for apartments; "
         "owner-occupied buildings usually go to banks or the SBA.</p>"),
        ("Worked Example: What the Balloon Looks Like",
         f"<p><strong>Illustrative, not a quote.</strong> A {usd(LOAN)} loan at an assumed {RATE:.1f}% with payments set "
         f"on a 25-year schedule pays about <strong>{usd(P25)} a month</strong> (principal and interest, computed by "
         "formula). What is still owed depends on when the term ends:</p>"
         + table(["Term ends at", "Balance due (balloon)", "Share of the loan"], [
             ["Year 5", usd(B5), f"{B5 / LOAN * 100:.0f}%"],
             ["Year 7", usd(B7), f"{B7 / LOAN * 100:.0f}%"],
             ["Year 10", usd(B10), f"{B10 / LOAN * 100:.0f}%"],
             ["Year 25 (fully amortizing)", "$0", "0%"],
         ])
         + "<p>Early payments are mostly interest, so even a 10-year term leaves most of the principal to refinance or "
         "pay off. Plan the exit when you take the loan; the "
         "<a href=\"/commercial-real-estate-loans/articles/refinance-balloon-commercial-mortgage-6-months-early/\">balloon "
         "refinance playbook</a> covers the timing.</p>"),
        ("How Amortization Length Changes the Payment",
         f"<p>Same {usd(LOAN)} loan, same assumed {RATE:.1f}% rate and a 10-year term; only the amortization changes:</p>"
         + table(["Amortization", "About per month", "Balance at year 10"],
                 [[f"{y} years", usd(m), usd(b)] for y, m, b in AMORT])
         + f"<p>Stretching from 20 to 30 years cuts the payment by about {usd(AMORT[0][1] - AMORT[2][1])} a month, which "
         "helps the property clear a lender&rsquo;s debt service coverage test, but leaves about "
         f"{usd(AMORT[2][2] - AMORT[0][2])} more to refinance at year 10. Model your own numbers in the "
         "<a href=\"/commercial-real-estate-loans/articles/commercial-real-estate-loan-calculator/\">commercial real estate "
         "loan calculator</a>.</p>"),
        ("The SBA Routes Have No Balloon",
         "<p>For owner-occupied property, the SBA programs are the main way to get a long, fully amortizing loan:</p><ul>"
         "<li><strong>SBA 7(a):</strong> loans run the shortest appropriate term, generally 10 years or less, but loans "
         "for real estate can go up to <strong>25 years</strong>, plus time for construction or improvements "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/13/120.212\" rel=\"noopener nofollow\" target=\"_blank\">13 CFR "
         "120.212</a>).</li>"
         "<li><strong>SBA 504:</strong> SBA publishes the debenture maturities in the Federal Register (13 CFR 120.933). "
         "Real estate projects use 20- or 25-year debentures that pay off in full; the 25-year option was added in "
         "2018, and its accompanying bank loan must run at least 10 years (SBA Policy Notice 5000-17058). The bank&rsquo;s "
         "first mortgage, about half the project, follows the bank&rsquo;s own terms and may balloon. See the "
         "<a href=\"/sba-loans/articles/sba-504-loan-amortization-schedule/\">SBA 504 amortization schedule</a>.</li></ul>"),
        ("Matching the Length to Your Plan",
         table(["Your plan", "Length that usually fits"], [
             ["Own and occupy for 15+ years", "SBA 7(a) or 504, or a long life-company loan"],
             ["Hold an investment property 7-10 years", "10-year bank, CMBS or agency loan"],
             ["Sell or refinance within 5 years", "5-year term with a short prepayment penalty"],
             ["Renovate or lease up first", "Bridge loan, then a permanent loan"],
         ])
         + "<p>The term and the prepayment penalty go together: a 10-year CMBS loan is cheap to hold to maturity and "
         "expensive to leave early. Read the "
         "<a href=\"/commercial-real-estate-loans/articles/cre-loan-red-flags-recourse-prepayment-balloon-closing-costs/\">CRE "
         "loan red flags</a> before choosing on payment alone.</p>"),
        ("What to Ask a Lender",
         "<ol><li>When is the loan due, and what is the amortization?</li>"
         "<li>How long is the rate fixed, and how does it reset?</li>"
         "<li>What is the estimated balloon at maturity?</li>"
         "<li>What does it cost to prepay in years 1, 3 and 5?</li>"
         "<li>Are there extension options at maturity, and on what terms?</li></ol>"
         "<p>Comparing several lenders side by side shows these differences; see "
         "<a href=\"/commercial-real-estate-loans/articles/commercial-mortgage-broker/\">working with a commercial "
         "mortgage broker</a>.</p>"),
    ],
    "faqs": [
        ("How long are commercial real estate loans?",
         "Most have a 5- to 10-year term with payments figured over 20 to 30 years, leaving a balloon at maturity. SBA 7(a) "
         "real estate loans can run up to 25 years and SBA 504 debentures 20 or 25 years, both fully amortizing; bridge "
         "loans run 6-36 months."),
        ("What is the difference between term and amortization on a commercial loan?",
         "The term is when the loan is due. The amortization is the schedule used to set the payment. When the term is "
         "shorter, the unpaid principal is due as a balloon."),
        ("Can you get a 30-year commercial mortgage?",
         "Thirty-year amortization is common on CMBS and agency loans, but the term is usually 10 years or less. Long "
         "fully amortizing terms come mainly from FHA multifamily programs, some life companies and the SBA (up to 25 years)."),
        (f"How much is the balloon on a {usd(LOAN)} commercial loan?",
         f"At an assumed 7% on a 25-year schedule, about {usd(B5)} at year 5 and {usd(B10)} at year 10. Illustrations, "
         "computed by formula, not quotes."),
        ("What happens when a commercial loan matures?",
         "You pay the balance by refinancing, selling or paying cash. Lenders do not have to extend, so start the refinance "
         "about six months before maturity."),
        ("Is an SBA loan longer than a conventional commercial mortgage?",
         "Usually. SBA 7(a) real estate loans can run up to 25 years and 504 debentures 20 or 25 years without a balloon, "
         "while conventional loans commonly mature in 5-10 years."),
    ],
    "related": [
        ("/commercial-real-estate-loans.html", "Commercial real estate loans"),
        ("/commercial-real-estate-loans/articles/commercial-real-estate-loan-calculator/", "Commercial real estate loan calculator"),
        ("/commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/", "How long it takes to close"),
        ("/commercial-real-estate-loans/articles/refinance-balloon-commercial-mortgage-6-months-early/", "Refinancing a balloon early"),
        ("/sba-loans/articles/sba-504-loan-amortization-schedule/", "SBA 504 amortization schedule"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [R212, R933, N25, HUD],
}]
