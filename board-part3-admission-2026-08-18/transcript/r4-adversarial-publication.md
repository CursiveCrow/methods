# Round 4 — adversarial-publication

### F1 — accept
- current evidence: `handbook/parts/p03/types-ultraproducts-supplement.tex:1-9`; `handbook/annex/p03/types-ultraproducts-supplement.tex:1-6`; `handbook/parts/p03/maps-elementarity-supplement.tex:1-8`; `handbook/parts/p03/qe-categoricity-games-supplement.tex:1-7, :121`
- response: The accepted reader-source repair remains intact. The four routed seams still use ordinary editorial attribution, source/proof standing, and nonreplacement prose and print no admission state, register ID, finalizer, or pointer-only construction token. The occurrence of “open” at the QE supplement's line 121 is the mathematical statement that an independent property is left open rather than fabricated; it is not workflow debt. Percent-comment control text remains outside this reader ruling.

### F8 — accept
- current evidence: `handbook/parts/p03/preservation-abstract-logic.tex:348-397`; `handbook/annex/p03/editorial-proofs.tex:79-279`; `handbook/annex/p03.tex:1-4`
- response: The current bytes preserve the exact regular-logic statement and reciprocal `proved=annex:p3.abstract.3`/`thm:p03-lindstrom` pair. The annex still contains the finite `Piso`/`Seq` encoding (`:86-134`), the explicit `BF(I)` potential-isomorphism construction (`:136-175`), the finite bounded-rank induction (`:177-194`), the discrete-number and `W` recursion formulas (`:196-239`), finite satisfiability and nonstandard-index step (`:241-255`), and the extracted families with both extension directions (`:257-277`). No source regression or new reader/coverage failure is established.

### F11 — accept
- current evidence: `tools/build_named_theorem_index.py:56-75, :91-108, :132, :135-145`; `handbook/generated/named-theorem-index.tex:9, :37, :202, :204, :216, :282`
- response: The round-3 generated-title defect is fixed. `title_parts` scans for the first unescaped, depth-zero `@`, preserving braced literal occurrences; `sort_text` uses the left/sort half and `render` emits only the right/display half. The refreshed file contains 358 `\hyperref` rows and no raw `@`. Its three formerly malformed rows now display only `Chang--\L o\'s--Suszko theorem`, `Lindstr\"om's theorem`, and `\L o\'s--Tarski preservation theorem`. The inherited ACF, Morley, and Ryll--Nardzewski destinations remain present exactly once at lines 9, 216, and 282. The prior F11 objection is therefore closed at generated-source level.

## Boundary

- disposition: accept F1, F8, and F11; no still-open source objection remains on this round's seam.
- evidence limit: This acceptance covers current source text, generator logic, generated-row content, and reciprocal labels only. I did not run the generator, a test, TeX/reference/index compilation, or a PDF build; did not inspect hyperlinks, page numbers, sorting in a rendered index, or layout; and do not infer F2 admission/provenance, human review, or user acceptance. I edited only this verbatim transcript and read no other seat transcript.
