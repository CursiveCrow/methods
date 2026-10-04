# Independent mathematical review: Kamp 7, product measures, causal models and social choice

Reviewer: `/root/kamp7_product_causal_social_topic_review`.
Dispatch: approximately 2026-09-08 06:40 UTC. Deadline: 07:25 UTC.
Standing: **PASS for all four frozen mathematical units.** Completed at
approximately 06:50 UTC, before the first required 15-minute checkpoint.
All 27 claimed result/proof pairs were read and assessed. No actionable
mathematical defect was found in the assigned scope.

This is an independent topic review of the actual LaTeX. No other reviewer's
report or verdict was read. Only this report is owned by the reviewer. No
manuscript file, source, registry, driver, software test or admission record
was changed. No manuscript PDF was built, rendered or inspected.

The complete governing contract and `handbook/CONVENTIONS.md` were read.
Their declared requirements govern correction, complete proofs, independent
review and the separation of mathematical review from production/admission.

## Frozen units and reading extents

| Unit | File | Full extent read | Verified SHA256 |
| --- | --- | --- | --- |
| Kamp Lemma 7 | `handbook/parts/p09/presentations/kamp-iii2-lemma7.tex` | 1–278 | `3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778` |
| Kamp Lemma 7 | `handbook/annex/p09/kamp-iii2-lemma7.tex` | 1–489 | `3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F` |
| Finite causal models | `handbook/parts/p16/finite-causal-models.tex` | 1–418 | `331568E5FF2329B4498CA98DCA7DC8BE79D4EB77B8A2152DAB33F05F05BABA42` |
| Finite causal models | `handbook/annex/p16/finite-causal-models.tex` | 1–377 | `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096` |
| Product measures | `handbook/parts/p15/product-measures.tex` | 1–391 | `9FFEDE5090864204636CEA69B317F2CEF9E82105A90A47DB8F75764FD23EE0AC` |
| Product measures | `handbook/annex/p15/product-measures.tex` | 1–571 | `E62A873EE1BC0B6435F19ABE71F9B121FD4EB53BA0B3322863BBF61186E1CAB4` |
| Social choice | `handbook/parts/p17/social-choice.tex` | 1–321 | `224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA` |
| Social choice | `handbook/annex/p17/social-choice.tex` | 1–321 | `C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F` |

All eight hashes matched the supplied freezes. The product and social targets
were first read only after the lead supplied their freezes. Kamp, causal and
product author intakes were read as maps, not substituted for the manuscript.

Actual prerequisites read:

- Kamp Lemma 1 body lines 1–194, especially basic grammar 30–103 and word
  semantics 105–132; its annex 1–133, including the complete guarded
  realization induction at 33–98. No temporal-translation result is needed
  for the cut proof, so its later temporal induction was not assessed.
- Kamp Lemma 4 body 1–121, especially elementary substitution membership
  at 13–42 and the actual past-word recursion at 44–92. These supply the
  claimed identity-substitution membership and exact cut-word constructors.
- Finite probability body 24–158, 219–256 and 348–384: finite event laws,
  grouping, positive-event conditioning, independence and finite expectation.
  Corresponding annex 1–120, 151–200 and 202–249 was read completely;
  annex 251–283 was also read, but conditional expectation is not a premise
  of the new causal theorems.
- Finite logical abduction body 1–96, to verify the stated contrast between
  explanatory entailment and the added structural equations/interventions.
  Its complexity results and later proofs are not causal prerequisites.
- Measurable-probability body 24–147, 206–346 and 400–415, and annex
  1–339 and 374–429: all directly used measure, measurable-map, Borel,
  nonnegative grouping, simple-approximation and pi-lambda arguments.
- Measure-extension body 1–242 and annex 1–468: the complete semialgebra,
  Caratheodory, cover-extension, uniqueness, Stieltjes and Borel Lebesgue
  constructions used in the product theorem and examples. The later
  quantile/CDF construction is not a premise of these results.
