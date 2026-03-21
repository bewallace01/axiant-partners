const https = require('https');
const fs = require('fs');
const path = require('path');

const fontsDir = './fonts';
if (!fs.existsSync(fontsDir)) fs.mkdirSync(fontsDir);

// Download Inter and Playfair Display woff2 files (using Fontsource CDN - stable URLs)
const fonts = [
  {
    url: 'https://cdn.jsdelivr.net/fontsource/fonts/inter@latest/latin-400-normal.woff2',
    file: 'inter-regular.woff2'
  },
  {
    url: 'https://cdn.jsdelivr.net/fontsource/fonts/playfair-display@latest/latin-600-normal.woff2',
    file: 'playfair-600.woff2'
  }
];

fonts.forEach(({ url, file }) => {
  const dest = path.join(fontsDir, file);
  const fileStream = fs.createWriteStream(dest);
  https.get(url, response => response.pipe(fileStream));
  console.log('Downloaded:', file);
});
