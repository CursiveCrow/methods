REJECT

# R2 topic-specialist review: Part IX

Role: logic-in-computer-science / formal-logic correctness specialist.  This was
an independent read of the current live reader graph rooted at
`handbook/parts/p09.tex` and `handbook/annex/p09.tex`, the five Part-IX calculus
sheets, their Part-XIV routing, the relevant register, bibliography, symbol, and
generated-audit surfaces.  I did not consult another reviewer's transcript or
conclusion, edit any manuscript/specification/generator/test file, run tests, or
build TeX/PDF.

The current route contains substantial, mathematically useful repairs.  In
particular, the CTL, Hoare, and TQBF annex proofs are complete at their stated
local ceilings; the PDL, Hoare, separation, and positive/ground-negative SLD
rule shapes are correctly routed; and the former qualitative-only treatment of
probabilistic verification has been replaced by real DTMC/MDP/PCTL and
CTMC/CSL content.  Admission nevertheless remains blocked by the exact defects
below.

## F1 — Critical — the registered ALC procedure is unsound as initialized and its blocking discipline does not establish termination

**Evidence.**

- `handbook/parts/p09/logic-in-computer-science.tex:225-247` gives the ALC
  semantics, but does not state the standard nonempty-domain condition even
  though `handbook/registry/symbols.csv:637` says that \(\Delta^I\) is nonempty.
- `handbook/parts/p09/logic-in-computer-science.tex:257-284` creates a node for
  each ABox individual, the declared role edges, and a fresh tested-concept
  root, but never puts the asserted concepts \(C(a)\) into \(\mathcal L(a)\) or
  the tested concept into its fresh root.  It adds only internalized GCIs to
  every label.
- `handbook/registry/calculi/tableaux-alc.tex:5-16` likewise has rules for global
  GCIs, Boolean constructors, role restrictions, and clashes, but no
  initialization row importing ABox concept assertions or the tested concept.
- `handbook/annex/p09/proofs.tex:15-30` proves model-guided preservation only for
  formulas already in a label, while `handbook/annex/p09/proofs.tex:51-53`
  simply asserts that the named roots satisfy the ABox and that the tested root
  satisfies the tested concept.  Those conclusions do not follow from the
  printed initialization.
- Blocking is defined only for a "saturated nonroot node" with the same
  "completed label" as an ancestor
  (`logic-in-computer-science.tex:274-283`; `tableaux-alc.tex:2,14,18-20`), but
  neither *completed label* nor a saturation phase excluding existential
  witness generation is defined.  The existential rule applies whenever a
  node is unblocked.  The annex nevertheless assumes that label repetition
  blocks before unbounded successor creation (`proofs.tex:5-13`).

**Minimal counterexamples and harm.**

1. Let \(\mathcal T=\varnothing\) and
   \(\mathcal A=\{\bot(a)\}\).  The printed initialization creates the node
   \(a\) with no formula in its label.  No clash rule applies, so the branch is
   complete, open, and accepted, although no interpretation can satisfy
   \(\bot(a)\).  The same failure occurs for tested concept \(\bot\) with empty
   TBox/ABox: its root is created but never labelled by \(\bot\).
2. Let \(\mathcal T=\{\top\sqsubseteq\exists r.\top\}\).  On the open
   disjunctive choice at each node, every generated node contains an
   existential obligation.  Under the ordinary meaning of "saturated" as no
   applicable completion rule, the node cannot become blockable until that
   obligation has generated another successor; the same situation then
   repeats forever.  Thus the registered rules do not imply the annex's
   \(2^{|\mathcal C|}\)-path bound.  If a narrower pre-existential notion of
   saturation was intended, it is precisely the missing definition and side
   condition.

**Exact correction.**

1. State \(\varnothing\ne\Delta^I\).  Initialize
   \[
     \mathcal L(a)=\{\operatorname{nnf}(C):C(a)\in\mathcal A\}
       \cup\mathsf{Glob}(\mathcal T),
   \]
   retain every \(r(a,b)\), initialize a tested root by
   \(\{\operatorname{nnf}(C_0)\}\cup\mathsf{Glob}(\mathcal T)\), and initialize
   a TBox-only anonymous root by \(\mathsf{Glob}(\mathcal T)\).  Put this on the
   sheet as an explicit initialization row.
