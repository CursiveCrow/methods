# Rendered visual evidence for inherited source lines 07150-07493

Date: 2026-08-14  
Audit mode: fail-closed, artifact-specific, read-only except for this new evidence report and fresh ignored temporary rasters

## Outcome

**Exact-source visual verdict: PASS.** The complete print-bearing presentation of exact inherited source lines 07150-07493 on physical pages 221-226 is legible and free of observed clipping, collision, accidental overprint, broken display layout, or damaged page furniture. The incoming chapter seam, the exact-source-to-OPEN-supplement seam, and the outgoing chapter seam are also visually clean.

**Overall publication-facing verdict: FAIL / OPEN.** Physical page 73 visibly prints the pending literal `??`. Independent whole-PDF extraction with pypdf 6.15.0 and PyMuPDF 1.28.2 found exactly that one occurrence. In addition, the named destination for the currently unconsumed exact label `method:back-and-forth` is placed at the bottom of physical page 223 while Method 19.13 typesets at the top of physical page 224. All live external consumers of exact replacement labels resolve correctly, but the semantic one-page anchor offset is a real navigation FAIL even though this build has no link annotation that consumes it.

The explicit OPEN body and annex material remains OPEN and unadmitted. This visual audit does not decide content correctness, mathematical correctness, proof completeness, admission, provenance, or any AI-review or human-review claim.

Inspection tally:

- 24/24 governed physical pages freshly rendered with Poppler 26.05.0 at fixed 200 dpi;
- 24/24 fresh rasters opened and inspected at original raster resolution;
- 24/24 free of observed clipping, collision, accidental overprint, broken table or figure layout, or damaged page furniture;
- 23/24 free of a visible literal pending-reference token; physical page 73 is the exception;
- 4,067/4,067 internal link annotations resolve to an in-range physical page;
- 394/394 outline entries have an in-range physical destination.

## Identity gate

Only this PDF was used for rendering, text extraction, link resolution, named-destination inspection, and outline inspection:

`tmp/qe-7150-7493-settled-20260814/qe-7150-7493-check.pdf`

| Property | Required | Observed | Gate |
|---|---:|---:|---|
| PDF title | `The Methods of Reason` | `The Methods of Reason` | PASS |
| Physical pages | 808 | 808 | PASS |
| Bytes | 4,341,800 | 4,341,800 | PASS |
| SHA-256 | `fe860828249ffe04e7c325bbbf16def6a4a273d39ab81e95b92b79a4a6662161` | `fe860828249ffe04e7c325bbbf16def6a4a273d39ab81e95b92b79a4a6662161` | PASS |
| Encryption | none | none | PASS |
| MediaBox | US Letter, 612 x 792 pt | all 808 pages are 612 x 792 pt | PASS |

This report does not transfer its verdict to `handbook/main.pdf`, to `source/formal-logic-reference.pdf`, or to any other build.

## Fresh-render protocol and governed set

The PDF instructions were reread in full before work began. The fresh raster directory did not exist before this audit:

`tmp/qe-7150-7493-visual-audit-20260814-fresh/`

Poppler `pdftoppm` 26.05.0 rendered each governed physical page separately with `-r 200 -png -singlefile`. Portrait pages are 1700 x 2200 pixels. The two intentionally landscape table pages, 228 and 230, are 2200 x 1700 pixels. No earlier raster or earlier visual verdict was reused.

The governed set is physical pages 14, 15, 23, 73, 219-236, 697, and 698:

- pages 14-15: affected Part III contents surfaces;
- page 23: affected Appendix P contents surface;
- page 73: known pending-reference placeholder;
- pages 219-220: preceding chapter ending and intended blank verso before Chapter 19;
- pages 221-226: every physical page containing print-bearing material from exact source lines 07150-07493;
- pages 226-233: every routed OPEN QE body-supplement page, including the two landscape tables and EF figure;
- pages 234-235: intended blank verso and clean Chapter 20 transition;
- page 236: the external Section 19.2 consumer in Chapter 20;
- pages 697-698: the complete routed Part III annex surface, including the OPEN QE annex supplement and both restored-label consumers.

## Exact-source page map

