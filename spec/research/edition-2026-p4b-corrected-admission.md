# Edition 2026 P4b: corrected-reader source-unit admission

Implementation checkpoint: 7 September 2026, 17:15 UTC. This bounded block
implements the admission mechanism and isolated regression fixtures. It does
not admit a real source unit, migrate a real provenance record, generate an
active view, or supply independent mathematical or implementation acceptance.

## Implemented contract

The existing source-unit schema version 5 supports the closed terminal pair
`full reconstruction` / `corrected-and-verified`. The join requires a live
version-4 correction record validated by the unchanged P4a validator. Exact
version-1 through version-3 source records retain their existing full
transcription path and exact/layout audit results.

The reviewed source identity still matches its frozen ordinal, kind, title,
source label, range and digest. Corrected presentation identity is exactly
`<provenance_id>:<correction_id>:unit-<unit_ordinal>`. The reviewed destination
path and raw hash equal the version-4 corrected artifact, and its wrapper and
artifact are each reachable once. The restoration-record path/hash binds the
complete correction policy, rationale, predecessor custody and replayed map.

The corrected result excludes this ordered list: `unexplained alteration`,
`abridged`, `omitted`, `hybridized`, `unsupported addition`. This admits only
the exact authorized mapped corrections while retaining the substantive
exclusions. It does not make the false legacy assertion that all alteration
is absent. Exact records retain the ordered list beginning with `altered`.

All ten completeness fields and all six verification fields must pass. Each
gate retains its existing separate evidence file, current hash, distinct
recorded producer and scope. The three independent AI categories retain their
required actual model/version, instructions, consulted authorities and hashes,
findings and declaration that other review outputs were not consulted.

Each evidence item on a corrected reviewed record additionally carries the
closed `correction_snapshot` object. Its seven fields equal the reviewed
record exactly, including value types: `unit_ordinal`, `source_sha256`,
`restoration_provenance_id`, `restoration_record_sha256`,
`presentation_identity_value`, `handbook_destination`, and
`handbook_destination_sha256`. Stale or wrong-unit evidence bindings fail.
This extends the existing evidence record and join; it creates no parallel
admission registry or authority.

The schema's `verification_evidence.maxItems` was five although admission
required six distinct categories. It is now six, and valid six-gate legacy
and corrected fixtures both pass schema validation. No existing review record
was rewritten to accommodate the extension.

## Consumers

- `tools/build_source_unit_audit_crosswalk.py` adds the corrected pair and
  evidence binding to `validate_restoration_record_link` and
  `apply_reviewed_records`. `validated_reviewed_rows` checks frozen inventory
  identities and reuses that existing join without trusting generated CSV
  claims. `require_corrected_reader_admissions` requires all units belonging
  to a corrected reader and coverage of every emitted correction label.
- `tools/check_terminal_readiness.py` revalidates corrected CSV rows against
  that live joined admission and counts only the supported pair under the
  existing six-gate CSV check. Candidate flags or edited CSV disposition
  strings cannot create admission.
- `tools/audit_tables.py` replaces the P4a candidate blocker with this validated
  join. Candidate-only, partial, stale and wrong-label projections remain
  blocked. The collected reader hash must match the admitted artifact. The
  command applies this check to both generation and freshness acceptance.
- `spec/provenance/reviewed-source-unit-records.schema.json` and the P4b
  section of `spec/provenance/README.md` describe the same supported shape.

The helper does not replace the full crosswalk builder's fixed inventory and
complete interval-coverage checks. Unitless corrected intervals have no
supported source-unit admission through this join. Existing active-label
requirements remain in force; an inferred/generated anchor is not silently
substituted for an active label owned by the exact reviewed destination.

## Tests and observed residual

The latest combined focused invocation was:

```text
python -B -m unittest tools.test_build_source_unit_audit_crosswalk_reviewed_records tools.test_check_terminal_readiness tools.test_check_inherited_restoration.CorrectedReaderCandidateTests tools.test_restoration_scope.RestorationScopeStaticTests
```

It ran **100 tests: 98 passed and two failed**. One failure was the old
candidate-blocker wording assertion. The audit diagnostic now preserves
`terminal admission input`; the exact failing case passed in the targeted
follow-up below. The other failure remains deliberately unchanged:

`ReviewedSourceUnitRecordTests.test_committed_records_cover_restored_unit_evidence_without_phantom_row`
expects nine unitless SRC fragments, while the live repository contains eleven.
The additional records are `SRC-16803-17196` and `SRC-17198-17204`. This work
did not change the expected list, those records, or the reviewed-record data.
It is a separate repository snapshot reconciliation issue.

The targeted four-test follow-up passed all four cases:

```text
python -B -m unittest tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_candidate_cannot_enter_active_audit_or_terminal_csv tools.test_restoration_scope.RestorationScopeStaticTests.test_candidate_audit_projection_cannot_promote_active_output tools.test_check_inherited_restoration.InheritedRestorationCliTests.test_reader_appendix_layout_fields_and_source_tokens_fail_closed tools.test_check_inherited_restoration.InheritedRestorationCliTests.test_reader_layout_rejects_altered_missing_and_duplicate_source_tokens
```

After the final malformed-value rejection was made explicit, this targeted
test also passed:

```text
python -B -m unittest tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_admission_rejects_false_identity_disposition_and_stale_links
```

The corrected fixture executes the actual v4 validator, actual reviewed-record
join, schema validation, terminal row reproduction and audit generation inside
an isolated temporary repository. It exercises every missing/failing/pending
verification gate, missing gate evidence, all completeness dimensions, missing
model versions, stale evidence snapshots, stale/wrong correction record links,
wrong destination and unit identity, false exact dispositions, a later artifact
edit, candidate-only records, partial interval admission, unadmitted emitted
labels and duplicate corrected-artifact reachability. Fixture producer/model
identifiers describe fixtures; no production metadata was fabricated.

Earlier development runs are not represented as passing evidence. The first
50-test run found the same repository snapshot mismatch and two old interface
assertions, which were updated for the supported schema. An intermediate
62-test invocation also exposed a handbook-relative path-key error in the new
artifact reachability check and a misspelled requested test-class name. The
path key and invocation were corrected before the 100-test run. The terminal
suite intentionally prints a failure diagnostic when testing rejection of a
stale upstream register closure; that test itself passed.

Scoped `git diff --check` passed before this handoff. No broad test suite, TeX
build, rendered-page inspection, full-book check or live generation was run.

## Preserved boundaries and next steps

P4a construction validation remains unchanged and does not require final
review/build/visual acceptance to authorize candidate source syntax. Pending
corrected reviewed records can expose validated identities while admission
remains open. Versions 1--3 keep their existing exact-token and line-count
checks. System-card withholding, source-line mapping and inherited-reference
policy are unchanged. The audit join introduces no force flag.

Independent implementation review is still owed. Real correction migration
must separately preserve predecessor records, construct exact cumulative edit
maps, bind real current artifacts, obtain the three independent reviews and
scoped static/build/visual evidence, and then supply the reviewed admission
record. Missing actual model/version metadata remains an open recording
condition. Symbol projections, packet admission, full crosswalk freshness,
whole-book builds and visual inspection, and final user acceptance retain
their separate requirements. No real provenance records, crosswalk outputs,
source corpus, manuscript, canonical data or active views were changed here.

## File hashes at handoff

| File | SHA256 |
| --- | --- |
| tools/build_source_unit_audit_crosswalk.py | 97BD48FB0341741C2770BB304ADBA31AFAF268EF69ECB9FE58BEE335FD34E9AE |
| tools/check_terminal_readiness.py | 6DF9D60A4ECE607F274F32DABDB02057B8FD52E7F178377BB17006B1E0D42465 |
| tools/audit_tables.py | 38B2F570159D789DF785EE3FDB2C89BC63481A7B3EC8006C847CBA2AD89A6507 |
| tools/test_build_source_unit_audit_crosswalk_reviewed_records.py | A7D51C93FEEFFEF7B3E07BB96C61482E5812841B9086AFD069DE2EA3449E16C3 |
| tools/test_check_terminal_readiness.py | 3503159FA9D8D762A5DD780E3F57F2C1EB4A533868BB504DBBE966639C086F25 |
| spec/provenance/reviewed-source-unit-records.schema.json | E54BA3C8D5E05A17398E92CA6CBC7D5933677F5C64C4D0A1561A38450F7A13A2 |
| spec/provenance/README.md | 4F6DA54DBE85B7550807AA53D3DE5E564F3A98447B336AFC1D292E45C2D88BA5 |
| tools/check_inherited_restoration.py (unchanged P4a) | 5B8BC9717A66B8DD28C2F4CA0135F369B70348BF7330379F45D4E4E93FAF881F |
| tools/check.py (unchanged P4a) | 5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57 |

## Independent-review repair: 17:35 UTC

The two findings in `spec/verification/edition-2026-p4b-independent-review.md`
were reproduced and repaired in a subsequent bounded block. Independent
recheck remains owed; this author does not change the review's FAIL verdict.

