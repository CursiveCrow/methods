VERDICT: REJECT

# Round 5 source-fidelity review of N-c-016

## Controlling scope

This verdict concerns only the current text of
`handbook/parts/p09/presentations/n-c-016.tex` as read through its final line,
its named host/prerequisite integration, the five supplied source/acquisition
notes, and the five exact bibliography records. It is a text-only
source-fidelity verdict. Four source-level repairs remain mandatory. Three are
independent defects in the reader-facing general Clarke--Emerson factoring
construction; the fourth is an ill-typed notation collision in the
Baier--Katoen-to-host bridge.

## Must-fix findings

### 1. Lines 443--452 do not give every fresh auxiliary program variable a total initial value

The text introduces \(z_{\Lambda}\) as a program variable with value domain
\(\{1,\ldots,d\}\), but lines 449--450 initialize it only when a duplicated
node \(v_r\) is both initial and has no incoming arc. This is not a total
typed construction:

- an initial \(v_r\) may have incoming cycle arcs, but no incoming arc is
  traversed before the initial state is evaluated, so its required initial
  value is still \(r\); and
- when the designated initial node is not in the duplicated \(\Lambda\)-class,
  the newly declared program variable is given no initial value at all.

The Clarke--Emerson authority note supports only the source's introduction of
auxiliary values to distinguish equal node labels and the carrying of their
assignments to local transitions (note lines 642--655). The manuscript labels
its stronger variable/domain construction as reader-facing, so that added
construction must itself be total before lines 479--480 may call the result
executable.

Minimal repair: for every fresh \(z_{\Lambda}\), give a value at every
designated initial state. If the initial node is \(v_r\), initialize
\(z_{\Lambda}:=r\) regardless of its indegree; if the initial node is outside
that duplicated class, choose and state a fixed default value in
\(\{1,\ldots,d\}\) (for example, 1). Keep the incoming-arc assignments for
later entries into the duplicated nodes.

### 2. Lines 455--477 omit the auxiliary discriminator from the source-state guards

The general source-node tuple at lines 461--474 contains only the current
region \(R_u\) and the \(p=k-1\) other-process region components. Its guard
at lines 465--477 therefore disjoins only
\(S_1\land\cdots\land S_p\). It never includes a current auxiliary equality
such as \(z_{\Lambda}=r\).

That omission defeats the stated purpose of the auxiliary value and fails to
recover the manuscript's own worked source construction: line 429 requires
the guard \(\mathsf{TRY}_2\land\mathsf{TURN}=1\). The authority note likewise
records that auxiliary values make equal global labels distinct before the
global graph is factored (lines 642--655). Merely copying assignments onto
outgoing local transitions does not let a local guard distinguish the two
current global nodes.

Minimal repair: make each guard disjunct the conjunction of the complete
non-\(P_i\) source condition for that global arc: the other-process region
atoms together with every auxiliary equality true at that source node. State
the empty-conjunction convention for the auxiliary part. This can be written
as an eliminable conjunction and need not introduce a speculative technical
name.

### 3. Lines 458--479 merge global arcs whose auxiliary updates are different

The rule creates one local \(R_u\to R_v\) arc by disjoining the guards of
*all* matching global \(i\)-arcs and then says to copy an auxiliary assignment
from “such a global arc” onto “the corresponding skeleton transition.” This
does not define an update when matching global arcs carry different
assignments, or when one carries an assignment and another carries none.

The defect is already visible in the worked example. Lines 422--426 retain
two separate \(\mathsf{NCS}_1\to\mathsf{TRY}_1\) transitions: the
\(\mathsf{NCS}_2\lor\mathsf{CS}_2\) transition has no \(\mathsf{TURN}\)
update, while the \(\mathsf{TRY}_2\) transition assigns
\(\mathsf{TURN}:=2\). The general rule would collapse them and leave a single
transition with no well-defined faithful update. The authority note requires
the assignments to be carried onto the *appropriate* local transition
(lines 647--655), not onto an endpoint-merged transition indiscriminately.

