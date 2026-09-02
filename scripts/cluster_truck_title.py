# -*- coding: utf-8 -*-
"""Commercial truck title loans - 8 articles. Asset-equity cluster, part 1 of 3.

Ranges are described as conventional across lenders, never quoted as anyone's
terms. No funded totals, no years in business, no testimonials, no named lender
rates. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
"""

CLUSTER = {
    "pillar": "commercial-truck-title-loan.html",
    "hub": "commercial-truck-title-loan/articles",
    "crumb": "Commercial Truck Title Loans",
    "cta_inline": "Get matched against your truck's equity",
    "cta_button": "Get Matched for a Truck Title Loan",
    "hub_title": "Commercial Truck Title Loan Guides | Axiant Partners",
    "hub_h1": "Commercial Truck Title Loan Articles",
    "hub_lede": "Borrowing against a truck you already own - what it is worth, "
                "what the lender checks, and what happens if you fall behind",
    "hub_desc": "Guides to borrowing against equity in a truck you already own: "
                "valuation, existing liens, owner-operator versus fleet terms, "
                "default consequences, and how title lending compares to an advance.",
    "hub_intro": "A title loan turns equity you already own into working capital "
                 "without selling the truck or waiting on a receivable. These guides "
                 "cover what a truck is worth to a lender, what an existing lien "
                 "does to the deal, and where title lending is the wrong tool. Start "
                 "with <a href=\"/commercial-truck-title-loan.html\">commercial truck "
                 "title loans</a>, or see <a href=\"/equipment-appraisal.html\">how "
                 "equipment is appraised</a>.",
    "hub_cta_h2": "Own the truck outright, or close to it?",
    "hub_cta_p": "Send the VIN, the mileage and what is still owed. We will tell you "
                 "plainly what the equity supports.",
}

FMCSA = ("https://www.fmcsa.dot.gov/registration/commercial-drivers-license",
         "FMCSA Commercial Driver Licensing",
         "Federal registration and licensing rules for commercial motor vehicles "
         "- the framework a titled commercial asset sits inside.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "The authority on Section 179 and depreciation for business vehicles, "
           "which is what determines a truck's book value against its market value.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "cost is presented to borrowers.")
FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Federal Trade Commission guidance on fee disclosure, collection practice "
       "and the warning signs of predatory business credit.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms apply for and receive credit, including "
        "approval rates and funding speed by product.")
BTS = ("https://www.bts.gov/",
       "Bureau of Transportation Statistics",
       "Federal freight and trucking data - the public record behind claims "
       "about rates, volumes and utilization.")

