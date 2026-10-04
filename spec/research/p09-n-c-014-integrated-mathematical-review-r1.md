REJECT

# Integrated mathematical/proof review R1: N-c-014

## Verdict

The actual reader LaTeX is not yet mathematically publication-admissible.  The
verdict-determining defect is local but foundational for Rabin's finite-tree
dependencies: `n-c-014.tex` introduces a new finite-tree automaton and then
quantifies over its runs without defining the run's domain, codomain, or local
transition condition.  The previously defined infinite-tree run cannot be
reused, because it is (S)-valued while the finite run must assign the external
frontier value (f\notin S).  The same passage also literally admits
(E=\varnothing), although acceptance subsequently evaluates the run at the
root.  This leaves the finite-tree lift, the complementation base, and the
emptiness base without a fully defined common object.

The remaining principal mathematics survives reconstruction at its stated
source-bounded strength.  In particular, I found no counterexample to the
handbook-owned Büchi analysis formula, Elgot unary-window completion,
Trakhtenbrot graph and empty-language repairs (under the source's nonempty
alphabet setting), Rabin zero-pair and empty-witness repairs, or Thomas
deadlock completion.  The finite-word and finite-tree host theorems are also
mathematically correct once their operative alphabet hypotheses are made
explicit.

The register remains open independently of this rejection: the 1959 Büchi
report supports only precursor strength until the 1960 journal body is
reconciled, and Thomas's May 1996 report supports only precursor strength until
the registered 1997 chapter is acquired and reconciled.  Those open source
obligations do not themselves cause the rejection.

## Evidence protocol and exact scope

I read directly and completely:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1596 through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--945,
  including the `n-c-014` input at line 936;
- the permitted Büchi, Elgot, Trakhtenbrot, Rabin, and Thomas source notes;
- only the `N-c-014` section and consolidated open-source bullets of
  `spec/research/p09-source-presentations-lot2-3.md`; and
- the relevant entries in `handbook/bib/handbook.bib`.

One concrete ambiguity could not be resolved from those records: whether the
finite predecessor-closed (E) in the Rabin passage is explicitly rooted and
how the source types its finite run.  I therefore consulted Rabin's original
1969 article at printed p. 30 only.  That historical source page says that a
finite binary tree is a finite predecessor-closed subset of (T), then defines
frontieredness, and later requires a finite run to take the value (s_0) at
(\Lambda) and (f) on the frontier.  This is historical-source evidence,
not a manuscript render.  It confirms both the intended run and the implicit
nonempty/root convention that the handbook must make eliminably explicit.

I did **not** inspect any manuscript PDF, rendered manuscript page, page image,
PNG, or other manuscript derivative.  I did not run TeX, a build, a test, a
checker, a repository script, a hash, or any automated validation.  I did not
open any prior review, admission record, independent-review record, board file,
board ledger, charter, transcript, chair report, or source outside the
explicitly permitted class.  Accordingly, this report makes no claim about
compilation, layout, page breaks, hyperlinks, index generation, visual quality,
human review, or final publication readiness beyond the direct mathematical
content audited here.

## Findings requiring correction

### M-01 — The Rabin finite-tree run is undefined

**Lines:** `n-c-014.tex` 1291--1305; downstream uses at 1307--1313 and
1392--1408.  The conflicting earlier run definition is at 1011--1024.  The
host's different bottom-up run is at `logic-in-computer-science.tex` 889--900.

The manuscript gives the data

\[
 \langle S,M,s_0,f\rangle,
 \qquad f\notin S,
 \qquad
 M:S\times\Sigma\longrightarrow
 \mathcal P\bigl((S\times S)\cup\{(f,f)\}\bigr),
\]

and says that it accepts when “a run” starts in (s_0) and assigns (f) at
the frontier.  It never defines that run.  There are two already available
meanings, and neither can silently supply the missing definition:

1. Lines 1011--1024 define an infinite-tree run as a map
   (r:T_x\to S).  Such a map cannot assign (f\notin S).
2. Host lines 889--900 define a bottom-up ranked-tree run assigning a state in
   (Q) to every node and accepting by a final root state.  Rabin's finite
   construction is top-down, labels only nonfrontier nodes, uses an external
   frontier value, and starts from (s_0).  It is intentionally a different
   object.

