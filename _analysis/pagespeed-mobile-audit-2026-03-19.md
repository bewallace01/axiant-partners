# PageSpeed Insights — Mobile Audit

**Date:** Mar 19, 2026  
**URL:** https://axiantpartners.com/  
**Focus:** Mobile (form_factor=mobile)  
**Note:** phone.pdf was not available; this audit is based on mobile testing conditions, standard Lighthouse mobile checks, and codebase analysis.

---

## 1. MOBILE vs DESKTOP TESTING ENVIRONMENT

| Aspect | Mobile | Desktop |
|--------|--------|---------|
| **Network** | Simulated 4G (1.6 Mbps down / 750 Kbps up, 150ms RTT) | Fast broadband |
| **CPU** | 4× slowdown | No throttle |
| **Viewport** | 412 × 732 px | 1920 × 1080 px |
| **Typical result** | Lower scores (50–70 common) | Higher scores (70–90) |

**Implication:** Every desktop issue is amplified on mobile. Image weight, render blocking, main-thread work, and layout shifts hurt more under throttled CPU and network.

---

## 2. MOBILE-SPECIFIC SCORE EXPECTATIONS

Desktop Performance was **74**; mobile is typically **15–25 points lower** under throttling. Expect mobile Performance in the **45–60** range before optimizations.

---

## 3. SAME INSIGHTS AS DESKTOP (Higher Impact on Mobile)

### Improve image delivery — Est. savings 36,429 KiB

**Mobile impact:** On 4G, 36 MB of images = several seconds of loading. WebP and proper sizing are more important on mobile.

**Status (post prior fixes):**
- Hero: WebP preload + picture ✓
- cre-hero, restaurants-hero-bg: picture + WebP ✓
- Industry tiles: picture + WebP ✓
- Nav logos: still PNG (small, lower priority)
- **Mobile-specific:** Consider `srcset` with smaller image variants for mobile viewport (e.g. 600w, 400w) instead of serving 1200px hero to 412px screen.

---

### Render blocking requests

**Mobile impact:** Critical.css blocks first paint. With 4× CPU slowdown, parsing/execution is slower. Every KB of blocking CSS delays LCP.

**Current:**
- `critical.css` — render-blocking
- Fonts — async ✓
- `styles.css` — loads async ✓

**Action:** Further reduce critical.css; consider inlining only above-fold rules for mobile.

---

### LCP (Largest Contentful Paint)

**Desktop LCP:** 6.4s (poor).  
**Mobile:** Usually 2–3× worse under throttling → ~12–18s possible.

**LCP element:** Hero image (`dump-truck-excavator-hero`). On mobile (412px wide), serving 1200×630 is overkill.

**Actions:**
1. Add responsive `srcset` for hero: e.g. `srcset="hero-600.webp 600w, hero-900.webp 900w, hero-1200.webp 1200w"` so mobile gets ~600w.
2. Ensure hero preload uses appropriate size for viewport (or let browser pick from srcset).
3. Prioritize hero fetch; reduce main-thread work before LCP.

---

### Total Blocking Time (TBT)

**Desktop:** 50 ms (good).  
**Mobile:** With 4× CPU slowdown, TBT can reach 200–400 ms from the same JS.

**Likely sources:** `language-switcher.js`, `script.js`, font loading. Consider:
- Deferring or lazy-loading language-switcher on mobile
- Breaking up long tasks (requestIdleCallback, code-splitting)

---

### Cumulative Layout Shift (CLS)

**Desktop:** 0.038 (good).  
**Mobile:** Same if images have dimensions. Nav logos now have width/height ✓. Content images on other pages may still shift.

---

### Avoid enormous network payloads — 37,963 KiB

**Mobile impact:** 38 MB on 4G is a serious delay. WebP and minification help; mobile should ideally receive smaller assets where possible.

---

### Long main-thread tasks — 3 found

**Mobile impact:** With 4× CPU slowdown, each 200 ms task becomes ~800 ms. Users perceive the app as frozen.

---

## 4. MOBILE-SPECIFIC LIGHTHOUSE AUDITS

### Viewport meta tag

**Status:** ✓ Present  
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

### Tap targets (interactive elements)

**Lighthouse rule:** Tap targets should be at least **48×48 px** to avoid mis-taps.

**Checked in codebase:**
- `.nav-links a` — padding: 10px 14px → ~38×34 px (can be < 48)
- `.btn-primary`, `.hero-btn` — typically larger ✓
- `.mobile-menu-toggle` — hamburger button; confirm ≥ 48×48
- `.theme-toggle` — 52×28 px (height < 48; width OK)
- Card links, trust-line links — may be small on mobile

