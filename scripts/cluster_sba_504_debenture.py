# -*- coding: utf-8 -*-
"""SBA 504 debenture explainer - new spoke, from the 2026-11-11 daily batch.

Search Console, Oct 13 to Nov 9 2026: "sba debenture" 41 impressions at position 45 and "current
sba 504 interest rates" 43 at 74, both landing on sba-504-loan-rates; "sba cdc 504 loan" 27 at 68;
"calculate 504 loan interest" 18 at 67. The rates page explains the rate range, the fees page has
one paragraph defining a debenture and the amortization page has the schedule and the premium. No
page explains the instrument itself: how the CDC's loan is funded by a monthly debenture sale, the
pricing calendar, the difference between the debenture rate, the note rate and the effective rate,
and who you actually pay. This page does only that and links to the others for rates, fees and
schedules.

Facts and where they come from (read 2026-11-11):
- NADCO / Eagle Compliance, "Understanding the SBA 504 Loan Funding Process" (October 2026): 20-
  and 25-year debentures priced over the 10-year Treasury, 10-year debentures over the 5-year;
  offering 2026-26J: Treasury 5.282 + spread 0.57 = 5.85 semiannual debenture rate, 5.906 borrower
  monthly note rate, + 0.209 SBA ongoing fee + 0.10 CSA fee + 0.625 minimum CDC servicing =
  6.984 full-term effective rate; the effective rate is not an APR because it leaves out upfront
  fees; October 2026 calendar (pricing Oct 8, funding Oct 14); DCPCs pay investors semiannually;
  the prepayment premium declines to par after 5 or 10 years; spreads compensate investors for
  the prepayment option and lower liquidity. The four listed pieces add to 6.84, not 6.984; the
  page says so and does not explain the gap beyond NADCO's pointer to the rate tutorial.
- 13 CFR 120.932 (SBA sets the rate, Treasury approves), 120.890 (interim financing),
  120.941 (certificates, SBA guarantee of timely payment), 120.954 (Central Servicing Agent).
The worked example reuses the fees page's $414,000 gross debenture and the 2026-26J note rate;
every figure was computed by script (monthly amortization) and is labelled illustrative. The
FY2027 annual fee (0.203%) differs from the 0.209% in the 2026-26J example; both are stated.
Never names a lender. no_hub: the SBA articles index is hand-edited.
"""
from cluster_table import table
from sba_sources import SOP, SBA_504

NADCO = ("https://cdn.ymaws.com/www.nadco.org/resource/resmgr/dcf_site/new_eagle_site_links/504_Funding_Process_October2.pdf",
         "NADCO / Eagle Compliance: Understanding the SBA 504 Loan Funding Process (October 2026)",
         "The monthly debenture sale, Treasury benchmarks by term, the 2026-26J rate build-up and the October 2026 calendar.")
CFR932 = ("https://www.law.cornell.edu/cfr/text/13/120.932",
          "13 CFR 120.932: Interest rate",
          "The rate on a 504 loan and its debenture is set by SBA and approved by the Secretary of the Treasury.")
CFR890 = ("https://www.law.cornell.edu/cfr/text/13/120.890",
          "13 CFR 120.890: Source of interim financing",
          "Who may provide interim financing for a 504 project before the debenture is sold.")
CFR941 = ("https://www.law.cornell.edu/cfr/text/13/120.941",
          "13 CFR 120.941: Certificates",
          "The participation certificates sold to investors, with SBA guaranteeing timely payment.")
CFR954 = ("https://www.law.cornell.edu/cfr/text/13/120.954",
          "13 CFR 120.954: Central Servicing Agent",
          "The agent that collects borrower payments and moves funds among borrowers, CDCs and SBA.")

