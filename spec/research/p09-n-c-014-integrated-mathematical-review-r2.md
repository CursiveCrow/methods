REJECT

# N-c-014 integrated mathematical/proof review — Round 2

## Verdict

The actual reader LaTeX is not yet mathematically publication-admissible.  The
bounded precursor/source posture is acceptable: this verdict is **not** based on
the unavailable literal body of B\"uchi's 1960 journal article or on the still
unreconciled 1997 Thomas chapter.  It is based on three defects in the text that
is present: Rabin's decisive finite-run base case quantifies an undefined kind
of run, Elgot's effective deletion construction invokes an undefined object,
and Thomas's automata/chain presentation omits types and the zero-pair chain
needed by its own Muller-to-chain theorem.

The B\"uchi, Trakhtenbrot, Rabin ordinary/dual-acceptance, Rabin finite-tree
transition, Thomas deadlock-completion, host finite-word theorem, host S2S
theorem, and host finite-ranked-tree results otherwise survive the
mathematical checks below at the source strengths expressly claimed.

## Blocking findings

### R2-MATH-01 — Rabin's p. 34 base case never defines the finite runs it quantifies

**Location:** `handbook/parts/p09/presentations/n-c-014.tex:1362-1376` and
`handbook/parts/p09/presentations/n-c-014.tex:1467-1483`.

Lines 1362--1374 define one precise finite-tree run: for a finite-tree automaton
`<S,M,s_0,f>`, it is a map
\(r:E\to S\cup\{f\}\), it assigns the external value \(f\) to every frontier
node, and it obeys the finite-tree transition table at every nonfrontier node.
That is not the object needed in the emptiness base.

Lines 1467--1480 have returned to a current one-letter table
\(\langle R,N\rangle\), with no external frontier value, and quantify over
“every run on \(E_i\) beginning in \(s_i\).”  No type, root clause, or local
transition clause is supplied for those finite maps.  Reading “run” as the only
finite run already defined is impossible: the current table has no \(f\), and
the claimed \(m=0\) equivalence is about the absence of an \(R\)-valued finite
partial run, not the absence of an \(f\)-frontier automaton run.  Reading it as
the infinite-tree run of lines 1055--1059 is also impossible because its domain
is \(T_x\), not finite \(E_i\).

The original historical-source check of Rabin's printed p. 34 settles the
intended condition.  With
\(U_0=\{s_1,\ldots,s_m\}\subseteq U_1\), it quantifies finite trees
\(E_0,\ldots,E_m\) and requires, for each \(i\), every table-run \(r\) on
\(E_i\) with \(r(\Lambda)=s_i\) to satisfy
\[
 r(E_i\setminus\{\Lambda\})\cap U_0\ne\varnothing.
\]
The handbook correctly repairs the source's printed nonemptiness restriction
by allowing \(m=0\), but the repair cannot be checked until the finite maps in
that display are defined.

**Required repair:** at the base case, state the owed object rather than naming
an unspecified run.  For the current table \(\langle R,N\rangle\) and a finite
frontiered \(E\), quantify maps \(r:E\to R\) satisfying
\(r(\Lambda)=s\) and
\((r(x0),r(x1))\in N(r(x))\) for every
\(x\in E\setminus\operatorname{Ft}(E)\).  State the hit condition exactly as
\(r(E\setminus\{\Lambda\})\cap U_0\ne\varnothing\), and explicitly distinguish
these maps from the \(f\)-frontier runs at lines 1362--1374 and from infinite
\(T_x\)-runs.  Then the \(m=0\) clause is literally the assertion that no such
finite map rooted at \(s_0\) exists, and K\"onig's lemma yields the advertised
equivalence with absence of an infinite run.

This is a blocker because the finite-run predicate is the terminal decision
condition in Theorem 1.6's reconstructed emptiness proof; it is not optional
expository detail.

### R2-MATH-02 — Elgot's effective fixed point invokes undefined “finite complete states”

**Location:** `handbook/parts/p09/presentations/n-c-014.tex:374-385`.

The text exactly defines \(A\)-extendability and strong \(A\)-extendability, but
then says that Lemma 6.1 constructs \(\gamma_A\) “by repeatedly deleting finite
complete states.”  No set of such objects, membership condition, transition, or
deletion operator has been defined.  The phrase is used only here, so it also
fails the local necessity/definition/standing/nonredundancy/use rule in
`AGENTS.md`.

