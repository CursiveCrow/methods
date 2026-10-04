# Walukiewicz completeness: source theorem and calculus alignment

Date: 2026-09-06.

## Source and exact locators

Igor Walukiewicz, *Completeness of Kozen's Axiomatisation of the
Propositional mu-Calculus*, is registered as `Walukiewicz2000`,
*Information and Computation* 157(1-2), 142-182, DOI
`10.1006/inco.1999.2836`.

The inspected body is the author's [complete 40-page PDF](https://www.labri.fr/perso/igw/Papers/igw-kozen-compl.pdf).
The locators below use its printed page numbers, which also equal its
one-based PDF page numbers. They are not asserted to be the journal's
page numbers or to establish byte-for-byte identity with the journal file.

| Author-version location | Relevant content |
| --- | --- |
| Introduction, pp. 1-2 | Original Kozen system; explicit weak-completeness meaning and noncompactness boundary |
| Section 2, pp. 5-7 | Grammar, arbitrary Kripke structures, environments, fixed-point semantics |
| Section 2, pp. 7-9 | Well-named formulas, capture-avoiding substitution, defined cover notation and standing proviso |
| Section 4, p. 14 | Equational judgments and K1-K6 |
| Section 4, p. 15, Fact 17 | Provable normalization to the standing presentation |
| Section 4, p. 15, Theorem 18 | Refutability of unsatisfiable disjunctive formulas |
| Section 6, p. 23, Theorems 25-26 | Full completeness and the provable implication to a semantically equivalent disjunctive formula |

The exact main statement is Theorem 25:

> For every unsatisfiable formula ϕ formula ¬ϕ is provable.

In the paper, provability of a formula means derivability of its equality
to top in the equational system. Thus the theorem yields validity
completeness for arbitrary finitary formulas. Soundness supplies the
reverse implication.

## 1. Actual handbook destinations

The live N18 file is
`handbook/parts/p09/presentations/n-c-018.tex`.

- Its opening grammar is the finitary `L_mu` grammar with variables,
  proposition constants, Boolean negation/disjunction, diamonds, and positive
  least fixed points. The separate ordinal-stage language `L_mu+` is
  explicitly auxiliary.
- `The source calculus`, label `sec:p09-kozen-calculus`, displays the
  Boolean equational base, modal join, mixed modal inequality, modal zero,
  prefixpoint axiom, and the fresh-variable Park rule.
- `Derived fixed-point laws` explicitly
  uses the formula-candidate Park rule with a derivable premise and the
  condition `X notin FV(b)`.
- The end of the aconjunctive development establishes its restricted
  consistency/model equivalence. The newly incorporated paragraph
  `sec:p09-kozen-full-completeness` now supplies the cited full theorem,
  the system alignment, and its consequences.

The actual rule sheet is `handbook/registry/calculi/hilbert-mu.tex`, label
`sheet:hilbert-mu`. It defines theoremhood as `A = top`, inequality as
`A or B = B`, and includes capture-avoiding uniform substitution when
formation conditions are preserved.

The p08 entry `entry:p08-modal-mu`, in
`handbook/parts/p08/temporal-epistemic-supplement.tex` (also retained in
`temporal-dynamic-epistemic.tex`), points to that sheet. The active supplement
now states weak validity completeness with `cited=Walukiewicz2000` and links
to the new N18 paragraph. Its semantics explicitly use nonempty state sets
and arbitrary binary action relations. That cited standing is appropriate.

## 2. Language and model scope

The source grammar has propositional letters `Prop`, fixed-point variables
`Var`, and action names `Act`, with top, bottom, unrestricted Boolean
negation, conjunction and disjunction, both modalities, and both fixed-point
binders. The formation condition is positivity of the variable bound by
each fixed-point binder. It does not restrict conjunction to the
aconjunctive fragment or impose a bound on alternation depth.

