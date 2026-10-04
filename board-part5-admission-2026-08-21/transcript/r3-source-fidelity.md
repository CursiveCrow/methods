# Part V admission board — round 3 final source-fidelity verification

- seat: source-fidelity/evidence
- scope: frozen Part V reader body/annex plus the generated/registry/bibliography surfaces named in the focused brief
- independence: I did not read another Part V seat transcript
- boundary: read-only; no manuscript, source, provenance, control, registry, generated, or test edit; no build or test

## Closure-style Sigma-one proof — accept-fixed

The reciprocal theorem remains `proved=annex:p5.sigma.1` at `handbook/parts/p05/models-and-interpretability-supplement.tex:139-160`. The revised proof at `handbook/annex/p05/depth-completion-supplement.tex:18-222` now respects the actual closure-style `\Sigma^0_1` syntax rather than assuming an invalid dependency-free prenex conversion:

- it first proves primitive-recursive positive and negative Q proof construction for every closed bounded instance (`:26-76`);
- it states that the proof/substitution constructors are metalinguistic primitive-recursive functions and that displayed applications are eliminable graph abbreviations (`:78-115`);
- it recursively assigns a bounded evidence formula `E_phi` to bounded bases, conjunctions/disjunctions, unbounded and bounded existentials, and bounded universals (`:117-150`);
- for a bounded universal whose inner Sigma-one evidence depends on the bounded index, it stores the separately chosen evidence objects in one beta-coded finite sequence (`:136-154`), exactly avoiding the dependency defect;
- Q proves evidence implies the original formula, while PA proves existence of evidence from the formula; the only finite-choice step is displayed and proved by ordinary PA induction and beta extension (`:156-191`);
- the bounded evidence formula feeds the verified proof-code constructor, yielding the internal `sigma -> Prov_PA(sigma)` clause and the external true-Sigma-one-to-Q-provability clause (`:193-221`).

The proof uses exact `\mathcal N`, `\mathsf{Proof}_{\PA}`, and `\mathsf{Prov}_{\PA}` notation; all its cited internal dependencies resolve. Its body, annex, generated audit, and named-theorem index all report the same `proved` standing.

## Relation-first Rosser formula and notation — accept-fixed

`handbook/parts/p05/provability-logic-gl.tex:114-160` now separates metalinguistic code operations from object-language formulas. It defines primitive-recursive `\operatorname{ProofRel}_T`, total code-negation `\operatorname{NegCode}`, and the bounded primitive-recursive relation `\operatorname{RProofRel}_T` first (`:114-132`); then it chooses a Sigma-one representing formula `\mathsf{RProof}_T` and defines `\mathsf{RProv}_T` by existential closure (`:132-138`). No undeclared code function is used as a term of `\Lang_A`.

The more general strict/non-strict comparisons are described by their proof-code inequalities rather than assigning new unqualified `\prec` or `\preccurlyeq` roles (`:145-152`), so global elementary-substructure notation is not overloaded. Registry rows `handbook/registry/symbols.csv:60-62` give the metalinguistic relation/function, object-language representative, and Rosser-provability roles separately; all three appear identically on both generated symbol surfaces. The Guaspari--Solovay logic-R sentence remains explicitly a bibliographic pointer, not a new local calculus (`provability-logic-gl.tex:154-158`).

## Exact consistency and reverse-mathematics registry — accept-fixed

`handbook/registry/symbols.csv:63` now uses exact inherited `\bottom_A` in the `\mathsf{Con}(T)` definition. `\mathsf Z_2` is registered at `:424`, and the five standard subsystem rows are complete at `:425-430`. The registry contains 586 data rows; `handbook/generated/symbols-tables.tex` and `handbook/generated/symbol-index.tex` each contain all 586 corresponding stable IDs, with zero missing ID and zero duplicate. The corrected proof/Rosser/consistency/Z2 rows agree textually with the live definitions.

## Goodstein and hydra proof standing — accept-fixed

Goodstein termination remains honestly `cited=Goodstein1944` at `handbook/parts/p05/independence-catalog.tex:135-137`. The former body “Proof ... square” is now a `proofboundary` at `:139-160`: it fixes the ordinal assignment and load-bearing descent, explicitly enumerates the omitted recursive borrowing and well-foundedness details, and says those details remain in the cited sources. This is architecture, not a competing local proof, and therefore agrees with `cited=` under `handbook/CONVENTIONS.md:60-72`.

The hydra theorem has the same exact separation at `handbook/parts/p05/independence-catalog.tex:186-208`: the theorem is citation-backed; the boundary fixes the rank/decrease and recursive-strategy architecture, names the omitted node induction and calibration, and disclaims a second proof. The generated theorem index and Part V audit consequently report both theorems as cited and the two boundaries as definition-class entries.

## Live reachability-backed Part V register — accept-fixed

`handbook/parts/p05.tex:38-51` now routes a reader-facing theorem/definition register and explains the exact-source unlabeled-row convention before inputting `handbook/generated/audit-p05.tex`. The generator's live-graph routine at `tools/audit_tables.py:52-75,159-250` starts from `handbook/parts/p05.tex`, strips comments/verbatims, and recursively follows only reachable `\input` edges. The current table has 81 data rows (plus its two repeated longtable header rows), exactly the live theorem/definition-class environment count. It includes the repaired Sigma proof status, current GL/independence/reverse entries, and no retired `thm:p05-compactness-nonstandard` row. Exact inherited units without source-assigned labels are deliberately shown with an em dash rather than fabricated identities.

## GL sheet, citations, and exact-source hooks — accept-fixed

- The GL calculus sheet remains `sheet:hilbert-gl` at `handbook/registry/calculi/hilbert-gl.tex:2-7`; it now links the Part V arithmetical-realization definition, dictionary table, and Solovay theorem. The Part V GL definition links back to the sheet at `handbook/parts/p05/provability-logic-gl.tex:10-25`.
- All 31 distinct inline Part V citation keys resolve. The Guaspari--Solovay and Feferman--Vaught records retain exact author/title/container/volume/issue/pages/year/DOI roles, and all newly attached historical/method citations remain tied to concrete claims. No citation/source-role regression was found.
- The governed hooks at `handbook/parts/p05.tex:10-20,28-34` remain narrowly scoped and are removed immediately after their exact artifacts. Environment-order inspection places `thm:arithmetization-syntax` on the sole/first theorem in `inherited-09328-09438.tex` and `thm:theoremhood-undecidable` on the sole corollary in `inherited-09620-09728.tex`. Both identities occur in the generated named-result index with reader-source status; no inherited byte was edited.

## Frozen-source and static integration check

- All 19 inherited artifacts still match `source/formal-logic-reference.tex:9080-10059`: 19/19 records, 980/980 lines, zero mismatch, with unchanged one-time authority order.
- The current registry and both generated symbol surfaces are one-to-one across all 586 rows.
- The live Part V body/annex graph has no duplicate active identity. All 29 distinct references resolve when the calculus-sheet identity is included; all 31 inline citations resolve; and the sole `proved` body target has one reciprocal annex item with no orphan.
- No rendered OPEN/unadmitted/gate/internal-ID prose remains.
- F2 provenance/control admission and compilation, PDF navigation, visual inspection, human review, and final-user acceptance remain explicitly external and are not inferred from this source/content verdict.

accept
