# Kozen (1983), “Results on the Propositional μ-Calculus”

## Purpose and closure standard

This note reconstructs the source presentation registered as **N-c-018.a**.
It distinguishes the full language from the syntactically restricted theorem
package, records the literal theorem and proof boundaries, and supplies the
page evidence needed for reader-facing prose. Later full-calculus results are
not used to strengthen the 1983 claims.

## Bibliographic identity, access, and rights

- Dexter Kozen, “Results on the Propositional μ-Calculus,” *Theoretical
  Computer Science* 27 (1983), 333–354.
- DOI: 10.1016/0304-3975(82)90125-6.
- The printed publisher is North-Holland/Elsevier Science Publishers B.V.
- Author bibliography:
  <https://www.cs.cornell.edu/~kozen/Papers/papers_by_year.htm#K83a>.
- Complete author-hosted scan:
  <https://www.cs.cornell.edu/~kozen/Papers/mu.pdf>.
- Local scholarly copy:
  tmp/pdfs/p09-kozen-1983/kozen-mu-1983.pdf.
- File size: 634,158 bytes.
- SHA-256:
  058524BDA54CB561814868B78FB353533BE64BE0C87150E48928E7084D21710C.
- The PDF has twelve landscape scan pages. The first eleven pair printed
  article pages; the last contains printed p. 354 and a blank facing page.
- Printed p. 333 carries © 1983 Elsevier Science Publishers B.V.
  (North-Holland). No Creative Commons or article-specific republication
  license appears in the scan. Author-hosted reading access is not treated
  as permission to republish the article.

Every one of the twelve PDF pages was rendered at 220 dpi and visually
inspected. No claim below rests on unverified OCR.

## Scan-to-printed-page map

| PDF page | Printed article page(s) | Main content |
|---:|---:|---|
| 1 | 333 | title, abstract, introduction |
| 2 | 334–335 | announced results; syntax and semantics |
| 3 | 336–337 | positive normal form; closure |
| 4 | 338–339 | active variables; aconjunctivity; continuity boundary |
| 5 | 340–341 | expressiveness; deductive system |
| 6 | 342–343 | derived proof rule; tableau rules and counters |
| 7 | 344–345 | counter updates; alternating algorithm |
| 8 | 346–347 | termination lemmas; main theorem |
| 9 | 348–349 | consistency-guided tableau subtree; rejection argument |
| 10 | 350–351 | extracted model and truth conditions |
| 11 | 352–353 | structural proof; conclusion of main theorem |
| 12 | 354 | remaining references |

## Abstract and announced scope

The abstract defines the subject as propositional modal logic with a least
fixed-point operator. It announces:

1. strict expressive superiority over propositional dynamic logic;
2. for a restricted version, an exponential-time decision procedure and a
   small-model property; and
3. for that restricted version, a complete deductive system.

The opening of §6 identifies the restriction exactly as aconjunctivity.
The paper also says that the full language is decidable by earlier work but
that the best bound then known was nonelementary. Thus “the μ-calculus is
EXPTIME-complete” is not the literal 1983 theorem; the literal result is for
the aconjunctive fragment. The later 1988 full-calculus finite-model and
completeness result is a distinct source.

## The two source languages

Section 2 defines \(L_\mu\) and an infinitary companion \(L_{\mu+}\).
The latter adds ordinal approximants and is used in the transfinite part of
the model construction; it is not a second object language registered by the
handbook.

The primitive nonlogical symbols are:

- propositional constants \(P,Q,\ldots\), including \(0,1\);
- propositional variables \(X,Y,\ldots\); and
- program constants \(a,b,\ldots\).

The formation clauses on printed p. 334 are

\[
\begin{array}{llll}
(2.1.1)&X,&(2.1.2)&P,\\
(2.1.3)&p\lor q,&(2.1.4)&\neg p,\\
(2.1.5)&\langle a\rangle p,&
(2.1.6)&\alpha X.pX\quad(\alpha\text{ an ordinal}),\\
(2.1.7)&\mu X.pX.&
\end{array}
\]

Clause (2.1.6) belongs to \(L_{\mu+}\); the other clauses form \(L_\mu\).
In (2.1.6) and (2.1.7), \(pX\) must be positive in \(X\): every free
occurrence of \(X\) is within the scope of an even number of negations.
The binders are formula constructors, and their denotations are state sets.
They are not programs or metalinguistic proof rules.

The necessity and use of \(L_{\mu+}\) are explicit in the source. Ordinary
\(L_\mu\) has only the least-fixed-point formula \(\mu X.pX\), whereas the
proof on pp. 350–353 assigns ordinal stages to unfoldings. The symbols
\(\alpha X.pX\) are the source’s eliminable transfinite approximants used for
that proof; they do not add a new handbook logic.

## Models and semantics

A model is \(M=(S,I)\), where \(S\) is a set of states and \(I\) sends a
propositional constant to a subset of \(S\) and a program constant to a binary
relation on \(S\). The source requires \(I(0)=\varnothing\) and \(I(1)=S\).
A valuation assigns a subset of \(S\) to each propositional variable.

Writing \(\bar A=(A_1,\ldots,A_n)\) for the values of the free variables, the
semantic clauses on pp. 334–335 are:

\[
\begin{aligned}
X_i^M(\bar A)&=A_i,\\
P^M(\bar A)&=I(P),\\
(p\lor q)^M(\bar A)&=p^M(\bar A)\cup q^M(\bar A),\\
(\neg p)^M(\bar A)&=S\setminus p^M(\bar A),\\
(\langle a\rangle p)^M(\bar A)&=
 \{s:\exists t\in p^M(\bar A)\ ((s,t)\in I(a))\}.
\end{aligned}
\]

For positive \(pX\), the induced operator is monotone in \(X\). The source
defines

\[
\begin{aligned}
0X.pX^M(\bar A)&=\varnothing,\\
(\alpha+1)X.pX^M(\bar A)
  &=p^M(\alpha X.pX^M(\bar A),\bar A),\\
\delta X.pX^M(\bar A)
  &=\bigcup_{\beta<\delta}\beta X.pX^M(\bar A)
  \quad(\delta\text{ a limit ordinal}),\\
\mu X.pX^M(\bar A)
  &=\bigcup_\beta\beta X.pX^M(\bar A).
\end{aligned}
\]

The least ordinal \(\kappa\) at which the approximant is unchanged is called
the closure ordinal of the induced operator. Equation (2.2.9) also gives the
Knaster–Tarski characterization:

\[
(\mu X.pX)^M(\bar A)
=\bigcap\{B:p^M(B,\bar A)\subseteq B\}.
\]

For a closed formula \(p\), \(M,s\models p\) iff \(s\in p^M\).

## Defined operations and positive normal form

Section 3.1 defines the usual Boolean operations together with

\[
[a]p:=\neg\langle a\rangle\neg p,
\qquad
\nu X.pX:=\neg\mu X.\neg p\neg X.
\]

The second display is the source’s fixed-point dual, with the bound variable
polarity reversed inside the body. Equation (3.1.1) identifies its semantics
with the greatest fixed point. After pushing negations inward and renaming
bound variables, every formula may be put in positive normal form over
\(\lor,\land,\mu,\nu,\langle a\rangle,[a]\), with negation applied only to
primitive proposition constants and with no variable quantified twice.

Positive normal form is used by the closure, active-variable,
aconjunctivity, and tableau definitions. It is not an optional typographical
preference.

## Source closure

Let \(p_0\) be a fixed closed formula in positive normal form. For every
bound variable \(X\), the unique enclosing \(\mu\)- or \(\nu\)-formula that
binds it is denoted \(\sigma X\), where \(\sigma\in\{\mu,\nu\}\).
The paper orders subformulas by containment and defines a substitution map
\(e\) which replaces the relevant free bound-variable occurrences by their
binding formulas, from the innermost relevant binder outward.

Definition 3.2.2 calls

\[
\operatorname{CL}(p_0)=\{e(p):p\text{ is a subformula of }p_0\}
\]

the closure of \(p_0\). The substitution makes every member closed.
The closure is finite and no larger than the number of symbols of \(p_0\).
Proposition 3.2.3 gives the equivalent least-set characterization:

1. \(p_0\in\operatorname{CL}(p_0)\);
2. \(\neg P\in\operatorname{CL}(p_0)\) implies
   \(P\in\operatorname{CL}(p_0)\);
3. \(p\lor q\) or \(p\land q\) in the closure implies that both components
   are in it;
4. \(\langle a\rangle p\) or \([a]p\) in the closure implies that \(p\) is
   in it; and
5. \(\sigma X.pX\) in the closure implies that its one-step unfolding
   \(p(\sigma X.pX)\) is in it.

The source proves Proposition 3.2.3. This closure is the finite formula
vocabulary carried by tableau labels. It is analogous to, but not literally
the same definition as, the PDL Fischer–Ladner closure.

## Active variables

Definition 3.3.1 is needed because a variable may become free only after
intervening fixed-point binders are unfolded. For a subformula \(p\) and a
bound variable \(Y\), the source says that \(Y\) is *active in \(p\)* when
\(\sigma Y\) is a proper superformula of \(p\) and, after substituting the
intervening binding formulas specified by the subformula order, the resulting
formula contains a free occurrence of \(Y\).

This is a metalinguistic relation between a bound variable and a source
subformula. It is not the ordinary free-variable relation. It is necessary
because the tableau must carry a counter for a least fixed point even through
a subformula in which the variable is not literally free before unfolding.
The set of variables active in \(p\) is \(A_p\), with \(A_{\mu p}\) and
\(A_{\nu p}\) its least- and greatest-fixed-point subsequences.

The paper’s example (3.3.2) is

\[
\mu X.\nu Y.
\bigl(X\land\mu Z.(\langle a\rangle Y\lor[b]Z)\bigr).
\]

Although \(X\) is not free in \(\langle a\rangle Y\), it is active there:
unfolding the intervening binder for \(Y\) exposes the conjunct \(X\).
Lemma 3.3.3 proves transitivity in the needed form: if \(Y\) is active in
\(p\), and \(X\) is active in the binding formula \(\sigma Y\), then \(X\)
is active in \(p\). The proof is printed.

## The exact restriction: aconjunctivity

Definition 3.3.4 says that a positive-normal formula \(p_0\) is
*aconjunctive in the \(\mu\)-variable \(X\)* when, for every conjunction
\(p\land q\) occurring as a subformula of \(p_0\), \(X\) is active in at most
one of \(p,q\). The formula is *aconjunctive* when it is aconjunctive in
every \(\mu\)-variable.

Standing: aconjunctivity is a syntactic property of a positive-normal formula.
It is not a property of a model, not a ban on conjunction, and not the
continuity condition.

Nonredundancy: ordinary occurrence and ordinary freeness cannot state the
restriction, because Example (3.3.2) has a variable active after unfolding
where it is not initially free. The restriction is weaker than full
syntactic continuity and allows conjunctions which do not duplicate one
active least-fixed-point obligation.

Use: at the conjunction rule in §6.1, the lists of \(\mu\)-counters can be
split into disjoint successor lists. Printed p. 344 says explicitly that
without aconjunctivity a \(\mu\)-counter would have to be duplicated. That
single-copy invariant is what permits the bounded-counter termination and
exponential-time argument.

Example (3.3.2) is not aconjunctive: in the subformula

\[
X\land\mu Z.(\langle a\rangle Y\lor[b]Z)
\]

the \(\mu\)-variable \(X\) is active in both conjuncts. By contrast,
\(\mu X.(P\lor\langle a\rangle X)\) is aconjunctive, because it has no
conjunction at which the active \(X\)-obligation is duplicated.

## Continuity boundary

Printed p. 339 defines continuity of the operator induced by \(pX\) through
preservation of unions of increasing ordinal chains. If \(pX\) is continuous
in every model, then

\[
\mu X.pX=\omega X.pX.
\]

The formula \(\mu X.[a]X\) supplies the source’s counterexample to continuity:
on Figure 1, the top state enters at stage \(\omega+1\), not stage \(\omega\).
Its denotation is the states from which no infinite \(a\)-path begins.
This explains both why transfinite approximants occur and why
aconjunctivity is not merely another name for continuity.

## Expressiveness results and examples

