# -*- coding: utf-8 -*-
"""Equipment appraisal - 5 articles. Plan priority 3.

Ranges are described as conventional across lenders and appraisers, never
quoted as anyone's terms. No funded totals, no years in business, no
testimonials, no invented figures. One entity: Axiant Partners,
(561) 268-0465, Boca Raton.
"""

CLUSTER = {
    "pillar": "equipment-appraisal.html",
    "hub": "equipment-appraisal/articles",
    "crumb": "Equipment Appraisal",
    "cta_inline": "See what your equipment supports",
    "cta_button": "Get Matched Against Your Equipment",
    "hub_title": "Equipment Appraisal Guides | Axiant Partners",
    "hub_h1": "Equipment Appraisal Articles",
    "hub_lede": "What an appraisal actually measures, which value a lender uses, "
                "and how the number becomes a loan amount",
    "hub_desc": "Guides to equipment appraisal for financing: desktop versus "
                "on-site, orderly against forced liquidation value, which "
                "credentials lenders accept, and how value sets loan-to-value.",
    "hub_intro": "An appraisal is not a mechanical inspection. It is a resale "
                 "estimate that decides how much a lender will advance, and the "
                 "basis it is written on matters more than the headline figure. "
                 "These guides cover which value gets used, who is qualified to "
                 "produce it, and how titled vehicles differ from yellow iron. "
                 "Start with <a href=\"/equipment-appraisal.html\">equipment "
                 "appraisal</a>, or see "
                 "<a href=\"/equipment-financing.html\">equipment financing</a>.",
    "hub_cta_h2": "Need to know what your equipment supports?",
    "hub_cta_p": "Tell us what you own, its age and condition, and what is still "
                 "owed. We will tell you plainly what the equity is likely to carry.",
}

IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "The authority on depreciation and Section 179 for business equipment "
           "- book value, which is a different number from market value.")
SBA_504 = ("https://www.sba.gov/funding-programs/loans/504-loans",
           "SBA 504 Loan Program",
           "Federal program terms for fixed-asset lending, where independent "
           "valuation is part of the process.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "terms and costs are presented to borrowers.")
FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Guidance on fee disclosure and the warning signs of predatory business "
       "credit.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards, including how collateral "
         "requirements move with credit conditions.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms apply for and receive credit, including "
        "the role of collateral.")

