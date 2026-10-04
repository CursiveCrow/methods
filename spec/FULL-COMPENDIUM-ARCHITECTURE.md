# Full-compendium architecture

> **Current governing amendment, 2026-09-07:**
> `EDITION-2026-CONTRACT.md` supersedes the fixed fourteen-part order and
> conflicting restrictions on reference entries, dated coverage and active
> mathematical correction. Its stable nineteen-part identities and reviewed
> catalog transition govern implementation. Earlier records remain historical
> evidence; outstanding implementation and admission work remains open.

**Binding layout architecture, 2026-08-12.** This document implements
`FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`. It governs containers,
provenance, navigation, and verification only. It does not authorize any
editorial alteration of logical content.

## 1. Immutable inherited corpus

The byte-exact artifact `source/formal-logic-reference.tex`, including its
preamble, comments, blank lines, control syntax, front matter, body, and back
matter, is preserved as the inherited authority. Its 17,206 physical lines
remain in their original order and are accounted for by the whole-file digest
and physical-line records. This artifact-preservation requirement does not
mean that TeX control syntax, comments, or blank lines are themselves printed
as compendium prose.

The reader-facing content floor is every content-bearing passage and rendered
element supplied by that preserved authority. Every named and unnamed passage,
formula, rule, proof boundary, example, qualification, table, and attribution
must appear in the final compendium in full. Reordering reader-facing content
for physical layout is permitted only through a lossless source map that gives,
for every source interval, its exact handbook destination or records that the
interval is nonprinting artifact material. Navigation records, registry cards,
calculus sheets, tables, figures, and cross-references may accompany the content
only as source-traceable lookup and layout surfaces. They may not rephrase,
condense, supplement, or replace any part of a presentation.

Until an integrated TeX transcription has passed interval-level comparison,
the frozen source PDF is the controlling render of the inherited corpus. A
temporary facsimile inclusion may be used as a fidelity floor during
construction; it is not evidence that a separately rewritten handbook section
is accurate.

### 1.1 One public book

The public deliverable is exactly one PDF, `handbook/main.pdf`, titled *The
Methods of Reason*. There is no companion book, core volume, expansion volume,
volume set, facsimile publication, or provisional public edition. The frozen
source and 251-page PDF remain immutable internal authority evidence and are
not distributed as part of the public book. The historical records that once
described another publication arrangement remain historical evidence only.

The one public PDF remains a construction draft until the terminal readiness
record has zero residuals, the final source and PDF hashes agree across all
build and visual evidence, and the user supplies the sole final editorial
acceptance. There is no page-count ceiling and no compression target.

Directly inputting the current source body into the handbook is not permitted:
the two TeX systems presently assign different definitions and standing to
shared commands and environments. Examples include source
`\defeq` as `:=` versus the live handbook's `:\equiv`, source paired-delimiter
forms of `\abs` and `\sem` versus live one-argument commands, and incompatible
proof-environment policies. Open: construct an integrated TeX artifact that
retains every source line unchanged while preventing the documented command
and environment conflicts from changing the rendered content. Supply complete
physical-line accounting, source-to-destination records, content comparison,
clean-build evidence, and page inspection for that artifact. The means of
satisfying this obligation is not assumed or named here, and manual editing of
source content tokens cannot serve as preservation evidence.

## 2. Presentation packets for additions

The administrative term **presentation packet** is needed because a generic
unit provenance record does not by itself bind all parts of one external
source presentation while keeping that presentation separate from neighboring
variants. It means exactly one record conforming to
`spec/presentation-packet.schema.json` that links one identified source
presentation to its complete maintained content artifacts, obligation IDs,
destination, completeness dimensions, and independent verification evidence.
It is a metalinguistic administrative artifact, not a logic, calculus,
theorem, interpretation, or content substitute. It differs from the source
presentation itself because it contains only content/evidence references and
control metadata; it differs from the generic provenance record by enforcing
presentation-level separation and the complete external-content categories.
Later content admission and generated reference surfaces require this exact
record, so the distinction is used rather than merely named.

Each external presentation is stored and verified through its own presentation
packet. A packet records:

- the identified work, edition, and exact locator;
- the presentation's own subject and system name;
- its notation and the typed role of every symbol used;
- its definitions, axioms, rules, semantic clauses, and side conditions;
- every hypothesis and the exact scope of every claim;
- the supplied proof, proof sketch, cited boundary, counterexample, example,
  exercise, warning, and qualification;
- the packet's handbook destination and stable labels; and
- a source-to-handbook completeness check.

One source presentation never silently supplies missing clauses for another.
When two sources differ, their packets remain separate. A comparison table may
link the packets after both have been presented in full, but a table cell is
not their content.

For copyrighted external works, "full" means a complete, independently
worded reconstruction of the mathematical presentation and every material
qualification needed to recover it without supplementation. It does not mean
copying protected expository prose. Verbatim quotation remains limited and is
used only where legally permitted and technically necessary.

## 3. Coverage manifests, not a house taxonomy

The administrative name **external coverage manifest** is necessary because
acquired source headings cannot be recorded as completed presentation packets
or as register obligations without falsely changing their standing.
The external coverage manifest is the open union of separately attributed
records copied from the displayed taxonomies of authoritative logic handbooks,
reference series, standards, primary works, and official system documentation.
Entries retain the work's own displayed title, hierarchy, and locator. This
manifest is an acquisition ledger, not a logic, subject classification, content
presentation, or completion verdict. It differs from a presentation packet
because it records acquired headings rather than reconstructed content and
evidence; it differs from the register ledger because its rows come from
identified external-source displays rather than inherited register records.
It is used to retain attributed acquisition order and to expose which acquired
records still lack separately verified presentation packets.

The compendium does not rank sources, select a canonical taxonomy, or collapse
overlapping headings into a newly invented classification. Subject indexes and
cross-reference tables may expose overlaps as navigation. An uncovered
authoritative entry remains an open obligation for a presentation packet rather
than being silently excluded.

The four existing registers remain a separate, lossless ledger of neutral open
obligations. They are not imported into the external coverage manifest, and
neither ledger is exhaustive or permission to omit unrecorded content. A future
keyed mapping from each register obligation to its identified authority,
presentation packet or physical apparatus artifact, handbook destination, and
verification evidence remains owed; no standing or fulfillment is inferred
from a register marker alone.

## 4. Physical book contents

The physical book contains:

1. the complete inherited source content and every completed external
   presentation;
2. contents lists, source lists, subject indexes, notation indexes, theorem
   indexes, dependency links, and separately attributed comparison tables;
3. rule sheets, system cards, symbol tables, bibliographic records, and status
   tables generated only from completed presentation packets, as lookup views
   rather than substitutes for content; and
4. source maps, digests, completeness records, and verification reports.

The final physical organization is fixed as follows:

1. Foundations of Formal Work
2. Classical Logic
3. Model Theory
4. Computability and Complexity
5. Arithmetic and Incompleteness
6. Axiomatic Set Theory
7. Proof Theory, Lambda Calculi, and Higher-Order Logic
8. Nonclassical Logics
9. Logic in Computer Science
10. Algebraic and Categorical Logic
11. Philosophy of Logic
12. Automation, Mechanization, and Formal Practice
13. Chronology and Biography
14. Apparatus

The rendered book contains these fourteen part headings exactly once each and
in this order. A source-exact inherited `\part` reached through its validated
wrapper is the part heading; a driver must not add a duplicate heading merely
to retain a convenient local file shape.

This organization is a physical navigation aid only. It cannot truncate a
presentation or determine what belongs to logic. Inherited material may move
within it only through an explicit `layout-only relocation` record; the
content and internal order of the mapped source unit remain unchanged. A
presentation packet may be linked from multiple parts without its presentation
being duplicated or rewritten into different house forms.

## 5. Unit identity and source map

The administrative name **source map** is necessary because a whole-file digest
cannot identify the destination and evidence for each inherited interval or
external presentation. It means the complete set of records having the fields
listed below, with one stable provenance identifier for every inherited source
interval and every external presentation packet. It is a metalinguistic
provenance artifact, not a logic, presentation, equivalence claim, or content
substitute. It differs from the source-unit audit crosswalk because that
crosswalk presently joins inherited named units only to historical interval
evidence, while the source map must eventually supply destination,
presentation, content-digest, completeness, and verification values. Release
gates use the source map to account for every source-to-handbook destination
without treating topic resemblance as fulfillment.

