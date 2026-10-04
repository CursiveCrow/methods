# Round 2 mathematical and proof-correctness review

## Result

The reconstruction is mathematically sound on normal form, finite memory,
topology, continuous finite realization, general solutions, fixed
anticipation, explicit synthesis, and the weak-system bridge, except for one
source-inherited but unqualified empty-language counterexample in the
finite-word converse.  That error is a must-fix because the reader currently
states a false theorem.

## Independence, competence, and evidence

This is a blind review of the seven Round 2 objects named in the charter.  I
did not read a Round 1 report, another Round 2 report, the board ledger, or the
chair transcript, and I did not contact another reviewer.  I did not inspect a
handbook PDF or run a test, checker, repository script, TeX command, or build.

I can parse mathematical Russian at a working level, including the theorem
headings, hypotheses, proof prose, formula syntax, and terminology used in
these two papers.  I am not a credentialed Russian-language specialist and do
not certify literary or philological nuance.  For this proof seat I used the
complete printed Russian scans at original visual detail, checked every
reported formula and theorem against the printed page, and used the two OCR
files only to navigate to already inspected print.  The source note and compact
record were checked as frozen claims, not treated as substitutes for the
printed sources.

## Frozen identity check — M01 checked-clean

The seven SHA-256 values recomputed before substantive review match the charter
exactly:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| trakhtenbrot-1961.pdf | 44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9 | match |
| trakhtenbrot-1962-expanded.pdf | EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D | match |
| n-c-014.tex | 109A631EBAFAC28A7C84A946FE4E305E91BA1818B7E4E9F08FCF4E15E4B95B72 | match |
| logic-in-computer-science.tex | A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD | match |
| handbook.bib | 75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C | match |
| p09-trakhtenbrot-1961-source-note.md | 6D84E96A50414E10FE229536D3E8A4557BEB45D2D0024DF182E6AD75D3DD41DC | match |
| p09-source-presentations-lot2-3.md | DFFF60FBB6E0C715A9B41D7000D670B374B0B62A86305AC2BAF92CA46726A687 | match |

The hashes are used only as identity labels.

## Complete visual source inspection — M02 checked-clean

All four announcement images and all twenty-nine expansion images were opened
at original detail.  The announcement physical-page map is:

| Physical page | Printed page | Visually checked contents |
|---:|---:|---|
| 1 | 326 | journal/volume/year, Russian title, formal-system comparison, conditional algorithm, lower/upper terminology, beginning of canonical equations |
| 2 | 327 | canonical equations, anticipation, Theorem 1, Cantor-space portions, homogeneous basis, Theorem 2 |
| 3 | 328 | Theorem 3 and closure characterization, Theorem 4, Theorem \(4'\), graph/solution distinction, both clauses of general solution, Theorem 5 |
| 4 | 329 | Putnam corollary, Church/Robinson/Elgot remarks, receipt and bibliography |

The expansion map is physical page \(j\) to printed page \(102+j\):

| Physical | Printed | Visually checked contents |
|---:|---:|---|
| 1 | 103 | journal identity, title, introduction |
| 2 | 104 | aims, section map, beginning of \(\mathcal I\) |
| 3 | 105 | syntax, primitive successor, eliminable extensions, semantic fictitious occurrence |
| 4 | 106 | dependence examples and controlled \(t\)-formulae |
| 5 | 107 | controlled-quantifier elimination |
| 6 | 108 | lower/upper normal form and proof start |
| 7 | 109 | normal-form proof completion and operator section start |
| 8 | 110 | anticipation, residual operators, whole-suffix finite-memory equations |
| 9 | 111 | weight, finite operators, \(A\)-operators, one-state future-dependence example |
| 10 | 112 | primitive-recursive recognition/synthesis impossibility |
| 11 | 113 | canonical-equation embedding in \(\mathcal I\), Cantor geometry |
| 12 | 114 | product topology, portions, compactness facts, homogeneity definition start |
| 13 | 115 | homogeneous basis, examples, internal/external transitions |
| 14 | 116 | covering operator and recurrence, definability Theorem 1 start |
| 15 | 117 | effective homogeneity proof |
| 16 | 118 | singleton result, nondefinable homogeneous example, closed converse and closure characterization |
| 17 | 119 | effectiveness qualification and section 4 setup |
| 18 | 120 | continuous finite-realization proof, discontinuous Theorem 2, general-solution definition start |
| 19 | 121 | both general-solution clauses, Theorem 3, stable-family definition |
| 20 | 122 | deletion process and canonical general-solution equations |
| 21 | 123 | parameter completeness and soundness induction |
| 22 | 124 | closedness completion, fixed-\(p\) Theorem \(3'\), section 5 start |
| 23 | 125 | explicit-definition criteria and synthesis Theorem 1 |
| 24 | 126 | shifted-formula construction and worked example start |
| 25 | 127 | worked tables, word-set definitions, Theorem 2 statement and proof start |
| 26 | 128 | both directions of Theorem 2 and the no-prefix proof branch, Theorem 10 start |
| 27 | 129 | Theorem 10 and explicit \(t\)-formula reduction |
| 28 | 130 | \(\mathcal I'\), special beginnings, Theorem 3 |
| 29 | 131 | Theorem 3 corollaries, receipt, bibliography |

The printed map is continuous: announcement pp. 326--329 and expansion
pp. 103--131, with no missing, duplicate, or silently transferred page.

## Must-fix finding

### R2-MP-01 — The finite-word converse omits the necessary nonemptiness hypothesis

**Severity:** must-fix.

**Frozen locations:** n-c-014.tex lines 729--744, especially 741--744;
p09-trakhtenbrot-1961-source-note.md lines 364--375; and
p09-source-presentations-lot2-3.md line 656.  Each says that an
automaton-decidable positive-length word language is automaton-enumerable if it
is prefix-closed and every member has a longer extension.

**Controlling print:** expanded p. 127, Section 5, Theorem 2(ii), continuing on
p. 128.  The source itself prints the two stated conditions without a
nonemptiness condition.  Its proof on p. 128 exposes the omission: when the
input word has no prefix in \(R\), the proposed enumerator is told to output
the first length-\(t\) word in \(R\).  No such word exists when \(R\) is empty.

**Counterexample.**  Work in the source's binary positive-length word setting
and take \(L=\varnothing\).

1. \(L\) is automaton-decidable.  A one-state \(A\)-operator with constant
   output \(0\) and a self-loop has terminal result \(0\) on every input word.
2. \(L\) is prefix-closed and every member has a longer extension in \(L\),
   both vacuously.
3. \(L\) is not automaton-enumerable.  For every \(t\geq1\), the binary input
   set contains a word \(u\), and a total length-preserving \(A\)-operator has
   an output \(T_t(u)\).  Hence \(T_t(A^t)\neq\varnothing\), whereas
   \(L\cap B^t=\varnothing\).

Thus the displayed reader claim is false as written.  This is not an
aesthetic objection and cannot be discharged by modern regular/MSO folklore.
The smallest correction is to add \(L\neq\varnothing\) to the converse in all
three frozen prose locations.  For positive-length languages, nonemptiness
together with prefix closure and proper extendibility supplies a word of every
positive length, exactly the seed used by the p. 128 construction.  Because
the printed theorem omits the condition, the reader should identify this as a
handbook-owned edge-case correction rather than silently attributing the
repaired statement to Trakhtenbrot.

## Mathematical derivation and mandatory-point audit

### M05 — checked-clean

Expanded pp. 103--105 support n-c-014.tex lines 499--510.  Individuals have
type \(\mathbb N_+=\{1,2,\ldots\}\); predicate variables have type
\(\mathcal P(\mathbb N_+)\); and immediate successor is the only nonlogical
primitive.  Predicate application to an individual term is atomic.  Equality,
order, bounded individual quantifiers, constants, and \(t+k\) are explicitly
eliminable.  The weak system \(\mathcal I'\) on pp. 130--131 changes only the
predicate-variable domain to eventually-zero predicates.  The standing of
\(\mathcal I\) as an interpreted language, rather than an automaton or set, is
unambiguous.

### M06 — checked-clean

Expanded pp. 105--109 and announcement pp. 326--327 support n-c-014.tex
lines 512--525.

Semantic fictitious occurrence is invariance of truth under changes outside
the stated interval.  It is stronger and more precise than absence of a
written occurrence.  An upper-controlled formula can be eliminated into a
finite Boolean dependence after fixing \(t\); the dual lower/upper forms have
different domains of dependence: a lower form uses a bounded prefix through
\(t+s\), while an upper form uses the tail from \(t\).

The normal-form proof is type-correct.  Predicate quantifiers are first moved
outside the individual-quantifier block.  Individual quantifiers are pushed
inward and split at \(t\), producing a prefix-dependent part and a
tail-dependent part.  For an existential predicate quantifier applied to a
conjunction of independent lower and upper pieces, one direction is immediate.
For the other, predicates witnessing the two pieces can be spliced because the
pieces inspect disjoint sides of the cut; the source's p. 109 construction
does exactly this.  Boolean distribution then returns a Boolean combination of
lower and upper \(t\)-formulae.  No effective step assumes a decision
procedure for closed \(\mathcal I\)-sentences.

### M07 — checked-clean

Expanded pp. 109--112 support n-c-014.tex lines 527--572.

For \(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\), anticipation at most \(p\)
means that equality of input prefixes through \(t+p\) implies equality of the
output at \(t\).  At \(p=0\), this is equivalent to the compatible family of
prefix maps.  Finite memory instead gives a finite state \(q(t)\) but permits
both output and next state to be arbitrary functions of the whole suffix
\(a_{\geq t}\).  The least finite state-set size is weight.  Adding one
uniform finite \(p\) yields the finite-window equations for a finite operator.
Setting \(p=0\) yields the automaton-realizable class called Л in 1961 and
\(A\) in 1962.  These implications are all one-way where the reader says they
are: finite memory alone does not give a lookahead bound, and zero anticipation
alone does not give finite memory.

### M08 — checked-clean

Expanded pp. 111--112 support n-c-014.tex lines 551--554 and 574--581.

The source's one-state operator
\[
 b(t)=1\quad\Longleftrightarrow\quad
 \exists \tau>t\;a(\tau)=1
\]
has finite memory of weight one but no bounded anticipation and no finite-prefix
effective evaluation.  It is the required minimal witness against collapsing
finite memory into finite operator.

The primitive-recursive boundary is also exact.  A constant operator generated
by a primitive-recursive sequence is an \(A\)-operator exactly when the
sequence is ultimately periodic, a property not decidable from an arbitrary
primitive-recursive scheme.  For synthesis, the source transforms a scheme
into an always ultimately-periodic eventual-indicator; canonical finite-state
extraction would decide whether the original scheme is identically zero.
Thus both recognition and synthesis are genuinely negative boundaries, not
mere absence of an algorithm in the paper.

### M09 — checked-clean

Expanded pp. 113--116 support n-c-014.tex lines 583--602.

For a finite word \(u\), \(M_u=\{Z:uZ\in M\}\) is well-typed; for tuple
streams, both the prefix and tail are taken coordinatewise.  Appending one
letter to \(u\) sends a basis portion to another basis portion, so the internal
transition is a function on the finite basis.  Empty portions cause no
problem: they transition to the empty portion and arbitrary external values
there are unreachable from a nonempty current portion.

The graph of a zero-anticipation finite-memory operator is closed because
agreement on longer input prefixes fixes equally long output prefixes.  Its
portion after a compatible input/output prefix is determined by the residual
memory state, giving degree at most the number of states.  A singleton's
portions are its successive tails, so it has finitely many portions exactly
when the stream is ultimately periodic.  The p. 115 family indexed by an
arbitrary irrational binary expansion supplies uncountably many
one-homogeneous sets, while there are only countably many formulas.  Closedness
is therefore not replaceable by homogeneity in the converse.

### M10 — checked-clean

Expanded pp. 116--118 support n-c-014.tex lines 604--607.

After normal form, fixing a finite prefix turns each lower formula into one of
finitely many Boolean functions of its bounded fringe, while upper formulae
remain among a finite syntactic family.  Consequently only finitely many
residual defining formulae can occur, proving homogeneity of every
\(\mathcal I\)-definable set.  Given a residual formula and an appended bit,
the next residual formula is computed by substitution and normalization; this
constructs the internal transition without a truth or nonemptiness oracle.
The reader correctly reserves the oracle issue for external choice.

### M11 — checked-clean

Expanded pp. 116--119 support n-c-014.tex lines 607--631.

Let \(M_1=M,M_2,\ldots,M_k\) be the distinct portions of a homogeneous set.
At a nonempty \(M_i\), a choice bit selects an allowed next output bit; the
internal transition selects the corresponding next portion.  Starting from
the literal one-hot state \(q_1(1)=1\), \(q_j(1)=0\) for \(j>1\), this gives the
displayed recurrence with free \(X\), bound state predicates \(q_j\), bound
choice predicate \(U\), and quantifier-free current/next matrix.

Every output of the recurrence lies in \(\overline M\): each of its finite
prefixes is realized by a point of \(M\).  Conversely, every point of
\(\overline M\) determines compatible choices.  Hence the recurrence defines
exactly \(\overline M\), and closedness is precisely what changes that set to
\(M\).  Conversely, a recurrence of this form is the projection of a closed
finite-state constraint over compact Cantor spaces, so it is closed; its
residual is determined by one of finitely many state values, so it is
homogeneous.  The fixed initial state is essential and is present in the
reader.

Complement and finite union realize Boolean operations, predicate projection
realizes existential predicate quantification, and intersection follows by
De Morgan.  This yields the stated least closure class without settling the
announcement's open Borel/projective classification question.

### M12 — checked-clean

Expanded pp. 117--119 and 124 support n-c-014.tex lines 633--640 and
681--699.

Residual normalization and internal transition are unconditional.  External
choice requires knowing which residual formulae define nonempty portions.
That is exactly where the source assumes a truth algorithm for closed
\(\mathcal I\)-sentences and calls the procedure conditional.  Putnam's
algorithm removes the condition for the existential-predicate,
individual-quantifier, quantifier-free recurrence fragment, not for every
construction merely because a later decision result is known.

### M13 — checked-clean

Announcement p. 328 and expanded pp. 119--120 support n-c-014.tex
lines 642--650.

Let \(G\) be the \(\mathcal I\)-definable graph of a continuous total operator.
Definability gives a finite portion basis of degree \(k\).  Continuity on the
compact input Cantor space makes the graph closed.  Each nonempty graph portion
is the graph of a continuous partial residual operator whose domain is compact.
Uniform continuity of its first output coordinate gives a finite input-window
length.  There are finitely many nonempty portions, so the maximum of these
lengths gives one anticipation bound for all times and all states.  The current
portion is the memory state; outputting one letter and moving to the next
portion gives the internal transition.  Hence the operator is finite and has
weight at most \(k\).  If the original operator has zero anticipation, the
window bound is zero and the result is an Л/\(A\)-operator.  Empty portions are
irrelevant because no run of the total graph reaches them.

### M14 — checked-clean

Expanded p. 120 supports n-c-014.tex lines 650--652.

If continuity is removed but the relation is still exactly a total functional
graph, a finite portion remains sufficient as memory: given the current
portion and the entire future input suffix, functionality determines the next
output and next portion.  Those two functions may be discontinuous and
noneffective.  Therefore Theorem 2 obtains finite memory and the degree weight
bound, but compact uniformity is unavailable and no finite anticipation bound
follows.  The one-state future-existence operator above witnesses strictness.

### M15 — checked-clean

Announcement p. 328 supports n-c-014.tex lines 654--663.

To say that \(\varphi\) defines an operator graph is equality between the
relation and one graph.  To say \(T\) solves \(\varphi\) is only
\(\operatorname{graph}(T)\subseteq\widehat X\widehat Y\varphi(X,Y)\).
Theorem \(4'\) starts with a closed homogeneous relation and a solution, not
an already functional relation.  A continuous solution can be replaced by a
finite solution of weight at most the relation's degree; a
zero-anticipation solution can be replaced by an Л/\(A\)-solution with the
same bound.  The announcement's open-relation analogue omits the weight bound.
The reader preserves all four distinctions.

### M16 — checked-clean

Announcement p. 328 and expanded pp. 120--121 support n-c-014.tex
lines 665--679.

For \(T(X,U)\) to be a general \(A\)-solution, completeness requires
\[
  \forall T_0\,
  \bigl(T_0\text{ is an \(A\)-solution}\Rightarrow
  \exists S\text{ an \(A\)-operator}\;
  T_0(X)=T(X,S(X))\bigr),
\]
and soundness requires
\[
  \forall S\,
  \bigl(S\text{ is an \(A\)-operator}\Rightarrow
  T(X,S(X))\text{ solves }\varphi\bigr).
\]
The source permits multiple parameter streams; packaging them as a finite
tuple is eliminable.  Replacing \(A\)-operator in both clauses, including the
parameter class, by arbitrary zero-anticipation operator yields the separate
general zero-anticipation notion.  Existence of one solution would satisfy
neither quantifier pattern, so the terminology is nonredundant.

### M17 — checked-clean

Announcement pp. 328--329 and expanded pp. 121--124 support n-c-014.tex
lines 681--699.

Starting with the finite basis of residual formulae, delete a formula if its
portion is empty; then delete it if for some current input bit both possible
output-successor residuals have already been deleted.  Iterate to a fixed
point.  A zero-anticipation solution's graph induces a stable subsystem, so if
the initial residual is deleted there can be no such solution.

If the initial residual survives, use its surviving formula index as state.
For each state and current input bit, a parameter bit chooses the output when
both stable output successors survive and is ignored when only one survives.
The corresponding successor residual supplies the next state.  Every finite
prefix produced this way extends inside the relation; because the relation is
closed, the infinite pair belongs to it.  This proves soundness for every
parameter substitution.

Conversely, given any zero-anticipation solution \(T_0\), define the parameter
at time \(t\) to select the stable output actually produced by \(T_0\).
The stable state is determined by the already seen input/output prefix, so this
parameter operator is itself zero-anticipating.  If \(T_0\) is an
\(A\)-operator, combining its finite state with the stable residual state makes
the parameter an \(A\)-operator.  This proves completeness for both named
classes.  The constructed general solution's state set is the surviving
subfamily, so its weight is at most the homogeneity degree.  Emptiness tests,
and only those tests, leave the arbitrary-formula construction conditional.

### M18 — checked-clean

Expanded p. 124 supports n-c-014.tex lines 692--697.

For one fixed \(p\), delay the output by \(p\) places:
\[
 \widetilde Y(1)=\cdots=\widetilde Y(p)=0,\qquad
 \widetilde Y(t+p)=Y(t).
\]
An operator has anticipation at most \(p\) exactly when the delayed operator
has anticipation zero.  Shifting each occurrence of \(Y\) in the relation
transports solutions and parameter substitutions in both directions.  Applying
Theorem 3 to the shifted relation yields the alternative and general solution
for this one \(p\).  Nothing in the reduction identifies the constructions for
different \(p\), and the reader correctly refuses an unbounded-lookahead
parametrization.

### M19 — checked-clean

Expanded pp. 124--127 support n-c-014.tex lines 701--714.

An explicit definition gives a unique total output bit at every time, and its
graph is \(\mathcal I\)-definable; expanded Theorem 2 therefore supplies finite
memory.  It has anticipation at most \(p\) exactly when the defining formula's
truth is independent of input values outside \([1,t+p]\); \(p=0\) gives the
\(A\)-operator criterion.

For a zero-shift prefix-controlled formula, fix the first input column,
evaluate the first output, shift time, and retain the residual formula.  The
normal form admits only finitely many residual formulae, so iteration
terminates and the residuals become states with canonical output and transition
tables.  The example on pp. 126--127 produces exactly the two printed
formulae and the two \(\Phi,\Psi\) tables reported by the reader.

### M20 — finding-linked to R2-MP-01

Expanded pp. 127--128 support the types in n-c-014.tex lines 716--741.
Zero anticipation makes
\(T_t:A^t\to B^t\) independent of the chosen infinite extension and makes the
family prefix-compatible.

The forward word-set direction is correct.  The length-\(t\) range of a finite
letter-to-letter transducer is recognized by existentially guessing an input
and run; equivalently, the source's explicit formula quantifies an input word
whose every output position matches the candidate.  Hence
automaton-enumerable implies automaton-decidable.

For the converse, if \(L\) is nonempty, prefix-closed, and every member has a
proper extension in \(L\), then every member has a one-letter extension in
\(L\): take the first extra letter of any longer extension and use prefix
closure.  Iteration supplies extensions of every desired length.  The source's
enumerator can therefore output the input itself when it lies in \(L\), and
otherwise output the lexicographically first length-\(t\) member extending its
longest \(L\)-prefix.  This proves the repaired theorem.  Without nonemptiness,
R2-MP-01 is the exact counterexample and the source proof has no initial seed.

### M21 — checked-clean

Expanded pp. 130--131 support n-c-014.tex lines 746--755.

In \(\mathcal I'\), every predicate is eventually zero.  A special beginning
\(X(1)\cdots X(t)\) requires the same predicate to be zero at every later
position; it is not an arbitrary prefix.  For an arbitrary
\(\mathcal I\)-formula, the explicit recognition formula existentially chooses
a satisfying predicate, requires it to match the presented prefix, and
requires zero afterward.  This is an \(A\)-operator by the explicit semantic
criterion, but the construction is not claimed effective.  When the original
formula belongs to \(\mathcal I'\), the source invokes Büchi's decision result
to make the operator effectively constructible.  Existence and effective
construction are kept separate.

### M22 — checked-clean

The announcement and expansion are not numbered as if they were one text.
Announcement Theorem 1 is paired with the unnumbered expanded Section 1 normal
form; announcement Theorems 2--3 with expanded Section 3 Theorems 1--\(2'\);
announcement Theorem 4 with expanded Section 4 Theorem 1; announcement
Theorem \(4'\) remains an announcement existence theorem; announcement
Theorem 5 is paired with expanded Section 4 Theorem 3; and expanded Theorems
2 and \(3'\), explicit Section 5 results, examples, and finite-word theorems
are not back-projected into the announcement.  n-c-014.tex lines 487--497,
604--631, 642--699, and 701--755 preserve these strengths.

### M23 — checked-clean

logic-in-computer-science.tex lines 811--825 explicitly labels the displayed
regular/MSO equivalence as a modern formulation, and lines 2341--2347 keep the
announcement, expansion, Büchi precursor/article, Elgot/errata, Thomas, and
Rabin routes distinct.  n-c-014.tex lines 757--790 separately gives the modern
proof architecture: atomic automata, Boolean closure, track projection, and
state-set encoding of a run.  On finite words, order defines successor and
endpoints, while MSO with successor and endpoints defines reachability/order
by quantifying successor-closed sets.  The modern theorem is correct, but it is
not used to prove Trakhtenbrot's broader operator claims or falsely quoted as a
sentence of either Russian paper.

### M26 — checked-clean

Every technical name introduced in the Trakhtenbrot reconstruction has a
necessary distinction, a definition, an explicit standing, a nonredundancy
explanation, and later use.  This includes \(\mathcal I\), semantic fictitious
occurrence, lower/upper \(t\)-formula, anticipation, finite memory, weight,
finite operator, \(A\)-operator as a declared normalization, ultimately
periodic, portion, homogeneous degree, basis, internal transition, general
solution, explicit definition, automaton-enumerable, automaton-decidable,
\(\mathcal I'\), and special beginning.  No hypothetical automaton kind is
invented from portion/basis data.  No definition-after-use or unused named
distinction remains.

### M27 — finding-linked to R2-MP-01; otherwise checked-clean

The audit found no hidden continuity assumption in Theorem 2, no missing
closedness in the converse or general-solution proof, no finite-memory/finite-
operator collapse, no graph/solution collapse, no fixed-\(p\)/unbounded
lookahead collapse, no recurrence-initialization ambiguity, no 1961/1962
numbering transfer, and no modern-source laundering.  R2-MP-01 is the one
false compression: two closure/extension conditions were reported as
sufficient although the source proof also needs a nonempty seed.

### M28 — checked-clean

The frozen records keep this work limited to N-c-014.c, distinguish source
inspection from handbook-PDF or human acceptance, and preserve the
nonredistribution rights boundary.  This review used only direct
source/manuscript reading, visual source-page inspection, mathematical
derivation, citation/provenance inspection, and SHA-256 identity labels.  No
software or rendered-handbook evidence is claimed.

VERDICT: REJECT — R2-MP-01
