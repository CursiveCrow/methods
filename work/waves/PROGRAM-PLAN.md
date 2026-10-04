# Plan: finish authoring *The Methods of Reason* through orchestrated writing waves

## Context

**Live ledger.** Nine JSONL shards in `spec/coverage/edition-2026/current-fulfillment/`, one row per planned section:

| Status | Rows |
|---|---:|
| authored_unreviewed (AU) | 750 |
| partial | 1,213 |
| missing | 195 |
| unassessed | 317 |

**1,725 sections are open, in 261 of the 289 chapters.** The remaining work is authoring and integration, not polishing. Exploration found more owed work than those counts show:

- **Unlinked catalog units.** 1,278 of 3,716 queue units (`completion-work-queue.jsonl`, 21,367 components) link to no ledger row; 629 of them have content_state=missing. Counting rows only would narrow the target.
- **Ledger rows that overstate coverage.**
  - 292 AU rows have parked `unassessed_scope`.
  - 23 partial rows have no recorded duty.
  - 747 of 6,867 evidence hashes have drifted from their files.
- **Unintegrated backlog.**
  - Batch B8 (`spec/research/edition-2026-authoring-batch-intake-8.json`): 17 groups plus 5 Codex follow-on drafts.
  - Twelve routed groups await canonical merge, with 6 open glyph-overlap decisions (≤ μ P dQ $ →).
  - About 11 saved drafts are off-route, several written today (Weihrauch, Abelard, cardinal separations, topological model theory, P19 language and task analysis, P16 remedy, P19 number line, early medieval Latin).
  - 17 unclassified off-route files remain.
- **Fused-text defect.** Codex dropped spaces next to numbers and between words: "in1348", "Theorem4.13", "Date:3October2026". It appears in `.tex` files, notes and ledger strings.
- **Numeric symbol scopes drift.** 1,609 symbol rows use `PNN.k` scopes, which renumber whenever a chapter is inserted. 105 live errors in P17 already come from this, and 337 rows point at chapters that no longer exist.
- **The baseline is red and stale.**
  - `check.py --tree handbook` reports 75 hard failures and 503 findings.
  - symbols2tex is blocked, and `audit_tables` has a digest mismatch on the edited contract.
  - A retained, pinned file (`parts/p03/types-ultraproducts.tex`) was edited by a Codex citation rewrite.
  - The last full build was 8 Sep.
  - Nothing has been committed since 13 Aug: about 9,800 untracked files, about 3.7 GB.

**Governing rules** (`spec/EDITION-2026-CONTRACT.md`, `EDITION-2026-EXECUTION-PLAN.md`):
- All writing, corrections and integration finish before the consolidated three-role reviews.
- One lead owns the drivers and canonical records.
- At most 12 concurrent subagents.
- Authors never accept their own work, and partial stays partial.
- Each source presentation is an independently worded reconstruction, and distinct versions stay separate.

### Done for this plan

1. Each of the 2,475 rows is either:
   - AU with live, routed evidence, upgraded only by two cross-family assessments; or
   - open, with every remaining duty classified `blocked_source`, `blocked_math` or `blocked_policy` and a concrete reference.
2. Every component of all 3,716 queue units is covered or present as a classified residual (invariant I7).
3. Zero `writable` duties and zero `unassessed` rows remain.

Nothing is dropped, capped, rescoped or upgraded on an author's word. The consolidated reviews and publication gates follow afterwards (see the last section).

### User decisions (2026-10-03)

- **Checkpoint:** commit everything, including citations/ and source/.
- **Tree ownership:** Claude owns the worktree exclusively during runs. The Codex "root" session, which was integrating live today, must be paused first.
- **Acquisitions:** batch lists, approved asynchronously, with downloads only after approval. The waves never wait.
- **Autonomy:** waves run fully autonomously in dependency order, each ending in a commit and a report.
- **Hintikka and abelian categories:** `p15-hintikka` (§164.8) and `p10-abelian` (§148.2) stay off-route, kept in place and not retired. The 2011 final Hintikka and the 1964 Freyd original go on the acquisition list.
- **Access basis:** freely reachable copies are acceptable, including course pages, university sites and third-party hosts.
- **Shadow libraries:** the user allows them, but Claude will not search or download from them. Sources with no other free copy are listed as "needs user-supplied file". Files the user drops into `source/references/` are verified and unblock their sections.

