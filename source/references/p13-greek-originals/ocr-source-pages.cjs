// Mechanical English OCR derivative; the shared immutable PDF is never changed.
const fs = require('fs');
const path = require('path');
const { createWorker } = require('C:/Users/Crow/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/tesseract.js');
const folder = 'C:/Dev/the-methods-of-reason/source/references/p13-greek-originals';
(async () => {
  const first = Number(process.argv[2]), last = Number(process.argv[3]);
  const output = process.argv[4];
  if (!Number.isInteger(first) || !Number.isInteger(last) || first < 1 || last < first || last > 620 || !/^[a-z0-9-]+\.txt$/.test(output)) throw new Error('Invalid source-only range');
  const worker = await createWorker('eng', 1, { cachePath: folder });
  let text = '';
  for (let page = first; page <= last; page++) {
    const image = path.join(folder, 'ocr-page-' + String(page).padStart(3, '0') + '.png');
    const result = await worker.recognize(image);
    text += '\n\n===== PHYSICAL PDF PAGE ' + page + ' =====\n' + result.data.text;
    fs.writeFileSync(path.join(folder, output), text, 'utf8');
    process.stdout.write('OCR physical page ' + page + '\n');
  }
  await worker.terminate();
})().catch(error => { console.error(error); process.exitCode = 1; });
