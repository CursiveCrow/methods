# Wave tooling specification (lead-owned tools)

Repository: C:/Dev/the-methods-of-reason (Windows; Python 3.14; Git Bash + PowerShell).
Governing plan: C:/Users/Crow/.claude/plans/c-users-crow-codex-attachments-7438f70f-synthetic-bonbon.md

## Rules for every tool

- Stdlib only, plus modules already in the repo (`tools/symbol_registry.py`, `tools/check.py`). PyMuPDF (`fitz`) and `pypdf` are installed and may be used for PDF page counts and text.
- Write text files with `newline="\n"` and UTF-8 with no BOM. Canonical files are LF. Read with `encoding="utf-8-sig"`.
- Each tool has a `--selftest` that runs assert-based checks on small in-memory or temp fixtures. It exits 0 on pass. It must not touch repository files.
- Every mutating command defaults to a dry run. `--apply` performs the writes. Writes go to a temp file followed by `os.replace`.
- Exit codes: 0 means OK, 1 means findings or refusal, 2 means a usage error.
- No inline regexes are run from Bash heredocs; all logic lives in these `.py` files.
- Never modify `source/formal-logic-reference.tex`, `handbook/restoration/**`, `handbook/generated/**` (except through the existing generators), `citations/**` or `source/references/**`.

## 0. Toolchain (binding; supersedes any MiKTeX command below)

All TeX builds use TeX Live 2025 by absolute path, because MiKTeX lacks the Cyrillic encodings the book needs:
`C:/texlive/2025/bin/windows/pdflatex.exe -no-shell-escape`, `C:/texlive/2025/bin/windows/biber.exe`,
`C:/texlive/2025/bin/windows/makeindex.exe`; full builds use `latexmk -r tools/texlive.latexmkrc -pdf ...`
with `C:/texlive/2025/bin/windows` first on PATH. Never pass `-disable-installer` (a MiKTeX-only flag).

## 1. `tools/find_fused_spaces.py`

Purpose: detect, and optionally repair, text where a space was dropped next to a number or between words. Examples: "in1348", "Theorem4.13", "300seconds", "Date:3October2026", "NotreDame".

API:
- `scan_tex(text) -> list[Hit]`
- `scan_md(text) -> list[Hit]`
- `Hit` has `line`, `col`, `cls`, `match` and `suggestion`.

**Masking (TeX).** Blank out the following before matching. Replace each masked character with a space and keep newlines, so line and column numbers stay valid.
- Comments: an unescaped `%` through the end of the line.
- `verbatim`.
- Math: `\(..\)`, `\[..\]`, `$..$`, `$$..$$`, and the environments `equation`, `align`, `gather`, `multline`, `eqnarray`, `array`, `tabular`, `displaymath`, `math`, including starred forms.
- The arguments of: `\cite*` and any `\…cite` (including the optional `[...]` locator), `\label`, `\ref`, `\cref`, `\Cref`, `\eqref`, `\pageref`, `\autoref`, `\hyperref[...]`, `\href{...}`, `\url`, `\input`, `\include`, `\entrysources`, `\showcalculus`, `\entrycalculus`, `\hbrule`, `\calculussheet`, `\begin`, `\end`, `\index`, `\texttt`, `\nolinkurl`.
- The first and second mandatory arguments of `hbtheorem`, `hblemma`, `hbcorollary`, `hbdefinition`, `hbconvention`, `hbmethod`, `hbexample`, `hbwarning`, `proofboundary`, `annexitem` and `systementry`, which are labels and status tokens.
- `proved=…`, `cited=…` and `sketched=…` tokens.
- Bare `prefix:token` labels (prefixes `part sec entry def thm tab fig sheet rule annex ch`).
- Control-sequence names.

**Classes.**
- **A — word then a number.** A word of 2 or more letters followed directly by 1–4 digits, where the word is a common English word or a structural noun. This is a lowercase-word or Capitalized-noun class.
  - Allowlist the word list from the integrity design: to, and, or, both, between, than, of, at, is, be, are, from, through, with, by, in, on, for, as, value, stage, rank, input, step, level, length, size, degree, arity, distance, around, about, planned, page, pages, pp, line, lines, Theorem, Lemma, Proposition, Corollary, Definition, Section, Chapter, Example, Table, Figure, Remark, Exercise, Appendix, Volume, Case, Axiom, Equation, exactly, least, most, only, every, each, returned, printed, contains, has, gives, yields, circa, until, after, before, since, during.
  - Also flag any lowercase word of 3 or more letters followed by a 3–4-digit year: `(?<![\w/.\\-])[a-z]{3,}\d{3,4}(?!\d)`.
