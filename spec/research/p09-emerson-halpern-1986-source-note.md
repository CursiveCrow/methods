# Emerson--Halpern (1986), “Sometimes” and “Not Never” Revisited

## Identity, access, and source state

- E. Allen Emerson and Joseph Y. Halpern, “'Sometimes' and 'Not Never'
  Revisited: On Branching versus Linear Time Temporal Logic,” *Journal of the
  Association for Computing Machinery* 33(1) (January 1986), 151--178.
- DOI: <https://doi.org/10.1145/4904.4999>.
- Official institutional record:
  <https://research.ibm.com/publications/sometimes-and-not-never-revisited-on-branching-versus-linear-time-temporal-logic>.
- Complete archived ACM publisher PDF:
  <https://web.archive.org/web/20200603155032id_/https://dl.acm.org/doi/pdf/10.1145/4904.4999?download=true>.
- Local scholarly copy:
  `tmp/pdfs/p09-emerson-halpern-1986/emerson-halpern-1986-acm-archive.pdf`.
- File size: 2,070,143 bytes.
- SHA-256:
  `31C05A055275B10AAF908EED0C7AD4C1E970D029E8C250C89BA428BF884FFF6F`.
- File state: PDF 1.2, 28 pages, 476 by 708 points, unencrypted, untagged;
  PDF metadata records creation on 11 May 1999 and modification on 13 May
  1999. Physical PDF page \(n\) is printed journal page \(150+n\).

The first page contains the JACM title, authors, abstract, journal citation,
ACM copyright line, and the article's copying terms. Those terms permit
fee-free copying only under their stated noncommercial, notice, and
attribution conditions; copying otherwise or republication requires a fee
and/or specific permission. The file is therefore evidence for read-only
scholarly reconstruction, not an open-content licence and not permission to
republish the scan or protected expression.

The first-page note identifies a preliminary paper presented at POPL 1983
under the shorter title “'Sometimes' and 'Not Never' Revisited: On Branching
versus Linear Time.” The 1986 JACM article is the controlling presentation
here. The conference version, the 1984 IBM report, and the 1984 University of
Texas report are distinct source states and are not silently identified with
the journal body.

All 28 pages were rendered at 180 dpi and visually accounted for. Formulae,
figures, theorem statements, and typographic defects were checked against the
page images. The extracted text layer is retained only as a navigation aid at
`tmp/pdfs/p09-emerson-halpern-1986/emerson-halpern-1986-layout.txt`.

## Page map

| PDF pages | Journal pages | Content |
|---:|---:|---|
| 1--3 | 151--153 | abstract; §1; §2.1 structure and path notation; §2.2 syntax |
| 4--5 | 154--155 | §2.3 two Lamport semantics; Definitions 1--2; Theorems 1--2; closure critique; Proposition 1 |
| 6 | 156 | critique of Lamport's two application arguments; start of §3 |
| 7--8 | 157--158 | CTL* typed grammar and semantics; exact sublanguages; Proposition 2 |
| 9--10 | 159--160 | Definitions 3--5; Propositions 3--4; Corollary 1; Theorem 3 |
| 11--12 | 161--162 | Figure 1; Theorems 4--7; Figures 2--3 |
| 13 | 163 | Theorems 8--9; derivation of the expressiveness diagram; further unproved comparisons |
| 14 | 164 | fairness and excluded-middle applications; CTL*-to-PL translation; Proposition 5 |
| 15 | 165 | MPL syntax/semantics; Lemmas 1--2; Theorem 10 |
| 16--17 | 166--167 | relation to TC; §6 application argument; terminal-server example; start of Appendix |
| 18--19 | 168--169 | Appendix proof of Theorem 4; start of continued proof of Theorem 5 |
| 20--21 | 170--171 | end of Theorem 5 proof; Theorem 6 witness; Figures 4--5 |
| 22--25 | 172--175 | Figures 6--8 and Appendix proof of Theorem 7 |
| 26--27 | 176--177 | PL summary; Appendix proof of Lemma 1; start of references |
| 28 | 178 | references and receipt/revision/acceptance dates |

## Structures and Lamport's two readings

Section 2.1 uses a structure

\[
M=(S,X,L),
\]

where \(S\neq\varnothing\) is a state set, \(X\neq\varnothing\) is a set of
nonempty finite or infinite state sequences, and \(L(s)\) is the set of atomic
propositions true at \(s\). A path with \(1+k\) states has length \(k\); an
infinite path has length \(\omega\). The source defines

