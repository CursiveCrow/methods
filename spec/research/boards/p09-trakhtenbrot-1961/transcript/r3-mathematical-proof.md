# Round 3 mathematical and proof-correctness review

## Disposition

The frozen Round 3 snapshot has one must-fix mathematical defect.  The
reader defines portions for every finite prefix, and therefore includes the
empty portion, but then repeats the source's claim that the graph of a
zero-anticipation operator of weight \(k\) has homogeneity degree at most
\(k\).  A one-state constant-zero operator is already a counterexample: its
graph and the empty portion are two distinct portions.  The correct bound
under the reader's definition is \(k+1\).

No other blocker or must-fix was found in this seat's mandate.

## Isolation, evidence, and competence

I did not read the board ledger, the chair transcript, any Round 1 or Round 2
report, or any other Round 3 report, and I did not contact another reviewer.
I read the charter, the seven frozen objects within their stated review
scopes, and the two noncontrolling OCR files only as navigation aids.

I visually inspected the four announcement images and all twenty-nine
expanded-article images with original detail preserved.  The physical maps
are continuous and exact:

- announcement physical pages 1--4 are printed pp. 326--329;
- expansion physical pages 1--29 are printed pp. 103--131.

My Russian competence is working mathematical-reading competence: I can read
the definitions, theorem statements, proof prose, qualifications, and
standard mathematical vocabulary in these bodies directly, but I am not a
native speaker, a certified translator, or a Russian-language specialist.
For this mathematical seat I used the printed scans as controlling evidence,
used OCR only to navigate the already inspected pages, and independently
rederived the mathematics.  This report does not supply specialist
translation certification.

I ran no test, checker, repository script, TeX command, build, interim
handbook render, or handbook-PDF inspection.

## Frozen-object identity

All seven recomputed SHA-256 labels exactly match the Round 3 charter.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf | 44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9 | match |
| tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf | EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D | match |
| handbook/parts/p09/presentations/n-c-014.tex | 75E224288547CC8FA0A14C15B866C170685448257F0A04DE9F6770D7C027D999 | match |
| handbook/parts/p09/logic-in-computer-science.tex | A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD | match |
| handbook/bib/handbook.bib | 75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C | match |
| spec/research/p09-trakhtenbrot-1961-source-note.md | 80BEE63A6F8C275716A6BC55652AA7F1E024B8FC4E033B57D28F0E0BAF5C719C | match |
| spec/research/p09-source-presentations-lot2-3.md | EE9ED7FBF9A1F15C3AFE6A3D02752830D0D287B28277819AEAA51B771B2D1A21 | match |

## Finding

### R3-MP-01 — must-fix — empty portions make the graph-degree bound off by one

- Reader locations:
  handbook/parts/p09/presentations/n-c-014.tex:583--598, especially
  lines 585--593 and 597--598.
- Source-note locations:
  spec/research/p09-trakhtenbrot-1961-source-note.md:184--210,
  especially lines 186--200 and 202--205.
- Controlling printed source:
  expanded pp. 114--115.  Page 114 introduces portions; p. 115 prints the
  graph example as closed and \(k\)-homogeneous.  The announcement's p. 327
  description explicitly allows the corresponding tail set to be empty.
- Violated coverage/invariant:
  M09 and the empty-portion edge case in the mathematical role card; the
  source-owned numerical claim is repeated without a handbook-owned
  correction.

The reader gives the total definition
\[
  M_u=\{Z:uZ\in M\}
\]
for every finite word \(u\), and defines degree by the number of distinct
members of \(\{M_u:u\text{ finite}\}\).  Hence \(\varnothing\) is a portion
whenever a finite prefix has no extension in \(M\).

