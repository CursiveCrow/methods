# Publication, admission, and review state

Inventory date: 6 September 2026 Pacific time; live checks on 7 September 2026, 06:49–06:55 UTC. Only this Markdown and its companion JSON are written.

## Current conclusion

**Final publication readiness and user acceptance are not established.** The live terminal-readiness manifest says OPEN. Its public PDF is still the identical August artifact. Formal reviewed-record stores do not encode the later September proof writing as full admissions. Conversely, their pending flags do not prove that the corresponding manuscript mathematics is absent.

The two frozen archival source files were verified against both the before-inventory snapshot and the inherited corpus manifest. Both hashes and byte counts agree with the live files.

## Exact dates and publication identity

| Artifact | Timestamp / recorded standing |
| --- | --- |
| spec/verification/terminal-readiness-manifest.json | Filesystem LastWriteTimeUtc 2026-08-18T08:06:59.9021243Z; no embedded generation timestamp |
| handbook/main.pdf | Filesystem LastWriteTimeUtc 2026-08-18T07:39:32.8088963Z; 4,442,893 bytes; manifest records 836 pages |
| spec/compendium-volume-manifest.json | Filesystem LastWriteTimeUtc 2026-08-18T07:58:19.5447871Z; publication_status construction-draft; release_ready false; final_release_evidence null |
| manuscript-snapshot-before.json | Embedded captured_utc 2026-09-07T06:32:40.260857+00:00 |
| spec/inherited-corpus-manifest.json | Filesystem LastWriteTimeUtc 2026-08-12T10:32:18.2587155Z |

The current main.pdf SHA-256 is ee4c5324c1aac7fc3b0e13fba816b35ec6f39be059e807b01695fe1a9900851f; it matches the August terminal/publication manifests exactly. That proves artifact identity, not that September additions were compiled or inspected. Its publication-artifact gate PASS is compatible with both construction-draft and overall OPEN. The recorded 836 pages were not recounted or rendered in this subtask.

Filesystem modification times are not silently promoted into actual review/run times. The terminal manifest contains no generated_at field. The raw UTC snapshot timestamp is retained; a shell parser's local-time conversion was not treated as a different capture instant.

## Stored terminal gate states

Evidence: spec/verification/terminal-readiness-manifest.json, JSON object gates.

| Gate | Required | Pass | Residual | Stored state |
| --- | ---: | ---: | ---: | --- |
| inherited_interval_restoration | 282 | 265 | 17 | OPEN |
| inherited_source_order | 0 | 0 | 0 | PASS |
| source_unit_admission | 1055 | 0 | 1055 | OPEN |
| handbook_unit_admission | 18174 | 0 | 18174 | OPEN |
| register_obligation_closure | 615 | 0 | 615 | OPEN |
| acquisition_gap_resolution | 6 | 0 | 6 | OPEN |
| presentation_packet_content_admission | 0 | 0 | 0 | PASS |
| external_coverage_assignment | 9162150 | 0 | 9162150 | OPEN |
| publication_artifact | 1 | 1 | 0 | PASS |

The stored non-user residual count is **9,182,017**. The source-order PASS is bound to a historical tree hash and 789 TeX files; it is not a current checker run. The packet PASS has required=0 and zero admitted packets: it is a vacuous gate, not positive content admission. The 9,162,150 external assignments were read only from the small manifest/index record; neither large coverage catalog was opened.

## Live ledger state versus the terminal snapshot

The source-unit crosswalk now has **1,055 rows**, all with destination identified, static=pass, audit_result=pending/unclassified and provenance_disposition=open/missing. Every source-fidelity, topic-specialist, adversarial-publication, build, and visual field is pending. Thus no source unit has the complete admission gate set.

The terminal manifest records only 1,037 source-unit static passes and 18 residuals. Its bound crosswalk digest is edf072b26e6070623b7ae27269e4f31a408353968c8d8bc6ae97fd82fc095948. The current file digest is ce75c60e6946b6432fe7914e583aa3cff28ab94bc6d24252d979c2b18ad4c050, LastWriteTimeUtc 2026-08-18T09:01:01.1483886Z. This binding is stale. The later all-static-pass flags do not imply passage of the other five gates or current validation of every destination.

