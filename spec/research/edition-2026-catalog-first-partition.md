# CAT-01: a first partition of explicit acquisition-file descriptors

Date: 7 September 2026. Bounded research proposal for the lead's catalog
reconciliation decision. No catalog, assignment, ledger, index or manuscript
record is changed or admitted by this note.

## Recommended first batch

Use the **409 file-inventory descriptors under `SRC-068-H278`** as the first
bounded candidate batch for a metadata disposition. Their historical stable
IDs are `SRC-068-T11120` through `SRC-068-T11528`, and their scratch ordinals
are exactly 0001 through 0409. They are generated records of a local path,
byte count, physical-line count and SHA-256. The descriptor row is acquisition
metadata; the referenced file and any source content it contains retain their
own evidence and substantive obligations.

This recommendation is established by the producer and the actual complete
409-row block, rather than by a sample of titles. All 409 displayed strings
were compared in order between the acquisition note, a bounded suffix of the
baseline and a bounded suffix of the catalog; they match exactly. Every row
also passed the structural and full-string format inspection specified below.
The lead still owns the disposition policy, its representation in the existing
mechanisms, and the full-catalog membership check before recording a batch as
reconciled.

The next related candidates are the other 743 scratch descriptors in SRC-061,
SRC-064 and SRC-066. Their producer sites and existing profile counts are
identified below, but their full manifest membership was not verified in this
block. No entire source group, title collection, abstract collection or
substantive chapter is classified as metadata here.

## Authority and existing counts

The edition contract requires all 9,162,150 historical records to receive
traceable dispositions while retaining source/version distinctions
(`spec/EDITION-2026-CONTRACT.md:31–42`). CAT-01 expressly permits deterministic
batches for known metadata structures when their predicates and membership are
preserved (`spec/EDITION-2026-WORK-PACKAGES.md:84–101`). Its unit definition
requires an actual intellectual treatment and explicit component mappings
(`64–82`). This batch types existing evidence records; it supplies no completed
writing and discards no requirement.

The existing profile and assignment index identify the historical catalog as:

- Path: `spec/full-compendium-coverage-manifest.csv`.
- SHA256: `69d0f7ccb89e9be070366102f958a4034f632088b269a92ee244bfa5b41d55e8`.
- Bytes: 6,947,214,502.
- Data records: 9,162,150 across 68 sources.

The hash and full record counts above are reused from the completed profile
and assignment index, as requested. This block checked the current byte size
and selected suffixes; it did not recompute the multi-gigabyte catalog hash or
repeat its complete scan. The assignment index's first six fields pin the
path, fingerprint, size and count (`spec/external-coverage-assignment-index.json:1–6`).

The profile JSON uses a split reporting category: its `topic` count is
9,132,951 and `topic_with_scratch_inventory_marker` is 1,152. These sum to
9,134,103 actual `record_type=topic` rows. The scratch category is not a fourth
raw catalog record type. Adding 68 source and 27,979 hierarchy rows gives
9,162,150. The same distinction applies to SRC-068: 11,119 other topic rows
plus 409 scratch descriptors gives 11,528 raw topic rows. Do not subtract the
scratch count a second time or treat the 11,119 remaining rows as all substantive.
Evidence: profile JSON `1–11`, source objects `1213–1394`; profile Markdown
`6–32`; producer constants `tools/build_coverage_manifest.py:36–44`.

## Actual schema and producer

`tools/build_coverage_manifest.py` is the catalog producer. Its input is
`spec/research/full-compendium-coverage-baseline.md` and its output is the
historical CSV (`29–34`). Its module contract expressly preserves source order,
displayed titles, hierarchy, repetitions, metadata and locators while assigning
administrative IDs; it performs no subject classification (`1–8`). Therefore
the producer's generic word `topic` is not evidence that a row is an intellectual
treatment.

The CSV schema is `FIELDNAMES` at `79–94`:

`stable_id, record_type, source_id, source_title, source_metadata,
retrieved_granularity, hierarchy_path, parent_stable_id, displayed_title,
source_https_urls, source_non_https_urls, source_scheme_less_identifiers,
retrieval_date, mapping_status`.

There are three generated record types:

| Type | Construction evidence | Consequence for reconciliation |
| --- | --- | --- |
| `source` | `source_manifest_record`, lines 850–865, constructs a self-keyed descriptor from source title, metadata, granularity, locators and date, with no parent and a one-title path. It is emitted before content parsing at 931–956. | The 68 source rows are separately identifiable source descriptors, suitable for preserving as identity nodes. This does not classify their descendants or merge editions. |
| `hierarchy` | Lines 967–1005 turn a level 4–6 heading into an administrative H identifier and a parent/path entry. | A heading may name a subject, a manifestation, an inventory or other structure. Its text must retain its role; this note selects no hierarchy row. |
| `topic` | Lines 1007–1035 turn every remaining nonempty `- ` bullet into a sequential T identifier and preserve its complete displayed string. | A mechanically generated file inventory bullet becomes `topic` just as a chapter-title bullet does. Record type alone cannot establish substance. |

Source metadata and locator lists are stored once on the source row. Empty
child cells mean resolve through `source_id`, whereas a source row's literal
JSON `[]` is an empty list (`96–111`, `147–172`). The validation function at
`714–769` protects that distinction. A new disposition must retain the source
join and the original ordered locators, including HTTP and scheme-less forms;
an empty child field does not mean absent source evidence.

## Why the selected 409 rows are file-descriptor metadata

The immediate producer is
`tmp/acquisition/src068/build_acquisition_note.py`:

- `16–24` fixes the acquisition directory, note, retained baseline and evidence inputs.
- `218–225`, `scratch_inventory()`, enumerates files in that directory and obtains
  their relative path, byte length, physical-line count and byte hash.
- `247–259`, `Ledger.heading/topic`, emits the heading and the administrative
  `[TOPIC-######] ... — **OPEN**` wrapper.
- `356–360` emits the exact heading `SRC-068 deterministic scratch inventory`
  followed by `[SCRATCH-####] path | bytes=... | physical_lines=... | sha256=...`.
- `421–443` places that ledger in the patch-ready note and checks its topic
  numbering. No body-content interpretation occurs in the inventory loop.

The actual note has that heading at
`spec/research/acquisition-src-068.md:12022`, followed by the first descriptor
at `12024`. The same heading and all 409 descriptor strings occur in the
current baseline suffix. The catalog maps the heading to `SRC-068-H278`, with
parent `SRC-068`; its children are the exact 409 records identified above.

For this bounded inspection, the final 1,048,576 catalog bytes were read,
discarding the first incomplete physical line and parsing the remaining 1,638
complete records using the actual CSV header. The entire H278 block and EOF
occur within that suffix. The final 262,144 baseline bytes likewise contain
the entire inventory block. These small suffix reads were repeated for direct
comparison; no whole-catalog or whole-baseline scan was run.

Observed results:

| Check | Result |
| --- | --- |
| Catalog rows whose parent is `SRC-068-H278` in the inspected complete block | 409 |
| First/last stable ID | `SRC-068-T11120` / `SRC-068-T11528` |
| First/last scratch marker and sequence | 0001 / 0409, every integer once in order |
| Full-string grammar or structural failures in those 409 rows | 0 |
| Acquisition-note inventory strings | 409 |
| Baseline-suffix inventory strings | 409 |
| Catalog-suffix inventory strings | 409 |
| Ordered note/baseline equality; ordered note/catalog equality | Both true |
| Last complete catalog record at EOF | `SRC-068-T11528` |

These observations establish the actual bounded block. The later full-set
check must also exclude unexpected same-ID/parent occurrences elsewhere in the
entire catalog before a total reconciliation records this batch as complete.

## Reproducible selection predicate

Bind this predicate to the identified catalog fingerprint. Parse CSV fields
and JSON rather than splitting on commas. A row belongs to the proposed
batch exactly when all the following hold:

1. `record_type == "topic"`, `source_id == "SRC-068"`, and
   `parent_stable_id == "SRC-068-H278"`.
2. `hierarchy_path` decodes to exactly
   `[source_title, "SRC-068 deterministic scratch inventory", displayed_title]`.
3. `displayed_title` fully matches the following expression, with ASCII digits:

```regex
^\[TOPIC-(?<topic>[0-9]{6})\] \[SCRATCH-(?<scratch>[0-9]{4})\] (?<path>tmp/acquisition/src068/[^\r\n|]+) \| bytes=(?<bytes>0|[1-9][0-9]*) \| physical_lines=(?<lines>0|[1-9][0-9]*) \| sha256=(?<sha>[0-9a-f]{64}) — \*\*OPEN\*\*$
```

