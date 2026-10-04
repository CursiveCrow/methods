ACCEPT

# Round-four adversarial publication/AGENTS review: N-c-012.c GPSS 1980

## Reviewer, runtime, independence, and method

- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Seat: adversarial publication and AGENTS compliance.
- Runtime model/version: not exposed to this reviewer.
- Decision standard: any identity mismatch, unread authority page, uncertainty,
  unsupported addition, omitted load-bearing qualification, technical-name
  failure, source/handbook boundary collapse, or cross-file inconsistency would
  require `REVISE`.
- Independence: I read no board `ledger.md`, no `transcript/chair.md`, no
  round-one, round-two, or round-three transcript (including my own), and no
  other reviewer's transcript, verdict, or output. I did not contact another
  reviewer.
- Mutation boundary: I created only this assigned transcript. I made no change
  to the manuscript, shared Part IX text, source note, source-presentation
  ledger, bibliography, authority, or reading derivatives.
- Prohibited operations: I ran no tests, test harnesses, automated checkers,
  repository scripts, TeX, handbook-PDF inspection, or builds. Source-PDF
  visual reading, read-only file inspection, `pdfinfo`, and SHA-256 identity
  hashing were the only mechanical aids.

## Frozen identities

I computed all eight round-four SHA-256 identities before substantive review
and recomputed them immediately before filing. Both passes matched the charter
exactly:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `DD9DF6D66A6632D98DBF88DD9968C299320B103F317932C836D624D21E76033F` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `038BB890132E61EABB91540EA6CC8BAEC5BFF897FC749FD52CEBD69FCBE2B060` |
| `spec/research/p09-source-presentations-lot2-3.md` | `F0681E77E779236104BF4B490FFCBA9400068AF0026F360A7F1CF0B740EE40CD` |

The eleven ordinary page-image hashes also matched the complete derivative map
in source-note lines 69--84. That supplementary comparison did not replace the
frozen authority hash: the source PDF remains controlling.

## Authority and artifact coverage

I visually reread the wrapper/provenance marks and every printed page of the
eleven-page authority, not merely OCR or the research note:

| Physical page | Printed page | Material visually checked |
|---:|---:|---|
| 1 | 163 | `Sh:134`, title, all four printed authors, affiliations, abstract, both rights notices, introduction, and the informal strict `F/G/X/U` clauses |
| 2 | 164 | full grammar, model, clauses (1)--(5), the literal past-pointing `F` inequality, one-sided `X` clause, omega-validity, `L(U)`, eliminations, execution frame, and partial correctness |
| 3 | 165 | total correctness, invariance/eventuality inventory, and the stated expressiveness motivation for `U` |
| 4 | 166 | insistence, its equivalent form, busy wait, weakest semaphore behaviour/minimal scheduler fairness, infinite overtaking, and the start of persistence |
| 5 | 167 | semaphore persistence, both guarded-region formulas and implementation claims, impulse, and the start of unsolicited response |
| 6 | 168 | unsolicited response, `Pr`, general FIFO, semaphore-specific axiom, the printed repeated-response refinement, and all four questions |
| 7 | 169 | Kamp boundary, prior `DX/DUX` proposal mapping, first-order comparison language, and order-class definitions |
| 8 | 170 | inclusive `>= x` future-formula quantifiers, Theorems 2.1--2.3, the explicit outline heading and `[SS]` referral, `At`, `Bet`, special formulas, Lemma 1, and decomposition formulas |
| 9 | 171 | Main Lemma, Proposition 2.4, event-expression architecture, Theorem 2.5, the exact `DX/DUX` schemes/rules, and Theorems 3.1--3.2 |
| 10 | 172 | maximal theories, asserted canonical facts, literal Gamma closure, finite quotient, both quotient relations, transitive-closure lemma, path/recurrence language, truth lemma, and decidability corollary |
| 11 | 173 | `F^0/G^0/U^0`, transformed systems, the `U^0` conflict, and the complete source bibliography including `[FL]`, `[G1]`, `[G2]`, `[MP]`, `[MY]`, `[P1]`, `[P2]`, and `[SS]` |

