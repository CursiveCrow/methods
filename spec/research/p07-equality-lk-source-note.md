# Exact equality-LK adequacy and its negative Cut result

Authored 1 October 2026 local date, beginning at 03:19 UTC on 2 October.
Scope: the literal current `handbook/registry/calculi/lk-eq.tex`, not a
substituted analytic equality calculus. This is mathematical authoring of
the gap identified by Chapter 282, not an independent review or admission
wave. The research skill supports this one source/dependency record; this
writer is the already delegated background investigator and spawned no child.

## Delivered files and ownership

- `handbook/parts/p07/equality-lk-metatheory.tex`:
  `sec:p07-equality-lk-metatheory`, one exact-domain definition, seven
  proved result statements and the explicit Cut warning.
- `handbook/annex/p07/equality-lk-metatheory.tex`: the seven reciprocal
  complete proof items `annex:p7.eqlk.alpha`, `.replacement`, `.congruence`,
  `.soundness`, `.nd`, `.completeness`, `.cut-failure`.
- `handbook/bib/intake-p07-equality-lk.bib`: comments only; existing
  Enderton2001 and Mendelson1997 citation identities are reused. No new
  external source manifestation is asserted.
- `handbook/registry/symbols-intake-p07-equality-lk.csv`: the exact LK-equality
  identity, reused finite-support disjunction, local counterexample constants,
  and proof-variable transposition roles are explicitly scoped.
- This single note retains the mathematical dependency record, concrete
  boundary and root-owned consumer edits. No shared sheet, driver, canonical
  file, earlier proof or Chapter 281 file was changed.

## Exact source surface and read dependencies

The controlling presentation is the existing sheet: contexted Id and falsum;
two-sided finite multiset contexts; primitive negation; the shared-context
implication-left rule; four total capture-avoiding quantifier rules with
their current free-variable eigenfreshness; Cut; positive-multiplicity Mix;
empty-context reflexivity; and the sole oriented left equality replacement.
Its 22 rule entries were read in full. Symmetric replacement is only derived
with Cut and is not a hidden primitive rule.

The inherited authority's corresponding exact interval is
`source/formal-logic-reference.tex:04062–04108`, maintained through
`handbook/restoration/inherited-04062-04108.tex` and its scope wrapper.
Its actual symmetry derivation already uses Cut. The authoring retains it,
adds its missing global metatheory and proves the negative admissibility
claim rather than silently editing that source surface.

Other actual materials read:

| Material | Exact mathematical dependency used |
| --- | --- |
| `handbook/registry/calculi/lk.tex`, `lk-defneg.tex`, `nd-fol.tex` | The canonical/shared-context versus defined-negation/split-context distinction; every ND rule, nonvacuous discharge, explicit alpha conversion, total instances and exact existential absence wording. |
| `handbook/restoration/inherited-03240-03428.tex` | Deterministic total capture-avoiding substitution and the least alpha-equivalence relation; `def:p02-fol-capture-avoiding-substitution`, `def:p02-fol-alpha-equivalence`, `lem:substitution-complexity`. |
| `inherited-03429-03518.tex`, `inherited-03519-03680.tex` | Nonempty structures, actual identity, total term evaluation; `lem:term-substitution`, `thm:fol-substitution`, `lem:fol-coincidence`, `cor:alpha-invariance`. Their substitution proof explicitly handles stopped, commuting and renamed quantifier binders. |
| `inherited-03927-04061.tex`, `inherited-04109-04213.tex` | Actual ND equality and quantifier rules; inherited soundness `thm:fol-soundness`, `thm:fol-lk-soundness`. |
| `inherited-04576-04712.tex`, `inherited-04713-04920.tex` | The actual equality-congruence quotient term model, `lem:equality-congruence`; full identity ND completeness `thm:fol-completeness`; complete countable-signature, no-Choice corollary `cor:fol-completeness-countable`; inherited LK completeness retains its translation-sketch boundary. |
| `handbook/parts/p02/first-order-calculi-supplement.tex` and current annex equality laws | Existing `thm:p02-equality-laws` concerns ND, not a Cut-free LK equality metatheorem. |
| `handbook/parts/p07/calculi-and-derivability-supplement.tex`, `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex` | Complete equality-free canonical ND bridge and finite-sequent completeness; actual finite-support succedent convention `def:p07-sequent-nd-translation`; their equality-free scope remains explicit. The new proof supplies the identity cases and freshening directly. |
| `handbook/parts/p07/classical-cut-elimination.tex`, matching annex, `spec/research/p07-classical-cut-source-note.md` | The supplied defined-negation Cut construction excludes equality. Gallier's LK and separate NNF equality calculus are not this sheet; no external equality Cut theorem is imported. |
| `spec/research/p14-classical-calculi-source-note.md`, `handbook/parts/p14/classical-and-constructive-calculi.tex` | Chapter 282's exact gap and current equality/Cut qualification, rather than an old missing-proof claim inferred only from a filename. |
| `spec/registers/depth-gaps.csv:29,74` and the exact `requirements-units.jsonl` record | D-P3-011's explicit symmetry/transitivity/function/relation congruence and actual-calculus equality-axiom goal; D-P8-001's sequent-completeness context. The source allocation is the named handbook mathematical goal, not an invented whole external book extent. |

