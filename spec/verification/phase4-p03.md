# Phase 4 verification: Part 3

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-11
Visit: P3, Model Theory
Verified source: `v1.1-verified`, Part IV, lines 6049--7493; the live
`source/` tree is unchanged.

## Delivered scope

- Body: maps and elementarity; diagrams and elementary chains; types,
  saturation, homogeneity, filters, ultraproducts, and Los's theorem;
  quantifier elimination, categoricity, back-and-forth, and EF games; prime
  and atomic models; indiscernibles, stability, simplicity, NIP, and
  o-minimality; finite model theory; preservation theorems; Robinson joint
  consistency; and Lindstrom's characterization.
- Annex: nineteen items in exact one-to-one correspondence with eighteen
  `proved` and one `sketched` body results.
- Result inventory: thirty-nine statused results -- eighteen `proved`, one
  `sketched`, and twenty `cited`.
- Tier-1 methods: Los and back-and-forth, each with an exact body method entry,
  statused theorem, and complete annex proof.
- Apparatus: A-040, A-041, A-042, A-043, A-044, A-122, and A-162.
- Integration: the Part-3 body and annex drivers input all six body fragments
  and all three annex fragments; the body driver ends with the generated P3
  audit register.

## Source and evidence accounting

All twenty-four status-bearing Part-IV results were checked against the
repaired source: seventeen complete proofs remain proved, the sole source
sketch remains sketched with an omission note, and all six cited theorems
remain citation-only.  The eighteenth proved result is the new complete
compactness-via-ultraproducts derivation required by D-P4-004.  No evidence
class was upgraded.

The established `detex` alphabetic-word check records these final migrated
proof or sketch ratios:

| Fragment | Annex items | Final ratios |
|---|---|---|
| Maps and elementarity | `p3.maps.1`--`.6` | 56.5%, 40.0%, 45.2%, 43.2%, 56.7%, 43.5% |
| Types and ultraproducts | `p3.types.1`--`.7` | 43.3%, 50.4%, 48.4%, 58.6%, 57.4%, 54.0%, 54.2% |
| QE and categoricity | `p3.qe.1`--`.5` | 47.3%, 60.0%, 60.0%, 44.8%, 58.6% |

Every migrated proof or sketch lies in the required 40--60% band.  The new
compactness-via-ultraproducts proof is not assigned a source-compression ratio.

## Repaired-source fidelity

- R-015: the model-completeness reduction factors an arbitrary embedding
  through its image and transports elementarity back through the isomorphism.
- R-016: back-and-forth begins with an arbitrary prescribed finite partial
  isomorphism and the resulting isomorphism extends that starting map.
- R-028: compactness of type spaces performs the complete-type completion
  step after first-order compactness supplies consistency.
- R-029: saturation-to-homogeneity explicitly establishes finite
  satisfiability, invokes compactness, and applies saturation at the stated
  cardinal bound.
- R-036: the labeled theorem invokes the explicitly assumed Ultrafilter Lemma
  for the extension step and retains the Frechet-filter verification,
  finite-set induction, and nonprincipality characterization.  The research
  ledger was corrected after a reviewer mistakenly described the frozen
  source as reproving the Ultrafilter Lemma by Zorn.
- R-030: the DLO construction retains all four interval cases: two bounds,
  lower only, upper only, and no bounds.

## Depth rows and apparatus ceilings

Filled at their registered ceilings: D-P3-005 and D-P4-001, D-P4-002,
D-P4-003, D-P4-004, D-P4-005, D-P4-007, D-P4-008, D-P4-009, D-P4-010,
and D-P4-012.  D-P4-006 and D-P4-011 are `could` rows and remain honestly
open behind explicit row-named `\hbstub` entries.

A-040 and A-041 give the language-sensitive first-order-theory and QE
catalogs; A-042 separates the preservation theorems and their semantic
operations; A-043 defines and compares the classification-theoretic dividing
lines; A-044 records finite-model results and unrestricted contrasts; A-122
is a fixed-round EF board with its nonproof limitation stated; and A-162
places the registered model-theory notation in a lookup table without
reassigning the Kleene-equality glyph.  Registers remain unchanged until
global Phase-4 reconciliation.

## Adversarial correction log

The independent source, spec, and standards reviews corrected:

- source accounting from two to all three retained map examples;
- parameter-expansion standing and the noninterchangeability of atomic and
  elementary diagrams;
- the exact P2 regular-abstract-logic closure package used by Lindstrom's
  theorem;
- the discrete finite type-space conclusion, order-indiscernible tuple
  arities, and the parameters and ambient structures in dividing and forking;
- the exact local-character quantifiers for simple theories and the intended
  countable random graph, IP, RCF, and fixed-characteristic ACF usages;
- constants in ultraproduct well-definedness and the membership/upward-closure
  steps in the compactness-via-ultraproducts proof;
- an undefined source-only `\Th` macro, replaced by the handbook's explicit
  `\operatorname{Th}` notation;
- the ACF categoricity status citation, changed to the verified primary
  `Steinitz1910` record while retaining Marker as modern exposition;
- the zero--one-law scope, restricted to finite positive-arity relational
  vocabularies, and the repetition/order cases in the EF parity strategy;
- definition-before-use cross-references in A-162 and ambiguous/redundant
  headings in A-040; and
- a stale bibliography-intake count and an inaccurate R-036 sentence in the
  research ledger.

The final verifier's remaining one-word ratio overrun was corrected before
the integrated build.  No additional polishing or recompression was done.

## Mechanical and visual evidence

- Integrated TeX Live build with biber and makeindex: pass, 385 pages; biber
  resolved 79 cited keys.
- `python tools/check.py --tree handbook --strict`: pass; 202 symbol rows,
  338 bibliography entries, 106 proved / 10 sketched / 55 cited globally,
  zero malformed statuses, and 34 remaining tracked stubs, two in P3.
- `python tools/check.py --tree source`: pass.
- `python tools/symbols2tex.py`: pass; 202 rows and 199 distinct glyphs.
- `python tools/audit_tables.py`: pass; 90 generated P3 audit rows.
- `git diff --check`: pass; `git diff -- source` is empty.
- The integrated log contains no undefined citation, reference, or control
  sequence.
- Visual inspection of the actual integrated PDF covered A-040, A-041,
  A-042, A-043, A-044, A-122, A-162, and every P3 annex page.  No clipped
  text, collision, unreadable table, malformed figure, or broken page flow
  was found.

Compilation and visual inspection establish integration and presentation,
not mathematical correctness.  Source fidelity, new-content evidence,
status preservation, standards, and rendering were checked separately above.
