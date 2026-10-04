# Exact derivations for the three alternation-class examples

Date: 2026-09-06. Status: direct structural derivations from the live
inductively generated formula classes, including lower bounds. This note
does not prove the semantic strictness theorem. It distinguishes syntactic
class membership from equivalence to a formula in another class.

## 1. Actual definitions and source boundary

The controlling reader definitions are `def:p09-mu-calculus` and
`thm:p09-mu-alternation` in
`handbook/parts/p09/logic-in-computer-science.tex`, inspected at current
lines 1037--1086. The three formulas are the final alternation examples
in `handbook/parts/p09/presentations/n-c-018.tex`.

I also read Section 7 of the
[Bradfield--Stirling preprint](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf),
printed pp. 21--23, especially the rules and examples on printed p. 22.
The reader's class-generation rules and symmetric depth convention agree
with those definitions. The source's second example reverses its sided
membership claim: the formula with outer `nu` and inner `mu` belongs to
`Pi_2`, not `Sigma_2`. The proofs below establish the correction from the
rules themselves. The current reader text gives only its symmetric depth,
which is correct.

Write `Sigma_n^T,Pi_n^T`, with `T in {S,EL,N}`, for the three systems,
suppressing only the extra `mu` in their superscripts. Level zero consists
of fixed-point-free formulas, including free fixed-point variables. The
next Sigma level contains both previous levels and is closed under
positive Boolean/modal operations and `mu`; the next Pi level uses `nu`.
System S has no substitution clause; EL allows substitution of a closed
formula; N allows capture-avoiding substitution of an open formula too.
All statements below concern finite positive syntax, up to alpha-renaming,
not closure under semantic equivalence.

## 2. Inclusions, duality, and symmetric indexing

Induction simultaneously on the level and the finite generation
derivation gives, for each side,

\[
 \Sigma_n^S\subseteq\Sigma_n^{EL}\subseteq\Sigma_n^N,
 \qquad
 \Pi_n^S\subseteq\Pi_n^{EL}\subseteq\Pi_n^N.
\]

The base classes coincide. Every S rule is an EL rule; every EL
substitution is an N substitution because a closed formula has no free
variable to capture. The preceding-level inclusions supply the inherited
generators at the next step.

For any one convention T, the definitions also give

\[
 \Sigma_n^T\cup\Pi_n^T
      \subseteq\Sigma_{n+1}^T\cap\Pi_{n+1}^T.
\]

In particular both sided hierarchies are increasing, and membership
on one side at level n gives membership on the opposite side at n+1.

The positive syntactic dual swaps true/false, proposition-literal
polarities, conjunction/disjunction, diamond/box, and mu/nu, retaining
variable names. It preserves free-variable sets and closedness and
commutes with capture-avoiding substitution, up to alpha-renaming.
Induction on the generation rules therefore proves

\[
 A\in\Sigma_n^T\quad\Longleftrightarrow\quad
 A^{\partial}\in\Pi_n^T.
\]

The reverse follows by applying the involution again. For open formulas,
this purely syntactic duality should not be confused with taking a
semantic complement under the same variable valuation: with variable
names retained, the semantic complement identity also complements the
free-variable valuation. For closed formulas no such qualification is
needed.

Let s_T(A),p_T(A) be the least Sigma and Pi levels of A. The reader's
symmetric depth is

\[
 d_T(A)=\max\{0,\max(s_T(A),p_T(A))-1\}.
\]

This is exactly its definition as the least `n>=0` with membership in
`Sigma_{n+1}^T intersect Pi_{n+1}^T`. In particular, fixed-point-free
formulas have depth zero; a pure nonempty least or greatest block has
depth one, not zero. No semantic simplification of vacuous binders is
implicit in these syntactic classes.

## 3. An exact decision recurrence for the simple classes

Define the pair `(s(A),p(A))` recursively:

\[
\begin{aligned}
 (s(A),p(A))&=(0,0)
     &&\text{for constants, proposition literals, and variables},\\
 s(A\circ B)&=\max(s(A),s(B)),
 &p(A\circ B)&=\max(p(A),p(B))
     &&(\circ\in\{\land,\lor\}),\\
 (s(\langle a\rangle A),p(\langle a\rangle A))
     &=(s(A),p(A)),\\
 (s([a]A),p([a]A))&=(s(A),p(A)),\\
 (s(\mu X.A),p(\mu X.A))&=(u,u+1),
       &u&=\max(1,s(A)),\\
 (s(\nu X.A),p(\nu X.A))&=(v+1,v),
       &v&=\max(1,p(A)).
\end{aligned}
\]