- **B — number then word.** `(?<![\w/.\\-])\d{1,4}[A-Za-z]{3,}`, excluding the allowlist (`2EXPTIME`, `2SAT`, `3SAT`, `2NEXPTIME`, `1st`, `2nd`, `3rd`, `Nth`-style ordinals, `\d+th`, `\d+st`, `\d+nd`, `\d+rd`, and units like `pt`, `em`, `ex`, `cm`, `mm`, `in`, `bp`, `sp`, `pc` when a dimension is intended). Also flag a month name squeezed between digits, `\d(January|…|December)\d`.
- **C — punctuation then a character.** `(?<=\w)[:;]\d(?=[A-Za-z])` and `(?<=[a-z]),(?=\d{4}\b)`. Example: "Date:3October2026".
- **D — CamelCase review candidates.** `\b[A-Z][a-z]{2,}[A-Z][a-z]{2,}\b` in prose, excluding an allowlist file `tools/fused_allowlist.txt` (create it with common legitimate CamelCase words such as PostScript, JavaScript, LaTeX, BibTeX, MiniSat, PageRank, NetLogo, MathSciNet, DeepMind, OpenAI, GitHub, YouTube and McCarthy-style surnames, Mc[A-Z]/Mac[A-Z]). Class D is never auto-fixed.

**CLI.**
- `find_fused_spaces.py [--md] [--json] PATH...`: directories recurse over `*.tex`, or `*.md` with `--md`.
- `--classes A,B,C` (default `A,B,C`), `--include-d`.
- `--fix`: inserts a single space at the split point for classes A–C. Use `~` instead of a space after Theorem, Lemma, Proposition, Corollary, Definition, Section, Chapter, Example, Table, Figure, Remark, Exercise, Appendix, Equation and Axiom in TeX files.
- `--fix` refuses files under `handbook/restoration/`, `handbook/generated/` and `source/`, and files listed as digest-pinned retained files in `tools/check.py`; read that list by importing check.
- `--manifest <batch-intake json>`: scan the bodies and annexes listed in it.
- Exit 1 if any class A–C hit remains.

**Selftest.** Include positive cases ("around1115", "in1348", "Theorem4.13", "between0 and1", "Date:3October2026", "300seconds"). Include negative cases: `\cite[p.~97]{Rubinstein2015LectureNotes}`, `\label{thm:p04-wc-basic}`, `$x_1+x2$`, "2EXPTIME", "ET5", "CF3" inside math, `annex:p15.x`, and "Lemma~4.4" (which is OK).

## 2. Additions to `tools/check.py`

Add two handbook categories, inserted into `HB_CATEGORY_ORDER` before `env-grammar`:
- **`fused-number`:** import `find_fused_spaces.scan_tex`, classes A–C, applied to every scanned `.tex` file except restoration captures and digest-pinned retained files.
- **`stub-marker`:** inside `annexitem` bodies and `proof` environments in `handbook/annex/**`, and in any body file, flag `\hbstub`, `TODO`, `FIXME`, `TBD`, "left to the reader", "omitted for brevity", "standard argument", "routine verification", "similarly for the remaining cases", "the remaining cases are similar", "details omitted" (case-insensitive).

Both categories are non-hard findings unless `--strict`, matching the existing convention. Do not change any other category's behaviour. Run the existing `tools/test_*` suites that import check and confirm they still pass:

```
python -B -m unittest discover -s tools -p "test_check*.py"
```

## 3. `tools/held_sources.py`

Purpose: build `spec/coverage/edition-2026/held-sources.json`, an index of locally held source files.

**Inputs.**
- `citations/manifest.json` and `citations/FILENAME-MAP.csv`, if present.
- Every `source/references/*/manifest.json`, `*.json` access records and README or READING files.
- The queue `spec/coverage/edition-2026/completion-work-queue.jsonl`, streamed. Read `source_presentations[]` and any of these keys: `local_path`, `local_artifact`, `local_artifacts`, `artifacts`, `local_capture`, `sha256`, `body_state`, `body_acquisition_standing`.
- A filesystem walk of `citations/` and `source/references/` covering PDF, DjVu, EPUB, HTML, TXT and images.

**Output.** One entry per held file:

```json
{"path","sha256","bytes","kind":"pdf|html|txt|image|other","pdf_pages":int|null,
 "source_ids":[...],"bibkeys":[...],"titles":[...],"version":"<as recorded or null>",
 "extent_verified":bool|null,"body_state":"<as recorded or null>","access_basis":"<as recorded or null>",
 "evidence":["<manifest/queue record that names this file>"],"location_stable":true}
```

Also emit `source_index`: `source_id -> [paths]`.
- Never invent a version or extent. Unknown means null.
- Hash files with streaming reads.
- Do not open more than the first page for the page count. Use `fitz`, falling back to `pypdf`.

**CLI.**
- `held_sources.py build [--out PATH]`: dry run prints a summary; `--apply` writes.
- `held_sources.py lookup SOURCE_ID|PATH`.
- `--selftest`.

## 4. `tools/ledger_patch.py`

The ledger is the nine shards in `spec/coverage/edition-2026/current-fulfillment/*.jsonl`. Section ids are unique across all shards. Each shard has a `<shard>-receipt.json`.

**Row hash.** `sha256` of the exact line bytes without the trailing newline.

**Editable fields:** `status`, `reader_evidence` (append-only), `missing_pieces`, `unassessed_scope`, `observed_utc`, `fulfillment_revision`. All other keys must remain byte-equal in value. The rule is "the parsed value is equal", plus re-serialization of untouched rows unchanged: only changed lines are rewritten, and the other lines' bytes are kept.

### `apply`

