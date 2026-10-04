# Craig interpolation by equality-free relationalization

Date: 2026-09-06.

## 1. Claim, hypotheses, and existing proof dependency

Work in classical first-order logic on nonempty domains. Function symbols
have fixed finite arities and denote total functions; a constant is a
function of arity zero. Equality, when used, denotes actual identity.
Predicate symbols may have any fixed finite arity, including zero.
Logical falsehood and truth are available, with truth definable as the
negation of falsehood.

Suppose `A` and `B` are formulas in one consistent signature and

\[
 \models A\to B,
 \tag{1}
\]

where validity for open formulas quantifies over all assignments. The
conclusion is a formula `C` such that

\[
 \models A\to C,\qquad \models C\to B,
 \qquad \operatorname{sig}(C)\subseteq
          \operatorname{sig}(A)\cap\operatorname{sig}(B),
 \qquad \operatorname{FV}(C)\subseteq
          \operatorname{FV}(A)\cap\operatorname{FV}(B).
 \tag{2}
\]

Here `sig` counts predicates, functions, and constants, but not logical
equality or the logical connectives. In particular, equality is permitted
in `C` even if neither input formula contains it. This is the convention
of the existing general Craig statement in
`handbook/parts/p07/cut-elimination-and-interpolation.tex`, under
`thm:p07-craig-interpolation`.

The input used below is the equality-free purely relational interpolation
theorem, with common-predicate and common-free-variable conditions. The
live supplement
`handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex`, under
`thm:p07-maehara-partition`, proves its partition lemma for supplied
cut-free derivations. Turning semantic validity into such a derivation
still requires the exact completeness and cut-elimination results, or a
direct cut-free completeness theorem, for that relational calculus. The
supplement currently marks that bridge as dependent on the inherited
cut-elimination sketch. This note supplies the function/equality reduction;
it does not itself upgrade that independent bridge's proof status.

No additional interpolation theorem, equality calculus, or alien-term
lifting theorem is used in the reduction.

## 2. Finite signatures and new relational symbols

Let `S_L = sig(A)` and `S_R = sig(B)`, and put `S = S_L union S_R`.
These sets are finite because formulas are finite. Signature membership
includes symbol kind and arity, not merely a printed name. Validity may
be checked in this finite signature: an ambient structure can be reduced
to it, and any structure for it can be expanded to unused symbols on its
nonempty domain, choosing one domain element for arbitrary unused
constant or function values if necessary.

Choose a fresh binary predicate `E`. For each n-ary function `f` in `S`,
choose a fresh `(n+1)`-ary predicate `F_f`. Use the same new symbol on both
sides exactly when it represents the same original function. All these
predicates are distinct from each other and from every original predicate.
Keep original predicate names. Thus a constant `c` receives a unary
predicate `F_c`. The new language is purely relational: it contains
neither function symbols, constants, nor logical equality. Its terms
are variables.

Write `S_L^r` for the original predicates on the left together with the
graph predicates of its functions, and define `S_R^r` similarly. The
auxiliary predicate `E` is kept separate from these sets.

## 3. Finite local axiom sets

Let `Eq(E)` be the conjunction of

\[
\begin{aligned}
 &\forall x\ E(x,x),\\
 &\forall x\forall y\ (E(x,y)\to E(y,x)),\\
 &\forall x\forall y\forall z\
       ((E(x,y)\land E(y,z))\to E(x,z)).
\end{aligned}
\tag{3}
\]

Every symbol in these formulas is relational and equality-free.

For each original r-ary predicate `P`, require

\[
 \operatorname{Cong}_P:
 \forall\bar x\forall\bar y\left[
   \bigwedge_{i=1}^r E(x_i,y_i)
       \to(P(\bar x)\leftrightarrow P(\bar y))\right].
 \tag{4}
\]

For a nullary predicate this is the harmless tautology `P iff P`;
it may be omitted. For each n-ary function `f`, require

\[
\begin{aligned}
 \operatorname{Tot}_f:
  &\quad\forall\bar x\ \exists z\ F_f(\bar x,z),\\
 \operatorname{Uniq}_f:
  &\quad\forall\bar x\forall z\forall w\
       ((F_f(\bar x,z)\land F_f(\bar x,w))\to E(z,w)),\\
 \operatorname{Cong}_{F_f}:
  &\quad\forall\bar x\forall\bar y\forall z\forall w\left[
       \left(\bigwedge_{i=1}^n E(x_i,y_i)\land E(z,w)\right)
       \to(F_f(\bar x,z)\leftrightarrow F_f(\bar y,w))\right].
\end{aligned}
\tag{5}
\]

Empty tuples, empty conjunctions, and empty universal prefixes have their
usual meanings. For a constant these are explicitly

