# Fresh rendered evidence for inherited source lines 07494-07850

Date: 2026-08-14  
Scope: the single settled Part IV candidate identified below; inherited source lines 07494-07850; the public-Part/subordinate-source-part route; the incoming and outgoing seams; the OPEN Machines supplement; affected body, annex, TOC, bookmark, and index consumers; and whole-PDF navigation integrity.  
Method boundary: fresh 200 dpi native-orientation raster inspection plus PDF-structure, source/static, AUX, and text-extraction checks. This report does not admit any source unit, close any OPEN register, establish mathematical correctness, or record human acceptance.

## Frozen candidate and separated verdicts

Candidate: `tmp/computability-7494-7850-settled-20260814-2030/p4-7494-7850-check.pdf`

| Property | Observed value | Result |
|---|---:|---|
| Title | `The Methods of Reason` | PASS |
| Physical pages | 803 | PASS |
| File size | 4,329,265 bytes | PASS |
| SHA-256 | `45339136d9697dd38dd85fa205dc4aad2ed8105710b04b6fa0c0e0f164f1c155` | PASS |
| Encryption | none | PASS |
| Media box | 612 x 792 pt on all 803 pages (US Letter) | PASS |
| Native page rotation | 763 pages at 0 degrees; 40 pages at 90 degrees | PASS |

**Exact restoration/static verdict: PASS.** The fail-closed checker passes all five records covering lines 07494-07850.

**Exact restoration/body visual verdict: PASS.** The source title on physical page 251, Chapter 23 and the complete exact print-bearing body on pages 253-259, its proof plans, equations, enumerated lists, exercise, both seams, and the OPEN supplement on pages 259-264 are legible and free of observed clipping, collision, overprint, damaged glyphs, bad folios, or broken running heads. The exact-source-to-OPEN handoff on page 259 is visibly explicit and clean.

**Part/counter/navigation verdict: PASS.** Public Part IV `Computability and Complexity` resolves to physical page 249; the non-counter-stepping subordinate source title `Computability` resolves to page 251; Chapter 23 resolves to page 253; and Chapter 24 follows on page 265. Part IV remains IV and the next public part remains V. All 3,612 named destinations, 4,040 internal named link annotations, and 396 outline entries resolve cleanly.

**Complete governed-surface visual verdict: FAIL.** One collision occurs on the required affected index surface, physical page 796 (printed index page 772): the left-column entry `Primitive, derived, and admissible rules,` overlaps the right-column entry `Proof theory, 17`, visibly producing `rulesProof`. This is outside the exact restored Chapter 23 body, and the affected Primitive-recursive entries immediately above it remain legible, but it fails the requested no-collision condition for the complete governed page set.

**Overall publication-facing verdict: OPEN.** Independent whole-PDF extraction passes find exactly one literal `??`, solely on physical page 73. The Machines supplement is also explicitly OPEN/unadmitted. Those conditions are independent of the clean exact-restoration/body tranche. The page-796 index collision additionally prevents a clean full-surface visual verdict. Human acceptance is not established.

## Fresh render protocol

- Candidate identity was checked before rendering; a mismatch would have stopped the audit.
- A new scratch directory, `tmp/visual-computability-7494-7850-20260814`, was created. No predecessor raster or verdict was reused.
- The complete governed physical-page set was 15-16, 23, 73, 248-265, 291, 312, 697, 783-785, 791, 795-797, and 802.
- Exactly 33 PNGs were rendered directly from the frozen candidate with Poppler at 200 dpi and individually inspected.
- Portrait renders are 1700 x 2200 pixels. Physical pages 262-263 are native landscape, 2200 x 1700 pixels.
- The tab-separated ledger `tmp/visual-computability-7494-7850-20260814/render-ledger.tsv` has 34 lines including its header, 2,885 bytes, and SHA-256 `4360ca45e48614fabb90429b771d482b108634a1d3c04fabead32431711e7441`.

## Per-page render and inspection ledger

