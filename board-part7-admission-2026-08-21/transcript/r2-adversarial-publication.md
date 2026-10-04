# Part VII admission board, round 2: adversarial-publication review

Reviewer: adversarial-publication seat  
Scope: current reader graph rooted at `handbook/parts/p07.tex` and
`handbook/annex/p07.tex`; no other seat transcript read.  
Mode: read-only hostile source/content review; no test, checker, TeX build, PDF
render, or handbook/spec/tool/generated-file edit.

## Executive disposition

The current graph is materially stronger than the opening graph. It now has a
visible source map, literal exact-source destinations, a routed and hyperlinked
A-113 register, complete named-theorem hooks, A-117, updated active-sheet
navigation, reciprocal proof items, a complete Church--Rosser proof, a complete
selected propositional cut-reduction proof, and source-honest Haken and HA
extraction boundaries. I found no silent missing rule family in the new
LK--ND, Maehara, Church--Rosser, or selected propositional cut proofs.

Four source/content publication blockers remain. The verdict is therefore
**REJECT**, independently of the unrun build/visual/administrative/user gates.

## Blocking findings

### R2-F1 — contradictory canonical-LK completeness status and stale public part identity

- **Severity:** major publication blocker.
- **Location:**
  `handbook/parts/p07/calculi-and-derivability-supplement.tex:49-56,214-245`.
- **Current evidence:** the structural-rules table says at lines 49-52 that
  canonical-LK cut admissibility is not established by “the Part-VIII
  reduction.” The live cut-elimination chapter is in current Part VII; if
  “Part VIII” means the historical v1.1 source part, that historical standing
  is not stated. More importantly, the calculi catalog at lines 242-245 still
  says canonical-LK completeness is “sketched,” while the same live file now
  declares `thm:p07-canonical-lk-completeness` as `proved=annex:p7.calculi.4`
  at lines 214-222, and the reciprocal proof is
  `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex:192-217`.
- **Failure path:** a reader consulting A-071 receives a lower and obsolete
  evidence level for a theorem immediately proved in the same chapter, and an
  unexplained Part-VIII reference appears to point to the next public part
  rather than to historical source provenance.
- **Exact correction:** change the canonical-LK catalog cell to state that
  finite-sequent completeness is proved in `thm:p07-canonical-lk-completeness`
  while cut admissibility remains unavailable for that presentation. Replace
  “Part-VIII reduction” with “the inherited defined-negation reduction in this
  Part VII” or explicitly “historical v1.1 Part VIII source reduction.”
- **Status:** open, source/content.

### R2-F2 — D-P8-004/N-a-070 still does not contain the promised local Craig/Beth proof

- **Severity:** blocker against register completeness.
- **Location:**
  `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:108-177`,
  `handbook/annex/p07/interpolation-supplement.tex:7-120`, and
  `handbook/restoration/inherited-11768-11823.tex:11-55`.
- **Current evidence:** the Maehara partition lemma is now honestly
  `proved=annex:p7.interp.1`, and the annex checks the two initials,
  weakening/contraction, all one- and two-premise propositional rules,
  non-eigenvariable quantifier rules, both placements of `\forall R`, and both
  placements of `\exists L`. But the body proof boundary expressly says at
  lines 120-127 that arbitrary Craig interpolation still depends on the
  inherited cut-elimination theorem, whose source status is only a proof
  sketch, and therefore the Craig and Beth theorems remain cited. Lines
  153-177 are labelled only “Route to the cited Craig theorem” and “Route from
  the cited Craig theorem to the cited Beth theorem.” D-P8-004 and N-a-070
  require Craig proved by Maehara with the Beth corollary, not merely the
  partition sublemma plus a route through an acknowledged sketch.
- **Failure path:** a reader cannot compose a complete local Craig proof because
  the transformation to a cut-free derivation is not available at proof
  standing. The generated audit correctly reports Craig/Beth as cited, which
  demonstrates that the must E-ceiling remains unfilled rather than silently
  closed.
- **Exact correction:** either supply a complete cut-elimination proof for the
  exact equality-free LKd calculus and then route complete Craig/Beth annex
  proofs, or explicitly import a complete cited cut-elimination theorem as a
  premise and give the complete derivational composition to Maehara and Beth.
  Only then change the Craig/Beth statuses; do not promote the inherited sketch.