The source-to-page map was rebuilt from the pinned PDF with independent text extraction and source anchors. Because TeX can break one source line across physical pages, source lines 07190 and 07388 occur on both adjacent pages. Blank and environment-control lines do not themselves print.

| Physical page | Print-bearing exact-source span | Boundary evidence | Visual result |
|---|---|---|---|
| 221 | 07150-07190 | Chapter 19 through the first half of the DLO construction remark | PASS |
| 222 | 07190-07259 | remainder of the remark through the complete reduction-lemma proof | PASS |
| 223 | 07261-07322 | DLO corollary and ACF theorem through finite partial isomorphism | PASS |
| 224 | 07324-07388 | back-and-forth method/test/proof through the first part of the saturated-corollary proof | PASS |
| 225 | 07388-07449 | remainder of the saturated-corollary proof through Ryll-Nardzewski | PASS |
| 226 | 07451-07493 | Morley, final warning, and Exercises 19.21-19.23; exact source then ends before the bold OPEN reader note | PASS |

The exact-source block is visibly distinguishable from the separately attributed derivative: the bold `OPEN:` reader note begins after Exercise 19.23 on physical page 226 and explicitly says the following material does not replace, alter, or complete the exact inherited chapter.

## Visual findings by governed surface

| Physical page(s) | Governed surface | Fresh visual result |
|---|---|---|
| 14-15 | Part III contents, Chapter 19 entries, and adjacent Chapter 18/20 entries | PASS: hierarchy, titles, leaders, and folios are separated, aligned, and unclipped. |
| 23 | Appendix P contents and P3 entry | PASS: P3 is distinct from its title and folio; wrapped later annex entries remain clean. |
| 73 | Known classical-natural-deduction placeholder | **FAIL:** literal `??` is visibly printed in the sentence ending `made exact in ??;`. No collision or clipping accompanies it. |
| 219-220 | Pre-Chapter-19 transition | PASS: the prior chapter and its separately marked supplement end cleanly; page 220 is an intended blank verso. |
| 221-226 | Exact inherited Chapter 19 presentation | PASS: headings, definitions, methods, statements, proofs, lists, displays, citations, exercises, running heads, and folios are legible and collision-free. |
| 226-227 | Exact-source-to-OPEN-body transition | PASS: Exercise 19.23 ends cleanly; the OPEN reader note and Definition 19.24 remain visibly separate and fit without clipping. |
| 228, 230 | Landscape Tables 19.1 and 19.2 | PASS: captions, rules, rows, columns, citations, rotated running furniture, and page edges are intact and readable at native resolution. |
| 229 | Post-Table-19.1 continuation | PASS: the short continuation is clean; retained whitespace is not leaked or clipped content. |
| 231 | OPEN QE continuation and EF section start | PASS: STUB box, section heading, definitions, theorem, and running furniture fit cleanly. The displayed STUB remains a content-status marker, not a visual closure. |
| 232 | EF theorem continuation, figure, and parity example | PASS: Figure 19.1, caption, labels, arrows, and surrounding text are sharp and nonoverlapping. |
| 233-235 | OPEN body ending and Chapter 20 transition | PASS: the supplement ends cleanly, page 234 is an intended blank verso, and Chapter 20 starts cleanly on page 235. |
| 236 | Chapter 20 external Section 19.2 consumer | PASS: the reference is legible and resolves to the exact restored Section 19.2 destination. |
| 697-698 | Part III annex and OPEN QE annex supplement | PASS: chapter heading, OPEN note split, proof text, restored-label marker, theorem consumer, displays, and folios are clean and unclipped. |

## Contents, outline, and destination validation

Affected contents links resolve as follows:

| Contents surface | Physical target | Result |
|---|---:|---|
| page 14, Part III Model Theory | 199 | PASS |
| page 15, Chapter 19 Quantifier Elimination and Categoricity | 221 | PASS |
| page 15, Section 19.1 Quantifier elimination | 221 | PASS |
| page 15, Section 19.2 Categoricity | 223 | PASS |
| page 15, Section 19.3 Ehrenfeucht-Fraisse games | 231 | PASS |
| page 15, Chapter 20 Prime Models and Classification Theory | 235 | PASS |
| page 23, Appendix P: Proof Annex | 687 | PASS |
| page 23, P3 Proof Annex for Part 3: Model Theory | 697 | PASS |

