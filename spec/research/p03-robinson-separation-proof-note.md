# Common completions, Robinson separation, and Craig interpolation

Date: 2026-09-06.

This note proves the finite-separation/common-completion step using
compactness and a transfinite completion, without using Craig or
Robinson. It then proves the Craig--Robinson equivalence, including
open formulas, and checks the active direct Robinson-to-Beth proof.
Only this note was written.

## Active statements and background

The active reader statements are in
handbook/parts/p03/preservation-abstract-logic.tex:

- thm:p03-robinson-joint-consistency, read at lines 110–119;
- thm:p03-beth-definability, read at lines 272–275;
- the Craig--Robinson discussion beginning at line 282.

The active annex proofs are annex:p3.abstract.1 and annex:p3.abstract.2
in handbook/annex/p03/editorial-proofs.tex, beginning at lines 21 and 51.
The first currently uses the Stone space of common completions and then
the Keisler--Shelah ultrapower theorem. The common-completion argument
below replaces only that proof's first step. It does not assume or
establish the subsequent joint-model conclusion by itself.

For arbitrary signatures, use the same ambient Axiom of Choice as the
active thm:fol-compactness and thm:fol-completeness. These are in
handbook/restoration/inherited-04921-04967.tex and
handbook/restoration/inherited-04713-04920.tex, respectively, and have
local proofs. Soundness is thm:fol-soundness. These results identify
syntactic consistency with satisfiability and syntactic consequence
with semantic consequence in the languages used below.

Signatures are set-sized; common symbols must have the same kind and
arity. Equality and logical constants are logical symbols. Structures
have nonempty domains. For a set of sentences, “compatible with \(T_i\)”
means that its union with \(T_i\) is satisfiable.

## 1. Common-completion lemma, without Craig or Robinson

Let \(L_1,L_2\) be compatible signatures and \(L_0=L_1\cap L_2\).
Let \(T_i\subseteq\operatorname{Sent}(L_i)\) be satisfiable. Suppose
there is no \(L_0\)-sentence \(\sigma\) such that
\[
 T_1\models\sigma,\qquad T_2\models\neg\sigma.
 \tag{1}
\]
If the hypothesis is stated with derivability, the active completeness
theorem gives exactly this semantic hypothesis.

Then there is a complete consistent \(L_0\)-theory \(S\) such that
both \(T_1\cup S\) and \(T_2\cup S\) are satisfiable.

### Collect all common-language consequences first

For \(i=1,2\), put
\[
 C_i=\{\sigma\in\operatorname{Sent}(L_0):T_i\models\sigma\},
 \qquad C=C_1\cup C_2.
\]
The set \(C\) is satisfiable. If it were not, compactness would give
finite \(\Delta_i\subseteq C_i\) whose union is unsatisfiable.
Put
\[
 \alpha=\bigwedge\Delta_1,\qquad
 \beta=\bigwedge\Delta_2,
\]
using \(\top\) for an empty conjunction. Then
\[
 T_1\models\alpha,\qquad
 T_2\models\beta,\qquad
 \models\beta\to\neg\alpha.
\]
Thus \(T_1\models\alpha\) and \(T_2\models\neg\alpha\), contradicting
(1). This is the finite-sentence separation calculation needed here.
It uses no interpolation theorem.

### The invariant that makes every later decision safe

If \(U\supseteq C\) is any satisfiable set of \(L_0\)-sentences, then
both \(T_i\cup U\) are satisfiable.

Indeed, if \(T_i\cup U\) were unsatisfiable, compactness would give
finite \(\Gamma\subseteq U\) such that
\[
 T_i\models\neg\bigwedge\Gamma.
\]
The displayed sentence belongs to \(C_i\subseteq U\), while \(U\)
also contains every member of \(\Gamma\). This contradicts the
satisfiability of \(U\).

Thus ordinary consistency of an extension of \(C\) is sufficient to
preserve compatibility with both original theories simultaneously.

### Transfinite completion and limit stages

Use Choice to well-order the set \(\operatorname{Sent}(L_0)\), writing
it as \((\sigma_\alpha)_{\alpha<\kappa}\) for an ordinal \(\kappa\).
Define an increasing sequence \((U_\alpha)_{\alpha\leq\kappa}\):
\[
 U_0=C,
\]
\[
 U_{\alpha+1}=
 \begin{cases}
 U_\alpha\cup\{\sigma_\alpha\},
          &\text{if this set is satisfiable},\\
 U_\alpha\cup\{\neg\sigma_\alpha\},
          &\text{otherwise},
 \end{cases}
\]
and at a limit ordinal \(\lambda\),
\[
 U_\lambda=\bigcup_{\alpha<\lambda}U_\alpha.
\]

