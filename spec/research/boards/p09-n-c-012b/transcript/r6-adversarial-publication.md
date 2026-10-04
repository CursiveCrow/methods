ACCEPT

# Round-six adversarial publication/AGENTS review: N-c-012.b

## Verdict

No blocker, must-fix, should-fix, or unresolved uncertainty remains in the
round-six frozen scope. The presentation is source-faithful and publication
ready at its declared N-c-012.b boundary. This verdict applies only to the
eight hash-pinned objects listed below and closes no wider gate.

## Reviewer, independence, and method

- Seat: adversarial publication/AGENTS.
- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Runtime model/version: the review harness did not expose a specific runtime
  model/version string.
- I read `spec/research/boards/p09-n-c-012b/charter.md` before substantive
  review and treated only its Round-six repaired snapshot as controlling.
- I did not inspect `ledger.md`, `transcript/chair.md`, any round-one through
  round-five transcript (including my own), or either other round-six
  transcript. I did not request, infer, or discuss another reviewer's verdict
  and did not contact another reviewer.
- I edited only this transcript. I made no manuscript, shared-surface,
  source-note, source-ledger, bibliography, authority, or other workspace edit.
- Review consisted only of visual primary-source reading, frozen-text reading,
  mathematical/source-critical reasoning, prose review, and the charter-required
  SHA-256 identity checks. I ran no tests, test harnesses, automated checkers,
  repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen identity verification

