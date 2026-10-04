# Chair transcript — Büchi 1959 report presentation

## Round 1 opened — 2026-08-23

The chair froze the six-object review snapshot identified in `../charter.md` and seated three independent reviewers for source fidelity, mathematical proof, and adversarial publication review.

Reviewers were blind to one another's reports and to the chair's reconciliation. They could read only the charter, the frozen review artifacts, and the rendered pages identified by the charter. They could not edit the frozen artifacts.

This was a scholarly manuscript review. No test harness, automated checker, repository script, TeX compilation, or handbook PDF build was authorized.

## Round 1 closed — REJECT

All three reports were opened only after all three reviewers had filed against the unchanged round-one snapshot.

- Source fidelity rejected on `R1-SF-01`: Definition 2 was transcribed with \(U[\bot^m]\) rather than the printed \(U[Y^m]\) on the left.
- Mathematical proof rejected on `MP-01`, `MP-02`, and `MP-03`, and recorded should-fix items `MP-04` and `MP-05`.
- Adversarial publication rejected on `AP-01` and `AP-02`.

Direct chair comparison with printed pp. 7, 17–20, 24, and 41 confirmed the Definition 2 error, the false-tail guard and inclusive-bound omission, the printed Theorem 2 witness defect, the Theorem 3 endpoint inconsistency, and the lost tentative qualification on the binary-to-ternary sentence.

The chair did not adopt `MP-03`'s proposed one-character repair. Changing \(u<v\) to \(u<x\) still makes the report's intended bit-occurrence formula accept \((x,y)=(2,8)\), witnessed by \((u,v)=(0,6)\). Later published correction history in Bruyère--Hansel--Michaux--Villemaire (1994), printed pp. 202–203, establishes the larger point: Büchi's unary-powers signature is not equivalent to the bit-occurrence or \(V_2\) signature. Theorem 4 and the dependent “exactly 2-regular” Theorem 9 are false as stated. This chair escalation is stricter than the round-one mathematical recommendation and is included in round-two mandatory coverage.

The frozen round-one snapshot was released only after the rejection was recorded. The reader, source note, compact record, and bibliography were corrected. The shared theorem and report PDF were not changed. No test, checker, repository script, TeX command, or handbook build was run.

Status: ROUND 1 CLOSED — REJECTED.

## Round 2 opened — 2026-08-23

The corrected six-object snapshot and the fixed later-correction source are identified in `../round2-charter.md`. The same three seats are reseated independently. They may not read any round-one transcript, this chair file, the ledger, or one another's round-two work while the round is open.

Status: ROUND 2 OPEN.

## Round 2 closed — ACCEPT

All three reports were opened only after all three reviewers had filed against
the unchanged round-two snapshot. The chair then read every report in full and
independently recomputed all six frozen identities. Every identity still
matched `../round2-charter.md`.

- Source fidelity and evidence: **ACCEPT**; no finding.
- Mathematical and proof correctness: **ACCEPT**; one nonblocking consider
  observation, `R2-MP-C01`.
- Adversarial publication and terminology: **ACCEPT**; no finding.

The mathematical seat observed that the reader's explicitly defined infix
notation \(x\mathrel{\in_2}y\) transposes the ordered arguments used by the
1994 survey. This is definitionally eliminable by exchanging variables, changes
no theorem or correspondence, satisfies the local terminology rule, and was
classified as consider rather than blocker or must-fix. The observation is
preserved in the transcript and admission record; the accepted snapshot is not
changed to erase it.

The board therefore admits the exact round-two snapshot for source acquisition,
reader-facing reconstruction, and topic-level manuscript review of the complete
1959 UMR1083 report precursor only. It does not establish literal fidelity to
the access-controlled 1960 journal article or 1990 reprint, and it does not
admit N-c-014 as a whole, Part IX, any other part, a rendered handbook, human
review, final-book completion, or user acceptance.

No test, test harness, automated checker, repository script, TeX command,
interim handbook build, or handbook-PDF inspection was run in either round.

Status: ROUND 2 CLOSED — ACCEPTED AT 1959-REPORT PRECURSOR STRENGTH.
