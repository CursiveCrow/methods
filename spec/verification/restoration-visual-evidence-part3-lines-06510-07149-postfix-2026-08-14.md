# Postfix rendered visual evidence for inherited source lines 06510–07149

Date: 2026-08-14  
Audit mode: fail-closed, artifact-specific, read-only except for this new evidence report and ignored temporary rasters

## Outcome

The definitive postfix scratch artifact **passes the repaired Appendix-P contents-page check** and **passes the governed layout/link checks for the exact inherited-source envelope at lines 06510–07149**. In particular, physical page 23 now keeps every `P2`–`P12` number distinct from its title, keeps every title distinct from its folio, wraps the three long titles cleanly, and preserves their destinations.

The artifact nevertheless remains **FAIL / OPEN for publication**: physical page 73 still prints the pending literal `??`. Two independent whole-PDF text extractions each found exactly that one occurrence and no other literal `??`.

Inspection tally:

- 22/22 governed physical pages freshly rendered at 200 dpi;
- 22/22 freshly inspected at original raster resolution;
- 22/22 free of observed clipping, collision, accidental overprint, or broken page furniture;
- 21/22 publication-clean; physical page 73 is the single exception because of the unresolved printed reference.

## Identity gate

Only this PDF was used for PDF rendering, text extraction, link resolution, and outline inspection:

`tmp/annex-toc-definitive-settled-20260814-0940/handbook/main.pdf`

| Property | Required | Observed | Gate |
|---|---:|---:|---|
| PDF title | `The Methods of Reason` | `The Methods of Reason` | PASS |
| Physical pages | 808 | 808 | PASS |
| Bytes | 4,340,364 | 4,340,364 | PASS |
| SHA-256 | `5ec19e985d24cf0180568eebde239c6172990cb6e65a4f522f62f10397041da8` | `5ec19e985d24cf0180568eebde239c6172990cb6e65a4f522f62f10397041da8` | PASS |
| Encryption | none | none | PASS |

This report does not transfer its verdict to `handbook/main.pdf` or to any other build.

## Fresh-render protocol

The PDF instructions were reloaded in full before work began. The governed pages were newly rasterized from the identity-gated scratch PDF with Poppler `pdftoppm` 26.05.0, PNG output, and `-r 200`. The new raster directory was absent before this audit:

`tmp/postfix-06510-07149-20260814-definitive-fresh/`

The complete governed set was physical pages 14, 15, 23, 73, 208–221, 233, 355, 695, and 696. Every output is 1700 × 2200 pixels. Each new image was opened and inspected at original resolution; no earlier raster or verdict was reused. PyMuPDF 1.28.2 and pypdf 6.15.0 supplied independent text/link checks against the same scratch PDF.

## Repaired Appendix-P contents page

Physical page 23 is visually clean. The minimum measured number-to-title separation is 6.153 pt (`P10`–`P12`); the minimum measured title-to-folio separation is 12.546 pt (`P4`). Those positive separations agree with the fresh original-resolution visual inspection: no label/title fusion, title/folio collision, clipped glyph, leader collision, or ambiguous wrap was observed.

| Entry | Printed folio | Physical link target | Number/title gap (pt) | Title/folio gap (pt) | Wrap | Result |
|---|---:|---:|---:|---:|---|---|
| P2 | 663 | 687 | 12.426 | 94.080 | one line | PASS |
| P3 | 671 | 695 | 12.426 | 96.163 | one line | PASS |
| P4 | 675 | 699 | 12.426 | 12.546 | one line | PASS |
| P5 | 685 | 709 | 12.426 | 289.953 | `Incomplete-` / `ness` | PASS |
| P6 | 691 | 715 | 12.426 | 113.302 | one line | PASS |
| P7 | 703 | 727 | 12.426 | 23.335 | one line | PASS |
| P8 | 711 | 735 | 12.426 | 69.556 | one line | PASS |
| P9 | 719 | 743 | 12.426 | 26.848 | one line | PASS |
| P10 | 721 | 745 | 6.153 | 283.419 | `Algebraic and Categorical` / `Logic` | PASS |
| P11 | 723 | 747 | 6.153 | 60.480 | one line | PASS |
| P12 | 725 | 749 | 6.153 | 290.957 | `Mechaniza-` / `tion` | PASS |

For wrapped entries P5, P10, and P12, the title/folio measurement is taken on the continuation line that carries the folio. Page 23 contains 14 link rectangles for the 11 P2–P12 top-level entries because those three wrapped continuations are separately clickable. Every rectangle resolves to its entry's physical target above. P7.1, P7.2, and P7.3 also remain clean and resolve respectively to physical pages 727, 729, and 730. No extracted token matched the former failure signature `P2Proof` through `P12Proof`.