Section 4 records the PDL fixed-point encodings

\[
\langle a^*\rangle p
 \equiv \mu X.(p\lor\langle a\rangle X),
\qquad
[a^*]p
 \equiv \nu X.(p\land[a]X).
\]

It also gives the liveness example

\[
\mu X.(p\lor[a]X),
\]

read as “along every \(a\)-path, \(p\) must eventually become true.”

Proposition 4.1, attributed to Streett, states that
\(\mu X.[a]X\) is not equivalent to any PDL formula. The printed proof assumes
an equivalent PDL formula, applies PDL filtration to Figure 1, and notes that
identifying finitely many PDL-equivalent states creates an \(a\)-loop. The
filtered root still satisfies the alleged PDL equivalent but no longer
satisfies \(\mu X.[a]X\), contradiction. This is a short printed proof.

Proposition 4.2 states a stronger, single-model separation. In Figure 2,

\[
\mu X.[a]\langle a\rangle X
\]

defines the even states, while every PDL formula, even with tests and reverse,
defines only a finite or cofinite set. The proposition is attributed to
reference [12] and no proof is printed.

The paper further says that full \(L_\mu\) encodes Streett’s \(\Delta\)PDL
through \(\Delta a=\nu X.\langle a\rangle X\), while the aconjunctive fragment
encodes a well-structured restriction of \(\Delta\)PDL. It does not turn that
observation into a general modern automata/game theorem.

## Deductive system

Section 5 uses equations \(p=q\) and inequalities \(p\le q\), where
\(p\le q\) abbreviates \(p\lor q=q\). It includes equational logic and
substitution of equals for equals when the syntactic binder conditions remain
well formed. The nonlogical axioms/rules on p. 341 are:

\[
\begin{array}{ll}
(5.1)&\text{the axioms of Boolean algebra},\\
(5.2)&\langle a\rangle X\lor\langle a\rangle Y
       =\langle a\rangle(X\lor Y),\\
(5.3)&\langle a\rangle X\land[a]Y
       \le \langle a\rangle(X\land Y),\\
(5.4)&\langle a\rangle0=0,\\
(5.5)&p(\mu X.pX)\le\mu X.pX,\\
(5.6)&pY\le Y\ \Longrightarrow\ \mu X.pX\le Y.
\end{array}
\]

For (5.5), the fixed-point formula must be free for \(X\) in the body.
For (5.6), \(Y\) does not occur in \(pX\). A formula is called consistent
when its equality to \(0\) is not derivable.

Axioms (5.5) and (5.6) state that \(\mu X.pX\) is the least pre-fixed point.
Rule (5.6) is Park’s fixed-point induction rule. The calculus is used in the
consistency side of Theorem 6.3.1.

Proposition 5.7 records change of bound variable, monotonicity, fixed-point
unfolding, elimination of a vacuous binder, and a strengthened induction
consequence. Only the proof of item (vi) is printed in detail; the paper
refers the reader elsewhere for the basic fixed-point facts. Item (vi) is
then used crucially in the proof of Theorem 6.3.1.

## Tableau vocabulary and five extension rules

Section 6 fixes an aconjunctive closed \(p_0\) in positive normal form and
constructs a labelled tree \(T\). A node \(s\) carries a finite set
\(\Gamma_s\) of closure formulas. The root label is \(\{p_0\}\).
The five extension rules on pp. 342–343 are:

1. **Conjunction:** replace \(p\land q\) by both \(p,q\) in one successor.
2. **Disjunction:** create two successors, one replacing \(p\lor q\) by
   \(p\), the other by \(q\).
3. **Binder:** replace \(\sigma X.pX\) by its body/unfolding in one successor.
4. **Bound variable:** replace \(X\) by the body of its unique binding formula
   \(\sigma X.pX\) in one successor.
5. **Modal demand:** for every \(\langle b\rangle p\in\Gamma_s\), create a
   \(b\)-labelled successor whose label contains \(p\) and every \(q\) such
   that \([b]q\in\Gamma_s\).

The modal rule creates a separate successor for every diamond demand.
The disjunction rule represents a choice; the modal rule requires all created
successors to survive. These are reflected as existential and universal
branches in the alternating algorithm.

## Counters and why the restriction is used

For each formula \(p\in\Gamma_s\), the construction carries a list
\(C(s,p)\) of counters corresponding to the variables active in \(p\).
The lists for distinct formulas are disjoint. If \(A_p=X_1,\ldots,X_n\),
then \(C(s,p)=(c_1,\ldots,c_n)\), with \(X(c_i)=X_i\).

- A counter for a \(\mu\)-variable ranges from \(0\) through
  \(2^{|p_0|}\).
- A counter for a \(\nu\)-variable is a one-bit flag in \(\{0,1\}\).
- A global list \(G\) is a shuffle of the existing \(\mu\)-counter lists.
  Its left-to-right order is a dynamic priority order.

The source gives update clauses (6.1.6)–(6.1.13). Their operative effects
are:

- unfolding a binder creates the counter newly made active;
- choosing a disjunct deletes counters no longer active on that branch;
- splitting a conjunction distributes the \(\mu\)-counters to disjoint
  successor lists, using aconjunctivity;
- unfolding a variable increments its counter and resets lower-priority
  obligations as specified by \(G\);
- taking a modal successor deletes inactive counters and resets the
  greatest-fixed-point flags; and
- conflicting inherited lists retain the higher-priority list while merging
  the lower-priority numerical information.

These counter lists are source proof machinery. They are not semantic
priorities of the later parity-game presentation.

## Alternating decision procedure

Section 6.2 executes the tableau with an alternating Turing machine.
Conjunction, disjunction, binder, and bound-variable rules are applied before
the modal rule. Disjunction branches existentially; the modal rule branches
universally over the demanded program successors. A \(\nu\)-variable may be
unfolded only when its associated one-bit counter is zero.

The four stopping/actions are literal:

1. if \(P,\neg P\in\Gamma_s\), halt and reject;
2. if some \(\mu\)-counter exceeds \(2^{|p_0|}\), halt and reject;
3. if only the modal rule applies and neither rejection condition holds,
   apply the modal rule;
4. if no rule applies and neither rejection condition holds, halt and accept.

The paper proves \(|G|\le |p_0|^2\) and says that the process needs at most
\(|p_0|^3\) space to encode the node label and counters. It then invokes the
standard alternating-space simulation to obtain deterministic exponential
time. Lemma 6.2.6 bounds the number of counter increments along the relevant
intervals; Lemma 6.2.7 uses that bound and a minimal infinitely unfolded
variable to prove that one of the four conditions occurs after finite time.
Thus the possibility of an infinite raw tableau expansion is closed inside
the source proof, rather than assumed away.

The matching EXPTIME lower bound is not reproved as a new reduction in this
paper. The introductory completeness claim is inherited through the
embedded PDL fragment and the cited alternating-machine/PDL results.

## Theorem 6.3.1 and exact proof boundary

Theorem 6.3.1 states that the following are equivalent for the fixed
aconjunctive positive-normal formula \(p_0\):

1. \(p_0\) is consistent in the deductive system;
2. the alternating tableau algorithm does not reject; and
3. \(p_0\) has a finite tree-like model of depth exponential in
   \(|p_0|^3\).

The source proves (1) ⇒ (2) by building a consistency-preserving subtree of
the tableau. At a disjunction it retains a consistent successor; at the
other rules it retains the required successors. Proposition 5.7(vi) handles
the least-fixed-point counter step. The proof then shows that neither a
propositional clash nor an overflowing \(\mu\)-counter can occur on the
selected subtree.

For (2) ⇒ (3), the source prunes rejecting processes and keeps one successful
disjunctive successor. From the surviving tree it constructs a model whose
states are modal-expansion nodes/leaves and whose program relations are the
labelled modal edges. It assigns ordinal approximants in \(L_{\mu+}\) to
active least-fixed-point formulas, forms closed sets \(\Theta_s\), and proves
the Boolean, modal, least-fixed-point, and greatest-fixed-point truth
conditions (6.3.16)–(6.3.21). Structural induction in (6.3.22) yields the
truth lemma and hence \(M,r_0\models p_0\). A cited tree-model technique gives
the stated finite tree-like depth bound.

The proof of (3) ⇒ (1), i.e. soundness of the deductive system, is explicitly
left to the reader on printed p. 353. Therefore the paper supplies a detailed
completeness/model-construction direction but not a printed line-by-line
soundness proof.

The theorem gives a depth bound, not a separately displayed exact state-count
bound. It must not be rewritten as a sharper modern small-model theorem.

## Proof-status inventory

| Item | Source status |
|---|---|
| semantic least/greatest fixed-point equations | defined/derived in §§2–3 |
| Proposition 3.2.3, closure characterization | proof printed |
| Lemma 3.3.3, transitivity of active dependence | proof printed |
| Definition 3.3.4, aconjunctivity | exact definition printed |
| Proposition 4.1, non-PDL definability | short proof printed |
| Proposition 4.2, even-state separation | statement attributed to [12]; proof absent |
| Proposition 5.7 | only item (vi) proved in detail; basic items referred/omitted |
| Lemmas 6.2.6–6.2.7, counter bound and termination | proofs printed |
| Theorem 6.3.1, consistency ⇒ algorithm ⇒ model | detailed proof printed |
| Theorem 6.3.1, model ⇒ consistency/soundness | explicitly left to reader |
| EXPTIME lower bound | not independently reconstructed in this paper; inherited/cited |

## What the source does not contain

- It does not prove the later full modal-μ-calculus completeness theorem.
- It does not give the later automata-on-trees equivalence.
- It does not define parity games or alternation-depth hierarchies.
- It does not give a modern local model-checking algorithm.
- It does not provide a worked end-to-end tableau run on a sample formula.
- It does not give a sharper explicit finite-state count than the
  Theorem 6.3.1 tree-depth statement.

Those topics belong to the Emerson–Jutla and Bradfield–Stirling presentations
or to later sources. They cannot be read backward into Kozen (1983).

## Reader-facing closure decision

The acquired scan is complete and the previously open visual-transcription
condition is discharged:

- exact grammar and semantics: closed;
- positive-normal and closure machinery: closed;
- exact active-variable and aconjunctive definitions: closed;
- membership/nonmembership examples: closed;
- expressiveness propositions and proof status: closed;
- deductive axioms and rule: closed;
- tableau rules, counter purpose, algorithm, and termination argument: closed;
- Theorem 6.3.1 statement and directional proof boundary: closed;
- source omissions and later-result boundary: closed.

No test, checker, TeX build, handbook PDF build, or visual handbook pass was
created or run. PDF rendering was used only to read the primary source.

## Exact Proposition 5.7 and induction-rule reconstruction (2026-09-06)

