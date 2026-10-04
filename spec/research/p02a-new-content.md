# P2a research: propositional new content

Status: source-backed research note for the Phase-4 P2a visit.  This file is
evidence and calibration, not handbook prose.  It does not assign handbook
status labels and does not by itself satisfy a register row.

## Evidence policy

- **Source-verified** means that the claim is stated in the linked primary
  source or authoritative modern reference.
- **Derived here** means that the claim follows by the displayed elementary
  argument from source-verified definitions/results.  These are suitable for a
  handbook proof only if that argument is actually migrated to the annex.
- **Do not claim** marks a tempting strengthening not licensed by the evidence.

The live bibliography already contains `Cook1971`, `Craig1957`, and
`Tseitin1968`.  The other sources in the ledger below were not present under
the suggested keys when this note was written; this is only an intake warning,
not authorization to edit the bibliography.

## 1. Post's functional-completeness criterion

### Definitions and standing

Let a Boolean operation of positive arity be a map

\[
f:\{0,1\}^n\longrightarrow\{0,1\},\qquad n\geq 1.
\]

A **clone** is a family of finitary operations containing every projection and
closed under composition (superposition).  Thus a clone is the correct object
for saying which truth functions can be generated from a basis.  The following
five named clones are needed because Post proved that they are exactly the
maximal proper clones of Boolean operations.  Each name has an eliminable
membership test:

| Modern notation | Exact membership test for \(f\) | Obstruction if every generator lies in it |
|---|---|---|
| \(T_0\), 0-preserving | \(f(0,\ldots,0)=0\) | cannot generate the constant-1 operation |
| \(T_1\), 1-preserving | \(f(1,\ldots,1)=1\) | cannot generate the constant-0 operation |
| \(M\), monotone | \(\mathbf x\leq\mathbf y\) coordinatewise implies \(f(\mathbf x)\leq f(\mathbf y)\) | cannot generate negation |
| \(L\), affine | \(f(\mathbf x)=a_0\oplus a_1x_1\oplus\cdots\oplus a_nx_n\) for coefficients \(a_i\in\mathbb F_2\) | cannot generate a nonlinear operation such as conjunction |
| \(S\), self-dual | \(f(\neg\mathbf x)=\neg f(\mathbf x)\), with componentwise complement | cannot generate a non-self-dual operation |

“Affine” is used rather than the ambiguous older word “linear” because the
constant term \(a_0\) is allowed.  Some truth-function literature calls this
class linear or counting; the displayed polynomial is normative.

**Source-verified theorem.**  Post's book states on p. 105 that exactly five
closed systems are immediately below the complete system, that every proper
closed system lies in one of them, and hence that a set generates the complete
system iff none of those five systems contains the set.  In modern notation:

> A set \(F\) of Boolean operations is functionally complete iff, for each of
> \(T_0,T_1,M,L,S\), at least one member of \(F\) is outside that clone.

This formulation is also stated, with the five modern tests, by Pelletier and
Martin.  The quantifiers matter: five different witnesses may be used.  The
criterion does **not** require one generator that simultaneously lies outside
all five classes.

Post's original notation for the five immediate predecessors is
\(C_2,C_3,D_3,A_1,L_1\), not the modern \(T_0,T_1,S,M,L\) notation.  Use the
modern tests in the handbook and cite the modern exposition for the notation;
cite Post for the classification.

#### Nullary constants convention

Post-style clone statements are cleanest for positive arities.  If the
handbook permits nullary \(\bot,\top\) in a basis, replace each nullary constant
by its corresponding unary constant operation before applying the table.  Do
not silently mix nullary and positive-arity conventions in the criterion.

### NAND and NOR as one-element complete bases

Define, at the same location,

\[
p\mathbin{\uparrow}q:=\neg(p\land q),\qquad
p\mathbin{\downarrow}q:=\neg(p\lor q).
\]

These are the NAND (Sheffer) and NOR operations, respectively.  Their use is
nonredundant here: each gives a singleton functionally complete basis.  The
following identities are direct truth-table calculations (**derived here**):

\[
\begin{aligned}
\neg p&=p\uparrow p,&
p\land q&=(p\uparrow q)\uparrow(p\uparrow q),&
p\lor q&=(p\uparrow p)\uparrow(q\uparrow q),\\
\neg p&=p\downarrow p,&
p\lor q&=(p\downarrow q)\downarrow(p\downarrow q),&
p\land q&=(p\downarrow p)\downarrow(q\downarrow q).
\end{aligned}
\]