- **Status:** open, source/content.

### R2-F3 — the selected full MLTT sheet still has no matching normalization or checking theorem

- **Severity:** blocker against N-c-030.
- **Location:**
  `handbook/parts/p07/lambda-calculi-and-type-theories.tex:397-451`,
  `handbook/registry/calculi/mltt-intensional.tex:4`, and
  `handbook/parts/p07/proof-complexity.tex:254-279`.
- **Current evidence:** the active `sheet:mltt-intensional` contains dependent
  products, dependent sums, intensional identity types, and a cumulative
  predicative Russell-universe hierarchy. The body now states with commendable
  precision that the cited Abel--Coquand--Dybjer theorem covers only dependent
  functions and one Russell universe and **does not** cover sums, identity
  types, cumulative/stratified universes, or the full selected sheet
  (`lambda-calculi-and-type-theories.tex:419-450`). A-189 repeats the same honest
  limitation at `proof-complexity.tex:254-279`. N-c-030, however, requires the
  selected Pi/Sigma/identity/universe MLTT entry together with normalization and
  decidable type-checking statements.
- **Failure path:** the reader has a public formal calculus but no theorem
  supporting normalization, judgmental-equality decision, or checking for that
  calculus. The narrower comparison row cannot be used as evidence for the
  live sheet, as the manuscript itself correctly warns.
- **Exact correction:** either narrow `sheet:mltt-intensional` and the public
  MLTT identity to the exact Abel--Coquand--Dybjer calculus, or state and cite
  normalization/equality-decision/type-checking theorems for the complete
  selected Pi/Sigma/identity/cumulative-universe system, matching its conversion
  and universe rules literally.
- **Status:** open, source/content.

### R2-F4 — N-a-055's “with proofs” requirement remains source-cited rather than supplied in the handbook

- **Severity:** blocker against the stated must-content ceiling; proof status
  itself is now honest.
- **Location:**
  `handbook/parts/p07/functional-interpretations.tex:325-389` and
  `handbook/annex/p07/functional-interpretations.tex:31-37`.
- **Current evidence:** IPC disjunction, HA disjunction, and HA numerical
  existence remain `cited=TroelstraVanDalen1988` at body lines 340-361. The new
  source boundary at lines 370-389 explicitly says the handbook does not
  reproduce the source's proof-term grammar, equality conversions, induction
  reductions, normalization, or erasure theorem and therefore does not claim a
  local proof. The annex likewise says those three properties receive no local
  annex proof. This removes the old status contradiction and stale stub prose,
  but N-a-055 explicitly requires the disjunction and numerical-existence
  properties “with proofs.”
- **Failure path:** a reader receives a precise bibliography locator and proof
  shape, not the promised proof artifact. The locally proved LJ last-rule lemma
  cannot discharge HA equality, induction, normalization, or erasure, exactly
  as the current boundary acknowledges.
- **Exact correction:** add a selected HA proof-term calculus with equality and
  induction reductions, state its normalization/canonicity/erasure theorem at
  honest evidence level, and give reciprocal annex proofs of the three
  extraction properties; alternatively obtain an explicit user/register ruling
  that citation-only treatment satisfies N-a-055 rather than claiming the
  current bytes meet a “with proofs” commitment.
- **Status:** open, source/content.

## Verified current repairs and clean seams

### Source/editorial distinction and construction debt

- `handbook/parts/p07/source-map.tex:1-19` visibly identifies all nineteen
  exact intervals, the authoritative line range, original proof statuses, and
  each editorial category without printing admission workflow state.
- The live graph contains no reader-visible OPEN, unadmitted, stub, workflow,
  or owed-artifact prose. Similar strings in retained, unreachable historical
  `parts/p07/*.tex` or annex files are outside the current route.

### A-113, literal exact destinations, and A-159

- `handbook/parts/p07.tex:5-84` supplies literal `entry:p07-source-1` through
  `entry:p07-source-31` anchors and governed labels for every formerly
  unlabelled exact named result while enabling the hooks only around exact
  wrappers.
- `handbook/parts/p07.tex:120-128` routes A-113 once.
  `handbook/generated/audit-p07.tex:15-143` contains hyperlinked stable IDs and
  no unclassified/invalid result; exact proofs, sketches, and citations retain
  their source standing.