- \(first(x)\);
- \(x^{succ}\), which removes the first state when possible and otherwise
  leaves a length-zero path fixed;
- \(x^0=x\) and \(x^{m+1}=(x^m)^{succ}\); and
- proper suffixes and the corresponding prefix notions.

These definitions admit finite paths. Later expressiveness results use
\(R\)-generable structures and hence infinite paths; the source explains the
usual convention of extending a finite execution by repeating its terminal
state.

Lamport's shared temporal syntax has atoms, Boolean conjunction/negation, a
primitive \(\Box p\) (“always \(p\)”), and a distinct primitive
\(\rightsquigarrow p\) (“sometimes \(p\)”). The source also defines

\[
\Diamond p:=\neg\Box\neg p
\]

as “not never \(p\).” The wavy-arrow glyph is the paper's primitive
“sometimes”; it must not be silently replaced by \(\Diamond\) before the
semantics have been fixed.

Under the branching reading, formulas are state assertions:

\[
\begin{aligned}
M,s\models_B\Box p
&\Longleftrightarrow
  \forall x\in X\bigl(first(x)=s\Rightarrow
    \forall n\ge 0\;M,first(x^n)\models_Bp\bigr),\\
M,s\models_B\rightsquigarrow p
&\Longleftrightarrow
  \forall x\in X\bigl(first(x)=s\Rightarrow
    \exists n\ge 0\;M,first(x^n)\models_Bp\bigr).
\end{aligned}
\]

Under the linear reading, formulas are assertions about one path:

\[
\begin{aligned}
M,x\models_L\Box p
&\Longleftrightarrow \forall n\ge0\;M,x^n\models_Lp,\\
M,x\models_L\rightsquigarrow p
&\Longleftrightarrow \exists n\ge0\;M,x^n\models_Lp.
\end{aligned}
\]

Thus \(\rightsquigarrow p\) and \(\Diamond p\) coincide on one linear path,
but the branching reading distinguishes universal eventuality from the
existence of a path on which \(p\) is not forever absent.

Definition 1 extends both relations to whole-model validity: every state must
satisfy a branching assertion, while every member of \(X\) must satisfy a
linear assertion. Definition 2 calls formulas under possibly different
interpretations *strongly equivalent* over a structure class when their
whole-model validity agrees on every structure in that class.

Theorems 1--2 quote Lamport's suffix-closed incomparability claims:

1. branching-time \(\Diamond P\) is not strongly equivalent to any linear
   assertion; and
2. linear-time \(\rightsquigarrow\Box P\) is not strongly equivalent to any
   branching assertion.

The paper does not reprint Lamport's proofs. It instead observes that the
first witness class need not be fusion closed and the second need not be limit
closed, then reproves the relevant separations over \(R\)-generable structures
in §4.

Proposition 1 exposes the weakness of whole-model equivalence. The locally
satisfiable conjunction \(\rightsquigarrow P\land\neg P\) is strongly
equivalent to `false`, under either interpretation, because no whole model
makes the conjunction true at every state or path. The proposition is stated
without a separate formal proof; the preceding paragraph supplies its
argument.

## Closure conditions and their standing

The source defines four properties of the path set \(X\):

- *suffix closed*: \(x\in X\Rightarrow x^{succ}\in X\);
- *fusion closed*: if \(x_1sy_1,x_2sy_2\in X\), then \(x_1sy_2\in X\);
- *limit closed*: if every path
  \(x_1y_1,x_1x_2y_2,x_1x_2x_3y_3,\ldots\) lies in \(X\), then its limit
  \(x_1x_2x_3\cdots\) lies in \(X\); and
- *\(R\)-generable*: some total binary relation \(R\subseteq S\times S\)
  generates exactly the infinite \(R\)-paths in \(X\).

These are properties of a structure's admissible computation paths, not new
temporal connectives. For sets of infinite paths, the cited result says
\(R\)-generability is equivalent to suffix, fusion, and limit closure
together. A structure is *state complete* when every state begins some path
in \(X\).

The printed definition of \(R\)-generability on p. 155 says “states from
\(X\),” although \(X\) is a set of paths and the states were defined to come
from \(S\). The tuple and every later use determine the intended \(S\); the
word is recorded as a source typo rather than reproduced as a new type
condition.

## CTL*: typed syntax and exact semantics

Section 3 deliberately separates state formulas from path formulas.

