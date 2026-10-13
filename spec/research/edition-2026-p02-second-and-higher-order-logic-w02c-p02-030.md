# Edition 2026, P2 section 23.3 (packet w02ca-p02-030, label tag p02-w02c-p02-030)

Section: 23.3 Failures of compactness, Loewenheim-Skolem, and effective completeness.

## Provenance and findings (w02ca r2)

- Owned body/annex files were not created. No duty in this packet is writable here:
  - FLRV1-U00835 to U00840 are recorded `open: false` in the packet; their existing treatment is
    `handbook/restoration/inherited-12415-12536.tex` (section `sec:second-order-logic-04`, lines 1-2;
    compactness theorem lines 4-6 with proof 8-20; no-effective-calculus theorem 22-59;
    `thm:second-order-reals-categorical` 61-105; `thm:lindstrom` 107-125), with complete proofs routed to
    the w02-p02-040 body/annex and to w02b-p02-034.
  - Every REQ unit (D-P9-001, N-a-071-01..04) is in `readonly_units`, owner w02c-p02-028 (A14). The r2
    assessment items for ED26-REQ-N-a-071-01 (Church 1940: Axiom 7 elimination for 26^iota', ... at p. 64;
    nondefinability of P_{alpha'alpha'} at p. 59; the four p. 61 claims; the p. 56 framing, credits and
    n. 1 history) belong to that owner; the assessment itself records them as lead_owned for this packet.
    Nothing was written for them here, to avoid a second treatment alongside w02ca-p02-028.
  - Henkin 1950 (ACQ-2026-10-0187), Andrews 2002 2nd ed. (ACQ-2026-10-0008) and Shapiro 1991
    (ACQ-2026-10-0503) are still not held: no entry in `spec/coverage/edition-2026/held-sources.json`,
    no directory under `source/references/` for these ACQ ids (checked 2026-10-10).
- Duty MP-3 (lead-owned; marker of `thm:p02-w02-p02-040-no-effective-calculus`): still uncorrected at
  040 body line 1443 (`proved=`), 040 body lines 1461-1465, 040 annex lines 2130-2246 and restoration
  lines 35-37, 51-53. Filed five anchor-verified patch requests in
  `work/waves/w02ca/patches/w02ca-p02-030.json`: mark the theorem `sketched=`, enumerate the omissions at
  the annex item, and point the body and the restoration capture to `def:p02-w02b-p02-034-boundary`,
  `thm:p02-w02b-p02-034-ta-not-ce` and `thm:p02-w02b-p02-034-no-calculus`.
- Existing treatments found that the packet's `existing` list omits:
  `handbook/parts/p02/second-and-higher-order-logic.tex` and `handbook/annex/p02/higher-order.tex`
  (chapter hosts mentioning compactness/Lindstroem), and the w02b-p02-034 chain above (complete proofs
  of clauses 3-5 of the 040 theorem).

## Continuation

- State after r2: no handbook file written; patch file written; return file written.
- `tools/waves.py unit-compile` fails only because the body file does not exist (no file was created,
  since creating one would be a stub section).
- Next steps belong to others: lead applies the MP-3 patches; w02ca-p02-028 closes the Church 1940
  items; acquisition of Henkin 1950, Andrews 2002, Shapiro 1991 unblocks S02-S04.