A source model is `(S,R,rho)` with nonempty `S`, arbitrary relations
`R(a) subset S x S`, and arbitrary proposition valuations `rho(p) subset S`.
An environment `V:Var -> P(S)` independently interprets free fixed-point
variables. Diamonds use existential successors, boxes universal successors,
and least and greatest fixed points are computed in `P(S)`. Empty successor
sets are allowed. There is no seriality, finiteness, finite-branching,
image-finiteness, binary-tree, or one-hot-label hypothesis.

Consequently, a formula is valid when it is true at every state of every
such structure under every environment. Unsatisfiability means that no
structure, state, and environment makes it true. This includes open formulas
and arbitrary occurrences of their free variables. The only positivity
requirement imposed on the full language concerns bound occurrences.

The theorem concerns finitary `L_mu`. It does not assert completeness of
the ordinal-stage syntax `L_mu+`.

## 3. Explicit presentation map

Identify the source's proposition, variable, and action sets with the
corresponding handbook sets, up to injective renaming. Send source top and
bottom to handbook `1` and `0`; retain variables, proposition letters,
negation, disjunction, diamonds, and least binders. Eliminate the extra
source constructors by the handbook's existing definitions:

\[
\begin{aligned}
 T(\alpha\land\beta)
   &=\neg(\neg T\alpha\lor\neg T\beta),\\
 T([a]\alpha)&=\neg\langle a\rangle\neg T\alpha,\\
 T(\nu X.\alpha)&=
   \neg\mu X.\neg\bigl((T\alpha)[\neg X/X]\bigr),\\
 T(\alpha\Rightarrow\beta)&=\neg T\alpha\lor T\beta.
\end{aligned}
\tag{1}
\]

Binders are renamed before substitution to prevent capture. The source's
cover construct is also just an abbreviation:

\[
 T(a\to\Psi)=
  \left(\bigwedge_{\psi\in\Psi}\langle a\rangle T\psi\right)
      \land[a]\left(\bigvee_{\psi\in\Psi}T\psi\right).
 \tag{2}
\]

Empty conjunction/disjunction mean top/bottom. Formula (2) introduces no
new proof rule and no extra model condition.

For models, put `I(a)=R(a)`, `I(P)=rho(P)`, and `eta=V`. Structural
induction, with the fixed-point complement identity for the greatest
binder, proves

\[
 \llbracket T\alpha\rrbracket_{M,\eta}
       =\llbracket\alpha\rrbracket_{(S,R,\rho),V}.
 \tag{3}
\]

Conversely, every finitary handbook formula is already a formula in the
source's expanded grammar. No translation through automata or ANF is
needed to align the languages.

The source writes `alpha <= beta` for `alpha and beta = alpha`; the
handbook writes it for `alpha or beta = beta`. These are provably
equivalent using Boolean absorption. For example, from
`alpha or beta = beta`,
`alpha and beta = alpha and (alpha or beta) = alpha`; the reverse uses
`(alpha and beta) or beta = beta`.

## 4. Every source axiom and rule maps to the displayed calculus

After (1)-(2) and the Boolean order conversion, the source's Section 4
system maps as follows:

| Source principle | Handbook principle |
| --- | --- |
| K1, Boolean algebra and equational reasoning | The declared Boolean equational base, including replacement |
| K2, diamond preserves binary joins | Modal join axiom |
| K3, diamond alpha and box beta below diamond(alpha and beta) | The same mixed modal inequality |
| K4, diamond bottom equals bottom | Modal zero axiom |
| K5, body evaluated at its least fixed point lies below it | The displayed prefixpoint axiom |
| K6, a derivable prefixed-point inequality yields the least-fixed-point bound | The displayed formula-instance Park rule |

The definitional box and greatest-fixed-point equations printed after
K6 are exactly those in (1), so their elimination is compatible with
equational replacement. Source substitution is capture avoiding and
respects binder positivity, matching the sheet's formation conditions.

For K6, let the positive body be `p(X)` and the candidate formula be `b`.
Rename the bound variable so that `X notin FV(b)`. Choose a variable `Y`
fresh for `p` and `b`. The whole fresh-variable Park schema

