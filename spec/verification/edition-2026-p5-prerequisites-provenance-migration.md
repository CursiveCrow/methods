# P5 prerequisite provenance migration

Date: 7 September 2026 local time; completed checks around 8 September
00:00 UTC. This is source/static candidate validation, not content admission.

## Current validated candidates

| Record | Reader extent and hash | Current record hash | Original units |
| --- | --- | --- | --- |
| SRC-09262-09327 | 253 lines; `b49a3b30aff36050841d4f384a6ba80fcf36f4661b3c4085e58d2371b4e003cb` | `7b8f17f8ecdd1b9c902321ee0f46f5a32389902a0fde6815c6120f58a7d69ddb` | 632–636 |
| SRC-09328-09438 | 546 lines; `a6e37fa592e81b888c14a2da97cc70f1a05ec69bae0ce4d36e2e60c59f09c541` | `eaa9c18d815aaaab71acfa949d497479779217151fb3f4f951214fa052003593` | 637–646 |

Both are version-4 corrected-reader candidates. Their exact maps have one
and eleven changed source/reader slices respectively. The immutable rationale
is `spec/research/edition-2026-p5-prerequisites-provenance-rationale.md`, SHA256
`a8764e6fa66daa86e37a551cde64c12950653de57c8197a8630323ae35e1a70d`.

The actual existing validator returned RESTORATION CHECK OK for each command:

```text
C:\Python314\python.exe -B tools\check_inherited_restoration.py --record spec\provenance\SRC-09262-09327.json
C:\Python314\python.exe -B tools\check_inherited_restoration.py --record spec\provenance\SRC-09328-09438.json
```

These checks establish the exact archive/interval, current reader identity,
complete edit replay, wrapper route, membership and pending boundaries only.

## Preserved evidence and limited record changes

Predecessor files were copied without overwriting any differing existing file:

- `spec/provenance/history/SRC-09262-09327.v1-760d1f94.json`, SHA256
  `760d1f944d5fd8ed2bb84f431e16b4981620fb7023780dc6936d8c5878aaefba`.
- `spec/provenance/history/SRC-09328-09438.v4-a1449293.json`, SHA256
  `a1449293801f79b7d7b87a0d03056d470665eda4abcec2c56d5566ba99322975`.
- `spec/provenance/history/reviewed-source-units.before-prerequisites-87b6b936.json`,
  SHA256 `87b6b93656a8322278874be4c15d8254aa8308a6bf118301f27e3e1be38ec34d`.

The current reviewed source-unit set has SHA256
`bd30c4a53425566391ad036d759d51ce02b74c7d8e9ba9e23ff6fa7eae8b5796`.
Direct before/after object comparison verifies exactly fifteen changed
ordinals, 632 through 646; all 1,040 other objects are identical and the total
remains 1,055. Changes are current restoration/destination identities,
presentation descriptions and their static correction snapshots. All fifteen
retain open/missing, pending/unclassified, pending completeness and pending
independent/build/visual gates. No original obligation or field meaning is waived.

The original 66-line representability prefix still hashes to
`75a27e87080116a235a904daedabe2a70dff472ba27ca8a454c448dfd4b58bb6`.
Removing only reader lines 496–522 from the current syntax fragment recovers
the preceding 519-line reader hash
`0e4ac6ad0d39474e49d2f868c62877fd7a0f1f1eec61e24d77d806e266d81b9c`.
The frozen source hash remains
`0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
No manuscript text was changed by this migration.

## Full join result and continuation

The read-only call to
`build_source_unit_audit_crosswalk.validated_reviewed_rows(Path.cwd())`
passed these refreshed records and stopped at array index 739, source unit
740, SRC-10675-10769. That constructible-hierarchy reader has 4,283 bytes,
while its stale version-1 record expects 3,872. The command exited 1.
The full source-unit join therefore remains failing. The next assignment is
the exact correction/provenance reconciliation for that fragment, followed
by the next actual residual. This result is not a whole-book readiness pass.

The temporary helper `tmp/edition-2026-p5-p16-integration/prepare_provenance.py`
only computed reviewable patches; all record edits were applied through
the file-editing tool. It is a construction aid, not a new acceptance system.
