#!/usr/bin/env node
/* Axiant Partners full-site audit -> self-contained HTML dashboard.
 * Run: node scripts/site-audit.js   (or: npm run audit)
 * Output: _analysis/site-audit.html      (gitignored; never deployed)
 * History: _analysis/site-audit-history.json (gitignored; one snapshot/run, dedup by day)
 * Auto-runs via .git/hooks/post-commit after every commit. */
const fs = require('fs'), path = require('path');
const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, '_analysis');
const today = new Date().toISOString().slice(0, 10);
const _now = new Date();
const _mon = ['January','February','March','April','May','June','July','August','September','October','November','December'][_now.getMonth()];
let _h = _now.getHours(); const _ap = _h >= 12 ? 'PM' : 'AM'; _h = _h % 12 || 12;
const stamp = _mon + ' ' + _now.getDate() + ', ' + _now.getFullYear() + ' at ' + _h + ':' + String(_now.getMinutes()).padStart(2,'0') + ' ' + _ap;

// ---------- crawl ----------
function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    const rel = path.relative(ROOT, p).split(path.sep).join('/');
    if (e.isDirectory()) {
      if (/^(\.git|node_modules|fonts|assets|docs|__pycache__)$/.test(e.name)) continue;
      if (rel.startsWith('_')) continue;
      walk(p, out);
    } else if (e.name.endsWith('.html')) {
      if (rel.startsWith('_')) continue;
      out.push(rel);
    }
  }
  return out;
}
const files = walk(ROOT, []).sort();

