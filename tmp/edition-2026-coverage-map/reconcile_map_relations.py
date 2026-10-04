"""Allocate active map interfaces and record exact shared-source/destination relations.

This is a construction projection. It does not review proofs, infer source
identity from a topic title, or transfer completed-writing credit.
"""
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/"spec/coverage/edition-2026"
sys.path.insert(0,str(ROOT/"tools"))
import check as grammar
import build_named_theorem_index as route

def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8-sig"))
def rows(path):
    return [json.loads(s) for s in (ROOT/path).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
def digest(path):
    p=ROOT/path
    return {"path":str(path),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
def write_rows(name,data):
    p=DEST/name
    p.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in data),encoding="utf-8")
    return {**digest(p.relative_to(ROOT)),"rows":len(data)}

master=load("spec/edition-2026-coverage-map.json")
units={}
input_pins=[]
for f in master["unit_shards"]:
    actual=digest(f["path"])
    if actual["sha256"].lower()!=f["sha256"].lower():
        raise SystemExit("Refresh master after active shard publication: "+f["path"])
    input_pins.append(actual)
    for u in rows(f["path"]):
        if u["unit_id"] in units:
            raise SystemExit("Duplicate unit "+u["unit_id"])
        units[u["unit_id"]]=u
for f in master.get("applied_unit_field_overlays",[]):
    actual=digest(f["path"])
    if actual["sha256"].lower()!=f["sha256"].lower():
        raise SystemExit("Changed prerequisite overlay "+f["path"])
    input_pins.append(actual)
    for overlay in rows(f["path"]):
        units[overlay["unit_id"]].update({k:v for k,v in overlay.items() if k in ["prerequisites","internal_setup","ambient_hypothesis_policy","external_premise_policy"]})

requirements={r["original_requirement_id"]:r["unit_ids"] for r in rows("spec/coverage/edition-2026/requirements-crosswalk.jsonl")}
domains={r["assignment_id"]:r["all_selected_unit_ids"] for r in rows("spec/coverage/edition-2026/new-domain-crosswalk-v3.jsonl")}
families={r["family_id"]:r["selected_unit_ids"] for r in rows("spec/coverage/edition-2026/mandatory-family-crosswalk-v2.jsonl")}
groups={**requirements,**domains,**families}
benchmarks=rows("spec/coverage/edition-2026/benchmark-crosswalk-v2.jsonl")
benchmark_domains=defaultdict(set)
for row in benchmarks:
    for uid in row.get("unit_ids",[]):
        for field in ["assignment_or_family","assignments","domains","selected_domain_ids"]:
            value=row.get(field,[])
            if isinstance(value,str):
                value=value.split(";")
            if isinstance(value,list):
                benchmark_domains[uid].update(x for x in value if isinstance(x,str))

# The literal TSV is the explicit editorial assignment authority for benchmark
# prerequisites; the crosswalk contains additional relation details.
import csv
with (DEST/"benchmark-contents-decisions.tsv").open(encoding="utf-8",newline="") as stream:
    for r in csv.DictReader(stream,delimiter="\t"):
        uid="ED26-BM-"+r["benchmark"]+"-"+r["row"].replace(".","-")
        if uid in units:
            benchmark_domains[uid].update(r["assignment_or_family"].split(";"))

bibtext=(ROOT/"handbook/bib/handbook.bib").read_text(encoding="utf-8-sig")
bib={}
for match in re.finditer(r"@[A-Za-z]+\s*\{",bibtext):
    args,end=grammar.scan_braced_args(bibtext,match.end()-1,1)
    if args and "," in args[0]:
        key=args[0].split(",",1)[0].strip()
        record=bibtext[match.start():end]
        doi=re.search(r"\bdoi\s*=\s*\{([^{}]+)\}",record,re.I)
        bib[key]={"key":key,"path":"handbook/bib/handbook.bib","line":bibtext.count("\n",0,match.start())+1,
            "doi":doi.group(1).lower() if doi else None,"literal_record":record}

