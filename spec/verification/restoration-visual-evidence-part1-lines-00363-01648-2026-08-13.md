# Restoration visual evidence for Part I source lines 00363--01648 -- 2026-08-13

## Bounded verdict

**FAIL for the bounded Part I rendered-page visual gate.** All 28 physical PDF
pages in the assigned interval, 29--56 inclusive, were freshly rendered at
fixed 200 dpi from the corrected checkpoint and inspected exactly once at the
original 1700 x 2200 pixel resolution. Twenty-four pages pass. Physical pages
41, 42, 54, and 56 fail because they visibly print five unresolved `??`
reference placeholders.

No clipping, overlap, margin collision, missing or substituted mathematical
glyph, malformed heading, running-head defect, page-number defect, broken
equation or inference-rule display, malformed list, broken longtable row, or
cross-page continuity defect was found. Those otherwise-correct layout results
do not override the visible-reference failures.

This verdict is bound only to the exact corrected PDF and corrected render set
below. It is visual evidence only; it is not a source, content, AI review,
full-build, admission, or human/user-review verdict.

## Corrected checkpoint and render parameters

- PDF: `handbook/main.pdf`
- SHA-256:
  `c3cb5c2630946cda36aa4ddf1ff71513c0fa1b6cdd8ebc031286c80f43bfc814`
- File size: 4,296,563 bytes
- Physical page count: 795
- Page geometry: US Letter, 612 x 792 points, rotation 0
- Renderer: Poppler `pdftoppm` 26.05.0
- Render parameters: PNG, 200 dpi, physical pages 29--56 inclusive
- Render dimensions: 1700 x 2200 pixels for every page
- Corrected retained render directory:
  `tmp/pdfs/part1-reconciled-c3cb5c26/`

The PDF hash and byte count were checked before rendering and checked again
after the inspection. They remained unchanged.

The earlier directory `tmp/pdfs/part1-reconciled-14756e8b/` is explicitly
superseded scratch from an invalidated PDF checkpoint. It was not credited,
its observations and hashes were not reused, and no report was finalized from
it. The corrected `c3cb5c26` directory above is the sole render evidence for
this record.

## Physical-page and chapter boundaries

The PDF outline independently locates the complete assigned range as follows:

- physical 29: Part I, *Foundations of Formal Work*, printed page 5;
- physical 30: intentional blank verso, logical printed page 6;
- physical 31: Chapter 1, *Sets, Relations, Functions, and Cardinality*;
- physical 38: intentional blank verso, logical printed page 14;
- physical 39: Chapter 2, *Levels, Objects, and Consequence*;
- physical 45: Chapter 3, *Finite Strings, Induction, and Recursion*;
- physical 51: Chapter 4, *Writing Formal Definitions and Proofs*;
- physical 56: final Part I content, printed page 32; and
- physical 57: Part II, *Classical Logic*, outside this visual-audit range.

Thus every physical Part I page occurs in the ledger below exactly once, and
no Part II page is credited.

## Exact 28-page render ledger

