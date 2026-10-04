# Edition 2026 P4b: independent implementation review

Review date: 7 September 2026. Verdict: **FAIL at the bounded implementation
scope**. The source-unit schema rejects supported corrected-reader labels that
the Python admission and audit paths accept. A second reproduced limitation
concerns the terminal aggregation API's selection of corrected CSV rows; the
mandatory command-line preflight protects the normal terminal command against
that particular hand-edited CSV case.

This report supplies implementation findings. It supplies no source-unit,
mathematical, manuscript, rendered-output, whole-book, or publication admission.

## Scope and snapshot

Repository: `C:/Dev/the-methods-of-reason`; branch `phase4-codex`; HEAD
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. The checkout has substantial existing
uncommitted work. Review was against the live files pinned below, not a claim
that the HEAD diff isolates P4b. All nine hashes match the P4b handoff. The two
P4a files also match their earlier P4a hashes.

Read in full: `spec/EDITION-2026-CONTRACT.md`,
`spec/research/edition-2026-p4-correction-admission-analysis.md`,
`spec/research/edition-2026-p4a-corrected-reader-implementation.md`, and
`spec/research/edition-2026-p4b-corrected-admission.md`. Inspected the admission
join, schema, audit consumer, terminal consumer, associated fixtures and tests,
and the unchanged source-unit identity validator as a dependency.

| File | SHA256 |
| --- | --- |
| tools/build_source_unit_audit_crosswalk.py | 97BD48FB0341741C2770BB304ADBA31AFAF268EF69ECB9FE58BEE335FD34E9AE |
| tools/check_terminal_readiness.py | 6DF9D60A4ECE607F274F32DABDB02057B8FD52E7F178377BB17006B1E0D42465 |
| tools/audit_tables.py | 38B2F570159D789DF785EE3FDB2C89BC63481A7B3EC8006C847CBA2AD89A6507 |
| tools/test_build_source_unit_audit_crosswalk_reviewed_records.py | A7D51C93FEEFFEF7B3E07BB96C61482E5812841B9086AFD069DE2EA3449E16C3 |
| tools/test_check_terminal_readiness.py | 3503159FA9D8D762A5DD780E3F57F2C1EB4A533868BB504DBBE966639C086F25 |
| spec/provenance/reviewed-source-unit-records.schema.json | E54BA3C8D5E05A17398E92CA6CBC7D5933677F5C64C4D0A1561A38450F7A13A2 |
| spec/provenance/README.md | 4F6DA54DBE85B7550807AA53D3DE5E564F3A98447B336AFC1D292E45C2D88BA5 |
| tools/check_inherited_restoration.py | 5B8BC9717A66B8DD28C2F4CA0135F369B70348BF7330379F45D4E4E93FAF881F |
| tools/check.py | 5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57 |

## Standards

The scoped `git diff --check` passed for the three production consumers, the
schema, and both associated source-unit/readiness test files. No new formatting
finding was established. The preservation requirement for the two P4a files
passes by the exact hashes above. This review adds only this report and does
not implement either correction below.

## Specification findings

### R1 — P2: the schema rejects corrected lemma and method labels accepted by the implementation

The schema's `unitLabel` pattern at
[reviewed-source-unit-records.schema.json:67](C:/Dev/the-methods-of-reason/spec/provenance/reviewed-source-unit-records.schema.json:67)
(lines 67–70) permits only `sec`, `entry`, `def`, `thm`, `ex`, `tab`, `fig`, and
`annex`. Every `stable_labels` item uses it at lines 307–310.

The Python `UNIT_LABEL_RE` at
[build_source_unit_audit_crosswalk.py:162](C:/Dev/the-methods-of-reason/tools/build_source_unit_audit_crosswalk.py:162)
(lines 162–165) includes `lem`, `cor`, `method`, `rem`, `prob`, and `app`, among
other prefixes. `validate_unit_label`, lines 373–413, applies that broader
taxonomy to restoration destinations. The v4 join requires the destination to
be the corrected restoration artifact, lines 686–698. It therefore accepts
legitimate corrected-reader labels that cannot pass the supplied schema.

