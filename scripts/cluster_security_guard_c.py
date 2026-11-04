# -*- coding: utf-8 -*-
"""Security guard company financing, article 5: invoice factoring.

Search Console (Aug 5 - Nov 2, 2026): 12 factoring queries, 693 impressions at
about position 28, 0 clicks. No page targets the question directly; the pillar
and the working capital spoke mention factoring in passing and are left alone.

Advance and fee ranges match /invoice-factoring.html and the guard payroll
spoke. Legal points were read from the cited text on 2026-11-04. No funded
totals, no testimonials, no named-lender rates. One entity: Axiant Partners,
(561) 268-0465, Boca Raton.
"""
from cluster_security_guard import DOL_FLSA, SAM, FTC

FAR_ASSIGN = ("https://www.acquisition.gov/far/subpart-32.8",
              "FAR Subpart 32.8: Assignment of Claims",
              "Conditions for assigning payments on a federal contract: payments "
              "of $1,000 or more, a bank, trust company or other financing "
              "institution, generally one party, and written notice to the agency "
              "and surety.")
UCC_406 = ("https://www.law.cornell.edu/ucc/9/9-406",
           "UCC 9-406: Discharge of Account Debtor",
           "After notice of assignment, the customer pays the assignee, and many "
           "contract terms restricting assignment of an account are ineffective.")
IRC_6323 = ("https://www.law.cornell.edu/uscode/text/26/6323",
            "26 USC 6323: Validity and Priority of Federal Tax Liens",
            "How a filed federal tax lien ranks against accounts receivable "
            "financing, including the 45-day limit on protected advances.")
IRS_EMP = ("https://www.irs.gov/businesses/small-businesses-self-employed/understanding-employment-taxes",
           "IRS: Understanding Employment Taxes",
           "The withholding and deposit duties every employer of guards carries, "
           "which funders check before advancing against invoices.")

