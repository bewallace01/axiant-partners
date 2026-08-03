# Site audit part 3 — structured data, breadcrumbs and AEO

Part 3 of 5. Every check compares the markup against the **rendered page**,
because that is the only rule Google applies consistently to all of it: markup
must correspond to something a visitor can see.


## Clean

| Check | Result |
|---|---|
| JSON-LD blocks parsed | **3,233** |
| Invalid JSON-LD | **0** |
| Distinct schema types | 35 |
| `FAQPage` markup with no visible Q&A | **0** |
| Visible FAQ (3+ pairs) with no `FAQPage` markup | **0** |
| Pages with no paragraph after the H1 | 3 (calculator, home, a partner page) |

FAQ coverage is genuinely complete: 740 pages carry `FAQPage`, and every one
of them matches visible content in both directions.


## Fixed: 35 breadcrumbs named a step the page never shows

**This was my own regression, introduced earlier today.**


PR #193 aligned schema `headline` and WebPage `name` to the `<title>` on 74
pages. The replacement matched `"name": "<old value>"` anywhere in the file, so
it also rewrote the **last item of `BreadcrumbList`** &mdash; which represents the
current page as the visitor sees it, and should mirror the H1.


Verified against git history:


```
before #193   crumb: Why Your Line of Credit Limit Is Too Low   (= H1)
after  #193   crumb: Why Your Business Line of Credit Limit Is Low   (= title)
page H1                Why Your Line of Credit Limit Is Too Low
```

The final crumb now returns to the H1 on all 35. `headline` and the WebPage
`name` still point at the title &mdash; that half of #193 was correct and is what
Google renders as the SERP title. Only the breadcrumb changed back.


## Fixed: 52 nested pages had no breadcrumb at all

Added, copying the structure the other 652 pages already use. Three details
that the dry run caught before anything was written:


- For `section/slug/index.html`, the page's **own** directory was being emitted
  as a parent crumb, producing `Home > Section > Borrow To Grow Not To Survive
  The > [page]`. Parents are now everything above the page's own folder.
- Section labels were carrying a trailing `|` from splitting the title.
- One parent, `business-growth-financing/`, has articles but **no landing page**.
  That crumb is omitted rather than pointed at a URL that does not exist.


Breadcrumb coverage: **652 &rarr; 704**. Breadcrumbs naming an invisible step:
**35 &rarr; 0**.


## Reported, not changed


### 645 of 652 breadcrumbs are markup-only

Only **7 pages** render a visible breadcrumb trail. The other 645 carry the
structured data with nothing on screen.


Google commonly accepts this and the site already gets breadcrumb enhancements
reported in Search Console, so it is not breaking anything today. But the
general structured-data guideline is that markup should reflect visible content,
and a visible trail is also a genuine navigation aid on a site three levels deep.
Adding one sitewide is a design change across 645 pages &mdash; an owner's
decision, not an audit's. The 7 that have one use `<nav class="ef-breadcrumb">`,
so the pattern already exists.


### 64 root-level pages still have no breadcrumb

Skipped deliberately. `Home > Page` on a top-level URL conveys nothing Google
cannot already read from the URL itself.


### AEO lead coverage is 67%


| | Pages |
|---|---|
| "Quick answer" block | 515 of 768 |
| `SpeakableSpecification` | 538 |
| Substantive lead paragraph after the H1 | 560 |

Around 250 pages have no answer-first block. That is a content task rather than
a markup one and belongs with part 4, not a bulk edit here.


