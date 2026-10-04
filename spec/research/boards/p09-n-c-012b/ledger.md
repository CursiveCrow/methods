# N-c-012.b review ledger

## Round-one result

All three independent seats returned **REVISE** on the original frozen
snapshot. No majority rule applies. The topic therefore remained open and the
chair admitted every supported defect into the repair ledger below.

- source fidelity: `transcript/r1-source-fidelity.md`, SHA-256
  `6A83F8907DF4B9B860C07662EA77B536DE6D05CB47DDF82A53F50E49840464B6`;
- mathematical/proof: `transcript/r1-mathematical-proof.md`, SHA-256
  `D1C1D81B96598512588EC611642BDB6B056E6AB488BC1A1221F81C1C465065C7`;
- adversarial publication/AGENTS:
  `transcript/r1-adversarial-publication.md`, SHA-256
  `3C5AD9CDD90D2D1FF719D46DAB51BC9B1453EFC40758BA3F10D94B99B10996E0`.

## Round-one merged repair obligations

The status “incorporated” means the working manuscript and evidence surfaces
contain a proposed repair. It does **not** mean a reviewer has accepted it.

| ID | Admitted obligation | Round-one provenance | Repair status |
|---|---|---|---|
| F01 | Correct the memorial-list description; state the rights boundary; identify the non-authoritative 13-page render, hash, and physical-to-printed page map. | SF-F1; AP-F1 | incorporated; fresh review required |
| F02 | Type the sequential and concurrent state spaces, maps, and transition equations; preserve that determinism is nonessential. | MP-F1; AP-F6 | incorporated; fresh review required |
| F03 | Define `R^0`, the finite powers, and reflexive-transitive `R*` before reachable-state use. | MP-F2 | incorporated; fresh review required |
| F04 | Define clean execution as invariant avoidance of illegal intermediate operations, distinguish it from partial correctness, and use the distinction. | AP-F6 | incorporated; fresh review required |
| F05 | Display literal P2 with `n>0` and current-state `psi(s)`; add a counterexample to its combination with strict `j>i`. | SF-F2; MP-F3; AP-F2 | incorporated; fresh review required |
| F06 | State ER's integer-induction metarule `(I)`, its proof-level standing, and its role before R4. | AP-F3 | incorporated; fresh review required |
| F07 | Define Theorem 1's “bounded nondeterminism” as pointwise finite branching, not a uniform bound. | MP-F4 | incorporated; fresh review required |
| F08 | Correct the Floyd direction: initial and per-instruction obligations are premises from which P1 yields invariance. | MP-F5 | incorporated; fresh review required |
| F09 | Give the exact partial-attachment representation, metalinguistic standing, distinction from full attachment, later use, and high-interaction caveat. | AP-F6 | incorporated; fresh review required |
| F10 | Give recursively typed satisfaction clauses for nested `F/G` formulas while keeping `H(t,p)` atemporal. | MP-F6 | incorporated; fresh review required |
| F11 | Supply F2--F3, Q1--Q4 at exact strengths, and RG's pure-system restriction without importing unprovided domain semantics. | SF-F3; MP-F7; AP-F4 | incorporated; fresh review required |
| F12 | Define the finite action partition and literal `j>=i` admitted-execution condition; keep it distinct from enabled-processor prose; state N only over that class. | SF-F4; MP-F8 | incorporated; fresh review required |
| F13 | State finite seriality, type Theorem 4's propositions, give the exact internal-edge SCC criterion and proof, and disclose the handbook reachable-state refinement. | MP-F9; AP-F5 | incorporated; fresh review required |
| F14 | Display `(P)` and `(MRG)` with its no-`P` side condition and nonredundancy example; restore Theorem 5's decidability and adequacy clauses. | SF-F5; MP-F10; AP-F5 | incorporated; fresh review required |
| F15 | Inventory Appendix A's T2/T3 formulas and corollaries, distinguish their external ownership, and reproduce the separate local lemma proof. | SF-F6 | incorporated; fresh review required |
| F16 | Replace premature closure claims with separate acquired/read, repaired, review-pending, IEEE-comparison-open, and larger-gates-open statuses. | SF-F7; MP-F11; AP-F7 | incorporated; fresh review required |

## Round-one coverage map

