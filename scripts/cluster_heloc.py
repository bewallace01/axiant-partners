# -*- coding: utf-8 -*-
"""HELOC used for business - 5 articles. Asset-equity cluster, 3 of 3.

The tax article carries an explicit "general information, confirm with your
CPA" statement in the quick answer, the body and the FAQ, per the plan. No
figure here is presented as anyone's terms and none is invented. One entity:
Axiant Partners, (561) 268-0465, Boca Raton.
"""

CLUSTER = {
    "pillar": "heloc-for-business.html",
    "hub": "heloc-for-business/articles",
    "crumb": "HELOC for Business",
    "cta_inline": "Compare business funding routes",
    "cta_button": "Get Matched for Business Funding",
    "hub_title": "Using a HELOC for Business: Guides | Axiant Partners",
    "hub_h1": "HELOC for Business Articles",
    "hub_lede": "Funding a business with home equity - what it costs, what it "
                "risks, and where a business product does the job better",
    "hub_desc": "Guides to using home equity for business capital: HELOC versus a "
                "business line of credit, versus a cash-out refinance, what happens "
                "if the business fails, and the personal guarantee question.",
    "hub_intro": "A HELOC is often the cheapest money a small business owner can "
                 "reach, and the only one secured by the house they live in. These "
                 "guides cover how it compares with a business line of credit, what "
                 "the risk actually is, and when a business product is worth its "
                 "higher rate. Start with "
                 "<a href=\"/heloc-for-business.html\">HELOC for business</a>, or "
                 "compare with a "
                 "<a href=\"/business-line-of-credit.html\">business line of credit</a>.",
    "hub_cta_h2": "Weighing home equity against a business facility?",
    "hub_cta_p": "Tell us what the money is for and how long you need it. We will "
                 "show you what the business side can do before you pledge the house.",
}

IRS_936 = ("https://www.irs.gov/publications/p936",
           "IRS Publication 936: Home Mortgage Interest Deduction",
           "The federal rules on when home-secured interest is deductible and how "
           "the use of the proceeds affects it.")
IRS_535 = ("https://www.irs.gov/publications/p535",
           "IRS Guide to Business Expense Resources",
           "Federal guidance on deductible business expenses, including interest "
           "on borrowing used in a trade or business.")
CFPB_HE = ("https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-loan-en-106/",
           "CFPB: What is a home equity loan?",
           "Consumer Financial Protection Bureau explainer on home equity "
           "borrowing, including how draw and repayment periods work.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "cost and terms are presented to borrowers.")
CFPB_MTG = ("https://www.consumerfinance.gov/consumer-tools/mortgages/",
            "CFPB Mortgages",
            "Guidance on mortgage products, the closing process and borrower "
            "protections.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards across consumer and "
         "commercial credit.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms fund themselves, including the use of "
        "personal finances and owner assets.")
FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Guidance on fee disclosure and the warning signs of predatory business "
       "credit.")