Take the one-state zero-anticipation operator
\[
  T:\{0,1\}^{\mathbb N_+}\longrightarrow
    \{0,1\}^{\mathbb N_+},
  \qquad T(X)=0^\omega .
\]
Its weight is \(1\).  Let \(G\) be its graph, viewed over the paired
alphabet.  Then
\[
  G_{\epsilon}=G,\qquad
  G_{\langle 0,0\rangle}=G,\qquad
  G_{\langle 0,1\rangle}=\varnothing .
\]
Thus \(G\) has at least two distinct portions, \(G\) and \(\varnothing\), and
is not homogeneous of degree at most \(1\).  More generally, a
weight-\(k\) causal operator has at most \(k\) distinct nonempty graph
portions, one per reachable residual memory state, plus the empty portion.
The valid bound under the frozen reader's definition is therefore
\[
  \deg(G)\leq k+1.
\]

This is not merely a choice of convention internal to the report.  The
reader and source note explicitly use the all-prefix residual definition,
and the later stable-deletion argument expressly reasons about empty
portions.  Under that convention, the \(k\) bound is false.

The smallest safe correction is:

1. retain the current all-prefix definition of portion;
2. change the graph example in n-c-014.tex:597--598 and
   p09-trakhtenbrot-1961-source-note.md:204--205 to degree at most \(k+1\);
3. state that the extra possible residual is the empty portion; and
4. identify this as a handbook-owned correction to expanded p. 115.

Alternatively, the project could redefine degree using nonempty portions
only, but that is the larger change because every later use of empty
portions, bases, transition maps, deletion, and degree bounds would then
need a fresh consistency audit.

The principal finite-realization and general-solution weight bounds do not
need to be weakened.  Their constructions use nonempty surviving portions
as memory states, so weight remains at most the all-portions homogeneity
degree.

## Independent mathematical derivation

### 1. System \(\mathcal I\), semantic dependence, and normal form

The scans support the frozen account of the interpreted language.  On
expanded pp. 104--105, individual variables range over
\(\mathbb N_+=\{1,2,\ldots\}\), monadic variables range over arbitrary
Boolean predicates on that domain, and immediate successor is primitive.
Atomic formulas apply a monadic predicate to an individual variable or an
iterate of successor.  Propositional operations and both individual and
predicate quantifiers form formulas.  Equality, order, bounded individual
quantifiers, constants, and \(t+k\) are explicitly eliminable extensions.
The manuscript's standing for Cyrillic И as an interpreted formal language,
not an automaton or a set, is correct.

The definition of fictitious occurrence on expanded pp. 105--106 is
semantic: two interpretations differing only outside the stated interval
must give the same truth value.  It is not syntactic nonoccurrence.
Consequently a lower \(t\)-formula has bounded prefix dependence through
\(t+s\), while an upper \(t\)-formula has tail dependence from \(t\).

The normal-form proof on expanded pp. 108--109 checks independently as
follows.

1. Move predicate quantifiers ahead of individual quantifiers and use the
   Behmann inward-pushing step on the individual quantifiers.
2. Split each remaining universal individual quantifier at \(t\) into a
   lower and upper conjunction, and each existential individual quantifier
   into a lower and upper disjunction.
3. It remains to commute one predicate quantifier through a conjunction
   \(\Gamma\widetilde\Gamma\) of a lower and an upper formula.
4. If the lower formula has shift \(s\), enumerate the finitely many truth
   patterns \(\sigma_0,\ldots,\sigma_s\) of the quantified predicate on the
   overlap \(t,\ldots,t+s\).
5. For a fixed pattern, one implication of the factorization is immediate.
   For the converse, glue a lower witness and an upper witness: use the
   former through \(t+s\) and the latter from \(t\) onward.  They agree on
   the enumerated overlap, and semantic fictitiousness preserves both
   conjuncts.

This proves the effective Boolean combination of lower and upper
\(t\)-formulae reported at n-c-014.tex:512--525.  No hidden disjointness
assumption is being made: the finite overlap is exactly why the truth
patterns are enumerated.

### 2. Anticipation, finite memory, weight, and effectiveness boundaries