The original historical-source check of Elgot's printed pp. 37--39 resolves
what the proof actually does.  Starting from an \(A\times B\)-automaton for
\(\gamma\), it works with a finite set of augmented letter/output/state data and
iteratively restricts that set: a datum survives the next stage exactly when,
for every next input letter, some compatible output/state successor survives
the current relation.  The descending finite sequence stabilizes, and the
stable relation is projected to obtain \(\gamma_A\).  “Finite complete states”
in the reader neither defines that finite carrier nor states this recurrence.

**Required repair:** describe that already owed finite carrier and survival
recurrence directly, or delete the undefined phrase and cite the source proof
without purporting to summarize the effective construction.  Do not introduce
a one-use replacement name.  The proof must still make clear why the iteration
terminates and why every strongly \(A\)-extendable sublanguage is contained in
the fixed point.

This is a blocker because effectivity and maximality are the content used by
Theorem 8.1 and Corollary 8.2, not merely an unused historical aside.

### R2-MATH-03 — Thomas's automata are under-typed, and the required empty Rabin chain is omitted

**Location:** `handbook/parts/p09/presentations/n-c-014.tex:932-962` and
`handbook/parts/p09/presentations/n-c-014.tex:1526-1567`.

The finite-word tuple at lines 935--942 types only \(\Delta\).  It never states
that \(Q\) is finite, that \(q_0\in Q\), or that \(F\subseteq Q\); nor does it
state the alphabet finiteness at that definition.  Without finite \(Q\), the
claim at lines 943--945 is not the finite-automaton/MSO theorem.  The tree tuple
at lines 1529--1546 likewise types only \(\Delta\): it does not locally state
that \(Q\) is finite and nonempty, that \(\Sigma\) is the finite input alphabet,
that \(q_0\in Q\), or that
\(\mathcal F\subseteq\mathcal P(Q)\).  The words “Muller tree automaton” occur
inside the definition being supplied and cannot themselves discharge all of
those types.

More seriously, lines 1553--1564 display a strict chain
\[
 E_1\subsetneq F_1\subsetneq\cdots
 \subsetneq E_m\subsetneq F_m\subseteq Q
\]
without declaring the range of \(m\) or admitting \(m=0\).  The zero-pair case
is necessary.  Take a Muller tree automaton with
\(\mathcal F=\varnothing\) (or \(\mathcal F=\{\varnothing\}\)); every infinite
path over finite nonempty \(Q\) has a nonempty infinitely recurring state set,
so no run is successful.  No nonempty strict chain can define the identically
false path condition in general: every pair has a nonempty upper set and is
satisfied by a constant path in an upper-set state outside its lower set.  The
empty chain, whose existential “for some \(i\)” condition is false, does define
it.

The original historical-source check of Thomas's printed pp. 44--46 confirms
both the inherited Muller types and the issue.  Definition 6.4 prints the proper
strict chain, while Theorem 6.5 constructs \(E_i,F_i\) and explicitly says to
drop a pair when \(F_i=E_i\) (and to drop the adjacent pair when
\(E_{i+1}=F_i\)).  For the rejecting Muller family, all constructed pairs can be
dropped.  Thus the theorem's construction itself requires the resulting proper
chain to be allowed to have length zero.

**Required repair:** locally type both Thomas automata.  At minimum, state that
\(Q\) is a finite nonempty state set, \(q_0\in Q\), the input alphabet is finite,
\(F\subseteq Q\) in the word case, and
\(\mathcal F\subseteq\mathcal P(Q)\) in the Muller-tree case.  State
\(m\geq0\) for the chain and say explicitly that \(m=0\) is the empty sequence
and rejects every path.  Carry that trivial base through Theorem 6.5, the game
argument, complementation, and the basis/emptiness route.  For the completed
game the empty-chain case is harmless: after the already supplied deadlock
completion, Pathfinder wins trivially from every position.

This is a blocker because, as written, Theorem 6.5 is not true for every Muller
tree automaton admitted by Definition 6.1, and the omitted finiteness hypotheses
are required by the later finite-game and regular-generator conclusions.

## Review protocol and evidence boundary

- I read `handbook/parts/p09/presentations/n-c-014.tex:1-1671` directly through
  EOF and `handbook/parts/p09/logic-in-computer-science.tex:836-946` directly,
  including the `n-c-014` input at host line 937.
