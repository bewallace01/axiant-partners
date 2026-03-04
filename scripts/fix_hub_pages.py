#!/usr/bin/env python3
"""Update *-blog.html hub pages: canonicals to /topic/articles/, links to canonical URLs."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
BASE_URL = "https://www.axiantpartners.com"

# topic slug -> final articles URL
HUBS = {
    "sba-loans-blog": ("/sba-loans/articles/", [
        ("blog/what-do-lenders-look-for-sba-loan-approval.html", "/sba-loans/articles/what-do-lenders-look-for-sba-loan-approval/"),
        ("blog/can-you-use-sba-loan-to-buy-a-business.html", "/sba-loans/articles/can-you-use-sba-loan-to-buy-a-business/"),
        ("blog/sba-loan-vs-business-line-of-credit.html", "/sba-loans/articles/sba-loan-vs-business-line-of-credit/"),
        ("blog/sba-7a-vs-504-loan.html", "/sba-loans/articles/sba-7a-vs-504-loan/"),
        ("blog/what-credit-score-needed-sba-loan.html", "/sba-loans/articles/what-credit-score-needed-sba-loan/"),
        ("blog/how-long-sba-loan-approval.html", "/sba-loans/articles/how-long-sba-loan-approval/"),
        ("blog/how-much-down-payment-required-sba-loan.html", "/sba-loans/articles/how-much-down-payment-required-sba-loan/"),
    ]),
    "equipment-financing-blog": ("/equipment-financing/articles/", [
        ("blog/what-credit-score-needed-equipment-financing.html", "/equipment-financing/articles/what-credit-score-needed-equipment-financing/"),
        ("blog/do-you-need-down-payment-for-equipment-financing.html", "/equipment-financing/articles/do-you-need-down-payment-for-equipment-financing/"),
        ("blog/what-benefits-does-lease-have-equipment-financing.html", "/equipment-financing/articles/what-benefits-does-lease-have-equipment-financing/"),
        ("blog/equipment-leasing-vs-loan-which-is-better.html", "/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/"),
        ("blog/can-you-finance-used-equipment.html", "/equipment-financing/articles/can-you-finance-used-equipment/"),
        ("blog/how-fast-can-equipment-financing-be-approved.html", "/equipment-financing/articles/how-fast-can-equipment-financing-be-approved/"),
        ("blog/what-are-typical-equipment-financing-rates.html", "/equipment-financing/articles/what-are-typical-equipment-financing-rates/"),
        ("blog/what-do-lenders-look-at-equipment-financing-approval.html", "/equipment-financing/articles/what-do-lenders-look-at-equipment-financing-approval/"),
        ("blog/can-equipment-financing-help-build-business-credit.html", "/equipment-financing/articles/can-equipment-financing-help-build-business-credit/"),
        ("blog/how-equipment-financing-works.html", "/equipment-financing/articles/how-equipment-financing-works/"),
    ]),
    "business-line-of-credit-blog": ("/business-line-of-credit/articles/", [
        ("blog/what-are-typical-business-line-of-credit-rates.html", "/business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/"),
        ("blog/business-line-of-credit-vs-term-loan.html", "/business-line-of-credit/articles/business-line-of-credit-vs-term-loan/"),
        ("blog/what-credit-score-needed-business-line-of-credit.html", "/business-line-of-credit/articles/what-credit-score-needed-business-line-of-credit/"),
        ("blog/do-you-need-collateral-business-line-of-credit.html", "/business-line-of-credit/articles/do-you-need-collateral-business-line-of-credit/"),
        ("blog/how-fast-can-you-get-approved-business-line-of-credit.html", "/business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit/"),
        ("blog/what-do-lenders-look-for-business-line-of-credit.html", "/business-line-of-credit/articles/what-do-lenders-look-for-business-line-of-credit/"),
        ("blog/secured-vs-unsecured-business-line-of-credit.html", "/business-line-of-credit/articles/secured-vs-unsecured-business-line-of-credit/"),
    ]),
    "working-capital-loans-blog": ("/working-capital-loans/articles/", [
        ("blog/what-is-working-capital-loan-how-does-it-work.html", "/working-capital-loans/articles/what-is-working-capital-loan-how-does-it-work/"),
        ("blog/working-capital-loan-vs-business-line-of-credit.html", "/working-capital-loans/articles/working-capital-loan-vs-business-line-of-credit/"),
        ("blog/what-credit-score-needed-working-capital-loan.html", "/working-capital-loans/articles/what-credit-score-needed-working-capital-loan/"),
        ("blog/how-fast-can-you-get-working-capital-loan.html", "/working-capital-loans/articles/how-fast-can-you-get-working-capital-loan/"),
        ("blog/what-do-lenders-look-for-working-capital-loan-application.html", "/working-capital-loans/articles/what-do-lenders-look-for-working-capital-loan-application/"),
        ("blog/how-much-can-you-qualify-for-working-capital-loan.html", "/working-capital-loans/articles/how-much-can-you-qualify-for-working-capital-loan/"),
        ("blog/when-is-working-capital-loan-not-right-option.html", "/working-capital-loans/articles/when-is-working-capital-loan-not-right-option/"),
    ]),
    "business-term-loans-blog": ("/business-term-loans/articles/", [
        ("blog/how-much-can-you-qualify-for-business-term-loan.html", "/business-term-loans/articles/how-much-can-you-qualify-for-business-term-loan/"),
        ("blog/secured-vs-unsecured-business-term-loan.html", "/business-term-loans/articles/secured-vs-unsecured-business-term-loan/"),
        ("blog/when-is-business-term-loan-not-right-option.html", "/business-term-loans/articles/when-is-business-term-loan-not-right-option/"),
        ("blog/how-fast-can-you-get-business-term-loan.html", "/business-term-loans/articles/how-fast-can-you-get-business-term-loan/"),
        ("blog/what-credit-score-needed-business-term-loan.html", "/business-term-loans/articles/what-credit-score-needed-business-term-loan/"),
        ("blog/business-term-loan-vs-line-of-credit.html", "/business-term-loans/articles/business-term-loan-vs-line-of-credit/"),
        ("blog/what-do-lenders-look-for-business-term-loan.html", "/business-term-loans/articles/what-do-lenders-look-for-business-term-loan/"),
    ]),
    "commercial-real-estate-loans-blog": ("/commercial-real-estate-loans/articles/", [
        ("blog/cash-out-refinance-commercial-property.html", "/commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/"),
        ("blog/owner-occupied-vs-investment-commercial-property-loan.html", "/commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/"),
        ("blog/sba-504-vs-conventional-commercial-real-estate-loan.html", "/commercial-real-estate-loans/articles/sba-504-vs-conventional-commercial-real-estate-loan/"),
        ("blog/how-long-close-commercial-real-estate-loan.html", "/commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/"),
        ("blog/what-credit-score-needed-commercial-real-estate-loan.html", "/commercial-real-estate-loans/articles/what-credit-score-needed-commercial-real-estate-loan/"),
        ("blog/how-much-down-payment-required-commercial-property-loan.html", "/commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/"),
        ("blog/what-do-lenders-look-for-commercial-real-estate-loan.html", "/commercial-real-estate-loans/articles/what-do-lenders-look-for-commercial-real-estate-loan/"),
    ]),
    "commercial-bridge-loans-blog": ("/commercial-bridge-loans/articles/", [
        ("blog/commercial-bridge-loan-vs-hard-money-loan.html", "/commercial-bridge-loans/articles/commercial-bridge-loan-vs-hard-money-loan/"),
        ("blog/commercial-bridge-loan-vs-sba-loan.html", "/commercial-bridge-loans/articles/commercial-bridge-loan-vs-sba-loan/"),
        ("blog/when-should-you-use-commercial-bridge-loan.html", "/commercial-bridge-loans/articles/when-should-you-use-commercial-bridge-loan/"),
        ("blog/how-fast-can-you-close-commercial-bridge-loan.html", "/commercial-bridge-loans/articles/how-fast-can-you-close-commercial-bridge-loan/"),
        ("blog/what-do-lenders-look-for-commercial-bridge-loan.html", "/commercial-bridge-loans/articles/what-do-lenders-look-for-commercial-bridge-loan/"),
    ]),
    "fix-and-flip-blog": ("/fix-and-flip/articles/", []),  # already redirect page, skip link updates
    "revenue-based-financing-blog": ("/revenue-based-financing/articles/", [
        ("blog/how-fast-can-you-get-revenue-based-financing.html", "/revenue-based-financing/articles/how-fast-can-you-get-revenue-based-financing/"),
        ("blog/how-much-can-you-qualify-for-revenue-based-financing.html", "/revenue-based-financing/articles/how-much-can-you-qualify-for-revenue-based-financing/"),
        ("blog/what-do-lenders-look-for-revenue-based-financing.html", "/revenue-based-financing/articles/what-do-lenders-look-for-revenue-based-financing/"),
        ("blog/what-is-revenue-based-financing-how-does-it-work.html", "/revenue-based-financing/articles/what-is-revenue-based-financing-how-does-it-work/"),
        ("blog/revenue-based-financing-vs-merchant-cash-advance.html", "/revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/"),
        ("blog/what-credit-score-needed-revenue-based-financing.html", "/revenue-based-financing/articles/what-credit-score-needed-revenue-based-financing/"),
    ]),
    "securities-based-lending-blog": ("/securities-based-lending/articles/", [
        ("blog/when-should-you-use-securities-based-lending.html", "/securities-based-lending/articles/when-should-you-use-securities-based-lending/"),
        ("blog/how-does-securities-based-lending-work.html", "/securities-based-lending/articles/how-does-securities-based-lending-work/"),
        ("blog/what-are-the-risks-of-securities-based-lending.html", "/securities-based-lending/articles/what-are-the-risks-of-securities-based-lending/"),
        ("blog/how-much-can-you-borrow-with-securities-based-lending.html", "/securities-based-lending/articles/how-much-can-you-borrow-with-securities-based-lending/"),
    ]),
}

def fix_hub(hub_name, canon_url, link_map):
    p = BASE / f"{hub_name}.html"
    if not p.exists():
        return
    content = p.read_text(encoding="utf-8")
    if "blog-grid" not in content:  # skip redirect-only pages (e.g. fix-and-flip-blog)
        return
    old_canon = f"{BASE_URL}/{hub_name}.html"
    # canonical
    content = re.sub(r'<link\s+rel="canonical"\s+href="[^"]*"', f'<link rel="canonical" href="{BASE_URL}{canon_url}"', content, count=1)
    # og:url
    content = re.sub(r'<meta\s+property="og:url"\s+content="[^"]*"', f'<meta property="og:url" content="{BASE_URL}{canon_url}"', content, count=1)
    # schema url - only in Blog JSON
    content = re.sub(r'"url"\s*:\s*"' + re.escape(old_canon) + r'"', f'"url":"{BASE_URL}{canon_url}"', content, count=1)
    # blog links
    for old, new in link_map:
        content = content.replace(f'href="{old}"', f'href="{new}"')
    p.write_text(content, encoding="utf-8")
    print(f"Fixed {hub_name}.html")

def main():
    for hub_name, (canon_url, link_map) in HUBS.items():
        fix_hub(hub_name, canon_url, link_map)

if __name__ == "__main__":
    main()