| Criterion | Source-fidelity seat | Mathematical/proof seat | Adversarial publication/AGENTS seat |
|---|---|---|---|
| C1 | REVISE: F01 | checked clean on its axis | REVISE: F01 |
| C2 | REVISE: F12 | REVISE: F02, F12 | REVISE: F04, F13 |
| C3 | REVISE: F05 | REVISE: F03, F05, F07 | REVISE: F05--F07 |
| C4 | ACCEPT on criterion | REVISE: F08 | REVISE: F09 |
| C5 | REVISE: F11--F12 | REVISE: F10--F12 | REVISE: F11--F12 |
| C6 | REVISE: F14--F15 | REVISE: F13--F14 | REVISE: F13--F14 |
| C7 | REVISE: F16 | REVISE: F16 | REVISE: F01, F14, F16 |
| C8 | REVISE: F05, F11--F12, F14--F16 | REVISE: F02--F03, F10, F12--F13 | REVISE: F04--F06, F09, F11, F13--F16 |

## Chair adjudication of one wording conflict

The mathematical seat paraphrased the p. 53 action-occurrence restriction
with `j>i`. Direct visual inspection of printed p. 53 shows the tail condition
`j>=i`. Its exact positive form is therefore

\[
\forall a\in\mathcal A\ \forall i\ge0\
\exists j\ge i\ a(s_j,s_{j+1}).
\]

This preserves the source rather than the reviewer's paraphrase. The action
family is recorded as a finite partition, and the necessity counterexample now
uses a nonempty designated action in such a partition.

## Round-two result

All three independent seats returned **REVISE** on the round-two repaired
snapshot. No finding was outvoted, and no round-two acceptance was recorded.

- source fidelity: `transcript/r2-source-fidelity.md`, SHA-256
  `06AAEBFB618AC0B83F3476774C4D8B6675C9AA75B3C82819D6F7EC5F85C3A95D`;
- mathematical/proof: `transcript/r2-mathematical-proof.md`, SHA-256
  `90C3CCA3749C2881D60795B987A1D0E332170B7FD320EE679BDC20B6A8609F7B`;
- adversarial publication/AGENTS:
  `transcript/r2-adversarial-publication.md`, SHA-256
  `29F002D4DB172D1CEE0EA5CDB0F38F4D836536CC1715812342ABCA0326B0EE52`.

## Round-two merged repair obligations

As above, “incorporated” records only a proposed repair in the working
surfaces. Each item remains open until all three seats accept the same new
snapshot.

| ID | Admitted obligation | Round-two provenance | Repair status |
|---|---|---|---|
| F17 | Type the sequential attachment by locations, declare the initial state and location-indexed assertion family, and type both partial-attachment families over enumerated location sets. | R2-MP-F1 | incorporated; fresh review required |
| F18 | Use a positive integer capacity with a name distinct from the next-location map; state the characteristic and semaphore maps; print all three invariants and the mutual-exclusion, bound, and two-case deadlock deductions. | R2-SF-F4; R2-MP-F2 | incorporated; fresh review required |
| F19 | Print the derived rules DI and DN with universal closures, derived standing, and their use in Example 2. | R2-SF-F1 | incorporated; fresh review required |
| F20 | State that Theorem 3's complete local proof is only the printed skeletal instruction and that no individual ER derivations appear. | R2-SF-F2 | incorporated; fresh review required |
| F21 | Preserve Q1--Q4's formula-metavariable range as source-unresolved; label atemporal later use as handbook policy rather than source restriction. | R2-SF-F3 | incorporated; fresh review required |
| F22 | Move F2--F3 to their exact printed-p. 52 locator in the source note. | R2-SF-F5; R2-AP-F1 | incorporated; fresh review required |
| F23 | Disclose that extending P2's rank-predicate domain to zero is a handbook typing repair while `n>0` remains the rule-instance restriction. | R2-AP-F2 | incorporated; fresh review required |
| F24 | Record Theorem 1's deadlock-vacuity gap under the paper's infinite-execution definition without silently adding seriality or changing the theorem. | R2-AP-F3 | incorporated; fresh review required |
| F25 | Remove the undefined and redundant phrase “maximal execution”; state the direct seriality consequence instead. | R2-AP-F4 | incorporated; fresh review required |
| F26 | State Appendix B's exact language recursion, define every local notation, avoid the action/automaton symbol collision, and assign the acceptor, closure, and inclusion-decision facts to their external owners. | R2-AP-F5 | incorporated; fresh review required |

