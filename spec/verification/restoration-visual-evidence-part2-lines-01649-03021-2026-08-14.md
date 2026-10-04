# Restoration visual evidence for Part II source lines 01649--03021 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Every physical PDF page
containing reader-facing material from restored source lines 1649--3021 was
mapped, freshly rendered at fixed 200 dpi from the frozen PDF checkpoint, and
inspected at its original render resolution. The complete physical coverage
envelope is pages 59--87 inclusive. All 29 pages in that envelope were
rendered and inspected exactly once: 28 page verdicts pass and one fails.
Physical page 73 fails because one unresolved reference visibly prints as
`??` in the sentence about where intuitionistic natural deduction is made
exact.

Within the 29-page envelope, physical pages 76--78 contain only the separately
attributed editorial Hilbert, tableau, and comparison supplement between two
exact inherited chapters. Those three pages pass the visual inspection needed
to establish the route boundary and cross-page continuity, but receive no
restored-source credit. Counting only pages carrying restored content plus its
intentional blank versos gives 26 restored-route pages: 25 pass and one fails.

No clipping, overlap, margin collision, missing or substituted mathematical
glyph, malformed heading, running-head defect, page-number defect, broken
table or list, broken rule array, broken derivation tree, malformed side
condition, or cross-page continuity defect was found. The otherwise-correct
layout does not override the visible-reference failure.

Physical pages 60 and 70 are intentional blank versos. Physical page 75 is a
shared boundary page: it completes source line 2450 before the reader note and
separately attributed supplement begin. Physical pages 82, 84, and 86 are
shared boundaries between successive exact restoration intervals within the
metatheory chapter. Physical page 87 closes source line 3021; the editorial
supplement begins on physical page 88 and is outside this audit.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, AI review, static validation, build approval,
admission, human review, or user acceptance.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- SHA-256:
  `bb73665b27fff68ecbf004294c487c65c66a1cf63c97a5661a4560b9d2764eef`
- File size: 4,281,396 bytes
- Physical page count: 795
- Default page geometry: US Letter, 612 x 792 points, rotation 0
- Physical page 78 geometry: US Letter, 612 x 792 points, rotation 90
- PDF version: 1.5
- Renderer: Poppler `pdftoppm` 26.05.0
- Render parameters: PNG, 200 dpi
- Inspected envelope: physical pages 59--87 inclusive
- Portrait render dimensions: 1700 x 2200 pixels for pages 59--77 and 79--87
- Landscape render dimensions: 2200 x 1700 pixels for rotated physical page 78
- Retained ignored render directory:
  `tmp/pdfs/part2-lines-01649-03021-bb73665b-2026-08-14/`

The PDF hash and byte count were checked before rendering and checked again
after inspection. They remained unchanged. The PDF was not rebuilt during
this audit. Both earlier Part II visual reports remain historical evidence
bound to earlier PDF hashes; none of their page verdicts was reused here.

## Physical-page and source boundaries

The current outline, auxiliary labels, exact restoration endpoints, rendered
headings, and cross-page continuity establish these boundaries:

- physical 59, printed 35: restored source lines 1649--1656, comprising the
  relocated inherited source presentation *Classical Propositional Logic*,
  its provenance line, and its introduction;
- physical 60: intentional blank verso corresponding to logical printed page
  36;
- physical 61--69, printed 37--45: Chapter 5, *Propositional Syntax and
  Semantics*, containing restored source lines 1658--2186;
- physical 69: source line 2186 closes the proof of Theorem 5.19 and therefore
  closes Chapter 5;
- physical 70: intentional blank verso corresponding to logical printed page
  46;
- physical 71--75, printed 47--51: Chapter 6, *Natural Deduction and Sequents*,
  containing restored source lines 2187--2450;
- physical 75: source line 2450 closes Example 6.7 before the reader note and
  separately attributed Section 6.3 begin on the same page;
- physical 76--78, printed 52--54: editorial supplement only; physical page 78
  is the rotated proof-system comparison table and none of these three pages
  receives restored-source credit;
- physical 79--80, printed 55--56: exact `SRC-02451-02544`, Chapter 7 and
  Section 7.1, ending with the proof of sequent-calculus soundness;
- physical 81--82, printed 57--58: exact `SRC-02545-02664`, Section 7.2,
  ending with the truth-lemma proof before Section 7.3 begins on page 82;
- physical 82--84, printed 58--60: exact `SRC-02665-02809`, Section 7.3,
  ending with the sequent-completeness proof sketch before Section 7.4 begins
  on page 84;
