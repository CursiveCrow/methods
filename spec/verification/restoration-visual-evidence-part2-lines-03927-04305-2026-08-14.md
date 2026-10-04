# Restoration visual evidence for Part II source lines 03927--04305 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Exact restored source
lines 3927--4305 map to physical PDF pages 113--118 inclusive. Every page in
that six-page exact-source envelope was freshly rendered at fixed 200 dpi
from the pinned PDF and inspected once at original render resolution. All six
exact-source pages pass their visual checks.

Physical 112, the final page of the preceding exact chapter, and physical
119, the continuation of the following editorial supplement, were also
freshly rendered and inspected as the two route transitions. Both pass.

Seven distinct contents or consumer pages outside that eight-page route set
were inspected: physical 13, 54, 73, 111, 122, 153, and 397. Physical 13, 54,
122, 153, and 397 pass. Physical 54 now visibly resolves the former
`ch:fol-deduction` placeholder as `chapter 11`. Physical 111 now visibly
resolves the reduct lemma, chapter, and soundness references as `lemma 11.2`,
`chapter 11`, and `theorem 11.6`. Physical 122 visibly resolves both
soundness references as `Theorem 11.6` and `Theorem 11.7`; physical 153
resolves `Theorem 11.6`; and physical 397 resolves `Theorem 11.7`.

Physical 73 still visibly prints one literal `??` for
`ch:intuitionistic-logic`. Physical 111 still visibly prints one literal `??`
for `thm:fol-completeness`. These two pages fail. The expected completeness
repair is therefore **not present in this pinned PDF**.

Across all fifteen distinct inspected physical pages, the result is therefore
**13 PASS and 2 FAIL**. Physical 111 is ledgered and counted exactly once even
though it is both a changed consumer and a former-placeholder target.

No clipping, overlap, margin collision, malformed chapter or section heading,
broken continuation, unreadable mathematical glyph, formula collision,
malformed proof or rule display, list collision, table collision, unintended
blank, running-head collision, page-number defect, or route-transition defect
was found. The six-page exact-source envelope is visually sound. The two
remaining reader-facing reference placeholders keep the governed checkpoint
open.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, static validation, build approval, AI review,
admission, section locking, human review, user acceptance, or terminal
readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `91a51c92ac34ef34d9d47978a120a33100d9532e5f5e85c0b6dfe2973db3951d`
- File size: 4,309,953 bytes
- Physical page count: 805
- PDF version: 1.5
- Default page geometry: US Letter, 612 x 792 points, rotation 0
- Landscape consumer pages: physical 122 and 153, US Letter with rotation 90
- Renderer: Poppler `pdftoppm` 24.04.0, executable SHA-256
  `23335d0ec465c53c2919fbec02574d4c14936fce2f22d8673bfd3e4e48c66091`
- Text extractor used only to locate literal placeholders and confirm targeted
  wording: Poppler `pdftotext` 24.04.0, executable SHA-256
  `6f1f7d8db783bd2fac74043dca400a53f42d0a03c4e7f81b2c51ed436c13faeb`
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 113--118 inclusive
- Route-transition pages: 112 and 119
- Outside-envelope contents and consumer pages: 13, 54, 73, 111, 122, 153,
  and 397
- Governed physical-page set: 13, 54, 73, 111, 112, 113, 114, 115, 116,
  117, 118, 119, 122, 153, and 397
- Portrait render dimensions: 1700 x 2200 pixels
- Landscape render dimensions: 2200 x 1700 pixels
- Retained ignored render directory:
  `tmp/pdfs/visual-audit-lines-03927-04305-91a51c92-20260814/`

The PDF title, page count, byte count, and hash were checked before rendering,
after rendering, after extraction, after inspection, and at evidence freeze.
They remained unchanged. The PDF was not rebuilt by this audit, and no visual
verdict from an earlier PDF hash was reused.

## Physical-page and source mapping

The exact restoration artifacts, source-unit evidence, Part II route, full-PDF
text extraction, auxiliary label map, and rendered headings establish this
map. A physical page may contain the end of one exact interval and the start
of the next, but every physical page is governed only once in the render
ledger.