Every successor stage is satisfiable. If adjoining \(\sigma_\alpha\)
is impossible, every model of the already satisfiable \(U_\alpha\)
satisfies \(\neg\sigma_\alpha\), so adjoining the negative sentence
preserves satisfiability. Hence at least one truth value is always
available. By the invariant just proved, that truth value also
preserves compatibility with both \(T_i\).

At a limit stage, every finite subset of \(U_\lambda\) is contained
in one earlier \(U_\alpha\): finitely many ordinals below a limit have
a common upper bound below that limit. It therefore has a model.
Compactness makes \(U_\lambda\) satisfiable. The compatibility
invariant applies at the limit as well.

The terminal set \(S=U_\kappa\) decides every \(L_0\)-sentence and
is satisfiable. It is consequently a complete consistent theory.
For example, if \(S\models\sigma\) but \(\sigma\notin S\), completeness
of the decisions puts \(\neg\sigma\) in \(S\), a contradiction.
Thus \(S\) is closed under consequences as well as deciding every
sentence. Since \(C\subseteq S\), both \(T_i\cup S\) are satisfiable.

This construction uses Choice for the well-ordering and the stated
arbitrary-signature compactness theorem at the limit stages. Its
successor rule is deterministic once that well-order is fixed; it
does not select a model at every stage.

### Why mere compatibility is not enough

It would be false to claim that every partial common theory
compatible with each \(T_i\) admits a next truth-value decision
preserving both compatibilities.

For example, take common nullary predicates \(r,p\), and let
\[
 T_1=\{r\to p\},\qquad T_2=\{r\to\neg p\}.
\]
The two theories even have a joint model with \(r\) false, so they
have no separating common sentence. Nevertheless \(U=\{r\}\) is
compatible with each separately, while
\[
 T_1\cup U\cup\{\neg p\}
 \quad\text{and}\quad
 T_2\cup U\cup\{p\}
\]
are both inconsistent. Neither decision about \(p\) preserves both.

The construction above avoids this problem because \(C_1\cup C_2\)
already contains \(r\to p\) and \(r\to\neg p\), and therefore entails
\(\neg r\). No consistent extension of that starting set can choose
the bad partial theory \(U=\{r\}\). This example concerns an
insufficient construction invariant, not a failure of Robinson.

## 2. Equivalence with the common-complete-theory formulation

The conclusion of Section 1 is itself equivalent to absence of a
common separator. For the converse, suppose a complete consistent
\(S\) is compatible with each \(T_i\). If
\(T_1\models\sigma\) and \(T_2\models\neg\sigma\), completeness of
\(S\) puts either \(\sigma\) or \(\neg\sigma\) in \(S\). One of the
two asserted compatibilities then fails.

Consequently the two usual formulations of Robinson joint consistency
are equivalent:

1. consistent theories with no separated common-language sentence
   have consistent union;
2. consistent theories extending one complete consistent theory of
   their common language have consistent union.

To obtain formulation 1 from formulation 2, first construct \(S\) as
above and apply formulation 2 to \(T_1\cup S,T_2\cup S\).
To obtain formulation 2 from formulation 1, a common complete theory
rules out a separator by the preceding paragraph.

The construction of \(S\) supplies models of \(T_i\cup S\) whose
common reducts are elementarily equivalent. It does not assert that
those particular reducts are identical or isomorphic. A separate
joint-consistency argument is still needed to put the two expansions
on one common reduct. This is the role of the ultrapower/transport
step in the current annex proof, or of Craig in the implication below.

## 3. The exact separation form of Robinson

Under Robinson joint consistency and ordinary completeness, the
following statement holds for arbitrary \(T_1,T_2\), including
inconsistent theories:
\[
 T_1\cup T_2\text{ is unsatisfiable}
 \quad\Longleftrightarrow\quad
 \exists\sigma\in\operatorname{Sent}(L_0)\
   (T_1\models\sigma\ \land\ T_2\models\neg\sigma).
 \tag{2}
\]
The right-to-left implication is immediate. If the union is
unsatisfiable and both sides are satisfiable, the contrapositive
of Robinson gives the separator. If \(T_1\) is unsatisfiable, use
\(\sigma=\bot\). If \(T_2\) is unsatisfiable, use
\(\sigma=\top\). These cover the case where both are unsatisfiable
as well. Logical constants ensure the construction works even when
the common nonlogical signature is empty.

By completeness, semantic consequences in (2) can be replaced by
derivations. Finite derivations, or the consequence form of
compactness, also supply finite subsets of each \(T_i\) supporting
the same separator.

## 4. Sentence Craig implies Robinson

