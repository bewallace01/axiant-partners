# -*- coding: utf-8 -*-
"""Startup business loans for veterans - new spoke under startup-financing/articles/.

Search Console (Aug-Nov 2026): 287 impressions at about position 70, nearly all on the
general /veteran-business-loans.html, 0 clicks. That page and the MREIDL guide stay
untouched. This page is for a veteran starting from zero, and says plainly that startups
are hard to place. SBA rules read from SOP 50 10 8.1 on 2026-11-05. Worked example fee from
the FY2027 notice as reported by NAGGL. No funded totals, no testimonials.
"""
from cluster_table import table
from sba_sources import SOP, FEES, SBA_7A

MICRO = ("https://www.sba.gov/funding-programs/loans/microloans", "SBA Microloans",
         "Loans of up to $50,000 through nonprofit intermediaries, with a maximum term of seven years.")
VBOC = ("https://www.sba.gov/local-assistance/resource-partners/veterans-business-outreach-center-vboc-program",
        "SBA Veterans Business Outreach Centers",
        "SBA-backed centers offering business training and counseling to veterans and military spouses.")
B2B = ("https://www.sba.gov/sba-learning-platform/boots-business", "SBA Boots to Business",
       "The SBA's entrepreneurship training for service members, veterans and military spouses.")
VOB = ("https://www.sba.gov/business-guide/grow-your-business/veteran-owned-businesses",
       "SBA: Veteran-owned businesses", "SBA's guide to programs, certification and support for veteran-owned firms.")

CLUSTER = {
    "pillar": "startup-financing.html",
    "hub": "startup-financing/articles",
    "no_hub": True,
    "crumb": "Startup Financing",
    "cta_inline": "See what your startup could qualify for",
    "cta_button": "Get Matched for Startup Financing",
}