Read-time dependency SHA-256 values (not claims about a future integrated tree):

| File | SHA-256 |
| --- | --- |
| `handbook/registry/calculi/lk-eq.tex` | `68caacaf82d2a505c2546f8f5a6aae204164c38d03a7a4ef67e215c3d36ca1d0` |
| `handbook/registry/calculi/lk.tex` | `09b0b81140bfb93431d88ba78b7de1cd6579987efbb38770eaecdbe8eed7d406` |
| `handbook/registry/calculi/nd-fol.tex` | `f25549bc18fc4aae212eea32cadc9fffd08e03d712f5df10e9da62f660be5370` |
| `handbook/parts/p07/calculi-and-derivability-supplement.tex` | `ccf4b949837a32969103c4589dd86f652a37440203e5d0418ca97942ff6d848b` |
| `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex` | `c9e42c111b0d8955ef8ffce3facaba702c7e44e8f5b04539ba0165e19d751298` |
| `handbook/parts/p07/classical-cut-elimination.tex` | `5af33fd7fbe212dc73110dcb8e4e0d0264240ffb5a35832530ad1f9e452b12f6` |

## Source-to-new-result record

These are new local proof constructions for the named literal calculus,
not reproductions of an external source's differently named presentation.
The body gives each statement; the matching annex carries its full proof.

| Body result | Reciprocal annex item | Construction and dependency boundary |
| --- | --- | --- |
| `thm:p07-eqlk-alpha` | `annex:p7.eqlk.alpha` | Native Cut/Mix-free kernels for atomic identity, falsum, negation, conjunction, disjunction, shared implication, both quantifiers; finite canonical binder freshening justifies opened alpha matrices. Occurrence conversion after the kernel uses Cut explicitly. |
| `thm:p07-eqlk-replacement` | `annex:p7.eqlk.replacement` | Literal primitive-left kernel, inherited single-Cut symmetry, reverse/right kernel and opposite-oriented left premise transformation. Fresh hole variable is only needed for the auxiliary symmetry formula; arbitrary original substitution variables and zero/multiple occurrences remain licensed. |
| `thm:p07-eqlk-congruence` | `annex:p7.eqlk.congruence` | Transitivity; one finite Cut stage per function/relation argument; both relation directions; exact nullary cases; contraction/weakening restore prescribed multiplicities. |
| `thm:p07-eqlk-soundness` | `annex:p7.eqlk.soundness` | Every one of the 22 sheet rule entries has an explicit counterevaluation/assignment proof. Actual substitution and coincidence dependencies are named, including all binder/capture cases and the eigenvariable-equals-binder case. |
| `thm:p07-eqlk-nd` | `annex:p7.eqlk.nd` | Complete LK-to-ND and ND-to-LK proof-tree constructions for all structural, logical, quantifier, alpha and equality rules; finite supports/disjunction association; empty succedent; nonvacuous discharge detours; duplicated retained occurrences; proof renaming without an induction call on a larger source proof. |
| `thm:p07-eqlk-completeness` | `annex:p7.eqlk.completeness` | Reduce each finite sequent to its finite nonlogical signature; expand any smaller nonempty model using one element for all unused functions and empty relations; use the actual no-Choice identity ND theorem and the newly proved translation. No Cut-elimination or equality-free completeness premise is used. |
| `thm:p07-eqlk-cut-failure` | `annex:p7.eqlk.cut-failure` | One essential Cut between two Cut/Mix-free premises; the complete backward atomic invariant; every initial and possible rule excluded; variable-only variant; negative Mix and Cut-free-completeness conclusions. |

### Exact negative derivation

For distinct constants a,b and a fresh variable z:

1. Id: `b=a ⇒ b=a`.
2. Existing `=L`, with r=a, t=b and auxiliary formula b=z:
   `a=b, b=b ⇒ b=a`.
3. Existing reflexivity: `⇒ b=b`.
4. A single Cut on b=b between 3 and 2: `a=b ⇒ b=a`.