Assume Craig interpolation for sentences. Suppose \(T_1,T_2\) have no
common separator, but \(T_1\cup T_2\) is unsatisfiable. Compactness
gives finite \(\Delta_i\subseteq T_i\) with unsatisfiable union.
Let
\[
 A=\bigwedge\Delta_1,\qquad B=\bigwedge\Delta_2.
\]
Then \(\models A\to\neg B\). Craig gives a sentence \(J\) such that
\[
 \models A\to J,\qquad \models J\to\neg B,
\]
whose nonlogical symbols occur in both \(A\) and \(B\), and hence
belong to \(L_0\). The second validity is classically equivalent to
\(\models B\to\neg J\). Therefore
\[
 T_1\models J,\qquad T_2\models\neg J.
\]
Completeness turns these into derivations if the Robinson hypothesis
uses \(\vdash\), contradicting that hypothesis. This proves Robinson.

The same argument proves the full finite-support separation statement
(2) directly. Empty finite conjunctions and inconsistent sides cause
no problem because Craig allows \(\bot,\top\).

## 5. Robinson implies sentence Craig

Let \(A,B\) be first-order sentences with \(\models A\to B\).
Use the **occurrence signatures**
\[
 L_1=\operatorname{sig}(A),\qquad
 L_2=\operatorname{sig}(B),\qquad
 L_0=L_1\cap L_2,
\]
where only nonlogical symbols are counted. This choice is necessary:
using a larger common ambient signature would not by itself establish
Craig's restriction to symbols actually occurring on both sides.

If \(A\) is unsatisfiable, take \(J=\bot\). If \(B\) is valid, take
\(J=\top\). Otherwise the theories
\[
 T_1=\{A\},\qquad T_2=\{\neg B\}
\]
are individually satisfiable, while their union is unsatisfiable.
The contrapositive of Robinson gives an \(L_0\)-sentence \(J\) with
\[
 A\models J,\qquad \neg B\models\neg J.
\]
Classical contraposition yields \(J\models B\), so \(J\) is exactly
the required interpolant. The two preliminary cases are needed if
one invokes the version of Robinson whose hypotheses require each
input theory to be consistent.

Functions and constants need no extra argument in this reduction:
they belong to the occurrence signatures and are restricted by the
same signature intersection. Equality remains logical.

## 6. Open-formula Craig and the free-variable intersection

Sentence Craig, and hence Robinson, gives the full open-formula
version. Let \(\varphi,\psi\) be formulas satisfying
\(\models\varphi\to\psi\) under every assignment. Let
\[
 V=\operatorname{FV}(\varphi)\cup\operatorname{FV}(\psi),
 \qquad
 W=\operatorname{FV}(\varphi)\cap\operatorname{FV}(\psi).
\]
Both sets are finite. For each \(x\in V\), choose one fresh constant
symbol \(c_x\), using the same constant on both sides when \(x\in W\).
Replace only free occurrences of \(x\) by \(c_x\). This produces
sentences \(\varphi^{\bar c},\psi^{\bar c}\) with
\[
 \models\varphi^{\bar c}\to\psi^{\bar c}.
\]
The validity follows because every interpretation of the new
constants supplies an assignment to the original free variables.

Apply the sentence result using the exact occurrence signatures of
these two sentences. Their common signature is
\[
 \bigl(\operatorname{sig}(\varphi)\cap
             \operatorname{sig}(\psi)\bigr)
       \cup\{c_x:x\in W\}.
\]
A parameter for a variable free on only one side therefore cannot
occur in the sentence interpolant \(J\).

Rename the bound variables of \(J\) away from \(W\), and replace each
remaining fresh \(c_x\) by \(x\), including occurrences inside compound
terms. Let the resulting formula be \(\theta\). It satisfies
\[
 \operatorname{sig}(\theta)\subseteq
      \operatorname{sig}(\varphi)\cap\operatorname{sig}(\psi),
 \qquad
 \operatorname{FV}(\theta)\subseteq W.
\]
For any original structure and assignment, interpret every fresh
\(c_x\) by the assigned value of \(x\). Applying the two sentence
implications and the substitution lemma gives
\[
 \models\varphi\to\theta,\qquad
 \models\theta\to\psi.
\]
Distinct constant symbols may denote the same element; no distinctness
assumption on variable values is introduced. Existing constants in
the original language are retained. Bound-variable renaming prevents
capture during the inverse replacement.

Unsatisfiable \(\varphi\), valid \(\psi\), an empty shared free-variable
set, and an empty shared nonlogical signature are all covered by
the sentence cases and logical constants. Conversely, open-formula
Craig includes sentence Craig as the special case with no free
variables. This proves the exact Craig--Robinson equivalence used
by the handbook.

## 7. Direct Robinson-to-Beth, with all edge cases

Let \(P\notin L\) have finite arity \(n\geq0\), and let
\(T\subseteq\operatorname{Sent}(L\cup\{P\})\) implicitly define \(P\)
over \(L\). Rename only \(P\) to a fresh \(P'\), obtaining \(T'\).
Choose fresh constants \(\bar c\) for the \(n\) coordinates; for
\(n=0\), take the empty list.

