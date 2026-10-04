"""Read-only source-PDF identity census; metadata and first four text pages only."""
from __future__ import annotations

import concurrent.futures
import csv
import hashlib
import json
import logging
from pathlib import Path
import subprocess
import sys

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def examine(path):
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    from pypdf import PdfReader
    result = {"path": str(path), "scope": "PDF metadata and physical pages 1 through min(4,page_count); no rendering, OCR, full-body reading, or PDF writes."}
    try:
        with path.open("rb") as handle:
            reader = PdfReader(handle, strict=False)
            result["encrypted"] = reader.is_encrypted
            if reader.is_encrypted:
                result["empty_password_decryption_result"] = int(reader.decrypt(""))
            result["metadata"] = {str(k): str(v) for k, v in (reader.metadata or {}).items()}
            result["pages"] = len(reader.pages)
            pages = []
            for index in range(min(4, len(reader.pages))):
                try:
                    page_text = reader.pages[index].extract_text() or ""
                    pages.append({"physical_page": index + 1, "text": page_text[:30000], "text_truncated": len(page_text) > 30000})
                except Exception as error:
                    pages.append({"physical_page": index + 1, "extraction_error": type(error).__name__ + ": " + str(error)[:1000]})
            result["opening_page_text"] = pages
            result["opening_text_characters"] = sum(len(p.get("text", "")) for p in pages)
            result["state"] = "metadata_and_opening_text_read" if result["opening_text_characters"] else "metadata_read_no_opening_text"
    except Exception as error:
        result["state"] = "metadata_read_error"
        result["error"] = type(error).__name__ + ": " + str(error)[:1500]
    return result


if len(sys.argv) > 1 and sys.argv[1] == "--one":
    print(json.dumps(examine(Path(sys.argv[2])), ensure_ascii=True))
    raise SystemExit(0)

if (OUT / "document-magic-inventory.json").exists():
    physical = [r for r in json.loads((OUT / "document-magic-inventory.json").read_text(encoding="utf-8")) if r["magic_kind"] == "pdf"]
else:
    with (OUT / "source-and-pdf-files.csv").open(encoding="utf-8-sig", newline="") as handle:
        physical = [r for r in csv.DictReader(handle) if r["header_type"] == "pdf"]
groups = {}
for row in physical:
    path = ROOT / row["path"]
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            hasher.update(block)
    groups.setdefault(hasher.hexdigest(), []).append(row)

checkpoint = OUT / "pdf-holdings-identities.jsonl"
completed = {}
if checkpoint.exists():
    for line in checkpoint.read_text(encoding="utf-8").split("\n"):
        if line.strip():
            record = json.loads(line)
            completed[record["sha256"]] = record
print(f"Physical PDF files: {len(physical)}; unique byte identities: {len(groups)}; already inventoried: {len(completed)}", flush=True)


def bounded_examine(item):
    sha, copies = item
    chosen = sorted(copies, key=lambda r: (r["extension"] != ".pdf", len(r["path"])))[0]
    try:
        run = subprocess.run([sys.executable, "-X", "utf8", str(Path(__file__).resolve()), "--one", str(ROOT / chosen["path"])],
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
        if run.returncode:
            result = {"state": "metadata_subprocess_error", "error": run.stderr[-2000:]}
        else:
            result = json.loads(run.stdout)
            result["parser_messages"] = run.stderr[-2000:]
    except subprocess.TimeoutExpired:
        result = {"state": "metadata_read_timeout", "error": "Opening metadata/page-text subprocess exceeded 30 seconds; exact same file requires a separate bounded alternative."}
    except Exception as error:
        result = {"state": "metadata_subprocess_error", "error": str(error)[:1500]}
    return {"sha256": sha, "representative": chosen["path"], "physical_copies": copies, **result}


pending = [(sha, copies) for sha, copies in groups.items() if sha not in completed]
with checkpoint.open("a", encoding="utf-8") as sink:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(bounded_examine, item) for item in pending]
        for future in concurrent.futures.as_completed(futures):
            record = future.result()
            completed[record["sha256"]] = record
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            sink.flush()
            if len(completed) % 10 == 0 or len(completed) == len(groups):
                print(f"Inventoried {len(completed)}/{len(groups)} unique PDF byte identities", flush=True)

records = [completed[sha] for sha in sorted(groups)]
for record in records:
    record["physical_copies"] = groups[record["sha256"]]
summary = {"physical_files": len(physical), "unique_byte_identities": len(groups), "duplicate_physical_copies": len(physical)-len(groups),
           "identity_records": len(records), "states": {},
           "method": "Every PDF-header file is SHA256 grouped; one representative per byte identity receives metadata and first-four-page text extraction. This is evidence for identity investigation, not whole-body reading, edition authentication, source-fidelity or rights approval."}
for record in records:
    summary["states"][record["state"]] = summary["states"].get(record["state"], 0) + 1
(OUT / "pdf-holdings-identities.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "pdf-holdings-identities-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2), flush=True)
