// Renderiza todos os carrosséis em PNG 1080x1350 e verifica sobreposições.
// Uso (raiz do projeto): NODE_PATH=$(npm root -g) node marketing/posts/2026-10-05-carrosseis/render-all.js [slug]
const {chromium} = require('playwright');
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');

(async () => {
  const only = process.argv[2];
  const dirs = fs.readdirSync(__dirname).filter(d => /^\d\d-/.test(d) && (!only || d.startsWith(only)));
  const browser = await chromium.launch(process.env.CHROME_PATH ? {executablePath: process.env.CHROME_PATH} : {});
  const page = await browser.newPage({viewport: {width: 1200, height: 1400}, deviceScaleFactor: 1});
  let problems = 0;
  for (const dir of dirs) {
    const folder = path.join(__dirname, dir);
    await page.goto(pathToFileURL(path.join(folder, 'carrossel.html')).href, {waitUntil: 'networkidle'});
    await page.evaluate(async () => { await document.fonts.ready; });
    const out = path.join(folder, 'instagram');
    fs.rmSync(out, {recursive: true, force: true});
    fs.mkdirSync(out, {recursive: true});
    const slides = await page.locator('.slide').all();
    const report = [];
    for (const [i, slide] of slides.entries()) {
      const issues = await slide.evaluate(el => {
        const b = el.getBoundingClientRect();
        const bottom = el.querySelector('.bottom').getBoundingClientRect();
        const out = [];
        for (const n of el.querySelectorAll('.main > *')) {
          const r = n.getBoundingClientRect();
          if (r.right > b.right - 60 || r.left < b.left + 60) out.push('horizontal: ' + n.className);
          if (r.bottom > bottom.top - 8) out.push('colide com rodapé: ' + (n.className || n.tagName));
          if (r.top < b.top + 140 && !el.classList.contains('split')) out.push('colide com topo: ' + (n.className || n.tagName));
        }
        return [...new Set(out)];
      });
      await slide.screenshot({path: path.join(out, `slide-${String(i + 1).padStart(2, '0')}.png`)});
      report.push({slide: i + 1, issues});
      problems += issues.length;
    }
    fs.writeFileSync(path.join(folder, 'verificacao.json'), JSON.stringify(report, null, 2));
    console.log(dir, report.filter(r => r.issues.length).map(r => `${r.slide}: ${r.issues.join('; ')}`).join(' | ') || 'ok');
  }
  await browser.close();
  if (problems) process.exitCode = 1;
})();
