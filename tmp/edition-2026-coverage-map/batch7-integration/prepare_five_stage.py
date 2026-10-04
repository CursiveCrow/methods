"""B7 five-group canonical preparation. Writes proposals only, never targets."""
from __future__ import annotations
import copy,csv,hashlib,importlib.util,io,json,re,sys
from datetime import datetime,timezone
from pathlib import Path
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
BASE=ROOT/"handbook"
spec=importlib.util.spec_from_file_location("b7_inventory_functions",OUT/"inventory_batch7.py")
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
registry=lib.registry;grounded=lib.grounded
grounded.OUT=OUT;grounded.PREFIX="batch7-five-proposal-"
FIELDS=registry.HEADER
SELECTED=["p03-lindstrom","p07-hott-identity-systems","p10-domain-constructions",
          "p15-stochastic-satisfiability","p18-erotetic-implication"]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return p.read_text(encoding="utf-8-sig")
def save(name,data):
    (OUT/("five-"+name+".json")).write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def public(row):return {k:v for k,v in row.items() if not k.startswith("_")}

def main():
    manifest_path=ROOT/"spec/research/edition-2026-authoring-batch-intake-7.json"
    manifest=json.loads(read(manifest_path))
    groups=[g for g in manifest["groups"] if g["stem"] in SELECTED]
    inputs={};guards=[];unresolved=[];rows=[];scopes={};transforms=[];bib=[]
    for p in [BASE/"registry/symbols.csv",BASE/"registry/symbol-scopes.json",
              BASE/"bib/handbook.bib",BASE/"handbook.sty",manifest_path]:
        inputs[p.relative_to(ROOT).as_posix()]={"sha256":sha(p),"text":read(p)}
    old_rows=list(csv.DictReader(io.StringIO(inputs["handbook/registry/symbols.csv"]["text"])))
    old_scopes=json.loads(inputs["handbook/registry/symbol-scopes.json"]["text"])
    old_bib=grounded.bib_records(inputs["handbook/bib/handbook.bib"]["text"])
    bykey={r["key"]:r for r in old_bib}
    index=registry.ReaderIndex(BASE)
    for group in groups:
        if group["integration_status"]!="routed-awaiting-canonical-merge":
            guards.append({"group":group["stem"],"reason":"Root manifest does not confirm selected actual-route stage"})
        for rel in group["bodies"]+group["annexes"]+group.get("rule_sheets",[]):
            p=BASE/rel
            if not p.is_file() or not index.files.get(rel):
                guards.append({"group":group["stem"],"path":rel,"reason":"Selected source is not literally reached"})
            if p.is_file():inputs[p.relative_to(ROOT).as_posix()]={"sha256":sha(p),"text":read(p)}
        if group.get("note"):
            p=ROOT/group["note"];inputs[p.relative_to(ROOT).as_posix()]={"sha256":sha(p),"text":read(p)}

    def local_regions(first,group):
        d=index.unique(first)
        owned=group["bodies"]+group["annexes"]+group.get("rule_sheets",[])
        if d.path not in owned:raise registry.RegistryError("first_use outside selected group")
        if d.path.startswith("annex/"):
            return [{"anchor":d.label}]+([{"anchor":d.owner}] if d.owner else [])
        if d.path.startswith("registry/calculi/"):return [{"file":d.path}]
        headings=[h for h in index.heading_records if h.path==d.path and h.start<=d.start<h.end]
        h=max(headings,key=lambda h:h.start) if headings else None
        selectors=[{"heading_of":first,"level":h.kind}] if h else [{"anchor":first}]
        region=index.region(selectors[0])
        for sites in index.labels.values():
            for a in sites:
                if a.kind=="annexitem" and a.owner and a.path in group["annexes"]:
                    owner=index.unique(a.owner)
                    if region.start<=owner.start<region.end:selectors.append({"anchor":a.label})
        return selectors

    for group in groups:
        for rel in group.get("symbol_intakes",[]):
            path=BASE/rel;inputs[path.relative_to(ROOT).as_posix()]={"sha256":sha(path),"text":read(path)}
            text=read(path);fixed=[];quote_pairs=[]
            for number,line in enumerate(text.splitlines(keepends=True),1):
                m=re.match(r"^(\\\(.*?\\\)),",line)
                if m and "," in m[1]:
                    replacement='"'+m[1].replace('"','""')+'",'+line[m.end():]
                    quote_pairs.append({"line":number,"original":line.rstrip("\r\n"),
                                        "proposed":replacement.rstrip("\r\n")})
                    line=replacement
                fixed.append(line)
            reader=csv.DictReader(io.StringIO("".join(fixed)))
            if reader.fieldnames!=FIELDS:guards.append({"path":rel,"reason":"Unexpected input header"})
            for number,raw in enumerate(reader,2):
                if None in raw:guards.append({"path":rel,"row":number,"reason":"Unmapped CSV overflow"});continue
                row={k:(raw.get(k) or "").strip() for k in FIELDS}
                original=copy.deepcopy(row);reasons=[]
                if group["stem"]=="p15-stochastic-satisfiability" and rel.endswith("symbols-intake-p15-stochastic-satisfiability.csv") and number==2:
                    row.update(glyph=r"\(\ssatrandom^{p}\)",macro=r"\ssatrandom^{p}",
                        role="native rotated-R independent weighted Boolean random quantifier",
                        notes="Native Roman R rotated180 degrees, with parameter p for the declared fixed independent Bernoulli extension. Fair source operator is the separately recorded ssatrandom without annotation. Original upright R^p readable-alias row remains immutable raw evidence; transformed by root's verified source-glyph repair.")
                    reasons.append("Root-confirmed native rotated-R repair and explicit weighted/fair distinction; no upright random alias appended.")
                elif rel.endswith("symbols-intake-p15-ssat-native.csv"):
                    if not row["glyph"].startswith(r"\("):row["glyph"]=r"\("+row["glyph"]+r"\)"
                    reasons.append("Math-mode serialization of the unchanged native glyph; macro/type unchanged.")
                if not row["macro"]:
                    g=row["glyph"];row["macro"]=g[2:-2] if g.startswith(r"\(") and g.endswith(r"\)") else g
                    reasons.append("Blank macro records unchanged spelling, not a new command.")
                if not registry.PREC_RE.fullmatch(row["precedence"]):
                    descriptor=row["precedence"];row["precedence"]="n/a"
                    row["notes"]+=(" " if row["notes"] else "")+"Original precedence descriptor "+repr(descriptor)+" retained; no numerical rank inferred."
                    reasons.append("Precedence descriptor retained, n/a proposed.")
                row.update(_group=group["stem"],_intake=rel,_line=number,_original=original)
                try:selectors=local_regions(row["first_use"],group)
                except registry.RegistryError as exc:
                    guards.append({"group":group["stem"],"path":rel,"row":number,"reason":str(exc)});selectors=[]
                name=row["scope"]
                if name not in old_scopes["scopes"] and not registry.parse_scope(name) and not registry.LABEL_RE.fullmatch(name) and " through " not in name:
                    binding=scopes.setdefault(name,{"presentation":"Actual selected B7 "+group["stem"]+" source declaration and reciprocal proof regions; native argument types, not typography, distinguish roles. No source/proof admission.",
                                                    "regions":[]})
                    for selector in selectors:
                        if selector not in binding["regions"]:binding["regions"].append(selector)
                rows.append(row)
                if public(row)!=original:
                    transforms.append({"group":group["stem"],"intake":rel,"row":number,
                        "original":original,"proposed":public(row),"reasons":reasons,
                        "quote_only_mapping":quote_pairs if number==2 else []})
        for rel in group.get("bibliography_intakes",[]):
            path=BASE/rel;inputs[path.relative_to(ROOT).as_posix()]={"sha256":sha(path),"text":read(path)}
            for record in grounded.bib_records(read(path)):
                bib.append({"group":group["stem"],"intake":rel,"record":record,
                            "fields":grounded.fields(record)})

    decisions_path=OUT/"five-root-decisions.json"
    decisions=json.loads(read(decisions_path)) if decisions_path.is_file() else {}
    alias=decisions.get("citation_aliases",{})
    append_bib=[];bib_decisions=[]
    for item in bib:
        record=item["record"];key=record["key"]
        if key in alias:
            target=alias[key]
            if target not in bykey:guards.append({"key":key,"reason":"Alias target absent"})
            bib_decisions.append({"key":key,"action":"reuse","canonical_key":target,"reason":decisions.get("alias_reasons",{}).get(key,"")})
        elif key in bykey:
            if record["comparison"]!=bykey[key]["comparison"]:
                unresolved.append({"kind":"same-key-publication-decision","key":key,
                    "incoming":grounded.fields(record),"canonical":grounded.fields(bykey[key])})
            bib_decisions.append({"key":key,"action":"existing-key-retained"})
        else:
            append_bib.append(record);bykey[key]=record
            bib_decisions.append({"key":key,"action":"append-distinct-exact-manifestation"})

    # Construct actual source-typed SAME-region exceptions; no role/glyph rename.
    sources={"p07-hott-identity-systems":"HoTT2013PublicReleaseFoundations",
             "p10-domain-constructions":"AbramskyJungCorrectedExpandedDomainTheory"}
    typed_pairs=[]
    for group,local_role,broad_role,reason in [
        ("p07-hott-identity-systems","integer-cover point constructor","coequalizer point constructor",
         "Native c has A→W in the general coequalizer and Z→R in the cover, explicitly declared in the SAME packet and compared in the cover proof. Constructor domain and codomain identify the occurrence; no source rename or fake disjoint region."),
        ("p10-domain-constructions","formal continuous semilattice union","ordinary union of finite basis sets",
         "The SAME Plotkin declaration/proofs use cup on finite basis subsets and on round ideals/dcpo-semilattice elements. Operand type determines set union versus formal algebra operation; formal union need not be set union or an information-order join.")
    ]:
        local=next((r for r in rows if r["_group"]==group and r["role"]==local_role),None)
        broad=next((r for r in rows if r["_group"]==group and r["role"]==broad_role),None)
        if local and broad:
            rule={"glyph":local["glyph"],"local_role":local["role"],"first_use":local["first_use"],
                  "broader_scope":broad["scope"],"broader_role":broad["role"],
                  "reason":reason,"source":sources[group]}
            scopes[local["scope"]].setdefault("overrides",[]).append(rule);typed_pairs.append(rule)
    for item in decisions.get("overrides",[]):
        scopes[item["scope"]].setdefault("overrides",[]).append(item["rule"])
    combined=copy.deepcopy(old_scopes);combined["scopes"].update(scopes)
    resolver=registry.Resolver(BASE,bindings=combined,index=index)
    resolver.source_keys.update(r["key"] for r in append_bib)
    decoded=[]
    for number,row in enumerate(old_rows,2):
        try:
            item=dict(row);item.update(_line=number,_scope=resolver.resolve(row["scope"]));decoded.append(item)
        except registry.RegistryError as exc:guards.append({"canonical_line":number,"reason":"Canonical scope data unavailable: "+str(exc)})
    incoming=[]
    for row in rows:
        try:
            row["_scope"]=resolver.resolve(row["scope"])
            if not resolver.contains(row["_scope"],row["first_use"]):
                guards.append({"group":row["_group"],"row":row["_line"],"reason":"First-use not in proposed source extent"})
            incoming.append(row)
        except registry.RegistryError as exc:guards.append({"group":row["_group"],"row":row["_line"],"reason":str(exc)})
    # Preparation compares exact row identities and occupied source regions.
    # It never calls collision_check, read_rows, strict checker or review tools.
    overlaps=[];bucket={}
    for row in decoded+incoming:bucket.setdefault(re.sub(r"\s+","",row["glyph"]),[]).append(row)
    for entries in bucket.values():
        for n,a in enumerate(entries):
            for b in entries[n+1:]:
                if not(a.get("_group") or b.get("_group")) or not resolver.overlaps(a["_scope"],b["_scope"]):continue
                supported=(a["role"]!=b["role"] and
                    (resolver.authorized_override(a,b) or resolver.authorized_override(b,a)))
                record={"a":public(a),"b":public(b),"a_group":a.get("_group","canonical"),
                    "b_group":b.get("_group","canonical"),"typed_exception_proposed":supported}
                overlaps.append(record)
                if not supported:unresolved.append({"kind":"overlapping-native-row-decision",**record})

    changed=[p for p,v in inputs.items() if sha(ROOT/p)!=v["sha256"]]
    if changed:guards.append({"reason":"Inputs changed during preparation","paths":changed})
    order={};sizes={}
    if not guards and not unresolved and decisions.get("emit_ordered_patches"):
        for key,updates in decisions.get("bibliography_metadata",{}).items():
            original=next(r for r in old_bib if r["key"]==key)
            proposed=grounded.update_record(original,updates)
            names,ss=grounded.replacement_chunks("bibliography-metadata",BASE/"bib/handbook.bib",
                                                 [(original["raw"],proposed["raw"])])
            order.setdefault("bibliography_metadata",[]).extend(names);sizes.update(ss)
        names,ss=grounded.chunks("bib",BASE/"bib/handbook.bib",old_bib[-1]["raw"],
                                [r["raw"] for r in append_bib])
        order["bibliography"]=names;sizes.update(ss)
        scope_text=inputs["handbook/registry/symbol-scopes.json"]["text"]
        last=next(reversed(old_scopes["scopes"]));token=json.dumps(last,ensure_ascii=False)
        sites=list(re.finditer(r"(?m)^([ \t]*)"+re.escape(token)+r"\s*:",scope_text))
        if len(sites)!=1:raise RuntimeError("Nonunique canonical scope tail")
        site=sites[0];start=site.start();at=start+len(site[1])
        value=scope_text.index(":",at+len(token))+1
        while scope_text[value].isspace():value+=1
        _,extent=json.JSONDecoder().raw_decode(scope_text[value:])
        anchor=scope_text[start:value+extent];prefix=scope_text[start:at]
        members=[prefix+json.dumps(name,ensure_ascii=False)+": "+json.dumps(value,ensure_ascii=False,separators=(",",":"))
                 for name,value in scopes.items()]
        names,ss=grounded.chunks("scopes",BASE/"registry/symbol-scopes.json",anchor,members,True)
        order["scopes"]=names;sizes.update(ss)
        names,ss=grounded.chunks("symbols",BASE/"registry/symbols.csv",
            inputs["handbook/registry/symbols.csv"]["text"].rstrip().splitlines()[-1],
            [grounded.csv_lines([public(r)]) for r in rows])
        order["symbols"]=names;sizes.update(ss)
        for group in groups:
            for rel in group["bodies"]+group["annexes"]:
                text=inputs["handbook/"+rel]["text"];pairs=[]
                for line in text.splitlines():
                    transformed=line
                    def convert(m):
                        keys=list(dict.fromkeys(alias.get(k.strip(),k.strip()) for k in m[1].split(",")))
                        return "{"+",".join(keys)+"}"
                    # Restrict alias substitutions to literal citation key groups.
                    transformed=re.sub(r"\{([^{}]*"+("|".join(re.escape(x) for x in alias))+r"[^{}]*)\}",convert,line) if alias else line
                    if transformed!=line:pairs.append((line,transformed))
                if pairs:
                    names,ss=grounded.replacement_chunks("citations-"+group["stem"]+"-"+Path(rel).parent.name+"-"+rel.split("/")[0],
                                                         BASE/rel,pairs)
                    order.setdefault("citations",[]).extend(names);sizes.update(ss)
    result={"utc":datetime.now(timezone.utc).isoformat(),"selected_groups":SELECTED,
        "retained_offroute_groups":[g["stem"] for g in manifest["groups"] if g["stem"] not in SELECTED and not g["integration_status"].startswith("merged")],
        "canonical_symbols_before":len(old_rows),"canonical_bib_before":len(old_bib),
        "raw_selected_symbol_rows":len(rows),"raw_selected_bib_records":len(bib),
        "proposed_symbol_rows":[public(r) for r in rows],"append_only_scopes":scopes,
        "transformations":transforms,"bibliography_decisions":bib_decisions,
        "append_bib_records":append_bib,"actual_typed_overlaps":overlaps,
        "root_decisions_required":unresolved,"preparation_guards":guards,
        "input_hashes":{p:v["sha256"] for p,v in inputs.items()},
        "baseline_sha256":sha(OUT/"pre-batch7-numeric-meanings.json"),
        "application_order":order,"patch_characters":sizes,
        "batch6_pending_preserved":["p15-hintikka","p10-abelian"],
        "scope":manifest["scope"],"standing":"CANONICAL PREPARATION ONLY. No independent checks/review/build/render; no target edited. Patches emitted only for confirmed actual five and resolved explicit root decisions; other seven retained without credit."}
    save("stage",result);save("decisions-required",unresolved);save("transformed-rows",[public(r) for r in rows])
    save("scope-bindings",scopes);save("transformations",transforms)
    print(json.dumps({"utc":result["utc"],"selected_symbols":len(rows),"selected_bib":len(bib),
        "new_bib":len(append_bib),"new_scopes":len(scopes),"typed_overlaps":len(overlaps),
        "root_decisions":len(unresolved),"preparation_guards":len(guards),"patches":sum(map(len,order.values()))}))

if __name__=="__main__":main()
