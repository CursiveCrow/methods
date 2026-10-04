# Round-two blind adversarial publication/AGENTS review: N-c-012.b

**Seat:** `/root/mcnaughton_1966_research`  
**Role:** adversarial publication and AGENTS compliance  
**Verdict:** **REVISE**

## Scope, independence, and method

I read the board charter before any substantive artifact review, including its
appended round-two snapshot. I verified all eight round-two SHA-256 identities
before review and reverified them immediately before filing this transcript. I
visually read the complete scholarly render of the authority: physical pages
2--13, corresponding to every printed page 46--57. I also inspected physical
page 1 solely to verify the May 1981 wrapper claim.

I then read the complete repaired N-c-012.b manuscript scope at
`handbook/parts/p09/presentations/n-c-012.tex:370--902` and the complete version
boundary continuing through lines 1307--1314, the complete source note, ledger
lines 151--164, the complete `Pnueli1977` bibliography record, and the relevant
shared temporal-logic/automata surface in
`handbook/parts/p09/logic-in-computer-science.tex:599--824`, together with the
chapter's source-standing paragraph. I inspected enough of the adjacent Kamp,
GPSS, Sistla--Clarke, and Alpern--Schneider boundaries to test for notation and
version collisions, without reviewing those presentations on their own merits.

I did **not** inspect `ledger.md`, `transcript/chair.md`, any round-one
transcript (including my own), or either other round-two transcript. I did not
contact another reviewer. I made no manuscript, source-note, ledger,
bibliography, or shared-surface edit. I ran no tests, automated checkers,
repository scripts, TeX, handbook-PDF inspection, or builds. The only edit made
is this owned transcript. Runtime model/version was not exposed by the harness.

## Steel-man

The repaired presentation is unusually strong on the central source problem.
It types the transition models; preserves the printed strict `j>i` definition;
prints literal P2 with its current-state target; supplies a concrete
counterexample instead of silently repairing the paper; separates A2,
inclusive `F`, and Theorem 3; restores the ER induction metarule and theorem
hypotheses; reconstructs the partial-attachment formula; gives recursive `F/G`
semantics, F2--F3, Q1--Q4, and the RG restriction; reads the p. 53 fairness tail
with the correct inclusive `j >= i`; makes N depend on that execution-class
restriction and supplies a nonempty-action countermodel without it; and gives
the correct internal-edge SCC criterion and P/MRG distinction. Those repairs
survive adversarial comparison with the printed pages. The remaining defects
are narrow, but the charter requires exact locators, explicit source/handbook
repair boundaries, and strict compliance with the five-part technical-name
rule, so they preclude acceptance.

## Findings

### AP-F1 — must-fix — the source note gives a false printed-page locator for F2--F3

- **Location:** `spec/research/p09-pnueli-1977-source-note.md:49--50`.
- **Claim:** The visual-locator table places F2--F3 in its printed pp. 53--54
  row.
- **Evidence:** The formulas `A => FA` (F2) and `FFA => FA` (F3) are visibly
  printed at the lower right of printed p. 52 (physical render page 8), directly
  after RG and MP. Printed p. 53 begins with the continuation of the Kb/S4
  discussion and then Theorem 2, Q1--Q4, and the non-pure axioms. The manuscript
  itself more accurately groups this material under pp. 52--53 at
  `n-c-012.tex:702--730`.
- **Harm:** The note is the source-critical audit trail, and C1/I3 require exact
  printed locators. A reader following the table to p. 53 will not find F2 or
  F3.
- **Exact correction:** Move `F2--F3` from the `53--54` row into the `51--52`
  row (preferably identifying p. 52), leaving Q1--Q4 and the later material in
  the `53--54` row.

