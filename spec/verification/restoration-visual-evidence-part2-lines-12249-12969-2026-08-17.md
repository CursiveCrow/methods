# Part II higher-order visual evidence: source lines 12249--12969

Date: 2026-08-17  
Status: bounded source/layout/navigation **PASS**; whole-publication reference
completeness **OPEN**

## Candidate identity

This report inspects only
`tmp/higher-order-12249-12969-settled-20260817/handbook/main.pdf`.

- metadata title: `The Methods of Reason`
- pages: 800
- bytes: 4,300,470
- SHA-256: `dc6ea76baa5f11796fbd1b50bdaef1cf99cf707186d3632252c5c40e7f2841a5`
- encryption: none
- media boxes: 800 US-Letter pages, 760 at rotation 0 and 40 at rotation 90

The identity was checked before rendering and again after page inspection,
navigation validation, two independent literal-text scans, complete-index
geometry analysis, and source-freeze verification. It was not canonical when
this inspection began.

## Exact source and build boundary

The frozen authority remains the 762,835-byte, 17,206-line CRLF file
`source/formal-logic-reference.tex`, SHA-256
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
This tranche is exactly source lines 12249--12969 inclusive. Line 12970,
`\part{Nonclassical Logic}`, is excluded.

The eleven artifacts concatenate to 30,397 LF bytes, SHA-256
`49d6ae3bf32d8ea9647290772a2e4036cc61378fd7b4fc1a23ee7bb5cf11182f`.
Their corresponding raw CRLF range is 31,118 bytes, SHA-256
`aed28e9f38fe67c26223acecaca7151bc8fb53ac60de696c68e95dd679fba828`.
Every artifact is LF-only, preserves its terminal source blank, and ends in
two LF bytes. The restoration checker passed all 188 current records; that
check establishes source/static integrity only.

The settled build copied 630 governed non-transient handbook inputs totaling
2,940,127 bytes. Their aggregate path/length/content fingerprint was
`4ca58d44f777ddcc9b9e3ef98e8578359b84242f6f3edc450f6c423a0861526f`
before and after the build. Every copied input matched the live tree exactly,
the live tree remained unchanged, and every input predated the PDF.

The final log is 295,173 bytes, SHA-256
`6eb7fc405c09239a3e295ecda4b417544f8ecba28377956d7921b4f0dd663f19`.
Biber processed 361 keys without warning or error. MakeIndex accepted 1,273
entries, rejected zero, wrote 1,503 lines, and reported zero warnings. The
settled log has zero undefined citations, duplicate labels or destinations,
rerun requests, Cleveref warnings, package errors, or fatal errors. It has two
undefined-reference occurrences, both exactly `ch:intuitionistic-logic`, and
two pre-existing font-warning lines. Observed typography diagnostics are 477
overfull hboxes, 1,271 underfull hboxes, zero overfull vboxes, and 13 underfull
vboxes; those counts do not visually approve unrelated pages.

## Fresh render set

Fifty-nine fresh Poppler 200-dpi renders were created under
`tmp/pdfs/visual-higher-order-12249-12969-20260817`. Fifty-seven are portrait
1700 by 2200 pixels. Physical pages 168 and 186 are correctly landscape 2200
by 1700. The PNGs total 19,849,206 bytes.

The render ledger is 5,867 bytes, SHA-256
`d6aa89bc5234684fda40550d813d40d96dc3b6d474b3503d4572f87f6bd6fda5`.
It binds every page to its filename, dimensions, byte count, and digest; every
render was opened at its native resolution.

The governed set comprises:

- body TOCs: physical 14--16;
- annex TOC: physical 23;
- the two known pending-reference pages: 73 and 439;
- incoming seam, subordinate source heading, exact two-chapter source,
  bounded body addition, outgoing seam, and first downstream consumer:
  168--191;
- complete Part II annex context and the two retained higher-order proofs:
  706--712;
- complete index: 779--800.

## Page inspection ledger