**Action:** Ensure all tappable elements have min 48×48 px. Add `min-height: 48px; min-width: 48px` or `padding` to meet that for nav links and theme toggle on mobile.

---

### Font sizes

**Lighthouse rule:** Body text should be at least **16 px** to avoid zoom on iOS.

**Status:** `body { font-size: 16px }` in critical.css ✓  
Media queries use `font-size: 14px` or `13px` at some breakpoints; verify these are for non-body elements or that zoom is acceptable.

---

### Content sized correctly for viewport

**Lighthouse rule:** Content should not overflow horizontally (no horizontal scroll).

**Status:** `overflow-x: clip` on html/body; `overflow-x: hidden` in mobile media queries ✓  
Grids use `minmax(0, 1fr)` to avoid overflow ✓

---

### Document has a valid `h1`

**Status:** ✓ `h1` present on index and other pages.

---

### Links are crawlable

**Status:** ✓ No `javascript:` or `#`-only links for main navigation.

---

### Image elements have `[alt]` attributes

**Status:** ✓ Images have alt text (including empty alt for decorative).

---

### Avoid non-composited animations

**Finding:** 33 animated elements. On mobile, animations that trigger layout (e.g. `width`, `height`, `top`, `left`) can cause jank.

**Action:** Prefer `transform` and `opacity`; audit any `box-shadow` or `filter` animations.

---

## 5. MOBILE LAYOUT & RESPONSIVE DESIGN

**Breakpoints in index.html:**
- `980px` — tablet: single-column hero, 2-col metric grid
- `768px` — mobile: single column, adjusted padding, typography
- Additional breakpoints in styles.css

**Hero layout:** `grid-template-columns: 1fr` at ≤980px ✓  
**Industry grid:** `repeat(auto-fit, minmax(210px, 1fr))` — adapts ✓

---

## 6. MOBILE-SPECIFIC RECOMMENDATIONS

### High impact

1. **Responsive hero image** — Add `srcset` with 600w / 900w / 1200w variants so mobile receives ~600px-wide image.
2. **Tap target size** — Ensure nav links, theme toggle, and mobile menu button are ≥ 48×48 px.
3. **Reduce critical CSS** — Inline only above-fold CSS for mobile to speed first paint.
4. **Defer heavy JS** — Lazy-load `language-switcher.js` on mobile for non-match pages.

### Medium impact

5. **Break up long tasks** — Use `requestIdleCallback` or split work to keep main thread responsive.
6. **Font display** — Ensure `font-display: swap` (or similar) for web fonts to avoid FOIT on slow connections.
7. **Third-party scripts** — Keep gtag deferred; avoid adding more sync scripts.

### Lower impact

8. **Service worker** — Consider caching static assets for repeat visits.
9. **Preconnect** — Already present for Google Fonts and origin ✓

---

## 7. MOBILE CHECKLIST (Run After Changes)

- [ ] Run PageSpeed Insights with Mobile selected
- [ ] Check tap target sizes in DevTools (414×896 or 412×732)
- [ ] Test on real device (iPhone/Android) on 4G
- [ ] Verify no horizontal scroll at 320px, 375px, 412px widths
- [ ] Confirm LCP element and LCP time in Lighthouse mobile report
- [ ] Test with Chrome DevTools CPU throttling (4× slowdown) and Fast 4G network

---

## 8. SUMMARY

| Category | Desktop | Mobile (expected) | Priority fixes |
|----------|---------|-------------------|----------------|
| Performance | 74 | ~45–55 | LCP, images, TBT |
| Accessibility | 98 | ~95–98 | Tap targets |
| Best Practices | 100 | 100 | — |
| SEO | 100 | 100 | — |

**Main mobile gaps vs desktop:**
- Slower LCP due to network + CPU throttling
- Tap targets may be under 48×48 px
- Hero image size not optimized for 412px viewport
- Same blocking resources, magnified impact

Implementing responsive hero `srcset`, tap target sizing, and further critical-CSS reduction will have the largest effect on mobile scores and real-user experience.

---

## 9. MOBILE OPTIMIZATIONS APPLIED (Mar 19, 2026)

| Fix | Status | Impact |
|-----|--------|--------|
| Hero preload: media query for mobile (600w) vs desktop (full) | Done | Mobile fetches ~60KB vs 204KB for LCP |
| Axel avatar: WebP + 96px variant (170KB → 2KB) | Done | Chat loads faster when opened |
| Hero grid: min-height 280px on mobile | Done | Reduces CLS from layout collapse |
| ai-howitworks / ai-growth: 450w variants created | Done | Available for match flow (script update needed to use) |
| Tap targets 48×48 px | Already in place | critical.css @media (max-width: 768px) |
