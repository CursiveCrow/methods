# Restoration visual evidence for Part II source lines 03729--03926 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Exact restored source
lines 3729--3926 map to physical PDF pages 109--112 inclusive. Every page in
that four-page exact-source envelope was freshly rendered at fixed 200 dpi
from the pinned PDF and inspected once at original render resolution. Physical
109, 110, and 112 pass. Physical 111 fails because it visibly prints four
literal `??` reference placeholders. The exact-source envelope is therefore
**3 PASS and 1 FAIL**.

Physical 108, the intentional blank immediately before Chapter 10, and
physical 113, the following Chapter 11 opener, were also freshly rendered and
inspected. Both transition pages pass. Four targeted consumer pages outside
the route envelope were inspected: physical 54, 56, 73, and 164. Physical 56
now visibly resolves the former `ch:fol-theories` placeholder as `chapter 10`,
and physical 164 now reads `those of the recursive satisfaction definition`.
Those two pages pass. Physical 54 and 73 each retain one literal `??` for a
later-source target and fail.

Across all ten distinct inspected physical pages, the result is therefore
**7 PASS and 3 FAIL**. The ten-page set covers physical 111 exactly once even
though that page belongs both to the exact chapter and to the placeholder
audit.

No clipping, overlap, margin collision, malformed chapter or section heading,
broken continuation, unreadable mathematical glyph, formula collision,
malformed proof display, list collision, unintended blank, running-head
collision, page-number defect, or route-transition defect was found. The
restored chapter's layout is visually sound, but the four reader-facing
placeholders on physical 111 keep its exact-source visual gate open.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, static validation, build approval, AI review,
admission, section locking, human review, user acceptance, or terminal
readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `a575a9e58a3484532231a77756bb8584cecc673b9c5a54a6f84fdd53914f928a`
- File size: 4,295,277 bytes
- Physical page count: 801
- PDF version: 1.5
- Page geometry for every inspected page: US Letter, 612 x 792 points,
  rotation 0
- Renderer: Poppler `pdftoppm` 26.05.0, executable SHA-256
  `742cbbd9a00931ad16c6618410bc40471375d639a45c61c1d86f3dcfc54b6388`
- Text extractor used only to locate literal placeholders and confirm targeted
  wording: Poppler `pdftotext` 24.04.0
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 109--112 inclusive
- Route-transition pages: 108 and 113
- Targeted outside-envelope pages: 54, 56, 73, and 164
- Governed physical-page set: 54, 56, 73, 108, 109, 110, 111, 112, 113,
  and 164
- Render dimensions: 1700 x 2200 pixels for every inspected page
- Retained ignored render directory:
  `tmp/pdfs/visual-audit-lines-03729-03926-a575a9e5-20260814/`

The PDF title, page count, byte count, and hash were checked before rendering,
after rendering, after inspection, and at evidence freeze. They remained
unchanged. The PDF was not rebuilt by this audit, and no visual verdict from
an earlier PDF hash was reused.

## Physical-page and source mapping

The exact restoration artifacts, source-unit shard, full-PDF text extraction,
and rendered headings establish this map:

| Source scope or route context | Units | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---:|---|
| intentional blank | -- | 108 | -- | blank verso before Chapter 10 |
| `SRC-03729-03907` | 271--279 | 109--111 | 85--87 | Chapter 10, theory and axiomatization definitions, four examples, definitional-extension theorem, and complete proof |
| `SRC-03908-03926` | 280--281 | 112 | 88 | Section 10.1 and seven-item axiomatization-errors warning |
| downstream route opener | -- | 113 | 89 | Chapter 11, *First-Order Calculi* |

The two exact restoration artifacts remain separately hash-identified:

| Source interval | Artifact bytes | Artifact LF lines | Artifact SHA-256 |
|---|---:|---:|---|
| `SRC-03729-03907` | 7,790 | 179 | `4575656d845980e653cc7f686bcdb35bc32b75ce5e3bf85c5e1a570fedb63901` |
| `SRC-03908-03926` | 753 | 19 | `b7f176a3a01dfa15e003386c8b6c72cd2982d123f0dcbd03e370bf5add095c06` |

These identities locate the rendered scope. This report does not independently
reperform or promote the source-fidelity or static-validation claims attached
to those artifacts.

