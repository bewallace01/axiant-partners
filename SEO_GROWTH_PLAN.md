# Axiant Partners — SEO / AEO / GEO Growth Plan

The living roadmap for growing organic traffic + leads on **axiantpartners.com**.
The site audit tells you *what's wrong right now*; this doc is the *engine* that
turns that into constant, compounding growth. Work it on a cadence.

> This is the master roadmap. The other SEO docs at root are inputs to it:
> `SEO_GUIDE.md` (how to write a page), `SEO_PUBLISH_CHECKLIST.md` (pre-publish gate),
> `LONG_TAIL_PLANNING_BREAKDOWN.md` + `COMPETITOR_KEYWORD_GAP_ANALYSIS.md` (what to add).

---

## 1. North star (the strategy)

- **A programmatic financing/broker SEO factory** (~846 pages). The job of every page
  is to rank for a financing search and route the visitor to **`/match.html`** (the lead form).
- **Audience:** business owners seeking financing + the brokers who serve them.
- **The trusted pages are the authority base** — AR financing, security-services, SBA,
  roofing, etc. already earn impressions. Deepen and cross-link these; don't dilute them.
- **One canonical page per intent.** Noun-swapped clones get canonicaled to the winner
  and dropped from the sitemap (e.g. `contractor-financing` → `construction-business-financing`).

---

## 2. The engine — run this on a cadence

**Every commit (automatic):** `npm run audit` runs via the post-commit hook →
`_analysis/site-audit.html` (gitignored, dev-only) + a copy in `~/Downloads/`.
Open it; work 🔧 **Fix** → 📈 **Improve** → 🚀 **Grow**.

**Before acting on any flag, confirm it's a real defect.** The audit over-flags
intentional decisions — e.g. "missing from sitemap" pages that correctly canonical
elsewhere, or "no freshness date" on noindex pages. The detector was taught to ignore
those; keep that discipline (verify, then fix the detector if it's a false positive).

**Monthly — refresh GSC and target winners:**
1. Drop the GSC export into `_analysis/gsc-YYYY-MM-DD/`, write a dated `_analysis/GSC_ANALYSIS_YYYY-MM-DD.md`.
2. Update the hand-maintained `gscPane` figures in `scripts/site-audit.js`, re-run the audit.
3. Deepen "striking-distance" pages (position ~3–40) — the cheapest wins.

**Before a release that should show in the JYNI Backend dashboard:** the dashboard
serves a *committed snapshot* in the CRM repo, and this generator lives in a *separate*
repo — so regenerate, then copy `_analysis/site-audit.html` →
`<CRM>/src/content/audits/axiant-site.html` and `<CRM>/audits/axiant-site-audit.html`,
commit in the CRM, and ship via the CRM's staging→main release. (Easy to forget.)

---

## 3. ADD — new pages (backlog + rules)

**Templates to follow:** `INDUSTRY-PAGE-TEMPLATE.md`, `BLOG_POST_TEMPLATE.md`,
`SEO_GUIDE.md` (title/meta standards), `SEO_PUBLISH_CHECKLIST.md` (pre-publish gate).

**Backlog (from the planning docs + keyword gaps):**
1. New **industry financing** pages (`<industry>-business-financing.html` + article clusters).
2. New **equipment categories** under `/equipment/<type>/` (each linked from the equipment hub + the relevant financing hub — never ship an orphan).
3. **Loan-amount** and **state/geo** programmatic pages following the templates.
4. New **article clusters** under each product hub (`/sba-loans/articles/…`, `/equipment-financing/articles/…`, etc.) targeting long-tail questions.

**Rules for every new page (non-negotiable):**
- [ ] **Genuinely unique body** — never a noun-swapped clone of a sibling. Read the template; trace every variable. Thin/duplicate pages get de-ranked.
- [ ] **Self-canonical**, and **add it to `sitemap.xml`** (only self-canonical URLs go in the sitemap — canonical-elsewhere dupes stay out).
- [ ] **At least one inbound contextual link** from a relevant hub/sibling, so it's never an orphan.
- [ ] **Emit `dateModified`** in the page JSON-LD (freshness = the strongest GEO signal).
- [ ] **1,000w+** for genuine articles; FAQ + a table/worked example for AEO/GEO.
- [ ] Run the `SEO_PUBLISH_CHECKLIST.md` before publishing.

---

## 4. FIX / IMPROVE — existing pages (current backlog)

From the latest audit (very-thin, orphans, and sitemap drift are **cleared**):

1. **Deepen the ~130 lean (500–800w) articles toward the 1,000w house standard**, cluster by cluster. **SBA cluster: done (20/20).** Next largest: `equipment-financing` (~50), `equipment` (~24), `commercial-real-estate-loans` (~10), `fix-and-flip` (~10). Add a worked example + a deeper section per article — unique, accurate, hedged (no fabricated rates).
2. **Strengthen the ~230 weak-link pages (1–2 inbound)** — add 1–2 contextual links each from stronger cluster pages. Do not over-optimize past ~3 inbound.
3. **Refresh stale articles** — update figures, bump `dateModified`, add a tool/FAQ where it fits.

---

## 5. GROW — off-page authority

The pages are fine; the ceiling is **domain authority**. Content alone won't break it.

1. **Earn links + mentions** — directories, partnerships, guest posts, digital PR.
2. **GSC-driven prioritization** — pour link-building and depth into the pages already
   earning impressions (the trusted cluster), not cold pages.

---

## 6. Guardrails (hard-won — read before any SEO change)

- **Uniqueness:** never claim a programmatic page is "unique" without reading the template and tracing variables. The de-rank rule applies here too.
- **Canonical/noindex discipline:** sitemap = self-canonical URLs only; noindex pages opt out of indexing *and* the GEO freshness count.
- **The audit over-flags** intentional decisions — verify before "fixing"; fix the detector if it's a false positive (and make sure a genuinely-new bad case still flags).
- **Honest freshness only** — `dateModified` reflects the real last content change, never a faked recent date.
- **Never touch the owner's in-progress files** — e.g. `employee-onboarding-handbook.html`, the `caller-*` and onboarding pages, `_analysis/` tooling. These are internal/noindex; stage only your own files explicitly.

---

## 7. Workflow (so growth ships safely)

- Work on a `feat/...` branch. Push it. **Merge to `main` only on the owner's go-ahead**
  — pushing `main` = a Netlify production deploy.
- After deploy, spot-check the live page renders (it's production).

---

*Companion: the JYNI.io product site has its own `docs/seo-growth-plan.md` in the CRM repo.*