def explicit_bib_keys(obj):
    found=set()
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in ["source_id","citation_key","source_key","key","bibkey","citation"] and isinstance(v,str) and v in bib:
                found.add(v)
            elif k in ["citation_keys","source_keys","selected_source_keys"] and isinstance(v,list):
                found.update(x for x in v if x in bib)
            elif k=="literal_record" and isinstance(v,str):
                m=re.match(r"@[A-Za-z]+\s*\{\s*([^,]+),",v)
                if m and m.group(1).strip() in bib:
                    found.add(m.group(1).strip())
            if isinstance(v,(dict,list)):
                found.update(explicit_bib_keys(v))
    elif isinstance(obj,list):
        for v in obj:
            found.update(explicit_bib_keys(v))
    return found

source_key_units=defaultdict(set)
source_doi_units=defaultdict(set)
source_container_units=defaultdict(set)
source_target_units=defaultdict(set)
for uid,u in units.items():
    for key in explicit_bib_keys(u.get("source_presentations",[])):
        source_key_units[key].add(uid)
        if bib[key]["doi"]:
            source_doi_units[bib[key]["doi"]].add(uid)
    for p in u.get("source_presentations",[]):
        if not isinstance(p,dict):
            continue
        for field in ["doi","chapter_doi"]:
            value=p.get(field)
            if isinstance(value,str):
                value=re.sub(r"^https?://(?:dx\.)?doi\.org/","",value,flags=re.I).strip().lower()
                source_doi_units[value].add(uid)
        sid=p.get("source_id")
        if isinstance(sid,str) and re.fullmatch(r"SRC-\d{3}",sid):
            source_container_units[sid].add(uid)
        if all(isinstance(p.get(k),str) and p[k] for k in ["title","version","url"]):
            source_target_units[json.dumps({k:p[k] for k in ["title","version","url"]},ensure_ascii=False,sort_keys=True)].add(uid)

labels=defaultdict(list)
path_units=defaultdict(set)
label_units=defaultdict(set)
def walk_destinations(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if isinstance(v,str):
                if k in ["path","proposed_path","body_path","proposed_source_presentation","proposed_source_proof_destination","completion_body","completion_annex"] and v.endswith(".tex"):
                    yield ("path",v)
                elif k in ["label","proposed_label","entry_label","completion_label"] and ":" in v:
                    yield ("label",v)
            elif isinstance(v,(dict,list)):
                yield from walk_destinations(v)
    elif isinstance(obj,list):
        for v in obj:
            yield from walk_destinations(v)
for uid,u in units.items():
    for kind,value in walk_destinations(u.get("destination",{})):
        (path_units if kind=="path" else label_units)[value].add(uid)
    for c in u.get("required_components",[]):
        if isinstance(c,dict) and isinstance(c.get("body_label"),str):
            label_units[c["body_label"]].add(uid)

reader_paths=set(route.reachable_files())
for path in list(reader_paths):
    text=grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding="utf-8-sig")))
    for m in re.finditer(r"\\showcalculus\s*\{([A-Za-z0-9_-]+)\}",text):
        target=ROOT/"handbook/registry/calculi"/(m.group(1)+".tex")
        if target.is_file():
            reader_paths.add(target)
for path in sorted(reader_paths):
    text=grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding="utf-8-sig")))
    rel=path.relative_to(ROOT).as_posix()
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    occurrences=[]
    for m in re.finditer(r"\\label\s*\{([^{}]+)\}",text):
        occurrences.append((m.group(1),m.start(),"explicit_label"))
    for m in grammar.HB_ENV_RE.finditer(text):
        args,_=grammar.scan_braced_args(text,m.end(),1)
        if args:
            occurrences.append((args[0],m.start(),"named_entry"))
    for m in re.finditer(r"\\(?:calculussheet|hbrule)\s*\{([^{}]+)\}",text):
        occurrences.append((m.group(1),m.start(),"registry_macro"))
    for label,offset,kind in occurrences:
        labels[label].append({"path":rel,"line":text.count("\n",0,offset)+1,"kind":kind,"sha256":sha})

unit_label_re=re.compile(r"\b(?:def|thm|lem|lemma|cor|prop|sec|ch|sheet|annex|tab|fig):[A-Za-z0-9_.:-]+")
requirement_re=re.compile(r"(?<![A-Za-z0-9-])(?:N-[a-z]-\d{3}|D-P\d+-\d{3}|[LRSAT]-\d{3})(?![A-Za-z0-9-])")
domain_re=re.compile(r"\bP(?:1[5-9])-[A-Z]\d+\b|\bCF-\d{2}\b")
unit_re=re.compile(r"ED26-[A-Za-z0-9_-]+")
unresolved=[]
relations=[]

