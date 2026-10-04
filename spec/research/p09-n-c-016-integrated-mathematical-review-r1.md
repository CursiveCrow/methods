# N-c-016 integrated mathematical and definedness review, Round 1

VERDICT: REJECT

## Scope and decision rule

This is a fresh, blind, text-only mathematical and definedness review of all
five presentations integrated in
handbook/parts/p09/presentations/n-c-016.tex, lines 1--1856, together with the
actual host bridge and its named Part VIII prerequisite definitions. The
review distinguishes:

- a defect printed by a historical source and accurately reported as such;
- a reader-supplied completion or proof, which must be correct and labelled;
- a source claim whose proof is omitted or delegated; and
- a false, ill-typed, or undefined assertion made by the integrated reader or
  host itself.

The first three statuses can be acceptable at an expressly bounded source
strength. The fourth is a must-fix. I found three line-specific must-fixes.

## Must-fix findings

### 1. \(P\) changes from a process to a state formula without a binding

**Current lines:** handbook/parts/p09/presentations/n-c-016.tex 597--612,
with the ill-typed occurrence at line 611.

Lines 597--608 bind \(P\) as a process: \(A(P)\) is its finite action set, and
\(\operatorname{enable}P\) abbreviates the disjunction of enabledness
predicates for those actions. Lines 609--612 then call
\(\operatorname{ALL}(P)\) an invariant schema:

\[
  \operatorname{Init}\Rightarrow\operatorname{ALL}(P).
\]

But \(\operatorname{ALL}\) takes a state formula by the grammar and typing at
lines 525--544, not a process. The intended second use of \(P\) is evidently a
program/state predicate, as the concrete instances at lines 616--625 confirm,
but that different standing is never bound. Under the only local binding, the
display applies a formula operator to a process.

**Minimal repair:** bind a fresh state-formula variable at lines 609--612 and
use it in the schema, for example: “For every state formula \(\varphi\) of the
source's invariant form, the schema is
\(\operatorname{Init}\Rightarrow\operatorname{ALL}(\varphi)\).” Keep \(P\)
reserved for the process in \(A(P)\). This also restores the AGENTS standing
requirement at the point of use.

### 2. The claimed CTL form is not equivalent to its CTL* target

**Current lines:** handbook/parts/p09/presentations/n-c-016.tex 1224--1230,
especially the display at lines 1225--1227 and its claimed target at line
1228.

The reader says that

\[
 \neg E[\neg P\ U\ (P\land EGP)]
\]

is a CTL form of \(A(FP\lor G\neg P)\). It is not.

Take the finite total transition structure with states \(s_0,s_1\), edges
\(s_0Rs_1\) and \(s_1Rs_1\), with \(P\) false at \(s_0\) and true at \(s_1\).
The sole path from \(s_0\) satisfies \(FP\), so

\[
 s_0\models A(FP\lor G\neg P).
\]

On the other hand, \(s_1\models P\land EGP\), and the path from \(s_0\) has
\(\neg P\) before reaching \(s_1\). Therefore

\[
 s_0\models E[\neg P\ U\ (P\land EGP)],
\]

so the displayed negation is false at \(s_0\). The formulas disagree on a
two-state finite total structure.

Indeed, under the typed CTL* definitions already supplied at lines 903--975,
\(G\neg P=\neg FP\) on a path, so \(FP\lor G\neg P\) is pathwise valid and
its universal closure is equivalent simply to \(\mathsf{true}\). The displayed
nontrivial CTL formula cannot be its equivalent.

**Minimal repair:** do not retain the equivalence claim as reader-endorsed
mathematics. Either identify and state the actual source target for the display
and verify that equivalence, or record this as an additional source-printed
defect. If the target remains exactly \(A(FP\lor G\neg P)\), replace the
alleged CTL form by \(\mathsf{true}\) or another explicitly proved CTL
tautology.

### 3. The host uses \(\top\) in \(\mathsf{EF}/\mathsf{AF}\) without a labelling clause

**Current lines:** handbook/parts/p09/logic-in-computer-science.tex 969--994,
with the use at lines 989--990 and the incomplete case display at lines
971--987. The prerequisite grammar is
handbook/parts/p08/temporal-epistemic-supplement.tex 58--64.

The host method says that \(\mathsf{EF}B\) and \(\mathsf{AF}B\) abbreviate
until with left operand \(\top\), but the bottom-up definition has no
\(L(\top)=S\) branch. The reused Part VIII CTL grammar says only that the state
formulas are the Boolean closure of the atoms and the temporal forms; it does
not supply a primitive truth-constant branch for this algorithm. Thus an
expanded \(\mathsf{EF}\) or \(\mathsf{AF}\) subformula contains an operand
whose labelling value is not assigned by the stated method.