The omission propagates.  “Every run on (E_i) beginning in (s_i)” at
lines 1398--1405 has no typed quantifier domain, and the assertions about a
finite tree admitting no run, weak-MSO expressibility, the Lemma 3.12 lift,
Corollary 3.15, and the base of Theorem 1.6 therefore do not have a complete
local statement in the handbook.

The minimal repair is to define, before acceptance, a run on a finite valued
tree ((v,E)) as a map

\[
 r:E\longrightarrow S\cup\{f\}
\]

such that

\[
 r(\Lambda)=s_0,
 \qquad
 r(x)=f\quad(x\in\operatorname{Ft}(E)),
\]

and, for every (x\in E\setminus\operatorname{Ft}(E)),

\[
 r(x)\in S,
 \qquad
 (r(x0),r(x1))\in M(r(x),v(x)).
\]

Acceptance is then the existence of such a run.  If the author prefers to
separate run from acceptance as Rabin does, put the root and frontier clauses
in the acceptance definition but still give the run's map and transition
clause explicitly.  No new technical name is needed.

This is a genuine mathematical definedness defect and independently requires
`REJECT`.

### M-02 — The literal finite-tree definition admits the empty set, but later evaluates the root

**Lines:** `n-c-014.tex` 1278--1305 and 1392--1408.

The displayed conditions permit (E=\varnothing): it is finite,
predecessor-closed, has empty frontier, and satisfies the frontiered implication
vacuously.  But the intended finite run must be evaluated at the root
(\Lambda), and the emptiness base speaks of a run “beginning in (s_i).”  No
root exists in (E=\varnothing).

The issue is not cosmetic.  If the empty (E) were admitted as a finite tree,
the root condition would be undefined; if it were treated as automatically
false, every automaton would reject that object, contradicting the claimed
Boolean-algebra behavior of finite-tree languages under complement.  The
original historical page also proceeds immediately from predecessor closure to
a condition at (\Lambda), so its intended convention is a rooted, nonempty
tree even though the nonemptiness is implicit in its prose.

Add either

\[
 E\ne\varnothing
\]

or, more directly,

\[
 \Lambda\in E.
\]

For a nonempty predecessor-closed subset of (T), the latter follows from the
former, but stating (\Lambda\in E) exposes the exact reason the later root
condition is defined.  This repair should be made at the same location as the
finite-tree definition and before the run definition required by M-01.

This is a second genuine definedness defect in the same proof dependency.

### M-03 — Büchi's terminal-marker encoding needs positive tuple arity

**Lines:** `n-c-014.tex` 144--169.

The marker construction is correct for (n\geq1), which is the source's
operative finite-word setting.  The local text does not state that hypothesis.
At (n=0), however,

\[
 \top^0=\bot^0=(),
\]

so the alleged terminal marker is indistinguishable from the all-false tail and
every word over the singleton alphabet (\Sigma_0) receives the same
zero-tuple predicate.  The map is then not an encoding and cannot support the
claimed word/formula equivalence by length.

State (n\geq1) when introducing (\Sigma_n) and the word map.  This does not
alter any acquired-source claim; it makes the arity on which the source's
all-true marker depends explicit.

### M-04 — Trakhtenbrot's empty-language repair silently requires nonempty alphabets

**Lines:** `n-c-014.tex` 550--585 and 822--858.

The manuscript generalizes the source's binary definitions to “finite
alphabets” (A,B), then proves that the empty language is not
automaton-enumerable because every total length-preserving operator has a
nonempty range in every positive length.  That inference requires
(A\ne\varnothing) (and the stream-output setup ordinarily requires
(B\ne\varnothing)).

Literally take (A=\varnothing) and a nonempty finite (B).  Then
(A^{\mathbb N_+}=\varnothing), there is a unique total stream map from that
empty domain, and, for every (t\geq1),

\[
 A^t=\varnothing,
 \qquad
 T_t(A^t)=\varnothing.
\]

Thus the empty positive-length language is a lengthwise range and the sentence
at lines 851--853 is false under the literal empty-alphabet case.  The source
states the word result for binary alphabets, so no source theorem is lost by
writing “finite nonempty alphabets” at line 551 and again when making the
arbitrary-alphabet generalization at lines 835--837.  With that hypothesis, the
handbook's nonemptiness correction is sound: (A^t\ne\varnothing) for every
(t\geq1), so every total (T_t) has nonempty image.

### P-01 — The public finite-word host theorem should quantify its finite alphabet

