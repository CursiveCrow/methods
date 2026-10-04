# Part VIII Intuitionistic visual evidence: source lines 12970--13200

Date: 2026-08-17  
Status: bounded source/build/layout/navigation **PASS**; whole-publication
admission and acceptance **OPEN**

## Candidate identity

This report inspects only
`tmp/intuitionistic-12970-13200-postfix-settled-20260817/handbook/main.pdf`.

- metadata title: `The Methods of Reason`
- pages: 794
- bytes: 4,282,224
- SHA-256: `898bef6b139599d586644283089970395f880ae42d681371c9f178dc438fe4b5`
- encryption: none
- page geometry: US Letter, with the existing native landscape rotations

The first settled attempt was disqualified because its addition note visibly
lost two TeX control-sequence backslashes. The helper was corrected,
regression-locked, and rerun in a new scratch directory. Only the postfix PDF
identified above is eligible for this verdict.

## Exact source and build boundary

The frozen authority remains the 762,835-byte, 17,206-line CRLF file
`source/formal-logic-reference.tex`, SHA-256
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
This tranche is exactly source lines 12970--13200 inclusive. Line 13201,
`\chapter{Modal, Temporal, and Epistemic Logic}`, is excluded.

The nine artifacts concatenate to 9,203 LF bytes, SHA-256
`473730b98840e61142dfe4719a75114b9cd4cb02717c16c78fed37b3119dcc63a`.
Their corresponding raw CRLF range is 9,434 bytes, SHA-256
`60769a4a30efefb09cc5bdd13a47ec6373950cf29f12eb48064457d0a912f1aa`.
Every artifact preserves its exact interval ending; the 13046--13057 proof
interval ends with one LF, while the other eight retain their terminal source
blank and end with two LF bytes. All 197 current restoration records pass the
source/static checker.

The settled build copied 649 governed non-transient handbook inputs totaling
2,977,342 bytes. Their aggregate path/length/content fingerprint was
`b0236b00376390df9b48f6ea3e1badb9bc0c846b86736265dc861672a9ce8f92`
before and after the build. Every copied input matched the frozen live tree and
predated the PDF.

The final log is 280,647 bytes, SHA-256
`4aa1575cb60dd61f529118981f92b8e69e77ea7cca48f019e355ed3250d70c9c`.
Biber processed 360 keys without warning or error. MakeIndex accepted 1,265
entries, rejected zero, wrote 1,494 lines, and reported zero warnings. The log
has zero undefined references, undefined citations, duplicate labels or
destinations, rerun requests, Cleveref warnings, package errors, or fatal
errors. Observed typography diagnostics are 459 overfull hboxes, 1,148
underfull hboxes, zero overfull vboxes, and 14 underfull vboxes; these counts do
not visually approve unrelated pages.

## Fresh render set

Forty-nine fresh Poppler 200-dpi renders were created under
`tmp/pdfs/visual-intuitionistic-12970-13200-postfix-20260817`. Forty-eight are
portrait 1700 by 2200 pixels; physical page 510 is correctly landscape 2200 by
1700. The PNGs total 16,362,651 bytes.

The render ledger is 4,877 bytes, SHA-256
`71b7385e92ffad72ca9cdcf7d48c2fcc34ce96cac02ec8c3b14e061e83e33b4b`.
All 49 postfix renders were rehashed. Forty-eight are byte-identical to the
corresponding pages from the immediately preceding fresh inspection; page 506
is the sole changed render and was reopened at native resolution after the
control-sequence fix.

The governed set comprises:

- body TOCs: physical 19--21;
- annex TOC: physical 24;
- former pending-reference consumers: 73 and 439;
- incoming seam, public Part VIII, exact chapter, bounded additions, and
  outgoing seam: 500--517;
- Part VIII annex transition/context: 724--726;
- complete index: 773--794.

## Page inspection ledger

