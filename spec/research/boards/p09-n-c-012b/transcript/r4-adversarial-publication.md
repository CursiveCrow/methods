REVISE

# Round-four adversarial publication/AGENTS review: N-c-012.b

## Seat, independence, and method

- Seat: `/root/mcnaughton_1966_research`, adversarial publication and AGENTS-compliance review.
- Runtime model/version: the harness did not expose an exact runtime model/version.
- I read the charter before substantive review, including the round-four repaired snapshot, C1--C8, I1--I10, and mandatory checks F27--F35.
- I did not inspect `ledger.md`, `transcript/chair.md`, any round-one, round-two, or round-three transcript, or either other round-four transcript. I did not contact another reviewer.
- I made no manuscript, source-note, source-presentation-ledger, bibliography, authority, or shared-surface edit. This transcript is the only file I created.
- The review used exact line reading, visual source-image reading, mathematical/proof analysis, adversarial inversion, and SHA-256 identity checks only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build.

## Exact identities verified before substantive review

All round-four identities matched the charter before substantive review:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `B015988618D84AA836D35D3AA0A1D484438C65910B78BB94CB74577A9FB02C9E` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `C3EE541610841D57A6FB6729C482919431660CFF896276FDABB330D9D21ADE54` |
| `spec/research/p09-source-presentations-lot2-3.md` | `32F11A80F21E9C33AF3E664EBDEEB778E36B4B81E7A772C5BD91589090962AA0` |

## Authority read visually

The image render, not OCR or memory, controlled this review. I visually read the physical-page-1 archival wrapper for provenance and every printed body page 46--57:

- wrapper: title, Amir Pnueli, and archival date “May 1981”;
- p. 46: summary, invariance/eventuality motivation, and the opening transition-system discussion;
- p. 47: dynamic discrete system, sequential and concurrent transition equations, atomic interleaving, and enabled-processor scheduling prose;
- p. 48: explicit-time motivation, accessible states, invariance, partial correctness, clean execution, mutual exclusion/deadlock, and the beginning of strict temporal implication;
- p. 49: strict temporal implication, total correctness/accessibility/responsiveness, specifications left outside the two basic cases, P1, literal P2, and the beginning of ER;
- p. 50: ER, induction metarule I, Theorem 1 and its proof sketch, sequential attachment/Floyd conditions, and finite-path composition;
- p. 51: concurrent full and partial attachment, their complexity discussion, global invariants, and the producer--consumer calculation;
- p. 52: completion of the producer--consumer deadlock argument and inclusive future-tense semantics, G1--G3, F2--F3, RT/RG/MP, and the RG warning;
- p. 53: Theorem 2, Q1--Q4, the finite action partition, the literal action-occurrence tail condition, and I1/I2/E/N;
- p. 54: DI/DN, Theorem 3, its corollary, and the mutual-exclusion accessibility example;
- p. 55: finite-state serial setting, proper executions, Theorem 4 and SCC route, P/MRG, Theorem 5, and the start of the discussion;
- p. 56: the temporal-device scope discussion, endogenous/exogenous comparison, and references 1--20;
- p. 57: references 21--33, Appendix A, and Appendix B's two decision routes and three distinct attribution points.

## Strongest case for acceptance

The repaired snapshot is source-critical rather than celebratory. It correctly types the sequential and concurrent transition models, expands the reflexive zero-step case of the source's `R*`, separates clean execution from partial correctness, preserves the strict-implication/P2/A2/inclusive-F/Theorem-3 tension instead of normalizing it, discloses Theorem 1's deadlock-vacuity gap, and distinguishes source assertions from handbook repairs. The future-only calculus, action restriction, finite-state validity, SCC reconstruction, P/MRG, Theorem 5, and Appendices A--B now have unusually careful proof-ownership boundaries. The provenance, rights limitation, author-copy/IEEE boundary, neighboring GPSS and modern-LTL boundaries, and open review status are also accurately narrow. Those repairs survive adversarial checking except for the single load-bearing omission below.

## Finding

### AP-F1 — must-fix — one producer--consumer inference uses the unstated converse of the listed indicator fact

**Locations.**

