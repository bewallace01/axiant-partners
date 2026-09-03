#!/usr/bin/env python3
"""Cut 4K grid images into the individual aside photos.

    python3 scripts/slice-grids.py              # slice every grid present
    python3 scripts/slice-grids.py --rows 1     # grids that stack 2 panels, not 2x2
    python3 scripts/slice-grids.py --dry-run

Reads _photo-manifest/batch-plan.json, which says which quadrant of which grid
holds which subject, and which target files that subject fills. For each grid
image in _photo-manifest/grids/ it crops the cell, centre-crops to 2.22:1
(the slot renders 532x240), resizes to 1064x480 and writes WebP q82 to every
target filename that subject serves - one subject can fill several slots.

Missing grids are skipped, so generate a few batches and run it, then more.
"""
import json, os, sys
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLAN = os.path.join(ROOT, "_photo-manifest", "batch-plan.json")
GRIDS = os.path.join(ROOT, "_photo-manifest", "grids")
DRY = "--dry-run" in sys.argv
ROWS = 2
if "--rows" in sys.argv:
    ROWS = int(sys.argv[sys.argv.index("--rows") + 1])
COLS = 2 if ROWS == 2 else 1

TARGET_W, TARGET_H = 1064, 480
RATIO = TARGET_W / TARGET_H

plan = json.load(open(PLAN, encoding="utf-8"))
written = skipped_grid = 0

for b in plan:
    src = None
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = os.path.join(GRIDS, b["batch"] + ext)
        if os.path.exists(p):
            src = p; break
    if not src:
        skipped_grid += 1; continue
    im = Image.open(src).convert("RGB")
    W, H = im.size
    cw, ch = W // COLS, H // ROWS
    for cell in b["cells"]:
        q = cell["quadrant"]
        col, row = (q % COLS, q // COLS) if COLS > 1 else (0, q)
        if row >= ROWS:
            continue
        box = im.crop((col * cw, row * ch, (col + 1) * cw, (row + 1) * ch))
        # centre-crop the cell to 2.22:1
        bw, bh = box.size
        if bw / bh > RATIO:
            nw = int(bh * RATIO); box = box.crop(((bw - nw) // 2, 0, (bw - nw) // 2 + nw, bh))
        else:
            nh = int(bw / RATIO); box = box.crop((0, (bh - nh) // 2, bw, (bh - nh) // 2 + nh))
        box = box.resize((TARGET_W, TARGET_H), Image.LANCZOS)
        for f in cell["files"]:
            out = os.path.join(ROOT, f)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            if not DRY:
                box.save(out, "WEBP", quality=82, method=6)
            written += 1
    print(("  would slice " if DRY else "  sliced ") + b["batch"] + "  -> " +
          str(sum(len(c["files"]) for c in b["cells"])) + " files")

print("")
print("files written     : " + str(written))
print("grids not present : " + str(skipped_grid))
if skipped_grid:
    print("(generate those and re-run - already-written files are simply overwritten)")