The source map records:

| Field | Required value |
|---|---|
| Provenance ID | Stable, source-specific identifier |
| Authority | Exact source and edition |
| Source locator | Exact lines, pages, sections, theorem/rule numbers, or official version |
| Artifact-line standing | Reader-facing content, or exact identification of nonprinting control syntax, comment, or blank material |
| Presentation identity | The source's own named or otherwise eliminably described presentation |
| Handbook destination | File and stable label for reader-facing content; empty with an exact reason for nonprinting artifact material |
| Disposition | Full transcription, full reconstruction, or open/missing |
| Content digest | Digest of the inherited interval or maintained reconstruction artifact |
| Completeness dimensions | Notation; definitions; rules; side conditions; hypotheses; statements; proofs; examples; qualifications; attribution |
| Verification | Independent source-fidelity AI, topic-specialist AI, adversarial-publication AI, static, build, and visual results |

A destination cannot close more than one materially different presentation.
An inherited interval cannot be marked present merely because a destination
mentions the same topic.

## 6. Restoration order

Restoration is mechanical and source-driven:

1. inventory every physical inherited interval, distinguishing reader-facing
   content from nonprinting control syntax, comments, and blank material;
2. map each reader-facing interval to its current handbook destination, if any,
   and record the exact standing of each nonprinting interval;
3. classify each claimed reader-facing representation under the transcription
   contract;
4. restore missing or altered inherited material without rewriting it into
   house notation;
5. verify the restored interval against the frozen source;
6. construct external presentation packets from their identified authorities;
7. generate lookup surfaces only from verified packets; and
8. build and inspect the complete book.

No content-writing stage begins from an outline label alone. If an authoritative
presentation has not yet been gathered, the manifest records an open packet and
its source obligation; it does not name or define a hypothetical replacement.

## 7. Independent release gates

Release requires separate recorded results for:

- inherited-corpus completeness;
- external-presentation completeness;
- source-fidelity AI review of each topic and section;
- topic-specialist AI review of each topic and section;
- adversarial-publication AI review of each topic and section;
- static registry and cross-reference checks;
- clean compilation;
- page-by-page rendered inspection; and
- one book-level user final acceptance after every other residual is zero.

A pass in one category cannot compensate for a failure or pending result in
another. The current handbook remains non-releasable until all categories pass
against the full-compendium contract.

### 7.1 Historical and current tree records

The administrative name **handbook construction snapshot** is necessary
because the immutable snapshot used by prior audits cannot, without ambiguity,
also assert equality with a handbook tree that is being restored. It means
exactly the canonical, lexically ordered CSV record of every current regular
file below `handbook/` except the finite full-path list of build transients,
with repository-relative path, byte count, and SHA-256 digest for each file;
the snapshot's own bytes are pinned by the current-tree checker. It is a
metalinguistic verification record, not a logical presentation, source
authority, content review, completeness verdict, or release artifact. It
differs from `spec/handbook-audit-snapshot.csv` because that older file remains
the byte-anchored record of the tree against which the historical audits were
performed and is never required to equal the live tree, while the handbook
construction snapshot must equal the live non-transient tree exactly. The
full-compendium controls require the current record both before and after the
independent checks, and require its generated file/physical-line inventory,
so a control run cannot silently substitute historical audit identity for
current construction identity or overlook tree drift during the run.

The historical snapshot and its historical inventory have no update mode.
Their checkers verify the anchored record bytes and internal schemas without
reading changed live files as though they were the historical files. Candidate
current records may be written only to explicit, non-existing paths for review;
pinning the governed current files is a separate reviewed edit. The generated
current inventory leaves every row `open/unmapped` and proves only file and
physical-line accounting. Neither snapshot nor either inventory establishes
source fidelity, mathematical correctness, rendered-page quality, AI review,
user acceptance, completeness, or release readiness.
