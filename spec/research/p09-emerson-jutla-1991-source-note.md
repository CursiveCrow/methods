# Emerson–Jutla (1991), “Tree Automata, Mu-Calculus and Determinacy”

## Identity, access, and source state

- E. Allen Emerson and C. S. Jutla, “Tree Automata, Mu-Calculus and
  Determinacy (Extended Abstract),” *32nd Annual Symposium on Foundations of
  Computer Science* (1991), 368–377.
- DOI: 10.1109/SFCS.1991.185392.
- Complete ten-page course-hosted copy:
  <https://www.cs.cornell.edu/courses/cs6860/2021sp/Handouts/EmersonJutla91.pdf>.
- Local scholarly copy:
  tmp/pdfs/p09-emerson-jutla-1991/emerson-jutla-1991.pdf.
- File size: 209,673 bytes.
- SHA-256:
  B2E24A97379FE1D1DE151B2D941282BC4871067C15EA2B6EA1847C52994F2D3A.
- The PDF contains the complete title, abstract, six numbered sections, and
  references. It does not display proceedings pagination or an IEEE copyright
  footer, so file-level evidence does not establish that these are the exact
  IEEE proceedings bytes.
- No open-content license appears. The file is treated as lawful scholarly
  reading access, not republication permission.

All ten PDF pages were rendered at 180 dpi and visually inspected. The text
layer was used only as a transcription aid; formulas and source defects were
checked against the page images.

## Page map

| PDF page | Content |
|---:|---|
| 1–2 | abstract and §1 introduction |
| 3 | Definitions 2.1–2.3, nondeterministic binary tree automata |
| 4 | Definitions 2.4–2.7 and Theorem 2.1, alternating automata/strategies |
| 5 | §2.1 construction, Theorem 2.2, Definitions 3.0–3.3 |
| 6 | Definitions 3.3–3.4 and Theorem 3.1 proof sketch |
| 7 | end of Theorem 3.1 sketch; §4; Definition 4.0 |
| 8 | Definitions/Theorems 4.1–4.2, Corollary 4.3, start of Theorem 4.4 |
| 9 | end of Theorem 4.4; Theorems 5.1–5.2 |
| 10 | references |

## Announced results and explicit proof deferral

The paper announces three connected results:

1. expressive equivalence between propositional μ-calculus and finite
   automata on infinite binary trees;
2. tree-automata complementation by translating through the
   complement-closed μ-calculus; and
3. fixed-point characterizations proving determinacy, including parity games
   and certain on-line algorithm games.

The introduction explicitly says: “Detailed proofs of Theorems in section 2
and 3 appear in the second author’s dissertation [J90].” Theorem 3.1 itself
is headed “Proof Sketch.” Therefore Definitions 2.1–3.4, Theorem 2.2’s literal
bound, and the Theorem 3.1 construction sketch are source content, but the
full correctness proofs of §§2–3 are not in this extended abstract.

Section 4 is different: it prints the alternating fixed-point formulas and
substantial proofs for parity determinacy and history-free strategies.

## Nondeterministic binary tree automata

Definition 2.1 gives

\[
\mathcal N=(\Sigma,OR,AND,\psi,\delta,L,s_0,\Omega).
\]

Its standing and components are:

- \(\Sigma\): input alphabet;
- \(OR\): finite state set;
- \(AND\): transition-choice nodes;
- \(\psi\subseteq OR\times AND\): choices from a state to an AND node;
- \(\delta:AND\times\{0,1\}\to OR\): left/right successor states;
- \(L:AND\to\Sigma\): the input symbol required by an AND node;
- \(s_0\in OR\): start state; and
- \(\Omega\subseteq OR^\omega\): an acceptance condition.

An input tree is \(t:\{0,1\}^*\to\Sigma\). Definition 2.2 recasts acceptance
as a two-player infinite game. Player I chooses an AND successor of the
current OR state consistent with the input label; Player II chooses the next
direction \(0\) or \(1\). A legal Player-I strategy and one infinite branch
determine a unique infinite OR-state path.

Definition 2.3 calls Player I’s strategy winning exactly when every infinite
input branch generates an OR-state path in \(\Omega\). The automaton accepts
\(t\) when such a strategy exists.

The paper’s Streett example uses pairs
\((GREEN_i,RED_i)\) and requires

\[
\bigwedge_i
\bigl(GF\,GREEN_i\Longrightarrow GF\,RED_i\bigr).
\]

Its “Pairs” condition is the complement of that Streett condition. These
names are source acceptance families on infinite OR-state sequences.

## Alternating binary tree automata

Definition 2.4 adds a second kind of AND node:

\[
\mathcal A=
(\Sigma,OR,DAND,AAND,\psi,\delta,\chi,L,s_0,\Phi).
\]

