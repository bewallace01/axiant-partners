# Blog Article Layout – Notes & Constraints

Avoid repeated layout breakage. Reference this before changing `blog-layout.css` or article structure.

## Current Structure

- **Shell** (`.blog-post-shell`): 3-column flex, `max-width: 1400px`, `margin: 0 auto` for centering
- **Left rail**: Back link + meta, Quick Facts, CTA (separate `blog-rail-card` boxes with `gap: 1rem`)
- **Center**: Main article content in one card
- **Right rail**: TOC in one card

## What Breaks Things

### 1. Form-container flex centering
- **Do not** add `display: flex; align-items: center` to `.form-container.blog-post-content`
- With `align-items: center`, the shell can shrink to content width instead of staying full width
- Centering is handled by `.blog-post-shell` with `margin-left: auto; margin-right: auto`

### 2. Sticky sidebars
- `position: sticky` on rails can cause layout issues:
  - `overflow-y: auto` + `max-height` on rails can make the layout feel cramped
  - Any `overflow: hidden` on an ancestor (e.g. `.container`, `.form-container`) breaks sticky
- Critical.css sets `overflow-x: hidden` on `.container` and `.form-container` at mobile breakpoint
- **Safe approach for sticky**: Test in isolation; if broken, avoid and keep rails scrolling with the page

### 3. Left rail “boxes”
- The left rail is **meant** to have multiple boxes (back link, Quick Facts, CTA) with gaps
- `gap: 1rem` on the rail controls spacing between cards
- Don’t collapse these into one box unless the design explicitly calls for it

## Max-width

- Shell: `max-width: 1400px` – intentional for readability
- On wide screens this creates side margins; that’s expected

## Before Changing Blog Layout

1. Verify no `overflow: hidden` (or `overflow-x: hidden` on a flex/grid parent) that affects the article area
2. Check that `.blog-post-shell` stays full-width via `width: 100%` and `margin: 0 auto`
3. Run a quick check on both light and dark themes
4. Test article pages opened via direct link vs in-site navigation
