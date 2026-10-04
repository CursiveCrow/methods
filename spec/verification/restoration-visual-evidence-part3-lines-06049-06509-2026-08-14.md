# Rendered visual evidence: Part III source lines 6049--6509

Date: 2026-08-14

## Verdict

The exact restored source envelope passes this bounded rendered-layout audit:
physical PDF pages 199--208 are visually sound, and the preceding and following
transition pages 198 and 209 are sound. The sole public part opener is `Part III`
and `Model Theory`; the chapter opener is `Maps, Substructures, and
Elementarity`; the source `Convention 17.1 (Status of results)` is rendered
correctly. No clipping, collision, broken margin, malformed display, missing
glyph, stale running head, or unintended blank was found in that envelope.

The assigned regression surfaces also pass their layout checks:

- all thirteen even physical pages 132, 134, ..., 156 carrying the long
  `Cardinality, Normal Forms, and Resolution` chapter mark retain a readable
  folio gap;
- TOC physical page 14 separates 13.10 and 13.11 from their titles and contains
  the one Part III entry cleanly;
- Table 68.2 on physical page 633 separates `Equisatisfiability/Tseitin` from
  the `OPEN:` destination cell;
- the former completeness consumer on physical page 111 renders resolved
  theorem references; and
- the new downstream consumer on physical page 209 renders `Definition 17.16`
  rather than a placeholder.

The bounded publication-facing verdict is nevertheless **FAIL / OPEN**, because
physical page 73 visibly contains the expected pending `??` destination for
`ch:intuitionistic-logic`. Whole-PDF text extraction finds exactly one literal
`??`, on physical page 73 only. This is a known open content/reference defect,
not a layout defect introduced by source lines 6049--6509.

This report is visual evidence only. It does not assert source-fidelity review,
static validation, build cleanliness, semantic review, AI topic approval,
admission, human review, user acceptance, or publication readiness.

## Fail-closed PDF identity

The audit stopped before rendering unless all assigned identity fields agreed.
They did agree, and the same byte identity was rechecked after page inspection.

| Field | Pinned value |
|---|---|
| File | `handbook/main.pdf` |
| PDF title metadata | `The Methods of Reason` |
| Physical pages | 804 |
| Bytes | 4,329,072 |
| SHA-256 | `796da722cf31ccdd8edff92fd1cb8d1a88c7dd1b272765f1fd3dddda761a8143` |

The PDF skill was applied as a read-only inspection workflow. Consequently no
PDF create/edit operation marker was run and no PDF was authored or rewritten.
MiKTeX Poppler `pdftoppm` rendered each governed physical page once at exactly
200 dpi to PNG. Every render is 1700 by 2200 pixels.

## Source-to-page map

Fragment page ranges overlap where a source boundary falls within a typeset
page. The governed physical-page envelope is the unique set 199--208; each of
those ten pages was rendered and inspected once. Pages 198 and 209 are the two
transitions.

| Source fragment | Inclusive lines | Source units | Physical PDF pages | Reader-facing role |
|---|---:|---:|---:|---|
| `SRC-06049-06069` | 6049--6069 | 406--408 | 199--201 | Part III opener, intentional verso, Chapter 17 opener, assumptions, references, and status convention |
| `SRC-06070-06137` | 6070--6137 | 409--415 | 201--202 | Homomorphisms, embeddings, isomorphisms, term preservation, proof, warning |
| `SRC-06138-06242` | 6138--6242 | 416--422 | 202--204 | Substructures, example, isomorphism invariance, image of an embedding, proofs |
| `SRC-06243-06331` | 6243--6331 | 423--429 | 204--205 | Elementary maps/substructures, remark, Tarski--Vaught theorem and proof, example |
| `SRC-06332-06421` | 6332--6421 | 430--435 | 205--207 | Parameter constants, diagrams, embedding tests and proof, example |
| `SRC-06422-06431` | 6422--6431 | 436 | 207 | Diagram exercise |
| `SRC-06432-06493` | 6432--6493 | 437--441 | 207--208 | Elementary chains, theorem, proof, warning |
| `SRC-06494-06509` | 6494--6509 | 442--443 | 208 | Two elementary-chain exercises |