- `handbook/parts/p09/presentations/n-c-012.tex:731-739` says that it is listing every location-indicator fact used. It states that simultaneous critical-region membership gives `m_1=m_2=1`, but it does not state the converse implication from `m_i=1` to critical-region membership.
- `handbook/parts/p09/presentations/n-c-012.tex:756-758` derives that the other process has indicator value one and then concludes that the other process is in its critical region. That conclusion uses precisely the omitted converse.
- `spec/research/p09-pnueli-1977-source-note.md:288-294` makes the same purportedly exhaustive list and omits the converse; `spec/research/p09-pnueli-1977-source-note.md:309-311` then uses it.
- `spec/research/p09-source-presentations-lot2-3.md:159` consequently overstates that the reconstruction “states exactly the location-indicator and semaphore facts used.”
- Authority evidence: printed pp. 51--52. The printed proof first obtains the other processor's `m`-value as one and then explicitly says that this means that processor is in its critical section. Thus the source supplies the implication, but the reader reconstruction has not stated it.

**Claim and evidence.** The reconstruction's listed direction

`process i is in its critical region  =>  m_i=1`

does not license the direction actually used later,

`m_i=1  =>  process i is in its critical region`.

Calling the `m_i` merely a location indicator and saying that it is one on “some control locations” does not identify those support locations as exactly the critical-region locations. The inference is therefore not derivable from the displayed invariant plus the reconstruction's stated indicator facts.

**Publication harm.** This leaves a gap in the advertised proof of absence of deadlock and makes the cross-file “all facts used” claims false. It directly leaves mandatory fresh check F29 unresolved and violates I4's exact-premise requirement; it also prevents C4 and C7 from being checked clean. At the terminology level, the standing of the `m_i` indicators is not exact enough for their later use, so I7 is not satisfied locally.

**Smallest exact correction.** In the manuscript's indicator-fact list, state the source-supplied support fact in the direction actually used—preferably, for each process `i`, that `m_i=1` exactly when its control location is in the critical region, if the reconstruction intends the characteristic-function reading. At minimum, explicitly add `m_i=1 => process i is in its critical region` alongside the already stated forward direction. Make the same correction in the source note. Then retain or update the ledger's “exact facts used” sentence only after those two evidence surfaces agree. No rule, invariant, or program semantics needs to change.

## Criterion-by-criterion coverage

- **C1 — checked clean.** The identity, DOI, printed pagination, wrapper/body map, first-party route, derived-render standing, rights limitation, and open IEEE-direct comparison agree across the presentation, note, ledger, and `Pnueli1977` entry.
- **C2 — checked clean.** The model, nondeterminism, exact transition types, atomicity, initial-state infinite executions, reflexive reachability repair, clean execution, strict temporal implication, and separation of enabled-processor prose from the later action condition are present and source-faithful.
- **C3 — checked clean.** P1, literal P2, the zero-rank typing repair, current-state target, strict-future counterexample, ER A1--A2/R1--R4, R4 hygiene, metarule I, Theorem 1's exact expressiveness/finite-branching assumptions, sketch standing, and deadlock-vacuity gap are all explicit.
- **C4 — fails AP-F1; otherwise checked clean.** Sequential attachment and its Floyd obligations, finite-path ER composition, typed full and partial attachment, two-process sum/product versus varying-process exponential size, and retained invariant proof obligations are coherent. The producer--consumer arithmetic is otherwise exact, but its deadlock inference lacks the stated reverse `m_i` implication.
- **C5 — checked clean.** Recursive inclusive F/G semantics, absolute present, G1--G3, F2--F3, RT/RG/MP, Q1--Q4 and unresolved schema range, exact action partition and `j>=i` condition, I1/I2/E/N, derived DI/DN, and Theorems 2--3 retain their printed strength and referral/skeletal-proof status.
- **C6 — checked clean.** Finite seriality, arbitrary-start action-condition paths, initial-state proper executions, restricted validity, Theorem 4, the disclosed handbook SCC formula and two-way proof, P/MRG, both Theorem 5 clauses, unproved adequacy, Appendix A ownership, and Appendix B's decision-only boundary are exact.
- **C7 — fails AP-F1; otherwise checked clean.** The presentation, note, ledger, three relevant bibliography entries, and shared Part IX surface agree on source identity, notation and historical/modern boundaries. AP-F1 is the remaining cross-file inconsistency.
- **C8 — fails AP-F1; otherwise checked clean.** The prose is independently worded; source repairs and external ownership are labelled; definitions generally precede use; and no later X/U, LTL-to-Büchi, safety/liveness, or PSPACE result is retrojected. AP-F1 is the remaining exact-definition/later-use failure.

## Invariant-by-invariant coverage

