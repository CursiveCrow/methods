# Round-two source-fidelity review: N-c-012.b Pnueli 1977

## Opening position

`REVISE`.

The repaired snapshot correctly resolves the central round-two source questions,
including the literal `j >= i` action-tail quantifier on printed p. 53, but it
still omits two printed derived rules, leaves one theorem's printed proof status
unstated, overcommits on the range of the quantified schemata, drops a material
hypothesis from the producer--consumer example, and contains one wrong printed-
page locator.

## Findings

### SF-F1 — must-fix — the printed derived rules (DI) and (DN) are absent

- **Artifact locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:750-797` presents I1, I2, E,
  N, Theorem 3, and the accessibility-example summary without the two derived
  rules between them;
  `spec/research/p09-pnueli-1977-source-note.md:310-318` likewise jumps from
  I1/I2/E/N to Theorem 3; and
  `spec/research/p09-source-presentations-lot2-3.md:159` inventories only
  I1/I2/E/N.
- **Claim/omission:** the frozen unit purports to give the pure and
  system-dependent proof systems and the source's concurrent applications, but
  omits the source-labelled stronger derived forms (DI) and (DN).
- **Authority evidence:** printed p. 54 says that stronger versions of (I2) and
  (N), derivable from them, will be used in the sequel, and prints
  \[
  \frac{
    p_1\Rightarrow q
    \qquad
    q(s)\land p_2(s')\land R(s,s')\Rightarrow q(s')}
   {p_1\land Gp_2\Rightarrow Gq}\ ({\rm DI})
  \]
  and
  \[
  \frac{
   \begin{gathered}
    p_1(s)\land R(s,s')\land\neg A(s,s')\land p_2(s')
      \Rightarrow p_1(s'),\\
    p_1(s)\land A(s,s')\land p_2(s')\Rightarrow q(s')
   \end{gathered}}
   {p_1\land Gp_2\Rightarrow Fq}\ ({\rm DN}),
  \]
  with the state variables understood universally at the same metalinguistic
  standing as the adjacent displayed rules. The source then uses these stronger
  forms in Example 2.
- **Harm:** this is precisely a missing printed proof-system extension and its
  side conditions. It makes C5 incomplete, weakens the evidence for the
  Example-2 summary, and violates I4's exact-rule requirement.
- **Exact correction:** add (DI) and (DN), with the displayed premises,
  conclusions, implicit-universal-closure disclosure, derived (not primitive)
  standing, and their use in Example 2, to the manuscript and source note; add
  them to the ledger's proof-system inventory.

### SF-F2 — must-fix — Theorem 3's local proof boundary is not recorded

- **Artifact locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:793-797` states Theorem 3 and
  its corollary but does not say what proof the paper prints;
  `spec/research/p09-pnueli-1977-source-note.md:315-318` has the same omission.
- **Claim/omission:** the unit records proof/referral boundaries for Theorems 1,
  2, 4, and 5, but not for Theorem 3.
- **Authority evidence:** immediately after Theorem 3 on printed p. 54, Pnueli's
  entire printed proof is the short instruction to express
  `p leadsto q` as `p => Fq` and the assertion that all ER axioms can then be
  shown to be theorems of the future-restricted Kb fragment. No individual ER
  derivations are printed. The relative-completeness sentence follows as a
  corollary.
- **Harm:** without this boundary, the presentation does not distinguish a
  printed derivation from a skeletal proof assertion, contrary to C5 and I4.
- **Exact correction:** state that the proof is local but only skeletal, quote
  its two dependencies (the representation and the asserted derivability of
  every ER axiom), and do not suggest that the omitted derivations are printed.

### SF-F3 — must-fix — the quantified-schema metavariable is narrowed without source support

