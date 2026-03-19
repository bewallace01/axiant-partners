# PageSpeed Insights Audit — Full Walkthrough

**Date:** Mar 19, 2026  
**URL:** https://axiantpartners.com/  
**Report:** Desktop, Lighthouse 13.0.1  

---

## 1. SCORES & METRICS

| Category      | Score | Note                        |
|---------------|-------|-----------------------------|
| Performance   | 74    | Main bottleneck             |
| Accessibility | 98    | Minor issues                |
| Best Practices| 100   |                             |
| SEO           | 100   |                             |

| Metric                 | Value | Target     | Status  |
|------------------------|-------|------------|---------|
| First Contentful Paint | 0.7s  | < 1.8s     | Good    |
| **Largest Contentful Paint** | **6.4s** | **< 2.5s** | **Poor** |
| Total Blocking Time    | 50ms  | < 200ms    | Good    |
| Cumulative Layout Shift| 0.038 | < 0.1      | Good    |
| Speed Index            | 1.5s  | < 3.4s     | Good    |

**Main issue:** LCP at 6.4s — hero image or its discovery is too late.

---

## 2. INSIGHTS (Opportunities)

### Improve image delivery — Est. savings 36,429 KiB

**Current state in codebase:**

| Location | Finding | Status |
|----------|---------|--------|
| `index.html` L40 | `preload` points to `dump-truck-excavator-hero.png` | Should preload `.webp` for WebP-capable browsers |
| `index.html` L1671 | `cre-hero.png` | **Missing** `<picture>` + WebP (still plain img) |
| `index.html` L1779 | `restaurants-hero-bg.png` | **Missing** `<picture>` + WebP (still plain img) |
| `styles.css` L1 | `@import url('https://fonts.googleapis.com/...')` | **Blocking** — fonts load synchronously from styles.css |
| `index.html` L36–39 | Font preload uses `as="style"` + onload swap | Fonts loaded async in HTML, but styles.css also @imports same fonts (duplicate) |
| Nav logos | `logo-horizontal-transparent.png`, `Axiant_light_logo.png` | Not converted to WebP |
| Other pages | 200+ img elements across site | Many without `width`/`height`; most not WebP |

**Action items:**
1. Add picture + WebP for `cre-hero` and `restaurants-hero-bg` on index.html
2. Update hero preload to use WebP (or preload both via `<link rel="preload" as="image" href="...webp" type="image/webp">` + PNG fallback)
3. Remove `@import` from styles.css; fonts already loaded async in index.html
4. Consider WebP for logos (small files, lower priority)

---

### Forced reflow

**Cause:** JS reading layout properties (offsetHeight, getBoundingClientRect, etc.) then writing DOM — triggers sync layout.

**Likely culprits:** `language-switcher.js`, `script.js` (sticky CTA scroll handler, theme toggle). Review layout-triggering reads inside loops or before paint.

---

### LCP request discovery

**Cause:** LCP image discovered late in the load. Hero is in HTML and has `fetchpriority="high"` — good. But:
- Preload points to PNG; browser may fetch PNG first, then picture selects WebP
- `critical.css` and font loading may block/prioritize other resources before hero

**Action:** Ensure hero preload matches what picture serves (WebP). Reduce render-blocking CSS.

---

### Network dependency tree

Audit which resources block the LCP image. Likely: `critical.css` (render-blocking), font CSS.

---

### Use efficient cache lifetimes — Est. savings 2 KiB

**Action:** Add long `Cache-Control` headers for static assets (server/hosting config). Not a code change — configure on server or CDN.

---

### Render blocking requests

| Resource | Location | Blocking? |
|----------|----------|-----------|
| `critical.css` | index.html L43 | Yes — blocks render |
| `styles.css` | L44 — `media="print"` + onload swap | No — loads async |
| Font CSS | index.html L41 — preload as style + onload | Loads async |
| Font CSS | styles.css L1 — `@import` | Yes — blocks styles.css, which loads async, so indirect |

**Action:** Minimize critical.css. Inline above-fold critical CSS if possible. Remove @import from styles.css.

---

### Layout shift culprits

**Diagnostic:** "Image elements do not have explicit width and height"

**Affected (index.html):** Nav logos have width/height. Hero has width/height. Industry tiles have width/height. **All index.html images have dimensions.**

**Affected (rest of site):** ~200+ img elements across 180+ files. Many nav logos and content images lack `width`/`height` — e.g.:
- `business-line-of-credit.html`: bloc-*, agriculture-* images — no dimensions
- Equipment pages, industry pages: many ef-card-img, ef-intro-img without dimensions
- Article pages: nav logos often lack dimensions

**Action:** Add `width` and `height` to all img elements sitewide. Priority: pages with images above the fold.

---

### Optimize DOM size

**Action:** Profile with DevTools. Reduce DOM nodes if very large (e.g. >1500). May require template/component simplification.

---

### LCP breakdown

