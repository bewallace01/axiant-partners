# Work Log

A running, timestamped log of what shipped — appended automatically on every commit.

## 2026-06-30
- 16:31 — SEO/AEO: build automotive-business-loans hub + fix FAQ schema + speakable (`7ca4fac36`) — Alex Solopenkov
- 17:15 — SEO: SBA pillar gains CAPLines (lines of credit) + 504-vs-7a variant FAQ (`c0477b0b3`) — Alex Solopenkov

## 2026-07-01
- 11:04 — SEO(growth): GEO dateModified, sitemap + orphan fix, internal links to weak pages (`f7bd2351b`) — Alex
- 11:10 — SEO(GEO): add dateModified to 8 startup-financing article schemas (`a810bda29`) — Alex
- 11:17 — audit: stop over-flagging FAQ/thin/stale on non-content pages (`d15a0ec9f`) — Alex
- 11:30 — SEO(GEO): add dateModified to vendors.html (`039043ec1`) — Alex

## 2026-07-02
- 10:39 — feat(seo): business acquisition financing roll-up hub (`854743e08`) — Alex
- 13:28 — feat(mca-calc): cityscape background + 'How it works' popup button (`69fdd74f1`) — Alex
- 13:39 — feat(nav): Calculator becomes a dropdown (Loan / MCA / DSCR) (`b1349ac4c`) — Alex
- 13:57 — fix(sw): network-first for scripts so JS updates appear on next load (`535d628a1`) — Alex
- 14:07 — feat(mca-calc): merge Embed into a wide two-column How it works / Embed popup (`49f1f4500`) — Alex
- 14:19 — fix(mca-calc): keep the floating button fixed while scrolling (`a1fbd0eb9`) — Alex
- 14:32 — chore(cache): bump language-switcher.js ?v to 202607021 (force fresh nav JS) (`9b73b580e`) — Alex
- 14:33 — chore: keep WORKLOG.md unchanged on main (exclude WIP from cache-bump commit) (`fbf621e65`) — Alex

## 2026-07-09
- 10:14 — Add Restaurant Equipment World partner to /equipment-for-sale/ (`5c1d1cfff`) — Alex Solopenkov
- 10:54 — Add internal links from restaurant financing pages to REW equipment listings (`37e9c0a93`) — Alex Solopenkov
- 12:18 — Improve REW equipment pages: FAQ+schema, payment estimator, equipment-tagged CTA (`6a46e2052`) — Alex Solopenkov

## 2026-07-14
- 09:56 — Add SENNEBOGEN as partner #5 on /equipment-for-sale/ (`84d9324af`) — Alex Solopenkov
- 10:41 — Fix invisible SENNEBOGEN logo: use their official white-on-green lockup (`35e27c926`) — Alex Solopenkov