\[
 \exists z\ F_c(z),\qquad
 \forall z\forall w\ ((F_c(z)\land F_c(w))\to E(z,w)),\qquad
 \forall z\forall w\ (E(z,w)\to(F_c(z)\leftrightarrow F_c(w))).
 \tag{6}
\]

Define the two finite conjunctions of sentences

\[
\begin{aligned}
 \mathrm{Ax}_L
  &=\mathrm{Eq}(E)\land
       \bigwedge_{P\in S_L}\mathrm{Cong}_P\land
       \bigwedge_{f\in S_L}
         (\mathrm{Tot}_f\land\mathrm{Uniq}_f\land\mathrm{Cong}_{F_f}),\\
 \mathrm{Ax}_R
  &=\mathrm{Eq}(E)\land
       \bigwedge_{P\in S_R}\mathrm{Cong}_P\land
       \bigwedge_{f\in S_R}
         (\mathrm{Tot}_f\land\mathrm{Uniq}_f\land\mathrm{Cong}_{F_f}).
\end{aligned}
\tag{7}
\]

The predicate and function index ranges in (7) use their respective symbol
kinds. Each private symbol contributes axioms only to its own side.
Common-symbol axioms, as well as `Eq(E)`, occur on both sides. In
particular,

\[
 \operatorname{sig}(\mathrm{Ax}_L)\subseteq S_L^r\cup\{E\},
 \qquad
 \operatorname{sig}(\mathrm{Ax}_R)\subseteq S_R^r\cup\{E\}.
 \tag{8}
\]

Fresh bound variables are used throughout, avoiding capture of variables
in the input formulas and translation contexts.

## 4. Terms and formulas

For a term `t` and an output variable `z` fresh for `t`, define an
equality-free relational formula `V_t(z)` by recursion:

\[
\begin{aligned}
 V_x(z)&=E(z,x),\\
 V_{f(t_1,\ldots,t_n)}(z)
   &=\exists z_1\cdots\exists z_n\left[
       \bigwedge_{i=1}^n V_{t_i}(z_i)\land F_f(z_1,\ldots,z_n,z)\right].
\end{aligned}
\tag{9}
\]

All intermediate variables are freshly chosen at every occurrence. In
particular `V_c(z)=F_c(z)` for a constant. Formula (9) uses only `E`, the
graph symbols of the functions in `t`, and its input/output variables.

Translate atoms by

\[
\begin{aligned}
 (P(t_1,\ldots,t_r))^r
  &=\exists z_1\cdots\exists z_r\left[
      \bigwedge_{i=1}^r V_{t_i}(z_i)\land P(z_1,\ldots,z_r)\right],\\
 (t=s)^r
  &=\exists z\exists w\,[V_t(z)\land V_s(w)\land E(z,w)].
\end{aligned}
\tag{10}
\]

A nullary predicate is unchanged. Logical falsehood and truth are
unchanged. The translation commutes with every Boolean connective and
with `forall x` and `exists x`, using fresh intermediate variables to
avoid capture. It is effective and satisfies

\[
 \operatorname{FV}(\varphi^r)=\operatorname{FV}(\varphi),\qquad
 \operatorname{sig}(\varphi^r)\subseteq\operatorname{sig}(\varphi)^r\cup\{E\}.
 \tag{11}
\]

If the original language has no equality atoms, the second line of (10)
is simply unused. Auxiliary `E` is still allowed in this purely
relational translation as an ordinary predicate.

## 5. Quotient model and the complete truth argument

Let `N` be a nonempty relational structure satisfying both sets in (7),
and write its domain as `D`. Define `a ~ b` iff `N |= E(a,b)`.
By (3), this is an equivalence relation. The quotient domain
`D/~` is a nonempty set. Write `p(a)=[a]` for its surjective projection.

Construct a structure `M=N/E` for the original finite signature `S`.
For an original predicate, set

\[
 P^M([a_1],\ldots,[a_r])
      \quad\Longleftrightarrow\quad P^N(a_1,\ldots,a_r).
 \tag{12}
\]

This is independent of representatives by (4); nullary predicates retain
their truth values. Define

\[
 f^M([a_1],\ldots,[a_n])=[b]
       \quad\text{when }F_f^N(a_1,\ldots,a_n,b).
 \tag{13}
\]

Totality supplies an output for every representative tuple. Uniqueness
modulo `E` makes its class unique. Input congruence shows that changing
the representatives does not change that class. This defines a total
function without needing a choice of one output representative globally:
the output class is uniquely characterized. Formula (6) supplies the same
argument for constants. Logical equality in `M` is identity of classes.

For any assignment `s` into `D`, let `bar s = p o s`. The term lemma is

