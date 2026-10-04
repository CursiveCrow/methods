# Packet w02-p02-039 (P2, section 22.8): L_{omega1 omega} full-treatment links and L_{infty omega} separation

Date: 2026-10-04. Label tag: `p02-w02-p02-039`.

## Inputs read in this session

- Packet `work/waves/w02/packets/w02-p02-039.json` (units ED26-REQ-D-P3-009-01, ED26-REQ-N-a-060-01/02/03).
- `handbook/parts/p02/variants.tex` 325-520 (sec:p02-infinitary-generalized, def:p02-lomega-one-omega, thm:p02-lomega-one-omega-calibration, def:p02-infinitary-derivation, thm:p02-karp-completeness, def:p02-generalized-quantifier, tab:p02-fol-extensions).
- `handbook/parts/p03/preservation-abstract-logic.tex` 365-420 (sec:p03-abstract-landmarks, def:p03-q-one, thm:p03-keisler-q-one).
- `handbook/parts/p08/sources/src-025-501.tex` 425-500 (def:p08-bvb501-potential-isomorphism, thm:p08-bvb501-potential-isomorphism, Q/R comparison) and its annex `handbook/annex/p08/sources/src-025-501.tex` 425-500 (annex:p08.src025501.potential).
- `handbook/parts/p03/presentations/n-a-004-02.tex` 70-240 (def:p03-morley-infinitary, thm:p03-morley-borel-truth, sec:p03-morley-scott, thm:p03-morley-scott-sentence, thm:p03-morley-approximant-isomorphism).
- `handbook/parts/p14/directory-of-logical-systems.tex` 168-190 (entry:p14-directory-infinitary); `handbook/parts/p02/further-reading.tex` 20-30.
- Held: `source/references/acq-r1-ACQ-2026-10-0497/schwichtenberg-1977-proof-theory-applications-cut-elimination.pdf` (whole 1977 Handbook of Mathematical Logic, eighth impression 1993, 1977 pagination; held-sources entry with bibkey Schwichtenberg1977). Read in this session: TOC; ch. A.1 (Barwise) section 5.4-5.5, pp. 43-45; ch. A.7 (Makkai) pp. 233-240, 244-245, 249-251, 253-254, 275-276, 281 (references). PDF page 292 = printed p. 276 viewed as image to confirm Theorem 8.11 wording (Sigma^1_1 over L_{omega1 omega}, union of aleph_1 L_{omega1 omega}-elementary classes). Chapter spans verified: A.1 pp. 5-46 (p. 6 header, A.2 starts p. 47); A.7 pp. 233-281 (A.8 starts p. 283).
- `spec/coverage/edition-2026/held-sources.json`: no entry for Karp1964, Scott1965, Mostowski1957, Lindstrom1966 or Keisler1970 (searched by key and by author name).

## What was written

- Body `handbook/parts/p02/many-sorted-and-alternative-first-order-w02-p02-039.tex` (263 lines): sec:p02-w02-p02-039-lomega-treatments with notation bridge (def:p02-w02-p02-039-notation), the claim-to-treatment table (tab:p02-w02-p02-039-treatments) with \cref links to the p03 and p08 fuller treatments, a written verification of the compactness counterexample, two lemmas and a theorem proving L_{omega1 omega} is a proper fragment of L_{infty omega} over a single binary relation (counting argument via ordinal rigidity under potential isomorphism), a worked example and a warning against identification with unrestricted infinitary languages.
- Annex `handbook/annex/p02/many-sorted-and-alternative-first-order-w02-p02-039.tex` (196 lines): full proofs annex:p02-w02-p02-039-formula-set, annex:p02-w02-p02-039-rigid, annex:p02-w02-p02-039-proper-fragment.
- The proper-fragment result is a new in-book proof built only from handbook definitions (p02 grammar, p08 potential isomorphism and its proved characteristic-sentence theorem). It is not attributed to any external source. Choice is used once (regularity of omega_1).

## Heading level