- I did not inspect a manuscript PDF, page image, render, crop, or derivative.
  I did not run TeX, a build, a test, a checker, a repository script, or an
  automated validator, and I did not use a hash as mathematical evidence.
- I did not open a Round 1 report, independent-review record, admission record,
  board file, board ledger, charter, transcript, or chair file.
- The five permitted source notes were read as source-reconstruction records.
  The `N-c-014` and consolidated open-source portions of
  `spec/research/p09-source-presentations-lot2-3.md` were used only to delimit
  current source strength, never as proof that the manuscript is correct.
  Relevant bibliography entries were checked for the cited identities.
- Four concrete ambiguities could not be resolved from the permitted notes.
  Under the express historical-source exception, I consulted only the relevant
  original source pages: Elgot 1961 pp. 37--39; Rabin 1969 pp. 30 and 33--34;
  and Thomas's May 1996 report pp. 8 and 44--46.  Those pages supplied the
  historical-source evidence expressly identified in the findings above.  No
  historical-source page was treated as a manuscript render.

## Complete mathematical reconstruction and disposition

### B\"uchi precursor presentation — lines 8--229

**Version and domain, lines 8--29.**  The text limits itself to the complete
1959 UMR1083 precursor and leaves literal 1960 reconciliation open.  It types
individuals as \(\mathbb N\), explains that a special predicate is an
eventually-false Boolean predicate/equivalently a finite subset, and correctly
distinguishes weak finite-set quantification from both alternation fragments and
the later full-set theory.

**Automaton and behavior, lines 31--71.**  The finite data are the formula
tuples \(E^m,H^m[Y^m,X^n]\); the induced run satisfies
\(r(0)=E\) and \(r(t+1)=H[r(t),i(t)]\).  The special-output identity
\(U(Y)=U(H(Y,\bot^n))\) is the correct pointwise invariance.  Once the input is
all false it makes the output constant, and the behavior's
\(\exists x\forall t\geq x\) quantifiers correctly express eventual permanent
truth.  Formula data, predicates on time, and the accepted set remain distinct.

**Synthesis and repaired analysis, lines 73--142.**  The local normal form has
the right finite-set quantifier prefix and adjacent-time matrix.  Complement,
expanded propositional form, and existential input projection have the right
roles.  The counterexample
\(E=\top,H(y,x)=y,U(y)=y\) proves that printed formula (2) incorrectly forces
\(U(\bot)=\top\).  The handbook repair is sound: a finite nonempty downward
closed \(j\) is exactly \(\{0,\ldots,h\}\); recurrence is required through
\(h\), the input is false from \(h\), and \(U(r(h))\) propagates along the
omitted all-false tail.  Conversely an accepted special input supplies such an
\(h\), including \(h=0\).  All repair clauses are local in \(t,t+1\), so the
advertised existential local form follows.

**Marker encoding and empty word, lines 144--169.**  The hypothesis \(n\geq1\)
prevents the zero-track marker from collapsing.  A nonempty word has its data at
\(0,\ldots,h\), the explicit \(\top^n\) marker at \(h+1\), and false tail; the
empty word has the marker at zero.  String acceptance at \(r(h+1)\) is after
the last data symbol, and arbitrary-output string behavior is correctly kept
separate from special-output eventual behavior.

**Decision and arithmetic boundary, lines 171--229.**  The free-individual
encoding uses the displayed last-true-point convention, including zero.  For a
closed normal sentence, \(B(\bot,\bot)\) is a necessary false-tail guard; when
it holds, loop deletion gives the finite inclusive search \(x\leq k\).  The
ultimate-periodicity conclusion has the right phase/period interpretation.  The
two numerical witnesses show that the printed bit-occurrence formula is false,
and the text correctly refuses the unary-\(\operatorname{Pw}_2\) equivalence
while retaining the one sound translation needed for decidability.  The later
\(\in_2/V_2\) signature is identified as correction evidence, not attributed
to the precursor.

**Disposition:** no mathematical finding in this block.

### Elgot presentation — lines 231--522

**Finite acceptor and empty word, lines 231--256.**  The input alphabet and
state set are finite nonempty; \(f:I\times S\to S\), \(d\in S\), and
\(D\subseteq S\) have the right standings.  The \(n+1\)-state run convention
and \(\Lambda\in T(\mathfrak A)\iff d\in D\) are correct.

