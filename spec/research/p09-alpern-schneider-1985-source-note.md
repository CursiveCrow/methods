# Alpern--Schneider 1985, *Defining Liveness*: source note

**Disposition:** COMPLETE AUTHOR-HOSTED JOURNAL ARTICLE ACQUIRED AND VISUALLY
READ; COMPLETE CORNELL TECHNICAL REPORT ACQUIRED, VISUALLY READ, AND KEPT AS A
SEPARATE COMPARISON WITNESS; READER RECONSTRUCTION SUPPLIED; INDEPENDENT
TOPIC REVIEW OPEN.

## Exact work and preserved authority

- Controlling publication: Bowen Alpern and Fred B. Schneider, “Defining
  Liveness,” *Information Processing Letters* 21(4), 7 October 1985,
  pp. 181--185, DOI
  [10.1016/0020-0190(85)90056-0](https://doi.org/10.1016/0020-0190(85)90056-0).
- The journal page records David Gries as communicating editor, receipt on
  5 November 1984, and revision on 20 February 1985.
- Controlling local object:
  `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf`.
- Journal-object SHA-256:
  `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31`.
- Author-hosted route:
  [Fred B. Schneider's Cornell publication copy](https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf).
- Comparison publication: Bowen Alpern and Fred B. Schneider, *Defining
  Liveness*, Cornell Department of Computer Science Technical Report TR 85-650,
  October 1984, revised February 1985. The inner title page gives 30 October
  1984 and revision on 20 February 1985.
- Comparison local object:
  `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf`.
- Technical-report SHA-256:
  `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE`.
- Technical-report route:
  [Cornell TR 85-650](https://www.cs.cornell.edu/fbs/publications/85-650.pdf).
- Both objects were retrieved on 23 August 2026. The journal PDF has five
  pages; the report PDF has eleven file pages, comprising two title/abstract
  leaves and nine internally numbered body pages.

This source has unlettered standing as the controlling authority for the exact
safety/liveness clauses used within register obligation `N-c-012`. The register
does not assign it a further letter, so this record does not invent an
`N-c-012.e` identifier.

The journal facsimile is the controlling mathematical and bibliographic
authority. The technical report is not substituted for it. It is retained to
show the prepublication state and to determine whether a suspicious printed
clause is a journal-only accident.

Printed p. 181 carries Elsevier Science Publishers B.V. (North-Holland)
copyright. Neither author-hosted file declares an open-content licence. The
handbook therefore gives an independently written mathematical reconstruction;
the local source objects are evidence and are not publication assets.

## Complete visual page map

Every file page of both source objects was inspected from a rendered page
image. Extracted text was used only as a navigation aid.

### Journal article

| PDF page | Printed page | Inspected content |
|---|---:|---|
| 1 | 181 | Publication metadata, abstract, keywords, Section 1, execution convention, program/property relation, beginning of Section 2 and safety examples |
| 2 | 182 | Exact sets \(S^\omega,S^*\), prefix notation, safety clause, stuttering footnote, Section 3 examples and exact liveness clause |
| 3 | 183 | Maximality argument for the liveness definition, uniform and absolute liveness, inclusion chain, leads-to and predictive examples, beginning of Section 4, until and total-correctness decompositions |
| 4 | 184 | Prefix topology, safety/closed and liveness/dense characterizations, Theorems 1--2 with proofs, Corollaries 1.1--2.1, Boolean-closure claims |
| 5 | 185 | Section 5 conclusion, acknowledgments, complete references |

### Cornell technical report

| PDF page | Internal location | Inspected content |
|---|---|---|
| 1 | outer cover | Title, authors, TR 85-650, October 1984, revised February 1985, Cornell affiliation, support footnote |
| 2 | title/abstract leaf | Exact 30 October 1984 and 20 February 1985 dates, abstract and keywords |
| 3 | body p. 1 | Section 1 and beginning of Section 2 |
| 4 | body p. 2 | Safety universe, exact safety definition, stuttering footnote |
| 5 | body p. 3 | Section 3, liveness examples and exact liveness definition |
| 6 | body p. 4 | Maximality discussion, uniform and absolute liveness, inclusion chain begins |
| 7 | body p. 5 | Inclusion chain completed, leads-to and predictive separations, Section 4 begins |
| 8 | body p. 6 | Until and total correctness, prefix topology, Theorem 1 begins |
| 9 | body p. 7 | Theorem 1 proof and first corollary, Theorem 2 and proof |
| 10 | body p. 8 | Second corollary, Boolean-closure results, Section 5 and acknowledgments |
| 11 | body p. 9 | Complete references |

## Version comparison

The journal article and revised technical report have the same substantive
mathematical presentation: the execution universe, safety and liveness
definitions, stuttering qualification, uniform and absolute variants,
examples, topology, Theorems 1--2, both corollaries, Boolean-closure paragraph,
and conclusion agree. Publication typesetting, citation style, pagination, and
corollary numbering differ. In particular, the report prints the two
corollaries without decimal numbers, whereas the journal labels them 1.1 and
2.1.

The problematic hypothesis in Corollary 2.1 is present in both versions. It is
therefore not treated as a journal compositor's isolated substitution. The
handbook records the literal clause and the mathematical repair separately.

## Typed semantic universe and source notation

The source takes \(S\) to be a set of program states. The reconstruction makes
the operationally implicit hypothesis

\[
 S\ne\varnothing
\]

explicit. This is needed because the source identifies liveness with density:
if \(S=\varnothing\), then \(S^\omega=\varnothing\) is topologically dense in
itself, while the source's continuation clause fails for the empty finite
sequence because no infinite suffix exists. Ordinary program-state universes
are nonempty, but the printed formalization does not state the hypothesis.

Let

\[
 S^*=\bigcup_{n<\omega}S^n,
 \qquad
 S^\omega=\{x:\omega\to S\}.
\]

Members of \(S^\omega\) are *executions* and members of \(S^*\) are *partial
executions*. The empty sequence belongs to \(S^*\). For \(u\in S^*\) and
\(y\in S^\omega\), \(u\mathbin{\smallfrown}y\in S^\omega\) is their
concatenation. For \(x\in S^\omega\), write \(x{\upharpoonright}n\) for the
finite sequence of its first \(n\) states. For \(s\in S\),
\(\langle s\rangle\in S^1\subseteq S^*\) is the one-state partial execution,
whereas \(s^\omega\in S^\omega\) is the constant execution defined by
\(s^\omega(n)=s\) for every \(n\in\omega\). These notations are needed below
to distinguish finite one-state prefixes from constant infinite witnesses.
Thus

\[
 u\preceq x
 \quad\Longleftrightarrow\quad
 \exists y\in S^\omega\;
 x=u\mathbin{\smallfrown}y.
\]

This prefix notation is the handbook's eliminable rendering of the paper's
subscripted partial-execution notation. It is not an additional relation on
programs.

A property has the exact standing

\[
 P\subseteq S^\omega.
\]

The paper writes \(x\models P\) to mean \(x\in P\); this is set membership,
not satisfaction of an independently supplied formula. A program likewise
denotes a subset \(B\subseteq S^\omega\), and the property holds for that
program exactly when \(B\subseteq P\). The paper represents a terminating run
as an infinite sequence by repeating its final state.

The introduction motivates the distinction by proof method: a safety proof
rests on an invariance argument, while a liveness proof rests on a
well-foundedness argument. This is explanatory source prose, not a theorem
that classifies proof systems.

The source classifies properties relative to the full sequence space
\(S^\omega\). If one instead relativizes the universe to the paths of a fixed
transition system, both the extension quantifiers and the topology change.
That is a separate construction and is not silently substituted here.

## Safety

The paper defines \(P\subseteq S^\omega\) to be a safety property exactly when

\[
 \forall x\in S^\omega\;
 \left(
  x\notin P
  \Longrightarrow
  \exists n\in\omega\;
  \forall y\in S^\omega\;
  (x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P
 \right).
\]

The finite prefix \(x{\upharpoonright}n\) is an irremediable witness to the
violation. The definition does not prescribe what the forbidden event must be;
it requires only that violation become recognizable after finitely many
states.

The source lists mutual exclusion, deadlock freedom, partial correctness, and
first-come-first-serve as safety examples. These examples use the paper's
execution convention, including final-state repetition for terminated runs.

Footnote 1 says this definition differs from a Lamport formulation but agrees
with it under a finite-stuttering-invariance assumption. Its separating
example is the property that the value of a variable changes at every
successive pair of states: a repeated adjacent value is a finite bad prefix,
so the property is safety here, but it is not stuttering invariant. This note
records Alpern and Schneider's comparison; it does not claim an independent
reconstruction of the cited Lamport source.

## Liveness and the two stricter source classes

The source first calls \(u\in S^*\) *live for \(P\)* exactly when there is a
\(y\in S^\omega\) with
\(u\mathbin{\smallfrown}y\in P\). This is a relation between a finite sequence
and a property, not a new property class. It differs from liveness of \(P\)
because it has not yet universally quantified over all partial executions.

Ordinary liveness means that every partial execution is live for \(P\), or
equivalently that no finite partial execution is irremediable:

\[
 \forall u\in S^*\;
 \exists y\in S^\omega\;
 u\mathbin{\smallfrown}y\in P.
\]

Equivalently, every finite word is the prefix of some member of \(P\). The
source lists starvation freedom, termination, and guaranteed service as
examples. The definition is broader than the surface form “eventually
\(q\)”: the continuation may depend on the entire finite prefix, and the
required future behavior need not be a single discrete event. Since the empty
sequence belongs to \(S^*\), the clause also implies \(P\ne\varnothing\).

The paper argues that this is the most permissive definition compatible with
its intended distinction. If the clause fails, some finite prefix has no
satisfying continuation and is therefore an irremediable bad witness. That
quantifier consequence is formal. The further claim that any property with
such a witness should not count as pure liveness is an interpretive defense of
the definition, not a mathematical uniqueness theorem.

The paper then needs to distinguish ordinary liveness from two proposals with
different continuation dependencies. The existing term *liveness* cannot
state those dependencies without ambiguity, so the paper introduces two
semantic subclasses of properties. Their standing, definitions,
nonredundancy, and use are all local:

1. A property \(P\subseteq S^\omega\) has **uniform liveness** exactly when

   \[
    \exists y\in S^\omega\;
    \forall u\in S^*\;
    u\mathbin{\smallfrown}y\in P.
   \]

   The name denotes a semantic class of properties. It differs from ordinary
   liveness because one fixed suffix must work for every finite prefix rather
   than a suffix being chosen after the prefix is known. The distinction is
   used in the predictive counterexample below.

2. A property \(P\subseteq S^\omega\) has **absolute liveness** exactly when

   \[
   \left(\exists z\in S^\omega\;z\in P\right)
   \land
   \forall y\in S^\omega\;
   \left(
    y\in P
    \Longrightarrow
    \forall u\in S^*\;
    u\mathbin{\smallfrown}y\in P
   \right).
   \]

   This also denotes a semantic class of properties. It differs from uniform
   liveness because every satisfying execution, rather than merely one common
   suffix, must remain satisfying after every finite prefix. The nonemptiness
   conjunct prevents the empty property from satisfying the universal clause
   vacuously. The distinction is used in the leads-to example below.

The quantifiers immediately give

\[
 \text{absolute liveness}
 \Longrightarrow
 \text{uniform liveness}
 \Longrightarrow
 \text{liveness}.
\]

For the first implication, choose a member of the nonempty absolute property;
it supplies the common uniform suffix. For the second, reuse the common suffix
after each prefix. The paper states this inclusion chain but does not attach a
separate numbered proof.

## Source separations: leads-to and predictive behavior

For its leads-to example, the paper requires every occurrence of event type
\(E_1\) eventually to be followed by an occurrence of event type \(E_2\). It
states that such properties are live when \(E_2\) is satisfiable, but states
without qualification that a leads-to property is not an absolute-liveness
property. The printed argument for failure of absolute liveness chooses an
infinite execution containing neither event type, which satisfies the
implication vacuously, and prefixes it by one \(E_1\)-event, leaving an
unserved request. The source does not state the existence assumptions needed
to make those choices.

In the handbook's state-set rendering, take \(E_1,E_2\subseteq S\). The exact
repaired separation assumes

\[
 E_1\ne\varnothing,
 \qquad E_2\ne\varnothing,
 \qquad S\setminus(E_1\cup E_2)\ne\varnothing.
\]

If \(e_2\in E_2\), the fixed suffix \(e_2^\omega\) works after every finite
prefix: it answers every earlier \(E_1\)-occurrence, and if
\(e_2\in E_1\cap E_2\), each suffix occurrence is answered by the next one.
Thus the property is uniformly live. If \(e_1\in E_1\) and
\(c\in S\setminus(E_1\cup E_2)\), then \(c^\omega\) satisfies the property
vacuously, but \(\langle e_1\rangle\mathbin{\smallfrown}c^\omega\) does not.
Thus, under the displayed hypotheses, the property is uniformly live but not
absolutely live.
This is a handbook repair of the source's overbroad claim, not a condition the
source prints.

The three displayed conditions are jointly necessary as well as sufficient
for this state-set rendering to be uniformly live but not absolutely live. If
\(E_1=\varnothing\), the property is all of \(S^\omega\) and is absolutely
live. If \(E_2=\varnothing\) while \(E_1\ne\varnothing\), the finite prefix
\(\langle e_1\rangle\) has no satisfying continuation. If
\(S\setminus(E_1\cup E_2)=\varnothing\), every satisfying execution contains
an \(E_2\)-state; consequently every satisfying suffix answers all
\(E_1\)-occurrences in any finite prefix and preserves its own internal
obligations. The property is then absolutely live. In particular, this last
case includes \(S=\{e_1,e_2\}\), \(E_1=\{e_1\}\), and
\(E_2=\{e_2\}\). Thus nonempty \(E_2\) alone does not validate the printed
separation.

The paper gives its predictive example in prose. The handbook renders its
quantifiers by taking state conditions \(A,B\subseteq S\), assuming
\(A,S\setminus A,B,S\setminus B\) are nonempty, and defining the property

\[
 \begin{split}
 P_{A,B}=\{x\in S^\omega:
  &(x_0\in A\Longrightarrow
    \exists N\;\forall n\ge N\;x_n\in B)\\
  {}\land{}&
  (x_0\notin A\Longrightarrow
    \exists N\;\forall n\ge N\;x_n\notin B)\}.
 \end{split}
\]

Here \(P_{A,B}\) is an ordinary property, not a new primitive. It is live when
the state alphabet permits the required eventual \(B\)- and eventual
non-\(B\)-continuations: after a nonempty prefix, its first state determines
which constant eventual behavior to choose, and after the empty prefix one
chooses a compatible first state and continuation. No single suffix can work
after both an \(A\)-initial and a non-\(A\)-initial prefix, so the property is
not uniformly live. This is exactly the dependency that the uniform
quantifier order was introduced to expose.

The existence qualifications in the previous paragraph are normally implicit
in the paper's example prose. They are stated here because, for degenerate
state alphabets or empty state conditions, the displayed separation need not
be available.

## Properties that are neither class

The source's *until* example says that an \(E_2\)-event eventually occurs and
that every preceding event has type \(E_1\). It is the intersection of:

- a safety property forbidding a non-\(E_1\) event before the first \(E_2\);
  and
- the liveness property requiring an eventual \(E_2\).

The combined property is generally neither safety nor liveness. A finite
prefix with only \(E_1\)-events has not yet violated it, but it still needs a
future \(E_2\), while a finite prefix containing a forbidden pre-\(E_2\) event
is already irremediable. The paper also presents total correctness as the
intersection of partial correctness (safety) and termination (liveness).

These examples block a false dichotomy. The paper does not claim that every
property is itself either safety or liveness.

## Prefix topology

For \(u\in S^*\), put

\[
 [u]=\{x\in S^\omega:u\preceq x\}.
\]

The cylinders \([u]\) form a basis for the prefix topology on \(S^\omega\).
This topology is the exact mathematical setting used by the source; no metric
is required. An open set is a union of cylinders, a closed set is the
complement of an open set, and a set is dense when it meets every nonempty
open set.

For nonempty \(S\):

- \(P\) is safety exactly when \(P\) is closed. If \(x\notin P\), the safety
  clause gives a cylinder \([x{\upharpoonright}n]\) contained in the complement,
  so the complement is open. Conversely, openness of the complement supplies
  just such a finite bad prefix.
- \(P\) is liveness exactly when \(P\) is dense. Every cylinder is nonempty,
  and meeting every cylinder says exactly that every finite prefix has an
  infinite continuation in \(P\).

The article states both equivalences in Section 4 but does not print these
two short direction-by-direction proofs. The handbook supplies them to expose
the role of the nonempty-state hypothesis and to avoid treating the
topological identification as a slogan.

## Theorem 1: safety--liveness decomposition

The article's Theorem 1 states that every property \(P\subseteq S^\omega\) is
the intersection of a safety property and a liveness property.

Let

\[
 \overline P
\]

be the topological closure of \(P\), equivalently the smallest safety property
containing \(P\), and define

\[
 L_P
 =S^\omega\setminus(\overline P\setminus P)
 =P\cup(S^\omega\setminus\overline P).
\]

The source writes this constructed factor simply as \(L\). The handbook's
\(L_P\) exposes its dependence on \(P\) and prevents collision with other
property variables. It is an eliminable metalinguistic renaming needed only to
state and prove the factorization, not a new primitive class of liveness. The
closure factor is safety, and

\[
 \overline P\cap L_P=P.
\]

For density, suppose toward contradiction that a nonempty open set \(O\) is
contained in the complement of \(L_P\). Then

\[
 O\subseteq\overline P\setminus P,
 \qquad
 P\subseteq\overline P\setminus O.
\]

Because \(\overline P\) and \(S^\omega\setminus O\) are closed,
\(\overline P\setminus O\) is a closed property containing \(P\). Since \(O\)
is a nonempty subset of \(\overline P\), this property is strictly smaller than
\(\overline P\), contradicting the minimality of the closure. Thus \(L_P\) is
dense and hence live.

The source proves existence only. The theorem does not say that every property
is itself one of the two classes, that the factors are unique, that a temporal
formula for them is available, or that computing a representation is cheap.
The particular safety factor \(\overline P\) is the least safety overapproximation
of \(P\); this minimality is part of the construction, not a uniqueness theorem
for all decompositions.

## Corollary 1.1: preserving expressibility

The journal's Corollary 1.1 is correctly supported by Theorem 1. If a notation
\(\Sigma\) for properties is closed under complement, intersection, and
topological closure, then every \(\Sigma\)-expressible property is the
intersection of a \(\Sigma\)-expressible safety property and a
\(\Sigma\)-expressible liveness property. Indeed,
\(\overline P\setminus P=\overline P\cap(S^\omega\setminus P)\) and its
complement are expressible under exactly those hypotheses.

This is a conditional preservation theorem. It does not assert that any
particular temporal language has closure expressible within that language;
that fact must be established separately.

Immediately afterward the article reports, on the authority of a 1983 private
communication from Plotkin, that every temporal-logic-expressible property can
be written as a conjunction of two temporal-logic-expressible liveness
properties. The article does not prove that separate expressibility claim, and
the cited private communication is not independently verifiable here.

## Theorem 2: two liveness factors

Theorem 2 assumes \(|S|>1\) and proves that every property is the intersection
of two liveness properties. Choose distinct states \(a,b\in S\), and let

\[
 \begin{aligned}
 E_a&=\{x\in S^\omega:\exists N\;\forall n\ge N\;x_n=a\},\\
 E_b&=\{x\in S^\omega:\exists N\;\forall n\ge N\;x_n=b\}.
\end{aligned}
\]

The source writes these properties as \(L_a,L_b\). The handbook alpha-renames
them \(E_a,E_b\) to avoid collision with the preceding constructed \(L_P\).
This is an eliminable metalinguistic renaming used only in this theorem and the
Corollary 2.1 countermodel. The symbols name sets of executions with eventually
all-\(a\) and eventually all-\(b\) tails. They are properties, not new kinds
of execution. Each is live because any finite prefix can be extended
by the corresponding constant infinite tail, and \(E_a\cap E_b=\varnothing\).
For arbitrary \(P\subseteq S^\omega\), both \(P\cup E_a\) and \(P\cup E_b\)
are live, and

\[
 (P\cup E_a)\cap(P\cup E_b)
 =P\cup(E_a\cap E_b)
 =P.
\]

The hypothesis is material. If \(S\) has one state, then \(S^\omega\) is a
singleton and its only dense subset is the whole space, so the empty property
cannot be an intersection of liveness properties.

The theorem also gives a direct counterexample to closure of liveness under
intersection: \(E_a\) and \(E_b\) are live but have empty intersection.

## Corollary 2.1: printed defect and minimal repair

The journal and technical report both print the following hypothesis for the
second expressibility corollary: the notation is closed under *intersection*
and has two expressible liveness properties with empty intersection. The
stated conclusion is that every expressible property is the intersection of
two expressible liveness properties.

That hypothesis does not justify the construction. Given expressible live
sets \(E_a,E_b\) with empty intersection, Theorem 2 forms

\[
 P\cup E_a
 \quad\text{and}\quad
 P\cup E_b.
\]

Intersection closure does not make these unions expressible. The printed
corollary therefore has a source-level closure-operator defect.

The stated hypothesis is insufficient, not merely insufficient for the
authors' displayed construction. In the same \(|S|>1\) space let

\[
 Q=\{a^\omega\},
 \qquad
\mathcal F=\{S^\omega,E_a,E_b,Q,\varnothing\}.
\]

Here \(a^\omega\) is the constant-\(a\) execution. The symbol \(Q\) is an
eliminable name for its singleton property, and
\(\mathcal F\) is an eliminable name for a possible denotation family. A
notation with exactly these denotations and conjunction interpreted as set
intersection is closed under intersection. Since
\(Q\subseteq E_a\), \(Q\cap E_b=\varnothing\), and
\(E_a\cap E_b=\varnothing\), the family is closed under intersection and
contains two expressible disjoint liveness properties. Its only liveness
members are \(S^\omega,E_a,E_b\): the cylinder \([\langle b\rangle]\) misses
\(Q\), and the
empty property is not dense. Their pairwise intersections are among
\(S^\omega,E_a,E_b,\varnothing\), never \(Q\). Thus the expressible property
\(Q\) has no decomposition into two \(\mathcal F\)-expressible liveness
properties. This is a countermodel to Corollary 2.1 as printed.

The minimal correction is to replace “closed under intersection” in the
hypothesis by “closed under union.” More strongly, closure under complement
and intersection would also suffice because it yields union by De Morgan's
law. Under union closure, both displayed factors are expressible and live, and
their intersection is \(P\). The handbook states the corrected conditional and
identifies the printed wording; it does not silently attribute the corrected
hypothesis to the authors.

## Boolean closure results

In the binary Boolean-operation setting of the paper:

| Class | Union | Intersection | Complement |
|---|---|---|---|
| safety / closed | closed | closed | not closed in general |
| liveness / dense | closed | not closed in general | not closed in general |

Closed sets are in fact closed under arbitrary intersections and finite
unions. A union containing a dense set is dense, so binary unions of liveness
properties are live. Theorem 2 supplies two dense sets with empty intersection
when \(|S|>1\). The only property that is both closed and dense is the whole
space \(S^\omega\).

The paper's phrase that liveness is “closed only under union” belongs to this
Boolean-operation comparison. It should not be read as a claim about arbitrary
operations not considered there.

## Proof and attribution boundaries

- The exact safety and liveness definitions, both stricter variants, examples,
  topology, Theorems 1--2, the theorem proofs, the corollary texts, and the
  Boolean-closure paragraph are printed in the acquired sources.
- The paper states rather than proves the safety/closed and liveness/dense
  equivalences. The handbook supplies the elementary direction-by-direction
  proofs.
- The inclusion chain among absolute, uniform, and ordinary liveness is stated
  without a numbered proof. The handbook expands the quantifier argument.
- Theorem 1 has a printed proof. Theorem 2 has a printed proof. Neither proof is
  imported from a later automata-theoretic development.
- Corollary 1.1 is supported as printed. Corollary 2.1 is not supported by its
  printed closure hypothesis; the union-closure repair is handbook-owned.
- Plotkin's topological proposal and the two private communications are cited
  by the article but are not independently accessible publications here. The
  handbook attributes only what Alpern and Schneider report.
- In particular, the temporal-logic-expressibility decomposition attributed to
  Plotkin by private communication is reported rather than promoted to an
  article theorem or independently verified result.
- The conclusion's claim that no more permissive definition fits the informal
  intuition is an argued methodological position, not a formal uniqueness or
  correctness theorem. The authors themselves say that “good” and “bad” are
  not formally defined enough to support such a proof.

## Reader-facing reconstruction requirements

The final presentation for this source must:

1. state \(S\ne\varnothing\), \(S^*\), \(S^\omega\), concatenation, prefix,
   singleton finite words, constant executions, property membership, program
   satisfaction, and the terminating-run padding convention before using them;
2. give both exact safety and liveness quantifier clauses and the full-sequence
   rather than fixed-transition-system boundary;
3. preserve the stuttering qualification and source examples;
4. define uniform and absolute liveness locally, state their standing as
   semantic subclasses of properties, explain their nonredundancy, and use the
   leads-to and predictive separations;
5. give the until and total-correctness decompositions without asserting a
   safety/liveness dichotomy;
6. prove safety equals closed and liveness equals dense in the prefix topology;
7. reconstruct Theorem 1 with the source's least-closed-superset proof and
   state its exact nonuniqueness, nonsyntactic, and nonalgorithmic boundaries;
8. state Corollary 1.1 with its closure hypotheses;
9. reconstruct Theorem 2, explain the \(|S|>1\) hypothesis, and state the
   Boolean-closure consequences;
10. print Corollary 2.1's defect, a countermodel to its stated hypothesis, and
    the union-closure repair rather than silently changing the source; and
11. keep the journal article, technical report, acquisition state, rights
    state, manuscript review, final build, rendered inspection, and human
    acceptance as separate statuses.

## Current source-critical findings

| ID | Source location | Finding | Required treatment |
|---|---|---|---|
| AS-01 | Journal p. 182; TR body p. 2 | The formal universe does not state \(S\ne\varnothing\), although the liveness/dense equivalence and Theorem 1 need it in the degenerate empty-state case. | State the implicit operational hypothesis explicitly in the reconstruction. |
| AS-02 | Journal p. 184, Cor. 2.1; TR body p. 8, second corollary | “Closed under intersection” neither supports the proof's unions \(P\cup E_a\), \(P\cup E_b\) nor implies the conclusion; the family \(\{S^\omega,E_a,E_b,\{a^\omega\},\varnothing\}\) is a countermodel. | Preserve the printed clause and countermodel; give union closure as the minimal correction. |
| AS-03 | Journal p. 184; TR body pp. 6--7 | The safety/closed and liveness/dense equivalences are asserted without their direction proofs. | Supply and label the elementary handbook reconstruction. |
| AS-04 | Journal p. 182 n. 1; TR body p. 2 n. 1 | The Lamport comparison depends on a cited external formulation and an in-preparation note. | Attribute it as the authors' qualification; do not claim independent source comparison. |
| AS-05 | Journal p. 185 | The conclusion argues intuitive maximality but expressly denies a formal proof of correctness. | Keep the philosophical argument distinct from Theorems 1--2. |
| AS-06 | Journal p. 183; TR body p. 5 | The leads-to paragraph conditions liveness on satisfiable \(E_2\) but claims failure of absolute liveness without the existence assumptions needed by its witness. | Preserve the two different source strengths; give the exact state-set hypotheses and counterexample as a handbook repair. |

## Bibliographic records used by the handbook

```bibtex
@article{AlpernSchneider1985,
  author       = {Alpern, Bowen and Schneider, Fred B.},
  title        = {Defining Liveness},
  journaltitle = {Information Processing Letters},
  volume       = {21},
  number       = {4},
  pages        = {181--185},
  date         = {1985-10-07},
  issn         = {0020-0190},
  doi          = {10.1016/0020-0190(85)90056-0},
  url          = {https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf},
  urldate      = {2026-08-23},
}

@techreport{AlpernSchneider1985TR,
  author      = {Alpern, Bowen and Schneider, Fred B.},
  title       = {Defining Liveness},
  institution = {Cornell University, Department of Computer Science},
  type        = {Technical Report},
  number      = {TR 85-650},
  date        = {1984-10-30},
  note        = {Revised 20 February 1985},
  url         = {https://www.cs.cornell.edu/fbs/publications/85-650.pdf},
  urldate     = {2026-08-23},
}
```

## Current disposition

The acquisition gap is closed: every page of the controlling journal article
and the comparison technical report has been visually read, hashed, and mapped.
The source note does not itself admit the reader presentation. That requires a
text-frozen reader section and compact record, followed by unanimous blind
source-fidelity, mathematical/proof, and adversarial-publication review of one
common snapshot. No test, checker, script, TeX run, interim handbook build, or
rendered-handbook claim belongs to that manuscript-content gate.
