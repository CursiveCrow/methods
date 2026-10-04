REVISE

# Round-three mathematical/proof review: N-c-012.b Pnueli 1977

## Review identity and scope

- Seat: mathematical/proof correctness.
- Stable agent identifier: `/root/p09_math_proof_review`.
- Frozen object reviewed: the exact round-three snapshot in
  `spec/research/boards/p09-n-c-012b/charter.md`.
- Authority read visually: archival wrapper `page-01.png`, followed by every
  body image `page-02.png` through `page-13.png`, corresponding respectively to
  printed pp. 46--57. The images, rather than OCR or memory, controlled every
  source reading.
- Manuscript read: `handbook/parts/p09/presentations/n-c-012.tex`, complete
  assigned lines 370--1048 and 1453--1460, plus adjacent lines 350--369,
  1049--1065, and 1438--1452 to check the Kamp, GPSS, safety/liveness, and
  version boundaries.
- Shared surface read: `handbook/parts/p09/logic-in-computer-science.tex`,
  assigned lines 599--823 plus adjacent lines 580--598 and 824--840.
- Evidence surfaces read: the complete
  `spec/research/p09-pnueli-1977-source-note.md`; ledger lines 151--167 plus
  their immediate Kamp/GPSS boundaries; and the complete `Pnueli1977`,
  `McNaughton1966`, and `Landweber1969` bibliography entries.

Three must-fix defects remain. The remaining mathematical package is checked
clean below; the verdict is not based on another seat or on a prior transcript.

## Findings

### R3-MP-F1 — must-fix — the finite-state proof changes the start point of a “proper” path without defining the generalized object, and never explicitly gives the system-validity quantifier

- **Locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:912-951`, especially
  `:920-924`, `:926-936`, and `:938-950`;
  `spec/research/p09-pnueli-1977-source-note.md:423-455`, especially
  `:432-440` and `:442-455`.
- **Claim:** The manuscript defines a proper execution to be an action-fair
  infinite path **beginning at the distinguished initial state** `s_0`
  (`n-c-012.tex:920-924`). It then invokes a “proper q-avoiding path from s”
  for an arbitrary relevant `p and not q` state `s` (`:938-950`). No second
  definition generalizes “proper” to a path whose first state is arbitrary.
  The intervening theorem also says that a formula is “valid ... on the fixed
  finite system” without explicitly defining this as truth at position zero on
  every proper execution (`:926-936`). Appendix B later makes the intended
  initial-state quantification recoverable through `L_prop(Sigma)`, but only
  after Theorems 4--5 have already used it.
- **Authority evidence:** Printed p. 55 first defines a proper execution of
  `Sigma` as a path starting at `s_0`, but the subsequent decision sketch speaks
  of an infinite proper execution sequence starting at the currently checked
  state `s`. The source therefore contains the same shorthand shift. A typed
  handbook reconstruction must resolve it rather than repeat it. The SCC
  argument itself is correct once the generalized continuation is stated.
- **Mathematical harm:** Under the live definition, a path beginning at
  `s != s_0` is not a proper execution. Consequently the displayed iff at
  `:938-950` applies an undefined adjective to the very witness on which the
  decision proof depends. The absence of an explicit system-satisfaction
  clause also leaves the quantifier domain of Theorems 4--5 unstated and makes
  the relation between those theorems and the later language inclusion
  `L_prop(Sigma) subseteq L(W)` definition-after-use rather than
  definition-before-use.
- **Exact correction:** Before Theorem 4, define without overloading the
  initial state:
  1. an infinite `R`-path `rho=t_0t_1...` from an arbitrary state `t_0=s`
     satisfies the action condition iff, for every `a in mathcal A`, an
     `a`-edge occurs infinitely often;
  2. a proper execution of `Sigma` is such an action-satisfying path with
     `t_0=s_0`; and
  3. `A` is valid on `Sigma` iff `(sigma,0) models A` for every proper execution
     `sigma` of `Sigma`.
  Then replace “proper q-avoiding path from s” in the SCC proof by “infinite
  q-avoiding path from s satisfying the action condition” (or introduce an
  exact, locally justified `action-fair continuation` abbreviation with its
  standing, distinction from a proper execution, and immediate use). Keep
  `L_prop(Sigma)` for the initial-state proper-execution language. Apply the
  same correction to the source note.

### R3-MP-F2 — must-fix — the attachment paragraph gives an unparameterized false exponential claim and overstates what global invariants eliminate

- **Locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:661-693`, especially
  `:689-693`; `spec/research/p09-pnueli-1977-source-note.md:248-266`,
  especially `:260-266`.
- **Claim:** In the explicitly two-process setting, the manuscript says that
  expanding strong opposite-location dependence can “recover exponential
  work,” and then says that global arithmetic invariants “avoid location-case
  enumeration altogether.”
