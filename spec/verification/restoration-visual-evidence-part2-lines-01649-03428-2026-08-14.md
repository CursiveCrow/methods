# Restoration visual evidence for Part II source lines 01649--03428 - 2026-08-14

## Bounded verdict

**FAIL for the bounded rendered-page visual gate.** Exact restored source lines
1649--3428 map to physical PDF pages 59--101 inclusive. Every page in that
43-page envelope was freshly rendered at fixed 200 dpi from the pinned PDF and
inspected exactly once at original render resolution. The envelope result is
42 PASS and 1 FAIL. Physical page 73 fails because the forward reference to
`ch:intuitionistic-logic` visibly prints as `??`.

The envelope deliberately includes three intentional blank versos (physical
60, 70, and 94) and eight separately attributed editorial interstitial pages
(physical 76--78 and 88--92). Those pages were inspected to establish the
complete route and its boundaries, but they receive no restored-source credit.
Physical page 75 is a shared exact/editorial boundary. Physical pages 82, 84,
86, 95, 96, and 97 are shared boundaries between exact restoration scopes.

Thirteen additional pages outside the main envelope were freshly rendered and
inspected exactly once for route reconciliation, TOC placement, remaining
visible placeholders, the trailing blank boundary, and changed proof-annex
consumers: physical pages 13, 14, 41, 42, 54, 56, 102--107, and 665. Their
result is 10 PASS and 3 FAIL. Physical pages 42, 54, and 56 fail for visible
`??` references to `ch:fol-semantics`, `ch:fol-deduction`, and
`ch:fol-theories`, respectively.

Across all 56 freshly inspected pages, the result is therefore **52 PASS and
4 FAIL**. No clipping, overlap, margin collision, malformed heading, broken
continuation, missing mathematical glyph, formula collision, malformed rule or
proof display, broken list, unintended blank, running-head defect, page-number
defect, or route-reconciliation defect was found. The otherwise-correct layout
does not override the four visible-reference failures.

The earlier `ch:fol-syntax-semantics` placeholder is gone. Its early consumer
now visibly resolves to Chapter 8; the same sentence retains only the separate
later-source `ch:fol-semantics` placeholder. The new *Classical First-Order
Logic* presentation is visibly subordinate within Part II, and the next public
part remains `III Model Theory` in the TOC.

This verdict is visual evidence only. It does not establish source fidelity,
mathematical correctness, source/static validation, build approval, AI review,
admission, human review, user acceptance, or terminal readiness.

## Frozen checkpoint and render parameters

- PDF: `handbook/main.pdf`
- PDF title metadata: `The Methods of Reason`
- PDF SHA-256:
  `6cf3fb470a09faec0a3d7ba9fbc4a87b94077d4ec499753b69157034ee50faac`
- File size: 4,291,888 bytes
- Physical page count: 799
- Default page geometry: US Letter, 612 x 792 points, rotation 0
- Physical page 78 geometry: US Letter, 612 x 792 points, rotation 90
- PDF version: 1.5
- Renderer: Poppler `pdftoppm` 26.05.0
- Render parameters: PNG, fixed 200 dpi
- Exact-source physical envelope: pages 59--101 inclusive
- Targeted outside-envelope pages: 13, 14, 41, 42, 54, 56, 102--107, 665
- Portrait render dimensions: 1700 x 2200 pixels
- Landscape render dimensions: 2200 x 1700 pixels for rotated physical 78
- Retained ignored render directory:
  `tmp/pdfs/part2-lines-01649-03428-6cf3fb47-2026-08-14/`

The PDF hash and byte count were checked before rendering, after inspection,
and at evidence freeze. They remained unchanged. The PDF was not rebuilt by
this audit. Earlier Part II page verdicts are historical evidence bound to
earlier PDF hashes; none was reused.

## Physical-page and source mapping

The current route, exact restoration endpoints, auxiliary labels, fresh text
extraction, rendered headings, and cross-page continuity establish this map:

| Exact source scope or interstitial | Physical PDF pages | Printed pages | Reader-facing placement |
|---|---:|---:|---|
| `SRC-01649-01660` | 59 | 35 | *Classical Propositional Logic* presentation, provenance, introduction |
| intentional blank | 60 | -- | blank verso before Chapter 5 |
| `SRC-01661-01816` | 61--63 | 37--39 | Chapter 5 opener and Section 5.1 |
| `SRC-01817-01898` | 64 | 40 | Section 5.2 |
| `SRC-01899-01945` | 65 | 41 | Section 5.3 |
| `SRC-01946-02186` | 65--69 | 41--45 | Section 5.4 through Chapter 5 close |
| intentional blank | 70 | -- | blank verso before Chapter 6 |
| `SRC-02187-02192` | 71 | 47 | Chapter 6 opener and Section 6.1 heading |
| `SRC-02193-02340` | 71--73 | 47--49 | classical natural deduction |
| `SRC-02341-02450` | 74--75 | 50--51 | classical sequent calculus; exact source closes on shared page 75 |
| editorial interstitial | 76--78 | 52--54 | Hilbert, tableau, and comparison supplement; page 78 landscape |
| `SRC-02451-02544` | 79--80 | 55--56 | Chapter 7 and Section 7.1 |
| `SRC-02545-02664` | 81--82 | 57--58 | Section 7.2 |
| `SRC-02665-02809` | 82--84 | 58--60 | Section 7.3 |
| `SRC-02810-02914` | 84--86 | 60--62 | Section 7.4 |
| `SRC-02915-02932` | 86 | 62 | Section 7.5 |
| `SRC-02933-03021` | 87 | 63 | Section 7.6 and all exercises |
| editorial interstitial | 88--92 | 64--68 | separately attributed propositional metatheory supplement |
| `SRC-03022-03037` | 93 and 95 | 69 and 71 | *Classical First-Order Logic* presentation and Chapter 8 opener |
| intentional blank | 94 | -- | blank verso before Chapter 8 |
| `SRC-03038-03104` | 95--96 | 71--72 | Section 8.1, signatures and terms |
| `SRC-03105-03165` | 96--97 | 72--73 | Section 8.2, formulas and unique readability |
| `SRC-03166-03239` | 97--98 | 73--74 | Section 8.3, free variables and sentences |
| `SRC-03240-03428` | 99--101 | 75--77 | Section 8.4, substitution and alpha-equivalence; source closes on 101 |

Physical page 102 is the intentional blank boundary before the separately
attributed Chapter 9 continuation on physical 103. It is not credited to exact
source lines 1649--3428, but it and pages 103--107 were inspected to establish
the reconciled downstream route.

## Exact 43-page main-envelope render ledger

`restored` identifies a page carrying exact inherited content; `blank`
identifies an intentional blank verso; `interstitial` identifies a separately
attributed editorial page inspected for the continuous envelope but receiving
no source credit. Each retained PNG was opened and visually inspected once.

