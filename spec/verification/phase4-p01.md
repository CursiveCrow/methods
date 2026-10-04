# Phase 4 verification: Part 1

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-10
Visit: P1, Notation, Symbols, Conventions, and front matter
Verified source: `v1.1-verified`; the live `source/` tree is unchanged.

## Delivered scope

- Front matter: title page, preface, lookup instructions, status grammar,
  annex protocol, terminology policy, naming policy, and evidence ladder.
- Body: symbol registry/binding/precedence; mathematical preliminaries;
  levels, consequence, and formal-work conventions.
- Annex: P1.1--P1.10, one complete proof for each P1 result labeled
  `proved`.
- Result inventory: 15 results -- 10 `proved`, no `sketched`, and 5
  `cited`.  Four cited results preserve the source evidence class; the fifth
  is the statused Ultrafilter Lemma required by S-005.
- Generated Part-1 audit: 27 labeled entries.
- Compression: the mathematical lookup chapter is approximately 3.7:1 by
  semantic alphabetic tokens against the two source chapters (the ratio is
  lower if TeX environment names, labels, and index keys are counted as
  prose).  Exact hypotheses take precedence over further shortening.

There are no depth-register rows whose `target_home` is P1.  Rows D-P1-005
and D-P1-001--004,006 originate in source Part I but are correctly homed in
Parts 2 and 6.  No P1 depth row is claimed complete.

## Source accounting

| v1.1 Part-I material | Disposition |
|---|---|
| Preface, terminology, and evidence policies | Compressed into `handbook/frontmatter.tex`; the three source evidence classes become the binding `proved`/`sketched`/`cited` grammar. |
| Graduate-level scope | The promise of a linear completion course is retired because the target is a lookup handbook. Audience, purpose, dependency order, and prerequisites remain in the preface and P1 registers. |
| Sets, classes, pairs, products, relations, functions, quotients | All definitions are represented in `mathematical-preliminaries.tex`; quotient well-definedness remains a method entry; ordered-pair identity retains a complete annex proof. |
| Size, ordinals, cardinal comparison | Definitions are represented; CSB and Cantor retain complete annex proofs; transfinite recursion remains cited. |
| Choice and finite coding | AC, the Ultrafilter Lemma, well-ordering, cardinal assignment, finite coding, and syntax counting are represented. S-005 is resolved with calibrated Halpern--Levy evidence. |
| Levels, language, semantics, consequence, proof | Compressed into `formal-work-conventions.tex`; source direction, use/mention, truth/satisfaction, model/structure, and countermodel restrictions survive. |
| Finite strings and concatenation | Definitions and all three results survive; complete proofs are P1.5--P1.7. The numerical pairing map is distinguished from the Kuratowski pair and proved bijective before use. |
| Inductive generation, structural induction/recursion, derivation induction, closures | General definitions, methods, and results survive; complete proofs are P1.8--P1.10. |
| Writing definitions, statements, proofs, and prose | Compressed into checklists, methods, and warnings in `formal-work-conventions.tex`. The nine-row error taxonomy survives. |
| Raw illustrative inference-rule display | Deliberately retired: the binding contract permits rule displays only in `registry/calculi/`; the conventions chapter instead explains registry references. |
| Formula-complexity example (R-019) | Deliberately retired from P1. Its well-definedness depends on unique readability; concrete formula complexity belongs with propositional syntax after that result. P1 retains the general recursion theorem and makes precedence conditional on unique readability. |
| Source exercises | Not reproduced as exercises. Routine drills are retired; the countable-choice exercise is routed to D-P1-006; propositional countervaluation work belongs to P2.1. Each definition, method, or distinction on which the exercises depend remains represented. |

Formal source totals checked: all 44 definition environments, all 14 original
result statements, all 10 complete source proofs, all five methods, and the
substance of every source warning are represented or have the explicit
retirement above.

## Apparatus

The following Phase-4 apparatus deliverables exist at their specified
ceilings:

- A-024: all sixteen binary Boolean truth functions, including NAND/Sheffer
  stroke and NOR definability notes;
- A-025: primary-source notation variants for the named
  Whitehead--Russell, Polish, Hilbert--Ackermann, and Gentzen sources;
- A-026: scoped Greek lowercase/uppercase, calligraphic, blackboard, and
  Fraktur family conventions;
- A-161: focused classical-logic sub-register covering connectives,
  quantifiers, metavariables, semantic/syntactic turnstiles, and sequents;
- A-186: a Part-1 further-reading section.

A-189 remains a cross-part/global row and is not claimed complete here.
The five direct rows remain `open` in `apparatus.csv` until the global Phase-4
reconciliation verifies them from the final integrated tree and records the
commit hash.

## Adversarial correction log

The visit was treated as wrong until rechecked. Corrections made after the
first draft included:

- added and wired a P1 annex after finding that the skeleton and contract had
  only anticipated Parts 2--12;
- restored exact finite/countable `iff` definitions, range versus codomain,
  finite-cardinal-list maximum, generated-set typing, image/inverse-image
  types, quotient hypotheses, sequence typing, and `A^{<omega}`;
- restored explicit set/cardinal/generation hypotheses in CSB, Cantor, finite
  coding, syntax counting, structural induction, and structural recursion;
- moved the numerical pairing proof out of the body, corrected its function
  type, and removed an undefined length symbol from the annex;
- restricted `countermodel` to sentences and restored structure-plus-
  assignment terminology for open formulas;
- corrected syntax standing, use/mention, singleton-premise consequence
  notation, truth in a structure, and the full formalization checklist;
- rehomed the Ultrafilter Lemma as a cited theorem, supplied the exact
  Halpern--Levy proceedings record, and replaced an overstrong/untyped
  independence formula with a relative-consistency statement in prose;
- completed A-026's Greek-uppercase rows and A-161's focused classical table;
- removed an active Sheffer-stroke collision with the cardinality glyph;
- made generated registry/audit tables readable and reproducible, including
  safe label breakpoints and landscape registry pages;
- corrected overflow in result statements, running headers, and annex
  headings; and
- retained R-017, R-018, and R-020 in substance while disposing of R-019 as
  recorded above.

The final mathematical re-audit compared every original result and all ten
annex proofs, rather than only the minimum twelve-entry sample. It found no
status upgrade and confirmed one-to-one body/annex backreferences.

## Mechanical and visual evidence

- `python tools/check.py --tree handbook --strict`: pass.
- `python tools/check.py --tree source`: pass.
- `python tools/audit_tables.py`: 14 outputs, 62 rows; P1 has 27 rows.
- `python tools/symbols2tex.py`: 105 rows, 9 scope groups.
- Scratch P1/front-matter/annex build: pass, 58 pages.
- Full handbook build: pass, 178 pages, no unresolved citation or reference.
- Full-tree metrics at this visit: 292 bibliography entries, 37 stubs,
  global statuses `proved=16`, `sketched=3`, `cited=7`.
- Visual inspection covered title/front-matter policies, portrait and
  landscape registry pages, focused classical register, precedence and
  Boolean tables, historical notation table, every mathematical-preliminary
  page, formal-work/error/audit tables, and all four P1 annex pages. No
  clipping, unreadable table, or P1 material overflow remains.

Compilation verifies typesetting integration, not mathematical correctness;
the independent statement/proof comparison above is separate evidence.
