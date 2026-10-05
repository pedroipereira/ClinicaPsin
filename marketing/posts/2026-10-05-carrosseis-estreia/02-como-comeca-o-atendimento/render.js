const {chromium} = require('playwright');
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
async function render() {
  const browser = await chromium.launch({executablePath: process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true});
  const page = await browser.newPage({viewport: {width: 1080, height: 1350}, deviceScaleFactor: 1, reducedMotion: 'reduce'});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto(pathToFileURL(path.join(__dirname, 'carrossel.html')).href);
  await page.evaluate(async () => {await document.fonts.ready; await Promise.all([...document.images].map(i => i.decode()));});
  const output = path.join(__dirname, 'instagram');
  fs.mkdirSync(output, {recursive: true});
  const report = [];
  for (const slide of await page.locator('.slide').all()) {
    const info = await slide.evaluate(el => {
      const bounds = el.getBoundingClientRect();
      const footer = el.querySelector('.slide-footer').getBoundingClientRect();
      const issues = [];
      const logo=el.querySelector('.brand img').getBoundingClientRect();
      if (logo.width!==76 || logo.height!==76 || logo.top < bounds.top) issues.push('logo dimensions');
      for (const node of el.querySelectorAll('h1,h2,.kicker,.copy,.credential,.audiences,.bottom-note,.cta-label,.text>p,.photo,.photo-split img')) {
        const r = node.getBoundingClientRect();
        if (r.left < bounds.left + 60 || r.right > bounds.right - 60) issues.push('horizontal: '+node.className+' '+node.textContent.slice(0,35));
        if (r.bottom > footer.top - 15) issues.push('footer collision: '+node.className+' '+node.textContent.slice(0,35));
        if (node.scrollHeight > node.clientHeight + 2 && ['hidden','clip'].includes(getComputedStyle(node).overflowY)) issues.push('text overflow: '+node.className);
      }
      return {id: el.id, width: bounds.width, height: bounds.height, issues, imagesLoaded: [...el.querySelectorAll('img')].every(i => i.naturalWidth > 0)};
    });
    await slide.screenshot({path: path.join(output, info.id+'.png')});
    report.push(info);
  }
  await browser.close();
  fs.writeFileSync(path.join(__dirname, 'verificacao.json'), JSON.stringify({errors, slides: report}, null, 2));
  console.log(path.basename(__dirname), JSON.stringify(report.map(r => ({id:r.id,issues:r.issues}))));
  if (errors.length || report.some(r=>r.issues.length || !r.imagesLoaded || r.width!==1080 || r.height!==1350)) throw new Error('Revisar layout: '+__dirname);
}
module.exports = render;
if (require.main === module) render().catch(error => {console.error(error.message);process.exitCode=1;});
