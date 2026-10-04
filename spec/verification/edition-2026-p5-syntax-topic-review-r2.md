# Edition 2026 P5 syntax: bounded topic recheck R2

Date: 7 September 2026. Role: independent topic reviewer returning to the
previously filed P5-TOP-01 finding. Scope: the three-line rationale repair and
its exact syntactic hierarchy prerequisite.

## Verdict

**PASS. P5-TOP-01 is CLOSED.** The revised explanation correctly derives the
Sigma1 classification of the exact chosen formula
`Prov_T(x) = exists p Proof_T(p,x)` from closure under unbounded existential
quantification. It imposes no unproved prefix-shape requirement on the chosen
Sigma1 numeralwise representative.

The original review's PASS findings for the syntax construction, annotated
ND checker, certified axiom leaves and both standard-model proof-relation
directions retain their original scope and dependency identities. The original
localized rationale failure is now closed. The separate cited Q representation
theorem, internal derivability obligations, source acquisition, formal
admission, build, visual production and release gates acquire no additional
acceptance from this bounded recheck.

## Current read evidence

| Artifact | Actual read scope | SHA256 |
| --- | --- | --- |
| `handbook/restoration/inherited-09328-09438.tex` | Lines 471–496; total file length independently checked as 519 lines | `0e4ac6ad0d39474e49d2f868c62877fd7a0f1f1eec61e24d77d806e266d81b9c` |
| `handbook/restoration/inherited-08306-08438.tex` | Lines 1–133, full; governing hierarchy at 61–94 | `0b020970be72999cd771566ba0d6cdb4e4668728362cbd3c0d1606059ee9d2b8` |
| `spec/verification/edition-2026-p5-syntax-topic-review.md` | Previously authored and completely read back in R1; report identity rehashed for this recheck | `ddb2174a463c07fc3b77c2c67f60029e48fd656081f613b59a2d0eb8a60f1d25` |

Paths are relative to `C:/Dev/the-methods-of-reason`. The hierarchy prerequisite
matches the identity in the original topic review.

## Mathematical verification

Current P5 lines 477–480 choose a Sigma1 formula numeralwise representing the
constructed numerical relation in Q. Line 482 forms its existential closure
in the proof-code argument. The repaired lines 484–486 state:

> The declared Sigma1 class is closed under unbounded existential
> quantification, so Prov_T is a Sigma1 formula by
> the syntactic hierarchy definition.

The quoted passage renders the source's mathematical macros in plain text.
The actual hierarchy at `inherited-08306-08438.tex:79–82`, with n=0, defines
the Sigma1 class in negation normal form to be closed under unbounded
existential quantification. Lines 88–93 extend the classification to an
arbitrary formula through its fixed negation-normal-form conversion. Applying
that conversion to an outer existential retains the existential and converts
its matrix; it does not require moving a quantifier across a connective or a
marked bounded quantifier. Thus the selected Sigma1 matrix gives a Sigma1
existential closure, regardless of its initial constructor.

The R1 example `(0=0) and rho_0(p,x)` is now covered directly: its outer
existential belongs to the same closure class even though the representative
begins with a conjunction. No literal prefix merge or arithmetic equivalence
to a chosen prenex formula is claimed. The distinction between syntactic
classification and truth in the standard structure is preserved.

The unchanged text at P5 lines 490–493 still attributes numeralwise Q
representation to the cited theorem and explicitly leaves internal derivability
conditions outside the standard-model checker construction.

## Exact change isolation

The reviewer read the current source bytes, decoded and re-encoded them as
strict UTF-8, and checked that the round-trip SHA256 was the current hash
above. The exact revised three-line rationale occurred once. In memory only,
the reviewer replaced that occurrence with the original three lines:

```tex
The additional existential quantifier merges with the initial existential
block of the chosen representation, so \(\mathsf{Prov}_T\) is a
\(\Sigma^0_1\) formula by the syntactic hierarchy definition.  The
```

The reconstructed bytes had SHA256
`87c2203ae4f94d78b973b592c9ca88013e7ef0641410e512b45c79a680ab9903`,
exactly the original 519-line reader snapshot reviewed in R1. This verifies
that reversing only the rationale recovers that complete source identity.
The reconstruction was never written to the manuscript or another file.

No other new review was read. No manuscript, dependency, registry or
provenance file was edited, and no tests, builds, renders, acquisitions or
delegation occurred. The sole output of this recheck is this new report.
