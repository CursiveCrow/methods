# Phase 4 verification: Part 6

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-11
Visit: P6, Set Theory
Verified source: `v1.1-verified`, Part VII, lines 10060--11352.

## Delivered scope

- The Part-6 body now contains eight chapters: axioms, ordinals, and the
  cumulative hierarchy; cardinals and Choice; constructibility, forcing, and
  independence; infinitary combinatorics; cardinal arithmetic; reflection,
  absoluteness, and large cardinals; descriptive set theory; and games and
  determinacy.  Ten body fragments keep the large forcing chapter and its
  catalogs readable while the Part driver preserves that chapter order.
- The Part-6 annex contains twenty-eight items in body order.  Sixteen body
  results are `proved`, twelve are `sketched`, and forty-one are `cited`, for
  sixty-nine statused P6 results.  The twenty-eight proved/sketched results
  form an exact twenty-eight-to-twenty-eight body--annex graph; no cited result
  has an annex item.
- The frozen source's axioms, constructions, ordinal and hierarchy material,
  cardinal/Choice material, constructibility, forcing, and exact CH-status
  chapter are all accounted for below.  Register-driven additions supply the
  missing ordinal/cardinal arithmetic, weak-choice, combinatorial, forcing,
  large-cardinal, descriptive-set-theoretic, and determinacy reference layers.
- All nineteen P6 depth rows are present at their treatment ceilings.  Sixteen
  of the seventeen in-scope P6 new-content rows are delivered; the sole
  remainder is the permitted `could` row `N-a-036`, represented by the one P6
  stub.  All nineteen Phase-4 P6 apparatus artifacts are present; Phase-6 row
  `A-134` is deliberately absent.

## Source and status accounting

The independent source audit mapped twenty-five P6-homed v1.1 result or
argument units statement by statement.  Nine complete source proofs or
complete embedded arguments remain `proved`, twelve source sketches or
conservatively extracted partial arguments remain `sketched`, and four
citation-only imports remain `cited`.  The additional ordered-pair result is
explicitly rehomed to Part 1.  No evidence class was upgraded.

The established one-pass `detex` alphabetic-word method excludes result
statements and proof delimiters.  It was applied only where the source contains
a complete proof or a complete argument that supplies a legitimate
denominator.

| Complete source proof | Source proof lines | Target annex item | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Transfinite induction | 10419--10423 | `annex:p6.ordinals.2` | 33 to 19 | 57.6% |
| Generic-filter existence | 10888--10897 | `annex:p6.force.4` | 75 to 45 | 60.0% |
| Semantic-forcing monotonicity | 11004--11009 | `annex:p6.force.6` | 60 to 31 | 51.7% |
| Relativization of derivations | 11128--11197 | `annex:p6.force.12` | 553 to 237 | 42.9% |
| Positive relative consistency of CH | 11207--11237 | `annex:p6.force.13` | 198 to 93 | 47.0% |
| Nonderivability of CH and its negation | 11301--11312 | `annex:p6.force.15` | 74 to 43 | 58.1% |
| **Total** | -- | -- | **993 to 468** | **47.1%** |

Three complete arguments embedded in source definitions or examples were
extracted into statused body results and annex proofs:

| Extracted complete argument | Source argument lines | Target annex item | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Existence and leastness of omega | 10196--10200 | `annex:p6.axioms.1` | 46 to 27 | 58.7% |
| Foundation excludes self-membership | 10302--10305 | `annex:p6.axioms.2` | 40 to 19 | 47.5% |
| One Cohen real | 11073--11101 | `annex:p6.force.7` | 155 to 92 | 59.4% |
| **Total** | -- | -- | **241 to 138** | **57.3%** |

One faithful compliance pass shortened only the generic-filter, omega, and
Cohen-real annex proofs, the three items whose first measurement exceeded the
upper bound.  Their hypotheses, witnesses, and load-bearing steps remain
present.  No already compliant proof was repeatedly tuned.