4. `stable_id` is `SRC-068-T` followed by the decimal integer captured as
   `topic`; the captured ordinal is in 11120–11528 and `scratch = topic - 11119`.
5. The source title agrees with the source descriptor reached by `source_id`;
   the parent resolves uniquely to the hierarchy descriptor with that exact
   title and source. The original retrieval date, `mapping_status`, ordered
   source locators and full displayed string are preserved in the disposition
   evidence. The predicate confers no acceptance from the word `OPEN`.

The regex is stated in .NET named-group syntax, matching the PowerShell
inspection used here. A Python implementation uses `(?P<name>...)` for the
same captures and `re.fullmatch`. The path is retained as a data string; the
predicate neither opens nor executes it. A record with an unexpected path
shape or conflicting field remains unresolved rather than being repaired
silently.

Steps 1–4 were checked for every row in the bounded block. The observed H278
record establishes its local title and source parent; whole-catalog source
resolution and global uniqueness are part of the later full-set check.

### Examples and exclusions

| Record or case | Result and reason |
| --- | --- |
| `SRC-068-T11120`, scratch 0001 | Included: descriptor of `tmp/acquisition/src068/__pycache__/acquire_presentations.cpython-314.pyc`, 9,860 bytes, 68 physical lines, hash `578103af6da5fb698f45598bbb1b4a7c7eeb4103c2759048d7a4049b601a8241`. The producer deliberately includes all file types. A physical-line count does not turn a bytecode file into substantive source text. |
| `SRC-068-T11528`, scratch 0409 | Included: descriptor of `tmp/acquisition/src068/web_source_presentations.json`, 612,289 bytes, 8,594 physical lines, hash `dffd70a531ae3093921f542ebad17cb1be445369b4fe09e55eb5566cc585d0fa`. Its descriptor is metadata; the referenced JSON may contain evidence requiring separate content/version reconciliation. |
| `SRC-068-T11119` | Excluded: actual preceding `[DIFFERING-DISPLAY-016]` record belongs to `SRC-068-H277` and concerns an unverified Scribd display, rights wording and absent body. Its separate source/access distinctions remain preserved and unresolved. |
| `SRC-068-H278` | Excluded by `record_type`: the inventory heading is a structural record. The lead may give it a separate metadata-structure disposition, with its own membership, rather than hiding it in the 409 count. |
| A title, theorem or abstract merely containing `[SCRATCH-0001]` | Excluded unless every field and the complete producer grammar match. A substring search supplies a lead, not this partition. |
| An inventory row under SRC-061, SRC-064 or SRC-066 | Excluded from this first batch even when its descriptor role is similar. Its path convention, wrapper and parent must be checked separately. |
| Same path or same digest in another record/edition | No automatic merge. Preserve each historical record identity, source identity, capture context and version evidence. |

## Full-set check needed for an admitted batch

The lead can fold the following into the next scheduled complete streaming
reconciliation of the existing catalog, avoiding an extra independent full
scan for this small batch:

1. Pin the exact catalog bytes by hash, size, header and total count. A changed
   fingerprint requires a new input identity rather than reuse of this batch
   receipt. Check all historical stable IDs for uniqueness through the chosen
   existing mechanism.
2. Evaluate the precise predicate on every CSV row, collecting the selected
   historical IDs and original row payloads. Resolve the source and parent
   descriptors uniquely. Reject a malformed record; do not widen the grammar
   merely to retain a desired count.
3. Require the selected ID set to equal exactly
   `{SRC-068-T11120, ..., SRC-068-T11528}`, with 409 elements, exact scratch
   ordinals 1–409, no other selected IDs, and no additional child of H278 left
   outside the documented structure without an explicit separate disposition.
4. Preserve a membership receipt containing the catalog fingerprint,
   predicate/version, every selected stable ID, original payload or payload
   digest, extracted descriptor fields and its source/parent join. Preserve
   the original record; the disposition is additional reconciliation evidence.
5. Keep the complement accounted for. This batch selects 409 of the frozen
   9,162,150 records; the other 9,161,741 are outside this predicate and retain
   whatever dispositions or unresolved status their own reviews establish.
   The arithmetic difference is not a writing-progress percentage.

A successful run establishes exact full-catalog membership and count for the
proposed predicate. It does not prove the referenced files' identities at the
current filesystem, prove their bodies have been read, settle rights, merge
source versions, or complete substantive presentation mappings.

