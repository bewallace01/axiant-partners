# Performance Optimization Summary

## Completed Optimizations

### 1. **Critical CSS**
- **critical.css** – Above-fold CSS (variables, reset, nav, header) extracted and loaded first
- **styles.css** – Loaded asynchronously (`media="print"` + `onload="this.media='all'"`) with noscript fallback
- **Impact:** Faster first contentful paint; full styles load without blocking render

### 2. **translations.js removed**
- Removed `translations.js` (~122KB) from all HTML pages; language switching was disabled
- **Impact:** ~122KB saved per page

### 3. **Server compression** (.htaccess)
- Gzip enabled for `text/html`, `text/plain`, `text/xml`, `text/css`, `application/javascript`, `application/json`
- **Impact:** Smaller transfer sizes for all text assets

### 4. **PurgeCSS** (optional build step)
- Run `npm install && npm run purgecss` to trim unused styles from styles.css
- Config: `purgecss.config.js` with safelist for dynamic classes (nav-, ef-, bloc-, etc.)
- **Impact:** Est. 30–50% reduction in styles.css size

### 5. **WebP conversion** (optional build step)
- Run `npm run webp` to convert PNGs in `assets/` to WebP
- **Impact:** ~25–35% smaller image files (HTML still uses PNG; add `<picture>` for WebP if desired)

### 6. **Font Loading** (styles.css)
- **Reduced font weights** from 7 variants (Playfair 400,500,600,700 + Inter 300,400,500,600,700) to 4 variants (Playfair 400,600 + Inter 400,600)
- **Impact:** ~50% reduction in font file downloads
- **Note:** Pages using 500 or 700 weight will fall back to 600; 300 falls back to 400. Visual difference is minimal.

### 7. **Image Optimization – Unsplash** (styles.css)
- **Header, calculator, CTA, nav mobile:** Reduced from `w=2069–2070, q=80` to `w=1200, q=75`
- **Global bottom CTA:** Reduced from `w=1400, q=70` to `w=1000, q=70`
- **Impact:** ~60–70% smaller image downloads from Unsplash
- **Files affected:** Header background, calculator header, CTA section, mobile nav overlay

### 8. **Resource Hints** (index.html)
- **dns-prefetch** for `images.unsplash.com` – DNS resolved early for faster image requests

### 4. **Script Loading**
- Scripts already use `defer` – non-blocking

### 10. **Image Best Practices**
- `loading="lazy"` on below-the-fold images
- `decoding="async"` on many images
- Hero images use `rel="preload"` for LCP

---

## Further Recommendations

### High Impact (mostly done)
1. ~~**Critical CSS**~~ – Done. See critical.css + async styles.css.
2. ~~**styles.css size**~~ – PurgeCSS configured. Run `npm run purgecss`.
3. ~~**translations.js**~~ – Removed from all pages.
4. **Convert PNGs to WebP** – Script ready: `npm run webp`. Update HTML to use `<picture>` for WebP+fallback if desired.

### Medium Impact
5. **Image dimensions:** Add `width` and `height` to all `<img>` tags to avoid layout shift (CLS).
6. **Self-host Unsplash images:** Download and host on your domain to avoid extra origin and reduce external dependencies.
7. **Preload key fonts:** Add `<link rel="preload">` for font files on critical pages.

### Lower Impact
8. **Consolidate JSON-LD:** Merge multiple `<script type="application/ld+json">` blocks per page.
9. ~~**Compress assets**~~ – Gzip enabled in .htaccess.
10. **CDN:** Serve static assets from a CDN for faster delivery.

---

## Estimated Impact

| Optimization            | Est. improvement                     |
|-------------------------|--------------------------------------|
| Font weight reduction   | ~50KB saved, faster font loading     |
| Unsplash image resize   | ~200–400KB saved per page (variable) |
| dns-prefetch            | ~50–100ms faster first Unsplash load |

Overall, these changes should improve LCP and TTI, especially on slower connections and mobile.
