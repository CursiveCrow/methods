"""Inventory current inherited content and its source correspondence; no book edits."""
from __future__ import annotations

import collections
import csv
import difflib
import hashlib
import json
from pathlib import Path
import re

ROOT = Path("C:/Dev/the-methods-of-reason")
OUT = ROOT / "spec/inventory/2026-09-06"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def table(name, rows):
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in row.items()})


latex = load_csv(OUT / "latex-files.csv")
active = {r["path"] for r in latex if r["active"] == "True"}
source_path = ROOT / "source/formal-logic-reference.tex"
source_bytes = source_path.read_bytes()
source_raw_lines = source_bytes.decode("utf-8").splitlines(keepends=True)
source_lines = source_bytes.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
records = {}
for path in sorted((ROOT / "spec/provenance").glob("*.json")):
    if not re.fullmatch(r"(?:SRC|PRE|SEP|CTL)-\d{5}-\d{5}\.json", path.name):
        continue
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    art = data.get("restoration_artifact", {}).get("path")
    if art:
        records[art] = {"record_path": path.relative_to(ROOT).as_posix(), "data": data}

fragments, contents, diff_sections = [], {}, []
for path in sorted((ROOT / "handbook/restoration").glob("inherited-*.tex")):
    match = re.fullmatch(r"inherited-(\d{5})-(\d{5})\.tex", path.name)
    if not match:
        continue
    start, end = map(int, match.groups())
    relative = path.relative_to(ROOT).as_posix()
    current_bytes = path.read_bytes()
    current = current_bytes.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    original = source_lines[start - 1:end]
    exact = original == current
    record = records.get(relative, {})
    data = record.get("data", {})
    is_active = relative in active
    status = "active_unchanged_source" if is_active and exact else "active_changed_reader_text" if is_active else "inactive_source_artifact"
    opcodes = difflib.SequenceMatcher(a=original, b=current, autojunk=False).get_opcodes()
    row = {
        "file": relative, "source_start": start, "source_end": end,
        "source_lines": len(original), "current_lines": len(current), "active": is_active,
        "inventory_state": status, "source_text_equal_after_eol_normalization": exact,
        "source_interval_normalized_sha256": digest("".join(original).encode()),
        "current_normalized_sha256": digest("".join(current).encode()), "current_file_sha256": digest(current_bytes),
        "record_path": record.get("record_path", ""),
        "record_artifact_hash_matches_current": data.get("restoration_artifact", {}).get("sha256") == digest(current_bytes) if record else None,
        "record_destination_status": data.get("handbook_destination", {}).get("status", ""),
        "record_destination_reason": data.get("handbook_destination", {}).get("reason", ""),
        "record_completeness": data.get("completeness", {}), "record_verification": data.get("verification", {}),
        "changed_ranges": [{"kind": tag, "source_start": start+i1, "source_end": start+i2-1,
                            "current_start": j1+1, "current_end": j2}
                           for tag, i1, i2, j1, j2 in opcodes if tag != "equal"]
    }
    fragments.append(row)
    contents[relative] = {"original": original, "current": current, "opcodes": opcodes, "row": row}
    if not exact:
        diff_sections += ["## " + relative, "", f"Active: {is_active}. Source lines {start}–{end}. Current file SHA-256: `{row['current_file_sha256']}`.", "",
                          "```diff", "".join(difflib.unified_diff(original, current,
                          fromfile=f"source/formal-logic-reference.tex:{start}-{end}", tofile=relative)).rstrip(), "```", ""]

crosswalk = {int(r["unit_ordinal"]): r for r in load_csv(ROOT / "spec/source-unit-audit-crosswalk.csv")}
units = []
for unit in load_csv(ROOT / "spec/source-unit-inventory.csv"):
    start, end, ordinal = int(unit["start_line"]), int(unit["end_line"]), int(unit["ordinal"])
    covering = [r for r in fragments if r["source_start"] <= start and r["source_end"] >= end]
    cw = crosswalk.get(ordinal, {})
    current_mappings = []
    for fragment in covering:
        body = contents[fragment["file"]]
        a, b = start-fragment["source_start"], end-fragment["source_start"]+1
        overlaps = [(tag,i1,i2,j1,j2) for tag,i1,i2,j1,j2 in body["opcodes"]
                    if max(a, i1) < min(b, i2) or (tag == "insert" and a <= i1 < b)]
        changed = any(tag != "equal" for tag,*_ in overlaps)
        exact_spans = [{"source_start": fragment["source_start"]+max(a,i1),
                        "source_end": fragment["source_start"]+min(b,i2)-1,
                        "current_start": j1+max(a,i1)-i1+1,
                        "current_end": j1+min(b,i2)-i1}
                       for tag,i1,i2,j1,j2 in overlaps if tag == "equal"]
        current_mappings.append({"file": fragment["file"], "active": fragment["active"],
                                 "source_unit_text_unchanged": not changed, "exact_spans": exact_spans,
                                 "changed_fragment_ranges": [r for r in fragment["changed_ranges"]
                                                             if max(start,r["source_start"]) <= min(end,r["source_end"])],
                                 "record_artifact_hash_matches_current": fragment["record_artifact_hash_matches_current"]})
    active_maps = [m for m in current_mappings if m["active"]]
    state = "active_unchanged_source_unit" if active_maps and all(m["source_unit_text_unchanged"] for m in active_maps) else "active_changed_unit_needs_content_disposition" if active_maps else "no_active_exact_fragment_route"
    units.append({"ordinal": ordinal, "kind": unit["kind"], "title": unit["title"], "label": unit["label"],
                  "source_start": start, "source_end": end, "inventory_state": state,
                  "source_unit_hash_matches_inventory": digest("".join(source_raw_lines[start-1:end]).encode()) == unit["sha256"],
                  "current_mappings": current_mappings, "historical_destination": cw.get("handbook_destination", ""),
                  "historical_admission": cw.get("provenance_disposition", ""),
                  "historical_audit_result": cw.get("audit_result", ""),
                  "remaining_inventory": "Inspect changed unit and current correction provenance." if state == "active_changed_unit_needs_content_disposition" else
                                         "Inspect alternate current representation, layout disposition, or missing source content." if state == "no_active_exact_fragment_route" else
                                         "Physical content correspondence established; mathematical/source correctness and publication evidence retain their separately recorded standing."})

