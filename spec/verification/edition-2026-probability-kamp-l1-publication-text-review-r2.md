# Finite probability and Kamp III.2 Lemma 1: R2 publication recheck

Date: 7 September 2026. Reviewer: `/root/probability_kamp_l1_publication_review`.
Bounded recheck requested for the 21:12–21:32 UTC work block.
Repository: `C:\Dev\the-methods-of-reason`.

## Verdict

**F1 CLOSED / PASS. F2 CLOSED / PASS. Mathematical-content preservation PASS
against the final kept-heading probability body and the specified annex and
wrapper changes.** No additional blocking finding arose within this recheck.

This report closes only the two findings filed in
`spec/verification/edition-2026-probability-kamp-l1-publication-text-review.md`
and verifies the stated change boundary. That R1 report remains unchanged at
SHA-256 `58BE9946ACF5B3EA0437DE57FE1B07A3A8920BC6A15D971AA4CA97031BDC769D`.
Its complete four-file text assessment is retained through the exact
preservation evidence below. The complete manuscript was not reread for R2.

| Recheck | Verdict | Evidence |
| --- | --- | --- |
| F1: global scope in the actual handbook symbol checker | CLOSED / PASS | Corrected stable-part domain; seven focused tests pass; real canonical-registry path has no findings. |
| F2: P15 numerical `<` and `\leq` declarations | CLOSED / PASS | Both canonical ranges include P15; existing exceptions remain; only the two upper endpoints changed. |
| Candidate notation table and index | PASS | Both reflect the two repaired ranges; reversing those endpoints recovers the exact R1 files. |
| Probability body, final hash `130943...` | PASS, content preserved | Reversing only the aligned display and four `\par\nobreak` lines recovers R1 hash `BD14...`. |
| Probability annex | PASS, content preserved | Replacing the single title line break with its prior space recovers R1 hash `D51...`. |
| P15 body and annex wrappers | PASS, bounded layout/source scope | Removing only the local grouping and emergency-stretch assignment recovers both R1 wrappers. |
| Kamp Lemma 1 body/annex, bibliography and shared style | UNCHANGED | Whole-file hashes equal the R1 hashes. |
| PDF/build/visual acceptance, canonical-view promotion, global admission and nineteen-part migration | NOT CLOSED | Outside this bounded recheck; their separate evidence and obligations remain required. |

The root supplied an intermediate body with hash `3F20F4DA...`, then froze a
final body with hash `130943C2...` after adding `\nobreak` to the same four
paragraph breaks. The final preservation verdict in this report applies to
`130943C2394584116D11FD6F794FA12B3DBD1588DC84FF5AB242C12741CF9905`, not merely
to the intermediate file. Both versions were mechanically checked, but the
intermediate result is superseded for this handoff.

## F1: actual behavior and stable scope semantics

The repaired `tools/check.py:1480` now reads:

```python
full = set(range(100, 2000))  # stable parts 1..19, every chapter unit
```

The direct source read covered `_hb_scope_parts` and the full actual
`_hb_check_symbols` path at lines 1468–1554. The endpoint parser still encodes
stable part `p` and chapter `c` by `100*p+c`; whole-part scopes still cover
chapter units 0–99. Range endpoints remain inclusive. Blank and unparseable
scopes retain the existing conservative global fallback. The domain is now
exactly 100–1999, so every approved stable part P1–P19 participates in global
overlap. P15.1 is unit 1501 and no longer falls outside that domain.

The collision path is unchanged: registrations are grouped by glyph; the
overlap test at line 1540 controls whether differing roles produce
`glyph-collision` or identical roles produce `symbols-csv`. In particular,
the repair covers both differing-role collisions and repeated identical roles.

An exact inverse of the single changed line, performed entirely in memory,
recovered the complete R1 checker hash
`5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57` from current
hash `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`.
This confirms that no other production checker bytes changed relative to the
previous review, including the endpoint and range parser.

The 98-line focused test module was read completely before execution. Its
fixtures call `_hb_check_symbols` through real temporary CSV files and inspect
the actual findings. It does not replace the checker with a test-local
implementation. The independent rerun was:

```powershell
& 'C:\Users\Crow\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B -m unittest tools.test_check_handbook_symbol_scope -v
```

Result: exit 0; **7 test methods passed in 0.185 seconds**. Their loops cover
70 two-row CSV cases: global conflicts in every approved part; identical-role
duplicates in new parts; whole-part and P19.99 endpoints; conservative
fallbacks; disjoint chapter and stable-part ranges; inclusive overlaps; and
36 checker/generator overlap comparisons. The test controls retain
`P8.2-P8.4` disjoint from `P8.5`, `P15.1` disjoint from `P15.2`, and
`P11-P14` disjoint from `P15-P19`. Conversely, `P8.2-P8.4` overlaps `P8.4`,
and `P14-P16` overlaps `P15.1`. These are stable-ID intervals; the printed
placement of P15 before P11 does not reinterpret them.

