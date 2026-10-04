# Edition 2026 P4b: independent R2 repair recheck

Review date: 7 September 2026. Review window: 17:47–17:57 UTC.

| Repair scope | Verdict |
| --- | --- |
| R1: restoration-label agreement between schema and Python validation | **PASS** |
| R2: direct terminal-API selection from live v4 identities, owning-v4 binding, and pending defaults | **PASS** |

No remaining actionable defect was established within these two repair scopes.
These verdicts close the two reproduced implementation findings at the hashes
below. They are not a new full P4b review, a real admission, mathematical
acceptance, or release readiness.

## Reviewer identity and independence

Reviewer: the independently dispatched `/root/alternation_diagonal_review`
context. I did not implement P4b and did not conduct or author R1's original
review. I read that report and the implementation's repair note because this
assignment expressly requires a finding-by-finding recheck. I do not claim to
have repeated R1's full review or to have performed a blind full-system review.
No exact backend model/version is exposed by the available review interface;
none is invented here. This document does not populate production review or
admission metadata.

The code-review skill was applied within the supplied frozen-file baseline
and the two specified findings. The request's read-only and no-delegation
limits governed; no broad branch review or additional reviewers were started.

## R1 — PASS: destination-sensitive restoration labels

The new `restorationUnitLabel` expression in
[the schema, lines 71–74](C:/Dev/the-methods-of-reason/spec/provenance/reviewed-source-unit-records.schema.json:71)
has the same accepted prefix alternatives and identifier pattern as Python's
`UNIT_LABEL_RE` at
[lines 162–165](C:/Dev/the-methods-of-reason/tools/build_source_unit_audit_crosswalk.py:162).
It includes `lem`, `cor`, `method`, `rem`, `prob` and `app`, as required by the
restoration path. `stable_labels` remains an array with unique items at
schema lines 311–314. The conditional at
[lines 365–373](C:/Dev/the-methods-of-reason/spec/provenance/reviewed-source-unit-records.schema.json:365)
selects that broader item rule only when `handbook_destination` is a
`handbook/restoration/...tex` path. Ordinary destinations still use the
unchanged `unitLabel` expression at lines 67–70.

The Python destination-sensitive ownership checks remain in
`validate_unit_label`, lines 373–413. In particular, the part-content branch
still rejects the restored lemma/method prefixes as editorial part-owned
labels. This is agreement for the repaired restoration-label domain, not a
claim that the JSON schema duplicates every live Python ownership check.
The schema still expressly describes validity as necessary but insufficient.

The new regression at
[test lines 488–503](C:/Dev/the-methods-of-reason/tools/test_build_source_unit_audit_crosswalk_reviewed_records.py:488)
uses `lem:relativization-derivations` and `method:back-and-forth` in an actual
isolated v4 fixture. It passes schema validation, the reviewed-record join,
terminal row validation and whole-reader admission. Repointing the records
at an ordinary editorial destination is rejected by both the schema and the
relevant Python label rule. The regression passed in this recheck.

## R2 — PASS: CSV marker edits no longer avoid live-v4 validation

The repaired helper at
[check_terminal_readiness.py:390–422](C:/Dev/the-methods-of-reason/tools/check_terminal_readiness.py:390)
first discovers canonical live provenance records and invokes the unchanged
v4 validator before deriving source-unit ordinals and their owning provenance
IDs. At lines 402–404, every affected ordinal must occur exactly once in the
provided rows. Missing/replaced or duplicate affected ordinals therefore
cannot escape selection. At lines 405–408, selection uses those independently
derived ordinals as well as explicit corrected CSV claims; CSV disposition,
destination and restoration-ID strings cannot turn a live corrected unit
into an unselected exact row.

The helper obtains the authoritative joined rows through
`validated_reviewed_rows` at line 411. At lines 416–420, a terminal joined row
for a live corrected unit must use the corrected disposition and an owning
v4 provenance ID. A legacy admission for the same frozen ordinal is not enough.
Lines 421–422 then compare all output fields except the two audit-interval
summary fields. Those excluded summaries are not used by the source terminal
predicate or six-review counting condition.

This check is unconditional in the direct aggregation entry point:
[build_readiness_manifest, lines 591–600](C:/Dev/the-methods-of-reason/tools/check_terminal_readiness.py:591)
loads source rows, calls `validate_corrected_source_rows`, and only then
counts the source-unit CSV gate. The lower-level `read_csv_gate` remains a
generic counter; it is not independently a source-admission validator. The
PASS here covers the repaired helper and its placement in the aggregation
entry point, not a claim that calling the generic counter alone validates
provenance.

### Honest pending states remain OPEN

[validated_reviewed_rows, lines 1366–1379](C:/Dev/the-methods-of-reason/tools/build_source_unit_audit_crosswalk.py:1366)
now initializes the same pending/open authority, presentation, destination,
label, audit and sixteen completeness/verification values that the ordinary
generator emits at lines 1497–1531. Reviewed records are subsequently applied
through the existing join. Unreviewed corrected units can consequently match
their canonical pending rows instead of being rejected for blank/default
differences. Pending rows do not satisfy `is_terminal_source_unit`, lines
1337–1344, and do not pass the six verification strings in the generic gate
counter at terminal lines 214–222. No candidate is promoted by this default
alignment.

