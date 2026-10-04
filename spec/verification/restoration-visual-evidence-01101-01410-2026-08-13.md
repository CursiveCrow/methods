# Restoration visual evidence for source lines 01101--01410 -- 2026-08-13

## Bounded verdict

**PASS for the bounded rendered-page visual gate.** Every physical PDF page
containing the restored Chapter 3 source interval 01101--01410 was rendered at
fixed 200 dpi and inspected at the original 1700 x 2200 pixel resolution. No
visible clipping, margin collision, missing or substituted glyph, broken
formula, malformed list, environment-layout defect, heading or label defect,
running-head defect, page-number defect, or cross-page continuity defect was
found on the six in-scope pages.

This verdict is bound to the exact PDF below. It is visual evidence only; the
scope limitations and the three still-pending references are stated at the end
of this record.

## Inspected PDF and render parameters

- PDF: `handbook/main.pdf`
- SHA-256:
  `df510759d39b4898572e13cb577c724f8358eee2e4f504fc336a3a276316c3e5`
- File size: 4,609,648 bytes
- Physical page count: 876
- Page geometry: US Letter, 612 x 792 points, rotation 0
- Renderer: Poppler `pdftoppm` 25.02.0
- Render parameters: PNG, 200 dpi, physical pages 45--50 inclusive
- Render dimensions: 1700 x 2200 pixels for every page
- Retained render directory: `tmp/pdfs/restoration-01101-01410/`

The PDF hash and byte count were checked before rendering and checked again
after inspection. They remained unchanged.

## Physical-page localization

The physical page interval was not inferred from the printed number. Poppler
named-destination inspection locates `chapter.3` on physical page 45,
`section.3.1` on 45, `section.3.2` on 47, `section.3.3` on 48,
`section.3.4` and `section.3.5` on 49, both Chapter 3 source exercises on 50,
and `chapter.4` on physical page 51. The current `main.aux` independently gives
printed page 21 for Chapter 3, printed pages 21--25 for its sections, printed
page 26 for its two exercises, and printed page 27 for Chapter 4. Therefore the
complete and exact physical page interval for the restored chapter is 45--50.

## Exact source interval checked

The nine current inherited fragments for 01101--01410 were compared line by
line against `source/formal-logic-reference.tex` lines 1101--1410. Each fragment
had the expected line count and an exact case-sensitive line match:

| Source interval | Fragment lines | Exact line match |
|---|---:|---|
| 01101--01147 | 47 | PASS |
| 01148--01163 | 16 | PASS |
| 01164--01223 | 60 | PASS |
| 01224--01263 | 40 | PASS |
| 01264--01308 | 45 | PASS |
| 01309--01319 | 11 | PASS |
| 01320--01342 | 23 | PASS |
| 01343--01397 | 55 | PASS |
| 01398--01410 | 13 | PASS |

`handbook/parts/p01.tex` inputs the corresponding nine restoration scopes in
that order. This comparison establishes which exact current text was visually
checked; it is not a source-authenticity, provenance, or mathematical-review
verdict.

## Retained page ledger

This is the single retained page ledger. Each in-scope physical page occurs
exactly once.