for uid,u in units.items():
    items=u.get("prerequisites",[])
    if not isinstance(items,list):
        unresolved.append({"unit_id":uid,"issue":"Non-list prerequisite field","value":items})
        continue
    for ordinal,p in enumerate(items,1):
        text=p if isinstance(p,str) else p.get("named_premise",p.get("name",p.get("statement",p.get("use_scope",p.get("use",""))))) if isinstance(p,dict) else str(p)
        role=p.get("role","") if isinstance(p,dict) else ""
        record={"relation_id":f"{uid}/PRE-{ordinal:03}","from_unit_id":uid,"original_prerequisite":p,
            "description":text,"mapping_state":"resolved","target_unit_ids":[],"target_labels":[],"catalog_groups":[]}
        direct=[]
        if isinstance(p,dict):
            if isinstance(p.get("unit_id"),str): direct.append(p["unit_id"])
            if isinstance(p.get("unit_ids"),list): direct.extend(p["unit_ids"])
        direct.extend(unit_re.findall(text))
        direct=sorted(set(direct))
        bad=[v for v in direct if v not in units]
        if bad:
            record["mapping_state"]="unresolved"
            unresolved.append({"relation_id":record["relation_id"],"missing_unit_ids":bad})
        record["target_unit_ids"].extend(v for v in direct if v in units)
        for name in sorted(set(requirement_re.findall(text)+domain_re.findall(text))):
            if name not in groups:
                unresolved.append({"relation_id":record["relation_id"],"missing_catalog_group":name})
                record["mapping_state"]="unresolved"
            else:
                record["catalog_groups"].append({"group_id":name,"unit_ids":groups[name]})
        for label in sorted(set(s.rstrip(":.") for s in unit_label_re.findall(text))):
            matches=labels.get(label,[])
            if len(matches)!=1:
                unresolved.append({"relation_id":record["relation_id"],"label":label,"matches":len(matches)})
                record["mapping_state"]="unresolved"
            record["target_labels"].append({"label":label,"declarations":matches,"catalog_unit_ids":sorted(label_units.get(label,[]))})
        if isinstance(p,dict) and p.get("source_key"):
            key=p["source_key"]
            record["source_import"]={"key":key,"identity":p.get("bibliographic_identity",bib.get(key)),
                "required_extent":p.get("required_source_extent",text),
                "related_source_unit_ids":sorted(source_key_units.get(key,set())-{uid}),
                "supply_destination":u.get("destination"),
                "standing":"Exact named external source obligation retained within this treatment until its body and proof are supplied; no source-body acceptance is inferred."}
            if not record["source_import"]["identity"] or not record["source_import"]["required_extent"]:
                unresolved.append({"relation_id":record["relation_id"],"issue":"Unidentified or unbounded source import"})
                record["mapping_state"]="unresolved"
        elif text in bib:
            record["source_import"]={"key":text,"identity":bib[text],"related_source_unit_ids":sorted(source_key_units.get(text,set())-{uid}),
                "required_extent":"The source-specific construction or result expressly required by the parent unit's preserved components and original requirement.","supply_destination":u.get("destination")}
        if uid.startswith("ED26-BM-") and text.startswith("The exact existing component interfaces linked by the assigned domains"):
            assigned=sorted(benchmark_domains.get(uid,set()))
            if not assigned:
                unresolved.append({"relation_id":record["relation_id"],"issue":"Benchmark has no assigned interface group"})
                record["mapping_state"]="unresolved"
            record["catalog_groups"]=[]
            for group in assigned:
                if group in groups:
                    record["catalog_groups"].append({"group_id":group,"unit_ids":groups[group]})
                elif re.fullmatch(r"P\d+",group):
                    record["catalog_groups"].append({"group_id":group,"destination":f"handbook/parts/p{int(group[1:]):02}.tex","standing":"Reader subject destination; not a claim that the whole part is a proof prerequisite."})
                else:
                    unresolved.append({"relation_id":record["relation_id"],"unknown_benchmark_assignment":group})
                    record["mapping_state"]="unresolved"
        # Roles follow the explicitly recorded relation. Broad background
        # vocabulary is allocated locally; it is not an invented proof edge.
        if role in ["external_proof_dependency","source_correction_dependency","external_status_dependency","dated_status_evidence","source_identity_correction"]:
            disposition=role
        elif isinstance(p,dict) and p.get("authority"):
            disposition="editorial_policy_dependency"
        elif isinstance(p,dict) and p.get("input_surfaces"):
            disposition="production_input"
        elif role=="ambient_hypothesis" or text in ["Axiom of Choice","Boolean prime ideal principle","ZF","ZF versus ZFA","Woodin-cardinal hypotheses"]:
            disposition="ambient_hypothesis"
        elif role in ["editorial_scope_rule","exact_target_source"]:
            disposition=role
        elif record["target_labels"] or record["catalog_groups"] or direct:
            disposition="declared_interface"
        elif "source_import" in record:
            disposition="bounded_source_import"
        elif role=="external_definition_interface" or "actually invoked" in text or "specific earlier source results" in text:
            disposition="source_closure_obligation"
        else:
            disposition="local_content_prerequisite"
        record["role"]=disposition
        if disposition in ["local_content_prerequisite","source_closure_obligation"]:
            record["local_allocation"]={"unit_id":uid,"destination":u.get("destination"),
                "success_condition":"Supply the explicitly named setup and required results before their use in the parent treatment. A source result reused from elsewhere must have an exact completed statement/proof link with matching assumptions.",
                "failure_condition":"An undefined object, an unproved required imported result, a different source variant or circular justification is used to complete the parent treatment.",
                "extent":"Only the named prerequisite and the parent unit's explicit selected source/components; no arbitrary whole-work dependency is added.",
                "completion_state":"Required writing and source-body matching remain governed by the parent content/source state."}
        record["proof_dependency_inferred"]=False
        relations.append(record)