## 2026-09-02
- 10:24 — Stop the sitemap contradicting the pages it points at (`e66e4ed85`) — Alex Solopenkov
- 10:28 — Self-host the fonts, and stop faking bold on the v1 pages (`abb6d8c55`) — Alex Solopenkov
- 10:38 — Stop shipping 91 KB of legacy JS to 761 pages that do not use it (`a8c891fde`) — Alex Solopenkov
- 10:42 — Give the pages that rank and never get clicked something to cite (`dac81683b`) — Alex Solopenkov
- 10:51 — Log the four commits in WORKLOG (`734ff7c5c`) — Alex Solopenkov
- 11:08 — Stop the article engine backdating every page it generates to 27 May (`d42364b4a`) — Alex Solopenkov
- 11:18 — Wire the MCA cluster to its four pillars (Priority 0) (`b515088e1`) — Alex Solopenkov
- 11:40 — Fix three ways the converter lost content, then convert the DSCR group (`b6b9a69e0`) — Alex Solopenkov
- 11:56 — Add the image ingest pipeline, so generated art becomes shipped WebP in one command (`a55ac4fbf`) — Claude
- 12:01 — DSCR cluster: the hub and the first three articles (`6a8fdef5a`) — Alex Solopenkov
- 12:12 — Build the first 27 generated images into WebP assets (`96c0cdbfd`) — Claude
- 12:13 — DSCR cluster: articles 4-14, completing the fourteen (`35fc2baed`) — Alex Solopenkov
- 12:32 — Give the 37 legacy-body pages the v2 look, without touching their markup (`aa5336b3f`) — Alex Solopenkov
- 12:42 — Fix the quick answer rendering light-on-light, and version the new sheet (`d777d5e11`) — Alex Solopenkov
- 12:51 — Place the generated images, and make every asset actually WebP (`46f90f0b6`) — Alex Solopenkov
- 13:01 — Asset equity 1 of 3: the truck title cluster, 8 articles (`9b6c98c58`) — Alex Solopenkov
- 13:12 — Asset equity 2 and 3 of 3: real-estate-secured and HELOC, 11 articles (`55c1a3a3a`) — Alex Solopenkov
- 13:17 — Equipment appraisal cluster, 5 articles (`bdc765d16`) — Alex Solopenkov
- 13:32 — Security guard cluster, 4 articles, and register the pillar in INDUSTRIES (`6f7e14353`) — Alex Solopenkov
- 13:39 — Deepen the four thin vertical pillars before building their clusters (`8764b2573`) — Alex Solopenkov
- 14:05 — Sweep British spellings out of the site copy (`bfb63e48a`) — Alex Solopenkov
- 14:05 — Four thin-vertical clusters: aircraft, marine, drone, data center (`4eeba0f70`) — Alex Solopenkov
- 14:06 — Link every cluster pillar down to its own articles (`e5affd34b`) — Alex Solopenkov
- 14:22 — Make the speakable schema on 613 pages resolve to something (`f0ce0de74`) — Alex Solopenkov
- 14:28 — Titles inside the SERP cut, and a dateModified on every indexable page (`6b9be0869`) — Alex Solopenkov
- 14:31 — Put all nine clusters on the map assistants actually read (`d6bbe0469`) — Alex Solopenkov
- 14:44 — Show the update date on the pillars, and fix the callout it exposed (`335ac6298`) — Alex Solopenkov
- 14:49 — Write the image brief and close out the daily report (`dc431c926`) — Alex Solopenkov
- 15:00 — Cite federal sources on the two DSCR articles that had none (`f2c310f65`) — Alex Solopenkov

## 2026-09-02
- 15:16 — Log the DSCR sources commit in WORKLOG (`13d691903`) — Alex Solopenkov
- 15:37 — Stop the body fade animation breaking position:fixed site-wide (`c3d609518`) — Alex Solopenkov

## 2026-09-02
- 15:55 — Stop the v2 body sheet overriding pages that already own their styling (`cfafc31e7`) — Alex Solopenkov

## 2026-09-02
- 16:10 — Put the hybrid pillar pages in the same content column as the rest of the site (`9a575a8f5`) — Alex Solopenkov

## 2026-09-02
- 16:32 — v2 contract: the 17 generated catalog pages, and two canonicals (`ede1d8988`) — Alex Solopenkov
- 17:14 — Convert the last 14 legacy pages onto the v2 design system (`ff76235b8`) — Alex Solopenkov
- 17:20 — Stop the hero background painting over the hero photograph (`df517ab5f`) — Alex Solopenkov
- 17:25 — Give the 14 converted pages a cache-buster on axiant-v2.css (`53351c59f`) — Alex Solopenkov
- 17:28 — Revert the hero :has() rule - it broke every page it was meant to help (`d4c88d02a`) — Alex Solopenkov
- 17:36 — Paint hero and band media at positive z-index, not below zero (`8989b898a`) — Alex Solopenkov
- 17:49 — Send /program/ to the program page, not to its articles hub (`558d18313`) — Alex Solopenkov
- 18:25 — Put the breadcrumb, dateline and quick answer inside the content column (`ee6fa1b93`) — Alex Solopenkov
- 19:57 — Convert the tool and article pages to the v2 design system (`1ca5fcdf3`) — Alex Solopenkov

## 2026-09-03
- 11:48 — Let the form-page hero images run the full width of the page (`3f0d7c451`) — Alex
- 14:15 — Fix the quick-answer contrast regression, one tone per section, 113 aside photos (`4dcd0fb13`) — Alex
- 14:27 — Bump the axiant-v2.css cache-bust so the contrast fix actually reaches people (`a712494f7`) — Alex
- 15:35 — Give each aside slot its own photo where a page repeated one (`e591aed6c`) — Alex
- 15:48 — Cache-bust the 36 replaced aside photos so the de-duplication is visible (`b8919375f`) — Alex