The PDF outline has 394 entries. All 394 have destinations in the 808-page artifact; none is missing, zero, or out of range. The affected outline route is:

| Outline surface | Physical destination |
|---|---:|
| III Model Theory | 199 |
| Types, Saturation, and Ultraproducts | 209 |
| Quantifier Elimination and Categoricity | 221 |
| Quantifier elimination | 221 |
| Categoricity | 223 |
| Ehrenfeucht-Fraisse games | 231 |
| Prime Models and Classification Theory | 235 |
| Appendix P: Proof Annex | 687 |
| Proof Annex for Part 3: Model Theory | 697 |

Across the complete PDF, PyMuPDF enumerated 4,067 named internal link annotations and 401 URI links. All 4,067 internal links resolve to physical pages in range 5-784; unresolved or out-of-range internal links: zero. Independently, pypdf enumerated 3,610 named destinations; all 3,610 resolve to physical pages in range 1-808.

### Exact labels and external consumers

The exact source contributes 13 labels. Their named destinations are in range:

| Exact label(s) | Named physical destination | Visible item page | Result |
|---|---:|---:|---|
| `ch:qe-categoricity`, `sec:qe-categoricity-01`, `thm:dlo-qe` | 221 | 221 | PASS |
| `def:theory-completeness`, `lem:model-completeness-reduction` | 222 | 222 | PASS |
| `sec:qe-categoricity-02` | 223 | 223 | PASS |
| `method:back-and-forth` | 223 at PDF y=116.509 pt | 224 | **FAIL:** anchor precedes the page break by one physical page; no live link annotation consumes it. |
| `thm:back-and-forth-test` | 224 | 224 | PASS |
| `thm:dlo-countable-categorical` | 225 | 225 | PASS |
| `ex:qe-categoricity-01`, `ex:qe-categoricity-02`, `ex:qe-categoricity-03`, `ex:back-and-forth-equivalence` | 226 | 226 | PASS |

Every external consumer of a genuine exact replacement label in the routed body or annex was inspected:

| Consumer surface | Named destination | Physical source -> target | Result |
|---|---|---:|---|
| page 236, `Section 19.2` | `section.19.2` | 236 -> 223 | PASS |
| page 698, `[proves thm:dlo-countable-categorical]` | `hbsourcetheorem.19.item.16` | 698 -> 225 | PASS |
| page 698, `Theorem 19.14` | `hbsourcetheorem.19.item.14` | 698 -> 224 | PASS |

These consumers target the genuine exact-source destinations, not retired historical aliases. The method-anchor failure above does not affect any link annotation in this PDF, but it is a real semantic destination failure and is not silently treated as correct.

## Whole-PDF pending-reference gate

Physical page 73 visibly prints:

> The calculus obtained by omitting RAA is intuitionistic natural deduction, made exact in ??; ...

Whole-PDF literal scans against the pinned PDF produced:

| Extractor | Literal `??` count | Physical pages |
|---|---:|---|
| pypdf 6.15.0 | 1 | 73 |
| PyMuPDF 1.28.2 | 1 | 73 |

This is a real rendered placeholder, not merely an extraction artifact, and it is the immediate publication-facing blocker observed in this governed audit.

## Fresh raster ledger

