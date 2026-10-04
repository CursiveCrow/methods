# N-c-017 mathematical corrections

## Editorial direction

The user's 6 September 2026 correction requires the reader-facing manuscript
to present corrected mathematics and the arguments supporting it. Describing
a source error does not fulfill the mathematical writing obligation.
Historical erroneous wording and the provenance of repairs belong in internal
research records. This direction supersedes earlier local fidelity guidance
where it would require preserving an error in the published treatment.
Source citations remain attached to the relevant mathematical topics.

## Recurrence diameter

The source inspected is Biere, Cimatti, Clarke, and Zhu, CMU-CS-99-101,
Section 5, especially Definition 22 and Theorem 24:
https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf

The extracted printed condition requires the last state of a path of
d+1 edges to equal an earlier state. That does not define the conventional
recurrence diameter of every finite graph. For states a,b and transitions
a->a, a->b, b->b, a path consisting of d+1 occurrences of a followed by b
violates that condition for every d.

The manuscript instead defines recurrence diameter as the maximum edge length
of a simple directed path. It proves that this is the least d for which every
path of d+1 edges contains some repeated pair of vertices. It states and
proves the upper bound |S|-1 and the equivalent unsatisfiable-simple-path
certificate.

The new reader-facing results prove:

- Initial reachability of a state predicate has a witness through the graph
  recurrence diameter.
- A bad-state reachability formula at a certified sufficient horizon decides
  the invariant property, with totality used to extend shorter prefixes.
- The initial-state diameter supplies the corresponding shortest-distance
  bound, including its distinction from longest simple paths.
- Existential persistence of a state predicate has a lasso witness through
  the recurrence diameter.
- For arbitrary LTL, the product with an ordinary nondeterministic Buechi
  automaton has a simple stem followed by an accepting simple cycle. Its
  recurrence diameter bounds the witness, and is at most |S||Q|-1.
  Q counts the actual automaton after any acceptance conversion.

The manuscript no longer substitutes an unverified exact 2^|h| automaton-size
estimate for the size of that construction. Its LTL-automaton dependency is
linked to the existing thm:p09-ltl-buchi and N-c-013 construction.

## Encoding correctness

The former statement that the SAT/bounded-witness correspondence was owed
has been replaced by an argument in both directions. The proof handles a
finite bounded witness whose prefix has an available back edge: bounded
truth in negation normal form survives every continuation of the prefix,
so a selected lasso also satisfies the formula.

## Bryant operations

The source is the annotated author version:
https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf

- The reduction treatment gives the bottom-up procedure and invariant,
  comparison-sorting cost, and any level-scanning overhead.
- Apply and Compose now include the reduction cost of their intermediate
  graphs, with linear-cost variants conditional on the stated data structures.
- Graph splicing is followed by reduction when needed; order preservation
  alone does not imply reducedness.
- Assignment counting uses the corrected skipped-variable exponents and
  includes their derivation and base cases. The source's Update footnote 10
  identifies the missing minus-one error in the original recurrence.

The reader-facing passages state these results directly. The source's
withdrawn assertions and contradictory cost claims are not printed as
unresolved mathematical content.

## Abstraction refinement

The controlling source is Clarke et al., JACM 50(5), 2003:
https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf

The manuscript now supplies the following constructions and proofs directly:

- Finite guarded-program semantics, with the first true guard effective,
  nonempty permitted next-value sets, simultaneous updates, explicit initial
  and transition relations, and proofs of nonemptiness and totality.
- Product-coordinate construction with constant predicates excluded from
  clustering and separate universal coordinates for unobserved variables.
  This resolves the typing boundary without printing it as an unresolved
  defect.
- A common-domain combined transition relation: selected blocks share one
  concrete witness, while remaining blocks are abstracted separately. The
  exact-to-combined-to-early inclusions, selection monotonicity, and simulation
  preservation are proved, with a worked three-Boolean-variable example.
- The slice-equality refinement is proved to be the unique greatest product
  refinement separating a subset of one rectangular old class from its
  entire complement. Both the coordinate-replacement separation proof and
  the symmetric-difference greatestness proof are included. Its minimum
  partition on the failure class is distinguished from gratuitous extra
  splits outside that class.
- A two-coordinate example proves that separating only dead and bad states
  can have incomparable minimum refinements and no greatest refinement.
  Treating irrelevant states as part of the complement solves a stronger
  problem; it is not asserted to minimize the weaker problem.
- The minimum-size hardness proof gives the clique-partition matrix and a
  complete row/column-locking reduction. The Section 5 printed locking gadget
  had inconsistent dimensions and insufficient locking witnesses. The
  corrected construction uses one leading bit, ceil(log2 n) identifier bits,
  and one guard row; all four locking properties and n=1 are proved.
- Exact refinement termination uses the strictly increasing number of
  partition classes. It relies on nonempty dead and bad sets at each exact
  spurious failure, and does not claim that a single separating refinement
  eliminates every refined lift of an old coarse path.