This affects actual migration candidates: the inspected live reader contains
`method:back-and-forth` at
[inherited-07295-07468.tex:31](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-07295-07468.tex:31),
and another contains `lem:relativization-derivations` at
[inherited-11104-11126.tex:5](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-11104-11126.tex:5).
These are observations of their labels, not admission of either manuscript.
The contract keeps existing labels stable and requires generation to preserve
accepted corrections; the P4b note explicitly says the schema and generator
describe the same supported shape (lines 65–72).

**Isolated reproduction:** use
`ReviewedSourceUnitRecordTests.setUp()` and `_corrected_records()`. Wrap the
existing `make_corrected_reader_fixture` call so the inserted bytes replace
`def:p01-unit-one` with `lem:p01-unit-one` before the v4 map and hashes are
constructed. Set record 1's `stable_labels` to `['lem:p01-unit-one']`. All other
fixture identities, six evidence categories and correction snapshots remain
as produced by the existing fixture. The actual `_apply_records`,
`validate_corrected_source_rows`, `require_corrected_reader_admissions`, and
`audit_tables.main` were executed against the temporary repository.

Observed output:

```text
PYTHON_ADMISSION True
ISOLATED_AUDIT_EXIT 0
SCHEMA_ERROR_COUNT 1
SCHEMA_ERROR_PATH ['records', 0, 'stable_labels', 0]
'lem:p01-unit-one' does not match
'^(?:sec|entry|def|thm|ex|tab|fig|annex):[A-Za-z0-9][A-Za-z0-9._-]*$'
```

**Consequence:** a valid corrected-reader admission can generate an active audit
projection while violating a schema described as a necessary admission
condition. Applying that schema instead blocks a valid stable lemma/method
identity. This is a schema/validator disagreement, not missing review evidence.

**Correction to consider:** align schema label acceptance with the existing
destination-sensitive Python rules, preserving substantive restoration labels.
Add a focused corrected lemma/method case that must pass both validators. Do
not rename an existing reader label merely to satisfy the narrower schema.
The narrow schema pattern already existed before P4b; this review identifies
an inherited interface gap in the newly claimed corrected-reader support,
not a claim that P4b originally introduced that pattern.

### R2 — P2, bounded API finding: relabelled exact CSV claims avoid corrected-row validation

[check_terminal_readiness.py:390](C:/Dev/the-methods-of-reason/tools/check_terminal_readiness.py:390)
(lines 390–402) selects rows solely when the CSV claims `full reconstruction`
or `corrected-and-verified`, and returns immediately if there are none.
It does not first inspect live v4 provenance or source-unit identities.
`build_readiness_manifest`, lines 571–579, then uses the disposition/result
predicate at `build_source_unit_audit_crosswalk.py:1337–1345` and the six CSV
verification strings checked at `check_terminal_readiness.py:214–222`.

**Isolated reproduction:** build the existing two-unit corrected fixture and
retain its initially passing rows. Replace the real reviewed-record input with
one candidate record carrying pending completeness, pending verification, empty
evidence, and `open/missing` / `pending/unclassified`. On copies of the old CSV
rows change only disposition/result to `full transcription` /
`full-and-accurate`. Run the actual corrected-row helper and `read_csv_gate`.

Observed output:

```text
FILTER_ACCEPTED_EXACT_CLAIMS_FOR_LIVE_V4_CANDIDATE True
DIRECT_SOURCE_GATE {'status': 'PASS', 'pass': 2, 'required': 2, 'residual': 0}
LIVE_ADMISSION_TERMINAL_COUNT 0
```

**Established limit:** this bypasses the library aggregation checks for the
source-unit gate. No live-v4 identity independently forces those relabelled
rows through `validate_corrected_source_rows`.

**Command-line protection:** the actual terminal CLI always calls
`run_upstream_checks` before aggregation (`check_terminal_readiness.py:803`).
That preflight includes `build_source_unit_audit_crosswalk.py --check` at
lines 766–787. The crosswalk rebuilds from validated reviewed records and
compares exact output bytes at `build_source_unit_audit_crosswalk.py:1632–1636`
and 1666–1676. Thus a stale or hand-edited exact CSV claim is rejected by the
normal command. This review does **not** establish a successful terminal CLI
or release bypass. The API finding must not be reported as one.