- physical 84--86, printed 60--62: exact `SRC-02810-02914`, Section 7.4,
  ending with the resolution attribution and further-reading paragraph before
  Section 7.5 begins on page 86;
- physical 86, printed 62: exact `SRC-02915-02932`, Section 7.5 and its complete
  seven-item warning list;
- physical 87, printed 63: exact `SRC-02933-03021`, Section 7.6 and all twelve
  exercises, with source line 3021 closing the final environment; and
- physical 88, printed 64: only the separately attributed editorial supplement
  remains, so it is outside the restored-source visual range.

Thus every physical page carrying restored source lines 1649--3021, each
intentional blank verso belonging to that route, and every interstitial page
needed to prove the route boundary occurs in the ledger below exactly once.
The Part II opener on physical 57 and its blank verso on 58 precede source line
1649 and are not credited.

## Exact 29-page render ledger

`Scope` is `restored` for pages carrying exact inherited content, `blank` for
an intentional blank verso in the restored route, and `interstitial` for a
separately attributed editorial page inspected only to establish the boundary
and continuity between exact inherited chapters.

| Physical PDF page | Printed page | Scope | 200-dpi render | PNG bytes | PNG SHA-256 | Result | Page-specific inspection |
|---:|---:|---|---|---:|---|---|---|
| 59 | 35 | restored | `restored-059.png` | 100,059 | `908b4d9a248628e5377c954f810f126189abed398bc5fa3a70f42c1f471df6dc` | PASS | Source presentation title, provenance line, introduction, citations, centered footer, whitespace, and margins are balanced, legible, and unclipped. |
| 60 | -- | blank | `restored-060.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso before Chapter 5; no stray ink, header, footer, page number, or rendering artifact. |
| 61 | 37 | restored | `restored-061.png` | 237,008 | `10dada28aa1dec6424b1f94cca06bbab059d6ee05a58d762abe6a429e28fe101` | PASS | Chapter 5 opener, two-line title, Section 5.1, Definitions 5.1--5.2, numbered formation clauses, grammar display, symbols, and centered footer are clear and within margins. |
| 62 | 38 | restored | `restored-062.png` | 379,626 | `24c74e15b2678448166c0237ccbd70e74cba852e326259ca8685ca3c2526064d` | PASS | Typographical conventions, Definition 5.3, finite conjunction and disjunction displays, Lemma 5.4, proof text, even-page chapter head, and page number are sharp and unclipped. |
| 63 | 39 | restored | `restored-063.png` | 410,323 | `03c66bca695bf232428a82ded083726043944902f913ea5ee8a2ffbf3a9d4df0` | PASS | Lemma 5.4 closes; Theorem 5.5 and proof, Definition 5.6, recursion displays, proof squares, odd-page section head, and page number are aligned and legible. |
| 64 | 40 | restored | `restored-064.png` | 334,715 | `3169ea537f411e4e62e94460499ba3b4c23a1eb51aba1b189d6097708512c285` | PASS | Section 5.2, valuation recursion, Lemma 5.8 and proof, Definition 5.9, semantic symbols, and the complete four-row truth table render without collision or missing glyphs. |
| 65 | 41 | restored | `restored-065.png` | 342,259 | `0a001a64b80336f974c6aad3c40ee22fc93e3a698567ffa93d9676bb41a717da` | PASS | Truth-table continuation, Sections 5.3--5.4, controlled-prose table, Examples 5.11--5.12, displays, running head, page number, and margins are intact. |
| 66 | 42 | restored | `restored-066.png` | 364,829 | `8f720cc77c8eb57017d63558a25e7e0d4649b77da7cc4170bc17da4a7f26cc91` | PASS | Definitions 5.13--5.14, clause coding, piecewise display, normal-form recursion, Lemma 5.15 and its numbered claims, running head, and page number are complete and unclipped. |
| 67 | 43 | restored | `restored-067.png` | 423,083 | `15edda8688df006ec3251b07ff5c64ae7b4dd974a965bf26ec82527b192e4a27` | PASS | Lemma 5.15 proof, Theorems 5.16--5.17, De Morgan and valuation displays, proof squares, running head, and page number are consistent and legible. |
| 68 | 44 | restored | `restored-068.png` | 432,399 | `333ace3b6bfe1e9491f0469cbd9c4a8e5aed7168f4bdf559735c822051d8adf6` | PASS | Theorem 5.17 proof continues through the DNF and CNF constructions; cases, bars, subscripts, superscripts, braces, running head, and page number remain sharp and within margins. |
| 69 | 45 | restored | `restored-069.png` | 309,884 | `23a47c6762fa1af8143fa10634fe98f4cbdd87399ea70f571cd74310ec40ab42` | PASS | Theorem 5.17 closes; Definition 5.18, Theorem 5.19 and proof, final proof square, Section 5.4 running head, and page number render cleanly. |
| 70 | -- | blank | `restored-070.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso before Chapter 6; no stray ink, header, footer, page number, or rendering artifact. |
| 71 | 47 | restored | `restored-071.png` | 311,217 | `f7a06ccf896b5be12f31b82e4d372c7eb579c2b41f67d35ecb0627b7ebf9c7f2` | PASS | Chapter 6 opener, two-line title, Section 6.1, Definition 6.1, discharge-label conditions, line wrapping, centered footer, and margins are legible and unclipped. |
| 72 | 48 | restored | `restored-072.png` | 232,893 | `e8faaa6e29008a518bcd25ddaee82648cbaf624346efeb993d3a433b01b5a318` | PASS | Definition 6.1 continues into the complete natural-deduction rule display. All nested rules, vertical dots, bars, discharge labels, side sentence, Definition 6.2, and Example 6.3 derivation are aligned and readable. |
| 73 | 49 | restored | `restored-073.png` | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** | Example 6.4 and its eight-line derivation are clean, as are Lemma 6.5, its proof, proof square, running head, and page number. One literal `??` is visibly printed in "made exact in `??`". |
| 74 | 50 | restored | `restored-074.png` | 318,859 | `4aaec2ae7a884fe43c902d12f557b7d87131ba0d6d20b81f0c03fa75470a4cc8` | PASS | Section 6.2 and Definition 6.6, support and consequence displays, complete two-column sequent-rule arrays, structural and logical rules, Cut, labels, running head, and page number are sharp, separated, and unclipped. |
| 75 | 51 | restored/shared | `restored-075.png` | 356,963 | `7c4d22112f01e37a3539d5ea4576535aec0333c1e516bdf1f1a3216d352ef4a4` | PASS | The exact sequent-derivation definition and nested Example 6.7 tree close source line 2450 cleanly. The reader note and added Section 6.3 begin below clear separation; the citation, displays, running head, and shared boundary have no collision. |
| 76 | 52 | interstitial | `restored-076.png` | 353,741 | `4b4867f54922944f80f78e1913c84e53d3e105685743717a79f2034c9563a611` | PASS | The Hilbert translation display, equivalence theorem, warning, and start of analytic tableaux are legible; registry identifiers are intentionally printed lookup text, not unresolved-reference placeholders. No restored-source credit is assigned. |
| 77 | 53 | interstitial | `restored-077.png` | 291,808 | `7a7d26678440d38eca50d7755d63db49878dfcf1a0e52a46c000c9fb96144144` | PASS | Natural-deduction/LK correspondence figure, tableau theorem, closed-tableau figure, captions, arrows, labels, running head, and page number are intact and within margins. No restored-source credit is assigned. |
| 78 | 54 | interstitial | `restored-078.png` | 215,759 | `20a9c801faabf422e169e1904658420077ef61b3c4c57aaee10a0949eaa9b9fd` | PASS | The intentional 90-degree landscape proof-system comparison page renders at 2200 x 1700; all five rows, rules, registry identifiers, column heads, table rules, rotated running head, and page number are legible and unclipped. No restored-source credit is assigned. |
| 79 | 55 | restored | `restored-079.png` | 269,924 | `b348fc3937faf5bd692f9536440a01ecda6290edf9e4ac8e5da04fe096df36ed` | PASS | Chapter 7 opener, three-line title, Section 7.1, Theorem 7.1, consequence display, proof opening, mathematical symbols, centered footer, and margins are balanced and legible. |
| 80 | 56 | restored | `restored-080.png` | 422,110 | `61979c081ea2eead2c7f0f4c44893d10e0f278938076fa3c00499f13aee55fdc` | PASS | Theorem 7.1 closes and Theorem 7.2 plus its full proof render without clipping. The long even-page running head remains distinct from the page number and inside the margin. |
| 81 | 57 | restored | `restored-081.png` | 412,827 | `30c744ca21d9b125a85c335bfc7bba9c32cda9d2b13448b3fb71a097d8b1fb1f` | PASS | Section 7.2, Definitions 7.3--7.4, five-item Lemma 7.5, its proof, proof square, logical glyphs, section head, and page number are complete and readable. |
| 82 | 58 | restored/shared | `restored-082.png` | 350,388 | `400b267914ef7b8e42c08418346c0cd215a3c22dc4660dbd3af5b349e4eac54c` | PASS | Lemmas 7.6--7.7, recursion and truth displays, both proofs and squares close Section 7.2; Section 7.3, Theorem 7.8, and its proof begin below clear separation. |
| 83 | 59 | restored | `restored-083.png` | 423,026 | `96f755a470823e65d1f235e288fd374944bc06b5149a30b6935de294b766848d` | PASS | Completeness proof closes; equivalence display, compactness theorem and proof, sequent-completeness theorem and proof sketch, list and formulas are legible with intact continuation. |
| 84 | 60 | restored/shared | `restored-084.png` | 387,393 | `e748a5d0b55f56c8ea60e019473593607430a15edf70d5f2665d3ca9bf992d43` | PASS | Five-step sequent construction, displayed Cut instance, edge-case paragraph, proof square, Section 7.4 opening, and Definition 7.11 start render cleanly and remain within margins. |
| 85 | 61 | restored | `restored-085.png` | 448,975 | `b6c40e08a6ff8cf4dcfcf801b9484b18ef117f4bb181cc1965c2f5872cb12abe` | PASS | Resolvent display, resolution-derivation definition, Theorems 7.12--7.13, proofs, complement bars, braces, subscripts, proof square, running head, and page number are sharp and continuous. |
| 86 | 62 | restored/shared | `restored-086.png` | 414,571 | `73fed777c4d235cae3d670cc387f5026b354e3e78d17f7d00c5c7bff9befccd9` | PASS | Resolution proof closes; Remark 7.14, citations, Section 7.5, and the complete seven-item warning list render clearly. The long even-page running head remains readable and unclipped. |
| 87 | 63 | restored | `restored-087.png` | 388,344 | `4e7bc835c97c922ff15beb7270c7afb67da401483f1f2b394144507082ba0a27` | PASS | Section 7.6 contains all twelve exercises, including the centered clause-set display; numbering, continuations, symbols, section head, page number, final line, and source endpoint are complete and unclipped. |

