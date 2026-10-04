# Beth explicit definability from full Craig interpolation

Date: 2026-09-06.

This note supplies a complete proof from full first-order Craig
interpolation, compactness, and ordinary first-order completeness.
It covers arbitrary sets of sentences, arbitrary set-sized signatures
with functions and constants, equality, and a distinguished relation
of any finite arity, including zero.

## Active manuscript destination

The active theorem is the result with label thm:beth in
handbook/restoration/inherited-11914-11960.tex. The Part VII driver
inputs its restoration scope and then
handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex.
The latter's paragraph beginning “Route from the cited Craig theorem
to the cited Beth theorem” currently gives the short route at lines
181–193 when read.

The active full Craig theorem is thm:craig-interpolation in the same
restoration file. Its statement is for first-order sentences, permits
all shared nonlogical symbols, and expressly allows equality and
logical falsity independently of the shared signature. The proof
below uses that full theorem, not a restricted relational partition
lemma. The similarly named theorem in
handbook/parts/p07/cut-elimination-and-interpolation.tex is not the
active theorem reached by the inspected driver.

Only this note was written. No handbook changes, tests, builds, or
renders were performed.

## Live supporting labels and their stated strength

The active Part II driver reaches the following results through its
restoration scopes. These are the unprefixed labels, not similarly
named inactive replacement-file labels.

- thm:fol-compactness, in
  handbook/restoration/inherited-04921-04967.tex, beginning at line 5:
  both the model form and finite-consequence form of first-order
  compactness. The statement explicitly assumes ambient Axiom of
  Choice and is followed by a full local proof.
- thm:fol-completeness, in
  handbook/restoration/inherited-04713-04920.tex, beginning at line 5:
  strong completeness for \(\ND_{\FOL}\), arbitrary signatures and
  arbitrary sets of formulas. It explicitly assumes ambient Axiom of
  Choice and is followed by a full local proof.
- cor:fol-completeness-countable, in that same file at line 49:
  completeness for countable signatures without Choice, explicitly
  marked complete proof. The final finite-premise implication in the
  Beth argument lies in a finite signature, so this result also
  suffices for that final syntactic step.
- lem:fresh-constant, in
  handbook/restoration/inherited-04306-04575.tex at line 67:
  from \(\Gamma\vdash\chi[c/x]\), with \(c\) absent from \(\Gamma\)
  and \(\chi\), infer \(\Gamma\vdash\forall x\,\chi\). A full proof
  replaces the constant throughout the finite derivation and checks
  the eigenvariable conditions.
- lem:new-constant-elimination, in that same file at line 127:
  an expanded-language derivation of an old-language conclusion from
  old-language assumptions can be replaced by an old-language
  derivation. Its full proof covers replacement inside function terms,
  equality instances, and eigenvariable conditions.
- thm:fol-substitution, in
  handbook/restoration/inherited-03519-03680.tex at line 61:
  the full semantic substitution lemma, with a local proof.
  Repeated application justifies the parameter-to-variable semantic
  substitution in the proof below.
- lem:reduct-invariance, in
  handbook/restoration/inherited-03927-04061.tex at line 70:
  satisfaction of old-language formulas is unchanged by expansion
  and reduct; this supports the fresh-parameter expansions.

The driver paths were checked in handbook/parts/p02.tex. In particular,
the arbitrary-signature proof below inherits the stated ambient
Choice assumption of the active compactness theorem. No appeal to
the merely sketched inherited LK completeness theorem is necessary.

## Exact desired statement

Work in classical first-order logic with nonempty domains and equality
interpreted as identity. Assume the Axiom of Choice in the ambient set
theory, as in the active arbitrary-signature compactness theorem.
The argument may instead take compactness itself as an explicit
premise; no equivalence between compactness and Choice is asserted.
Let \(L\) be any set-sized signature, whose
relation and function symbols have finite arities and which may contain
constants. Let \(n\geq0\), let \(P\notin L\) be a new \(n\)-ary relation
symbol, and let \(T\) be any set of \(L\cup\{P\}\)-sentences.

Say that \(T\) implicitly defines \(P\) over \(L\) when
\[
 \forall\mathcal M\ \forall U,V\subseteq M^n:
 \quad
  (\mathcal M,U)\models T\ \land\ (\mathcal M,V)\models T
       \quad\Longrightarrow\quad U=V,
\]
where \(\mathcal M\) ranges over \(L\)-structures with domain \(M\).
Both expansions have literally the same domain and the same
interpretations of every symbol in \(L\), including all functions and
constants. There is no requirement that every \(L\)-structure have a
\(T\)-expansion.

