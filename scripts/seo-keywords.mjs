// DataForSEO keyword research helper for Axiant SEO.
// Credentials live in _analysis/dataforseo.creds.json (gitignored) — never hardcoded.
//
// Usage:
//   node scripts/seo-keywords.mjs --test                      # check auth + account balance (free)
//   node scripts/seo-keywords.mjs --volume "kw one, kw two"   # search volume + CPC + competition
//   node scripts/seo-keywords.mjs --ideas "seed keyword"      # related keyword opportunities w/ volume
//
// US English by default (location_code 2840, language_code "en").

import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const creds = JSON.parse(readFileSync(join(ROOT, "_analysis", "dataforseo.creds.json"), "utf8"));
const AUTH = "Basic " + Buffer.from(`${creds.login}:${creds.password}`).toString("base64");
const BASE = "https://api.dataforseo.com/v3";
const LOC = 2840, LANG = "en"; // United States, English
const OUR_DOMAIN = "axiantpartners.com";
// Known competitors we explicitly track (in addition to DataForSEO's auto-detected ones).
// These are domains we know compete with us / pull strong traffic. Edit freely.
const KNOWN_COMPETITORS = [
  "midamericacommerciallending.com",
  "lendio.com",
  "swoopfunding.com",
  "crestmontcapital.com",
  "unitedcapitalsource.com",
];

// Every Axiant-network landing site exists to drive financing applications, so a keyword is
// only "on-purpose" if it touches money/credit/funding. Shared funding-intent filter.
const FUNDING_REL = /(\bloans?\b|financ|lend(er|ing)?|funding|\bfunds?\b|capital|working.?capital|merchant cash|cash advance|invoice factor|factoring|receivable|\bsba\b|line of credit|\bloc\b|term loan|\bmca\b|leas(e|ing)|equipment financ|debt (relief|consolidat|settlement|refinanc|payoff)|refinanc|bridge loan|acquisition (loan|financ)|hard money|underwrit|business credit|credit line|broker|referral|\biso\b|commission|white.?label)/i;

// Off-purpose finance these are NOT for: consumer lending, big-bank brands, and regulatory/markets
// noise that lender competitors rank for. Stripped from every landing site's keyword + gap lists.
const FUNDING_EXCLUDE = /(student loan|education loan|home loan|mortgage|reverse mortgage|refinance home|home equity|\bheloc\b|personal loan|\bcar loan|\bauto loan|auto financ|auto refinanc|automobile|\bcar financ|financ\w* (a |new |your )car|\bcar (loan|calculator|estimat)|financ\w* (a |new |your )vehicle|vehicle (loan|calculator)|credit card|capital one|chase\b|wells fargo|bank of america|navy federal|discover\b|securities and exchange|\bsec\b|volatility|stock market|\bforex\b|crypto|payday|\bfha\b|\bva loan|\busda\b|debt to income|credit score|credit karma|fico)/i;

// Per-domain vertical terms — what each landing page is topically about. A keyword is relevant
// to a site if it touches funding OR the vertical; gap (build) targets must touch BOTH so we
// never recommend off-topic operations/software keywords the auto-competitors drag in.
// jyni.io is NOT a financing site. JYNI is an AI-run CRM & lead-generation platform (SaaS),
// sold to businesses that want a CRM + to generate/work their own leads. Its real target market
// is software buyers (crm software, lead generation software, sales automation, AI SDR), NOT the
// financing/broker terms its legacy content cluster happens to rank for. These filters keep the
// product-relevant keywords and gap it against SaaS CRM/lead-gen competitors instead of lenders.
const JYNI_REL = /(\bcrm\b|customer relationship management|lead gen|lead generation|\bleads?\b|sales (software|tool|automation|engagement|pipeline|platform|outreach|prospect|crm|rep|team)|cold (email|outreach|call)|email (outreach|sequenc|campaign|automation)|outreach (software|tool|platform|automation)|prospect(ing|or)|\bsdr\b|appointment setting|dialer|contact management|deal (pipeline|management|tracking)|pipeline (software|management|crm)|drip campaign|marketing automation|ai (crm|sdr|sales|lead|outreach|assistant|agent|email|chatbot)|find (customers|clients|leads)|lead (capture|management|nurtur|scoring|enrichment|database|list|provider)|business development|sales engagement)/i;
const JYNI_EXCLUDE = /(\bloan|financ(e|ing)|lend(er|ing)|funding|\bfund\b|\bsba\b|merchant cash|cash advance|\bcapital\b|working.?capital|invoice factor|factoring|receivable|\bbroker|\bmca\b|debt (relief|consolidat|settlement|payoff)|underwrit|line of credit|term loan|mortgage|equipment financ|hard money|bridge loan|credit score|credit card|credit repair)/i;
const JYNI_COMPETITORS = [
  "hubspot.com",
  "apollo.io",
  "instantly.ai",
  "clay.com",
  "pipedrive.com",
  "close.com",
  "gohighlevel.com",
  "smartlead.ai",
  "lemlist.com",
  "zoho.com",
];

