# Chair transcript: Alpern--Schneider 1985 controlling presentation

## Event C01: board convened

- Mode: review.
- Board type: live.
- Artifact authorship: chair-authored reconstruction disclosed in the charter.
- Frozen snapshot: seven objects and hashes recorded in `charter.md`.
- Independence: blind opening; no seat may inspect any other transcript,
  ledger, chair file, or prior Part IX board record before filing.
- Evidence boundary: complete source-page visual reading, direct manuscript
  reading, mathematical reasoning, citation inspection, and snapshot hashes.
  No test, checker, script, TeX run, interim handbook build, or rendered
  handbook inspection is authorized.
- Roster:
  - source fidelity and evidence: `/root/as_r1_source_fidelity`, `gpt-5.5`,
    xhigh reasoning;
  - mathematical and proof correctness: `/root/as_r1_mathematical_proof`,
    `gpt-5.6-sol`, xhigh reasoning;
  - adversarial publication and terminology:
    `/root/as_r1_adversarial_publication`, `gpt-5.6-terra`, xhigh reasoning.
- Status: all three blind opening seats spawned in parallel; reports sealed until
  all seats finish.

## Event C02: blind opening completed and triaged

- The chair waited until all three reports were filed before opening any
  transcript.
- Source fidelity and evidence filed `VERDICT: ACCEPT` with no finding.
- Mathematical and proof correctness filed `VERDICT: REJECT — F-MP-01`.
- Adversarial publication and terminology filed
  `VERDICT: REJECT — R1-AP-01, R1-AP-02, R1-AP-03`.
- The chair read every report in full and checked each cited manuscript passage
  against the frozen records.  All four must-fixes are admitted in
  `ledger.md`.
- F-MP-01 controls the apparent disagreement over the leads-to example: the
  source-fidelity seat verified the printed wording, while the mathematical
  seat supplied a countermodel showing that the wording is overbroad.  The
  repair must preserve both facts.
- No deliberation round is needed.  The findings do not conflict, each has a
  determinate minimal correction, and no user decision is required.
- Round one therefore closes without admission.  The seven-object snapshot is
  thawed for the four recorded repairs.  Any edit invalidates all round-one
  verdicts; a new hash-pinned blind round is required.
- Evidence boundary remains manuscript scholarship only.  No test, checker,
  script, TeX command, interim build, or handbook-PDF inspection is authorized.

## Event C03: four repairs applied and round two frozen

- F-MP-01: the reader and both source records now distinguish the article's
  overbroad leads-to claim from the exact state-set repair.  They state
  `E_1,E_2 \subseteq S`, all three existence hypotheses, the constant
  `E_2` suffix proving uniform liveness, the neutral suffix disproving
  absolute liveness, and the two-state counterexample showing materiality.
- R1-AP-01: the compact safety clause now binds
  `x \in S^\omega`, uses the implication from `x \notin P`, and types
  `n \in \omega`.
- R1-AP-02: the compact record now says that the printed
  intersection-closure hypothesis is insufficient, rather than false.
- R1-AP-03: the predictive-property paragraph now declares
  `A,B \subseteq S` before defining `P_{A,B}`.
- The chair directly reread every changed passage.  No other content repair
  was made.
- The repaired seven-object snapshot and its hashes are recorded under
  `Frozen round-two repaired snapshot` in `charter.md`.
- Three fresh seats will conduct a blind validation.  They may not read the
  ledger, chair transcript, any round-one transcript, or one another's report.
- No test, checker, script, TeX command, handbook build, or handbook-PDF
  inspection was performed.

## Event C04: blind round two completed and triaged

- The chair waited until all three round-two reports were filed before opening
  any of them, then read each complete transcript.
- Source fidelity filed `VERDICT: REJECT — R2-SF-01`; mathematical and proof
  correctness filed `VERDICT: REJECT — R2-MP-01`; adversarial publication and
  terminology filed `VERDICT: REJECT — R2-AP-01, R2-AP-02, R2-AP-03` and two
  should-fixes.
- `R2-SF-01`, `R2-MP-01`, and `R2-AP-01` are the same source-attribution defect
  and are merged as admitted finding R2-01.  The paper conditions the liveness
  half of its leads-to example on satisfiable `E_2`; its non-absolute-liveness
  claim is the unqualified half.
