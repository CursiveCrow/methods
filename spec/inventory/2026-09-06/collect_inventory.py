"""Read-only manuscript census; generated outputs stay in this audit directory."""
from __future__ import annotations

import collections
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path("C:/Dev/the-methods-of-reason")
HB = ROOT / "handbook"
OUT = ROOT / "spec/inventory/2026-09-06"
sys.path.insert(0, str(ROOT / "tools"))
sys.dont_write_bytecode = True
import check as tex


def rel(path):
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")


def table(name, rows, fields=None):
    rows = list(rows)
    if not fields:
        fields = list(dict.fromkeys(k for row in rows for k in row))
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict))
                             else v for k, v in row.items()})


def read(path):
    return path.read_text(encoding="utf-8-sig", errors="replace")


def hash_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_category(path):
    value = rel(path)
    if value.startswith("handbook/"):
        return "manuscript_source" if path.suffix.lower() in {".tex", ".sty", ".bib", ".csv", ".md"} else "manuscript_build_or_asset"
    if value.startswith("source/"):
        return "archival_source"
    if value.startswith("spec/registers/"):
        return "requirement_register"
    if value.startswith("spec/research/"):
        return "research_and_review_notes"
    if value.startswith(("spec/verification/", "spec/provenance/")):
        return "verification_and_provenance"
    if value.startswith("spec/full-compendium-coverage-manifest."):
        return "legacy_coverage_catalog"
    if value.startswith("spec/"):
        return "specification_and_ledgers"
    if value.startswith("tools/"):
        return "tooling"
    if value.startswith("tmp/"):
        return "acquisition_and_working_artifacts"
    return "other_project_files"


started = datetime.now(timezone.utc).isoformat()
files, links, read_errors = [], [], []
if "--refresh-text" in sys.argv:
    # Reuse the immutable initial physical census. Never rebaseline the book.
    with (OUT / "workspace-files.csv").open(encoding="utf-8", newline="") as handle:
        files = list(csv.DictReader(handle))
    for row in files:
        row["bytes"] = int(row["bytes"])
    baseline = json.loads(read(OUT / "manuscript-snapshot-before.json"))
    snapshot = baseline["files"]
    aggregate = baseline["aggregate_sha256"]
