# P15 164.6 — packet w02b-p15-029 (Carnap 1950 / Zabell HHL10)

Authoring note, 2026-10-04. Unreviewed author-side work; nothing here is accepted or complete.

## Files

- Body: `handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-029.tex` (chapter, label `sec:p15-w02b-p15-029`).
- Annex: `handbook/annex/p15/inductive-logic-and-confirmation-w02b-p15-029.tex` (13 annexitems, reciprocal).
- Bib intake: no new keys (uses `Carnap1950Probability`, `Zabell2011CarnapInductiveInference`).
- Symbol intake: 14 rows, chapter-scoped.
- Editable hosts touched: boundary sentences only, in `carnap-logical-probability-and-induction.tex` (def:p15-carnap-source-boundary) and `carnap-confirmation-relevance-and-reliability.tex` (def:p15-carnap-continuation-boundary), now pointing to the new chapter.
- Insertion: body after `parts/p15/goodman-entrenchment-and-projectibility` in `handbook/parts/p15.tex`; annex after the same in `handbook/annex/p15.tex` (lead executes).

## Sources opened this session

- `source/references/p15-carnap-induction/carnap-1950-archive-ocr.txt`: §15A (signs, denumerable constants, identity), D16-6, §41 (pp.161–177 lines 10640–11500), §54A (pp.287–289), §56 (pp.302–305: D56-1, D56-2, T56-1, T56-2, T56-4 and the W/W' discussion), §94 (T94-1), §95 (pp.497–502), §96 (pp.502–508).
- `carnap-1950-appendix-pages-562-577.txt`: whole §110A–J. Page image of printed p.563 (PDF p.585) rendered to confirm τ, ζ_i, Fraktur Z and 𝔏_N notation.
- `carnap-1950-comparative-428-482.txt`: §81 (D81-1, proof of T81-1, T81-2a/b with printed proofs, examples).
- `zabell-2011-published.txt` lines 1–780 and 945–1075 (secs. 1–6.4, 8.3–8.5); page image of p.273 (PDF p.9) rendered: the held copy prints the count of structure descriptions as C(n+t−1, t); the correct number is C(n+t−1, t−1). Recorded in the reader as a source erratum.

## Decisions and findings

- 110A's existence/effective-reduction claim stands under the declared restriction to degree-one predicates (p.566, "all theorems mentioned in the remainder of this section"). The monadic proof therefore discharges the source claim; the relational existence question is not a 1950 claim and is not asserted.
- The OCR of 110A (5) cites "D16-6g" for "purely general"; D16-6h is purely general in the held D16-6 text. The reader cites D16-6f–h for the definitions.
- Monadic limit proof: Ehrenfeucht–Fraïssé-style count lemma plus predictive-formula tail bound (independent reconstruction).
- T81-2a transfer: monadic explicit threshold (no choice); relational via compactness + downward LS (inherited labels `thm:fol-compactness`, `thm:downward-ls`, both under AC).
- §96 normal approximations: Carnap prints no proof; rigorous content given as limits via `thm:p15-stirling-general-binomial`; finite-population transfer via `thm:p15-finite-urn-approximation`. Exact Chebyshev form of T96-1e.
- 110I: proof delegated by Carnap to his 1945 paper (not held). Independent c* computation shows variety leaves law and unqualified instance unchanged and raises the qualified prediction for the omitted kind.
- Johnson–Carnap: full proof for t ≥ 3 (sufficientness) and t = 2 (affine), with the iid exception and the sign argument using infinite extendability.
- Existing treatments found and linked (not in packet list): `sec:p15-exchangeability-and-definetti` (de Finetti kernel, binary de Finetti, finite-urn TV bound), `thm:p15-feller-hausdorff`, `thm:p15-stirling-general-binomial`, `sec:p15-hintikka...` (hintikka-inductive-logic.tex, relevant to Zabell 6.3).

## Block 1 (r2) additions, 2026-10-04

- Sources opened this block: `carnap-1950-archive-ocr.txt` lines 18130-19803 (secs. 57-60, printed pp. 305-333) and `carnap-1950-appendix-pages-562-577.txt` (110E-G); page images rendered from `carnap-1950-first-edition.pdf` PDF pp. 593 (printed 571: formulas (11), (12), (13)), 595 (printed 573: (15)-(17)), 334 (printed 312: T58-1f-l), 351-353 (printed 329-331: T60-1-T60-6). PDF offset +22.
- Finding: (11) is c*(l,e) ~ (s/N)^{w_1}. Printed (13) uses the approximation sign, but C(s+kappa-1, s_1+w_1)/C(N+kappa-1, s_1+w_1) is the exact value (proved equal to the earlier exact form).
- Finding: 110G claim "both grow close to 1 as s increases" is exact for (16); for (17) it needs s_2 -> infinity (non-swans leave c_qi fixed).
- 110F large-N claim: conforming factor (s+kappa)/(s+kappa-s_1-w_1), independent of N; violating factor (s+kappa)/(N+kappa-1-s_1-w_1).
- OCR shows no T60-4 between T60-3 and T60-5 on p. 330 (page image confirms); not cited.
- New body sections: sec:p15-w02b-p15-029-laws, -regular, -bayes; bridge extended with 110F (11), (13), large-N, 110G (14)-(17) and limit, T57-1, D57-1, D57-3-5, T57-3/5/6, T58-1, D58-1, T58-3-5, T59-1, T59-2q, T59-3d, T59-4, T59-5, T59-6a-g, T60-1-3, T60-5, T60-6.
- L-infinity passage of the sec. 59-60 theorems uses thm:p15-w02b-p15-029-ltruth-transfer (AC in relational systems), matching Carnap's (II) route via T20-11 and T40-21.

## Block 2 additions, 2026-10-04

- Sources opened this block: carnap-1950-archive-ocr.txt lines 13700-17900 (secs. 46-54) and 18780-19000 (T55-2, T59-1, T59-2), 20086-20420 (sec. 62); page images of PDF pp. 297, 300 (printed 275, 278: the two Bernoulli tables), 338-339 (printed 316-317: T59-1a-w, T59-2a-h), 360-362 and 364 (printed 338-340, 342: sec. 62 correspondences). zabell-2011-published.txt lines 100-200 (secs. 2.1-2.2, pp. 267-268) and 520-575 (sec. 5.2, pp. 275-276).
- Finding: Carnap's tables (pp. 275, 278) differ from exact values in the last digits: 9,949.88 / -50.12 (exact 9,949.874, -50.126); premiums 16.50 and 11.52 (exact 16.470, 11.505), from q rounded to seven figures. Recorded as hbwarning def:p15-w02b-p15-029-table-rounding.
- Finding: restaurant estimate 2.2 and insurance estimated loss 10 verified.
- Kemeny converse: Zabell gives no argument (p. 268); finite-system coherence characterization and proof are an independent reconstruction (both directions).
- Dirichlet identification (Zabell 5.2, p. 276): proved via the rising-factorial product, the Dirichlet integral (Gamma change of variables), and uniqueness of the de Finetti mixing law.
- New body sections: sec:p15-w02b-p15-029-problem, -conventions, -axiom-systems; bridge rows for secs. 46-54 and 62; pointer to the preceding chapters' boundaries removed.
- Notation: Carnap's total utility f-bar is written u-bar (bridge row records it) to avoid a clash with fortune f.
- Existing treatment linked (not in the packet list): sec:p17-finite-expected-utility.

## Block 1 (r3) additions, 2026-10-04

- Sources opened: carnap-1950-archive-ocr.txt lines 7156-8105 (secs. 25-28 start: D25-1-4, A25-1, D26-1-6, T26-1-5, D27-1, T27-2, T27-3), 10060-10130 and 10200-10330 (D40-3, T40-11-14, T40-20 table, D40-5, D40-6, T40-21, T40-22), 10495-10560 (T40-32), 11421-12280 (secs. 41E-F, 42), 28558-29250 (secs. 90-92, 94 start), 1250-1300 (TOC). Page images from carnap-1950-first-edition.pdf PDF pp. 174 (printed 152: D40-3), 511-514 (printed 489-492: T91-3, T92-1, T92-3, the jump from sec. 92 to sec. 94).
- Finding: no sec. 93 in the 1950 edition (TOC and p. 492). Sec. 97 is likewise absent from the TOC list.
- Finding: T40-20 is the normal-function table; T40-21 a-f are the limit laws (sum, difference, product, constant, final-segment equality, order).
- New body sections: sec:p15-w02b-p15-029-two-senses (41E, 41F (1)-(8b), 42A (1)-(10), 42B (13)-(20), (i)/(ii)); sec:p15-w02b-p15-029-symmetrical (D25-4, D26-1-6, D27-1, D40-3, T26-2, T26-5, T27-2f, T27-3, T40-32, D90-1-4, D91-1-4, T90-1, T91-1-3, T92-1a-k, T92-3a-j, worked example, nonsymmetrical failure case). Annex: four new annexitems. Bridge rows for all of these.
- The L_infinity step of T91-2 is made explicit (finite in-correlations agreeing with C on the constants involved); no choice used. T92-3 (i), (j) hold for any sequence of symmetrical functions since the finite values do not depend on N (stated and explained in the reader).

## Continuation

Remaining after block 1 (r3): sec. 41E-F, 42 and secs. 90-92 written (with secs. 25-27, D40-3, T40-21, T40-32 as used there). Still not written: secs. 43, 44, 45A (OCR lines 12277-12894, 12894-13180, 13180-13318); chapter I (secs. 1-7) and chapter II (secs. 8-13) beyond the existing summary; sec. 33 (Q-normal form, OCR ~8700-8954), secs. 37-38 incl. D37-2b (OCR 9381-9818); sec. 55B-C (pp. 296-305, carnap-1950-pages-294-305.txt); bridge rows for chapters I-II, 43-45, 65-76, 82-88, 98-107, 110H, 110J; all Zabell items listed below. Items 1-6 below otherwise stand.

Remaining, in the duties' own words (block 2 state):

1. 1950 secs. 41E-F, 42, 43-44, 61 (confirmation by a predictable observation), 90-93 (symmetrical m-/c-functions): not written. OCR line starts: sec.41 10711, 42 11764, 43 12277, 44 ~12850, 61 19803, 90 28558, 91 28741, 92 28939, 93 ~29050. Secs. 46-54 and 62 written this block.
2. Secs. 57-60: T59-1 r-w, T59-2a-p beyond a, h, T59-3a-c, T59-6h-y not individually stated or proved.
3. Bridge: numbered items of secs. 65-76, 77-89 beyond D81-1/T81, 90-93, 97-107 still lack item-by-item rows (the host chapter carnap-confirmation-relevance-and-reliability cites D65-1d, T68-4, T69-1, T69-3, T70-4, T71-2, T71-3, D81-1, D82-1, D84-1, D103-1, T104-2, T105-1; those locators must be checked against the OCR before rows are written). Sec. 62 correspondences for Hosiasson's T61 items and Jeffreys's T59-2e, g, T59-3b, T61-2 are reported, not proved.
4. Zabell: 2.2 and 5.2 written. Not written: 6.1-6.4 (incl. attribute symmetry 6.4), 7, 8.3-8.5, 10.1-10.5, 11, 12.1-12.5, 13-14; worked cases and claim types of secs. 6-12 (C003). Zabell text lines: 6.1 644, 6.2 692, 6.3 728, 6.4 761, 8.3 950, 8.4 1021, 8.5 1030, 10.2 1215, 10.3 1227, 10.5 1326, 11 ~1440, 12.4 1622.
5. 110I proof: blocked_source (Carnap 1945, Phil. Sci. 12, sec. 15, not held). Comparative vindication and quantitative-language c-function: deferred by the 1950 text to vol. II. The contradiction from the general principle of indifference (secs. 47A, 62) is likewise deferred by Carnap to vol. II.
6. Held-source index linkage (lead-owned) and Zabell 2009 footer vs 2011 publication record: unresolved.
