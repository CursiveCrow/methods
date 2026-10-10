# Resume plan (the user asked on 2026-10-05: continue authoring the book until it is complete)

Done criteria: work/waves/PROGRAM-PLAN.md "Done for this plan". Process: PROGRAM-PLAN.md, TOOLING-SPEC.md,
and the W2-b procedure recorded in output/manuscript-status/wave-02b-report.md. All agents are Opus.
Check usage first (mcp__ccd_session_mgmt__get_usage); every workflow halts cleanly on limits and resumes
from its cache (resumeFromRunId) in the same session.

## 1. Finish the Part 15 confirmation audit — DONE 2026-10-10

Result: 71 audited (28 recovered from run wf_e89adb4b-109's journal, 43 re-run), 34 failed and returned to partial with writable duties; 69 unit residual records. authored_unreviewed 785 -> 751.


- Run `wf_e89adb4b-109`: `Workflow({scriptPath: "work/waves/workflows/tmor-upgrade-audit.js", resumeFromRunId: "wf_e89adb4b-109", args: <work/waves/w02b/args-audit3.json>})`.
- Save results to work/waves/w02b/results-audit3.json; `python -B work/waves/tooling/audit_downgrades.py w02b-audit3 work/waves/w02b/proposals-audit3.jsonl work/waves/w02b/results-audit3.json`; `ledger_patch.py apply --apply`; append the failed components to unit-residuals.jsonl as writable (as in commit 2aaab256); `ledger_patch.py check`; commit.

## 2. W2-c: Parts 1, 2, 15 continuation

Status 2026-10-10: packetized (w02ca 83 packets, w02cb 82); w02ca snapshots committed, tag `w02ca-base` (1160357); w02ca run 1 launched as workflow run `wf_6b25aa9b-ba9` (session c1ff47f6). For w02cb, leave out the 14 unit_accounting packets whose units are already fully covered in unit-residuals.jsonl.


1. `python -B tools/waves.py packetize w02c --parts P1,P2,P15 --census work/waves/w01/census.json --apply` (splits into w02ca / w02cb).
2. Snapshot every w02ca packet (`waves.py snapshot`, about 20 min), commit, set base_sha in work/waves/w02ca/args.json, commit, tag `w02ca-base`. Do not change handbook/, spec/research/ or spec/coverage/ while a run is live (G1).
3. Launch `work/waves/workflows/tmor-authoring-wave.js` with w02ca args (runTag only for continuations). Continue halted packets with runTag r2, r3 ... until every packet closes or reaches max_blocks.
4. Wave-end integration exactly as W2-b: ownership audit; normalize_returns + fixups; `integrate_wave collect --wave N --apply`; route; group_patches + group_lead; tmor-wave-integrate.js; restoration_correct.py for edited captures; adopt (dry, then --apply); symbols2tex; check-delta against a fresh baseline taken with the current tools on the wave base (`git worktree` + `check-delta --init`); fix rounds until 0 new; full TeX Live build (`latexmk -r tools/texlive.latexmkrc`) compared with the previous build summary; keyed post-routing re-assessment (keyed_reassess_args.py; keys come from packets); wave_proposals; ledger_patch apply; 1-in-20 audit, and if any sampled upgrade fails, audit every upgrade; report; tag. Commit spec/provenance with handbook changes.
5. Repeat for w02cb.

## 3. Later waves (PROGRAM-PLAN.md table)

W3 P3, P16, P17; W4 P4, P5; W5 P6, P7; W6 P8, P10, P18; W7 P9, P19; W8 P11, P12, P13; then W9 (packets unblocked by acquired sources, carry-over) and W10 (P14 apparatus, reorder, final checks). Before each wave: scout and list new acquisition requests for the user's approval (tmor-acq-r3-scout.js pattern); downloads only after approval.

## Open items for the user

- Manual downloads: work/waves/w01/USER-DOWNLOADS.md (bot-protected hosts), and files listed as "needs a file from you" in work/waves/w02b/ACQUISITION-LIST-r3.md.
