"""Capture only public locator pages; never claim an unread original body."""
import hashlib
import json
import pathlib
import urllib.request
from datetime import datetime, timezone

folder = pathlib.Path(__file__).resolve().parent
locators = [
    ("rcin-1959-volume.html", "https://rcin.org.pl/dlibra/publication/52319/bulletin-de-l-academie-polonaise-des-sciences-serie-des-sciences-mathematiques-astronomiques-et-physiques?language=en"),
    ("mcnulty-course.html", "https://people.math.sc.edu/mcnulty/modeltheory/"),
    ("wiley-svenonius-record.html", "https://onlinelibrary.wiley.com/doi/10.1111/j.1755-2567.1959.tb00294.x"),
]
records = []
for name, url in locators:
    record = {"requested_url": url, "role": "public locator only, not original article body"}
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            raw = response.read()
            record.update(final_url=response.url, content_type=response.headers.get("Content-Type"), bytes=len(raw))
        target = folder / name
        target.write_bytes(raw)
        record.update(path=name, sha256=hashlib.sha256(raw).hexdigest())
        if b"High Load - Verifying Browser" in raw:
            record["access_result"] = "Browser-verification response only; catalogue metadata was not captured by this request."
        else:
            record["access_result"] = "Public locator response; original article acquisition is not inferred."
    except Exception as failure:
        record.update(error=type(failure).__name__ + ": " + str(failure))
    records.append(record)
receipt = {
    "captured_utc": datetime.now(timezone.utc).isoformat(),
    "original_RyllNardzewski1959_body_acquired": False,
    "original_Engeler1959_abstract_acquired": False,
    "original_Svenonius1959_body_acquired": False,
    "Hodges1993_book_sections_acquired": False,
    "normal_TLS_verification": True,
    "records": records,
}
(folder / "locator-capture-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
