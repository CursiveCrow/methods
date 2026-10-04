# Part VII R2b — proof-theory/type-theory topic specialist

## Focused disposition

The former R2 blocking objection is closed.  My position changes because the
arbitrary-multiplicity multiset-Mix proof that I rejected no longer occurs in
the live route.  It has been replaced by an exactly defined finite-set support
calculus in
`handbook/parts/p07/arithmetic-proof-theory-supplement.tex:94-157` and a
unit-Cut reduction proof in
`handbook/annex/p07/arithmetic-proof-theory-supplement.tex:6-127`.  In that
presentation contraction is not an inference, so the invalid nested
same-rank/multiplicity step from R2 has no analogue.

### 1. Presentation, nonclean erasure, and rule coverage — checked clean

- The objects and rules are fixed before the measure: sequents have finite-set
  contexts; the logical rules are literal support images; identity and
  \(\bot L\) are contexted; weakening is finite-context monotonicity; exchange
  and contraction are identities; Mix is absent; and support Cut is displayed
  explicitly (`parts/p07/arithmetic-proof-theory-supplement.tex:94-113`).
  This is an eliminable presentation of the propositional restriction of
  `sheet:lk-defneg`, not an undeclared new logic.
- The definition of clean Cut is sufficient.  If the Cut formula \(A\) occurs
  in \(\Gamma\) or \(\Pi\), the right premise weakens to the conclusion; if it
  occurs in \(\Delta\) or \(\Sigma\), the left premise weakens to the
  conclusion (with the symmetric choices when several of these conditions
  hold).  The strategy now selects the first nonclean Cut and erases it before
  selecting a clean maximal-rank Cut
  (`parts/p07/arithmetic-proof-theory-supplement.tex:110-113,146-152`;
  `annex/p07/arithmetic-proof-theory-supplement.tex:8-28`).
- Every zero-premise case is present.  A contexted identity on the Cut formula
  reduces to the other premise; if it is instead an identity on \(B\ne A\),
  \(B\) survives on both sides of the Cut conclusion and that conclusion is
  itself a contexted identity.  The two \(\bot L\) configurations are also
  separated (`annex/p07/arithmetic-proof-theory-supplement.tex:30-43`).
- The nonprincipal permutation is licensed for every unary and binary logical
  rule, monotonicity, and a lower-rank last Cut
  (`annex/p07/arithmetic-proof-theory-supplement.tex:45-58`).  The support-only
  collision is now handled explicitly: if the removed contextual member is
  also an immediate subformula of the other principal formula, monotonicity
  restores that member before the old inference is reapplied
  (`annex/p07/arithmetic-proof-theory-supplement.tex:48-52`).  For example, if
  the Cut formula is \(A\) and the last left inference introduces
  \(A\land B\), cutting its first premise removes the single support member
  \(A\); the stated monotonicity step restores it for \(\land R\).  Thus set
  fusion does not hide an illicit occurrence-level permutation.
- The three possible compound principal pairs are correct and exhaustive.
  The displayed \(\land\) reduction first Cuts on \(B\) and then on \(C\);
  the \(\lor\) reduction uses the two \(\lor L\) branches in turn; and the
  implication reduction Cuts \(E_B\) against the \(\to R\) premise on \(B\)
  and then against \(E_C\) on \(C\).  Their calculated endsequents are exactly
  the original Cut conclusion, including when set union merges contexts, and
  all replacement formulas are proper subformulas
  (`annex/p07/arithmetic-proof-theory-supplement.tex:65-98`).  Atoms have no
  principal logical pair and \(\bot\) has no right introduction, as stated.

### 2. Rank, height, and natural-sum decrease — checked clean

- Rank is finite formula depth, and the Cut height is now defined for **every**
  Cut node before \(o(D)\) sums over all of them
  (`parts/p07/arithmetic-proof-theory-supplement.tex:129-144`).  Hence the
  measured first-nonclean erasure is typed; it removes its own summand and may
  discard additional summands in the unused premise
  (`annex/p07/arithmetic-proof-theory-supplement.tex:8-13`).
- After all Cuts are clean, the selected greatest-rank Cut has no same-rank Cut
  in either premise subtree (`parts/p07/arithmetic-proof-theory-supplement.tex:
  146-152`).  A nonprincipal permutation replaces it by finitely many
  same-rank Cuts whose relevant premise is a proper subtree, so each new
  premise-height sum is strictly smaller.  A duplicated opposite premise can
  contain only lower-rank Cuts.  Restoring a fused support member happens
  outside the new Cuts and therefore does not change those Cut heights.
