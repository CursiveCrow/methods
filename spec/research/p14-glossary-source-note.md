# Chapter 289: symbols, terminology and glossary — author return

## Deliverable and boundary

Owned body: `handbook/parts/p14/symbols-terminology-and-glossary.tex`.
Assignment: all five sections of Chapter 289 in the approved
`spec/PROPOSED-TABLE-OF-CONTENTS.md` (chapter heading at line 3408).
This is an authored lookup chapter based on existing, routed definitions,
not a claim that every term in every source presentation has been indexed.
The root owns the part route, canonical bibliography and symbol register,
scope bindings and generated indexes. None of those shared files was edited.

The five sections are substantive:

1. Symbols by spelling, typed role and named source convention, including
   the operand/type-sensitive readings of consequence, satisfaction,
   sequent arrows, equivalence, forcing, probability, tensor and context
   letters. A reader method explains how to resolve a spelling rather than
   inventing one global meaning.
2. Grammar and precedence, binding by occurrence, alpha-equivalence,
   capture avoidance, and the difference between simultaneous uniform
   substitution, term substitution, selected subformula replacement and
   lambda substitution. Worked parsing and capture examples are included.
3. Sixteen overloaded-word comparisons: admissible, argument, belief,
   coherence, complete, confidence, consistency, independence, model,
   normal, possibility, preference, resolution, support, type and valid.
4. Eighty-one grouped glossary entries: 20 logic/syntax/semantics/proof;
   14 inference/explanation/computation/argumentation; 22 probability,
   statistics and uncertainty; 11 causal/counterfactual; 14 decision,
   preference and strategic interaction. Groups contain multiple related
   vocabulary terms with their distinctions, not 81 claims of exhaustive
   coverage of the book.
5. Twenty-two historical/source-name rows: Sheffer/NAND, Peirce/NOR,
   material conditional, equivalence/biconditional, Polish notation,
   categorical terminology, Hauptsatz, Entscheidungsproblem, recursive,
   r.e./c.e., semidecision, Skolemization, Lowenheim–Skolem/Skolem paradox,
   manifestations/abducibles, Dung acceptability, the finite CHANCE source's
   distribution-function name, Neyman's coefficient convention,
   Bayes formula/factor, fixed/common-effect terminology, Bernoulli/vNM
   utilities, Nash countering and meta-reasoning.

No new theorem, calculus or mathematical symbol role is declared. The one
new `hbmethod` is a reading procedure, not a formal existence or adequacy
claim. No new proof annex is needed: calculations are direct illustrations
of linked existing definitions and results. Existing proof statuses are not
upgraded by the glossary.

## Actual live source route used

The project reader index was constructed from `handbook/main.tex` using the
existing `tools/symbol_registry.py::ReaderIndex`. At initial acquisition it
contained 1,155 routed source files and 8,658 labels and reported no route
errors. Generated input tables are deliberately excluded by that index.
The tempting `parts/p01/formal-work-conventions.tex` and several compact old
P4 chapter files are **not** on that route. Their contents were not treated
as live reference targets. The following are the actual read destinations.

### Foundational notation and logical definitions

- `handbook/parts/p01/symbol-registry.tex`: complete reader chapter;
  `sec:p01-symbol-registry`, `tab:p01-precedence`, `tab:p01-sixteen`,
  `tab:p01-notation-variants`, `sec:p01-letter-conventions`.
- `handbook/registry/symbols.csv`: actual base/core rows and the operand,
  scope and source-local conventions used in this chapter.
- `handbook/registry/symbol-scopes.json`: actual named bindings and typed
  override records, particularly `s` as initial search state versus
  first-order assignment, the inquisitive tensor scope, normal linear
  temporal/Chellas presentation boundaries and source-local order roles.
  The JSON is locator/registration data, not proof of a mathematical claim.
- `handbook/restoration/inherited-00798-00852.tex`,
  `00853-00906`, `00907-00984`, `00985-01023`, `01024-01084`:
  the live Levels chapter, language/calculus/semantics and object/meta-level
  definitions, consequence/derivability/soundness/completeness,
  satisfaction/truth/model, arguments and sentence countermodels.
- `handbook/restoration/inherited-01661-01816.tex`: actual CPL grammar,
  right-associated chain and finite connective conventions, defined
  biconditional/verum and unique readability.
