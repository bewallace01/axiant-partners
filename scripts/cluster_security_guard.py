# -*- coding: utf-8 -*-
"""Security guard company financing - 4 articles. Plan priority 5.

The pillar was already 2,463 words but was not registered in INDUSTRIES, so it
never appeared on the industries hub. That is fixed in the same change.

Ranges are described as conventional across lenders, never quoted as anyone's
terms. No funded totals, no years in business, no testimonials, no invented
figures. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
"""

from cluster_table import table

CLUSTER = {
    "pillar": "security-guard-business-financing.html",
    "hub": "security-guard-business-financing/articles",
    "crumb": "Security Guard Company Financing",
    "cta_inline": "See what your contracts support",
    "cta_button": "Get Matched for Guard Company Financing",
    # Hub copy retuned 2026-11-12 to a plain index. Search Console Oct 13 - Nov 9:
    # "security guard payroll funding" 663 + "payroll financing" 542 impressions, 0
    # clicks, split between this hub, the working-capital article and the pillar after
    # the Nov 7 batch gave all three "payroll funding" titles. Nov 8-10: hub 3.9,
    # guard-payroll-between-invoices 4.4, working-capital article 35. One target now:
    # guard-payroll-between-invoices. The hub routes to it instead of answering it.
    "hub_title": "Security Guard Company Financing Guides | Axiant",
    "hub_h1": "Security Guard Company Financing Guides",
    "hub_lede": "Payroll, factoring, bonding, vehicles and bigger contracts: one guide "
                "for each cash problem a guard company runs into",
    "hub_desc": "Guides for security guard company owners: payroll funding, invoice "
                "factoring, bonding and insurance costs, patrol vehicles and the cash "
                "to win larger contracts.",
    "hub_quick_answer": "Security guard companies usually finance three things: the gap "
                        "between weekly payroll and clients who pay on <strong>net-30 to "
                        "net-60</strong> terms, the up-front cost of winning a contract "
                        "(bonding, insurance, recruiting), and patrol vehicles and radios. "
                        "Each guide below covers one of them, and the payroll guide "
                        "publishes typical advances of <strong>80-95%</strong> of an invoice. "
                        "Axiant Partners, a business-loan broker in Boca Raton, matches "
                        "guard companies with funders.",
    "hub_intro": "Looking for <a href=\"guard-payroll-between-invoices/\">security guard "
                 "payroll funding</a> or payroll financing? That guide has the rates, "
                 "advances, a sizing table and setup steps. For factoring on its own, see "
                 "<a href=\"security-guard-invoice-factoring/\">security guard invoice "
                 "factoring</a>. For cash beyond payroll, such as contract ramp-ups and "
                 "insurance renewals, read "
                 "<a href=\"/working-capital-loans/articles/security-guard-company-working-capital/\">"
                 "working capital for security guard companies</a>, and for every product "
                 "see <a href=\"/security-guard-business-financing.html\">security guard "
                 "company financing</a>.",
    "hub_cta_h2": "Payroll due before the client pays?",
    "hub_cta_p": "Tell us your contract terms, your billing cycle and your weekly "
                 "payroll. We will show you which instruments actually fit.",
}

SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms fund payroll and working capital, "
        "including approval rates by product.")
DOL_FLSA = ("https://www.dol.gov/agencies/whd/flsa",
            "US Department of Labor: Fair Labor Standards Act",
            "Federal wage and hour rules, including overtime - the obligations "
            "that make guard payroll non-negotiable and time-sensitive.")
SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans",
          "SBA 7(a) Loan Program",
          "Official terms and eligibility for the SBA's primary business loan, "
          "including its use for working capital.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "cost is presented to borrowers.")
FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "The FTC's guidance to lenders, brokers and merchant cash advance providers on misrepresented costs, unlawful collection and false claims of government affiliation.")
SAM = ("https://sam.gov/",
       "SAM.gov",
       "The federal registration system for contractors - where public-sector "
       "guard contracts are advertised and awarded.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "The authority on Section 179 and depreciation for vehicles and "
           "equipment bought by the business.")

UCC_9406 = ("https://www.law.cornell.edu/ucc/9/9-406",
            "UCC 9-406: Discharge of account debtor; restrictions on assignment",
            "Notice of assignment, and why a contract term banning assignment of a "
            "receivable is generally ineffective.")