These are the actual minimum indices for the S classes, not an informal
count of all binders. Here is a structural proof of the lower bounds.
For a finite sign word w, let r(w) be its number of maximal constant-sign
blocks after adjacent equal signs have been compressed. Set

\[
\begin{aligned}
 c_\mu(\epsilon)&=c_\nu(\epsilon)=0,\\
 c_\mu(w)&=r(w)+\mathbf 1_{\text{first sign of }w=\nu},\\
 c_\nu(w)&=r(w)+\mathbf 1_{\text{first sign of }w=\mu}
                   \qquad(w\ne\epsilon).
\end{aligned}
\]

Read the binder signs along each syntax branch. The displayed
recurrence computes the maxima of c_mu and c_nu over those words.
A contiguous subword has no greater cost on either side than the
original word. Prefixing mu does not increase c_mu beyond the maximum
of its old value and 1, and prefixing nu has the dual property.

Induction on every S generation derivation now bounds these maxima
by the indicated class level. Boolean and modal constructors preserve
the bound. The same-sign binder rule preserves it. Moving from either
previous-level class into the next class is sound because the two
word costs differ by at most one. Hence a computed value greater than
n proves nonmembership in the corresponding class.

Conversely, the recurrence yields derivations at its computed levels:
combine the child derivations for Boolean/modal constructors; introduce
the appropriate binder on its own side; and use the preceding-level
inclusion to reach the other side one level later. Thus

\[
 A\in\Sigma_n^S\iff s(A)\le n,
 \qquad A\in\Pi_n^S\iff p(A)\le n.
\]

## 4. An exact closed-fragment characterization for Emerson--Lei

For any formula A, split its syntax into closed-subformula fragments.
In the current piece, replace every maximal **proper** closed subformula
by a distinct fresh variable, and recursively apply the same procedure
to each removed closed subformula. The piece's root is not removed from
itself. Continue until no proper closed subformula remains. This is a
finite collection of finite formulas, because each recursive call uses
a strict original subformula. Even closed literal leaves may be split;
they have no binder cost.

Then, for either side C and each level n,

\[
 A\in C_n^{EL}
   \quad\Longleftrightarrow\quad
 \text{every closed-subformula fragment of }A
                         \text{ belongs to }C_n^S.
\]

At level zero, both conditions simply say that no fixed-point binder
occurs anywhere; the fragments retain every such binder if one exists.
For the reverse implication at n>=1, reconstruct the removed closed pieces
bottom-up. The simple fragments are already in the EL class. Each
piece inserted at a fresh hole is the original closed formula after
its own reconstruction, so every reconstruction step is an allowed
closed substitution at that same EL level.

For the forward implication, consider binder words within fragments,
equivalently syntax paths that do not cross a proper closed-subformula
boundary. Induct on the EL generation derivation. Boolean/modal rules
and same-sign binder rules obey the costs of Section 3. Introducing
a binder does not remove any closed boundary inside its body. A
closed substitution introduces a boundary at each inserted formula;
it can also make some context subformulas newly closed, creating
additional boundaries. It cannot open an already closed subformula.
Thus every resulting fragment word is a contiguous subword of a
context-fragment word or an inserted-formula-fragment word. Its cost
does not increase. The inherited lower levels are treated as in
Section 3. This proves the forward bound and hence the characterization.

Applying the simple recurrence to every fragment and taking the
componentwise maximum is therefore a finite exact EL decision
calculation. Closedness here means absence of free fixed-point
variables when the subformula is read in isolation: a reference to
an enclosing variable makes that subformula open.

## 5. A substitution-stable Niwinski lower-bound invariant

The following finite structural invariant is enough for all needed N
nonmembership claims. It is not asserted here to be a complete
general-purpose decision algorithm for every N class.

Use clean bound names and binding occurrences. Put an edge

\[
 b_X\longrightarrow b_Y
 \quad\Longleftrightarrow\quad
 b_Y\text{ is a proper descendant of }b_X
                  \text{ and }X\in FV(b_Y).
\]

These edges form a finite acyclic graph because they descend the
syntax tree. For every nonempty directed binder chain, read its sign
word and compute the costs c_mu,c_nu of Section 3. Include singleton
chains, even for vacuous binders. Let h_mu(A),h_nu(A) be the respective
maxima, with maximum zero when there are no binders.