State formulas are generated by:

1. every atom \(P\);
2. \(p\land q\) and \(\neg p\) for state formulas \(p,q\); and
3. \(Ap\) and \(Ep\) for a path formula \(p\).

Path formulas are generated by:

1. every state formula;
2. path-level conjunction and negation;
3. \(Fp\), \(Xp\), and \(pUq\), with separate grammar clauses allowing the
   operands to be state formulas or path formulas; and
4. \(\widetilde Fp\), again with separate state- and path-operand clauses.

The paper reads \(\widetilde Fp\) as “infinitely often \(p\)” and defines
\(\widetilde Gp:=\neg\widetilde F\neg p\), “almost everywhere \(p\).” It also
defines \(Gp:=\neg F\neg p\), \(Ap:=\neg E\neg p\),
\(Fp:=(\mathsf{true}\ U\ p)\), and \(\widetilde Fp:=GFp\). Consequently the
source can take \(E,X,U,\neg,\land\) as primitive. These are source definitions, not a
new handbook nomenclature.

For \(M=(S,X,L)\), a state formula is evaluated at \(s\in S\), and a path
formula is evaluated at a finite or infinite sequence over \(S\). The footnote
on p. 157 is important: path-formula semantics are defined on **all** paths
over \(S\), not only members of \(X\); only \(A\) and \(E\) restrict their
quantification to paths in \(X\) beginning at the current state.

The temporal clauses are current-inclusive for \(F\) and strong \(U\):

\[
\begin{aligned}
x\models Fp
&\Longleftrightarrow \exists i\ge0\;x^i\models p,\\
x\models Xp
&\Longleftrightarrow |x|\ge1\ \land\ x^1\models p,\\
x\models pUq
&\Longleftrightarrow
  \exists i\ge0\bigl(x^i\models q\ \land\
    \forall j<i\;x^j\models p\bigr),\\
x\models\widetilde Fp
&\Longleftrightarrow
  x^i\models p\ \text{for infinitely many distinct }i.
\end{aligned}
\]

When the operand is a state formula, \(x^i\models p\) in these displays means
\(first(x^i)\models p\). At the last state of a finite path, \(Xp\) is false.

The exact named sublanguages are:

- \(L(F)\), \(L(F,U)\), and \(L(F,X,U)\), obtained from path formulas without
  state-level path quantification;
- \(B(F)\), generated by state Boolean operations, \(A/E\), and path-level
  \(F\) applied directly to state formulas;
- \(B(F,X,U)\), adding direct state-formula uses of \(X,U\);
- \(B(F,X,U,\land,\neg)\), adding path-level Boolean combinations; and
- \(B(F,X,U,\widetilde F,\land,\neg)\), adding infinitely-often path
  formulas.

The final-language notation distinguishes path-level Boolean closure from the
Boolean operations already available between state formulas. The source calls
\(B(F,X,U)\) CTL and calls the full set of state formulas CTL*. Formula length
\(|p|\) is the number of symbols in the formula string.

## Translating Lamport's syntax and replacing strong equivalence

For a Lamport temporal formula \(p\), the source defines:

- \(p^L\): replace \(\Box\) by \(G\) and \(\rightsquigarrow\) by \(F\); and
- \(p^B\): replace \(\Box\) by \(AG\) and \(\rightsquigarrow\) by \(AF\).

Proposition 2 states the corresponding pointwise equivalences under the two
old semantics. The source's excluded-middle-in-time example becomes

\[
FP\lor G\neg P
\]

on a linear path, but \(AFP\lor AG\neg P\) under the old branching reading.
The former is valid and the latter is not. The correctly typed branching
assertion of the linear principle is \(A(FP\lor G\neg P)\).

Definition 3 associates with a path language \(L\) the state language

\[
B(L)=\{Ap:p\in L\}.
\]

The source warns that this set is not closed under semantic negation or
disjunction. Definition 4 replaces whole-model strong equivalence by ordinary
pointwise equivalence of state formulas over every state of every structure in
the chosen class.

Proposition 3 proves, for every path formula \(p\), that whole-model \(p\) is
strongly equivalent to \(Ap\). For the class \(\mathcal F\) of fusion-closed,
state-complete structures, Proposition 4 proves

\[
p\equiv_s^{\mathcal F}q
\quad\Longleftrightarrow\quad
AGp\equiv^{\mathcal F}AGq
\]

