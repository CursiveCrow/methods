"""Materialize root's 35 reserved mathematical goal mappings for shard A."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/"spec/coverage/edition-2026"
sys.path.insert(0,str(ROOT/"tools"))
import check as grammar

def read_rows(name):
    return [json.loads(s) for s in (DEST/name).read_text(encoding="utf-8-sig").splitlines() if s.strip()]
requirements={r["original_requirement_id"]:r for r in read_rows("requirements-crosswalk.jsonl")}
existing_units={r["unit_id"]:r for r in read_rows("requirements-units.jsonl")}
with (DEST/"root-depth-profiles.tsv").open(encoding="utf-8",newline="") as stream:
    profiles=list(csv.DictReader(stream,delimiter="\t"))
if len(profiles)!=35 or len({r["id"] for r in profiles})!=35:
    raise SystemExit("Wrong reserved goal set")

anchors={
1:["def:p08-modal-canonical-model","thm:p08-modal-canonical-completeness","annex:p8.modal.1"],
2:["def:p08-modal-filtration","thm:p08-modal-filtration"],
3:["def:p08-modal-standard-translation","thm:p08-modal-correspondence","tab:p08-modal-correspondence","def:p08-sahlqvist-class","thm:p08-sahlqvist"],
4:["def:p08-modal-bisimulation","thm:p08-modal-bisimulation-invariance","thm:p08-van-benthem"],
5:["def:p08-modal-b-convention","entry:p08-modal-d","entry:p08-modal-b","entry:p08-modal-k4","entry:p08-modal-kd45","entry:p08-modal-grz","tab:p08-modal-systems"],
6:["def:p08-tense-until-since","thm:p08-kamp","def:p08-modal-fusion","def:p08-ockhamist-peircean"],
7:["def:p08-neighborhood-model","def:p08-neighborhood-conditions","entry:p08-neighborhood-e","entry:p08-neighborhood-m","entry:p08-neighborhood-c","entry:p08-neighborhood-n","entry:p08-neighborhood-r"],
8:["def:p08-qml-family","def:p08-qml-model","def:p08-qml-domain-regimes","def:p08-barcan-schemas","thm:p08-barcan-domain-validities"],
10:["sec:p09-presentation-n-c-013"],
11:["def:p08-distributed-knowledge","def:p08-public-announcement","thm:p08-pal-reduction","entry:p08-pal","def:p08-unsuccessful-announcement"],
13:["def:p08-heyting-algebra","thm:p08-heyting-completeness","thm:p10-heyting-completeness","thm:p10-heyting-prime-representation","thm:p10-ipc-prime-kripke-completeness","thm:p10-rasiowa-sikorski"],
14:["def:p08-ipl-topological-semantics","thm:p08-topological-completeness"],
15:["def:p08-bhk-reading","def:p07-number-realizability","thm:p07-number-realizability-soundness"],
16:["thm:p08-normal-existence-extraction","sec:normalization-curry-howard-01"],
17:["def:p08-iqc-expanding-domain","thm:p08-iqc-completeness","def:p08-iqc-constant-domain-principle","thm:p08-iqc-constant-domain-boundary"],
18:["def:p08-intermediate-logic","def:p08-intermediate-lattice","thm:p08-kc-profile","thm:p08-lc-profile","thm:p10-intermediate-variety-correspondence"],
20:["def:p08-lukasiewicz-matrices","thm:p08-finite-lukasiewicz-tableau","entry:p08-lukasiewicz-finite","entry:p08-lukasiewicz-infinite","thm:p08-lukasiewicz-completeness","thm:p08-mcnaughton"],
21:["def:p08-tnorm-residuum","thm:p08-tnorm-completeness","tab:p08-tnorm-logics","sec:p10-many-substructural"],
22:["def:p10-mv-algebra","sec:p10-many-substructural"],
23:["def:p08-post-n-valued","thm:p08-post-matrix-decision","thm:p08-post-matrix","annex:p8.post.1"],
24:["def:p08-fde-matrix","def:p08-fde-orders","entry:p08-fde","thm:p08-k3-lp-facts"],
25:["def:p08-weak-kleene-matrix","def:p08-bochvar-external","thm:p08-bochvar-tableau"],
26:["def:p08-supervaluation","thm:p08-supervaluation-classical","def:p08-supervaluation-gap"],
28:["def:p08-cll-language","def:p08-focusing-polarity","entry:p08-cll","thm:p08-cll-cut-elimination","thm:p08-linear-decision-boundaries"],
29:["def:p08-phase-space","thm:p08-phase-adequacy"],
30:["def:p08-linear-pointer-boundary","def:p07-proof-nets-goi-boundary"],
31:["def:p07-generalized-sequent-frameworks","tab:p07-generalized-frameworks","def:p07-worked-derivation-boundary","def:p07-gs5-derivation","def:p07-labelled-k-derivation","def:p07-display-k-derivation","def:p07-deep-s5-derivation"],
32:["def:p08-pointed-rm-frame","entry:p08-relevance-r","thm:p08-relevance-adequacy","thm:p08-relevance-variable-sharing","thm:p08-gamma-admissibility"],
33:["def:p08-lambek-semantics","entry:p08-lambek-l","thm:p08-lambek-adequacy"],
34:["def:p10-residuated-lattice","sec:p10-many-substructural"],
35:["def:p08-default-theory","def:p08-circumscription","def:p08-autoepistemic-expansion","entry:p08-reiter-default","entry:p08-circumscription","entry:p08-autoepistemic"],
36:["def:p08-agm","tab:p08-agm-postulates","tab:p08-agm-contraction-postulates","def:p08-agm-faithful-preorder","thm:p08-agm-representation"],
37:["def:p08-sdl","def:p08-dyadic-obligation","tab:p08-deontic-systems"],
38:["def:p08-stalnaker-conditional","def:p08-lewis-conditional","def:p08-ck-semantics","thm:p08-ck-completeness","thm:p08-vc-completeness","tab:p08-conditional-logics"],
39:["def:p10-boolean-algebra","thm:p10-ultrafilter-separation","thm:p10-stone-representation","thm:p10-stone-duality","thm:p10-countable-atomless-uniqueness","thm:p10-cantor-cylinder-algebra","thm:p10-atoms-isolated"]}

paths={d["path"] for p in profiles for d in requirements[p["id"]]["present_destinations"]}
paths.update(["handbook/parts/p07/functional-interpretations.tex","handbook/parts/p07/lambda-calculi-and-type-theories.tex",
    "handbook/restoration/inherited-11961-12029.tex","handbook/parts/p10/stone-duality.tex","handbook/parts/p10/countable-atomless.tex",
    "handbook/parts/p10/intermediate-algebras.tex","handbook/parts/p10/heyting-completeness.tex","handbook/parts/p10/rasiowa-sikorski.tex"])
lookup={}
for rel in sorted(paths):
    path=ROOT/rel
    text=grammar.strip_verbatims(grammar.strip_comments(path.read_text(encoding="utf-8-sig")))
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    for m in re.finditer(r"\\label\{([^{}]+)\}",text):
        lookup.setdefault(m.group(1),[]).append({"path":rel,"line":text.count("\n",0,m.start())+1,"label":m.group(1),"sha256":sha,"kind":"explicit label"})
    for m in grammar.HB_ENV_RE.finditer(text):
        env=m.group(1)
        arity=3 if env in grammar.HB_STATUS_ENVS or env=="annexitem" else 2
        args,end=grammar.scan_braced_args(text,m.end(),arity)
        if len(args)==arity:
            close=text.find("\\end{"+env+"}",end)
            lookup.setdefault(args[0],[]).append({"path":rel,"line":text.count("\n",0,m.start())+1,"label":args[0],"sha256":sha,
                "kind":env,"title":args[-1],"declared_status":args[1] if env in grammar.HB_STATUS_ENVS else None,
                "declaration_text":text[end:close] if close>=0 else None})

bib=(ROOT/"handbook/bib/handbook.bib").read_text(encoding="utf-8-sig")
bib_records={}
for m in re.finditer(r"@[A-Za-z]+\s*\{",bib):
    args,end=grammar.scan_braced_args(bib,m.end()-1,1)
    if args and "," in args[0]:
        key=args[0].split(",",1)[0].strip()
        bib_records[key]={"path":"handbook/bib/handbook.bib","line":bib.count("\n",0,m.start())+1,"literal_record":bib[m.start():end]}

proposals=[]
unresolved=[]
for p in profiles:
    rid=p["id"]; r=requirements[rid]
    keys=p["source_keys"].split(",")
    missing_keys=[k for k in keys if k not in bib_records]
    related=[s for s in p["related_requirements"].split(";") if s]
    bad_related=[x for x in related if x not in requirements]
    if missing_keys or bad_related:
        raise SystemExit(json.dumps({"id":rid,"missing_bib":missing_keys,"missing_related_ids":bad_related}))
    n=int(rid.rsplit("-",1)[1])
    present=[]
    for label in anchors[n]:
        matches=lookup.get(label,[])
        if len(matches)!=1:
            unresolved.append({"requirement":rid,"label":label,"matches":len(matches)})
        else:
            present.append(matches[0])
    home=r["original_register_row"]["target_home"].split(".")[0].lower()
    home="p"+home[1:].zfill(2)
    proposed_body=f"handbook/parts/{home}/presentations/{rid.lower()}-completion.tex"
    proposed_annex=f"handbook/annex/{home}/{rid.lower()}-completion.tex"
    descriptions=[s.strip() for s in p["components"].split(";") if s.strip()]
    parent_ids=[c["component_id"] for uid in r["unit_ids"] for c in existing_units[uid]["required_components"]]
    child_components=[{"component_id":f"{rid}-MAP-{i:02}","parent_component_ids":parent_ids,"description":description,
        "success_condition":"Supply this exact subgoal under the named source/calculus/language and hypothesis regime, including every required construction, proof direction, example and limitation.",
        "failure_condition":p["failure_case"],
        "required_source_extent":{"authority":"Exact original mathematical goal, not an unspecified whole monograph","original_goal":r["original_wording"],"selected_source_keys":keys,"bounded_mathematical_extent":description},
        "destination":{"existing_goal_anchors":[{"path":x["path"],"label":x["label"],"line":x["line"]} for x in present],
            "completion_body":proposed_body,"completion_annex":proposed_annex,"completion_label":f"sec:{home}-{rid.lower()}-component-{i:02}"},
        "standing":"Finite owed subgoal/destination; current presence or proof acceptance is not inferred from an anchor."} for i,description in enumerate(descriptions,1)]
    source_presentations=[{"source_id":"original-register:"+rid,"title":r["original_wording"],
        "version":"Original depth-gaps requirement and complete original notes; this row specifies a mathematical goal, not an unidentified external edition",
        "precise_extent":{"original_register_row":r["original_register_row"],"subgoal_ids":[c["component_id"] for c in child_components]},
        "standing":"The exact mathematical/construction goal is the authority for scope. Published source variants remain separate below and in the linked N/source units."}]
    for key in keys:
        source_presentations.append({"source_id":key,"bibliographic_identity":bib_records[key],
            "precise_extent":"The exact named goal and listed subgoals as presented by this identified source, including its actual proof/hypothesis boundaries; not automatic reconstruction of the whole cited monograph.",
            "extent_component_ids":[c["component_id"] for c in child_components],
            "body_access_standing":"Primary body access and exact publication-copy fidelity not reaccepted by this mapping block."})
    proposals.append({"original_requirement_id":rid,"original_wording":r["original_wording"],"original_register_row":r["original_register_row"],
        "unit_ids":r["unit_ids"],"parent_component_ids_preserved":parent_ids,"required_subcomponents":child_components,
        "source_presentations":source_presentations,
        "prerequisites":[{"named_premise":s.strip(),"role":"specific mathematical interface or explicit ambient hypothesis; exact body/source treatment identified by the retained anchors and related units"} for s in p["prerequisites"].split(";") if s.strip()],
        "related_original_requirement_ids":related,
        "related_unit_ids":sorted({uid for other in related for uid in requirements[other]["unit_ids"]}),
        "present_destinations":present,"precise_missing_completion_destinations":{"body":proposed_body,"annex":proposed_annex},
        "destination_rule":"Amend/complete existing correct treatment first. These exact disjoint completion destinations are available for missing full developments, not duplicate copies of already supplied proofs; route them during authoring integration only.",
        "proof_boundary_rule":"Preserve all explicit full-proof obligations and current source-specific boundaries. A statement-only subgoal does not itself create an unrelated whole-source proof obligation; source access and any separately promised proof still remain owed. Old E/T/S/P ceilings do not retire a full treatment required elsewhere.",
        "mapping_state":"resolved","scope_state":"resolved","unresolved_questions":[],
        "preserve_current_assessment":True,"current_assessment":r["current_assessment"],
        "remaining_work":r["current_assessment"].get("remaining_book_work",[])+["Read the exact selected source extents as needed and complete every unsupplied subgoal without weakening its stated regime.","Reconcile source-specific overlaps with the listed N/source units and integrate the actual proof/lookup destinations.","Obtain the final consolidated independent content and publication reviews; this scope mapping supplies no acceptance."],
        "evidence":["spec/coverage/edition-2026/root-depth-profiles.tsv","spec/coverage/edition-2026/requirements-crosswalk.jsonl"]})
if unresolved:
    raise SystemExit(json.dumps({"unresolved_live_anchor_bindings":unresolved},ensure_ascii=False))
out=DEST/"root-depth-proposals.jsonl"
if out.exists():
    raise SystemExit("Preserve prior proposal output")
out.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in proposals),encoding="utf-8")
receipt={"reserved_ids":[r["original_requirement_id"] for r in proposals],"requirements":len(proposals),
    "subcomponents":sum(len(r["required_subcomponents"]) for r in proposals),"all_selected_live_anchors_unique":True,
    "original_wording_and_assessment_preserved":True,"sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
    "standing":"Root scope proposals for canonical integration by shard A; no manuscript changes or independent proof review."}
(DEST/"root-depth-proposals-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
