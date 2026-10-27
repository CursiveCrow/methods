# Packet w03a-p03-048 (P3 ch. 37; sections 37.2, 37.3, 37.4) - research note

## Provenance

- Barwise 1974, "Axioms for abstract model theory", Annals of Mathematical Logic 7 (1974) 221-265.
  Held: source/references/acq-r1-ACQ-2026-10-0032/ACQ-2026-10-0032.pdf (publisher version of record, 45 pp.).
  Read this session: pp. 221-222 (preface, Part I section 1 opening), 228-238 (sections 3-8 via text extraction),
  241-247 (sections 9-10), 248-260 (Part II sections 1-4 opening). Page images checked for pp. 244-246, 249-250, 255-256, 258.
  Re-read this session (block 1 rerun, 2026-10-12): pp. 234-235 (axioms, Example 7.1), 243-247 (I.10 incl. 10.4-10.10, beth indexing
  p. 246 from page image), 248, 251-253 (1.4, 1.6, bounded), 257-259 (3.1-3.4, p. 259 remark; p. 257 from page image), 264-265 (refs).
  Handbook key used: Barwise1974Axioms (existing in handbook.bib); packet source id Barwise1974Abstract is the same work.
- SRC-049 (Model-Theoretic Logics) held preview: tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf.
  The reading text ends inside Ch. II section 7.2 (Proposition 7.2.5, p. ~72). Ch. III (Flum, "Characterizing Logics") begins p. 77
  per the contents page; no page of Ch. III sections 1-5 is in the held preview.

## Findings recorded in the reader text (source-fidelity issues)

1. Thm 1.2 (iii)=>(i), p. 250: printed sentence lacks "U empty or has a largest element"; a model of type >= omega+1 gives infinite U.
2. Thm 1.4(2), p. 251: printed clause only requires predecessors of x to lie below x in an indexed model; the order on them must
   also agree, otherwise (W, prec) need not be well-ordered.
3. Thm 2.2 sentence, p. 255: pairing coding gives no subtuple preservation, no equality clause, no base E-pair; both copies share
   symbols (constants). Reconstruction: positions S, ternary E, renamed second copy.
4. Thm 3.2 sentence, p. 258: same coding; reconstruction with positions S, levels H, renamed copy.
5. sigma-formulas, p. 246 with Def 10.4 p. 245: rank-0 atomic sentences contain no function symbol of positive arity, so sigma never
   records function graphs; Thm 10.7 fails as printed for L = {V, f} (identity vs successor on omega, forall x f(x)=x has rank 2).
   Reconstruction: tau^m formulas with graph literals.
6. Sigma-1-1 definition, p. 249, requires gamma identity except at V; Barwise's own proofs (1.4) use renamed order symbols.
   Reading adopted: any one-one 0-term morphism. "Bounded by beta" read strictly (forced by the proof of 3.2).
7. Def 10.1: nonempty I read in (as for I_beta of 10.5).

## Existing treatments found

- handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02c-p02-003.tex lines 228-525 and its annex
  (annex:p02-w02c-p02-003-b74-lindstrom): Barwise 1974 axioms (def:p02-w02c-p02-003-b74-languages, -b74-logic), Cor. 3.4 proved by a
  non-Karp route, comparison warning (incl. p. 259 remark). NOT routed by any driver (handbook/parts/p02.tex has no input for it).
  This chapter cites those definitions for the axioms instead of restating them; routing is the lead's decision.
- handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex: Marker-based partial isomorphism systems,
  countable back and forth, Karp's theorem, (Q,<)/(R,<) example. Cross-referenced; notions differ for function symbols.
- handbook/parts/p03/abstract-model-theory-and-characterization-of-w03-p03-047.tex: Barwise 1985 Ch. I and Ebbinghaus Ch. II
  (owner of ED26-SRC-049-0002); not duplicated here. Cross-referenced thm:p03-w03-p03-047-q0-omega.
- Host thm:p03-lindstrom (preservation-abstract-logic.tex 424-472) with annex:p3.abstract.3 (editorial-proofs.tex 358-558).

## Continuation

Block 1 (rerun 2026-10-12) added, in the owned body/annex files:
- sec:p03-w03-p03-048-infinitary: def:...-infinitary (Barwise beth indexing beth_0(lambda)=lambda, beth_omega=aleph_0; L_kappa-omega by
  subformula count, p. 246; bounded, p. 252); thm:...-levels-transfinite (J_beta, tau^beta, count <= beth_{beta+1}(aleph_0) < kappa);
  thm:...-lopez-escobar (cited=Barwise1974Axioms: Barwise attributes wo(L_lambda-omega) <= (2^lambda)^+ to Lopez-Escobar and refers to
  Barwise-Kunen [5]; not proved in the paper, p. 257); thm:...-karp-kappa (3.2 and 3.3, <=, proved); thm:...-kappa-forward (3.2 and 3.3,
  =>, proved from the cited bound and the infinitary Karp lemma). fo-karp lemma extended to L_infty-omega.
- Host bridge: thm:...-host-karp (Barwise 2.2 in the regular relational package) and thm:...-host-route (thm:p03-lindstrom via
  Karp route; compactness applied directly with singleton predicates P_i in place of 1.4/1.2 indexed unions). Alternative (a) not
  transferable to host (needs indexed unions) - stated in reader text.
- Axioms paragraph expanded (syntax functor to classes, semantics relation, relativization Example 7.1 p. 235); the exact definitions of
  languages / interpretations / category / axioms remain by \cref to def:p02-w02c-p02-003-b74-languages and -b74-logic (w02c file,
  pending integration, unrouted). Lead decision: route that file, or authorize restating the definitions here.

Remaining:
- N-a-061-S01-*: Lindstrom 1969 (Theoria) not held; not searched online this block.
- N-a-061-S03-*: EFT 1994 2nd ed. Ch. XIII not held; not searched online this block.
- ED26-SRC-049-0003-C001..C005: Flum Ch. III not in held preview.
- Barwise Thm 10.3/10.7 (Karp's theorem for L_infty-omega with Barwise's sigma and rank) are not presented; the route uses tau^beta instead.

## Author correction on 26 October 2026

The chapter now contains its own definitions of Barwise languages, closed-term
interpretations and their composition, partial structures, pull-backs,
invertibility, the five category conditions, and the three logic axioms. Their
labels are `def:p03-w03-p03-048-b74-languages` and
`def:p03-w03-p03-048-b74-logic`. The definitions were checked against the held
1974 primary paper, printed pages 228--231 and 233--235, and against the
existing P2 reconstruction. Body and annex references use the local labels.

This removes the two-definition dependency on the unrouted w02c-p02-003 file;
it does not complete or admit that separate P2 source presentation. The
additional Boolean, quantifier and finite-occurrence hypotheses remain separate
from the three axioms, in the existing standing-hypotheses convention. Symbol
intake records were added for the local definitions. Other source and proof
boundaries recorded above remain open. This is an author correction, not
independent admission.
