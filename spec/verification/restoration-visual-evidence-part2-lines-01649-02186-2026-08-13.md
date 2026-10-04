# Restoration visual evidence for Part II source lines 01649--02186 - 2026-08-13

## Bounded verdict

**PASS for the bounded rendered-page visual gate for the exact restored
presentation.** Every physical PDF page containing reader-facing material from
source lines 1649--2186 was mapped, freshly rendered at fixed 200 dpi, and
inspected exactly once at the original 1700 x 2200 pixel render resolution.
All 11 physical pages in the resulting range, 59--69 inclusive, pass.

Physical page 60 is the intentional blank verso between the inherited source
part presentation and Chapter 5. Physical page 69 is a shared boundary page:
it completes the restored normal-form proof and functional-completeness
treatment before the added Section 5.5 begins. The whole page was inspected,
but this record credits only its restored content and the visual integrity of
that shared boundary.

No clipping, overlap, margin collision, malformed mathematical glyph,
malformed table, broken proof or equation display, heading defect, running-head
defect, page-number defect, cross-page continuity defect, or visible `??`
reference placeholder was found in physical pages 59--69.

The narrow Part I recheck also **passes**: physical page 41 now visibly reads
"the grammar of chapter 5" rather than "the grammar of `??`". This repairs only
the formerly visible `ch:prop-syntax-semantics` placeholder on that page. No
other Part I page is re-inspected or credited here, and this narrow result does
not by itself replace the earlier bounded Part I verdict.

These verdicts are visual evidence only. They do not establish source fidelity,
mathematical correctness, AI review, static validation, build approval,
admission, human review, or user acceptance.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- SHA-256:
  `fea49904e36ade1ac19f0219b3a8d6840f281a3ccaa4edb1076f6fc56813a0bc`
- File size: 4,266,198 bytes
- Physical page count: 789
- Page geometry: US Letter, 612 x 792 points, rotation 0
- PDF version: 1.5
- Renderer: Poppler `pdftoppm` 26.05.0
- Render parameters: PNG, 200 dpi
- Restored range: physical pages 59--69 inclusive
- Narrow Part I recheck: physical page 41 only
- Render dimensions: 1700 x 2200 pixels for every inspected page
- Retained ignored render directory:
  `tmp/pdfs/part2-lines-01649-02186-2026-08-13/`

The PDF hash and byte count were checked before rendering and checked again
after inspection. They remained unchanged. The PDF was not rebuilt during
this audit.

## Physical-page and source boundaries

The existing outline, auxiliary labels, rendered headings, and cross-page
continuity establish these boundaries:

- physical 59, printed 35: the relocated inherited source presentation
  *Classical Propositional Logic*, its provenance line, and its introduction;
- physical 60: intentional blank verso, corresponding to logical printed page
  36;
- physical 61, printed 37: Chapter 5, *Propositional Syntax and Semantics*, and
  Section 5.1 begin;
- physical 62--63, printed 38--39: Section 5.1 continues and closes;
- physical 64, printed 40: Section 5.2;
- physical 65, printed 41: Section 5.3 and then Section 5.4 begin;
- physical 66--68, printed 42--44: Section 5.4 continues;
- physical 69, printed 45: the restored Section 5.4 proof continues, Definition
  5.18 and Theorem 5.19 are presented and proved, and source line 2186 closes
  that proof before added Section 5.5 begins on the same page; and
- physical 70: only added Section 5.5 content remains, so it is outside this
  restored-source visual range.

The targeted Part I phrase occurs on physical page 41, printed page 17, in
Section 2.3. No other Part I page is within this record's recheck scope.

## Exact 11-page restored render ledger

