# Site audit part 5 — query-demand targeting

Part 5 of 5. Search Console, `https://axiantpartners.com/`, **2026-05-02 to
2026-08-01**. Baseline: **422 clicks, 109,000 impressions, CTR 0.4%, average
position 16.8**.


## First, the long-tail premise

The brief assumed long tail helps. On this site it does not, and the data is
unambiguous:


| Query length | Impressions | Median position | Clicks |
|---|---|---|---|
| 2&ndash;3 words (head) | 5,401 | 35.7 | **39** |
| 7+ words (long tail) | 4,592 | **9.2** | **0** |

The site already ranks ninth for long tail and earns nothing from it, because
those queries are AI fan-out rather than people. The single largest query on the
site is *"i have a $10m+ investment portfolio and need liquidity without selling
assets — what lending options are available through a private bank?"* at **1,007
impressions, position 4.5, zero clicks**. Nobody types that.


So this part audits **demand-matched targeting**: where is there real commercial
demand, and what is standing between the site and the click.


## Three patterns, three different problems

Taking the highest-volume human commercial queries and asking, for each, how many
of the site's own pages Google shows:


### 1. Cannibalization &mdash; seven pages, one query

**"imaging patient financing"** &mdash; 689 impressions, average position 36.4


| Page | Impressions | Position |
|---|---|---|
| `patient-financing-imaging-centers` | 219 | **7.8** |
| `carecredit-vs-patientfi-imaging-radiology` | 197 | 21.3 |
| `equipment/medical-imaging/` | 184 | 53.2 |
| `mri-ct-scanner-financing` | 148 | 79.3 |
| `medical-imaging-financing-radiology-practices` | 84 | 44.6 |
| `used-medical-imaging-financing` | 12 | 78.1 |
| `radiology-practice-financing-complete-guide` | 1 | 75.0 |

**The best page ranks 7.8 &mdash; page one.** It is shown for less than a third
of the query's impressions. The other six, ranking 21 to 79, drag the average to
36.4 and take the impressions with them.


`"radiology patient financing"` behaves identically: 544 impressions, six pages,
best at **10.0**, average 40.9.


The cluster totals roughly **3,200 impressions** of real commercial demand.


### 2. One page, right target, weak authority

**"electrical contractor funding"** &mdash; 576 impressions, position 32.7


| Page | Impressions | Position |
|---|---|---|
| `electrical-contractor-financing` | 572 | 32.7 |
| `contractor-financing.html` | 4 | 40.2 |

One page, correctly targeted, consistently 33rd. Nothing to consolidate. This is
an authority problem and no on-page change will move it.


### 3. One page, already at the page-one boundary

**"security guard payroll financing"** &mdash; 932 impressions, position 10.5


| Page | Impressions | Position |
|---|---|---|
| `security-guard-company-working-capital` | 932 | 10.5 |

One page taking every impression, sitting on the boundary between page one and
page two. With its sibling *"security guard payroll funding"* at 895 impressions
and position 11.4, this is **1,827 impressions three places from the fold**, and
the closest thing to a free win on the site.


## This corrects the cannibalization finding from earlier today

`CANNIBALIZATION_FINDINGS_2026-08-02.md` and
`PER_QUERY_PAGE_FINDINGS_2026-08-02.md` concluded that **none of nine pairs was
cannibalization**. That conclusion was right about those nine pairs and wrong
about the site, because the method could not see this:


- It compared **pairs**. The imaging problem is a group of **seven**.
- It started from **title similarity**. These seven titles are quite different
  &mdash; *Patient Financing for Imaging & Radiology Centers*, *Medical Imaging
  Equipment Financing*, *CareCredit vs PatientFi vs Cherry*. Nothing about them
  pairs up.
- It asked *do two similar pages both earn impressions*. The right question is
  **for a query with demand, how many of my pages does Google show**.


The earlier documents are not withdrawn &mdash; nine pairs really were not
cannibalization, and the excavator advice still stands. But the site does have
cannibalization, in the patient-financing cluster, and the screen was pointed the
wrong way to find it.


## What to do, in order


1. **Security guard payroll** &mdash; 1,827 impressions at 10.5 and 11.4, one page,
   no competition from your own site. Three places from page one. The schema and
   title work shipped today already targets it; the crawl was requested; this is
   the one to watch first.
2. **Consolidate the imaging/radiology cluster** &mdash; roughly 3,200 impressions
   split across six or seven pages where one of them already ranks 7.8. Pick that
   page as the target for the category terms and point the others at it, or
   differentiate them onto genuinely different intents. This is the largest
   recoverable block of demand on the site.
3. **Electrical contractor funding** &mdash; 576 impressions at 32.7 with a single
   well-targeted page. Nothing on-page will fix it. File under authority.
4. **Stop optimising for fan-out.** Two thirds of this site's impressions come
   from queries that convert at zero by construction. A page written to serve them
   is written for nobody.


## The honest ceiling

Every genuinely commercial query on this site sits at position 10 or worse. The
site converts at 3&ndash;20% when it reaches the top ten &mdash; *printing press
financing* 10.5% at 3.5, *electrical contractors working capital* 20% at 5.0,
*cherry vs patientfi* 3.2% at 10.2. The mechanism works. It just rarely gets
there, and that is a link-authority constraint rather than anything markup can
reach.

