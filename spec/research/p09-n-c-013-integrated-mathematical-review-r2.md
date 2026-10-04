REJECT

# Review basis

This is a fresh mathematical and proof review of the current actual LaTeX.  I
read `handbook/parts/p09/presentations/n-c-013.tex` from line 1 through line
1300 and `handbook/parts/p09/logic-in-computer-science.tex` from line 723
through line 920, including the `N-c-013` input at line 910.  I used the
permitted source records and the compact register row only to resolve source
standing and exact source-level conventions.  I did not read an earlier
integrated review or admission report, inspect a manuscript rendering, or run
a build, test, checker, hash, repository script, or automated validation.

# Blocking findings

## 1. The registered parity-acceptance obligation is absent from the integrated text

`spec/registers/new-content.csv:120` requires, as part of `N-c-013`,
"Buchi/Rabin/parity acceptance."  The integrated definition at
`logic-in-computer-science.tex:723-744` reuses nondeterministic Buechi
acceptance and defines deterministic Rabin acceptance, but it supplies no
parity word-automaton data and no parity acceptance clause.  The closure
paragraph at lines 759-762 also mentions only Buechi and Rabin forms.  The
entire source presentation at `n-c-013.tex:1-1300` discusses Buechi, Muller,
Rabin, and Streett conditions but never defines parity acceptance.

This is not terminological decoration.  A parity definition must fix the
priority map's type and one of the inequivalent-looking conventions (minimum
or maximum priority recurring infinitely often, and which parity accepts), and
must say that it is an acceptance condition on a word-automaton run.  Without
those data, the `must` item in the compact ledger is not mathematically
present, and no later closure or equivalence claim can be checked against it.

Required repair: supply the owed parity-acceptance artifact at the integrated
omega-automata definition, with its exact run condition and its relation to the
already defined Buechi/Rabin conventions, or explicitly reopen and narrow the
registered obligation.  Merely adding the word "parity" would not repair the
gap.

## 2. Thomas's named-tree update does not define a deterministic transition

In Thomas's presentation, the exact live-node name map is part of every target
state (`n-c-013.tex:1193-1204`), and the acceptance sets are indexed by those
exact names (`n-c-013.tex:1250-1257`).  Surviving names persist, but lines
1240-1247 say only that newly created nodes receive pairwise distinct names
which were absent from the entire predecessor name set.  They never choose
which available names are assigned to which new nodes.

There are ordinarily several legal choices.  For example, from a predecessor
using only name (1), a surviving new child in an input automaton with
(n\geq2) may receive any of several names in
(\{1,\ldots,2n\}\setminus\{1\}).  Those choices give different successor
tuples because (\nu) is state data, and they affect different indexed sets
(E_k,F_k).  Thus the stated update is a relation with several successors,
not the total transition function required by Thomas's deterministic
convention at lines 1130-1139 and by the integrated Rabin tuple at
`logic-in-computer-science.tex:726-738`.

The reservoir proof at lines 1245-1248 establishes existence of enough names;
it does not establish uniqueness of the assignment.  By contrast, the Safra
expanded-manuscript presentation explicitly fixes a traversal order and least
unused-name rule at lines 972-979.  Thomas's presentation needs the same kind
of eliminable representative choice: fix an order of the new nodes and assign
the least available names in that order.  Until such a rule is stated, the
claimed deterministic Rabin automaton and Proposition 5.6 reconstruction are
not fully defined.

## 3. Appendix B's eventuality transition is missing, contrary to the integrated “complete construction” claim

The local component is specified by exact state conditions and exact
consecutive-state clauses at `n-c-013.tex:97-132`.  The eventuality component,
however, is given only the state set, initial state, and accepting state at
lines 134-145.  Lines 135-138 say verbally that it "collects unsatisfied until
formulas and carries each one," but omit the proof-critical batching rule: new
pending eventualities are collected when the current obligation set is empty;
while it is nonempty, the update only retains members of that current batch
whose right operands have not yet become true.  No exact transition or timing
clause says whether discharge and recollection occur in the same step or which
local type controls them.