The author repair note was read as context. Its reported old failing run was
not counted as an independent test run here. The R2 closure rests on the
reviewer's source trace, inverse-hash evidence and current actual-path rerun.
No broad checker or test suite was run.

## F2: repaired registry and candidate projections

Only the following scope cells changed in the 932-row canonical registry:

| CSV line | Symbol/role | R1 scope | R2 scope |
| --- | --- | --- | --- |
| 83 | `\leq`, canonical ordering | `P5.2-P14` | `P5.2-P19` |
| 87 | `<`, canonical strict ordering | `P4.4-P14` | `P4.4-P19` |

Both ranges now cover P15.1 and the approved later stable parts. The descriptions
remain ambient order on declared numerical and order-theoretic objects. The
object-language arithmetic exceptions at P4.3 and, for `\leq`, P5.1 remain
unchanged; the retained lower endpoints do not overwrite those declarations.
The remaining new source-specific meanings still require their own honest
typed scope declarations when introduced. Extending these ambient defaults
does not accept future P16–P19 content.

The changed rows project to candidate table lines 401 and 265 respectively,
and candidate index lines 290 and 3. Their entry identities `00083` and `00087`,
roles, first-use locators, notes and registration links are retained. Reversing
exactly one occurrence of each new range endpoint in each of the three files
recovers its R1 whole-file hash. Therefore every other registry cell and every
other candidate-output byte, including all seventeen rows 917–933 inspected
in R1, is unchanged.

In addition to the focused tests, the reviewer called the actual
`_hb_check_symbols` path on the current canonical CSV, followed by the
generator's `read_rows` and `collision_check` functions. This was a bounded,
read-only symbol check; the full handbook checker and output-writing generator
entry point were not run. Result: exit 0, **932 rows, 891 distinct glyphs,
handbook findings `{}`, generator errors `[]`**. Both repaired scopes contained
P15.1 under the checker. The generator returned intervals `(5002, 19999)` and
`(4004, 19999)` under its own scale. That different internal scale does not
alter the validated overlap semantics on the approved part/chapter grammar.

These results close the specific P15 coverage defect and confirm that this
two-row correction introduces no registry error detected by the actual current
symbol validators. They do not establish complete notation coverage for
unwritten future chapters or promote candidate files into the active apparatus.

## Exact mathematical-content preservation

The reviewer read the changed source spans and then used exact, counted string
substitutions on whole-file contents in memory. No transformed file was written.
Each current UTF-8 text re-encoding first reproduced its current whole-file
hash; the inverse changes then recovered the previously frozen whole-file
hash. This establishes the change boundary without relying on a dirty HEAD
diff or an author's summary.

For the final probability body, there was exactly one changed law-projection
display at lines 101–107. Its `aligned` wrapper, alignment marks and row break
place the same three equalities across two displayed rows. The event grouping
and both marginal formulas, their quantifiers/operands and following
push-forward formula are unchanged. Replacing just that block by its R1
three-line source spelling and removing exactly four standalone
`\par\nobreak` lines recovers the complete 461-line R1 body hash.

The four `\par\nobreak` lines are current lines 243, 259, 281 and 368,
immediately after the independence theorem, pairwise-independence example,
inspection example and expectation theorem headings respectively. They add
paragraph/page-break control between a heading and its unchanged body. They
introduce no mathematical expression, assumption, statement, definition, proof
target, example weight or attribution.

The probability annex's sole changed substring is in the final item title
at line 251: `Conditional\\means and their averaging property` replaces
`Conditional means and their averaging property`. Replacing that one title
line break with the prior space recovers the exact 284-line R1 annex hash.
All proof bodies and all result/back-reference labels are consequently
byte-identical to R1.

The body and annex wrappers now place only their substantive input inside
`\begingroup` / `\endgroup` with
`\setlength{\emergencystretch}{1.5em}`. Their stable ownership/part or annex
heading declarations remain before the group. Removing those exact three
new control lines recovers each complete R1 wrapper. The local setting controls
paragraph layout; it does not change the input identity or shared style.

