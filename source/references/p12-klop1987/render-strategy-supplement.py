"""Reading aids for the ordinary-TRS appendix cited by the 1987 tutorial."""
from pathlib import Path
import pypdfium2 as pdfium
from pypdf import PdfReader

root = Path(__file__).parent
source = root / "bergstra-klop1986.pdf"
out = root / "strategy-source-pages"
out.mkdir(exist_ok=True)
document = pdfium.PdfDocument(str(source))
for printed in (330, 331, 332, 352, 353, 354, 355, 356, 357, 359, 360):
    document[printed - 323].render(scale=1.5).to_pil().save(out / f"printed-{printed}.png")
reader = PdfReader(source)
print(f"Physical extent: {len(reader.pages)} pages; printed 323-362")
for index in (7, 8, 9, *range(29, 38)):
    print(f"\nPRINTED {index + 323}\n{reader.pages[index].extract_text()}")
