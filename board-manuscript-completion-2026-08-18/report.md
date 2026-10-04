# Board report: manuscript-completion batch

- Verdict: Every source-level finding F1--F22 in the reviewed batch has been
  corrected and accepted by the relevant final poll.  F16 and F18 are
  source-fixed but deliberately retain final-build and rendered-page gates for
  index behavior and page furniture.  This board does not admit the book or any
  section: broader reader-visible OPEN material, register closure, external
  assignment, acquisition, final build, full visual inspection, and user
  acceptance remain outside this batch.
- Board: live source-fidelity, formal-logic topic-specialist, and
  adversarial-publication seats; blind r1, focused r2--r4, and final poll.  The
  chair can identify the live Codex seats but not an externally exposed exact
  deployment version, so this report is construction review evidence rather
  than terminal reviewer-provenance evidence.

## Coverage map

- Part V additions: checked by all three mandates; F10 fixed and accepted.
- Parts IX--XI: checked by topic and publication seats; F1--F5, F7, F12,
  F20, and F22 fixed and accepted.
- Parts XIII--XIV: checked by source and publication seats; F13--F16 fixed at
  source, with final render evidence still required for F16.
- New calculus sheets and affected Parts II, III, VI, VII, VIII, XII: checked
  against the filed agenda; F6, F8, F17, and F21 fixed and accepted.
- Bibliography and inherited backmatter conversion: all 64 inherited rows
  checked individually; F9, F18, and F19 fixed at source, with final render
  evidence still required for F18.
- Not checked by this batch: every non-agenda theorem and proof in the full
  656-file reachable reader graph, all remaining register/external/acquisition
  obligations, and any final PDF surface.

## Dispositions

- F1--F5, F7, F9--F15, F19--F22: fixed and accepted.
- F6: typed computations, universes, and genuinely multi-sorted dependent
  congruence fixed; topic-specialist final poll accepted.
- F8: exact J\"ager--Probst \(\mathsf{PA}_{\infty}\) calculus, indexed
  derivability, and cut-elimination bound fixed; topic-specialist final poll
  accepted.
- F16: all 569 symbol rows have unique registration anchors and compact-index
  links; final person/symbol sorting, target resolution, pagination, and layout
  remain build/visual work.
- F17: all eleven agenda sheets carry controlling citations and named
  dependencies; final citation rendering remains build work.
- F18: historical mapping evidence and live non-identical adaptation status are
  coherent; final running-head, folio, scaling, navigation, and legibility
  remain build/visual work.

## Rejected on the record

- R1: the proposal to invent a new page-furniture audit classification was
  rejected.  Historical mapping fields retain their evidentiary meaning while
  current destination fields explicitly prevent an exact-rendering claim; the
  adversarial seat withdrew its objection in r4.

## Dissents

None after the three final polls.

## Evidence checks

- E1: Rackoff's publisher-hosted formula and abstract establish the fixed
  elementary-recursive space bound now stated for Skolem arithmetic.
- E2: J\"ager--Probst Definition 1 and Theorem 2 match the live one-sided rules,
  domain, cut-rank/height judgment, and \(2_n(\alpha)\) conclusion.
- F9: the deterministic ledger check reports 64 static and semantic passes and
  pins the independent transcript digest in every row.

## Verification

- `python -B tools/check.py --tree handbook --strict`: all hard checks passed;
  zero inherited pending references and zero routed stubs.
- `python -B tools/build_inherited_bibliography_field_ledger.py --check`: 64
  static and semantic mappings passed.
- `python -B tools/build_named_theorem_index.py --check`: 335 live
  theorem/lemma rows reproduced.
- `git diff --check` on the repaired batch: passed.
- Full build and rendered-page inspection: not run, because the manuscript and
  its reader-visible OPEN backlog are still changing.

## Board records

The verbatim r1--r4 transcripts, chair evidence/rulings, ledger, and three final
polls are retained in this directory.  No reviewer edited the manuscript.
