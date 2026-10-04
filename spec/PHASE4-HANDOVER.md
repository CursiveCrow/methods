# Phase 4 handover — migration campaign

> **SUPERSEDED CONTENT POLICY (2026-08-11).** Read
> `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md` before using this work order.
> The user's current instruction requires a full, accurate compendium and
> revokes every authorization below to compress, abridge, normalize, select,
> hybridize, retire, or omit content. This file remains useful only as a
> historical inventory of source ranges, registers, and intended artifacts.
> Where it conflicts with the full-compendium contract, the contract controls.

**Written 2026-08-10 after the first Phase-4 attempt aborted.** This document is
a self-contained work order: a session with no prior context can execute Phase 4
from it. Read it start to finish before touching anything.

---

## 1. What this campaign is

The user is building a comprehensive CRC-*Handbook-of-Chemistry-and-Physics*-style
reference work for logic. A 14,780-line dependency-ordered manuscript
(`source/formal-logic-reference.tex`) was audited, repaired, and demoted to
**verified source material**; it is not printed. The printed work is the
14-part handbook under `handbook/`, built by compressing that source into
lookup entries plus a proof annex, and by adding four domains of new content.

Full specification: **`spec/gap-analysis.pdf`** (52 pp). Its tables are generated
from four CSV registers in `spec/registers/`, which are the single source of
truth for all work. The approved campaign plan lives at
`C:\Users\Crow\.claude\plans\c-users-crow-downloads-formal-logic-ref-vivid-canyon.md`.

**The three fixed decisions** (the user's; they define "done" and are not
renegotiable):

1. Comprehensiveness spans four domains: deep mathematical logic, philosophical
   logic, logic in computer science, algebraic & categorical logic.
2. Restructure toward a pure handbook — topical entries and tables, proofs
   compressed into an annex.
3. The gap report was the first deliverable; the writing campaign runs against it.

## 2. Where the campaign stands (verified 2026-08-10)

Phases 0–3 are complete and committed. `main` is at **`f7554c7`**, clean.

| Fact | Value |
|---|---|
| Repo | `C:\Users\Crow\Downloads\formal-logic-handbook` |
| Tag `v1.0-audit` (676d170) | the audited manuscript; **all line references in the registers mean this revision** |
| Tag `v1.1-verified` (a2cf370) | the repaired manuscript — 37 FIX-SOURCE defects executed + adversarially verified. **This is what you migrate from.** |
| Source build | 251 pp, `check.py --tree source` passes |
| Handbook build | 138 pp, `check.py --tree handbook --strict` passes, 40 tracked stubs |
| Registers | 88 defects · 141 depth gaps · 185 new-content · 201 apparatus |
| Binding contract | `handbook/CONVENTIONS.md` |
| Pilot exemplar | `handbook/parts/p05/` + `handbook/annex/p05.tex` (the migrated incompleteness chapters — **copy this style**) |

Re-verify in under a minute before starting:

```bash
cd /c/Users/Crow/Downloads/formal-logic-handbook && git log --oneline | head -3 && git status --short && python tools/check.py --tree handbook --strict && python tools/check.py --tree source
```

## 3. Why the previous attempt failed, and what that implies

A 26-agent workflow was launched and **every agent died on a Fable 5 usage
limit**; 0 of 26 completed. Nothing reached `main`. This was a capacity failure,
not a design failure — the wave/verify structure below is sound and should be
reused.

**Implications for the executing session:**

- The user has switched the session model to **Opus 5**. Run the campaign on a
  model tier you actually have headroom for, and prefer **fewer concurrent
  agents** (see §8) so a limit hit costs one visit, not twenty-six.
- **Land work incrementally.** The failed run had wave-level commits, so a
  mid-wave death lost everything. Commit after *each verified part-visit*
  instead (§7 step 8). A part-visit is the unit of durable progress.
- Do not launch a multi-agent workflow unless the user has opted in
  (`ultracode` is currently off). Either ask, or execute visits sequentially
  yourself — both are fine; §8 covers each.

## 4. Salvage from the aborted run