## Ten-page render ledger

`targeted` identifies a consumer inspected for a prior repair or a remaining
placeholder; `blank` identifies the intentional chapter boundary; `restored`
identifies exact inherited content; and `route` identifies the following
chapter opener. Each physical page appears exactly once in this ledger, and
each retained PNG was opened and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 54 | 30 | targeted | `p054.png` | 342663 | 1700x2200 | `bb0005f5e3e588c98f7407eb1914af8ff86f43b88eee6c3f0e706f2d40de86f7` | **FAIL** |
| 56 | 32 | targeted | `p056.png` | 119325 | 1700x2200 | `fe2094b562fb06fcbb05f1430c49734449e8b839548715dab4d15b5c2fe74b0d` | PASS |
| 73 | 49 | targeted | `p073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 108 | -- | blank | `p108.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 109 | 85 | restored | `p109.png` | 287307 | 1700x2200 | `f97189469b16339f72e4017220538fe9effa9d046afcc04c06c5c60f86197bc9` | PASS |
| 110 | 86 | restored | `p110.png` | 327559 | 1700x2200 | `25820c2e6cbfab9de759c687cd3860d60dbeae8398da8e351c6e0ef59a792b9e` | PASS |
| 111 | 87 | restored/placeholder target | `p111.png` | 455745 | 1700x2200 | `7d5c08e2e03664302cf9d8caaf607a36aa4b99dc730c5c07698f4e5873506cc5` | **FAIL** |
| 112 | 88 | restored | `p112.png` | 141435 | 1700x2200 | `e7895f468d3244700bf4ee49180ebed12fabafeb82bdb3bc2d79acd1453c6c43` | PASS |
| 113 | 89 | route | `p113.png` | 257039 | 1700x2200 | `c2af8d2dfdcc5974cac224ade8f9de1f5be58e5c34c1f2d45a04121469e05c11` | PASS |
| 164 | 140 | targeted | `p164.png` | 403564 | 1700x2200 | `7a2ed62f0c4c68432bfb9e4dd2010d2e5b495c00f9692b1cc22e5ca21a196d36` | PASS |

## Page-specific visual findings

### Exact Chapter 10 and its transitions

- Physical 108 is wholly blank, with no stray ink, header, footer, or page
  number. It correctly supplies the verso before the recto chapter opener.
- Physical 109 cleanly opens Chapter 10, *Theories and Axiomatization*.
  Definitions 10.1 and 10.2, the structure-theory and semantic-closure
  displays, and the opening of Example 10.3 are sharp, aligned, and unclipped.
- Physical 110 continues Example 10.3 and cleanly renders Examples 10.4--10.6.
  Quantifier strings, equality and inequality, the indexed finite conjunction,
  signature symbols, and the defining-axiom display remain distinct within the
  margins.
- Physical 111 prints Theorem 10.7, both numbered clauses, the complete proof,
  its proof square, and the following derivability paragraph without overlap,
  truncation, or broken proof continuity. The page nevertheless fails because
  it visibly contains four literal `??` placeholders.
- Physical 112 cleanly prints Section 10.1 and all seven ordered warning items.
  The large lower whitespace is the ordinary close of this short exact
  chapter, not an unintended blank page.
- Physical 113 cleanly opens Chapter 11. Its chapter heading, introductory
  paragraph, Section 11.1 heading, derivability display, reduct lemma, running
  pagination, and following-route transition are legible and unclipped.

### Targeted repaired and pending consumers

- Physical 56 now reads `the definition of deductive completeness used in
  chapter 10`. The former `ch:fol-theories` placeholder is absent, and the
  resolved chapter number is visibly correct.
- Physical 164 now reads `the atomic and Boolean clauses are those of the
  recursive satisfaction definition in Section 9.2`. The prior capitalized
  splice is absent, the sentence is grammatical, and the formula displays
  below it remain aligned.
- Physical 54 still prints `defined in ??` for `ch:fol-deduction` and fails.
- Physical 73 still prints `made exact in ??` for
  `ch:intuitionistic-logic` and fails.

## Complete visible-placeholder localization