- A principal reduction produces only proper-subformula Cuts.  If
  \(r'<r\), then \(\omega r'+h'<\omega r\) for every finite \(h'\), so even
  arbitrarily tall lower-rank replacements lie below every exponent belonging
  to rank \(r\).  A commuting reduction replaces
  \(\omega^{\omega r+h}\) only by finitely many terms
  \(\omega^{\omega r+h_i}\) with \(h_i<h\), plus lower-rank terms; an erasure
  contributes none.  Therefore, in the Hessenberg natural sum, the coefficient
  at the greatest changed exponent decreases.  This proves
  \(o(D')<o(D)<\omega^{\omega^2}\)
  (`annex/p07/arithmetic-proof-theory-supplement.tex:100-108`).
- Ordinal well-foundedness then terminates the fixed strategy, and a stopped
  finite derivation cannot contain a Cut because either its first nonclean Cut
  or an uppermost greatest-rank clean Cut would be eligible
  (`annex/p07/arithmetic-proof-theory-supplement.tex:110-112`).  The theorem
  correctly limits the claim to this strategy rather than claiming strong
  normalization of arbitrary reduction orders
  (`parts/p07/arithmetic-proof-theory-supplement.tex:173-183`).

### 3. Both support translations — checked clean

- In the forward induction, multiset exchange and contraction become
  identities; primitive Cut becomes support Cut; primitive multiset Mix
  becomes support Cut on the Mix formula; and every logical/weakening rule is
  its support instance.  If extra copies make a Cut or Mix image nonclean, the
  already proved monotonicity erasure applies
  (`parts/p07/arithmetic-proof-theory-supplement.tex:120-127`;
  `annex/p07/arithmetic-proof-theory-supplement.tex:114-119`).  This explicitly
  covers the primitive Mix row on
  `handbook/registry/calculi/lk-defneg.tex:13`; it no longer invokes a target
  rule that the set presentation omitted.
- In the return induction, choose one occurrence of each support member,
  simulate contexted identity from the sheet's identity plus weakening,
  simulate monotonicity by weakenings, and realize each logical support rule by
  the matching multiset rule.  Weakening supplies a displayed copy when union
  had fused it with a context member, and contraction removes the resulting
  duplicate; final weakenings restore the original endsequent multiplicities.
  Since the input set derivation after reduction contains no Cut, this
  simulation uses neither Cut nor Mix
  (`annex/p07/arithmetic-proof-theory-supplement.tex:120-125`).  The body now
  accurately distinguishes this preservation claim from the forward mapping
  of a source Mix to support Cut
  (`parts/p07/arithmetic-proof-theory-supplement.tex:125-127`).

### 4. Purely relational Maehara proof — regression checked clean

The body still restricts the locally proved lemma to a purely relational
signature with no equality, functions, or constants, defines both the common
predicate condition and the common-free-variable condition, and keeps general
function-bearing Craig/Beth at cited standing
(`handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:64-140`).
The annex still covers both initial forms, structural rules, both placements of
all unary and binary propositional rules, and all quantifier placements
(`handbook/annex/p07/interpolation-supplement.tex:8-135`).

In particular, the repaired non-eigenvariable argument at annex lines 72-94
is sound.  Because the instantiating term is a variable in the purely
relational signature, and because the induction hypothesis already imposes
the common-free-variable condition, a variable occurring in \(I\) but ceasing
to be common after replacement of the principal instance can remain only on
the opposite half.  A first-half principal therefore permits
\(J=\forall z I(z)\) (original rule, then \(\forall R\), with \(\forall L\)
on the other required sequent); a second-half principal permits
\(J=\exists z I(z)\), after the stated fresh renaming needed for
\(\exists L\).  The eigenvariable cases at lines 96-132 respect their
freshness conditions.  No alien compound term is silently lifted.

### 5. Haken boundary — regression checked clean

The body retains exactly the nonfunctional \(\mathsf{PHP}^{n}_{n+1}\) CNF and
the general DAG-like resolution size measure
(`handbook/parts/p07/proof-complexity.tex:63-96`).  The annex correctly counts
\((n+1)n!\) critical injections, observes that each falsifies its unique omitted
pigeon's totality clause, and gives the sound backwards routing step through a
resolvent (`handbook/annex/p07/proof-complexity.tex:11-26`).  Most importantly,
it no longer substitutes the false "number of pigeons mentioned" heuristic.
It explicitly marks the full bottleneck predicate, numerical constants,
critical-assignment count, and DAG bookkeeping as omitted imported material,
then uses only the resulting exponential charging estimate
(`handbook/annex/p07/proof-complexity.tex:5-10,28-46`).  That is honest
`sketched` standing, not a claim of a local complete proof.  The theorem domain
and exponential conclusion agree with Haken's original result and the
Beame--Pitassi account: [Haken 1985](https://doi.org/10.1016/0304-3975(85)90144-6),
[Beame--Pitassi survey](https://homes.cs.washington.edu/~beame/papers/proofsurvey.pdf),
and the authors' explicit DAG/PHP treatment in
[Beame--Pitassi 1996](https://homes.cs.washington.edu/~beame/papers/focsclause.pdf).

No mathematical or source-content blocker remains in the R2b scope.  No build,
test, or visual claim is made.

ACCEPT
