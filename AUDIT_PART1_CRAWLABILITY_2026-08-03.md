# Site audit part 1 — crawlability and indexability

Part 1 of 5. Scope: can Google reach, read and keep every page that should be
kept. 820 HTML files, 768 indexable, 52 `noindex`.


## Clean — verified, not assumed

| Check | Result |
|---|---|
| `robots.txt` | Sitemap + LLM directives present; 16 AI crawlers explicitly allowed |
| Missing `<title>` / viewport / `html lang` | **0 / 0 / 0** |
| Missing canonical | **0** |
| Self-referencing canonicals | 764 of 768 |
| Sitemap URLs | 764 — 0 `noindex`, 0 redirecting, 0 non-indexable |
| Live status, 100 pages across 63 families | **100× 200** |
| `www` &rarr; apex, `http` &rarr; `https` | 301, correct |
| Redirect chains among 431 rules | **0** |

The four indexable pages without a self-canonical point at consolidation
targets and are correctly excluded from the sitemap. That is deliberate and
right.


## Fixed


### 88 root pages answered 200 at two URLs

Netlify serves `/foo` as well as `/foo.html`. Both returned 200:


```
200  https://axiantpartners.com/1-million-business-loan
200  https://axiantpartners.com/1-million-business-loan.html
```

Canonicals already pointed at `.html`, so there was no ranking risk &mdash; but
it is **~10% more crawlable URLs** on a site where one page went **51 days**
between crawls, and Google demonstrably crawls them: four of these bare forms
turned up in the *crawled &mdash; currently not indexed* report.


**Zero internal links** used the bare form, so 87 explicit 301s are free.
(88 twins, one already had a rule.)


### Two stale rules pointed a live hub at a product page

```
/startup-financing/articles/  /startup-financing.html  301
/startup-financing/articles   /startup-financing.html  301
```
`startup-financing/articles/index.html` exists &mdash; it is the hub built
earlier this session, and **24 pages link to it**. The rules were inert only
because Netlify lets an existing file beat a *non-forced* rule. The same file
has forced rules elsewhere in this repo: 56 of 431 use `301!`, which overrides
files. One `!` added to either line and the hub disappears silently. Removed.


### Two smaller items

- One **relative canonical** (`/equipment-financing.html`) made absolute; every
  other canonical on the site is absolute.
- **Three internal links** pointed at forced redirects and now point at the
  destination, removing a needless 301 hop.


## Left alone, deliberately

`business-term-loans/articles/business-term-loan-vs-line-of-credit/index.html`
exists on disk, is force-redirected to `/business-line-of-credit.html`, and is
excluded from the sitemap by name in `generate_sitemap.py`. It is unreachable
dead weight, but deleting content is the owner's call, not an audit's.


## Method note

Four checks in this pass produced false results before they produced true ones,
all from comparing a derived string rather than the thing itself:


- A `\s` escaped twice inside an f-string reported `robots.txt` as having no
  Sitemap directive. It has one.
- `Path.exists()` counted directories as pages, inflating "shadowed redirect
  rules".
- A substring test said `/sba-loans/` was in the sitemap; it was matching
  `/sba-loans/articles/`.
- Stripping trailing slashes on both sides of a comparison turned 3 links
  costing a redirect hop into 27.


Each was caught by checking the source. The numbers above are the corrected ones.


## Next

Part 2: hub architecture and internal linking &mdash; reachability, click depth,
orphans, whether every hub links its children and every child links back.