## Visible failure localization

The sole visible placeholder has this read-only localization. This explains
the printed defect but is not a source, provenance, or static-validation
verdict.

| Physical page | Visible count | Restoration origin | Pending target |
|---:|---:|---|---|
| 73 | 1 | `handbook/restoration/inherited-02193-02340.tex:119` | `ch:intuitionistic-logic` |

A page-by-page text-extraction scan and the visual inspection both found no
other literal `??` on physical pages 59--87. Because this placeholder is
visible reader-facing output, physical page 73 and the overall bounded visual
gate fail even though all other inspected layout features pass.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No ink crosses a text block, trim, header, footer, table rule, inference bar, or page edge; no line, symbol, proof square, list item, or display is cut off. |
| Source presentation and chapter boundaries | PASS | The inherited source presentation occurs on physical 59; blank versos 60 and 70 are intentional; Chapters 5, 6, and 7 begin on 61, 71, and 79; the editorial interstitial occupies 76--78; restored content ends on 87. |
| Headings, running heads, and page numbers | PASS | Chapter openers use centered footer numbers; body-page heads and printed pages 35--63 are ordered and positioned consistently. Long Chapter 7 even-page heads remain separated from the page numbers. |
| Natural-deduction rules | PASS | Every introduction and elimination rule, nested disjunction-elimination display, assumption label, vertical continuation, inference bar, rule name, and discharge statement on physical 72 is legible and within margins. |
| Sequent rules and Cut displays | PASS | Weakening, contraction, negation, conjunction, disjunction, implication, and Cut on physical 74, and the derived Cut construction on 84, have intact premises, conclusions, contexts, labels, spacing, and separation. |
| Derivation trees and diagrams | PASS | Natural-deduction derivations on physical 72--73, the sequent derivation on 75, the correspondence and tableau figures on 77, and the Cut display on 84 are complete, aligned, and reader-traceable. |
| Proofs and continuity | PASS | Every proof opening, continuation, and closing square is visible; no theorem, proof, definition, display, remark, warning, example, or exercise is silently truncated at a page break. |
| Tables and lists | PASS | Formation clauses, semantic notions, truth and controlled-prose tables, numbered proof steps, rule arrays, warning items, twelve exercises, and the rotated comparison table have consistent alignment and safe margins. |
| Landscape page | PASS | Physical page 78 intentionally rotates 90 degrees; its table, running head, page number, and all five rows render at 2200 x 1700 with no crop, overlap, or unreadable cell. |
| Fonts and glyph consistency | PASS | Roman, italic, bold, small-cap, Greek, blackboard-bold, calligraphic, logical, and proof-theoretic glyphs remain visually consistent; no missing-glyph box or substituted symbol is visible. |
| Reference rendering | **FAIL** | One literal `??` remains visible on physical 73 at the forward reference to `ch:intuitionistic-logic`. No other literal `??` is visible on physical pages 59--87. |
| Intentional blanks | PASS | Physical pages 60 and 70 are wholly blank with no stray mark and correctly separate right-opening chapters. |

