/**
 * Batch 1b acceptance test: the get-matched block sends attribution to the CRM.
 *
 * Serves the repo on a local port, lands on a cited article as ChatGPT would send someone
 * (?utm_source=chatgpt.com), submits the 3-field block with /.netlify/functions/apply mocked,
 * and checks:
 *   - the CRM payload carries lead_channel = ai_assistant and lead_landing_page = that article
 *   - it is a front_page lead with lead_type citation-block
 *   - /match.html opens with name/email/phone prefilled, and none of them in the URL
 *   - match.html does not send a second (partial) lead for the same person
 *
 * Playwright is not a dependency of this repo. Point at any install:
 *   PLAYWRIGHT_MODULE=../Axiant-Partners-CRM/node_modules/playwright node scripts/tests/get-matched.test.mjs
 */
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { chromium } = (() => {
  try { return require("playwright"); } catch { return require(path.resolve(process.env.PLAYWRIGHT_MODULE || "playwright")); }
})();

const PAGE = "/business-line-of-credit/articles/best-unsecured-business-lines-of-credit-2026/";
const TYPES = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".webp": "image/webp",
  ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".json": "application/json" };

const server = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, "http://x").pathname);
  if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" });
  fs.createReadStream(f).pipe(res);
});
await new Promise((r) => server.listen(0, "127.0.0.1", r));
const origin = `http://127.0.0.1:${server.address().port}`;

const fail = [];
const check = (ok, msg) => { console.log(`${ok ? "PASS" : "FAIL"}  ${msg}`); if (!ok) fail.push(msg); };

const browser = await chromium.launch();
try {
  const page = await browser.newPage();
  const crmCalls = [];
  // Nothing leaves the machine: third-party tags are dropped, the CRM and Netlify Forms are mocked.
  await page.route("**/*", (route) => {
    const u = new URL(route.request().url());
    if (u.origin !== origin) return route.abort();
    if (u.pathname === "/.netlify/functions/apply") {
      crmCalls.push(JSON.parse(route.request().postData() || "{}"));
      return route.fulfill({ status: 200, contentType: "application/json", body: '{"ok":true}' });
    }
    if (route.request().method() === "POST" && u.pathname === "/") return route.fulfill({ status: 200, body: "" });
    return route.continue();
  });

  await page.goto(`${origin}${PAGE}?utm_source=chatgpt.com`, { waitUntil: "load" });
  await page.waitForFunction(() => typeof window.__axAttr === "function");
  await page.fill("#axGetMatched [name=name]", "Test Borrower");
  await page.fill("#axGetMatched [name=email]", "test.borrower@example.com");
  await page.fill("#axGetMatched [name=phone]", "5615550100");
  await Promise.all([page.waitForURL("**/match.html"), page.click("#axGetMatched button")]);

  const lead = crmCalls[0] || {};
  check(crmCalls.length === 1, `one CRM call from the block (got ${crmCalls.length})`);
  check(lead.lead_channel === "ai_assistant", `lead_channel = ai_assistant (got ${lead.lead_channel})`);
  check((lead.lead_landing_page || "").startsWith(PAGE), `lead_landing_page = ${PAGE}... (got ${lead.lead_landing_page})`);
  check(lead.form_type === "front_page" && lead.lead_type === "citation-block", `front_page / citation-block (got ${lead.form_type} / ${lead.lead_type})`);
  check(lead.utm_source === "chatgpt.com", `utm_source forwarded (got ${lead.utm_source})`);

  check(!/test\.borrower|Borrower|555/.test(page.url()), `no contact details in the match.html URL (${page.url()})`);
  await page.waitForFunction(() => document.getElementById("email")?.value);
  check(await page.inputValue("#fullName") === "Test Borrower", "match.html name prefilled");
  check(await page.inputValue("#email") === "test.borrower@example.com", "match.html email prefilled");
  check(await page.inputValue("#phone") === "5615550100", "match.html phone prefilled");

  await page.focus("#email"); await page.focus("#phone"); await page.focus("#fullName"); // fire the blur-based partial capture
  await page.waitForTimeout(500);
  check(crmCalls.length === 1, `match.html sent no second partial lead (CRM calls: ${crmCalls.length})`);
} finally {
  await browser.close();
  server.close();
}
console.log(fail.length ? `\n${fail.length} failed` : "\nall passed");
process.exit(fail.length ? 1 : 0);
