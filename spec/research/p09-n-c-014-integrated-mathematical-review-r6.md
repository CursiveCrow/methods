# N-c-014 integrated mathematical review — blind Round 6

## Verdict

VERDICT: REJECT

The current LaTeX has two mathematical-definedness must-fixes. The first leaves
the finite-tree run predicate undefined on part of its stated input domain. The
second leaves the Trakhtenbrot positive-word converse with an ambiguous—and,
under the ordinary finite-prefix convention used earlier in the same
presentation, inconsistent—prefix hypothesis. Both are local repairs; no
other mathematical must-fix was found within the permitted evidence.

## Material read

I read the following actual text directly:

- handbook/parts/p09/presentations/n-c-014.tex, lines 1--1869, from line 1
  through EOF;
- handbook/parts/p09/logic-in-computer-science.tex, lines 836--944;
- spec/research/p09-buchi-1960-source-note.md, lines 1--367;
- spec/research/p09-elgot-1961-source-note.md, lines 1--423;
- spec/research/p09-trakhtenbrot-1961-source-note.md, lines 1--583;
- spec/research/p09-rabin-1969-source-note.md, lines 1--665;
- spec/research/p09-thomas-1996-report-source-note.md, lines 1--353;
- the compact N-c-014 record in
  spec/research/p09-source-presentations-lot2-3.md, lines 681--745; and
- the relevant entries in handbook/bib/handbook.bib: Buchi1959WeakReport,
  Buchi1960, BruyereEtAl1994, Elgot1959Report, Elgot1961,
  Elgot1962Errata, Trakhtenbrot1961, Trakhtenbrot1962Expanded,
  Rabin1969, Meyer1975Complexity, McNaughton1966, and
  Thomas1996Report.

I did not read an earlier N-c-014 review, admission record, board record, or
history file. I did not open, inspect, render, build, or cite a manuscript PDF,
PNG, page image, or other render. I did not run a test, harness, automated
checker, repository script, hash computation, TeX command, PDF build, or other
manuscript build. I created no admission record and changed no manuscript,
host, ledger, bibliography, source note, or prior report.

## Must-fix findings

### M1. The finite-tree run predicate is not defined on every stated finite-valued-tree input

Current lines 1233--1241 deliberately distinguish a general finite tree
\(E\subseteq T\), which is merely finite, rooted, and predecessor-closed, from
a *frontiered* one, in which every node outside
\(\operatorname{Ft}(E)\) has both children in \(E\). Lines 1464--1467 repeat
that predecessor closure alone permits a node with exactly one child.

Despite that distinction, current lines 1478--1488 define a run "on a finite
valued tree" as a map \(r:E\to S\cup\{f\}\) and require, for every
\(x\in E\setminus\operatorname{Ft}(E)\),

\[
 (r(x0),r(x1))\in M(r(x),v(x)).
\]

If \(E\) has exactly one child of \(x\), then
\(x\notin\operatorname{Ft}(E)\) but one of \(x0,x1\) is outside the domain
\(E\) of \(r\). The corresponding term \(r(xd)\) is therefore undefined.
This is not merely a rejecting transition: as written, the run condition is
not a proposition on every object that the preceding definition calls a finite
valued tree. Current lines 1493--1496 correctly discuss a different,
well-defined edge case—a *frontiered* tree with one frontier child and one
internal child, for which the pair is mixed and the printed transition codomain
supplies no move—but that does not totalize evaluation at an absent child of a
nonfrontiered tree.

**Required repair (current lines 1468--1500, with the operative defect at
1478--1488):** explicitly restrict the finite-tree automaton's input, run, and
acceptance clauses to a frontiered finite tree \(E\). For example, introduce
the valuation and run with "Let \(E\) be frontiered" or say "A run on a
frontiered finite valued tree \((v,E)\) is ...". The lift statement should use
the same domain when it refers to an automaton-definable collection. This is
the minimal repair consistent with the already stated source architecture and
with the separate frontiered finite table-runs in lines 1572--1587; inventing a
value for a missing child would instead change the finite-tree model.

### M2. “Prefix closure” is not typed relative to the positive-word universe

Current lines 942--955 define Trakhtenbrot's language only on positive lengths:
\(L\subseteq\bigcup_{t\geq1}B^t=B^+\). Lines 956--965 then state the
printed converse and its handbook correction using unqualified “prefix
closure” and “proper extendibility.” Under the ordinary convention that every
finite prefix is included, the empty word is a prefix of every positive-length
word. That is also the convention made explicit for Elgot's
\((A\times B)^*\)-behaviors at lines 368--380, whose prefix-closed behavior
contains the empty paired word. Consequently a nonempty \(L\subseteq B^+\)
cannot be prefix-closed in that sense. Adding \(L\neq\varnothing\) at line 961
then makes the displayed package of hypotheses inconsistent rather than
repairing the source's empty-language counterexample.

