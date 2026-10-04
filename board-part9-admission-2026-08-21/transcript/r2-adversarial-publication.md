REJECT

# Part IX R2 adversarial-publication review

The current Part IX source is not yet admissible.  Four source/content defects
have concrete reader failure paths.  This verdict does not depend on an
unobserved TeX, reference, or visual failure: the failures are present in the
live source and survive even if the book compiles and renders perfectly.

## Must-fix findings

### F1 [must-fix] The book publishes two identities for the same Trakhtenbrot theorem

- **Location.** The exact inherited result is labelled `thm:trakhtenbrot` by
  `handbook/parts/p04.tex:43-50`; its statement is
  `handbook/restoration/inherited-08248-08305.tex:43-51`.  The live Part III
  navigation explicitly calls that the *single public* Trakhtenbrot statement
  and says it does not create another identity at
  `handbook/parts/p03/finite-model-theory.tex:96-100`.  Part IX nevertheless
  creates `thm:p09-trakhtenbrot` with the same signature hypothesis and the
  same c.e./undecidability conclusions at
  `handbook/parts/p09/logic-in-computer-science.tex:57-63`, and routes the new
  identity again at `:1280`.  The duplication is visible in
  `handbook/generated/audit-p09.tex:16` and as adjacent independent named-index
  rows in `handbook/generated/named-theorem-index.tex:424-425`.
- **Concrete failure.** A reader looking up Trakhtenbrot receives two public
  theorem destinations and two status presentations for one proposition,
  while another live chapter guarantees that only the inherited destination is
  public.  Citations or later corrections can therefore attach to different
  identities for no mathematical distinction.  This is an actual identity and
  publication contradiction, not merely repeated explanatory prose.
- **Exact correction.** Remove the Part IX `hbtheorem` environment and replace
  it with a prose route to `Theorem~\ref{thm:trakhtenbrot}`.  Change the Part IX
  complexity-table route at line 1280 to that inherited label.  Regenerate the
  Part IX theorem/definition audit and named-theorem index so
  `thm:p09-trakhtenbrot` disappears from both.  Retain the Part IX explanation
  of the finite/unrestricted consequence boundary, but do not give the result
  another theorem identity.
- **Status.** Still open in current source.

### F2 [blocker] The advertised ALC procedure never initializes concept assertions or the tested concept

- **Location.** `handbook/parts/p09/logic-in-computer-science.tex:257-276`
  normalizes the tested concept and GCIs and creates ABox roots and role edges,
  but never states that a root label receives its ABox concept assertions or
  that the fresh tested root receives the tested concept.  The active sheet
  likewise declares the input at
  `handbook/registry/calculi/tableaux-alc.tex:2`, then supplies only global-GCI
  and expansion rules at `:5-20`; it has no initialization clause for either
  datum.  Despite that, Theorem `thm:p09-alc-tableau` claims equivalence for
  concept, TBox, and ABox input at
  `handbook/parts/p09/logic-in-computer-science.tex:288-292`.  The annex assumes
  the missing invariant at `handbook/annex/p09/proofs.tex:15-30` and concludes,
  without establishing it, that the roots satisfy the ABox and tested concept
  at `:51-55`.
- **Concrete failure.** Take the finite knowledge base with empty TBox and
  ABox `\(\{\bot(a)\}\)`.  Under the literal initialization printed in the
  method, the node for `a` receives no `\bot`; none of the registered rules can
  introduce it, so the branch is complete, clash-free, and accepted although
  the knowledge base is unsatisfiable.  The same omission lets an empty
  TBox/ABox test of concept `\bot` open unless the unprinted root-label
  convention is supplied.  Thus the `proved=annex:p9.alc.1` theorem is false
  for the procedure as actually specified.
- **Exact correction.** Add a literal initialization clause to both the method
  and active sheet.  Normalize every asserted ABox concept; initialize
  `\(\mathcal L(a)\)` with every normalized `C` for which `C(a)` is in the
  ABox, plus `\(\mathsf{Glob}(\mathcal T)\)`; retain every declared role edge;
  and initialize a tested root with the normalized tested concept plus the
  global GCIs.  Make the closure explicitly contain those normalized ABox
  concepts.  Then revise the first invariant paragraph of the annex to verify
  these base cases before applying the expansion-rule induction.
- **Status.** Still open in current source; a successful build cannot repair
  the missing algorithmic base case.

### F3 [must-fix] Binding-amendment N-x-015 admits PCTL/CSL syntax without defining the path formulas whose probabilities are measured

- **Location.** The board's binding amendment makes the former exclusion row
  `spec/registers/new-content.csv:186` part of the Part IX content ceiling.
  The new material correctly defines DTMC/MDP data at
  `handbook/parts/p09/logic-in-computer-science.tex:623-641` and prints PCTL
  syntax at `:643-653`, but its semantic clause at `:655-660` refers to the
  undefined set `\(\{\pi:\pi\models\psi\}\)`.  No clause states when a path
  satisfies `\(\mathsf X\Phi\)`, `\(\Phi\mathsf U\Psi\)`, or
  `\(\Phi\mathsf U^{\leq k}\Psi\)`.  The algorithm at `:665-680` then relies
  on exactly those missing until conditions.  The symbol registry registers
  only their roles and binding at `handbook/registry/symbols.csv:652-653`; it
  does not supply the missing truth definition.