Branch **`phase4-salvage`** holds three files written before the agents died:
`handbook/frontmatter.tex` (235 lines), `handbook/parts/p02/propositional-syntax-semantics.tex`
(689 lines), `handbook/registry/calculi/tableaux-cpl.tex` (16 lines).

They look complete but are **unverified and unintegrated** (no annex files, no
drivers, no register reconciliation). Treat them as a draft, not as progress:
either run the normal §6 verification over them before adopting, or ignore them
and write fresh. Never merge them unverified — the campaign's whole value is
that nothing enters the handbook unchecked.

## 5. Non-negotiables

These come from the contract and the standards rulings; violating them silently
is the one unrecoverable failure mode.

1. **Never edit `source/`.** It is the verified substrate, frozen at
   `v1.1-verified`.
2. **Status may never upgrade.** A v1.1 *complete proof* becomes
   `proved=annex:…`; a *proof sketch* becomes `sketched=annex:…` with
   `\sketchnote` enumerating the omissions; a *cited theorem* becomes
   `cited=<bibkey>` with no annex item. If compression means a proof no longer
   fully supports its label, downgrade the label — never the reverse.
3. **No proofs in the body.** `parts/**` contains statements; `annex/**`
   contains proofs. The check suite enforces this.
4. **Rules live only in `registry/calculi/`.** Body chapters reference sheets;
   they never re-display rules. Every `\hbrule` carries all five arguments,
   side conditions included.
5. **Shared-file rule** (only matters if visits run concurrently): a visit never
   edits `main.tex`, `handbook.sty`, `bib/handbook.bib`, or
   `registry/symbols.csv`. New bib entries go to `bib/intake-pNN.bib`; new
   symbols to `registry/symbols-intake-pNN.csv`; the wave/global finalizer
   merges and deletes intakes.
6. **Labels** carry the part prefix: `thm:p06-zorn`, `def:p03-ef-game`.
7. **Glyph rulings**: `|·|` is cardinality only (domains are `\dom M`); `≡` is
   elementary equivalence only; formula equivalence is `⇔`; the definitional
   sign is `:≡`; one registered forcing macro. Translate v1.1 notation as you
   migrate.
8. **Honesty in the registers.** A row flips to `done` only when its deliverable
   genuinely exists at its treatment ceiling. Stubbed or partial stays `open`.

## 6. Verification requirement (per visit)

Every part-visit is followed by an adversarial check — by a second agent if you
are delegating, by a deliberate second pass if you are not. Assume the migration
is wrong until shown otherwise:

- **Fidelity**: sample ≥12 migrated entries (including every Tier-1 method
  entry) statement-by-statement against v1.1 — hypotheses exact, statuses not
  upgraded, Phase-2 repairs preserved in substance, compression did not delete
  load-bearing steps, sketches enumerate omissions.
- **Depth fill**: every `must`/`should` row targeting the part is either filled
  at its ceiling — *check the mathematics of new statements, especially
  hypotheses* — or carries an explicit `\hbstub` naming the row id. No silent
  absences. New content cites real sources; no fabricated bibliography data.
- **Conventions**: label prefixes, status grammar, intake discipline, glyph
  rulings, `\index` tags at definition sites.
