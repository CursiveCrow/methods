# Board report: Part V source/content review

- Verdict: the final Part V reader graph is source-faithful and
  mathematically acceptable under the independent source-fidelity,
  arithmetic/proof-theory, and adversarial-publication mandates. Every
  substantive finding is repaired and all three final polls say `accept`.
- Boundary: Part V is not globally admitted or publication-locked. Exact
  provenance destinations, reviewed-unit/register controls, the one final
  whole-book build, PDF/navigation checks, page-by-page visual inspection,
  human review, and user acceptance remain separate later gates.

## Coverage

- Exact Robinson arithmetic and PA, bounded arithmetic lemmas,
  representability, coding, diagonalization, Godel/Rosser incompleteness,
  derivability conditions, Lob, Godel II, Tarski undefinability, and exercises.
- Nonstandard arithmetic: finite-distance blocks, the countable order type,
  overspill, Tennenbaum's theorem and inseparability argument.
- External and formalized Sigma-one completeness, with a reciprocal annex
  proof for the full closure-style formula class.
- Relative interpretation and essential-undecidability transfer.
- GL: rule sheet, Kripke semantics, modal fixed points, the fixed-PA
  arithmetical realization, Solovay completeness, and Rosser witness
  comparison.
- Presburger and Skolem arithmetic, with procedures and calibrated complexity
  bounds.
- Paris--Harrington, Goodstein sequences, the exact Kirby--Paris hydra,
  presentation-sensitive consistency, and their proof boundaries.
- Reverse mathematics: exact two-sorted schemes, the Big Five, strictness,
  representative reversals, the inclusion figure, and reversal method.
- All Part V tables, figure, further reading, symbol/index entries, exact-source
  anchors, and the routed live theorem/definition register.

## Frozen evidence

- 19 exact inherited wrappers and all 980 authoritative source lines,
  preserved and routed once in order.
- 47 reachable files through 45 noncomment input edges.
- 104 reader identities after the final generated-table label; no duplicate
  active identity.
- All Part V references and citations resolve, including the specialized GL
  calculus-sheet identity.
- One `proved=` editorial result with exactly one reciprocal annex proof.
- 586 symbol-registry rows and 547 distinct glyphs reproduced in both
  generated symbol surfaces.
- 531 bibliography entries with zero intake stubs.
- 369 live named theorem/lemma index rows.
- The reachability-backed generator emits 14 captioned per-part registers from
  1,158 live theorem/definition rows; Part V contains 81 such rows and the
  stable table identity `tab:p05-theorem-definition-register`.
- No reader-visible OPEN/unadmitted/internal-gate prose, routed stub, pending
  inherited reference, missing citation, malformed status, orphan annex item,
  or unlabelled routed register table remains.

## Verification

- `python -B tools/check.py --tree handbook --strict`: all hard checks passed.
- `python -B tools/symbols2tex.py`: 586 rows, 10 scope groups.
- `python -B tools/audit_tables.py`: 14 captioned registers, 1,158 live rows.
- `python -B tools/build_named_theorem_index.py --write`: 369 live rows.
- `python -B tools/csv2tex.py`: six register-appendix surfaces regenerated
  with LF-stable output.
- `git diff --check`: passed.
- Full build and visual review: not run; the remaining manuscript is still
  changing.

## Board records

The charter, consolidated ledger, three blind round-one reports, two focused
repair rounds, final verification transcripts, and three one-word `accept`
polls are retained here. Reviewers made no manuscript, source, registry,
control, build, or test edits.