- **Artifact locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:708-720` and
  `spec/research/p09-pnueli-1977-source-note.md:266-282` type `p` in Q1--Q4 as
  a “first-order state formula” while calling the displayed strengths exact.
- **Claim:** the source restricts the Q1--Q4 schema variable to an atemporal
  first-order state formula.
- **Authority evidence:** printed p. 52 first says that F and G are unary
  operators used to construct arbitrary tense well-formed formulas together
  with the conventional logical connectives and quantifiers. Printed p. 53 then
  displays Q1--Q4 using `p`, but states neither an atemporal-only restriction on
  `p` nor a separate quantified domain semantics.
- **Harm:** the frozen wording turns an unstated source boundary into a definite
  restriction and can understate the printed schema range. This fails the exact
  typing/quantifier-treatment requirement in I4 and C5.
- **Exact correction:** present `p` as the source's formula metavariable with
  `x` free, and explicitly say that the paper does not state whether the schema
  range is restricted to atemporal formulas or permits arbitrary tWFFs. Keep
  the already-correct warning that no separate domain semantics is supplied. If
  the handbook elects to use only the atemporal instances, label that as a
  conservative handbook restriction rather than source wording.

### SF-F4 — must-fix — the producer--consumer deadlock claim loses its positive-capacity hypothesis and its promised calculation

- **Artifact locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:461-468` calls the later item a
  producer--consumer calculation, while `:654-658` gives only an unqualified
  outcome sentence; `spec/research/p09-pnueli-1977-source-note.md:231-233` also
  lists the outcomes without the decisive hypothesis.
- **Claim:** the paper's three global invariants derive mutual exclusion,
  `0 <= n <= N`, and absence of deadlock, without further qualification.
- **Authority evidence:** printed p. 51 defines the characteristic functions
  `m_i,r_i,s_i` and prints the three invariants
  \[
  m_1+m_2+\mathit{MUTEX}=1,
  \qquad
  r_1+r_2+\mathit{IS\_EMPTY}+\mathit{IS\_FULL}=N,
  \qquad
  s_1+s_2+\mathit{IS\_EMPTY}=n.
  \]
  The deadlock argument continues on printed p. 52. Its final case forces
  `r_1=r_2=IS_EMPTY=IS_FULL=0`, hence `N=0` by the second invariant, and calls
  this a contradiction because the buffer has **positive capacity**. The proof
  also uses the semaphore/characteristic-function standing and `s_i <= r_i` in
  the bound calculation.
- **Harm:** for `N=0` the source's final contradiction disappears. The frozen
  sentence therefore states the deadlock conclusion more generally than the
  printed calculation proves and does not actually supply the calculation that
  its earlier prose promises. This is a C4 scope and qualification failure.
- **Exact correction:** state `N>0` and the semaphore/characteristic-function
  hypotheses, print the three invariants, and give the source's essential
  deductions for mutual exclusion, both buffer bounds, and the two deadlock
  cases. Keep the example identified as an invariant proof, not later model
  checking.

### SF-F5 — must-fix — F2 and F3 have the wrong printed-page locator in the source note

- **Artifact location:**
  `spec/research/p09-pnueli-1977-source-note.md:50` assigns F2--F3 to printed
  pp. 53--54.
- **Authority evidence:** both derived formulas, `A => FA` (F2) and
  `FFA => FA` (F3), appear at the lower right of printed p. 52. Printed p. 53
  begins with the continuation of the Kb/S4 comparison, Theorem 2, and then
  Q1--Q4 and the system-dependent axioms.
- **Harm:** the visual-locator table is expressly an exact page map; this wrong
  locator frustrates independent verification and fails C1/C7.
- **Exact correction:** move F2--F3 into the `51--52` row (or otherwise cite
  printed p. 52 exactly) and remove them from the `53--54` row. The manuscript's
  broader `pp. 52--53` citation at lines 725--730 is already compatible with the
  source.

## Checked-clean coverage

- **C1:** The title, author, FOCS 1977 identity, printed pp. 46--57, DOI,
  author-hosted NYU route, retrieval date, three authority/render hashes,
  image-only standing, physical/printed page map, May 1981 wrapper boundary,
  no-licence observation, independently worded-use boundary, and still-open
  IEEE-file comparison are otherwise consistent across manuscript, note,
  ledger, and bibliography. The wrapper and all twelve printed pages were read
  visually. SF-F5 is the sole page-map defect found.
- **C2:** Printed pp. 46--49 support the system tuple, infinite executions,
  possibly infinite state set, nondeterministic R, exact sequential transition
  equation, exact one-processor concurrent transition equation, deterministic-
  notation qualification, atomicity choice, early enabled-processor fairness,
  R-star reachable-state reconstruction, clean-execution distinction, and the
  invariance/eventuality hierarchy. The strict clause is correctly `j>i`.
