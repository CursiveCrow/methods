# Wave W2-a report: Parts 1 and 2 (main lanes and the first 12 chain packets)

Date: 2026-10-04. Base: tag `w02-base`. Ledger: `spec/coverage/edition-2026/current-fulfillment/`.
This report records ledger bookkeeping. It is not a review, admission or acceptance of any text.

## Ledger status

| status | at w02-base | now | change |
|---|---:|---:|---:|
| authored_unreviewed | 750 | 760 | +10 |
| partial | 1,213 | 1,203 | −10 |
| missing | 195 | 195 | 0 |
| unassessed | 317 | 317 | 0 |

| part | authored_unreviewed | partial | missing |
|---|---|---|---|
| P1 | 34 → 42 | 20 → 12 | — |
| P2 | 35 → 37 | 74 → 72 | 2 → 2 |

Duty conservation (I7): of 21,367 required components, 21,306 were unaccounted before this wave's ledger application and 20,810 are now (across 3,396 units).

## What happened

1. **Authoring.** Opus authors drafted and routed new treatments for the P1 and P2 main lanes and for the first 12 packets of the serial P2 chain lane (1.2, 1.5, 5.1–5.4, 6.1, 6.3–6.8, 8.3, 8.4, 8.7, 10.1–10.6). The chain was stopped after packet 12 so integration could run.
2. **Integration.** The new files were routed, symbol and bibliography intakes adopted, and the full TeX Live build was green (13,651 pages).
3. **Assessment.** Every section touched by the main lanes was assessed by two independent Opus assessors (first and confirm, distinct contexts) after routing. Three rounds were needed (w02r, w02r2, w02r3), because two defects in the assessment process surfaced and were fixed:
   - The assessors were judging different subsets of a section's owed items. Packets now carry explicit per-section keys: every required component of the row's queue units and every recorded duty.
   - Assessments made before routing hashed driver files that routing then changed, so they were stale. Only post-routing assessments were applied.
4. **Audit.** A fresh adversarial Opus auditor re-checked a 1-in-20 sample of the 68 rows confirmed as authored_unreviewed in this wave (§2.6, §7.4, §15.1, §21.7). All four held, with every owed component covered at cited lines.

Outcome for the 106 sections assessed: 68 authored_unreviewed (24 upgrades, 44 confirmations of existing rows), 36 partial and 2 missing, each with recorded duties.

## Downgrades (authored_unreviewed → partial)

Each rests on a negative verdict from an assessor, a source that is not held, or a scope question. None is caused by an assessor omitting an item or by stale hashes.

| sections | reason |
|---|---|
| 9.1–9.4 | The confirm assessor found the Woods–Irvine source link missing (component LR001-C4). |
| 9.5–9.7 | A Boger page locator (p. 160) does not show the cited claim, which is on p. 166. |
| 11.4, 11.5 | The CNF treatment in a restoration capture points forward to a Tseitin section that does not supply the owed content. Restoration captures are lead-owned. |
| 18.6 | The Baaz–Egly–Leitsch 2001 presentation is owed and not held. |
| 21.2, 21.3 | An inherited scope note needs your decision (questions below). |
| 22.1, 22.2 | The reduction and its proofs cover only countable signatures. |

## Open work carried to W2-b

- **Writable gaps found by assessors** (to be authored in W2-b):
  - 2.1: write out the omitted proof steps;
  - 9.5–9.7: correct the locator;
  - 15.5, 15.6: link the Horn/2-SAT material to Part 9;
  - 15.7: the Cook–Levin dependency;
  - 8.1, 8.2, 8.5: notation and registry tables (partly lead-owned: the canonical symbol registry);
  - 9.1–9.4, 22.1, 22.2;
  - 21.8: the BGG 1997 §2.1.2 exercises;
  - 23.3.
- **Lead-owned:** 11.4, 11.5 (restoration CNF capture); 148 patch requests from W2-a authors (`work/waves/w02/lead-backlog-patches.json`).
- **Not yet assessed after routing:** the sections of the 12 completed chain packets (listed under Authoring). W2-b's initial assessment covers them.
- **Not yet run:** the remaining 13 chain packets (w02-p02-011 … w02-p02-034) and all Part 15 lanes.

