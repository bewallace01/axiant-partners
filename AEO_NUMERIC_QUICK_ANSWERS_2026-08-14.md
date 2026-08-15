# AEO pass: numeric Quick Answers + HowTo schema (2026-08-14)

## Why

Clicks looked like they were collapsing. They were not: rolling 7-day clicks ran 53 -> 65 -> 82 -> 73
over the four weeks to 2026-08-13, near a record. What is real is that impressions went from
~1,300/day in mid-July to ~3,400/day, so site CTR fell from ~0.6% to ~0.3% by arithmetic.

The actual constraint is AI Overview absorption. Live SERP check on 2026-08-14 (DataForSEO
`serp/google/organic/live/advanced`, one keyword per POST):

| query | AI Overview | cites us | our rank |
|---|---|---|---|
| security guard payroll financing | yes | no | 6 |
| commercial real estate loan down payment | yes | no | 11 |
| trucking business financing | yes | no | - |
| patientfi vs carecredit | yes | no | 7 |
| securities based lending | yes | no | - |
| vending machine financing | yes | **YES** | 9 |
| business loan calculator | no | - | - |

Seven of eight carry an AI Overview above the first organic result and we are cited in one.

## The thesis

The one cited page (`vending-machine-financing`) earns 12 clicks on 1,581 impressions. The
comparable uncited page (`security-guard-company-working-capital`) earns 1 on 1,612. Structural
difference:

| | vending machine (cited) | security guard (not cited) |
|---|---|---|
| HowTo schema | yes, 5 HowToSteps | none |
| Q&A pairs | 9 | 6 |
| Quick Answer content | `$3K-$10K, $5K-$12K, $15K-$50K` | "bridge a payroll-heavy gap" |

So: make the extractable blocks numeric, and add HowTo schema. All figures used were already
stated in each page's body. Nothing was invented.

## Target selection (three of the original six were rejected)

Impression counts alone pick the wrong pages. Query mix was checked per page before editing.

**Rejected as false targets:**

- `business-loan-calculator-guide` - 100% of its 410 impressions are one Excel formula string,
  `pmt(0.1025, 20, -126000000)`. Position 3.3 is a machine artifact. Page was also already fully
  optimized (numeric Quick Answer, numeric rail, HowTo). No edit made.
- `securities-based-lending` - 608 of 723 impressions come from a single persona-prompt fan-out
  query. Real queries ("securities backed loan", "securities based lending rates") rank 59-82.
  Authority-blocked; schema will not move it.
- `trucking-business-financing` - dominated by the "commercial trucking equipment and working
  capital financing for independent owner-operators" fan-out cluster. Real queries rank 28-36.

**Edited (5 files):**

| page | impr/30d | clicks | real query positions | change |
|---|---|---|---|---|
| working-capital-loans/articles/security-guard-company-working-capital | 1,527 | 1 | 8-9, all 18 queries human | body Quick Answer -> numeric, rail -> numeric, +HowTo |
| equipment-financing/articles/carecredit-vs-patientfi-imaging-radiology | 1,779 | 4 | 7-9 | +HowTo (blocks already numeric) |
| commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan | 2,206 | 1 | 11-30 | rail -> numeric, +HowTo |
| business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit | 717 | 0 | 6-16 | rail -> numeric, +HowTo |
| equipment/semi-trucks/semi-truck-financing-down-payment | 559 | 0 | 13-17, all 80 queries human | speakable answer + rail -> numeric, +HowTo |

**Checked, already compliant, left alone:** `equipment-financing/articles/patient-financing-imaging-centers`
(406 impr, 0 clicks, all 9 queries human) already had a numeric Quick Answer, a numeric rail, and
HowTo schema. Its problem is ranking depth at position 11-15, not an extractability gap. This is
the honest caveat on the thesis: extractability is necessary, not sufficient.

## Baselines to measure against (GSC, 30 days to 2026-08-13)

```
page                                          impr   clicks   pos
security-guard-company-working-capital        1527      1     ~8-9 on money queries
carecredit-vs-patientfi-imaging-radiology     1779      4     7.7 on "patientfi vs carecredit"
how-much-down-payment-required...             2206      1     11.1 on "commercial real estate loan down payment"
how-fast-can-you-get-approved...               717      0     9.5 on "how long does it take to get a business line of credit"
semi-truck-financing-down-payment              559      0     14.0 on "how much down payment for a semi truck"
patient-financing-imaging-centers (control)    406      0     11.2 on "imaging financing service"
```

Site-wide at time of change: 90-day 523 clicks / 125,963 impressions / avg position 17.7.

## How to measure

1. `cd Axiant-Partners-CRM && npm run audit:gsc-pull axiant-site` (service account
   `gsc-reader@bridge-seo.iam.gserviceaccount.com`, key at `scripts/gsc/.service-account.json`).
2. Re-run the AI Overview citation check on the same 8 queries. **The primary success metric is
   citation count, not rank and not CTR.** Rank is already fine on these pages.
3. `patient-financing-imaging-centers` is the control: unchanged, same profile. If it moves too,
   the cause was not these edits.

Re-check on or after **2026-09-04** (3 weeks). Expect nothing before then; AI Overview membership
re-evaluates slowly.

## Caveat on attribution

74% of this site's clicks sit in Google's anonymized bucket and AI-assistant referrals never appear
in GSC at all. `match.html` still captures no referrer, UTM, or landing page, so none of this can be
tied to applications yet. That fix remains unbuilt and is the higher-value project.