| Physical PDF page | Printed page | Corrected 200-dpi render | PNG bytes | PNG SHA-256 | Result | Page-specific inspection |
|---:|---:|---|---:|---|---|---|
| 29 | 5 | `page-029.png` | 31,763 | `5e875b3e2af68b86851aea85a8b63716cca6f193ba3481fbed292052ee08a894` | PASS | Sole Part I opener. Part number, title, centered footer number, type, whitespace, and margins are balanced and unclipped. |
| 30 | -- | `page-030.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso between the Part I opener and Chapter 1; no stray ink, header, footer, or artifact. |
| 31 | 7 | `page-031.png` | 239,311 | `b3f20e409b229f7585c5a6a0518b93840d45f7bc53733d31b1036a397b3c7740` | PASS | Chapter 1 opener, title, introductory paragraph, section 1.1, Definitions 1.1--1.3, displayed set notation, Warning 1.4, and centered footer are legible and unclipped. |
| 32 | 8 | `page-032.png` | 373,397 | `67e2c02714184662c593223e7435b9d559d8bf3a9433080a81b393a86090cd11` | PASS | Sections 1.2--1.3, ordered-pair displays, proof and QED mark, products, relations, and even-page running head and number are complete and aligned. |
| 33 | 9 | `page-033.png` | 321,088 | `ac0207affe540ef9535920a1c3f98a511eeecb6b23f3294102e7afbdcaa8d67d` | PASS | Function and quotient definitions, compact three-item list, inverse-image notation, quotient displays, Method 1.16, odd-page running head, and number render cleanly. |
| 34 | 10 | `page-034.png` | 391,676 | `737defcabfa7393364dc884f5727d7279a25bcb0d8a5349e83a0834341d3cf06` | PASS | Section 1.5, cardinal definitions, piecewise map, Cantor proofs, arrows, braces, proof squares, running head, and margins are intact. |
| 35 | 11 | `page-035.png` | 375,745 | `88465678e104aaa0039062ee05642a304ef5bc3cca9e72b17663abeb37c8fcf6` | PASS | Ordinal/cardinal material, recursion display, status lines, `[Jec03]` citation, section 1.6, theorem hierarchy, running head, and page number are legible. |
| 36 | 12 | `page-036.png` | 474,652 | `2af9875ff3973087b4596edd1ffe6f64ba36ebdb537d762f611f4171148841d8` | PASS | Cardinal notation, four-item and two-item lists, proof, aleph and union glyphs, citations, QED mark, even-page head, and the continued final paragraph fit without collision. |
| 37 | 13 | `page-037.png` | 368,091 | `17cb936b96d36adb3a47e966bdd9a3523f3aeac07c1b87deddfbf41c811cb800` | PASS | Chapter 1 continuation and close, Ultrafilter Lemma displays, Exercises 1.31--1.33, dependency summary, running head, and number are complete. |
| 38 | -- | `page-038.png` | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS | Intentional blank verso between Chapters 1 and 2; no stray ink, header, footer, or artifact. |
| 39 | 15 | `page-039.png` | 269,153 | `6d2bdb145c775287c65bcd010a938aa61d846c81001c4ef6581fadb9e8f508c4` | PASS | Chapter 2 opener, full title, section 2.1, Definitions 2.1--2.4, ordered-triple display, and centered footer render correctly. |
| 40 | 16 | `page-040.png` | 413,115 | `f37a40ddd76f3057dbf31c487c8e57dcffde0273028bb41dc6dde15f6316bfb5` | PASS | Example 2.5, section 2.2, Definitions 2.6--2.7, `[Tar83]`, logical and Greek glyphs, display, running head, and continued bottom line are intact. |
| 41 | 17 | `page-041.png` | 361,380 | `42bc3cbc765eedfcbd3fae40ea55dc6d056fa36f64ccb3d1848a15a639fa8557` | **FAIL** | One visible unresolved placeholder occurs in "the grammar of `??`". Warning 2.9, section 2.3, semantic-consequence and derivability displays, running head, number, and margins otherwise render correctly. |
| 42 | 18 | `page-042.png` | 378,604 | `4e9d27e792b61c9431ed3e0ea2419b22f490cdad8aa28369ff92d89ec26b3d05` | **FAIL** | Two visible unresolved placeholders occur in "definitions in `??` and `??`". Soundness/completeness displays, Warning 2.18, section 2.4, model display, running head, number, and margins otherwise render correctly. |
| 43 | 19 | `page-043.png` | 379,829 | `29186bc38c434ab4b3ee875aa8d161664ec2cc9138fd68a15035946bc5d46673` | PASS | Section 2.5, argument and countermodel definitions, compact seven-item method list, logical glyphs, running head, and number are legible and aligned. |
| 44 | 20 | `page-044.png` | 173,232 | `e636c61e45f52fe1cbcc3efea585d369348128e222b7a88ba5015090da164a49` | PASS | Quantifier-order displays and Exercises 2.26--2.27 close Chapter 2 cleanly; the even-page head and intentional lower-page whitespace are correct. |
| 45 | 21 | `page-045.png` | 214,956 | `71895597c38b1d04fd2e58be540a30aa6361f9e0790c9a200d0329d5050c236b` | PASS | Chapter 3 opener, full title, section 3.1, Definitions 3.1--3.2, string and numerical-pairing displays, interval notation, and centered footer are intact. |
| 46 | 22 | `page-046.png` | 367,052 | `7182712aec04b2e6fdfef4e9fd23e8867955bb3ee20a9aaa2464de0af6636138` | PASS | Pairing proof, Lemma 3.3, Corollary 3.4, concatenation cases, Lemma 3.5, restrictions, cases, proof squares, running head, and number render correctly. |
| 47 | 23 | `page-047.png` | 429,659 | `59a84d4ab8586c598d6965f998ec692a6d447a0bd834401e9901fa5878df770e` | PASS | Lemma 3.5 closes; section 3.2, Definition 3.6, Theorem 3.7 and its compact list, proof, and Warning 3.8 begin without clipping or spacing defects. |
| 48 | 24 | `page-048.png` | 398,638 | `b5efbc1595fceed8621cafadae041ef02ec23d64ab5a821c81dd67e5866c8a2d` | PASS | Warning 3.8 continues correctly; section 3.3, Theorem 3.9 and list, recursion displays, proof, Example 3.10, glyphs, running head, and number are intact. |
| 49 | 25 | `page-049.png` | 390,097 | `85335016e5d564e98b8804cb95718fa60a000d63d070b816d360e4d226164af0` | PASS | Sections 3.4--3.5, Method 3.11 and four-item list, Definition 3.12, Lemma 3.13, status line, path notation, running head, and page number render cleanly. |
| 50 | 26 | `page-050.png` | 259,907 | `4b87dcdb8bfebacf7c5cca2082a35acc9ffcc29ec728a4ba96657de4ff0683d5` | PASS | Lemma 3.13 closes; Definition 3.14 and Exercises 3.15--3.16 complete Chapter 3 with correct spacing, QED mark, head, number, and intentional whitespace. |
| 51 | 27 | `page-051.png` | 210,204 | `ca8d7d076d20b27eac247c44eae20bdd2cc9ad9af5128e8c8bec45539f969378` | PASS | Chapter 4 opener, title, section 4.1, compact nine-item list, section 4.2, Method 4.1 list start, and centered footer are balanced and unclipped. |
| 52 | 28 | `page-052.png` | 356,198 | `927df1fd4e1676e869cc93b84d65e4079843bfc28d6951e3d8b746f226e5130c` | PASS | Method 4.1 list continues, Example 4.2 display, Warning 4.3, section 4.3, bullet list, Method 4.4 list start, running head, and number are intact. |
| 53 | 29 | `page-053.png` | 307,814 | `968402dd9fed804d962ba51d0dc4c7a8aea40fe7f08270062acc1d99e57f2f6b` | PASS | Method 4.4 list continues; sections 4.4.1--4.4.5, implication and bottom glyphs, hierarchy, prose, running head, and page number render consistently. |
| 54 | 30 | `page-054.png` | 342,663 | `bb0005f5e3e588c98f7407eb1914af8ff86f43b88eee6c3f0e706f2d40de86f7` | **FAIL** | One visible unresolved placeholder occurs in "that calculus is defined in `??`". The aligned equivalence display, citations, inference-rule fraction, rule name, side condition, headings, head, and number otherwise render correctly. |
| 55 | 31 | `page-055.png` | 303,231 | `4ff9827f862c117e0d97ffb2d5f0f1a2d0f6dbe19f14d2ee981d22da0598c589` | PASS | Section 4.7 longtable is sharp, within margins, and internally aligned; all nine body rows, header rules, wrapped cells, continuation into Exercise 4.5, running head, and number are intact. |
| 56 | 32 | `page-056.png` | 117,720 | `9e2f2b0e1b9b20e4099e80b287dd34ca859f88bac46d6d305fe2d394619212af` | **FAIL** | One visible unresolved placeholder occurs in Exercise 4.6 at "completeness used in `??`". Exercise 4.5 continues correctly from page 55; page head, number, margins, and intentional Part I closing whitespace otherwise render correctly. |

## Visible failure localization

The five visible placeholders are the five currently pending inherited forward
references. Read-only localization gives the following exact origins and
targets; this mapping explains the printed defects but is not a source or
provenance verdict:

| Physical page | Visible count | Restoration origin | Pending target |
|---:|---:|---|---|
| 41 | 1 | `handbook/restoration/inherited-00853-00906.tex:39` | `ch:prop-syntax-semantics` |
| 42 | 2 | `handbook/restoration/inherited-00985-01023.tex:6` | `ch:fol-syntax-semantics`, `ch:fol-semantics` |
| 54 | 1 | `handbook/restoration/inherited-01580-01591.tex:11` | `ch:fol-deduction` |
| 56 | 1 | `handbook/restoration/inherited-01632-01648.tex:14` | `ch:fol-theories` |

Because `??` is visible reader-facing output, the four affected pages and the
overall bounded Part I visual gate fail even though the references are already
classified as pending by separate static controls.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No ink crosses a text block, trim, header, footer, table boundary, or page edge; no line or display is cut off. |
| Part and chapter boundaries | PASS | Part I appears once on physical 29; Chapters 1--4 begin on 31, 39, 45, and 51; blank versos 30 and 38 are intentional; Part I content ends on 56 before the outlined Part II start on 57. |
| Running heads and page numbers | PASS | Chapter openers use centered footer numbers; even pages use chapter heads; odd body pages use section heads; printed pages 5 and 7--32 are positioned and ordered consistently. |
| Equations and inference-rule display | PASS | Fractions, cases, aligned equalities, quantifiers, consequence and derivability signs, subscripts, superscripts, QED squares, the named rule, and its side condition are legible and unclipped. |
| Lists | PASS | Arabic lists and the bullet list use consistent indentation, continuation alignment, spacing, and safe margins across page breaks. |
| Longtable | PASS | The section 4.7 error-taxonomy table on physical 55 has intact rules, aligned columns, readable wrapped cells, and no overlap or clipping. |
| Mathematical glyphs and fonts | PASS | Set, relation, function, cardinal, ordinal, logical, Greek, restriction, aleph, arrow, brace, union, product, quotation, and proof-end glyphs are sharp and internally consistent. |
| Citations | PASS | `[Jec03]`, `[Tar83]`, `[Hal70; KLR89]`, and `[Amea]` are reader-visible and legible. |
| Reference rendering | **FAIL** | Five literal `??` placeholders remain visible on physical pages 41, 42, 54, and 56. |
| Cross-page continuity | PASS | Every sentence, proof, list, warning, table/exercise transition, and chapter boundary continues or closes coherently across physical pages 29--56. |

## Cross-page continuity ledger

- Physical 29 is followed by intentional blank verso 30; Chapter 1 begins on
  31.
- Physical 35 closes Corollary 1.27; physical 36 supplies the following
  citation and cardinal conventions. Physical 36 ends mid-paragraph and 37
  resumes it before closing Chapter 1.
- Physical 37 is followed by intentional blank verso 38; Chapter 2 begins on
  39.
- Physical 40 ends inside Example 2.8; physical 41 resumes its quoted-formula
  explanation. Physical 41 ends with the derivability display; physical 42
  begins its defining `iff` clause. Physical 42 ends with the model display;
  physical 43 begins by expanding that display.
- Physical 44 closes Chapter 2; Chapter 3 begins on 45.
- Physical 45 ends with the inverse pairing display; physical 46 begins with
  its upper-inequality consequence. Physical 46 ends after enumerating the
  associativity-proof intervals; physical 47 begins the first case. Physical
  47 ends inside Warning 3.8; physical 48 begins "in force" and completes it.
  Physical 49 ends in the path-concatenation proof; physical 50 resumes and
  closes the proof before ending Chapter 3.
- Physical 51 begins Chapter 4 and ends after item 2 of Method 4.1; physical 52
  resumes at item 3. Physical 52 ends after item 2 of Method 4.4; physical 53
  resumes at item 3. Physical 53 ends inside section 4.4.5; physical 54 resumes
  its construction paragraph.
- Physical 55 ends Exercise 4.5 at the hyphenated `cal-`; physical 56 begins
  `culus` and continues the exercise before Exercise 4.6 closes Part I.

## Scope limits

This record is bounded visual evidence only for physical pages 29--56 of the
exact corrected PDF hash above. It does **not** establish source-byte equality,
source provenance, source/static restoration gates, mathematical correctness,
AI content review, a clean or complete build, whole-book visual correctness,
admission or promotion, or human/user review. No independent gate is promoted
by this record.
