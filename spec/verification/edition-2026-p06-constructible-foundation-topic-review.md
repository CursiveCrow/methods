# P6 constructible-hierarchy foundations: independent mathematical review

Date: 8 September 2026 UTC. Reviewer:
`/root/constructible_foundation_topic_review`.
Review began at 08:01 UTC. This report was prepared within the assigned
45-minute block, before the first 15-minute checkpoint fell due.

## Scoped verdict

**PASS for the mathematical content of the eight theorem/proof pairs at the
two hashes below.** I read the complete 220-line body and complete 587-line
annex, and checked the specified prerequisites in their actual LaTeX.
I found no false statement, missing essential proof case, circular use of
the earlier ordinal or recursion sketches, invalid set-existence step, or
use of Choice in this unit. There are no open mathematical findings from
this review.

This is an independent topic review of a handbook derivation from its
stated ZF axioms. I did not consult another reviewer's conclusions. No Jech
body was read, and this verdict makes no claim about fidelity to Jech's
presentation or completion of that source obligation. Integration, changes
to older reader text, provenance, production, and admission are separate
from this scoped verdict.

| Frozen target | Complete extent read | SHA256 |
| --- | --- | --- |
| `handbook/parts/p06/constructible-hierarchy-foundations.tex` | Lines 1-220, all three definitions and eight statements | `64E22FE49017819108160AF5C291E8507A94D4751C2D452EF2DBA8DE6F0E1B95` |
| `handbook/annex/p06/constructible-hierarchy-foundations.tex` | Lines 1-587, all eight proofs | `4D13EF83F571C7D61BCBD25B0AAF07EA1A0EA4840D3152ED738FB2D7CFFBA43C` |
| `spec/research/edition-2026-p06-constructible-hierarchy-foundations.md` | Lines 1-142, intake and prerequisite map | `25F1B623CFBB04FFA2FB91BE531639637F78E3D34701609011165FABAADDA7DF` |

The two target hashes and intake hash were rechecked immediately before
this report was written. An initial combined output truncated the middle
of the annex; I separately read lines 115-240 in full. The declared full
read therefore includes those paragraphs, rather than treating the
truncated output as complete.

## Actual prerequisite reading

I read `handbook/CONVENTIONS.md` and
`spec/EDITION-2026-CONTRACT.md` completely. The table records complete file
reads; the last column identifies which content was actually used.

| Prerequisite | Lines | SHA256 | Use in this review |
| --- | --- | --- | --- |
| `handbook/restoration/inherited-00603-00647.tex` | 1-45 | `B76C0E5AEE32C23E036F59F780A99690C9788636444A4456B8E6762A3307B795` | Original transitivity, ordinal, successor, and limit definitions. The cited recursion theorem was not assumed. |
| `handbook/restoration/inherited-03038-03104.tex` | 1-67 | `8531B8FC91A659AB7C5B131A77FCA7AFF9C97F0A052E3B78FE0459ADEC25FFAB` | Countable variable supply, signature, and terms. |
| `handbook/restoration/inherited-03105-03165.tex` | 1-61 | `5C062C8A2584C841ED74EC9B546FA502EF0FF4D667A5A702EC56B7C8A49463C9` | Actual formula constructors and readability, against the nine instruction tags. |
| `handbook/restoration/inherited-03166-03239.tex` | 1-74 | `D7D08869229F450D219BCB06FFA8E990B60DB10F195B76D53E9ECCBBC480AC3C` | Free-variable clauses, finite formula complexity, and bound occurrences. |
| `handbook/restoration/inherited-03429-03518.tex` | 1-90 | `EF123D37FB24D3D7194768867468E3E739E92C066E855195B0F7F6B040892D0B` | Nonempty structures, assignments and updates, term evaluation and coincidence. |
| `handbook/restoration/inherited-03519-03680.tex` | 1-162 | `B1F502609BB084ACFF222A7431E05CAED5273ACD19C367B45CBDCCB63F306897` | All Tarskian truth clauses and the complete formula-coincidence proof. Later substitution and alpha-invariance results were read but are not needed in place of the new direct renaming argument. |
| `handbook/restoration/inherited-10060-10088.tex` | 1-29 | `21DC5D4896EA787EB7AE605589C4126C11BA969B5FA41B0FA1D30B9D28C8C7B8` | Membership language has only the binary relation, with logical equality; ordinary terms in this language are variables. |
| `handbook/restoration/inherited-10089-10271.tex` | 1-183 | `6E8EB080C5FC4C5D359798C48AFFB7692ACE514F702DABF643003AE57FFF4B29` | Exact ZF axiom list, Separation and Replacement schemas, Foundation, Power Set, and the least-inductive-set construction of omega. Choice is stated there but was not used. |
| `handbook/restoration/inherited-10272-10352.tex` | 1-81 | `0FC1DB84F232FDC88F0860164281D9F0F1182565B6D510F376DE90E0F016A0F3` | Kuratowski pairs, pair identity, functions, and no self-membership. The sketched general membership recursion was not assumed. |
| `handbook/restoration/inherited-10353-10451.tex` | 1-99 | `6B0A7785FADE6927950AD97D90EC2B24FC90A335B7673AC0A3B75F6E6C791008` | The complete transfinite-induction proof at lines 66-72. The ordinal and definable-recursion sketches were not accepted as completed prerequisites. |
| `handbook/restoration/inherited-10452-10520.tex` | 1-69 | `EF5058570C685B60C04893267C8F57B4BFF5E214E344E0BF51DCF30DF347DFF4` | Exact V-recursion clauses. The hierarchy sketch and rank-existence assertions were not assumed. |
| `handbook/restoration/inherited-10675-10769.tex` | 1-104 | `B745B19A1B07592A4CD59FEC1791B3102E88B3C53E30F276C06CA168EBC1D57A` | Active Def(empty) clause, nonempty finite-parameter definition, L-recursion, original class theorem and its remaining sketch. |