for state formulas \(p,q\). The forward direction restricts a fusion-closed
model to all states occurring on paths from the chosen state; the reverse
direction uses state completeness to recover \(q\) at every state. The source
then gives exact counterexamples showing that both hypotheses are needed:

- without fusion closure,
  \(p=P\land EFEX\neg P\), \(q=\mathsf{false}\); and
- without state completeness,
  \(p=AGEF\mathsf{true}\land EF\mathsf{true}\),
  \(q=(AGEF\mathsf{true}\land EF\mathsf{true})\lor AG\mathsf{false}\).

Corollary 1 states the mixed path/state version:

\[
p\equiv_s^{\mathcal F}q
\quad\Longleftrightarrow\quad
AGAp\equiv^{\mathcal F}AGq.
\]

Definition 5 then defines “at least as expressive,” “exactly as expressive,”
and “strictly less expressive” by pointwise state-formula equivalence. Those
relations are metalinguistic comparisons between languages, not formulas of
CTL*.

## The expressiveness results

Section 4 works over \(R\)-generable structures. The authors say the same
proofs work unchanged for suffix-closed, fusion-closed structures, but leave
that check to the reader.

Figure 1 has the following exact edges:

\[
\begin{array}{ccccc}
B(L(F,X,U))&<&CTL^*&&\\
\rotatebox{90}{$<$}&&\rotatebox{90}{$>$}&&\\
B(L(F,U))&&B(F,X,U,\widetilde F,\land,\neg)&&\\
\rotatebox{90}{$<$}&&\rotatebox{90}{$>$}&&\\
B(L(F))&<&B(F,X,U,\land,\neg)&&\\
&&\rotatebox{90}{$=$}&&\\
&&B(F,X,U)&&\\
&&\rotatebox{90}{$>$}&&\\
&&B(F).&&
\end{array}
\]

In prose, the eight labelled arcs are:

1. \(B(F,X,U,\widetilde F,\land,\neg)<CTL^*\);
2. \(B(F,X,U,\land,\neg)<B(F,X,U,\widetilde F,\land,\neg)\);
3. \(B(F,X,U)=B(F,X,U,\land,\neg)\);
4. \(B(F)<B(F,X,U)\);
5. \(B(L(F))<B(F,X,U,\widetilde F,\land,\neg)\);
6. \(B(L(F,X,U))<CTL^*\);
7. \(B(L(F,U))<B(L(F,X,U))\); and
8. \(B(L(F))<B(L(F,U))\).

Any pair not joined by a chain of \(<\) and \(=\) edges is asserted to be
incomparable. The source derives the strictness and missing-edge claims from
Theorems 3--9; the diagram is not a mere syntactic-containment chart.

### Theorem 3

The \(B(F)\) formula \(EFP\) is not equivalent to any
\(B(L(F,X,U))\) formula. The printed proof uses a two-state
\(R\)-generable model with

\[
R=\{(s_1,s_1),(s_1,s_2),(s_2,s_2)\},
\qquad s_1\models\neg P,\quad s_2\models P,
\]

and its one-state restriction to \(s_1\). The existential possibility \(EFP\)
is true at \(s_1\) in the first model and false in the restriction. A formula
\(Aq\) true before deleting paths remains true after the deletion, yielding
the contradiction. This is a complete short source proof.

### Theorem 4

\[
B(L(F))\le B(F,X,U,\widetilde F,\land,\neg).
\]

The Appendix supplies the announced induction. It defines a set \(B\) of
basic linear formulas: propositional formulas; finite segment forms

\[
[p_1,\ldots,p_n]
:=p_1U(p_2U\cdots(p_{n-1}UGp_n)\cdots);
\]

\(GFp\) for propositional \(p\); and a displayed family
\(F(p\land\text{segments}\land Fr_1\land\cdots\land Fr_n)\). It lets
\(B^+\) be the conjunction/disjunction closure and proves by structural
normalization that every \(F/G\) path formula has an equivalent in \(B^+\).

For \(Ep\), the proof first merges conjunctions of segment formulas by
disjoining over consistent interleavings. It handles the case with no nested
\(Fr\) by nested \(E[\_U\_]\) formulas, then inducts on the number of nested
\(F\)-subformulas by choosing which \(r_i\) is met first and in which segment.
The Appendix prints the normalization identities and both induction steps.
It uses no \(X\), so the later remark observes that the proof lands inside
the displayed rich branching language even after every \(X\)-forming clause
is removed. Theorem 3 supplies strictness of the relevant edge.

