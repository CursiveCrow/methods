# P15 symbol-checker compatibility repair: F1

Date: 7 September 2026. Author: `/root/p5_kamp_source_review`.
Scope: publication finding F1 in
`spec/verification/edition-2026-probability-kamp-l1-publication-text-review.md`.
Result: the bounded checker correction and its focused regression verification
are complete. This note supplies repair evidence; the independent reviewer
retains responsibility for closing the filed finding.

## Defect and exact change

The actual CSV validation path in `tools/check.py::_hb_check_symbols` groups
registrations by glyph, intersects their `_hb_scope_parts` footprints, then
reports differing roles as `glyph-collision` and repeated identical roles as
`symbols-csv`. Before this repair, `global` stopped below unit 1500, so a
P15-P19 registration could bypass both diagnostics.

The only production-code change is inside `_hb_scope_parts`, at line 1480:

```diff
-    full = set(range(100, 1500))  # parts 1..14, every chapter unit
+    full = set(range(100, 2000))  # stable parts 1..19, every chapter unit
```

The existing `part * 100 + chapter` encoding, endpoint parsing, chapter range
meaning, inclusive range endpoints and stable-ID ordering remain unchanged.
The enlarged full set contains every chapter unit 0-99 for stable parts P1-P19.
Blank and unparseable scopes retain their conservative global fallback, now
with the same corrected footprint. No new scope grammar or schema is introduced.

This agrees with `tools/symbols2tex.py` for the approved stable-ID domain.
The generator already admits P1-P19 and defines its global interval to cover
them. Its internal scale is different; the regression compares overlap
decisions rather than requiring identical internal integer encodings.

## Regression seam and reproduction

New file: `tools/test_check_handbook_symbol_scope.py`.
There was no existing test directly exercising `_hb_check_symbols` or
`_hb_scope_parts` among the inspected `tools/test_*.py` files. The new test
uses standard-library `unittest`, temporary CSV files and the actual `_HBData`
and `_hb_check_symbols` implementations. Each fixture contains exactly two
registrations of the same glyph. It does not mock scope parsing or reproduce
the validator's algorithm inside the test.

The seven test methods exercise 70 two-row validation cases:

- A global conflicting role against a chapter in every approved stable part,
  including each of P15-P19, with the actual diagnostic category and location.
- Identical-role duplicates in P15.1 and P19.99, with reversed row ordering.
- Global overlap with full P15/P19 scopes and the last valid P19 chapter.
- The existing blank/unparseable conservative-global behavior in P19.
- Disjoint chapter scopes P8.2-P8.4 versus P8.5 and P15.1 versus P15.2;
  disjoint stable-ID ranges P11-P14 versus P15-P19, for both equal and
  differing roles. Printed order does not change those stable-ID ranges.
- Inclusive overlapping chapter and cross-part ranges that must still fail.
- Thirty-six pairings comparing the actual checker's collision result with
  the existing generator's `parse_scope`/`overlap` decisions.

The test file was saved and run before changing production code:

```powershell
& 'C:\Users\Crow\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -m unittest tools.test_check_handbook_symbol_scope -v
```

Working directory: `C:/Dev/the-methods-of-reason`.

Before the repair, the command exited 1:

```text
Ran 7 tests in 0.318s
FAILED (failures=15)
```

These are fifteen failed subcases, not fifteen test methods. The checker
returned empty findings for the global-versus-P15-P19 collision and duplicate
cases. The generator parity test also returned `False != True` for global
against P15, P15.1 and P19.99. The disjoint-scope and existing range-overlap
controls already passed. This reproduces F1 through the real CSV path rather
than merely asserting what a parser helper should return.

After the one-line correction, the same command exited 0:

```text
Ran 7 tests in 0.196s
OK
```

All collision, duplicate, fallback, disjointness, endpoint and generator-parity
cases passed. The interpreter used `-B` to avoid creating repository bytecode
artifacts. Temporary CSV fixtures were removed by their context managers.
Only this focused module was run; no manuscript build/render or full-book
checker run was added to the assignment.

## Preservation and identities

The working tree already contained substantial modifications to `tools/check.py`.
They were preserved. To verify the change boundary independently of the dirty
HEAD diff, I hashed the file bytes outside `_hb_scope_parts`: the bytes before
`def _hb_scope_parts(` concatenated with the bytes starting at the newline
before `def _hb_check_symbols(`. That digest was identical before and after:

`382FB1380112C5A85B014AE8864B9854CA75918D5B5065FBF2494A617D665FDC`.

Thus the existing restoration validation and every other part of `tools/check.py`
remain byte-identical to the pre-repair working snapshot. The parsed-scope
function itself was read back and differs only by the displayed line.

| Artifact | SHA256 |
| --- | --- |
| `tools/check.py`, before this repair | `5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57` |
| `tools/check.py`, after this repair | `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914` |
| `tools/test_check_handbook_symbol_scope.py` | `90D03DDE20646E644E8FB26BCE6C496618F009FD1164E74C87EF8955B30017F4` |

The bug-diagnosis skill supplied the actual-path failing-test discipline.
Broad bisection and instrumentation were unnecessary because the independent
publication finding had already isolated the defective branch, and the
minimal fixtures reproduced precisely that defect before the repair.

Only the named production line, new test file and this note were written.
F2's canonical numerical-order scope edits, generator outputs, corpus,
manuscript integration and review records remain with their assigned owners.
No registry contents or source/provenance records were changed. The next
handoff is a bounded independent F1 recheck against these exact artifacts.