- \(DAND\) nodes choose transitions in the two tree directions;
- \(AAND\) nodes express universal nondeterminism;
- \(\psi\subseteq OR\times DAND\);
- \(\delta:DAND\times\{0,1\}\to AAND\);
- \(\chi\subseteq AAND\times OR\); and
- \(\Phi\subseteq OR^\omega\) is the acceptance condition.

The distinction is necessary because a single input-tree branch can now
generate a set of OR-state sequences, one for each universal choice. The
source calls a finite such sequence a thread and the corresponding infinite
sequence an ithread. Definition 2.6 requires every ithread generated along
every input branch by Player I’s strategy to satisfy \(\Phi\).

Definition 2.7 says that a Player-I strategy is history-free when its choice
at a tree node depends only on the current automaton state and that tree node,
not on the earlier universal-choice history. An automaton is history-free when
every accepted tree has such an accepting strategy. This is a property of an
alternating automaton’s winning strategies, not the memoryless-strategy
theorem later proved for arbitrary parity game trees.

Theorem 2.1 is attributed to Gurevich–Harrington: a winning strategy for a
Muller alternating automaton can be replaced by a forgetful strategy depending
only on a small finite history. The proof is not supplied here.

## Theorem 2.2: exact construction and bound

Section 2.1 explains the construction problem. A nondeterministic automaton
must collect the many universal threads into one finite-state path. For a
history-free alternating automaton it does not need the general forgetful
strategy theorem; its finite state can instead combine the thread endpoints
and apply the cited Safra/co-Safra word-automaton constructions.

Theorem 2.2 states that a Streett alternating tree automaton
\(\mathcal A\) is converted to an equivalent nondeterministic Pairs tree
automaton \(\mathcal N\). If

\[
|OR|=n,\qquad |DA|=m,
\qquad\Phi\text{ has }k\text{ pairs},
\]

then the literal printed bounds are

\[
\begin{aligned}
|OR'|
  &=2^{\,k^2\,2^{O(n\log n)}},\\
|AND'|
  &=2^{\,k^2\,2^{O(n\log n)}}
       \cdot m^{\,2^{O(n\log n)}},\\
\Omega&\text{ has }k\,2^{O(n\log n)}\text{ pairs}.
\end{aligned}
\]

The theorem gives no hidden polynomial simplification of these nested
exponents. The extended abstract sketches the thread-collection idea but
defers the detailed proof to Jutla’s dissertation.

## Propositional μ-calculus on binary trees

Definition 3.0 gives proposition letters, proposition variables, Boolean
connectives, \(EX,AX\), and

\[
\mu X.f(X),\qquad \nu X.f(X),
\]

where \(f\) is syntactically monotone in \(X\). A sentence has no free
propositional variables.

Definition 3.1 literally takes a Kripke tree as

\[
t:\{0,1\}^*\to Prop
\]

and writes \(x\models P\) iff \(P=t(x)\). The source notes that a Kripke tree
is usually labelled by \(2^{Prop}\), but chooses the tree-automaton alphabet
presentation for the equivalence argument. This source-specific single-label
convention must not silently become the general transition-system semantics.

Definition 3.2 has the standard child clauses:

\[
\begin{aligned}
x\models EXp&\Longleftrightarrow
 \exists i\in\{0,1\}\ (x i\models p),\\
x\models AXp&\Longleftrightarrow
 \forall i\in\{0,1\}\ (x i\models p).
\end{aligned}
\]

The intended fixed-point clauses are the least fixed point as the intersection
of pre-fixed points and the greatest fixed point as the union of post-fixed
points.

### Printed defect in Definition 3.2

The page image prints \(\nu X.f(X)\) at the start of both numbered
fixed-point clauses (3) and (4). Clause (3) uses the intersection/pre-fixed
point construction and therefore must begin with \(\mu X.f(X)\); clause (4)
uses the union/post-fixed point construction and is the \(\nu\)-clause.
The grammar, prose, and mathematics make the correction determinate. A
reader-facing transcription must identify the duplicated \(\nu\) as a print
defect rather than silently reproducing it or assigning least-fixed-point
semantics to \(\nu\).

## Fischer–Ladner closure and its print defect

Every formula is put in positive normal form, with negation only on
proposition letters; \(not(p)\) names the positive normal form of \(\neg p\).
Definition 3.3 makes \(FL(p)\) the least set containing \(p\), closed under
positive complement, Boolean/modal components, and one-step unfolding of
both \(\mu\) and \(\nu\).

### Printed defect in Definition 3.3(6)

Clause (5) correctly prints:

\[
EXq\in FL(p)\Longrightarrow q\in FL(p).
\]

Clause (6) literally prints:

\[
AXp\in FL(p)\Longrightarrow q\in FL(p),
\]

with unrelated metavariables \(p\) and \(q\). The only coherent parallel
clause, and the one used by the construction, is