- Combined approximation uses an explicitly specified exact-recheck policy.
  Before any partition split, a failed approximate check is replaced by a
  check of the exact existential relation at the same partition. The
  lexicographic measure (concrete state count minus abstract class count,
  approximate-selection flag) proves termination.

The Section 6 source completeness assertion did not supply this last
algorithm and measure. The manuscript presents a complete sufficient policy;
it does not attribute those added implementation choices verbatim to the
source. The policy keeps the initial image exact and has the same
finite-path/lasso refutation hypothesis as the exact completeness theorem.
The obsolete source-gap narration has been removed from the book.

## Burch applications and their corrected arguments

The primary source is Burch et al., Information and Computation 98(2), 1992:
https://mcmil.net/pubs/IC92.pdf
The added material uses Sections 5--10 and supplies independent explanatory
proofs rather than reproducing the paper's prose.

- Positive closure now has the exact approximant invariant: after round
  i >= 1 it contains paths of lengths 1 through 2^(i-1). The stopping bound
  uses shortest positive distances, including positive self-returns; it
  does not confuse them with zero-length reflexive distances.
- The fairness construction explicitly returns to the outer fixed-point
  set at every scheduled visit. An additional tautological fairness set
  enforces infinite continuation even when the user-supplied list is empty.
  The proof covers nontotal graphs, which are needed by the tableau.
- A reviewer caught a missing starting-state restriction in the prose
  describing positive-length constrained reachability. It is now written
  as F intersect Pre(Reach_F(B)). The displayed outer fixed-point formula
  already had the required intersection.
- The LTL tableau gives every elementary-coordinate, valuation, initial,
  transition, and until-fairness definition, with a truth lemma and its
  converse construction. Satisfiability quantifies existentially over
  initial tableau valuations, not universally. Dead-end valuations are
  discarded by infinite-path semantics, not made into artificial loops.
- Weak bisimulation uses reflexive internal closure for a tau match.
  The printed Section 8.2 uniform H;Delta_a;H expression, if also used
  for tau, demands at least one internal move and excludes stuttering.
  The manuscript's case distinction gives standard divergence-insensitive
  weak bisimulation and proves equivalence to direct weak matching.
- The Section 9 positive-cycle containment criterion includes membership
  in the first automaton's accepting set as well as a positive return
  outside the second acceptance set. The printed diagonal-only expression
  omits the first accepting-set conjunct described in its preceding prose.
  The corrected criterion and the alternative fair fixed-point criterion
  are proved in both directions.
- Containment states deterministic completeness of the specification
  automaton, gives rejecting-sink completion for missing transitions, and
  explains why a rejecting nondeterministic run alone is insufficient.
- The pipeline example now defines every CTL register expression bitwise.
  Horizon-wise existential/universal bit agreement proves a unique future
  register file. The update and preservation assertions are then written
  as actual Boolean CTL abbreviations.
- The general iterative-squaring transformation now specifies the admissible
  operator B union Post_K(X), with tuple arities and parameters independent
  of the iteration variable. It proves both least and greatest formulas,
  including the full fixedness argument for the cycle-supported component
  that the source Section 5.2 leaves to the reader.
- The general proof states finiteness where it is needed and gives an
  infinite-domain counterexample. CTL use reverses the kernel explicitly.
  A binary-union counterexample shows why monotonicity by itself does not
  justify the transformation.
- The nested Section 5.2 example is reconstructed with its inner positive
  reachability calculation, outer kernel, complete recurring-visit proof,
  and a worked path through states outside the recurring set.

## Further Bryant development

The complete source derivations and experiment locators are in
p09-n-c-017-bryant-bounds-source-note.md. The manuscript now proves the exact
interleaved/separated graph counts, parity count, symmetric-function upper
bound, and multiplication lower bound. The latter separates reading-order
positions from bit significance and proves the stronger rounded exponent
ceil(ceil(n/2)^2/(2n-1)), retaining the original 2^(n/8) consequence.
It does not exchange the order/output quantifiers.
The ALU table specifies what the historical timings measured.
The focused check caught one missing hypothesis in the parity comparison:
only a noncontradictory conjunction of literals must mention every input.
The manuscript now includes that hypothesis in the first claim, not just
in its later minterm-count consequence.

A subsequent full principal-content comparison found a circular step in
the earlier dependency-count canonicity proof: the child beneath an
irrelevant early root can still have the parent's dependency set.
The manuscript now proves existence by reduction and uniqueness by
induction on the number of allowed suffix variables, which strictly
decreases at every child. It also proves compatibility of child sharing
and strict minimality. The corrected proof does not infer semantic
uniqueness from reducedness alone.

The missing Apply sharpness example is now included: two disjunctions
over disjoint sets of separated variable pairs have sizes 2^(n+1) and
2^(m+1), while their disjunction has 2^(n+m+1) vertices, half the product.
This establishes output-size sharpness separately from the multiplier
lower bound measured in input-bit width.

## Further Biere bounds

The primary research and complete supplied derivations are recorded in
p09-n-c-017-biere-bounds-source-note.md.

- The ordinary all-state diameter now has an exact universal-existential
  quantified certificate and proof. It is distinguished from both the
  SAT certificate for recurrence diameter and constrained-until distance.
