REJECT

# Part IX blind R1 topic-specialist report

## Scope and method

I reviewed the current reader route rooted at `handbook/parts/p09.tex` and
`handbook/annex/p09.tex` under the four lots in the charter.  The body driver
has exactly one live input, `handbook/parts/p09/logic-in-computer-science.tex`
(`handbook/parts/p09.tex:1-3`), and the annex is a navigation-only unit
(`handbook/annex/p09.tex:1-17`).  I also checked the three explicit cross-part
references, the relevant prior definitions/results, the calculus and symbol
registries, the bibliography entries used by the body, and the P9-targeted
depth/new-content/apparatus rows.  I did not read another seat's transcript or
conclusion, edit any manuscript/spec/tool/generated file, run tests, or build
TeX/PDF.

The three explicit references in the body resolve to live objects:
`def:p04-captures-complexity`, `thm:p03-fagin`, and
`thm:p04-immerman-vardi`.  All 46 distinct bibliography keys cited by the P9
body have live entries in `handbook/bib/handbook.bib`.  Those mechanical facts
do not cure the mathematical and admission defects below.

## Findings

### F1 — critical — the stated first-order zero--one theorem is false under the handbook's own signature definition

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:14-17,
  33-55`; governing signature syntax at
  `handbook/parts/p02/first-order-syntax-semantics.tex:19-30,59-73`; the
  correctly scoped earlier theorem at
  `handbook/parts/p03/finite-model-theory.tex:14-20,25-40,122-123`.
- **Defect:** P9 fixes merely a “finite relational signature” and then states
  the zero--one law for **every** such signature.  The global signature
  definition maps relation symbols to all of `\N` and explicitly admits a
  zero-ary relation formula.  P3 correctly restricts the theorem to finite,
  purely relational, positive-arity vocabularies with no constants or
  functions; P9 silently drops the positive-arity hypothesis.
- **Minimal counterexample:** let `\sigma={P}` with `P` zero-ary.  For every
  nonempty universe `[n]` there are exactly two labelled `\sigma`-structures,
  one satisfying `P` and one not satisfying it.  Consequently the sentence
  `P` has probability `1/2` for every `n`, so the limit in P9's own definition
  is `1/2`, contradicting `handbook/parts/p09/logic-in-computer-science.tex:51-53`.
  The associated claim about one complete almost-sure theory at lines 53-55
  fails for the same reason.
- **Concrete harm:** a headline theorem is false and directly contradicts the
  book's already-correct finite-model table.  This is not repaired by the
  cited Glebskii--Fagin sources, because the hypothesis is missing from the
  statement being attributed to them.
- **Exact correction:** either delete the duplicate P9 theorem and point to
  `thm:p03-fol-zero-one`, or add exactly P3's scope: a fixed finite purely
  relational vocabulary whose relation symbols all have positive arity, with
  no constants or function symbols, under the uniform distribution on all
  labelled structures.  Carry that same scope into the extension-axiom/random-
  structure sentence.
- **Status:** open.

### F2 — major — the locality theorem is not the Gaifman theorem and is false on the natural reading induced by the preceding definition

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:61-80`;
  registered obligation `spec/registers/new-content.csv:110`.
- **Defect:** after defining a formula to be Gaifman local when its truth is
  determined by one bounded neighbourhood, line 75 says every first-order
  formula has a “Gaifman-local normal form”.  No such normal form is defined.
  The actual Gaifman normal-form theorem gives a Boolean combination of local
  formulas and **basic local sentences** asserting suitably separated
  witnesses; it does not make every formula equivalent to one local formula.
  Likewise, the Hanf clause needs an exact equivalence relation (radius,
  neighbourhood types, and exact-count or threshold-count convention) and its
  structure/degree scope, rather than the prose at lines 66-68.
- **Minimal counterexample to the local-formula reading:** in the empty
  relational signature, consider `\varphi(x):=\exists y\,(y\ne x)`.  For every
  radius, the pointed neighbourhood of `x` is the same one-point edgeless
  structure in a one-element model and in a two-element model, yet `\varphi`
  is false at the former point and true at the latter.  Global witness-spacing
  is precisely why basic local sentences occur in Gaifman's theorem.
- **Concrete harm:** the inexpressibility applications at lines 77-80 invoke a
  theorem whose stated form is not available, so the advertised proof route
  cannot be reconstructed even though connectivity and acyclicity themselves
  are indeed not first-order definable on all finite graphs.
