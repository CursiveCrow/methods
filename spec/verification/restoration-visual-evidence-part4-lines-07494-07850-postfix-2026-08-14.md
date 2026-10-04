# Fresh postfix rendered evidence for inherited source lines 07494-07850

Date: 2026-08-14  
Scope: the frozen index-column-gap postfix candidate identified below; inherited source lines 07494-07850; the public-Part/subordinate-source-Part route; the incoming and outgoing seams; the explicitly OPEN Machines supplement; affected body, annex, TOC, bookmark, and index consumers; the complete reflowed index; and whole-PDF navigation integrity.  
Method boundary: fresh 200 dpi native-orientation raster inspection, complete index word-box comparison, and PDF destination/link/outline/text-extraction checks. This report does not admit a source unit, close an OPEN register, establish mathematical correctness, or record human acceptance.

## Frozen candidate and verdicts

Candidate: `tmp/index-column-gap-settled-20260814-2150/index-column-gap-check.pdf`

| Property | Observed value | Result |
|---|---:|---|
| Title | `The Methods of Reason` | PASS |
| Physical pages | 804 | PASS |
| File size | 4,330,107 bytes | PASS |
| SHA-256 | `613a51cf81ec36ae53fed8217e87cb78ab312c1ed72dc7cd401ec299c40a21b5` | PASS |
| Encryption | none | PASS |
| Media box | 612 x 792 pt on all 804 pages | PASS |
| Native rotation | 764 pages at 0 degrees; 40 pages at 90 degrees | PASS |

**Exact restoration/static verdict: PASS.** All five records for source lines 07494-07850 retain their exact governed artifacts and pass the fail-closed static restoration checks.

**Exact-source/body/supplement visual verdict: PASS.** The Part IV opening, subordinate inherited `Computability` presentation, Chapter 23 exact body, proof plans, equations, lists, exercise, exact-to-OPEN handoff, OPEN Machines supplement, both route seams, affected consumers, and P4 annex are visually clean.

**Navigation verdict: PASS.** Both PDF engines enumerate the same 3,613 named destinations. All 4,040 internal named links and 401 URI links are valid. All 396 outline items are in range and preserve public Part IV, subordinate `Computability`, Chapter 23, and the P4 annex in the correct order.

**Complete governed-surface visual verdict: FAIL.** A distinct cross-column collision occurs on physical page 794 in the reflowed index. The left-column fragment `Entschei-` overlaps the right-column word `normal`; the raster visibly fuses them as `Entscheinormal`.

**Overall publication-facing verdict: OPEN.** The p794 collision prevents a visual release. Both full-PDF extractors also find the single already-governed literal `??` on physical page 73, the supplement remains explicitly OPEN/unadmitted, and human acceptance is absent.

## Fresh render set

The candidate identity was checked before rendering. No raster or verdict from the preceding failed candidate was reused.

- Scratch evidence: `tmp/visual-computability-7494-7850-postfix-20260814/`
- Governed pages: 15-16, 23, 73, 248-265, 291, 312, 697, and every index page 781-804.
- Exactly 49 fresh PNGs were rendered at 200 dpi and inspected at native resolution.
- The render ledger is `tmp/visual-computability-7494-7850-postfix-20260814/render-ledger.tsv`.
- Physical pages 262-263 are correctly native landscape pages; the remaining governed pages are portrait.

All 25 non-index pages passed inspection. Intentional blank versos 250 and 252 are genuinely blank. No observed clipping, collision, overprint, damaged glyph, folio defect, running-head defect, broken TOC leader, or route-seam defect occurs on those pages.

All 24 index pages 781-804 were inspected. The earlier p796 `rules,` / `Proof theory` collision is repaired: the long `Primitive, derived, and admissible rules, 392` entry wraps within its column and `Proof theory, 17` appears on p797. The separate p794 collision below remains a hard failure.

## Exact p794 collision evidence

Physical page 794 is printed index page 770. Fresh word-box extraction finds vertically and horizontally intersecting words in opposing columns:

| Column | Text | Bounding box `(x0, y0, x1, y1)` pt |
|---|---|---|
| left | `Entschei-` | `(306.130, 373.667, 349.988, 383.299)` |
| right | `normal` | `(343.482, 376.037, 376.846, 385.669)` |

The boxes overlap horizontally by 6.506 pt and vertically by 7.262 pt. The fresh native-resolution crop `tmp/visual-computability-7494-7850-postfix-20260814/p794-gutter-crop.png` visibly reads `Entscheinormal`. This is a genuine rendered collision, not merely extraction order.

A stricter independent scan using the unrounded word boxes reproduced the same failure with `Entschei-` at x 306.206-350.094 and `normal` at x 343.482-376.853, horizontal clearance -6.612 pt and vertical intersection 8.539 pt. The small coordinate difference is extractor precision; both measurements establish the same collision.

## Route and navigation surfaces

The relevant destinations remain correct:

| Surface | Physical page | Result |
|---|---:|---|
| public Part IV `Computability and Complexity` | 249 | PASS |
| subordinate inherited `Computability` | 251 | PASS |
| Chapter 23 `Machines and Effective Procedures` | 253 | PASS |
| exact-to-OPEN handoff | 259 | PASS |
| outgoing Chapter 24 | 265 | PASS |
| affected body consumers | 291, 312 | PASS |
| P4 annex and consumer | 697 | PASS |

The Part IV TOC pages 15-16 and annex TOC page 23 are clean. The public part, subordinate source title, chapter, supplement, later chapters, and annex appear once and in the intended hierarchy.

The navigation census is:

- named destinations: 3,613 in each engine, with zero missing, extra, or page-mismatched destinations;
- internal named links: 4,040, all resolving to existing in-range targets;
- URI links: 401, all structurally valid;
- outline items: 396, all in range and ordered correctly.

## Whole-PDF pending-reference scan

Both independent extractors find exactly one literal `??`, solely on physical page 73. No other page contains the literal token. This placeholder is outside source lines 07494-07850 and is not a Chapter 23 layout failure, but it independently keeps publication status OPEN.

## Frozen conclusion

- Candidate identity: PASS.
- Source/static restoration for lines 07494-07850: PASS.
- Exact source, OPEN supplement, seams, consumers, TOCs, annex, and navigation: PASS.
- Prior p796 collision repair: PASS.
- Complete reflowed-index visual audit: **FAIL** on the measured p794 `Entscheinormal` collision.
- Publication readiness: **OPEN** because of the collision, the sole p73 placeholder, explicitly OPEN material, and absent human acceptance.

The candidate must not be promoted. No canonical PDF, source file, test, manifest, ledger, readiness control, or prior report was changed by this audit. The repository-visible write is this standalone report; renders and the ledger remain ignored scratch evidence.
