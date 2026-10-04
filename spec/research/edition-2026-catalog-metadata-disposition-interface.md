# CAT-01: interface for reviewed metadata dispositions

Date: 7 September 2026. Author: `/root/kamp_iii1_topic_review`.
Scope: bounded schema and consumer research for the 409 children of
`SRC-068-H278`. This note is the sole write. No catalog, binding, schema,
consumer, assignment, admission record or manuscript was changed.

## Finding

**The existing external-coverage assignment mechanism has no metadata
disposition variant.** It accepts only assignments to independently admitted
presentation packets with nonempty present-content-item references. The
existing index and streaming checker are nevertheless the correct extension
point: add a reviewed metadata-batch branch to that same index and account
for it separately in the existing terminal-readiness consumer.

The 409 rows must not be represented by invented presentation packets or
dummy present-content items. Their reviewed metadata standing can discharge
their historical catalog reconciliation obligation without claiming that
the referenced source files, their contents, or a book treatment have been
completed.

## Batch evidence reused

The complete first-partition and full-set notes were read:

- `spec/research/edition-2026-catalog-first-partition.md`
- `spec/research/edition-2026-catalog-first-partition-full-set.md`

They identify exactly `SRC-068-T11120` through `SRC-068-T11528`, the 409
children of `SRC-068-H278`. The latter note records the complete-catalog
membership and uniqueness check against:

- `spec/full-compendium-coverage-manifest.csv`
- SHA256 `69d0f7ccb89e9be070366102f958a4034f632088b269a92ee244bfa5b41d55e8`
- 6,947,214,502 bytes; 9,162,150 records.

The existing receipt is
`tmp/edition-2026-catalog-first-batch/membership-receipt.json`; the full-set
note records SHA256
`53fda56272025d31368a02b6ac4cb9203de5604ac44134024fff6ad903e76ced`.
Its header and first selected-record structure were inspected for interface
purposes. They expose `catalog_path`, `catalog_sha256`, `catalog_bytes`,
`rows`, `predicate`, `selected_count`, `source_and_parent`,
`preceding_excluded_record`, and `selected`. Each selected entry contains
`original_record`, `payload_sha256`, and `descriptor_fields`.

The record count, full-catalog hash and membership result above are reused
from the supplied evidence, not recomputed in this research. No part of the
7 GB catalog was read and no membership check was rerun. The receipt itself
calls its standing mechanical evidence with semantic disposition and
admission pending. This note does not change that standing or claim that
independent review has already occurred.

## What exists now

### 1. The historical catalog is a preserved input

`tools/build_coverage_manifest.py:43` fixes `MAPPING_STATUS` to
`open/unmapped`. The CSV's fields are `FIELDNAMES` at lines 79-94:

`stable_id, record_type, source_id, source_title, source_metadata,
retrieved_granularity, hierarchy_path, parent_stable_id, displayed_title,
source_https_urls, source_non_https_urls, source_scheme_less_identifiers,
retrieval_date, mapping_status`.

The producer checks its fixed mapping status at lines 503-505 and
1071-1073. Updating the 409 historical CSV rows to a new status would
change the pinned input and violate this producer's current contract.
Their original payloads and source/parent joins should remain preserved.

### 2. The existing index pins that catalog and packet admission

Current path: `spec/external-coverage-assignment-index.json`.
Current schema: `spec/external-coverage-assignment-index.schema.json`.
The schema disallows additional properties and fixes `schema_version` to 1.
The index currently contains exactly these top-level fields:

| Field | Current meaning/value |
| --- | --- |
| `schema_version` | `1` |
| `coverage_manifest_path` | `spec/full-compendium-coverage-manifest.csv` |
| `coverage_manifest_sha256` | The catalog digest above |
| `coverage_manifest_bytes` | `6947214502` |
| `coverage_manifest_record_count` | `9162150` |
| `packet_admission_path` | `spec/presentation-packet-admission.csv` |
| `packet_admission_sha256` | `be0ca787dcfd5f7e3430e93e04406aa3a26ff304bdf3fa95c1053bba50705339` |
| `packet_admission_bytes` | `413` |
| `sidecars` | Empty array in the inspected index |

Each existing sidecar index entry has the exact fields `sidecar_path`,
`sidecar_sha256`, `assignment_count`, `first_coverage_id`, and
`last_coverage_id`. Its path must start with
`spec/provenance/external-coverage-assignments/` (schema lines 47-71;
checker lines 424-456).