- **Authority evidence:** Printed p. 51 gives the exact counts: a full
  attachment has a number of local assertions proportional to the **product**
  of component program sizes, whereas the displayed two-process partial
  attachment has a number proportional to their **sum**. It warns that strong
  interaction can force consideration of all opposite-process values and uses
  the phrase “regaining the exponential complexity.” The producer--consumer
  paragraph on the same page nevertheless says that each proposed global
  invariant is established by checking the initial state and every possible
  one-step transition of each processor.
- **Mathematical harm:** For the two explicit sizes `|I|` and `|J|`, unfolding
  every opposite-location dependency yields `Theta(|I||J|)` cases. Relative to
  the ordinary explicit input measure `|I|+|J|`, that is product/quadratic,
  not exponential. An exponential cross-product arises only after generalizing
  to a variable number of processes, where the full location space has size
  `product_i |L_i|`. Global arithmetic invariants avoid the full cross-product
  **attachment representation**; they do not eliminate the initial-state and
  per-transition preservation checks. The current prose therefore turns the
  source's informal complexity warning into an unqualified mathematical claim
  with no valid parameter and then overstates the alternative method.
- **Exact correction:** State the exact two-process comparison first:
  sum-size partial families versus a product-size `|I||J|` full expansion.
  Add that, when the number of processes is itself variable, the analogous
  product `product_i |L_i|` can be exponential in that parameter; identify this
  as the precise qualification of the source's “exponential” warning. Replace
  “avoid location-case enumeration altogether” by “avoid materializing the
  full cross-product attachment, while still requiring the initial-state and
  relevant per-transition preservation checks.” Make the same parameter and
  proof-obligation qualification in the source note.

### R3-MP-F3 — must-fix — Appendix B conflates a locally asserted acceptor existence with the claim actually referred to McNaughton

