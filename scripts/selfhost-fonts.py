# -*- coding: utf-8 -*-
"""
Serve Inter and Playfair Display from our own origin instead of Google's.

Every page opened with two render-blocking round-trips to a third party:
a stylesheet from fonts.googleapis.com, which then points at font files on
fonts.gstatic.com -- so the browser had to resolve DNS, negotiate TLS and fetch
a stylesheet from one host before it even learned the URL of the font on a
second host, all before first paint. The preconnect hints on the page reduced
that cost; they did not remove it.

The repo already had fonts/ with two woff2 files and a download-fonts.js that
fetched them, so the intent was there -- it just was not wired up. This pulls
the four Inter weights and two Playfair weights the CSS actually asks for,
declares them locally, and drops the Google links.

It also fixes a real rendering bug on the way past. styles.css declared:

    @font-face{font-family:'Inter';src:url('/fonts/inter-regular.woff2');
               font-weight:400 700}

-- one 400-weight file claiming the whole 400-700 range, so every 500/600/700
weight on a v1 page was synthetic bold smeared out of the regular face rather
than Inter's real semibold and bold. Now each weight maps to its own file.

Run scripts/bump-asset-version.py afterwards so browsers pick up the new CSS.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_backup-pre-v2-swap", "node_modules", ".git", "_preview",
             "_analysis", "_outreach", "_marketing", "_components",
             "tools", "scripts", "docs", "__pycache__"}

FACES = """/* Self-hosted: the first paint no longer waits on fonts.googleapis.com.
   One file per weight -- declaring a single face across `font-weight:400 700`
   makes the browser synthesise bold instead of using the real cut. */
@font-face{font-family:'Inter';src:url('/fonts/inter-400.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('/fonts/inter-500.woff2') format('woff2');font-weight:500;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('/fonts/inter-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:'Inter';src:url('/fonts/inter-700.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}
@font-face{font-family:'Playfair Display';src:url('/fonts/playfair-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}
@font-face{font-family:'Playfair Display';src:url('/fonts/playfair-700.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}
"""

# The two faces above the fold on essentially every page: body copy and the
# display face the h1 is set in. Preloading more than the critical faces costs
# bandwidth the first paint does not spend.
PRELOADS = (
    '<link rel="preload" href="/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>\n'
    '<link rel="preload" href="/fonts/playfair-700.woff2" as="font" type="font/woff2" crossorigin>\n'
)

# Any <link> pointing at either Google font host, in any attribute order.
GOOGLE_LINK = re.compile(
    r'[ \t]*<link\b(?=[^>]*fonts\.(?:googleapis|gstatic)\.com)[^>]*>[ \t]*\r?\n?',
    re.I)
IS_STYLESHEET = re.compile(r'rel=["\']stylesheet["\']', re.I)


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def write(p, s):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(s)


def patch_css(apply_changes):
    """Put the real faces in axiant-v2.css; fix the faux-bold pair in styles.css."""
    done = []

    v2 = os.path.join(ROOT, "axiant-v2.css")
    s = read(v2)
    if "@font-face" not in s:
        if apply_changes:
            write(v2, FACES + "\n" + s)
        done.append(("axiant-v2.css", "6 faces added"))
    else:
        done.append(("axiant-v2.css", "already has @font-face - skipped"))

    v1 = os.path.join(ROOT, "styles.css")
    s = read(v1)
    before = s
    s = s.replace(
        "@font-face{font-family:'Inter';src:url('/fonts/inter-regular.woff2') format('woff2');font-weight:400 700;font-style:normal;font-display:swap}",
        "@font-face{font-family:'Inter';src:url('/fonts/inter-400.woff2') format('woff2');font-weight:400;font-style:normal;font-display:swap}"
        "@font-face{font-family:'Inter';src:url('/fonts/inter-500.woff2') format('woff2');font-weight:500;font-style:normal;font-display:swap}"
        "@font-face{font-family:'Inter';src:url('/fonts/inter-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}"
        "@font-face{font-family:'Inter';src:url('/fonts/inter-700.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}")
    s = s.replace(
        "@font-face{font-family:'Playfair Display';src:url('/fonts/playfair-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}",
        "@font-face{font-family:'Playfair Display';src:url('/fonts/playfair-600.woff2') format('woff2');font-weight:600;font-style:normal;font-display:swap}"
        "@font-face{font-family:'Playfair Display';src:url('/fonts/playfair-700.woff2') format('woff2');font-weight:700;font-style:normal;font-display:swap}")
    if s != before:
        if apply_changes:
            write(v1, s)
        done.append(("styles.css", "synthetic-bold range split into real weights"))
    else:
        done.append(("styles.css", "no match - check by hand"))
    return done


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def patch_html(apply_changes):
    swapped = 0
    for path in pages():
        src = read(path)
        found = GOOGLE_LINK.findall(src)
        if not found:
            continue
        had_stylesheet = any(IS_STYLESHEET.search(t) for t in found)
        out = GOOGLE_LINK.sub("", src)
        # Only pages that were actually pulling the stylesheet need the
        # preload; a page carrying a stray preconnect and nothing else just
        # loses the dead hint.
        if had_stylesheet and "/fonts/inter-400.woff2" not in out:
            idx = out.lower().rfind("</head>")
            if idx != -1:
                out = out[:idx] + PRELOADS + out[idx:]
        if out != src:
            swapped += 1
            if apply_changes:
                write(path, out)
    return swapped


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for name, note in patch_css(apply_changes):
        print(f"  {name:16} {note}")
    print(f"  pages de-googled: {patch_html(apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
