# Full-transcription readiness

**Status: FAIL / whole integrated book untrusted (2026-08-14).**

The earlier `phase4-p*.md` verification notes were written against a migration
policy that expressly allowed proof compression, source-unit retirement,
exercise retirement, pointer substitution, representative sampling, treatment
ceilings, and preservation merely "in substance." The user has rejected that
policy. Those notes remain useful as evidence of what was changed, but none of
their PASS verdicts establishes compliance with
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`.

This failure applies to every existing section, including committed Parts 1--7,
uncommitted Parts 8 and 12, stubbed Parts 9--11 and 13, Part 14, all annexes,
calculus sheets, symbol records, and generated apparatus.

## Known disqualifying practices recorded by the old notes

- Part 1 records approximately 3.7:1 source compression and explicit retirement
  of scope material, examples, inference-rule material, and exercises.
- Parts 2--4 record 40--60 percent proof-length targets, repeated shortening to
  satisfy those ratios, exercise retirement, and pointer substitutions.
- Part 5 records retirement of an inherited proof sketch and exercises.
- Part 6 records shortened complete proofs, retired exercises, and ceiling-bound
  pointer treatments.
- Part 7 records compressed framing, a retired worked derivation, seven retired
  exercise blocks, abbreviated proofs, and excluded/deferred topics.
- Part 8 work was additionally affected by editorial selection among source
  presentations, notation normalization, hybridization, and source replacement.
- Part 12 records extensive compression, rehoming by pointer, and deliberate
  retirement of exercises, solutions, feedback, rule-sheet copies, notation
  material, and source demonstrations.
- Parts 9--11 and 13 are still stubs, and Part 14 is incomplete.

These facts are sufficient to reject the existing book as a full transcription
before any finer mathematical comparison is made.

## Replacement audit

The inherited-source line audit is exhaustive rather than sampled: its three
ledgers account for every physical TeX line between `\begin{document}` and
`\end{document}` and record the current interval-level evidence against the
exact 214-file handbook source snapshot in
`spec/handbook-audit-snapshot.csv`. This is line accounting for the authority
artifact; blank lines, comments, control syntax, and document delimiters are
not thereby asserted to be reader-facing printed content. The snapshot
manifest itself is anchored by a checker constant; any source-file addition,
deletion, or byte change fails the control and makes the audit evidence
historical until re-audited. The audit does not yet supply the complete
contract provenance fields or a full-transcription verdict for every named
unit.

The register-required audit is **OPEN**. The lossless register manifest and
keyed closure ledger contain all 615 original rows. The closure ledger records
zero `COMPLETE` and 615 `OPEN`; its governed reviewed-record input is empty, so
it infers no closure. No part may regain a PASS
verdict until every inherited unit and every register obligation has complete
provenance, destination, and verification evidence and has the audit result
`full-and-accurate` or `layout-only relocation`.

The reverse live-handbook provenance audit is also **OPEN**. The semantic
handbook inventory now partitions all 61,982 physical lines in the 793-file
current construction into a deterministic semantic projection and supplies a keyed
reverse ledger. Zero rows are admitted as `mapped/reviewed`, so the interval
table's zero `unsupported addition` count is not evidence that the live
construction contains none. A lossless historical reverse baseline inventories all 214 handbook source files
and 35,669 physical lines (35,883 records total), but every row is deliberately
`open/unmapped`; file/line presence is not a semantic provenance verdict.

The separately pinned current-construction snapshot contains 793 files. Its
physical inventory contains 61,982 UTF-8 text lines and 62,775 total file/line
records, again all `open/unmapped`. These current counts describe bytes and
physical lines only. The semantic partition now exists, but its zero admitted
mappings leave the reverse provenance review open.

Working ledgers:

- `spec/research/full-transcription-audit-p01-p04.md`
- `spec/research/full-transcription-audit-p05-p08.md`
- `spec/research/full-transcription-audit-p09-p14.md`

The generated interval-audit baseline contains 282 typed records: 265 audited
intervals within the document bounds, six blank/comment continuity intervals,
nine preamble obligations, and two document controls. It covers every physical
TeX line 171--17,205 exactly once. The independent audit-coverage checker also
reports complete, single coverage of all 15,371 nonblank, noncomment TeX lines
within those bounds: zero uncovered lines and zero multiply covered lines. This
is a PASS for audit locator coverage only. It is not a claim that every
accounted line prints. The ledger verdicts themselves establish the book's
content-fidelity FAIL and remain to be restored.

The terminal physical-restoration join currently recognizes 265 of those 282
intervals as exactly accounted for by the 266 governed restoration records;
17 intervals remain residual. The record-set count and accounted-interval
count use different governed identities and therefore are not interchangeable.
The preserved `SRC-09099-09111` island is counted once and cannot be counted
again when sequential restoration reaches that source location.

The 1,055-row source-unit crosswalk connects every active heading or named
block to its exact audit interval. One thousand thirty-seven reviewer-supplied
records identify source-unit ordinals 1--1037 and link them to two hundred fifty-two
unit-bearing restoration records through `SRC-15620-15637`, with the preserved
out-of-order island `SRC-09099-09111` counted once. The restored fragment
`SRC-00171-00197` and the later fragments `SRC-11012-11052`,
`SRC-11240-11279`, `SRC-11520-11598`, `SRC-13255-13284`, and
`SRC-13410-13439`, `SRC-13862-13896`, `SRC-13897-13918`,
`SRC-14035-14051`, `SEP-14561-14561`, `SEP-14590-14590`, and
`SEP-15092-15092` contain no
source-unit inventory row and therefore create no invented crosswalk unit. All
1037 supplied records
retain the provenance disposition `open/missing`. Their prior
independent-source comparison remains historical evidence rather than being
silently promoted into a new AI-review pass. Static validation passes where
recorded; all three AI review results, all ten completeness results, and build
and visual validation remain pending. Their audit result is therefore
`pending/unclassified` rather than either passing audit label. The other 46
units retain every default. Thus all 1,055 source units remain open and zero
are admitted as `full transcription`.

Controlling integrity and layout records:

- `spec/INHERITED-CORPUS-MANIFEST.md`
- `spec/FULL-COMPENDIUM-ARCHITECTURE.md`
- `spec/source-unit-inventory.csv`
- `tools/check_transcription_audit_coverage.py`

External coverage acquisition is tracked separately in
`spec/research/full-compendium-coverage-baseline.md`. Its current 68 source
records form an open attributed union of official or institutional handbook,
standard, and system taxonomies. They are not a proposed house taxonomy and
are not a completeness certification. Every recorded entry remains an owed
mapping/presentation until separately reconstructed and verified.

The external-coverage baseline and its generated sparse manifest currently
contain 9,162,150 open rows: 68 source records, 27,979 source-hierarchy
records, and 9,134,103 attributed topic records, carrying 23,765 unique official
or institutional HTTPS locators. Every
row remains `open/unmapped`; these counts establish inventory structure only,
not coverage completeness.

The same baseline and manifest records expose 5,511 exact non-HTTPS source
locators and 20,071 exact scheme-less source identifiers in separate fields.
They are source-evidence forms, not substitutes for HTTPS locators, and their
presence does not change any acquisition, mapping, or readiness status.

The separate acquisition-gap ledger contains six explicit open gaps and two
active provenance controls. Source-acquisition closure is therefore **OPEN**,
independently of the 9,162,150 acquired rows. Deleting or changing a supplementary
gap note without updating the hash-locked authority causes the control to fail.

The live presentation-record controls currently find no presentation-packet
files. Their corpus accounting therefore reports zero verified fulfillment of
the 9,162,150 external-coverage records and zero verified fulfillment of the 615
register obligations. The 1037 reviewed source-unit records establish bounded
identity, provenance, destination, independent-source evidence, and static
evidence only; none establishes terminal content admission. These structural
results leave content and restoration readiness **OPEN**; they do not establish
source fidelity, semantic correctness, completeness, or reviewer independence.

The generated register-obligation manifest and keyed closure ledger contain all 615 rows from the
four existing registers: 141 depth gaps, 185 new-content rows, 201 apparatus
rows, and 88 defect rows. It infers no completion. All 615 obligations carry
the neutral disposition `open`. Any legacy exclusion, pointer, sketch,
ceiling, retirement, stub, or old completion string remains preserved only in
the original record; the generator does not interpret it. The original
register row determines whether fulfillment requires a source presentation,
apparatus artifact, correction, or another owed object; the manifest does not
invent that standing.
These rows are not imported into the external coverage manifest. The closure
ledger can validate supplied keyed links to admitted handbook units or verified
presentation packets, destinations, and six separate AI/static/build/visual
evidence files. Its
governed input has no ordinary completion or contract-supersession record, so
all 615 obligations remain open: zero `COMPLETE` and zero
`SUPERSEDED_BY_CONTRACT`.

## Single-publication status

`spec/COMPENDIUM-VOLUME-MANIFEST.md` and its machine-readable manifest now
bind exactly one possible public artifact: `handbook/main.pdf`, titled *The
Methods of Reason*. The exact inherited source and 251-page PDF remain
hash-locked internal authority evidence and are explicitly excluded from the
publication. The current 836-page artifact remains a construction draft and is
not release-ready. Its settled build has zero undefined references, and the
ordinary strict plus terminal no-pending-reference checks both pass. No companion,
volume set, facsimile publication, or
provisional publication is authorized.

A release state additionally requires the all-zero-residual terminal readiness
record and the user's final-acceptance record, both hash-locked to the same
final PDF. Neither record exists yet, so publication readiness remains
**OPEN**.

The current deterministic terminal-readiness manifest is 7,919 bytes with
SHA-256
`fae10cd1b64c28da96b55e4c6d562813bba2dfd74e8a2a6099b45d91d2f6b819`.
It records 9,182,017 non-user residuals and no user-final-acceptance record.
That manifest is an exact construction checkpoint, not a release verdict.

## Current mechanical controls

`tools/check_full_compendium_controls.py` currently verifies, without changing
the authoritative source:

- the TeX and PDF hashes, sizes, line count, and page count;
- the immutable 214-file historical handbook source snapshot against which
  interval classes and locators were recorded;
- the separate current-construction snapshot and physical-line inventory,
  which are repinned only after the current tree is reviewed and stable;
- the 18,174-row semantic handbook-unit inventory and keyed reverse ledger,
  with zero `mapped/reviewed` rows;
- the historical 35,883-record reverse handbook source baseline, with every
  row still `open/unmapped`;
- the 1,055-unit source inventory;
- the 282-record inherited interval-audit baseline;
- the physical-restoration join, with 265 exactly accounted intervals and 17
  residual intervals;
- the zero-pending inherited-reference terminal source-order surface;
- the 1,055-row source-unit audit crosswalk, with 1037 reviewed-but-open records,
  18 untouched defaults, and zero `full transcription` admissions;
- the 9,162,150-row external coverage baseline and generated sparse manifest;
- the six-open-gap/two-control acquisition ledger;
- the 615-row register-obligation manifest;
- the 615-row register-obligation closure ledger, with zero `COMPLETE` and zero
  `SUPERSEDED_BY_CONTRACT` rows;
- presentation-packet record validation and whole-corpus structural accounting,
  presently with zero packet files and no fulfilled coverage or register
  assignments; and
- exact single coverage of every nonblank, noncomment inherited TeX line within
  the document bounds by the three whole-book audit ledgers.

A PASS from that command means only that these integrity and accounting
controls agree. It does not mean that altered or missing handbook content has
been restored.

No compilation, static check, visual inspection, or prior agent review can
override a missing or altered content unit.