**Defaults the lead applies unless you object at approval:**
- Revert the 3-line Codex edit to the pinned retained `parts/p03/types-ultraproducts.tex`.
- Re-pin `spec/provenance` to the current `EDITION-2026-CONTRACT.md`, whose additions record your 8–9 Sep directives, with a provenance note.
- Adopt the integration design's default resolutions for the 6 glyph overlaps.

**Scale:** about 2,700–4,200 agents and about a week of continuous running. That is well above the session's default workflow-size guideline of under 10 agents, which this task's scale requires. Approving this plan approves that scale.

## Models

> **Superseded 2026-10-03 by the user: every agent (authoring, assessment, tooling, fixes, verification) uses Opus 5.5 (`model: 'opus'`). No Codex, no Fable. Independent assessments are separate fresh Opus contexts (`first` + adversarial `confirm`) instead of cross-family.**

| Role | Model |
|---|---|
| Authoring (reader prose, proofs, hard fixes) | `fable`, effort high; max effort on redirects |
| First coverage assessment, census, mechanical fixes and triage | gpt-5.5 via `agentType: 'codex:codex-rescue'` ("read-only" in the prompt when applicable). A parse failure is re-run on opus. |
| Confirming upgrades, 1-in-20 audit sample, backlog readiness, acquisition verification, host patching, overlap decisions | `opus`, effort high |

Never Haiku.

## Step 0: quiesce, checkpoint, tools, baseline repair (lead; no workflow)

1. **Quiesce.** The user pauses Codex. Confirm that no codex, latexmk or pdflatex process is running, and that `git status --porcelain | wc -l` is stable across two minutes.
2. **Checkpoint commit** on `phase4-codex`, committing everything as decided:
   - Run `git lfs track` on each untracked file over 5 MB (about 85 files plus the citations/source PDFs), so the commit stays workable. There is no remote; LFS is installed.
   - `git add -A`, then `git add -f tmp/edition-2026-coverage-map` (60 MB of integration helpers; the rest of `tmp/`, 8 GB, stays ignored).
   - Commit and tag `w00-checkpoint`.
3. **Write the tools.** All are lead-owned. Each has one `--selftest`, writes LF via `newline="\n"`, and lives in a checked-in `.py` file, never in an inline heredoc, because the Bash tool mangles `\\`.
   - **`tools/find_fused_spaces.py`.** A masking detector that blanks comments, math, label/ref/cite/url/input arguments, status arguments and control sequences. It has classes A–C, which it auto-fixes, and class D (CamelCase), which needs review. `--md` handles notes, and pinned and restoration files are skipped.
   - **`tools/held_sources.py`.** Merges `citations/manifest.json`, `source/references/*/manifest.json` and the queue's artifact fields into `spec/coverage/edition-2026/held-sources.json`: path, sha256, version, printed pages, extent-verified flag, access basis.
   - **`tools/waves.py`.** Author-side and wave tooling:
     - `packetize`;
     - `snapshot` / `verify`: ownership hash manifest plus guards G1–G16 as deltas against the snapshot;
     - `unit-compile`: a scratch driver in `tmp/unit-builds/<stem>/`, run from `handbook/` with `pdflatex -disable-installer`, biber, then two passes; the canonical and intake bibs are both added;
     - `report`.
   - **`tools/integrate_wave.py`.** Lead integration:
     - `collect`;
     - `route` / `unroute`: insertions need an exactly-once anchor and must not land inside a driver's `\AddToHook…\RemoveFromHook` label bracket; the heading level must match the host;
     - `adopt`: a deterministic bib/symbol merge that reuses `symbol_registry.read_rows` and `collision_check` and ports the helpers from `prepare_oct3_batch5_intakes.py` and `prepare_remaining_inventory.py`; a decisions JSON covers judgment calls; it rejects `PNN.k` scopes; intakes are kept after adoption;
     - `check-delta`: normalized check.py findings compared against the previous tag;
     - `scoped-build`, `build-summary`.
   - **`tools/ledger_patch.py`.** Ledger edits and checks:
     - `apply`: pinned to `original_row_sha256`; edits only status, append-only reader_evidence, missing_pieces, unassessed_scope and observed_utc; writes `fulfillment_revision` with `previous_observation`; enforces the two-family vote rule for upgrades; has no bulk path; refreshes receipts.
     - `check`: invariants I1–I11, including I7 duty conservation over all 3,716 units via `unit-residuals.jsonl`.
     - `report`, `show <section>`.
   - **`check.py`:** add `fused-number` and `stub-marker` categories.