**Lines:** `logic-in-computer-science.tex` 836--841.

The displayed theorem says only “A language of finite words.”  Every proof
route reconstructed in this item uses a fixed finite alphabet and finitely many
letter predicates.  The exact theorem should therefore begin, for example:

\[
 \text{Let (\Sigma) be a finite alphabet and (L\subseteq\Sigma^*).}
\]

Then state the MSO/regular equivalence for (L).  This is a scope and
quantifier repair, not a change in theorem strength.  If a global handbook
convention already makes every alphabet finite and nonempty, the local theorem
should cite that convention; no such convention occurs in the mandated host
region.

### T-01 — The game-player position names occur before their definition

**Lines:** `n-c-014.tex` 1526--1527; definition follows at 1534--1538.

“Automaton position” and “Pathfinder position” first occur while the manuscript
is still defining the completion, before the game and its two players are
introduced.  The next paragraph does supply the needed distinction—Automaton
chooses a transition and Pathfinder chooses a direction—but the order violates
the local terminology rule.

Either move that one-sentence player definition before line 1526, or change
lines 1526--1527 to the eliminable statement that every position in the
completed game has a nonempty outgoing-move set.  The distinction is necessary
and used, so the name may remain once its standing and moves have been defined.
This finding does not undermine the deadlock-completion proof, but it must be
repaired for publication under the supplied `AGENTS.md` rule.

## Complete mathematical audit

### 1. Büchi: weak finite-set logic, formula automata, and finite words

#### Definitions and standings, lines 8--71

- The authority boundary is exact: the 1959 UMR1083 report supplies the body,
  while the registered 1960 article supplies identity only.  The text does not
  project report pagination or wording onto the journal.
- “Weak” is correctly defined as finite-set monadic quantification over
  (\mathbb N), not as an alternation fragment or as the later full-set
  infinite-word theory.
- The (n/m)-automaton has the correct source standing: finite tuples of
  propositional formulae (E^m,H^m[Y^m,X^n]), inducing the unique deterministic
  recursion (r(0)=E), (r(t+1)=H(r(t),i(t))).  Formula tuple, input predicate,
  run predicate, output predicate, and behavior set are not conflated.
- The special-output identity
  (U(Y)=U(H(Y,\bot^n))) is the right pointwise condition.  Once a special
  input becomes all false, repeated use of that identity makes the Boolean
  output constant.  The eventual-truth definition of behavior follows.

No defect was found in this block.

#### Synthesis and repaired analysis, lines 73--142

The synthesis route is logically complete at outline strength: local normal
form supplies a quantifier-free base; output negation supplies complement;
state-form expansion and one-coordinate input removal supply existential
finite-set projection; alternation of projection and complement realizes the
finite set-quantifier prefix.

The criticism of Büchi's printed analysis formula is correct.  If the weakly
quantified run witness (r) is finite, it is eventually (\bot^m); requiring
(U(r(t))) on the cutoff tail therefore adds the unwarranted condition
(U(\bot^m)=\top).  The displayed one-bit counterexample has a constantly true
actual run, satisfies special-output invariance, accepts every special input,
and has no finite printed witness.

The handbook-owned replacement is sound in both directions.  Downward closure
and (j(0)) make (j) the initial segment (0,\ldots,h).  The recurrence
guard (j(t+1)) makes the finite witness equal the actual run through (h).
The clause (\neg j(t+1)\to i(t)=\bot^n) makes the input false from (h)
onward.  The boundary clause gives (U(r(h))), and special-output invariance
propagates this truth along the omitted actual tail.  Conversely, choose (h)
after both input extinction and permanent output truth, retain the actual run
through (h), and set only the later witness values false.  The case (h=0)
also satisfies every clause.  All clauses are local in time (t,t+1), so the
advertised existential local normal form follows.

No further defect was found in this block.

#### Word encoding, decision, and arithmetic, lines 144--229

- For positive (n), the all-true terminal marker makes the word encoding
  injective, includes the empty word, and keeps the resulting predicate finite.
  The arbitrary output is read at (r(h+1)), after the data letters and before
  any need to continue the run; this indexing is consistent, including the
  empty word where the state is (r(0)).  M-03 records the missing positive
  arity hypothesis.
