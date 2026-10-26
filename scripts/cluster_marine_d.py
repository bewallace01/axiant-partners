# -*- coding: utf-8 -*-
"""Commercial marine financing, articles 6-7: the companion citation pages (AEO
plan 2e). Imported by cluster_marine.

The money page converts (6 leads, 4 apps) but has almost no outside links and is
rarely what an assistant quotes; these answer the questions asked around it -
what a commercial vessel loan costs, and loan vs lease.

Rules as cluster_marine: ranges are conventional across lenders, never anyone's
quote; no funded totals, no testimonials, no named-lender rates. Facts specific
to these pages: the preferred ship mortgage on documented vessels (46 U.S.C.
31322), owner-citizenship rules behind coastwise and fishery endorsements (46
U.S.C. 12112-12113), and commercial vessels as 10-year MACRS property (IRS Pub
946, asset class 00.28).
"""
from cluster_marine import USCG_NVDC, SBA_7A, FTC

PSM = ("https://www.law.cornell.edu/uscode/text/46/31322",
       "46 U.S.C. &sect; 31322: Preferred Mortgages",
       "The statute that makes a recorded mortgage on a documented vessel a "
       "preferred ship mortgage - the lender's lien in a vessel loan.")
FISHERY = ("https://www.law.cornell.edu/uscode/text/46/12113",
           "46 U.S.C. &sect; 12113: Fishery Endorsement",
           "Owner eligibility for a fishery endorsement, including the U.S. "
           "citizenship rules a lease or financing structure has to respect.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "MACRS recovery periods, including vessels, barges and tugs (asset class "
           "00.28), and how leases are treated.")


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


MORE = [
    # ------------------------------------------------------------------ 7
    {
        "slug": "commercial-vessel-loan-vs-marine-lease",
        "crumb": "Vessel Loan vs Marine Lease",
        "title": "Commercial Vessel Loan vs Marine Lease | Axiant",
        "og_title": "Commercial Vessel Loan vs Marine Lease",
        "h1": "Commercial Vessel Loan vs Marine Lease",
        "headline": "Commercial Vessel Loan vs Marine Lease: Which Fits Your Operation",
        "lede": "Owning with a preferred ship mortgage or leasing from a lessor - what "
                "changes for title, endorsements, taxes and the end of the term",
        "meta_desc": "A vessel loan makes you the owner, with a preferred ship mortgage "
                     "on the vessel. A lease leaves the lessor as owner. How endorsements, "
                     "taxes and buyouts differ.",
        "article_desc": "How a commercial vessel loan and a marine lease differ, and "
                        "which suits charter, fishing and workboat operations.",
        "keywords": "commercial vessel loan vs lease, marine equipment lease, boat lease "
                    "vs loan commercial, bareboat charter vs vessel loan",
        "quick_answer": "With a <strong>vessel loan</strong> you own the boat and the "
                        "lender records a <strong>preferred ship mortgage</strong> (or a "
                        "state lien on a smaller, titled vessel). With a <strong>marine "
                        "lease</strong> the lessor owns it and you pay to use it, with a "
                        "buyout or return at the end. Axiant Partners, a business-loan "
                        "broker in Boca Raton, finds the deciding question is often "
                        "<strong>who has to own the vessel</strong> for its endorsements "
                        "and permits.",
        "sections": [
            ("Side by Side",
             _table(["", "Vessel loan", "Marine lease"], [
                 ["Owner", "You", "The lessor"],
                 ["Lender's security", "Preferred ship mortgage or state lien", "Ownership itself"],
                 ["End of term", "Mortgage released", "Buy out, renew or return"],
                 ["Depreciation", "Yours", "The lessor's (true lease)"],
                 ["Survey required", "Yes", "Yes"],
                 ["Endorsements", "In your name", "Depend on the lessor's eligibility"],
             ])
             + "<p>A $1-buyout lease is, in substance, a purchase with lease paperwork; "
             "a fair-market-value lease is closer to renting. A bareboat (demise) "
             "charter is a third form: you take full control of the vessel and crew it, "
             "but the owner keeps title.</p>"),
            ("How the Lender Secures a Loan",
             "<p>On a vessel documented with the Coast Guard, the lender records a "
             "<strong>preferred ship mortgage</strong> with the National Vessel "
             "Documentation Center. Federal law gives that mortgage strong priority, "
             "which is why lenders often prefer documentation on larger commercial "
             "vessels. Smaller vessels titled by a state carry the lien on the state "
             "title instead, much like a truck.</p>"
             "<p>Either way you are the owner of record, the vessel's certificate and "
             "endorsements are in your name, and the lien comes off when the loan is "
             "paid. What lenders ask for before they record anything is covered in "
             "<a href=\"../commercial-vessel-loan-requirements/\">commercial vessel loan "
             "requirements</a>.</p>"),
            ("Endorsements and Permits: Who Owns It Matters",
             "<p>This is where marine leasing differs most from leasing a truck or a "
             "machine. A vessel's <strong>coastwise</strong> and <strong>fishery</strong> "
             "endorsements carry U.S. citizenship requirements for the owner, and the "
             "fishery endorsement's are the strictest. In a lease, the lessor is the "
             "owner, so the structure has to fit those rules or the vessel may not be "
             "able to work in the trade you need it for.</p>"
             "<p>Fishing permits and quota add another layer: they are often worth as "
             "much as the hull, are tied to the vessel or the permit holder under "
             "fishery rules, and may not move with a lease the way you expect. See "
             "<a href=\"../commercial-fishing-vessel-financing/\">commercial fishing "
             "vessel financing</a>. Have a maritime attorney review any lease or "
             "charter on an endorsed vessel before you sign.</p>"),
            ("Taxes: Who Gets the Deduction",
             "<p>With a loan or a $1-buyout lease you are generally treated as the "
             "owner and depreciate the vessel. Commercial vessels, barges and tugs are "
             "generally 10-year property under MACRS (IRS Publication 946, asset class "
             "00.28), and may qualify for Section 179 or bonus depreciation in the year "
             "placed in service. With a true lease the lessor owns the vessel and your "
             "lease payments are generally deductible instead.</p>"
             "<p>Which is worth more depends on your tax position that year. Confirm "
             "with your accountant before choosing a structure for tax reasons.</p>"),
            ("Which One Fits",
             _table(["Operation", "Usually leans", "Why"], [
                 ["Fishing, endorsed vessel", "Loan", "Ownership keeps endorsements simple"],
                 ["Charter, long-term vessel", "Loan", "Equity builds; no return conditions"],
                 ["Workboat, fixed contract", "Lease or loan", "Match the term to the contract"],
                 ["Fleet you upgrade often", "FMV lease", "Hand back and replace"],
             ])
             + "<p>A lease can also fit when the down payment is the obstacle, but "
             "check what the lessor requires at return - hull condition, engine hours "
             "and survey - because those conditions can cost more than the deposit "
             "saved.</p>"),
            ("Questions to Ask Before You Sign Either",
             "<ul>"
             "<li><strong>What is the total of payments</strong>, plus any buyout or "
             "balloon?</li>"
             "<li><strong>Who arranges the survey</strong>, and how recent must it be?</li>"
             "<li><strong>For a lease:</strong> what are the return conditions, and can "
             "the vessel work in every trade you need?</li>"
             "<li><strong>For a loan:</strong> is there a prepayment penalty?</li>"
             "<li><strong>Insurance:</strong> hull and P&amp;I coverage naming the "
             "lender or lessor.</li>"
             "</ul>"
             "<p>Before either, the vessel will be surveyed: see "
             "<a href=\"../marine-survey-what-lenders-require/\">what a marine survey "
             "covers for a lender</a>. For SBA as an alternative on larger purchases, see "
             "<a href=\"/sba-loans.html\">SBA loans</a>.</p>"),
        ],
        "faqs": [
            ("Is it better to lease or finance a commercial boat?",
             "Finance when you will keep the vessel and need its endorsements in your "
             "name; consider a lease when you upgrade often or the down payment is the "
             "obstacle. Compare total of payments plus buyout either way."),
            ("What is a preferred ship mortgage?",
             "A mortgage recorded against a Coast Guard documented vessel that federal "
             "law treats as a preferred lien. It is how a lender secures a loan on a "
             "documented commercial vessel."),
            ("Can a leased vessel keep its fishery endorsement?",
             "Only if the ownership structure meets the endorsement's citizenship "
             "rules, which are strict for fishery endorsements. Have a maritime "
             "attorney review the lease before signing."),
            ("What is a bareboat charter?",
             "A charter in which you take full control of the vessel and provide the "
             "crew, while the owner keeps title. It works much like a lease."),
            ("How are commercial vessels depreciated?",
             "Generally as 10-year MACRS property (IRS Publication 946, asset class "
             "00.28) when you own the vessel. With a true lease, the lessor depreciates "
             "it."),
        ],
        "related": [
            ("/commercial-marine-financing.html", "Commercial marine financing"),
            ("../marine-survey-what-lenders-require/", "What a marine survey covers for a lender"),
            ("/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/", "Equipment leasing vs loan"),
            ("/match.html", "Get matched"),
        ],
        "sources": [PSM, FISHERY, IRS_946, USCG_NVDC],
    },
]
