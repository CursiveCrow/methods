# w03a-p03-063 (P3 39.10) computable presentations: provenance note

## Sources

- Selected treatment (read online this session): A. Montalban, *Computable
  Structure Theory: Within the Arithmetic*, author's draft of Part 1,
  "Compiled on June 25, 2019", https://math.berkeley.edu/~antonio/CSTpart1.pdf
  (author-hosted). Pages read: title page, contents (iii-v), preface vii-viii,
  Notation and Conventions xvii-xxi (Vocabularies and languages, p. xviii),
  Chapter I pp. 1-9 (Def. I.1, I.2; I.1.2 example p. 3; I.1.3 and Obs. I.3
  pp. 3-4; I.1.4; I.1.5 p. 4-5; Def. I.6, Obs. I.7-I.10; I.1.6-I.1.7; Lemma
  I.14; Obs. I.15; Theorem I.16 statement), pp. 39-41 (Def. III.13, Lemma
  III.15, Def. III.17, Theorem III.18 statement), pp. 123-124 (Def. VIII.1,
  Lemma VIII.2, index-set footnote p. 124).
  The version of record is Cambridge University Press / ASL, Perspectives in
  Logic, 2021 (ISBN 9781108423298); NOT read; no locator refers to it.
- Re-read in the later session (same URL, same draft "Compiled on June 25,
  2019"): title page; pp. xviii-xx (Vocabularies and languages, p. xviii);
  pp. 1-6 (Def. I.1 pp. 1-2; I.1.1 and Def. I.2 p. 2; I.1.2 example pp. 2-3;
  I.1.3 and Obs. I.3 pp. 3-4; I.1.4-I.1.5 pp. 4-5); p. 40 (Lemma III.15);
  pp. 123-124 (Def. VIII.1, Lemma VIII.2, index-set footnote p. 124).
  Every locator in the body was checked against these pages; the I.1.2
  locator was corrected from p. 3 to pp. 2-3.
- AshKnight2000 (Elsevier 2000): no held copy; WebSearch found only the
  Elsevier shop page, a commercial e-book seller, library catalogue records
  and a paywalled BSL review. No legitimate free copy of any version found.
  N-a-024 components (source-specific Ash-Knight presentation) are therefore
  blocked_source; nothing Ash-Knight-specific is written.

## Attribution map (reader text vs source)

- Computable signature: Montalban p. xviii (computable vocabulary = computable
  arity functions; index sets initial segments).
- omega-presentation, copy, computable (uniformly computable interpretations,
  tau^M): Def. I.1 pp. 1-2. Atomic diagram D(M) via effective enumeration of
  atomic formulas: Def. I.2 p. 2; Turing equivalence D(M) ~ tau^M asserted
  without proof p. 2 -> handbook gives its own proof (equivalence theorem).
- (subset omega)-presentations and D(M)(i)=0 convention: I.1.3 p. 3;
  Observation I.3 pp. 3-4 -> domain theorem part (a); finite structures
  I.1.3-I.1.5 pp. 4-5; (sqsubseteq omega)-presentations p. 4.
- Example of two computable non-computably-isomorphic presentations of
  (N, <=): I.1.2 p. 3 (Montalban uses <= and 0'; handbook uses strict < and
  the self-application set K of Part IV).
- Computably categorical: Def. VIII.1 p. 123.
- Back-and-forth property/Lemma III.15 p. 40: relationship only.
- Handbook's own (not from the source): the explicit numeric coding, the
  parsing lemma, the pullback lemma, the one-element counterexample in an
  infinite signature, the cycle structure without computable copy, the
  noncomputable presentation of (N,<).

## Continuation

- Block 1 (first session) wrote body, annex, intake bib and symbol intake.
  That run halted before the lead applied the patch requests, so the chapter
  is not on the reader route and the assessment read only the host entry in
  finite-model-theory.tex and the P4 continuation.
- Block 1 (this session): all Montalban locators re-verified (see Sources);
  I.1.2 locator fixed to pp. 2-3; symbol-intake note now points to
  sec:turing-machines-01 for pair_N (def:p04-numerical-coding does not exist);
  patch file work/waves/w03a/patches/w03a-p03-063.json rewritten with every
  anchor checked to occur exactly once: driver inputs (body, annex); host
  def:p03-computable-presentation first sentence (countably infinite,
  computable signature, def:diagrams link, literal coding, finite case);
  host pointer sentence (prerequisites, selected treatment, Ash-Knight
  disclaimer); P4 numbering/serialization cross-references; P4 Ash-Knight
  'chaps. 1--3' sentence (unverifiable locator) replaced by the selected
  treatment.
- def:p03-diagrams (parts/p03/maps-elementarity.tex) is off route; the live
  def:diagrams (restoration/inherited-06332-06421.tex) has the same content
  (literal L(M)-sentences true in M_M) and is the one linked.
- unit-compile ok (3 overfull boxes from long annexitem headings);
  find_fused_spaces clean; check.py: only own-intake bib-key findings.
- Open: N-a-024 (Ash-Knight 2000) blocked_source; WebSearch this session again
  found only publisher/retailer/catalogue/paywalled-review pages.