Review in DevTools: Time to First Byte, resource load order, main-thread work before LCP. LCP at 6.4s suggests either:
1. Hero image loads late (network or prioritization)
2. Main-thread blocked by JS/CSS before image can paint
3. Fonts blocking text, delaying "largest" paint

---

### 3rd parties

- Google Tag Manager (gtag) — deferred to `window.load` ✓
- EmailJS — `defer` ✓
- Fonts (Google Fonts) — loaded async ✓

---

## 3. DIAGNOSTICS

### Image elements do not have explicit width and height

**Scope:** Sitewide. index.html is fine. Other pages: nav logos (`logo-horizontal-transparent.png`, `Axiant_light_logo.png`) and content images in industry/service pages lack dimensions.

**Files with many images:** `business-line-of-credit.html` (16 imgs), `equipment.html` (55), `equipment/*` category pages (~11 each), `landscaping-business-financing.html`, `manufacturing-business-financing.html`, etc.

---

### Minify CSS — Est. savings 12 KiB

**Files:** `critical.css` (~12 KB), `styles.css` (~302 KB). Both have whitespace and could be minified.

**Action:** Add build step (e.g. cssnano, clean-css) or serve minified versions.

---

### Minify JavaScript — Est. savings 6 KiB

**Files:** `language-switcher.js` (~110 KB), `script.js` (~29 KB). Minification would reduce size.

**Action:** Add build step (terser, esbuild) for production.

---

### Reduce unused CSS — Est. savings 35 KiB

**Cause:** `styles.css` is large and shared across all pages. Per-page usage is low.

**Action:** Split CSS by section/page, or use PurgeCSS / UnCSS to remove unused rules. Higher effort.

---

### Reduce unused JavaScript — Est. savings 113 KiB

**Cause:** `language-switcher.js` is ~110 KB and likely includes logic for match flow, translations, visuals — not all used on index.

**Action:** Code-split or lazy-load language-switcher for non-index pages. Defer or load conditionally on index if not needed above the fold.

---

### Avoid enormous network payloads — Total 37,963 KiB (~38 MB)

**Cause:** Sum of all resources. Image optimization (WebP) should reduce this. Also: large CSS, large JS, unoptimized images on other pages.

**Action:** WebP sitewide, minification, code-splitting. Re-run audit after changes.

---

### Avoid long main-thread tasks — 3 long tasks found

**Action:** Profile with DevTools Performance. Break up long tasks (>50ms). Likely in language-switcher.js init or script.js.

---

### User Timing marks and measures — 10 user timings

Informational. Can help debug custom performance marks.

---

### Avoid non-composited animations — 33 animated elements

**Action:** Prefer `transform` and `opacity` for animations. Avoid animating `top`, `left`, `width`, `height`. Check for `box-shadow` or `filter` animations.

---

## 4. ACCESSIBILITY (98)

### Heading elements are not in a sequentially-descending order

**index.html structure:**
- h1 (line 1448) ✓
- h2, h3 under sections ✓
- Possible issue: "Ready to see your options?" (h2) may appear after an h3 in a previous section — verify DOM order.

**Action:** Ensure no h3 without a preceding h2, no h4 without h3, etc. Check sections "Explore Resources" and "Ready to see your options?" for skipped levels.

---

### Identical links have the same purpose

**Finding:** Multiple links to `/match.html` with different text:
- "Find Match", "Check Your Financing Options", "Get matched", "See your options", "Check eligibility", "Talk through a plan", "Find your match", "Start here", "Check your financing options", "Apply now"

**Lighthouse:** Warns when links with same `href` have different visible text and may confuse users.

**Action:** Either:
- Use same link text for same destination (e.g. "Get matched" everywhere), or
- Add `aria-label` to clarify purpose for screen readers, or
- Restructure so links are distinguishable (e.g. different context: "Get matched for equipment" vs "Get matched for SBA").

---

## 5. BEST PRACTICES & SEO

- **Best Practices:** 100 — no issues
- **SEO:** 100 — no issues  
- Trust & Safety (CSP, HSTS, COOP, Trusted Types) — manual checks recommended

---

## 6. SUMMARY — Prioritized Fixes

### High impact (LCP / Performance)

1. **Hero preload** — Preload WebP instead of (or in addition to) PNG for LCP image.
2. **cre-hero & restaurants-hero-bg** — Add `<picture>` + WebP on index.html.
3. **Remove @import from styles.css** — Fonts already loaded async in HTML; @import blocks styles.css parse.
4. **Reduce render-blocking CSS** — Minimize critical.css; consider inlining critical above-fold CSS.

### Medium impact

5. **Add width/height** to all images sitewide (prioritize index + high-traffic pages).
6. **Minify CSS and JS** — Build step for production.
7. **Break up long main-thread tasks** — Profile and optimize language-switcher.js, script.js.

### Lower impact

8. **Unused CSS/JS** — Code-split, lazy-load, or purge.
9. **Accessibility** — Fix heading order; unify or clarify identical match.html links.
10. **Cache headers** — Configure on server/CDN.
