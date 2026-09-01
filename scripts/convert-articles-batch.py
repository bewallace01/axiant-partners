"""Resumable article conversion. Converts pending pages until a time budget is
spent, then exits cleanly - long-running background jobs stall on the mounted
filesystem, so progress is made in short, repeatable passes."""
import contextlib, io, importlib.util, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

args = [a for a in sys.argv[1:] if not a.startswith("--")]
budget = float(args[0]) if args else 35.0
pages = conv.article_pages()
force = "--all" in sys.argv
pending = pages if force else [
    p for p in pages
    if "axiant-v2.css" not in (ROOT / p).read_text(encoding="utf-8", errors="ignore")]
start, done, errs = time.time(), 0, []
for rel in pending:
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            conv.convert(ROOT / rel)
        done += 1
    except Exception as e:
        errs.append("%s :: %s: %s" % (rel, type(e).__name__, str(e)[:90]))
    if time.time() - start > budget:
        break
print("converted %d this pass | %d were pending | %d total | errors %d"
      % (done, len(pending), len(pages), len(errs)))
for e in errs[:6]:
    print("  !!", e)