### 3. Existing sidecar rows mean completed presentation content

`tools/check_external_coverage_assignments.py:48-53` fixes the exact CSV
header to:

`coverage_id, packet_id, source_locator, present_content_item_ids`.

There is no row kind or metadata status. `Assignment` at lines 81-87 has
those four payload fields and an internal `location` field.

`iter_assignments`, lines 424-496, requires:

- A canonical historical coverage ID.
- A nonempty `packet_id` resolving to an independently admitted packet
  (lines 467-472).
- A nonempty source locator.
- A compact JSON array of sorted unique content-item IDs, which must be
  nonempty and belong to that admitted packet (lines 473-483).
- Correct shard count, first/last IDs and exact byte hash.

`read_admitted_packets`, lines 302-420, validates the packet-admission
projection hash and byte count, admission status, all six passing content
verification categories, actual packet hash, identified presentation,
verified standing and matching nonempty content projection. Packet-declared
coverage assignments are crosschecked against the sidecars.

The packet schema agrees: `spec/presentation-packet.schema.json:441-507`
defines `obligation_links.coverage_assignments` using the fields
`obligation_id`, `assignment_status`, `source_locator`,
`present_content_item_ids`, and `owed_artifact_ids`. Its only statuses are
`open` and `fulfilled`. A fulfilled assignment requires present content and
no owed artifact; an open one requires an owed artifact and no present
content. This is not a metadata-classification interface.

### 4. Current reconciliation accounting has only two outcomes

`validate_index` in `tools/check_external_coverage_assignments.py:499-614`
requires the exact index field set and version. It streams the pinned
manifest while hashing its bytes and verifying unique stable IDs. A row
either matches a content assignment and increments `assignment_count`, or
increments `unassigned_count` (lines 557-590). Unknown, duplicate or
out-of-order assignments and input drift fail. `require_complete` fails
when any row remains unassigned (lines 606-607).

The result fields at lines 60-66 are `coverage_record_count`,
`assignment_count`, `unassigned_count`, `admitted_packet_count`, and
`sidecar_count`. There is no independently tracked metadata count.

### 5. Terminal readiness consumes those exact counts

The direct production consumer found is
`tools/check_terminal_readiness.py:635-650`. Its existing
`external_coverage_assignment` gate records:

- `required = coverage_record_count`
- `pass = assignment_count`
- `residual = unassigned_count`
- `status = PASS` only when the residual is zero
- `admitted_packet_count` and `sidecar_count`.

`spec/terminal-readiness-manifest.schema.json:217-230` constrains this
`coverageGate` and uses `unevaluatedProperties: false`. Adding explanatory
counts to the runtime output consequently requires the matching schema
change. The separate `presentation_packet_content_admission` gate at
consumer lines 627-633 must retain its present-content meaning.

## Smallest proposed compatibility change

**Everything in this section is proposed, not implemented.** Preserve the
same index path, the same historical catalog fields and fingerprint, and
the existing packet sidecars and their validation. Introduce one metadata
variant alongside them in version 2 of the existing index. Keep a strict
version-1 parsing branch so existing indexes retain their current meaning.

Recommended new top-level field: `metadata_dispositions`, an array of
reviewed batch records. The minimal useful batch fields are:

| Proposed field | Required meaning |
| --- | --- |
| `disposition_id` | Stable identity of this reviewed administrative decision, distinct from the historical IDs it covers |
| `disposition_kind` | Initially the specific value `acquisition_file_descriptor`; do not add a generic arbitrary-exclusion escape |
| `membership_receipt_path`, `membership_receipt_sha256` | Pin the existing complete-set receipt and its preserved selected row payloads |
| `rationale_path`, `rationale_sha256` | Pin the reviewed producer/predicate classification rationale |
| `verification_evidence` | Passing independent evidence whose recorded scope binds this disposition, exact receipt, rationale, catalog fingerprint and selected IDs |

The receipt already carries the 409 IDs, original payload digests, source
and parent, predicate and total count. Derive membership from that evidence
instead of adding a parallel catalog or an unrelated list of excluded IDs.
The reviewed canonical receipt may be preserved under the existing
`spec/provenance/external-coverage-assignments/` directory before admission;
the current `tmp/` receipt remains the original mechanical artifact. A
copied receipt is evidence for this same mechanism, not a new content store.