The 38 source units are ordinals 406--443 without a gap. The visual inspection
did not promote any of them from their governed OPEN standing.

## Exact-envelope inspection

### Transitions and part structure

- Physical page 198 cleanly ends Chapter 16 with its audit table. No Part III
  material leaks backward.
- Physical page 199 is the sole public `Part III` / `Model Theory` body opener.
  Its folio is present and the title is centered with book-consistent spacing.
- Physical page 200 is an intentional blank verso. It is entirely blank, with
  no stale running head or folio.
- Physical page 201 opens Chapter 17. The two-line chapter title is unclipped;
  the assumption paragraph, citations, exact source convention, section 17.1,
  first list, and formula display are legible and remain within the text block.
- Physical page 209 begins Chapter 18 cleanly and resolves its parameter-
  expansion consumer to `Definition 17.16`. No Chapter 17 mark leaks forward.

### Statements, proofs, examples, exercises, and notation

- Pages 201--202: Definitions 17.2--17.4, Lemma 17.5 and its complete proof,
  Warning 17.6, the three-item homomorphism list, tuple bars, structure
  superscripts, arrows, satisfaction glyphs, and the preservation display all
  render clearly.
- Pages 202--204: Definition 17.7, Example 17.8, Lemmas 17.9 and 17.10 and both
  proofs render without collisions. The natural/integer order example,
  negated-satisfaction glyph, image notation, restriction prose, QED marks,
  and cross-reference to section 13.1 are legible.
- Pages 204--205: Definitions 17.11 and 17.12, Remark 17.13, Theorem 17.14,
  its complete proof, Example 17.15, inclusion and elementarity symbols,
  quantifier displays, and references to theorem 13.3 and lemma 17.5 render
  correctly.
- Pages 205--207: Definitions 17.16 and 17.17, Theorem 17.18 and proof,
  Example 17.19, Exercise 17.20, the two-item theorem list, parameter constants,
  `Diag`/`ElDiag`/`Th` notation, expansion primes, citations, and all formula
  displays are legible and continuous across pages.
- Pages 207--208: Definition 17.21, Theorem 17.22 and proof, Warning 17.23,
  Exercises 17.24 and 17.25, ordinal-indexed chains, unions, subscripts,
  elementarity symbols, ellipsis, and theorem cross-reference all render
  correctly. Page 208 intentionally has substantial remaining white space
  after the two final exercises; this is not clipping or lost content.

No tabular environment occurs inside source lines 6049--6509. All enumerated
lists in the envelope were inspected. The separately assigned Table 68.2
regression is recorded below.

Running heads and folios alternate correctly throughout pages 201--208. All
chapter and section headings remain inside the text block; no equation, proof,
list item, citation, or glyph touches a page edge.

## Assigned regression checks

### Long even-page chapter mark

Physical pages 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154,
and 156 were each visually inspected. The scaled long mark is complete and
legible on every page, and the printed folios 108, 110, ..., 132 remain
separate. Independent Poppler bounding-box extraction measured the gap from
the folio's right edge to the word `CHAPTER` as 10.909 pt on every one of the
thirteen pages. There is no fused folio/header token.

### TOC width

Physical page 14 contains each of `13.10 First-order proof-system comparison`,
`13.11 Compactness applications`, and `III Model Theory` once. Section numbers
have an ordinary visible gap before their titles. Dot leaders, right-aligned
page numbers, Part III, Chapter 17, and sections 17.1--17.5 are unclipped and
noncolliding.

### Table 68.2

On physical page 633, the first-column label breaks as
`Equisatisfiability/` then `Tseitin`. The second column begins with bold
`OPEN:` and does not collide with either first-column line. The boundary text
stays in the third column. The remaining rows retain their column boundaries.
The row's OPEN content standing is not changed by this layout pass.

### Pending and repaired references

