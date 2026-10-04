# Constructible-hierarchy foundations: independent publication-text review

Date: 8 September 2026 UTC. Reviewer:
`/root/constructible_foundation_publication_review`.
Started at 08:09:11 UTC; maximum return time 08:54:11 UTC.

## Standing

The complete new body and all eight annex proofs have been read directly
in LaTeX. No actionable defect has been identified in that text. The final
verdict remains pending the integrator's exact route/correction delta and
canonical notation plus generated-view snapshot. No other reviewer's
conclusions were read, and no manuscript content, source record, shared
registry, or driver was edited by this reviewer.

This review concerns publication text and its specified navigation. It is
not a manuscript build, page inspection, source acquisition, formal
admission, or acceptance of the whole constructibility presentation.

## Exact reading

Both governing files were read completely:
`handbook/CONVENTIONS.md`, 251 lines, SHA256
`4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`;
`spec/EDITION-2026-CONTRACT.md`, 168 lines, SHA256
`C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`.

| File | Entire extent read | SHA256 |
| --- | --- | --- |
| `handbook/parts/p06/constructible-hierarchy-foundations.tex` | Lines 1-220 | `64E22FE49017819108160AF5C291E8507A94D4751C2D452EF2DBA8DE6F0E1B95` |
| `handbook/annex/p06/constructible-hierarchy-foundations.tex` | Lines 1-587, including all eight complete proofs | `4D13EF83F571C7D61BCBD25B0AAF07EA1A0EA4840D3152ED738FB2D7CFFBA43C` |
| `spec/research/edition-2026-p06-constructible-hierarchy-foundations.md` | Lines 1-142 | `25F1B623CFBB04FFA2FB91BE531639637F78E3D34701609011165FABAADDA7DF` |
| `handbook/restoration/inherited-00603-00647.tex` | Lines 1-45 | `B76C0E5AEE32C23E036F59F780A99690C9788636444A4456B8E6762A3307B795` |
| `handbook/restoration/inherited-03519-03680.tex` | Lines 1-162 | `B1F502609BB084ACFF222A7431E05CAED5273ACD19C367B45CBDCCB63F306897` |
| `handbook/restoration/inherited-10089-10271.tex` | Lines 1-183 | `6E8EB080C5FC4C5D359798C48AFFB7692ACE514F702DABF643003AE57FFF4B29` |
| `handbook/restoration/inherited-10272-10352.tex` | Lines 1-81 | `0FC1DB84F232FDC88F0860164281D9F0F1182565B6D510F376DE90E0F016A0F3` |
| `handbook/restoration/inherited-10353-10451.tex` | Lines 1-99 | `6B0A7785FADE6927950AD97D90EC2B24FC90A335B7673AC0A3B75F6E6C791008` |
| `handbook/restoration/inherited-10452-10520.tex` | Lines 1-69 | `EF5058570C685B60C04893267C8F57B4BFF5E214E344E0BF51DCF30DF347DFF4` |
| `handbook/restoration/inherited-10675-10769.tex`, before integration correction | Lines 1-104 | `B745B19A1B07592A4CD59FEC1791B3102E88B3C53E30F276C06CA168EBC1D57A` |

The complete pre-integration `handbook/parts/p06.tex`,
`handbook/annex/p06-route.tex`, and `scope-SRC-10675-10769.tex` were also
read. Targeted reads of `handbook/handbook.sty` covered the result/plain
environment implementations and their source-environment counterparts.
The bibliography record for `Jech2003` was read as attribution metadata;
the book's actual body was not available or read and is not treated as
the authority for the new proofs.

## Complete promise audit

The following suffixes form reciprocal pairs with `thm:p06-` in the body
and `annex:p06.` in the annex. All eight status tokens promise a full
proof, and each corresponding proof was read to its end.

