"""Inventory saved B7 candidate intakes; no canonical writes, checks or reviews."""
from __future__ import annotations
import copy, csv, hashlib, importlib.util, io, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
BASE = ROOT/"handbook"
spec = importlib.util.spec_from_file_location(
    "batch7_baseline_support", OUT/"capture_batch7_baseline.py")
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
grounded = support.helper.grounded
registry = support.helper.registry
FIELDS = registry.HEADER
MANIFEST = ROOT/"spec/research/edition-2026-authoring-batch-intake-7.json"

def digest(data):
    return hashlib.sha256(data).hexdigest()

def public_declaration(d):
    return {"label":d.label,"path":d.path,"line":d.line,"kind":d.kind,
            "owner":d.owner,"part":d.part,"chapter":d.chapter,
            "start":d.start,"end":d.end}

def identity(value):
    return re.sub(r"\s+"," ",re.sub(r"[{}]","",value or "")).strip().casefold()

def publication_year(fields):
    return (fields.get("year") or fields.get("date") or "")[:4]

def source_locators(record):
    values = grounded.fields(record)
    found = set(grounded.locators(record))
    for field in ("eprint","url","note"):
        for value in re.findall(r"\b[A-Za-z][A-Za-z.-]*/[0-9]{7}v[0-9]+\b",
                                values.get(field,"")):
            found.add("arxiv:"+value)
    return sorted(found)

def publication_candidates(record, canonical):
    incoming = grounded.fields(record)
    locators = set(source_locators(record))
    results = []
    for old in canonical:
        conflicts = []
        fields = grounded.fields(old)
        shared = sorted(locators & set(source_locators(old)))
        isbn = incoming.get("isbn") and identity(incoming["isbn"]) == identity(fields.get("isbn"))
        same_identity = all(incoming.get(k) and fields.get(k) and
            identity(incoming[k]) == identity(fields[k]) for k in ("author","title"))
        same_identity = same_identity and bool(publication_year(incoming)) and \
            publication_year(incoming) == publication_year(fields)
        identity_fields = ("booktitle","journaltitle","volume","number","pages",
                           "publisher","editor","isbn")
        identity_conflicts = [k for k in identity_fields if incoming.get(k) and fields.get(k)
            and identity(incoming[k]) != identity(fields[k])]
        conflicts = [k for k in ("edition","version","eprint") if incoming.get(k) and fields.get(k)
            and identity(incoming[k]) != identity(fields[k])]
        if old["key"] == record["key"]:
            status = ("identical-key-and-record-reuse" if
                record["comparison"] == old["comparison"] else
                ("same-key-verified-publication-metadata-reuse-candidate"
                 if same_identity and not identity_conflicts and not conflicts
                 else "same-key-different-record-root-decision"))
        elif same_identity:
            status = ("metadata-and-publication-locator-reuse-candidate" if not conflicts else
                      "publication-match-with-version-conflict-held")
            if identity_conflicts:
                status = "publication-core-match-with-container-conflicts-held"
            elif not shared and not isbn:
                status = "exact-author-title-year-publication-reuse-candidate"
        elif shared:
            conflicts = []
            status = "shared-source-locator-nonidentical-publication-held"
        else:
            continue
        results.append({"canonical_key":old["key"],"standing":status,
            "shared_exact_locators":shared,"same_isbn":bool(isbn),
            "incoming_fields":incoming,"canonical_fields":fields,
            "canonical_record":old["raw"],
            "version_conflicts":conflicts,"container_conflicts":identity_conflicts,
            "identity_basis":"Exact author/title and normalized publication year; all shared container/version fields shown. Saved-record comparison only."})
    return results