I also visually inspected the controlling p. 170 crop and confirmed that both
future quantifier restrictions use `>= x`, and the controlling p. 172 crop and
confirmed the literal closure premise `Xw in Gamma` implies the pool also
contains `X not-w`; I did not substitute a mathematically expected alternative.
The local PDF metadata was independently read: eleven pages, PDF 1.3, 623 by
799 points, 778,981 bytes, not encrypted, embedded title and POPL subject, and
an embedded Author field naming Pnueli, Shelah, and Stavi but omitting Gabbay.

The complete frozen artifact scope read was:

- `n-c-012.tex` lines 1206--1850 in full, plus the preceding Pnueli boundary at
  lines 1150--1205 and the opening Sistla--Clarke boundary at lines 1851--1875;
- `logic-in-computer-science.tex` lines 599--823, including the reused inclusive
  language, both recursive translation directions, the discrete-word theorem,
  and the separately owned complexity/automata material;
- the complete 1,179-line GPSS source note;
- the N-c-012.c source-presentation ledger block, lines 169--183, with enough of
  N-c-012.b and N-c-012.d to test open-boundary consistency;
- the complete `GabbayPnueliShelahStavi1980` bibliography entry at lines
  194--207.

## Steel-man of the frozen presentation

The presentation's organizing decision is sound: it does not flatten GPSS into
modern LTL. It first fixes the source's strict convention and disclosed printed
defects, then reconstructs the program examples, separates four unequal
expressiveness domains, reports the two proof outlines at their actual strength,
and only afterward gives an explicit bridge to the handbook's inclusive
notation. That arrangement makes the many similar-looking `U`, `U^0`, `S`,
`X`, and language symbols auditable without claiming that an external
manuscript or a later automata/complexity result supplies a missing GPSS proof.

## Findings

No blocking or must-fix finding remains. I attempted to falsify the source
identity, theorem domains, formula directions, proof ownership, technical-name
standing, source-key acquisition boundaries, status language, and adjacent
presentation boundaries; none of those attacks produced a residual defect in
the frozen round-four snapshot.

## Criterion-by-criterion disposition

### C1 -- identity, provenance, page map, metadata, rights, and bibliography: checked clean

- Printed p. 163 and reader lines 1208--1225 agree on the four-author title-page
  identity, eleven-page POPL body, printed pages 163--173, conditional ACM
  copying notice, and independent-reconstruction boundary.
- Source-note lines 12--46 and 48--105 give the exact archive URLs, DOI, local
  size/hash/page properties, no-wrapper page map, derivative identities, and
  metadata defect. The reader correctly lets the printed page control over the
  embedded Author field and does not infer ACM byte identity or an open-content
  licence from author hosting.
- Bibliography lines 194--207 preserve all four authors, title, venue, pages,
  publisher, year, ISBN, DOI, archive record, access date, and the rights-safe
  hosting qualification. Ledger lines 169--171 match those facts.

### C2 -- model, grammar, strict semantics, defects, local symbols, and convention bridge: checked clean

- Authority pp. 163--164 and reader lines 1227--1305 agree on atoms `q_i`, all
  four printed Boolean connectives, primitive `F/X/U`, derived `G`, the linear
  model, `q_i`/`Q_i` typing, omega-models, omega-validity, strict witnesses, and
  `L(U)`'s grammar-versus-expressive-equivalence overload.
- Reader lines 1248--1262 reproduce the literal `m_1 < m` defect before adopting
  the coherent future direction as a handbook repair, and separately identify
  false-at-no-successor as a handbook totalization. No endpoint convention is
  retrojected into the printed clause.
- Reader lines 1264--1328 give exact eliminable definitions and standings for
  local strict `U_s` and the handbook-supplied past dual `S_s`, explicitly
  reverse Kamp's operand order, distinguish the source transcription from the
  handbook construction, and supply both strict/inclusive directions on
  omega-words. Shared lines 602--691 use the same convention and do not claim
  inclusive `U/S` alone define next/previous.

### C3 -- executions, correctness, fairness examples, `Pr`, FIFO, and repeated response: checked clean

- Reader lines 1330--1356 define `at_l`, both value tuples, precondition, and
  postcondition with their exact atemporal standing before the partial- and
  total-correctness displays. The termination distinction matches pp. 164--165.