- Physical page 73 visibly reads `made exact in ??`; the page otherwise has no
  visual layout defect. This page is the single FAIL/OPEN row in the governed
  page set.
- Physical page 111 renders `theorem 11.6` and `theorem 12.14` in the
  completeness consumer with no `??`, clipping, or collision.
- Physical page 209 renders `Definition 17.16` in the new Part III downstream
  consumer with no `??`, clipping, or collision.

## Extraction, outline, TOC, and body checks

Poppler extracted 804 physical text pages from the pinned PDF.

| Check | Result |
|---|---|
| Exact literal `??` in whole extracted PDF | 1 |
| Physical pages containing literal `??` | 73 only |
| Outline entries traversed | 392 |
| Unresolved or out-of-range outline destinations | 0 |
| Outline title exactly `III Model Theory` | 1, targeting physical page 199 |
| TOC page 14 exact `III Model Theory` count | 1 |
| TOC page 14 exact `13.10` count | 1 |
| TOC page 14 exact `13.11` count | 1 |
| Body pages containing `Part III` | physical page 199 only |
| Body page 199 `Part III` count | 1 |
| Body page 199 `Model Theory` count | 1 |

Thus the Part III outline, TOC, and body surfaces each occur once, and every
outline destination resolves to a physical page in the 804-page PDF.

## Governed render ledger

The required set was constructed before rendering and deduplicated to these 29
physical pages:

`14, 73, 111, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154,
156, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 633`.

There are 29 ledger rows, 29 PNG files, 29 unique page numbers, and no required
page omitted. Each PNG was generated directly from the pinned PDF at 200 dpi.

