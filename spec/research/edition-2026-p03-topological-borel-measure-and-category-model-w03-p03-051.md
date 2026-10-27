# w03a-p03-051 (P3 ch. 38, sections 38.1-38.3): research note

## Sources read in this session

- Held: `source/references/p03-topological-models/ten-cate-gabelaia-sustretov-2006-institutional.pdf`
  (key TenCateGabelaiaSustretov2006TopologyDraft; October 2006 author draft).
  Read pp. 7-14 and Appendix A pp. 45-47 and the reference list (p. 42).
  Locators verified: Theorem 2.3 p. 9; Definition 13 p. 11; Table 1 p. 12;
  Theorem 2.9 p. 12 (the computed task said p. 11; the draft's own page
  footer puts Theorem 2.9 on p. 12, Definition 13 on p. 11).
  Theorem 2.9 is stated without proof, attributed to "[17, page 8]" =
  Flum and Ziegler, Topological Model Theory, LNM 769, Springer 1980.
  The converse half of Theorem 2.3 is also stated without proof (cites [17]).
- Ziegler, Ch. XV of Model-Theoretic Logics (SRC-049): only the pageplace
  preview is held. Online attempts on 2026-10-11: web search for a free copy
  of the chapter or of Flum-Ziegler LNM 769 found only Cambridge Core /
  Springer paywalled listings; Project Euclid (Perspectives in Logic) returned
  a bot-check page, which was not bypassed. No legitimate copy reached.

## What was written

Body `handbook/parts/p03/topological-borel-measure-and-category-model-w03-p03-051.tex`,
annex `handbook/annex/p03/topological-borel-measure-and-category-model-w03-p03-051.tex`.

- Two-sorted downward LS with countable parameter sets (via tagged one-sorted
  encoding + thm:downward-ls (restoration capture, on route)).
- Trace lemma: elementary piece -> trace basis -> generated topology, with
  L_t-agreement on parameters (via thm:p03-topological-basis); generated
  topology = subspace topology when the parameter opens include a basis.
- Real line vs a countable X_0 containing Q: L_t-equivalent, X_0 disconnected.
- Non-expressibility of connectedness (sentence and theory level, and its
  failure), relative to K_R and to any L_t-theory true in R.
- Compactness corollary ([0,1] vs countable Z_0) -- this corollary is the
  handbook's own; not taken from the draft.
- Conn separates the basis from its topology; modal pointwise corollary.
- Method entry, worked example, limitations warning.

The proof is new reasoning built from route theorems; it is not presented
as Flum-Ziegler's or Ziegler's argument.

## Not written

- Ziegler Ch. XV sections 1-6 (C001-C006): source not held (ACQ-2026-10-0471).
- L_t interpolation (38.2 / C002), characterization of L_t-definable L_2
  formulas (converse of basis invariance), Beth-type definability for L_t:
  no held or reachable source supplies a proof; the draft only states the
  converse and cites the L_2 failure of interpolation with a sketch.

## Continuation

Block 1 written: the connectedness/compactness non-expressibility chapter
(all labels p03-w03-p03-051-*). Open for later blocks only if a source is
acquired: Ziegler Ch. XV body; Flum-Ziegler LNM 769 (for interpolation, the
basis-invariance converse and Beth definability for L_t).

Session 2026-10-12: the computed gap for 38.3 (L_t non-definability of
connectedness from thm:p03-topological-basis, thm:p03-topological-compactness-ls
and the draft's Thm 2.9) is the material already in the owned files; it was
re-checked (proofs read through, locators re-verified in the held PDF: Thm 2.3
p. 9, Def. 13 p. 11, Table 1 and Thm 2.9 p. 12). One reader-text fix: "author
draft" -> "draft". New online attempt for Ziegler Ch. XV: Cambridge Core
abstract page fetched (metadata and purchase block only); search found only
paywalled or commercial copies. Still open: C001, C002, C004-C006 (source not
held), and within C003 Ziegler's Sec. 3 itself, the basis-invariance converse
and interpolation/Beth definability for L_t.

## Author correction, 2026-10-26

The rational interval basis now explicitly includes the empty set, as the
standing carrier convention requires. The countability argument and free
open-parameter wording were adjusted accordingly. The concluding preservation
claim now says every L_t sentence, rather than every informal local condition.
The symbol intake records the corrected basis and valid CSV quoting.

The complete body and its seven annex proofs were read for this correction.
The scoped TeX Live build (pdflatex, biber, pdflatex twice) succeeded, producing
15 pages; its one overfull warning is in the bibliography. The changed real-line
page was visually inspected. External references in the isolated unit require
the complete book. This is an author correction, not independent acceptance or
source-admission certification; no source requirement or ledger status changed.