// ---------- helpers ----------
const norm = s => s.replace(/&amp;/g,'&').replace(/&[a-z]+;/g,' ').replace(/&#\d+;/g,' ').replace(/\s+/g,' ').trim();
const keyOf = rel => ('/' + rel).replace(/index\.html$/,'');
function resolveLink(fromRel, href) {
  href = href.split('#')[0].split('?')[0];
  if (!href) return null;
  let target = href.startsWith('/') ? href.slice(1)
    : path.posix.normalize(path.posix.join(path.posix.dirname(fromRel), href));
  const cands = [target, target.replace(/\/$/,'') + '/index.html', target + (target.endsWith('.html')?'':'.html'), target + '/index.html'];
  for (const c of cands) {
    const clean = c.replace(/^\//,'');
    if (fs.existsSync(path.join(ROOT, clean)) && fs.statSync(path.join(ROOT, clean)).isFile()) return clean;
  }
  return null;
}
function classify(rel) {
  const parts = rel.split('/'), base = parts[parts.length-1];
  if (/^get-matched\//.test(rel)) return 'ad-landing';
  if (/(^|\/)(tools|fragments)\//.test(rel) || /digital-marketing\/fragments/.test(rel)) return 'fragment';
  if (/articles\/index\.html$/.test(rel)) return 'article-index';
  if (/^[^/]+\/articles\/[^/]+\/index\.html$/.test(rel)) return 'article';
  if (/^equipment\/[^/]+\/[^/]+\/index\.html$/.test(rel)) return 'article';
  if (/^equipment\/[^/]+\/index\.html$/.test(rel)) return 'equipment-hub';
  if (parts.length>1 && base==='index.html') return 'cluster-index';
  if (parts.length===1) {
    if (/-business-financing\.html$/.test(base)) return 'industry-hub';
    if (/-guide\.html$/.test(base)) return 'guide';
    if (/^business-loans-[a-z-]+\.html$/.test(base)) return 'geo-landing';
    if (/(\d+|business-loan)\.html$/.test(base) && /loan|financing/.test(base)) return 'landing';
    const svc = new Set(['equipment-financing.html','sba-loans.html','business-line-of-credit.html','working-capital-loans.html','commercial-real-estate-loans.html','business-term-loans.html','merchant-cash-advance.html','invoice-factoring.html','commercial-bridge-loans.html','accounts-receivable-financing.html','revenue-based-financing.html','securities-based-lending.html','inventory-financing.html']);
    if (svc.has(base)) return 'service-hub';
    const util = new Set(['index.html','match.html','calculator.html','calculator-embed.html','contact.html','services.html','industries.html','about.html','blog.html','faq.html','referral.html','privacy-policy.html','terms-and-conditions.html','vendors.html','thank-you.html','business-growth.html']);
    if (util.has(base)) return 'core';
    return 'root-page';
  }
  return 'page';
}
const CHROME = new Set(['/','/match.html','/index.html','/services.html','/industries.html','/calculator.html','/contact.html','/about.html','/privacy-policy.html','/terms-and-conditions.html','/vendors.html','/blog.html','/faq.html','/referral.html','/business-growth.html','/calculator-embed.html','/thank-you.html']);

// ---------- sitemap ----------
let sitemapKeys = new Set();
try {
  const sm = fs.readFileSync(path.join(ROOT,'sitemap.xml'),'utf8');
  for (const m of sm.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g)) sitemapKeys.add(m[1].replace(/^https?:\/\/[^/]+/,''));
} catch(e){}

// ---------- parse ----------
const pages = {}, inbound = {};
for (const rel of files) {
  const html = fs.readFileSync(path.join(ROOT, rel), 'utf8');
  const key = keyOf(rel);
  const titleM = html.match(/<title>([^<]*)<\/title>/i);
  const descM = html.match(/<meta name="description" content="([^"]*)"/i);
  const robotsM = html.match(/<meta name="robots" content="([^"]*)"/i);
  const canonM = html.match(/<link rel="canonical"[^>]*href="([^"]+)"/i);
  const noindex = robotsM ? /noindex/i.test(robotsM[1]) : false;
  const h1 = (html.match(/<h1[\s>]/gi)||[]).length;
  const ldBlocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi)];
  let ldFail = 0; const types = new Set();
  for (const b of ldBlocks) {
    try { JSON.parse(b[1].replace(/&amp;/g,'&')); } catch(e){ ldFail++; }
    for (const t of b[1].matchAll(/"@type"\s*:\s*"([^"]+)"/g)) types.add(t[1]);
  }
  let wc=0, src='body';
  const mainM = html.match(/<main[\s\S]*?<\/main>/i);
  if (mainM){ wc = norm(mainM[0].replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; src='main'; }
  else {
    const secs=[...html.matchAll(/<section class="about-section[^"]*">([\s\S]*?)<\/section>/gi)];
    if (secs.length){ wc = norm(secs.map(s=>s[1]).join(' ').replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; src='about'; }
    else { const bodyM=html.match(/<body[\s\S]*<\/body>/i); wc = norm((bodyM?bodyM[0]:html).replace(/<(script|style)[\s\S]*?<\/\1>/gi,' ').replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; }
  }
  const imgs=[...html.matchAll(/<img\b[^>]*>/gi)].map(m=>m[0]);
  const imgNoAlt = imgs.filter(t=>!/\balt\s*=/.test(t)).length;
  const hrefs=[...html.matchAll(/href="([^"]+)"/gi)].map(m=>m[1])
    .filter(h=>!/^(https?:|mailto:|tel:|\/\/|data:|#)/.test(h))
    .filter(h=>!/\.(css|js|json|xml|txt|webp|png|jpg|jpeg|svg|gif|ico|pdf|webmanifest)(\?|$)/i.test(h.split('#')[0]));
  const outKeys=new Set(); const broken=[];
  for (const h of hrefs){
    const r = resolveLink(rel, h);
    if (r===null){ if(!h.includes("'+")&&!h.includes('${')) broken.push(h); }
    else outKeys.add(keyOf(r));
  }
  const modM = html.match(/(?:article:modified_time|dateModified)["']?\s*[:=]\s*["']?(\d{4}-\d{2}-\d{2})/);
  // A meta-refresh redirect stub is not real content — it should not be flagged as thin/stale/no-FAQ.
  const redirect = /<meta[^>]+http-equiv=["']?refresh["']?[^>]*content=["'][^"']*url=/i.test(html);
  const dataBatch = /data-batch/.test(html);
  const hasTool = /<iframe[^>]*calculator|<input\b|id="[^"]*[Cc]alc/.test(html);
  let na=0; for(const b of Buffer.from(html)){ if(b>127) na++; }
  pages[key] = { key, rel, type: classify(rel), cluster: rel.includes('/')?rel.split('/')[0]:'(root)',
    title: titleM?norm(titleM[1]):'', desc: descM?descM[1].length:0, h1, noindex,
    schema:[...types], ldFail, wc, wcSrc:src, imgs:imgs.length, imgNoAlt,
    out:[...outKeys], broken, inSitemap: sitemapKeys.has(key), mod: modM?modM[1]:null, canonical: canonM?canonM[1]:null, redirect, dataBatch, hasTool, nonascii:na };
  for (const ok of outKeys) inbound[ok]=(inbound[ok]||0)+1;
}
for (const k in pages) pages[k].inbound = inbound[k]||0;

// ---------- aggregates ----------
const arr = Object.values(pages);
const indexable = arr.filter(p=>!p.noindex);
const contentTypes = new Set(['article','industry-hub','service-hub','guide','article-index','equipment-hub','cluster-index','landing','geo-landing','root-page','page']);
const isContent = p => contentTypes.has(p.type);
// List/card-grid page types are not Q&A/answer targets — FAQPage schema is inappropriate there.
const LIST_TYPES = new Set(['article-index','cluster-index']);
// A page that canonicals to a DIFFERENT URL is a duplicate that consolidates elsewhere; it is
// correctly excluded from the sitemap and should NOT be flagged as orphan/weak — link equity is
// meant to flow to its canonical, not to it.
const trimSlash = s => (s.replace(/\/$/,'') || '/');
const isSelfCanonical = p => {
  if (!p.canonical) return true;
  const cpath = p.canonical.replace(/^https?:\/\/[^/]+/,'').replace(/index\.html$/,'') || '/';
  return trimSlash(cpath) === trimSlash(p.key);
};
const titleMap={};
for(const p of indexable){ if(p.type==='fragment'||p.type==='ad-landing')continue; const t=p.title.replace(/\s*\|\s*Axiant.*/i,'').trim().toLowerCase(); if(!t)continue; (titleMap[t]=titleMap[t]||[]).push(p.key); }
const dupTitles = Object.entries(titleMap).filter(([t,v])=>v.length>1);
const orphans = indexable.filter(p=>p.inbound===0 && !CHROME.has(p.key) && isContent(p) && p.type!=='core' && !p.redirect && isSelfCanonical(p));
const articles = arr.filter(p=>p.type==='article');
// Thin = genuine ARTICLES only. Calculators/embeds, article-index card grids, hubs,
// print brochures, and vendor pages are legitimately short and are NOT thin content.
const isArticleType = p => p.type==='article' && !/calculator|embed|brochure/.test(p.rel);
const veryThin = indexable.filter(p=>isArticleType(p)&&!p.redirect&&p.wc<500);
const thin = indexable.filter(p=>isArticleType(p)&&!p.redirect&&p.wc>=500&&p.wc<800);
const brokenList=[]; for(const p of arr) for(const b of p.broken) brokenList.push({from:p.key, href:b});
const notInSitemap = indexable.filter(p=>!p.inSitemap && !['core','fragment','ad-landing','cluster-index'].includes(p.type) && isSelfCanonical(p));
const noindexInSitemap = arr.filter(p=>p.noindex && p.inSitemap);
const deadSitemap=[...sitemapKeys].filter(k=>!pages[k]);
const noSchema = indexable.filter(p=>isContent(p)&&p.schema.length===0 && p.type!=='cluster-index' && p.inSitemap && !p.redirect);
const ldFails = arr.filter(p=>p.ldFail>0);
const stale = articles.filter(p=>!p.redirect && (!p.mod || p.mod < '2026-03-01'));
const filler = arr.filter(p=>p.dataBatch);
const weak = indexable.filter(p=>isContent(p)&&p.inbound>0&&p.inbound<=2&&p.type!=='core'&&!CHROME.has(p.key)&&!p.redirect&&isSelfCanonical(p));
const noToolHubs = arr.filter(p=>['industry-hub','service-hub','landing','geo-landing'].includes(p.type)&&!p.hasTool);
const clusters={};
for(const p of arr){ const o=(clusters[p.cluster]=clusters[p.cluster]||{cluster:p.cluster,n:0,words:0,thin:0,orphan:0,noindex:0,inb:0,inSm:0,broken:0}); o.n++; o.words+=p.wc; if(p.wc<500&&isArticleType(p))o.thin++; if(p.inbound===0&&isContent(p)&&!CHROME.has(p.key)&&isSelfCanonical(p))o.orphan++; if(p.noindex)o.noindex++; o.inb+=p.inbound; if(p.inSitemap)o.inSm++; o.broken+=p.broken.length; }
const clusterArr = Object.values(clusters).map(o=>({...o, avgw:Math.round(o.words/o.n), avgInb:(o.inb/o.n).toFixed(1)})).sort((a,b)=>b.n-a.n);
const typeDist={}; for(const p of arr) typeDist[p.type]=(typeDist[p.type]||0)+1;
const buckets=[[0,300],[300,600],[600,900],[900,1200],[1200,1600],[1600,99999]];
const hist=buckets.map(([a,b])=>({label:b>9000?(a+'+'):a+'-'+b, n: arr.filter(p=>isContent(p)&&p.wc>=a&&p.wc<b).length}));
const artByCluster={}; arr.forEach(p=>{ if(p.type==='article') artByCluster[p.cluster]=(artByCluster[p.cluster]||0)+1; });
const hubGaps = arr.filter(p=>p.type==='industry-hub').map(p=>{const base=p.rel.replace(/\.html$/,'');return {k:p.key,arts:artByCluster[base]||0};}).filter(h=>h.arts<3).sort((a,b)=>a.arts-b.arts);
const summary = {
  totalFiles: files.length, indexable: indexable.length, noindex: arr.length-indexable.length,
  inSitemap: arr.filter(p=>p.inSitemap).length, clusters: Object.keys(clusters).length,
  articles: articles.length, totalWords: arr.reduce((s,p)=>s+p.wc,0),
  avgArticleWords: Math.round(articles.reduce((s,p)=>s+p.wc,0)/(articles.length||1)),
  orphans: orphans.length, veryThin: veryThin.length, thin: thin.length, weak: weak.length,
  brokenLinks: brokenList.length, notInSitemap: notInSitemap.length, noindexInSitemap: noindexInSitemap.length,
  deadSitemap: deadSitemap.length, noSchema: noSchema.length, ldFails: ldFails.length, dupTitles: dupTitles.length,
  filler: filler.length, stale: stale.length, sitemapTotal: sitemapKeys.size, withTool: arr.filter(p=>p.hasTool).length,
  noToolHubs: noToolHubs.length,
};

// ---------- history (append one snapshot/day, dedup by date) ----------
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });
const HIST_FILE = path.join(OUT_DIR, 'site-audit-history.json');
let history = [];
try { history = JSON.parse(fs.readFileSync(HIST_FILE,'utf8')); } catch(e){}
const snap = { date: today, files: summary.totalFiles, indexable: summary.indexable, articles: summary.articles,
  avgw: summary.avgArticleWords, broken: summary.brokenLinks, veryThin: summary.veryThin, thin: summary.thin,
  weak: summary.weak, filler: summary.filler, noidxSm: summary.noindexInSitemap, notInSm: summary.notInSitemap,
  stale: summary.stale, orphans: summary.orphans, tools: summary.withTool };
history = history.filter(h => h.date !== today);
history.push(snap);
history = history.slice(-180);
fs.writeFileSync(HIST_FILE, JSON.stringify(history));

// ---------- suggested fixes (data-driven) ----------
const brokenBy={}; brokenList.forEach(b=>{brokenBy[b.from]=(brokenBy[b.from]||0)+1;});
const brokenTop = Object.entries(brokenBy).sort((a,b)=>b[1]-a[1]).slice(0,10).map(e=>e[0]+'  ('+e[1]+' broken)');
const samp = (list,n) => list.slice(0,n||8).map(x=>x.k + (x.w!=null?'  ('+x.w+'w)':''));
const fixes=[];
if(summary.brokenLinks) fixes.push({pri:'NOW',effort:'Low',title:'Fix '+summary.brokenLinks+' broken internal links',how:'Largely resolved in PRs #49/#50 — merge them, then re-run this audit to confirm it drops to ~0. Worst offenders below.',sample:brokenTop});
if(summary.veryThin) fixes.push({pri:'NOW',effort:'Med',title:'Expand, merge, or prune '+summary.veryThin+' very-thin articles (<500w)',how:'Genuine articles only (calculators, index/card-grid, hubs and brochures are excluded). For each: expand to 1,000w+, merge into a stronger sibling, or 301/prune. Start by pruning the dated "wartime/inflation" set.',sample:samp(veryThin.map(p=>({k:p.key,w:p.wc})),12)});
if(summary.filler) fixes.push({pri:'NOW',effort:'Low',title:'Strip data-batch filler from '+summary.filler+' pages',how:'Empty/boilerplate H2 blocks that read as over-optimization. A deterministic strip pass exists; PR #49 covers most.',sample:samp(filler.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.orphans) fixes.push({pri:'NOW',effort:'Low',title:'Reconnect '+summary.orphans+' orphan pages (0 inbound)',how:'Add a contextual link from the relevant hub/sibling so they are discoverable.',sample:samp(orphans.map(p=>({k:p.key})),10)});
if(summary.noindexInSitemap+summary.notInSitemap) fixes.push({pri:'SOON',effort:'Low',title:'Fix sitemap drift ('+summary.noindexInSitemap+' noindex in, '+summary.notInSitemap+' indexable missing)',how:'Remove noindex URLs from sitemap.xml and add the missing indexable pages. Keeps crawl signals clean.',sample:noindexInSitemap.map(p=>'(noindex-in) '+p.key).concat(notInSitemap.map(p=>'(missing) '+p.key)).slice(0,12)});
if(summary.thin) fixes.push({pri:'SOON',effort:'Med',title:'Deepen '+summary.thin+' lean articles (500-800w)',how:'Genuine articles only. Add a worked example, FAQ, or comparison table to push toward the 1,000w+ house standard.',sample:samp(thin.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.weak) fixes.push({pri:'SOON',effort:'Med',title:'Strengthen internal links to '+summary.weak+' weak pages (1-2 inbound)',how:'Add 1-2 contextual links each from stronger cluster pages. Do not over-optimize past ~3.',sample:samp(weak.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.stale) fixes.push({pri:'SOON',effort:'Low',title:'Refresh '+summary.stale+' stale articles',how:'Update figures, bump dateModified, add a tool/FAQ where it fits. Freshness helps both ranking and trust.',sample:samp(stale.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.noToolHubs) fixes.push({pri:'SOON',effort:'Med',title:'Add conversion tools to '+summary.noToolHubs+' hubs/landing pages',how:'Only '+summary.withTool+' pages have an interactive tool today. Inline calculators + prefilled apply CTAs are the AIO-proof lever that actually converts.',sample:samp(noToolHubs.map(p=>({k:p.key})),12)});
if(summary.noSchema) fixes.push({pri:'LATER',effort:'Low',title:'Add JSON-LD schema to '+summary.noSchema+' content pages',how:'Add BreadcrumbList + Article/FinancialService + FAQPage for AEO/GEO eligibility.',sample:samp(noSchema.map(p=>({k:p.key})),10)});

// ---------- opportunities ("things to go after") ----------
const opps=[];
if(hubGaps.length) opps.push({title:'Build article clusters for '+hubGaps.length+' shallow industry hubs',impact:hubGaps.length+' hubs',detail:'These industry hubs have fewer than 3 supporting articles. Add a 3-problem cluster each (same proven pattern as septic/towing) to build topical depth.',sample:hubGaps.slice(0,12).map(h=>h.k+'  ('+h.arts+' articles)')});
opps.push({title:'Net-new verticals (zero cannibalization by construction)',impact:'~9 clean gaps',detail:'Industries with no page yet — safe, additive ranking surface. Each = a hub + 3 problem-articles with apply CTAs.',sample:['welding & metal fabrication','catering','sign company','masonry','flooring','pool service & construction','demolition','pressure washing','IT / MSP','auto detailing']});
opps.push({title:'Commercial comparison / "best-X" pages',impact:'highest click-intent',detail:'"X vs Y" and "best X for [audience]" earn the few clicks AI Overviews leave on the table. Dedup hard against the existing Best-X set first.',sample:['best equipment financing for [trade]','term loan vs SBA for [use]','more lender-type head-to-heads','best working capital for [industry]']});
opps.push({title:'Factoring cluster Tier-2',impact:'depth + intent',detail:'Round out the invoice-factoring set (4 Tier-1 articles in flight) with vertical/specialty pieces.',sample:['medical / healthcare receivables factoring','government-contractor factoring (Assignment of Claims Act)','dedicated trucking/freight factoring (fuel advances, quick-pay)','staffing-agency factoring (dedicated)']});
opps.push({title:'Local geo + industry landing pages',impact:'least AIO-suppressed',detail:'City + service combos (e.g. "HVAC financing in Atlanta") capture high-intent local traffic. Extends the metro work already shipped.',sample:['metro x service combinations','more city pages where Atlanta validates','state hub deepening']});
opps.push({title:'Conversion funnel upgrades',impact:'revenue, not just traffic',detail:'Reorder the match form to ask loan details before contact info, add inline email micro-capture under calculators, and prefill from each page.',sample:['match.html step reorder (global — propose first)','email micro-capture under calc results','prefill ?type=&amount= on every calc CTA']});

// ---------- visual architecture (route-prefix breakdown into categories) ----------
const PRODUCTS = new Set(['equipment-financing','sba-loans','working-capital-loans','business-line-of-credit','commercial-real-estate-loans','business-term-loans','merchant-cash-advance','invoice-factoring','commercial-bridge-loans','revenue-based-financing','securities-based-lending','fix-and-flip','accounts-receivable-financing','inventory-financing','business-debt-relief','startup-financing']);
function archCat(c){
  if(/-business-financing$/.test(c)) return 'Industries (hubs + clusters)';
  if(PRODUCTS.has(c)) return 'Financing products';
  if(c==='equipment') return 'Equipment by type';
  if(/glossary|comparison|guide|^articles$|blog/.test(c)) return 'Guides & reference';
  if(c==='(root)') return 'Root pages';
  return 'Other sections';
}
const archMap={};
for(const o of clusterArr){ const cat=archCat(o.cluster); (archMap[cat]=archMap[cat]||[]).push({label:o.cluster==='(root)'?'/':('/'+o.cluster), n:o.n}); }
// root pages: break into type pills instead of one giant "(root)"
const rootByType={}; for(const p of arr){ if(p.cluster==='(root)') rootByType[p.type]=(rootByType[p.type]||0)+1; }
archMap['Root pages']=Object.entries(rootByType).map(([t,n])=>({label:t,n})).sort((a,b)=>b.n-a.n);
const ARCH_ORDER=['Financing products','Industries (hubs + clusters)','Equipment by type','Guides & reference','Root pages','Other sections'];
const arch=ARCH_ORDER.filter(c=>archMap[c]).map(cat=>({cat, items: archMap[cat].sort((a,b)=>b.n-a.n)}));

const DATA = { summary, stamp, pages: arr, clusterArr, typeDist, hist, history, fixes, opps, arch, lists: {
  orphans: orphans.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.k.localeCompare(b.k)),
  veryThin: veryThin.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.w-b.w),
  thin: thin.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.w-b.w),
  weak: weak.map(p=>({k:p.key,t:p.type,w:p.wc,i:p.inbound})),
  broken: brokenList,
  notInSitemap: notInSitemap.map(p=>({k:p.key,t:p.type})),
  noindexInSitemap: noindexInSitemap.map(p=>({k:p.key})),
  deadSitemap,
  noSchema: noSchema.map(p=>({k:p.key,t:p.type})),
  ldFails: ldFails.map(p=>({k:p.key,n:p.ldFail})),
  dupTitles: dupTitles.map(([t,v])=>({t,v})),
  filler: filler.map(p=>({k:p.key,w:p.wc})),
  stale: stale.map(p=>({k:p.key,m:p.mod||'none',w:p.wc})).sort((a,b)=>(a.m||'').localeCompare(b.m||'')),
}};

// ---------- render ----------
const CSS = `
:root{--bg:#0b1626;--bg2:#101f33;--card:#13243b;--card2:#172b46;--line:#22405f;--tx:#e6eef7;--tx2:#9fb3c8;--cy:#7dd3fc;--bl:#2d7fb8;--good:#22c55e;--warn:#f59e0b;--bad:#ef4444}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,-apple-system,Segoe UI,sans-serif;background:var(--bg);color:var(--tx);line-height:1.5;padding:0 0 80px}
a{color:var(--cy);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:none;margin:0 auto;padding:0 40px}
header.hd{background:linear-gradient(135deg,#0d1f3c,#1e3a5f);padding:34px 0 28px;border-bottom:1px solid var(--line);margin-bottom:26px}
.hd h1{font-size:2.1rem;font-weight:800;letter-spacing:-.02em;margin-top:14px}
.hd .lede{color:var(--tx2);margin-top:12px;font-size:.98rem;max-width:780px;line-height:1.6}
.hd .lede b{color:var(--tx)}
.badge{display:inline-block;background:#0b1626;border:1px solid var(--line);color:var(--cy);border-radius:20px;padding:3px 12px;font-size:.78rem;margin-right:8px;margin-top:10px}
.pillbadge{display:inline-flex;align-items:center;gap:7px;border-radius:20px;padding:5px 13px;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-right:10px}
.pb-green{background:rgba(34,197,94,.12);border:1px solid rgba(34,197,94,.4);color:#86efac}
.pb-gen{background:rgba(125,211,252,.08);border:1px solid var(--line);color:var(--tx2)}
.pb-gen .dot{width:8px;height:8px;border-radius:50%;background:var(--good);box-shadow:0 0 8px var(--good)}
.toptabs{display:flex;gap:6px;border-bottom:1px solid var(--line);margin:22px 0 6px}
.toptab{padding:11px 18px;cursor:pointer;font-size:.95rem;font-weight:600;color:var(--tx2);border-bottom:2px solid transparent;margin-bottom:-1px}
.toptab.on{color:var(--cy);border-bottom-color:var(--cy)}
.tabpane{display:none}.tabpane.on{display:block}
header.hd{position:relative}
.dlbtn{position:absolute;top:22px;right:40px;appearance:none;cursor:pointer;border:1px solid var(--cy);background:rgba(125,211,252,.12);color:var(--cy);font:700 .8rem Inter,sans-serif;padding:9px 16px;border-radius:9px;display:inline-flex;align-items:center;gap:8px;white-space:nowrap}
.dlbtn:hover{background:rgba(125,211,252,.22)}
.dlbtn svg{width:15px;height:15px}
@media print{
  @page{size:A3 landscape;margin:11mm}
  *{-webkit-print-color-adjust:exact !important;print-color-adjust:exact !important}
  html,body{background:var(--bg) !important}
  .toptabs,.dlbtn,.tabs{display:none !important}
  .tabpane{display:block !important}
  .tabpane+.tabpane{page-break-before:always}
  .panel,[style*="max-height"]{max-height:none !important;overflow:visible !important}
  h2.sec{page-break-after:avoid}
  .arch-card,.fixcard,.good-li,tr{page-break-inside:avoid}
}
.arch-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:820px){.arch-grid{grid-template-columns:1fr}}
.arch-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.arch-card h3{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--tx2);margin-bottom:12px}
.routepill{display:inline-flex;align-items:center;gap:6px;background:#0b1626;border:1px solid var(--line);border-radius:8px;padding:5px 10px;margin:0 7px 8px 0;font-size:.82rem;font-family:ui-monospace,Menlo,monospace}
.routepill .ct{background:rgba(125,211,252,.14);color:var(--cy);border-radius:6px;padding:0 6px;font-weight:700;font-family:Inter,sans-serif}
h2.sec{font-size:1.25rem;font-weight:700;margin:38px 0 6px;padding-top:10px}
.sub{color:var(--tx2);font-size:.9rem;margin-bottom:16px;max-width:900px}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi .v{font-size:1.7rem;font-weight:800}.kpi .l{color:var(--tx2);font-size:.78rem;margin-top:3px}
.kpi.good .v{color:var(--good)}.kpi.warn .v{color:var(--warn)}.kpi.bad .v{color:var(--bad)}.kpi.neu .v{color:var(--cy)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px}@media(max-width:820px){.grid2{grid-template-columns:1fr}}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{text-align:left;padding:7px 9px;border-bottom:1px solid var(--line)}
th{color:var(--tx2);font-weight:600;cursor:pointer;user-select:none;position:sticky;top:0;background:var(--card2)}
th:hover{color:var(--cy)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tr:hover td{background:rgba(125,211,252,.05)}
.bar{height:20px;background:linear-gradient(90deg,var(--bl),var(--cy));border-radius:4px}
.barrow{display:flex;align-items:center;gap:10px;margin:5px 0;font-size:.82rem}
.barrow .lab{width:130px;color:var(--tx2);flex:none;text-align:right}
.barrow .n{width:46px;flex:none;font-variant-numeric:tabular-nums}
.barwrap{flex:1;background:#0b1626;border-radius:4px}
.tabs{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.tab{background:var(--card);border:1px solid var(--line);color:var(--tx2);border-radius:8px;padding:7px 12px;cursor:pointer;font-size:.83rem}
.tab.on{background:var(--bl);color:#fff;border-color:var(--bl)}
.tab .c{display:inline-block;background:rgba(0,0,0,.25);border-radius:10px;padding:0 7px;margin-left:6px;font-size:.75rem}
.tab.crit .c{background:var(--bad);color:#fff}.tab.warnc .c{background:var(--warn);color:#0b1626}
.list{max-height:430px;overflow:auto;border:1px solid var(--line);border-radius:8px}
.pill{display:inline-block;font-size:.7rem;padding:1px 7px;border-radius:10px;background:#0b1626;border:1px solid var(--line);color:var(--tx2)}
.flag{font-size:.68rem;padding:1px 6px;border-radius:6px;margin-right:3px}
.f-bad{background:rgba(239,68,68,.16);color:#fca5a5}.f-warn{background:rgba(245,158,11,.16);color:#fcd34d}.f-good{background:rgba(34,197,94,.16);color:#86efac}
.controls{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}
input,select{background:#0b1626;border:1px solid var(--line);color:var(--tx);border-radius:8px;padding:8px 11px;font-size:.85rem}
input{min-width:240px}
.note{background:rgba(245,158,11,.1);border-left:3px solid var(--warn);padding:12px 16px;border-radius:8px;margin:14px 0;font-size:.9rem;color:#fcd34d}
.good-li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 16px;margin-bottom:10px;font-size:.9rem}
.good-li b{color:var(--good)}
.fixcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:10px}
.fixhead{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.fixhead b{font-size:.95rem}
.eff{margin-left:auto;font-size:.72rem;color:var(--tx2);background:#0b1626;border:1px solid var(--line);border-radius:10px;padding:2px 8px}
.tag{font-size:.7rem;padding:2px 8px;border-radius:10px;font-weight:700}
.t-now{background:var(--bad);color:#fff}.t-soon{background:var(--warn);color:#0b1626}.t-later{background:var(--bl);color:#fff}
.trendgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:12px}
details summary{cursor:pointer}
.muted{color:var(--tx2)}
code{background:#0b1626;padding:1px 6px;border-radius:5px;color:var(--cy);font-size:.85em}
/* Start Here: plain-English Fix / Improve / Grow */
.sh-intro{font-size:.95rem;color:var(--tx2);line-height:1.65;max-width:880px;margin:18px 0 0}.sh-intro b{color:var(--tx)}
.sh-verdict{display:flex;align-items:center;gap:12px;margin-top:16px;padding:15px 18px;border-radius:12px;border:1px solid var(--line);background:var(--card);flex-wrap:wrap}
.sh-verdict.good{border-left:4px solid var(--good)}.sh-verdict.attn{border-left:4px solid var(--warn)}
.sh-verdict .vh{font-size:1.15rem;font-weight:800}.sh-verdict.good .vh{color:var(--good)}.sh-verdict.attn .vh{color:var(--warn)}
.sh-verdict .vsub{font-size:.85rem;color:var(--tx2)}
.sh-sec{margin-top:26px}
.sh-sechead{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}.sh-sechead h2{margin:0;font-size:1.2rem}
.sh-sechead .cnt{font-size:.72rem;font-weight:800;padding:2px 10px;border-radius:20px}
.sh-fix .cnt{color:#fca5a5;background:rgba(239,68,68,.16)}.sh-improve .cnt{color:#fcd34d;background:rgba(245,158,11,.16)}.sh-grow .cnt{color:var(--cy);background:rgba(125,211,252,.14)}
.sh-sechead .blurb{font-size:.83rem;color:var(--tx2)}
.sh-cards{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:13px}@media(max-width:900px){.sh-cards{grid-template-columns:1fr}}
.sh-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px 17px;border-left:3px solid var(--line);cursor:pointer;transition:border-color .12s,transform .12s,box-shadow .12s}
.sh-card:hover{border-color:var(--cy);transform:translateY(-1px);box-shadow:0 6px 18px rgba(0,0,0,.25)}
.sh-card:focus-visible{outline:2px solid var(--cy);outline-offset:2px}
.sh-more{margin-top:10px;font-size:.74rem;font-weight:700;color:var(--cy);opacity:.85}
.shmodal{position:fixed;inset:0;background:rgba(3,8,15,.7);display:none;align-items:flex-start;justify-content:center;padding:6vh 20px;z-index:100;overflow:auto}
.shmodal.on{display:flex}
.shmodal-box{background:var(--card);border:1px solid var(--line);border-radius:16px;max-width:680px;width:100%;padding:26px 30px 30px;position:relative;box-shadow:0 24px 70px rgba(0,0,0,.55)}
.shmodal-x{position:absolute;top:12px;right:16px;background:none;border:0;color:var(--tx2);font-size:1.7rem;line-height:1;cursor:pointer}.shmodal-x:hover{color:var(--tx)}
.shmodal-tag{font-size:.72rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--cy)}
.shmodal-title{font-size:1.3rem;margin:8px 36px 0 0;color:var(--tx);line-height:1.3}
.shmodal-h{font-size:.7rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--tx2);margin:18px 0 7px}
.shmodal-body{font-size:.95rem;line-height:1.65;color:var(--tx)}
.shmodal-list{display:flex;flex-wrap:wrap;gap:6px}
.shmodal-list code{font-size:.78rem;font-family:ui-monospace,Menlo,monospace;background:#0b1626;border:1px solid var(--line);border-radius:5px;padding:2px 7px;color:var(--cy)}
.sh-fix .sh-card{border-left-color:var(--bad)}.sh-improve .sh-card{border-left-color:var(--warn)}.sh-grow .sh-card{border-left-color:var(--cy)}
.sh-card .t{font-size:.97rem;font-weight:700;color:var(--tx);line-height:1.4}
.sh-card .row{margin-top:9px;font-size:.85rem;color:var(--tx2);line-height:1.55;display:grid;grid-template-columns:58px 1fr;gap:10px}
.sh-card .row .k{font-size:.62rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--tx2);padding-top:2px}
.sh-card .row.do .v{color:var(--tx)}.sh-card .row.do .k{color:var(--cy)}
.sh-empty{margin-top:13px;padding:15px 18px;border-radius:12px;background:rgba(34,197,94,.1);border:1px solid rgba(34,197,94,.3);color:var(--tx);font-size:.9rem}.sh-empty b{color:var(--good)}
.sh-gloss{margin-top:30px;border-top:1px solid var(--line);padding-top:16px}
.sh-gloss>summary{cursor:pointer;font-size:.9rem;font-weight:700;color:var(--cy);list-style:none}
.sh-gloss>summary::-webkit-details-marker{display:none}.sh-gloss>summary::before{content:"▸ ";color:var(--tx2)}.sh-gloss[open]>summary::before{content:"▾ "}
.sh-gloss dl{margin:14px 0 0;display:grid;grid-template-columns:180px 1fr;gap:8px 18px;font-size:.85rem}
.sh-gloss dt{font-weight:700;color:var(--tx)}.sh-gloss dd{margin:0;color:var(--tx2)}
@media(max-width:760px){.sh-gloss dl{grid-template-columns:1fr;gap:2px 0}.sh-gloss dd{margin:0 0 8px}}
.techwrap{margin-top:28px;border-top:1px solid var(--line)}
.techwrap>summary{cursor:pointer;list-style:none;padding:16px 0 4px;font-size:.92rem;font-weight:700;color:var(--tx2)}
.techwrap>summary::-webkit-details-marker{display:none}.techwrap>summary::before{content:"▸ ";color:var(--tx2)}.techwrap[open]>summary::before{content:"▾ "}
.techwrap>summary:hover{color:var(--tx)}.techwrap .techhint{font-size:.8rem;color:var(--tx2);font-weight:400;margin-left:6px}
.sh-focus{margin-top:16px;padding:15px 18px;border-radius:12px;background:rgba(125,211,252,.08);border:1px solid var(--cy);border-left:4px solid var(--cy)}
.sh-focus-h{font-size:.95rem;font-weight:800;color:var(--cy)}
.sh-focus-sub{font-size:.7rem;font-weight:600;color:var(--tx2);margin-left:8px}
.sh-focus-list{margin:10px 0 0;padding-left:22px}.sh-focus-list li{font-size:.92rem;color:var(--tx);margin:6px 0;line-height:1.5}
.scoreboard{margin-top:13px;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.scoreboard table{width:100%;border-collapse:collapse;font-size:.85rem}
.scoreboard th,.scoreboard td{text-align:left;padding:9px 14px;border-bottom:1px solid var(--line)}
.scoreboard th{font-size:.68rem;letter-spacing:.05em;text-transform:uppercase;color:var(--tx2);font-weight:700}
.scoreboard td.ax,.scoreboard th.ax{text-align:center}
.scoreboard tr:last-child td{border-bottom:0}
.sdot{display:inline-block;font-weight:800;font-size:.95rem}.sdot.ok{color:var(--good)}.sdot.mid{color:var(--warn)}.sdot.no{color:var(--bad)}
.scoreboard .miss{color:var(--tx2);font-size:.8rem}
.axhead{display:flex;flex-direction:column;gap:1px}.axhead small{font-size:.6rem;color:var(--tx2);font-weight:600;text-transform:none;letter-spacing:0}
.sgrid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:12px 0 16px}@media(max-width:820px){.sgrid3{grid-template-columns:1fr}}
@media print{.sh-card,.sh-verdict,.sh-focus,.scoreboard tr{break-inside:avoid}.sh-gloss,.techwrap{break-inside:avoid}.techwrap>summary{display:none}}
`;

const JS = [
"var P=DATA.pages, S=DATA.summary;",
"function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;');}",
"function kpi(v,l,cls){return '<div class=\"kpi '+(cls||'')+'\"><div class=\"v\">'+v+'</div><div class=\"l\">'+l+'</div></div>';}",
"document.getElementById('kpis').innerHTML=[",
" kpi(S.totalFiles,'HTML pages','neu'),kpi(S.indexable,'Indexable','neu'),kpi(S.inSitemap+' / '+S.sitemapTotal,'In sitemap','neu'),",
" kpi(S.clusters,'Clusters/sections','neu'),kpi(S.articles,'Articles','neu'),kpi(S.avgArticleWords,'Avg article words',S.avgArticleWords>=1000?'good':'warn'),",
" kpi(S.dupTitles,'Duplicate titles',S.dupTitles?'bad':'good'),kpi(S.orphans,'Orphans (0 inbound)',S.orphans>5?'bad':'good'),",
" kpi(S.brokenLinks,'Broken internal links',S.brokenLinks?'bad':'good'),kpi(S.veryThin,'Very thin articles',S.veryThin>20?'bad':'warn'),",
" kpi(S.thin,'Thin articles',S.thin>50?'warn':'good'),kpi(S.weak,'Weak links (1-2 inb)','warn'),",
" kpi(S.notInSitemap,'Not in sitemap',S.notInSitemap?'warn':'good'),kpi(S.noindexInSitemap,'Noindex in sitemap',S.noindexInSitemap?'warn':'good'),",
" kpi(S.filler,'data-batch filler',S.filler?'warn':'good'),kpi(S.stale,'Stale articles',S.stale?'warn':'good'),",
" kpi(S.noSchema,'Missing schema',S.noSchema?'warn':'good'),kpi(S.withTool,'Pages w/ tool','neu')",
"].join('');",
"var cl=DATA.clusterArr, cSort={k:'n',d:-1};",
"function renderCl(){var rows=cl.slice().sort(function(a,b){var x=a[cSort.k],y=b[cSort.k];if(typeof x==='string'){return cSort.d*x.localeCompare(y);}return cSort.d*(x-y);});",
" var h='<table><thead><tr>'+['cluster|Cluster','n|Pages','avgw|Avg words','thin|Thin','orphan|Orphans','avgInb|Avg inbound','inSm|In sitemap','broken|Broken'].map(function(c){var p=c.split('|');return '<th data-k=\"'+p[0]+'\" class=\"'+(p[0]==='cluster'?'':'num')+'\">'+p[1]+'</th>';}).join('')+'</tr></thead><tbody>';",
" rows.forEach(function(o){h+='<tr><td>'+esc(o.cluster)+'</td><td class=num>'+o.n+'</td><td class=num>'+o.avgw+'</td><td class=num>'+(o.thin||'')+'</td><td class=num>'+(o.orphan||'')+'</td><td class=num>'+o.avgInb+'</td><td class=num>'+o.inSm+'</td><td class=num>'+(o.broken||'')+'</td></tr>';});",
" document.getElementById('cltbl').innerHTML=h+'</tbody></table>';",
" document.querySelectorAll('#cltbl th').forEach(function(t){t.onclick=function(){var k=t.getAttribute('data-k');cSort.d=(cSort.k===k?-cSort.d:-1);cSort.k=k;renderCl();};});}",
"renderCl();",
"function bars(id,items){var m=Math.max.apply(null,items.map(function(i){return i.n;}));document.getElementById(id).innerHTML=items.map(function(i){var w=(i.n/m*100).toFixed(1);return '<div class=barrow><div class=lab>'+esc(i.label)+'</div><div class=barwrap><div class=bar style=\"width:'+w+'%\"></div></div><div class=n>'+i.n+'</div></div>';}).join('');}",
"bars('typedist',Object.keys(DATA.typeDist).map(function(k){return {label:k,n:DATA.typeDist[k]};}).sort(function(a,b){return b.n-a.n;}));",
"bars('hist',DATA.hist.map(function(b){return {label:b.label+' w',n:b.n};}));",
// fixes + opps
"function fcard(f){var s=f.sample&&f.sample.length?'<details style=\"margin-top:8px\"><summary class=muted style=\"font-size:.8rem\">'+f.sample.length+' example pages</summary><div style=\"font-size:.78rem;color:var(--tx2);margin-top:6px;line-height:1.8;font-family:monospace\">'+f.sample.map(esc).join('<br>')+'</div></details>':'';return '<div class=fixcard><div class=fixhead><span class=\"tag t-'+f.pri.toLowerCase()+'\">'+f.pri+'</span><b>'+esc(f.title)+'</b><span class=eff>'+f.effort+' effort</span></div><div class=muted style=\"font-size:.85rem;margin-top:6px\">'+esc(f.how)+'</div>'+s+'</div>';}",
"document.getElementById('fixes').innerHTML=DATA.fixes.map(fcard).join('')||'<div class=good-li>No open issues — clean.</div>';",
"document.getElementById('opps').innerHTML=DATA.opps.map(function(o){var s=o.sample&&o.sample.length?'<div style=\"font-size:.8rem;color:var(--tx2);margin-top:8px;line-height:1.8\">'+o.sample.map(function(x){return '&bull; '+esc(x);}).join('<br>')+'</div>':'';return '<div class=fixcard><div class=fixhead><b>'+esc(o.title)+'</b><span class=eff>'+esc(o.impact)+'</span></div><div class=muted style=\"font-size:.85rem;margin-top:6px\">'+esc(o.detail)+'</div>'+s+'</div>';}).join('');",
// trends
"var H=DATA.history;",
"function spark(vals){if(!vals||vals.length<2)return '<span class=muted style=\"font-size:.72rem\">collecting&hellip; (need 2+ runs)</span>';var mn=Math.min.apply(null,vals),mx=Math.max.apply(null,vals),r=(mx-mn)||1,w=170,h=34;var pts=vals.map(function(v,i){return (i/(vals.length-1)*w).toFixed(1)+','+(h-((v-mn)/r)*h).toFixed(1);}).join(' ');return '<svg width='+w+' height='+h+' style=\"display:block\"><polyline points=\"'+pts+'\" fill=none stroke=\"#7dd3fc\" stroke-width=2 stroke-linejoin=round stroke-linecap=round /></svg>';}",
"var METR=[['broken','Broken links',1],['thin','Thin 500-800',1],['veryThin','Very thin',1],['filler','Filler',1],['weak','Weak inbound',1],['stale','Stale',1],['articles','Articles',0],['tools','Pages w/ tool',0]];",
"document.getElementById('trendcards').innerHTML=METR.map(function(m){var vals=H.map(function(h){return h[m[0]];}).filter(function(v){return v!=null;});var last=vals.length?vals[vals.length-1]:0,prev=vals.length>1?vals[vals.length-2]:null;var d=prev==null?'':last-prev;var col=d===''?'var(--tx2)':((m[2]?(d<0):(d>0))?'var(--good)':(d===0?'var(--tx2)':'var(--bad)'));var dt=d===''?'&middot;':(d>0?'\\u25b2'+d:(d<0?'\\u25bc'+Math.abs(d):'\\u2014'));return '<div class=kpi><div style=\"display:flex;justify-content:space-between;align-items:baseline\"><div class=v style=\"font-size:1.3rem\">'+last+'</div><div style=\"font-size:.8rem;color:'+col+'\">'+dt+'</div></div><div class=l>'+m[1]+'</div><div style=\"margin-top:8px\">'+spark(vals)+'</div></div>';}).join('');",
"var hcols=[['date','Date'],['files','Pages'],['articles','Articles'],['broken','Broken'],['veryThin','VThin'],['thin','Thin'],['weak','Weak'],['filler','Filler'],['stale','Stale'],['tools','Tools']];",
"var hh='<table><thead><tr>'+hcols.map(function(c){return '<th'+(c[0]==='date'?'':' class=num')+'>'+c[1]+'</th>';}).join('')+'</tr></thead><tbody>';H.slice().reverse().forEach(function(r){hh+='<tr>'+hcols.map(function(c){return '<td'+(c[0]==='date'?'':' class=num')+'>'+(r[c[0]]==null?'':r[c[0]])+'</td>';}).join('')+'</tr>';});document.getElementById('histtbl').innerHTML=hh+'</tbody></table>';",
// issues tabs
"var L=DATA.lists;",
"function listKW(a){return a.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span> <span class=pill>'+p.w+'w</span>');}).join('');}",
"function row(k,meta){return '<div style=\"display:flex;justify-content:space-between;gap:10px;padding:7px 12px;border-bottom:1px solid var(--line);font-size:.82rem\"><span>'+esc(k)+'</span><span style=flex:none>'+meta+'</span></div>';}",
"var TABS=[",
" {name:'Broken links',crit:1,n:L.broken.length,render:function(){var by={};L.broken.forEach(function(b){(by[b.from]=by[b.from]||[]).push(b.href);});return Object.keys(by).sort().map(function(f){return '<div style=\"padding:8px 12px;border-bottom:1px solid var(--line)\"><b>'+esc(f)+'</b> <span class=muted>('+by[f].length+')</span><br><span class=muted style=\"font-size:.8rem\">'+by[f].map(esc).join(' &middot; ')+'</span></div>';}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Very thin articles',crit:1,n:L.veryThin.length,render:function(){return listKW(L.veryThin);}},",
" {name:'Thin articles',warnc:1,n:L.thin.length,render:function(){return listKW(L.thin);}},",
" {name:'Weak (1-2 inbound)',warnc:1,n:L.weak.length,render:function(){return L.weak.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span> <span class=pill>'+p.w+'w</span> <span class=pill>'+p.i+' inbound</span>');}).join('');}},",
" {name:'Orphans',crit:1,n:L.orphans.length,render:function(){return listKW(L.orphans)||'<div style=padding:14px>None.</div>';}},",
" {name:'Not in sitemap',warnc:1,n:L.notInSitemap.length,render:function(){return L.notInSitemap.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Noindex in sitemap',warnc:1,n:L.noindexInSitemap.length,render:function(){return L.noindexInSitemap.map(function(p){return row(p.k,'');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'data-batch filler',warnc:1,n:L.filler.length,render:function(){return L.filler.map(function(p){return row(p.k,'<span class=pill>'+p.w+'w</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Stale articles',warnc:1,n:L.stale.length,render:function(){return L.stale.map(function(p){return row(p.k,'<span class=pill>mod '+p.m+'</span> <span class=pill>'+p.w+'w</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Missing schema',warnc:1,n:L.noSchema.length,render:function(){return L.noSchema.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Duplicate titles',n:L.dupTitles.length,render:function(){return L.dupTitles.length?L.dupTitles.map(function(d){return '<div style=\"padding:8px 12px;border-bottom:1px solid var(--line)\"><b>'+esc(d.t)+'</b><br>'+d.v.map(esc).join('<br>')+'</div>';}).join(''):'<div style=padding:14px>None &mdash; clean.</div>';}}",
"];",
"var panelEl=document.getElementById('tabpanel');",
"document.getElementById('tabs').innerHTML=TABS.map(function(t,i){return '<div class=\"tab'+(i===0?' on':'')+(t.crit?' crit':'')+(t.warnc?' warnc':'')+'\" data-i=\"'+i+'\">'+t.name+'<span class=c>'+t.n+'</span></div>';}).join('');",
"function showTab(i){panelEl.innerHTML='<div class=list>'+(TABS[i].render()||'<div style=padding:14px>None.</div>')+'</div>';document.querySelectorAll('#tabs .tab').forEach(function(t,j){t.classList.toggle('on',j==i);});}",
"document.querySelectorAll('#tabs .tab').forEach(function(t){t.onclick=function(){showTab(+t.getAttribute('data-i'));};});showTab(0);",
"var eSort={k:'wc',d:-1};",
"function flags(p){var f=[];if(p.inbound===0&&!/^\\/(index)?$/.test(p.key))f.push('<span class=\"flag f-bad\">orphan</span>');if(p.wc<500)f.push('<span class=\"flag f-bad\">thin</span>');else if(p.wc<800)f.push('<span class=\"flag f-warn\">lean</span>');if(p.broken.length)f.push('<span class=\"flag f-bad\">'+p.broken.length+' broken</span>');if(p.noindex)f.push('<span class=\"flag f-warn\">noindex</span>');if(!p.inSitemap)f.push('<span class=\"flag f-warn\">no-sitemap</span>');if(p.dataBatch)f.push('<span class=\"flag f-warn\">filler</span>');if(p.schema.length===0)f.push('<span class=\"flag f-warn\">no-schema</span>');if(p.hasTool)f.push('<span class=\"flag f-good\">tool</span>');return f.join('');}",
"function renderEx(){var q=document.getElementById('q').value.toLowerCase();var ft=document.getElementById('ft').value;",
" var rows=P.filter(function(p){return (!q||p.key.toLowerCase().indexOf(q)>=0||(p.title||'').toLowerCase().indexOf(q)>=0)&&(!ft||p.type===ft);});",
" rows.sort(function(a,b){var x=a[eSort.k],y=b[eSort.k];if(typeof x==='string')return eSort.d*x.localeCompare(y);return eSort.d*((x||0)-(y||0));});",
" document.getElementById('excount').textContent=rows.length+' pages';",
" var h='<table><thead><tr>'+['key|Page','type|Type','wc|Words','inbound|Inbound','schema|Schema','x|Flags'].map(function(c){var p=c.split('|');return '<th data-k=\"'+p[0]+'\" class=\"'+(/wc|inbound/.test(p[0])?'num':'')+'\">'+p[1]+'</th>';}).join('')+'</tr></thead><tbody>';",
" rows.slice(0,400).forEach(function(p){h+='<tr><td>'+esc(p.key)+'</td><td><span class=pill>'+p.type+'</span></td><td class=num>'+p.wc+'</td><td class=num>'+p.inbound+'</td><td class=num>'+p.schema.length+'</td><td>'+flags(p)+'</td></tr>';});",
" h+='</tbody></table>';if(rows.length>400)h+='<div class=muted style=padding:10px>Showing first 400 of '+rows.length+'.</div>';",
" document.getElementById('extbl').innerHTML=h;",
" document.querySelectorAll('#extbl th').forEach(function(t){t.onclick=function(){var k=t.getAttribute('data-k');eSort.d=(eSort.k===k?-eSort.d:-1);eSort.k=k;renderEx();};});}",
"document.getElementById('q').oninput=renderEx;document.getElementById('ft').onchange=renderEx;",
"document.getElementById('ft').innerHTML='<option value=\"\">All types</option>'+Object.keys(DATA.typeDist).sort().map(function(t){return '<option>'+t+'</option>';}).join('');",
"renderEx();",
// visual architecture pills
"document.getElementById('arch').innerHTML=DATA.arch.map(function(g){var pills=g.items.map(function(i){return '<span class=routepill>'+esc(i.label)+'<span class=ct>'+i.n+'</span></span>';}).join('');return '<div class=arch-card><h3>'+esc(g.cat)+'</h3>'+pills+'</div>';}).join('');",
// top-level tab switching
"document.querySelectorAll('.toptab').forEach(function(t){t.onclick=function(){var p=t.getAttribute('data-pane');document.querySelectorAll('.toptab').forEach(function(x){x.classList.toggle('on',x===t);});document.querySelectorAll('.tabpane').forEach(function(pane){pane.classList.toggle('on',pane.id==='pane-'+p);});window.scrollTo(0,0);};});"
].join("\n");

// ---------- GSC performance pane (static snapshot from the 2026-06-18 Search Console pull, 7-day window) ----------
// Hand-maintained: this generator crawls the codebase, not GSC. Update these figures when a fresh
// Search Console export is dropped (window/totals/tables below), then re-run the audit.
const gscRow = (u, imp, clk, pos) => '<tr><td style="font-family:ui-monospace,Menlo,monospace;font-size:.8rem">'+u+'</td><td class=num>'+imp+'</td><td class=num>'+clk+'</td><td class=num>'+pos+'</td></tr>';
const gscPane =
'<div class="note" style="border-left-color:var(--warn);background:rgba(245,158,11,.1);color:#fcd34d"><b>Headline &mdash; recovery holding; the CTR leak is still the core problem.</b> The last 7 days (Jun 10&ndash;16) pulled <b>~6,631 impressions</b> and <b>31 clicks</b> &mdash; CTR <b>~0.47%</b>, up from the 28-day 0.33%, with avg position tightening to <b>~19</b> (from ~21). Rankings are fine; <b>AI Overviews / Google AI Mode</b> still answer most queries in-SERP so the click never happens. Source: GSC export dated <b>2026-06-18</b>, window <b>Last 7 days (Jun 10 &ndash; Jun 16)</b>.</div>'+
'<div class=kpis>'+
'<div class="kpi neu"><div class=v>~6.6k</div><div class=l>Impressions (7d)</div></div>'+
'<div class="kpi warn"><div class=v>31</div><div class=l>Clicks (7d)</div></div>'+
'<div class="kpi warn"><div class=v>0.47%</div><div class=l>Site-wide CTR (was 0.33%)</div></div>'+
'<div class="kpi good"><div class=v>~19</div><div class=l>Avg position (was ~21)</div></div>'+
'<div class="kpi bad"><div class=v>321&rarr;0</div><div class=l>Top page impr&rarr;clicks @ pos 3.8</div></div>'+
'</div>'+
'<h2 class=sec>Where the clicks are leaking &mdash; high impressions, ~0 clicks</h2>'+
'<div class=sub>Pages ranking well but barely clicked. The calculator guide at position 3.8 with 321 impressions and zero clicks is the textbook signature of AI-answer cannibalization &mdash; not a ranking issue. The bright spot, the <code>carecredit-vs-patientfi</code> comparison page at 3 clicks, shows what survives: "vs", "rates", and concrete-data pages.</div>'+
'<div class=panel style="overflow:auto"><table><thead><tr><th>Page</th><th class=num>Impr.</th><th class=num>Clicks</th><th class=num>Position</th></tr></thead><tbody>'+
gscRow('/commercial-real-estate-loans/&hellip;/how-much-down-payment-required-commercial-property-loan','491','1','12.43')+
gscRow('/equipment-financing/&hellip;/carecredit-vs-patientfi-imaging-radiology','332','<b style="color:var(--good)">3</b>','19.09')+
gscRow('/business-loan-calculator-guide','321','<b style="color:var(--bad)">0</b>','3.77')+
gscRow('/commercial-real-estate-loans/&hellip;/multifamily-loan-down-payment','203','0','8.94')+
gscRow('/business-line-of-credit/&hellip;/what-are-typical-business-line-of-credit-rates','178','<b style="color:var(--bad)">0</b>','37.05')+
gscRow('/business-line-of-credit/&hellip;/how-fast-can-you-get-approved-business-line-of-credit','154','0','9.09')+
'</tbody></table></div>'+
'<h2 class=sec>Recovery from the May 18 dilution event</h2>'+
'<div class=sub>Holding. Across Jun 10&ndash;16 daily clicks averaged <b>~4</b> (stable after the early-June 4&ndash;10 spike), impressions rose <b>925&rarr;1,313/day</b>, and avg position tightened from <b>18.3 to 15.6</b> over the week. Site-wide CTR ticked up to 0.47%. The cleanup-before-publishing strategy is working &mdash; <b>hold the freeze on new programmatic pages</b> until index count and position fully stabilize.</div>'+
'<h2 class=sec>Bridge loan cluster &mdash; detail</h2>'+
'<div class=sub>The full bridge cluster pulled only <b>~41 impressions and 1 click</b> in the last 7 days, and the hub (<code>/commercial-bridge-loans.html</code>) recorded <b>zero impressions</b> &mdash; authority for "commercial bridge loan" is still split across child URLs while the hub itself goes unseen (<b>keyword cannibalization</b>). The cluster is over-built relative to its search demand.</div>'+
'<div class=panel style="overflow:auto"><table><thead><tr><th>Bridge page</th><th class=num>Impr.</th><th class=num>Clicks</th><th class=num>Position</th></tr></thead><tbody>'+
gscRow('/commercial-bridge-loans/articles/5m-bridge-loan-multifamily-structure-closing-timeline','15','0','7.53')+
gscRow('/commercial-bridge-loans/articles/typical-commercial-bridge-loan-rates-2026','7','<b style="color:var(--good)">1</b>','6.00')+
gscRow('/commercial-bridge-loans/articles/when-should-you-use-commercial-bridge-loan','7','0','5.14')+
gscRow('/commercial-bridge-loans/articles/bridge-loan-pay-off-construction-debt','4','0','8.25')+
gscRow('/commercial-bridge-loans/articles/what-do-lenders-look-for-commercial-bridge-loan','4','0','20.00')+
gscRow('/commercial-bridge-loans/articles/bridge-loan-pitfalls-what-can-go-wrong','2','0','11.00')+
gscRow('/commercial-bridge-loans/articles/bridge-loan-value-add-commercial-property','1','0','3.00')+
gscRow('/commercial-bridge-loans/articles/construction-loan-vs-bridge-loan','1','0','66.00')+
gscRow('<b>/commercial-bridge-loans.html &nbsp;(HUB)</b>','<b style="color:var(--bad)">0</b>','0','&mdash;')+
'</tbody></table></div>'+
'<h2 class=sec>What "more agency on bridge" should mean &mdash; not more pages</h2>'+
'<div class=fixcard><div class=fixhead><span class="tag t-now">NOW</span><b>Fix the hub cannibalization</b><span class=eff>~1 hr</span></div><div class=muted style="font-size:.85rem;margin-top:6px">The hub pulled <b>0 impressions</b> while child articles ranked &mdash; Google is ignoring it entirely. Find which bridge URL ranks for core "commercial bridge loan" terms and consolidate intent onto the hub so authority stops splitting across child articles. Zero new URLs.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-now">NOW</span><b>Recover the BLoC rates page stuck on page 4</b><span class=eff>~30 min</span></div><div class=muted style="font-size:.85rem;margin-top:6px"><code>what-are-typical-business-line-of-credit-rates</code> pulled <b>178 impressions at position 37</b> with 0 clicks &mdash; a high-demand "rates" query buried on page 4. Rewrite title/meta to the seo-geo-aeo bar, add a dated 2026 rate table, and refresh.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-soon">SOON</span><b>Win AI-citation with data + tables</b><span class=eff>~half day</span></div><div class=muted style="font-size:.85rem;margin-top:6px">Port the rates-2026 page approach to the hub: a real comparison table (bridge vs hard money vs construction vs SBA &mdash; term / speed / LTV / rate) plus dated 2026 rate ranges. Tables and dated numbers get extracted and cited by AI engines.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-later">HOLD</span><b>No net-new bridge URLs yet</b><span class=eff>gated</span></div><div class=muted style="font-size:.85rem;margin-top:6px">Do not publish new bridge pages until the recovery gates clear (index count down, avg position up). Adding supply where there is little demand, mid-penalty, is the wrong lever.</div></div>'+
'<div class="good-li" style="margin-top:14px"><b>Bigger-picture priority:</b> bridge is high-ticket but low-volume (~41 impr/7d). The recoverable traffic is in CRE down-payment, the business-loan calculator guide, equipment, and "vs/comparison" queries &mdash; pages already pulling 150&ndash;500 impressions at near-zero CTR. Fixing CTR / AI-citation on those is the far larger prize. Fix bridge because deals are large; spend the most effort on the high-impression CTR leak.</div>'+
'<p class=muted style="margin-top:16px;font-size:.8rem">Static snapshot &mdash; figures hand-entered from the 2026-06-18 GSC export (7-day window; this dashboard crawls the codebase, not Search Console). Full write-up: <code>_analysis/GSC_ANALYSIS_2026-06-18.md</code>.</p>';

const Sx = summary;

// ---------- Start Here: plain-English Fix / Improve / Grow ----------
const eH = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---------- SEO / AEO / GEO readiness (from each page's parsed schema) ----------
// SEO = found in Google (in sitemap, linked, real content, has schema).
// AEO = answer-engine ready (FAQ / HowTo schema for answer boxes & "People also ask").
// GEO = AI-citation ready (a freshness date + article/service/FAQ schema AI can extract).
const contentPagesG = arr.filter(isContent);
const hasType = (p, t) => p.schema.includes(t);
const aeoReady = p => hasType(p, 'FAQPage') || hasType(p, 'HowTo');
const geoReady = p => !!p.mod && (hasType(p, 'Article') || hasType(p, 'FAQPage') || hasType(p, 'FinancialService') || hasType(p, 'HowTo'));
const seoReady = p => p.inSitemap && p.inbound > 0 && p.wc >= 500 && p.schema.length > 0 && !p.noindex;
// Only flag REAL indexable, sitemap-listed pages. Exclude noindex, non-sitemap includes
// (e.g. tools/article_supplements), meta-refresh redirects, and — for FAQ — list/card-grid
// index pages where FAQPage schema does not belong.
const aeoGapPages = contentPagesG.filter(p => !aeoReady(p) && !p.noindex && p.inSitemap && !p.redirect && !LIST_TYPES.has(p.type));
const geoGapPages = contentPagesG.filter(p => !p.mod && !p.noindex && p.inSitemap && !p.redirect);
// fold AEO/GEO gaps into the fixes list so they flow into Start Here + the fixes tab
if (aeoGapPages.length) fixes.push({ pri: 'SOON', effort: 'Med', title: aeoGapPages.length + ' content pages have no FAQ/Q&A schema (AEO)', how: 'Add an FAQ block + FAQPage schema so Google answer boxes and "People also ask" can lift the answer. Most of the site already has this — these are the stragglers.', sample: aeoGapPages.slice(0, 12).map(p => p.key) });
if (geoGapPages.length) fixes.push({ pri: 'SOON', effort: 'Low', title: geoGapPages.length + ' pages show no "last updated" date (GEO)', how: 'Add dateModified / article:modified_time so AI engines (Google AI Overviews, ChatGPT, Perplexity) trust and cite them. Freshness is the strongest GEO signal.', sample: geoGapPages.slice(0, 12).map(p => p.key) });
// per-content-type scorecard (% of pages in each type that are ready on each axis)
const byTypeG = {};
for (const p of contentPagesG) { const t = byTypeG[p.type] = byTypeG[p.type] || { type: p.type, n: 0, aeo: 0, geo: 0, seo: 0 }; t.n++; if (aeoReady(p)) t.aeo++; if (geoReady(p)) t.geo++; if (seoReady(p)) t.seo++; }
const typeScores = Object.values(byTypeG).filter(t => t.n >= 3).sort((a, b) => b.n - a.n);
const pctG = (x, n) => (n ? Math.round(x / n * 100) : 0);
const sdotG = v => v >= 70 ? '<span class="sdot ok">&#9679;</span>' : v >= 30 ? '<span class="sdot mid">&#9680;</span>' : '<span class="sdot no">&#9675;</span>';
const scoreRowsG = typeScores.map(t => { const a = pctG(t.aeo, t.n), g = pctG(t.geo, t.n), s = pctG(t.seo, t.n); const gap = [a < 70 ? 'FAQ schema' : null, g < 70 ? 'freshness date' : null, s < 70 ? 'links/depth/sitemap' : null].filter(Boolean).join(' &middot; ') || '&mdash;'; return '<tr><td><code>' + eH(t.type) + '</code> <span class=muted>&times;' + t.n + '</span></td><td class=ax>' + sdotG(s) + '</td><td class=ax>' + sdotG(a) + '</td><td class=ax>' + sdotG(g) + '</td><td class=miss>' + gap + '</td></tr>'; }).join('');

const shFixItems = fixes.filter(f => f.pri === 'NOW');
const shImproveItems = fixes.filter(f => f.pri !== 'NOW');
const shGrowItems = opps;
const fixCard = (f, i) => '<div class=sh-card role=button tabindex=0 data-sh="' + i + '"><div class=t>' + eH(f.title) + '</div><div class="row do"><span class=k>Do</span><span class=v>' + eH(f.how) + '</span></div><div class=sh-more>Click for details + the exact pages &rarr;</div></div>';
const oppCard = (o, i) => '<div class=sh-card role=button tabindex=0 data-sh="' + i + '"><div class=t>' + eH(o.title) + '</div><div class=row><span class=k>Why</span><span class=v>' + eH(o.detail) + '</span></div>' + (o.impact ? '<div class="row do"><span class=k>Upside</span><span class=v>' + eH(o.impact) + '</span></div>' : '') + '<div class=sh-more>Click for details + examples &rarr;</div></div>';
// blurb/empty are author-controlled literals (may contain HTML entities) — do NOT eH them.
const shSection = (cls, icon, name, blurb, items, cards, empty, base) =>
  '<div class="sh-sec ' + cls + '"><div class=sh-sechead><h2>' + icon + ' ' + name + '</h2>' + (items.length ? '<span class=cnt>' + items.length + '</span>' : '') + '<span class=blurb>' + blurb + '</span></div>' +
  (items.length ? '<div class=sh-cards>' + items.map((it, j) => cards(it, (base || 0) + j)).join('') + '</div>' : '<div class=sh-empty><b>&#10003;</b> ' + empty + '</div>') + '</div>';
// flat card data for the click-to-open detail modal (same order as rendered: fix, improve, grow)
const shCardData = [];
shFixItems.forEach((o) => shCardData.push({ grp: 'Fix', pri: o.pri || '', effort: o.effort || '', title: o.title, body: o.how, pages: o.sample || [] }));
shImproveItems.forEach((o) => shCardData.push({ grp: 'Improve', pri: o.pri || '', effort: o.effort || '', title: o.title, body: o.how, pages: o.sample || [] }));
shGrowItems.forEach((o) => shCardData.push({ grp: 'Grow', impact: o.impact || '', title: o.title, body: o.detail, pages: o.sample || [] }));
// click-to-open detail modal for the Start Here cards (self-contained IIFE)
const SH_MODAL_JS = "(function(){var M=document.getElementById('shmodal');if(!M)return;function esc(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;');}function openCard(i){var c=SH_CARDS[i];if(!c)return;M.querySelector('.shmodal-tag').textContent=[c.grp,c.pri,c.effort?c.effort+' effort':'',c.impact].filter(Boolean).join('  \\u00b7  ');M.querySelector('.shmodal-title').textContent=c.title;M.querySelector('.shmodal-body').textContent=c.body;var pg=M.querySelector('.shmodal-pages');if(c.pages&&c.pages.length){pg.innerHTML='<div class=shmodal-h>'+(c.grp==='Grow'?'Examples to model':'Pages to work on')+' ('+c.pages.length+(c.pages.length>=12?'+':'')+')</div><div class=shmodal-list>'+c.pages.map(function(p){return '<code>'+esc(p)+'</code>';}).join('')+'</div>';}else{pg.innerHTML='';}M.classList.add('on');document.body.style.overflow='hidden';}function closeCard(){M.classList.remove('on');document.body.style.overflow='';}document.querySelectorAll('[data-sh]').forEach(function(el){el.addEventListener('click',function(){openCard(+el.getAttribute('data-sh'));});el.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();openCard(+el.getAttribute('data-sh'));}});});M.addEventListener('click',function(e){if(e.target===M||e.target.classList.contains('shmodal-x'))closeCard();});document.addEventListener('keydown',function(e){if(e.key==='Escape')closeCard();});})();";
const shModalHtml = '<div id=shmodal class=shmodal><div class=shmodal-box role=dialog aria-modal=true><button class=shmodal-x aria-label=Close>&times;</button><div class=shmodal-tag></div><h3 class=shmodal-title></h3><div class=shmodal-h>What to do &amp; why</div><div class=shmodal-body></div><div class=shmodal-pages></div></div></div>';
const shHealthy = shFixItems.length === 0;
const shVerdict = shHealthy
  ? '<div class="sh-verdict good"><span class=vh>&#9989; Nothing urgent to fix right now.</span><span class=vsub>There are still ways to improve and grow &mdash; see below.</span></div>'
  : '<div class="sh-verdict attn"><span class=vh>&#9888;&#65039; ' + shFixItems.length + ' thing' + (shFixItems.length === 1 ? '' : 's') + ' to fix first.</span><span class=vsub>Start with the &#128295; Fix list &mdash; broken or risky right now.</span></div>';
const shGloss = [
  ['SEO', 'Search Engine Optimization &mdash; getting found in normal Google results (the blue links). Driven by unique content, internal links, and ranking position.'],
  ['AEO', 'Answer Engine Optimization &mdash; getting your answer lifted into Google\'s answer box and &ldquo;People also ask.&rdquo; Needs clear Q&amp;A plus FAQ / HowTo schema.'],
  ['GEO', 'Generative Engine Optimization &mdash; getting quoted by AI engines (ChatGPT, Perplexity, Google AI Overviews). Needs fresh dates, named authors, and data-rich structured facts AI can extract.'],
  ['Broken link', 'A link on your site that points to a page that no longer exists &mdash; visitors (and Google) hit a dead end.'],
  ['Thin article', 'A page with too little content (under ~500&ndash;800 words) to rank or be useful.'],
  ['Orphan page', 'A page nothing else links to, so visitors and Google can barely find it.'],
  ['Sitemap', 'The file that tells Google every page you want it to find. &ldquo;Drift&rdquo; = it lists the wrong pages.'],
  ['Schema (JSON-LD)', 'Hidden labels that tell Google what a page is (an article, a service, an FAQ) so it can show rich results.'],
  ['Impression', 'One time your page showed up in someone&rsquo;s Google results (whether or not they clicked).'],
  ['Click / CTR', 'A click is someone visiting from Google. CTR = clicks &divide; impressions. Low CTR = shown a lot, clicked rarely.'],
  ['Position', 'Average ranking spot. 1&ndash;10 = page 1. ~19 means bottom of page 2.'],
  ['AI Overviews / AIO', 'Google answering the question directly at the top, so users never click through &mdash; your biggest click leak.'],
  ['Cannibalization', 'Two of your own pages chasing the same search, so they compete and split the ranking instead of one winning.'],
].map(g => '<dt>' + g[0] + '</dt><dd>' + g[1] + '</dd>').join('');
// Today's focus: top 3 moves, re-derived every build
const focusG = [];
shFixItems.forEach(f => focusG.push('<b>' + eH(f.title) + '</b>'));
if (geoGapPages.length) focusG.push('<b>Add &ldquo;last updated&rdquo; dates to ' + geoGapPages.length + ' pages</b> so AI engines (ChatGPT, Perplexity, Google AI) trust and cite you. <span class=muted>GEO</span>');
if (aeoGapPages.length) focusG.push('<b>Add FAQ blocks to ' + aeoGapPages.length + ' pages</b> so Google&rsquo;s answer box can feature you. <span class=muted>AEO</span>');
const focusTopG = focusG.slice(0, 3);
const focusBoxG = focusTopG.length
  ? '<div class=sh-focus><div class=sh-focus-h>&#127919; Today\'s focus <span class=sh-focus-sub>the top moves right now &mdash; this list re-sorts itself as pages change</span></div><ol class=sh-focus-list>' + focusTopG.map(f => '<li>' + f + '</li>').join('') + '</ol></div>'
  : '';
const seoStrategyG =
  '<h2 class=sec style="margin-top:30px">&#128202; Your SEO &middot; AEO &middot; GEO playbook <span class=muted style="font-weight:400;font-size:.85rem">live-scored from each page\'s structured data</span></h2>' +
  '<div class=sub>There are three ways people find you now &mdash; optimize for all three. Fix a page and its dots below flip automatically on the next build.</div>' +
  '<div class=sgrid3>' +
  '<div class=panel style="border-left:3px solid var(--cy)"><b>&#128269; SEO</b> &mdash; classic Google results.<div class=muted style="margin-top:6px">Be crawlable, internally linked, and substantial. Win = a blue link on page 1.</div></div>' +
  '<div class=panel style="border-left:3px solid var(--warn)"><b>&#128172; AEO</b> &mdash; answer engines.<div class=muted style="margin-top:6px">Get lifted into Google\'s answer box &amp; &ldquo;People also ask.&rdquo; Needs clear Q&amp;A + FAQ / HowTo schema.</div></div>' +
  '<div class=panel style="border-left:3px solid var(--good)"><b>&#129302; GEO</b> &mdash; AI engines (ChatGPT, Perplexity, AI Overviews).<div class=muted style="margin-top:6px">Get quoted by AI. Needs fresh dates and data-rich structured facts it can extract.</div></div>' +
  '</div>' +
  '<div class=scoreboard><table><thead><tr><th>Page type</th><th class=ax><div class=axhead>SEO<small>found</small></div></th><th class=ax><div class=axhead>AEO<small>answer box</small></div></th><th class=ax><div class=axhead>GEO<small>AI cites</small></div></th><th>Biggest gap to close</th></tr></thead><tbody>' + scoreRowsG + '</tbody></table></div>' +
  '<p class=muted style="margin-top:8px">&#9679; 70%+ of pages ready &nbsp; &#9680; partial &nbsp; &#9675; under 30% &mdash; auto-scored from each page\'s schema every build. The &ldquo;Improve&rdquo; items above come straight from these gaps.</p>';
const startHere =
  '<p class=sh-intro>&#128203; <b>What this page is:</b> an automatic health check of every page on axiantpartners.com &mdash; which are thin or broken, how they link together, and how they&rsquo;re doing across Google search (<b>SEO</b>), Google&rsquo;s answer boxes (<b>AEO</b>), and AI engines like ChatGPT &amp; Perplexity (<b>GEO</b>). It rebuilds from the live site every commit, so the to-do list below stays current on its own.</p>' +
  shVerdict +
  focusBoxG +
  shSection('sh-fix', '&#128295;', 'Fix', 'Broken or risky &mdash; handle these first.', shFixItems, fixCard, 'Nothing broken or urgent right now.', 0) +
  shSection('sh-improve', '&#128200;', 'Improve', 'Works today, but tightening these makes it stronger.', shImproveItems, fixCard, 'No cleanup items right now.', shFixItems.length) +
  shSection('sh-grow', '&#128640;', 'Grow', 'New ground to win more traffic &mdash; without cannibalizing what you have.', shGrowItems, oppCard, 'No growth items flagged.', shFixItems.length + shImproveItems.length) +
  seoStrategyG +
  '<details class=sh-gloss><summary>Plain-English dictionary &mdash; what every term here means</summary><dl>' + shGloss + '</dl></details>';

const HTML =
'<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'+
'<title>Axiant Partners &mdash; Site Audit</title><style>'+CSS+'</style></head><body>'+
'<header class=hd><div class=wrap>'+
'<button class=dlbtn onclick="downloadReport()" title="Save this report as a PDF"><svg viewBox="0 0 24 24" fill=none stroke=currentColor stroke-width=2 stroke-linecap=round stroke-linejoin=round><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1=12 y1=15 x2=12 y2=3 /></svg>Download report (PDF)</button>'+
'<span class="pillbadge pb-green">Site Architecture &amp; SEO Audit</span>'+
'<span class="pillbadge pb-gen"><span class=dot></span>Auto-generated '+stamp+'</span>'+
'<h1>Axiant Partners &mdash; Full Site Breakdown</h1>'+
'<p class=lede>Every published page on axiantpartners.com, mapped by type, cluster, and content health. Page counts and structure are <b>auto-derived from the codebase on every commit</b> &mdash; this report regenerated <b>'+stamp+'</b>. The <b>Fixes &amp; Opportunities</b> tab is where the work is.</p>'+
'</div></header><div class=wrap>'+
'<div class=kpis id=kpis></div>'+
'<div class=note><b>Top findings:</b> <b>'+Sx.brokenLinks+' broken internal links</b>, <b>'+Sx.filler+' pages with <code>data-batch</code> filler</b>, <b>'+Sx.noindexInSitemap+' noindex pages in the sitemap</b>, and <b>'+(Sx.veryThin+Sx.thin)+' thin articles</b> &mdash; see the Fixes &amp; Opportunities tab.</div>'+
startHere+
'<details class=techwrap><summary>&#128295; Technical details <span class=techhint>&mdash; full inventory, page-by-page explorer, raw issue lists, and the GSC performance data. Open this when you want to dig in.</span></summary>'+
'<div class=toptabs><div class="toptab on" data-pane="overview">&#128202; Overview &amp; Audit</div><div class=toptab data-pane="fixes">&#128295; Fixes &amp; Opportunities</div><div class=toptab data-pane="gsc">&#128201; GSC Performance</div></div>'+
'<div class="tabpane on" id="pane-overview">'+
'<h2 class=sec>Visual architecture</h2><div class=sub>Every section of the site by route prefix, with live page counts &mdash; auto-derived from the codebase. Financing products and industry clusters are the backbone; equipment subtypes, guides, and landing pages fill the long tail.</div><div class=arch-grid id=arch></div>'+
'<h2 class=sec>Page types &amp; content depth</h2><div class=sub>Static, framework-free HTML on Netlify: service hubs, industry hubs, per-cluster articles, amount/geo landing pages, calculators, and ad-landing variants.</div>'+
'<div class=grid2><div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Page types</h3><div id=typedist></div></div>'+
'<div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Content depth (words, content pages)</h3><div id=hist></div></div></div>'+
'<h2 class=sec>Clusters &mdash; depth &amp; health</h2><div class=sub>Click headers to sort.</div><div class=panel style="overflow:auto;max-height:540px" id=cltbl></div>'+
'<h2 class=sec>Issues &mdash; raw lists</h2><div class=sub>Each tab is a working list. Red = highest priority.</div><div class=tabs id=tabs></div><div id=tabpanel></div>'+
'<h2 class=sec>What is good</h2>'+
'<div class="good-li"><b>Strong topical clustering.</b> '+Sx.clusters+' clusters, '+Sx.articles+' articles averaging '+Sx.avgArticleWords+' words.</div>'+
'<div class="good-li"><b>Almost no orphans ('+Sx.orphans+') and '+Sx.dupTitles+' duplicate titles.</b> Interlinking + cannibalization work paid off.</div>'+
'<div class="good-li"><b>'+Sx.ldFails+' JSON-LD parse failures; schema near-universal</b> ('+Sx.noSchema+' content pages without it). Strong AEO/GEO base.</div>'+
'<h2 class=sec>Explore every page</h2><div class=sub>Search, filter by type, click headers to sort. Flags show each page\'s issues.</div>'+
'<div class=controls><input id=q placeholder="Search URL or title..."><select id=ft></select><span class=muted id=excount style="align-self:center"></span></div>'+
'<div class=panel style="overflow:auto;max-height:640px" id=extbl></div>'+
'</div>'+
'<div class=tabpane id="pane-fixes">'+
'<h2 class=sec>Site hygiene sweep &mdash; 2026-06-18</h2>'+
'<div class="note" style="border-left-color:var(--good);background:rgba(34,197,94,.1);color:#86efac"><b>Full-site observation + remediation &mdash; 846 pages scanned.</b> A deterministic scan (<code>_analysis/observe-site.mjs</code>) flagged dead cards, duplicate/cannibalizing pages, sitemap gaps, and encoding bugs. The items below were fixed this session; broken internal links held at <b>0</b> throughout. Full write-up: <code>_analysis/SITE_HYGIENE_2026-06-18.md</code>.</div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-now">FIXED</span><b>35 dead-end article cards removed</b><span class=eff>18 pages</span></div><div class=muted style="font-size:.85rem;margin-top:6px">Link-less &ldquo;Relevant Articles&rdquo; cards advertising planned/deleted pages (e.g. <code>contractor-cash-flow-red-flags-*</code>, &ldquo;wartime inflation&rdquo; LOC pieces already 301&rsquo;d in <code>_redirects</code>). Auto-relinking was rejected &mdash; fuzzy matches produced wrong-section mismatches &mdash; so the dead cards were removed. Every section kept its real, linked cards (min 4).</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-now">FIXED</span><b>Rate-page cannibalization &mdash; BLoC + equipment</b><span class=eff>dedup</span></div><div class=muted style="font-size:.85rem;margin-top:6px">Two pages each targeted &ldquo;business line of credit rates&rdquo; and &ldquo;equipment financing rates.&rdquo; Canonicaled the 0-impression <code>typical-*-rates-2026</code> duplicates to the established <code>what-are-typical-*-rates</code> winners, removed the dups from the sitemap, and added hub&rarr;rates internal links.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-now">FIXED</span><b>Duplicate contractor hub consolidated</b><span class=eff>canonical</span></div><div class=muted style="font-size:.85rem;margin-top:6px"><code>contractor-financing.html</code> was a noun-swapped template clone of <code>construction-business-financing.html</code> (same section skeleton). Construction is the clear winner (15 impr vs 0; 79 inbound links vs 11; owns the article cluster), so the contractor page was canonicaled to it and dropped from the sitemap.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-soon">FIXED</span><b>25 indexable pages added to the sitemap</b><span class=eff>discovery</span></div><div class=muted style="font-size:.85rem;margin-top:6px">Self-canonical industry sub-pages (business-growth-financing, landscaping, logistics, manufacturing, medical-practices, restaurants) had no crawl path. Added them; excluded canonical-elsewhere dupes and bare-dir stubs.</div></div>'+
'<div class=fixcard><div class=fixhead><span class="tag t-soon">FIXED</span><b>894 &ldquo;&middot;&rdquo;-as-em-dash typos corrected</b><span class=eff>54 pages</span></div><div class=muted style="font-size:.85rem;margin-top:6px">A past find/replace turned em-dashes into <code>&amp;middot;</code> glued mid-sentence (&ldquo;project-based&middot;you incur costs&rdquo;). Replaced with <code>&amp;mdash;</code> everywhere it was not a space-padded separator; left the 281 legitimate <code> &middot; </code> separators alone.</div></div>'+
'<div class="good-li" style="margin-top:14px"><b>Checked &amp; intentionally left alone:</b> the construction working-capital cluster (retainage, mobilization, draw gaps&hellip;) is genuinely distinct long-tail, not duplicates; WC / MCA / SBA / CRE / SBL each have a single rates page (no cannibalization); &ldquo;1 inbound link&rdquo; pages are a thin-linking opportunity, not breakage (true zero-inbound orphans &asymp; 1); and the <code>digital-marketing/fragments/</code> &amp; <code>tools/article_supplements/</code> files have no title/meta because they are HTML includes, not standalone pages &mdash; consider a <code>noindex</code>/robots guard if they ever become linkable.</div>'+
'<h2 class=sec>Suggested fixes</h2><div class=sub>Auto-derived from the data, prioritized NOW / SOON / LATER with effort and example pages. Expand any card for the affected URLs.</div><div id=fixes></div>'+
'<h2 class=sec>Things to go after</h2><div class=sub>Growth opportunities that won\'t cannibalize existing pages &mdash; sized by data where possible.</div><div id=opps></div>'+
'<h2 class=sec>Trends over time</h2><div class=sub>Each run appends a snapshot (deduped per day). Arrows compare to the previous run &mdash; green is the good direction. Sparklines fill in as history accumulates.</div><div class=trendgrid id=trendcards style="margin-bottom:18px"></div><div class=panel style="overflow:auto;max-height:340px" id=histtbl></div>'+
'</div>'+
'<div class=tabpane id="pane-gsc">'+gscPane+'</div>'+
'</details>'+
'<p class=muted style="margin-top:30px;font-size:.8rem">Auto-generated '+stamp+' by scripts/site-audit.js from '+Sx.totalFiles+' HTML files. Word counts use the &lt;main&gt; region where present. Orphan = 0 resolved inbound links excluding global nav/footer.</p>'+
shModalHtml+
'</div><script>\nvar DATA='+JSON.stringify(DATA)+';\nvar SH_CARDS='+JSON.stringify(shCardData)+';\nfunction downloadReport(){var o=[];document.querySelectorAll("details:not([open])").forEach(function(d){d.open=true;o.push(d);});function r(){o.forEach(function(d){d.open=false;});window.removeEventListener("afterprint",r);}window.addEventListener("afterprint",r);window.print();}\n'+JS+'\n'+SH_MODAL_JS+'\n</script></body></html>';

fs.writeFileSync(path.join(OUT_DIR, 'site-audit.html'), HTML);
// Best-effort: also drop a copy in ~/Downloads (as axiant-site-audit.html) so a
// locally-opened copy is never stale. No-ops silently if there is no Downloads dir.
try {
  const dl = path.join(require('os').homedir(), 'Downloads');
  if (fs.existsSync(dl)) {
    fs.copyFileSync(path.join(OUT_DIR, 'site-audit.html'), path.join(dl, 'axiant-site-audit.html'));
    console.log('[site-audit] copied -> ' + path.join(dl, 'axiant-site-audit.html'));
  }
} catch (e) { /* best-effort */ }
console.log('[site-audit] '+Sx.totalFiles+' pages, '+Sx.articles+' articles | broken:'+Sx.brokenLinks+' thin:'+(Sx.veryThin+Sx.thin)+' filler:'+Sx.filler+' | history:'+history.length+' snapshot(s) -> _analysis/site-audit.html');
