# Edition contract re-pin: correction policy authority

Date: 3 October 2026. Scope: the `reader_correction.policy_authority.sha256`
evidence pin of the fifteen current version-4 restoration records, and the
record pins that the source-unit master holds for their 85 linked units.

This is an evidence re-pin only. No review, admission, completeness,
verification or content standing changed. No reader artifact, frozen source,
rationale, predecessor record or history file was touched.

## Why

The fifteen records pinned `spec/EDITION-2026-CONTRACT.md` at SHA-256
`c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3`. The
contract was later amended by the user's recorded directives (the
blockquotes dated 8 and 9 September 2026 and the twelve-subagent paragraph
under "Work ownership and review"). Its current SHA-256 is
`61a8214479f302cd89b131ad7530099f5cdfe4ffdd5ab353e667542b38f1904d`. The old
bytes cannot be reconstructed: the only committed version of the contract
(checkpoint `a4ed54f`) already has the new digest. The restoration
validator therefore rejected all fifteen records with
`reader_correction.policy_authority: evidence digest mismatch`.

The user approved re-pinning to the current contract on 3 October 2026.

Before re-pinning, the current contract was checked against the validator's
other two policy conditions (`tools/check_inherited_restoration.py`,
`validate_reader_correction`). The heading `## Reader-facing content and
corrections` is present. The whitespace-normalized `CORRECTION_POLICY_TEXT`
("Correct known mathematical errors directly in active definitions, formulas,
statements and proofs, ...") is present. The path and locator are unchanged.

## Mechanism

Each record changed in exactly one value. A byte-level replacement, checked by
exact counts, preserved indentation, key order, LF line endings and the
trailing newline. A parsed comparison confirmed that no other value changed.

No history copy or predecessor link was added. The records carry no
self-digest. Their `predecessor_record` links name archived *correction*
predecessors under `spec/provenance/history/`. Those files are unchanged, and
their digests still verify. The repository has already edited record metadata
in place without archiving (for example, the destination metadata of
`SRC-09099-09111`). The most recent master refresh, for the P6 foundation,
also edited `reviewed-source-unit-records.json` in place without a
`history/reviewed-source-units.before-*` copy. The superseded bytes remain in
git at `45d4e9e`.

## Files changed

| File | Old SHA-256 | New SHA-256 | Linked units |
| --- | --- | --- | --- |
| spec/provenance/SRC-01946-02186.json | 527ca7743badc27229147dacdc92f78faeff94c26138935bbb93f18c92aca08d | 47de6832a65eaf28d7b910300b7a2661f7430b31c50fca4f8d49b1a87fbe0144 | 155–166 |
| spec/provenance/SRC-07295-07468.json | 153fbea792e7e3ea6d38630298f354d4e4c979b7398e12d81eb215fe07b6155c | 8930426b19d3371bbddfb9cda3078d831265fb8d852c1b8658eb9bc0af9c87b1 | 499–513 |
| spec/provenance/SRC-07851-08048.json | 3a1227a4d9560bbd34096ec789402af7d2a2038207c9a3c387b17495ba2320ac | 8132b7f2d714e4abab1c02e47b25aa2819037f77427a4b86afe9bd45ac4cffd9 | 544–552 |
| spec/provenance/SRC-08710-08876.json | 467953f1c2c384a2f907118f7504236bed1eca30231e740e9fad852686b53abb | 7e8008a708f45e2d01a4f97250b9a8f3761cbbc01ee68851aa81f5e23e5ebc69 | 595–603 |
| spec/provenance/SRC-09262-09327.json | 7b8f17f8ecdd1b9c902321ee0f46f5a32389902a0fde6815c6120f58a7d69ddb | 6800275bf70e0f8c217df70e057322095d9da20643e62cc8493f6f02bec810f5 | 632–636 |
| spec/provenance/SRC-09328-09438.json | 76d9e27fbf4e96fbc7e2febc697388fc87845b2da52143fc217c0abb9898b889 | 664358b9c9f0b7f2727b45d4f9671a9d160d5ad942d248197f8da9f185fefcb1 | 637–646 |
| spec/provenance/SRC-09750-09816.json | b4484714438ffc2a7e33f311dfe3c5c71d463366c219d7d7405b658790ba8120 | 476ad8bb3c2ee9d7134c7d51eff65836b61f14785d23195c5999fbdf9e8c588b | 668–672 |
| spec/provenance/SRC-09877-09924.json | 2b7cbd95bc2fc5f58272c81f42cfbd4508e997431bc4c995df6054806beddcdc | bde5b0c24ea0e6d3524baf04ebea5b7fde54ca24166fd2573be9b82a231034a4 | 676–680 |
| spec/provenance/SRC-10675-10769.json | 4c7ce3bec285cec29ad07ee31c1a9dadaf872be985e658f59e656b6d6d4501a7 | c92d80803f651784ef1fd60d74ac41f4b2cdb34e82a92adbf687cb58f2dd66c9 | 740–743 |
| spec/provenance/SRC-11104-11126.json | bbd05d017597c42f296eb92dbb7718b353c0c9bcb7de006872ec497e5056d1f4 | 23333bfcb7754878af2999d5b5174eed49a417a0aa2f70936b29491efe66805d | 755–756 |
| spec/provenance/SRC-11127-11199.json | 6af46bf25d853258c8f6a82a5aae38d706ea047eede57c6885166f64da37e996 | 776ca86b1955f109c46f4cbbdadf6e3fbe81efad1ed5fd6545008e1897dd8725 | 757 |
| spec/provenance/SRC-11711-11740.json | 434ae4ad21efb0a135605fc24b9edb19f48343bae98200143c3c11c88385fb29 | 847d69b3c1e2bcdf890b94109d1a693091d4c7b73a766a28ccca60a66800cd8a | 787–789 |
| spec/provenance/SRC-11914-11960.json | ee352221675d4a9f8603c759f9ea2d22f970dbdfd788f0d7e2d0d582a6e6f699 | e4293f739364c202f323d3009a280077b97902013a29e47e449666bd6b947448 | 805–807 |
| spec/provenance/SRC-13519-13551.json | 491e638b07e139492dbfa12ee67846be353a28e7c8675c2fcf2153ec2ce6204f | c6f7f3295c26b4dca764440a133f17fb9409b877f652b97e0d13f7d76759e103 | 891 |
| spec/provenance/SRC-13972-14000.json | 272b0da9217300570a0e876b36c18efc379674e7e73b9d310d71e1e7ab03e4ed | e0ac3a0e6493d49393e20a041f30ef5cde74e78934b495f60cfee2879d1680dd | 918 |
| spec/provenance/reviewed-source-unit-records.json | 9b0fdec148ee4e757db9392e0e110163982f4e8273ddb03c8485cc89817b418e | f2b346bfd781cb3bacdd477475609c039145b454dc4f469e03511d29db0e1d97 | 85 entries |

In the master, the 85 linked entries pin each record hash in three places:
`restoration_record_sha256`, the static `verification_evidence[].sha256` (whose
artifact is the record), and `correction_snapshot.restoration_record_sha256`.
Only those 255 values changed. All other fields of these entries, all 970
other entries and the four top-level fields compare equal.

## Builders run

There is no generated ledger that pins the record hashes and has a runnable
write mode. Both official write modes were attempted after the edit. Each
failed before writing on a preexisting, unrelated failure, and wrote nothing:

- `python -B tools/build_source_unit_audit_crosswalk.py --write` stopped at
  `records[0]` with `handbook destination does not contain stable label
  'sec:inherited-preface'` (`SRC-00198-00234`). `spec/source-unit-audit-crosswalk.csv`
  and `.md` were already stale before this repair: for example, unit 637 still
  shows the version-1 record hash `cad02c7e…`.
- `python -B tools/check_terminal_readiness.py --write` stopped in its upstream
  gate (inherited restoration, crosswalk, reverse ledger and register closure
  all fail for preexisting reasons). `spec/verification/terminal-readiness-manifest.json`
  was already stale before this repair: it pins a 266-record set.

The stored OPEN shards in `spec/provenance/reviewed-source-unit-shards/` still
pin the version-1 history hashes of these fifteen intervals. They were already
stale against the pre-repin version-4 records and were not regenerated here.

A targeted read-only run of the crosswalk's own `validate_restoration_record_link`,
plus the evidence-hash and correction-snapshot checks, over the 85 linked
entries changed from 85 failures (policy digest mismatch) to 85 passes.

## Checker results before and after

| Checker | Before | After |
| --- | --- | --- |
| audit_tables.py --check | FAIL: policy digest mismatch | FAIL: `restoration artifact byte count mismatch: 2675 != 2453` (preexisting SRC-06792-06845, previously masked) |
| check_inherited_restoration.py | FAIL: 252 OK, 30 failing (15 policy digest, 5 missing frontmatter labels, 10 artifact byte counts) | FAIL: 267 OK, 15 failing (the same 5 + 10) |
| build_source_unit_audit_crosswalk.py --check | FAIL: records[0] sec:inherited-preface | identical |
| build_handbook_unit_reverse_ledger.py --check | FAIL: snapshot source drifted: handbook/CONVENTIONS.md | identical |
| build_register_obligation_closure.py --check | FAIL: register manifest row 169 drift | identical |
| build_presentation_packet_admission.py --check | PASS | PASS |
| build_acquisition_gap_resolution.py --check | PASS | PASS |
| build_inherited_bibliography_field_ledger.py --check | FAIL: expected 64 entries, found 73 | identical |
| check_terminal_readiness.py --check | FAIL: upstream restoration (30 records) | FAIL: upstream restoration (the same 15 non-policy records) |
| check_compendium_volume_manifest.py | FAIL: 26 lines, 8 policy digest | FAIL: the 18 remaining lines, identical |
| check_external_coverage_assignments.py | PASS | PASS |
| check_presentation_packet_corpus.py | PASS | PASS |
| check.py --tree source | FAIL | identical |
| check.py --tree handbook | 495 findings, 71 hard | 282 findings, the same 71 hard. The 213 removed findings are the 15 stale scopes and their cascades in the fifteen readers and their annex backrefs. No finding was added. |

Unit tests (`python -B -m unittest discover -s tools -p <file>`):

| Test file | Before | After |
| --- | --- | --- |
| test_check_inherited_restoration | 15 failures | 9 failures, all present before |
| test_build_source_unit_audit_crosswalk_reviewed_records | 2 failures | the same 2 (the committed master differs from the stale merged shards, as before) |
| test_build_open_source_unit_review_shard | 14 errors | 7 errors and 5 failures |
| test_build_register_obligation_closure | 7 failures, 2 errors | identical |
| test_merge_reviewed_record_shards | 4 failures | identical |
| test_restoration_scope | 8 failures | identical |
| test_build_handbook_unit_reverse_ledger, test_check_terminal_readiness, test_build_presentation_packet_admission, test_build_acquisition_gap_resolution, test_ai_review_schema_migration | pass | pass |

In the shard tests, two tests now pass. Two errors (Part V, Part VII) now
reach a preexisting byte-count mismatch. Five former policy errors now fail
because the stored shard pins the version-1 hash (for example `7032cc2f…` for
SRC-10675-10769) while the live record is version 4. Those shards were already
stale against the pre-repin records, so this failure was masked by the policy
error and is not caused by the re-pin.

No checker or test has a failure caused by the re-pin. Every after-failure
was present before or was masked by the policy digest error.

## Not changed

Some files still pin `c9b101ad…`. These are historical read records, so their
pins describe what was read at that time:
`spec/coverage/edition-2026/current-reasoning-units.jsonl` and the research and
verification reports that cite the contract. None of them is validated against
the live contract. `spec/EDITION-2026-PROGRESS.md` line 1161 records the
previous master hash `9B0FDEC1…` as of its own entry. The history copies under
`spec/provenance/history/` are unchanged.