The introduction's pointer “cf. Theorem 4.2” on p. 153 has no matching
numbered theorem in the article. The result is numbered **Theorem 4** on
p. 161 and proved under that number on pp. 167--169.

### Theorem 5

The displayed theorem statement literally says that the formula

\[
A[F(P\land XP)]
\]

is not equivalent to any
\(B(L(F,X,U,\widetilde F,\land,\neg))\) formula. That target cannot be the
proof-supported result: the displayed witness is itself \(Aq\) for the linear
path formula \(q=F(P\land XP)\), hence belongs to the named
associated linear language under the paper's own Definition 3 and grammar.

The proof instead establishes nondefinability in
\(B(F,X,U,\widetilde F,\land,\neg)\). Figures 2--3 define families
\(M_i,N_i\), and the three proof obligations are:

1. \(M_i,a_i\models A[F(P\land XP)]\), while
   \(N_i,a_i\models\neg A[F(P\land XP)]\);
2. over these model families, every
   \(B(F,X,U,\widetilde F,\land,\neg)\) formula has an equivalent
   \(B(F,X,U)\) formula; and
3. every \(B(F,X,U)\) formula \(p\) with \(|p|\le i\) agrees at the two
   roots.

The Appendix proves (3) by induction using \(EXq\), \(E[qUr]\), and
\(A[qUr]\) as primitive modal cases. It proves (2) by observing that every
path in the witnesses ends in a self-loop at \(d\), reducing the
\(\widetilde F/\widetilde G\) obligations to an \(EFAG\) condition, and then
invoking “Theorem 9” for Boolean-path elimination. That invocation is another
printed cross-reference defect: the needed equality is Theorem 8(a),
\(B(F,X,U)=B(F,X,U,\land,\neg)\); Theorem 9 instead separates linear \(U\) and
\(X\) from weaker linear languages. Atomic, conjunction, and negation cases
are left to the reader. The proof is substantial but depends on the cited
Theorem 8(a) equality and is not fully self-contained.

Figure 1 and the paragraph on p. 163 confirm the proof-supported reading:
they say arc 1,
\[
B(F,X,U,\widetilde F,\land,\neg)<CTL^*,
\]
follows from Theorem 5. No erratum correcting the extra printed \(L(\cdot)\)
was located on the official ACM/IBM or author-publication surfaces inspected.
The handbook must therefore print both statuses: the literal theorem target
is defective, while the proof and its announced use establish the target
without \(L(\cdot)\).

### Theorem 6

\[
E[((P_1UP_2)\lor(Q_1UQ_2))UR]
\]

is likewise printed as not equivalent to any
\(B(L(F,X,U,\widetilde F,\land,\neg))\) formula. The proof does not address
that target. Figures 4--5 define the separating \(M_i,N_i\) families and print
every atomic label; the Appendix's obligation (2) again quantifies over
\(B(F,X,U,\widetilde F,\land,\neg)\) formulas, reduces them to
\(B(F,X,U)\) on the witnesses, and combines that reduction with root
indistinguishability. It therefore supports nondefinability in the rich
branching language, with no \(L(\cdot)\) in the target. The Appendix says the
remaining induction follows exactly the same lines as Theorem 5 and leaves
those details to the reader. This is a witness construction and proof
reduction, not a complete repeated induction.

### Theorem 7


\[
E\widetilde FP
\]

is not equivalent to any \(B(F,X,U,\land,\neg)\) formula. Figures 6--8
define two ladder-like model families. The Appendix proves that beyond a
formula's length, truth at the \(c_j\) states is either eventually everywhere
or nowhere, and likewise for the \(d_j\) states. A second induction shows that
the \(M_i\) roots \(a_i,b_i\) and \(N_i\) roots \(c_i,d_i\) agree on every
\(B(F,X,U)\) formula of length at most \(i\). Theorem 8(a) then transfers the
indistinguishability to path-level Boolean closure, while
\(E\widetilde FP\) separates the roots. The source prints all three modal
cases; Boolean cases are left to the reader, and Theorem 8(a) is cited rather
than reproved.

### Theorems 8--9 and the completed diagram

Theorem 8 is attributed to the authors' earlier work [9]:

\[
B(F,X,U)=B(F,X,U,\land,\neg),
\]

and \(E(PUQ)\) is not equivalent to any \(B(F)\) formula. Theorem 9 is
attributed to Process Logic [16]: \(PUQ\) is not equivalent to any \(L(F)\)
formula, and \(XP\) is not equivalent to any \(L(F,U)\) formula. Neither
proof is reproduced.