- Reader lines 1358--1423 preserve the source inventories and all three response
  strengths. Local strict `Gp` is correctly separated from eventual permanence;
  the global prefix repeats the obligation. The busy-wait, semaphore, and both
  guarded-region formulas, weakest-behaviour/minimal-fairness calibration,
  infinite-overtaking warning, and implementation limitations match pp.
  165--167.
- Reader lines 1425--1470 preserve the boundary-qualified unsolicited-response
  formula, define `Pr` as an eliminable formula-to-formula abbreviation, type
  its standing, distinguish it from implication/eventuality, and use it in
  exactly the three promised displays. The semaphore formula is explicitly a
  proposed implementation-specific axiom, and the last display is correctly
  called the source's printed repeated-response refinement.

### C4 -- four questions, Kamp boundary, first-order language, future quantifiers, and handbook translation: checked clean

- Reader lines 1472--1486 state all four questions and do not turn them into a
  complexity problem. They accurately separate GPSS's compressed Kamp IV.3
  attribution from the literal integer-order isolation-tense theorem and do not
  invent the missing reduction.
- Reader lines 1488--1529 give equality, `<`, unary predicates and interpretations,
  define complete/discrete orders, retain endpoints, and use the visually
  verified inclusive `>= x` quantifier restriction. The recursive strict
  temporal-to-first-order clauses are explicitly labelled the handbook's
  spelling-out rather than printed GPSS text; their types, operand order,
  immediate-successor condition, strict open intervals, past clause, and
  Boolean extension are correct.

### C5 -- Theorems 2.1--2.5 and the normal-form/event-expression outline: checked clean

- Reader lines 1531--1554 keep the four hypothesis packages separate: arbitrary
  first-order input at omega-point zero; future input at every point of a
  discrete complete model; mixed past/future separation over discrete complete
  models; and arbitrary linear orders only after adding undefined gap symbols.
  Number 2.4 remains Proposition 2.4.
- Reader lines 1556--1660 correctly call the body `Proof of 2.2 (outline)`,
  identify `[SS]` as the forthcoming Shelah--Stavi manuscript without importing
  or independently verifying it, and reconstruct `At`, every `Bet_n` clause,
  `Aft/Bef`, special formulas, Lemma 1, decomposition formulas, the Main Lemma,
  Proposition 2.4, and the event-order complement architecture.
- The event-expression grammar, semantics, finite-set construction, and return
  translations remain explicitly missing. The source's `2.1` sentence under a
  `2.2` proof heading remains unreconciled. The arbitrary-complete-order
  modification, dual past case, gap semantics, and Theorem 2.5 proof are not
  manufactured. `[G2]` is expanded and its direct-proof referral is reported
  with an explicit nonacquisition/nonverification boundary.

### C6 -- `DX/DUX`, exact schemes, theorem strengths, and canonical outline: checked clean

- Reader lines 1662--1703 identify `[P2]` and `[MY]` and their exact respective
  proposal mapping, distinguish those external reports from the systems printed
  in GPSS, state Section 3's primitive basis and validity domain, transcribe
  A1--A5, U1--U2, and all three rules in the correct directions, and keep
  soundness without proof separate from weak theoremhood completeness.
- Reader lines 1705--1737 define maximal consistency relative to the appropriate
  system before use; preserve the source's unprinted standard choice of
  `Delta_0`; type `Delta^+` and `<`; reproduce the three exact asserted facts;
  and limit the linearity conclusion to `Delta_0` together with its strict
  successors.
- Reader lines 1738--1787 retain every literal Gamma-closure obligation,
  correctly say only finitely many formulas up to logical equivalence, treat
  the finite quotient as a source assertion without manufacturing
  representatives, define both quotient relations, preserve the exact
  transitive-closure claim, and separate path adjacency from the later formal
  recurrence condition that omits it. The truth lemma, omitted derivations, and
  formula-dependent but unstated decision bound remain calibrated as an outline;
  no asymptotic class is inferred.

### C7 -- p. 173 conventions, conflict, transformed systems, and anti-retrojection: checked clean

