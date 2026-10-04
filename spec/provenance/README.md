# Input for changing inherited-unit crosswalk defaults

The generated crosswalk begins with every inherited unit `open/missing` and
every completeness or verification result `pending`. The JSON file in this
directory is reviewer-supplied input that the generator checks before
overriding any field. An accepted record may expose exact checked facts while
the unit remains open. This page introduces no new content term: “object,”
“record,” and the JSON field names below are ordinary administrative
descriptions.

## Exact governed reader placement

The `reader_layout` field occurs only in provenance records
`SRC-01649-01660`, `SRC-03022-03037`, `SRC-06049-06069`,
`SRC-07494-07505`, `SRC-09080-09098`, `SRC-10060-10088`, and
`SRC-11354-11413`, together with `SRC-12249-12261`, whose
`schema_version` is exactly `2`, `SRC-12970-12988`, also version `2`, and
the label-less layout record `SRC-14095-14146`, likewise version `2`;
the distinct `reader_appendix_layout` field occurs only in
`SRC-15093-15206`, `SRC-15207-15239`, `SRC-15240-15488`, and
`SRC-15489-15619`, together with the Appendix D.6 continuation
`SRC-15620-15637`, Appendix E record `SRC-15638-16742`, and Appendix F
record `SRC-16743-16801`, whose
`schema_version` is exactly `3`. All other inherited restoration records remain
version `1` and must not contain either field.

Necessity: the unchanged source intervals begin with
`\part{Classical Propositional Logic}` and
`\part{Classical First-Order Logic}`, while the constructed handbook already
has the fixed public `\part{Classical Logic}\label{part:p02}`.  The source
commands cannot be deleted or rewritten, and publishing them as additional
parts would violate the fixed fourteen-part surface.  Exact source line 6049
also supplies `\part{Model Theory}` from inherited printed Part IV; the final
fourteen-part surface requires that unchanged command to execute directly as
the sole public Part III, without a duplicate part command in the P3 driver.
Exact source line 7494 supplies `\part{Computability}` beneath fixed public
`\part{Computability and Complexity}\label{part:p04}`; its unchanged source
title therefore requires subordinate navigation treatment without a second
public Part IV.  Exact source line 9080 supplies
`\part{Formal Arithmetic and Incompleteness}` and the exact label
`part:incompleteness`; the fixed final public title is *Arithmetic and
Incompleteness*, so the exact command must advance once to Part V while the
governed layout supplies that public title without a driver alias.
Exact source line 10060 supplies the final direct `\part{Axiomatic Set Theory}`
and `part:set-theory`; it executes unchanged once as public Part VI with no
driver duplicate or alias.  Exact source line 11354 supplies
`\part{Proof Theory}` beneath the fixed public
`\part{Proof Theory, Lambda Calculi, and Higher-Order Logic}\label{part:p07}`;
its unchanged source title therefore receives subordinate navigation without
creating a second public Part VII.  Exact source line 12249 supplies
`\part{Second-Order and Higher-Order Logic}` and `part:higher-order`; the
binding architecture retains that source at the audited public Part II
higher-order destination, so it receives subordinate navigation without a
new public part or a Part-II label alias.
Exact source line 12970 supplies `\\part{Nonclassical Logic}` and the exact
label `part:nonclassical`; the fixed final public title is *Nonclassical
Logics*, so the command advances once to Part VIII while governed layout
supplies the plural public title without a driver alias.
Exact source line 14095 supplies the label-less
`\part{Formal Practice, Automation, and Verification}` beneath fixed public
`\part{Automation, Mechanization, and Formal Practice}\label{part:p12}`; it
therefore receives subordinate navigation without a second public Part XII or
an invented source label.

