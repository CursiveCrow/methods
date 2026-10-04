# Restoration visual evidence for Part II source lines 01649--02450 - 2026-08-13

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Every physical PDF page
containing reader-facing material from restored source lines 1649--2450 was
mapped, freshly rendered at fixed 200 dpi from the new PDF checkpoint, and
inspected exactly once at the original 1700 x 2200 pixel render resolution.
The complete range is physical pages 59--75 inclusive. Sixteen of these 17
pages pass. Physical page 73 fails because one unresolved reference visibly
prints as `??` in the sentence about where intuitionistic natural deduction is
made exact.

No clipping, overlap, margin collision, missing or substituted mathematical
glyph, malformed heading, running-head defect, page-number defect, broken
table or list, broken rule array, broken derivation tree, malformed side
condition, or cross-page continuity defect was found. The otherwise-correct
layout does not override the visible-reference failure.

Physical pages 60 and 70 are intentional blank versos. Physical page 75 is a
shared boundary page: it completes the exact restored sequent material before
a reader note and separately attributed Section 6.3 begin. The whole page was
inspected, but only the restored content and the visual integrity of the shared
boundary are credited.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, AI review, static validation, build approval,
admission, human review, or user acceptance.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- SHA-256:
  `3f2c0dce5b3458717879980a9c3ab461e1aef808befeb614579c4f23325d5091`
- File size: 4,271,551 bytes
- Physical page count: 793
- Page geometry: US Letter, 612 x 792 points, rotation 0
- PDF version: 1.5
- Renderer: Poppler `pdftoppm` 26.05.0
- Render parameters: PNG, 200 dpi
- Inspected restored range: physical pages 59--75 inclusive
- Render dimensions: 1700 x 2200 pixels for every rendered page
- Retained ignored render directory:
  `tmp/pdfs/part2-lines-01649-02450-3f2c0dce-2026-08-13/`

The PDF hash and byte count were checked before rendering and checked again
after inspection. They remained unchanged. The PDF was not rebuilt during
this audit. The earlier visual report remains historical evidence bound to its
earlier PDF hash; none of its page verdicts was reused for physical pages
59--75 here.

## Physical-page and source boundaries

The current outline, auxiliary labels, exact restoration endpoints, rendered
headings, and cross-page continuity establish these boundaries:

- physical 59, printed 35: the relocated inherited source presentation
  *Classical Propositional Logic*, its provenance line, and its introduction;
- physical 60: intentional blank verso corresponding to logical printed page
  36;
- physical 61--69, printed 37--45: Chapter 5, *Propositional Syntax and
  Semantics*, containing the restored treatment through source line 2186;
- physical 69: source line 2186 closes the proof of Theorem 5.19 and therefore
  closes the first restored chapter;
- physical 70: intentional blank verso corresponding to logical printed page
  46;
- physical 71--75, printed 47--51: Chapter 6, *Natural Deduction and Sequents*,
  containing restored source lines 2187--2450;
- physical 75: source line 2450 closes Example 6.7 before the reader note and
  separately attributed Section 6.3 begin on the same page; and
- physical 76: only added Section 6.3 material remains, so it is outside this
  restored-source visual range.

Thus every physical page carrying restored source lines 1649--2450 occurs in
the ledger below exactly once. The Part II opener on physical 57 and its blank
verso on 58 precede source line 1649 and are not credited.

## Exact 17-page restored render ledger

