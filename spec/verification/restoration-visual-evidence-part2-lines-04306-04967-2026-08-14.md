# Restoration visual evidence for Part II source lines 04306--04967 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Exact restored source
lines 4306--4967 map to physical PDF pages 119--129 inclusive. Every page in
that eleven-page exact-source envelope was freshly rendered at fixed 200 dpi
from the pinned PDF and inspected once at original render resolution. All
eleven exact-source pages pass their visual checks.

Physical 118, the final page of the preceding exact chapter, and physical
130, the continuation of the following editorial supplement, were also
freshly rendered and inspected as the two route transitions. Both pass.
Physical 129 carries both the final restored corollary and the start of the
following supplement; it is ledgered exactly once as restored/transition.

Eight distinct contents, placeholder-target, or downstream-consumer pages
outside the route-transition envelope were inspected: physical 13, 73, 111,
132, 152, 159, 343, and 403. Physical 111, 132, 152, 159, 343, and 403 pass.
Physical 111 now visibly resolves the former `thm:fol-completeness`
placeholder as `theorem 12.14`. Every external consumer of a label introduced
by this tranche is represented in the governed set, including the consumer on
physical 129.

Physical 73 still visibly prints one literal `??` for
`ch:intuitionistic-logic` and fails. A complete extraction scan of all 804
physical pages found no other literal `??`; in particular physical 111 no
longer contains one. Physical 13 also fails because its Chapter 12 contents
entries visibly run the two-digit section numbers into their titles:
`12.10The Löwenheim--Skolem theorems` and
`12.11Compactness applications`. This is a real table-of-contents spacing
defect, not an open content or review gate.

Across all twenty-one distinct inspected physical pages, the result is
therefore **19 PASS and 2 FAIL**. No page is counted twice when it serves more
than one scope.

No clipping, overlap, margin collision, malformed chapter or in-body section
heading, broken proof continuation, missing proof square, malformed recursion,
quotient, denotation, or Cut display, list collision, citation collision,
unreadable mathematical glyph, table collision, unintended blank, running-head
collision, page-number defect, or route-transition defect was found. The
eleven-page exact-source envelope is visually sound. The one unresolved
reader-facing reference and the contents-spacing defect keep the governed
checkpoint open.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, static validation, build approval, AI review,
admission, section locking, human review, user acceptance, or terminal
readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `fbb9a9253bf4b76e4bdd6245423f992bc157a672417e761dd69aa6eba780adb0`
- File size: 4,319,513 bytes
- Physical page count: 804
- PDF version: 1.5
- Default page geometry: US Letter, 612 x 792 points, rotation 0
- Landscape consumer pages: physical 132 and 159, US Letter with rotation 90
- Renderer: Poppler `pdftoppm` 24.04.0, executable SHA-256
  `23335d0ec465c53c2919fbec02574d4c14936fce2f22d8673bfd3e4e48c66091`
- Text extractor used only to map pages, locate literal placeholders, and
  confirm targeted wording: Poppler `pdftotext` 24.04.0, executable SHA-256
  `6f1f7d8db783bd2fac74043dca400a53f42d0a03c4e7f81b2c51ed436c13faeb`
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 119--129 inclusive
- Route-transition pages: 118 and 130
- Outside-envelope contents, placeholder, and consumer pages: 13, 73, 111,
  132, 152, 159, 343, and 403
- Governed physical-page set: 13, 73, 111, 118, 119, 120, 121, 122, 123,
  124, 125, 126, 127, 128, 129, 130, 132, 152, 159, 343, and 403
- Portrait render dimensions: 1700 x 2200 pixels
- Landscape render dimensions: 2200 x 1700 pixels
- Retained ignored render directory:
  `tmp/pdfs/visual-audit-lines-04306-04967-fbb9a925-20260814/`

The PDF title, page count, byte count, and hash were checked before extraction,
before rendering, after rendering, after inspection, and at evidence freeze.
They remained unchanged. The PDF was not rebuilt by this audit, and no visual
verdict from an earlier PDF hash was reused.

## Physical-page and source mapping

The exact restoration artifacts, source-unit evidence, Part II route, full-PDF
text extraction, auxiliary label map, active-source consumer search, and
rendered headings establish this map. A physical page may contain the end of
one exact interval and the start of the next, but every physical page is
governed only once in the render ledger.