The file with inherited interval 10675-10769 has 104 current lines; I used
its actual current extent rather than its historical interval length.
I also read all 153 lines of `handbook/parts/p06.tex` at
`586423629382AABF0D804C56B6458D8E8AFAA1BADCE5DB81D7C39CF19613EA86`
and all 18 lines of `handbook/annex/p06-route.tex` at
`0B7884FD52231742CE9EA922CAF32A325BEFCC1D9AA61B39C9F6E54172B63E44`.
The named induction hook identifies the actual proved inherited induction
theorem. These route snapshots precede integration of the new files.

## Proof-by-proof assessment

The following suffixes carry the body prefix `thm:p06-` and the annex
prefix `annex:p06.`. I checked their reciprocal ownership directly.

| Pair | Annex extent | Verdict and mathematical check |
| --- | --- | --- |
| `ordinal-foundation-facts` | 3-113 | PASS. Ordinal members inherit the strict well-order and are proved transitive. The least member of the proper difference is shown to include, and be included in, the smaller ordinal. Intersection then gives comparison without assuming it. Foundation supplies irreflexivity and the minimum needed for the reverse bounded-predicate implication. Successors, set unions, zero in nonzero ordinals, limit unions, and successor indices below limits all follow with the displayed set bounds. The separated inductive subset of omega proves its members are ordinals included in omega and are zero or successors; this then proves omega itself is an ordinal. |
| `definable-ordinal-recursion` | 115-204 | PASS. Restrictions use Separation on the existing graph. Compatibility precedes existence and uses the least disagreement in the smaller ordinal. Successors append one new ordered pair. At a limit, the induction hypothesis and uniqueness make App functional on that particular set ordinal, so Replacement supplies the family of prior graphs and Union supplies its graph. The use of xi+1 below the limit proves each equation in that union. The formula for F is functional, its ordinal restrictions are the approximations, and Replacement forms restrictions to arbitrary sets of ordinals. Competing definable class solutions are compared through their set restrictions. |
| `set-sized-definability` | 206-364 | PASS. Products have the double-power-set bound claimed; triple records, lists, valid codes, assignments, and truth relations are subsequently separated from explicit sets. The nine truth clauses have the correct signs, connectives, and quantifier updates. The auxiliary operation is total even on ordinal-domain functions with arbitrary earlier set values, so the already proved recursion theorem applies. The final-position computation gives a single guarded formula for Sat. Both code/formula directions and both finite-parameter directions are justified, including index shifts and bijective variable renaming. The final Def value uses Separation on P(A), with the empty branch supplied separately. |
| `bounded-transitive-absoluteness` | 366-396 | PASS. Atomic and Boolean cases agree. In each bounded quantifier, the bound variable differs from the variable naming the bound set, so the latter value stays fixed. Transitivity makes the internal witness range exactly the ambient members of that bound set. The ordinalhood consequence uses only the bounded formula and the ambient ordinal characterization; it imposes no ZF-model assumption on A. |
| `def-transitive-growth` | 398-417 | PASS. Every Def member is a subset of A. The equality formula defines A for nonempty inputs; the empty case is explicit. For transitive A, membership with a parameter x in A defines x itself, giving A subset Def(A). Combining that inclusion with each Def member being a subset of A proves transitivity of Def(A). No monotonicity of Def on unrelated inputs is assumed. |
| `hierarchy-recursion-existence` | 419-470 | PASS. Each operation has disjoint zero, successor, and nonzero-limit cases. Successor predecessor uniqueness follows from ordinal comparison. Ranges at limits are sets by Replacement, and Union applies. The established Def operation and Power Set separately supply total functional successor operations. The proved recursion theorem therefore gives both original hierarchy clauses and their set restrictions. The expanded L predicate quantifies only over sets. |
| `constructible-level-height` | 472-569 | PASS. Transitivity and increasing levels are established before the height induction. The zero successor uses Def(empty). At a nonzero successor, the induction hypothesis makes the previous level nonempty, bounded absoluteness defines precisely beta over it, and the parameter-free definition admits beta into the next level. Any ordinal eta in that Def set is a subset of the previous level, so every member of eta lies in beta and eta is at most beta. The limit equivalence is the already proved union-of-limit identity. Height excludes alpha from L_alpha and proves strict growth. The V comparison uses only its locally justified recursion clauses. |
| `constructible-class-foundation` | 571-587 | PASS. Level transitivity gives class transitivity; the next-level membership gives every ordinal. If L were a set, Separation would produce a set O of all ordinals. Union would give an ordinal nu, while nu+1 in O forces nu in nu, contradicting Foundation. |