A page-by-page extraction scan of all 801 physical pages found exactly six
literal `??` occurrences on exactly three pages. All three pages were opened
in their fresh 200-dpi renders. The mapping to the unresolved source labels is:

| Physical page | Visible count | Reader-facing phrase or role | Pending label |
|---:|---:|---|---|
| 54 | 1 | `defined in ??` | `ch:fol-deduction` |
| 73 | 1 | `made exact in ??` | `ch:intuitionistic-logic` |
| 111 | 1 | `invariance under reduct (??)` | `lem:reduct-invariance` |
| 111 | 1 | `that lemma is stated in ??` | `ch:fol-deduction` |
| 111 | 1 | `soundness (??)` | `thm:fol-soundness` |
| 111 | 1 | `completeness (??, under its Axiom-of-Choice hypothesis)` | `thm:fol-completeness` |

Thus `ch:fol-deduction` accounts for two of the six global occurrences;
physical 111 is still governed only once in the render ledger. The earlier
`ch:fol-theories` occurrence is absent from the complete extraction and
visibly resolved on physical 56.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No inspected text, formula, proof square, list item, heading, header, footer, or page number is cut off or crosses a page edge. |
| Exact chapter and boundaries | PASS | Physical 108 is the intentional blank; Chapter 10 begins on 109, exact content ends on 112, and Chapter 11 opens on 113 without duplication or route ambiguity. |
| Headings, running heads, and page numbers | PASS | Printed pages 85--89 are ordered and consistently positioned; chapter and section headings do not collide with content. |
| Equations and symbols | PASS | Satisfaction, consequence, quantifiers, signature subscripts, assignment updates, finite conjunctions, equality, inequality, reduct notation, and derivability glyphs are distinct and readable. |
| Proof display and continuity | PASS | Theorem 10.7, both clauses, its cross-page context, complete proof, proof square, and following paragraph are present without truncation or overlap. |
| Lists, examples, and warning | PASS | Four examples and all seven warning items are complete, ordered, and unclipped. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, calligraphic, Greek, logical, set-theoretic, update-arrow, and proof glyphs show no missing-glyph box or visible substitution. |
| Intentional blank | PASS | Physical 108 is wholly blank and correctly precedes the recto opener. |
| Repaired consumer references and prose | PASS | Physical 56 visibly says `chapter 10`; physical 164 visibly contains the repaired lowercase grammatical sentence and resolved `Section 9.2`. |
| Remaining visible references | **FAIL** | Six literal `??` occurrences remain on physical 54, 73, and 111 at the labels listed above. |

## Coverage and integrity checks

- Exact-source expected set: every integer physical page 109--112, count 4.
- Exact-source render set: exactly one governed PNG for each expected page,
  with no missing, duplicate, or unknown page, count 4.
- Route-transition expected set: physical 108 and 113, count 2.
- Route-transition render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 2.
- Outside-envelope target set: physical 54, 56, 73, and 164, count 4.
- Outside-envelope render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 4.
- Total inspected render set: ten distinct physical pages, each inspected
  once; 7 PASS and 3 FAIL.
- Physical 111 is counted and ledgered once despite serving both the exact
  envelope and the global placeholder audit.
- Every governed PNG byte count, pixel dimension, and SHA-256 digest is
  recorded above. Every governed render is 1700 x 2200 pixels.
- The complete 801-page text scan found exactly six literal `??` occurrences,
  all localized above; no uninspected placeholder page remains.
- The report is UTF-8 without BOM and uses LF line endings only.
- Repository-wide `git diff --check` and the report-specific no-index
  whitespace check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 801 pages, 4,295,277 bytes,
  title `The Methods of Reason`, SHA-256
  `a575a9e58a3484532231a77756bb8584cecc673b9c5a54a6f84fdd53914f928a`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page carrying exact restored source lines 3729--3926 and every
listed transition or consumer target was freshly rendered at 200 dpi,
inspected once, hash-ledgered, and assigned the visual verdict recorded above.
Three visible reference-placeholder pages, including exact-source physical
111, keep the bounded visual gate at FAIL.

It makes no source-fidelity, mathematical-correctness, static-validation,
build-validation, AI-review, admission, section-locking, human-review,
user-acceptance, or release-readiness claim, and it promotes no source unit,
packet, register obligation, semantic row, topic, or section.