> **Corrected 2026-08-03.** The 515 count matched one class name and missed the
> other three block variants in use. Counting all of them &mdash; `quick-answer`,
> `blog-rail-quick-answer`, `article-quick-answer`, `tldr`, and the visible
> "Quick answer" / "Short answer" / "Quick Take" labels &mdash; the real figure
> was **584 of 768**, so **184** pages lacked a block, not ~250.
>
> Of those 184: 82 hub / landing / state pages, 66 articles, 19
> `equipment-for-sale` listings, and 17 article index pages where a direct
> answer does not belong.
>
> The 82 hubs are now done, less nine utility pages where the block is
> meaningless (the calculator, the contact and application forms, the FAQ page,
> the homepage, the industries directory, the partner application, and the two
> legal pages). **73 blocks added; coverage 584 &rarr; 657, missing 184 &rarr;
> 111.**
>
> The **57 `equipment/` category pages** followed. These were the easiest set to
> write well, because each page already carries its own cost tiers, term range,
> credit line and a worked payment example &mdash; so every answer leads with a
> direct yes, quotes that machine's own numbers, and closes on the thing an
> underwriter actually looks at for it (undercarriage percentage on an
> excavator, reefer unit hours on a refrigerated truck, the dielectric
> certificate on a bucket truck). **708 figures were checked against their own
> page before writing.** Coverage **657 &rarr; 714**, missing **111 &rarr; 54**.
>
> The **17 `equipment-for-sale/` pages** followed. These are dealer and
> manufacturer listing pages rather than financing guides, so each answer leads
> on the machine and closes on the financing, using that page's own
> specifications &mdash; Service King's depth ratings, SENNEBOGEN's lift
> figures, Mix Right's batch sizes, Albach's throughput.
>
> None of the 17 carried a `WebPage` node, so there was nothing for speakable to
> attach to &mdash; the property is valid on `WebPage` and `Article`, not on the
> `Product` and `ItemList` these pages use. A `WebPage` node was added in the
> shape `BLOG_POST_TEMPLATE.md` section 4 specifies, with every pre-existing
> JSON-LD payload compared byte for byte afterwards.
>
> Coverage **714 &rarr; 731**, missing **54 &rarr; 37**. Speakable **620 &rarr;
> 637**.
>
> Then the **root pages**. Sixteen lacked a block, but only **seven** are
> candidates: the two calculators (`dscr-calculator`, `mca-calculator`), the two
> sourced data reports (`small-business-lending-statistics`,
> `small-business-financing-report`), and the three section landing pages
> (`services`, `equipment`, `industries`). Between them they carry the strongest
> AEO material on the site &mdash; DSCR thresholds, factor-rate arithmetic,
> Federal Reserve approval rates, six years of SBA 7(a) loan-level data.
>
> The other **nine are not candidates** and are deliberately left: the loan
> calculator and contact form (no prose), the application form, the partner
> application form, the homepage (a designed landing experience, not a
> document), `faq.html` (already entirely question-and-answer, so a summary box
> duplicates its own first item), the two legal pages, and
> `articles/index.html`, a blog roll like the other article indexes.
>
> Coverage **731 &rarr; 738**, missing **37 &rarr; 30**.
>
> Finally the last **7 candidates**: four `articles/` guides (which loan is
> right, first-time borrower, improving approval odds, behind on payments), the
> `articles/` hub, and two `trucking-business-financing/` pages (growth, working
> capital). These are process and decision articles rather than product pages,
> so they carry far fewer numbers &mdash; only 4 figures across all seven, all
> grounded.
>
> `articles/index.html` is included on a second look. The previous pass filed it
> with the article indexes as a blog roll, but its H1 is a real query
> (*&ldquo;Applying for Business Loans&rdquo;*) with a real answer, which the
> other indexes' H1s are not.
>
> Coverage **738 &rarr; 745**, missing **30 &rarr; 23**.


### Where the Quick answer pass ended

| | Start of pass | End |
|---|---|---|
| Pages with a direct answer block | 584 | **745** of 768 |
| `SpeakableSpecification` declared | 538 | **644** |
| Selectors resolving to nothing | 0 | **0** |

The remaining 23 are the ones that should not have one: the two calculators
without prose, the contact, application and partner forms, the homepage,
`faq.html`, the two legal pages, and the article index pages.


### Div markup: 41 pages balanced

Counting `<div` against `</div>` said 41 pages were unbalanced, but that count
cannot tell you what to do &mdash; a browser auto-closes an unclosed div at its
parent's close, so a `</div>` inserted in the wrong place *changes* the
rendering rather than preserving it. Walking the tag stack with a real parser
gave three distinct shapes:


