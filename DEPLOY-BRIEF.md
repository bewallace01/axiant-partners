# Deploy brief — de-duplicate the aside photos

Repo: `axiant-partners` (origin `bewallace01/axiant-partners`, branch `main`).

**The previous batch is already live.** Commits `4dcd0fb13` (contrast fix, section
tones, 113 photos) and `a712494f7` (cache-bust bump) are pushed, and HEAD equals
origin/main. Nothing in this brief re-does that work.

What remains is one small follow-up.

---

## What this changes

36 pages were showing **the same photograph twice on the same page** — both aside
slots resolved to one image, which reads as a mistake rather than a design. The
worst example was `towing-business-financing.html`, with the identical tow-truck
shot in both slots.

Every duplicated slot now has a different, thematically adjacent photo, taken
from grid quadrants that were generated but never used:

- **6 DSCR pages** → a second property shot (multi-unit house, brick apartment,
  renovation) instead of repeating the duplex
- **4 loan-size pages** → different owner scenes (lender at a desk, kitchen
  table, team, calculator)
- **9 state pages** → rotated across nine different business scenes, so they
  don't repeat each other either
- **6 equipment pages** → dealer lot, tradesperson in a van, underwriter, etc.
- **11 others** — debt, acquisition, factoring, moving, towing, FAQ, legal pages

**Only image file contents changed. No HTML, no CSS.** Each slot already had its
own filename, so the fix was to overwrite the file the second slot points at.

---

## The change set

```
36 modified files, all under assets/aside/*.webp
 1 modified WORKLOG.md   (2 lines — Claude Code's own log)
```

Everything else `git status` reports is CRLF churn with no content change
(`git diff --ignore-cr-at-eol` shows nothing for those files).

Because these are **modifications to already-tracked files**, plain `git add -u`
is sufficient here — unlike the previous push, where `assets/aside/` was
untracked and needed `-A`. `git add -A` is still fine.

---

## Verify before committing

Both already pass locally.

```bash
# 1. no page repeats an image  -> expect 0
python3 - <<'PY'
import re, glob, hashlib, os
bad = slots = 0
for p in glob.glob('**/*.html', recursive=True):
    if any(x in p for x in ('node_modules','_backup','_to_delete','_preview')): continue
    s = open(p, encoding='utf-8', errors='replace').read()
    srcs = re.findall(r'class="aside-mark has-photo"><img src="([^"]+)"', s)
    slots += len(srcs)
    if len(srcs) < 2: continue
    h = [hashlib.md5(open(x.lstrip('/'),'rb').read()).hexdigest()
         for x in srcs if os.path.exists(x.lstrip('/'))]
    if len(set(h)) < len(h): bad += 1
print(f'{slots} photo slots, {bad} pages repeating an image')
PY

# 2. design system            -> expect "877/877 pages conformant"
python3 scripts/check-page.py
```

Current local state: **113 photo slots, 0 pages repeating, 877/877 conformant,
113 aside refs with 0 broken.**

---

## Commit and push

```bash
git add -A
git status --short | grep -v '^ M ' | head

git commit -m "$(cat <<'EOF'
Give each aside slot its own photo where a page repeated one

Thirty-six pages resolved both of their aside slots to the same image, which
reads as a mistake rather than a design - towing-business-financing.html showed
the identical tow-truck shot twice.

Each duplicated slot now draws a different, thematically adjacent photo from
grid quadrants that were generated but never used: the DSCR pages get a second
property shot rather than repeating the duplex, the loan-size pages get
different owner scenes, and the nine state pages rotate across nine scenes so
they do not repeat each other either.

Only file contents changed - every slot already had its own filename, so no
markup was touched. 113 slots, 64 visually distinct images, no page repeating.
EOF
)"

git push origin main
```

---

## Verify live

- **https://axiantpartners.com/towing-business-financing.html** — scroll through
  both aside images. The first is the tow truck; the second should now be an
  owner working at a laptop, **not** a second tow truck and **not** a lot full
  of excavators.
- **https://axiantpartners.com/dscr-loans.html** — the two property images
  should be different buildings.
- **https://axiantpartners.com/business-loans-texas.html** — second image should
  be a business scene, not a repeat of the Texas street.

---

## One thing worth knowing

Three images still appear on **four or more different pages** — unavoidable with
62 generated subjects covering 113 slots, and invisible unless someone opens two
pages side by side. Same-page repetition, the thing that actually looked wrong,
is gone. If you want those thinned out too, it needs more generated scenes, not
a code change.

## Do NOT do these

- **Do not regenerate the photos from `_photo-manifest/PROMPTS.txt` expecting the
  current set.** Batches 13-17 were rewritten by hand after that file was
  written; the file holds the earlier, weaker prompts.
- **Do not run `scripts/apply-aside-photos.py` expecting it to fix duplicates.**
  It only fills empty slots — it skips any slot that already carries an `<img>`.
  The de-duplication was done by replacing file contents.
- The standing rules from the last brief still hold: no
  `scripts/convert-program-page.py` on tool/article pages, no
  `.form-step{display:none}` on match.html, and leave the `$300M+ funded` copy
  alone.