ARTICLES = [
    {
        "slug": "orderly-vs-forced-liquidation-value",
        "crumb": "Orderly vs Forced Liquidation",
        "title": "Orderly vs Forced Liquidation Value: The Difference | Axiant",
        "og_title": "Orderly vs Forced Liquidation Value: Why It Decides Your Advance",
        "h1": "Orderly vs Forced Liquidation Value",
        "headline": "Orderly vs Forced Liquidation Value",
        "lede": "The distinction that decides your advance rate, and the reason "
                "two appraisals of the same machine disagree",
        "meta_desc": "Orderly and forced liquidation value describe the same "
                     "equipment sold on different timelines. Which basis a lender "
                     "uses decides the advance, and the gap between them is wide.",
        "article_desc": "How the liquidation bases differ and why the one your "
                        "lender uses determines the loan.",
        "keywords": "orderly liquidation value, forced liquidation value, OLV FLV, "
                    "equipment appraisal basis, fair market value equipment",
        "quick_answer": "They are the same equipment sold on different clocks. "
                        "<strong>Orderly liquidation value</strong> assumes a "
                        "reasonable marketing period to find the right buyer; "
                        "<strong>forced liquidation value</strong> assumes it must go "
                        "quickly, usually at auction. FLV is the lower number, often "
                        "considerably, and which basis your lender advances against "
                        "matters more than the appraiser's opinion of the machine.",
        "sections": [
            ("Four Numbers, One Machine",
             "<p>An appraisal report can carry several values for the same asset, and "
             "quoting the wrong one is the most common reason an owner's expectation "
             "and a lender's offer are far apart.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Basis</th><th>Assumes</th><th>Relative level</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Basis">Fair market value</td>'
             '<td data-label="Assumes">Willing buyer and seller, no time pressure, '
             "in continued use</td>"
             '<td data-label="Level">Highest</td></tr>'
             '<tr><td data-label="Basis">Orderly liquidation value (OLV)</td>'
             '<td data-label="Assumes">A sale, but with a reasonable marketing '
             "period</td>"
             '<td data-label="Level">Lower</td></tr>'
             '<tr><td data-label="Basis">Forced liquidation value (FLV)</td>'
             '<td data-label="Assumes">A quick sale, typically auction</td>'
             '<td data-label="Level">Lower again</td></tr>'
             '<tr><td data-label="Basis">Salvage or scrap</td>'
             '<td data-label="Assumes">No longer viable as working equipment</td>'
             '<td data-label="Level">Floor</td></tr>'
             "</tbody></table></div>"
             "<p>The spread between the top and the bottom of that table is not a "
             "rounding difference. On specialised equipment it can be most of the "
             "value.</p>"),
            ("Why Lenders Reach for the Lower Numbers",
             "<p>A lender is not estimating what your machine is worth to you. They "
             "are estimating what they would recover if they had to sell it, in "
             "circumstances where you are not paying and the sale is not leisurely.</p>"
             "<p>That is precisely the definition of a liquidation basis. Fair market "
             "value assumes an unhurried transaction between willing parties, which is "
             "the opposite of a recovery scenario, so it rarely governs a secured "
             "advance even though it is the number owners quote.</p>"
             "<p>Which of OLV or FLV a lender uses depends on the asset and their own "
             "risk posture. Common, liquid equipment with a deep resale market can be "
             "advanced against OLV; specialised or slow-moving equipment tends to be "
             "priced closer to FLV, because that is the realistic outcome.</p>"),
            ("What Widens the Gap",
             "<p>The distance between OLV and FLV is not fixed. It is a proxy for how "
             "hard the asset is to sell:</p>"
             "<ul>"
             "<li><strong>How many buyers exist.</strong> A common skid steer has a "
             "deep market; a bespoke production line has a handful of plausible "
             "buyers worldwide.</li>"
             "<li><strong>How mobile it is.</strong> Equipment that must be "
             "dismantled, rigged and transported loses value to the cost of moving "
             "it.</li>"
             "<li><strong>Whether it is installed.</strong> An asset bolted into a "
             "building is worth less than the same asset on a trailer.</li>"
             "<li><strong>How fast the technology moves.</strong> Where new models "
             "obsolete old ones quickly, a forced sale falls further.</li>"
             "<li><strong>Where it is.</strong> Remote locations narrow the buyer pool "
             "and add freight to any sale.</li>"
             "</ul>"
             "<p>Owners of highly specialised equipment are often surprised by the "
             "advance, and this is why. The machine may be excellent and expensive and "
             "still be difficult to sell quickly, which is the only question the basis "
             "is asking.</p>"),
            ("Book Value Is a Different Question Again",
             "<p>Worth separating clearly, because it causes real confusion.</p>"
             "<p>Book value is an accounting figure &mdash; what you paid, less "
             "depreciation taken under the rules in "
             '<a href="https://www.irs.gov/publications/p946" rel="noopener nofollow" '
             'target="_blank">IRS Publication 946</a>. Equipment expensed aggressively '
             "under Section 179 can carry a very low book value while remaining "
             "genuinely valuable in the market.</p>"
             "<p>The reverse also happens: an asset can sit on the books at a "
             "substantial figure while the resale market for it has collapsed.</p>"
             "<p>Lenders do not advance against book value. It answers a tax question, "
             "not a recovery one.</p>"),
            ("What to Ask Before the Appraisal",
             "<ul>"
             "<li><strong>Which basis will you advance against?</strong> The single "
             "most useful question, and it is rarely volunteered.</li>"
             "<li><strong>What advance rate applies to that basis?</strong> A high "
             "rate on FLV can be worse than a lower rate on OLV.</li>"
             "<li><strong>Will the report include more than one basis?</strong> Most "
             "do, and it is useful to see the spread.</li>"
             "<li><strong>Does installation cost come off?</strong> On fixed plant "
             "the removal cost can be material.</li>"
             "</ul>"
             "<p>Comparing two lenders on advance rate alone is meaningless without "
             "knowing the basis each applies it to. See "
             '<a href="../how-appraisal-value-sets-loan-to-value/">how appraisal value '
             "sets loan-to-value</a> for how the two combine into an actual "
             "number.</p>"),
        ],
        "faqs": [
            ("What is the difference between orderly and forced liquidation value?",
             "The assumed selling time. <strong>Orderly liquidation value</strong> "
             "assumes a reasonable marketing period to find the right buyer; "
             "<strong>forced liquidation value</strong> assumes a quick sale, usually "
             "at auction. FLV is the lower figure, often by a wide margin."),
            ("Which value do lenders use?",
             "A liquidation basis rather than fair market value, because they are "
             "estimating recovery rather than an unhurried sale. Common, liquid "
             "equipment may be advanced against OLV; specialised or slow-moving assets "
             "tend to be priced closer to FLV."),
            ("Why is my specialised equipment valued so low?",
             "Because the basis asks how quickly it could be sold, not how good or "
             "expensive it is. A machine with few plausible buyers, high transport "
             "cost, or installation that must be undone falls a long way on a forced "
             "basis regardless of condition."),
            ("Is book value the same as appraised value?",
             "No. Book value is what you paid less depreciation taken for tax "
             "purposes. Equipment expensed under Section 179 can carry almost no book "
             "value and still be worth a great deal, and the reverse happens too. "
             "Lenders advance against market-based value, not book."),
            ("What should I ask a lender about valuation?",
             "Which basis they advance against, and what advance rate applies to that "
             "basis. A high advance rate on forced liquidation value can produce a "
             "smaller loan than a lower rate on orderly liquidation value, so "
             "comparing rates alone is meaningless."),
        ],
        "related": [
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../how-appraisal-value-sets-loan-to-value/",
             "How appraisal value sets loan-to-value"),
            ("../desktop-vs-onsite-equipment-appraisal/",
             "Desktop vs on-site appraisal"),
            ("/equipment-financing.html", "Equipment financing"),
        ],
        "sources": [IRS_946, SBA_504, SLOOS],
    },
    {
        "slug": "desktop-vs-onsite-equipment-appraisal",
        "crumb": "Desktop vs On-Site",
        "title": "Desktop vs On-Site Equipment Appraisal | Axiant Partners",
        "og_title": "Desktop vs On-Site Equipment Appraisal: Which You Need",
        "h1": "Desktop vs On-Site Equipment Appraisal",
        "headline": "Desktop vs On-Site Equipment Appraisal",
        "lede": "One is faster and cheaper and assumes the worst; the other "
                "costs more and can prove you right",
        "meta_desc": "Desktop appraisals are built from records and photographs and "
                     "run conservative. On-site inspections cost more and take longer "
                     "but let above-average equipment beat the assumption.",
        "article_desc": "When a desktop equipment appraisal is enough and when an "
                        "on-site inspection pays for itself.",
        "keywords": "desktop appraisal equipment, on-site equipment inspection, "
                    "equipment valuation types, appraisal cost equipment",
        "quick_answer": "A <strong>desktop</strong> appraisal is built from the "
                        "serial number, specification, hours and photographs, with no "
                        "one attending. It is faster and cheaper and, because "
                        "condition is assumed rather than seen, "
                        "<strong>conservative</strong>. An <strong>on-site</strong> "
                        "inspection costs more and takes longer, and is worth it when "
                        "your equipment is genuinely better than average for its age.",
        "sections": [
            ("The Trade in One Sentence",
             "<p>A desktop valuation assumes typical condition. An on-site inspection "
             "observes actual condition.</p>"
             "<p>If your equipment is typical, those produce nearly the same number "
             "and the desktop saves you time and money. If your equipment is "
             "meaningfully better than typical &mdash; low hours, documented major "
             "work, careful storage &mdash; the desktop cannot know that and prices as "
             "though it were not true.</p>"
             "<p>So the decision is not really about cost. It is about whether you "
             "have something to prove.</p>"),
            ("How They Compare",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Desktop</th><th>On-site</th></tr></thead><tbody>"
             '<tr><td data-label=""><strong>Built from</strong></td>'
             '<td data-label="Desk">Serial, spec, hours, photographs, comparable '
             "sales</td>"
             '<td data-label="Site">A physical inspection, plus all of that</td></tr>'
             '<tr><td data-label=""><strong>Turnaround</strong></td>'
             '<td data-label="Desk">Fast</td>'
             '<td data-label="Site">Slower &mdash; scheduling plus travel</td></tr>'
             '<tr><td data-label=""><strong>Cost</strong></td>'
             '<td data-label="Desk">Lower</td><td data-label="Site">Higher</td></tr>'
             '<tr><td data-label=""><strong>Condition</strong></td>'
             '<td data-label="Desk">Assumed typical</td>'
             '<td data-label="Site">Observed and recorded</td></tr>'
             '<tr><td data-label=""><strong>Bias</strong></td>'
             '<td data-label="Desk">Conservative</td>'
             '<td data-label="Site">Reflects what is actually there</td></tr>'
             '<tr><td data-label=""><strong>Suits</strong></td>'
             '<td data-label="Desk">Common, liquid, average-condition assets</td>'
             '<td data-label="Site">Large, specialised, or better-than-average '
             "assets</td></tr>"
             "</tbody></table></div>"),
            ("When the Desktop Is Enough",
             "<ul>"
             "<li>The equipment is a common model with an active resale market</li>"
             "<li>Age and hours are unremarkable for the type</li>"
             "<li>The loan is modest relative to the cost of an inspection</li>"
             "<li>Speed matters &mdash; a desktop can turn round in a fraction of the "
             "time</li>"
             "<li>You are sizing a deal rather than closing one, and want an "
             "indication</li>"
             "</ul>"
             "<p>For a five-year-old skid steer with average hours, an inspector is "
             "unlikely to find anything the comparable sales did not already imply. "
             "Paying for one buys very little.</p>"),
            ("When the Inspection Pays for Itself",
             "<ul>"
             "<li><strong>The equipment is better than its age suggests</strong> "
             "&mdash; low hours, indoor storage, a documented rebuild</li>"
             "<li><strong>It is specialised</strong>, so comparable sales are thin and "
             "a desktop has little to work from</li>"
             "<li><strong>The loan is large</strong>, and a percentage improvement in "
             "the valuation is worth more than the fee</li>"
             "<li><strong>Several units are involved</strong>, where one visit covers "
             "the fleet</li>"
             "<li><strong>The desktop came back low</strong> and you believe it is "
             "wrong</li>"
             "</ul>"
             "<p>That last case is the most common reason to escalate. A desktop "
             "figure is an opinion formed without seeing the asset; an inspection is "
             "the evidence that rebuts it. Disagreement alone moves nothing &mdash; "
             "evidence does.</p>"),
            ("How Long Each Takes, and Why It Matters",
             "<p>Turnaround is the other axis, and on a time-sensitive deal it can "
             "decide the choice regardless of accuracy.</p>"
             "<p>A desktop valuation is largely research: pull the comparables, read "
             "the photographs, write it up. The constraint is the appraiser's queue "
             "rather than logistics, so it moves quickly once instructed.</p>"
             "<p>An on-site inspection adds scheduling, travel and a site visit that "
             "has to fit around your operation as well as theirs. Equipment in daily "
             "use, spread across sites, or in a remote location adds days before "
             "anyone has looked at anything &mdash; and if a machine is out on a job "
             "when the inspector arrives, it adds a return trip.</p>"
             "<p>Two practical consequences. If the equipment is working, coordinate "
             "the visit around a day it will actually be on the yard. And if a "
             "deadline is genuinely tight, ask whether the lender will proceed on a "
             "desktop figure and treat an inspection as a condition afterwards &mdash; "
             "some will, at a more conservative advance.</p>"),
            ("Making Either One Land Well",
             "<p>You have more influence over a desktop valuation than most owners "
             "realise, because you supply most of its inputs.</p>"
             "<ul>"
             "<li><strong>Photograph properly.</strong> Clean, well lit, every angle, "
             "plus the data plate and the hour meter. Poor photographs produce "
             "conservative numbers.</li>"
             "<li><strong>Send the service file</strong> without being asked. "
             "Documented work you cannot evidence counts as work that did not "
             "happen.</li>"
             "<li><strong>Give exact identifiers</strong> &mdash; serial number, model "
             "and year. Approximations get valued as the weaker interpretation.</li>"
             "<li><strong>Disclose the flaws.</strong> An appraiser who finds "
             "something undisclosed discounts everything else you said.</li>"
             "<li><strong>Fix the cheap things</strong> before an on-site visit. "
             "Warning lights and leaks read as deferred maintenance across the whole "
             "machine.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("What is a desktop equipment appraisal?",
             "A valuation produced without attending &mdash; built from the serial "
             "number, specification, hours, photographs and comparable sales. It is "
             "faster and cheaper, and conservative, because condition is assumed "
             "rather than observed."),
            ("Is an on-site appraisal worth the extra cost?",
             "When your equipment is genuinely better than average for its age, when "
             "it is specialised enough that comparable sales are thin, or when the "
             "loan is large enough that a percentage improvement exceeds the fee. For "
             "an average machine on a modest loan, usually not."),
            ("Why did my desktop appraisal come back low?",
             "Because it assumes typical condition, and typical is not generous. Poor "
             "photographs, missing service history or approximate identifiers all push "
             "it further down, since the appraiser resolves uncertainty conservatively."),
            ("Can I challenge a desktop valuation?",
             "With evidence, yes &mdash; comparable sold units of the same model and "
             "specification, documented major work, or an on-site inspection. "
             "Disagreement on its own does not move a valuation; evidence does."),
            ("What should I send for a desktop appraisal?",
             "Clean, well-lit photographs from every angle including the data plate "
             "and hour meter, the exact serial, model and year, and the service file. "
             "Disclose known faults &mdash; an appraiser who finds something "
             "undisclosed discounts the rest of what you said."),
        ],
        "related": [
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../orderly-vs-forced-liquidation-value/",
             "Orderly vs forced liquidation value"),
            ("../who-can-appraise-business-equipment/",
             "Who can appraise business equipment"),
            ("/commercial-truck-title-loan/articles/what-a-truck-appraiser-looks-for/",
             "What a truck appraiser looks for"),
        ],
        "sources": [SBA_504, CFPB, SBCS],
    },
]

# Articles 3-5 live in a companion module to keep each file readable.
from cluster_equip_appraisal_b import MORE as _B
ARTICLES = ARTICLES + _B
