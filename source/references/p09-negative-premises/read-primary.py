"""Read and render selected primary TSS pages; never render the manuscript."""
from pathlib import Path
import sys
from pypdf import PdfReader
import pypdfium2 as pdfium

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).parent
source = root / sys.argv[1]
reader = PdfReader(source)
print(f"{source.name}: {len(reader.pages)} physical pages")
doc = pdfium.PdfDocument(str(source))
out = root / "source-pages"
out.mkdir(exist_ok=True)
for number in map(int, sys.argv[2:]):
    print(f"\nPHYSICAL PAGE {number}\n{reader.pages[number - 1].extract_text()}")
    doc[number - 1].render(scale=1.5).to_pil().save(out / f"{source.stem}-{number:03d}.png")