Minimal repair: for fixed local endpoints, partition the contributing global
arcs by their complete auxiliary update (including the empty/no-update case).
Create one local transition for each identical-update group, disjoin the full
source guards only within that group, and attach that group's common update.
If two updates differ, retain two local transitions, exactly as the worked
\(\mathsf{NCS}_1\to\mathsf{TRY}_1\) case does.

### 4. Lines 1510--1511 and 1597--1598 use \(L\) at two incompatible types without rebinding it

The Baier--Katoen source tuple explicitly declares
\(L:S\to2^{AP}\) at lines 1510--1511. Line 1597 then writes
\(L(\operatorname{tr}(\Phi))\) for the output of the host labelling method.
But \(\operatorname{tr}(\Phi)\) is a host CTL formula, not a state, so the
locally declared source \(L\) cannot be applied to it. The referenced host
method happens also to call its satisfaction-set table \(L\), but the current
paragraph neither qualifies that second notation nor declares a deliberate
overload. The bridge is otherwise explicitly type-sensitive; leaving its
conclusion ambiguous undercuts the claimed exact typed instantiation.

Minimal repair: avoid a second technical name and write that the host method
“returns exactly
\(\{s\in S:TS,s\models_{\mathrm{BK}}\Phi\}\).” Alternatively, introduce a
distinct host-table symbol with an explicit formula-to-\(\mathcal P(S)\) type,
standing, and use. Do not reuse the source's state-labelling function \(L\)
without an explicit typed qualification.

## Bounded positive findings

Subject to those four repairs, the remaining audited source surfaces are
substantively well controlled.

- The Clarke--Emerson presentation keeps the authorized published reprint
  distinct from the longer author manuscript; preserves the indexed
  \(EX_i/AX_i\) logic, total union relation, source defect in the universal
  approximation, source-versus-handbook reconstruction of the existential
  recurrence, exact Proposition 4.1/4.2 strength, and the abridged tableau and
  synthesis proof boundaries. The technical names “synchronization
  skeleton,” “global system flowgraph,” and “model fragment” have stated
  standing, distinctions, and uses. The new \(z_{\Lambda}\) construction is
  necessary and nonredundant, but findings 1--3 prevent its current definition
  and later use from satisfying the supplied technical-name rule.

- The Queille--Sifakis presentation preserves the original/reprint/access
  hierarchy and the unresolved redistribution authorization; types the
  execution-domain reconstruction without attributing omitted clauses to the
  source; distinguishes \(\operatorname{enable}a\) from
  \(\operatorname{after}a\); gives eliminable finite-family, process-family,
  and nullary conventions; preserves the printed `receivack` defect while
  using the defined `receiveack` action; retains image-finiteness and the
  delegated proof status of Propositions 1--2; and does not turn CESAR's
  iteration cap into a proof or completeness claim. No action-, message-,
  place-, or process-name blocker was found.

- The Emerson--Halpern presentation keeps the JACM article distinct from its
  preliminary/report source states; preserves the state/path types, closure
  hypotheses, exact language hierarchy, pointwise-versus-whole-model
  comparison, proof-supported repairs to Theorems 5--6 and the later
  cross-reference, Appendix and cited-result boundaries, the literal MPL
  \(U/X\) conflict, and the application-only status of the conclusion. New
  local notation is eliminably defined and used.

- The Clarke--Grumberg--Peled presentation remains an acquisition boundary.
  It attributes no grammar, algorithm, theorem, proof, or complexity claim to
  the unacquired 1999 body, and it keeps the 1996 survey, 2001 handbook
  chapter, and 2018 second edition distinct.

