"""Read only the primary star-game proof dependency; no manuscript rendering."""
from pathlib import Path
import pypdfium2 as pdfium
from pypdf import PdfReader
import sys

sys.stdout.reconfigure(encoding="utf-8")

root = Path(__file__).parent
source = root / "star-games-hydras-2021.pdf"
out = root / "marked-tree-source-pages"
out.mkdir(exist_ok=True)
doc = pdfium.PdfDocument(str(source))
reader = PdfReader(source)
print(f"Physical extent {len(reader.pages)}; journal pages20:1-20:32")
for page in (9, 12, 13, 14, 15, 16, 17, 18):
    doc[page - 1].render(scale=1.5).to_pil().save(out / f"eko2021-{page:02d}.png")
    print(f"\nPAGE20:{page}\n{reader.pages[page - 1].extract_text()}")
