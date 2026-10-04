# Active reference repairs, 9 September 2026

## Completed extent

The active editorial corrections address 33 of the 35 ordinary Reference warnings in build/review-2026-09-08-2130/handbook/main.log: 24 whitespace-damaged label occurrences, seven destination repairs, and two missing preorder-definition destinations restored to the active route. The remaining two ordinary warnings concern generated CQ/TQBF entries; those retired names also produce four associated Hyper reference warnings.

Every edited caller and its actual destination was read. One read-through of the saved edits was completed. No build, render, test, scanner, independent review or generated-output regeneration was run. These are source-level corrections, not a claim that a new compilation has confirmed a warning-free result.

## Seven exact destination repairs

| Active caller | Old destination | New destination |
| --- | --- | --- |
| handbook/parts/p10/heyting-completeness.tex, IPC language and finite-support derivability | def:p08-ipl-finite-support | sec:intuitionistic-logic-01 |
| handbook/parts/p10/modal-algebra-completeness.tex, extension to arbitrary normal L | def:p08-modal-derivability | sec:modal-temporal-epistemic-01 |
| handbook/parts/p10/modal-algebra-completeness.tex, strong local general-frame completeness | def:p08-modal-derivability | def:p10-normal-modal-algebra-logic |
| handbook/parts/p19/conditional-reasoning-and-suppression.tex, material-conditional benchmark | def:p02-valuation | sec:prop-syntax-semantics-02 |
| handbook/parts/p19/conditional-interpretation-experiments.tex, finite valuation states | def:p02-valuation | sec:prop-syntax-semantics-02 |
| handbook/annex/p19/conditional-reasoning-and-suppression.tex, truth-preservation proof | def:p02-valuation | sec:prop-syntax-semantics-02 |
| handbook/annex/p06/cardinals-choice-supplement.tex, Choice-to-Zorn proof | thm:p01-well-ordering | thm:p06-choice-equivalents-source |

The active source sections contain the exact finite-support LJ, theorem-only modal necessitation and recursive classical truth clauses required by their callers. The P19 bodies explicitly identify 0 and 1 as codes for false and true, matching the active source's named truth values.

The well-ordering caller requires a well-order of an arbitrary set P under AC. Its new target is the well-ordering clause of the active Choice-equivalence theorem, anchored in handbook/parts/p06.tex and stated in handbook/restoration/inherited-10559-10674.tex. It was not redirected to the least-element principle for natural numbers.

## Preorder definitions restored before use

The exact nonempty-preorder domain required by the P10 caller differed from the inherited partial-order presentation. Following the root's additional instruction, three definitions were inserted near the beginning of the already active handbook/parts/p08/intuitionistic-supplement.tex, before its system card:

- def:p08-ipl-kripke-structure: a nonempty reflexive/transitive frame, an arbitrary declared propositional-variable set and persistent valuations.
- def:p08-ipl-forcing: atoms, bottom, conjunction, current-world disjunction and implication over all later worlds.
- def:p08-ipl-consequence: local consequence at a common world over those nonempty preorder structures.

The third definition keeps semantic consequence distinct from finite-support syntactic derivability. Kripke1965 and TroelstraSchwichtenberg2000 attribution is retained. The two original missing references in handbook/parts/p10/heyting-completeness.tex now name the intended active definitions. The inherited partial-order definitions were preserved; no obsolete file was routed wholesale and no shared driver was changed.

## Whitespace corrections

Literal cref argument lists were joined where a line break after a comma had become an initial space in the next label. All mathematical label identities and their order were preserved. The 24 affected occurrences span GPSS, probability/martingale results, causal mediation and identification, matching and information comparison, and argumentation/program semantics.

## Changed active files

All paths are relative to C:/Dev/the-methods-of-reason:

- handbook/parts/p08/intuitionistic-supplement.tex
- handbook/parts/p09/presentations/n-c-012.tex
- handbook/parts/p10/heyting-completeness.tex
- handbook/parts/p10/modal-algebra-completeness.tex
- handbook/parts/p15/martingales-and-convergence.tex
- handbook/parts/p15/strong-law-rates-and-normalization.tex
- handbook/parts/p15/weak-laws-and-triangular-arrays.tex
- handbook/parts/p15/feller-weak-law-presentation.tex
- handbook/parts/p15/martingale-maximal-inequalities.tex
- handbook/parts/p15/weak-convergence-of-laws.tex
- handbook/parts/p15/predictable-quadratic-variation.tex
- handbook/parts/p16/finite-counterfactuals.tex
- handbook/parts/p16/latent-identification-foundations.tex
- handbook/parts/p16/causal-mediation.tex
- handbook/parts/p17/social-choice.tex
- handbook/parts/p17/value-of-information.tex
- handbook/parts/p18/arbitrary-argumentation.tex
- handbook/parts/p18/logic-program-argumentation.tex
- handbook/parts/p18/argumentation-meta-interpreters.tex
- handbook/parts/p19/conditional-reasoning-and-suppression.tex
- handbook/parts/p19/conditional-interpretation-experiments.tex
- handbook/annex/p06/cardinals-choice-supplement.tex
- handbook/annex/p19/conditional-reasoning-and-suppression.tex

## Two generated-output residuals and their actual upstream producers

The retired thm:p09-cq-evaluation occurs in handbook/generated/audit-p09.tex at line 83 and handbook/generated/named-theorem-index.tex at line 94. Its current upstream content is split between thm:p09-cq-data-evaluation and thm:p09-cq-combined-evaluation in handbook/parts/p09/logic-in-computer-science.tex. They must remain distinct: fixed-query data complexity is AC0, whereas combined evaluation is NP-complete.

The retired thm:p09-tqbf-proof occurs in handbook/generated/audit-p09.tex at line 89 and handbook/generated/named-theorem-index.tex at line 357. The actual canonical target is thm:p04-tqbf-pspace in handbook/parts/p04/complexity.tex, paired with annex:p9.tqbf.1 in handbook/annex/p09/proofs.tex. The P09 proof-route paragraph explicitly preserves that single public theorem identity.

The actual generators were read, not executed:

- tools/audit_tables.py: reachable_part_files follows the input graph from each handbook/parts/pNN.tex; collect reads the active theorem/definition environments. Source metadata comes from spec/source-unit-inventory.csv and validated restoration provenance. Generation additionally requires the applicable corrected-reader admission records. The upstream CQ content is the active P09 host, not a separate obsolete CQ declaration.
- tools/build_named_theorem_index.py: reachable_files follows the input graph from handbook/main.tex; collect reads active theorem/lemma/corollary declarations, with source titles from spec/source-unit-inventory.csv and explicit source-hook mappings. The canonical TQBF record is the active P04 theorem.

The bounded upstream search found the retired IDs in generated outputs and historical inventory reports, not current active declarations. Their current upstream identities are already correct. The generated lookup surfaces should be regenerated at the final apparatus step, after the required admission inputs are ready; no replacement alias or direct generated-file edit was introduced.