- **Mechanical**: scratch-compile the part, then `python tools/check.py --tree
  handbook` (findings in this part's files only, mid-wave).

The verifier fixes what it finds and records each correction. Precedent: the
Phase-3 verifier caught a dropped `x ∉ Var(t)` proviso that would have silently
broken a repaired result; the Phase-2 verifiers caught 21 defects in designs
that had already been reviewed once.

## 7. The work: eleven part-visits

Phase 4 covers **Parts 1–8 and 12** (Parts 9–11, 13 are Phase-5 new-domain work;
Part 14 is Phase 6). Depth rows are in `spec/registers/depth-gaps.csv` — filter
by `target_home`. Treatment ceilings: **E** full entry · **T** table rows · **S**
statement + status + citation · **P** pointer sentence.

Row counts by target part (must/should/could): P2 13/9/2 · P3 2/9/2 ·
P4 3/4/1 · P5 3/4/1 · P6 11/8/0 · P7 4/5/1 · P8 13/17/5 · P12 3/6/2.
Fill `must` and `should`; stub each `could` with its row id.

### Per-visit procedure

1. Read `handbook/CONVENTIONS.md`, the pilot part, and your depth rows.
2. Locate your source chapters in `source/formal-logic-reference.tex` (v1.1) by
   title; read them fully.
3. Write body chapter files: entries with exact hypotheses and status specs.
4. Write annex fragments: Tier-1 method proofs (compressed) for the named
   methods; Tier-2 compressed proofs at 40–60% of source length; nothing for
   cited theorems.
5. Fill depth rows at their ceilings; stub the rest with row ids.
6. Build the part's tables/figures from `apparatus.csv` rows with `phase=4`.
7. Scratch-compile (a driver in the session scratchpad that loads
   `handbook.sty` and your files) — never `main.tex` if siblings are running.
8. Verify (§6), then **commit this visit** with its entry counts and depth rows
   in the message.

### Wave 1 — foundations and classical logic

**P1 · Notation, Symbols, Conventions + front matter.**
Files: `parts/p01.tex`, `parts/p01/*.tex`, `handbook/frontmatter.tex`.
Source: v1.1 Part I ("Sets, Relations, Functions, Cardinality"; "Finite Strings,
Induction, Recursion") compressed ~4:1 into reference tables — CSB and Cantor
keep annex proofs, transfinite recursion stays cited; the front-matter policies
(Preface, terminology policy, evidence ladder) and the usable core of "Levels,
Objects, and Consequence" and "Writing Formal Definitions and Proofs" become
`frontmatter.tex` plus a conventions chapter (the error-taxonomy table survives).
Specifics: `\input{generated/symbols-tables}` with framing prose; precedence
chapter from the registry's precedence column with worked disambiguations; the
16-binary-connectives table; notation-variants-across-the-literature table;
mathematical-preliminaries register.

**P2a · 2.1 Propositional.** Files: `parts/p02/propositional*.tex`,
`annex/p02/propositional*.tex`. (Do not write `parts/p02.tex` — the finalizer
assembles it from the three P2 visits.)
Source: v1.1 Part II entire, including the Phase-2 repairs (CNF induction R-011,
discharge licensing R-013, LK completeness scope R-014, Davis–Putnam
attribution R-023).
Depth: Post's five maximal clones + functional completeness (E; Post's criterion
stated, clone table, Sheffer/NOR), duality, Hilbert-CPL (`sheet:hilbert-cpl`
exists) + deduction theorem with annex proof, propositional tableaux (new sheet
`registry/calculi/tableaux-cpl.tex` — salvage draft exists) + adequacy (S),
decidability and SAT NP/coNP statements, interpolation (S), Tseitin
forward-link, equivalence-laws master table, Post's-lattice figure (tikz).

**P2b · 2.2 First-order.** Files: `parts/p02/first-order*.tex`,
`annex/p02/first-order*.tex`.
Source: v1.1 Part III entire — Henkin construction is a **Tier-1 method entry**;
preserve the R-009 transfinite Lindenbaum, the R-027 countable choice-free
completeness corollary, the R-007/R-008 prenex–Skolem chain, R-024
conservativity, R-026 degarbled compactness.
Depth: Hilbert-FOL + deduction theorem, first-order tableaux (new sheet),
**Herbrand's theorem proper** (E: universe, structure, validity form),
Craig/Beth *statements* (cited; proofs live in P7), Robinson joint consistency
(S), decidable-fragments table with complexity column (monadic, FO², guarded,
Bernays–Schönfinkel, Presburger), many-sorted (S), clausal-form pipeline table,
consolidated equality metatheory.

**P2c · 2.3 Higher-order + 2.4 Variants.** Files: `parts/p02/higher-order.tex`,
`parts/p02/variants.tex`, `annex/p02/higher-order.tex`.
Source: v1.1 Part IX entire (full vs Henkin semantics, the
categoricity/compactness-failure/non-enumerability trio with the R-031/R-033
repairs, the many-sorted translation as Tier-2 annex, simple type theory).
Depth: a **displayed second-order calculus** (comprehension + choice schemas;
new sheet `registry/calculi/sol.tex`; Henkin completeness cited), analytical
hierarchy pointer to P4, free logic (S: positive/negative/neutral + definite
descriptions), infinitary L_{ω₁ω} (S/P), generalized quantifiers (P),
full-vs-Henkin comparison table.

### Wave 2 — the mathematical core

**P3 · Model Theory.** Source: v1.1 Part IV entire (Tarski–Vaught, diagrams,
types/saturation with R-028/R-029, ultraproducts with Łoś, QE and categoricity
with R-015/R-016, the R-036 ultrafilter promotion). Łoś and back-and-forth are
Tier-1 method entries.
Depth: **EF games** (E: game, theorem, inexpressibility applications),
preservation-theorems table (Łoś–Tarski, Chang–Łoś–Suszko), Keisler–Shelah (S),
compactness-via-ultraproducts (S, annex derivation from Łoś), prime/atomic
models with Ryll-Nardzewski restated (S), Lindström moved here (cited),
stability/NIP/o-minimality overview table, 0–1 law statement (S),
**QE catalog table** (DLO, ACF, RCF, Presburger, Th(ℕ,S), atomless BA ×
QE/completeness/decidability/complexity) — a flagship table.

**P4 · Computability and Complexity.** Source: v1.1 Part V entire — preserve the
G2 interdependencies exactly (R-002 bounded-verification apparatus, R-004 jump,
R-005 enumeration theorem, R-006 prefix-form equivalence, R-035 definition).
Depth: **μ-recursion + TM-equivalence theorem** (E), Church–Turing entry,
**Turing degrees + jump + Post's problem + finite injury** (priority method as
`hbmethod` with sketched annex), c.e.-set structure (S), Kolmogorov complexity
(S), analytical hierarchy (T/S), **complexity as a subject** (class-ladder
table, hierarchy theorems, Cook–Levin, QBF PSPACE-completeness, logic-relevant
completeness catalog), descriptive-complexity pointer; hierarchy figures.

