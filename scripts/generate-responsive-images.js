/**
 * Generate responsive WebP variants (400w, 600w, 800w) for equipment/card images.
 * Run: node scripts/generate-responsive-images.js
 */
const fs = require('fs');
const path = require('path');

async function main() {
  let sharp;
  try {
    sharp = require('sharp');
  } catch (e) {
    console.error('Install sharp: npm install sharp');
    process.exit(1);
  }

  const assetsDir = path.join(__dirname, '..', 'assets');
  if (!fs.existsSync(assetsDir)) {
    console.log('assets/ not found');
    return;
  }

  const files = fs.readdirSync(assetsDir);
  const webpFiles = files.filter(f => {
    if (!f.endsWith('.webp') || /-[0-9]+w\.webp$/.test(f)) return false;
    return /equipment|intro|industry|forestry|manufacturing|restaurants|trucking|agriculture|auto-repair|medical-practices|logistics/.test(f);
  });

  const TARGET_WIDTHS = [400, 600, 800];
  const QUALITY = 80;
  let created = 0;

  for (const file of webpFiles) {
    const inputPath = path.join(assetsDir, file);
    const stem = file.replace(/\.webp$/, '');

    for (const targetW of TARGET_WIDTHS) {
      const outName = `${stem}-${targetW}w.webp`;
      const outPath = path.join(assetsDir, outName);
      if (fs.existsSync(outPath)) continue;

      try {
        const meta = await sharp(inputPath).metadata();
        const w = meta.width || 0;
        if (w <= targetW) continue;

        const ratio = targetW / w;
        const nh = Math.round((meta.height || 0) * ratio);

        await sharp(inputPath)
          .resize(targetW, nh, { fit: 'inside' })
          .webp({ quality: QUALITY })
          .toFile(outPath);

        created++;
        console.log('Created:', outName);
      } catch (err) {
        console.error('Error', file, targetW, err.message);
      }
    }
  }

  console.log(`Done. Created ${created} responsive variants.`);
}

main();
