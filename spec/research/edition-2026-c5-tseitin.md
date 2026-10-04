# Edition 2026 C5: Tseitin construction for D-P2-007

Date: 7 September 2026. Authoring and read-back completed at 16:10 UTC.
The 16:02 checkpoint saved the new body, complete annex proofs and both
driver inputs within fifteen minutes of the 15:48 start. Root integration
seams remain explicitly pending below. No independent review pass, build or
render is claimed.

## Scope and source basis

The active input is the primitive formula-string language in
`handbook/restoration/inherited-01661-01816.tex`: propositional variables,
bottom, negation, conjunction, disjunction and implication. Valuations and
the coincidence lemma are in `inherited-01817-01898.tex`; clauses, their
canonical literal order and formula interpretation, and the CNF convention
are in `inherited-01946-02186.tex`. The new occurrence definitions in
`parts/p02/propositional-substitution.tex` and its complete annex were read.
The existing Part 12 general claim, root clause, and conjunction example were
read in `inherited-14351-14400.tex`; the modern SAT chapter's routing paragraph
was read in `parts/p12/sat-and-certificates.tex`.

The primary modern source actually consulted is John Harrison, *Formal
Verification Methods 1: Propositional Logic*, Marktoberdorf, 30 July 2003,
[author-hosted slides](https://www.cl.cam.ac.uk/~jrh13/slides/marktoberdorf-30jul03/slides1.pdf).
The PDF has 19 physical pages, numbered 0–18. Printed slide 12, physical
page 13, displays fresh definitions for selected subformulas, both directions
of the defining equivalences, their CNF clauses, and the final asserted root
variable. Slides 11 and 13 frame the normal-form and set-of-clauses roles.
The title page and these passages were read through the primary web text;
the source screenshot attempt timed out, so no successful visual PDF check
is claimed. Proposed key: `Harrison2003PropositionalSlides`, supplied to the
root for its owned bibliography integration.

Harrison's [author resource page](https://www.cl.cam.ac.uk/~jrh13/atp/) and
[defcnf.ml](https://www.cl.cam.ac.uk/~jrh13/atp/OCaml/defcnf.ml) were also read:
`maincnf`/`defstep`, lines 18–29, store definitions; `mk_defcnf`, lines 46–52,
combines the transformed root with those definitions. This is accompanying
code, not a claimed reading of the full 2009 book. Its sharing, NNF processing
and variable-index policy are not identified with the construction written here.

No original 1968 Tseitin proof or unread Prestwich chapter is claimed as
consulted. The supplied occurrence construction reuses original variable
leaves and gives a distinct fresh label to every nonvariable occurrence,
including bottom. This is a fully specified definitional-CNF variant, with
all primitive clauses and the complete proof supplied in the annex. The
source's own p_1,p_2,p_3 notation is not rewritten or passed off as the new
occurrence notation z_a. The existing Part 12 source presentation is unchanged.

## Mathematical contract

V is exactly the set of original input variables; Z is a finite disjoint
set of auxiliary variables. The theorem quantifies over v:V→{F,T} and
w:V∪Z→{F,T}. Every v has one defining extension satisfying D_phi; this
extension satisfies the rooted S_phi exactly when v satisfies phi. There
is no claim that an already total global Prop valuation can be extended
while changing its existing auxiliary values, or that arbitrary global
extensions outside V∪Z are unique.

The proof checks variable, bottom, negation, conjunction, disjunction and
implication cases separately, in both directions, then proves existence and
uniqueness of the defining extension. The root assertion supplies the exact
projection onto satisfying original assignments. The inherited clause/formula
semantics transfer this result to one explicitly ordered CNF formula string.
The existential extension statement is metatheoretic; no new propositional
quantifier is introduced. T_phi entails phi on the enlarged vocabulary, but
the reverse implication is not generally valid.

The worked example combines conjunction, negation and implication. A separate
bottom example shows why dropping the root turns an unsatisfiable input into
satisfiable gate definitions. A negated-atom countervaluation distinguishes
equisatisfiability from logical equivalence on the enlarged variable set.

For N tree occurrences and M nonvariable occurrences, the construction emits
at most 3M+1 clauses and 7M+1 literals, with width at most 3. Linear emission
is stated only for a parsed tree and supplied fresh names under unit-cost
references. Under binary indices and fixed connective/separator codes, the
output bound is O(L+N log(N+1)); polynomial bit-time effectiveness is proved.
The fresh symbols can all be selected among the first N variable names.
Neither abbreviation expansion, long position words nor repeated subformulas
is hidden in the measure.

## Routing and ownership checkpoint

Body: `handbook/parts/p02/tseitin-transformation.tex`, inserted after
`scope-SRC-01946-02186` and before the next source chapter at
`scope-SRC-02187-02192`. Annex: `handbook/annex/p02/tseitin-transformation.tex`,
inserted after the existing substitution/replacement annex. No old proof,
stable-ID repair, PA2 insertion, or substitution addition is removed.

The root owns the explicit CNF forward link, proposed immediately after the
proof of `thm:prop-normal-forms` and before the next truth-function paragraph
in `inherited-01946-02186.tex`, and the matching input-sequence guard. The
root also owns canonical bibliography and symbol changes.

Body/annex pairs are `thm:p02-tseitin` → `annex:p2.prop.tseitin` and
`thm:p02-tseitin-size` → `annex:p2.prop.tseitin-size`. The previously matching
Tseitin label in `propositional-syntax-semantics.tex` is inactive; that old
file is not imported or used as current proof evidence.

## Frozen author handoff

Both complete new files were read, followed by read-back of the final
type/quantifier/size clarifications. Every primitive gate and both directions
were checked in the written proof, including coincident binary input
representatives. The author also checked atomic input (no auxiliary variables),
variable-free input, the unsatisfiable bottom/root example, the two worked
assignments, and the countervaluation to enlarged-vocabulary equivalence.
This is author read-back, not independent mathematical acceptance.

| File | Lines | SHA-256 |
| --- | ---: | --- |
| `handbook/parts/p02/tseitin-transformation.tex` | 188 | `6511c58389ddb2a79f470cc30cbcf9a7e932c11c9a9d51445568d99abe3660d4` |
| `handbook/annex/p02/tseitin-transformation.tex` | 167 | `975195e565e2ae77f128eda22568bf728555380f03e360006d4a5d67c4d19561` |
| `handbook/parts/p02.tex` | body input at 10 | `77811cdf11b5e6e2fbb3b56a45b229d973ba39815926de29d49823d3f2fa7854` |
| `handbook/annex/p02.tex` | annex input at 12 | `16509f383235271f580f1cb4402d188cab5e44360e4396f612ec034632fefd86` |

The body has zero proof environments; the annex has the two complete proofs.
Both proved-status destinations and annex back-references match. Each driver
contains its new input exactly once. Removing that one line in memory
recovers the driver's pre-task hash, respectively
`3576cc349c1245430b30531c266e0483144c5470b2f61a894c0d16d38522fbdd` and
`65c7b1d7300401cff444dd324fd6c44951b3ab9d8acb9b07d58c41739e9bc87f`.
Thus all prior driver entries, including stable-ID and PA2 routing, are
preserved. The existing substitution body and annex hashes are unchanged:
`5b39b8dc52b60442850707c6d4df2c7e853929fc52541f85d839986bfd8dc146` and
`4b28adaff5f2a3217ed4808b2ea459639635eb957f7fffd22347071657efc5df`.

### Pending root integration and acceptance conditions

At the final read-back, the explicit CNF forward link and
`Harrison2003PropositionalSlides` bibliography key were not yet present.
The root has their exact proposed seam and verified source metadata. The
root also owns the corresponding expected-input guard and the canonical
symbol integration. The annex driver's introductory exhaustive topic list
needs to include Tseitin; this was reported rather than edited beyond the
authorized one-input addition.

D-P2-007 may be counted integrated only when the active CNF section reaches
this statement, the bibliography and input guards agree with the active
driver, and the new proof pair has passed its required independent review.
That review should reject any loss of the root clause, conflation of V with
global Prop, unqualified enlarged-vocabulary equivalence, unproved one-way
gate weakening, or an encoding claim that treats unbounded variable names
as single bits. The frozen author text explicitly avoids those claims.

No tests, manuscript builds/renders or subagents were used. The final source
handoff ends this authoring assignment; subsequent integration and the
manuscript completion plan are owned by the root.