source_relations=[]
for kind,index in [("same_canonical_source_key",source_key_units),("same_registered_doi",source_doi_units),("same_historical_container",source_container_units),("same_explicit_source_target",source_target_units)]:
    for key,members in sorted(index.items()):
        if len(members)<2: continue
        source_relations.append({"relation":kind,"identity":key,"unit_ids":sorted(members),
            "disposition":"Retain every source extent and original requirement facet; reuse only the same completed component after exact source/version and statement/proof matching.",
            "same_presentation_inferred":False,"completed_content_credit_transferred":False,
            "evidence":"Explicit source IDs, DOI fields or canonical bibliographic keys in the pinned unit shards; no title similarity join."})
destinations=[]
for kind,index in [("path",path_units),("label",label_units)]:
    for value,members in sorted(index.items()):
        if len(members)<2: continue
        destinations.append({"kind":kind,"destination":value,"unit_ids":sorted(members),
            "relation":"Shared reader destination or overlapping requirement facets, with distinct required source components retained.",
            "authoring_rule":"Assign the destination one integrator. Credit a component once against its exact content/source identity, then link all satisfied requirement facets. Preserve separate source presentations and unsupplied components.",
            "all_facets_completed_inferred":False})

now=datetime.now(timezone.utc).isoformat()
pins=[write_rows("prerequisite-allocation-crosswalk.jsonl",relations),write_rows("source-overlap-crosswalk.jsonl",source_relations),write_rows("shared-destination-crosswalk.jsonl",destinations)]
receipt={"snapshot_utc":now,"input_unit_shards":input_pins,"active_unit_count":len(units),"prerequisite_records":len(relations),
    "prerequisite_roles":dict(Counter(r["role"] for r in relations)),"unresolved_relations":unresolved,
    "known_interface_allocation_complete":not unresolved,"outputs":pins,
    "proof_dependency_graph_accepted":False,"source_body_closure_accepted":False,
    "standing":"Construction allocation of declared interfaces, known source imports and local setup. Actual source-body proof imports and writing closure remain explicit completion work; this receipt does not certify proof truth or manuscript acceptance."}
(DEST/"relation-reconciliation-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"units":len(units),"prerequisites":len(relations),"source_relation_groups":len(source_relations),"shared_destinations":len(destinations),"unresolved_count":len(unresolved),"unresolved":unresolved[:25]},ensure_ascii=False))
