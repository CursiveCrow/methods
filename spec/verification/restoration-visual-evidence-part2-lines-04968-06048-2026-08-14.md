# Restoration visual evidence for Part II source lines 04968--06048 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Exact restored source
lines 4968--6048 map to physical PDF pages 131--147 inclusive. Every page in
that seventeen-page exact-source envelope was freshly rendered at fixed
200 dpi from the pinned PDF and inspected once at original render resolution.
Nine exact-source pages pass and eight fail.

The mathematical body, proof continuations, proof squares, definitions,
examples, exercises, notation, inference-rule displays, and the inherited
common-errors longtable are legible and remain inside the text block on all
seventeen pages. The eight failing exact-source pages are every even physical
page from 132 through 146. Their long Chapter 13 running head has no visible
gap after the printed folio: the raster shows `108CHAPTER`, `110CHAPTER`,
`112CHAPTER`, `114CHAPTER`, `116CHAPTER`, `118CHAPTER`, `120CHAPTER`, and
`122CHAPTER`. This is a repeated running-head layout defect; it is not a
source-content or mathematical verdict.

Physical 129, 130, and 148 were freshly rendered as the route transitions.
Physical 129 cleanly closes the preceding exact chapter. Physical 130 is an
intentional blank leaf and passes. Physical 148 begins the following editorial
supplement cleanly in the body but fails because its running head similarly
prints `124CHAPTER` without a visible gap.

Eleven distinct contents, placeholder, style-target, or downstream-consumer
pages outside the transition and exact-source envelope were also inspected:
physical 13, 14, 73, 109, 111, 160, 167, 351, 603, 604, and 635. Nine pass and
two fail. Physical 73 still visibly prints the sole literal `??` in the PDF.
Physical 635 has a real table collision: the first-row text
`Equisatisfiability/Tseitin` from the first column runs into the second-column
`OPEN:` marker.

The earlier contents collision is fixed in this PDF. The Chapter 13
integration renumbered the former `12.10` and `12.11` entries as `13.10` and
`13.11` and moved them from physical 13 to physical 14. Both current entries
have clear number/title separation. Physical 13 now contains only Sections
12.1--12.4 and is also clean.

The scoped Cleveref repair is visible and clean: physical 133 renders exact
source line 5124 as `defined in definition 10.1`, with physical 109 providing
the correctly numbered Definition 10.1 target. Physical 111 visibly resolves
the completeness consumer as `theorem 12.14`.

Across all thirty-one distinct governed physical pages, the result is
therefore **20 PASS and 11 FAIL**. No page is counted twice when it serves more
than one scope.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, static validation, build approval, AI review,
admission, section locking, human review, user acceptance, or terminal
readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `4e5bf53aba8f8fa2aa71417a759dc5761f4e392b7db66c733adefe4a0bf15dfb`
- File size: 4,335,010 bytes
- Physical page count: 808
- PDF version: 1.5
- PDF subject: `A graduate-level reference in formal logic`
- PDF creator: `LaTeX with hyperref`
- PDF producer: `MiKTeX pdfTeX-1.40.29`
- Encryption: none
- Default page geometry: US Letter, 612 x 792 points, rotation 0
- Landscape consumer page: physical 167, US Letter with rotation 90
- Renderer: Poppler `pdftoppm` 24.04.0, executable SHA-256
  `23335d0ec465c53c2919fbec02574d4c14936fce2f22d8673bfd3e4e48c66091`
- Text extractor used only to map pages, locate literal placeholders, and
  check targeted wording and title/navigation surfaces: Poppler `pdftotext`
  24.04.0, executable SHA-256
  `6f1f7d8db783bd2fac74043dca400a53f42d0a03c4e7f81b2c51ed436c13faeb`
- Full-layout extraction: 1,576,248 bytes, SHA-256
  `2c8a54c0984f0d2519780e3391a66ab2fbc4a98298a8fcac7cf01027c3345f68`
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 131--147 inclusive
- Route-transition pages: 129, 130, and 148
- Outside-envelope contents, placeholder, style-target, and consumer pages:
  13, 14, 73, 109, 111, 160, 167, 351, 603, 604, and 635
