"""Convert everything still on the old design: landing pages, location pages,
loan-amount pages, the remaining articles and the document pages. Skips
meta-refresh redirect stubs, which have nothing to show. Time-boxed and
resumable - the mount stalls on long-running jobs."""
import contextlib, importlib.util, io, pathlib, re, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

def pending():
    out = []
    for f in sorted(ROOT.rglob("*.html")):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith("_") or "/_" in rel or rel.startswith("node_modules/"):
            continue
        t = f.read_text(encoding="utf-8", errors="ignore")
        if "axiant-v2.css" in t:
            continue
        if re.search(r'http-equiv=["\']refresh', t, re.I):
            continue                      # redirect stub: nothing to convert
        # fragments and embeds are partial documents pulled into other pages;
        # wrapping them in a full page would break whatever includes them
        if "/fragments/" in rel or f.name.endswith("embed.html"):
            continue
        if "<html" not in t.lower() or "<head" not in t.lower():
            continue
        out.append(rel)
    return out

budget = float([a for a in sys.argv[1:] if not a.startswith("-")][0]) if len(sys.argv) > 1 else 40.0
todo = pending()
start, done, errs = time.time(), 0, []
for rel in todo:
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            conv.convert(ROOT / rel)
        done += 1
    except Exception as e:
        errs.append("%s :: %s: %s" % (rel, type(e).__name__, str(e)[:90]))
    if time.time() - start > budget:
        break
print("converted %d this pass | %d pending | errors %d" % (done, len(todo), len(errs)))
for e in errs[:8]:
    print("  !!", e)