ARTICLES = [
    {
        "slug": "how-much-can-you-borrow-against-a-semi",
        "crumb": "How Much Can You Borrow",
        "title": "How Much Can You Borrow Against a Semi Truck? | Axiant",
        "og_title": "How Much Can You Borrow Against a Semi Truck?",
        "h1": "How Much Can You Borrow Against a Semi Truck?",
        "headline": "How Much Can You Borrow Against a Semi Truck",
        "lede": "What a lender will advance against a truck you already own, "
                "and the four things that move the number",
        "meta_desc": "Truck title loans advance a percentage of the truck's "
                     "wholesale value, not what you paid or what it is listed at. "
                     "See how advance rates work and what moves them.",
        "article_desc": "How lenders size an advance against a commercial truck, "
                        "and what raises or lowers it.",
        "keywords": "borrow against semi truck, truck title loan amount, truck "
                    "equity loan, commercial truck collateral value",
        "quick_answer": "Lenders advance a percentage of the truck's "
                        "<strong>wholesale or orderly liquidation value</strong> - "
                        "what it would fetch quickly at auction, not retail and not "
                        "what you paid. Anything still owed comes off the top, so the "
                        "advance is against your <strong>equity</strong>, not the "
                        "truck. Age, mileage, spec and condition move the valuation "
                        "more than anything you can say about the business.",
        "sections": [
            ("The Number Is Built From Equity, Not Value",
             "<p>The single most common misunderstanding is treating a title loan as "
             "a loan against the truck. It is a loan against the part of the truck "
             "you own.</p>"
             "<p>The arithmetic runs in one direction:</p>"
             "<ul>"
             "<li>Start with the lender's opinion of <strong>wholesale value</strong></li>"
             "<li>Apply the <strong>advance rate</strong> - a percentage, never the "
             "whole value</li>"
             "<li>Subtract <strong>anything still owed</strong> to an existing "
             "lienholder</li>"
             "<li>What remains is what can actually reach your account</li>"
             "</ul>"
             "<p>A truck worth $70,000 wholesale with $30,000 still owed does not "
             "support the same loan as an identical truck owned outright, and the "
             "difference is not marginal. See "
             "<a href=\"../title-loan-with-an-existing-lien/\">title loans with an "
             "existing lien</a> for how that case is structured.</p>"),
            ("Which Value a Lender Uses",
             "<p>Three different numbers get called \"the truck's value\", and only "
             "one of them is the one being lent against.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Basis</th><th>What it means</th><th>Used for lending?</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"Basis\">Retail</td>"
             "<td data-label=\"Means\">What a dealer would list it for</td>"
             "<td data-label=\"Used\">No - the highest number and the least relevant</td></tr>"
             "<tr><td data-label=\"Basis\">Wholesale / trade</td>"
             "<td data-label=\"Means\">What a dealer would pay for it</td>"
             "<td data-label=\"Used\">Commonly the basis</td></tr>"
             "<tr><td data-label=\"Basis\">Orderly liquidation</td>"
             "<td data-label=\"Means\">What it fetches sold in a reasonable window</td>"
             "<td data-label=\"Used\">Common on larger or specialised units</td></tr>"
             "<tr><td data-label=\"Basis\">Forced liquidation</td>"
             "<td data-label=\"Means\">What it fetches sold fast</td>"
             "<td data-label=\"Used\">The conservative floor some lenders price to</td></tr>"
             "</tbody></table></div>"
             "<p>The gap between retail and forced liquidation on a used sleeper can "
             "be substantial, which is why an owner quoting a marketplace listing and "
             "a lender quoting an advance rarely start in the same place.</p>"),
            ("What Moves the Valuation",
             "<p>Four things account for most of the spread between two otherwise "
             "similar trucks:</p>"
             "<ul>"
             "<li><strong>Age and mileage together.</strong> Neither alone. A "
             "high-mileage truck with a documented rebuild is a different asset from "
             "one without.</li>"
             "<li><strong>Spec.</strong> Engine, transmission, axle configuration and "
             "sleeper size decide how many buyers exist. A common spec sells quickly; "
             "an unusual one does not, and lenders price that.</li>"
             "<li><strong>Condition and records.</strong> Service history, tyre and "
             "brake condition, and whether the truck presents as maintained.</li>"
             "<li><strong>Title status.</strong> A clean title against a branded, "
             "salvage or rebuilt one is a different conversation entirely.</li>"
             "</ul>"
             "<p><a href=\"../what-a-truck-appraiser-looks-for/\">What a truck "
             "appraiser looks for</a> covers the inspection in detail.</p>"),
            ("What the Proceeds Are Really For",
             "<p>Title lending is short-dated, secured capital. It suits a specific "
             "shape of need: a gap you can see the end of.</p>"
             "<p>It fits a repair that puts a truck back to work, a bridge across a "
             "slow-paying receivable, or capital to take a contract that starts before "
             "it pays. It fits poorly as general operating cash on a business that is "
             "losing money, because the collateral is the thing that earns.</p>"
             "<p>That distinction matters more here than with unsecured credit. "
             "Defaulting on an unsecured loan is a financial problem; defaulting on a "
             "title loan can remove the asset the revenue depends on. See "
             "<a href=\"../title-loan-proceeds-repairs-vs-payroll/\">what the proceeds "
             "should and should not fund</a>.</p>"),
            ("Getting a Realistic Number Before You Apply",
             "<p>You can approximate the lender's view without an appraisal:</p>"
             "<ul>"
             "<li><strong>Find the wholesale number</strong>, not the asking price - "
             "comparable sold units, same spec, similar mileage.</li>"
             "<li><strong>Assume an advance rate, not the full value.</strong></li>"
             "<li><strong>Subtract the exact payoff</strong> on any existing lien, in "
             "writing from the lienholder.</li>"
             "<li><strong>Take off closing costs</strong> - title work, filing and "
             "any inspection.</li>"
             "</ul>"
             "<p>If the remainder is not worth the cost of the money, that is useful "
             "to know before an inspection is booked rather than after.</p>"),
        ],
        "faqs": [
            ("How much can I borrow against my semi truck?",
             "A percentage of the truck's <strong>wholesale or orderly liquidation "
             "value</strong>, less anything still owed on it. Lenders lend against "
             "equity rather than value, so a truck with an existing loan supports a "
             "smaller advance than the same truck owned outright."),
            ("Do lenders use retail value or wholesale?",
             "Wholesale, or a liquidation basis, essentially always. Retail is what a "
             "dealer would list the truck for; a lender is sizing what it could "
             "recover if it had to sell, which is a different and lower number."),
            ("Can I borrow against a truck I am still paying off?",
             "Often yes, but the existing balance comes off the top and the structure "
             "differs - the new lender is either paying off the first lienholder or "
             "taking a subordinate position, and not every lender will do the "
             "latter."),
            ("Does my credit score decide the amount?",
             "It influences pricing more than size. The advance is driven by the "
             "collateral - value, equity, condition and title status - while credit "
             "and the operating history tend to move the rate and the term."),
            ("What lowers the advance the most?",
             "An unusual spec and a branded title, more than mileage. A common "
             "configuration with a clean title has a deep buyer pool, which is what a "
             "lender is really pricing; a truck that would be slow to sell gets a "
             "conservative number regardless of condition."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../what-a-truck-appraiser-looks-for/", "What a truck appraiser looks for"),
            ("../title-loan-with-an-existing-lien/", "Title loans with an existing lien"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
        ],
        "sources": [IRS_946, BTS, CFPB],
    },
    {
        "slug": "what-a-truck-appraiser-looks-for",
        "crumb": "What an Appraiser Looks For",
        "title": "What a Truck Appraiser Looks For | Axiant Partners",
        "og_title": "What a Truck Appraiser Looks For",
        "h1": "What a Truck Appraiser Looks For",
        "headline": "What a Truck Appraiser Looks For",
        "lede": "The inspection that decides your advance - what is checked, "
                "what is documented, and what you can prepare",
        "meta_desc": "A truck appraisal decides the advance. See what inspectors "
                     "check, why records matter as much as condition, and how to "
                     "prepare so the valuation reflects the truck you actually own.",
        "article_desc": "What a commercial truck appraisal covers and how to "
                        "prepare for one.",
        "keywords": "truck appraisal, commercial truck inspection, equipment "
                    "appraiser, truck valuation for loan",
        "quick_answer": "An appraiser is answering one question: <strong>what would "
                        "this truck sell for, and how quickly</strong>. That means "
                        "spec and title status first, then condition, then records. "
                        "Documentation moves the number more than owners expect - a "
                        "maintained truck without a service history appraises like an "
                        "unmaintained one.",
        "sections": [
            ("The Question Behind the Inspection",
             "<p>An appraisal is not a mechanical assessment. It is a resale estimate "
             "with an inspection attached.</p>"
             "<p>That reframing explains most of what seems arbitrary about the "
             "process. An appraiser is not grading how well you have looked after the "
             "truck; they are estimating what a buyer would pay and how long a sale "
             "would take. A well-kept truck in an unpopular spec can appraise below a "
             "tireder one that half the market wants.</p>"
             "<p>The distinction between orderly and forced liquidation value is where "
             "that time element lands - the same truck is worth less if the sale has "
             "to happen quickly. See "
             "<a href=\"/equipment-appraisal.html\">equipment appraisal</a> for how "
             "those bases differ across asset classes.</p>"),
            ("What Gets Checked",
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Area</th><th>What matters</th></tr></thead><tbody>"
             "<tr><td data-label=\"Area\">Identity</td>"
             "<td data-label=\"Matters\">VIN against the title, and that the title is "
             "clean rather than branded, salvage or rebuilt</td></tr>"
             "<tr><td data-label=\"Area\">Spec</td>"
             "<td data-label=\"Matters\">Engine, transmission, axle configuration, "
             "wheelbase, sleeper - this decides the buyer pool</td></tr>"
             "<tr><td data-label=\"Area\">Mileage and hours</td>"
             "<td data-label=\"Matters\">Read against age; a rebuild resets part of "
             "the story if it is documented</td></tr>"
             "<tr><td data-label=\"Area\">Driveline</td>"
             "<td data-label=\"Matters\">Engine and transmission condition, leaks, "
             "aftertreatment history</td></tr>"
             "<tr><td data-label=\"Area\">Wear items</td>"
             "<td data-label=\"Matters\">Tyres, brakes, clutch - cheap individually, "
             "material together</td></tr>"
             "<tr><td data-label=\"Area\">Body and frame</td>"
             "<td data-label=\"Matters\">Accident evidence, rust, frame straightness</td></tr>"
             "<tr><td data-label=\"Area\">Records</td>"
             "<td data-label=\"Matters\">Service history, major repairs, inspection "
             "reports</td></tr>"
             "</tbody></table></div>"),
            ("Why Records Move the Number",
             "<p>This is the part owners most often underestimate. Two trucks in "
             "identical condition, one with a documented service history and one "
             "without, do not appraise the same.</p>"
             "<p>The reason is the same as everything else here - resale. A buyer pays "
             "more for a truck whose history they can see, so an appraiser estimating "
             "resale credits the paperwork. An engine rebuild you cannot evidence is, "
             "to the valuation, an engine rebuild that did not happen.</p>"
             "<p>Keep invoices for anything significant: engine and transmission work, "
             "aftertreatment, tyres, brakes. It is the cheapest thing you can do to "
             "protect the asset's borrowing capacity.</p>"),
            ("Desktop Against On-Site",
             "<p>Not every valuation involves someone walking round the truck.</p>"
             "<ul>"
             "<li><strong>Desktop.</strong> Built from the VIN, spec, mileage, "
             "photographs and comparable sales. Faster and cheaper; usually "
             "conservative, because unverified condition is assumed rather than "
             "seen.</li>"
             "<li><strong>On-site.</strong> A physical inspection. Slower and it costs "
             "more, but it is where a genuinely good truck can beat the desktop "
             "assumption.</li>"
             "</ul>"
             "<p>If your truck is better than average for its age, an on-site "
             "inspection is usually worth asking for. If it is average, the desktop "
             "figure will not be far off and you save the time.</p>"),
            ("Preparing for It",
             "<ul>"
             "<li><strong>Have the title to hand</strong> and know exactly what is "
             "owed, in writing from the lienholder.</li>"
             "<li><strong>Assemble the service file</strong> before the inspection, "
             "not after the number comes back.</li>"
             "<li><strong>Clean it.</strong> Presentation genuinely affects a resale "
             "estimate, which is what this is.</li>"
             "<li><strong>Fix the cheap things.</strong> Warning lights and small "
             "leaks read as deferred maintenance and cost more in the valuation than "
             "they do to repair.</li>"
             "<li><strong>Photograph it honestly</strong> if the appraisal is a "
             "desktop one - a bad photo set produces a conservative number.</li>"
             "</ul>"
             "<p>Then check the equity arithmetic against "
             "<a href=\"../how-much-can-you-borrow-against-a-semi/\">what the advance "
             "is likely to be</a> before committing to the process.</p>"),
        ],
        "faqs": [
            ("What does a truck appraiser actually check?",
             "Identity and title status first - VIN against title, and whether the "
             "title is clean or branded - then spec, mileage against age, driveline "
             "condition, wear items like tyres and brakes, body and frame, and the "
             "service records."),
            ("Does a service history really change the valuation?",
             "Yes, and by more than owners expect. An appraisal is a resale estimate, "
             "and buyers pay more for documented history. Work you cannot evidence is "
             "effectively work that did not happen as far as the number is "
             "concerned."),
            ("What is the difference between a desktop and an on-site appraisal?",
             "A desktop valuation is built from VIN, spec, mileage, photographs and "
             "comparable sales - faster, cheaper, and usually conservative because "
             "condition is assumed. An on-site inspection costs more but is where an "
             "above-average truck can beat that assumption."),
            ("Does a branded or rebuilt title matter?",
             "Considerably. A branded, salvage or rebuilt title narrows the buyer pool "
             "sharply, and since the appraisal is estimating resale, a narrow buyer "
             "pool produces a conservative number regardless of how the truck "
             "presents."),
            ("Can I dispute an appraisal I think is low?",
             "You can supply evidence - comparable sold units in the same spec, "
             "documented major work, or an on-site inspection if the first pass was a "
             "desktop. Evidence moves valuations; disagreement on its own does not."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../how-much-can-you-borrow-against-a-semi/", "How much can you borrow against a semi"),
            ("../title-loan-with-an-existing-lien/", "Title loans with an existing lien"),
        ],
        "sources": [IRS_946, BTS, FTC],
    },
    {
        "slug": "title-loan-with-an-existing-lien",
        "crumb": "With an Existing Lien",
        "title": "Truck Title Loan With an Existing Lien | Axiant Partners",
        "og_title": "Can You Get a Truck Title Loan With an Existing Lien?",
        "h1": "Truck Title Loans With an Existing Lien",
        "headline": "Truck Title Loans With an Existing Lien",
        "lede": "Borrowing against a truck you are still paying off - how the "
                "structures differ and which lenders will do it",
        "meta_desc": "You can often borrow against a truck that still has a loan on "
                     "it. How payoff-and-replace differs from a second position, what "
                     "each costs, and which lenders will consider it.",
        "article_desc": "How truck title lending works when the vehicle already "
                        "carries a lien.",
        "keywords": "title loan existing lien, second lien truck loan, refinance "
                    "truck loan cash out, truck equity with loan",
        "quick_answer": "Usually yes, in one of two shapes. Either the new lender "
                        "<strong>pays off the existing lienholder</strong> and takes "
                        "first position, or they take a <strong>subordinate "
                        "position</strong> behind it. The first is cleaner and more "
                        "widely available; the second is priced higher and fewer "
                        "lenders will do it. Either way you are borrowing against "
                        "equity, so a large remaining balance leaves little to lend "
                        "against.",
        "sections": [
            ("The Two Structures",
             "<p>An existing lien does not usually stop a title loan. It changes what "
             "the transaction is.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th></th><th>Payoff and replace</th><th>Subordinate position</th>"
             "</tr></thead><tbody>"
             "<tr><td data-label=\"\"><strong>What happens</strong></td>"
             "<td data-label=\"Payoff\">New lender clears the old loan and takes first "
             "position</td>"
             "<td data-label=\"Sub\">Original lien stays; new lender sits behind it</td></tr>"
             "<tr><td data-label=\"\"><strong>Availability</strong></td>"
             "<td data-label=\"Payoff\">Widely offered</td>"
             "<td data-label=\"Sub\">Fewer lenders</td></tr>"
             "<tr><td data-label=\"\"><strong>Pricing</strong></td>"
             "<td data-label=\"Payoff\">Lower - first position on the whole asset</td>"
             "<td data-label=\"Sub\">Higher - recovers only after the first lien</td></tr>"
             "<tr><td data-label=\"\"><strong>Cash to you</strong></td>"
             "<td data-label=\"Payoff\">New loan less the payoff</td>"
             "<td data-label=\"Sub\">The full new advance</td></tr>"
             "<tr><td data-label=\"\"><strong>Watch for</strong></td>"
             "<td data-label=\"Payoff\">Prepayment penalty on the loan being cleared</td>"
             "<td data-label=\"Sub\">Whether the first lender's terms permit it at all</td></tr>"
             "</tbody></table></div>"),
            ("Equity Is Still the Constraint",
             "<p>Whichever structure, the arithmetic that governs is the same: value, "
             "times advance rate, minus what is owed.</p>"
             "<p>A truck with most of its original loan outstanding has little equity "
             "regardless of what it is worth, and no structure invents any. This is "
             "the most common reason an application that looked promising does not "
             "produce a useful number - the truck is valuable and the equity is not "
             "there yet.</p>"
             "<p>Get the exact payoff figure in writing before you start. A payoff "
             "quote is not the same as the balance on a statement, because it includes "
             "interest to the payoff date and any early-settlement charge.</p>"),
            ("The Prepayment Trap on a Payoff",
             "<p>If the new lender is clearing your existing loan, that loan is being "
             "repaid early - and early repayment is exactly what a prepayment clause "
             "is written for.</p>"
             "<p>On a title or equipment loan taken relatively recently, the charge can "
             "be a meaningful percentage of the balance, and it comes out of the "
             "proceeds. A deal that pencils on the balance can stop making sense on "
             "the payoff figure.</p>"
             "<p>Read the clause in the existing note before you get as far as an "
             "inspection. It is the cheapest step in the process and the one most "
             "often skipped.</p>"),
            ("Whether Your First Lender Permits a Second",
             "<p>Subordinate lending has a second gate: the original loan agreement.</p>"
             "<p>Some agreements prohibit additional liens on the collateral outright, "
             "and taking one anyway can be a default under the first loan even if you "
             "keep paying it. Others require the first lender's written consent. "
             "Others are silent.</p>"
             "<p>This is worth checking rather than assuming, because the consequence "
             "of getting it wrong is not a declined application - it is a default on "
             "the loan you already have.</p>"),
            ("Which Structure Fits",
             "<p><strong>Payoff and replace</strong> tends to fit when the existing "
             "loan is expensive, the remaining term is long, or you want a single "
             "payment. You are refinancing and taking cash out in one move, and you "
             "get first-position pricing.</p>"
             "<p><strong>A subordinate position</strong> tends to fit when the "
             "existing loan is cheap and you do not want to disturb it - a low rate "
             "locked some time ago is worth keeping, and paying it off to access "
             "equity can cost more than the higher rate on the smaller second "
             "loan.</p>"
             "<p>Run both. The comparison is arithmetic, and the answer is not always "
             "the cheaper headline rate. Start from "
             "<a href=\"../how-much-can-you-borrow-against-a-semi/\">what the equity "
             "supports</a>.</p>"),
        ],
        "faqs": [
            ("Can I get a title loan if my truck still has a loan on it?",
             "Usually yes. Either the new lender pays off the existing lienholder and "
             "takes first position, or takes a subordinate position behind it. The "
             "payoff structure is more widely available and cheaper; the subordinate "
             "one leaves your existing loan untouched."),
            ("What is a second-position truck loan?",
             "A loan secured against the same truck but ranking behind an existing "
             "lien, so the first lender is repaid first if the truck is sold. Fewer "
             "lenders offer it and it is priced higher, because the recovery position "
             "is weaker."),
            ("Will paying off my existing loan trigger a penalty?",
             "It can. Clearing a loan early is what a prepayment clause exists for, "
             "and the charge comes out of your proceeds. Get the payoff figure in "
             "writing rather than working from the statement balance, since a payoff "
             "includes interest to date and any settlement charge."),
            ("Does my current lender have to agree to a second lien?",
             "Sometimes. Some loan agreements prohibit additional liens on the "
             "collateral outright and others require written consent. Taking one "
             "where it is prohibited can be a default on the loan you already have, so "
             "check the agreement before applying."),
            ("How much equity do I need for this to be worth doing?",
             "Enough that the advance, after the payoff and closing costs, is worth "
             "the cost of the money. A truck with most of its original loan "
             "outstanding has little equity whatever it is worth, and no structure "
             "creates any."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("../how-much-can-you-borrow-against-a-semi/", "How much can you borrow against a semi"),
            ("../truck-title-loan-vs-sale-leaseback/", "Title loan vs sale-leaseback"),
            ("../what-happens-if-you-default-truck-title-loan/", "What happens if you default"),
        ],
        "sources": [FTC, CFPB, IRS_946],
    },
]

# Articles 4-8 live in companion modules to keep each file readable.
from cluster_truck_title_b import MORE as _B
from cluster_truck_title_c import MORE as _C
ARTICLES = ARTICLES + _B + _C