- Governed physical-page set: 13, 14, 73, 109, 111, 129, 130, 131, 132,
  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
  147, 148, 160, 167, 351, 603, 604, and 635
- Portrait render dimensions: 1700 x 2200 pixels
- Landscape render dimensions: 2200 x 1700 pixels
- Retained ignored render directory:
  `tmp/pdfs/visual-audit-4e5bf53a-lines-04968-06048/`

The PDF title, page count, byte count, and hash were checked before extraction,
before rendering, after rendering, after inspection, and at evidence freeze.
They remained unchanged. The PDF was not rebuilt by this audit, and no visual
verdict from an earlier PDF hash was reused.

## Physical-page and source mapping

The restoration records, source-unit inventory, Part II route, complete PDF
text extraction, active-route consumer search, and rendered headings establish
this map. A physical page may contain the end of one exact interval and the
start of another, but every physical page is governed only once in the render
ledger.

| Source scope or route context | Units | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---:|---|
| preceding exact route close | 341--345 | 129 | 105 | Corollary 12.18 and its complete proof, immediately before Chapter 13 |
| intentional blank transition | -- | 130 | -- | blank verso inserted before the Chapter 13 opening |
| `SRC-04968-05042` | 346--351 | 131--132 | 107--108 | Chapter 13 opening; elementary substructures; Tarski--Vaught theorem and complete proof |
| `SRC-05043-05131` | 352--356 | 132--133 | 108--109 | downward and upward Loewenheim--Skolem theorems with complete proofs |
| `SRC-05132-05567` | 357--371 | 133--139 | 109--115 | prenex form, negation normal form, rectification, prenex extraction, and Skolemization, with definitions, lemmas, example, theorem, and proofs |
| `SRC-05568-05923` | 372--392 | 139--145 | 115--121 | first-order clauses, simultaneous substitutions, unification, resolution and factoring rules, soundness, Herbrand and lifting results, example, and refutational completeness |
| `SRC-05924-05959` | 393--394 | 145--146 | 121--122 | Common errors section and inherited longtable |
| `SRC-05960-06048` | 395--405 | 146--147 | 122--123 | Exercises 13.30--13.39 |
| following editorial route | -- | 147--148 | 123--124 | explicit `OPEN.` boundary on 147; equality and Hilbert supplement begins on 148 |

The 1,081-line interval contains sixty inventoried source units: one chapter,
six sections, twelve definitions, five lemmas, ten theorems, thirteen proofs
or proof sketches, two examples, one longtable, and ten exercises.

The six exact restoration artifacts remain separately hash-identified:

| Source interval | Units | Artifact bytes | Artifact LF lines | Artifact SHA-256 |
|---|---:|---:|---:|---|
| `SRC-04968-05042` | 346--351 | 3,259 | 75 | `4b0d85e405ff1514804860a2c7521b03d4c2743b0f6395b565dd05e9b0755720` |
| `SRC-05043-05131` | 352--356 | 3,678 | 89 | `28328fc73cd1b9a6c6cba26bf98c5d40844f50cbe2e4460caf00d0ad38d81aba` |
| `SRC-05132-05567` | 357--371 | 21,067 | 436 | `dc57c114d652db41e6e82b834285ee9249b36677462acb570d09f760baafc0ee` |
| `SRC-05568-05923` | 372--392 | 16,138 | 356 | `b59f2bd9857082e603cce1b42728031b441e120992e94d378ff4fdb1c1f867b6` |
| `SRC-05924-05959` | 393--394 | 1,450 | 36 | `7ddf96d90915704cabe88ef44753bd5f576279134b64ad26b73e4c1b5c189a8a` |
| `SRC-05960-06048` | 395--405 | 2,593 | 89 | `4cbddf043c5957e4902e40f1ee6b2948435a8d6edc7dd48b257af65cc4454846` |

These identities locate the rendered scope. This report does not independently
reperform or promote the source-fidelity or static-validation claims attached
to those artifacts.

## Thirty-one-page render ledger