- The current named index has 408 data rows and includes exact LK soundness,
  cut elimination, propositional subformula, empty-sequent underivability, NJ
  normalization, STLC subject reduction, and STLC strong normalization.
  `handbook/parts/p14/master-tables.tex:239-241` is count-free.

### New proof audit

- **LK--ND and canonical-LK completeness:**
  `annex/p07/calculi-and-cut-elimination-supplement.tex:50-217` handles every
  equality-free canonical-LK structural, propositional, primitive-negation,
  quantifier, empty-succedent, eigenvariable, Cut, and initial case in the
  forward translation and every equality-free ND assumption, introduction,
  elimination, alpha, eigenvariable, and RAA case in reverse. It explicitly
  respects nonvacuous discharge and then derives arbitrary finite succedents.
  The completeness item correctly composes the proved ND completeness theorem
  with that translation and makes no cut-free claim.
- **Maehara:** `annex/p07/interpolation-supplement.tex:7-120` checks all rules
  of the selected cut-free equality-free LKd sheet, including all four
  eigenvariable placements and the free-variable invariant. Its remaining
  Craig dependency is reported under R2-F2, not silently skipped.
- **Church--Rosser:** `annex/p07/lambda-calculi.tex:4-124` proves parallel
  reflexivity, alpha compatibility, parallel substitution including the beta
  substitution-composition case, complete development, the diamond property,
  both simulations, the finite grid argument, and normal-form uniqueness.
- **Selected propositional cut strategy:**
  `annex/p07/arithmetic-proof-theory-supplement.tex:6-102` fixes an uppermost
  greatest-rank selection and checks identity/bottom, weakening, commuting,
  contraction, and all three compound principal pairs. It proves natural-sum
  decrease and termination without claiming every possible reduction strategy
  strongly normalizes.
- **Haken:** `thm:p07-haken-resolution-lower-bound` is now honestly
  `sketched=annex:p7.complexity.1`; the annex explicitly lists the bottleneck,
  counting, and DAG-bookkeeping omissions and does not inflate its routing
  argument into a complete lower-bound proof.

### A-117, active sheets, A-189, symbols, and source roles

- A-117 is present as `fig:p07-sequent-nd-correspondence` at
  `calculi-and-derivability-supplement.tex:169-212` and is distinct from the
  Curry--Howard and STLC/ND figures.
- A-071 now lists the four active GS5, labelled-K, display-K, and deep-S5
  sheets, and `structural-extensions.tex:209-230` splits the four adequacy/cut
  claims into source-specific cited theorems. The earlier false Wansing-only
  aggregate status and “owed” prose are gone.
- A-189 at `proof-complexity.tex:192-342` now includes the new calculi proofs,
  selected propositional and omega results, source-relative HA properties,
  all four modal adequacy theorems, and the Haken sketch. It accurately records
  the narrower MLTT theorem rather than claiming the active sheet is absent.
- The Part VII registry and compact index now contain the MLTT context/type/
  term/equality judgments, Pi/Sigma, identity type, universes, identity
  eliminator, substitutions, and multi-sorted equality-premise abbreviation
  (`handbook/generated/symbols-tables.tex:530-539`). This fixes retrieval even
  though the metatheorem gap remains R2-F3.
- Bibliography roles are now explicit: Haken's missing combinatorics remains a
  sketch backed by Haken/Beame--Pitassi; the constructive-property source is
  located to volume/chapter/section/page; and each modal adequacy claim names
  its own primary source. No cited theorem is accompanied by a contradictory
  local-proof claim.
- A-070, A-072--A-075, A-113, A-117, A-151, A-152, A-159, A-186, and A-189
  have live source surfaces. Captions and labels are distinct at source level.

## Evidence boundary

The existing strict handbook check is background supplied by the brief; I did
not rerun it. I did not compile TeX, inspect auxiliary files or a PDF, or
validate actual hyperlink destinations, bibliography rendering, counters,
floats, landscape pages, longtable continuation, proof-tree sizing, indexes,
blank versos, or overfull/underfull pages. Build, visual, administrative,
provenance, human mathematical, and final user gates remain external and are
not implied by this source/content verdict.

REJECT