The omission is material.  If "collects" is read as adding every currently
unsatisfied until formula at every step, a word alternating (p) and
(\neg p) while satisfying recurrent obligations (Fp) and (F\neg p) can
keep at least one obligation present forever: one is discharged exactly when
the other is recollected.  The empty obligation state then fails to recur even
though each eventuality is fulfilled.  The source construction avoids this by
finishing one finite batch before collecting another.

The product sets and count at lines 139-155 are correct once the intended
transition is supplied:

\[
 |N_M|\leq 2^{|cl(\varphi)|}2^{|e(\varphi)|}
 \leq 2^{3|\varphi|},
\]

and the single-start conversion then adds one state.  But those sets and the
bound do not define the missing transition.  The integrated theorem's claim at
`logic-in-computer-science.tex:750-756` that the section contains the
"complete construction" is therefore false on the current text.  Required
repair: state the exact eventuality update, including its empty-set batching
and local-state timing, and either give the induced product transition or
narrow "complete construction" to the actual summary strength.

## 4. The registered source versions remain openly undischarged

This is a source-strength incompleteness, not a false attribution in the prose.
The compact row `spec/registers/new-content.csv:120` names McNaughton 1966,
Safra 1988, and Thomas 1997.  The manuscript correctly says that the
McNaughton article body was not read and withholds its definitions and proof
(`n-c-013.tex:829-853`); confines the detailed Safra construction to the 1995
author-hosted expansion rather than the unread 1988 proceedings body (lines
855-870 and 1099-1106); and confines the Thomas reconstruction to the May 1996
report rather than the registered 1997 chapter (lines 1108-1110 and
1296-1300).  Those are mathematically responsible boundaries.  They also mean
that the literal registered-source obligation is not complete and must not be
reported as such.

# Exhaustive line audit

The following records the remainder of the direct mathematical check.  No
additional defect was found in these passages beyond the blockers above.

## Vardi--Wolper semantics, conversion, construction, and model checking

- **Lines 17-40:** The computation type and the (X) and non-strict (U)
  clauses are coherent.  The right operand of until may hold at the current
  point, and truth of a computation is correctly taken at position zero.

- **Lines 42-60:** The source permitted-start-set Buechi tuple, one-based input
  lettering, transition timing, recurrence condition, and distinction between
  semi-determinism and determinism are mutually consistent.  In particular,
  semi-determinism constrains each transition image to have size at most one
  but permits several starts.

- **Lines 62-83:** The permitted-start-set-to-single-start conversion is
  correct in the handbook's zero-based convention.  A new run consumes the
  first letter while moving from the fresh state to a successor of an old
  permitted start.  Removing the old start's single position-zero occurrence
  and inserting the fresh nonaccepting state's single occurrence cannot change
  infinite recurrence.  When (Q_0=\varnothing), the fresh state has no
  outgoing transition on any letter, hence there is no infinite run and both
  languages are empty.  The construction adds exactly one state and does not
  claim to preserve semi-determinism, which in general it would not.

- **Lines 85-95:** The (2^{O(|\varphi|)}) translation bound and the separate
  linear-time/nondeterministic-logspace emptiness statements have the correct
  standings.

- **Lines 97-132 and 139-162:** The closure set, local consistency conditions,
  next/until one-step conditions, (N_L), (N_\varphi), product state set,
  permitted initial set, accepting set, and inequalities are all correctly
  typed and counted.  Projection of closure types to proposition valuations
  does not change the state count.  The only defect in this portion is the
  missing eventuality transition identified in Finding 3.

- **Lines 164-200:** With the source transition
  (s'\in\rho(s,a)\) iff (sRs') and (a=V(s)), the first consumed letter is
  the label of (s_0), so the accepted word is
  (V(s_0)V(s_1)\ldots).  The displayed tuple-order inconsistency is correctly
  treated as a source presentation defect rather than as a second mathematical
  convention.  The reduction
  (L(A_P)\subseteq L(A_\varphi)) iff
  (L(A_P)\cap L(A_{\neg\varphi})=\varnothing) is exact and uses formula
  negation rather than automaton complementation.

- **Lines 201-219:** The special product needs no additional Buechi phase bit
  because the program factor designates every state.  The state and
  two-parameter time/space bounds are consistent.  The PSPACE lower bound is
  kept separate from Vardi--Wolper's upper-bound theorem.