- **Locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:1004-1047`, especially
  `:1013-1017` and `:1033-1044`;
  `spec/research/p09-pnueli-1977-source-note.md:505-550`, especially
  `:514-518` and `:535-548`;
  `spec/research/p09-source-presentations-lot2-3.md:163`.
- **Claim:** The manuscript first correctly says that Pnueli **asserts** that a
  finite-state infinite-word acceptor `A_Sigma` for the proper executions can
  be constructed but prints no tuple or acceptance condition. It later says
  that “Pnueli assigns the acceptor construction ... to McNaughton's
  reference [32].” The source note and ledger repeat the latter attribution.
- **Authority evidence:** On printed p. 57, the `A_Sigma` sentence is Pnueli's
  own uncited observation: “for a given finite state system ... it is possible
  to construct a finite state automaton `A_Sigma`” accepting exactly the proper
  executions. Reference [32] is attached later to the term
  `omega`-regular in the separate inductive `L(W)` construction. The closure
  step then uses the imported omega-regular machinery, and reference [33] is
  attached to decidability of the final omega-language inclusion question.
  Pnueli does not display the `A_Sigma` construction, but he also does not
  explicitly refer that elementary system-acceptor assertion to [32].
- **Mathematical harm:** “Not locally proved” and “explicitly referred to a
  named external source” are different proof standings. The current final
  ownership sentence contradicts the accurate earlier sentence and assigns
  McNaughton a source-local role the printed locator does not give him. This is
  load-bearing because the charter requires exact separation of the local
  recursion, the asserted system acceptor, the imported closure theorem, and
  the external inclusion decision.
- **Exact correction:** Preserve three distinct standings in all three live
  surfaces:
  1. Pnueli locally asserts, without tuple, acceptance condition, or proof, that
     a finite-state acceptor `A_Sigma` for proper executions can be constructed;
  2. his citation [32] accompanies the omega-regular language machinery used
     for the `L(W)` recursion and its effective closure step; and
  3. citation [33] supports decidability of the resulting inclusion problem.
  It is correct to say none of those automata results is locally proved in this
  paper, but not that the uncited `A_Sigma` assertion is explicitly assigned to
  McNaughton.

## Criterion-by-criterion coverage

### C1 — source identity, provenance, page map, rights, and version boundary: checked clean

- The wrapper visibly reads *The Temporal Logic of Programs*, Amir Pnueli,
  May 1981. Physical images 2--13 carry printed pp. 46--57 and the complete
  conference body, including references and Appendices A--B.
- The manuscript, note, ledger, and `Pnueli1977` entry consistently identify
  the FOCS 1977 paper, pp. 46--57, DOI `10.1109/SFCS.1977.32`, the author-hosted
  route, the archival wrapper, and the absence of an observed republication
  licence.
- The 1981 wrapper is correctly kept separate from the 1977 printed body and
  is not called a second edition. The IEEE-direct comparison remains open.
- `McNaughton1966` and `Landweber1969` match printed references [32] and [33]
  in author, title, venue, year, and pages. F3 concerns proof attribution, not
  their bibliographic identities.

### C2 — program model, execution, atomicity, fairness, and specification hierarchy: checked clean

- `Sigma=<S,R,s_0>`, `R subseteq S times S`, infinite executions, and
  nondeterminism are typed exactly.
- Sequential `N:L times D -> L` and `T:L times D -> D` give the displayed
  transition iff. Concurrent `N_i,T_i` update exactly one control coordinate
  and the shared data while fixing every other coordinate.
- Atomic-statement granularity and permissible refinement are accurately
  separated. The early enabled-processor prose is not equated with the later
  literal every-action-occurs-infinitely-often premise.
- `R^0`, `R^{m+1}`, `R^*`, and `X` are typed and make reachability reflexive.
  Partial correctness, clean execution, mutual exclusion, deadlock freedom,
  strict temporal implication, total correctness, accessibility, and
  responsiveness retain distinct standings.

### C3 — P1/P2, ER, Theorem 1, and completeness sketch: checked clean

- P1 has the correct initial and transition-preservation premises and concludes
  invariance only on reachable states.
- Literal P2 retains `psi(s)`, quantifies rule ranks by `n>0`, and discloses the
  handbook-only extension of `A` to rank zero. The two-state counterexample is
  valid: the only ranked transition discharges through `psi(a)`, while no
  strictly later state satisfies `psi`.
- ER A1--A2/R1--R4 are correctly universally closed; R4's missing source side
  condition `u` not free in `q` is stated; first-order theorems remain axioms.
- Metarule I has the right induction direction and temporary-hypothesis
  standing. R4 is used only after induction.
- Theorem 1 is reported as a proof sketch with assertion-language
  expressiveness and pointwise finite branching, not a uniform branching
  bound. The Koenig step is valid under the execution-existence premise that
  the source omitted. The singleton deadlock example correctly exposes the
  vacuous `P(d,0)` base failure. The strict/A2/P2/inclusive-F/Theorem-3 tensions
  are kept explicit rather than normalized.

### C4 — sequential and concurrent applications: not clean because of R3-MP-F2; all other mathematics checked clean

- The repaired sequential attachment is now typed by locations, declares
  `s_0=<ell_0,u_0>`, and uses `q_{N(ell,u)}` at the correct location type.
  The initial and per-instruction formulas are premises to P1, not conclusions.
- Partial attachment has exact domains
  `p_i:L_2 times D -> Prop` and `q_j:L_1 times D -> Prop`; its displayed global
  assertion is type-correct and semantically only a representation change.
- The producer--consumer repair is correct. Capacity `C>0` is distinct from the
  next-location map `N`; load and indicator/semaphore maps have coherent
  codomains. Each step of mutual exclusion,
  `0 <= b = s_1+s_2+e <= r_1+r_2+e = C-f <= C`, and the final
  `C=0` deadlock contradiction is valid under the printed invariant and
  nonnegativity hypotheses.
- Only the complexity parameter and “altogether” claim in F2 remain defective.

### C5 — future calculus, quantified schemata, system rules, and Theorems 2--3: checked clean

- `H(t,p)` is correctly kept metalinguistic and atemporal. The recursive
  Boolean/F/G semantics supports nested formulas; both F and G are inclusive,
  and the absolute system present is `s_0`.
- G1--G3, RT/RG/MP, F2--F3, and Q1--Q4 have their exact displayed directions.
  Q1--Q2 remain biconditionals; Q3--Q4 remain one-way. The missing domain and
  schema-range specification is preserved as source-unresolved, with the
  atemporal restriction labelled a conservative handbook policy.
- RG is unrestricted only in the pure basis. Theorem 2 is limited to the pure
  propositional future fragment, and its completeness and decision arguments
  remain referrals; no complexity class is invented.
- The action family is finite, covers and partitions R, and the visually read
  p. 53 tail is exactly `j >= i`. I1/I2/E/N have correct state-variable
  closures. The nonempty-action counterexample correctly shows N unsound on
  arbitrary paths. DI and DN have the correct successor-side `p_2` premises
  and are accurately labelled derived.
- Theorem 3 is not inflated: only the representation instruction and skeletal
  “show every ER axiom” claim are attributed locally; individual derivations
  are not fabricated.

### C6 — finite-state package and appendices: not clean because of R3-MP-F1 and R3-MP-F3; all other mathematics checked clean

- Finite seriality is correctly stated and extends every finite path. The
  action-occurrence property on infinite paths is exact.
- Subject to F1's missing arbitrary-start definition, the SCC iff proof is
  valid: a reachable strongly connected cyclic component with one internal
  edge of every action supports a repeated finite tour, and every infinite
  fair path in a finite condensation graph eventually remains in a component
  containing an internal edge of every action.
- P and MRG have their exact source restriction. The path with a proposition
  true only initially correctly demonstrates why present-specific P cannot be
  followed by unrestricted RG. Theorem 5 retains both decidability and
  adequacy clauses in the context of the already displayed system-dependent
  proof basis.
- Appendix A's T2/T3 formulas and corollaries are externally owned. The local
  six-step lemma proof is valid at each propositional step and is not transferred
  to T2/T3.
- Appendix B gives both the MSO-successor and infinite-word routes. Atomic,
  complement, conjunction, disjunction, F, and G language clauses are correct;
  `S^*L(W)` implements inclusive F. The one-letter-word embedding in
  `[[p]]S^omega` is the standard formal-language convention. `L_prop(Sigma)`
  and the eliminable Büchi-recognizability reading of “omega-regular” are typed
  and satisfy the terminology rule. The inclusion direction is correct.
  F3 is solely the remaining attribution/ownership defect.

### C7 — cross-file consistency: not clean because the same F1/F2/F3 defects occur on evidence surfaces

- Hash-pinned manuscript, shared surface, bibliography, source note, and ledger
  agree on all source identities, formulas, theorem clauses, and the open
  admission boundary.
- The source note repeats F1's arbitrary-start “proper” shorthand and F2's
  complexity/avoidance overstatement. The source note and ledger repeat F3's
  incorrect assignment of the uncited `A_Sigma` assertion to McNaughton.
- No other notation, source, or version conflation was found in the assigned or
  adjacent surfaces.

### C8 — exposition, definition-before-use, and terminology: not clean because of R3-MP-F1; otherwise checked clean

- The prose is independently worded and visibly separates source statement,
  local reconstruction, local counterexample, and external referral.
- `leadsto`, partial attachment, proper execution, `L_prop(Sigma)`, and the
  eliminable omega-regular label otherwise supply necessity, definition or
  axiom, standing, nonredundancy, and actual use at their introduction.
- F1's “proper path from s” is the one remaining newly used technical
  generalization without an exact local definition and standing.

## Invariant-by-invariant coverage

- **I1:** Satisfied. This was source reading and mathematical reasoning only.
  No test, checker, harness, repository script, TeX, handbook PDF, or build was
  run.
- **I2:** Satisfied. Every round-three identity matched before substantive
  review and again after substantive review immediately before filing.
- **I3:** Satisfied. The wrapper and all twelve printed pages 46--57 were
  visually read; no conclusion rests on OCR.
- **I4:** Not satisfied by the frozen text because F1 leaves a quantifier domain
  and arbitrary-start path standing undefined, F2 omits the complexity
  parameter, and F3 misstates proof referral.
- **I5:** Satisfied. Strict temporal implication, ER A2, inclusive F, and the
  Theorem 3 representation remain visibly distinct, with a valid counterexample
  and no silent repair.
- **I6:** Satisfied. The Pnueli unit does not import later X/U syntax,
  LTL-to-Büchi translation, safety/liveness syntax, or PSPACE bounds. The
  Appendix B omega-language route is kept at its 1977/external-reference
  standing.
- **I7:** Not yet fully satisfied because of F1. All other technical names pass
  the five-part rule; the correction must either avoid a new name or define the
  arbitrary-start action-fair path locally with necessity, standing,
  nonredundancy, and use.
- **I8:** Satisfied. The author-hosted-body reconstruction and IEEE-direct
  comparison are separate; the latter remains open.
- **I9:** Satisfied. This verdict is independent and makes no majority appeal;
  REVISE keeps the topic open.
- **I10:** Satisfied. Nothing here purports to admit N-c-012 as a whole, Part IX,
  a build, a handbook visual audit, human review, or user acceptance.

## Hash verification

The following eight identities matched the charter both in the
pre-substantive gate and in the post-substantive/pre-filing gate:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` —
  `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps` —
  `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf` —
  `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex` —
  `80F9D4B96FEEBD329F683D5048E31544EDD4A97B3922752AC3D17DAB851D9219`
- `handbook/parts/p09/logic-in-computer-science.tex` —
  `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib` —
  `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md` —
  `BC88DE02A62B27112B723548D1483D2E8525CFB0EF175273DE4D15A3EAAB5BBF`
- `spec/research/p09-source-presentations-lot2-3.md` —
  `5FF3CCC5C8B88882D9218BB4221AEFAEB313EFF15657BCDB427C25F9F6852714`

## Independence, constraints, and runtime record

I did not inspect `ledger.md`, `transcript/chair.md`, any round-one or
round-two transcript (including my own), or any other seat's round-three
transcript. I did not contact another reviewer. I edited only this assigned
transcript. I ran no tests, automated checkers, test harnesses, repository
scripts, TeX, handbook-PDF inspection, or builds; the only command-level
operations were read-only source display and SHA-256 identity hashing. The
runtime model/version was not exposed by the harness.

## Final verdict

REVISE