2. Define the exact label used for blocking and the expansion order.  In
   particular, complete the global/Boolean/universal consequences, test
   ancestor-label blocking **before** applying an existential at the candidate
   node, and re-evaluate dynamic blocking when labels change.  Then rewrite the
   termination paragraph and the open-branch model proof against that exact
   discipline.

This is the standard source boundary controlled by
`BaaderEtAl2003` and `BaaderHorrocksLutzSattler2017`; the latter is fetchable at
[doi:10.1017/9781139025355](https://doi.org/10.1017/9781139025355)
(`handbook/bib/handbook.bib:2205`).  Status: **open**.

## F2 — High — the definite-program/SLD adequacy theorem has an unfixed object-language equality scope and an undefined theorem hypothesis

**Evidence.**

- `handbook/parts/p09/logic-in-computer-science.tex:961-985` says only that the
  displayed clause members are atomic.  It does not exclude logical equality,
  state that the signature has a ground term, or cross-reference the earlier
  equality-free Herbrand convention.  The live Herbrand definition does make
  those choices: `handbook/parts/p02/first-order-depth.tex:23-38` requires a
  ground term (adjoining a fresh constant when necessary) and excludes logical
  equality from the Herbrand base.
- `handbook/registry/calculi/sld-resolution.tex:2-8` calls its equality
  "first-order unification equality" and supplies no object-level equality
  transition.  Thus unification is metalinguistic, but the Part-IX clause
  grammar does not say that equality atoms are absent.
- `handbook/parts/p09/logic-in-computer-science.tex:1004-1009` quantifies over a
  "correct answer" \(\eta\), but neither the definition at lines 988-1002 nor
  the sheet defines correct answerhood.  It is therefore unspecified whether
  the remaining variables are universally closed, existentially closed, or
  treated as answer parameters.  The factorization claim
  \(\eta=\theta\rho\) has no determinate hypothesis.
- The fairness sentence at `logic-in-computer-science.tex:999-1000` mixes atom
  selection with clause/node enumeration.  Completeness should instead fix a
  computation rule (the theorem works for any such fixed rule) and then require
  fair enumeration of the resulting complete SLD tree.

**Minimal counterexamples and harm.**

- If equality atoms are permitted by the printed word "atomic", take
  \(P=\{p(X)\leftarrow X=a\}\) and goal \(\leftarrow p(a)\).  With logical
  equality, \(P\models p(a)\).  But \(a=a\) is not in the equality-free
  Herbrand base and the sheet has no resolution step for it, so neither the
  displayed \(T_P\) nor the displayed SLD calculus derives the consequence.
  The least-model and adequacy statements are therefore false on one permitted
  reading.
- With \(P=\{p(a)\}\) and goal \(\leftarrow p(X)\), the empty substitution is
  an answer under an existential-query reading, since \(\exists X,p(X)\) is
  true, but it is not a standard correct-answer substitution, since
  \(P\not\models\forall X,p(X)\).  The current theorem does not choose between
  these readings.

**Exact correction.**  Declare that the pure definite/normal language here has
non-equality predicate atoms over a signature with a ground term (or explicitly
invoke the Part-II fresh-constant convention), and that equality in the sheet
is metalinguistic unification only.  Alternatively, add a separately sourced
object-equality program semantics and calculus; do not conflate the two.  For
an initial goal \(G=\leftarrow A_1,\ldots,A_n\) with original variables
\(\bar x\), define a substitution \(\eta\) on \(\bar x\) to be a correct
answer exactly when
\(P\models\forall((A_1\land\cdots\land A_n)\eta)\), where the universal closure
binds variables remaining after substitution.  State the factorization theorem
against that definition, a fixed computation rule, and fair enumeration of
all finite nodes/clauses of its complete SLD tree.

The controlling scholarly source is `Lloyd1987`, fetchable at
[doi:10.1007/978-3-642-83189-8](https://doi.org/10.1007/978-3-642-83189-8)
(`handbook/bib/handbook.bib:2490`).  Status: **open**.

## F3 — High — the quantitative model-checking repair still lacks the input invariants needed for its probability measures and polynomial-time claim

**Evidence.**

- `handbook/parts/p09/logic-in-computer-science.tex:631-639` says that each
  *enabled* state-action pair carries a distribution, but never defines
  \(\mathsf{Act}(s)\), requires it to be nonempty, or fixes whether schedulers
  are deterministic or randomized.  Nevertheless it immediately asserts that
  every fixed scheduler induces a path measure and defines extrema over all
  schedulers.
- The PCTL grammar introduces \(k\in\mathbb N\) without an encoding convention
  (`logic-in-computer-science.tex:643-653`).  Theorem
  `thm:p09-pctl-model-checking` then claims polynomial time in the **encoded**
  model and formula and justifies bounded until by dynamic programming
  (`logic-in-computer-science.tex:665-680`).  The displayed dynamic program is
  linear in the numerical value \(k\), not in the bit length of a binary
  encoding.  Thus the written argument does not establish the claimed
  encoding-independent polynomial bound.
- CSL permits an arbitrary real interval
  \(I\subseteq\mathbb R_{\ge0}\) (`logic-in-computer-science.tex:683-697`), but
  `thm:p09-csl-model-checking` describes an effective finite-input computation
  (`logic-in-computer-science.tex:701-707`).  No rational-endpoint/effective
  representation condition is stated, and the \(E(s)=0\) absorbing-state
  convention is also omitted.

**Minimal counterexample and harm.**  A one-state tuple with no enabled action
satisfies every printed requirement on enabled pairs vacuously, but has no
scheduler-induced infinite-path measure.  Hence
\(\Pr_s^{\min}\), \(\Pr_s^{\max}\), and the PCTL satisfaction clause are
undefined on a purported model in the theorem's domain.  Independently, with a
binary bound \(k=2^m\), the stated step-by-step dynamic program takes
\(\Theta(2^m)\) iterations although the written bound occupies \(O(m)\) bits.

**Exact correction.**  Type the MDP with a nonempty finite enabled-action set
\(\mathsf{Act}(s)\) at every state and a probability kernel exactly on those
pairs; define the scheduler class and the induced cylinder measure.  Print the
\(\min/\max\) decoration in the MDP object language.  Declare bounds \(k\)
unary (or state the running time in the numerical value of \(k\), or supply and
cite the correct binary-bound result).  Restrict effective CSL inputs to
rational thresholds and effectively encoded intervals, normally rational
endpoints with open/closed flags, and state that zero-exit states are
absorbing.  Then restate the algorithm/complexity boundary against those exact
encodings.  Status: **open**.

## F4 — High — binding-amendment register content remains represented by pointers or by only one of the listed source presentations

**Controlling requirement.**
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:3-7` makes the amendment
supersede pointer/treatment ceilings; lines 45-51 make every register row an
inclusion requirement; and lines 62-78 prohibit replacing it by a pointer,
capsule, or omitted source presentation.

**Residuals.**

1. `spec/registers/new-content.csv:122` (N-c-015) requires tree automata and
   decidability transfer.  The live text explicitly says it is only a pointer
   and declines to define the ranked alphabet, run, and acceptance relation
   (`logic-in-computer-science.tex:485-489`).  Replace this with the complete
   source-grounded presentation actually used: typed ranked alphabets, finite
   trees, bottom-up runs/transitions, acceptance, the stated closure/decision
   result, and the exact decidability-transfer application.  The existing
   online scholarly source is `ComonEtAl2007`, fetchable at
   [HAL-03367725](https://inria.hal.science/hal-03367725)
   (`handbook/bib/handbook.bib:5669`).
2. `spec/registers/new-content.csv:135` (N-c-028) requires the McMillan
   interpolation-in-verification item.  The current text is one sentence saying
   only that an interpolant strengthens an approximation
   (`logic-in-computer-science.tex:618-621`).  It supplies no algorithm, state
   encoding, SAT partition, interpolant invariant, iteration/termination
   criterion, or soundness boundary.  Reconstruct the actual source
   presentation rather than retaining the former pointer ceiling.  The cited
   paper is fetchable at
   [doi:10.1007/978-3-540-45069-6_1](https://doi.org/10.1007/978-3-540-45069-6_1)
   (`handbook/bib/handbook.bib:5318`).
3. `spec/registers/new-content.csv:114` (N-c-007) requires both guarded-fragment
   decidability and the modal connection.  The live Part-IX paragraph
   (`logic-in-computer-science.tex:171-178`) and its destination table
   (`handbook/parts/p02/first-order-depth.tex:225-236`) give the guarded syntax,
   model properties, and complexity, but never state the modal standard
   translation into the guarded fragment or the exact resulting boundary.  Add
   that source-attributed translation/result; a generic ALC-to-K theorem is not
   this obligation.
4. `spec/registers/depth-gaps.csv:133` (D-P11-006) explicitly includes Prolog.
   The live route gives abstract SLD/SLDNF only
   (`logic-in-computer-science.tex:988-1091`) and nowhere defines Prolog's
   operational selection/search convention or its departure from fair SLD-tree
   enumeration.  Supply that separately attributed operational presentation,
   including its completeness/divergence and unification/occurs-check
   boundaries; do not silently identify it with the abstract fair procedure.
5. `spec/registers/new-content.csv:186` (N-x-015) is no longer lawfully excluded:
   it lists both Halpern 2003 and Baier--Katoen 2008 for probabilistic/stochastic
   model checking and probability logics beyond a pointer.  Lines 623-708 are a
   genuine Baier--Katoen-based PCTL/CSL repair, but the reader route contains no
   separately identified Halpern probability-logic presentation and
   `handbook/bib/handbook.bib` has no `Halpern2003` entry at all.  Add the
   missing bibliographic authority and reconstruct its exact probability-logic
   language, model class, satisfaction clauses, and theorem/proof status as a
   separate source presentation; do not treat PCTL/CSL as automatically
   exhausting a materially different source.

Status: **open**.

## F5 — High — the Part-XIV rule-sheet routing is fixed, but the A-051 master decision table still does not harvest the accepted Part-IX problem boundaries

**Accepted routing.**  `handbook/parts/p14/rule-sheets.tex:80-87` now routes all
five Part-IX sheets exactly once: `tableaux-alc`, `hilbert-pdl`, `hoare-while`,
`separation-logic`, and `sld-resolution`.  Their labels agree with every body
hyperlink.  No residual routing defect was found there.

**Residual apparatus defect.**  `spec/registers/apparatus.csv:52` (A-051)
requires the master logic decision-problem table to give every logic's exact
problem and completeness degree.  `handbook/parts/p14/master-tables.tex:23-43`
does not harvest the current Part-IX results.  For example, it prints CTL model
checking merely as "polynomial time" at line 37 and omits CTL* entirely, even
though `logic-in-computer-science.tex:566-571` states P-complete CTL model
checking and the separate CTL* model-checking/satisfiability bounds.  It omits
PCTL and CSL (`logic-in-computer-science.tex:665-708`), stable-model reasoning
(`:1109-1114`), and conjunctive-query problems (`:1173-1180`); its Datalog row
at line 43 omits both the fixed-query P-completeness and combined
EXPTIME-completeness printed at `logic-in-computer-science.tex:1196-1204`.

**Concrete harm.**  The master lookup weakens exact complete results to broad
upper bounds and makes several admitted P9 systems unfindable, contradicting
its own promise at `master-tables.tex:5-9` not to weaken destination rows.

**Exact correction.**  Harvest one row per distinct Part-IX decision problem,
retaining the syntax/model class, fixed parameter, input encoding, reduction,
and completeness degree, and route each row to the corresponding Part-IX
theorem/card.  At minimum add the missing CTL*, PCTL/CSL, stable-model, CQ, and
combined-Datalog rows and change CTL from "polynomial time" to the exact
P-complete statement.  Status: **open**.

## Verified-clean current content

- **Lot 1:** finite satisfiability/validity, the Trakhtenbrot boundary, the
  positive-arity zero--one scope and nullary counterexample, finite Craig/Beth
  failure, Gaifman normal form, bounded-degree Hanf locality, Fagin, and the
  ordered Immerman--Vardi scope are mathematically coherent.  The BSR,
  Ackermann, GKS, and equality boundary are typed separately.  The GF modal
  register obligation is the residual recorded in F4.
- **Lot 2:** ALC syntax/semantics apart from the omitted nonempty-domain clause,
  the ALC--multimodal-K boundary, and the EL/DL-Lite/SHOIQ/SROIQ problem table are
  coherent.  The ALC decision calculus/proof is blocked exactly by F1.
- **Lot 3:** the past-LTL semantics, FO/LTL statement, safety/liveness
  distinction, nondeterministic Buechi semantics, parity/Rabin acceptance,
  LTL-to-automaton translation, product/SCC counterexample criterion,
  BET/S1S/S2S statements, CTL fixed-point algorithm and complete annex proof,
  CTL/LTL/CTL* boundaries, modal-mu alternation statement, and ROBDD canonicity
  are coherent.  The tree-automata and quantitative-input residuals are F3/F4.
- **Lot 4:** the PDL grammar/relational semantics and registered Segerberg-style
  rule surface are coherent; the Fischer--Ladner/EXPTIME boundary is correctly
  scoped.  The Hoare sheet includes skip, assignment, consequence, sequence,
  conditional, partial while, and dependency-correct total while; the annex
  soundness induction and worked countdown are correct.  The separation frame
  rule has both locality and modified-variable hypotheses.  Stable and
  well-founded semantics, CQ homomorphisms/containment, Datalog data-versus-
  combined complexity, CSP, and the complexity table are coherent.  Pure
  SLD's residual specification is F2/F4.
- **Annex proofs:** `annex:p9.ctl.1`, `annex:p9.hoare.1`, and
  `annex:p9.tqbf.1` were checked line by line.  The selector recurrence in the
  TQBF proof has one textual recursive occurrence, the existential blocks may
  depend on the universal selector bit, reachability doubles correctly, and
  the final formula has polynomial size.  `annex:p9.alc.1` is not accepted for
  the reasons in F1.
- **Five calculus sheets:** PDL, Hoare, separation, and the printed SLD/SLDNF
  transition shapes are clean within their stated languages; ALC is not.
- **Bibliography:** every citation key actually used by the Part-IX body,
  annex, five sheets, and theorem metadata resolves in
  `handbook/bib/handbook.bib`.  The missing register-listed `Halpern2003`
  authority is separately recorded in F4.
- **Symbols and technical names:** the dedicated P9 rows
  `handbook/registry/symbols.csv:635-679` agree with the defined roles.  The
  AGENTS rule is satisfied for the newly introduced automaton, probability,
  fixed-point, program, heap, query, and QBF metalinguistic names.  It is not
  satisfied for the undefined load-bearing phrases *completed label* (F1) and
  *correct answer* (F2), nor can an undefined MDP scheduler domain support the
  probability names in F3.
- **Generated audit:** `handbook/generated/audit-p09.tex:15-78` covers all live
  Part-IX definition/theorem environments and accurately distinguishes
  `cited`, `proved=annex`, and untagged definitions.  Its four annex targets
  exist.  No reader-visible OPEN/TODO/stub/admission prose was found on the
  reader route.

## Obligation coverage

- New-content rows checked: N-c-001--N-c-026, N-c-028, and N-x-015.  Open:
  N-c-007, N-c-009, N-c-015, N-c-022 to the extent specified in F2,
  N-c-028, and N-x-015.  The remaining rows are source/content-clean at their
  declared theorem/status boundary.
- Depth rows with P9 as target checked: D-P10-010 and D-P11-006--D-P11-008.
  Open: the Prolog component of D-P11-006; the remaining components are clean.
- P9-relevant apparatus checked: A-013, A-022, A-023, A-036, A-044, A-050--052,
  A-079, A-095--097, A-112, A-127, A-148, A-157, A-160, A-165--166, A-177,
  A-180, A-189, and A-193.  Source/content open: A-051 as in F5 and A-023 to
  the SLD specification extent in F2.  Build, generated-tool execution,
  visual, human, and user gates were deliberately not evaluated in this review.

Final source/content verdict: **REJECT** until F1--F5 are corrected and the
same live bytes receive a focused mathematical recheck.