- **I1:** obeyed; scholarship/prose review only.
- **I2:** obeyed; every frozen identity matched before and after substantive review.
- **I3:** obeyed; wrapper inspected for provenance and every printed page 46--57 visually read.
- **I4:** not satisfied because of AP-F1; all other checked types, quantifiers, premises, side conditions, theorem strengths, proof statuses, and referral boundaries are exact.
- **I5:** satisfied; strict `leadsto`, A2, inclusive F, and Theorem 3 remain visibly distinct and the inconsistency is disclosed.
- **I6:** satisfied; no later operator grammar, automata translation, safety/liveness syntax, or complexity classification is attributed to the 1977 paper.
- **I7:** not satisfied locally for the `m_i` indicator standing used in AP-F1; the other introduced labels and notations meet necessity, exact definition/axiom, standing, nonredundancy, and later-use requirements.
- **I8:** satisfied; body acquisition and the open IEEE comparison remain separate.
- **I9:** satisfied; all status surfaces keep N-c-012.b open pending three acceptances on one snapshot.
- **I10:** satisfied; no topic verdict is promoted to N-c-012, Part IX, build, visual-handbook, human, final-book, or user acceptance.

## Mandatory F27--F35 fresh checks

- **F27 — resolved.** The raw-path counterexample uses relation symbols `a,c`; the producer--consumer load is `b:S->Z`. No symbol or type collision remains.
- **F28 — resolved.** Full attachment has typed component predicates, an exact formula, metalinguistic standing, explicit nonredundancy against partial attachment, and immediate use in the size comparison.
- **F29 — not resolved.** AP-F1 identifies the omitted reverse indicator implication actually used by the deadlock proof.
- **F30 — resolved.** State assertions are typed before use, and no redundant one-off technical synonym remains.
- **F31 — resolved.** Arbitrary-start action-condition paths, initial-state proper executions, and `Sigma |=_prop A` have distinct definitions, standings, and uses.
- **F32 — resolved.** The text separates two-process sum/product growth from exponential growth as the number of processes varies and preserves initial/per-transition invariant obligations.
- **F33 — resolved.** The internal-edge SCC condition and both directions of its proof are explicitly identified as handbook-supplied.
- **F34 — resolved.** Theorem 5's adequacy clause is labelled asserted but unproved; Appendix B is limited to semantic routes for the decidability clause.
- **F35 — resolved.** Pnueli's local proper-execution acceptor assertion, reference 32's imported omega-regular/closure machinery, and reference 33's inclusion decision remain three separate ownership standings.

## Other mandatory inventory checked clean

- The exact sequential/concurrent model types, `R*`, clean execution, literal P2 and counterexample, ER/I/Theorem 1, typed attachments, recursive F/G, F2--F3, Q1--Q4, RG, action partition, the p. 53 `j>=i` tail, I1/I2/E/N, DI/DN, finite-state seriality, P/MRG, Theorems 4--5, and both appendices were checked against their printed locations.
- The Appendix B recursion was checked clause by clause, including the local types of `[[p]]`, finite-prefix concatenation, `L_prop(Sigma)`, and the inclusion. Its omega-regular label is eliminable and does not create a new automaton or retroject the later general LTL translation.
- The shared Part IX definitions precede the presentation input and do not identify Pnueli's source-specific future-only Kb calculus or strict `leadsto` with the modern reused LTL grammar.
- The neighboring Kamp and GPSS material, the later Sistla--Clarke/Alpern--Schneider material, and the McNaughton/Landweber references remain distinct in version, syntax, result, and proof ownership.
- The bibliography entries `Pnueli1977`, `McNaughton1966`, and `Landweber1969` have identities consistent with the source and the manuscript's citation boundary.

## Premortem

Assume this snapshot shipped and a source-critical reader rejected it. The most likely concrete failure is the step “the other `m`-indicator equals one, therefore that processor is in its critical section” after the book has just claimed to list every indicator premise but supplied only the opposite direction. The failure would look minor typographically yet would break the stated deadlock argument and undermine confidence in the advertised exhaustive reconstruction. A checklist that merely matched the three invariant equations would miss it; following each inference direction against printed pp. 51--52 exposes it. No second blocker or must-fix item survived that same pass.

## Post-review identity recheck and narrow boundary

Immediately before filing, all eight frozen hashes were rechecked and remained exactly the values listed in the pre-review table. The verdict applies only to the round-four N-c-012.b snapshot. It does not close N-c-012.b, any other N-c-012 presentation, Part IX admission, the IEEE-file comparison, a build, handbook visual inspection, human review, final-book completion, or user acceptance.

REVISE
