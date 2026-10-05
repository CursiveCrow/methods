# Wave W2-b report: Parts 1, 2 and 15 (remaining packets)

Date: 2026-10-05. Base: tag `w02b-base-reconstructed`, a rebuild of the lost `w02b-base` (see "Repository" below). Ledger: `spec/coverage/edition-2026/current-fulfillment/`.
This report records ledger bookkeeping. It is not a review, admission or acceptance of any text.

## Ledger status

| status | at W2-b base | now | change |
|---|---:|---:|---:|
| authored_unreviewed | 759 | 785 | +26 |
| partial | 1,228 | 1,261 | +33 |
| missing | 171 | 169 | −2 |
| unassessed | 317 | 260 | −57 |

| part | authored_unreviewed | partial | missing | unassessed |
|---|---|---|---|---|
| P1 | 42 → 44 | 12 → 10 | — | — |
| P2 | 37 → 46 | 72 → 63 | 2 → 2 | — |
| P15 | 92 → 107 | 37 → 81 | 6 → 4 | 66 → 9 |

Net transitions: unassessed → authored_unreviewed 34, unassessed → partial 23, partial → authored_unreviewed 14, authored_unreviewed → partial 22, missing → partial 3, partial → missing 1.

Duty conservation (I7): unaccounted components went from 20,434 (after W0) to 19,061, across 3,075 units.

## What happened

1. **Repository.** The project's git repository lived outside the project: `.git` was a link to `C:\Users\Crow\Downloads\formal-logic-handbook`, which was deleted during the run. All earlier commits and tags (`w00-checkpoint`, `w00`, `w02-base`, `w02a`, `w02b-base`) are lost; the reports of earlier waves still name them. History restarts at `w02b-recovered` (the tree as found). The W2-b base was rebuilt exactly for `handbook/`, `spec/research/` and `spec/coverage/` from the packet snapshots (`w02b-base-reconstructed`; every guarded file matches its recorded sha256), and the guards were re-anchored after verifying all 47 frozen and 54 held files against the snapshot hashes.
2. **Authoring.** 136 packets in three runs. Run 1 stopped on the weekly usage limit (130 agents failed; only 26 author blocks did real work); run 2 halted cleanly on the session limit; run 3 finished. Outcomes: 100 packets closed (66 at their first assessment, 34 after authoring) and 36 reached their block budget with work left.
3. **Integration.** 56 groups routed (112 inserts) and 59 groups collected into batch 11. 88 author patch requests were applied to 39 hosts. The lead backlog of both waves was worked: 85 corrections to 32 restoration captures, each capture's provenance record rewritten as a validated version-4 corrected-reader record; the Part 1 lookup tables are now generated from the registry; new registry checks (generated-table staleness, notation lint, first-use order) were added as W2-a authors requested. Adoption: batch 11 (1,599 symbol rows, 9 bibliography records, 38 canonical edits) and batch 12 (308 rows from the fix round).
4. **Checks.** check-delta against the W2-b base under the same checks: 0 new findings, 57 fixed (one fix round: 298 notation findings resolved by registration, 12 by text edits). Full TeX Live build: 17,271 pages, no new undefined references or citations, duplicate labels or missing characters relative to W2-a; undefined citations 13 → 0. The 102 undefined references already present at W2-a remain.
5. **Assessment.** Every section of the wave's packets (297) was re-assessed after routing by a first and an independent confirming Opus assessor, keyed to the row's owed components and recorded duties.
6. **Audit.** See below.

## Audit: the confirmation step was too lenient

The 1-in-20 sample (4 of the 70 upgrades) found one false upgrade (§172.2: Huber's variant hypothesis, the Winsorizing invariance and one attainment case were missing). As the plan requires, every remaining upgrade was then re-checked by a fresh adversarial Opus auditor at maximum effort. 21 more failed.

- **Measured false-upgrade rate: 22 of 70 (31%).** Part 15: 22 of 57. Parts 1–2: 0 of 13.
- The failures share one pattern: both assessors accepted treatments that narrowed a source's hypotheses or variants, or omitted promised cases, justificatory claims or the fields of empirical claims (e.g. Jaynes's inferential premises in §166.6–166.7, Wald's procedures in §170).
- The 22 rows are back to partial, each with the auditor's gaps as writable duties, and the unit residuals were corrected to match.
- **Process change:** the in-wave confirmation now applies the audit's standard (default not covered; compare the source's whole extent item by item) at maximum effort.
- **Unaudited risk:** the 106 existing authored_unreviewed rows that this wave re-confirmed went through the same lenient confirmation. The plan audits upgrades only; given this result I recommend an adversarial audit of the Part 15 confirmations after the usage reset.

## Downgrades

Rows that were authored_unreviewed before W2-b and are now partial (or missing), each on a negative verdict:

| sections | reason (summary) |
|---|---|
| 8.4 | the identity-sign region list misses an occurrence; the \Leftrightarrow / := sweep is incomplete |
| 11.8 | the source proof of the normal-form theorem is only partly carried over |
| 158.6 | a source consequence (Borel cardinality trichotomy) is stated without proof |
| 159.2 | an unsupported source attribution (Grinstead and Snell) |
| 160.5, 160.6, 160.8 | Durrett Exercise 3.3.24's consequence clause is missing although the boundary promises it |
| 161.12 | only the Theorem-1 half of the Hoeffding note is covered |
| 162.3, 162.4 | an annex proof cites an unproved martingale condition |
| 162.6, 163.3 | promised full treatments behind proof boundaries are not supplied |
| 164.11 | Hempel–Oppenheim examples beyond the illustration are missing |
| 165.1, 165.2, 165.11 | the nested modus ponens bound is not derived (sources not held: ACQ-2026-10-0633/0634) |
| 165.5, 165.8, 166.9, 166.10 | source claims and argument steps are missing or unbounded |
| 167.9, 167.10 | an omitted algebra step; dependent-source claims not written |
| 171.9 | partial → missing |

Reversed in-wave upgrades (failed the audit): 166.3, 166.5, 166.6, 166.7, 169.1, 169.4, 169.6, 169.7, 169.8, 170.2–170.6, 171.4, 172.1, 172.2, 172.4, 172.5, 173.11, 174.5, 174.6.

§175.7 keeps its earlier status: its re-assessment file lacks the input hashes, which is a defect of the record, not a negative verdict. It is re-assessed next.

## Open work carried to the next P1/P2/P15 pass

- **91 sections with writable or disputed gaps**, including the 22 audit reversals and the sections of the 36 packets that ended at their block budget.
- **13 sections still owing an assessment:** 22.4–22.7 and 175.2–175.6, 175.8–175.11. The packetizer's source gate had held them back (and with them the writable locator fix of 9.5–9.7); the gate is fixed (below).
- **§175.7** re-assessment.
- Lead items: the registry-extract convention for the W2-a extract tables (OI-19), registry leftovers (OI-18).

## Blocked

- **On sources:** 40 sections owe only missing sources. New acquisition requests from this wave: ACQ-2026-10-0625 to 0635 (Carnap 1945; Zabell 2011 publisher version; Hintikka–Niiniluoto; Kuipers 1978; Zabell 1996 and 1997; Pitman 1995; Diaconis–Freedman 1980; Sanfilippo–Pfeifer–Gilio 2017; Gilio–Sanfilippo 2014; Rubin–Stern 1994). With ACQ-0615 to 0624 these form acquisition list r3, which still has to be scouted before it comes to you for approval.
- **On policy:** 21.2, 21.3, 22.3 (POL-0001 to 0003) and 164.6 (POL-0006, 0007).

## Questions for you

1. **POL-2026-10-0001 to 0005**, unchanged from the W2-a and W0 reports.
2. **POL-2026-10-0006, §164.6:** Carnap 1950 defers the quantitative-language confirmation function and the comparative vindication of c* to a second volume. Does 164.6 owe them from the 1950 allocation?
3. **POL-2026-10-0007, §164.6:** Carnap asserts m*-limits only under the monadic restriction (sec. 110). Does 164.6 owe limit existence and effective evaluation for general relational sentences, which the source does not assert?
4. **OI-17:** keep the exact source rendering of `\Rule` / `\side`, or adopt the shared rule typography an author requested (it removes two overruns but changes the exact-source surface and its test)?
5. **OI-14:** retirement of the 7 off-route files listed in the W0 report.
6. **Audit of confirmations:** run the adversarial audit over the Part 15 authored_unreviewed confirmations after the usage reset? (Recommended.)

## Tooling changes in this wave

- `tools/restoration_correct.py` (new): records lead corrections to restoration captures as validated version-4 records; rolls back on refusal.
- `tools/waves.py`: the packetizer's source gate blocks a packet only when every recorded duty of every open row is itself blocked_source and nothing is unassessed (it had held back writable and unassessed rows).
- `tools/integrate_wave.py`: sub-wave packet ids; notation-scope findings compared by file and glyph in check-delta.
- `tools/check.py`, `symbol_registry.py`, `symbols2tex.py`: generated-table staleness check, notation lint, first-use check, generated Part 1 precedence and letter-family tables (W2-a author requests).
- `tools/test_restoration_scope.py`: fixture compiles accept references to labels defined elsewhere in the handbook (corrected captures link to routed proofs).
- Workflows: run tags and a clean halt after 6 consecutive agent failures; wave-end integration workflow; the confirmation step's adversarial standard.
- Recovery: `work/waves/recovery/reconstruct_base.py`.

## Next

1. A P1/P2/P15 continuation pass (the open work above), with the hardened confirmation.
2. Acquisition list r3: scouting, then your approval.
3. W3 (Parts 3, 16, 17). Weekly usage is high; these start after the reset on 10 October.
