# Part VII restoration visual evidence: source lines 11354--11960

Date: 2026-08-17  
Status: bounded source/layout/navigation **PASS**; whole-publication reference
completeness **OPEN**

## Candidate identity

This report inspects only the settled candidate at
`tmp/part7-11354-11960-settled-20260817-r2/handbook/main.pdf`.

- metadata title: `The Methods of Reason`
- pages: 806
- bytes: 4,329,782
- SHA-256: `1fe2a7e8d83c7672d0c5fe99df826e41f364a8fe777d0b2a00f56bcdc5d5695d`
- encryption: none
- media boxes: 806 US-Letter pages, 766 at rotation 0 and 40 at rotation 90

The identity was checked before rendering and again after the navigation,
literal-text, and source-freeze checks. This candidate was not canonical when
the inspection began.

## Source and build boundary

The frozen authority remains
`source/formal-logic-reference.tex`, 762,835 bytes, 17,206 CRLF physical
lines, SHA-256
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
The restored tranche is exactly lines 11354--11960 inclusive. Line 11961,
which begins the normalization chapter, is excluded.

The fourteen exact restoration artifacts concatenate to 24,384 LF bytes,
SHA-256
`d9e149eaf9e40a256fae0629a228c6a94ab50c14e086fe5643075c18a011d519`.
Every artifact is LF-only, preserves its final source blank line, and ends in
two LF bytes. The restoration checker passed all 172 current records and
states only source/static evidence; it makes no independent-source, build,
visual, semantic, or human-review promotion.

The settled build copied 594 governed `.tex`, `.sty`, `.bib`, `.csv`, and
`.md` inputs, totaling 2,852,381 bytes. Their aggregate path/length/content
fingerprint was
`aecfa62a760e2a8c9a244e0ad2a7893778a31e62b2d53d95608c5825543e6151`
before and after the build. The copied and live source maps were byte-identical,
and every live input predated the final PDF.

The final log is 320,466 bytes, SHA-256
`fa07ae3b48c370dc56880c7e6662bd6eff4a009f63333799f1ebf2b011f73d6e`.
Biber processed 362 citation keys without warning or error. MakeIndex accepted
1,312 entries, rejected zero, wrote 1,551 lines, and reported zero warnings.
The final TeX log has zero undefined citations, duplicate labels,
duplicate destinations, rerun requests, package errors, or fatal errors. It
has two undefined-reference occurrences, both exactly
`ch:intuitionistic-logic`, plus the standard summary, and two pre-existing
font-warning lines. Typography diagnostics are 499 overfull hboxes, 1,515
underfull hboxes, zero overfull vboxes, and 14 underfull vboxes; those counts
are observations, not a global typography pass.

## Fresh render set

The inspection created 54 fresh Poppler 200-dpi PNGs in
`tmp/pdfs/visual-part7-11354-11960-20260817`. Fifty-three are portrait
1700 by 2200 pixels; physical page 498 is correctly landscape 2200 by 1700.
The PNGs total 18,018,348 bytes.

The retained machine-readable render ledger is 12,845 bytes, SHA-256
`9655c4c983c5976f7092adebe8c12d9841b37c99c8a73188a201a4141c8a955c`.
It binds each physical page number to its path, byte count, dimensions, and
PNG SHA-256. All 54 entries were re-opened and rehashed after inspection.

The governed physical-page set is:

- body and annex TOCs: 19, 20, and 23;
- the pre-existing unresolved-reference consumer: 73;
- incoming transition, public Part VII, exact subordinate heading, exact two
  source chapters, both bounded additions, and outgoing transition: 430--454;
- the downstream body/sheet/annex route table: 498;
- the Part VII annex additions: 729--730;
- the complete index: 785--806.

## Page inspection ledger

