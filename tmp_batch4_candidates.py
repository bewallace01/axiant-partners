import csv
import io
import zipfile
from pathlib import Path

zip_path = Path(r"C:\Users\alexr\Downloads\https___axiantpartners.com_-Performance-on-Search-2026-03-27 (1).zip")

exclude = {
    # Batch 1
    "https://axiantpartners.com/equipment/semi-trucks/how-to-finance-a-semi-truck/",
    "https://axiantpartners.com/equipment-financing/articles/equipment-financing-requirements/",
    "https://axiantpartners.com/commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/",
    "https://axiantpartners.com/business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/",
    "https://axiantpartners.com/commercial-bridge-loans.html",
    "https://axiantpartners.com/equipment/diagnostic-equipment-auto/scan-tool-financing/",
    "https://axiantpartners.com/trucking-business-financing.html",
    "https://axiantpartners.com/construction-business-financing/progress-payment-cash-flow-gaps/",
    "https://axiantpartners.com/revenue-based-financing/articles/revenue-based-financing-traps/",
    "https://axiantpartners.com/sba-loans/articles/sba-loan-restaurant-acquisition/",
    # Batch 2
    "https://axiantpartners.com/sba-loans/articles/sba-loan-franchise-acquisition/",
    "https://axiantpartners.com/sba-loans/articles/sba-loan-vs-business-line-of-credit/",
    "https://axiantpartners.com/articles/why-applying-multiple-banks-blindly-hurts-approval-odds/",
    "https://axiantpartners.com/working-capital-loans/articles/working-capital-loan-vs-business-line-of-credit/",
    "https://axiantpartners.com/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/",
    "https://axiantpartners.com/commercial-real-estate-loans/articles/what-do-lenders-look-for-commercial-real-estate-loan/",
    "https://axiantpartners.com/commercial-bridge-loans/articles/commercial-bridge-loan-vs-sba-loan/",
    "https://axiantpartners.com/merchant-cash-advance/articles/mca-for-restaurants/",
    "https://axiantpartners.com/equipment-financing/articles/construction-heavy-equipment-financing/",
    "https://axiantpartners.com/business-term-loans/articles/business-term-loan-requirements/",
    # Batch 3
    "https://axiantpartners.com/business-line-of-credit/articles/business-line-of-credit-for-startups/",
    "https://axiantpartners.com/working-capital-loans/articles/what-credit-score-needed-working-capital-loan/",
    "https://axiantpartners.com/business-term-loans/articles/term-loan-mistakes-cost-thousands/",
    "https://axiantpartners.com/business-term-loans/articles/why-business-term-loan-application-stuck/",
    "https://axiantpartners.com/fix-and-flip/articles/fix-and-flip-loan-out-of-state-investors/",
    "https://axiantpartners.com/commercial-bridge-loans/articles/whats-holding-up-your-bridge-loan-funding/",
    "https://axiantpartners.com/revenue-based-financing/articles/why-revenue-based-financing-advance-lower-than-needed/",
    "https://axiantpartners.com/equipment-financing/articles/restaurant-commercial-kitchen-equipment-financing/",
    "https://axiantpartners.com/revenue-based-financing/articles/why-revenue-based-financing-not-working/",
    "https://axiantpartners.com/fix-and-flip/articles/fix-and-flip-loan-multifamily-properties/",
}

with zipfile.ZipFile(zip_path) as zf:
    data = zf.read("Pages.csv").decode("utf-8-sig", errors="ignore")

rows = []
for row in csv.DictReader(io.StringIO(data)):
    page = (row.get("Top pages") or "").strip()
    if not page or page in exclude:
        continue
    if "/articles/" not in page:
        continue
    impressions = float((row.get("Impressions") or "0").replace(",", ""))
    ctr = float((row.get("CTR") or "0").replace("%", "").replace(",", ""))
    position = float((row.get("Position") or "999").replace(",", ""))
    clicks = float((row.get("Clicks") or "0").replace(",", ""))
    score = impressions * (1.3 if 4 <= position <= 20 else 1.0) * (1.15 if ctr < 1 else 1.0)
    rows.append((score, impressions, ctr, position, clicks, page))

rows.sort(reverse=True)
for i, (_, imp, ctr, pos, clicks, page) in enumerate(rows[:20], 1):
    print(f"{i}. {page}\timp={imp:.0f}\tctr={ctr:.2f}%\tpos={pos:.2f}\tclicks={clicks:.0f}")