_NADCO_A = '<a href="' + NADCO[0] + '" rel="noopener nofollow" target="_blank">NADCO\'s October 2026 funding guide</a>'

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans/articles",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "Compare 504 lenders and CDCs",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "sba-504-debenture",
    "crumb": "SBA 504 Debenture",
    "title": "SBA 504 Debenture: How It's Funded and Priced | Axiant",
    "og_title": "SBA 504 Debenture: How the CDC Loan Is Funded, Priced and Paid",
    "h1": "SBA 504 Debenture: How the CDC Loan Is Funded, Priced and Paid",
    "headline": "SBA 504 Debenture: How the CDC Loan Is Funded, Priced and Paid",
    "lede": "The monthly debenture sale behind every 504 loan, how its rate is built from Treasury yields, "
            "and how to work out the interest you'll actually pay",
    "meta_desc": "An SBA 504 debenture is the SBA-guaranteed bond that funds the CDC's loan. How the monthly sale "
                 "sets your rate, note vs effective rate, and 504 interest worked out.",
    "article_desc": "How the SBA 504 debenture works: interim financing, the monthly pooled sale, the Treasury "
                    "benchmark and spread, the difference between the debenture, note and effective rates, and "
                    "a worked example of 504 interest.",
    "keywords": "sba debenture, sba 504 debenture, sba cdc 504 loan, calculate 504 loan interest, 504 debenture "
                "rate, 504 effective rate, 504 note rate",
    "quick_answer": "A 504 debenture is the <strong>SBA-guaranteed bond</strong> a Certified Development Company "
                    "(CDC) issues to fund its share, about 40%, of a 504 project. Debentures are pooled and sold to "
                    "investors each month, and the rate is set on that pricing date as a spread over the "
                    "<strong>10-year Treasury</strong> (5-year for 10-year debentures). In the October 2026 "
                    "example published by NADCO, that gave a 5.85% debenture rate and a "
                    "<strong>6.984% effective rate</strong> after ongoing fees, in line with the ~6-7% typical "
                    "this year. Axiant Partners, a business-loan broker in Boca Raton, helps owners compare the "
                    "bank and CDC sides.",
    "sections": [
        ("How a Debenture Funds the CDC Loan",
         "<p>The CDC doesn't lend its own money for the long term. It approves your loan with SBA, the "
         "project closes with interim money, and the CDC's share is then refinanced by selling a debenture "
         "into a monthly pool. Investors buy participation certificates in that pool, and the sale proceeds "
         "pay off the interim loan. From then on you make one fixed monthly payment on the CDC loan for 10, "
         "20 or 25 years.</p>"
         + table(["Step", "What happens", "Who"], [
             ["1. Approval", "SBA approves the 504 loan and the debenture amount", "CDC and SBA"],
             ["2. Interim financing", "Construction or purchase is funded before the debenture is sold; usually the bank", "Interim lender"],
             ["3. Closing package", "Loan documents go to SBA counsel by the district cut-off date", "CDC"],
             ["4. Pooling and pricing", "Debentures are grouped into that month's pool and the rate is set", "SBA's fiscal and selling agent"],
             ["5. Funding", "Sale proceeds are distributed and pay off the interim lender", "Central Servicing Agent"],
             ["6. Repayment", "You pay monthly; investors are paid semiannually", "Borrower, CSA, trustee"],
         ])
         + "<p>Under 13 CFR 120.890 almost any qualified source can provide the interim money, as long as it "
         "isn't you or an associate and doesn't come from an SBA program. In practice it's usually the bank "
         'that holds the first mortgage. For how the bank and CDC halves fit together, see <a href="/sba-loans/articles/what-is-an-sba-504-loan/">what '
         "an SBA 504 loan is</a>.</p>"),
        ("The Monthly Sale Calendar",
         "<p>Your rate isn't known when you close. It's set on the pricing date of the first sale your loan "
         "makes it into, and missing a cut-off pushes it to the next month. " + _NADCO_A + " gives this "
         "calendar for the October 2026 sale:</p>"
         + table(["Date", "Milestone"], [
             ["Thu, Sep 10", "District cut-off: closing packages due to SBA counsel"],
             ["Thu, Sep 24", "Central Servicing Agent cut-off for loan documents"],
             ["Mon, Oct 5", "Last day a loan can be pulled from the sale"],
             ["Tue, Oct 6", "Announcement of final pool figures"],
             ["Thu, Oct 8", "Pricing date: rates set and pools formed"],
             ["Wed, Oct 14", "Funding date: proceeds distributed"],
         ])
         + "<p>So a loan whose package reached SBA counsel by September 10 was priced on October 8 and "
         "funded on October 14, about five weeks later. Ask your CDC which sale your loan is aiming for, "
         "and what the interim lender charges until then.</p>"),
        ("How the Debenture Rate Is Set",
         "<p>The rate on a 504 loan and its debenture is set by SBA and approved by the Secretary of the "
         "Treasury (13 CFR 120.932). In practice it's a Treasury yield on the pricing date plus a spread "
         "that the market sets at the sale.</p>"
         + table(["Debenture term", "Benchmark", "Typical use"], [
             ["25 years", "10-year Treasury yield", "Real estate"],
             ["20 years", "10-year Treasury yield", "Real estate, long-life equipment"],
             ["10 years", "5-year Treasury yield", "Equipment"],
         ])
         + "<p>Investors accept a spread over Treasuries because the borrower can prepay and because the "
         "certificates trade less often than Treasuries. Your credit doesn't change the debenture rate: "
         "every loan in the same pool gets the same rate. The bank's first mortgage is priced separately, "
         "and that's where most of the difference between two 504 quotes comes from. Current ranges are on "
         'our <a href="/sba-loans/articles/sba-504-loan-rates/">SBA 504 loan rates</a> page.</p>'),
        ("Debenture Rate vs Note Rate vs Effective Rate",
         "<p>A 504 quote can show three rates, and they're not interchangeable. Here is how NADCO built "
         "them up for debenture offering 2026-26J:</p>"
         + table(["Piece", "Rate", "What it is"], [
             ["Treasury yield", "5.282%", "The benchmark on the pricing date"],
             ["+ Spread", "0.57%", "Set by the market at the sale"],
             ["= Debenture rate", "5.85%", "Paid to investors, semiannually"],
             ["Note rate", "5.906%", "The rate on your monthly note"],
             ["+ SBA ongoing guaranty fee", "0.209%", "Yearly, on the unpaid balance"],
             ["+ CSA fee", "0.10%", "Central Servicing Agent"],
             ["+ CDC servicing fee", "0.625% minimum", "Yearly, on the unpaid balance"],
             ["Full-term effective rate", "6.984%", "As published for 2026-26J"],
         ])
         + "<p>Adding the note rate and the three fees gives about 6.84%. NADCO publishes 6.984% for that "
         "offering and points to Eagle Compliance's 504 rate tutorial for how the full-term effective rate "
         "is calculated, so ask the CDC for its effective rate rather than adding the pieces yourself. Two "
         "more cautions. The effective rate isn't an APR, because it leaves out the upfront fees financed "
         'into the debenture (see <a href="/sba-loans/articles/sba-504-loan-fees/">SBA 504 loan fees</a>). '
         "And the SBA annual fee depends on the fiscal year your loan is approved in: it's 0.203% for "
         "fiscal 2027, not the 0.209% in this example.</p>"),
        ("Worked Example: How to Calculate 504 Loan Interest",
         "<p><strong>Illustrative, not a quote.</strong> Take the $414,000 gross debenture from our fees "
         "example and the 2026-26J note rate of 5.906% over 25 years. Standard monthly amortization gives "
         "a principal and interest payment of about <strong>$2,643.67 a month</strong>.</p>"
         + table(["First month", "How it's worked out", "About"], [
             ["Interest", "$414,000 x 5.906% / 12", "$2,037.57"],
             ["Principal", "Payment minus interest", "$606.10"],
             ["Ongoing fees", "$414,000 x (0.209% + 0.10% + 0.625%) / 12", "$322.23"],
             ["Total first payment", "Principal, interest and ongoing fees", "$2,965.90"],
         ])
         + "<p>Over the first year that comes to about $24,251 of interest and $3,835 of ongoing fees, with "
         "about $406,527 still owed. Because the fees are charged on the unpaid balance, they shrink each "
         "year along with the interest. A 20-year term at the same note rate would be about $2,943.62 a month "
         "before fees. Your CDC and the Central Servicing Agent produce the official schedule, which can "
         "differ by a few dollars from this approximation. For every year of a 25-year schedule, see the "
         '<a href="/sba-loans/articles/sba-504-loan-amortization-schedule/">SBA 504 amortization schedule</a>.</p>'),
        ("Who Holds Your Debenture and Who You Pay",
         "<p>Once it's sold, your debenture sits in a pool held by a trustee, and investors own participation "
         "certificates in the pool. SBA guarantees timely payment of principal and interest on those "
         "certificates (13 CFR 120.941), which is why insurance companies, banks and money managers buy them "
         "at a fairly narrow spread. You never deal with the investors. Your monthly payment goes to the "
         "Central Servicing Agent, which SBA appoints to move funds among borrowers, CDCs and SBA "
         "(13 CFR 120.954); NADCO's guide names Guidehouse in that role. The CDC keeps servicing the loan "
         "for you.</p>"
         "<p>The same structure explains the prepayment rule. Investors are owed a fixed stream of payments, "
         "so the debenture can be repaid only in full, with a premium in roughly the first half of the term. "
         "The premium table is on our "
         '<a href="/sba-loans/articles/sba-504-loan-amortization-schedule/">amortization schedule</a> page. '
         'To compare real bank and CDC pairings, <a href="/match.html">get matched with SBA 504 lenders</a> '
         'or call <a href="tel:+15612680465">(561) 268-0465</a>. Approval is up to the lender, the CDC and SBA.</p>'),
    ],
    "faqs": [
        ("What is an SBA debenture?",
         "It's the bond a Certified Development Company issues to fund its share of a 504 loan, usually about "
         "40% of the project. SBA guarantees it, and it's sold to investors in a monthly pool, which is how "
         "the CDC can offer a fixed rate for 10, 20 or 25 years."),
        ("How is the SBA 504 debenture rate set?",
         "On the pricing date of the monthly sale, as a spread over the 10-year Treasury yield for 20- and "
         "25-year debentures, or the 5-year yield for 10-year debentures. SBA sets the rate with Treasury's "
         "approval. In NADCO's October 2026 example, 5.282% plus a 0.57% spread gave 5.85%."),
        ("When is my 504 rate locked?",
         "When your debenture is priced in the monthly sale, which happens after closing. Missing a cut-off "
         "moves you to the next month's sale and its rate. The bank's first mortgage can often be locked "
         "earlier."),
        ("What is the difference between the 504 note rate and the effective rate?",
         "The note rate is the interest rate on your monthly note. The effective rate adds the ongoing SBA, "
         "CSA and CDC servicing fees. For offering 2026-26J the note rate was 5.906% and the full-term "
         "effective rate 6.984%. Neither is an APR, because upfront fees are left out."),
        ("How do you calculate interest on a 504 loan?",
         "Multiply the unpaid balance by the note rate and divide by 12 for each month's interest, then add "
         "the ongoing fees on the same balance. On a $414,000 debenture at 5.906%, the first month is about "
         "$2,038 of interest plus about $322 of fees."),
        ("Who do I make 504 debenture payments to?",
         "To SBA's Central Servicing Agent, monthly. The agent passes payments to the trustee, which pays "
         "investors semiannually. Your CDC still services the loan and is your contact."),
    ],
    "related": [
        ("/sba-loans/articles/sba-504-loan-rates/", "SBA 504 loan rates"),
        ("/sba-loans/articles/sba-504-loan-fees/", "SBA 504 loan fees"),
        ("/sba-loans/articles/sba-504-loan-amortization-schedule/", "SBA 504 amortization schedule"),
        ("/sba-loans/articles/what-is-an-sba-504-loan/", "What is an SBA 504 loan?"),
        ("/sba-loans/articles/sba-504-lenders/", "SBA 504 lenders"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [NADCO, CFR932, CFR890, CFR941, CFR954, SBA_504, SOP],
}]
