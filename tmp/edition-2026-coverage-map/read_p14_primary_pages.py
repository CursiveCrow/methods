"""Read primary PDFs and rasterize only the source pages needing glyph checks."""
from pathlib import Path
import hashlib
import json
from pypdf import PdfReader
import pypdfium2 as pdfium

root = Path(r'C:\Dev\the-methods-of-reason')
source = root / 'source/references/p14-reference-repairs'
for filename in ('pfenning-1998-sequent-handout.pdf', 'statman-1979.pdf', 'ladner-1977.pdf'):
    path = source / filename
    reader = PdfReader(path)
    print(json.dumps({'path': str(path), 'bytes': path.stat().st_size,
                      'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                      'pages': len(reader.pages)}))
    indices = (4, 5, 6) if filename.startswith('pfenning') else (0,)
    for index in indices:
        print(f'{filename}: physical page {index + 1}')
        print(reader.pages[index].extract_text())

path = source / 'pfenning-1998-sequent-handout.pdf'
document = pdfium.PdfDocument(str(path))
for index in (4, 5):
    page = document[index]
    page.render(scale=2).to_pil().save(source / f'pfenning-source-page-{index+1}.png')
    page.close()
document.close()
