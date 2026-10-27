# -*- coding: utf-8 -*-
"""Electrical contractor financing - rewrite of an existing page (AEO Batch 3).

The page at construction-business-financing/electrical-contractor-financing/
was hand-published on 2026-03-31 with no Quick Answer, no numbers and no
sources. Search Console showed 747 impressions at position 25.5 for
"electrical contractor funding". Same URL; date_published keeps the original.

The folder has no Articles index, so the cluster sets no_hub: the renderer
drops the "Articles" crumb and build-cluster skips the hub.

Ranges are described as conventional across lenders, never as anyone's quote,
and every one is a range the site already publishes (line of credit rates
page, invoice factoring, cargo van and bucket truck pages, retainage spoke,
working capital pillar). No funded totals, no testimonials, no named-lender
rates. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
"""
from cluster_security_guard import SBA_7A, IRS_946, FTC

CLUSTER = {
    "pillar": "construction-business-financing.html",
    "hub": "construction-business-financing",
    "no_hub": True,
    "crumb": "Construction Business Financing",
    "cta_inline": "See what your jobs and receivables support",
    "cta_button": "Get Matched for Electrical Contractor Financing",
}

FAR_PROMPT_PAY = ("https://www.acquisition.gov/far/52.232-27",
                  "FAR 52.232-27: Prompt Payment for Construction Contracts",
                  "Federal construction progress payments are due 14 days after "
                  "a proper payment request, and the prime must pay its "
                  "subcontractors within 7 days of being paid.")
FAR_BONDS = ("https://www.acquisition.gov/far/28.102-1",
             "FAR 28.102-1: Bonds for Construction Contracts (Miller Act)",
             "Performance and payment bonds are required on federal "
             "construction contracts over $150,000.")