**Correction to consider:** force rows associated with live v4 provenance through
the validated join regardless of their claimed CSV strings, or make the
aggregation API's required upstream-validation precondition explicit and
enforced. Preserve the command-line preflight and exact legacy behavior.

## Confirmed admission properties

The inspected path and focused fixtures establish the following bounded
implementation behavior:

- A corrected terminal pair requires actual v4 validation, exact presentation
  identity, corrected artifact path/hash and exactly-once artifact reachability
  (`build_source_unit_audit_crosswalk.py:666–709`). Source ordinal membership,
  containing frozen interval, inventory identity and wrapper reachability are
  also rechecked (lines 716–774). Legacy records cannot claim the corrected pair.
- All ten completeness and six verification values are exact closed maps.
  Each nonpending category needs evidence, and a terminal disposition needs
  every category and every value to pass (lines 1094–1106 and 1258–1288).
- Every corrected evidence item has the seven exact snapshot fields with exact
  value types (lines 1131–1145). Evidence category uniqueness, separate files,
  live hashes, distinct normalized producer identities and scope are checked
  (lines 1146–1200). Passing AI evidence needs model/version, instructions,
  authorities with live hashes, findings, and the independence declaration
  (lines 1201–1257). These are validation of recorded attestations; they do not
  independently prove that a producer's asserted model/version or conclusion
  is truthful. The investigation's explicit warning about fabricated metadata
  remains applicable.
- The old evidence `maxItems: 5` contradiction is corrected: the schema allows
  six items at lines 355–359 and requires exactly six for terminal dispositions
  at lines 439–471. Both the existing legacy and corrected six-gate fixtures
  passed schema validation during this review. Category uniqueness and live
  evidence identity remain additional Python checks, as the schema description
  says; schema validity alone is not admission.
- The audit command collects the corrected reader hash and every emitted label
  (`audit_tables.py:224–234`, 300–302), then requires every source unit belonging
  to the corrected reader and all those labels to be admitted
  (`build_source_unit_audit_crosswalk.py:1381–1410`). This occurs before either
  emission or freshness acceptance (`audit_tables.py:462–485`). The existing
  tests reject candidate-only input, partial reader admission, unknown emitted
  labels, stale collected bytes, and duplicated artifact reachability.
- Unitless corrected intervals remain unsupported by the whole-reader helper:
  it rejects an empty ordinal list at lines 1399–1401. No scope extension or
  real-record migration was performed. The separate documented expected-nine /
  live-eleven unitless-fragment test was not rerun or rebaselined.

## Checks actually run

Runtime: `C:/Python314/python.exe`, invoked with `-B`. One focused unittest
invocation passed **19 tests in 2.340 seconds**, containing:

1. The six P4b corrected/legacy tests beginning at
   `tools/test_build_source_unit_audit_crosswalk_reviewed_records.py:468`, 480,
   484, 521, 552, and 559.
2. `test_evidence_categories_files_results_and_hashes_are_exact` from that file.
3. The existing `tools.test_check_terminal_readiness` module.

The terminal suite printed its deliberate stale-register-closure failure
diagnostic while testing rejection; the unittest result was `OK`.
The two extra probes described in R1 and R2 ran only in disposable repositories
created and cleaned by the existing fixture. The R1 probe generated only its
temporary fixture's audit file. No active repository generation occurred.
The scoped whitespace check passed. No broad suite, full crosswalk generation,
TeX build, page render, live provenance migration, canonical-record change,
manuscript edit, or production evidence rebaseline was performed.

## Disposition

Standards: no finding established; preserved P4a hashes and scoped whitespace
check pass. Specification: one confirmed schema/validator compatibility
failure and one bounded terminal-API trust gap. P4b implementation acceptance
remains **FAIL** pending correction and a focused independent recheck. Normal
terminal CLI protection against the reproduced CSV hand edit remains intact
on the inspected code. Formal book-admission gates remain outside this review.