`contents` identifies a table-of-contents page; `targeted` identifies a former
or remaining placeholder or style target; `restored` identifies exact
inherited content; `transition` identifies an immediately adjacent route; and
`consumer` identifies a page that prints a reference to this tranche. Each
physical page appears exactly once in this ledger, and each retained PNG was
opened and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 13 | ix | contents | `p013.png` | 285858 | 1700x2200 | `67653330ba5bace9a7ff5e9715f8cad2686c58719af14fd42f32023955836293` | PASS |
| 14 | x | contents | `p014.png` | 328381 | 1700x2200 | `25ede71d723b39de9b4f202f20c87373d3a14a80059789e7ad053ade20e80c58` | PASS |
| 73 | 49 | targeted | `p073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 109 | 85 | targeted | `p109.png` | 287307 | 1700x2200 | `f97189469b16339f72e4017220538fe9effa9d046afcc04c06c5c60f86197bc9` | PASS |
| 111 | 87 | targeted/consumer | `p111.png` | 449279 | 1700x2200 | `4bac5fbd800f20ecd526b2ffcba4ea25dfa9ebf581bb87e9270670baa26906da` | PASS |
| 129 | 105 | transition | `p129.png` | 118301 | 1700x2200 | `05f0de7fd34ebef91ce6185ceb27aeb91fdc3be2877e621074aa375fa66f5ea7` | PASS |
| 130 | -- | transition/blank | `p130.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 131 | 107 | restored | `p131.png` | 252814 | 1700x2200 | `e30e394b8ceda97674161ccf9d026240075607d31f3e9f8a67bf99f3104d3028` | PASS |
| 132 | 108 | restored | `p132.png` | 394642 | 1700x2200 | `691d8925ed155df35025610f0aa52ed50fb1ac6b64eb07b8038f3bbeda64405f` | **FAIL** |
| 133 | 109 | restored/targeted | `p133.png` | 421101 | 1700x2200 | `149ab4417e5fb566c769541175f5011171a9c134f96a32066e657d94b44176e1` | PASS |
| 134 | 110 | restored | `p134.png` | 379252 | 1700x2200 | `8f5b11aa53f74cb4d8d92ba4dd7df97911b4256801fc2286d2ccf6895b130f49` | **FAIL** |
| 135 | 111 | restored | `p135.png` | 489298 | 1700x2200 | `79fbf06d044f615b5c4fac73dd4138fca0776e7223f8d2b05dd34a8e61c2e41d` | PASS |
| 136 | 112 | restored | `p136.png` | 498800 | 1700x2200 | `525af110359259eb9ce172b43d01d45a6d977417163a9d40481c9ba59d2aef14` | **FAIL** |
| 137 | 113 | restored | `p137.png` | 433846 | 1700x2200 | `5c76791e6472197610c65fe16d45054c975d6db952266c09934ab0c758a8e2b1` | PASS |
| 138 | 114 | restored | `p138.png` | 433743 | 1700x2200 | `b1e44bf32257cb2f26933515605edadef60e21091ec616f6a1aaa24b55c19a93` | **FAIL** |
| 139 | 115 | restored | `p139.png` | 431900 | 1700x2200 | `ab7fe73388da1decccf7c1a5747b1937527e9caf9c21da153effcb386ca6f1ef` | PASS |
| 140 | 116 | restored | `p140.png` | 400665 | 1700x2200 | `43aec30ea95cef722867c4431cb82e62943dba109ca3595a9571c8123f2d37e4` | **FAIL** |
| 141 | 117 | restored | `p141.png` | 342643 | 1700x2200 | `86eb3a3aa9c6cc5e14cc3eb8dbaeae1feb74e2d15410d211c72a8e47e0781bde` | PASS |
| 142 | 118 | restored | `p142.png` | 408476 | 1700x2200 | `05f24457d531f1658b1b71060ce2d798b6b5a89da7953fb20da24de4becc6f15` | **FAIL** |
| 143 | 119 | restored | `p143.png` | 397209 | 1700x2200 | `4b3f663b167b16f0b953e57e05f6ffdd18f3dab0884b1d9bdfde49fec8e55ce1` | PASS |
| 144 | 120 | restored | `p144.png` | 514122 | 1700x2200 | `aa8a28d39e98e437669da33abcb2b2d09d35a857722d930f8ac5757137188a8a` | **FAIL** |
| 145 | 121 | restored | `p145.png` | 373579 | 1700x2200 | `5ef978aa98e24e0c305e3538ee38b663cad576aaf917d4432baafa46a66f8fb0` | PASS |
| 146 | 122 | restored | `p146.png` | 318109 | 1700x2200 | `d71c577aa876c684716c65c62740ec09c0f3e8c252a2f7d889dc5f2bc80f814d` | **FAIL** |
| 147 | 123 | restored/transition | `p147.png` | 374862 | 1700x2200 | `5b1507ae38f2c971ce86742046be3ea971169d2a1966829f9cc53f41acff0f40` | PASS |
| 148 | 124 | transition | `p148.png` | 368691 | 1700x2200 | `6a17fcfa4647475295c80bccf0c9f6c3693b81c72d496d7a88288befbc9c2ffc` | **FAIL** |
| 160 | 136 | consumer | `p160.png` | 403673 | 1700x2200 | `f065e9fd50ebe8f351c70a278bb6fdd410fb08d2e29cc09e44cf9764df8361ea` | PASS |
| 167 | 143 | consumer/landscape | `p167.png` | 305332 | 2200x1700 | `9fd170a5d1e764594474f21b126300f5a9baf16176fcebb3f80300db28e2aed1` | PASS |
| 351 | 327 | consumer | `p351.png` | 335200 | 1700x2200 | `010cfcfa4224d1a66066dcf10f0b8815e9a994b620fc24d60a2be01bc957aa35` | PASS |
| 603 | 579 | consumer | `p603.png` | 324691 | 1700x2200 | `75d5de7d8fa664ca43c98ed5492fbb1e75a0eaed0b8c66fbd84997e222558eb2` | PASS |
| 604 | 580 | consumer | `p604.png` | 448980 | 1700x2200 | `153e9ef05cb829986d0b55a3b53a9e54c4ba12ff2551e93190902cb267411a91` | PASS |
| 635 | 611 | consumer | `p635.png` | 262905 | 1700x2200 | `1d16edf3546b2f7705c8c993046e76e90e442c24be6df979af53ab653753ea7e` | **FAIL** |