- Reader lines 1789--1816 preserve both coherent `F^0/G^0` equations and the
  literal `U^0` equation, accurately report the source's inclusive/universal
  description, give a fully specified omega-countermodel separating that
  equation from U0.2, and label substitution of `G^0 A` for `G A` only as an
  unprinted possible repair. `U^0` is not assigned one coherent handbook
  standing.
- Reader lines 1818--1849 transcribe A0.1--A0.5 and U0.1--U0.2 in the exact
  directions, give the correct `D^0X` and `D^0UX` languages and source-claimed
  completeness strengths, retain the missing separate proof and unresolved
  `U^0` qualification, identify `[MY]` without importing it, and keep the Part
  VIII strong-until calculus, later LTL name, Büchi translation, PSPACE result,
  and model-checking results outside GPSS.

### C8 -- shared translations and discrete-word theorem: checked clean

- Shared lines 602--623 state the reused inclusive language and independently
  define the needed past constructors on pointed words.
- Shared lines 625--682 give both recursive translations, all atomic/Boolean and
  temporal cases, exact strict operand reversal, exact use of `X/Y`, typed
  metalinguistic standing for `tau/sigma`, and the structural-induction
  truth-preservation argument. Direct semantic calculation confirms every
  displayed direction.
- Shared Theorem lines 684--691 states the one-free-variable first-order result
  on pointed natural-number words, distinguishes Kamp strict `U/S` from the
  inclusive `X/Y/U/S` language, and cites Kamp/GPSS without upgrading either
  GPSS outline. The immediately following complexity and automata material has
  separate later-source ownership.

### C9 -- reader sufficiency, definitions before use, terminology rule, prose, and status: checked clean

- Every handbook-introduced load-bearing symbol is locally eliminable and
  typed: `U_s/S_s`, the temporal-to-first-order star map, `Pr`, `tau/sigma`,
  maximal consistency, `Delta^+`, the canonical `<`, Gamma, the quotient, and
  both rho relations. Their distinctions are necessary to prevent actual
  source/modern, syntax/semantics, or graph/relation collisions, and each is
  used in a later display or result.
- Source names with full standing (`omega-model`, insistence, persistence,
  impulse, complete/discrete order, future formula, special formula,
  decomposition formula, `DX/DUX`) are defined before their load-bearing use.
  Source names whose definitions are absent (`S` in GPSS, `S'/U'`, event
  expressions, and a coherent `U^0`) are explicitly reported as missing or
  conflicted artifacts rather than adopted as handbook objects.
- The prose is independently worded, exact source claims carry printed-page
  locators, derived constructions identify handbook ownership, and no statement
  closes an external body or a larger handbook boundary.

## Invariant-by-invariant disposition

- **I1:** clean. Review was scholarship/prose inspection only; prohibited
  engineering and publication operations were not run.
- **I2:** clean. Both pre-review and immediate pre-filing hash passes matched all
  eight frozen identities.
- **I3:** clean. Every printed page 163--173 was visually reread; both controlling
  crops were inspected; OCR and memory were not treated as authority.
- **I4:** clean. The p. 164 inequality, coherent-future repair, one-sided `X`
  totalization, handbook translation, and handbook past clause all retain their
  exact ownership.
- **I5:** clean. GPSS strict infix `U`, Kamp strict prefix `U/S`, inclusive strong
  `U/S`, and conflicted `U^0` remain separate in witness, current-point,
  operand-order, and next/previous requirements.
- **I6:** clean. Grammar, equivalence, hypotheses, proof status, and deductive
  completeness are not collapsed; absent `S`, `S'`, and `U'` clauses remain
  absent.
- **I7:** clean. Both major outlines and every listed omitted proof artifact are
  labelled at their actual strength.
- **I8:** clean. No later LTL, automata translation, explicit model bound, PSPACE,
  or model-checking result is attributed to GPSS.
- **I9:** clean. The five-part technical-name rule is met for handbook additions;
  undefined source labels are reported, not silently completed.
- **I10:** clean. This review was blind and independent under the stated
  no-contact/no-prior-transcript rule.
- **I11:** clean. This is one seat's verdict, not a majority or topic-closure
  claim.
