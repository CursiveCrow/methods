# Round-one mathematical and proof-correctness review

## Scope and method

I reviewed the six hash-pinned objects named in the charter and no other board
record.  I did not read the ledger, chair transcript, another current or earlier
transcript, or a prior review.  I visually read the required rendered source
pages at original detail: front-matter file pp. 4--5, contents file p. 8, every
Büchi article page (file pp. 12--22 = printed pp. 1--11), and the boundary file
p. 23.  I read every line in each frozen textual scope.  I performed no test,
checker, repository script, TeX command, handbook build, or handbook-PDF
inspection.

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
arose within this seat's mandate.  The detailed derivations below therefore
record why the mathematical claims were checked clean rather than merely
recognizing them as familiar later results.

## Frozen identities (M01)

The independently recomputed SHA-256 values are:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-buchi-1962/logic-methodology-philosophy-science-pageplace-preview-includes-buchi-pp1-11.pdf` | `D37929230CD874D9B6E91CDDE50DD57EAF51D625BC7575878853E4018B64E089` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | `F674BDB103A3B07DEE5925A1D7F3880D92DA31C6442196FB075B2FA85F4ADD24` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `2778CAA3D0EB741A78B9D2EA44BD157E5FCCB4E2F3034ED539D52A9788287A1B` | exact match |
| `handbook/bib/handbook.bib` | `748B159ED5CE40855878D3E8492DA98D0A465B73C68830E5BE11165EFF2ACA6A` | exact match |
| `spec/research/p09-buchi-1962-source-acquisition.md` | `90C23E094604342726B02EC78FE1A4211D56233A063532E8EDA94537676C434B` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `EBC0E39AF016B22F1BA52D7DEEB620DE6B00F5B48AA1F3E0687BB10BBC316508` | exact match |

## Visual source and page-boundary audit (M02--M03)

The rendered title page names *Logic, Methodology and Philosophy of Science:
Proceedings of the 1960 International Congress*, editors Ernest Nagel, Patrick
Suppes, and Alfred Tarski, and Stanford University Press, Stanford, California.
The copyright page prints copyright 1962, `First published 1962`, and the later
printing indicator ending in `77`.  The contents page places J. Richard Büchi's
“On a Decision Method in Restricted Second Order Arithmetic” at printed p. 1
and Julia Robinson's next article at printed p. 12.  The article scan begins
with Büchi's title and author on file p. 12 / printed p. 1, continues without a
gap through the references on file p. 22 / printed p. 11, and file p. 23 visibly
begins Robinson's article on printed p. 12.  Thus the map and article boundary
in reader lines 377--389, source-note lines 1--48, bibliography lines
2276--2288, and compact-record lines 556--558 agree with the images.

The 1962 Stanford identity, pp. 1--11, is kept separate from the 1966 Elsevier
and 1990 Springer republications and their later identifiers.  The public
preview is described only as a research copy; no open-content licence is
inferred.  These provenance claims are correctly bounded and do not enter any
mathematical proof.

## Independent mathematical rederivation

### 1. The formalism, word encoding, and formula classes (M04--M06, M08)

Printed p. 1 makes the two domains unambiguous: individual variables range over
the natural numbers and monadic predicate variables range over arbitrary
subsets of the natural numbers.  The nonlogical vocabulary is (0) and unary
successor, with propositional connectives and quantifiers of both sorts.  Thus
\(SC\) is an interpreted formalism, not an automaton or a class of languages.
Reader lines 391--400 and source-note lines 78--96 reproduce exactly that
standing.

For \(\mathbf i=(i_1,\ldots,i_k)\), define
\(\mathbf i(n)=(\mathbf1_{i_1}(n),\ldots,\mathbf1_{i_k}(n))\).  This is a
letter of \(\{0,1\}^k\), and the assignment itself is therefore the infinite
word \(\mathbf i(0)\mathbf i(1)\cdots\).  No second sequence has been introduced
at this point.  A later existential tuple \(\mathbf r\), not the input word,
supplies the finite-state witness.  Reader lines 402--419 and printed p. 3 keep
that distinction exact.

The four displayed clauses at reader lines 421--444 agree symbol-for-symbol in
quantifier polarity with printed p. 2:

* \(\Sigma_1\) has an existential monadic block, an initial conjunct, a
  universal local-transition conjunct, and an existential final occurrence;
* \(\Pi_1\) has a universal monadic block and the displayed dual disjunctive
  pattern;
* \(\Sigma_{n+1}\) existentially prefixes a \(\Pi_n\) formula; and
* \(\Pi_{n+1}\) universally prefixes a \(\Sigma_n\) formula.

The source's infinitely-often abbreviation is exactly
\((\forall x)(\exists t)[x<t\land D(t)]\).  Its strict inequality still has the
intended meaning: for every bound there is a later occurrence, hence there are
infinitely many occurrences, and conversely every infinite subset of
\(\mathbb N\) is unbounded.  Substitution into the base recurrence gives the
\(\Sigma_1^\omega\) display at reader lines 452--460.  The symbol's two uses—as
a formula class and, when denotation is explicitly in view, as the class of
defined relations—are source-declared on printed p. 3, as are the analogous
uses of \(\Sigma^0\).

A regular formula \(R(\mathbf i,x,y)\) constrains its recurrence on
\(x\le t<y\), initializes at \(x\), and tests at \(y\).  Its value therefore
depends only on the finite word
\(\mathbf i(x)\cdots\mathbf i(y-1)\).  This proves the finite-interval claim at
reader lines 500--509 rather than confusing a formula with its finite-word
denotation.

### 2. Formula to automaton, including the initial-set edge case (M07)

Fix the recurrent formula at reader lines 452--460 and the finite data at lines
469--479.  For any input word \(w=a_0a_1\cdots\), an assignment to the
\(\ell\) predicates in \(\mathbf r\) determines
\(q_n=\mathbf r(n)\in Q=\{0,1\}^{\ell}\).  The three matrix clauses say,
respectively,

1. \(q_0\in Q_0\);
2. \(q_{n+1}\in\Delta(q_n,a_n)\) for every \(n\); and
3. \(q_n\in F\) for infinitely many \(n\).

Hence a satisfying predicate assignment gives exactly an accepting state
sequence for the permitted-initial-set presentation.  Conversely, from such a
state sequence define the \(j\)-th predicate by
\(r_j=\{n:q_n(j)=1\}\).  Substitution recovers all three conjuncts, so the
correspondence is pointwise in the input and not merely equisatisfiable.

The difference between \(Q_0\) and a single initial state is harmless but must
be handled explicitly.  If \(Q_0=\varnothing\), the formula denotes the empty
language; a single nonaccepting sink with its self-loop recognizes that same
language.  If \(Q_0\ne\varnothing\), add a fresh nonaccepting state \(s\), and
on the first letter \(a\) let its successors be
\[
 \Delta'(s,a)=
 \bigcup_{q\in Q_0}\Delta(q,a).
\]
After that first transition use \(\Delta\).  An old accepting state at position
zero contributes only one visit, so deleting that finite initial visit cannot
change an infinitely-often condition.  Every new run also records some
\(q\in Q_0\) witnessing its first transition, giving the converse.  This proves
the boundary stated at reader lines 491--498, including the empty-initial-set
case, without attributing the five finite-data objects to the article.

The edge case \(\ell=0\) is also sound: \(Q=\{()\}\) has one truth-value state.
If the initial or recurrent matrix is false, the corresponding set is empty;
otherwise the same three-clause argument applies.

### 3. Automaton to formula, including unused codes (M15)

Let a nondeterministic Büchi automaton over \(\{0,1\}^k\) have a nonempty finite
state set \(S\), one initial state, transition relation \(\delta\), and recurrent
set \(F_A\).  Choose \(\ell\ge1\) and an injection
\(\operatorname{code}:S\hookrightarrow\{0,1\}^{\ell}\).  For each state \(s\),
the assertion that the auxiliary bits equal \(\operatorname{code}(s)\) is a
propositional matrix.  Define:

* \(A\) to assert the code of the initial state;
* \(B[a,q,q']\) as the finite disjunction of the code triples corresponding
  exactly to \(s'\in\delta(s,a)\); and
* \(C\) as the finite disjunction of the codes in \(F_A\).

Because \(B\) enumerates only actual source and target codes, an unused binary
pattern cannot occur at any position of an infinite witness; \(A\) excludes it
at position zero and every later position is a target of the preceding
transition.  If \(F_A=\varnothing\), \(C\) is the false propositional matrix and
both sides denote the empty language.  Reading an accepting run bitwise gives
the existential predicate tuple, and reading any satisfying tuple through the
injective code gives an accepting run.  Thus the construction at reader lines
622--632 is exact in both directions and handles unused codes without assuming
that the number of states is a power of two.

Combining this direct direction with Theorem 1 in the other direction proves
the handbook-owned language equivalence.  Printed pp. 2--9 supply the recurrent
formula and its effective normal form, but do not print the modern tuple or
theorem name.  The ownership sentence at reader lines 622--632 and the source
boundary at lines 746--755 keep those facts separate.  The compact theorem at
`logic-in-computer-science.tex` lines 817--828 has the same mathematical
strength: formulas with free monadic variables give languages over
({0,1}^k), the converse is direct, and closed truth additionally uses the
effective normal form before Lemma 12.

### 4. Finite words, two-sided congruence, and Lemmas 2--6 (M09, M11)

The relation at reader lines 511--516 is a two-sided monoid congruence: replacing
\(u\) by \(v\) preserves both \(uw\) and \(wu\).  A finite-word language is
multiperiodic precisely when it is saturated for one such finite-index
relation.  This is a property of a finite-word language, not of an infinite
word or of a predicate set; reader lines 518--523 make the nonredundancy and
later use explicit.

Printed pp. 3--4 give the following exact dependency chain.  Lemma 2 identifies
a \(\Sigma^0\)-defined finite-word language with an endpoint-output behavior of
a deterministic finite-state recursion.  For a word of length \(x\), the
recursion consumes positions \(0,\ldots,x-1\) and tests \(U[\mathbf r(x)]\), so
reader lines 545--557 have the endpoint on the correct side of the last
transition.  The hard implication is credited to Myhill's subset construction
and Büchi 1960; the reverse regular formula is displayed.  Lemmas 3--5 give the
stated Boolean, bounded-variable, and endpoint reductions.  Lemma 6 is stated
as behavior iff multiperiodic and referred to Rabin--Scott.  Therefore the
three-way bridge at reader lines 561--573 is correct, while its proof-ownership
labels do not claim local proofs for the cited directions.

### 5. The Sequential Lemma (M10)

For the finite partition \(\mathcal E_0,\ldots,\mathcal E_n\), color the
two-element set \(\{y_1,y_2\}\), \(y_1<y_2\), by the unique cell containing
\(\mathbf i(y_1)\cdots\mathbf i(y_2-1)\).  Infinite Ramsey gives positions
\(x_1<x_2<\cdots\) whose every two-element subset has one color \(c\).
Consequently the segment from \(x_p\) through \(x_q-1\) lies in
\(\mathcal E_c\) for every \(p<q\).  The conclusion is not limited to adjacent
blocks.  This is exactly the printed proof on p. 3 and exactly the quantifier
at reader lines 525--543.

### 6. Boolean closure, finite congruence, and complement (M12)

Union is supplied by a finite choice of the two existential witnesses.
Intersection uses one additional Boolean control coordinate that waits for
one recurrent condition, then for the other, and designates completion of
infinitely many complete alternations.  Thus the combined recurrence is
satisfied exactly when both original recurrent conditions occur infinitely
often.  This verifies the role, rather than merely the name, of Lemmas 7--8 at
reader lines 575--578 and printed p. 5.

For Lemma 9, let the original auxiliary state set have \(m\) elements.  For
each finite input word \(u\), record two Boolean \(m\times m\) matrices:

* whether an \(H\)-path labeled by \(u\) exists from \(V\) to \(W\); and
* whether such a path exists with an \(L\)-state in the source's designated
  portion of the path.

Concatenation of words composes the first matrices.  It computes the second
from the two first/second pairs by relational composition and union (with the
fixed junction-state convention if the junction is not counted in either
piece).  Therefore equality of both matrices is preserved by concatenation on
either side and is a two-sided congruence.  There are (2m^2) Boolean entries,
so there are at most (2^{2m^2}) equivalence classes.  This proves both the
rank bound and its congruence status at reader lines 579--587.

Apply the Sequential Lemma to these classes.  Every input has a decomposition
with one finite initial class \(c\) and one homogeneous later-block class \(d\).
Suppose two inputs have the same pair \((c,d)\) and one has an accepting
\(H\)-path.  At infinitely many selected cuts, choose a repeated auxiliary
state.  Equality of the first path matrix transfers the initial path and every
return path; infinitely many recurrent visits ensure that the second matrix
for the repeated class records a recurrent visit.  Selecting corresponding
paths for the other input yields an accepting path there.  The argument is
symmetric, so acceptance is constant on each nonempty \((c,d)\)-class.  A finite
union of the classes on which acceptance is false therefore defines the
complement.  This is the homogeneous-block argument printed on pp. 5--6 and
summarized at reader lines 588--593; no determinization result is required.

The effectivity claim also survives a possible rank strictly below the stated
bound.  Starting from the empty word, enumerate one-letter extensions of known
class representatives and use the decidable matrix equality to merge them.
When every extension is represented, right-congruence closes the search over
all words; finite rank guarantees termination.  Thus the procedure need not
wait to discover all (2^{2m^2}) possible Boolean patterns.  Lemmas 2 and 6
then effectively define the resulting classes.

### 7. Lemma 10 and the nonempty repeated-block condition (M13)

The preceding construction yields a finite union of sets
\(\mathcal C\mathcal D\mathcal D\cdots\).  The initial block can be empty if its
chosen first cut is zero.  Each later block runs from \(x_p\) to \(x_{p+1}-1\),
and \(x_p<x_{p+1}\), so every repeated block has positive length.  Even if the
congruence class \(\mathcal D\) also contains the empty word, the displayed
infinite factorization uses nonempty members; otherwise infinitely many
factors would not necessarily consume an infinite input.  Reader lines
595--603 and compact-record line 562 state exactly this mathematically required
reading of printed p. 7.

### 8. Lemma 11, Theorem 1, and collapse (M14)

Lemma 11 places an arbitrary \(SC\) formula in some alternating
\(\Sigma_n\)-level; the paper refers this step to the 1960 method.  A
\(\Sigma_1\) formula with a once-only final condition can be converted to a
recurrent one by finite control that remembers once the final condition has
occurred and then remains designated.  Requiring that persistent state
infinitely often is equivalent to requiring the original occurrence once.
Complement closure from Lemma 9 changes polarity at each monadic alternation,
and union/intersection closure combines the resulting clauses.  Induction on
the level therefore yields a \(\Sigma_1^\omega\) formula for every \(SC\)
formula, which is Theorem 1 at reader lines 605--612 and printed p. 7.

Every \(\Sigma_2\) formula is an \(SC\) formula, hence Theorem 1 puts it in
\(\Sigma_1^\omega\).  Conversely, expanding the infinitely-often condition as
\(\forall x\exists t>x\) and applying the paper's finite recurrence/regular
formula reductions places the recurrent existential form at the second
alternating level.  Thus \(\Sigma_1^\omega\) and \(\Sigma_2\) define the same
relations.  Since the recurrent class is also closed under complement, both
polarities at and above level two collapse extensionally.  The reader correctly
states a definability collapse, not a modern state-complexity bound.

For free individual variables, testing the reached recurrence state at each
free position adds the endpoint conditions printed on p. 7; it does not change
the finite recurrence.  The source then draws the two finite-set consequences
at that stated strength.  Reader lines 617--620 neither omit the free-variable
extension nor promote the referred proof into a locally printed proof.

### 9. Lemma 12's exact finite stem--cycle argument (M16)

For a closed recurrent matrix, form the finite directed graph on
\(S=\{0,1\}^k\), with an edge \(V\to W\) exactly when \(H[V,W]\).  Let
\(K_S=\{V:K[V]\}\) and \(L_S=\{V:L[V]\}\).  The sentence is satisfiable exactly
when some \(U\in L_S\) is reachable from \(K_S\) and lies on a nonempty directed
cycle:

* If an infinite satisfying sequence exists, it has infinitely many positions
  in \(L_S\).  Since \(L_S\) is finite, one state \(U\in L_S\) occurs at two
  such positions (indeed infinitely often).  The prefix is the stem and the
  segment between two distinct occurrences is a nonempty return cycle.
* Conversely, concatenate a stem ending at \(U\) with infinitely many copies
  of a nonempty return cycle.  All adjacent pairs satisfy \(H\), the first state
  satisfies \(K\), and \(U\in L_S\) occurs once per cycle.

Write \(n=|S|=2^k\).  A shortest stem has no repeated internal state, so it has
at most \(n-1\) edges unless it is the zero-edge stem.  A shortest positive
return path has no repeated internal state and has at most \(n\) edges.  Hence
the reader's common bound of \(2^k\) edges is safe for every candidate.  The
cycle may not be shortened to the zero-edge path: that would lose the infinite
sequence of actual transitions.  A self-loop is the length-one edge case.

If \(k=0\), then \(n=1\) and the same test reduces to whether the sole state is
initial, recurrent, and has a self-loop.  If \(K_S\) or \(L_S\) is empty, there
is no candidate.  These cases confirm reader lines 634--652 and source-note
lines 357--383, including the nonempty-cycle and finite-enumeration clauses.

### 10. Remaining effectivity and Theorem 2 (M17)

The local propositions \(K,H,L\) are decidable on the finite truth-value state
set, and the preceding bounds make Lemma 12 a finite search.  For the earlier
complement step, the two path matrices decide word congruence, the class search
terminates as described above, and effective Lemmas 2 and 6 give formulas for
the classes.  For a proposed pair \((c,d)\), the question whether any input in
that class satisfies the old recurrent formula is the truth of a conjunction
of recurrent formulas; Lemma 8 returns it to one recurrent formula and Lemma
12 decides it.  Negating that finite yes/no answer determines which classes
enter the complement.  Thus Lemma 9, Theorem 1, and finally the truth test are
effective, exactly as printed on pp. 8--9 and stated at reader lines 654--659.

Nothing in this derivation bounds the iterated normal-form growth by an
elementary function, PSPACE, or an optimum.  Reader lines 660--663, shared
theorem lines 825--827, and the source-note proof ledger correctly stop at
effective decidability.  The source motivates supplied-system verification but
contains no worked circuit example.

### 11. Consequences, later theorems, and open questions (M18--M23)

The five post-Theorem-2 items at reader lines 665--687 match printed p. 9 and
remain reports rather than new proofs: the printed and locally undefined
\(\Sigma_2^0\) comparison; definability of equality, order, and every fixed
positive modulus; definability of finiteness and the resulting
\(SC_{\mathrm{fin}}\) decision claim; the
([\mathrm{Nn},+,\mathrm{Pw}]) consequence; and the Skolem--Behmann
comparison.  The reader does not identify \(\Sigma_2^0\) with \(\Sigma^0\), and
defines \(SC_{\mathrm{fin}}\) as a restriction of the monadic assignment
domain.

The candidate axiom schema is accurately reported as a proposal.  Printed p. 9
says a further analysis would yield a complete axiom system and displays the
homogeneous-sequence schema, but supplies no soundness-and-completeness proof.
Reader lines 689--695 preserve that modal and proof boundary.

For \(SC_{\mathrm{per}}\), the reader gives the eliminable definition
\[
 \exists N\exists p\ge1\;\forall n\ge N\;
 (n\in X\leftrightarrow n+p\in X).
\]
This stands for the same interpreted formalism with its monadic quantifiers
restricted to such sets.  In the finite quotient semigroup used by the block
argument, every element has an idempotent positive power: finiteness makes the
power sequence eventually periodic, and an exponent sufficiently far into
the periodic portion and divisible by its period satisfies
\(c^{2e}=c^e\).  Repeating a word representing that idempotent class gives an
ultimately periodic witness with the same homogeneous block behavior.  This
checks the mathematical content of the outline around printed pp. 9--10.  The
article does not print the full detailed derivation, and reader lines 703--715
correctly call it an outline.  Theorem 3 is stated only for sentences, as it
must be when comparing truth under two monadic quantifier domains.

The binary-expansion route on printed p. 10 uses arbitrary predicate sequences
for real expansions and ultimately periodic sequences for rational expansions;
Theorem 3 is the transfer that supports Theorem 4's arithmetic equivalence and
decidability claim.  The source states this as a corollary rather than printing
a full treatment of nonunique binary expansions, and the manuscript likewise
does not pretend to supply that omitted proof.  The symbol lists and order in
reader lines 717--728 match the theorem.  The visual source has the real
discrepancy the reader reports: printed p. 1 calls \(\mathrm{Nn}\) the natural
numbers, while printed p. 10's ordered glossary calls it the integers.  No
silent choice between those readings is made.

Printed p. 10 attributes undecidability after adjoining (2x) to Robinson and
attributes the monadic-function definability report to Gödel; neither proof is
printed, and reader lines 730--733 preserve those limits.  The three closing
problems are also exact: \(SC^2\) replaces successor by \(2x+1,2x+2\);
\(SC(\alpha)\) uses ordinal individual domain \(\alpha\) and its well-order as a
primitive, with the question at \(\omega^2\); and the last asks whether some
finite-state recursion can satisfy an arbitrary supplied condition.  That last
question is synthesis.  Theorem 2 answers only whether a supplied behavior
satisfies a condition, so reader lines 735--744 do not turn verification into
a solved synthesis theorem.

## Cross-artifact reconciliation (M24)

The reader at `n-c-013.tex` lines 375--759, the shared theorem at
`logic-in-computer-science.tex` lines 817--828, the bibliography at
`handbook.bib` lines 2276--2288, the complete 541-line source note, and the
compact record at `p09-source-presentations-lot2-3.md` lines 556--568 agree on:

* the \(SC\) domains and vocabulary;
* the truth-value-word encoding;
* the \(\Sigma_1^\omega\) recurrence and its handbook-owned modern comparison;
* the finite-word congruence and proof dependencies;
* complement rank (2^{2m^2}), the homogeneous-block construction, and the
  absence of a determinization claim;
* Theorems 1--2, the nonempty stem--cycle search, effectivity, and the absence
  of a modern complexity bound;
* the five source-reported consequences;
* Theorems 3--4, the \(\mathrm{Nn}\) discrepancy, attribution limits, and the
  three open problems; and
* the 1962 pp. 1--11 identity, later-version separation, and research-copy
  rights limit.

The consolidated open-acquisition list at compact-record lines 888--901 has no
entry for N-c-013.a, while the sufficient-body ledger at line 903 includes
Büchi 1962 with the later-printing and identifier qualification.  “Body
sufficient” is explicitly limited to acquisition and does not claim review or
book completion.  This is consistent with reader lines 756--759 and
source-note lines 532--541.

## Terminology, scope, and evidence boundary (M25)

Every technical name introduced in the frozen scope satisfies the supplied
terminology rule.  In particular, `multiperiodic` is the source's defined class
of finite-word languages and is distinguished from ultimately periodic sets;
\(SC_{\mathrm{fin}}\) and \(SC_{\mathrm{per}}\) are defined restrictions of an
interpreted formalism and are immediately used; and
\(\Gamma,Q,Q_0,\Delta,F\) are explicitly eliminable finite data, with their
standing, nonredundancy, and use given at reader lines 469--498.  The text does
not name hypothetical proof objects in place of owed artifacts.

The rights qualification, topic-only N-c-013.a scope, source-proof versus
referred-proof boundary, and no-test/no-build boundary are all explicit.  This
review establishes only manuscript-level source fidelity and mathematical
proof correctness on the frozen snapshot.  It does not establish a build,
rendered handbook quality, another topic, Part IX completion, human review, or
user acceptance.

## Mandatory-coverage reconciliation

| Point | Status | Basis |
|---|---|---|
| M01 | checked-clean | all six SHA-256 identities recomputed and matched |
| M02 | checked-clean | every required original-detail image read; complete file/printed page map confirmed |
| M03 | checked-clean | identity, editors, venue, publisher, place, year, pages, later-printing status, identifier separation, route, and rights boundary reconciled |
| M04 | checked-clean | printed p. 1; reader 391--400 |
| M05 | checked-clean | printed p. 3; reader 402--419; input assignment distinguished from later witness sequence |
| M06 | checked-clean | printed p. 2; reader 421--467; all polarities and the strict infinitely-often expansion verified |
| M07 | checked-clean | both directions proved above; empty \(Q_0\), single-start conversion, and \(\ell=0\) checked |
| M08 | checked-clean | printed pp. 2--3; finite interval and formula/denotation overload verified |
| M09 | checked-clean | printed pp. 2--3; two-sided congruence, finite rank, standing, and nonredundancy verified |
| M10 | checked-clean | printed p. 3 Ramsey coloring rederived with the required \(p<q\) quantifier |
| M11 | checked-clean | printed pp. 3--4; endpoint convention, reductions, and referred proof ownership verified |
| M12 | checked-clean | printed pp. 5--6; conjunction, congruence, rank bound, transfer argument, effectivity, and non-determinization boundary rederived |
| M13 | checked-clean | printed p. 7; finite union form and nonempty repeated blocks verified |
| M14 | checked-clean | printed p. 7; normal form, collapse, free-individual extension, finite-set consequence, and proof strength verified |
| M15 | checked-clean | both handbook-owned equivalence directions proved; modern naming/source boundary preserved |
| M16 | checked-clean | printed p. 8; stem, recurrent state, positive cycle, (2^k) bound, converse, finite search, and all empty/one-state cases checked |
| M17 | checked-clean | printed pp. 8--9; remaining effective constructions and exact decidability strength verified |
| M18 | checked-clean | printed p. 9; all five consequences and the \(\Sigma_2^0\) standing limit verified |
| M19 | checked-clean | printed p. 9; candidate schema not promoted to a proved complete axiomatization |
| M20 | checked-clean | printed pp. 9--10; periodic-set definition, formalism standing, theorem, and finite-semigroup outline verified |
| M21 | checked-clean | printed pp. 1 and 10; theorem, binary-expansion route, symbol glosses, and \(\mathrm{Nn}\) discrepancy verified |
| M22 | checked-clean | printed p. 10; Robinson/Gödel reports and proof limits preserved |
| M23 | checked-clean | printed p. 10; all definitions/questions and verification/synthesis distinction verified |
| M24 | checked-clean | reader, shared theorem, bibliography, complete note, compact record, open list, and sufficient-body ledger reconciled |
| M25 | checked-clean | terminology rule, rights, topic scope, and no-test/no-build boundary checked |

VERDICT: ACCEPT
