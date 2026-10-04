"""Replace broad keyword candidates with exact semantic coverage selections."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"
def read(name):
    return [json.loads(s) for s in (DEST / name).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
def write(name,rows):
    path = DEST / name
    if path.exists():
        raise SystemExit("Preserve previous refinement: " + name)
    path.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in rows),encoding="utf-8")
    return {"path":path.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"rows":len(rows)}
inherited = read("inherited-crosswalk.jsonl")
requirements = read("requirements-crosswalk.jsonl")
bench = read("benchmark-crosswalk.jsonl")

required_ids = {
 "3.1": {"D-P1-005"} | {f"D-P2-{n:03}" for n in [1,2,3,4,5,6,7,8,10,11]} | {f"D-P3-{n:03}" for n in [1,2,3,4,6,7,10,11,12,13,14]},
 "5.1": {"N-b-011","R-039"},
 "5.2": {"N-b-032","D-P10-036","A-093"},
 "6.1": {"N-b-016","N-b-017","N-b-018","D-P10-038","A-089"}}
inherited_ranges = {"3.1":(135,405),"5.1":(890,896)}
receipts = []
for row in bench:
    if row["benchmark_id"] != "RAT2021" or row["contents_row"] not in required_ids:
        continue
    number = row["contents_row"]
    selected = set()
    for r in requirements:
        if r["original_requirement_id"] in required_ids[number]:
            selected.update(r["unit_ids"])
    if number in inherited_ranges:
        lower,upper = inherited_ranges[number]
        for r in inherited:
            if lower <= int(r["inherited_ordinal"]) <= upper:
                selected.update(r["unit_ids"])
    if number == "6.1":
        selected.add("ED26-P16-CH-finite-counterfactuals")
    receipts.append({"row":number,"removed_overbroad_candidates":sorted(set(row["unit_ids"])-selected),
        "added_exact_component_units":sorted(selected-set(row["unit_ids"])),
        "exact_original_requirement_ids":sorted(required_ids[number]),
        "exact_inherited_ordinal_range":inherited_ranges.get(number)})
    row["unit_ids"] = sorted(selected)
    row["relation_selection"] = "Exact original requirement IDs and source-structural membership, replacing lexical candidates; retained units provide the named subject and explicitly related comparisons, not automatic acceptance of the benchmark chapter."
    row["exact_original_requirement_ids"] = sorted(required_ids[number])
    if number in inherited_ranges:
        row["exact_inherited_ordinal_range"] = inherited_ranges[number]
    row["evidence"].append("spec/coverage/edition-2026/benchmark-relation-refinement-receipt.json")

domains = read("new-domain-crosswalk-v2.jsonl")
old_bench = read("benchmark-crosswalk.jsonl")
for domain in domains:
    did = domain["assignment_id"]
    old_ids = {uid for b in old_bench if did in b["assigned_domains_or_families"] for uid in b["unit_ids"]}
    new_ids = {uid for b in bench if did in b["assigned_domains_or_families"] for uid in b["unit_ids"]}
    own = set(domain["unit_ids"])
    all_ids = (set(domain["all_selected_unit_ids"]) - (old_ids-new_ids)) | new_ids | own
    domain["all_selected_unit_ids"] = sorted(all_ids)
    domain["selected_additional_unit_ids"] = sorted(all_ids-own)
    domain["benchmark_crosswalk_version"] = "spec/coverage/edition-2026/benchmark-crosswalk-v2.jsonl"
outputs = [write("benchmark-crosswalk-v2.jsonl",bench),write("new-domain-crosswalk-v3.jsonl",domains)]
receipt = {"purpose":"Resolve actual mapping relations; no manuscript review or source acceptance",
    "reason":"Substring matching included irrelevant incompleteness/complexity results, epistemicism and Lewis 1979; case-insensitive AGM also matched fragments. Exact IDs and source-part membership control the refinement.",
    "outputs":outputs,"refined_rows":receipts,"all_original_obligations_preserved":True,
    "no_manuscript_content_removed":True,"global_map_complete":False}
(DEST / "benchmark-relation-refinement-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"outputs":outputs,"refined_rows":len(receipts),"removed_false_relations":sum(len(r["removed_overbroad_candidates"]) for r in receipts)},ensure_ascii=False))
