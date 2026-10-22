# -*- coding: utf-8 -*-
"""Heavy equipment equity loans - 5 articles. Asset-equity cluster (AEO plan 2b).

Validated 2026-10-22 against Bing AI Mode: "title loan on my excavator" returned no
specialist source (the answer fell back to Florida car-title rules), and "cash out
equity in my construction equipment" cited only a generalist on sale-leaseback.

Ranges are described as conventional across lenders, never quoted as anyone's
terms, and match what the site already publishes (equipment refinancing: roughly
50-80% of forced liquidation value, 24-72 month terms). No funded totals, no
testimonials, no named-lender rates. One entity: Axiant Partners, (561) 268-0465,
Boca Raton. Business-purpose only.

The fact this cluster is built around: most yellow iron has no title. Excavators,
dozers and loaders are not covered by a state certificate-of-title statute, so the
lender perfects its security interest by filing a UCC-1 financing statement, not by
noting a lien on a title (UCC 9-310, 9-311).
"""

CLUSTER = {
    "pillar": "heavy-equipment-equity-loan.html",
    "hub": "heavy-equipment-equity-loan/articles",
    "crumb": "Heavy Equipment Equity Loans",
    "cta_inline": "Get matched against your equipment's equity",
    "cta_button": "Get Matched for an Equipment Equity Loan",
    "hub_title": "Heavy Equipment Equity Loan Guides | Axiant Partners",
    "hub_h1": "Heavy Equipment Equity Loan Articles",
    "hub_lede": "Borrowing against excavators, loaders and dozers you already own - "
                "what they are worth to a lender, how the lien works, and the "
                "alternatives",
    "hub_desc": "Guides to borrowing against construction equipment you own: valuation, "
                "existing liens, equity loan versus sale-leaseback or a merchant cash "
                "advance, and what happens in a default.",
    "hub_intro": "Most construction equipment has no title, so borrowing against it "
                 "works differently from a truck title loan: the lender files a UCC-1 "
                 "and lends against what the machine would bring at auction. Start with "
                 "<a href=\"/heavy-equipment-equity-loan.html\">heavy equipment equity "
                 "loans</a>, or see <a href=\"/equipment-appraisal.html\">how equipment "
                 "is appraised</a>.",
    "hub_cta_h2": "Own the iron outright, or close to it?",
    "hub_cta_p": "Send the make, model, year, hours and what is still owed. We will "
                 "tell you plainly what the equity supports.",
}

UCC_9310 = ("https://www.law.cornell.edu/ucc/9/9-310",
            "UCC &sect; 9-310: When Filing Is Required to Perfect a Security Interest",
            "The rule that a lender perfects a lien on most equipment by filing a "
            "financing statement (UCC-1) rather than through a title.")
UCC_9311 = ("https://www.law.cornell.edu/ucc/9/9-311",
            "UCC &sect; 9-311: Property Subject to Certificate-of-Title Statutes",
            "Why titled vehicles such as dump trucks and lowboy trailers are handled "
            "through the title, unlike untitled machines.")
UCC_9513 = ("https://www.law.cornell.edu/ucc/9/9-513",
            "UCC &sect; 9-513: Termination Statement",
            "The obligation to file a termination (UCC-3) once a secured debt is paid, "
            "which clears an old lien off the record.")
UCC_9609 = ("https://www.law.cornell.edu/ucc/9/9-609",
            "UCC &sect; 9-609: Secured Party's Right to Take Possession After Default",
            "The rule allowing repossession without a court order, provided there is no "
            "breach of the peace.")
UCC_9610 = ("https://www.law.cornell.edu/ucc/9/9-610",
            "UCC &sect; 9-610: Disposition of Collateral After Default",
            "The requirement that every aspect of a sale of repossessed collateral be "
            "commercially reasonable.")
UCC_9615 = ("https://www.law.cornell.edu/ucc/9/9-615",
            "UCC &sect; 9-615: Application of Proceeds; Surplus and Deficiency",
            "How sale proceeds are applied and when the borrower owes a deficiency or "
            "is owed a surplus.")
UCC_9623 = ("https://www.law.cornell.edu/ucc/9/9-623",
            "UCC &sect; 9-623: Right to Redeem Collateral",
            "The borrower's right to recover the collateral by paying what is owed "
            "before it is sold.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "The authority on Section 179 and depreciation for business equipment - "
           "the deduction you give up when you sell a machine.")
IRS_544 = ("https://www.irs.gov/publications/p544",
           "IRS Publication 544: Sales and Other Dispositions of Assets",
           "How gain on selling depreciated business property is taxed, including "
           "depreciation recapture.")
ASA = ("https://www.appraisers.org/",
       "American Society of Appraisers",
       "The professional body that credentials machinery and equipment appraisers.")
TAF = ("https://appraisalfoundation.org/",
       "The Appraisal Foundation",
       "Publisher of the Uniform Standards of Professional Appraisal Practice "
       "(USPAP) that credentialed appraisers work under.")
CARB = ("https://ww2.arb.ca.gov/our-work/programs/use-road-diesel-fueled-fleets-regulation",
        "California Air Resources Board: In-Use Off-Road Diesel-Fueled Fleets",
        "California's rules on older off-road diesel engines, which narrow the "
        "buyer pool for older-tier machines.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on small business credit, including how cost is "
        "disclosed to borrowers.")
FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "The FTC's guidance to lenders, brokers and merchant cash advance providers on "
       "misrepresented costs, unlawful collection and false claims of government affiliation.")


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


ARTICLES = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "what-your-excavator-is-worth-to-a-lender",
        "crumb": "What Your Excavator Is Worth",
        "title": "What Is Your Excavator Worth to a Lender? | Axiant",
        "og_title": "What Is Your Excavator Worth to a Lender?",
        "h1": "What Is Your Excavator Worth to a Lender?",
        "headline": "What Your Excavator Is Worth to a Lender",
        "lede": "Why the number a lender works from sits well below what you paid, and "
                "the machine-specific things that move it",
        "meta_desc": "Lenders value excavators, dozers and loaders at liquidation value, "
                     "then advance a share of it. Hours, undercarriage, brand and "
                     "emissions tier move the number.",
        "article_desc": "How lenders value construction equipment for an equity loan, "
                        "and what raises or lowers the figure.",
        "keywords": "excavator value for loan, borrow against excavator, heavy "
                    "equipment collateral value, forced liquidation value equipment",
        "quick_answer": "A lender values your excavator at what it would bring at "
                        "auction - usually <strong>forced or orderly liquidation "
                        "value</strong>, not what you paid or a dealer's asking price - "
                        "then advances a share of that, typically in the range of "
                        "<strong>50-80%</strong>. Engine hours, undercarriage wear, "
                        "brand, emissions tier and service records move the valuation "
                        "more than anything about your business.",
        "sections": [
            ("Three Numbers, and the Lender Uses the Lowest",
             "<p>Owners usually start from the purchase price or a listing for a "
             "similar machine. A lender starts somewhere else entirely: what it could "
             "recover if it had to sell the machine without you.</p>"
             + _table(["Value", "What it means", "Used for lending?"], [
                 ["Retail / dealer asking", "A reconditioned machine on a lot, often with a warranty", "No - the highest and least relevant"],
                 ["Fair market value", "A willing buyer and seller, no pressure", "Sometimes as a reference"],
                 ["Orderly liquidation (OLV)", "Sold over a reasonable marketing window", "Common on larger or newer units"],
                 ["Forced liquidation (FLV)", "Sold quickly, typically at auction", "The conservative basis many lenders price to"],
             ])
             + "<p>The advance is then a percentage of the liquidation figure, which "
             "is why the first number an owner hears is almost always lower than "
             "expected. Our guide to <a href=\"/equipment-appraisal/articles/orderly-vs-forced-liquidation-value/\">"
             "orderly versus forced liquidation value</a> explains the gap in detail.</p>"),
            ("Hours Matter More Than Age",
             "<p>On a truck, mileage and model year drive value. On construction "
             "equipment the equivalent is the <strong>hour meter</strong>. A five-year-old "
             "excavator with low hours can be worth more than a three-year-old unit "
             "that has run double shifts.</p>"
             "<p>What a lender and appraiser look at alongside the hours:</p>"
             "<ul>"
             "<li><strong>Whether the hours are believable.</strong> A meter that "
             "reads low against visible wear, or a replaced meter with no record, "
             "pushes the valuation down rather than up.</li>"
             "<li><strong>Major component history.</strong> A documented engine or "
             "hydraulic pump rebuild changes the picture on a high-hour machine.</li>"
             "<li><strong>How the hours were earned.</strong> Demolition, quarry and "
             "forestry work wears a machine faster than general site work, and "
             "appraisers look for it.</li>"
             "</ul>"),
            ("Undercarriage, Brand and Attachments",
             "<p>Three things that rarely matter on a truck matter a great deal on "
             "yellow iron:</p>"
             "<ul>"
             "<li><strong>Undercarriage condition.</strong> On tracked excavators and "
             "dozers, tracks, rollers, idlers and sprockets wear out and are expensive "
             "to replace. Appraisers estimate remaining undercarriage life as a "
             "percentage, and a worn undercarriage comes straight off the value.</li>"
             "<li><strong>Brand and dealer support.</strong> Machines from makers "
             "with deep dealer networks and parts availability resell faster, and a "
             "lender prices the depth of the buyer pool, not the brand name.</li>"
             "<li><strong>Attachments.</strong> Buckets, thumbs, hammers and quick "
             "couplers add value when they are common and match the machine; "
             "specialised attachments add less than they cost.</li>"
             "</ul>"),
            ("Emissions Tier and Where the Machine Can Be Sold",
             "<p>Diesel engines in off-road equipment are built to federal emissions "
             "tiers. Newer Tier 4 Final machines sell into every market; older tiers "
             "can face a narrower buyer pool. In California, the Air Resources "
             "Board's in-use off-road diesel fleet rules limit how long older engines "
             "can stay in service in covered fleets, which affects who will buy an "
             "older machine there.</p>"
             "<p>A lender cares because a narrower buyer pool means a lower, slower "
             "recovery if it ever has to sell. Two otherwise identical machines can "
             "be valued differently because of the engine tier alone.</p>"),
            ("What You Can Do Before the Valuation",
             "<p>You cannot change the hours, but you can change how much of the "
             "machine's real value is visible:</p>"
             "<ul>"
             "<li><strong>Pull the service records</strong> - oil analysis, dealer "
             "invoices, component rebuilds.</li>"
             "<li><strong>Photograph it properly</strong> - hour meter, serial plate, "
             "undercarriage from both sides, bucket and attachments, cab.</li>"
             "<li><strong>Fix the cheap, visible things</strong> - leaks, broken "
             "glass and missing guards cost little and drag a valuation.</li>"
             "<li><strong>Know what is owed.</strong> Anything still financed comes "
             "off the top; see <a href=\"../heavy-equipment-loan-with-an-existing-lien/\">"
             "borrowing against equipment you are still paying off</a>.</li>"
             "</ul>"
             "<p>For the formal side - who can sign an appraisal a lender will accept "
             "- see <a href=\"/equipment-appraisal/articles/who-can-appraise-business-equipment/\">"
             "who can appraise business equipment</a>.</p>"),
            ("A Worked Example",
             "<p>Illustrative arithmetic, not a quote. A mid-size tracked excavator, "
             "owned outright; the owner's estimate comes from a recent listing for a "
             "similar unit, and both liquidation values from an appraisal:</p>"
             + _table(["Step", "Figure"], [
                 ["Owner's estimate", "$165,000"],
                 ["Orderly liquidation value", "$118,000"],
                 ["Forced liquidation value", "$96,000"],
                 ["Advance at 65% of FLV", "$62,400"],
                 ["Less closing costs", "Varies"],
             ])
             + "<p>The owner expected to borrow against $165,000. The lender is "
             "lending against $96,000. Knowing that before you build a plan around "
             "the money saves weeks.</p>"),
        ],
        "faqs": [
            ("Do lenders use what I paid for the machine?",
             "No. They use what it would bring if sold - usually forced or orderly "
             "liquidation value - and then advance a percentage of that. Purchase "
             "price and dealer listings are not part of the calculation."),
            ("How much of the value will a lender advance?",
             "Advances against forced liquidation value commonly fall in the range of "
             "roughly 50-80%, depending on the machine, its condition, how quickly it "
             "would sell, and the business's ability to repay."),
            ("Do high hours rule a machine out?",
             "Not on their own. High hours lower the value, but a well-maintained "
             "machine with documented rebuilds and a strong resale market can still "
             "support a meaningful advance."),
            ("Does the undercarriage really matter that much?",
             "On tracked machines, yes. Undercarriage replacement is one of the "
             "largest repair costs on an excavator or dozer, so appraisers estimate "
             "the remaining life and adjust the value for it."),
            ("Do I need a formal appraisal?",
             "For larger loans, usually. Smaller deals may rely on a desktop "
             "valuation from photos, serials and auction data; larger ones often "
             "require an on-site inspection by a credentialed appraiser."),
        ],
        "related": [
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("../heavy-equipment-loan-with-an-existing-lien/", "Borrowing against equipment with an existing lien"),
            ("/equipment-appraisal/articles/orderly-vs-forced-liquidation-value/", "Orderly vs forced liquidation value"),
            ("/equipment/excavators/", "Excavator financing"),
        ],
        "sources": [ASA, TAF, CARB],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "heavy-equipment-loan-with-an-existing-lien",
        "crumb": "Borrowing With an Existing Lien",
        "title": "Equipment Equity Loan With an Existing Lien | Axiant",
        "og_title": "Borrowing Against Equipment You Still Owe On",
        "h1": "Borrowing Against Equipment You Still Owe On",
        "headline": "Borrowing Against Heavy Equipment With an Existing Lien",
        "lede": "How a cash-out refinance works on a machine that is not paid off, and "
                "the liens owners do not know they have",
        "meta_desc": "You can borrow against equipment you are still paying for if "
                     "there is real equity. How cash-out refinances work, and why "
                     "blanket UCC liens block deals.",
        "article_desc": "How lenders handle construction equipment that still has a "
                        "lender on it, and the lien problems that stop deals.",
        "keywords": "equipment cash out refinance, borrow against financed equipment, "
                    "UCC lien equipment, blanket lien business loan",
        "quick_answer": "Yes, if there is real equity. The usual structure is a "
                        "<strong>cash-out refinance</strong>: the new lender pays off "
                        "the existing balance and advances the rest of what the machine "
                        "supports, typically sized at <strong>50-80% of forced "
                        "liquidation value</strong> minus the payoff. The deal-killer "
                        "is often not the loan you know about but a <strong>blanket "
                        "UCC lien</strong> from another lender that already covers "
                        "all your equipment.",
        "sections": [
            ("Equity Is the Only Thing That Can Be Lent Against",
             "<p>A machine with a loan on it can still raise money, but only the part "
             "you own. The arithmetic:</p>"
             "<ol>"
             "<li>The lender values the machine at liquidation value.</li>"
             "<li>It applies its advance rate - a share of that value, never all of it.</li>"
             "<li>It subtracts the payoff on the existing loan.</li>"
             "<li>What is left, less closing costs, is what reaches you.</li>"
             "</ol>"
             + _table(["", "Owned outright", "Still owes $40,000"], [
                 ["Forced liquidation value", "$100,000", "$100,000"],
                 ["Advance at 65%", "$65,000", "$65,000"],
                 ["Less existing payoff", "$0", "$40,000"],
                 ["Cash to you (before costs)", "$65,000", "$25,000"],
             ])
             + "<p>Illustrative arithmetic. If the payoff is close to the advance, "
             "there is nothing to draw, and the more useful conversation is about "
             "the payment rather than the equity.</p>"),
            ("Cash-Out Refinance vs a Second Lien",
             "<p>There are two ways to borrow against a machine that already has a "
             "lender on it:</p>"
             "<ul>"
             "<li><strong>Cash-out refinance.</strong> The new lender pays off the "
             "first lender in full and takes the first position. This is the common "
             "route, because lenders prefer to be first in line.</li>"
             "<li><strong>Second-position loan.</strong> The new lender lends behind "
             "the existing one and is paid only after it. Fewer lenders will do this "
             "on equipment, and it usually costs more, because a second lien recovers "
             "little in a forced sale.</li>"
             "</ul>"
             "<p>If the existing loan has a low rate you want to keep, raise that up "
             "front - it decides which lenders are worth talking to.</p>"),
            ("How Equipment Liens Work When There Is No Title",
             "<p>Most construction machines are not covered by a state title statute, "
             "so a lender's lien is not written on a title. It is recorded by filing "
             "a <strong>UCC-1 financing statement</strong>, usually with the "
             "secretary of state where your business is organized. Titled units such "
             "as dump trucks and lowboy trailers are the exception: their liens go "
             "on the title, as with a "
             "<a href=\"/commercial-truck-title-loan.html\">commercial truck title loan</a>.</p>"
             "<p>That matters for two reasons. A new lender will search the UCC "
             "records before it lends, and anything filed against your equipment "
             "shows up whether or not you think of it as a loan on that machine. And "
             "when a loan is paid off, the old lender should file a termination "
             "(UCC-3) - if it never did, the old lien still sits on the record.</p>"),
            ("The Blanket Lien Problem",
             "<p>The most common surprise is a <strong>blanket lien</strong>: a UCC-1 "
             "that covers \"all assets\" or \"all equipment\" of the business. Bank "
             "lines of credit, SBA loans and many merchant cash advances file them. "
             "If one exists, that lender already has a claim on the excavator you "
             "thought you owned free and clear.</p>"
             "<p>What happens next depends on the blanket lienholder:</p>"
             "<ul>"
             "<li>It may agree to <strong>subordinate</strong> its lien on the "
             "specific machine, letting the new lender go first on that unit.</li>"
             "<li>It may need to be <strong>paid off</strong> as part of the deal.</li>"
             "<li>It may refuse, in which case the machine cannot be used as "
             "first-position collateral.</li>"
             "</ul>"
             "<p>If the blanket filing is from an advance you have already paid off, "
             "getting it released is usually a paperwork problem - see "
             "<a href=\"/business-debt-relief/articles/release-ucc-lien-business/\">"
             "releasing a UCC lien</a>.</p>"),
            ("What to Have Ready",
             "<ul>"
             "<li>A current <strong>payoff letter</strong> from the existing lender, "
             "with a good-through date.</li>"
             "<li>The <strong>loan or lease agreement</strong>, so the new lender can "
             "see whether it is a loan or a lease with a buyout.</li>"
             "<li>Your own <strong>UCC search</strong>, or at least a list of every "
             "lender and advance provider you have used.</li>"
             "<li>Serial numbers, hours, photos and service records for the machine.</li>"
             "</ul>"
             "<p>Deals in this category stall on liens far more often than on credit. "
             "Clearing them up before you apply is the difference between days and "
             "weeks.</p>"),
        ],
        "faqs": [
            ("Can I get an equity loan on equipment I am still paying for?",
             "Yes, if the machine is worth meaningfully more than what you owe. The "
             "usual structure is a cash-out refinance that pays off the existing lender "
             "and advances the remaining equity, less costs."),
            ("What is a blanket lien?",
             "A UCC-1 filing that covers all of a business's assets or all of its "
             "equipment, rather than one machine. Banks, SBA lenders and many merchant "
             "cash advance providers file them, and they can block a new lender from "
             "taking first position on your equipment."),
            ("Will a lender take second position behind my current loan?",
             "Some will, but fewer than will refinance, and second-position equipment "
             "loans usually cost more because the lender recovers little if the "
             "machine is sold."),
            ("How do I find out what liens are on my equipment?",
             "Search the UCC records with the secretary of state where your business "
             "is organized. A lender will run the same search before it funds."),
            ("My old loan is paid off but the lien is still on file. What now?",
             "Ask the former lender to file a UCC-3 termination. Secured parties are "
             "obliged to terminate filings once the debt is paid, and a lender can "
             "usually close once the termination is filed or the release is in hand."),
        ],
        "related": [
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("../what-your-excavator-is-worth-to-a-lender/", "What your excavator is worth to a lender"),
            ("/equipment-financing/articles/equipment-refinancing/", "Equipment refinancing"),
            ("/business-debt-relief/articles/release-ucc-lien-business/", "Releasing a UCC lien"),
        ],
        "sources": [UCC_9310, UCC_9311, UCC_9513],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "equipment-equity-loan-vs-sale-leaseback",
        "crumb": "Equity Loan vs Sale-Leaseback",
        "title": "Equipment Equity Loan vs Sale-Leaseback | Axiant",
        "og_title": "Equipment Equity Loan vs Sale-Leaseback",
        "h1": "Equipment Equity Loan vs Sale-Leaseback",
        "headline": "Equipment Equity Loan vs Sale-Leaseback",
        "lede": "Two ways to pull cash out of machines you own - one keeps ownership, "
                "the other sells and leases back",
        "meta_desc": "An equity loan keeps the machine in your name; a sale-leaseback "
                     "sells it and leases it back. How the cash, cost, tax and "
                     "ownership compare.",
        "article_desc": "How an equipment equity loan and a sale-leaseback compare on "
                        "cash raised, ownership, cost and tax.",
        "keywords": "equipment equity loan vs sale leaseback, sale leaseback "
                    "construction equipment, cash out equipment",
        "quick_answer": "Both raise cash from equipment you own and let you keep "
                        "using it. An <strong>equity loan</strong> keeps the machine in "
                        "your name with a lien filed against it; a "
                        "<strong>sale-leaseback</strong> sells it to a lessor and "
                        "leases it back, so you give up ownership (often with a "
                        "buyout at the end). Equity loans commonly advance "
                        "<strong>50-80% of forced liquidation value</strong>; "
                        "sale-leasebacks can price closer to fair value, but the tax "
                        "and ownership consequences are different.",
        "sections": [
            ("The Side-by-Side",
             _table(["", "Equity loan", "Sale-leaseback"], [
                 ["Who owns the machine", "You", "The lessor, until any buyout"],
                 ["Security", "UCC-1 lien on the machine", "Ownership itself"],
                 ["Cash raised", "A share of liquidation value", "Often priced nearer fair value"],
                 ["Payments", "Loan principal and interest", "Lease payments"],
                 ["End of term", "Lien released, you own it clear", "Buy back, renew or return"],
                 ["Depreciation", "Stays with you", "Passes to the owner of the machine"],
                 ["On your balance sheet", "Asset plus a loan", "Depends on the lease terms"],
             ])
             + "<p>Neither is cheaper in every case. The right one depends on how much "
             "cash you need, whether you want to own the machine at the end, and what "
             "the tax consequences are for your business.</p>"),
            ("When an Equity Loan Is the Better Fit",
             "<ul>"
             "<li><strong>You want to keep owning the machine</strong> and come out "
             "of the term with it free and clear.</li>"
             "<li><strong>The machine still has depreciation left</strong> you want "
             "to keep claiming.</li>"
             "<li><strong>You need less than the full value</strong>, so the lower "
             "advance is not a constraint.</li>"
             "<li><strong>You have several machines</strong> and can pledge more than "
             "one, which raises the total without selling anything.</li>"
             "</ul>"),
            ("When a Sale-Leaseback Is the Better Fit",
             "<ul>"
             "<li><strong>You need the maximum cash</strong> the equipment can raise.</li>"
             "<li><strong>The machine is largely depreciated</strong>, so there is "
             "little deduction left to give up.</li>"
             "<li><strong>You would rather carry a lease payment</strong> than a loan, "
             "for reasons your accountant can explain for your situation.</li>"
             "</ul>"
             "<p>Our <a href=\"/equipment-financing/articles/equipment-sale-leaseback-financing/\">"
             "sale-leaseback guide</a> covers the structure in detail.</p>"),
            ("The Tax Questions to Ask Before You Sell",
             "<p>Selling a machine you have depreciated is a taxable event. If it "
             "sells for more than its depreciated tax basis, the gain attributable to "
             "depreciation you took is generally <strong>recaptured as ordinary "
             "income</strong> - which can surprise owners who took Section 179 or "
             "bonus depreciation in the year of purchase. An equity loan is not a "
             "sale, so it does not trigger that.</p>"
             "<p>On the lease side, whether a sale-leaseback is treated as a true "
             "lease or as a financing for tax purposes depends on its terms, "
             "including the buyout. That changes what you can deduct. These are "
             "questions for your tax adviser before you sign, not after.</p>"),
            ("A Worked Example",
             "<p>Illustrative arithmetic, not a quote. A wheel loader, owned "
             "outright, fair market value $140,000, forced liquidation value "
             "$100,000:</p>"
             + _table(["", "Equity loan", "Sale-leaseback"], [
                 ["Cash raised", "$65,000 (65% of FLV)", "Up to roughly fair value, depending on the lessor"],
                 ["You still own it", "Yes", "No, until the buyout"],
                 ["Tax event at closing", "No", "Possible depreciation recapture"],
             ])
             + "<p>If $65,000 covers the need, the equity loan raises it without a "
             "taxable sale. If the business needs more, the sale-leaseback can raise "
             "it, at the cost of ownership and a tax conversation.</p>"),
            ("Questions to Ask Before You Sign Either",
             "<ul>"
             "<li><strong>What value is the offer built on?</strong> Ask whether the "
             "number is a percentage of forced liquidation, orderly liquidation or "
             "fair value, and see the appraisal it came from.</li>"
             "<li><strong>What is the total you will pay?</strong> For a loan, total "
             "payments over the term; for a lease, every lease payment plus the "
             "buyout. Compare totals, not monthly payments.</li>"
             "<li><strong>How is the buyout set?</strong> A fixed amount, a "
             "percentage of the original price, or fair market value at the end - "
             "the last can be the most expensive if the machine holds its value.</li>"
             "<li><strong>What happens if you sell the business or the machine "
             "early?</strong> Prepayment terms on a loan and early-termination "
             "terms on a lease differ widely.</li>"
             "<li><strong>Who pays insurance, maintenance and taxes</strong> during "
             "a lease? In most equipment leases it is still you.</li>"
             "</ul>"
             "<p>If two offers cannot be compared on those five points, ask for the "
             "missing figures in writing before you decide.</p>"),
        ],
        "faqs": [
            ("Which raises more cash, an equity loan or a sale-leaseback?",
             "A sale-leaseback often can, because it can be priced nearer the "
             "machine's fair value, while an equity loan advances a share of "
             "liquidation value. The difference narrows on older machines."),
            ("Do I keep using the equipment either way?",
             "Yes. In both structures the machine stays on your jobsite. What "
             "changes is whether you own it during the term."),
            ("Does a sale-leaseback have tax consequences?",
             "It can. Selling depreciated equipment may trigger depreciation "
             "recapture, and how the lease is treated depends on its terms. Speak to "
             "your tax adviser before you sign."),
            ("Can I buy the equipment back at the end of a sale-leaseback?",
             "Usually, if the lease includes a purchase option. The buyout price "
             "and how it is set vary by lessor and should be read before signing."),
        ],
        "related": [
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("/equipment-financing/articles/equipment-sale-leaseback-financing/", "Equipment sale-leaseback financing"),
            ("../equipment-equity-loan-vs-mca/", "Equipment equity loan vs MCA"),
            ("/commercial-truck-title-loan/articles/truck-title-loan-vs-sale-leaseback/", "Truck title loan vs sale-leaseback"),
        ],
        "sources": [IRS_946, IRS_544],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "equipment-equity-loan-vs-mca",
        "crumb": "Equity Loan vs MCA",
        "title": "Equipment Equity Loan vs Merchant Cash Advance | Axiant",
        "og_title": "Equipment Equity Loan vs Merchant Cash Advance",
        "h1": "Equipment Equity Loan vs Merchant Cash Advance",
        "headline": "Equipment Equity Loan vs Merchant Cash Advance",
        "lede": "Borrowing against machines you own, compared with an advance on future "
                "sales - for contractors who have both options",
        "meta_desc": "An MCA is fast and needs no collateral; an equipment equity loan "
                     "is secured by iron you own and is usually cheaper. How the cost, "
                     "payments and risks compare.",
        "article_desc": "How a loan secured by owned construction equipment compares "
                        "with a merchant cash advance on cost, payments and risk.",
        "keywords": "equipment loan vs merchant cash advance, contractor MCA "
                    "alternative, borrow against equipment instead of MCA",
        "quick_answer": "If you own equipment with equity, borrowing against it is "
                        "usually far cheaper than a merchant cash advance. MCAs are "
                        "priced by <strong>factor rate</strong> - commonly "
                        "<strong>1.15 to 1.50</strong> - and collected by daily or "
                        "weekly debits over a few months, while an equity loan "
                        "amortizes over <strong>24-72 months</strong>. The trade-off "
                        "is speed and paperwork: an MCA can fund in days, an equity "
                        "loan needs a valuation and a lien search first.",
        "sections": [
            ("How Each One Works",
             _table(["", "Equipment equity loan", "Merchant cash advance"], [
                 ["What it is", "A loan secured by machines you own", "A purchase of future sales or receivables"],
                 ["Pricing", "Interest rate over a term", "Factor rate on the amount advanced"],
                 ["Repayment", "Fixed monthly payments", "Daily or weekly debits"],
                 ["Typical term", "24-72 months", "A few months to about a year"],
                 ["Collateral", "The equipment, by UCC-1", "Usually none specific; often a blanket UCC"],
                 ["Speed", "Days to a few weeks", "Often days"],
             ])
             + "<p>The cost difference comes from the term as much as the price. An "
             "advance repaid over a few months concentrates the whole cost into a "
             "short window; an equity loan spreads a lower cost over years.</p>"),
            ("What a Factor Rate Costs",
             "<p>A factor rate is a multiplier, not an interest rate. A $50,000 "
             "advance at a 1.35 factor means $67,500 is repaid. Because it is repaid "
             "over months rather than years, the equivalent annual cost is far higher "
             "than the factor suggests - see "
             "<a href=\"/articles/factor-rate-vs-apr-business-loan-cost/\">factor rate "
             "vs APR</a> for how to convert one to the other.</p>"
             "<p>The daily or weekly debits are the other cost. On a contractor's "
             "uneven cash flow - big draws, then weeks waiting on the next one - a "
             "fixed daily debit can drain the account between progress payments.</p>"),
            ("When an MCA Still Makes Sense",
             "<ul>"
             "<li>You need money in days and there is no time for a valuation.</li>"
             "<li>You do not own equipment with meaningful equity.</li>"
             "<li>The need is small and short, and you know exactly where repayment "
             "comes from.</li>"
             "</ul>"
             "<p>Outside those cases, a contractor who owns paid-off machines is "
             "usually paying for speed with an MCA, not for access to capital.</p>"),
            ("What Each One Needs Before It Funds",
             "<p>Most of the speed difference comes from the paperwork, and most of "
             "it can be prepared before you need the money:</p>"
             + _table(["", "Equipment equity loan", "Merchant cash advance"], [
                 ["Bank statements", "Usually the last 3-6 months", "Usually the last 3-4 months"],
                 ["Collateral details", "Make, model, year, hours, serials, photos", "Not needed"],
                 ["Valuation", "Desktop or on-site appraisal", "Not needed"],
                 ["Lien search", "UCC search on the business", "Often, to see other advances"],
                 ["Existing debt", "Payoff letters for anything on the machines", "A list of current advances"],
             ])
             + "<p>A contractor who keeps a current equipment list with serials, "
             "hours and photos, and knows what liens are on file, can close an "
             "equity loan far closer to MCA speed. The valuation is usually the "
             "longest step, and a desktop valuation from good photos is often "
             "enough on smaller amounts.</p>"),
            ("Using Equipment Equity to Get Out of MCAs",
             "<p>If you are already carrying one or more advances, the equity in your "
             "equipment can sometimes pay them off and replace daily debits with one "
             "monthly payment. Two cautions:</p>"
             "<ul>"
             "<li><strong>Check the advance providers' UCC filings first.</strong> "
             "Many MCAs file blanket liens that already cover your equipment, which "
             "has to be resolved before a new lender can take first position.</li>"
             "<li><strong>Make sure the cash flow problem is fixed.</strong> "
             "Refinancing advances with equipment debt only helps if the business "
             "can carry the new payment without taking another advance.</li>"
             "</ul>"
             "<p>See <a href=\"/mca-consolidation-loan.html\">MCA consolidation "
             "secured by asset equity</a> for how that payoff is structured.</p>"),
            ("Red Flags in Either Offer",
             "<ul>"
             "<li>A cost quoted only as a factor rate or a \"low daily payment\", "
             "with no total repayment amount.</li>"
             "<li>Large fees deducted from the funds you receive but left out of the "
             "contract amount.</li>"
             "<li>A confession of judgment, or pressure to sign the same day.</li>"
             "<li>Claims of government affiliation or guaranteed approval.</li>"
             "</ul>"
             "<p>The Federal Trade Commission has brought cases over exactly these "
             "practices in small-business financing.</p>"),
        ],
        "faqs": [
            ("Is an equipment equity loan cheaper than an MCA?",
             "Usually much cheaper. MCAs are priced by a factor rate repaid over a "
             "few months, which works out to a far higher equivalent annual cost than "
             "a secured loan amortized over two to six years."),
            ("Can I use my equipment to pay off merchant cash advances?",
             "Often, if the equipment has enough equity and any blanket liens from "
             "the advance providers can be released or subordinated. The new loan "
             "pays the advances off and replaces the debits with one monthly payment."),
            ("Why does an MCA fund faster?",
             "Because it is underwritten mostly on bank deposits and does not need "
             "a valuation of collateral or a lien search. An equity loan does, which "
             "adds days to the process."),
            ("Does a merchant cash advance put a lien on my equipment?",
             "Many advance providers file a blanket UCC-1 covering all business "
             "assets, which includes equipment. Check the filings before assuming a "
             "machine is free and clear."),
        ],
        "related": [
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("/mca-consolidation-loan.html", "MCA consolidation secured by asset equity"),
            ("/articles/factor-rate-vs-apr-business-loan-cost/", "Factor rate vs APR"),
            ("../heavy-equipment-loan-with-an-existing-lien/", "Borrowing with an existing lien"),
        ],
        "sources": [CFPB, FTC],
    },
    # ------------------------------------------------------------------ 5
    {
        "slug": "what-happens-if-you-default-on-an-equipment-loan",
        "crumb": "If You Default",
        "title": "What Happens If You Default on an Equipment Loan | Axiant",
        "og_title": "What Happens If You Default on an Equipment Loan",
        "h1": "What Happens If You Default on an Equipment Loan",
        "headline": "What Happens If You Default on an Equipment Loan",
        "lede": "The sequence from a missed payment to repossession and sale, and the "
                "points where it can still be stopped",
        "meta_desc": "A secured equipment lender can repossess without a court order and "
                     "sell the machine, but must act commercially reasonably. What "
                     "happens, and how to stop it early.",
        "article_desc": "What a lender can do when an equipment-secured loan defaults, "
                        "and the borrower's options at each step.",
        "keywords": "equipment loan default, equipment repossession, UCC repossession "
                    "rules, deficiency balance equipment loan",
        "quick_answer": "If an equipment-secured loan defaults, the lender can "
                        "<strong>repossess the machine without a court order</strong> "
                        "as long as it avoids a breach of the peace, then sell it in a "
                        "<strong>commercially reasonable</strong> way after giving "
                        "notice. If the sale brings less than you owe, you can still "
                        "owe the <strong>deficiency</strong>, often under a personal "
                        "guarantee. The cheapest point to fix it is before the first "
                        "missed payment.",
        "sections": [
            ("The Sequence, Step by Step",
             "<ol>"
             "<li><strong>Missed payment.</strong> Most agreements allow a short grace "
             "period and a late fee before the loan is in default.</li>"
             "<li><strong>Default and acceleration.</strong> The agreement usually "
             "lets the lender declare the whole balance due once you are in default.</li>"
             "<li><strong>Repossession.</strong> Under the UCC a secured lender can "
             "take the collateral without going to court, provided it does so "
             "without a breach of the peace.</li>"
             "<li><strong>Notice of sale.</strong> Before selling, the lender must "
             "send notice of the planned disposition to the borrower and guarantors.</li>"
             "<li><strong>Sale.</strong> Every aspect of the sale - method, timing, "
             "place and terms - must be commercially reasonable.</li>"
             "<li><strong>Deficiency or surplus.</strong> Proceeds go to the costs of "
             "repossession and sale, then the debt. A shortfall can be pursued; a "
             "surplus goes back to you.</li>"
             "</ol>"),
            ("Heavy Equipment Is Easier to Repossess Than You Think",
             "<p>A machine parked on an open jobsite is reachable in a way a vehicle "
             "in a locked garage is not. Many equipment lenders also require GPS or "
             "telematics, so they know where the machine is. Owners sometimes assume "
             "a machine on a remote site is safe; it rarely is.</p>"
             "<p>What a lender cannot do is breach the peace - for example, by force, "
             "by threats, or over your objection at the time. If that happens, speak "
             "to a lawyer.</p>"),
            ("Why the Sale Price Matters to You",
             "<p>The sale of repossessed equipment is usually fast - often at auction "
             "- which is exactly why lenders lend against forced liquidation value. "
             "If that sale brings less than the balance plus costs, the difference "
             "is a <strong>deficiency</strong>, and most equipment loans to small "
             "businesses carry a personal guarantee that makes the owner liable for it.</p>"
             + _table(["", "Illustrative figure"], [
                 ["Balance owed at default", "$80,000"],
                 ["Repossession and sale costs", "$6,000"],
                 ["Auction proceeds", "$62,000"],
                 ["Deficiency still owed", "$24,000"],
             ])
             + "<p>A sale that was not commercially reasonable can reduce or "
             "eliminate a deficiency claim, which is one reason to keep every notice "
             "you receive.</p>"),
            ("Leases Default Differently From Loans",
             "<p>If the machine is <strong>leased</strong> rather than financed with "
             "a loan, the lessor already owns it. In a default the lessor typically "
             "takes the equipment back and claims the remaining lease payments "
             "under the agreement, rather than selling the machine to pay down a "
             "loan. Whether a leftover balance is owed, and how it is calculated, "
             "depends on the lease's default and early-termination terms.</p>"
             "<p>Some documents called leases - especially those with a nominal "
             "buyout, such as $1 - are treated as secured loans in substance, and the "
             "loan rules above then apply. Read which kind of agreement you signed "
             "before deciding how to handle a missed payment, because the exposure "
             "can be very different.</p>"),
            ("Cross-Default and Blanket Liens",
             "<p>A default on one loan can trigger defaults on others. Many "
             "agreements contain <strong>cross-default</strong> clauses, and a lender "
             "with a blanket lien may have a claim on more than the machine you "
             "fell behind on. Read the default section of every agreement you have "
             "signed before you decide which payment to miss.</p>"),
            ("Where You Can Still Stop It",
             "<ul>"
             "<li><strong>Before the first missed payment:</strong> call the lender. "
             "Deferrals, interest-only periods and re-amortizations are far easier "
             "to get before a default is on the record.</li>"
             "<li><strong>After default, before repossession:</strong> a refinance "
             "against other equity, or selling the machine yourself, usually "
             "recovers more than a forced sale.</li>"
             "<li><strong>After repossession, before the sale:</strong> you have the "
             "right to redeem the collateral by paying what is owed, including "
             "costs.</li>"
             "</ul>"
             "<p>If the problem is wider than one loan, see "
             "<a href=\"/business-debt-relief.html\">business debt relief options</a>.</p>"),
        ],
        "faqs": [
            ("Can an equipment lender repossess without a court order?",
             "Yes. Under the Uniform Commercial Code a secured lender may take the "
             "collateral after default without going to court, provided it does so "
             "without a breach of the peace."),
            ("Do I still owe money after the equipment is sold?",
             "You may. If the sale brings less than the balance plus the costs of "
             "repossession and sale, the lender can pursue the deficiency, often "
             "against the owner under a personal guarantee."),
            ("Does the lender have to tell me before it sells the machine?",
             "Generally yes. A secured lender must send notice of the planned "
             "disposition, and the sale itself must be commercially reasonable."),
            ("Can I get the equipment back after it is repossessed?",
             "Before it is sold, you generally have the right to redeem it by paying "
             "the full amount owed, including the lender's costs."),
        ],
        "related": [
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("/commercial-truck-title-loan/articles/what-happens-if-you-default-truck-title-loan/", "Defaulting on a truck title loan"),
            ("/business-debt-relief.html", "Business debt relief"),
            ("../equipment-equity-loan-vs-mca/", "Equipment equity loan vs MCA"),
        ],
        "sources": [UCC_9609, UCC_9610, UCC_9615, UCC_9623],
    },
]