- Integration-expectation body 1–195 and 306–348, and annex 1–252 and
  405–459: nonnegative and signed definitions, simple refinement, monotone
  convergence, series additivity, null-set rules, signed linearity, source
  construction bridge and expectation/atomic identities. The calculus
  example explicitly uses elementary one-variable differentiation and the
  fundamental theorem; its Lebesgue/Riemann identification is proved in the
  new product annex 369–391.
- Finite-preferences body 21–90 and annex 1–106: the actual weak/strict
  definitions and relational facts. The new Arrow proof independently
  proves the strict-transitivity fact it uses without a finite-X premise.

The prerequisite hashes matched the intakes. In particular, the integration
body is the corrected `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5`
version, whose bridge theorem explicitly resets `f` to an arbitrary
nonnegative measurable extended function before its sigma-finite assertion.
The finite-preference body and annex hashes are
`58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C`
and `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C`.

## Kamp Lemma 7: mathematical assessment

Current result: **PASS for the frozen mathematical text.** All three result
and proof pairs were read and checked, including both orientations.

The cut construction is exhaustive: an existing strict interior point is
either one of the `n−1` internal realization points or lies in exactly one
of its `n` gaps. The finite maximum argument uses linearity, not density or
order completeness (annex 26–37). Point cuts retain their common point
label. Gap cuts require the old gap label both at the new endpoint and in
each adjoining gap; joining deletes the cut point and recovers the old
gap by the three cases below, equal to, or above the cut (annex 57–137).
This checks the easily missed middle-point requirement, including when
both adjoining intervals are empty.

The length calculation is exact. Point cuts yield lengths `2k+1` and
`2(n−k)+1`; gap cuts yield `2k+1` and `2(n−k+1)+1`. Therefore the last
gap is the sole full-length left candidate and the first gap the sole
full-length right candidate (annex 139–158). Every subset has at most
one such residual occurrence. No deduplication or relaxed bound is used.
The positive stage-one case is retained without adding a zero-stage pattern.

Each quantified proof selects the set of true fixed-side factors once,
then permits the successful cut to vary with the universally quantified
endpoint (left annex 221–260; right 376–399). Its converse uses only
positive fixed-side factors, which justifies dropping negative truth tests
inside the complete alternative construction without asserting false
pointwise equivalence of a complete truth pattern and its positive part
(left 262–285; right 401–418). Both empty subsets and vacuous tested
intervals are handled. Additional free parameters and free occurrences
of `v` in `psi_1` retain their original scopes (body 120–126; annex 433–443).

The seven-point two-interval example was recomputed at both tested values.
At `v=1`, only the second-gap residual works; at `v=2`, only the first-gap
residual works. The point cut fails because `A_1(3)` is false. The two
required fixed suffixes both hold, giving exactly the stated subset
(body 213–241; annex 308–343).

The all-false interpretation independently refutes the individual-basic
fixed-side requirement described in the intake. Every basic past pattern
has a false initial unary atom, while the original quantified formula
with tautological `psi_1,psi_2` has a strict interior witness. The four-point
variant gives a nonempty tested right interval. Thus the corrected aggregate
statement and its empty conjunction are mathematically necessary for this
input class (body 243–267; annex 454–481). This topic review verifies the
countermodel and corrected theorem; it does not independently certify the
historical scan's glyph reading.

## Finite structural causal models: mathematical assessment

Current result: **PASS for the frozen mathematical text.** All eight result
and proof pairs were read and checked.

The finite predecessor-chain argument proves that every nonempty remaining
DAG has a source vertex. Removal therefore supplies an actual topological
enumeration (annex 13–34). Total functions evaluated in that order produce
one solution; induction proves uniqueness and hence independence of the
chosen topological order. Probability laws are grouped fibers, including
empty fibers and the one empty coordinate tuple (annex 36–71).

Intervention deletes incoming edges and replaces exactly the named equations.
The resulting functions remain total and the graph remains acyclic. The
original tuple is a modified solution whenever its intervened coordinates
already equal the prescribed values. Nonintervened nondescendants form a
parent-closed set, so topological induction proves their pointwise invariance.
Empty and disjoint commuting replacements are proved without probabilistic
conditioning assumptions (annex 73–112).

