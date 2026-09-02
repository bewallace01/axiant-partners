# -*- coding: utf-8 -*-
"""
Deepen the four thin vertical pillars before their clusters are built.

The plan requires 1,800-2,500 words with at least one comparison table before
these pillars can anchor a cluster. Measured against the live pages (header,
footer and nav stripped):

    aircraft-financing           1,114 words   0 tables
    commercial-marine-financing    794 words   0 tables
    drone-financing                830 words   0 tables
    data-center-financing        1,302 words   0 tables

One thing the plan implied that turned out to be wrong: all four already carry
a visible FAQ with matching FAQPage schema, 4-5 questions each. So the gap is
depth and comparison tables, not answer-engine markup.

These are hybrid pages - v2 chrome, v1 body - so this appends sections in the
page's own <section class="about-section"> idiom rather than converting
anything. New sections are inserted immediately before the closing
about-section.cta-section, so the call to action stays last.
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTA = re.compile(r'<section class="about-section cta-section"', re.I)


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def section(heading, body):
    return ('<section class="about-section">\n'
            f'<h2 id="{slug(heading)}">{heading}</h2>\n{body}\n</section>\n')


def table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = ""
    for r in rows:
        tds = "".join(f'<td data-label="{headers[i]}">{c}</td>' for i, c in enumerate(r))
        trs += f"<tr>{tds}</tr>"
    return ('<div class="ba-table-wrap"><table class="ba-table">'
            f"<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>")


PAGES = {}

# --------------------------------------------------------------- aircraft --
PAGES["aircraft-financing.html"] = [
    ("How Aircraft Lenders Segment the Market",
     "<p>Aircraft financing is not one market. Lenders divide it by how the "
     "aircraft is used and how liquid it is, and those two things decide the "
     "terms far more than the buyer's balance sheet does.</p>"
     + table(["Segment", "Typical use", "How lenders treat it"], [
         ["Piston single and twin", "Owner-flown, flight training",
          "Smallest amounts and shortest terms; a deep resale market keeps it "
          "financeable"],
         ["Turboprop", "Regional charter, utility, cargo",
          "Well understood; values hold reasonably and terms lengthen"],
         ["Light and mid jet", "Corporate and charter",
          "Larger amounts, longer terms, closer scrutiny of the operating plan"],
         ["Helicopter", "Utility, EMS, tour, survey",
          "Underwritten on the contract behind it as much as the airframe"],
         ["Ageing airframes", "Any",
          "Hardest &mdash; term is capped by remaining life, not by your credit"],
     ])
     + "<p>The pattern worth taking from that table is that <strong>resale depth "
       "drives the terms</strong>. A common airframe with an active market "
       "supports a longer term and a higher advance than a rare one of the same "
       "value, because the lender is pricing how quickly it could sell.</p>"),
    ("What Moves the Rate and the Term",
     "<p>Beyond the segment, five things do most of the work:</p>"
     "<ul>"
     "<li><strong>Airframe and engine hours against the overhaul schedule.</strong> "
     "An aircraft approaching a major overhaul carries a known, large cost, and "
     "lenders price it.</li>"
     "<li><strong>Engine programme enrolment.</strong> Being on a maintenance "
     "programme converts a lumpy future cost into a predictable one, which "
     "lenders view favourably.</li>"
     "<li><strong>Damage history.</strong> Disclosed and repaired is workable; "
     "undisclosed and discovered at pre-buy is usually fatal to the deal.</li>"
     "<li><strong>Logbook completeness.</strong> Gaps in the records reduce value "
     "more reliably than most physical faults.</li>"
     "<li><strong>How it will be operated</strong> &mdash; private carriage "
     "against commercial operation changes both the risk and the paperwork.</li>"
     "</ul>"
     "<p>Age matters less than the two things people assume it stands for: "
     "remaining life on the major components, and whether the history is "
     "documented.</p>"),
    ("The Costs That Sit Outside the Loan",
     "<p>Financing covers the aircraft. It does not cover the reason aircraft "
     "ownership surprises first-time buyers, which is that the purchase price is "
     "the beginning of the commitment rather than the end of it.</p>"
     "<ul>"
     "<li><strong>Pre-buy inspection</strong>, paid before you know whether the "
     "deal proceeds</li>"
     "<li><strong>Insurance</strong>, which for a newly-rated pilot in a new type "
     "can be a material annual figure</li>"
     "<li><strong>Hangarage</strong>, fixed whether the aircraft flies or not</li>"
     "<li><strong>Scheduled maintenance and inspections</strong> on a calendar "
     "and hours basis</li>"
     "<li><strong>Reserves for engine and propeller overhaul</strong>, which "
     "accrue whether or not you set the money aside</li>"
     "</ul>"
     "<p>Lenders ask about these because an owner who has not budgeted for them "
     "is a borrower whose aircraft will be deferred-maintenance collateral within "
     "two years. Having credible figures improves the file as well as the "
     "decision.</p>"),
]

# ----------------------------------------------------------------- marine --
PAGES["commercial-marine-financing.html"] = [
    ("How Lenders Read a Commercial Vessel",
     "<p>Vessels are not interchangeable collateral. A lender's comfort comes "
     "from how specific the hull is to one trade, because that determines who "
     "else could buy it.</p>"
     + table(["Vessel type", "Typical work", "Collateral profile"], [
         ["Charter and tour boats", "Passenger day trips, dive, fishing charters",
          "Broad buyer pool; passenger certification adds value"],
         ["Commercial fishing vessels", "Harvest, processing support",
          "Value is tied to permits and quota as much as the hull"],
         ["Workboats and crew boats", "Offshore support, construction",
          "Follows the offshore cycle; contracts matter"],
         ["Tugs and push boats", "Towing, harbour work",
          "Long-lived, specialised, slower to sell"],
         ["Aluminium and small craft", "Patrol, survey, transfer",
          "Liquid, quick to value, smaller amounts"],
     ])
     + "<p>The consequence is that two vessels of equal value do not support "
       "equal loans. A charter boat with passenger certification has many "
       "plausible buyers; a purpose-built tug has few, and the terms reflect "
       "it.</p>"),
    ("Where Permits and Certification Sit in the Value",
     "<p>The feature that makes marine lending different from other equipment "
     "finance: on some vessels, a large part of the value is not the boat.</p>"
     "<p>Fishing permits, licences and quota can be worth a substantial "
     "proportion of a commercial fishing operation, and they are transferable "
     "assets in their own right in many fisheries. A lender financing the vessel "
     "alone may be securing considerably less than the business is worth &mdash; "
     "and one financing the package needs to understand how the permit "
     "transfers, and whether it can.</p>"
     "<p>Passenger certification works similarly on the charter side. A "
     "certificated vessel is worth more than an identical hull without it, "
     "because certification is slow and expensive to obtain.</p>"
     "<p>Bring documentation of any permits, quota or certification to the first "
     "conversation. It changes the arithmetic and it is not something a lender "
     "can infer from the hull.</p>"),
    ("Survey, Documentation and Insurance",
     "<p>Three requirements that reliably decide the timeline:</p>"
     "<ul>"
     "<li><strong>Marine survey.</strong> A condition and valuation survey from "
     "an accredited surveyor is effectively universal above the smallest "
     "amounts. It is the marine equivalent of an appraisal and it drives the "
     "advance.</li>"
     "<li><strong>Documentation.</strong> Federally documented vessels carry a "
     "Certificate of Documentation, and a lender's preferred ship mortgage is "
     "recorded against it. State-titled vessels work differently, and which "
     "applies affects how the lien is perfected.</li>"
     "<li><strong>Insurance.</strong> Hull and protection-and-indemnity cover "
     "with the lender named, bound before funding. Cover for commercial "
     "operation is materially different from recreational cover, and quoting the "
     "wrong one delays closing.</li>"
     "</ul>"
     "<p>Order the survey early. It is the step most likely to find something "
     "that changes the deal, and finding it in week one is an adjustment rather "
     "than a collapse.</p>"),
]

# ------------------------------------------------------------------ drone --
PAGES["drone-financing.html"] = [
    ("What Actually Gets Financed in a Drone Operation",
     "<p>The aircraft is rarely the expensive part. In a commercial drone "
     "business the spend is spread across payload, ground equipment and "
     "software, and lenders treat those very differently.</p>"
     + table(["Component", "Share of a typical build", "Financeable?"], [
         ["Airframe", "Often the smallest line",
          "Yes, but low individual value limits it"],
         ["Payload &mdash; LiDAR, thermal, multispectral", "Frequently the largest",
          "Yes &mdash; high value and identifiable by serial"],
         ["Ground control and RTK base stations", "Moderate", "Sometimes, bundled"],
         ["Batteries and consumables", "Recurring", "No &mdash; treat as operating cost"],
         ["Processing software and licences", "Recurring", "No &mdash; nothing to recover"],
         ["Vehicles and trailers", "Varies", "Yes &mdash; titled and liquid"],
     ])
     + "<p>The practical implication: a lender will look past the drone to the "
       "sensor. A survey-grade LiDAR payload can be worth several times the "
       "aircraft carrying it, and it is the part with a resale market.</p>"),
    ("Why Contracts Matter More Than Kit",
     "<p>Drone equipment depreciates quickly and the resale market is shallow, "
     "which limits how much comfort a lender takes from the hardware alone. What "
     "moves an application is the work behind it.</p>"
     "<p>An operator with recurring inspection contracts &mdash; utility "
     "corridors, cell towers, insurance surveys, construction progress &mdash; "
     "is financing against a revenue stream that happens to require equipment. "
     "An operator buying kit speculatively is asking a lender to take a view on "
     "fast-depreciating hardware and an unproven pipeline.</p>"
     "<p>Bring the contracts. Signed work, or a documented history of repeat "
     "clients, does more for the terms than the specification of the "
     "sensor.</p>"),
    ("Regulatory Standing Is Part of the File",
     "<p>Commercial drone work in the United States operates under FAA Part 107, "
     "and a lender will expect the operation to be properly certificated before "
     "financing equipment for it.</p>"
     "<ul>"
     "<li><strong>Remote pilot certification</strong> for the operators</li>"
     "<li><strong>Aircraft registration</strong> as required</li>"
     "<li><strong>Waivers or authorisations</strong> where the work needs them "
     "&mdash; night operations, beyond visual line of sight, controlled "
     "airspace</li>"
     "<li><strong>Insurance</strong> appropriate to commercial operation, which "
     "is not the same as hobbyist cover</li>"
     "</ul>"
     "<p>The reasoning is straightforward: work that cannot legally be performed "
     "cannot generate the revenue that repays the loan. Where a contract depends "
     "on a waiver, having it in hand is worth more to the file than any "
     "equipment specification.</p>"),
]

# ------------------------------------------------------------ data centre --
PAGES["data-center-financing.html"] = [
    ("Where the Money Goes in a Data Centre Build",
     "<p>Data centre spend divides into categories that finance very "
     "differently, and treating them as one number is why budgets and facilities "
     "so often fail to line up.</p>"
     + table(["Category", "Examples", "How it is usually funded"], [
         ["IT equipment", "Servers, storage, switching",
          "Equipment finance &mdash; identifiable, serialised, resaleable"],
         ["Accelerated compute", "GPU clusters",
          "Equipment finance, but term capped by how fast it obsoletes"],
         ["Power infrastructure", "UPS, switchgear, generators",
          "Long-lived; longer terms, sometimes real-estate-secured"],
         ["Cooling", "CRAC, chillers, containment",
          "Long-lived; often bundled with power"],
         ["Fit-out and civils", "Raised floor, containment, security",
          "Hard to finance alone &mdash; it is improvement, not equipment"],
         ["Colocation commitments", "Contracted rack and power",
          "An operating expense, not an asset"],
     ])
     + "<p>The distinction that matters most: <strong>power and cooling outlive "
       "the compute they support, often by a wide margin.</strong> Financing "
       "them on the same term as servers means either paying for infrastructure "
       "long after the servers are gone, or paying for servers over a term the "
       "hardware will not survive.</p>"),
    ("Matching the Term to the Refresh Cycle",
     "<p>The most consequential structural decision in this category, and the "
     "one most often got wrong.</p>"
     "<p>Compute hardware is refreshed on a cycle measured in a small number of "
     "years, and accelerated compute faster still. Power and cooling "
     "infrastructure lasts a great deal longer. Financing both over an "
     "identical term guarantees a mismatch at one end.</p>"
     "<p>The practical approach is to split the facility: shorter terms on IT "
     "equipment, matched to the refresh you actually plan, and longer terms on "
     "the infrastructure that will still be there through several refreshes. "
     "That produces two facilities rather than one, which is more paperwork and "
     "materially better economics.</p>"
     "<p>It also avoids the position where a refresh is due and the previous "
     "generation is still being paid for &mdash; the point at which growth "
     "stops being fundable from cash flow.</p>"),
    ("What Lenders Ask a Data Centre Operator",
     "<p>Because much of the value is in fast-depreciating hardware, "
     "underwriting leans on the contracts around it:</p>"
     "<ul>"
     "<li><strong>Committed revenue.</strong> Contracted colocation or hosting "
     "revenue against the capacity being built.</li>"
     "<li><strong>Utilisation.</strong> Capacity already sold, against capacity "
     "being added speculatively.</li>"
     "<li><strong>Power availability and cost.</strong> Increasingly the binding "
     "constraint on expansion, and a real underwriting question.</li>"
     "<li><strong>Where the equipment sits.</strong> Kit installed in a "
     "third-party facility is harder to secure and recover than kit in premises "
     "you control.</li>"
     "<li><strong>Customer concentration.</strong> One tenant carrying most of "
     "the revenue is a risk regardless of their credit.</li>"
     "</ul>"
     "<p>Speculative capacity is financeable, but on more conservative terms "
     "than capacity with contracts behind it. If you have committed revenue, "
     "lead with it.</p>"),
]


def deepen(path, sections, apply_changes):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return "MISSING"
    s = io.open(p, encoding="utf-8").read()
    added = [(h, b) for h, b in sections if f'id="{slug(h)}"' not in s]
    if not added:
        return "already deepened"
    m = CTA.search(s)
    if not m:
        return "NO CTA SECTION TO INSERT BEFORE"
    block = "".join(section(h, b) for h, b in added)
    out = s[:m.start()] + block + s[m.start():]
    if apply_changes:
        io.open(p, "w", encoding="utf-8", newline="").write(out)
    return f"+{len(added)} sections"


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for path, secs in PAGES.items():
        print(f"  {path:34} {deepen(path, secs, apply_changes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