- **Lines 221-241:** The worked (Fp) counterexample respects the same timing.
  The branch (s_0b^\omega) reads only letters omitting (p), remains in the
  accepting state of the (G\neg p) automaton, and projects from the accepting
  product cycle to the stated ultimately periodic program counterexample.

- **Lines 243-268:** The past-operator extension and the three (ETL)
  acceptance modes have distinct and correctly stated meanings.  Finite-prefix
  success, existence of an infinite run, and recurrent success are not
  conflated, and the (O(\exp(|\varphi|^2))) claim is left at cited-source
  strength.

- **Lines 270-309:** Cylinder probabilities, measure-one satisfaction, and
  the warning that measure-zero counterexamples may be nonempty are correct.
  The Streett implication and the representation of Buechi acceptance by
  ((S,F)) are correct because every infinite run over finite (S) recurs in
  some state.  The printed conversion-direction inconsistency is not promoted
  to a theorem.

- **Lines 311-420:** The grammars of (TL(F)), (TL(X,F)), (TL(Y,S)), and
  (past\text{-}TL(X,F)) are stated with the correct constructor distinctions;
  the last forbids future operators in the scope of a past operator.  Ordinary
  and (k)-limit equivalence retain exactly the finite prefix/window needed by
  the corresponding fragments.  Probabilistic fairness is a path condition,
  not universal-path quantification.  The time/space bounds and all deferrals
  to a later full paper are kept separate.

## Buechi 1962: regular formulas, recurrent normal form, and S1S corollary

- **Lines 438-466:** The standing of (SC), the individual and monadic
  domains, and the truth-value-word encoding are correct.  The assignment word
  is not confused with an automaton run.

- **Lines 468-514:** The displayed (\Sigma_1), (\Pi_1), higher-level, and
  (\Sigma_1^\omega) schemata have consistent quantifier polarity.  The
  infinitely-often quantifier
  (\forall x\,\exists t>x) has the intended recurrence meaning.