- **Exact correction:** define `r`-local formulas and basic local sentences;
  state that each FO formula is equivalent to a Boolean combination of those
  objects, with the radius bound depending on quantifier rank (and the fixed
  vocabulary).  State Hanf equivalence separately with its exact count/
  threshold and degree convention.  Then give the finite graph pairs used for
  connectivity and acyclicity, or mark those applications as cited sketches.
  The cited treatments `EbbinghausFlum1995` and `Libkin2004` are suitable once
  their theorem is stated accurately.
- **Status:** open.

### F3 — major — Lot 1 omits required finite-model and classical-decision content and leaves fragment scopes indeterminate

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:26-31,
  102-113`; obligations `spec/registers/new-content.csv:108,112-115`; the
  existing but incomplete-for-this-obligation comparison table at
  `handbook/parts/p02/first-order-depth.tex:158-165,188-248`.
- **Defect:** `N-c-001` requires the finite failures of Craig and Beth and the
  finite EF method as well as compactness/Trakhtenbrot.  P9 supplies only the
  latter pair, and there is no finite-Craig or finite-Beth statement in the
  reader route.  `N-c-005` requires the Bernays--Schönfinkel--Ramsey,
  Ackermann, Gödel--Kálmar--Schütte, and reduction-class classification with a
  decidable/undecidable prefix table.  P9 merely names BSR and Ackermann and
  expressly stops short of a procedure or classification.  The Part II table
  supplies monadic FO, `FO^2`, guarded FO, and one BSR row, but not the omitted
  Ackermann/GKS/reduction-class deliverable, and P9 does not point to that
  table.
- **Scope defect:** “a declared equality convention” at P9 line 105 is a
  placeholder, not a declaration.  The `FO^2` and guarded-fragment sentences
  also omit the function-free relational-language hypotheses under which the
  cited finite-model and complexity claims are being made.  The exact Part II
  rows show why those qualifications are load-bearing
  (`handbook/parts/p02/first-order-depth.tex:199-236`).
- **Concrete harm:** readers cannot determine the input language of the claimed
  decision problems, and the P9 route does not contain the classification its
  register row promises.  Allowing the handbook's ambient function symbols to
  leak into a fragment name is not a harmless notational variant.
- **Exact correction:** add a finite-semantics comparison statement for Craig
  and Beth with the exact counterexample/source boundary and a precise link to
  the finite EF theorem; replace lines 102-113 by, or explicitly link them to,
  a table giving formula prefix, equality policy, constants/functions,
  satisfiability versus validity, finite-model status, and decision result for
  every registered class, including Ackermann, GKS, and the reduction classes.
  Say explicitly whether equality is present in each row.
- **Status:** open.

### F4 — critical — the ALC tableau as written is neither correct nor a total terminating algorithm

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:118-136,
  146-164`; obligation `spec/registers/new-content.csv:116`.
- **Defect 1 (completeness):** the method internalizes `C\sqsubseteq D` as
  `\neg C\sqcup D` but never puts the resulting concepts in negation-normal
  form and supplies no rules for negated complex concepts, `\top`, or `\bot`.
  Its sole clash condition is an atomic `A,\neg A` pair.
- **Minimal counterexample:** take input concept `A\sqcap B` and TBox
  `{\top\sqsubseteq\neg(A\sqcap B)}`.  The input is unsatisfiable.  The written
  procedure may decompose the input to `A,B`, choose the second disjunct of
  `\neg\top\sqcup\neg(A\sqcap B)`, and leave `\neg(A\sqcap B)` undecomposed.
  No stated clash applies, so it reports an open branch.
- **Defect 2 (termination):** “for every `\exists r.C` create an
  `r`-successor” has no expansion record or applicability condition.  The same
  existential at one unblocked node can therefore create successors forever.
  Finiteness of the closure and ancestor-label blocking do not bound the number
  of repeatedly generated siblings, so the claimed termination measure at
  lines 159-161 does not prove termination of the stated procedure.
- **Defect 3 (scope/status):** ABoxes are defined at lines 130-131 but the
  algorithm starts with a single input concept, not an ABox completion graph.
  No soundness lemma, model-unravelling completeness lemma, or exact status is
  supplied, although `N-c-009` requires tableau correctness at theorem level.