- Theorem 6's bridge from arbitrary endpoint output to special-output behavior,
  Theorem 7's two translations, and Theorem 8's four-way regularity
  equivalence are stated at the precursor's actual strength.  The analysis half
  is correctly attached to the repaired witness, not to the false printed
  formula.
- The closed-sentence decision proof correctly tests
  (B(\bot,\bot)) before searching.  If that guard fails, no finite predicate
  can satisfy the all-false tail.  If it holds, a shortest path from a
  (K)-state to (\bot) is bounded by the finite Boolean state count; loop
  deletion justifies the inclusive source bound.
- The last-true-point encoding of a free individual is coherent at (x=0);
  the manuscript does not repeat the report's inconsistent prose about length.
- The ultimate-periodicity consequence is at the correct unary definability
  strength.
- The refutation of the unary powers-of-two bit formula is arithmetically
  correct: ((1,1)) is a false negative and ((2,8)) has the displayed false
  witness.  Replacing only (u<v) by (u<x) still permits the second false
  witness.  The later (\in_2/V_2) signature is correctly owned by later
  scholarship, while the sound first-order-to-weak-MSO direction still yields
  the claimed decidability consequence.

Apart from M-03, no defect was found.

### 2. Elgot: canonical finite-set words, design, arithmetic, and erratum

#### Acceptor and canonical assignment encoding, lines 231--343

- The controlling 1961 article, 1959 precursor, and 1962 errata have distinct
  authority.  The article controls publication claims and the errata controls
  corrections.
- The source acceptor is correctly typed as
  ((S,f,d,D)), with finite nonempty state set (S), total
  (f:I\times S\to S), and empty-word acceptance exactly when (d\in D).
- The finite-set encoding is canonical: the all-empty assignment maps to
  (\Lambda); every other assignment stops at its last nonzero column; and
  admissible words are (U_r^*U_r^0\cup\{\Lambda\}).  This also handles
  (r=0): the only assignment and only admissible word are empty.
- Formula-to-language induction includes the required right truncation after
  coordinate projection; plain projection would leave noncanonical terminal
  zero columns.
- The reverse construction has the correct temporal indexing.  A complete
  letter stores the state after its input column; the initial set contains
  ((x,f(x,d))), and adjacency uses (f(x_2,y_1)=y_2).  The terminal set
  (U_r^0\times D) and separate empty-word case yield exactly the requested
  admissible language.
- The decision and arithmetic consequences are downstream uses, not
  redefinitions of the automaton.  The finite carry set gives the claimed
  direction to Presburger arithmetic.

No defect was found.

#### Finite and infinite design, lines 345--401

- The (A/B)-automaton is correctly separated from the acceptor: it applies
  the state transition and then the total output map at each position, includes
  the empty paired word, and defines a total synchronous behavior.
- Theorem 7.1's four conditions are jointly sufficient.  Membership in
  ((A\times B)^*) enforces equal input/output length; prefix closure gives the
  source's “open” property; functionality and totality give a unique output at
  every input prefix; regular coordinate products recover finite memory.
- Strong extendibility is exactly the safety kernel needed by Theorem 8.1.
  If it is empty there is no transducer behavior contained in the
  specification.  If it is nonempty, lexicographic selection plus prefix
  closure and totality gives a realizing transducer.  The vacuous branch of
  Corollary 8.2 is correctly retained.
- Theorem 7.3 is a causal stream-behavior statement, not an omega-acceptance
  theorem.  Totality gives one output for every infinite input; prefix
  functionality makes it unique; hence the regular prefix language determines
  the behavior.

No defect was found.

#### Corrected infinite synthesis and negative boundary, lines 403--485

- The restricted syntax is explicit enough to justify bounded windows:
  quantifier-free (M), only successor iterates of (x) and (0), and no
  equality or order.  The corrected (1+\max h) window length is used.
- The manuscript does not silently collapse the erratum's finite union.  For
  arity (n\geq2), overlapping tagged windows force one constant tag and
  projection gives exactly the union.  For (n=1), replacing a unary
  constraint by (R_j\times R_j) preserves exactly the same infinite
  sequences; the tagged binary construction then forces a constant tag.  Empty
  or inconsistent components remain empty under this transformation.
- Only after that correction does finite-prefix regularity feed Theorem 8.1.
- The Post-system undecidability boundary is stated for the richer language and
  prevents an overbroad positive design claim.  Fixed-automaton satisfaction
  and existence of some satisfying automaton retain different quantifier
  strengths.

