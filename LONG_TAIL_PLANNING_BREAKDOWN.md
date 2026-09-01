# Axiant Partners – Complete Long-Tail Planning Breakdown

*Share this document with ChatGPT to plan your next long-tail content pages.*

---

## 1. Site Overview

**Business:** Axiant Partners – Business financing matchmaker (SBA loans, equipment financing, working capital, etc.)  
**Domain:** https://axiantpartners.com  
**Tech:** Static HTML/CSS/JS, deployed on Netlify via GitHub

---

## 2. Page Types & URL Patterns

| Content Type | URL Pattern | Example |
|--------------|-------------|---------|
| **Equipment category index** | `/equipment/[slug]/` | `/equipment/backhoes/` |
| **Equipment how-to (long-tail)** | `/equipment/[slug]/how-to-finance-[thing]/` | `/equipment/backhoes/how-to-finance-a-backhoe/` |
| **Industry page** | `/[industry]-business-financing.html` | `/construction-business-financing.html` |
| **Service article hub** | `/[service]/articles/` | `/equipment-financing/articles/` |
| **Service article** | `/[service]/articles/[slug]/` | `/equipment-financing/articles/how-fast-can-equipment-financing-be-approved/` |

**Equipment how-to slug conventions:**
- Singular: `how-to-finance-a-backhoe`, `how-to-finance-a-semi-truck`
- Plural/group: `how-to-finance-restaurant-refrigeration`, `how-to-finance-pallet-racking`
- Custom: `how-to-finance-a-lathe-or-mill`, `how-to-finance-press-brake-equipment`

---

## 3. Existing Content Inventory

### Main Pages (root)
- `index.html` – Homepage (About)
- `match.html` – Primary CTA / lender matching
- `services.html`, `equipment.html`, `industries.html`
- `calculator.html`, `contact.html`, `faq.html`, `referral.html`
- `blog.html` – Articles hub
- Legal: `privacy-policy.html`, `terms-and-conditions.html`, `vendors.html`

### Service Pages (11)
- `sba-loans.html`, `equipment-financing.html`, `equipment.html`
- `business-line-of-credit.html`, `working-capital-loans.html`, `business-term-loans.html`
- `commercial-real-estate-loans.html`, `commercial-bridge-loans.html`, `fix-and-flip.html`
- `revenue-based-financing.html`, `securities-based-lending.html`

### Industry Pages (10)
| Industry | Path |
|----------|------|
| Construction | `construction-business-financing.html` |
| Trucking | `trucking-business-financing.html` |
| Agriculture | `agriculture-business-financing.html` |
| Forestry | `forestry-business-financing.html` |
| Landscaping | `landscaping-business-financing.html` |
| Manufacturing | `manufacturing-business-financing.html` |
| Medical Practices | `medical-practices-business-financing.html` |
| Restaurants | `restaurants-business-financing.html` |
| Auto Repair | `auto-repair-business-financing.html` |
| Logistics & Warehousing | `logistics-warehousing-business-financing.html` |

### Equipment How-To Pages (43 total)

| Category | Equipment Types |
|----------|-----------------|
| **Construction (7)** | Excavators, wheel loaders, mini excavators, backhoes, bulldozers, skid steers, stump grinders |
| **Trucks (10)** | Semi-trucks, box trucks, dump trucks, log trucks, flatbed trucks, tanker trucks, refrigerated trucks, bucket trucks, trailers |
| **Agriculture (5)** | Tractors, combines, hay balers, sprayers, grain equipment |
| **Landscaping (3)** | Zero-turn mowers, commercial mowers, landscape trailers |
| **Manufacturing (5)** | CNC machines, lathes & milling, press brakes, injection molding, industrial robots |
| **Logistics (6)** | Forklifts, pallet jacks, pallet racking, conveyors, dock equipment, scanning & WMS |
| **Auto Repair (6)** | Auto lifts, diagnostic equipment, tire changers, alignment racks, brake & rotor, shop tools & storage |
| **Medical (6)** | Medical imaging, dental, exam & procedure, lab, surgical, diagnostic devices |
| **Restaurant (6)** | Commercial kitchen, refrigeration, POS, dishwashers, prep equipment, ventilation & hood systems |