Input: `--proposals FILE.jsonl`, one proposal per line:

```json
{"section_id":"52.8","original_row_sha256":"...",
 "set":{"status":"partial","missing_pieces":[...],"unassessed_scope":[...]},
 "append_reader_evidence":[{"path":"handbook/...","anchor":"sec:...","line_start":1,"line_end":99,"read_extent":"...","components":["..."],"assessment_ids":["..."]}],
 "assessment_ids":["CA-..."],"reason":"..."}
```

Rules:
- Refuse if the pin mismatches, if a section has two proposals in one run, if the status is invalid, or if an immutable key would change.
- Refuse an `append_reader_evidence` path that is missing, or whose `line_end` exceeds the file length.
- Refuse an anchor not found in the file. Search for `\label{anchor}` or the environment's first argument equal to the anchor.
- Fill each new evidence entry's `sha256` (uppercase hex, matching existing rows) from the current bytes. Fill `route_state` as `on_current_recursive_input_route` if the path is in the `\input` closure of `handbook/main.tex`, else `off_route`. Compute the closure by reusing `symbol_registry.ReaderIndex` or `check._hb_static_input_reachability`, whichever exists and works; check what they expose.
- Set `observed_utc` to now, as `YYYY-MM-DDTHH:MM:SSZ`.
- Write `fulfillment_revision = {"reason", "patch_id", "assessment_ids", "previous_observation": {"status", "missing_pieces", "unassessed_scope", "observed_utc", "row_sha256", "prior_revision": <old fulfillment_revision or null>}}`.

**Upgrade rule (Opus-only, 2026-10-03 user decision: every agent is Opus 5.5; no cross-family assessors exist).** Changing status to `authored_unreviewed` requires all of the following, otherwise refuse:
1. `assessment_ids` reference at least 2 files under `spec/coverage/edition-2026/assessments/**/<id>.json`.
2. One has `assessor.role == "first"` and another `assessor.role == "confirm"`, with different `assessor.context_id` values (independent fresh contexts). `assessor.family` is recorded but is not required to differ.
3. Every component and duty verdict in both is `covered`.
4. Every `inputs.tex[].sha256` equals the current file hash.
5. At least one evidence path is on route.
6. `missing_pieces` and `unassessed_scope` are both empty.

There is no override flag.

Downgrades and any other change need at least 1 assessment id, or an explicit `"reason"` starting with `lead:` for mechanical evidence refreshes.

Strings in `set` must have no fused-number hits (classes A–C of `find_fused_spaces` in plain-text mode).

Output: dry run prints an old→new table. `--apply` rewrites only the changed lines per shard, atomically, then refreshes that shard's receipt. In the receipt, set or replace the `current` object to `{"ledger_sha256", "rows", "unique_section_ids", "status_counts", "by_part", "observed_utc"}`, and append any earlier `current` to a `history` array. Leave all other receipt keys untouched. Serialize rows with `json.dumps(obj, ensure_ascii=False, separators=(",",":"))`.

### `check` invariants (exit 1 on a hard failure)

- **I1:** exactly 2,475 unique section ids, equal to the id set of `spec/proposed-table-of-contents.json` (`numbered_sections`).
- **I2:** status is in the 4 allowed values.
- **I3:** AU implies empty `missing_pieces`, empty `unassessed_scope` and non-empty evidence. With `--final` this is hard and also requires the evidence hashes to be live; otherwise violations are reported as warnings with counts. Include "AU-stale", the count of AU rows whose evidence sha differs from the file.
- **I4:** partial or missing implies non-empty `missing_pieces` (warning, or hard with `--final`).
- **I5:** unassessed implies non-empty `unassessed_scope`. With `--final`, zero unassessed rows.
- **I6:** each AU upgrade carrying a `fulfillment_revision.patch_id` from this tool has a `first` and a `confirm` assessment from distinct contexts on file.
- **I7:** duty conservation. Every component id of every queue unit is either covered by AU evidence `components`, or appears in an open row's `missing_pieces` items (dict items with `component_ids`, or `[component:ID]` tags in strings), or appears in `spec/coverage/edition-2026/unit-residuals.jsonl`. Report the unaccounted count by unit; hard with `--final`. Stream the queue, which is 43 MB.
- **I8:** blocker refs (`ACQ-*`, `MATH-*`, `POL-*`) resolve to records in `acquisition-requests.jsonl` or `blockers.jsonl`.
- **I9:** each receipt's `current.ledger_sha256` equals the shard's actual sha256.
- **I10:** no fused-number hits in editable string fields (warning, or hard with `--final`).
- **I11:** no row key outside the union of keys currently present.

### `report`

`report --wave NN [--prev-tag TAG]` writes Markdown to stdout in the integrity-design format:
- section status counts with deltas;
- AU-stale;
- partial with writable duties;
- blocked by source, math or policy (by `missing_pieces` item kind or tag);
- unassessed;
- downgrades listed first;
- the acquisition summary, if the file exists.

The report never uses the words done, complete, finished or closed about manuscript units, and ends with the standard non-acceptance sentence.

### `show SECTION_ID`

Prints the shard, row sha and pretty JSON of the row.

