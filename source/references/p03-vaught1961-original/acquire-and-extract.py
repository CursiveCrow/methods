"""Capture the exact original Vaught manifestation with both paginations."""
from pathlib import Path
import hashlib
import json
import urllib.request
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
URL = "https://www.math.uic.edu/~jbaldwin/pub/vaught59.pdf"
PDF = HERE / "vaught-1961-denumerable-models.pdf"
if not PDF.exists():
    request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        final_url = response.geturl()
        content_type = response.headers.get("Content-Type")
    if not data.startswith(b"%PDF-"):
        raise RuntimeError("Response is not the selected PDF")
    PDF.write_bytes(data)
else:
    data = PDF.read_bytes()
    final_url = URL
    content_type = "application/pdf (held copy)"
reader = PdfReader(PDF)
texts = [page.extract_text() for page in reader.pages]
if len(texts) != 19 or not all(text.strip() for text in texts):
    raise RuntimeError("The expected nineteen readable pages are absent")
(HERE / "vaught-1961-extracted.txt").write_text(
    "\n\n".join(f"--- PHYSICAL PAGE {i} / ORIGINAL {302+i} / OUTER {608+i} ---\n{text}"
                for i, text in enumerate(texts, 1)), encoding="utf-8")
record = {
    "url": URL,
    "final_url": final_url,
    "content_type": content_type,
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "physical_pages": len(texts),
    "identity": "Robert L. Vaught, Denumerable Models of Complete Theories, Infinitistic Methods, 1961, 303-321",
    "paginations": {"original_printed": "303-321", "outer_scan": "609-627"},
    "read_status": "Acquired and extracted; full reading is recorded in the author source note",
}
(HERE / "acquisition.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