| Physical page(s) | Surface | Verdict | Observation |
|---:|---|---|---|
| 19--20 | body TOC | PASS | Public Part VII, subordinate `Proof Theory`, Chapters 44--51, section numbers, titles, and folios are separated and ordered. |
| 23 | annex TOC | PASS | P7 annex title/folio spacing and target are intact; no number/title or title/folio fusion. |
| 73 | earlier exact-source consumer | OPEN | One visible `??` remains for `ch:intuitionistic-logic`; this is the already governed forward target. |
| 430 | incoming transition | PASS | The preceding Part VI content closes without collision or clipped furniture. |
| 431 | public Part VII | PASS | The fixed public title is centered, correctly wrapped, and numbered VII exactly once. |
| 432 | verso | PASS | Intentionally blank. |
| 433 | exact subordinate source part | PASS | `Proof Theory` and the recorded source attribution render once with clean spacing. |
| 434 | verso | PASS | Intentionally blank. |
| 435--438 | exact Chapter 44 | PASS | Chapter opening, conventions, sequent definitions, complete LK/LJ rule surfaces, quantifier side conditions, and derivation definitions are legible and unclipped. |
| 439 | exact Chapter 44 | OPEN | The soundness sketch and worked derivation are visually sound; its exact forward reference to `ch:intuitionistic-logic` visibly prints the second `??`. |
| 440 | exact-source/addition seam | PASS | Source rule-standing definitions and exercises close cleanly before the separately marked registered-calculus addition begins. |
| 441--444 | bounded calculus addition | PASS | A-070 structural table, translations, and the long calculus catalog stay within their page/column boundaries; no table collision or truncation is visible. |
| 445--448 | exact Chapter 45 | PASS | Chapter opening, Mix surface, complete equipollence proof, cut-elimination sketch, subformula proof, corollaries, warnings, and exercises are readable and correctly ordered. |
| 449 | exact-source/addition seam | PASS | Exact Craig/Beth statements close before the distinct midsequent/Herbrand addition; no duplicate heading or overprint. |
| 450--451 | bounded cut/interpolation addition | PASS | Midsequent, Herbrand, Maehara, proof-boundary, and OPEN stub surfaces are legible; boxes remain within the text block. |
| 452 | verso | PASS | Intentionally blank. |
| 453--454 | outgoing transition | PASS | Chapter 46 begins cleanly with unchanged running heads and margins. |
| 498 | downstream route table | PASS | Corrected exact-source and distinct-addition destinations fit the landscape table without overlap, clipping, or stale annex labels. |
| 729--730 | Part VII annex | PASS | The two registered-calculus items and Maehara item render in order with reciprocal body targets and no historical Cut-item duplicates. |
| 785--806 | complete index | PASS | All 22 pages were inspected. The exhaustive vertically-intersecting cross-column word scan found zero pairs below 4 pt; minimum clearance is 12.578210 pt on physical 785 (`proof-theoretic` / `An`). No fused `rulesProof` or `Entscheinormal` extraction remains. |

No inspected page shows clipping, cross-column collision, accidental overprint,
broken display, missing glyph, bad folio/running head, or malformed transition.
The two visible placeholders are reference-state failures, not layout failures.

## Navigation and literal-text checks

Both chapter labels and all restored section, exercise, lemma, theorem, and
annex destinations resolve to the inspected pages. Representative exact
destinations include:

- `part:proof-theory` to physical 433;
- `ch:lk-lj` to 435;
- `ch:cut-elimination` to 445;
- `lem:cut-mix-equipollence` to 445;
- `lem:cutfree-subformula` to 447;
- `thm:craig-interpolation` to 448;
- `thm:beth` to 449;
- the three retained annex items to 729, 729, and 730.

The PDF contains 3,635 named destinations, all valid; 3,843 internal named
links and 401 URI links, all valid; and 406 outline entries, all in range.
The Part VII outline order is public Part VII (431), subordinate `Proof Theory`
(433), Chapter 44 (435), Chapter 45 (445), Chapter 46 (453), the later Part VII
chapters, and the Part VII annex (729).

Independent full-document extraction with pypdf and pdfplumber agrees exactly:
there are two literal `??` occurrences, one on physical page 73 and one on
physical page 439. Both arise from exact source references to the same future
label `ch:intuitionistic-logic`. No other literal `??` occurs.

## Verdict and limits

The exact restored source through line 11960, both bounded OPEN additions,
their consumer corrections, source/addition seams, annex routes, TOC/outline,
internal links, and complete index pass this fresh visual inspection.

The whole publication remains **OPEN**, not release-ready, because the exact
future target `ch:intuitionistic-logic` has not yet been restored and therefore
produces two visible placeholders. The additions and register obligations also
remain explicitly OPEN, and no human acceptance is established. This report
does not convert source/static/build/visual evidence into content review,
semantic admission, register closure, or user acceptance.