### `missing_pieces` item format

Items may be strings (legacy) or dicts:

```json
{"duty","component_ids":[...],"kind":"writable|blocked_source|blocked_math|blocked_policy|assessment_dispute","blocker_ref":str|null,"since":"..."}
```

Treat legacy strings as `kind="unclassified"`, unless they start with a `[kind:REF]` tag.

## 5. `tools/waves.py`

Paths: wave root `work/waves/wNN/`; unit builds go under `tmp/unit-builds/<stem>/` (gitignored).

### `packetize wNN --parts P1,P2,P15 [--carry FILE] [--census FILE]`

1. Read the ledger shards, the TOC JSON, the queue (only the needed units), `held-sources.json`, the census and the blockers.
2. Select open rows (status != AU) of the given parts, plus carry-over.
3. Cluster within each chapter by shared facet `unit_id` (union-find). Rows with no facets form singletons.
4. Bin-pack in TOC order, up to 4 sections or 8 open components per packet. Compute `max_blocks = min(4, 1 + ceil(components/3))`.
5. **Source gate.** If every facet unit's required source presentations are absent from `held-sources.json`, and the census verdict is not full or partial, then write blocker records instead of a packet, and add entries to an acquisition-needs list.
6. **Ownership.**
   - New files: `handbook/parts/pNN/<slug>.tex`, `handbook/annex/pNN/<slug>.tex`, `handbook/bib/intake-pNN-<slug>.bib`, `handbook/registry/symbols-intake-pNN-<slug>.csv`, `spec/research/edition-2026-pNN-<slug>.md` and `spec/research/edition-2026-pNN-<slug>-return.json`.
   - The slug derives from the chapter title plus a short packet id. It must not collide with existing files or other packets.
   - For P13, the body path is `handbook/parts/p13/presentations/<slug>.tex`.
   - Existing hosts from `reader_evidence` paths are editable by the packet only if they are not under `restoration/` or `generated/`, are not drivers (`handbook/parts/pNN.tex`, `handbook/annex/pNN*.tex`, `main.tex`, `handbook.sty`, `frontmatter.tex`), are not digest-pinned retained files, and no other packet in the wave references the same host. Otherwise the host is read-only and changes go through patch requests in `work/waves/wNN/patches/<packet>-<n>.json`.
   - Packets sharing an editable host or a unit are grouped into one lane, in TOC order.
7. Assign a `label_tag` (`pNN-<short>`), unique across the repo's labels.
8. **Insertion anchor.** Propose the host file and the `\input` line after which the new body should go: after the last routed input among the chapter's existing evidence files, or the previous chapter's. The same applies to the annex. Never place it inside a `\AddToHook…\RemoveFromHook` bracket.
9. **Heading level** from the host table:
   - Flat chapter lists (`parts/p11.tex`, `p13`, `p15`–`p19`, `parts/p12/automation-and-mechanization.tex`): `\chapter`.
   - Section hosts (`p02/first-order-logic`, `p03/classification-theory`, `p03/preservation-abstract-logic`, `p07/lambda-calculi-and-type-theories`, `p12/rewriting`): `\section`.
   - Subsection hosts (`p09/logic-in-computer-science`, `p10/algebraic-and-categorical-logic`, `p04/frontiers-of-computability`): `\subsection`.
   - Mixed drivers (`parts/p01`–`p08`, `p12.tex`, `p14.tex`): match the neighbouring sibling's first heading.
   - Supplements of an existing chapter use one level below the host.