The packet's computed heading level is `\chapter` (taken from the sibling `variants.tex`, which opens chapter 22). The insertion point is after `parts/p02/variants` and before `parts/p02/second-and-higher-order-logic-supplement`, which has no heading and continues chapter 22. A `\chapter` heading here would start a new chapter and absorb the supplement, contradicting the toc tag `P2 22 22.8`. The body therefore opens with `\section`. The lead should confirm or change this at insertion.

## Open items

- Exact locators (chapter, theorem or page) for the Karp 1964 completeness claim (thm:p02-karp-completeness, def:p02-infinitary-derivation) and the Scott 1965 calibration and Scott-sentence claims (thm:p02-lomega-one-omega-calibration and the construction paragraph, variants.tex 357-404). Sources not held: Karp, Languages with Expressions of Infinite Length (North-Holland, Studies in Logic and the Foundations of Mathematics 33, 1964); Scott, "Logic with denumerably long formulas and finite strings of quantifiers", in The Theory of Models (1965), pp. 329-341. No locator was written.
- N-a-060 (Mostowski 1957, Fundamenta Mathematicae 44(1) 12-36; Lindstrom 1966, Theoria 32(3) 186-195; Keisler 1970, Annals of Mathematical Logic 1(1) 1-93): none held; no source-specific presentation written.

## Existing treatments found that were not in the packet's list

- def:p03-morley-infinitary, thm:p03-morley-borel-truth, thm:p03-morley-scott-sentence and related results in `handbook/parts/p03/presentations/n-a-004-02.tex` (on route via classification-theory.tex line 206).
- def:p08-bvb501-potential-isomorphism and thm:p08-bvb501-potential-isomorphism in `handbook/parts/p08/sources/src-025-501.tex` (on route via p08.tex line 74).
- `handbook/parts/p02/further-reading.tex` line 26 (bare citation of Karp1964, Scott1965).

## Round 2 (2026-10-04)

- Added body subsection sec:p02-w02-p02-039-sources (body lines 261-313): exact held-survey locators for the grammar (Barwise A.1 sec. 5.4 pp. 43-44), compactness failure / Lowenheim-Skolem / need for an infinitary rule (p. 44), attribution of the L_{omega1 omega} completeness theorem to Karp 1964 and Lopez-Escobar 1965 and its admissible-fragment strengthening (Makkai A.7 sec. 1 p. 236), Karp 1964 and Scott 1965 roles (p. 235), Scott's isomorphism theorem as a consequence of Vaught's Theorem 8.11 (sec. 8 p. 276), and the L_{omega1 omega} sentence characterizing omega (sec. 5 p. 254). The table row for the Karp boundary (body line 129-132) now carries the p. 236 locator.
- New intake bib keys: Barwise1977FirstOrder, Makkai1977, LopezEscobar1965 (LopezEscobar1965 data from Makkai's reference list, p. 281 region; not independently held).
- Guard G1 (files spec/research/edition-2026-p02-unit-accounting-w02-p02-044{,-return.json}.md and -045 equivalents): these were written at 04:01-04:02 by the unit-accounting packets w02-p02-044 and w02-p02-045, after this packet's first-round files (03:13-03:18). This packet did not create or modify them and did not touch them in round 2; they are outside this packet's owned set and are left for the lead.
- Unit compile: ok, 1 overfull (6.6 pt, in the unit bibliography rendering of the LopezEscobar1965 entry; layout of the unit-only bibliography).

## Continuation

- D-P3-009-GOAL-03 full-treatment links: written (body lines 64-154). Exact held-survey locators: written (body lines 261-313). Remaining: internal locators (chapter/theorem/page) inside Karp 1964 and Scott 1965 themselves, blocked_source until those works are acquired; then add them in this file and, via patch request, in variants.tex 357-404.
- D-P3-009-C01 remains open until both halves of GOAL-03 are supplied.
- N-a-060 components: blocked_source pending acquisition of the three articles.
- Self-checks run: find_fused_spaces (no hits), unit-compile (ok, 0 overfull), check.py --tree handbook (no findings naming these files).
