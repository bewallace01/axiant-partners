#!/usr/bin/env python3
"""Turn a folder of generated images into shipped site assets.

Everything this writes is WebP. Source files may be PNG, JPG or WebP; nothing
but WebP is written into assets/.

    python scripts/ingest-images.py                  # dry run: what matched
    python scripts/ingest-images.py --run            # build the assets
    python scripts/ingest-images.py --run --place    # ...and patch the sources
    python scripts/ingest-images.py --run --no-realism

Drop the generated files in _incoming/ named after the asset in
scripts/image-manifest.json (extension ignored): btl-hero.png, roofing-crew-tearoff.jpg.

Each image is centre-cropped to the manifest's aspect ratio, resized, passed
through scripts/photo-realism.py, and written as assets/<name>.webp plus
-400w -560w -800w -1200w variants.
"""
import argparse, importlib.util, json, pathlib, re, shutil, subprocess, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS, INCOMING = ROOT / "assets", ROOT / "_incoming"
BACKUP = ROOT / "_backup-pre-v2-swap"
SRC_EXT = (".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff")

_spec = importlib.util.spec_from_file_location("pr", ROOT / "scripts/photo-realism.py")
_pr = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_pr)


def page_key(rel):
    p = pathlib.Path(rel)
    return "__".join(p.parent.parts) if p.stem == "index" else \
           "__".join(list(p.parent.parts) + [p.stem])


def cover(img, w, h):
    """Centre-crop to the target aspect, then resize. Never distorts."""
    tw, th = w / h, img.width / img.height
    if th > tw:                       # too wide - trim the sides
        nw = int(img.height * tw)
        img = img.crop(((img.width - nw) // 2, 0, (img.width - nw) // 2 + nw, img.height))
    elif th < tw:                     # too tall - trim top and bottom
        nh = int(img.width / tw)
        img = img.crop((0, (img.height - nh) // 2, img.width, (img.height - nh) // 2 + nh))
    return img.resize((w, h), Image.LANCZOS)


def find_source(name):
    for ext in SRC_EXT:
        for cand in (INCOMING / (name + ext), INCOMING / (name + ext.upper())):
            if cand.exists():
                return cand
    return None


def build(entry, cfg, do_realism):
    src = find_source(entry["asset"])
    im = cover(Image.open(src).convert("RGB"), entry["w"], entry["h"])
    if do_realism:
        im = _pr.realism(im, strength=cfg.get("realism_strength", 1.0))
    out = ASSETS / (entry["asset"] + ".webp")
    im.save(out, format="WEBP", quality=cfg.get("quality", 86), method=6)
    written = [out.name]
    for vw in cfg.get("variants", [400, 560, 800, 1200]):
        if vw >= im.width:
            continue
        v = im.resize((vw, round(im.height * vw / im.width)), Image.LANCZOS)
        vp = ASSETS / f"{entry['asset']}-{vw}w.webp"
        v.save(vp, format="WEBP", quality=cfg.get("quality", 86), method=6)
        written.append(vp.name)
    return src, written


def repoint_png_refs(stem):
    """Rewrite /assets/<stem>.png references to .webp, in pages and sources."""
    hits = 0
    for f in list(ROOT.glob("*.html")) + list(BACKUP.glob("*.html")):
        t = f.read_text(encoding="utf-8", errors="ignore")
        n = t.replace(f"/assets/{stem}.png", f"/assets/{stem}.webp")
        if n != t:
            f.write_text(n, encoding="utf-8"); hits += 1
    return hits


def place(entry):
    """Insert the image into the page's pre-v2 source, next to its heading."""
    from bs4 import BeautifulSoup
    bp = BACKUP / (page_key(entry["page"]) + ".html")
    if not bp.exists():
        return f"no backup source at {bp.name}"
    o = BeautifulSoup(bp.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    want = entry["section_match"].lower()
    head = next((h for h in o.find_all(["h2", "h3"])
                 if want in h.get_text(" ", strip=True).lower()), None)
    if head is None:
        return f"section not found: {entry['section_match']!r}"
    if o.find("img", src=re.compile(re.escape(entry["asset"]))):
        return "already placed"
    tag = o.new_tag("img", src=f"/assets/{entry['asset']}.webp",
                    alt=entry.get("alt", ""), width=str(entry["w"]),
                    height=str(entry["h"]), loading="lazy", decoding="async")
    head.insert_after(tag)
    bp.write_text(str(o), encoding="utf-8")
    return "placed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--place", action="store_true")
    ap.add_argument("--no-realism", action="store_true")
    ap.add_argument("--only", default="", help="substring filter on asset name")
    a = ap.parse_args()

    cfg = json.loads((ROOT / "scripts/image-manifest.json").read_text())
    items = [e for e in cfg["images"] if a.only in e["asset"]]
    INCOMING.mkdir(exist_ok=True)

    ready = [e for e in items if find_source(e["asset"])]
    missing = [e for e in items if not find_source(e["asset"])]
    print(f"manifest {len(items)}  ready {len(ready)}  missing {len(missing)}")
    for e in missing:
        print(f"  missing  _incoming/{e['asset']}.(png|jpg|webp)")
    if not a.run:
        print("\ndry run - add --run to build")
        return

    to_place = []
    for e in ready:
        src, written = build(e, cfg, not a.no_realism)
        extra = ""
        if e.get("also_update_refs"):
            extra = f"  (repointed .png refs on {repoint_png_refs(e['asset'])} files)"
        print(f"  {src.name:44} -> {len(written)} webp{extra}")
        if e["type"] == "band" and a.place:
            to_place.append(e)

    if a.place:
        pages = set()
        for e in to_place:
            r = place(e)
            print(f"  place {e['asset']:34} {r}")
            if r == "placed":
                pages.add(e["page"])
        for p in sorted(pages):
            subprocess.run([sys.executable, "scripts/convert-program-page.py", p], cwd=ROOT)

    heroes = [e for e in ready if e["type"] == "new-hero"]
    if heroes:
        print("\nMANUAL: these need the page's hero repointed by hand -")
        for e in heroes:
            print(f"  {e['page']}: set the hero image to /assets/{e['asset']}.webp")
            if e.get("note"):
                print(f"      ({e['note']})")


if __name__ == "__main__":
    main()
