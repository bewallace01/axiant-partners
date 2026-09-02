# -*- coding: utf-8 -*-
"""
Stop shipping language-switcher.js (91.4 KB) on the pages that do not use it.

WHAT IT ACTUALLY DID, measured rather than assumed. Every archetype was
rendered in Chrome twice, once with the script and once without, and the two
DOMs compared node by node (v2 service page, v2 article, v2 hub, v2 industry
page, v1 lander, v1 form page):

  v2 pages   nodes 850 -> 843. The difference is exactly two things:
             * <script id="axiant-org-jsonld"> -- an Organization JSON-LD node
               injected at runtime when the page has none
             * #mobileNavOverlay -- a SECOND mobile nav overlay, with its own
               logo <img>, close button and link list, injected alongside the
               #mobileMenu that v2 already ships. v2's own menu was tested
               open/close with and without the script and behaves identically,
               so the injected one is a duplicate of a control that already
               works.

  v1 pages   nodes 366 -> 365. Only the JSON-LD node. No overlay -- that path
             needs v2's .mobile-menu-close to exist.

Neither is worth 91.4 KB on 761 pages. The JSON-LD is replaced here with a
server-rendered Organization node, which is a better signal than a
script-injected one anyway; the duplicate overlay just goes.

WHAT IS DELIBERATELY LEFT ALONE. 28 pages carry a .mobile-cta-bar -- a sticky
mobile call/apply bar that CSS parks off-screen at translateY(120%) until
initCtaBar() adds .is-visible on scroll. That function lives in this script.
It could not be made to fire in a test harness either way, so it may already be
broken, but "may already be broken" is not proof, and the failure mode is a
silently hidden conversion CTA. Those pages keep the script until someone
ports initCtaBar deliberately.

script.js is untouched everywhere. It is live code -- addRevealClasses marks
117 nodes on a typical page, and enhanceTablesForMobile wraps tables for
horizontal scroll.
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_backup-pre-v2-swap", "node_modules", ".git", "_preview",
             "_analysis", "_outreach", "_marketing", "_components",
             "tools", "scripts", "docs", "__pycache__", "_jstest"}

TAG = re.compile(
    r'[ \t]*<script\b(?=[^>]*\blanguage-switcher\.js)[^>]*>\s*</script>[ \t]*\r?\n?',
    re.I)

# The sticky mobile CTA bar, the one behaviour still worth keeping the script for.
KEEPS_SCRIPT = re.compile(r'class="[^"]*\bmobile-cta-bar\b', re.I)

HAS_ORG = re.compile(r'"@type"\s*:\s*"Organization"')

ORG_NODE = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://axiantpartners.com/#organization",
    "name": "Axiant Partners",
    "url": "https://axiantpartners.com/",
    "logo": {"@type": "ImageObject",
             "url": "https://axiantpartners.com/logo-horizontal-transparent.png"},
    "telephone": "+1-561-268-0465",
    "address": {"@type": "PostalAddress", "addressLocality": "Boca Raton",
                "addressRegion": "FL", "addressCountry": "US"},
    "areaServed": {"@type": "Country", "name": "United States"},
    "sameAs": [
        "https://www.linkedin.com/company/axiantpartners/",
        "https://www.facebook.com/axiantpartners",
        "https://www.instagram.com/axiantpartners",
        "https://www.youtube.com/@axeltheloanlion",
    ],
}
ORG_BLOCK = ('<script type="application/ld+json">\n'
             + json.dumps(ORG_NODE, separators=(",", ":"))
             + '\n</script>\n')

# The footer component and the pages carry a warning about a runtime footer
# rewrite that can no longer happen once the script is gone.
STALE_NOTE = re.compile(
    r'\n[ \t]*Do NOT add the class "site-footer" to the <footer> below\.\s*'
    r'\n[ \t]*language-switcher\.js runs enhanceGlobalFooter\(\), which does\s*'
    r'\n[ \t]*querySelector\(\'\.site-footer\'\) and REPLACES the whole innerHTML with the\s*'
    r'\n[ \t]*legacy footer - silently wiping this markup at runtime\.')


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def main(apply_changes):
    dropped = injected = kept = notes = 0
    kept_files = []
    for path in pages():
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        if not TAG.search(src):
            continue
        if KEEPS_SCRIPT.search(src):
            kept += 1
            kept_files.append(os.path.relpath(path, ROOT).replace("\\", "/"))
            continue

        out = TAG.sub("", src)
        dropped += 1
        if not HAS_ORG.search(out):
            idx = out.lower().rfind("</head>")
            if idx != -1:
                out = out[:idx] + ORG_BLOCK + out[idx:]
                injected += 1
        stale = STALE_NOTE.sub("", out)
        if stale != out:
            notes += 1
            out = stale
        if apply_changes:
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(out)

    print("APPLIED" if apply_changes else "DRY RUN")
    print(f"  script dropped from            : {dropped} pages")
    print(f"  server-rendered Organization   : {injected} pages")
    print(f"  stale footer warning removed   : {notes} pages")
    print(f"  kept (have .mobile-cta-bar)    : {kept} pages")
    for f in kept_files[:5]:
        print(f"      {f}")
    if len(kept_files) > 5:
        print(f"      ... and {len(kept_files) - 5} more")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
