"""Record bounded source overlap for the eleven selected practical/scientific additions."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CAT = HERE.parent

def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]

paths = [CAT / "sources-001-036/SRC-036-content-units-v2.jsonl", CAT / "sources-001-036/SRC-036-additional-presentation-units-v3.jsonl"]
paths += [CAT / f"sources-037-068/src{n:03}-content-units.jsonl" for n in [42,57,58,59,60,61,62]]
paths += [CAT / x for x in ["current-reasoning-units.jsonl", "benchmark-content-units.jsonl", "additional-method-units.jsonl", "requirements-units.jsonl"]]
units = {}
for path in paths:
    for unit in rows(path):
        if unit["unit_id"] in units:
            raise ValueError("Unresolved same-ID overlay: " + unit["unit_id"])
        units[unit["unit_id"]] = {"path": path.relative_to(ROOT).as_posix(), "unit": unit}

selected = [(HERE / "practical.jsonl", r) for r in rows(HERE / "practical.jsonl") if r.get("inclusion_decision") == "add_finite_source_treatment"]
selected += [(HERE / "scientific.jsonl", r) for r in rows(HERE / "scientific.jsonl")[:8] if r.get("proposed_unit_id")]
assert len(selected) == 11

# Every relation below is a semantic allocation decision, not a keyword join.
# Related full source chapters remain owed independently. No relation accepts a proof.
decisions = {
"ED26-P12-PRACT-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-025", "partial_scope", "Chapter25 already maps task/problem-solving methods, knowledge roles and specification languages. This overlaps problem specification/decomposition at a method level, but it is Schreiber's knowledge-engineering presentation, not the selected Pólya2004 entries or their backward/forward implication discipline."),
  ("ED26-SRC-036-027", "distinct_source_presentation", "The separate18-page Knowledge Engineering author draft retains its problem-solving-method typology and examples. Keep it distinct from the2008chapter and from Pólya."),
  ("ED26-SRC-060-0011", "shared_subject", "Practical-reasoning systems, goals, agency and resource-sensitive reasoning are already fully allocated. The Gabbay–Woods2002survey does not establish identity with Pólya's selected problem-transformation presentation."),
  ("ED26-SRC-059-0010", "shared_subject", "Resolution-based logic-program execution already supplies a formal backward-search setting. It does not replace Pólya's heuristic generation, side-condition retention and reconstruction of a forward justification.")],
 "rationale": "Retain the Pólya source-specific unit, connect the existing method and backward-search treatments, and avoid saying problem decomposition or backward reasoning as a whole is absent."},
"ED26-P12-PRACT-002": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-004", "partial_scope", "Chapter4 explicitly allocates propagation, backtracking/local search/hybrids, optimization search and inference. Search procedures are already in scope; this is not evidence that the1985Dechter–Pearl equal-information optimality presentation has been supplied."),
  ("ED26-SRC-036-022", "partial_scope", "Chapter22 already allocates plans/executions, strong and strong-cyclic planning and technology. The selected A* state-cost/reopening/expansion comparisons are a separately identified source treatment."),
  ("ED26-SRC-057-0005", "partial_scope", "Explicit-State Model Checking already maps successor exploration, search/storage/counterexample reconstruction and exhaustive-guarantee boundaries. These overlap search objects and exploration policy, but model-checking counterexamples are not automatically least-cost solutions with A* admissibility and four computational optimality types."),
  ("ED26-SRC-057-0027", "shared_subject", "Graph-game strategies and reactive synthesis already map algorithmic solution construction; adversarial winning strategies are different solution objects from the selected single-agent cost-search presentation.")],
 "rationale": "Qualify the old absent_from_catalog observation. General search and guarantee analysis are already mapped. Retain Dechter–Pearl1985as a distinct complete presentation with its exact solution/expansion optimality restrictions; no duplicate exact source treatment was established."},
"ED26-P17-PRACT-003": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-022", "partial_scope", "The actual chapter components name state/goal plans, strong/strong-cyclic/full-observation, temporally extended goals, conformant and partial-observation planning. They overlap plan existence but do not identify Erol–Hendler–Nau1996method-constrained task-network derivation and its restriction/complexity proofs."),
  ("ED26-SRC-036-025", "shared_subject", "Knowledge-engineering task/problem-solving method descriptions concern task decomposition, but do not establish the specific HTN reduction semantics and1996plan-existence theorem package."),
  ("ED26-SRC-060-0011", "shared_subject", "Agency/goals/resources and formal practical reasoning are already allocated. Preserve their broader arguments without treating them as the selected HTN syntax, reduction relation and complexity classification."),
  ("ED26-SRC-057-0027", "shared_subject", "Strategy existence in reactive graph games has explicit adversarial/environment semantics. It is not identical to method-constrained finite HTN plan derivability."),
  ("ED26-SRC-058-0016", "shared_subject", "Action refinement is already a source treatment in process algebra. Refinement semantics and HTN method decomposition share a structural idea but have different languages, solution relations and proof obligations.")],
 "rationale": "Retain the exact1996HTN source presentation and link existing planning/refinement coverage. Do not claim automated planning or hierarchical decomposition generally absent; do not equate an older chapter mention with the complete selected source proof."},
"ED26-SCI-JCGM2008-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-014", "shared_subject", "Physical reasoning already maps component/process models, rigid mechanics/liquids and abstraction across models. These are related model-construction treatments, but they do not identify JCGM2008measurand, TypeA/TypeB, covariance propagation and coverage-factor procedures."),
  ("ED26-SRC-060-0009", "shared_subject", "Probability logic already addresses event/statement assignments and coherence. Measurement uncertainty evaluation is a different source-specific inferential procedure, not simply a probability-logic axiom.")],
 "rationale": "Retain the selected GUM procedure. Reuse already mapped variance/conditional-expectation prerequisites and distinguish its metrological source conventions from physical-model and probability-logic treatments."},
"ED26-SCI-Mahajan2014-001": {
 "classification": "source_specific_treatment_not_identified_in_checked_sets", "relations": [
  ("ED26-SRC-036-014", "shared_subject", "Physical reasoning has complete source domain theories and abstraction/multiple-model components. This establishes existing quantitative/physical reasoning scope, but its component map does not identify Mahajan's dimension-matrix nullspace/scaling procedure or the selected2014chapters.")],
 "rationale": "Keep the absence claim restricted to the selected explicit dimensional/scaling treatment in the checked sets. Retain Mahajan2014and its unit/rank/omitted-variable limits; do not call all physical reasoning absent or infer that no historical chapter mentions dimensions."},
"ED26-SCI-Mahajan2014-002": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-014", "partial_scope", "Abstraction and multiple models are explicitly mapped in14.3. They share controlled simplification and regime reasoning, while Mahajan's selected lumping/easy-case constructions and the separately labelled error-bound example remain distinct."),
  ("ED26-SRC-057-0005", "shared_subject", "Explicit-state search maps approximations and the survival of exhaustive guarantees. Its approximation is a verification/search procedure, not automatically a real-valued asymptotic estimate."),
  ("ED26-SRC-057-0013", "shared_subject", "Property-preserving abstraction/refinement maps simulation relations and spurious counterexamples. These are not numeric approximation-error intervals or uniform asymptotic claims.")],
 "rationale": "Qualify absent_from_catalog: approximation and abstraction have existing source obligations. Retain the distinct Mahajan numerical/regime inference treatment and distinguish its heuristic examples from formal abstraction guarantees."},
"ED26-SCI-GoldbergOracle-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-042-0109", "partial_scope", "The captured SMT-LIB FloatingPoint theory already maps exact sorts, value encodings, rounding modes, operations, exceptional values and the complete declaration/model conditions in21components. It overlaps representable values and operation semantics. It does not replace the selected Goldberg/OracleD.3rounding-error, guard-digit, cancellation and stability proofs or their D.6dependencies."),
  ("ED26-SRC-042-0107", "shared_subject", "FixedSizeBitVectors gives formal finite-width bit operations; bit-vector encoding is related representation infrastructure, not proof of a numerical conditioning or rounding-error bound."),
  ("ED26-SRC-057-0011", "shared_subject", "SMT methods are already mapped for formula satisfaction and theory solving. Proving a machine-arithmetic formula needs the correct theory and does not automatically justify a real-number approximation claim.")],
 "rationale": "The unqualified absence label must be revised: floating-point formal semantics is already catalogued. Retain Goldberg/Oracle as a distinct numerical-analysis source treatment; connect exact operation semantics to the separate error-bound argument."},
"ED26-SCI-SaltelliAnnoni2010-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-011", "partial_scope", "Bayesian Networks already allocates exact and approximate inference, stochastic sampling, engineering/learning and causal intervention. These overlap uncertain model inputs/inference but do not supply the selected OAT criticism and first-order/total variance sensitivity indices."),
  ("ED26-SRC-036-014", "shared_subject", "Abstraction and multiple physical models offer a related model-dependence context. They do not establish the specific Saltelli–Annoni2010global-sensitivity source treatment.")],
 "rationale": "Retain the2010source and explicit independence/distribution assumptions for variance-based indices; reuse existing variance and model uncertainty prerequisites without claiming sensitivity analysis follows merely from sampling."},
"ED26-SCI-GelmanMengStern1996-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-011", "partial_scope", "Bayesian Networks maps inference, approximation and model construction/learning. Posterior predictive realized-discrepancy checks are not identical to posterior prediction, fitting or a marginal-likelihood comparison."),
  ("ED26-SRC-057-0001", "shared_subject", "The existing Handbook of Model Checking concerns formal state-system property satisfaction. The phrase model checking does not make that source a duplicate of statistical posterior predictive model criticism."),
  ("ED26-SRC-060-0009", "shared_subject", "Probability logic concerns probability assignments and coherence, not the selected1996replication/discrepancy construction and its reference distribution.")],
 "rationale": "Retain the1996main-article presentation with its comment/rejoinder boundaries. Link existing prediction/inference content and distinguish statistical model criticism from formal verification."},
"ED26-SCI-NASA7009B2024-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-057-0003", "partial_scope", "Modeling for Verification explicitly maps abstraction into verification models, environment assumptions/model correspondence and properties preserved or lost. These overlap the model/implementation/claim distinction but do not supply NASA7009B's particular empirical validation, data pedigree and intended-use procedure."),
  ("ED26-SRC-057-0013", "shared_subject", "Simulation guarantees in abstraction/refinement are formal relational preservation results; they are not repeated numerical simulation runs or empirical validation against a physical target."),
  ("ED26-SRC-057-0019", "shared_subject", "Combining model checking and testing is a separate formal/software assurance source presentation; retain it while attributing NASA's numerical-model validation criteria only to the selected2024standard."),
  ("ED26-SRC-036-014", "partial_scope", "Physical-model architectures, domain theories and abstraction are already mapped. The proposed contribution is the explicit warrant from an implemented simulation to a target claim, under the selected validation/use-domain conditions.")],
 "rationale": "Retain a bounded attributed methodology, not a new universal theorem or mandatory handbook process. Avoid claiming modeling/verification or all simulation-related reasoning absent."},
"ED26-SCI-NIST2012-001": {
 "classification": "insufficient_scope", "relations": [
  ("ED26-SRC-036-011", "shared_subject", "Causal intervention is already mapped in Bayesian Networks11.6. Intervention semantics alone does not determine factorial design rank, contrast estimability, blocking or alias structure."),
  ("ED26-SRC-060-0003", "shared_subject", "The induction chapter already maps sample projection and limits of nondeductive support. It is not the selected design-matrix/aliasing procedure in the2012NISTsource.")],
 "rationale": "Retain and extend the existing P19factorial example rather than claim factorial reasoning absent. The NISTunit adds explicit contrasts, replication/blocking and estimability/aliasing with source-specific design assumptions."}
}

output = []
for original_path, original in selected:
    uid = original.get("proposed_unit_id") or original["unit_id"]
    decision = decisions[uid]
    relations = []
    for existing_id, relation, rationale in decision["relations"]:
        entry = units[existing_id]
        existing = entry["unit"]
        relations.append({"existing_unit_id": existing_id, "relationship": relation, "rationale": rationale, "evidence_path": entry["path"], "existing_title": existing["title"], "source_presentations": existing.get("source_presentations", []), "component_evidence": [{"component_id": c["component_id"], "description": c["description"]} for c in existing.get("required_components", [])]})
    previous = original.get("related_existing_unit_ids", original.get("existing_mapped_unit_ids", []))
    for existing_id in previous:
        if existing_id not in units:
            raise ValueError("Unbound original overlap ID: " + existing_id)
    output.append({"unit_id": uid, "title": original["title"], "assessed_at": "2026-09-09", "mapping_state": "resolved", "original_observation_preserved": {"path": original_path.relative_to(ROOT).as_posix(), "row_id": original.get("finding_id", original.get("gap_id")), "classification": original["classification"], "gap_finding": original.get("gap_finding"), "findings": original.get("evidence", {}).get("findings", []) if isinstance(original.get("evidence"), dict) else [], "original_related_unit_ids": previous, "source_file_sha256": hashlib.sha256(original_path.read_bytes()).hexdigest()}, "reconciled_classification": decision["classification"], "existing_unit_ids": list(dict.fromkeys(previous + [r[0] for r in decision["relations"]])), "relationships": relations, "exact_duplicate_source_presentation_established": False, "allocation_decision": "retain_distinct_source_presentation_and_link_existing_scope", "rationale": decision["rationale"], "scope_bound": "Compared the selected source identities and components with the explicit checked chapter/declaration records. Complete chapter obligations include their source text, but no claim is made that an unread chapter never mentions a selected subject or citation. Shared subject and partial overlap do not prove source identity or discharge a selected proof.", "checked_source_unit_paths": [p.relative_to(ROOT).as_posix() for p in paths], "original_gap_files_modified": False, "manuscript_acceptance_inferred": False, "unresolved_questions": []})

target = HERE / "selected-source-overlaps.jsonl"
if target.exists():
    raise SystemExit("Refusing to overwrite published overlap records")
target.write_text("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in output), encoding="utf-8")
receipt = {"units": len(output), "source_relations": sum(len(r["relationships"]) for r in output), "exact_source_duplicates_established": 0, "new_units_retained_as_distinct_presentations": len(output), "old_absence_labels_qualified": [r["unit_id"] for r in output if r["original_observation_preserved"]["classification"] == "absent_from_catalog"], "sha256": hashlib.sha256(target.read_bytes()).hexdigest(), "input_hashes": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths + [HERE / "practical.jsonl", HERE / "scientific.jsonl"]}}
(HERE / "selected-source-overlaps-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