## Round-three result

The source-fidelity seat returned **ACCEPT**, while the mathematical/proof and
adversarial publication/AGENTS seats returned **REVISE**. Unanimity was not
reached, so the source-fidelity acceptance does not close the topic and every
supported defect below is admitted.

- source fidelity: `transcript/r3-source-fidelity.md`, SHA-256
  `E3D8AAE58BF4EB7A9AF41237B343BB3BB2688ED3F4E865E83870B0D694253FAB`;
- mathematical/proof: `transcript/r3-mathematical-proof.md`, SHA-256
  `69EF5AC00ABC43C7AF19C0D6CC888DE673343B26A93A13BACC35917B86683225`;
- adversarial publication/AGENTS:
  `transcript/r3-adversarial-publication.md`, SHA-256
  `4099E3A76FC2912518ED849C7C25C71780273C53695D66F31865CEBBE543B1B5`.

## Round-three merged repair obligations

| ID | Admitted obligation | Round-three provenance | Repair status |
|---|---|---|---|
| F27 | Rename the raw-path counterexample's second action relation so it does not reuse the producer--consumer load symbol `b` at a different type. | R3-AP-F1 | incorporated; fresh review required |
| F28 | Give the full two-process attachment an exact typed formula, metalinguistic standing, nonredundancy relative to partial attachment, and immediate use in the size comparison. | R3-AP-F2 | incorporated; fresh review required |
| F29 | State exactly which source-supplied indicator implications connect producer--consumer locations and waits to `m_i,r_i,s_i`; do not pretend that unprinted support sets were reconstructed. | R3-AP-F3 | incorporated; fresh review required |
| F30 | Type a state assertion at first use and replace the redundant one-off phrase “pure homogeneous system” by the already defined pure propositional basis. | R3-AP-F4 | incorporated; fresh review required |
| F31 | Distinguish arbitrary-start infinite paths satisfying the action condition from initial-state proper executions; define restricted system validity before Theorems 4--5 and use the correct path phrase in the SCC argument. | R3-MP-F1 | incorporated; fresh review required |
| F32 | Parameterize the attachment-size comparison: sum versus product for two processes, possible exponential growth only with varying process count; qualify global invariants as avoiding the full cross-product attachment while retaining initial and per-transition checks. | R3-MP-F2 | incorporated; fresh review required |
| F33 | Identify the internal-edge SCC formula and both-direction argument as a handbook formalization and proof of the source's informal component-label sentence. | R3-AP-F5 | incorporated; fresh review required |
| F34 | State that Theorem 5's adequacy clause is asserted without a printed general derivation and that Appendix B supplies two semantic decision routes only for its decidability clause. | R3-AP-F6 | incorporated; fresh review required |
| F35 | Keep Appendix B's ownership exact: Pnueli locally asserts `A_Sigma` without construction or proof; reference 32 accompanies the imported omega-regular/closure machinery; reference 33 supports the inclusion decision. | R3-MP-F3; R3-AP-F7 | incorporated; fresh review required |

## Round-four result

The source-fidelity seat returned **ACCEPT**, while the mathematical/proof and
adversarial publication/AGENTS seats returned **REVISE**. Unanimity was not
reached. The source-fidelity acceptance does not close the topic, and every
supported defect below is admitted.

- source fidelity: `transcript/r4-source-fidelity.md`, SHA-256
  `A85A85FF4888B2906262335712004CADC7592935F93ECD71F749FD6DFB3CF00A`;
- mathematical/proof: `transcript/r4-mathematical-proof.md`, SHA-256
  `58BF3947AAE46DAAE66AD53D12C8A93EC0C51175C464A3BC51B0D67E3F3DE891`;
- adversarial publication/AGENTS:
  `transcript/r4-adversarial-publication.md`, SHA-256
  `194BFBC11A89F71AE5D22AB9395545E1591D8BBF984E333FFDF5AC8D80B8563F`.

## Round-four merged repair obligations