- **Exact correction:** declare NNF and the finite closure; give each Boolean,
  existential, universal, top/bottom, clash, and GCI rule with an applicability
  mark; generate at most one witness per applicable existential occurrence;
  state when labels are saturated and when blocking is tested; and prove
  closed-branch soundness plus open-blocked-branch model construction.  Either
  scope the method expressly to concept satisfiability relative to a general
  TBox or add the ABox rules.  Register the algorithm/status at the promised
  level.
- **Status:** open.

### F5 — major — the description-logic family and source surfaces do not meet their exact obligations

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:138-172`;
  obligations `spec/registers/new-content.csv:117-118`; apparatus
  `spec/registers/apparatus.csv:96`.
- **Defect:** the two prose sentences about `\mathcal{EL}`, DL-Lite, and more
  expressive logics do not give constructor sets, reasoning problems, TBox
  conventions, OWL correspondences, or the registered complexity table from
  `\mathcal{ALC}` through the named expressive families.  “Polynomial-time
  classification” and “many ontology-mediated queries” are family-wide phrases
  whose exact task and input convention are not fixed.  The expected apparatus
  A-095 is absent.
- **Source/status defect:** the modal-translation theorem is mathematically a
  straightforward structural induction, but its status names
  `SchmidtSchaussSmolka1991`; the registered source for `N-c-011` is Schild's
  correspondence, and no `Schild1991` bibliography entry is present.  The
  current status therefore does not identify the registered theorem source or
  provide a local proof.
- **Exact correction:** add A-095 with a row-specific grammar/constructor set,
  reasoning task (concept/TBox/ABox consistency, subsumption, classification,
  query answering), input convention, exact upper/lower bound, and OWL map.
  Give the ALC--multimodal-K induction locally or add and cite the exact Schild
  source; keep the no-global-TBox hypothesis already correctly stated at lines
  141-143.
- **Status:** open.

### F6 — major — the temporal/automata route is not reconstructible at the registered algorithm and acceptance ceilings

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:177-227`;
  obligations `spec/registers/new-content.csv:119-122` and
  `spec/registers/depth-gaps.csv:94`.
- **Defect:** past operators are dismissed as “analogous” without their syntax
  or clauses, and the registered Gabbay--Pnueli--Shelah--Stavi expressive-
  completeness boundary is absent.  The omega-automata “definition” supplies
  acceptance predicates but no automaton tuple, transition type, initial-state
  convention, nondeterministic acceptance quantifier, or run definition.  It
  then says the same objects stand over words **or trees**, even though a tree
  run is a labelled tree and Büchi/parity/Rabin acceptance must quantify over
  its branches; “a run visits” is not a tree-acceptance clause.
- **Algorithm gap:** the route states the exponential LTL-to-Büchi existence
  theorem but never gives the automata-theoretic model-checking construction
  required by `D-P10-010`: negate the property, take the product with the
  transition structure, and decide accepting-cycle/emptiness.  A prior Part
  VIII unit does define a nondeterministic Büchi **word** automaton
  (`handbook/parts/p08/temporal-epistemic-supplement.tex:353-369`), but P9 does
  not reference it and it does not supply parity/Rabin/tree types or the
  missing product algorithm.
- **Exact correction:** define previous/since (or explicitly point to their
  exact earlier definition); state the exact Kamp/GPSS domains; type word and
  tree automata separately, including the existential run and all-branches
  acceptance quantifiers; and give the complete LTL model-checking product and
  emptiness algorithm with input/output and correctness invariant.  Preserve
  the already-correct least-priority-even convention at lines 200-203.
- **Status:** open.

### F7 — major — two fixed-point equations are not the promised CTL/CTL-star labelling algorithm or its correctness proof

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:229-255`;
  obligation `spec/registers/new-content.csv:123`.
- **Defect:** the route gives examples rather than full CTL/CTL* grammars and
  semantics, then gives only the `EG` and `EU` equations.  It never says that
  least-fixed-point iteration starts at `\varnothing`, greatest-fixed-point
  iteration starts at `S`, how atomic/Boolean/`EX`/universal subformulas are
  labelled, or how the bottom-up order is chosen.  There is no induction
  proving that a generated label is exactly the satisfaction set.  The
  `N-c-016` row expressly requires the labelling algorithm at full-entry level
  **with correctness proof**.
- **Concrete harm:** the displayed equations are correct on finite total
  structures, but they do not determine a total procedure for an arbitrary CTL
  formula and do not justify the complexity conclusion for that procedure.
- **Exact correction:** either link to and import the complete earlier CTL and
  CTL* syntax/semantics, or restate them; give all labelling clauses, the two
  iteration initializations and stopping tests, an induction on subformulas
  proving label correctness, and the exact `O(|\varphi|(|S|+|R|))` bound for
  the declared adjacency representation.  Keep CTL* satisfiability/model-
  checking separate from CTL.
- **Status:** open.

### F8 — major — BDD, modal-mu, and PDL claims are below their stated definitions/theorem levels

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:257-284`;
  obligations `spec/registers/new-content.csv:124-128`.