\[
 \frac{\vdash p[Y/X]\leq Y}{\vdash\mu X.p\leq Y}
 \tag{4}
\]

has the capture-avoiding uniform instance `Y := b`, namely

\[
 \frac{\vdash p[b/X]\leq b}{\vdash\mu X.p\leq b}.
 \tag{5}
\]

Freshness ensures that this substitution changes neither the body nor its
bound variable in the conclusion; the candidate replaces precisely the
designated occurrences in the premise. All binders in the substituted body
are renamed away from the free variables of `b`. Apply (5) to the given
derivation of its premise.

This is substitution into a **rule schema**, not an attempted inference
from `p(b) <= b` back to a theorem `p(Y) <= Y`. The N18 passage already
states and uses (5) explicitly. To make the registry sheet's reading equally
explicit, it can state that the displayed Park rule includes its admissible
formula-substitution instances, or display (5) directly. Merely having a
theorem-level substitution rule, while forbidding instances of inference
schemas, would not justify that backwards step and is not the reading used
in N18.

Thus a finite source proof can be translated line by line into the actual
N18 calculus. The cited completeness theorem applies to that calculus;
one does not merely know that the two systems happen to be sound for the
same structures.

## 5. Theorem 26: exact direction and hypotheses

Theorem 26, in the supplied author version at p. 23, starts with a positive,
guarded formula `phi` and supplies a disjunctive formula `phi_hat` such that

\[
 \phi\equiv_{\mathrm{sem}}\widehat\phi,
 \qquad
 \vdash_K\phi\leq\widehat\phi.
 \tag{6}
\]

The provable implication is from the original formula **to** the
disjunctive formula. The theorem does not state the reverse derivability
as its hypothesis or output. It additionally preserves a variable's
positive-only occurrence property whenever that property holds in the
input. It does not require all free variables to occur only positively.

The surrounding standing proviso also uses well-named formulas and the
cover notation: bound variables are distinct, free variables are distinct
from bound ones, negations in positive form apply only to proposition
letters or free variables, and bound-variable occurrences are guarded by
modalities. Fact 17, p. 15, provides **provable equivalence** from any
formula to this presentation. Thus these restrictions organize the proof;
Theorem 25 is not restricted to inputs already in that form.

The proof-bearing chain for an unsatisfiable formula is:

1. Fact 17 replaces it by a provably equivalent formula satisfying the
   proviso.
2. Theorem 26 supplies (6), whose semantic equivalence makes the
   disjunctive output unsatisfiable.
3. Theorem 18 derives the negation of that disjunctive output, equivalently
   its equality to bottom.
4. The derivable inequality in (6) and Boolean reasoning derive the
   original formula's equality to bottom, hence its negation as a theorem.

This explains the full completeness result without reproducing the
research paper's tableau-consequence construction. In particular, the
handbook's separately established **semantic** equivalence to ANF does
not supply the provable implication in (6). That implication is an
essential conclusion of Walukiewicz's proof, not a consequence inferred
from semantic equivalence before completeness has been established.

## 6. Exact theorem suitable for the handbook

For every well-formed formula `p` of finitary `L_mu`, including open
formulas interpreted under all environments,

\[
 \bigl(\forall M\ \forall\eta\quad
       \llbracket p\rrbracket_{M,\eta}=S_M\bigr)
       \quad\Longleftrightarrow\quad
       \vdash_K p=1.
 \tag{7}
\]

The left-to-right implication is Walukiewicz's **cited weak completeness**
theorem, mapped through Sections 3-4. Apply Theorem 25 to `not p` and use
Boolean double negation. The other direction is the soundness already
proved in N18. Equivalently, for any `p,q`,

\[
 \forall M,\eta\quad
    \llbracket p\rrbracket_{M,\eta}\subseteq
    \llbracket q\rrbracket_{M,\eta}
       \quad\Longleftrightarrow\quad\vdash_K p\leq q.
 \tag{8}
\]

