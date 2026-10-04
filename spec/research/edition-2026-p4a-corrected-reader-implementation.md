# Edition 2026 P4a: corrected-reader candidate implementation

Implementation checkpoint: 2026-09-07T16:17:04.0796266Z. This block implements candidate
construction support only. It does not implement P4b, migrate real provenance,
admit source units or provide independent acceptance.

## Exact implementation scope

- [check_inherited_restoration.py](C:/Dev/the-methods-of-reason/tools/check_inherited_restoration.py:988) adds correction_slice_bytes, predecessor custody checking, reader_source_line_map and validate_reader_correction. validate_record dispatches explicit version 4 to that branch. The original validate_restoration_artifact token-equality implementation remains the path for versions 1–3.
- [check.py](C:/Dev/the-methods-of-reason/tools/check.py:760) records exact-capture versus corrected-reader authorization and the validated source-line projection. It rejects scan/validation byte drift. Its future-reference rule uses only mapped original occurrences for corrected files.
- [audit_tables.py](C:/Dev/the-methods-of-reason/tools/audit_tables.py:89) loads validated provenance rather than deriving original line numbers from a filename. New/replaced lines have no original locator. Corrected-container proofs are described as reader proofs, and anchor counters follow actual validated reader-environment order.
- The two existing restoration/scope test files contain isolated regression fixtures and cases for this feature.
- [The provenance README](C:/Dev/the-methods-of-reason/spec/provenance/README.md:385) documents the complete closed record shape and range convention.

No source-unit terminal schema, source-unit generator, terminal-readiness
predicate, style, canonical symbols, generated file or real SRC record was
changed. The eight currently corrected real SRC records still have version 1.

## Record semantics

Version 4 requires exactly one reader_correction object. It supports plain,
reader-facing SRC intervals; the closed governed-layout and PRE/CTL/SEP cases
remain outside this version. Its disposition must be full reconstruction,
never full transcription or layout-only relocation.

The existing frozen authority, source_locator and source-unit IDs remain
unchanged. The corrected artifact has its own actual raw/canonical hashes,
byte/line counts and same locator-bound reader path. The corrected destination
must name that artifact and remains open/missing.

reader_correction requires:

1. The exact candidate-kind marker and a stable correction ID.
2. A hash-bound copy of the approved correction policy and its exact locator.
   The direct-correction authorization is checked in that policy text.
3. A separately hashed rationale artifact and locator.
4. A hashed predecessor record. Historical chains must retain the same source,
   interval, artifact identity and source-unit evidence; stale hashes and
   cyclic/self predecessors fail. Old records are custody evidence, not
   revalidated claims about the now changed live artifact.
5. Sorted affected IDs including this SRC ID, with other IDs checked against
   the bound source-unit ordinals or present original registers.
6. The frozen interval's canonical-content hash.
7. A complete ordered edit map, with reasons and exact old/new slice hashes.

Edit ranges are zero-based, half-open line offsets relative to the frozen
interval and the complete current reader file. Insertion uses an empty source
range; deletion an empty reader range. Empty slices hash empty bytes.
All nonempty lines require terminal endings; newline normalization is the
existing CRLF/LF/CR-to-LF rule. Every unchanged prefix, gap and tail must match,
and no unexplained change, overlap, reversal, out-of-bounds range or no-op edit
is accepted. The whole current artifact is independently checked for raw
hash/size, UTF-8, BOM absence and canonical-content hash.

The version-4 comparison/evidence-scope constants explicitly say that this is
candidate identity/edit validation. The usual completeness fields and all
independent/build/visual fields remain pending. Candidate syntax scope does
not require prior build/visual admission and cannot issue that admission.

## Source-line and generated-view behavior

After validation, reader_source_line_map returns original absolute line
numbers only for unchanged spans. Every inserted/replaced hunk line maps to
None, including any unchanged token embedded in a rewritten line. This is a
conservative occurrence policy: a new correction reference must resolve
normally rather than acquire an inherited future-reference exception.

The audit collector uses this map for source metadata, reads current titles
for unmapped new text, and detects source drift between validation and parsing.
Calling source_line without a validated map returns None.

Candidate projections can be inspected through collect for internal
construction work. The default audit command deliberately blocks active
output/check acceptance when corrected candidates are present. It has no
P4b terminal-admission input yet. Removing that block or generating those rows
by hand would not be admission. Existing system-card withholding remains
unchanged.

## Verification performed

The final focused run passed **55 tests** in the existing unittest structure:

- Ten corrected-reader candidate tests, including individual insertion,
  deletion and same-line replacement plus a combined multi-edit map.
- All 39 static restoration-scope cases, including six new correction/metadata
  cases.
- Six selected existing exact/version-2/version-3 invariants.

They cover stale artifact hashes, rehashed unexplained text, incomplete and
overlapping maps, wrong slice hashes, wrong frozen authority/source interval,
wrong or rehashed unrelated policy, wrong/stale predecessor identity, unknown
affected IDs, missing correction objects, false transcription/layout
dispositions, fake build acceptance and false verification-scope wording.
They also cover duplicate wrappers, retained source syntax with pending gates,
new-reference rejection, mapped-reference policy, correction-aware metadata,
and blocked active-output promotion.

The old-version checks confirm that refreshed hashes cannot launder changed
source tokens and that governed layout cases retain their closed invariants.
The owned-file whitespace check passed.

Only isolated fixture repositories were modified by tests; no real provenance
was migrated. No TeX compilation, page render, full-book build, broad test suite
or independent mathematical/source-fidelity review was performed in this block.

## Exact next integration steps

1. Obtain independent implementation review of this bounded feature.
2. P4b must add the truthful corrected source-unit disposition/result to the
   existing schema/generator/terminal join under all six gates; P4a leaves those
   files and requirements unchanged.
3. Replace the audit command's candidate block only with a validated admission
   join supplied by that integration, not with a force flag or blanket waiver.
4. Migrate each real corrected interval separately: preserve its predecessor
   record, construct the exact cumulative frozen-source-to-reader edit map,
   attach policy/rationale and affected IDs, and keep its pending standing
   truthful. This was expressly not performed here.
5. Actual reviewer model/version evidence remains a later formal-record
   requirement. Candidate validation neither invents missing values nor treats
   text-review notes as six-gate acceptance.

The work stops at this handoff. No P4b work or real-record migration was begun.

## Implemented file hashes

| File | SHA256 |
|---|---|
| tools/check_inherited_restoration.py | 5B8BC9717A66B8DD28C2F4CA0135F369B70348BF7330379F45D4E4E93FAF881F |
| tools/check.py | 5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57 |
| tools/audit_tables.py | C732C350007F1E17F678099A1ADDCA9CB9878EFAC23350432467C08260027B53 |
| tools/test_check_inherited_restoration.py | D5962BB23F7113139F91C630A6CAC75498803D25E94BEC506B2CEBA2CA311F01 |
| tools/test_restoration_scope.py | AD66CAFF44E0493AA46BF229CBCC453C948F13CAE09E94C30567A33DD58861B9 |
| spec/provenance/README.md | 79EA4D2A5108B498581B27EAD431C64234B18DD5ADC2ADD1A75454BD188C869F |