\[
 N,s[z:=a]\models V_t(z)
       \quad\Longleftrightarrow\quad
       [a]=t^M(\bar s).
 \tag{14}
\]

For a variable, (14) is exactly the definition of the quotient. Suppose
it holds for the immediate subterms of `f(t_1,...,t_n)`. Witnesses for
(9) then represent their term values; (13) proves the forward direction.
Conversely choose representatives of those finitely many values. The
induction hypothesis provides the subterm witnesses, and totality
provides an output representative `b`. If `[a]` is the required output
class, then `E(b,a)`. Output congruence in (5), together with reflexivity
on the unchanged inputs, gives `F_f(...,a)`. This proves the reverse
direction. The constant case is the same argument with no subterms.

For every original formula whose symbols are in `S`,

\[
 N,s\models\varphi^r
       \quad\Longleftrightarrow\quad
 M,\bar s\models\varphi.
 \tag{15}
\]

For predicate atoms, combine (10), (14), and representative independence
in (12). For equality atoms, combine (14) with equality of equivalence
classes. Boolean steps follow immediately, including negation: the
translated atom already has an exact truth value independent of the
chosen representatives. For an existential quantifier, project a
relational witness using `p`; conversely lift a quotient witness using
surjectivity. The universal clause follows in the same two directions,
or from existential quantification and negation. This completes the
structural induction, with no change to the free-variable assignment.

## 6. The asymmetric implication and vocabulary control

The correct implication to interpolate is

\[
 \models (\mathrm{Ax}_L\land A^r)
              \to(\mathrm{Ax}_R\to B^r).
 \tag{16}
\]

Indeed, a countermodel and assignment would satisfy both axiom sets,
`A^r`, and `not B^r`. Formula (15) would give a quotient countermodel to
(1). This establishes (16) over all equality-free relational structures;
the axioms are formulas within the implication, not a restriction on the
class to which the relational interpolation theorem is applied.

Apply equality-free relational Craig to

\[
 L=\mathrm{Ax}_L\land A^r,
 \qquad R=\mathrm{Ax}_R\to B^r.
\]

It supplies `J` with `models L -> J` and `models J -> R`. By (8) and
(11), every predicate of `J` belongs to

\[
 \{E\}\ \cup\
 \{P:P\text{ is an original predicate common to }A,B\}\ \cup\
 \{F_f:f\text{ is an original function or constant common to }A,B\}.
 \tag{17}
\]

Its free variables belong to `FV(A) intersect FV(B)` because the axiom
sets are sentences. The relational theorem may omit some of the permitted
symbols; no equality of vocabulary sets is needed.

Placing both axiom sets in the antecedent would spoil this argument:
right-private symbols would then also occur on the left and would become
eligible interpolant vocabulary. The asymmetric placement in (16) is
therefore essential to this particular reduction.

## 7. Canonical expansion and translating the interpolant back

For any original structure `M`, let `M^#` have the same domain and
original predicate interpretations, with