The intended proof described in lines 961--963 needs closure only under
*nonempty* prefixes: from one positive-length member it obtains a word of
length one, and proper extension plus nonempty-prefix closure supplies every
intermediate positive length. That condition is mathematically sound, but it
is not what the unqualified phrase currently fixes, especially after the
earlier all-finite-prefix definition.

**Required repair (current lines 942--965):** state the conditions directly in
the positive-word universe, without introducing an unexplained replacement
name. The corrected converse should say that an automaton-decidable
\(L\subseteq B^+\) is automaton-enumerable when

1. \(L\neq\varnothing\);
2. every nonempty prefix of every word in \(L\) also belongs to \(L\); and
3. every word in \(L\) is a strict prefix of some longer word in \(L\).

The subsequent seed argument should use those same quantified conditions.
This both discharges the empty-word case and keeps the positive-length source
domain distinct from Elgot's star-language prefix convention.

## Audit of the remaining mathematics

Subject to the two must-fixes above, the other constructions inspected are
mathematically coherent at their expressly bounded source strengths:

- **Büchi.** The standings of formula data, special finite predicates, runs,
  outputs, and behaviors are separated. The handbook-owned analysis repair is
  typed over finite witnesses and handles the last-point case, including
  \(h=0\): downward closure makes \(j\) a nonempty finite initial segment, the
  guarded transition follows the real run only while needed, the input is
  false from the boundary onward, and special-output invariance propagates the
  boundary truth value. The terminal-marker encoding treats the empty word
  separately. The false-tail guard in the sentence decision and the later
  correction of the unary-powers claim are not conflated with the sound
  finite-word correspondence.

- **Elgot.** The acceptor, transducer, formula, assignment, column word, run,
  and language types remain distinct. Empty admissible words and terminal-zero
  truncation are accounted for. The descending \(M_h\) construction is a
  finite, monotone greatest-survivor computation; its two initial tests exactly
  handle failure of the empty prefix or of first-letter extendibility. The
  erratum's finite union is not collapsed to one component. For arity one,
  \(\widehat R_j=R_j\times R_j\) and
  \(\widehat E_j=(E_j\cap R_j)\times R_j\) preserve both the unary pointwise
  constraint and the first-letter condition before tagging, so the overlap
  argument is defined for every positive window arity.

- **Trakhtenbrot apart from M2.** Anticipation, broad whole-future finite
  memory, finite operators, and the zero-anticipation automaton-realizable class
  have separate domains. Tuple portions are coordinatewise, residual stream
  operators are not identified with memory states, and the supplied two-state
  counterexample really has the claimed outputs and distinct graph portions.
  The closed-homogeneous construction splits the nonempty covering case from
  the empty contradictory-initial-state case. Solution, general solution, and
  fixed-\(p\) solution claims retain their different quantifier strengths and
  the source's conditional-effectivity boundary.

- **Rabin apart from M1.** Ordinary acceptance has one global run followed by
  all paths; the dual construction reverses those quantifiers and correctly
  permits no-run vacuity. The deterministic path-word product has the right
  state type and update: its first coordinate is the unique Muller word run on
  the second-coordinate state stream, and projection of the infinitely
  recurring product states gives the word condition because both factors are
  finite. The empty pair sequence is exactly represented by
  \(((S,S))\). The restricted-table root exception and the separate
  frontiered finite table-run used in the emptiness base are explicitly typed;
  allowing \(H=\varnothing\) and \(m=0\) closes the two vacuous branches without
  turning full \(S2S\) into weak logic.

- **Thomas and the host theorem.** Finite-word runs have \(n+1\) states and
  the empty-word formula guard is identified. The strict-chain empty endpoint
  is given a false path condition. The fresh rejecting state lies outside all
  chain sets; every added transition creates a path eventually constant at
  that state, so completion is language-preserving and makes all game moves
  live. The game positions, direction-stream paths, memoryless strategies,
  local instruction functions, and regular-tree generators have distinct
  types. The host's finite-word theorem is explicitly a modern formulation,
  and the successor/order equivalence is confined to finite successor chains.

The local technical-name rule is otherwise respected in the audited
mathematical constructions: source-specific names such as special output,
strong extendibility, portion, frontiered, finite table-run, strict chain,
order-vector with hit, and regular tree are accompanied by a definition,
standing, distinction, and later proof use. M1 is a domain failure after a
properly introduced name; M2 should be repaired by stating the quantified
property directly, which avoids creating another hypothetical term.

## Disposition

No acceptance or admission record may be created from this snapshot. Once the
two specified passages are repaired, a fresh review must check the changed
LaTeX rather than carrying this verdict forward.

REGISTER STATUS: OPEN
