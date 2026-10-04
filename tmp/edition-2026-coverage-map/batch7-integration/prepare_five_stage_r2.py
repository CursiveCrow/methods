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
grounded.OUT=OUT;grounded.PREFIX="batch7-five-r2-proposal-"
FIELDS=registry.HEADER
SELECTED=["p03-lindstrom","p07-hott-identity-systems","p10-domain-constructions",
          "p15-stochastic-satisfiability","p18-erotetic-implication"]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return p.read_text(encoding="utf-8-sig")
def save(name,data):
    (OUT/("five-r2-"+name+".json")).write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def public(row):return {k:v for k,v in row.items() if not k.startswith("_")}


def actual_forms(row,group,rel,number):
    members=[]
    def family(glyph,role,parts):
        row["glyph"]=r"\("+glyph+r"\)"
        row["macro"]=glyph
        row["role"]=role
        row["notes"]+=" Family listing, not one atomic glyph: "+"; ".join(p[0]+" "+p[1] for p in parts)+"."
        for glyph,meaning in parts:
            members.append({"glyph":r"\("+glyph+r"\)","macro":glyph,"role":meaning,
                            "first_use":row["first_use"]})
    if group["stem"]=="p15-stochastic-satisfiability" and rel.endswith("symbols-intake-p15-stochastic-satisfiability.csv"):
        glyphs={3:r"\Pi",4:r"\phi|_{x=b}",5:r"\bar x",6:r"V(\Pi,\phi)",
                7:r"\theta",8:r"\Downarrow",9:r"\operatorname{Eval}",
                11:r"p_b",12:r"\mu",13:r"C_{i,u}",14:r"\Psi",
                15:r"\widehat v_s",16:r"D",17:r"P",18:r"N_{h,b}",
                19:r"F_m^{k,n}",20:r"Z"}
        if number in glyphs:
            g=glyphs[number];row["glyph"]=r"\("+g+r"\)";row["macro"]=g
            row["notes"]+=" Actual displayed reader TeX spelling; original ASCII intake remains raw evidence."
        if number==8:
            row["first_use"]="def:p15-ssat-evaluation-judgment"
            row["notes"]+=" Real judgment definition before the literal sheet; no inferred definition from value alone."
        if number==10:
            family("L,H","threshold-window endpoint symbol family",
                   [("L","lower threshold-window endpoint"),("H","upper threshold-window endpoint")])
        if number in (13,15,18,19):
            row["notes"]+=" Indexed symbol family at the stated indices, not the former hyphenated ASCII alias."
    if group["stem"]=="p18-erotetic-implication":
        simple={2:r"D_L",3:r"dQ",5:r"\mathcal P",6:r"\models_L",
                7:r"\mathrel{\|=}_L",9:r"\operatorname{Im}_L",10:r"E_L",
                11:r"\operatorname{RIm}_L",13:r"\operatorname{Pres}(Q)"}
        if number in simple:
            g=simple[number];row["glyph"]=r"\("+g+r"\)";row["macro"]=g
        if number==3:
            row["role"]="direct-answer set in the declared general fixed language L, possibly infinite (closed first-order answers in the wh instances)"
            row["scope"]="P18 generalized direct-answer declaration"
            row["notes"]+=" Domain/standing differs from the old finite-propositional PMCE record. The declaration-local catalog scope is chosen for existing resolver containment only; every later body/proof use is separately exposed as provenance. No extensional identity with an arbitrary old PMCE answer assignment is asserted."
        if number==4:
            family(r"P,T_P,U_P","admissible-partition and component symbol family",
                [("P","admissible partition"),("T_P","designated-true declarative component"),
                 ("U_P","complementary untrue declarative component")])
        if number==8:
            family(r"\vdash_\ell,\operatorname{Cn}_\ell","declarative-consequence relation/operator symbol family",
                [(r"\vdash_\ell","declarative consequence relation"),
                 (r"\operatorname{Cn}_\ell","declarative consequence-set operator")])
        if number==12:
            row.update(glyph=r"\(Y_B\)",macro="Y_B",
                       role="first-leg nonempty proper answer-reduction witness family indexed by B")
            row["notes"]+=" Split from the original Y_B/V_C family: Y_B is actually declared here; V_C is separately bound to the composition theorem."
        if number==14:
            family(r"F_C,Q^C","conditional-prefix map and transformed-question symbol family",
                [("F_C","conditional prefix map on declarative answer sets"),
                 ("Q^C","corresponding conditional-prefixed question")])
        if number==15:
            family(r"G_X,Q_X,R_X","conjunctive-prefix map and transformed-question symbol family",
                [("G_X","finite conjunctive prefix map on declaratives and their sets"),
                 ("Q_X","first exact conjunctively transformed question"),
                 ("R_X","second exact conjunctively transformed question")])
        if number==16:
            family(r"?S(Ax),?U(Ax)","source wh-question-form family",
                [(r"?S(Ax)","named-witness wh-question form"),
                 (r"?U(Ax)","nonempty finite complete-list wh-question form")])
        row["notes"]+=" Actual displayed TeX forms; original family descriptor retained as raw evidence."
    return row,members


