# -*- coding: utf-8 -*-
"""Real-estate-secured business loans, articles 4-6."""
from cluster_res_business_loan import (SLOOS, CFPB, CFPB_MTG, FTC, IRS_527,
                                       HUD_MF, SBCS)

MORE = [
    {
        "slug": "what-equity-lenders-require-behind-a-first-mortgage",
        "crumb": "Behind a First Mortgage",
        "title": "What Equity Lenders Require Behind a First Mortgage | Axiant",
        "og_title": "What Equity Lenders Require Behind a First Mortgage",
        "h1": "What Equity Lenders Require Behind a First Mortgage",
        "headline": "What Equity Lenders Require Behind a First Mortgage",
        "lede": "The checks a subordinate lender runs before agreeing to sit "
                "behind someone else's claim",
        "meta_desc": "What a second-position lender checks: combined loan-to-value, "
                     "the senior loan's terms, title and insurance, and the equity "
                     "cushion they need behind an existing first mortgage.",
        "article_desc": "The requirements a subordinate real-estate lender applies "
                        "before lending behind a first mortgage.",
        "keywords": "second position requirements, equity lender criteria, combined "
                    "ltv, subordinate lender underwriting",
        "quick_answer": "A subordinate lender is underwriting the "
                        "<strong>cushion</strong> &mdash; whether enough equity sits "
                        "behind the first mortgage to make them whole. That means "
                        "<strong>combined loan-to-value</strong> first, then the "
                        "senior loan's terms, then title, insurance and your ability "
                        "to carry both payments. The property's value matters less "
                        "than how much of it is already spoken for.",
        "sections": [
            ("They Are Underwriting the Cushion",
             "<p>A first-position lender asks what the property is worth. A "
             "second-position lender asks what is left after the first is paid.</p>"
             "<p>That reframing explains most of what follows. A valuable property "
             "heavily mortgaged offers a thin cushion and gets treated cautiously; a "
             "modest property owned nearly outright offers a thick one and does not. "
             "The absolute value is almost incidental.</p>"
             "<p>It is also why improving the file usually means reducing what sits "
             "ahead of the new loan, not arguing the property is worth more.</p>"),
            ("The Checks, In Order",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Check</th><th>What they want</th><th>Why it decides</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Check">Combined loan-to-value</td>'
             '<td data-label="Want">Meaningful equity behind every lien</td>'
             '<td data-label="Why">The cushion; the single biggest factor</td></tr>'
             '<tr><td data-label="Check">Senior loan terms</td>'
             '<td data-label="Want">No prohibition on additional liens</td>'
             '<td data-label="Why">A prohibited second can default the first</td></tr>'
             '<tr><td data-label="Check">Title</td>'
             '<td data-label="Want">Clean, with every lien disclosed</td>'
             '<td data-label="Why">An undisclosed lien changes their real position</td></tr>'
             '<tr><td data-label="Check">Insurance</td>'
             '<td data-label="Want">Adequate cover, lender named</td>'
             '<td data-label="Why">A fire without cover destroys the collateral</td></tr>'
             '<tr><td data-label="Check">Payment capacity</td>'
             '<td data-label="Want">Both payments carried comfortably</td>'
             '<td data-label="Why">Their recovery is slow; they would rather be '
             "repaid</td></tr>"
             '<tr><td data-label="Check">Occupancy and use</td>'
             '<td data-label="Want">Clarity on owner-occupied vs tenanted</td>'
             '<td data-label="Why">Changes both the value and the recovery route</td></tr>'
             "</tbody></table></div>"),
            ("Why the Senior Loan's Terms Matter So Much",
             "<p>This is the check that most often kills an otherwise sound "
             "application, and borrowers rarely see it coming.</p>"
             "<p>Many first mortgages restrict further encumbrance. Some prohibit "
             "additional liens outright; some require the senior lender's written "
             "consent; some contain a due-on-encumbrance clause that lets the senior "
             "call the loan if another lien appears.</p>"
             "<p>A subordinate lender will not knowingly lend into a position that "
             "defaults the loan ahead of them &mdash; it makes their own security "
             "worthless. So the answer to \"can I do this\" often lives in a document "
             "you already have. Read it before applying. See "
             '<a href="../second-and-third-position-business-loans/">second and third '
             "position lending</a> for how position itself is priced.</p>"),
            ("Title and Insurance Are Not Formalities",
             "<p>They read as closing admin and they are where deals stall.</p>"
             "<p><strong>Title</strong> has to show every lien. An undisclosed "
             "judgment, tax lien or mechanic's lien does not just delay things &mdash; "
             "it changes the lender's actual position, potentially from second to "
             "third or worse. Order the search early rather than at closing.</p>"
             "<p><strong>Insurance</strong> has to be adequate and correctly named, "
             "and if the property is held in an entity the policy must be in that "
             "entity's name rather than yours personally. It is a common and "
             "avoidable last-minute problem.</p>"),
            ("What Gets a Subordinate Application Declined",
             "<p>Declines here cluster into a small number of causes, and most are "
             "visible before you apply:</p>"
             "<ul>"
             "<li><strong>The cushion is too thin.</strong> The most common by some "
             "distance. Combined liens leave too little equity for the lender to "
             "recover from, and no amount of business strength compensates &mdash; "
             "their exposure is to the property, not the trading.</li>"
             "<li><strong>The senior loan prohibits it.</strong> A hard stop rather "
             "than a judgement call, and one that lives in a document you already "
             "hold.</li>"
             "<li><strong>Title surprises.</strong> An undisclosed lien pushes the "
             "lender further down the queue than the deal they agreed to, which is a "
             "different transaction from the one they underwrote.</li>"
             "<li><strong>The property is hard to sell.</strong> Special-purpose "
             "buildings, unusual zoning or rural locations narrow the buyer pool. A "
             "subordinate lender's recovery depends on a sale actually happening at a "
             "sensible price.</li>"
             "<li><strong>Capacity does not cover both payments.</strong> Foreclosing "
             "is slow, expensive and uncertain from second position; a lender who "
             "doubts they will simply be repaid usually declines rather than prices "
             "for it.</li>"
             "</ul>"
             "<p>Notice that four of the five are about the collateral and the "
             "structure rather than about you. That is the nature of subordinate "
             "lending, and it is why the fixes are structural too.</p>"),
            ("Strengthening the File",
             "<ul>"
             "<li><strong>Pay down the first</strong> if you can. Nothing else moves "
             "the cushion as directly.</li>"
             "<li><strong>Get a current valuation</strong> rather than relying on what "
             "you believe the property is worth.</li>"
             "<li><strong>Clear small liens</strong> before applying &mdash; a stale "
             "judgment can be cheap to resolve and expensive to leave.</li>"
             "<li><strong>Bring the senior loan documents</strong> to the first "
             "conversation. It saves a week.</li>"
             "<li><strong>Show both payments covered</strong> from documented cash "
             "flow, not projections.</li>"
             "</ul>"
             "<p>If the cushion is genuinely thin, a subordinate loan may be the wrong "
             "instrument regardless of how the file is presented.</p>"),
        ],
        "faqs": [
            ("What combined loan-to-value do second-position lenders want?",
             "They want meaningful equity remaining behind every lien, and the "
             "threshold varies by lender and property type. The principle is constant: "
             "they are underwriting the cushion left after the first mortgage, not the "
             "property's headline value."),
            ("Why do they care about my first mortgage's terms?",
             "Because many first mortgages restrict further encumbrance. If taking a "
             "second would default or trigger the senior loan, the subordinate "
             "lender's own security becomes worthless, so they will not knowingly lend "
             "into that position."),
            ("What can go wrong with title?",
             "An undisclosed lien &mdash; a judgment, tax lien or mechanic's lien "
             "&mdash; changes the lender's real position, potentially pushing them "
             "further down the queue than agreed. Ordering the search early avoids "
             "discovering it at closing."),
            ("Do they check whether I can afford both payments?",
             "Yes. A subordinate lender's recovery route is slow and uncertain, so "
             "they would much rather be repaid than foreclose. Documented capacity to "
             "carry both payments matters more here than on a first mortgage."),
            ("What improves a thin file most?",
             "Reducing what sits ahead of the new loan. Paying down the first mortgage "
             "moves the cushion directly, in a way that arguing for a higher valuation "
             "does not."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("../second-and-third-position-business-loans/",
             "Second and third position business loans"),
            ("../how-fast-can-an-equity-secured-business-loan-close/",
             "How fast an equity-secured loan closes"),
            ("../cross-collateralization-what-youre-signing/",
             "Cross-collateralisation: what you are signing"),
        ],
        "sources": [SLOOS, CFPB_MTG, FTC],
    },
    {
        "slug": "real-estate-secured-vs-unsecured-business-loan",
        "crumb": "Secured vs Unsecured",
        "title": "Real-Estate-Secured vs Unsecured Business Loan | Axiant",
        "og_title": "Real-Estate-Secured vs Unsecured Business Loan",
        "h1": "Real-Estate-Secured vs Unsecured Business Loan",
        "headline": "Real-Estate-Secured vs Unsecured Business Loan",
        "lede": "What pledging property buys you, and what it costs that a rate "
                "comparison will not show",
        "meta_desc": "Secured or unsecured business borrowing? Property collateral "
                     "buys a lower rate and longer terms; unsecured costs more but "
                     "keeps the asset out of it. How to weigh the trade honestly.",
        "article_desc": "How real-estate-secured and unsecured business borrowing "
                        "differ in cost, speed and consequence.",
        "keywords": "secured vs unsecured business loan, collateral business loan, "
                    "unsecured working capital, property collateral risk",
        "quick_answer": "Pledging property buys a <strong>lower rate, a longer term "
                        "and a larger amount</strong>. Unsecured borrowing costs more "
                        "per dollar and is faster, but the failure mode is contained "
                        "&mdash; a bad outcome is a debt problem rather than losing a "
                        "building. The right comparison is not the rate; it is what "
                        "each one costs you if the plan does not work.",
        "sections": [
            ("What Collateral Actually Buys",
             "<p>Security lowers a lender's loss if things go wrong, and they pass "
             "part of that back. The benefits are real and worth naming:</p>"
             "<ul>"
             "<li><strong>A materially lower rate</strong> than unsecured credit</li>"
             "<li><strong>A longer term</strong>, so a lower payment for the same "
             "amount</li>"
             "<li><strong>A larger amount</strong>, governed by equity rather than "
             "revenue</li>"
             "<li><strong>Availability when revenue is thin</strong>, since the "
             "collateral carries more of the decision</li>"
             "</ul>"
             "<p>For a business with real property equity and a defined need, that "
             "combination is hard to beat on cost.</p>"),
            ("The Comparison",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Real-estate-secured</th><th>Unsecured</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Rate</strong></td>'
             '<td data-label="Secured">Lower</td><td data-label="Unsecured">Higher</td></tr>'
             '<tr><td data-label=""><strong>Term</strong></td>'
             '<td data-label="Secured">Longer</td>'
             '<td data-label="Unsecured">Short &mdash; often under two years</td></tr>'
             '<tr><td data-label=""><strong>Amount driven by</strong></td>'
             '<td data-label="Secured">Equity in the property</td>'
             '<td data-label="Unsecured">Revenue and credit</td></tr>'
             '<tr><td data-label=""><strong>Speed</strong></td>'
             '<td data-label="Secured">Slower &mdash; valuation, title, recording</td>'
             '<td data-label="Unsecured">Days</td></tr>'
             '<tr><td data-label=""><strong>Paperwork</strong></td>'
             '<td data-label="Secured">Heavy</td><td data-label="Unsecured">Light</td></tr>'
             '<tr><td data-label=""><strong>If it goes wrong</strong></td>'
             '<td data-label="Secured">The property is at risk</td>'
             '<td data-label="Unsecured">A debt problem, contained</td></tr>'
             "</tbody></table></div>"),
            ("Pricing the Downside, Not Just the Rate",
             "<p>Most comparisons stop at cost per dollar, and that is the half of the "
             "question that is easy to compute.</p>"
             "<p>The other half: if this does not work, what happens? Unsecured default "
             "is serious &mdash; collections, credit damage, and a personal guarantee "
             "that follows the owner. Secured default can take a building that took a "
             "decade to acquire and may house the business or a tenant.</p>"
             "<p>Those are not the same magnitude, and the rate difference is the "
             "price of that gap. Sometimes it is worth paying to keep the property out "
             "of the question; sometimes the saving is large enough that it is not. "
             "The point is to make the choice deliberately rather than by picking the "
             "lower number.</p>"),
            ("Match the Instrument to the Need",
             "<p>A reliable test is how long the need lasts and what repays it.</p>"
             "<ul>"
             "<li><strong>Short and self-liquidating</strong> &mdash; a receivable "
             "gap, a seasonal build. Unsecured usually fits; the higher rate applies "
             "briefly and the asset stays clear.</li>"
             "<li><strong>Long and structural</strong> &mdash; an acquisition, a "
             "building purchase, consolidating expensive debt. Secured fits; a "
             "multi-year need on short-term money is how businesses end up "
             "refinancing under pressure.</li>"
             "<li><strong>Large relative to revenue</strong> &mdash; often only "
             "secured borrowing reaches the number at all.</li>"
             "<li><strong>Urgent</strong> &mdash; unsecured, simply on speed. A "
             "secured loan cannot close in three days.</li>"
             "</ul>"),
            ("What a Personal Guarantee Does and Does Not Change",
             "<p>Worth separating, because the two words get used interchangeably and "
             "they are not the same thing.</p>"
             "<p><strong>Unsecured</strong> means no specific asset is pledged. It "
             "does not mean nobody is liable. Most small business borrowing carries a "
             "personal guarantee either way, so an unsecured default still reaches the "
             "owner &mdash; through collections, a judgment, and credit damage that "
             "follows them personally.</p>"
             "<p>What the guarantee does not give the lender is a <em>named</em> asset "
             "they can move against directly. A secured lender has a defined route to "
             "a defined building. An unsecured lender with a guarantee has to obtain a "
             "judgment first and then find something to enforce against, which is "
             "slower, costlier and far less certain.</p>"
             "<p>That gap is most of what the rate difference is buying. It is also "
             "why \"I am personally guaranteeing it anyway, so I may as well pledge "
             "the property\" is the wrong conclusion &mdash; the guarantee is a claim, "
             "the lien is a key.</p>"),
            ("The Middle Options",
             "<p>It is not a binary. Between the two sit instruments that secure "
             "something other than your building.</p>"
             "<p>Equipment secures itself. Invoices can be financed on their own "
             "strength. A truck can be pledged rather than a property &mdash; see "
             '<a href="/commercial-truck-title-loan.html">commercial truck title '
             "loans</a>. Each isolates the risk to one asset rather than the "
             "property.</p>"
             "<p>Where the business already owns an asset that matches the need, "
             "pledging that asset is usually better than reaching for the most "
             "valuable thing on the balance sheet.</p>"),
        ],
        "faqs": [
            ("Is a secured business loan always cheaper?",
             "On rate, usually and often substantially, because the lender's loss "
             "given default is lower. Whether it is cheaper in the round depends on "
             "what you are risking, which a rate comparison does not capture."),
            ("How much faster is unsecured borrowing?",
             "Considerably. Unsecured can fund in days; a real-estate-secured loan "
             "needs a valuation, title work and recording, which takes weeks. If the "
             "need is genuinely urgent, speed may decide it regardless of cost."),
            ("When should I not pledge property?",
             "When the need is short and self-liquidating, when the business is "
             "covering a loss rather than a timing gap, or when a smaller asset could "
             "secure the loan instead. Reaching for the most valuable asset on the "
             "balance sheet should be a considered decision, not a default one."),
            ("Does unsecured mean no personal liability?",
             "No. Unsecured means no specific asset is pledged, not that nobody is on "
             "the hook. Most small business borrowing carries a personal guarantee "
             "either way; what differs is whether a named asset can be taken."),
            ("What sits between the two?",
             "Financing that secures something other than your building &mdash; "
             "equipment securing itself, invoice financing against receivables, or a "
             "truck title loan. Each isolates the risk to one asset instead of the "
             "property."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../business-loan-against-rental-property/",
             "Business loan against a rental property"),
            ("/working-capital-loans.html", "Working capital loans"),
        ],
        "sources": [SBCS, CFPB, FTC],
    },
    {
        "slug": "how-fast-can-an-equity-secured-business-loan-close",
        "crumb": "How Fast It Closes",
        "title": "How Fast Can an Equity-Secured Business Loan Close? | Axiant",
        "og_title": "How Fast Can an Equity-Secured Business Loan Close?",
        "h1": "How Fast Can an Equity-Secured Business Loan Close?",
        "headline": "How Fast Can an Equity-Secured Business Loan Close",
        "lede": "The real timeline, which steps actually take the time, and "
                "what you can do in parallel",
        "meta_desc": "Equity-secured business loans close in weeks, not days. Where "
                     "the time actually goes - valuation, title, senior lender "
                     "consent - and which steps you can run in parallel.",
        "article_desc": "The realistic timeline on a real-estate-secured business "
                        "loan and how to compress it.",
        "keywords": "how fast equity secured loan, second position closing time, "
                    "business loan against property timeline, title search time",
        "quick_answer": "Weeks rather than days. The lender's decision is rarely the "
                        "bottleneck &mdash; <strong>valuation, title work and, where "
                        "required, the senior lender's consent</strong> are, and the "
                        "last of those is the least predictable because it depends on "
                        "someone with no stake in your deadline. Ordering title early "
                        "and having the senior loan documents ready compresses it "
                        "more than anything else.",
        "sections": [
            ("Where the Time Actually Goes",
             "<p>Borrowers assume underwriting is the slow part. It usually is not.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Step</th><th>Typical shape</th><th>Can it run in parallel?</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Step">Application and credit review</td>'
             '<td data-label="Shape">Days</td><td data-label="Parallel">Starts everything</td></tr>'
             '<tr><td data-label="Step">Valuation</td>'
             '<td data-label="Shape">Scheduling plus report turnaround</td>'
             '<td data-label="Parallel">Yes &mdash; order it immediately</td></tr>'
             '<tr><td data-label="Step">Title search</td>'
             '<td data-label="Shape">Days, longer where records are not digitised</td>'
             '<td data-label="Parallel">Yes, and it should be</td></tr>'
             '<tr><td data-label="Step">Senior lender consent</td>'
             '<td data-label="Shape">The wild card &mdash; days to weeks</td>'
             '<td data-label="Parallel">Yes, and start it first</td></tr>'
             '<tr><td data-label="Step">Underwriting decision</td>'
             '<td data-label="Shape">Days once the file is complete</td>'
             '<td data-label="Parallel">Needs the above</td></tr>'
             '<tr><td data-label="Step">Documents, signing, recording</td>'
             '<td data-label="Shape">Days</td><td data-label="Parallel">No</td></tr>'
             "</tbody></table></div>"
             "<p>Two of the three slowest steps depend on third parties who do not "
             "know your timeline exists.</p>"),
            ("Senior Lender Consent Is the Unpredictable One",
             "<p>Where the first mortgage requires consent to a further lien, that "
             "consent is the single least controllable part of the process.</p>"
             "<p>It sits with an institution that has no commercial interest in your "
             "deadline, often routes through a department rather than a person, and "
             "may take a view rather than simply signing. It can also be refused.</p>"
             "<p>So this is the first thing to check and the first request to make "
             "&mdash; before the valuation is ordered, not after. See "
             '<a href="../what-equity-lenders-require-behind-a-first-mortgage/">what '
             "equity lenders require behind a first mortgage</a> for what else lives "
             "in that senior loan document.</p>"),
            ("Title Is the Quiet Delay",
             "<p>Title work rarely takes long in itself. What takes long is what it "
             "finds.</p>"
             "<p>An old judgment, an unreleased lien from a loan you settled years "
             "ago, a mechanic's lien from a contractor dispute, an unpaid tax bill "
             "&mdash; each has to be cleared or subordinated before closing, and "
             "clearing one involves a third party too.</p>"
             "<p>The lesson is to order the search at the start rather than as a "
             "closing formality. A lien found in week one is an administrative task; "
             "the same lien found in week four is a delay.</p>"),
            ("What You Can Do to Compress It",
             "<ul>"
             "<li><strong>Read the senior loan agreement on day one</strong> and, if "
             "consent is needed, request it immediately.</li>"
             "<li><strong>Order title early</strong>, before underwriting asks.</li>"
             "<li><strong>Have the payoff figure in writing</strong> for every "
             "existing lien.</li>"
             "<li><strong>Sort insurance</strong> in the correct entity's name with "
             "the lender named, before it becomes a closing condition.</li>"
             "<li><strong>Assemble entity documents</strong> if the property is held "
             "in an LLC, including a foreign qualification where the entity and the "
             "property are in different states.</li>"
             "<li><strong>Answer conditions the same day.</strong> Files stall in the "
             "gaps between requests far more than in the work itself.</li>"
             "</ul>"),
            ("If You Genuinely Need Money This Week",
             "<p>Then this is not the instrument, and no amount of preparation makes "
             "it one. A valuation and a title search cannot be compressed into "
             "days.</p>"
             "<p>For a genuine emergency, unsecured working capital funds far faster "
             "and costs more &mdash; see "
             '<a href="../real-estate-secured-vs-unsecured-business-loan/">secured '
             "versus unsecured</a>. A reasonable pattern is to bridge the urgent need "
             "with fast money and take the secured loan at its own pace to repay it, "
             "provided the secured loan is genuinely coming.</p>"
             "<p>What does not work is treating a weeks-long process as though "
             "pressure will shorten it. The valuer and the title company are not "
             "moving.</p>"),
        ],
        "faqs": [
            ("How long does a real-estate-secured business loan take?",
             "Weeks rather than days. The decision itself is quick once the file is "
             "complete; the time goes to valuation, title work and, where required, "
             "the senior lender's consent."),
            ("What is the slowest part?",
             "Senior lender consent, where the first mortgage requires it. It depends "
             "on an institution with no stake in your deadline, often routes through a "
             "department rather than a person, and can be refused outright."),
            ("Why does title work cause delays?",
             "Not the search itself but what it finds &mdash; an old judgment, an "
             "unreleased lien, a mechanic's lien, unpaid taxes. Each has to be cleared "
             "or subordinated, and each involves another third party. Ordering it "
             "early turns a delay into an admin task."),
            ("Can I speed it up?",
             "Materially, yes. Read the senior loan agreement on day one and request "
             "any consent immediately, order title before you are asked, have written "
             "payoff figures ready, sort insurance in the right name, and answer "
             "conditions the same day."),
            ("What if I need the money this week?",
             "Then this is the wrong instrument &mdash; a valuation and title search "
             "cannot compress into days. Unsecured working capital funds far faster at "
             "higher cost, and can bridge to a secured loan that is genuinely coming."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("../what-equity-lenders-require-behind-a-first-mortgage/",
             "What equity lenders require behind a first mortgage"),
            ("../real-estate-secured-vs-unsecured-business-loan/",
             "Secured vs unsecured business loans"),
            ("/working-capital-loans.html", "Working capital loans"),
        ],
        "sources": [CFPB_MTG, SLOOS, SBCS],
    },
]
