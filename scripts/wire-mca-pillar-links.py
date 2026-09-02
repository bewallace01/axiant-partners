# -*- coding: utf-8 -*-
"""
Priority 0 wiring: give the MCA and debt-relief cluster a contextual link to
whichever of the four MCA pillars actually fits.

37 articles sit under business-debt-relief/articles/ and
merchant-cash-advance/articles/. Ten already linked to a pillar; the other 27
linked to none of them, so four commercial pages were being supported by
nothing but the nav.

Deliberately NOT a "related links" block appended to 27 pages. Each link is a
phrase already in the body, inside a sentence where the pillar is the actual
next step for that reader. The pillar is chosen per article, not by template:

  mca-debt-relief.html           the umbrella - relief options, default,
                                 collections, "what are my paths"
  mca-consolidation-loan.html    consolidation, reverse consolidation,
                                 refinancing advances into one payment
  business-debt-settlement.html  negotiated reductions specifically
  mca-attorney-vs-debt-relief.html  lawyers, lawsuits, judgments, UCC
                                 enforcement, frozen accounts

A keyword score was used to shortlist, then overridden by hand where it was
wrong. It defaulted eight top-of-funnel articles ("how to apply", "what do
lenders look for", "rates 2026") to the attorney pillar because they contain no
distress vocabulary at all. Those readers are shopping for an advance, not
escaping one, so they are anchored instead on the stacking passage each of them
already carries, pointing at the relief umbrella - which is the honest link for
someone about to take a second advance.

Every anchor is matched with flexible whitespace and must occur exactly once
outside an existing <a>. A miss is a hard failure, not a silent skip.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DR = "business-debt-relief/articles"
MCA = "merchant-cash-advance/articles"

# (article dir, pillar, anchor phrase already present in the body)
SPECS = [
    # --- distress: consolidation is the concrete next step -------------------
    (f"{DR}/auto-repair-debt-relief", "mca-consolidation-loan",
     "refinance the advances into one cheaper term loan"),
    (f"{DR}/contractor-debt-relief", "mca-consolidation-loan",
     "refinance the advances into one cheaper term loan"),
    (f"{DR}/landscaping-debt-relief", "mca-consolidation-loan",
     "refinance the advances into one cheaper term loan"),
    (f"{DR}/retail-debt-relief", "mca-consolidation-loan",
     "refinance the advances into one cheaper term loan"),
    (f"{DR}/trucking-debt-relief", "mca-consolidation-loan",
     "refinance the advances into a single cheaper term loan"),
    (f"{MCA}/refinance-mca-to-term-loan-30-day-playbook", "mca-consolidation-loan",
     # the phrase this first pointed at also appears verbatim in the visible
     # FAQ answer, so it matched twice; this one is unique to the body.
     "Run the math before committing"),
    (f"{MCA}/how-to-get-out-of-an-mca", "mca-consolidation-loan",
     "Refinancing replaces daily deductions with a more predictable structure"),
    (f"{MCA}/mca-for-auto-repair-shops", "mca-consolidation-loan",
     "Have a plan to refinance or pay off the advance when cash flow allows"),

    # --- distress: settlement / mediation ------------------------------------
    (f"{DR}/business-debt-mediation", "business-debt-settlement",
     # the obvious sentence has a <strong> inside it, so anchor past the tag
     "the firm handles the negotiation end to end"),
    (f"{DR}/restaurant-debt-relief", "business-debt-settlement",
     "Debt mediation and settlement are performed by independent partner firms"),

    # --- distress: legal escalation ------------------------------------------
    (f"{DR}/can-you-go-to-jail-for-not-paying-mca", "mca-attorney-vs-debt-relief",
     "failing to appear for a court-ordered debtor"),
    (f"{DR}/release-ucc-lien-business", "mca-attorney-vs-debt-relief",
     "you may be able to compel removal"),
    (f"{MCA}/red-flags-mca-agreements", "mca-attorney-vs-debt-relief",
     "lets the MCA provider obtain a legal judgment against you without a normal court process"),

    # --- distress: the relief umbrella ---------------------------------------
    (f"{DR}/glossary", "mca-debt-relief",
     # the body uses curly apostrophes; this fragment avoids them entirely
     "only a business problem"),
    (f"{DR}/how-much-does-business-debt-relief-cost", "mca-debt-relief",
     "two real considerations can affect the true cost of relief"),
    (f"{DR}/stacked-debt-relief-calculator", "mca-debt-relief",
     "the next question is which path gets you there"),
    (f"{DR}/stop-mca-ach-withdrawals", "mca-debt-relief",
     "without defaulting"),
    (f"{DR}/request-mca-reconciliation", "mca-debt-relief",
     "Debt mediation and settlement are performed by independent partner firms"),
    (f"{MCA}/how-to-get-out-of-a-merchant-cash-advance", "mca-consolidation-loan",
     "paying off the advance stops the daily drain immediately"),

    # --- top of funnel: anchored on the stacking passage they already carry ---
    (f"{MCA}/how-much-can-you-qualify-for-merchant-cash-advance", "mca-debt-relief",
     "new advances stack on top"),
    (f"{MCA}/reasons-mca-funding-gets-delayed", "mca-debt-relief",
     "stacking review when existing daily-debit obligations push capacity"),
    (f"{MCA}/typical-merchant-cash-advance-rates-2026", "mca-debt-relief",
     "industry risk, and existing advances"),
    (f"{MCA}/what-do-lenders-look-for-merchant-cash-advance", "mca-debt-relief",
     "multiple stacked advances"),
    (f"{MCA}/mca-for-restaurants", "mca-debt-relief",
     "Stacking MCAs can create a"),
    (f"{MCA}/mca-for-retail-stores", "mca-debt-relief",
     "MCA can be risky for highly seasonal retail"),
    (f"{MCA}/how-to-apply-merchant-cash-advance", "mca-debt-relief",
     "a fixed amount is debited from your bank account each business day"),
    (f"{MCA}/merchant-cash-advance-vs-working-capital-loan", "mca-consolidation-loan",
     "A working capital loan is almost always cheaper"),
]

# The six one-off pillar links from the brief. Three were already wired before
# this ran -- dscr-rental-loans-real-estate-investors already pointed at both
# dscr-loans and dscr-lenders, security-guard-company-working-capital at
# security-guard-business-financing, and bridge-loan-vs-heloc at
# heloc-for-business -- so only the four genuine misses are listed.
ONE_OFFS = [
    ("commercial-real-estate-loans/articles/dscr-loan-vs-conventional-mortgage",
     "dscr-loan-requirements", "rather than your tax returns or DTI"),
    ("equipment-financing/articles/equipment-sale-leaseback-financing",
     "commercial-truck-title-loan",
     ("remaining financing — heavy construction equipment, trucks and trailers",
      "trucks and trailers")),
    ("equipment-financing/articles/equipment-sale-leaseback-financing",
     "equipment-appraisal", "Advance depends on appraisal, condition, and title"),
    ("commercial-real-estate-loans/articles/appraisal-came-in-low-options-to-save-deal",
     "equipment-appraisal", "Appraisals are opinions, not facts"),
]


def phrase_re(anchor):
    """Match the phrase allowing any whitespace run between words."""
    return re.compile(r"\s+".join(re.escape(w) for w in anchor.split()))


def strip_chrome(s):
    """Index ranges that are header/footer/script, so we never link inside them."""
    spans = []
    for pat in (r"<!-- AXIANT-HEADER:START.*?AXIANT-HEADER:END -->",
                r"<!-- AXIANT-FOOTER:START.*?AXIANT-FOOTER:END -->",
                r"<script.*?</script>", r"<head>.*?</head>"):
        for m in re.finditer(pat, s, re.S | re.I):
            spans.append((m.start(), m.end()))
    return spans


def inside(spans, i):
    return any(a <= i < b for a, b in spans)


def in_anchor(s, i):
    """True if position i sits between an <a ...> and its </a>."""
    before = s[:i]
    return before.rfind("<a ") > before.rfind("</a>")


def apply_link(path, pillar, anchor, dry):
    """anchor is either a phrase, or (context, phrase).

    The two-part form exists because the phrase that reads best as link text is
    not always unique. equipment-sale-leaseback-financing names "trucks and
    trailers" in two near-identical paragraphs, and the shortest unique string
    around it, "trucks and trailers, CNC", cuts an enumeration in half -- the
    sentence reads "heavy construction equipment, trucks and trailers, CNC and
    manufacturing machinery", so linking through "CNC" orphans it from the
    "and manufacturing machinery" it belongs to. Context locates the right
    paragraph; only the phrase inside it becomes the link.
    """
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    href = f"/{pillar}.html"
    if href in s:
        return "already linked"
    context, phrase = anchor if isinstance(anchor, tuple) else (anchor, anchor)
    spans = strip_chrome(s)
    hits = [m for m in phrase_re(context).finditer(s)
            if not inside(spans, m.start()) and not in_anchor(s, m.start())]
    if not hits:
        return "ANCHOR NOT FOUND"
    if len(hits) > 1:
        return f"AMBIGUOUS ({len(hits)} matches)"
    m = hits[0]
    if context is phrase:
        start, end = m.start(), m.end()
    else:
        inner = phrase_re(phrase).search(s, m.start(), m.end())
        if not inner:
            return "PHRASE NOT INSIDE CONTEXT"
        start, end = inner.start(), inner.end()
    out = s[:start] + f'<a href="{href}">' + s[start:end] + "</a>" + s[end:]
    if not dry:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(out)
    return f"linked -> {pillar}"


def main(dry):
    print("DRY RUN" if dry else "APPLIED")
    bad = 0
    print("\n-- cluster articles --")
    for art, pillar, anchor in SPECS:
        p = os.path.join(ROOT, art.replace("/", os.sep), "index.html")
        if not os.path.exists(p):
            print(f"  MISSING FILE  {art}")
            bad += 1
            continue
        r = apply_link(p, pillar, anchor, dry)
        flag = "  " if r.startswith("linked") or r == "already linked" else "!!"
        if flag == "!!":
            bad += 1
        print(f"  {flag} {art.split('/')[-1][:52]:<52} {r}")

    print("\n-- one-off pillar links --")
    for art, pillar, anchor in ONE_OFFS:
        p = os.path.join(ROOT, art.replace("/", os.sep), "index.html")
        if not os.path.exists(p):
            print(f"  MISSING FILE  {art}")
            bad += 1
            continue
        r = apply_link(p, pillar, anchor, dry)
        flag = "  " if r.startswith("linked") or r == "already linked" else "!!"
        if flag == "!!":
            bad += 1
        print(f"  {flag} {art.split('/')[-1][:42]:<42} -> {pillar[:27]:<27} {r}")

    print(f"\n  {len(SPECS)} cluster + {len(ONE_OFFS)} one-off   problems: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--apply" not in sys.argv))
