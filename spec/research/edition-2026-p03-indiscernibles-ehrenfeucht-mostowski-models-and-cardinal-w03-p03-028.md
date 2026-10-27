# Research note: P3 chapter 31 (packet w03a-p03-028), indiscernibles and EM models

Label tag `p03-w03-p03-028`.  Body
`handbook/parts/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-028.tex`,
annex `handbook/annex/p03/indiscernibles-ehrenfeucht-mostowski-models-and-cardinal-w03-p03-028.tex`.
Neither file is input by a driver yet; see the patch file
`work/waves/w03a/patches/w03a-p03-028.json`.

## Sources opened in this session

- Ramsey 1930 (held): `source/references/acq-r1-ACQ-2026-10-0415/ramsey-1930-on-a-problem-of-formal-logic.pdf`,
  PDF pages 1-7 = printed pp. 264-270, read as page images and OCR text.
  Locators used: Theorem A statement p. 264, proof pp. 264-266; notation
  conventions p. 266; Theorems B and C p. 267; f/g recursion p. 267; proof of
  C pp. 268-269; h recursion and deduction of B p. 269; remarks on the size of
  m0 pp. 267 and 269 (2^{n(n-1)/2} versus n!).  Section II (logic) begins
  p. 270 and is not used.
- Ehrenfeucht-Mostowski 1956, read online:
  url https://www.impan.pl/shop/en/publication/transaction/download/product/94255
  (linked as "Free download under CC-BY license" from the IMPAN article page
  https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/43/1/94255/models-of-axiomatic-theories-admitting-automorphisms).
  Version: scan of the published printing, Fund. Math. 43 (1956) pp. 50-68
  (version of record; 10 PDF sheets, two printed pages per sheet).  Pages read
  as images: 50-51, 56-65.  Not read: 52-55, 66-68.  Saved under
  `tmp/agent-scratch/w03a-w03a-p03-028-b1-author/em/` (scratch only, not a
  held-source registration; the lead may register it).
  Locators used: Lemma 4.1, 4.2, Theorem 4.3 and G_M notation p. 56; Theorem
  5.1 (Ramsey, cited as "[8], theorem A on p. 384") p. 57; Lemmas 5.2-5.4
  pp. 57-59; "strongly contains" p. 59; Theorem 5.5 p. 60; Theorem 5.6
  p. 60 with proof pp. 60-62 (Ramsey applied to Y^{2n+1} with 2^s classes,
  p. 62; reduction to open theories by Theorems 1.1 and 4.2, p. 62);
  counterexample (transitive irreflexive connected pi) pp. 62-63; G(X,<)
  and Theorem 5.7 p. 63, proof pp. 63-65 (partition of Y^n into 2^s sets and
  Theorem 5.1, pp. 64-65).
- Morley 1965 (held): `source/references/p03-morley1965/morley1965-categoricity-in-power.pdf`,
  pdftotext of pp. 525-529.  Locators: Theorem 3.1 p. 525; Theorem 3.2
  pp. 525-526 (one arity N after embedding X in an order without maximum,
  2^m classes); Theorem 3.3 p. 526; Theorems 3.4-3.6 p. 527.  Morley's
  reference [12] (p. 538) gives Ramsey as Proc. LMS (2) 30 (1929) 291-310,
  which does not match the printed article (1930, pp. 264-286).
- Ehrenfeucht-Mostowski 1956 is now held:
  `source/references/acq-r1-ACQ-2026-10-0116/ACQ-2026-10-0116.pdf` (scan, no
  text layer).  Re-read in the session of 2026-10-12 as page images, sheets
  4-8 (pp. 56-65): Theorem 5.1 p. 57 (cites Ramsey "theorem A on p. 384");
  Theorem 5.5 and 5.6 p. 60; arbitrary ordering of Y "nothing in common
  with relations definable in S" p. 61; Y^{2n+1}, 2^s classes p. 61,
  Theorem 5.1 applied p. 62; counterexample pp. 62-63; Theorem 5.7 p. 63;
  Y^n into 2^s sets and Theorem 5.1 p. 64.
- Shelah 1971 (Israel J. Math. 9, 473-487), read online 2026-10-12 from
  the author's archive https://shelah.logic.at/files/95465/12.pdf (linked
  from https://shelah.logic.at/papers/12/ as the published version, Sh:12,
  15 pages, printed pagination 473-487).  pdftotext of all pages.  Locators
  used: Theorem 0.1 pp. 473-474; definition of unstable p. 474; Lemma 1.1
  p. 475 (quoted from Shelah [9] Theorem 2.13, not proved there);
  Assumption 2 p. 475; Lemma 1.2 and Definition 1.1 p. 476; Definitions
  2.1-2.2 and Theorem 2.2 pp. 477-481 (Definition 2.4, club filter, p. 478);
  Theorem 3.1 p. 481, Lemma 3.2 p. 482; Theorem 4.1 and Lemma 4.2 pp.
  484-486.  Saved under tmp/agent-scratch/w03a-w03a-p03-028-b1-author/sh12/.