def main():
    started = datetime.now(timezone.utc)
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8-sig"))
    manifest_evidence = OUT/("manifest-"+digest(manifest_bytes)+".json")
    if manifest_evidence.exists() and manifest_evidence.read_bytes()!=manifest_bytes:
        raise RuntimeError("Immutable manifest evidence conflict")
    if not manifest_evidence.exists():
        manifest_evidence.write_bytes(manifest_bytes)
    baseline_path = OUT/"pre-batch7-numeric-meanings.json"
    frozen = json.loads(baseline_path.read_text(encoding="utf-8"))
    recorded = {}
    recorded_bytes = {}
    def snapshot(path):
        key = path.relative_to(ROOT).as_posix()
        if key in recorded:
            return recorded[key]
        if not path.is_file():
            recorded[key] = {"path":key,"exists":False}
            return recorded[key]
        data = path.read_bytes()
        recorded_bytes[key] = data
        recorded[key] = {"path":key,"exists":True,"sha256":digest(data),
            "bytes":len(data),"text":data.decode("utf-8-sig")}
        return recorded[key]
    canonical_paths = [BASE/"registry/symbols.csv",BASE/"registry/symbol-scopes.json",
                       BASE/"bib/handbook.bib"]
    canonical_snapshots = [snapshot(p) for p in canonical_paths]
    canonical_rows = list(csv.DictReader(io.StringIO(canonical_snapshots[0]["text"])))
    canonical_tuples = {tuple(r.get(k,"") for k in FIELDS) for r in canonical_rows}
    canonical_scopes = json.loads(canonical_snapshots[1]["text"])["scopes"]
    canonical_bib = grounded.bib_records(canonical_snapshots[2]["text"])
    for driver in [BASE/"main.tex"]+sorted((BASE/"parts").glob("p[0-9][0-9].tex"))+ \
                  sorted((BASE/"annex").glob("p[0-9][0-9].tex")):
        snapshot(driver)
    actual = registry.ReaderIndex(BASE)
    actual_files = set(actual.files)
    # Candidate declarations live in a separate index and have no chapter credit.
    candidates = copy.deepcopy(actual)
    for group in manifest["groups"]:
        for rel in group.get("bodies",[])+group.get("annexes",[])+group.get("rule_sheets",[]):
            source = snapshot(BASE/rel)
            if source["exists"] and rel not in actual_files and rel not in candidates.files:
                candidates._close_headings(0)
                candidates._visit(rel,int(group["part"][1:]))
                candidates._close_headings(0)
                for items in candidates.labels.values():
                    for d in items:
                        if d.path == rel:
                            d.chapter = None
                for h in candidates.heading_records:
                    if h.path == rel:
                        h.chapter = None
                for region in candidates.files.get(rel,[]):
                    region.chapter = None
    for items in candidates.labels.values():
        for d in items:
            if d.path not in actual_files:
                d.chapter = None
    for h in candidates.heading_records:
        if h.path not in actual_files:
            h.chapter = None
    for rel, regions in candidates.files.items():
        if rel not in actual_files:
            for region in regions:
                region.chapter = None
    confirmations_path = OUT/"root-confirmations.json"
    confirmations = json.loads(confirmations_path.read_text(encoding="utf-8")) if confirmations_path.exists() else {}
    groups, scopes, normalizations, all_bib, syntax_proposals = [], {}, [], [], []
    for group in manifest["groups"]:
        stem = group["stem"]
        merged = group.get("integration_status","").startswith("merged")
        owned = set(group.get("bodies",[])+group.get("annexes",[])+group.get("rule_sheets",[]))
        source_regions = []
        for rel in sorted(owned):
            source = snapshot(BASE/rel)
            source_regions.append({k:v for k,v in source.items() if k!="text"} |
                {"literal_actual_route_at_index_capture":rel in actual_files,
                 "candidate_only":rel not in actual_files})
        note = group.get("note")
        if note:
            snapshot(ROOT/note)
        rows, csv_inputs = [], []
        for rel in group.get("symbol_intakes",[]):
            source = snapshot(BASE/rel)
            csv_inputs.append({k:v for k,v in source.items() if k!="text"})
            if not source["exists"]:
                continue
            repaired_lines = []
            original_rows = list(csv.DictReader(io.StringIO(source["text"])))
            for number, line in enumerate(source["text"].splitlines(keepends=True),1):
                # A comma inside an unquoted math glyph is a CSV delimiter,
                # not an intentional eighth field. Preserve its spelling.
                match = re.match(r"^(\\\(.*?\\\)),",line)
                if match and "," in match[1]:
                    fixed = '"'+match[1].replace('"','""')+'",'+line[match.end():]
                    syntax_proposals.append({"group":stem,"intake":rel,
                        "physical_line":number,"original_line":line.rstrip("\r\n"),
                        "proposed_line":fixed.rstrip("\r\n"),"source_sha256":source["sha256"],
                        "standing":"Quote-only CSV serialization repair; glyph and all seven intended values unchanged. Original intake not edited."})
                    line = fixed
                repaired_lines.append(line)
            repaired_text = "".join(repaired_lines)
            if any(x["intake"]==rel for x in syntax_proposals):
                raw_name = "raw-"+Path(rel).name+"-"+source["sha256"]+".csv"
                fixed_name = "quote-only-"+Path(rel).name+"-"+source["sha256"]+".csv"
                raw_data = recorded_bytes[source["path"]]
                fixed_data = repaired_text.encode("utf-8")
                if raw_data.startswith(b"\xef\xbb\xbf"):
                    fixed_data = b"\xef\xbb\xbf"+fixed_data
                for name, data in ((raw_name,raw_data),(fixed_name,fixed_data)):
                    evidence_path = OUT/name
                    if evidence_path.exists() and evidence_path.read_bytes()!=data:
                        raise RuntimeError("Immutable CSV evidence name conflict: "+name)
                    if not evidence_path.exists():
                        evidence_path.write_bytes(data)
                for fix in syntax_proposals:
                    if fix["intake"]==rel:
                        fix["raw_byte_evidence"]=raw_name
                        fix["transformed_csv"]=fixed_name
                        fix["transformed_sha256"]=digest(fixed_data)
            reader = csv.DictReader(io.StringIO(repaired_text))
            for number, raw in enumerate(reader,2):
                row = {k:raw.get(k) for k in FIELDS}
                sites = candidates.labels.get(row.get("first_use"),[])
                local_sites = [d for d in sites if d.path in owned]
                exact_canonical = tuple(row.get(k,"") for k in FIELDS) in canonical_tuples
                proposed = {k:(row.get(k) or "").strip() for k in FIELDS}
                changes = []
                if not proposed["macro"]:
                    glyph = proposed["glyph"]
                    proposed["macro"] = glyph[2:-2] if glyph.startswith(r"\(") and glyph.endswith(r"\)") else glyph
                    changes.append("Fill blank macro with unchanged glyph spelling; no new TeX macro.")
                if not registry.PREC_RE.fullmatch(proposed["precedence"]):
                    descriptor = proposed["precedence"]
                    proposed["precedence"] = "n/a"
                    proposed["notes"] += (" " if proposed["notes"] else "") + \
                        "Original precedence descriptor "+repr(descriptor)+" retained; no rank inferred."
                    changes.append("Nonrank precedence descriptor retained in notes; propose n/a.")
                if proposed != row:
                    normalizations.append({"group":stem,"intake":rel,"record_number":number,
                        "original":row,"proposed":proposed,"changes":changes,
                        "standing":"Proposal only; original intake untouched."})
                item = {"intake":rel,"record_number":number,"raw":row,
                    "original_parser_fields":original_rows[number-2],
                    "header":reader.fieldnames,"overflow_fields":raw.get(None),
                    "canonical_exact_row_reuse":exact_canonical,
                    "excluded_already_merged_root":merged,
                    "candidate_declarations":[public_declaration(d) for d in local_sites],
                    "unresolved_first_use":not local_sites,
                    "unique_owned_first_use":len(local_sites)==1,
                    "normalization_proposed":proposed if proposed!=row else None}
                rows.append(item)
                if not merged and not exact_canonical:
                    name = proposed["scope"]
                    key = stem+"::"+name
                    if key not in scopes:
                        scopes[key] = {"group":stem,"scope":name,
                            "existing_named_scope":name in canonical_scopes,
                            "numeric_scope":registry.parse_scope(name) is not None,
                            "first_use_anchors":[],"minimal_candidate_regions":[],
                            "proposed_rows":[],
                            "standing":"Typed-scope preparation only; bounded anchor hints are NOT final usage bindings or route credit. Root must confirm actual routes, frozen input hashes and intended extent."}
                    scopes[key]["proposed_rows"].append({"intake":rel,"record_number":number,
                        "glyph":proposed["glyph"],"role":proposed["role"],
                        "first_use":proposed["first_use"]})
                    for d in local_sites:
                        if d.label not in scopes[key]["first_use_anchors"]:
                            scopes[key]["first_use_anchors"].append(d.label)
                        selector = {"anchor":d.label}
                        if selector not in scopes[key]["minimal_candidate_regions"]:
                            scopes[key]["minimal_candidate_regions"].append(selector)
                        for annex_sites in candidates.labels.values():
                            for annex in annex_sites:
                                if annex.kind=="annexitem" and annex.owner==d.label and annex.path in owned:
                                    selector = {"anchor":annex.label}
                                    if selector not in scopes[key]["minimal_candidate_regions"]:
                                        scopes[key]["minimal_candidate_regions"].append(selector)
        bib_inputs, records = [], []
        for rel in group.get("bibliography_intakes",[]):
            source = snapshot(BASE/rel)
            bib_inputs.append({k:v for k,v in source.items() if k!="text"})
            if not source["exists"]:
                continue
            for record in grounded.bib_records(source["text"]):
                reuse = publication_candidates(record,canonical_bib)
                item = {"group":stem,"intake":rel,"key":record["key"],
                    "raw":record["raw"],"fields":grounded.fields(record),
                    "exact_source_locators":source_locators(record),
                    "publication_reuse_candidates":reuse,
                    "standing":"Exact saved-record metadata comparison only, not external source/version/proof admission. No alias applied."}
                records.append(item)
                if not merged:
                    all_bib.append(item)
        frozen_status = group.get("integration_status","")
        groups.append({"stem":stem,"part":group["part"],
            "owner":group.get("owner"),
            "manifest_declared_proof_pairs":group.get("declared_proof_pairs"),
            "manifest_integration_status":frozen_status,
            "root_manifest_frozen_confirmation":frozen_status.startswith(("frozen","read","routed","merged")),
            "explicit_root_confirmation":confirmations.get(stem),
            "already_merged_root_excluded":merged,"source_regions":source_regions,
            "note":note,"symbol_inputs":csv_inputs,"bibliography_inputs":bib_inputs,
            "raw_symbol_records":len(rows),"raw_bibliography_records":len(records),
            "symbol_rows":rows,"bibliography_records":records,
            "standing":"Saved file presence is not an author freeze, routing approval, review or completion verdict."})
    candidate_exports = []
    for group in groups:
        if group["already_merged_root_excluded"]:
            continue
        export_rows = [r["normalization_proposed"] or r["raw"]
                       for r in group["symbol_rows"] if not r["canonical_exact_row_reuse"]]
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream,fieldnames=FIELDS,lineterminator="\n")
        writer.writeheader()
        writer.writerows(export_rows)
        data = stream.getvalue().encode("utf-8")
        export_name = "candidate-symbols-"+group["stem"]+"-"+digest(data)+".csv"
        export_path = OUT/export_name
        if export_path.exists() and export_path.read_bytes()!=data:
            raise RuntimeError("Immutable candidate dataset conflict")
        if not export_path.exists():
            export_path.write_bytes(data)
        candidate_exports.append({"group":group["stem"],"dataset":export_name,
            "sha256":digest(data),"rows":len(export_rows),
            "raw_scope_names_preserved":True,
            "standing":"Transformed candidate dataset only. Scope/type/alias decisions remain root-owned; do not append canonically before actual routes and coherent incoming pass."})
    changed = []
    for key,item in recorded.items():
        p = ROOT/key
        now = digest(p.read_bytes()) if p.is_file() else None
        if now != item.get("sha256"):
            changed.append({"path":key,"captured_sha256":item.get("sha256"),
                            "after_sha256":now})
    manifest_after = digest(MANIFEST.read_bytes())
    finished = datetime.now(timezone.utc)
    payload = {"capture_started_utc":started.isoformat(),"capture_finished_utc":finished.isoformat(),
        "manifest_sha256":digest(manifest_bytes),"manifest_after_sha256":manifest_after,
        "manifest_raw_evidence":manifest_evidence.name,
        "baseline_sha256":digest(baseline_path.read_bytes()),
        "baseline_utc":frozen["utc"],"baseline_symbols":frozen["canonical_row_count"],
        "baseline_bibliography":frozen["canonical_bib_count"],
        "actual_current_symbols":len(canonical_rows),"actual_current_bibliography":len(canonical_bib),
        "current_canonical_hashes":{x["path"]:x["sha256"] for x in canonical_snapshots},
        "groups":groups,"typed_scope_candidates":list(scopes.values()),
        "normalization_proposals":normalizations,"bibliography_candidates":all_bib,
        "csv_syntax_proposals":syntax_proposals,
        "candidate_csv_exports":candidate_exports,
        "changed_during_capture":changed,
        "non_atomic":bool(changed or manifest_after!=digest(manifest_bytes)),
        "batch6_pending_preserved":["p15-hintikka","p10-abelian"],
        "scope":manifest.get("scope"),
        "standing":"Preparation snapshot only. Off-route candidates remain off-route; no collision/strict check, proof/source review, build or render. No patches are applicable; no canonical, manuscript, driver, B6 history or manifest edits."}
    name = "inventory-"+finished.strftime("%Y%m%dT%H%M%S%fZ")+".json"
    target = OUT/name
    if target.exists():
        raise RuntimeError("Immutable inventory name unexpectedly exists")
    target.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    # Preserve all raw intake bytes, including comments and original line endings.
    raw_intakes = []
    for key, item in recorded.items():
        if item.get("exists") and key.startswith(("handbook/registry/symbols-intake-",
                                                  "handbook/bib/intake-")):
            name = "raw-intake-"+Path(key).name+"-"+item["sha256"]+Path(key).suffix
            evidence = OUT/name
            data = recorded_bytes[key]
            if evidence.exists() and evidence.read_bytes()!=data:
                raise RuntimeError("Immutable intake evidence conflict: "+name)
            if not evidence.exists():
                evidence.write_bytes(data)
            raw_intakes.append({"original_path":key,"evidence":name,
                "sha256":item["sha256"],"bytes":item["bytes"]})
    (OUT/"current-raw-intake-evidence.json").write_text(
        json.dumps(raw_intakes,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for group in groups:
        (OUT/("current-group-"+group["stem"]+".json")).write_text(
            json.dumps({"capture":target.name,"inventory_sha256":digest(target.read_bytes()),
                        "group":group},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"current-publication-reuse-candidates.json").write_text(
        json.dumps({"capture":target.name,"records":all_bib,
            "standing":"Saved-record identity candidates only; preserve exact source versions. In particular KLM1990 and cs/0202021v1 are distinct. Root decides aliases."},
            ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"current-candidate-datasets.json").write_text(
        json.dumps({"capture":target.name,"datasets":candidate_exports},
            ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    summary = {"inventory":target.name,"inventory_sha256":digest(target.read_bytes()),
        "utc":finished.isoformat(),"baseline_sha256":payload["baseline_sha256"],
        "canonical_symbols":len(canonical_rows),"canonical_bibliography":len(canonical_bib),
        "groups":[{"stem":g["stem"],"manifest_status":g["manifest_integration_status"],
            "raw_symbols":g["raw_symbol_records"],"raw_bibliography":g["raw_bibliography_records"],
            "missing_source_files":[x["path"] for x in g["source_regions"] if not x["exists"]],
            "actually_routed_source_files":[x["path"] for x in g["source_regions"] if x["literal_actual_route_at_index_capture"]],
            "already_merged_root_excluded":g["already_merged_root_excluded"]} for g in groups],
        "incoming_raw_symbols":sum(g["raw_symbol_records"] for g in groups if not g["already_merged_root_excluded"]),
        "incoming_bib_records":len(all_bib),"scope_candidates":len(scopes),
        "normalization_proposals":len(normalizations),
        "csv_syntax_proposals":len(syntax_proposals),
        "non_atomic":payload["non_atomic"],"changed_during_capture":changed,
        "standing":payload["standing"]}
    (OUT/"current-inventory-summary.json").write_text(
        json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    grounded.save("csv-syntax-proposals",syntax_proposals)
    # Root asked for transformed datasets, never edits to original author intakes.
    # Previously emitted original-target quote patches remain historical only.
    (OUT/"original-target-quote-patch-standing.json").write_text(json.dumps({
        "standing":"Superseded historical proposals, DO NOT APPLY to original intakes. Root requested immutable raw bytes and a quote-only transformed CSV for proposal/merge datasets.",
        "files":[p.name for p in sorted(OUT.glob("batch7-proposal-csv-quotes-*.patch"))],
        "current_csv_syntax_proposals":"batch7-proposal-csv-syntax-proposals.json",
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False))

if __name__=="__main__":
    main()