The paragraph excluding additional arcs says that the dual of the Theorem 6
witness is expressible in \(B(L(F,X,U))\) but not in the rich branching
language “by Theorem 7.” That citation is internally mismatched: Theorem 7
concerns \(E\widetilde FP\), whereas the proof-supported target of Theorem 6,
together with closure of the rich branching language under state negation,
is the dependency that excludes the dual. The three aligned source signals
are therefore: remove the extra \(L(\cdot)\) from the printed targets of
Theorems 5--6, and read the later “Theorem 7” as “Theorem 6.” The reader
reconstruction records every printed form before giving this
proof-and-diagram-supported repair.

The final §4 remark lists further comparisons whose details are omitted. It
observes that \(AXP\) needs an explicit \(X\); cites [10] for the separation
by \(E(FP\land FQ)\); strengthens Theorem 4 because its proof used no \(X\);
and says techniques from [9] give
\(B(F,U)=B(F,U,\land,\neg)\). These remarks are not additional full proofs in
this paper.

## The source's two application formulae

The strong-eventual-fairness assertion in Lamport's notation is translated
to the typed branching assertion

\[
A(\widetilde G\neg enabled\lor Fexecuted).
\]

Here \(\widetilde G\neg enabled\) means that enabledness occurs only finitely
often. The assertion therefore says: if the process is enabled infinitely
often, execution eventually occurs. It is an example of the additional
infinitely-often modality, not a fairness premise built into the structure.

The linear principle \(FP\lor G\neg P\) becomes

\[
A(FP\lor G\neg P).
\]

The source also gives the less transparent CTL equivalent

\[
\neg E[\neg P\ U\ (P\land EGP)].
\]

This example demonstrates expressibility; it is not a state-labelling
algorithm or a complexity result.

## Relation to PL

For a CTL* structure \(M=(S,X,L)\), §5 associates a PL path model in which an
atomic program \(A\) denotes exactly \(X\), and atomic labels agree. Taking
\(E,X,U\) as primitive, the translation is printed as

\[
\begin{aligned}
P'&=P, & (\neg p)'&=\neg p', & (p\land q)'&=p'\land q',\\
(pUq)'&=q'\lor(p'\mathbin{\mathrm{suf}}q'),
& (Ep)'&=\mathsf f(\langle A\rangle p'),
& (Xp)'&=\mathsf{false}\mathbin{\mathrm{suf}}p'.
\end{aligned}
\]

The \(\mathsf f\) operator tests the unique length-zero initial prefix;
\(\mathrm{suf}\) quantifies over a proper suffix, and
\(\mathsf n p:=\mathsf{false}\mathbin{\mathrm{suf}}p\) is the PL next-time analogue.
Proposition 5 asserts preservation for all path formulas on \(x\in X\) and
all state formulas at \(s\in S\). The article calls its proof a
straightforward structural induction; it does not print the cases.

The Appendix summarizes the needed test-free PDL program operations,
path fusion, \(\mathsf f\), and \(\mathrm{suf}\). That summary belongs to the proof
support for Proposition 5; it does not turn this paper into a complete
presentation of Process Logic.

## Relation to MPL and a literal-source defect

MPL formulas are atoms closed under \(\neg,\land,\Diamond,X,U\), with
\(\Box p:=\neg\Diamond\neg p\). They are evaluated at triples \(M,x,y\),
where \(x\in X\) and the *stage* \(y\) is a finite prefix of \(x\). Prefix
order is written \(y\le z\).

As literally printed on p. 165, the relevant clauses are

\[
\begin{aligned}
M,x,y\models pUq
\Longleftrightarrow{}&
\exists z\bigl(y\le z\le x\land M,x,z\models q\\
&\qquad\land
  \forall w(y\le w\le z\Rightarrow M,x,w\models p)\bigr),\\
M,x,y\models Xp
\Longleftrightarrow{}&
\exists z\bigl(M,x,z\models p\land y\le z\le x\\
&\qquad\land\neg\exists w(y<w<z)\bigr),\\
M,x,y\models\Diamond p
\Longleftrightarrow{}&
\exists x'\in X\bigl(y\le x'\land M,x',y\models p\bigr).
\end{aligned}
\]

The non-strict inequalities are visible in the page image. Read literally,
they conflict with the CTL* clauses printed on p. 158 and with the claimed
translation:

- CTL* \(pUq\) permits \(q\) now while \(p\) is false; printed MPL \(pUq\)
  also requires \(p\) at the endpoint \(z=y\).
- CTL* \(Xp\) requires a successor; printed MPL \(Xp\) permits \(z=y\)
  because there is no stage strictly between a stage and itself.

These are semantic differences, not cosmetic typography. On a one-state path
whose only stage satisfies \(q\land\neg p\), CTL* \(pUq\) is true with
witness \(i=0\), while the printed MPL formula is false. On a two-state path
with \(p\) true only at the first state, printed MPL \(Xp\) is true by
choosing the current stage, whereas CTL* \(Xp\) is false. The paper supplies
no erratum or local reconciliation. The proof-supported intended clauses
would require \(p\) only before \(z\) and \(z\) to be a proper successor for
\(X\), but the handbook must label any such repair rather than attribute it
to the display.

The source makes the closure restrictions mathematically substantive. It
gives

\[
EGX\mathsf{true}\land\neg EXEGX\mathsf{true}
\]

as a CTL* formula satisfiable only outside suffix-closed structures, and

\[
EFEFp\land\neg EFp
\]

as one satisfiable only outside fusion-closed structures. It contrasts these
examples with Lemma 1: every pointed MPL model has a satisfaction-equivalent
point in a structure possessing both closure properties.

Lemma 1 says every pointed MPL model \(M,x,y\) has a satisfaction-equivalent
point in a suffix-closed, fusion-closed structure. Its Appendix proof first
keeps only paths extending \(y\), unwinds them into a fresh-state tree, closes
under suffix, and preserves truth by induction. In the uncountable case the
authors say the construction appears to require well-ordering, hence the
axiom of choice.

Lemma 2 says that in suffix-closed, fusion-closed structures, truth at stage
\(y\) agrees with truth at the first stage of the suffix \(x/y\). The paper
gives the closure-dependent modal step and leaves the structural induction's
details to the reader.

Theorem 10 says that, on suffix-closed, fusion-closed structures, replacing
every CTL* \(E\) by MPL \(\Diamond\) preserves both path-formula and
state-formula truth. The claim is presented after Lemma 2 without a further
proof. Because the printed MPL \(U/X\) clauses differ from the CTL* clauses,
the theorem cannot be reported as following from the literal displays
without the repair just described.

The final paragraph compares CTL*, MPL, and Lehmann--Shelah's TC. TC replaces
\(A\) by a measure-one path operator. The paper says TC and MPL are known to
have the same complete axiomatizations and therefore the same valid and
satisfiable formulas; it then says one would *expect* a translation from CTL*
or MPL to TC. It does not construct or prove that translation.

## Conclusion: application argument, not theorem

Section 6 argues that linear time is often adequate and simpler for manual
verification of a preexisting concurrent program when the desired assertion
is universal over executions. It then gives three reasons to retain explicit
branching:

1. model checking on finite global-state graphs;
2. closure under negation, which \(B(L)=\{Aq:q\in L\}\) lacks; and
3. specifications that must require the existence of alternative
   nondeterministic computation paths.

The terminal-server example requires, while process \(P_i\) is in its
noncritical section, both a path that remains there and a path that reaches
the trying region, while every path either remains or eventually tries:

\[
EG(inNCS_i)\land EF(inTRY_i)\land
A(G(inNCS_i)\lor F(inTRY_i)).
\]

The natural linear candidate
\(A(G(inNCS_i)\lor F(inTRY_i))\) permits a degenerate model in which every
path eventually tries and no path remains in \(NCS_i\) forever. The example
therefore gives the existential path quantifier an actual specification use;
it does not prove that branching logic is uniformly preferable.

The paper connects explicit path quantification to synthesis and to excluding
single-path degenerate implementations. Its final recommendation is to use
the CTL* fragment appropriate to the application's expressiveness and
decision complexity. The article itself concentrates on expressiveness and
refers elsewhere for satisfiability and finite-model truth complexity. It
does not present a CTL/CTL* model-checking algorithm, a general complexity
bound, or a synthesis correctness theorem.

## Proof-status matrix

