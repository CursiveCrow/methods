# CAT-01: bounded metadata-disposition compatibility

Date: 2026-09-07. Implementer: `standard_pa_argumentation_publication_review`. Work completed within the assigned 23:10--23:55 UTC block; the concrete implementation/test checkpoint was sent at approximately 23:20 UTC.

## Implemented result

The existing external-coverage index and checker now accept a strict version-2 metadata branch alongside the unchanged content sidecars. Version 1 retains its exact top-level field set and content-only meaning. Its `SCHEMA_VERSION` constant remains 1 for existing callers; the separate supported metadata version is 2. Version 2 requires `metadata_dispositions`, which may be empty.

The sole implemented kind is `acquisition_file_descriptor`, and the required `descriptor_profile` is exactly `src068-h278-v1`. This profile covers the documented 409 topic records `SRC-068-T11120` through `SRC-068-T11528` under `SRC-068-H278`. Other profile values and disposition kinds fail. The other 743 scratch descriptors have different producer profiles and require separate reviewed implementations. No live disposition was created or admitted.

The actual interface note, complete coverage checker, relevant admission evidence schema/validator, readiness consumer/schema, existing regression fixtures, first-partition/full-set notes, receipt structure, and receipt-producing payload-hash convention were read before implementation. The existing live index and mechanical receipt remain unchanged. All writes are confined to the seven files listed below. Other dirty repository work was preserved.

## Version-2 batch contract

Each metadata entry has exactly these fields:

- `disposition_id`: an administrative identity matching `META-[A-Za-z0-9][A-Za-z0-9._-]*`, unique in the index.
- `disposition_kind`: `acquisition_file_descriptor`.
- `descriptor_profile`: `src068-h278-v1`.
- `membership_receipt_path` and `membership_receipt_sha256`: a preserved receipt under `spec/provenance/external-coverage-assignments/` and its exact lowercase SHA-256.
- `rationale_path` and `rationale_sha256`: the actual reviewed rationale under `spec/research/` and its exact lowercase SHA-256.
- `verification_evidence`: exactly three separate passing records, one each for `source_fidelity_ai`, `topic_specialist_ai`, and `adversarial_publication_ai`.

The evidence records use the established packet-admission AI field convention: category, result, artifact path/hash, producer identity, recorded scope, model, model version, instructions, consulted authority files/locators, findings, and evidence digest. The implementation does not populate real reviewer metadata. Real reviews must record their actual configuration and findings.

`metadata_review_scope(disposition, index)` defines the exact required `recorded_scope`. It is the disposition ID followed by `disposition_sha256=<digest>`. The digest is the existing canonical compact-JSON SHA-256 of the disposition fields excluding evidence itself, plus the catalog path, hash, byte count, and record count. Thus it binds the kind/profile, exact receipt and rationale identities, and complete catalog identity without a self-referential evidence hash. The pinned receipt in turn binds the selected IDs and original row payloads.

Each review must list the exact receipt, rationale, and catalog as consulted authorities, with sorted unique canonical repository paths and matching hashes. It must include this exact membership locator:

```text
acquisition_file_descriptor:SRC-068-H278:SRC-068-T11120..SRC-068-T11528
```

Passing evidence must have distinct artifact filesystem identities, distinct bytes, and distinct producer identities after the existing Unicode/case/whitespace normalization. The index, catalog, receipt, and rationale cannot serve as their own review artifacts. Hardlink aliases and copied self-evidence bytes are rejected. The evidence digest must equal the artifact digest; empty model/configuration/findings records, missing categories, failed results, stale scopes, stale artifacts, and stale authorities fail.

This is administrative evidence. No fake static/build/visual records are required or synthesized for descriptor decisions. The unchanged content-assignment path still verifies all six content categories, admitted packet identity, nonempty present-content projection, source locators, and packet-declared assignment consistency.

## Receipt and membership validation

The runtime accepts the existing receipt's exact field structure. Its catalog path/hash/bytes/count must equal the index. The descriptor regex is the fixed producer grammar from the research note, not a regex executed on the receipt's authority. A broader regex or different predicate fails even when accompanied by a desired count.

All 409 selected entries must occur in the exact documented ID order. Each must have:

- The complete fourteen-field original catalog record and its compact UTF-8 JSON payload hash in CSV-field order.
- The exact topic/source/parent identity, preserved retrieval date and mapping status, and the expected three-element hierarchy path.
- The full TOPIC/SCRATCH/path/byte-count/physical-line-count/SHA-256 descriptor syntax and exact extracted descriptor fields.
- The fixed relation between topic ordinal and scratch ordinal, covering precisely scratch 0001--0409.
- A canonical acquisition path stored as data. No referenced acquisition file is opened or credited as read.

The receipt also preserves the source, parent, and preceding excluded record. The source and parent structures and their joins are checked; `SRC-068-H278` and `SRC-068-T11119` never enter the selected metadata count.

During the existing catalog stream, the checker compares all 412 watched original records (409 selected, source, parent, and preceding excluded record), checks selected payload/source/parent equality, and rejects extra children of H278. The existing disk-backed global stable-ID uniqueness check and complete byte hash/count remain active. Unknown or missing watched IDs, duplicate IDs, duplicate disposition identities, overlapping metadata batches, and overlap with either packet-declared or actual sidecar content assignments fail. Receipt type/source totals are compared with totals from this same stream.

