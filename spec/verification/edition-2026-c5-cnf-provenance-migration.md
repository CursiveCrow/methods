# C5 CNF: first live corrected-reader provenance migration

Date: 7 September 2026. Scope: SRC-01946-02186 and its twelve already-open
source-unit records. This is candidate identity/mechanical evidence, not
formal admission.

## Preserved identities

- Frozen source/formal-logic-reference.tex remains unchanged and is validated
  against the existing authority digest by the restoration checker.
- The predecessor interval record is preserved byte for byte at
  spec/provenance/history/SRC-01946-02186.v1-e457571c.json, SHA256
  E457571C6C4AA33473B0C949E44D496749BB353EDCC377C9FF7BD4AC0C5B1D2F.
- The entire previous source-unit review-record set is preserved at
  spec/provenance/history/reviewed-source-units.before-cnf-v4-86d26c24.json,
  SHA256 86D26C246D0961795AD0324361E76625954A5734A8C84ABE813AC16BDAD80E47.

## Installed candidate and exact edit map

spec/provenance/SRC-01946-02186.json is now version 4, SHA256
527CA7743BADC27229147DACDC92F78FAEFF94C26138935BBB93F18C92ACA08D.
It pins the unchanged frozen interval separately from the current reader
artifact, which retains SHA256
185C35156F2E1983B1BEF028888C3FF2A0DFFF333366CFF1A3D2769225E37468.

The complete comparison identified a four-line forward-link insertion and
deletion of the former final blank line. Both operations are recorded with
half-open source/reader ranges and exact slice hashes; every intervening line
matches. The rationale is edition-2026-c5-cnf-provenance-rationale.md.

The installed record passed:

    C:\Python314\python.exe tools\check_inherited_restoration.py --record spec\provenance\SRC-01946-02186.json

Reader lines 210–213 map to no original line. Reader line 214 maps to original
line 2155. All candidate completeness dimensions and independent/build/visual/
human fields remain pending; the two mechanical source/static fields pass.

## Linked open source-unit records

The twelve records for ordinals 155–166 already had open/missing disposition,
pending/unclassified audit results, all completeness dimensions pending,
all AI/build/visual fields pending, and one mechanical static evidence item.
Their restored-record hash, destination hash and corrected presentation identity
now match version 4. The static evidence has the actual new scope and required
correction snapshot. No content or production gate was marked pass.

All 1,043 other record objects compare unchanged. The live set still contains
1,055 records, with SHA256
B4A666CBC6C491A6AA324E126D9909A1C19085FC245146506365B7063BD75C8D.

The actual live join processed these twelve migrated records and continued
until a later preexisting stale restoration at record index 498. It then
stopped with the concrete byte mismatch 12808 != 8261. This is not a passing
full crosswalk/readiness check. The remaining corrected fragments and their
linked records still require controlled migration; no generated crosswalk or
active audit view was manually patched or promoted.

The P4b implementation's initial findings and their independent repair recheck
remain in edition-2026-p4b-independent-review.md and its -r2.md companion.
This live migration does not convert those implementation checks into any
mathematical or publication acceptance.
