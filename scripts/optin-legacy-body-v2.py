# -*- coding: utf-8 -*-
"""
Give the v2 look to the pages that keep the v1 body, without touching markup.

These 37 pages already wear the v2 header and footer via axiant-v2-chrome.css
while their bodies are still styled by styles.css, so they read as two
different sites stitched together. Converting them properly is not an option:
convert-program-page.py rebuilds a body out of content bands, and measured on
the tool pages that takes match.html from 2 forms to 0 and 25 fields to 0, and
calculator.html from 1 form to 0 and 34 element ids to 3.

So nothing here changes markup. Each page gets exactly two edits:

  1. class="v2-body" on the <body> tag  -- the opt-in switch
  2. a <link> to axiant-v2-legacy-body.css, after the chrome sheet so it lands
     after styles.css and wins

Every rule in that sheet is prefixed .v2-body and its tokens are declared
there rather than on :root, so a page that has not opted in is untouched and
the collision that made loading all of axiant-v2.css unsafe cannot happen.
.container is never styled -- it is a full-width wrapper in styles.css and a
max-width centred one in v2, and that single clash is what flattened these
layouts the last time someone tried.

The <body> tag is located after </head>. Matching the first "<body>" in the
file finds one inside a CSS comment on several of these pages.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_backup-pre-v2-swap", "node_modules", ".git", "_preview",
             "_analysis", "_outreach", "_marketing", "_components",
             "tools", "scripts", "docs", "__pycache__", "claude"}

CHROME_LINK = re.compile(r'<link href="/axiant-v2-chrome\.css\?v=([0-9A-Za-z]+)" rel="stylesheet"/?>')
BODY_TAG = re.compile(r"<body(\s[^>]*)?>", re.I)


def pages():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".html"):
                yield os.path.join(dirpath, fn)


def opt_in(path, apply_changes):
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    if "AXIANT-HEADER:START" not in s or "axiant-v2-chrome.css" not in s:
        return None                     # not a hybrid
    if "axiant-v2.css" in s and "axiant-v2-chrome.css" not in s:
        return None                     # already fully v2
    if 'class="v2-body' in s or "axiant-v2-legacy-body.css" in s:
        return "already opted in"

    m = CHROME_LINK.search(s)
    if not m:
        return "NO CHROME LINK"
    v = m.group(1)

    head_end = s.lower().find("</head>")
    b = BODY_TAG.search(s, head_end if head_end > 0 else 0)
    if not b:
        return "NO <body> AFTER </head>"

    attrs = b.group(1) or ""
    if "class=" in attrs:
        tag = b.group(0).replace('class="', 'class="v2-body ', 1)
    else:
        tag = '<body class="v2-body">' if not attrs.strip() else f'<body class="v2-body"{attrs}>'
    out = s[:b.start()] + tag + s[b.end():]
    out = out.replace(m.group(0),
                      m.group(0) + f'<link href="/axiant-v2-legacy-body.css?v={v}" rel="stylesheet"/>',
                      1)

    if apply_changes:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(out)
    return "opted in"


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    done = skipped = bad = 0
    forms = []
    for p in sorted(pages()):
        r = opt_in(p, apply_changes)
        if r is None:
            continue
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        if r == "opted in":
            done += 1
            with open(p, encoding="utf-8") as fh:
                if "<form" in fh.read():
                    forms.append(rel)
        elif r == "already opted in":
            skipped += 1
        else:
            bad += 1
            print(f"  !! {rel:58} {r}")
        print(f"     {rel:58} {r}")
    print(f"\n  opted in {done}, already {skipped}, problems {bad}")
    if forms:
        print(f"\n  {len(forms)} of them contain a <form> - verify these interactively:")
        for f in forms:
            print(f"     {f}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