| Source scope or route context | Units | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---:|---|
| preceding exact route close | 298--307 | 118 | 94 | Exercises 11.9--11.17, immediately before Chapter 12 |
| `SRC-04306-04575` | 308--323 | 119--123 | 95--99 | Chapter 12 opening; syntactic preparation; quantifier duality; fresh constants; witness extension; new-constant elimination; transfinite recursion; Henkin--Lindenbaum proof |
| `SRC-04576-04712` | 324--333 | 123--125 | 99--101 | Term structure, equality congruence, quotient and interpretations, term evaluation, quantifier membership, and truth lemma |
| `SRC-04713-04920` | 334--340 | 125--128 | 101--104 | Strong completeness, countable-signature completeness, and sequent-calculus completeness with the Cut display |
| `SRC-04921-04967` | 341--345 | 128--129 | 104--105 | Compactness theorem and the nonaxiomatizability corollary, with both complete proofs |
| following editorial route | -- | 129--130 | 105--106 | Separately attributed equality and Hilbert supplements begin after the exact corollary |

The four exact restoration artifacts remain separately hash-identified:

| Source interval | Artifact bytes | Artifact LF lines | Artifact SHA-256 |
|---|---:|---:|---|
| `SRC-04306-04575` | 13,004 | 270 | `3af221be1a62243fd0cb2896f63b419476ce8a5bfc5bdb49df06d1ef00d782d3` |
| `SRC-04576-04712` | 4,758 | 137 | `4fe5d6b961b9a64a861a8756a2587220e9c0d2f646145afb6f014ff6e938cbee` |
| `SRC-04713-04920` | 10,464 | 208 | `1b6d33c14aef530364ee62b342db74be130011f775a3a9d5958f3cca5b9808da` |
| `SRC-04921-04967` | 2,075 | 47 | `79e3e081d7496c13f92517b899cc9518fc6e63a97adfe1715b85f04c3d23abad` |

These identities locate the rendered scope. This report does not independently
reperform or promote the source-fidelity or static-validation claims attached
to those artifacts.

## Twenty-one-page render ledger

