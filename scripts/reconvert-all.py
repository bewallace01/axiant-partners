"""Re-run the converter over every page that has a backup, so a change to the
extractors is applied everywhere. Time-boxed and resumable: it records what it
has done this round in .reconvert-state so the next pass picks up where the
last one stopped (the mounted filesystem stalls on long jobs)."""
import contextlib, importlib.util, io, pathlib, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
BACKUP = ROOT / "_backup-pre-v2-swap"
STATE = ROOT / ".reconvert-state"
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

def live_for(name):
    if "__" in name:
        return ROOT.joinpath(*name[:-5].split("__")) / "index.html"
    if (ROOT / name).exists():
        return ROOT / name
    if (ROOT / name[:-5] / "index.html").exists():
        return ROOT / name[:-5] / "index.html"
    return ROOT / name

args = [a for a in sys.argv[1:] if not a.startswith("-")]
budget = float(args[0]) if args else 150.0
if "--restart" in sys.argv and STATE.exists():
    STATE.write_text("")   # cannot unlink on the mount; empty it instead
done_set = set(STATE.read_text().split("\n")) if STATE.exists() else set()

# Hand-built or interactive pages the converter must never touch: the homepage,
# the matcher, the calculators, the print pieces, and the four index hubs that
# scripts/build-hubs.py owns.
SKIP = {
    ".html", "index.html", "match.html", "calculator.html", "calculator-embed.html",
    "embed-calculator.html", "construction-loan-calculator.html", "dscr-calculator.html",
    "mca-calculator.html", "sba-loan-calculator.html", "business-loan-calculator-guide.html",
    "rightmfgsystems.html", "referral.html", "consolidate.html",
    "employee-onboarding-handbook.html", "referral-partner-brochure-2-sided.html",
    "get-matched__equipment.html", "get-matched__line-of-credit.html",
    "get-matched__merchant-cash-advance.html", "get-matched__working-capital.html",
    "blog.html", "services.html", "industries.html", "equipment.html",
    "small-business-financing-report.html",   # bespoke report design
}
todo = [b.name for b in sorted(BACKUP.glob("*.html"))
        if b.name not in done_set and b.name not in SKIP]
start, done, errs = time.time(), 0, []
for name in todo:
    live = live_for(name)
    if not live.exists():
        done_set.add(name); continue
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            conv.convert(live)
        done += 1
    except Exception as e:
        errs.append("%s :: %s: %s" % (name, type(e).__name__, str(e)[:90]))
    done_set.add(name)
    if time.time() - start > budget:
        break
STATE.write_text("\n".join(sorted(x for x in done_set if x)))
print("reconverted %d this pass | %d left | errors %d"
      % (done, len(list(BACKUP.glob('*.html'))) - len(done_set), len(errs)))
for e in errs[:8]:
    print("  !!", e)