### AP-F2 — must-fix — P2's zero-rank typing repair is performed but not disclosed as a repair

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:498--511` and
  `spec/research/p09-pnueli-1977-source-note.md:138--150`; the ledger calls this
  reconstruction "literal P2" at
  `spec/research/p09-source-presentations-lot2-3.md:157`.
- **Claim:** The handbook takes
  `A:S x N -> Prop`, explicitly includes `0` in `N`, and restricts displayed
  rule instances to `n>0`, while describing the intervention only as making
  unprinted universal closures explicit.
- **Evidence:** Printed p. 49 says that `A(s,n)` depends on "a natural number
  n > 0", but the second P2 premise itself prints `A(s',n-1)`. Its `n=1`
  instance therefore requires `A(s',0)`. Taking A's second argument over a
  natural-number set containing zero is a sensible way to type the printed
  expression, but that domain repair is not literally supplied by the printed
  sentence.
- **Harm:** The current wording obscures a genuine source/handbook boundary
  precisely where the presentation claims literal fidelity. It also leaves a
  reader unable to tell whether `n>0` restricts A's domain, the rule instances,
  or both.
- **Exact correction:** At the P2 display, add: "Printed p. 49 says `n>0` but
  also uses `A(s',n-1)`; to type the `n=1` instance, the handbook takes A over
  natural numbers including zero and retains `n>0` as the rule-instance
  restriction. This is a handbook typing repair, not an additional printed
  clause." Record the same boundary in the source note and replace the
  ledger's unqualified "literal P2" wording by "the literal formula, with the
  disclosed zero-rank typing repair."

### AP-F3 — must-fix — the Theorem 1 recap omits a proof-sketch gap caused by deadlock and the paper's infinite-execution definition

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:580--596`,
  `spec/research/p09-pnueli-1977-source-note.md:193--206`, and the Theorem 1
  status sentence at
  `spec/research/p09-source-presentations-lot2-3.md:157`.
- **Claim:** The reconstruction identifies assertion-language expressiveness
  and pointwise finite branching as the proof sketch's operative assumptions
  and repeats its base claim `P(s,0) => psi(s)` without identifying any further
  gap.
- **Evidence:** Printed p. 47 defines an execution as an infinite sequence.
  Printed p. 50 defines `P(s,n)` in words as "Every execution starting with s"
  reaching a psi-state within n steps, and then treats `P(s,0) => psi(s)` as
  valid. No seriality/no-deadlock assumption is made in this general theorem;
  seriality is introduced only in the finite-state specialization on printed
  p. 55. In the one-state system `S={d}`, `R` empty, and `psi(d)` false, there
  is no infinite execution from d, so the displayed universal reading of
  `P(d,0)` is vacuously true while `psi(d)` is false. Thus step 4 needs either
  existence of an execution from each state or a nonvacuous finite-prefix or
  recursive definition of P.
- **Harm:** The current prose makes the proof architecture look complete modulo
  only expressiveness and finite branching. A skeptical reader can refute the
  printed base step under the very execution semantics the presentation has
  just reconstructed. This is a C3 proof-status defect, independent of the
  already disclosed strictness conflicts.
- **Exact correction:** Do not silently add seriality to Theorem 1. After the
  printed definition of P, disclose that the sketch's base step additionally
  requires either seriality/existence of an infinite execution from each state
  or a repaired nonvacuous finite-prefix/recursive definition of P, neither of
  which the source states there. Carry that source-defect boundary into the
  source note and ledger theorem-status sentence.

### AP-F4 — must-fix — `maximal execution` is undefined, redundant, and inconsistent with the established execution standing

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:799--805`.
- **Claim:** After stating seriality, the text says, "Thus every maximal
  execution is infinite."
- **Evidence:** The presentation already defines `execution` at lines 389--395
  to mean an infinite sequence. It never defines a prefix order, a maximal
  finite path, or the new phrase `maximal execution`. Printed p. 55 instead says
  that no halting states or deadlocks are assumed "so that only infinite
  execution paths have to be considered."
- **Harm:** The one-off phrase violates I7: it has no necessity, definition,
  standing, nonredundancy, or later use. It can also mislead the reader into
  thinking that the handbook has introduced a second, possibly finite notion
  of execution.
- **Exact correction:** Replace the sentence by the eliminable consequence of
  the displayed formula: "Thus no state is terminal; every finite R-path can
  be extended to an infinite execution." No new name is needed.

### AP-F5 — must-fix — Appendix B introduces an under-typed infinite-word automaton and an undefined language class, while omitting the printed recursion

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:890--900`,
  `spec/research/p09-pnueli-1977-source-note.md:401--412`, and
  `spec/research/p09-source-presentations-lot2-3.md:159`. The earlier action
  family is already named `mathcal A` at `n-c-012.tex:732--750`; the relevant
  shared automata definition at
  `handbook/parts/p09/logic-in-computer-science.tex:663--686` defines Buchi,
  parity, and Rabin acceptance but never defines "omega-regular language."
- **Claim:** The presentation says to build a "finite-state automaton
  `mathcal A_Sigma`" for proper executions, assign an "omega-regular language"
  `L(W)` recursively, and decide inclusion. It supplies neither the
  infinite-word acceptance condition nor an eliminable definition of the
  named language class; it also reuses the already occupied calligraphic-A
  glyph for a different type of object.
- **Evidence:** Printed p. 57 explicitly gives the source's status and content:
  it asserts existence of an automaton `A_Sigma` accepting proper executions,
  cites reference [32] for the omega-regular class, prints the recursive clauses
  for atomic p, negation, conjunction, disjunction, F, and G, and cites [33] for
  decidability of the final inclusion problem. It does not print an automaton
  acceptance tuple or prove the cited closure and inclusion results. The
  manuscript omits those printed clauses while adopting the undefined class
  name as if it were locally typed.
- **Harm:** A first-time reader cannot determine what kind of finite automaton
  accepts an infinite proper execution, what "omega-regular" eliminates to, or
  why `L(mathcal A_Sigma) subseteq L(W)` is decidable. This violates C6 and I7,
  and the `mathcal A`/`mathcal A_Sigma` collision obscures the difference
  between the action partition and the automaton.
- **Exact correction:** Preserve the historical boundary without importing a
  later LTL-to-Buchi construction: (1) use a fresh typed symbol such as
  `mathcal M_Sigma`, while noting that the source prints `A_Sigma`; (2)
  transcribe the source's six recursive language clauses in independently
  worded form, defining the atomic-state set and prefix concatenation used in
  them; and (3) state explicitly that p. 57 supplies no acceptance tuple and
  delegates the infinite-word automaton/class facts and inclusion decision to
  references [32]--[33]. Either provide an already established eliminable
  definition for "omega-regular" or report it only as the source's externally
  defined term, not as a new local handbook name.

## Criterion-by-criterion coverage

- **C1 — REVISE because of AP-F1; otherwise checked clean.** The DOI, title,
  author, venue, pp. 46--57, NYU memorial publication-list route, compressed and
  decompressed identities, 13-page local render, physical-to-printed page map,
  May 1981 wrapper/non-edition boundary, author-hosted-versus-IEEE distinction,
  and no-inferred-republication-right language all match the inspected objects.
  The IEEE-direct comparison remains explicitly open.
- **C2 — checked clean.** The dynamic system and possibly infinite state set,
  infinite executions, nondeterministic R, typed sequential N/T model, typed
  concurrent interleaving, one-statement atomicity/refinement qualification,
  early enabled-processor fairness prose, later nonidentified action condition,
  reflexive R-star reconstruction, invariant standing, clean execution, mutual
  exclusion, deadlock, accessibility, responsiveness, and excluded
  higher-order/quantitative specification cases match printed pp. 46--49.
- **C3 — REVISE because of AP-F2 and AP-F3; otherwise checked clean.** P1,
  literal current-state P2, the two-state strict-future counterexample, A1--A2,
  R1--R4, R4 variable hygiene, first-order axioms, metarule I, pointwise rather
  than uniform finite branching, expressiveness, the Koenig-lemma architecture,
  and the proof-sketch label all match pp. 49--50. The strict-definition/A2/P2
  source defects remain visibly source defects.
- **C4 — checked clean.** The full sequential attachment, initial and
  per-instruction Floyd obligations as premises to P1, finite A1/R2 path
  composition, full-versus-partial concurrent attachment, exact two-family
  partial formula, sum/product/high-interaction qualification, global
  invariants, and producer--consumer conclusions match pp. 50--52.
- **C5 — checked clean apart from AP-F1's note locator.** H is kept
  metalinguistic; recursive F/G and Boolean semantics are inclusive; no X or U
  is imported; G1--G3, F2--F3, RT/RG/MP, Q1--Q4 and their implication/equivalence
  strengths are exact; pure RG and its restriction warning are separated; the
  action family is a finite partition; the literal p. 53 tail is
  `forall i exists j >= i`, not `j>i`; I1, I2, E, and N have the correct
  directions; N is restricted to the fair execution class and the nonempty
  action countermodel is sound; Theorems 2--3 and their proof/referral limits
  are not inflated.
- **C6 — REVISE because of AP-F4 and AP-F5; otherwise checked clean.** Finite
  seriality, the source's proper action-fair execution, the p/q state-assertion
  renaming, reachable-state-pruning disclosure, internal-action-edge SCC
  criterion and both directions, P, MRG and its counterexample, and both
  Theorem 5 clauses are correct. Appendix A correctly leaves T2/T3 and their
  corollaries with reference [23] while reproducing only Pnueli's local six-step
  lemma proof. Appendix B is correctly kept distinct from a later
  LTL-to-Buchi translation or complexity result, but its current terminology
  and omitted printed recursion are not yet publication-ready.
- **C7 — REVISE because AP-F1 and AP-F5 propagate across the note/ledger.** The
  bibliography record is otherwise coherent with the source object. The shared
  Part IX section's modern non-strict LTL, GPSS's strict operators,
  Sistla--Clarke's later operator-sensitive complexity, Alpern--Schneider's
  semantic classes, and the later automata constructions remain separate from
  Pnueli's historical calculus. No later X/U grammar, safety/liveness syntax,
  PSPACE result, or complete Buchi translation is attributed to Pnueli 1977.
- **C8 — REVISE because AP-F2--AP-F5 violate the required repair/terminology
  discipline.** The prose is otherwise independently worded, definitions
  usually precede use, strict and inclusive variants remain separate, and all
  review/admission/build/human/user gates remain honestly open.

## Charter-invariant audit

- **I1--I4:** Review method and primary-source coverage complied; exactness
  failures are AP-F1--AP-F3.
- **I5:** Checked clean. Strict `j>i`, A2, inclusive F, and Theorem 3's
  `p => Fq` representation are all separately visible and unreconciled.
- **I6:** Checked clean. No later X/U grammar, Buchi translation,
  safety/liveness syntax, or PSPACE classification is retrojected.
- **I7:** Fails AP-F4 and AP-F5; AP-F2 also needs explicit repair standing.
  Other locally introduced names and symbols were checked for necessity,
  exact definition or rule, standing, nonredundancy, and actual use. In
  particular `leadsto`, the rank predicate, ER, metarule I, partial attachment,
  H, the action family, proper execution, P, and MRG meet the rule.
- **I8:** Checked clean. Author-copy reconstruction and IEEE-file comparison
  remain distinct.
- **I9:** Checked clean. The ledger says fresh unanimous review is pending and
  does not claim majority closure.
- **I10:** Checked clean. The rest of N-c-012, Part IX admission, builds, visual
  gates, final-book completion, human review, user acceptance, and the
  publisher-file comparison remain open.

## Premortem

Assume this snapshot shipped and later failed scholarly review. The most likely
failure is not one of the headline temporal formulas: those are now unusually
careful. It is a source-critical reader following the note to p. 53 and finding
F2--F3 on p. 52, then noticing that "literal" P2 silently changes the rank
domain and that the Theorem 1 base step is vacuous at a deadlock. A second
failure mode is a first-time automata reader reaching Appendix B and being
unable to type the automaton or eliminate "omega-regular," while the same
calligraphic A already denotes the action partition. An ordinary checklist
could miss all of these because it would mark the named formulas and theorems
as present. The page-by-page locator audit, zero-rank substitution, deadlock
countermodel, and five-part name audit are what exposed them.

## Verified round-two hashes

Verified before substantive review and reverified immediately before filing:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex` — `83C56ED3E9A17246150C727DCBCA4418F185FB166AA7AF6201D353CDF4467C07`
- `handbook/parts/p09/logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib` — `757EBA2102F6D2A1A31299FB990C6D30718BBAE2EA213114AD75C4038463BF60`
- `spec/research/p09-pnueli-1977-source-note.md` — `9BE7FC420BF1987191517960D4209A435B812F828C9A28476E94EBCA96904518`
- `spec/research/p09-source-presentations-lot2-3.md` — `D920A431C50518FD6F976AAC5A98C4826270ED3BA8898D7CC73A60231FE92F5B`

## Final verdict

**REVISE.** The central reconstruction is strong, but AP-F1--AP-F5 are
substantive under the charter's exact-locator, proof-boundary, and five-part
technical-name rules.
