#!/usr/bin/env python3
"""Give every content <h2> a stable anchor id so Google can deep-link the section.

Google surfaces section-level jump links (page/#section) at noticeably better
positions than the parent page, but it can only do that when the heading carries
an id. Roughly a third of the site's pages have h2s with no id at all, which
makes those sections structurally impossible to surface.

Slug convention matches the pages that already have ids: lowercase, parentheses
dropped, every run of non-alphanumerics collapsed to a single hyphen, trimmed.
"Frequently Asked Questions" is special-cased to `faq`, which is what the
existing pages use.

Idempotent. Only ever ADDS an id= attribute to an h2 that lacks one; never
rewrites an existing id, never touches heading text, never reorders attributes.

    python3 scripts/add_h2_anchor_ids.py --dry-run     # report only
    python3 scripts/add_h2_anchor_ids.py               # write
    python3 scripts/add_h2_anchor_ids.py --limit 5     # first N changed files
"""
import io
import os
import re
import sys
import html
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKIP_DIRS = {"_analysis", "_components", "_marketing", "_outreach", "node_modules",
             "tools", "docs", "scripts", ".git", "assets", "fonts"}

# Headings that are navigational furniture rather than content sections.
SKIP_TEXT = {"related resources", "related articles", "related guides"}

FAQ_TEXT = {"frequently asked questions", "faq", "faqs",
            "frequently asked questions (faq)", "common questions"}

H2_RE = re.compile(r"<h2(?P<attrs>[^>]*)>(?P<inner>.*?)</h2>", re.S | re.I)
ID_RE = re.compile(r"""\bid\s*=\s*["']([^"']*)["']""", re.I)
SCRIPT_RE = re.compile(r"<(script|style|template|textarea)\b.*?</\1>", re.S | re.I)


def slugify(text):
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)          # strip inline tags
    text = text.replace("&", " and ")
    text = re.sub(r"[()\[\]]", "", text)           # drop bracket chars, keep content
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text[:80].rstrip("-")


def mask_scripts(s):
    """Replace script/style/template bodies with same-length filler so heading
    regexes cannot match anything inside them. Offsets stay identical."""
    spans = []
    for m in SCRIPT_RE.finditer(s):
        spans.append((m.start(), m.end()))
    if not spans:
        return s, spans
    buf = list(s)
    for a, b in spans:
        for i in range(a, b):
            if buf[i] not in "\n\r":
                buf[i] = " "
    return "".join(buf), spans


def process(path):
    raw = io.open(path, encoding="utf-8").read()
    masked, _ = mask_scripts(raw)

    reserved = set(ID_RE.findall(masked))
    edits = []          # (start_of_attrs, slug)
    added = []

    for m in H2_RE.finditer(masked):
        attrs = m.group("attrs")
        if ID_RE.search(attrs):
            continue
        text = m.group("inner")
        plain = re.sub(r"<[^>]+>", " ", html.unescape(text))
        plain = re.sub(r"\s+", " ", plain).strip()
        if not plain:
            continue
        low = plain.lower().rstrip(":").strip()
        if low in SKIP_TEXT:
            continue
        slug = "faq" if low in FAQ_TEXT else slugify(plain)
        if not slug:
            continue
        base, n = slug, 2
        while slug in reserved:
            slug = f"{base}-{n}"
            n += 1
        reserved.add(slug)
        edits.append((m.start("attrs"), slug))
        added.append((slug, plain[:60]))

    if not edits:
        return None

    out = raw
    for pos, slug in sorted(edits, reverse=True):   # back-to-front keeps offsets valid
        out = out[:pos] + f' id="{slug}"' + out[pos:]

    # --- safety checks -------------------------------------------------
    # 1. only additions, and exactly the expected byte growth
    expected = sum(len(f' id="{s}"') for _, s in edits)
    if len(out) - len(raw) != expected:
        return {"path": path, "error": f"byte delta {len(out)-len(raw)} != expected {expected}"}
    # 2. heading count unchanged
    if len(H2_RE.findall(out)) != len(H2_RE.findall(raw)):
        return {"path": path, "error": "h2 count changed"}
    # 3. tag balance unchanged for structural tags
    for tag in ("div", "p", "h2", "section", "main", "script"):
        o = len(re.findall(rf"<{tag}[\s>]", raw, re.I)) - len(re.findall(rf"</{tag}>", raw, re.I))
        n2 = len(re.findall(rf"<{tag}[\s>]", out, re.I)) - len(re.findall(rf"</{tag}>", out, re.I))
        if o != n2:
            return {"path": path, "error": f"<{tag}> balance changed {o} -> {n2}"}
    # 4. removing the inserted attributes must reproduce the original exactly
    check = out
    for _, slug in sorted(edits, reverse=True):
        check = check.replace(f' id="{slug}"', "", 1)
    if check != raw:
        # replace() is order-sensitive; fall back to a targeted rebuild
        check = out
        for pos, slug in sorted(edits, reverse=True):
            ins = f' id="{slug}"'
            if check[pos:pos + len(ins)] != ins:
                return {"path": path, "error": "reverse-check offset mismatch"}
            check = check[:pos] + check[pos + len(ins):]
        if check != raw:
            return {"path": path, "error": "reverse-check content mismatch"}
    # 5. no duplicate ids anywhere in the result
    all_ids = ID_RE.findall(mask_scripts(out)[0])
    dupes = {i for i in all_ids if all_ids.count(i) > 1 and i}
    if dupes:
        return {"path": path, "error": f"duplicate ids: {sorted(dupes)[:4]}"}

    return {"path": path, "out": out, "added": added}


def main():
    dry = "--dry-run" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    files = []
    for root, dirs, names in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for n in names:
            if n.endswith(".html"):
                files.append(os.path.join(root, n))
    files.sort()

    changed, errors, total_ids = [], [], 0
    for f in files:
        try:
            r = process(f)
        except Exception as e:                      # noqa: BLE001
            errors.append({"path": f, "error": f"{type(e).__name__}: {e}"})
            continue
        if not r:
            continue
        if "error" in r:
            errors.append(r)
            continue
        changed.append(r)
        total_ids += len(r["added"])

    if limit:
        changed = changed[:limit]

    print(f"scanned {len(files)} html files")
    print(f"pages needing ids: {len(changed)}   ids to add: {total_ids}")
    if errors:
        print(f"\n!! SKIPPED {len(errors)} file(s) failing a safety check:")
        for e in errors[:15]:
            print(f"   {os.path.relpath(e['path'], BASE)}: {e['error']}")

    print("\nsample of what will change:")
    for r in changed[:6]:
        rel = os.path.relpath(r["path"], BASE)
        print(f"\n  {rel}  (+{len(r['added'])})")
        for slug, txt in r["added"][:6]:
            print(f'      id="{slug}"   <- {txt}')

    if dry:
        print("\n[dry run] nothing written")
        return

    written = 0
    for r in changed:
        io.open(r["path"], "w", encoding="utf-8", newline="").write(r["out"])
        written += len(r["added"])
    print(f"\nwrote {len(changed)} files, added {written} anchor ids")


if __name__ == "__main__":
    main()