**Full equipment URLs (examples):**
- `/equipment/excavators/how-to-finance-an-excavator/`
- `/equipment/semi-trucks/how-to-finance-a-semi-truck/`
- `/equipment/forklifts/how-to-finance-a-forklift/`
- `/equipment/dental-equipment/how-to-finance-dental-equipment/`
- *(… 39 more – see equipment hub at `/equipment.html`)*

### Service Articles (by hub)
| Hub | Article Count | Example Articles |
|-----|---------------|------------------|
| SBA Loans | ~6 | How long SBA approval, credit score, collateral |
| Equipment Financing | 10 | Credit score, used equipment, rates, approval speed, loan vs lease |
| Business Line of Credit | ~7 | Credit score, rates, approval time |
| Working Capital | ~6 | Credit score, qualify amount, speed |
| Business Term Loans | ~6 | When not right, speed, qualify amount |
| Commercial Real Estate | ~7 | Cash-out, down payment, credit score |
| Commercial Bridge | ~5 | Speed, when to use |
| Fix and Flip | ~8 | ARV, LTV, rates, speed |
| Revenue-Based Financing | ~6 | Credit score, qualify, lenders |
| Securities-Based Lending | ~4 | Risks, how much |

---

## 4. Content Templates

### Equipment How-To Page (de facto template)

**Head structure:**
- Meta: description, canonical, og:title, og:description, og:image, twitter:card, Article schema, BreadcrumbList, FAQPage, HowTo

**Body structure:**
- H1: "How to Finance a [Thing]"
- Tagline (costs, options, requirements)
- Back link: "Back to Equipment by Type" → `/equipment.html`
- Lead paragraph with links to `equipment-financing.html`, `sba-loans.html`
- Hero image (topic-visual-compact)
- H2 sections: What Is It? | How Do You Finance? | How Much Does It Cost? | Financing Options | Credit & Approval | Related Equipment
- FAQ schema (4–5 Q&As)
- HowTo schema (4–5 steps)
- Related equipment links (3–5)
- Industry links (1–2)
- CTA → `/match.html`

**Typical sections:**
- What Is [Equipment]?
- How Do You Finance [Equipment]?
- How Much Does [Equipment] Cost? (new/used, factors)
- Financing Options (loans, leases, SBA, working capital)
- Credit Score & Approval
- Related Equipment (links to sibling how-tos)

### Industry Page (INDUSTRY-PAGE-TEMPLATE.md)

**Sections:**
1. Industry Overview (H2) – 2–3 paragraphs, operational costs, cash flow
2. How [Industry] Uses Financing (H2)
3. [Industry] Business Financing Options (H2) – table: Financing Option | Best For | CTA link
4. Common [Industry] Equipment That Businesses Finance (H2) – 5–8 equipment items with image, description, link
5. Equipment Financing Guides for [Industry] (H2) – 4–6 links to equipment-financing articles
6. Apply for [Industry] Financing (H2) – CTA

**SEO:** H1 = "[Industry] Business Financing", 1200–1800 words, avoid cannibalizing product pages.

### Service Article (BLOG_POST_TEMPLATE.md)

**Fields:** SLUG, DATE, PRIMARY_TOPIC, POST_TITLE_H1, POST_TAGLINE, TARGET_KEYWORD, SEARCH_INTENT, META_TITLE_DRAFT, META_DESCRIPTION_DRAFT, CTA_BUTTON_URL, BACK_LINK, SERVICE_PAGE_URL, RELATED_ARTICLE_URL

**Body:** H1 → Tagline → Lead → H2 sections → H2 Final Thoughts + service link

**SEO:** 45–65 char title, 120–155 char meta description, keyword in H1, first paragraph, one H2

---

## 5. Identified Gaps & Opportunities

### Industry Gap
- **Cleaning Companies** – Listed in INDUSTRY-PAGE-TEMPLATE.md but no `cleaning-business-financing.html` exists.

