# Kozen Figure 2: a complete finite/cofinite proof

Date: 2026-09-06. Status: supplied mathematical proof, not a recovered proof
from the cited unpublished manuscript. No manuscript build or independent
review is claimed by this note.

## Exact statement and source boundary

Let the states be \(\mathbb N=\{0,1,2,\ldots\}\), and put
\[
 R_a=\{(n+1,n):n\geq0\}
       \cup\{(2k+3,2k+1):k\geq0\}.
\]
Interpret every ordinary proposition constant as the empty set, and the
Boolean constants 0 and 1 as the empty set and all of \(\mathbb N\).
Programs are built from a by union, composition, star, formula tests, and
converse. Formulas are closed PDL formulas with Boolean operations and
program modalities. Converse is relational inverse, not a new independent
primitive relation.

**Theorem.** Every such formula denotes a finite or cofinite state set.

This is the finite/cofinite side of the assertion at Proposition 4.2 and
Figure 2, printed p. 340, physical PDF page 5 of the
[author-hosted Kozen scan](https://www.cs.cornell.edu/kozen/Papers/mu.pdf).
The paper attributes the proposition to reference [12], identified on
printed p. 354, physical PDF page 12, as the unpublished manuscript
*On the expressiveness of mu*. The published article does not print the
proof. The argument below is supplied here, not attributed to that unseen
manuscript. The valuation above explicitly completes the unlabeled figure;
the claim would fail for arbitrary primitive-proposition valuations.

The existing `p09-kozen-1983-source-note.md` separately proves that
\(\mu X.[a]\langle a\rangle X\) denotes the even states on this exact
frame. The present theorem completes the mathematical single-model
separation for the stated signature and valuation.

## 1. A word lemma on the bi-infinite extension

For this section only, extend the frame to all integers: a has every
unit downward edge and every downward edge of length two between odd
integers. Write b for the converse of a. Thus either letter always permits
its unit step; a also permits a downward skip of length two from an odd
state, and b an upward skip of length two from an odd state. Every finite
walk can be translated by an even integer. A realization of a word is a
walk whose successive edge labels spell that word, in execution order.

**Word lemma.** Suppose a nonempty word w over \(\{a,b\}\) has a
realization from an integer to a strictly smaller integer of the same
parity. There is a constant \(C_w\geq0\) such that, for every integer
\(B\geq0\) and every \(y\geq B+C_w\), all sufficiently large integers x
have a realization of a power of w from x to y entirely within
\(\{B,B+1,\ldots\}\). The threshold for x may depend on B and y.

**Proof.** We first work without a lower boundary.

1. Both parity types communicate under powers of w. If the length of w
   is odd, its all-unit realization changes parity from either starting
   parity. If its length is even, it is at least two. For either starting
   parity, one of the first two letters of its all-unit realization has
   an odd source. Replacing that one unit step by the available skip,
   and leaving all other steps unit, changes the endpoint parity.
   Consequently there are fixed realizations of powers of w from either
   parity type to the other. Identity walks cover a type to itself.

2. The doubled word ww contains two adjacent identical letters. Otherwise
   w is an even-length alternating word, either \((ab)^k\) or
   \((ba)^k\). Direct calculation shows that ab relates precisely the
   two members of each pair \(\{2j,2j+1\}\), in both directions and
   including both identity pairs. Similarly ba is precisely the union
   of complete relations on \(\{2j-1,2j\}\). Their positive powers
   are unchanged. Such a w therefore cannot have a strictly descending
   same-parity realization, contrary to the hypothesis.

3. Put \(d=\#b(w)-\#a(w)\). The all-unit realization of ww has
   displacement \(2d\). Choose a starting parity t so that the source
   at the adjacent identical letters from step 2 is odd. Replace those
   two unit steps by two skips. The first skip leaves the state odd, so
   the second is available. This changes the total displacement by
   \(2\sigma\), where \(\sigma=-1\) for aa and \(\sigma=1\) for bb.
   Both realizations start and end in parity t. Measuring same-parity
   displacements in units of two, they give two t-to-t walks, each
   reading a power of w, with integer displacements d and
   \(d+\sigma\).

4. The negative same-parity realization in the hypothesis has cell
   displacement \(-c\), for some \(c\geq1\), at a parity u. Use the
   fixed parity bridges from step 1 to go from t to u and back. Their
   combined cell displacement is an integer e. Inserting N copies of
   the negative realization between them gives a t-to-t walk of cell
   displacement \(e-Nc\). Choose N so that this is an integer h<0.
   Append the same sufficiently large number K of copies of this walk
   to each of the two walks in step 3. The resulting displacements
   \(d+Kh\) and \(d+\sigma+Kh\) are consecutive negative integers.
   Thus there are fixed t-to-t walks, reading powers of w, with cell
   displacements \(-r\) and \(-(r+1)\), for some \(r\geq1\).

5. Every integer \(L\geq r(r-1)\) is a nonnegative integral combination
   of r and r+1. Indeed, write \(L=qr+s\), with \(0\leq s<r\).
   Then \(q\geq r-1\geq s\), and
   \(L=(q-s)r+s(r+1)\). Concatenating the two fixed walks from step 4
   therefore connects every sufficiently high state of parity t to
   any prescribed lower state of parity t. The fixed parity bridges
   extend this conclusion to either starting and either target parity.

Here is the boundary check for the last step. There are only two fixed
descending walks in step 4. Choose \(K_0\geq0\) such that neither walk
ever falls more than \(K_0\) below its endpoint. A concatenation whose
final endpoint is z stays at least \(z-K_0\), because its successive
endpoints strictly decrease.

For each target parity p, fix an output bridge from t to p. Let its
displacement be \(\delta_p\), and let \(m_p\) be the minimum displacement
of a prefix of this bridge, including the empty prefix. To end at y the
bridge starts at \(z=y-\delta_p\), and it stays at least
\(y-\delta_p+m_p\). Choose an integer
\[
 C_w\geq
 \max_{p\in\{\mathrm{even},\mathrm{odd}\}}
       \{0,\delta_p+K_0,\delta_p-m_p\}.
\]
Then \(y\geq B+C_w\) keeps both the descending concatenation and the
output bridge at least B. For each starting parity, fix an input bridge
to t. All sufficiently large starting x keep that fixed bridge at least
B and make the remaining cell difference to z at least \(r(r-1)\).
Step 5 fills that difference exactly. Taking the larger of the two
starting thresholds proves the assertion for all sufficiently large x.
All walks so obtained lie in the original half-line frame. QED.

## 2. Finite automata with finite/cofinite tests

A guarded finite automaton here has a finite set Q of control states, an
initial state \(q_0\), a set of final states, and finitely many transitions
labeled a, b, or \(D?\), where \(D\subseteq\mathbb N\) is finite or
cofinite. A configuration is \((q,n)\). An a- or b-transition changes n
along the corresponding frame edge; a \(D?\)-transition changes only q
and requires \(n\in D\). An epsilon transition is the special case
\(D=\mathbb N\). Acceptance means a finite execution ending at a final
control state, with no restriction on its final numerical state.

**Automaton lemma.** The set of starting numerical states from which
such an automaton accepts is finite or cofinite.

**Proof.** Choose \(B\geq0\) such that every guard has constant truth
value on \(\{B,B+1,\ldots\}\). Form the high-tail control graph by
deleting guards that are false there and treating every remaining guard
as an epsilon edge.

If this graph has a control path from \(q_0\) to a final state, fix one
such path. Realize each a and b by its unit step. From all sufficiently
large starting states the whole finite path remains at least B, so all
its guards hold. The accepted set is then cofinite.

Suppose instead that no such control path exists. Every accepting
execution starting at least B must visit a numerical state below B.
If the accepted set is bounded, it is finite and there is nothing to
prove. Assume it is unbounded.

Above B, project configurations to the finite weighted graph G with
vertices \(Q\times\{\mathrm{even},\mathrm{odd}\}\). Its transitions
are those of the high-tail control graph together with the possible
parity changes and numerical displacements:

| Letter | Source parity | Target parity | Displacement |
|---|---|---|---:|
| a | even | odd | -1 |
| a | odd | even | -1 |
| a | odd | odd | -2 |
| b | even | odd | +1 |
| b | odd | even | +1 |
| b | odd | odd | +2 |
| epsilon | either | unchanged | 0 |

Keep distinct edges when their control transitions differ. A cycle
displacement is the sum of its edge displacements. For each negative
simple cycle of G, choose a base vertex and let w be its sequence of
non-epsilon labels. It has a negative same-parity realization on the
bi-infinite frame, so w is nonempty and the word lemma applies. There
are finitely many such simple cycles. Choose H at least B and at least
\(B+C_w\) for all their words. If there are none, just take H=B.

Write \(s=2|Q|\). By unboundedness choose an accepted starting state
\[
 x>H+1+2(s-1).
\]
Fix an accepting execution. It eventually goes below B. Stop its prefix
at the first numerical state strictly below H+2. The prefix begins at
x, ends at H or H+1, and stays at least H: the last step decreases by
at most two. Its projection to G therefore has displacement strictly
less than \(-2(s-1)\).

Every finite walk in a finite graph decomposes into a simple path and
simple cycles: remove a segment between repeated vertices, and repeat,
decomposing each removed closed walk in the same way. A simple path in
G has at most s-1 edges and hence displacement at least
\(-2(s-1)\). The projected prefix must consequently contain, in this
decomposition, a negative simple cycle. This also rules out the case
where G had no such cycle. Every vertex of the selected cycle occurred
on the original prefix, even if the cycle was obtained after other
segments were removed.

Let q be its chosen base control state, w its word, and y the numerical
state at an occurrence of the base vertex on the original prefix.
Then \(y\geq H\geq B+C_w\). Retain the original accepting suffix
from \((q,y)\). The selected simple cycle is a control walk from q
back to q, and all its guards are true above B. Any realization of a
power of w staying above B can therefore follow that control walk the
corresponding number of times, inserting its epsilon/guard transitions
at their prescribed positions.

Finally retain the original control prefix from \(q_0\) to this
occurrence of q, but realize its a and b edges by unit steps. From
every sufficiently large new starting state z this fixed prefix stays
above B and reaches \((q,z+d_0)\), for one fixed integer \(d_0\).
The word lemma connects all sufficiently large \(z+d_0\) to y by
powers of w above B. Append the retained accepting suffix. Thus every
sufficiently large z is accepted. The unbounded accepted set is
cofinite, completing the proof. QED.

## 3. Application to the full stated PDL syntax

Use induction on formula size, counting formulas inside program tests
as proper syntactic subexpressions. Primitive propositions denote the
empty set; 0 and 1 denote finite/cofinite sets. Finite/cofinite sets are
closed under complement and every finite Boolean combination.

For \(\langle\pi\rangle\varphi\), the induction hypothesis makes
the denotation of \(\varphi\) and of every formula tested in \(\pi\)
finite or cofinite. Normalize converse using
\[
 (\alpha\cup\beta)^{-1}=\alpha^{-1}\cup\beta^{-1},\qquad
 (\alpha;\beta)^{-1}=\beta^{-1};\alpha^{-1},\qquad
 (\alpha^*)^{-1}=(\alpha^{-1})^*,\qquad
 (\psi?)^{-1}=\psi?,\qquad
 (\alpha^{-1})^{-1}=\alpha.
\]
The result is a regular expression over a, b, and the finitely many
test symbols, where b denotes \(R_a^{-1}\). Convert this expression
to a finite guarded automaton. Explicitly, an atomic expression has
one labeled edge; union makes a new entrance and exit with epsilon
edges to and from the two automata; composition joins the first exit
to the second entrance by epsilon; star adds an epsilon path for zero
iterations and an epsilon edge from the body exit back to its entrance.
Induction on these constructions proves equality between program
executions and accepting automaton executions, including empty paths
and all finite iteration counts.

At the program automaton's exit append one guard for the denotation
of \(\varphi\), leading to a fresh sole final control state. Its
accepted starting states are exactly
\(\llbracket\langle\pi\rangle\varphi\rrbracket\). All guards
are finite or cofinite, so the automaton lemma applies. Boxes follow
by \([\pi]\varphi=\neg\langle\pi\rangle\neg\varphi\).
This completes the induction and proves the theorem. QED.

## Scope and verification record

- The proof includes arbitrary finite nesting of regular iteration,
  formula tests, and converse; it is not a finite-modal-depth argument.
- The only infinite auxiliary structure is the explicitly defined
  bi-infinite frame in the word lemma. Its boundary estimate returns
  every witness used in the automaton proof to the given half-line.
- The argument also works when primitive propositions have any fixed
  finite/cofinite valuation. It does not assert the claim for arbitrary
  valuations, intersection/complement of programs, or added independent
  primitive program relations.
- Primary-source pp. 340 and 354 were visually rechecked against the
  already existing page images. No PDF was generated, no software test
  was run, and no independent review of this new proof is asserted.

## Subsequent independent check and incorporation

A separate reader subsequently challenged the complete proof and reported
no definite mathematical defect, specifically checking parity bridges,
consecutive negative displacements, the uniform lower boundary,
negative-cycle extraction, and exact prefix/suffix joins.
The proof was then incorporated into n-c-018.tex under the label
sec:p09-kozen-finite-cofinite. A further read-back found the LaTeX
incorporation faithful to the checked argument.
These are bounded mathematical checks, not whole-topic or publication
acceptance. No builds, software tests, or manuscript renders were used.