Each operation also individually fails all five membership tests: it sends
\((0,0)\) to 1 and \((1,1)\) to 0; it is nonmonotone; it fails self-duality at
\((0,1)\); and its algebraic normal form contains the quadratic monomial
\(xy\).  Thus singleton completeness follows either from the identities or
from Post's criterion.  Sheffer's 1913 paper is the primary historical source
for the single primitive now represented by NAND.  The NOR completeness claim
needs no separate historical attribution because the displayed identities
prove it.

### Negative examples appropriate for the entry

The clone tests make the usual incompleteness arguments exact:

- \(\{\land,\lor,\bot,\top\}\) is contained in \(M\), so it cannot define
  negation.
- \(\{\neg,\leftrightarrow\}\) is contained in \(L\), so it cannot define
  conjunction.
- \(\{\to\}\) is contained in \(T_1\), so it is not complete.
- \(\{\neg,\land\}\), \(\{\neg,\lor\}\), and \(\{\neg,\to\}\) escape all
  five classes and are complete.

### Figure calibration

Post's full clone lattice is not the six-node diagram consisting of the top and
its five lower covers; the original classification contains infinite families.
A figure that shows only \(\mathrm{BF}\) above \(T_0,T_1,M,L,S\) must be
captioned **“upper cover of Post's lattice”** or “the five maximal proper
clones,” not “Post's lattice” without qualification.  A full-lattice figure may
highlight these five nodes, but it must not imply that the rest of the lattice
is absent.

## 2. Hilbert CPL and the deduction theorem

### Exact calculus supported by the existing sheet

For formulas in the \(\neg/\to\) language, take the three axiom schemas

\[
\begin{array}{ll}
\mathrm{A1}&\varphi\to(\psi\to\varphi),\\
\mathrm{A2}&(\varphi\to(\psi\to\chi))
 \to((\varphi\to\psi)\to(\varphi\to\chi)),\\
\mathrm{A3}&(\neg\psi\to\neg\varphi)
 \to((\neg\psi\to\varphi)\to\psi),
\end{array}
\]

and modus ponens.  A derivation from \(\Gamma\) is a finite sequence whose
members are hypotheses in \(\Gamma\), axiom instances, or modus-ponens
consequences of earlier members.  This is the system documented in the live
`sheet:hilbert-cpl`; Mendelson's Chapter 1 is the authoritative modern source
for this presentation and its metatheory.

### Deduction theorem

**Source-verified statement.**  For any set \(\Gamma\) of formulas,

\[
\Gamma\cup\{\varphi\}\vdash\psi
\quad\Longleftrightarrow\quad
\Gamma\vdash\varphi\to\psi.
\]

The right-to-left direction is one application of modus ponens after taking
\(\varphi\) as a hypothesis.  The left-to-right direction is proved by induction
on the finite derivation.  The three induction cases are:

1. If a line \(\theta\) is an axiom or belongs to \(\Gamma\), combine it with
   A1 to derive \(\varphi\to\theta\).
2. If the line is \(\varphi\), derive \(\varphi\to\varphi\) from A1 and A2.
3. If \(\theta\) follows by MP from \(\eta\) and \(\eta\to\theta\), apply the
   induction hypotheses and A2 to obtain \(\varphi\to\theta\).

The proof uses A1, A2, and MP; A3 is not used.  This is a metatheorem about
derivations, not an additional object-language axiom or calculus rule.  It
therefore belongs in the annex, while the body should state it and reference
the calculus sheet.

**Do not claim.**  Soundness and completeness show that Hilbert, natural
deduction, and LK derive the same classical consequences.  That extensional
equivalence alone does not establish length-preserving proof translations or
proof-complexity equivalence.

## 3. Classical propositional tableaux adequacy

Smullyan's *First-Order Logic*, Part I, develops propositional logic explicitly
from the viewpoint of analytic tableaux (preliminaries pp. 3--14, tableaux
pp. 15--30, compactness pp. 30--40).  The following is the calibrated finite
adequacy statement for a standard analytic tableau sheet.

