"""Record ordinary primary requests and reject HTML returned as a PDF."""
import hashlib
import json
import pathlib
import re
import urllib.request
from datetime import datetime, timezone

folder = pathlib.Path(__file__).resolve().parent
article_url = "https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/number-of-countable-models/122DECC61115A6F9C89E3827A1D2686D"
pdf_url = "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/122DECC61115A6F9C89E3827A1D2686D/S0022481200092173a.pdf/div-class-title-the-number-of-countable-models-div.pdf"
requests = [
    ("cambridge-article.html", article_url, "publisher identity and public extract"),
    ("cambridge-pdf-response", pdf_url, "PDF URL observed in the publisher citation_pdf_url metadata"),
    ("project-euclid-response.html", "https://projecteuclid.org/euclid.jsl/1183737029", "archive link observed in DBLP Morley70 record"),
    ("dblp-response.html", "https://dblp.org/pid/01/3276", "institutional bibliographic locator"),
]
records = []
acquired = False
for name, url, role in requests:
    item = {"requested_url": url, "role": role}
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            raw = response.read()
            item.update(final_url=response.url, content_type=response.headers.get("Content-Type"), bytes=len(raw))
        if raw.startswith(b"%PDF-"):
            name = "morley-1970-number-countable-models.pdf"
            item["access_result"] = "PDF acquired; identity and complete extent still require inspection."
            acquired = True
        else:
            if name == "cambridge-pdf-response":
                name += ".html"
            if b"_Incapsula_Resource" in raw:
                item["access_result"] = "Browser-verification response only; no archive article body."
            elif b"anubis_challenge" in raw:
                item["access_result"] = "Browser challenge only; no bibliography captured."
            elif url == pdf_url:
                item["access_result"] = "Redirected to article/extract HTML; not a PDF."
            else:
                item["access_result"] = "Public article identity/extract only; not full proof."
        (folder / name).write_bytes(raw)
        item.update(path=name, sha256=hashlib.sha256(raw).hexdigest())
    except Exception as failure:
        item["error"] = type(failure).__name__ + ": " + str(failure)
    records.append(item)
article_capture = folder / "cambridge-article.html"
if article_capture.exists():
    image_match = re.search(r'src="([^"]+S0022481200092173_inline1\.png[^"]*)"', article_capture.read_text(encoding="utf-8"))
    if image_match:
        image_record = {"requested_url": image_match.group(1), "role": "publisher extract mathematical glyph only, not full article"}
        try:
            with urllib.request.urlopen(image_match.group(1), timeout=20) as response:
                image_raw = response.read()
                image_record.update(final_url=response.url, content_type=response.headers.get("Content-Type"))
            if not image_raw.startswith(b"\x89PNG\r\n\x1a\n"):
                raise ValueError("The inline-formula response is not PNG data.")
            (folder / "publisher-continuum-glyph.png").write_bytes(image_raw)
            image_record.update(path="publisher-continuum-glyph.png", bytes=len(image_raw), sha256=hashlib.sha256(image_raw).hexdigest())
        except Exception as failure:
            image_record["error"] = type(failure).__name__ + ": " + str(failure)
        records.append(image_record)
receipt = {
    "requested_identity": {"key": "Morley1970CountableModels", "title": "The number of countable models", "journal": "Journal of Symbolic Logic", "volume": 35, "issue": 1, "year": 1970, "pages": "14-18", "doi": "10.2307/2271150"},
    "captured_utc": datetime.now(timezone.utc).isoformat(),
    "original_pdf_acquired": acquired,
    "original_body_read": False,
    "normal_TLS_verification": True,
    "challenge_bypass_attempted": False,
    "records": records,
}
(folder / "acquisition-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