- **Defect:** the BDD sentence never defines orderedness or the two reduction
  operations and does not state Bryant canonicity exactly (for each fixed
  variable order, one reduced ordered BDD per Boolean function up to rooted
  labelled isomorphism).  The modal-mu entry omits formula environments and the
  registered alternation-hierarchy statement.  The PDL paragraph omits atomic
  programs, the mutually recursive formula/program grammar, relational
  semantics for union/composition/test/star, the Segerberg axiom/rule surface,
  an entry card, and the registered small-model theorem.  There is no PDL
  calculus sheet in `handbook/registry/calculi/`.
- **Concrete harm:** terms such as “Fischer--Ladner closure” and “standard
  Segerberg axioms” cannot be eliminated into any object present in the reader
  route.  Consequently the completeness and EXPTIME claims have no exact
  syntax/calculus pair to govern them.
- **Exact correction:** define reduced ordered BDDs and state canonicity at the
  promised theorem status; add the modal-mu alternation definition/strictness
  statement with its exact finite-transition-system boundary; and supply the
  full PDL entry, registered calculus, Fischer--Ladner closure, filtration/
  small-model theorem, and exact EXPTIME decision problem.
- **Status:** open.

### F9 — critical — the Hoare theorem refers to three nonexistent displayed rules and an undefined semantics

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:289-330`;
  `handbook/annex/p09.tex:14-16`; obligations
  `spec/registers/new-content.csv:126`, `spec/registers/depth-gaps.csv:135`,
  and `spec/registers/apparatus.csv:23,97`.
- **Defect:** only assignment and while are displayed.  Consequence,
  sequencing, and conditional are merely named, yet the theorem and annex say
  that all five are displayed and proved sound.  No command grammar,
  expression/guard evaluation, state-transition relation, or fault convention
  defines the “standard deterministic while-language semantics”.  There is no
  Hoare calculus sheet, no complete rules table, no weakest-precondition
  calculus, and no required worked verification example.
- **Proof-status defect:** the theorem is metadata-marked `cited=Apt1981`, while
  lines 315-322 present an unaddressed induction sketch as a proof.  Because
  three rule premises/conclusions are absent and the semantics is unspecified,
  that paragraph cannot be a complete proof of the theorem as worded.
- **Exact correction:** define the exact deterministic while language and
  small- or big-step semantics; add a registered Hoare sheet containing every
  rule and side condition; add the A-096 rule/wp table and a derivation of one
  nontrivial loop example; prove each rule sound against the declared
  semantics; and mark the theorem `proved` or `sketched` with the actual proof
  address.  State Cook relative completeness only for the exact assertion-
  language expressiveness hypothesis already mentioned at lines 324-326.
- **Status:** open.

### F10 — critical — the displayed separation-logic frame rule is not sound from the stated hypotheses

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:332-349`;
  obligation `spec/registers/new-content.csv:127`.
- **Defect:** disjoint heap union plus the stack-variable nonmodification side
  condition does not by itself validate the frame rule.  Its soundness also
  requires a local command semantics (equivalently, the relevant safety-
  monotonicity/frame property for command actions).  No command semantics or
  locality lemma is stated.
- **Minimal countermodel:** let `P` and `Q` be the singleton predicate
  containing a one-cell heap `h_\ell`, and `R` the singleton predicate
  containing a disjoint one-cell heap `h_m`.  Let a heap transformer `C` leave
  `h_\ell` unchanged but, on `h_\ell\uplus h_m`, delete the second cell and
  return `h_\ell`.  It modifies no stack variable free in `R`.  The premise
  `{P}C{Q}` is valid, while `{P*R}C{Q*R}` is false.  The missing property is
  exactly that execution on an extended heap preserves the untouched frame.
- **Concrete harm:** P9 presents a rule shape as sound without the semantic
  hypothesis that makes it sound, and does so without any registered calculus,
  violating the charter independently of the missing Hoare sheet.