**Source-verified theorem, calibrated to finite input.**  Let \(\Gamma\) be a
finite set of classical propositional formulas.  If every compound formula is
eventually expanded once by the appropriate truth-preserving tableau rule,
then the completed tableau for \(\Gamma\) is closed iff \(\Gamma\) is
unsatisfiable.  Equivalently,

\[
\Gamma\vDash\varphi
\quad\Longleftrightarrow\quad
\text{the completed tableau for }\Gamma\cup\{\neg\varphi\}
\text{ is closed}.
\]

The soundness invariant is local: each rule preserves satisfiability on at
least one successor branch, so a closed tableau cannot begin with a satisfiable
set.  For completeness, a saturated open branch assigns each atom according
to the literal occurring on the branch; the no-clash condition and induction
on formulas show that this valuation satisfies the branch and hence the root.
Because the input has finitely many subformulas and each is expanded only once
per branch, systematic propositional search terminates.  This yields a decision
procedure, although not a polynomial-time bound.

**Do not claim.**  A finite tableau proof system's strong completeness for
arbitrary infinite premise sets incorporates a compactness assertion.  Do not
state the finite adequacy theorem as if it by itself proved arbitrary-language
compactness; that set-theoretic strength is treated in Section 7 below.

## 4. Propositional interpolation

### Exact statement

For a formula \(A\), write \(\operatorname{Var}(A)\) for its set of
propositional variables.  **Craig interpolation for CPL** is:

> If \(A\vDash B\), then there is a formula \(I\) such that
> \[
> A\vDash I,\qquad I\vDash B,\qquad
> \operatorname{Var}(I)\subseteq
> \operatorname{Var}(A)\cap\operatorname{Var}(B).
> \]

The theorem is a propositional special case of Craig's 1957 interpolation
theorem.  The citation supports the theorem's provenance; the following finite
truth-table construction is **derived here**, not attributed to Craig's proof.

Let \(S=\operatorname{Var}(A)\cap\operatorname{Var}(B)\).  For every assignment
\(s:S\to\{0,1\}\) that extends to a valuation satisfying \(A\), form the
complete conjunction

\[
m_s:=\bigwedge_{p\in S}
\begin{cases}p,&s(p)=1,\\ \neg p,&s(p)=0.\end{cases}
\]

and let \(I\) be the disjunction of all such \(m_s\).  Then \(A\vDash I\).
If some valuation satisfied \(I\land\neg B\), choose the corresponding \(s\)
and an extension satisfying \(A\).  Combine that extension's values on the
variables occurring only in \(A\) with the first valuation's values on the
variables occurring only in \(B\); agreement on \(S\) would produce a
valuation of \(A\land\neg B\), contradicting \(A\vDash B\).  Hence
\(I\vDash B\).

The empty cases must be explicit.  An empty disjunction is \(\bot\); an empty
conjunction is \(\top\).  Thus, when \(A\) and \(B\) share no variables, the
interpolant is a truth constant: \(\bot\) if \(A\) is unsatisfiable, otherwise
\(\top\) (and then \(B\) must be valid).  A statement that requires a shared
variable unnecessarily weakens the theorem when \(\bot,\top\) are available.

## 5. Tseitin CNF transformation

### Exact construction and bound

Let \(C\) be a Boolean circuit, or a formula regarded as its syntax tree, with
bounded-arity gates.  Introduce a fresh variable \(y_g\) for every internal
gate \(g\), and add a constant-size CNF definition of \(y_g\) in terms of its
inputs.  For the standard gates:

\[
\begin{array}{ll}
y\leftrightarrow(a\land b):&
(\neg y\lor a)\land(\neg y\lor b)\land(y\lor\neg a\lor\neg b),\\[2pt]
y\leftrightarrow(a\lor b):&
(y\lor\neg a)\land(y\lor\neg b)\land(\neg y\lor a\lor b),\\[2pt]
y\leftrightarrow\neg a:&
(\neg y\lor\neg a)\land(y\lor a).
\end{array}
\]

Conjoin all gate definitions and the unit clause \(y_r\) for the output gate
\(r\).  If the circuit has \(s\) gates, the output has \(O(s)\) clauses and
literal occurrences; with these gates every clause has width at most three.

