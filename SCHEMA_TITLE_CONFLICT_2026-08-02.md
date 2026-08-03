# Google is not using your titles &mdash; it is using your schema headline

Follow-up to `TITLE_CTR_FINDINGS_2026-08-02.md`, which concluded that titles were
not the problem. **That conclusion was wrong in a specific way.** It verified the
`<title>` tag against the query and never checked what Google actually renders.


## The SERP that shows it

Query **"security guard payroll financing"** &mdash; 906 impressions, position 10.5,
**0 clicks**.


Every result above the Axiant listing carries the searcher's words in its title:


| # | Site | Displayed title |
|---|---|---|
| 1 | Payro Finance | Security Guard **Payroll Financing**: A Solution For Cash&hellip; |
| 2 | Payroll Funding | What Is Security Guard **Payroll Funding** & How Does it Work? |
| 3 | Advance Partners | Security Staffing **Payroll Funding**, Factoring & Back Office |
| 4 | SouthStar Capital | Security Guard Agency **Financing** |
| &hellip; | 1st Commercial Credit, Riviera, Biz2Credit, Byzfunder | all carry *payroll* and/or *financing* |
| ~9 | **Axiant Partners** | **Security Guard Company Working Capital** |

The page's `<title>` is *Security Guard Payroll Financing: Cover Net-30 Gaps* &mdash;
an exact match. Google ignored it.


## Why Google ignored it

The page named itself two different things, and one of them had three votes:


| Signal | Said |
|---|---|
| `<title>` | Security Guard **Payroll Financing**: Cover Net-30 Gaps |
| `og:title` | Security Guard **Payroll Financing**: Cover Net-30 Gaps |
| schema `headline` | Security Guard Company **Working Capital** |
| schema WebPage `name` | Security Guard Company **Working Capital** |
| URL slug | security-guard-company-**working-capital** |

Google took the majority and displayed a title containing neither *payroll* nor
*financing* &mdash; on a SERP where all eight competitors above it did.


That is a concrete, sufficient explanation for zero clicks on 906 impressions, and
it is not something the previous audit could see: the title tag was perfect.


## Fixed

`headline` and the WebPage `name` now match the title, and the H1 leads with the
exact phrase instead of burying it:


- headline: *Security Guard Company Working Capital* &rarr; *Security Guard Payroll Financing: Cover Net-30 Gaps*
- H1: *Security Guard Company Payroll Financing & Working Capital* &rarr; *Security Guard Payroll Financing: Covering Weekly Payroll on Net-30 Contracts*


**The slug is deliberately unchanged.** Renaming it needs a redirect, and risking a
page-one ranking to flip a signal now outvoted 4-1 the other way is the worse trade.
If the displayed title does not change within a few weeks, the slug is the next
lever.


## 49 other pages carry the same conflict

Pages whose schema `headline` shares less than half its content words with the
`<title>`. These were **not** changed &mdash; there is SERP evidence for one page,
and inference for the rest, and on several the headline is the *better* string:


| Page | `<title>` | `headline` |
|---|---|---|
| `business-line-of-credit/articles/line-of-credit-for-ecommerce-inventory` | LOC for E-Commerce Inventory | Line of Credit for Ecommerce Inventory: Revolving Use, Peak-Season Stocking |
| `business-growth/articles/unit-economics-scaling-without-bankruptcy` | Unit Economics: How to Scale Without Going Broke | How to Avoid Scaling Yourself Into Bankruptcy: Unit Economics Every Owner Should T |
| `business-line-of-credit/articles/business-line-of-credit-for-startups` | Startup Business Line of Credit: Under 2 Years | How New Businesses Get a Line of Credit Before the Two-Year Mark |
| `merchant-cash-advance/articles/how-to-apply-merchant-cash-advance` | How to Apply for an MCA | How to Apply for a Merchant Cash Advance (Step-by-Step) |
| `sba-loans/articles/why-sba-loan-approval-taking-forever` | SBA Loan Stuck in Underwriting? 5 Common Stalls (2026) | Why Your SBA Loan Approval Is Taking Forever |
| `business-debt-relief/articles/release-ucc-lien-business` | UCC Lien Release: How to Remove a UCC Filing | How To Get a UCC Lien Released From Your Business |
| `sba-loans/articles/sba-loan-veterinary-practice` | SBA Loans for Veterinary Practices: Buy, Build, Equip (2026) | SBA Loan for Veterinary Practice |
| `articles/why-applying-multiple-banks-blindly-hurts-approval-odds` | Why Multiple Bank Applications Hurt Loan Odds (2026) | Why Applying to Multiple Banks Blindly Hurts Your Approval Odds (and What to Do In |
| `business-line-of-credit/articles/documents-needed-business-line-of-credit` | Business LOC Document Checklist | Documents Needed for a Business Line of Credit (Checklist) |
| `equipment-financing/articles/equipment-financing-tax-returns-losses` | Equipment Financing: Tax Losses & Cash Flow | Equipment Financing When Tax Returns Show a Loss (How to Get Approved) |
| `merchant-cash-advance/articles/mca-for-auto-repair-shops` | Merchant Cash Advance for Auto Repair | MCA for Auto Repair Shops |
| `commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026` | Commercial Mortgage Rates in 2026 by Lender Type | Typical Commercial Real Estate Loan Rates in 2026 by Property and Lender |
| `equipment-financing/articles/equipment-financing-ucc-lien-approval` | UCC Liens Blocking Equipment Financing? Clear in 3 Steps | Equipment Financing with a UCC Lien: How to Get Approved |
| `business-line-of-credit/articles/reasons-line-of-credit-draw-request-gets-declined` | LOC Draw Declined: Reasons & Fixes | Reasons Your Line of Credit Draw Request Gets Declined |
| `business-growth/articles/slow-season-leads-offers-working-capital` | How to Survive a Slow Season: Leads & Cash Flow | How to Survive a Slow Season: Leads, Offers, and Working Capital in the Right Orde |
| `commercial-real-estate-loans/articles/cash-out-refinance-commercial-property` | Commercial Cash-Out Refinance: Pull Equity From CRE | Commercial Cash-Out Refinance: How It Works, LTV and DSCR |
| `construction-business-financing/material-deposits-supplier-cod-before-first-payment` | Material Deposits & Supplier COD Cash Crunch | Material Deposits & Supplier COD Before First Payment: How Contractors Bridge It |
| `trucking-business-financing/deadhead-miles-cash-drain` | Deadhead Miles Cash Drain: Trucking Fixes | Deadhead Miles Cash Drain: How Carriers Reduce Empty-Mile Losses |
| `business-line-of-credit/articles/line-of-credit-for-contractors` | Line of Credit for Contractors | Line of Credit for Contractors: Draw Timing, Seasonal Projects, Bonding |
| `equipment-financing/articles/carecredit-vs-patientfi-imaging-radiology` | PatientFi vs CareCredit vs Cherry: Which to Offer | CareCredit vs PatientFi vs Affirm vs Cherry for Imaging & Radiology |
| `equipment-financing/articles/equipment-financing-requirements` | Equipment Financing Requirements: FICO, Time & Docs | Equipment Financing Requirements: What You Need to Qualify |
| `equipment/diagnostic-equipment-auto/scan-tool-financing` | Automotive Scan Tool & Diagnostic Equipment Financing | Scan Tool Financing for Auto Shops |
| `fix-and-flip/articles/fix-and-flip-mistakes-to-avoid` | Fix-and-Flip Mistakes to Avoid | Fix and Flip Mistakes That Kill Your Deal or Your Profit |
| `merchant-cash-advance/articles/red-flags-mca-agreements` | MCA Agreement Red Flags | Red Flags in Merchant Cash Advance (MCA) Agreements |
| `sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify` | SBA Loan Alternatives: 5 Options if Denied (2026) | SBA Loan Alternatives When You Don't Qualify |
| `working-capital-loans/articles/working-capital-loan-seasonal-businesses` | Seasonal Working Capital: Loans, Timing and Amounts | Working Capital Loan for Seasonal Businesses |
| `construction-business-financing/bonding-capacity-surety-cash-crunch` | Bonding Capacity Cash Crunch: Contractor Fixes | Bonding Capacity Cash Crunch: How Contractors Qualify for Bigger Jobs |
| `construction-business-financing/change-orders-delaying-payments` | Change Orders Delaying Payments? Contractor Fixes | Change Orders Delaying Payments? How Contractors Fix the Cash Gap |
| `construction-business-financing/weather-delay-cash-crunch` | Weather Delay Cash Crunch: Contractor Fixes | Weather Delay Cash Crunch: How Contractors Bridge Standby Costs |
| `merchant-cash-advance/articles/mca-for-restaurants` | MCA for Restaurants | MCA for Restaurants: What to Know Before You Sign |

Several show the reverse problem &mdash; the title is an abbreviation and the
headline is the fuller keyword match:


- *LOC for E-Commerce Inventory* vs *Line of Credit for Ecommerce Inventory*
- *How to Apply for an MCA* vs *How to Apply for a Merchant Cash Advance*
- *Business LOC Document Checklist* vs *Documents Needed for a Business Line of Credit*

On those the fix is to improve the **title**, not to overwrite the headline with an
abbreviation. Each needs its query data read before choosing a winner, which is why
none were touched.


## What this corrects

`TITLE_CTR_FINDINGS_2026-08-02.md` said *"do not rewrite these titles again, they
are correct."* The titles are correct. The finding that was missing is that a
correct title can be overridden by structured data that disagrees with it, and
checking the tag is not the same as checking the SERP.


The rest of that document stands: the fan-out impressions are still fan-out, the
control-group CTRs are still healthy, and there is still no evidence that mass title
rewriting would help. What changed is that **schema/title conflict is a real,
measurable defect class**, and there are 49 more instances of it.