- The Baier--Katoen presentation preserves the action-labelled source tuple,
  no-terminal-state convention, maximal-path standing, exact CTL and CTL*
  types, non-strict until, ENF expansion boundary, Algorithms 13--16,
  Theorem 6.23 proof strength, Theorem 6.30 representation hypotheses,
  source defects, witness systems, and Theorems 6.83--6.84 proof boundaries.
  The definitions of \(R_0\), \(V_0\), \(\mathcal K_0\), and
  \(\operatorname{tr}\) give necessity, exact standing, nonredundancy, and
  later use. The recursive translation covers every primitive
  Baier--Katoen CTL constructor and is semantically compatible with the host
  CTL grammar. Finding 4 concerns only the final output notation, not the
  translation clauses themselves.

- The five bibliography entries agree with the supplied authority records in
  authorship, title, venue or publisher, year, volume/pages where applicable,
  DOI/ISBN identity, source-state note, and access/rights qualification. In
  particular, `ClarkeGrumbergPeled1999` identifies the 1999 MIT Press
  first-edition record and expressly says that no complete body was acquired.

## Host and prerequisite integration

The host defines a finite total transition structure, the typed predecessor
maps, the formula-to-state-set labelling method, and its separate correctness
and binary-edge complexity theorem. The prerequisite text supplies the
nonempty total CTL/CTL* state/path types inherited by that host. The
Baier--Katoen bridge correctly handles the source's possible empty state set
outside the host, maps a finite nonempty no-terminal source system to the
host's type, and distinguishes source transition triples \(K\) from collapsed
binary edges \(|R_0|\). The N-c-016 input is in the declared model-checking
section and does not alter the host's theorem statements. Apart from finding
4's overloaded \(L\), no host/prerequisite inconsistency was found in the
audited spans.

## Text ranges read

Every substantive range below was read as current text, not inferred from a
render or an earlier report.

- `handbook/parts/p09/presentations/n-c-016.tex`: lines 1--2021, complete
  through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`: lines 925--1055 and
  1475--1535, covering the reused CTL method/theorems and the N-c-016 input
  context.
- `handbook/parts/p08/temporal-epistemic-supplement.tex`: lines 35--185,
  covering the inherited transition-structure, CTL, and CTL* types.
- `spec/research/p09-clarke-emerson-1981-source-note.md`: lines 1--884,
  complete through EOF.
- `spec/research/p09-queille-sifakis-1982-source-note.md`: lines 1--867,
  complete through EOF.
- `spec/research/p09-emerson-halpern-1986-source-note.md`: lines 1--729,
  complete through EOF.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`: lines
  1--470, complete through EOF.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`: lines 1--1120,
  complete through EOF.
- `handbook/bib/handbook.bib`: lines 2393--2458, exactly the entries
  `ClarkeEmerson1981`, `QueilleSifakis1982`, `EmersonHalpern1986`,
  `ClarkeGrumbergPeled1999`, and `BaierKatoen2008`.
- `spec/research/p09-n-c-016-integrated-source-review-r5.md`: the complete
  file was read back through EOF after writing.

## Prohibitions observed and non-claims

- No prior N-c-016 review or report of any round was opened, including any
  report previously authored by this reviewer.
- No mathematical/publication review, board, admission, history, parent
  conclusion, or other agent output was opened.
- No agent was contacted and no work was delegated.
- No PDF, render, screenshot, page image, or historical publication file was
  opened or inspected.
- No web access was used.
- No TeX or handbook build, test, checker, validator, source-analysis script,
  hash, or executable source tool was run.
- This report does not establish compilation, cross-reference resolution,
  typography, page layout, visual quality, or rendered-PDF correctness.
- It does not independently authenticate the authority notes' historical
  source inspections or hashes, and it makes no legal determination about
  copyright, licence, fair use, distribution, or republication. It only checks
  that the manuscript's access/rights language stays within the supplied
  notes.
- It is not a mathematical/publication-board verdict, a rights clearance, a
  final register admission, or a human editorial approval. The rejection is
  confined to the four current text defects enumerated above.

REGISTER STATUS: OPEN
