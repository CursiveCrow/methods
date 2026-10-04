REVISE

# Round-five blind adversarial publication/AGENTS review

## Independence, method, and exact scope

I acted only as the adversarial publication/AGENTS-compliance seat. I read the
round-five snapshot in `spec/research/boards/p09-n-c-012b/charter.md` before
substantive work. I did not inspect `ledger.md`, `transcript/chair.md`, any
round-one through round-four transcript, or either other round-five transcript;
I did not contact another reviewer. I made no manuscript, source-note, ledger,
bibliography, or authority edit. I ran no tests, test harnesses, automated
checkers, repository scripts, TeX, handbook-PDF inspection, or build. The only
file I created is this assigned transcript.

I visually read the archival wrapper for provenance only and every printed body
page 46--57 from the source-image renders. The images, not OCR or memory,
controlled every source adjudication. I then read the complete frozen reader
scope in `handbook/parts/p09/presentations/n-c-012.tex` lines 370--1178 and
1583--1590, the shared Part IX scope in
`handbook/parts/p09/logic-in-computer-science.tex` lines 599--823, the complete
Pnueli source note, source-presentation-ledger lines 151--167, the complete
`Pnueli1977`, `McNaughton1966`, and `Landweber1969` bibliography entries, and
the adjacent Kamp/GPSS/Sistla--Clarke presentation boundaries needed to test
conflation. The harness did not expose a runtime model/version.

## Strongest case for acceptance

The repaired snapshot is unusually source-critical and, apart from the findings
below, substantially stronger than a conventional historical summary. It keeps
the author-hosted scan, the later archival wrapper, and the still-uncompared IEEE
file at distinct version standings; types the transition systems, state
assertions, attachments, R4 parameter family, metarule I, action relations,
proper-execution language, and one-letter word embedding; proves both P2
counterexamples; does not silently normalize strict temporal implication to
inclusive `F`; separates the early fairness prose from the later action
condition; discloses the handbook-supplied SCC proof; and keeps Pnueli's local
acceptor assertion, reference [32]'s imported closure machinery, and reference
[33]'s inclusion decision separate. Its reader-facing status also remains
narrow and pre-admission. Those strengths do not cure the remaining
source-proof omission and two publication-level precision defects.

## Findings

### R5-AP-F1 — must-fix — Theorem 1's completeness sketch has an additional unreachable-state gap

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:384-395`,
  `:445-483`, and `:629-660`; `spec/research/p09-pnueli-1977-source-note.md:56-65`,
  `:122-135`, and `:248-275`; `spec/research/p09-source-presentations-lot2-3.md:155-157`.
  Authority: printed pp. 47, 48, and 50.
- **Claim:** The presentation correctly finds the deadlock-vacuity failure of
  the printed base step, but presents that as the sketch's additional unspoken
  gap. It omits a separate failure of printed step 1: the source defines system
  executions from the distinguished initial state, while step 1 requires a
  pointwise assertion about every state satisfying the antecedent.
- **Evidence:** Printed p. 47 defines an execution as
  `s_0,s_1,...`; printed p. 48 defines temporal implication by quantifying over
  those system executions; printed p. 50 claims as step 1 that
  `phi(s) => exists n P(s,n)` is valid, where `P(s,n)` quantifies over every
  execution beginning at arbitrary `s`. Consider the serial finitely branching
  system
  \[
    S=\{s_0,u\},\qquad R=\{(s_0,s_0),(u,u)\},
  \]
  with `phi` true only at `u` and `psi` false everywhere. The unique execution
  from `s_0` never satisfies `phi`, so the source's temporal implication holds
  vacuously. But the execution `u,u,...` avoids `psi`, so `P(u,n)` is false for
  every `n`; hence `phi(u) => exists n P(u,n)` is false. This counterinstance is
  serial, so the manuscript's proposed execution-existence repair at lines
  657--658 does not address it.
- **Harm:** The reader is told the completeness sketch's source defects have
  been bounded, while its first displayed proof step still does not follow from
  the reconstructed semantics. The source note, ledger, and disposition then
  propagate an incomplete proof-boundary claim. This fails C3, C7, I4, and the
  requirement to distinguish source theorem strength from handbook repair.
- **Exact correction:** Add the unreachable-state counterinstance and identify
  the extra missing hypothesis or semantic change explicitly. A sufficient
  repair would be to require `S=X` (all states accessible), to restrict the
  assertion/rule semantics consistently to `X`, or to redefine the temporal
  implication theorem over executions from every start state; Pnueli prints none
  of these. Do not silently choose one. Update the source note, ledger, and
  reader-facing disposition so the deadlock and reachability gaps remain
  separate.

### R5-AP-F2 — must-fix — The handbook's S4 countermodel is only a partially specified frame

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:890-904` and
  `spec/research/p09-pnueli-1977-source-note.md:421-436`; the abbreviated status
  claim is at `spec/research/p09-source-presentations-lot2-3.md:161`. Authority:
  printed p. 53 supplies the S4 referral, while the separating formula and
  countermodel are handbook additions.