R1: the schema now uses a separate `restorationUnitLabel` rule matching the
Python restoration-label taxonomy, selected only for a restoration
destination. Its ordinary `unitLabel` rule and the Python editorial ownership
validator remain unchanged. The fixture now accepts label parameters, and a
regression uses the actual label forms `lem:relativization-derivations` and
`method:back-and-forth`. The same corrected records pass schema, Python
admission, terminal revalidation and whole-reader admission. Moving those
labels to an ordinary editorial destination still fails both relevant rules.

R2: `validate_corrected_source_rows` now discovers canonical live provenance
records and validates every version-4 record before deriving its actual source
unit ordinals and owning provenance IDs. It requires each affected ordinal
exactly once in the supplied rows. Selection uses those independently derived
ordinals, plus any explicit corrected claims. Changing CSV disposition/result,
restoration links or destination no longer avoids the validated join. Missing,
replaced or duplicate affected ordinals fail. A terminal row returned by the
join must also belong to an owning version-4 record, preventing substitution
by a legacy admission for the same frozen unit. This is a repair to direct API
aggregation. The normal CLI's existing mandatory upstream crosswalk preflight
remains intact; the original finding did not establish a CLI or release bypass.

A bounded read-only helper independently identified two details incorporated
in this repair. First, `validated_reviewed_rows` previously used empty values
for unreviewed fields while the crosswalk generator emitted canonical pending
values. It now matches those existing defaults, so wholly unreviewed corrected
units and explicitly reviewed pending candidates remain representable as OPEN.
Second, selection by an ordinal alone needed the explicit owning-v4 terminal
assertion described above. The helper returned and stopped without edits.

Exact production changes in this repair are limited to:

- Schema: new restoration-label definition and destination-sensitive
  `stable_labels` conditional; existing editorial label rule preserved.
- `validated_reviewed_rows`: canonical pending defaults for the authority,
  presentation, destination, labels, audit result and sixteen gate fields.
- `validate_corrected_source_rows`: validated live-v4 ownership discovery,
  exact affected-ordinal presence, provenance-based selection, and the owning
  v4 assertion before the existing exact joined-row comparison.
- Existing source-unit tests: configurable corrected labels and two focused
  regressions for R1/R2; fixture defaults now match generated pending rows.
- README: terminal selection and honest pending behavior documented.

The diagnosis skill supplied the reproduce-before-repair workflow. The new
two-test invocation first failed exactly as reviewed: schema rejection of the
lemma label, and both forged legacy-marker cases failing to raise (with and
without replaced restoration links/destination). Broader hypothesis gathering
was skipped because the independent review supplied minimized reproductions.

After repair, this focused invocation passed **17 tests in 1.033 seconds**:

```text
python -B -m unittest tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_restoration_lemma_and_method_labels_pass_schema_and_python tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_terminal_selection_uses_live_corrected_units_and_preserves_open_candidates tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_six_gate_records_pass_schema_admission_and_active_audit tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_legacy_six_gate_record_is_schema_valid tools.test_build_source_unit_audit_crosswalk_reviewed_records.ReviewedSourceUnitRecordTests.test_corrected_candidate_cannot_enter_active_audit_or_terminal_csv tools.test_check_terminal_readiness
```

After making the owning-v4 assertion explicit, the single terminal-selection
regression passed again in 0.274 seconds. That test uses real isolated v4
fixtures for valid corrected rows, false markers, reviewed and unreviewed
pending states, replaced links/destination, and missing/replaced/duplicate
ordinals. One additional narrowly mocked joined-row return tests the consumer's
owning-v4 assertion; it is not claimed as an independently validated legacy
admission fixture. The terminal module's expected stale-preflight diagnostic
appeared while its rejection test passed. Scoped whitespace checks passed.

No legacy snapshot expectation was rerun or rebaselined in this repair. No
production records, corpus, manuscript or generated outputs were modified.
No P4a code, audit-table code or terminal CLI preflight was changed.

The following hashes supersede the four affected code/schema/test entries in
the original handoff table; all other code hashes remain unchanged:

| File | SHA256 after repair |
| --- | --- |
| tools/build_source_unit_audit_crosswalk.py | 7C0E85314A8792FE1C529BC289B459E449BDAB3287A7C9C7A95AAE5DD9FCCCF0 |
| tools/check_terminal_readiness.py | B4062BC9410023CA56E7EE927D49BCD514424011778911AF0E45D74D92524804 |
| tools/test_build_source_unit_audit_crosswalk_reviewed_records.py | 7ECF28F0759C737AB1AB8935FEA7FE807C2F796A9AEE15C15B19E7D9A3981037 |
| spec/provenance/reviewed-source-unit-records.schema.json | A542E4F076F7833AE58B5C785C32548BFCA6FBAFC349B07849521AEB58B8ED5C |
