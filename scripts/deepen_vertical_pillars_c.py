# -*- coding: utf-8 -*-
"""Third deepening pass. After pass two: aircraft 1,692, marine 1,529,
drone 1,471, data center 1,856 (in band). This closes the remaining three."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_vertical_pillars import table, deepen

PAGES = {}

PAGES["aircraft-financing.html"] = [
    ("Preparing an Aircraft Finance Application",
     "<p>Aircraft lending rewards preparation more than most categories, because "
     "so much of the decision rests on documents that either exist or do "
     "not.</p>"
     "<ul>"
     "<li><strong>Complete logbooks</strong> for airframe, engines and "
     "propellers. Gaps reduce value more reliably than most physical faults, and "
     "they cannot be created retrospectively.</li>"
     "<li><strong>Current weight and balance, and equipment list.</strong></li>"
     "<li><strong>Airworthiness directive compliance status</strong>, "
     "documented.</li>"
     "<li><strong>Time remaining</strong> on engines, propellers and any "
     "life-limited components, against the overhaul schedule.</li>"
     "<li><strong>Damage history</strong>, disclosed up front. Disclosed and "
     "repaired is workable; discovered at pre-buy is usually fatal.</li>"
     "<li><strong>Engine programme enrolment</strong> if applicable.</li>"
     "<li><strong>An insurance quote</strong> at the limits the lender will "
     "require, for the pilot who will actually fly it.</li>"
     "</ul>"
     "<p>That last point catches first-time buyers. Insurance for a newly-rated "
     "pilot moving into a more complex type can be both expensive and slow to "
     "arrange, and it is a closing condition rather than an afterthought. Get "
     "the quote while the offer is still being negotiated.</p>"),
]

PAGES["commercial-marine-financing.html"] = [
    ("How a Marine Application Is Assembled",
     "<p>Marine lending sits between equipment finance and specialist asset "
     "lending, and the file reflects that. What a lender will want, roughly in "
     "the order it becomes relevant:</p>"
     + table(["Stage", "What is needed", "Who provides it"], [
         ["Enquiry", "Vessel details, age, intended trade, amount sought", "You"],
         ["Indicative terms", "Basic financials and operating history", "You"],
         ["Valuation", "Condition and valuation survey", "Accredited surveyor"],
         ["Title and liens", "Documentation or state title, lien search",
          "Lender or documentation agent"],
         ["Insurance", "Hull and P&amp;I cover, lender named",
          "Your broker"],
         ["Closing", "Preferred ship mortgage recorded, funds released",
          "Lender and documentation agent"],
     ])
     + "<p>Two steps carry most of the risk to the timetable. The "
       "<strong>survey</strong> is where a deal changes shape, so book it early "
       "rather than treating it as a formality near closing. And "
       "<strong>documentation</strong> &mdash; establishing clean title and "
       "recording the mortgage &mdash; runs on its own timetable and cannot "
       "usefully be rushed.</p>"
       "<p>A vessel with clear documentation, a recent survey and a broker who "
       "understands commercial cover moves through this in a fraction of the "
       "time of one where each item is started from scratch when asked for.</p>"),
]

PAGES["drone-financing.html"] = [
    ("Building a Case a Lender Can Underwrite",
     "<p>Drone operations are still an unfamiliar category to many lenders, "
     "which means the burden of making the business legible falls more heavily "
     "on the operator than it would in a settled industry.</p>"
     "<p>The applications that go through easily tend to share the same "
     "features:</p>"
     "<ul>"
     "<li><strong>Revenue described by contract, not by capability.</strong> "
     "\"Three utility inspection contracts on annual renewal\" underwrites; "
     "\"we fly LiDAR surveys\" does not.</li>"
     "<li><strong>Utilisation figures for existing equipment.</strong> Flight "
     "hours, jobs completed, revenue per asset. It shows the last purchase "
     "worked.</li>"
     "<li><strong>Named clients with real credit.</strong> As with factoring, "
     "who pays you matters as much as what you do.</li>"
     "<li><strong>Certification and waivers in place</strong> for the work being "
     "financed, not applied for.</li>"
     "<li><strong>A clear split between hardware and operating costs</strong>, "
     "so it is obvious what the facility is actually funding.</li>"
     "</ul>"
     "<p>The underlying point is that a lender is not evaluating drones. They "
     "are evaluating a services business that happens to use them, and the "
     "operators who present it that way get treated accordingly.</p>"
     "<p>Where the operation is genuinely new, expect equipment finance to be "
     "harder and a general working capital facility or a line of credit to be "
     "the more realistic route until there is a trading record to point at.</p>"),
]


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for path, secs in PAGES.items():
        print(f"  {path:34} {deepen(path, secs, apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