**Finite-set columns and Theorem 5.3, lines 258--343.**  The canonical encoding
ends at the last nonzero column and maps the all-empty assignment to
\(\Lambda\).  Thus admissible words are exactly
\(U_r^*U_r^0\cup\{\Lambda\}\).  Formula-to-language closure uses relative
complement and, crucially, coordinate projection followed by right truncation.
The reverse construction correctly stores the post-letter state, uses
\(f(x_2,y_1)=y_2\) for adjacency, requires the terminal input column to be
nonzero and state final, and treats the empty word separately.  The finite carry
set and arithmetic consequences are kept as consequences, not automaton
definitions.

**Design and finite/infinite behavior, lines 345--401.**  The transducer applies
\(f\) and then \(g\), includes the empty paired word, and is kept distinct from
the acceptor.  The four conditions in Theorem 7.1 give regularity, prefix
closure, output functionality, and input totality.  Strong extendability is
defined with the correct \(\forall a\exists b\) order.  Theorem 8.1 and the
vacuous uniqueness case of Corollary 8.2 are correct once Lemma 6.1's effective
fixed point is actually defined; that missing definition is finding
R2-MATH-02.  Theorem 7.3 is a total causal graph theorem, not an omega-word
acceptance condition.

**Arbitrary-set specification and erratum, lines 403--495.**  The predicate
tuples, total dimension \(d\), characteristic streams, quantifier-free matrix,
successor-iterate restriction, and window length are stated before use.  The
erratum's finite union is not collapsed to one component.  For arity at least
two, overlapping tagged windows force one constant tag.  For unary windows,
promotion to \(R_j\times R_j\) preserves exactly the pointwise constraint and
allows the same tag argument; the one-letter prefix condition is retained.
These two cases make the projection claim sound.

**Negative boundary and version ownership, lines 497--522.**  Finite-predicate
satisfiability, its maximal r.e. degree, the fixed-machine/existential-machine
distinction, and the published-errata ownership are separated correctly.

**Disposition:** R2-MATH-02 only.

### Trakhtenbrot presentation — lines 524--930

**Formal system and normal form, lines 524--585.**  The announcement and
expansion are not silently identified.  \(\mathcal I\) names the interpreted
language, individuals range over \(\mathbb N_+\), predicate variables range
over all subsets, and only successor-iterate membership is primitive.  The
upper/lower syntactic classes are distinguished from their prefix/tail semantic
dependence, and the normal-form proof operations are given in the right order.

**Operators, lines 587--640.**  Anticipation has the correct prefix-agreement
quantifiers.  Broad finite memory allows \(\Phi\) and \(\Psi\) to inspect the
whole suffix, so it is correctly separated from bounded anticipation.  A finite
operator has both properties; the zero-anticipation automaton-realizable class
has its announcement/expansion naming boundary stated.  Weight is a minimum
over finite presentations.  “Periodic” is correctly read as ultimately
periodic.

**Portions, graphs, and the source counterexample, lines 642--780.**  Portions
are coordinatewise and may be empty under the selected announcement convention.
The graph calculation
\((G_T)_{(u,v)}=G_{T_u}\) for the unique output prefix and empty otherwise is
typed correctly.  In the counterexample, the displayed two-state equations do
give \(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\), hence the required output; the
one-state contradiction at input prefix \(01\) is valid.  The graph has the
original, constant-zero, identity, and empty portions, so the source's weight
bound is genuinely false.  The nonempty covering construction has image
\(\overline M\); closedness yields \(M\), and the contradictory initial clause
correctly handles \(M=\varnothing\).

**Effectivity, realization, and general solutions, lines 782--849.**  Internal
portion transitions are effective, while output choice needs emptiness
decisions.  Continuity plus compactness supplies bounded anticipation; dropping
continuity yields only broad finite memory.  “Solution” means graph containment.
The two clauses of a general solution quantify all and only substitutions of
the named class.  The fixed-lookahead result is correctly stated one \(p\) at a
time.

**Finite-word boundary, lines 851--930.**  The maps
\(T_t:A^t\to B^t\) are extension-independent and prefix-compatible for
\(t\geq1\).  Enumeration and terminal recognition have correct types.  The
empty language proves that the printed converse needs nonemptiness; together
with prefix closure and proper extendibility, nonemptiness supplies a word at
every positive length.  A special beginning is correctly stronger than an
arbitrary finite prefix.  The modern regular/MSO sentence is not falsely
attributed verbatim to the four-page announcement.