def main():
    manifest_path=ROOT/"spec/research/edition-2026-authoring-batch-intake-7.json"
    manifest=json.loads(read(manifest_path))
    groups=[g for g in manifest["groups"] if g["stem"] in SELECTED]
    inputs={};guards=[];unresolved=[];rows=[];scopes={};transforms=[];bib=[];raw_count=0
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
                original=copy.deepcopy(row);reasons=[];raw_count+=1
                row,members=actual_forms(row,group,rel,number)
                if members:row["_family_members"]=members
                if any(row.get(k)!=original.get(k) for k in FIELDS):
                    reasons.append("Root-directed actual-glyph/family/first-use preparation repair; no original intake edited.")
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
                if name=="P18 generalized direct-answer declaration":
                    selectors=[{"anchor":"def:p18-ei-setting"}]
                if name not in old_scopes["scopes"] and not registry.parse_scope(name) and not registry.LABEL_RE.fullmatch(name) and " through " not in name:
                    binding=scopes.setdefault(name,{"presentation":"Actual selected B7 "+group["stem"]+" source declaration and reciprocal proof regions; native argument types, not typography, distinguish roles. No source/proof admission.",
                                                    "regions":[]})
                    if name=="P18 generalized direct-answer declaration":
                        binding["presentation"]="Exact generalized direct-answer declaration at def:p18-ei-setting; not a claim that later use/proof regions are absent. Those complete occurrences are exposed in the stage's separate provenance and the relation usage bindings. Old finite-propositional PMCE scope remains unchanged."
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


    # One original witness-family record has two genuinely different declarations.
    p18=next(g for g in groups if g["stem"]=="p18-erotetic-implication")
    original_witness=next(r for r in rows if r["_group"]==p18["stem"] and r["_line"]==12)
    second=copy.deepcopy(original_witness)
    second.update(glyph=r"\(V_C\)",macro="V_C",
        role="second-leg nonempty proper answer-reduction witness family indexed by C",
        first_use="thm:p18-ei-composition",
        notes="V_C is actually declared in the composition theorem as the second-leg witness subset of dR. Split from original raw Y_B/V_C record at line12; no fake first-use at the earlier relation definition.")
    second.pop("_family_members",None)
    rows.append(second)
    for selector in local_regions(second["first_use"],p18):
        if selector not in scopes[second["scope"]]["regions"]:
            scopes[second["scope"]]["regions"].append(selector)
    transforms.append({"group":p18["stem"],"intake":second["_intake"],"row":12,
        "original":second["_original"],"proposed":public(second),
        "reasons":["Split V_C to its actual later declaration; retained the raw jointly listed family."]})
    source_additions={
      "P15 SSAT native syntax":[
        "thm:p15-ssat-native-correspondence","annex:p15.ssat-native-correspondence"],
      "p18 erotetic implication":[
        "thm:p18-ei-composition","annex:p18.ei.composition",
        "thm:p18-ei-nontransitivity","annex:p18.ei.nontransitivity",
        "thm:p18-ei-native-patterns","annex:p18.ei.native-patterns",
        "def:p18-ei-travel-inquiry","thm:p18-ei-inquiry","annex:p18.ei.inquiry",
        "def:p18-ei-certificate","thm:p18-ei-certificate","annex:p18.ei.certificate"]
    }
    for name,labels in source_additions.items():
        for label in labels:
            try:index.unique(label)
            except registry.RegistryError as exc:
                guards.append({"scope":name,"label":label,"reason":str(exc)});continue
            selector={"anchor":label}
            if selector not in scopes[name]["regions"]:scopes[name]["regions"].append(selector)

    # The catalog exception is declaration-local; later use is NOT hidden.
    # Record every actual direct-answer spelling/argument variant and its owner.
    dq_tokens=re.compile(r"(?<![A-Za-z])d(?:[QRUS](?:_[A-Za-z])?|\?[SU]|\s*\(\??[QRUS]|\\(?:bigl|left)\s*\(\??[QRUS])|\\\(\s*d\s*\\\)")
    dq_usage=[]
    for rel in p18["bodies"]+p18["annexes"]+p18.get("rule_sheets",[]):
        text=inputs["handbook/"+rel]["text"];lines=text.splitlines()
        declarations=[d for sites in index.labels.values() for d in sites
                      if d.path==rel and d.kind in registry.ReaderIndex.NAMED]
        intervals=[]
        for d in declarations:
            depth=0;end_line=len(lines)
            pattern=re.compile(r"\\(begin|end)\{"+re.escape(d.kind)+r"\}")
            for line_no in range(d.line-1,len(lines)):
                for event in pattern.finditer(lines[line_no]):
                    depth+=1 if event[1]=="begin" else -1
                    if depth==0:
                        end_line=line_no+1;break
                if depth==0:break
            intervals.append((d,d.line,end_line))
        for line_no,line in enumerate(lines,1):
            tokens=[m[0] for m in dq_tokens.finditer(line)]
            if not tokens:continue
            enclosing=[x for x in intervals if x[1]<=line_no<=x[2]]
            owner=max(enclosing,key=lambda x:x[1])[0] if enclosing else None
            dq_usage.append({"path":"handbook/"+rel,"line":line_no,
                "sha256":inputs["handbook/"+rel]["sha256"],"literal_tokens":tokens,
                "text":line,"declaration_or_proof":owner.label if owner else None,
                "kind":owner.kind if owner else "prose",
                "body_owner":owner.owner if owner and owner.kind=="annexitem" else
                             (owner.label if owner else None),
                "standing":"Actual occurrence/owner provenance, not proof acceptance or a claim that the old finite PMCE d assignment equals this generalized one."})
    old_dq=next(r for r in old_rows if r["glyph"]==r"\(dQ\)" and r["scope"]=="P18 question evocation")
    old_binding=copy.deepcopy(old_scopes["scopes"][old_dq["scope"]])
    new_binding=copy.deepcopy(scopes["P18 generalized direct-answer declaration"])
    local_region=index.region({"anchor":"def:p18-ei-setting"})
    old_regions=[index.region(s) for s in old_binding["regions"]]
    declaration_contained=any(r.start<=local_region.start and local_region.end<=r.end
                              for r in old_regions)
    if not declaration_contained:
        guards.append({"reason":"Proposed generalized dQ declaration is outside unchanged older body scope"})
    dq_proposal={"old_row":old_dq,"old_binding_preserved_unchanged":old_binding,
        "new_scope_name":"P18 generalized direct-answer declaration",
        "new_binding_proposed":new_binding,"actual_first_use":"def:p18-ei-setting",
        "declaration_contained_in_old_body_region":declaration_contained,
        "actual_declaration_region":{"start":local_region.start,"end":local_region.end,
                                    "part":local_region.part,"chapter":local_region.chapter},
        "all_later_usage_provenance":dq_usage,
        "relation_scope_regions_preserved":scopes["p18 erotetic implication"]["regions"],
        "decision":"Retain both domain-specific records and the same glyph. Bind the new catalog standing only to its actual generalized declaration, satisfying existing containment with no resolver change. All later body/annex/sheet use and owners remain exposed; relation/correspondence/certificate scopes retain their proof regions. Root reads/adopts this proposal before applying.",
        "source_keys":["Wisniewski2001QuestionsInferences","Wisniewski2018DeductionReduction"],
        "old_source_domain":"Finite propositional question expressions over Form with n>1 direct answers.",
        "new_source_domain":"Declared general fixed L with possibly infinite assigned direct-answer sets; closed first-order answers in wh instances. No arbitrary extensional identity with the PMCE assignment."}
    decisions_path=OUT/"five-r2-root-decisions.json"
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
    dq_proposal["new_binding_proposed"]=copy.deepcopy(scopes["P18 generalized direct-answer declaration"])
    dq_proposal["adoption_standing"]="Root read and adopted the declaration-local binding and its limited standing on resumed authoring; old finite PMCE binding and record remain unchanged. All later use remains exposed; no extensional-identity claim or resolver change."
    save("dq-binding-proposal",dq_proposal)
    # Fresh actual old-chapter identity changes, not a replay of an old stage.
    numeric_path=OUT/"batch7-proposal-numeric-migrations.json"
    numeric=json.loads(read(numeric_path))
    if numeric["baseline_sha256"]!=sha(OUT/"pre-batch7-numeric-meanings.json"):
        guards.append({"reason":"Numeric proposal baseline differs from immutable pre-B7 capture"})
    if numeric.get("changed_during_capture") or numeric.get("unresolved"):
        guards.append({"reason":"Numeric identity preparation is unsettled",
                       "changed":numeric.get("changed_during_capture"),"unresolved":numeric.get("unresolved")})
    migrations={r["canonical_line"]:r for r in numeric["proposed_migration_rows"]}
    for change in migrations.values():
        if change["binding"]:
            name=change["proposed"]["scope"]
            if name in old_scopes["scopes"]:
                guards.append({"reason":"Would replace an old named scope","scope":name})
            elif name in scopes and scopes[name]!=change["binding"]:
                guards.append({"reason":"Conflicting frozen numeric binding","scope":name})
            else:scopes[name]=copy.deepcopy(change["binding"])
    inputs[numeric_path.relative_to(ROOT).as_posix()]={"sha256":sha(numeric_path),"text":read(numeric_path)}
    combined=copy.deepcopy(old_scopes);combined["scopes"].update(scopes)
    resolver=registry.Resolver(BASE,bindings=combined,index=index)
    resolver.source_keys.update(r["key"] for r in append_bib)
    decoded=[]
    for number,original_row in enumerate(old_rows,2):
        row=copy.deepcopy(migrations[number]["proposed"] if number in migrations else original_row)
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
    overlaps=[];bucket={};member_records=[]
    expanded=[]
    for row in incoming:
        if row.get("_family_members"):
            for member in row["_family_members"]:
                projected=copy.deepcopy(row);projected.update(member)
                projected["_family_parent"]=row["glyph"]
                member_records.append({"family_record":public(row),"member":public(projected),
                    "standing":"Actual family member participates in overlap preparation; not hidden as one atomic combined glyph."})
                expanded.append(projected)
        else:expanded.append(row)
    for row in decoded+expanded:bucket.setdefault(re.sub(r"\s+","",row["glyph"]),[]).append(row)
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
        raw_lines=inputs["handbook/registry/symbols.csv"]["text"].splitlines()
        replacements=[(raw_lines[line-1],grounded.csv_lines([change["proposed"]]))
                      for line,change in migrations.items()]
        names,ss=grounded.replacement_chunks("numeric-meanings",BASE/"registry/symbols.csv",replacements)
        order["numeric_meanings"]=names;sizes.update(ss)
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
        "retained_offroute_groups":[g["stem"] for g in manifest["groups"] if g["stem"] not in SELECTED and g["integration_status"]=="frozen-unrouted"],
        "retained_other_groups":[{"stem":g["stem"],"integration_status":g["integration_status"],"standing":"Outside this actual-five canonical subset; current route status is factual, not credit from this packet."} for g in manifest["groups"] if g["stem"] not in SELECTED and not g["integration_status"].startswith("merged")],
        "canonical_symbols_before":len(old_rows),"canonical_bib_before":len(old_bib),
        "raw_selected_symbol_rows":raw_count,"proposed_symbol_rows_count":len(rows),"raw_selected_bib_records":len(bib),
        "family_member_records":member_records,"source_region_additions":source_additions,
        "dq_binding_proposal":dq_proposal,
        "numeric_identity_proposals":numeric,
        "numeric_migration_rows":len(migrations),
        "new_symbol_source_scopes":len(scopes)-len({r["proposed"]["scope"] for r in migrations.values() if r["binding"]}),
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
    save("scope-bindings",scopes);save("transformations",transforms);save("family-members",member_records)
    print(json.dumps({"utc":result["utc"],"selected_symbols":len(rows),"raw_symbol_records":raw_count,"selected_bib":len(bib),
        "new_bib":len(append_bib),"new_scopes":len(scopes),"numeric_migrations":len(migrations),"typed_overlaps":len(overlaps),
        "root_decisions":len(unresolved),"preparation_guards":len(guards),"patches":sum(map(len,order.values()))}))

if __name__=="__main__":main()