- **Claim:** The displayed separating formula is indeed valid on inclusive
  linear futures, but the prose calls the witness a “frame” while assigning
  truth at successors and never states the root valuation. A frame has no
  valuation, and the stated partial data do not force the formula to fail.
- **Evidence:** If the root satisfies `p` or `q`, the displayed consequent can
  become true at the root. The intended failure is obtained only after fixing a
  model, for example `W={r,u,v}`, the reflexive relation plus `rRu` and `rRv`
  and no comparability between `u,v`, with `V(p)={u}` and `V(q)={v}`. Then `r`
  satisfies neither atom, `Fp and Fq` holds at `r`, and neither nested-order
  disjunct holds.
- **Harm:** A skeptical reader cannot verify the mandatory linear/S4 separation
  from the object actually specified, and “frame” and “model” lose their exact
  standings. This is an independently supplied mathematical witness, so its
  omitted valuation cannot be excused as source shorthand.
- **Exact correction:** Replace “frame” by “Kripke model” and give the complete
  relation and valuation, explicitly stating that the root satisfies neither
  `p` nor `q`. Mirror the complete model in the source note; adjust the ledger's
  “explicit” description if it continues to summarize this repair.

### R5-AP-F3 — must-fix — “stronger” overstates the relation between the two fairness formulations

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:439-443`, against
  the manuscript's own qualification at `:918-926`, the source note at
  `spec/research/p09-pnueli-1977-source-note.md:92-95`, and the ledger at
  `spec/research/p09-source-presentations-lot2-3.md:161`. Authority: printed
  pp. 47 and 53.
- **Claim:** Line 441 calls the later action-occurrence condition “stronger.”
  Printed p. 47 speaks about a processor not being postponed indefinitely while
  enabled; printed p. 53 quantifies over members of a finite partition of the
  transition relation and requires every action to recur. The reconstruction
  supplies no exact action-to-processor/enabledness map under which an ordering
  of these conditions has been proved, and lines 923--926 correctly say the
  paper proves no equivalence.
- **Harm:** The single adjective turns a deliberately preserved source boundary
  into an unsupported formal comparison and conflicts with the more careful
  note and ledger. A reader can no longer tell whether “stronger” is source
  wording, a proved handbook implication, or an informal intuition.
- **Exact correction:** Replace “The stronger action-occurrence condition” by
  “The distinct formal action-occurrence condition” or “The later formal
  action-occurrence condition.” If a strict implication is desired, first type
  the processor/action/enabledness correspondence and prove it as a disclosed
  handbook observation.

## Criterion-by-criterion coverage

- **C1 — checked clean.** The DOI, title, author, conference pagination,
  first-party NYU route, retrieval date, compressed/decompressed/render hashes,
  13-physical-page map, May 1981 wrapper boundary, absence-of-observed-licence
  language, independent-prose restriction, and open IEEE-direct comparison are
  mutually consistent. The bibliography does not claim a reproduction right.
- **C2 — one defect, otherwise checked clean.** The state space, initial state,
  infinite execution, deterministic sequential maps, nondeterministic atomic
  interleaving, nonessential determinism, reflexive `R*`, accessible set,
  partial correctness, clean execution, invariant examples, strict temporal
  implication, and excluded specification classes match printed pp. 46--49.
  R5-AP-F3 is the only surviving fairness-boundary defect.
- **C3 — fails by R5-AP-F1, otherwise checked clean.** P1, literal P2, its
  zero-rank typing repair, the independent zero-rank and strict-future
  counterexamples, the inclusive-only false-at-zero repair, A1--A2/R1--R4,
  uniform parameter hygiene, metarule I, pointwise finite branching, assertion
  expressiveness, Koenig architecture, and deadlock-vacuity gap were all checked.
  The omitted unreachable-state failure prevents acceptance.
- **C4 — checked clean.** Sequential location typing, Floyd-premise direction,
  finite-path ER composition, full and partial two-process attachments,
  sum/product/process-count comparison, retained invariant proof obligations,
  the positive-capacity producer--consumer inequalities, both used indicator
  directions, semaphore nonnegativity, and the deadlock case split agree with
  printed pp. 50--52. No full support set is fabricated.
- **C5 — fails by R5-AP-F2, otherwise checked clean.** The recursive inclusive
  `F/G` semantics, absolute present, G1--G3, F2--F3, RT/RG/MP, exact Q1--Q4
  directions, unresolved schema range, RG restriction, action partition,
  literal `j>=i` tail, I1/I2/E/N, DI/DN, Theorem 3's skeletal proof, and its
  relative-completeness corollary are kept at printed strength. The linear
  validity argument is correct, but the branching witness is not fully typed as
  a model.
- **C6 — checked clean.** Finite seriality, arbitrary-start action-condition
  paths, initial-state proper executions, `models_prop`, the every-state versus
  reachable-state Theorem 4 distinction, internal-edge SCC criterion and both
  directions, P, restricted MRG, both Theorem 5 clauses, adequacy nonproof,
  Appendix A ownership, Appendix B's two decision routes, local acceptor
  assertion, one-letter atomic languages, full recursion, closure, and inclusion
  ownership are exact.
- **C7 — fails only where the three findings propagate.** The shared LTL/automata
  surface otherwise keeps Pnueli's inclusive `F/G` presentation distinct from
  GPSS strict operators and from later `X/U`, Buechi translation,
  safety/liveness, and PSPACE results. The three bibliography entries match the
  printed reference identities. The ledger and note must be revised with
  R5-AP-F1 and R5-AP-F2; R5-AP-F3 is already avoided there but survives in the
  manuscript.
- **C8 — fails by the findings, otherwise checked clean.** The prose is
  independently worded; definitions generally precede use; the attachment,
  proper-execution, restricted-validity, and language names satisfy necessity,
  exact definition, standing, nonredundancy, and later use. The source/version
  and larger-open boundaries remain honest.

## Invariant-by-invariant coverage

- **I1:** complied with; scholarship and prose review only.
- **I2:** complied with; all eight identities matched before substantive review
  and again after the complete review.
- **I3:** complied with; wrapper plus printed pp. 46--57 read visually.
- **I4:** not satisfied because R5-AP-F1 omits a theorem hypothesis/semantic
  mismatch and R5-AP-F2 leaves the separating model incompletely typed.
- **I5:** otherwise satisfied: strict `leadsto`, current-target P2, A2,
  inclusive `F`, and Theorem 3's representation remain distinct.
- **I6:** satisfied: no later `X/U` grammar, Buechi translation,
  safety/liveness classification, or PSPACE result is attributed to Pnueli.
- **I7:** the locally introduced technical names were audited. `state
  assertion`, the parameterized family and pointwise existential, full/partial
  attachment, proper execution, restricted validity, `L_prop`, and the
  eliminable omega-regular label all have local standing and actual use. The
  three findings concern missing proof/semantic data and an unsupported
  comparison, not an otherwise unnamed hypothetical artifact.
- **I8:** satisfied: body-level reading is closed while IEEE-direct comparison
  remains open.
- **I9:** satisfied: all status prose requires fresh unanimous acceptance on one
  hash-pinned snapshot; this verdict keeps the topic open.
- **I10:** satisfied: no claim is made about the remainder of N-c-012, Part IX,
  any build/visual/human gate, final-book completion, or user acceptance.

## F27--F40 and mandatory fresh-check coverage

The charter-disclosed F27--F35 subjects were all rechecked from the repaired
text: the raw-path action symbols are relations and do not collide with the
producer load; full attachment has an exact metalinguistic formula and immediate
size use; all actually used indicator implications are stated without a
fabricated support set; state assertions are typed; arbitrary-start paths,
proper executions, and restricted validity remain distinct; the size comparison
separates two-process sum/product growth from process-count exponential growth;
the internal-edge SCC formula and proof are handbook-owned; Theorem 5 adequacy
is expressly unproved; and the three Appendix B proof owners remain separate.

The round-five P2 checks were recomputed: the false-everywhere target example
makes both premises true through `A(b,0)` yet defeats inclusive eventuality; the
current-only target example independently defeats strict futurity; false at zero
blocks only the former mechanism and is clearly unprinted. R4 uses one family
`hat p:S x U -> Bool`, its existential is pointwise state-level, and the
arbitrary-parameter/open-assumption conditions are correct. I specializes that
family to `N_0`, uses a temporary hypothesis at an arbitrary index, and feeds
the same pointwise family to Theorem 1. The producer proof includes both
critical-membership indicator directions and the nonwaiting consequence. The
linear formula is valid, but its advertised S4 witness fails the complete-model
check in R5-AP-F2. The one-letter embedding `S^1 subseteq S*`, prefix
concatenation, and `L(p)=[[p]]S^omega` are well typed and faithful to printed
p. 57.

## Premortem

If this snapshot shipped, the likely scholarly failure would be a reader
checking printed step 1 of Theorem 1 on an unreachable state and discovering
that the handbook's apparently exhaustive source-proof audit had stopped at
deadlocks. A second reader could object that the modal separation was described
as a frame while depending on an unstated valuation. The ordinary checklist did
not miss either issue here: the first emerged by varying reachability while
holding seriality and finite branching fixed, and the second by requiring the
countermodel to be a completely typed semantic object. The fairness adjective
would then compound the problem by making an unproved comparison precisely
where the presentation promises to preserve two formulations separately.

## Hash verification and narrow closure

The following SHA-256 identities matched the charter both before substantive
review and after the complete review, immediately before filing:

- `focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `n-c-012.tex` — `1FABE2120A026468AE21DD2BC116A92DE9AAE048D84655032DA4F7048B82620E`
- `logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook.bib` — `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `p09-pnueli-1977-source-note.md` — `B27AAA9E6C69403998671A924B7F1883DBC2122048D7CF47124464CA63B65803`
- `p09-source-presentations-lot2-3.md` — `3065E52284FF29AAD53121398C3307D691955C13358AE9E314819285A3534203`

This `REVISE` verdict applies only to the round-five N-c-012.b snapshot. It
closes no topic, source comparison, neighboring presentation, Part IX gate,
build, handbook visual inspection, human review, final-book gate, or user
acceptance.

REVISE