- **C3:** P1, literal P2 with `psi(s)`, the disclosed two-state strictness
  counterexample, A1--A2, R1--R4 (including the disclosed R4 hygiene repair),
  first-order-axiom standing, induction metarule (I), Theorem 1's expressiveness
  assumption, pointwise finite branching, Koenig-lemma dependency, and proof-
  sketch boundary all match printed pp. 49--50. The text correctly preserves
  the unreconciled strict/A2/P2/inclusive-F tension.
- **C4:** The sequential attachment and Floyd direction, finite-path A1/R2
  composition, full-versus-partial concurrent attachment, exact partial-
  attachment formula, sum/product/high-interaction qualifications, and global-
  invariant rather than model-checking standing are clean. SF-F4 concerns the
  omitted positive-capacity qualification and missing concrete calculation.
- **C5:** Recursive inclusive F/G semantics, Boolean standing, `FA := not G not
  A`, G1--G3, RT/RG/MP, F2--F3 formulas, Q1--Q4 logical forces, unrestricted-
  pure RG warning, finite action partition, I1/I2/E/N formulas, and N's
  restricted execution class match printed pp. 52--54. Visual inspection of
  printed p. 53 resolves (R) as `forall j (j >= i)`, equivalently every action
  occurs infinitely often. Theorem 2's pure-propositional strength/referrals,
  Theorem 3's statement/corollary, and the anti-conflation from later X/U are
  otherwise clean. SF-F1--SF-F3 are the remaining rule, proof-status, and
  quantifier-range defects.
- **C6:** The finite-state and finite-serial hypotheses, proper action-fair
  paths, Theorem 4's exact `G(p => Fq)` strength, disclosed reachable-pruning
  observation, internal-edge SCC criterion, P and restricted MRG, both Theorem
  5 clauses, Appendix A's external T2/T3 ownership and local six-step lemma,
  and Appendix B's two cited/outlined routes are source-faithful. The text does
  not turn Appendix B into a later LTL-to-Buchi construction or add a complexity
  classification.
- **C7:** The shared Part IX temporal definitions and integration surfaces keep
  modern X/U, safety/liveness, PSPACE, and LTL-to-Buchi results assigned to
  their later sources; no such result is attributed to Pnueli 1977. The
  bibliography entry and open ledger status are otherwise consistent. The
  cross-file repairs owed by SF-F1, SF-F2, SF-F4, and SF-F5 remain.
- **C8:** The prose is independently worded; the `leadsto`, partial-attachment,
  action-family, and proper-execution distinctions have definitions, standing,
  nonredundancy, and later use. The snapshot correctly keeps N-c-012.b review,
  IEEE comparison, N-c-012/Part IX admission, builds, visual handbook review,
  human review, and user acceptance separate. No later-result conflation was
  found. The five findings above prevent acceptance under I4 and C4--C7.

## Hash verification

Every round-two hash was checked before substantive review and rechecked after
the complete reading, immediately before this transcript was filed. Both passes
matched the charter:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `83C56ED3E9A17246150C727DCBCA4418F185FB166AA7AF6201D353CDF4467C07` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `757EBA2102F6D2A1A31299FB990C6D30718BBAE2EA213114AD75C4038463BF60` |
| `spec/research/p09-pnueli-1977-source-note.md` | `9BE7FC420BF1987191517960D4209A435B812F828C9A28476E94EBCA96904518` |
| `spec/research/p09-source-presentations-lot2-3.md` | `D920A431C50518FD6F976AAC5A98C4826270ED3BA8898D7CC73A60231FE92F5B` |

## Independence and process record

- Stable reviewer: `/root/schmidt_smolka_1991_research`, source-fidelity seat.
- Runtime model/version: the harness did not expose it.
- Read visually: wrapper physical p. 1 and every authority body page, printed
  pp. 46--57 (`page-02.png` through `page-13.png`), with the images controlling
  over OCR.
- Read in scope: the complete repaired manuscript range 370--902 and version
  boundary 1307--1314 (line 1314 completes the sentence begun in the assigned
  range), the entire source note, ledger lines 151--164, complete `Pnueli1977`
  bibliography entry, and all relevant temporal definition/integration surfaces
  in `logic-in-computer-science.tex`.
- I did not inspect `ledger.md`, `transcript/chair.md`, any round-one transcript
  (including my own), or either other round-two transcript. I did not contact
  another reviewer.
- I edited only this owned transcript. I ran no tests, automated checkers,
  repository scripts, TeX, handbook-PDF inspection, or builds. The only PDF/PNG
  inspection was the permitted source scholarship.

## Verdict

**REVISE**