The omission is especially visible against the integrated Baier--Katoen
source clause at presentation lines 1553--1555:
\(\operatorname{Sat}(true)=S\).

**Minimal repair:** add \(L(\top)=S\) to the host's case display before using
\(\top\) in the \(\mathsf{EF}/\mathsf{AF}\) abbreviations. If \(\bot\) is
also admitted as a primitive input constant, add \(L(\bot)=\varnothing\);
that second clause is not required merely to repair the current use.

## Mathematical audit apart from the three must-fixes

### Clarke--Emerson presentation, lines 3--463

- Lines 38--56 type the countable state set, process-indexed transition
  relations, valuation, total union relation, infinite paths, and computation
  tree coherently. Finiteness is imposed later for model checking and is not
  silently built into the source semantics.
- The grammar and satisfaction clauses at lines 58--95 keep formulas at state
  type, retain process-indexed \(EX_j\), quantify both until clauses over paths
  from the current state, permit the current state as the right-endpoint
  witness, and require a witness for strong until.
- The derived forms at lines 97--120 are well typed. In particular,
  \(AX_i:=\neg EX_i\neg\) may be vacuously true when process \(i\) is disabled,
  while unindexed \(EX\) ranges over the total union of process moves. The
  mutual-exclusion requirements later use that distinction correctly.
- The reconstructed universal and existential until chains at lines 133--164
  are monotone and correct on a finite total structure. Starting at the
  right-operand set, universal growth requires the left operand and all
  successors, while existential growth requires the left operand and one
  successor. Stabilization by \(|S|\) rounds is sufficient. The text correctly
  separates the paper's representation-sensitive
  \(\operatorname{length}(f_0)|S|^2\) bound from the later edge-sensitive
  implementation bound.
- Lines 166--179 properly identify the missing \(f_1\land\) in the source's
  printed universal-until approximation, show the internally supported guarded
  equation, and label the repair.
- The worked \(AFb\land EGa\) calculation, the finite SCC/self-loop
  characterization of infinitely-often reachability, and the Hamiltonian-path
  reduction at lines 181--220 have the stated directions and strengths. The
  latter proves only NP-hardness for the source's arbitrary-linear-path
  extension.
- The tableau material at lines 222--303 remains explicitly an abridged
  outline. No omitted soundness-and-completeness proof is promoted to a printed
  theorem.
- The nine mutual-exclusion groups at lines 305--375 are well typed. The
  enabledness conjunct in group 6 prevents vacuous \(AX_i\), and group 8
  intentionally permits the vacuity appropriate to a disabled other process.
- Model fragment, \(\mathsf{TURN}\), the global flowgraph, and factorization at
  lines 377--451 have stated standings and actual uses. The conclusion
  accurately separates the model checker, the proved graph propositions, and
  the abridged tableau/synthesis status.

### Queille--Sifakis presentation, lines 465--787

- The IPN at lines 477--503 is defined as a program model with both Petri-net
  control and guarded data updates; diagnostics, translation correctness,
  counterexamples, and synthesis are not invented.
- The alternating-bit transition model and its external non-loss assumption at
  lines 505--523 are kept separate. Repeated loss remains possible in the
  displayed program because the logic has no fairness premise.
- Lines 525--585 correctly distinguish the source's unary state-operator
  language from later full CTL. The reader explicitly supplies the missing
  start and adjacency clauses for maximal finite/infinite executions and
  records the source's missing Boolean interpretation clauses.
- The fictitious-\(\omega\) and indexed-reachability convention makes
  \(\operatorname{POT}\) and \(\operatorname{INEV}\) quantify only over
  defined positions of maximal executions and makes the universal implications
  for \(\operatorname{ALL}\) and \(\operatorname{SOME}\) vacuous past a finite
  sink. All four operators include the current state.
- Apart from finding 1, the program predicates, liveness/deadlock distinction,
  response targets, and repaired \(\operatorname{receiveack}\) identifier at
  lines 587--688 preserve the source's distinctions: enabledness is not
  execution, and no hidden fairness is added.
- Lines 690--738 correctly type predicate transformers as maps on subsets of
  \(Q\), define identity, composition, pointwise union/intersection, the
  source's star and literal superscript-\(x\) iterations, existential
  predecessor and its Boolean dual. The four identities retain the printed
  image-finiteness hypothesis. The existential predecessor factor in the
  \(\operatorname{INEV}\) transformer excludes a non-\(f\) sink.
- The proposition proofs remain delegated to Sifakis 1979. The analyzer's
  reduction, sole worked predecessor calculation, user-selected iteration cap,
  possible no-answer outcome, and absence of an asymptotic theorem are stated
  at the source's strength.

### Emerson--Halpern presentation, lines 789--1350