## Focused checks of possible gaps

The formula `Ord_b` contains transitivity of its argument, transitivity of
each member, and pairwise comparison. Its reverse implication therefore
has the transitivity of the strict membership relation needed in addition
to linearity and Foundation. It is not merely a formula for a transitive
set whose elements happen to be comparable.

In the satisfaction construction, tags 0 and 1 use variable indices for
equality and membership; tag 2 gives the empty truth set; tag 3 gives the
complement within the assignment set; tags 4, 5, and 6 give conjunction,
disjunction, and material implication; tags 7 and 8 range over every or
some member of A after updating the named variable. Earlier-position
fields are shifted when lists are concatenated, while variable fields and
unused fixed zero fields keep their roles. Finite induction on the shift
recurrence places the second list after the first and preserves the prior
references. Unfolding shared earlier positions preserves the ordinary
formula, rather than creating a new logical operation.

For nonempty A, one locally fixed member gives a constant assignment.
Extending a given finite parameter assignment by that same member is a
Separation construction on omega times A. Neither step selects members
from a family of nonempty sets. The uniform Def formula itself need not
choose a distinguished element for every A. Formula coincidence reduces
the output formula's other free-variable values to a finite tuple. The
reverse construction moves all occurrences in a bijective variable
renaming, including bound occurrences, so it does not introduce capture.

The base cases are consistent: L_0 is empty, L_1 is {empty}, and the
successor argument at beta=0 gives precisely the ordinal subset 1.
At every nonzero successor, the parameter-free bounded ordinal formula
defines beta, not beta+1. The latter is the set of all ordinal members of
the new level after beta is admitted. This distinction and the reverse
inclusion are both present in the proof.

## Limits and handoff

No manuscript files were changed. No tests, manuscript builds, renders,
external-source substitutions, admission records, or other review reports
were used or produced. This review writes only this report.

The older constructible-class paragraph remained a sketch at the input
snapshot. The new proof establishes that theorem's stated transitivity
and ordinal-containment conclusions, and the new corollary also proves
properness. Parent-owned integration may link the old statement to this
derivation with its required correction provenance. Such an integration
change is not already included in this frozen-file verdict.

The axiom-relativization scheme for L, its definable well-order,
condensation, reflection, GCH, V=L, and relative consistency have separate
proof obligations. None is inferred from the eight results reviewed here.
