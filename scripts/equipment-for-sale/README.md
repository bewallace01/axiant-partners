# Equipment-for-Sale category template

One template renders every `/equipment-for-sale/<slug>/` page from a JSON data file.

```bash
python3 scripts/equipment-for-sale/build.py               # all categories
python3 scripts/equipment-for-sale/build.py vacuum-trucks # one
```

Stdlib only — no new dependencies, matching the rest of `scripts/`.

## Layout

1. **Dealer strip** — logo, name, blurb, phone, website.
2. **Hero** — eyebrow, serif H1, intro, "How financing works →", then a balanced
   two-column row: photo (1.5fr) + **equal-height** "Finance with Axiant" card (1fr).
   The trust checklist uses `margin-top:auto` so it sinks to the card floor and the
   card always matches the photo — that's the fix for the old empty wedge.
3. **Model cards** — photo, capacity badge, spec chips, and **two CTAs per model**:
   *View inventory ↗* (out to the dealer) and *Estimate financing* (into Axiant's funnel).
4. **Finance band** — navy, core pitch + proof points + pre-approval CTA.
5. **Preserved SEO prose** — verbatim, never rewritten.

## Files

| File | What it is |
|---|---|
| `build.py` | Generator + the `.efs` component CSS |
| `_chrome.html` | Head/nav/footer shell with `{{META}} {{SCHEMA}} {{BREADCRUMB}} {{BODY}}` slots |
| `data/<slug>.json` | Everything category-specific: dealer, hero, models, band |
| `data/_<slug>.meta.html` | **SEO — verbatim.** title, meta description, canonical, og:* |
| `data/_<slug>.schema.html` | **SEO — verbatim.** JSON-LD (BreadcrumbList + ItemList + FAQPage) |
| `data/_<slug>.seo.html` | **SEO — verbatim.** The prose sections (what-is-a-X, how-to-choose, FAQs…) |

## SEO guardrails — read before touching

The `_*.meta.html`, `_*.schema.html` and `_*.seo.html` sidecars are copied through
**byte-for-byte**. This template is a **re-layout, not a content change**. Do not
author or rewrite that content here. After any change, diff against the previous
page and confirm title / description / canonical / og / JSON-LD / H1 are identical.

## Adding a category

1. Create `data/<slug>.json` (copy `vacuum-trucks.json`).
2. Create the three `_<slug>.*.html` sidecars by lifting the existing page's meta,
   JSON-LD and prose **verbatim**.
3. `python3 scripts/equipment-for-sale/build.py <slug>`

## Two things to know

**Deep lineups.** Categories with more than 6 models (material-handlers has 15,
dry-batch-plants 9, workover-rigs 8) also render a collapsed **"Full lineup & specs"**
table under the cards, so a long lineup stays comparable at a glance instead of
becoming 15 cards. Controlled by `TABLE_THRESHOLD` in `build.py`.

**Missing model photos.** Most categories have no per-model photo yet. A model with
`"image": null` falls back to the category hero image, and `build.py` prints a
`TODO images:` line naming them. Drop the real photo into the data file when the
dealer supplies one and it appears automatically. Vacuum-trucks is fully photographed.

## Theme

The CSS is built on the site's existing tokens (`--accent-color`, `--bg-card`,
`--text-primary`…), **not hardcoded hex**. The site ships a working dark-mode toggle;
hardcoding the light palette would break every category page in dark mode. It renders
the light catalog look by default and stays correct in dark. Fonts are the site's real
ones — Playfair Display (display) + Inter (body).

One deliberate `!important`: `header.efs-crumbhead` must override the global bare-`header`
rule, which styles it as the full-bleed hero (60px padding, centred white text on the
overlay background). Without it the breadcrumb renders as a giant empty blue band.