Definition: `reader_layout` is exactly the closed administrative object with
fields `source_part_line`, `source_part_command`, `source_label_line`,
`source_label`, `wrapper_path`, `public_part_file`, `public_part_title`,
`public_part_label`, `reader_heading_level`, `reader_heading_title`,
`reader_attribution`, `part_counter_effect`, `toc_level`, and
`bookmark_level`.  Their sole allowed values are the ten complete value sets
committed in `SRC-01649-01660.json`, `SRC-03022-03037.json`,
`SRC-06049-06069.json`, `SRC-07494-07505.json`, `SRC-09080-09098.json`,
`SRC-10060-10088.json`, `SRC-11354-11413.json`, and
`SRC-12249-12261.json`, `SRC-12970-12988.json`, and
`SRC-14095-14146.json`.  The first two sets identify source lines 1649/1650
with `part:classical-propositional` and source lines 3022/3023 with
`part:classical-first-order`; each exact wrapper; the Part II driver and public
title/label; an unnumbered `chapter*` carrying the unchanged source title; the
corresponding recorded source attribution; no part-counter effect; a chapter
TOC entry; and bookmark level 0.  The third identifies source lines 6049/6050
with `part:model-theory`, its exact wrapper and P3 driver, the direct public
part heading and source attribution, one part-counter increment to final Part
III, a part TOC entry, and bookmark level -1.  The fourth identifies source
lines 7494/7495 with `part:computability`, its exact wrapper and P4 driver, the
fixed public Part IV title/label, an unnumbered `chapter*` carrying the
unchanged source title, the recorded source attribution, no part-counter
effect, a chapter TOC entry, and bookmark level 0.
The fifth identifies source lines 9080/9081 with `part:incompleteness`, its
exact wrapper and P5 driver, the fixed public Part V title, one counter
increment to final Part V, a part TOC entry, and bookmark level -1.
The sixth identifies source lines 10060/10061 with `part:set-theory`, its exact
wrapper and P6 driver, the unchanged public Part VI title, one counter
increment to final Part VI, a part TOC entry, and bookmark level -1.
The seventh identifies source lines 11354/11355 with `part:proof-theory`, its
exact wrapper and P7 driver, the fixed public Part VII title/label, an
unnumbered `chapter*` carrying the unchanged source title, the recorded source
attribution, no part-counter effect, a chapter TOC entry, and bookmark level 0.
The eighth identifies source lines 12249/12250 with `part:higher-order`, its
exact wrapper and P2 driver, the fixed public Part II title/label, an
unnumbered `chapter*` carrying the unchanged source title, the recorded
printed-Part-IX-to-public-Part-II attribution, no part-counter effect, a
chapter TOC entry, and bookmark level 0.
The ninth identifies source lines 12970/12971 with `part:nonclassical`, its
exact wrapper and P8 driver, the fixed plural public Part VIII title, one
counter increment to final Part VIII, a part TOC entry, and bookmark level -1.
The tenth identifies source line 14095 with no source part label, its exact
wrapper and P12 driver, the fixed public Part XII title/label, an unnumbered
`chapter*` carrying the unchanged source title, no counter effect, a chapter
TOC entry, and bookmark level 0.  Its `source_label_line` is exactly 0 and its
`source_label` is exactly empty; any part label in that artifact fails closed.

Standing: this object is layout and build metadata.  It is not a motive,
relation, statement family, source-fidelity result, completeness result,
verification result, source-unit disposition, or publication-readiness claim.

Nonredundancy: the source locator and artifact digest prove which bytes were
restored, and `handbook_destination` records where the artifact is routed, but
neither states how each listed nested source part is displayed without
creating an additional public part, nor how the listed direct source part is
kept as the sole final Part III without a driver duplicate.  The added object
supplies only those missing instructions for the ten listed provenance IDs.
The Part V and Part VIII values additionally record their sole allowed
exact-source/public-title distinctions; no label alias is introduced.

Use: the restoration checker validates the exact field set and values, literal
source command and optional label, three-line wrapper, and public binding.  The TeX
scope uses only the six exact subordinate provenance identifiers and the
mapped Part V and Part VIII identifiers and rejects a missing, repeated, starred, or
wrong-title part call; the direct Part III and Part VI cases are not intercepted.  The
publication scanner classifies the six subordinate source headings, the two
direct public source parts, and the two governed public-title mappings and
rejects every extra or misrouted part.  None of these checks can change an
audit or review status.