else:
    if (OUT / "manuscript-snapshot-before.json").exists():
        raise SystemExit("Initial snapshot already exists. Use --refresh-text to preserve it.")
    for current, dirs, names in os.walk(ROOT, followlinks=False):
        current = Path(current)
        kept = []
        for directory in sorted(dirs):
            path = current / directory
            if directory == ".git" or path == OUT.parent:
                continue
            if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
                links.append({"path": rel(path), "kind": "unfollowed_directory_link"})
                continue
            kept.append(directory)
        dirs[:] = kept
        for name in sorted(names):
            path = current / name
            try:
                stat = path.stat()
                files.append({"path": rel(path), "bytes": stat.st_size,
                              "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                              "extension": path.suffix.lower(), "category": file_category(path)})
            except OSError as error:
                read_errors.append({"path": rel(path), "error": str(error)})
    files.sort(key=lambda row: row["path"])
    table("workspace-files.csv", files)
    dump("unfollowed-links-and-read-errors.json", {"links": links, "errors": read_errors})

    # Snapshot all reader-source files, publication/image assets, four registers,
    # the governing contract/conventions, and the frozen inherited source.
    snapshot = []
    snapshot_suffixes = {".tex", ".sty", ".bib", ".csv", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".eps", ".ps"}
    for row in files:
        path = ROOT / row["path"]
        selected = (row["path"].startswith("handbook/") and path.suffix.lower() in snapshot_suffixes)
        selected |= row["path"].startswith("spec/registers/") and path.suffix.lower() in {".csv", ".md"}
        selected |= row["path"] in {"source/formal-logic-reference.tex", "source/formal-logic-reference.pdf",
                                   "spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md",
                                   "spec/INHERITED-CORPUS-MANIFEST.md"}
        if selected:
            snapshot.append({"path": row["path"], "bytes": row["bytes"], "sha256": hash_file(path)})
    aggregate = hashlib.sha256("".join(f'{r["path"]}\t{r["sha256"]}\n' for r in snapshot).encode()).hexdigest()
    dump("manuscript-snapshot-before.json", {"captured_utc": started, "aggregate_sha256": aggregate, "files": snapshot})

cache = {}
def source(path):
    key = str(path)
    if key not in cache:
        raw = read(path)
        body = tex.strip_verbatims(tex.strip_comments(raw))
        body = re.sub(r"\\verb\*?([^A-Za-z\s])(.*?)\1", lambda m: " " * len(m.group(0)), body)
        cache[key] = (raw, body)
    return cache[key]


def after_options(body, index):
    while True:
        while index < len(body) and body[index].isspace():
            index += 1
        if index >= len(body) or body[index] != "[":
            return index
        depth = 1
        index += 1
        while index < len(body) and depth:
            if body[index] == "\\":
                index += 2
                continue
            if body[index] == "[":
                depth += 1
            elif body[index] == "]":
                depth -= 1
            index += 1


edge_pattern = re.compile(r"\\(input|include|showcalculus)\s*\{([^{}]+)\}")
reachable, edges, dynamic, contexts = set(), [], [], collections.defaultdict(set)
visits = set()


def walk(path, part="front_back", area="front_back"):
    path = path.resolve()
    if not path.is_file():
        return
    key = (str(path), part, area)
    if key in visits:
        return
    visits.add(key)
    reachable.add(path)
    contexts[path].add((part, area))
    _, body = source(path)
    for found in edge_pattern.finditer(body):
        command, reference = found.groups()
        target_ref = ("registry/calculi/" + reference if command == "showcalculus" else reference)
        new_part, new_area = part, area
        owner = re.match(r"(parts|annex)/p(\d\d)(?:[/. -]|$)", target_ref)
        if owner:
            new_part = "P" + str(int(owner.group(2)))
            new_area = "body" if owner.group(1) == "parts" else "annex"
        if command == "showcalculus":
            new_area = "calculus"
        line = body.count("\n", 0, found.start()) + 1
        if "#" in target_ref or "\\" in target_ref:
            dynamic.append({"file": rel(path), "line": line, "command": command, "reference": reference})
            continue
        if not Path(target_ref).suffix:
            target_ref += ".tex"
        target = (HB / target_ref).resolve()
        edges.append({"parent": rel(path), "line": line, "command": command, "target": rel(target),
                      "part": new_part, "area": new_area, "exists": target.is_file()})
        walk(target, new_part, new_area)


walk(HB / "main.tex")
all_tex = sorted(ROOT / row["path"] for row in files if row["path"].startswith("handbook/") and row["extension"] == ".tex")
mathematical = {"hbtheorem", "hblemma", "hbcorollary", "hbdefinition", "hbconvention",
                "hbmethod", "hbexample", "hbwarning", "proofboundary", "annexitem", "systementry",
                "theorem", "lemma", "corollary", "proposition", "definition", "example", "proof", "proofplan"}
arg_count = {name: 2 for name in ("hbdefinition", "hbconvention", "hbmethod", "hbexample", "hbwarning", "proofboundary", "systementry")}
arg_count.update({name: 3 for name in ("hbtheorem", "hblemma", "hbcorollary", "annexitem")})
units, headings, labels, references, citations, rule_rows, literal_markers, inventory = [], [], [], [], [], [], [], []
statuses = []
all_environments, captions, explicit_index_entries = [], [], []
counts_by_part = collections.defaultdict(collections.Counter)
for path in all_tex:
    raw, body = source(path)
    active = path.resolve() in reachable
    owners = sorted({p for p, _ in contexts.get(path.resolve(), set())})
    areas = sorted({a for _, a in contexts.get(path.resolve(), set())})
    role = "calculus" if "/registry/calculi/" in path.as_posix() else "generated" if "/generated/" in path.as_posix() else "reader_or_driver"
    inventory.append({"path": rel(path), "active": active, "parts": owners, "areas": areas, "role": role,
                      "lines": len(raw.splitlines()), "bytes": path.stat().st_size})
    for match in re.finditer(r"\\begin\{([^{}]+)\}", body):
        kind = match.group(1)
        if active:
            all_environments.append({"file": rel(path), "line": body.count("\n", 0, match.start())+1,
                                     "parts": owners, "areas": areas, "kind": kind})
        if kind not in mathematical:
            continue
        args, _ = tex.scan_braced_args(body, match.end(), arg_count.get(kind, 0))
        label = args[0].strip() if args and kind in arg_count else ""
        status = args[1].strip() if kind in {"hbtheorem", "hblemma", "hbcorollary"} and len(args) > 1 else ""
        title = args[-1].strip() if args and len(args) == arg_count[kind] else ""
        if not args:
            end = body.find(r"\end{" + kind + "}", match.end())
            segment = body[match.end():end if end >= 0 else match.end()+2000]
            found_label = re.search(r"\\label\s*\{([^{}]+)\}", segment)
            label = found_label.group(1) if found_label else ""
            found_title = re.match(r"\s*\[([^\]]*)\]", segment)
            title = found_title.group(1) if found_title else ""
        row = {"file": rel(path), "line": body.count("\n", 0, match.start())+1, "active": active,
               "parts": owners, "areas": areas, "kind": kind, "label": label, "title": title,
               "declared_status": status, "backref": args[1].strip() if kind == "annexitem" and len(args)>1 else ""}
        units.append(row)
        if active:
            for part in owners:
                counts_by_part[part][kind] += 1
                if status:
                    counts_by_part[part]["status_" + status.split("=", 1)[0]] += 1
        if active and label:
            labels.append({"label": label, "file": rel(path), "line": row["line"], "origin": kind})
        if active and status:
            statuses.append({"file": rel(path), "line": row["line"], "parts": owners,
                             "origin": kind, "owner_label": label, "status": status})
            if status.startswith("cited="):
                for key in status.split("=", 1)[1].split(","):
                    citations.append({"key": key.strip(), "file": rel(path), "line": row["line"], "command": kind + "_status"})
    if not active:
        continue
    for match in re.finditer(r"\\(part|chapter|section|subsection|subsubsection|paragraph|subparagraph)(?![A-Za-z@])\*?\s*", body):
        args, _ = tex.scan_braced_args(body, after_options(body, match.end()), 1)
        if args:
            headings.append({"file": rel(path), "line": body.count("\n",0,match.start())+1,
                             "parts": owners, "level": match.group(1), "title": args[0]})
    for match in re.finditer(r"\\label\s*\{([^{}]+)\}", body):
        labels.append({"label": match.group(1), "file": rel(path), "line": body.count("\n",0,match.start())+1, "origin": "literal_label"})
    for match in re.finditer(r"\\(ref|pageref|eqref|autoref|cref|Cref)\*?\s*\{([^{}]+)\}|\\hyperref\[([^\]]+)\]", body):
        for target in (match.group(2) or match.group(3)).split(","):
            references.append({"target": target.strip(), "file": rel(path), "line": body.count("\n",0,match.start())+1})
    for match in re.finditer(r"\\(calculussheet|hbrule)\s*", body):
        n = 3 if match.group(1) == "calculussheet" else 5
        args, _ = tex.scan_braced_args(body, match.end(), n)
        if len(args) != n:
            continue
        labels.append({"label": args[0], "file": rel(path), "line": body.count("\n",0,match.start())+1, "origin": match.group(1)})
        rule_rows.append({"file": rel(path), "parts": owners, "kind": match.group(1),
                          "label": args[0], "name": args[1], "line": body.count("\n",0,match.start())+1})
    for match in re.finditer(r"\\(cite|textcite|autocite|parencite|nocite|citeauthor|citetitle|citeyear|citeyearpar|entrysources)(?![A-Za-z@])\*?", body):
        args, _ = tex.scan_braced_args(body, after_options(body, match.end()), 1)
        if args:
            for key in args[0].split(","):
                citations.append({"key": key.strip(), "file": rel(path), "line": body.count("\n",0,match.start())+1, "command": match.group(1)})
    for match in re.finditer(r"\\(entryadequacy|entrydecidability)(?![A-Za-z@])", body):
        args, _ = tex.scan_braced_args(body, match.end(), 2)
        if len(args) == 2:
            status = args[0].strip()
            line = body.count("\n", 0, match.start()) + 1
            statuses.append({"file": rel(path), "line": line, "parts": owners,
                             "origin": match.group(1), "owner_label": "", "status": status})
            if status.startswith("cited="):
                for key in status.split("=", 1)[1].split(","):
                    citations.append({"key": key.strip(), "file": rel(path), "line": line, "command": match.group(1) + "_status"})
    for match in re.finditer(r"\\(caption|captionof|index)(?![A-Za-z@])\*?", body):
        n = 2 if match.group(1) == "captionof" else 1
        args, _ = tex.scan_braced_args(body, after_options(body, match.end()), n)
        if len(args) == n:
            row = {"file": rel(path), "line": body.count("\n", 0, match.start())+1,
                   "parts": owners, "command": match.group(1), "text": args[-1]}
            (explicit_index_entries if match.group(1) == "index" else captions).append(row)
    for match in re.finditer(r"\\hbstub\s*\{|\\sketchnote\s*\{|\\begin\{proofboundary\}|(?im:^[^\n]*(?:TODO|FIXME|TBD)[^\n]*)", body):
        literal_markers.append({"file": rel(path), "line": body.count("\n",0,match.start())+1,
                                "marker": match.group(0), "parts": owners})

table("latex-files.csv", inventory)
table("input-edges.csv", edges)
table("headings.csv", headings)
table("mathematical-environments.csv", units)
table("calculus-rules.csv", rule_rows)
table("citation-occurrences.csv", citations)
table("status-declarations.csv", statuses)
table("all-environments.csv", all_environments)
table("captions.csv", captions)
table("explicit-index-entries.csv", explicit_index_entries)
proof_headings = [r for r in headings if re.search(r"\b(proof|sketch|derivation|completeness|soundness|construction)\b", r["title"], re.I)]
table("proof-and-result-headings.csv", proof_headings)
dump("dynamic-inputs.json", dynamic)
dump("explicit-markers.json", literal_markers)

bib_text = read(HB / "bib/handbook.bib")
entries = []
bib_matches = list(re.finditer(r"@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", bib_text))
for i, match in enumerate(bib_matches):
    end = bib_matches[i+1].start() if i+1<len(bib_matches) else len(bib_text)
    entry = bib_text[match.start():end]
    title_match = re.search(r"\btitle\s*=\s*", entry, re.I)
    title = ""
    if title_match:
        args, _ = tex.scan_braced_args(entry, title_match.end(), 1)
        title = args[0] if args else ""
    entries.append({"key": match.group(2), "type": match.group(1).lower(), "title": title,
                    "line": bib_text.count("\n",0,match.start())+1,
                    "stub_marker": bool(re.search(r"keywords\s*=\s*\{[^}]*\bstub\b", entry, re.I)),
                    "cited": any(c["key"] == match.group(2) for c in citations)})
table("bibliography.csv", entries)
bibkeys = {r["key"] for r in entries}
known_labels = {r["label"] for r in labels}
proof_links = []
for status in statuses:
    if status["status"].startswith(("proved=", "sketched=")):
        target = status["status"].split("=", 1)[1].strip()
        proof_links.append({**status, "target": target, "target_defined_on_reader_route": target in known_labels,
                            "target_locations": [r for r in labels if r["label"] == target]})
table("proof-links.csv", proof_links)
table("label-references.csv", references)
dump("reference-candidates.json", {
    "method": "Literal reader-route labels/refs; dynamic labels and source hooks require separate interpretation.",
    "unresolved_literal_targets": sorted({r["target"] for r in references if r["target"] not in known_labels and "#" not in r["target"]}),
    "missing_bib_keys": sorted({r["key"] for r in citations if r["key"] not in bibkeys and r["key"] != "*" and "#" not in r["key"]}),
    "duplicate_bib_keys": [k for k,n in collections.Counter(r["key"] for r in entries).items() if n>1],
    "label_definitions": labels
})

registers = []
for name in ("new-content", "depth-gaps", "defects", "apparatus"):
    with (ROOT / "spec/registers" / (name+".csv")).open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            registers.append({"register": name, **row})
dump("original-registers.json", registers)

pdfs = []
magic_path = OUT / "document-magic-inventory.json"
additional_document_paths = {r["path"] for r in json.loads(read(magic_path)) if r["magic_kind"] in {"pdf", "postscript"}} if magic_path.exists() else set()
for row in files:
    path = ROOT / row["path"]
    if path.suffix.lower() not in {".pdf", ".body", ".ps", ".eps"} and row["path"] not in additional_document_paths:
        continue
    try:
        with path.open("rb") as handle:
            header = handle.read(8)
        kind = "pdf" if header.startswith(b"%PDF-") else "postscript" if header.startswith(b"%!PS") else "not_pdf_or_postscript"
        pdfs.append({**row, "header_type": kind})
    except OSError as error:
        read_errors.append({"path": row["path"], "error": str(error)})
table("source-and-pdf-files.csv", pdfs)

artifact = {"path": "handbook/main.pdf", "sha256": hash_file(HB/"main.pdf")}
try:
    from pypdf import PdfReader
    reader = PdfReader(str(HB/"main.pdf"))
    artifact.update({"pages": len(reader.pages), "metadata": {str(k):str(v) for k,v in (reader.metadata or {}).items()}})
except Exception as error:
    artifact["metadata_read_error"] = str(error)

git = {}
for key, args in (("head", ["rev-parse", "HEAD"]), ("branch", ["branch", "--show-current"])):
    git[key] = subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
status = subprocess.check_output(["git", "status", "--porcelain=v1", "-uall"], cwd=ROOT, text=True).splitlines()
status = [s for s in status if "spec/inventory/" not in s]
table("git-state.csv", [{"status":s[:2], "path":s[3:]} for s in status])
git["status_counts"] = dict(collections.Counter(s[:2] for s in status))

category_totals = {}
for row in files:
    count = category_totals.setdefault(row["category"], {"files":0, "bytes":0})
    count["files"] += 1
    count["bytes"] += row["bytes"]
active_inventory = [r for r in inventory if r["active"]]
active_units = [r for r in units if r["active"]]
summary = {
    "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
    "root": str(ROOT), "snapshot_sha256": aggregate, "snapshot_files": len(snapshot),
    "workspace_files_excluding_git_links_and_this_audit": len(files), "category_totals": category_totals,
    "git": git, "artifact": artifact,
    "handbook_tex_files": len(inventory), "reachable_tex_files": len(active_inventory),
    "unreachable_tex_files": len(inventory)-len(active_inventory),
    "reachable_source_lines": sum(r["lines"] for r in active_inventory),
    "reachable_tex_bytes": sum(r["bytes"] for r in active_inventory),
    "missing_literal_input_edges": [r for r in edges if not r["exists"]],
    "dynamic_input_count": len(dynamic),
    "active_environment_counts": dict(collections.Counter(r["kind"] for r in active_units)),
    "all_active_environment_counts": dict(collections.Counter(r["kind"] for r in all_environments)),
    "caption_commands": len(captions),
    "explicit_index_commands": len(explicit_index_entries),
    "declared_result_status_counts": dict(collections.Counter(r["declared_status"].split("=",1)[0] for r in active_units if r["declared_status"])),
    "entry_card_status_counts": dict(collections.Counter(r["status"].split("=",1)[0] for r in statuses if r["origin"].startswith("entry"))),
    "proof_and_result_heading_counts": dict(collections.Counter(r["level"] for r in proof_headings)),
    "unresolved_proof_link_targets": sorted({r["target"] for r in proof_links if not r["target_defined_on_reader_route"]}),
    "per_part_environment_counts": {k:dict(v) for k,v in sorted(counts_by_part.items())},
    "active_calculus_sheets": sum(r["kind"]=="calculussheet" for r in rule_rows),
    "active_rule_rows": sum(r["kind"]=="hbrule" for r in rule_rows),
    "bibliography_entries": len(entries), "bibliography_stub_markers": sum(r["stub_marker"] for r in entries),
    "distinct_cited_keys": len({r["key"] for r in citations}),
    "register_counts": dict(collections.Counter(r["register"] for r in registers)),
    "physical_pdf_header_files": sum(r["header_type"]=="pdf" for r in pdfs),
    "pdf_extension_non_pdf_headers": [r["path"] for r in pdfs if r["extension"]==".pdf" and r["header_type"]!="pdf"],
    "tool_test_files": sum(r["path"].startswith("tools/test_") and r["extension"]==".py" for r in files),
    "method_limits": [
        "Reader graph follows literal input/include and the known showcalculus macro, without executing TeX.",
        "Counts are unique physical source files/environments, not counts of printed occurrences, propositions, or completed requirements.",
        "Declared proved/sketched/cited status is recorded, not revalidated mathematically.",
        "Workspace and PDF holdings counts are physical files and may include duplicates, failed downloads, and manuscript builds.",
        "Multi-GB coverage catalogs were inventoried by path/size only, not read as a progress denominator."
    ]
}
dump("inventory-summary.json", summary)
print(json.dumps(summary, ensure_ascii=False, indent=2))
