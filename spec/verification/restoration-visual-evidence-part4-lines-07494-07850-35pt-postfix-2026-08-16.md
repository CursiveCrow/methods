# Fresh 35pt-postfix rendered evidence for inherited source lines 07494-07850

Date: 2026-08-16  
Scope: the frozen class-intended 35pt index candidate identified below; inherited source lines 07494-07850; public Part IV and its subordinate inherited presentation; the exact body, both seams, explicitly OPEN Machines supplement, affected body and annex consumers, TOCs, and all 24 index pages.  
Method boundary: fresh 200 dpi native-orientation raster inspection, two independent index word-box scans, and whole-PDF destination/link/outline/text checks. This report does not admit a source unit, close a register, establish mathematical correctness, dispose of build-warning debt, or record user acceptance.

## Frozen candidate and separated verdicts

Candidate: `tmp/index-column-gap-settled-35pt-20260816-221055/index-column-gap-35pt-check.pdf`

| Property | Observed value | Result |
|---|---:|---|
| Title | `The Methods of Reason` | PASS |
| Physical pages | 804 | PASS |
| File size | 4,330,372 bytes | PASS |
| SHA-256 | `f917b28d27689b99346c8526e9558ea16f1081932d3032ef6f97a02c926166c2` | PASS |
| Encryption | none | PASS |
| Media box | 612 x 792 pt on all pages | PASS |
| Page rotation | 764 pages at 0 degrees; 40 pages at 90 degrees | PASS |

**Exact restoration/static verdict: PASS.** All five governed records covering source lines 07494-07850 retain their exact artifacts and pass the source/static restoration gates.

**Part IV exact-body and supplement visual verdict: PASS.** The public Part IV opening, subordinate inherited `Computability` heading, Chapter 23 exact body, proof plans, equations, lists, exercise, exact-to-OPEN handoff, OPEN Machines supplement, landscape table, both route seams, affected consumers, and P4 annex are visually clean.

**Complete governed-surface visual verdict: PASS.** All 49 governed pages were freshly rendered and inspected. All 24 index pages are clean. The former p794 `Entscheinormal` and p796 `rulesProof` collisions are absent.

**Navigation verdict: PASS.** The PDF has 3,613 valid named destinations, 4,040 valid internal named links, 401 valid URI links, and 396 in-range outline entries. Public Part IV, subordinate `Computability`, Chapter 23, and the P4 annex retain the intended hierarchy and targets.

**Overall publication-facing verdict: OPEN.** Both full-PDF extractors retain exactly one literal `??`, solely on physical page 73. The Machines supplement and all reviewed source units remain OPEN/unadmitted, user acceptance is absent, and the build still carries global warning/box-diagnostic debt outside this bounded visual gate.

## Fresh render protocol

- Candidate identity was checked before rendering; any mismatch would have stopped the audit.
- Fresh scratch evidence: `tmp/pdfs/visual-part4-35pt-20260816/`.
- Governed pages: 15-16, 23, 73, 248-265, 291, 312, 697, and every index page 781-804.
- Exactly 49 PNGs were freshly rendered at 200 dpi and inspected at native resolution.
- Physical pages 262-263 are correctly native landscape pages; all other governed pages are portrait.
- Render ledger: `tmp/pdfs/visual-part4-35pt-20260816/render-ledger.tsv`, 50 lines including header, 5,101 bytes, SHA-256 `f6711070a21400e4524e12d5cf7f99a56e917dd368a15be25e00d1784c8b0b01`.

The 25 non-index pages pass for clipping, margins, tables, equations, lists, glyphs, folios, running heads, TOC leaders, anchors, and route transitions. Intentional blank versos 250 and 252 are genuinely blank. The sparse landscape continuation on p263 is intentional and not clipped.

The 24-page index was inspected page by page. Columns remain visually separate throughout, long entries wrap within their own columns, folios and running heads are intact, and the final index leaf is intentional.

## Exhaustive index geometry

The same Poppler `-bbox-layout` representation used by the public regression scanned every left/right word pair whose vertical boxes intersect on physical pages 781-804:

- index pages: 24;
- cross-column pairs below 4 pt: 0;
- minimum clearance: 12.578210 pt;
- limiting pair: `proof-theoretic` / `An`;
- `Entscheinormal`: absent;
- `rulesProof` and `rules,Proof`: absent.

An independent pdfplumber advance-box scan also found zero physical overlap. Its smallest positive advance-box separation was 3.043639 pt (`from` / `a` on p788); that extractor includes font-advance extents rather than Poppler's rendered word extents, but independently confirms no intersection or fused text.

Full-resolution inspection of p794 and p796 confirms the two earlier failures are repaired. The production hook now applies the book class's intended 35 pt column separation before `theindex` computes column widths.

## Route, consumers, and navigation

| Surface | Physical page | Result |
|---|---:|---|
| public Part IV `Computability and Complexity` | 249 | PASS |
| subordinate inherited `Computability` | 251 | PASS |
| Chapter 23 `Machines and Effective Procedures` | 253 | PASS |
| exact-to-OPEN handoff | 259 | PASS |
| outgoing Chapter 24 | 265 | PASS |
| affected body consumers | 291, 312 | PASS |
| P4 annex and consumer | 697 | PASS |

The TOC surfaces on p15-16 and the annex TOC on p23 are clean. Public Part IV, subordinate source title, exact chapter, supplement, later chapters, and annex each occur in their intended hierarchy.

Whole-PDF structure checks found:

- title: exactly `The Methods of Reason`;
- named destinations: 3,613, zero invalid;
- outline entries: 396, zero invalid;
- internal links: 4,040, zero invalid;
- URI links: 401, zero invalid;
- literal `??`: one occurrence, physical page 73 only.

## Build boundary

The settled build completed LaTeX, Biber, MakeIndex, and both final settling passes. MakeIndex accepted all 1,405 entries with zero rejects or warnings. There are no undefined citations, duplicate labels/destinations, or rerun requests. Exactly one governed pending reference remains, `ch:intuitionistic-logic`.

This is not a global clean-build claim. The log still reports two inherited font warnings and 544 overfull, 1,799 underfull horizontal, and 15 underfull vertical box diagnostics. The exhaustive index geometry establishes that none of those diagnostics causes a cross-column index collision, but the completion plan requires separate disposition or removal of all global warning debt before release.

## Frozen conclusion

- Candidate identity: PASS.
- Source/static restoration for lines 07494-07850: PASS.
- Exact body, OPEN supplement, seams, consumers, TOCs, annex, and navigation: PASS.
- Complete 49-page governed visual set: PASS.
- Complete 24-page index: PASS, with no cross-column collision.
- Whole publication readiness: **OPEN** because source/register/external/AI/admission work remains, the p73 reference is unresolved, global build-warning debt remains, and user acceptance is absent.

The candidate is eligible for the next bounded canonical checkpoint but is not a release artifact. The two failed Part IV candidates and their reports remain preserved as historical evidence. No canonical PDF, manifest, ledger, readiness control, or earlier report was changed by this audit.