No defect was found.

### 3. Trakhtenbrot: portions, operators, synthesis, and finite words

#### Formal system and syntactic normal form, lines 487--548

The announcement and expanded article remain distinct primary bodies.  The
system (\mathcal I) has the correct positive-integer domain, arbitrary monadic
predicates, successor-only primitive term formation, and eliminable equality,
order, constants, and bounded quantifiers.  Fictitious occurrence is semantic
independence.  Upper and lower (t)-formulae are syntactic classes; their tail
and bounded-prefix dependence statements are separate consequences.  The
normal-form outline accounts for predicate prenexing, splitting at (t), and
the independence needed to distribute predicate quantifiers.

No defect was found.

#### Anticipation, whole-future memory, and portions, lines 550--745

- Anticipation and finite memory are correctly non-equivalent.  The maps
  (\Phi,\Psi) may inspect the entire current suffix, so a memory state need
  not be determined by the already read prefix.  A finite operator adds a
  bounded-lookahead requirement; the source's (A)-operator is the
  zero-lookahead case.  M-04 records the missing nonempty-alphabet hypothesis
  in the handbook's generalization.
- Tuple portions concatenate each coordinate separately.  Homogeneity counts
  residual sets, not states, and the residual operator (T_u) has the right
  type and shift.
- The handbook counterexample to the printed weight bound is correct.  With
  (q(1)=0) and
  (q(t+1)=q(t)\mathsf{xor}X(t)\mathsf{xor}X(t+1)), induction gives
  (q(t)=X(1)\mathsf{xor}X(t)).  The output
  ((1-q(t))X(t)) is therefore (X(t)) when (X(1)=1) and (0) otherwise.
  One state is impossible because its single suffix-output function must equal
  the leading bit at time one but would then give the wrong time-two output on
  a stream beginning (01).  The original graph, constant-zero residual,
  identity residual, and inconsistent empty residual are four distinct
  all-prefix portions; the three nonempty portions already refute the expanded
  source's bound.
- A singleton has finitely many residual tails exactly when its stream is
  ultimately periodic.  Homogeneity alone does not imply definability; the
  countability argument is sound.
- The empty closed homogeneous set is correctly separated from the source's
  total covering operator: a total operator cannot have empty image, while a
  contradictory initial state clause defines the empty set in the same
  recurrent syntactic family.
- The internal residual transition is effective without deciding nonemptiness;
  choosing permitted outputs requires the source's conditional truth oracle.
  The Putnam qualification is not erased.

Apart from M-04, no defect was found.

#### Finite realization and general solutions, lines 747--805

Compactness and the finite residual basis justify one bounded anticipation and
finite memory for a continuous definable total operator.  Dropping continuity
correctly leaves only finite memory.  A solution is correctly weaker than an
exact graph definition.  The general-solution clauses parametrize all and only
solutions of the named class; they are not collapsed to mere existence.  The
closed-relation theorem, its conditional deletion construction, the unbounded
weight of the separate open-relation statement, and the fixed-(p) extension
all retain their distinct strengths.

No defect was found.

#### Explicit synthesis and word boundary, lines 807--886

Zero anticipation makes each (T_t) independent of the chosen infinite
extension and makes the finite maps prefix-compatible.  The recognizer's
terminal value is equally well-defined.  Under finite **nonempty** input and
output alphabets, the handbook's correction to the printed converse is sound:
the empty language is decided by a constant-zero recognizer, but a total
length-preserving map has nonempty range at every positive length; nonemptiness,
prefix closure, and proper extendibility supply a seed word of every length for
the source construction.  M-04 is exactly the missing local hypothesis needed
for this reasoning.

The definition of a special beginning correctly requires the actual
eventually-zero predicate to be false after the displayed word.  The weak
system and the arbitrary-predicate system are not conflated, and the modern
regular/MSO sentence is not falsely attributed verbatim to the four-page
announcement.

### 4. Thomas's finite-word survey route, lines 888--925

The finite-word automaton has (n+1) run states for a length-(n) word.  State
tracks through the last input position plus a separate final transition give a
correct automaton-to-formula translation.  The empty word is the only edge at
which all tracks can be empty without witnessing an actual transition; the
reported existence guard exactly distinguishes whether (q_0\in F).

