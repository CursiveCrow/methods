# P3 24.6 Elementary amalgamation and expansion of the language (w03a-p03-006)

Packet: work/waves/w03a/packets/w03a-p03-006.json, label_tag p03-w03-p03-006.

## Scope taken from the packet

- Section 24.6 had no owned text; the gap was the missing body and annex files.
- All three source units in the packet (ED26-SRC-048-0001, -0002, -0006: Hodges 1993,
  chapters 1, 2, 6) are listed under readonly_units with owner w03-p03-001. Their
  components are not written here (rule A14). The Hodges 1993 chapter bodies are not
  held in this tree (only the contents PDF and the author's corrigenda are held), so
  nothing in the reader text presents Hodges' own sections.
- The section text is a general treatment of elementary amalgamation and language
  expansion, written from the authorities below and proved in full in the annex.

## Sources read in this session

- Online, read now: Martin Speirs, "Math 225A -- Model Theory, Lecture 19:
  Amalgamation", notes of Thomas Scanlon's Berkeley course, Autumn 2013.
  URL https://math.berkeley.edu/~scanlon/225af13lectures/20130511Lec19.pdf
  (author/course page). PDF created 2013-11-13, 7 physical pages, lecture pages
  numbered 1--6. SHA digest 283db385ea1282c1eb041b125947cac7448e788ac8f4e5f2bc9557751d65b13a.
  Locators seen: Theorem 1 (Elementary Amalgamation), statement p. 1, proof pp. 1--3;
  two examples p. 3; Definition of algebraic element/acl p. 3; Theorem 2 (disjoint
  amalgamation over an algebraically closed common set) p. 3, proof (self-described
  as a sketch) pp. 4--5; Corollary (amalgamating a family) p. 5; Corollary (realizing
  all 1-types) pp. 5--6.
  The notes say the course book is Hodges' A Shorter Model Theory; they are not the
  1993 Model Theory chapter.
- Handbook-internal results used (on the active P3 route): def:parameter-expansion,
  def:diagrams, thm:diagram-tests, thm:elementary-chain, thm:fol-compactness,
  thm:dlo-qe, lem:iso-invariance, lem:embedding-image, and the existing lemma
  thm:p03-elementary-reduct-extension with its annex annex:p3.abstract.4.

## Existing treatment found

- handbook/parts/p03/preservation-abstract-logic.tex: lemma
  thm:p03-elementary-reduct-extension (listed in packet) and the non-elementary
  failure example after it (unlabelled); Robinson joint consistency; Los--Tarski
  (cited); Craig--Robinson--Beth. The new expansion-amalgamation theorem contains the
  lemma as a special case; the body says so and does not reprove the lemma's
  application to joint consistency.
- handbook/parts/p03/maps-elementarity.tex is not on the active P3 route (the
  restoration captures carry the active definitions); not listed in the packet.

## Notes on the mathematics

- Speirs Theorem 2 assumes only that the common set is algebraically closed in one
  structure; its sketched final step (infinitely many values per coordinate gives a
  tuple avoiding a finite set) is not justified as written. The reader text proves the
  disjointness theorem when the common part is an elementary substructure of both
  structures, where the argument closes directly, and mentions the
  algebraically-closed version only as a statement in the notes. A proof of that
  version needs a covering lemma of Neumann type; open item, not written.
- The failure example for disjointness (one-element predicate) and the N/Z example for
  existential amalgamation are this treatment's own.

## Open items

- Disjoint amalgamation over an algebraically closed (not elementary) common set:
  statement only, no proof here.

## Continuation

- 2026-10-11 block 1: body (389 lines), annex (7 annexitems), intake bib
  (Speirs2013Amalgamation) and symbol intake written; unit-compile ok; check.py shows
  only the expected bib-key finding for the intake key; fused-space check clean.
- Remaining: the algebraically-closed disjoint-amalgamation version is unproved here
  (statement only). The Hodges units belong to w03-p03-001.
- Return file: spec/research/edition-2026-p03-structures-definability-and-elementary-maps-w03-p03-006-return.json