- **Exact correction:** fix a standard local heap-command language and prove
  its commands satisfy safety monotonicity and the frame property, or make
  locality an explicit semantic hypothesis of the rule.  Define safety/fault
  in triple validity, retain the stack-variable side condition, register the
  rule surface, and supply the promised theorem-level soundness argument.  The
  cited Reynolds/O'Hearn sources distinguish these semantic and syntactic
  conditions.
- **Status:** open.

### F11 — major — SLD, negation-as-failure, and normal-program syntax are not defined before their theorems

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:354-396`;
  obligations `spec/registers/new-content.csv:129-130`,
  `spec/registers/depth-gaps.csv:133-134`, and apparatus
  `spec/registers/apparatus.csv:24,98,149`.
- **Defect:** the least-`T_P` claim is standard only after fixing the Herbrand
  language, universal closure of clauses, and the treatment of logical
  equality.  “Atomic formulas” under the global grammar includes equality,
  whereas the Herbrand-base construction used by `T_P` is predicate-atomic;
  the P9 definition does not choose a scope.  The SLD paragraph gives no goal
  syntax, selected-clause variant condition, mgu/composition convention,
  computed-answer substitution, success/failure clause, or separation between
  completeness of SLD and completeness of a fair search.  Prolog is absent.
  Clark completion and SLDNF are only names, with no definition or theorem
  hypotheses.
- **Stable-model fallout:** “finite propositional normal program” is used
  before its rule grammar is defined.  The reduct instructions therefore do
  not say whether constraints, classical-negation atoms, or empty heads are in
  the input class.  The NP-completeness claim is correct for the standard
  finite ground normal-program problem, but the text has not fixed that
  problem.
- **Exact correction:** register A-023 as an exact SLD calculus with finite
  goals, standardized-apart clauses, mgu action, computed answers, and the
  soundness/completeness theorem; define the selected fair tree/search
  condition separately; define Clark completion, allowed negative goals,
  floundering, and SLDNF scope; and add the promised worked SLD tree.  Before
  defining the reduct, give the exact ground normal rule
  `a <- b_1,...,b_m, not c_1,...,not c_n` and state whether constraints and
  classical-negation atoms are excluded or encoded.
- **Status:** open.

### F12 — major — CQ/Datalog syntax and the data/combined complexity boundary are not exact

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:398-404`;
  obligation `spec/registers/new-content.csv:131`.
- **Defect:** the text does not say whether its conjunctive queries are Boolean
  or have a distinguished output tuple.  For non-Boolean queries, the
  Chandra--Merlin homomorphism must map the distinguished variables/head tuple
  of `q_2` to that of `q_1`; this condition is absent.  “Canonical database”,
  “homomorphism”, and Datalog's safe function-free rule syntax are not defined.
  Finally, “combined complexity is strictly larger” is not an exact
  classification and does not identify whether program, query, database, or
  all three vary.
- **Exact correction:** define Boolean and `k`-ary CQs separately and state the
  head-preserving homomorphism theorem; define safe Datalog syntax and active-
  domain evaluation; then state query evaluation's parameters explicitly.
  For ordinary Datalog evaluation, record P-complete data complexity for a
  fixed program/query and EXPTIME-complete combined complexity (with the
  adopted reduction convention), as supported by `Vardi1982` and
  `AbiteboulHullVianu1995`.  Keep CQ evaluation/containment complexity separate
  from Datalog evaluation.
- **Status:** open.

### F13 — major — the registered QBF proof and complete logic-complexity surface are absent

- **Location:** `handbook/parts/p09/logic-in-computer-science.tex:412-435`;
  obligation `spec/registers/new-content.csv:133`.
- **Defect:** `N-c-026` requires a proof of QBF/TQBF PSPACE-completeness and a
  Ladner-style table.  P9 gives neither; it merely says the result is
  “established in Parts IV and V”.  The actual Part IV item is itself a cited
  theorem statement (`handbook/parts/p04/complexity.tex:237-241`), not the
  registered proof.  P9 also gives no exact labels for the alleged lookup and
  its seven-row table omits several decision problems introduced in the same
  chapter (including CTL*/modal-mu bounds and exact Datalog combined
  complexity).