| Physical PDF page | Printed page | 200-dpi render | PNG bytes | PNG SHA-256 | Result | Page-specific inspection |
|---:|---:|---|---:|---|---|---|
| 59 | 35 | `restored-059.png` | 100,059 | `908b4d9a248628e5377c954f810f126189abed398bc5fa3a70f42c1f471df6dc` | PASS | Source presentation title, provenance line, introductory paragraph, citations, centered footer number, whitespace, and margins are balanced, legible, and unclipped. |
| 60 | -- | `restored-060.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso before Chapter 5; no stray ink, header, footer, page number, or rendering artifact. |
| 61 | 37 | `restored-061.png` | 237,008 | `10dada28aa1dec6424b1f94cca06bbab059d6ee05a58d762abe6a429e28fe101` | PASS | Chapter 5 opener, two-line title, Section 5.1, Definitions 5.1--5.2, numbered formation clauses, grammar display, symbols, and centered footer are clear and within margins. |
| 62 | 38 | `restored-062.png` | 379,626 | `24c74e15b2678448166c0237ccbd70e74cba852e326259ca8685ca3c2526064d` | PASS | Typographical conventions, Definition 5.3, finite conjunction and disjunction displays, Lemma 5.4, proof text, even-page chapter head, and page number are sharp and unclipped. |
| 63 | 39 | `restored-063.png` | 410,323 | `03c66bca695bf232428a82ded083726043944902f913ea5ee8a2ffbf3a9d4df0` | PASS | Lemma 5.4 closes; Theorem 5.5 and proof, Definition 5.6, recursion displays, proof squares, odd-page section head, and page number are aligned and legible. |
| 64 | 40 | `restored-064.png` | 334,715 | `3169ea537f411e4e62e94460499ba3b4c23a1eb51aba1b189d6097708512c285` | PASS | Section 5.2, valuation recursion, Lemma 5.8 and proof, Definition 5.9, semantic symbols, and the complete four-row truth table render without collision or missing glyphs. |
| 65 | 41 | `restored-065.png` | 342,259 | `0a001a64b80336f974c6aad3c40ee22fc93e3a698567ffa93d9676bb41a717da` | PASS | Truth-table continuation, Sections 5.3--5.4, the controlled-prose translation table, Examples 5.11--5.12, formula displays, section head, number, and margins are intact. |
| 66 | 42 | `restored-066.png` | 364,829 | `8f720cc77c8eb57017d63558a25e7e0d4649b77da7cc4170bc17da4a7f26cc91` | PASS | Definitions 5.13--5.14, clause coding, piecewise display, normal-form recursion, Lemma 5.15 and its numbered claims, running head, and page number are complete and unclipped. |
| 67 | 43 | `restored-067.png` | 423,083 | `15edda8688df006ec3251b07ff5c64ae7b4dd974a965bf26ec82527b192e4a27` | PASS | Lemma 5.15 proof, Theorems 5.16--5.17, De Morgan and valuation displays, proof squares, running head, and page number are consistent and legible. |
| 68 | 44 | `restored-068.png` | 432,399 | `333ace3b6bfe1e9491f0469cbd9c4a8e5aed7168f4bdf559735c822051d8adf6` | PASS | Theorem 5.17 proof continues through the DNF and CNF constructions; cases, bars, subscripts, superscripts, set braces, quantifiers, running head, and page number remain sharp and within margins. |
| 69 | 45 | `restored-069.png` | 309,884 | `23a47c6762fa1af8143fa10634fe98f4cbdd87399ea70f571cd74310ec40ab42` | PASS | Theorem 5.17 closes; the truth-function paragraph, Definition 5.18, Theorem 5.19 and proof, final proof square, Section 5.4 running head, and page number render cleanly. |
| 70 | -- | `restored-070.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso before Chapter 6; no stray ink, header, footer, page number, or rendering artifact. |
| 71 | 47 | `restored-071.png` | 311,217 | `f7a06ccf896b5be12f31b82e4d372c7eb579c2b41f67d35ecb0627b7ebf9c7f2` | PASS | Chapter 6 opener, two-line title, Section 6.1, Definition 6.1, discharge-label conditions, line wrapping, centered footer number, and margins are legible and unclipped. |
| 72 | 48 | `restored-072.png` | 232,893 | `e8faaa6e29008a518bcd25ddaee82648cbaf624346efeb993d3a433b01b5a318` | PASS | Definition 6.1 continues into the complete natural-deduction rule display. All simple and nested rules, vertical dots, bars, discharge labels, the disjunction-elimination side sentence, Definition 6.2, and Example 6.3 derivation are aligned and readable. |
| 73 | 49 | `restored-073.png` | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** | Example 6.4 and its eight-line derivation are clean, as are Lemma 6.5, its proof, proof square, running head, and page number. One literal `??` is visibly printed in "made exact in `??`". |
| 74 | 50 | `restored-074.png` | 318,859 | `4aaec2ae7a884fe43c902d12f557b7d87131ba0d6d20b81f0c03fa75470a4cc8` | PASS | Section 6.2 and Definition 6.6, support and consequence displays, the complete two-column sequent-rule arrays, structural and logical rules, Cut, labels, running head, and page number are sharp, separated, and unclipped. |
| 75 | 51 | `restored-075.png` | 356,963 | `7c4d22112f01e37a3539d5ea4576535aec0333c1e516bdf1f1a3216d352ef4a4` | PASS | The sequent-derivation definition and nested Example 6.7 tree close the restored source cleanly. The reader note and added Section 6.3 begin below clear separation; the matching page-top running head, citation, displays, and shared boundary have no collision or ambiguous continuation. |

## Visible failure localization

The sole visible placeholder has this read-only localization. This explains the
printed defect but is not a source, provenance, or static-validation verdict.

| Physical page | Visible count | Restoration origin | Pending target |
|---:|---:|---|---|
| 73 | 1 | `handbook/restoration/inherited-02193-02340.tex:119` | `ch:intuitionistic-logic` |

Because the placeholder is visible reader-facing output, physical page 73 and
the overall bounded visual gate fail even though all other inspected layout
features pass.

## Part I scope decision

