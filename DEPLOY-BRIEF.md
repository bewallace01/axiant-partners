# Deploy brief — take the v2 conversion live

Repo: `axiant-partners` (origin `bewallace01/axiant-partners`, branch `main`).
`HEAD == origin/main` — **none of this work is committed yet.** It is all sitting
in the working tree, reviewed and verified. Your job is to get it live without
losing anything and without shipping 44 MB of backups.

---

## The one thing that will break the site if you get it wrong

There are **184 untracked new image files** in `assets/`. They are the responsive
variants (`-560w.webp`, `-800w.webp`, `-1200w.webp`, `-1600w.webp`) plus 41
JPG/PNG→WebP conversions.

**3,829 `srcset` URLs across the HTML now point at those files.** If you commit
only the modified tracked files, every one of those becomes a 404 and images
vanish sitewide. `git add -A` (after the ignore step below) is required — do not
use `git add -u`.

---

## Step 1 — keep the backups out of the commit

Five untracked folders totalling ~44 MB are local safety copies. They must not
ship. Append to `.gitignore`:

```
# Local safety copies from the v2 conversion — do not commit
_backup-fullv2/
_backup-images/
_backup-v2body/
_backup-pre-v2-swap/
_to_delete/
```

(`_analysis/` is already tracked in the repo — leave it alone.)

## Step 2 — stage everything else

```bash
git add -A
git status --short | head -40
```

## Step 3 — verify BEFORE you commit

Run all four. Do not commit if any fails.

```bash
# 1. every page conforms to the design system  -> expect "877/877 pages conformant"
python3 scripts/check-page.py

# 2. no backup folder crept in  -> expect no output
git diff --cached --name-only | grep -E '^_backup|^_to_delete'

# 3. the new image files are staged  -> expect ~184
git diff --cached --name-only | grep -cE 'assets/.*\.webp$'

# 4. every srcset target is actually staged or already tracked -> expect 0 broken
python3 - <<'PY'
import re, glob, os, subprocess
staged = set(subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split('\n'))
staged |= set(subprocess.run(['git','diff','--cached','--name-only'],capture_output=True,text=True).stdout.split('\n'))
bad = 0
for p in glob.glob('**/*.html', recursive=True):
    if any(x in p for x in ('node_modules','_backup','_to_delete','_analysis')): continue
    s = open(p, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'srcset="([^"]+)"', s):
        for part in m.group(1).split(','):
            u = part.strip().split()[0].split('?')[0].lstrip('/')
            if u and not u.startswith('http') and u not in staged and not os.path.exists(u):
                bad += 1; print('MISSING', u)
print(f'{bad} broken srcset targets')
PY
```

## Step 4 — commit and push

```bash
git commit -m "$(cat <<'EOF'
Convert the tool and article pages to the v2 design system

Twenty-three pages (match, the five calculators, referral, get-matched/*,
*/articles/*, small-business-financing-report, rightmfgsystems, consolidate)
were running v2 chrome over a legacy body via .v2-body-scoped rules, so their
bodies still rendered from the 239KB styles.css and looked like the old site
next to the converted pages.

Swapping the stylesheet with the markup untouched was measured in a headless
browser and preserves the forms the band-based converter would have destroyed:
match.html holds at 2 forms / 38 fields / 28 ids. Container goes 1440px
full-bleed to 1200px centred, no overflow at 1440px or 390px.

axiant-v2.css gains two sections: 23 legacy-markup component rules, each one
measured losing its fill or border without them, and 32KB of page-scoped CSS
lifted out of ten per-page <style> blocks with their !important removed.

Also serves the responsive image variants that already existed unused on disk:
181 card and hero images gain srcset, 145 missing variants generated, the last
38 JPGs and 3 PNGs converted to WebP with the equipment-for-sale JSON source
data repointed so build.py will not undo it. equipment.html drops from 37.9MB
to 3.7MB.

877/877 pages conformant. axiant-v2-chrome.css and axiant-v2-legacy-body.css
are now referenced by zero pages.
EOF
)"

git push origin main
```

## Step 5 — verify live

Deployment is push-to-`main` (the only workflow in `.github/workflows/` is
`indexnow.yml`, which pings IndexNow — it does not build the site).

After the deploy lands, check on **https://axiantpartners.com/match.html**:

- **View source** — exactly one stylesheet, `/axiant-v2.css?v=202609030001`.
  No `styles.css`, no `critical.css`, no `axiant-v2-chrome.css`, no
  `axiant-v2-legacy-body.css`.
- The form renders in a centred white card ~1200px wide, submit button in
  accent blue `#2d7fb8`, and **the form still submits** (2 forms, 38 fields).
- **https://axiantpartners.com/equipment.html** — DevTools ▸ Network ▸ Img.
  Total transferred should be roughly 3–4 MB, not 38 MB. Card images should
  request `-800w.webp`, not the bare `.webp`.
- Spot-check one article page (`/equipment-financing/articles/affirm-vs-cherry/`)
  and one landing page (`/get-matched/working-capital/`) — on the latter the
  loan-type dropdown must still be hidden.

---

## Do NOT do these

- **Do not run `scripts/convert-program-page.py` on any of these pages.** It
  rebuilds a body out of content "bands" and a form is not a band — measured, it
  takes match.html from 2 forms to 0 and 25 fields to 0.
- **Do not re-add the legacy stylesheets** to any page that now loads
  `axiant-v2.css`. `check-page.py` will fail you, correctly.
- **Do not set `.form-step{display:none}`** on match.html. The step machinery is
  dead code — `script.js` only shows the Continue button on mobile
  (`nextBtn.style.display = isMobile() ? 'inline-flex' : 'none'`), so hiding the
  steps makes the desktop form unsubmittable. All four steps are meant to show
  at once on desktop. There is a comment in `axiant-v2.css` saying so.
- **Do not change the `$300M+ funded` / `Since 2020` copy** on match.html. Alex
  has been told twice it conflicts with the company's age and has chosen to keep
  it. Leave it.
- **Do not delete `styles.css` in this commit.** It is down to 3 referencing
  files but that is Alex's call to make after he has seen the site live.

## Optional follow-ups, only if Alex asks

- `styles.css` (239 KB), `axiant-v2-chrome.css` and `axiant-v2-legacy-body.css`
  are effectively dead and can be removed later.
- `assets/` holds ~1.1 GB of PNG `<picture>` fallbacks. No modern browser
  downloads them, so they cost deploy size, not page speed.
- Pre-existing bugs, unrelated to this work: `calculator.js` prints
  "per monthly"; `.calc-intro-loan` / `.calc-intro-lease` are dead selectors.