- **Lines 516-548:** The finite-data extraction from a recurrent formula is
  exact.  An auxiliary bit sequence starts in (Q_0), consumes input
  (\mathbf i(n)) on the transition from (q_n) to (q_{n+1}), and visits
  (F) infinitely often.  The possible multiplicity of (Q_0) and the
  nondeterminism of (B[a,q,q']) are correctly retained.  Applying the fresh
  single start is language preserving, including when the formula has no
  permitted initial code.

- **Lines 550-574:** The (\Sigma^0) regular-formula schema is correctly
  indexed: initialization is at (x), transitions consume precisely the
  letters at (x\leq t<y), and the final test is at (y).  Its truth therefore
  depends exactly on
  (\mathbf i(x)\ldots\mathbf i(y-1)), including the empty-word case (x=y).

- **Lines 576-638:** The two-sided finite-rank congruence, multiperiodic
  standing, Sequential Lemma with all (p<q), finite recursion, and the
  three-way regular-language bridge are coherent.  The proof dependencies on
  the 1960 paper and Rabin--Scott remain explicit.

- **Lines 640-669:** The conjunction scheduler, complement congruence, and
  count (2^{2m^2}) are correct: there are two Boolean reachability facts for
  each of the (m^2) ordered state pairs.  The homogeneous-block
  factorization requires nonempty repeated blocks and is not confused with an
  ultimately periodic single word.

- **Lines 670-697:** The collapse to recurrent existential form and the modern
  automata corollary have the correct ownership.  Conversely, a finite tuple of
  predicate bits can encode automaton states; the propositional matrices can
  exclude unused codes and enforce initial, transition, and recurrent codes.
  Thus the two language classes coincide extensionally without retrojecting a
  modern tuple into the article.

- **Lines 699-728:** The finite stem--cycle decision proof is sound.  From an
  infinite satisfying sequence, a recurrent (L)-state supplies a reachable
  stem and a nonempty return cycle.  Conversely, repeating that cycle is a
  model.  Simple stems/cycles need no more than (2^k) edges, and no modern
  complexity bound is inferred.

- **Lines 730-827:** The finite-set and ultimately-periodic restrictions,
  arithmetic consequences, source notation discrepancy, and open synthesis
  problem are kept at their stated source strength.  The ultimately periodic
  definition correctly requires a positive period.  No unproved completeness
  system or synthesis algorithm is asserted.

## Safra's expanded manuscript

- **Lines 855-870:** The 1988 proceedings/1995 expanded-manuscript boundary is
  explicit and correct; detailed claims are not attributed to the unread
  proceedings body.

- **Lines 872-943:** The total deterministic convention, Buechi/Muller/Rabin
  conditions, strict-ancestor corrections, inclusive specificity definition,
  and tree invariants are coherent.  In Safra's order, (L_i) is the recurring
  good component and (U_i) the eventually absent bad component.

- **Lines 945-986:** The chosen initial name and six-stage update define a
  function because lines 972-979 fix both a traversal order and a least-unused
  renaming rule.  Transition-image monotonicity preserves child containment;
  leftmost horizontal pruning restores branch disjointness; empty deletion and
  collapse restore proper child-union containment.  Every survivor then has a
  specific original state, proving the (n)-node/name bound.

- **Lines 988-1014:** The rejecting sink is necessary when the advanced root
  is empty and correctly makes the target transition total.  Putting it in
  every bad set and no good set makes it reject.  The (n) pairs have the
  correct Safra ordering and acceptance polarity.

- **Lines 1016-1061:** The lineage explanation and both correctness directions
  are mathematically adequate.  Between successive green events, finite run
  segments contain an (F)-visit; the finite predecessor tree supports
  Koenig's lemma.  Conversely, horizontal responsibility moves only toward
  older siblings and bounded strict label descent forces a persistent,
  infinitely green witness.

- **Lines 1063-1097:** Adding an absent-state symbol to the label encoding
  repairs the printed (n^n) omission.  The bounds
  ((n+1)^n=2^{O(n\log n)}), (3^n), and the ordered-tree count combine to
  (2^{O(n\log n)}).  The (n!) lower bound supports only optimality up to a
  constant in the exponent.  The application target classes and pair counts
  are not conflated.

- **Lines 1099-1106:** The distinction between the expanded manuscript's
  (n)-name/(n)-pair presentation and Thomas's (2n)-name/(2n)-pair
  presentation is correctly maintained.

## Thomas's 1996 report precursor

- **Lines 1108-1166:** The word-automaton run timing and total deterministic
  transition are correct.  Thomas's Rabin order
  ((E_i,F_i)) means eventually absent bad component followed by recurrent
  good component.  The displayed Streett clause is its universal dual, so
  recurrence in (F_i) requires recurrence in (E_i).  This order agrees with
  the integrated definition and is correctly distinguished from Safra's
  notation.

- **Lines 1168-1189:** The finite-union (U_jV_j^\omega) characterization is
  correctly qualified by unbounded concatenated length, so epsilon factors do
  not manufacture a finite word.  Total deterministic Muller complementation
  is valid, and the deterministic-Buechi nonclosure example has the right
  polarity.

- **Lines 1191-1213:** The Safra-tree tuple gives separate standings to the
  ordered tree, subset labels, injective persistent names, and current-update
  marks.  Clearing predecessor marks is required and correctly stated.

- **Lines 1214-1239:** The update order is internally coherent.  Advancing a
  child label preserves inclusion in the advanced parent label.  Deleting a
  duplicate through the entire younger-sibling subtree is exactly what is
  needed to preserve descendant containment, and sibling-level processing
  handles arbitrary non-ancestral duplicates through their first divergent
  siblings.  Empty deletion and collapse restore the two tree invariants.  The
  separate absorbing empty tree closes the empty-root case and rejects every
  continuation.  No defect remains in horizontal deletion or root definedness.

- **Lines 1240-1272:** Pairwise-distinct fresh names outside the predecessor
  name set preserve injectivity, and the (2n)-name reservoir/count is
  sufficient.  The (E_k,F_k) polarity, empty-state placement, current-mark
  example, (2^{O(n\log n)}) state bound, (2n) pair count, and factorial
  lower-bound qualification are correct.  The sole failure in this range is
  the missing deterministic choice of the new names identified in Finding 2.

- **Lines 1274-1294:** The Buechi/MSO equivalence, repaired accepting-cycle
  criterion, bounded-quantifier normal form, and weak-MSO corollary are
  coherent.  A reachable cycle without (F) would not suffice; the manuscript
  correctly requires a reachable nonempty cycle containing an (F)-state.

- **Lines 1296-1300:** The 1996-precursor boundary is stated exactly and makes
  no claim about the literal 1997 body or the other original sources.

## Integrated core, model-checking product, and adjacent theorems

- **`logic-in-computer-science.tex:723-744`:** The deterministic Rabin tuple is
  total and its pair order matches Thomas: (E_i) is avoided infinitely often
  and (F_i) is met infinitely often.  It is correctly a word-automaton
  condition, not an infinite-tree run.  The missing parity mode is Finding 1.

- **Lines 746-757:** The exponential theorem, (2^{3|A|}) permitted-start
  product bound, and one-state conversion are numerically correct.  The phrase
  "complete construction" is blocked by Finding 3.

- **Lines 759-762:** Union, intersection, and effective complement closure of
  nondeterministic Buechi languages are correct, and no trivial deterministic
  Buechi complementation is asserted.

- **Lines 764-797:** The product consumes the initial structure label exactly
  once in the initial automaton transition, then consumes each target state's
  label on the corresponding structure edge.  Hence a product path
  ((s_0,q_1),(s_1,q_2),\ldots) corresponds to the word
  (\ell_A(s_0)\ell_A(s_1)\ldots) and automaton run
  (q_0q_1q_2\ldots).  The SCC criterion correctly requires both an
  (F)-coordinate and a genuine cycle, including a self-loop for a cyclic
  singleton SCC.  Projecting a lasso gives an infinite counterexample path.

- **Lines 792-812:** Explicit product search is linear in the product graph.
  On-the-fly formula translation/emptiness gives polynomial space in the
  combined input, and the existential-path PSPACE lower bound transfers to the
  universal statement by formula negation and
  (\mathsf{PSPACE}=\mathsf{coPSPACE}).  For fixed formula/automaton, the
  product factor is constant and the check is linear in the explicit
  structure.  The PSPACE lower bound is not misattributed to Vardi--Wolper's
  upper-bound theorem.

- **Lines 814-828:** The finite-word Buechi--Elgot--Trakhtenbrot statement is a
  sound modern packaging.  Order and successor with definable endpoints have
  equivalent MSO expressive power on finite words, and the prose does not
  claim verbatim priority for the modern sentence.

- **Lines 830-846:** The S1S theorem correctly restricts the displayed word
  corollary to formulas with no free individual variables, preserves full
  monadic-set semantics, and distinguishes Buechi's recurrent normal form from
  the handbook-owned automaton packaging.  The decision statement includes the
  effective normal-form step before the finite stem--cycle test and makes no
  complexity claim.

- **Lines 848-851:** The S2S sentence states only the standard decidability
  conclusion and does not import later Thomas proofs into Rabin's source.

- **Lines 853-903:** The ranked-alphabet, finite-tree, bottom-up run, and root
  acceptance definitions are correctly typed.  MSO and weak MSO coincide on a
  finite position domain because every subset is finite; the text correctly
  refuses to transfer that coincidence to the infinite successor tree.
  Subset determinization, Boolean closure, membership, and upward-reachability
  emptiness are the right finite-tree consequences.

- **Lines 905-920:** The source-presentation inputs occur after the shared
  definitions and before the next section.  The `N-c-013` input itself is
  present at line 910; its presence does not cure Findings 1-4.

# Verdict

The permitted-start conversion (including (Q_0=\varnothing)), Appendix-B
sets and count, all restricted-fragment grammars, Buechi's (\Sigma^0)
schema and modern S1S corollary, Thomas's subtree-wide horizontal deletion,
both Rabin pair orders, the product timing, and the PSPACE attribution all pass
direct mathematical scrutiny.  The snapshot nevertheless fails because parity
acceptance is absent, Thomas's exact-name update is not a function, Appendix
B's eventuality transition is missing despite a "complete construction"
claim, and the registered final-source versions remain explicitly open.