| Physical page | Governed content | PNG bytes | PNG SHA-256 | Visual result |
|---:|---|---:|---|---|
| 15 | Body TOC: public Part IV, subordinate `Computability`, Chapter 23, exact sections, OPEN supplement | 306,594 | `77f9afa16b0dd5ceaef9efea430d4d46cf9279cef96d9faa102f08fe1a29460d` | PASS: hierarchy, leaders, page numbers, and wrapping are clean. |
| 16 | Body TOC continuation: Section 23.4, Chapter 24, and the remainder of Part IV | 335,432 | `7370e9377ee148d15e358830f38ffca821e3d703807ba778153a3ebbc3aa6d85` | PASS. |
| 23 | Annex TOC including P4 | 257,031 | `ca6147ae85d53eb6702e65a6de9ac9e33e3439cb34e1d8fe9a2a815c83091f9a` | PASS: hierarchy and wrapped annex titles are clean. |
| 73 | Sole global literal `??` | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | OPEN globally: placeholder visible; surrounding proof layout is clean. |
| 248 | Incoming seam: final page of Chapter 22 | 332,049 | `918b38de938396edc118707c33b6d957099e1f35f038fd112144708d0cfbab6c` | PASS. |
| 249 | Public Part IV title, `Computability and Complexity` | 42,551 | `6d2f8178881d705af331f7727b715279af11d95e2e38b2fdbff3fe83ba2ac3cb` | PASS: part counter, title, folio, and centering are clean. |
| 250 | Intentional blank interleaf | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS: genuinely blank and artifact-free. |
| 251 | Exact source title `Computability` and source-line 7494 attribution | 41,187 | `bbae3b1738d72a49e6a9e3084881f192c7ec6b18faaefa22f2123360e74c34ec` | PASS: visibly subordinate to public Part IV and noncolliding. |
| 252 | Intentional blank interleaf | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS. |
| 253 | Exact Chapter 23 opening, Section 23.1, and Turing-machine definition | 231,070 | `30f417ac9f0b5216c49cb493f9db87a1ee374ea9c08dcbf93fc46c7f1216e97e` | PASS: heading, tuple, display, and five-item list fit cleanly. |
| 254 | Exact configuration/computation definition and coding displays | 282,421 | `65ef8a4eb1aafbed45b10bf7b3190548257fe25dafd212757ecfaa7e0309798c` | PASS. |
| 255 | Exact tuple coding, output convention, and Definition 23.3 | 410,982 | `d48b71c55a968a6ad44806febb0f8616eca53c2549b376700748d205eda3178f` | PASS: long displays and partial-function notation are clear. |
| 256 | Exact unary-successor example, warning, Section 23.2, and primitive-recursion definitions | 410,181 | `0f06c5168b3d11f7a69a20eed3dfbe61a395c939e688673ebed778b43737f664` | PASS: equations, lists, and section transition are clean. |
| 257 | Exact primitive-recursion proof plan/example/remark and Section 23.3 opening | 391,581 | `61127adb471105da248b1624c7807062837c28c6743242e12dadd95c53f749c2` | PASS: proof plan and aligned equations are legible. |
| 258 | Exact decidability proof, four-item c.e. equivalence list, and proof plan | 447,032 | `d61cf52373976caf76005a313369173d5174bbda7a1c0f2df01f088c04eaf82e` | PASS: list, proof markers, and page furniture are clean. |
| 259 | Exact Theorem 23.17 and Exercise 23.18; explicit OPEN supplement seam; Section 23.4 opening | 366,821 | `436fdce3fe6b35b6dc14345d400353b351d947b159fe3b742da39c2f2813cabb` | PASS visually: exact material closes before the explicit OPEN notice. |
| 260 | OPEN supplement: minimization, Kleene normal form, Turing/partial-recursive equivalence | 473,870 | `1161b3934d1c894be8611bdd13ad1abf7518bd64a6bac6c89a09c33df9f0fe82` | PASS visually; named exact-source consumers route correctly. |
| 261 | OPEN supplement: numbering boundary and Shepherdson-Sturgis URM | 309,135 | `5f76ee0833247722d5920f92eb4dbecda8801cf19d0c5c8fbc5e51b2fcc9b319` | PASS visually. |
| 262 | OPEN supplement Table 23.1, native landscape | 318,581 | `c1dc604eda5244f568554ca025ab5ce9cfd94643ee421fa4b52e98b1b423062a` | PASS: all columns, rules, rotated folio/running head, and citations remain inside the page. |
| 263 | Table 23.1 continuation tail, native landscape | 83,986 | `97388619efb4f48c4dd3bb08e6b184f13ef25871883cb0e86b754a93ded189c4` | PASS: sparse continuation is intentional; row and rules are not clipped. |
| 264 | OPEN supplement Church-Turing proof boundary | 167,894 | `7a26552a67247ddb36ac2cd419be0d40601a39063449f590941784402a98610a` | PASS visually. |
| 265 | Outgoing seam: Chapter 24 opening | 244,585 | `9f4df1fdf49d7aa40df32915cec968352c49a44ebcc08e0d0d9c95ef4f9f23e1` | PASS: chapter title, Section 24.1, list, and folio are clean. |
| 291 | Chapter 27 body consumer of Definition 23.3 | 348,277 | `f01a6b991ac9b0825c300c645c12797fa7f5685a2cfb489aef9837499e5ef8f3` | PASS. |
| 312 | Chapter 29 body consumer of Section 23.1 | 392,940 | `40aa88f7e851eb8bc197dd6512950973bc4c181cba6e3e805b3fb8b6ddc6d71b` | PASS. |
| 697 | P4 annex opening and Definition 23.3 consumer | 260,226 | `d5b9a5124e6141a1e08cfa203e377f5070539afeee357d0180da779ef0b9ff88` | PASS: annex title, proof items, source pointer, and folio are clean. |
| 783 | Index: Church-Turing thesis, 240 | 435,218 | `c3d335e64ac7beffb5cde3c48015a3429be06cb146fc720abb648818e365ee4b` | PASS. |
| 784 | Index: Computably enumerable set, 233 | 460,244 | `7f534dabc56ada48882692a017451b3b5974fdaf21fef569fa8d5e3e45a6e1b6` | PASS. |
| 785 | Index: Decidable set, 233 | 452,181 | `1c7b4f71b05ba9e4094eec5bc0145e300b8fa8ae1598bb28bdd93d97a472ff68` | PASS. |
| 791 | Index: Kleene equality, 235; Kleene normal form, 236 | 423,311 | `a798782279d869391fe2d1df325fee23adf00f6bf057569a862559f79a198fc2` | PASS. |
| 795 | Index: Partial computable function, 231; partial recursive function, 236 | 408,289 | `c33e25db14dc058021ad6a269c7245e8e4d059c728aeec5c0aee5c70a41d53db` | PASS. |
| 796 | Index: Primitive recursive functions, 232; Primitive recursive relation, 233 | 412,685 | `bc164d0b95173fe674c9547c63ed4db913f164dc8ffd8052235cefab800cc43d` | **FAIL:** separate adjacent entries `rules,` and `Proof` overlap by 3.393 pt. |
| 797 | Index: register machine / Shepherdson-Sturgis, 237 | 423,494 | `d00cc1bea695b19f99618547fe32138356cbf037e87b0f854cf4a63b274cf7ba` | PASS. |
| 802 | Index: Turing machine, 229; unbounded minimization, 236; Unlimited Register Machine, 237 | 415,317 | `4f41f1a32ec1c23ed346b193f0fb948179b3ab2f9e99f00fa8275e4bd2fd8ced` | PASS. |