| | Count | Shape | Fix |
|---|---|---|---|
| **A** | 8 on 4 pages | `<div class="wrap sh">` absorbed by `</section>` | close it before `</section>`, as the sibling sections on the same page already do |
| **B** | 31 on 31 pages | `<div class="container">` absorbed by `</body>` | close it before `<footer class="site-footer">`, as ~700 balanced pages do |
| **C** | 6 on 6 pages | stray `</div>`, one close too many | remove it |


Shape B was the only one that could plausibly move something, so it was tested
in the browser against the live site first. Moving the footer and everything
after it out of `.container` gives **byte-identical geometry** &mdash; footer
x/y/w/h, document height, body scroll width &mdash; and identical hit-testing at
the CTA bar's position. `.container` computes to `width:100%; max-width:100%;
margin:0; padding:0`, so it carries no box model at all.


After the fix the 41 pages have body children identical to the pages that were
already balanced: `div.mobile-nav-overlay`, `div.container`,
`footer.site-footer`, `div.mobile-cta-bar`.


### Stray close tags: the count was 1, not 14

The sweep above reported `</meta>` on 12 pages, one `</p>` and one `</br>`.
**Thirteen of those were a bug in the sweep, not defects in the pages.**


Python's `HTMLParser` calls `handle_starttag` then `handle_endtag` from its
default `handle_startendtag`, so every self-closing tag in the source &mdash;
`<meta ... />` on 12 pages, `<br/>` on one &mdash; arrived at `handle_endtag`
and was recorded as a stray close. Both are valid markup. Defining
`handle_startendtag` as a no-op leaves exactly **one** real stray, on
`articles/factor-rate-vs-apr-business-loan-cost/`:


```html
<div class="tldr"><b>The short version:</b> ...in writing.</p></div>
```


There is no `<p>` in that block. Per the HTML parsing spec, an end tag for `p`
with no `p` in button scope is a parse error that **inserts an empty
`<p></p>`** &mdash; which the live page did contain. The site's other two
`.tldr` blocks have no `<p>` and no stray `</p>`, so removing it matches them.


Checked on the live page before the edit: the inserted empty paragraph computed
to `margin: 0` and removing it changed the `.tldr` box height by **0px**.


Stray close tags across the site are now **0**, with no tags left open at EOF.


### Three pages declared `FAQPage` twice &mdash; fixed

`commercial-bridge-loans.html`, `trucking-business-financing.html` and
`equipment/diagnostic-equipment-auto/scan-tool-financing/` each carried two
`FAQPage` blocks against 740 pages with one.


On all three the two `<script>` elements were **byte-identical and adjacent**,
separated by a newline and indent, so the second was removed with its separator.
Had they differed, the fix would have been a merge rather than a delete. Pages
declaring more than one `FAQPage` is now **0**.


### Found on the way out: 153 double-escaped entities on 72 pages

The FAQ parity sweep run after that fix reported 57 answers not supported by
visible text. Sampling three showed two different causes, and the larger one is
a **reader-visible defect**:


| Entity | Count |
|---|---|
| `&amp;amp;mdash;` | 75 |
| `&amp;amp;amp;` | 38 |
| `&amp;amp;ndash;` | 24 |
| `&amp;amp;rsquo;` | 16 |
| **Total** | **153 across 72 pages** |


All 153 sit in body text, none inside an attribute, so a reader sees the literal
string on the page &mdash; for example, in a visible FAQ question on
`business-term-loans.html`:


> Business term loan vs line of credit&amp;mdash;which is right?


The remaining parity misses are answers whose text genuinely is not on the page.
Neither is fixed here; the entity problem is the larger and more visible.
>
> Speakable was extended at the same time. 430 of the 431 pages that already had
> a block point `cssSelector` at `.quick-answer`; the 73 pointed at `h1`,
> `.ef-speakable` or nothing. All 73 now follow the convention, and all 563
> declarations resolve to something on the page.


## Verification

3,233 JSON-LD blocks parse; 0 broken. FAQ parity 756/756. Title/headline
conflicts 0. No file gained mixed line endings &mdash; the 9 files with bare LF
all predate this work. Audit clean at 841 pages.