- The Lamport structure at lines 800--815 admits nonempty finite and infinite
  paths and defines suffix iteration, including the fixed length-zero suffix.
  The two old readings at lines 817--854 correctly distinguish a state claim
  over all paths from a one-path claim.
- Whole-model strong equivalence, suffix/fusion/limit closure,
  \(R\)-generability, and state completeness at lines 856--901 are typed as
  metalinguistic properties of structures and path families. The source's
  “states from \(X\)” typo is explicitly identified.
- The mutually generated CTL* grammar and semantics at lines 903--975 preserve
  the state/path distinction. Only \(A/E\) return a path formula to state type;
  \(F\) and strong until include the current position; next is false at the end
  of a finite path; and \(A/E\) alone restrict quantified paths to \(X\).
- The associated-language constructor \(B(L)\), pointwise equivalence, closure
  hypotheses, and expressiveness diagram at lines 996--1069 remain
  metalinguistic. The path-deletion proof for Theorem 3 is correct.
- Lines 1071--1212 distinguish printed theorem statements, source-supported
  repairs, complete local proof portions, cited equalities, and reader-left
  inductions. The self-defeating printed targets of Theorems 5--6 and the bad
  theorem cross-references are not silently treated as correct.
- The fairness formula is a specification, not a semantic fairness condition.
  The PL translation is typed and its structural-induction proof boundary is
  stated.
- Lines 1255--1325 accurately preserve the literal MPL \(U\) and \(X\)
  defects: the printed clauses respectively require the left operand at the
  until endpoint and permit next at the current stage. Concrete countermodels
  are given, and Theorem 10 is not claimed to follow from those displays.
- The terminal-server formula and application conclusion at lines 1327--1350
  correctly use existential paths to require alternative behaviors and do not
  invent a model-checking or synthesis theorem.
- The only reader-level mathematical failure found in this presentation is the
  separate false equivalence in finding 2.

### Clarke--Grumberg--Peled boundary, lines 1824--1856

- The route-bounded acquisition status does not say the book is globally
  unavailable and does not treat preview locators, controlled lending,
  institutional access, the 1996 survey, the 2001 handbook chapter, the 2008
  Baier--Katoen book, or the 2018 second edition as the missing first-edition
  body.
- No grammar, algorithm, proof, example, or complexity theorem is attributed
  to the unacquired body. The host's four complexity classifications are
  explicitly assigned to independent sources. The remaining source-content
  acquisition is an open register obligation, not another rejection finding.

### Baier--Katoen presentation, lines 1352--1822

- Lines 1363--1419 retain the action-labelled transition-system tuple and
  define the binary handbook bridge \(R_0,V_0\) with explicit types. Forgetting
  action names preserves state sequences, and \(|R_0|\leq K\) correctly keeps
  the host's binary-edge parameter distinct from the source triple count.
- Finite/maximal/initial path distinctions and the no-terminal-state hypothesis
  at lines 1421--1432 are consistent. Under that hypothesis every member of
  \(\operatorname{Paths}(s)\) used by CTL is infinite.
- The CTL state/path grammar and semantics at lines 1434--1481 are well typed.
  Until is strong and current-inclusive, and system satisfaction is correctly
  vacuous when \(I=\varnothing\).
- The ENF translation-size warning at lines 1483--1497 is preserved:
  Theorem 6.30 cannot be obtained by first materializing an exponentially
  larger ENF formula.
- The least/greatest satisfaction-set characterizations, proofs, naive loops,
  simultaneous chains, optimized worklists, count invariant, and global
  subformula induction at lines 1499--1616 are coherent. Nullary truth is
  explicitly assigned \(\operatorname{Sat}(true)=S\).
- The source graph, label table, propositional comparison abbreviations, and
  final sets at lines 1618--1667 check out:
  \(\operatorname{Sat}(\exists\Diamond\Theta)=\{s_4,s_5,s_6,s_7\}\) and
  \(\operatorname{Sat}(\exists\Box b)=\{s_0,s_2,s_4\}\).
- The representation-sensitive complexity statement at lines 1669--1683 has
  the correct hypotheses: finite no-terminal system, \(N\) states, \(K\)
  source transitions, predecessor linked lists, direct modality handling, and
  no separately attributed asymptotic space theorem.
- The Hamiltonian-path family at lines 1685--1744 is correctly typed. Every
  graph vertex is initial, the added sink makes the system total, the recursive
  formula selects exactly a labelled graph path, and the final
  non-satisfaction equivalence is correct. The text identifies the missing
  uniformity premise in the book's informal \(\mathsf P=\mathsf{NP}\)
  inference.
- The CTL/LTL witnesses at lines 1746--1769 retain their source proof
  omissions. The CTL* grammar, LTL embedding, and strictness formula at lines
  1771--1805 are well typed; the atom-substitution step is correctly labelled
  as a reader completion.
