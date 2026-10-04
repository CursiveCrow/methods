"""Locate exact-source candidates in the fully enumerated held-PDF identity data."""
from __future__ import annotations

import collections
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def norm(value):
    value = value.replace(r"\mu", "mu").replace("μ", "mu").replace("µ", "mu")
    value = re.sub(r"\\[\"'`^~=.Hckbduvr]\s*\{?([A-Za-z])\}?", r"\1", value)
    value = re.sub(r"\\[A-Za-z]+", "", value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", value.lower())


keys = json.loads((OUT / "bibliography-current-keys.json").read_text(encoding="utf-8"))
pdfs = json.loads((OUT / "pdf-holdings-identities.json").read_text(encoding="utf-8"))
sources = []
for pdf in pdfs:
    if pdf["representative"].startswith(("handbook/", "source/")):
        continue
    metadata = pdf.get("metadata", {})
    pages = pdf.get("opening_page_text", [])
    title = metadata.get("/Title", "")
    text = "\n".join(p.get("text", "") for p in pages)
    sources.append({"pdf": pdf, "title": title, "title_norm": norm(title),
                    "page_heads": [{"physical_page": p["physical_page"], "text": p.get("text", "")[:1800],
                                    "norm": norm(p.get("text", "")[:1800])} for p in pages[:4]],
                    "all_norm": norm(text), "all_text": text,
                    "metadata_norm": norm(" ".join(metadata.values()))})

rows = []
for entry in keys:
    title = norm(entry["title"])
    people = entry["fields"].get("author", entry["fields"].get("editor", ""))
    surnames = [norm(p.split(",")[0]) for p in people.split(" and ")]
    surnames = [s for s in surnames if len(s) >= 3]
    year = entry["year_or_date"][:4]
    doi = entry["doi"].lower()
    candidates = []
    for source in sources:
        if len(title) < 8:
            continue
        title_meta = title == source["title_norm"]
        title_heads = [p for p in source["page_heads"] if title in p["norm"]]
        title_body = title in source["all_norm"]
        doi_found = bool(doi and doi in source["all_text"].lower())
        if not (title_meta or title_heads or doi_found):
            continue
        author_hits = [s for s in surnames if s in source["all_norm"] or s in source["metadata_norm"]]
        year_present = bool(re.fullmatch(r"\d{4}", year) and re.search(r"(?<!\d)" + year + r"(?!\d)", source["all_text"]))
        score = 80*title_meta + 35*bool(title_heads) + 20*doi_found + min(30, 10*len(author_hits)) + 10*year_present
        if score < 45:
            continue
        pdf = source["pdf"]
        candidates.append({"sha256": pdf["sha256"], "file": pdf["representative"], "all_physical_copies": [r["path"] for r in pdf["physical_copies"]],
                           "pages": pdf.get("pages"), "metadata_title": source["title"], "metadata_author": pdf.get("metadata", {}).get("/Author", ""),
                           "score_for_inspection_order_only": score, "exact_metadata_title_match": title_meta,
                           "opening_pages_with_title_in_first_1800_characters": [p["physical_page"] for p in title_heads],
                           "surname_tokens_found": author_hits, "year_found_in_opening_text": year_present,
                           "doi_found_in_opening_text": doi_found,
                           "opening_evidence": [{"physical_page": p["physical_page"], "text": p["text"]} for p in title_heads[:2]],
                           "standing": "Candidate only: the title/author/year can occur in a review, contents page, bibliography, different edition or partial extract. Read the page context and extent before admitting an exact holding."})
    candidates.sort(key=lambda c: (-c["score_for_inspection_order_only"], c["file"]))
    rows.append({"key": entry["key"], "title": entry["title"], "author_or_editor": entry["author_or_editor"],
                 "year_or_date": entry["year_or_date"], "edition": entry["edition"], "doi": entry["doi"],
                 "current_citation_count": entry["active_citation_count"], "pdf_candidates": candidates,
                 "note_candidate_count": len(entry["exact_key_or_doi_note_candidates"]),
                 "source_identity_inventory_complete": False})

(OUT / "bibliography-pdf-candidates.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
summary = {"bibliography_keys": len(rows), "keys_with_pdf_candidates": sum(bool(r["pdf_candidates"]) for r in rows),
           "candidate_matches": sum(len(r["pdf_candidates"]) for r in rows),
           "keys_without_pdf_or_note_candidate": [r["key"] for r in rows if not r["pdf_candidates"] and not r["note_candidate_count"]],
           "method": "All 630 keys compared to extracted identity text for all held PDF byte identities. Candidates only; metadata or a name match is never promoted to exact-source identity."}
(OUT / "bibliography-pdf-candidates-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
md = ["# Bibliography and held-PDF identity candidates", "", "This is an inspection queue for every current bibliography key. All candidate matches remain unadmitted until the actual context, version and extent are checked. A file with a matching title can be a review, contents page or partial extract.", "",
      "| Key | Required title and date | Candidate held source files |", "| --- | --- | --- |"]
for row in rows:
    values = [f"{c['file']} ({c.get('pages')} pages; inspection score {c['score_for_inspection_order_only']})" for c in row["pdf_candidates"][:5]]
    md.append("| " + row["key"] + " | " + (row["title"]+"; "+row["year_or_date"]).replace("|", "\\|").replace("\n", " ") + " | " + ("; ".join(values) if values else "No candidate from the inspected PDF identity text; recorded note evidence remains separate.") + " |")
(OUT / "bibliography-pdf-candidates.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
