# Inherited-source audit-interval baseline

Generated mechanically from the five-column frozen-source restoration ledgers. The CSV is the complete ordered interval-audit baseline; this file records the coverage proof, normalized counts, and non-body obligations without changing any audit wording or class string.

## Validation

- Frozen source: `source/formal-logic-reference.tex`.
- Frozen-source SHA-256: `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.
- Audited handbook-source snapshot: `spec/handbook-audit-snapshot.csv`, SHA-256 `63b405b2b9d1384ee32ae963e053d5c971b90dfe34d186fde0d1b2a0b3cec2ba`.
- All locator evidence and classes are historical evidence for that exact snapshot; any handbook-source drift invalidates them until re-audited.
- Physical source lines: 17,206.
- Printed-source bounds: 171--17205 (17,035 physical lines).
- Five-column audit rows parsed: 273.
- Printed audit intervals: 265.
- Blank/comment continuity intervals inserted: 6 (6 physical lines).
- Coverage verdict: every printed line 171--17205 is covered exactly once; no overlap remains.

Continuity rows have no inherited class. They exist only where the audit ledger omitted a blank or comment-only separator; a nonblank omission causes generation to fail.

## Ledger intake by audit

| Audit note | Five-column rows | Printed intervals | Printed lines |
|---|---:|---:|---:|
| `spec/research/full-transcription-audit-p01-p04.md` | 132 | 125 | 9,630 |
| `spec/research/full-transcription-audit-p05-p08.md` | 101 | 101 | 4,294 |
| `spec/research/full-transcription-audit-p09-p14.md` | 40 | 39 | 3,105 |

## Normalized contract-class counts

Synonyms in the audit notes are normalized only for counting: `shortened` maps to `abridged`, `hybrid` to `hybridized`, and `layout-only` to `layout-only relocation`. Every original single- or multi-class string remains unchanged in the CSV. A multi-class interval is counted once in each applicable row, so these rows are not mutually exclusive.
The `unsupported addition` count below includes only that class when attached to an inherited source interval. This one-way baseline does not inventory live-handbook-only material; the reverse live-handbook provenance audit remains OPEN, so zero is not evidence that no unsupported addition exists.

| Normalized contract class | Printed intervals | Lines in those intervals |
|---|---:|---:|
| full-and-accurate | 0 | 0 |
| layout-only relocation | 1 | 13 |
| altered | 204 | 14,057 |
| abridged | 172 | 12,558 |
| omitted | 43 | 2,486 |
| hybridized | 108 | 8,662 |
| unsupported addition | 0 | 0 |

## Content-bearing preamble obligations

These intervals are preserved from the audit's preamble inventory but are excluded from printed-body coverage and class counts. The first audit row includes implementation/layout data because the audit itself recorded that obligation; its original class and wording remain unchanged.

| Stable ID | Source lines | Audit | Controlling function | Original class |
|---|---:|---|---|---|
| `PRE-00001-00038` | 1--38 | `spec/research/full-transcription-audit-p01-p04.md:81` | document class, packages, page geometry, color, running heads, and listing style | layout-only relocation |
| `PRE-00039-00047` | 39--47 | `spec/research/full-transcription-audit-p01-p04.md:82` | PDF title, subject, and keywords | altered |
| `PRE-00049-00055` | 49--55 | `spec/research/full-transcription-audit-p01-p04.md:81` | document class, packages, page geometry, color, running heads, and listing style | layout-only relocation |
| `PRE-00056-00070` | 56--70 | `spec/research/full-transcription-audit-p01-p04.md:83` | exact standing and common numbering of definition, example, exercise, method, convention, theorem, lemma, corollary, remark, and warning environments | altered, hybridized |
| `PRE-00072-00089` | 72--89 | `spec/research/full-transcription-audit-p01-p04.md:84` | title-index wrappers; `solution`; `proofplan` explicitly displayed as “Proof sketch.” | altered, hybridized |
| `PRE-00090-00096` | 90--96 | `spec/research/full-transcription-audit-p01-p04.md:85` | source delimiter macros | altered, abridged |
| `PRE-00097-00151` | 97--151 | `spec/research/full-transcription-audit-p01-p04.md:86` | the complete source notation declaration from `\N` through `\coNP` | altered, abridged, hybridized |
| `PRE-00152-00156` | 152--156 | `spec/research/full-transcription-audit-p01-p04.md:87` | exact rule, side-condition, tuple, and definition-sign macros | altered, hybridized |
| `PRE-00158-00169` | 158--169 | `spec/research/full-transcription-audit-p01-p04.md:81` | document class, packages, page geometry, color, running heads, and listing style | layout-only relocation |

## Nonprinted document controls

These controls came from five-column audit rows but lie outside the printed bounds and therefore do not contribute to printed-body coverage or classification counts.

| Stable ID | Source lines | Audit source locator | Audit |
|---|---:|---|---|
| `CTL-00170-00170` | 170 | 170--197 | `spec/research/full-transcription-audit-p01-p04.md:93` |
| `CTL-17206-17206` | 17206 | 17206 | `spec/research/full-transcription-audit-p09-p14.md:85` |

## Complete interval-audit baseline

See `spec/inherited-source-map.csv`. This is not yet the complete contract provenance map: typed handbook destinations, stable labels, per-dimension completion evidence, and independent verification remain open. Each row currently supplies the stable interval ID, literal inclusive source bounds and digest, audit file/line, source-surface description, audited-snapshot locator/evidence, exact original class string, normalized count classes, and exact restoration obligation.
