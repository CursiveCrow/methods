# Packet w02-p02-041 (P2 chapter 23, sections 23.5-23.8): research and provenance note

## Existing treatment found (A9)

The packet's gaps (typed calculus with comprehension/choice/extensionality,
its general models with encoding/decoding adequacy, native sheet:sol
completeness, Church 1940 presentation/proof/bridge, written
nonaxiomatizability) are already written by packet w02-p02-040, not listed in
this packet's `existing` list:

- handbook/parts/p02/second-and-higher-order-logic-w02-p02-040.tex (1477 lines)
- handbook/annex/p02/second-and-higher-order-logic-w02-p02-040.tex (2246 lines)
- its return: spec/research/edition-2026-p02-second-and-higher-order-logic-w02-p02-040-return.json
- its driver/pointer patch requests: work/waves/w02/patches/w02-p02-040.json

These files are not yet input by handbook/parts/p02.tex or handbook/annex/p02.tex
(drivers are read-only here), which is why an on-route assessment found nothing.
No second treatment of those items was written in this packet. This packet
links them and closes one remaining mathematical dependency.

## What this packet wrote

The 040 nonaxiomatizability theorem (thm:p02-w02-p02-040-no-effective-calculus)
proves clause 3 (TA not c.e.) via thm:p04-ce-sigma-one, whose annex proof
(annex:p04-hierarchy.8) is a sketch; clauses 4 and 5 depend on clause 3.
This packet proves clauses 4 and 5 by a different route:

- Recursion terms (codes with tags 30-35) denoting partial recursive maps.
- Second-order graph conditions Def_sigma; in N under full semantics the
  conditions over Sub(rho) have exactly the graphs as solution.
- Divergence sentence Theta_rho = PA2 -> forall X (Defs -> not exists y X_rho(code, y));
  valid iff f_rho(code of rho) undefined (uses full categoricity of PA2 from 040
  and second-order isomorphism invariance, proved here).
- rd: term code -> code of Theta is primitive recursive (course-of-values and
  bounded loops of sec:arithmetic-coding-04).
- Diagonal: delta = C^1(beta; alpha) gives a contradiction if dom f_beta = Val2.
- Calculus corollary uses Sent2 primitive recursive from the 040 annex
  (second-order recognition paragraph of annex:p02-w02-p02-040-no-effective-calculus).

Imported step: Turing-machine c.e. -> partial recursive uses
thm:p04-tm-partial-recursive (cited=Kleene1952). Clauses (a), (b) are free of it.

## Sources opened in this session

- Kleene1952: source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf
  (held; 1974 seventh reprint). PDF page 386 = printed p. 376, read from the page
  image: section 69 ends with Theorem XXX (partial recursive, computable and 1/1
  computable functions coextensive), and section 70 begins. Text layer of PDF
  page 383 = printed p. 373 shows Theorem XXIX (not cited).
- Church1940 not reopened (no Church locator written in this packet).
- Not held: Henkin1950, Andrews2002, Shapiro1991 (checked against
  spec/coverage/edition-2026/held-sources.json).

## Handbook files read

work/waves/w02/packets/w02-p02-041.json; 040 body lines 1-28, 1335-1477 and
annex lines 1-30, 2120-2246; 040 note and return; restoration
inherited-12262-12289, 12290-12355 (lines 1-70), 09328-09438 (lines 1-200),
07678-07752 (lines 1-60), 07753-07843 (lines 1-60); parts/p02/pa2-definition.tex;
parts/p04/universal-reductions.tex lines 1-200 and its annex items 2-6, 9;
parts/p04/machines-effective-procedures-supplement.tex lines 1-101;
parts/p04/decision-problems-and-arithmetical-hierarchy.tex (headers) and annex
items 7-8.

## Decisions

- Tags 30-35 for recursion-term codes: unused by sec:arithmetic-coding-04 (0-18)
  and by 040's second-order tags (15-18).
- Reduction function named rd (040 uses r); graph written Gr (Gamma is a premise
  set in the supplement); conditions Def; sentence Theta.
- Terms admit arity 0 so that Z_0 and k = 0 primitive recursion of
  sec:turing-machines-02 have terms; coverage (a) needs only that the
  term-denoted class is closed, not equality with the handbook class.
- \Pow is restricted to restoration scope; \mathcal P used instead.

## Block 2 (relational decoding induction; Church presentation gaps)

