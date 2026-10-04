# Baier--Katoen 2008, *Principles of Model Checking*, Chapter 6: source note

**Registered presentation:** `N-c-016.e`, Christel Baier and Joost-Pieter
Katoen, *Principles of Model Checking*, Chapter 6, “Computation Tree Logic.”

**Disposition:** COMPLETE PUBLISHED BOOK BODY ACQUIRED FROM TWO INSTITUTIONAL
HOSTS; THE TWO RETRIEVED FILES ARE BYTE-IDENTICAL. THE REQUESTED CTL,
EXPRESSIVENESS, MODEL-CHECKING, AND CTL* SURFACES HAVE BEEN PAGE-MATCHED.
PUBLIC DOWNLOAD SUPPORTS READ-ONLY SCHOLARSHIP, NOT REPUBLICATION OF THE BOOK.

## Bibliographic identity and controlling source object

Christel Baier and Joost-Pieter Katoen, *Principles of Model Checking*.
Cambridge, Massachusetts, and London: The MIT Press, 2008. ISBN
978-0-262-02649-9. The publisher identity surface is the
[MIT Press book record](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/).
No book DOI is printed in the acquired body or exposed by the cited publisher
record.

The complete body used for this note was independently retrieved on 22 August
2026 from both institutional routes already registered for this presentation:

| Institutional route | HTTP state observed 22 August 2026 | Bytes | Physical PDF pages | SHA-256 |
|---|---|---:|---:|---|
| [LaBRI, Universite de Bordeaux](https://www.labri.fr/perso/anca/Verif/Baier-Katoen.pdf) | `200 OK`, `application/pdf`; `Last-Modified: Tue, 16 Jan 2018 12:05:52 GMT` | 5,767,528 | 994 | `C190470BD8E085FC8B83B147E68218BD7DE9ADFC20603C4595DABAEA7E75D37B` |
| [IFMO institutional copy](https://is.ifmo.ru/books/_principles_of_model_checking.pdf) | `200 OK`, `application/pdf`; `Last-Modified: Tue, 22 Oct 2019 14:34:48 GMT` | 5,767,528 | 994 | `C190470BD8E085FC8B83B147E68218BD7DE9ADFC20603C4595DABAEA7E75D37B` |

The identical hashes establish that these are two access routes to the same
PDF object, not two editions or source states. PDF metadata gives title
*Principles of Model Checking*, authors Baier and Katoen, Acrobat Distiller
7.0.5 for Macintosh, creation 7 February 2008, modification 27 June 2008,
PDF 1.5, page size approximately 576 by 720 points, no encryption, and no
document tagging. The Arabic book pagination has the exact mapping

\[
  \text{physical PDF page}=\text{printed page}+19.
\]

Thus printed p. 313 is physical PDF p. 332, printed p. 341 is physical PDF
p. 360, and printed p. 424 is physical PDF p. 443.

The copyright leaf, physical PDF p. 5, says copyright Massachusetts Institute
of Technology and “All rights reserved,” and requires publisher permission for
reproduction. It contains no Creative Commons or other open-content licence.
Anonymous institutional download permits inspection and ordinary source use;
it is not evidence of permission to redistribute the PDF, page images, or a
substantial transcription. This note therefore records definitions, formulae,
algorithm steps, proof boundaries, and brief source-critical observations for
read-only scholarship. It does not reproduce the chapter.

## Corrected locator map

The locator ranges in the earlier lot note are directionally useful but need
the following exact corrections before they are used in reader-facing prose.

| Requested range | What the published book actually contains |
|---|---|
| printed pp. 311--312 | The end of Chapter 5 exercises, not CTL syntax or semantics |
| printed p. 313 | Chapter 6 title and §6.1 introduction begin |
| printed pp. 317--319 | §6.2.1, CTL syntax, legal formulae, and derived modalities |
| printed pp. 320--329 | §6.2.2, CTL state/path semantics, examples, weak until, negation, and terminal-state adaptation |
| printed pp. 329--334 | §6.2.3 equivalence and §6.2.4 normal forms; §6.3 begins on p. 334 |
| printed pp. 334--341 | §6.3, CTL versus LTL expressiveness; §6.4 begins partway down p. 341 |
| printed pp. 341--357 | Most of §6.4, including Algorithms 13--16, Theorems 6.23 and 6.30, and Examples 6.26 and 6.28 |
| printed p. 358 | The final equivalence calculation of Example 6.31; §6.5 then begins. The table of contents correctly locates §6.5 at p. 358, so §6.4 does not end on p. 357. |
| printed pp. 417--421 | The end of §6.7.4, symbolic CTL model checking, not CTL* |
| printed p. 422 | §6.8 and §6.8.1 on CTL* begin |
| printed pp. 422--425 | CTL* syntax and semantics, Theorems 6.83--6.84, Figure 6.27, and the beginning of the equivalence discussion |
| printed p. 427 | §6.8.2 CTL* model checking begins; it is outside the requested surface |

The exact relevant contents page is printed p. ix. It locates Chapter 6 at
p. 313, §6.2 at p. 317, §6.3 at p. 334, §6.4 at p. 341, §6.5 at p. 358,
§6.7 at p. 381, and §6.8 at p. 422.

## Definitions inherited by Chapter 6

Chapter 6 does not introduce a smaller unlabeled Kripke tuple. It uses the
book's earlier action-labelled transition-system tuple, then ignores action
names when CTL truth depends only on direct state successors. The following
definitions are therefore part of the Chapter 6 presentation and must be
supplied before its syntax and algorithms are reconstructed.

### Transition systems, finiteness, successors, and terminal states

Definition 2.1, printed p. 20, defines

\[
  TS=(S,Act,\mathord\to,I,AP,L),
\]

where:

- \(S\) is the state set;
- \(Act\) is the action set;
- \(\to\subseteq S\times Act\times S\) is the transition relation;
- \(I\subseteq S\) is the set of initial states;
- \(AP\) is the set of atomic propositions; and
- \(L:S\to 2^{AP}\) is the labelling function.

The source calls \(TS\) finite exactly when \(S\), \(Act\), and \(AP\) are
finite. It explicitly permits \(I=\varnothing\); in that case the system has
no initial behaviour. This matters because the later clause
\(TS\models\Phi\) universally quantifies over \(I\) and is therefore vacuous
when \(I\) is empty.

Definition 2.3, printed p. 23, defines

\[
  Post(s,\alpha)=\{s'\in S\mid s\xrightarrow{\alpha}s'\},\qquad
  Post(s)=\bigcup_{\alpha\in Act}Post(s,\alpha),
\]

and dually \(Pre(s,\alpha)\) and \(Pre(s)\). The pointwise extensions to
sets are also defined. Definition 2.4 on the same page says that \(s\) is
terminal exactly when \(Post(s)=\varnothing\).

The book does not introduce “total transition system” as a Chapter 6
technical term. Its literal standing hypothesis is **without terminal
states**. In the notation just defined, this is exactly

\[
  \forall s\in S\;\bigl(Post(s)\ne\varnothing\bigr).
\]

This condition is not merely presentational. It makes every maximal path
fragment starting at any state infinite, supplies the successor needed in the
greatest-set argument of Theorem 6.23(g), and is inherited by the CTL and CTL*
semantics. Section 6.4 adds the independent hypothesis that \(TS\) is finite.

### Path fragments and paths

Definition 3.4, printed pp. 95--96, defines a finite path fragment as a state
sequence \(s_0s_1\ldots s_n\) with \(s_i\in Post(s_{i-1})\) for
\(0<i\le n\), and an infinite path fragment as
\(s_0s_1s_2\ldots\) with the analogous condition for every \(i>0\).
For an infinite fragment \(\pi=s_0s_1\ldots\), the source defines

\[
 first(\pi)=s_0,\qquad \pi[j]=s_j,\qquad
 \pi[..j]=s_0\ldots s_j,\qquad \pi[j..]=s_js_{j+1}\ldots.
\]

Definition 3.5, printed p. 96, defines a maximal path fragment as either an
infinite path fragment or a finite one ending in a terminal state. An initial
path fragment begins in \(I\). The same page defines
\(Paths(s)\) as the maximal path fragments whose first state is \(s\), and
\(Paths_{fin}(s)\) as all finite path fragments beginning at \(s\).
Definition 3.6 then reserves “path of \(TS\)” for an initial, maximal path
fragment and writes \(Paths(TS)\) for all such paths.

Accordingly, Chapter 6's \(\pi\in Paths(s)\) need not begin in a system
initial state. It begins in the state at which the CTL state formula is being
evaluated. Under the no-terminal-state hypothesis, every member of
\(Paths(s)\) is infinite.

## CTL syntax, standing, and derived operators

### Definition 6.1, printed pp. 317--318

For a fixed set \(AP\), the primitive state-formula grammar is

\[
  \Phi ::= true\mid a\mid \Phi_1\land\Phi_2\mid\neg\Phi
          \mid\exists\varphi\mid\forall\varphi,
  \qquad a\in AP,
\]

and the primitive path-formula grammar is

\[
  \varphi ::= \bigcirc\Phi\mid \Phi_1\mathbin{U}\Phi_2.
\]

The source uses capital Greek letters for CTL state formulae and lower-case
Greek letters for CTL path formulae. A state formula is a statement evaluated
at a state. A path formula is a statement evaluated on a maximal path
fragment. A temporal operator in CTL must be immediately under a path
quantifier in order to yield a state formula. Boolean combinations and nested
temporal operators do not occur at the CTL path-formula level. This is the
syntactic restriction later relaxed by CTL*.

Example 6.2, printed p. 318, uses the restriction to distinguish legal
formulae such as

\[
  \exists\bigcirc(x=1),\quad
  \forall\bigcirc(x=1),\quad
  \exists((x<2)\ U\ (x\ge3)),\quad
  \forall(true\ U\ (x<2))
\]

from illegal strings such as
\(\exists(x=1\land\forall\bigcirc(x\ge3))\) and
\(\exists\bigcirc(true\ U\ (x=1))\). It then shows that putting the relevant
state formula beneath \(\bigcirc\), or putting a path quantifier before the
until expression, restores well-formedness.

The source says that the usual propositional operators are derived in the
usual way. Its displayed temporal abbreviations on printed p. 318 are exact:

\[
\begin{aligned}
  \exists\Diamond\Phi &:= \exists(true\ U\ \Phi),
  &\forall\Diamond\Phi &:= \forall(true\ U\ \Phi),\\
  \exists\Box\Phi &:= \neg\forall\Diamond\neg\Phi,
  &\forall\Box\Phi &:= \neg\exists\Diamond\neg\Phi.
\end{aligned}
\]

The pronunciations given there are “potentially” for
\(\exists\Diamond\), “inevitable” for \(\forall\Diamond\), “potentially
always” for \(\exists\Box\), and “invariantly” for \(\forall\Box\).
Printed p. 319 stresses that \(\exists\neg\Diamond\neg\Phi\) is not legal CTL;
the definition of \(\exists\Box\Phi\) must switch the path quantifier as
shown above.

Remark 6.9, printed pp. 327--328, defines weak until by

\[
\begin{aligned}
 \exists(\Phi\ W\ \Psi)
   &:=\neg\forall((\Phi\land\neg\Psi)\ U\ (\neg\Phi\land\neg\Psi)),\\
 \forall(\Phi\ W\ \Psi)
   &:=\neg\exists((\Phi\land\neg\Psi)\ U\ (\neg\Phi\land\neg\Psi)).
\end{aligned}
\]

It proves the expected path meaning and in particular

\[
 \exists(\Phi\ W\ \Psi)
   \equiv \exists(\Phi\ U\ \Psi)\lor\exists\Box\Phi.
\]

Printed p. 334 also defines release, for the positive-normal-form discussion,
by

\[
 \exists(\Phi\ R\ \Psi):=\neg\forall((\neg\Phi)\ U\ (\neg\Psi)),
 \qquad
 \forall(\Phi\ R\ \Psi):=\neg\exists((\neg\Phi)\ U\ (\neg\Psi)).
\]

### Definitions 6.4--6.5, printed pp. 320--321

Let \(TS=(S,Act,\to,I,AP,L)\) have no terminal states. For
\(s\in S\), state formulae \(\Phi,\Psi\), and path formula \(\varphi\),
Definition 6.4 gives the state clauses

\[
\begin{aligned}
s\models a &\iff a\in L(s),\\
s\models\neg\Phi &\iff s\not\models\Phi,\\
s\models\Phi\land\Psi &\iff s\models\Phi\text{ and }s\models\Psi,\\
s\models\exists\varphi &\iff
  \text{some }\pi\in Paths(s)\text{ satisfies }\varphi,\\
s\models\forall\varphi &\iff
  \text{every }\pi\in Paths(s)\text{ satisfies }\varphi,
\end{aligned}
\]

and, for \(\pi=s_0s_1s_2\ldots\), the path clauses

\[
\begin{aligned}
 \pi\models\bigcirc\Phi
   &\iff \pi[1]\models\Phi,\\
 \pi\models\Phi\ U\ \Psi
   &\iff \exists j\ge0\;\bigl(
       \pi[j]\models\Psi\ \land\
       \forall k\,(0\le k<j\Rightarrow\pi[k]\models\Phi)
     \bigr).
\end{aligned}
\]

The until semantics is non-strict: \(j=0\) is permitted, so the left operand
need not hold when the initial state already satisfies the right operand.

Definition 6.5 sets

\[
  Sat_{TS}(\Phi)=\{s\in S\mid s\models\Phi\}
\]

and defines system satisfaction by

\[
  TS\models\Phi
  \iff \forall s_0\in I\;(s_0\models\Phi)
  \iff I\subseteq Sat(\Phi).
\]

The derived path readings are then

\[
\begin{aligned}
s\models\exists\Box\Phi
 &\iff \exists\pi\in Paths(s)\;\forall j\ge0\;(\pi[j]\models\Phi),\\
s\models\forall\Box\Phi
 &\iff \forall\pi\in Paths(s)\;\forall j\ge0\;(\pi[j]\models\Phi),
\end{aligned}
\]

with the analogous existential and universal eventuality readings.

Remark 6.8, printed pp. 326--327, gives a two-direction proof that

\[
s\models\forall\Box\forall\Diamond a
\iff
\text{every }\pi\in Paths(s)\text{ visits }a\text{-states infinitely often}.
\]

The reverse direction explicitly splices an arbitrary continuation from
\(\pi[j]\) onto the prefix through \(\pi[j]\); this is why merely showing
that one selected continuation revisits \(a\) would not suffice.

Remark 6.11, printed p. 329, separately explains the change needed if terminal
states are retained. For a finite maximal fragment
\(\pi=s_0\ldots s_n\), it makes \(\bigcirc\Phi\) true only when \(n>0\)
and \(s_1\models\Phi\), and bounds the until witness by \(j\le n\). Under
that alternative convention, \(s\models\forall\bigcirc false\) exactly at a
terminal state. This is an adaptation, not the standing semantics used by the
algorithms requested below.

## Equivalence, expansion laws, and existential normal form

Definition 6.12, printed p. 329, calls CTL formulae equivalent when their
satisfaction sets agree in every transition system over the same \(AP\).
Figure 6.5, printed p. 330, records the duality, expansion, and selected
distribution laws used later. The essential expansion laws are

\[
\begin{aligned}
\exists(\Phi\ U\ \Psi)
 &\equiv \Psi\lor(\Phi\land\exists\bigcirc\exists(\Phi\ U\ \Psi)),\\
\forall(\Phi\ U\ \Psi)
 &\equiv \Psi\lor(\Phi\land\forall\bigcirc\forall(\Phi\ U\ \Psi)),\\
\exists\Diamond\Phi
 &\equiv \Phi\lor\exists\bigcirc\exists\Diamond\Phi,\\
\forall\Diamond\Phi
 &\equiv \Phi\lor\forall\bigcirc\forall\Diamond\Phi,\\
\exists\Box\Phi
 &\equiv \Phi\land\exists\bigcirc\exists\Box\Phi,\\
\forall\Box\Phi
 &\equiv \Phi\land\forall\bigcirc\forall\Box\Phi.
\end{aligned}
\]

Definition 6.13, printed p. 332, defines existential normal form (ENF) by

\[
 \Phi ::= true\mid a\mid\Phi_1\land\Phi_2\mid\neg\Phi
       \mid\exists\bigcirc\Phi
       \mid\exists(\Phi_1\ U\ \Phi_2)
       \mid\exists\Box\Phi.
\]

The standing of ENF is syntactic: it is a class of CTL state formulae. It is
not a new semantics or a new model class.

Theorem 6.14, printed pp. 332--333, states that every CTL formula has an
equivalent ENF formula. Its printed proof is a rewrite proof outline, not a
line-by-line structural induction. It supplies exactly these two eliminations:

\[
\begin{aligned}
 \forall\bigcirc\Phi
   &\equiv\neg\exists\bigcirc\neg\Phi,\\
 \forall(\Phi\ U\ \Psi)
   &\equiv
     \neg\exists(\neg\Psi\ U\ (\neg\Phi\land\neg\Psi))
     \land\neg\exists\Box\neg\Psi.
\end{aligned}
\]

The source says the second rewrite triples occurrences of the right operand
and therefore an explicit CTL-to-ENF translation can be exponentially larger
than its input. This warning is essential to the later complexity statement:
one must not first materialize that exponential translation and then claim
Theorem 6.30's linear dependence on the original formula.

Printed p. 333 also lists derived rewrites. The first is correct:

\[
  \forall\Diamond\Phi\equiv\neg\exists\Box\neg\Phi.
\]

The second line begins correctly with
\(\forall\Box\Phi\equiv\neg\exists\Diamond\neg\Phi\) but then literally
prints \(=\neg\exists(true\ U\ \Phi)\), dropping the negation on \(\Phi\).
The internally supported expansion, forced by the first equality and by the
definitions on pp. 318 and 330, is

\[
  \forall\Box\Phi
  \equiv\neg\exists\Diamond\neg\Phi
  =\neg\exists(true\ U\ \neg\Phi).
\]

The reader must not reproduce the last printed term without this defect
record.

Definition 6.15 and Theorem 6.16, printed pp. 333--334, give positive normal
form and its existence proof. They require negation only before atoms and use
\(W\) as the dual of \(U\). The proof gives the relevant negation-pushing
laws and again warns of possible exponential growth. These items are adjacent
source context; ENF, not PNF, controls Algorithms 13--16.

## CTL and LTL expressiveness

### Definition 6.17 and Theorem 6.18

Definition 6.17, printed p. 334, defines equivalence between a CTL formula
\(\Phi\) and LTL formula \(\varphi\) by agreement of
\(TS\models\Phi\) and \(TS\models\varphi\) for every transition system over
the same \(AP\). This is system-level equivalence under the book's respective
state interpretations, not equality of a CTL satisfaction set with a language
of isolated words.

Theorem 6.18, printed p. 335 and attributed there to Clarke and Draghicescu,
states: if \(\varphi\) is obtained from CTL formula \(\Phi\) by deleting all
path quantifiers, then either \(\Phi\equiv\varphi\), or no LTL formula is
equivalent to \(\Phi\). The proof is expressly omitted. Consequently, later
uses of this criterion inherit a cited-but-unproved step in this textbook
surface.

### Lemmas 6.19--6.20 and their concrete systems

Lemma 6.19, printed pp. 335--336, separates
\(\forall\Diamond\forall\Box a\) from the LTL formula
\(\Diamond\Box a\). Its transition system has initial state \(s_0\), labels

\[
  L(s_0)=\{a\},\qquad L(s_1)=\varnothing,\qquad L(s_2)=\{a\},
\]

and edges

\[
 s_0\to s_0,\quad s_0\to s_1,\quad s_1\to s_2,\quad s_2\to s_2.
\]

Every path from \(s_0\) eventually remains forever at either \(s_0\) or
\(s_2\), so the LTL formula holds. The path \(s_0^\omega\) never reaches a
state satisfying \(\forall\Box a\), because \(s_0\) still has a route through
the non-\(a\) state \(s_1\). Hence the CTL formula fails. The lemma itself
only proves non-equivalence of those two displayed formulae; the subsequent
no-equivalent-LTL conclusion also uses unproved Theorem 6.18.

Lemma 6.20, printed pp. 336--337, similarly separates

\[
 \forall\Diamond(a\land\forall\bigcirc a)
 \quad\text{from}\quad
 \Diamond(a\land\bigcirc a).
\]

Figure 6.6 has initial state \(s_0\), labels

\[
L(s_0)=L(s_1)=L(s_4)=\{a\},\qquad
L(s_2)=L(s_3)=\varnothing,
\]

and edges

\[
s_0\to s_1,\ s_1\to s_2,\ s_2\to s_2,
\qquad
s_0\to s_3,\ s_3\to s_4,\ s_4\to s_0.
\]

Every path satisfies the LTL formula: the \(s_0s_1\) branch satisfies it at
\(s_0\), and the \(s_0s_3s_4s_0\) branch satisfies it at \(s_4\). The path
\(s_0s_1s_2^\omega\) never reaches a state satisfying
\(a\land\forall\bigcirc a\), so the CTL formula fails. Again, the stronger
non-definability conclusion uses Theorem 6.18.

### Theorem 6.21, printed pp. 337--340

Theorem 6.21 states both directions of incomparability.

1. LTL formulae with no equivalent CTL formula include
   \(\Diamond\Box a\) and \(\Diamond(a\land\bigcirc a)\).
2. CTL formulae with no equivalent LTL formula include
   \(\forall\Diamond\forall\Box a\),
   \(\forall\Diamond(a\land\forall\bigcirc a)\), and
   \(\forall\Box\exists\Diamond a\).

The proof status is uneven and must not be flattened into “full proof.”

#### Witness family for \(\Diamond\Box a\notin CTL\)

For \(AP=\{a\}\), Figure 6.7 defines the base systems:

- \(TS_0\) has initial \(s_0\) labelled \(\varnothing\), state \(t_0\)
  labelled \(\{a\}\), and edges
  \(s_0\to t_0\), \(t_0\to t_0\), and \(t_0\to s_0\).
- \(TS'_0\) has initial \(s'_0\) labelled \(\varnothing\), state \(t'_0\)
  labelled \(\{a\}\), and edges
  \(s'_0\to t'_0\) and \(t'_0\to t'_0\).

For \(n>0\), Figure 6.8 and its text add fresh \(s_n,t_n\) or
\(s'_n,t'_n\) around a copy of \(TS'_{n-1}\). All \(s\)-states have empty
labels and all \(t\)-states have label \(\{a\}\). The edges added to the
unprimed member are

\[
s_n\to t_n,\qquad t_n\to t_n,\qquad
t_n\to s'_{n-1},\qquad t_n\to s_n,
\]

while the primed member omits the return to its new empty-labelled state:

\[
s'_n\to t'_n,\qquad t'_n\to t'_n,\qquad
t'_n\to s'_{n-1}.
\]

Thus \(TS_n\not\models\Diamond\Box a\), witnessed by
\((s_nt_n)^\omega\), while every initial path of \(TS'_n\) eventually stays
at some \(t'_i\), so \(TS'_n\models\Diamond\Box a\).

The proof then asserts that, for every \(n\), no CTL formula of length at most
\(n\) distinguishes \(TS_n\) from \(TS'_n\). The induction proving this key
bounded-formula claim is explicitly left to the reader. The final formula-
length contradiction is printed. The second LTL witness
\(\Diamond(a\land\bigcirc a)\) is said to follow similarly, and its proof is
omitted.

The printed family definition has two local defects that must be resolved from
Figures 6.7--6.8 and the surrounding prose:

- on p. 338 the tuple whose components are all primed is printed with
  \(TS_n\) rather than \(TS'_n\) on the left of the equality; and
- the inductive transition display is presented under \(n\ge0\) and mentions
  \(s'_{n-1}\), although \(s'_{-1}\) is never defined. Figure 6.7 separately
  gives the two base systems, so the only coherent reading is: use Figure 6.7
  at \(n=0\), and use the displayed inductive clauses for \(n>0\).

#### Witness systems for \(\forall\Box\exists\Diamond a\notin LTL\)

Figure 6.10(a), printed p. 340, has initial state \(s\) with empty label, a
self-loop at \(s\), an edge \(s\to s'\), and an \(a\)-labelled state \(s'\)
with a self-loop. It satisfies \(\forall\Box\exists\Diamond a\). Figure
6.10(b) is the subsystem consisting only of the empty-labelled self-loop at
\(s\), and it does not satisfy that CTL formula.

If an LTL formula \(\varphi\) were equivalent to the CTL formula, the first
system would satisfy \(\varphi\). Its path \(s^\omega\), the sole path of the
second system, would therefore satisfy \(\varphi\), forcing the second system
to satisfy \(\varphi\), a contradiction. This is the complete intended
trace-inclusion argument.

The printed proof contains a consequential formula defect. After correctly
assuming that \(\varphi\) is equivalent to
\(\forall\Box\exists\Diamond a\), p. 340 literally says
\(\varphi\equiv\forall\Diamond\exists\Diamond a\). The inference and both
figures require
\(\varphi\equiv\forall\Box\exists\Diamond a\). The diamond in that one
printed occurrence must not be carried into the reader.

For the other two CTL witnesses, Theorem 6.21(b) refers back to Lemmas 6.19
and 6.20 and Theorem 6.18. Their concrete separating systems are printed, but
the general criterion on which non-definability rests remains proof-omitted in
this book.

## CTL model checking: exact input, output, and Algorithms 13--16

Section 6.4 begins on printed p. 341 with two standing assumptions:

- \(TS\) is finite and has no terminal states; and
- the core presentation computes with an ENF formula, whose temporal cases
  are \(\exists\bigcirc\), \(\exists U\), and \(\exists\Box\).

The section immediately recommends implementing universal and other derived
operators directly instead of materializing the potentially exponential ENF
translation. The output \(Sat(\Phi)\) is global: it classifies every state,
not only the initial states. System satisfaction is the final test
\(I\subseteq Sat(\Phi)\).

### Algorithm 13, printed p. 342

Algorithm 13's input is a finite \(TS\) and CTL formula \(\Phi\), both over
\(AP\); its output is the truth value of \(TS\models\Phi\). Its exact control
structure is:

1. for each formula length \(i\le |\Phi|\);
2. for every subformula \(\Psi\in Sub(\Phi)\) of length \(i\);
3. compute \(Sat(\Psi)\) from the already computed satisfaction sets of its
   maximal genuine subformulae; and
4. return whether \(I\subseteq Sat(\Phi)\).

The accompanying text identifies this with a bottom-up traversal of the parse
tree. For an ENF formula, inner nodes are labelled by
\(\neg,\land,\exists\bigcirc,\exists U,\exists\Box\). Once a satisfaction
set is known, the exposition describes replacing that subformula by a fresh
atomic proposition whose label is present exactly at those states. Example
6.22, printed p. 343, illustrates this on

\[
  \exists\bigcirc a\ \land\ \exists(b\ U\ \exists\Box\neg c).
\]

Algorithm 13 is a skeleton. Algorithms 14--16 supply the set operations and
the two nontrivial temporal searches.

### Theorem 6.23, printed pp. 343--345

For a transition system without terminal states, Theorem 6.23 gives these
exact characterizations:

\[
\begin{array}{ll}
(a)&Sat(true)=S,\\
(b)&Sat(a)=\{s\in S\mid a\in L(s)\},\\
(c)&Sat(\Phi\land\Psi)=Sat(\Phi)\cap Sat(\Psi),\\
(d)&Sat(\neg\Phi)=S\setminus Sat(\Phi),\\
(e)&Sat(\exists\bigcirc\Phi)
   =\{s\in S\mid Post(s)\cap Sat(\Phi)\ne\varnothing\}.
\end{array}
\]

It characterizes \(Sat(\exists(\Phi\ U\ \Psi))\) as the least
\(T\subseteq S\) such that

\[
 Sat(\Psi)\subseteq T,
 \qquad
 s\in Sat(\Phi)\land Post(s)\cap T\ne\varnothing\Rightarrow s\in T,
\]

and \(Sat(\exists\Box\Phi)\) as the greatest \(T\subseteq S\) such that

\[
 T\subseteq Sat(\Phi),
 \qquad
 s\in T\Rightarrow Post(s)\cap T\ne\varnothing.
\]

“Least” and “greatest” are explicitly with respect to set inclusion.

The proof labels (a)--(e) straightforward and does not expand them. It gives
two-part proofs for the last two clauses. For until, the expansion law proves
closure, and a finite backwards induction along an until-witness path proves
minimality. For existential always, the expansion law proves the two
conditions, and repeated selection of a successor in \(T\) constructs a path
staying in \(T\), proving maximality. This latter construction explicitly
uses the absence of terminal states. Finiteness is not stated in Theorem 6.23
itself; it is required by the terminating algorithms that iterate these
characterizations.

Remark 6.24, printed pp. 345--347, restates the two temporal clauses as least
and greatest fixed points of

\[
 F\equiv\Psi\lor(\Phi\land\exists\bigcirc F),
 \qquad
 F\equiv\Phi\land\exists\bigcirc F,
\]

and gives the universal counterparts by replacing existential successor with
the condition \(Post(s)\subseteq T\).

Remark 6.25, printed p. 347, correctly gives the greatest-set clauses for weak
until, but its displayed universal expansion literally reads

\[
 \forall(\Phi\ W\ \Psi)
 \equiv \Psi\lor(\Psi\land\forall\bigcirc\forall(\Phi\ W\ \Psi)).
\]

The second \(\Psi\) is a printed defect. The correct operand is forced by the
path semantics on pp. 327--328 and by the correct set clause on p. 347:

\[
 \forall(\Phi\ W\ \Psi)
 \equiv \Psi\lor(\Phi\land\forall\bigcirc\forall(\Phi\ W\ \Psi)).
\]

### Algorithm 14, printed p. 348

Algorithm 14 takes a finite transition system with state set \(S\) and an ENF
formula \(\Phi\), and returns \(Sat(\Phi)\). In normalized mathematical
pseudocode, preserving every source branch, it performs:

```text
Sat(true)                    := S
Sat(a)                       := {s in S | a in L(s)}
Sat(Phi1 and Phi2)           := Sat(Phi1) intersect Sat(Phi2)
Sat(not Psi)                 := S minus Sat(Psi)
Sat(exists next Psi)         := {s in S | Post(s) intersects Sat(Psi)}

T := Sat(Phi2)
while some s in Sat(Phi1) minus T has a successor in T:
    choose one such s
    T := T union {s}
return T                     // exists(Phi1 U Phi2)

T := Sat(Phi)
while some s in T has no successor in T:
    choose one such s
    T := T minus {s}
return T                     // exists always Phi
```

The source presents the branches inside one switch over \(\Phi\). The set
computations for operands are recursive/bottom-up calls already governed by
Algorithm 13.

### Algorithm 15 and Example 6.26, printed pp. 349--351

For \(\exists(\Phi\ U\ \Psi)\), printed p. 348 defines the increasing
approximants

\[
T_0=Sat(\Psi),\qquad
T_{i+1}=T_i\cup\{s\in Sat(\Phi)\mid Post(s)\cap T_i\ne\varnothing\}.
\]

Finiteness makes this chain stabilize at the least set of Theorem 6.23(f).
Algorithm 15 realizes the same computation once per relevant edge, assuming
inverse adjacency lists:

```text
E := Sat(Psi)
T := E
while E is nonempty:
    choose s' in E
    remove s' from E
    for every s in Pre(s'):
        if s is in Sat(Phi) minus T:
            add s to E
            add s to T
return T
```

Example 6.26 uses Figure 6.11. The state labels are

\[
\begin{array}{c|cccccccc}
s&s_0&s_1&s_2&s_3&s_4&s_5&s_6&s_7\\\hline
L(s)&\{a,b,c\}&\{a,b\}&\{b,c\}&\{a\}&\{b\}&\{a,c\}&\{c\}&\varnothing,
\end{array}
\]

the initial marker is at \(s_1\), and the directed edges reconstructed from
the figure are

\[
\begin{gathered}
s_0\to s_2,\quad
s_1\to s_3,\quad
s_2\to s_0,\ s_2\to s_1,\quad
s_3\to s_0,\\
s_4\to s_0,\ s_4\to s_1,\quad
s_5\to s_1,\ s_5\to s_7,\quad
s_6\to s_4,\quad
s_7\to s_3,\ s_7\to s_6.
\end{gathered}
\]

The checked formula is

\[
 \exists\Diamond\Theta=\exists(true\ U\ \Theta),
 \qquad
 \Theta=((a=c)\land(a\ne b)).
\]

The truth-value comparisons select \(Sat(\Theta)=\{s_4,s_5\}\). The source's
selection order is: remove \(s_5\), whose predecessor set is empty; process
\(s_4\) and add \(s_6\); process \(s_6\) and add \(s_7\); then process
\(s_7\), whose relevant predecessor is already visited. Thus Figure 6.12's
black sets progress

\[
\{s_4,s_5\}
\subset
\{s_4,s_5,s_6\}
\subset
\{s_4,s_5,s_6,s_7\},
\]

and the final satisfaction set is
\(\{s_4,s_5,s_6,s_7\}\). Example 6.26 is an execution trace of the algorithm,
not a separately proved theorem.

### Algorithm 16 and Examples 6.27--6.28, printed pp. 351--355

For \(\exists\Box\Phi\), the source first gives the decreasing iteration

\[
T_0=Sat(\Phi),\qquad
T_{i+1}=T_i\cap\{s\in Sat(\Phi)\mid Post(s)\cap T_i\ne\varnothing\}.
\]

Algorithm 16 implements deletion with successor counts:

```text
E := S minus Sat(Phi)
T := Sat(Phi)
for each s in Sat(Phi): count[s] := |Post(s)|

while E is nonempty:
    choose s' in E
    remove s' from E
    for every s in Pre(s'):
        if s is in T:
            count[s] := count[s] - 1
            if count[s] = 0:
                remove s from T
                add s to E
return T
```

The printed loop invariant is
\(count[s]=|Post(s)\cap(T\cup E)|\). Each extracted state is removed from
\(T\cup E\), so decrementing its predecessors maintains that invariant.

One pseudocode comment on p. 352 is stale: beside “let \(s'\in E\)” it says
\(s'\not\models\Phi\). That is true of the initial members of \(E\), but
later \(E\) also contains states removed from \(T\) that may satisfy
\(\Phi\) while failing \(\exists\Box\Phi\). The operative invariant and the
algorithm are consistent; the comment should read that
\(s'\not\models\exists\Box\Phi\), not necessarily
\(s'\not\models\Phi\).

Example 6.27 runs Algorithm 16 on Figure 6.11 for
\(\exists\Box b\). It starts with

\[
T_0=\{s_0,s_1,s_2,s_4\},\quad
E=\{s_3,s_5,s_6,s_7\},\quad
count=[1,1,2,1,2,2,1,2].
\]

After processing \(s_3\), state \(s_1\) is removed. Processing
\(s_6,s_7,s_1,s_5\) in the source's order decrements the relevant counters
but removes no further state. The returned set is
\(\{s_0,s_2,s_4\}\).

Example 6.28 presents the alternative strongly-connected-component
calculation for the same formula. The restriction \(TS[b]\) has states
\(\{s_0,s_1,s_2,s_4\}\) and only the edges among those states:

\[
s_0\to s_2,\quad
s_2\to s_0,\quad s_2\to s_1,\quad
s_4\to s_0,\quad s_4\to s_1.
\]

Its sole nontrivial strongly connected component is \(\{s_0,s_2\}\).
State \(s_4\) can reach that component; \(s_1\) cannot. Hence the alternative
method returns the same set
\(Sat(\exists\Box b)=\{s_0,s_2,s_4\}\).

The prose cross-references on p. 354 are off by one subfigure: the black SCC
is Figure 6.13(c), not 6.13(b), and the completed backward-reachability result
is Figure 6.13(d), not 6.13(c). The page image makes the intended sequence
unambiguous.

Theorem 6.29, printed pp. 354--355, justifies the alternative method for a
finite transition system:

\[
s\models\exists\Box\Phi
\iff
s\models\Phi\text{ and a nontrivial SCC of }TS[\Phi]
\text{ is reachable from }s.
\]

It prints both directions: an infinite \(\Phi\)-path in a finite graph yields
a repeatedly traversed cycle; conversely, a reachable nontrivial SCC supplies
a cycle that can be repeated forever. Example 6.28 is therefore supported by
a printed general theorem, not merely by the picture.

## Theorem 6.30 and the exact complexity boundary

Section 6.4.3, printed p. 355, fixes the parameters and representation
hypotheses before stating Theorem 6.30:

- \(TS\) is finite, with \(N\) states and \(K\) transitions;
- the section-wide no-terminal-state hypothesis remains in force;
- predecessor sets \(Pre(s)\) are stored as linked lists;
- Algorithms 15 and 16 then take \(O(N+K)\) time;
- the bottom-up parse-tree traversal is linear in \(|\Phi|\); and
- if initial states are stored in a linked list, testing
  \(I\subseteq Sat(\Phi)\) costs \(O(N_0)\), where \(N_0=|I|\).

Theorem 6.30 states

\[
  \text{time}(TS\models\Phi)
    \in O\bigl((N+K)\,|\Phi|\bigr).
\]

The theorem is preceded by the derivation just listed rather than followed by
a separately labelled proof. Its linear formula dependence is for direct
handling of the CTL modalities. The source explicitly warns that first
expanding arbitrary CTL into ENF can be exponential and recommends analogous
direct algorithms for \(\forall U\), \(\forall\Diamond\),
\(\forall\Box\), \(\exists\Diamond\), and weak until. Those direct set
algorithms remain linear in \(N+K\).

The heading says “Time and Space Complexity,” but the requested pp. 355--357
print no separate asymptotic space theorem or explicit space bound. A reader
may infer storage costs from satisfaction sets, predecessor lists, work sets,
and counters, but such an inference must not be attributed as an expressly
stated Baier--Katoen theorem.

Printed pp. 355--358 also qualify the comparison with LTL. Linear dependence
on a CTL formula does not mean that CTL is uniformly more efficient for the
same property: LTL can be exponentially more succinct. Example 6.31 gives an
explicit disjunction over all vertex permutations for a CTL Hamiltonian-path
formula and finishes its equivalence argument on p. 358. This succinctness
qualification is separate from the correctness and runtime of Algorithms
13--16.

## CTL*: syntax, semantics, embedding, and strictness

Section 6.8 begins on printed p. 422, not p. 417. Printed pp. 417--421 complete
the symbolic CTL discussion in §6.7.4. The relevant CTL* surface in the
requested range is therefore pp. 422--425.

### Definitions 6.80--6.82, printed pp. 422--423

Definition 6.80 gives the CTL* state grammar

\[
  \Phi ::= true\mid a\mid\Phi_1\land\Phi_2\mid\neg\Phi\mid\exists\varphi
\]

and the CTL* path grammar

\[
  \varphi ::= \Phi\mid\varphi_1\land\varphi_2\mid\neg\varphi
             \mid\bigcirc\varphi\mid\varphi_1\ U\ \varphi_2.
\]

Thus an arbitrary CTL* state formula may be used as an elementary path
formula, and Boolean and temporal operators may be nested at path level. The
source derives

\[
 \Diamond\varphi:=true\ U\ \varphi,
 \qquad
 \Box\varphi:=\neg\Diamond\neg\varphi,
 \qquad
 \forall\varphi:=\neg\exists\neg\varphi.
\]

It explicitly contrasts the last definition with CTL: in CTL*, because path
negation is legal, the universal path quantifier can be derived without the
operator-by-operator dual constructions required by CTL.

For a transition system without terminal states, Definition 6.81 gives the
same state clauses for atoms, negation, conjunction, and existential path
quantification as before. For \(\pi=s_0s_1\ldots\), its path clauses are

\[
\begin{aligned}
\pi\models\Phi &\iff s_0\models\Phi,\\
\pi\models\varphi_1\land\varphi_2
  &\iff \pi\models\varphi_1\text{ and }\pi\models\varphi_2,\\
\pi\models\neg\varphi &\iff \pi\not\models\varphi,\\
\pi\models\bigcirc\varphi &\iff \pi[1..]\models\varphi,\\
\pi\models\varphi_1\ U\ \varphi_2
 &\iff \exists j\ge0\;\bigl(
    \pi[j..]\models\varphi_2\land
    \forall k(0\le k<j\Rightarrow\pi[k..]\models\varphi_1)
   \bigr).
\end{aligned}
\]

Definition 6.82 retains the state satisfaction set and all-initial-states
system semantics:

\[
 Sat(\Phi)=\{s\in S\mid s\models\Phi\},
 \qquad
 TS\models\Phi\iff\forall s_0\in I\;(s_0\models\Phi).
\]

### Theorem 6.83, printed p. 424

For every transition system without terminal states, LTL formula
\(\varphi\), and state \(s\), Theorem 6.83 states

\[
 s\models_{LTL}\varphi
 \iff
 s\models_{CTL^*}\forall\varphi.
\]

In particular,

\[
 TS\models_{LTL}\varphi
 \iff
 TS\models_{CTL^*}\forall\varphi.
\]

The page prints no labelled proof after the theorem. The preceding paragraph
supplies the reason: LTL path formulae are the CTL* path formulae whose
elementary state formulae are restricted to atoms, and LTL state semantics
already universally quantifies over \(Paths(s)\). This is a direct
definition-matching argument, not an automata translation and not a CTL*
model-checking result.

### Theorem 6.84, printed pp. 424--425

Over \(AP=\{a,b\}\), Theorem 6.84 uses the well-typed CTL* state formula

\[
  \Phi=
  (\forall\Diamond\Box a)\lor
  (\forall\Box\exists\Diamond b)
\]

and states that no LTL formula and no CTL formula is equivalent to \(\Phi\).
The first disjunct is the universal CTL* closure of the LTL persistence
formula \(\Diamond\Box a\); the second is the CTL formula already separated
from LTL in Theorem 6.21.

The printed proof is one sentence: it cites the two non-definability facts
from Theorem 6.21 and says the result follows directly. It prints no new
transition systems and does not spell out why a disjunction inherits both
separations. The missing elementary step is closure under substituting a
constant truth value for an atom:

- on systems where \(a\) is false at every state, the first disjunct is false,
  so an equivalent LTL formula would yield an LTL definition of
  \(\forall\Box\exists\Diamond b\); and
- on systems where \(b\) is false at every state, the second disjunct is
  false, so an equivalent CTL formula would yield a CTL definition of the
  state interpretation of \(\Diamond\Box a\).

This substitution argument is an explicit reconstruction of the omitted
justification, not prose printed in the source. The source witnesses reused by
Theorem 6.84 are therefore the \(TS_n,TS'_n\) family for
\(\Diamond\Box a\) and Figure 6.10's two systems for
\(\forall\Box\exists\Diamond b\), with the indicated atom names. There is no
separate pair of “CTL* strictness systems” on pp. 424--425.

Figure 6.27, printed p. 425, depicts LTL and CTL as overlapping proper parts
of CTL*. It places \(\Diamond(a\land\bigcirc a)\) in the LTL-only region,
\(\Box\Diamond a\) in the overlap, and
\(\forall\Box\exists\Diamond a\) in the CTL-only region. Its outer-region
display is
\(\Diamond(a\land\bigcirc a)\lor\forall\Box\exists\Diamond a\).
Taken literally under Definition 6.80, that display is a CTL* path formula,
not a state formula, unless universally closed; Theorem 6.84's separately
quantified formula is the safe, well-typed strictness theorem to cite.

## Requested numbered items: exact proof-status matrix

| Item | Printed locator | Exact role | Proof status in the acquired book |
|---|---:|---|---|
| Theorem 6.14 | 332--333 | Every CTL formula has an equivalent ENF formula | Rewrite proof outline using two universal-elimination laws; no explicit structural induction; adjacent derived `forall always` expansion has a dropped negation |
| Theorem 6.18 | 335 | Quantifier-erasure criterion for a CTL formula that has any LTL equivalent | Proof expressly omitted and attributed to Clarke--Draghicescu |
| Lemma 6.19 | 335--336 | `forall eventually forall always a` differs from LTL `eventually always a` | Concrete three-state proof printed; non-definability conclusion additionally uses proof-omitted Theorem 6.18 |
| Lemma 6.20 | 336--337 | `forall eventually (a and forall next a)` differs from LTL `eventually (a and next a)` | Concrete five-state proof printed; non-definability conclusion additionally uses Theorem 6.18 |
| Theorem 6.21 | 337--340 | CTL and LTL are expressively incomparable | One infinite-family argument with key bounded-formula induction left to reader; second LTL witness omitted as similar; two CTL witnesses delegated to Lemmas 6.19--6.20 and Theorem 6.18; `forall always exists eventually a` trace argument printed but contains one wrong modality in the assumed equivalence |
| Algorithm 13 | 342 | Bottom-up global CTL satisfaction-set skeleton | Pseudocode and parse-tree explanation printed; depends on later set computations |
| Theorem 6.23 | 343--345 | Satisfaction-set clauses and least/greatest set characterizations | Clauses (a)--(e) called straightforward; detailed minimality/maximality arguments printed for existential until and existential always |
| Algorithm 14 | 348 | Recursive ENF satisfaction-set computation | Complete switch-level pseudocode printed; naive fixed-point loops |
| Example 6.26 | 349--350 | Backward search for existential eventuality on Figure 6.11 | Worked sequence printed; no separate proof claim |
| Algorithm 15 | 351 | Edge-linear predecessor worklist for existential until | Complete pseudocode printed; termination/correctness derived immediately before it from finite least-set iteration |
| Algorithm 16 | 352 | Count-based deletion worklist for existential always | Complete pseudocode and invariant explanation printed; one comment incorrectly says every extracted work item falsifies the operand itself |
| Example 6.28 | 354 | SCC alternative for existential always | Worked computation printed; two wrong subfigure references; supported by Theorem 6.29's printed two-direction proof |
| Theorem 6.30 | 355 | CTL model checking in `O((N+K)|Phi|)` time | Complexity derivation precedes theorem; inherits finite/no-terminal and predecessor-list hypotheses and direct-modality implementation warning |
| Theorem 6.83 | 424 | LTL state semantics embeds as universal CTL* path quantification | No labelled proof; direct semantic correspondence explained immediately before theorem |
| Theorem 6.84 | 424 | One CTL* formula has neither an LTL nor a CTL equivalent | One-sentence appeal to Theorem 6.21; no new systems and no explicit substitution argument |

## Printed defects and source-critical qualifications

| Location | Literal issue | Required evidentiary treatment |
|---|---|---|
| p. 318 | Sentence about “usual” Boolean operators appears to repeat primitive material and does not give eliminations | Attribute only the claim that propositional abbreviations are usual; do not invent source-displayed definitions that are not printed |
| p. 333 | `forall always Phi` line ends with `not exists(true U Phi)` | Record the literal defect; use `not exists(true U not Phi)`, forced by the preceding equality and pp. 318/330 |
| p. 338 | Primed family tuple has unprimed `TS_n` on the left | Read it as `TS'_n`, as forced by all primed components, Figure 6.8, and subsequent prose |
| p. 338 | Inductive transition display mentions `s'_{n-1}` under `n >= 0`, but no `s'_{-1}` exists | Take Figure 6.7 as the separate base case and the display only for `n > 0` |
| p. 339 | CTL indistinguishability through formula length `n` is essential | Preserve that the proof is left to the reader; do not call Theorem 6.21 fully proved in this chapter |
| p. 340 | Assumed LTL equivalence changes `forall always exists eventually a` to `forall eventually exists eventually a` in one line | Keep `forall always exists eventually a`; the premise, figures, and contradiction require it |
| p. 347 | Universal weak-until expansion repeats `Psi` where `Phi` is required | Use the correct set clause on the same page and the semantics on pp. 327--328 |
| p. 352 | Algorithm 16 comments `s' does not satisfy Phi` for every extracted work item | Change only the comment: later work items may satisfy `Phi` but fail `exists always Phi`; the algorithm and invariant remain sound |
| p. 354 | Example 6.28 points to Figure 6.13(b) for the SCC and (c) for the final set | The page image shows these are (c) and (d), respectively |
| p. 355 | Heading promises time and space complexity | Attribute the stated time theorem and representation hypotheses; do not attribute a separate printed space bound on this surface |
| p. 424 | Theorem 6.84 says its disjunction result follows “directly” from component separations | Mark the proof as one sentence and supply the atom-substitution step only as reconstruction |
| p. 425 | Figure 6.27 outer witness begins with an unquantified temporal path formula | Cite Theorem 6.84's well-typed state formula for strictness; do not silently treat the figure display as a primitive CTL* state formula |

## Evidentiary closure and reader-facing use

| Needed artifact or claim | Closed? | Controlling evidence and permitted formulation |
|---|---|---|
| Bibliographic identity and edition | Yes | MIT Press record, title/copyright leaves, ISBN, and 2008 cataloguing data |
| Complete body and duplicate-route identity | Yes | LaBRI and IFMO files are byte-identical, 994 pages, with the hash recorded above |
| Rights to inspect for scholarship | Yes, with ordinary source limits | Anonymous institutional access plus the acquired complete body |
| Open licence or right to republish the PDF/pages | No | Copyright leaf says all rights reserved and requires publisher permission; no open licence appears |
| Exact printed-page map | Yes | Arabic printed page plus 19 equals physical PDF page |
| Transition-system tuple, paths, and no-terminal-state hypothesis | Yes | Definitions 2.1, 2.3--2.4, and 3.4--3.6, printed pp. 20, 23, 95--96 |
| CTL grammar, derived operators, and state/path semantics | Yes | Definition 6.1, Remarks 6.8--6.11, and Definitions 6.4--6.5, pp. 317--329 |
| Existential normal form and translation-size warning | Yes, with printed defect recorded | Definition 6.13 and Theorem 6.14, pp. 332--333 |
| CTL/LTL incomparability formulae and source systems | Yes, with proof omissions recorded | Lemmas 6.19--6.20, Figures 6.6--6.10, and Theorem 6.21, pp. 335--340 |
| Algorithms 13--16 and satisfaction-set theorem | Yes | pp. 342--352; exact set clauses, work sets, counters, and proof boundary recorded above |
| Examples 6.26 and 6.28 | Yes | Figures 6.11--6.13 and pp. 349--354; final state sets reconstructed from the printed graph and prose |
| Theorem 6.30 exact complexity | Yes, for its inherited hypotheses | p. 355; finite no-terminal system, `N` states, `K` transitions, predecessor linked lists, direct modality handling |
| CTL* typed grammar and semantics | Yes | Definitions 6.80--6.82, pp. 422--423 |
| LTL embedding and CTL* strictness | Yes, with proof-strength qualification | Theorems 6.83--6.84, p. 424, reusing Theorem 6.21 witnesses |
| CTL* model-checking algorithm | Not part of this requested surface | §6.8.2 begins at p. 427; no claim about it should be inferred from Theorems 6.83--6.84 |

The reader-facing reconstruction may therefore use this book as a complete
modern textbook authority for the typed CTL and CTL* semantics, enumerative
CTL model checking, the exact finite-model time theorem, and the listed
expressiveness results. It must preserve the finite/no-terminal and data-
representation hypotheses, distinguish source proofs from omitted or
reader-left steps, and carry none of the recorded defective formulae or figure
references into the handbook.
