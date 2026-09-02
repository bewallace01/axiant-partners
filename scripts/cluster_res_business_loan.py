# -*- coding: utf-8 -*-
"""Real-estate-secured business loans - 6 articles. Asset-equity cluster, 2 of 3.

Ranges are described as conventional across lenders, never quoted as anyone's
terms. No funded totals, no years in business, no testimonials, no named lender
rates. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
"""

CLUSTER = {
    "pillar": "real-estate-secured-business-loan.html",
    "hub": "real-estate-secured-business-loan/articles",
    "crumb": "Real-Estate-Secured Business Loans",
    "cta_inline": "See what your equity supports",
    "cta_button": "Get Matched for an Equity-Secured Loan",
    "hub_title": "Real-Estate-Secured Business Loan Guides | Axiant Partners",
    "hub_h1": "Real-Estate-Secured Business Loan Articles",
    "hub_lede": "Borrowing against property equity for the business - what "
                "lenders require behind a first mortgage, and what you sign",
    "hub_desc": "Guides to business borrowing secured on real estate: second and "
                "third position lending, cross-collateralisation, rental property "
                "as collateral, and how fast an equity-secured loan closes.",
    "hub_intro": "Property equity is usually the cheapest collateral a business "
                 "owner has, and the most consequential to pledge. These guides "
                 "cover what a lender behind a first mortgage actually requires, "
                 "what cross-collateralisation commits you to, and when secured "
                 "borrowing is the wrong answer. Start with "
                 "<a href=\"/real-estate-secured-business-loan.html\">real-estate-"
                 "secured business loans</a>, or compare with "
                 "<a href=\"/heloc-for-business.html\">a HELOC used for business</a>.",
    "hub_cta_h2": "Have equity in property you own?",
    "hub_cta_p": "Send the property, the balance on the first mortgage and what you "
                 "need. We will tell you plainly what position is available and what "
                 "it costs.",
}

SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards including commercial real "
         "estate - the public record of whether underwriting is tightening.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "cost and terms are presented to borrowers.")
CFPB_MTG = ("https://www.consumerfinance.gov/consumer-tools/mortgages/",
            "CFPB Mortgages",
            "Consumer Financial Protection Bureau guidance on mortgage products, "
            "closing process and borrower protections.")
FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Federal Trade Commission guidance on fee disclosure and the warning "
       "signs of predatory business credit.")
IRS_527 = ("https://www.irs.gov/publications/p527",
           "IRS Publication 527: Residential Rental Property",
           "The federal treatment of rental income and expenses - what an "
           "underwriter reads when a rental property is the collateral.")
HUD_MF = ("https://www.hud.gov/program_offices/housing/mfh",
          "HUD Multifamily Housing Programs",
          "Federal multifamily programs and their equity requirements, the "
          "benchmark conventional terms are quoted against.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms apply for and receive credit, including "
        "approval rates and funding speed by product.")