The equations below were checked directly against printed pp. 341--342
(physical PDF pages 5--6) of the
[Cornell primary scan](https://www.cs.cornell.edu/kozen/Papers/mu.pdf), using
the existing source-page images. The schematic notation is expanded here;
these are mathematical transcriptions and supplied derivations, not copied
source prose. No manuscript rendering or edits were performed.

### All six items

Write `p(t)` for capture-avoiding replacement of the designated free
variable of a formula context by `t`. Other free variables are parameters.
The fixed-point bodies must have the positivity required by the language;
`sigma` below ranges over `mu,nu`.

\[
\begin{array}{ll}
\text{(i)}&\mu X.pX=\mu Y.pY,\\
\text{(ii)}&pX\leq qX\ \Longrightarrow\
                 \sigma X.pX\leq\sigma X.qX,\\
\text{(iii)}&q\leq r\ \Longrightarrow\ p(q)\leq p(r),\\
\text{(iv)}&p(\sigma X.pX)=\sigma X.pX,\\
\text{(v)}&\mu X.q=q,\\
\text{(vi)}&p\bigl(\mu X.(q\land pX)\bigr)\leq q
                   \ \Longrightarrow\ \mu X.pX\leq q.
\end{array}
\]

The printed side conditions are: in (i), X and Y are free for Z in pZ;
in (iii), X is positive in pX; in (iv), the fixed-point formula is free
for X in pX; in (v), X is not free in q; in (vi), q is free for X in pX.
Items (ii) and (iv) use sigma, whereas (i), (v), and (vi) are printed with
mu. Formula well-formedness supplies positivity in every displayed binder.

For a parameter-explicit manuscript, implement (i) as genuine alpha-renaming:
\(\mu X.p=\mu Y.(p[X:=Y])\), with Y fresh for p and substitution
capture-avoiding. Do not rename a binder to the name of an unrelated free
parameter. In the proof of (vi) below, q is held fixed and X is chosen
outside FV(q); internal binders are renamed away from substitution
arguments. This makes explicit the independent-parameter reading needed
by the displayed algebra. Being free for substitution alone does not mean
that a formula contains no free X.

### What rule (5.6) means

The printed rule on p. 341 is
\[
 \frac{pY\leq Y}{\mu X.pX\leq Y},
 \qquad Y\text{ does not occur in }pX.
\]
Here Y is a fresh propositional variable, not a state and not a program;
pY replaces the designated X by Y. The rule acts on derivable inequalities,
where \(u\leq v\) abbreviates \(u\lor v=v\). It is not an object-language
implication evaluated at one state. Equational substitution instances give
the familiar form
\[
 \frac{p(b)\leq b}{\mu X.pX\leq b},
\]
with b independent of the bound X and all substitutions free for their
positions. Semantically, with all parameters fixed, p denotes a monotone
map \(F:\mathcal P(S)\to\mathcal P(S)\), the premise is the inclusion
\(F(B)\subseteq B\), and the conclusion is \(\mu F\subseteq B\).

The distinction from a local implication is necessary. Take states s,t,
an a-edge s to t, P true only at t, Y empty, and
\(pX=P\lor\langle a\rangle X\). At s the local formula
\(pY\to Y\) is true because pY is false. Nevertheless s satisfies
\(\mu X.pX\) and does not satisfy Y. Thus the local implication
\((pY\to Y)\to(\mu X.pX\to Y)\) is not an axiom supplied by (5.6).

### Complete algebraic proof of (vi)

Fix a positive formula context p and a parameter formula q with the hygiene
above. Set
\[
 A:=\mu X.(q\land pX),\qquad
 B:=\mu X.\bigl(q\land p(q\land X)\bigr),\qquad
 C:=q\land B.
\]
Assume \(p(A)\leq q\). The following supplies all comparisons in the
printed steps (a)--(g), including the intermediate comparison compressed
in step (b):

1. Boolean order gives \(q\land X\leq X\). By (iii),
   \(p(q\land X)\leq pX\), hence
   \(q\land p(q\land X)\leq q\land pX\).
   Item (ii) therefore gives \(B\leq A\).
2. Consequently \(C\leq B\leq A\), so (iii) and the premise give
   \(p(C)\leq p(A)\leq q\). This is the printed step (b).
3. Thus \(p(C)\leq q\land p(C)\) by Boolean order, the printed (c).
4. Axiom (5.5), applied to the body defining B, gives
   \(q\land p(q\land B)\leq B\), or
   \(q\land p(C)\leq B\). Combining with step 3 gives
   \(p(C)\leq B\), the printed (d).
5. Steps 2 and 4 give \(p(C)\leq q\land B=C\), the printed (e).
6. Rule (5.6), with C as the candidate pre-fixed formula, gives
   \(\mu X.pX\leq C\), the printed (f).
7. Since \(C\leq q\), conclude \(\mu X.pX\leq q\), the printed (g).

The source prints (a)--(d) at the bottom of p. 341 and (e)--(g) at the
top of p. 342. The auxiliary letters A,B,C above are local abbreviations;
in the proof they denote formulas, and under a fixed model/valuation their
denotations are subsets of the same state set S.

Once item (iv) is available, a shorter correct proof is possible:
\(A=q\land p(A)\); the premise \(p(A)\leq q\) yields
\(p(A)=q\land p(A)=A\); induction gives
\(\mu X.pX\leq A\leq q\). The longer argument above records the
source's own algebraic route with its suppressed comparison made explicit.

### Consistency consequence used on p. 342

With the same hygiene, if \(q\land\mu X.pX\) is consistent, then
\[
 q\land p\bigl(\mu X.(\neg q\land pX)\bigr)
\]
is consistent. For if this formula were derivably zero, Boolean algebra
would give \(p(\mu X.(\neg q\land pX))\leq\neg q\).
Apply (vi) with parameter \(\neg q\) to derive
\(\mu X.pX\leq\neg q\), contradicting the assumed consistency.
This is a proof-theoretic contrapositive, not an appeal to completeness
to infer satisfiability from consistency.

## Figure 2 and raw tableau labels: bounded recheck (2026-09-06)

Primary locators: Proposition 4.2 and Figure 2 are on printed p. 340
(physical PDF page 5); Section 6.1 begins on printed p. 342 and continues
on p. 343 (physical page 6). These pages were read directly from the
existing images of the [Cornell source scan](https://www.cs.cornell.edu/kozen/Papers/mu.pdf).

### The depicted frame and its fixed point

Number Figure 2's unlabeled dots from left to right by
\(S=\{0,1,2,\ldots\}\). The displayed a-edges give
\[
 R_a=\{(n+1,n):n\geq0\}
       \cup\{(2k+3,2k+1):k\geq0\}.
\]
The straight arrows descend by one; the curved arrows descend from an
odd state at least 3 to the preceding odd state. No self-loops are drawn,
and 0 has no successor. Numerical names are our explicit indexing of the
unlabeled diagram. No extra transitions, including a loop at 0, should be
inserted to make the frame total.

Here is a complete supplied proof of the mu-formula part of Proposition 4.2.
For \(F(B)=[a]\langle a\rangle B\), set
\[
 E_0=\varnothing,\qquad E_j=\{0,2,\ldots,2j-2\}\quad(j\geq1).
\]
Then \(F(E_j)=E_{j+1}\):

- State 0 satisfies the outer box vacuously.
- An even state \(2r\geq2\) has only successor \(2r-1\). That odd
  successor has the even successor \(2r-2\), and its only possible
  additional successor is odd. It therefore has an E_j-successor exactly
  when \(r\leq j\).
- An odd state \(2r+1\) has the even successor \(2r\). For r=0 this
  successor is dead; for r>0 its only successor is odd. In either case it
  has no E_j-successor, so the outer box fails.

The same calculation shows that the set E of all even states is fixed.
Every pre-fixed set contains E_0 and, inductively, every E_j. Hence it
contains E, proving
\[
 \llbracket\mu X.[a]\langle a\rangle X\rrbracket=E.
\]

### Proposition interpretations and the PDL claim

The drawing and adjacent proposition do not print interpretations for
ordinary proposition constants or other program constants. The mandatory
Boolean constants retain \(I(0)=\varnothing\), \(I(1)=S\). A fully
specified working model can restrict the signature to a and those Boolean
constants, or explicitly interpret every additional ordinary proposition
and unused primitive program by the empty set. This is an explicit model
completion, not additional literal valuation data recovered from the scan.
Converse in PDL means the inverse of the displayed program relation.

Proposition 4.2 asserts that its mu-formula defines the even states while
PDL formulas, including tests and reverse, define only finite or cofinite
sets in that model. This cannot mean arbitrary proposition valuations on
the bare frame: assigning a primitive proposition the even set immediately
contradicts such a reading. The proposition is attributed to reference
[12], identified on printed p. 354 as Kozen's unpublished manuscript
*On the expressiveness of mu*.

The calculation above proves the mu side, not the PDL finite/cofinite
side. A complete proof of the latter must handle regular iteration with
nested tests and converse; finite modal-depth indistinguishability alone
does not do so. No such complete argument was established in this bounded
pass, and no proof is printed with Proposition 4.2. Thus the source claim
and the proved fixed-point calculation must not be presented as a newly
completed proof of the entire single-model separation.

### Correction to the earlier tableau-vocabulary paragraph

Section 6.1 explicitly assigns Gamma_s a set of raw subformulas of p_0,
not a set of closed CL(p_0) formulas. Its binder rule replaces sigma X.pX
by the raw body pX; its variable rule replaces X by that same body.
Neither operation performs closing substitution at this stage. This
supersedes the earlier sentence in this note calling Gamma_s a set of
closure formulas. The finite closed closure CL and the raw subformula
labels are distinct objects; closing maps and later semantic formula
sets must be applied explicitly when needed.

## Exact closure, active lists, counter equations, and supplied termination proof (2026-09-06)

This bounded addition records equations checked in the primary scan on
printed pp. 336--338 and 343--346, physical PDF pages 3--4 and 6--8.
Source: [Kozen's Cornell PDF](https://www.cs.cornell.edu/kozen/Papers/mu.pdf),
retrieved 2026-09-06; local copy
`tmp/pdfs/p09-kozen-1983/kozen-mu-1983.pdf`. The existing primary-page images
were inspected at original size. No OCR inequality was adopted. Mathematical
transcriptions are separated from the supplied derivations and cautions;
this section does not reproduce the article's prose or establish acceptance
of the entire presentation.

### Source equations: ordered closing substitution, pp. 336--337

Kozen's order has the following orientation:
\[
 p\leq q\ \Longleftrightarrow\ q\in\operatorname{Sub}(p),
 \qquad
 p<q\ \Longleftrightarrow\ q\in\operatorname{Sub}(p)\setminus\{p\}.
\]
Thus the left member is the containing formula. For a raw subformula p,
Definition 3.2.1 gives the ordered enclosing-binder list
\[
 V_p=(Y_1,\ldots,Y_n),\qquad
 \sigma Y_1<\cdots<\sigma Y_n<p.
\]
It contains all enclosing variables, not just free or active ones. For an
ordered subsequence \(\bar X=(X_1,\ldots,X_k)\) and arguments
\(\bar q=(q_1,\ldots,q_k)\), the displayed substitution convention is
\[
 p[\bar X/\bar q]
   =p[X_k/q_k][X_{k-1}/q_{k-1}]\cdots[X_1/q_1].
\]
Here \(p[X/q]\) replaces free X by q: the source puts the variable before
the slash. This is sequential substitution, starting with the innermost
listed binder, not simultaneous substitution. An empty list acts identically.
Definition 3.2.2 gives
\[
 \sigma V_p=(\sigma Y_1,\ldots,\sigma Y_n),\qquad
 e(p)=p[V_p/\sigma V_p],\qquad
 \operatorname{CL}(p_0)=\{e(p):p_0\leq p\}.
\]
The seven closure conditions of Proposition 3.2.3 are, for a set D of closed
formulas,
\[
\begin{array}{rll}
 (i)&p_0\in D,\\
 (ii)&\neg P\in D&\Longrightarrow P\in D,\\
 (iii)&p\lor q\in D&\Longrightarrow p,q\in D,\\
 (iv)&p\land q\in D&\Longrightarrow p,q\in D,\\
 (v)&\langle a\rangle p\in D&\Longrightarrow p\in D,\\
 (vi)&[a]p\in D&\Longrightarrow p\in D,\\
 (vii)&\sigma X.pX\in D&\Longrightarrow p(\sigma X.pX)\in D.
\end{array}
\]
Its proof displays the identities
\[
\begin{aligned}
 e(p)&=p &&(p\text{ closed}),\\
 e(p\lor q)&=e(p)\lor e(q),&
 e(p\land q)&=e(p)\land e(q),\\
 e(\langle a\rangle p)&=\langle a\rangle e(p),&
 e([a]p)&=[a]e(p),\\
 e(X)&=e(\sigma X.p)
       =\sigma X.\bigl(p[V_{\sigma X}/\sigma V_{\sigma X}]\bigr).
\end{aligned}
\]

### Supplied closure proof details

The last identity requires no simultaneous-substitution convention. On a
variable occurrence X, the binders between \(\sigma X\) and that occurrence
do not change the raw variable; substituting X inserts \(\sigma X\), and
the remaining outer substitutions close its parameters. On the binder
itself, exactly those outer substitutions act, giving the same result.

Every free variable in p has an enclosing binder. Substituting an inner
binder can introduce only variables bound farther outside it. The
inner-to-outer order subsequently replaces them, so e(p) is closed. There
is one image per raw subformula, hence
\(|\operatorname{CL}(p_0)|\leq|\operatorname{Sub}(p_0)|\leq|p_0|\).

For \(b=\sigma X.u\), put \(S=[V_b/\sigma V_b]\). The raw body has the
additional last enclosing variable X, so
\[
 e(u)=u[X/b]S=(uS)[X/e(b)].
\]
This is exactly the one-step unfolding of \(e(b)=\sigma X.(uS)\).
All substitutions are free for their positions after the usual renaming.
The Boolean and modal identities above, this identity, and
\(e(X)=e(\sigma X)\) prove that the image set obeys (i)--(vii).
For leastness, let D obey those conditions and descend the raw syntax tree
from p0. The closed image of each Boolean/modal child is obtained by the
corresponding component rule. The image of a binder body is obtained by
(vii) and the displayed body identity. A variable is a leaf, and a negated
constant uses (ii). Thus every e(p) belongs to D. This supplies the
minimality argument without relying on the printed claim that each closed
binder has exactly two preimages, which needs qualification for vacuous
binders whose bound variable never occurs.

### Source equations: activity and active-list order, pp. 337--338

For Y and p, let \(W_{Y,p}\) be the subsequence of \(V_p\) consisting of
the variables Z satisfying \(\sigma Y<\sigma Z<p\). Definition 3.3.1 is
\[
 Y\in A_p\ \Longleftrightarrow\
 \sigma Y<p\ \text{ and }\
 Y\in\operatorname{FV}\bigl(p[W_{Y,p}/\sigma W_{Y,p}]\bigr).
\]
The ordered list \(A_p\) is a subsequence of \(V_p\);
\(A_{\mu p}\) and \(A_{\nu p}\) retain respectively its mu- and nu-variables.
All three orders are outer-to-inner. In particular
\[
 A_X=A_{\sigma X}\mathbin{\cdot}(X),
\]
where the dot appends an entry to an ordered list, and X is a raw variable
occurrence bound by \(\sigma X\).

The substitution identity used in Lemma 3.3.3 is as follows. Choose the
complete intervening lists \(\bar X,\bar Y\) so that
\[
 \sigma X<\sigma X_1<\cdots<\sigma X_m<\sigma Y
       <\sigma Y_1<\cdots<\sigma Y_n<p.
\]
Then
\[
\begin{split}
 &p[\bar Y/\sigma\bar Y]
     [Y/\sigma Y[\bar X/\sigma\bar X]]
     [\bar X/\sigma\bar X]\\
 &\hspace{12mm}=
 p[\bar Y/\sigma\bar Y][Y/\sigma Y]
     [\bar X/\sigma\bar X].
\end{split}
\]
Under \(Y\in A_p\) and \(X\in A_{\sigma Y}\), the first factor has a
free Y, and the replacement for that Y has a free X. The remaining
substitutions do not bind or replace X. The displayed equality therefore
exhibits a free X after all binders strictly between \(\sigma X\) and p
have been substituted. Hence \(X\in A_p\), proving Lemma 3.3.3.

An accompanying prefix fact makes the counter proof explicit. If X is
active in p, the portion of \(A_p\) through X is exactly \(A_X\).
For an enclosing Y outside X, activity in \(\sigma X\) implies activity
in p by Lemma 3.3.3. Conversely, any free Y exposed below \(\sigma X\)
comes either from that binder's body or from an intervening binder inserted
into it, so the same outside substitutions expose Y in \(\sigma X\).
Consequently a retained X-counter retains every earlier local counter in
that prefix. Newly opened binders can only append counters after it.

### Source counter assignments (6.1.6)--(6.1.13), pp. 343--344

These assignments concern \(\Gamma_s\subseteq\operatorname{Sub}(p_0)\),
not closed CL-formulas. A counter c is an identity carrying an immutable
variable \(X(c)\); \(c(s)\) is its value at node s. Distinct counters may
have the same variable. For \(A_p=(X_1,\ldots,X_k)\),
\[
 C(s,p)=(c_1,\ldots,c_k),\qquad X(c_i)=X_i.
\]
Write \(C_\mu,C_\nu\) for the corresponding subsequences. With
\(m=|p_0|\) and \(N=2^m\), mu-values before rejection lie in
\(\{0,\ldots,N\}\); nu-values lie in \(\{0,1\}\).
A completed configuration rejects if a live mu-counter exceeds N.
No separate pre-collision overflow check is stated in the source;
the operational timing is clarified below. The global list is a shuffle
\[
 G(s)\in\operatorname{Shuffle}
        \bigl(C_\mu(s,p):p\in\Gamma_s\bigr),
 \qquad C(r_0,p_0)=G(r_0)=().
\]
It preserves each local mu-order. Its leftmost entry has highest priority.
For compactness below, \(L\upharpoonright A\) means the order-preserving
sublist whose counters have variables in A; every formula-rule assignment
is provisional until collisions are resolved.

1. **(6.1.6), binder \(\sigma X.u\) to raw body u.** If X is free in u,
   create a new c with \(X(c)=X\), \(c(t)=0\), and set
   \[
    C(t,u)=C(s,\sigma X.u)\mathbin{\cdot}(c).
   \]
   If X is mu, also set \(G(t)=G(s)\mathbin{\cdot}(c)\). A new nu-counter
   is not appended to G. If X is not free in u, create nothing and use
   \(C(t,u)=C(s,\sigma X.u)\), \(G(t)=G(s)\).

2. **(6.1.7), disjunction.** On the p-successor of \(p\lor q\),
   \[
    C(t,p)=C(s,p\lor q)\upharpoonright A_p;
   \]
   on the q-successor use the analogous restriction to \(A_q\).
   Delete from that successor's G every mu-counter removed by this
   restriction. Surviving counter values are inherited before the
   priority-deletion reset in (6.1.13).

3. **(6.1.8), conjunction.** At the single successor,
   \[
    C(t,p)=C(s,p\land q)\upharpoonright A_p,
    \qquad
    C(t,q)=C(s,p\land q)\upharpoonright A_q.
   \]
   Before collisions, G is unchanged. Aconjunctivity makes the two mu
   subsequences disjoint and together exhaust the old mu subsequence.
   A nu-counter can be inherited by both lists. Therefore the unrestricted
   assertion on p. 343 that all lists are disjoint cannot be retained as a
   literal invariant alongside (6.1.8); the disjointness actually required
   by G is mu-counter disjointness. No replacement of this convention by
   fresh, independently valued nu-copies is established here.

4. **(6.1.9), raw variable X to u, where \(\sigma X=\sigma X.u\).**
   \[
    C(t,u)=C(s,X),\qquad c(t)=c(s)+1,
    \quad X(c)=X.
   \]
   This c is the last counter on the local list. For mu-X, reset every
   mu-counter to its right in G to zero. On every local successor list,
   reset a nu-counter to zero whenever some mu-counter to its left on that
   same list was incremented or reset. For nu-X, the algorithm permits
   this rule only when \(c(s)=0\); the assignment makes it 1.

5. **(6.1.10), modal successor for \(\langle b\rangle p\).** If its
   raw label is \(\{p,q_1,\ldots,q_n\}\), with all relevant
   \([b]q_i\in\Gamma_s\), set
   \[
    C(t,p)=C(s,\langle b\rangle p),\qquad
    C(t,q_i)=C(s,[b]q_i)\quad(1\leq i\leq n).
   \]
   Restrict G to the counters occurring in these inherited lists. Reset
   every surviving nu-counter to zero. Each diamond demand has its own
   successor; all boxes with the same program contribute to that successor.

6. **(6.1.11), untouched formulas.** If a nonmodal rule acts on
   \(q\ne p\), and \(p\in\Gamma_s\), then
   \[
    C(t,p)=C(s,p).
   \]
   This is inheritance, not an exemption from the global or dependent
   resets prescribed by (6.1.9) and (6.1.13).

7. **(6.1.12), duplicate-formula collision.** Multiple provisional lists
   for the same raw formula have the same variable sequence. If they have
   mu-entries, keep the list whose first mu-entry occurs earlier in G and
   discard the other list, including its mu-identities from G. There is
   no componentwise numerical maximum in this case. If the lists have
   no mu-entries, say \(C=(c_1,\ldots,c_k)\) and
   \(C'=(c'_1,\ldots,c'_k)\), retain C and assign
   \[
    c_i(t)=\max\{c_i(t),c'_i(t)\}\quad(1\leq i\leq k).
   \]
   The source writes \(C'\longrightarrow C\) for discarded-to-retained
   lists and \(c'\longrightarrow c\) for their entries with
   \(X(c')=X(c)\). Thus an arrow can connect distinct identities with
   different values; it is not equality of identities or of values.

8. **(6.1.13), deletion-priority and dependent-flag resets.** If deleting
   a higher-priority mu-counter changes a surviving mu-counter's position
   in G, reset the survivor to zero. Every increment or reset of a
   mu-counter also resets all nu-counters lying after it on the same local
   list. These apply to deletions from branch restriction, modal restriction,
   and collision disposal. New counters are appended at the end of G;
   deletions preserve the relative order of the survivors.

The false-0 rejection and normalization of negated Boolean constants in
the current manuscript remain necessary explicit corrections; the printed
clash-only wording is not a reason to remove them. The nu-zero guard above
also remains essential. This section does not change any manuscript rule.

### Source counter-chain definition and displayed estimates, pp. 345--346

Definition 6.2.5 allows distinct successive identities. Along a path choose
\[
 s=s_1,t_1,s_2,t_2,\ldots,s_n,t_n=t,
 \qquad s_{i+1}\text{ immediately succeeds }t_i,
\]
and \(c=c_1,\ldots,c_n\), where \(c_i\) exists on \([s_i,t_i]\)
and \(c_i\longrightarrow c_{i+1}\) at \(t_i\). Let \(a_i\) count
increments of \(c_i\) on that interval. The displayed definition is
\[
 a(c,s,t)=\sum_{1\leq i\leq n}a_i.
\]
In particular this is not just the number of increments of the original
surviving object c. The source expressly follows collision replacements.

With \(K=\max_s|G(s)|\leq m^2\), Lemma 6.2.6 prints
\[
 a(c,s,t)\leq m^4 2^{m^3}
\]
when either c is a mu-counter, or c is a nu-counter and no modal rule
occurs on \([s,t]\). Its mu-case proof displays
\[
 a(c,s,t)\leq K^2N^K\leq m^4 2^{m^3},\qquad N=2^m.
\]
The literal exponential is \(2^{m^3}\), not \(2^{m}\) or
\(2^{m^2}\). These are the source's exact displayed estimates, not
independently certified sharp constants.

### Supplied mu-counter counting with an explicit safe radix

The following supplies the finite mu-counter argument while avoiding an
off-by-one shortcut in the printed odometer estimate. A digit ranging
from 0 through N has N+1 values, so use radix N+1.

Fix one mu-counter identity c during its lifetime. Births occur to its
right in G. Its rank can therefore only decrease as earlier counters are
deleted, at most K-1 times. Split its lifetime into at most K intervals
of constant rank. On such an interval the prefix of G ending at c has
fixed identities. Every increment of a prefix counter strictly increases
the lexicographic vector of prefix values; all lower-priority entries are
reset, and no deletion before c occurs within the interval. All values
are in \(\{0,\ldots,N\}\) before rejection. There are at most
\((N+1)^K\) vectors. Every reset of c within the interval accompanies
one of these strict increases. Boundary priority changes add at most K
events. Thus a safe lifetime bound for increments and resets is
\[
 K\bigl((N+1)^K+1\bigr)+1,
\]
including a possible last rejecting increment.

For a collision chain of mu-counters, choose the first mu-counter d on
the same local list as c. The active-prefix fact keeps d with c until a
collision. Each collision replaces d by a globally earlier first
mu-counter. A retained d never moves right, and new identities cannot be
inserted before it. Consequently there are at most K identities in this
replacement chain. Multiplying the lifetime estimate gives the safe bound
\[
 a(c,s,t)\leq
 K\left(K\bigl((N+1)^K+1\bigr)+1\right)
   =2^{O(m^3)}.
\]
This is a supplied coarser bound, not a claim that the printed
\(K^2N^K\) estimate has been proved with its exact constant. For the
termination proof below, finiteness of each mu-identity's increments and
resets is sufficient.

### Bounded check of the nu-case auxiliary assertion

The last paragraph of the printed nu-case proof on p. 346 asserts
\(a(c,s,t)\leq1\) when no mu-variable is active in \(X(c)\), provided
there is no modal step. Under the displayed collision-chain definition,
the following supplied trace gives two increments. This checks only that
auxiliary assertion; it does not contradict the much larger displayed
bound of Lemma 6.2.6 or the main theorem.

Let
\[
 B=\nu X.\mu Y.(X\lor Y),\qquad p_0=\nu Z.(B\land Z).
\]
The input is closed, positive-normal, and aconjunctive: the only
conjunction is \(B\land Z\), and Y is active in neither conjunct.
For the raw X, \(A_X=(X)\), so no mu-variable is active in X. For the
raw Y, \(A_Y=(X,Y)\). Use lower-case letters for counter identities.
All steps below are nonmodal and satisfy the nu-zero guard.

1. Open Z, split its conjunction, open B, open Y, and choose the
   Y-disjunct. This gives
   \[
    \Gamma=\{Y,Z\},\quad C(Y)=(x_0,y_0),\quad C(Z)=(z_0),
    \quad G=(y),
   \]
   where subscripts are values, not identity indices.
2. Unfold the raw Z once, changing z from 0 to 1, and split the
   conjunction. The label becomes \(\{Y,B,Z\}\).
3. Open this new B with new nu-counter x' at 0; open its mu-Y with
   new counter y' at 0. Choose the X-disjunct, deleting y'. The label
   is \(\{Y,X,Z\}\), with \(C(X)=(x'_0)\) and \(G=(y)\).
4. Unfold this X: x' changes from 0 to 1. Open the resulting
   \(\mu Y.(X\lor Y)\), creating y'' at 0. Now
   \[
    \Gamma=\{Y,X\lor Y,Z\},\quad
    C(Y)=(x_0,y_0),\quad C(X\lor Y)=(x'_1,y''_0),
    \quad G=(y,y'').
   \]
5. Unfold the older raw Y. It proposes another list
   \((x_0,y_1)\) for \(X\lor Y\). The increment of y resets y''
   but does not reset x or x', which lie to the left of their mu-counters
   on the local lists. Collision (6.1.12) keeps \((x_0,y_1)\), because
   y precedes y'' in G, and discards \((x'_1,y''_0)\). In the exact
   source notation this gives \(x'\longrightarrow x\). The componentwise
   maximum rule does not apply, since these lists contain mu-counters.
6. Choose the X-disjunct, deleting y, and unfold X. The retained x changes
   from 0 to 1. Along the permitted chain \(x'\longrightarrow x\),
   one increment occurred before the collision and one afterward:
   \[
    a(x',s,t)=2.
   \]

The surviving identity x was not reset by the collision. Rather, the
chain moved from distinct identity x', already valued 1, to x, still
valued 0. This is why identifying a collision chain with one monotone
flag's lifetime would be incorrect. No claim that the uniform nu-counter
bound has been independently repaired is made here.

### Supplied termination proof avoiding that auxiliary assertion

This proves the finite nonmodal-saturation conclusion of Lemma 6.2.7
using the mu lifetime bound above and the literal counter assignments.
It is not a reproduction of the printed proof.

Suppose a path continues forever using only Boolean, binder, and raw
variable rules, without rejecting or reaching the modal/accepting action.
Every rule except a raw variable rule strictly reduces the sum of the
sizes of the raw formulas in the label. Therefore some variable is unfolded
infinitely often. Choose such an X whose binding formula is outermost:
no Y with \(\sigma Y<\sigma X\) is unfolded infinitely often.

Only a raw variable rule for such a proper enclosing Y can replenish
occurrences of the raw binder \(\sigma X\). To see this without an
implicit fairness assumption, count occurrences of \(\sigma X\) inside
the raw formulas in a label. Decomposition never increases this count;
opening \(\sigma X\) reduces it. Unfolding X or a variable bound inside
\(\sigma X\) inserts a body that does not contain \(\sigma X\), so
cannot increase it. The only possible increasing steps unfold a proper
enclosing variable, and there are finitely many such steps by the choice
of X. Hence only finitely many \(\sigma X\)-rules occur, and only
finitely many counter identities associated with X are created.

If X is mu, each such identity is incremented only finitely often by the
mu lifetime argument. Collisions merely select an already existing identity;
aconjunctivity never duplicates a mu-identity. Infinitely many X-unfoldings
are impossible.

If X is nu, every mu-counter before an X-counter on its local list belongs
to a proper enclosing variable. By the same binder-occurrence argument,
each of those enclosing variables has only finitely many counter births:
all variables enclosing it also enclose X and have finitely many unfolding
steps. There are finitely many enclosing variables, so only finitely many
such preceding mu-identities can occur. Each has finitely many increments
and resets by the mu lifetime argument. Consequently (6.1.9)/(6.1.13)
cause only finitely many resets of X-counters. Modal resets do not occur
on this path. A collision does not decrease the value of a retained
nu-identity: it either keeps the selected list's values or takes maxima
in the nu-only case. Since there are finitely many X-counter identities,
and the zero guard permits at most one increment between resets of each
identity, there can be only finitely many X-unfoldings. Sharing a nu-identity
between two conjunction lists creates no new identity or new zero value.
This again contradicts the choice of X.

Thus an infinite nonmodal segment is impossible: after finitely many
steps the process rejects, takes the modal action, or accepts. The proof
does not assert that an arbitrary unbounded sequence of modal actions is
a finite tableau branch. Nor does it replace the separate alternating-space
simulation or the theorem's model-construction proof.

### Scope of this addition

The ordered substitutions, active-list order, all eight counter updates,
collision direction, and printed exponents are now equation-pinned.
The supplied closure proof and finite nonmodal-saturation proof are
explicit. The exact published uniform nu-counter-chain bound remains a
source statement, not a newly completed proof: its last auxiliary
one-increment assertion cannot be used as written under Definition 6.2.5.
No manuscript file, checker, test, build, or manuscript render was changed
or run in this bounded retrieval pass.

### Follow-up: nonrejection is not global tableau halting

Rechecked printed pp. 345--350 and the references on p. 353 against the
primary images on 2026-09-06. The decisive source sentence on p. 345 is:

> Despite the possibility of infinite computations, this alternating algorithm can be simulated in deterministic exponential time [3].

The four actions (6.2.1)--(6.2.4) have these mathematical conditions:
\[
\begin{array}{rl}
 (6.2.1)&\{P,\neg P\}\subseteq\Gamma_s
                 \quad\Longrightarrow\quad\text{halt/reject},\\
 (6.2.2)&\exists c\in G(s):c(s)>2^{|p_0|}
                 \quad\Longrightarrow\quad\text{halt/reject},\\
 (6.2.3)&\text{only the modal rule is applicable, no preceding rejection}
                 \quad\Longrightarrow\quad\text{apply the modal rule},\\
 (6.2.4)&\text{no rule is applicable, no preceding condition}
                 \quad\Longrightarrow\quad\text{halt/accept}.
\end{array}
\]
Action (6.2.3) is a continuation, not a halt. Theorem 6.3.1(ii), p. 347,
uses the exact outcome phrase "the algorithm does not reject". On p. 349,
rejection propagates from a rejecting successor at a universal node, or
from both rejecting successors at an existential node. Its (ii)-to-(iii)
proof removes rejecting processes, keeps one disjunctive successor, and
retains the root. Page 350 uses Lemma 6.2.7 to find the next modal node or
leaf after a modal edge, not to prove that there are finitely many such
edges on a branch.

Supplied direct check: take \(p_0=\nu X.\langle a\rangle X\). After
opening the binder there is one nu-counter x and no mu-counter:
\[
 (\{\langle a\rangle X\},x=0)
 \xrightarrow{\langle\rangle}
 (\{X\},x=0)
 \xrightarrow{X}
 (\{\langle a\rangle X\},x=1)
 \xrightarrow{\langle\rangle}
 (\{X\},x=0).
\]
The final two configurations recur indefinitely. Every modal step resets
x to zero by (6.1.10), making the next X-step legal. There is no clash,
no mu-overflow, and no irreducible label. Thus the raw process never
executes halt/accept or halt/reject. Nevertheless the theorem's
nonrejection condition holds; semantically, a one-state a-loop satisfies
the formula. This explicitly separates nonrejection from halting acceptance.

No repeated-configuration stopping rule appears in (6.2.1)--(6.2.4), and
no such rule is supplied by their surrounding algorithm description.
The simulation is referred to [3], identified on p. 353 as Chandra,
Kozen, and Stockmeyer, *Alternation*, JACM 28(1) (1981), 114--133; that
reference was not independently inspected in this follow-up. A safety or
greatest-fixed-point characterization of nonrejection, and a finite
configuration-graph implementation, would be supplied explanations rather
than additional literal tableau rules from this article. In particular,
Lemma 6.2.7 must not be described as global halting of the tableau.

### Completed-configuration and collision convention

A further direct reading of pp. 344--345 found no stated rejection
microstep between a provisional increment and collision resolution.
The manuscript resolves structural assignments, collisions, and
dependent resets before applying the live-counter overflow check at
the successor configuration. This is an explicit operational
clarification consistent with the node-configuration presentation,
not a quoted additional sequencing rule.

For the finite configuration-graph simulation, the manuscript also fixes
an identity-renaming-invariant ordering of provisional-list origins,
collision groups, and nu-only survivors. This matters with shared flags:
different surviving identities can change sharing elsewhere, not merely
rename a configuration. Mu-containing collisions still use the stated
global-priority comparison.

The individual-counter result bounds increment/reset events, not the
duration of an identity's existence. A mu-identity may persist forever
through modal actions with no increments. An independent mathematical
reader identified both this heading overclaim and the missing collision
tie-break; they were corrected and the specific repairs rechecked.
The same reader checked finite nonmodal saturation, the finite-state
safety characterization of nonrejection, and the resulting exponential
nonmodal-segment bound. No whole model-construction theorem or topic
acceptance is asserted by that bounded review.

## Theorem 6.3.1: equation dossier and supplied model reconstruction (2026-09-06)

This is one bounded addition, based on direct inspection of the existing
primary images for printed pp. 347--354 (PDF pages 8--12), retrieved again
from [the Cornell primary scan](https://www.cs.cornell.edu/kozen/Papers/mu.pdf)
on 2026-09-06. The displays labelled with source equation numbers below
transcribe mathematical content; the intervening derivations are supplied
arguments, not quotations of Kozen's prose. The exact remaining
source-identification obligation concerning the adjective `tree-like` is
recorded at the end. Nothing here is whole-topic acceptance.

### Retrieved mathematical content: consistency annotations, pp. 347--349

The standing input is a closed, aconjunctive, positive-normal formula p0,
with uniquely named bound variables. Labels Gamma_s contain raw subformulas.
The ordered substitution convention and active lists are those recovered
above, not simultaneous substitution. For p in Gamma_s, write
V_p = (X_1,...,X_n). For X_i in A_{mu p}, let c_i be its counter and write
sigma X_i = mu X_i.qX_i. The source's modified closing substitution is
\[
 q_i=\mu X_i.(r(s,c_i)\land qX_i),\qquad
 e'(s,p)=p[\bar X/\bar q],
\]
with q_i = sigma X_i for X_i not in A_{mu p}. Every r(s,c) is closed,
and e'(s,p) <= e(p). Put
\[
 \Delta_s=\{e'(s,p):p\in\Gamma_s\}.
\]
The source initializes a new mu-counter with r(s+,c)=true in (6.3.3),
inherits r for existing counters in (6.3.2)/(6.3.4), and, when a raw
mu-variable X with counter c is expanded, gives
\[
\begin{array}{rll}
 (6.3.5)&r(s+,d)=true&d\text{ has lower priority than }c,\\
 (6.3.6)&r(s+,d)=r(s,d)&d\text{ has higher priority than }c,\\
 (6.3.7)&r(s+,c)=r(s,c)\land\neg\bigwedge\Delta'_s,&
\end{array}
\]
where
\[
 \Delta'_s=\{e'(s+,p):p\in\Gamma_s,\ p\ne X\}.
\]
The annotation of c is defined last: c belongs only to the list of X,
so Delta'_s is determined without its new annotation. This uses
mu-counter disjointness, not disjointness of all nu-counter lists.
The source also displays
\[
 r(s,c)=\neg\bigwedge\Delta'_{s_0}\land\cdots\land
             \neg\bigwedge\Delta'_{s_{c(s)-1}},
\]
where the s_i are the most recent ancestors at the indicated counter
values and an empty conjunction is 1.

For a root-containing selected set B of tableau nodes, the source's
conditions are
\[
\begin{array}{rl}
 (6.3.8)&s\in B,\ s\text{ a disjunction node}
                 \ \Longrightarrow\ \text{at least one successor lies in }B,\\
 (6.3.9)&s\in B,\ s\text{ any other node}
                 \ \Longrightarrow\ \text{every successor lies in }B,\\
 (6.3.10)&s\in B\ \Longrightarrow\ \Delta_s\text{ is consistent}.
\end{array}
\]
At the nontrivial mu-variable step the displayed formulas are
\[
\begin{array}{rl}
 (6.3.11)&\displaystyle
 \bigwedge\Delta_s\leq\bigwedge\Delta'_s\land e'(s,X),\\[2mm]
 (6.3.12)&\displaystyle
 \Delta'_s\cup\{e'(s,X)\}
   =\Delta'_s\cup\{\mu X.(r(s,c)\land p'X)\},\\[2mm]
 (6.3.13)&\displaystyle
 \Delta'_s\cup
 \{p'(\mu X.(r(s,c)\land\neg\bigwedge\Delta'_s\land p'X))\}.
\end{array}
\]
Both sets in (6.3.12)/(6.3.13) are asserted consistent. The subsequent
display identifies (6.3.13) with
\[
 \Delta'_s\cup\{p'(\mu X.(r(s+,c)\land p'X))\}
   =\Delta'_s\cup\{e'(s+,pX)\}=\Delta_{s+}.
\]
In the overflow argument, u and v are two repeated-label predecessors
at which the same surviving c is incremented, without any intervening
reset of c. The displayed equations are
\[
\begin{array}{rl}
 (6.3.14)&\Delta'_u=\Delta'_v,\\[1mm]
 (6.3.15)&\displaystyle
 \bigwedge\Delta_v\leq r(v,c)
       \leq\neg\bigwedge\Delta'_u
       =\neg\bigwedge\Delta'_v.
\end{array}
\]
The companion inequality is
\[
 \bigwedge\Delta_v\leq\bigwedge\Delta'_v.
\]

### Provisional consistency argument, including reset bookkeeping

The global overflow conclusion of this argument is not established.
See the correction section below: local annotation staging can be repaired,
but the claimed repeated-label correspondence across modal edges still
requires a new proof. The separately checked nonrejection-to-model
construction does not depend on this provisional argument.

The numerical deletion resets in (6.1.13) are not explicitly mirrored in
the source's list (6.3.2)--(6.3.7). To make the displayed history formula
and the completed-configuration convention agree, use the following
annotation convention in a reconstruction: whenever a surviving
mu-counter is reset to zero, reset its auxiliary r to 1; when a collision
discards a list, discard its auxiliary annotations with it. These are
proof annotations, not additional algorithmic counters or rules.
Resetting an r to 1 weakens the affected mu-body and therefore weakens
every enclosing positive formula. It cannot destroy consistency. The
nontrivial update (6.3.7) is evaluated before any additional deletion
reset that subsequently weakens it. The formula r(s,c) then contains
exactly the constraints acquired since the last reset of c.

Here are the rule cases in the construction of B.

1. At the root, the substitution list is empty, so
   Delta_{r0}={p0}, consistent by hypothesis. Positivity and fixed-point
   monotonicity give e'(s,p) <= e(p) at every node: replacing a mu-body
   F(X) by r and F(X) makes its least fixed point smaller, and the
   ordered outside substitutions preserve that comparison.

2. At a disjunction p or q, if a pre-existing copy of p has higher
   list priority, its annotations are retained; the new disjunctive
   obligation can be discarded because p is already present. All
   surviving other annotations are unchanged or weakened by resets,
   so conjunction Delta_s <= conjunction Delta_t for that successor t.
   The q-case is identical with its q-successor. Otherwise, transfer
   the relevant counter sublists to both candidates. The Boolean
   identity for e' and annotation weakening give
   \[
    \bigwedge\Delta_s\leq
      \bigwedge\Delta_t\lor\bigwedge\Delta_u.
   \]
   If both successors were derivably zero, so would Delta_s be.
   Select a consistent one. This proves (6.3.8).

3. At conjunction, aconjunctivity prevents copying a mu-counter to
   both children. Transfer the two sublists; the conjunction of the
   two translated children is the old translated conjunction before
   any weakening. If a higher-priority pre-existing copy absorbs
   either child, that copy was already a conjunct of Delta_s.
   Thus the new label remains consistent. At a binder opening, the
   new r is 1, so fixed-point unfolding identifies the translated body
   with the old translated binder. Opening a nu-binder or expanding
   a legal raw nu-variable changes no mu-annotation; use greatest
   fixed-point unfolding. Any additional reset only weakens formulas.

4. For a particular diamond demand <a>p, write D for the conjunction
   of its translated p-successor with the translated bodies of all
   [a]q demands. Repeated applications of (5.3), and the Boolean/modal
   identities, derive conjunction Delta_s <= <a>D before weakening.
   If D=0 were derivable, (5.4) would make Delta_s inconsistent.
   Hence this successor is consistent; the argument applies separately
   to every required diamond. Formula-list collisions again either
   retain the contributing list or retain an already demanded copy.
   This proves that every modal successor may be placed in B.

5. Suppose raw mu-X is expanded. A higher-priority pre-existing pX
   makes the new copy redundant, as in case 2. Otherwise put
   D=conjunction Delta'_s, R=r(s,c), and let F(X)=R and p'(X), where
   p' has had its outside parameters closed by the old annotations.
   Neither D nor R has a free X. Weakening the annotations of lower
   priorities gives (6.3.11), so D and mu X.F(X) is consistent.
   The consistency consequence of Proposition 5.7(vi), proved earlier
   in this note, gives consistency of
   \[
    D\land F(\mu X.(\neg D\land F(X))).
   \]
   Dropping the outside conjunct R weakens this formula to
   \[
    D\land p'(\mu X.(R\land\neg D\land p'(X))),
   \]
   exactly (6.3.13). The definition R_new=R and not D identifies
   this with the translated raw-body successor. Collateral deletion
   resets weaken annotations after this argument. Thus they preserve
   the conclusion also when they reset the just-incremented counter.

This proves consistency preservation without using satisfiability or
completeness to justify a proof-theoretic step. To exclude rejection,
first a literal clash, or the explicitly normalized constant 0, makes
Delta_s derivably zero. Such a node cannot belong to B.

For overflow, let m=|p0| and N=2^m. A live counter with value N+1 has
undergone N+1 surviving increments since its last reset. The associated
predecessor labels range over at most N subsets of the m raw subformulas.
There are therefore two such predecessors u<v with Gamma_u=Gamma_v.
No higher-priority counter was incremented, reset, or deleted between
them: any of those events would reset c. No new higher-priority identity
can be born, since births are appended to G. Thus all annotations above
c are identical at u and v. Immediately after either increment, all
annotations below c are 1. The raw X is the only formula whose list
contains c. Consequently the translated labels excluding X are equal,
which proves (6.3.14), not merely equality of the raw labels.

The constraint not(conjunction Delta'_u) was added to r at u and has
not been erased, since c was not reset. Its translated raw-X formula
at v is mu X.(r(v,c) and p'X). By unfolding this least fixed point is
below r(v,c). This gives (6.3.15). But (6.3.11) at v gives the companion
inequality into conjunction Delta'_v. Boolean algebra now proves
conjunction Delta_v=0, a contradiction. Hence no node in B overflows.

Finally use finite rejection ranks, not global tableau halting.
A rejecting universal node has a rejecting successor; a rejecting
disjunction node has both successors rejecting. Induction on the
finite rejection derivation, using (6.3.8)/(6.3.9), excludes every such
node from B. Since B contains the root, the root does not reject.
This was the proposed (i)-to-(ii) conclusion; it is not established by
the preceding overflow argument. The later correction records the gap.

### Retrieved mathematical content: the extracted model, pp. 349--351

Prune rejecting nodes and select exactly one disjunctive successor at
each surviving disjunction. Call the resulting rooted tree T'. Let S
consist of its modal-expansion nodes and its leaves. For a tableau node
t, U(t) contains t and the preceding nodes back to, but not including,
the most recent strict ancestor in S; if there is no such ancestor,
include the original root. In particular U(s), for s in S, is its
incoming finite nonmodal segment. An outgoing modal edge from s enters
exactly one segment U(t), with t in S, by finite nonmodal saturation.
The source model is M=(S,I), with
\[
\begin{split}
 (s,t)\in I(a)&\quad\Longleftrightarrow\quad
    \text{an }a\text{-labelled edge from }s
       \text{ enters a node in }U(t),\\
 s\in I(P)&\quad\Longleftrightarrow\quad P\in\Gamma_s.
\end{split}
\]
There is no family M_s in these definitions. The distinct families are
Delta_s (consistency formulas), Theta'_s (one node's ordinal-closed
formulas), and Theta_s (the union over one model state's segment).

For p in Gamma_s let V_p=(X_1,...,X_n) and
sigma X_i=sigma X_i.p_iX_i. The source defines, for a mu-counter c,
\[
 \alpha(s,c)=\sup_{t\in T'}a(c,s,t),\qquad
 q_i=\alpha(s,c)X_i.p_iX_i\quad(X_i=X(c)\in A_{\mu p}),
\]
and q_i=sigma X_i for X_i outside A_{mu p}. Only descendant endpoints
with a counter-continuation chain contribute to the supremum; the
zero-length continuation contributes 0. Then
\[
 e''(s,p)=p[\bar X/\bar q],\qquad
 \Theta'_s=\{e''(s,p):p\in\Gamma_s\},\qquad
 \Theta_s=\bigcup_{t\in U(s)}\Theta'_t.
\]
The rank follows the discarded-to-retained counter arrows of (6.1.12).
It is not the present counter value. The mu-chain bound makes every
rank finite; no repaired nu-chain bound is needed here.

The source relation p' square-subset-or-equal p permits decreasing
ordinal indices in occurrences of alpha X.qX, without other syntactic
changes. Write it as p' preceq p in the supplied arguments below. It
does not change a nu into a mu, and does not replace an ordinary mu
binder by a finite approximant. Source conditions (6.3.16)--(6.3.21)
are the following mathematical implications, for s in S:
\[
\begin{array}{rll}
 (6.3.16)&p\land q\in\Theta_s&\Longrightarrow p,q\in\Theta_s,\\
 (6.3.17)&p\lor q\in\Theta_s&\Longrightarrow p\in\Theta_s\text{ or }q\in\Theta_s,\\
 (6.3.18)&\langle a\rangle p\in\Theta_s&\Longrightarrow
    \exists t\in S\ ((s,t)\in I(a)\land p\in\Theta_t),\\
 (6.3.19)&[a]p\in\Theta_s&\Longrightarrow
    \forall t\in S\ ((s,t)\in I(a)\Rightarrow
         \exists p'\preceq p\ (p'\in\Theta_t)),\\
 (6.3.20)&\alpha X.pX\in\Theta_s&\Longrightarrow
    \exists\beta<\alpha\ (p(\beta X.pX)\in\Theta_s),\\
 (6.3.21)&\nu X.pX\in\Theta_s&\Longrightarrow
    p(\nu X.pX)\in\Theta_s.
\end{array}
\]
In (6.3.20), alpha is an ordinal or the symbol mu, and every ordinal
is below mu for this notation. The source proof deals with the ordinary
mu case and the finite ordinal ranks actually introduced above.
It subsequently defines, for closed q,
\[
 q^\Theta=\{s\in S:\exists q'\preceq q\ (q'\in\Theta_s)\},
 \qquad
 \bar q^\Theta=(q_1^\Theta,\ldots,q_n^\Theta),
\]
and states
\[
 (6.3.22)\qquad p(\bar q)^\Theta\subseteq p^M(\bar q^\Theta).
\]

### Supplied rank and saturation details

For definiteness a continuation of a mu-obligation records its
successive local-list positions, including the replacement position
after a collision. Count a raw-X increment on the step that performs
it, even if that provisional list is then discarded. Such a final
increment adds at most one event per collision to the earlier safe
chain bound; there are at most K such changes of first-mu priority.
Thus the finiteness argument in the preceding section still bounds
these continuation counts. This event convention makes explicit the
edge accounting used in the equality
alpha(t,c)=alpha(t+,c')+1 on p. 351.

The resulting ranks satisfy these exact recurrences.

- Along the unique surviving nonmodal successor, a continued counter's
  rank is unchanged if its own variable is not expanded. Resets change
  its numerical value, but are not counted as increments of that
  variable. If its variable is expanded, its rank is one plus the
  successor rank, following a collision arrow if necessary.
- At a modal node a counter in a diamond list continues only along
  that demand's edge. A counter in a box list continues along every
  matching-program diamond edge. Its rank is the supremum of the
  ranks on those continuations, with supremum empty = 0.
- The prefix through any active variable is retained together. Hence
  all its outer active mu-parameters have equal ranks along a
  nonmodal continuation that does not expand them; when an entire
  list collides, follow the corresponding prefix entries as well.

All these follow by partitioning the set of finite continuations at
their first step. There is one selected disjunctive successor, and no
branching at conjunction, binder, or variable steps. Aconjunctivity
is essential in the modal statement: the same mu-identity does not
simultaneously belong to an unrelated diamond and box list.

To prove (6.3.16), follow a translated conjunction in its nonmodal
segment to the step at which its raw conjunction is decomposed.
The mu-rank recurrences preserve its outside substitutions; the two
translated children are exactly its conjuncts. Both enter the same
segment union, including after a collision continuation. The same
argument for the one selected disjunction child proves (6.3.17).
Literals persist to the segment's endpoint, so P in Theta_s iff
P in Gamma_s, and no s has both P and not P in Theta_s. The explicit
normalization/rejection of 0 handles the Boolean constants.

A diamond persists to the terminal modal node of its segment. Its
own required edge exists, and the translated body has the same ranks
on that edge; finite nonmodal saturation supplies the unique next
model state. This proves (6.3.18). A box contributes its body to
every matching edge. The rank on any one edge is at most the rank
before the branching. Thus the body in that successor segment is
obtained only by lowering ordinal indices, proving (6.3.19). There
is no demand for an a-edge when there is no a-diamond, and the box
condition is then vacuous.

For (6.3.20) with an ordinary mu binder, take its raw binder opening
in the segment. The new counter's finite rank beta yields the
translated body p(beta X.pX), and beta<mu. For a finite alpha binder,
its top-level origin is a raw X carrying rank alpha. A raw mu-X can
never remain unexpanded at a saturated endpoint. Its eventual X-step
has a continued counter c' and gives
\[
 \alpha=\alpha(t,c)=1+\alpha(t+,c'),\qquad
 \beta=\alpha(t+,c').
\]
The translated body is p(beta X.pX); outer active parameters are
unchanged along this continuation. This proves strict descent and
also shows that a top-level zero approximant cannot occur in Theta_s.

For (6.3.21), an ordinary raw nu-binder is handled by its opening.
A raw nu-X with flag 0 is handled by its permitted variable step.
If the flag is 1 at a saturated node, trace the provenance of that
1 backward inside the same segment. At inheritance follow the old
flag. At a nu-only maximum collision follow an input attaining the
maximum 1, even if that input's identity was discarded. At sharing
follow the input from which the shared flag arose. A modal step or
a reset cannot be crossed while tracing a 1. The segment is finite,
and births are at 0, so this backward trace reaches a genuine
nu-X expansion in the segment.

Its translated greatest fixed point has the same outside
mu-parameters as the present one. For a retained mu-containing list,
a change to a preceding mu-counter would reset the flag, so no such
change occurs on the provenance interval, and the rank recurrence
keeps those parameters equal. A nu-only collision has no preceding
mu-parameters to compare. Moreover, sharing a nu-counter across
conjunction children cannot share a preceding active mu-counter:
activity transitivity would make that mu-variable active in both
children, contradicting aconjunctivity. Thus the shared case also
has no preceding mu-parameters. The earlier genuine X-step therefore
put exactly p(nu X.pX) into this same Theta_s. This repairs the source's
implicit assumption that the retained flag identity itself must have
undergone a 0-to-1 X-step.

The binder-opening cases also include vacuous binders. If X is not
free in the raw body, no X-counter is created. For mu choose beta=0:
p(beta X.pX)=p, and the translated raw body is already exactly p.
For nu the unfolding likewise gives p(nu X.pX)=p. Thus these cases
do not assume a nonexistent new counter.

### Supplied complete truth lemma from the six conditions

Fix the above M and Theta. All formula substitutions are
capture-avoiding; p is positive-normal in its free variables and q_i
are closed positive-normal L_{mu+} formulas. The relation preceq is
reflexive and transitive, so
\[
 q'\preceq q\quad\Longrightarrow\quad(q')^\Theta\subseteq q^\Theta.
\]
Lowering indices preserves the outer Boolean/modal constructor. At
a binder it preserves the binder kind unless that binder already
has an ordinal index, in which case it can lower that index.
Substitution into a positive context preserves this syntactic
comparison, after hygienic bound-variable renaming. These facts let
each of (6.3.16)--(6.3.21) be applied to the particular witness in
Theta_s used in the definition of q^Theta, rather than assuming
that the unshortened q itself belongs to Theta_s.

We prove (6.3.22) by structural induction on p, with transfinite
induction on an ordinal binder's index inside its binder case.
The cases are as follows.

1. For P, P^Theta=I(P). For not P, the absence of a clash gives
   (not P)^Theta subseteq S minus I(P). The normalized constants
   give 0^Theta=empty and 1^Theta subseteq S. For a free variable
   X_i, X_i(q)^Theta=q_i^Theta by substitution, exactly its semantic
   value in the valuation bar q^Theta.

2. If s is in (u or v)(bar q)^Theta, its witness in Theta_s is a
   disjunction of index-decreased copies. Condition (6.3.17) puts
   one of those copies into Theta_s. Hence
   \[
    (u\lor v)(\bar q)^\Theta
       \subseteq u(\bar q)^\Theta\cup v(\bar q)^\Theta
       \subseteq u^M(\bar q^\Theta)\cup v^M(\bar q^\Theta).
   \]
   The final union is (u or v)^M(bar q^Theta). For conjunction,
   (6.3.16) gives both witnesses; replace the two unions by
   intersections and obtain the required conjunction semantics.

3. Condition (6.3.18), applied to a witnessing diamond, gives
   \[
    (\langle a\rangle u)(\bar q)^\Theta
      \subseteq\langle I(a)\rangle u(\bar q)^\Theta
      \subseteq\langle I(a)\rangle u^M(\bar q^\Theta).
   \]
   The second inclusion is monotonicity of relational preimage and
   the induction hypothesis. For a witnessing box, (6.3.19) gives
   at every a-successor a formula preceq the witnessing body, hence
   preceq u(bar q). Thus every successor lies in u(bar q)^Theta.
   Apply the induction hypothesis and monotonicity of the universal
   relational operator to obtain [a]u^M(bar q^Theta). This also
   covers a state with no a-successors.

4. Let p=alpha X.u(X,bar Y), with alpha an ordinal. Condition
   (6.3.20) gives the following inclusion; the union is essential:
   \[
    (\alpha X.u(X,\bar q))^\Theta
      \subseteq\bigcup_{\beta<\alpha}
       u(\beta X.u(X,\bar q),\bar q)^\Theta.
   \]
   The witness beta can depend on s. If the witness formula itself
   has outer index gamma<=alpha, its beta satisfies beta<gamma<=alpha,
   and its body is preceq the corresponding body on the right.
   Put F(A)=u^M(A,bar q^Theta). Structural induction on u gives
   \[
    u(\beta X.u(X,\bar q),\bar q)^\Theta
       \subseteq F((\beta X.u(X,\bar q))^\Theta).
   \]
   The induction hypothesis on beta and monotonicity of F give
   \[
    F((\beta X.u(X,\bar q))^\Theta)
        \subseteq F(F^\beta(\varnothing))
        =F^{\beta+1}(\varnothing)
        \subseteq F^\alpha(\varnothing).
   \]
   The last inclusion holds because beta+1<=alpha. Taking the union
   proves the alpha case, including alpha=0, whose witness union is
   empty. For p=mu X.u, use the same union over ordinal beta and the
   same structural step; each F^{beta+1}(empty) is contained in mu F.
   No single beta uniform over all states is asserted.

5. Let p=nu X.u(X,bar Y) and
   A=(nu X.u(X,bar q))^Theta. Condition (6.3.21) applied to each
   witness, with the syntactic comparison after unfolding, gives
   \[
    A\subseteq u(\nu X.u(X,\bar q),\bar q)^\Theta
      \subseteq u^M(A,\bar q^\Theta)=F(A).
   \]
   The second inclusion is structural induction on u with the
   closed argument nu X.u(X,bar q). Thus A is a post-fixed set of F.
   The greatest-fixed-point characterization yields A subseteq nu F,
   which is precisely the required nu case.

These exhaust the positive-normal grammar and prove (6.3.22).
Let rho be the first member of S below the original tableau root r0.
Its existence follows from finite nonmodal saturation, and r0 is in
U(rho). Since e''(r0,p0)=p0, we have p0 in Theta_rho. Therefore
rho in p0^Theta subseteq p0^M. This corrects the source's final
notation M,r0 models p0 when r0 itself is not a modal node or leaf.

### Supplied finite-configuration model and ordinary backedge depth

The preceding construction works on any nonrejecting selected tree.
To make finiteness constructive, select the disjunctive successor by
the memoryless strategy in the finite nonrejecting configuration
region already proved in the manuscript. Fix the same deterministic
administrative scheduling and collision-origin convention throughout.
Let C be the set of normalized configurations, so |C|=2^{O(m^3)}.

Use as finite model states the reachable entry configurations of
nonmodal segments: the initial configuration, and configurations
immediately after actual modal edges. From an entry c, follow its
unique chosen nonmodal path to its modal or accepting endpoint h(c).
The path is finite, and h(c) is uniquely determined by c. Do not use
the artificial self-loop assigned to an accepting terminal for the
safety computation as a program edge. Put an a-edge from c to d for
each actual a-demand edge from h(c) whose successor configuration is d.
Set P true at c exactly when P belongs to Gamma_{h(c)}. This is a
finite directed model with at most |C| states and outdegree at most m.

The rank proof is still available on its unfolding. More explicitly,
each rank is a property of an entry configuration and a local counter
position, with transitions following that position through the fixed
successor updates. Normalization renames identities consistently and
does not change the set of future increment counts. Thus isomorphic
normalized configurations give identical ranks at corresponding
positions. The finite nonmodal path and its union of translated
formulas consequently depend only on the entry configuration, not
on the history by which it was reached. Define Theta_c as this union.
The six proved conditions hold on the finite model itself: their
proofs use exactly these finite segments, counter continuations and
actual modal edges. The truth lemma therefore proves that its initial
state satisfies p0. This supplies a finite directed model directly;
it is not an appeal to filtration preserving fixed points.

A precise weaker tree-with-backedges representation follows without
any additional mu-calculus theorem. Unfold this finite graph from its
initial state along paths until a state would repeat on the current
path. Replace that last extension by an edge to its earlier occurrence
on the same path, allowing a self-loop when the target is the current
node. Every non-backedge root-to-node path has distinct
projected states, so the underlying rooted-tree depth is at most
|C|-1 (or at most |C| if one counts the final backedge as a step).
There are finitely many such paths, and each node has at most m
outgoing edges. Cycles are represented by the backedges, not deleted.

For completeness, the projection pi from this representation to the
finite graph preserves proposition labels and has both modal edge
properties: each representation edge projects to a graph edge, and
each graph edge out of pi(v) has a representation edge out of v to
a node projecting to its target. Inverse image under pi therefore
commutes with Boolean and modal operations. By transfinite induction
it commutes with each approximant of a fixed-point body, and hence
with least and greatest fixed points. Thus it preserves satisfaction
of p0. Its underlying-tree depth is 2^{O(m^3)}. This argument permits
nested or crossing backedges; it must not be described as proving a
more restrictive backedge convention.

If backedges must target strict ancestors, modify just the self-loop
case: first create a second consecutive occurrence of that graph
state; its next self-loop demand can point to the first occurrence.
At every edge choose a strict ancestor with the target state if one
exists, otherwise create the required child. Each graph state then
occurs at most twice on an underlying-tree path, so the depth is at
most 2|C|-1. The same projection argument applies, and the depth is
still 2^{O(m^3)}. Neither variant prohibits nested or crossing cycles.

### Exact `tree-like` provenance and remaining bounded obligation

Kozen's Theorem 6.3.1(iii), p. 347, uses the phrase
`finite tree-like model of depth exponential in |p0|^3`.
Printed p. 353 sends the finite-model conversion to references [8,13]
without defining tree-like, defining its depth, or printing a folding
construction. Reference [8] is Halpern--Reif, the FOCS 1981 extended
abstract on deterministic well-structured PDL, pp. 322--334.
Reference [13], p. 354, is Kozen's unpublished manuscript
`Small models for the propositional mu-calculus`. The present scan
does not contain that manuscript.

The author-hosted journal continuation of [8] is Halpern--Reif,
*Theoretical Computer Science* 27 (1983), 127--165,
[author PDF](https://users.cs.duke.edu/~reif/paper/halpern/detdynlogic.pdf).
Its indexed primary text, Definition 4.20 on p. 146, describes a
treelike frame as a tree with backedges to ancestors and additionally
excludes nesting or crossing of backedges. Thus that definition is
strictly more restrictive than an arbitrary finite graph represented
by simple-path unfolding. A short exact identifying excerpt is:

> tree with backedges only to ancestors and no nesting or crossing of backedges

This indexed passage was retrieved on 2026-09-06. Direct PDF opening
at the author URL returned HTTP 403, and the accessible MIT report
metadata did not yield page screenshots. Its exact diagrams and
endpoint convention were therefore not visually checked in this
pass. The journal continuation is not silently identified with the
1981 extended abstract, and neither is identified with unpublished [13].

The remaining obligation is specific: obtain the exact relevant
version of [8] or [13], identify whether Kozen's word `tree-like`
imports the no-nesting/no-crossing restriction, and, if it does,
supply a construction meeting that restriction with the stated
depth bound. The direct finite-configuration argument above proves
a finite directed model and an ordinary ancestor-backedge
representation of exponential underlying-tree depth, but does not
discharge that stricter graph-shape claim.

In every convention that can apply here, `finite` cannot mean a
finite acyclic transition tree. The aconjunctive formula
nu X.<a>X has a one-state a-loop model. A finite acyclic frame has
no nonempty post-fixed set for A |-> {s: exists t in A, s R_a t}:
choose an element of such a set furthest down an acyclic topological
order to contradict its required successor in the same set. Hence
that formula has no finite acyclic tree model. The relevant finite
depth is the depth of a finite representation's underlying tree,
not a bound on lengths of all executions in its cyclic transition
relation.

This addition edited only this source note. It did not edit the
manuscript, create software, run tests or builds, or render a
manuscript PDF. The source-shape/version obligation above remains
an authority-note obligation; it is not a license to present a
compressed outline as a completed proof in the reader-facing book.

## Correction to the supplied consistency argument: provisional occurrences and the still-open modal recurrence (2026-09-06)

An independent review found two gaps in the supplied consistency section
beginning at line 1369: its use of completed successor lists can make
Delta'_s circular, and repeated raw labels do not determine which fixed
higher-priority counter identities are attached to their formulas.
This correction supersedes that section's assertion that the global
(i)-to-(ii) proof has been completed. It does not retract the transcribed
source equations, nor does it assert that Theorem 6.3.1 is false. The first
gap is repaired below. The second is repaired for nonmodal intervals only;
the general modal recurrence remains a specific open proof obligation.

### A noncircular temporary-label construction

Suppose the rule expands raw mu-X at s, with associated counter c and
old annotation R=r(s,c). Write sigma X=mu X.bX. Counter c is last on
the local list for X; all its outside mu-parameters have higher priority.
Keep a decorated occurrence for each old formula: an occurrence records
both the raw formula and its own local counter list. Distinct decorated
occurrences are not merged merely because their raw formulas agree.

Before inserting the incoming body occurrence or resolving any collision,
give each inherited old occurrence p != X its old local list and the
temporary annotations
\[
 \widehat r(d)=
 \begin{cases}
  r(s,d),&d\text{ is higher priority than }c,\\
  1,&d\text{ is lower priority than }c.
 \end{cases}
\]
Define its translated formula using this inherited list, and put
\[
 D_s=\bigwedge_{p\in\Gamma_s\setminus\{X\}}
        \widehat e_s(p;C(s,p)).
\]
No inherited old occurrence p != X contains c, by mu-counter
disjointness. Consequently D_s is independent of the new annotation of
c, including when bX is already an old formula. In particular, the old
bX occurrence is translated using its old list, not the incoming list
which may later replace it.

Let b'(X) be the raw body with the outside parameters of the X occurrence
closed using their inherited annotations. Both D_s and R are closed,
and bound variables are renamed hygienically. Weakening all old
lower-priority annotations gives
\[
 \bigwedge\Delta_s\leq D_s\land\mu X.(R\land b'(X)).
\]
Thus consistency of Delta_s implies consistency of the right side.
Apply the already proved consistency consequence of Proposition 5.7(vi)
to F(X)=R and b'(X), with external conjunct D_s. It gives consistency of
\[
 D_s\land F\bigl(\mu X.(\neg D_s\land F(X))\bigr).
\]
Dropping the outer conjunct R yields consistency of
\[
 L_s:=D_s\land b'\bigl(\mu X.(R\land\neg D_s\land b'(X))\bigr).
\]
Now set the incoming c-annotation to R and not D_s. Form the temporary
decorated successor family by keeping every inherited old occurrence
p != X and adding the incoming decorated bX occurrence. Its translated
conjunction is exactly L_s. If bX was already present, this family has
two occurrences of bX, possibly with different translations. Retaining
both at this proof stage is intentional.

Only after this consistent temporary family exists, perform the actual
collision disposal. Removing one decorated occurrence removes one
conjunct, which weakens the conjunction, regardless of which priority
list is retained. Numerical deletion resets are then mirrored by setting
the surviving reset counters' auxiliary annotations to 1. By positivity
and fixed-point monotonicity this again weakens the conjunction. Nu-only
maximum collisions change flags but no mu-annotation, and the flag
values are not arguments of e'. Thus
\[
 L_s\leq\bigwedge\Delta_{s+}.
\]
This is the required implication; equality with the final label is not
claimed. It proves consistency of the completed successor without
requiring a special higher-priority-copy exception. If collision disposal
resets c itself, its new constraint is also erased, in agreement with its
new numerical value zero; if it discards c, there is no surviving
c-annotation to interpret. This completes the local mu-rule consistency
repair.

### What repeated labels do not determine

Keep two higher-priority identities d1,d2 associated with Y. Inside a
nu-binder with raw body
\[
 q=Y\lor(P\lor Z),\qquad r=P\lor Z,
\]
the nonmodal sequence
\[
 \{q[d1],Z[d2]\}
 \longrightarrow\{r[d1],Z[d2]\}
 \longrightarrow\{r[d1],q[d2]\}
 \longrightarrow\{Z[d1],q[d2]\}
\]
returns to the same raw set {q,Z} while exchanging the holders of d1
and d2. No Y-counter event is needed. This is the reviewer's
counterexample to attachment equality; it is not a counterexample to the
theorem. Indeed, for any closed parameter A,
\[
 \nu Z.(A\lor P\lor Z)=1,
\]
so the relevant closed q, r and Z formulas in this particular example
are equal to 1. The annotated conjunctions therefore agree here, even
though the decorated labels do not. Equality of raw labels and fixed
higher identities alone is nevertheless not a proof of (6.3.14).

### A proved sufficient invariant on nonmodal intervals

Here is a useful repair which does not match holders. Fix a surviving
mu-counter c on an interval, and suppose no counter of higher priority
than c is incremented, reset, or deleted there. Its fixed higher-priority
identities carry fixed annotations. For every node t on the interval,
translate the WHOLE current label with those higher annotations retained,
but with the annotation of c and every lower-priority counter set to 1.
Denote the translated conjunction by J_t. The holder of c must be
included: omitting it would lose constraints when that holder absorbs
a pre-existing lower-priority occurrence in a collision.

For every nonmodal step t -> t+ in this interval,
\[
 J_{t+}\leq J_t.
\]
To prove this, first keep all provisional decorated occurrences.
Selecting a disjunct replaces a disjunction by a smaller conjunctive
requirement; splitting a conjunction preserves its translation. Binder
opening and variable unfolding preserve the translated formula by the
fixed-point equation: no higher-priority mu-variable is unfolded, and
all lower annotations, including c's, are 1. New counters are appended
below c and also have annotation 1. The ordered substitution identities
give these statements with the fixed outside annotations unchanged.
Aconjunctivity ensures that a mu-counter is not copied to both
conjunction children.

It remains to check collision disposal, since merely dropping an
arbitrary conjunct need not preserve this backwards implication.
No discarded list can contain a higher-priority identity: deleting that
identity would reset c and violate the interval hypothesis. Nor is c
discarded, since it survives the interval. Every discarded list therefore
has only lower-priority mu-entries, all translated with annotation 1.
Its translated occurrence of the raw formula p is e(p). The retained
occurrence translates p with annotations each <= 1, and hence is <= e(p)
by positivity and fixed-point monotonicity. Thus the retained conjunct
implies the discarded one, and removing the latter does not change the
temporary conjunction up to provable equality. This argument applies
successively to all collisions. Resets below c do not change J, while
resets above c are excluded. Hence the displayed implication holds for
the completed step.

Consequently J_v <= J_u across any finite nonmodal interval [u,v]
satisfying these hypotheses. If u and v both expand the same c, use the
noncircular D_u defined above at u. Since the whole actual label at v
only strengthens J_v, and J_u contains every factor of D_u, we obtain
\[
 \bigwedge\Delta_v\leq J_v\leq J_u\leq D_u.
\]
The constraint not D_u was added at u and persists in r(v,c), since c
was not reset. The raw-X conjunct at v is below r(v,c), by fixed-point
unfolding. Hence also conjunction Delta_v <= not D_u, a contradiction
to consistency. This establishes the needed exclusion for nonmodal
intervals, without requiring identical attachments or even identical
raw labels.

### The unresolved modal case and the exact status

The overflow pigeonhole argument does not guarantee that its repeated
raw-label interval is nonmodal. Modal steps change the state at which
an obligation is evaluated. The preceding J-implication cannot simply
be carried across them: even the elementary rule <a>P -> P does not
give P <= <a>P as a formula inequality. For example, at an a-dead-end
where P holds, the first formula is true and the second false.

Therefore the above nonmodal invariant is not a completed global repair.
For an overflowing surviving c, one still needs either a proved
correspondence across the complete interval giving
\[
 \bigwedge\Delta_v\leq D_u
\]
for a recorded earlier D_u, or another bounded recurrence argument
which respects changing higher-counter attachments and the stated
threshold 2^{|p0|}. The stronger condition D_v <= D_u would suffice,
but has not been proved here. Equality of raw Gamma labels, fixed
higher identities, and fixed higher r-formulas do not by themselves
discharge that obligation. Increasing the numerical threshold to count
decorated configurations would change the algorithm and is not a repair
of the stated argument without additional authorization and proof.

Accordingly, the local consistency-preservation construction is now
repaired, and the nonmodal recurrence implication is proved. The global
counter-overflow exclusion, and therefore this supplied (i)-to-(ii)
proof as a whole, remains open at precisely the modal recurrence step.
The separate Theta/model direction is not independently reviewed by
this correction. Only this labelled correction was appended; no
manuscript, code, tests, builds, or manuscript renders were changed
or run.
