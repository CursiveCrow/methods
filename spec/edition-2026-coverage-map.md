# The Methods of Reason: scope and coverage map

Construction completed: 2026-09-09T16:21:25.492426+00:00.

The edition is a CRC-style reference handbook of logic and reasoning. Its entries support subject lookup and reasoning-task lookup, with explicit assumptions, methods, results, required proofs or arguments, examples, counterexamples and source distinctions.

## Complete construction accounting

| Coverage set | Mapped | Unresolved scope |
| --- | ---: | ---: |
| Original requirements | 615 / 615 | 0 |
| Inherited structural units | 1,055 / 1,055 | 0 |
| Historical source groups | 68 / 68 | 0 |
| Historical records | 9,162,150 / 9,162,150 | 0 |
| Initial new-reasoning assignments | 26 / 26 | 0 |
| Mandatory cross-part families | 12 / 12 | 0 |
| Selected benchmark contents | 106 / 106 | 0 |

The integrated catalog contains 3,716 unit records and 21,367 component records. These are source and requirement facets with explicit overlap relations, not independent books or a manuscript completion percentage. Historical metadata and repeated captures retain their own dispositions.

## Additional source treatments selected by the gap analysis

The gap register accounts for 32 findings and selects 17 additional finite source treatments. Existing and already planned coverage is retained. Original absence observations are preserved where later source reconciliation qualifies them.

| Treatment | Required contribution |
| --- | --- |
| Heuristic problem transformations and working backwards | How can I generate a solution or proof while tracking which transformations preserve the original problem? |
| Best-first search, A* and the limits of heuristic guarantees | Given a represented search problem and heuristic estimates, when does best-first search find a least-cost solution, and what efficiency claim is justified? |
| Hierarchical task-network inference and plan existence | When does decomposing a task by declared methods produce an admissible plan, and when can this search be guaranteed to terminate? |
| Measurement uncertainty and propagation through an inference | What uncertainty does a conclusion inherit from measured inputs? |
| Dimensional and scaling constraints on quantitative claims | Which quantitative relationships are possible given dimensions and scaling assumptions? |
| Approximate conclusions, limiting regimes and explicit error | When does an approximation justify the conclusion being drawn? |
| Numerical error and the validity of computed conclusions | Can a computed value support the claimed sign, ordering or accuracy? |
| Global sensitivity and robustness of model-based inference | Which uncertain inputs or assumptions control the conclusion, and do interactions change the answer? |
| Posterior predictive model criticism | Which aspects of observed data are incompatible with a proposed Bayesian model? |
| Warranted inference from a simulation | What conclusion about a target system is warranted by a simulation result? |
| Factorial contrasts, estimability and confounding | Which separate effects can this experimental design identify? |
| An explicit categorical-syllogistic calculus, with empty-term boundaries | Which categorical conclusions follow from quantified term premises, and when does an inference require a nonempty subject class? |
| Monotonicity and polarity as an explicit method of natural-language inference | When may a phrase be replaced by a broader or narrower expression while preserving an entailment? |
| Inquisitive propositional logic: support, question entailment and resolution-producing proofs | When does resolving some questions, together with stated information, suffice to resolve another question? |
| Question evocation and the PMCE calculus | When do known premises warrant raising a particular question without already settling one of its answers? |
| Refutation and fallacy diagnosis by the defect in an inference | Where exactly does an apparent refutation change meaning, omit a qualification, assume its conclusion or fail to contradict the claim at issue? |
| Consistent aggregation of judgments on logically connected propositions | Can a group accept propositions one by one by majority vote and still have a logically coherent set of conclusions? |

General design/prototyping additions were not selected. Existing analogy, testimony, diagrammatic logic, constraint programming, planning, scientific reasoning and empirical benchmarks retain their actual authored or missing-text standing.

## Using the map

- `edition-2026-coverage-map.json` is the root manifest. It selects exact active shard revisions and hashes; superseded files are historical evidence.
- `coverage/edition-2026/requirements-crosswalk.jsonl` preserves every original requirement and its current assessment.
- `coverage/edition-2026/inherited-crosswalk.jsonl` preserves all inherited ordinals, including the explicit retirement of the six opening-framing units.
- `coverage/edition-2026/reasoning-gap-register.jsonl` preserves every new candidate and its selected, existing or nonselected disposition.
- `coverage/edition-2026/prerequisite-allocation-crosswalk.jsonl` binds declared interfaces and explicit local setup/source-closure obligations. A reference alone is not a proof dependency.
- `coverage/edition-2026/source-overlap-crosswalk.jsonl` and `shared-destination-crosswalk.jsonl` preserve distinct source extents and prevent duplicate completion credit.
- `coverage/edition-2026/completion-work-queue.jsonl` supplies each unit's source, components, destination, remaining work and success/failure conditions.

## Remaining manuscript work

Source acquisition, complete writing and proofs, correction of active errors, integration of drafts and annexes, bibliography and symbols, task/subject navigation, and the final consolidated reviews remain governed by the completion queue and edition contract. Known repairs include unrecognized draft proof environments, unrouted annex material and source-attribution corrections. They were mapped during this phase; the book was not rewritten or rendered.

`map_complete: true` records construction of the scope/coverage map. `catalog_admission_complete: false` preserves the separate independent-admission gate. Neither is publication acceptance. The finite source cutoff remains 7 September 2026. No broad authoring or manuscript review was substituted for this mapping task.