ARTICLES = [
    {
        "slug": "second-and-third-position-business-loans",
        "crumb": "Second and Third Position",
        "title": "Second and Third Position Business Loans Explained | Axiant",
        "og_title": "Second and Third Position Business Loans Explained",
        "h1": "Second and Third Position Business Loans",
        "headline": "Second and Third Position Business Loans",
        "lede": "Borrowing behind an existing mortgage - what position means, "
                "what it costs, and where lenders stop",
        "meta_desc": "Second and third position business loans sit behind an "
                     "existing mortgage. What lien position means for pricing and "
                     "recovery, how far down lenders will go, and what to check first.",
        "article_desc": "How subordinate lien position works on business borrowing "
                        "secured by real estate.",
        "keywords": "second position business loan, third position lien, "
                    "subordinate lien business, junior lien commercial",
        "quick_answer": "Position is the order lenders get repaid if the property is "
                        "sold. A <strong>second</strong> sits behind the first "
                        "mortgage and recovers only after it is satisfied; a "
                        "<strong>third</strong> sits behind both. Each step down "
                        "means a weaker recovery position, so pricing rises sharply "
                        "and the number of willing lenders falls. Beyond third, very "
                        "few will lend at all.",
        "sections": [
            ("What Position Actually Means",
             "<p>Lien position is a queue. If the property is sold or foreclosed, "
             "proceeds pay the first lienholder in full before the second sees "
             "anything, and the second in full before the third.</p>"
             "<p>That is the whole concept, and everything else follows from it. A "
             "second-position lender is not taking a slightly worse version of the "
             "first lender's risk &mdash; in a downturn where the property is worth "
             "less than the first mortgage, they recover nothing at all while the "
             "first is made whole.</p>"
             "<p>Price reflects that asymmetry, and it is why the step from first to "
             "second is much larger than the step from a good credit score to an "
             "average one.</p>"),
            ("How the Positions Compare",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Position</th><th>Recovers</th><th>Pricing</th>"
             "<th>Lender availability</th></tr></thead><tbody>"
             '<tr><td data-label="Position">First</td>'
             '<td data-label="Recovers">Before anyone else</td>'
             '<td data-label="Pricing">Lowest</td>'
             '<td data-label="Availability">Widest &mdash; banks included</td></tr>'
             '<tr><td data-label="Position">Second</td>'
             '<td data-label="Recovers">After the first is satisfied</td>'
             '<td data-label="Pricing">Materially higher</td>'
             '<td data-label="Availability">Good, mostly non-bank</td></tr>'
             '<tr><td data-label="Position">Third</td>'
             '<td data-label="Recovers">After both</td>'
             '<td data-label="Pricing">Higher again</td>'
             '<td data-label="Availability">Narrow, specialist</td></tr>'
             '<tr><td data-label="Position">Fourth or beyond</td>'
             '<td data-label="Recovers">In practice, rarely</td>'
             '<td data-label="Pricing">Rarely offered on price at all</td>'
             '<td data-label="Availability">Effectively none</td></tr>'
             "</tbody></table></div>"
             "<p>If you are being offered a fourth position, the question worth asking "
             "is not the rate. It is why the property is being asked to carry that "
             "much debt.</p>"),
            ("The Combined Loan-to-Value Test",
             "<p>A subordinate lender does not look at their own loan in isolation. "
             "They look at every lien on the property together, against its value.</p>"
             "<p>That total is the combined loan-to-value, and it is the number that "
             "governs the decision. A modest second on a property with a small first "
             "is a comfortable loan; the same second behind a large first is not, and "
             "the second lender is the one exposed to the difference.</p>"
             "<p>Work it out before applying: add every balance, divide by a realistic "
             "value, and be honest about the value. Lenders use an appraisal, not a "
             "listing price or what a neighbour got.</p>"),
            ("What to Check in the First Mortgage",
             "<p>The senior loan agreement can decide this before a lender does.</p>"
             "<ul>"
             "<li><strong>Does it prohibit additional liens?</strong> Some do "
             "outright, and taking one anyway can be a default on the loan you already "
             "have &mdash; even while you keep paying it.</li>"
             "<li><strong>Does it require consent?</strong> Common on commercial "
             "first mortgages, and the consent takes time.</li>"
             "<li><strong>Is there a due-on-sale or due-on-encumbrance clause?</strong> "
             "The second is broader than the first and catches more.</li>"
             "<li><strong>Is there a prepayment penalty</strong> if you would rather "
             "refinance the whole thing into one loan instead?</li>"
             "</ul>"
             "<p>These are questions with written answers in a document you already "
             "hold. Reading it is the cheapest step in the process.</p>"),
            ("When a Second Beats Refinancing",
             "<p>The alternative to borrowing behind a first mortgage is replacing it "
             "&mdash; one larger loan in first position, at first-position pricing.</p>"
             "<p>A second wins when the existing first is cheap. A low rate fixed some "
             "years ago is an asset, and giving it up to access equity can cost far "
             "more over the remaining term than the higher rate on a smaller second.</p>"
             "<p>A refinance wins when the existing first is expensive, near maturity, "
             "or when you want one payment rather than two. Run both as total cost "
             "over how long you expect to hold the property, not as a rate "
             "comparison. See "
             '<a href="../real-estate-secured-vs-unsecured-business-loan/">secured '
             "versus unsecured</a> for the prior question of whether to pledge the "
             "property at all.</p>"),
        ],
        "faqs": [
            ("What does second position mean on a business loan?",
             "The lender sits behind an existing first mortgage in the repayment "
             "queue. If the property is sold or foreclosed, the first lienholder is "
             "paid in full before the second receives anything, which is why "
             "subordinate debt is priced higher."),
            ("Can you get a third position business loan?",
             "Sometimes, from specialist lenders, at materially higher cost. Beyond "
             "third position very few lenders will participate at all, because the "
             "realistic recovery in a downturn approaches zero."),
            ("What is combined loan-to-value?",
             "Every lien on the property added together, divided by the property's "
             "appraised value. A subordinate lender underwrites to that combined "
             "figure rather than to their own loan alone, because it is what "
             "determines whether anything is left for them."),
            ("Does my first mortgage lender have to approve a second?",
             "Sometimes. Some agreements prohibit additional liens outright, others "
             "require written consent, and some are silent. Taking a second where it "
             "is prohibited can be a default on the loan you already have, so check "
             "the document first."),
            ("Is a second better than refinancing the first?",
             "It depends on the rate on your existing first. A cheap first mortgage is "
             "worth keeping, and a smaller second at a higher rate can cost less "
             "overall than replacing it. Compare total cost over your expected hold, "
             "not headline rates."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("../cross-collateralization-what-youre-signing/",
             "Cross-collateralisation: what you are signing"),
            ("../what-equity-lenders-require-behind-a-first-mortgage/",
             "What equity lenders require behind a first mortgage"),
            ("/commercial-real-estate-loans.html", "Commercial real estate loans"),
        ],
        "sources": [SLOOS, CFPB_MTG, FTC],
    },
    {
        "slug": "cross-collateralization-what-youre-signing",
        "crumb": "Cross-Collateralisation",
        "title": "Cross-Collateralization: What You Are Signing | Axiant",
        "og_title": "Cross-Collateralization: What You Are Actually Signing",
        "h1": "Cross-Collateralization: What You Are Signing",
        "headline": "Cross-Collateralization: What You Are Signing",
        "lede": "One clause that ties assets together - what it buys you, and "
                "what it costs when you want to sell one",
        "meta_desc": "Cross-collateralisation ties several assets to one debt. What "
                     "it buys in pricing, what a release clause has to say, and why "
                     "selling a single asset can become impossible without one.",
        "article_desc": "What cross-collateralisation commits you to and how release "
                        "clauses govern it.",
        "keywords": "cross collateralization, blanket lien business, dragnet clause, "
                    "release clause business loan",
        "quick_answer": "Cross-collateralisation makes <strong>every pledged asset "
                        "secure the whole debt</strong>, not just its own share. It "
                        "buys better pricing and lets a strong asset carry a weak one. "
                        "The cost is flexibility: selling or refinancing a single "
                        "asset needs a <strong>release clause</strong>, and without a "
                        "workable one you can be unable to sell anything without "
                        "repaying everything.",
        "sections": [
            ("What the Clause Does",
             "<p>Normally a loan is secured by one thing, and that thing answers for "
             "that loan. Cross-collateralisation removes the pairing: each pledged "
             "asset secures the entire obligation.</p>"
             "<p>It is what makes blended underwriting possible. A lender looking at "
             "three properties together can lend against the total in a way they would "
             "not against each separately, and a property that would not qualify alone "
             "can be carried by the others.</p>"
             "<p>That is a real benefit and it is why the structure exists. The "
             "question is whether you understand what you have given up to get it.</p>"),
            ("The Trade, Set Out",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Cross-collateralised</th><th>Separately secured</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Pricing</strong></td>'
             '<td data-label="Cross">Better &mdash; more security behind the debt</td>'
             '<td data-label="Separate">Each priced on its own merits</td></tr>'
             '<tr><td data-label=""><strong>A weak asset</strong></td>'
             '<td data-label="Cross">Carried by the others</td>'
             '<td data-label="Separate">Fails on its own</td></tr>'
             '<tr><td data-label=""><strong>Selling one</strong></td>'
             '<td data-label="Cross">Needs a release; may require a large paydown</td>'
             '<td data-label="Separate">Repay that loan and it is done</td></tr>'
             '<tr><td data-label=""><strong>Refinancing one</strong></td>'
             '<td data-label="Cross">Usually not possible in isolation</td>'
             '<td data-label="Separate">Straightforward</td></tr>'
             '<tr><td data-label=""><strong>If one fails</strong></td>'
             '<td data-label="Cross">The lender can reach all of them</td>'
             '<td data-label="Separate">Contained to that asset</td></tr>'
             "</tbody></table></div>"),
            ("The Release Clause Is the Whole Negotiation",
             "<p>If you read one clause before signing, read this one.</p>"
             "<p>A release clause governs what happens when you want a single asset "
             "out. Without a workable one, selling one property can require repaying "
             "the entire facility &mdash; which is not a theoretical risk, it is the "
             "thing that traps owners who assumed they could sell an asset when they "
             "needed to.</p>"
             "<p>What to establish in writing:</p>"
             "<ul>"
             "<li><strong>Can a single asset be released</strong>, and on what "
             "conditions</li>"
             "<li><strong>How much must be repaid</strong> to release it &mdash; "
             "commonly more than that asset's share of the balance</li>"
             "<li><strong>What the remaining collateral must still satisfy</strong> "
             "on loan-to-value and coverage after the release</li>"
             "<li><strong>Whether a release fee or prepayment charge applies</strong> "
             "to the amount repaid</li>"
             "</ul>"),
            ("Dragnet Clauses Go Further Still",
             "<p>A related clause worth knowing by name. A dragnet, or "
             "cross-default, clause makes the collateral secure not just this debt but "
             "<em>other</em> obligations you owe the same lender &mdash; sometimes "
             "including future ones.</p>"
             "<p>The practical effect is that a default on an unrelated facility with "
             "the same lender can reach property pledged here. It is common in bank "
             "relationships and often unremarked at signing, because it sits in the "
             "security agreement rather than the term sheet.</p>"
             "<p>Ask directly whether the security is limited to this loan. It is a "
             "one-sentence question with a consequential answer.</p>"),
            ("When to Accept It",
             "<p>Cross-collateralisation is not a trap in itself. It is a structure "
             "with a specific shape, and it fits some situations well.</p>"
             "<p><strong>Accept it</strong> when you hold assets you intend to keep, "
             "the pricing benefit is real, and the release terms are workable. A "
             "portfolio you are not planning to break up loses little.</p>"
             "<p><strong>Push back</strong> when you may sell an individual asset, "
             "when the assets differ enough that blended terms suit none of them, or "
             "when the release clause is vague. Vagueness in a release clause is not "
             "an oversight &mdash; it is the lender keeping the option.</p>"
             "<p><strong>This is general information, not legal advice.</strong> "
             "Security agreements are where these clauses live and they repay reading "
             "with an attorney rather than alone.</p>"),
        ],
        "faqs": [
            ("What does cross-collateralised mean?",
             "Every pledged asset secures the whole debt rather than just its own "
             "share. It is what allows a lender to blend several assets into one "
             "facility, and it means a problem with one is not contained to that one."),
            ("What is a release clause?",
             "The term that governs taking a single asset out of a cross-collateralised "
             "facility &mdash; whether it can be done, what must be repaid to do it, "
             "and what the remaining collateral must still satisfy afterwards. Without "
             "a workable one, selling one asset can require repaying everything."),
            ("What is a dragnet clause?",
             "A clause making the collateral secure other obligations you owe the same "
             "lender, sometimes including future ones. It means a default on an "
             "unrelated facility can reach property pledged here. It usually sits in "
             "the security agreement rather than the term sheet."),
            ("Does cross-collateralisation get me a better rate?",
             "Generally yes, because there is more security behind the debt and a weak "
             "asset can be carried by stronger ones. The cost is paid in flexibility "
             "rather than in interest, which is why it looks free at signing."),
            ("Should I ever refuse it?",
             "Push back when you may want to sell an individual asset, when the assets "
             "are dissimilar enough that blended terms suit none of them, or when the "
             "release clause is vague. Vagueness there is the lender keeping an "
             "option, not an oversight."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("../second-and-third-position-business-loans/",
             "Second and third position business loans"),
            ("/dscr-loans/articles/dscr-portfolio-loans-multiple-properties/",
             "DSCR portfolio loans for multiple properties"),
            ("../real-estate-secured-vs-unsecured-business-loan/",
             "Secured vs unsecured business loans"),
        ],
        "sources": [FTC, CFPB, SLOOS],
    },
    {
        "slug": "business-loan-against-rental-property",
        "crumb": "Against a Rental Property",
        "title": "Business Loan Against a Rental Property | Axiant Partners",
        "og_title": "Business Loan Against a Rental Property",
        "h1": "Business Loan Against a Rental Property",
        "headline": "Business Loan Against a Rental Property",
        "lede": "Using an investment property as collateral for the business - "
                "what changes when the collateral has tenants",
        "meta_desc": "Borrowing for the business against a rental property you own. "
                     "How lenders treat tenanted collateral, what the rent has to "
                     "cover, and the risk of mixing two balance sheets.",
        "article_desc": "How business borrowing secured against a rental property is "
                        "underwritten and what it risks.",
        "keywords": "business loan against rental property, investment property "
                    "collateral, rental equity business loan, cross collateral rental",
        "quick_answer": "You can generally pledge a rental you own, and lenders like "
                        "it because the collateral produces income. Two things change: "
                        "the property must still <strong>cover its own mortgage</strong> "
                        "after the new lien, and you are "
                        "<strong>connecting the property to the business</strong> "
                        "&mdash; if the business fails, the rental is now exposed to "
                        "it.",
        "sections": [
            ("Why Lenders Like Tenanted Collateral",
             "<p>A rental is unusually good security. It has a market value like any "
             "property, and unlike a warehouse or an owner-occupied building it "
             "produces cash on its own.</p>"
             "<p>That means a lender is not relying solely on a sale to recover. The "
             "property services debt while it is held, which lowers the risk and "
             "usually shows up in the pricing relative to unsecured business "
             "credit.</p>"
             "<p>It is also why the rent gets underwritten rather than assumed. The "
             "question is not just what the property is worth &mdash; it is whether "
             "the income still covers everything secured against it once your new loan "
             "is added.</p>"),
            ("What the Rent Has to Cover",
             "<p>Adding a lien adds a payment, and the property has to carry the total.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>What is tested</th><th>Why</th></tr></thead><tbody>"
             '<tr><td data-label="Tested">Net operating income against total debt service</td>'
             '<td data-label="Why">The coverage test, now including your new loan</td></tr>'
             '<tr><td data-label="Tested">Combined loan-to-value across all liens</td>'
             '<td data-label="Why">Whether equity remains behind the new position</td></tr>'
             '<tr><td data-label="Tested">Lease and payment history</td>'
             '<td data-label="Why">Whether the income is contractual and actually '
             "arriving</td></tr>"
             '<tr><td data-label="Tested">Vacancy and expenses</td>'
             '<td data-label="Why">Gross rent is not income &mdash; taxes, insurance, '
             "management and vacancy come off first</td></tr>"
             "</tbody></table></div>"
             "<p>The arithmetic is the same one covered in "
             '<a href="/dscr-loans/articles/how-dscr-is-calculated/">how DSCR is '
             "calculated</a>, applied here with your business loan added to the "
             "denominator.</p>"),
            ("The Risk Nobody Prices at Signing",
             "<p>This is the part worth sitting with.</p>"
             "<p>Before the loan, the rental and the business are separate. The "
             "property has its own debt, its own income, and its own risk. If the "
             "business fails, the rental carries on.</p>"
             "<p>After the loan, they are connected. A business failure now reaches "
             "the property, and the tenant's rent is servicing debt that a failing "
             "business took on. Owners who built a rental portfolio deliberately "
             "separate from an operating company can undo that separation with one "
             "signature.</p>"
             "<p>That is not an argument against doing it. It is an argument for doing "
             "it consciously, and for asking whether the business need is worth the "
             "connection.</p>"),
            ("What Lenders Ask For",
             "<ul>"
             "<li><strong>The lease</strong>, signed, for each unit</li>"
             "<li><strong>Evidence the rent arrives</strong> &mdash; usually bank "
             "statements showing deposits</li>"
             "<li><strong>The mortgage statement and exact payoff</strong> on existing "
             "liens</li>"
             "<li><strong>Insurance</strong> with the new lender named, in the right "
             "entity's name</li>"
             "<li><strong>Entity documents</strong> if the property is held in an LLC "
             "&mdash; see "
             '<a href="/dscr-loans/articles/llc-vesting-dscr-loans/">holding title in '
             "an LLC</a></li>"
             "<li><strong>The business case</strong>, because this is business "
             "borrowing even though the collateral is property</li>"
             "</ul>"),
            ("When Something Else Fits Better",
             "<p>Pledging a rental is not automatically the cheapest route, and it is "
             "rarely the most reversible.</p>"
             "<p>If the need is short and the business has revenue, unsecured working "
             "capital keeps the property out of it entirely &mdash; more expensive per "
             "dollar, but the failure mode is smaller. If the need is a property "
             "purchase rather than operating capital, a "
             '<a href="/dscr-loans.html">DSCR loan</a> on the new property may be the '
             "better instrument. If it is equipment, the equipment can secure "
             "itself.</p>"
             "<p>Reach for property equity when the cost difference genuinely matters "
             "and the need is defined &mdash; not because it is the largest number "
             "available.</p>"),
        ],
        "faqs": [
            ("Can I use a rental property as collateral for a business loan?",
             "Generally yes, and lenders often prefer it to unsecured lending because "
             "the collateral produces income. The property has to keep covering "
             "everything secured against it once your new loan is added."),
            ("Does the rent have to cover the new loan too?",
             "Yes. Lenders test net operating income &mdash; rent after vacancy, "
             "management, taxes and insurance &mdash; against total debt service "
             "including the new lien, alongside the combined loan-to-value across all "
             "liens on the property."),
            ("What happens to the rental if the business fails?",
             "It is exposed, which it was not before. Pledging the property connects "
             "two balance sheets that were separate, so a business failure can now "
             "reach an asset that would otherwise have carried on independently."),
            ("Is this cheaper than an unsecured business loan?",
             "Usually on rate, because the lender has real security. Whether it is "
             "cheaper in the round depends on what you are risking &mdash; unsecured "
             "borrowing costs more per dollar but keeps the property out of the "
             "question entirely."),
            ("Can I do this if the property is in an LLC?",
             "Normally yes. The lender will want the entity documents, evidence of "
             "good standing, authority for whoever signs, and insurance in the "
             "entity's name. Expect a personal guarantee regardless of the entity."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("/dscr-loans/articles/how-dscr-is-calculated/", "How DSCR is calculated"),
            ("../second-and-third-position-business-loans/",
             "Second and third position business loans"),
            ("../real-estate-secured-vs-unsecured-business-loan/",
             "Secured vs unsecured business loans"),
        ],
        "sources": [IRS_527, SLOOS, HUD_MF],
    },
]

# Articles 4-6 live in a companion module to keep each file readable.
from cluster_res_business_loan_b import MORE as _B
ARTICLES = ARTICLES + _B