- Ramsey 1930 and Morley 1965 re-checked 2026-10-12 by pdftotext (Theorem A
  p. 264; Morley Theorem 3.1 p. 525, 3.3 p. 526).
- Hodges 1993 body: not held (only the author corrigenda are held); not
  used.  No legitimate free copy of the book body is known.

## Decisions

- The partition theorem the construction uses is Ramsey's Theorem A (EM 1956
  Theorem 5.1; Morley 1965 Theorem 3.1).  The classification-theory host says
  "finite Ramsey"; a patch request replaces both phrases.  Theorem B is
  proved too and recorded as an alternative route
  (def:p03-w03-p03-028-finite-route).
- h(r,n,mu)=n for n<r or mu=1 is an added totality clause, flagged in the
  reader text as not in Ramsey's text.
- Theorem C is stated with the side condition k+1>=r when n=1 (Ramsey's
  recursion side condition); the reader text explains the trivial case.
- EM 1956 Theorem 5.7 and 5.6 are proved through the Morley-style
  Skolem-hull argument (written out in the annex for languages of any
  cardinality), not through EM's own section 3 model M(X,I).  The reader
  text says so.
- Existing treatments extended, not duplicated: def:p03-order-indiscernibles,
  thm:p03-ehrenfeucht-mostowski, blueprint paragraph and thm:p03-em-models
  (classification-theory.tex), thm:p03-morley-ramsey-em and its annex
  (n-a-006-01), thm:p06-infinite-ramsey.  The finite-satisfiability lemma
  overlaps the second sentence of thm:p03-morley-ramsey-em; it is kept as
  the precise statement of the Ramsey application (single arity, padding),
  and the text links the two.
- Existing treatment not listed in the packet: thm:p06-infinite-ramsey and
  def:p06-partition-arrow (handbook/parts/p06/infinitary-combinatorics.tex
  120-141); thm:p03-morley-ramsey-em / annex:p3.morley.ramsey-em.

## Continuation

Block 1, session 2 (2026-10-12), closing the assessed gaps for GOAL-03 /
C01 / MAP-02:
- 31.1: Theorem A now linked to thm:p03-morley-ramsey-em (Morley Theorem
  3.1 p. 525) with the difference between the two proofs stated; new
  paragraph after the finite-satisfiability lemma names the partition
  theorem used (Theorem A, arity N, 2^q classes) and EM's application with
  locators (pp. 61-62, 64).
- 31.4: Shelah 1971 proof decomposed with locators (four steps) and the
  proofboundary rewritten with located citations; the only route step
  Shelah uses is Lemma 1.2 (EM models with ordered skeleton).
- Patch file rewritten: host sentences 238-241 and 276-283 replaced with
  located, per-step citations and links (Marker2002 and Hodges1993 not
  kept because unlocatable: not held); new patch on n-a-006-01 linking
  thm:p03-morley-ramsey-em to Ramsey 1930 and chapter 31.

Open (unchanged):
1. MAP-03 at Hodges's scope (11.2, p. 547 correction): Hodges body not held.
2. EM 1956 C01: pp. 52-55 (sections 1-3), Lemmas 4.1-4.2/Theorem 4.3
   proofs, Lemmas 5.2-5.5 in EM's own formulation, pp. 66-68 are not
   reconstructed (source now held).
3. MAP-05: the nonisomorphic-model application is now decomposed with
   Shelah locators but not proved (Lemma 1.1 depends on Shelah's
   Stability paper Theorem 2.13; Theorem 2.2 and Lemma 4.2 not proved).
4. MAP-04, ED26-SRC-048-0011-C001..C006: Hodges 1993 chapter 11 body not held.

Block 2 (2026-10-12), EM 1956 reconstruction (C01 / MP-0 for 31.1-31.4):
- Source read this session: held scan
  source/references/acq-r1-ACQ-2026-10-0116/ACQ-2026-10-0116.pdf, rendered
  with pdftoppm at 200 dpi (tmp/agent-scratch/w03a-w03a-p03-028-b2-author/),
  every printed page 50-68 read as page images, including the reference
  list p. 68 (Ramsey entry given as Proc. LMS (2) 30 (1929) 338-384).
- Body: four new subsections of 31.3 (body lines 399-903):
  sec:p03-w03-p03-028-em1956 (intro pp. 50-51; sections 1-3: syntax
  convention, pseudo-models, Theorem 2.1, theorems = valid matrices,
  Theorem 1.1, S*(X)/S(X,I)/M(X,I), Lemmas 3.1-3.6, complete-set existence,
  Theorems 3.7-3.8, warning on quantified matrices),
  sec:p03-w03-p03-028-em-automorphisms (automorphisms, Lemmas 4.1-4.2,
  Theorem 4.3, example Z/3), sec:p03-w03-p03-028-em-induced (Theorem 5.1,
  Lemmas 5.2-5.4, Theorem 5.5, example of a non-inducing transposition),
  sec:p03-w03-p03-028-em-original (finite steps of 5.6 and 5.7 in EM's form,
  reduction to open theories, Theorem 6.1).  Route items 4 and 5 of
  def:p03-w03-p03-028-route now link the new results; route item 1 records
  the p. 68 reference-list entry.
