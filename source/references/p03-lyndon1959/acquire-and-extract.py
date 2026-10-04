"""Acquire the two distinct original publisher PDFs and extract every page."""
import hashlib
import json
import pathlib
import urllib.request
from datetime import datetime, timezone
from pypdf import PdfReader

folder = pathlib.Path(__file__).resolve().parent
sources = [
    ("lyndon-1959-preservation", "https://msp.org/pjm/1959/9-1/p13.xhtml", "https://msp.org/pjm/1959/9-1/pjm-v9-n1-p13-s.pdf", "10.2140/pjm.1959.9.143", "143-154"),
    ("lyndon-1959-interpolation", "https://msp.org/pjm/1959/9-1/p12.xhtml", "https://msp.org/pjm/1959/9-1/pjm-v9-n1-p12-s.pdf", "10.2140/pjm.1959.9.129", "129-142"),
]
records = []
for stem, page_url, pdf_url, doi, extent in sources:
    with urllib.request.urlopen(page_url, timeout=20) as response:
        page_raw = response.read()
        final_page_url = response.url
    if pdf_url.replace("https://msp.org", "") not in page_raw.decode("utf-8", "replace"):
        raise ValueError("Selected PDF path is absent from the actual publisher page.")
    (folder / (stem + "-publisher.html")).write_bytes(page_raw)
    with urllib.request.urlopen(pdf_url, timeout=20) as response:
        raw = response.read()
        final_url = response.url
    if not raw.startswith(b"%PDF-"):
        raise ValueError("Publisher response is not PDF data.")
    pdf_path = folder / (stem + ".pdf")
    pdf_path.write_bytes(raw)
    reader = PdfReader(pdf_path)
    texts = []
    for number, page in enumerate(reader.pages, 1):
        texts.append(f"\n=== PHYSICAL PAGE {number} ===\n" + (page.extract_text() or ""))
    (folder / (stem + ".reading.txt")).write_text("\n".join(texts), encoding="utf-8")
    records.append({
        "stem": stem, "doi": doi, "original_printed_extent": extent,
        "publisher_page_requested": page_url, "publisher_page_final": final_page_url,
        "pdf_url_requested": pdf_url, "pdf_url_final": final_url,
        "bytes": len(raw), "physical_pages": len(reader.pages),
        "pdf_sha256": hashlib.sha256(raw).hexdigest(),
        "publisher_page_sha256": hashlib.sha256(page_raw).hexdigest(),
        "text_sha256": hashlib.sha256((folder / (stem + ".reading.txt")).read_bytes()).hexdigest(),
    })
receipt = {"acquired_utc": datetime.now(timezone.utc).isoformat(), "normal_TLS_verification": True, "sources": records}
(folder / "acquisition.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