## Blocked on sources

Acquisition states: "approved" means approved in r1/r2, but the host blocks automated download, so the file waits on your manual download (`work/waves/w01/USER-DOWNLOADS.md`). "Needs user file" means no free copy was found. "New" means the request goes on acquisition list r3.

| sections | work | request | state |
|---|---|---|---|
| 3.7, 3.8 | Halpern & Lévy 1971, BPI does not imply AC (Proc. Symp. Pure Math. 13 I, pp. 83–134) | ACQ-2026-10-0616 | new |
| 13.6, 13.7 | Skura 2011, Refutation systems in propositional logic (HPL 2nd ed. vol. 16, pp. 115–157) | ACQ-2026-10-0617 | new |
| 14.7 | Craig 1957, two JSL papers (22(3), pp. 250–285) | ACQ-2026-10-0091 | needs user file |
| 17.4 | Mendelson 1997, Introduction to Mathematical Logic, 4th ed., ch. 2 | ACQ-2026-10-0618 | new |
| 17.4 | Enderton 2001, A Mathematical Introduction to Logic, 2nd ed., §2.4 | named in the duty; record ACQ-2026-10-0118 exists | unresolved |
| 18.6 | Baaz, Egly, Leitsch 2001, Normal form transformations (HAR vol. 1, pp. 273–333) | ACQ-2026-10-0619 | new |
| 21.8 | Trakhtenbrot 1950 (Doklady 70, pp. 569–572); owed only if 21.8 must present the original proof | ACQ-2026-10-0615 | new |
| 22.8 | Mostowski 1957 (Fund. Math. 44) | ACQ-2026-10-0311 | approved, needs your download |
| 22.8 | Lindström 1966 (Theoria 32) | ACQ-2026-10-0265 | needs user file |
| 22.8 | Keisler 1970 (Ann. Math. Logic 1) | ACQ-2026-10-0225 | approved, needs your download |
| 23.1–23.8 | Henkin 1950 (JSL 15) | ACQ-2026-10-0187 | needs user file |
| 23.1–23.8 | Andrews 2002, An Introduction to Mathematical Logic and Type Theory, 2nd ed. | ACQ-2026-10-0008 | needs user file |
| 23.1–23.7 | Shapiro 1991, Foundations without Foundationalism | ACQ-2026-10-0503 | needs user file |

## Questions for you (blocked on policy)

1. **POL-2026-10-0001, §21.2 (Craig interpolation)** and **POL-2026-10-0002, §21.3 (Beth / Robinson)**. Both rows carry an inherited note: "Broader source/version, other-calculus or whole-facet allocation/admission is not inferred." The bounded treatments are complete at their stated hypotheses. Does either section owe anything beyond the required components of queue units D-P3-004 and D-P3-005? If so, what?
2. **POL-2026-10-0003, §22.3 (empty sorts).** (i) Is an original-source presentation allocated to 22.3? The held Pitts 1995 draft (Example 2.3.2) is cited but not presented. (ii) Are presentations beyond countable signatures owed? That would enlarge the countable variable supply fixed in the first-order semantics conventions.

## Tooling changes in this wave

- `tools/wave_proposals.py`:
  - Owed items for a section are the required components of its row's queue units. An owed item that neither assessor judged blocks an upgrade, and assessor-added extras are ignored.
  - Blocker refs resolve to the record whose work the duty text cites. A record whose source is already downloaded never counts as a blocker.
- `tools/waves.py`: packets carry `assessment_keys` per section.
- `work/waves/workflows/tmor-authoring-wave.js`: both assessors judge exactly the keyed items.
- `tools/held_sources.py`: the frozen Version 1.0 manuscript is indexed as held (FLRV1).
- `work/waves/workflows/tmor-upgrade-audit.js`: the 1-in-20 audit.

## Next

1. W0: backlog readiness and integration (16 items, 17 unclassified off-route files), followed by a post-routing re-assessment.
2. W2-b: the remaining 13 chain packets, Part 15 lanes, and the W2-a carry-over above.
3. Acquisition list r3 (the new requests above), for your approval.
