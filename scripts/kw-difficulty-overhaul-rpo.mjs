#!/usr/bin/env node
// DataForSEO Labs: phrase-match expansions with volume + keyword difficulty.
import fs from "node:fs";
import path from "node:path";

const CRM = "C:/Users/walla/Desktop/JYNI CRM x Scraper/Axiant-Partners-CRM";
for (const name of [".env.local", ".env.local.txt", ".env"]) {
  try {
    for (const line of fs.readFileSync(path.join(CRM, name), "utf8").split(/\r?\n/)) {
      const m = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)\s*$/);
      if (!m || line.trim().startsWith("#")) continue;
      if (process.env[m[1]] === undefined) process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
    }
  } catch {}
}
const LOGIN = process.env.DATAFORSEO_LOGIN, PASS = process.env.DATAFORSEO_PASSWORD;
if (!LOGIN || !PASS) { console.error("Missing DATAFORSEO_LOGIN/PASSWORD"); process.exit(1); }
const AUTH = "Basic " + Buffer.from(`${LOGIN}:${PASS}`).toString("base64");

const SEEDS = [
  "truck repair financing",
  "engine overhaul financing",
  "rental purchase option",
  "rent to own equipment",
  "lease to own equipment",
];

// Labs keyword_suggestions accepts only ONE task per request.
const allTasks = [];
let totalCost = 0;
for (const seed of SEEDS) {
  const res = await fetch("https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live", {
    method: "POST",
    headers: { Authorization: AUTH, "Content-Type": "application/json" },
    body: JSON.stringify([{
      keyword: seed,
      location_code: 2840,
      language_code: "en",
      include_serp_info: false,
      include_seed_keyword: true,
      limit: 60,
      order_by: ["keyword_info.search_volume,desc"],
    }]),
  });
  const j = await res.json();
  if (j.status_code !== 20000) { console.error(`API error for "${seed}":`, j.status_code, j.status_message); continue; }
  totalCost += j.cost ?? 0;
  allTasks.push(...(j.tasks || []));
}
const json = { tasks: allTasks, cost: totalCost };
fs.writeFileSync("kd_raw.json", JSON.stringify(json, null, 2));

for (const t of json.tasks || []) {
  if (t.status_code !== 20000) { console.log(`\n### ${t.data?.keyword} -> TASK ERROR ${t.status_code} ${t.status_message}`); continue; }
  const items = t.result?.[0]?.items || [];
  console.log(`\n### seed: ${t.data?.keyword}   (${items.length} returned)`);
  console.log("KEYWORD".padEnd(52), "VOL/mo".padStart(7), "  KD", "   CPC$");
  const rows = items
    .map(i => ({
      kw: i.keyword,
      vol: i.keyword_info?.search_volume ?? 0,
      kd: i.keyword_properties?.keyword_difficulty,
      cpc: i.keyword_info?.cpc,
    }))
    .filter(r => r.vol >= 10)
    .slice(0, 30);
  for (const r of rows) {
    console.log(
      r.kw.slice(0, 52).padEnd(52),
      String(r.vol).padStart(7),
      String(r.kd ?? "-").padStart(4),
      "  " + (r.cpc == null ? "-" : Number(r.cpc).toFixed(2))
    );
  }
}
console.log(`\ncost: $${json.cost ?? 0}`);