| File | Current SHA-256 | Exact inverse recovers R1 SHA-256 |
| --- | --- | --- |
| `handbook/parts/p15/finite-probability.tex` | `130943C2394584116D11FD6F794FA12B3DBD1588DC84FF5AB242C12741CF9905` | `BD14BAB29058D7235155D827A8F11793A1D07AF119AD1B34239835EF98805AC0` |
| `handbook/annex/p15/finite-probability.tex` | `EA7BD4AA1783E4D94AB92B209E80517E62723524ADF4F1EEC4650B1D40DDDDB0` | `D51A43CF5E2CD2DCE15CD558EF3A167AC084347BB471E2A44E657769399EAE58` |
| `handbook/parts/p15.tex` | `234902D78F435603CC88523F5D7B19C21CA7E444730A92BAC91B8871C4AB0781` | `086B941242042DFC0797B625E4707E41FFC71322EBFBAE9231439DAE58E41794` |
| `handbook/annex/p15.tex` | `E8EC3BEEAEDAEFAA4E17F4C69EC6E3F48D44E3EC37046EFD2455DF408107D5AA` | `0C2B7A83557C8F939ECFB69064D7A0731DACC96C79CA3B67F92F51603DEE2FFB` |
| `tools/check.py` | `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914` | `5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57` |
| `handbook/registry/symbols.csv` | `4AA0A323A3B32831853650FAFE33E4E52FA39FF69DD13C6AAD27521B1891037B` | `4C8E503AA79DE05E399514211087E8ACA0BDF4D0DDE8961B5AED39609C075CF9` |
| Candidate `symbols-tables.tex` | `0BDF49D4101FBBAACF942A3033D1E40D0439C4CD5649927605544F719015D95F` | `31C7A631B7EE1CCA51F1C1B1B4DAC293EF604BDD81E3FC569B2C95DFB6A0645B` |
| Candidate `symbol-index.tex` | `39B7D207A96515973DE3A4313649DF0636962E809B108C4BD8C35806E006BFC0` | `AA2377EBB22285E065D55B4614FB51D8EC6D24D836E3ABB36B824FEEC3480921` |

Both candidate files in this table are under
`tmp/edition-2026-probability-kamp-l1-candidate/`.

## Read extents and remaining identities

The current whole files in the inverse-hash table were processed in memory in
their entirety. Direct human-readable source inspection in this R2 was bounded
as follows; it supplements the complete target-file reading recorded in R1.

| File | Total lines | R2 direct read / inspection extent |
| --- | ---: | --- |
| `tools/check.py` | 1740 | 1468–1554, entire scope parser and actual symbol-validation path |
| `tools/test_check_handbook_symbol_scope.py` | 98 | 1–98, complete; executed independently |
| `tools/symbols2tex.py` | 272 | 35–151, including approved grammar, interval semantics, CSV validation and collision check |
| `spec/research/edition-2026-p15-symbol-checker-repair.md` | 124 | 1–124, complete; author evidence kept distinct from independent rerun |
| `handbook/registry/symbols.csv` | 933 / 932 data rows | 79–89; actual validators read all rows; exact whole-file inverse verifies all other cells unchanged |
| Candidate `symbols-tables.tex` | 1143 | Changed rows 265 and 401, surrounding matching ordering declarations at 87–88 and 262; whole-file inverse |
| Candidate `symbol-index.tex` | 933 | Changed rows 3 and 290, matching ordering declarations at 2 and 288–289; whole-file inverse |
| `handbook/parts/p15/finite-probability.tex` | 467 | 48–120, 237–264, 275–305, 363–405, 415–437; all final `\par\nobreak` lines and adjacent headers/body; whole-file inverse |
| `handbook/annex/p15/finite-probability.tex` | 284 | 248–255 and exact title search; whole-file inverse |
| `handbook/parts/p15.tex` | 7 | 1–7, complete; whole-file inverse |
| `handbook/annex/p15.tex` | 6 | 1–6, complete; whole-file inverse |
| Kamp Lemma 1 body and annex | 202 / 212 | Whole-file hash equality to the fully read R1 targets; no new semantic reread claimed |
| `handbook/bib/handbook.bib` | 6594 | Whole-file hash equality to R1 |
| `handbook/handbook.sty` | 1826 | Whole-file hash equality to the R1 style; no shared-style change |

Additional exact hashes:

| File | SHA-256 |
| --- | --- |
| `tools/test_check_handbook_symbol_scope.py` | `90D03DDE20646E644E8FB26BCE6C496618F009FD1164E74C87EF8955B30017F4` |
| `tools/symbols2tex.py` | `1107FA18828213D26FC7221B3D51A384F27A8CF8C1B136FF6DD15A2076A614D5` |
| `spec/research/edition-2026-p15-symbol-checker-repair.md` | `54F0A48F11B5A80038F1DBF7F7009121F17C9BB610623F5F2B7B7EA37351AAE8` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/bib/handbook.bib` | `A9CFDB177C40F50581B87F8626318FDEFEAA7C5C300D7971A09FFEA2F22C9A53` |
| `handbook/handbook.sty` | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |

## Handoff boundary

The reported F1 and F2 failures are closed against these exact inputs. The
R1 mathematical/expository content passes survive the demonstrated layout-only
changes, and the seventeen new notation entries/projections retain their R1
content. This report adds actual symbol-validation evidence within the named
scope. It does not supply PDF inspection, publication-layout approval, a
full-book build/check, source-fidelity acceptance, canonical-view promotion,
global admission or completion of the nineteen-part migration. The unrelated
P5 annex prerequisite change was not reviewed.

The reviewer wrote only this R2 report. The focused module used temporary CSV
fixtures and `-B` to avoid repository bytecode output; the canonical-symbol
checks and inverse transformations wrote no outputs. No manuscript, registry,
style, production tool, candidate view or admission record was edited here.