In the reverse direction, singleton-set atomic automata, Boolean closure, and
bit-track projection implement the formula constructors.  The input-free
successful-run test decides the weak theory, and reversed finite binary words
plus a finite carry set support the stated Presburger route.  This proof is
properly owned by the May 1996 report and is not substituted for any original
Büchi, Elgot, or Trakhtenbrot presentation.

No defect was found.

### 5. Rabin: infinite trees, duality, complementation, and emptiness

#### Structures and ordinary automata, lines 927--1042

- The source root symbol, concatenation, predecessor, initial-segment order,
  and lexicographic order are separately typed.  The editorial order subscripts
  are eliminable disambiguations.
- The structure (\mathfrak N_n) is stated for (0<n\leq\omega), and the
  finite-(n) order-definability qualification is retained.  The later
  non-elementary lower bound applies to a sublanguage of the binary theory and
  therefore correctly removes only Rabin's worst-case elementary-recursive
  claim, not decidability or effectivity.
- A path through (T_x) is infinite by the one-child continuation clause and
  predecessor closure.  The transition table may be partial.  Ordinary
  acceptance has the correct (\exists r\,\forall\pi) order and the correct
  Muller-family datum (F\subseteq\mathcal P(S)).  Arbitrary-root valued trees
  are not silently reduced to full-root trees in the definition.
- Projection, Boolean closure, complement, and emptiness have the correct
  dependencies.

No defect was found.

#### Formula tracks and both directions, lines 1044--1117

The track map is a bijection between (n)-tuples of node sets and full-root
(n)-bit trees.  Principal formulae have finite successor offsets, and the
worked example has an exact finite witness: choose a frontiered initial subtree
large enough that both the witness node and its left child are labelled
nonfrontier nodes.  The finite-tree lift then supplies the infinite-tree
automaton, subject to the finite-run definition required by M-01.

The converse run encoding uses finitely many state tracks and one universally
quantified path set.  Individual quantification in the matrix can express that
a given state occurs infinitely often along the path, so the stated
(\exists\bar B\,\forall C) set-quantifier prefix is sufficient.  For a closed
sentence, adding a dummy leading existential set if needed and testing
nonemptiness is sound; Rabin's source route has no regular-tree-basis step.

No further defect was found.

#### Theorem 3.1 product, lines 1119--1158

The product is correctly indexed.  At a node carrying product state ((u,s)),
both children receive first coordinate (K(u,s)); thus, before a branch splits,
the deterministic word-automaton history is shared.  Along a branch, the first
coordinate sequence is the deterministic run on the second-coordinate state
sequence, up to an irrelevant one-step shift.  Because the second coordinate is
finite,

\[
 p_1(\operatorname{In}(r))
 =\operatorname{In}(p_1\circ r),
\]

so the designated family
(\{C:p_1(C)\in H\}) enforces exactly the word condition.  McNaughton's theorem
is explicitly an external dependency, not a theorem reconstructed from an
unread body.

No defect was found.

#### Dual acceptance and complement, lines 1160--1322

- The pair-sequence type and type-empty refinement have the correct quantifier
  and set intersections.  Dual acceptance has the exact
  (\forall r\,\exists\pi) order and correctly permits vacuous truth when the
  partial table has no run from the named state.
- If the sequence is empty, no path map has its type, so the dual condition is
  equivalent to nonexistence of a rooted run.  The normalization
  (\Omega^\dagger=((S,S))) is exact: on an infinite path into a finite nonempty
  state set, the infinitely recurring set is nonempty; it cannot both meet and
  avoid (S).  Hence this one pair has the same impossible path type as the
  empty sequence and legitimately enters the positive-length induction.
- Marked trees, simultaneous-copy merging, and well-founded obligation
  dependencies have separate standings.  The no-infinite-descent definition is
  strong enough for the ordinal-stratum characterization, and the text places
  transfinite induction only in Lemmas 3.3 and 3.11 rather than substituting it
  for the finite-state proof.
- The two half-steps decrease the pair-sequence length in the stated order.
  The division among Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15
  is correct.

The only defects in this block are M-01 and M-02 in the finite-tree definition.

#### Emptiness, lines 1324--1419

The one-letter reduction is bidirectional: a labelled run forgets its labels,
and every run of the union table can choose, node by node, a label witnessing
its transition.  Complement followed by Lemma 3.6 therefore reduces original
nonemptiness to one specified dual-language membership question.