ARTICLES = [{
    "slug": "startup-business-loans-for-veterans",
    "crumb": "Startup Business Loans for Veterans",
    "title": "Startup Business Loans for Veterans: Options | Axiant",
    "og_title": "Startup Business Loans for Veterans: What You Can Realistically Get",
    "h1": "Startup Business Loans for Veterans: What You Can Realistically Get",
    "headline": "Startup Business Loans for Veterans: What You Can Realistically Get",
    "lede": "Serving helps with fees and support, but it doesn't replace a down payment or a "
            "plan. An honest look at what lenders fund for a brand-new business",
    "meta_desc": "Startup business loans for veterans: SBA Express fee waivers, 10% equity on 7(a) start-ups, microloans up to $50,000, and why startups are hard to place.",
    "article_desc": "Realistic startup funding options for veterans, including SBA 7(a), "
                    "microloans, equipment financing and free support programs.",
    "keywords": "startup business loans for veterans, loans for veterans to start a business, "
                "veteran startup loans, sba loans for veterans starting a business",
    "quick_answer": "No federal loan program funds veteran startups just for having served, and "
                    "startups are hard to place. The usual routes are <strong>SBA microloans up "
                    "to $50,000</strong>, or an SBA 7(a) loan with at least <strong>10% equity</strong> "
                    "from you. SBA Express waives its upfront fee for eligible veteran-owned firms. "
                    "Axiant Partners, a business-loan broker in Boca Raton, can tell you which fits. "
                    "Credit expectations are typical lender practice, not a quote.",
    "sections": [
        ("Being a Veteran Helps, but Not the Way Most People Expect",
         "<p>There's a common belief that veterans can get a special startup loan or a grant "
         "just for having served. The SBA's old Patriot Express program is gone, and lenders apply "
         "the same repayment tests to you as anyone else. What service does get you is real, "
         "though more modest:</p>"
         "<ul>"
         "<li><strong>Lower cost on some loans.</strong> "
         '<a href="https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs" '
         'rel="noopener nofollow" target="_blank">SBA SOP 50 10 8.1</a> waives the upfront fee on '
         "SBA Express loans (up to $500,000) to businesses owned and controlled by eligible "
         "veterans, certain transitioning service members and spouses.</li>"
         "<li><strong>Priority handling.</strong> The SBA prioritizes veteran-owned applications "
         "it processes itself and encourages lenders to give them special consideration. That can "
         "mean speed, but it doesn't change approval standards.</li>"
         "<li><strong>Free help.</strong> "
         '<a href="https://www.sba.gov/local-assistance/resource-partners/veterans-business-outreach-center-vboc-program" '
         'rel="noopener nofollow" target="_blank">Veterans Business Outreach Centers</a> and '
         '<a href="https://www.sba.gov/sba-learning-platform/boots-business" rel="noopener nofollow" '
         'target="_blank">Boots to Business</a> can help you build a plan a lender can use.</li>'
         "</ul>"
         "<p>Your service record helps in conversation, but it doesn't replace cash, credit or relevant "
         "experience. For veteran-owned "
         'companies already operating, see <a href="/veteran-business-loans.html">veteran business '
         "loans</a>, which covers more choices.</p>"),
        ("Your Realistic Options at the Start",
         table(["Option", "Typical amount", "What it takes", "Honest read"], [
             ["SBA microloan", "Up to $50,000", "Business plan, some collateral, intermediary's criteria", "The most realistic first loan for many startups"],
             ["SBA 7(a), including Express", "Up to $5M; Express up to $500K", "At least 10% equity, good credit, industry experience", "Possible, but few lenders want true startups"],
             ["Equipment financing", "The machine's value", "Strong personal credit, often money down", "Good if equipment is the main cost"],
             ["Buying a business", "Varies", "10% equity under SBA rules, plus cash flow history", "Often easier than a startup because there's a track record"],
             ["Franchise", "Varies", "Equity, credit, brand on the SBA directory", "Lenders like a known model and may be more willing"],
         ])
         + "<p>Be careful with a merchant cash advance or a personal credit card used as your "
         "startup plan. A brand-new company has no sales to support daily debits. And SBA loans "
         "can't simply fund an idea with no plan behind it: lenders review your projections, "
         "assumptions and experience closely.</p>"),
        ("Why Startups Are Hard to Place",
         "<p>A lender's first question is how the loan gets repaid. An existing business can show "
         "tax returns. A startup has only a forecast, and many lenders we work with don't lend on "
         "projections alone. The SBA doesn't ban startup loans, but individual lenders can set "
         "tighter rules, which is why one bank's no may not be the final answer.</p>"
         "<p>These are what usually tip the decision, framed as common lender practice rather than "
         "fixed rules:</p>"
         "<ul>"
         "<li><strong>Experience in that industry.</strong> A former aircraft mechanic opening a "
         "repair shop reads very differently from one opening a restaurant.</li>"
         "<li><strong>Personal credit.</strong> Many SBA lenders look for roughly 650-680 or higher.</li>"
         "<li><strong>Cash you've saved.</strong> SBA rules require equity, and more than the "
         "minimum makes you stronger.</li>"
         "<li><strong>Outside income.</strong> Retirement or disability income, or a spouse's job, "
         "can show you can survive the first year. Ask how a lender treats it.</li>"
         "<li><strong>Signed customers.</strong> A letter of intent or a contract can carry real "
         "weight, especially in government work.</li>"
         "</ul>"),
        ("The 10% Equity Rule and Where the Money Can Come From",
         "<p>Under SOP 50 10 8.1, a business that has operated for one year or less counts as a "
         "start-up, and every 7(a) start-up loan needs an equity injection of at least 10% of the "
         "total project cost. That means all costs needed to become operational, whichever source "
         "pays for them, except lines of credit and 504 loans.</p>"
         "<ul>"
         "<li><strong>Acceptable:</strong> cash that isn't borrowed, including from savings or a "
         "documented gift.</li>"
         "<li><strong>Possibly acceptable:</strong> debt on full standby, meaning no principal or "
         "interest payments for the term of the 7(a) loan. Ask your lender how much it counts.</li>"
         "<li><strong>Who can own the company:</strong> the SOP requires all direct and indirect owners and "
         "required guarantors to be U.S. citizens or nationals who live in the U.S. or its "
         "territories.</li>"
         "</ul>"
         "<p>Note that a VA home loan is for a home, not a business. If you're thinking of "
         "borrowing against your house for equity, ask the lender first, and consider what happens "
         "to your family if the business fails.</p>"),
        ("Worked Example: Opening a $145,000 Shop",
         "<p><strong>Illustrative numbers, not a quote.</strong> A veteran with ten years of relevant "
         "experience opens a shop needing $140,000 for buildout, equipment and early expenses, "
         "plus about $5,000 in closing costs. With an estimated guaranty fee of about $2,250, the "
         "total project comes to about $147,250.</p>"
         + table(["Item", "Amount"], [
             ["Total project cost", "About $147,250"],
             ["Veteran's equity (10%)", "About $14,725"],
             ["SBA 7(a) loan", "About $132,500"],
             ["Assumed rate and term", "11%, 10 years"],
             ["Monthly payment", "About $1,826"],
         ])
         + "<p>On that structure, the business has to produce about $1,826 a month plus a cushion "
         "before the owner takes a paycheck, starting close to day one. The guaranty fee is figured "
         "using 2% of the 85% guaranteed share for loans of $150,000 or less, per the "
         '<a href="https://www.naggl.org/sba-issues-notices-announcing-fy-2027-7a-and-504-loan-program-fees/" '
         'rel="noopener nofollow" target="_blank">FY2027 fee notice</a>; an SBA Express loan to an '
         "eligible veteran wouldn't carry it. Keep several months of operating cash outside the "
         "loan, because a line of credit is hard to get right after opening.</p>"),
        ("What to Do Before You Apply",
         "<ol>"
         "<li><strong>Talk to a VBOC or SCORE mentor.</strong> It's free, and a sharper plan helps "
         "with any lender.</li>"
         "<li><strong>Write down the numbers.</strong> Include startup costs, monthly costs and how "
         "you'll live during the first year.</li>"
         "<li><strong>Check your credit.</strong> Fix errors now, since you can't correct them in a "
         "hurry mid-application.</li>"
         "<li><strong>Gather your DD-214.</strong> Lenders and the SBA may need proof of veteran status.</li>"
         "<li><strong>Consider buying instead of starting.</strong> An existing business has cash flow "
         "to underwrite; see <a href=\"/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/\">"
         "buying a business with 5% down</a>.</li>"
         "<li><strong>Apply to lenders that do startups.</strong> That's where a broker helps most. "
         '<a href="/match.html">Get matched</a>, or read <a href="/startup-financing/articles/how-to-qualify-for-startup-financing/">'
         "how to qualify for startup financing</a>.</li>"
         "</ol>"
         "<p>Selling to the government later? Learn about "
         '<a href="https://www.sba.gov/business-guide/grow-your-business/veteran-owned-businesses" '
         'rel="noopener nofollow" target="_blank">veteran-owned certification</a> once you\'re '
         "operating. It can open set-aside contracts. "
         'See <a href="/startup-financing.html">startup financing</a> for non-veteran routes.</p>'),
    ],
    "faqs": [
        ("Are there startup business loans just for veterans?",
         "Not as a separate federal loan program. Veterans use the same SBA and private options as "
         "other owners, with benefits such as an upfront fee waiver on SBA Express loans and priority "
         "handling when the SBA processes the application itself."),
        ("Can a veteran get an SBA loan with no money down to start a business?",
         "Generally no. SOP 50 10 8.1 requires at least 10% equity on a 7(a) loan to a start-up, based "
         "on total project cost. Some of this may be able to come from debt on full standby, which your "
         "lender would need to review."),
        ("What credit score do veterans need for a startup loan?",
         "There isn't a single veteran standard. Many SBA lenders look for roughly 650-680 or higher, "
         "while microloan intermediaries set their own criteria. These are typical ranges, not a quote."),
        ("Does the VA give business loans?",
         "A VA home loan is for housing, so don't plan on it for a company. For business lending, "
         "veterans generally go through SBA programs and private lenders."),
        ("Can I get a grant instead of a loan?",
         "Small-business grants exist, but they're competitive and rarely enough to fund a startup. Be "
         "suspicious of anyone charging a fee to get you a grant, and treat grants as a bonus."),
        ("Is it easier to buy a business than start one?",
         "Often, because the business has tax returns a lender can underwrite. SBA rules still require "
         "at least 10% equity on a typical first acquisition, and half of that may come from a seller "
         "note on full standby."),
    ],
    "related": [
        ("/veteran-business-loans.html", "Veteran business loans"),
        ("/startup-financing.html", "Startup financing"),
        ("/startup-financing/articles/sba-microloan-startup-approval-guide/", "SBA microloans for startups"),
        ("/sba-loans/articles/veterans-business-loans-sba-mreidl/", "Veteran SBA loans and MREIDL"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buying a business with 5% down"),
        ("/startup-financing/articles/startup-financing-no-revenue-options/", "Startup financing with no revenue"),
    ],
    "sources": [SOP, MICRO, FEES, VBOC, B2B, VOB, SBA_7A],
}]