- Annex: one annexitem per new result (annex lines 502-1207); the annex
  items for em-56 and em-57 now also carry the article's own proofs.
- Decisions: T(S) read as ND_FOL derivability of universal closures (stated
  in def:p03-w03-p03-028-em-syntax); "complete" I read as containing all its
  theorems (stated after def:p03-w03-p03-028-em-mxi, justified by the use in
  Lemmas 3.2-3.6); side condition X nonempty or a constant in S for M(X,I)
  (stated); Theorem 1.1 proved by Skolemization + completeness under AC,
  the body says EM state it without that hypothesis and derive it from the
  second epsilon-theorem (Hilbert-Bernays, not held, not reconstructed);
  the 5.6 proof's "2n+1 variables" for 2n+2 constants is noted; the
  psi-bar / fictitious-variable step of 5.7 is replaced by Theorem 3.8 at
  the shifted valuation and the text says so.
- Live references only: thm:fol-completeness, thm:fol-soundness,
  thm:prenex-normal-form, thm:skolem-equisatisfiable,
  lem:new-constant-elimination, lem:transfinite-lindenbaum, lem:prop-mcs with
  sec:fol-metatheory-01, thm:fol-substitution (the p02 labels of
  first-order-completeness.tex / first-order-normal-forms.tex are not on the
  static route and were dangling).
- Checks: unit-compile ok; check.py --tree shows no finding in owned files;
  find_fused_spaces clean.

Open after block 2:
1. Theorem 1.1 without the axiom of choice (EM's route via the second
   epsilon-theorem, Hilbert-Bernays vol. II pp. 18-33): not held.
2. MAP-03 at Hodges's scope, MAP-04, ED26-SRC-048-0011-C001..C006: Hodges
   1993 chapter 11 body not held.
3. MAP-05: Shelah 1971 steps cited, not proved (unchanged).

Block 2, session 2 (2026-10-13), MAP-05 nonisomorphic-model application:
- Guard G1 (spec/research/edition-2026-authoring-batch-intake-13.json
  changed): not touched in this session; `git status` shows it unmodified in
  the working tree now, so the earlier change was made by another process.
  Guard G3/G4: `tools/check.py --tree handbook` rerun with a 1500 s limit,
  finished in about 2.5 min; no finding names a file of this packet (the
  remaining findings are in other packets' files).
- Body: new subsection sec:p03-w03-p03-028-two-models in 31.4 (lemma
  thm:p03-w03-p03-028-thin-tuples, lemma thm:p03-w03-p03-028-thick, theorem
  thm:p03-w03-p03-028-two-models, example def:p03-w03-p03-028-dlo-example,
  warning def:p03-w03-p03-028-two-models-limits); Shelah material now under
  sec:p03-w03-p03-028-shelah; proofboundary sentence adjusted.
- Annex: three annexitems at the end of the annex file (thin-tuples, thick,
  two-models), all proofs written out; inputs are thm:p03-morley-ramsey-em,
  the chapter's coherent/realize/elementary lemmas, thm:fol-compactness,
  thm:downward-ls, lem:iso-invariance, def:p03-stability.
- Decision: instability is taken in the handbook's sense
  (def:p03-stability: some formula has the order property); Shelah's
  type-counting definition reaches it only through his Lemma 1.1, cited.
- Hodges 1993 body: searched again 2026-10-13 (web search for an open copy
  of Model Theory, CUP 1993, chapter 11): only retail/Cambridge Core pages;
  no legitimate free copy of any version found.

Open after this session:
1. Theorem 1.1 of EM 1956 without the axiom of choice (second epsilon
   theorem, Hilbert-Bernays, not held).
2. MAP-03 at Hodges's scope, MAP-04, ED26-SRC-048-0011-C001..C006: Hodges
   1993 chapter 11 body not held.
3. MAP-05: the count 2^kappa (Shelah 1971 Lemma 1.1, Theorem 2.2,
   Lemmas 3.2 and 4.2) is cited, not proved; the route-level application
   (two nonisomorphic models in each uncountable kappa, countable language)
   is proved.


## Author source correction, 26 October 2026

Checked Shelah, *The number of non-isomorphic models of an unstable
first-order theory* (1971), printed p. 474, against the rendered author-archive
copy at <https://shelah.logic.at/files/95465/12.pdf>. The printed bound in the
definition of instability is `|A| <= lambda`, not the strict inequality
suggested by OCR. The body now says “at most lambda,” with lambda infinite
as stipulated by the source's notation. This matters already at aleph-zero.

The former statement that the counting-to-order bridge is not proved in the
handbook is superseded by packet 032's stability spectrum theorem. Updated
both proof-boundary passages to link that argument. The contradictory-order
combinatorics and the full nonisomorphism argument for `2^lambda` models remain
cited dependencies; this correction does not assert those proofs have been
written here. The unavailable exact Hodges chapter and choice-free EM route
remain open. This is an author correction, not independent admission.
