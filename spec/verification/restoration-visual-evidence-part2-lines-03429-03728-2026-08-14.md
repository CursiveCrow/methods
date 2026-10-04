# Restoration visual evidence for Part II source lines 03429--03728 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate, with the exact restored-page
subverdict PASS.** Exact restored source lines 3429--3728 map to physical PDF
pages 103--107 inclusive. Every page in that five-page exact-source envelope
was freshly rendered at fixed 200 dpi from the pinned PDF and inspected once
at original render resolution. All five exact-source pages pass.

Six route-transition pages, physical 101--102 and 108--111, were also freshly
rendered and inspected. They establish the preceding exact chapter endpoint,
intentional blank recto boundary, shared exact/editorial endpoint, downstream
editorial continuation, intentional blank verso, and next chapter opener. All
six pass. Thus the complete eleven-page route envelope, physical 101--111, is
11 PASS and 0 FAIL.

Ten additional consumer and route pages outside that envelope were freshly
rendered and inspected: physical 13, 14, 41, 42, 54, 56, 73, 162, 602, and
666. Their result is 6 PASS and 4 FAIL. The former `ch:fol-semantics`
placeholder on physical 42 now visibly resolves: the sentence reads
`chapter 8 and chapter 9`. Physical pages 54, 56, and 73 still print one
literal `??` each for later-source targets. Physical page 162 prints the
malformed sentence fragment `those of The recursive satisfaction
definition`; the newly resolved Section 9.2 reference on that page is correct,
but the retained `those of` makes the consumer prose visibly defective.

Across all 21 freshly inspected pages, the result is therefore **17 PASS and
4 FAIL**. No clipping, overlap, margin collision, malformed chapter or section
heading, broken continuation, missing mathematical glyph, formula collision,
malformed proof display, table collision, unintended blank, running-head
collision, page-number defect, or route-reconciliation defect was found. The
five exact-source pages themselves are visually sound, but their passing
layout does not override the four reader-facing defects on targeted consumer
pages.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, static validation, build approval, AI review,
admission, section locking, human review, user acceptance, or terminal
readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `b8807aa3610952b595096325a3788d15054b395b8723a8f624bebec03d78e2be`
- File size: 4,294,798 bytes
- Physical page count: 801
- Page geometry for every inspected page: US Letter, 612 x 792 points,
  rotation 0
- PDF version: 1.5
- Renderer: Poppler `pdftoppm` 26.05.0
- Text extractor used only for the full-PDF placeholder scan: Poppler
  `pdftotext` 24.04.0
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 103--107 inclusive
- Route-transition pages: 101--102 and 108--111
- Targeted outside-envelope pages: 13, 14, 41, 42, 54, 56, 73, 162, 602,
  and 666
- Render dimensions: 1700 x 2200 pixels for every inspected page
- Retained ignored render directory:
  `tmp/pdfs/part2-lines-03429-03728-b8807aa3-2026-08-14/`

The PDF hash and byte count were checked before rendering, after rendering,
after inspection, and at evidence freeze. They remained unchanged. The PDF
was not rebuilt by this audit. No visual verdict from an earlier PDF hash was
reused.

## Physical-page and source mapping

The exact restoration records, source-unit crosswalk, route inputs, current
auxiliary labels, fresh full-PDF text extraction, TOC, bookmarks, and rendered
headings establish this map:

| Exact source scope or route context | Units | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---:|---|
| preceding `SRC-03240-03428` endpoint | 222--246 | 101 | 77 | Chapter 8 proof continuation and exact endpoint |
| intentional blank | -- | 102 | -- | blank verso before Chapter 9 |
| `SRC-03429-03518` | 247--256 | 103--104 | 79--80 | Chapter 9 and Section 9.1; structures, assignments, term values, lemmas, and proofs |
| `SRC-03519-03680` | 257--267 | 104--106 | 80--82 | Section 9.2; satisfaction, coincidence, substitution, alpha-invariance, sentence independence, truth, validity, and consequence |
| `SRC-03681-03728` | 268--270 | 106--107 | 82--83 | Section 9.3; restricted quantification and both translation examples |
| separately attributed editorial continuation | -- | 107--109 | 83--85 | shared physical 107 after the exact endpoint, then Section 9.4 remainder |
| intentional blank | -- | 110 | -- | blank verso before Chapter 10 |
| downstream route opener | -- | 111 | 87 | Chapter 10, *First-Order Calculi* |

