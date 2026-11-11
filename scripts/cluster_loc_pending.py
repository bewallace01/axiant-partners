# -*- coding: utf-8 -*-
"""Why a line of credit application keeps pending - rewrite on the v2 renderer, 2026-11-11 batch.

Same URL (business-line-of-credit/articles/why-line-of-credit-application-keeps-pending/),
original datePublished 2026-03-19 kept. Title and meta are the CTR rewrite from 2026-11-09 (348
impressions at 5.6, 0 clicks then) and are kept unchanged. The body shared 55% of its 5-word
shingles with working-capital-loans/articles/why-your-working-capital-application-stuck-in-review/
(the same seven numbered causes); it is rewritten around what is specific to a revolving line:
the lender sizes a limit, checks existing liens and advances, reviews a borrowing base on secured
lines, issues counteroffers at a lower limit, and re-reviews at renewal.

Facts and where they come from (read 2026-11-11):
- 12 CFR 1002.9 (Regulation B): notice of approval, counteroffer or adverse action within 30
  days of a completed application; a 30-day notice of incompleteness for incomplete ones; the
  business-credit variations by revenue ($1 million or less vs more) in 1002.9(a)(3).
- UCC 9-322: generally the first secured party to file or perfect has priority.
- OCC Comptroller's Handbook, Asset-Based Lending: borrowing bases and field examinations.
Timing ranges reuse the site's published ones (how-fast-can-you-get-approved, a cited page,
linked not edited): 24-72 hours for initial review and 3-7 business days at online lenders, 1-3
weeks at banks. No lender is named. hub_by_hand: the LOC hub is hand-edited.
"""
from cluster_table import table

REGB = ("https://www.law.cornell.edu/cfr/text/12/1002.9",
        "12 CFR 1002.9 (Regulation B): Notifications",
        "The 30-day notice after a completed application, incompleteness notices and the business-credit rules.")
UCC = ("https://www.law.cornell.edu/ucc/9/9-322",
       "UCC 9-322: Priorities among conflicting security interests",
       "Why an earlier UCC filing by another lender can come ahead of a new line's lien.")
OCC = ("https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/index-asset-based-lending.html",
       "OCC Comptroller's Handbook: Asset-Based Lending",
       "How lenders set borrowing bases on receivables and inventory and use field examinations.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Annual survey of small-business credit applications, approvals and lender types.")

CLUSTER = {
    "pillar": "business-line-of-credit.html",
    "hub": "business-line-of-credit/articles",
    "hub_by_hand": True,
    "crumb": "Business Line of Credit",
    "cta_inline": "Compare line of credit lenders",
    "cta_button": "Get Matched for a Line of Credit",
}