ARTICLES = [
    {
        # Target page for "security guard payroll funding" (663 impressions) and
        # "security guard payroll financing" (542), Search Console Oct 13 - Nov 9;
        # position 4.4 / 13.2 on Nov 8-10. Strengthened 2026-11-12: both names in the
        # title, client-mix fee table (moved here from the working-capital article),
        # a computed sizing table, setup steps, UCC 9-406 assignment rule.
        "slug": "guard-payroll-between-invoices",
        "date_published": "2026-10-27",
        "crumb": "Payroll Funding",
        "title": "Security Guard Payroll Funding &amp; Financing: Rates | Axiant",
        "og_title": "Security Guard Payroll Funding and Financing: Rates, Terms, How It Works",
        "h1": "Security Guard Payroll Funding and Financing: Rates, Terms, How It Works",
        "headline": "Security Guard Payroll Funding and Financing: Rates, Terms, How It Works",
        "lede": "Wages weekly, invoices at sixty days - what payroll funding typically "
                "costs, how much your payroll needs, and how to set it up before the next "
                "pay run",
        "meta_desc": "Security guard payroll funding (or payroll financing) commonly advances "
                     "80-95% of invoices for about 1-5%. See fees by client mix, a sizing "
                     "table and setup steps.",
        "article_desc": "How payroll funding covers the gap between a security guard "
                        "company's weekly payroll and net-30 to net-60 client payments: "
                        "typical rates and terms, sizing and setup.",
        "keywords": "security guard payroll funding, security guard payroll financing, "
                    "payroll funding guard companies, guard payroll factoring, net 60 payroll gap",
        "quick_answer": "As of November 2026, security guard payroll funding (also sold as "
                        "payroll financing) is usually invoice factoring timed to the wage run. "
                        "A funder commonly advances <strong>80-95%</strong> of each client "
                        "invoice, often within <strong>24 hours</strong> once the account is "
                        "set up, and charges about <strong>1-5% of invoice value</strong>, "
                        "more when clients pay slowly. Axiant Partners, a business-loan broker "
                        "in Boca Raton, matches guard companies with these funders. These are "
                        "typical ranges, not a quote.",
        "sections": [
            ("Why This Industry Feels It Worse",
             "<p>Almost every service business waits to be paid. Guard companies have "
             "the sharpest version of it, for three reasons that compound.</p>"
             "<p><strong>Labour is nearly the whole cost.</strong> There is little "
             "material spend to defer and no inventory to run down. When cash is "
             "short, the thing you cannot delay is the thing you mostly buy.</p>"
             "<p><strong>Wages are legally time-bound.</strong> Payroll is not a "
             "supplier who can be asked to wait. Federal wage and hour obligations "
             "under the "
             '<a href="https://www.dol.gov/agencies/whd/flsa" rel="noopener nofollow" '
             'target="_blank">Fair Labor Standards Act</a> apply regardless of whether '
             "the client has paid you.</p>"
             "<p><strong>Clients are slow by convention.</strong> Property managers, "
             "facilities firms and public bodies pay on net-30 to net-60 as standard, "
             "and it is rarely negotiable for a smaller vendor.</p>"),
            ("The Instruments That Fit",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Instrument</th><th>How it works</th><th>Fits when</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Instrument">Invoice factoring</td>'
             '<td data-label="How">Advances against issued invoices; the funder is '
             "repaid when the client pays</td>"
             '<td data-label="Fits">Contracts are billed and clients are '
             "creditworthy</td></tr>"
             '<tr><td data-label="Instrument">Payroll funding</td>'
             '<td data-label="How">Factoring structured around the payroll cycle, '
             "sometimes with payroll administration attached</td>"
             '<td data-label="Fits">Payroll timing is the whole problem</td></tr>'
             '<tr><td data-label="Instrument">Business line of credit</td>'
             '<td data-label="How">Revolving; draw and repay as billing cycles</td>'
             '<td data-label="Fits">Cheaper, but usually needs trading history</td></tr>'
             '<tr><td data-label="Instrument">Working capital term loan</td>'
             '<td data-label="How">Lump sum, fixed repayment</td>'
             '<td data-label="Fits">A one-off ramp rather than a recurring gap</td></tr>'
             "</tbody></table></div>"
             "<p>Factoring dominates here for a structural reason: it underwrites "
             "<em>your client's</em> ability to pay rather than yours. A young guard "
             "company billing a well-rated property manager can often factor when it "
             "could not get a line of credit.</p>"),
            ("Payroll Funding or Payroll Financing? Same Product, Two Names",
             "<p>Funders use both names, and searchers do too. In the guard business they "
             "nearly always describe the same thing: money advanced against invoices you "
             "have already issued, timed so the wage run is covered. The difference that "
             "matters is not the name but the structure underneath it:</p>"
             + table(["If the contract says", "What it is", "How it is priced"], [
                 ["You sell or assign the invoice", "Factoring (payroll funding)",
                  "A fee per invoice, rising the longer it stays unpaid"],
                 ["You borrow against all receivables", "Accounts receivable line",
                  "Interest on the balance you draw"],
                 ["You borrow against your next pay run", "Payroll advance or loan",
                  "A fixed fee or factor; ask for the APR"],
             ])
             + "<p>Ask any provider which of the three you are signing. The same "
             "headline number, say 3%, is cheap as a fee on a 30-day invoice and very "
             "expensive as a fee on a one-week advance. See "
             "<a href=\"/working-capital-loans/articles/accounts-receivable-financing/\">"
             "accounts receivable financing</a> for the second structure.</p>"),
            ("Typical Payroll Funding Rates and Terms",
             "<p>Payroll funding is priced as a fee on each invoice rather than as "
             "an interest rate. The ranges below are those conventional across "
             "funders and lenders, not anyone's quote; your file decides where you "
             "land.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Term</th><th>Payroll funding</th><th>Line of credit</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Term">Advance</td>'
             '<td data-label="Payroll funding">Commonly 80-95% of invoice value</td>'
             '<td data-label="Line of credit">A set limit you draw against</td></tr>'
             '<tr><td data-label="Term">Cost</td>'
             '<td data-label="Payroll funding">About 1-5% of invoice value</td>'
             '<td data-label="Line of credit">About 8-13% APR at banks; 14-30%+ '
             "online</td></tr>"
             '<tr><td data-label="Term">Speed</td>'
             '<td data-label="Payroll funding">Setup takes a few business days; '
             "then invoices often fund within 24 hours</td>"
             '<td data-label="Line of credit">Weeks at a bank; faster online</td></tr>'
             '<tr><td data-label="Term">Decided by</td>'
             '<td data-label="Payroll funding">Mostly your clients&rsquo; credit</td>'
             '<td data-label="Line of credit">Your credit, revenue and time in '
             "business</td></tr>"
             "</tbody></table></div>"
             "<p><strong>Fees by client mix.</strong> The same ranges, placed against "
             "the kind of clients a guard company bills. They match our "
             "<a href=\"/working-capital-loans/articles/invoice-factoring-rates/\">invoice "
             "factoring rates</a> guide and are typical, not quotes.</p>"
             + table(["Your client mix", "Likely fee", "Why"], [
                 ["Strong clients, near net 30", "About 1-2%", "Good credit and faster pay"],
                 ["Mixed clients, average pay", "About 2-3.5%", "Moderate volume and credit"],
                 ["Slow payers, net 60-90", "About 3.5-5%", "More time in tiered pricing"],
             ])
             + "<p><strong>What moves the fee.</strong> Slow-paying clients cost more, "
             "because the fee grows with how long the invoice is outstanding; so do "
             "small invoice volumes and concentration in one client. Recourse "
             "funding, where you buy back an invoice the client never pays, usually "
             "costs less than non-recourse, where the funder absorbs that credit "
             "loss. See <a href=\"/invoice-factoring.html\">how invoice factoring "
             "works</a> and <a href=\"/business-line-of-credit/articles/typical-business-line-of-credit-rates-2026/\">"
             "typical line of credit rates</a> for the detail behind each column.</p>"
             "<p><strong>Worked example (illustrative).</strong> A guard company "
             "bills a property manager $60,000 at month end on net-45 terms. At an "
             "85% advance it receives $51,000 within days of invoicing, which covers "
             "the next payroll runs. If the fee works out at 3% of the invoice, "
             "$1,800, the funder releases the remaining $7,200 once the client pays. "
             "The numbers are an example, not a quote; your advance and fee depend "
             "on your clients and volume.</p>"
             "<p>To see which structure your contracts support, "
             "<a href=\"/match.html\">get matched with funders that work with guard "
             "companies</a>.</p>"),
            ("Worked Example: How Much Funding Your Payroll Needs",
             "<p>A simple way to size the gap: multiply your weekly payroll, including "
             "taxes and workers&rsquo; comp, by the weeks between a guard&rsquo;s first "
             "shift and the day the client pays for it. With monthly billing in arrears "
             "that is about <strong>4.3 weeks</strong> of billing period plus the payment "
             "terms. The table does the multiplication (rounded to the nearest "
             "$1,000):</p>"
             + table(["Weekly payroll", "Net 30 (8.6 wks)", "Net 45 (10.8 wks)",
                      "Net 60 (12.9 wks)", "Factored at invoice (4.3 wks)"], [
                 ["$10,000", "$86,000", "$108,000", "$129,000", "$43,000"],
                 ["$25,000", "$215,000", "$269,000", "$323,000", "$108,000"],
                 ["$50,000", "$431,000", "$538,000", "$645,000", "$217,000"],
             ])
             + "<p>The last column is the point of payroll funding. Once each invoice is "
             "advanced the day it is issued, you only carry the month you have not billed "
             "yet, plus the 5-20% the funder holds back until the client pays. Billing "
             "every two weeks instead of monthly roughly halves that column again, where "
             "the contract allows it. This is a planning estimate, not a credit limit; a "
             "funder sizes the facility on your invoices and your clients.</p>"),
            ("Growth Makes the Gap Wider, Not Narrower",
             "<p>The counter-intuitive part, and the thing that catches owners out.</p>"
             "<p>Winning a new contract means staffing posts immediately. Wages start "
             "in week one. The first invoice goes out at month end and pays perhaps "
             "sixty days later. So a new contract consumes cash for months before it "
             "produces any, and the bigger the win, the larger the hole.</p>"
             "<p>A company growing quickly can be profitable on paper and unable to "
             "make payroll, which is a different problem from being unprofitable and "
             "has a different fix. Financing growth is reasonable; financing a loss is "
             "not, and the two look similar on a bank statement for a while.</p>"
             "<p>See <a href=\"../cash-requirements-to-win-larger-guard-contracts/\">"
             "what larger contracts require in cash</a> before signing one.</p>"),
            ("What Funders Look At",
             "<p>Because factoring underwrites the receivable, the checks are "
             "different from a conventional loan:</p>"
             "<ul>"
             "<li><strong>Who your clients are.</strong> Their credit, not yours, "
             "carries most of the decision.</li>"
             "<li><strong>Concentration.</strong> One client at most of your revenue "
             "is a risk, however good that client is.</li>"
             "<li><strong>Contract terms.</strong> Clean payment terms and who you "
             "send the notice of assignment to. Under "
             '<a href="https://www.law.cornell.edu/ucc/9/9-406" rel="noopener nofollow" '
             'target="_blank">UCC 9-406</a> a clause banning assignment of a receivable is '
             "generally ineffective, but many funders still pass on a contract that has "
             "one, and federal contracts follow the Assignment of Claims Act instead.</li>"
             "<li><strong>Billing discipline.</strong> Invoices that go out late, or "
             "that clients dispute, undermine the whole structure.</li>"
             "<li><strong>Existing liens.</strong> A blanket UCC filing from an "
             "earlier lender can capture your receivables and has to be subordinated "
             "first.</li>"
             "</ul>"
             "<p>Read the assignment clause in your contracts before you apply. It "
             "rarely makes factoring impossible, but it is a common reason a funder "
             "slows down or says no.</p>"),
            ("How to Set Up Payroll Funding Before the Next Pay Run",
             "<ol>"
             "<li><strong>List every client</strong> with its payment terms, average "
             "monthly billing and how late it really pays.</li>"
             "<li><strong>Pull your contracts</strong> and flag any assignment clause or "
             "government client, since those change the paperwork.</li>"
             "<li><strong>Run a UCC search</strong> on your company. An earlier lender "
             "with a blanket lien has to release or subordinate the receivables "
             "first.</li>"
             "<li><strong>Apply with an aging report</strong> and recent invoices. The "
             "funder checks your clients&rsquo; credit more closely than yours.</li>"
             "<li><strong>Send notices of assignment</strong> so clients pay the funder "
             "directly, or agree a different payment route if the funder allows it.</li>"
             "<li><strong>Submit the first invoices</strong> two or three business days "
             "before payroll, so the first advance lands in time.</li>"
             "</ol>"
             "<p>Setup commonly takes a few business days; after that, invoices often "
             "fund within 24 hours. If you need cash before the account is live, a "
             "<a href=\"/business-line-of-credit.html\">line of credit</a> or a short "
             "working capital loan can carry one pay run.</p>"),
            ("Fixing the Cause as Well as the Symptom",
             "<p>Financing the gap is sensible. Narrowing it is cheaper, and several "
             "levers are within your control:</p>"
             "<ul>"
             "<li><strong>Invoice immediately.</strong> A week's delay in billing is a "
             "week added to every payment term, at your cost.</li>"
             "<li><strong>Bill more often.</strong> Fortnightly rather than monthly "
             "billing halves the average wait where the contract permits it.</li>"
             "<li><strong>Get terms right at contract stage.</strong> Payment terms "
             "are negotiable before signature and almost never afterwards.</li>"
             "<li><strong>Chase early.</strong> Most late payment is administrative "
             "rather than deliberate &mdash; a missing purchase order number, an "
             "invoice sent to the wrong address.</li>"
             "<li><strong>Watch concentration.</strong> It affects both your risk and "
             "your access to funding.</li>"
             "</ul>"
             "<p>Our <a href=\"/working-capital-loans/articles/security-guard-company-working-capital/\">"
             "guide to working capital for guard companies</a> covers the wider "
             "picture.</p>"),
        ],
        "faqs": [
            ("How much does security guard payroll funding cost?",
             "Commonly about 1-5% of invoice value, with the advance commonly 80-95% "
             "of the invoice. Slow-paying clients, small volumes and reliance on one "
             "client push the fee up. These are typical ranges across funders, not "
             "a quote."),
            ("Why do security guard companies struggle with payroll?",
             "Because labour is nearly the entire cost, wages are legally time-bound, "
             "and commercial and municipal clients pay on net-30 to net-60 as "
             "standard. There is no material spend to defer and no inventory to run "
             "down, so the one cost you cannot delay is the one you mostly have."),
            ("What is payroll funding for guard companies?",
             "Invoice factoring structured around the payroll cycle, sometimes with "
             "payroll administration attached. The funder advances against issued "
             "invoices and is repaid when your client pays, which aligns the money "
             "with the wage run rather than the billing cycle."),
            ("Can a new guard company get factoring?",
             "Often yes, and this is the main reason factoring dominates the sector. "
             "It underwrites your client's ability to pay rather than your trading "
             "history, so a young company billing a well-rated property manager can "
             "frequently factor when it could not get a line of credit."),
            ("Why does winning a big contract make cash worse?",
             "Because you staff the posts immediately and bill in arrears. Wages start "
             "in week one, the first invoice goes out at month end, and payment "
             "arrives perhaps sixty days after that. The bigger the contract, the "
             "larger the hole before any revenue arrives."),
            ("What can stop me factoring my invoices?",
             "Most often an existing blanket UCC filing from an earlier lender that "
             "already captures your receivables, or a client contract with an "
             "assignment clause. Under UCC 9-406 that clause is generally ineffective, "
             "but some funders still decline the contract, and federal contracts follow "
             "the Assignment of Claims Act. Both are checkable before you apply."),
            ("Is payroll financing the same as payroll funding?",
             "For guard companies, usually yes: both names describe advances against "
             "invoices you have issued, timed to the wage run. Check the contract. If "
             "you are selling invoices it is factoring, priced per invoice; if you are "
             "borrowing against your next pay run it is a loan, and you should ask for "
             "the APR."),
            ("How much payroll funding does a guard company need?",
             "Roughly your weekly payroll times the weeks from first shift to client "
             "payment. With monthly billing on net-45 terms that is about 10.8 weeks, so "
             "a $25,000 weekly payroll ties up about $269,000. Advancing each invoice "
             "when issued cuts the gap to about the 4.3-week billing month."),
        ],
        "related": [
            ("/security-guard-business-financing.html", "Security guard company financing"),
            ("/invoice-factoring.html", "Invoice factoring"),
            ("/working-capital-loans/articles/security-guard-company-working-capital/",
             "Working capital for security guard companies"),
            ("../cash-requirements-to-win-larger-guard-contracts/",
             "Cash requirements to win larger contracts"),
        ],
        "sources": [DOL_FLSA, UCC_9406, SBCS, CFPB],
    },
    {
        "slug": "bonding-and-insurance-costs-for-guard-contracts",
        "crumb": "Bonding and Insurance",
        "title": "Bonding and Insurance Costs for Guard Contracts | Axiant",
        "og_title": "Bonding and Insurance Costs for Guard Contracts",
        "h1": "Bonding and Insurance Costs for Guard Contracts",
        "headline": "Bonding and Insurance Costs for Guard Contracts",
        "lede": "The cost of being allowed to bid - what clients require, when "
                "it is payable, and how to finance the timing",
        "meta_desc": "Guard contracts require licensing, bonding and insurance "
                     "before work begins. What the requirements typically cover, why "
                     "the timing hurts cash flow, and how to finance the gap.",
        "article_desc": "What bonding and insurance requirements cost a guard "
                        "company and how to manage the cash timing.",
        "keywords": "security guard bonding, guard company insurance cost, surety "
                    "bond security, contract insurance requirements",
        "quick_answer": "Bonding and insurance are the cost of being "
                        "<strong>eligible to bid</strong>, and the timing is the "
                        "problem: premiums and bond costs are due "
                        "<strong>before</strong> the contract generates revenue, and "
                        "larger contracts demand higher limits. The requirements "
                        "themselves vary by state and by client, so the reliable step "
                        "is to read the tender's insurance schedule before pricing "
                        "the work.",
        "sections": [
            ("What Clients Typically Require",
             "<p>Requirements vary considerably by state, by client and by contract, "
             "so treat this as the shape rather than the specification. The recurring "
             "elements:</p>"
             "<ul>"
             "<li><strong>State licensing</strong> for the company and for individual "
             "officers, with renewal cycles and fees attached</li>"
             "<li><strong>General liability cover</strong> at limits the client "
             "specifies, often higher for larger or public-sector work</li>"
             "<li><strong>Workers' compensation</strong>, which for a labour-intensive "
             "business is a substantial recurring cost</li>"
             "<li><strong>Commercial auto</strong> where patrol vehicles are used</li>"
             "<li><strong>A surety or fidelity bond</strong>, guaranteeing performance "
             "or covering employee dishonesty</li>"
             "<li><strong>Additional insured endorsements</strong> naming the client "
             "&mdash; administratively small, frequently forgotten, and it delays "
             "contract start</li>"
             "</ul>"
             "<p>The precise requirements sit in the tender or contract documents. "
             "Read the insurance schedule before pricing, not after winning.</p>"),
            ("Why the Timing Is the Real Problem",
             "<p>The amounts are usually manageable. The sequence is not.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Stage</th><th>Cash movement</th></tr></thead><tbody>"
             '<tr><td data-label="Stage">Bidding</td>'
             '<td data-label="Cash">Licensing current, sometimes a bid bond</td></tr>'
             '<tr><td data-label="Stage">Award</td>'
             '<td data-label="Cash">Higher limits bound, endorsements issued, bond '
             "premium paid</td></tr>"
             '<tr><td data-label="Stage">Mobilisation</td>'
             '<td data-label="Cash">Recruiting, screening, uniforms, equipment</td></tr>'
             '<tr><td data-label="Stage">Weeks 1-4</td>'
             '<td data-label="Cash">Payroll, with nothing invoiced yet</td></tr>'
             '<tr><td data-label="Stage">Month 2-3</td>'
             '<td data-label="Cash">First payment arrives</td></tr>'
             "</tbody></table></div>"
             "<p>Every outflow precedes every inflow. A company can win good work and "
             "be unable to start it, which is the specific failure this article "
             "exists to name.</p>"),
            ("What Actually Moves the Cost",
             "<ul>"
             "<li><strong>Claims history.</strong> The single biggest lever over time, "
             "and the one most within your control.</li>"
             "<li><strong>Armed against unarmed.</strong> A materially different risk "
             "profile and priced accordingly.</li>"
             "<li><strong>What you guard.</strong> Retail, construction sites, events "
             "and healthcare carry different exposures.</li>"
             "<li><strong>Payroll size.</strong> Workers' compensation scales with "
             "wages, so growth raises it automatically.</li>"
             "<li><strong>Screening and training standards.</strong> Documented "
             "procedure is an underwriting argument, not just good practice.</li>"
             "<li><strong>For bonding, your financials.</strong> A surety is "
             "underwriting your ability to perform, so it looks like credit "
             "underwriting.</li>"
             "</ul>"
             "<p>A clean claims record compounds. It is worth treating incident "
             "management as a financial function as well as an operational one.</p>"),
            ("Financing the Timing",
             "<p>Since the problem is sequence rather than size, the instruments that "
             "help are the ones that bridge:</p>"
             "<ul>"
             "<li><strong>Premium finance</strong> spreads an annual premium over "
             "monthly instalments, converting a lump sum into a run rate.</li>"
             "<li><strong>A line of credit</strong> covers mobilisation and is repaid "
             "as invoices settle &mdash; the cleanest fit where you can get one.</li>"
             "<li><strong>Factoring</strong> does not help with pre-contract costs, "
             "because there is no invoice yet. It helps from the first billing "
             "onward; see "
             '<a href="../guard-payroll-between-invoices/">covering payroll between '
             "invoices</a>.</li>"
             "<li><strong>A working capital loan</strong> suits a one-off step up in "
             "limits rather than a recurring cycle.</li>"
             "</ul>"
             "<p>The distinction worth holding: costs incurred <em>before</em> "
             "invoicing need a facility that does not depend on an invoice existing.</p>"),
            ("Pricing It Into the Bid",
             "<p>The avoidable version of this problem is winning work that was "
             "underpriced because compliance costs were not in the model.</p>"
             "<ul>"
             "<li><strong>Read the insurance schedule before pricing.</strong> Higher "
             "required limits change your cost base for that contract.</li>"
             "<li><strong>Get a quote at the required limits</strong>, not your "
             "current ones.</li>"
             "<li><strong>Include the bond premium</strong> as a line item.</li>"
             "<li><strong>Model the mobilisation gap</strong> &mdash; weeks of payroll "
             "before the first payment.</li>"
             "<li><strong>Check the endorsement requirements</strong> early; they take "
             "days to issue and can delay a start date.</li>"
             "</ul>"
             "<p>A contract that is profitable on the rate and unaffordable on the "
             "timing is still a problem. Price both.</p>"),
        ],
        "faqs": [
            ("What insurance do guard contracts usually require?",
             "Commonly general liability at client-specified limits, workers' "
             "compensation, commercial auto where patrol vehicles are used, and often "
             "a surety or fidelity bond, plus additional insured endorsements naming "
             "the client. Requirements vary by state and contract, so read the "
             "schedule in the tender."),
            ("Why do bonding and insurance hurt cash flow so much?",
             "Because of sequence rather than size. Premiums, bond costs and "
             "mobilisation are paid before the contract has generated any revenue, and "
             "the first client payment may be two to three months after the work "
             "starts."),
            ("What makes guard insurance more expensive?",
             "Claims history most of all, then whether officers are armed, what is "
             "being guarded, and payroll size &mdash; workers' compensation scales "
             "with wages, so growth raises it automatically. Documented screening and "
             "training standards work in your favor at renewal."),
            ("Can I finance an insurance premium?",
             "Premium finance is common and spreads an annual premium into monthly "
             "instalments, turning a lump sum into a run rate. For mobilisation costs "
             "more broadly, a line of credit fits better because factoring cannot help "
             "before an invoice exists."),
            ("How should I price compliance costs into a bid?",
             "Quote insurance at the limits the contract requires rather than the ones "
             "you currently hold, include the bond premium as a line item, and model "
             "the weeks of payroll before the first payment arrives. A contract "
             "profitable on rate can still be unaffordable on timing."),
        ],
        "related": [
            ("/security-guard-business-financing.html", "Security guard company financing"),
            ("../guard-payroll-between-invoices/", "Covering guard payroll between invoices"),
            ("../cash-requirements-to-win-larger-guard-contracts/",
             "Cash requirements to win larger contracts"),
            ("/business-line-of-credit.html", "Business line of credit"),
        ],
        "sources": [DOL_FLSA, SBA_7A, FTC],
    },
]

# Articles 3-4 live in a companion module to keep each file readable.
from cluster_security_guard_b import MORE as _B
from cluster_security_guard_c import MORE_C as _C
ARTICLES = ARTICLES + _B + _C