For a total stream map, anticipation \(p\) means that output position \(t\)
is determined by the input prefix through \(t+p\).  At \(p=0\), two
extensions of the same length-\(t\) word produce the same output prefix, so
the induced lengthwise maps are well defined and prefix compatible.
Conversely, a prefix-compatible family determines a causal stream map.

Finite memory is strictly different.  Expanded p. 110 allows the external
and internal transition functions to consume the entire suffix
\(a(t),a(t+1),\ldots\).  A finite state set therefore restricts retained
past information but does not bound, or make effective, future dependence.
The least state-set cardinality is the weight.  Adding one uniform
lookahead bound produces the finite-window equations of a finite operator;
setting that bound to zero gives the automaton-realizable class called
Л in the announcement and \(A\) in the expansion.

The one-state example on expanded p. 111 is valid:
\[
 b(t)=1\quad\Longleftrightarrow\quad
 \exists \tau\geq t\;a(\tau)=1.
\]
The state never changes, so the weight is one, while deciding output zero
requires knowing the whole remaining suffix.  Thus finite memory does not
imply continuity, bounded anticipation, or recursiveness.

The primitive-recursive negative boundary on pp. 111--112 also checks.
Recognizing whether a primitive-recursive constant output is ultimately
periodic would decide a known undecidable property.  For synthesis, from an
arbitrary primitive-recursive \(f\) the paper forms an eventually constant
predicate \(g\) which is always ultimately periodic; canonical equations
for \(g\) would decide whether \(f\) is identically zero.  The reader
correctly separates this promised-finite-state synthesis failure from the
positive \(\mathcal I\) bounds.

### 3. Portions, examples, and the exact consequence of empty portions

Coordinatewise residualization is mathematically sound:
\[
 M_u=\{Z:uZ\in M\},\qquad (M_u)_a=M_{ua}.
\]
A finite residual family therefore carries a finite internal transition
map.  Empty residuals satisfy
\((\varnothing)_a=\varnothing\).

The singleton criterion is correct even with the empty residual included.
The nonempty residuals of \(\{X\}\) are exactly the singleton tails of
\(X\).  There are finitely many such tails exactly when two tails repeat,
which is equivalent to ultimate periodicity.  Adding the one empty
residual changes only the numerical degree, not the equivalence.

The uncountability counterexample also survives the convention.  Fix a
non-ultimately-periodic binary sequence \(\xi\), and let \(M_\xi\) consist
of all streams eventually equal to a tail of \(\xi\).  Every finite prefix
can be prepended without changing eventual-tail equivalence, so every
portion equals \(M_\xi\).  Tail-equivalence has continuum many classes,
giving uncountably many one-homogeneous sets but only countably many
\(\mathcal I\)-formulae.

For a \(k\)-state zero-anticipation operator, every nonempty paired-prefix
portion of its graph is the graph of the residual operator determined by a
reachable memory state.  Hence there are at most \(k\) nonempty portions.
The graph is closed because matching the first \(n\) input letters fixes the
first \(n\) output letters.  The only error is the omitted empty residual,
as recorded in R3-MP-01.

### 4. Definability, the recurrent converse, and conditionality

The proof that every \(\mathcal I\)-definable set has finitely many portions
checks from the normal form.  After fixing a prefix of length \(v\), each
lower formula reduces effectively to one of finitely many Boolean functions
of a bounded window, while each upper formula is shifted to the residual
origin.  Canonical Boolean forms therefore leave only finitely many residual
formulas.  Appending a bit computes the next residual syntactically, so the
internal transition is unconditional and effective.

For the converse, take the finite family of nonempty portions and encode
the current portion by one-hot state predicates.  A choice predicate selects
the next bit when both are possible; when only one is possible, the output
map is constant.  The local transition sends the current portion to the
selected successor portion.  From the literal initial state:

- every parameter stream produces a point whose every finite prefix extends
  to a point of \(M\), hence a point of \(\overline M\);
- every point of \(\overline M\) determines choices that reproduce it.

