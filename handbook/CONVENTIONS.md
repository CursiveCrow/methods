# Handbook tree conventions (Phase-3 contract)

> **Front-matter correction (2026-09-08).**
> The user's current instruction removes the inherited Formal Logic title,
> preface and Graduate-Level Scope from the active book opening.
> Those files are archival, and restoration must not reinsert them.
> The Methods of Reason is a reference to reasoning and logic.
> The active frontmatter.tex owns the contents and page-numbering transitions;
> main.tex supplies the current book metadata.

> **Edition amendment (2026-09-07).**
> `spec/EDITION-2026-CONTRACT.md` and its approved execution plan govern the
> expanded reasoning scope, reference entries and nineteen-part printed order.
> Stable part IDs must be independent of printed numbering; existing labels
> remain stable. Implement compatibility changes before adding the new drivers.
> Other structural rules below continue to apply unless explicitly superseded.

> **Correction policy (2026-09-06, current user instruction).** Correct known
> mathematical errors directly in the active manuscript definitions, theorem
> statements, formulas, and proofs. Active files under restoration/ are part
> of that manuscript. Keep the frozen source/formal-logic-reference.tex and
> historical readings as archival evidence, and record correction provenance
> in spec/research/. Remove appended instructions that make readers repair
> an earlier false statement themselves. This policy supersedes the older
> prohibition on altering inherited reader text wherever a correction is
> needed. Source restoration and generated navigation must preserve these
> corrections.

> **Content-policy amendment (2026-08-11).** The structural and mechanical
> rules in this file remain binding, but they do not authorize any alteration,
> compression, normalization, selection, hybridization, retirement, or omission
> of logical content. `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md` governs
> fidelity and completeness throughout the book and supersedes conflicting
> Phase-3/Phase-4 content instructions.

Binding for every file under `handbook/`. Implements rulings §7 of
`spec/gap-analysis.pdf`. Tools parse these conventions mechanically — deviations
break the check suite, not just style.

## Layout

```
handbook/
  main.tex                 # book class driver; \input's parts and annex
  handbook.sty             # ALL environments/macros defined here, nowhere else
  parts/p01.tex .. p14.tex # part drivers: one transitive \part + chapter inputs
  parts/pNN/<chapter>.tex  # chapter files (kebab-case slugs)
  restoration/             # exact source-token captures, provenance-gated
  annex/pNN.tex            # added proof-audit layer, parallel to parts 1–12
  annex/pNN/<slug>.tex     # optional: per-chapter annex fragments, \input by annex/pNN.tex
  registry/calculi/<slug>.tex   # added calculus navigation sheets
  registry/symbols.csv     # symbol registry (data; generates Part-1 tables)
  bib/handbook.bib         # biblatex database (biber backend)
  generated/               # tool output only; never hand-edited
```

`main.tex` uses `\documentclass[11pt]{book}` + `\usepackage{handbook}` +
`biblatex` (`backend=biber, style=alphabetic`). It must compile with every part
present (stubs allowed: a part driver whose chapters are `\hbstub{<what is
pending>}` paragraphs).

Each part driver must expose exactly one reader-facing `\part` in its static
input closure. A direct driver heading and a source-exact inherited heading may
not coexist. When the frozen source supplies the required heading, the driver
reaches that provenance wrapper once and does not print a second heading or
inject a label into the byte-exact source command. Direct editorial headings
retain their ordinary `part:pNN` labels.

## Labels

Prefixes (checked): `part:`, `sec:`, `entry:`, `def:`, `thm:`, `tab:`, `fig:`,
`sheet:`, `rule:`, `annex:`. Nothing else. Every numbered environment defined
below takes its label as an ARGUMENT (not a following `\label`) so tools can
parse ownership. The id after the prefix begins `pNN-` for part-owned material
(`thm:p05-godel-second`), preventing cross-part collisions.

## Multi-agent intake files (Phase 4+)

Parallel part-visits never edit shared files. New bibliography entries go to
`bib/intake-pNN.bib`; new symbol rows to `registry/symbols-intake-pNN.csv`
(same header). Wave finalizers merge intakes into `bib/handbook.bib` /
`registry/symbols.csv` (deduping keys, checking glyph collisions) and delete
the intake files. New calculus sheets are ordinary new files under
`registry/calculi/` (disjoint by construction).

## Status grammar (compile-mandatory)

Status specs are single tokens of exactly one of three forms:

- `proved=annex:<id>`   — full proof at that annex item
- `sketched=annex:<id>` — sketch at that annex item (omissions enumerated there)
- `cited=<bibkey>`      — statement only; source carries the proof

`handbook.sty` must raise a compile ERROR (`\PackageError`) on an empty or
malformed status argument.  New editorial proof-audit material lives under
`annex/`.  An exact, hash-checked inherited-source capture may retain its
original proof environment at its source-mapped destination; the bounded
restoration scope does not authorize a new or rewritten body proof.

## Environments (defined in handbook.sty)

Theorem-class (numbered per chapter, shared counter; all take label first):

```latex
\begin{hbtheorem}{thm:<id>}{<status-spec>}{<Title>} ... \end{hbtheorem}
\begin{hblemma}{thm:<id>}{<status-spec>}{<Title>} ... \end{hblemma}
\begin{hbcorollary}{thm:<id>}{<status-spec>}{<Title>} ... \end{hbcorollary}
\begin{hbdefinition}{def:<id>}{<Title>} ... \end{hbdefinition}
\begin{hbconvention}{def:<id>}{<Title>} ... \end{hbconvention}
\begin{hbmethod}{def:<id>}{<Title>} ... \end{hbmethod}
\begin{hbexample}{def:<id>}{<Title>} ... \end{hbexample}
\begin{hbwarning}{def:<id>}{<Title>} ... \end{hbwarning}        % numbered+indexed
\begin{proofboundary}{def:<id>}{<Title>} ... \end{proofboundary} % numbered+indexed
```

The status spec renders as a tagline under the statement, e.g.
"Status: proved (Annex P5.3)" with a hyperlink, and is written to the `.aux`-side
harvest file `\jobname.hbstatus` (one line per result:
`<label>|<status-form>|<target>|<part>`) for tools to consume.

System entry cards (Part 8 and elsewhere):

```latex
\begin{systementry}{entry:<id>}{<System Name>}
  \entryaliases{...}                    % optional
  \entrylanguage{...}
  \entrysemantics{...}
  \entrycalculus{sheet:<id>}            % pointer into registry/calculi
  \entryadequacy{<status-spec>}{...}
  \entrydecidability{<status-spec>}{...}
  \entrycharacteristic{...}             % theorems/failures, free text
  \entrytranslations{...}               % optional
  \entryalgebra{...}                    % optional
  \entrysources{<bibkey>[,<bibkey>...]}
\end{systementry}
```

`\entryadequacy`/`\entrydecidability` take a status spec (same grammar,
compile-enforced) plus text.  Card data are harvested to `\jobname.hbentry`
in this typed grammar:

```text
CARD|<entry-label>|<part>|<system-name>
FIELD|<entry-label>|<field>|<content>
STATUS|<entry-label>|<field>|<status-form>|<target>|<content>
```

One `CARD` row begins each card; `part` has the form `pNN`.  Required fields
occur exactly once and are nonblank.  Adequacy and decidability use `STATUS`;
the other required fields use `FIELD`.  Rows follow card/source order.  The
payload is the final column, so consumers use bounded splitting and preserve
any literal `|` in that payload.  Optional fields remain optional; this
document does not claim that the implementation rejects duplicate optional
fields.

The serialized field tokens are `aliases`, `language`, `semantics`, `calculus`,
`adequacy`, `decidability`, `characteristic`, `translations`, `algebra`, and
`sources`.  Optional nonstatus fields, when present, also emit `FIELD` rows.
This typed stream is a structural harvest only: it carries no source locator,
presentation-packet identity, admission status, or completeness verdict and
therefore cannot by itself authorize a derived table or a release claim.

Every card must supply the seven unmarked fields: language, semantics,
calculus, adequacy, decidability, characteristic theorems/failures, and
sources.  Aliases, translations, and algebraic counterpart are optional.
Missing required fields are compile errors and strict-check failures.

Annex (Parts 1–12; Part 1 is included because the Phase-4 work order
explicitly retains the CSB and Cantor proofs):

```latex
\begin{annexitem}{annex:<id>}{thm:<backref>}{<Title>}
  ... proof or labeled sketch ...
\end{annexitem}
```

Every `annexitem` names exactly one body result; the bidirectional check
enforces: every `proved=`/`sketched=` target exists as an `annexitem`, and every
`annexitem`'s backref is a body result whose status points back at it (112=112
discipline). Inside `annexitem`, ordinary `proof` environments are allowed; a
sketch must open with `\sketchnote{<what is omitted>}`.

