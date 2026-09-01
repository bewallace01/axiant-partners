import csv, zipfile, io
from pathlib import Path
zip_path = Path(r'C:\Users\alexr\Downloads\https___axiantpartners.com_-Performance-on-Search-2026-03-27 (1).zip')
exclude = {
'https://axiantpartners.com/equipment/semi-trucks/how-to-finance-a-semi-truck/',
'https://axiantpartners.com/equipment-financing/articles/equipment-financing-requirements/',
'https://axiantpartners.com/commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/',
'https://axiantpartners.com/business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/',
'https://axiantpartners.com/commercial-bridge-loans.html',
'https://axiantpartners.com/equipment/diagnostic-equipment-auto/scan-tool-financing/',
'https://axiantpartners.com/trucking-business-financing.html',
'https://axiantpartners.com/construction-business-financing/progress-payment-cash-flow-gaps/',
'https://axiantpartners.com/revenue-based-financing/articles/revenue-based-financing-traps/',
'https://axiantpartners.com/sba-loans/articles/sba-loan-restaurant-acquisition/'
}
with zipfile.ZipFile(zip_path) as z:
    data = z.read('Pages.csv').decode('utf-8-sig', errors='ignore')
rows=[]
for r in csv.DictReader(io.StringIO(data)):
    page=(r.get('Top pages') or '').strip()
    if not page or page in exclude:
        continue
    imp=float((r.get('Impressions') or '0').replace(',',''))
    ctr=float((r.get('CTR') or '0').replace('%','').replace(',',''))
    pos=float((r.get('Position') or '999').replace(',',''))
    clicks=float((r.get('Clicks') or '0').replace(',',''))
    if '/articles/' not in page and not page.endswith('.html'):
        continue
    score = imp * (1.3 if 4 <= pos <= 20 else 1.0) * (1.15 if ctr < 1 else 1.0)
    rows.append((score, imp, ctr, pos, clicks, page))
rows.sort(reverse=True)
for i,(_,imp,ctr,pos,clicks,page) in enumerate(rows[:15],1):
    print(f"{i}. {page}\timp={imp:.0f}\tctr={ctr:.2f}%\tpos={pos:.2f}\tclicks={clicks:.0f}")