## Cross-page continuity ledger

- Physical 59 is followed by intentional blank verso 60; Chapter 5 begins on
  physical 61.
- Physical 61 ends after the grammar display; physical 62 begins with the
  typographical conventions applying to that grammar.
- Physical 62 ends inside the proof of Lemma 5.4; physical 63 resumes and
  closes it before presenting unique readability and the complexity recursion.
- Physical 64 ends with the truth table; physical 65 begins with the sentence
  explaining what that table checks.
- Physical 65 ends at the opening of Definition 5.13; physical 66 resumes its
  definition of a propositional literal and clause.
- Physical 66 ends after the two claims of Lemma 5.15; physical 67 begins their
  proof and continues through the start of Theorem 5.17.
- Physical 67 ends inside the construction for Theorem 5.17; physical 68
  continues it and ends inside the final CNF argument. Physical 69 resumes and
  closes that argument, then completes Chapter 5.
- Physical 69 is followed by intentional blank verso 70; Chapter 6 begins on
  physical 71.
- Physical 71 ends inside the explanation of label merging; physical 72 begins
  "used when" and completes the sentence before displaying every rule.
- Physical 72 closes Example 6.3; physical 73 presents Example 6.4 and completes
  the substitution lemma and proof before Section 6.2 begins on 74.