Stubs: `\hbstub{<one sentence: what is pending, which register rows>}` — renders
visibly boxed and is counted by tools.  Zero stubs is only a structural metric;
it does not establish full transcription or any source-fidelity AI,
topic-specialist AI, adversarial-publication AI, static, build, or visual gate.

## Calculus registry

Each added `registry/calculi/<slug>.tex` contains only:

```latex
\calculussheet{sheet:<slug>}{<Display Name>}{<one-line identity: language,
  sequent shape, negation treatment, equality treatment>}
\hbrule{rule:<slug>-<rulename>}{<RuleName>}{<premises>}{<conclusion>}{<side conditions>}
...
```

`\hbrule` renders premises over conclusion with the name at the right and the
side condition below; ALL five arguments mandatory (empty side condition is the
explicit token `\none`).  A new editorial rule display outside
`registry/calculi/` is a check-suite failure.  An exact, hash-checked inherited
source capture retains every original rule display at its source-mapped
destination; registry sheets cross-reference rather than replace it.  Part-14
sheets and body chapters may `\input` navigation sheets (optionally via
`\showcalculus{<slug>}`).

Nomenclature ruling (binding): `sheet:lk` is the two-sided, primitive-negation,
contexted-initial-sequent presentation (the v1.1 Parts II–III calculus);
`sheet:lk-defneg` is the defined-negation variant; `sheet:lk-eq` adds the
equality rules and is a distinct calculus. Slugs to seed in Phase 3:
`nd-cpl`, `nd-fol`, `lk`, `lk-defneg`, `lk-eq`, `lj`, `hilbert-cpl`,
`hilbert-fol`, `hilbert-k`, `hilbert-t`, `hilbert-s4`, `hilbert-s5` (modal
extensions may state "all rules of sheet:hilbert-k plus:").

## Symbol registry

`registry/symbols.csv` header:

```
glyph,macro,role,scope,precedence,first_use,notes
```

LaTeX-valued cells (same conventions as spec/registers). `scope` is a part/chapter
range or `global`. Normally
there is one glyph–role pair per row, and an undeclared glyph with two roles in
overlapping scopes is a check failure. A named primary calculus, logic, or
model keeps its own published syntax: if that syntax reuses a glyph, each local
type and standing must be declared before use and every genuine typed role must
be recorded honestly rather than renamed to fit a house notation. Seed
contents: the 34 v1.1
registered-notation rows, RE-HOMED under the Phase-1 glyph rulings
(the house defaults for newly introduced editorial notation: `|·|` cardinality;
domains `\dom`; `≡` elementary equivalence; `⇔` formula equivalence; `:≡`
definitional; forcing macro `\forces`. An identified source presentation keeps
its own notation and may reuse one of these glyphs for another role, for
example bars around a structure for its domain, provided the role and its
scope are defined before use and recorded in the registry, and the typed
distinction and any valid bridge are stated where the meanings meet:
spec/decisions/edition-2026-coverage-policy-resolution.md section 7), plus
every symbol the audits listed as unregistered (Parts IV–IX list and the Part-X
list: ⊩, □, ◇, X U F G, K_i E_G C_G, ⊗ ⊸ 1 !, Routley–Meyer W N R *, matrix
V D f_c, per-system turnstiles, ⌜·⌝, numeral bar, ≤_m ≤_T, φ_e, ∅⁽ⁿ⁾, V_α, rk,
L_α, ℙ, names/ν^G/x̌, M[G], ⊩ˢᵉᵐ, ε₀, ≤, >).

## Bibliography

biblatex/biber. Keys keep the v1.1 mnemonic style (`Jech2003`). Every entry the
old `thebibliography` had, plus the five primaries (Glivenko 1929, Gödel 1933,
Gentzen 1936, Kleene 1938, Priest 1979), plus intake stubs for every source
named in `spec/registers/new-content.csv` rows with priority `must`
(`keywords = {stub}` on entries whose full data is pending).  The check suite
counts these stubs.  Any remaining bibliography stub keeps the bibliography,
all three AI review gates, static, build, visual, rights, and reproduction
gates open.

## Checks (tools/check.py --tree handbook --strict)

Hard failures: malformed/missing status specs; new editorial body `proof`
environments; new editorial rule displays outside the registry;
annex↔body bidirectional mismatches;
label-prefix violations; duplicate labels; dangling refs; undeclared glyph-role
collisions in symbols.csv; chapters (non-stub) with zero citations; undefined
bib keys; and missing required system-entry fields (`entry-fields`). Metrics:
stub count per part; status-form distribution; entry-card field coverage.
