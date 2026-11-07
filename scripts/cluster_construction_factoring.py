# -*- coding: utf-8 -*-
"""Construction factoring rates - new spoke, from the 2026-11-07 daily batch.

Search Console, Oct 7 to Nov 4 2026: "construction factoring rates" 30 impressions, best position
18, "construction factoring" 29 at 28, on construction-invoice-factoring, which explains how it
works but publishes no price. Fees and advances reuse the site's published 1-5% and 80-95% from
invoice-factoring-rates; retainage of 5-10% comes from construction-invoice-factoring. There's no
separate construction range because the site has no deal data for one, and the page says so.
Federal facts read 2026-11-07: 31 USC 3727(c). no_hub: the folder's index isn't generated.
"""
from cluster_table import table

ACA = ("https://www.law.cornell.edu/uscode/text/31/3727",
       "31 U.S.C. 3727: Assignments of claims",
       "When a federal contract payment can be assigned to a financing institution, and the required notices.")
FAR = ("https://www.acquisition.gov/far/52.232-27",
       "FAR 52.232-27: Prompt Payment for Construction Contracts",
       "Federal payment timing on construction contracts, including when subcontractors must be paid.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research on small business credit, including how costs are disclosed to borrowers.")

CLUSTER = {
    "pillar": "working-capital-loans.html",
    "hub": "working-capital-loans/articles",
    "no_hub": True,
    "back_href": "/working-capital-loans/articles/",
    "crumb": "Working Capital Loans",
    "cta_inline": "See real pricing on your progress billings",
    "cta_button": "Get Matched With Construction Factors",
}

