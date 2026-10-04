"""Render only held primary-source pages; never build the handbook."""
from pathlib import Path
import pypdfium2 as pdfium

SOURCE = Path(r"C:\Dev\the-methods-of-reason\tmp\acquisition\src027\cwi-klop.pdf")
OUT = Path(__file__).parent / "source-pages"
OUT.mkdir(parents=True, exist_ok=True)
document = pdfium.PdfDocument(str(SOURCE))
for printed in (4, 5, 6, 7, 8, 11, 13, 14, 15, 16, 19, 20, 22, 24, 25, 29, 30, 31, 32, 33, 34, 35):
    page = document[printed + 3]
    image = page.render(scale=1.5).to_pil()
    image.save(OUT / f"printed-{printed:02d}.png")
print(f"Rendered selected primary-source pages to {OUT}")