Necessity: exact source line 15093 is `\appendix`. Executing the ordinary
book-class command without a governed boundary would convert the later public
Parts XIII and XIV into appendices, while deleting or rewriting the token would
break exact restoration. The part-only `reader_layout` object cannot describe
this different command or its local counter restoration without ambiguity.
The following source chapters have no second `\appendix` token but must
continue as Appendices B through F, so their continuation ordinals must also be
explicit. The following section must resume after D.5 as D.6 even though its
separate provenance scope restores public counters, so that section counter is
likewise explicit. The following source chapters must then resume as Appendices
E and F, so both ordinals must remain explicit after the D.6 scope boundary.

Definition: `reader_appendix_layout` is exactly the closed administrative
object with fields `source_appendix_line`, `source_appendix_command`,
`source_chapter_line`, `source_chapter_command`, `source_label_lines`,
`source_labels`, `wrapper_path`, `public_part_file`, `public_part_title`,
`public_part_label`, `appendix_ordinal`, `reader_heading_level`,
`reader_heading_title`, `chapter_counter_effect`, `toc_level`, and
`bookmark_level`. Its sole allowed value sets are committed in
`SRC-15093-15206.json`, `SRC-15207-15239.json`, `SRC-15240-15488.json`,
`SRC-15489-15619.json`, `SRC-15620-15637.json`,
`SRC-15638-16742.json`, and `SRC-16743-16801.json`: exact source Appendix A,
chapter *Registered Notation*,
and all four literal labels; continuation Appendix B, chapter *Binding and
Precedence*, and both literal labels; continuation Appendix C, chapter *Rule
Sheets*, and all five literal labels; continuation Appendix D, chapter
*Qualifying-Examination Problems and Selected Solutions*, and all twelve
literal labels; their exact wrappers and Part XII driver; local appendix
numbering; restoration of the prior public chapter counter; chapter TOC
entries; and bookmark level 0; followed by the exact Appendix D.6 section
continuation *Additional problems*, its one literal label, local section
counter, section TOC entry, and bookmark level 1. The Appendix B--F chapter
values and the D.6 value use appendix source line 0 and an empty
appendix-command value and
reject any repeated `\appendix` token. D.6 additionally uses chapter source
line 0 and an empty chapter-command value and rejects any chapter token. The
Appendix E value restores chapter *Exercise Feedback* and its two literal
labels, exact wrapper, local counter, chapter TOC entry, and bookmark level 0.
The Appendix F value restores chapter *Editorial and Formal-Logical Release
Checklist*, its two chapter labels and four section labels, exact wrapper,
local counter, chapter TOC entry, and bookmark level 0.

Standing: this object is layout and build metadata. It is not a mathematical
relation, statement family, source-fidelity result, admission result, review
result, or publication-readiness claim.

Nonredundancy: the source locator and artifact digest establish the unchanged
bytes, and `handbook_destination` records the routed file, but neither states
that Appendix A--F/D.6 numbering is local nor that the prior public chapter and
section counters resume afterward. `reader_layout` governs `\part`, not
`\appendix`, and therefore cannot supply this boundary.

Use: the restoration checker validates the closed field set, exact transition
or continuation, chapter, labels, wrapper, public binding, and order before the
editorial aggregator. The provenance-specific TeX scopes require one appendix
transition, render Appendices A--F and D.6 with unique anchors, restore the prior
counters after each, and do not leak their numbering. Route, publication, and
compile tests independently reject missing, repeated, reordered, or globally
renumbering variants.

`reviewed-source-unit-records.json` has exactly four top-level fields:
`schema_version` (currently `5`), `authority_path`, `authority_sha256`,
and `records`. Each object in `records` must have the exact field set
required by `reviewed-source-unit-records.schema.json`; unknown and missing
fields are rejected. The Python generator repeats these checks against the
live files, so schema validity alone cannot authorize a change.

## What must match exactly

Each supplied object repeats the existing unit ordinal, kind, title, source
label, source line range, and source digest. It also repeats the frozen
authority path, digest, and edition. The generator rejects duplicate or
unknown ordinals, booleans or non-integers in integer fields, stale unit data,
authority drift, and any authority other than the frozen Version 1.0 source.

