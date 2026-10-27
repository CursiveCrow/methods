# P3 28.9 Decidability by elimination and interpretation (packet w03a-p03-022)

## Provenance

- Label tag `p03-w03-p03-022`; body `handbook/parts/p03/quantifier-elimination-existential-closure-and-model-w03-p03-022.tex`,
  annex `handbook/annex/p03/quantifier-elimination-existential-closure-and-model-w03-p03-022.tex`.
- The reader text is a general, self-contained treatment. Every proof was constructed in this
  session and is written in full in the annex. No locator from any external source is used, and
  no new bibliography key is introduced.
- Existing treatments linked rather than duplicated: `def:p03-quantifier-elimination`,
  `def:p03-one-quantifier-reduction` (outline only; the proved effective lemma is new),
  `thm:p03-dlo-qe` (cited statement; the new item gives the procedure and proof),
  `thm:p03-acfp-qe`, `tab:p03-qe-catalog`, `def:p03-imaginaries-interpretation`,
  `def:p03-imaginaries-translation`, `thm:p03-imaginaries-quotient-truth` (truth lemma reused for
  the transfer theorem), `thm:p05-interpretation-transfer` (theory-level transfer, cited TMR1953),
  `thm:p05-theoremhood-undecidable`.
- Existing treatments found that were not in the packet's list: `handbook/parts/p05/decidable-arithmetics.tex`
  (`thm:p05-presburger-qe`, cited), `handbook/parts/p05/models-and-interpretability.tex`
  (`def:p05-relative-interpretation`, `thm:p05-interpretation-transfer`),
  `handbook/parts/p03/imaginaries-and-quotient-interpretations.tex`, `handbook/parts/p10/countable-atomless.tex`,
  `handbook/parts/p03/presentations/n-a-001-01.tex` (`sec:p03-rn-dlo`),
  `handbook/restoration/inherited-07150-07294.tex` (`thm:dlo-qe`).

## Source access for SRC-049 (Baudisch, Seese, Tuschik, Weese, Model-Theoretic Logics Ch. VII)

Tried on 2026-10-11:
- Held preview `tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf`:
  contents only for Chapter VII (pp. 235-268); body absent.
- Project Euclid chapter page and PDF
  (`https://projecteuclid.org/ebooks/perspectives-in-logic/Model-Theoretic-Logics/chapter/Decidability-and-Quantifier-Elimination/pl/1235417272`,
  `.../pl/1235417272.pdf`, `https://projecteuclid.org/ebook/Download?urlid=pl/1235417272&isFullBook=false`):
  every request returns an Incapsula "Pardon Our Interruption" bot-check page. Not bypassed.
- Cambridge Core chapter page (DOI 10.1017/9781316717158.011): paywalled.
- Web search for other legitimate versions (author preprint, institutional copy): none found;
  the 1980 Akademie-Verlag monograph by the same authors is a different work and not freely reachable.
- Not used: dokumen.pub (shadow library).

Consequently no source-specific presentation of Ch. VII sections 1-3 was written.

## Continuation

Block 1 written:
- Effective QE definition, one-step lemma (proved), decision theorem (proved), Morleyization failure warning.
- Elimination steps with full proofs: DLO; T_S = successor with 0 (and Th(N;S)); atomless Boolean
  algebras; Th(Z) with divisibility predicates (Cooper-style) and transfer to N in L_N and to
  {0,1,+,<}; boundary lemma that congruence predicates are needed.
- Interpretation transfer for structures (proved via the quotient truth lemma), examples N in Z and Z
  in N (pairs), boundary warning.

Block 2 written (2026-10-12), closing MP-0(a):
- Body subsection "Algebraically closed fields" (sec:p03-w03-p03-022-acf): parametric-polynomial
  convention (links def:p03-w03-p03-037-parametric, def/thm:p03-w03-p03-037-prem), explicit recursive
  elimination step Elim for ACF (Euclidean reduction by pseudo-remainders, divisibility test
  F | G^q), correctness theorem for every algebraically closed field, decision theorem for each
  ACF_p (complete, decidable; AC only for consistency via thm:p03-w03-p03-020-closure-exists) and
  for ACF (effective QE, decidable, not complete), two worked runs, boundary warning (R and F_p).
  Annex items annex:p03-w03-p03-022-acf-step, annex:p03-w03-p03-022-acf with full proofs (factor
  theorem, splitting, root counting proved inline; infiniteness from thm:p03-w03-p03-020-field-algebra).
- Body subsection "Real closed fields" (sec:p03-w03-p03-022-rcf): theorem that the sign-table
  construction of thm:p03-w03-p03-037-qe is an algorithm, hence RCF effective QE, complete,
  decidable; Th(R) in ordered-ring and ring signatures decidable. Annex item
  annex:p03-w03-p03-022-rcf checks computability of every ingredient (atoms, T_{s,D}, reordering
  through rho, P-flat/R/Q, pseudo-remainders, Phi, termination) and the atomic-sentence decision.
  Worked trace of the sign-table step on a*x+b=0.
- Existing treatments found and linked (not in the packet's existing list):
  handbook/parts/p03/quantifier-elimination-existential-closure-and-model-w03-p03-020.tex
  (sec:p03-w03-p03-020-fields, thm:p03-w03-p03-020-acf-qe proved by the one-point test, not
  effective) and handbook/parts/p03/simple-nip-and-o-minimal-theories-w03-p03-037.tex
  (sec:p03-w03-p03-037-qe, sign-table RCF elimination). Neither is yet input in handbook/parts/p03.tex;
  the new text depends on both being integrated.
- Source re-check 2026-10-12: Project Euclid chapter page pl/1235417272 still returns a bot-check page.

Block 2 re-run (2026-10-13): the assessment that called the fields subsection conditional (body
lines 324-335, relying on thm:p03-acfp-qe and a catalog row) was made on the 2026-10-12 03:34
snapshot, before the block 2 text above was saved (05:28). Current text: ACF body 326-478, RCF body
479-533, annex 416-676. Re-verified this run: the Elim recursion and its termination measure, both
worked runs (recomputed by hand against the prem recursion of annex:p03-w03-p03-037-prem), the two
boundary counterexamples, and every cross-reference into w03-p03-020 and w03-p03-037 (labels exist,
proved= annex items present). One clarification added to def:p03-w03-p03-022-parametric: prem is
computed by the recursion proving thm:p03-w03-p03-037-prem, which also covers formal degree q-1
(def:p03-w03-p03-037-prem itself states p >= q). unit-compile ok; check.py no findings in own files;
find_fused_spaces no hits.

Remaining (MP-0, general part):
- The "quoted algorithmic bound proofs" (e.g. Fischer-Rabin lower bound, Ferrante-Rackoff, Kozen,
  Grigor'ev, Davenport-Heintz bounds in tab:p03-qe-catalog) are not proved; the reader text states
  that the procedures carry no time bound.
- An undecidability-transfer example with full proof (e.g. arithmetic interpreted in the ring of
  integers needs the four-square theorem from a held authority).

Remaining (source-specific, blocked_source): ED26-SRC-049-0007-C001, C002, C003 and the source-specific
reading of MP-0, until a legitimate copy of Ch. VII is reachable.