| Physical PDF page | Printed page | Retained 200-dpi render | PNG bytes | PNG SHA-256 | Result | Page-specific inspection |
|---:|---:|---|---:|---|---|---|
| 45 | 21 | `physical-045.png` | 214,956 | `71895597c38b1d04fd2e58be540a30aa6361f9e0790c9a200d0329d5050c236b` | PASS | Chapter 3 opener, full title, section 3.1, Definitions 3.1--3.2, the `A* :=` display, numerical-pairing display, interval notation, and the first inverse display are legible and unclipped. The chapter-opener page has the expected centered footer number and no running head. |
| 46 | 22 | `physical-046.png` | 367,052 | `7182712aec04b2e6fdfef4e9fd23e8867955bb3ee20a9aaa2464de0af6636138` | PASS | The pairing argument continues correctly; Lemma 3.3 and its proof, Corollary 3.4 and its proof, the concatenation cases, Lemma 3.5, and the start of its proof are intact. `len`, the restriction glyph in `w ↾ n`, subscripts, superscripts, arrows, cases, proof squares, and the even-page chapter running head render correctly. |
| 47 | 23 | `physical-047.png` | 429,659 | `59a84d4ab8586c598d6965f998ec692a6d447a0bd834401e9901fa5878df770e` | PASS | The Lemma 3.5 proof continues and closes; section 3.2, Definition 3.6, Theorem 3.7 with its compact Arabic list and proof, and the start of Warning 3.8 are correctly laid out. `X := {x in G : P(x)}` is visibly scoped to the proof. The odd-page section running head and printed number are correct. |
| 48 | 24 | `physical-048.png` | 398,638 | `b5efbc1595fceed8621cafadae041ef02ec23d64ab5a821c81dd67e5866c8a2d` | PASS | Warning 3.8 continues without loss; section 3.3, Theorem 3.9 with its compact Arabic list and display, its proof and proof square, and Example 3.10 are intact. `Fm`, union/subscript notation, primes, negation, conjunction, and all recursion formulas render consistently. The even-page chapter running head and number are correct. |
| 49 | 25 | `physical-049.png` | 390,097 | `85335016e5d564e98b8804cb95718fa60a000d63d070b816d360e4d226164af0` | PASS | Sections 3.4 and 3.5, Method 3.11 with its compact four-item Arabic list, Definition 3.12, Lemma 3.13 including the visible status line, and the first part of its proof are legible, aligned, and unclipped. Relation stars, indexed paths, products, inclusions, and quantifier bounds render correctly. The odd-page section running head and number are correct. |
| 50 | 26 | `physical-050.png` | 259,907 | `4b87dcdb8bfebacf7c5cca2082a35acc9ffcc29ec728a4ba96657de4ff0683d5` | PASS | The Lemma 3.13 proof continues and closes; Definition 3.14, the closure comparison paragraph, and Exercises 3.15--3.16 are complete and consistently spaced. Exercise labels, proof square, relation notation, margins, even-page running head, and printed number are correct. The remaining lower-page whitespace is intentional. |

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No ink crosses the text block, trim, header, or footer boundary; no line or display is cut off. |
| Running heads and page numbers | PASS | Physical 45 uses the chapter-opener footer; physical 46, 48, and 50 use the even-page chapter head; physical 47 and 49 use the odd-page section head; printed pages 21--26 are present and consistent. |
| Critical source symbols | PASS | `\length` is visibly rendered as `len`; `\restr` is visibly rendered as the restriction bar `↾`; `\Fm` is rendered as `Fm`; and the three source `\defeq` sites render as `:=` at `A*`, `pair_N`, and the proof-local `X`. |
| Other mathematical glyphs | PASS | Natural-number glyphs, epsilon, braces, union, products, subsets, arrows, inequalities, stars, subscripts, primes, negation, conjunction, and hollow proof-end squares are present and consistent. The hollow squares are intentional QED marks, not missing-glyph boxes. |
| Compact lists | PASS | Theorem 3.7, Theorem 3.9, and Method 3.11 use Arabic numbering, compact `nosep` spacing, aligned continuation lines, and safe left and right margins. |
| Environments | PASS | Definition, lemma, corollary, theorem, proof, warning, example, method, and exercise labels and body styles remain distinguishable and internally consistent. |
| Headings and labels | PASS | Chapter and section numbers/titles are complete, correctly ordered, and typographically consistent; item numbering advances from 3.1 through 3.16 without a visible break. |
| Font consistency and legibility | PASS | Text, headings, theorem italics, roman definitions/proofs, operators, and mathematical alphabets are sharp and consistent at 200 dpi; no substituted or unreadable glyph was found. |

## Cross-page continuity

- Physical 45 ends with the inverse display `b = z - t_s, a = s - b`;
  physical 46 begins with the consequence of its upper inequality.
- Physical 46 ends after listing the three exhaustive index intervals in the
  associativity proof; physical 47 begins with the first interval case.
- Physical 47 ends inside Warning 3.8 after "the grammar actually"; physical
  48 begins "in force" and completes the warning before section 3.3.
- Physical 48 finishes Example 3.10; physical 49 begins section 3.4.
- Physical 49 ends in the path-concatenation proof after `u_0 = x`; physical
  50 begins with `u_{m+n} = z` and completes that proof.
- Physical 50 ends with Exercise 3.16. The independent destination check puts
  Chapter 4 on physical page 51, so no Chapter 3 page is omitted.

## Scope limits and still-pending references

This record is **bounded visual evidence only** for physical pages 45--50 of
the exact PDF hash above. It does **not** establish any source-authenticity or
full-source gate, AI mathematical/content-review gate, whole-book visual gate,
clean-build or compilation gate, or human/user-review gate. It must not be used
to promote any of those independent statuses.

The current build log still contains exactly these three pending undefined
references, followed by the aggregate "There were undefined references"
warning:

1. `ch:prop-syntax-semantics`
2. `ch:fol-syntax-semantics`
3. `ch:fol-semantics`

Those references remain pending and are not repaired or discharged by this
visual PASS.