**Disposition:** no mathematical finding in this block.

### Thomas finite-word route — lines 932--969

The run length, transition indices, final-state condition, and empty-word guard
are correct.  State tracks stop at \(r(n-1)\), so the final input letter must be
handled by an \(F\)-successor exactly as stated.  The singleton-set atomic cases,
Boolean operations, projection, WS1S decision, and carry-set Presburger route
have the correct roles.  The source is explicitly bounded to the 1996 report
and is not substituted for the three historical presentations.

**Disposition:** the missing tuple hypotheses are part of R2-MATH-03.

### Rabin structures, translations, complement, and emptiness — lines 971--1524

**Structures and ordinary automata, lines 971--1086.**  The two order symbols
are disambiguated without creating new relations.  The predecessor fixes the
root and removes one letter elsewhere.  \(T_n\), \(\mathfrak N_n\), and \(SnS\)
have the correct range \(0<n\leq\omega\); finite-\(n\) definability of the
orders and the \(S\omega S\) interpretation are separated.  The later lower
bound invalidates only Rabin's elementary-recursive qualification.  A path
through arbitrary \(T_x\), a valued subtree, table, automaton, run, and Muller
family are all separately typed.  Ordinary acceptance has the essential
\(\exists r\forall\pi\) prefix and allows partial move tables.

**Tracks and both logical directions, lines 1088--1177.**  The characteristic
track map is bijective.  Principal formulas have finite successor offsets;
Boolean closure and set projection have the right dependencies.  The finite
witness is rooted, predecessor-closed, and frontiered, so both labelled witness
nodes can be internal.  The converse state-track formula has the right
\(\exists\bar B\forall C\) set prefix.  Sentence truth reduces directly to
automaton nonemptiness, with no regular-tree basis inserted into Rabin's proof.

**Path product, lines 1179--1218.**  The product transition updates both child
first coordinates by \(K(u,s)\).  Along a branch this is the unique deterministic
word-automaton run, and projecting an infinitely recurring product-state set to
\(U\) gives exactly the recurrent word states because the second coordinate is
finite.  Determinism is correctly identified as the coherence requirement.

**Duality and zero pairs, lines 1220--1336.**  Type \(\Omega\), type
\(\Omega\)-empty, and dual acceptance have the correct quantifiers.  Vacuous
dual acceptance when no run exists is preserved.  If the sequence is empty,
its path type is empty; \(((S,S))\) also has empty path type by the infinite
pigeonhole principle.  Thus the one-pair normalization is exact and allows the
positive-length induction.  The marked obligations, no-infinite-descent
definition, ordinal stratification, two half-steps, and induction on pair count
retain their distinct roles.

**Finite-tree transition, lines 1338--1388.**  The original historical-source
check of Rabin's printed p. 30 confirms the manuscript's unusual but literal
codomain
\[
 M:S\times\Sigma\longrightarrow
   \mathcal P\bigl((S\times S)\cup\{(f,f)\}\bigr),
 \qquad f\notin S.
\]
It is not a typo for all pairs in \((S\cup\{f\})^2\).  The manuscript correctly
identifies \(f\) as an external frontier value.  A frontiered tree can have one
frontier child and one internal child; such a shape simply has no run for this
source automaton at that node.  Nothing in the stated lift or later finite-level
witness use assumes that every frontiered shape has a run.  Lemma 3.12,
Corollary 3.13, Lemma 3.14, and Corollary 3.15 are assigned their correct and
different roles.

**One-letter reduction and finite recursion, lines 1399--1494.**  Union over
input labels is equivalent to existentially choosing a valuation node by node.
Complement followed by Lemma 3.6 correctly returns the original one-letter
language as a dual language.  The restricted table constrains precisely the
states strictly below the root.  Finite state space bounds the nonempty strata.
The \(H=\varnothing\) branch is the direct shorter question, and allowing
\(U_0=\varnothing\) is necessary for vacuous dual acceptance.  The mathematical
content of those repairs is right, but the decisive finite maps are not defined;
that is R2-MATH-01.  The weak finite-tree theorem remains an external base and
does not weaken S2S quantification.

**Applications and boundary, lines 1496--1524.**  The listed interpretations
are clearly application results rather than parts of the main automaton
definition.  The text accurately says which complement details remain in the
complete article.