4. **Baseline repair.** Each item is its own commit, and `check-delta` may show only fixes.
   - a. Revert the types-ultraproducts edit and re-pin the contract digest (defaults above).
   - b. **One-time numeric-scope migration:** `tmp/edition-2026-coverage-map/migrate_numeric_scopes.py`, based on `propose_numeric_migrations` with its skip guard removed.
     - It rebinds about 1,248 rows into roughly 163 named, label-anchored scopes, and rewrites the 6 numeric override `broader_scope`s.
     - One Fable agent maps the 16 dead ordinals (P9.3–9.8, P10.2–10.9, P16.17–18) and re-scopes the monolithic P9.1, P9.2 and P10.1 rows.
     - Verification: `symbols2tex` exits 0, `symbols-csv` goes from 105 to 0, and no other category changes. The `≤` canonical-ordering duplicate is inspected first.
   - c. **Fused-space repair:** auto-fix classes A–C; Codex reviews class D per file. `git diff --ignore-all-space --exit-code` proves the change is whitespace only. Notes and ledger editable fields are repaired the same way, then receipts are refreshed.
   - d. **Backlog wave A:** adopt the 12 routed groups (B7: p06-iterations, KLM, recombination-models, medieval-latin, savage; B8: recombination-iteration, erotetic-search, operational-adequacy, identification, proper-iteration, computable-analysis, properness-parameters).
     - Port the earlier root row judgments.
     - Repair the p04 intake CSV overflow.
     - Record the 6 overlap decisions. Defaults: typed overrides for ≤, $ and →; narrow the μ and P rows; reuse `def:p18-ei-setting` for dQ.
   - e. Regenerate `symbols2tex`, `audit_tables` and `build_named_theorem_index`. Run a full build on a `git archive` snapshot in `tmp/builds/w00` (MiKTeX, `latexmk -pdf`), fix it to green, and tag `w00-clean`. That tag is the delta baseline.

## W0 — `tmor-backlog-integrate` (backlog wave B)

Items:
- 9 B8 saved-off-route groups;
- the 2 B7 frozen groups (p16 remedy, p19 number line);
- 4 follow-on drafts (Weihrauch, topological model theory, task analysis, HSP);
- `p09-recombination-computation`, left mid-authoring;
- the 17 unclassified off-route files.

Hintikka and Abelian are excluded.

Steps:
1. An opus readiness check per item: backlinks, unit compile, filtered check output, overlap with routed text. The verdict is route, fix or continue-authoring.
2. "Fix" items get one Fable block on their own files. "Continue-authoring" items become carry-over packets at the front of their part's wave.
3. The 17 unclassified files are classified as route, keep or propose-retire. Retirements are listed for the user, and nothing is moved without approval; `annex/p01.tex` and `parts/p14/master-tables.tex` stay, because tools reference them.
4. The lead runs `integrate_wave` collect → route → adopt → views → check-delta → scoped builds → full build → fix loop. Units needing content judgment are unrouted and go to the next wave.
5. Commit, then report.

## W1 — `tmor-census`