\[
 E^{M^\#}(a,b)\Longleftrightarrow a=b,\qquad
 F_f^{M^\#}(\bar a,b)\Longleftrightarrow f^M(\bar a)=b.
 \tag{18}
\]

This canonical expansion satisfies every relevant axiom in (3)-(6),
including the constant axioms. Directly by the term/formula induction,

\[
 M,s\models\varphi\quad\Longleftrightarrow\quad
 M^\#,s\models\varphi^r.
 \tag{19}
\]

The relational interpolant has only variables as terms. Define its
back-translation by

\[
\begin{aligned}
 (E(x,y))^\flat&=(x=y),\\
 (F_f(x_1,\ldots,x_n,z))^\flat&=(f(x_1,\ldots,x_n)=z),\\
 (F_c(z))^\flat&=(c=z),\\
 (P(\bar x))^\flat&=P(\bar x),
\end{aligned}
\tag{20}
\]

and commute with all logical constructors. No binders are added, so free
variables are unchanged. By structural induction using (18),

\[
 M,s\models J^\flat\quad\Longleftrightarrow\quad M^\#,s\models J.
 \tag{21}
\]

Take `C=J^flat`. If `M,s |= A`, then its canonical expansion satisfies
`Ax_L and A^r`, hence `J`, hence `C` by (21). If `M,s |= C`, then the
canonical expansion satisfies `J` and automatically satisfies `Ax_R`;
the second interpolation implication therefore yields `B^r`, hence `B`
by (19). This proves both implications in (2).

By (17), the only original nonlogical symbols introduced by (20) are
common functions and constants. The other translated symbol is logical
equality. This proves the full symbol restriction. Equations (11), the
relational free-variable condition, and (20) prove the free-variable
restriction. For sentences, `C` is a sentence. Empty common nonlogical
vocabulary presents no problem: equality and logical constants remain
permitted, and an interpolant may simply be falsehood or truth.

## 8. Open formulas if only sentence Craig is available

The previous sections already handle open formulas when relational Craig
has the free-variable clause of the live Maehara theorem. Here is the
alternative route using only its sentence version.

Let `bar x` list `FV(A) \ FV(B)`, let `bar y` list
`FV(B) \ FV(A)`, and let `bar z` list their intersection. Rename bound
variables to avoid all capture and put

\[
 A_0(\bar z)=\exists\bar x\ A,\qquad
 B_0(\bar z)=\forall\bar y\ B.
 \tag{22}
\]

Then `models A_0 -> B_0`. Fix a structure and values for the common
variables. A witness for `A_0` gives values for the left-private variables.
For any choice of right-private values, combine the assignments and use
(1). Since `B` has no free left-private variables, this proves `B_0`.
Conversely, `A` implies `A_0` and `B_0` implies `B`, so (22) is also an
equivalent validity problem. The existential/universal directions in (22)
must not be exchanged.

Replace each common variable `z_i` by a fresh constant `c_i`. The resulting
sentences `A_*` and `B_*` satisfy `models A_* -> B_*`, because all possible
interpretations of the fresh constants are included. Apply the sentence
construction in Sections 2-7. Its interpolant contains only common original
symbols and some of these fresh constants. Rename its bound variables away
from `bar z`, then replace each `c_i` by `z_i`. Interpreting `c_i` as the
assigned value of `z_i` proves the resulting formula lies between `A_0`
and `B_0`, hence between `A` and `B`. Its free variables are a subset of
the common variables, as required.

One can instead replace all free variables in `A,B` directly by distinct
fresh constants. Constants representing private variables then occur on
only one side, so sentence Craig excludes them automatically. Replacing
the remaining shared constants back by variables gives the same conclusion.
Neither construction assumes that different constants have different values.

## 9. Equality-free input formulas and the stronger equality-free-output question

If `A,B` do not contain equality, the full construction remains valid:
omit the equality-atom clause in (10). Auxiliary `E` is still an ordinary
binary predicate in the relational problem, and the final interpolant may
contain logical equality. This proves exactly the general Craig statement
in Section 1, including its equality-free input cases.

If equality-free output is additionally required, two cases must be
distinguished. For purely relational equality-free inputs, apply the
original relational theorem directly without `E`; its output is
equality-free. If the inputs also contain constants but no positive-arity
functions, replace those constants by distinct fresh variables, apply the
relational theorem with its free-variable condition, and replace the
surviving common parameters back by constants. Assignments may give the
fresh variables identical values, just as different original constants
may coincide. This yields equality-free output in that case too.

For positive-arity functions, the reduction above does not itself prove
equality-free output. Formula (20) uses actual equalities for graph atoms,
and `E` is eligible common vocabulary even when equality was absent from
the inputs. A separate equality-elimination or direct function-symbol
interpolation argument would be needed for that stronger syntactic claim.
It is not required by the existing general theorem, which expressly permits
logical equality regardless of its occurrence in the inputs.

## 10. Failure modes and completion boundary

The graph axioms cannot be weakened to totality alone. For example, the
equality-free formula

\[
 \forall z\neg(P(z)\land Q(z))
      \to\neg(P(f(x))\land Q(f(x)))
 \tag{23}
\]

is valid for an actual function. In a two-element relational structure,
interpret `E` as identity, let `P={a}`, `Q={b}`, and allow both outputs
`a,b` in `F_f(v,-)` for every
input `v`. The existential term translations make both `P(f(x))^r` and
`Q(f(x))^r` true while the antecedent remains true. Thus omitting uniqueness
can invalidate the required relational implication. Uniqueness in (5)
must be modulo `E`; writing logical equality there would leave the
equality-free relational language.

Predicate congruence makes quotient predicates well defined; input
congruence makes quotient functions independent of representatives; output
congruence supplies every equivalent output representative needed for the
reverse direction of (14). Constants need totality and uniqueness just
as other functions do. Private axioms must remain on their respective
sides of (16), and all fresh relation names must avoid original predicates.

Subject to equality-free relational Craig, the route is complete for
classical first-order logic with total finite-arity functions, constants,
standard equality, and nonempty domains. Empty-domain conventions,
partial functions, many-sorted empty sorts, and equality-free output with
positive-arity functions are not silently included. The independent
proof-status dependency is still the semantic-validity-to-cut-free-proof
bridge identified in Section 1.

Only this proof note was created. No handbook edits, software tests,
builds, renders, or additional agents were used.