ARTICLES = [{
    "slug": "why-line-of-credit-application-keeps-pending",
    "date_published": "2026-03-19",
    "crumb": "Why Your Line of Credit Application Keeps Pending",
    "title": "Credit Application Pending or Under Review? What It Means",
    "og_title": "Credit Application Pending or Under Review? What It Means | Axiant Partners",
    "h1": "Why Your Line of Credit Application Keeps Pending",
    "headline": "Why Your Line of Credit Application Keeps Pending",
    "lede": "A revolving line is sized, not just approved, so it gets reviews a term loan doesn't. What each "
            "pending status means and what moves it",
    "meta_desc": "A pending business credit application usually means a manual check: missing statements, "
                 "verification or a backlog. How long it can take and what to do now.",
    "article_desc": "Why business line of credit applications stay pending: limit sizing, existing liens and "
                    "advances, borrowing-base review on secured lines, counteroffers and renewal reviews, with "
                    "typical timelines and your Regulation B notice rights.",
    "keywords": "line of credit application pending, credit application pending, credit application under review, "
                "business line of credit pending, line of credit approval time, line of credit counteroffer",
    "quick_answer": "A line of credit stays pending longer than a loan because the lender is sizing a "
                    "<strong>limit you can draw again and again</strong>, not approving one payment. It checks "
                    "existing liens and advances, how your deposits support a limit, and, on secured lines, the "
                    "collateral. Online lenders often finish in <strong>3-7 business days</strong>; banks commonly "
                    "take <strong>1-3 weeks</strong>. Those are typical ranges, not promises; Axiant Partners, a "
                    "business-loan broker in Boca Raton, sees most stalls come from liens, limits or a counteroffer "
                    "waiting on you.",
    "sections": [
        ("What Each Pending Status Usually Means",
         "<p>Portals use different words, but a line of credit application tends to move through the same "
         "stages. Knowing which one you're in tells you whether to wait or act.</p>"
         + table(["Status you see", "What's usually happening", "Your move"], [
             ["Submitted / received", "Automated checks: identity, credit pull, bank connection", "Nothing yet; confirm the bank link worked"],
             ["In review / under review", "An underwriter is sizing the limit from deposits and debts", "Answer questions the same day"],
             ["Pending documents", "Something is missing or unreadable", "Send exactly what was asked, as full PDFs"],
             ["Pending verification", "Business, ownership or bank data didn't match", "Explain the mismatch in writing"],
             ["Approved, pending acceptance", "A limit was offered, often lower than you asked", "Accept, negotiate or decline"],
             ["Approved, pending setup", "Agreement, guarantee or draw account still open", "Sign and finish the account link"],
         ])
         + "<p>The last two catch people out. An offer that sits in your inbox shows as pending on the "
         "lender's side, and an approved line can't fund until the agreement is signed and the draw account "
         "is verified.</p>"),
        ("Why Lines of Credit Get More Review Than Loans",
         "<p>With a term loan the lender knows its exposure on day one. With a revolving line you can draw, "
         "repay and draw again, so the lender underwrites the worst case: the full limit drawn when your "
         "business is at its weakest. That shows up in four places.</p>"
         "<ul>"
         "<li><strong>Limit sizing.</strong> The underwriter works out how large a line your deposits and "
         "existing payments can carry. If you asked for more than that, the file sits while they decide "
         "whether to counter. See <a href=\"/business-line-of-credit/articles/why-line-of-credit-limit-too-low/\">why "
         "a line of credit limit comes in low</a>.</li>"
         "<li><strong>Existing liens.</strong> Many lines are secured by a general lien on business assets. "
         "If another lender or a cash advance company already filed a UCC-1, it generally comes first, so "
         "the new lender may want it released, subordinated or paid off before it approves.</li>"
         "<li><strong>Existing advances.</strong> Daily or weekly debits from a merchant cash advance reduce "
         "the cash a line could be repaid from, and some lenders won't open a line behind one.</li>"
         "<li><strong>Collateral review on secured lines.</strong> A line secured by receivables or "
         "inventory is sized by a borrowing base, and bank asset-based lenders may run a field exam of "
         "your books before closing.</li>"
         "</ul>"),
        ("Typical Timelines by Lender Type",
         "<p>These are ranges commonly seen, not guarantees. A clean file at the right lender moves at the "
         "fast end; a lien, a mismatch or a counteroffer adds days at any of them.</p>"
         + table(["Lender type", "Initial decision", "Full approval to first draw"], [
             ["Online / fintech line", "24-72 hours", "About 3-7 business days"],
             ["Bank unsecured line", "Days to a week", "About 1-3 weeks"],
             ["Bank secured or asset-based line", "After financials are reviewed", "Longer: collateral review and any field exam come first"],
             ["SBA line (CAPLines)", "After the lender's SBA review", "Weeks, as with other SBA loans"],
         ])
         + "<p>For the full breakdown, see "
         '<a href="/business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit/">how '
         "fast you can get approved for a business line of credit</a>.</p>"),
        ("How Long Can a Lender Leave It Pending?",
         "<p>Not indefinitely. Under Regulation B a lender generally has to tell you within <strong>30 "
         "days</strong> of a completed application whether it approved, made a counteroffer or declined. If "
         "the application is incomplete, it has 30 days to tell you what's missing, and the notice has to say "
         "what it needs and give you a reasonable time to send it. The rules for business credit vary with "
         "the business's revenue, with lighter requirements above $1 million, so ask the lender directly: "
         "\"Is my application complete, and if not, what exactly is missing?\"</p>"
         "<p>If you hear nothing for a week, that question usually gets a straight answer. If the lender "
         "says the file is complete and gives no decision date, it's reasonable to apply elsewhere, keeping "
         "in mind that each new application can mean another credit inquiry.</p>"),
        ("What to Send for Each Kind of Stall",
         table(["Stall", "What clears it fastest"], [
             ["Limit being sized", "Recent bank statements for every operating account and a list of current debts with payments"],
             ["UCC lien found", "The lien holder's payoff letter, a UCC-3 termination or a subordination agreement"],
             ["Cash advance in place", "The advance agreement and current balance; ask whether the lender will refinance it"],
             ["Borrowing base review", "An aged receivables report, an inventory listing and the most recent financial statements"],
             ["Identity or ownership mismatch", "Formation documents and ownership breakdown matching the application"],
             ["Counteroffer waiting", "A reply: accept, ask what would raise the limit, or decline"],
         ])
         + '<p>The full checklist is in <a href="/business-line-of-credit/articles/documents-needed-business-line-of-credit/">documents '
         'needed for a business line of credit</a>. If you would rather compare several lenders at once, '
         '<a href="/match.html">get matched</a>.</p>'),
        ("Worked Example: A Line Stuck Behind an Old Lien",
         "<p><strong>Illustrative.</strong> A contractor applies for a $75,000 line with an online lender on a "
         "Monday. The automated checks pass the same day and the status moves to \"in review\". On Wednesday the "
         "underwriter's lien search finds a UCC-1 filed two years earlier by an equipment lender, covering all "
         "business assets, even though that loan was paid off last spring. Nothing moves for a week, because the "
         "lender's request for a lien release went to an inbox nobody checks.</p>"
         "<p>When the owner calls, the fix takes two days: the old lender sends a paid-in-full letter and files a "
         "UCC-3 termination. The underwriter then offers $50,000 instead of $75,000, sized to the deposits, and "
         "that offer shows as \"approved, pending acceptance\" until the owner signs. Two of the three delays "
         "were on the borrower's side, which is typical.</p>"),
        ("Pending at Renewal: When an Existing Line Is Under Review",
         "<p>Many lines, especially at banks, run on a 12-month term and are re-reviewed before renewal. "
         "During that review the lender may ask for new financial statements or tax returns, and some "
         "pause new draws until it finishes. Send the renewal package early, before the maturity date, so "
         "the line doesn't lapse while it sits in review. If a draw is refused or the limit is cut at "
         'renewal, see <a href="/business-line-of-credit/articles/reasons-line-of-credit-draw-request-gets-declined/">why '
         'a draw request gets declined</a> and <a href="/business-line-of-credit/articles/why-business-lines-of-credit-get-cut-or-revoked/">why '
         "lines get cut or revoked</a>.</p>"),
    ],
    "faqs": [
        ("Why is my line of credit application still pending?",
         "Usually because the lender is still sizing the limit, found an existing lien or cash advance, is "
         "waiting on a document, or has made a counteroffer that's waiting for your reply. Ask whether the "
         "application is complete and what is missing."),
        ("How long does a business line of credit approval take?",
         "Online lenders commonly decide in 24-72 hours and fund in about 3-7 business days. Bank lines "
         "commonly take 1-3 weeks, and secured or SBA lines longer. These are typical ranges, not promises."),
        ("What does approved pending mean on a line of credit?",
         "The lender has offered a limit but something is still open: you haven't accepted the offer, signed "
         "the agreement or personal guarantee, or verified the account draws will go to."),
        ("How long can a lender keep a credit application pending?",
         "Under Regulation B a lender generally must notify you within 30 days of a completed application, "
         "and within 30 days tell you what's missing if it's incomplete. Requirements are lighter for "
         "businesses with more than $1 million in revenue."),
        ("Can a UCC lien hold up a line of credit?",
         "Yes. If another lender already filed a lien on business assets, it generally has priority, so a new "
         "line lender may ask for a payoff, a termination or a subordination before approving."),
    ],
    "related": [
        ("/business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit/",
         "How Fast Can You Get Approved for a Business Line of Credit?"),
        ("/business-line-of-credit/articles/why-line-of-credit-limit-too-low/", "Why your line of credit limit came in low"),
        ("/business-line-of-credit/articles/business-line-of-credit-requirements/", "Business Line of Credit Requirements"),
        ("/business-line-of-credit/articles/documents-needed-business-line-of-credit/", "Documents Needed for a Business Line of Credit"),
        ("/working-capital-loans/articles/why-your-working-capital-application-stuck-in-review/",
         "Working capital application stuck in review?"),
        ("/match.html", "Get Matched"),
    ],
    "sources": [REGB, UCC, OCC, SBCS],
}]
