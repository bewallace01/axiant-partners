# Deploy brief #2 — contrast fix, section tones, 113 photos

Repo: `axiant-partners` (origin `bewallace01/axiant-partners`, branch `main`).
The previous push (`1ca5fcdf3`, the v2 conversion + responsive images) is already
live. This is the next batch, sitting uncommitted in the working tree.

**741 files changed, plus 4 untracked paths.**

---

## The one thing that will break the site if you get it wrong

`assets/aside/` is **untracked, and git reports it as a single line** —
`?? assets/aside/` — not as 113 separate files. It holds all 113 photos, and
**113 `<img>` tags across 69 pages point at them.**

`git add -A` picks it up. **`git add -u` does not**, and would ship 113 broken
images. Use `-A`.

The same applies to `_photo-manifest/` (64 KB of manifest/prompt files, worth
keeping) and the two new scripts.

---

## What is in this push

**1. Quick-answer contrast fix — this one is urgent.**
Right now, live, **705 article pages render their "Quick answer" box as white
text on pale blue**, which is unreadable. That was a regression introduced by the
previous push: the legacy-markup port gave `.quick-answer` a pale background
without realising `.callout` already supplies a navy gradient with light text.

It could not just be reverted — **558 other pages use bare
`class="quick-answer"`** and genuinely needed that rule. The fix scopes it to
`.quick-answer:not(.callout)`. Measured after the change: dark boxes **7.5:1**,
light boxes **17.4:1**. Both pass WCAG AA.

**2. One tone per section.**
Cards each carried their own `data-tone`, so a single grid cycled
blue → teal → indigo → bronze → rust and read as a rainbow. Two changes:

- a CSS block (`ONE TONE PER SECTION`) makes cards inherit their section's tone
  by specificity — `.group[data-tone="x"] .card` (0,2,0) beats the card's own
  `[data-tone="y"]` (0,1,0). No markup touched; delete the block to revert.
- `.group` sections now rotate through the five tones down each page
  (739 pages, 4,432 sections), because 789 pages previously had *every* section
  set to blue and the card cycling was the only source of colour.

**3. 113 aside photos.**
The decorative hatched `.aside-mark` panels are replaced with real photography on
69 pages. `assets/aside/` is 113 WebP files, 5.0 MB, every one 1064×480 (2× the
532×240 slot). Pages without a photo would keep the hatched fallback — there are
none left.

Also new: `scripts/slice-grids.py` and `scripts/apply-aside-photos.py`, plus
`_photo-manifest/` (the CSV, prompts and batch plan that drive them).

---

## Verify before you commit

All four already pass locally. Re-run them after staging.

```bash
# 1. design system         -> expect "877/877 pages conformant"
python3 scripts/check-page.py

# 2. photos are staged     -> expect 113
git diff --cached --name-only | grep -c 'assets/aside/.*\.webp$'

# 3. no backups crept in   -> expect no output
git diff --cached --name-only | grep -E '^_backup|^_to_delete'

# 4. every image ref resolves -> expect "0 broken"
python3 - <<'PY'
import re, glob, os
miss = chk = 0
for p in glob.glob('**/*.html', recursive=True):
    if any(x in p for x in ('node_modules','_backup','_to_delete','_preview')): continue
    s = open(p, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'(?:src|srcset)="([^"]+)"', s):
        for part in m.group(1).split(','):
            u = part.strip().split()[0].split('?')[0].lstrip('/')
            if not u or u.startswith(('http','data:')): continue
            if not u.lower().endswith(('.webp','.png','.jpg','.jpeg','.svg')): continue
            chk += 1
            if not os.path.exists(u): miss += 1
print(f'{chk} image refs checked, {miss} broken')
PY
```

Current local state: **877/877 conformant, 8,275 image refs, 0 broken,
113/113 photo slots filled, 0 hatched.**

---

## Commit and push

```bash
git add -A
git status --short | head -20

git commit -m "$(cat <<'EOF'
Fix the quick-answer contrast regression, one tone per section, 113 aside photos

The legacy-markup port in 1ca5fcdf3 gave .quick-answer a pale accent-100
background without accounting for .callout, which already supplies a navy
gradient with light text. The result was white text on pale blue on the 705
pages using `class="callout quick-answer"`. Deleting the rule was not an option
because 558 pages use bare `class="quick-answer"` and rely on it, so it is now
scoped .quick-answer:not(.callout). Measured: 7.5:1 dark, 17.4:1 light.

Cards and tiles each carried their own data-tone, so one grid cycled through
five colours and read as a rainbow. Cards now inherit their section's tone by
specificity, and because 789 pages had every section set to blue, the sections
themselves now rotate through the five tones down the page. 532 pages show
three tones and 153 show five, against 789 single-tone before.

The decorative hatched .aside-mark panels read as unfinished placeholders, so
all 113 slots across 69 pages now carry real photography: 1064x480 WebP at 2x
the rendered 532x240 box, 5.0MB total, object-fit cover so nothing reflows.
scripts/slice-grids.py cuts 4K grid renders into the individual files and
scripts/apply-aside-photos.py swaps them in; both are idempotent and skip slots
whose file is absent.

877/877 pages conformant. 8,275 image references, none broken.
EOF
)"

git push origin main
```

---

## Verify live

Deployment is push-to-`main` (the only workflow is `indexnow.yml`, which pings
IndexNow — it does not build the site).

- **https://axiantpartners.com/dscr-loans/articles/dscr-loans-no-seasoning/** —
  the "Quick answer" box at the top should be a **navy panel with light text**,
  clearly readable. This is the fix that matters most.
- **https://axiantpartners.com/equipment/excavators/** — beside the body copy
  there should be a **photograph of an excavator**, not a hatched grey box.
- **https://axiantpartners.com/dscr-loans/articles/** — the card grid should be
  one colour per section, not five colours in one grid.
- Any article page — confirm images load (DevTools ▸ Network ▸ Img, no 404s
  under `/assets/aside/`).

---

## Do NOT do these

- **Do not `git add -u`.** It misses `assets/aside/` and ships 113 broken images.
- **Do not delete the `.quick-answer:not(.callout)` scoping** and "simplify" it
  back to `.quick-answer`. That is the exact bug being fixed here.
- **Do not run `scripts/convert-program-page.py`** on the tool or article pages.
  It rebuilds a body out of content "bands" and a form is not a band — measured,
  it takes match.html from 2 forms to 0 and 25 fields to 0.
- **Do not set `.form-step{display:none}`** on match.html. `script.js` only shows
  the Continue button on mobile, so hiding the steps makes the desktop form
  unsubmittable. All four steps are meant to show at once on desktop.
- **Do not change the `$300M+ funded` / `Since 2020` copy** on match.html. Alex
  has been told twice it conflicts with the company's age and has chosen to keep
  it.

## Optional, only if Alex asks

- `styles.css` (239 KB), `axiant-v2-chrome.css` and `axiant-v2-legacy-body.css`
  are referenced by zero real pages and can be deleted — but as a **separate
  commit**, so rollback stays easy.
- `assets/` holds ~1.1 GB of PNG `<picture>` fallbacks. No modern browser
  downloads them; they cost deploy size, not page speed.