The ten explicit source sketches retain `sketched` status and omission notes:

| Source unit | v1.1 lines | Body and annex disposition |
|---|---:|---|
| Set recursion | 10311--10333 | `thm:p06-set-recursion` / `annex:p6.axioms.3` |
| Ordinal trichotomy | 10372--10404 | `thm:p06-ordinal-trichotomy` / `annex:p6.ordinals.1` |
| Transfinite recursion | 10426--10447 | `thm:p06-transfinite-recursion` / `annex:p6.ordinals.3` |
| Hierarchy theorem | 10471--10491 | `thm:p06-hierarchy` / `annex:p6.hierarchy.1` |
| Mostowski collapse | 10537--10557 | `thm:p06-mostowski-collapse` / `annex:p6.hierarchy.2` |
| Hartogs's theorem | 10574--10586 | `thm:p06-hartogs` / `annex:p6.card.1` |
| Choice equivalents and Zorn | 10602--10623 | `thm:p06-zorn` / `annex:p6.choice.1` |
| Constructible class | 10743--10752 | `thm:p06-constructible-class` / `annex:p6.force.1` |
| Strength of the ctm hypothesis | 10790--10824 | `thm:p06-ctm-strength` / `annex:p6.force.2` |
| Arithmetized CH implications | 11280--11292 | `thm:p06-arithmetized-ch-consistency` / `annex:p6.force.14` |

The bounded-absoluteness argument at 10873--10879 and the check-name
calculation at 10923--10938 are embedded partial arguments without canonical
source proof blocks.  They were conservatively extracted as
`thm:p06-bounded-absoluteness` / `annex:p6.force.3` and
`thm:p06-check-name-evaluation` / `annex:p6.force.5`, both `sketched`.  No
compression denominator was manufactured for either item, for any explicit
source sketch, or for any new proof.  The forcing method likewise contains a
mixture of complete local proofs, sketches, cited imports, and new supporting
proofs, so it is not assigned a synthetic chapter-wide ratio.

Four source imports remain citation-only, with no annex item: the rank equation
at 10493--10507 (`thm:p06-rank-recursion`), the constructible-universe scheme
at 10754--10768 (`thm:p06-l-model`), the forcing theorem at 11012--11051
(`thm:p06-forcing-theorem`), and negative CH consistency at 11240--11278
(`thm:p06-not-ch-relative-consistency`), all cited to `Jech2003`.

The complete ordered-pair result at 10283--10299 is not duplicated: it already
appears as `thm:p01-ordered-pair-identity` / `annex:p1.1`.  Seven source
exercises are deliberately retired because the handbook has no exercise
layer: product bounding (10341--10345), Foundation and two-cycles
(10347--10351), ordinal inclusion (10656--10661), rank calculation
(10663--10667), collapse/extensionality (10669--10673), Cohen density and
single-valuedness (11338--11343), and the distinction among semantic truth,
derivability, and relative consistency (11345--11352).  Their substantive
cautions survive in adjacent entries, proofs, and source-disposition
paragraphs.

The remaining forty-four P6 statuses are register-driven additions: seven new
complete proofs (binary K\"onig, the classical fan corollary, the Delta-system
lemma, Cohen ccc, ccc preservation, nice-name counting, and the many-Cohen-real
continuum calculation) and thirty-seven citation-backed statements.  They have
no source-compression denominator.

## Depth rows

Every P6-targeted `must` and `should` row is filled at its registered treatment
ceiling; no depth-row stub is needed.