- R2-AP-02 and R2-AP-03 are admitted as R2-02 and R2-03: the witnesses need a
  typed singleton-word/constant-execution distinction, and the reader must use
  the source's word `until`, not `strong-until`.
- The two should-fixes are admitted as R2-04 and R2-05: the source-critical table
  must include the leads-to defect, and the reported Plotkin private-
  communication claim must appear with its evidence limit.
- No deliberation is needed.  The findings are mutually compatible, have exact
  minimal repairs, and require no user decision.
- Round two closes without admission.  Its snapshot is thawed; every round-two
  verdict becomes non-controlling after the edits, and a fresh hash-pinned blind
  round is required.
- The evidence boundary remains manuscript scholarship only.  No test,
  checker, script, TeX command, interim build, or handbook-PDF inspection is
  authorized or performed.

## Event C05: five repairs applied and round three frozen

- R2-01: the reader and both source records now preserve the source's two
  different leads-to strengths: liveness is conditioned on satisfiable `E_2`,
  while failure of absolute liveness is the unqualified printed claim.
- R2-02: all three records distinguish
  `\langle s\rangle\in S^1\subseteq S^*` from the constant execution
  `s^\omega\in S^\omega`; the non-absolute witness and the countermodel
  cylinder are typed accordingly.
- R2-03: the reader now uses the source-exact name `until`.
- R2-04: the detailed source-critical table now records the leads-to defect as
  AS-06.
- R2-05: the reader and both records now report the Plotkin decomposition with
  its 1983 private-communication standing and independent-verification limit.
- The state-set account also states and proves that nonempty `E_1`, nonempty
  `E_2`, and a nonempty neutral state set are jointly necessary and sufficient
  for the advertised uniform-but-not-absolute separation.
- The chair directly reread every changed passage.  The repaired seven-object
  snapshot and its hashes are recorded under `Frozen round-three repaired
  snapshot` in `charter.md`.
- Three fresh seats will conduct a blind validation.  They may not read the
  ledger, chair transcript, any round-one or round-two transcript, or one
  another's report.
- No test, checker, script, TeX command, handbook build, or handbook-PDF
  inspection was performed.

## Event C06: blind round three unanimously accepted and admitted

- The chair waited until all three fresh round-three seats were complete before
  opening any transcript, then read every line of all three reports.
- Source fidelity and evidence filed `VERDICT: ACCEPT`; mathematical and proof
  correctness filed `VERDICT: ACCEPT`; adversarial publication and terminology
  filed `VERDICT: ACCEPT`.
- Final transcript identities are:
  - source fidelity and evidence:
    `19AB40D06B6E26E74A15C44FDDAF9BD9EF4BEED6641B5735121AE9356B6E0197`;
  - mathematical and proof correctness:
    `C1DB1C0520EBB61A3336C4B9470A53FAFE6FADDEC061AFE038E0511D50EB1B1A`;
  - adversarial publication and terminology:
    `D6F61FD3CBA23D292F889211CC3D40F90AB083BB86AE1E1B5E8D19648BC04D50`.
- Every seat independently checked M01--M22, the five round-two repairs, the
  exact leads-to necessity/sufficiency result, all five journal pages, all
  eleven technical-report pages, every in-scope manuscript line, and all seven
  frozen identities.  No blocker, must-fix, should-fix, uncertainty, unread
  page, source mismatch, or identity mismatch remains.
- After reading the reports, the chair independently recomputed all seven
  frozen artifact hashes and all three transcript hashes.  Every identity
  remained exact.
- No majority vote was taken, no supported finding was discarded, and no
  acceptance from an earlier snapshot was carried forward.
- The exact round-three snapshot is admitted only for the unlettered
  Alpern--Schneider 1985 controlling presentation inside `N-c-012`.  This does
  not admit `N-c-012` overall, Part IX, the book, a rendered artifact, human
  review, final completion, or user acceptance.
- The durable admission record is
  `spec/research/p09-alpern-schneider-1985-independent-review-record.md`,
  SHA-256
  `F7E4158604704B5CFA095D2305B40F045F1C9779445E95031667C5FBD68807CB`.
- No test, test harness, automated checker, repository script, TeX command,
  handbook-PDF inspection, or build formed part of this admission.