- `handbook/restoration/inherited-03105-03165.tex`,
  `03166-03239`, `03240-03428`, `03429-03518`: FOL grammar,
  free-variable sets, substitution and alpha-equivalence, structures,
  assignment/update, expansion and reduct. `parts/p02.tex` supplies the
  live `def:p02-fol-capture-avoiding-substitution` and
  `def:p02-fol-alpha-equivalence` hook labels at those definitions.
- `handbook/parts/p02/propositional-substitution.tex`: actual uniform
  substitution and selected occurrence replacement definitions, the
  example contrasting them and the equisatisfiability failure.
- `handbook/parts/p02/syllogistic-inference.tex`: actual two-literal
  categorical language, no individual variable binder, set semantics and
  empty-class distinction from historical treatments.
- `handbook/restoration/inherited-04921-04967.tex`: compactness statement
  and its Choice/signature/sentence scope.
- `handbook/restoration/inherited-05132-05567.tex`: Skolemization and the
  two directions of the expanded-signature equisatisfiability theorem.
- `handbook/restoration/inherited-05568-05923.tex`: actual equality-free,
  finite-clause resolution completeness statement and its factoring,
  ground-term and lifting boundaries. Glossary use does not change the
  source proof-sketch standing.
- `handbook/parts/p03/maps-elementarity-supplement.tex`: complete live
  notation lookup, including atomic **and negated atomic** diagram
  sentences, elementary diagram, type space and isomorphism glyph.
- `handbook/restoration/inherited-06138-06242.tex`,
  `06332-06421`, `06510-06629`, `07150-07294`: substructure and isomorphism
  invariance, parameter expansion/diagrams, types/type space and the
  explicit distinction between deductive, semantic and model completeness.
- `handbook/restoration/inherited-07753-07843.tex` and
  `08248-08305`: actual c.e./decidable/recognizer definitions and classical
  Entscheidungsproblem statement. `parts/p04.tex` exposes the existing
  machine-decidability/c.e.-equivalent-forms result labels.
- `handbook/restoration/inherited-10770-10825.tex` and
  `10900-10988`: forcing order, typed names, interpretation/extension and
  distinction between semantic and recursively specified forcing.
  `parts/p06.tex` supplies `def:p06-forcing-order-orientation`.
- `handbook/registry/calculi/lj.tex`, `lk.tex`, and
  `handbook/parts/p14/rule-sheets.tex`: exact sequent shapes and the
  `showcalculus` route for the two named sheets. The literal reader index
  does not expand `showcalculus`; these two sheet labels were verified in
  the actual rendered-route source files instead of reported dangling.
- `handbook/parts/p07/intuitionistic-cut-elimination.tex` and
  `lambda-calculi-and-type-theories.tex`: literal/alpha-class distinction,
  exact LJ target, lambda grammar/substitution, conversion versus
  reduction, weak/strong normalization and confluence boundary.
- `handbook/parts/p08/intuitionistic-kripke-completeness.tex`,
  `paraconsistent-and-nonmonotonic.tex`, `inquisitive-propositional.tex`,
  `many-valued-supplement.tex`, `relevance-linear-supplement.tex`:
  local forcing, paraconsistency/nonmonotonicity/preferential models,
  support and tensor, numeric residuum and the actual CLL grammar/units.

### Inference, probability, causation, decision and historical lookup

- Existing `parts/p14/master-tables.tex` glossary and its surrounding
  apparatus, `reasoning-methods-and-evidence.tex`,
  `reasoning-task-finder.tex`, and the current countermodel chapter's
  live destinations. The new chapter develops the cross-domain glossary
  without editing or silently retiring the old short glossary.
- `parts/p12/heuristic-search.tex`: actual instance and
  admissibility/consistency declarations.
- `parts/p15/finite-probability.tex`: finite space/mass/law,
  conditioning/null-event boundary, hypothesis partition, Bayes formula,
  independence, expectation and conditional expectation.
- `parts/p15/measurable-probability.tex`: sigma-algebra/measure,
  measurable map, pushforward law and CDF definitions;
  `measure-extension.tex`: quantile map;
  `independent-random-variables.tex`: covariance/correlation definition.
  Only the needed defining passages were read, not claimed full new
  acquisitions of the entire Durrett source.
- `parts/p15/hypothesis-tests-and-confidence.tex`,
  `bayesian-updating-prediction.tex`, `bayesian-model-comparison.tex`:
  sampling experiment/errors/power, valid p-value, confidence procedure,
  dominated joint model, posterior/credibility/loss and marginal-factor
  odds definitions with their quantifier and normalization boundaries.
