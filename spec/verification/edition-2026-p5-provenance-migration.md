# P5 syntax correction: candidate provenance migration

Date: 7 September 2026. These results concern the 519-line P5 snapshot
`0e4ac6ad0d39474e49d2f868c62877fd7a0f1f1eec61e24d77d806e266d81b9c`.
Subsequent internal-predicate authoring must receive its own updated record.

## Candidate identity and exact mapping

The existing version-1 SRC-09328-09438 record was preserved byte for byte at
`spec/provenance/history/SRC-09328-09438.v1-cad02c7e.json`, SHA256
`cad02c7e015bfd2f4643658ece75dc269bb44ee45b046d4d318d29a0aad86970`.

The installed version-4 candidate is `spec/provenance/SRC-09328-09438.json`,
SHA256 `a1449293801f79b7d7b87a0d03056d470665eda4abcec2c56d5566ba99322975`.
It retains the exact frozen source authority, interval, audit evidence and
ten source units. Its immutable rationale is
`spec/research/edition-2026-p5-syntax-provenance-rationale.md`, SHA256
`d9ef9b381f2a6589cd56c06dbd9c8aea58c7da6f6a02c7b3b082346d7dbc1c5c`.

The full transformation has ten edit hunks. The original 111-line interval
and the 519-line reader have separate identities. Every unchanged gap and
tail was checked; replaced or inserted reader lines receive no invented
original-source coordinate. The last hunk removes the final blank line.

Actual command:

    C:\Python314\python.exe tools/check_inherited_restoration.py --record spec/provenance/SRC-09328-09438.json

Result: `RESTORATION CHECK OK: SRC-09328-09438`. Its scope is source/static
identity, edit replay and candidate boundaries only. All content completeness,
independent, build, visual and legacy human fields remain pending.

## Ten linked open source-unit records

Preserved the complete prior set as
`spec/provenance/history/reviewed-source-units.before-p5-syntax-b776ce70.json`,
SHA256 `b776ce7086d449fc5f3e847eff36de095b2bec97642b47d48a4928a3582ea723`.
Updated only source units 637–646 in
`spec/provenance/reviewed-source-unit-records.json`: correction identity,
record hash, destination hash, static scope and seven-field correction snapshot.
The 1,045 other record objects are unchanged. All 1,055 records remain present.

The resulting set has SHA256
`87b6b93656a8322278874be4c15d8254aa8308a6bf118301f27e3e1be38ec34d`.
Every changed record remains open/missing, pending/unclassified, with every
content and independent/build/visual field pending. Mechanical static PASS
is rebound only to the actually validated candidate.

The live read-only `validated_reviewed_rows` join passed the migrated P5
records and next stopped at array index 739, original unit 740, for
`SRC-10675-10769`: the constructible-hierarchy reader has 4,283 bytes while
its existing record expects 3,872. This identifies the next stale restoration
record. It is not a passing full join or a new content verdict for that file.

The earlier three C5/C6 version-4 records, SRC-07295-07468,
SRC-07851-08048 and SRC-08710-08876, remain installed and were traversed by
this join. Their 33 linked open records were already in the preserved input
set. This P5 migration neither rewrites nor independently admits those units.

No generated crosswalk, active notation view, terminal disposition, manuscript
build or final publication artifact was promoted. Publication finding PT-1
requires additional arithmetic construction and remains a separate open task.