Each supplied object also provides `restoration_record_path`,
`restoration_record_sha256`, and `restoration_provenance_id`. The path must
be a canonical inherited-restoration record path directly under
`spec/provenance/`; its file name and recorded identifier must agree, and
the live file must have the supplied digest. The generator runs the existing
inherited-restoration validator on that exact record. The record's
`source_unit_evidence` must list the unit ordinal, its source locator must
contain the unit's full source range, and the linked inventory row must repeat
the unit's kind, title, label, range, and digest exactly. The linked
restoration record's disposition must be `full transcription`.

The matching `handbook/restoration/scope-<provenance-id>.tex` file must
contain exactly its governed restoration-artifact input. Starting at
`handbook/main.tex`, the generator follows uncommented literal `\input`
commands recursively and requires the wrapper to be reached exactly once. A
missing reachable file, a cycle, no route to the wrapper, or more than one
route closes admission. A dynamic input expression does not establish the
required static route.

The accepted unit dispositions are `open/missing` and `full transcription`.
An omitted unit keeps every default. An `open/missing` record can identify
its authority, presentation, exact restoration provenance, destination,
labels, audit result, and the verification dimensions actually checked. Its
pending or failing fields remain visible and cannot close the row. A `full
transcription` record is accepted only when all ten completeness dimensions
and all five verification categories are `pass` and all five verification
categories have recorded evidence.

The exact comparison result is one scalar `audit_result`. An open record whose
comparison is not yet classified uses exactly `pending/unclassified`, with
empty `layout_changes` and `defect_exclusions` arrays. This value is forbidden
on a `full transcription` record. The passing results are
`full-and-accurate` and `layout-only relocation`; neither is accepted unless
all ten completeness and all five verification dimensions are `pass`, even
when the record's disposition remains `open/missing` for another stated
reason. `full-and-accurate` requires an empty `layout_changes` array, while
`layout-only relocation` requires at least one distinct value from the
contract's permitted list: `wrapper`, `placement`, `pagination`, `typography`,
`stable label`, or `added navigation heading`. For either passing result, the
`defect_exclusions` array must be exactly, in this order:

```json
[
  "altered",
  "abridged",
  "omitted",
  "hybridized",
  "unsupported addition"
]
```

These values record the review outcome; the generator does not infer textual
equivalence from the strings. Acceptance also requires the recorded evidence
described below.

## Destinations and active labels

A destination must exist and be hash-locked. Ordinarily it is a nested
`.tex` content file under one of these paths:

- `handbook/parts/pNN/`
- `handbook/annex/pNN/`
- `handbook/restoration/`
- `handbook/frontmatter.tex`

An open record may use `handbook/parts/pNN.tex` only when that exact part
driver is the linked restoration's integration destination. This exception
records the existing placement and does not turn a driver into substantive
content or allow a `full transcription` disposition. Other drivers,
generated files, registry files, and known lookup-only files cannot be
destinations. In particular, the generator rejects `handbook/generated/**`,
`handbook/registry/**`, `handbook/main.tex`, `handbook/annex/pNN.tex`,
`handbook/parts/p01/symbol-registry.tex`,
`handbook/parts/p14/master-tables.tex`, and
`handbook/parts/p14/rule-sheets.tex`.

An open record may use an empty `stable_labels` array when the exact restored
unit has no dedicated active label. A `full transcription` record requires at
least one stable label. Every supplied label must use the handbook taxonomy.
Each declared label must occur exactly once in the exact destination. The
counter recognizes active `\label{...}` commands and the first label
argument of the typed handbook environments. Commented and escaped examples
do not count, and a label cannot be claimed by two supplied units.

## Separately recorded variants

`variant_links` is required even when empty. Each nonempty link repeats
another inventory unit's exact identity and adds a nonempty relationship
description. The generator rejects self-links, duplicates, unknown or stale
targets. The linked unit must also occur in the same cumulative JSON input,
must link back, and must have a different presentation-identity string.

## Recorded evidence

`verification` has exactly six categories: `source_fidelity_ai`,
`topic_specialist_ai`, `adversarial_publication_ai`, `static`, `build`, and
`visual`. `verification_evidence` contains at
most one object for each category. Every non-pending result requires one
evidence object; a pending result may omit it.