| Suffix | Body opening | Annex extent | Result of the text examination |
| --- | --- | --- | --- |
| `ordinal-foundation-facts` | 37 | 3-113 | Supplies ordinal membership and comparison before using them, both inclusions in the proper-subordinal argument, the bounded-predicate equivalence, successors, set unions, limit facts, and the required properties of omega. |
| `definable-ordinal-recursion` | 72 | 115-204 | Supplies the fixed approximation formula, bounded least-disagreement argument, restriction graphs, successor extension, the exact Replacement domain at a limit, compatibility, class definability, arbitrary set restrictions, and uniqueness as a definable-class scheme. |
| `set-sized-definability` | 125 | 206-364 | Bounds pairs, records, lists, and assignments by actual power sets; gives all nine truth-set clauses; obtains finite computations from the proved recursion theorem; defines a guarded uniform satisfaction formula; proves both formula/code translations and finite-parameter equivalence; treats the empty argument separately. |
| `bounded-transitive-absoluteness` | 151 | 366-396 | Covers atomic, Boolean, existential bounded, and universal bounded clauses. The bounding set retains its value because the variables are distinct. Transitivity identifies the internal witness range with the ambient range. No internal ZF assumption appears. |
| `def-transitive-growth` | 166 | 398-417 | Gives the actual formulas defining the whole input and each member of a transitive input; establishes the two inclusions and transitivity; explicitly includes the empty argument. |
| `hierarchy-recursion-existence` | 181 | 419-470 | Gives total operations for L and V, disjoint ordinal cases and predecessor uniqueness, a set range at limits, and the expanded first-order constructibility formula. |
| `constructible-level-height` | 194 | 472-569 | Gives separate inductions for transitivity, inclusion, exact ordinal height, and comparison with V. The successor height step actually defines the previous ordinal using the bounded formula; the zero case uses Def(empty). Reverse height inclusion, limit equality, and strict successor growth are all supplied. |
| `constructible-class-foundation` | 213 | 571-587 | Derives transitivity and containment of every ordinal from the level theorem. Assuming L is a set, Separation forms its ordinal subset and the union-of-ordinals argument yields the explicit Foundation contradiction. |

## Dependency, typing, and attribution examination

The chapter declares class notation to be formulas with set parameters
before its first class-function use. The recursion's operation symbol G
records one fixed functional formula; it is not an additional quantified
class parameter. The limit construction collects approximations only over
the current set ordinal. Every later use of the recursion theorem has
set-valued branches and a fixed formula definition.

The instruction table distinguishes variable-index fields from references
to earlier positions. The concatenation proof shifts only position fields,
and the parameter argument explicitly handles a bijective variable
renaming. Assignments are members of the set A^omega. A single element
of a given nonempty A supplies a constant assignment, so no choice
function on a family of sets is required. Satisfaction uses a set A,
a code c, and an assignment s; it is never applied to the universe.
Def(empty) is the explicit singleton of the empty subset, and the
satisfaction branch is guarded by nonemptiness.

Ordinalhood is represented by the displayed bounded formula only after
its equivalence to the original transitive strict-well-order definition
has been proved in ambient ZF. The absoluteness argument consequently
does not need a level L_alpha to satisfy ZF. The successor-height proof
uses this exact distinction. Growth uses A subset Def(A) for each
transitive A; it does not infer general monotonicity of Def between two
different transitive inputs.

The actual earlier transfinite-induction proof and the stated axioms are
used. The older ordinal, recursion, general membership-recursion,
hierarchy, and rank sketches do not supply omitted proof steps here.
The comparison with V uses only its newly established existence and
recursion clauses. The final paragraph retains separate obligations for
axiom relativization, a definable well-order, condensation, and GCH.
The new derivation is presented as a deduction from the stated ZF
axioms, with its own complete proof destinations, rather than a
transcription or source-reading claim about Jech2003.

## Integration and notation examination

Pending the integrator's exact frozen delta and generated snapshot.

## Findings and boundary

No actionable defect found in the complete new LaTeX body or annex at
the hashes above. Navigation and notation remain to be examined before
the final verdict. No software tests, manuscript builds, or manuscript
renders were performed or requested by this reviewer.
