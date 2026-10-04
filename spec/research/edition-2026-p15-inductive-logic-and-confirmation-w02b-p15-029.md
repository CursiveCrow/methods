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

## Continuation

Remaining, in the duties' own words:

1. Zabell sec.2.2 Kemeny coherence converse proof; sec.5.2 Dirichlet identification (Dirichlet integral identity).
2. Zabell secs.6.1–6.3 (paradox feigned — product-to-zero argument is partly in the earlier chapter; paradox lost — extended continuum with universal generalizations, Zabell 1996 not held; Hintikka–Niiniluoto(–Kuipers) systems — link hintikka-inductive-logic.tex where it matches), 6.4 beyond the die example.
3. Zabell secs.8.3–8.5 (finite rule of succession via finite representation, finite continuum with negative α, Diaconis–Freedman quantitative approximation as Zabell states it), 9 beyond the first induction theorem, 10.1–10.5, 11 (species sampling, three-parameter theorem), 12.1–12.5 (ravens, grue, total evidence, old evidence, Popper–Miller), 13.1–13.2, 14 — definitions, statements, examples, claim types, proofs of Markov/normal mixture and species-sampling characterizations.
4. 1950: formula 110F (11) (OCR illegible; render PDF p.593 to read it); proof of 110I (needs Carnap 1945 "On Inductive Logic", Phil. Sci. 12, sec.15 — not held); comparative vindication and full quantitative-language c-function (deferred by the source itself; user decision).
5. Held-source index linkage: Carnap1950Probability unit has empty held_paths; SRC-063 held_paths point to Milton/Fordham, not `zabell-2011-published.pdf`; held-sources.json entries lack source_ids/bibkeys. Lead-owned files.
6. 2009 footer vs 2011 publisher version of Zabell: unresolved; needs the publisher PDF.