Each supplied artifact must be an existing repository file with the supplied
digest, and supplied artifacts must be different files. The authority,
destination, and JSON input cannot serve as their own evidence. On an open
record only, the exact linked restoration record may support the `static`
result because the generator independently validates that record, its
artifact, its wrapper, its source-unit membership, and its single reachable
route. It cannot support another category or a closed record. Producer
identities must be nonempty and pairwise distinct after Unicode compatibility
normalization, case folding, and whitespace folding; scopes must be nonempty.
Each passing AI review additionally records its model and version, complete
instructions, the exact review scope, every consulted authority file and
locator with a digest, nonempty findings, and that the other two review outputs
were not consulted. A pre-migration evidence pointer may remain attached to a
pending AI field without those new fields; it cannot establish a pass.

This is mechanically honest recorded-evidence validation. It proves only the
supplied path identities, file contents, category keys, results, and recorded
scope. It does not authenticate a person, derive mathematical correctness,
prove content completeness, authenticate a model identity, or let one AI,
static, build, or visual result substitute for another.

## Current projection and limitations

The generated crosswalk projects the exact restoration identifier, record path
and digest, authority edition, presentation identity, disposition, destination,
stable labels, audit result, ten completeness results, and six verification
results. `layout_changes`, `defect_exclusions`, variant links, and evidence
metadata remain in the hash-checked JSON input rather than becoming repeated
CSV columns.

The canonical reviewed-source input is now the deterministic merge of the
documents under `spec/provenance/reviewed-source-unit-shards/`. The initial
shard preserves ordinals 1--13 and 619; the first source-order pilot shard
preserves ordinals 14--52, and the later source-order shards continue without
a gap through ordinal 1055; the Part V shard omits already governed ordinal 619
so that it is merged exactly once. `tools/merge_reviewed_record_shards.py` rejects
different authority pins, duplicate or unknown ordinals, stale hashes, and an
output whose byte order differs from the canonical ordinal order.

The generator proves the required single static route to the governed wrapper;
it does not interpret TeX conditionals or dynamic input expressions, compare
rendered pages to the frozen source, validate the internal format of arbitrary
evidence files, or link inherited units to external presentation-packet
variants.

The committed v5 input contains all 1055 open records: source-unit ordinals 1--1055,
with the preserved out-of-order ordinal 619 counted exactly once. The unitless
restored intervals `SRC-00171-00197`, `SRC-11012-11052`, and
`SRC-11240-11279`, `SRC-11520-11598`, `SRC-13255-13284`, and
`SRC-13410-13439`, `SRC-13862-13896`, `SRC-13897-13918`,
`SRC-14035-14051`, `SEP-14561-14561`, `SEP-14590-14590`,
`SEP-15092-15092`, `SEP-16802-16802`, `SRC-16803-17196`,
`SEP-17197-17197`, `SRC-17198-17204`, `SEP-17205-17205`, and
`CTL-17206-17206` have empty
`source_unit_evidence.unit_ordinals` arrays.
They therefore have no source-unit crosswalk rows; inventing rows would
contradict the source-unit inventory. Their exact provenance, artifacts,
wrappers, destinations, and evidence remain governed by their restoration
records and the restoration checks.

All 1055 supplied unit records retain `open/missing` and
`pending/unclassified`. Their three AI review results remain `pending`; the
older independent-source comparison is retained only as a pending historical
evidence pointer and is not promoted. Static validation is `pass`; all ten
completeness results and build and visual validation are `pending`. Their empty
defect-exclusion arrays make no passing audit claim.
No source-unit defaults remain. Thus all 1,055 source units remain open and
zero are admitted as `full transcription`.

The 64-row `inherited-bibliography-field-ledger.csv` maps the exact manual
bibliography blocks in `SRC-16803-17196` to the first 64 entries in the unified
BibLaTeX database. It pins both sides and statically checks key order, locators,
years, and substantive lexical facts. Its semantic field-review column remains
pending until independent review; the ledger is not itself an admission claim.

## Version 4: candidate corrected reader intervals (P4a)

Version 4 is an explicit **construction-stage** alternative for plain
reader-facing SRC intervals. It does not admit content. Versions 1--3 retain
their original line-count and exact-token invariants. The governed part/appendix
layout IDs and PRE/CTL/SEP controls cannot use version 4 in this stage.