## Page-specific visual findings

### Exact Chapter 13 and its transitions

- Physical 129 cleanly closes exact Chapter 12 with Corollary 12.18 and its
  complete proof. The large lower whitespace is an ordinary chapter close.
- Physical 130 is a clean intentional blank verso: it has no stale running
  head, folio, mark, or other rendered artifact.
- Physical 131 cleanly opens Chapter 13, *Cardinality, Normal Forms, and
  Resolution*. Section 13.1 and Definition 13.1 are separated correctly; the
  earlier tentative concern about a section/definition run-in is refuted by
  the original-resolution raster. Definitions 13.1--13.2 and the opening of
  the Tarski--Vaught theorem and proof are legible.
- Physical 132 fails only at the running head, which prints `108CHAPTER`
  without a visible gap. The Tarski--Vaught proof ends cleanly with its square,
  Section 13.2 opens correctly, and the downward Loewenheim--Skolem theorem
  and proof begin without clipping.
- Physical 133 cleanly completes the downward theorem, renders the upward
  theorem and proof, and opens Section 13.3. Exact source line 5124 visibly
  reads `defined in definition 10.1`; no Cleveref warning text or `??` appears
  on the page.
- Physical 134 fails only at `110CHAPTER`. Definitions 13.6--13.7, Lemma 13.8,
  simultaneous recursion, logical symbols, and the continuing proof remain
  clear.
- Physical 135 cleanly completes the negation-normal-form proof and renders
  Lemma 13.9 and its rectification proof with substitutions and variable sets
  distinct.
- Physical 136 fails only at `112CHAPTER`. Lemma 13.10, the displayed
  equivalence conditions, and its continuing prenex-extraction proof remain
  aligned and unclipped.
- Physical 137 cleanly completes prenex extraction, renders Theorem 13.11 and
  its proof, Definition 13.12, and Example 13.13. Quantifier prefixes and
  Skolem symbols remain readable.