- Lines 1807--1822 catalogue the source's dropped negation, malformed indexed
  family, wrong modality, weak-until operand, stale work-item comment,
  subfigure references, and proof boundaries instead of copying those defects
  as correct mathematics.

## Host and prerequisite consistency apart from finding 3

- handbook/parts/p08/temporal-epistemic-supplement.tex 42--164 supplies a
  nonempty total transition structure, infinite path type, CTL state grammar
  and strong-until semantics, and a mutually typed CTL* grammar before Part IX
  uses them.
- Host lines 948--967 type the existential and universal predecessor maps as
  operations on state sets and distinguish them from path quantifiers.
- Host lines 969--987 give the correct Boolean, next, least-until, and
  greatest-always equations on a finite total structure. Least approximations
  start at \(\varnothing\), greatest approximations at \(S\), and all displayed
  transformers are monotone.
- Host lines 997--1005 state the correct satisfaction-set correspondence and
  adjacency-list/worklist bound \(O((|S|+|R|)|A|)\).
- Host lines 1007--1014 use correctly typed finite witnesses for LTL--CTL
  incomparability: \(\mathsf{AG}\mathsf{EF}p\) is branching-sensitive, while
  universally read \(\mathsf F\mathsf Gp\) is not CTL-definable.
- Host lines 1016--1022 keep CTL/CTL* model checking and satisfiability as four
  distinct decision problems. Nothing attributes those bounds to the
  unavailable Clarke--Grumberg--Peled body.

## AGENTS technical-name audit

No hypothetical answer is named in advance. Source terms and reader
metalinguistic names are ordinarily introduced with necessity, definition,
standing, nonredundancy, and actual use at one location, notably:

- synchronization skeleton versus computation tree and global system
  flowgraph (lines 17--36);
- \(\operatorname{Blocks}\) versus \(\operatorname{Tiles}\) (lines 235--248);
- model fragment (lines 377--386);
- \(\mathsf{TURN}\) and the uniquely labelled global flowgraph (lines 388--450);
- interpreted Petri net (lines 477--493);
- structure-closure names and associated language families (lines 870--892,
  1007--1014, 1089--1106);
- MPL stage (lines 1255--1261); and
- the handbook bridge \(R_0,V_0\) (lines 1389--1401).

The unbound reuse of \(P\) in finding 1 is the sole local standing failure
found under this rule. The Clarke--Grumberg--Peled section correctly describes
owed artifacts without assigning names to an uninspected construction.

## Files and exact ranges actually read

Only the following repository text was opened as evidence:

1. handbook/parts/p09/presentations/n-c-016.tex, lines 1--1856, read directly
   from line 1 through EOF;
2. handbook/parts/p09/logic-in-computer-science.tex, lines 945--1022 and
   1504--1506;
3. handbook/parts/p08/temporal-epistemic-supplement.tex, lines 42--190;
4. spec/research/p09-clarke-emerson-1981-source-note.md, lines 1--884,
   through EOF;
5. spec/research/p09-queille-sifakis-1982-source-note.md, lines 1--867,
   through EOF;
6. spec/research/p09-emerson-halpern-1986-source-note.md, lines 1--729,
   through EOF;
7. spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md, lines
   1--470, through EOF;
8. spec/research/p09-baier-katoen-2008-ch6-source-note.md, lines 1--1120,
   through EOF;
9. spec/research/p09-source-presentations-lot2-3.md, lines 781--847 only;
10. spec/research/p08-new-content.md, lines 810--830 only;
11. handbook/bib/handbook.bib, only these complete entries and ranges:
    ClarkeEmerson1981 2393--2407, QueilleSifakis1982 2409--2422,
    EmersonHalpern1986 2424--2436, ClarkeGrumbergPeled1999 2438--2447,
    BaierKatoen2008 2449--2458, EmersonHalpern1985 4815--4824,
    ClarkeEmersonSistla1986 4826--4835, EmersonLei1987 4837--4846, and
    EmersonJutla1999 4897--4906.

Review/admission-status prose embedded inside the expressly permitted source
notes or compact-register excerpt was not used as evidence for this verdict.

## Prohibitions observed

- I did not open or use any N-c-016 review, board, admission, handoff, or
  review-history file.
- I did not inspect, list, ask, message, or delegate to another agent.
- I did not inspect a manuscript PDF, rendered manuscript page, screenshot,
  PNG, page image, or any other visual manuscript evidence.
- I did not open a historical publication file. No ambiguity required the
  exceptional source-page route after the permitted text notes were read.
- I did not build TeX or a handbook PDF.
- I did not run a test, test harness, checker, automated validator, repository
  script, or hash operation.
- I did not edit the manuscript, host, prerequisite, source notes, compact
  register, bibliography, ledger, or any file other than this review report.

REGISTER STATUS: OPEN