| Physical page | Role | PNG bytes | Dimensions | PNG SHA-256 | Verdict |
|---:|---|---:|---:|---|---|
| 14 | TOC 13.10/13.11 and Part III regression | 325789 | 1700x2200 | `73c37a58cc559f3fa24aa7cb90e3724bc757f88a667644eca47d6851933f7d24` | PASS |
| 73 | Pending intuitionistic destination | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | FAIL / OPEN: visible `??`; layout otherwise sound |
| 111 | Former completeness consumer | 449279 | 1700x2200 | `4bac5fbd800f20ecd526b2ffcba4ea25dfa9ebf581bb87e9270670baa26906da` | PASS |
| 132 | Long even running head, printed folio 108 | 394277 | 1700x2200 | `5af4a8d36891737b79667c6ddc60709ed0b599537ad198a3745b3ecb85c57f63` | PASS |
| 134 | Long even running head, printed folio 110 | 378929 | 1700x2200 | `20e38f8b5127e97d7bcaccd7d2712df4a4ccbecb169af6f423a8ac8bc8965240` | PASS |
| 136 | Long even running head, printed folio 112 | 498458 | 1700x2200 | `bce42dba22e6c15a0d3742b906b9b6171ae8fdd6041ec9fa423612ee0363241a` | PASS |
| 138 | Long even running head, printed folio 114 | 433475 | 1700x2200 | `7da31d2ad0c571d9bdeeb00f037a01c4992379b7432fd27277cc04fac48e3bd6` | PASS |
| 140 | Long even running head, printed folio 116 | 400254 | 1700x2200 | `dc97f3eb0bdfdca53add8a35dc54cfde6b4d05ab437a3473946e0ba917f18f10` | PASS |
| 142 | Long even running head, printed folio 118 | 408144 | 1700x2200 | `4684d8544c78a6bbd83282e303c7296554c91300283bd7310a01749362b33ff9` | PASS |
| 144 | Long even running head, printed folio 120 | 513764 | 1700x2200 | `ab47ea6acfb63195276e3746615a025acbed9958e864bc1ed015a912718cd63d` | PASS |
| 146 | Long even running head, printed folio 122 | 317700 | 1700x2200 | `2e1ae58fc62f8555675a33819bea659525cf6ac1633f9ca7b84e4039410ea4e1` | PASS |
| 148 | Long even running head, printed folio 124 | 368391 | 1700x2200 | `810becc1d58dec1b77b02dec9c8f21698328420c9e1446e7d394a5a0b903511b` | PASS |
| 150 | Long even running head, printed folio 126 | 142545 | 1700x2200 | `207a50bf0459534910d82517a9ed18dc24960577cdcdb48229eb88c6e72d674c` | PASS |
| 152 | Long even running head, printed folio 128 | 412032 | 1700x2200 | `ab6e20120eecf12efff9cfda253f4b42ea3c5f69158ce7ac8c5595c05317cfca` | PASS |
| 154 | Long even running head, printed folio 130 | 140828 | 1700x2200 | `31543a83646dd67afb04ef41d75148ff1c69d13342d9da25b7f32b91aa7ea868` | PASS |
| 156 | Long even running head, printed folio 132 | 267880 | 1700x2200 | `f9cfbbd10e4aad0b5f65f58071d9881aa9eab0745b9431e44780c79acd4bde05` | PASS |
| 198 | Preceding transition, Chapter 16 audit tail | 113757 | 1700x2200 | `4ee448272606d5f6a264966f3c9635caafb64b5f119d6fd484ef966d7272dcb4` | PASS |
| 199 | Sole Part III / Model Theory opener | 28448 | 1700x2200 | `b1b130f46ce92fe72f88ca644604b6cbf938849ac9a67929cbda201db94dd74d` | PASS |
| 200 | Intentional blank verso | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 201 | Chapter 17 opener, convention, section 17.1 | 246665 | 1700x2200 | `35a7aa832613f9af92ed36356692bf7e67efe71c279ea76b1dfad1a572d70c07` | PASS |
| 202 | Sections 17.1--17.2, statements/proof/warning | 347610 | 1700x2200 | `506de72d834e48f5035bcea84df635901099e8652d944bc078b2179c98f1fbfe` | PASS |
| 203 | Section 17.2, example/lemmas/proof | 424837 | 1700x2200 | `4d746c2d41a8127b34c168179941431cce60a3a6e7565de9be2f7e548038576e` | PASS |
| 204 | Sections 17.2--17.3, proof/definitions/theorem | 410815 | 1700x2200 | `01bc681357f0845749e3cd343df3fe47cd4a4402d87d6aeaeaf4e94df206da6a` | PASS |
| 205 | Sections 17.3--17.4, proof/example/definition | 414904 | 1700x2200 | `396d5402933bd009014a89b26a492bf97fe5955503916570e371182b75c8b8bf` | PASS |
| 206 | Section 17.4, definitions/theorem/proof/example | 437780 | 1700x2200 | `56dcad9a2850a69ec1240d8b3ecdfa0d18536b67e8155118e9ad0b2a75d8635e` | PASS |
| 207 | Sections 17.4--17.5, example/exercise/chain proof | 407789 | 1700x2200 | `ff1f3692acb0bbb674cc278c707d871f48e63b428bc58499e79730cc15957230` | PASS |
| 208 | Section 17.5 warning and final exercises | 118696 | 1700x2200 | `38010985dc92317f05efe111de16b740b579c35a05077c1c9ddd33e313e94b34` | PASS |
| 209 | Following transition and Definition 17.16 consumer | 276817 | 1700x2200 | `a84b023f8fcd2bff5b4ba0e829ccda5fe6b048f16368addee3506182ad876be3` | PASS |
| 633 | Table 68.2 first-row regression | 263995 | 1700x2200 | `393039bebd52f14f9b9b68cda499e857e0175f94de36c132ca643471b1fbf77e` | PASS for layout; row content remains OPEN |

## Claim boundaries

- `PASS` in this report means only that the pinned PDF page passed the stated
  200-dpi rendered inspection.
- The single `FAIL / OPEN` is the visible pending reference on physical page
  73. It prevents an all-green bounded publication-facing verdict.
- Source/static/build/AI/admission/human/user claims remain separate. In
  particular, this report does not modify the OPEN provenance or source-unit
  review records and does not admit source units 406--443.
- A change to the PDF SHA-256 invalidates every result in this report.