**Disposition:** R2-MATH-01 only.  The source-literal finite-tree transition is
accepted, not a finding.

### Thomas infinite-tree/game/basis route — lines 1526--1671

**Run and acceptance, lines 1526--1551.**  The global run and its
\(\exists r\forall\pi\) acceptance order are correct, subject to the missing
tuple types in R2-MATH-03.  The B\"uchi/Muller separation examples are assigned
only their stated role.

**Chain conversion, lines 1553--1573.**  The path test has the correct
\(\exists i\) pair quantifier and the order-vector-with-hit has the correct
standing as finite state memory.  The omitted zero-pair case makes the claimed
conversion incomplete, as proved in R2-MATH-03.

**Deadlock completion, lines 1575--1608.**  The completion itself is sound.
Every original run remains.  If an added transition is used, either new child
begins a path that remains forever at \(\bot\); because \(\bot\) belongs to no
upper chain set, that path satisfies no pair.  Hence no successful run uses an
added transition, while every state/letter position gains a move.  The chain is
unchanged and the new notation's standing, difference, necessity, and use are
all stated.

**Game complement, lines 1609--1637.**  Automaton chooses a transition and
Pathfinder chooses a direction, so a single play follows one state sequence.
Nonacceptance plus memoryless determinacy gives local instruction functions;
the instruction-labelled tree has a finite alphabet.  Universal path checking
and nondeterministic instruction guessing produce an automaton depending only
on \(\mathcal A\), not the input tree.  Completion supplies the game theorem's
nonempty-outdegree premise.

**Regular member and S2S, lines 1639--1671.**  A regular input tree is correctly
a deterministic direction-word generator with an output map, not an acceptance
mode.  A memoryless winning strategy fixes finite generator data; this gives
emptiness and a regular member.  Formula induction uses complement only after
the language-preserving completion, and the reverse state-track/universal-path
translation has the right quantifier architecture.  The report-precursor and
Rabin/non-Rabin boundaries are explicit.

**Disposition:** R2-MATH-03 only.

### Host theorems and input boundary — host lines 836--946

**Finite words, lines 836--851.**  For a finite alphabet, MSO over order and
MSO over successor with definable endpoints give the same finite-word languages,
and the regular equivalence is correct.  The text expressly labels this as the
modern formulation and does not claim verbatim occurrence in every historical
source.  The empty-alphabet case causes no counterexample:
\(\Sigma^*=\{\Lambda\}\), and its two languages are both regular and MSO
definable.

**S2S, lines 874--877.**  The host theorem is exactly the decidability of the
full binary successor structure.  The preceding Rabin presentation explains
why adding the definable finite-\(n\) orders does not change it.

**Finite ranked trees, lines 879--929.**  Ranked symbols, term formation,
bottom-up transitions, accepting root state, and the recognized language are
typed.  On a finite domain every monadic subset is finite, so weak and full
quantification coincide there but not on the infinite binary tree.  Subset
determinization, Boolean closure, membership, and upward reachability for
emptiness are correct.  The host automaton is explicitly distinguished from
Rabin's top-down infinite-tree run and from his source-specific finite-tree
run.

**Integration, lines 931--946.**  The figure references do not supply proof for
N-c-014.  The `n-c-014` input is present at host line 937.  No neighboring input
was used as a substitute for the reviewed presentation.

**Disposition:** no mathematical finding in the host block.

## Source-strength and register conclusion

- The 1959 B\"uchi report precursor is sufficient for the bounded reconstruction
  actually claimed, provided its printed defects and handbook repairs remain
  explicit.  Literal 1960 journal reconciliation remains open but is not a
  reason for this rejection.
- Elgot is reviewed at controlling 1961-article plus published-1962-errata
  strength, with the report kept as precursor evidence.
- Trakhtenbrot is reviewed at the distinct 1961-announcement and
  1962-expansion strengths stated in the reader.
- Rabin is reviewed against the complete 1969 article, with Meyer's later
  complexity correction confined to the false worst-case qualification.
- Thomas is reviewed only at May 1996 report-precursor strength.  The 1997
  reconciliation remains open but is not a reason for this rejection.
- R2-MATH-01 through R2-MATH-03 must be repaired in the actual LaTeX and then
  freshly re-read.  No build or rendered-page result can substitute for that
  mathematical re-review.

REGISTER STATUS: OPEN
