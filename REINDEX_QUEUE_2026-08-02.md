# Re-index queue - pages Google crawled and declined

> **CORRECTED 2026-08-03.** The first version listed `/services`, `/blog`,
> `/vendors` and `/terms-and-conditions` as the top priorities. They are
> extensionless duplicates that correctly canonicalise to their `.html` twins,
> and the `.html` pages are indexed. Google declining to index a canonicalised
> duplicate is the intended outcome, not a failure. They are removed from the
> queue entirely. Corrected total: **86** genuine rejections, not 90.

Ranked by inbound internal links (the site's own vote of importance), then length.
Search Console > URL inspection > paste URL > REQUEST INDEXING.

**Quota is a rolling window, not a daily reset.** 10 URLs were submitted on
2026-08-02 and 2 on 2026-08-03; the third attempt on the 3rd returned *"you've
exceeded your daily quota"*. Assume roughly a dozen per rolling 24 hours and
expect the allowance to still be spent the next morning.

Resubmitting a URL wastes a slot &mdash; Google's own dialog says submitting a
page again "will not change its queue position or priority". At least two slots
went that way on 2026-08-02 because the confirmation dialog steals focus, so the
next URL never loads and the button re-fires on the previous one. Confirm the
inspected URL in the header before clicking.

**On hold as of 2026-08-03.** At a dozen a day this is eight more sessions for 78
pages, and the sitemap `lastmod` refresh already covers all 86 at once at no
further cost. If that works the queue is redundant; if it does not, hand-feeding
78 URLs is unlikely to save them either. Revisit only if the March cohort has not
moved a few weeks after the crawl.

## Not in the queue - canonicalised duplicates, working as intended

- https://axiantpartners.com/vendors &rarr; canonical `/vendors.html` (indexed)
- https://axiantpartners.com/terms-and-conditions &rarr; canonical `/terms-and-conditions.html` (indexed)
- https://axiantpartners.com/blog &rarr; canonical `/blog.html` (indexed)
- https://axiantpartners.com/services &rarr; canonical `/services.html` (indexed)

## Submitted 2026-08-02

- [x] https://axiantpartners.com/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/   (270 links, 1712 words)
- [x] https://axiantpartners.com/equipment-financing/articles/what-credit-score-needed-equipment-financing/   (190 links, 1469 words)
- [x] https://axiantpartners.com/equipment-financing/articles/equipment-financing-requirements/   (79 links, 2256 words)
- [x] https://axiantpartners.com/restaurants-business-financing.html   (53 links, 2806 words)
- [x] https://axiantpartners.com/working-capital-loans/articles/business-loans-for-bad-credit/   (41 links, 4091 words)
- [x] https://axiantpartners.com/logistics-warehousing-business-financing.html   (35 links, 2838 words)
- [x] https://axiantpartners.com/equipment-financing/articles/equipment-financing-vs-sba-loan/   (33 links, 1922 words)
- [x] https://axiantpartners.com/equipment/semi-trucks/   (32 links, 3260 words)

## Submitted 2026-08-03 - after rewriting both pages

- [x] https://axiantpartners.com/services.html   (762 links, 363 -> 1,303 words)
- [x] https://axiantpartners.com/blog.html   (123 links, 400 -> 1,274 words)

Both were already indexed. Requested because the content changed substantially,
which is what the *Page changed?* prompt on that button is for.


## Submitted 2026-08-04

Queue taken off hold. Five submitted, each confirmed by the *"Indexing
requested &mdash; URL was added to a priority crawl queue"* dialog:

- [x] https://axiantpartners.com/equipment/medical-imaging/   (last crawl Jul 6)
- [x] https://axiantpartners.com/landscaping-business-financing.html   (last crawl Apr 10)
- [x] https://axiantpartners.com/revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/
- [x] https://axiantpartners.com/equipment-financing/articles/equipment-financing-new-businesses/
- [x] https://axiantpartners.com/business-line-of-credit/articles/business-line-of-credit-for-startups/   (Discovered, **never crawled**)
- [x] https://axiantpartners.com/equipment-financing/articles/construction-heavy-equipment-financing/
- [x] https://axiantpartners.com/equipment/cargo-vans/   (last crawl May 29)
- [x] https://axiantpartners.com/equipment/auto-lifts/
- [x] https://axiantpartners.com/equipment/dump-trucks/   (last crawl Jun 8)
- [x] https://axiantpartners.com/trucking-business-financing/fuel-advance-cash-crunch/   (last crawl May 18)

**Ten submitted, two skipped as already indexed, and then the wall.** The
eleventh attempt &mdash; `construction-business-financing/retainage-cash-flow-gap/`
&mdash; returned:

> **Quota Exceeded.** Sorry, we couldn't process this request because you've
> exceeded your daily quota. Please try submitting this again tomorrow.

**So the allowance is exactly 10 per rolling 24 hours for this property**, not
"roughly a dozen" as this doc previously guessed. Ten succeeded; the eleventh
was refused outright. Plan sessions around 10.

Note that the two already-indexed pages did **not** consume anything &mdash;
inspecting is free, and ten requests still went through after them.

Already indexed and struck from the queue:

- `articles/how-to-prequalify-business-loan/`
- `equipment/dental-equipment/`

That is **2 of the 10 inspected**, both listed here as rejections. Extrapolating
naively, something like a fifth of the remaining 70 may no longer need anything
&mdash; which is why the next session should inspect before it clicks.


### The queue is stale &mdash; verify status before spending a slot

`https://axiantpartners.com/articles/how-to-prequalify-business-loan/` is
**already indexed**. It sits in this queue as a rejection, and inspecting it
returns *"URL is on Google &mdash; Page is indexed"*. Submitting it would have
burned a slot on a page that needs nothing.

**Inspecting a URL costs no quota; only Request Indexing does.** So inspect
first, read the status, and only click for pages that still say *"URL is not on
Google"*. The remaining 73 should be re-checked this way rather than submitted
blind &mdash; some number of them have been picked up since 2026-08-02, which is
also the first real evidence that the sitemap `lastmod` refresh is working.


### Working procedure, and the three ways it fails

The confirmation dialog steals focus, and the failure is silent. What works:

1. Navigate to the console overview to get a clean page (no dialog).
2. Click the inspect box **in its own round trip** &mdash; a click batched
   immediately before typing does not take focus.
3. Type the URL, then **screenshot and confirm the text is in the box** before
   pressing Return.
4. After Return, **confirm the header shows the new URL** and the button reads
   *Request indexing*, not *Request again*.
5. Click, then wait ~30s and confirm the dialog text.

Three failures hit on 2026-08-04, all silent:

- After *Dismiss*, the next click on the search box is swallowed, so the typed
  URL goes nowhere and the header still shows the previous page.
- With focus lost, **Return activates the still-focused *Request again* button**
  and re-submits the page just done. Caught once and cancelled mid-test.
- Browser zoom flips to 250% on its own during a session, apparently from a
  keystroke landing outside the input. At that zoom the screenshot is in device
  pixels while `getBoundingClientRect` returns CSS pixels, so a click computed
  from the DOM lands in the wrong place. The fix that works: read the rect,
  `scrollIntoView`, then multiply by `devicePixelRatio` for the click. Check
  `window.devicePixelRatio` at the start of every page &mdash; it changes
  mid-session.


### What to verify with, instead of screenshots

Screenshots time out on this console often enough to be unreliable, and they
cannot distinguish the two status texts because **the DOM contains both** and
hides one. Read the visible leaf nodes instead:

```js
const vis = el => { const r = el.getBoundingClientRect();
  return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== 'hidden'; };
const txt = [...document.querySelectorAll('*')]
  .filter(e => e.children.length === 0 && vis(e))
  .map(e => (e.textContent || '').trim());
txt.find(t => /^URL is (not )?on Google$/.test(t))   // the real status
txt.some(t => /indexing requested/i.test(t))          // the real confirmation
```

An earlier check that ignored visibility reported *"URL is on Google"* for a
page that was plainly not indexed.


### One thing that does not work

`input.focus()` reliably focuses the box where clicking often does not &mdash;
but the typing that follows still goes nowhere, because the type action is
delivered at the OS level and the programmatic focus does not hold it. Focus has
to be established by a real click, in its own round trip.

## Remaining queue

- [x] https://axiantpartners.com/equipment/medical-imaging/   (32 links, 1306 words)
- [x] https://axiantpartners.com/landscaping-business-financing.html   (31 links, 3034 words)
- [x] https://axiantpartners.com/revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/   (30 links, 1931 words)
- [x] https://axiantpartners.com/equipment-financing/articles/equipment-financing-new-businesses/   (28 links, 1850 words)
- [x] https://axiantpartners.com/business-line-of-credit/articles/business-line-of-credit-for-startups/   (26 links, 2100 words)
- [~] https://axiantpartners.com/articles/how-to-prequalify-business-loan/  **already indexed &mdash; no request needed**   (24 links, 1787 words)
- [x] https://axiantpartners.com/equipment-financing/articles/construction-heavy-equipment-financing/   (20 links, 1722 words)
- [x] https://axiantpartners.com/equipment/cargo-vans/   (19 links, 2715 words)
- [~] https://axiantpartners.com/equipment/dental-equipment/  **already indexed &mdash; no request needed**   (18 links, 1189 words)
- [x] https://axiantpartners.com/equipment/auto-lifts/   (18 links, 1043 words)
- [x] https://axiantpartners.com/equipment/dump-trucks/   (16 links, 2637 words)
- [x] https://axiantpartners.com/trucking-business-financing/fuel-advance-cash-crunch/   (16 links, 2057 words)
- [ ] https://axiantpartners.com/construction-business-financing/retainage-cash-flow-gap/   (16 links, 1988 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/restaurant-commercial-kitchen-equipment-financing/   (16 links, 1815 words)
- [ ] https://axiantpartners.com/equipment/commercial-kitchen/   (16 links, 1258 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/medical-dental-equipment-financing/   (15 links, 2191 words)
- [ ] https://axiantpartners.com/merchant-cash-advance/articles/merchant-cash-advance-vs-working-capital-loan/   (15 links, 1253 words)
- [ ] https://axiantpartners.com/articles/business-loan-guarantee-traps/   (15 links, 1036 words)
- [ ] https://axiantpartners.com/fix-and-flip/articles/   (15 links, 441 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/equipment-financing-no-money-down/   (12 links, 2132 words)
- [ ] https://axiantpartners.com/startup-financing/articles/startup-financing-credit-score-guide/   (11 links, 1604 words)
- [ ] https://axiantpartners.com/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/   (11 links, 1369 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/working-capital-loan-traps-to-avoid/   (10 links, 1928 words)
- [ ] https://axiantpartners.com/business-line-of-credit/articles/what-credit-score-needed-business-line-of-credit/   (10 links, 1287 words)
- [ ] https://axiantpartners.com/commercial-bridge-loans/articles/how-fast-can-you-close-commercial-bridge-loan/   (10 links, 1260 words)
- [ ] https://axiantpartners.com/articles/why-applying-multiple-banks-blindly-hurts-approval-odds/   (10 links, 1165 words)
- [ ] https://axiantpartners.com/equipment/wheel-loaders/   (9 links, 2653 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/can-equipment-financing-help-build-business-credit/   (9 links, 1920 words)
- [ ] https://axiantpartners.com/startup-financing/articles/startup-financing-no-revenue-options/   (8 links, 2138 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/how-to-avoid-overpaying-equipment-financing/   (8 links, 2130 words)
- [ ] https://axiantpartners.com/startup-financing/articles/startup-working-capital-loan-under-30-days/   (8 links, 1839 words)
- [ ] https://axiantpartners.com/sba-loans/articles/sba-loan-vs-business-line-of-credit/   (8 links, 1414 words)
- [ ] https://axiantpartners.com/equipment/commercial-mowers/   (8 links, 1245 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/heavy-equipment-financing/   (8 links, 1191 words)
- [ ] https://axiantpartners.com/sba-loans/articles/sba-loan-franchise-acquisition/   (7 links, 1472 words)
- [ ] https://axiantpartners.com/restaurant-financing-guide/   (7 links, 948 words)
- [ ] https://axiantpartners.com/equipment/lab-equipment-medical/   (7 links, 930 words)
- [ ] https://axiantpartners.com/equipment/bucket-trucks/bucket-truck-financing-utility-contractors/   (7 links, 926 words)
- [ ] https://axiantpartners.com/sba-loans/articles/sba-loan-restaurant-acquisition/   (6 links, 2102 words)
- [ ] https://axiantpartners.com/construction-business-financing/contractor-financing-mistakes-delay-deny-funding/   (6 links, 1984 words)
- [ ] https://axiantpartners.com/articles/why-down-payment-not-enough-loan-you-want/   (6 links, 723 words)
- [ ] https://axiantpartners.com/merchant-cash-advance/articles/how-to-apply-merchant-cash-advance/   (5 links, 2046 words)
- [ ] https://axiantpartners.com/construction-business-financing/weather-delay-cash-crunch/   (5 links, 1947 words)
- [ ] https://axiantpartners.com/trucking-business-financing/deadhead-miles-cash-drain/   (5 links, 1913 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/why-your-working-capital-application-stuck-in-review/   (5 links, 1729 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/home-health-agency-working-capital/   (5 links, 1634 words)
- [ ] https://axiantpartners.com/revenue-based-financing/articles/why-revenue-based-financing-advance-lower-than-needed/   (5 links, 1278 words)
- [ ] https://axiantpartners.com/commercial-bridge-loans/articles/whats-holding-up-your-bridge-loan-funding/   (5 links, 1258 words)
- [ ] https://axiantpartners.com/manufacturing-financing-guide/   (5 links, 1124 words)
- [ ] https://axiantpartners.com/revenue-based-financing/articles/why-revenue-based-financing-not-working/   (5 links, 1095 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/dry-cleaning-equipment-financing/   (5 links, 1010 words)
- [ ] https://axiantpartners.com/equipment/surgical-equipment/   (5 links, 954 words)
- [ ] https://axiantpartners.com/equipment/restaurant-refrigeration/walk-in-cooler-freezer-financing/   (5 links, 930 words)
- [ ] https://axiantpartners.com/revenue-based-financing/articles/revenue-based-financing-traps/   (4 links, 2090 words)
- [ ] https://axiantpartners.com/trucking-business-financing/breakdown-repair-cash-crunch/   (4 links, 2071 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/what-do-lenders-look-for-working-capital-loan-application/   (4 links, 2026 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/equipment-financing-pre-approval/   (4 links, 1801 words)
- [ ] https://axiantpartners.com/fix-and-flip/articles/fix-and-flip-loan-first-time-flippers/   (4 links, 1719 words)
- [ ] https://axiantpartners.com/business-line-of-credit/articles/line-of-credit-for-ecommerce-inventory/   (4 links, 1621 words)
- [ ] https://axiantpartners.com/sba-loans/articles/what-documents-needed-sba-loan/   (4 links, 1567 words)
- [ ] https://axiantpartners.com/business-term-loans/articles/term-loan-for-manufacturing-expansion/   (4 links, 1368 words)
- [ ] https://axiantpartners.com/fix-and-flip/articles/fix-and-flip-loan-out-of-state-investors/   (4 links, 1367 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/what-credit-score-needed-working-capital-loan/   (4 links, 1349 words)
- [ ] https://axiantpartners.com/fix-and-flip/articles/whats-killing-fix-and-flip-profit/   (4 links, 993 words)
- [ ] https://axiantpartners.com/healthcare-practice-financing-guide/   (4 links, 936 words)
- [ ] https://axiantpartners.com/commercial-real-estate-loans/articles/multifamily-loan-down-payment/   (3 links, 1627 words)
- [ ] https://axiantpartners.com/working-capital-loans/articles/how-much-can-you-qualify-for-working-capital-loan/   (3 links, 1320 words)
- [ ] https://axiantpartners.com/equipment/mini-excavators/mini-excavator-financing-contractors/   (3 links, 872 words)
- [ ] https://axiantpartners.com/equipment-financing/articles/reasons-equipment-dealer-financing-falls-through/   (2 links, 2297 words)
- [ ] https://axiantpartners.com/business-term-loans/articles/business-term-loan-requirements/   (2 links, 1906 words)
- [ ] https://axiantpartners.com/sba-loans/articles/sba-loan-mistakes-delay-kill-approval/   (2 links, 1311 words)
- [ ] https://axiantpartners.com/commercial-real-estate-loans/articles/what-do-lenders-look-for-commercial-real-estate-loan/   (2 links, 1259 words)
- [ ] https://axiantpartners.com/business-line-of-credit/articles/red-flags-line-of-credit-offers/   (2 links, 1252 words)
- [ ] https://axiantpartners.com/equipment/excavators/excavator-lease-vs-loan/   (2 links, 1199 words)
- [ ] https://axiantpartners.com/merchant-cash-advance/articles/what-do-lenders-look-for-merchant-cash-advance/   (2 links, 1097 words)
- [ ] https://axiantpartners.com/business-term-loans/articles/term-loan-mistakes-cost-thousands/   (2 links, 978 words)
- [ ] https://axiantpartners.com/equipment/forklifts/used-forklift-financing/   (1 links, 1349 words)
- [ ] https://axiantpartners.com/faq.html   (1 links, 1030 words)

Total genuine rejections: 86 | submitted: 9 | remaining: 78
