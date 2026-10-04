# N-c-017 writing progress, 6 September 2026

## Manuscript work

The live presentation is handbook/parts/p09/presentations/n-c-017.tex.
This visit expanded the Bryant, Burch, Biere, and CEGAR material. McMillan's acquisition
boundary was moved from the end of the CEGAR account to its own peer
subsubsection, between Burch and Biere.

Added mathematical content:

- Boolean-function and cofactor types, the nullary function case, restriction,
  functional substitution, existential/universal abstraction, and a worked
  cofactor calculation; fixed-order graph isomorphism is distinguished from
  constant-time identifier comparison in a shared representation.
- Formula and relation denotations for Burch's relational calculus, positive
  arities, interpretation environments, the application side condition,
  parameter handling, least/greatest fixed-point semantics, finite-iteration
  justification, both BDD evaluator recurrences, complement duality, and a
  finite-domain encoding argument.
- An explicit two-bit encoding of the existing three-state example, with
  a surjective state map, transition predicate, symbolic preimage calculation,
  and least-until approximants through convergence.
- Every atomic, Boolean, next, eventually, always, until, and release clause
  of Biere's no-loop and selected-loop translations, plus the loop successor,
  empty-range conventions, endpoint cases, and the wrapped-witness branches.
- A handbook explanation of why one traversal of the reachable loop positions
  suffices for temporal witnesses, and a wrapped-until/release calculation.
- Correct guarded-program semantics, a fully defined combined abstraction
  and its preservation proofs, the minimum-size product-refinement hardness
  reduction, the coarsest complement-separating refinement proof, and exact
  and combined-policy termination arguments. The detailed correction
  provenance is in p09-n-c-017-mathematical-corrections-2026-09-06.md.
- Exact graph-size derivations for the paired-variable examples, parity
  and symmetric functions; the complete multiplication lower-bound proof;
  and the historical ALU equivalence-checking experiment.
- Nested fairness fixed points and their path characterization; a complete
  symbolic LTL tableau and truth lemma; strong/weak equivalence operators
  and coinductive proofs; deterministic-specification Büchi containment by
  fair paths and by accepting positive cycles; and typed pipeline formulas.
- General iterative squaring for B union Post_K(X), with complete least
  and greatest fixed-point proofs, typed tuple kernels, the finite-domain
  necessity, exact CTL direction, applicability limitation, and the nested
  recurring-visit construction and example.
- Ordinary-diameter quantified certification; lasso padding and a
  single-horizon product check; uniform stem/period and deterministic
  model bounds; a proved linear F/G-only bound; and a separately defined
  bounded ECTL certificate construction with branching SAT witnesses.

## Controlling source locators

Existing acquisition context is spec/research/p09-source-presentations-lot2-3.md,
N-c-017.a--e. This visit also read the following primary documents as text:

- Bryant, annotated electronic author version:
  https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf
  Section 1.1, fixed-order canonicity, and Section 4.4. The added access note in
  handbook/bib/handbook.bib distinguishes this version from IEEE pagination.
- Burch et al., Information and Computation 98(2), 1992:
  https://mcmil.net/pubs/IC92.pdf
  Sections 3--4 and Figure 2 for syntax, interpretations, placeholders,
  evaluator recursion, and Boolean-domain encoding.
- Biere et al., CMU-CS-99-101, 4 January 1999:
  https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf
  Definitions 6 and 10--15 for bounded semantics and both SAT translations.
  These remain report locators, not claims about the typeset TACAS pages.
- Clarke et al., JACM 50(5), 2003:
  https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf
  Sections 2.2, 3.1, 4.2.1--4.2.3, 4.4--6 for program semantics,
  abstraction, refinement, hardness, and combined approximation.

The worked Boolean and wrapped-lasso calculations are handbook explanations;
they are not attributed as additional figures or examples printed by a source.

## Focused review and corrections

One read-only agent checked the new mathematical passages through the end of
Biere. It found three errors in the inherited draft examples: terminal merging
must precede identical-child elimination in the full BDD tree; the two
ordering-size formulas require n >= 1 and 2n arguments; and iterative squaring
computes positive transitive closure. All three were corrected. A subsequent
focused check found both newly added worked calculations correct.

The same read-only agent subsequently checked the actual CEGAR LaTeX from
the combined-abstraction construction through the end of the presentation.
It reported no concrete mathematical defects in that bounded interval.

Later bounded mathematical readings checked the new Bryant arguments,
fairness/LTL constructions, and equivalence/containment treatments. The
positive-length reachability prose needed its F restriction at the starting
state, and the parity minterm argument needed its noncontradictory hypothesis
in the first sentence. Both were corrected. No other mathematical defects
were reported in those intervals.
The pipeline-only reading subsequently confirmed the typing and uniqueness
argument and prompted a correction from an overbroad equivalence sentence
to clause-by-clause correspondence with the path-level requirements.
The general and nested squaring paragraphs then received a bounded
mathematical reading that reported no concrete defects.
The subsequent Burch source-coverage comparison against Sections 3--10
reported no remaining material mathematical omission or incorrect source
claim. Its optional empirical clarification was incorporated: the measured
verifier operates directly on CTL rather than through the general translation.
This result is coverage evidence, not complete source fidelity or admission.
Bryant's principal-content comparison found a circular canonicity step
and the missing Apply product-size sharpness example. The replacement
suffix-variable proof and added example then passed a bounded mathematical
reading, together with the ordinary-diameter certificate and counterexample.
A different reader checked the new lasso, F/G, and ECTL results and reported
no concrete mathematical defects in that interval.
The final CEGAR principal-source comparison reported no material gap.
The Biere comparison requested its three-bit example, explicit horizon
search, compact positive experiment/implementation account, and an explicit
ECTL attribution sentence. Those additions are now in the LaTeX and were
read back directly; the example includes both its illustrative k=2
calculation and the valid k=0 self-loop witness.
The detailed coverage dispositions are appended to the existing
Biere bounds and mathematical-corrections notes.

These checks are authoring evidence only. They are not the three independent
topic-admission reviews. No whole-section acceptance, source completeness,
rights closure, compilation, or page-layout result is claimed.

## Remaining writing

- Acquisition and separate reconstruction of the revised McMillan 1993 book;
  the existing note identifies the available adjacent body as the 1992 thesis.
  The bounded 6 September author/publisher/institutional recheck is recorded
  in p09-n-c-017-mcmillan-acquisition-note.md; it did not obtain the book body.
  The user has been asked whether an authorized copy can be supplied.
- Complete independent topic reviews after the source reconstruction,
  followed by the separately required admission and final publication work.

REGISTER STATUS: OPEN
