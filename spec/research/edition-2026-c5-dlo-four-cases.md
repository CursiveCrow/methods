# Edition 2026, C5: complete active DLO extension argument

Date: 7 September 2026. Requirement R-030. This is an author proof-completion
record, not independent review acceptance or formal admission.

The active proof at `handbook/restoration/inherited-07295-07468.tex:115-131`
previously invoked the cut, density and absence of endpoints without supplying
the four required extension cases. The source feedback at
`inherited-15638-16742.tex:465-474` names those cases but leaves them to the
reader. The inactive `annex/p03/qe-categoricity-games.tex:45-53` was read as a
historical repair lead; its compressed case list is not active proof evidence.

## Direct completion

The existing active proof now starts from the empty finite map and explicitly
defines lower and upper subsets of its finite range for a proposed new domain
element. The cases are: two nonempty bounds; lower only; upper only; and no
bounds. The proof establishes the bound ordering, uses the appropriate DLO
axiom in each case, and proves that the chosen point is outside the entire old
range. It then proves preservation and reflection of order for the extension.

The backward step applies this same established argument to the inverse map
in the other DLO. The proof explains why the increasing union is an injective
function, total, surjective and order preserving/reflecting. It also makes
existence of a countably infinite DLO explicit, as required by the immediately
preceding definition of categoricity.

The source's finite-partial-isomorphism definition, back-and-forth method and
complete general extension theorem at lines 24-75 were read before the edit.
The correction elaborates the existing argument and preserves its theorem,
label, hypotheses, mathematical objects and existing proof environment. It
does not claim new consultation or source fidelity to Hodges or Marker, whose
citations remain the source's general further-reading attribution.

## Author verification and remaining gates

For two bounds, every old range element is at most the lower endpoint or at
least the upper endpoint; density therefore supplies an unused point. For one
bound, absence of the corresponding endpoint supplies a point beyond all old
range elements. With neither bound, the finite range is empty. The inverse
construction has precisely the same hypotheses. No finite-avoidance assertion
is left unsupported by these partitions.

Before-edit complete file SHA256:
`ac14d5d63a54e8d7174783e28a228fac224a72352e15f0ce253d89eafc1c0672`.
After-edit complete file SHA256:
`1958b3363dcac80b5c7af56f446e74591b4249d23c1c8543cc9ec7de7bb93a89`.
The frozen `source/formal-logic-reference.tex` was not edited. Its standing
as an archival authority is distinct from the active corrected proof.

This closes the authored missing-case component of R-030. The other C5 results,
independent source/topic/publication reviews, provenance admission and output
verification remain separate. No build, render or software test was run for
this mathematical proof edit.