| Physical | Printed | Scope | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 59 | 35 | restored | `restored-059.png` | 100059 | 1700x2200 | `908b4d9a248628e5377c954f810f126189abed398bc5fa3a70f42c1f471df6dc` | PASS |
| 60 | -- | blank | `restored-060.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 61 | 37 | restored | `restored-061.png` | 237008 | 1700x2200 | `10dada28aa1dec6424b1f94cca06bbab059d6ee05a58d762abe6a429e28fe101` | PASS |
| 62 | 38 | restored | `restored-062.png` | 379626 | 1700x2200 | `24c74e15b2678448166c0237ccbd70e74cba852e326259ca8685ca3c2526064d` | PASS |
| 63 | 39 | restored | `restored-063.png` | 410323 | 1700x2200 | `03c66bca695bf232428a82ded083726043944902f913ea5ee8a2ffbf3a9d4df0` | PASS |
| 64 | 40 | restored | `restored-064.png` | 334715 | 1700x2200 | `3169ea537f411e4e62e94460499ba3b4c23a1eb51aba1b189d6097708512c285` | PASS |
| 65 | 41 | restored | `restored-065.png` | 342259 | 1700x2200 | `0a001a64b80336f974c6aad3c40ee22fc93e3a698567ffa93d9676bb41a717da` | PASS |
| 66 | 42 | restored | `restored-066.png` | 364829 | 1700x2200 | `8f720cc77c8eb57017d63558a25e7e0d4649b77da7cc4170bc17da4a7f26cc91` | PASS |
| 67 | 43 | restored | `restored-067.png` | 423083 | 1700x2200 | `15edda8688df006ec3251b07ff5c64ae7b4dd974a965bf26ec82527b192e4a27` | PASS |
| 68 | 44 | restored | `restored-068.png` | 432399 | 1700x2200 | `333ace3b6bfe1e9491f0469cbd9c4a8e5aed7168f4bdf559735c822051d8adf6` | PASS |
| 69 | 45 | restored | `restored-069.png` | 309884 | 1700x2200 | `23a47c6762fa1af8143fa10634fe98f4cbdd87399ea70f571cd74310ec40ab42` | PASS |
| 70 | -- | blank | `restored-070.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 71 | 47 | restored | `restored-071.png` | 311217 | 1700x2200 | `f7a06ccf896b5be12f31b82e4d372c7eb579c2b41f67d35ecb0627b7ebf9c7f2` | PASS |
| 72 | 48 | restored | `restored-072.png` | 232893 | 1700x2200 | `e8faaa6e29008a518bcd25ddaee82648cbaf624346efeb993d3a433b01b5a318` | PASS |
| 73 | 49 | restored | `restored-073.png` | 352970 | 1700x2200 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | **FAIL** |
| 74 | 50 | restored | `restored-074.png` | 318859 | 1700x2200 | `4aaec2ae7a884fe43c902d12f557b7d87131ba0d6d20b81f0c03fa75470a4cc8` | PASS |
| 75 | 51 | restored/shared | `restored-075.png` | 356963 | 1700x2200 | `7c4d22112f01e37a3539d5ea4576535aec0333c1e516bdf1f1a3216d352ef4a4` | PASS |
| 76 | 52 | interstitial | `restored-076.png` | 353741 | 1700x2200 | `4b4867f54922944f80f78e1913c84e53d3e105685743717a79f2034c9563a611` | PASS |
| 77 | 53 | interstitial | `restored-077.png` | 291808 | 1700x2200 | `7a7d26678440d38eca50d7755d63db49878dfcf1a0e52a46c000c9fb96144144` | PASS |
| 78 | 54 | interstitial | `restored-078.png` | 215759 | 2200x1700 | `20a9c801faabf422e169e1904658420077ef61b3c4c57aaee10a0949eaa9b9fd` | PASS |
| 79 | 55 | restored | `restored-079.png` | 269924 | 1700x2200 | `b348fc3937faf5bd692f9536440a01ecda6290edf9e4ac8e5da04fe096df36ed` | PASS |
| 80 | 56 | restored | `restored-080.png` | 422110 | 1700x2200 | `61979c081ea2eead2c7f0f4c44893d10e0f278938076fa3c00499f13aee55fdc` | PASS |
| 81 | 57 | restored | `restored-081.png` | 412827 | 1700x2200 | `30c744ca21d9b125a85c335bfc7bba9c32cda9d2b13448b3fb71a097d8b1fb1f` | PASS |
| 82 | 58 | restored/shared | `restored-082.png` | 350388 | 1700x2200 | `400b267914ef7b8e42c08418346c0cd215a3c22dc4660dbd3af5b349e4eac54c` | PASS |
| 83 | 59 | restored | `restored-083.png` | 423026 | 1700x2200 | `96f755a470823e65d1f235e288fd374944bc06b5149a30b6935de294b766848d` | PASS |
| 84 | 60 | restored/shared | `restored-084.png` | 387393 | 1700x2200 | `e748a5d0b55f56c8ea60e019473593607430a15edf70d5f2665d3ca9bf992d43` | PASS |
| 85 | 61 | restored | `restored-085.png` | 448975 | 1700x2200 | `b6c40e08a6ff8cf4dcfcf801b9484b18ef117f4bb181cc1965c2f5872cb12abe` | PASS |
| 86 | 62 | restored/shared | `restored-086.png` | 414571 | 1700x2200 | `73fed777c4d235cae3d670cc387f5026b354e3e78d17f7d00c5c7bff9befccd9` | PASS |
| 87 | 63 | restored | `restored-087.png` | 388344 | 1700x2200 | `4e7bc835c97c922ff15beb7270c7afb67da401483f1f2b394144507082ba0a27` | PASS |
| 88 | 64 | interstitial | `restored-088.png` | 411278 | 1700x2200 | `82a8fdb70aa7290155ae0812bfbc13bd31ef1b54b43124b594211babe99ec7a9` | PASS |
| 89 | 65 | interstitial | `restored-089.png` | 312304 | 1700x2200 | `31c92c7424cdabb37657f983e20c73ae4a84310f1933c9fa7c08bfe50f853454` | PASS |
| 90 | 66 | interstitial | `restored-090.png` | 461796 | 1700x2200 | `46e56c3820415faae0b72f8112494c5df8101c4ff794003fbf26a17cd4689ef7` | PASS |
| 91 | 67 | interstitial | `restored-091.png` | 484321 | 1700x2200 | `01bbdb77e2fcf393c8e21538f4f2feaf05aecd97476d8695cad8dad37994d2df` | PASS |
| 92 | 68 | interstitial | `restored-092.png` | 129371 | 1700x2200 | `05533090d041a56c1e6262dab1788b4a5e0f9d31df2b4476930693a519adc178` | PASS |
| 93 | 69 | restored | `restored-093.png` | 113176 | 1700x2200 | `a1e1e7ba76645ddd59bb3b623f95e4e532ec311f7bde6fecf5e609e78a2bc895` | PASS |
| 94 | -- | blank | `restored-094.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 95 | 71 | restored/shared | `restored-095.png` | 221438 | 1700x2200 | `2996c4b30ad86bd8f0cf219c6646121b016cf319f87bc229326fd6424cbf8c03` | PASS |
| 96 | 72 | restored/shared | `restored-096.png` | 363508 | 1700x2200 | `ec820e2c75316a75c89282d8b96428184b33fcb81d11e01ef84a56c5d3ad6bda` | PASS |
| 97 | 73 | restored/shared | `restored-097.png` | 367442 | 1700x2200 | `0d59ba6a68b89c7dbda0da52aaa747f1b5829acf62b59358d65aa9095f4cf9ab` | PASS |
| 98 | 74 | restored | `restored-098.png` | 286098 | 1700x2200 | `27f8891795854d62ca880ecd9c7054b4bab0be5e56d58c1de635708c3ed51c52` | PASS |
| 99 | 75 | restored | `restored-099.png` | 323600 | 1700x2200 | `d47c9d741ce96c2dae5b79207d616c021683725092c5575c23f8169c38524b38` | PASS |
| 100 | 76 | restored | `restored-100.png` | 405717 | 1700x2200 | `0f497bbd834233aa267bdd4d2f503a3dd6eb7ac471bb4f6a1508618b5e24fb17` | PASS |
| 101 | 77 | restored | `restored-101.png` | 490110 | 1700x2200 | `9e412d4381001caed1538933c568acdbcdec55dced5f984a26fb2647194efde8` | PASS |

## Exact 13-page targeted render ledger

These pages are outside the exact-source envelope. They were inspected only
for the named route, TOC, reference, blank-boundary, continuation, or annex
consumer question and receive no restored-source credit.

| Physical | Printed | Target | 200-dpi render | PNG bytes | Pixels | PNG SHA-256 | Result |
|---:|---:|---|---|---:|---:|---|---|
| 13 | ix | TOC placement | `toc-013.png` | 309387 | 1700x2200 | `5cc3ee175355d39ada693eb597e56ee9996d2bd1ed8713984475afcbc1974182` | PASS |
| 14 | x | TOC public-part boundary | `toc-014.png` | 338519 | 1700x2200 | `47176677734bdf20029b1eabe66448c85aef8ab2df98af04016c96d215db2356` | PASS |
| 41 | 17 | early syntax consumer | `earlyref-041.png` | 362651 | 1700x2200 | `419f23fa4317301e6d13705dd1fea60d126bc6159cf356ac145ee110c28edb98` | PASS |
| 42 | 18 | syntax/semantics consumers | `earlyref-042.png` | 381182 | 1700x2200 | `81c1e64ea92bff49659ad94983b17a74308524cb66acc1b129d6ef1bcd6c89e6` | **FAIL** |
| 54 | 30 | deduction consumer | `unresolved-054.png` | 342663 | 1700x2200 | `bb0005f5e3e588c98f7407eb1914af8ff86f43b88eee6c3f0e706f2d40de86f7` | **FAIL** |
| 56 | 32 | theories consumer | `unresolved-056.png` | 117720 | 1700x2200 | `9e2f2b0e1b9b20e4099e80b287dd34ca859f88bac46d6d305fe2d394619212af` | **FAIL** |
| 102 | -- | trailing blank boundary | `reconciled-102.png` | 15924 | 1700x2200 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS |
| 103 | 79 | reconciled continuation opener | `reconciled-103.png` | 269868 | 1700x2200 | `5310f81eb5b5022b797a51a609c17db97d1014cc75c3bcb8220a532dfa3dac31` | PASS |
| 104 | 80 | reconciled continuation | `reconciled-104.png` | 275474 | 1700x2200 | `ef40848218d91b56f261df4d68d487a8bbda4f9cec99d30de6cb4dbfe959213e` | PASS |
| 105 | 81 | reconciled continuation | `reconciled-105.png` | 328304 | 1700x2200 | `56e71af3465f14c99ac8383b22f82de9eec02fbfe2efca5cbab09fbf8416b917` | PASS |
| 106 | 82 | reconciled continuation | `reconciled-106.png` | 358062 | 1700x2200 | `ffa8d3e5670e4af4ada80ec28369d157594a1570bec468ae98c47f920d06ab1c` | PASS |
| 107 | 83 | reconciled continuation | `reconciled-107.png` | 359252 | 1700x2200 | `e94900fea44de05c7a766c038e71c57cd61c37b678db4d4f435ea698418b719d` | PASS |
| 665 | 641 | changed annex consumers | `annex-665.png` | 396447 | 1700x2200 | `39acca34b5ffe7cf77c236e756a3614fab071db43afdd9abd9b101825b154dfb` | PASS |

## Page-specific visual findings

### New first-order source presentation and Chapter 8

- Physical 93 cleanly presents *Classical First-Order Logic*, the inherited
  provenance line for source line 3022, the introductory paragraph, citations,
  centered page number, and generous margins. It has no public Roman part
  number and does not masquerade as Part III.
- Physical 94 is an intentional blank verso with no stray ink, header, footer,
  or page number.
- Physical 95 cleanly opens Chapter 8, *First-Order Syntax*. The chapter title,
  textbook citations, Section 8.1, signature tuple, arity maps, token set, and
  local definitional `:=` notation are sharp and unclipped.
- Physical 96 preserves the syntactic/semantic warning, term grammar, examples,
  formula grammar, complete six-item formation list, quantifier scope, and all
  function, relation, equality, bottom, connective, and quantifier glyphs.
- Physical 97 contains the complete unique-readability theorem and proof,
  Section 8.3, the sans-serif/roman variable distinction, and the start of the
  free-variable definition without collision or truncation.
- Physical 98 cleanly completes the free-variable recursion, sentence and
  complexity definitions, set-level `FV` extension, occurrence discussion, and
  bound/free example.
- Physical 99 cleanly begins capture-avoiding substitution. The term clauses,
  three-case quantified formula display, braces, freshness side conditions,
  recursion explanation, and complexity lemma remain aligned and legible.
- Physical 100 cleanly closes the complexity proof and presents
  alpha-equivalence as `equiv` with an `alpha` subscript, its generating
  renaming clause, capture-avoidance example, free-variable lemma, and proof
  opening. The alpha-equivalence glyph is neither missing nor confused with
  literal equality or the local definitional sign.
- Physical 101 preserves both proof continuations, quantified cases, subscripts,
  substitutions, set differences, induction references, proof squares, running
  head, page number, and exact source endpoint without clipping.

### Earlier exact material and editorial interstitials

- Physical 59--75 preserve presentation and chapter openers, continuations,
  formula arrays, truth and controlled-prose tables, proof trees, sequent
  rules, Cut, examples, warnings, and proof closures. Physical 73 alone fails
  for the visible reference placeholder; its derivation and all other layout
  features pass.
- Physical 76--78 preserve the separately attributed Hilbert, tableau, and
  proof-system comparison interstitial. The rotated landscape page 78 renders
  at 2200 x 1700 with complete table rules, all five rows, rotated header, and
  page number inside the page.
- Physical 79--87 preserve Chapter 7 formulas, proofs, numbered construction,
  resolution argument, warnings, and all twelve exercises with intact running
  heads, page numbers, margins, and continuations.
- Physical 88--92 preserve the separately attributed propositional metatheory
  supplement, including the boxed owed-artifact notice, interpolation material,
  resolution DAG, complexity statements, and final tractable-class table.

### Route reconciliation and consumers

- TOC physical 13 places *Classical First-Order Logic* immediately before
  Chapter 8 and lists Sections 8.1--8.4. It is subordinate to the existing
  Part II sequence rather than a new public part. TOC physical 14 retains
  `III Model Theory` as the next public part.
- The built bookmark data independently records *Classical First-Order Logic*
  (`section*.29`) and *First-Order Syntax* (`chapter.8`) as level-0 children of
  `part.2`; later `part.3` remains the public `III Model Theory` bookmark. This
  bookmark statement is an auxiliary structural check, not a rendered-page
  verdict.
- The early combined consumer on physical 42 now reads `chapter 8 and ??`.
  Thus `ch:fol-syntax-semantics` visibly resolves to Chapter 8; only the
  independent `ch:fol-semantics` target remains unresolved.
- Physical 102 is an intentional blank boundary. Physical 103 cleanly opens
  the separately attributed *First-Order Semantics and Remaining Editorial
  Material* continuation, and physical 104--107 preserve its formulas, proofs,
  examples, theory definitions, and table without visible placeholder or route
  collision.
- Physical 665 cleanly renders the changed first-order natural-deduction and
  sequent-calculus annex consumers. Their repaired propositional soundness
  references print as Theorem 7.1 and Theorem 7.2, not as `??`.

## Visible failure localization

A page-by-page text extraction scan of all 799 physical pages found literal
`??` on exactly four pages. All four were then inspected in their fresh 200-dpi
renders. This table localizes the visible defects without claiming source,
static, build, AI, or admission status.

| Physical page | Visible count | Reader-facing phrase | Pending target |
|---:|---:|---|---|
| 42 | 1 | `chapter 8 and ??` | `ch:fol-semantics` |
| 54 | 1 | `defined in ??` | `ch:fol-deduction` |
| 56 | 1 | `used in ??` | `ch:fol-theories` |
| 73 | 1 | `made exact in ??` | `ch:intuitionistic-logic` |

The first half of the phrase on physical 42 confirms the requested repair:
the former `ch:fol-syntax-semantics` placeholder now renders as `chapter 8`.
The four surviving placeholders are reader-visible defects and therefore keep
their pages and the overall bounded visual gate open even though their targets
belong to later restoration work.

## Interval-wide visual checks

| Check | Result | Evidence observed |
|---|---|---|
| Clipping and margins | PASS | No text, formula, proof square, rule, table, figure, heading, header, footer, or page number is cut off or crosses the page edge. |
| Source presentations and chapter boundaries | PASS | Presentations occur on 59 and 93; Chapters 5, 6, 7, and 8 begin on 61, 71, 79, and 95; blanks 60, 70, and 94 correctly preserve recto openings. |
| New subordinate placement | PASS | Page 93, TOC 13--14, and the auxiliary bookmark hierarchy preserve the single public Part II route and leave Part III as Model Theory. |
| Headings, running heads, and page numbers | PASS | Printed pages 35--77 are ordered and positioned consistently; long even-page heads remain legible and inside margins; centered opener footers are intact. |
| Formulas and local notation | PASS | Definitional `:=`, equality, semantic consequence, derivability, substitution, assignment update, quantifiers, set operations, and alpha-equivalence render distinctly and consistently. |
| Proof and rule displays | PASS | Natural-deduction rules, sequent rules, Cut displays, derivation trees, proof squares, cases, and freshness side conditions remain aligned and reader-traceable. |
| Lists, exercises, tables, and figures | PASS | Formation lists, warnings, exercises, truth tables, comparison tables, resolution DAG, and axiomatization table are complete, ordered, and unclipped. |
| Continuations | PASS | Every inspected page break resumes the preceding sentence, definition, theorem, proof, list, or display coherently; no source endpoint is silently truncated or duplicated. |
| Fonts and glyphs | PASS | Roman, italic, bold, small-cap, Greek, blackboard-bold, calligraphic, logical, substitution, assignment, proof-theoretic, and alpha-equivalence glyphs show no missing-glyph box or visible substitution. |
| Intentional blanks | PASS | Physical 60, 70, 94, and targeted boundary 102 are wholly blank with no stray mark. |
| Route-reconciled consumers | PASS | The early syntax consumer resolves to Chapter 8; continuation 103--107 and annex consumer 665 render cleanly. |
| Visible references | **FAIL** | Literal `??` remains on physical pages 42, 54, 56, and 73 at the four later-source labels listed above. |

## Coverage and integrity checks

- Main-envelope expected set: every integer physical page 59--101, count 43.
- Main-envelope render set: exactly one `restored-NNN.png` for each expected
  page, with no missing, duplicate, or unknown page, count 43.
- Targeted expected set: 13, 14, 41, 42, 54, 56, 102, 103, 104, 105, 106,
  107, and 665, count 13.
- Targeted render set: exactly one retained PNG for each expected target, with
  no missing, duplicate, or unknown page, count 13.
- Total inspected render set: 56 distinct physical pages, each inspected once;
  52 PASS and 4 FAIL.
- Every PNG byte count, pixel dimension, and SHA-256 digest is recorded in the
  two ledgers above. All are 1700 x 2200 except the intentional 90-degree
  landscape physical page 78 at 2200 x 1700.
- Repeated byte/digest identity among the blank renders is expected: pages 60,
  70, 94, and 102 are the same wholly blank 200-dpi raster.
- The report is UTF-8 without BOM and uses LF line endings only.
- The retained render directory contains only the 56 governed PNGs after
  scratch extraction files were removed.
- Repository-wide `git diff --check` and the report-specific no-index
  whitespace check were run at freeze; neither reported a whitespace error.
- The canonical PDF identity at freeze remained 799 pages, 4,291,888 bytes,
  title `The Methods of Reason`, SHA-256
  `6cf3fb470a09faec0a3d7ba9fbc4a87b94077d4ec499753b69157034ee50faac`.

## Claim boundary

This report supports only the following bounded claim: for the pinned PDF,
every physical page in the exact source-line 1649--3428 envelope and every
listed route-reconciliation target was freshly rendered at 200 dpi, inspected
once, hash-ledgered, and assigned the visual verdict recorded above. Four
reader-visible unresolved references keep the visual gate at FAIL.

It does not promote any source unit, packet, register record, semantic row,
topic, section, AI review, build result, human review, admission decision,
user acceptance, or release-readiness claim.