Then there exist a finite subset \(T_0\subseteq T\), a finite
subsignature \(L_0\subseteq L\), and an \(L_0\)-formula
\(\varphi(x_1,\ldots,x_n)\), with no other free variables, such that
\[
 T_0\models
 \forall x_1\cdots\forall x_n
       \bigl(P(x_1,\ldots,x_n)
                  \leftrightarrow\varphi(x_1,\ldots,x_n)\bigr).
 \tag{Beth}
\]
Consequently the same consequence holds from \(T\). In any sound and
complete ordinary first-order proof calculus, one also has
\[
 T_0\vdash
 \forall x_1\cdots\forall x_n
       \bigl(P(x_1,\ldots,x_n)
                  \leftrightarrow\varphi(x_1,\ldots,x_n)\bigr),
\]
and therefore the corresponding derivation from \(T\).

When \(n=0\), \(M^0=\{()\}\), so a nullary relation has either truth value.
The tuple of variables and universal prefix are empty; the conclusion
is \(T_0\models P\leftrightarrow\varphi\), with \(\varphi\) an
\(L_0\)-sentence.

Conversely, any explicit definition of this form implies the stated
implicit definition condition: the \(L\)-reduct alone determines the
truth of \(\varphi\) at every tuple, hence the interpretation of \(P\).
The finite-support conclusion is thus stronger than the usual
existence-only formulation of Beth's theorem.

## 1. Doubling the distinguished relation

