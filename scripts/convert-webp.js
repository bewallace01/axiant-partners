/**
 * Convert PNG/JPG/JPEG images in assets/ to WebP format.
 * Skips if .webp already exists. Run: node scripts/convert-webp.js
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
  const images = files.filter(f => /\.(png|jpg|jpeg)$/i.test(f));
  let converted = 0;
  let skipped = 0;

  for (const file of images) {
    const inputPath = path.join(assetsDir, file);
    const webpPath = inputPath.replace(/\.(png|jpg|jpeg)$/i, '.webp');
    if (fs.existsSync(webpPath)) {
      skipped++;
      continue;
    }
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

  console.log(`Done. Converted ${converted} images to WebP (${skipped} already existed).`);
}

convertToWebP();