For the semantic-to-derivable direction in (8), apply (7) to `not p or q` and use
Boolean algebra. Equality completeness follows by taking both
inequalities. These are statements about theoremhood of equations or
inequalities, not about an unspecified premise calculus.

## 7. Finite premises and noncompactness

For a finite set `Gamma` of formulas, define local consequence at a
point using one common environment. Then

\[
 \Gamma\models_{\mathrm{loc}}q
  \quad\Longleftrightarrow\quad
  \models\left(\bigwedge\Gamma\right)\to q
  \quad\Longleftrightarrow\quad
  \vdash_K\bigwedge\Gamma\leq q.
 \tag{9}
\]

The empty conjunction is top. Formula (9) is the precise finite-premise
corollary obtained by internalizing the premises into one formula. It does
not authorize Park induction or arbitrary equational replacement on a
formula merely assumed true at the current state. The Park premise is a
derived predicate inclusion, as the N18 soundness proof explicitly says.
Nor does (9) identify local consequence with a different notion of
global equational consequence from equations assumed throughout a model.

For a concrete noncompact set, fix one proposition `p` and action `a`,
put

\[
 R=\mu X.(p\lor\langle a\rangle X),\qquad
 \Gamma=\{R\}\cup\{[a]^n\neg p:n\in\mathbb N\},
 \tag{10}
\]

where `[a]^0 not p` means `not p`. The least fixed point `R` holds
exactly at states having a finite a-path to a p-state. Every finite subset
of (10) is satisfiable: choose `N` at least every exponent it mentions,
take a finite chain of length `N+1`, and put `p` only at its last state.
The root satisfies reachability and all the indicated boxes. But the
whole set has no pointed model: any finite witnessing path to `p` has
some length `n`, contradicting `[a]^n not p`.

Any finite derivation from premises uses only finitely many of them.
Consequently no sound finitary premise calculus can derive every local
semantic consequence of arbitrary sets such as (10). This is the
strong-completeness boundary stated in the source's introduction, with
the counterexample supplied explicitly here. It leaves (7)-(9) intact.

## 8. Actual incorporation and bounded review

The actual insertion at `sec:p09-kozen-full-completeness` was read in full
through the following Emerson-Jutla heading after this note was drafted.
Its theorem retains `cited=Walukiewicz2000` and correctly states weak
completeness for every finitary formula, every model, and every environment,
with unrestricted conjunction and initially unguarded formulas included.
The nonempty models, arbitrary action relations, and powerset semantics
match the source.

The K1-K6 identification, Boolean order-convention conversion, and whole-rule
Park substitution have the intended sound direction. Fact 17 and Theorem 26
are used to provide a deductive normalization step; the displayed inequality
is `phi <= phi_hat`. The additional positive-only-variable preservation
conclusion of Theorem 26 is not needed for the weaker proof outline stated
in the insertion. The text does not infer that inequality merely from its
separate semantic ANF theorem.

The inequality/equality consequences, consistency-to-satisfiability result,
finite-premise local consequence statement, and noncompactness example all
check out. In the actual example, the chain ends at an `N` strictly greater
than the exponents present in the chosen finite subset, which is equivalent
to the indexing used in Section 7 of this note. The active p08 card now
uses weak completeness and links to the insertion.

No mathematical repair was identified in that bounded review. The verified
numbering of Theorem 25, Fact 17, and Theorem 26 is that of the supplied
author version. The source locator should say so unless the corresponding
journal numbering has separately been checked.

The insertion fulfills the promise of full-calculus treatment through an
accurately stated cited theorem and its explained calculus mapping. It does
not claim a local reconstruction of the full research proof. N18's local
soundness and aconjunctive completeness remain their own established results.

Only this source note was created. No manuscript files, software tests,
builds, renders, or additional agents were used. The exact theorem and
system clauses were read from the supplied primary PDF; the whole
40-page research proof was not independently reconstructed or audited.
