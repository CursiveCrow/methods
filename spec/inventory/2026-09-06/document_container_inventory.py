"""Inventory document magic and archive members without extracting or editing sources."""
from __future__ import annotations
import collections
import csv
import json
from pathlib import Path
import zipfile

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"
with (OUT / "workspace-files.csv").open(encoding="utf-8-sig", newline="") as handle:
    files = list(csv.DictReader(handle))
observed, archives, errors = [], [], []
counts = collections.Counter()
for index, row in enumerate(files, 1):
    path = ROOT / row["path"]
    try:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT.resolve()):
            errors.append({"path": row["path"], "state": "out_of_root_link_not_followed"})
            continue
        with path.open("rb") as handle:
            head = handle.read(32)
        kind = "pdf" if head.startswith(b"%PDF-") else "postscript" if head.startswith(b"%!PS") else "djvu" if head.startswith(b"AT&TFORM") else "zip" if head.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")) else "gzip" if head.startswith(b"\x1f\x8b") else "7zip" if head.startswith(b"7z\xbc\xaf\x27\x1c") else "other"
        counts[kind] += 1
        if kind != "other":
            observed.append({**row, "magic_kind": kind})
        if kind == "zip":
            try:
                with zipfile.ZipFile(path) as archive:
                    infos = archive.infolist()
                    names = {i.filename for i in infos}
                    role = "epub" if "META-INF/container.xml" in names and "mimetype" in names else "docx" if "word/document.xml" in names else "xlsx" if "xl/workbook.xml" in names else "pptx" if "ppt/presentation.xml" in names else "generic_zip"
                    members = [{"name": i.filename, "bytes": i.file_size, "compressed_bytes": i.compress_size,
                                "crc32": format(i.CRC, "08x"), "encrypted": bool(i.flag_bits & 1)}
                               for i in infos if Path(i.filename).suffix.lower() in {".pdf", ".ps", ".djvu", ".epub", ".bib", ".tex"}]
                    archives.append({"path": row["path"], "role": role, "member_count": len(infos), "document_members": members,
                                     "method": "Central directory only. No archive member extracted or executed; filenames/CRC are not source identity or full content validation."})
            except Exception as error:
                errors.append({"path": row["path"], "state": "archive_directory_error", "error": str(error)})
    except OSError as error:
        errors.append({"path": row["path"], "state": "header_read_error", "error": str(error)})
    if index % 10000 == 0:
        print(f"Read document headers for {index}/{len(files)} enumerated files", flush=True)
old_pdf_paths = set()
with (OUT / "source-and-pdf-files.csv").open(encoding="utf-8-sig", newline="") as handle:
    old_pdf_paths = {r["path"] for r in csv.DictReader(handle) if r["header_type"] == "pdf"}
new_pdfs = [r for r in observed if r["magic_kind"] == "pdf" and r["path"] not in old_pdf_paths]
summary = {"enumerated_files": len(files), "header_kind_counts": dict(counts), "errors_or_unfollowed_links": errors,
           "additional_pdf_header_files": new_pdfs, "archive_count": len(archives),
           "archive_roles": dict(collections.Counter(r["role"] for r in archives)),
           "archives_with_document_members": sum(bool(r["document_members"]) for r in archives),
           "embedded_pdf_named_members": sum(Path(m["name"]).suffix.lower() == ".pdf" for r in archives for m in r["document_members"]),
           "method": "First32bytes of every previously enumerated workspace file, not an extension filter; zip central-directory metadata only. No content absence or exact-source claim from unexamined compressed members."}
for name, value in (("document-magic-inventory.json", observed), ("document-archive-members.json", archives), ("document-container-summary.json", summary)):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
