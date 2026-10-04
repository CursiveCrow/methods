# Inherited corpus manifest

This manifest fixes the inherited content authority used by the
full-compendium transcription contract. It records artifacts and integrity
facts only; it does not summarize or reinterpret their contents.

## Authoritative artifacts

| Role | Path | Size | Integrity |
|---|---|---:|---|
| TeX source authority | `source/formal-logic-reference.tex` | 762,835 bytes; 17,206 lines | SHA-256 `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc` |
| Controlling inherited render | `source/formal-logic-reference.pdf` | 2,042,303 bytes; 251 pages | SHA-256 `0a8fb84042175343e5ba8bbcf65d4804d8a4019367edb3d22473927a3399bb3f` |

The PDF title is *Formal Logic: Language, Semantics, Deduction, and
Metatheory*. Its pages are US Letter (`612 × 792` points), PDF version 1.5.

The printed TeX body occupies lines 171--17,205, between
`\begin{document}` at line 170 and `\end{document}` at line 17,206. The
preamble at lines 1--169 is the
controlling implementation record for the source render and the notation
commands used by the inherited corpus.

## Derived integrity records

- `spec/inherited-corpus-manifest.json` is the machine-readable artifact
  record used by the integrity gate.
- `spec/COMPENDIUM-VOLUME-MANIFEST.md` and
  `spec/compendium-volume-manifest.json` retain this exact inherited record as
  internal authority evidence while explicitly excluding it from the single
  public book, `handbook/main.pdf`.
- `tools/check_inherited_corpus.py` accepts only the exact top-level JSON keys
  `schema_version`, `tex`, and `pdf`; requires integer schema version `1`;
  requires the exact role-specific nested keys and field types; requires the
  canonical `source/formal-logic-reference.tex` and
  `source/formal-logic-reference.pdf` paths and every frozen recorded value;
  and checks each file's actual byte count and SHA-256 digest plus the TeX
  file's actual line count. Extra, missing, mistyped, or renamed fields fail.
- `spec/source-unit-inventory.csv` records named structural and content units,
  exact line intervals, contextual headings, labels, and per-unit SHA-256
  digests. The validated inventory contains 1,055 active units: 263 headings
  and 792 block environments.
- `spec/source-unit-inventory.md` records generation counts and the whole-file
  digest.
- `tools/source_unit_inventory.py` is the deterministic generator.
- `spec/source-unit-audit-crosswalk.csv` joins all 1,055 active units to the
  exhaustive interval-audit baseline while leaving every typed destination,
  stable label, completeness result, and verification result open or pending.
- `tools/build_source_unit_audit_crosswalk.py` regenerates and checks that
  crosswalk; it does not infer a provenance or content verdict.
- `tools/check_transcription_audit_coverage.py` verifies that the combined
  audit ledgers account for every nonblank, noncomment printed source line.
- `tools/check_full_compendium_controls.py` orchestrates the independently
  maintained compendium controls. A successful run means only that every
  control it invoked accepted its own recorded structure and integrity
  conditions; it is not a content-restoration, semantic-correctness,
  completeness, proof, AI-review, rendered-page, or user-acceptance verdict.

Derived files do not replace either authoritative artifact. If a derived
record disagrees with the TeX source or PDF, the disagreement is a failed
integrity gate and must be resolved before transcription continues.

The inherited-corpus checker does not compare the TeX semantics to the PDF,
prove any theorem, assess the accuracy or completeness of the logical
material, inspect every rendered page, or establish that any construction
draft transcribes the inherited corpus. Byte identity with the frozen records
is an integrity fact only.

The validated active counts include 112 theorem environments and 125 proof
environments. The additional lexical `\begin{theorem}` at line 14,882 and
`\begin{proof}` at line 14,889 are literal TeX printed inside the `lstlisting`
at lines 14,881--14,895, not active environments. All six active `longtable`
environments are inventoried.