Arbitrary exogenous dependence is allowed by the model definition. The
factorization theorem explicitly adds mutual independence. For a fixed
assignment, the solution fiber is exactly the intersection of its separate
disturbance equation-events. Independence gives the structural product at
every assignment (annex 114–146). Earlier endogenous variables depend only
on earlier disturbances, yielding independence of the current disturbance
from its parent tuple and the conditional-kernel identity only when that
parent event has positive mass (annex 148–181).

Truncation applies this theorem to the modified model: independent disturbances
retain their joint law, replaced kernels are point masses, and all other
kernels retain their total parent-domain definitions (annex 185–210).
The full-positive-support hypothesis makes every observational denominator
positive and turns these factors into an explicit function of the common
observational law (annex 212–241). It is correctly stated as sufficient,
not necessary for each particular target. The independent chain calculation
uses a conditional probability only at a positive treatment event
(body 282–301).

The common-cause masses were recomputed directly. Equal observed bit pairs
have mass `(9+1)/32=5/16`; unequal pairs have `(3+3)/32=3/16`.
The conditional contrast is `5/8−3/8=1/4`. Replacing the `X` equation
leaves the response marginal `(1/2)(1/4)+(1/2)(3/4)=1/2`, giving zero
intervention contrast. Conditioning additionally on the measured common
cause yields exactly the stated direct adjustment calculation, with both
denominators positive (annex 243–308).

Both nonidentification witnesses belong to their stated classes. The reduced
common-cause model has dependent disturbances and an explicitly allowed
inactive edge; it shares all four positive observed masses with the model
`X=c, Y=c xor d`, but their targets are `1/2` and `5/8`. The latter
has independent disturbances and therefore also belongs to the larger
class permitting dependence. The singleton-disturbance pair is mutually
independent and observationally concentrated at `(0,0)`, but its equations
`Y=0` and `Y=X` give targets zero and one at `do(X=1)` (annex 310–377).
These are actual two-model counterexamples. The text does not reuse the
independent-kernel product after the latent projection.

## Product measures: mathematical assessment

Result: **PASS for the frozen mathematical text.** All nine result/proof
pairs and every worked example were read and checked.

The rectangle assignment is well defined, including empty rectangles.
Its countable disjoint-partition identity is derived by taking sections,
using factor countable additivity, and integrating a nonnegative series in
one variable. It does not assume product integration or Tonelli. The case
of an infinite coefficient times an indicator is proved by monotone
convergence with the declared zero-times-infinity convention. This supplies
exactly the earlier semialgebra/premeasure hypotheses, so the unrestricted
existence assertion is justified; sigma-finiteness enters the stated
uniqueness branch (annex 60–131).

The finite-product domain proof extends elementary rectangles successively
in both coordinate blocks. The uniqueness proof restricts to finite-mass
covering rectangles before any subtraction. This validates arbitrary
parenthesization and coordinate permutation, including zero/infinite
rectangle factors (annex 133–196).

Every measurable-set and function section is proved measurable at every
point, using the actual product sigma-algebra (annex 11–58). For section
measure functions, the finite-box argument establishes a lambda-system
using bounded integrable real functions and finite measure subtraction.
It first exhausts sets inside a fixed box and then exhausts the two factor
covers. Thus both measurability and integral equalities precede Tonelli
(annex 198–265). Tonelli applies simple approximation and monotone
convergence separately in the section, the outer factor and the product
(annex 267–307).

Signed Fubini uses the measurable absolute-section functions to define its
actual null exceptions. Positive and negative section-integral functions
are each replaced by zero there before subtraction. All subsequent
subtracted integrals are finite. The a.e. replacement arguments explicitly
retain measurability and do not assume completion (annex 309–365). The
single exceptional-section example correctly has zero product integral
and an infinite section at precisely one null point (body 221–232).