## Exact-source, OPEN supplement, and seams

The fail-closed restoration checker was run separately for every governed record:

| Record | Exact artifact | SHA-256 | Static result |
|---|---|---|---|
| `SRC-07494-07505` | `handbook/restoration/inherited-07494-07505.tex` | `42286f6d8f726d226161235ac88df4632b9b516984b92722e8aa85267dd5d0c8` | PASS |
| `SRC-07506-07677` | `handbook/restoration/inherited-07506-07677.tex` | `eb27fe6de9a8ffbbe3ec6f317dff66d97dde72f22b1fa3fcb48a4304d85f3c7d` | PASS |
| `SRC-07678-07752` | `handbook/restoration/inherited-07678-07752.tex` | `1b3a7277d05f42cd5e568cc12b851f2e460bdbab4244d11f91f30eff78aa02dd` | PASS |
| `SRC-07753-07843` | `handbook/restoration/inherited-07753-07843.tex` | `e2b7284beabca82f440bb921d779243f1615f8d7077aba73dff6cbde28458b00` | PASS |
| `SRC-07844-07850` | `handbook/restoration/inherited-07844-07850.tex` | `298513236515d123734bf675793bb2c1fc55b5fbe0b2f628c0109e3d9e4e39e4` | PASS |

The five records govern source units 517-543 (27 units). Their source/static PASS and visual body PASS do not admit them: register status remains OPEN/pending.