Written:
- Body sec:p02-w02-p02-041-decoding (body lines 312-520): def -collapse,
  lemmas -henkin-coincidence, -tagging, theorem -collapse, corollary
  -adequacy-route, example -collapse-example, warning -collapse-limits.
  Annex sec:annex-p02-w02-p02-041-decoding (annex lines 391-903) with all cases
  (atomic incidence, predicate-constant, equality, each connective, object and
  relation quantifiers) for both the tagging encoding (annex:p2.hol.7) and the
  extensional collapse (annex:p2.hol.8), plus coincidence for Henkin semantics
  (used for the schema clause: instances are sentences) and both adequacy
  directions through thm:fol-soundness, cor:fol-completeness-countable and
  thm:p02-many-sorted-translation.  No choice is used in the collapse.
- Body sec:p02-w02-p02-041-church-supplement (body lines 522-651): Schoenfinkel
  attribution (p. 57 n. 6), p. 58 parenthesis examples, p. 59 bracket example
  with both expansion stages (balance and truth-table agreement of the
  transcription checked by script), p. 61 formal/syntactical theorems and
  ambiguity of "theorem", p. 62 turnstile vs Russell/Frege assertion sign,
  predecessor remark attributed to Axioms 7 and 8 jointly (p. 59 with p. 61)
  and marked as an unproved source claim, theorem that 30^o is not a theorem.
  Annex annex:p02-w02-p02-041-church-30 (annex lines 905-985): standard model
  S(N,c); 1_{o'} = 3_{o'} (every map on a 2-element set equals its third
  iterate), 1_{o''} != 3_{o''} (3-cycle on D_{o'}, 256 elements).
- Off-route labels replaced: def:p02-fol-satisfaction, thm:p02-fol-*-coincidence,
  -nd-soundness, -completeness-countable are not input by the drivers; used
  sec:fol-semantics-01/02, thm:fol-soundness, cor:fol-completeness-countable.
- Patch requests: work/waves/w02/patches/w02-p02-041.json (driver inputs after
  the 040 inputs; hol.8 line 115-116 pointer; hol.7 pointer; 040 body lines
  162-164 attribution correction; 040 body line 460 pointer to the 30^o proof).

Church1940 pages opened this block (held scan, PDF page = printed page - 54):
pp. 57 (n. 6), 58, 59, 60 (section 4 heading), 61, 62, 66; the p. 58 and p. 59
formulas were read from rendered page images.

## Block 3 (predecessor attribution: explicit supersession)

Assessment item: 040 body lines 162-164 ground the p. 59 predecessor remark in
the independence of Axiom 8; the source (held scan, PDF p. 5 = printed p. 59,
re-read this session) derives it from the independence of the axiom of
infinity of section 4, and printed p. 61 (PDF p. 7, re-read) says Axioms 7 and
8 together have the effect of that axiom and gives separate independence
interpretations for 7 (one individual) and 8 (finitely many, more than one).

Written: def:p02-w02-p02-041-church-predecessor (body lines 617-635) now names
the paragraph after def:p02-w02-p02-040-church-abbrev, says its attribution
does not match the source and that the warning's attribution supersedes it,
and states that 040 clause 3 proves only the separate independence results;
the step to non-definability is the unproved source claim.

Coordination: patch request 5 (correct the 040 sentence) is still the
preferred fix; patch request 7 deletes the 041 supersession sentence and must
be applied in the same change as patch 5, never alone.

## Continuation

Written: block 1 (sec:p02-w02-p02-041-direct and its annex), block 2 and block 3 (above).
unit-compile ok; check.py shows no finding for these files; find_fused_spaces no hits.

Remaining, in priority order:
1. Driver insertion of 040 and 041 files and the host patches (lead);
   patches 5 and 7 of w02-p02-041.json only together.
2. D-P9-001-GOAL-03: Turing-machine to partial-recursive step cited
   (thm:p04-tm-partial-recursive); proof belongs in P4 files not owned here.
3. N-a-071-S01-PROOF items from 040: (i) 26^iota', 26^iota'', ... from
   1-6^alpha and 8 without Axiom 7 (p. 64); (ii) n. 12 replacement results
   (p. 66); (iii) section 8 schema only under hypothesis (H).
4. The non-definability of the same-type predecessor without descriptions
   (p. 59) is recorded as an unproved source claim; no proof written.
5. N-a-071-S02/S03/S04: blocked_source (Henkin1950, Andrews2002, Shapiro1991).