| Row | Ceiling | Delivered evidence |
|---|---:|---|
| `D-P1-001` | E | Exact Choice-equivalence entry, Zorn statement, and honest `sketched` annex route from Choice through transfinite recursion and Hartogs. |
| `D-P1-002` | T | Master table separates seven full-Choice equivalents from BPI-equivalent compactness forms. |
| `D-P1-003` | S | Cited cardinal-trichotomy equivalence over ZF, explicitly distinguished from choice-free ordinal trichotomy. |
| `D-P1-004` | E | Binary-tree definitions, proved K\"onig lemma and fan corollary, and the explicit ZF route to countable propositional compactness. |
| `D-P1-006` | S | Exact `AC_omega`, `AC_omega^fin`, and DC statements, a cited implication theorem, dependency table, and calibrated diagram. |
| `D-P7-001` | E | Recursive ordinal operations, law/failure table, Cantor normal form, epsilon-zero figure, and distinct induction/recursion theorems. |
| `D-P7-002` | E | Cardinal sum, product, exponentiation, aleph/beth, CH/GCH, and regular/singular reference entry with Choice scope. |
| `D-P7-003` | E | Cofinality definitions, exact family form of K\"onig's theorem, and standard corollaries. |
| `D-P7-004` | S | Cited Easton statement restricted to regular cardinals with monotonicity, cofinality, ground-model, and preservation hypotheses. |
| `D-P7-005` | S | Exact Martin's-axiom convention and cited Suslin-hypothesis consequence; the iteration proof remains a pointer. |
| `D-P7-006` | T | Definitions from inaccessible through supercompact, cited conditional consequences, and a nonexistence-neutral ladder table. |
| `D-P7-007` | E | L\'evy hierarchy, formula-by-formula absoluteness, finite-family reflection, Shoenfield statement, and forcing application. |
| `D-P7-008` | S | Constructible hierarchy, cited condensation and GCH-in-L scheme, exact reflection pointer, and Jensen fine-structure pointer. |
| `D-P7-009` | E | Club, stationary, diagonal-intersection, club-normality, and Fodor entries with regular-uncountable hypotheses. |
| `D-P7-010` | E | Proved Delta-system lemma and Cohen-ccc application, plus exact partition notation and cited Ramsey/Erdos--Rado statements. |
| `D-P7-011` | S | Boolean-valued definition and generic-quotient statement, with product, iteration, and proper-forcing pointers only. |
| `D-P7-012` | E | Complete local Cohen-ccc, ccc-preservation, nice-name, and continuum-counting annex proofs supporting the cited negative-CH import. |
| `D-P7-013` | S | Polish/Borel/projective definitions, exact ZFC regularity boundary, determinacy calibration, table, and hierarchy figure. |
| `D-P7-014` | S | Cited open/closed and Borel determinacy, AD-versus-Choice statement, and conditional projective-determinacy calibration. |

## New-content and exclusion ledger

| Row | Reality in the P6 tree |
|---|---|
| `N-a-035` | Filled at E by cofinality, regular/singular cardinals, K\"onig, Hausdorff recursion, and Easton. |
| `N-a-036` | Open at S.  The sole P6 `\hbstub` names the owed Silver statement; PCF remains only a pointer. |
| `N-a-037` | Filled at E by clubs, stationary sets, diagonal intersection, normality, and Fodor. |
| `N-a-038` | Filled at T by the Delta-system proof and the Cohen-ccc pattern. |
| `N-a-039` | Filled at T by partition notation, the Ramsey table row, and the exact cited Erdos--Rado statement. |
| `N-a-040` | Filled at S by binary K\"onig, cited Aronszajn existence, and the Suslin definition and relative status. |
| `N-a-041` | Filled at S by exact diamond, square, and Martin's-axiom statements and one cited application of each. |
| `N-a-042` | Filled at T by `Add(omega,aleph_2)`, Cohen ccc, cardinal/cofinality preservation, distinct generics, and nice-name counting. |
| `N-a-043` | Filled at S by the permutation/symmetric-model method and the cited basic Fraenkel ZFA model, with pure-ZF transfer explicitly cited. |
| `N-a-044` | Filled at S by the inaccessible--supercompact definitions, measurable ultrapower statement, Scott obstruction, and ladder. |
| `N-a-045` | Filled at T by the L\'evy hierarchy/absoluteness table, reflection, Shoenfield, and a forcing application. |
| `N-a-046` | Filled at E by Polish spaces, Borel and projective pointclasses, Suslin's theorem, and the exact regularity boundary. |
| `N-a-047` | Filled at P by the explicit lightface/effective bridge from Part 4; no substantive effective-DST entry is claimed. |
| `N-a-048` | Filled at S by games, Gale--Stewart, Borel determinacy, AD/Choice incompatibility, and the conditional Martin--Steel pointer. |
| `N-a-066` | Filled at E by ordinal arithmetic, Cantor normal form, induction, recursion, table, and figure. |
| `N-a-067` | Filled at S by L, condensation, GCH in L, an exact pointer to finite-family L\'evy reflection, and the fine-structure boundary. |
| `N-a-068` | Filled at S by the Boolean-valued statement and product/iteration pointers. |
| `N-x-003` | Enforced: proper and iterated forcing, PFA, and MM receive navigation only. |
| `N-x-004` | Enforced: inner/core models and fine structure stop at the L/condensation/Jensen pointer. |
| `N-x-005` | Enforced: PCF stops at the Silver-statement stub and a Shelah pointer. |

