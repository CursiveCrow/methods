"""Map current declared mathematical reader interfaces to exact LaTeX targets.

An interface reference is a reading prerequisite, not automatically a premise
of a proof. This distinction prevents a chapter comparison from becoming a
false circular proof-dependency claim.
"""
from pathlib import Path
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"
sys.path.insert(0,str(ROOT / "tools"))
import check as grammar
import build_named_theorem_index as route

units = [json.loads(s) for s in (DEST / "current-reasoning-units.jsonl").read_text(encoding="utf-8").splitlines()]
surfaces = [json.loads(s) for s in (DEST / "new-domain-destination-evidence.jsonl").read_text(encoding="utf-8").splitlines()]
label_units = {}
for u in units:
    for c in u["required_components"]:
        label_units.setdefault(c["body_label"],[]).append({"unit_id":u["unit_id"],"component_id":c["component_id"]})

targets = {}
for path in route.reachable_files():
    raw = path.read_text(encoding="utf-8-sig")
    text = grammar.strip_verbatims(grammar.strip_comments(raw))
    rel = path.relative_to(ROOT).as_posix()
    declarations = []
    for m in re.finditer(r"\\label\{((?:def|thm):[^{}]+)\}",text):
        declarations.append((m.group(1),m.start(),"explicit_label"))
    for m in grammar.HB_ENV_RE.finditer(text):
        args,_ = grammar.scan_braced_args(text,m.end(),1)
        if args and args[0].startswith(("def:","thm:")):
            declarations.append((args[0],m.start(),"named_entry_argument"))
    for label,offset,kind in declarations:
        targets.setdefault(label,[]).append({"path":rel,"line":text.count("\n",0,offset)+1,
            "declaration_kind":kind,"file_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            "catalog_components":label_units.get(label,[])})

records = []
for unit in units:
    uid = unit["unit_id"]
    own_labels = {c["body_label"] for c in unit["required_components"]}
    owned_paths = [unit["destination"]["body"]["path"]]
    ann = unit["destination"]["annex"]
    if ann["exists"]:
        owned_paths.append(ann["path"])
    for rel in owned_paths:
        text = grammar.strip_verbatims(grammar.strip_comments((ROOT / rel).read_text(encoding="utf-8-sig")))
        for m in re.finditer(r"\\(?:c|C|eq)?ref\{([^{}]+)\}",text):
            for label in (s.strip() for s in m.group(1).split(",")):
                if not label.startswith(("def:","thm:")):
                    continue
                destinations = targets.get(label,[])
                records.append({"from_unit_id":uid,"from_path":rel,"line":text.count("\n",0,m.start())+1,
                    "target_label":label,"scope":"internal_component" if label in own_labels else "external_reader_interface",
                    "reference_context":text[max(0,m.start()-260):m.end()+260],
                    "destinations":destinations,"mapping_state":"resolved" if len(destinations)==1 else "unresolved",
                    "relation":"Declared mathematical interface needed to follow this treatment; its specific proof-premise versus comparison role is retained in the context and is not asserted from a reference alone."})

path = DEST / "reader-interface-crosswalk.jsonl"
if path.exists():
    raise SystemExit("Preserve the previous reader-interface projection")
path.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in records),encoding="utf-8")
unresolved = [r for r in records if r["mapping_state"] == "unresolved"]
receipt = {"purpose":"Exact source-interface mapping; not a proof dependency or validity review",
    "path":path.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
    "units":len(units),"reference_occurrences":len(records),
    "external_reader_interface_occurrences":sum(r["scope"]=="external_reader_interface" for r in records),
    "unresolved_reference_occurrences":len(unresolved),
    "unresolved_targets":sorted(set(r["target_label"] for r in unresolved)),
    "static_input_graph_only":True,"proof_dependency_graph_accepted":False}
(DEST / "reader-interface-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
