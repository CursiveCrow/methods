"""Prepare current-writing proposals only; never edit a ledger or manuscript.

Root reviews and applies field-level JSON patches separately. A final pin is
permitted only after root reports canonical alias/migration completion.
Read extents below are human reading records, not deductions from file presence.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "oct3-fulfillment-proposals"
LEDGERS = ROOT / "spec/coverage/edition-2026/current-fulfillment"
START = "2026-10-03T07:31:18Z"
TARGETS = ["29.5"] + [f"75.{i}" for i in (2,3,4,6,7,8,9,10)]
TARGETS += [f"90.{i}" for i in range(1,8)] + [f"91.{i}" for i in range(1,9)]
TARGETS += [f"95.{i}" for i in range(1,4)] + [f"151.{i}" for i in range(1,5)]
TARGETS += [f"164.{i}" for i in range(4,7)]
TARGETS += [f"179.{i}" for i in (2,3,4,5,7,8,9)]
TARGETS += [f"186.{i}" for i in range(1,4)]
TARGETS += ["222.3","225.8"] + [f"248.{i}" for i in range(2,5)] + ["250.3"]
TARGETS += ["264.3","264.4"] + [f"265.{i}" for i in range(2,5)]
TARGETS += [f"266.{i}" for i in range(1,5)]

# Each profile is a bounded actual-reader observation, not a source closure.
# More profiles are added only after the specified intervals have been read.
PROFILES = [
    dict(sections=["29.5"], group="p03-imaginaries",
         files={"handbook/parts/p03/imaginaries-and-quotient-interpretations.tex":
                [(138,273),(316,345)]},
         supplied="Imaginary sorts, parameter fibers, canonical parameters, real/weak/uniform codes, selector conditions, and explicit unordered-pair and infinite-class failures are now written.",
         remaining=["Complete the separately allocated original Hodges1993 Chapters4/5 presentation and correction correspondence, including its broad interpretability, pseudo-elementary and totally-transcendental developments, remaining examples/exercises and original proof routes. The written quotient/code constructions do not establish elimination for every theory."]),
    dict(sections=["75.2","75.3","75.4","75.6","75.7","75.8","75.9","75.10"], group="p06-forcing",
         files={"handbook/parts/p06/forcing-recursion-and-truth.tex":
                [(70,89),(156,193),(214,280)],
                "handbook/parts/p06/boolean-valued-forcing-and-consistency.tex":
                [(72,107),(126,193)]},
         supplied="Current writing supplies named recursive forcing/name-evaluation results, density/truth and all-ZFC transfer statements with reciprocal proof items; the Boolean continuation supplies fullness, quotient truth, the cardinal-sized non-CH calculation and a metalogical bare-consistency bridge.",
         remaining=["Preserve and complete the separately allocated Cohen/Jech/Kunen/Bell presentations and distinct Scott–Solovay attribution/manifestation duties. The written transitive-ground kernel and arbitrary-model Boolean bridge are separate presentations; original clauses and proof routes are not discharged by their shared subjects.",
                    "Exact primitive-recursive/arithmetic proof-code translation, class forcing, iteration constructions and forcing-axiom consistency duties remain separate. Match nice-name/counting source components at their actual extents; the Boolean non-CH theorem does not by itself transcribe all those source constructions."]),
    dict(sections=[f"90.{i}" for i in range(1,8)], group="p07-hott",
         files={"handbook/parts/p07/hott-paths-and-equivalences.tex":[(1,434)]},
         supplied="Paths/J-built laws, transport/ap/apd, coherent equivalence and fiber bridges, homotopy levels and closures, declared funext/univalence computations, and typed Boolean/uniform-selector countercases are now written. The classical-principle discussion distinguishes type-level obstructions from mere-proposition principles.",
         remaining=["The complete HoTT2013 source allocation remains wider: natural-number encoding, algebraic-structure identity comparisons, later Chapter4/7 developments, remaining source exercises/universal properties and exact version/correction correspondence retain their duties.",
                    "Univalence and funext are explicit assumptions where used, not proved from Id/J; the complete original univalence-to-funext derivation remains a distinct dependency. No full infinity-groupoid semantics, all higher coherences, canonicity/normalization for added axioms, or complete mere-proposition excluded-middle/choice independence-model treatment is supplied."]),
    dict(sections=["91.1","91.2","91.3"], group="p07-hit",
         files={"handbook/parts/p07/higher-inductive-types.tex":[(14,414)]},
         supplied="Actual circle/interval/suspension/pushout/truncation/quotient and hub/spoke declarations, dependent eliminator data, judgmental-point versus propositional-path computations, coherent mapping claims and concrete countercases are now written.",
         remaining=["General n-truncation still requires the full loop-level characterization, sphere–loop adjunction and chosen fiber contractions/coherences. Circle encode–decode/loop-space and higher homotopy-group computations, torus comparison, source algebra/cell/flattening and impredicative quotient/resizing variants, remaining exercises and original qualifications remain owed.",
                    "HIT declarations are additional principles, not MLTT-only existence, general syntactic admissibility, normalization or canonicity proofs. Preserve the distinct computational cubical presentation."]),
    dict(sections=["95.1","95.2","95.3"], group="p07-proof-nets",
         files={"handbook/parts/p07/multiplicative-proof-nets.tex":[(17,375)],
                "handbook/parts/p07/girard-1987-trips-and-empires.tex":[(1,183)]},
         supplied="Occurrence/link graphs, sequent construction, switching and original long-trip criteria, worked separating networks, modern splitting/sequentialization, original seven-case empire/realization/splitting reconstruction, and unit-free graph cut contractions with reciprocal result items are now written.",
         remaining=["Original Girard CUT-marker trip preservation, cyclic-door box theorem, all PN1/PN2 unit/box/exponential/quantifier contraction cases, the exact unread Danos–Regnier1989 native presentation and distinct geometry-of-interaction/operator execution duties remain separate. A modern binary switching argument does not close those original variants."]),
    dict(sections=[f"151.{i}" for i in range(1,5)], group="p10-domains",
         files={"handbook/parts/p10/domain-theory-and-recursive-models.tex":
                [(1,102),(140,263),(307,371),(392,469)],
                "handbook/parts/p10/domain-recursion-and-invariance.tex":
                [(39,112),(317,417)]},
         supplied="Directed dcpo/Scott continuity/way-below bases, ideal completion/topology, typed function domains, least fixed points and failures, expanding-sequence bilimits/fold–unfold, and canonical invariance/initial-final/relational claims are now written at explicit map/variance hypotheses.",
         remaining=["Complete the corrected-expanded source's remaining Sections2/3 exercises, general directed-index/adjunction bilimits, L-domain/bifinite/FS/coherence hierarchy, equational theories, powerdomains, domain logic and further directions/apparatus. Source5 normal-form/conversion developments, unsupplied exercises and the four-parameter fixed-point relation-action lift remain separate.",
                    "Retain distinct printed1994/PostScript and Gunter/Scott/Mosses/Tennent/Wagner manifestations and source-native bridges, including actual operational adequacy/full-abstraction assumptions. A written corrected-author kernel is not whole167-page or whole-catalog completion."]),
]

PROFILES += [
    dict(sections=[f"91.{i}" for i in range(4,9)],group="p07-cchm2016",
         files={"handbook/parts/p07/cubical-type-theory-cchm2016.tex":[(1,571)],
                "handbook/registry/calculi/p07-cchm2016-cubical.tex":[(1,264)]},
         supplied="The actual original-v1 de Morgan interval, face lattice/substitutions, path syntax, composition/filling/transport clauses, corrected Glue algorithm, constructed line equivalence and universe composition, presheaf meaning and exact computational theorem boundary are written; the routed76-entry rule sheet and eight local proof items are present.",
         remaining=["Complete the transport/eqToPath comparison, two-dimensional Glue coherence and full equivalence-data coherence needed for local univalence; the typed Glue path and unglue equivalence alone are not that proof.",
                    "Supply all semantic interpretation/substitution/naturality/soundness and composition-uniformity cases, singular-set uniformity, and the exact CCHM2016v1 identity/circle/truncation extensions. The separate Huber1607.04156v1 typed-operational/computability canonicity proof remains unread/unreconstructed; no normalization theorem follows from the sheet."]),
    dict(sections=["164.4"],group="p15-popper",
         files={"handbook/parts/p15/popper-hypothetico-deductive-reasoning.tex":[(53,126),(286,375)]},
         supplied="A conditional test package, explicit premise-isolation/nonentailment claims, worked thread test, corroboration/probability distinction, chance-law countercase and criticism method are written.",
         remaining=["The complete allocated Musgrave2011 HHL10 pp205–234 presentation remains distinct and still requires its actual argument/examples/objections/replies. Popper's source-specific probability/quantum treatments, later-note/addendum distinctions and other original scope are not discharged by the bounded2002-source test reconstruction."]),
    dict(sections=["164.5"],group="p15-hempel",
         files={"handbook/parts/p15/hempel-confirmation-and-paradoxes.tex":[(25,70),(221,279),(448,462)]},
         supplied="Actual observation/hypothesis language, Nicod/unary stipulations, Hempel adequacy conditions, closure-collapse and joint-consistency claims with reciprocal proof items and declared acceptance limits are written.",
         remaining=["Complete/match the entire selected Sprenger2011 historical argument separately from the1945 original-article reconstruction. Hempel's complete1943 technical construction, remaining source-specific proof/example/qualification duties, quantitative and projectibility/acceptance presentations remain distinct; no probability or experimental reliability is inferred from the logical conditions."]),
    dict(sections=["164.6"],group="p15-carnap",
         files={"handbook/parts/p15/carnap-logical-probability-and-induction.tex":[(39,115),(168,224),(559,583)],
                "handbook/parts/p15/carnap-confirmation-relevance-and-reliability.tex":[(115,176),(419,468),(678,697)]},
         supplied="The1950 finite state/structure distinction, equal-structure c-star construction and worked equal-state contrast, signed relevance/conditioning requirements and general-estimation framework are written, with explicit infinite-language/source limits.",
         remaining=["For arbitrary general sentences, construct the original infinite-system limits, full logical transfer/effective evaluation and quantitative-language confirmation function; comparative vindication and general variety-of-instances claims are not supplied by finite definitions.",
                    "Retain and complete remaining whole1950-book/history proof dependencies: sufficientness, infinite deFinetti/representation, Hintikka–Niiniluoto and mixture/species-sampling/finite-approximation arguments. Resolve the history copy's2009 footer versus the allocated2011 chapter and keep1952/1962 variants distinct."]),
    dict(sections=[f"179.{i}" for i in (2,3,4,5,7,8,9)],group="p16-best-explanation",
         files={"handbook/parts/p16/inference-to-best-explanation.tex":[(23,263),(330,488)]},
         supplied="Actual considered-alternative/agnosticism, loveliness–likeliness, contrastive-causal/correspondence arguments, worked raven sampling distinction, bad-lot/background replies, prediction/accommodation/selection and defeater appraisal are now written.",
         remaining=["The complete selected Lipton2004 second-edition book or other exact allocated Lipton/HHL presentation remains a separate full-source argument/example/qualification duty. The related Companion2000 and1993/1998 articles, bounded2004 raven pages and editorial Bayesian/causal calculations do not discharge the full book or every original chapter.",
                    "Explanatory virtue-to-truth warrant, exhaustive candidate generation and the source's complete responses/limits are not proved by a stipulated ranking or posterior formula. Preserve source-native causal/contrastive and sampling distinctions rather than hybridize them."]),
    dict(sections=["186.1","186.2","186.3"],group="p16-qualitative-models",
         files={"handbook/parts/p16/qualitative-process-and-model-reasoning.tex":[(22,33),(72,114),(221,267),(401,418)]},
         supplied="A set-valued sign abstraction, actual QPT participant/precondition/quantity-condition/direct-influence mechanism and heat-flow case, and source two-pass fragment/assumption/nogood/query model formulation with restrictions are now written.",
         remaining=["Complete the selected full Forbus/QPT/qualitative-modeling source families at their actual versions, including all field/spatial/kinematic/liquid theories, propagation/simulation/filter extended-endpoint cases, global realizability/guaranteed-coverage proofs, abstraction/multiple-model arguments and apparatus. Local sign operations and finite pruning are not the full QSIM theorem or unrestricted model-formulation algorithm."]),
    dict(sections=["222.3"],group="p19-spatial-updating",
         files={"handbook/parts/p19/spatial-orientation-and-updating.tex":[(1,259),(394,428)]},
         supplied="Orientation/updating/reorientation and egocentric/allocentric distinctions, turn-versus-translation worked cases, actual movement/imagined-heading evidence and virtual-room geometry alternatives are written with task/population/denominator/uncertainty limits.",
         remaining=["Acquire/read and reconstruct the complete Hegarty–Stull2012 Oxford Chapter31 pp606–630, including all source-native mechanisms/tasks, figures/notes/references and retained components. These three bounded primary-study records do not replace that synthesis; author-versus-final Shusterman protocol/numerical discrepancies remain version-qualified."]),
    dict(sections=["225.8"],group="p19-motivated-reasoning",
         files={"handbook/parts/p19/motivated-reasoning-and-goals.tex":[(1,167),(228,318)]},
         supplied="Actual directional/accuracy/closure/strategy distinctions, Wason desired-conclusion evidence, seizing/freezing theory and worked commitment contrast, and capacity/resource/strategy limits are written with specified study scope.",
         remaining=["The complete allocated Molden–Higgins2012 Oxford Chapter20 remains unheld/unreconstructed beyond public metadata. Its complete argument, reviewed studies, figures, notes and references are not discharged by the separately attributed Wason/closure/regulatory-focus experiments or conceptual comparisons. No common dataset, meta-analysis, universal mechanism or normative debiasing prescription is supplied."]),
    dict(sections=["248.2","248.3","248.4"],group="p12-cdcl-uip",
         files={"handbook/parts/p12/cdcl-uip-and-watched-literals.tex":[(91,385)]},
         supplied="Actual reverse-trail first-UIP construction and native conflict traces, full watched-literal event/update/rollback conditions and failure case, general search loop/liveness policies and separately attributed activity/look-ahead/restart/deletion mechanisms are written with reciprocal result items.",
         remaining=["The exact final GRASP1999, original MiniSat2004 versus extended1.2, final2009 versus manuscript and complete2021 CDCL/branching/look-ahead source allocations retain their acquisition/version/reconstruction duties. No arbitrary-restart/forgetting termination, implementation floating-point/performance guarantee, or extended/incremental constraint-API correctness follows from the declared plain-CNF core."]),
    dict(sections=["250.3"],group="p12-drat-checking",
         files={"handbook/parts/p12/drat-certificates-and-checking.tex":[(1,60),(116,290),(370,469)]},
         supplied="Finite-CNF/RUP/RAT semantics, exact pivot-retaining test and model repair, complete forward trace-checking method and soundness claim, dated format/deletion variants and executable/encoding trust boundaries are written with reciprocal proof text.",
         remaining=["The optimized executable DRAT-trim/parser/runtime correspondence and every relevant encoding implication remain distinct from mathematical checker soundness. Complete SAT Handbook2021 Chapter15 and its author/final-galley relation, full LRAT/FRAT constructions/pipelines and counting/optimization/QBF preservation conditions remain separate source duties."]),
    dict(sections=["264.3","264.4"],group="p13-greek-originals",
         files={"handbook/parts/p13/presentations/src063-0103.tex":[(136,269)],
                "handbook/parts/p13/presentations/src063-0104.tex":[(84,391)]},
         supplied="Actual Boger predicate-first grammar, meaning/nonexistence interpretation and guarded modern bridge, Johnson subject-first assertoric mood/rejection/contrasted-instance machinery, modal matrices/translations and finite countercases are written; historical and modern reconstructions remain distinguished.",
         remaining=["Complete/match the rest of the retained Greek original-source allocation, including clipped Boger table/source intervals and unadopted categorical proof/reduction cases. Johnson's McCall/contingency/implication third approach and exact original Greek/source correspondences require their own read/match; active later authoring is not credited in this B3/B4 observation. The written matrices/countermodels do not establish unique historical adequacy or whole-source closure."]),
    dict(sections=["265.2","265.3","265.4"],group="p13-indian-logic",
         files={"handbook/parts/p13/nyaya-sutra-inference-and-debate.tex":[(1,547)]},
         supplied="The unchanged fully read1913 BookI translation treatment supplies sixteen categories, knowledge sources, five-member arguments and actual reasons/examples, pervasion failures, debate/cavil/quibble cases and translation-versus-commentary/modern-correction boundaries.",
         remaining=["The complete allocated Ganeri2004 HHL1 Indian-logic chapter remains unheld/unreconstructed. The distinct Gotama/Vidyabhusana1913 primary treatment cannot discharge that source, the wider Buddhist/Jaina doctrines, other original editions/translations, or corrupt/unread Sanskrit; source-native comparative historical scope remains owed."]),
    dict(sections=["266.1","266.2","266.3","266.4"],group="p13-arabic",
         files={"handbook/parts/p13/presentations/src063-0107.tex":[(55,158)],
                "handbook/parts/p13/presentations/src063-0108.tex":[(50,108),(175,228)],
                "handbook/parts/p13/presentations/src063-0107-original-2004.tex":[(12,92),(179,248),(507,526)],
                "handbook/parts/p13/presentations/src063-0108-original-2004.tex":[(71,175),(201,248)]},
         supplied="Both prior2005 supplements and newly recovered2004 Street/Burnett presentations contain substantive doctrinal disputes, temporality/conversion/meaning distinctions, actual Latin lexical/truth-bearer and audience/curricular transmission arguments, qualified inventories and source limitations.",
         remaining=["Do not retain the obsolete claim that the published2004 chapters are unavailable: author acquisition/reading has changed. Reconcile Street's four-versus-three mode group, item14 temporal-caption mismatch, item19 contradictory rendition, subject-existence conditions and the needed Rescher/vanderNat1974 source; supply historically qualified modal proof routes rather than treat the26 renditions as Avicenna's complete calculus.",
                    "Underlying medieval Arabic/Latin editions/witnesses and semantic transmission comparisons retain their own uninspected scope; a qualified2004 historical reconstruction does not verify every manuscript attribution or every translation. Keep2004 originals,2005 supplements and materially different author-manuscript/source variants distinct, with all retained original-source facets owed."]),
]

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")

def dump(path: Path, data) -> None:
    if path.parent.resolve() != OUT.resolve():
        raise ValueError("Output outside owned proposal directory")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

def small_operation_patches(section, common, operations):
    """Emit ordered field-level chunks, excluding the immutable facet array."""
    batches=[]; current=[]
    def size(ops):
        return len(json.dumps(dict(common,operations=ops),ensure_ascii=False,indent=2).encode("utf-8"))
    for operation in operations:
        if current and size(current+[operation])>7500:
            batches.append(current); current=[]
        if size([operation])>7800:
            raise ValueError(("Single field operation exceeds small-patch bound",section,operation["path"]))
        current.append(operation)
    if current: batches.append(current)
    names=[]
    for number,batch in enumerate(batches,1):
        name=f"row-{section}-step-{number:02d}.jsonpatch"
        payload=dict(common,step=number,total_steps=len(batches),
                     requires_prior_steps=names.copy(),
                     original_hash_is_pre_sequence_pin=True,operations=batch)
        dump(OUT/name,payload);names.append(name)
    return names

def manifests():
    groups = []
    for number in (3,4):
        path=ROOT/f"spec/research/edition-2026-authoring-batch-intake-{number}.json"
        groups.extend(json.loads(read(path))["groups"])
    groups.extend([
        dict(stem="p07-girard-empires",
             bodies=["parts/p07/girard-1987-trips-and-empires.tex"],
             annex="annex/p07/girard-1987-trips-and-empires.tex",
             note="spec/research/edition-2026-p07-proof-nets.md"),
        dict(stem="p10-domain-invariance",
             bodies=["parts/p10/domain-recursion-and-invariance.tex"],
             annex="annex/p10/domain-recursion-and-invariance.tex",
             note="spec/research/edition-2026-p10-domain-theory.md"),
    ])
    return groups

def route_trace():
    """Literal input graph only: no TeX execution or conditional interpretation."""
    base=ROOT/"handbook"; visited=set(); frontier=["main.tex"]
    snapshots={}
    while frontier:
        rel=frontier.pop()
        if rel in visited: continue
        visited.add(rel); path=base/rel
        if not path.is_file(): continue
        raw=path.read_bytes(); text=raw.decode("utf-8-sig")
        snapshots["handbook/"+rel]=sha_bytes(raw)
        clean=re.sub(r"(?m)(?<!\\)%.*$", "", text)
        for command, arg in re.findall(r"\\(input|include|showcalculus)\s*\{([^{}]+)\}",clean):
            if "\\" in arg: continue
            child=("registry/calculi/"+arg if command=="showcalculus" else arg)
            if not child.endswith(".tex"): child+=".tex"
            frontier.append(child)
    return snapshots

def evidence(path: str, intervals, routes):
    raw=(ROOT/path).read_bytes(); lines=raw.decode("utf-8-sig").splitlines()
    result=[]
    for start,end in intervals:
        if not 1 <= start <= end <= len(lines):
            raise ValueError((path,start,end,len(lines)))
        snippet="\n".join(lines[start-1:end])
        anchors=re.findall(r"\\label\{([^{}]+)\}|\\begin\{hb(?:definition|convention|theorem|lemma|corollary|method|example|warning)\}\{([^{}]+)\}|\\begin\{proofboundary\}\{([^{}]+)\}",snippet)
        labels=[next(a for a in xs if a) for xs in anchors]
        labels += re.findall(r"\\(?:calculussheet|hbrule)\{([^{}]+)\}",snippet)
        result.append(dict(path=path,anchor=labels[0] if labels else None,
                           anchors=labels,line_start=start,line_end=end,
                           read_extent=f"Complete actual current-reader interval lines{start}–{end} read for authored content and stated scope; not a proof-correctness or complete-primary-source review.",
                           route_state=("on_current_literal_recursive_input_trace" if path in routes else "root_reported_routed_literal_trace_unresolved"),
                           sha256=sha_bytes(raw)))
    return result

def proof_inventory(groups):
    records=[]
    for group in groups:
        for rel in [group.get("annex")]+group.get("annexes",[]):
            if not rel: continue
            path="handbook/"+rel; raw=(ROOT/path).read_bytes()
            text=raw.decode("utf-8-sig")
            declarations=re.findall(r"\\begin\{annexitem\}\s*\{([^{}]+)\}\s*\{([^{}]+)\}",text)
            records.append(dict(group=group["stem"],path=path,sha256=sha_bytes(raw),
                                item_declarations=[dict(anchor=a,body_backref=b) for a,b in declarations],
                                proof_environment_count=text.count(r"\begin{proof}"),
                                read_extent="Actual declaration/markup inventory only. Full proof arguments not independently read or evaluated in this reconciliation.",
                                standing="Proof-text presence, not mathematical completeness, correctness or admission."))
    return records

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aliases-confirmed",action="store_true",
                        help="Use only after root explicitly reports canonical aliases/migrations applied.")
    args=parser.parse_args()
    OUT.mkdir(exist_ok=True)
    snapshots={p.name:sha_bytes(p.read_bytes()) for p in LEDGERS.glob("*.jsonl")}
    routes=route_trace(); groups=manifests()
    by_section={}
    for profile in PROFILES:
        for section in profile["sections"]:
            if section in by_section: raise ValueError("Overlapping profile "+section)
            by_section[section]=profile
    proposals=[]; untouched=[]
    for path in sorted(LEDGERS.glob("*.jsonl")):
        for line_number, raw in enumerate(read(path).splitlines(),1):
            old=json.loads(raw); section=old.get("section_id")
            if section not in TARGETS: continue
            if section not in by_section:
                untouched.append(dict(section_id=section,status=old["status"],reason="Target awaiting actual interval read/match; no file-existence credit."))
                continue
            profile=by_section[section]; new=copy.deepcopy(old)
            current=[]
            for body,intervals in profile["files"].items():
                current.extend(evidence(body,intervals,routes))
            new["status"]=("partial" if old["status"] in {"missing","unassessed"} else old["status"])
            new["reader_evidence"]=copy.deepcopy(old.get("reader_evidence",[]))+current
            new["missing_pieces"]=profile["remaining"]
            wider_candidates=[
                scope for scope in old.get("unassessed_scope",[])
                if any(marker in scope for marker in (
                    "Additional routed candidates", "Uninspected current-reader extents",
                    "Actual neighboring current reader locator", "that full cross-part body"))
            ]
            new["unassessed_scope"]=[
                "Original source/variant/proof obligations outside the explicitly read current-reader intervals remain unassessed. This author-side writing reconciliation is not correctness, primary-source admission or publication acceptance."
            ]+wider_candidates
            # Original wider candidates remain owed, with exact old payload retained.
            new["reader_adoption_qualification"]={
                "standing":"Author-side current-writing qualification only; not independent correctness, source or publication acceptance.",
                "observed_scope":profile["supplied"],
                "historical_remaining_payload":{k:copy.deepcopy(old.get(k,[])) for k in ("missing_pieces","unassessed_scope")},
                "historical_status":old["status"],
                "source_facets_preserved_unchanged":True,
                "whole_source_discharge":False,
                "proof_standing":"Declared result and reciprocal proof-text presence only; no independent correctness review.",
                "canonical_aliases_confirmed_by_root":args.aliases_confirmed,
                "started_utc":START,
            }
            new["observed_utc"]=datetime.now(timezone.utc).isoformat()
            if new["source_facets"]!=old["source_facets"]:
                raise ValueError("Source facet mutation")
            changes={k:v for k,v in new.items() if old.get(k)!=v}
            proposal=dict(section_id=section,shard=path.name,ledger_line=line_number,
                          original_row_sha256=sha_bytes(raw.encode()),
                          source_facet_ids=[x["unit_id"] for x in old["source_facets"]],
                          before=old,after=new,field_changes=changes)
            proposals.append(proposal)
            # A small field-level patch never repeats or rewrites source facets.
            operations=[dict(op="test",path="/section_id",value=section)]
            for key,value in changes.items():
                if key=="reader_evidence":
                    if "reader_evidence" not in old:
                        operations.append(dict(op="add",path="/reader_evidence",value=[]))
                    operations.extend(dict(op="add",path="/reader_evidence/-",value=item) for item in current)
                else:
                    operations.append(dict(op="replace" if key in old else "add",path="/"+key,value=value))
            common=dict(section_id=section,shard=path.name,ledger_line=line_number,
                       original_row_sha256=proposal["original_row_sha256"],
                       format="RFC6902 operations against the parsed single JSONL row; root applies separately",
                       final_pins=args.aliases_confirmed)
            proposal["small_patch_files"]=small_operation_patches(section,common,operations)
    manifest=dict(standing="PROPOSALS ONLY; root reviews/applies separately",final_pins=args.aliases_confirmed,
                  target_sections=TARGETS,proposal_sections=[x["section_id"] for x in proposals],
                  active_patch_files=[name for row in proposals for name in row["small_patch_files"]],
                  expected_row_hashes={x["section_id"]:x["original_row_sha256"] for x in proposals},
                  immutable_source_facet_occurrences=sum(len(x["source_facet_ids"]) for x in proposals),
                  source_facet_ids=sorted({uid for x in proposals for uid in x["source_facet_ids"]}),
                  excluded_outputs="Unlisted earlier-stage files are not an active adoption sequence.",
                  scope=dict(parts=19,chapters=289,main_sections=2475,original_requirements=615),
                  note="No source-reading, proof-correctness, independent admission or publication credit.")
    dump(OUT/"active-manifest.json",manifest)
    dump(OUT/"proposals.json",dict(standing="PROPOSALS ONLY",final_pins=args.aliases_confirmed,
                                  observed_utc=datetime.now(timezone.utc).isoformat(),
                                  ledger_sha256=snapshots,route_sha256=routes,
                                  canonical_alias_pins={rel:sha_bytes((ROOT/rel).read_bytes()) for rel in
                                      ("handbook/bib/handbook.bib","handbook/registry/symbols.csv","handbook/registry/symbol-scopes.json")},
                                  target_count=len(TARGETS),proposal_count=len(proposals),
                                  proposals=proposals,unchanged_unread_targets=untouched,
                                  proof_presence_inventory=proof_inventory(groups)))
    if snapshots!={p.name:sha_bytes(p.read_bytes()) for p in LEDGERS.glob("*.jsonl")}:
        raise RuntimeError("Ledger changed concurrently; regenerate pins before adoption")
    print(json.dumps(dict(proposals=len(proposals),unread_targets=len(untouched),
                          final_pins=args.aliases_confirmed,ledgers_modified=False),indent=2))

if __name__=="__main__":
    main()
