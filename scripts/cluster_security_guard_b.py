# -*- coding: utf-8 -*-
"""Security guard company financing, articles 3-4."""
from cluster_security_guard import (SBCS, DOL_FLSA, SBA_7A, CFPB, FTC, SAM,
                                    IRS_946)

MORE = [
    {
        "slug": "guard-vehicle-and-radio-equipment-financing",
        "crumb": "Vehicles and Equipment",
        "title": "Financing Guard Vehicles and Radio Equipment | Axiant",
        "og_title": "Financing Guard Patrol Vehicles and Radio Equipment",
        "h1": "Financing Guard Vehicles and Radio Equipment",
        "headline": "Financing Guard Vehicles and Radio Equipment",
        "lede": "Patrol vehicles, radios, cameras and reporting systems - what "
                "can be financed as equipment and what cannot",
        "meta_desc": "Guard companies finance patrol vehicles, radios, body cameras "
                     "and reporting systems. Which assets support equipment "
                     "financing, which do not, and how to match term to useful life.",
        "article_desc": "How security guard companies finance patrol vehicles and "
                        "operational equipment.",
        "keywords": "guard patrol vehicle financing, security equipment financing, "
                    "radio equipment lease, body camera financing",
        "quick_answer": "Patrol vehicles finance easily &mdash; they are titled, "
                        "liquid and easy to value. <strong>Radios, cameras and "
                        "reporting systems are harder</strong>, because they are low "
                        "value individually, hard to recover and depreciate quickly, "
                        "so they are often better funded from a line of credit than "
                        "financed as equipment. Match the term to the asset's useful "
                        "life either way.",
        "sections": [
            ("Not All of It Is Financeable Equipment",
             "<p>Equipment financing works when the asset is worth recovering. That is "
             "the whole test, and it splits a guard company's kit list into two "
             "groups.</p>"
             "<p><strong>Patrol vehicles</strong> sit firmly on the financeable side. "
             "They are titled, individually valuable, and there is a deep resale "
             "market. A lender can identify one, secure it on the title and sell it if "
             "it comes to that.</p>"
             "<p><strong>Radios, body cameras, tablets and software</strong> sit on "
             "the other. Each unit is low value, they are spread across staff, they "
             "wear and go missing, and the resale market is thin. A lender asked to "
             "secure against them is being asked to take a position they cannot "
             "realistically enforce.</p>"),
            ("What Fits Which Instrument",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Asset</th><th>Financeable as equipment?</th>"
             "<th>Usually funded by</th></tr></thead><tbody>"
             '<tr><td data-label="Asset">Patrol vehicles</td>'
             '<td data-label="Fin">Yes &mdash; titled and liquid</td>'
             '<td data-label="Via">Equipment finance or a vehicle loan</td></tr>'
             '<tr><td data-label="Asset">Vehicle fit-out, lightbars, livery</td>'
             '<td data-label="Fin">Sometimes, bundled with the vehicle</td>'
             '<td data-label="Via">Rolled into the vehicle facility</td></tr>'
             '<tr><td data-label="Asset">Radios and repeaters</td>'
             '<td data-label="Fin">Rarely on their own</td>'
             '<td data-label="Via">Line of credit, or vendor terms</td></tr>'
             '<tr><td data-label="Asset">Body cameras</td>'
             '<td data-label="Fin">Rarely &mdash; low unit value, high loss rate</td>'
             '<td data-label="Via">Line of credit, or subscription</td></tr>'
             '<tr><td data-label="Asset">Reporting and scheduling software</td>'
             '<td data-label="Fin">No &mdash; nothing to recover</td>'
             '<td data-label="Via">Operating expense</td></tr>'
             '<tr><td data-label="Asset">Uniforms and consumables</td>'
             '<td data-label="Fin">No</td>'
             '<td data-label="Via">Working capital</td></tr>'
             "</tbody></table></div>"
             "<p>A useful heuristic: if you could not sell it second-hand for a "
             "meaningful sum, do not expect to finance it against itself.</p>"),
            ("Match the Term to the Life",
             "<p>The most common structural mistake in this category is financing "
             "short-lived kit over a long term.</p>"
             "<p>Paying for radios over five years when the fleet is replaced in three "
             "means paying for equipment you no longer use, while also paying for its "
             "replacement. The same applies to cameras and to anything where the "
             "technology moves quickly.</p>"
             "<p>Vehicles are the opposite case and are usually fine over a longer "
             "term, because a patrol vehicle genuinely lasts and retains value. That "
             "is exactly why lenders treat the two categories differently, and it is "
             "worth matching your own structure to the same logic.</p>"),
            ("Buying Against Leasing",
             "<p>Both exist for vehicles and the choice is less about cost than about "
             "what you want at the end.</p>"
             "<ul>"
             "<li><strong>Buying</strong> leaves you owning an asset with residual "
             "value, and it is depreciable &mdash; see "
             '<a href="https://www.irs.gov/publications/p946" rel="noopener nofollow" '
             'target="_blank">IRS Publication 946</a> for how Section 179 and '
             "depreciation work on business vehicles. <strong>Confirm the treatment "
             "with your CPA.</strong></li>"
             "<li><strong>Leasing</strong> usually means a lower monthly payment and a "
             "predictable replacement cycle, which suits a fleet that must look "
             "presentable, but you own nothing at the end unless you exercise a "
             "buyout.</li>"
             "</ul>"
             "<p>For a fleet that gets hard use and high mileage, ownership tends to "
             "win on total cost. For one that must present well to clients and be "
             "refreshed regularly, leasing often fits better.</p>"),
            ("Sequencing Against Contract Wins",
             "<p>Equipment spend on this side of the business is usually triggered by "
             "a contract, which creates the same timing problem as everything else "
             "here &mdash; the vehicles are needed before the contract pays.</p>"
             "<ul>"
             "<li><strong>Finance the vehicles</strong> rather than buying them "
             "outright from working capital, so the cash stays available for "
             "payroll.</li>"
             "<li><strong>Keep the small kit on a line of credit</strong>, repaid as "
             "invoices settle.</li>"
             "<li><strong>Do not fund equipment from a factoring advance</strong> "
             "&mdash; factoring is priced for a short receivable cycle, not for an "
             "asset you will hold for years.</li>"
             "<li><strong>Check the insurance implications</strong> before ordering. "
             "Adding vehicles changes your commercial auto position, which the "
             "contract may specify; see "
             '<a href="../bonding-and-insurance-costs-for-guard-contracts/">bonding '
             "and insurance costs</a>.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("Can I finance patrol vehicles for my guard company?",
             "Yes, and they are among the easier assets to finance. Patrol vehicles "
             "are titled, individually valuable and have a deep resale market, so a "
             "lender can identify, secure and if necessary sell them."),
            ("Can radios and body cameras be financed?",
             "Rarely on their own. They are low value per unit, spread across staff, "
             "prone to loss and damage, and have a thin resale market, so there is "
             "little for a lender to secure against. A line of credit or vendor terms "
             "usually fits better."),
            ("Should I lease or buy patrol vehicles?",
             "Buying leaves you owning a depreciating asset with residual value and "
             "suits hard-use, high-mileage fleets. Leasing gives a lower payment and a "
             "predictable refresh cycle, which suits a fleet that must present well. "
             "Confirm any tax treatment with your CPA."),
            ("What term should I finance equipment over?",
             "No longer than the asset's useful life. Financing radios over five years "
             "when you replace them in three means paying for kit you no longer use "
             "while also paying for its replacement. Vehicles tolerate longer terms "
             "because they genuinely last."),
            ("Should I use a factoring advance to buy equipment?",
             "No. Factoring is priced for a short receivable cycle, not for an asset "
             "held over years, so using it that way is expensive. Finance the vehicle "
             "and keep the factoring for the payroll gap it is designed for."),
        ],
        "related": [
            ("/security-guard-business-financing.html", "Security guard company financing"),
            ("/equipment-financing.html", "Equipment financing"),
            ("../bonding-and-insurance-costs-for-guard-contracts/",
             "Bonding and insurance costs for guard contracts"),
            ("../guard-payroll-between-invoices/", "Covering guard payroll between invoices"),
        ],
        "sources": [IRS_946, SBCS, CFPB],
    },
    {
        "slug": "cash-requirements-to-win-larger-guard-contracts",
        "crumb": "Winning Larger Contracts",
        "title": "Cash Requirements to Win Larger Guard Contracts | Axiant",
        "og_title": "The Cash Required to Win Larger Guard Contracts",
        "h1": "Cash Requirements to Win Larger Guard Contracts",
        "headline": "Cash Requirements to Win Larger Guard Contracts",
        "lede": "What a step up in contract size actually demands before the "
                "first payment arrives",
        "meta_desc": "Larger guard contracts demand cash before they pay: higher "
                     "insurance limits, recruitment, uniforms and weeks of payroll. "
                     "How to size the requirement and finance it.",
        "article_desc": "How to size and finance the cash a larger guard contract "
                        "requires before it pays.",
        "keywords": "win larger guard contracts, security contract mobilisation, "
                    "guard company growth capital, scaling security company",
        "quick_answer": "Model the requirement as <strong>weeks of payroll before "
                        "the first payment</strong>, plus mobilisation. A contract "
                        "billed monthly on net-45 can mean roughly "
                        "<strong>two to three months of wages funded up front</strong> "
                        "before any revenue lands &mdash; on top of higher insurance "
                        "limits, recruitment and uniforms. Size that number before "
                        "bidding, not after winning.",
        "sections": [
            ("The Cost of Winning",
             "<p>A larger contract is a cash event before it is a revenue event, and "
             "the outflows arrive in a predictable order:</p>"
             "<ul>"
             "<li><strong>Higher insurance limits</strong>, bound before the start "
             "date</li>"
             "<li><strong>Bonding</strong>, where the contract requires it</li>"
             "<li><strong>Recruitment and screening</strong> &mdash; advertising, "
             "background checks, licensing for new officers</li>"
             "<li><strong>Training</strong>, paid and delivered before the first "
             "shift</li>"
             "<li><strong>Uniforms and equipment</strong> for every new officer</li>"
             "<li><strong>Vehicles</strong> where the contract needs patrol "
             "coverage</li>"
             "<li><strong>Weeks of payroll</strong> before the first invoice is even "
             "issued</li>"
             "</ul>"
             "<p>The last one dwarfs the rest on a labour-intensive contract, and it "
             "is the one most often left out of the model.</p>"),
            ("Sizing It Properly",
             "<p>The arithmetic is simple and worth doing explicitly rather than by "
             "feel.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Input</th><th>What to use</th></tr></thead><tbody>"
             '<tr><td data-label="Input">Weekly payroll for the contract</td>'
             '<td data-label="Use">Wages plus employer taxes and workers\' '
             "compensation, not the headline wage</td></tr>"
             '<tr><td data-label="Input">Weeks until the first invoice</td>'
             '<td data-label="Use">Your billing cycle &mdash; a month if billed '
             "monthly in arrears</td></tr>"
             '<tr><td data-label="Input">Payment terms</td>'
             '<td data-label="Use">What the contract says, plus how that client '
             "actually pays</td></tr>"
             '<tr><td data-label="Input">Mobilisation costs</td>'
             '<td data-label="Use">Recruitment, training, uniforms, equipment, '
             "insurance step-up</td></tr>"
             '<tr><td data-label="Input">A margin for slippage</td>'
             '<td data-label="Use">First invoices are disputed or delayed more often '
             "than later ones</td></tr>"
             "</tbody></table></div>"
             "<p>Payroll multiplied by the weeks before payment, plus mobilisation, "
             "plus a margin. That figure is the real entry price of the contract, and "
             "it is frequently a large multiple of the monthly invoice.</p>"),
            ("Fund It Before You Sign, Not After",
             "<p>The order matters more than the instrument.</p>"
             "<p>Arranging finance after winning means negotiating under time pressure "
             "with a start date already agreed, which is the weakest possible "
             "position. Arranging it before means you know whether you can afford the "
             "contract while you can still decline it.</p>"
             "<p>Most funders will discuss a facility on the basis of a contract you "
             "are bidding for rather than one already signed, particularly where the "
             "client is creditworthy &mdash; which is the point of "
             '<a href="../guard-payroll-between-invoices/">factoring against your '
             "client's credit rather than yours</a>. Have the conversation at bid "
             "stage.</p>"),
            ("Which Instruments Cover Which Costs",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Cost</th><th>Best fit</th><th>Why</th></tr></thead><tbody>"
             '<tr><td data-label="Cost">Payroll after invoicing starts</td>'
             '<td data-label="Fit">Invoice factoring</td>'
             '<td data-label="Why">Scales with billing; no fixed limit to outgrow</td></tr>'
             '<tr><td data-label="Cost">Payroll before the first invoice</td>'
             '<td data-label="Fit">Line of credit</td>'
             '<td data-label="Why">No invoice exists yet for factoring to advance '
             "against</td></tr>"
             '<tr><td data-label="Cost">Insurance step-up</td>'
             '<td data-label="Fit">Premium finance</td>'
             '<td data-label="Why">Turns a lump sum into a run rate</td></tr>'
             '<tr><td data-label="Cost">Vehicles</td>'
             '<td data-label="Fit">Equipment finance</td>'
             '<td data-label="Why">Titled and liquid; keeps cash free for payroll</td></tr>'
             '<tr><td data-label="Cost">Recruitment and uniforms</td>'
             '<td data-label="Fit">Line of credit or working capital</td>'
             '<td data-label="Why">Nothing to secure against</td></tr>'
             "</tbody></table></div>"
             "<p>The pattern: anything before the first invoice needs a facility that "
             "does not depend on an invoice existing.</p>"),
            ("When to Decline",
             "<p>Worth saying plainly, because growth is treated as an unqualified "
             "good and it is not.</p>"
             "<p>A contract is worth declining when the cash requirement exceeds what "
             "you can fund and the shortfall would come out of existing clients' "
             "service. Losing a good contract you already hold in order to staff a new "
             "one is a bad trade, and it happens.</p>"
             "<p>It is also worth declining when winning it would concentrate too much "
             "revenue in one client &mdash; which affects your risk and your access to "
             "funding, since funders look hard at concentration.</p>"
             "<p>Public-sector work advertised through "
             '<a href="https://sam.gov/" rel="noopener nofollow" target="_blank">'
             "SAM.gov</a> is worth a particular look on this point: the contracts are "
             "large and reliable, and the payment cycles are long enough that the "
             "working capital requirement is correspondingly bigger.</p>"),
        ],
        "faqs": [
            ("How much cash does a larger guard contract require?",
             "Model it as weekly payroll multiplied by the weeks until the first "
             "payment arrives, plus mobilisation costs and a margin for slippage. On "
             "monthly billing with net-45 terms that can mean roughly two to three "
             "months of wages funded before any revenue lands."),
            ("What costs come before the first invoice?",
             "Higher insurance limits, any bonding, recruitment and screening, paid "
             "training, uniforms and equipment, vehicles where patrol coverage is "
             "required, and weeks of payroll. On a labour-intensive contract the "
             "payroll dwarfs everything else."),
            ("Should I arrange funding before or after winning?",
             "Before. Arranging finance after a win means negotiating under time "
             "pressure with a start date already agreed. Most funders will discuss a "
             "facility on the basis of a contract you are bidding for, especially "
             "where the client is creditworthy."),
            ("Can factoring cover mobilisation costs?",
             "No, because there is no invoice yet for a funder to advance against. "
             "Factoring works from the first billing onward; costs before that need a "
             "line of credit, premium finance or working capital."),
            ("When should I turn a contract down?",
             "When the cash requirement exceeds what you can fund and the shortfall "
             "would degrade service to clients you already have, or when the contract "
             "would concentrate too much revenue in one client &mdash; which raises "
             "your risk and narrows your access to funding."),
        ],
        "related": [
            ("/security-guard-business-financing.html", "Security guard company financing"),
            ("../guard-payroll-between-invoices/", "Covering guard payroll between invoices"),
            ("../bonding-and-insurance-costs-for-guard-contracts/",
             "Bonding and insurance costs for guard contracts"),
            ("/invoice-factoring.html", "Invoice factoring"),
        ],
        "sources": [SAM, SBCS, DOL_FLSA],
    },
]