| Raster | Dimensions | Mode | Bytes | SHA-256 |
|---|---:|---|---:|---|
| `page-014.png` | 1700x2200 | RGB | 325,789 | `73c37a58cc559f3fa24aa7cb90e3724bc757f88a667644eca47d6851933f7d24` |
| `page-015.png` | 1700x2200 | RGB | 296,117 | `9b69446257d6c577d1208252486088acd9b1f11d10f4debb2d9117f8f0abafc0` |
| `page-023.png` | 1700x2200 | RGB | 256,531 | `21f2135cd0d9238b1130bb3693a4d7cf74aafa8d7dd4ab135af836464c395b8a` |
| `page-073.png` | 1700x2200 | RGB | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` |
| `page-219.png` | 1700x2200 | RGB | 349,408 | `8fec0060c6bea935b88c7c198463ec6c7db6f5b84ea06df8ddd80e767fef1f8f` |
| `page-220.png` | 1700x2200 | RGB | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` |
| `page-221.png` | 1700x2200 | RGB | 275,582 | `6873feed3bd9093bd4ac04c6a898dcad7c130a7e1062064f196562aaca5a709e` |
| `page-222.png` | 1700x2200 | RGB | 411,609 | `ea8c8f528fadba00a2267a9dfda5cebdb68c1d2633c2399e3eba070a98641aa8` |
| `page-223.png` | 1700x2200 | RGB | 441,761 | `bc7bd78c834c1fe983d40a4db29e5f37d2846c865a9a80d763135cbe431a77fa` |
| `page-224.png` | 1700x2200 | RGB | 471,805 | `6286db3c5c061cb1088fe2aee06193939a8f32724c33a8a7b05a52f6eebedd78` |
| `page-225.png` | 1700x2200 | RGB | 448,003 | `0dad2f343aa8b6c1086d3fffa58110e38f1dbcb2b0cdc641e530ae539a13976f` |
| `page-226.png` | 1700x2200 | RGB | 453,163 | `0d9f14495b48107e964196dfca5b9dbbbcb31e3e83920e28f2419fa4222489ef` |
| `page-227.png` | 1700x2200 | RGB | 129,758 | `6660fc43c2edacf51533e01357c4967dcaa479d128bc011079af8a77675fb7d7` |
| `page-228.png` | 2200x1700 | RGB | 202,023 | `c43ec08dffdaac60a0fc0f6af7a655c1f4ec493255c517dc740cbd887ff6255e` |
| `page-229.png` | 1700x2200 | RGB | 93,306 | `2f5e6ede56d4ee3f0b719c5110ea2c922accbd194c84afac2d44fba5fa4b4225` |
| `page-230.png` | 2200x1700 | RGB | 236,453 | `fdd9cf7f31a55e348815fe8ba454e99a211011908468baf28860f15189f38312` |
| `page-231.png` | 1700x2200 | RGB | 441,113 | `e1890e55d2dc6f449c39fee77862586d97a98122d60076be13541df91b9e2cea` |
| `page-232.png` | 1700x2200 | RGB | 392,157 | `dc992c73809dccfe420a5647178df13216878b313fc74e5704eae073d00c97b2` |
| `page-233.png` | 1700x2200 | RGB | 188,670 | `9d3653a301ceb6cdb7c1d4c3687e6b80c60e10c2580fa261c263b00e0c169e57` |
| `page-234.png` | 1700x2200 | RGB | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` |
| `page-235.png` | 1700x2200 | RGB | 256,121 | `d37dc96d3bb5eac3d07e2e2a0b099de1b240a60fcf7501bf4d9391b7b8963fe6` |
| `page-236.png` | 1700x2200 | RGB | 418,033 | `5109260405b39fbe54660ece148744e33e4e08cb3d1b896e5eb93ee650fb0c39` |
| `page-697.png` | 1700x2200 | RGB | 250,056 | `19b8e36eb1de01bdf9b0d981e5ed28dda9f0e7de402ccd3ad3fe8f1f9bbb2da9` |
| `page-698.png` | 1700x2200 | RGB | 139,763 | `304c008e350eff1cca1ec06a1046a6bb76e7eddc7922298617d7854c246500bc` |

## Claim boundary and freeze

This audit establishes rendered-layout and PDF-navigation facts only for the exact hash-pinned scratch artifact above. It does not independently establish source-byte fidelity, mathematical correctness, proof completeness, source or derivative admission, register closure, AI-review completion, human-review completion, or terminal publication readiness. The exact-source visual layout passes; the overall artifact remains FAIL / OPEN because of the visible page-73 placeholder, the latent method-label destination placement, and all separately governed OPEN claims that this report leaves unchanged.

No handbook source, test, canonical PDF, manifest, snapshot, ledger, readiness file, or prior evidence report was edited by this audit.