The former Part I `ch:prop-syntax-semantics` placeholder remains mapped to
physical page 41, printed page 17. A fresh 200-dpi comparison raster was made
from the current PDF solely to determine whether that page's mapping or visible
content changed:

- current comparison render: `part1-map-check-041.png`;
- current PNG bytes: 362,651;
- current PNG SHA-256:
  `419f23fa4317301e6d13705dd1fea60d126bc6159cf356ac145ee110c28edb98`;
- prior approved page-41 render SHA-256:
  `419f23fa4317301e6d13705dd1fea60d126bc6159cf356ac145ee110c28edb98`.

The raster hashes are identical and the physical mapping is unchanged.
Therefore the condition requiring a new Part I visual recheck was not met.
Physical page 41 was not visually re-inspected, is not included in the
17-page ledger, and receives no new visual credit from this report. The
comparison render records the scope decision only.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No ink crosses a text block, trim, header, footer, table rule, inference bar, or page edge; no line, symbol, proof square, or display is cut off. |
| Source presentation and chapter boundaries | PASS | The inherited source presentation occurs on physical 59; blank versos 60 and 70 are intentional; Chapters 5 and 6 begin on 61 and 71; restored content ends on the shared page 75 before added Section 6.3. |
| Headings, running heads, and page numbers | PASS | Chapter openers use centered footer numbers; body-page heads and printed pages 37--51 are ordered and positioned consistently. The Section 6.3 running head on shared page 75 matches the section beginning later on that page. |
| Natural-deduction rules | PASS | Every introduction and elimination rule, nested disjunction-elimination display, assumption label, vertical continuation, inference bar, rule name, and discharge statement on physical 72 is legible and within margins. |
| Sequent rules | PASS | Weakening, contraction, negation, conjunction, disjunction, implication, and Cut displays on physical 74 have intact premises, conclusions, context symbols, labels, spacing, and separation. |
| Derivation trees | PASS | The numbered natural-deduction derivations on physical pages 72--73 and the nested sequent derivation on 75 are complete, aligned, and reader-traceable. |
| Proofs and continuity | PASS | Every proof opening, continuation, and closing square is visible; no proof, definition, display, or example is silently truncated at a page break. |
| Tables and lists | PASS | Formation-clause lists, semantic-notion list, truth table, controlled-prose table, numbered derivations, and rule arrays have consistent alignment and safe margins. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, small-cap, Greek, blackboard-bold, calligraphic, logical, and proof-theoretic glyphs remain visually consistent; no missing-glyph box or substituted symbol is visible. |
| Reference rendering | **FAIL** | One literal `??` remains visible on physical 73 at the forward reference to `ch:intuitionistic-logic`. No other `??` is visible on physical pages 59--75. |
| Intentional blanks | PASS | Physical pages 60 and 70 are wholly blank with no stray mark and correctly separate right-opening chapters. |

## Cross-page continuity ledger

- Physical 59 is followed by intentional blank verso 60; Chapter 5 begins on
  physical 61.
- Physical 61 ends after the grammar display; physical 62 begins with the
  typographical conventions that apply to that grammar.
- Physical 62 ends inside the proof of Lemma 5.4; physical 63 resumes and closes
  it before presenting unique readability and the complexity recursion.
- Physical 64 ends with the truth table; physical 65 begins with the sentence
  explaining what that table checks.
- Physical 65 ends at the opening of Definition 5.13; physical 66 resumes its
  definition of a propositional literal and clause.
- Physical 66 ends after the two claims of Lemma 5.15; physical 67 begins their
  proof and continues through the start of Theorem 5.17.
- Physical 67 ends inside the construction used for Theorem 5.17; physical 68
  continues it and ends inside the final CNF argument. Physical 69 resumes and
  closes that argument, then completes Chapter 5.
- Physical 69 is followed by intentional blank verso 70; Chapter 6 begins on
  physical 71.
- Physical 71 ends inside the explanation of label merging; physical 72 begins
  "used when" and completes the sentence before displaying every rule.
- Physical 72 closes Example 6.3; physical 73 presents Example 6.4 and completes
  the substitution lemma and proof before Section 6.2 begins on 74.
- Physical 74 ends after the Cut display; physical 75 gives the derivation
  definition and Example 6.7, closing restored source line 2450 before the
  reader note and added Section 6.3.

## Scope limits

This record is bounded visual evidence only for restored source lines
1649--2450 on physical pages 59--75 of the exact PDF hash above. The Part I
page-41 raster comparison establishes only that its mapping and pixels did not
change; it is not a new visual inspection. This record does **not** establish
source-byte equality, provenance, source-fidelity AI review, topic-specialist
AI review, adversarial-publication AI review, static validation, a clean or
complete build, mathematical correctness, section admission or locking,
whole-book visual correctness, human review, user review, or user final
acceptance. No independent gate is promoted by this record.
