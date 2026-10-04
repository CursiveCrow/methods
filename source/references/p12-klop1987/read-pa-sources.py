"""Read and render only primary sources for the PA/Puel block."""
from pathlib import Path
import sys
from pypdf import PdfReader
import pypdfium2 as pdfium

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).parent
if len(sys.argv) == 1:
    source = Path(r"C:\Dev\the-methods-of-reason\tmp\acquisition\src027\cwi-klop.pdf")
    doc = pdfium.PdfDocument(str(source))
    out = root / "source-pages" / "printed-21.png"
    doc[24].render(scale=1.8).to_pil().save(out)
    print(out)
else:
    source = root / sys.argv[1]
    reader = PdfReader(source)
    print(f"{source.name}: {len(reader.pages)} physical pages")
    selected = [int(number) for number in sys.argv[2:]]
    for physical in selected:
        print(f"\nPHYSICAL PAGE {physical}\n{reader.pages[physical - 1].extract_text()}")
        doc = pdfium.PdfDocument(str(source))
        out = root / "pa-source-pages"
        out.mkdir(exist_ok=True)
        doc[physical - 1].render(scale=1.5).to_pil().save(out / f"{source.stem}-{physical:02d}.png")