| Source scope or route context | Units | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---:|---|
| preceding exact route close | 280--281 | 112 | 88 | Section 10.1, *Axiomatization errors*, immediately before Chapter 11 |
| `SRC-03927-04061` | 282--289 | 113--115 | 89--91 | Chapter 11 opening, natural-deduction rules, derivability, reduct lemma and proof, and three examples |
| `SRC-04062-04108` | 290 | 115 | 91 | First-order sequent rules and equality replacement explanation |
| `SRC-04109-04213` | 291--295 | 116--117 | 92--93 | Soundness section, two theorems, and both complete proofs |
| `SRC-04214-04234` | 296--297 | 117 | 93 | Quantifier-rule errors and five-item warning |
| `SRC-04235-04305` | 298--307 | 117--118 | 93--94 | Exercises section and nine exercises |
| following editorial route | -- | 118--119 | 94--95 | Supplement begins after the exact exercises on 118 and continues with equality metatheory on 119 |

The five exact restoration artifacts remain separately hash-identified:

| Source interval | Artifact bytes | Artifact LF lines | Artifact SHA-256 |
|---|---:|---:|---|
| `SRC-03927-04061` | 4,975 | 135 | `2ad2846970d4976177b0fbb8ac59ff8106253f5d155a5e4861956f7f651bf480` |
| `SRC-04062-04108` | 1,929 | 47 | `adc1b454faf1f14072796fe12ce17de288bc6b4e9d1d9a79e83cdfc7b1f19209` |
| `SRC-04109-04213` | 5,050 | 105 | `0d45236d978cd3b75f7e536fe45d9516ed0d735ab6dc8745137b8685959075f1` |
| `SRC-04214-04234` | 927 | 21 | `5acc307f5a2ef1ad5372e6426b301ffcb49d010003184aa527c109f54e6c1578` |
| `SRC-04235-04305` | 1,964 | 71 | `6d5c4d14b406be294ca731d91e02cd5c966a8b0b4d3df53eff0a11e4aa6fe82d` |

These identities locate the rendered scope. This report does not independently
reperform or promote the source-fidelity or static-validation claims attached
to those artifacts.

## Fifteen-page render ledger