## Apparatus ledger

- Tables `A-058` through `A-068` are all present: exact ZFC axioms; system
  variants; ordinal arithmetic; cardinal arithmetic; AC/BPI equivalents;
  theorem-by-theorem choice dependencies; combinatorial principles; the
  conditional large-cardinal ladder; two-sided relative-independence claims;
  exact forcing-poset conventions; and the Borel/projective calibration.
- Figures `A-129`, `A-130`, `A-131`, `A-132`, `A-133`, and `A-135` are present:
  ordinal milestones, the cumulative hierarchy and rank axis, L inside V,
  forcing names/evaluation/extension, the calibrated choice diagram, and the
  Borel/projective hierarchy.  `A-134` remains open because its register phase
  is 6, not 4.
- `A-164` is realized by sixty-seven new P6 symbol rows plus fourteen corrected
  first-use/scope homes in the 371-row registry.  `A-186` is the annotated
  further-reading section at the physical end of Part 6.
- The regenerated P6 audit register contains 143 rows.  These delivery facts do
  not pre-empt global finalization: the CSV rows remain unchanged until the
  campaign's final register-reconciliation pass records actual commit IDs.

## Adversarial correction log

The independent fidelity, standards, and depth passes corrected:

- the three initially overlong complete-proof migrations, in one faithful
  pass only: generic-filter existence, omega leastness, and the Cohen-real
  argument now lie at 60.0, 58.7, and 59.4 percent respectively;
- the R-001 boundary: the ctm presentation remains stronger than bare
  `Con(ZFC)`, the forcing theorem and negative-CH Boolean-valued import remain
  cited, the positive CH and final syntactic nonderivability arguments remain
  local, and one Cohen real is not misreported as a proof of not-CH;
- the Delta-system ccc proof's finite-fiber/domain-map step;
- the ccc-preservation and nice-name proofs: antichains are built below the
  chosen condition, density below that condition is globalized correctly,
  both cofinality inequalities are proved, and the nice-name theorem is stated
  at the exact local scope needed for counting;
- the permutation-model datum, adding atom stabilizers to the normal filter;
- the weaker-choice theorem and diagram, adding the sourced
  `BPI -> AC_omega^fin` arrow while leaving BPI/DC, BPI/AC-omega, and the
  reverse diagonal unasserted;
- the L\'evy hierarchy, separating literal bounded formulas from
  base-theory-equivalent representatives and requiring equivalence in both
  compared structures;
- the coanalytic boundary, separating ZFC analytic regularity, the conditional
  V=L thin-coanalytic example, and determinacy hypotheses;
- the independence, system-variant, choice, forcing, and pointclass tables:
  both relative-consistency directions and base theories are explicit,
  NF carries the current formalization caveat, the collapse row distinguishes
  closure, collapse, cardinal preservation, and cofinality, and no hypothesis
  drifts between columns;
