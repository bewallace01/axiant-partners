# -*- coding: utf-8 -*-
"""Fourth and final deepening pass. Marine 1,703 and drone 1,672 need ~130-160
words each to clear 1,800."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_vertical_pillars import deepen

PAGES = {
    "commercial-marine-financing.html": [
        ("Common Reasons a Marine Application Stalls",
         "<p>Most marine deals that fail do so for reasons that were visible at "
         "the start:</p>"
         "<ul>"
         "<li><strong>The survey finds structural work</strong> the seller had "
         "not disclosed, changing the value and the price at once.</li>"
         "<li><strong>Documentation is unclear</strong> &mdash; an unreleased "
         "lien from a previous owner, or a vessel whose registration status does "
         "not match the paperwork.</li>"
         "<li><strong>Insurance for commercial operation</strong> is quoted on "
         "recreational terms, and the correct cover costs materially more or is "
         "harder to place.</li>"
         "<li><strong>Permits do not transfer</strong> as the buyer assumed, "
         "which on a fishing vessel can remove most of the value the deal was "
         "built on.</li>"
         "<li><strong>Seasonal accounts read as decline</strong> when only the "
         "quiet months are supplied, rather than a full trading year.</li>"
         "</ul>"
         "<p>Each of those is checkable before an offer is made. The survey and "
         "the lien search are the two worth paying for early, because they are "
         "the ones that change whether the deal exists at all.</p>"),
    ],
    "drone-financing.html": [
        ("Where Drone Operators Most Often Get Stuck",
         "<p>A few patterns account for most declined or stalled applications in "
         "this sector:</p>"
         "<ul>"
         "<li><strong>Financing consumables.</strong> Batteries, propellers and "
         "software subscriptions are operating costs. Asking equipment finance "
         "to cover them does not work, because there is nothing to secure.</li>"
         "<li><strong>Buying ahead of demand.</strong> Capability purchased "
         "speculatively, with the pipeline described as an intention rather than "
         "a contract.</li>"
         "<li><strong>Certification pending.</strong> A waiver applied for is "
         "not a waiver held, and work that cannot yet legally be flown cannot "
         "underwrite the payment.</li>"
         "<li><strong>Terms longer than the kit lasts.</strong> A five-year "
         "facility on a sensor replaced in three.</li>"
         "<li><strong>Hobbyist insurance</strong> presented for commercial "
         "operation, which is a different policy entirely.</li>"
         "</ul>"
         "<p>All five are fixable before applying, and doing so usually costs "
         "nothing but sequencing.</p>"),
    ],
}


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for path, secs in PAGES.items():
        print(f"  {path:34} {deepen(path, secs, apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
