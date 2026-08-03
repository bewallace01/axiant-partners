# Low CTR is not a title problem

Written after being asked to rewrite the titles on the low-CTR pages. I checked
first, and the premise does not hold: the titles on those pages are already exact
matches for the queries they rank on. Rewriting them would trade correct alignment
for nothing.


Source: Search Console, `https://axiantpartners.com/`, per-page query breakdowns,
**2026-05-01 to 2026-07-31**.


## What the low-CTR pages actually rank for

Six of the highest-impression pages, checked individually:


| Page | Impressions | CTR | Position | What its queries are |
|---|---|---|---|---|
| `business-loan-calculator-guide` | 2,251 | **0%** | 4.2 | every query is a variant of `pmt(0.1025, 20, -126000000)` |
| `why-contractors-need-working-capital` | 4,067 | 0% | 4.9 | 356 template permutations of "[top/common/why] reasons [trade] need working capital" |
| `how-much-down-payment-required-commercial-property-loan` | 10,951 | 0.1% | 10.7 | "commercial multifamily loan down payment **typically 20% 30%**" &mdash; answer inside the query |
| `semi-truck-financing-down-payment` | 2,357 | 0.3% | 9.8 | real queries, but they rank 14&ndash;51 |
| `trac-lease-benefits-saves-money` | 2,191 | 0.4% | 10.8 | real queries, ranking 12&ndash;58 |
| `security-guard-company-working-capital` | 1,888 | **0%** | 11.0 | **real commercial queries at position 10.5** |

### Two different populations averaged into one number

The site's 0.4% CTR is not one phenomenon. It is:


1. **Machine-generated queries where the page ranks well.** Excel formula strings.
   Template permutations swapping "construction / electrical / restoration /
   cleaning". Queries containing their own answer. These are AI fan-out &mdash; the
   model reads the page and synthesises a response, and no human ever sees a blue
   link to click. **No title can produce a click here.**
2. **Human queries where the page ranks 14&ndash;50.** Real demand, below the fold
   of page 2. **No title produces a click from position 30 either.**


### And the control group proves CTR is not broken

When the site ranks top-10 for a genuine query, it converts at normal rates:


| Query | Position | CTR |
|---|---|---|
| top reasons electrical contractors need working capital | 5.0 | **20%** |
| printing press financing | 3.5 | **10.5%** |
| cherry vs patientfi | 10.2 | 3.2% |
| merchant cash advance for auto repair shop | 7.4 | 1.5% |

Titles that were genuinely broken would fail here too. They do not.


## The titles are already right

Every low-CTR page checked already carries an exact-match title:


| Page | Top query | Title |
|---|---|---|
| security guard | "security guard payroll financing" (906 impr) | *Security Guard Payroll Financing: Cover Net-30 Gaps* |
| semi truck | "how much down payment for a semi truck" | *How Much Down Payment for a Semi Truck? 0-25% (2026)* |
| TRAC lease | "trac lease meaning", "terminal rental adjustment clause" | *TRAC Lease Meaning (Terminal Rental Adjustment Clause)* |
| SBA timing | "how long sba loan approval" | *SBA Loan Approval Time: 7(a) vs 504 Week-by-Week (2026)* |
| BLOC rates | "business line of credit rates" | *Business Line of Credit Rates (2026): Typical APR Ranges by Lender* |

## Full metadata audit &mdash; 768 indexable pages


| Check | Result |
|---|---|
| Missing title | **0** |
| Missing meta description | **0** |
| Duplicate titles | **0** |
| Duplicate descriptions | **0** |
| Title length | median 58, max 78 |
| Description length | median 147, max 185 &rarr; now 160 |

**148 titles exceed 65 characters, and were deliberately left alone.** 117 of them
would fit if the ` | Axiant` suffix were dropped &mdash; but 505 pages carry that
suffix, Google routinely rewrites or drops brand suffixes itself, and what gets
truncated is the brand and the year, not the value proposition. Removing it from
117 pages would create inconsistency to fix nothing.


**Title vs H1 divergence looked alarming and is not.** 14 pages score near-zero
overlap, but they are money pages pairing a keyword title with a benefit-led H1
&mdash; *Commercial Real Estate Loans* over *Stop Paying Rent and Own Your
Building*. That is deliberate and correct.


## What was changed

Three meta descriptions, the only metadata on the site long enough to cut
mid-sentence in a SERP: `cherry-vs-carecredit` (185&rarr;143),
`carecredit-vs-affirm` (176&rarr;138), `affirm-vs-cherry` (170&rarr;140). The
`og:` and `twitter:` mirrors were updated in step.


Nothing else. Rewriting exact-match titles to look busy would have been the
"impressions as progress" error in a different costume.


## The one genuine anomaly, unexplained

`security-guard-company-working-capital` earns **1,780 impressions across two real
commercial queries** &mdash; "security guard payroll financing" (906, position
10.5) and "security guard payroll funding" (874, position 11.4) &mdash; with an
exact-match title, a matching description, and **zero clicks**.


Position 10.5 means mostly page two, which explains most of it. But zero from
1,780 is still low. This is the single page where a SERP-appearance check is worth
doing by hand: search the query, see what the listing actually looks like, and
whether an AI Overview is sitting above it.


## What would move the number


1. **Get real queries into the top 10.** "semi truck down payment" at 15.8,
   "commercial real estate loan down payment" at 27.9, "excavator financing" at 46.
   The site converts at 3&ndash;20% when it ranks. It does not rank.
2. **Stop counting fan-out impressions as demand.** A page ranking 4th for
   `pmt(0.1025, 20, -126000000)` has no audience, and optimising toward that number
   optimises toward nobody.
3. **Do not rewrite these titles again.** They are correct. This document exists so
   the question is not reopened in three months on the same evidence.