| ID | Admitted obligation | Round-four provenance | Repair status |
|---|---|---|---|
| F36 | Disclose that totalizing P2's rank predicate at zero does not make the rule sound: give the independent false-at-zero counterexample, distinguish it from the strict-future defect, and identify the unprinted boundary condition a sound inclusive reading would need. | R4-MP-F1 | incorporated; fresh review required |
| F37 | Type R4 and metarule I as parameterized families of state assertions, define their pointwise existential assertions, and state R4's uniform-arbitrary-variable and consequent-independence conditions without inventing a new tense constructor. | R4-MP-F2 | incorporated; fresh review required |
| F38 | Add the source-supplied implication that `m_i=1` means process `i` is in its critical section and therefore is not waiting on a semaphore operation; retain the no-invented-support-set boundary. | R4-MP-F3; R4-AP-F1 | incorporated; fresh review required |
| F39 | Report Theorem 2's completeness claim as model-class-sensitive: the S4 referral does not establish completeness for the preceding linear-execution semantics, and the paper does not reconcile those readings. | R4-MP-F4 | incorporated; fresh review required |
| F40 | Type Appendix B's atomic language by identifying states with one-letter words before using it as the left factor of prefix concatenation. | R4-MP-F5 | incorporated; fresh review required |

## Round-five result

The source-fidelity and mathematical/proof seats returned **ACCEPT**, while the
adversarial publication/AGENTS seat returned **REVISE**. Unanimity was not
reached. Neither acceptance closes the topic, and all three supported
adversarial findings below are admitted.

- source fidelity: `transcript/r5-source-fidelity.md`, SHA-256
  `98EC60EA943248026941F820117A30EE24FB9A8761EA25ADC00253C31223554C`;
- mathematical/proof: `transcript/r5-mathematical-proof.md`, SHA-256
  `F7F025E3058E976CE36B4C9ED2ADC95E5454BA3C0246CF54E5D19101671D3BE3`;
- adversarial publication/AGENTS:
  `transcript/r5-adversarial-publication.md`, SHA-256
  `B95CB8A37F232EF3536C213D12BA9D3729B35074FC567672AB1674C8FCDF6FCE`.

## Round-five merged repair obligations

| ID | Admitted obligation | Round-five provenance | Repair status |
|---|---|---|---|
| F41 | Disclose the independent unreachable-state failure in Theorem 1's first proof step: initial-state temporal implication does not imply its pointwise arbitrary-state assertion. Give the serial counterexample and state the alternative missing reachability or semantic boundaries without choosing one silently. | R5-AP-F1 | incorporated; fresh review required |
| F42 | Replace the partially specified S4 frame by a complete three-world Kripke model, including its reflexive-transitive relation, full valuation, and the fact that the root satisfies neither atom. | R5-AP-F2 | incorporated; fresh review required |
| F43 | Replace the unproved description of the later action-occurrence condition as “stronger” by a neutral distinction; no ordering follows without a typed processor/action/enabledness correspondence. | R5-AP-F3 | incorporated; fresh review required |

## Round-six result

All three independent seats returned **ACCEPT** on the same round-six frozen
snapshot. No majority inference was used.

- source fidelity: `transcript/r6-source-fidelity.md`, SHA-256
  `EB0A98970CE3C7D8D4CA2F97CD0B1E98BE24C9B8EDDBE549AB5CBC85A6CD8971`;
- mathematical/proof: `transcript/r6-mathematical-proof.md`, SHA-256
  `2D11A37E140587C24D0FE1C8E55EB297AF3940C8F2955BE179003519F77BC003`;
- adversarial publication/AGENTS:
  `transcript/r6-adversarial-publication.md`, SHA-256
  `59D083B7C6D2907D41D18B6959E08BBC668A7A8CD20F39873461129795F83EB7`.

Every seat independently reread the wrapper and all printed pages 46--57,
rechecked the complete frozen artifact scope, and found F27--F43 clean. Their
criterion-level rereads also confirmed the earlier F01--F26 repairs. The
historical row statuses above record the state before round-six review and are
superseded by this unanimous result. The durable admission record is
`../../p09-n-c-012b-independent-review-record.md`.

## Current disposition

The three independent manuscript-content review gates and body-level reader
reconstruction for `N-c-012.b` are closed on the exact round-six identities in
the charter and independent review record. The IEEE-direct comparison,
`N-c-012.c`, `N-c-012.d`, `N-c-012` as a whole, Part IX admission, every build
and visual gate, human review, final-book completion, and user acceptance
remain open.