ARTICLES = [{
    "slug": "construction-factoring-rates",
    "crumb": "Construction Factoring Rates",
    "title": "Construction Factoring Rates: Fees and Advances | Axiant",
    "og_title": "Construction Factoring Rates: What Subcontractors Really Pay",
    "h1": "Construction Factoring Rates: What Subcontractors Really Pay",
    "headline": "Construction Factoring Rates: What Subcontractors Really Pay",
    "lede": "Fees, advance rates and why retainage changes the math, with a progress-billing example you can "
            "rerun on your own pay application",
    "meta_desc": "Construction factoring rates typically fall within the 1-5% per invoice range, with 80-95% advances on the payable amount, not retainage. See a worked example.",
    "article_desc": "Typical construction factoring fees and advance rates, how retainage and slow pay change "
                    "the real cost, and what to ask a factor.",
    "keywords": "construction factoring rates, construction factoring, factoring for construction subcontractors, "
                "construction invoice factoring cost, retainage factoring",
    "quick_answer": "Construction factoring usually costs within the general range of <strong>1-5% per invoice</strong>, "
                    "with advances of <strong>80-95%</strong> on the approved, payable part of a progress billing. "
                    "Retainage, commonly 5-10%, is usually excluded, and slow payers push you up the range. Axiant "
                    "Partners, a business-loan broker in Boca Raton, matches contractors with factors that "
                    "handle construction. These are typical ranges across factors, not a quote.",
    "sections": [
        ("Typical Construction Factoring Costs",
         "<p>We don't publish a separate construction price, because factors quote this work case by case. The table below "
         "applies the ranges on our <a href=\"/working-capital-loans/articles/invoice-factoring-rates/\">invoice factoring "
         "rates</a> page to situations a contractor can recognize.</p>"
         + table(["Your receivable", "Likely fee zone", "Why"], [
             ["Strong GC, pays near net 30", "About 1-2%", "Good credit and fast pay, with steady volume"],
             ["Mixed GCs, average pay", "About 2-3.5%", "Moderate volume and more verification"],
             ["Slow GC, net 60-90", "About 3.5-5%", "More tiers while the invoice is open"],
             ["Pay-if-paid, thin file", "4-5% or more, or a decline", "Higher chance that payment never comes due"],
         ])
         + "<p>Many factors won't do construction at all, so expect fewer quotes than a staffing company would get. "
         "That is one reason a contractor can't assume the bottom of the range. Advance rates commonly run 80-95% "
         "of what's factored, with the rest held as a reserve until the customer pays.</p>"),
        ("Why Retainage Changes the Math",
         "<p>The percentage on the proposal applies to less than you billed. If a factor excludes retainage, your advance "
         "starts from the currently payable amount, so compare quotes on cash received, not on the headline fee. The "
         "mechanics are covered in our <a href=\"/working-capital-loans/articles/construction-invoice-factoring/\">construction "
         "invoice factoring</a> guide. This page is about the price.</p>"
         "<p>Watch for the money sitting in two places: retainage held by the GC, and the reserve held by the factor. On "
         "a long job, both can be outstanding while your payroll runs. If retainage is the bigger problem, see our guide "
         "to the <a href=\"/construction-business-financing/retainage-cash-flow-gap/\">retainage cash flow gap</a>.</p>"),
        ("Worked Example: A $100,000 Progress Billing",
         "<p><strong>Illustrative numbers, not a quote.</strong> A subcontractor bills $100,000 on an approved pay application "
         "with 10% retainage. The factor advances 85% of the payable amount and charges 3.5% for 60 days.</p>"
         + table(["Item", "Math", "Amount"], [
             ["Billed", "Approved pay application", "$100,000"],
             ["Retainage held", "10%", "$10,000"],
             ["Payable amount", "Billed less retainage", "$90,000"],
             ["Advance today", "85% of $90,000", "$76,500"],
             ["Fee at 60 days", "3.5% of $90,000", "$3,150"],
             ["Reserve released later", "$90,000 less advance and fee", "$10,350"],
         ])
         + "<p>So you get <strong>$76,500 now</strong> on a $100,000 billing, or about 76.5 cents on the dollar. Annualized, "
         "$3,150 on $76,500 for 60 days is about 25%, which is useful for comparing with a "
         '<a href="/business-line-of-credit.html">line of credit</a>. That figure is only arithmetic. It doesn\'t include '
         "setup, wire or minimum fees. Rerun it at net 90 under tiered pricing, because the fee may rise as the "
         "invoice stays open.</p>"),
        ("What Moves Your Rate",
         "<ul>"
         "<li><strong>Who pays you.</strong> A factor relies on the GC or owner's credit more than yours, so a strong payer helps most.</li>"
         "<li><strong>Billing quality.</strong> Signed pay applications are easier to fund than billings still open to adjustment.</li>"
         "<li><strong>Contract language.</strong> Pay-if-paid is riskier than pay-when-paid because it can decide whether you're paid at all.</li>"
         "<li><strong>Lien discipline.</strong> Preliminary notices and clean waivers protect the collateral behind the receivable.</li>"
         "<li><strong>Concentration.</strong> One GC on most of your billing can lower the advance or raise the fee.</li>"
         "<li><strong>Volume.</strong> Steady monthly volume generally earns better tiers than one-off billings.</li>"
         "</ul>"),
        ("Federal Jobs Have Their Own Rules",
         "<p>Factoring a federal receivable has an extra step. The "
         '<a href="https://www.law.cornell.edu/uscode/text/31/3727" rel="noopener nofollow" target="_blank">Assignment of '
         "Claims Act</a> lets money due on a federal contract be assigned to a financing institution if the contract doesn't "
         "forbid it. It goes to one party, and written notice must go to the contracting officer, any surety and the disbursing "
         "official. Primes need that paperwork, and it adds time, so ask about it before pricing the deal. Subcontractors bill "
         "the prime, not the government, and "
         '<a href="https://www.acquisition.gov/far/52.232-27" rel="noopener nofollow" target="_blank">FAR 52.232-27</a> sets '
         "payment timing for subs on federal jobs, which can make the receivable easier to judge. Bonded private jobs raise a "
         "similar question, so tell the factor if a surety is involved.</p>"),
        ("Fees to Ask About Beyond the Rate",
         "<ul>"
         "<li><strong>Setup or due diligence.</strong> A one-time charge to open the account, which may be higher for construction review.</li>"
         "<li><strong>Tier schedule.</strong> The exact fee at 30, 45, 60 and 90 days, not just the first tier.</li>"
         "<li><strong>Minimums and exit.</strong> Monthly minimum volume and the penalty for leaving early.</li>"
         "<li><strong>Recourse.</strong> When an unpaid invoice comes back to you, and how fast.</li>"
         "<li><strong>Disputes.</strong> What happens when a GC back-charges or adjusts a billing after you've been advanced.</li>"
         "<li><strong>Retainage.</strong> Whether it's excluded, discounted or financed separately, and on what terms.</li>"
         "</ul>"
         '<p>Is factoring even the right tool? See <a href="/invoice-factoring.html">invoice factoring</a> and the '
         '<a href="/construction-business-financing.html">construction financing</a> overview, or '
         '<a href="/match.html">get matched</a> with factors that handle progress billing, and compare the cash you keep '
         "after every fee. Business-purpose financing only; all terms are set by the funder.</p>"),
    ],
    "faqs": [
        ("What are typical construction factoring rates?",
         "Expect fees within the general 1-5% per invoice range, with advances of 80-95% on the approved, payable part of a "
         "progress billing. Slow payers, pay-if-paid clauses and thin files push toward the top of that range. These are "
         "typical ranges across factors, not a quote."),
        ("Does a factor advance against retainage?",
         "Usually not. Retainage is paid later and depends on completion, so most factors exclude it or discount it heavily. "
         "Some offer separate retainage financing."),
        ("How much cash do I get on a $100,000 progress billing?",
         "With 10% retainage and an 85% advance, about $76,500 up front. After a 3.5% fee on $90,000, about $10,350 of reserve "
         "comes later. That example is illustrative."),
        ("Why do many factors avoid construction?",
         "Progress billings can be adjusted or disputed, pay-if-paid clauses can make a payment contingent, and lien rights and "
         "waivers complicate collateral. Factors that do this work build those risks into their terms."),
        ("Can I factor a federal construction contract?",
         "Often, with an assignment under the Assignment of Claims Act if the contract doesn't forbid it, and with written notice "
         "to the required officials. It takes extra time, so raise it early."),
        ("Is a line of credit cheaper than construction factoring?",
         "Often, if you qualify, since factoring can be expensive when annualized. Factoring leans on your customer's credit, so "
         "it can fit younger contractors who can't get a large line yet."),
    ],
    "related": [
        ("/working-capital-loans/articles/construction-invoice-factoring/", "Construction invoice factoring"),
        ("/working-capital-loans/articles/invoice-factoring-rates/", "Invoice factoring rates"),
        ("/construction-business-financing/retainage-cash-flow-gap/", "The retainage cash flow gap"),
        ("/construction-business-financing/working-capital-subcontractors-invoices/", "Working capital for subcontractors"),
        ("/invoice-factoring.html", "Invoice factoring"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [ACA, FAR, CFPB],
}]