If \(M\) is closed, the image is exactly \(M\).  This yields the recurrent
existential-predicate formula with free input predicate, bound state and
choice predicates, a literal initial basis state, and a quantifier-free
current/next matrix.  Conversely, any formula of that local existential
shape defines a projection of a closed subset of a finite Cantor product;
compactness makes the projection closed, and the finite boundary-state
sets give homogeneity.

Complement and finite union provide the Boolean operations, and predicate
existential quantification is projection.  Hence the least closure
characterization reported in the reader follows.  Homogeneity without
closedness is not enough, as the uncountability example shows.

The effectiveness qualification is exact.  The internal transition follows
from the finite residual formulas.  Choosing the external output requires
knowing which residual formulas are nonempty.  That is the source's
conditional \(\mathcal I\)-algorithm boundary.  Putnam applies to the stated
existential-predicate/individual-quantifier/quantifier-free fragment, which
includes the displayed recurrent form; it is not a blanket removal of the
condition for arbitrary formulas.

### 5. Continuous realization and the weaker discontinuous theorem

Let an \(\mathcal I\)-formula define the graph \(G\) of a total continuous
operator.  The graph is closed and has a finite portion basis.  Each nonempty
portion is a functional closed relation on a compact domain and hence the
graph of a continuous residual function.  Uniform continuity gives, for
each such portion, a finite input-prefix length determining its first output
letter.  Taking the maximum over the finite basis gives one anticipation
bound.  The current nonempty portion is a finite memory state; after the
output letter is computed, the paired input/output letter determines the
next portion.  This proves finite realization and the weight bound by the
number of nonempty basis portions, hence by the reader's all-portions
homogeneity degree.

If continuity is omitted, the same portion state still works, but the
external output and next-state functions may depend on the whole future
suffix.  They can be extended arbitrarily away from the suffixes that reach
the state.  This gives finite memory only.  The one-state future-existence
operator shows why no anticipation bound can be inferred.  The reader
therefore correctly keeps expanded Section 4, Theorem 2 strictly weaker
than a finite-operator conclusion.

