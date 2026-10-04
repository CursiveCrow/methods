# Gelfond--Lifschitz 1988 source-specific authoring record

Unit: `ED26-REQ-N-c-023-01`; parent requirement: `N-c-023`.
Allocation read: the exact `ED26-REQ-N-c-023-01` record in
`spec/coverage/edition-2026/completion-work-queue.jsonl`, including
`N-c-023-C01`, `N-c-023-MAP-01`, and the shared `N-c-023-MAP-04`.
Current common treatment read: `handbook/parts/p09/presentations/n-c-023.tex`.
Applicable contracts read completely: `handbook/CONVENTIONS.md`,
`spec/EDITION-2026-CONTRACT.md`, and
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`.
This is a bounded author return, not independent admission.

## Identified source and exact held body

Michael Gelfond and Vladimir Lifschitz, *The Stable Model Semantics for Logic
Programming* (1988), proceedings pp. 1070--1080, MIT Press,
ISBN 0-262-61056-6. The held source is the complete eleven-page author copy
obtained historically from the archived former first-party PostScript URL,
not an inspected publisher proceedings facsimile. The canonical bibliography
key is `GelfondLifschitz1988`; this intake enriches that existing key rather
than introducing another source identity.

Archive: [capture timestamp 2003-03-31 14:53:08](https://web.archive.org/web/20030331145308id_/http://www.cs.utexas.edu:80/users/vl/mypapers/stable.ps).
Existing acquisition record: `spec/research/p09-source-presentations-lot4.md`,
lines 1039--1119. The record's older completion assertions are historical
evidence, not renewed acceptance. No new network acquisition or live-link
test was performed in this author block.

The complete extracted text was read, and all eleven pre-existing page images
were inspected. Extraction has substantial font-encoding losses; rule symbols,
the source subscript reduct, and the full expansion equations were checked
against page pixels. Page locators below mean one-based author-copy sequence;
they do not assert original publisher page markings.

Held source files are preserved byte for byte under
`source/references/p09-gelfond1988/`. The lead created that exact directory
after this worker's child-path grant did not permit creating the parent entry.
The source also remains at the original `tmp/pdfs/` paths.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `gelfond-lifschitz-1988-stable-model.ps` | 98,568 | `27425678580AC9A1A3E6D460C200586B658B621B3285810AE0CE001697719DF5` |
| `gelfond-lifschitz-1988-stable-model.pdf` | 106,189 | `15F71284CB51E0186739B1798FA3334ECD8B5A397815093DBC62128BE717C3AD` |
| `gelfond-lifschitz-1988-stable-model.txt` | 27,651 | `81F6C41F84B007E3DFEB0BAF9977D0A1C8948ABA00C36C869B63F05B073872CE` |

The directory's JSON manifest records archive identity, file standing and
destinations. These are the already held original source, conversion, and
extraction; no conversion was run in this block.

## Source-to-destination account

Body: `handbook/parts/p09/presentations/n-c-023-01.tex`, label
`sec:p09-n-c-023-01`. Proof annex:
`handbook/annex/p09/n-c-023-01.tex`. Reconstruction is independently worded;
original source syntax `Pi_M`, `S_Pi`, `At`, `th`, and `I(Pi)` is retained.
The role of source negative body literal `neg B` is declared before use and
kept distinct from modern strong-negation head literals and autoepistemic
negation of belief. New explanatory symbols are explicitly editorial and
recorded in the symbol intake.

| Exact source locator | Delivered content and standing |
| --- | --- |
| Section 1, pp. 1--3, programs (1)--(2), sets (3)--(4) | Rule syntax and implication reading; classical versus Herbrand models; source program (2) and its two Herbrand models; minimal versus least model and canonical selection |
| Section 2, pp. 3--4 | All-ground-instance convention, permitted infinite grounding, original two deletions, `Pi_M`, `S_Pi`, fixed-point stable sets, source unique-canonical-model terminology |
| Section 2, Theorem 1 and proof, pp. 4--5 | Original modelhood and subset-minimality result, with full reciprocal annex proof |
| Section 3, p. 5 | Positive-program special case; the positive least-model dependency receives a full proof valid for infinite rule sets with finite bodies |
| Section 3, program (5), pp. 5--6 | All four ground rules, original failed candidate, successful candidate, elimination of the other 60 candidates and the remaining four complete tests |
| Section 3, Remarks 1--3, p. 6 | Source nonstratified comparison standing; its program-specific Prolog observation; game interpretation with identical legal moves |
| Section 3, program (6), pp. 6--7 | Positive-body empty stable model and the full general argument |
| Section 3, p. 7, Remarks 4--5 | All tests of zero/two models; reverse-move addition and both stable models; symmetry and loop-free game qualification |
| Section 4, Theorem 2, pp. 7--8 | Statement attributed by the source to Van Gelder--Ross--Schlipf [15], Corollary 6.2; strict-generality attribution to Examples 6.1--6.2; original cited standing retained |
| Section 4, Corollaries 1--2, p. 8 | Locally-stratified/perfect and stratified/iterated-fixed-point identifications; cited dependency standing and personal-communication boundary outside local stratification retained |
| Section 4, p. 8 | Full-formula stable-expansion equation, objective formula definition, propositional closure (not modal axioms), original program translation and source-cited objective-expansion fact |
| Section 4, lemma and proof, p. 9 | Full rulewise equivalence under the same introspective assumption set, for arbitrary candidate formula set E; reciprocal annex proof |
| Section 4, Theorem 3, pp. 8--9 | Exact unique-model theorem, existence and uniqueness calculations, express Halina Przymusinska attribution; reciprocal annex proof |

The objective-expansion fact is cited by Gelfond--Lifschitz to [8] (Marek,
unpublished note, 1986) and [6] (Konolige, 1987); this author block does not
claim to have acquired either prior proof. Instead it supplies an explicitly
editorial proof of the exact needed fact. Structural recursion replaces each
`LG` by true/false according to whether the objective theory entails the
already reduced proper subformula `G`. The proof shows valuation equivalence,
the complete expansion equation, conservativity, finite-modal-depth uniqueness,
and the inconsistent-theory boundary. It therefore establishes the dependency
rather than restating stable-expansion existence as an assumption.

The general model--expansion bijection is a separately labeled derived
corollary, not falsely reported as the original wording of Theorem 3.
The warning about the objective kernel is important: it is the objective
consequence theory, not the full classical truth set of the least model.
For `A={p}` with independent `q`, the expansion has `not Lq`, but neither
`q` nor `not q`. The formal full-formula proof respects that boundary.

## Actual author-level component states

`N-c-023-MAP-01`: source-specific writing supplied. Original definition,
positive recovery, minimality, complete zero/one/multiple-model calculations,
source terminology, source comparisons and actual proof boundaries, and the
full required autoepistemic argument are present. This is authored content
awaiting lead routing and independent admission, not a renewed terminal state.

`N-c-023-MAP-04`: the 1988-source subextent is supplied: candidate reduct
verification, infinite versus finite grounding, compact-source versus explicit
ground input, fixed function-free program versus data size, brave/cautious
task definitions and vacuity, default/strong-negation distinction, and the
fresh-fact/positive-loop task reductions. Later normal/disjunctive complexity
and the uniform-NP compilation are explicitly not attributed to 1988.
Their common/source-specific later treatments remain distinct shared
dependencies; this author return does not claim those full proofs have been
completed or close the whole shared component. In particular the existing
common treatment's general NP compilation and disjunctive-hardness citation
boundary are not repaired by this proof of the autoepistemic dependency.

`N-c-023-C01`: the Gelfond--Lifschitz source facet is authored subject to those
shared-component and production boundaries; no canonical queue/coverage state
was edited by this worker.

Seven body results have seven reciprocal full-proof annex items:

1. `thm:p09-gl88-positive-closure` / `annex:p9.n-c-023.1.positive-closure`.
2. `thm:p09-gl88-theorem1` / `annex:p9.n-c-023.1.theorem1`.
3. `thm:p09-gl88-positive-body` / `annex:p9.n-c-023.1.positive-body`.
4. `thm:p09-gl88-objective-expansion` / `annex:p9.n-c-023.1.objective-expansion`.
5. `thm:p09-gl88-expansion-reduct` / `annex:p9.n-c-023.1.expansion-reduct`.
6. `thm:p09-gl88-theorem3` / `annex:p9.n-c-023.1.theorem3`.
7. `thm:p09-gl88-correspondence` / `annex:p9.n-c-023.1.correspondence`.

## Scope, evidence and remaining integration

Only the assigned new presentation, annex, bibliography intake, symbol intake,
source directory and this note are within this worker's write scope. No common
treatment, shared driver, style, canonical bibliography/registry, generated
file, coverage queue, or admission record was edited.

The current manuscript was read back after authoring, and the exact mathematical
dependencies were checked directly in the derivations. This is author checking,
not an independent review. No new manuscript render, build, prose test or
independent review was run; that follows the assignment's batch sequence.
No substantive step is knowingly left unresolved in the supplied Theorem 1,
objective-expansion construction, expansion--reduct lemma, or Theorem 3.
Their correctness and source fidelity remain subject to the required fresh
independent review contexts.

Lead integration remains to add the body and annex inputs to their shared
routes, reconcile rather than duplicate the common autoepistemic summary,
deduplicate/enrich the existing bibliography key, merge the symbol rows,
register lookup targets, and preserve the distinction between this completed
author argument and the later-source shared proof boundaries. Then the full
consolidated independent, static, build and visual gates remain due.

The original source body's previous missing-source finding must not be
revived. A publisher-specific facsimile/typography claim remains unsupported;
the qualified archived author presentation is the actual content authority.