1. **Source census.** Codex shards cover about 694 source ids plus the unnamed presentations: held path, sha, identity, version, extent and a verdict. This refreshes the frozen Sept-9 `source_state` and feeds `held-sources.json`.
2. **Acquisition scouting.** Opus searches publisher OA, arXiv, author pages, repositories, course pages and university hosts. It never downloads and never uses shadow libraries. Entries go into `spec/coverage/edition-2026/acquisition-requests.jsonl` using the integrity schema; identity must be agreed by both opus and Codex. Entries with no copy are marked "needs user-supplied file".
3. **Reassessment.** Codex assesses first; an opus confirm is required for any upgrade. Order:
   1. the 292 parked-scope AU rows;
   2. the 23 empty-duty partial rows;
   3. the roughly 50 AU-only facets;
   4. rows with drifted hashes;
   5. the 317 unassessed rows;
   6. rows that today's drafts cover.

   The 1,278 unlinked units are mapped to destinations, with residuals in `unit-residuals.jsonl`.
4. **Outputs:**
   - ledger patches, applied by the lead;
   - acquisition list r1, shown to the user;
   - the true writable versus blocked size, which sets the W2–W8 sizing.

## W2–W8 — `tmor-authoring-wave`, in dependency order

| Wave | Parts | Approx. open sections |
|---|---|---:|
| W2 | P1, P2, P15 | 205 |
| W3 | P3, P16, P17 | 212 |
| W4 | P4, P5 | 212 |
| W5 | P6, P7 | 238 |
| W6 | P8, P10, P18 | 295 |
| W7 | P9, P19 | 254 |
| W8 | P11, P12, P13 | 298 |

The final counts come from W1.

### Packetize (`waves.py packetize wNN`)

1. **Cluster** each chapter's open sections by shared queue unit. Bin-pack into packets of at most 4 sections or about 8 components; `max_blocks = min(4, 1 + ceil(components/3))`.
2. **Source gate.** Fully blocked packets spend no agents and go straight to blocker records.
3. **Ownership.**
   - New files are owned by construction: body, annex, `bib/intake-pNN-<slug>.bib`, `registry/symbols-intake-pNN-<slug>.csv`, the `spec/research/…` note, and a `…-return.json` with placement and proposed decisions.
   - An existing host may be edited only if it is not a driver, restoration capture, pinned retained file or canonical file, and no other lane in the wave touches it.
   - Any other change becomes a patch request under `work/waves/wNN/patches/`.
   - Packets that share an editable host or unit form one serial lane.
4. **Labels and headings.**
   - Each unit gets a `label_tag` (for example `thm:p17-sg-…`) and an insertion anchor.
   - The heading follows the host: `\chapter` in flat P11/P13/P15–P19 lists, `\section` for supplements and section hosts, `\subsection` in the P9, P10 and p04-frontiers hosts.
   - Every new file opens with a tag such as `%% toc: P4 52 52.8,52.9`, so the final reordering is mechanical.
5. **Cross-links.** Packets may only `\cref` labels that already exist or that they define. Anything else becomes a cross-link request.

### Per packet: loop over blocks

1. **Fable author block** (about 45 minutes). The note's `## Continuation` section is saved at about 15 and about 45 minutes. The prompt includes, verbatim, the integrity clauses A1–A12:
   - account for every component_id;
   - no narrowing language;
   - source-specific text only from a held file opened in this session;
   - only locators seen in the source;
   - own words, at most 10 consecutive source words outside a quotation;
   - every owed proof step in the annex;
   - spaces before numbers;
   - check the EXISTING list first;
   - no workflow language in reader text;
   - the empirical fields;
   - no invented systems;
   - owned files only, with no driver, git-write or `main.tex` build commands.

   The author self-checks with `waves.py unit-compile`, filtered check.py output and the fused-space detector.
