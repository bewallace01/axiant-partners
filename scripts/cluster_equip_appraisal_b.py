# -*- coding: utf-8 -*-
"""Equipment appraisal, articles 3-5."""
from cluster_equip_appraisal import (IRS_946, SBA_504, CFPB, FTC, SLOOS, SBCS)

ASA = ("https://www.appraisers.org/",
       "American Society of Appraisers",
       "A professional body issuing machinery and equipment appraisal "
       "credentials and publishing the standards members work to.")
TAF = ("https://appraisalfoundation.org/",
       "The Appraisal Foundation",
       "The body behind USPAP, the uniform standards most lender-accepted "
       "appraisal work in the United States is written to.")

MORE = [
    {
        "slug": "who-can-appraise-business-equipment",
        "crumb": "Who Can Appraise",
        "title": "Who Can Appraise Business Equipment? | Axiant Partners",
        "og_title": "Who Can Appraise Business Equipment, and Which Credentials Count",
        "h1": "Who Can Appraise Business Equipment?",
        "headline": "Who Can Appraise Business Equipment",
        "lede": "Which credentials lenders accept, why a dealer quote is not an "
                "appraisal, and who chooses the appraiser",
        "meta_desc": "Not every valuation counts. Which appraisal credentials "
                     "lenders accept, why USPAP matters, and why a dealer's offer or "
                     "a price guide printout is not an appraisal.",
        "article_desc": "Which equipment appraisal credentials lenders accept and "
                        "why independence matters.",
        "keywords": "equipment appraiser credentials, USPAP appraisal, certified "
                    "machinery appraiser, who appraises equipment",
        "quick_answer": "Lenders want an <strong>independent, credentialed</strong> "
                        "appraiser working to recognised standards &mdash; in the "
                        "United States that usually means work written to "
                        "<strong>USPAP</strong>, from someone holding a machinery and "
                        "equipment credential. A dealer's trade-in offer, a price "
                        "guide printout and your own estimate are all useful "
                        "information and none of them is an appraisal.",
        "sections": [
            ("Independence Is the Point",
             "<p>The reason a lender will not accept a dealer's number is not that it "
             "is wrong. It is that the person producing it has a position.</p>"
             "<p>A dealer quoting a trade-in is quoting what they would pay, which is "
             "a bid, not a valuation. A seller's asking price is an aspiration. Your "
             "own figure, however well informed, is the borrower's opinion of the "
             "borrower's collateral.</p>"
             "<p>An appraisal is a documented opinion from someone with no interest in "
             "the transaction, produced to a standard, with the reasoning written "
             "down. That is what makes it usable as the basis for lending, and it is "
             "why lenders often instruct the appraiser directly rather than accepting "
             "one you commissioned.</p>"),
            ("What Lenders Look For",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Element</th><th>Why it matters</th></tr></thead><tbody>"
             '<tr><td data-label="Element">USPAP compliance</td>'
             '<td data-label="Why">The uniform standards most lender-accepted work in '
             "the US is written to</td></tr>"
             '<tr><td data-label="Element">Machinery and equipment credential</td>'
             '<td data-label="Why">A specialism &mdash; real estate credentials do not '
             "transfer</td></tr>"
             '<tr><td data-label="Element">Independence</td>'
             '<td data-label="Why">No interest in the sale, the loan or the '
             "equipment</td></tr>"
             '<tr><td data-label="Element">Relevant experience</td>'
             '<td data-label="Why">Yellow iron, machine tools and medical imaging are '
             "different markets</td></tr>"
             '<tr><td data-label="Element">A stated basis</td>'
             '<td data-label="Why">The report must say which value it is reporting</td></tr>'
             '<tr><td data-label="Element">Professional indemnity cover</td>'
             '<td data-label="Why">Often required before a lender will rely on the '
             "work</td></tr>"
             "</tbody></table></div>"
             '<p><a href="https://appraisalfoundation.org/" rel="noopener nofollow" '
             'target="_blank">The Appraisal Foundation</a> publishes USPAP, and '
             '<a href="https://www.appraisers.org/" rel="noopener nofollow" '
             'target="_blank">the American Society of Appraisers</a> is one of the '
             "bodies issuing machinery and equipment credentials.</p>"),
            ("What a Real Report Contains",
             "<p>You can judge quality without being an appraiser. A usable report "
             "shows its working:</p>"
             "<ul>"
             "<li><strong>The basis, named explicitly</strong> &mdash; fair market, "
             "orderly liquidation, forced liquidation. A report that does not say is "
             "not usable; see "
             '<a href="../orderly-vs-forced-liquidation-value/">orderly versus forced '
             "liquidation value</a>.</li>"
             "<li><strong>The effective date.</strong> Values move; an undated opinion "
             "is worthless.</li>"
             "<li><strong>Identification</strong> &mdash; serial numbers, models, "
             "years, hours.</li>"
             "<li><strong>Method and comparables</strong>, so the number can be "
             "followed rather than taken on trust.</li>"
             "<li><strong>Scope</strong> &mdash; whether it was a desktop or an "
             "inspection, and what was assumed.</li>"
             "<li><strong>Signature and credentials</strong>, with a statement of "
             "independence.</li>"
             "</ul>"
             "<p>A number on letterhead with none of that is a quote wearing a "
             "costume.</p>"),
            ("Who Instructs the Appraiser",
             "<p>Usually the lender, and there is a reason worth understanding.</p>"
             "<p>An appraisal commissioned by the borrower creates an obvious "
             "incentive question, however scrupulous the appraiser. Many lenders "
             "therefore instruct from their own panel, or will accept an existing "
             "report only if the appraiser agrees to address it to them &mdash; which "
             "makes the lender the client and the appraiser answerable to them.</p>"
             "<p>The practical consequence: if you commission your own appraisal "
             "before approaching a lender, expect that it may be informative rather "
             "than decisive. It is often still worth having for your own planning, but "
             "do not assume the lender will simply adopt it.</p>"),
            ("Where the Cost Falls",
             "<p>Appraisal cost scales with effort rather than with the value of the "
             "asset &mdash; scope, travel, number of units and how obscure the "
             "equipment is. A single common machine assessed from records sits at one "
             "end; a multi-site inspection of specialised plant sits at the other.</p>"
             "<p>Two things worth establishing before instructing:</p>"
             "<ul>"
             "<li><strong>Who pays</strong>, and whether it is due regardless of "
             "whether the loan completes. It usually is &mdash; the appraiser did the "
             "work either way.</li>"
             "<li><strong>Whether the report is portable</strong> if you end up with a "
             "different lender. Sometimes it can be re-addressed; sometimes it cannot, "
             "and that is worth knowing before you pay for it twice.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("Can a dealer's quote be used as an appraisal?",
             "No. A dealer quoting a trade-in is stating what they would pay, which is "
             "a bid rather than an independent valuation. Lenders want a documented "
             "opinion from someone with no interest in the transaction."),
            ("What is USPAP?",
             "The Uniform Standards of Professional Appraisal Practice, published by "
             "The Appraisal Foundation. Most lender-accepted appraisal work in the "
             "United States is written to it, and a report stating USPAP compliance "
             "tells a lender what standard it was produced under."),
            ("Does a real estate appraiser qualify to value equipment?",
             "Generally not. Machinery and equipment appraisal is a separate "
             "specialism with its own credentials, and within it the markets differ "
             "&mdash; construction equipment, machine tools and medical imaging are "
             "not interchangeable expertise."),
            ("Can I use an appraisal I paid for myself?",
             "Sometimes, but do not count on it. Many lenders instruct from their own "
             "panel, or will accept an existing report only if it is re-addressed to "
             "them so they become the client. Your own appraisal is often informative "
             "rather than decisive."),
            ("What makes a report unusable?",
             "Most often, not naming the basis. A figure that does not say whether it "
             "is fair market, orderly liquidation or forced liquidation value cannot be "
             "lent against. An undated opinion, or one with no method or comparables "
             "shown, has the same problem."),
        ],
        "related": [
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../orderly-vs-forced-liquidation-value/",
             "Orderly vs forced liquidation value"),
            ("../desktop-vs-onsite-equipment-appraisal/",
             "Desktop vs on-site appraisal"),
            ("../how-appraisal-value-sets-loan-to-value/",
             "How appraisal value sets loan-to-value"),
        ],
        "sources": [TAF, ASA, SBA_504],
    },
    {
        "slug": "how-appraisal-value-sets-loan-to-value",
        "crumb": "Value to Loan Amount",
        "title": "How Appraisal Value Sets Loan-to-Value | Axiant Partners",
        "og_title": "How Appraisal Value Becomes a Loan Amount",
        "h1": "How Appraisal Value Sets Loan-to-Value",
        "headline": "How Appraisal Value Sets Loan-to-Value",
        "lede": "From a valuation to money in the account - the arithmetic, and "
                "the deductions people forget",
        "meta_desc": "How an equipment appraisal becomes a loan amount: the basis, "
                     "the advance rate, existing liens and costs. Why the same "
                     "advance rate can mean very different money.",
        "article_desc": "The arithmetic that turns an equipment valuation into an "
                        "actual advance.",
        "keywords": "equipment loan to value, advance rate equipment, LTV equipment "
                    "financing, how much can I borrow equipment",
        "quick_answer": "<strong>Value &times; advance rate, minus what is owed, "
                        "minus costs.</strong> The trap is that the advance rate is "
                        "meaningless without knowing which value it applies to &mdash; "
                        "a high rate against forced liquidation value can produce less "
                        "money than a lower rate against orderly liquidation value. "
                        "Always compare the resulting dollars, not the percentage.",
        "sections": [
            ("The Arithmetic",
             "<p>Four steps, in order, and each one reduces the number:</p>"
             "<ul>"
             "<li><strong>Start with the appraised value</strong> on whichever basis "
             "the lender uses</li>"
             "<li><strong>Apply the advance rate</strong> &mdash; a percentage, never "
             "the whole value</li>"
             "<li><strong>Subtract existing liens</strong> at their exact payoff "
             "figures</li>"
             "<li><strong>Subtract costs</strong> &mdash; appraisal, filing, "
             "documentation</li>"
             "</ul>"
             "<p>What remains is what reaches your account. Owners generally do the "
             "first two steps and are surprised by the last two, which is where the "
             "gap between expectation and offer usually sits.</p>"),
            ("Why the Percentage Alone Tells You Nothing",
             "<p>This is the point of the whole article. Consider the same machine at "
             "two lenders:</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Lender A</th><th>Lender B</th></tr></thead><tbody>"
             '<tr><td data-label=""><strong>Basis used</strong></td>'
             '<td data-label="A">Forced liquidation value</td>'
             '<td data-label="B">Orderly liquidation value</td></tr>'
             '<tr><td data-label=""><strong>Value on that basis</strong></td>'
             '<td data-label="A">$40,000</td><td data-label="B">$60,000</td></tr>'
             '<tr><td data-label=""><strong>Advance rate quoted</strong></td>'
             '<td data-label="A">80%</td><td data-label="B">65%</td></tr>'
             '<tr><td data-label=""><strong>Advance</strong></td>'
             '<td data-label="A"><strong>$32,000</strong></td>'
             '<td data-label="B"><strong>$39,000</strong></td></tr>'
             "</tbody></table></div>"
             "<p>Illustrative arithmetic, not a quote. Lender A advertises the higher "
             "percentage and lends less money. If you shop on advance rate you will "
             "pick the worse offer, and the paperwork will look like you got the "
             "better one.</p>"
             "<p>Ask both questions together: which basis, and what rate against it. "
             "See <a href=\"../orderly-vs-forced-liquidation-value/\">orderly versus "
             "forced liquidation value</a>.</p>"),
            ("What Moves the Advance Rate",
             "<p>Once the basis is fixed, the percentage still varies:</p>"
             "<ul>"
             "<li><strong>How liquid the equipment is.</strong> A deep resale market "
             "supports a higher rate.</li>"
             "<li><strong>Whether it is titled.</strong> Titled assets are easier to "
             "secure and recover; see "
             '<a href="../appraising-titled-vehicles-vs-yellow-iron/">titled vehicles '
             "versus yellow iron</a>.</li>"
             "<li><strong>Age and remaining life.</strong> Equipment near the end of "
             "its useful life gets a thinner rate whatever its current value.</li>"
             "<li><strong>Whether it is installed or mobile.</strong> Removal cost "
             "comes out of any recovery.</li>"
             "<li><strong>Your credit and trading history.</strong> Secondary to the "
             "asset here, but not absent.</li>"
             "</ul>"),
            ("The Deductions People Forget",
             "<p>Two reliably produce an unpleasant surprise late in the process.</p>"
             "<p><strong>Existing liens</strong> come off at the payoff figure, not "
             "the balance on your last statement. A payoff includes interest to the "
             "payoff date and any early-settlement charge, and it is always the larger "
             "number. Get it in writing at the start.</p>"
             "<p><strong>Costs</strong> &mdash; the appraisal itself, UCC filing, "
             "documentation fees &mdash; are usually deducted from proceeds rather "
             "than invoiced. On a small advance they matter proportionally more, and "
             "on a very small one they can make the transaction not worth doing.</p>"),
            ("Where an Appraisal Sits Against the Purchase Price",
             "<p>A specific case worth separating out, because it trips up people "
             "buying rather than borrowing against equipment they own.</p>"
             "<p>When the loan funds a purchase, lenders generally advance against "
             "<strong>the lower of the appraised value and the purchase price</strong>. "
             "Paying above market does not increase what they will lend &mdash; the "
             "excess is simply more deposit from you.</p>"
             "<p>Buying below market does not automatically help either. Many lenders "
             "cap against the price actually paid on a recent purchase, on the "
             "reasoning that an arm's-length transaction is itself the best evidence "
             "of value. That is the same logic as the seasoning rules on property, and "
             "it is why a bargain purchase often cannot be borrowed against at its "
             "appraised value straight away.</p>"
             "<p>If you are buying well and expect to finance the difference, ask "
             "about that cap before committing, not after.</p>"),
            ("Working It Out Before You Apply",
             "<p>You can approximate the outcome without an appraisal, and it is worth "
             "doing before anyone incurs a fee:</p>"
             "<ul>"
             "<li>Find <strong>sold</strong> comparables for the same model and "
             "specification, not asking prices</li>"
             "<li>Assume a liquidation basis rather than what you would hope to "
             "achieve in an unhurried private sale</li>"
             "<li>Apply a conservative advance rate</li>"
             "<li>Subtract the written payoff on anything owed</li>"
             "<li>Subtract a realistic allowance for costs</li>"
             "</ul>"
             "<p>If the result is not worth the cost of the money, that is much better "
             "to discover now than after an inspection has been booked and paid "
             "for.</p>"),
        ],
        "faqs": [
            ("How is an equipment loan amount calculated?",
             "Appraised value on the lender's chosen basis, multiplied by the advance "
             "rate, less the payoff on any existing lien, less costs. Each step reduces "
             "the figure, and the last two are the ones borrowers most often leave "
             "out."),
            ("Is a higher advance rate always better?",
             "No, and this is the most useful thing to know. A high rate against forced "
             "liquidation value can yield less money than a lower rate against orderly "
             "liquidation value. Compare the resulting dollars rather than the "
             "percentages."),
            ("Why is the payoff higher than my balance?",
             "A payoff figure includes interest to the payoff date and any "
             "early-settlement or prepayment charge, so it is always larger than the "
             "balance on a statement. Ask the existing lienholder for it in writing at "
             "the start."),
            ("Are appraisal costs taken out of the proceeds?",
             "Usually, along with filing and documentation fees, rather than invoiced "
             "separately. On a small advance those costs matter proportionally more "
             "and can make the transaction not worth completing."),
            ("What advance rate should I expect?",
             "It depends on the basis first, then on how liquid the equipment is, "
             "whether it is titled, how much useful life remains, and whether it is "
             "installed or mobile. Any rate quoted without naming the basis it applies "
             "to is not comparable to another lender's."),
        ],
        "related": [
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../orderly-vs-forced-liquidation-value/",
             "Orderly vs forced liquidation value"),
            ("../appraising-titled-vehicles-vs-yellow-iron/",
             "Titled vehicles vs yellow iron"),
            ("/equipment-financing.html", "Equipment financing"),
        ],
        "sources": [SBA_504, SLOOS, CFPB],
    },
    {
        "slug": "appraising-titled-vehicles-vs-yellow-iron",
        "crumb": "Titled Vehicles vs Yellow Iron",
        "title": "Appraising Titled Vehicles vs Yellow Iron | Axiant Partners",
        "og_title": "Appraising Titled Vehicles vs Yellow Iron: Why They Differ",
        "h1": "Appraising Titled Vehicles vs Yellow Iron",
        "headline": "Appraising Titled Vehicles vs Yellow Iron",
        "lede": "Why a truck and an excavator of the same value do not support "
                "the same loan",
        "meta_desc": "Titled vehicles and untitled heavy equipment are appraised and "
                     "secured differently. How title, serial numbers and UCC filings "
                     "change the advance on assets of equal value.",
        "article_desc": "How titled and untitled equipment differ in appraisal, "
                        "security and advance rate.",
        "keywords": "titled vehicle vs equipment, yellow iron appraisal, UCC filing "
                    "equipment, serial number collateral",
        "quick_answer": "A <strong>titled</strong> asset carries a government record "
                        "of ownership, and a lender's interest is recorded on it. "
                        "<strong>Yellow iron</strong> is identified by serial number "
                        "and secured by a <strong>UCC filing</strong> instead. Titled "
                        "assets are easier to verify and recover, which usually shows "
                        "up as a better advance on an asset of the same value.",
        "sections": [
            ("Two Different Ways of Proving Ownership",
             "<p>The distinction is administrative rather than mechanical, and it "
             "matters more to a lender than the machinery does.</p>"
             "<p><strong>Titled</strong> assets &mdash; over-the-road trucks, "
             "trailers, some larger vehicles &mdash; have a state-issued title naming "
             "the owner. A lender records its lien directly on that title, so "
             "ownership and encumbrance are matters of public record and a search is "
             "definitive.</p>"
             "<p><strong>Yellow iron</strong> &mdash; excavators, dozers, loaders, "
             "most plant &mdash; usually has no title. It is identified by "
             "manufacturer serial number, and a lender perfects its interest by filing "
             "a UCC financing statement instead.</p>"
             "<p>Both work. They are not equally strong.</p>"),
            ("What Changes for the Lender",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Titled vehicle</th><th>Yellow iron</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Ownership proof</strong></td>'
             '<td data-label="Titled">State title</td>'
             '<td data-label="Iron">Invoice, serial number, possession</td></tr>'
             '<tr><td data-label=""><strong>Lien recorded</strong></td>'
             '<td data-label="Titled">On the title itself</td>'
             '<td data-label="Iron">UCC financing statement</td></tr>'
             '<tr><td data-label=""><strong>Verifying prior liens</strong></td>'
             '<td data-label="Titled">Definitive</td>'
             '<td data-label="Iron">A UCC search, and blanket filings complicate '
             "it</td></tr>"
             '<tr><td data-label=""><strong>Locating the asset</strong></td>'
             '<td data-label="Titled">Registered, roadgoing</td>'
             '<td data-label="Iron">Moves between sites; no registration trail</td></tr>'
             '<tr><td data-label=""><strong>Resale market</strong></td>'
             '<td data-label="Titled">Broad and well indexed</td>'
             '<td data-label="Iron">Auction-led, more variable</td></tr>'
             '<tr><td data-label=""><strong>Typical advance</strong></td>'
             '<td data-label="Titled">Generally better</td>'
             '<td data-label="Iron">Generally more conservative</td></tr>'
             "</tbody></table></div>"),
            ("The Blanket Filing Problem",
             "<p>The specific complication on untitled equipment, and the one most "
             "worth knowing about.</p>"
             "<p>A UCC financing statement can be written narrowly against named "
             "serial numbers, or broadly as a blanket filing against all equipment a "
             "business owns, now and in future. Blanket filings are common &mdash; "
             "working capital lenders and advance funders take them routinely.</p>"
             "<p>The consequence: a machine you own outright may already be captured "
             "by a blanket filing from an unrelated facility, and a new lender "
             "searching UCC records will see it. That does not always stop the deal, "
             "but it usually requires a subordination or a partial release from the "
             "existing filer, which takes time and their cooperation.</p>"
             "<p>Run a UCC search on your own business before applying. Owners are "
             "regularly surprised by what is on record.</p>"),
            ("Serial Numbers Do the Work That Titles Would",
             "<p>Without a title, the serial number is the asset's identity, and "
             "sloppiness with it causes real problems.</p>"
             "<ul>"
             "<li><strong>Record it exactly</strong> from the data plate, not from an "
             "invoice that may contain a typographical error.</li>"
             "<li><strong>Photograph the plate</strong> as part of any appraisal "
             "submission.</li>"
             "<li><strong>Check it matches</strong> your purchase documents, insurance "
             "schedule and any existing filings. A mismatch between them is a delay "
             "every time.</li>"
             "<li><strong>Note attachments separately.</strong> Buckets, hammers and "
             "couplers may carry their own numbers and may or may not be included in "
             "the collateral.</li>"
             "</ul>"
             "<p>A filing against a wrong serial number may not perfect against the "
             "asset you meant, which is a problem for the lender and therefore for "
             "you.</p>"),
            ("What This Means in Practice",
             "<p>If you own both kinds, the titled assets will usually support the "
             "better terms, and pledging them first is often the cheaper route to the "
             "same money &mdash; see "
             '<a href="/commercial-truck-title-loan.html">commercial truck title '
             "loans</a>.</p>"
             "<p>If your equipment is untitled, three things make the file "
             "straightforward: an accurate serial number list, a clean UCC search or a "
             "known plan to deal with what it shows, and photographs that match the "
             "records. Sorting those before applying removes most of the friction "
             "from the process.</p>"
             "<p>Then the arithmetic is the same for both &mdash; see "
             '<a href="../how-appraisal-value-sets-loan-to-value/">how appraisal value '
             "sets loan-to-value</a>.</p>"),
        ],
        "faqs": [
            ("Why do titled vehicles get better advance rates?",
             "Because ownership and encumbrance are a matter of public record on the "
             "title, and the asset is registered and roadgoing. That makes verification "
             "definitive and recovery more straightforward, both of which reduce the "
             "lender's risk on an asset of the same value."),
            ("How is untitled equipment secured?",
             "By a UCC financing statement filed against the business, identifying the "
             "equipment by manufacturer serial number. There is no title to record a "
             "lien on, so the filing is what perfects the lender's interest."),
            ("What is a blanket UCC filing?",
             "A filing covering all equipment a business owns, now and in future, "
             "rather than named serial numbers. They are common from working capital "
             "lenders and advance funders, and they can capture machinery you own "
             "outright &mdash; which a new lender will see on a search."),
            ("Should I run a UCC search on my own business?",
             "Yes, before applying. Owners are regularly surprised by what is on "
             "record, and finding a blanket filing early gives you time to arrange a "
             "subordination or partial release rather than discovering it mid-deal."),
            ("Do attachments count as part of the collateral?",
             "Not automatically. Buckets, hammers, couplers and similar may carry their "
             "own serial numbers and may or may not be included. List them explicitly "
             "rather than assuming they travel with the machine."),
        ],
        "related": [
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../how-appraisal-value-sets-loan-to-value/",
             "How appraisal value sets loan-to-value"),
            ("../orderly-vs-forced-liquidation-value/",
             "Orderly vs forced liquidation value"),
        ],
        "sources": [SBA_504, FTC, IRS_946],
    },
]