### Equipment Gaps (potential new long-tail)
- **Cleaning equipment:** Floor scrubbers, carpet extractors, pressure washers, commercial vacuums, sweepers
- **Other verticals:** No dedicated cleaning, janitorial, or facility-services equipment

### Equipment Subtype Opportunities
- "How to finance a crawler excavator" vs "wheel excavator"
- "How to finance a 3-axis CNC" vs "5-axis CNC"
- "How to finance a class 8 semi" vs "class 6 truck"
- "How to finance used [equipment]" – some general content exists; could add per-equipment variants

### Service Article Gaps
- Each service hub could have more "what credit score," "how fast," "what do lenders look for" variants
- Comparison articles: "SBA vs equipment loan for [use case]"
- Industry-specific service articles: "SBA loans for construction contractors"

### Cross-Linking Opportunities
- Industry pages ↔ equipment pages (partially done)
- Equipment pages ↔ service articles (done)
- New: industry + equipment combo pages or sections

---

## 6. Internal Linking Rules

**Equipment how-to:**
- Back: Equipment hub (`/equipment.html`)
- In-body: `equipment-financing.html`, `sba-loans.html`, relevant equipment-financing articles
- Related: 3–5 equipment how-to links
- Industry: 1–2 industry page links
- CTA: `/match.html`

**Industry page:**
- In-body: equipment-financing, sba-loans, working-capital, business-line-of-credit, commercial-real-estate
- Equipment: 5–8 links in "Common Equipment" section
- Guides: 4–6 equipment-financing article links
- CTA: `/match.html`

**Service article:**
- Back: Hub (e.g. `../` or `../index.html`)
- In-body: Primary service page, one related article
- Related Resources block: service page, hub, related article, `/match.html`

---

## 7. Schema & SEO

- **Equipment how-to:** BreadcrumbList, Article, FAQPage, HowTo
- **Industry page:** FinancialService
- **Canonical:** All pages have `rel="canonical"`
- **Sitemap:** `sitemap.xml` – add new URLs when creating pages
- **Note:** `industries.html` is not in sitemap (per SEO_REVIEW.md)

---

## 8. File Paths for New Content

| Content Type | Create |
|--------------|--------|
| Equipment how-to | `equipment/[category]/how-to-finance-[thing]/index.html` |
| Equipment category | `equipment/[category]/index.html` |
| Industry page | `[industry]-business-financing.html` (root) |
| Service article | `[service]/articles/[slug]/index.html` |

**Asset path for equipment images:** `assets/[slug]-equipment.png` (e.g. `assets/backhoe-equipment.png`)

---

## 9. Suggested Long-Tail Priorities

1. **Cleaning Companies** – Industry page + cleaning equipment (floor scrubbers, carpet extractors, pressure washers, vacuums, sweepers)
2. **Equipment subtypes** – Crawler vs wheel excavator, 3-axis vs 5-axis CNC, used-equipment guides per type
3. **Service article expansion** – More "how fast," "what credit score," "what do lenders look for" per service
4. **Industry + service combos** – "SBA loans for construction," "Equipment financing for restaurants" (partly covered by industry pages)
5. **Comparison pages** – "Equipment loan vs lease for [equipment type]" (some content in articles; could expand)

---

## 10. Summary for ChatGPT

When planning new long-tail pages for Axiant Partners:

- **Equipment pages:** Use `/equipment/[category]/how-to-finance-[thing]/` pattern. Include: costs (new/used), financing options (loans, leases, SBA), credit/approval, related equipment, industry links. Add FAQ and HowTo schema.
- **Industry pages:** Follow INDUSTRY-PAGE-TEMPLATE.md. Main gap: Cleaning Companies.
- **Service articles:** Follow BLOG_POST_TEMPLATE.md. Each service hub can support more "how to," "what," "when" articles.
- **Internal links:** Always link to equipment-financing, match.html, related equipment/industry pages.
- **Add new URLs to sitemap.xml** when publishing.