The source boundaries on physical 104, 106, and 107 are shared boundaries.
Physical 107 first completes exact inherited Example 9.13 and Example 9.14,
then prints the explicit reader note separating the editorial Section 9.4
remainder from the exact source chapter. The exact source content is neither
truncated nor duplicated at that boundary.

The three exact restoration artifacts remain separately hash-identified:

| Source interval | Artifact bytes | Artifact LF lines | Artifact SHA-256 |
|---|---:|---:|---|
| `SRC-03429-03518` | 3,359 | 90 | `ef123d37fb24d3d7194768867468e3e739e92c066e855195b0f7f6b040892d0b` |
| `SRC-03519-03680` | 6,293 | 162 | `b1f502609bb084acff222a7431e05caed5273acd19c367b45cbdccb63f306897` |
| `SRC-03681-03728` | 1,599 | 48 | `f944101df4bb8f02bc50a5ad67ba1451396d63dd1523b2409050e85dc2c88fbe` |

These artifact identities help locate the rendered scope; this report does
not independently reperform or promote the source-fidelity claim.

## Exact and transition 11-page render ledger

`restored` identifies a page carrying exact inherited content; `prior`
identifies the immediately preceding exact-source endpoint; `blank` identifies
an intentional blank verso; `editorial` identifies the separately attributed
continuation; and `route` identifies the next chapter opener. Physical 104,
106, and 107 are shared exact-source boundaries. Each retained PNG was opened
and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 101 | 77 | prior | `route-101.png` | 490110 | 1700x2200 | `9e412d4381001caed1538933c568acdbcdec55dced5f984a26fb2647194efde8` | PASS |
| 102 | -- | blank | `route-102.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 103 | 79 | restored | `restored-103.png` | 290581 | 1700x2200 | `29f0cd3470de7bd0c5c670cbf587992b8df5fe74e10cb1b7abd04b3f7aa8d745` | PASS |
| 104 | 80 | restored/shared | `restored-104.png` | 287148 | 1700x2200 | `b16c8820d9bfee023138b9df82aed5b08243eb0b4240a0af184920f556ccef77` | PASS |
| 105 | 81 | restored | `restored-105.png` | 453320 | 1700x2200 | `3f104993103513d50804b22cbb66c05cbbe738519a6226366b7b0e899315fa13` | PASS |
| 106 | 82 | restored/shared | `restored-106.png` | 335275 | 1700x2200 | `e9bbe290e9b1ba974e371cb45548f0a8e0ab02e80606f43cdb69aeda1812fc42` | PASS |
| 107 | 83 | restored/editorial shared | `restored-107.png` | 361738 | 1700x2200 | `414920ebffd0f57db85ed0539a6e30a7183856fa52d9599ad3491a6639bfde8f` | PASS |
| 108 | 84 | editorial | `route-108.png` | 352140 | 1700x2200 | `f744b12c509aeb643018bc5ecacecf50943dd5ffc736d472d8395d59af0cbf39` | PASS |
| 109 | 85 | editorial | `route-109.png` | 171312 | 1700x2200 | `1f29163a971a2ff5065ce0929f0b4518fb131b5f458684530bb688580f934192` | PASS |
| 110 | -- | blank | `route-110.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 111 | 87 | route | `route-111.png` | 259253 | 1700x2200 | `bc13a2bf2c54d2375162a909e1dcc847918533e436ef9ce4f52a6c83e3421dd4` | PASS |

## Targeted 10-page render ledger

These pages are outside the exact-source envelope. They were inspected only
for TOC and public-part placement, the resolved Chapter 9 consumer, every
remaining literal placeholder, or a newly resolved exact-semantics consumer.
They receive no exact-source visual credit.