`contents` identifies the table-of-contents consumer; `targeted` identifies a
former-placeholder page; `consumer` identifies a page whose visible reference
number changed because of this tranche; `restored` identifies exact inherited
content; and `transition` identifies the immediately adjacent route. Each
physical page appears exactly once in this ledger, and each retained PNG was
opened and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 13 | ix | contents | `p013.png` | 295208 | 1700x2200 | `fe78f1fe41f307824b114ce18f2d721fc9d3513def0e627f8c6da31c35df95b9` | PASS |
| 54 | 30 | targeted/consumer | `p054.png` | 343230 | 1700x2200 | `bbf3d88aceb23c7c47359c0b7d237e97ef5b17f21abdf8e4a2cf21f7afb44168` | PASS |
| 73 | 49 | targeted | `p073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 111 | 87 | targeted/consumer | `p111.png` | 458147 | 1700x2200 | `933037e745fdfcb7e542e316cfb07d3ccee321c97af90bae88dbd5c619f21620` | **FAIL** |
| 112 | 88 | transition | `p112.png` | 141435 | 1700x2200 | `e7895f468d3244700bf4ee49180ebed12fabafeb82bdb3bc2d79acd1453c6c43` | PASS |
| 113 | 89 | restored | `p113.png` | 229748 | 1700x2200 | `6aec63228c63e6d2e475935b4e19ffe4d6245dbf3c99f20761fbbeab24d49f45` | PASS |
| 114 | 90 | restored | `p114.png` | 344477 | 1700x2200 | `c048281762e0bb673e469f6907ef28122cf11871c1abba0b28b24ef4d8a89fd4` | PASS |
| 115 | 91 | restored | `p115.png` | 334132 | 1700x2200 | `5c849afacf31ef4f856d3b28632326c3042118d2eb5b4744fadd16ecba57c18e` | PASS |
| 116 | 92 | restored | `p116.png` | 452462 | 1700x2200 | `23bef36f82488e5d4447aa514de87eb0bd5d5bac62e50cecb93870ca01417de9` | PASS |
| 117 | 93 | restored | `p117.png` | 390296 | 1700x2200 | `444bc2158b51d3f2494cb8bc27c9c2c4b1eebff03ccc77b1c6491bc757c1376d` | PASS |
| 118 | 94 | restored/transition | `p118.png` | 368606 | 1700x2200 | `cc858e0824b7dfbaba903d71026b99ab2a04af905bb368975d3bd29953661b5e` | PASS |
| 119 | 95 | transition | `p119.png` | 364072 | 1700x2200 | `ca9e74ca829b0e90891127c4b1746ee07e2b0b12e2d389de7b48cec2c6ea3825` | PASS |
| 122 | 98 | consumer | `p122.png` | 290274 | 2200x1700 | `c13da1d3593aa3ad7cd32397b59f6680826c6afaec7de68052bde5c50b89920d` | PASS |
| 153 | 129 | consumer | `p153.png` | 304393 | 2200x1700 | `ab24a83ed58e38759e9a90e88e01219847493dc0cadf695589aba22cb10770f0` | PASS |
| 397 | 373 | consumer | `p397.png` | 415228 | 1700x2200 | `4a0ae32ba52f78f9913c76b863bfa0a8cee1505719b3b945ffe6be759568cd50` | PASS |

## Page-specific visual findings

### Exact Chapter 11 and its transitions

- Physical 112 cleanly closes Chapter 10 with Section 10.1 and its complete
  seven-item warning. Its large lower whitespace is the ordinary close of a
  short exact chapter, not an unintended blank.
- Physical 113 cleanly opens Chapter 11, *First-Order Deduction*. The chapter
  and Section 11.1 headings, quantifier rules, eigenvariable conditions,
  alpha-conversion display, surrounding prose, and printed page number are
  sharp, aligned, and unclipped.
- Physical 114 cleanly continues the alpha-conversion discussion, renders the
  two equality rules, Definition 11.1, Lemma 11.2 and its complete proof, and
  the seven-line universal-reasoning derivation. Logical symbols, assignment
  updates, proof square, and derivation annotations remain distinct.
- Physical 115 cleanly renders Examples 11.4 and 11.5, then Section 11.2 with
  the four first-order sequent rules, equality initial sequent, replacement
  rule, and the complete symmetric-replacement explanation. No rule line,
  side condition, or formula crosses a margin.
- Physical 116 cleanly renders Theorems 11.6 and 11.7, the complete
  natural-deduction soundness proof, and the first part of the sequent
  soundness proof. The cross-page proof continuation is unambiguous.
- Physical 117 cleanly completes the sequent soundness proof, including its
  proof square, then renders Section 11.4, all five warning items, Section
  11.5, and the opening exercise without overlap or truncation.
- Physical 118 cleanly continues Exercises 11.9--11.17 and then begins the
  separately attributed editorial supplement. The exact-source ending and
  following-route beginning are visibly ordered with no duplicate exercise or
  missing transition.
- Physical 119 cleanly continues the supplement with Section 11.6, derived
  equality laws, four displayed consequences, status line, and the start of
  Section 11.7. The preceding exact material is not duplicated.

### Contents and changed consumers

- Physical 13 lists Chapter 11 as *First-Order Deduction* on printed page 89,
  with Sections 11.1--11.9 in order. Dot leaders, hierarchy, page numbers,
  and the following Chapter 12 entry are aligned and unclipped.
- Physical 54 now reads `active calculus until that calculus is defined in
  chapter 11`. The former `ch:fol-deduction` placeholder is absent.
- Physical 111 now reads `invariance under reduct (lemma 11.2)`, `that lemma
  is stated in chapter 11`, and `soundness (theorem 11.6)`. The theorem,
  complete proof, proof square, and following derivability paragraph render
  cleanly. The page nevertheless fails because the adjacent completeness
  reference remains a literal `??`.
- Physical 122 is an intentional landscape proof-system comparison table.
  Its natural-deduction row visibly cites `Theorem 11.6`, and its LK row cites
  `Theorem 11.7`. The five columns, table rules, rotated running head, and all
  row text remain within the page.
- Physical 153 is an intentional landscape metatheorem-summary table. Its
  natural-deduction soundness row visibly cites `Theorem 11.6`; all eight
  result rows, formulas, citations, table rules, rotated running head, and
  printed page number are legible and unclipped.
- Physical 397 visibly states that propositional and first-order soundness
  remain proved Theorems 7.2 and 11.7. The consumer reference is resolved and
  the page layout passes. The same page also visibly carries the pre-existing
  boxed `STUB. A-070`; that is a separate content-completion blocker, not a
  rendering failure or a result of this restoration tranche.

### Visible construction-status text

The inspected renders also contain two explicit construction-status markers
that are not undefined-reference render failures:

| Physical page | Visible marker | Standing in this report |
|---:|---|---|
| 118 | `OPEN.` preceding the separately attributed equality, Hilbert, tableau, and comparison supplement | Properly rendered following-route status text; content, review, and admission remain open |
| 397 | boxed `STUB. A-070` for relevance and affine comparison rows | Properly rendered but still a separate final-publication content blocker |

Neither marker is promoted, closed, or excused by this visual report. Their
presence must be handled by the content and admission workflow. They do not
alter the bounded raster-layout verdict for the restored interval.

## Complete visible-placeholder localization

A page-by-page Poppler extraction scan of all 805 physical pages found exactly
two literal `??` occurrences on exactly two pages. Both pages were opened in
their fresh 200-dpi renders. The mapping to unresolved source labels is:

| Physical page | Visible count | Reader-facing phrase or role | Pending label |
|---:|---:|---|---|
| 73 | 1 | `made exact in ??` | `ch:intuitionistic-logic` |
| 111 | 1 | `completeness (??, under its Axiom-of-Choice hypothesis)` | `thm:fol-completeness` |

The former physical-54 `ch:fol-deduction` placeholder is absent. The former
three physical-111 placeholders for `lem:reduct-invariance`,
`ch:fol-deduction`, and `thm:fol-soundness` are also absent and visibly
resolved. No uninspected literal-`??` page remains in this PDF.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No inspected text, formula, rule, proof square, list item, table cell, heading, header, footer, or page number is cut off or crosses a page edge. |
| Exact chapter and boundaries | PASS | Chapter 10 closes on physical 112; exact Chapter 11 occupies 113--118; the editorial supplement begins after the exact exercises on 118 and continues on 119 without duplication or route ambiguity. |
| Headings, running heads, and page numbers | PASS | Printed pages 88--95 are ordered and consistently positioned; chapter and section headings do not collide with content. |
| Equations, rules, and symbols | PASS | Quantifiers, equality, alpha-conversion, derivability, satisfaction, assignment updates, sequent arrows, rule lines, eigenvariable conditions, proof squares, and logical glyphs are distinct and readable. |
| Proof display and continuity | PASS | Lemma 11.2 and Theorems 11.6--11.7 carry their reader-facing proofs in place, with clean continuations and visible proof squares. |
| Lists, examples, exercises, and warning | PASS | Three examples, nine exercises, and the five-item quantifier-error warning are complete, ordered, and unclipped. |
| Landscape tables | PASS | Physical 122 and 153 render at 2200 x 1700 pixels with complete columns, rows, rules, citations, rotated running heads, and page numbers. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, calligraphic, Greek, logical, set-theoretic, update-arrow, rule, and proof glyphs show no missing-glyph box or visible substitution. |
| Restored consumer references | PASS | Physical 54, 111, 122, 153, and 397 visibly resolve the restored chapter, reduct lemma, and soundness targets. |
| Remaining visible references | **FAIL** | Two literal `??` occurrences remain on physical 73 and 111 at the labels listed above. |

## Coverage and integrity checks

- Exact-source expected set: every integer physical page 113--118, count 6.
- Exact-source render set: exactly one governed PNG for each expected page,
  with no missing, duplicate, or unknown page, count 6.
- Route-transition expected set: physical 112 and 119, count 2.
- Route-transition render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 2.
- Outside-envelope contents and consumer set: physical 13, 54, 73, 111, 122,
  153, and 397, count 7.
- Outside-envelope render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 7.
- Total inspected render set: fifteen distinct physical pages, each inspected
  once; 13 PASS and 2 FAIL.
- Physical 111 is counted and ledgered once despite serving both as a changed
  consumer and as a former-placeholder target.
- Every governed PNG byte count, pixel dimension, and SHA-256 digest is
  recorded above. Thirteen governed renders are 1700 x 2200 pixels; physical
  122 and 153 are 2200 x 1700 pixels.
- The complete 805-page text scan found exactly two literal `??` occurrences,
  both localized above; no uninspected literal-placeholder page remains.
- The report is UTF-8 without BOM and uses LF line endings only.
- Repository-wide `git diff --check` and the report-specific no-index
  whitespace check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 805 pages, 4,309,953 bytes,
  title `The Methods of Reason`, SHA-256
  `91a51c92ac34ef34d9d47978a120a33100d9532e5f5e85c0b6dfe2973db3951d`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page carrying exact restored source lines 3927--4305 and every
listed transition, contents, or consumer target was freshly rendered at 200
dpi, inspected once, hash-ledgered, and assigned the visual verdict recorded
above. The exact-source envelope passes 6 of 6 pages. Two remaining visible
reference-placeholder pages keep the governed checkpoint at FAIL.

It makes no source-fidelity, mathematical-correctness, static-validation,
build-validation, AI-review, admission, section-locking, human-review,
user-acceptance, or release-readiness claim, and it promotes no source unit,
packet, register obligation, semantic row, topic, or section.