summary = {"source_file_sha256": digest(source_bytes), "source_line_count": len(source_lines),
           "fragment_count": len(fragments), "fragment_states": dict(collections.Counter(r["inventory_state"] for r in fragments)),
           "fragment_record_bindings": dict(collections.Counter(str(r["record_artifact_hash_matches_current"]) for r in fragments)),
           "unit_count": len(units), "unit_states": dict(collections.Counter(r["inventory_state"] for r in units)),
           "source_unit_hash_comparisons": dict(collections.Counter(str(r["source_unit_hash_matches_inventory"]) for r in units)),
           "changed_active_fragments": [r["file"] for r in fragments if r["inventory_state"] == "active_changed_reader_text"],
           "inactive_fragments": [r["file"] for r in fragments if not r["active"]],
           "unresolved_unit_ordinals": [r["ordinal"] for r in units if r["inventory_state"] != "active_unchanged_source_unit"],
           "limits": "Exact normalized-byte correspondence is content-presence evidence, not semantic reading or proof correctness. Changed text can be an authorized correction; it is not automatically an error. Unrouted fragments can have alternate permitted representations requiring inspection."}
dump("inherited-current-fragments.json", fragments)
dump("inherited-current-units.json", units)
dump("inherited-current-summary.json", summary)
table("inherited-current-fragments.csv", fragments)
table("inherited-current-units.csv", units)
(OUT / "inherited-current-differences.md").write_text("# Current inherited-source differences\n\nThis report records actual text differences, without altering or condemning them. Current correction policy must be applied by reading the changed passages and provenance.\n\n" + "\n".join(diff_sections), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))

# The inherited feedback uses paragraph-level solutions, not solution environments.
feedback_path = ROOT / "handbook/restoration/inherited-15638-16742.tex"
feedback = feedback_path.read_text(encoding="utf-8")
label_data = json.loads((OUT / "reference-candidates.json").read_text(encoding="utf-8"))["label_definitions"]
labels = collections.defaultdict(list)
for label in label_data:
    labels[label["label"]].append(label)
starts = list(re.finditer(r"\\paragraph\{\\hyperref\[([^\]]+)\]", feedback))
feedback_rows = []
for index, match in enumerate(starts):
    end = starts[index+1].start() if index+1 < len(starts) else len(feedback)
    body = feedback[match.start():end]
    status = re.search(r"\\textit\{(Solution(?: sketch)?\.)\}", body)
    brace = feedback.index("{", match.start())
    depth, cursor = 1, brace+1
    while cursor < len(feedback) and depth:
        if feedback[cursor] == "\\":
            cursor += 2
            continue
        if feedback[cursor] == "{":
            depth += 1
        elif feedback[cursor] == "}":
            depth -= 1
        cursor += 1
    heading = feedback[brace+1:cursor-1]
    heading_targets = re.findall(r"\\hyperref\[([^\]]+)\]", heading)
    feedback_rows.append({"target": match.group(1), "file": feedback_path.relative_to(ROOT).as_posix(),
                          "all_heading_targets": heading_targets,
                          "line_start": feedback.count("\n", 0, match.start())+1,
                          "line_end": feedback.count("\n", 0, end),
                          "declared_status": status.group(1) if status else "no_recognized_status",
                          "target_locations_on_active_route": labels[match.group(1)],
                          "all_heading_target_locations": {target: labels[target] for target in heading_targets},
                          "target_on_active_route": all(bool(labels[target]) for target in heading_targets)})
all_targets = {target for row in feedback_rows for target in row["all_heading_targets"]}
feedback_summary = {"feedback_units": len(feedback_rows), "unique_target_labels": len(all_targets),
                    "unique_exercise_targets": sum(t.startswith("ex:") for t in all_targets),
                    "unique_problem_targets": sum(t.startswith("prob:") for t in all_targets),
                    "declared_statuses": dict(collections.Counter(r["declared_status"] for r in feedback_rows)),
                    "unresolved_targets": sorted(t for t in all_targets if not labels[t]),
                    "file_sha256": digest(feedback_path.read_bytes()),
                    "source_correspondence": next(r["source_text_equal_after_eol_normalization"] for r in fragments if r["file"] == feedback_path.relative_to(ROOT).as_posix()),
                    "method": "Every feedback paragraph heading, declared solution status and active literal target is inventoried. Declared Solution is not a new correctness verdict; complete source text corresponds exactly to the frozen authority."}
dump("exercise-feedback-current-inventory.json", {"summary": feedback_summary, "units": feedback_rows})
table("exercise-feedback-current-inventory.csv", feedback_rows)
print(json.dumps(feedback_summary, ensure_ascii=False, indent=2))
