# Adjoint presentations and the presheaf-topos construction

Date: 6 September 2026 Pacific time.

The active Part X host and annex now include
adjoint-first-order-calculus, presheaf-categories, and presheaf-topos.
Both additional calculus sheets are included in the body and the
Part XIV catalogue. This pass supplies eight complete proof pairs.

## Proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-contextual-predicate-transport | annex:p10.adjoint.1 |
| thm:p10-contextual-adjoint-equivalence | annex:p10.adjoint.2 |
| thm:p10-contextual-equality-reduction | annex:p10.adjoint.3 |
| thm:p10-presheaf-limits | annex:p10.psh.1 |
| thm:p10-presheaf-mono-epi | annex:p10.psh.2 |
| thm:p10-presheaf-exponentials | annex:p10.psh.3 |
| thm:p10-presheaf-topos | annex:p10.psh.4 |
| thm:p10-presheaf-power-objects | annex:p10.psh.5 |

## The alternate source presentations

Pitts's Figures 4, 6, and 8 are now displayed as all fifteen
directed inferences of their seven bi-rules. The source's double
line is explained as equivalence of derivability. The separate
parameter-free equality variant in Remark 5.6.2 has its own
two-direction sheet.

The syntactic transport proof discharges the finite hypothesis
list into implications, universally closes the retained variable
context, and re-instantiates it in the target context. Original
theory-axiom leaves remain unchanged. It applies to predicate
sequents and does not assert external term-equation transport.

Every natural-deduction/adjoint direction is derived explicitly.
In particular the equality bi-rule keeps assumptions depending
on its first equality variable. The parameter-free variant
recovers the full rule by discharging both assumptions and
parameters under exactly the implication/universal hypotheses.
No semantic completeness theorem or cut-elimination assertion
is substituted for these syntactic derivations.

Source and review:

- p10-adjoint-calculus-source-note-2026-09-06.md;
- p10-adjoint-calculus-review-2026-09-06.md.

The independent reviewer checked all four actual files against
Pitts's primary figures and found no necessary repair.

## The presheaf construction

The elementary-topos definition now states the exact unique
characteristic-map pullback property for every monomorphism.
The presheaf development proves local smallness, canonical
pointwise small limits and colimits, and all componentwise
mono/epi/isomorphism criteria. The converse epimorphism proof
uses a pointwise pushout test. Canonical image subpresheaves
represent the ordered subobjects without selecting arbitrary
isomorphic presentations.

The exponential proof gives the full natural-transformation
components, restriction action, evaluation, both transpose
naturalities, and both inverse identities. The sieve construction
proves closure, truth naturality, characteristic-map existence and
uniqueness, and the pullback property for arbitrary monos.
The power-object proof gives natural classification, membership,
stage identification, and restrictions. Empty components and the
empty base are included. A two-stage example distinguishes these
objects from external pointwise function and powerset sets.

The primary sources are the acquired exact 1992 Mac Lane--Moerdijk
book and the separately identified Utrecht 2007 Moerdijk--van Oosten
lecture notes. The new bibliography entry is
MoerdijkVanOosten2007Topos.

Source and review:

- p10-presheaf-topos-source-note-2026-09-06.md;
- p10-presheaf-foundations-review-2026-09-06.md;
- p10-presheaf-topos-review-2026-09-06.md.

The size review prompted explicit closure properties for the
categorical size convention. It permits the ordinary ambient
all-sets/set-class reading; a set-sized relativization explicitly
requires Grothendieck-universe closure, whose existence is a
separate hypothesis. This does not assert a new universe-existence
theorem. The missing local type of the exponential's comparison
map and its source bibliography entry were also supplied.
All incorporation repairs were read back; both presheaf review
scopes now pass without an unresolved finding.

## Integration and navigation

The actual Part X annex route was recounted at 80 proof items:
the previous 72 plus these eight.
The new sheets have fifteen and two directed rule rows.
The existing Part X formatter produced 157 theorem/definition rows.
The existing named-theorem generator supplied the eight new
index rows as a scoped update. Nineteen notation rows were added,
nine existing categorical scopes were extended through P10.9,
and both generated symbol tables now use 854 registry rows.
The scoped whitespace check passed.

The current per-part record is
manuscript-completion-status-2026-09-06.md.
These counts measure integrated proof items, not completed
requirement rows or an overall manuscript percentage.

## Next writing and remaining scope

The next presheaf development is its internal Heyting operations,
quantifiers, and forcing semantics, followed by the precise
higher-order/comprehension interpretation and distinctions from
generalized-element and site/sheaf semantics.

The relevant exact Mac Lane--Moerdijk body passages have now
been inspected and recorded in
p10-presheaf-logic-source-verification-2026-09-06.md.
The record distinguishes actual proof passages from exercises,
contents locators, and cited soundness/completeness claims.
It also supplies the correctly typed formulas needed to avoid
copying slips from the sources.

Whole-Part-X and whole-book fulfillment remain unestablished.
Other algebraic and philosophical topics, source-presentation
coverage, full requirement reconciliation, and final production
remain open. No software tests, manuscript build, or manuscript
page renders were used in this writing pass. The saved PDF still
predates these additions. The full manuscript goal remains active.