The register-obligation closure CSV contains **615 rows, all OPEN**, all manifest bindings open, and all six review/verification fields pending. Its current digest still matches the terminal binding. The 18,174 handbook-unit reverse-ledger figure is a dated physical/unit inventory, not an accepted-content count; its reviewed-record store is empty.

| Reviewed provenance store | Records | LastWriteTimeUtc |
| --- | ---: | --- |
| spec/provenance/reviewed-source-unit-records.json | 1055 | 2026-08-18T09:00:41.0925995Z |
| spec/provenance/reviewed-handbook-unit-records.json | 0 | 2026-08-18T07:57:28.4638034Z |
| spec/provenance/reviewed-register-obligation-records.json | 0 | 2026-08-14T11:47:23.9903774Z |
| spec/provenance/reviewed-acquisition-gap-resolutions.json | 0 | 2026-08-14T10:21:25.4783546Z |
| spec/provenance/reviewed-presentation-packet-admissions.json | 0 | 2026-08-14T01:35:58.6543518Z |

The 1,055 source records are all pending/unclassified and open/missing. They are not 1,055 completed reviews merely because the filename begins reviewed-. The source schema explicitly says schema validity is necessary but insufficient; full transcription additionally requires all ten completeness dimensions, all six verification gates, exact authority/destination/evidence bindings, and defect exclusions. See reviewed-source-unit-records.schema.json:5 and :373–450.

The acquisition-gap reviewed store has zero terminal records. Its three nonterminal reports say not_clean and gap_status_effect=none; a further planned-presentation item also has effect none. This does not establish that no sources were acquired later. New holdings and old formal gap-resolution entries answer different questions.

The presentation admission policy (spec/presentation-packet-admission.md:9–21) requires a terminal record pinning packet/destination bytes, authority and presentation identity, complete content projection, and all six gates. Its current projection has zero packet files and zero independently admitted packets. Later source-specific Markdown ACCEPT records have not become these formal packet records.

## Frozen archival source identity: verified

Evidence: spec/inherited-corpus-manifest.json and the source entries in manuscript-snapshot-before.json, checked by read-only SHA-256 hashing of the actual two files.

| Frozen source | Bytes | Manifest = snapshot = live SHA-256 |
| --- | ---: | --- |
| source/formal-logic-reference.tex | 762835 | 0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc |
| source/formal-logic-reference.pdf | 2042303 | 0a8fb84042175343e5ba8bbcf65d4804d8a4019367edb3d22473927a3399bb3f |

Both comparisons passed. These are the frozen Version 1.0 archival authorities (manifest: 17,206 TeX lines and 251 PDF pages), not the current handbook source or publication PDF. Hash preservation of an archive is not a claim that its mathematical defects are retained in current reader text, nor proof of current full-compendium completion.

## Historical fixed/done and source/text acceptance

The defects register currently contains **37 historical fixed-status rows and 51 open rows**. The apparatus register contains **18 done (6348bdc) and 183 open rows**. spec/registers/execution-notes.md records the 10 August 2026 Phase-2 work and its bounded review/sweep results. Those strings preserve history; this subtask does not recertify their current mathematical, routing, apparatus, or publication standing. The formal closure projection still remains OPEN.

Three representative source/text acceptance cases demonstrate the boundary:

- **N-c-010**: p09-n-c-010-independent-review-record.md reports three ACCEPT verdicts only for N-c-010.a/.b and the controlling W3C presentation; N-c-010.c and Part IX/build/visual/final acceptance remain open. Its filesystem timestamp is 2026-08-23T04:43:44.1975373Z. The currently saved n-c-010.tex no longer matches its accepted snapshot hash.
- **Thomas 1996 precursor**: p09-thomas-1996-report-independent-review-record.md, timestamp 2026-08-24T07:28:55.2490341Z, admits only the named 1996-report portions of N-c-013.e/N-c-014.e. It explicitly excludes the registered 1997 chapter and whole-presentation/part/publication acceptance. Current N13/N14 bytes no longer match its frozen accepted snapshots.
- **N-c-016**: p09-n-c-016-integrated-independent-review-record.md was recorded on 6 September from the completed 24 August cycle (filesystem timestamp 2026-09-06T07:43:09.9351903Z). Three reports say ACCEPT, but all end REGISTER STATUS: OPEN. The checkpoint expressly withholds source reacquisition/authentication, static/build/visual/section/global/user admission; it lacks required reviewer model-version/evidence-digest fields. Its recorded snapshot has 2,070 lines; the current file has 2,167. It is historical bounded source/text evidence, not a new current acceptance.