- **Concrete failure.** From the live text alone a reader cannot determine
  whether `\(\Phi\)` must hold at every position before the first selected
  `\(\Psi\)`-position, whether position zero may already witness
  `\(\Psi\)`, or whether the bound counts transitions or visited states.
  Those choices change the measurable path set and the values returned by the
  displayed reachability equations.  Consequently the quantitative modality
  and the claimed total model-checking procedure are not reconstructible at
  the exact semantic ceiling required by the charter.
- **Exact correction.** For a path `\(\pi=s_0s_1\ldots\)`, print the three
  clauses
  `\(\pi\models\mathsf X\Phi\iff s_1\models\Phi\)`,
  `\(\pi\models\Phi\mathsf U\Psi\iff\exists j\ge0\,[s_j\models\Psi\land
  \forall i<j\,s_i\models\Phi]\)`, and the same clause with `\(j\le k\)` for
  bounded until.  State explicitly that `k` counts transitions.  Give the
  analogous elapsed-time clause for CSL's `\(\mathsf U^I\)` (target at a time
  in `I`, left operand at every earlier time), and bind the printed MDP
  `min`/`max` decorations directly to infimum/supremum over the declared
  scheduler class.
- **Status.** Still open in current source.

### F4 [must-fix] The must-level Prolog obligation is absent, leaving the fair-SLD theorem exposed to a false implementation reading

- **Location.** `spec/registers/depth-gaps.csv:133` requires at must/E level
  “SLD resolution with soundness/completeness, negation as failure, Prolog.”
  The body defines fair SLD and promises eventual discovery under fair
  enumeration at `handbook/parts/p09/logic-in-computer-science.tex:988-1010`,
  then treats SLDNF, completion, stable models, and well-founded semantics at
  `:1035-1137`.  There is no reader-visible Prolog definition or boundary in
  the Part IX body, annex, rule sheet, comparison table, or further reading.
- **Concrete failure.** The nearest operational conclusion says that fair
  enumeration eventually visits a refutation.  A reader looking for the owed
  Prolog treatment is given no warning that Prolog's ordered-clause,
  leftmost-selection, depth-first search policy is not that fair enumeration
  and can diverge before an existing refutation is reached.  The required
  distinction is therefore both absent and liable to turn the correct SLD
  completeness statement into an unsupported claim about an implementation.
- **Exact correction.** Add a short, exact Prolog operational-boundary
  paragraph after the SLD theorem and route it from the logic-programming
  comparison table.  It must state (i) necessity: distinguish the implementation
  search policy from fair SLD; (ii) definition/standing: the logical core uses
  ordered clauses, leftmost literal selection, and depth-first backtracking as
  an operational policy, not a new consequence relation; (iii)
  nonredundancy: that policy need not be fair and may diverge despite an SLD
  refutation elsewhere; and (iv) scope: cut and other extra-logical facilities
  are outside the theorem unless separately specified.  Add a controlling
  source already suitable for that implementation boundary.
- **Status.** Still open in current source.

## Checked-clean source/content coverage

### Lot 1: finite-model theory, locality, descriptive complexity, and decidable fragments

- N-c-001--N-c-008 are substantively present apart from F1's identity
  duplication.  Part IX routes the one live zero--one theorem and its extension
  axiom/random-graph calculation at
  `handbook/parts/p09/logic-in-computer-science.tex:70-77`; routes the live EF
  game, theorem, worked board, and finite-model comparison at `:89-97`; states
  exact Gaifman/Hanf hypotheses at `:99-144`; and routes the Fagin and ordered
  Immerman--Vardi results without duplicating those identities at `:146-166`.
- The monadic, two-variable, guarded, Bernays--Schönfinkel, Ackermann,
  Gödel--Kalmár--Schütte, and equality boundary are navigable at `:168-220`.
  The finite/arbitrary, equality, and function-symbol qualifications are
  printed rather than inferred from family names.

### Lot 2: description logics

- N-c-009--N-c-011 have syntax, set/relational semantics, TBox/ABox truth,
  multimodal-K scope, a registered sheet, a system card, complexity, and a
  family/OWL table at
  `handbook/parts/p09/logic-in-computer-science.tex:222-348`.
- The five constructor/complexity rows in
  `tab:p09-description-logic-family` keep the reasoning problem and number
  encoding attached to the bound.  F2 is the remaining substantive failure;
  the later expansion rules and the model-extraction argument are otherwise
  aligned once initialization is supplied.

### Lot 3: temporal logic, automata, explicit/symbolic/quantitative model checking

- N-c-012--N-c-018 and D-P10-010 are present: past LTL semantics and the
  discrete-word expressive-completeness theorem (`:354-386`), exact safety and
  liveness classes (`:388-396`), Büchi/parity/Rabin acceptance and the
  LTL-to-automaton route (`:398-466`), finite-word/S1S/S2S statements and the
  deliberately pointer-level tree-automata boundary (`:468-489`), complete CTL
  fixed-point labelling (`:498-555`), CTL/CTL*/LTL and modal-mu boundaries
  (`:557-591`), and ROBDD/symbolic-model-checking routes (`:593-621`).