A version-4 record has every existing root field plus exactly one
reader_correction object, and disposition is full reconstruction.
The original authority, source_locator and source_unit_evidence still identify
the immutable frozen source. The restoration_artifact identifies the actual
corrected reader file, whose line count may differ. Its destination file must
be that same artifact; the destination remains open/missing.

The closed reader_correction fields are:

- kind: exactly candidate corrected reader interval.
- correction_id: a stable nonempty administrative ID.
- policy_authority: path, sha256, locator. The path is
  spec/EDITION-2026-CONTRACT.md, the locator is Reader-facing content and
  corrections, the current file hash must match, and the specified direct-
  correction authorization must be present.
- rationale: path, sha256, locator of a separate explanatory artifact under
  spec/. It is evidence custody, not an independent acceptance verdict.
- predecessor_record: path and sha256 of the archived previous record.
  Predecessor chains are checked for matching source/interval/artifact identities,
  stale hashes and cycles, ending at a plain version-1 record. Historical records
  are not revalidated against the now changed live artifact or treated as
  accepted reviews.
- affected_ids: sorted unique IDs including this exact SRC provenance ID.
  Further IDs must be matching source-unit:<ordinal> identifiers already bound
  by source_unit_evidence, or known IDs in the four present original registers.
- source_content_token_sha256: the canonical frozen interval hash, distinct
  from the current artifact's canonical hash.
- edits: a nonempty ordered array described below.

Each edit has exactly source_range, reader_range, source_sha256,
reader_sha256 and reason. Both ranges are zero-based, half-open **line offsets**:
source offsets are relative to the frozen interval, reader offsets to the
complete current artifact. Thus [2,4] denotes the third and fourth lines.
An insertion uses [k,k] on the source side; a deletion uses [j,j] on the
reader side. Adjacent ranges are allowed; overlapping or out-of-order ranges
are rejected. Both sides empty, or equal normalized old/new slices, are no-ops
and are rejected.

Slice hashes normalize each terminal CRLF, LF or CR to one LF, preserving every
other byte. A nonempty slice must have a terminal line ending on every line.
An empty slice is empty bytes, with the ordinary SHA256 of empty bytes.
Every unchanged prefix/gap/tail must match exactly under this same normalization.
The complete edit map plus those unchanged spans accounts for every source and
reader line; unexplained changes are rejected even if the whole-file hash was
refreshed. The corrected artifact also needs matching raw byte count, line count,
raw SHA256, canonical SHA256, valid UTF-8 and no added BOM.

Use check_inherited_restoration.CORRECTED_CONTENT_COMPARISON verbatim for
restoration_artifact.content_token_comparison. The two verification-evidence
scope strings must be the exact CORRECTION_VERIFICATION_SCOPES values. They
state what the mechanical source/static checks establish, not exact unchanged
transcription or source-text acceptance.

All existing completeness values remain pending. Only the existing mechanical
source/static results may be pass; independent_source, build, visual and the
legacy human_review field remain pending. No model/model-version fields are
invented or accepted in this candidate shape. Later independent records must
supply their own actual metadata and six-gate evidence.

### Source syntax and line provenance

After validate_record succeeds, reader_source_line_map(record) projects
1-based reader lines to absolute original source lines. Inserted/replaced hunk
lines map to None. Only unchanged spans receive original locations.
The helper assumes a validated record and grants no admission itself.

check.py records this distinction when authorizing the existing one-input
scope wrapper. The corrected candidate may use retained source syntax, while
duplicate/wrong/unreachable wrappers still fail. Only references on mapped
original lines retain the original future-source-reference exception. References
on correction lines must resolve normally; identical tokens on a changed line
do not acquire that exception merely by resembling an original reference.

audit_tables.py validates source records before recovering locators; it no
longer derives source positions from filename offsets alone. New correction
text uses its current title and has no invented original source line. Proof
targets in a corrected container are described as reader proofs/status, not
claimed as unchanged source proofs. Reader anchor counters follow actual
validated reader-environment order. Concurrent drift between record validation
and parsing is rejected.

collect() can inspect candidate projections for internal construction work.
P4a blocked active output/check acceptance whenever the default audit-table
command encountered a corrected candidate. P4b now supplies the validated
admission join described below. Candidate-only records still block active
output; no generated files or real provenance records were migrated in P4a
or P4b.

