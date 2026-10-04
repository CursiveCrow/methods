# Fresh postfix rendered evidence for inherited source lines 07150-07493

Date: 2026-08-14  
Scope: the single settled candidate identified below; inherited source lines 07150-07493; their incoming and outgoing seams; the related body and annex consumers; and whole-PDF navigation integrity.  
Method boundary: fresh 200 dpi raster inspection plus PDF-structure and text-extraction checks. This report does not admit any source unit, close any OPEN register, establish the mathematical correctness of the text, or record human acceptance.

## Frozen candidate and verdict

Candidate: `tmp/qe-7150-7493-anchor-postfix-settled-20260814/qe-7150-7493-anchor-postfix-check.pdf`

| Property | Observed value | Result |
|---|---:|---|
| Title | `The Methods of Reason` | PASS |
| Physical pages | 808 | PASS |
| File size | 4,342,675 bytes | PASS |
| SHA-256 | `7bb75ff1782ccbd1002e09e34358a14ab9de86d0229ecc07a0a6cec1e05a5391` | PASS |
| Encryption | none | PASS |
| Media box | 612 x 792 pt on all 808 pages (US Letter) | PASS |
| Native page rotation | 768 pages at 0 degrees; 40 pages at 90 degrees | PASS |

**Exact-source visual verdict: PASS.** The complete print-bearing presentation of inherited source lines 07150-07493 on physical pages 221-226 is legible and free of observed clipping, collision, accidental overprint, broken display layout, unreadable glyphs, or damaged page furniture. The source boundary on page 226 remains visibly separate from the following OPEN supplement.

**Postfix navigation verdict: PASS.** The exact label `method:back-and-forth` now resolves to physical page 224, the same page as the visible `Method 19.13 (Back-and-forth)` heading. Its counter value and Cleveref family remain `19.13` and `hbsourcemethod`. All 3,617 named destinations, 4,067 internal named link annotations, and 394 outline entries resolve to in-range pages.

**Tranche layout verdict: PASS.** All 24 governed pages were freshly rendered and inspected. The body and annex TOCs, OPEN supplements, incoming and outgoing chapter seams, landscape tables, body/annex consumers, and blank recto/verso control pages are visually coherent.

**Overall publication-facing verdict: OPEN.** Both independent whole-PDF extraction passes find exactly one literal `??`, solely on physical page 73. That inherited pending reference is outside this tranche and is not a visual failure of lines 07150-07493. It nevertheless prevents a final publication-ready verdict. Human acceptance is also not established by this report.

## Fresh render protocol

- The candidate identity was checked before rendering; a mismatch would have stopped the audit.
- A new scratch directory, `tmp/visual-qe-7150-7493-anchor-postfix-20260814`, was created for this audit. No raster or verdict from the rejected predecessor candidate was used.
- Physical pages 14, 15, 23, 73, 219-236, 697, and 698 were rendered directly from the frozen candidate with Poppler at 200 dpi and native orientation.
- The required set contains 24 pages. Exactly 24 PNGs were produced and each was visually inspected.
- Portrait renders are 1700 x 2200 pixels. The two governed rotated table pages, 228 and 230, are 2200 x 1700 pixels.
- The canonical tab-separated render ledger payload has 24 lines, 2,181 bytes, and SHA-256 `e59415c264db6121834f4188df8f88d44d9bc3da98d3ce75b40295fa9724e42b`.

## Per-page render and inspection ledger