All four failures were recomputed. The counting array has row sums one,
zero, zero, ... and all column sums zero, with both part sums infinite.
The exponential example's two section antiderivatives have opposite signs
and finite outer integrals. Positive compact lower bounds on `xy` in
`[1,2]` and negative ones on `[1/4,1/2]` yield divergent `1/x` bounds
for both product parts. The uncountable-counting diagonal is product
measurable by rational rectangles but its factor is not sigma-finite.
The transported-ordinal example explicitly assumes the CH bijection and
choice; countable initial segments give zero in one order and cocountable
tails give one in the other, contradicting joint measurability via the
already proved Tonelli theorem (annex 367–495). No conditional set-theoretic
premise is dropped.

The absolute-series proof encodes the sequence measurably on a counting
product, establishes the null absolute-divergence set, and applies signed
Fubini with a measurable sum version. Counting integration equals summation
by decomposing into singleton indicators and the already proved nonnegative
series law; signed absolute convergence then permits subtraction. The
numerical series also has the explicit sum-of-absolute-integrals bound
(annex 497–535). The layer-cake subgraph has the correct countable strict
rational-rectangle description and zero/finite/infinite section lengths
(annex 537–571). The triangular example gives `1/3` in both orders, with
singleton endpoint differences null.

## Social choice: mathematical assessment

Result: **PASS for the frozen mathematical text.** All seven result/proof
pairs were read and checked.

The cycle's three pair counts are each two to one. The binary weak-majority
relation is transitive even with a tie, by exhaustion of the two-element
middle-coordinate cases (annex 3–33). All six aggregation procedures have
well-defined ranking outputs on their stated domains. Under unanimity,
each victory of the dominated alternative is also a victory of the
dominating alternative, which additionally wins their own comparison;
this proves strict Pareto for the victory count. Strictly decreasing
rank scores give a positive contribution for every voter. The changed
victory-score example and both `2,1,0` rank-score profiles were recomputed
(annex 35–85 and 225–258).

The extreme-alternative lemma covers weak social ties: if `b` is neither
strictly top nor strictly bottom, completeness and at least three
alternatives supply distinct `a,c` with `a >= b >= c`. Reordering the
other alternatives unanimously as `c > a` preserves both comparisons
with the individually extreme `b`, producing the Pareto/transitivity
contradiction (annex 87–129). The explicit insertion also works in an
infinite strict ordering.

The Arrow proof takes the first socially top step in a finite sequence;
it does not infer unproved monotonicity of that sequence. IIA fixes each
reference-pair vector independently of the orderings on the remaining
alternatives. Inserting `b` between the pivot's chosen pair gives the
two comparisons from the consecutive extreme profiles and therefore that
pair's strict social ordering. Both directions for pairs involving `b`
are then proved using a third alternative, unanimity, strict transitivity
and IIA. One voter consequently determines every pair at every profile.
The empty-profile-domain case is explicitly vacuous and does not import an
ordering-existence axiom for arbitrary X (annex 131–223). All four premise
counterexamples have their stated domains and actual nondictatorship
witnesses.

For May's characterization, balanced profiles are sent to zero by a voter
permutation and neutrality. Any positive-imbalance profile is obtained from
a balanced one by finitely many permitted `0 -> 1` steps, each controlled
by responsiveness. Neutrality supplies the negative case. The displayed
majority rule satisfies both upward and downward responsiveness. For the
three independence examples, positive weights preserve both required
directions, the constant-one rule's downward premise is always false,
and constant zero fails the specified upward test (annex 260–321).
The weak-input binary domain is explicitly distinct from Arrow's strict
input domain.

## Final scope and handoff

The full assigned mathematical scope passes: Kamp 7 (3 proof pairs), product
measures (9), finite causal models (8), and social choice (7). No target
line or claimed proof was left unread. The prerequisite extents above
record the actual bounded dependency assessment; unrelated chapter results
are not independently reaccepted by this report.

The lead received concrete progress messages after the first two full units
and after the second two full units, before this completion. There was no
need for a 15/30-minute checkpoint because the review returned before the
first interval elapsed. No other review conclusions were consulted.

This report grants no source-fidelity, publication, build, visual, catalog or
formal admission gate and makes no claim of full manuscript completion.