Then

\[
 A\in\Sigma_n^N\Longrightarrow h_\mu(A)\le n,
 \qquad
 A\in\Pi_n^N\Longrightarrow h_\nu(A)\le n.
\]

Proof is by induction on the actual N generation rules. Base,
Boolean/modal, inherited-level, and same-sign binder cases use the
same word-cost facts as before. A newly added root binder can only
prefix its sign to an old dependency chain, or stand alone.

For substitution, first rename bound variables freshly. Since the
substitution is capture-avoiding, a free variable of the inserted
formula cannot acquire a binder from the context. Hence no new
dependency edge connects a context binder to an inserted binder.
An inserted binder cannot enclose a context binder, either. Edges
among context binders are not newly created: that would require the
inserted formula to supply a free occurrence captured by an enclosing
context binder. Every resulting binder chain consequently stays in
the context or within one inserted copy. The bounds for the two
premises preserve the claimed bound for the result.

This proves the lower-bound invariant from the class rules, including
the substitution rule. It is stronger evidence for the examples than
merely counting their visible binder nesting.

## 6. Example 1: closed eventuality inside a greatest block

Let

\[
 E=\mu Z.(P\lor\langle a\rangle Z),\qquad
 A_1=\nu Y.(E\land\langle a\rangle Y).
\]

The simple recurrence gives `(s(E),p(E))=(1,2)`, leaves that pair
unchanged upon conjunction with the fixed-point-free `<a>Y`, and
then gives

\[
 (s_S(A_1),p_S(A_1))=(3,2).
\]

In particular the syntax branch nu Y -> mu Z has sign word nu mu,
whose Sigma cost is 3. This proves `A_1 notin Sigma_2^S`; the recurrence
also gives its explicit `Pi_2^S` derivation.

For the EL Sigma upper bound, let

\[
 F(W)=\nu Y.(W\land\langle a\rangle Y).
\]

Then `F(W) in Pi_1^{EL} subseteq Sigma_2^{EL}`, and
`E in Sigma_1^{EL} subseteq Sigma_2^{EL}`. The formula E is closed,
so substituting E for W proves `A_1 in Sigma_2^{EL}`. Its simple
Pi_2 derivation also puts it in `Pi_2^{EL}`. Inclusions give the same
upper bounds for N.

Every level-one Sigma formula, in any of the three conventions,
contains only mu binders; every level-one Pi formula contains only
nu binders. This follows immediately by induction on the level-one
generation rules, including substitution. A_1 contains both kinds,
so it belongs to neither level-one side. Consequently

\[
 (s_{EL}(A_1),p_{EL}(A_1))
   =(s_N(A_1),p_N(A_1))=(2,2).
\]

The symmetric depths are therefore 2 for S and 1 for EL and N.

## 7. Example 2: the inner least block refers to the outer variable

Let

\[
 A_2=\nu Y.\mu Z.
       ((P\lor\langle a\rangle Z)\land\langle a\rangle Y).
\]

The inner mu formula, with Y free, is in `Sigma_1^S`; inherited
membership in `Pi_2^S` and the nu constructor give `A_2 in Pi_2^S`.
Hence A_2 is in Pi_2 for all three conventions.

For the lower bound there is a dependency edge

\[
 b_Y\longrightarrow b_Z,
 \qquad
 Y\in FV\left(\mu Z.
       ((P\lor\langle a\rangle Z)\land\langle a\rangle Y)\right).
\]

Its sign word is nu mu, with Sigma cost 3. Section 5 therefore gives
`A_2 notin Sigma_2^N`, and the class inclusions give nonmembership in
`Sigma_2^{EL}` and `Sigma_2^S` too. The Pi minimum is 2 because the
formula contains a mu binder; level-one Pi formulas cannot do so.
The opposite-side next-level inclusion gives the Sigma upper bound 3.
Thus, for every convention T,

\[
 (s_T(A_2),p_T(A_2))=(3,2),\qquad d_T(A_2)=2.
\]

This also pinpoints why an attempted low-level substitution fails.
Writing `B(Y)=mu Z.((P or <a>Z) and <a>Y)` and substituting B for W
inside `nu Y.W` would capture its free Y. A capture-avoiding alpha
renaming changes the context binder to a fresh name and leaves Y
free; that result is not A_2. Thus the capture restriction cannot be
evaded by calling the prohibited substitution alpha-renaming.