- `parts/p15/imprecise-probability.tex`: bounded gamble/prices/coherence;
  `measurement-uncertainty.tex`: expanded uncertainty;
  `evidence-synthesis.tex`: distinct synthesis targets, normal effects and
  estimated-weight versus known-variance boundary.
- `parts/p16/finite-abduction.tex`, `finite-causal-models.tex`,
  `graphical-separation-adjustment.tex`, `finite-counterfactuals.tex`:
  explanation and minimality inputs, model/equation/intervention/
  identification data, active paths/conditional independence/back-door
  overlap, shared-background worlds, ATE/ATT, potential outcomes and
  nonidentification of their coupling.
- `parts/p17/finite-preferences.tex`, `finite-expected-utility.tex`,
  `ambiguity-and-robust-choice.tex`, `finite-strategic-games.tex`,
  `risk-aversion.tex`, `sequential-decisions.tex`,
  `value-of-information.tex`: actual preference/choice, lotteries/mixture
  independence/vNM scale, maxmin versus robust dominance, unilateral
  best-response/Nash, sure-mean risk aversion/FSD, history/Markov/stationary
  policies and signal-value definitions.
- `parts/p18/finite-argumentation.tex`: framework/attack/defense,
  extensions and the explicit nonempty-family skeptical-query convention.
- `parts/p19/evidence-methods.tex`, `calibration-and-extreme-confidence.tex`,
  `rationality-8-6.tex`: empirical question/benchmark/estimand/evidence
  record, confidence/accuracy/calibration/resolution and monitoring/control
  with the psychological/formal object-level distinction. No numerical
  original Ackerman2014 assertion is added; its protected open source
  dependency remains unchanged.
- `parts/p13/chronology-and-biography.tex`: actual historical names,
  Skolem internal/external countability distinction and notation/method
  coexistence account.

## Attribution and intakes

The chapter uses 18 already canonical citation keys:
`Church1936`, `DeeksEtAl2024Cochrane10`, `Enderton2001`,
`Gentzen1934a`, `Gentzen1935b`, `GrinsteadSnellChance2006`,
`HalpernUncertaintyChapter2Extract`, `HilbertAckermann1928`,
`Lukasiewicz1929`, `Nash1950EquilibriumPoints`,
`Nash1951NonCooperative`, `Neyman1937Confidence`,
`Pearl2009CausalOverview`, `Rubinstein2015LectureNotes`,
`Shoenfield1967`, `ThompsonElqayamAckerman2021MetaReasoning`,
`Turing1937`, `WhiteheadRussell1910`.
The home entries supply their other original-source attribution and
proof standing. This task reused those source-supported manuscript
definitions; it does not certify rereading every external source behind
every linked term or every linked proof.

`handbook/bib/intake-p14-glossary.bib` explicitly records that there are no
new bibliography entries. `handbook/registry/symbols-intake-p14-glossary.csv`
contains its header and no new rows: these are existing symbol-role
lookups, not new local definitions or newly invented notation. No published
symbol was renamed to hide an overlapping role.

## Author read-through and bounded checks

The actual LaTeX chapter was read through in sections. Repairs from that
read-through: the countermodel chapter label was corrected; the mixture
independence weight was stated strictly between zero and one; distinct
variables and a binary relation were stated in the capture example;
alphabetical ordering was retained in the domain glossary; the source
CPL right-association versus editorial left-association distinction was
made concrete instead of relying on a generic override disclaimer.

A focused reference inventory found 188 distinct reference targets:
all are existing unique live targets, own new targets, or the two
verified `showcalculus` sheet targets. No missing target remained.
The 15 new labels did not collide with live labels. All 18 citation
keys exist in the canonical bibliography. Four longtables, five
description lists and the one reader-method environment have matched
openings/closings. This was a bounded check of the authored package,
not a book review wave or a mathematical revalidation of every linked
theorem. No tests, new test files, book build or PDF render were run.

Remaining integration: root adds the owned body route for Chapter 289 and
decides the relation of its old compact master glossary to the expanded
lookup chapter. Canonical intakes/generation remain root-owned. Physical
layout and the integrated book's build have not been checked in this
authoring block. The package does not claim glossary exhaustiveness,
publication readiness or completion of unrelated open source units.