ARTICLES = [
    {
        "slug": "electrical-contractor-financing",
        "date_published": "2026-03-31",
        "crumb": "Electrical Contractor Financing",
        "title": "Electrical Contractor Funding: Rates and Options | Axiant",
        "og_title": "Electrical Contractor Financing and Funding: Rates, Terms and Options",
        "h1": "Electrical Contractor Financing and Funding: Rates, Terms and Options",
        "headline": "Electrical Contractor Financing and Funding: Rates, Terms and Options",
        "lede": "Payroll weekly, pay apps monthly, retainage at closeout - which "
                "funding fits service work, project work and new vans, and what "
                "each typically costs",
        "meta_desc": "Electrical contractor funding compared: lines of credit "
                     "about 8-13% APR at banks, factoring advances of 80-95%, van "
                     "and bucket truck loans about 6-15%. Retainage, pay apps and "
                     "what lenders check.",
        "article_desc": "How electrical contractors fund payroll, materials, "
                        "retainage and vehicles, with typical rates and terms for "
                        "each option.",
        "keywords": "electrical contractor funding, electrical contractor "
                    "financing, electrician business loan, electrical contractor "
                    "line of credit, bucket truck financing",
        "quick_answer": "Electrical contractors usually fund two different needs "
                        "two different ways. Payroll and materials between pay apps "
                        "go on a <strong>line of credit</strong> (commonly about "
                        "<strong>8-13% APR</strong> at banks, 14-30%+ online) or "
                        "<strong>invoice factoring</strong> (advances of commonly "
                        "<strong>80-95%</strong> of approved invoices). Vans and "
                        "bucket trucks go on <strong>equipment loans</strong>, "
                        "commonly about <strong>6-15%</strong> over 36-72 months. "
                        "These are typical ranges across lenders, not a quote.",
        "sections": [
            ("Electrical Contractor Funding at a Glance",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Need</th><th>Usual fit</th><th>Typical range</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Need">Recurring payroll gaps</td>'
             '<td data-label="Usual fit">Business line of credit</td>'
             '<td data-label="Typical range">About 8-13% APR at banks; 14-30%+ '
             "online</td></tr>"
             '<tr><td data-label="Need">Slow commercial invoices</td>'
             '<td data-label="Usual fit">Invoice factoring</td>'
             '<td data-label="Typical range">80-95% advance; fee about 1-5% of '
             "invoice value</td></tr>"
             '<tr><td data-label="Need">One project ramp</td>'
             '<td data-label="Usual fit">Working capital loan</td>'
             '<td data-label="Typical range">From $10,000; funds in about 48 '
             "hours to 1 week once approved</td></tr>"
             '<tr><td data-label="Need">Service vans</td>'
             '<td data-label="Usual fit">Equipment loan or lease</td>'
             '<td data-label="Typical range">About 6-15%; 36-72 months; 0-20% '
             "down</td></tr>"
             '<tr><td data-label="Need">Bucket trucks</td>'
             '<td data-label="Usual fit">Equipment loan or lease</td>'
             '<td data-label="Typical range">About 6-15%; 24-72 months; truck '
             "and aerial unit financed together</td></tr>"
             '<tr><td data-label="Need">Buying a shop or building</td>'
             '<td data-label="Usual fit">SBA 7(a)</td>'
             '<td data-label="Typical range">Up to $5 million</td></tr>'
             "</tbody></table></div>"
             "<p>The ranges are those conventional across lenders, not anyone's "
             "quote. Credit, time in business, revenue and who your customers are "
             "decide where in each range you land.</p>"),
            ("Service Work and Project Work Need Different Money",
             "<p><strong>Service work</strong> (repairs, panel upgrades, "
             "maintenance contracts) turns fast. Tickets are small, customers pay "
             "within days or weeks, and the cash need is a steady float for parts "
             "and payroll. A revolving line fits because the same small gap opens "
             "and closes every week.</p>"
             "<p><strong>Project work</strong> (new construction, tenant "
             "improvements, commercial fit-outs) turns slowly. You buy wire, gear "
             "and fixtures up front, bill a monthly pay application, wait for the "
             "general contractor to be paid by the owner, and then have part of "
             "every payment held back as retainage. The gap is larger, longer and "
             "tied to specific jobs.</p>"
             "<p>Lenders judge service revenue on deposit consistency and project "
             "revenue on backlog and receivables concentration, so show the two "
             "streams separately. For the project gap, see "
             '<a href="/construction-business-financing/progress-payment-cash-flow-gaps/">'
             "cash flow gaps between progress payments</a>.</p>"),
            ("Retainage, Pay Apps and Federal Work",
             "<p>Retainage is the share of each progress payment held until the "
             "job is complete, commonly <strong>5-10%</strong>. On one job it is a "
             "nuisance. Across several jobs running at once it becomes a large "
             "balance you have earned but cannot spend, released only at "
             "closeout and sometimes later. Our "
             '<a href="/construction-business-financing/retainage-cash-flow-gap/">'
             "retainage guide</a> covers how to price and plan for it.</p>"
             "<p>Federal jobs follow fixed timing rules. Under "
             '<a href="https://www.acquisition.gov/far/52.232-27" rel="noopener nofollow" '
             'target="_blank">FAR 52.232-27</a>, a federal agency\'s construction '
             "progress payment is due 14 days after it receives a proper payment "
             "request, and the prime contractor must pay its subcontractors within "
             "7 days of being paid. Federal construction contracts over $150,000 "
             "also require payment bonds under the Miller Act, which gives "
             "unpaid subs and suppliers a claim against the bond rather than the "
             "project. Private and state work follows state prompt-payment and "
             "lien laws, which vary.</p>"
             "<p>Factoring and lines of credit both work around pay-app timing, "
             "but check two things first: whether your subcontract prohibits "
             "assigning receivables, and whether a blanket UCC filing from an "
             "earlier lender already covers them. Subcontractors waiting on a "
             "general contractor should also read "
             '<a href="/construction-business-financing/working-capital-subcontractors-invoices/">'
             "working capital for subcontractors between invoices</a>.</p>"),
            ("Vans, Bucket Trucks and Field Equipment",
             "<p>Vehicles are the largest asset most electrical firms buy, and "
             "they should be financed as assets, over their working life, not out "
             "of the operating line.</p>"
             "<ul>"
             "<li><strong>Cargo and service vans</strong> commonly run about "
             "$35,000-$75,000 before upfit. Used vans often trade 25-45% below "
             "comparable new pricing. See "
             '<a href="/equipment/cargo-vans/">cargo van financing</a>.</li>'
             "<li><strong>Bucket trucks</strong> commonly run $100,000-$200,000 "
             "or more, with the chassis and aerial device financed together. Used "
             "units commonly cost 30-50% less. See "
             '<a href="/equipment/bucket-trucks/">bucket truck financing</a>.</li>'
             "</ul>"
             "<p>Equipment financed this way is generally depreciable, and Section "
             "179 may let you deduct much of the cost in the first year; check "
             '<a href="https://www.irs.gov/publications/p946" rel="noopener nofollow" '
             'target="_blank">IRS Publication 946</a> and your accountant for the '
             "current limits.</p>"),
            ("Worked Example: A Commercial Fit-Out",
             "<p><strong>Illustrative numbers, not a quote.</strong> An electrical "
             "subcontractor wins a five-month commercial fit-out with monthly pay "
             "applications of $80,000 and 10% retainage. Field payroll runs "
             "$18,000 a week.</p>"
             "<ul>"
             "<li>The first pay app goes in at the end of month one. If the general "
             "contractor pays about 30 days later, the firm carries roughly eight "
             "weeks of payroll, about <strong>$144,000</strong>, before any money "
             "arrives, plus the material buys.</li>"
             "<li>Each payment arrives as $72,000, because $8,000 is held as "
             "retainage. By the last pay app, <strong>$40,000</strong> is held "
             "and is not released until closeout.</li>"
             "</ul>"
             "<p>A sensible structure here is a line of credit sized to the "
             "payroll gap, drawn as the job ramps and paid down as pay apps "
             "clear, or factoring on approved pay apps if the line is too small.</p>"),
            ("What Lenders Check in an Electrical File",
             "<ul>"
             "<li><strong>Bank statements</strong>, usually 3-6 months, for "
             "deposit consistency and existing payments.</li>"
             "<li><strong>AR aging and backlog</strong>, including who your "
             "general contractors are and how much of your receivables sit with "
             "one of them.</li>"
             "<li><strong>A debt schedule</strong> covering vehicle notes, "
             "equipment loans and any merchant cash advances.</li>"
             "<li><strong>License and insurance in good standing</strong>, which "
             "lenders read as a sign jobs will keep closing and paying.</li>"
             "<li><strong>A specific use of funds</strong>, tied to jobs, hires or "
             "vehicles, rather than \"working capital\" alone.</li>"
             "</ul>"
             "<p>Apply before the squeeze shows; the "
             '<a href="/construction-business-financing/contractor-financing-mistakes-delay-deny-funding/">'
             "contractor financing mistakes guide</a> lists the most common "
             "delays.</p>"),
            ("How to Choose and Apply",
             "<ol>"
             "<li><strong>Name the bottleneck.</strong> A recurring timing gap, a "
             "one-off project ramp and a vehicle purchase are three different "
             "loans.</li>"
             "<li><strong>Size it from your numbers.</strong> Use weekly payroll, "
             "your average days to payment and the retainage you are carrying, "
             "not a round figure.</li>"
             "<li><strong>Check your contracts</strong> for assignment clauses "
             "before counting on factoring.</li>"
             "<li><strong>Gather the file</strong>: bank statements, AR aging, "
             "backlog, debt schedule and quotes for any vehicles.</li>"
             "<li><strong>Compare total cost</strong>, including fees, guarantees "
             "and prepayment terms, not just the rate.</li>"
             "</ol>"
             "<p>When you are ready, "
             '<a href="/match.html">get matched with lenders that finance '
             "electrical contractors</a>. One application covers lines of credit, "
             "factoring, working capital and equipment. For the wider picture, "
             'see <a href="/construction-business-financing.html">construction '
             "business financing</a>.</p>"),
        ],
        "faqs": [
            ("What is the best funding for an electrical contractor?",
             "It depends on the need. A line of credit usually fits recurring "
             "payroll and material gaps, invoice factoring fits slow commercial "
             "invoices, a working capital loan fits a one-off project ramp, and "
             "equipment financing fits vans, bucket trucks and field equipment."),
            ("What interest rate do electrical contractors pay?",
             "Commonly about 8-13% APR on bank lines of credit and 14-30%+ online, "
             "and about 6-15% on van and bucket truck loans. Factoring is priced "
             "as a fee of about 1-5% of invoice value. These are typical ranges "
             "across lenders, not a quote."),
            ("Can an electrical subcontractor factor pay applications?",
             "Often, if the pay app is approved and the subcontract does not "
             "prohibit assigning receivables. Funders commonly advance 80-95% and "
             "look mostly at the general contractor's and owner's ability to pay."),
            ("How does retainage affect an electrician's cash flow?",
             "Retainage holds back commonly 5-10% of each progress payment until "
             "the job is complete. Across several jobs it becomes a large balance "
             "you have earned but cannot use, so plan financing around it."),
            ("How fast must a federal prime contractor pay an electrical sub?",
             "Under FAR 52.232-27, within 7 days of receiving payment from the "
             "agency. The agency's own progress payment is due 14 days after it "
             "receives a proper payment request."),
            ("Can electrical contractors finance bucket trucks and vans?",
             "Yes. Vans and bucket trucks are commonly financed over about 24-72 "
             "months with 0-20% down, and the bucket truck's chassis and aerial "
             "device are financed together."),
        ],
        "related": [
            ("/construction-business-financing.html", "Construction business financing"),
            ("/construction-business-financing/retainage-cash-flow-gap/",
             "The retainage cash flow gap"),
            ("/construction-business-financing/working-capital-subcontractors-invoices/",
             "Working capital for subcontractors between invoices"),
            ("/business-line-of-credit.html", "Business line of credit"),
            ("/invoice-factoring.html", "Invoice factoring"),
            ("/equipment/bucket-trucks/", "Bucket truck financing"),
        ],
        "sources": [FAR_PROMPT_PAY, FAR_BONDS, IRS_946, SBA_7A, FTC],
    },
]
