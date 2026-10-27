# Research note: P3 ch. 28.1-28.4 (packet w03a-p03-020), block 1

## Files
- Body: handbook/parts/p03/quantifier-elimination-existential-closure-and-model-w03-p03-020.tex (chapter, toc P3 28 28.1-28.4)
- Annex: handbook/annex/p03/quantifier-elimination-existential-closure-and-model-w03-p03-020.tex (21 annex items, all proofs written in full)
- Bib intake: Kruckman2020 (author-hosted lecture notes)
- Symbol intake: qftp, T_forall, T_forall-exists, L_r, chi_p, Fld_p, ACF_p, DLO^E, b/t, T_Z

## Sources read in this session
- Kruckman, Math 509 Lecture Notes: Model theory of the real numbers, final version 4 May 2020,
  https://akruckman.faculty.wesleyan.edu/files/2020/05/Lecture-Notes.pdf (author/institution page,
  Wesleyan faculty site). Read: TOC; sec. 2.2-2.3 pp. 16-22 (Def. 2.19-2.20, Ex. 2.21, Thm 2.22,
  Def. 2.23, Thm 2.24, Cor. 2.25, Rem. 2.26, Thm 2.27, Prop. 2.28, Cor. 2.29-2.30); result list of
  sec. 3 (pp. 24-46). Locators cited in reader text: sec. 2.2-2.3 pp. 16-22; Remark 2.26 p. 19;
  Theorem 2.27 p. 20; Example 2.21 p. 16. Note: Kruckman allows empty structures; the handbook
  convention is nonempty structures, and the reader text uses quantifier-free types of tuples
  instead of common substructures to cover constant-free sentences.
- Not held, no legitimate free copy found (searched 2026-10-12): Robinson, Complete Theories
  (North-Holland 1956; only catalogue records and Open Library borrow, which needs login);
  Chang-Keisler, Model Theory, 3rd ed. 1990 (and Dover 2012 reprint: commercial, Bookshare login);
  Marker, Model Theory: An Introduction, GTM 217, 2002 (Springer, paywalled); Hodges, Model Theory
  1993 ch. 8 (only the author's corrigenda PDF is held). No source-specific presentation of any of
  these is written; the reader text attributes nothing to them.

## Existing treatment found and linked (A9)
- sec:qe-categoricity-01 (restoration): QE definition, one-quantifier method, thm:dlo-qe (cited),
  DLO corollary (sketch), ACF_p theorem (cited). New proofs: thm:p03-w03-p03-020-primitive,
  -dlo-bf, -acf-qe.
- preservation-abstract-logic.tex: def:p03-existentially-closed, def:p03-model-companion,
  thm:p03-robinson-model-completeness (cited), thm:p03-field-model-completions (cited).
  New proofs: -robinson (adds items 4, 5), -acf-completion (ACF half only).
- Not listed in the packet's existing list: quantifier-elimination-existential-closure-and-model-w03-p03-022.tex
  (28.9) proves the effective one-step lemma and the syntactic DLO step with all literal cases
  (thm:p03-w03-p03-022-one-step, thm:p03-w03-p03-022-dlo-step); linked, not duplicated.
  comparison-games-and-infinitary-languages-w03-p03-038.tex def:p03-w03-p03-038-bf-system
  (finite Fraisse systems, relational); linked.
  Restoration inherited-06332-06421 (diagram tests), inherited-06432-06493 (elementary chain),
  inherited-04921-04967 (compactness) are used by label.

## Crosslinks wanted (lead)
- restoration inherited-07150-07294.tex: after thm:dlo-qe remark and after the ACF theorem, a pointer
  to thm:p03-w03-p03-020-dlo-bf and thm:p03-w03-p03-020-acf-qe (restoration is not editable here; no
  patch filed because restoration captures are hash-checked).
- preservation-abstract-logic.tex: thm:p03-robinson-model-completeness and
  thm:p03-field-model-completions could point to thm:p03-w03-p03-020-robinson and -acf-completion.

## Block 2 (N-a-012-MAP-05, ordered fields and RCF)
- Source re-read this session: Kruckman2020 PDF fetched again from the author page (same URL,
  final version 4 May 2020) and extracted with pdftotext to
  tmp/agent-scratch/w03a-w03a-p03-020-b2-author/pdf/k.txt; PDF page = printed page. Read sec. 3.1-3.4,
  pp. 24-46. Locators used: Example 3.4 p. 25; Lemmas 3.12-3.13 pp. 27-28; Definitions 3.16, 3.18 p. 30;
  Lemmas 3.20-3.21 p. 31; Theorem 3.22 pp. 32-33; Lemma 3.27, Theorem 3.28 p. 36; Theorem 3.31 pp. 37-38;
  Theorem 3.38 p. 42; Theorem 3.39 p. 43; Corollary 3.40 p. 44; Theorem 3.46 p. 46.
- Differences from Kruckman recorded in reader text: order kept as data (real closure of an ordered
  field); R(i) algebraically closed via symmetric polynomials (Laplace-style 2-adic induction) instead
  of Galois/Sylow; real closure by Zorn over ordered subfields of an algebraic closure; RCF elimination
  taken from thm:p03-w03-p03-037-qe (sign tables, no uniqueness of real closure needed).
- Uniqueness of real closures (Kruckman Thm 3.38, Sturm) is mentioned with its locator and not proved;
  the gap statement for MAP-05 does not list it; only elementary equivalence over F is proved (rcf-mc item 3).
- New labels: sec:p03-w03-p03-020-rcf, def:p03-w03-p03-020-ordered-fields, thm:p03-w03-p03-020-order-extension,
  -root-ext, -rcf-char, -real-closure, -rcf-mc, def:p03-w03-p03-020-rcf-example, -rcf-ring-diagram.
- Existing treatment reused, not duplicated: simple-nip-and-o-minimal-theories-w03-p03-037.tex
  (def:p03-w03-p03-037-rcf, thm:p03-w03-p03-037-qe, -complete, -poly-basics, -ring-language). Not in the
  packet's existing list.

## Continuation
Block 2 written: MAP-05 in body sec:p03-w03-p03-020-rcf (lines 489-709) and annex items order-extension,
root-ext, rcf-char, real-closure, rcf-mc (annex lines 888-1262). unit-compile ok.
Still open: MAP-03 general existence criterion for model companions; C01 and SRC-048-0008 C001-C006
blocked_source (Robinson 1956, Chang-Keisler 1990, Marker 2002, Hodges 1993 not reachable).
