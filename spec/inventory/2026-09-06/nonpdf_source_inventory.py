"""Inspect compressed/source document metadata without rendering or writing source files."""
from __future__ import annotations
import collections
import gzip
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"
magic = json.loads((OUT / "document-magic-inventory.json").read_text(encoding="utf-8"))
archives = json.loads((OUT / "document-archive-members.json").read_text(encoding="utf-8"))
pdfs = json.loads((OUT / "pdf-holdings-identities.json").read_text(encoding="utf-8"))
pdf_hashes = {r["sha256"]: r["representative"] for r in pdfs}
postscript, compressed, docs, members = [], [], [], []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dsc(text):
    return [{"line": text.count("\n", 0, m.start())+1, "field": m.group(1), "value": m.group(2).strip()}
            for m in re.finditer(r"(?m)^%%(Title|Creator|CreationDate|Pages|BoundingBox|DocumentData|LanguageLevel):\s*(.*)$", text)]


for row in magic:
    path = ROOT / row["path"]
    if row["magic_kind"] == "postscript":
        raw = path.read_bytes()
        prefix, suffix = raw[:65536].decode("latin1"), raw[-8192:].decode("latin1")
        postscript.append({"path": row["path"], "bytes": len(raw), "sha256": sha(raw),
                           "prefix_dsc": dsc(prefix), "tail_dsc": dsc(suffix),
                           "first_line": prefix.split("\n", 1)[0],
                           "standing": "PostScript source program held. Only DSC comments and file identity inventoried; no interpreter execution or source-body correctness claim."})
    elif row["magic_kind"] == "gzip":
        try:
            with gzip.open(path, "rb") as handle:
                data = handle.read(64*1024*1024+1)
            over = len(data) > 64*1024*1024
            head = data[:65536]
            kind = "postscript" if head.startswith(b"%!PS") else "quoted_postscript" if head.startswith(b">%!PS") else "pdf" if head.startswith(b"%PDF-") else "dvi" if head.startswith(b"\xf7") else "other"
            compressed.append({"path": row["path"], "compressed_bytes": int(row["bytes"]), "expanded_bytes_read": len(data),
                               "complete_stream_read": not over, "expanded_sha256": sha(data) if not over else None,
                               "expanded_kind": kind, "prefix_dsc": dsc(head.decode("latin1")) if kind == "postscript" else [],
                               "standing": "Decoded only in memory for identity/metadata; no file written or content executed."})
        except Exception as error:
            compressed.append({"path": row["path"], "error": str(error)})

for archive_row in archives:
    path = ROOT / archive_row["path"]
    with zipfile.ZipFile(path) as archive:
        if archive_row["role"] == "docx":
            xml = ET.fromstring(archive.read("word/document.xml"))
            namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            paragraphs = ["".join(t.text or "" for t in p.findall(".//w:t", namespace)) for p in xml.findall(".//w:p", namespace)]
            text = "\n".join(paragraphs)
            docs.append({"path": archive_row["path"], "sha256": sha(path.read_bytes()), "paragraph_count": len(paragraphs),
                         "text_characters": len(text), "complete_document_text": text,
                         "standing": "All WordprocessingML paragraph text extracted; this may be a citation export rather than a chapter body. No Word rendering or edits."})
        else:
            for member in archive_row["document_members"]:
                if Path(member["name"]).suffix.lower() != ".pdf":
                    continue
                if member["bytes"] > 64*1024*1024:
                    members.append({"archive": archive_row["path"], **member, "state": "not_read_size_boundary"})
                    continue
                data = archive.read(member["name"])
                digest = sha(data)
                members.append({"archive": archive_row["path"], **member, "sha256": digest,
                                "pdf_header": data.startswith(b"%PDF-"),
                                "identical_uncompressed_pdf": pdf_hashes.get(digest),
                                "standing": "Archive member read only in memory and SHA256 compared with physical PDF identities. No extraction file created."})

ps_hashes = {r["sha256"]: r["path"] for r in postscript}
for row in compressed:
    row["identical_uncompressed_postscript"] = ps_hashes.get(row.get("expanded_sha256"))
summary = {"postscript_files": len(postscript), "gzip_files": len(compressed),
           "gzip_expanded_kinds": dict(collections.Counter(r.get("expanded_kind", "error") for r in compressed)),
           "gzip_stream_errors_or_incomplete": [r["path"] for r in compressed if r.get("error") or not r.get("complete_stream_read")],
           "docx_files": len(docs), "unique_docx_byte_identities": len({r["sha256"] for r in docs}),
           "docx_text_length_min_max": [min(r["text_characters"] for r in docs), max(r["text_characters"] for r in docs)],
           "embedded_pdf_members": len(members),
           "embedded_pdf_members_identical_to_physical_files": sum(bool(r.get("identical_uncompressed_pdf")) for r in members),
           "embedded_pdf_members_without_physical_identity": [r for r in members if not r.get("identical_uncompressed_pdf")],
           "method": "Metadata, XML text and bounded in-memory decompression only. No document/PS execution, source edits, new downloads or rendering."}
for name, value in (("postscript-source-inventory.json", postscript), ("gzip-source-inventory.json", compressed),
                    ("word-source-exports-inventory.json", docs), ("embedded-pdf-source-inventory.json", members),
                    ("nonpdf-source-summary.json", summary)):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
for row in docs:
    if row["path"].endswith(".docx"):
        print(row["path"] + "\n" + row["complete_document_text"] + "\n")
