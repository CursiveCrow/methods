"""Current remaining B7/B8 preparation only. No applying/check/review."""
from __future__ import annotations
import copy,csv,hashlib,importlib.util,io,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[2];BASE=ROOT/"handbook"
spec=importlib.util.spec_from_file_location("remaining_inventory_helpers",OUT/"inventory_batch7.py")
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
registry=lib.registry;grounded=lib.grounded;FIELDS=registry.HEADER
B7={"p06-iterations","p08-klm-preferential","p09-recombination-models"}
B8={"p15-identification","p10-operational-adequacy","p06-proper-iteration",
    "p18-erotetic-search","p09-recombination-iteration","p04-computable-analysis",
    "p06-properness-parameters"}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return p.read_text(encoding="utf-8-sig")
def save(name,data):
    (OUT/("remaining-"+name+".json")).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def public(r):return {k:v for k,v in r.items() if not k.startswith("_")}
def unwrap(g):
    return g[2:-2] if g.startswith(r"\(") and g.endswith(r"\)") else g
def split_top(g):
    parts=[];start=0;depth=0
    for n,c in enumerate(g):
        if c in "({[":depth+=1
        elif c in ")}]":depth-=1
        elif c=="," and depth==0:parts.append(g[start:n].strip());start=n+1
    parts.append(g[start:].strip())
    return parts

def actual_row(row,group,rel,n):
    row=copy.deepcopy(row);reasons=[];inactive=None;members=[]
    stem=group["stem"];g=unwrap(row["glyph"])
    if stem=="p09-recombination-models" and rel.endswith("symbols-intake-p09-recombination-models.csv"):
        forms={2:"V",3:r"\#",4:r"\$",5:"u_i",6:r"\sigma",7:r"\vdash_r",
               9:"A/B",10:r"B\backslash A",11:r"\sigma^*",12:"V_B",
               14:"M",15:"G",16:"E",17:r"\omega",18:"P",19:"h",
               20:r"\pi",22:r"\sigma_{\min}"}
        if n==8:inactive="Raw epsilon is superseded by the actual root-restored lambda native supplement; source notation is not normalized to epsilon."
        if n in forms:g=forms[n];reasons.append("Actual displayed reader TeX form, not the raw ASCII alias.")
        if n==13:
            g="P,H,L,U";row["role"]="turtle position and orthonormal-frame symbol family"
            members=[("P","turtle position vector"),("H","orthonormal heading vector"),
                     ("L","orthonormal left vector"),("U","orthonormal up vector")]
        if n==21:
            g="N_k,p_k";row["role"]="apex-count and conditional-branching symbol family"
            members=[("N_k","current apex count"),("p_k","conditional binary branching probability")]
    if stem=="p09-recombination-iteration":
        if n==13:inactive="The four O_r/C_r/Q_r/D_r ASCII aliases are no longer active in root-restored body/annex; retain raw evidence and the four actual native bracket records."
        if g=="$":g=r"\$"
        if n==27:
            g="L_k,W_1,W_2,W";row["role"]="radius-witness and wrapper-language symbol family"
            members=[(x,row["role"]+" member "+x) for x in split_top(g)]
    if stem=="p18-erotetic-search" and rel.endswith("symbols-intake-p18-erotetic-search.csv"):
        if n==7:inactive="Editorial binary-question B(A,B) alias is superseded by the native ?pm|A,B| supplement after root restored the source expression."
        spaced={3:r"e,\varphi_k",4:"Q,X",11:"Z,Y",13:"x_1,x_2,x_3"}
        if n in spaced:
            g=spaced[n];row["role"]+=" symbol family"
            members=[(x,row["role"]+" member "+x) for x in split_top(g)]
        if n==5:row["_reuse_candidate"]="Existing generalized dQ declaration from implication packet; actual search explicitly imports def:p18-ei-setting. Keep declaration-local scope unchanged; expose new usage, do not blindly reuse old finite PMCE."
    if stem=="p10-operational-adequacy" and n==29:
        inactive="Byte-identical repeated successor record after the preceding record; preserve raw duplicate evidence without appending a second identical glyph-role."
    parts=split_top(g)
    if not members and len(parts)>1:
        row["role"]+=" symbol family"
        members=[(x,row["role"]+" member "+x) for x in parts]
        reasons.append("Explicit displayed family; member types and common actual first-use exposed, not one atomic glyph.")
    if g.startswith(r"\("):g=unwrap(g)
    row["glyph"]=r"\("+g+r"\)"
    row["macro"]=g
    if not registry.PREC_RE.fullmatch(row["precedence"]):
        old=row["precedence"];row["precedence"]="n/a"
        row["notes"]+=" Original precedence descriptor "+repr(old)+" retained; no rank inferred."
    if reasons:row["notes"]+=" "+" ".join(reasons)
    if members:
        row["notes"]+=" Family listing, not one atomic glyph."
        row["_members"]=[{"glyph":r"\("+x+r"\)","macro":x,"role":role,"first_use":row["first_use"]} for x,role in members]
    return row,reasons,inactive