- Lasso padding retains the same infinite execution at every larger horizon.
  It strengthens the existing product-bound conclusion to one sufficiently
  large SAT check rather than requiring every smaller horizon.
- Explicit stem/period conventions give the bound U+V-1 when their lengths
  count states. A deterministic total N-state system has a combined
  stem-plus-period bound N and hence horizon N-1 for every LTL formula.
  No analogous formula-independent bound is inferred from finiteness alone.
- For the F/G-only fragment, a supplied construction proves the sufficient
  bound 2(m+1)N-2, where m counts distinct temporal subformulas. Constant
  temporal-record intervals are compressed, and a recurring closed walk
  preserves the remaining eventuality/counterexample obligations.
- The report Section 5.1 does not print bounded ECTL semantics or a
  translation. The manuscript therefore explicitly defines a separate
  finite state-certificate relation, with a local horizon at each temporal
  operator and independent witnesses for its children. It does not identify
  this construction with the existing bounded LTL path semantics or with
  an unacquired source definition.
- The ECTL construction states EX=false at horizon zero and proves soundness
  for all horizons and completeness at max(1,recdiam). Its SAT compilation
  uses fresh private witnesses; no polynomial-size claim is made for naive
  expansion.

## Verification boundary

The author read the resulting LaTeX and checked its formulas and source
locators. A read-only agent checked the encoding-correctness proof and all
new finite-bound proofs through the end of the general LTL argument and
reported no mathematical defects. A final local edit made C_r's definition
valid for every natural horizon before stating its sufficient-horizon theorem,
and made the negated-property automaton and existing construction references
explicit.

A subsequent read-only mathematical check covered the actual CEGAR LaTeX
from the combined-abstraction paragraph through the end of N-c-017. It
reported no concrete mathematical defects in the common-domain inclusions,
selection monotonicity, Boolean example, corrected hardness gadget,
slice-equivalence proof, finite/lasso validation, or exact and combined
termination proofs. The final wording also makes explicit that the necessary
coordinate update can split other old product classes using the same
coordinate values. No manuscript build, render inspection, or software
tests were used for this writing pass.

The next writing pass received separate bounded LaTeX checks for (1) positive
closure, fairness, and LTL tableau, (2) strong/weak equivalence and Büchi
containment, and (3) the added Bryant bounds and experiment. Two local
omissions were identified and repaired: the positive constrained-preimage
starting-state restriction and the noncontradictory parity-term hypothesis.
The checks found no other mathematical defects in those intervals. They
are not whole-source or whole-manuscript acceptance.

A final pipeline-only reading confirmed the bitwise uniqueness argument
and typing, and caught an overbroad equivalence sentence: the full update,
preservation, and STALL conjunction is not equivalent to the destination
equation alone. The text now asserts clause-by-clause equivalence to the
corresponding path clauses under the proved uniqueness conditions.

The general and nested squaring additions received a further bounded
read-only mathematical check of their actual LaTeX. It reported no concrete
mathematical defects in those two paragraphs. No whole-paper acceptance
was inferred from that result.

The corrected suffix-order canonicity proof, Apply product-sharpness
example, ordinary-diameter quantified certificate, and constrained-until
counterexample received a separate direct-LaTeX check with no concrete
mathematical defect reported.

A different bounded reader checked lasso padding, the strengthened
single-horizon product conclusion, uniform and deterministic bounds,
the F/G phase-compression proof, and the separate ECTL certificate
construction. It reported no concrete mathematical defects, including
the zero-horizon and zero-obligation cases. This is authoring evidence,
not whole-source, topic, or publication acceptance.

This is a completed repair of these passages, not full admission of N-c-017,
Part IX, or the manuscript. Other content and publication obligations remain.

REGISTER STATUS: OPEN

## Bounded CEGAR principal-content coverage

A read-only comparison on 6 September 2026 covered the actual CEGAR
subsection of `n-c-017.tex`, lines 2463--3584, against the
[Clarke et al. 2003 primary article](https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf).
No remaining material mathematical omission or incorrect principal-source
claim was found in this scope. The comparison covered simulation and
appropriateness (Section 2.4 and Theorems 3.3/3.5, pp. 761--765), initial
product abstraction (Section 4.2, pp. 767--771), finite-path and phase-aligned
lasso validation (Lemma 4.10/Theorem 4.13, pp. 772--776), separating and
coarsest product refinements (Section 4.4, pp. 777--781), and the hardness
reduction (Section 5, pp. 781--783).

The checked completeness statement retains the finite-path/lasso refutation
hypothesis of Theorem 4.24. Proper partition growth, not elimination of
every lift of an old coarse trace, supplies termination. The common-domain
combined approximation and explicit exact-recheck policy give proved
guarantees in place of the underspecified Section 6 recipe (pp. 784--785).
Corrected mathematics was not rejected for departing from defective source
wording. This is bounded coverage evidence, not complete source/topic or
publication acceptance. No manuscript edits, builds, renders, or tests were
performed by this reader.