### Regression extent

The new regression at
[test lines 505–550](C:/Dev/the-methods-of-reason/tools/test_build_source_unit_audit_crosswalk_reviewed_records.py:505)
passed. It covers valid corrected rows; false exact markers; the same forged
markers after replacing restoration links and destination; honest reviewed
pending candidates; completely unreviewed pending rows; a replaced affected
ordinal; and duplicate affected rows.

Its additional narrow mock of `validated_reviewed_rows`, lines 515–517,
exercises the consumer's own terminal-v4 assertion with a legacy-marker
return. It is not an independently validated legacy-admission fixture, and I
do not represent it as one. The explicit owning-ID membership branch was
also checked directly in the current implementation.

## CLI distinction preserved

R1 did not establish a terminal CLI or release bypass. Its normal-command
protection remains visible: `main` calls `run_upstream_checks` at
[lines 823–824](C:/Dev/the-methods-of-reason/tools/check_terminal_readiness.py:823)
before aggregation, and that preflight includes the crosswalk `--check` at
lines 786–794. The original stale or hand-edited CSV was already blocked by
that normal preflight. R2 closes the separately identified direct-API
selection gap. No CLI release attempt was run during this recheck.

## Read and execution scope

Read in full: R1's 219-line report and the 242-line implementation/repair note.
Actual code and documentation read:

- `build_source_unit_audit_crosswalk.py`: 147–180, 373–414, 627–774,
  1327–1422 and 1474–1538.
- `check_terminal_readiness.py`: 177–225, 375–467, 542–612 and 786–851.
- `reviewed-source-unit-records.schema.json`: 1–80 and 300–383; the relevant
  path/label definitions were reread without the earlier display truncation.
- `test_build_source_unit_audit_crosswalk_reviewed_records.py`: 1–565,
  including setup, record construction and both new tests.
- `test_check_inherited_restoration.py`: 1976–2040 for the shared isolated-v4
  fixture; adjacent candidate-test context through 2080 was also inspected.
- `spec/provenance/README.md`: P4b section, 487–557.

Only the following two narrowly named regressions were executed:

```text
C:/Python314/python.exe -B -m unittest -v tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_restoration_lemma_and_method_labels_pass_schema_and_python tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_terminal_selection_uses_live_corrected_units_and_preserves_open_candidates

Ran 2 tests in 0.466s
OK
```

The fixtures use `TemporaryDirectory`, copy the frozen authority into that
temporary repository, construct synthetic records/evidence there, and clean
it through the registered fixture cleanup. Their model/version strings are
explicit fixture data, not production reviewer identities. `-B` was used.
No broad suite, unchanged unitless-count fixture, rebaseline, real admission,
active generation, manuscript build or render was run. The only maintained
repository write by this review is this report.

## Frozen hashes and preservation

The four repaired code/schema/test hashes match the R2 implementation note.
P4a and `check.py` were rehashed before and after the regressions and remain
unchanged, as do the audit consumer and unchanged terminal-test module.

| File | Current SHA-256 |
| --- | --- |
| `tools/build_source_unit_audit_crosswalk.py` | `7c0e85314a8792fe1c529bc289b459e449bdab3287a7c9c7a95aae5dd9fcccf0` |
| `tools/check_terminal_readiness.py` | `b4062bc9410023ca56e7ee927d49bcd514424011778911af0e45d74d92524804` |
| `tools/audit_tables.py` | `38b2f570159d789df785ee3fdb2c89bc63481a7b3ec8006c847cba2ad89a6507` |
| `tools/test_build_source_unit_audit_crosswalk_reviewed_records.py` | `7ecf28f0759c737ab1ab8935fea7fe807c2f796a9aee15c15b19e7d9a3981037` |
| `tools/test_check_terminal_readiness.py` | `3503159fa9d8d762a5dd780e3f57f2c1eb4a533868bb504dbbe966639c086f25` |
| `tools/test_check_inherited_restoration.py` | `d5962bb23f7113139f91c630a6cac75498803d25e94bec506b2ceba2ca311f01` |
| `spec/provenance/reviewed-source-unit-records.schema.json` | `a542e4f076f7833ae58b5c785c32548bfca6fbafc349b07849521aeb58b8ed5c` |
| `spec/provenance/README.md` | `ff84c3875cb65de274ceb60deb3ebbe386be0684eeccf7276f19319e2d80d460` |
| `tools/check_inherited_restoration.py` — unchanged P4a | `5b8bc9717a66b8dd28c2f4ca0135f369b70348bf7330379f45d4e4e93faf881f` |
| `tools/check.py` — unchanged P4a consumer | `5ac607ffb5138fb2202d199209b000ec82d699f4df7975b68e4c7c84501d3f57` |
| R1 review report | `92a20dc74fbea5790121602be12bbbde2de891ab7958f5281a4d556bd8df19b6` |
| P4b implementation/repair note | `1b3b2c08b13de7ba6e0d6a8bd47e5648a0b4c0a87b3e5845e253f595bc006e00` |

Standards at this scope: destination ownership and preservation boundaries
remain intact; no new finding established. Specification at this scope: both
reported repairs PASS. The original broader review remains its own historical
record, and formal admission and all unrelated residuals remain outside this
recheck. In particular, the unitless-count snapshot issue was neither retested
nor resolved here.