10. **Packet JSON** `work/waves/wNN/packets/<id>.json` contains: `id`, `wave`, `part`, `chapter`, `sections` (each with `section_id`, `title`, `status`, `missing_pieces`, `unassessed_scope` and `reader_evidence`), `units` (each with `unit_id`, `title`, `required_components` (id, description, `success_condition`, `failure_condition`), `source_presentations` and `held_paths`), `owned_files`, `editable_hosts`, `readonly_hosts`, `existing` (labels and files already treating these sections, found by grepping `reader_evidence` anchors, labels and the queue's destinations), `label_tag`, `heading_level`, `insertion` (body and annex host plus after-line), `toc_tag` (the `%% toc: P4 52 52.8,52.9` line), `max_blocks` and `lane`.
11. **Arguments file** `work/waves/wNN/args.json`: `{wave, root, maxConcurrent:12, agentBudget:940, lanes:[{packets:[{id,path,part,sections,max_blocks}]}]}`.
12. Print a summary: packets, lanes, sections, blocked sections, and the worst-case agent count, `sum(2*max_blocks + 1)`. If that exceeds 940, split the wave into wNNa and wNNb.

### `snapshot PACKET`

Records `work/waves/wNN/snapshots/<id>.json` with the sha256 of the owned files (`null` if absent), the editable hosts and the frozen sets: drivers, canonical bib and symbols, `symbol-scopes.json`, `handbook.sty`, `main.tex`. It also records check.py findings for the owned files, so later findings can be compared against this baseline.

### `verify PACKET`

Compares against the snapshot and runs these guards, reporting a JSON verdict `{hard:[...], findings:[...]}`:

| Guard | Check |
|---|---|
| G1 | Changed files lie only within owned and editable hosts. Use mtime/size prefilter, then hash, over `handbook/`, `spec/research/` and `spec/coverage/`. |
| G2 | Frozen files unchanged. |
| G3/G4 | New check.py findings in the owned files for annex-bidir, status-spec, duplicate-label, dangling-ref, label-prefix and bib-key. Bib keys present in the packet's own intake bib are OK. |
| G5 | Intake bib parses and its CSV header is `glyph,macro,role,scope,precedence,first_use,notes`. No `PNN.k` scopes. |
| G6 | Numeric page locators in `\cite[...]` for keys mapped to held PDFs lie within the PDF page count plus a printed offset; out-of-range is a finding. |
| G8 | `find_fused_spaces` classes A–C on owned files (hard). |
| G9 | Stub markers (hard). |
| G10 | Unit compile result. |
| G11 | New `\newcommand`, `\def` or `\DeclareMathOperator` in content (hard). |
| G12 | Unbalanced `\begin`/`\end` (hard). |
| G13 | Copied prose: longest common word run against the held source text for the packet's `held_paths`, extracted with `fitz`, cached under `tmp/unit-builds/_srctext/<sha>.txt`. 12 or more words is a finding; 25 or more, or 3 runs of 12 or more, is hard. Strip math and `\cite` before comparing. |
| G14 | Workflow words in body files: review, admission, admitted, ledger, assessor, intake, wave, "this record", "author block" (hard). |
| G15 | Prescriptive words in P19 files (finding). |
| G16 | Non-UTF-8 bytes or U+FFFD (hard). |

### `unit-compile PACKET`

Generates `tmp/unit-builds/<stem>/unit.tex` using this template:

```latex
\documentclass[11pt]{book}
\usepackage{handbook}
\usepackage[backend=biber,style=alphabetic]{biblatex}
\addbibresource{bib/handbook.bib}
\addbibresource{bib/intake-pNN-SLUG.bib}
\input{bib/inherited-keys}
\begin{document}
\setcounter{part}{ORD-1}
\hbpartidentity{pNN}\part{Scoped unit check}
[\chapter{Scoped host} if heading is section; \chapter{..}\section{..} if subsection]
\input{BODY-without-.tex}
\hbannexsetup
\hbannexchapter{N}{Scoped annex}
[\section{Scoped annex host} if annex starts with subsection]
\input{ANNEX-without-.tex}
\hbannexfinish
\backmatter\printbibliography
\end{document}
```

Printed ordinals:

| Parts | Printed ordinal |
|---|---|
| p01–p10 | 1–10 |
| p15–p19 | 11–15 |
| p11–p14 | 16–19 |

Run from `handbook/` (cwd):

```
pdflatex -disable-installer -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=<abs out> <abs unit.tex>
biber --input-directory <out> --output-directory <out> unit
```

followed by two more pdflatex passes. If the intake bib does not exist, omit that line.

Parse `unit.log` for:
- `^! ` errors;
- "Undefined control sequence";
- undefined citations;
- "multiply defined";
- "Missing character";
- the Overfull count;
- biber WARN and ERROR lines.

Undefined references are OK only if the label exists somewhere in the handbook tree. Output JSON `{ok, errors[], undefined_citations[], undefined_refs_unknown[], overfull}`. Use a timeout of 600 s per pdflatex pass.

### `report wNN`

Summarizes `work/waves/wNN/results.json` together with the verdict files.

## 6. `tools/integrate_wave.py`

Commands:

**`collect --wave N RETURN_JSON...`**
- Builds `spec/research/edition-2026-authoring-batch-intake-N.json` in the existing batch-group schema: `stem`, `part`, `bodies`, `annexes`, `symbol_intakes`, `bibliography_intakes`, `note`, `declared_proof_pairs` (count of `annexitem`), `integration_status:"returned"`, `placement`, `label_tag`, `proposed_decisions`.
- Validates that the files exist.

**`route --manifest M [--apply]`**
- For each placement `{host, after, input, supplement_of?}`, insert `\input{<input>}` on the line after the unique line in `host` that contains `\input{<after>}`.
- Refuse if the anchor occurs 0 or more than once.
- Refuse if the insertion point lies between an `\AddToHook` and its matching `\RemoveFromHook`. Detect these brackets by scanning the host lines.
- Refuse if the new file's first heading command (`\chapter`, `\section` or `\subsection`) differs from the first heading of the `after` sibling file, unless `supplement_of` is set.
- After a dry-run simulation, verify that each new input is reached exactly once from `main.tex`, using the static `\input` closure.
- Idempotent: an `\input` that is already present is a no-op.
- Annex placements work the same way.

**`unroute --manifest M --stems a,b [--apply]`**
- Removes those `\input` lines and sets the group status to `returned-for-fix`.

**`adopt --manifest M --decisions D [--apply]`**
- Deterministically merges each group's intake bib into `handbook/bib/handbook.bib`. Skip identical entries and append new ones.
- Key conflicts with different content are errors, unless `decisions.citation_aliases` or `bib_keep_canonical` covers them.
- Detect likely duplicate works under a different key (same DOI, ISBN or arXiv id, or the same normalized author+title+year) and report them as decisions-needed.

Symbol intakes:
- Repair quotes for unquoted `\(..,..\)` glyphs.
- Wrap a bare glyph in `\(...\)`.
- A blank macro becomes the inner TeX.
- A precedence outside `{number, meta, n/a, object, relation, infix}` becomes `n/a`, with the original appended to notes.
- Errors:
  - a numeric `PNN.k` scope or first_use;
  - a first_use that does not resolve exactly once on the route (use `symbol_registry`'s resolver);
  - a CSV parse failure.
- A named scope that is not yet bound gets a binding synthesized from its first_use: `{heading_of: <innermost heading label>, level}` plus the owned annex items' `annexitem` labels. Check `symbol_registry`'s region kinds.
- Run `symbol_registry.collision_check` (read it to learn its signature) on canonical plus incoming rows. Each new overlap must be covered by the decisions file (`overrides`, `row_edits`, `drop_rows`, `canonical_row_edits`, `extend_scopes`); otherwise it is reported as decisions-needed.
- Apply only when there are 0 errors and 0 unresolved decisions. Append rows to `handbook/registry/symbols.csv`, merge bindings into `handbook/registry/symbol-scopes.json`, and append bib records.
- Rewrite citation alias keys only inside cite commands in that group's own files.
- Re-validate by re-reading with `symbol_registry.read_rows` and running `collision_check`. On failure, restore the three canonical files from their in-memory originals.
- Set group status to `merged`. Keep the intake files.
- Port the logic from `tmp/edition-2026-coverage-map/prepare_oct3_batch5_intakes.py` and `tmp/edition-2026-coverage-map/batch7-integration/prepare_remaining_inventory.py`; read them first.
- `--return R --virtual-route` copies `handbook/` (excluding PDFs and build files) to `tmp/unit-builds/<stem>/tree`, applies the placement there, and runs adopt in dry-run mode against the copy. This is the author self-check.

**`check-delta --tag T | --init DIR | --stage NAME`**
- Runs `python -B tools/check.py --tree handbook` and normalizes the output: keep only lines starting with `  - `, strip `:<line>)` and line-number tokens, sort with C locale.
- Diffs against the stored normalized file for the previous stage or tag, under `tmp/integration/<name>/check-norm.txt`.
- Prints new and fixed counts per category.
- Exits 1 if there are new findings, excluding findings that mention only untracked paths not in the given manifest (`--manifest`).

**`scoped-build --snapshot DIR --parts 15,17`**
- Per part, generates a driver following the P15 pattern: book class, handbook, biblatex with the canonical bib, inherited-keys; `\setcounter{part}{ORD-1}`; for P8, `\input{parts/p08/source-anchors}` first; then `\input{parts/pNN}`, `\hbannexsetup`, the annex driver (`annex/p01-route`, `p05-route`, `p06-route` for P1/P5/P6, else `annex/pNN`), `\hbannexfinish` and `\printbibliography`.
- Builds each part in parallel in `DIR/scoped/pNN`, running from `DIR/handbook`.
- The gate is no TeX error.

**`build-summary LOG [--prev JSON]`**
- Records: page count, sorted unique undefined refs and citations, multiply-defined labels, Overfull count per file, Missing character lines, and biber WARN/ERROR lines from the `.blg`.
- With `--prev`, prints the new items and exits 1 on any new undefined ref or citation, multiply-defined label or missing character.

## 7. Selftests and verification commands

Each tool runs `python -B tools/<tool>.py --selftest`.

Read-only smoke tests on the real tree:
- `python -B tools/find_fused_spaces.py handbook/parts/p13` (expect hits).
- `python -B tools/held_sources.py build` (dry run; prints the summary).
- `python -B tools/ledger_patch.py check` (expect warnings and the I7 count; no crash).
- `python -B tools/ledger_patch.py show 52.8`.
- `python -B tools/waves.py packetize w02 --parts P1,P2,P15 --dry-run` (prints the summary only).
- `python -B tools/integrate_wave.py adopt --manifest spec/research/edition-2026-authoring-batch-intake-8.json --decisions <empty json>` (dry run). It should report decisions-needed overlapping the 6 known ones (≤ μ P dQ $ →) recorded in `tmp/edition-2026-coverage-map/batch7-integration/remaining-stage.json`.

## 8. One-off `tmp/edition-2026-coverage-map/migrate_numeric_scopes.py` (faithful numeric-scope migration)

Purpose: replace every numeric `PNN.k` / `PNN.k-PMM.j` / `PNN-PMM` scope and numeric `first_use` in
`handbook/registry/symbols.csv` with label-anchored or named scopes that cover EXACTLY the same reader regions,
so later chapter insertions cannot shift meanings. Policy: faithful rebinding only. Never narrow a scope because
a glyph happens to be used in a smaller region; narrowing is a separate, recorded decision.

- Meaning source: `tmp/edition-2026-coverage-map/batch7-integration/post-actual-five-numeric-baseline.json`
  (per-row chapter meaning captured when `sha256(symbols.csv)` = its `canonical_symbols_sha256`). The script MUST
  refuse (exit 1, write nothing) when the current `symbols.csv` hash differs, even in dry-run mode it must report it.
- Binding construction: port `propose_numeric_migrations` from `tmp/edition-2026-coverage-map/prepare_oct3_batch5_intakes.py`
  with its skip guard removed. Each binding covers the chapter body regions (anchor, or `heading_of` for `ch:`
  chapters) PLUS the annex items owned by results in those chapters (compressed to whole annex files only when the
  file is entirely owned), whole parts as their driver files. Rows sharing the same numeric scope string MUST receive
  the same binding (one binding per distinct numeric scope string).
- Ghost ordinals (P9.3–P9.8, P10.2–P10.9, P16.17–P16.18; capture `old_chapters` empty): use the legacy
  interpretation consistently for all rows of the same ordinal: P9.k = the k-th `\section` unit of the monolithic
  P9 chapter in route order, plus its owned annex items; P16.17/18 = the current chapters that held those units;
  for P10 ordinals beyond the chapter's sections use `tmp/edition-2026-coverage-map/ghost-ordinal-map.json` evidence
  but bind ALL rows of that ordinal to the same region set (union of the evidence regions plus owned annex items).
  Whole-chapter rows (P9.1, P9.2, P10.1) bind to the whole chapter plus owned annex items, not to a sub-section.
- Naming: single chapter `P17 <anchor-stem>`; several chapters in one part `P6 <first-stem> to <last-stem>`;
  cross-part `Parts 5–19 from <stem>` (never starting with `P<digit>`); legacy ghost units
  `P9 legacy unit <k> <stem>`.
- Also rewrite the six `symbol-scopes.json` overrides whose `broader_scope` is numeric.
- Edit CSV lines in place (line numbers unchanged). `--apply` writes symbols.csv and symbol-scopes.json atomically,
  LF, UTF-8 no BOM. Default is dry run, writing `tmp/numeric-migration/dry-run.json` with: rows rebound, bindings,
  rows still numeric (must be 0), `symbol_registry.read_rows` errors on the in-memory result (must be 0), and
  `collision_check` results; any collision that a faithful rebinding creates is listed as `decision_needed`
  (do not resolve by narrowing).
- `--selftest` with a small fixture (two parts, a ghost ordinal, an override, a hash-mismatch refusal).

## 9. Rulings for `tools/waves.py` verify (lead, 2026-10-03)

- **G1 concurrency.** Lanes run concurrently. A change since the snapshot is legitimate if the path is
  (a) in this packet's `owned_files` or `editable_hosts`, (b) in the `owned_files`/`editable_hosts` of any other
  packet of the same wave (union over `work/waves/<wave>/packets/*.json`), (c) under
  `spec/coverage/edition-2026/assessments/<wave>/`, `work/waves/<wave>/patches/` or `tmp/`. Only changes outside
  (a)–(c) are hard G1 violations. Cross-packet edits (this packet touching another packet's file) are detected by
  that other packet's own owned-file hash check (each packet's snapshot records its owned-file hashes and the author
  return reports final hashes); report them as findings naming both packets.
- **Snapshot integrity.** The lead takes the wave snapshot and commits it (`work/waves/<wave>/snapshots/`) in the
  wave-base commit before any author runs, and records the commit SHA in `work/waves/<wave>/args.json` as
  `base_sha`. `verify` loads the snapshot from git (`git show <base_sha>:<path>`), never from the working tree, and
  refuses (hard) if `base_sha` is missing. The frozen-file check (G2) compares against `git show <base_sha>:<file>`.
- **Stub phrases** must match across any whitespace (including line breaks) and inside comments-stripped text.

## 10. `tools/waves.py packetize` extension: accounting and unit-only packets (lead, 2026-10-03)

Invariant I7 (duty conservation over all 3,716 queue units / 21,367 components) means every wave must also
account rows and units that need no new writing. Extend `packetize` (keep all existing behaviour and checks):

- **Row selection** for the given parts: every row with status != authored_unreviewed (as now), PLUS every
  authored_unreviewed row that (a) has non-empty `unassessed_scope`, or (b) has any `reader_evidence` whose sha256
  differs from the current file, or (c) lacks component accounting: no evidence group covers all component ids
  of its facet units, where a group is the entries sharing one `assessment_ids` set (a first+confirm pair split
  per file, e.g. body and annex) and an entry without `assessment_ids` is its own group (amended 2026-10-04). Such AU-only packets get
  `"mode": "accounting"` (all sections AU at selection) — the workflow assesses them first and authors only if the
  assessment downgrades a section. Mixed clusters get `"mode": "author"`. Packets of only open rows: `"mode": "author"`.
- **Unit-only packets.** Queue units of these parts that link to no ledger row (no `source_facets` reference in
  any row; part taken from the unit's destination paths/`destination` part or `prerequisite_allocation_prefix`)
  form packets with `"sections": []`, `"units": [...]`, `"mode": "unit_accounting"`; owned files are the unit's
  proposed body/annex destination files when they do not exist yet (so an author can write them), otherwise none
  (existing destinations become editable_hosts if sole-owned in the wave, else read-only). Bin-pack up to 6 units.
  Their assessments write residual records to `spec/coverage/edition-2026/unit-residuals.jsonl` (via the lead) in
  the `missing_pieces` item schema plus `unit_id`.
- Every packet records `component_ids` (all required_components ids of its units) so assessors account each one.
- `--selftest` gains fixtures for an AU row with parked scope, an AU row with a stale hash, an AU row lacking
  component accounting, and an unlinked unit.
- The summary prints counts per mode and the worst-case agent count with the accounting packets included
  (accounting packets: 2 agents; author packets: 2*max_blocks+2 — one initial assessment block is added).

## 11. `tools/wave_proposals.py` — wave results + assessment files → ledger proposals and unit residuals

Input: `--wave wNN --results FILE` where FILE is the JSON the `tmor-authoring-wave` workflow returned (saved by the
lead to `work/waves/wNN/results-<n>.json`; shape: `{results:[{id, outcome, sections:[{section_id, status, gaps,
blocked, a, c}], units:[{unit_id, open_components:[{component_id, gap, kind}], assessment_id, confirm_assessment_id?}]}]}`),
and the assessment files under `spec/coverage/edition-2026/assessments/<wave>/` (schema coverage-assessment/1:
`assessor{family,model,role,context_id}`, `inputs.tex[{path,sha256}]`, `components[{component_id, verdict,
evidence[{path,line_start,line_end,label}], gap, blocker}]`, `duties[...]`).
Output (dry run by default; `--apply` writes): `work/waves/<wave>/proposals.jsonl` in the `ledger_patch.py apply`
proposal format (section 4), and appended records in `spec/coverage/edition-2026/unit-residuals.jsonl`.

Per section result (the latest assessment ids `a` = first, `c` = confirm when present):
- `original_row_sha256` from the live ledger row (sha256 of the exact line bytes); `reason`: "wave <wave> packet <id>".
- `append_reader_evidence`: from the FIRST assessment's covered components, one entry per (path) with
  `line_start=min`, `line_end=max` over that path's evidence, `components=[covered component ids in that path]`,
  `assessment_ids=[a, c?]`, `read_extent="coverage assessment <a>"`, and `anchor` = a real label in that file:
  the first `prefix:token` label occurring in the evidence `label` strings that is declared in the file
  (`\label{...}` or an environment's first argument), else the nearest label declared at or before `line_start`.
  Skip evidence paths that do not exist; never invent an anchor.
- status `authored_unreviewed` only when both `a` and `c` exist and both files have every component and duty
  verdict `covered` (else downgrade to `partial`): `set = {status, missing_pieces: [], unassessed_scope: []}`,
  `assessment_ids=[a, c]`.
- status `partial`/`missing`: `set.status`, `set.unassessed_scope=[]`, `set.missing_pieces` = dict items
  `{duty, component_ids, kind, blocker_ref, since}`: one per open gap (`kind:"writable"`; component ids taken from
  the first assessment's non-covered components whose gap text matches, else all non-covered ids) and one per blocked
  item (`kind` normalised to blocked_source|blocked_math|blocked_policy|lead_owned; `blocker_ref` = the ACQ id from
  `spec/coverage/edition-2026/acquisition-requests.jsonl` whose `units` include one of the section's facet units
  for blocked_source, else null). `assessment_ids=[a]`.
- Never touch immutable fields; strings must pass `find_fused_spaces` classes A–C (fix by inserting spaces).
Per unit result: for each component in the unit's assessment files: covered → a residual record
`{"unit_id","component_id","kind":"covered","assessment_ids":[first, confirm],"evidence":[...],"wave"}` ONLY when a
confirm assessment file exists for that unit with the component covered; otherwise `kind:"covered_unconfirmed"`.
Open components → `{"unit_id","component_id","kind":<writable|blocked_source|blocked_math|blocked_policy|lead_owned>,
"duty":<gap>,"blocker_ref","assessment_ids","wave","since"}`. Replace earlier records for the same (unit, component)
by appending a newer record (latest wins; keep history).
`--selftest` with fixtures (AU with a+c, partial with blocked_source + ACQ match, unit covered/unconfirmed/open).
The lead then runs `python -B tools/ledger_patch.py apply --proposals work/waves/<wave>/proposals.jsonl [--apply]`.

## 12. Lead rulings for `integrate_wave.py route` (2026-10-04)

- **Heading rule (ratified, supersedes section 6's "first heading differs" wording):** a placement is refused
  only when the new file's first heading would skip a level below the heading in force at the insertion point
  (e.g. a `\subsection` file directly under a `\chapter` with no `\section`). Heading-less annex files and a
  `\section` file after a `\chapter`-opening or heading-less sibling are accepted. The literal section-6 rule would
  refuse most legitimate placements.

## 13. Shared units and lanes (amended 2026-10-04)

A queue unit listed by several packets of one wave has one writer: the first author packet listing it (else
the first packet). Every other packet lists it under `readonly_units` (unit -> owner packet id) and does not
write its components (author rule A14); its assessor files a non-covered readonly component as
`lead_owned` "owned by <owner>" (assessor rule S10). Lanes therefore join packets only through shared
editable hosts and owned files, not through shared units. The post-routing keyed re-assessment judges every
section against the merged text.