**Source-verified modern claim.**  Tseitin encoding converts an arbitrary
propositional formula to an equisatisfiable CNF formula with only linear size
increase.  The original 1968 paper is the historical source; Prestwich's
*Handbook of Satisfiability* chapter and the CMU propositional-encodings notes
state the modern encoding claim explicitly.

The full biconditional construction above has the stronger projection property
(**derived here**): every assignment of the original variables extends
uniquely to the gate variables by evaluating the circuit, and it satisfies the
CNF with \(y_r\) iff it makes the original formula true.  If \(\mathbf y\) is
the tuple of auxiliary variables, the precise equivalence is

\[
C(\mathbf x)\quad\Longleftrightarrow\quad
\exists\mathbf y\,T_C(\mathbf x,\mathbf y).
\]

**Do not claim.**  \(C\) and \(T_C\) are not literally equivalent formulas in
the same vocabulary: \(T_C\) contains fresh variables.  “Equivalent CNF” is
therefore wrong unless the existential projection is displayed.  Also do not
transfer the unique-extension claim to one-direction/polarity encodings such
as Plaisted--Greenbaum without a separate proof.

## 6. SAT, TAUT, and tractable fragments

### General complexity statements

Let `SAT` be the set of satisfiable Boolean formulas and `TAUT` the set of
formulas true under every valuation.

- **Source-verified (modern formulation):** SAT, including CNF-SAT, is
  NP-complete under polynomial-time many-one reductions.  Arora and Barak,
  Theorem 2.10, states SAT and 3SAT in this form.
- Cook's 1971 primary paper is the historical source.  Its abstract is framed
  using polynomial oracle reducibility and tautologyhood, so a handbook using
  the current many-one definition should cite an authoritative modern
  formulation alongside Cook rather than silently treating the formulations as
  verbatim identical.
- **Source-verified (modern formulation):** TAUT is coNP-complete under the
  same reductions.  Arora and Barak define polynomial-time Karp reduction as
  polynomial-time many-one (mapping) reduction in Definition 2.7, p. 42, and
  state the TAUTOLOGY classification in Example 2.21, p. 56.  Independently,
  membership follows because a falsifying valuation certifies non-tautology;
  for hardness, negation is a linear-time map and
  \(\varphi\in\mathrm{SAT}\) iff
  \(\neg\varphi\notin\mathrm{TAUT}\); equivalently, TAUT is the complement,
  up to this map, of an NP-complete language.

NP-completeness is a classification, not an unconditional lower bound.  The
correct framing is: SAT has a polynomial-time algorithm iff \(\mathsf P=\mathsf
NP\).  It is not known that \(\mathsf P\ne\mathsf{NP}\).  Likewise, calling
TAUT “NP-complete” would exchange NP and coNP and is not licensed.

### Tractable-fragment table

Let \(N\) be the total number of literal occurrences in a CNF input; let \(m\)
and \(n\) be the numbers of equations and variables for a parity input.

| Fragment | Exact syntactic standing | Algorithm and supported bound | Evidence |
|---|---|---|---|
| Horn-SAT | every CNF clause has at most one positive literal | forward chaining / indexed unit propagation; \(O(N)\) | Dowling--Gallier 1984, source-verified |
| dual-Horn-SAT | every CNF clause has at most one negative literal | complement every variable, solve the resulting Horn instance; \(O(N)\) | derived from Dowling--Gallier; the transformation is linear |
| 2-SAT | every CNF clause has at most two literals | build the implication graph; satisfiable iff no variable and its negation lie in the same strongly connected component; \(O(N)\) | Aspvall--Plass--Tarjan 1979, source-verified |
| XOR-SAT | a conjunction of parity equations \(\ell_1\oplus\cdots\oplus\ell_k=b\) | absorb negated literals into \(b\), then Gaussian elimination over \(\mathbb F_2\); polynomial time, e.g. \(O(mn\min\{m,n\})\) field operations by dense elimination | polynomial tractability is covered by Schaefer 1978; the displayed reduction is elementary linear algebra |

A satisfiable Horn theory need not have a unique model; the forward-chaining
algorithm computes its least model.  Avoid “unique satisfying assignment.”
The dual-Horn claim is not a second independent algorithm: it is the exact
linear reduction \(x\mapsto\neg x\) followed by Horn-SAT.  For XOR-SAT,
\(\neg x\) is \(x\oplus1\), so constants are moved to the equation's right-hand
side before elimination.

