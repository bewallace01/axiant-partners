# -*- coding: utf-8 -*-
"""Batch 2 of the DSCR cluster - articles 4-8 of 14.

Same rules as batch 1: ranges described as conventional across DSCR lenders,
never quoted as any lender's terms. No funded totals, no years in business, no
testimonials, no named lender rates. One entity: Axiant Partners,
(561) 268-0465, Boca Raton.
"""
from dscr_articles_batch1 import SLOOS, CFPB, IRS_527, HUD_MF, CENSUS_HV, SBA_NOTE

FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Federal Trade Commission guidance on fee disclosure and the warning "
       "signs of predatory business credit.")
FINCEN_BOI = ("https://www.fincen.gov/boi",
              "FinCEN Beneficial Ownership Information",
              "The federal reporting regime for LLCs and other reporting "
              "companies - the filing obligation that comes with holding title "
              "in an entity.")

ARTICLES = [
    # ------------------------------------------------------------------ 4 --
    {
        "slug": "minimum-dscr-ratio-by-lender-type",
        "crumb": "Minimum DSCR by Lender Type",
        "title": "Minimum DSCR Ratio by Lender Type: Who Wants What | Axiant",
        "og_title": "Minimum DSCR Ratio by Lender Type: Who Wants What",
        "h1": "Minimum DSCR Ratio by Lender Type",
        "headline": "Minimum DSCR Ratio by Lender Type",
        "lede": "Why the same property clears one lender's floor and fails "
                "another's, and what the different minimums are actually pricing",
        "meta_desc": "Minimum DSCR varies by lender type: agency and bank programs sit "
                     "highest, portfolio and non-QM lenders lower, and some price below 1.00. "
                     "What each floor means and what it costs you.",
        "article_desc": "How minimum DSCR requirements differ across agency, bank, "
                        "portfolio and non-QM lenders, and what the differences price.",
        "keywords": "minimum dscr ratio, dscr requirement by lender, dscr 1.0 lender, "
                    "no ratio dscr loan, portfolio dscr lender, agency dscr minimum",
        "quick_answer": "There is no single minimum. <strong>1.20 to 1.25</strong> is the "
                        "common floor at banks and agency-style programs, "
                        "<strong>1.00 to 1.10</strong> at most portfolio and non-QM DSCR "
                        "lenders, and a smaller group will go <strong>below 1.00</strong> or "
                        "drop the ratio test entirely in exchange for a larger down payment, "
                        "a higher rate, or both. The floor is a price, not a rule.",
        "sections": [
            ("Why the Minimum Moves",
             "<p>A DSCR floor is not a regulatory threshold. It is the point at which a "
             "particular lender stops being comfortable, and comfort depends on who "
             "ultimately holds the loan.</p>"
             "<p>A lender selling into a securitisation has to meet the expectations of "
             "the buyers on the other end, and those expectations are conservative and "
             "written down in advance. A lender keeping the loan on its own balance sheet "
             "can decide for itself. That difference &mdash; not the property &mdash; "
             "explains most of the variation you will see quoted.</p>"
             "<p>It follows that shopping a marginal file is worth real money. The same "
             "1.05 property is a decline at one desk and a straightforward approval at "
             "another.</p>"),
            ("The Range by Lender Type",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Lender type</th><th>Typical DSCR floor</th>"
             "<th>What you trade</th></tr></thead><tbody>"
             "<tr><td data-label=\"Type\">Bank / credit union</td>"
             "<td data-label=\"Floor\">1.20&ndash;1.25</td>"
             "<td data-label=\"Trade\">Lowest rates, but usually full personal "
             "underwriting alongside the ratio</td></tr>"
             "<tr><td data-label=\"Type\">Agency-style investor programs</td>"
             "<td data-label=\"Floor\">1.15&ndash;1.25</td>"
             "<td data-label=\"Trade\">Standardised terms; least flexibility on "
             "exceptions</td></tr>"
             "<tr><td data-label=\"Type\">Portfolio / non-QM DSCR lender</td>"
             "<td data-label=\"Floor\">1.00&ndash;1.10</td>"
             "<td data-label=\"Trade\">The mainstream DSCR product; rate above bank "
             "pricing</td></tr>"
             "<tr><td data-label=\"Type\">Sub-1.00 programs</td>"
             "<td data-label=\"Floor\">0.75&ndash;1.00</td>"
             "<td data-label=\"Trade\">Larger down payment, higher rate, reserves</td></tr>"
             "<tr><td data-label=\"Type\">No-ratio programs</td>"
             "<td data-label=\"Floor\">None tested</td>"
             "<td data-label=\"Trade\">Lowest leverage and highest price; leans on "
             "equity and credit instead</td></tr>"
             "</tbody></table></div>"
             "<p>Treat these as the shape of the market rather than a rate sheet. Floors "
             "move with credit conditions, and the "
             "<a href=\"https://www.federalreserve.gov/data/sloos.htm\" rel=\"noopener "
             "nofollow\" target=\"_blank\">Federal Reserve's quarterly survey of lending "
             "standards</a> is the public record of which way they are moving.</p>"),
            ("What a Floor Is Actually Pricing",
             "<p>A minimum DSCR is a lender's estimate of how much can go wrong before "
             "the property stops paying its own debt. At 1.25 the property can lose a "
             "fifth of its net income and still cover the mortgage. At 1.00 it cannot lose "
             "anything.</p>"
             "<p>That is why the floor and the rate move together. A lender accepting 1.00 "
             "is accepting a thinner cushion and charging for it. A lender accepting 0.85 "
             "knows the property does not cover its debt today and is lending against your "
             "equity and your willingness to fund the gap.</p>"
             "<p>Which means the honest question is not \"what is the lowest ratio I can "
             "get approved at\" but \"what happens to me at that ratio if the roof goes or "
             "the tenant leaves\".</p>"),
            ("Compensating Factors That Move the Floor",
             "<p>Most lenders publish a floor and then flex it. What typically buys "
             "flexibility:</p>"
             "<ul>"
             "<li><strong>A larger down payment.</strong> The most reliable lever there is "
             "&mdash; lower leverage lowers the lender's loss if the property "
             "underperforms.</li>"
             "<li><strong>Reserves.</strong> Several months of payments held after "
             "closing, evidencing you can cover a shortfall.</li>"
             "<li><strong>Credit depth.</strong> A stronger score usually opens a lower "
             "ratio at the same lender.</li>"
             "<li><strong>Track record.</strong> Documented experience operating rentals "
             "carries weight on many programs.</li>"
             "<li><strong>Property type.</strong> A long-let single-family house is "
             "treated more kindly than a seasonal or short-term property.</li>"
             "</ul>"
             "<p>These are the same levers that lift the ratio itself &mdash; see "
             "<a href=\"../how-dscr-is-calculated/\">how DSCR is calculated</a> &mdash; "
             "which is why a marginal file often has two routes to approval rather than "
             "one.</p>"),
            ("How to Shop a Marginal File",
             "<p>If your ratio lands between 1.00 and 1.20, you are in the band where "
             "lender choice matters more than anything else you can do. A practical "
             "order:</p>"
             "<ul>"
             "<li><strong>Fix the inputs first.</strong> A stale insurance quote or the "
             "seller's old tax figure can be the entire gap.</li>"
             "<li><strong>Ask each lender which convention they use</strong> &mdash; "
             "principal and interest, PITI, or PITIA. The same property presents "
             "differently under each.</li>"
             "<li><strong>Ask what the floor is <em>with</em> compensating factors</strong>, "
             "not just the headline number.</li>"
             "<li><strong>Compare total cost, not the floor.</strong> A lender who accepts "
             "1.00 at a materially higher rate may be the worse deal than one who wants "
             "1.15 and a larger deposit.</li>"
             "</ul>"
             "<p><a href=\"/dscr-lenders.html\">How to compare DSCR lenders</a> goes "
             "through the criteria that matter more than the rate.</p>"),
        ],
        "faqs": [
            ("What is the minimum DSCR most lenders require?",
             "<strong>1.00 to 1.10</strong> at most portfolio and non-QM DSCR lenders, "
             "which is where the bulk of this lending happens. Banks and agency-style "
             "programs typically sit higher at <strong>1.20 to 1.25</strong>. There is no "
             "universal minimum &mdash; it is set by whoever ends up holding the loan."),
            ("Can I get a DSCR loan with a ratio below 1.0?",
             "Yes, from a smaller group of lenders. Sub-1.00 programs generally require a "
             "larger down payment, carry a higher rate, and often ask for reserves. Be "
             "clear about what it means in practice: below 1.00 the property does not "
             "cover its own debt and you fund the difference every month."),
            ("What is a no-ratio DSCR loan?",
             "A program that does not test the coverage ratio at all, leaning on equity "
             "and credit instead. It carries the lowest leverage and the highest pricing "
             "of the DSCR family, and is generally a tool for properties whose income is "
             "hard to evidence rather than a way to avoid the arithmetic."),
            ("Why did two lenders give me different DSCR figures for the same property?",
             "Almost always because they use different denominators. Some count principal "
             "and interest only, most single-family programs use PITI, and condos usually "
             "add HOA dues to make PITIA. Ask which convention each is using before "
             "concluding one of them is wrong."),
            ("Does a higher DSCR get me a better rate?",
             "Usually, yes. Coverage is one of the inputs to pricing alongside leverage "
             "and credit, and clearing a lender's next threshold up can move you into "
             "better pricing. It is worth asking where the breakpoints sit before "
             "deciding on a down payment."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
            ("/dscr-lenders.html", "How to compare DSCR lenders"),
            ("../why-dscr-loans-get-denied/", "Why DSCR loans get denied"),
        ],
        "sources": [SLOOS, CFPB, HUD_MF],
    },

    # ------------------------------------------------------------------ 5 --
    {
        "slug": "dscr-prepayment-penalties-step-downs",
        "crumb": "Prepayment Penalties & Step-Downs",
        "title": "DSCR Prepayment Penalties: Step-Downs Explained | Axiant",
        "og_title": "DSCR Prepayment Penalties and Step-Downs Explained",
        "h1": "DSCR Prepayment Penalties and Step-Downs",
        "headline": "DSCR Prepayment Penalties and Step-Downs",
        "lede": "What a 5-4-3-2-1 actually costs, when a penalty is worth "
                "accepting for a lower rate, and the exits that trigger it",
        "meta_desc": "DSCR prepayment penalties explained: how 5-4-3-2-1 and 3-2-1 "
                     "step-downs work, what a flat penalty costs, when buying one out makes "
                     "sense, and which exits trigger a charge.",
        "article_desc": "How prepayment penalties are structured on DSCR loans and how "
                        "to decide whether to accept, buy down or avoid one.",
        "keywords": "dscr prepayment penalty, step down prepayment, 5-4-3-2-1 prepay, "
                    "dscr prepay buyout, yield maintenance rental loan",
        "quick_answer": "Most DSCR loans carry a prepayment penalty for the first three "
                        "to five years, commonly as a <strong>step-down</strong> such as "
                        "5-4-3-2-1 &mdash; 5% of the balance repaid in year one, 4% in year "
                        "two, and so on. Selling or refinancing inside that window triggers "
                        "it. You can usually buy the penalty down or out by accepting a "
                        "higher rate, which is worth doing only if you expect to exit early.",
        "sections": [
            ("How a Step-Down Works",
             "<p>A step-down prepayment penalty charges a percentage of the balance you "
             "repay, falling each year until it disappears. The two structures you will "
             "see most often:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Year</th><th>5-4-3-2-1</th><th>3-2-1</th>"
             "<th>On a $225,000 balance (5-4-3-2-1)</th></tr></thead><tbody>"
             "<tr><td data-label=\"Year\">1</td><td data-label=\"5-4-3-2-1\">5%</td>"
             "<td data-label=\"3-2-1\">3%</td><td data-label=\"Cost\">$11,250</td></tr>"
             "<tr><td data-label=\"Year\">2</td><td data-label=\"5-4-3-2-1\">4%</td>"
             "<td data-label=\"3-2-1\">2%</td><td data-label=\"Cost\">$9,000</td></tr>"
             "<tr><td data-label=\"Year\">3</td><td data-label=\"5-4-3-2-1\">3%</td>"
             "<td data-label=\"3-2-1\">1%</td><td data-label=\"Cost\">$6,750</td></tr>"
             "<tr><td data-label=\"Year\">4</td><td data-label=\"5-4-3-2-1\">2%</td>"
             "<td data-label=\"3-2-1\">&mdash;</td><td data-label=\"Cost\">$4,500</td></tr>"
             "<tr><td data-label=\"Year\">5</td><td data-label=\"5-4-3-2-1\">1%</td>"
             "<td data-label=\"3-2-1\">&mdash;</td><td data-label=\"Cost\">$2,250</td></tr>"
             "<tr><td data-label=\"Year\">6+</td><td data-label=\"5-4-3-2-1\">None</td>"
             "<td data-label=\"3-2-1\">None</td><td data-label=\"Cost\">&mdash;</td></tr>"
             "</tbody></table></div>"
             "<p>The arithmetic is worth internalising. Selling in month 13 of a "
             "5-4-3-2-1 on a $225,000 balance costs $9,000 &mdash; frequently more than "
             "the rate saving that bought the penalty in the first place.</p>"),
            ("The Other Structures",
             "<p>Step-downs are the most common but not the only shape:</p>"
             "<ul>"
             "<li><strong>Flat penalty.</strong> A single percentage for the whole "
             "period, such as 3% for three years. Simpler, and worse than a step-down if "
             "you exit late in the window.</li>"
             "<li><strong>Declining by month rather than year.</strong> Kinder to a "
             "borrower who exits mid-year.</li>"
             "<li><strong>Yield maintenance.</strong> You make the lender whole on the "
             "interest they expected to earn. Far more expensive than a step-down when "
             "rates have fallen, and the cost is not knowable in advance.</li>"
             "<li><strong>Interest guarantee.</strong> A minimum number of months of "
             "interest regardless of when you repay.</li>"
             "</ul>"
             "<p>If a term sheet says yield maintenance rather than a percentage, ask for "
             "a worked figure at a couple of exit dates before signing. It is the one "
             "structure where borrowers routinely misjudge the cost by an order of "
             "magnitude.</p>"),
            ("What Triggers a Penalty",
             "<p>Anything that repays the loan early, which is a wider set than most "
             "people expect:</p>"
             "<ul>"
             "<li><strong>Selling the property</strong> &mdash; the most common trigger</li>"
             "<li><strong>Refinancing</strong>, including with the same lender in many cases</li>"
             "<li><strong>A cash-out refinance</strong> that replaces the loan</li>"
             "<li><strong>Paying the balance off</strong> from other funds</li>"
             "</ul>"
             "<p>What usually does not trigger it: ordinary monthly payments, and "
             "additional principal payments up to whatever the note permits &mdash; often "
             "a percentage of the balance per year without charge. That allowance is worth "
             "reading, because it determines whether you can pay a loan down aggressively "
             "without paying for the privilege.</p>"
             "<p>Some notes carve out an exemption for a sale to an unrelated third party. "
             "Some do not. It is a question worth asking rather than assuming.</p>"),
            ("Buying the Penalty Down",
             "<p>Most DSCR lenders will shorten or remove a prepayment penalty in exchange "
             "for a higher rate. The trade is straightforward to evaluate:</p>"
             "<ul>"
             "<li><strong>Work out your realistic exit.</strong> Not your intended exit "
             "&mdash; your realistic one, including the possibility of selling sooner than "
             "planned.</li>"
             "<li><strong>Price the penalty at that date.</strong> A percentage of the "
             "balance, from the schedule in the note.</li>"
             "<li><strong>Price the rate difference over the same period.</strong> The "
             "extra interest you would pay to remove it.</li>"
             "<li><strong>Compare the two numbers.</strong></li>"
             "</ul>"
             "<p>Buy-outs tend to be worth it when you genuinely expect to exit in the "
             "first two years &mdash; a flip taking longer than planned, or a property you "
             "intend to refinance once stabilised. They tend not to be worth it on a "
             "long-term hold, where you are paying a permanently higher rate to insure "
             "against an event you do not expect.</p>"),
            ("Where Investors Get Caught",
             "<p>Three patterns account for most of the unpleasant surprises:</p>"
             "<ul>"
             "<li><strong>The BRRRR refinance.</strong> Buying, renovating and refinancing "
             "inside twelve months runs straight into year one of the penalty. If that is "
             "the plan, the penalty structure matters more than the rate. See "
             "<a href=\"../dscr-exit-from-a-flip/\">DSCR as an exit from a flip</a>.</li>"
             "<li><strong>The unplanned sale.</strong> Life changes, a market turns, a "
             "partnership ends. The penalty does not care why.</li>"
             "<li><strong>Rate-drop refinancing.</strong> Borrowers who took a high rate "
             "expecting to refinance when rates fell, without checking whether the note "
             "let them.</li>"
             "</ul>"
             "<p>Read the prepayment clause before the rate. It is the term most likely to "
             "cost you real money and the one most often skimmed.</p>"),
        ],
        "faqs": [
            ("What does 5-4-3-2-1 mean on a DSCR loan?",
             "A step-down prepayment penalty. You pay <strong>5%</strong> of the balance "
             "repaid if you pay off in year one, 4% in year two, 3% in year three, 2% in "
             "year four, 1% in year five, and nothing from year six. On a $225,000 balance "
             "that is $11,250 in year one falling to $2,250 in year five."),
            ("Do all DSCR loans have a prepayment penalty?",
             "Most do, typically for three to five years, but not all. Lenders will "
             "generally shorten or remove one in exchange for a higher rate, so a "
             "no-penalty DSCR loan usually exists at a price rather than not existing."),
            ("Does selling the property trigger the prepayment penalty?",
             "Usually yes &mdash; a sale repays the loan, which is exactly what the "
             "penalty is written for. Some notes carve out an exemption for a sale to an "
             "unrelated third party, so read the clause rather than assuming either way."),
            ("Can I make extra principal payments without a penalty?",
             "Often, up to a limit. Many notes permit additional principal of a set "
             "percentage of the balance each year without charge, with the penalty "
             "applying only above that. The allowance is written into the note and is "
             "worth checking if you plan to pay down aggressively."),
            ("Is it worth paying a higher rate to remove the penalty?",
             "Only if you realistically expect to exit early. Price the penalty at your "
             "likely exit date, price the rate difference over the same period, and "
             "compare. On a long-term hold you are usually paying a permanently higher "
             "rate to insure against something you do not expect to happen."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/dscr-loan-rates.html", "DSCR loan rates: how pricing is built"),
            ("../dscr-exit-from-a-flip/", "Using a DSCR loan to exit a flip"),
            ("../dscr-loan-closing-costs-and-fees/", "DSCR loan closing costs and fees"),
        ],
        "sources": [CFPB, FTC, SLOOS],
    },

    # ------------------------------------------------------------------ 6 --
    {
        "slug": "dscr-cash-out-refinance-how-much-equity",
        "crumb": "Cash-Out Refinance",
        "title": "DSCR Cash-Out Refinance: How Much Equity Can You Pull | Axiant",
        "og_title": "DSCR Cash-Out Refinance: How Much Equity Can You Pull?",
        "h1": "DSCR Cash-Out Refinance: How Much Equity Can You Pull?",
        "headline": "DSCR Cash-Out Refinance: How Much Equity Can You Pull",
        "lede": "What the loan-to-value cap allows, why the ratio usually binds "
                "first, and what seasoning rules mean for a recent purchase",
        "meta_desc": "DSCR cash-out refinance: how much equity you can pull, why the "
                     "coverage ratio usually caps you before the LTV does, and how seasoning "
                     "rules treat a property you bought recently.",
        "article_desc": "How much equity a DSCR cash-out refinance releases, and which "
                        "constraint binds first.",
        "keywords": "dscr cash out refinance, cash out rental property, dscr ltv cash out, "
                    "brrrr refinance, pull equity rental property",
        "quick_answer": "Cash-out on a DSCR loan is usually capped around "
                        "<strong>70&ndash;75% of value</strong>, against roughly 75&ndash;80% "
                        "on a rate-and-term refinance. But the loan-to-value cap is often not "
                        "what stops you: <strong>taking cash out raises the payment, which "
                        "lowers the coverage ratio</strong>, and the ratio floor usually binds "
                        "first. Work backwards from the payment the rent supports.",
        "sections": [
            ("Two Caps, and the One That Usually Binds",
             "<p>Every cash-out refinance runs into two separate limits, and investors "
             "tend to plan around the wrong one.</p>"
             "<p>The first is <strong>loan-to-value</strong>: a percentage of the "
             "appraised value the lender will lend against, commonly 70&ndash;75% when "
             "cash is coming out. The second is <strong>the coverage ratio</strong>: the "
             "rent has to support the new, larger payment.</p>"
             "<p>On a property with strong equity and modest rent, the ratio binds long "
             "before the LTV does. You can be sitting on 50% equity and still be unable to "
             "pull much of it, because every dollar borrowed raises the payment and pushes "
             "the ratio down. That is the single most common surprise in a DSCR cash-out.</p>"
             "<p>The practical move is to work backwards: start from the payment the rent "
             "supports at the lender's floor, and see what loan that implies.</p>"),
            ("How the Two Interact",
             "<p>Take a property appraised at $400,000 renting at $2,900 a month, with net "
             "operating income of roughly $25,000 a year after expenses.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Constraint</th><th>What it allows</th><th>Effect</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"Constraint\">LTV cap at 75%</td>"
             "<td data-label=\"Allows\">$300,000 loan</td>"
             "<td data-label=\"Effect\">The headline number most people plan around</td></tr>"
             "<tr><td data-label=\"Constraint\">Coverage floor at 1.20</td>"
             "<td data-label=\"Allows\">Annual debt service up to about $20,800</td>"
             "<td data-label=\"Effect\">Implies a materially smaller loan</td></tr>"
             "<tr><td data-label=\"Constraint\">Coverage floor at 1.00</td>"
             "<td data-label=\"Allows\">Annual debt service up to about $25,000</td>"
             "<td data-label=\"Effect\">More proceeds, no cushion left</td></tr>"
             "</tbody></table></div>"
             "<p>Whichever constraint produces the smaller loan is the one that governs. "
             "Illustrative arithmetic, not a quote &mdash; but the shape holds: the "
             "coverage test is what turns a strong-equity property into a modest cash-out.</p>"
             "<p><a href=\"../how-dscr-is-calculated/\">How DSCR is calculated</a> covers "
             "the inputs on both sides of that.</p>"),
            ("Seasoning: How Recently You Bought Matters",
             "<p>Seasoning is how long you must have owned a property before a lender will "
             "lend against its current value rather than what you paid.</p>"
             "<p>It matters enormously to anyone renovating. Buy at $250,000, spend "
             "$60,000, and the property may be worth $380,000 &mdash; but a lender applying "
             "a twelve-month seasoning rule will lend against $310,000 of cost, not "
             "$380,000 of value, and the renovation profit stays locked up until the clock "
             "runs out.</p>"
             "<p>Programs vary widely, and a shorter requirement is one of the things "
             "worth shopping for specifically. See "
             "<a href=\"../dscr-loans-no-seasoning/\">DSCR loans with no seasoning</a> for "
             "how the shorter-window programs work and what they cost.</p>"),
            ("What the Proceeds Can Be Used For",
             "<p>One of the genuine advantages here: cash-out proceeds on an investment "
             "property are generally unrestricted. Buying the next property, paying down "
             "other debt, funding a renovation, or holding reserves are all ordinary uses, "
             "and lenders do not usually police it the way they would on an owner-occupied "
             "loan.</p>"
             "<p>Two things do get attention. Lenders will ask about the source of funds "
             "for the original purchase if it was recent, and a cash-out that leaves the "
             "borrower with no reserves is a weaker file than one that does not.</p>"
             "<p>The tax treatment of what you do with the proceeds is a separate question "
             "and depends on how the money is used. That is a conversation for your CPA, "
             "not your lender, and general guidance is in "
             "<a href=\"https://www.irs.gov/publications/p527\" rel=\"noopener nofollow\" "
             "target=\"_blank\">IRS Publication 527</a>.</p>"),
            ("Making a Cash-Out File Work",
             "<p>If the coverage ratio is what is capping you, the levers are the same "
             "ones that lift any DSCR file:</p>"
             "<ul>"
             "<li><strong>Take less cash.</strong> The most direct fix, and often the "
             "right one &mdash; leaving a cushion in the ratio is not a wasted "
             "opportunity.</li>"
             "<li><strong>Extend the amortization</strong> to lower the payment, accepting "
             "more total interest.</li>"
             "<li><strong>Look for an interest-only period</strong>, which some lenders "
             "will underwrite to.</li>"
             "<li><strong>Buy the rate down</strong> with points, lowering the payment.</li>"
             "<li><strong>Get the rent right.</strong> If the appraiser's market rent "
             "opinion is low, comparable evidence is a legitimate challenge.</li>"
             "</ul>"
             "<p>And check the prepayment clause on the loan you are replacing before you "
             "start &mdash; refinancing inside the penalty window can wipe out the benefit "
             "entirely. See "
             "<a href=\"../dscr-prepayment-penalties-step-downs/\">prepayment penalties "
             "and step-downs</a>.</p>"),
        ],
        "faqs": [
            ("How much can you cash out on a DSCR loan?",
             "Commonly up to <strong>70&ndash;75% of the appraised value</strong>, against "
             "roughly 75&ndash;80% on a rate-and-term refinance. In practice the coverage "
             "ratio often caps you below the LTV limit, because taking cash out raises the "
             "payment and lowers the ratio."),
            ("Why can't I pull all my equity out?",
             "Because two limits apply and the tighter one governs. Even with substantial "
             "equity, every dollar borrowed raises the debt service, and once the rent no "
             "longer covers the new payment at the lender's floor, the loan stops growing "
             "regardless of how much equity remains."),
            ("What is seasoning on a DSCR cash-out refinance?",
             "How long you must have owned the property before the lender will lend "
             "against current value rather than your purchase price. It matters most after "
             "a renovation, where the difference between the two is the whole point of the "
             "refinance. Requirements vary by program and are worth shopping for."),
            ("Can I use DSCR cash-out proceeds for anything?",
             "Generally yes on an investment property &mdash; buying another property, "
             "paying down debt, funding renovation or holding reserves are all ordinary "
             "uses. Lenders pay more attention to a cash-out that leaves you with no "
             "reserves, and to the source of funds if the original purchase was recent."),
            ("Does a cash-out refinance trigger my old loan's prepayment penalty?",
             "If the existing loan is still inside its penalty window, yes &mdash; a "
             "refinance repays it, which is what the penalty is written for. Check the "
             "schedule in the existing note before starting, because the charge can exceed "
             "the benefit of refinancing."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
            ("../dscr-loans-no-seasoning/", "DSCR loans with no seasoning"),
            ("../dscr-prepayment-penalties-step-downs/", "Prepayment penalties and step-downs"),
        ],
        "sources": [IRS_527, SLOOS, HUD_MF],
    },

    # ------------------------------------------------------------------ 7 --
    {
        "slug": "llc-vesting-dscr-loans",
        "crumb": "Holding Title in an LLC",
        "title": "LLC Vesting on DSCR Loans: Title, Guarantees, Filings | Axiant",
        "og_title": "LLC Vesting on DSCR Loans: Title, Guarantees and Filings",
        "h1": "Holding Title in an LLC on a DSCR Loan",
        "headline": "LLC Vesting on DSCR Loans",
        "lede": "Why DSCR lenders allow entity title where conventional lenders "
                "do not, and what still follows you personally",
        "meta_desc": "DSCR loans usually allow title in an LLC, unlike conventional "
                     "mortgages. What lenders need from the entity, why a personal guarantee "
                     "usually still applies, and the filings that come with it.",
        "article_desc": "How LLC vesting works on a DSCR loan, what documentation "
                        "lenders require, and what liability remains personal.",
        "keywords": "llc dscr loan, vesting in llc, rental property llc mortgage, "
                    "dscr personal guarantee, llc title investment property",
        "quick_answer": "Most DSCR lenders will close in the name of an "
                        "<strong>LLC</strong>, which is one of the clearest differences from "
                        "a conventional mortgage. The entity holds title and the lender "
                        "underwrites the property &mdash; but expect to sign a "
                        "<strong>personal guarantee</strong> anyway, so the LLC is a "
                        "liability and organisational structure rather than a way to borrow "
                        "without recourse.",
        "sections": [
            ("Why DSCR Lenders Allow It",
             "<p>Conventional residential lending is built around an individual borrower "
             "and their income. An entity does not have a W-2 or a debt-to-income ratio, "
             "so it does not fit the machinery, and most conventional programs will not "
             "close in an LLC's name.</p>"
             "<p>DSCR lending starts from a different place. The property's income is the "
             "qualification, and a property produces the same rent whoever holds title. "
             "Once personal income is out of the underwriting, entity ownership stops "
             "being a problem to solve.</p>"
             "<p>The practical result is that investors can hold each property the way "
             "their attorney and accountant would prefer, rather than the way the "
             "financing forces them to.</p>"),
            ("What Lenders Need From the Entity",
             "<p>The documentation is modest and predictable:</p>"
             "<ul>"
             "<li><strong>Articles of organisation</strong> filed with the state</li>"
             "<li><strong>Operating agreement</strong>, showing ownership and who may "
             "bind the entity</li>"
             "<li><strong>EIN</strong> for the entity</li>"
             "<li><strong>Certificate of good standing</strong>, and a foreign "
             "qualification if the LLC is registered in one state and the property sits "
             "in another</li>"
             "<li><strong>Resolution authorising the loan</strong>, naming the person "
             "signing</li>"
             "</ul>"
             "<p>Two practical notes. A brand-new LLC is generally fine &mdash; lenders "
             "are not looking for entity history the way a business lender would. And an "
             "LLC registered in one state holding property in another usually needs to be "
             "qualified to do business where the property is, which is a filing worth "
             "sorting before closing rather than during it.</p>"),
            ("The Personal Guarantee",
             "<p>This is where expectations most often need correcting. Holding title in "
             "an LLC does not usually mean borrowing without recourse.</p>"
             "<p>Most DSCR lenders require a personal guarantee from the members, so if "
             "the property does not perform and the entity cannot pay, the lender can "
             "pursue you. The LLC still does useful work &mdash; it separates properties "
             "from each other and from your other affairs, and it is the structure your "
             "insurance and estate planning are likely built around &mdash; but it is not "
             "a liability shield against the lender.</p>"
             "<p>Non-recourse DSCR lending exists. It is less common, generally requires "
             "lower leverage, and is priced accordingly. If borrowing without a personal "
             "guarantee is the objective rather than a preference, say so at the first "
             "conversation, because it narrows the lender list considerably.</p>"),
            ("Title, Insurance and the Details That Delay Closings",
             "<p>Entity ownership introduces a handful of details that reliably cause "
             "last-minute problems when they are left late:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Item</th><th>What goes wrong</th><th>Fix</th></tr></thead><tbody>"
             "<tr><td data-label=\"Item\">Insurance named insured</td>"
             "<td data-label=\"Wrong\">Policy is in your name, loan is in the LLC's</td>"
             "<td data-label=\"Fix\">Have the policy issued to the entity from the start</td></tr>"
             "<tr><td data-label=\"Item\">Foreign qualification</td>"
             "<td data-label=\"Wrong\">Out-of-state LLC not registered where the property is</td>"
             "<td data-label=\"Fix\">File before closing; processing takes time</td></tr>"
             "<tr><td data-label=\"Item\">Transferring an owned property in</td>"
             "<td data-label=\"Wrong\">Moving title can trigger a due-on-sale clause on an "
             "existing loan, and may trigger transfer tax</td>"
             "<td data-label=\"Fix\">Take advice before deeding anything</td></tr>"
             "<tr><td data-label=\"Item\">Signing authority</td>"
             "<td data-label=\"Wrong\">Operating agreement does not clearly authorise the signer</td>"
             "<td data-label=\"Fix\">Resolution naming the signer, prepared in advance</td></tr>"
             "</tbody></table></div>"
             "<p>None of these is difficult. All of them take longer than a day, which is "
             "why they are worth handling before the file is in underwriting.</p>"),
            ("The Reporting Obligation",
             "<p>Holding property in an entity brings filing obligations that holding it "
             "personally does not. Beneficial ownership reporting is the significant one: "
             "LLCs and similar entities can be required to report who owns and controls "
             "them, with the current requirements published by "
             "<a href=\"https://www.fincen.gov/boi\" rel=\"noopener nofollow\" "
             "target=\"_blank\">FinCEN</a>.</p>"
             "<p>The rules in this area have moved more than once, so treat any summary "
             "&mdash; including this one &mdash; as a pointer rather than the current "
             "position, and confirm what applies to your entity today.</p>"
             "<p>The same caution applies to tax. How an LLC is treated, and whether "
             "holding property in one changes anything for you, depends on the entity's "
             "election and your circumstances. <strong>This is general information, not "
             "tax or legal advice &mdash; confirm the position with your CPA and "
             "attorney.</strong></p>"),
        ],
        "faqs": [
            ("Can I get a DSCR loan in an LLC?",
             "Usually yes. Most DSCR lenders will close in an entity's name, which is one "
             "of the clearest differences from conventional residential lending, where "
             "most programs will not. The entity holds title and the property's income "
             "carries the underwriting."),
            ("Do I still sign a personal guarantee if the LLC holds title?",
             "Usually. Most DSCR lenders require a guarantee from the members, so the LLC "
             "is an organisational and liability structure rather than a way to borrow "
             "without recourse. Non-recourse programs exist but are less common, carry "
             "lower leverage, and are priced for it."),
            ("Does the LLC need a history or credit of its own?",
             "Generally no. A newly formed LLC is normally acceptable, because the lender "
             "is underwriting the property rather than the entity. What is needed is the "
             "paperwork: articles, operating agreement, EIN, good standing, and a "
             "resolution authorising the loan."),
            ("Can I move a property I already own into an LLC?",
             "It is possible but not automatic. Transferring title can trigger a "
             "due-on-sale clause on an existing loan and may have transfer tax "
             "consequences depending on the state. Take legal advice before deeding "
             "anything rather than after."),
            ("Does my LLC need to be registered in the property's state?",
             "Usually it needs to be qualified to do business there, even if it was formed "
             "elsewhere. The filing is routine but takes time, so it is worth completing "
             "before the file reaches underwriting rather than discovering it at closing."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/dscr-loan-requirements.html", "DSCR loan requirements"),
            ("../dscr-portfolio-loans-multiple-properties/", "DSCR portfolio loans for multiple properties"),
            ("../dscr-loans-first-time-investors/", "DSCR loans for first-time investors"),
        ],
        "sources": [FINCEN_BOI, IRS_527, FTC],
    },

    # ------------------------------------------------------------------ 8 --
    {
        "slug": "dscr-loans-no-seasoning",
        "crumb": "No-Seasoning DSCR Loans",
        "title": "DSCR Loans With No Seasoning: Refinance at Current Value | Axiant",
        "og_title": "DSCR Loans With No Seasoning: Refinancing at Current Value",
        "h1": "DSCR Loans With No Seasoning",
        "headline": "DSCR Loans With No Seasoning",
        "lede": "How ownership seasoning decides whether a refinance uses your "
                "purchase price or the property's value today",
        "meta_desc": "No-seasoning DSCR loans let you refinance at current appraised "
                     "value rather than purchase price. How seasoning rules work, why they "
                     "matter after a renovation, and what the shorter windows cost.",
        "article_desc": "How ownership seasoning affects a DSCR refinance and when a "
                        "no-seasoning program is worth its price.",
        "keywords": "no seasoning dscr loan, dscr seasoning requirement, brrrr refinance "
                    "seasoning, delayed financing, refinance at appraised value",
        "quick_answer": "Seasoning is how long you must own a property before a lender "
                        "will refinance against its <strong>current appraised value</strong> "
                        "rather than what you paid. Conventional programs often want twelve "
                        "months; a number of DSCR lenders will use current value after "
                        "<strong>three to six months, and some with no seasoning at all</strong>. "
                        "It matters most straight after a renovation, when purchase price and "
                        "value have diverged.",
        "sections": [
            ("What Seasoning Actually Restricts",
             "<p>Seasoning does not stop you refinancing. It decides which number the "
             "lender uses as value.</p>"
             "<p>Inside the seasoning window, many lenders lend against the lower of the "
             "appraised value and your purchase price &mdash; sometimes purchase price "
             "plus documented improvements. Outside it, they lend against the appraisal.</p>"
             "<p>For a property bought and held unchanged, the distinction rarely matters. "
             "For a property bought below market and renovated, it is the whole "
             "transaction: it determines whether the value you created is available now or "
             "in a year.</p>"),
            ("Why It Decides a Renovation Deal",
             "<p>The arithmetic is stark. Take a property bought at $250,000 with $60,000 "
             "of renovation, appraising afterwards at $380,000.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Basis</th><th>Value used</th><th>Loan at 75%</th>"
             "<th>Against $310,000 invested</th></tr></thead><tbody>"
             "<tr><td data-label=\"Basis\">Seasoned &mdash; current appraised value</td>"
             "<td data-label=\"Value\">$380,000</td><td data-label=\"Loan\">$285,000</td>"
             "<td data-label=\"Result\">Most of the capital returned</td></tr>"
             "<tr><td data-label=\"Basis\">Unseasoned &mdash; cost basis</td>"
             "<td data-label=\"Value\">$310,000</td><td data-label=\"Loan\">$232,500</td>"
             "<td data-label=\"Result\">Roughly $77,500 still tied up</td></tr>"
             "</tbody></table></div>"
             "<p>Illustrative figures, not a quote. But the gap between the two rows is "
             "the reason investors pay attention to seasoning at all &mdash; it is the "
             "difference between recycling capital into the next deal and waiting a year "
             "for it.</p>"),
            ("Documenting Improvements Inside the Window",
             "<p>Where a lender allows purchase price <em>plus improvements</em>, the "
             "improvements have to be evidenced. What is normally acceptable:</p>"
             "<ul>"
             "<li><strong>Paid invoices</strong> from contractors, itemised</li>"
             "<li><strong>Receipts for materials</strong> where you did the work</li>"
             "<li><strong>Permits</strong> for anything structural or systems-related</li>"
             "<li><strong>Before and after photographs</strong>, commonly asked for</li>"
             "<li><strong>Proof of payment</strong> &mdash; bank or card records matching "
             "the invoices</li>"
             "</ul>"
             "<p>What generally is not credited: your own labour, and estimates for work "
             "not yet done. Keep the paperwork as you go. Reconstructing it six months "
             "later is unpleasant and frequently incomplete, and a renovation you cannot "
             "evidence is a renovation the lender cannot count.</p>"),
            ("What a Shorter Window Costs",
             "<p>No-seasoning and short-seasoning programs are not free. The usual "
             "trade-offs:</p>"
             "<ul>"
             "<li><strong>A higher rate</strong> than the same lender's seasoned "
             "product</li>"
             "<li><strong>Lower maximum leverage</strong> &mdash; a tighter loan-to-value "
             "cap than a seasoned refinance would allow</li>"
             "<li><strong>Closer appraisal scrutiny</strong>, sometimes a second opinion, "
             "since the whole loan rests on a value that did not exist months ago</li>"
             "<li><strong>Reserve requirements</strong> on some programs</li>"
             "</ul>"
             "<p>Whether that is worth paying depends on what the trapped capital would "
             "earn elsewhere. If it goes straight into the next deal, a higher rate on "
             "one property can be cheap. If it sits in an account, it is not.</p>"),
            ("Fitting It Into a BRRRR",
             "<p>Buy, renovate, rent, refinance, repeat depends entirely on the refinance "
             "step, and seasoning is what governs its timing. A sequence that tends to "
             "work:</p>"
             "<ul>"
             "<li><strong>Confirm the seasoning rule before you buy</strong>, not after "
             "the renovation. It determines your capital timeline.</li>"
             "<li><strong>Get the property rented first.</strong> A signed lease "
             "strengthens the income side; see "
             "<a href=\"../what-counts-as-rental-income-dscr/\">what counts as rental "
             "income</a>.</li>"
             "<li><strong>Keep the renovation file as you go</strong> &mdash; invoices, "
             "permits, photographs, proof of payment.</li>"
             "<li><strong>Check the coverage ratio at the new loan amount</strong> before "
             "assuming the appraisal is what limits you. Often it is not; see "
             "<a href=\"../dscr-cash-out-refinance-how-much-equity/\">how much equity you "
             "can pull</a>.</li>"
             "<li><strong>Read the prepayment clause</strong> on whatever you are "
             "refinancing out of.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("What is seasoning on a DSCR loan?",
             "How long you must have owned a property before the lender will use its "
             "<strong>current appraised value</strong> rather than your purchase price. "
             "Inside the window, many lenders use the lower of appraised value and cost, "
             "sometimes cost plus documented improvements."),
            ("How long is the seasoning period?",
             "It varies by program. Conventional financing often wants twelve months, "
             "while a number of DSCR lenders will use current value after three to six "
             "months, and some have no seasoning requirement at all. It is one of the "
             "terms most worth shopping specifically."),
            ("Can I refinance immediately after renovating?",
             "With a no-seasoning or short-seasoning program, often yes. With a "
             "twelve-month rule, the lender will generally lend against your cost basis "
             "rather than the post-renovation appraisal, which leaves the value you "
             "created tied up until the window closes."),
            ("What proof of renovation do lenders accept?",
             "Itemised paid invoices, material receipts where you did the work, permits "
             "for structural or systems work, before-and-after photographs, and proof of "
             "payment matching the invoices. Your own labour is generally not credited, "
             "and neither are estimates for work not yet completed."),
            ("Do no-seasoning loans cost more?",
             "Usually. Expect a higher rate than the same lender's seasoned product, often "
             "lower maximum leverage, and closer appraisal scrutiny, since the loan rests "
             "on a value that did not exist a few months earlier. Whether that is worth it "
             "depends on what the released capital would otherwise earn."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../dscr-cash-out-refinance-how-much-equity/", "DSCR cash-out refinance: how much equity"),
            ("../dscr-exit-from-a-flip/", "Using a DSCR loan to exit a flip"),
            ("../what-counts-as-rental-income-dscr/", "What counts as rental income"),
        ],
        "sources": [SLOOS, IRS_527, CENSUS_HV],
    },
]
