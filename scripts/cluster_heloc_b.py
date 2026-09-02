# -*- coding: utf-8 -*-
"""HELOC for business, articles 3-5.

The tax article is deliberately the most cautious page in the cluster. It
explains the shape of the rules and points at the primary sources, and it says
in the quick answer, the body and the FAQ that it is general information and
that the reader must confirm with their CPA. It states no deductibility
conclusion for any reader's situation.
"""
from cluster_heloc import (IRS_936, IRS_535, CFPB_HE, CFPB, CFPB_MTG,
                           SLOOS, SBCS, FTC)

MORE = [
    {
        "slug": "heloc-vs-cash-out-refinance-for-business-capital",
        "crumb": "HELOC vs Cash-Out Refinance",
        "title": "HELOC vs Cash-Out Refinance for Business Capital | Axiant",
        "og_title": "HELOC vs Cash-Out Refinance for Business Capital",
        "h1": "HELOC vs Cash-Out Refinance for Business Capital",
        "headline": "HELOC vs Cash-Out Refinance for Business Capital",
        "lede": "Two ways to reach the same equity - one leaves your first "
                "mortgage alone, the other replaces it",
        "meta_desc": "HELOC or cash-out refinance to fund a business? One adds a "
                     "second line and keeps your existing mortgage; the other "
                     "replaces it entirely. When each is worth it.",
        "article_desc": "How a HELOC and a cash-out refinance differ when the "
                        "purpose is business capital.",
        "keywords": "heloc vs cash out refinance, refinance to fund business, home "
                    "equity business capital, second mortgage business",
        "quick_answer": "A <strong>HELOC</strong> sits alongside your existing "
                        "mortgage as a revolving second line, so a low rate you "
                        "already hold is untouched. A <strong>cash-out refinance</strong> "
                        "replaces the first mortgage entirely with a larger one. If "
                        "your existing rate is below what the market offers today, "
                        "refinancing to reach equity can cost far more over the "
                        "remaining term than the HELOC's higher rate on a smaller "
                        "balance.",
        "sections": [
            ("The Question Is What Happens to Your First Mortgage",
             "<p>Both reach the same equity. The difference is what they do to the "
             "loan you already have.</p>"
             "<p>A HELOC leaves it completely alone and adds a second, revolving line "
             "behind it. A cash-out refinance pays it off and replaces it with a "
             "single larger mortgage at today's rate on the whole balance.</p>"
             "<p>That distinction is worth more than any rate comparison when you hold "
             "an older, cheaper mortgage. Refinancing to release equity re-prices "
             "every dollar you already owe, not just the new money.</p>"),
            ("Where the Cost Actually Lands",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>HELOC</th><th>Cash-out refinance</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Existing mortgage</strong></td>'
             '<td data-label="HELOC">Untouched</td>'
             '<td data-label="Refi">Repaid and replaced</td></tr>'
             '<tr><td data-label=""><strong>Rate applies to</strong></td>'
             '<td data-label="HELOC">Only what you draw</td>'
             '<td data-label="Refi">The entire new balance</td></tr>'
             '<tr><td data-label=""><strong>Rate type</strong></td>'
             '<td data-label="HELOC">Usually variable</td>'
             '<td data-label="Refi">Usually fixed</td></tr>'
             '<tr><td data-label=""><strong>Access</strong></td>'
             '<td data-label="HELOC">Revolving during the draw period</td>'
             '<td data-label="Refi">One lump sum</td></tr>'
             '<tr><td data-label=""><strong>Closing costs</strong></td>'
             '<td data-label="HELOC">Lower</td>'
             '<td data-label="Refi">Full mortgage costs</td></tr>'
             '<tr><td data-label=""><strong>Payments</strong></td>'
             '<td data-label="HELOC">Two</td><td data-label="Refi">One</td></tr>'
             "</tbody></table></div>"
             "<p>The second row is the one that decides most cases. A HELOC prices "
             "only the money you actually use; a refinance re-prices the whole "
             "mortgage.</p>"),
            ("The Arithmetic Worth Doing",
             "<p>A worked shape rather than a rule. Suppose $200,000 remains on a "
             "mortgage taken at a low rate some years ago, and the business needs "
             "$60,000.</p>"
             "<p>Under a <strong>HELOC</strong>, the $200,000 keeps its old rate and "
             "the higher HELOC rate applies to $60,000.</p>"
             "<p>Under a <strong>cash-out refinance</strong>, all $260,000 sits at "
             "today's rate. If today's rate is meaningfully above the old one, the "
             "extra cost on the $200,000 you were not trying to borrow can exceed the "
             "entire cost of the HELOC.</p>"
             "<p>Run it as total interest over the years you expect to hold the "
             "property, not as a monthly payment comparison. The monthly figure can "
             "favor the refinance while the total cost does not, because a refinance "
             "usually restarts the amortisation.</p>"),
            ("When the Refinance Still Wins",
             "<ul>"
             "<li><strong>Your existing rate is at or above today's.</strong> Then "
             "there is nothing cheap to protect and one loan is simpler.</li>"
             "<li><strong>You want a fixed rate.</strong> HELOCs are typically "
             "variable, and a business plan that cannot absorb a rate rise is worth "
             "insulating.</li>"
             "<li><strong>You need the full amount now.</strong> A refinance delivers "
             "a lump sum; a HELOC delivers a facility.</li>"
             "<li><strong>You want one payment.</strong> Worth something, though "
             "rarely worth the arithmetic on its own.</li>"
             "<li><strong>The draw period ending would leave you exposed</strong> "
             "&mdash; a fixed loan has no such transition.</li>"
             "</ul>"),
            ("Closing Costs Change the Threshold",
             "<p>Cost per dollar is only half the comparison. The fixed cost of "
             "getting the money decides whether a route is worth taking at all.</p>"
             "<p>A cash-out refinance is a full mortgage transaction &mdash; "
             "origination, appraisal, title work, recording, and in some states "
             "transfer taxes. Those costs are broadly the same whether you release "
             "$40,000 or $200,000, which means they are trivial spread across a large "
             "release and punitive across a small one.</p>"
             "<p>A HELOC is much lighter, and some lenders waive costs entirely in "
             "exchange for an early-closure fee if you shut the line within a set "
             "period. That is worth reading before assuming a no-cost line is "
             "genuinely free.</p>"
             "<p>The practical effect: below a certain size, a refinance rarely makes "
             "sense however attractive the rate looks, because the closing costs "
             "consume the benefit. Work out the total cost including fees over your "
             "expected hold rather than comparing rates.</p>"),
            ("Both Put the House Behind the Business",
             "<p>Worth restating, because the comparison above is a cost analysis and "
             "cost is not the whole question.</p>"
             "<p>Whichever route, the money is secured on your home and the purpose is "
             "business risk. A cash-out refinance arguably goes further, because it "
             "puts the whole mortgage into the transaction rather than adding a "
             "smaller second position.</p>"
             "<p>Before optimising between them, it is worth checking the prior "
             "question: whether a business facility can do the job at a higher rate "
             "and leave the house out of it. See "
             '<a href="../heloc-vs-business-line-of-credit/">HELOC versus a business '
             "line of credit</a>.</p>"),
        ],
        "faqs": [
            ("Should I refinance my mortgage to fund my business?",
             "Only if your existing rate is at or above today's. If you hold an older, "
             "cheaper mortgage, refinancing re-prices the entire balance rather than "
             "just the new money, and that extra cost can exceed the whole cost of a "
             "HELOC."),
            ("Which has lower closing costs?",
             "A HELOC, generally and by a clear margin. A cash-out refinance is a full "
             "mortgage transaction with full mortgage costs, which is another reason "
             "it suits larger needs better than smaller ones."),
            ("Is a HELOC rate fixed?",
             "Usually variable, where a cash-out refinance is usually fixed. If the "
             "business plan cannot absorb a rate rise, that difference matters and may "
             "outweigh the cost advantage."),
            ("Which gets me the money faster?",
             "Both are mortgage-speed rather than days, but a HELOC is generally "
             "lighter and closes sooner. Neither is an emergency instrument."),
            ("Does a cash-out refinance restart my mortgage term?",
             "Typically yes, and it is easy to miss. A lower monthly payment achieved "
             "by restarting amortisation can still mean more total interest, which is "
             "why the comparison should be run on total cost over your expected hold "
             "rather than on the monthly figure."),
        ],
        "related": [
            ("/heloc-for-business.html", "HELOC for business"),
            ("../heloc-vs-business-line-of-credit/", "HELOC vs business line of credit"),
            ("/dscr-loans/articles/dscr-cash-out-refinance-how-much-equity/",
             "Cash-out refinance: how much equity"),
            ("../heloc-interest-when-used-for-business/",
             "HELOC interest when used for business"),
        ],
        "sources": [CFPB_HE, CFPB_MTG, SLOOS],
    },
    {
        "slug": "what-happens-to-a-heloc-if-the-business-fails",
        "crumb": "If the Business Fails",
        "title": "What Happens to a HELOC If the Business Fails | Axiant",
        "og_title": "What Happens to a HELOC If the Business Fails",
        "h1": "What Happens to a HELOC If the Business Fails",
        "headline": "What Happens to a HELOC If the Business Fails",
        "lede": "The scenario nobody plans for - what a home-secured business "
                "debt does when the business stops paying it",
        "meta_desc": "A HELOC drawn for a business is personal debt secured by your "
                     "home. What happens if the business fails, why closing the "
                     "company does not clear it, and where to act early.",
        "article_desc": "What a HELOC drawn for business purposes does when the "
                        "business fails, and the realistic options.",
        "keywords": "heloc business failure, home equity business risk, business "
                    "closed heloc, foreclosure business debt",
        "quick_answer": "The debt does not go with the business. A HELOC is "
                        "<strong>personal borrowing secured by your home</strong>, so "
                        "closing the company, dissolving an LLC or a business "
                        "bankruptcy does not clear it &mdash; the balance remains "
                        "yours and the lien remains on the house. That is the whole "
                        "risk, and it is the part that is easiest not to think about "
                        "at the point of drawing.",
        "sections": [
            ("The Debt Was Never the Business's",
             "<p>This is the thing to understand before drawing rather than after.</p>"
             "<p>A HELOC is issued to you personally against your home. Using the "
             "proceeds for the business does not make the business the borrower. The "
             "company never signed, so it was never liable, and it cannot take the "
             "debt with it when it goes.</p>"
             "<p>That is why an LLC offers no protection here. Owners who carefully "
             "structured an entity to separate business and personal liability can "
             "route straight around it by funding the business from a home-secured "
             "line, and the structure does exactly nothing against that debt.</p>"),
            ("What Actually Happens, In Order",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Stage</th><th>What happens</th></tr></thead><tbody>"
             '<tr><td data-label="Stage">Business stops generating</td>'
             '<td data-label="What">The HELOC payment continues; it is your payment, '
             "not the company's</td></tr>"
             '<tr><td data-label="Stage">Draw period may end</td>'
             '<td data-label="What">The line closes to new draws and converts to '
             "principal and interest, often a higher payment</td></tr>"
             '<tr><td data-label="Stage">Payments missed</td>'
             '<td data-label="What">Late fees, then default under the loan; personal '
             "credit damage</td></tr>"
             '<tr><td data-label="Stage">Continued default</td>'
             '<td data-label="What">The lender can pursue foreclosure on the property '
             "securing the line</td></tr>"
             '<tr><td data-label="Stage">Business dissolved or bankrupt</td>'
             '<td data-label="What">No effect on this debt &mdash; it was never the '
             "business's</td></tr>"
             "</tbody></table></div>"
             "<p>The second row deserves attention. A business under strain often "
             "coincides with a draw period ending, which raises the payment at exactly "
             "the worst moment.</p>"),
            ("Position Matters to the Outcome",
             "<p>Most HELOCs sit in second position behind a first mortgage, and that "
             "affects how a lender behaves.</p>"
             "<p>A second-position lender foreclosing has to deal with the first "
             "mortgage, and if there is little equity above it, foreclosure may "
             "recover nothing. That does not make them harmless &mdash; they can still "
             "sue on the debt and pursue a judgment &mdash; but it does mean a "
             "second-position lender is often more willing to negotiate than a first "
             "would be.</p>"
             "<p>Where there is substantial equity, that calculus changes and "
             "foreclosure becomes a realistic route. The amount of equity above the "
             "first mortgage is a good predictor of how the lender will behave.</p>"),
            ("Where to Act, and When",
             "<p>The options are widest early and narrow quickly:</p>"
             "<ul>"
             "<li><strong>Before missing anything.</strong> Talk to the lender. "
             "Hardship arrangements, interest-only spells and modifications exist, and "
             "are far easier to obtain before a default than after.</li>"
             "<li><strong>Stop drawing.</strong> Obvious and frequently not done. "
             "Funding a loss from home equity enlarges the problem rather than "
             "postponing it.</li>"
             "<li><strong>Separate the business's fate from the debt's.</strong> "
             "Closing the business may still be right &mdash; just do not expect it to "
             "address the HELOC.</li>"
             "<li><strong>Look at the whole picture.</strong> Where there is other "
             "business debt, "
             '<a href="/mca-debt-relief.html">business debt relief</a> may address '
             "more of the problem than focusing on this one line.</li>"
             "<li><strong>Take advice.</strong> Foreclosure, deficiency and homestead "
             "rules are state law and vary considerably.</li>"
             "</ul>"),
            ("The Decision This Should Inform",
             "<p>None of this is an argument that a HELOC is the wrong instrument. It "
             "is cheap money, and for a business that works it is a rational way to "
             "fund a defined need.</p>"
             "<p>It is an argument for making the decision with the failure case in "
             "view. Before drawing, ask what the household does if the business does "
             "not work &mdash; and if the answer is that you lose the house, the "
             "cheaper rate is not compensation for that.</p>"
             "<p><strong>This is general information, not legal advice.</strong> "
             "Foreclosure procedure, deficiency rules and homestead protections differ "
             "by state; if a default is close or has happened, take advice from an "
             "attorney in yours.</p>"),
        ],
        "faqs": [
            ("Does closing my business clear a HELOC I used for it?",
             "No. The HELOC is personal borrowing secured by your home, and the "
             "business never signed for it. Dissolving the company, closing it or a "
             "business bankruptcy leaves the balance yours and the lien in place."),
            ("Does having an LLC protect my house here?",
             "Not against this debt. An LLC separates business liabilities from "
             "personal ones, but a HELOC was never a business liability &mdash; it is "
             "yours, secured by your home. Funding the business this way routes around "
             "the protection the entity provides."),
            ("Can the lender foreclose if I stop paying?",
             "Yes, subject to state procedure. Most HELOCs sit behind a first "
             "mortgage, and where there is little equity above it a second-position "
             "lender may prefer to negotiate or sue on the debt rather than foreclose "
             "&mdash; but with substantial equity, foreclosure becomes realistic."),
            ("What should I do first if I see trouble coming?",
             "Contact the lender before missing a payment, and stop drawing. Hardship "
             "arrangements and modifications are much easier to obtain before a "
             "default than after, and continuing to draw against a loss enlarges the "
             "problem rather than postponing it."),
            ("Does the draw period ending make this worse?",
             "It often does, and the timing is cruel. When the draw period ends the "
             "line closes to new draws and converts to principal and interest, so the "
             "payment can step up at the same moment the business is under strain."),
        ],
        "related": [
            ("/heloc-for-business.html", "HELOC for business"),
            ("../personal-guarantee-risk-home-equity-business/",
             "Personal guarantee and home equity risk"),
            ("/mca-debt-relief.html", "Business debt relief"),
            ("../heloc-vs-business-line-of-credit/", "HELOC vs business line of credit"),
        ],
        "sources": [CFPB_HE, CFPB_MTG, FTC],
    },
    {
        "slug": "heloc-interest-when-used-for-business",
        "crumb": "Interest and Tax",
        "title": "HELOC Interest When Used for Business: What to Know | Axiant",
        "og_title": "HELOC Interest When Used for Business: What to Know",
        "h1": "HELOC Interest When the Proceeds Fund a Business",
        "headline": "HELOC Interest When Used for Business",
        "lede": "Why the answer depends on what the money did, and why this is a "
                "question for your CPA rather than your lender",
        "meta_desc": "How HELOC interest is treated when the proceeds fund a "
                     "business depends on use, tracing and your circumstances. The "
                     "shape of the rules, the primary sources, and why to ask a CPA.",
        "article_desc": "General information on how the use of HELOC proceeds bears "
                        "on the treatment of the interest, with primary sources.",
        "keywords": "heloc interest business, home equity interest deduction, "
                    "interest tracing, business use home equity",
        "quick_answer": "<strong>This is general information, not tax advice.</strong> "
                        "The treatment of interest on home-secured borrowing depends "
                        "on <strong>what the proceeds were used for</strong>, how well "
                        "that use is documented, and your own circumstances &mdash; "
                        "there is no single answer that applies to every reader. The "
                        "primary sources are IRS Publications 936 and 535. "
                        "<strong>Confirm your position with your CPA before relying "
                        "on any treatment.</strong>",
        "sections": [
            ("Why There Is No Single Answer",
             "<p>People want a yes or a no here, and the honest response is that the "
             "question is not well formed without more facts.</p>"
             "<p>Interest on borrowing is generally categorised by <strong>what the "
             "borrowed money was used for</strong>, not simply by what secured it. "
             "That means the same HELOC can be treated differently depending on where "
             "the proceeds went, and a single line drawn for several purposes can have "
             "its interest split between categories.</p>"
             "<p>So an article cannot tell you your answer. What it can do is set out "
             "the shape of the question so that the conversation with your accountant "
             "is a short one.</p>"),
            ("The Two Primary Sources",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Source</th><th>What it covers</th></tr></thead><tbody>"
             '<tr><td data-label="Source">'
             '<a href="https://www.irs.gov/publications/p936" rel="noopener nofollow" '
             'target="_blank">IRS Publication 936</a></td>'
             '<td data-label="Covers">Home mortgage interest &mdash; the rules on '
             "interest secured by a residence, and how the use of the proceeds bears "
             "on it</td></tr>"
             '<tr><td data-label="Source">'
             '<a href="https://www.irs.gov/publications/p535" rel="noopener nofollow" '
             'target="_blank">IRS business expense guidance</a></td>'
             '<td data-label="Covers">Deductible business expenses, including interest '
             "on borrowing used in a trade or business</td></tr>"
             "</tbody></table></div>"
             "<p>Both are federal and current. Neither replaces advice on your own "
             "facts, and state treatment can differ from federal.</p>"),
            ("Tracing Is the Practical Issue",
             "<p>Whatever the treatment turns out to be, the ability to support it "
             "rests on being able to show where the money went. That is the part you "
             "control, and the part most often neglected.</p>"
             "<p>What makes tracing straightforward:</p>"
             "<ul>"
             "<li><strong>Draw for one purpose at a time</strong> rather than taking a "
             "lump and spending it across categories</li>"
             "<li><strong>Move business draws into the business account</strong> "
             "directly, rather than through a personal account</li>"
             "<li><strong>Keep the paperwork</strong> for what the money bought, "
             "matched to the draw</li>"
             "<li><strong>Avoid mixing</strong> a business draw with personal spending "
             "in the same account and period</li>"
             "<li><strong>Tell your accountant when it happens</strong>, not at "
             "year-end</li>"
             "</ul>"
             "<p>Money that lands in a personal account and is spent from there is "
             "considerably harder to trace afterwards than money that went straight to "
             "the business.</p>"),
            ("What Your Accountant Will Want",
             "<p>Turning up with these makes the question answerable in one "
             "conversation:</p>"
             "<ul>"
             "<li>The <strong>loan documents</strong>, showing what secures the line "
             "and when it was taken</li>"
             "<li>A <strong>schedule of draws</strong> with dates and amounts</li>"
             "<li><strong>What each draw funded</strong>, with supporting invoices</li>"
             "<li>The <strong>account trail</strong> from draw to expenditure</li>"
             "<li>Your <strong>entity structure</strong>, since treatment can depend "
             "on how the business is organized</li>"
             "</ul>"
             "<p>Without those, an accountant is guessing, and a guess is not a "
             "position you would want to defend.</p>"),
            ("Do Not Let the Tax Question Drive the Decision",
             "<p>A closing caution, because it is a real pattern.</p>"
             "<p>The treatment of the interest is a second-order consideration next to "
             "the fact that the borrowing is secured by your home. A favorable "
             "treatment does not make an unwise loan wise, and the difference it makes "
             "is small relative to what is at stake if the business does not work "
             "&mdash; see "
             '<a href="../what-happens-to-a-heloc-if-the-business-fails/">what happens '
             "if the business fails</a>.</p>"
             "<p>Decide whether to pledge the house on the merits of the borrowing. "
             "Then ask your CPA how to treat the interest.</p>"
             "<p><strong>This page is general information and does not constitute tax "
             "or legal advice. Axiant Partners is a financing brokerage, not a tax "
             "adviser. Confirm your own position with a qualified CPA before relying "
             "on any treatment described here.</strong></p>"),
        ],
        "faqs": [
            ("Is HELOC interest deductible if I use it for my business?",
             "<strong>This is general information, not tax advice.</strong> The "
             "treatment depends on what the proceeds were used for, how that use is "
             "documented, and your circumstances, so there is no answer that applies "
             "to every reader. IRS Publications 936 and 535 are the primary sources. "
             "<strong>Confirm your position with your CPA.</strong>"),
            ("Does it matter what I spent the money on?",
             "Yes &mdash; use is central. Interest on borrowing is generally "
             "categorised by what the borrowed money funded rather than simply by what "
             "secured it, which is why a single line drawn for several purposes can "
             "have its interest split between categories."),
            ("What is interest tracing?",
             "Following borrowed money from the draw to what it actually paid for. It "
             "is what supports any treatment you claim, and it is far easier when a "
             "draw goes straight into the business account for one purpose than when "
             "it lands in a personal account and is spent from there."),
            ("What records should I keep?",
             "The loan documents, a schedule of draws with dates and amounts, what "
             "each draw funded with supporting invoices, and the account trail from "
             "draw to expenditure. Also tell your accountant as it happens rather than "
             "at year-end."),
            ("Should the tax treatment decide whether I use a HELOC?",
             "No. It is a second-order consideration next to the fact that the "
             "borrowing is secured by your home. A favorable treatment does not make "
             "an unwise loan wise. Decide on the merits of the borrowing, then ask "
             "your CPA how to treat the interest."),
        ],
        "related": [
            ("/heloc-for-business.html", "HELOC for business"),
            ("../what-happens-to-a-heloc-if-the-business-fails/",
             "What happens to a HELOC if the business fails"),
            ("../heloc-vs-cash-out-refinance-for-business-capital/",
             "HELOC vs cash-out refinance"),
            ("../heloc-vs-business-line-of-credit/", "HELOC vs business line of credit"),
        ],
        "sources": [IRS_936, IRS_535, CFPB_HE],
    },
]
