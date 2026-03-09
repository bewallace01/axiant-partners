/**
 * Adds equipment-specific content and hub elements to all how-to-finance pages.
 * Run from project root: node scripts/update-equipment-pages.js
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const EQUIPMENT_DIR = path.join(ROOT, 'equipment');
const CONTENT_PATH = path.join(__dirname, 'equipment_specific_content.json');

const content = JSON.parse(fs.readFileSync(CONTENT_PATH, 'utf8'));

// Map folder -> how-to-finance subfolder name
function getHowToFinanceDirs() {
  const dirs = fs.readdirSync(EQUIPMENT_DIR);
  const result = [];
  for (const dir of dirs) {
    const fullPath = path.join(EQUIPMENT_DIR, dir);
    if (!fs.statSync(fullPath).isDirectory()) continue;
    const subs = fs.readdirSync(fullPath);
    const howTo = subs.find(s => s.startsWith('how-to-finance'));
    if (howTo) {
      result.push({ folder: dir, howTo });
    }
  }
  return result;
}

// Title from folder: "wheel-loaders" -> "Wheel Loader", "dental-equipment" -> "Dental Equipment"
function folderToTitle(folder) {
  return folder
    .split('-')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');
}

// URL path for related equipment
function getHowToPath(folder) {
  const d = getHowToFinanceDirs().find(x => x.folder === folder);
  if (!d) return null;
  return `/equipment/${folder}/${d.howTo}/`;
}

function buildAtGlanceBox(glance) {
  return `            <div class="at-a-glance-box" style="background:var(--bg-secondary); border:1px solid var(--border-color); border-radius:8px; padding:1rem 1.25rem; margin:1.5rem 0;">
                <h3 style="margin-top:0; font-size:1rem;">At a Glance</h3>
                <ul style="margin:0; padding-left:1.25rem; list-style:disc;">
                    <li><strong>Cost range:</strong> ${glance.cost}</li>
                    <li><strong>Typical terms:</strong> ${glance.terms}</li>
                    <li><strong>Typical approval:</strong> ${glance.approval}</li>
                </ul>
            </div>

`;
}

function buildSpecificSection(folder, specific) {
  const title = folderToTitle(folder);
  return `            <h2>Why ${title} Financing Is Different</h2>
            <p>${specific}</p>

`;
}

function main() {
  const dirs = getHowToFinanceDirs();
  let updated = 0;
  let skipped = 0;

  for (const { folder, howTo } of dirs) {
    const data = content[folder];
    if (!data || !data.glance || !data.specific) {
      console.log('Skip (no content):', folder);
      skipped++;
      continue;
    }

    const htmlPath = path.join(EQUIPMENT_DIR, folder, howTo, 'index.html');
    if (!fs.existsSync(htmlPath)) {
      console.log('Skip (no file):', htmlPath);
      skipped++;
      continue;
    }

    let html = fs.readFileSync(htmlPath, 'utf8');

    // 1. Add At a Glance after </figure> if not present
    if (!html.includes('at-a-glance-box')) {
      const figureEnd = '</figure>\n\n            <h2>';
      const insert = `</figure>\n\n${buildAtGlanceBox(data.glance)}            <h2>`;
      if (html.includes(figureEnd)) {
        html = html.replace(figureEnd, insert);
      } else {
        const alt = '</figure>\n\n            <';
        if (html.includes(alt)) {
          html = html.replace(alt, `</figure>\n\n${buildAtGlanceBox(data.glance)}            <`);
        }
      }
    }

    // 2. Add "Why X Financing Is Different" after "How Do You Finance" paragraph if not present
    const specificTitle = `Why ${folderToTitle(folder)} Financing Is Different`;
    if (!html.includes(specificTitle)) {
      // Find: <h2>How Do You Finance ...?</h2>\n<p>...</p>\n\n<h2> (next section)
      const re = /(<h2>How Do You Finance[^<]+<\/h2>\s*<p>[^<]+<\/p>)\s*(\n\s*<h2>)/;
      const specificBlock = buildSpecificSection(folder, data.specific);
      const replacement = `$1\n\n${specificBlock}            $2`;
      if (re.test(html)) {
        html = html.replace(re, replacement);
      }
    }

    // 3. Prepend related equipment links to existing "Related Financing Guides" ul (if we have related[] and page has that section)
    if (data.related && data.related.length > 0 && html.includes('<h2>Related Financing Guides</h2>')) {
      const relatedPaths = data.related
        .map(r => {
          const p = getHowToPath(r);
          const t = folderToTitle(r);
          return p ? { path: p, title: t } : null;
        })
        .filter(Boolean);

      if (relatedPaths.length > 0) {
        const relatedLinks = relatedPaths
          .map(({ path: p, title }) => `                <li><a href="${p}">How to Finance ${title}</a></li>`)
          .join('\n');
        // Insert after <h2>Related Financing Guides</h2> and <ul>, before first existing <li>
        const beforeFirstLi = /(<h2>Related Financing Guides<\/h2>\s*<ul>)\s*(<li>)/;
        if (beforeFirstLi.test(html)) {
          html = html.replace(beforeFirstLi, `$1\n${relatedLinks}\n                $2`);
        }
      }
    }

    fs.writeFileSync(htmlPath, html);
    console.log('Updated:', folder);
    updated++;
  }

  console.log('\nDone. Updated:', updated, 'Skipped:', skipped);
}

main();
