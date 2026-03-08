/**
 * Convert PNG images in assets/ to WebP format.
 * Run: node scripts/convert-webp.js
 */
const fs = require('fs');
const path = require('path');

async function convertToWebP() {
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
  const pngs = files.filter(f => /\.png$/i.test(f));
  let converted = 0;

  for (const file of pngs) {
    const inputPath = path.join(assetsDir, file);
    const webpPath = inputPath.replace(/\.png$/i, '.webp');
    try {
      await sharp(inputPath)
        .webp({ quality: 82 })
        .toFile(webpPath);
      converted++;
      console.log('Created:', path.basename(webpPath));
    } catch (err) {
      console.error('Error:', file, err.message);
    }
  }

  console.log(`Done. Converted ${converted}/${pngs.length} PNGs to WebP.`);
}

convertToWebP();