MORE_C = [
    {
        "slug": "security-guard-invoice-factoring",
        "crumb": "Security Guard Invoice Factoring",
        "title": "Security Guard Invoice Factoring: Rates and Terms | Axiant",
        "og_title": "Security Guard Invoice Factoring: Rates, Advances and How It Works",
        "h1": "Security Guard Invoice Factoring: Rates, Advances and How It Works",
        "headline": "Security Guard Invoice Factoring: Rates, Advances and How It Works",
        "lede": "Guards get paid weekly and clients pay in 30 to 60 days. What "
                "factoring those invoices costs, what funders check, and when it "
                "is the wrong tool",
        "meta_desc": "Security guard factoring commonly advances 80-95% of an invoice for a fee of about 1-5%. How it works on net-30 to net-60 contracts and what funders check.",
        "article_desc": "How security guard companies factor client invoices to "
                        "meet weekly payroll, with typical advances, fees, a worked "
                        "example and the checks funders run.",
        "keywords": "security guard invoice factoring, security guard factoring, "
                    "factoring for security guard companies, accounts receivable "
                    "financing for security guard companies",
        "quick_answer": "Security guard invoice factoring turns an unpaid client "
                        "invoice into cash for payroll. Funders commonly advance "
                        "<strong>80-95%</strong> of the invoice within days and "
                        "charge a fee of about <strong>1-5%</strong> of its value, "
                        "then release the balance when the client pays on its "
                        "<strong>net-30 to net-60</strong> terms. Approval leans on "
                        "your clients' ability to pay more than on your own credit. "
                        "Axiant Partners, a business-loan broker in Boca Raton, "
                        "matches guard companies with funders. These are typical "
                        "ranges across funders, not a quote.",
        "sections": [
            ("Guard Company Factoring at a Glance",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Term</th><th>Typical range</th></tr></thead><tbody>"
             '<tr><td data-label="Term">Advance</td>'
             '<td data-label="Typical range">80-95% of an approved invoice</td></tr>'
             '<tr><td data-label="Term">Fee</td>'
             '<td data-label="Typical range">About 1-5% of invoice value</td></tr>'
             '<tr><td data-label="Term">Setup</td>'
             '<td data-label="Typical range">Often a few business days</td></tr>'
             '<tr><td data-label="Term">Later invoices</td>'
             '<td data-label="Typical range">Can fund in as little as 24 hours once verified</td></tr>'
             '<tr><td data-label="Term">Client terms</td>'
             '<td data-label="Typical range">Net-30 is easier to fund than net-60</td></tr>'
             "</tbody></table></div>"
             "<p>These are conventional ranges, not anyone's quote. Your clients' "
             "credit, invoice size, monthly volume and how long clients take to pay "
             "decide where you land.</p>"),
            ("How Factoring Works on a Guard Contract",
             "<ol>"
             "<li><strong>You bill the client</strong> for hours worked at each "
             "post, with signed timesheets or the client's approval behind it.</li>"
             "<li><strong>The funder verifies</strong> that the invoice is real, "
             "that the service was delivered, and that nothing is disputed.</li>"
             "<li><strong>You receive the advance</strong>, commonly in time for the "
             "next payroll run.</li>"
             "<li><strong>The client pays the funder</strong> under a notice of "
             "assignment. Under "
             '<a href="https://www.law.cornell.edu/ucc/9/9-406" rel="noopener nofollow" '
             'target="_blank">UCC 9-406</a>, once the client has that notice, it '
             "settles the invoice by paying the assignee rather than you.</li>"
             "<li><strong>The funder releases the reserve</strong>, which is the "
             "balance of the invoice minus the fee.</li>"
             "</ol>"
             "<p>Clients see this process, so tell your larger accounts before the "
             "first notice arrives. Factoring is common in the guard industry, but "
             "a surprise letter to a property manager is not a good first "
             "impression.</p>"),
            ("Worked Example: A $120,000 Month on Net-45",
             "<p><strong>Illustrative numbers, not a quote.</strong> A guard company "
             "bills <strong>$120,000</strong> a month to commercial clients on "
             "net-45 terms and factors all of it at an 85% advance and a 3% fee.</p>"
             "<ul>"
             "<li>Advance within days of billing: <strong>$102,000</strong></li>"
             "<li>Fee at 3% of the invoice value: <strong>$3,600</strong></li>"
             "<li>Reserve released after the client pays: <strong>$14,400</strong></li>"
             "</ul>"
             "<p>That $3,600 on $102,000 for 45 days works out to roughly "
             "<strong>29% annualized</strong>, so factoring is not cheap money. It "
             "competes with a missed payroll, not with a bank line. Guard margins "
             "are thin because labor is most of the cost, so run the fee against "
             "the margin on each contract before factoring all of them. If clients "
             "pay faster than the fee schedule assumes, the true cost falls; if "
             "they pay slower, tiered fees can push it higher.</p>"),
            ("Factoring vs Other Guard Payroll Funding",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Option</th><th>Best for</th><th>Watch out for</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Option">Invoice factoring</td>'
             '<td data-label="Best for">Growing firms with strong clients on long terms</td>'
             '<td data-label="Watch out for">Fees, minimums, client notice</td></tr>'
             '<tr><td data-label="Option">Line of credit</td>'
             '<td data-label="Best for">Established firms with a recurring small gap</td>'
             '<td data-label="Watch out for">Limit may not grow with new posts</td></tr>'
             '<tr><td data-label="Option">Payroll funding</td>'
             '<td data-label="Best for">Funding tied directly to the pay cycle</td>'
             '<td data-label="Watch out for">Many products are factoring under another name</td></tr>'
             '<tr><td data-label="Option">Merchant cash advance</td>'
             '<td data-label="Best for">Rarely a fit for this cycle</td>'
             '<td data-label="Watch out for">Daily payments erode thin contract margins</td></tr>'
             "</tbody></table></div>"
             "<p>For the payroll side of this decision, read "
             '<a href="/security-guard-business-financing/articles/guard-payroll-between-invoices/">'
             "security guard payroll funding</a>. For the instrument itself across "
             'all industries, see <a href="/invoice-factoring.html">invoice '
             "factoring</a>.</p>"),
            ("Federal, State and Municipal Guard Contracts",
             "<p>Government clients usually pay reliably, which funders like, but "
             "assigning those payments takes more paperwork.</p>"
             "<p><strong>Federal contracts</strong> follow "
             '<a href="https://www.acquisition.gov/far/subpart-32.8" rel="noopener nofollow" '
             'target="_blank">FAR Subpart 32.8</a>. The contract must specify '
             "payments aggregating $1,000 or more, the assignment must go to a bank, "
             "trust company or other financing institution, it is generally limited "
             "to one party, and the assignee must send written notice to the "
             "contracting officer, any surety and the disbursing officer. Confirm "
             "that your registration on "
             '<a href="https://sam.gov/" rel="noopener nofollow" target="_blank">SAM.gov</a> '
             "is current and that your funder has handled federal assignments "
             "before.</p>"
             "<p><strong>State and municipal contracts</strong> have their own "
             "rules, and some restrict assignment. Ask the funder and read the "
             "contract before you count on the advance. The same goes for private "
             "contracts: UCC 9-406 makes many assignment restrictions ineffective, "
             "but it has exceptions and does not replace a review of your "
             "agreement.</p>"),
            ("What Funders Check on a Guard Company",
             "<ul>"
             "<li><strong>Client credit and concentration.</strong> Funders may cap "
             "how much of your receivables can sit with one client.</li>"
             "<li><strong>Clean invoices.</strong> Signed timesheets and clear rates "
             "reduce the disputes that hold up funding.</li>"
             "<li><strong>Payroll taxes.</strong> Funders check that "
             '<a href="https://www.irs.gov/businesses/small-businesses-self-employed/understanding-employment-taxes" '
             'rel="noopener nofollow" target="_blank">employment taxes</a> are '
             "current, because a federal tax lien can reach receivables. Under "
             '<a href="https://www.law.cornell.edu/uscode/text/26/6323" rel="noopener nofollow" '
             'target="_blank">26 USC 6323</a>, protection for later advances is '
             "limited to about 45 days after a lien is filed.</li>"
             "<li><strong>Existing liens.</strong> A blanket UCC filing from an "
             "earlier lender may already cover your receivables and has to be "
             "released or subordinated.</li>"
             "<li><strong>Existing advances.</strong> A merchant cash advance can "
             "block factoring outright until it is dealt with.</li>"
             "<li><strong>License and insurance.</strong> A lapsed state license or "
             "policy puts the contract, and so the invoice, at risk.</li>"
             "</ul>"
             "<p>Wages are the reason timing matters. "
             '<a href="https://www.dol.gov/agencies/whd/flsa" rel="noopener nofollow" '
             'target="_blank">Federal wage and hour rules</a> apply whether or not '
             "the client has paid you.</p>"),
            ("Terms to Read Before You Sign",
             "<ul>"
             "<li><strong>Recourse.</strong> With recourse factoring you are "
             "responsible if the client never pays. Non-recourse moves covered "
             "credit losses to the funder for a higher fee.</li>"
             "<li><strong>Fee schedule.</strong> Ask whether the fee is flat or "
             "rises every 10 or 15 days an invoice stays open. On net-60 clients "
             "that difference is large.</li>"
             "<li><strong>Minimums and term.</strong> Monthly volume minimums and "
             "long contracts can cost more than the fee if a big client leaves.</li>"
             "<li><strong>All-invoices clauses.</strong> Some agreements require you "
             "to factor every invoice, including the fast payers you do not need "
             "to fund.</li>"
             "<li><strong>Exit terms.</strong> Check notice periods, early "
             "termination fees and how the UCC filing gets released.</li>"
             "</ul>"
             "<p>The "
             '<a href="https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic" '
             'rel="noopener nofollow" target="_blank">FTC</a> has warned small '
             "businesses about misrepresented financing costs, so get the full fee "
             "schedule in writing.</p>"),
            ("When Factoring Is the Wrong Tool",
             "<p>Factoring fits a timing gap on good invoices. It does not fix a "
             "contract priced too low, because the fee comes straight out of an "
             "already thin margin. It is also a poor fit if most of your clients "
             "pay in under two weeks, or if one client makes up nearly all of your "
             "billing. In those cases a line of credit, or repricing the contract "
             "at renewal, usually does more. If daily advances are already draining "
             "the account, deal with those first using "
             '<a href="/mca-consolidation-loan.html">MCA consolidation</a>.</p>'
             "<p>To check your options, "
             '<a href="/match.html">get matched with funders that work with guard '
             "companies</a>, or start with the wider guide to "
             '<a href="/security-guard-business-financing.html">security guard '
             "company financing</a>.</p>"),
        ],
        "faqs": [
            ("How much does security guard invoice factoring cost?",
             "Commonly about 1-5% of the invoice value, with an advance of 80-95% of "
             "the invoice. The cost depends on your clients' credit, your monthly "
             "volume and how long clients take to pay. These are typical ranges "
             "across funders, not a quote."),
            ("Can a new security guard company use factoring?",
             "Often yes, because funders look mostly at your clients' ability to pay "
             "and not only your own credit or time in business. You still need real "
             "contracts, clean invoices, and current licensing and payroll taxes."),
            ("How fast does factoring fund guard payroll?",
             "Setup often takes a few business days. After that, individual invoices "
             "can fund in as little as 24 hours once the funder verifies them."),
            ("Can guard companies factor government invoices?",
             "Often, but with more paperwork. Federal contracts follow FAR Subpart "
             "32.8 on assignment of claims, including written notice to the agency. "
             "State and municipal contracts have their own rules, and some restrict "
             "assignment."),
            ("Is payroll funding the same as factoring?",
             "Many payroll funding products are factoring under another name: the "
             "funder advances against issued invoices. A smaller number are true "
             "payroll advances underwritten on your billing history and pay runs. "
             "Ask which one you are being offered."),
            ("Will my clients know I factor my invoices?",
             "Usually yes. Standard factoring sends the client a notice of "
             "assignment telling it to pay the funder. Some funders offer "
             "non-notification programs, typically to larger and stronger "
             "companies."),
        ],
        "related": [
            ("/security-guard-business-financing.html", "Security guard company financing"),
            ("/security-guard-business-financing/articles/guard-payroll-between-invoices/",
             "Security guard payroll funding"),
            ("/security-guard-business-financing/articles/cash-requirements-to-win-larger-guard-contracts/",
             "Cash requirements to win larger guard contracts"),
            ("/invoice-factoring.html", "Invoice factoring"),
            ("/business-line-of-credit.html", "Business line of credit"),
            ("/working-capital-loans/articles/how-to-choose-factoring-company/",
             "How to choose a factoring company"),
        ],
        "sources": [FAR_ASSIGN, UCC_406, IRC_6323, IRS_EMP, DOL_FLSA, SAM, FTC],
    },
]