- **I12:** clean. Ledger line 183 leaves section admission, final build,
  rendered-page inspection, human review, final-book completion, and user
  acceptance open; N-c-012.d and all larger boundaries remain open.

## Mandatory-repair recheck F01--F16

- **F01:** clean at reader 1208--1220 and source note 30--38. The exact embedded
  Author omission and archive-versus-ACM byte boundary are present.
- **F02:** clean at reader 1234--1242 and 1674--1676. Initial grammar, `q_i/Q_i`,
  all Booleans, primitive/derived status, and Section 3 basis are separate.
- **F03:** clean at reader 1365--1389. Local strict `Gp` and globally repeated
  obligation are exact; no `FGp` substitution appears.
- **F04:** clean at reader 1391--1400. Weakest acceptable behaviour, minimal
  scheduler fairness, and infinite overtaking all survive.
- **F05:** clean at reader 1330--1347. All program symbols and tuples are defined
  and typed before use.
- **F06:** clean at reader 1452--1460. The FIFO semaphore display is a proposed
  implementation-specific basic axiom, not a logic theorem.
- **F07:** clean at reader 1605--1610. Lemma 1 is an unprinted induction
  essentially following Kamp II.1.
- **F08:** clean at reader 1705--1737. All three canonical assertions are exact;
  linearity is on the restricted Delta0 domain; derivations remain absent.
- **F09:** clean at reader 1818--1840. Exact transformed languages and claimed
  strengths are given without a separate invented proof.
- **F10:** clean at reader 1789--1842. Both conflicting `U^0` surfaces,
  separating model, only-possible repair, and qualified `D^0UX` claim remain.
- **F11:** clean at reader 1705--1737 and 1762. Maximal consistency is
  system-relative, Delta0's selection is source-asserted, the domain is explicit,
  and `s_0` contains `A_0`.
- **F12:** clean at reader 1738--1755. Gamma is not called a literally finite
  syntactic set; finite-up-to-equivalence and the unprinted quotient argument
  remain distinct.
- **F13:** clean at reader 1556--1563. `[SS]` is fully identified and its proof
  body is neither imported nor independently verified.
- **F14:** clean at reader 1654--1673, source note 107--125, and ledger 177--183.
  `[G2]`, `[P2]`, and `[MY]` are expanded at first reader-facing use; the exact
  respective mapping and nonacquisition/nonverification boundaries are clear;
  the note maps all eight load-bearing source keys; the literal P1
  nineteenth-versus-authoritative-eighteenth FOCS discrepancy remains; ledger
  uses locally identifiable keys.
- **F15:** clean at reader 1461--1467, source note 491--501, and ledger 175. The
  repeated-response display is consistently the source's printed refinement,
  never a handbook repair.
- **F16:** clean at reader 1433--1445. `Pr` has exact eliminable metalinguistic
  standing and the use statement names exactly the three actual following
  displays: general FIFO, semaphore instance, and repeated-response refinement.

## Premortem

Assume this topic shipped and later failed scholarly review. The most plausible
causes would have been: silently correcting p. 164 or p. 173; conflating four
until conventions; reporting outlines or external manuscripts as complete local
proofs; leaving source keys opaque while relying on their results; or allowing
later LTL/automata/complexity results to bleed backward. The frozen snapshot
contains direct defenses against each failure at the exact point of use, and
the source note/ledger/bibliography agree with those defenses. The ordinary
checklist could easily have missed the metadata-author defect, inclusive p. 170
quantifier signs, literal Gamma closure, respective `[P2]/[MY]` mapping, or the
`U^0` countermodel; the mandatory visual and F01--F16 passes caught and cleared
each one. No additional failure mechanism survived the fresh inversion pass.

## Narrow closure boundary

This `ACCEPT` means only that the adversarial publication/AGENTS seat finds the
frozen round-four N-c-012.c integrated snapshot publication-ready at its declared
topic scope. It does not record the other seats' verdicts and does not itself
admit or close N-c-012.c. N-c-012.d, N-c-012 as a whole, Part IX, source-wide
ledgers, the final publication build, rendered-page inspection, human review,
final-book completion, and user acceptance remain open.

ACCEPT