- The CTL proof at `handbook/annex/p09/proofs.tex:58-94` covers every printed
  fixed-point clause and its worklist bound.  The Part VIII Büchi and CTL
  figures referenced at Part IX `:491-493` resolve to live destinations.
- The binding quantitative amendment has DTMC, MDP, CTMC, PCTL, CSL, a
  comparison table, error-bound warnings, bibliography, and registered symbols
  at Part IX `:623-728`; F3 is the remaining definition-before-use gap.

### Lot 4: program/database logics, complexity, and navigation

- N-c-019--N-c-021 and D-P11-008 have exact PDL syntax/card/sheet
  (`:734-782`), deterministic partial/total Hoare semantics, all active-sheet
  routes, soundness and relative-completeness boundaries, wp/wlp, a worked
  total-correctness loop, and the Hoare/separation table (`:784-956`).  The
  Hoare proof at `handbook/annex/p09/proofs.tex:96-123` matches both printed
  correctness tags and all registered rules.
- N-c-022--N-c-025, N-c-028, and D-P11-007 have definite least-model semantics,
  SLD and computed answers, the SLD figure, SLDNF/floundering, Clark completion,
  stable and well-founded semantics, conjunctive-query homomorphisms, Datalog,
  and fixed-template CSP at Part IX `:961-1253`.  The absent Prolog component is
  isolated as F4; no blanket termination or arbitrary-normal-program
  completeness claim was found.
- N-c-026 has a parameter-qualified complexity table at `:1255-1341` and an
  explicit polynomial-size TQBF construction with a reciprocal full annex
  proof at body `:1344-1354` and annex `:125-196`.  The selector construction
  uses one recursive occurrence and states the fresh-variable/dependency
  convention, so the usual exponential formula-duplication gap is not present.

## Apparatus, identity, and navigation checks

- The five Part IX calculus files are each rendered exactly once by
  `handbook/parts/p14/rule-sheets.tex:80-87`: `tableaux-alc`, `hilbert-pdl`,
  `hoare-while`, `separation-logic`, and `sld-resolution`.  Every `sheet:*`
  reference in the Part IX body and annex has a source label.  No unregistered
  editorial rule display occurs on the reviewed Part IX route.
- The Part IX theorem/definition register is routed exactly once at
  `handbook/parts/p09/logic-in-computer-science.tex:1382-1385`, with its unique
  table label at `handbook/generated/audit-p09.tex:4`.  Static comparison found
  64 unique body theorem/definition/method/example identities and exactly the
  same 64 unique generated links; there was no omission or orphan row.  F1 is
  a semantic/public-identity duplication against the pre-existing theorem, not
  a duplicate TeX label.
- All 34 Part IX theorem identities occur in
  `handbook/generated/named-theorem-index.tex`; proof-status reciprocity is
  exact for the four `proved=` theorems and the four annex items.  All 34
  theorem status tokens conform to the grammar in
  `handbook/CONVENTIONS.md:60-72`.
- The symbol CSV currently has 678 data rows; the generated registration table
  has 678 unique `entry:symbol-registry-*` destinations and the generated
  symbol index has 678 unique links to the same destination set.  Fifty-seven
  rows have P9 in scope, including the newly admitted probabilistic and TQBF
  notation.  The registry is reader-routed once through
  `handbook/parts/p01.tex:36` and the symbol index through
  `handbook/parts/p14/master-tables.tex:229`.
- Static reference extraction over the Part IX body, annex, generated audit,
  and five active sheets found 109 unique referenced targets and no missing
  source destination.  All 67 bibliography/status/source-card keys resolve in
  `handbook/bib/handbook.bib`.  The new finite-model, description-logic,
  automata, program-logic, database, and CSP entries have reader-visible roles
  in `handbook/parts/p09/logic-in-computer-science.tex:11-29` and `:1363-1380`.
- The reviewed noncomment route has no `OPEN`, `TODO`, `FIXME`, stub,
  unadmitted, owed, workflow/finalizer, or internal A-/N-/D-P row prose.  The
  occurrences of the word “open” are the mathematical open-branch notion in
  the ALC tableau.
- Local publication surfaces comprise six labelled body tables, one labelled
  generated theorem/definition-register table, and one labelled SLD figure.
  The description-logic, Hoare/wp, logic-programming, temporal-comparison,
  Büchi, CTL, and SLD apparatus routes are present.  No second
  `tab:p09-theorem-definition-register` or second Part IX audit input was
  found.

## Non-build/non-visual boundary

Per commission, I ran no tests and no TeX/PDF build.  I did not inspect page
breaks, floats, font substitution, index sorting after makeindex, hyperlink
click geometry, overfull boxes, or the rendered distinction between repeated
headers and first-page table captions.  The static source checks above do not
approve any of those gates.  Conversely, F1--F4 are source/content defects and
cannot be deferred to the final build, visual, provenance, human, or user
polls.