Schaefer's dichotomy provides a broader classification, but it should not be
compressed into “every non-Horn fragment is NP-complete”: bijunctive (2-SAT),
affine (XOR-SAT), Horn, dual-Horn, and the constant-valid cases are tractable
families in its generalized setting.

## 7. BPI, the Ultrafilter Lemma, and propositional compactness

### Exact principles

Work over \(\mathsf{ZF}\).  The three principles are:

1. **Boolean Prime Ideal Theorem (BPI):** every nontrivial Boolean algebra has
   a prime ideal (equivalently, every proper ideal extends to a prime ideal).
2. **Ultrafilter Lemma:** every proper filter on a Boolean algebra extends to an
   ultrafilter.
3. **Arbitrary-language propositional compactness:** for every set \(P\) of
   propositional variables and every set \(\Gamma\) of finitary formulas over
   \(P\), if every finite subset of \(\Gamma\) is satisfiable, then \(\Gamma\)
   is satisfiable.

**Source-verified theorem.**  These principles are equivalent over
\(\mathsf{ZF}\).  Paseau and Leek explicitly state the Ultrafilter Lemma /
compactness equivalence and list BPI among the ZF-equivalents, referring to
Jech, Chapter 2, and Howard--Rubin, Form 14.  Their propositional proof uses the
Lindenbaum Boolean algebra: finite consequences of a finitely satisfiable
\(\Gamma\) form a proper filter; extend it to an ultrafilter and read the
ultrafilter as a valuation.

For the converse, the following standard construction records what the
handbook statement commits to (**derived here from compactness**).  Given a
Boolean algebra \(B\), introduce one atom \(p_b\) for each \(b\in B\) and impose

\[
p_1,\quad\neg p_0,\quad
p_{\neg b}\leftrightarrow\neg p_b,\quad
p_{b\land c}\leftrightarrow(p_b\land p_c)
\]

for all \(b,c\in B\).  Every finite subset is satisfiable: the finitely many
mentioned elements generate a finite Boolean subalgebra, which has a
two-valued homomorphism.  Compactness supplies a valuation of the whole theory,
hence a homomorphism \(h:B\to\mathbf2\); \(h^{-1}(0)\) is a prime ideal and
\(h^{-1}(1)\) an ultrafilter.

### Scope warning

The reverse implication needs a propositional language with one variable for
each member of an arbitrary Boolean algebra.  Therefore the handbook must say
“for arbitrary sets of propositional variables” (or state the all-cardinals
scheme).  Do **not** attach the BPI equivalence without qualification to only
the manuscript's fixed countable alphabet; that restricted statement does not
by itself encode arbitrary Boolean algebras.

BPI is weaker than full Choice in relative consistency strength; the separate
evidence and exact conditional wording are already recorded in
`spec/research/p01-ultrafilter-lemma.md`.  Do not call BPI or the Ultrafilter
Lemma another name for AC.

## 8. Source ledger and exact metadata

### Functional completeness

