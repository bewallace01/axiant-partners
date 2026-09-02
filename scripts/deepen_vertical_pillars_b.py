# -*- coding: utf-8 -*-
"""Second deepening pass on the four vertical pillars.

After pass one: aircraft 1,543, marine 1,206, drone 1,173, data center 1,714.
The target is 1,800-2,500, so this pass is weighted to the thinnest two.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deepen_vertical_pillars import table, deepen

PAGES = {}

PAGES["commercial-marine-financing.html"] = [
    ("Repower and Refit Financing",
     "<p>A large share of marine lending is not a purchase at all. Repowering an "
     "existing vessel &mdash; new engines, gear, electronics, sometimes a hull "
     "extension &mdash; is often the better economic decision than replacing a "
     "boat that is otherwise sound, and it is financed differently.</p>"
     "<p>The distinction that matters to a lender is whether the work "
     "<strong>adds value to the vessel</strong> or merely maintains it. New "
     "engines in a well-found hull increase what the vessel is worth and extend "
     "its working life, which supports lending against it. Routine maintenance "
     "does not, however necessary it is.</p>"
     "<p>Three practical points on a refit application:</p>"
     "<ul>"
     "<li><strong>Get the yard quote in writing and itemised.</strong> A lender "
     "will fund specified work, not a lump sum described as an overhaul.</li>"
     "<li><strong>Expect staged disbursement.</strong> Funds released against "
     "milestones rather than paid up front, which is normal and worth planning "
     "cash flow around.</li>"
     "<li><strong>Budget the downtime.</strong> A vessel in the yard earns "
     "nothing, and the refit period is often the tightest cash month of the "
     "year.</li>"
     "</ul>"),
    ("Seasonality and How Lenders Read It",
     "<p>Few industries are as openly seasonal as commercial marine work. "
     "Charter and tour operators may earn most of their revenue in a handful of "
     "months; fishing follows seasons and quotas; even workboat operations "
     "follow weather windows.</p>"
     "<p>Lenders who work in the sector expect this and read the year as a "
     "whole rather than reacting to a quiet month. What they look for is "
     "evidence the operator manages it deliberately:</p>"
     "<ul>"
     "<li><strong>A full trading year</strong> rather than the strong months, so "
     "the shape is visible</li>"
     "<li><strong>Cash held through the off-season</strong>, which is the single "
     "clearest sign of a well-run seasonal business</li>"
     "<li><strong>Payment structures that match</strong> &mdash; some marine "
     "lenders will structure seasonal or skip payments so the schedule follows "
     "the revenue</li>"
     "<li><strong>Off-season plans</strong>, whether that is maintenance, a "
     "different trade, or a genuine shutdown that is budgeted for</li>"
     "</ul>"
     "<p>If a seasonal payment structure would help, ask for it at term-sheet "
     "stage. It is a common arrangement in marine lending and much harder to "
     "introduce after the documents are drawn.</p>"),
]

PAGES["drone-financing.html"] = [
    ("Buying Against Leasing Fast-Moving Kit",
     "<p>Drone equipment is unusual in how quickly capability moves. A sensor "
     "that is competitive today may be two generations behind within a few "
     "years, and that reality should shape the structure rather than be "
     "discovered by it.</p>"
     + table(["", "Buying", "Leasing"], [
         ["Ownership at the end", "Yours", "Returned, or bought out"],
         ["Obsolescence risk", "Carried by you", "Shared with the lessor"],
         ["Monthly cost", "Higher", "Usually lower"],
         ["Suits", "Kit with a long useful life &mdash; vehicles, ground stations",
          "Payloads and airframes on a fast refresh cycle"],
         ["Upgrade path", "Sell and replace", "Return and re-lease"],
     ])
     + "<p>The sensible split for most operations mirrors the equipment itself: "
       "own the things that last, lease the things that date. A vehicle and a "
       "ground station will serve for years; a payload competing on resolution "
       "will not.</p>"
       "<p>Whichever route, keep the term inside the working life. Financing a "
       "sensor over five years when you will replace it in three means paying "
       "for obsolete kit alongside its successor.</p>"),
    ("Sizing the Facility Around the Work",
     "<p>The most common mistake in this sector is buying capability before "
     "demand, on the reasoning that better equipment wins better contracts. It "
     "occasionally does. More often it produces an operator with excellent "
     "sensors, monthly payments and an empty schedule.</p>"
     "<p>A more reliable sequence:</p>"
     "<ul>"
     "<li><strong>Win the work first</strong>, or at least establish that the "
     "demand is real and repeatable</li>"
     "<li><strong>Finance to the contract</strong>, so the payment has revenue "
     "behind it from the first month</li>"
     "<li><strong>Keep the term inside the contract</strong> where you can, "
     "rather than carrying payments past the work that justified them</li>"
     "<li><strong>Add capability incrementally</strong> as utilization "
     "justifies it</li>"
     "</ul>"
     "<p>This is also what a lender wants to see, so the discipline that makes "
     "the business work is the same discipline that gets the application "
     "approved. An operator who can show utilization on existing kit is a "
     "straightforward file; one buying speculatively is not.</p>"),
]

PAGES["aircraft-financing.html"] = [
    ("Private Carriage Against Commercial Operation",
     "<p>How the aircraft will be used is not an administrative detail. It "
     "changes the insurance, the maintenance regime and the paperwork, and "
     "lenders ask early because it changes their risk.</p>"
     "<p>An aircraft flown privately by its owner is a straightforward "
     "proposition. One placed on a commercial certificate and flown for hire "
     "carries a heavier maintenance and inspection burden, different insurance, "
     "and a revenue stream that a lender may want to understand &mdash; "
     "particularly if that revenue is part of how the loan gets repaid.</p>"
     "<p>Two practical consequences worth planning for:</p>"
     "<ul>"
     "<li><strong>Say what you intend at application.</strong> Changing the "
     "operating basis after closing can breach the loan terms and the insurance "
     "policy at the same time.</li>"
     "<li><strong>Charter revenue is not guaranteed revenue.</strong> Where an "
     "owner plans to offset costs by placing the aircraft on a charter "
     "certificate, lenders discount projected utilization heavily. Build the "
     "case on what you can carry without it.</li>"
     "</ul>"),
]

PAGES["data-center-financing.html"] = [
    ("Owned Premises Against Colocation",
     "<p>Where the equipment physically sits changes what can be financed and "
     "how.</p>"
     "<p>In <strong>premises you own or lease directly</strong>, the "
     "infrastructure is yours: power, cooling and fit-out are assets on your "
     "balance sheet, and the longer-lived elements can sometimes be financed "
     "against the property itself rather than as equipment.</p>"
     "<p>In <strong>colocation</strong>, you are buying contracted rack space "
     "and power. That is an operating expense, not an asset, and it cannot be "
     "financed as equipment because there is nothing to secure. Your IT "
     "equipment inside that facility can still be financed, but a lender will "
     "note that recovering hardware from a third-party site is harder than "
     "collecting it from premises you control &mdash; and may price for it.</p>"
     "<p>Neither model is better. But the funding routes differ enough that the "
     "decision is worth making with the financing in view rather than "
     "afterwards.</p>"),
]


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for path, secs in PAGES.items():
        print(f"  {path:34} {deepen(path, secs, apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