| Physical page | Governed content | PNG bytes | PNG SHA-256 | Visual result |
|---:|---|---:|---|---|
| 14 | Body TOC through Chapter 17 | 325,789 | `73c37a58cc559f3fa24aa7cb90e3724bc757f88a667644eca47d6851933f7d24` | PASS: hierarchy, leaders, page numbers, and margins are clean. |
| 15 | Body TOC for Chapters 18-23, including Chapter 19 | 296,117 | `9b69446257d6c577d1208252486088acd9b1f11d10f4debb2d9117f8f0abafc0` | PASS: Chapter 19 and its three sections are present and aligned. |
| 23 | Annex TOC, including P3 | 256,531 | `21f2135cd0d9238b1130bb3693a4d7cf74aafa8d7dd4ab135af836464c395b8a` | PASS: annex hierarchy and long wrapped titles are legible and noncolliding. |
| 73 | Sole inherited pending reference | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` | OPEN globally: one visible `??`; surrounding proof layout is otherwise clean. |
| 219 | Chapter 18 OPEN editorial supplement and annex consumer | 349,408 | `8fec0060c6bea935b88c7c198463ec6c7db6f5b84ea06df8ddd80e767fef1f8f` | PASS visually; OPEN/unadmitted status is printed explicitly. |
| 220 | Intentional blank verso before Chapter 19 | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS: genuinely blank and artifact-free. |
| 221 | Exact lines 07150-07190: Chapter 19 through the opening DLO construction | 275,582 | `6873feed3bd9093bd4ac04c6a898dcad7c130a7e1062064f196562aaca5a709e` | PASS. |
| 222 | Exact line 07190 continuation through line 07259 | 411,609 | `ea8c8f528fadba00a2267a9dfda5cebdb68c1d2633c2399e3eba070a98641aa8` | PASS: displays, long definition title, proof, and QED fit cleanly. |
| 223 | Exact lines 07261-07322 | 441,761 | `bc7bd78c834c1fe983d40a4db29e5f37d2846c865a9a80d763135cbe431a77fa` | PASS: categoricity section and finite-partial-isomorphism definition close cleanly. |
| 224 | Exact lines 07324-07388, including Method 19.13 and Theorem 19.14 | 471,805 | `6286db3c5c061cb1088fe2aee06193939a8f32724c33a8a7b05a52f6eebedd78` | PASS: Method 19.13 is visibly at the top and shares this physical page with its label destination. |
| 225 | Exact line 07388 continuation through line 07449 | 448,003 | `0dad2f343aa8b6c1088d3fffa58110e38f1dbcb2b0cdc641e530ae539a13976f` | PASS: source theorem 19.16 and subsequent classification material are legible. |
| 226 | Exact lines 07451-07493, followed by the OPEN supplement seam | 453,163 | `0d9f14495b48107e964196dfca5b9dbbbcb31e3e83920e28f2419fa4222489ef` | PASS: exact exercises end before a plainly marked OPEN reader note. |
| 227 | OPEN QE supplement continuation | 129,758 | `6660fc43c2edacf51533e01357c4967dcaa479d128bc011079af8a77675fb7d7` | PASS visually; no admission is inferred. |
| 228 | OPEN supplement Table 19.1, native landscape | 202,023 | `c43ec08dffdaac60a0fc0f6af7a655c1f4ec493255c517dc740cbd887ff6255e` | PASS: all columns, rules, caption, and rotated furniture remain inside the page. |
| 229 | OPEN supplement bridge after Table 19.1 | 93,306 | `2f5e6ede56d4ee3f0b719c5110ea2c922accbd194c84afac2d44fba5fa4b4225` | PASS. |
| 230 | OPEN supplement Table 19.2, native landscape | 236,453 | `fdd9cf7f31a55e348815fe8ba454e99a211011908468baf28860f15189f38312` | PASS: dense cells and mathematical notation are legible without clipping. |
| 231 | OPEN supplement continuation, STUB notice, and Section 19.3 | 441,113 | `e1890e55d2dc6f449c39fee77862586d97a98122d60076be13541df91b9e2cea` | PASS visually; the deferred row remains explicitly open. |
| 232 | OPEN supplement EF-game material and Figure 19.1 | 392,157 | `dc992c73809dccfe420a5647178df13216878b313fc74e5704eae073d00c97b2` | PASS: figure, caption, formulas, and text do not collide. |
| 233 | OPEN supplement outgoing text | 188,670 | `9d3653a301ceb6cdb7c1d4c3687e6b80c60e10c2580fa261c263b00e0c169e57` | PASS: clean close with no orphaned or clipped text. |
| 234 | Intentional blank verso before Chapter 20 | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` | PASS: genuinely blank and artifact-free. |
| 235 | Chapter 20 opening seam | 256,121 | `d37dc96d3bb5eac3d07e2e2a0b099de1b240a60fcf7501bf4d9391b7b8963fe6` | PASS: chapter opening, introduction, definition, and theorem start are clean. |
| 236 | Chapter 20 continuation | 418,033 | `5109260405b39fbe54660ece148744e33e4e08cb3d1b896e5eb93ee650fb0c39` | PASS: continuation and Section 20.2 transition are clean. |
| 697 | P3 annex opening and TYPES.8 consumer pair | 250,056 | `19b8e36eb1de01bdf9b0d981e5ed28dda9f0e7de402ccd3ad3fe8f1f9bbb2da9` | PASS visually; OPEN/nonadmission notes are explicit. |
| 698 | P3 annex continuation and QE.5 source-result link | 139,763 | `304c008e350eff1cca1ec06a1046a6bb76e7eddc7922298617d7854c246500bc` | PASS: continuation seam, proof, QED, and source-result link text are clean. |

## Exact-source and seam checks

The fail-closed static restoration checker was run separately for each governed record and returned PASS for `SRC-07150-07294`, `SRC-07295-07468`, and `SRC-07469-07493`. The exact artifacts observed by this audit are:

| Artifact | SHA-256 | Static result |
|---|---|---|
| `handbook/restoration/inherited-07150-07294.tex` | `ccb19227218a479328d04079082c149bbd9acf4b587c45d13fff49a07548eff8` | PASS |
| `handbook/restoration/inherited-07295-07468.tex` | `ac14d5d63a54e8d7174783e28a228fac224a72352e15f0ce253d89eafc1c0672` | PASS |
| `handbook/restoration/inherited-07469-07493.tex` | `ed7ab7dab5fb7e2774abefc9b3a3022f25000df53f468e11e9ba740d86505c4e` | PASS |

That static result establishes byte-exact restoration under the records' own stated boundary. The page inspection independently establishes that the exact material is present and visually sound. Neither result admits the 31 governed source units: their register status remains OPEN/pending.

The incoming route is clean: the Chapter 18 OPEN editorial supplement ends on page 219, page 220 is an intentional blank verso, and Chapter 19 begins on page 221. The exact-source-to-supplement boundary is visible on page 226: the final exact exercise closes before a reader note explicitly marked `OPEN`. The outgoing route is also clean: OPEN supplement material closes on page 233, page 234 is blank, and Chapter 20 begins on page 235.

## Navigation and consumer audit

PyMuPDF 1.28.2 and pypdf 6.15.0 independently resolve 3,617 named destinations; all 3,617 land on physical pages 1-808. PyMuPDF enumerates 4,067 internal named link annotations and 401 external URI annotations. Every internal link has an existing named target, an in-range page, and a page matching the named-destination table. There are zero missing targets, zero invalid pages, and zero target-page mismatches.

The PDF outline contains 394 entries, all internal and all in range, with a maximum nesting level of four. The body TOC Chapter 19 link on physical page 15 resolves to physical page 221. The annex TOC P3 link on physical page 23 resolves to physical page 697.

### Method 19.13 anchor regression

The settled AUX record is:

```text
\newlabel{method:back-and-forth}{{19.13}{200}{Back-and-forth}{section*.39}{}}
\newlabel{method:back-and-forth@cref}{{[hbsourcemethod][13][]19.13}{[1][199][]200}{}{}{}}
```

Thus the semantic counter is still `19.13`, the title is still `Back-and-forth`, the printed page is still 200, and the Cleveref family is still `hbsourcemethod`. The label target `section*.39` resolves to zero-based PDF page 223, hence physical page 224, at PDF coordinate `(151.701, 664.335)` pt. In top-origin coordinates its vertical position is 127.665 pt. The visible `Method 19.13` heading begins on that same page at 130.120 pt, so the destination precedes the heading by approximately 2.455 pt.

The theorem-environment destination `hbsourcemethod.19.item.13` still exists on physical page 223, but it is not the target recorded by `method:back-and-forth`, and neither destination currently has a live link annotation consumer. Its continued existence therefore does not reintroduce the rejected one-page label offset. The exact label's actual route is the post-heading `section*.39` destination on physical page 224.

### Body and annex consumers

| Visible consumer | Named target | Resolved route | Result |
|---|---|---|---|
| Page 219, `Status: proved (Annex P3.TYPES.8)` | `annexitem.annex.3.annexitem.1` | 219 -> 697 | PASS |
| Page 697, `[proves thm:p03-compactness-ultraproduct]` | `hbitem.18.item.31` | 697 -> 219 | PASS |
| Page 698, `[proves thm:dlo-countable-categorical]` | `hbsourcetheorem.19.item.16` | 698 -> 225 | PASS |
| Source theorem label `thm:dlo-countable-categorical` | `hbsourcetheorem.19.item.16` | physical page 225, visible Theorem 19.16 | PASS |

The annex labels retain their AUX/Cleveref identities: `annex:p3.types.8` maps to `annexitem.annex.3.annexitem.1` and `annex:p3.qe.5` maps to `annexitem.annex.3.annexitem.2`. The visible historical names do not imply admission or closure.

## Whole-PDF pending-reference scan

Two complete, independent extraction passes were performed across all 808 pages:

| Extractor | Version | Literal `??` count | Physical pages |
|---|---:|---:|---|
| pypdf | 6.15.0 | 1 | 73 |
| PyMuPDF | 1.28.2 | 1 | 73 |

Both locate the same sentence in the classical-natural-deduction chapter: the calculus is described as "made exact in ??". No other page contains the literal token. This is the sole observed global pending-reference blocker and remains outside the governed exact-source tranche.

## Final bounded conclusion

- Source/static restoration for lines 07150-07493: PASS under the three restoration records.
- Fresh required-page rendering and visual inspection: PASS, 24 of 24 pages.
- Exact-source print presentation: PASS.
- OPEN supplements and body/annex seams: PASS visually; still OPEN/unadmitted substantively.
- Method 19.13 label, counter, Cleveref family, and physical destination: PASS.
- All named destinations, internal links, and outline entries: PASS.
- Whole publication readiness: OPEN because physical page 73 still contains the sole literal `??` and human acceptance has not occurred.

No canonical PDF, source file, test, control manifest, prior report, or prior render was changed by this audit.