The restricted table keeps the root state unrestricted and forces precisely
the states strictly below it into (R'); the displayed intersection with
(R'\times R') proves that claim.  Over a finite state set, the transfinite
stages stabilize after finitely many nonempty additions.

The two handbook-owned empty choices are necessary and sufficient:

- (H=\varnothing) is the direct shorter dual question, including its
  permitted no-run/vacuous branch.
- At (k=1), (U_0=\varnothing) makes the universal finite-run condition say
  that (E_0) has no compatible run.  Finite branching and König's lemma make
  existence of such a finite obstruction equivalent to absence of an infinite
  run.

Once the finite run is explicitly defined and the finite tree rooted as required
by M-01/M-02, this base condition is expressible in weak MSO over the finite
tree: finitely many monadic tracks encode a candidate run and universal set
quantification excludes all candidates.  The cited finite-tree decision theorem
then closes the recursion.  The argument neither weakens full (S2S) nor uses a
regular-tree basis.

No additional defect was found.

#### Applications and proof boundary, lines 1421--1449

The Chapter II claims retain their distinct structures and quantifier ranges.
The (F_\sigma) determinacy statement is described as an (S2S)-expressible
statement decided by the procedure, not as a new source proof of a stronger
determinacy theorem.  The manuscript accurately says which complement details
it outlines and which remain in the complete article.

No defect was found.

### 6. Thomas's later infinite-tree route, lines 1451--1596

#### Muller and chain acceptance, lines 1451--1498

The run is global and the path condition is universal, so the essential
(\exists r\,\forall\pi) order is retained.  Chain acceptance has the right
avoid-(E_i)/recur-(F_i) condition.  The order-vector-with-hit is given an
exact standing as finite memory attached to a state, and eventual hit positions
are the reason it recovers the Muller recurrent set.  It is not confused with
an input tree, branch, or run.

No defect was found.

#### Deadlock completion, lines 1500--1529

The completion is mathematically sound.  It adds a fresh state outside every
chain set, fills exactly the missing state/letter transition cases with two
fresh children, and loops the fresh state.  Every old run remains.  If a run
uses an added transition, any path through a new child is thereafter constantly
fresh; its recurrent set meets no (F_i), so that run cannot be successful.
Thus the language and strict chain are preserved and all state/letter cases in
the subsequent game are live.  T-01 records only the premature player-position
names.

#### Complement game, regular-tree basis, and S2S, lines 1531--1596

- For the completed automaton, Automaton chooses a transition and Pathfinder a
  branch.  A winning Automaton strategy is equivalent to one global successful
  run; failure gives a memoryless Pathfinder strategy by the chain-game
  theorem.
- A node label (i:\Sigma\times\Delta\to\{0,1\}) contains finitely much data
  and can encode all of Pathfinder's local responses at that node.  The
  sequential omega-automaton step checks that no transition sequence consistent
  with those responses yields an accepting play; deterministic Muller tree
  acceptance universalizes that check over paths, and projection guesses the
  labels.  The resulting complement depends only on the source automaton.
- For emptiness, removing the input lets the automaton's move choose a label
  and transition.  A memoryless winning strategy on the finite game fixes an
  output label and two successor generator states at every reachable state,
  yielding a deterministic finite direction-word generator.  Hence every
  nonempty language has a regular tree and emptiness is decidable.
- Formula-to-automaton induction uses the completed complement operation for
  negation.  Conversely, existential state tracks plus a universal path track
  have the stated (\Sigma^1_2) form.  Applying effective emptiness to the
  input-free sentence automaton proves (S2S) decidable.
- The manuscript keeps this later game/basis route separate from Rabin's
  marked-tree complement and finite-tree emptiness route, and every locator is
  bounded to the May 1996 report.

No mathematical defect was found in these constructions.

### 7. Host theorems and finite-tree dependency

#### Public finite-word theorem, host lines 836--850

With a fixed finite alphabet and its unary letter predicates, order and
successor give equivalent MSO presentations on finite words: successor is
first-order definable from order, and reachability/order is MSO-definable from
successor by quantifying over successor-closed sets.  Endpoint cases, including
the empty word, can be split by a sentence asserting whether a position exists.
The regular/MSO equivalence is effective in both directions by the Thomas route
and is independently reflected in the source-specific Büchi and Elgot routes.
The prose correctly refuses to attribute the modern one-sentence formulation
verbatim to each original source.  P-01 is the missing local alphabet
quantifier.

#### S2S host theorem, host lines 873--876

The theorem states exactly the source-bounded conclusion supported by Rabin:
the monadic second-order theory of the full binary successor tree is decidable.
It adds no false modern complexity bound.

#### Ranked finite trees, host lines 878--928

- The inductive definition of (T_\Sigma) handles nullary leaves and also the
  edge case where no finite tree exists because the ranked alphabet has no
  nullary symbol.
- The bottom-up run and final-root acceptance are typed.  Partial transition
  sets are permitted.
- On a finite position domain, weak and full monadic quantification coincide
  because every subset is finite.  The text correctly refuses to transfer that
  coincidence to the infinite successor tree.
- Subset determinization, Boolean closure, membership, and bottom-up reachable
  state computation give the stated effective operations and emptiness test.

This host theorem is mathematically sound.  It does not cure M-01 by itself,
because Rabin's frontier-sentinel top-down run is a different construction; the
manuscript explicitly says those objects are distinct.

## Terminology, standing, and ownership audit

Except for M-01 and T-01, the technical names satisfy the supplied rule:

- source terms such as special predicate, admissible word, strong
  (A)-extendibility, portion, homogeneity, dual acceptance, type-empty,
  frontiered, chain acceptance, and regular tree are defined before their proof
  uses;
- editorial terms and symbols—order subscripts, residual (T_u),
  (\Omega^\dagger), and (\mathcal A^\bot)—have eliminable definitions,
  explicit standings, a stated distinction from existing objects, and an
  immediate proof use;
- the manuscript consistently distinguishes formulae, assignments, runs,
  automata, accepted languages, relations, residual operators, memory states,
  finite input trees, infinite input trees, and game strategies; and
- every handbook-owned correction is labelled as such rather than silently
  attributed to the historical source.

M-01 fails this rule substantively: “finite-tree run” is a new typed object
because it cannot be either existing run, but its exact definition is absent.
T-01 is an ordering violation: the player-position names are defined shortly
after, not at their first use.

## Source strength and register disposition

- **Büchi:** the mathematical presentation is admissible only at complete 1959
  report-precursor strength, with the printed Theorem 2 and Theorem 4/9 defects
  and handbook/later corrections explicit.  Literal 1960 journal reconciliation
  remains open and is not replaced by the precursor.
- **Elgot:** the controlling 1961 article plus the published 1962 errata support
  the stated claims; the 1959 report remains a separate precursor.  No open
  source blocker was found for this component.
- **Trakhtenbrot:** the four-page 1961 announcement and complete 1962 expansion
  support distinct source strengths.  No neighboring finite-word theorem is
  substituted for their operator-and-predicate theory.  M-04 concerns only the
  handbook's generalized alphabet hypothesis.
- **Rabin:** the complete 1969 article supports the structures, translations,
  complement architecture, source emptiness proof, and applications.  Meyer's
  later report correctly withdraws the elementary-recursive qualification.
  M-01/M-02 concern the handbook's failure to exactify the finite-tree object,
  including an implicit convention visible on Rabin's printed p. 30.
- **Thomas:** the May 1996 report supports the finite-word and later game/basis
  routes at precursor strength.  The final 1997 chapter remains unread and
  unreconciled, so final-chapter strength is open.
- **External dependencies:** McNaughton's deterministic-word equivalence and
  the finite-tree weak-MSO theorem are identified as dependencies rather than
  silently claimed as reconstructed original-source proofs.  Their use does not
  change the bounded verdict on the material actually presented here.

## Required disposition

Before a new mathematical review, make the smallest source-faithful corrections:

1. add (\Lambda\in E) (or (E\ne\varnothing)) to Rabin's finite-tree
   definition;
2. define the finite run explicitly as an
   (E\to S\cup\{f\}) map with the root, frontier, and local transition
   clauses;
3. state (n\geq1) for Büchi's all-true terminal-marker encoding;
4. state finite **nonempty** alphabets in the generalized Trakhtenbrot operator
   and word passage;
5. quantify the finite alphabet in the public finite-word host theorem; and
6. define the Automaton/Pathfinder positions before first naming them, or use
   eliminable generic wording in the completion paragraph.

No change to the valid handbook-owned proof repairs is otherwise required by
this review.

REGISTER STATUS: OPEN
