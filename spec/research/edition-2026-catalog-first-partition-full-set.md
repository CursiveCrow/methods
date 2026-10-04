# CAT-01: full-catalog verification of the first descriptor batch

Date: 7 September 2026. This completes the global membership and uniqueness
check left open by `edition-2026-catalog-first-partition.md`. It supplies
mechanical evidence for the proposed metadata disposition. Independent
semantic review, reconciliation admission and catalog rebinding remain due.

## Exact corpus and result

The complete `spec/full-compendium-coverage-manifest.csv` was read as CSV
while hashing every original byte. Observed values match the pinned corpus:

| Measure | Verified value |
| --- | --- |
| Bytes | 6,947,214,502 |
| SHA256 | 69d0f7ccb89e9be070366102f958a4034f632088b269a92ee244bfa5b41d55e8 |
| Data records | 9,162,150 |
| Source records | 68 |
| Hierarchy records | 27,979 |
| Raw topic records | 9,134,103 |
| Selected children of SRC-068-H278 | 409 |
| Selected stable IDs | SRC-068-T11120 through SRC-068-T11528, exactly once each |
| Extra or malformed children of that parent | 0 |

Every source identifier matches its consecutive producer ordinal and each
source group occurs once. Every hierarchy and topic identifier within that
group matches its respective consecutive H or T ordinal. Together with
disjoint prefixes, these checks establish uniqueness of every historical
stable ID without retaining millions of strings in memory. This establishes
identity uniqueness, not uniqueness of source content or intellectual units.

For every child of H278, the full original displayed string matched the
previous note's exact descriptor grammar; the topic and scratch ordinals,
source ID, hierarchy path and parent agreed. The selected sequence equals
exactly the expected 409 IDs. The source and hierarchy descriptors resolve
uniquely and their titles agree with every selected child. The preceding
SRC-068-T11119 record retains its separate H277 parent and remains excluded.

## Reproducible evidence

The bounded checker is
`tmp/edition-2026-catalog-first-batch/verify_membership.py`. It reads only the
historical catalog and generates one new receipt; it changes no catalog or
assignment record. It refuses to overwrite an existing receipt.

Command from the manuscript root:

    C:\Python314\python.exe -X utf8 tmp/edition-2026-catalog-first-batch/verify_membership.py

The generated receipt is
`tmp/edition-2026-catalog-first-batch/membership-receipt.json`, SHA256
`53fda56272025d31368a02b6ac4cb9203de5604ac44134024fff6ad903e76ced`.
It preserves all original fields of all 409 selected rows, the extracted
descriptor fields, each original-row payload digest, the full source/parent
join, the preceding excluded record, corpus identity, predicate and counts.
Payload digests use UTF-8 compact JSON in the explicitly fixed CSV-field order;
they are not represented as raw CSV-line hashes.

The note and receipt preserve original retrieval dates, mapping states,
source metadata and ordered locator lists. A blank child source field still
inherits through the source record; it does not erase that source evidence.

## Remaining CAT-01 work

Obtain independent review of the classification predicate, producer evidence
and this complete-set receipt; then record the 409 dispositions through the
existing reconciliation mechanism. The descriptor row is acquisition
metadata; every referenced file and substantive source treatment retains its
own obligations. Neither this check nor the old word `topic` decides those
substantive obligations.

The other 743 scratch descriptors and all other catalog records require their
own semantic dispositions. No entire source group was classified as metadata,
no book content was credited as written, and no validator was rebound to a
new catalog. Full catalog reconciliation and the five new reasoning parts
remain substantial work.