- **Exact correction:** supply a reader-facing proof of TQBF membership by
  depth-first recursive evaluation in polynomial space and a fully specified
  polynomial-time hardness reduction from the adopted PSPACE machine/problem
  characterization; state the encoding and reduction.  Give exact links to
  Cook--Levin and FO undecidability and complete the per-logic table with the
  precise problem, structure class, fixed/varying parameters, and completeness
  notion.  Do not count the cited Part IV theorem as the proof required by this
  row.
- **Status:** open.

### F14 — major — P9 has unregistered notation and missing required apparatus; several technical names fail the local naming rule

- **Location:** P9 notation at
  `handbook/parts/p09/logic-in-computer-science.tex:118-129,177-183,242-250,
  257-264,300-304,327-341,354-367,379-389`; symbol registry
  `handbook/registry/symbols.csv:94-97,231,316`; apparatus obligations
  `spec/registers/apparatus.csv:23-24,96-98,149`.
- **Symbol defect:** the only symbol-registry row whose scope mentions P9 is the
  previously defined LFP constructor at line 316.  P9 introduces new roles for
  `\sqcap,\sqcup,\sqsubseteq`, temporal operators, CTL path/fixed-point
  notation, `\operatorname{Pre}_\exists`, `\mu/\nu`, `wp/wlp`, heap
  `\perp,\uplus,*`, `T_P`, and default `\mathsf{not}` without P9-scoped rows.
  The existing temporal rows are scoped only to P8.3, and the existing
  `\sqcup` row names the P4 blank-tape symbol, not ALC concept disjunction.
  P9 also switches from the registered `\mathsf X,\mathbin{\mathsf U},
  \mathsf F,\mathsf G` glyphs to unregistered italic `X,U,F,G`.
- **Apparatus defect:** no Hoare sheet A-022, SLD sheet A-023, DL-family table
  A-095, Hoare/wp table A-096, logic-programming semantics table A-097, or SLD
  tree A-148 exists in the live route/registry.  By contrast, the relevant
  global apparatus that does exist was checked: A-036 in Part II, A-044 in
  Part III, A-050/A-052/A-127 in Part IV, A-051/A-112 in Part XIV, and
  A-013/A-079/A-145--A-147 in Part VIII.  Those earlier objects do not supply
  the six missing P9 program/DL artifacts.
- **Technical-name rule:** “Gaifman-local normal form”, “reduced ordered binary
  decision diagram”, “Fischer--Ladner closure”, “standard Segerberg axioms”,
  “Clark completion”, “SLDNF”, “normal program”, “canonical database”, and
  “Datalog” are used without an exact eliminable definition/axiom and without
  all of necessity, standing, nonredundancy, and later-use data at their point
  of introduction.  These are mathematical interface gaps, not requests for
  stylistic expansion.
- **Additional registered boundary:** `N-x-015` at
  `spec/registers/new-content.csv:186` calls for at least an attributed pointer
  fixing the qualitative/quantitative model-checking boundary; P9 contains no
  probabilistic/stochastic model-checking or probability-logic pointer.
- **Exact correction:** register every genuine P9 glyph-role/scope and use the
  registered temporal glyphs consistently; add the six missing apparatus
  objects and link every displayed rule to its sheet; and either give each
  listed technical name its exact eliminable definition and standing or remove
  it until that artifact exists.  Add the registered quantitative-methods
  boundary pointer without transferring probabilistic results to the
  qualitative algorithms.
- **Status:** open.

## Checked-clean mathematics and boundaries

The following portions survived adversarial checking and should be preserved
while repairing the records above:

- `handbook/parts/p09/logic-in-computer-science.tex:14-31`: finite
  satisfiability/validity and the Trakhtenbrot boundary are correct once kept
  separate from the false zero--one scope.
- `handbook/parts/p09/logic-in-computer-science.tex:82-100`: the public Fagin
  and Immerman--Vardi cross-references resolve, the ESO certificate proof idea
  is honestly marked as a sketch, and the built-in-order hypothesis is
  correctly load-bearing.  The referenced statements at
  `handbook/parts/p03/finite-model-theory.tex:67-91` and
  `handbook/parts/p04/complexity.tex:412-475` match those uses.
- `handbook/parts/p09/logic-in-computer-science.tex:118-144`: ALC concept
  syntax/semantics and the no-global-TBox limitation on the multimodal-K
  translation are mathematically correct.
- `handbook/parts/p09/logic-in-computer-science.tex:177-196`: the displayed
  future-time `X/U/F/G` truth clauses, LTL PSPACE-completeness statement, and
  safety/liveness distinction are correct under infinite-word semantics.