**P5d · Part 5 depth completion** (body already migrated by the pilot; add
entries only). Depth: nonstandard-model structure (S: order type ω + ℤ·ℚ,
overspill), **Σ₁-completeness as a named theorem** (S + annex sketch — implicit
in v1.1), interpretability (S), Tennenbaum (S cited). Leave the four Phase-5
stub chapters in place. Keep `audit_tables.py` output regenerable.

**P6 · Set Theory** (heaviest depth fill: 11 must). Source: v1.1 Part VII entire
— **preserve the R-001 honest CH treatment in full** (the cited Boolean-valued
import, the ctm presentation as pedagogy, the syntactic nonderivability
argument). Forcing is a Tier-1 method entry.
Depth: **ordinal arithmetic + Cantor normal form** (E — absent book-wide, and
P7's ordinal analysis depends on it), cardinal arithmetic/cofinality/König (E),
**AC equivalents including Zorn** (E — Zorn finally enters the book),
clubs/stationary/Fodor (S), Δ-system + Ramsey (S), combinatorial-principles
table (◊, □, MA), **large cardinals** with the consistency-strength ladder table
and figure (connect to the ctm hypothesis), reflection/absoluteness/condensation
(S), descriptive set theory + determinacy (S/T), Boolean-valued and iterated
forcing pointers, independence-catalog table.

**P7 · Proof Theory and λ-Calculi.** Source: v1.1 Part VIII entire — body
references registry sheets rather than re-displaying rules; cut elimination with
the R-012 mix apparatus and rest-on-sketch corollaries is a Tier-1 method entry;
the honest internal-proof-boundary paragraphs become `proofboundary`
environments.
**Resolve the flagged Mix-homing question**: v1.1 states mix for the
defined-negation calculus the cut-elimination chapter actually uses, but the
Phase-3 registry homed Mix on `sheet:lk`/`sheet:lk-eq`. Either add Mix rows to
`sheet:lk-defneg` (and `lj` if needed) or document on `sheet:lk` why the homing
stands. Decide, implement, record in the file comments.
Depth: **untyped λ-calculus + Church–Rosser** (E; annex sketch via
Tait–Martin-Löf parallel reduction), System F (S), MLTT/CIC overview (S),
midsequent/Herbrand via cut elimination (S), **Maehara interpolation** (S/E),
proof complexity (S: Frege systems, resolution lower bounds), ordinal-analysis
calibration table (needs P6's ordinal arithmetic), structural-rules table,
Curry–Howard correspondence table.

### Wave 3 — entry cards and automation

**P8 · Nonclassical cores** (13 must / 17 should — the largest visit; consider
splitting by chapter). This is the **first real exercise of the `systementry`
card machinery**; if `handbook.sty` has bugs in the card or `.hbentry` harvest
path, record them precisely for the finalizer.
Source: v1.1 Part X entire with Phase-2 repairs (R-040 ⊥-priority in the
Gödel–Gentzen recursion, R-041 prime theories, R-037 tableau honesty).
Cards for the systems v1.1 has: IPL (8.1); K, T, S4, S5 (8.2); LTL and
S5ₙ-epistemic with the common-knowledge extension and its honest
no-proof-theory warning (8.3); K3, LP (8.5); relevance/Routley–Meyer (preserve
the internal-proof-boundary discipline) and IMLL + exponentials (8.6). Every
card: full field set, `\entrycalculus` pointing at a real sheet (extract new
sheets `hilbert-ltl`, `hilbert-s5n`, `tableaux-matrix`, `imll` from v1.1),
statuses never above v1.1's labels. **The modal completeness title-overclaim
dies here**: correspondence claims move into the correspondence table with their
own statuses.
Depth: canonical-model method entry (`hbmethod` + annex sketch — v1.1 only
*names* it), filtration/FMP/decidability for K/T/S4/S5 (S),
**frame-correspondence table** (axiom ↔ condition ↔ algebra; Sahlqvist row),
bisimulation + standard translation (S), IPL disjunction *and* existence
properties, Glivenko and Gödel–Gentzen entries citing the primaries
(`Glivenko1929`, `Godel1933`), K3/LP facts registered (K3 has no tautologies;
LP's tautologies are the classical ones; duality), substructural family-map
figure. Chapters 8.4 and 8.7 are Phase-5 stubs naming their N-rows.

**P12 · Automation and Mechanization cores.** Source: v1.1 Part XI entire —
construction methods as `hbmethod` entries; DPLL with its repaired correctness
proof (Tier-2 annex); resolution sheet extracted **with the renaming-apart side
condition on the rule display**; SMT/SMT-LIB/TPTP entries; the mechanization
chapter (kernel, elaboration, tactic, trusted base, propositions-as-types
example); the writing/typesetting and workflow chapters compress to one
reference chapter of method boxes plus the release-audit checklist as a table.
Depth: complexity-and-practical-status entries with real statements (SAT
NP-complete cited `Cook1971` with the P-vs-NP framing corrected; FOL validity
undecidable cited `Church1936`+`Turing1937`), 2-SAT/Horn tractability (S),
prover-landscape table, LCF architecture + de Bruijn criterion (S),
landmark-formalizations table. CDCL, Martelli–Montanari, superposition-as-a-
calculus, tableau methods, and model checking are Phase-5 stubs naming their
N-rows.

## 8. Orchestration options

**Option A — reuse the workflow script** (needs the user's opt-in, since
ultracode is off). The full orchestration survives on disk:

```
C:\Users\Crow\.claude\projects\C--Users-Crow-Downloads-formal-logic-handbook\8318ebbc-8b55-4a6a-acff-5aafa2e17aa4\workflows\scripts\phase4-migration-wf_d2cad78d-b03.js
```

Invoke with `Workflow({scriptPath: "…phase4-migration-wf_d2cad78d-b03.js"})`.
**Edit it first**: (a) reduce wave width — run 2–3 visits concurrently, not
5; (b) move commits from wave-level to visit-level so a limit hit costs one
visit; (c) split the P8 visit by chapter. Resuming the old run id gains nothing
(0 agents completed).

**Option B — sequential execution by the main session.** Work one part-visit at
a time in the order above, committing each. Slower in wall-clock, but every
commit is durable and you keep full control of fidelity. This is the right
choice if agent capacity is uncertain.

Either way the order matters only in two places: P6 before P7 (ordinal
arithmetic), and P2a/b/c before the `parts/p02.tex` driver is assembled.

## 9. Wave / batch finalization

After each group of visits (or after every visit, in Option B):

1. **Merge intakes**: `bib/intake-*.bib` → `bib/handbook.bib` (dedupe by key,
   prefer richer entries), `registry/symbols-intake-*.csv` →
   `registry/symbols.csv` (resolve glyph collisions by scoping); delete intakes;
   `python tools/symbols2tex.py` must exit 0.
2. **Assemble drivers**: each `parts/pNN.tex` inputs its chapter files and ends
   with `\input{generated/audit-pNN}`; each `annex/pNN.tex` inputs its
   fragments; wire `frontmatter.tex` into `main.tex` once it exists.
3. **Regenerate**: `python tools/audit_tables.py`, `python tools/symbols2tex.py`.
4. **Build**: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
   `handbook/` (biber included) — must exit 0. Fix integration breakage:
   cross-part dangling refs resolve to real labels or degrade to prose; missing
   bib keys get real entries; genuine `handbook.sty` bugs get minimal fixes,
   recorded.
5. **Check**: `python tools/check.py --tree handbook --strict` must pass, and
   `--tree source` must still pass (regression).
6. **Commit.**

## 10. Global finalization (end of Phase 4)

1. **Reconcile registers honestly.** For every `depth-gaps.csv` row, determine
   from the actual tree whether it is filled at its ceiling; flip only those to
   `done (<commit>)`. Same for `apparatus.csv` phase-4 rows. Stubbed or partial
   stays `open` — the register is the campaign's memory, and a false `done` is
   worse than an open row.
2. `python tools/csv2tex.py`; rebuild `spec/gap-analysis.tex` (must exit 0).
3. Final handbook build; record page count and stub count.
4. Append a dated Phase-4 section to `spec/registers/execution-notes.md`: what
   was migrated per part, depth rows done vs open, notable verifier catches,
   open questions for Phase 5.
5. Commit; update the campaign memory file at
   `C:\Users\Crow\.claude\projects\C--Users-Crow-Downloads\memory\formal-logic-handbook-campaign.md`.

## 11. Definition of done

Phase 4 is complete when **all** of the following hold. This standard comes from
the approved plan; do not narrow it to fit what got built — if something cannot
be met, say so specifically and let the user decide.

- Parts 1–8 and 12 have migrated bodies and annex fragments; every source
  chapter of v1.1 Parts I–V and VII–XI is accounted for (migrated, or
  deliberately retired with the reason recorded).
- Every `must` and `should` depth row targeting those parts is filled at its
  treatment ceiling or carries an `\hbstub` naming its row id.
- No status was upgraded anywhere; every `proved`/`sketched` resolves to an
  annex item and every annex item is pointed at exactly once.
- `check.py --tree handbook --strict` passes; `--tree source` still passes.
- The handbook builds clean; the registers reflect reality.

## 12. Known risks

- **Scope creep** — the treatment ceilings and the NOT-IN-SCOPE register
  (`new-content.csv`, domain `x`) exist to stop it. Writing beyond a ceiling
  means editing the register row *first* (spec-first rule).
- **Silent status upgrades** during compression — the single most damaging
  failure mode, because it launders a sketch into a proof. The verifier's
  fidelity sample is the control.
- **P8 size** — 13 must + 17 should rows plus the first real card usage; split
  it rather than letting one agent run out of room mid-part.
- **Cross-part references** — a visit cannot `\cref` a label that does not exist
  yet. Keep forward references as prose and let the finalizer upgrade them.