All eight identities matched the Round-six charter before substantive review
and again immediately before filing:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `3A4ECE9251B46ACAD8925FFCD34162BE3F9741C09DF912B70967C8FAAB7BE1BC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `86EA6E1F4934B61D5D7E517C01466D6CDA98F80348B1233D52F953F9B1A821CA` |
| `spec/research/p09-source-presentations-lot2-3.md` | `05931057A05C0DCD81507394AF6152B02C3BC12B7E5A7E7AAB757A84A4B1F5C9` |

The post-filing identity check recorded below confirmed that filing this owned
transcript did not alter any controlling object.

## Authority and frozen text actually read

I visually read the archival wrapper and every printed authority page from the
source images. The wrapper was used only for provenance. The body-page map was:

- physical page 2 / printed p. 46;
- physical page 3 / printed p. 47;
- physical page 4 / printed p. 48;
- physical page 5 / printed p. 49;
- physical page 6 / printed p. 50;
- physical page 7 / printed p. 51;
- physical page 8 / printed p. 52;
- physical page 9 / printed p. 53;
- physical page 10 / printed p. 54;
- physical page 11 / printed p. 55;
- physical page 12 / printed p. 56; and
- physical page 13 / printed p. 57.

The images controlled over OCR and memory. I also read the full frozen reader
scope `n-c-012.tex:370-1204,1610-1617`; the complete shared scope
`logic-in-computer-science.tex:599-823`; the complete 730-line source note;
the source-presentation ledger at lines 151-167; the full `Pnueli1977`,
`McNaughton1966`, and `Landweber1969` bibliography entries; and the adjacent
Kamp/GPSS/Sistla--Clarke/Alpern--Schneider boundaries needed to test
conflation. No part of the substantive authority body was skipped.

## Finding register

No finding. In particular, no unsupported source assertion, missing
load-bearing source clause, mathematical defect, definition-before-use failure,
five-part technical-name violation, proof-ownership inflation, provenance or
rights defect, version collapse, cross-file contradiction, or false status
claim survived the round-six snapshot.

## Criterion-by-criterion checked-clean coverage

### C1 — identity, provenance, page map, rights, and version

Checked clean. The reader identifies the NYU memorial route, the image-only
author-hosted body, the May 1981 archival wrapper, the twelve printed 1977 FOCS
pages 46-57, non-IEEE acquisition, and the absence of an observed republication
licence without inferring reproduction rights (`n-c-012.tex:372-382`). The
source note independently records the DOI, retrieval date, all three source and
render hashes, the physical-to-printed page map, the wrapper/body distinction,
the derived-render boundary, and the rights limit
(`p09-pnueli-1977-source-note.md:7-40`). The source ledger agrees
(`p09-source-presentations-lot2-3.md:151-153`), and the `Pnueli1977`
bibliography entry has the correct title, conference, pages 46-57, year, DOI,
first-party URL, retrieval date, and rights note
(`handbook.bib:2226-2237`). The IEEE-direct comparison remains open in every
status surface (`n-c-012.tex:1610-1617`; source note 721-730; source ledger
167).

### C2 — program model, executions, atomicity, fairness, and specifications

Checked clean against printed pp. 46-49. The reader gives the typed dynamic
system and infinite initial-state executions, sequential location/data maps and
transition equation, concurrent product state, processor-indexed maps, and
exact atomic-interleaving relation (`n-c-012.tex:384-438`). It preserves the
source's modelling-granularity qualification. The early enabled-processor
progress prose is reported only as an informal condition and is separated from
the later action-occurrence formula without an unproved equivalence or strength
comparison (`n-c-012.tex:439-443,937-953`). Reflexive reachability is explicitly
reconstructed, with `R^0`, `R*`, and the accessible set typed before invariant
use (`n-c-012.tex:445-462`). Partial correctness, clean execution, mutual
exclusion, deadlock freedom, total correctness, accessibility, responsiveness,
and the source's stated exclusions are separated at their printed logical
standings (`n-c-012.tex:464-490`).

### C3 — invariance, P2, ER, induction, and Theorem 1

Checked clean against printed pp. 49-50.

- P1 is the exact reachable-state induction principle
  (`n-c-012.tex:492-500`).
- P2 retains the source's current-state target and strict temporal-implication
  conclusion. The handbook discloses the zero-rank typing repair and unprinted
  universal closures rather than attributing them to Pnueli
  (`n-c-012.tex:501-526`).
- Totalization is not confused with soundness. The first two-state example
  satisfies both printed premises via `A(b,0)` and falsifies the conclusion
  even for inclusive eventuality. The false-at-zero premise is accurately
  labelled a sufficient, unprinted handbook repair only for that inclusive
  case and is not added to literal P2 (`n-c-012.tex:528-542`).
- The independent strict-future counterexample still satisfies false-at-zero:
  the current `psi(a)` discharges the sole ranked transition, while no later
  state satisfies `psi` (`n-c-012.tex:544-552`).
- A1-A2 and R1-R4 are complete and correctly directed. The one parameterized
  state-assertion family, pointwise existential, arbitrary-parameter
  uniformity, and consequent/open-assumption hygiene are explicit handbook
  typing disclosures (`n-c-012.tex:554-606`).
- The induction metarule specializes that same family to `N_0`, states its
  temporary-hypothesis and arbitrary-index standing, and feeds the typed R4
  instance (`n-c-012.tex:608-627`).
- Theorem 1 is accurately called a source soundness/completeness assertion with
  an explicitly sketched completeness proof, assertion-language expressiveness,
  and pointwise finite branching rather than a uniform branching bound. The
  `P_n`/Koenig/induction/R4/R2/A2 architecture and its source proof status are
  exact (`n-c-012.tex:629-648`).
- The F41 arbitrary-state gap is now explicit and correct. In
  `S={s_0,u}` with the two self-loops, `p` only at unreachable `u`, and `q`
  nowhere, initial-state temporal implication is vacuously true, while the
  infinite `u`-loop makes every `P(u,n)` false. The example is both serial and
  pointwise finitely branching. The three possible missing boundaries are
  stated as alternatives the paper does not supply (`n-c-012.tex:650-665`).
- That gap remains distinct from deadlock vacuity. The one-state empty-relation
  example makes the universal English `P(d,0)` vacuous but falsifies the base
  implication to `q(d)`; its separate repair family is neither conflated with
  nor added to Theorem 1 (`n-c-012.tex:667-677`).
- The strict `j>i` definition, A2, inclusive `F`, and Theorem 3 representation
  remain visibly unreconciled source clauses rather than a normalized modern
  convention (`n-c-012.tex:679-687`).

### C4 — sequential and concurrent applications

Checked clean against printed pp. 50-52. Sequential assertions are indexed by
actual locations, the attachment is typed, and its initial and per-instruction
verification conditions are expressly obligations needed before P1 applies,
not consequences produced by P1 (`n-c-012.tex:689-722`). Full attachment has
an exact pair-indexed formula and metalinguistic standing; partial attachment
has two exact typed families and an exact formula. Their nonredundancy and
immediate size-comparison use are explicit (`n-c-012.tex:724-778`). The text
distinguishes the two-process sum/product comparison from process-count
exponential growth and retains the initial/preservation obligations for global
invariants (`n-c-012.tex:765-779`).

The positive-capacity producer-consumer reconstruction keeps the source's
location map `N` distinct from renamed capacity `C`, types the load, semaphore
values, and indicators, states every indicator implication actually used in
both directions, and invents no full support set (`n-c-012.tex:781-801`). Each
mutual-exclusion, load-bound, and deadlock deduction follows from the three
displayed invariants plus the stated indicator facts, and the final deadlock
contradiction explicitly uses `C>0` (`n-c-012.tex:802-828`).

### C5 — future tense, proof systems, quantifiers, and Theorems 2-3

Checked clean against printed pp. 52-55. `H(t,p)` is typed as a source
metalinguistic evaluation abbreviation rather than an object-language
constructor. The handbook supplies recursive Boolean/F/G semantics for nested
formulas, with both `F` and `G` inclusive, the absolute system present at
`s_0`, and no imported next or until operator (`n-c-012.tex:830-856`). G1-G3,
RT, RG, MP, F2-F3, and Q1-Q4 are complete and correctly directed. The Q1-Q4
schema range and absent domain discussion remain source-unresolved, while the
atemporal-instance restriction is clearly a conservative handbook policy
(`n-c-012.tex:858-905`).

The F42 witness is a complete Kripke model, not a bare frame:
`M=(W,rho,V)` has all three worlds, the full reflexive-transitive fork relation,
and valuations `V(p)={u}`, `V(q)={v}`. The root satisfies neither atom, does
satisfy `Fp and Fq`, and satisfies neither consequent disjunct because the two
successor worlds are incomparable and each sees only itself. The reader
correctly concludes only that the S4 referral does not establish completeness
for the preceding linear-execution semantics; it does not claim the source
theorem refuted at an unstated model class (`n-c-012.tex:907-935`).

The finite action partition and literal `j>=i` tail quantifier are exact. I1,
I2, E, and N retain their types, premises, directions, and action-restricted
semantic standing (`n-c-012.tex:937-997`). The nonempty-action raw-path example
is well typed, partitions the displayed relation, satisfies both N premises,
and falsifies its conclusion only because the raw initial path omits action
`a`; it does not collide with the later load symbol `b`
(`n-c-012.tex:987-997`). DI and DN are correctly marked derived from I2 and N,
not primitive, with the `Gp_2` side condition and Example 2 use stated
(`n-c-012.tex:999-1025`). Theorem 3's proof is accurately limited to the
source's skeletal representation instruction; no individual ER derivation is
invented (`n-c-012.tex:1027-1035`).

### C6 — finite-state package and appendices

Checked clean against printed pp. 55-57. Finite seriality, arbitrary-start
infinite action-condition paths, initial-state proper executions, and
restricted system validity have separate exact definitions and are used at
their distinct standings (`n-c-012.tex:1037-1069`). Theorem 4's source route is
correctly described as sufficient on every `p`-state, while reachable-state
pruning is labelled a handbook observation needed for exact initial-state
validity (`n-c-012.tex:1071-1080`). The internal-edge SCC condition is exact;
the cyclic/reachability requirements and both proof directions are explicitly
handbook-supplied rather than printed source mathematics
(`n-c-012.tex:1082-1101`).

The initial-state rule P and restricted MRG are exact and nonredundant, and the
counterexample to unrestricted post-P generalization is sound
(`n-c-012.tex:1103-1117`). Both Theorem 5 clauses are present. Its derivability
or adequacy clause is explicitly unconstructed in the paper, while Appendix B
is limited to the two semantic routes for decidability
(`n-c-012.tex:1119-1124,1157-1160`).

Appendix A preserves three ownership levels: T2/T3 are attributed to source
reference 23; their adjacent corollaries are printed in Pnueli; and only the
six-step lemma is locally proved (`n-c-012.tex:1126-1155`). Appendix B
separates Pnueli's unproved local proper-execution acceptor assertion,
reference 32's imported omega-regular/closure machinery, and reference 33's
inclusion decision (`n-c-012.tex:1161-1204`). The one-letter embedding into
`S^1`, prefix-concatenation types, and all six atomic/Boolean/F/G language
clauses make the printed recursion well typed. The imported “omega-regular”
label has an eliminable Büchi-recognizability standing and is not used to
retroject a later LTL-to-Büchi translation or complexity result.

### C7 — cross-file integration

Checked clean. The source note and ledger agree with every reader-level source,
repair, theorem-strength, proof-ownership, provenance, rights, and status
claim. The three bibliography entries match the identities printed or invoked
on p. 57 (`handbook.bib:2226-2237,2262-2281`). The shared Part IX surface puts
modern inclusive LTL, past operators, Büchi/parity/Rabin automata, model
checking, and later results at separately cited modern standings
(`logic-in-computer-science.tex:599-749`); it does not assign them to Pnueli.
The Pnueli local presentation explicitly denies next/until and later
translation/complexity attribution. Adjacent Kamp, GPSS, Sistla-Clarke, and
Alpern-Schneider text preserves its own order classes, strict/non-strict
conventions, proof versions, complexity results, and semantic property classes
(`n-c-012.tex:340-368,1206-1272,1590-1608`). No notation, theorem, or source
version is collapsed across those boundaries.

### C8 — first-reader sufficiency, independent wording, and terminology

Checked clean. The prose is independently written and cites exact printed
locators. Definitions precede use throughout. The potentially novel or
source-specific names satisfy all five AGENTS conditions at their introduction:

- `state assertion` is an exact map, has single-state/metalinguistic standing,
  is distinguished from a tense formula, and is used by invariance and every
  rule (`n-c-012.tex:458-462`);
- temporal implication is needed to preserve the source's strict clause, is
  exactly defined as a statement family between state assertions, is
  distinguished from handbook LTL, and is used by P2, ER, and Theorems 1 and 3
  (`n-c-012.tex:473-482`);
- the parameterized state-assertion family and pointwise existential are exactly
  typed, distinguished from ordinary state assertions and tense constructors,
  and used by R4, I, and Theorem 1 (`n-c-012.tex:554-627`);
- full and partial attachment have exact eliminable formulas,
  metalinguistic standing, an explicit difference, and immediate proof-size use
  (`n-c-012.tex:724-778`);
- proper execution and restricted system validity have exact path and semantic
  relation standings, explicit nonredundancy relative to arbitrary-start paths,
  and use in Theorems 4-5 and Appendix B (`n-c-012.tex:1045-1069`);
- `L_prop(Sigma)` is an exact subset of `S^omega`, is needed to avoid inventing
  the source's omitted automaton tuple, is distinguished from `A_Sigma`, and is
  used in the inclusion question (`n-c-012.tex:1161-1199`); and
- “omega-regular” is expressly an eliminable metalinguistic Büchi-language
  abbreviation, distinguished from an automaton, and used only for the cited
  closure/inclusion route (`n-c-012.tex:1189-1201`).

No hypothetical technical vocabulary is named in place of an owed artifact.
No one-off synonym remains that obscures an existing exact term.

## Invariant-by-invariant audit

- **I1:** satisfied by the scholarship-only method recorded above.
- **I2:** satisfied; all eight hashes matched before review, immediately before
  filing, and after filing.
- **I3:** satisfied; wrapper plus every printed page 46-57 was visually read,
  with images controlling over OCR or memory.
- **I4:** satisfied across the exact type, quantifier, premise, side-condition,
  theorem-strength, proof-status, and referral checks under C2-C6.
- **I5:** satisfied at `n-c-012.tex:473-483,578-579,679-687,841-856,1027-1032`:
  strict temporal implication, A2, inclusive F, and the Theorem 3 representation
  remain visibly distinct.
- **I6:** satisfied at `n-c-012.tex:830-856,1189-1204` and by the adjacent/shared
  separations: no later X/U grammar, Büchi translation, safety/liveness syntax,
  or PSPACE result is assigned to Pnueli 1977.
- **I7:** satisfied by the term-by-term five-part audit under C8.
- **I8:** satisfied at `n-c-012.tex:372-382,1610-1617`, source-note lines 7-40
  and 721-730, and source-ledger lines 153 and 167: body reconstruction and the
  IEEE-direct comparison are separate.
- **I9:** satisfied; source note lines 721-728, source-ledger line 167, and
  `n-c-012.tex:1612-1614` keep topic review open pending three independent
  acceptances on one hash-pinned snapshot.
- **I10:** satisfied; source note lines 728-730 and source-ledger line 167 leave
  the rest of N-c-012, Part IX admission, builds, handbook visual review, human
  review, final-book completion, and user acceptance open.

## Mandatory F27-F43 fresh recheck

All mandatory repair obligations were independently rechecked from the current
text rather than presumed correct.

- **F27-F35 group:** clean. The raw-path action symbol is type-stable and does
  not collide with the load; full attachment has exact formula/standing/use;
  only source-supplied indicator implications are used; state assertions precede
  use; arbitrary paths, proper executions, and restricted validity are distinct;
  sum/product/process-count growth is parameterized correctly; the exact SCC
  condition and proof are handbook-supplied; Theorem 5's adequacy construction
  remains unproved; and the three Appendix B ownership standings are separate.
- **F36-F40 group:** clean. P2's two independent counterexamples and limited
  false-at-zero repair are correct; R4 and I use one typed parameter family with
  the necessary hygiene; both producer-indicator directions used by the proof
  are explicit; the linear/S4 distinction uses a valid linear formula and a
  genuine branching countermodel; and the one-letter embedding makes the
  language recursion well typed.
- **F41:** clean. The unreachable-state counterexample is serial and finitely
  branching, separates initial-state truth from the arbitrary-state `P_n` step,
  and is not conflated with deadlock vacuity or silently repaired.
- **F42:** clean. The witness supplies `W`, `rho`, and `V`, proves the frame
  properties, evaluates the antecedent at the root, and falsifies both
  consequent disjuncts.
- **F43:** clean. The early enabled-processor prose and later formal action-tail
  condition are called distinct; no unsupported equivalence, implication,
  strength ordering, or typed correspondence remains.

## Premortem

If this topic later failed scholarly review, the most plausible cause would be
a downstream editor erasing one of the deliberately preserved boundaries:
treating Theorem 1's source assertion as a repaired theorem, treating the S4
referral as a proof for the displayed linear semantics, identifying enabled
processor fairness with action recurrence, or treating the author-hosted body
as an IEEE-verified/republication-licensed object. Those are exactly the
failure modes a superficial copyedit would miss. The current snapshot prevents
them with explicit local counterexamples, source-versus-handbook ownership
labels, non-equivalence language, and open-gate status repeated consistently
across the reader, source note, and ledger. I found no residual prose or symbol
that reopens those failure modes.

## Post-filing hash confirmation and narrow closure

Immediately after filing, the same eight controlling SHA-256 identities were
recomputed and remained exactly those in the frozen-identity table. This
transcript therefore reviews one unchanged round-six snapshot.

`ACCEPT` means only that this adversarial publication/AGENTS seat finds no
remaining substantive defect in N-c-012.b on these hashes. It does not supply
another seat's vote, compare the IEEE file, close neighboring presentations,
admit N-c-012 or Part IX, certify a build or handbook visual rendering, provide
human review, complete the book, or constitute user acceptance.

ACCEPT
