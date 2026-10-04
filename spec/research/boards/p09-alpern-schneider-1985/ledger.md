# Ledger: Alpern--Schneider 1985 controlling presentation

## Snapshot

Round three is complete.  Three fresh blind seats independently returned
`ACCEPT` on the unchanged seven-object snapshot frozen in `charter.md`.  The
chair read every report in full, independently recomputed every frozen artifact
and transcript identity, and admitted exactly that snapshot for the unlettered
Alpern--Schneider 1985 controlling presentation inside `N-c-012`.

## Findings

### F-MP-01 — must-fix — admitted

- Author: round-one mathematical and proof-correctness seat.
- Locations: `handbook/parts/p09/presentations/n-c-012.tex:2769-2778`;
  `spec/research/p09-alpern-schneider-1985-source-note.md:276-288`;
  `spec/research/p09-source-presentations-lot2-3.md:454-469`.
- Finding: the article's unqualified claim that every leads-to property fails
  absolute liveness uses a witness whose existence is not guaranteed.  In the
  handbook's state-set rendering, the advertised separation needs
  `E_1,E_2 \subseteq S`, `E_1 \ne \varnothing`,
  `E_2 \ne \varnothing`, and
  `S \setminus (E_1 \cup E_2) \ne \varnothing`.  Without a neutral state the
  property can instead be absolutely live.
- Required correction: report the source's printed strength, identify the
  missing-witness defect as source-level, and state the repaired uniform-but-
  not-absolute separation with the exact hypotheses and both witnesses.
- Triage: admitted.  The explicit two-state counterexample in the opening
  report establishes material reader harm and the proposed correction is the
  least source-preserving repair.
- Disposition: repaired, independently validated in round three, and closed.

### R1-AP-01 — must-fix — admitted

- Author: round-one adversarial publication and terminology seat.
- Location: `spec/research/p09-source-presentations-lot2-3.md:423-433`.
- Finding: the compact safety display binds `x \notin P` without declaring
  `x \in S^\omega`, although restriction and concatenation require an
  execution.
- Required correction: restore the typed outer binder and implication used in
  the source and detailed reader.
- Triage: admitted as an exact-standing and cross-record defect.
- Disposition: repaired, independently validated in round three, and closed.

### R1-AP-02 — must-fix — admitted

- Author: round-one adversarial publication and terminology seat.
- Location: `spec/research/p09-source-presentations-lot2-3.md:504-515`.
- Finding: the compact record calls the printed intersection-closure
  assumption false, whereas the countermodel shows that this satisfiable
  assumption is insufficient and that the printed implication is false.
- Required correction: say that the printed hypothesis is insufficient, or
  equivalently that the printed implication is false.
- Triage: admitted as a source-critical logical distinction.
- Disposition: repaired, independently validated in round three, and closed.

### R1-AP-03 — must-fix — admitted

- Author: round-one adversarial publication and terminology seat.
- Location: `handbook/parts/p09/presentations/n-c-012.tex:2780-2800`.
- Finding: the predictive-property paragraph uses `A` and `B` as state sets
  without explicitly stating `A,B \subseteq S`.
- Required correction: add that standing before defining `P_{A,B}`.
- Triage: admitted as a definition-before-use defect.
- Disposition: repaired, independently validated in round three, and closed.

No blocker, should-fix, consider, discard, or unresolved-user finding was
filed.  The source-fidelity seat filed `ACCEPT`; its clean findings do not
override the four independently evidenced must-fixes.

### R2-01 — must-fix — admitted

- Aliases: `R2-SF-01`, `R2-MP-01`, `R2-AP-01`.
- Authors: all three round-two seats independently.
- Locations: the leads-to paragraphs in the reader, detailed source note, and
  compact presentation.
- Finding: the records attributed an unqualified two-part claim to the source.
  The paper conditions liveness on satisfiable `E_2`; only its claim that a
  leads-to property is not absolutely live is unqualified.
- Required correction: preserve those two different source strengths and keep
  the handbook's exact state-set repair visibly separate.
- Triage: admitted; the three reports converge on the same source-attribution
  defect.
- Disposition: repaired, independently validated in round three, and closed.

### R2-02 — must-fix — admitted

- Alias: `R2-AP-02`.
- Locations: all three records' constant-execution and one-state-prefix
  witnesses; the Corollary 2.1 countermodel cylinders.