The graph/solution distinction is also correct.  A formula defines an
operator only when its relation is exactly the graph.  An operator solves a
formula when its graph is merely contained in the relation.  For a closed
homogeneous relation, the same finite-portion selection proves announcement
Theorem \(4'\): a continuous solution can be replaced by a finite one, and
a zero-anticipation solution by an automaton-realizable one, with the stated
closed-case weight bound.  The announcement's separate open-relation remark
does not carry that bound.

### 6. General solutions, deletion, parameters, and fixed anticipation

The two clauses of a general \(A\)-solution are both necessary and are
correctly retained:

1. completeness: every \(A\)-solution is obtained by an \(A\)-operator
   parameter substitution;
2. soundness: every \(A\)-operator parameter substitution is a solution.

Replacing \(A\)-operators throughout by arbitrary zero-anticipation
operators gives the second generality notion; mere existence of one
solution proves neither clause.

For the main alternative, begin with the finite portion basis of the closed
relation.  Delete empty portions, then repeatedly delete any portion which,
for some current input letter, has no surviving output successor.  If the
initial portion is deleted, a causal solution is impossible: the nonempty
residual graphs of any such solution would form a stable family and could
not be deleted at any stage.  If the initial portion survives, a parameter
bit chooses between the surviving output successors and the internal
portion transition supplies finite memory.

Soundness for every parameter follows because every constructed finite
paired prefix reaches a nonempty surviving portion; hence every such prefix
extends to the relation.  Closedness then places the infinite pair in the
relation.  For completeness, given a causal solution \(T_0\), choose at each
step the parameter value that selects \(T_0(X)(t)\).  The relation-portion
state together with a presentation of \(T_0\) makes this parameter choice a
causal operator; if \(T_0\) is an \(A\)-operator, the parameter operator is
an \(A\)-operator.  This reconstructs all and only the named solutions.  The
outer memory uses at most the surviving nonempty portion count, so the
stated weight bound remains valid despite R3-MP-01.

For fixed \(p\), define the delay transform
\[
 (D_pY)(1)=\cdots=(D_pY)(p)=0,\qquad
 (D_pY)(t+p)=Y(t).
\]
Then \(Y\) has anticipation at most \(p\) exactly when \(D_pY\) has zero
anticipation.  The transformed relation is closed, and applying the
zero-anticipation theorem gives the fixed-\(p\) result.

The parameter edge case also checks without accumulating lookahead.  Delay
the parameter in the same way: if \(\widetilde U\) is causal, set
\(U(t)=\widetilde U(t+p)\); conversely, \(D_pU\) is causal whenever \(U\)
has anticipation at most \(p\).  After translating the outer solution back,
its time-\(t\) output uses \(X\) through \(t+p\) but \(U\) only through
\(t\).  Substituting a \(p\)-anticipating \(U\) therefore still uses \(X\)
only through \(t+p\), not through \(t+2p\).  This supplies the omitted
composition check and confirms that Theorem \(3'\) is a separate theorem
for each fixed \(p\), not one parametrization over unbounded lookahead.

The deletion step still requires nonemptiness decisions, so the arbitrary
closed-formula construction remains conditional.  Putnam removes the
condition only for the stated recurrent fragment.

### 7. Explicit synthesis and the worked example

An explicit definition
\[
  Y(t)\leftrightarrow\varphi(X_1,\ldots,X_m;t)
\]
defines a total operator whose graph is \(\mathcal I\)-definable, so the
discontinuous theorem gives finite memory.  It has anticipation at most
\(p\) exactly when the defining truth value is semantically independent of
input values after \(t+p\); the \(p=0\) instance is exactly the \(A\)-operator
criterion.

For a zero-shift upper-controlled formula, fixing the first input column
determines the first output and produces a shifted residual formula.  The
normal-form bound leaves only finitely many residual formulas, so iteration
terminates and the residuals are precisely the finite states.  Expanded
pp. 126--127 visibly carry the reported two residual formulas and both
output and transition tables.  The reader does not inflate that example
into a separate theorem.

### 8. Typed finite-word theorem and all edge cases

For \(t\geq1\), a causal stream operator induces
\[
  T_t:A^t\to B^t.
\]
Any two infinite extensions of \(u\in A^t\) agree through \(t\), so their
output prefixes agree through \(t\); \(T_t\) is well defined.  For
\(1\leq s\leq t\), the same argument proves
\[
  T_s(u|_{1..s})=T_t(u)|_{1..s}.
\]
The stream range itself is not confused with a finite-word language.

The first direction of expanded Section 5, Theorem 2 is sound.  If a
causal finite-state operator enumerates \(L\), membership of
\(v\in B^t\) is
\[
  \exists u\in A^t\;\forall \tau\leq t\,
  \bigl(T_\tau(u|_{1..\tau})(\tau)=v(\tau)\bigr).
\]
The source expresses this with a bounded predicate quantifier formula.
It is prefix controlled and therefore yields a terminal recognizer.

For the converse, under the source's binary-word scope, suppose \(L\) is
nonempty, prefix closed, properly extendible, and terminally decidable.
Given an input word \(x\):

- if \(x\in L\), output \(x\);
- otherwise let \(x_\tau\) be its longest prefix in \(L\), taking
  \(\tau=0\) when there is none, and output the lexicographically first
  length-\(|x|\) member of \(L\) extending \(x_\tau\).

Nonemptiness supplies a positive-length seed.  Prefix closure supplies all
shorter lengths, and repeated proper extension, followed by prefix closure,
supplies every longer length.  Thus the \(\tau=0\) branch is defined at
every positive length.  The chosen words are prefix compatible: a smaller
choice at an earlier length would extend to a smaller choice at the later
length.  Surjectivity is immediate because every \(v\in L\) maps to itself.
The source's bounded formula makes the construction an \(A\)-operator.

The empty language is exactly the missing edge case.  It is decided by the
constant-zero one-state recognizer and satisfies the two printed universal
conditions vacuously, but the range of a total length-preserving operator
on the nonempty binary input alphabet is nonempty at every positive length.
Adding \(L\neq\varnothing\) is therefore necessary and, by the construction
above, sufficient.  The reader correctly owns this correction rather than
attributing it to the source.

The paragraph is explicitly scoped to the source's binary words.  Its
arbitrary-alphabet analogue is sound when the enumerator's input alphabet
is chosen with the required branching, for example the same nonempty
alphabet as the output.  Nothing in the frozen text needs the false stronger
claim that the construction works for every previously fixed pair of
alphabets with too small an input alphabet.

Positive-length source words remain separate from the modern theorem's
possible empty word; no empty-word conclusion is silently imported into
Trakhtenbrot's theorem.

### 9. The weak system \(\mathcal I'\) and special beginnings

Expanded p. 130 defines \(\mathcal I'\) by restricting predicate variables
to predicates eventually equal to zero.  For such \(X\), a word
\(X(1)\cdots X(t)\) is special exactly when the tail after \(t\) is already
all zero; it is not an arbitrary prefix.

For an \(\mathcal I\)-formula \(\varphi(\Gamma)\), the source's terminal
recognizer asks whether there exists an eventually-zero \(\Gamma\) which
satisfies \(\varphi\), agrees with the presented word through \(t\), and is
zero afterward.  The input predicate is fictitious beyond \(t\), hence the
explicit definition is causal and finite-state.  Existence is therefore
valid for an arbitrary \(\mathcal I\)-formula.  When \(\varphi\) is an
\(\mathcal I'\)-formula, the \(\mathcal I'\) decision procedure makes the
construction effective.  The scan explicitly attributes that effective
case to Büchi.  The reader preserves the existence/effectivity distinction.

### 10. Modern finite-word MSO theorem

The shared theorem at
handbook/parts/p09/logic-in-computer-science.tex:811--825 is mathematically
correct and properly labeled modern.  Over finite word positions, successor
defines reachability in MSO by quantifying over successor-closed sets, so
order is definable; first and last positions are definable by absence of a
predecessor or successor.  The empty word can be handled by a separate
sentence case, so it creates no equivalence failure.

For MSO-to-automata, atomic relations have finite automata, Boolean
connectives use effective Boolean closure, and existential monadic
quantification projects a valuation track.  For automata-to-MSO, disjoint
state-set variables encode a run, with initial, transition, and final
conditions.  This proves regularity exactly.  The theorem paragraph and
n-c-014.tex:782--800 explicitly separate this modern proof from
Trakhtenbrot's positive-length operator theorem and from the distinct Büchi
and Elgot encodings.  The Thomas locator is therefore used as a modern proof
source, not laundered into either Russian article.

## Terminology and scope audit

The technical names used in the Trakhtenbrot reconstruction are defined
before substantive use and have clear standing:

- \(\mathcal I\) and \(\mathcal I'\) are interpreted formal languages;
- fictitious occurrence and lower/upper \(t\)-formula are semantic formula
  properties;
- anticipation, finite memory, finite operator, \(A\)-operator, and weight
  are distinct operator properties or invariants;
- portion, degree, basis, and internal transition are data or properties of
  stream sets;
- solution and general solution are relation/operator notions with both
  parameter quantifiers stated;
- explicit definition is a formula form;
- automaton-enumerable, automaton-decidable, terminal result, and special
  beginning are finite-word language notions with their types stated.

The Л/\(A\) normalization is declared, and the reader explains that the
hyphenated \(A\) labels the automaton-realizable class rather than the input
alphabet variable.  I found no definition-after-use, redundant coined name,
standing ambiguity, or unused distinction requiring a separate terminology
finding.

The topic boundary is preserved.  The reader does not call the modern
regular/MSO sentence a verbatim theorem of the announcement, does not merge
finite memory with finite operators, does not turn the fixed-\(p\) theorem
into an unbounded one, and does not promote source-time conditional
algorithms or historical priority remarks.  The frozen status records say
only that the two bodies are body-sufficient and the reconstruction is
pending independent review.  No build, rendered-handbook, human-acceptance,
or broader Part IX completion claim is made.

## Mandatory coverage map

| Point | Status | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven Round 3 hashes recomputed and matched. |
| M02 | checked-clean | All 4+29 pages inspected at original detail; maps 1--4 to 326--329 and 1--29 to 103--131 confirmed. |
| M05 | checked-clean | Primitive syntax, \(\mathbb N_+\), arbitrary predicates, successor, eliminable extensions, and \(\mathcal I'\) checked. |
| M06 | checked-clean | Semantic fictitiousness, lower/upper dependence, Theorem 1, overlap gluing, and all reported proof moves rederived. |
| M07 | checked-clean | Stream types, anticipation, prefix equivalence, whole-suffix memory equations, weight, finite windows, and \(A\)-standing checked. |
| M08 | checked-clean | Both primitive-recursive negative reductions and the one-state future-suffix example checked. |
| M09 | finding-linked | R3-MP-01: graph-degree bound omits the empty portion.  Portion typing, tuple residuals, singleton, basis, and uncountability claims otherwise check. |
| M10 | checked-clean | Finite residual-formula proof and effective internal transition independently derived. |
| M11 | checked-clean | Closed homogeneous converse, recurrent form, compact projection, full closure characterization, and topology checked. |
| M12 | checked-clean | Internal transition unconditional; output/deletion conditional on nonemptiness; Putnam fragment exactly bounded. |
| M13 | checked-clean | Compact uniformity, common anticipation bound, finite memory, and weight bound independently proved. |
| M14 | checked-clean | Discontinuous theorem yields finite memory only; counterexample blocks finite-operator collapse. |
| M15 | checked-clean | Exact graph/solution distinction and both closed Theorem \(4'\) branches checked; open remark kept unbounded. |
| M16 | checked-clean | Completeness and soundness parameter quantifiers for both generality classes checked. |
| M17 | checked-clean | Stable deletion, no-solution branch, surviving branch, parameter completeness/soundness, closedness, weight, and conditionality rederived. |
| M18 | checked-clean | Fixed-\(p\) delay, parameter delay, no \(2p\) composition leak, and fixed-versus-unbounded scope checked. |
| M19 | checked-clean | Explicit definitions, anticipation criterion, shifted residual termination, canonical equations, and pp. 126--127 tables checked. |
| M20 | checked-clean | Both language definitions, both theorem directions, empty-language counterexample, nonempty repair, prefix closure, and extendibility checked. |
| M21 | checked-clean | Eventually-zero semantics, exact special beginning, existence/effectivity split, and Büchi attribution checked. |
| M22 | checked-clean | Announcement Theorems 1--5 and \(4'\) kept distinct from expanded section numbering and proof detail. |
| M23 | checked-clean | Modern theorem and Thomas paragraph checked independently; no folklore substituted for the source packages. |
| M26 | checked-clean | Complete AGENTS terminology rule applied; no separate terminology finding. |
| M27 | finding-linked | R3-MP-01 is a source-owned numerical defect repeated without correction; all other listed collapse/laundering risks checked-clean. |
| M28 | checked-clean | Topic-only and no-test/no-build boundaries obeyed and accurately stated. |

For completeness beyond this seat's mandatory set, I also reconciled the
mathematical claims against the source note, compact N-c-014.c record, shared
theorem, bibliography entries, and consolidated acquisition-status
paragraph.  The two bibliography identities and distinct title renderings
are internally consistent with the scans and records.  I did not independently
re-audit external access-route or licence law, which belongs to the
source-fidelity seat.

VERDICT: REJECT — R3-MP-01
