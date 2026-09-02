# -*- coding: utf-8 -*-
"""
Place the built WebP assets into the live pages.

WHY NOT ingest-images.py --place, WHICH IS WHAT THE BRIEF ASKED FOR
That path writes the <img> into _backup-pre-v2-swap/<page>.html and then
re-runs convert-program-page.py on the live page. The backups are gitignored,
tracked on no branch, and stale against main - measured on the exact pages this
would touch:

    roofing-business-financing      backup 2528w  live 2559w
    hvac-business-financing         backup 2357w  live 2395w
    plumbing-business-financing     backup 2518w  live 2556w
    fencing-business-financing      backup 1524w  live 1571w
    moving-company-business-financing backup 1570w  live 1611w
    cleaning-business-financing     backup 1590w  live 1629w
    manufacturing-business-financing backup 2922w live 2959w
    inventory-financing             backup  837w  live  901w

Every backup is SHORTER than the page it would regenerate. Re-converting from
them would silently delete 31-64 words of real content per page, which is the
same class of failure as 02448e178 ("Rebuild v2 on current main, so the
conversion stops reverting SEO work").

Refreshing the backups from the live pages is not a fix either: a backup is a
PRE-v2 source, and the live pages are already v2. Feeding a converted page back
through the converter does not round-trip.

So the images go straight into the live pages. The edits are surgical and
additive - a placeholder becomes a picture, a hero src changes - and nothing
regenerates these pages, so there is nothing to clobber them.

WHAT IT DOES
  band      replaces <div class="aside-mark">...</div> inside the section whose
            heading matches the manifest's section_match, with the same
            <div class="prose-figure"><picture>...</picture></div> shape the
            converter emits on pages that already have photographs
  new-hero  swaps the src on <section class="hero-compact"> .hero-media img,
            and any matching rel=preload, to the page's own hero

Everything written references .webp only.
"""
import html, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "scripts", "image-manifest.json")

# The three pages whose hero belongs to a different page. Kept here rather than
# inferred so the swap can never hit the page the image legitimately belongs to.
HERO_SWAPS = {
    "moving-company-business-financing.html":
        ("box-truck-hero-bg", "moving-company-hero"),
    "cleaning-business-financing.html":
        ("landscaping-hero-bg", "cleaning-hero"),
    "inventory-financing.html":
        ("wcl-hero-operations", "inventory-financing-hero"),
}


def built(asset):
    return os.path.exists(os.path.join(ROOT, "assets", asset + ".webp"))


def variants(asset):
    out = []
    for vw in (400, 560, 800, 1200):
        if os.path.exists(os.path.join(ROOT, "assets", f"{asset}-{vw}w.webp")):
            out.append(vw)
    return out


def figure_html(e):
    """The same markup convert-program-page.py emits for a band image."""
    a = e["asset"]
    vs = variants(a)
    w, h = e["w"], e["h"]
    disp = 800 if 800 in vs else (vs[-1] if vs else None)
    src = f"/assets/{a}-{disp}w.webp" if disp else f"/assets/{a}.webp"
    dh = round(h * disp / w) if disp else h
    srcset = ", ".join(f"/assets/{a}-{v}w.webp {v}w" for v in vs) or src
    alt = (e.get("alt") or "").replace('"', "&quot;")
    return (
        '<div class="prose-figure"><picture>'
        f'<source srcset="{srcset}" sizes="(max-width:900px) 92vw, 46rem" type="image/webp"/>'
        f'<img alt="{alt}" decoding="async" loading="lazy" '
        f'src="{src}" width="{disp or w}" height="{dh}"/>'
        '</picture></div>'
    )


SECTION = re.compile(r'<section\b.*?</section>', re.S | re.I)
ASIDE = re.compile(r'<div[^>]*class="aside-mark"[^>]*>.*?</div>', re.S | re.I)


def place_band(page, e, apply_changes):
    p = os.path.join(ROOT, page.replace("/", os.sep))
    if not os.path.exists(p):
        return "PAGE MISSING"
    s = io.open(p, encoding="utf-8").read()
    if f"/assets/{e['asset']}" in s:
        return "already placed"
    # Headings are stored escaped - "Septic &amp; Portable Sanitation" - while
    # the manifest writes the character. Unescape both sides before comparing,
    # or every ampersand heading silently fails to match.
    want = html.unescape(e["section_match"]).lower()
    for m in SECTION.finditer(s):
        sec = m.group(0)
        heads = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", sec, re.S | re.I)
        if not any(want in html.unescape(re.sub(r"<[^>]+>", "", x)).lower() for x in heads):
            continue
        am = ASIDE.search(sec)
        if not am:
            return f"no placeholder in section {e['section_match']!r}"
        new_sec = sec[:am.start()] + figure_html(e) + sec[am.end():]
        out = s[:m.start()] + new_sec + s[m.end():]
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
        return "placed"
    return f"section not found: {e['section_match']!r}"


def swap_hero(page, old, new, apply_changes):
    p = os.path.join(ROOT, page)
    if not os.path.exists(p):
        return "PAGE MISSING"
    s = io.open(p, encoding="utf-8").read()
    if f"/assets/{new}" in s:
        return "already swapped"
    if f"/assets/{old}" not in s:
        return f"current hero {old} not found"
    out = re.sub(rf"/assets/{re.escape(old)}(-\d+w)?\.webp",
                 lambda m: f"/assets/{new}{m.group(1) or ''}.webp", s)
    if apply_changes:
        io.open(p, "w", encoding="utf-8", newline="").write(out)
    return "swapped"


def main(apply_changes):
    cfg = json.load(io.open(MANIFEST, encoding="utf-8"))
    print("APPLIED" if apply_changes else "DRY RUN")

    print("\n-- band images --")
    ok = skip = bad = 0
    for e in cfg["images"]:
        if e["type"] != "band":
            continue
        if not built(e["asset"]):
            print(f"  --  {e['asset']:38} not built yet (art pending)")
            skip += 1
            continue
        r = place_band(e["page"], e, apply_changes)
        flag = "  " if r in ("placed", "already placed") else "!!"
        if flag == "!!":
            bad += 1
        else:
            ok += 1
        print(f"  {flag}  {e['asset']:38} {r}")

    print("\n-- heroes that belong to another page --")
    for page, (old, new) in HERO_SWAPS.items():
        if not built(new):
            print(f"  --  {new:38} not built")
            continue
        r = swap_hero(page, old, new, apply_changes)
        flag = "  " if r in ("swapped", "already swapped") else "!!"
        if flag == "!!":
            bad += 1
        print(f"  {flag}  {page:38} {old} -> {new}: {r}")

    print(f"\n  placed/ok {ok}, pending art {skip}, problems {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