| Physical PDF page | Printed page | 200-dpi render | PNG bytes | PNG SHA-256 | Result | Page-specific inspection |
|---:|---:|---|---:|---|---|---|
| 59 | 35 | `restored-059.png` | 100,059 | `908b4d9a248628e5377c954f810f126189abed398bc5fa3a70f42c1f471df6dc` | PASS | Source presentation title, provenance line, introductory paragraph, citations, centered footer number, whitespace, and margins are balanced, legible, and unclipped. |
| 60 | -- | `restored-060.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso; no stray ink, header, footer, page number, or rendering artifact. |
| 61 | 37 | `restored-061.png` | 237,008 | `10dada28aa1dec6424b1f94cca06bbab059d6ee05a58d762abe6a429e28fe101` | PASS | Chapter 5 opener, two-line title, Section 5.1, Definitions 5.1--5.2, numbered formation clauses, grammar display, symbols, and centered footer are clear and within margins. |
| 62 | 38 | `restored-062.png` | 379,626 | `24c74e15b2678448166c0237ccbd70e74cba852e326259ca8685ca3c2526064d` | PASS | Typographical conventions, Definition 5.3, finite conjunction and disjunction displays, Lemma 5.4, proof text, even-page chapter head, and page number are sharp and unclipped. |
| 63 | 39 | `restored-063.png` | 410,323 | `03c66bca695bf232428a82ded083726043944902f913ea5ee8a2ffbf3a9d4df0` | PASS | Lemma 5.4 closes; Theorem 5.5 and its proof, Definition 5.6, recursion displays, proof squares, odd-page section head, and page number are aligned and legible. |
| 64 | 40 | `restored-064.png` | 334,715 | `3169ea537f411e4e62e94460499ba3b4c23a1eb51aba1b189d6097708512c285` | PASS | Section 5.2, valuation recursion, Lemma 5.8 and proof, Definition 5.9, semantic symbols, and the complete four-row truth table render without collision or missing glyphs. |
| 65 | 41 | `restored-065.png` | 342,259 | `0a001a64b80336f974c6aad3c40ee22fc93e3a698567ffa93d9676bb41a717da` | PASS | Truth-table continuation, Sections 5.3--5.4, the controlled-prose translation table, Examples 5.11--5.12, formula displays, section head, number, and margins are intact. |
| 66 | 42 | `restored-066.png` | 364,829 | `8f720cc77c8eb57017d63558a25e7e0d4649b77da7cc4170bc17da4a7f26cc91` | PASS | Definitions 5.13--5.14, clause coding, piecewise display, normal-form recursion, Lemma 5.15 and its numbered claims, running head, and page number are complete and unclipped. |
| 67 | 43 | `restored-067.png` | 423,083 | `15edda8688df006ec3251b07ff5c64ae7b4dd974a965bf26ec82527b192e4a27` | PASS | Lemma 5.15 proof, Theorems 5.16--5.17, De Morgan and valuation displays, proof squares, running head, and page number are consistent and legible. |
| 68 | 44 | `restored-068.png` | 432,399 | `333ace3b6bfe1e9491f0469cbd9c4a8e5aed7168f4bdf559735c822051d8adf6` | PASS | Theorem 5.17 proof continues through the DNF and CNF constructions; cases, bars, subscripts, superscripts, set braces, quantifiers, running head, and page number remain sharp and within margins. |
| 69 | 45 | `restored-069.png` | 412,218 | `a5fe88d66186c2cfa3e8c550951c573db50876b4560ad91a732d2ac7eb3a4ade` | PASS | Theorem 5.17 closes; the truth-function paragraph, Definition 5.18, Theorem 5.19 and proof all render cleanly. The added Section 5.5 begins below a clear heading; its matching page-top running head is intact, and the shared boundary has no collision or ambiguous continuation. |

## Narrow Part I recheck ledger

| Physical PDF page | Printed page | 200-dpi render | PNG bytes | PNG SHA-256 | Result | Credited observation |
|---:|---:|---|---:|---|---|---|
| 41 | 17 | `part1-recheck-041.png` | 362,651 | `419f23fa4317301e6d13705dd1fea60d126bc6159cf356ac145ee110c28edb98` | PASS | The formerly failing phrase now visibly reads "the grammar of chapter 5" with no `??`. Section 2.3, Warning 2.9, formulas, headings, running head, page number, and margins remain intact. Only this one repaired placeholder is credited. |

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No ink crosses a text block, trim, header, footer, table rule, or page edge; no line, symbol, proof square, or display is cut off. |
| Source presentation and chapter boundary | PASS | The inherited source presentation occurs on physical 59, blank verso 60 separates it from Chapter 5 on 61, and the final restored proof closes on the shared boundary page 69 before added Section 5.5. |
| Headings, running heads, and page numbers | PASS | The source presentation and chapter opener use their intended display styles; body-page heads and printed pages 37--45 are ordered and positioned consistently. The Section 5.5 running head on shared page 69 matches the section beginning later on that page. |
| Equations and mathematical symbols | PASS | Logical connectives, consequence signs, truth values, arrows, hats, bars, braces, cases, finite conjunction and disjunction signs, subscripts, superscripts, quantifiers, set operations, and proof squares are sharp and correctly positioned. |
| Proofs and continuity | PASS | Every proof opening, continuation, and closing square is visible; no proof is silently truncated at a page break. Theorem 5.17 continues coherently through physical pages 67--69. |
| Tables and lists | PASS | Formation-clause lists, semantic-notion list, the truth table, and the controlled-prose translation table use clear rules, consistent alignment, safe margins, and readable entries. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, small-cap, Greek, blackboard-bold, calligraphic, and mathematical glyphs remain visually consistent with surrounding pages; no missing-glyph box or substituted symbol is visible. |
| Reference rendering | PASS | No literal `??` appears on physical pages 59--69. The targeted prior placeholder on physical 41 now renders as "chapter 5". |
| Intentional blank | PASS | Physical page 60 is wholly blank with no stray mark and correctly separates the source presentation from the right-opening chapter. |

## Cross-page continuity ledger

- Physical 59 is followed by the intentional blank verso 60; Chapter 5 begins
  on physical 61.
- Physical 61 ends after the grammar display; physical 62 begins with the
  typographical conventions that apply to that grammar.
- Physical 62 ends inside the proof of Lemma 5.4; physical 63 resumes and closes
  it before presenting unique readability and the complexity recursion.
- Physical 64 ends with the truth table; physical 65 begins with the sentence
  explaining what that table checks.
- Physical 65 ends at the opening of Definition 5.13; physical 66 resumes its
  definition of a propositional literal and clause.
- Physical 66 ends after the two claims of Lemma 5.15; physical 67 begins its
  proof and continues through the start of Theorem 5.17.
- Physical 67 ends inside the construction used for Theorem 5.17; physical 68
  continues it and ends inside the final CNF argument.
- Physical 69 resumes and closes that argument, then presents and proves
  functional completeness before the added Section 5.5 begins. Physical 70
  contains only that added section and is not credited.

## Scope limits

This record is bounded visual evidence only for restored source lines
1649--2186 on physical pages 59--69 of the exact PDF hash above, plus the one
specified prior-placeholder recheck on physical page 41. It does **not**
establish source-byte equality, provenance, source-fidelity AI review,
topic-specialist AI review, adversarial-publication AI review, static
validation, a clean or complete build, mathematical correctness, section
admission or locking, whole-book visual correctness, human review, user review,
or user final acceptance. No independent gate is promoted by this record.
