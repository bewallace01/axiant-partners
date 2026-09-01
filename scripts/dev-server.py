#!/usr/bin/env python3
"""Local preview server that never lets the browser cache anything.

Why this exists: `python -m http.server` sends Last-Modified and no
Cache-Control, so Chrome happily serves a stale copy after you edit a file.
During this redesign that repeatedly made finished pages look unconverted -
the file on disk was right, the browser was showing yesterday.

    python scripts/dev-server.py          # port 8765
    python scripts/dev-server.py 9000     # any other port

Then just hit reload. No Ctrl+Shift+R, no ?v= query strings, no DevTools
"disable cache" checkbox to remember.
"""
import sys, os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class NoCacheHandler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_header(self, key, value):
        # drop the validators Chrome uses to serve from cache
        if key.lower() in ("last-modified", "etag"):
            return
        super().send_header(key, value)

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"serving {ROOT}")
    print(f"  http://127.0.0.1:{port}/            (no-cache: edits show on plain reload)")
    print("  Ctrl+C to stop\n")
    ThreadingHTTPServer(("127.0.0.1", port), NoCacheHandler).serve_forever()