1. Emil L. Post, *The Two-Valued Iterative Systems of Mathematical Logic*,
   Annals of Mathematics Studies 5, Princeton University Press, 1941, 122 pp.,
   eISBN 978-1-4008-8236-6.  The publisher-backed
   [JSTOR book record](https://www.jstor.org/stable/j.ctt1bgzb1r) provides the
   metadata; [§26, pp. 105--118](https://www.jstor.org/stable/j.ctt1bgzb1r.29)
   states the five-immediate-predecessor criterion.  Suggested key:
   `Post1941`.
2. Francis Jeffry Pelletier and Norman M. Martin, “Post's Functional
   Completeness Theorem,” *Notre Dame Journal of Formal Logic* 31(3) (1990),
   462--475, DOI
   [10.1305/ndjfl/1093635508](https://doi.org/10.1305/ndjfl/1093635508).
   An [author-hosted article PDF](https://www.sfu.ca/~jeffpell/papers/PostPellMartin.pdf)
   gives the modern five-property statement.  Suggested key:
   `PelletierMartin1990`.
3. Henry Maurice Sheffer, “A Set of Five Independent Postulates for Boolean
   Algebras, with Application to Logical Constants,” *Transactions of the
   American Mathematical Society* 14(4) (1913), 481--488, DOI
   [10.2307/1988701](https://doi.org/10.2307/1988701); the
   [JSTOR issue record](https://www.jstor.org/stable/i308118) confirms author,
   title, issue, and pages.  Suggested key: `Sheffer1913`.

### Proof systems and interpolation

4. Elliott Mendelson, *Introduction to Mathematical Logic*, 4th ed., Chapman
   & Hall, 1997, x + 440 pp., ISBN 0-412-80830-7 / 978-0-412-80830-2.  The
   [Google Books record](https://books.google.com/books?id=ZO1p4QGspoYC)
   confirms edition, publisher-year record, ISBNs, and Chapter 1; the deduction
   theorem is Proposition 1.9 in this presentation.  Suggested key:
   `Mendelson1997`.
5. Raymond M. Smullyan, *First-Order Logic*, Ergebnisse der Mathematik und
   ihrer Grenzgebiete, 2. Folge, vol. 43, Springer, 1968, XII + 160 pp., DOI
   [10.1007/978-3-642-86718-7](https://doi.org/10.1007/978-3-642-86718-7).
   The [Springer record](https://link.springer.com/book/10.1007/978-3-642-86718-7)
   identifies the propositional analytic-tableaux chapters and page ranges.
   Suggested key: `Smullyan1968`.
6. William Craig, “Three Uses of the Herbrand--Gentzen Theorem in Relating
   Model Theory and Proof Theory,” *The Journal of Symbolic Logic* 22(3)
   (1957), 269--285, DOI
   [10.2307/2963594](https://doi.org/10.2307/2963594).  Existing key:
   `Craig1957`.

### CNF and complexity

7. G. S. Tseitin, “On the Complexity of Derivation in Propositional
   Calculus,” originally *Zapiski Nauchnykh Seminarov LOMI* 8 (1968),
   234--259; [MathNet primary record and scan](https://www.mathnet.ru/eng/znsl2268).
   English translation in J. H. Siekmann and G. Wrightson (eds.), *Automation
   of Reasoning 2*, Springer, 1983, 466--483, DOI
   [10.1007/978-3-642-81955-1_28](https://doi.org/10.1007/978-3-642-81955-1_28).
   Existing key: `Tseitin1968` (the live entry cites the translation and notes
   the 1968 original).
8. Steven Prestwich, “Chapter 2: CNF Encodings,” in Armin Biere, Marijn Heule,
   Hans van Maaren, and Toby Walsh (eds.), *Handbook of Satisfiability*, 2nd
   ed., Frontiers in Artificial Intelligence and Applications 336, IOS Press,
   2021, 75--100, DOI
   [10.3233/FAIA200985](https://doi.org/10.3233/FAIA200985).  The
   [University College Cork record](https://research.ucc.ie/en/publications/chapter-2-cnf-encodings/)
   supplies complete metadata and identifies Tseitin encodings as a subject.
   Suggested key: `Prestwich2021`.
9. Stephen A. Cook, “The Complexity of Theorem-Proving Procedures,” in
   *Proceedings of the Third Annual ACM Symposium on Theory of Computing*,
   ACM, 1971, 151--158, DOI
   [10.1145/800157.805047](https://doi.org/10.1145/800157.805047).  Existing
   key: `Cook1971`.
10. Sanjeev Arora and Boaz Barak, *Computational Complexity: A Modern
    Approach*, Cambridge University Press, 2009, ISBN 978-0-521-42426-4.  The
    [authors' official book page](https://theory.cs.princeton.edu/complexity/)
    hosts the draft; [Chapter 2](https://theory.cs.princeton.edu/complexity/NPchap.pdf),
    Theorem 2.10 states SAT and 3SAT NP-completeness in the modern formulation.
    In the published edition, Definition 2.7 (p. 42) identifies Karp reduction
    with polynomial-time many-one/mapping reduction, and Example 2.21 (p. 56)
    states that TAUTOLOGY is coNP-complete; the corresponding author-draft item
    is Example 2.23.
    Suggested key: `AroraBarak2009`.
11. William F. Dowling and Jean H. Gallier, “Linear-Time Algorithms for
    Testing the Satisfiability of Propositional Horn Formulae,” *The Journal of
    Logic Programming* 1(3) (1984), 267--284, DOI
    [10.1016/0743-1066(84)90014-1](https://doi.org/10.1016/0743-1066(84)90014-1).
    The [publisher record](https://www.sciencedirect.com/science/article/pii/0743106684900141)
    states the \(O(N)\) bound with \(N\) equal to total literal occurrences.
    Suggested key: `DowlingGallier1984`.
12. Bengt Aspvall, Michael F. Plass, and Robert E. Tarjan, “A Linear-Time
    Algorithm for Testing the Truth of Certain Quantified Boolean Formulas,”
    *Information Processing Letters* 8(3) (1979), 121--123, DOI
    [10.1016/0020-0190(79)90002-4](https://doi.org/10.1016/0020-0190(79)90002-4).
    The [Princeton publication record](https://collaborate.princeton.edu/en/publications/a-linear-time-algorithm-for-testing-the-truth-of-certain-quantifi/)
    supplies the exact metadata and identifies 2-CNF, 2-satisfiability, and
    strongly connected components.  Suggested key: `AspvallPlassTarjan1979`.
13. Thomas J. Schaefer, “The Complexity of Satisfiability Problems,” in
    *Proceedings of the Tenth Annual ACM Symposium on Theory of Computing*,
    ACM, 1978, 216--226, DOI
    [10.1145/800133.804350](https://doi.org/10.1145/800133.804350).  The
    [ACM record](https://dl.acm.org/doi/10.1145/800133.804350) states the
    polynomial/NP-complete dichotomy and its inclusion of 2-SAT.  Suggested
    key: `Schaefer1978`.

### Choice-strength calibration

14. A. C. Paseau and Robert Leek, “The Compactness Theorem,” *Internet
    Encyclopedia of Philosophy*, 23 March 2022,
    [stable entry](https://iep.utm.edu/compactness/), especially §§4a and 7a.
    The [University of Birmingham record](https://research.birmingham.ac.uk/en/publications/the-compactness-theorem/)
    confirms authorship and date.  Suggested key: `PaseauLeek2022`.
15. Thomas J. Jech, *The Axiom of Choice*, Studies in Logic and the
    Foundations of Mathematics 75, North-Holland, 1973, xi + 202 pp., ISBN
    0-444-10484-4.  Chapter 2, “Use of the Axiom of Choice,” pp. 9--30, DOI
    [10.1016/S0049-237X(08)71753-1](https://doi.org/10.1016/S0049-237X(08)71753-1),
    treats the Boolean Prime Ideal Theorem.  Suggested key: `Jech1973Choice`.
16. Paul Howard and Jean E. Rubin, *Consequences of the Axiom of Choice*,
    Mathematical Surveys and Monographs 59, American Mathematical Society,
    Providence, RI, 1998, viii + 432 pp., DOI
    [10.1090/surv/059](https://doi.org/10.1090/surv/059), ISBN 0-8218-0977-6.
    The [AMS book record](https://bookstore.ams.org/SURV/59) supplies the
    metadata; Form 14 is the compactness/BPI family referenced by Paseau and
    Leek.  Suggested key: `HowardRubin1998`.

## 9. Unsupported or easily overclaimed formulations

- “A basis is complete iff one connective fails all five Post properties” is
  false; the witnesses may be different members of the basis.
- A six-node top fragment is not the whole of Post's lattice.
- The deduction theorem is not a fourth Hilbert rule, and its pure-CPL form
  should not be copied without side conditions into calculi with extra rules.
- Tableau closure for finite input does not by itself establish strong
  completeness for arbitrary premise sets.
- Craig interpolation must cover the empty shared-vocabulary case with truth
  constants, or expressly restrict the statement.
- Tseitin output is equisatisfiable (and equivalent after existentially
  forgetting auxiliaries), not literally equivalent in the expanded
  vocabulary.
- Cook's historical reducibility formulation and the modern many-one
  Cook--Levin theorem should not be described as textually identical.
- TAUT is coNP-complete; the unresolved \(\mathsf P\) versus \(\mathsf{NP}\)
  question forbids an unconditional “requires exponential time” gloss.
- A Horn formula may have many models even though forward chaining computes a
  least one.
- The BPI/compactness equivalence is an arbitrary-language statement; the
  reverse direction is not supplied by a theorem restricted to a single fixed
  countable alphabet.