Use the existing review-evidence field conventions: the established
`aiEvidence` definition at
`spec/provenance/reviewed-presentation-packet-admissions.schema.json:67-109`
records category, result, artifact path/hash, producer, scope, actual model
configuration, consulted authorities, findings and evidence digest. The
packet builder's evidence validation is at
`tools/build_presentation_packet_admission.py:289-410`. Its validator is
currently fixed to six packet categories, so it cannot simply be called
unchanged for metadata. Reuse the applicable path/hash, authority and
independence checks in the metadata branch; retain the existing six-category
requirement for actual content packets. Do not fabricate manuscript build
or visual evidence for an administrative descriptor decision. The lead
must pin the applicable administrative review conditions before admitting
this new branch.

One reuse boundary matters for scale: the packet evidence validator reads
authority files with `path.read_bytes()` before hashing them (lines
379-385). Do not pass the 7 GB catalog into that helper or load it once per
reviewer. Validate the catalog authority identity through the existing
single streamed hash/count result; ordinary small receipts and review
artifacts can retain the current byte-hash checks.

### Required consumer behavior

Within the existing `check_external_coverage_assignments.py` checker:

1. Parse and validate each metadata disposition and its evidence. Require
   the receipt's catalog path/hash/bytes/count to equal the existing index
   identity. A metadata record with only a claimed count or unsigned list
   of IDs does not pass.
2. Check the selected original records and their canonical payload digests
   against the stated predicate and source/parent evidence. Apply only the
   exact reviewed membership; `SRC-068-H278` and `SRC-068-T11119` remain
   excluded from this 409-row disposition.
3. During the checker's existing manifest stream, match each selected ID
   and payload. Reject overlap between two metadata batches, overlap with
   a packet assignment, unknown IDs, missing members, source/parent drift,
   and changed payloads. Keep the existing manifest hashing and uniqueness
   check. Fold this work into the scheduled reconciliation stream; do not
   add another per-batch full-catalog scan.
4. Preserve `assignment_count` as content assignments, add
   `metadata_disposition_count` and `metadata_batch_count`, and compute
   `unassigned_count = coverage_record_count - assignment_count -
   metadata_disposition_count`. Completion means every historical row has
   one validated disposition; metadata counts never become content-item
   or admitted-packet counts.

Update `check_terminal_readiness.py` so that this gate's `pass` is the sum
of the two disjoint disposition counts, with separate
`content_assignment_count`, `metadata_disposition_count`, and
`metadata_batch_count` fields visible in the gate. Extend `coverageGate`
in the existing readiness schema to admit those fields. Keep the separate
presentation-content gate and its denominator unchanged.

The minimal runtime/schema edit surface is therefore:

- `spec/external-coverage-assignment-index.schema.json`
- `tools/check_external_coverage_assignments.py`
- `tools/check_terminal_readiness.py`
- `spec/terminal-readiness-manifest.schema.json`

The actual reviewed decision would then be added to the existing
`spec/external-coverage-assignment-index.json` by its root owner. Existing
packet schemas, packet admission, original requirement ledgers and the
historical CSV do not need a metadata escape or changed binding.

Future implementation verification should cover legacy version-1 behavior,
one valid metadata batch, stale evidence or corpus identity, overlap with
content assignment, duplicate metadata coverage, included parent/preceding
record, and payload mismatch. These are proposed compatibility cases;
none was executed in this research assignment.

## Current fingerprints and limits

| Inspected artifact | SHA256 verified in this block |
| --- | --- |
| `spec/external-coverage-assignment-index.json` | `2A2BF44FCB19D0B823CF2962751AD05322CDBF269313E38F94DA163B7CCB58BD` |
| `spec/external-coverage-assignment-index.schema.json` | `F87AEE92B5714B2C89B02E2EB258E64C26634084D7F71CE412725D426F507266` |
| `tools/check_external_coverage_assignments.py` | `76E962E77E02C963C87429BEE7A65ED022C2FFEC1A6A67931668D5743E46B89D` |
| `tools/check_terminal_readiness.py` | `B4062BC9410023CA56E7EE927D49BCD514424011778911AF0E45D74D92524804` |

The assignment index/schema and complete 638-line coverage checker were
read; relevant packet-schema, admission-evidence and readiness-consumer
sections were read directly. Searches located the direct production
consumer described above. The Research skill guided primary code tracing
and this single-note output; the assignment's no-delegation instruction
controlled execution. No tests, builds, catalog scans, membership checks,
new source acquisition or canonical binding change occurred.
