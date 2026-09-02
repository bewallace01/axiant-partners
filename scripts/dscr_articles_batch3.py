# -*- coding: utf-8 -*-
"""Batch 3 of the DSCR cluster - articles 9-14 of 14.

Same rules as batches 1 and 2: ranges described as conventional across DSCR
lenders, never quoted as any lender's terms. No funded totals, no years in
business, no testimonials, no named lender rates. One entity: Axiant Partners,
(561) 268-0465, Boca Raton.
"""
from dscr_articles_batch1 import SLOOS, CFPB, IRS_527, HUD_MF, CENSUS_HV
from dscr_articles_batch2 import FTC

ARTICLES = [
    # ------------------------------------------------------------------ 9 --
    {
        "slug": "why-dscr-loans-get-denied",
        "crumb": "Why DSCR Loans Get Denied",
        "title": "Why DSCR Loans Get Denied: The Seven Common Reasons | Axiant",
        "og_title": "Why DSCR Loans Get Denied: The Seven Common Reasons",
        "h1": "Why DSCR Loans Get Denied",
        "headline": "Why DSCR Loans Get Denied",
        "lede": "The failures that show up after application rather than before, "
                "and which of them you can still fix",
        "meta_desc": "Why DSCR loans get denied: the ratio missing after real taxes and "
                     "insurance, appraisal and rent-schedule shortfalls, credit and reserve "
                     "gaps, property type, and entity paperwork. What to fix.",
        "article_desc": "The most common reasons a DSCR file is declined, and which of "
                        "them can be corrected before reapplying.",
        "keywords": "dscr loan denied, dscr loan declined, why dscr loan rejected, "
                    "dscr appraisal low, dscr loan problems",
        "quick_answer": "Most DSCR declines come down to the ratio missing once "
                        "<strong>reassessed taxes and a real insurance quote</strong> go in, "
                        "or the appraisal coming back below expectation on value or market "
                        "rent. Credit, reserves, property type and entity paperwork account "
                        "for most of the rest. Nearly all of it is visible before you apply "
                        "if you run the numbers the way an underwriter will.",
        "sections": [
            ("The Ratio Misses Once Real Numbers Go In",
             "<p>By some distance the most common decline, and the most avoidable. A deal "
             "pencils at application on estimated costs and fails at underwriting on actual "
             "ones.</p>"
             "<p>Two lines do most of the damage. <strong>Property taxes</strong> get "
             "budgeted at the seller's current bill, and in states that reassess on sale "
             "the real figure lands materially higher. <strong>Insurance</strong> gets "
             "estimated from last year's premium, and in coastal and wildfire markets "
             "premiums have moved sharply enough to swallow a thin margin on their own.</p>"
             "<p>Both sit in the denominator on a PITI program, so both push the ratio "
             "down directly. Run your own arithmetic with the reassessed tax figure and a "
             "bound insurance quote before you apply &mdash; the "
             "<a href=\"../how-dscr-is-calculated/\">calculation walkthrough</a> shows "
             "where each lands.</p>"),
            ("The Appraisal Comes In Short",
             "<p>An appraisal can sink a DSCR file two separate ways, and investors "
             "usually only anticipate the first.</p>"
             "<ul>"
             "<li><strong>Value below expectation.</strong> Reduces the maximum loan at a "
             "given loan-to-value, so either more cash is needed at closing or the deal "
             "does not fit.</li>"
             "<li><strong>Market rent below expectation.</strong> The rent schedule &mdash; "
             "Form 1007 for single-family, Form 1025 for two to four units &mdash; feeds "
             "the income side. Underwriters generally take the lower of it and your lease, "
             "so a weak rent opinion caps the ratio no matter what the tenant pays.</li>"
             "</ul>"
             "<p>On a vacant property the rent schedule is the entire income side, which "
             "makes it worth supplying genuine comparable rentals rather than leaving the "
             "selection to chance. A rebuttal with real comparables is a legitimate "
             "response to a weak opinion, not an argument.</p>"),
            ("Credit, Reserves and the Personal Side",
             "<p>DSCR removes personal <em>income</em> from underwriting. It does not "
             "remove the borrower.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>What is still checked</th><th>Why it declines a file</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"Checked\">Credit score</td>"
             "<td data-label=\"Why\">Below a program's floor, or a recent derogatory event "
             "inside its lookback</td></tr>"
             "<tr><td data-label=\"Checked\">Reserves</td>"
             "<td data-label=\"Why\">Not enough months of payments left after closing, "
             "particularly on thin-ratio files</td></tr>"
             "<tr><td data-label=\"Checked\">Recent housing events</td>"
             "<td data-label=\"Why\">Foreclosure, short sale or bankruptcy inside the "
             "program's window</td></tr>"
             "<tr><td data-label=\"Checked\">Source of down payment</td>"
             "<td data-label=\"Why\">Funds that cannot be traced, or that arrived "
             "unexplained</td></tr>"
             "<tr><td data-label=\"Checked\">Citizenship / residency status</td>"
             "<td data-label=\"Why\">Program-specific; some accept foreign nationals, many "
             "do not</td></tr>"
             "</tbody></table></div>"
             "<p>Reserves catch people out most often, because they are the requirement "
             "least likely to be mentioned early. Ask what is needed after closing, not "
             "just at it.</p>"),
            ("The Property Itself",
             "<p>Some declines are about the asset rather than the arithmetic:</p>"
             "<ul>"
             "<li><strong>Condition.</strong> An appraisal noting deferred maintenance or "
             "habitability issues can require repairs before funding.</li>"
             "<li><strong>Property type.</strong> Rural acreage, mixed-use, unusual "
             "construction, manufactured homes and very small units all sit outside some "
             "programs.</li>"
             "<li><strong>Unit count.</strong> Many DSCR programs stop at four units; "
             "beyond that it becomes commercial underwriting.</li>"
             "<li><strong>Short-term letting restrictions.</strong> Where the income is "
             "short-term and local rules prohibit it, the income generally is not counted. "
             "See <a href=\"../dscr-loans-short-term-rentals/\">DSCR loans for short-term "
             "rentals</a>.</li>"
             "<li><strong>HOA problems.</strong> Litigation or low owner-occupancy in a "
             "condo project can fail a lender's project review even when your file is "
             "perfect.</li>"
             "</ul>"),
            ("Paperwork and Timing",
             "<p>The last group is administrative, and the most frustrating because it has "
             "nothing to do with the deal:</p>"
             "<ul>"
             "<li><strong>Entity documents.</strong> An LLC not in good standing, not "
             "qualified in the property's state, or an operating agreement that does not "
             "clearly authorise the signer. See "
             "<a href=\"../llc-vesting-dscr-loans/\">holding title in an LLC</a>.</li>"
             "<li><strong>Insurance in the wrong name.</strong> A policy issued to you "
             "personally when the loan is to the entity.</li>"
             "<li><strong>Leases that do not match.</strong> Rent on the application "
             "differing from the signed lease, or a lease with no proof of payment behind "
             "it.</li>"
             "<li><strong>Slow responses.</strong> Conditions left unanswered until a rate "
             "lock expires.</li>"
             "</ul>"
             "<p>None of these is a judgement on the investment. All of them are avoidable "
             "with a file assembled before it is needed.</p>"),
            ("What to Do After a Decline",
             "<p>A decline from one lender is not a verdict on the property. The useful "
             "sequence:</p>"
             "<ul>"
             "<li><strong>Get the specific reason in writing.</strong> \"Ratio\" and "
             "\"appraisal\" lead to completely different fixes.</li>"
             "<li><strong>If it was the ratio</strong>, the levers are more down payment, "
             "longer amortization, an interest-only period, a rate buy-down, or a lender "
             "with a lower floor &mdash; see "
             "<a href=\"../minimum-dscr-ratio-by-lender-type/\">minimum DSCR by lender "
             "type</a>.</li>"
             "<li><strong>If it was the appraisal</strong>, a rebuttal with genuine "
             "comparables is worth attempting; a second appraisal at another lender is the "
             "fallback.</li>"
             "<li><strong>If it was credit or reserves</strong>, the fix is usually time "
             "and documentation rather than a different lender.</li>"
             "<li><strong>If it was the property type</strong>, shop specifically for a "
             "program that takes it. This is a matching problem, not a strengthening one.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("What is the most common reason a DSCR loan is denied?",
             "The coverage ratio missing once real numbers replace estimates &mdash; "
             "typically reassessed property taxes and a bound insurance quote coming in "
             "above what was budgeted. Both sit in the denominator on a PITI program, so "
             "both push the ratio down directly."),
            ("Can a low appraisal kill a DSCR loan?",
             "Two ways. A low <strong>value</strong> reduces the maximum loan at a given "
             "loan-to-value, and a low <strong>market rent opinion</strong> on the "
             "appraiser's rent schedule caps the income side. Underwriters generally take "
             "the lower of that opinion and your signed lease."),
            ("Does credit matter on a DSCR loan?",
             "Yes. DSCR removes personal income from underwriting, not the borrower. "
             "Credit score, recent housing events such as foreclosure or bankruptcy, "
             "reserves after closing and the traceable source of your down payment are all "
             "still reviewed."),
            ("Why was I declined when the property cash flows well?",
             "Most often reserves, property type or paperwork rather than the income. A "
             "property that covers its debt comfortably can still fail on an out-of-standing "
             "LLC, an insurance policy in the wrong name, a condo project review, or "
             "insufficient months of reserves after closing."),
            ("Can I reapply after a DSCR loan is denied?",
             "Usually, and often successfully &mdash; but only once you know the specific "
             "reason. A ratio decline, an appraisal decline and a credit decline lead to "
             "entirely different fixes, and reapplying without addressing the actual cause "
             "tends to produce the same answer."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../minimum-dscr-ratio-by-lender-type/", "Minimum DSCR by lender type"),
            ("/dscr-loan-requirements.html", "DSCR loan requirements"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
        ],
        "sources": [SLOOS, CFPB, CENSUS_HV],
    },

    # ----------------------------------------------------------------- 10 --
    {
        "slug": "dscr-loan-closing-costs-and-fees",
        "crumb": "Closing Costs and Fees",
        "title": "DSCR Loan Closing Costs and Fees: What to Budget | Axiant",
        "og_title": "DSCR Loan Closing Costs and Fees: What to Budget",
        "h1": "DSCR Loan Closing Costs and Fees",
        "headline": "DSCR Loan Closing Costs and Fees",
        "lede": "Which costs are the lender's, which are third-party, and which "
                "are negotiable once you know what to ask",
        "meta_desc": "DSCR loan closing costs: origination points, appraisal with rent "
                     "schedule, title and escrow, prepaids and reserves. What each is, which "
                     "are negotiable, and how to compare two quotes honestly.",
        "article_desc": "What makes up closing costs on a DSCR loan and which items are "
                        "genuinely negotiable.",
        "keywords": "dscr loan closing costs, dscr origination fee, dscr loan points, "
                    "rental property closing costs, dscr loan fees",
        "quick_answer": "DSCR closing costs generally run <strong>2% to 5% of the loan "
                        "amount</strong>, plus prepaid taxes and insurance and any required "
                        "reserves. The largest single line is usually "
                        "<strong>origination</strong>, quoted in points. Lender fees are "
                        "negotiable, third-party costs largely are not, and prepaids are not "
                        "a cost at all &mdash; they are your own money moving into escrow.",
        "sections": [
            ("The Three Kinds of Cost",
             "<p>Separating them is the whole skill in reading a quote, because they "
             "behave completely differently.</p>"
             "<ul>"
             "<li><strong>Lender charges.</strong> Origination points, underwriting, "
             "processing, document preparation. These are the lender's revenue and the "
             "part that is genuinely negotiable.</li>"
             "<li><strong>Third-party costs.</strong> Appraisal, title, escrow or "
             "attorney, recording, credit report, flood determination. Passed through "
             "largely at cost; the lender has limited influence.</li>"
             "<li><strong>Prepaids and reserves.</strong> Property taxes and insurance "
             "collected in advance, plus any reserve requirement. Not a cost in the real "
             "sense &mdash; it is your money, sitting in escrow or your own account.</li>"
             "</ul>"
             "<p>Quotes that blur the three make an expensive loan look cheap. A lender "
             "showing low fees but heavy prepaids has not saved you anything.</p>"),
            ("What Each Line Is",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Line</th><th>Whose</th><th>Typical shape</th>"
             "<th>Negotiable?</th></tr></thead><tbody>"
             "<tr><td data-label=\"Line\">Origination</td><td data-label=\"Whose\">Lender</td>"
             "<td data-label=\"Shape\">Quoted in points, i.e. a percentage of the loan</td>"
             "<td data-label=\"Neg\">Yes &mdash; the main lever</td></tr>"
             "<tr><td data-label=\"Line\">Underwriting / processing</td>"
             "<td data-label=\"Whose\">Lender</td><td data-label=\"Shape\">Flat fee</td>"
             "<td data-label=\"Neg\">Sometimes, often waivable</td></tr>"
             "<tr><td data-label=\"Line\">Appraisal with rent schedule</td>"
             "<td data-label=\"Whose\">Third party</td>"
             "<td data-label=\"Shape\">Higher than a plain appraisal &mdash; it includes "
             "the 1007 or 1025</td><td data-label=\"Neg\">No</td></tr>"
             "<tr><td data-label=\"Line\">Title insurance and search</td>"
             "<td data-label=\"Whose\">Third party</td>"
             "<td data-label=\"Shape\">Scales with loan size; varies a lot by state</td>"
             "<td data-label=\"Neg\">Sometimes by shopping the provider</td></tr>"
             "<tr><td data-label=\"Line\">Escrow / settlement / attorney</td>"
             "<td data-label=\"Whose\">Third party</td>"
             "<td data-label=\"Shape\">Flat, state-dependent</td>"
             "<td data-label=\"Neg\">Sometimes</td></tr>"
             "<tr><td data-label=\"Line\">Recording and transfer taxes</td>"
             "<td data-label=\"Whose\">Government</td>"
             "<td data-label=\"Shape\">Set by jurisdiction</td><td data-label=\"Neg\">No</td></tr>"
             "<tr><td data-label=\"Line\">Prepaid taxes and insurance</td>"
             "<td data-label=\"Whose\">Escrow</td>"
             "<td data-label=\"Shape\">Months collected in advance</td>"
             "<td data-label=\"Neg\">Not a fee</td></tr>"
             "<tr><td data-label=\"Line\">Reserves</td><td data-label=\"Whose\">You</td>"
             "<td data-label=\"Shape\">Months of payments retained</td>"
             "<td data-label=\"Neg\">Program-dependent</td></tr>"
             "</tbody></table></div>"),
            ("Points, and Why They Are Not Simply a Fee",
             "<p>Origination is quoted in points because it is partly a pricing "
             "instrument. Paying more points usually buys a lower rate, and paying fewer "
             "raises it.</p>"
             "<p>That makes \"which quote has lower fees\" the wrong question. A lender "
             "charging two points at one rate and another charging half a point at a "
             "higher rate may be identical over your holding period, better if you sell "
             "early, worse if you hold for ten years.</p>"
             "<p>The comparison that works: ask each lender to quote the same rate, then "
             "compare fees; or the same fees, then compare rate. Comparing two quotes that "
             "differ on both at once tells you very little.</p>"
             "<p>The same logic runs through <a href=\"/dscr-loan-rates.html\">how DSCR "
             "pricing is built</a>.</p>"),
            ("Reserves Are the Line People Miss",
             "<p>Reserves are not paid to anyone. They are months of principal, interest, "
             "taxes and insurance you must still hold after closing, evidenced in an "
             "account.</p>"
             "<p>They catch investors out for two reasons. They are frequently not "
             "mentioned in an early quote, because they are not a fee. And they scale with "
             "the number of financed properties on some programs &mdash; the more rentals "
             "you hold, the more months you may be asked to keep.</p>"
             "<p>Ask early, and ask specifically: how many months, on this property, given "
             "how many financed properties I already have. It is a cash-planning question "
             "rather than a cost one, and getting it wrong at the last minute has killed "
             "otherwise sound closings.</p>"),
            ("Comparing Two Quotes Honestly",
             "<p>A short procedure that removes most of the noise:</p>"
             "<ul>"
             "<li><strong>Separate the three categories.</strong> Lender charges, "
             "third-party costs, prepaids and reserves.</li>"
             "<li><strong>Compare lender charges only.</strong> That is what each is "
             "actually charging you.</li>"
             "<li><strong>Normalise the rate.</strong> Ask both to quote at the same rate, "
             "or price the difference over your expected hold.</li>"
             "<li><strong>Ask which DSCR convention each uses</strong> &mdash; principal "
             "and interest, PITI or PITIA. It changes the loan you qualify for, which "
             "changes everything downstream.</li>"
             "<li><strong>Read the prepayment clause.</strong> A cheaper closing with a "
             "five-year penalty can be the more expensive loan. See "
             "<a href=\"../dscr-prepayment-penalties-step-downs/\">prepayment penalties "
             "and step-downs</a>.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("How much are closing costs on a DSCR loan?",
             "Generally <strong>2% to 5% of the loan amount</strong> in fees, plus prepaid "
             "taxes and insurance and any required reserves. Origination, quoted in points, "
             "is usually the largest single line."),
            ("Are DSCR closing costs higher than a conventional mortgage?",
             "Often somewhat, mainly because origination tends to be higher and the "
             "appraisal costs more &mdash; it includes a market rent schedule that a "
             "standard residential appraisal does not. Third-party and government costs are "
             "broadly the same."),
            ("Which DSCR closing costs are negotiable?",
             "The lender's own charges: origination points, underwriting, processing and "
             "document fees. Third-party costs such as the appraisal, recording and "
             "transfer taxes are passed through and largely fixed, though title and escrow "
             "can sometimes be shopped."),
            ("Are reserves part of closing costs?",
             "No. Reserves are months of payments you must still hold after closing, in "
             "your own account &mdash; they are not paid to anyone. They are easy to miss "
             "because they rarely appear in an early quote, and on some programs they "
             "scale with the number of financed properties you already own."),
            ("Can closing costs be rolled into the loan?",
             "Sometimes, within the loan-to-value cap. Be aware of the knock-on: financing "
             "the costs increases the loan, which increases the payment, which lowers the "
             "coverage ratio. On a thin file that can be the difference between an approval "
             "and a decline."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/dscr-loan-rates.html", "DSCR loan rates: how pricing is built"),
            ("../dscr-prepayment-penalties-step-downs/", "Prepayment penalties and step-downs"),
            ("/dscr-lenders.html", "How to compare DSCR lenders"),
        ],
        "sources": [CFPB, FTC, IRS_527],
    },

    # ----------------------------------------------------------------- 11 --
    {
        "slug": "dscr-vs-hard-money-for-rentals",
        "crumb": "DSCR vs Hard Money",
        "title": "DSCR vs Hard Money for Rentals: Which Fits When | Axiant",
        "og_title": "DSCR vs Hard Money for Rentals: Which Fits When",
        "h1": "DSCR vs Hard Money for Rentals",
        "headline": "DSCR vs Hard Money for Rentals",
        "lede": "Two different jobs — one buys time, the other holds a property. "
                "Where each belongs and how they work together",
        "meta_desc": "DSCR vs hard money for rental property: hard money buys speed and "
                     "condition tolerance for months, DSCR holds a stabilised rental for "
                     "years. How they differ and how investors use both.",
        "article_desc": "How DSCR loans and hard money differ in purpose, term and cost, "
                        "and when each is the right instrument.",
        "keywords": "dscr vs hard money, hard money rental property, bridge loan vs dscr, "
                    "dscr refinance hard money, short term vs long term investor loan",
        "quick_answer": "They do different jobs. <strong>Hard money</strong> is short-term "
                        "capital &mdash; months, not years &mdash; priced for speed and "
                        "tolerant of a property that is not yet rentable. <strong>DSCR</strong> "
                        "is long-term financing for a property that already produces rent. "
                        "Most investors do not choose between them: they buy and renovate with "
                        "one, then refinance into the other.",
        "sections": [
            ("Different Instruments, Not Competing Offers",
             "<p>Framing these as alternatives causes more bad decisions than any other "
             "misunderstanding in investor finance.</p>"
             "<p>Hard money answers \"I need to close quickly on something that will not "
             "pass a normal lender's condition standards.\" It is expensive because it is "
             "fast, short and secured against a property that may currently be "
             "uninhabitable.</p>"
             "<p>A DSCR loan answers \"this property produces rent and I want to hold it.\" "
             "It is cheaper because it is long, secured against stabilised income, and the "
             "lender has time to underwrite.</p>"
             "<p>Asking which is better is like asking whether a van is better than a car. "
             "The question is what you are doing this month.</p>"),
            ("The Practical Differences",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th></th><th>Hard money / bridge</th><th>DSCR</th></tr></thead><tbody>"
             "<tr><td data-label=\"\"><strong>Term</strong></td>"
             "<td data-label=\"Hard money\">Months &mdash; typically 6 to 24</td>"
             "<td data-label=\"DSCR\">Years &mdash; commonly 30-year amortization</td></tr>"
             "<tr><td data-label=\"\"><strong>Priced on</strong></td>"
             "<td data-label=\"Hard money\">Speed and asset value; often after-repair value</td>"
             "<td data-label=\"DSCR\">Coverage ratio, leverage and credit</td></tr>"
             "<tr><td data-label=\"\"><strong>Cost</strong></td>"
             "<td data-label=\"Hard money\">Materially higher rate, points at the front</td>"
             "<td data-label=\"DSCR\">Substantially lower rate over a long term</td></tr>"
             "<tr><td data-label=\"\"><strong>Property condition</strong></td>"
             "<td data-label=\"Hard money\">Tolerant &mdash; can be uninhabitable</td>"
             "<td data-label=\"DSCR\">Must be rentable and generally rented</td></tr>"
             "<tr><td data-label=\"\"><strong>Income required</strong></td>"
             "<td data-label=\"Hard money\">Usually none at underwriting</td>"
             "<td data-label=\"DSCR\">Rent, actual or appraiser's market opinion</td></tr>"
             "<tr><td data-label=\"\"><strong>Speed to close</strong></td>"
             "<td data-label=\"Hard money\">Days to a couple of weeks</td>"
             "<td data-label=\"DSCR\">Weeks</td></tr>"
             "<tr><td data-label=\"\"><strong>Repayment</strong></td>"
             "<td data-label=\"Hard money\">Often interest-only with a balloon</td>"
             "<td data-label=\"DSCR\">Amortising, sometimes interest-only for a period</td></tr>"
             "</tbody></table></div>"
             "<p>The row that matters most is the first. Hard money has a maturity date "
             "measured in months, and it arrives whether or not your plan worked.</p>"),
            ("How They Work Together",
             "<p>The standard investor sequence uses both, in order:</p>"
             "<ul>"
             "<li><strong>Buy with hard money</strong>, because the property needs work "
             "and the seller needs a fast close.</li>"
             "<li><strong>Renovate</strong>, keeping every invoice, permit and photograph "
             "&mdash; that file becomes the evidence for the refinance.</li>"
             "<li><strong>Rent it</strong>, because a signed lease strengthens the income "
             "side.</li>"
             "<li><strong>Refinance into a DSCR loan</strong>, repaying the hard money and "
             "converting to long-term debt.</li>"
             "</ul>"
             "<p>The refinance is the load-bearing step, and it is worth arranging before "
             "the hard money matures rather than after. Two things govern its timing: "
             "whether the property clears the coverage ratio at the new payment, and "
             "whether you have owned it long enough for the lender to use current value "
             "rather than your cost &mdash; see "
             "<a href=\"../dscr-loans-no-seasoning/\">DSCR loans with no seasoning</a>.</p>"
             "<p>Our <a href=\"/commercial-bridge-loans.html\">commercial bridge loans</a> "
             "page covers the short-term side of that sequence.</p>"),
            ("When Hard Money Is the Right Answer",
             "<ul>"
             "<li>The property will not pass a condition review &mdash; no working "
             "kitchen, systems out, uninhabitable</li>"
             "<li>The close has to happen in days rather than weeks</li>"
             "<li>You are buying at auction or from a seller who needs certainty over price</li>"
             "<li>The plan is to sell within months, so a long-term rate is irrelevant</li>"
             "<li>The value is in the renovation and you need capital against after-repair "
             "value rather than current value</li>"
             "</ul>"
             "<p>In all of these the high rate is buying something specific. Paying it for "
             "months is a cost of doing the deal; paying it for years is a mistake.</p>"),
            ("When DSCR Is the Right Answer",
             "<ul>"
             "<li>The property is rented, or rentable and ready to let</li>"
             "<li>You intend to hold it rather than flip it</li>"
             "<li>The rent covers the payment at the lender's floor</li>"
             "<li>You want amortising debt at a rate that works over years</li>"
             "<li>You are exiting a bridge or hard-money loan that is approaching maturity</li>"
             "</ul>"
             "<p>The failure mode to avoid is staying in hard money because the refinance "
             "was never arranged. A short-term loan reaching maturity without an exit is "
             "how investors end up selling on someone else's timetable rather than their "
             "own. If a flip has become a hold, "
             "<a href=\"../dscr-exit-from-a-flip/\">the DSCR exit</a> is the route out.</p>"),
        ],
        "faqs": [
            ("Is a DSCR loan cheaper than hard money?",
             "Materially, yes &mdash; lower rate and a long amortising term against hard "
             "money's short, front-loaded pricing. But they are not substitutes: hard money "
             "funds a property that is not yet rentable and closes in days, which a DSCR "
             "lender will not do."),
            ("Can I refinance hard money into a DSCR loan?",
             "That is the standard sequence. Buy and renovate with hard money, rent the "
             "property, then refinance into a DSCR loan to repay it. Two things govern the "
             "timing: whether the rent covers the new payment at the lender's floor, and "
             "the seasoning rule that decides whether current value or your cost basis is "
             "used."),
            ("Can I use a DSCR loan to buy a property that needs work?",
             "Usually not while it needs work. DSCR lending is secured against income, and "
             "a property that cannot be let does not produce any. Bridge or hard money "
             "covers that phase, with a DSCR refinance once the property is rentable."),
            ("How fast can each close?",
             "Hard money can close in days to a couple of weeks, which is much of what you "
             "are paying for. A DSCR loan takes weeks, since it needs an appraisal with a "
             "rent schedule, title work and full underwriting."),
            ("What happens if my hard money loan matures before I refinance?",
             "You are exposed. Extensions are sometimes available and usually cost points, "
             "and the alternative is selling on the lender's timetable rather than yours. "
             "Arrange the takeout financing well before maturity rather than at it."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/commercial-bridge-loans.html", "Commercial bridge loans"),
            ("../dscr-exit-from-a-flip/", "Using a DSCR loan to exit a flip"),
            ("../dscr-loans-no-seasoning/", "DSCR loans with no seasoning"),
        ],
        "sources": [SLOOS, CFPB, FTC],
    },

    # ----------------------------------------------------------------- 12 --
    {
        "slug": "dscr-loans-first-time-investors",
        "crumb": "First-Time Investors",
        "title": "DSCR Loans for First-Time Investors: What to Expect | Axiant",
        "og_title": "DSCR Loans for First-Time Investors: What to Expect",
        "h1": "DSCR Loans for First-Time Investors",
        "headline": "DSCR Loans for First-Time Investors",
        "lede": "Whether you can get one with no rental track record, what "
                "changes without experience, and how to make a first file strong",
        "meta_desc": "DSCR loans for first-time investors: whether experience is "
                     "required, what changes without a track record, and how to assemble a "
                     "first file that underwrites cleanly.",
        "article_desc": "What first-time property investors should expect from DSCR "
                        "underwriting and how to strengthen a first application.",
        "keywords": "dscr loan first time investor, first rental property loan, "
                    "dscr no experience, first investment property financing",
        "quick_answer": "Yes, first-time investors can get DSCR loans &mdash; the property "
                        "qualifies, not your landlord CV. Expect some programs to ask for a "
                        "<strong>slightly larger down payment or more reserves</strong> "
                        "without a track record, and expect the property to be scrutinised "
                        "harder because there is no operating history behind you. A clean, "
                        "well-documented first file matters more than experience.",
        "sections": [
            ("Experience Is a Factor, Not a Gate",
             "<p>DSCR underwriting is built around the property, which is precisely why it "
             "is accessible to someone buying their first rental. There is no requirement "
             "to have managed property before, and no debt-to-income test that a first-time "
             "buyer would struggle with.</p>"
             "<p>Experience does still appear, as a compensating factor rather than a "
             "requirement. Where a lender is deciding whether to flex on a thin ratio or a "
             "higher leverage request, a documented track record helps. Without one, the "
             "file has to be stronger on its own terms.</p>"
             "<p>In practice that means a first-time investor is competing on the quality "
             "of the deal and the tidiness of the paperwork, both of which are entirely "
             "within your control.</p>"),
            ("What Changes Without a Track Record",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Area</th><th>What to expect</th></tr></thead><tbody>"
             "<tr><td data-label=\"Area\">Down payment</td>"
             "<td data-label=\"Expect\">Some programs ask for a little more than they "
             "would from an experienced investor</td></tr>"
             "<tr><td data-label=\"Area\">Reserves</td>"
             "<td data-label=\"Expect\">More months of payments retained after closing</td></tr>"
             "<tr><td data-label=\"Area\">Coverage ratio</td>"
             "<td data-label=\"Expect\">Less flexibility below a program's stated floor</td></tr>"
             "<tr><td data-label=\"Area\">Property type</td>"
             "<td data-label=\"Expect\">Straightforward long-let property is easiest; "
             "short-term and unusual assets are harder on a first file</td></tr>"
             "<tr><td data-label=\"Area\">Rate</td>"
             "<td data-label=\"Expect\">Broadly the same &mdash; pricing follows leverage, "
             "coverage and credit rather than experience</td></tr>"
             "</tbody></table></div>"
             "<p>None of this is prohibitive. It is the difference between a lender's best "
             "terms and its standard ones.</p>"),
            ("Make the Property Do the Work",
             "<p>Since the property carries the file, the strongest thing a first-time "
             "investor can do is choose one that underwrites easily:</p>"
             "<ul>"
             "<li><strong>Already rented, on a signed lease</strong>, with payment history "
             "you can evidence. It removes the largest uncertainty in the file.</li>"
             "<li><strong>A comfortable ratio, not a marginal one.</strong> Aiming for a "
             "cushion above the floor rather than exactly at it means an insurance quote "
             "coming in high does not sink the deal.</li>"
             "<li><strong>An ordinary property type.</strong> A single-family house or "
             "small multi-unit in a normal market is the easiest thing to finance.</li>"
             "<li><strong>Good condition.</strong> Deferred maintenance flagged in the "
             "appraisal can require repairs before funding.</li>"
             "</ul>"
             "<p>A first deal that is boring to an underwriter is a good first deal. There "
             "will be time for complicated later.</p>"),
            ("Assembling the File",
             "<p>What a DSCR lender will want, most of which you can gather before you "
             "even find a property:</p>"
             "<ul>"
             "<li><strong>Credit report</strong> &mdash; know your score before you apply, "
             "not after</li>"
             "<li><strong>Proof of funds</strong> for the down payment, and a traceable "
             "history for where it came from</li>"
             "<li><strong>Reserves</strong> evidenced in an account, after closing costs</li>"
             "<li><strong>The lease</strong>, if the property is tenanted</li>"
             "<li><strong>Entity documents</strong>, if you are holding title in an LLC "
             "&mdash; articles, operating agreement, EIN, good standing. See "
             "<a href=\"../llc-vesting-dscr-loans/\">holding title in an LLC</a></li>"
             "<li><strong>Insurance quote</strong> in the right name, bound before closing</li>"
             "</ul>"
             "<p>What you will not be asked for is tax returns, W-2s or a debt-to-income "
             "calculation. If a lender starts asking, you are being underwritten as an "
             "individual rather than on the property, and it is worth asking why.</p>"),
            ("The Mistakes First Files Make",
             "<p>Four patterns account for most first-time declines, and every one is "
             "avoidable:</p>"
             "<ul>"
             "<li><strong>Budgeting the seller's property tax bill.</strong> In states that "
             "reassess on sale the real figure is higher, and it lands straight in the "
             "denominator.</li>"
             "<li><strong>Estimating insurance.</strong> Get a bound quote early. In "
             "coastal and wildfire markets it is frequently the line that breaks the "
             "ratio.</li>"
             "<li><strong>Forgetting reserves.</strong> They are not a fee, so they rarely "
             "appear in an early quote &mdash; and then the cash is not there at closing.</li>"
             "<li><strong>Assuming rent equals income.</strong> Vacancy, management and "
             "maintenance all come off before the ratio is calculated. See "
             "<a href=\"../how-dscr-is-calculated/\">how DSCR is calculated</a>.</li>"
             "</ul>"
             "<p>Run the arithmetic the way an underwriter will, before you apply. "
             "<a href=\"../why-dscr-loans-get-denied/\">Why DSCR loans get denied</a> "
             "covers the rest of the list.</p>"),
        ],
        "faqs": [
            ("Can a first-time investor get a DSCR loan?",
             "Yes. DSCR underwriting is built around the property's income rather than the "
             "borrower's income or landlord history, so there is no requirement to have "
             "owned a rental before. Some programs ask for a slightly larger down payment "
             "or more reserves without a track record."),
            ("Do DSCR lenders require rental experience?",
             "Generally not as a requirement. Experience functions as a compensating "
             "factor &mdash; it helps when a lender is deciding whether to flex on a thin "
             "ratio or higher leverage &mdash; but its absence is not usually a decline on "
             "its own."),
            ("Is the rate higher for a first-time investor?",
             "Usually not by much. DSCR pricing follows leverage, coverage ratio and "
             "credit rather than experience. What more often differs is the down payment or "
             "reserve requirement rather than the rate itself."),
            ("What should I look for in a first rental to finance?",
             "Something an underwriter finds unremarkable: already rented on a signed "
             "lease, a coverage ratio comfortably above the floor rather than exactly at "
             "it, an ordinary property type, and good condition. A cushion in the ratio is "
             "what absorbs an insurance quote coming in higher than budgeted."),
            ("Will I need to provide tax returns?",
             "Not on a genuine DSCR loan. The product exists specifically to underwrite "
             "the property rather than your personal income, so tax returns, W-2s and a "
             "debt-to-income calculation are not part of it. If they are being requested, "
             "ask which product you are actually being quoted."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
            ("../why-dscr-loans-get-denied/", "Why DSCR loans get denied"),
            ("/dscr-loan-requirements.html", "DSCR loan requirements"),
        ],
        "sources": [CENSUS_HV, CFPB, IRS_527],
    },

    # ----------------------------------------------------------------- 13 --
    {
        "slug": "dscr-portfolio-loans-multiple-properties",
        "crumb": "Portfolio Loans",
        "title": "DSCR Portfolio Loans: Financing Multiple Properties | Axiant",
        "og_title": "DSCR Portfolio Loans: Financing Multiple Properties at Once",
        "h1": "DSCR Portfolio Loans for Multiple Properties",
        "headline": "DSCR Portfolio Loans for Multiple Properties",
        "lede": "One loan across several rentals — what it solves, what it "
                "costs in flexibility, and when separate loans are better",
        "meta_desc": "DSCR portfolio loans finance several rentals under one loan, "
                     "underwritten on blended coverage. What they solve, how release clauses "
                     "work, and when separate loans are the better structure.",
        "article_desc": "How DSCR portfolio loans work across multiple properties and "
                        "the trade-offs against financing each separately.",
        "keywords": "dscr portfolio loan, blanket loan rental properties, multiple "
                    "rental property financing, blanket mortgage investors, release clause",
        "quick_answer": "A portfolio or blanket DSCR loan finances several rentals under "
                        "<strong>one loan and one payment</strong>, underwritten on the "
                        "<strong>blended coverage ratio</strong> across all of them. It "
                        "solves administrative sprawl and lets a strong property carry a weak "
                        "one. The cost is flexibility: selling a single property requires a "
                        "<strong>release clause</strong>, and cross-collateralisation ties "
                        "the whole portfolio together.",
        "sections": [
            ("What a Portfolio Loan Actually Is",
             "<p>One loan, one note, one payment, secured against several properties at "
             "once. The lender underwrites the group rather than each asset in isolation, "
             "which changes the arithmetic in a way that can work strongly in your "
             "favour.</p>"
             "<p>Because coverage is calculated on the combined income against the combined "
             "debt service, a property that would fail on its own can be carried by "
             "stronger ones. A portfolio blending to 1.25 can contain something at 0.95 "
             "without that being fatal.</p>"
             "<p>The corollary is the part to think hardest about: the properties are now "
             "tied to each other. That is the whole trade.</p>"),
            ("Portfolio Loan Against Separate Loans",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th></th><th>One portfolio loan</th><th>Separate loans</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"\"><strong>Coverage tested</strong></td>"
             "<td data-label=\"Portfolio\">Blended across all properties</td>"
             "<td data-label=\"Separate\">Each property on its own</td></tr>"
             "<tr><td data-label=\"\"><strong>Weak property</strong></td>"
             "<td data-label=\"Portfolio\">Can be carried by the others</td>"
             "<td data-label=\"Separate\">Fails on its own merits</td></tr>"
             "<tr><td data-label=\"\"><strong>Closing costs</strong></td>"
             "<td data-label=\"Portfolio\">One set of lender fees</td>"
             "<td data-label=\"Separate\">One set per property</td></tr>"
             "<tr><td data-label=\"\"><strong>Selling one property</strong></td>"
             "<td data-label=\"Portfolio\">Needs a release clause; may require paying down</td>"
             "<td data-label=\"Separate\">Repay that loan, done</td></tr>"
             "<tr><td data-label=\"\"><strong>Refinancing one</strong></td>"
             "<td data-label=\"Portfolio\">Generally not possible in isolation</td>"
             "<td data-label=\"Separate\">Straightforward</td></tr>"
             "<tr><td data-label=\"\"><strong>Risk linkage</strong></td>"
             "<td data-label=\"Portfolio\">Cross-collateralised &mdash; a default reaches "
             "all of them</td>"
             "<td data-label=\"Separate\">Contained to one property</td></tr>"
             "<tr><td data-label=\"\"><strong>Administration</strong></td>"
             "<td data-label=\"Portfolio\">One payment, one renewal</td>"
             "<td data-label=\"Separate\">One of everything, per property</td></tr>"
             "</tbody></table></div>"),
            ("The Release Clause Is the Term That Matters",
             "<p>If you take one thing from this page: read the release clause before the "
             "rate.</p>"
             "<p>A release clause governs what happens when you sell one property out of "
             "the group. Without a workable one, selling a single asset can require "
             "repaying the entire loan &mdash; which is not a theoretical problem, it is "
             "the thing that traps portfolios.</p>"
             "<p>What to establish in writing:</p>"
             "<ul>"
             "<li><strong>Can a single property be released at all</strong>, and under what "
             "conditions</li>"
             "<li><strong>How much must be paid down</strong> to release it &mdash; often "
             "more than that property's share of the balance</li>"
             "<li><strong>What the remaining portfolio must still clear</strong> on "
             "coverage and leverage after the release</li>"
             "<li><strong>Whether a release fee applies</strong>, and whether prepayment "
             "penalties bite on the amount repaid</li>"
             "</ul>"
             "<p>A portfolio loan with a restrictive release clause is a decision about the "
             "next five years, not this month.</p>"),
            ("Cross-Collateralisation, Plainly",
             "<p>Cross-collateralisation means every property in the loan secures the whole "
             "debt. It is what allows the blended underwriting, and it is also the "
             "concentration of risk.</p>"
             "<p>If the portfolio stops performing, the lender's remedy is not limited to "
             "the property that caused the problem. One bad asset in a group of six can put "
             "the equity in the other five at issue &mdash; which is precisely the "
             "separation many investors set up their entity structure to achieve in the "
             "first place. See <a href=\"../llc-vesting-dscr-loans/\">holding title in an "
             "LLC</a> for what that structure does and does not protect.</p>"
             "<p>None of this makes portfolio lending wrong. It makes it a structure to "
             "choose deliberately rather than default into because it was simpler at "
             "closing.</p>"),
            ("When Each Structure Fits",
             "<p><strong>A portfolio loan tends to fit when:</strong></p>"
             "<ul>"
             "<li>You hold several stabilised rentals you intend to keep</li>"
             "<li>One or two would not qualify alone but the group is comfortable</li>"
             "<li>Administrative simplicity has real value at your scale</li>"
             "<li>You are consolidating several existing loans into one</li>"
             "</ul>"
             "<p><strong>Separate loans tend to fit when:</strong></p>"
             "<ul>"
             "<li>You may sell individual properties</li>"
             "<li>You want each asset's risk contained</li>"
             "<li>The properties differ enough that blended terms suit none of them</li>"
             "<li>You are still building and want flexibility to refinance one at a time</li>"
             "</ul>"
             "<p>Reserves are worth asking about either way: on many programs the "
             "requirement scales with the number of financed properties you hold, which is "
             "a cash-planning question that arrives late if you do not raise it early. See "
             "<a href=\"../dscr-loan-closing-costs-and-fees/\">closing costs and fees</a>.</p>"),
        ],
        "faqs": [
            ("What is a DSCR portfolio loan?",
             "One loan secured against several rental properties at once, with a single "
             "payment, underwritten on the <strong>blended coverage ratio</strong> across "
             "the group rather than property by property."),
            ("Can a weak property be included in a portfolio loan?",
             "Often, yes &mdash; that is one of the main reasons to use one. Because "
             "coverage is calculated across the whole group, stronger properties can carry "
             "a weaker one that would not qualify on its own."),
            ("What happens if I want to sell one property?",
             "It depends entirely on the release clause. A workable one lets you release a "
             "single property on agreed conditions, usually paying down more than that "
             "property's share of the balance. Without one, selling a single asset can "
             "require repaying the whole loan."),
            ("What does cross-collateralisation mean here?",
             "Every property in the loan secures the entire debt. It is what makes blended "
             "underwriting possible, and it also means a problem with one property is not "
             "contained to that property &mdash; the lender's remedy reaches the whole "
             "group."),
            ("Is a portfolio loan cheaper than separate loans?",
             "On closing costs usually yes, since there is one set of lender fees rather "
             "than one per property. On rate it depends on the blended profile. The larger "
             "consideration is not cost but flexibility &mdash; what it takes to sell or "
             "refinance a single property later."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../llc-vesting-dscr-loans/", "Holding title in an LLC"),
            ("../dscr-loan-closing-costs-and-fees/", "DSCR loan closing costs and fees"),
            ("../minimum-dscr-ratio-by-lender-type/", "Minimum DSCR by lender type"),
        ],
        "sources": [SLOOS, HUD_MF, CFPB],
    },

    # ----------------------------------------------------------------- 14 --
    {
        "slug": "dscr-exit-from-a-flip",
        "crumb": "Exiting a Flip",
        "title": "Using a DSCR Loan to Exit a Flip That Won't Sell | Axiant",
        "og_title": "Using a DSCR Loan to Exit a Flip That Won't Sell",
        "h1": "Using a DSCR Loan to Exit a Flip",
        "headline": "Using a DSCR Loan to Exit a Flip",
        "lede": "When a flip becomes a hold — how to convert short-term debt "
                "into a rental loan before the maturity date decides for you",
        "meta_desc": "A flip that will not sell can be refinanced into a DSCR loan and "
                     "held as a rental. How the exit works, what seasoning and coverage "
                     "require, and how to move before the bridge loan matures.",
        "article_desc": "How to convert a flip into a rental by refinancing short-term "
                        "debt into a DSCR loan, and the timing that governs it.",
        "keywords": "dscr exit flip, flip wont sell, refinance flip to rental, "
                    "bridge loan exit dscr, brrrr refinance, hard money takeout",
        "quick_answer": "If a flip is not selling, renting it and refinancing into a "
                        "<strong>DSCR loan</strong> converts short-term debt into long-term "
                        "debt and removes the maturity date from the equation. Two things "
                        "govern whether it works: whether the rent covers the new payment at "
                        "the lender's floor, and whether you have owned it long enough for "
                        "the lender to use <strong>current value rather than your cost</strong>. "
                        "Start the conversation early &mdash; a bridge loan at maturity has "
                        "no leverage.",
        "sections": [
            ("The Situation This Solves",
             "<p>A flip that does not sell is a timing problem before it is a money "
             "problem. The renovation is finished, the listing is quiet, and a short-term "
             "loan is running toward a maturity date that does not care.</p>"
             "<p>The options narrow as that date approaches. Cutting the price surrenders "
             "the margin the project existed to earn. Extending the bridge usually costs "
             "points and buys months. Doing nothing ends with the lender setting the "
             "timetable.</p>"
             "<p>The fourth option is to stop selling. Rent the property, refinance into a "
             "DSCR loan, and hold it &mdash; converting a deal that failed on its original "
             "terms into one that works on different ones.</p>"),
            ("What Has to Be True",
             "<p>Three conditions, and it is worth testing all three before committing to "
             "the plan:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Condition</th><th>What it means</th><th>If it fails</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"Condition\">The rent covers the payment</td>"
             "<td data-label=\"Means\">Coverage ratio clears the lender's floor at the new "
             "loan amount</td>"
             "<td data-label=\"Fails\">Borrow less, extend the term, or look for a lower "
             "floor</td></tr>"
             "<tr><td data-label=\"Condition\">Seasoning allows current value</td>"
             "<td data-label=\"Means\">You have owned it long enough to refinance against "
             "the appraisal rather than cost</td>"
             "<td data-label=\"Fails\">A short- or no-seasoning program, or wait</td></tr>"
             "<tr><td data-label=\"Condition\">The property is rentable</td>"
             "<td data-label=\"Means\">Finished, habitable, and lettable in that market</td>"
             "<td data-label=\"Fails\">Finish the work first &mdash; DSCR lends against "
             "income</td></tr>"
             "</tbody></table></div>"
             "<p>The first condition is the one people misjudge. A property priced to sell "
             "at a flip margin does not automatically produce enough rent to cover a loan "
             "against that same value.</p>"),
            ("Seasoning Decides the Timing",
             "<p>If you bought recently, the lender may lend against what you paid plus "
             "documented improvements rather than what the property is now worth. On a "
             "successful renovation those are very different numbers, and the difference is "
             "exactly the margin you were trying to realise.</p>"
             "<p>Programs vary from no seasoning requirement to twelve months, which makes "
             "it one of the terms most worth shopping specifically rather than accepting "
             "from the first lender. <a href=\"../dscr-loans-no-seasoning/\">DSCR loans "
             "with no seasoning</a> covers how the shorter windows work and what they "
             "cost.</p>"
             "<p>Keep the renovation file either way &mdash; itemised invoices, permits, "
             "before-and-after photographs and proof of payment. Where a lender allows cost "
             "plus improvements, that file is what makes the improvements count.</p>"),
            ("Get It Rented First",
             "<p>A signed lease materially strengthens the file. It removes the largest "
             "uncertainty on the income side and gives the underwriter something "
             "contractual to work from rather than an opinion.</p>"
             "<p>Two practical notes. Underwriters generally take the lower of the lease "
             "and the appraiser's market rent, so an above-market lease signed in a hurry "
             "does not lift the ratio &mdash; see "
             "<a href=\"../what-counts-as-rental-income-dscr/\">what counts as rental "
             "income</a>. And a vacant property is still financeable, on the appraiser's "
             "rent opinion alone, though some programs apply a larger vacancy deduction or "
             "lower leverage.</p>"
             "<p>If the property can be let quickly at a sensible rent, let it. The file "
             "gets easier and the carrying cost stops.</p>"),
            ("Move Before the Maturity Date",
             "<p>This is the whole of the practical advice. A DSCR refinance takes weeks "
             "&mdash; appraisal with a rent schedule, title work, underwriting. Starting "
             "the process a fortnight before a bridge loan matures means negotiating from "
             "no position at all.</p>"
             "<p>A workable sequence:</p>"
             "<ul>"
             "<li><strong>Decide early that the flip has become a hold.</strong> The month "
             "you would otherwise spend hoping is the month the refinance needs.</li>"
             "<li><strong>Check the coverage ratio at a realistic rent</strong> before "
             "anything else. If it does not clear, the plan needs changing, not "
             "accelerating.</li>"
             "<li><strong>Confirm the seasoning position</strong> with a specific lender "
             "rather than assuming.</li>"
             "<li><strong>Get it let</strong>, or get a market rent opinion.</li>"
             "<li><strong>Check the bridge loan's prepayment terms</strong> &mdash; "
             "repaying early can carry a charge; see "
             "<a href=\"../dscr-prepayment-penalties-step-downs/\">prepayment penalties</a>.</li>"
             "<li><strong>Start the DSCR application with weeks of margin</strong>, not "
             "days.</li>"
             "</ul>"
             "<p>A flip converted deliberately into a rental is an ordinary outcome. A flip "
             "converted at the last minute is a distressed one, and the difference is "
             "mostly calendar.</p>"),
        ],
        "faqs": [
            ("Can I refinance a flip into a rental loan?",
             "Yes &mdash; renting the property and refinancing into a DSCR loan is the "
             "standard route when a flip will not sell. It replaces short-term debt with "
             "long-term amortising debt and removes the maturity date from the problem."),
            ("What stops a flip-to-rental refinance from working?",
             "Usually one of two things. The rent does not cover the payment at the "
             "lender's coverage floor, or seasoning rules mean the lender uses your "
             "purchase price plus improvements rather than the post-renovation appraisal. "
             "Both are checkable before you commit to the plan."),
            ("How long do I need to own it before refinancing at current value?",
             "It depends on the program. Some DSCR lenders have no seasoning requirement, "
             "others use three to six months, and conventional financing often wants "
             "twelve. It is one of the terms most worth shopping for specifically when a "
             "renovation has changed the value."),
            ("Should I rent it before refinancing?",
             "Generally yes. A signed lease with evidenced payments is the strongest "
             "version of the income side. A vacant property can still be financed on the "
             "appraiser's market rent opinion, though some programs apply a larger vacancy "
             "deduction or lower maximum leverage."),
            ("When should I start the refinance?",
             "Weeks before the bridge loan matures, not days. A DSCR refinance needs an "
             "appraisal with a rent schedule, title work and full underwriting. Arriving at "
             "maturity without a completed takeout means negotiating from no position."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/fix-and-flip.html", "Fix and flip loans"),
            ("../dscr-loans-no-seasoning/", "DSCR loans with no seasoning"),
            ("../dscr-vs-hard-money-for-rentals/", "DSCR vs hard money for rentals"),
        ],
        "sources": [SLOOS, CFPB, IRS_527],
    },
]