| Physical page(s) | Surface | Verdict | Observation |
|---:|---|---|---|
| 19--21 | body TOC | PASS | Public Part VIII, exact Chapter 53, addition sections, and Chapter 54 appear once in order with separated numbers, titles, and folios. |
| 24 | annex TOC | PASS | P8 appears once and targets physical 725 without number/title or title/folio fusion. |
| 73, 439 | former pending consumers | PASS | Both formerly visible `??` placeholders are gone. Each link lands directly on exact `ch:intuitionistic-logic` at physical 503. |
| 500 | incoming transition | PASS | Propositional Proof Complexity closes cleanly. |
| 501--502 | public Part VIII and verso | PASS | The exact singular source command is governed into the fixed public title `Nonclassical Logics`; Part VIII appears once, followed by an intentional blank verso. |
| 503--506 | exact Chapter 53 | PASS | Convention, finite-support derivability, partial-order Kripke semantics, persistence proof, strong-completeness statement/sketch, examples, warning, exercises, Glivenko, negative translation, and the complete disjunction-property proof are legible and correctly ordered. |
| 506 | source/addition seam | PASS | The corrected italic `Reader note.` is exact and clean; no `oindent`/`extit` artifact remains. The IPL system card begins without collision. |
| 507--510 | figures and translation additions | PASS | A-137/A-138 figures, Kolmogorov/Kuroda variants, and the A-082 landscape table are unclipped and link to the genuine source Glivenko and negative-translation theorems. |
| 511--515 | later semantics additions | PASS | Algebraic, topological, BHK, first-order, and intermediate-logic additions remain visibly distinct, readable, and consumer-corrected to exact Section 53.1. |
| 516--517 | outgoing seam | PASS | The intentional blank verso is followed by Modal Logics on a clean open-right page. |
| 724--726 | Part VIII annex transition/context | PASS | The altered historical Intuitionistic annex items are absent; the P8 annex begins with its remaining distinct modal material and clean furniture. |
| 773--794 | complete index | PASS | All 22 pages were inspected or proven pixel-identical to the immediately inspected pre-fix pages. Exhaustive vertically-intersecting cross-column analysis found zero pairs below 4 pt. Minimum clearance is 16.606941 pt on physical 775 (`equiv-` / `CIC`). |

No governed page shows clipping, cross-column collision, accidental overprint,
broken figure/table, missing glyph, malformed transition, bad folio, or
running-head collision.

## Navigation and literal-text checks

The PDF contains 3,625 named destinations, all valid; 3,754 internal named
links and 400 URI links, all valid; and 411 outline entries, all in range. The
retained navigation audit is 1,860 bytes, SHA-256
`e3cf7eea667e4e0aad2212fa0b90c16e7c7e4e0f08b1fd46050f49b6fc959877`.

Relevant destinations and consumers include:

- public Part VIII to physical 501 and exact Chapter 53 to 503;
- exact Sections 53.1 and 53.2 to 503 and 505;
- exact exercises to 505 and exact Glivenko, negative-translation, and
  disjunction-property theorems to 505--506;
- the IPL system card and figures to 506--508;
- the translation table to 510 and algebraic definition to 511;
- the two former forward references on 73 and 439, now targeting Chapter 53;
- the addition consumers on 506, 507, 510, 512, and 513, all targeting genuine
  exact-source anchors or separately retained addition anchors.

The complete-index bounding-box evidence is 723,307 bytes, SHA-256
`a0de076640339bd7c43b26a827dc74f951f9b1ae471dd39cf64dfde43a63c402`.
Independent pypdf and pdfplumber full-document scans both find zero literal
`??` occurrences.

## Verdict and limits

The exact inherited source at lines 12970--13200, its governed public-title
mapping, complete Intuitionistic chapter, six-slice OPEN addition, every seam,
all actual consumers, TOCs, outlines, links, former placeholders, annex
transition, and complete index pass this fresh candidate-bound inspection.

The whole publication remains **OPEN**, not release-ready. All 1,055 source
units and all handbook semantic units remain unadmitted, all 615 register
obligations remain OPEN, six acquisition gaps and all external assignments
remain unresolved, and no human acceptance exists. This report does not turn
source/static/build/visual evidence into semantic admission, completed AI
review, register closure, or user acceptance.