\[
AXq\in FL(p)\Longrightarrow q\in FL(p).
\]

This is a second visible typographical defect in the extended abstract.

## Pre-models and regeneration

Definition 3.4 calls a labelled Kripke tree a pre-model when its closure
labelling satisfies:

- exactly one of \(p\) and \(not(p)\);
- a disjunction iff one disjunct;
- \(EXp\) iff some child has \(p\); and
- \(\mu X.f(X)\) iff its one-step unfolding \(f(\mu X.f(X))\).

The last equivalence permits an arbitrary fixed point, not necessarily the
least. The source therefore defines a regeneration relation: a
\(\mu\)-sentence is regenerated from one node to a later node when it is
rederived while remaining a subsentence at every intervening derivation step.
A winning strategy is well founded when every such \(\mu\)-regeneration
relation is well founded.

Standing: regeneration is a relation among occurrences of least-fixed-point
sentences in a derivation generated by a pre-model strategy. It is not a
transition relation on the input Kripke tree. Its necessity is exactly the
difference between an arbitrary fixed point allowed by the local unfolding
equation and the intended least fixed point. Its use is to characterize when
a pre-model is a genuine model.

The main Streett–Emerson result cited in the prose says that a pre-model is a
model iff it is generated by a well-founded winning strategy. The formal proof
is referred to the cited source, not reproduced.

## Theorem 3.1: formula-to-automaton construction

Theorem 3.1 states that every μ-calculus formula \(f_0\) is converted to a
Streett history-free alternating tree automaton accepting exactly the
proposition-labelled binary-tree models of \(f_0\).

The printed proof sketch:

1. views the formula parse tree as an alternating transition diagram;
2. sends conjunction to \(AAND\), disjunction to \(OR\), and \(AX/EX\) to
   directional \(DAND\) behavior;
3. identifies a bound-variable occurrence with its binder node, creating the
   unfolding loop;
4. observes that a winning strategy for the initial trivial acceptance
   condition generates a pre-model;
5. orders fixed-point variables by syntactic precedence;
6. assigns a height to each variable in that partial order; and
7. replaces the trivial condition with Streett pairs which enforce
   well-founded least-fixed-point regeneration.

For height \(i\), \(GREEN_i\) consists of nodes corresponding to a variable
of height \(i\) bound by a \(\mu\)-subformula. \(RED_i\) consists of nodes
corresponding to variables of height at least \(i\) bound by
\(\nu\)-subformulas. The Streett condition is

\[
\bigwedge_i
(GREEN_i\text{ infinitely often}
\Longrightarrow RED_i\text{ infinitely often}).
\]

The sketch asserts that the resulting automaton has a winning strategy exactly
when the pre-model strategy is well founded. Because only the acceptance
condition changes, history-freedom is preserved. The theorem is not
accompanied by a state-count bound in §3, and its detailed correctness proof
is deferred to Jutla’s dissertation.

## Expressive equivalence and complementation

At the start of §4, Theorems 3.1 and 2.2 yield a translation from
propositional μ-calculus to nondeterministic Rabin/Pairs tree automata.
Niwiński’s reverse translation is cited. The paper therefore concludes
expressive equivalence between propositional μ-calculus and nondeterministic
tree automata.

Formula complementation is syntactic in positive normal form. Translating an
automaton to a formula, complementing the formula, and translating back gives
the claimed alternative proof of Rabin’s tree-automata complementation lemma.
The reverse translation is cited rather than reproved here, and the two
forward construction proofs retain the extended-abstract boundary above.

## Definition 4.0: literal parity convention

Automaton/game states carry colors \(0,\ldots,m\). On an infinite sequence,
the source declares:

- \(even_k\): the largest color in \(0,\ldots,k\) occurring infinitely often
  is even;
- \(odd_k\): the largest such infinitely recurring color is odd.

The parity condition is \(even_m\). This is the largest-recurring-even
convention. It is not the later Bradfield–Stirling
least-recurring-even convention, although a finite priority reversal converts
one to the other.

## Theorems 4.1–4.2 and parity determinacy

A game tree is an infinite AND/OR tree whose nodes are colored
\(0,\ldots,m\), with each OR node having the same color as its AND
successors. Player I selects an AND successor at OR nodes; Player II selects
an OR successor at AND nodes.

Definition 4.1 lets \(I_k(t)\) be the game trees where Player I has a strategy
whose every path satisfies \(even_k\lor Ft\), and \(II_k(t)\) the dual class
for Player II with \(odd_k\lor Ft\). Put

\[
\lambda_n=
\begin{cases}
\nu,&n\text{ even},\\
\mu,&n\text{ odd}.
\end{cases}
\]

Theorem 4.1 gives the alternating fixed-point characterization