- Physical 138 fails only at `114CHAPTER`. Theorem 13.14 and the continuing
  Skolem-equisatisfiability proof render cleanly, including the expanded
  signature, assignments, simultaneous substitutions, and iterated choices.
- Physical 139 cleanly completes that proof, states its non-equivalence
  qualification, opens Section 13.4, and begins Definition 13.15 without a
  boundary or heading collision.
- Physical 140 fails only at `116CHAPTER`. Definition 13.16 and its notation
  for finite-support simultaneous term substitution remain legible and inside
  the margins.
- Physical 141 cleanly renders Definition 13.17, Lemma 13.18, the composition
  and instance-preorder formulas, and the proof. There is no symbol or list
  collision.
- Physical 142 fails only at `118CHAPTER`. Lemma 13.19 and its proof plus
  Definitions 13.20--13.22 render cleanly; renamings, unifiers, substitutions,
  and the unification procedure remain visually distinct.
- Physical 143 cleanly renders Theorem 13.23, its proof sketch, and the
  Resolution and Factoring inference-rule displays. Rule lines, premises,
  conclusions, labels, and side text are complete and unclipped.
- Physical 144 fails only at `120CHAPTER`. Theorem 13.24 and its complete proof,
  Definition 13.25, and Theorems 13.26--13.27 render cleanly; the proof square,
  clauses, ground instances, and substitutions are visible.
- Physical 145 cleanly renders Example 13.28, Theorem 13.29 and its proof
  sketch, the equality-free qualification, and the Section 13.5 heading.
- Physical 146 fails only at `122CHAPTER`. The inherited common-errors
  longtable is complete: all three columns, seven error rows, rules, and
  correction text are legible. Section 13.6 and Exercises 13.30--13.31 begin
  cleanly below it.
- Physical 147 cleanly renders Exercises 13.32--13.39 and their displays.
  The following editorial `OPEN.` notice begins after the last exact exercise
  without duplicating or replacing it.
- Physical 148 begins Sections 13.7 and 13.8 cleanly in the body but fails at
  the running head, which prints `124CHAPTER` without a visible gap.

The eight exact-source failures and the one outbound-transition failure have
the same narrow visual cause. No body line, source proof, source theorem,
source definition, source example, source exercise, longtable row, rule
display, formula, or proof square is itself rejected by this audit.

### Contents, placeholder and style targets, and downstream consumers

- Physical 13 passes. It now lists Chapter 12 with only Sections 12.1--12.4;
  none of those number fields touches its title.
- Physical 14 passes. Current entries `13.10 First-order proof-system
  comparison` and `13.11 Compactness applications` have clear number/title
  separation, aligned dot leaders, and unclipped destinations. The requested
  literal `12.10` and `12.11` contents entries no longer exist because the new
  exact Chapter 13 changed the numbering.
- Physical 73 fails because it still prints `made exact in ??` for the pending
  `ch:intuitionistic-logic` label. Its otherwise clean proof and margins do not
  remove that reader-facing defect.
- Physical 109 cleanly renders Definition 10.1, the target used by exact source
  line 5124. The definition number, title, body, running head, and folio do not
  collide.
- Physical 111 cleanly reads `completeness (theorem 12.14, under its
  Axiom-of-Choice hypothesis)`. The former completeness placeholder is absent.
- Physical 160 cleanly distinguishes the Herbrand validity theorem from the
  dual finite-ground-instance criterion in Theorem 13.26. The header has
  adequate separation and the formulas remain inside the text block.
- Physical 167 is an intentional landscape metatheorem-summary table. Its
  downward and upward Loewenheim--Skolem rows visibly cite Theorems 13.4 and
  13.5. All four columns, table rules, rotated running head, and folio are
  readable and unclipped.
- Physical 351 cleanly cites Theorem 13.4 in the choice-principle table. The
  portrait columns, line breaks, and surrounding prose remain legible.
- Physical 603 cleanly opens Chapter 64 and points the reader to Section 13.4.
  The chapter title, section heading, page number, and consumer prose do not
  collide.
