# Part VII completion visual evidence: source lines 11961--12248

Date: 2026-08-17  
Status: bounded source/layout/navigation **PASS**; whole-publication reference
completeness **OPEN**

## Candidate identity

This report inspects only
`tmp/part7-11961-12248-settled-20260817/handbook/main.pdf`.

- metadata title: `The Methods of Reason`
- pages: 802
- bytes: 4,321,299
- SHA-256: `5e8d429e389df0ae55ed83e135eb608afbbebe72c75798d86a0ce3adb3d9b905`
- encryption: none
- media boxes: 802 US-Letter pages, 762 at rotation 0 and 40 at rotation 90

The PDF identity was checked before rendering and again after the complete
navigation, text, index, and source-freeze checks. It was not canonical when
this inspection began.

## Exact source and build boundary

The frozen authority remains the 762,835-byte, 17,206-line CRLF file
`source/formal-logic-reference.tex`, SHA-256
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
This tranche is exactly source lines 11961--12248 inclusive. Line 12249,
`\part{Second-Order and Higher-Order Logic}`, is excluded.

The five artifacts concatenate to 12,980 LF bytes, SHA-256
`b14aa4ab3bf2941e15676fefa59c3e66ccb5aa0abb154ce8264f9c860fbfe692`.
Every artifact is LF-only, preserves its final source blank line, and ends in
two LF bytes. The source/static restoration checker passed all 177 current
records; that checker does not establish independent source review, semantic
correctness, build, visual inspection, or human acceptance.

The settled build copied 606 governed `.tex`, `.sty`, `.bib`, `.csv`, and
`.md` inputs totaling 2,891,885 bytes. Their aggregate path/length/content
fingerprint was
`bb2d702d69b370437fe5e04cc79944d0b30880704a73b40c27300c25f5901ddf`
before and after the build. The copied/live source maps were byte-identical;
all live inputs predated the PDF.

The final log is 320,951 bytes, SHA-256
`d1ae2fb6cbc22091d7e867fa7ead94a57cc605b30cc43c9209e274461e8a427d`.
Biber processed 362 keys without warning/error. MakeIndex accepted 1,297
entries, rejected zero, wrote 1,538 lines, and reported zero warnings. The
settled log has zero undefined citations, duplicate labels/destinations,
rerun requests, package errors, or fatal errors. It has two undefined-reference
occurrences, both exactly `ch:intuitionistic-logic`, and two pre-existing font
warning lines. Observed typography diagnostics are 498 overfull hboxes, 1,517
underfull hboxes, zero overfull vboxes, and 14 underfull vboxes; these counts
are not a claim that unrelated pages were visually approved.

## Fresh render set

Sixty-five fresh Poppler 200-dpi renders were created under
`tmp/pdfs/visual-part7-11961-12248-20260817`. Sixty-two are portrait
1700 by 2200 pixels. Physical pages 461, 473, and 498 are correctly landscape
2200 by 1700. The PNGs total 23,261,326 bytes.

The retained render ledger is 15,466 bytes, SHA-256
`686ffaa320c076dd22dc53a97c684ca2dc634c62894dcd80dc23d52f06ffc3ed`.
It binds every page to its file, dimensions, byte count, and PNG digest; every
entry was re-opened and rehashed after inspection.

The governed set comprises:

- body/annex TOCs: physical 19, 20, and 23;
- the two known pending-reference pages: 73 and 439;
- incoming seam, exact normalization/ordinal chapter, categorical addition,
  lambda/type-theory continuation, arithmetic-calibration addition, and
  outgoing seam: 452--481;
- corrected consumer surfaces: 498, 512, 637, and 659;
- complete Part VII annex: 727--730;
- complete index: 781--802.

## Page inspection ledger