The routed supplement is `handbook/parts/p04/machines-effective-procedures-supplement.tex`, 11,482 bytes, SHA-256 `a964cffbd9ca70f70a16be497cfd235a4e252d4d3878763de050b378076bc1f4`. It is explicitly printed as OPEN/unadmitted on page 259, retains only the nonoverlapping historical material, and does not close the registers enumerated in its notice. Its minimization, normal-form, equivalence, URM, landscape table, and Church-Turing surfaces on pages 259-264 are visually clean.

The incoming route is physical page 248 (Chapter 22 close), page 249 (public Part IV), blank page 250, page 251 (subordinate exact source title), blank page 252, and page 253 (Chapter 23). The outgoing route is page 264 (supplement close) to page 265 (Chapter 24). No duplicated chapter opening, lost folio, accidental blank, or content collision occurs at either seam.

## Public part, subordinate source title, counters, and anchors

The relevant settled AUX records are:

```text
\newlabel{part:p04}{{IV}{227}{Computability and Complexity}{part.4}{}}
\newlabel{part:p04@cref}{{[part][4][]IV}{[1][227][]227}{}{}{}}
\newlabel{part:computability}{{Computability}{227}{Computability}{section*.41}{}}
\newlabel{part:computability@cref}{{[part][4][]IV}{[1][227][]227}{}{}{}}
\newlabel{ch:turing-machines}{{23}{229}{Machines and Effective Procedures}{chapter.23}{}}
\newlabel{ch:turing-machines@cref}{{[chapter][23][]23}{[1][229][]229}{}{}{}}
\newlabel{part:p05}{{V}{285}{Arithmetic and Incompleteness}{part.5}{}}
```

Thus the public part is IV, the subordinate exact source title does not step the part counter, Chapter 23 remains Chapter 23, and the next public part remains V. The public label's AUX page field is evaluated after the part interleaf, but its actual named destination `part.4` correctly lands on physical page 249.

| Named destination | Physical page | PDF destination `(x,y)` pt | Visible surface/result |
|---|---:|---|---|
| `part.4` | 249 | `(100.892, 513.712)` | Public `Part IV / Computability and Complexity`; PASS |
| `section*.41` | 251 | `(100.892, 529.005)` | Subordinate `Computability` with source-line 7494 attribution; PASS |
| `chapter.23` | 253 | `(100.892, 664.335)` | `Chapter 23 / Machines and Effective Procedures`; PASS |
| `chapter.24` | 265 | `(100.892, 664.335)` | Outgoing Chapter 24; PASS |
| `chapter.annex.4` | 697 | `(100.892, 664.335)` | P4 proof annex; PASS |

The body TOC and outline order is public Part IV (249), subordinate `Computability` (251), Chapter 23 (253), followed by the later Part IV chapters. The outline contains exactly one entry for each of those three surfaces. The P4 annex outline and TOC entry land on page 697.

## Exact labels and consumer-link routes

The exact source labels retain their semantic identities:

| Label | AUX value / Cleveref family | Named destination | Physical page | Result |
|---|---|---|---:|---|
| `sec:turing-machines-01` | 23.1 / `section` | `section.23.1` | 253 | PASS |
| `def:partial-computable` | 23.3 / `definition` | `hbitem.23.item.3` | 255 | PASS |
| `sec:turing-machines-02` | 23.2 / `section` | `section.23.2` | 256 | PASS |
| `sec:turing-machines-03` | 23.3 / `section` | `section.23.3` | 257 | PASS |
| `ex:turing-machines-01` | 23.18 / `hbsourceexercise` | `hbsourceexercise.23.item.18` | 259 | PASS |

The complete relevant annotation census is:

| Target | Physical link sources | Resolved target | Result |
|---|---|---:|---|
| `part.4` | 15 | 249 | PASS |
| `section*.41` | 15 | 251 | PASS |
| `chapter.23` | 15 | 253 | PASS |
| `section.23.1` | 15, 260, 262, 264, 312 | 253 | PASS |
| `hbitem.23.item.3` | 260, 262, 291, 697 | 255 | PASS |
| `section.23.2` | 15, 260 | 256 | PASS |
| `section.23.3` | 15 | 257 | PASS |
| `hbsourceexercise.23.item.18` | none | 259 | PASS: destination exists; no live consumer is claimed. |
| `section*.42` | 15 | 259 | PASS |
| `section.23.4` | 16 | 259 | PASS |
| `chapter.24` | 16 | 265 | PASS |
| `chapter.annex.4` | 23 | 697 | PASS |

The requested affected consumers are therefore present: OPEN supplement references on pages 260, 262, and 264; the Chapter 27 body consumer on page 291; the Chapter 29 body consumer on page 312; and the P4 annex consumer on page 697. No alias target replaces a genuine exact-source destination.

## Whole-PDF navigation census

PyMuPDF 1.28.2 and pypdf 6.15.0 independently enumerate 3,612 named destinations, all on physical pages 1-803. PyMuPDF enumerates 4,040 internal named link annotations and 401 external URI annotations. Every internal annotation has an existing named target, an in-range resolved page, and a page matching the named-destination table: zero missing targets, zero invalid pages, and zero page mismatches.

The PDF outline contains 396 entries, all internal and in range, with maximum nesting level four. Relevant outline rows are:

| Level | Title | Physical page | Named destination |
|---:|---|---:|---|
| 1 | `IV Computability and Complexity` | 249 | `part.4` |
| 2 | `Computability` | 251 | `section*.41` |
| 2 | `Machines and Effective Procedures` | 253 | `chapter.23` |
| 2 | `Proof Annex for Part 4: Computability and Complexity` | 697 | `chapter.annex.4` |

## Index collision: exact visual and geometric evidence

Physical page 796 is printed index page 772. The relevant Chapter 23 entries `Primitive recursive functions, 232` and `Primitive recursive relation, 233` are present and readable. Immediately below them, however, two independent column entries collide on the same baseline:

- left-column final word `rules,`: bounding box `(313.832, 509.489, 339.403, 520.398)` pt;
- right-column first word `Proof`: bounding box `(336.010, 509.489, 362.268, 520.398)` pt.

Because `336.010 < 339.403`, the boxes overlap horizontally by exactly 3.393 pt (approximately 9.43 pixels at 200 dpi). The raster visibly reads `rulesProof`. This is a genuine collision, not extraction order, link highlighting, or antialiasing. No other governed raster showed clipping or collision.

## Whole-PDF pending-reference scan

Two independent full-document extraction passes were performed across all 803 pages:

| Extractor | Version | Literal `??` count | Physical pages |
|---|---:|---:|---|
| pypdf | 6.15.0 | 1 | 73 |
| PyMuPDF | 1.28.2 | 1 | 73 |

Both locate the same inherited phrase in the classical-natural-deduction chapter, `made exact in ??`. No other page contains the literal token. It is outside source lines 07494-07850 and is not a Chapter 23 layout failure, but it independently keeps publication status OPEN.

## Frozen conclusion

- Candidate identity: PASS, exact match to the requested 803-page file.
- Source/static restoration for lines 07494-07850: PASS under all five records.
- Exact-source/body rendering and visual presentation: PASS.
- Public Part IV, subordinate exact source title, chapter order, counters, TOC, outline, and anchors: PASS.
- OPEN supplement and both transition seams: PASS visually; supplement remains OPEN/unadmitted substantively.
- Exact labels and all located body/annex consumers: PASS.
- All named destinations, internal links, and outline entries: PASS.
- Complete governed-surface visual audit: **FAIL** because of the measured index collision on physical page 796.
- Whole publication readiness: **OPEN** because of the sole literal `??` on page 73, the explicitly OPEN supplement, the page-796 collision, and the absence of human acceptance.

No canonical PDF, source file, test, control manifest, or prior report was changed by this audit. The only repository-visible write is this new standalone report; all fresh renders and the ledger are ignored scratch evidence.