- Finding: `s^\omega`, singleton prefixes, and `[b]` were used without a local
  typed distinction between a one-state finite word and a constant execution.
- Required correction: define `\langle s\rangle\in S^1\subseteq S^*` and
  `s^\omega\in S^\omega`, type the concatenated witness, and write the
  one-letter cylinder as `[\langle b\rangle]`.
- Triage: admitted under I3--I4; the correction is notation only and creates no
  new theoretical object.
- Disposition: repaired, independently validated in round three, and closed.

### R2-03 — must-fix — admitted

- Alias: `R2-AP-03`.
- Location: reader's neither-class paragraph.
- Finding: `strong-until` is a new name not used or needed by the source.
- Required correction: use the source-exact word `until`.
- Triage: admitted under I4.
- Disposition: repaired, independently validated in round three, and closed.

### R2-04 — should-fix — admitted

- Alias: `R2-AP-04`.
- Location: detailed source note's source-critical findings table.
- Finding: the table omitted the source-level leads-to qualification defect
  already central to the reconstruction.
- Required correction: add a source-located row that distinguishes the printed
  claim from the handbook repair.
- Triage: admitted for source-record completeness.
- Disposition: repaired, independently validated in round three, and closed.

### R2-05 — should-fix — admitted

- Alias: `R2-AP-05`.
- Locations: the Corollary 1.1/Theorem 2 seam in the reader and both source
  records.
- Finding: the presentation omitted the article's separate report, attributed
  to Plotkin by 1983 private communication, about temporal-logic-expressible
  two-liveness-factor decompositions.
- Required correction: report it in paraphrase with an explicit
  private-communication and independent-verification limit.
- Triage: admitted because the claim bears directly on the expressibility
  boundary while remaining weaker evidence than an article theorem.
- Disposition: repaired, independently validated in round three, and closed.

## Round-three validation and admission

All three final reports were kept sealed until every seat had filed.  The chair
then read all three complete transcripts, including every mandatory check
M01--M22 and every validation of the five round-two repairs.  No seat filed a
blocker, must-fix, should-fix, uncertainty, unread page, source mismatch, or
identity mismatch.

| Seat | Verdict | Transcript SHA-256 |
|---|---|---|
| source fidelity and evidence | `ACCEPT` | `19AB40D06B6E26E74A15C44FDDAF9BD9EF4BEED6641B5735121AE9356B6E0197` |
| mathematical and proof correctness | `ACCEPT` | `C1DB1C0520EBB61A3336C4B9470A53FAFE6FADDEC061AFE038E0511D50EB1B1A` |
| adversarial publication and terminology | `ACCEPT` | `D6F61FD3CBA23D292F889211CC3D40F90AB083BB86AE1E1B5E8D19648BC04D50` |

The chair independently recomputed the seven artifact hashes in `charter.md`
after opening the reports; every identity remained exact.  No majority vote
was taken, no dissenting supported finding was discarded, and no verdict from
an earlier snapshot was carried forward.

The durable admission record is
`spec/research/p09-alpern-schneider-1985-independent-review-record.md`, SHA-256
`F7E4158604704B5CFA095D2305B40F045F1C9779445E95031667C5FBD68807CB`.
Its disposition is topic-only: it admits the exact round-three snapshot for
the unlettered Alpern--Schneider controlling presentation inside `N-c-012`,
not `N-c-012` as a whole, Part IX, the book, any rendered artifact, human
review, final completion, or user acceptance.

## Status

- opening round: complete — one `ACCEPT`, two `REJECT`
- triage: complete — four must-fixes admitted
- round-one deliberation: not required; the four corrections are compatible
  and exact
- round-one snapshot: superseded; its verdicts are non-controlling
- round-two snapshot: complete — three `REJECT`; snapshot rejected and thawed
- round-two triage: complete — three must-fixes and two should-fixes admitted;
  overlapping source-attribution findings merged as R2-01
- round-two deliberation: not required; every admitted correction is compatible
  and determinate
- round-three snapshot: complete — three fresh blind `ACCEPT` verdicts on the
  unchanged seven hashes in `charter.md`
- final poll: complete — unanimous acceptance, with no vote needed to suppress
  any finding
- report: complete — durable admission record written, reread, and hash-pinned
- admission: complete for the exact topic-only scope stated above

No test, checker, script, TeX command, handbook build, or handbook-PDF
inspection formed part of this decision.