Both inputs to that Cut are Cut/Mix-free. The root is valid but cannot
be derived without those rules. Reading a putative free proof backward,
every sequent can only have a=a/a=b antecedent atoms and b=a succedent
atoms, with repetitions or empty contexts. Weakening deletes and contraction
duplicates; a logical principal conclusion is impossible. For equality
replacement, its displayed equality is a=a or a=b. The first changes
nothing. For the latter, a replaced output a=a has no hole; a replaced
output a=b comes from either a=b or a=the-hole and becomes a=b or a=a
backward. No function application or other constant disappears under
substitution. No identity, falsum or reflexivity leaf has this shape.
The annex proves the same literal shape argument for two free variables,
including a hole variable equal to either of them.

The existing sheet is therefore sound and complete **with Cut**, but
Cut/Mix elimination is false for it. There is no need to modify its
primitive rules for the positive adequacy theorem. A right replacement,
reflexivity-deletion or other analytic equality extension would be a new
surface, not a repair silently made in this task.

### Two literal interface details retained by the new proof

The deterministic total substitution can rename a binder even when its
hole variable has no free occurrence, if that binder occurs in the inserted
term. Zero-hole instances therefore need not be literally the same string.
The new kernels use the registered literal instances; no false literal
identity is used to simplify them.

LK eigenfreshness is free-variable absence, whereas ND existential
elimination says the eigenvariable is absent from the conclusion, surviving
assumptions and existential formula. A direct conversion need not meet that
stronger wording when the LK eigenvariable occurs bound in a context.
Concrete case: the legal LK `exists-L` step from
`forall y P(y), Q(y) ⇒ forall y P(y)` to
`forall y P(y), exists x Q(x) ⇒ forall y P(y)` (x distinct from y)
has eigenvariable y free-absent in its conclusion, but y occurs bound in
the ND conclusion `forall y P(y)`. The new translation first transposes y
with a variable absent from the already translated finite ND proof and
original conclusion, proves substitution covariance up to alpha, converts
surviving assumptions back, then applies the ND rule. It does not recursively
translate a larger, newly cut proof and does not assume a blanket proof
substitution result without constructing it.

## Root-owned integration and consumer targets

Route the new P7 body and matching annex, then merge the four scoped symbol
rows. The bibliography intake adds no key. Preserve the original equality
sheet and inherited symmetry derivation; no primitive sheet correction is
requested. Consumer text should report proved cut-admitting adequacy and
proved negative Cut/Mix admissibility, not merely an unknown transfer.

Concrete current consumers:

- `handbook/parts/p14/classical-and-constructive-calculi.tex`, the
  “Equality-bearing sequents” paragraph at the current line 291: link
  `thm:p07-eqlk-completeness` and `thm:p07-eqlk-cut-failure` and replace
  its outstanding-construction qualification by the actual new results.
- `handbook/parts/p07/calculi-and-derivability-supplement.tex`, the equality
  catalog row near current line 253: its local “no ... theorem added here”
  qualification must not imply the new result is absent from the live book.
- `handbook/registry/calculi/lk-eq.tex`, descriptive comments/identity/Mix
  prose: keep every rule untouched; root may add the proved negative-result
  pointer where it currently only says that other proofs do not establish
  admissibility.
- `handbook/parts/p02/first-order-calculi-supplement.tex`, equality paragraph
  near line 38: its symmetry-with-Cut statement stays correct; an added
  link may distinguish the new complete sequent metatheory from ND laws.
- `handbook/parts/p14/directory-of-logical-systems.tex`, first-order profile:
  no existing false Cut claim was found there; root may add the new exact
  adequacy/negative-boundary references without changing the profile's scope.
- `handbook/annex/p07/calculi-and-cut-elimination-supplement.tex`, old
  canonical bridge's `exists-L` translation wording: the concrete bound-y
  case above requires the same freshening step; the new annex supplies it.
  This task did not edit that root-owned upstream proof.

## Verification standing

The author read the actual sheet and dependencies, checked each proof against
the actual rule directions, and re-read the new body/annex. The counterexample
is a general finite-tree exclusion argument, not a bounded search or a
confidence judgment. The alpha, substitution, stronger-absence, shared-context,
empty-context and repeated-occurrence points are treated in the proofs.
At the 03:48 UTC author checkpoint the body had 144 lines and the annex
553 lines. Read-only declaration reconciliation found all 20 reference
identities, and each of the seven body `proved=` statuses had its exactly
matching reciprocal annex item. The two cited keys already exist canonically.
These are source/declaration navigation checks, not a proof verifier or
independent acceptance result.

No child, independent review, consolidated check suite, manuscript build,
render, source-page recreation or prose test was performed. These proofs
are authored results with their explicit reciprocal `proved=` records;
independent admission and integration are not claimed.