- the forcing-extension figure, giving names and the generic filter separate
  incoming arrows to an explicit evaluation node before values enter the
  extension;
- the exact reflection pointer for `N-a-067`, the placement of `A-186` at the
  end of Part 6, and missing constructibility index tags; and
- the symbol registry and definition-before-use surface: formula/ordinal
  metavariables, tree and binary-sequence notation, Boolean-valued names,
  forcing notation, domain notation, and all fourteen existing-row homes were
  normalized without introducing a second forcing glyph; and
- five page-flow defects found only after the integrated render: scope headings
  now reserve enough following space, the relative-independence heading is
  homed inside its landscape section, blank pages 384 and 524 carry no running
  furniture, and both A-067 landscape pages use corrected widths and suppress
  the stale preceding section mark; and
- the overfull AC-to-Zorn-to-well-ordering-to-product-to-AC annex display,
  split without changing its implication cycle.

## Mechanical evidence

- Integrated TeX Live 2025 `latexmk` build with biber and makeindex: pass,
  571 pages.  The authoritative PDF is timestamped 2026-08-11 10:41:54 and has
  no undefined citation, reference, or control-sequence warning.
- `python tools/check.py --tree handbook --strict`: pass; 371 symbol rows, 352
  distinct glyphs, 382 bibliography entries, 140 proved / 33 sketched / 134
  cited statuses globally, zero malformed statuses, and 30 tracked stubs,
  exactly one in P6.
- P6-specific accounting: 69 statuses (16 proved, 12 sketched, 41 cited), 28
  annex items, one stub, and 143 generated audit rows.
- `python tools/check.py --tree source`: pass; the source file's Git object hash
  is `ea8c2fa647a387817171468199f989b30de6bdf6`, exactly the object at
  `v1.1-verified`.
- `python tools/symbols2tex.py`: pass; 371 rows in ten scope groups.
- `python tools/audit_tables.py`: pass; 143 generated P6 rows and 657 rows
  across all fourteen generated part tables.
- Text-tree `git diff --check`, excluding the tracked binary `main.pdf`, passes;
  `git diff --exit-code -- source` is empty.  The standards scans also find no
  body proof, body-displayed calculus rule, malformed status, forbidden glyph,
  raw cardinality/domain misuse, or unregistered second forcing relation in P6.

## Visual evidence

The authoritative 571-page PDF was rendered and inspected across the P6 title
on physical page 321, its blank verso on page 322, pages 323--394 for the body
and audit register, and pages 513--524 for the P6 annex.  Body content occupies
pages 323--389, the audit begins on page 389 and ends on page 394, and annex
content ends on page 523; page 524 is the blank verso before P7 begins cleanly
on page 525.  The A-164 P6 symbol scope spans pages 48--55, and its boundary
transitions were rechecked on pages 47--48 and 55--56.

The pass covered every P6 table and figure, including both landscape pages of
A-067 on pages 352--353, the A-066 landscape continuation on pages 357--358,
and A-068's transition at page 384.  Body running heads and displays were also
sampled on pages 335--336, and the entire twelve-page P6 annex range was
checked for statement/proof flow and the P6-to-P7 boundary.

The initial render exposed six presentation defects, all corrected and
rerendered: orphaned symbol-scope headings at both sides of the P6 scope; the
relative-independence heading stranded before its landscape table; a running
head on the intentionally blank page after A-068; a P6-annex running head on
the blank verso before P7; a stale preceding-section head on A-067's
landscape continuation; and an overfull AC-equivalence cycle in the annex.
The final pages have no clipped text, overlap, orphaned heading, stale running
head, broken glyph, unreadable table, visible furniture on an intentional
blank, or broken body/annex transition.

The independent source-fidelity/status, standards, depth/content, and visual
reviews are all PASS.  Compilation and rendering establish integration and
presentation, not independent human mathematical review.