- Physical 604 cleanly cites Section 13.4 and Theorem 13.29. Its shorter
  Chapter 64 running head has adequate separation after the folio.
- Physical 635 fails. In the first row of Table 68.2, the unbroken first-column
  text `Equisatisfiability/Tseitin` intrudes into the second column and visibly
  collides with `OPEN:`. The later Resolution row correctly cites Section 13.4
  and Theorem 13.29, but that valid reference does not cure the table overlap.
  The exact source locator is `handbook/parts/p12/further-reading.tex`: the
  three-column declaration is line 63, the colliding row is lines 72--75, and
  the Section 13.4/Theorem 13.29 consumer row is lines 78--84.

An active-source search found printed external uses of the tranche labels in
the reader-route files represented by physical 160/167, 351, 603/604, and
635. Later restoration files that mention these labels are not yet reachable
in this PDF and therefore are not falsely counted as rendered consumer pages.
Together with generated contents and the two targeted reference pages, no
currently printed mapped consumer page was omitted.

## Complete visible-placeholder localization

A page-by-page Poppler extraction scan of all 808 physical pages found exactly
one literal `??` occurrence on exactly one page. That page was opened in its
fresh 200-dpi render:

| Physical page | Visible count | Reader-facing phrase or role | Pending label |
|---:|---:|---|---|
| 73 | 1 | `natural deduction, made exact in ??` | `ch:intuitionistic-logic` |

Physical 111 no longer contains a placeholder and visibly resolves as
`theorem 12.14`. Physical 133 visibly resolves exact source line 5124 as
`definition 10.1`. No uninspected literal-`??` page remains in this PDF.

## Title, metadata, outline, and contents checks

| Surface | Result | Evidence |
|---|---|---|
| Printed book title text | PASS for text presence | Whole-PDF extraction contains exactly one `The Methods of Reason`, on physical 1. Physical 1 was located by extraction but is outside this bounded raster ledger, so this is not a visual-title claim. |
| PDF title metadata | PASS | The `/Title` value is exactly `The Methods of Reason`. |
| PDF metadata identity | PASS | Subject, creator, producer, PDF version, encryption state, size, page count, and hash are pinned above. |
| Outline destination integrity | PASS | All 393 outline destinations resolve to physical pages; none raises a destination error. Relevant destinations are Chapter 13 on 131, Sections 13.1--13.6 on 131, 132, 133, 139, 145, and 146, and the following Sections 13.7--13.12 on 148, 148, 149, 151, 152, and 154. |
| Legacy outline titles | PASS | No outline item contains `integrated-layout`, `integrated layout`, `Volume I`, `Volume II`, or `Formal Logic Handbook`. |
| Exact book-title bookmark | OPEN / not established | No outline item itself is named `The Methods of Reason`. The content bookmarks are valid, but this audit cannot claim that the stronger planned title-in-bookmarks requirement is met. |
| Chapter 13 contents typography | PASS | Physical 13 cleanly carries Sections 13.1--13.5; physical 14 cleanly carries Sections 13.6--13.12, including separated `13.10` and `13.11` entries. |

The absent exact-title outline item is reported as an administrative/navigation
observation, not converted into an extra physical-page failure. The governed
render tally remains 20 PASS and 11 FAIL.

## Visible construction-status text

The inspected renders contain explicit construction-status text that must not
be confused with visual admission:

| Physical page | Visible marker | Standing in this report |
|---:|---|---|
| 147 | `OPEN.` preceding the separately attributed equality, Hilbert, tableau, and comparison material | Clean route-boundary rendering; content, review, and admission remain open |
| 635 | `OPEN:` in the Equisatisfiability/Tseitin destination and in the Notation destination | Separate content blockers; the first occurrence also participates in the independently reported table collision |