| Physical page(s) | Surface | Verdict | Observation |
|---:|---|---|---|
| 19--20 | body TOC | PASS | Exact Chapter 46 and distinct Chapters 47--51 appear once, in order, with separated numbers, titles, and folios. |
| 23 | annex TOC | PASS | The shortened P7 annex target remains correct; no number/title or title/folio fusion. |
| 73, 439 | governed forward references | OPEN | Each visibly contains one `??` for the same future label `ch:intuitionistic-logic`; no other placeholder occurs. |
| 452 | incoming transition | PASS | The preceding cut/Maehara material closes cleanly. |
| 453--458 | exact Chapter 46 | PASS | Normalization, full proof sketch, exact STLC grammar/rules, subject reduction, strong normalization, Curry--Howard example, ordinal-analysis boundary, warning, three exercises, and abstract-reduction definition are legible and correctly ordered. |
| 458--461 | categorical addition | PASS | The exact-source/addition seam is clean; A-072 table and A-151/A-152 figures fit their portrait/landscape pages without collision or clipping. |
| 462 | verso | PASS | Intentionally blank. |
| 463--473 | lambda/type-theory continuation | PASS | Corrected source-section consumers, prose, displays, and the landscape comparison table remain legible and within their columns. |
| 474 | transition | PASS | Landscape table closes cleanly before the next open-right chapter. |
| 475--480 | arithmetic calibration addition | PASS | The duplicate Gentzen theorem/boundary is absent; method, component table, theory definitions, ordinal table, Veblen entry, qualified theorem, and OPEN stubs render without overlap. The Gentzen row links to exact source Section 46.4. |
| 481 | outgoing transition | PASS | Functional Interpretations begins cleanly with unchanged furniture. |
| 498 | Part VII route table | PASS | Normalization and Gentzen rows use genuine exact sections; no retired annex/theorem destination appears. |
| 512 | Part VIII consumer | PASS | The normal-form statement points to exact source Section 46.1 and remains readable. |
| 637 | Part XII typed example | PASS | The STLC consumer points to source Section 46.2 while the distinct categorical definition remains its own target. |
| 659 | Part XII route table | PASS | The typed-example row points to source Section 46.2; table columns remain separated. |
| 727--730 | complete Part VII annex | PASS | Only distinct registered-calculus, Maehara, lambda, and functional items remain; duplicate normalization/arithmetic annex fragments are absent. |
| 781--802 | complete index | PASS | All 22 pages were inspected. Exhaustive vertically-intersecting cross-column word analysis found zero pairs below 4 pt. Minimum clearance is 15.232394 pt on physical 799 (`propo-` / `Suslin`); no fused legacy strings occur. |

No inspected page shows clipping, cross-column collision, accidental overprint,
broken display, missing glyph, bad folio/running head, or malformed transition.

## Navigation and literal-text checks

The exact and addition destinations resolve to the observed pages, including:

- `ch:normalization-curry-howard` to physical 453;
- its four exact section anchors to 453, 454, 456, and 456;
- the three exact exercise anchors to physical 458;
- the categorical table/figures to 459, 460, and 461;
- the distinct Arithmetic Proof Theory chapter to 475;
- its method/table/definitions and Feferman--Schuette entry to 475--480.

The PDF contains 3,629 named destinations, all valid; 3,806 internal links and
401 URI links, all valid; and 407 outline entries, all in range. The relevant
outline order is public Part VII (431), exact Normalization and Ordinal
Analysis (453), Lambda Calculi and Type Theories (463), Arithmetic Proof
Theory (475), Functional Interpretations (481), and Part VII annex (727).

The exact-section consumers occur on physical 444, 463, 473, 478, 498, 512,
637, and 659. The distinct categorical-definition consumers occur on 460,
469, and 637. Every inspected link lands on its intended genuine source or
separately justified addition anchor; no alias supplies a retired label.

Independent pypdf and pdfplumber full-document scans agree exactly: one
literal `??` occurs on physical page 73 and one on physical page 439, both for
`ch:intuitionistic-logic`; no other literal `??` occurs.

## Verdict and limits

The exact source through the end of Part VII at line 12248, its bounded
categorical and arithmetic additions, every source/addition seam, all corrected
consumers, the Part VII annex, TOCs/outlines/links, and the complete index pass
this fresh visual inspection.

The whole publication remains **OPEN**, not release-ready. The later exact
intuitionistic-logic target has not yet been restored, two visible placeholders
remain, the additions/register obligations remain OPEN, and no human
acceptance exists. This report does not convert source/static/build/visual
evidence into semantic admission, completed AI review, register closure, or
user acceptance.