`contents` identifies the table-of-contents consumer; `targeted` identifies a
former or remaining placeholder page; `consumer` identifies a page that
prints a reference introduced by this tranche; `restored` identifies exact
inherited content; and `transition` identifies the immediately adjacent route.
Each physical page appears exactly once in this ledger, and each retained PNG
was opened and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 13 | ix | contents | `p013.png` | 291231 | 1700x2200 | `8150e89edf6bd133c785462b7f8f45b4390245de569e3c47548e435d583c4419` | **FAIL** |
| 73 | 49 | targeted | `p073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 111 | 87 | targeted/consumer | `p111.png` | 449279 | 1700x2200 | `4bac5fbd800f20ecd526b2ffcba4ea25dfa9ebf581bb87e9270670baa26906da` | PASS |
| 118 | 94 | transition | `p118.png` | 258212 | 1700x2200 | `772324c435e3070354ab7326e2d73759112828f99ad2c2ef6b53311947bacb9b` | PASS |
| 119 | 95 | restored | `p119.png` | 276029 | 1700x2200 | `4021ad94f09d54e274246917d3305690e7ac57b811e45bd1b2c3f150a33c9d7c` | PASS |
| 120 | 96 | restored | `p120.png` | 445865 | 1700x2200 | `7aa8fee607c01e52afc3f5b1dd9178f9127e18f6b9833a94af82bd556c21b9aa` | PASS |
| 121 | 97 | restored | `p121.png` | 426882 | 1700x2200 | `d08a60d7268a3ac7192b20506aa2e62cd1c9e0466c18d322ab174897bb09fdd7` | PASS |
| 122 | 98 | restored | `p122.png` | 481028 | 1700x2200 | `70a771ec9c4edb269c252aab202c4e9a2cdc4599aec018df1ae725f34c78198d` | PASS |
| 123 | 99 | restored | `p123.png` | 343049 | 1700x2200 | `de943abf919ebf64436051dd10d39a8c4701a0fa7ad6d063767193233855f920` | PASS |
| 124 | 100 | restored | `p124.png` | 338534 | 1700x2200 | `fc5a9a1f0f7e62659b6b0214c01a724cd5db2e4d80b5df68263527c9e7a871d9` | PASS |
| 125 | 101 | restored | `p125.png` | 379941 | 1700x2200 | `95a4ae1b3f6a0365db5c04874143e07d6686600c8c57b5c241df19f8491689c9` | PASS |
| 126 | 102 | restored | `p126.png` | 458443 | 1700x2200 | `3f53741e1a7fa512cf4b098a5044ef78202ad3534e3b25747e0a7ef62d844bb1` | PASS |
| 127 | 103 | restored | `p127.png` | 465793 | 1700x2200 | `8893b7436d5850a31b7c1ffec5e510db3bc52909e3d649c90a25a4ac2c68985f` | PASS |
| 128 | 104 | restored | `p128.png` | 384815 | 1700x2200 | `50bef2ec0dedfe52cd446cb64cafdf7781ba880ad6d37669385802434df9c7fc` | PASS |
| 129 | 105 | restored/transition/consumer | `p129.png` | 399819 | 1700x2200 | `188c167b62ef7c910cafd71a24e77f539e3abe4cdf08c11b51427a5a913bc6fe` | PASS |
| 130 | 106 | transition | `p130.png` | 375533 | 1700x2200 | `eef0215a31bb98b800a338bcc628ef8e4c178121d04b5378e7fcb0471b9a176d` | PASS |
| 132 | 108 | consumer | `p132.png` | 299537 | 2200x1700 | `3b618c51e51c2c14c92062e36399628f1d7bbfbe691de3ed2cb8e150eb4df0c6` | PASS |
| 152 | 128 | consumer | `p152.png` | 403669 | 1700x2200 | `c4a096742fbe4b6c69b3265bed3e4d7cfe63ea2d20a212535522e06e6818fae3` | PASS |
| 159 | 135 | consumer | `p159.png` | 305768 | 2200x1700 | `5f8c60fb261f0dbb64be192c003b3d3059243e455aa919002a028b0a3e8009eb` | PASS |
| 343 | 319 | consumer | `p343.png` | 336032 | 1700x2200 | `614dbdac49bee3bf87b90c83e5d6b6834ee366f4b06b355f67a6c5d21bc64130` | PASS |
| 403 | 379 | consumer | `p403.png` | 415267 | 1700x2200 | `adc3474d81ed764eed2fd6dd47dc866c502563fb9cea13d81c7f0077a034bb1d` | PASS |

## Page-specific visual findings

### Exact Chapter 12 and its transitions

- Physical 118 cleanly closes Chapter 11 with Exercises 11.9--11.17. Its
  lower whitespace is the ordinary close of the exact chapter, not an
  unintended blank.
- Physical 119 cleanly opens Chapter 12, *Henkin Completeness and
  Compactness*, and Section 12.1. The Gödel and Henkin citations print as
  `[Göd30]` and `[Hen49]`, the consistency definition is legible, and the
  quantifier-duality display is aligned and unclipped.
- Physical 120 cleanly renders the complete quantifier-duality and
  fresh-constant proofs with two distinct proof squares, Definition 12.4, and
  the witness-extension display. Eigenvariable and substitution notation is
  sharp.
- Physical 121 cleanly completes the witness-extension and new-constant
  elimination proofs with their proof squares, then begins the transfinite
  Lindenbaum proof. The recursion cases, union, subscripts, and limit-stage
  notation remain distinct.
- Physical 122 cleanly completes the transfinite Lindenbaum proof and begins
  the Henkin--Lindenbaum proof. Both the terminal proof square and the
  indexed existential-formula enumeration display are visible.
- Physical 123 cleanly completes the Henkin--Lindenbaum proof with its proof
  square, opens Section 12.2, and renders equality congruence and its proof.
  The quotient-domain and function-interpretation displays begin cleanly.
- Physical 124 cleanly continues the quotient and relation interpretations,
  then renders term evaluation, the two-item quantifier-membership list and
  proof, and the opening denotation chain of the truth lemma. Three proof
  squares are not owed here: the page correctly shows exactly the two proofs
  that end on it, while the truth proof continues.
- Physical 125 cleanly completes the truth lemma, opens Section 12.3, renders
  Theorem 12.14 and its complete proof, and begins Corollary 12.15. The
  semantic brackets, assignment update, reduct, consequence, and derivability
  symbols remain legible; both completed proofs have visible squares.
- Physical 126 cleanly continues the countable-signature proof. The long
  coding construction, natural-number indices, cardinal symbols, and
  recursion wording are fully within the margins.
- Physical 127 cleanly ends the countable-signature proof with its square and
  begins the sequent-calculus completeness proof sketch. Items 1--4 of its
  five-item list are ordered and aligned; the final Cut construction
  continues unambiguously to the next page.
- Physical 128 cleanly renders the Cut inference, item 5, and the terminal
  proof square for Theorem 12.16, then opens Section 12.4 and renders the
  two-item compactness statement and complete proof with a second square.
  No rule line, label, formula, or list item crosses a margin.
- Physical 129 cleanly renders Corollary 12.18 and its complete proof with the
  fifteenth and final proof square of the exact tranche. The separately
  attributed `OPEN.` supplement follows without duplication and visibly
  resolves its term-congruence consumer as `Lemma 12.9`.
- Physical 130 cleanly continues the editorial supplement with Sections 12.6
  and 12.7. The exact corollary is not duplicated and the transition remains
  unambiguous.

Across physical 119--129, all fifteen source proofs or proof sketches end with
fifteen visible proof squares: two on 120, two on 121, one on 122, two on 123,
two on 124, two on 125, one on 127, two on 128, and one on 129. The three
source lists are likewise complete: the two quantifier-membership clauses on
124, the five sequent-completeness steps across 127--128, and the two
compactness clauses on 128.

### Contents, placeholder target, and downstream consumers

- Physical 13 lists Chapter 12 on printed page 95 and Sections 12.1--12.11 in
  numerical order. It fails because the section-number field is too narrow:
  `12.10` touches `The Löwenheim--Skolem theorems`, and `12.11` touches
  `Compactness applications`. The entries are not clipped, but the missing
  inter-field space is visibly malformed.
- Physical 73 still prints `made exact in ??` for the pending
  `ch:intuitionistic-logic` label. Its otherwise clean proof display and page
  layout do not remove that reader-facing failure.
- Physical 111 now reads `completeness (theorem 12.14, under its
  Axiom-of-Choice hypothesis)`. The former placeholder is absent; the theorem,
  complete proof, proof square, and surrounding references render cleanly.
- Physical 129 visibly resolves the equality-metatheory consumer as
  `Lemma 12.9`; it is counted once in the main ledger despite also carrying
  exact restored and transition material.
- Physical 132 is an intentional landscape proof-system comparison table.
  Its natural-deduction row visibly cites `Theorem 12.14` and
  `Corollary 12.15`, and its LK row cites `Theorem 12.16`. All five columns,
  table rules, rotated running head, and row text are legible and unclipped.
- Physical 152 visibly distinguishes the unquotiented Herbrand structure from
  the term structure in `Section 12.2`. The consumer reference and all
  formulas render cleanly.
- Physical 159 is an intentional landscape metatheorem-summary table. It
  visibly cites `Theorem 12.14`, `Corollary 12.15`, and `Theorem 12.17` in the
  strong-completeness and compactness rows. Columns, row text, formulas,
  rotated running head, and printed page number remain within the page.
- Physical 343 visibly cites countable-signature completeness as
  `Corollary 12.15` and arbitrary-signature completeness as `Theorem 12.14`
  in the choice-principle table. The portrait table is legible and unclipped.
- Physical 403 visibly cites first-order sequent completeness as the sketched
  `Theorem 12.16`. The consumer, running head, page number, surrounding prose,
  and following section heading do not collide.

An active-source search found external uses of the tranche's labels only in
the four files represented by physical 129/132, 152/159, 343, and 403, plus
the earlier exact consumer on physical 111. Together with the generated
contents entry on physical 13, no mapped downstream consumer page was omitted.

### Visible construction-status text

The inspected renders also contain two explicit construction-status markers
that are not undefined-reference render failures:

| Physical page | Visible marker | Standing in this report |
|---:|---|---|
| 129 | `OPEN.` preceding the separately attributed equality, Hilbert, tableau, and comparison supplement | Properly rendered following-route status text; content, review, and admission remain open |
| 403 | boxed `STUB. A-070` for relevance and affine comparison rows | Properly rendered but still a separate final-publication content blocker |

Neither marker is promoted, closed, or excused by this visual report. Their
presence must be handled by the content and admission workflow. They do not
alter the bounded raster-layout verdict for the restored interval.

## Complete visible-placeholder localization

A page-by-page Poppler extraction scan of all 804 physical pages found exactly
one literal `??` occurrence on exactly one page. That page was opened in its
fresh 200-dpi render. The mapping is:

| Physical page | Visible count | Reader-facing phrase or role | Pending label |
|---:|---:|---|---|
| 73 | 1 | `made exact in ??` | `ch:intuitionistic-logic` |

The former physical-111 `thm:fol-completeness` placeholder is absent and
visibly resolved as `theorem 12.14`. No uninspected literal-`??` page remains
in this PDF.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No inspected text, formula, rule, proof square, list item, table cell, heading, header, footer, or page number is cut off or crosses a page edge. |
| Exact chapter and boundaries | PASS | Chapter 11 closes on physical 118; exact Chapter 12 occupies 119--129; the editorial supplement starts after the exact corollary on 129 and continues on 130 without duplication or route ambiguity. |
| In-body headings, running heads, and page numbers | PASS | Printed pages 94--106 are ordered and consistently positioned; the Chapter 12 and Sections 12.1--12.7 headings inspected in the route do not collide with content. |
| Contents typography | **FAIL** | Physical 13 runs `12.10` and `12.11` directly into their titles without an inter-field space. |
| Recursion, quotient, and denotation displays | PASS | The transfinite cases and unions, existential enumeration, quotient domain, function/relation interpretations, assignment, semantic brackets, substitution, and truth chains are distinct and readable. |
| Cut display | PASS | The two-premise Cut rule on physical 128 has a complete rule line, both premises, conclusion, and label, all within the text block. |
| Proof display and continuity | PASS | All fifteen proofs or proof sketches remain reader-facing, continue cleanly across pages where necessary, and have fifteen visible terminal proof squares. |
| Lists | PASS | The two quantifier-membership clauses, five sequent-completeness steps, and two compactness clauses are complete, ordered, and unclipped. |
| Citations | PASS | The Chapter 12 opening prints readable Gödel and Henkin citation keys; the following supplement citations on 129 and 130 are also legible. |
| Landscape tables | PASS | Physical 132 and 159 render at 2200 x 1700 pixels with complete columns, rows, rules, citations, rotated running heads, and page numbers. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, calligraphic, Greek, logical, set-theoretic, assignment, quotient, rule, and proof glyphs show no missing-glyph box or visible substitution. |
| Restored consumer references | PASS | Physical 111, 129, 132, 152, 159, 343, and 403 visibly resolve every mapped external consumer of labels introduced by this tranche. |
| Remaining visible references | **FAIL** | One literal `??` remains on physical 73 at the pending label listed above. |

## Coverage and integrity checks

- Exact-source expected set: every integer physical page 119--129, count 11.
- Exact-source render set: exactly one governed PNG for each expected page,
  with no missing, duplicate, or unknown page, count 11.
- Route-transition expected set: physical 118 and 130, count 2.
- Route-transition render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 2.
- Outside-envelope contents, placeholder, and consumer set: physical 13, 73,
  111, 132, 152, 159, 343, and 403, count 8.
- Outside-envelope render set: exactly one governed PNG for each target, with
  no missing, duplicate, or unknown page, count 8.
- Total inspected render set: twenty-one distinct physical pages, each
  inspected once; 19 PASS and 2 FAIL.
- Physical 129 is counted and ledgered once despite serving as exact restored
  content, transition, and consumer.
- Every governed PNG byte count, pixel dimension, and SHA-256 digest is
  recorded above. Nineteen governed renders are 1700 x 2200 pixels; physical
  132 and 159 are 2200 x 1700 pixels.
- The complete 804-page text scan found exactly one literal `??` occurrence,
  localized above; no uninspected literal-placeholder page remains.
- The report is UTF-8 without BOM and uses LF line endings only.
- Repository-wide `git diff --check` and the report-specific no-index
  whitespace check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 804 pages, 4,319,513 bytes,
  title `The Methods of Reason`, SHA-256
  `fbb9a9253bf4b76e4bdd6245423f992bc157a672417e761dd69aa6eba780adb0`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page carrying exact restored source lines 4306--4967 and every
listed transition, contents, placeholder, or consumer target was freshly
rendered at 200 dpi, inspected once, hash-ledgered, and assigned the visual
verdict recorded above. The exact-source envelope passes 11 of 11 pages. One
remaining visible reference-placeholder page and one contents-spacing page
keep the governed checkpoint at FAIL.

It makes no source-fidelity, mathematical-correctness, static-validation,
build-validation, AI-review, admission, section-locking, human-review,
user-acceptance, or release-readiness claim, and it promotes no source unit,
packet, register obligation, semantic row, topic, or section.