def main():
    started=datetime.now(timezone.utc);inputs={};groups=[];retained=[]
    baseline=OUT/"post-actual-five-numeric-baseline.json"
    frozen=json.loads(read(baseline))
    def capture(p):
        key=p.relative_to(ROOT).as_posix();data=p.read_bytes()
        inputs[key]={"sha256":hashlib.sha256(data).hexdigest(),"text":data.decode("utf-8-sig")}
        if key.startswith(("handbook/registry/symbols-intake-","handbook/bib/intake-")):
            target=OUT/("remaining-raw-"+p.name+"-"+inputs[key]["sha256"]+p.suffix)
            if target.exists() and target.read_bytes()!=data:raise RuntimeError("Immutable raw conflict")
            if not target.exists():target.write_bytes(data)
        return inputs[key]["text"]
    for number,chosen in ((7,B7),(8,B8)):
        p=ROOT/("spec/research/edition-2026-authoring-batch-intake-"+str(number)+".json")
        manifest=json.loads(capture(p))
        for group in manifest["groups"]:
            if group["stem"] in chosen:
                group=copy.deepcopy(group);group["_batch"]=number;groups.append(group)
            else:retained.append({"batch":number,"stem":group["stem"],"status":group["integration_status"],
                                 "standing":"Retained outside this explicit remaining-stage subset; no prior stage replay or new route credit."})
    native="registry/symbols-intake-p09-recombination-native.csv"
    for group in groups:
        if group["stem"]=="p09-recombination-models" and native not in group["symbol_intakes"]:
            group["symbol_intakes"].append(native)
    for p in [BASE/"registry/symbols.csv",BASE/"registry/symbol-scopes.json",BASE/"bib/handbook.bib",BASE/"main.tex",BASE/"handbook.sty"]:
        capture(p)
    for p in sorted((BASE/"parts").glob("p[0-9][0-9].tex"))+sorted((BASE/"annex").glob("p[0-9][0-9].tex")):capture(p)
    old_rows=list(csv.DictReader(io.StringIO(inputs["handbook/registry/symbols.csv"]["text"])))
    old_scopes=json.loads(inputs["handbook/registry/symbol-scopes.json"]["text"])
    old_bib=grounded.bib_records(inputs["handbook/bib/handbook.bib"]["text"])
    index=registry.ReaderIndex(BASE);rows=[];scopes={};guard=[];inactive=[];bib=[];source_records=[];raw_count=0
    all_annexes={p for g in groups for p in g["annexes"]}
    body_group={p:g["stem"] for g in groups for p in g["bodies"]}
    def regions(first,group):
        d=index.unique(first)
        if d.path not in group["bodies"]+group["annexes"]+group.get("rule_sheets",[]):
            raise registry.RegistryError("First-use outside actual selected source group")
        if d.path.startswith("annex/"):return [{"anchor":d.label}]+([{"anchor":d.owner}] if d.owner else [])
        if d.path.startswith("registry/"):return [{"file":d.path}]
        hs=[h for h in index.heading_records if h.path==d.path and h.start<=d.start<h.end]
        h=max(hs,key=lambda x:x.start) if hs else None
        selectors=[{"heading_of":first,"level":h.kind}] if h else [{"anchor":first}]
        region=index.region(selectors[0])
        for sites in index.labels.values():
            for a in sites:
                if a.kind=="annexitem" and a.owner and a.path in all_annexes:
                    try:owner=index.unique(a.owner)
                    except registry.RegistryError:
                        continue
                    if region.start<=owner.start<region.end:selectors.append({"anchor":a.label})
        return selectors
    for group in groups:
        if group["integration_status"]!="routed-awaiting-canonical-merge":
            guard.append({"group":group["stem"],"reason":"Not confirmed actual incoming route"})
        for rel in group["bodies"]+group["annexes"]+group.get("rule_sheets",[]):
            p=BASE/rel;capture(p)
            if rel not in index.files:guard.append({"group":group["stem"],"path":rel,"reason":"Not literally reached"})
            source_records.append({"group":group["stem"],"path":rel,"sha256":sha(p),"literal_route":rel in index.files})
        if group.get("note"):capture(ROOT/group["note"])
        for rel in group.get("symbol_intakes",[]):
            text=capture(BASE/rel);fixed=[]
            for line in text.splitlines(keepends=True):
                m=re.match(r"^(\\\(.*?\\\)),",line)
                if m and "," in m[1]:line='"'+m[1].replace('"','""')+'",'+line[m.end():]
                fixed.append(line)
            reader=csv.DictReader(io.StringIO("".join(fixed)))
            for number,raw in enumerate(reader,2):
                raw_count+=1
                if None in raw:guard.append({"group":group["stem"],"intake":rel,"row":number,"reason":"Unrepaired CSV overflow"});continue
                original={k:(raw.get(k) or "").strip() for k in FIELDS}
                row,reasons,disposition=actual_row(original,group,rel,number)
                row.update(_group=group["stem"],_intake=rel,_line=number,_original=original)
                if disposition:inactive.append({"group":group["stem"],"intake":rel,"row":number,"original":original,"reason":disposition});continue
                try:selectors=regions(row["first_use"],group)
                except registry.RegistryError as exc:guard.append({"group":group["stem"],"row":number,"reason":str(exc)});selectors=[]
                if row["scope"] not in old_scopes["scopes"] and not registry.parse_scope(row["scope"]):
                    binding=scopes.setdefault(row["scope"],{"presentation":"Actual remaining B7/B8 "+group["stem"]+" source-labelled declarations and physical reciprocal proof regions; typed source roles, no source/proof acceptance.","regions":[]})
                    for selector in selectors:
                        if selector not in binding["regions"]:binding["regions"].append(selector)
                rows.append(row)
        for rel in group.get("bibliography_intakes",[]):
            for record in grounded.bib_records(capture(BASE/rel)):
                bib.append({"group":group["stem"],"intake":rel,"record":record,"fields":grounded.fields(record),
                            "reuse_candidates":lib.publication_candidates(record,old_bib)})
    cross=[]
    for sites in index.labels.values():
        for a in sites:
            if a.kind=="annexitem" and a.path in all_annexes and a.owner:
                try:owner=index.unique(a.owner)
                except registry.RegistryError as exc:
                    guard.append({"annex_label":a.label,"annex_path":a.path,
                                  "body_owner":a.owner,"reason":str(exc),
                                  "actual_sites":[{"path":d.path,"line":d.line} for d in index.labels.get(a.owner,[])]})
                    continue
                annex_group=next(g["stem"] for g in groups if a.path in g["annexes"])
                if owner.path not in next(g["bodies"] for g in groups if g["stem"]==annex_group):
                    cross.append({"annex_label":a.label,"annex_path":a.path,"annex_group":annex_group,
                                  "body_label":owner.label,"body_path":owner.path,"body_group":body_group.get(owner.path),
                                  "standing":"One physical cross-group pair; no full-body duplication or double proof-count credit."})
    combined=copy.deepcopy(old_scopes);combined["scopes"].update(scopes)
    resolver=registry.Resolver(BASE,bindings=combined,index=index)
    resolver.source_keys.update(item["record"]["key"] for item in bib)
    decoded=[];incoming=[]
    for n,r in enumerate(old_rows,2):
        try:decoded.append(dict(r,_line=n,_scope=resolver.resolve(r["scope"])))
        except registry.RegistryError as exc:guard.append({"canonical_line":n,"reason":str(exc)})
    for row in rows:
        try:
            row["_scope"]=resolver.resolve(row["scope"])
            if not resolver.contains(row["_scope"],row["first_use"]):guard.append({"group":row["_group"],"row":row["_line"],"reason":"first_use outside proposed extent"})
            if row.get("_members"):
                for m in row["_members"]:incoming.append(dict(row,**m,_family_parent=row["glyph"]))
            else:incoming.append(row)
        except registry.RegistryError as exc:guard.append({"group":row["_group"],"row":row["_line"],"reason":str(exc)})
    overlaps=[];buckets={}
    for row in decoded+incoming:buckets.setdefault(re.sub(r"\s+","",row["glyph"]),[]).append(row)
    for entries in buckets.values():
        for n,a in enumerate(entries):
            for b in entries[n+1:]:
                if not(a.get("_group") or b.get("_group")):continue
                if resolver.overlaps(a["_scope"],b["_scope"]):
                    overlaps.append({"a":public(a),"b":public(b),"a_group":a.get("_group","canonical"),"b_group":b.get("_group","canonical"),
                                     "standing":"Exact source-region/type decision needed; no checker invoked or glyph avoidance."})
    changed=[p for p,v in inputs.items() if sha(ROOT/p)!=v["sha256"]]
    result={"utc":datetime.now(timezone.utc).isoformat(),"started_utc":started.isoformat(),
        "baseline":"post-actual-five-numeric-baseline.json","baseline_sha256":sha(baseline),
        "baseline_symbols":frozen["canonical_row_count"],"baseline_bib":frozen["canonical_bib_count"],
        "canonical_current_symbols":len(old_rows),"canonical_current_bib":len(old_bib),
        "groups":groups,"retained_other_groups":retained,"raw_symbol_records":raw_count,
        "candidate_symbol_rows":[public(r) for r in rows],"family_member_records":[{"parent":r["glyph"],"group":r["_group"],"members":r["_members"]} for r in rows if r.get("_members")],
        "inactive_raw_records":inactive,"append_scope_prototypes":scopes,"bibliography_candidates":bib,
        "cross_group_pairs":cross,"source_regions":source_records,"input_hashes":{p:v["sha256"] for p,v in inputs.items()},
        "preparation_guards":guard,"exact_overlap_decisions":overlaps,"changed_during_capture":changed,
        "standing":"Preparation data only; applied R2/old11/B6 pending2 never replayed. No canonical/manuscript/driver/source/ledger write or strict/collision checker, independent review, build or render. Root decides exact reuse/types before any patch packet.",
        "scope":{"parts":19,"planned_chapters":289,"main_sections":2475,"original_requirements":615}}
    save("stage",result);save("decisions",overlaps);save("bibliography",bib);save("rows",[public(r) for r in rows]);save("cross-group-pairs",cross)
    print(json.dumps({"utc":result["utc"],"groups":len(groups),"raw_symbols":raw_count,"candidates":len(rows),"inactive":len(inactive),
                      "bib_records":len(bib),"scopes":len(scopes),"overlap_decisions":len(overlaps),"guards":len(guard),"cross_pairs":len(cross),"changed":changed}))
if __name__=="__main__":main()