\[
I_n(t)=
\lambda_n x_n\cdots\mu x_1\nu x_0
\left(
 \bigvee_{i=0}^{n}
   (color_i\land EX\,AX\,x_i)
 \lor t
\right).
\]

Theorem 4.2 gives the player-dual characterization

\[
II_n(t)=
\lambda_{n-1}x_n\cdots\nu x_1\mu x_0
\left(
 \bigvee_{i=0}^{n}
   (color_i\land AX\,EX\,x_i)
 \lor t
\right).
\]

The proof of Theorem 4.1 is printed as an induction on the largest color,
using a well-founded relation for the least-fixed-point case. Theorem 4.2 is
declared symmetric. Corollary 4.3 follows because the two formulas are
complements: every parity game tree is won by one of the players.

## Theorem 4.4: history-free winning strategies

Theorem 4.4 states that either player’s winning strategy in a parity infinite
game can be replaced by a history-free winning strategy. Here history-free
means that two occurrences with identical remaining partial game trees receive
the same choice.

The printed proof treats Player I and assigns ordinal rank maps
\(\mu_{2k+1}\) to odd-color obligations. Their finite tuple is ordered
left-lexicographically, hence well founded. At each OR node the new strategy
chooses, among occurrences with the same remaining partial game tree, a
successor with least rank tuple. If the new strategy admitted a losing path,
two successive occurrences of the decisive odd color would force a strict
decrease in the well-order, contradiction. The Player-II case swaps AND and
OR. This is a substantive printed proof, unlike the deferred construction
details of §§2–3.

## Section 5: on-line-game applications

Section 5 applies the same fixed-point method to an infinitely colored game
from Raghavan–Snir. Theorem 5.1 gives dual μ-calculus schemata for the sets
\(I\) and \(II\) of game trees won by Players I and II:

\[
\begin{aligned}
I&=\mu y\,\exists i\,\nu x
  ((EX\,AX\,x\land color_n,\ n<i)\lor y),\\
II&=\nu y\,\forall i\,\mu x
  ((AX\,EX\,x\lor color_n,\ n\ge i)\land y).
\end{aligned}
\]

Theorem 5.2 gives the corresponding \(F_\sigma\)-game schemata when
\(A=\bigcup_iF_i\) and each closed \(F_i\) is represented by a tree \(T_i\):

\[
\begin{aligned}
I&=\mu y\,\exists i\,\nu x((EX\,AX\,x\land T_i)\lor y),\\
II&=\nu y\,\forall i\,\mu x((AX\,EX\,x\lor\neg T_i)\land y).
\end{aligned}
\]

The paper presents these as determinate complements and as a simplification
of the earlier existential derandomization argument. They are applications of
the fixed-point characterization, not additional finite-automaton translation
bounds.

## Proof-status table

| Source item | Status in the extended abstract |
|---|---|
| Definitions 2.1–2.7 | printed |
| Theorem 2.1 | cited Gurevich–Harrington result; no proof |
| Theorem 2.2 | exact statement/bounds and construction idea; details deferred |
| Definitions 3.0–3.4 | printed, with two visible typographical defects |
| Theorem 3.1 | explicitly a proof sketch; details deferred |
| reverse automaton-to-formula translation | cited to Niwiński |
| Definition 4.0 | printed |
| Theorem 4.1 | proof printed |
| Theorem 4.2 | symmetric argument only |
| Corollary 4.3 | immediate complement consequence |
| Theorem 4.4 | substantive ranking proof printed |
| Theorems 5.1–5.2 | formula statements and short determinacy argument |

## Source limitations

- The extended abstract does not contain the detailed proofs promised in
  Jutla’s dissertation for §§2–3.
- It does not work a concrete automaton run on a sample tree.
- It does not work a small formula through the full alternating-to-
  nondeterministic construction.
- It does not give a separate size bound for Theorem 3.1.
- It does not use arbitrary finite transition systems; its μ-calculus
  semantics is on full infinite binary labelled trees.
- It does not use the least-recurring parity convention.
- It does not define the later three alternation-depth hierarchies.

These are literal source boundaries, not manuscript gaps to fill by inventing
content.

## Closure decision

The complete extended-abstract body has now been visually reconciled.
Reader-facing reconstruction can close at the published source’s actual
strength by including:

- exact automaton and game objects;
- exact Theorem 2.2 bound;
- exact binary-tree μ-calculus semantics and both printed defects;
- Fischer–Ladner closure, pre-models, and regeneration;
- Theorem 3.1’s Streett construction and proof-sketch boundary;
- expressive equivalence/complementation;
- literal largest-recurring parity;
- Theorems 4.1–4.4 and their unequal proof status; and
- the Section 5 applications.

No test, checker, TeX build, handbook PDF build, or handbook visual pass was
created or run. PDF rendering was used only to read the primary source.
