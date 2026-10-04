# Vardi--Wolper 1986, *An Automata-Theoretic Approach to Automatic Program Verification*: source note

**Disposition:** OFFICIAL/COAUTHOR-INSTITUTIONAL AUTHOR PREPRINT ACQUIRED AND
VISUALLY TRANSCRIBED; PUBLISHED PROCEEDINGS RECORD FIXED; PROCEEDINGS-FILE
COMPARISON OPEN.

## Exact work and accessible source state

- Registered work: Moshe Y. Vardi and Pierre Wolper, “An Automata-Theoretic
  Approach to Automatic Program Verification,” *Proceedings of the First
  Symposium on Logic in Computer Science* (LICS 1986), published by IEEE,
  pp. 322--331, ISBN 0-8186-0720-3.
- The [IEEE CEDA paper page](https://ieee-ceda.org/media/automata-theoretic-approach-automatic-program-verification)
  identifies the work, authors, July 1986 publication, proceedings, abstract,
  and its [full-text PDF](https://ieee-ceda.org/files/ieeeceda/2024-03/lics86.pdf).
- The [ORBi record maintained by the University of Liège](https://orbi.uliege.be/handle/2268/116609),
  Wolper's institution, independently identifies the proceedings presentation,
  publisher, ISBN, event dates, and pp. 322--331. It labels the same 856.27 kB
  file an **author preprint**, not a scan of the printed proceedings.
- Retrieved 2026-08-22. SHA-256 of the acquired PDF:
  28AC190CA9C03AAC2B045195241DC9D1944669A36A55E5E2E2EBCE68267D64A3.
- The PDF has 18 letter-size image-only pages. Its abstract cover is dated
  August 15, 1985. The internal body has its own pagination and is longer than
  the ten-page published proceedings range. It is therefore authoritative
  access to the authors' mathematical presentation, but it is not described
  as a page facsimile of pp. 322--331. No byte- or page-level comparison with
  a separately acquired printed-proceedings file has been made.

The public records and the acquired title page do not append “Preliminary
Report” to the title. That phrase is not retained as though it were part of
the registered title. The paper itself repeatedly promises details “in the
full paper,” so its proof-detail limitations remain visible independently of
the bibliographic title.

## Visual page map

All eighteen file pages were inspected from rendered page images. “Internal
page” below means the number printed by the preprint, not proceedings
pagination.

| PDF pages | Internal location | Inspected content |
|---|---|---|
| 1 | abstract cover | Title, authors and affiliations, abstract, August 15, 1985 date |
| 2--4 | body pp. 1--3 | Introduction; finite-state programs as propositional Kripke structures and infinite-word generators; separation of logical translation from automata operations; PTL grammar begins |
| 5 | body p. 4 | Exact Büchi tuple, run and acceptance; Theorems 2.1--2.2; finite-state program tuple begins |
| 6 | body p. 5 | Program-as-automaton construction; negated-formula product; Lemma 3.1; Theorem 3.2; fairness qualification |
| 7 | body p. 6 | Past connectives; three extended temporal logics; Theorem 3.3 |
| 8--9 | body pp. 7--8 | Markov-chain sequence space and measure-one satisfaction; probabilistic universality/emptiness; Streett acceptance; $TL(F)$ and limit equivalence; Lemmas 4.1--4.2 |
| 10 | body p. 9 | Lemma 4.2 sketch; Theorem 4.3; $k$-limit equivalence; Lemma 4.4; Theorem 4.5 |
| 11 | body p. 10 | $past\text{-}TL(X,F)$ and $TL(Y,S)$; Lemma 4.6; Theorem 4.7; concurrent Markov-chain model begins |
| 12 | body p. 11 | Concurrent probabilistic model completed; conclusion and open questions |
| 13--15 | references pp. 1--3 | Complete preprint references |
| 16--17 | Appendix A pp. 1--2 | Exact future and past PTL clauses; automata as temporal connectives; $ETL_f$, $ETL_l$, and $ETL_r$ acceptance |
| 17--18 | Appendix B pp. 2--3 | Closure; local and eventuality automata; product and projection; modification for past connectives |

## PTL and Büchi semantics

The source's propositional temporal logic is generated from $\mathit{Prop}$ by
Boolean operations, unary next $X$, and binary until $U$. A computation is a
function

\[
 \Pi:\omega\longrightarrow 2^{\mathit{Prop}}.
\]

Appendix A gives the pointed clauses

\[
\begin{aligned}
 \Pi,i\models p
 &\Longleftrightarrow p\in\Pi(i),\\
 \Pi,i\models \xi\land\psi
 &\Longleftrightarrow
   \Pi,i\models\xi\ \text{and}\ \Pi,i\models\psi,\\
 \Pi,i\models\neg\psi
 &\Longleftrightarrow \Pi,i\not\models\psi,\\
 \Pi,i\models X\psi
 &\Longleftrightarrow \Pi,i+1\models\psi,\\
 \Pi,i\models \xi U\psi
 &\Longleftrightarrow
   \exists j\ge i\,
   \bigl(\Pi,j\models\psi\land
         \forall k\,(i\le k<j\Rightarrow\Pi,k\models\xi)\bigr).
\end{aligned}
\]

Thus until permits its right operand at the current point. The source writes
$\Pi\models\varphi$ for truth at point zero.

A Büchi automaton is

\[
 A=(\Sigma,S,\rho,S_0,F),
 \qquad
 \rho:S\times\Sigma\longrightarrow 2^S,
\]

where $S_0\subseteq S$ is the set of starting states and $F\subseteq S$ the
set of designated states. A run on $a_1a_2\cdots$ is $s_0s_1\cdots$, with
$s_0\in S_0$ and $s_i\in\rho(s_{i-1},a_i)$ for every $i\ge1$. It is
accepting when one designated state occurs infinitely often. The automaton is
*semi-deterministic* when

\[
 |\rho(s,a)|\le1
 \quad\text{for every }s\in S,\ a\in\Sigma,
\]

and deterministic when it is semi-deterministic and $|S_0|=1$. These are
source terms with exact standing as restrictions on the automaton's
transition and start data. Semi-determinism differs from determinism only by
permitting several starts, and that distinction is used in Lemma 4.6.

Theorem 2.1, attributed in the paper to WVS83, states that from every PTL
formula $\varphi$ one can build a Büchi automaton $A_\varphi$ over
$2^{\mathit{Prop}}$ such that

\[
 |S|\le 2^{O(|\varphi|)}
 \quad\text{and}\quad
 L(A_\varphi)
 =\{\Pi:\Pi\models\varphi\}.
\]

This is the literal asymptotic source bound formerly missing from the
handbook. Theorem 2.2 separately records two cited automata results: Büchi
emptiness is solvable in linear time, and it is solvable in nondeterministic
logarithmic space. Neither emptiness proof is reproduced.

## Appendix B construction and proof boundary

Appendix B calls its material “Proofs of Theorem 2.1,” but presents a compact
construction rather than a line-by-line language-equality induction. Let
$cl(\varphi)$ contain the subformulas of $\varphi$ and their negations, with
double negation identified, and let $e(\varphi)$ be the set of until formulas
in the closure. The source records

\[
 |cl(\varphi)|\le2|\varphi|.
\]

The local automaton has as states the propositionally consistent sets
$u\subseteq cl(\varphi)$. Its Boolean conditions are

\[
 \psi\in u\Longleftrightarrow\neg\psi\notin u,
 \qquad
 \xi\land\psi\in u
 \Longleftrightarrow
 \xi\in u\ \text{and}\ \psi\in u.
\]

For consecutive local states $u,v$, the temporal transition conditions are

\[
\begin{aligned}
 X\psi\in u
 &\Longleftrightarrow \psi\in v,\\
 \xi U\psi\in u
 &\Longleftrightarrow
   \psi\in u\ \text{or}\
   (\xi\in u\ \text{and}\ \xi U\psi\in v).
\end{aligned}
\]

The starting local states contain $\varphi$. All local states are designated,
because this component enforces only Boolean and consecutive-state
consistency.

The eventuality component has state set $2^{e(\varphi)}$, starts at the empty
set, and designates only the empty set. When its current obligation set is
empty, it collects the until formulas currently unsatisfied; when it is
nonempty, it carries forward each obligation whose right operand has not yet
become true. Büchi recurrence of the empty set forces every collected until
obligation eventually to be discharged.

The product of the local and eventuality components has

\[
 N_M=N_L\times2^{e(\varphi)},
 \qquad
 N_{M0}=N_\varphi\times\{\varnothing\},
 \qquad
 F_M=N_L\times\{\varnothing\},
\]

and the appendix gives the explicit finite bound

\[
 |N_M|
 \le2^{|cl(\varphi)|}2^{|e(\varphi)|}
 \le2^{3|\varphi|}.
\]

This intermediate automaton reads full closure types. Projection sends a
letter $b\subseteq cl(\varphi)$ to $b\cap\mathit{Prop}$, producing the
required alphabet $2^{\mathit{Prop}}$. The construction explains the
theorem's exponential bound and the two distinct obligations: local
consistency and eventual fulfilment. It does not supply a separate worked
input formula or a fully expanded induction proving both language inclusions.

For past operators $Y$ (previous) and $S$ (since), Appendix A gives

\[
\begin{aligned}
 \Pi,i\models Y\psi
 &\Longleftrightarrow i>0\ \text{and}\ \Pi,i-1\models\psi,\\
 \Pi,i\models \xi S\psi
 &\Longleftrightarrow
   \exists j\,(0\le j\le i\land\Pi,j\models\psi\land
   \forall k\,(j<k\le i\Rightarrow\Pi,k\models\xi)).
\end{aligned}
\]

Appendix B adds the corresponding one-step local conditions and initial-state
conditions. Section 3.2 says this extension preserves Theorem 2.1 and its
model-checking bounds.

## Nonprobabilistic finite-state model checking

A finite-state program is

\[
 P=(W,s_0,R,V),
\]

where $W$ is finite, $s_0\in W$, $R\subseteq W^2$ is total, and
$V:W\to2^{\mathit{Prop}}$. Every infinite $R$-path from $s_0$ yields a
computation by reading its state labels. The program satisfies $\varphi$ when
all those computations satisfy $\varphi$.

The source displays the program automaton as

\[
 A_P=(2^{\mathit{Prop}},W,s_0,\rho,W),
\]

with

\[
 s'\in\rho(s,a)
 \Longleftrightarrow
 (s,s')\in R\ \text{and}\ a=V(s).
\]

This display puts the singleton start $s_0$ before $\rho$, whereas the general
tuple puts $\rho$ before the start set $S_0$. The typed data are unambiguous:
alphabet $2^{\mathit{Prop}}$, states $W$, transition $\rho$, start set
$\{s_0\}$, and designated set $W$. Every infinite program run is accepting
because every state is designated.

The required inclusion is

\[
 L(A_P)\subseteq L(A_\varphi).
\]

Instead of complementing $A_\varphi$ automata-theoretically, the paper
constructs $A_{\neg\varphi}$ by Theorem 2.1 and checks

\[
 L(A_P)\cap L(A_{\neg\varphi})=\varnothing.
\]

An accepting word in that intersection is exactly a legal program computation
violating the specification; a violating computation is accepted by both
factors. This is the two-direction correctness argument.

Lemma 3.1, cited to Choueka, states that two Büchi automata with state sets
$S,S'$ have an intersection automaton with $2|S||S'|$ states. When one factor
designates every state, as $A_P$ does, the paper observes that $|S||S'|$
states suffice. Consequently the model-checking automaton has

\[
 |W|\,2^{O(|\varphi|)}
\]

states. Theorem 3.2 then states

\[
\begin{aligned}
 \text{time}&=O(\lVert P\rVert\,2^{O(|\varphi|)}),\\
 \text{space}&=O\bigl((\log\lVert P\rVert+|\varphi|)^2\bigr).
\end{aligned}
\]

The source uses $\lVert P\rVert$ for the finite program's input size. It does
not identify this upper-bound theorem with the separate PSPACE-hardness
argument in Sistla--Clarke. It also notes that a product program
$P_1\times\cdots\times P_k$ can be searched without materializing the full
product, using space quadratic in the sum of the logarithms of the component
sizes.

Fair executions can be represented by giving the program automaton its own
Büchi acceptance condition rather than designating every state. The preprint
says this is easy in the framework but defers elaboration to the full paper.

## Extensions of the temporal language

Section 3.3 uses nondeterministic finite automata as $n$-ary temporal
connectives. Appendix A defines three distinct source logics according to the
acceptance of the connective automaton:

- $ETL_f$: some finite run on a prefix ends in a state in $F$;
- $ETL_l$: some infinite run exists on the word;
- $ETL_r$: some infinite run visits a state in $F$ infinitely often.

The distinctions are needed because finite, merely looping, and recurring
acceptance impose different conditions; each name stands as a formula
language, not as another class of program. The source says the exact analogue
of Theorem 2.1 was already known for $ETL_f$ and $ETL_l$. Its Theorem 3.3,
cited to SVW85, gives for $ETL_r$ an equivalent Büchi automaton with

\[
 |S|\le O(\exp(|\varphi|^2)).
\]

The paper contrasts this quadratic-exponent bound with Theorem 2.1's linear
exponent. It does not reproduce the cited translation proof.

## Probabilistic model and measure-one satisfaction

A labelled Markov chain over $\Sigma$ is

\[
 \Pi=(W,P,w_0,V),
 \qquad
 P:W^2\longrightarrow[0,1],
 \qquad
 \sum_{v\in W}P(u,v)=1,
 \qquad
 V:W\longrightarrow\Sigma.
\]

Its sequence space is $\Psi_\Pi=(\Omega,\Delta,\mu)$, where $\Omega$ contains
the infinite state sequences beginning at $w_0$, $\Delta$ is the Borel field
generated by finite-prefix cylinders, and

\[
 \mu(\Delta(w_0,\ldots,w_n))
 =\prod_{i=0}^{n-1}P(w_i,w_{i+1}).
\]

A probabilistic program uses $\Sigma=2^{\mathit{Prop}}$. For a temporal
formula $\varphi$, let $\Delta(\varphi)$ be the measurable set of state
sequences whose label word satisfies $\varphi$. The source defines

\[
 \Pi\models\varphi
 \Longleftrightarrow
 \mu(\Delta(\varphi))=1.
\]

This is almost-sure satisfaction, not universal-path satisfaction. For an
omega-automaton $B$, the source likewise defines probabilistic universality by
measure one and probabilistic emptiness by measure zero. It says the algorithms
depend only on which transitions have nonzero probability and takes the finite
program size to be the number of nonzero transition-matrix entries.

A Streett automaton has the same alphabet, state, transition, and start data
as the Büchi tuple, but its acceptance component is a finite collection

\[
 \mathcal F\subseteq(2^S)^2.
\]

A run is accepting exactly when, for every $(L,U)\in\mathcal F$, infinite
recurrence of some state in $L$ implies infinite recurrence of some state in
$U$. The pair $(S,F)$ represents Büchi acceptance. Immediately after this
observation, the preprint calls the next conversion “opposite” but its
parenthesis again says “given a Büchi automaton, construct an equivalent
Streett automaton,” while attaching an exponential cost. The literal
parenthesis repeats the already trivial direction and is internally
inconsistent. A faithful account may infer that the intended expensive
direction is Streett-to-Büchi, but must label that as correction of a printed
defect rather than quote the sentence as a clean theorem.

## Restricted probabilistic results and their proof status

Put $F\varphi\equiv\mathit{true}\,U\,\varphi$. The fragment $TL(F)$ permits
only $F$ as temporal connective. For an infinite word $w$, let $let(w)$ be
the letters occurring in $w$ and $lim(w)$ the letters occurring infinitely
often. Two words are *limit equivalent* exactly when

\[
 w=uav,\qquad
 w'=uav',\qquad
 let(av)=lim(w)=lim(w')=let(av')
\]

for some $u\in\Sigma^*$, $a\in\Sigma$, and infinite tails $v,v'$. This is a
relation between infinite words, strictly coarser than word equality; its
distinctive information is needed immediately in Lemma 4.1, which says
limit-equivalent time structures satisfy the same $TL(F)$ formulas at zero.

A computation is *probabilistically fair* when, whenever a state occurs
infinitely often, every positive-probability choice from it is taken
infinitely often. This is a property of a computation, not an assumption that
all paths are scheduled fairly. It differs from unrestricted recurrence by
requiring every available probabilistic branch at a recurrent state, and its
only use here is to represent a positive-measure class by one computation.
The paper expresses the condition by Streett pairs.

Lemma 4.2 reduces probabilistic model checking for $TL(F)$ to Streett
emptiness. Its printed proof is explicitly a sketch: equip the program
automaton with the probabilistic-fairness Streett condition, intersect it with
$A_{\neg\varphi}$, and test emptiness. Theorem 4.3 concludes

\[
 \text{time}=O(\lVert P\rVert\,2^{O(|\varphi|)}).
\]

The paper expressly says it does not know whether Theorem 3.2's space bound
also holds for probabilistic model checking.

For $TL(X,F)$, if a formula has $k-1$ occurrences of $X$, the source replaces
individual letters by length-$k$ subwords. Let
$k\text{-}let(w)$ be the length-$k$ factors occurring in $w$ and
$k\text{-}lim(w)$ those occurring infinitely often. It defines
$k$-limit equivalence exactly when

\[
 w=uxv,\qquad
 w'=uxv',\qquad
 k\text{-}let(xv)=k\text{-}lim(w)
 =k\text{-}lim(w')=k\text{-}let(xv')
\]

for some $u\in\Sigma^*$, $x\in\Sigma^k$, and infinite tails $v,v'$. This
relation differs from ordinary limit equivalence by remembering the finite
window needed for the next operators, and Lemma 4.4 uses that distinction to
preserve truth of the formula. The program is augmented to remember the
preceding computation segment of length $k$. The source defers those details
to the full paper. Theorem 4.5 gives

\[
 \text{time}=O(\lVert P\rVert\,2^{O(|\varphi|^2)})
\]

and says it is unknown whether the bound can be improved.

The fragment $past\text{-}TL(X,F)$ adds $Y,S$ but forbids $X$ or $F$ inside
the scope of $Y$ or $S$. The source notes that it has the same expressive
power as PTL, while the cited translation can be nonelementary. For the
pure-past fragment $TL(Y,S)$, Lemma 4.6 says $A_\varphi$ is
semi-deterministic. Theorem 4.7 then gives

\[
\begin{aligned}
 \text{time}&=O(\lVert P\rVert\,2^{O(|\varphi|)}),\\
 \text{space}&=O\bigl((\log\lVert P\rVert+|\varphi|)^2\bigr).
\end{aligned}
\]

The claimed extension from the pure-past result to all of
$past\text{-}TL(X,F)$ is again deferred to the full paper.

Finally, a concurrent Markov chain is displayed as

\[
 \Pi=(W,N,F,P,w_0,V),
 \qquad
 N\subseteq W,
 \qquad
 F\subseteq N,
 \qquad
 P:W^2\to[0,1],
 \qquad
 w_0\in W,
 \qquad
 V:W\to\Sigma.
\]

For $u\in W\setminus N$, the outgoing probabilities sum to one. For
$u\in N$, the condition $P(u,v)>0$ records a possible nondeterministic
transition rather than its probability. The subset $F$ marks the
nondeterministic states governed by the fair scheduler. The preprint gives the
model but defers the promised model-checking extension; it supplies no theorem
or complete algorithm for concurrent Markov chains.

## Reader-facing disposition

The former open locator condition is closed. The source supports exact PTL,
Büchi, program, Markov, Streett, and restricted-language definitions;
Theorems 2.1--2.2, 3.2--3.3, and 4.3--4.7; the explicit exponential
translation and product bounds; Appendix B's construction; and precise proof
status. The handbook must retain four qualifications:

1. the acquired source is an author preprint, not a proceedings facsimile;
2. published pages are 322--331, while reader locators use PDF/internal
   preprint pages;
3. cited results and matters deferred to a full paper are not promoted to
   proofs in this source;
4. the probabilistic semantics is measure-one satisfaction and is not folded
   into ordinary universal-path emptiness.

The remaining proceedings-file comparison is provenance work only. It does
not leave the acquired mathematical body unread, but it bars claims of exact
printed-page identity.
