# Chapter 285: Decidability and Complexity Tables

Authoring unit: handbook/parts/p14/decidability-and-complexity.tex.
New proofs only: handbook/annex/p14/decidability-and-complexity.tex.
Unique intakes: handbook/bib/intake-p14-decidability.bib and
handbook/registry/symbols-intake-p14-decidability.csv.
Root owns driver routing, canonical merging, scope bindings and replacement
of overlapping shared master-table rows.

## Five-section coverage

The proposed five headings are all written. There are 14 longtables and
169 rows, plus two new theorem statements with reciprocal full proofs.

- Exact decision problem/input representation: 12 rows; a finite encoded
  problem includes fixed objects, supplied inputs, yes condition, size and
  reduction convention. Node/literal/arithmetic counts are not bit costs.
  Explicit and succinct models, formula/tree expansion, rational encodings,
  unary horizons and finite schema versus finite grounding are distinguished.
- Validity/SAT/consequence/equivalence/model checking: 40 rows; the five
  questions are separated, finite CPL reductions are proved, and Boolean,
  modal, epistemic, conditional, matrix, inquisitive, erotetic, relevant,
  linear and nonmonotonic languages retain their exact restrictions.
- Data/formula/query/combined complexity: 42 rows; fixed-query, fixed-model,
  fixed-template, fixed-arity and combined inputs are separated. CQ,
  Datalog, Vardi's distinct source languages, CSP, standalone versus
  general-TBox DL, each written AL/EL boundary, stable/well-founded programs,
  LTL fragments, CTL/CTL*, PDL, mu, PCTL, CSL and likelihood appear.
- Finite/unrestricted structures: 42 rows; unrestricted/finite FO,
  relational monadic/FO2/counting/guarded/prefix fragments, the fixed
  almost-sure graph theory, full/matched-Henkin SOL, automata,
  arithmetic/word/tiling/index problems, SMT, unification and typed decisions.
- Classifications/conditional bounds/open questions: 33 rows; complete
  reductions are separated from citations/sketches, unmatched bounds stay
  unmatched, hierarchy/Savitch/proof-size/interpretation/Occam hypotheses
  stay visible, and HTN/argumentation/abduction/causal/transformation results
  retain output and representation costs.

The current-reader inventory had about 130 theorem/card candidates, plus
source paragraphs (notably AL/EL and first-order prefix bounds). Pure
semantic completeness, expressive capture, substitution formula rank,
bias--variance, and representability are not automatically decision
classifications. Capture and relevant conditional consequences are included
with their distinct roles, not silently treated as model-checking classes.
This unit is a lookup presentation; it does not replace the full source
presentations or satisfy unread whole-source/version obligations.

## Actual reader material used

The existing P14 master decision table was read before authoring. ReaderIndex
was used only to locate the current main.tex route; inactive historical
labels were not substitutes for current definitions or proofs. Relevant
actual statements, procedures and restrictions were read in:

- P02 propositional metatheory/Tseitin/syllogistic/first-order fragments and
  current matched-Henkin semantics; P04 complexity/frontier and current
  inherited serialization, enumeration, halting and Rice passages.
- P05 decidable arithmetic/theoremhood/interpretation transfer and P07
  normalization, Church checking, Curry undecidability and proof complexity.
- P08 current system cards/supplements and the completed non-strict X/U
  completeness/space proofs, not the older seven-rule presentation by name
  alone.
- P09 current main chapter and routed presentations N-c-002,004--007,
 009--014,024 and the relevant database/program material. The 2005 EL
  extension bounds are dated source results; ELI's old unmatched bounds
  are not a claim that its classification remains open today.
- P12 actual automation/SMT/optimization/completion statements; P15 Occam;
  P16 abduction/ID/Tian; P17 exact HTN restrictions; P18 finite versus
  infinite program and argument/game interfaces.

Matched Henkin strong adequacy is thm:p02-sol-derived-adequacy, for the
translation-defined relation under ambient AC. Its native displayed rule
list completeness is expressly not proved (def:p02-sol-native-boundary).
The inactive legacy sol-henkin-completeness label was not reused.