| Physical page(s) | Surface | Verdict | Observation |
|---:|---|---|---|
| 14--16 | body TOC | PASS | The subordinate higher-order heading, Chapters 15--17, sections, folios, and surrounding Parts II--IV remain separated and correctly ordered. |
| 23 | annex TOC | PASS | P2 appears once and links to its annex; no number/title or title/folio fusion is visible. |
| 73, 439 | governed forward references | OPEN | Each visibly contains one `??` for the same future target `ch:intuitionistic-logic`; no other placeholder occurs. |
| 168 | incoming transition | PASS | The preceding First-Order Reference Entries table closes cleanly on its native landscape page. |
| 169--170 | subordinate source heading and verso | PASS | `Second-Order and Higher-Order Logic` appears as an attributed subordinate Part II navigation heading; the following verso is intentionally blank. |
| 171--178 | exact Chapter 15 | PASS | Second-order syntax, full and Henkin semantics, categoricity, compactness/effective-completeness results, translation, warning, and three exercises are legible and correctly ordered. The exact `\R` occurrences render as blackboard-bold reals without leakage or missing glyphs. |
| 179--183 | exact Chapter 16 | PASS | Simple types, term formation, standard/Henkin structures, semantic calculation, foundational warning, and three exercises render without clipping or collision. The exact-to-addition handoff begins cleanly on 183. |
| 183--187 | bounded body addition | PASS | The sorted-assignment guard, translation-defined calculus, qualified adequacy theorem, proof boundary, comparison section, and landscape table remain visibly distinct from exact source. Page 187 is a sparse but valid table tail. |
| 188 | verso | PASS | Intentionally blank before Chapter 17. |
| 189--191 | outgoing seam and consumer | PASS | Variants begins cleanly; its Definition 16.10 and Annex P2.HOL.5 consumers point to genuine live anchors and remain readable. |
| 706 | annex transition | PASS | Intentionally blank before the open-right Part II annex. |
| 707--710 | existing Part II annex context | PASS | Earlier OPEN notes and distinct proof items remain legible and correctly separated from the higher-order supplement. |
| 711--712 | higher-order annex addition | PASS | Annex P2.HOL.5 and P2.HOL.8 render once, prove only their separately retained results, and link back to genuine body/source anchors. |
| 779--800 | complete index | PASS | All 22 pages were inspected. Exhaustive vertically-intersecting cross-column word analysis found zero pairs below 4 pt. Minimum clearance is 15.232394 pt on physical 797 (`propo-` / `Suslin`); no fused legacy string or opposite-column collision occurs. |

No inspected page shows clipping, cross-column collision, accidental
overprint, broken display or table, missing glyph, malformed transition, bad
folio, or running-head collision.

## Navigation and literal-text checks

The PDF contains 3,634 named destinations, all valid; 3,767 internal named
links and 400 URI links, all valid; and 413 outline entries, all in range. The
relevant named destinations include:

- the subordinate higher-order heading on physical 169;
- Chapters 15 and 16 on 171 and 179;
- the eight exact section anchors on 171--182;
- the six exact exercise anchors on 178 and 183;
- the exact categoricity/Lindstroem theorem anchors on 174--175;
- the body-addition definitions, theorem, boundary, section, and table on
  183--186;
- Annex P2.HOL.5 and P2.HOL.8 on physical 711.

All actual consumers resolve to genuine anchors. In particular, the Chapter
15/16/section TOC links originate on 14; the comparison table links to exact
Section 15.4; the retained annex adequacy proof links to exact Section 15.5;
the downstream many-sorted theorem links to Definition 16.10 and Annex
P2.HOL.5; and the body adequacy theorem links to Annex P2.HOL.8. No alias
supplies a retired historical label.

The retained navigation audit is 2,496 bytes, SHA-256
`453e001a12b0cbeeb7eb7070012a86fae88d21f110c4e13cb9a9838e255bdabe`.
The complete-index bounding-box evidence is 727,457 bytes, SHA-256
`5ed95082bcc7b0d34472876a2e8836eef9277001da7a3610fcecd3e02dc94a61`.

Independent pypdf and pdfplumber full-document scans agree exactly: one
literal `??` occurs on physical page 73 and one on physical page 439, both for
`ch:intuitionistic-logic`; no other literal `??` occurs.

## Verdict and limits

The exact inherited source at lines 12249--12969, the governed subordinate
Part II relocation, both exact chapters, bounded body and annex additions,
every source/addition seam, all actual consumers, TOCs, outlines, links, and
the complete index pass this fresh build-bound visual inspection.

The whole publication remains **OPEN**, not release-ready. The later exact
intuitionistic-logic target has not yet been restored, two visible placeholders
remain, all source units and handbook units remain unadmitted, all register
obligations remain OPEN, external assignment remains incomplete, and no human
acceptance exists. This report does not convert source/static/build/visual
evidence into semantic admission, completed AI review, register closure, or
user acceptance.