## Exact-source envelope and governed seams

| Physical page(s) | Governed surface | Fresh visual result |
|---|---|---|
| 14 | Contents transition into Part III and Chapter 17 | PASS: titles, leaders, folios, and the Part III transition remain separated and aligned. |
| 15 | Contents entries for 17.6, Chapter 18, its five sections, its editorial supplement, and Chapter 19 | PASS: clean wrapping and leaders; every affected contents link resolves to the expected physical page. |
| 208 | End of Chapter 17 followed by the separately retained OPEN A-162 model-theory notation lookup | PASS: the inherited ending and the pre-Chapter-18 supplement remain visibly distinct; the table fits without clipping or row collision. |
| 209–218 | Exact inherited Chapter 18 body within source lines 06510–07149 | PASS: headings, definitions, statements, proofs, lists, displays, and running furniture are legible and collision-free. |
| 219 | Exact inherited Chapter 18 ending followed by the separately retained OPEN types supplement | PASS: the source ending and supplement are visibly separated; the reader note and Theorems 18.30–18.31 fit cleanly. |
| 220 | Intended blank verso at the chapter boundary | PASS: blank as intended, with no leaked marks or furniture. |
| 221 | Start of Chapter 19 | PASS: clean recto transition; no carry-over or collision from Chapter 18. |
| 233 | Downstream principal-type consumer | PASS: the reference remains legible and clickable. |
| 355 | Choice-dependency table consumers | PASS: rows and linked theorem labels remain separated and legible. |
| 695 | OPEN Part-3 annex supplement and reciprocal body consumer | PASS: heading, reader note, proof, displays, and link surface fit without collision. |
| 696 | Annex continuation and exact Theorem 18.12 consumer | PASS: proof text, displays, headings, and links remain clean. |

The two placement seams required by the restoration route are therefore preserved: the OPEN A-162 lookup is after the Chapter 17 source ending and before Chapter 18, while the OPEN types body supplement is after the Chapter 18 source ending. The related OPEN annex material remains in Appendix P3 rather than being fused into or substituted for the exact source body.

## Contents, outline, and exact-label destinations

Affected contents links resolve as follows:

- physical page 14: Part III → 199; Chapter 17 → 201; sections 17.1–17.5 → 201, 202, 204, 205, and 207;
- physical page 15: section 17.6 → 208; Chapter 18 / section 18.1 → 209; sections 18.2–18.5 → 212, 213, 214, and 216; editorial supplement → 219; Chapter 19 / section 19.1 → 221;
- physical page 23: all P2–P12 targets are recorded in the repair table above, including matching targets for each wrapped continuation.

The PDF outline contains 394 entries. All 394 have physical destinations in the 808-page artifact; none is missing, zero, or out of range. The affected outline route is:

| Outline surface | Physical destination |
|---|---:|
| Model-theory notation lookup | 208 |
| Types, Saturation, and Ultraproducts | 209 |
| Types over parameter sets | 209 |
| Homogeneity | 212 |
| Omitting types | 213 |
| Filters and ultrafilters | 214 |
| Ultraproducts | 216 |
| Editorial supplement to the restored chapter | 219 |
| QE, Categoricity, and Games | 221 |
| Appendix P: Proof Annex | 685 |
| Proof Annex for Part 3: Model Theory | 695 |

The exact-label and supplement consumers in the governed set resolve to genuine destinations rather than aliases:

| Consumer surface | Physical source → target |
|---|---:|
| page 208, `Definition 18.2` | 208 → 209 |
| page 208, `Sections 18.4 and 18.5` | 208 → 214 and 216 |
| page 219, `theorem 18.24` | 219 → 217 |
| page 219, `Annex P3.TYPES.8` | 219 → 695 |
| page 233, `definition 18.15` | 233 → 213 |
| page 355, `lemma 18.20` and `18.24` | 355 → 215 and 217 |
| page 695, `[proves thm:p03-compactness-ultraproduct]` | 695 → 219 |
| page 696, `Theorem 18.12` | 696 → 212 |

Across the complete PDF, PyMuPDF enumerated 4,484 link annotations: 4,083 named internal links and 401 URI links. Every one of the 4,083 named internal links resolved to a physical destination in range (observed target range: physical pages 5–784); unresolved or out-of-range internal destinations: zero.

## Pending-reference gate

Physical page 73 visibly prints:

> The calculus obtained by omitting RAA is intuitionistic natural deduction, made exact in ??; …

Whole-PDF literal scans against the identity-gated scratch PDF produced:

| Extractor | Literal `??` count | Physical pages |
|---|---:|---|
| pypdf 6.15.0 | 1 | 73 |
| PyMuPDF 1.28.2 | 1 | 73 |

This is a real printed pending reference, not merely an extraction artifact: it is also visible in the fresh page-73 raster. It is the publication-blocking finding for this postfix artifact.

## Fresh raster ledger

| Raster | Dimensions | Bytes | SHA-256 |
|---|---:|---:|---|
| `page-014.png` | 1700×2200 | 325,789 | `73c37a58cc559f3fa24aa7cb90e3724bc757f88a667644eca47d6851933f7d24` |
| `page-015.png` | 1700×2200 | 305,001 | `51ffccde7b965ac82df0b731611f2d0a4c53fe094edd0af508619f09bb6a30d8` |
| `page-023.png` | 1700×2200 | 256,756 | `15afce5313afa09de919e564b3a23fb9f1e99625c27403ee8c0e60d040d1d37f` |
| `page-073.png` | 1700×2200 | 352,970 | `432edf2f60fcd389bb04e98c782353a0ce6257773041d88e402d11e3b43cffe8` |
| `page-208.png` | 1700×2200 | 291,131 | `fbb99a8cfe3229182400a69c1767573091a31131080247ef6b96aa83a5ff3e06` |
| `page-209.png` | 1700×2200 | 280,404 | `53a1604c2df764ab4ff3620855ac61866d9f18fa32d392e5f6fe5126285ab977` |
| `page-210.png` | 1700×2200 | 468,302 | `fe3dcc568d7e12e41b80cb8eba1a5bc69a466069166ce5533bd23ba16ac6160d` |
| `page-211.png` | 1700×2200 | 445,247 | `fb71d18e3df1c9ed60f27deff5b6672058dd7efa9d28eb8d4daa0825a83e8fb1` |
| `page-212.png` | 1700×2200 | 443,943 | `d951a32fd4e10ae96c7e2baae06775aa8eebbf002b72e0d410cb44dee9ca5f4a` |
| `page-213.png` | 1700×2200 | 429,433 | `efe76d316e3af050815af76ff96f031d7959a16ecc7c477374e687fd4ad1efb0` |
| `page-214.png` | 1700×2200 | 387,926 | `ea6aa58a9c895e9b50dc18cfd30c455f68d6f7e7e8b4bcef02d1b35594feeef6` |
| `page-215.png` | 1700×2200 | 478,446 | `c0f9674c43775669815b0ff36020e9a15b94b6adf467e39a0f04e7f4dd0ad5c0` |
| `page-216.png` | 1700×2200 | 331,111 | `b3323e2e64942b1abdf5fd66a71bb17c39b44160b338edc3bb66c39365fa3ff0` |
| `page-217.png` | 1700×2200 | 326,477 | `058242cade5cd1d66a89fe285aa8e1eff1a853844b92e961498dab487babdfdb` |
| `page-218.png` | 1700×2200 | 461,890 | `656eea24f7ca3685c9e6b01322cd5b3cd3ea58de48af5434dfcbba1e4989d92b` |
| `page-219.png` | 1700×2200 | 349,408 | `8fec0060c6bea935b88c7c198463ec6c7db6f5b84ea06df8ddd80e767fef1f8f` |
| `page-220.png` | 1700×2200 | 15,924 | `bec662eb728e5bf0421540c5c176a0f90ef321debb54c0ae08e86a3fe51d714e` |
| `page-221.png` | 1700×2200 | 281,637 | `ce321856a7b444efc2232da435a5fc8465ac046ec59b27847ef20095e144f264` |
| `page-233.png` | 1700×2200 | 256,901 | `fdf03ad7d6bba2d0b67bc32fe0da431f5699cf54757c01ce744dc9c1bfce3b6f` |
| `page-355.png` | 1700×2200 | 335,131 | `b33dc3c5690aed0d805cd57a6694b3df0eaf6f1697ccb90605ac757e294bc27d` |
| `page-695.png` | 1700×2200 | 244,924 | `734ad149b33c95787c1dc4c0e1983eb1dc81cbee8da5b12d9e3a12f65672840e` |
| `page-696.png` | 1700×2200 | 414,555 | `20bab8991fa0c5dde909df7fe0046aa98ca9d96c80e198ffa9a37c61c7c9cc1e` |

## Claim boundary and freeze

This audit establishes rendered-layout and PDF-navigation facts only for the hash-pinned scratch artifact above. It does not independently establish source-byte fidelity, mathematical correctness, proof completeness, or the status of any OPEN register item. The sole publication-facing failure observed in the governed set is the pending reference on physical page 73. No handbook source, control file, prior evidence report, or canonical PDF was edited by this audit.
