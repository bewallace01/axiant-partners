const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

async function optimizeMobileImages() {
  const assetsDir = path.join(__dirname, 'assets');
  if (!fs.existsSync(assetsDir)) {
    console.log('assets directory not found');
    return;
  }

  const files = fs.readdirSync(assetsDir);

  for (const file of files) {
    if (!file.match(/\.(png|jpg|jpeg|webp)$/i)) continue;
    if (file.includes('-mobile')) continue;

    const inputPath = path.join(assetsDir, file);
    const baseName = file.replace(/\.(png|jpg|jpeg|webp)$/i, '');
    const outputPath = path.join(assetsDir, `${baseName}-mobile.webp`);

    try {
      if (file.toLowerCase().includes('hero')) {
        await sharp(inputPath)
          .resize(480, 320, { fit: 'inside', withoutEnlargement: true })
          .webp({ quality: 75 })
          .toFile(outputPath);
      } else if (file.toLowerCase().includes('howitworks')) {
        await sharp(inputPath)
          .resize(360, 200, { fit: 'inside', withoutEnlargement: true })
          .webp({ quality: 75 })
          .toFile(outputPath);
      } else {
        await sharp(inputPath)
          .resize(480, 480, { fit: 'inside', withoutEnlargement: true })
          .webp({ quality: 75 })
          .toFile(outputPath);
      }
      console.log('Mobile version created:', file);
    } catch (err) {
      console.error('Error processing', file, err.message);
    }
  }
  console.log('All mobile images done.');
}

optimizeMobileImages().catch(console.error);
