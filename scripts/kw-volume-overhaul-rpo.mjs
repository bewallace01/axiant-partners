#!/usr/bin/env node
// Overhaul/engine + RPO/rent-to-own keyword volume via DataForSEO.
// Credential loading copied from Axiant-Partners-CRM/scripts/kw_volume.mjs (never printed).
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

const GROUPS = {
  "A. OVERHAUL/ENGINE — commercial truck (target ICP)": [
    "truck engine overhaul financing", "semi truck engine overhaul financing",
    "engine overhaul financing", "truck engine rebuild financing",
    "semi truck engine rebuild financing", "engine rebuild financing",
    "commercial truck engine repair financing", "semi truck engine repair financing",
    "semi truck repair financing", "commercial truck repair financing",
    "truck repair financing", "heavy duty truck repair financing",
    "diesel truck repair financing", "diesel repair financing",
    "semi truck repair loan", "commercial truck repair loan",
    "engine overhaul loan", "engine rebuild loan",
    "truck repair financing bad credit", "semi truck repair financing no credit check",
    "commercial truck repair financing no credit check",
  ],
  "B. OVERHAUL — cost research (top of funnel)": [
    "truck engine overhaul cost", "semi truck engine overhaul cost",
    "truck engine rebuild cost", "semi truck engine rebuild cost",
    "in frame overhaul cost", "out of frame overhaul cost",
    "cummins isx overhaul cost", "cummins x15 overhaul cost", "n14 cummins overhaul cost",
    "cummins in frame rebuild cost", "dd15 in frame rebuild cost", "dt466 in frame rebuild cost",
    "volvo truck engine rebuild cost", "mack truck engine rebuild cost",
    "how much does it cost to rebuild a semi truck engine",
    "difference between in frame and out of frame overhaul",
  ],
  "C. OVERHAUL — consumer branch (wrong ICP, control)": [
    "engine repair financing", "engine repair financing near me",
    "engine replacement financing", "engine replacement loan",
    "auto repair financing", "auto repair financing for bad credit",
    "transmission replacement financing", "financing for transmission repair",
  ],
  "D. OVERHAUL — adjacent verticals": [
    "aircraft engine overhaul financing", "aircraft engine overhaul loan",
    "aircraft engine overhaul cost",
  ],
  "E. RPO — literal term (the one you asked for)": [
    "rpo financing", "rental purchase option", "rental purchase option equipment",
    "rental purchase option financing", "rental purchase option agreement",
    "rpo equipment", "rental conversion financing", "rpo buyout financing",
  ],
  "F. RENT-TO-OWN / LEASE-TO-OWN — the real demand": [
    "rent to own equipment", "lease to own equipment", "lease to own equipment financing",
    "rent to own heavy equipment", "lease to own heavy equipment",
    "rent to own construction equipment", "lease to own construction equipment",
    "rent to own heavy equipment no credit check",
    "rent to own construction equipment no credit check",
    "rent to own equipment no credit check", "lease to own equipment no credit check",
    "lease to own equipment with bad credit", "how does rent to own equipment work",
  ],
  "G. RENT-TO-OWN — by machine": [
    "rent to own excavator", "rent to own mini excavator", "rent to own skid steer",
    "rent to own backhoe", "rent to own forklift", "rent to own dump truck",
    "rent to own trailers", "rent to own semi trucks", "lease to own semi trucks",
    "rent to own skid steer no credit check", "rent to own excavator no credit check",
    "lease to own skid steer", "lease to own excavator", "lease to own dump truck",
  ],
  "H. LEASE PURCHASE — trucking (adjacent)": [
    "lease purchase semi truck", "lease purchase semi trucks",
    "lease purchase a semi truck", "lease purchase semi truck no credit check",
    "lease purchase semi truck with bad credit", "lease purchase trucking companies",
  ],
  "I. BENCHMARKS — terms the site already targets": [
    "equipment financing", "business line of credit", "semi truck financing",
    "commercial truck financing", "owner operator truck financing",
  ],
};

// Google Ads search_volume rejects the whole task if any keyword exceeds 10 words.
const ALL_RAW = [...new Set(Object.values(GROUPS).flat())];
const TOO_LONG = ALL_RAW.filter(k => k.split(/\s+/).length > 10);
if (TOO_LONG.length) console.log("SKIPPED (>10 words, endpoint limit):\n  " + TOO_LONG.join("\n  ") + "\n");
const ALL = ALL_RAW.filter(k => k.split(/\s+/).length <= 10);
const body = [{ location_code: 2840, language_name: "English", keywords: ALL }];
const res = await fetch("https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live", {
  method: "POST", headers: { Authorization: AUTH, "Content-Type": "application/json" }, body: JSON.stringify(body),
});
const json = await res.json();
if (json.status_code !== 20000) { console.error("API error:", json.status_code, json.status_message); process.exit(1); }

const byKw = new Map();
for (const r of json.tasks?.[0]?.result || []) byKw.set(r.keyword, r);

for (const [label, kws] of Object.entries(GROUPS)) {
  console.log("\n" + label);
  console.log("-".repeat(78));
  const rows = kws.map(k => {
    const r = byKw.get(k) || {};
    return { kw: k, vol: r.search_volume ?? null, cpc: r.cpc ?? null, comp: r.competition ?? "-" };
  }).sort((a, b) => (b.vol ?? -1) - (a.vol ?? -1));
  console.log("KEYWORD".padEnd(50), "VOL/mo".padStart(7), "   CPC$", " COMP");
  for (const r of rows) {
    console.log(
      r.kw.padEnd(50),
      String(r.vol === null ? "no data" : r.vol).padStart(7),
      "  " + (r.cpc === null ? "  -  " : Number(r.cpc).toFixed(2)).padStart(6),
      " " + r.comp
    );
  }
}
console.log(`\ncost: $${json.cost ?? 0}   keywords requested: ${ALL.length}`);
fs.writeFileSync("volume_raw.json", JSON.stringify(json, null, 2));