ARTICLES = [
    {
        "slug": "heloc-vs-business-line-of-credit",
        "crumb": "HELOC vs Business LOC",
        "title": "HELOC vs Business Line of Credit: Which to Use | Axiant",
        "og_title": "HELOC vs Business Line of Credit: Which to Use",
        "h1": "HELOC vs Business Line of Credit",
        "headline": "HELOC vs Business Line of Credit",
        "lede": "Cheaper money secured on your house, or costlier money that "
                "keeps the house out of it",
        "meta_desc": "HELOC or business line of credit? One is cheaper and secured "
                     "by your home; the other costs more and separates business risk "
                     "from where you live. How to weigh the trade.",
        "article_desc": "How a HELOC and a business line of credit compare on cost, "
                        "access and consequence.",
        "keywords": "heloc vs business line of credit, home equity for business, "
                    "business loc, fund business with home equity",
        "quick_answer": "A <strong>HELOC</strong> is usually cheaper, easier to "
                        "qualify for and secured by your home. A <strong>business "
                        "line of credit</strong> costs more and is harder to get "
                        "early on, but it builds business credit and keeps a business "
                        "failure away from where you live. The rate gap is the price "
                        "of that separation &mdash; sometimes worth paying, sometimes "
                        "not.",
        "sections": [
            ("The Honest Comparison",
             "<p>Most comparisons of these two are written to sell one of them. The "
             "real position is that a HELOC is genuinely cheaper and genuinely "
             "riskier, and both halves of that are true at once.</p>"
             "<p>Cheaper, because it is secured by residential property, which is the "
             "best collateral consumer lending knows. Riskier, because the "
             "consequence of default is your home rather than your company.</p>"
             "<p>Everything else &mdash; qualification, speed, credit building, "
             "flexibility &mdash; sits downstream of that one difference.</p>"),
            ("Side by Side",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>HELOC</th><th>Business line of credit</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Secured by</strong></td>'
             '<td data-label="HELOC">Your home</td>'
             '<td data-label="BLOC">Business assets, or unsecured</td></tr>'
             '<tr><td data-label=""><strong>Rate</strong></td>'
             '<td data-label="HELOC">Lower</td><td data-label="BLOC">Higher</td></tr>'
             '<tr><td data-label=""><strong>Qualifies on</strong></td>'
             '<td data-label="HELOC">Home equity and personal income</td>'
             '<td data-label="BLOC">Business revenue and time trading</td></tr>'
             '<tr><td data-label=""><strong>Builds business credit</strong></td>'
             '<td data-label="HELOC">No</td><td data-label="BLOC">Yes</td></tr>'
             '<tr><td data-label=""><strong>Available to a new business</strong></td>'
             '<td data-label="HELOC">Yes &mdash; it does not look at the business</td>'
             '<td data-label="BLOC">Often not</td></tr>'
             '<tr><td data-label=""><strong>If the business fails</strong></td>'
             '<td data-label="HELOC">Your home is exposed</td>'
             '<td data-label="BLOC">Contained, subject to any guarantee</td></tr>'
             '<tr><td data-label=""><strong>Draw structure</strong></td>'
             '<td data-label="HELOC">Draw period, then repayment period</td>'
             '<td data-label="BLOC">Revolving while in good standing</td></tr>'
             "</tbody></table></div>"),
            ("The Draw Period Is Not Forever",
             "<p>A structural feature of a HELOC that catches business borrowers out: "
             "it has two phases.</p>"
             "<p>During the <strong>draw period</strong> you can borrow and repay "
             "freely, often paying interest only. When it ends, the line closes to new "
             "draws and converts to a <strong>repayment period</strong> where "
             "principal and interest are both due &mdash; and the payment steps up, "
             "sometimes sharply.</p>"
             "<p>A business treating a HELOC as permanent revolving capital can reach "
             "that transition with the balance still outstanding and no facility left "
             "to draw on. The "
             '<a href="https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-loan-en-106/" '
             'rel="noopener nofollow" target="_blank">CFPB explainer</a> sets out how '
             "the two phases work. Know your dates before relying on the line.</p>"),
            ("Qualifying Is a Different Test Entirely",
             "<p>The two products ask completely different questions, and this is why "
             "a HELOC is so often the only option a young business actually has.</p>"
             "<p>A <strong>HELOC</strong> underwrites you: home equity, personal "
             "credit, personal income, and the debt-to-income ratio a mortgage lender "
             "would apply. It does not care whether the business exists. Someone who "
             "left a salaried job last month with equity in a house and a good score "
             "can generally get one.</p>"
             "<p>A <strong>business line of credit</strong> underwrites the company: "
             "time trading, revenue, deposit consistency, and often a minimum period "
             "in business that a new venture cannot satisfy at any price. No amount of "
             "personal strength substitutes for a trading history that does not "
             "exist.</p>"
             "<p>There is a timing consequence worth planning around. If you draw on "
             "personal credit for the first two years, the business reaches year three "
             "with revenue but no credit file of its own, and still cannot qualify. "
             "Opening a modest business facility early &mdash; even one you barely use "
             "&mdash; is what builds the record that replaces the HELOC later.</p>"),
            ("When the HELOC Is the Right Call",
             "<ul>"
             "<li>The business is too new to qualify for a real facility</li>"
             "<li>The need is defined and you can see what repays it</li>"
             "<li>The cost difference is large enough to matter at your scale</li>"
             "<li>You have enough non-home assets that the house is not your whole "
             "safety net</li>"
             "<li>You are bridging to a business facility you can already see</li>"
             "</ul>"
             "<p>For a first-time owner with equity and no trading history, it is "
             "often the only realistic option, and pretending otherwise is not "
             "useful.</p>"),
            ("When to Pay More for the Business Facility",
             "<ul>"
             "<li>The business can qualify &mdash; then the separation is worth "
             "buying</li>"
             "<li>You want business credit history, which the HELOC will never "
             "build</li>"
             "<li>The need is ongoing rather than one-off, so a draw period ending "
             "matters</li>"
             "<li>Your household could not absorb losing the house</li>"
             "<li>There are other people in the house who did not choose the business "
             "risk</li>"
             "</ul>"
             "<p>That last one is not a financial argument and it is often the "
             "deciding one. See "
             '<a href="../what-happens-to-a-heloc-if-the-business-fails/">what happens '
             "if the business fails</a> before deciding, and compare against a real "
             '<a href="/business-line-of-credit.html">business line of credit</a>.</p>'),
        ],
        "faqs": [
            ("Is a HELOC cheaper than a business line of credit?",
             "Usually yes, and often by a wide margin, because it is secured by "
             "residential property. The saving is real; so is the reason for it, which "
             "is that the lender can reach your home if the borrowing goes wrong."),
            ("Can I use a HELOC for business expenses?",
             "Generally yes &mdash; lenders rarely restrict how draws are used. The "
             "constraint is not permission but consequence, since the debt is secured "
             "by your home regardless of what the money funded."),
            ("Does a HELOC build business credit?",
             "No. It is personal borrowing and reports personally, so a business "
             "funded this way can trade for years and still have no credit history of "
             "its own when it needs a facility."),
            ("What is the draw period?",
             "The phase when you can borrow and repay freely, often interest-only. "
             "When it ends the line closes to new draws and converts to a repayment "
             "period covering principal and interest, and the payment can step up "
             "sharply."),
            ("Which should a brand-new business use?",
             "Often the HELOC, because a business without trading history usually "
             "cannot qualify for a real facility. The sensible framing is that it is a "
             "bridge to business credit rather than a permanent arrangement."),
        ],
        "related": [
            ("/heloc-for-business.html", "HELOC for business"),
            ("/business-line-of-credit.html", "Business line of credit"),
            ("../what-happens-to-a-heloc-if-the-business-fails/",
             "What happens to a HELOC if the business fails"),
            ("../personal-guarantee-risk-home-equity-business/",
             "Personal guarantee and home equity risk"),
        ],
        "sources": [CFPB_HE, SBCS, SLOOS],
    },
    {
        "slug": "personal-guarantee-risk-home-equity-business",
        "crumb": "Guarantee and Home Equity Risk",
        "title": "Personal Guarantee vs Home Equity: The Real Risk | Axiant",
        "og_title": "Personal Guarantee vs Home Equity: The Real Risk",
        "h1": "Personal Guarantee and Home Equity Risk",
        "headline": "Personal Guarantee and Home Equity Risk",
        "lede": "Why signing a guarantee and pledging your house are not the "
                "same exposure, however similar they sound",
        "meta_desc": "A personal guarantee and a lien on your home are different "
                     "exposures. What each gives a lender, why the distinction "
                     "matters, and how to think about layering both.",
        "article_desc": "How a personal guarantee differs from pledging home equity, "
                        "and why the distinction matters.",
        "keywords": "personal guarantee business loan, home equity risk business, "
                    "pledging home for business, guarantee vs lien",
        "quick_answer": "A <strong>personal guarantee</strong> is a promise: the "
                        "lender must sue, win, and then find something to enforce "
                        "against. A <strong>lien on your home</strong> is a key: they "
                        "already have a defined route to a defined asset. Both put "
                        "you personally at risk, but only one hands over the house in "
                        "advance &mdash; and owners routinely treat them as "
                        "equivalent when they are not.",
        "sections": [
            ("A Claim Against a Key",
             "<p>The reasoning that leads people wrong runs like this: \"I am "
             "guaranteeing the loan anyway, so the house is already at risk &mdash; I "
             "may as well use the HELOC and get the better rate.\"</p>"
             "<p>The premise is half true and the conclusion does not follow.</p>"
             "<p>Under a <strong>guarantee</strong>, a lender who is not paid has to "
             "sue you, obtain a judgment, and then pursue collection against whatever "
             "they can find and reach. That process is slow, expensive and uncertain, "
             "and homestead protections in some states limit what can be taken at "
             "all.</p>"
             "<p>Under a <strong>lien</strong>, none of that is necessary. They hold "
             "security over a named property and a defined process for realising it. "
             "The difference between those two positions is the difference between a "
             "claim and a key.</p>"),
            ("What Each Gives the Lender",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Personal guarantee</th><th>Lien on your home</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>What it is</strong></td>'
             '<td data-label="PG">A promise to pay if the business does not</td>'
             '<td data-label="Lien">Security over a specific property</td></tr>'
             '<tr><td data-label=""><strong>To enforce</strong></td>'
             '<td data-label="PG">Sue, win, then collect</td>'
             '<td data-label="Lien">A defined foreclosure process</td></tr>'
             '<tr><td data-label=""><strong>Speed</strong></td>'
             '<td data-label="PG">Slow</td><td data-label="Lien">Faster and more certain</td></tr>'
             '<tr><td data-label=""><strong>Certainty</strong></td>'
             '<td data-label="PG">Depends what you own and where</td>'
             '<td data-label="Lien">High &mdash; the asset is identified</td></tr>'
             '<tr><td data-label=""><strong>Effect on pricing</strong></td>'
             '<td data-label="PG">Modest</td><td data-label="Lien">Large</td></tr>'
             "</tbody></table></div>"
             "<p>The pricing column is the tell. If a guarantee and a lien were "
             "equivalent exposures, they would not price so differently.</p>"),
            ("Layering Both Is the Position to Notice",
             "<p>The situation worth flagging is not either instrument. It is holding "
             "several at once without having stepped back to look.</p>"
             "<p>An owner can end up guaranteeing a business line, guaranteeing an "
             "equipment lease, carrying a HELOC drawn for the business, and having "
             "pledged a rental property &mdash; each decision reasonable on its own "
             "day, and collectively a position where a single bad year reaches "
             "everything.</p>"
             "<p>Nobody sets out to build that. It accretes, one sensible decision at "
             "a time. The useful habit is to keep a written list of what is pledged "
             "and what is guaranteed, and to look at it before adding to it.</p>"),
            ("What Can Sometimes Be Negotiated",
             "<p>Guarantees are more negotiable than most borrowers assume, "
             "particularly once a business has a record:</p>"
             "<ul>"
             "<li><strong>A limited guarantee</strong> capped at an amount rather "
             "than unlimited</li>"
             "<li><strong>A burn-off</strong> that reduces or ends once the business "
             "hits agreed milestones</li>"
             "<li><strong>Several rather than joint</strong> liability where there "
             "are multiple owners, so each is liable for a share</li>"
             "<li><strong>Carving out the residence</strong> explicitly</li>"
             "</ul>"
             "<p>None is guaranteed to be offered, and on a new business probably none "
             "will be. But these are ordinary requests rather than unusual ones, and "
             "not asking is the only way to be certain of not getting them. A lien is "
             "far less negotiable &mdash; it is the security itself.</p>"),
            ("A Question Worth Asking Out Loud",
             "<p>Before pledging a residence for business capital, the question is not "
             "whether the plan will work. Everyone signing believes that.</p>"
             "<p>It is: if this does not work, what happens to the people living "
             "here?</p>"
             "<p>If the honest answer is that the household absorbs it and moves on, "
             "the trade may be reasonable. If it is that the family loses their home, "
             "the cheaper rate is not compensation, and a more expensive business "
             "facility is doing something the rate comparison does not capture.</p>"
             "<p><strong>This is general information, not legal advice.</strong> "
             "Guarantees and homestead protections vary considerably by state &mdash; "
             "take advice from an attorney in yours before signing.</p>"),
        ],
        "faqs": [
            ("Is a personal guarantee the same as pledging my house?",
             "No. A guarantee is a promise that requires the lender to sue, win and "
             "then find assets to enforce against. A lien is security over a named "
             "property with a defined process for realising it. Both expose you "
             "personally; only one hands over a specific asset in advance."),
            ("If I am guaranteeing anyway, why not use the HELOC?",
             "Because the two are not equivalent. Under a guarantee the lender faces "
             "a slow, uncertain collection process, and some states limit what can be "
             "reached. A lien removes that uncertainty. The large pricing difference "
             "between them is the market telling you they are not the same risk."),
            ("Can a personal guarantee be negotiated?",
             "More often than borrowers assume, particularly once a business has a "
             "track record &mdash; a cap, a burn-off tied to milestones, several "
             "rather than joint liability among owners, or an explicit carve-out of "
             "the residence. A new business will usually get none of these, but they "
             "are ordinary asks."),
            ("What is the risk of layering several of these?",
             "That a single bad year reaches everything at once. Guarantees and liens "
             "accrete one reasonable decision at a time, and few owners have a written "
             "list of what is pledged and guaranteed. Keeping one, and reading it "
             "before adding, is the practical safeguard."),
            ("Does a homestead exemption protect my house?",
             "Sometimes, partially, and it varies a great deal by state &mdash; and it "
             "generally does not defeat a lien you granted voluntarily. This is "
             "general information, not legal advice; confirm the position in your "
             "state with an attorney."),
        ],
        "related": [
            ("/heloc-for-business.html", "HELOC for business"),
            ("../heloc-vs-business-line-of-credit/", "HELOC vs business line of credit"),
            ("../what-happens-to-a-heloc-if-the-business-fails/",
             "What happens to a HELOC if the business fails"),
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
        ],
        "sources": [CFPB_HE, CFPB, FTC],
    },
]

# Articles 3-5 live in a companion module to keep each file readable.
from cluster_heloc_b import MORE as _B
ARTICLES = ARTICLES + _B
