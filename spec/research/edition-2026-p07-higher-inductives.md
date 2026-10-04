# P7 higher-inductive-type authoring block

Block began 2026-10-03 04:46:34 UTC. The source allocation is ED26-REQ-N-x-001-01 (HoTTBook2013), not N-x-013: the latter's actual frozen units are Jacobs/Lurie categorical logic. Planned sections 91.1–91.3 are the HIT constructors, eliminators/computation, and circle/suspension/quotient/truncation material. No queue, coverage, driver or canonical file was changed. No frozen imaginary packet file was touched.

## Exact sources and reading

The official book site explains that first-edition builds are rolling corrected versions; the version marker, not the bibliographic year alone, fixes the bytes. Official GitHub API metadata verifies public-release commit `e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3`, dated **2013-06-19T19:21:50Z**. This block uses its pinned TeX, not the moved first-edition tag.

| Owned source artifact | SHA256 | Read extent/standing |
|---|---|---|
| `source/references/p07-higher-inductives/hits-public-release-2013.tex` | `cb605e5c917f8ee32ac79f10595148a1dd71e11f73e1d1659c967ac183d79095` | Complete Chapter 6 lines 1–2166, including every constructor/eliminator/proof region, notes and exercises, read sequentially in bounded intervals; truncated command-output gaps were explicitly reread. |
| `source/references/p07-higher-inductives/hlevels-public-release-2013.tex` | `d5340c7d511eabd08eff0cc9404ef0e9faca6d20c5afa60bdd38b3bafd7e0e19` | Chapter 7.3 lines 447–777 read for the general hub-and-spoke construction and its exact sphere/loop dependencies; other Chapter 7 regions not claimed read. |
| `source/references/p07-higher-inductives/hott-book-arxiv-2013-v1.pdf` | `05a533d30addb060a89fba1d1bef15d1f6f115c1f01c8b7f6ed3b2660608179a` | Official arXiv v1 of 3 August 2013; title/copyright/version metadata read: first-edition-257-g5561b73. Its technical chapter body was not substituted for the June source. |
| `source/references/p07-higher-inductives/hits-first-edition-4715f712.tex` | `916f3184ef405acc95c880b58c132c14531e82ee86d41ff4b91dd1c78be75187` | The current first-edition tag resolves to commit 4715f7129f08737f20b028822f1a308d7d83d866 dated 2023-05-24. Retained as a distinct version observation, not 2013 coverage or a completed version comparison. |

Exact official URLs: [book](https://homotopytypetheory.org/book/), [2013 release](https://github.com/HoTT/book/tree/e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3), [Chapter 6 bytes](https://raw.githubusercontent.com/HoTT/book/e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3/hits.tex), [Chapter 7 bytes](https://raw.githubusercontent.com/HoTT/book/e0aa8e9d16858fc0ce01aacd43b24da0bd765ae3/hlevels.tex), and [arXiv v1](https://arxiv.org/pdf/1308.0729v1). The book's title page and official website identify CC BY-SA 3.0; attribution/license standing of the source-derived sections is retained for root's rights integration. No paid access or bypass was used.

New primary-source reading ended at 05:02:59 UTC, before the 05:16:34 cutoff. TeX was read as source; no source or manuscript rendering was performed.

## Actual manuscript contribution

The body and reciprocal annex are `handbook/parts/p07/higher-inductive-types.tex` and `handbook/annex/p07/higher-inductive-types.tex`. Fourteen full local proof items supply transport/dependent 2-path comparisons, circle recursion and coherent mapping property, interval contraction and its nondependent function-equality witness, boolean-monodromy loop nontriviality, suspension-booleans/circle equivalence, coherent pushout mapping property, low-dimensional truncation elimination/universals, witness-extraction counterexample, quotient surjectivity/universal property, a directed-relation example, based-map hub contraction, and conditional dependent hub induction from explicitly supplied fiber-contraction functions.

Point computation is judgmental, path/higher-path computation propositional. HIT principles are added rules/axioms, not an MLTT-only existence theorem. No later cubical face/composition rules are borrowed. Quotient relation paths are not assumed to enumerate every identity, nor are merely existing representatives made into a selector. General n-truncation's raw hub/spoke dependent data are supplied with their recursive inputs; its deeper level-characterization/sphere-adjunction dependencies remain explicit.

The 2013 source has apparent typing slips in the displayed dependent truncation data: lines 1103 give the point value as `a` rather than the supplied `g(a)`, and lines 1120 use base-path arguments where dependent lifts are required. The new text uses the actual motive type and the dependent 2-path definition from lines 505–520, supplying `g(a)` and the correctly typed lift `h = tr²(alpha,u)·k`. These are direct typing repairs, not an import of later cubical computation. Pushout data comparison also retains propositional third-component computation rather than promoting it to judgmental equality.

## Dependencies, intakes and seam

The path/equivalence author supplied stable interfaces `def:p07-hott-transport`, `thm:p07-hott-transport-laws`, `def:p07-hott-funext`, `thm:p07-hott-function-paths`, `def:p07-hott-univalence`, `thm:p07-hott-adjointification` and `thm:p07-hott-fiber-equivalence`. Mapping equivalence proofs supply actual two-sided homotopies and use the reciprocal adjointification/fiber proof; raw uniqueness is not treated as proof that homotopy fibers are propositions. Root must route and preserve those foundational dependencies before calling the combined packet integrated.

The bibliography intake adds only `HoTT2013PublicReleaseHIT`, an exact version key, leaving canonical `HoTTBook2013` unchanged. The symbol intake has the canonical columns `glyph,macro,role,scope,precedence,first_use,notes`; source-specific judgmental equality, DPath/DPath², suspension versus dependent-sum notation, HIT interval versus cubical dimensions, and each recursive truncation constructor have explicit scopes.

Root owns driver insertion. Suggested seam: after the new HoTT path/equivalence/univalence foundation packet in P7 and before the separate cubical packet. Add the new reciprocal annex once in matching order and merge the disjoint intakes. No child, review agent, test, build, render, receipt, map or coverage-row edit was performed.

## Exact remaining source duties

This is a substantive **incomplete** original-source reconstruction, not closure of Chapter 6 or the broad N-x-001 facet. Remaining Chapter 6/7 work includes the precise torus dependent-composition/computation exercise and its product comparison; direct-versus-suspension higher-sphere comparisons and full based sphere–loop adjunction coherences; the general n-type loop characterization and its use to prove full general truncation elimination/universals; complete impredicative/canonical-representative quotient comparisons with resizing/universe hypotheses; original free/presented algebra constructions and their omitted list/cancellation lemmas; the complete flattening construction with dependent-function and Σ-path coherence; every not-yet-authored source exercise, figure and qualification. These families remain owed, not excluded for this block.

For the circle's loop-space/fundamental-group calculation, the remaining duty is the actual code family, transport/winding construction and both encode–decode composites with their needed coherence, not a theorem-name placeholder. No such calculation or higher homotopy-group claim is made in the new packet. Independent review, static/build/render checks and original-version correspondence remain pending for the completed integrated batch.
