"""Acquire the exact free Holm 1979 scan and record its readable extent."""
from pathlib import Path
import hashlib
import json
import urllib.request

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
URL = "https://www.ime.usp.br/~abe/lista/pdf4R8xPVzCnX.pdf"
PDF = HERE / "holm-1979-sequentially-rejective.pdf"
if not PDF.exists():
    request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        content_type = response.headers.get("Content-Type")
        final_url = response.geturl()
    if not data.startswith(b"%PDF-"):
        raise RuntimeError("The source response is not a PDF")
    PDF.write_bytes(data)
else:
    data = PDF.read_bytes()
    content_type = "application/pdf (held copy)"
    final_url = URL
reader = PdfReader(PDF)
pages = [page.extract_text() for page in reader.pages]
if len(pages) != 7 or not all(page.strip() for page in pages):
    raise RuntimeError("The expected seven readable physical pages are absent")
transcript = "\n\n".join(
    f"--- PHYSICAL PAGE {number} ---\n{text}"
    for number, text in enumerate(pages, 1)
)
(HERE / "holm-1979-extracted.txt").write_text(transcript, encoding="utf-8")
record = {
    "url": URL,
    "final_url": final_url,
    "content_type": content_type,
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "physical_pages": len(pages),
    "article_extent": "Printed pages 65-70; physical pages 2-7 after archive cover",
    "source_identity": "Sture Holm, A Simple Sequentially Rejective Multiple Test Procedure, Scandinavian Journal of Statistics 6(2), 1979, 65-70",
    "read_status": "Acquired and extracted; author reading is recorded separately",
}
(HERE / "acquisition.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