## Adjacent bounded work and remaining decisions

The existing profile's 1,152 scratch-marker records are concentrated as follows:

| Source | Profile count | Producer evidence for the next scoped batch |
| --- | --- | --- |
| SRC-061 | 177 | `tmp/acquisition/src061/build_acquisition_note.py:288–295,382–388`: two nested inventory headings; JSON-quoted path relative to its acquisition directory, bytes and SHA-256, without physical-line field. `Ledger.topic` at 170–182 adds OPEN without a TOPIC prefix. |
| SRC-064 | 189 | `tmp/acquisition/src064/build_acquisition_note.py:190–198,214–232,336–341`: root-relative path, bytes, physical lines, SHA-256, TOPIC/SCRATCH prefixes. |
| SRC-066 | 377 | `tmp/acquisition/src066/build_acquisition_note.py:202–210,226–244,348–352`: corresponding typed inventory with its own source heading and root-relative path. |
| SRC-068 | 409 | Complete first-batch block checked here. |

The producer evidence makes the remaining 743 records promising next metadata
batches. It does not establish that every occurrence of a scratch marker in
an arbitrary title belongs to them. Verify their exact parent/path structure,
full-string grammar, sequence and catalog membership separately. Examples in
the profile and acquisition notes are leads, not a substitute for that check.

The 68 source descriptors also have a directly justified structural predicate:
`record_type=source`, `stable_id=source_id`, empty parent, one-item hierarchy
path equal to source title, and displayed title equal to source title. They
should remain preserved as source-identity nodes carrying metadata and
locators. Whether their final disposition name is `source descriptor` or a
specific metadata subtype belongs to the lead's schema decision. No descendant
is selected by that predicate.

Remaining semantic decisions are the lead's choice of disposition representation
in existing mechanisms; the review/admission of the predicate and membership
receipt; separate handling of the H278 structural header; obligations arising
from the retained file bodies and differing source displays; and substantive
unit/version mappings for the remaining catalog. The completed manuscript
inventory is not reopened by this proposal, and CAT-01 is not declared complete.

## Evidence fingerprints and method

| File read | SHA256 |
| --- | --- |
| `spec/research/edition-2026-catalog-record-profile.md` | `990154D465CF8F709CEB480D48B044E1E552C52C91CD33F1E059CC33DD7D33FE` |
| `spec/research/edition-2026-catalog-record-profile.json` | `3E92DE2614473EDA50AC00EFAE60B48C5DBAA17B5DED4FACBE89209AEF03F796` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | `A945CF2AFFA5B7F606D14C0AD2F777AAA66DA492D1FBC735CCDB5E35E9458AE1` |
| `spec/EDITION-2026-CONTRACT.md` | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/external-coverage-assignment-index.json` | `2A2BF44FCB19D0B823CF2962751AD05322CDBF269313E38F94DA163B7CCB58BD` |
| `tools/build_coverage_manifest.py` | `60D521B20641358A9E8C6A0E723D943F44B9A1B68B8FBD0B8F951494CA8AE5E1` |
| `tmp/acquisition/src061/build_acquisition_note.py` | `DE6EE5E571089BEDF5D13B0181C5CFCD42A8E5E1EF454CB0A6C5C541D2E2F0F7` |
| `tmp/acquisition/src064/build_acquisition_note.py` | `3231A8B09187E4E16D77D4B22873E6684C7D6170CA309B792DDA16BDE3D4900D` |
| `tmp/acquisition/src066/build_acquisition_note.py` | `43E03A139656768D3E5FBB4FDA82BF92BDD2876CB7322C110975CFC584A62A50` |
| `tmp/acquisition/src068/build_acquisition_note.py` | `3B1851D347B0A2B2F4ADBE74F59F3A0D474B46AB77ABE20543B750B876597C40` |
| `spec/research/acquisition-src-068.md` | `70CE8846711F9B63FC60EEE2AF7A90F0B56FD2BFEC8034B2ACB3985777964150` |

The research skill's primary-evidence and single-note practice was used. The
assignment's explicit no-delegation boundary governed execution. The profile
was parsed for all 68 source count objects and the four scratch groups; exact
producer sections and actual bounded data supplied the recommendation. No new
full multi-gigabyte scan, source acquisition, software test, build, render or
delegation occurred. This note is the sole write. Catalog and admission
decisions remain with the lead.
