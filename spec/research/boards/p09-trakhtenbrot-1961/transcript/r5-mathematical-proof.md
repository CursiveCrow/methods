# Round 5 mathematical and proof-correctness review

## Disposition

No blocker or must-fix finding remains within the mathematical/proof-correctness
seat's mandate. The frozen reader correctly separates the announcement from
the expansion, preserves the source's unusually broad whole-future notion of
finite memory, and owns rather than launders the three material edge repairs:

1. the printed graph-degree bound by weight is false;
2. the total covering construction cannot cover the empty set; and
3. the empty language refutes the printed converse in expanded Section 5,
   Theorem 2.

I independently rederived those cases below. In particular, I did not presume
the charter's statement about the weight-two example: the calculation gives
exactly three nonempty graph portions and exactly four all-prefix graph
portions. Consequently the example refutes the printed bound \(k\) under the
expansion's nonempty convention and refutes the former proposed repair
\(k+1\) under the announcement/reader all-prefix convention when \(k=2\).

## Blind-review and evidence declaration

I read the Round 5 charter and no ledger, chair transcript, earlier-round
report, or other Round 5 report. I did not contact another reviewer. The only
substantive evidence used was the seven-object Round 5 snapshot and the
charter-permitted page renders of the two Russian source bodies.

I am not a Russian-language specialist and do not provide a specialist
translation certification. My competence for this seat is mathematical and
formal-logical: I can read the displayed formulae, standard mathematical
Russian terminology, theorem/proof structure, symbols, and cross-references,
and I checked those directly against the page images. For fine philological
wording I relied only on the bounded translation claims already present in the
frozen reader and source note; I do not elevate that reliance into independent
linguistic certification. This limitation does not prevent the complete
mathematical mandate, because every conclusion below is established by an
explicit derivation or counterexample and tied to the controlling displays.

No test, test harness, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, or handbook build was used. SHA-256
was used only as the charter-permitted identity label. I made no change to a
frozen artifact. This transcript is my only write.

## M01 — frozen identity labels

All seven SHA-256 values were recomputed before substantive review and agree
exactly with the Round 5 charter.

| Frozen object | Recomputed SHA-256 |
|---|---|
| tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf | 44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9 |
| tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf | EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D |
| handbook/parts/p09/presentations/n-c-014.tex | 070252A0A152D814FD1420FDBF889CAA9FEFBB5D187B2C1CDAB1B0595CAA13DB |
| handbook/parts/p09/logic-in-computer-science.tex | A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD |
| handbook/bib/handbook.bib | 75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C |
| spec/research/p09-trakhtenbrot-1961-source-note.md | 6C214BCC16961AEC1124D87FA5D474E957B93C083CA377C5EC414DCF055FC655 |
| spec/research/p09-source-presentations-lot2-3.md | 667283E6415851F28A35EEE339DD466AA8706DB13DC05EA0ACDCAF096A24E974 |

Status: **checked-clean**.

## M02 — complete visual source pass and page map

I visually inspected every permitted render at original detail, in order.

- Announcement physical pages 1, 2, 3, 4 map to printed pp. 326, 327, 328,
  329. All four folios and the article's continuous body are visible.
- Expansion physical pages 01 through 29 map to printed pp. 103 through 131,
  with \(p=102+n\) for physical page \(n\). The opening article page is p. 103;
  physical page 02 visibly begins p. 104, and the visible folios then continue
  without a gap through p. 131 on physical page 29.

The mathematical displays, theorem headings, proof continuations, examples,
footnotes, and section transitions were all inspected from those images. The
announcement is a compressed four-page statement; the expansion is a distinct
five-section proof body. No theorem number or proof detail was transferred
from one body to the other.

Status: **checked-clean**.

## M05 — systems \(\mathcal I\) and \(\mathcal I'\)

Controlling reader locations are n-c-014.tex lines 499--510 and 801--810;
the detailed record is p09-trakhtenbrot-1961-source-note.md lines 107--143
and 464--473. The controlling expansion pages are 103--105 and 130--131.

The source syntax and interpretation are represented correctly:

- individuals range over \(1,2,\ldots\);
- monadic predicate variables range over arbitrary subsets of that domain;
- immediate successor is primitive;
- atomic formulae apply a predicate to a variable or an iterated successor;
- propositional operations and both individual and predicate quantification
  form formulae; and
- equality, order, bounded individual quantifiers, numerical constants, and
  \(t+k\) are eliminable extensions, not hidden primitives.