### Remaining formal integration

The P4b mechanism below supplies the separately reviewed corrected
disposition/result and active audit-table admission join. Real SRC records
must be migrated in a separate controlled task with frozen predecessor records,
complete correction maps, truthful pending standing and exact scoped reviews.

## P4b: corrected-reader source-unit admission

The existing reviewed-source-unit schema version remains 5. Its supported
terminal pairs are `full transcription` with either `full-and-accurate` or
`layout-only relocation`, and the closed corrected pair `full reconstruction`
with `corrected-and-verified`. The corrected pair requires a live, validated
version-4 restoration record; a generic reconstruction string does not grant
admission. The version-4 construction record keeps its pending fields.

For a corrected unit, the existing `presentation_identity_value` must be
`<provenance_id>:<correction_id>:unit-<unit_ordinal>`. The existing restoration
record path/hash binds the complete policy, rationale, predecessor and edit
map. The frozen unit ordinal, kind, title, source label, source range and
source digest are checked against the inventory as before. The reviewed
destination path and raw hash must equal the corrected artifact in that exact
version-4 record. The governed wrapper and corrected artifact each occur
exactly once in the reachable handbook input graph. Existing label ownership,
active-label, variant, path and evidence-file checks remain in force.

The corrected result requires this exact ordered `defect_exclusions` list:
`unexplained alteration`, `abridged`, `omitted`, `hybridized`,
`unsupported addition`. Authorized changes are the exact policy-backed,
replayed edit map. The corrected result therefore excludes unexplained changes
without claiming that the reader text contains no alterations at all. Legacy
exact results retain their original list beginning with `altered`.

All ten completeness dimensions and all six verification dimensions must
pass. Each verification category has its own hash-bound evidence file and
distinct recorded producer identity. The three AI categories still require
the actual model, actual model version, exact instructions, consulted
authorities and locators/hashes, findings, and a false declaration for
`other_review_outputs_consulted`. Unavailable model versions remain an open
recording obligation; placeholder text or inferred aliases do not constitute
the required actual metadata.

Every evidence item on a version-4 reviewed record additionally contains one
closed `correction_snapshot` object, with these seven fields copied exactly
from the reviewed record: `unit_ordinal`, `source_sha256`,
`restoration_provenance_id`, `restoration_record_sha256`,
`presentation_identity_value`, `handbook_destination`, and
`handbook_destination_sha256`. This binds the recorded scope of each gate to
the exact corrected unit and artifact. The ordinary evidence hash, producer,
scope and independence checks remain mandatory. Legacy evidence shapes stay
unchanged. Pending corrected records may expose checked identities while their
completeness and verification values remain pending; they grant no terminal
disposition. The schema's evidence array now permits six items, correcting the
earlier maximum of five that contradicted the six-gate requirement.

The terminal checker discovers validated live version-4 provenance first and
binds its actual source-unit ordinals independently of CSV disposition,
restoration-ID or destination claims. Each such ordinal must occur exactly
once in the CSV. Those rows, and any additional explicit corrected claims,
must reproduce the live reviewed-record join. A terminal joined row must use
its owning version-4 provenance. Honest reviewed or unreviewed pending rows
retain their canonical OPEN state. The normal terminal command also retains
its mandatory upstream crosswalk freshness check. The audit command uses the
same join and requires admission for every source unit bound by each corrected
reader, plus coverage of every emitted label by those admitted units. It also
compares the collected reader hash with the admitted artifact. A partial or
missing admission, stale evidence, unadmitted emitted label, or candidate-only
record blocks generation and freshness acceptance. No force option exists.

`validated_reviewed_rows` validates frozen inventory identities and applies
the existing reviewed-record join. It does not write a crosswalk or replace
the crosswalk builder's complete interval-coverage checks. Corrected readers
without source-unit ordinals have no supported admission through this join.
System-card withholding, symbol-view admission, packet admission, final builds,
visual review and final user acceptance keep their existing separate gates.

See `spec/research/edition-2026-p4b-corrected-admission.md` for the bounded
implementation evidence and remaining integration work.
