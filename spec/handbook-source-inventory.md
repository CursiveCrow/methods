# Handbook-source reverse-audit inventory

This generated baseline inventories every source file and every physical
line of every UTF-8 text file in the exact handbook snapshot used by the
inherited-source audit. Binary inputs remain covered by their whole-file
byte counts and digests rather than being treated as text lines.
It is not a semantic-unit inventory and makes no provenance or correctness
claim. Every row remains `open/unmapped` with no source-authority IDs.

- Snapshot source files: 214.
- Physical source lines: 35,669.
- Total inventory records: 35,883.
- Reverse provenance status on every row: `open/unmapped`.
- Semantic handbook-unit inventory and keyed provenance join: `OPEN`.

The CSV is lossless at the file/physical-line level through exact byte
counts and SHA-256 digests. Later semantic-unit records must cover these
rows without using file/line presence as a content-fidelity verdict.