Two new mathematical dependencies are fully resolved locally:

1. Finite classical consequence and equivalence: polynomial countervaluation
   certificates and reductions from the existing cited coNP-complete TAUT.
   No arbitrary-premise compactness or nonclassical implication is imported.
2. Horn-SAT P-hardness: existing cited logspace P-complete CVP is translated
   to a dual-rail Horn instance, with the false output rail forbidden.
   Topological induction proves the least closure has exactly the computed
   rails; malformed encodings map to an unsatisfiable constant instance.
   Negation gates are handled explicitly, so monotone CVP hardness is not
   presumed. The existing forward-chaining upper bound stays in its original
   literal-reference measure.

## New primary status evidence

1. Clay Mathematics Institute, official “P vs NP and Complexity Lower Bounds”
   workshop page; 29 September--3 October 2025:
   https://www.claymath.org/events/p-vs-np-and-complexity-lower-bounds/
   Its actual introduction reports P versus NP as open. This is selected
   dated status evidence, not a proof or an entire source-paper reading.
   Bib key ClayPVNP2025Workshop.

2. Marnix Suilen and Guillermo A. Pérez, “On the Complexity of Robust Markov
   Decision Processes and Bisimulation Metrics”, arXiv:2604.26748v1 [cs.LO],
   29 April 2026, 24 pages.
   https://arxiv.org/pdf/2604.26748v1
   Captured at source/references/p14-decidability/suilen-perez-2026-v1.pdf;
   854246 bytes, SHA-256
   faef6155b47773221268bc8393842a210671864d8a374c7d4f68f80068ad449a.
   Actual first three PDF pages, including the Introduction/contribution 3,
   were read. Its dated report calls parity-game polynomial winner decision
   a longstanding open question. No RMDP/bisimulation classification or
   reduction proof from the remainder is imported.
   Bib key SuilenPerez2026RobustMDPV1.

A November 2025 arXiv polynomial-parity algorithm claim appeared in retrieval.
Its title/abstract is not an accepted solution; its full proof has not been
assessed here. The chapter reports exactly the dated April 2026 primary
statement, rather than asserting a verified up-to-October status.

## Integration and precise remaining catalog obligations

- Route the new body/annex and merge the two bibliography keys and seven
  genuinely local symbol rows. Proposed named scope bindings:
  “P14 decidability inputs” -> def:p14-dc-instance;
  “P14 Horn reduction” -> annex:p14.dc.horn.
  Both first-use anchors exist in the corresponding new source.
- Shared master-table 2-SAT currently says NL-complete; its routed theorem
  supplies linear SCC time only. A complete matching NL lower/upper
  source/reduction presentation is not discharged by that algorithm.
  The new chapter records the actually supported linear procedure.
- Shared master-table unrestricted FO validity says c.e.-complete; current
  named body establishes c.e. enumeration plus cited undecidability.
  The stronger many-one degree statement still needs its exact active
  reduction/source presentation. The new row does not deny the stronger
  known classification; it does not promote the weaker local argument.
- Modal-mu satisfiability uses the existing cited EXPTIME-complete card.
  Kozen1983 alone must not silently stand in for a later exact complexity
  proof. Root's source allocation/full-presentation obligation remains.
- Current loosely guarded finite-model status and the modern sharp ELI
  class are not settled by 1999/2005 historical source snapshots. The
  chapter preserves their actual dated/unrestricted bounds. Add a current
  classification only after its own primary statement/proof standing is
  read and integrated.
- The dated parity question is selected status evidence, not a proof audit
  of all later claimed solutions. Any undated current-open master wording
  needs its cutoff/source qualifier.

## Author verification

Actual final TeX and the two proofs were read for mathematical dependencies,
including the CVP dual-rail negation case and least-model rather than guessed
rail values. A bounded current-route reference check (plus the new local
labels because routing is root-owned) found no missing references and no
unknown citation keys; 14 longtables have matching endpoints. No inactive
global-label inventory, book build, PDF inspection, prose test or consolidated
review wave was used. Driver and registry integration are pending root work.