Choose another \(n\)-ary relation symbol \(P'\), fresh for
\(L\cup\{P\}\). For an \(L\cup\{P\}\)-sentence \(\sigma\), let
\(\sigma'\) be obtained by replacing every occurrence of \(P\) with
\(P'\), leaving all \(L\)-symbols unchanged. Put
\[
 T'=\{\sigma':\sigma\in T\}.
\]

Implicit definability is equivalent to
\[
 T\cup T'\models
 \forall\bar x\bigl(P(\bar x)\leftrightarrow P'(\bar x)\bigr).
 \tag{1}
\]
Indeed, a structure for \(L\cup\{P,P'\}\) satisfying both theories
contains two \(T\)-expansions of the same \(L\)-reduct. Implicit
definability makes the two interpretations equal, yielding (1).
Conversely, any two expansions of one \(L\)-structure can be combined
into such a doubled structure; (1) then makes their distinguished
relations equal. This reasoning is unchanged for nullary relations.

No other nonlogical symbol is renamed. Renaming the entire language
would discard precisely the common-reduct requirement needed by the
hypothesis.

## 2. Inconsistent theories

If \(T\) has no model, compactness gives a finite inconsistent
\(T_0\subseteq T\). Take \(\varphi(\bar x)=\bot\), which has no free
variables and no nonlogical symbols. The semantic conclusion (Beth)
then follows vacuously. Ordinary completeness gives a derivation of
falsity from \(T_0\), and explosion gives the displayed explicit
definition in the proof calculus.

Thus inconsistency satisfies implicit definability and causes no
exception to the theorem. The remaining argument can be presented for
consistent \(T\), although it also works without this case distinction.

## 3. Compactness produces two fixed finite supports

For \(n>0\), introduce pairwise distinct new constant symbols
\(\bar c=(c_1,\ldots,c_n)\), none occurring in \(L\cup\{P,P'\}\).
Their interpretations are arbitrary and are not required to be
distinct elements. This permits all tuples, including tuples with
repeated coordinates. For \(n=0\), use the empty tuple of constants
and read \(P(\bar c)\) as the nullary sentence \(P\).

By (1), the following set of sentences is inconsistent:
\[
 T\cup T'\cup\{P(\bar c),\neg P'(\bar c)\}.
 \tag{2}
\]
Compactness gives finite subsets \(\Delta,\Gamma\subseteq T\) such that
\[
 \Delta\cup\Gamma'\cup
           \{P(\bar c),\neg P'(\bar c)\}
 \quad\text{is inconsistent}.
 \tag{3}
\]
Here \(\Gamma'=\{\gamma':\gamma\in\Gamma\}\). If the finite inconsistent
subset first supplied by compactness omits one of the last two
sentences, add it; the enlarged finite subset remains inconsistent.
This justifies exactly the displayed form of (3).

Let
\[
 D=\bigwedge\Delta,\qquad G=\bigwedge\Gamma,
\]
with an empty conjunction defined to be \(\top\). Then (3) is exactly
the validity
\[
 \models
   \bigl(D\land P(\bar c)\bigr)
       \longrightarrow
   \bigl(G'\longrightarrow P'(\bar c)\bigr).
 \tag{4}
\]
It is important that the right-hand sentence is the implication
\(G'\to P'(\bar c)\). This puts the renamed copy's finite assumptions
on the right side of the interpolation problem.

The finite sets \(\Delta,\Gamma\) are chosen once. They do not depend
on a model, a tuple in a model, or a subsequently chosen interpretation
of the constants.

## 4. Apply full Craig interpolation

Set
\[
 \alpha=D\land P(\bar c),\qquad
 \beta=G'\to P'(\bar c).
\]
Both are sentences in the expanded signature. By full Craig
interpolation applied to (4), there is a sentence \(\theta\) such that
\[
 \models\alpha\to\theta,\qquad
 \models\theta\to\beta,
 \tag{5}
\]
and every nonlogical symbol occurring in \(\theta\) occurs in both
\(\alpha\) and \(\beta\).

The left sentence contains no \(P'\), and the right sentence contains
no \(P\). Consequently \(\theta\) contains neither distinguished
relation. Its only possible nonlogical symbols are the fresh constants
\(\bar c\) and symbols in
\[
 L_0=
   \operatorname{sig}_L(D)\cap\operatorname{sig}_L(G).
 \tag{6}
\]
This is a finite subsignature of \(L\), because \(D\) and \(G\) are
finite sentences. Equality and logical constants remain available.
The conclusion covers function and constant symbols of any permitted
finite arity: shared ones may occur in \(\theta\); symbols present
on only one side cannot.

Writing \(\theta(\bar c)\) merely to display its possible fresh
constant parameters, (5) yields
\[
 \Delta\models P(\bar c)\to\theta(\bar c),
 \tag{7}
\]
and
\[
 \Gamma'\models\theta(\bar c)\to P'(\bar c).
 \tag{8}
\]
For example, (8) follows because
\(\models\theta\to(G'\to P'(\bar c))\); equivalently,
\(\models G'\to(\theta\to P'(\bar c))\).

## 5. Rename back and remove the parameters

Rename \(P'\) to \(P\) in (8), fixing \(L\) and the constants
\(\bar c\). This is a uniform change of the relation symbol in that
formula and theory. It leaves \(\theta\) unchanged, since \(\theta\)
contains neither \(P\) nor \(P'\), and gives
\[
 \Gamma\models\theta(\bar c)\to P(\bar c).
 \tag{9}
\]
Together, (7) and (9) give, for the fixed finite set
\[
 T_0=\Delta\cup\Gamma\subseteq T,
\]
the consequence
\[
 T_0\models P(\bar c)\leftrightarrow\theta(\bar c).
 \tag{10}
\]

Choose pairwise distinct variables \(x_1,\ldots,x_n\), and first rename
the bound variables of \(\theta\) so that none is one of these
variables. Replace each occurrence of each fresh constant \(c_i\)
by \(x_i\), simultaneously, including occurrences inside compound
terms. Call the resulting formula \(\varphi(\bar x)\). It is an
\(L_0\)-formula with
\(\operatorname{FV}(\varphi)\subseteq\{x_1,\ldots,x_n\}\).
The renaming prevents variable capture.

To justify universal generalization semantically, take any
\(\mathcal A\models T_0\) and any tuple \(\bar a\in A^n\).
Interpret the fresh constants by \(\bar c^{\mathcal A}=\bar a\).
Because those constants do not occur in \(T_0\), this expansion
still satisfies \(T_0\). By (10) and the substitution lemma,
\[
 \bar a\in P^{\mathcal A}
 \quad\Longleftrightarrow\quad
 \mathcal A,\bar x\mapsto\bar a\models\varphi(\bar x).
 \tag{11}
\]
The tuple was arbitrary, so (11) proves (Beth).

For \(n=0\), there are no parameters to eliminate or variables to
generalize. The interpolant \(\theta\) is already an \(L_0\)-sentence,
and (10) is exactly the required nullary explicit definition.

Finally, the finite-premise implication
\[
 \models\left(\bigwedge T_0\right)\to
  \forall\bar x\bigl(P(\bar x)\leftrightarrow\varphi(\bar x)\bigr)
\]
is valid. Ordinary first-order completeness proves this sentence.
Using the finitely many assumptions in \(T_0\) gives the announced
derivation from \(T_0\), and hence from \(T\). No separate use of
strong completeness for an infinite premise set is necessary here.

## Parameter elimination: exact side conditions and an open-formula variant

The parameter constants are syntactically distinct new symbols, but
their values may coincide. Do not add inequalities between them:
the definition must cover repeated-coordinate tuples. An interpolant
may omit some parameters, so the free-variable conclusion is inclusion
in \(\{\bar x\}\), not equality with that set.

Only these new parameter constants are replaced. Constants already
belonging to \(L_0\) remain genuine symbols of the defining formula.
Replacement includes all occurrences inside arbitrary compound terms.
Renaming the finitely many bound variables of the interpolant away
from \(\bar x\) before replacement is enough to prevent capture.
There is no need to find a variable absent from every formula of an
infinite \(T\).

If a syntactic parameter-removal proof is preferred, first derive
(10) in the constant-expanded language using completeness. Apply
lem:fresh-constant successively to \(c_n,\ldots,c_1\), obtaining the
universal closure in the desired variable order. Each new variable
can be chosen fresh for the finite derivation and its finite used
assumptions. After generalization, the conclusion and the assumptions
contain none of the added constants. Apply
lem:new-constant-elimination to remove any such constants remaining
inside the proof. That last lemma cannot be applied directly while
the conclusion still contains \(\bar c\).

If full Craig is supplied for open formulas with
\[
 \operatorname{FV}(\theta)\subseteq
   \operatorname{FV}(\alpha)\cap\operatorname{FV}(\beta),
\]
the fresh constants can be avoided entirely. Apply the consequence
form of thm:fol-compactness to
\[
 T\cup T'\models
       \forall\bar x\bigl(P(\bar x)\to P'(\bar x)\bigr).
\]
It supplies fixed finite \(\Delta,\Gamma\subseteq T\) witnessing
that consequence. Form the open formulas
\[
 \alpha(\bar x)=D\land P(\bar x),\qquad
 \beta(\bar x)=G'\to P'(\bar x).
\]
Their implication is valid under every assignment. Open-formula
Craig gives an interpolant containing neither \(P\) nor \(P'\),
with free variables among \(\bar x\) and nonlogical vocabulary in
the finite intersection (6). Renaming \(P'\) back gives the two
implications under \(T_0\). Since every sentence of \(T_0\) is
closed, universal generalization over \(\bar x\) immediately gives
(Beth). For \(n=0\) all formulas in this variant are sentences.
This alternative has the same uniform finite support.

## Uniform finite support

The proof establishes more than pointwise definability:

- A single finite set \(T_0\subseteq T\) suffices for all models and
  all tuples.
- A single finite-signature formula \(\varphi\) supplies the definition.
- The only nonlogical symbols needed by that formula may be taken
  from the shared \(L\)-vocabulary of the two finite conjunctions.
- The same \(T_0\) therefore implicitly defines \(P\): its explicit
  definition forces any two of its expansions of a common
  \(L\)-reduct to agree.

This is a uniform existence statement. Neither a model-specific
parameter nor a separate finite support for each tuple is introduced.

## Suggested example: a total right-inverse relation

Take \(L=\{\cdot,e\}\), consisting of a binary function and a constant,
and let \(P\) be binary. Let \(T\) contain the monoid axioms
\[
 \forall x\,y\,z\ ((x\cdot y)\cdot z=x\cdot(y\cdot z)),
 \qquad
 \forall x\ (e\cdot x=x\land x\cdot e=x),
\]
together with
\[
 \forall x\,\exists y\,P(x,y),
 \qquad
 \forall x\,y\,(P(x,y)\to x\cdot y=e).
 \tag{12}
\]
These sentences require \(P\) to choose at least one right inverse
for every element; no explicit biconditional defining \(P\) is an
axiom.

Nevertheless \(P\) is uniquely determined by the monoid reduct.
First every element has a right inverse by (12). If \(a\cdot b=e\),
choose \(c\) with \(b\cdot c=e\). Associativity gives
\[
 a=a\cdot e=a\cdot(b\cdot c)=(a\cdot b)\cdot c=e\cdot c=c,
\]
so \(b\cdot a=e\) as well. If also \(a\cdot d=e\), then
\[
 d=e\cdot d=(b\cdot a)\cdot d
   =b\cdot(a\cdot d)=b\cdot e=b.
\]
Thus every element has exactly one right inverse. Since \(P\) is
total and contains only right-inverse pairs, it must contain
exactly those pairs:
\[
 T\models\forall x\,y\,
       \bigl(P(x,y)\leftrightarrow x\cdot y=e\bigr).
\]
The explicit defining formula is therefore
\[
 \varphi(x,y)\equiv x\cdot y=e.
\]
This example uses function symbols, a constant, and equality, and
illustrates how existence plus constraints can force an implicit
definition. Its four displayed monoid/specification sentences already
provide a finite support; adding further sentences to the theory does
not require changing the definition.

## Incorporation guidance

The theorem should retain the active destination thm:beth. Its statement
should say that \(P\) is fresh over \(L\), permit \(n=0\), specify the
same-reduct hypothesis without requiring expansions of every reduct,
and state the finite-support conclusion if desired. The argument above
is a complete derivation from the full Craig theorem, compactness,
and completeness. It neither supplies nor presupposes an unproved
extension of a restricted local Maehara lemma to function-bearing
signatures.
