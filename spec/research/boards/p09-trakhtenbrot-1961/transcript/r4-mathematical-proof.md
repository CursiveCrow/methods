# Round 4 mathematical and proof-correctness review: `N-c-014.c`

## Disposition

I found no blocker, must-fix, or other mathematical finding in the frozen
Round 4 snapshot.  The reconstruction states the operator classes at their
different strengths, gives the necessary topological hypotheses, preserves
both quantifiers in the general-solution definition, keeps the fixed-
anticipation theorem fixed at one bound, and repairs the two genuine empty-
object edge cases without damaging any later weight claim.

This verdict is only for the mathematical/proof-correctness mandate on
`N-c-014.c` and the seven hash-pinned objects in the charter.  It does not
certify a Russian specialist translation, another registered presentation,
the rendered handbook, a build, or final publication acceptance.

## Blindness, evidence boundary, and source-language competence

I read the charter before the frozen objects.  I did not read `ledger.md`,
`transcript/chair.md`, any Round 1--3 report, either other Round 4 report, or
another board.  I did not contact another seat.  I used no text extraction as
controlling evidence and ran no test, checker, repository script, TeX command,
build, or handbook-PDF inspection.  The only computation was the expressly
permitted recomputation of the seven SHA-256 identity labels.

I have working reading competence in mathematical Russian sufficient to read
the displayed definitions, theorem statements, proof transitions, examples,
and qualifications in these two papers.  I do not claim native or specialist
Russian philological certification.  For this review I used the original
rendered pages at original detail, treating their Russian prose and printed
formulae as controlling, and compared the bounded English reconstruction in
the frozen manuscript and source record against them.

## M01: independently recomputed frozen identities

All seven SHA-256 values recomputed exactly to the Round 4 charter labels.

| Frozen object | Independently recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` | exact match |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `D3480007167E06CEDB9FB6ABF847F66F3113A4907B72FA92BE80BAF3378B349A` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | exact match |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` | exact match |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `A1ED4C1AF0E173AFDEAE98FC7C49BD9BB1C0ED4D72BAF61D6E8AFC1B571D78BC` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `7024F2410F69BD0D4ADFF3B31E9ED316BDB23AE27704984D0691BE0F1A1CC63A` | exact match |

## M02: original-detail source-page inspection

I visually inspected all thirty-three rendered source pages at original
detail.  The physical-to-printed map is exact and gap-free:

| Source body | Physical images inspected | Printed-page map | Visible identity checks |
|---|---|---|---|
| 1961 announcement | `rendered/page-1.jpg` through `page-4.jpg` | image (i) is printed p. (325+i), hence pp. 326--329 | *Doklady Akademii Nauk SSSR*, 1961, vol. 140, no. 2; Russian title; B. A. Trakhtenbrot; presentation and receipt notices; theorem sequence 1--5 and (4'); bibliography and correction note |
| 1962 expansion | `expanded-rendered/page-01.jpg` through `page-29.jpg` | image (i) is printed p. (102+i), hence pp. 103--131 | *Sibirskii Matematicheskii Zhurnal*, vol. III, no. 1, January--February 1962; same Russian title; B. A. Trakhtenbrot; five sections; receipt notice; bibliography |

No page was missing, duplicated, reordered, or transferred between the two
bodies.  Formulae, Cyrillic/Latin operator letters, theorem numbering, and
page locators below were checked from these images rather than from a text
reading aid.

## Independent mathematical derivation

### 1. The system \(\mathcal I\), semantic dependence, and normal form

The reader at `n-c-014.tex:487--525` and the source note at
`p09-trakhtenbrot-1961-source-note.md:79--143` agree with announcement
pp. 326--327 and expanded pp. 103--109.

The standing is exact.  Cyrillic И names an interpreted monadic formal
language.  Individuals range over \(\mathbb N_+=\{1,2,\ldots\}\), monadic
variables range over arbitrary subsets, and immediate successor is primitive.
Equality, order, bounded individual quantification, constants, and \(t+k\) are
eliminable extensions, not silently added primitives.  This also keeps
\(\mathcal I\) distinct from the eventually-zero interpretation later called
\(\mathcal I'\).

The definition of fictitious occurrence is semantic: two interpretations that
can differ only outside the named interval must give the same truth value.
Thus it correctly supports both a lower formula, whose relevant prefix ends at
\(t+s\), and an upper formula, whose relevant tail starts at \(t\).

I independently checked the effective normal-form proof.  Predicate
quantifiers are first moved before individual quantifiers; the individual
quantifiers are pushed into the Boolean matrix and split at \(t\).  For a
predicate quantifier applied to a lower/upper conjunction, one expands over
the finitely many truth patterns of the quantified predicate on the overlap
\(t,\ldots,t+s\).  Once one such overlap pattern is fixed, a lower witness and
an upper witness agree there and can be spliced; this gives the conjunction of
the separately quantified lower and upper pieces.  Disjoining over the finite
overlap patterns and restoring the Boolean matrix yields the stated Boolean
combination.  This is the exact move printed on expanded p. 109 and validates
the compressed architecture at manuscript lines 519--523; no unjustified
distribution of a quantifier across overlapping data is being used.

### 2. Anticipation, finite memory, weight, and finite operators

The typed definitions at `n-c-014.tex:527--571` agree with expanded
pp. 109--112.  For a total stream map, anticipation \(p\) means that agreement
through \(t+p\) fixes output position \(t\).  At \(p=0\), this is equivalent to
extension independence and prefix compatibility: two infinite extensions of
the same length-\(t\) input word have the same first \(t\) output letters.

The finite-memory equations intentionally permit \(\Phi\) and \(\Psi\) to
inspect the whole future suffix.  Therefore finite memory does not imply a
lookahead bound.  The one-state operator
\[
 b(t)=1\quad\Longleftrightarrow\quad(\exists \tau>t)\,a(\tau)=1
\]
is the source's decisive example: one memory state suffices, but the output on
the all-zero suffix cannot be determined from any finite lookahead and the
operator is not recursive in the relevant stream sense.  This confirms the
manuscript's nonimplication at lines 538--554.

A finite operator adds one uniform anticipation bound, so its equations reduce
to a fixed window \(a(t),\ldots,a(t+p)\).  Its zero-anticipation subclass is
the automaton-realizable class printed with Cyrillic Л in 1961 and Latin
\(A\) in 1962.  The reader explicitly declares the normalization and explains
why the alphabet variable is not the standing of the hyphenated class name.
The four notions therefore remain distinct.

Expanded pp. 111--112 also support the negative primitive-recursive boundary.
A constant operator defined by a primitive-recursive stream is finite exactly
in the ultimately-periodic case, whose recognition is undecidable at that
scheme strength; effective extraction of canonical finite-state equations
would also decide a known undecidable zero-identity question.  The bounded
summary at manuscript lines 573--580 is consequently exact.

### 3. All-prefix portions, empty portions, homogeneity, and the graph bound

The reader definition at `n-c-014.tex:582--605` is genuinely an all-prefix
definition:
\[
 M_u=\{Z:uZ\in M\}
\]
is formed for every finite word \(u\), so an incompatible prefix contributes
the portion \(\varnothing\).  For tuples, the prefix and tail operations are
coordinatewise.  A basis contains the original set and all distinct portions;
the internal transition appends one current coordinate tuple.  These objects
are stream-set data, not invented automaton types.

I independently derived the corrected graph bound.  Let \(G_T\) be the graph
of a zero-anticipation operator presented with \(k\) memory states, and let
\((u,v)\) be an equal-length paired prefix.

1. If \(v\ne T_{|u|}(u)\), then \((G_T)_{(u,v)}=\varnothing\).
2. If \(v=T_{|u|}(u)\), the causal finite-state presentation has a definite
   reachable state after \(u\).  The remaining graph is the graph of the same
   presentation started in that state.  Hence all compatible prefixes yield
   at most \(k\) distinct nonempty portions.
3. Every incompatible prefix yields the same one empty portion.

Thus the all-prefix degree is at most \(k+1\), not necessarily at most \(k\).
The extra one is necessary: for the weight-one constant-zero operator,
\[
 G_0=\{(X,0^\omega):X\in 2^\omega\},
\]
every compatible paired prefix has residual \(G_0\), while a paired prefix
whose output coordinate contains a \(1\) has residual \(\varnothing\).
Its all-prefix degree is exactly two.  The correction at manuscript
lines 597--605, source-note lines 203--213, and compact-record line 652 is
therefore exact, minimal, explicitly handbook-owned, and confined to the
numerical bound; zero anticipation still makes the graph closed.

The correction creates no collateral inconsistency.  The empty portion is
absorbing under the internal transition and is not a memory state for a total
operator.  In the later finite-realization construction only nonempty graph
portions supply states, so the claimed weight \(\le\) all-prefix homogeneity
degree remains true (indeed it can be loose by one).  In the general-solution
construction the empty portion is deleted before the stable family is made
into memory states, so that weight bound also remains true.  No later argument
reverses either inequality or infers a \(k\)-state presentation merely from the
corrected \(k+1\) upper bound.

The other edge cases also check.  For a singleton \(\{X\}\), the compatible
portions are the singleton tails of \(X\), together with \(\varnothing\) from
incompatible prefixes.  There are finitely many precisely when the shift orbit
of \(X\) is finite, equivalently when \(X\) is ultimately periodic.  The
uncountability argument uses prefix-invariant tail classes whose every portion
is the same nonempty set, so one-homogeneous nondefinable sets remain valid
even under the all-prefix convention.

### 4. Definability, recurrence, topology, and effectiveness

The claims at `n-c-014.tex:610--646` agree with announcement pp. 327--328 and
expanded pp. 116--119.

For an \(\mathcal I\)-formula in normal form, fixing a finite prefix evaluates
each lower component to one of finitely many Boolean functions of its bounded
window; the upper components retain only one of finitely many normalized
forms.  Therefore only finitely many semantic portions occur.  Appending the
next coordinate tuple transforms one normalized residual formula into another,
so the internal transition table is obtained effectively without deciding
whether a residual is empty.

Conversely, from a finite basis one introduces bound one-hot state predicates
\(q_1,\ldots,q_k\), a bound choice predicate \(U\), a quantifier-free local
current/next matrix, and the literal initial valuation selecting the original
basis member.  The displayed initial state is essential: omitting it would
define a union over possible starting portions rather than the named set.
The resulting witness space is a closed subset of a finite product of Cantor
spaces; compactness makes its projection closed.  Its finite local state data
also give only finitely many portions.  Conversely the covering construction
for a homogeneous set has image equal to its closure, so closedness makes that
image the original set.  This verifies both directions of the recurrence
characterization and the necessity of the topological hypothesis.

Boolean operations and existential predicate projection then give exactly the
least class generated by the closed homogeneous sets under complement, finite
union, and projection.  The homogeneous-but-nondefinable examples show that
homogeneity alone is not a converse, and the announcement's Borel/projective
question remains open rather than being silently answered.

The effectiveness boundary is also correct.  Formula residuals and their
internal transitions are syntactic and unconditional.  Choosing an external
output/choice requires knowing which relevant residual formula is nonempty,
equivalently a truth/nonemptiness decision.  Hence the general construction is
only a conditional \(\mathcal I\)-algorithm.  Putnam's cited decision procedure
removes that condition for the displayed existential-predicate recurrent
fragment, not for every source-time construction without qualification.

### 5. Continuous total operators and the strictly weaker memory theorem

At `n-c-014.tex:648--670`, the graph-versus-solution distinction and the two
operator theorems agree with announcement p. 328 and expanded pp. 119--120.

If an \(\mathcal I\)-formula defines exactly the graph of a continuous total
operator, the graph is homogeneous and closed.  Each nonempty graph portion is
the graph of a continuous function on a compact domain.  For its first output
coordinate, continuity and compactness give a finite input-prefix bound.  The
finite residual basis has only finitely many nonempty members, so the maximum
of those local bounds is one global anticipation bound.  The current residual
is a finite memory state, and the next paired letter determines the next
residual.  This proves finite-operator standing and gives weight no greater
than the graph's homogeneity degree.  It also shows why compact uniformity and
finite homogeneity are both used: compact continuity alone gives bounds for
successive output prefixes, not by itself one time-translation-invariant
lookahead constant.

Without continuity the same finite residual basis still gives finite memory:
in a residual state, the whole future input suffix determines the unique first
output and next residual.  Nothing makes that dependence finite-window.  Thus
expanded \(\S4\), Theorem 2, concludes only finite memory and the same safe
weight inequality.  It does not establish a finite operator, bounded
anticipation, or \(A\)-operator standing.

For a relation, a solution needs only graph containment.  Announcement
Theorem \(4'\) starts from a closed homogeneous relation, not an already
identified operator graph.  A continuous solution can be replaced by a finite
solution of bounded weight; a zero-anticipation solution can be replaced by a
Л-solution (an \(A\)-solution in the expansion's normalized terminology).  The
separate open-relation statement carries no weight bound.  The reader neither
conflates these hypotheses nor promotes existence into graph equality.

### 6. General solutions, stable deletion, parameter standing, and fixed lookahead

The two clauses at `n-c-014.tex:672--686` exactly express generality.  A
parameterized \(A\)-operator must obtain every \(A\)-solution from an
\(A\)-operator parameter substitution (completeness), and every allowed
substitution must yield a solution (soundness).  Replacing the class name in
both clauses, not just in the conclusion, gives general zero-anticipation
standing.

I reconstructed the deletion proof behind manuscript lines 688--699 from
expanded pp. 121--124.  Write the finite basis of relation portions as states
\(i\), with transition \(\psi(i,\sigma\tau)\) after current input bit \(\sigma\)
and output bit \(\tau\).  First remove empty basis members.  Then repeatedly
remove any state \(i\) for which some input \(\sigma\) has neither output
choice \(\tau\in\{0,1\}\) leading to a surviving state.  The process terminates
on the finite basis and leaves the greatest stable family.

If the initial relation state is deleted, a zero-anticipation solution cannot
exist: the nonempty residual graph portions generated by any such solution
would themselves form a stable surviving subsystem containing the initial
state, a contradiction.  If the initial state survives, define the output
selector in state \(i\) on input \(\sigma\) to use a free parameter bit when
both output children survive and to force the unique surviving output when
only one does.  The selected output and \(\psi\) determine the next state.

Every parameter stream then keeps every generated finite paired prefix in a
nonempty relation portion.  Because the relation is closed, the resulting
infinite pair lies in it; this is the soundness clause.  Conversely, given any
zero-anticipation solution \(T_0\), choose the parameter at time \(t\) to
select \(T_0(X)(t)\) in the current relation state.  That state depends only on
the input/output prefix, so the induced parameter operator has zero
anticipation.  If \(T_0\) is an \(A\)-operator, its finite state together with
the finite relation state makes the parameter operator an \(A\)-operator.
This proves both completeness clauses simultaneously.  The surviving family
has no more members than the relation's all-prefix homogeneity degree, so the
general \(A\)-solution has the claimed weight bound; the deleted empty portion
cannot add a state.  Testing initial emptiness and subsequent empty children
is exactly why the construction for an arbitrary closed \(\mathcal I\)-formula
remains conditional.

For expanded Theorem \(3'\), fix one \(p\ge0\).  Prefixing the first \(p\)
output positions by fixed symbols and delaying the remaining output converts
operators of anticipation at most \(p\) bijectively into zero-anticipation
operators for the shifted formula.  Applying the preceding construction and
undoing the shift preserves the fixed bound and the weight inequality.  The
quantifier order is therefore
\[
 (\forall p\ge0)\;[\text{one alternative and one general solution for that
 fixed class }p],
\]
not one parameterization of the union over unbounded lookahead classes.  The
reader at lines 699--704 and source note at lines 332--339 preserve this exact
scope.

### 7. Explicit definitions and canonical synthesis

The explicit definition at `n-c-014.tex:708--721` has output standing, not
general relation standing.  Its graph is \(\mathcal I\)-definable, so the
unconditional operator has finite memory.  Semantic fictitious occurrence
outside \([1,t+p]\) is necessary and sufficient for anticipation at most
\(p\); the case \([1,t]\) is exactly zero anticipation and hence \(A\)-operator
standing once finite memory is included.

For a zero-shift upper \(t\)-formula, fixing the first input column computes
the first output and produces a shifted residual formula.  Repeating this for
all input columns yields only finitely many normalized residuals by the normal
form.  They are the states, and the computed output and next-residual maps are
the canonical tables.  Expanded pp. 126--127 visibly carry the two-formula
worked example through both tables; the reader gives its exact role and does
not claim that the pages prove an unrelated general theorem.

### 8. Finite-word actions, both directions of Theorem 2, and the empty language

The maps at `n-c-014.tex:723--734` are well typed.  For \(u\in A^t\), any two
infinite extensions agree through \(t\); zero anticipation therefore makes
\(T_t(u)\) extension-independent.  Applying the same observation at every
\(s\le t\) gives the displayed prefix compatibility.  The range of the stream
operator is consequently not confused with a language of finite words.

The automaton-enumerability and automaton-decidability definitions at
manuscript lines 736--748 agree with expanded p. 127.  I checked both proof
directions.

For enumeration \(\Rightarrow\) decision, an explicitly definable enumerator
can be tested at length \(t\) by existentially quantifying an input stream and
requiring equality of the first \(t\) output letters to the presented word.
The resulting explicit formula is prefix-controlled, so its synthesized
terminal output is one exactly on the lengthwise range.

For the printed converse, suppose \(L\) is nonempty, prefix-closed, properly
extendible, and decided by a zero-anticipation recognizer.  On an accepted
input prefix, output that prefix.  Once the input has left \(L\), retain its
longest accepted prefix and output the lexicographically first length-\(t\)
member of \(L\) extending it.  Nonemptiness gives the initial seed; prefix
closure and proper extendibility give a member at every positive length.  The
lexicographically first length-\(t+1\) choice extends the first length-\(t\)
choice, because every length-\(t\) member itself has a longer extension.  The
maps are therefore prefix-compatible, total, and have lengthwise range exactly
\(L\).

The source's printed hypotheses omit nonemptiness.  The empty language is
decided by the one-state constant-zero recognizer and satisfies prefix closure
and proper extendibility vacuously, but no total map from the nonempty binary
input alphabet has empty length-\(t\) range.  Adding \(L\ne\varnothing\) is
both necessary and sufficient, and it supplies exactly the missing first word
used on expanded p. 128.  The correction at manuscript lines 750--759 is
therefore exact and explicitly handbook-owned.

### 9. \(\mathcal I'\), special beginnings, and the modern theorem boundary

At `n-c-014.tex:761--779`, \(\mathcal I'\) restricts every predicate variable
to an eventually-zero predicate.  A special beginning at length \(t\) includes
the tail condition \((\forall\tau>t)X(\tau)=0\); it is not an arbitrary prefix.
For an arbitrary \(\mathcal I\)-formula, existentially quantifying an
eventually-zero completion that agrees with the presented prefix gives a
prefix-controlled explicit definition and hence existence of an \(A\)-operator
recognizer.  For an \(\mathcal I'\)-formula, the source's cited decision result
makes the construction effective.  Expanded p. 130 explicitly attributes
that effective case to Büchi.  Existence and effective synthesis are not
collapsed.

The shared theorem at `logic-in-computer-science.tex:811--825` labels the
regular/MSO equivalence as a modern formulation and immediately distinguishes
the acquired Büchi report precursor, Elgot's finite-set design development,
and Trakhtenbrot's arbitrary-predicate/operator theory.  The source-navigation
paragraph at lines 2341--2347 keeps the announcement, expansion, Büchi report,
registered Büchi article, Elgot article/errata, Thomas survey, and Rabin tree
source distinct.  The Thomas paragraph at `n-c-014.tex:789--807` gives the
standard two directions--state-set encoding of accepting runs, and atomic
automata plus Boolean closure and projection--as Thomas's later synthesis.  It
does not launder that sentence into either Russian source or use modern
regular/MSO folklore as proof of Trakhtenbrot's broader operator theorems.

## Terminology, nonconflation, and correction audit

The technical names first used in the Trakhtenbrot block satisfy the supplied
AGENTS rule.

- `fictitious outside` is semantically eliminable as invariance under changes
  outside an interval; lower and upper formulae differ by prefix/tail standing
  and are used in normal form and synthesis.
- anticipation, finite memory, finite operator, weight, and \(A\)-operator are
  separately defined operator properties/data, their nonimplications are
  explained, and every distinction is used later.
- portion, homogeneous degree, basis, and internal transition are defined as
  stream-set properties/data and are used in every finite-realization proof.
- solution is graph containment; exact graph definition is separately stated.
- general \(A\)-solution and general zero-anticipation solution have explicit
  all-and-only parameter clauses and parameter-class standing.
- explicit definition, automaton-enumerable, automaton-decidable, and special
  beginning each receive an exact definition before theorem use.

No named hypothetical object is introduced without necessity, standing,
nonredundancy, and later use.  In particular, the manuscript does not invent a
new automaton species for portions, residuals, stability, or the repaired
empty case.

The 1961/1962 boundaries are also clean.  The announcement controls its
Theorems 1--5 and \(4'\) on pp. 326--329.  The expansion controls its
section-specific results, including the strictly weaker discontinuous
Theorem 2, the fixed-\(p\) Theorem \(3'\), explicit synthesis, the worked
example, the word theorem, and \(\mathcal I'\).  The different official English
title renderings and the Л/\(A\) letter change are declared rather than silently
normalized.  `handbook.bib:5991--6013`, the source note, the compact record,
and the reader are mutually consistent on these identities.

## Mandate coverage map

| Point | Status | Evidence and result |
|---|---|---|
| M01 | checked-clean | Seven independently recomputed hashes above; every value exact. |
| M02 | checked-clean | All 4+29 images inspected at original detail; physical/printed maps 1→326 through 4→329 and 01→103 through 29→131 confirmed. |
| M05 | checked-clean | `n-c-014.tex:487--510`, expanded pp. 104--105 and 130--131: syntax, domains, primitive successor, eliminable conveniences, \(\mathcal I\)/\(\mathcal I'\) standing. |
| M06 | checked-clean | `n-c-014.tex:512--525`, announcement pp. 326--327, expanded pp. 105--109: semantic fictitious occurrence, unequal prefix/tail dependence, overlap case split, effective normal form. |
| M07 | checked-clean | `n-c-014.tex:527--571`, expanded pp. 109--112: total map, anticipation/prefix equivalence, whole-suffix finite memory, weight, finite window, \(A\)-standing, all nonimplications. |
| M08 | checked-clean | `n-c-014.tex:551--554,573--580`, expanded pp. 111--112: one-state nonrecursive future-dependent operator and primitive-recursive recognition/synthesis boundary. |
| M09 | checked-clean | `n-c-014.tex:582--608`, expanded pp. 113--116: coordinatewise portions, degree, basis, internal transition, corrected \(k+1\) graph bound, singleton and uncountability examples. |
| M10 | checked-clean | `n-c-014.tex:610--613`, expanded pp. 116--118: finite normalized residual family and effective internal transition independently derived. |
| M11 | checked-clean | `n-c-014.tex:613--637`, announcement pp. 327--328, expanded pp. 116--119: closed converse, literal initial basis state, recurrent form, compact projection, full closure characterization. |
| M12 | checked-clean | `n-c-014.tex:639--646`, expanded p. 119: internal transition unconditional; external choice conditional on nonemptiness; Putnam restricted to recurrent form. |
| M13 | checked-clean | `n-c-014.tex:648--656`, announcement p. 328, expanded pp. 119--120: compact residual uniformity, one global lookahead, finite memory, safe weight bound. |
| M14 | checked-clean | `n-c-014.tex:656--658`, expanded p. 120: discontinuous theorem gives finite memory only; no bounded anticipation or finite-operator collapse. |
| M15 | checked-clean | `n-c-014.tex:660--670`, announcement p. 328: graph equality versus solution containment; every closed/open clause and weight qualification of Theorem \(4'\). |
| M16 | checked-clean | `n-c-014.tex:672--686`, announcement p. 328 and expanded pp. 120--121: both all-and-only quantifiers, parameter streams, and class replacement. |
| M17 | checked-clean | `n-c-014.tex:688--699`, announcement pp. 328--329, expanded pp. 121--124: no-solution contradiction, greatest stable surviving family, selector parameters, soundness, completeness, closedness, weight, conditional pruning. |
| M18 | checked-clean | `n-c-014.tex:699--704`, expanded p. 124: delay/shift reduction separately for each fixed \(p\); no union over unbounded lookahead. |
| M19 | checked-clean | `n-c-014.tex:708--721`, expanded pp. 124--127: explicit standing, semantic criteria, residual termination, canonical tables, exact two-formula example role. |
| M20 | checked-clean | `n-c-014.tex:723--759`, expanded pp. 127--129: typed word maps, both proof directions, prefix compatibility, exact nonempty/prefix-closed/properly-extendible correction. |
| M21 | checked-clean | `n-c-014.tex:761--770`, expanded pp. 130--131: eventually-zero domain, non-arbitrary special beginnings, existence/effectivity split, Büchi attribution. |
| M22 | checked-clean | Announcement pp. 326--329 versus expanded pp. 103--131 and `n-c-014.tex:487--787`: numbering, detail, letter, title, and strength kept source-specific. |
| M23 | checked-clean | `logic-in-computer-science.tex:811--825,2341--2347` and `n-c-014.tex:772--807`: modern theorem and Thomas proof route expressly nonliteral and non-substitutive. |
| M26 | checked-clean | Terminology audit above; every new distinction is defined with standing, nonredundancy, and actual use. |
| M27 | checked-clean | No hidden continuity/closedness, finite-memory/lookahead collapse, source laundering, translation inflation, priority inflation, or completion inflation found. |
| M28 | checked-clean | Topic-only scope and rights/translation boundary preserved; no forbidden test, script, build, or handbook-PDF evidence used or claimed. |

## Finding register

No findings.

VERDICT: ACCEPT