| Physical | Printed | Target | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 13 | ix | TOC Chapter 9 placement | `toc-013.png` | 311188 | 1700x2200 | `8bf162059d24a1c29b665e069d8b48ebed0d62a82091cfe162f51f3cd95da84c` | PASS |
| 14 | x | TOC public-part boundary | `toc-014.png` | 337897 | 1700x2200 | `8d9333674b568d77d6db9a71288d49a273a004d434ad3e2b958d49d056644dca` | PASS |
| 41 | 17 | early consumer continuity | `earlyref-041.png` | 362651 | 1700x2200 | `419f23fa4317301e6d13705dd1fea60d126bc6159cf356ac145ee110c28edb98` | PASS |
| 42 | 18 | former `ch:fol-semantics` placeholder | `earlyref-042.png` | 382977 | 1700x2200 | `47b2359db9f5920168dcb99687dd23cb9e0ff1df3bb9bc98ec079ef4d74b9b7d` | PASS |
| 54 | 30 | remaining deduction placeholder | `unresolved-054.png` | 342663 | 1700x2200 | `bb0005f5e3e588c98f7407eb1914af8ff86f43b88eee6c3f0e706f2d40de86f7` | **FAIL** |
| 56 | 32 | remaining theories placeholder | `unresolved-056.png` | 117720 | 1700x2200 | `9e2f2b0e1b9b20e4099e80b287dd34ca859f88bac46d6d305fe2d394619212af` | **FAIL** |
| 73 | 49 | remaining intuitionistic placeholder | `unresolved-073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 162 | 138 | Section 9.2 consumer | `variant-162.png` | 403472 | 1700x2200 | `905854ce9e2fe3cbacfac432c6927235fae74242a9e1a880f4278bc5417cf869` | **FAIL** |
| 602 | 578 | Theorem 9.9 consumer | `workflow-602.png` | 449328 | 1700x2200 | `8554e08beb14dafbce4b0dbb511f34afc282ba65ac5e91b70edc1a1f946d0094` | PASS |
| 666 | 642 | Corollary 9.10 and Theorem 9.9 consumers | `annex-666.png` | 413607 | 1700x2200 | `3aced6c56f1b51ebd41f3f12efdc0620362b2b94dbaeedc8a158d59d319637d7` | PASS |

## Page-specific visual findings

### Exact semantics chapter

- Physical 103 cleanly opens Chapter 9, *Structures, Satisfaction, and
  Translation*, and Section 9.1. The three-part structure definition,
  signature-extension tuples, arity subscripts, expansion/reduct notation,
  assignments, and opening continuation are sharp, aligned, and unclipped.
- Physical 104 cleanly continues the assignment definition, term-value
  recursion, term-coincidence and substitution lemmas with complete proofs,
  and the nine-clause satisfaction display. Update arrows, semantic brackets,
  negated satisfaction, quantifiers, and proof squares remain distinct and
  aligned.
- Physical 105 preserves formula coincidence, the full substitution lemma and
  proof, alpha-invariance, substitutions, set differences, freshness
  conditions, and proof continuations without collision or truncation.
- Physical 106 cleanly closes alpha-invariance, prints assignment independence,
  truth/validity/consequence, distinguishes logical equivalence from
  alpha-equivalence, and opens Section 9.3. Restricted-quantifier displays and
  the opening quantifier-order example fit within the margins.
- Physical 107 completes both translation examples before the explicit reader
  note and editorial Section 9.4. Formula nesting, negation, quantifier order,
  quotation marks, exact-source endpoint, and shared boundary remain legible.
  The page running head names Section 9.4 because that section begins later on
  the same physical page; it neither collides with content nor conceals the
  preceding Section 9.3 continuation.

### Route transitions and consumers

- Physical 101 cleanly completes the preceding restored syntax proof. Physical
  102 is wholly blank, without stray ink, header, footer, or page number.
- Physical 108 preserves the editorial axiomatization table and following
  definitions without clipping or row collision. Physical 109 cleanly closes
  the editorial remainder; its remaining whitespace is the ordinary short
  chapter close, not an unintended blank page. Physical 110 is wholly blank,
  and physical 111 cleanly opens Chapter 10.
- TOC physical 13 places Chapter 9 and Sections 9.1--9.4 after Chapter 8 and
  before Chapter 10. TOC physical 14 retains `III Model Theory` as the next
  public part. The auxiliary bookmark hierarchy independently places Chapters
  8, 9, and 10 beneath `part.2`, with Sections 9.1--9.4 beneath Chapter 9; this
  is a structural check, not a rendered-page verdict.
- The cross-page early consumer on physical 42 now reads `chapter 8 and chapter
  9`. Thus both the syntax and semantics targets resolve visibly; physical 41
  and 42 have no remaining placeholder or layout defect.
- Physical 602 cleanly renders `Theorem 9.9` in the metatheorem proof-plan
  audit. Physical 666 cleanly renders `Corollary 9.10` and `Theorem 9.9` in the
  proof annex, with no placeholder or reference collision.
- Physical 162 visibly resolves the intended target as `Section 9.2`, but its
  sentence reads `Term evaluation and the atomic and Boolean clauses are those
  of The recursive satisfaction definition in Section 9.2`. The duplicated
  construction is a reader-facing prose defect. Its current source is
  `handbook/parts/p02/variants.tex:74--75`.

## Visible failure localization

A page-by-page text-extraction scan of all 801 physical pages found literal
`??` on exactly three pages. All three were inspected in their fresh 200-dpi
renders. The fourth failure is the separately localized malformed consumer
sentence on physical 162.

| Physical page | Visible count | Reader-facing phrase | Defect or pending target |
|---:|---:|---|---|
| 54 | 1 | `defined in ??` | `ch:fol-deduction` |
| 56 | 1 | `used in ??` | `ch:fol-theories` |
| 73 | 1 | `made exact in ??` | `ch:intuitionistic-logic` |
| 162 | 0 | `those of The recursive satisfaction definition in Section 9.2` | malformed consumer prose at `handbook/parts/p02/variants.tex:74--75` |

The earlier fourth placeholder, `ch:fol-semantics`, is absent from the full
801-page extraction and visibly resolved on physical 42. The three surviving
placeholders belong to later restoration work, but they remain reader-visible
defects in this pinned PDF.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No inspected text, formula, proof square, table, heading, header, footer, or page number is cut off or crosses a page edge. |
| Exact source chapter and boundaries | PASS | Chapter 9 begins on 103; Sections 9.1, 9.2, and 9.3 occur on 103, 104, and 106; exact content ends on shared 107 before the explicit editorial reader note. |
| Headings, running heads, and page numbers | PASS | Printed pages 77 and 79--87 are ordered and positioned consistently; shared page 107 and the following chapter transition remain unambiguous. |
| Formulas and local notation | PASS | Domains, reducts, assignment updates, semantic brackets, satisfaction, consequence, alpha-equivalence, logical equivalence, quantifiers, substitutions, and set operations render distinctly. |
| Proof displays and continuations | PASS | Every exact theorem, lemma, corollary, proof square, induction continuation, and cross-page formula resumes coherently without duplication or truncation. |
| Lists, tables, and examples | PASS | The structure list, satisfaction array, quantifier examples, and targeted editorial table are complete, ordered, and unclipped. |
| Fonts and glyphs | PASS | Roman, italic, bold, calligraphic, Greek, logical, set-theoretic, substitution, assignment, proof, and alpha-equivalence glyphs show no missing-glyph box or visible substitution. |
| Intentional blanks | PASS | Physical 102 and 110 are wholly blank with no stray mark. |
| TOC, route, and resolved exact consumers | PASS | Chapter 9 is subordinate within Part II; the early Chapter 9 consumer and the Section 9.2, Theorem 9.9, and Corollary 9.10 targets resolve to visible numbers. |
| Consumer prose | **FAIL** | Physical 162 contains the malformed `those of The recursive satisfaction definition` construction. |
| Remaining visible references | **FAIL** | Literal `??` remains on physical 54, 56, and 73 at the three later-source labels listed above. |

## Coverage and integrity checks

- Exact-source expected set: every integer physical page 103--107, count 5.
- Exact-source render set: exactly one `restored-NNN.png` for each expected
  page, with no missing, duplicate, or unknown page, count 5.
- Route-transition expected set: 101, 102, 108, 109, 110, and 111, count 6.
- Route-transition render set: exactly one governed PNG for each expected
  target, with no missing, duplicate, or unknown page, count 6.
- Outside-envelope target set: 13, 14, 41, 42, 54, 56, 73, 162, 602, and
  666, count 10.
- Outside-envelope render set: exactly one governed PNG for each expected
  target, with no missing, duplicate, or unknown page, count 10.
- Total inspected render set: 21 distinct physical pages, each inspected once;
  17 PASS and 4 FAIL.
- Every PNG byte count, pixel dimension, and SHA-256 digest is recorded in the
  two ledgers above. Every render is 1700 x 2200 pixels.
- Repeated byte/digest identity for physical 102 and 110 is expected: both are
  the same wholly blank 200-dpi raster.
- The retained render directory contains only the 21 governed PNGs after
  inspection.
- The report is UTF-8 without BOM and uses LF line endings only.
- Repository-wide `git diff --check` and the report-specific no-index
  whitespace check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 801 pages, 4,294,798 bytes,
  title `The Methods of Reason`, SHA-256
  `b8807aa3610952b595096325a3788d15054b395b8723a8f624bebec03d78e2be`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page carrying exact restored source lines 3429--3728 and every
listed transition or consumer target was freshly rendered at 200 dpi,
inspected once, hash-ledgered, and assigned the visual verdict recorded above.
The exact five-page semantics chapter envelope passes. Three visible reference
placeholders and one malformed consumer sentence keep the broader bounded
visual gate at FAIL.

It does not promote any source unit, packet, register record, semantic row,
topic, section, AI review, build result, human review, admission decision,
user acceptance, or release-readiness claim.