const SITE_VERTICALS = {
  "therestaurantownersguide.com": /(restaurant|food.?service|food truck|caf[eé]|catering|\bbar\b|brewery|hospitality|kitchen|diner|bakery|food &)/i,
  "contractorcapitalguide.com": /(contractor|construction|builder|roofing|hvac|plumb|electric|remodel|landscap|concrete|excavat|\btrade\b|subcontractor)/i,
  "commercialvehicleguide.com": /(truck|trucking|fleet|semi|commercial vehicle|box truck|tractor|trailer|hauling|freight|owner.?operator|\bcdl\b|dump truck|reefer)/i,
  "equipmentfinancehub.com": /(equipment|machinery|machine|excavator|forklift|\bcnc\b|manufacturing|heavy equipment|construction equipment|skid steer|backhoe)/i,
  "businessdebtreliefgroup.com": /(debt|consolidat|settlement|relief|creditor|\bowe\b|payoff|collections|restructur)/i,
  "commercialfinancereferrals.com": /(referral|broker|\biso\b|partner|commission|white.?label|\bagent\b|refer )/i,
};

async function df(path, body, method = "POST") {
  const res = await fetch(BASE + path, {
    method,
    headers: { Authorization: AUTH, "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : undefined,
  });
  const json = await res.json();
  if (json.status_code !== 20000) throw new Error(`API ${json.status_code}: ${json.status_message}`);
  return json;
}

async function test() {
  const j = await df("/appendix/user_data", null, "GET");
  const r = j.tasks?.[0]?.result?.[0] || {};
  console.log("✓ DataForSEO connected as", r.login || creds.login);
  if (r.money) console.log(`  balance: $${r.money.balance} ${r.money.currency || ""}`);
  if (r.rates) console.log(`  limits: ${r.rates.limits_minute || "?"}/min`);
  console.log(`  account: ${r.price ? "live" : JSON.stringify(r).slice(0,120)}`);
}

async function volume(kwCsv) {
  const keywords = kwCsv.split(",").map(s => s.trim()).filter(Boolean).slice(0, 1000);
  const j = await df("/keywords_data/google_ads/search_volume/live", [
    { keywords, location_code: LOC, language_code: LANG },
  ]);
  const rows = (j.tasks?.[0]?.result || []).map(r => ({
    keyword: r.keyword, volume: r.search_volume, cpc: r.cpc,
    competition: r.competition, comp_index: r.competition_index,
  })).sort((a, b) => (b.volume || 0) - (a.volume || 0));
  console.log("keyword | monthly volume | cpc | competition");
  rows.forEach(r => console.log(`${r.keyword} | ${r.volume ?? "—"} | $${r.cpc ?? "—"} | ${r.competition ?? "—"}`));
  console.log(`\n(${rows.length} keywords · cost: $${j.cost ?? "?"})`);
}

// keyword_suggestions: long-tail keywords that CONTAIN the seed phrase — the
// relevant "what else could this page rank for" set (vs keyword_ideas, which drifts).
async function ideas(seed) {
  const j = await df("/dataforseo_labs/google/keyword_suggestions/live", [
    { keyword: seed, location_code: LOC, language_code: LANG, limit: 40,
      order_by: ["keyword_info.search_volume,desc"] },
  ]);
  const items = j.tasks?.[0]?.result?.[0]?.items || [];
  console.log(`\n--- KEYWORD OPPORTUNITIES (contain "${seed}") ---`);
  console.log("keyword | volume | difficulty | cpc");
  items.forEach(it => {
    const ki = it.keyword_info || {};
    const kd = it.keyword_properties?.keyword_difficulty;
    console.log(`${it.keyword} | ${ki.search_volume ?? "—"} | ${kd ?? "—"} | $${ki.cpc ?? "—"}`);
  });
  console.log(`(${items.length} suggestions · cost: $${j.cost ?? "?"})`);
}

// --page: full one-page report. Pulls the page's own ranking queries from GSC,
// then (live) fetches volume + difficulty for them and idea opportunities for the seed.
async function page(seed, dry) {
  const gsc = JSON.parse(readFileSync(join(ROOT, "_analysis", "gsc.json"), "utf8"));
  const tokens = seed.toLowerCase().split(/\s+/).filter(w => w.length > 3);
  const related = gsc.queries
    .filter(q => tokens.filter(t => q.query.toLowerCase().includes(t)).length >= 2)
    .sort((a, b) => b.impressions - a.impressions);
  const kwSet = [...new Set([seed, ...related.map(r => r.query)])].slice(0, 50);

  console.log(`\n=== One-page keyword analysis: "${seed}" ===`);
  console.log(`\nYour page already ranks for these ${related.length} queries (from GSC):`);
  console.log("  query | impr | pos | clicks");
  related.slice(0, 20).forEach(r => console.log(`  ${r.query} | ${r.impressions} | ${r.position.toFixed(1)} | ${r.clicks}`));
  console.log(`\nWill fetch volume + difficulty for ${kwSet.length} keywords, plus idea opportunities for the seed.`);
  console.log(`Estimated cost: ~$0.10–0.20.`);
  if (dry) { console.log(`\n(--dry: no API calls made. Re-run without --dry once the account is verified.)`); return; }

  // live volume
  const vj = await df("/keywords_data/google_ads/search_volume/live", [{ keywords: kwSet, location_code: LOC, language_code: LANG }]);
  const vol = Object.fromEntries((vj.tasks?.[0]?.result || []).map(r => [r.keyword.toLowerCase(), r]));
  // live difficulty
  const dj = await df("/dataforseo_labs/google/bulk_keyword_difficulty/live", [{ keywords: kwSet, location_code: LOC, language_code: LANG }]);
  const diff = Object.fromEntries((dj.tasks?.[0]?.result?.[0]?.items || []).map(it => [it.keyword.toLowerCase(), it.keyword_difficulty]));

  console.log("\n--- VOLUME + DIFFICULTY (your page's keywords) ---");
  console.log("keyword | volume | difficulty | cpc | your pos");
  const posByQ = Object.fromEntries(gsc.queries.map(q => [q.query.toLowerCase(), q.position]));
  kwSet.map(k => ({ k, v: vol[k.toLowerCase()]?.search_volume ?? 0, d: diff[k.toLowerCase()] ?? "—", c: vol[k.toLowerCase()]?.cpc ?? "—", p: posByQ[k.toLowerCase()] }))
    .sort((a, b) => b.v - a.v)
    .forEach(r => console.log(`${r.k} | ${r.v} | ${r.d} | $${r.c} | ${r.p ? r.p.toFixed(1) : "-"}`));
  // suggestion seed = seed minus stopwords, so we get the broad opportunity set
  const sugSeed = seed.toLowerCase().split(/\s+/).filter(w => !["need","needs","companies","company","the","for","a","to","of","why","do"].includes(w)).join(" ");
  await ideas(sugSeed);
}

// --serp: who actually ranks in the top 10 for a query (your real competition for it).
async function serp(keyword) {
  const j = await df("/serp/google/organic/live/advanced", [
    { keyword, location_code: LOC, language_code: LANG, depth: 10 },
  ]);
  const items = (j.tasks?.[0]?.result?.[0]?.items || []).filter(i => i.type === "organic");
  console.log(`\n--- TOP 10 for "${keyword}" (who you're up against) ---`);
  console.log("pos | domain | title");
  items.slice(0, 10).forEach(i => console.log(`${String(i.rank_group).padStart(2)} | ${(i.domain||"").padEnd(28)} | ${(i.title||"").slice(0,60)}`));
  const us = items.find(i => (i.domain||"").includes("axiantpartners"));
  console.log(us ? `\nYou: position ${us.rank_group} — ${us.url}` : `\nYou: not in top 10.`);
  console.log(`(cost: $${j.cost ?? "?"})`);
}

// helper: pull a domain's ranked keywords (top by volume)
async function rankedKeywords(domain, limit = 200) {
  const j = await df("/dataforseo_labs/google/ranked_keywords/live", [
    { target: domain, location_code: LOC, language_code: LANG, limit,
      order_by: ["keyword_data.keyword_info.search_volume,desc"] },
  ]);
  return (j.tasks?.[0]?.result?.[0]?.items || []).map(it => ({
    keyword: it.keyword_data?.keyword,
    volume: it.keyword_data?.keyword_info?.search_volume ?? 0,
    difficulty: it.keyword_data?.keyword_properties?.keyword_difficulty,
    pos: it.ranked_serp_element?.serp_item?.rank_group,
  })).filter(r => r.keyword);
}

// --competitors: the domains that compete with you for the most keywords (who to gap-analyze).
async function competitors(domain = OUR_DOMAIN) {
  const j = await df("/dataforseo_labs/google/competitors_domain/live", [
    { target: domain, location_code: LOC, language_code: LANG, limit: 20,
      order_by: ["intersections,desc"] },
  ]);
  const items = j.tasks?.[0]?.result?.[0]?.items || [];
  const seen = new Set(items.map(i => (i.domain || "").toLowerCase()));
  // ensure our explicitly-known competitors always appear, even if not auto-detected
  KNOWN_COMPETITORS.forEach(d => { if (!seen.has(d.toLowerCase())) items.push({ domain: d, intersections: null, avg_position: null, known: true }); });
  console.log(`\n--- SEO competitors of ${domain} (auto-detected + known) ---`);
  console.log("domain | shared keywords | their avg pos");
  items.forEach(i => console.log(`${(i.domain||"").padEnd(34)} | ${i.intersections ?? "—"} | ${i.avg_position ? i.avg_position.toFixed(1) : "—"}${i.known ? "   (known)" : ""}`));
  console.log(`(cost: $${j.cost ?? "?"})`);
}

// --gap: keywords a competitor ranks for that you DON'T (the content-gap build list).
async function gap(competitor) {
  const [theirs, ours] = await Promise.all([rankedKeywords(competitor, 300), rankedKeywords(OUR_DOMAIN, 700)]);
  const oursSet = new Set(ours.map(r => r.keyword.toLowerCase()));
  const gaps = theirs.filter(r => r.volume > 0 && !oursSet.has(r.keyword.toLowerCase()))
    .sort((a, b) => b.volume - a.volume).slice(0, 40);
  console.log(`\n--- CONTENT GAP: ${competitor} ranks for these, ${OUR_DOMAIN} does NOT ---`);
  console.log("keyword | volume | difficulty | their pos");
  gaps.forEach(r => console.log(`${r.keyword} | ${r.volume} | ${r.difficulty ?? "—"} | ${r.pos ?? "—"}`));
  console.log(`\n(${gaps.length} gap keywords · they rank ${theirs.length}, you rank ${ours.length} of those checked)`);
}

// rich per-keyword extraction from a ranked_keywords item
function richItem(it) {
  const kd = it.keyword_data || {};
  const feats = kd.serp_info?.serp_item_types || [];
  return {
    keyword: kd.keyword,
    volume: kd.keyword_info?.search_volume ?? 0,
    difficulty: kd.keyword_properties?.keyword_difficulty,
    cpc: kd.keyword_info?.cpc != null ? Math.round(kd.keyword_info.cpc * 100) / 100 : null,
    competition: kd.keyword_info?.competition_level || null,
    intent: kd.search_intent_info?.main_intent || null,
    trend: kd.keyword_info?.search_volume_trend?.yearly ?? null,
    serpFeatures: feats,
    aiOverview: feats.includes("ai_overview"),
    featuredSnippet: feats.includes("featured_snippet"),
    paa: feats.includes("people_also_ask"),
    refDomainsNeeded: kd.avg_backlinks_info?.referring_domains != null ? Math.round(kd.avg_backlinks_info.referring_domains) : null,
    position: it.ranked_serp_element?.serp_item?.rank_group ?? null,
    url: it.ranked_serp_element?.serp_item?.url || null,
  };
}
async function rankedRich(domain, limit) {
  const j = await df("/dataforseo_labs/google/ranked_keywords/live", [
    { target: domain, location_code: LOC, language_code: LANG, limit,
      order_by: ["keyword_data.keyword_info.search_volume,desc"] },
  ]);
  return (j.tasks?.[0]?.result?.[0]?.items || []).map(richItem).filter((r) => r.keyword);
}

// Axiant/financing relevance filter — strips competitor blog cruft (hedge funds,
// credit-score definitions, accounting theory) so the gap is real lending terms.
// Applied ONLY for axiantpartners.com; other sites keep all competitor terms.
const REL_FINANCE = /(business (loan|financ|lend|fund|credit|capital|line)|small business (loan|financ|lend|fund|credit)|working.?capital|unsecured (business|commercial)|merchant cash|cash advance|invoice factor|factoring|receivable financ|accounts receivable financ|a\/r financ|equipment financ|equipment leas|\bsba\b|revenue.?based (loan|financ|lend)|bridge loan|swing loan|acquisition (loan|financ)|line of credit|term loan|commercial (loan|financ|lend|mortgage|real estate|bridge)|asset (financ|based lend)|\bmca\b|hard money|fix and flip|construction (loan|financ)|debt (relief|consolidat|refinanc)|startup (loan|financ|fund)|funder)/i;
const SOCIAL = /(youtube|reddit|facebook|instagram|linkedin|quora|pinterest|twitter|x\.com|wikipedia|yelp|tiktok|medium\.com|bbb\.org)/i;

// --generate: comprehensive per-site pull -> writes keyword-data JSON for the audit Keywords tab.
// Works for ANY domain: Axiant uses its curated competitor list + finance filter;
// other sites use auto-detected competitors and keep all terms.
async function generate(domain, outPath) {
  const target = domain || OUR_DOMAIN;
  const isAxiant = target === OUR_DOMAIN;
  const isJyni = target.toLowerCase() === "jyni.io";
  const vertical = SITE_VERTICALS[target.toLowerCase()] || null; // financing-niche landing site?
  log(`Pulling ranked keywords for ${target}…`);
  let ours = await rankedRich(target, 700);
  // jyni.io: AI CRM & lead-gen product — keep brand + product/software-buyer terms, strip the
  // legacy financing/broker keywords its old content cluster ranks for (off-strategy for the product).
  if (isJyni) ours = ours.filter((k) => /jyni/i.test(k.keyword) || (JYNI_REL.test(k.keyword) && !JYNI_EXCLUDE.test(k.keyword)));
  // landing sites: keep only keywords on-purpose for that page (funding intent OR its vertical),
  // minus consumer/markets finance noise.
  else if (vertical) ours = ours.filter((k) => (FUNDING_REL.test(k.keyword) || vertical.test(k.keyword)) && !FUNDING_EXCLUDE.test(k.keyword));
  const ourSet = new Set(ours.map((k) => k.keyword.toLowerCase()));

  // auto-detected competitor list
  let compList = [];
  try {
    const cj = await df("/dataforseo_labs/google/competitors_domain/live", [
      { target, location_code: LOC, language_code: LANG, limit: 15, order_by: ["intersections,desc"] }]);
    compList = (cj.tasks?.[0]?.result?.[0]?.items || []).map((i) => ({ domain: i.domain, sharedKeywords: i.intersections ?? null, avgPosition: i.avg_position ?? null }));
  } catch { /* ignore */ }

  // gap competitors: Axiant uses its curated known list. Financing-niche landing sites union their
  // top auto-detected non-social competitors with the known lenders (auto-detection on these sites
  // often surfaces operations/POS software, which aren't financing competitors). Other sites: auto only.
  const autoComps = compList.filter((c) => !SOCIAL.test(c.domain) && c.domain.toLowerCase() !== target.toLowerCase()).map((c) => c.domain);
  const gapComps = isAxiant ? KNOWN_COMPETITORS
    : isJyni ? [...new Set([...autoComps.slice(0, 3), ...JYNI_COMPETITORS])].slice(0, 6)
    : vertical ? [...new Set([...autoComps.slice(0, 3), ...KNOWN_COMPETITORS])].slice(0, 5)
    : autoComps.slice(0, 3);
  const gapMap = new Map();
  for (const comp of gapComps) {
    try {
      log(`Gap vs ${comp}…`);
      const theirs = await rankedRich(comp, 200);
      theirs.forEach((k) => {
        const key = k.keyword.toLowerCase();
        if (ourSet.has(key) || (k.volume || 0) <= 0) return;
        const prev = gapMap.get(key);
        if (!prev || (k.volume || 0) > (prev.volume || 0)) gapMap.set(key, { ...k, competitor: comp, competitorPos: k.position });
      });
    } catch (e) { log(`  (skip ${comp}: ${e.message})`); }
  }
  let gap = [...gapMap.values()].sort((a, b) => (b.volume || 0) - (a.volume || 0));
  if (isAxiant) gap = gap.filter((g) => REL_FINANCE.test(g.keyword));
  // jyni.io: every build target must be a CRM / lead-gen / sales-software term — never a
  // financing keyword the SaaS competitors happen to also rank for.
  else if (isJyni) gap = gap.filter((g) => JYNI_REL.test(g.keyword) && !JYNI_EXCLUDE.test(g.keyword));
  // landing sites: every gap target must be funding-intent (no off-topic ops/software terms),
  // and vertical-specific ones (e.g. "restaurant business loan") lead — generic financing head
  // terms only pad the tail. Keeps the list on-purpose without going empty when lenders don't
  // rank for many vertical-flavored terms.
  if (vertical) {
    const fund = gap.filter((g) => FUNDING_REL.test(g.keyword) && !FUNDING_EXCLUDE.test(g.keyword));
    const strict = fund.filter((g) => vertical.test(g.keyword));
    const strictKeys = new Set(strict.map((g) => g.keyword));
    gap = [...strict, ...fund.filter((g) => !strictKeys.has(g.keyword))];
  }
  gap = gap.slice(0, 80);

  // ensure the competitors we gapped against appear in the displayed list
  if (isAxiant || vertical || isJyni) {
    const seen = new Set(compList.map((c) => c.domain.toLowerCase()));
    gapComps.forEach((d) => { if (!seen.has(d.toLowerCase())) compList.push({ domain: d, sharedKeywords: null, avgPosition: null }); });
  }

  const data = { domain: target, generatedAt: new Date().toISOString().slice(0, 10), sample: false, keywords: ours, gap, competitors: compList };
  const out = outPath || join(ROOT, "_analysis", "keyword-data.json");
  writeFileSync(out, JSON.stringify(data, null, 2), "utf8");
  log(`✓ wrote ${out}`);
  console.log(`  ${ours.length} ranked keywords · ${gap.length} gap keywords · ${compList.length} competitors`);
  console.log(`  ${ours.filter((k) => k.aiOverview && (k.position || 99) <= 20).length} AI-Overview-exposed · ${ours.filter((k) => (k.position || 99) >= 3 && (k.position || 99) <= 20).length} striking-distance`);
}
function log(m) { console.log(m); }

// ===== Profile-driven generation (scripts/site-profiles.json) =====
// Each property has an "About this page" profile: industry, audience, seedKeywords,
// competitorCandidates, and HARD relevance/exclude filters. This makes keywords + gap
// industry-specific (e.g. restaurant terms, not generic lender terms) and surfaces
// MISALIGNED pages (ranking for off-topic terms) as cut/redirect candidates.
function loadProfiles() {
  try { return JSON.parse(readFileSync(join(ROOT, "scripts", "site-profiles.json"), "utf8")); }
  catch { return {}; }
}
async function suggestionsRich(seed, limit = 30) {
  const j = await df("/dataforseo_labs/google/keyword_suggestions/live", [
    { keyword: seed, location_code: LOC, language_code: LANG, limit, order_by: ["keyword_info.search_volume,desc"] }]);
  return (j.tasks?.[0]?.result?.[0]?.items || []).map((it) => {
    const ki = it.keyword_info || {}, feats = it.serp_info?.serp_item_types || [];
    return { keyword: it.keyword, volume: ki.search_volume ?? 0,
      difficulty: it.keyword_properties?.keyword_difficulty,
      cpc: ki.cpc != null ? Math.round(ki.cpc * 100) / 100 : null,
      competition: ki.competition_level || null,
      intent: it.search_intent_info?.main_intent || null,
      trend: ki.search_volume_trend?.yearly ?? null,
      serpFeatures: feats, aiOverview: feats.includes("ai_overview"),
      featuredSnippet: feats.includes("featured_snippet"), paa: feats.includes("people_also_ask"),
      refDomainsNeeded: null, position: null, url: null };
  }).filter((r) => r.keyword);
}
async function generateProfiled(target, profile, outPath) {
  const relRe = new RegExp(profile.relevance, "i"), excRe = new RegExp(profile.exclude, "i");
  // Optional intent filter: financing-vertical sites must match the topic AND a money/funding
  // intent (so "cafe near me" from a POS competitor is dropped, "restaurant equipment financing" kept).
  const intentRe = profile.intent ? new RegExp(profile.intent, "i") : null;
  // onVertical = the site's topic (keeps top-of-funnel content like "restaurant p&l").
  // onTarget   = topic AND money/funding intent — the build/gap targets only.
  const onVertical = (kw) => relRe.test(kw) && !excRe.test(kw);
  const onTarget = (kw) => onVertical(kw) && (!intentRe || intentRe.test(kw));
  log(`[profiled] ${target} — ${profile.industry}`);
  log(`Pulling ranked keywords…`);
  const rawOurs = await rankedRich(target, 700);
  const ours = rawOurs.filter((k) => onVertical(k.keyword));
  const ourSet = new Set(ours.map((k) => k.keyword.toLowerCase()));

  // MISALIGNED: terms the site ranks for that EXPLICITLY conflict with its goal (hit the exclude
  // pattern) -> group by page = cut / redirect / noindex candidates. Using exclude (not merely
  // "fails relevance") keeps this precise — a delete recommendation must not flag on-strategy pages
  // just because a long-tail term isn't captured by the relevance regex. Brand terms never match
  // exclude, so a site ranking for its own name is never flagged.
  const misRaw = rawOurs.filter((k) => excRe.test(k.keyword) && (k.volume || 0) > 0 && k.url && (k.position || 99) <= 30);
  const byUrl = new Map();
  for (const k of misRaw) {
    const e = byUrl.get(k.url) || { url: k.url, terms: [], maxVol: 0 };
    e.terms.push({ keyword: k.keyword, volume: k.volume, position: k.position });
    e.maxVol = Math.max(e.maxVol, k.volume || 0); byUrl.set(k.url, e);
  }
  const misaligned = [...byUrl.values()]
    .map((e) => ({ url: e.url, maxVol: e.maxVol, terms: e.terms.sort((a, b) => (b.volume || 0) - (a.volume || 0)).slice(0, 5) }))
    .sort((a, b) => b.maxVol - a.maxVol).slice(0, 40);

  // GAP: seed-driven (industry) + competitor-driven, all HARD-filtered to on-topic. No padding.
  const gapMap = new Map();
  const addGap = (k, comp) => {
    const key = k.keyword.toLowerCase();
    if (ourSet.has(key) || (k.volume || 0) <= 0 || !onTarget(k.keyword)) return;
    const prev = gapMap.get(key);
    if (!prev) { gapMap.set(key, { ...k, competitor: comp || null, competitorPos: comp ? k.position : null }); return; }
    if ((k.volume || 0) > (prev.volume || 0)) { prev.volume = k.volume; if (k.difficulty != null) prev.difficulty = k.difficulty; }
    if (comp && !prev.competitor) { prev.competitor = comp; prev.competitorPos = k.position; }
  };
  for (const seed of (profile.seedKeywords || []).slice(0, 8)) {
    try { log(`Ideas: "${seed}"…`); (await suggestionsRich(seed, 30)).forEach((k) => addGap(k, null)); }
    catch (e) { log(`  (skip seed "${seed}": ${e.message})`); }
  }
  let compList = [];
  try {
    const cj = await df("/dataforseo_labs/google/competitors_domain/live", [
      { target, location_code: LOC, language_code: LANG, limit: 15, order_by: ["intersections,desc"] }]);
    compList = (cj.tasks?.[0]?.result?.[0]?.items || []).map((i) => ({ domain: i.domain, sharedKeywords: i.intersections ?? null, avgPosition: i.avg_position ?? null }));
  } catch { /* ignore */ }
  const autoComps = compList.filter((c) => !SOCIAL.test(c.domain) && c.domain.toLowerCase() !== target).map((c) => c.domain);
  const gapComps = [...new Set([...autoComps.slice(0, 3), ...(profile.competitorCandidates || [])])].slice(0, 6);
  for (const comp of gapComps) {
    try { log(`Gap vs ${comp}…`); (await rankedRich(comp, 200)).forEach((k) => addGap(k, comp)); }
    catch (e) { log(`  (skip ${comp}: ${e.message})`); }
  }
  const score = (k) => (k.volume || 0) * (1 - ((k.difficulty ?? 50) / 100));
  const gap = [...gapMap.values()].sort((a, b) => score(b) - score(a)).slice(0, 80);
  const seen = new Set(compList.map((c) => c.domain.toLowerCase()));
  gapComps.forEach((d) => { if (!seen.has(d.toLowerCase())) compList.push({ domain: d, sharedKeywords: null, avgPosition: null }); });

  const data = { domain: target, generatedAt: new Date().toISOString().slice(0, 10), sample: false,
    overview: profile.overview, industry: profile.industry, audience: profile.audience,
    relevance: profile.relevance, intent: profile.intent || null, exclude: profile.exclude,
    keywords: ours, gap, misaligned, competitors: compList };
  const out = outPath || join(ROOT, "_analysis", "keyword-data.json");
  writeFileSync(out, JSON.stringify(data, null, 2), "utf8");
  log(`✓ wrote ${out}`);
  console.log(`  ${ours.length} ranked · ${gap.length} gap · ${misaligned.length} misaligned page(s) · ${compList.length} competitors`);
}
async function generateDispatch(domain, outPath) {
  const target = (domain || OUR_DOMAIN).toLowerCase();
  const profile = loadProfiles()[target];
  if (profile) return generateProfiled(target, profile, outPath);
  log(`(no profile for ${target} — using legacy generator)`);
  return generate(domain, outPath);
}

const arg = process.argv[2];
const rest = process.argv.slice(3);
const dry = rest.includes("--dry");
const outIdx = rest.indexOf("--out");
const outPath = outIdx >= 0 ? rest[outIdx + 1] : null;
const val = rest.filter((a, i) => a !== "--dry" && a !== "--out" && !(outIdx >= 0 && i === outIdx + 1)).join(" ");
try {
  if (arg === "--test") await test();
  else if (arg === "--volume") await volume(val);
  else if (arg === "--ideas") await ideas(val);
  else if (arg === "--page") await page(val, dry);
  else if (arg === "--serp") await serp(val);
  else if (arg === "--competitors") await competitors(val || OUR_DOMAIN);
  else if (arg === "--gap") await gap(val);
  else if (arg === "--generate") await generateDispatch(val || OUR_DOMAIN, outPath);
  else console.log("usage: --test | --volume \"kw\" | --ideas \"seed\" | --page \"seed\" [--dry] | --serp \"kw\" | --competitors [domain] | --gap \"competitor.com\" | --generate [domain] [--out path]");
} catch (e) {
  console.error("ERROR:", e.message);
  process.exit(1);
}