| Snapshot-bound manuscript | Accepted digest | Current digest | Match |
| --- | --- | --- | --- |
| handbook/parts/p09/presentations/n-c-010.tex | 2eca1d578b5734e8bac039bdbfa7a2f7bef5364e7268a11a25b02e1b09a18c68 | a5e7135ded58aa5e8778ac7a71e0b9bbbc3ba57e62fa7970e4fcc3bdb4493f93 | false |
| handbook/parts/p09/presentations/n-c-013.tex | 23e73da416ce583adf084e1d16e4a5846ac9659e4ed0e937a1cb00fa0738afed | e98d593a11b0bb96d3749a8c9855c2fea2ea22ddef9518bb46be411bcdd274a7 | false |
| handbook/parts/p09/presentations/n-c-014.tex | f9576bb10063037cdfd9018e6dc7dfb553651590fb74fc77d2d33eebbf4d5915 | fd2b17ec24d4e7ad48d69cdff593d5adff1154a443fcfa3f45e5d47034de0a3f | false |

A changed digest does not establish that a later edit is wrong. It establishes that the old exact-byte verdict does not by itself admit the new bytes; affected-scope review must be associated with the current version.

## September scoped proof reviews

The companion JSON indexes **42 dated review/writing/status artifacts**, with their exact file timestamps and sampled explicit scope markers. This is an artifact inventory, not a count of distinct independent reviews or admitted requirements.

The current manuscript-completion-status record (LastWriteTimeUtc 2026-09-07T06:11:04.3043804Z) expressly says it is not a replacement acceptance manifest. Its 80 routed Part X proof items are a scoped output count, not 80 completed register rows. The adjoint/presheaf progress record at the same date identifies eight new proof pairs and the actual review scopes, while explicitly leaving further presheaf logic, whole-Part-X, full source-presentation coverage, global reconciliation, and publication open.

P3/P7 Craig–Robinson–Beth and the PCF introduction have dated scoped completion/review records. P9 records likewise describe bounded work: N15 keeps its exact Thatcher–Wright source obligation open; N17 distinguishes report locators and ongoing source obligations; N18 explicitly says old reconstruction-closure statements do not establish completion of its expanded treatment. None of these notes claims all six formal gates for the entire book.

## Final user acceptance

The actual file spec/provenance/user-final-acceptance.json is absent. Only its schema exists. The schema requires a user-supplied acceptance record after all non-user residuals are zero and pins the exact readiness manifest and final PDF. Schema presence, AI ACCEPT verdicts, progress notes, a prior saved PDF, and an ordinary user instruction to continue are not substitutes for that record.

## Why these counts cannot yield a writing percentage

1. 265/282 measures a dated set of inherited restoration intervals, not coverage of current new topics, proofs, variants, examples, or source books. The manifest separately reports 266 restoration records; neither count is a new-content completion total. The directory currently has 265 SRC record files and 9 PRE record files, whose mere presence does not rerun the gate.
2. Restoration, source units, handbook physical units, register obligations, acquisition gaps, packets and external coverage assignments have different units and overlap. Summing them does not define a weighted writing denominator.
3. The terminal artifact is dated August; later mathematical writing and corrections are not represented by a fresh terminal run, and the crosswalk binding is demonstrably stale.
4. A stored static pass, historical fixed/done marker, local proof review, source-text ACCEPT, build/visual result, and user acceptance establish different things.
5. Under the current full-compendium contract and correction policy, old treatment ceilings and scope-pointer allowances cannot serve as completion criteria.

No percentage is inferred. Current writing coverage is given by the separate row-level inventory; formal publication admission remains open. No build, test, render, acquisition, regeneration, or commit was performed in this subtask.