2. **`waves.py verify`.** Guards G1–G16 run as deltas: ownership/hash manifest, frozen files, annex pairing, labels, bib keys, locator page range, fused numbers, stub markers, unit compile, new macros, balanced environments, copied-prose runs against the held text layer (pdftotext/PyMuPDF are installed), workflow language, encoding. A hard stop quarantines the return and restores the files from the snapshot.
3. **Assessment.**
   - Codex assesses first, and opus confirms any upgrade.
   - Assessors see the components (description, success and failure conditions), the current duties, the hash-pinned LaTeX with line numbers and the held sources. They do not see author notes or claims.
   - Every cited line range and label is validated mechanically; an invalid citation voids the assessment.
   - An upgrade requires both families to say "covered" for every component, plus routed evidence. A downgrade needs one vote. A disagreement keeps the row partial, with the dissent recorded as a duty.
   - A random 1-in-20 sample of upgrades goes to a fresh opus audit; a failure re-runs that wave's upgrades.
   - Assessment files are written to `spec/coverage/edition-2026/assessments/wNN/`.
4. **Progress metric:** components verified plus 2 × sections upgraded.
5. **Escalation.**
   - Two blocks with no progress: split into one child per section.
   - A child that stalls: redirect at max effort to the exact missing step.
   - Still no progress: record `nonprogress_blocked` with the exact gap.
   - Reaching `max_blocks` or 940 agents per workflow: the remainder becomes logged carry-over at the front of the next wave. Nothing is dropped silently.

**Concurrency.** A semaphore holds each workflow to 12 concurrent agents, and only one workflow runs at a time. Results returned to the main loop are compact (ids, statuses, paths); details live in files.

### Wave-end integration (lead, autonomous)

1. Ownership audit against the wave's base commit; violations are restored.
2. `integrate_wave collect` → `route` → host patches (one opus agent per host; hosts are disjoint, so these run in parallel) → cross-links → `adopt` (decisions JSON) → regenerate views → `check-delta` with zero new findings → scoped part builds → full build on a `git archive` snapshot.
3. Fix loop, at most 2 rounds (Codex for mechanical errors, Fable for content); anything still failing is unrouted to the next wave.
4. `ledger_patch.py apply` then `check`.
5. Records: batch manifest `…-intake-N.json` (N from 9), `authoring-progress.json` key, `spec/verification/edition-2026-wave-log.md`.
6. Commit with explicit paths and tag `wNN`.
7. Acquisition list update. Downloads happen only for entries the user has approved in chat, each followed by identity, version and page-sequence checks and a hash.
8. `output/manuscript-status/wave-NN-report.md`, generated by `ledger_patch.py report` (downgrades first, no "done" wording, blockers by kind), plus a two-line chat summary.

## W9 deferred / W10 apparatus and ordering

- **W9** reruns the authoring wave on packets unblocked by approved or user-supplied sources, plus carry-over and split remainders. It repeats as approvals arrive.
- **W10** covers:
  - **P14 apparatus:** the 11 open sections and the lookup obligations; subject and task finders; theorem, method, symbol and name indexes from content; glossary.
  - **Reorder** to the approved 289-chapter contents using the `%% toc:` tags. Python proposes the order, opus checks it, Python applies it. Restoration chapters move only through recorded layout-only relocation.
  - **Final checks:** `ledger_patch.py check` with every invariant hard (I3–I5, I7, I10), a strict check, and a clean full build of `handbook/main.pdf`.

## Verification

- **Per tool:** `--selftest`. Run `adopt` against the backlog A inputs first; it must reproduce the 6 known overlaps from `remaining-stage.json`.
- **Per block:** guards G1–G16, and line-range validation of every assessment.
- **Per wave:**
  - `check-delta`: zero new findings;
  - `ledger_patch.py check` I1–I11;
  - full-build delta: no new undefined references or citations, multiply-defined labels or missing characters;
  - the measured audit-sample false-upgrade rate;
  - a tagged commit and a generated report.
- **End:** zero writable duties, zero unassessed rows, I7 over all 3,716 units, a strict check, and a clean build.

## After this plan (still owed under the contract)

- Consolidated three-fresh-context reviews (source fidelity, topic specialist, adversarial publication) of the frozen units.
- Batch repair and recheck.
- Formal admission.
- Inspection of every page.
- Terminal readiness at zero residuals.
- Your final acceptance.

These are a separate plan, started once "done" above holds. This plan does not claim them.