The Cyrillic И therefore names the interpreted formal language, rendered
typographically as \(\mathcal I\); it does not name an automaton or a set. On
expanded p. 130, \(\mathcal I'\) changes only the predicate range: its predicates
are eventually zero. This is exactly the distinction stated in the reader.

Status: **checked-clean**.

## M06 — fictitious occurrence and normal form

Controlling reader location: n-c-014.tex lines 512--525. Controlling pages:
announcement pp. 326--327 and expansion pp. 105--109.

The source's fictitious-occurrence condition is semantic. If two
interpretations differ only outside \([a,b]\), changing the free predicate there
cannot change truth. It is not a claim that a written predicate letter is
absent. The lower and upper classes are correctly kept asymmetric:

- a lower \(t\)-formula depends on a bounded prefix through \(t+s\);
- an upper \(t\)-formula depends on the tail starting at \(t\).

The proof architecture reported in lines 517--523 is valid. Predicate
quantifiers are put outside the individual quantifiers; individual quantifiers
are pushed inward and split at \(t\); the lower bounded part is reduced to a
finite Boolean function of a bounded window; and a remaining predicate
quantifier distributes across lower and upper factors after the common finite
overlap has been fixed. The last step is justified by splicing two predicate
assignments which agree on that fixed overlap: use the lower witness on the
prefix and the upper witness on the tail. This gives the displayed Boolean
combination normal form and explains, rather than merely asserts, why only
finitely many residual formulae can later arise.

Announcement Theorem 1 on p. 327 and the unnumbered expanded theorem on
pp. 108--109 are not assigned a common source number by the reader.

Status: **checked-clean**.

## M07 — anticipation, memory, weight, and finite realization classes

Controlling reader location: n-c-014.tex lines 527--580. Controlling
expansion pages: 109--113; the announcement's compressed canonical equations
are on pp. 326--327.

For \(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\), anticipation bounded by \(p\)
means that agreement of inputs through \(t+p\) forces agreement of outputs at
\(t\). At \(p=0\), agreement through \(t\) forces agreement through \(t\) of
the outputs coordinate by coordinate. Conversely, prefix preservation of all
finite word maps gives the same coordinate condition. Thus the reader's
prefix equivalence is exact.

The finite-memory equations in lines 541--550 correctly take the *whole*
suffix \(a_{\ge t}\), not merely a bounded window. Hence a state reached at
time \(t\) may depend on future input and need not be fixed by the consumed
prefix. Weight is the minimum cardinality of such a state set. Adding one
uniform bounded lookahead \(p\) produces the finite-window equations in lines
556--562 and defines a finite operator. Setting \(p=0\) gives the
automaton-realizable class called Л in the announcement and \(A\) in the
expansion.

The four conditions remain genuinely distinct:

1. zero anticipation alone admits uncountably many causal stream maps;
2. finite memory alone can inspect an unbounded or noncomputable property of
   the suffix;
3. bounded anticipation alone does not supply finitely many memory states;
4. a finite operator requires both finite memory and bounded anticipation,
   while an \(A\)-operator additionally sets the anticipation bound to zero.

The reader also expressly declares its normalization from Л to \(A\), so the
letter is not silently transferred from 1962 to 1961.

Status: **checked-clean**.

## M08 — negative recognition/synthesis boundary

Controlling reader location: n-c-014.tex lines 551--580. Controlling pages:
expanded pp. 111--113.

The one-state edge case is real. With one state and

\[
  \Phi(z)=1\quad\Longleftrightarrow\quad
  (\exists i\geq 1)\ z_i=1,
\]

the output at time \(t\) asks whether a strictly later input value is \(1\).
The state transition is trivial, so the weight is one, but no finite
anticipation bound works: after any proposed bound \(p\), the all-zero stream
and the stream whose first later \(1\) is at \(t+p+1\) agree through \(t+p\)
and give different outputs at \(t\). As an operation on arbitrary infinite
inputs this look-ahead question is not an effective total stream computation.

The primitive-recursive negative arguments are also sound. An input-free
finite-state output stream is ultimately periodic, and every ultimately
periodic stream has such a presentation. Therefore recognition of whether a
primitive-recursive output scheme is an \(A\)-operator would decide the
undecidable ultimate-periodicity problem for primitive-recursive sequences.
For synthesis, transform a primitive-recursive \(f\) into a sequence \(g\)
which is identically zero when \(f\) is identically zero and which becomes
permanently one after the first nonzero value of \(f\). Every resulting \(g\)
is ultimately periodic, so a supposed canonical-equation synthesizer would
produce a finite machine; checking that finite machine for identically-zero
output would decide whether \(f\equiv0\), also undecidable. This proves the
recognition and synthesis boundaries claimed in the reader without converting
them into a blanket negative claim about \(\mathcal I\).

Status: **checked-clean**.

## M09 — portions, examples, and the complete weight-two calculation

Controlling reader location: n-c-014.tex lines 582--642. The same
calculation is recorded at p09-trakhtenbrot-1961-source-note.md lines
203--290 and in the compact record at
p09-source-presentations-lot2-3.md line 652. Controlling pages are
announcement p. 327 and expansion pp. 113--116.

### The two source conventions

For a finite word \(u\), the residual

\[
  M_u=\{Z:uZ\in M\}
\]

has an unambiguous standing as a set of suffix streams. Tuple residuals are
taken coordinatewise. The announcement permits \(M_u=\varnothing\); the
expansion first requires the prefix cylinder to meet \(M\), and therefore
names only nonempty residuals as portions. Homogeneous degree, a basis, and
the internal transition are respectively the number of distinct residuals,
a list of them, and the map induced by appending one letter. The reader states
all of this before use and does not turn the data into an invented automaton
kind.

### Anticipation zero

Define

\[
 T(X)(t)=
 \begin{cases}
 X(t),&X(1)=1,\\
 0,&X(1)=0.
 \end{cases}
\]

If two inputs agree through \(t\), they agree both at coordinate \(1\) and at
coordinate \(t\), so their outputs agree at \(t\). Hence \(T\) has
anticipation zero.

### The displayed two-state whole-future presentation

Take \(Q=\{0,1\}\), \(q(1)=0\), and for
\(z=(z_0,z_1,\ldots)\),

\[
 \Phi(q,z)=(1-q)z_0,
 \qquad
 \Psi(q,z)=q\mathbin{\mathsf{xor}}z_0
                 \mathbin{\mathsf{xor}}z_1.
\]

For an input \(X\), induction gives

\[
 q(t)=X(1)\mathbin{\mathsf{xor}}X(t).
\]

The base case is \(q(1)=0=X(1)\mathbin{\mathsf{xor}}X(1)\). If the formula
holds at \(t\), then

\[
\begin{aligned}
q(t+1)
 &=q(t)\mathbin{\mathsf{xor}}X(t)
          \mathbin{\mathsf{xor}}X(t+1)\\
 &=X(1)\mathbin{\mathsf{xor}}X(t+1).
\end{aligned}
\]

If \(X(1)=0\), then \(q(t)=X(t)\) and
\((1-q(t))X(t)=0\). If \(X(1)=1\), then
\(q(t)=1-X(t)\) and \((1-q(t))X(t)=X(t)\). The equations therefore present
exactly \(T\).

### No one-state presentation

With one state, the output equation would have one time-independent suffix
function \(f(z)\). At time \(1\), \(T(X)(1)=X(1)\) for every input, so

\[
 f(z)=z_0\qquad\text{for every suffix }z.
\]

Now take any input beginning \(01\). At time \(2\) its suffix begins in \(1\),
so the one-state equation gives \(f(z)=1\), while the defining operator gives
\(T(X)(2)=0\) because \(X(1)=0\). This contradiction proves that the weight is
exactly two.

### Every graph portion

Let \(G=\{(X,T(X)):X\in2^\omega\}\). For paired words \(u,v\) of the same
length \(n\), direct substitution gives the complete classification:

| Paired prefix | Consistency condition | Residual of \(G\) |
|---|---|---|
| \(n=0\) | always | \(G\) |
| \(n>0,\ u_1=0\) | \(v=0^n\) | \(C=\{(Z,0^\omega):Z\in2^\omega\}\) |
| \(n>0,\ u_1=1\) | \(v=u\) | \(I=\{(Z,Z):Z\in2^\omega\}\) |
| any other pair | inconsistent | \(\varnothing\) |

Indeed, if \(u_1=0\), the entire output must be zero, while the remaining input
is arbitrary; if \(u_1=1\), output and input must agree at every coordinate.
Longer prefixes impose no other residual behavior. The three nonempty sets
\(G,C,I\) are pairwise distinct, and the inconsistent residual is a fourth
distinct all-prefix portion. Thus

\[
 \#\operatorname{Portions}_{\ne\varnothing}(G)=3,
 \qquad
 \#\operatorname{Portions}_{\mathrm{all}}(G)=4.
\]

Since \(k=2\), the expansion's printed claim \(3\leq k\) is false. Under the
all-prefix convention, the former proposed repair would require
\(4\leq k+1=3\), also false. These are the exact conclusions warranted by the
example. The example does not purport to disprove every conceivable function
of \(k\); it proves that broad state weight is neither the printed portion
count nor that count plus the empty residual. The exact invariant is the
number of distinct suffix operators induced by consistent paired prefixes,
with the empty residual added under the all-prefix convention.

Graph closedness survives the correction. If
\((X_n,T(X_n))\to(X,Y)\), then for each \(t\), sufficiently large \(n\) have
\(X_n|_t=X|_t\) and \(T(X_n)|_t=Y|_t\). Zero anticipation gives
\(T(X_n)|_t=T(X)|_t\); hence \(Y|_t=T(X)|_t\) for every \(t\), so \(Y=T(X)\).

### Singleton and uncountability examples

For a singleton \(\{X\}\), the nonempty residuals are precisely the singleton
suffixes \(\{\sigma^nX\}\); the all-prefix convention may additionally add
\(\varnothing\). There are finitely many such suffixes exactly when two
suffixes coincide, which is equivalent to ultimate periodicity of \(X\).

The uncountability argument also works with the reader's all-prefix
convention. For an aperiodic stream \(\xi\), consider the set of streams that
eventually agree with some suffix of \(\xi\). Adding or deleting a finite
prefix does not alter this property, so every residual equals the original
set; it is one-homogeneous and has no empty residual. Eventual-shift
equivalence classes are countable, while Cantor space is uncountable, hence
there are uncountably many distinct such one-homogeneous sets but only
countably many \(\mathcal I\)-formulae.

Status: **checked-clean**.

## M10 — definability implies homogeneity and effective internal transition

Controlling reader locations: n-c-014.tex lines 643--646 and 679--686.
Controlling pages: announcement p. 327 and expansion pp. 116--118.

Take a defining formula in the lower/upper normal form of M06. After fixing a
prefix of length \(v\), every lower factor is reduced to one of finitely many
Boolean functions of the fixed prefix and its fixed-width continuation window.
Every upper factor is the same tail formula with its origin shifted to the new
first position. There are only finitely many truth functions on the bounded
window and finitely many upper factors, so only finitely many residual formulae
can result. Equal residual formulae define equal portions; hence the defined
set is homogeneous.

This is effective at the internal level. Put the finitely many residual
formulae into a list, append each possible input letter, normalize the shifted
formula, and record the index already on the list. That finite table is
exactly the internal transition map. No truth or nonemptiness decision is
needed merely to compute the syntactic transition; that distinction is used
correctly in M12.

Status: **checked-clean**.

## M11 — closed homogeneous converse, recurrence, closure class, and empty set

Controlling reader location: n-c-014.tex lines 643--677. Detailed record:
p09-trakhtenbrot-1961-source-note.md lines 281--324. Controlling pages:
announcement pp. 327--328 and expansion pp. 116--119.

### Nonempty covering construction

Let \(M\ne\varnothing\) have finite nonempty basis
\(M_1=M,M_2,\ldots,M_k\). From a basis member and a choice bit, select a bit
whose one-letter residual is nonempty, and move to that residual's basis
index. This gives a total finite-state covering map because every basis member
is nonempty and hence admits at least one next letter.

Every generated stream has each finite prefix extendible to a point of \(M\),
so it lies in \(\overline M\). Conversely, if \(X\in\overline M\), every prefix
cylinder about \(X\) meets \(M\); at each step choose the branch that emits the
next bit of \(X\). The covering map then outputs \(X\). Its image is therefore
exactly \(\overline M\).

Encoding the basis index by bound one-hot predicates \(q_1,\ldots,q_k\), the
branch choices by a bound predicate \(U\), and the local output/state relation
by a quantifier-free matrix \(\theta\) gives exactly the recurrence displayed
at reader lines 649--657. The free predicate is \(X\); the other predicates
are witnesses; and the fixed initial clause selects \(M\) rather than an
unspecified union of basis members.

If \(M\) is closed, the image \(\overline M\) is \(M\), proving definability.
Conversely, the set of triples satisfying the fixed initial clause and every
local recurrence clause is closed in a finite product of Cantor spaces. That
product is compact, and projection to the free \(X\)-coordinate is therefore
compact and closed. Only finitely many state patterns can occur, so its
residual family is finite. Thus every formula of the recurrent shape defines
a closed homogeneous set.

### The empty set

A total map has a nonempty domain and hence a nonempty image. The covering
argument above therefore cannot possibly cover \(M=\varnothing\); this is not
a cosmetic proof omission. The reader's separate formula is correct: retain
the recurrent syntax and conjoin

\[
 q_1(1)=1\quad\text{and}\quad q_1(1)=0.
\]

No witness predicates can satisfy the initial conjunction, so the formula
defines exactly the empty set. This verifies both the restriction of the
source covering construction to nonempty sets and the inconsistent recurrent
formula used for the empty case.

### Full closure characterization

The normal form reduces arbitrary \(\mathcal I\)-definitions to Boolean
combinations and predicate projections of recurrent closed homogeneous cores.
Conversely, closed homogeneous sets have the recurrence just proved, and
\(\mathcal I\) is closed under complement, finite union, and existential
predicate projection. Hence the least class described at reader lines
672--675 is exact. Closedness is not silently imposed on every homogeneous
set, and the announcement's open Borel/projective classification question
remains open in the reader.

Status: **checked-clean**.

## M12 — unconditional and conditional constructions

Controlling reader locations: n-c-014.tex lines 679--686 and 734--744.
Controlling pages: announcement pp. 326 and 329; expansion pp. 117--119 and
124.

The following boundary is mathematically necessary and is stated correctly.

- Normalization and the internal residual transition are syntactic finite
  constructions and are unconditional.
- Selecting an external output branch requires knowing that a residual set is
  nonempty. For an arbitrary \(\mathcal I\)-formula, that is a truth question,
  so the covering and stable-deletion procedures are conditional on a truth
  algorithm for closed \(\mathcal I\)-sentences.
- The displayed existential-predicate recurrent fragment lies in the source's
  stated Putnam-decidable form, so its required emptiness/truth tests are
  unconditional.

The reader neither retroactively erases source-time conditionality nor extends
Putnam's qualification to every \(\mathcal I\)-formula.

Status: **checked-clean**.

## M13 — continuous total operators are finite

Controlling reader location: n-c-014.tex lines 688--698. Controlling pages:
announcement p. 328 and expansion pp. 119--120.

Let \(G\) be the \(\mathcal I\)-definable graph of a continuous total operator
and let \(G_1,\ldots,G_k\) be its nonempty graph portions. Each input-domain
projection \(D_i\) is compact. On \(D_i\), functionality makes the first
output coordinate a continuous map to the finite discrete output alphabet.
Its inverse images are clopen in \(D_i\). Compactness supplies a finite
cylinder subcover, hence an integer \(r_i\geq1\) such that agreement of inputs
on their first \(r_i\) letters forces agreement of the first output letter on
\(D_i\).

There are finitely many portions, so take

\[
 p=\max_i(r_i-1).
\]

At time \(t\), use as state the portion reached after the already consumed
input/output prefix. The next output is determined by that state and
\(a(t),\ldots,a(t+p)\); appending the current input/output pair moves to another
basis portion. These are canonical finite-window equations with at most \(k\)
states. Thus the operator has one uniform anticipation bound, finite memory,
and weight at most the homogeneity degree. If the original operator already
has anticipation zero, the equations have \(p=0\), placing it in class Л in
the announcement and class \(A\) in the expansion.

This proof uses compactness exactly where the reader says it does and does not
derive bounded anticipation from finite memory alone.

Status: **checked-clean**.

## M14 — expanded Section 4, Theorem 2 is strictly weaker

Controlling reader location: n-c-014.tex lines 696--698. Controlling page:
expanded p. 120.

Without continuity, the finite basis still supplies finite memory. In state
\(G_i\), allow \(\Phi_i\) to inspect the entire remaining input suffix and take
the first coordinate of its unique related output; \(\Psi_i\) moves to the
portion obtained after that input/output pair. This is precisely the source's
whole-future finite-memory form, with at most the homogeneity degree many
states. No compact-uniformity step remains, so no finite lookahead follows.

The loss is strict. The \(\mathcal I\)-explicit operator

\[
 T(X)(t)=1\quad\Longleftrightarrow\quad
 (\exists s>t)\ X(s)=1
\]

has a one-state whole-suffix presentation, but for every \(p\) the all-zero
input and an input with its first later \(1\) at \(t+p+1\) agree through
\(t+p\) and give different outputs at \(t\). It has no bounded anticipation.
The reader therefore correctly reports finite memory, not finite-operator
standing.

Status: **checked-clean**.

## M15 — graph, solution, and announcement Theorem \(4'\)

Controlling reader location: n-c-014.tex lines 700--710. Controlling page:
announcement p. 328.

The distinction is exact. A formula defines an operator only when its entire
relation is that graph; an operator solves the formula when its graph is merely
contained in the relation. The latter permits many possible outputs and is
the standing required by Theorem \(4'\).

For a closed homogeneous relation with a continuous solution, the compact
uniformity argument of M13 can be applied while choosing outputs inside the
relation, yielding a finite solution with weight bounded by the relation's
degree. If a zero-anticipation solution exists, its prefix-compatible choices
witness a surviving allowed output at every reachable portion; choosing among
those finitely many portion transitions yields a Л-solution of the same weight
bound. The expansion's \(A\)-terminology is used only as the reader's declared
normalization. For the separately stated open-relation analogue, compactness
of a continuous solution graph inside the open relation yields a finite
cylinder refinement, but the relation's original homogeneous degree need not
bound the refinement; the reader correctly omits a weight estimate.

All clauses of announcement Theorem \(4'\), including the open-relation
remark and its missing bound, are preserved.

Status: **checked-clean**.

## M16 — both quantifiers in a general solution

Controlling reader location: n-c-014.tex lines 712--726. Controlling pages:
announcement p. 328 and expansion pp. 120--121.

The standing is correct: \(T\) is an operator from the original input streams
and a finite tuple of parameter streams to the output stream. Generality is
not mere existence. It consists of two logically independent clauses:

1. **completeness:** every solution \(T_0\) of the named class is
   \(T(X,S(X))\) for a parameter-operator tuple \(S\) of that class;
2. **soundness:** every parameter-operator tuple \(S\) of that class makes
   \(T(X,S(X))\) a solution.

Replacing \(A\)-operator by zero-anticipation operator in *both* clauses gives
the general zero-anticipation notion. Replacing it in only the parameter or
only the represented-solution clause would be a different and inadequate
definition; the reader does not make that error. A tuple of parameter streams
is only finite product packaging and does not change either quantifier.

Status: **checked-clean**.

## M17 — Theorem 5 / expanded Theorem 3

Controlling reader location: n-c-014.tex lines 728--746. Controlling pages:
announcement pp. 328--329 and expansion pp. 121--124.

Let \(M\) be the closed relation and let \(M_1=M,\ldots,M_k\) be its finite
portion basis. Begin with the nonempty portions and repeatedly delete a basis
member \(M_i\) if some current input letter \(\sigma\) has no output letter
\(\tau\) whose residual after \((\sigma,\tau)\) remains in the current family.
The process terminates because the family is finite.

### No-solution branch

If \(M_1\) is deleted, no zero-anticipation solution exists. Otherwise a
purported causal solution would, after every consistent prefix, have to choose
an output using only that prefix and remain inside a portion from which the
same obligation can be met at the next step. Its reachable portions would
form a nonempty family closed under the required one-letter choices, hence
would survive the deletion. This contradicts deletion of \(M_1\).

### Surviving-family branch

If \(M_1\) survives, for each surviving state and current input letter there
is at least one surviving output. When one output is possible, use it; when
both Boolean outputs are possible, let a free parameter bit select. The next
state is the basis index of the chosen residual. This defines a zero-lookahead
finite-state operator \(T(X,U)\) with at most \(k\) states.

Every finite prefix it produces is compatible with \(M\). Since \(M\) is
closed, the resulting infinite pair belongs to \(M\), proving soundness for
every zero-anticipation parameter substitution. Given any zero-anticipation
solution \(T_0\), choose the parameter bit at time \(t\) to encode which of the
surviving output branches \(T_0\) takes. That choice depends only on the input
prefix, so it is a zero-anticipation parameter operator and recovers \(T_0\).
If \(T_0\) is an \(A\)-operator, combining its finite state with the finite
relation-state index makes the parameter selector an \(A\)-operator. Thus the
same \(T\) is both a general \(A\)-solution and a general zero-anticipation
solution, with weight at most the relation's homogeneous degree.

Testing whether a formula-defined portion is empty is exactly the conditional
step identified in M12. The reader reports the conditionality rather than
claiming that stable deletion itself solves arbitrary \(\mathcal I\)-truth.

Status: **checked-clean**.

## M18 — expanded Theorem \(3'\) at fixed anticipation

Controlling reader location: n-c-014.tex lines 739--744. Controlling page:
expanded p. 124.

Fix \(p\geq0\). For an output \(Y\) with anticipation bounded by \(p\), define

\[
 \widetilde Y(1)=\cdots=\widetilde Y(p)=0,
 \qquad
 \widetilde Y(t+p)=Y(t).
\]

Then \(\widetilde Y(s)\) depends only on the input through \(s\), so the shifted
operator has zero anticipation. Conversely, a zero-anticipation
\(\widetilde Y\) with the fixed zero prefix determines
\(Y(t)=\widetilde Y(t+p)\), which has anticipation bounded by \(p\). Shifting
every occurrence of the output predicate in the formula gives a one-to-one
reduction to M17, including parameter soundness and completeness. The
construction is performed separately for this fixed \(p\). It supplies no
single general solution simultaneously covering unbounded lookahead classes,
and the reader makes no such overstatement.

Status: **checked-clean**.

## M19 — explicit definitions and shifted-formula synthesis

Controlling reader location: n-c-014.tex lines 748--761. Controlling pages:
expanded pp. 124--127.

An explicit definition fixes \(Y(t)\) by one formula
\(\varphi(X_1,\ldots,X_m;t)\), so it defines a total unique operator. Its graph
is \(\mathcal I\)-definable, and expanded Section 4, Theorem 2 supplies finite
memory even when the formula has unbounded future dependence. It has
anticipation bounded by \(p\) exactly when changing input-predicate values
outside \([1,t+p]\) cannot change \(\varphi\)'s truth; necessity and sufficiency
are immediate from the semantic definition of anticipation. The \(p=0\)
case is exactly the \(A\)-operator criterion.

For the zero-shift upper-controlled case, fix the first input column, evaluate
the first output, and shift the remaining formula back to origin \(1\). The
normal form admits only finitely many resulting residual formulae, so repeated
shifting terminates at a finite list. The current residual's first output and
the next residual index are the canonical output and transition tables.

The pp. 126--127 worked example was checked, not merely located. Its first
residual has first output \(0\) for all four input columns; its second residual
has first output \(1\) for all four. With rows \(00,01,10,11\), the printed
tables are

\[
\begin{array}{c|cc}
\sigma_1\sigma_2&\Phi(1,\sigma)&\Phi(2,\sigma)\\\hline
00&0&1\\
01&0&1\\
10&0&1\\
11&0&1
\end{array}
\qquad
\begin{array}{c|cc}
\sigma_1\sigma_2&\Psi(1,\sigma)&\Psi(2,\sigma)\\\hline
00&1&1\\
01&1&2\\
10&1&1\\
11&2&2.
\end{array}
\]

The transition pattern agrees with the formula: state 1 enters state 2 only
after column \(11\), while state 2 persists exactly when the second input bit
is \(1\). The example illustrates the general residual construction; it is
not presented as proof of the earlier topological theorems.

Status: **checked-clean**.

## M20 — finite-word maps and both directions of expanded Theorem 2

Controlling reader location: n-c-014.tex lines 763--799. Detailed record:
p09-trakhtenbrot-1961-source-note.md lines 423--462. Controlling pages:
expanded pp. 127--129.

For a zero-anticipation stream operator, two infinite extensions of
\(u\in A^t\) agree through \(t\), so their output prefixes through \(t\) agree.
This proves that \(T_t:A^t\to B^t\) is well-defined. Applying the same argument
to a shorter prefix proves

\[
T_s(u|_s)=T_t(u)|_s\qquad(s\leq t).
\]

Thus the word maps are extension-independent and prefix-compatible.

The source's two word-set properties are represented with the correct types:

- enumeration means \(L\cap B^t=T_t(A^t)\) at each positive length;
- decision means that the recognizer's output at the terminal position of a
  presented word is \(1\) exactly for members of \(L\).

### Enumeration implies decision

If \(T\) explicitly enumerates \(L\), a word \(Y|_t\) belongs to \(L\) exactly
when

\[
 (\exists X)(\forall \tau\leq t)
       \bigl(Y(\tau)=T(X)(\tau)\bigr).
\]

This is a \(t\)-formula, so Section 5 synthesis gives an \(A\)-recognizer.
That establishes the first direction.

### Corrected converse

The printed conditions do not suffice for \(L=\varnothing\). The empty
language is decided by the constant-zero one-state recognizer. It is
prefix-closed and every-member-extendible vacuously, but the range of a total
map \(A^t\to B^t\) is nonempty for every \(t\geq1\), so no operator enumerates
it.

Now assume \(L\ne\varnothing\), prefix closure, and that every member has a
proper extension in \(L\). Prefix closure gives a length-one member; proper
extension plus prefix closure gives a member of every positive length. Given
an input word \(u\) of length \(t\), output \(u\) when \(u\in L\). Otherwise,
take its longest accepted prefix \(w\) and output the lexicographically first
length-\(t\) member of \(L\) extending \(w\); if there is no accepted positive
prefix, use the first length-\(t\) member of \(L\).

The choices are prefix-compatible. Once an input prefix fails membership,
no longer input prefix can re-enter a prefix-closed language. Moreover, the
prefix of the lexicographically first length-\(t+1\) extension is the
lexicographically first length-\(t\) extension: otherwise a smaller
length-\(t\) candidate could be properly extended and would yield a smaller
length-\(t+1\) candidate. The defining membership and first-choice conditions
are \(t\)-formulae relative to the given recognizer, so the source's synthesis
produces an \(A\)-enumerator.

Nonemptiness is therefore both necessary for the omitted seed and sufficient
with the two printed conditions. The reader's correction is exact and is
honestly marked handbook-owned.

Status: **checked-clean**.

## M21 — weak system, special beginnings, and expanded Theorem 3

Controlling reader location: n-c-014.tex lines 801--810. Controlling pages:
expanded pp. 130--131.

In \(\mathcal I'\), every predicate is eventually zero. A word
\(X(1)\cdots X(t)\) is a special beginning of \(X\) only when
\(X(\tau)=0\) for every \(\tau>t\). It is not an arbitrary prefix, and the
reader states the tail-zero requirement at the definition.

For an arbitrary \(\mathcal I\)-formula \(\varphi\), the source's displayed
operator at p. 130 accepts a presented prefix exactly when there exists a
predicate \(\Gamma\) satisfying \(\varphi\), agreeing with that prefix, and
equal to zero afterward. The input predicate is semantically fictitious
beyond \(t\), so the definition has zero anticipation and yields existence of
an \(A\)-operator. No effectiveness follows for arbitrary \(\mathcal I\),
because deciding the required formula may be unavailable. When the formula
belongs to \(\mathcal I'\), the source invokes the Büchi decision/synthesis
result to construct the operator effectively. The reader preserves both the
existence/effectivity distinction and the explicit Büchi attribution.

Status: **checked-clean**.

## M22 — announcement/expansion comparison

Controlling reader locations: n-c-014.tex lines 487--525, 643--746, and
748--810. Controlling announcement pages: 326--329. Controlling expansion
pages: 103--131.

The result map is correct and does not transfer numbering:

| 1961 announcement | 1962 expansion | Reader treatment |
|---|---|---|
| Theorem 1 | Section 1.4 unnumbered normal-form theorem | effective lower/upper normal form, separately located |
| Theorem 2 | Section 3, Theorem 1 | definability implies homogeneity and effective internal transition |
| Theorem 3 | Section 3, Theorems 2 and \(2'\) plus closure corollary | closed homogeneous converse and recurrent form |
| Theorem 4 | Section 4, Theorem 1 | continuous definable operator is finite |
| Theorem \(4'\) | announcement's relation/solution existence form | kept at announcement strength, including open-relation remark |
| Theorem 5 | Section 4, Theorem 3 | no-solution/general-solution alternative |
| — | Section 4, Theorem 2 | continuity removed, finite memory only |
| — | Section 4, Theorem \(3'\) | separately fixed anticipation bound \(p\) |
| — | Section 5, Theorems 1--3 | explicit synthesis, word sets, and \(\mathcal I'\) |

The announcement's Л and expansion's \(A\) are separately reported. Proof
detail found only in the expansion is not described as though it were printed
in the four-page announcement.

Status: **checked-clean**.

## M23 — modern finite-word theorem and Thomas paragraph

Controlling frozen locations are
logic-in-computer-science.tex lines 811--825 and n-c-014.tex lines
812--847. The literal Trakhtenbrot boundary is controlled by announcement
pp. 326--329 and expansion pp. 124--131.

The displayed modern theorem is mathematically correct. Over finite words,
MSO with order and MSO with successor plus definable endpoints are equivalent;
atomic relations have finite automata, Boolean connectives use effective
Boolean language operations, and existential monadic quantification is track
projection. Conversely, disjoint monadic state-position sets express an
accepting run. These steps prove regularity exactly.

The frozen text then immediately labels this as the *modern formulation* and
states that the original sources have different encodings and packages. The
Trakhtenbrot pages visually inspected here contain the broader theory of
arbitrary predicates, topology, anticipation, memory, and general solutions,
and their Section 5 bridge uses automaton-enumerability, terminal
automaton-decidability, and special beginnings. The reader does not quote the
one-sentence regular/MSO equivalence as announcement Theorem 1--5. The Thomas
paragraph is used for the modern proof architecture, not as a substitute for
either Russian body. Thus the compound theorem name is not used to launder
folklore into Trakhtenbrot's literal statement.

Status: **checked-clean**.

## M26 — complete terminology-rule audit

Controlling scope: n-c-014.tex lines 487--847, together with the repository
rule in the charter.

Every technical name introduced in the Trakhtenbrot presentation satisfies the
five requirements at first use:

- \(\mathcal I\) is necessary to render Cyrillic И, is exactly defined, has
  formal-language standing, is separated from automata and Büchi's weak
  system, and is used throughout.
- fictitious occurrence, lower \(t\)-formula, and upper \(t\)-formula have
  semantic definitions, formula/dependence standing, explicit distinctions,
  and immediate use in the normal-form theorem.
- anticipation, finite memory, weight, finite operator, and \(A\)-operator have
  typed equations or exact minimization clauses, operator/property standing,
  explicit nonredundancy, and later theorem use.
- ultimately periodic is given an exact preperiod/period equation and is
  introduced only to disambiguate the source's use of “periodic.”
- portion, homogeneous degree, basis, and internal transition are exactly
  defined as residual-set properties/data, explicitly denied automaton-kind
  standing, distinguished from each other, and used immediately.
- solution, general \(A\)-solution, and general zero-anticipation solution have
  relation/operator/parameter standing and exact soundness/completeness
  clauses; their nonredundancy from graph definition and mere existence is
  explicit.
- explicit definition, automaton-enumerable, automaton-decidable, terminal
  result, and special beginning all receive eliminable definitions, correct
  formula/word-set standing, explicit distinctions, and immediate theorem use.

Descriptive phrases such as “constant-zero graph,” “identity graph,” and
“operator induced on the remaining suffix” eliminate directly to the displayed
graph or residual definition and are not promoted into unsupported primitives.
I found no definition-after-use, standing ambiguity, redundant coined name, or
unused distinction.

Status: **checked-clean**.

## M27 — adversarial mathematical compression audit

The following failure modes were tested against the exact reader lines and the
controlling pages:

- **hidden continuity:** continuity is used only in M13 and the continuous
  branch of M15; M14 explicitly drops it and loses bounded anticipation;
- **hidden closedness:** the closed-homogeneous converse, Theorem \(4'\), and
  stable-deletion limit step all state closedness; the open-relation remark is
  separately qualified;
- **operator-class collapse:** whole-future finite memory, finite operator,
  zero anticipation, and \(A\)-operator remain distinct;
- **false weight compression:** the printed \(k\) claim and the former \(k+1\)
  repair are both defeated by the fully calculated example rather than
  retained tacitly;
- **empty-object suppression:** the empty portion, empty set, no-solution
  branch, and empty language are each treated explicitly;
- **generality inflation:** both parameter quantifiers are present, and fixed
  \(p\) is not changed into unbounded lookahead;
- **source laundering:** announcement numbering, expansion proof detail,
  Л/\(A\), and the modern finite-word theorem are kept separate;
- **priority inflation:** Church, Büchi, Elgot, Putnam, and Thomas appear as
  bounded historical/source attributions, not newly adjudicated priority
  theorems; and
- **completion inflation:** the compact record and source note say that
  independent scholarly review remains required and distinguish body
  sufficiency from admission.

No false compression or hidden mathematical hypothesis remains within this
seat's scope.

Status: **checked-clean**.

## M28 — topic, rights, and method boundary

The reviewed claim is limited to N-c-014.c at the separate 1961 announcement
and 1962 expansion strengths. It does not admit the unreconciled Büchi 1960
article, N-c-014 as a whole, Rabin, Part IX, a rendered handbook, final-book
completion, human acceptance, or user acceptance. The rights qualification in
the source note and compact record treats the local PDFs as nonredistributable
research objects and does not infer an open-content licence from public
archival access.

The review method obeyed the scholarly boundary stated at M02 and in the blind
declaration: direct frozen-text reading, page-image inspection, mathematical
derivation, citation/provenance inspection inside the frozen objects, and
identity hashing only.

Status: **checked-clean**.

## Mandatory-point ledger for this seat

| Point | Disposition |
|---|---|
| M01 | checked-clean — seven hashes recomputed and matched |
| M02 | checked-clean — all 4 + 29 renders inspected; page maps confirmed |
| M05 | checked-clean — exact \(\mathcal I/\mathcal I'\) syntax and standing |
| M06 | checked-clean — semantic dependence and full normal-form proof moves |
| M07 | checked-clean — operator, anticipation, whole-future memory, weight, finite and \(A\) classes |
| M08 | checked-clean — primitive-recursive negative boundary and one-state example |
| M09 | checked-clean — both portion conventions; exact two-state counterexample; 3/4 counts; \(k\)/\(k+1\) consequences; singleton and uncountability examples |
| M10 | checked-clean — definability/homogeneity derivation and effective internal transition |
| M11 | checked-clean — closed converse, recurrence, closure class, nonempty cover, inconsistent empty formula |
| M12 | checked-clean — unconditional/conditional/Putnam boundaries |
| M13 | checked-clean — compact uniformity, one anticipation bound, memory and weight |
| M14 | checked-clean — finite memory only; explicit unbounded-lookahead witness |
| M15 | checked-clean — graph/solution distinction and every Theorem \(4'\) clause |
| M16 | checked-clean — both general-solution quantifiers and parameter standing |
| M17 | checked-clean — deletion, no-solution and survivor branches, parameters, closedness, weight, conditionality |
| M18 | checked-clean — fixed-\(p\) shift and no unbounded-lookahead overstatement |
| M19 | checked-clean — explicit criteria, finite residual termination, canonical equations, two-table example |
| M20 | checked-clean — typed word maps, both directions, and exact nonempty corrected converse |
| M21 | checked-clean — \(\mathcal I'\), special beginnings, existence/effectivity, Büchi attribution |
| M22 | checked-clean — announcement/expansion result map without number or strength transfer |
| M23 | checked-clean — modern theorem valid and not laundered into either Russian source |
| M26 | checked-clean — complete terminology rule satisfied |
| M27 | checked-clean — no hidden continuity/closedness, collapse, laundering, or inflation |
| M28 | checked-clean — topic, rights, blind-review, and no-test/no-build boundaries enforced |

VERDICT: ACCEPT