The source's printed `Sigma_2 but not Pi_2` assertion for this exact
outer-nu formula is reversed. Its symmetric depth 2 remains correct.

## 8. Example 3: open substitution skips an independent middle binder

Let

\[
 B(X)=\mu Z.[-](X\lor Z),\qquad
 A_3=\mu X.\nu Y.([-]Y\land B(X)).
\]

The modality `[-]` does not introduce a binder and has the same
class effect as any box. The simple recurrence gives

\[
 (s_S(B(X)),p_S(B(X)))=(1,2),
\]

then `(3,2)` after the nu Y binder, and finally

\[
 (s_S(A_3),p_S(A_3))=(3,4).
\]

The branch mu X -> nu Y -> mu Z has Pi cost 4, which supplies the
required simple nonmembership in Pi_3.

There is no proper closed subformula in A_3. In particular,
`FV(B(X))={X}`, and the middle nu formula also has free variable X.
The whole formula is closed, but the whole formula is not a proper
piece available to lower its own class membership by substitution.
Section 4 therefore gives exactly the same EL pair:

\[
 (s_{EL}(A_3),p_{EL}(A_3))=(3,4).
\]

For the N upper bound, set

\[
 H(W)=\nu Y.([-]Y\land W).
\]

We have `H(W) in Pi_1^N subseteq Sigma_2^N` and
`B(X) in Sigma_1^N subseteq Sigma_2^N`. The only free variable of
B(X) is X, while the context H binds only Y. Hence the substitution
`H(B(X))` is capture-safe and remains in `Sigma_2^N`. Now introduce
the outer mu X binder by the Sigma_2 binder rule. This proves

\[
 A_3\in\Sigma_2^N.
\]

The order of these operations matters. Substituting B(X) into an
already formed context `mu X.H(W)` would capture X and is not that
allowed substitution. Instead the legitimate open substitution is
performed first, and only then does the permitted binder constructor
bind X.

For the exact lower bound, the dependency graph has edges from the
outer mu X binder to both the middle nu Y binder and the inner mu Z
binder, since each of those formulas has X free. There is no edge
from nu Y to mu Z because `Y notin FV(B(X))`. In particular it has
the chain mu X -> nu Y, whose Pi cost is 3. Hence
`A_3 notin Pi_2^N`. Membership in Sigma_2 implies membership in Pi_3,
and the presence of nu rules out Sigma_1. Thus

\[
 (s_N(A_3),p_N(A_3))=(2,3),\qquad d_N(A_3)=2.
\]

The symmetric S and EL depths are 3, not 2. The current manuscript's
sided S/EL level-three assertions and N Sigma_2 assertion are correct.

## 9. Exact result table and strictness caution

Each entry gives the least Sigma level, least Pi level, and symmetric
depth, respectively:

| Formula | Simple | Emerson--Lei | Niwinski |
|---|---|---|---|
| A_1, closed eventuality inside nu | (3,2,2) | (2,2,1) | (2,2,1) |
| A_2, dependent nu/mu pair | (3,2,2) | (3,2,2) | (3,2,2) |
| A_3, mu/nu/mu with middle-independent inner block | (3,4,3) | (3,4,3) | (2,3,2) |

Every upper bound above has a derivation from the actual rules. Every
lower bound follows from the proved simple recurrence, exact EL
fragment characterization, or substitution-stable N dependency
invariant. None is inferred merely from a semantic equivalence or
an informal picture of binder nesting.

The host theorem correctly restricts semantic strictness to levels
`n>=1`; at level zero the two classes coincide. Syntactic
nonmembership of one displayed formula is not a semantic strictness
witness: it does not exclude an equivalent formula in the other
class.

Finally, the inclusions `S subseteq EL subseteq N` alone do not
logically transfer an arbitrary N-Sigma witness into an S-Sigma
class. A semantic strictness transfer needs the additional fact that
the hard witnesses can be chosen at the corresponding simple Sigma
level, or another same-level translation result. The preprint supplies
an alternating-prefix hard-formula pattern after Theorem 7.1; its
syntactic simple-class membership is immediate from Section 3's
recurrence. Its semantic hardness remains part of the cited
strictness theorem, not a result established by these three easy
class examples. This is a proof-boundary qualification, not a
rejection of the cited strictness statement in the current host.