Only the bounded receipt and evidence structures are retained in memory. The catalog authority hash is reused from the index during evidence parsing and then verified by the existing complete manifest stream before any result is returned. It is never loaded by `read_bytes()` or hashed once per review. A catalog hardlink presented as another authority is rejected before any duplicate read. Small authority hashes are cached for the invocation.

## Accounting and downstream meaning

`CoverageAssignmentResult.assignment_count` remains the number of content assignments. Two default-zero result fields were added after the original five fields, preserving existing positional constructors:

- `metadata_disposition_count`: number of catalog rows covered by validated descriptor dispositions.
- `metadata_batch_count`: number of validated metadata batches.

The stream counts the disjoint cases directly, giving `unassigned_count = coverage_record_count - assignment_count - metadata_disposition_count`. `require_complete` still rejects any residual.

The existing terminal `external_coverage_assignment` gate now reports their sum as `pass`, with explicit `content_assignment_count`, `metadata_disposition_count`, and `metadata_batch_count`. The readiness schema describes these fields. The separate `presentation_packet_content_admission` gate and its denominator are unchanged. Descriptor decisions create no admitted packets or present-content items.

## Verification actually run

From `C:\Dev\the-methods-of-reason`:

```text
C:\Python314\python.exe -B -m unittest tools.test_check_external_coverage_assignments tools.test_check_external_coverage_metadata tools.test_check_terminal_readiness
```

Final result: **34 tests passed**, exit code 0, reported unittest runtime 3.494 seconds. A negative readiness fixture deliberately prints `terminal readiness: FAIL (upstream register closure check failed: register obligation closure CSV is stale)`; the unittest result is `OK`. The first combined run rediscovered an imported legacy test class; its duplicate discovery was removed before the final count. No production test baseline was changed.

Coverage includes strict version-1 and version-2/schema behavior; a valid 409-row batch; exact residuals and complete disjoint accounting; all six real-content review gates; missing, failing, stale, reused, or malformed review evidence; stale receipt/rationale/artifacts/catalog; broad predicate and unsupported profile rejection; parent/preceding inclusion attempts; duplicate selected records; payload/source/parent drift; missing and extra members; duplicate/overlapping metadata batches; sidecar and packet-declared content overlap; hardlinked self-evidence; catalog-authority aliases; copied review bytes; a single manifest stream; and prevention of a catalog `read_bytes()` authority load. A readiness regression verifies that metadata reconciliation leaves the presentation-content gate unchanged.

Both modified JSON schemas also passed `jsonschema.Draft202012Validator.check_schema`. The unchanged live version-1 index passed the expanded index schema. These checks read no catalog.

The existing mechanical receipt was separately passed to `read_descriptor_receipt` against the existing index identity. Result: **409 selected IDs and 412 preserved watched records**. This was structural compatibility of the actual receipt; it did not rerun catalog membership, validate semantic reviews, or admit a disposition.

The preserved live artifacts were rehashed:

| Artifact | Unchanged SHA-256 |
| --- | --- |
| `spec/external-coverage-assignment-index.json` | `2A2BF44FCB19D0B823CF2962751AD05322CDBF269313E38F94DA163B7CCB58BD` |
| `tmp/edition-2026-catalog-first-batch/membership-receipt.json` | `53FDA56272025D31368A02B6AC4CB9203DE5604AC44134024FFF6AD903E76CED` |

No 7 GB catalog scan, source acquisition, book build/render, live-index edit, ledger edit, packet-projection edit, actual review/admission-record edit, or subdelegation occurred in this block.

## Changed-file hashes and remaining work

SHA-256 values at implementation handoff:

| File | SHA-256 |
| --- | --- |
| `spec/external-coverage-assignment-index.schema.json` | `79413A9179E7F31155D4E01BE781E5C1BC2EEB07B6FA4BC38EDF7A80AC66EBF2` |
| `tools/check_external_coverage_assignments.py` | `9585699235804312E88C1DF5D2053BB8C2E8F0144A403E977A8865C9E63753E5` |
| `tools/check_terminal_readiness.py` | `9673AE24E7E0C84662D97445F89BD9278A004CB61A5DB51035F07F710F2FF964` |
| `spec/terminal-readiness-manifest.schema.json` | `D22510C6BBB7365BAFF886048A34466A52C2D95594F349AA0551421668110711` |
| `tools/test_check_external_coverage_metadata.py` | `B1B680B213DC9481A74960359A6EC7CD94887E78951631E3E5FBCF51A8D49451` |
| `tools/test_check_terminal_readiness.py` | `E7DCA836229451F282B03A6E8514ECAFFFFC2B67771BF0D680628A41C3ABC7B5` |

This note is the seventh owned output; its hash is returned externally after writing.

The root must preserve the reviewed receipt at its admitted provenance path, obtain three actual independent semantic reviews of the exact disposition/receipt/rationale/catalog/profile scope, and then add a real version-2 batch through the existing index. The next scheduled reconciliation must stream the actual catalog and verify those records. This block demonstrates structural compatibility and regression behavior on bounded fixtures; production-scale timing was not measured.

Evidence validation checks recorded configuration, identity, binding, and independence properties. Whether the reviews faithfully report the actual model configuration, full reading, and semantic conclusions remains an independent review/admission responsibility under the edition contract. No implementation can infer those facts from a passing string alone. Future descriptor profiles need reviewed producer grammars and membership rules. Full CAT-01 reconciliation and substantive presentation admission remain open.