- Physical 74 ends after the Cut display; physical 75 gives the derivation
  definition and Example 6.7, closing source line 2450 before the reader note
  and editorial supplement.
- Physical pages 76--78 continue only the editorial supplement. The rotated
  comparison table closes on 78; exact source line 2451 begins Chapter 7 on
  physical 79 with no duplicated or blended transition.
- Physical 79 ends inside the proof of Theorem 7.1; physical 80 resumes and
  closes it, then completes the exact soundness interval with Theorem 7.2 and
  its proof.
- Physical 81 presents the first portion of Section 7.2; physical 82 resumes
  with the Lindenbaum and truth lemmas, closes their proofs, and then begins
  Section 7.3.
- Physical 82 ends inside the proof of Theorem 7.8; physical 83 resumes and
  closes it, proves compactness, and begins the sequent-completeness proof
  sketch.
- Physical 83 ends before the proof sketch's numbered construction; physical
  84 supplies all five steps and the Cut display, closes the proof, and begins
  propositional resolution.
- Physical 84 ends at Definition 7.11; physical 85 resumes the resolvent formula
  and continues through Theorem 7.13's proof.
- Physical 85 ends inside the resolution proof; physical 86 resumes and closes
  it, presents the finite-to-arbitrary scope remark, and completes the
  seven-item common-errors warning.
- Physical 87 contains all twelve exercises and closes source line 3021. The
  editorial supplement begins on physical 88, outside this ledger.

## Render-coverage validation

- One render call requested the closed physical interval 59--87 at 200 dpi.
- The retained directory contains exactly 29 files named
  `restored-059.png` through `restored-087.png` with no missing, duplicate, or
  out-of-range page identifier.
- Every portrait render is exactly 1700 x 2200 pixels.
- The sole rotated render, physical page 78, is exactly 2200 x 1700 pixels.
- Every PNG byte count and SHA-256 digest is recorded in the ledger above.
- The PDF title, page count, byte count, geometry, rotations, version, and
  SHA-256 were re-read from the same file used for rendering.
- The PDF SHA-256 remained
  `bb73665b27fff68ecbf004294c487c65c66a1cf63c97a5661a4560b9d2764eef`
  after inspection.

## Scope limits

This record is bounded visual evidence only for restored source lines
1649--3021 and the explicitly identified interstitial boundary pages on
physical pages 59--87 of the exact PDF hash above. The three interstitial
pages receive no restored-source credit. This record does **not** establish
source-byte equality, provenance, source-fidelity AI review, topic-specialist
AI review, adversarial-publication AI review, static validation, a clean or
complete build, mathematical correctness, section admission or locking,
whole-book visual correctness, human review, user review, or user final
acceptance. No independent gate is promoted by this record.