| Item | Locator | Source proof status |
|---|---|---|
| Theorems 1--2 | p. 154 | Lamport results restated; proofs not reproduced |
| Proposition 1 | p. 155 | argument in preceding prose; no separate proof block |
| Proposition 2 | p. 158 | called clear from the translation; no proof block |
| Proposition 3 | p. 159 | complete short proof |
| Proposition 4 | pp. 159--160 | proof printed in both directions; assumptions separately tested |
| Corollary 1 | p. 160 | stated from Propositions 3--4; no proof block |
| Theorem 3 | p. 160 | complete short separating-model proof |
| Theorem 4 | pp. 161, 167--169 | full Appendix normalization/induction, with routine checks implicit |
| Theorem 5 | pp. 161--162, 169--170 | printed \(B(L(\cdot))\) target is self-defeating; proof and Figure 1 support \(B(F,X,U,\widetilde F,\land,\neg)\); substantial Appendix induction, Boolean cases left to reader; printed “Theorem 9” dependency must be Theorem 8(a) |
| Theorem 6 | pp. 162, 170--171 | same printed-target/proof mismatch; proof supports the rich branching target; witness and invariants printed, remaining induction explicitly left to reader |
| Theorem 7 | pp. 162, 172--175 | substantial Appendix proof; Boolean cases left to reader; uses cited Theorem 8 |
| Theorems 8--9 | p. 163 | cited from [9] and [16]; no proofs here |
| Proposition 5 | p. 164 | translation stated; structural induction asserted but not printed |
| Lemma 1 | pp. 165, 176--177 | full Appendix construction with an uncountable-case qualification |
| Lemma 2 | p. 165 | induction asserted; closure-dependent step explained; details left to reader |
| Theorem 10 | p. 165 | stated after Lemma 2; no separate proof; literal MPL clauses conflict with direct translation |

## Historical reader-facing disposition

The 1986 journal body is complete and page-authenticated at the archived ACM
publisher state. Its path structures, closure hypotheses, both Lamport
semantics, CTL* typed grammar and semantics, named sublanguages, equivalence
repair, Figure 1 taxonomy, Theorems 3--9 and witness invariants, PL/MPL
relations, source defects, proof boundaries, and terminal-server application
are sufficient for an exact reader-facing reconstruction.

The reconstruction must not:

- infer a CTL state-labelling algorithm from this expressiveness paper;
- identify CTL with arbitrary universally prefixed LTL;
- copy the scan or protected prose;
- promote cited or reader-delegated proof steps to full local proofs;
- silently repair the printed targets of Theorems 5--6 or their later
  Theorem 7 cross-reference;
- report Theorem 10 without the printed MPL \(U/X\) tension; or
- turn the §6 recommendation into a theorem about all verification tasks.

No test, checker, TeX build, or handbook-PDF build was created or run while
preparing this source note. Source rendering was used only for read-only
scholarship.

## Current manuscript correction, 2026-09-06

A new primary-page check also corrected this note's own transcription:
Theorem 5 uses ordinary F in A[F(P and X P)]. The earlier tilde-F
reading was not the source's formula. The corrected base models and
recursive construction are recorded in
p09-emerson-halpern-theorem5-correction-note.md. The reader text now
supplies that construction and the induction establishing its separating
property.

The user's current instruction is to fix mathematical errors in the book
itself. The historical restrictions above on repairing printed targets and
MPL clauses no longer govern the reader text. This note retains the literal
source readings as provenance.

The active N-c-016 presentation now states Theorems 5 and 6 with the rich
branching target B(F,X,U,tilde F,and,not). The proof discussion invokes
Theorem 8(a) for Boolean-path elimination and Theorem 6 for the dual
separation. The false extra L constructor and the source's erroneous
cross-references have been removed from the mathematical exposition.

The MPL definition now requires p strictly before the q-stage for p U q,
and a proper immediate successor for X p. Stages and the quantified prefix
variables are nonempty finite prefixes. Atoms and Boolean clauses are
explicit. The presentation supplies a simultaneous structural induction
proving the CTL* translation on suffix-closed, fusion-closed path structures,
including the terminal finite-path case and truncation of until witnesses
at the final actual position. The existential path case proves both the
suffix and fusion implications. It also derives the MPL suffix lemma.
The state-formula conclusion is stated at states starting a path in X;
state completeness yields the conclusion at every state.

The R-generability characterization now has a direct two-way proof with
state completeness. Its forward construction uses dependent choice in the
ambient metatheory to obtain paths from totality. Its reverse construction
defines R by initial edges, extends finite prefixes by fusion, and uses
limit closure. The incomplete three-property wording and mistyped state
domain remain documented earlier in this research note.