- `handbook/parts/p09/logic-in-computer-science.tex:198-225`: the displayed
  Büchi, least-priority-even parity, and Rabin **run** acceptance conditions are
  correct for word runs; the Büchi closure/complement caution and S1S/S2S
  decidability statements are correct at citation level.  F6 concerns the
  missing automaton/run types and the invalid word/tree conflation, not those
  clauses themselves.
- `handbook/parts/p09/logic-in-computer-science.tex:229-255`: the CTL `EG` and
  `EU` satisfaction clauses and least/greatest fixed-point equations are
  correct on finite total Kripke structures; F7 concerns completeness of the
  algorithm/proof surface.
- `handbook/parts/p09/logic-in-computer-science.tex:269-278`: the bounded-
  counterexample warning correctly separates bounded absence from an unbounded
  proof; the CEGAR/interpolation sentences are acceptable as pointers.
- `handbook/parts/p09/logic-in-computer-science.tex:289-298,324-330`: partial
  versus total correctness and `wp` versus `wlp` are correctly distinguished,
  and the expressiveness hypothesis on Cook relative completeness is present.
- `handbook/parts/p09/logic-in-computer-science.tex:354-369`: for the standard
  equality-free definite-program setting, the displayed `T_P` operator and its
  omega-iteration/least-Herbrand-model theorem are correct.
- `handbook/parts/p09/logic-in-computer-science.tex:379-396`: after the normal-
  rule grammar is supplied, the Gelfond--Lifschitz reduct definition and NP/
  polynomial-verification bounds are correct for finite ground normal
  programs.
- `handbook/parts/p09/logic-in-computer-science.tex:398-410`: the
  Chandra--Merlin direction is correct for Boolean CQs (and for same-arity CQs
  after adding the head-tuple condition); the finite fixed-template CSP
  dichotomy is correctly separated from unrestricted homomorphism.
- `handbook/parts/p09/logic-in-computer-science.tex:415-442`: every complexity
  row actually printed is correct at the qualification shown, and the closing
  solver/certificate boundary appropriately refuses to promote a run or build
  to a theorem.

## Coverage ledger

- **Lot 1 — finite-model theory, zero--one laws, locality, descriptive
  complexity, decidable fragments, prefix classes:** checked completely.
  Open findings F1--F3.  Clean portions: finite semantics/Trakhtenbrot and the
  Fagin/Immerman--Vardi cross-part route.  No item in this lot was left
  unchecked.
- **Lot 2 — description logics, modal correspondence, blocking, families,
  complexity, ontology/query:** checked completely.  Open findings F4--F5.
  Clean portions: ALC grammar/semantics and the TBox-free modal translation.
  No item in this lot was left unchecked.
- **Lot 3 — temporal logics, omega/tree automata, MSO, explicit/symbolic model
  checking, modal mu, complexity:** checked completely.  Open findings F6--F8
  and the relevant part of F14.  Clean portions are enumerated above.  No item
  in this lot was left unchecked.
- **Lot 4 — Hoare/dynamic/separation; logic programming/stable/Datalog/CQ/CSP;
  complexity, symbols, citations, navigation:** checked completely.  Open
  findings F8--F14.  All 46 body citation keys and all three body references
  resolve; the annex's claim that all five Hoare rules are displayed does not.
  No source/content item in this lot was left unchecked.
- **P9 register coverage:** checked all P9-targeted rows `N-c-001` through
  `N-c-026`, `N-c-028`, `N-x-015`, `D-P10-010`, `D-P11-006` through
  `D-P11-008`, and the relevant apparatus listed in F14.  Rows whose content is
  correctly housed earlier in the book were credited rather than re-filed as
  omissions.
- **External gates:** build, PDF rendering/visual inspection, provenance,
  rights, human review, and user acceptance were not checked and are not
  implied by this source/content rejection, as required by the charter.

## Prioritized repair order

1. Fix F1's false theorem and F4/F10's invalid procedures/rule immediately.
2. Supply the registered Hoare, SLD, CTL-labelling, automata-model-checking, and
   PDL algorithms/calculi with exact status (F6--F9, F11).
3. Restore the missing finite/prefix, DL-family, BDD/mu, query/Datalog, QBF, and
   quantitative-boundary content (F3, F5, F8, F12--F14).
4. Register notation, add the missing tables/figures/sheets, and correct source
   attribution/navigation only after the mathematical objects are exact.