Consider
\[
 U_1=T\cup\{P(\bar c)\},\qquad
 U_2=T'\cup\{\neg P'(\bar c)\}.
\]
Their union is unsatisfiable: a model would give two \(T\)-expansions
of the same \(L\)-reduct disagreeing on the named tuple. Their common
signature is exactly \(L\cup\{\bar c\}\), so the full separation form
(2) gives a sentence \(\sigma(\bar c)\) in that signature with
\[
 T\cup\{P(\bar c)\}\models\sigma(\bar c),\qquad
 T'\cup\{\neg P'(\bar c)\}\models\neg\sigma(\bar c).
\]
Equivalently,
\[
 T\models P(\bar c)\to\sigma(\bar c),\qquad
 T'\models\sigma(\bar c)\to P'(\bar c).
\]
Rename \(P'\) back to \(P\). The common-language sentence
\(\sigma\) is unchanged. Therefore
\[
 T\models P(\bar c)\leftrightarrow\sigma(\bar c).
\]

If the consistent-input formulation of Robinson is used instead of
(2), make its two preliminary cases explicit:

- If \(U_1\) is unsatisfiable, \(T\models\neg P(\bar c)\), and fresh
  parameters yield \(T\models\forall\bar x\,\neg P(\bar x)\).
  The explicit definition is \(\bot\).
- If \(U_2\) is unsatisfiable, rename back to obtain
  \(T\models P(\bar c)\). The explicit definition is \(\top\).
- Otherwise both inputs are consistent and Robinson's contrapositive
  applies directly.

These cases also cover an inconsistent \(T\).

For parameter elimination, rename the finitely many bound variables
of \(\sigma\) away from distinct \(x_1,\ldots,x_n\), then replace
the new constants by these variables throughout all terms and
formulas. The resulting \(L\)-formula \(\theta(\bar x)\) has no other
free variables. For each model of \(T\), interpret the constants
by an arbitrary tuple, whose values may repeat. The substitution
lemma yields
\[
 T\models\forall\bar x\,
       (P(\bar x)\leftrightarrow\theta(\bar x)).
 \tag{3}
\]
For \(n=0\), no parameters or variables are present and (3) is a
sentence biconditional. No existence of a \(T\)-expansion for every
\(L\)-structure is assumed.

Finally apply the consequence form of compactness to the single
sentence (3). It supplies a finite \(T_0\subseteq T\) supporting
that same definition for every model and every tuple. Completeness
gives the corresponding derivation from \(T_0\), and hence from \(T\).
The formula uses only a finite part of \(L\) because it is finite.
This matches the strengthened Part VII Beth statement.

## 8. Exact incorporation observations from the current text

The current direct Beth proof at annex:p3.abstract.2 has the correct
orientation of both entailments and already branches on the two
inconsistent-input cases. Its predicate-renaming step is valid.
The following additions make its scope agree explicitly with the
new Part VII theorem and proof:

- Inherit or state the ambient Choice assumption used for arbitrary
  languages in compactness, completeness, and the Robinson proof.
- State \(n\geq0\), with empty tuples and quantifier blocks in the
  nullary case.
- Spell out capture avoidance, replacement inside function terms,
  and arbitrary, possibly equal values of fresh parameter constants,
  or refer to the exact corresponding step of annex:p7.interp.4.
- After the uniform sentence definition, invoke compactness and
  completeness for one finite supporting \(T_0\) and its derivation.

The reader's current Craig-to-Robinson paragraph has the right finite
conjunction argument. In its converse, an unconditional application
of Robinson to \(\{\varphi\}\) and \(\{\neg\psi\}\) skips the
consistent-input hypothesis when \(\varphi\) is unsatisfiable or
\(\psi\) is valid. Add the \(\bot\) and \(\top\) cases from Section 5,
or explicitly invoke the generalized separation form (2).
Also specify occurrence signatures and the fresh-constant argument
when claiming the full open-formula Craig result.

The common-completion construction above is independent of Craig
and Robinson, so it can replace the compact-Stone-space separation
paragraph without creating a circular proof. Mere simultaneous
compatibility must not replace the stronger starting invariant
\(C_1\cup C_2\subseteq U\).

The consequence chain proved here is
Craig \(\Longleftrightarrow\) Robinson \(\Longrightarrow\) Beth.
The current separate citation for a reverse Beth-to-Craig principle
is not used or verified by this bounded derivation.

## Review outcome

The requested common completion, truth-value extension, limit-stage
argument, sentence and open-formula Craig--Robinson equivalence, and
direct Beth consequence are established with the stated foundational
assumptions. The concrete missing cases in the current abbreviated
Craig converse and the exact additions aligning direct Beth with
Part VII are identified above. No manuscript edits, tests, builds,
renders, or additional agents were used.
