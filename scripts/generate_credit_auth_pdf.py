"""One-off: build Credit Authorization & Broker Disclosure PDF (logo + body)."""
from __future__ import annotations

from pathlib import Path

from fpdf import FPDF

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore[misc, assignment]

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "logo-horizontal-transparent.png"
OUT = ROOT / "forms" / "credit-authorization-broker-disclosure.pdf"


class Doc(FPDF):
    def __init__(self) -> None:
        super().__init__(format="letter", unit="mm")
        self.set_margins(left=18, top=18, right=18)
        self.set_auto_page_break(auto=True, margin=18)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    pdf = Doc()
    pdf.add_page()

    # Centered logo (width in mm; height from image aspect ratio)
    logo_w_mm = 88.0
    x_logo = (pdf.w - logo_w_mm) / 2
    y_logo = 12.0
    if Image is not None:
        with Image.open(LOGO) as im:
            pw, ph = im.size
        logo_h_mm = logo_w_mm * (ph / pw)
    else:
        logo_h_mm = logo_w_mm * (74 / 180)
    pdf.image(str(LOGO), x=x_logo, y=y_logo, w=logo_w_mm)
    pdf.set_y(y_logo + logo_h_mm + 6)

    pdf.set_font("Helvetica", "B", 13)
    pdf.multi_cell(0, 6, "CREDIT AUTHORIZATION & BROKER DISCLOSURE", align="C")
    pdf.ln(1)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5, "Axiant Partners | Axiant LLC", align="C")
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "APPLICANT INFORMATION", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)

    fields = [
        "Full Legal Name:",
        "Residential Address:",
        "City, State, Zip:",
        "Social Security Number (SSN):",
        "Date of Birth (DOB):",
    ]
    for label in fields:
        pdf.cell(0, 5, label, new_x="LMARGIN", new_y="NEXT")
        pdf.cell(0, 0, "_" * 72, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(4)

    pdf.ln(3)

    sections: list[tuple[str, str]] = [
        (
            "1. AUTHORIZATION TO OBTAIN CREDIT REPORTS",
            'The undersigned applicant ("Applicant") certifies that all information provided in this business credit application is true and accurate. Applicant authorizes Axiant LLC d/b/a Axiant Partners, its affiliates, and service providers to obtain consumer and business credit reports and other investigative information from credit reporting agencies to evaluate this application.',
        ),
        (
            "2. MULTI-LENDER & BROKER DISCLOSURE",
            "Applicant acknowledges that Axiant Partners acts as a financing broker. Applicant explicitly authorizes Axiant Partners to share this application and associated credit/financial data with multiple third-party lending institutions, funding partners, and banks within its network to identify potential commercial financing options.",
        ),
        (
            "3. CONSENT TO INQUIRIES & COMMUNICATION",
            'Applicant understands that credit inquiries may include both "soft" and "hard" pulls, which may impact credit scores. Applicant consents to receive communications regarding this application from Axiant Partners and its lending partners via phone, email, and SMS.',
        ),
        (
            "4. COMMERCIAL USE ONLY",
            "Applicant certifies that any financing sought is solely for commercial or business purposes and not for personal, family, or household use. Submission of this application does not constitute an offer or approval of credit.",
        ),
    ]

    for title, body in sections:
        pdf.set_font("Helvetica", "B", 10)
        pdf.multi_cell(0, 5, title)
        pdf.ln(1)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 5, body)
        pdf.ln(4)

    pdf.ln(6)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(90, 5, "Signature of Authorized Signer: ____________________________")
    pdf.cell(0, 5, "Date: ___________", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.cell(0, 5, "Printed Name: __________________________________________", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.cell(0, 5, "Title: ____________", new_x="LMARGIN", new_y="NEXT")

    pdf.output(str(OUT))
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