No marker is promoted, closed, or excused by this visual report.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and page margins | PASS | No governed text, formula, rule, proof square, table rule, heading, header, footer, or page number is cut off by a page edge. |
| Exact chapter and boundaries | PASS | Chapter 12 closes on physical 129, physical 130 is intentionally blank, exact Chapter 13 occupies 131--147, and the editorial supplement begins after the last exact exercise. |
| In-body chapter and section headings | PASS | The Chapter 13 opener, Sections 13.1--13.6, and the following Sections 13.7--13.8 are separated from adjacent body content. The tentative p131 run-in concern is refuted. |
| Running heads and folios | **FAIL** | Every even physical page 132--148 concatenates the printed folio with `CHAPTER` because the Chapter 13 mark is too long. |
| Contents typography | PASS | Physical 14 gives `13.10` and `13.11` adequate number/title width; physical 13 has no collision. |
| Definitions and notation | PASS | Substructure, elementary-substructure, prenex, Skolem, clause, substitution, instance, renaming, unifier, ground-term, and related notation remain distinct and legible. |
| Proof display and continuity | PASS | All thirteen inventoried source proof/proof-sketch units remain reader-facing, continue cleanly across pages where necessary, and show their expected terminal squares where complete proofs end. |
| Resolution and factoring rules | PASS | Both rule displays on physical 143 have complete rule lines, premises, conclusions, and labels within the text block. |
| Common-errors longtable | PASS | The inherited three-column longtable on physical 146 is complete, aligned, and unclipped. |
| Exercises | PASS | Exercises 13.30--13.39 occupy physical 146--147 in order; all prompts and mathematical displays are legible. |
| Downstream Table 68.2 | **FAIL** | Physical 635 has a first-row cross-column text collision. |
| Landscape table | PASS | Physical 167 renders at 2200 x 1700 pixels with complete columns, rows, rules, references, rotated running head, and folio. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, calligraphic, Greek, logical, set-theoretic, quantifier, substitution, rule, and proof glyphs show no missing-glyph box or visible substitution. |
| Targeted reference rendering | PASS | Physical 111 resolves `theorem 12.14`; physical 133 resolves `definition 10.1`; the current TOC entries are separated. |
| Remaining visible references | **FAIL** | One literal `??` remains on physical 73 at the pending label listed above. |

## Coverage and integrity checks

- Exact-source expected set: every integer physical page 131--147, count 17.
- Exact-source render set: exactly one governed PNG for each expected page,
  with no missing, duplicate, or unknown page, count 17; 9 PASS and 8 FAIL.
- Route-transition expected set: physical 129, 130, and 148, count 3.
- Route-transition render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 3; 2 PASS and 1 FAIL.
- Outside-envelope contents, placeholder, style-target, and consumer set:
  physical 13, 14, 73, 109, 111, 160, 167, 351, 603, 604, and 635, count 11.
- Outside-envelope render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 11; 9 PASS and 2 FAIL.
- Total inspected render set: thirty-one distinct physical pages, each
  inspected once; 20 PASS and 11 FAIL.
- Physical 147 is counted and ledgered once despite serving as exact restored
  content and the outbound route boundary.
- Every governed PNG byte count, pixel dimension, and SHA-256 digest is
  recorded above. Thirty governed renders are 1700 x 2200 pixels; physical
  167 is 2200 x 1700 pixels.
- The complete 808-page text scan found exactly one literal `??` occurrence,
  localized above; no uninspected literal-placeholder page remains.
- All 393 PDF outline destinations resolve; no broken destination was hidden by
  the bounded page selection.
- The report is UTF-8 without BOM and uses LF line endings only.
- Repository-wide `git diff --check` and a report-specific no-index whitespace
  check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 808 pages, 4,335,010 bytes,
  title `The Methods of Reason`, SHA-256
  `4e5bf53aba8f8fa2aa71417a759dc5761f4e392b7db66c733adefe4a0bf15dfb`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page carrying exact restored source lines 4968--6048 and every
listed transition, contents, placeholder, style-target, or printed consumer
page was freshly rendered at 200 dpi, inspected once, hash-ledgered, and
assigned the visual verdict recorded above. The exact-source envelope passes
9 of 17 pages; repeated running-head collisions, one remaining visible
reference placeholder, and one downstream table collision keep the governed
checkpoint at FAIL.

It makes no source-fidelity, mathematical-correctness, static-validation,
build-validation, AI-review, admission, section-locking, human-review,
user-acceptance, or release-readiness claim, and it promotes no source unit,
packet, register obligation, semantic row, topic, or section.
