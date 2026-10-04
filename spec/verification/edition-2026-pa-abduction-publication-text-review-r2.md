# P5 substitution-bound notation: focused publication-text recheck

Date: 7 September 2026, America/Los_Angeles. Repository:
`C:\Dev\the-methods-of-reason`.

## Disposition

**PASS** at the current P5 body SHA256
`993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA`.
The changed bound supplies the numerical matrix code explicitly through its
declared constructor projection. The clarification agrees with the selected
description language and with the unchanged substitution proof. No further
publication-text repair is required for this change.

The first review's P5/P16 publication and scoped integration conclusions are
preserved for all unchanged content. Its report is
`spec/verification/edition-2026-pa-abduction-publication-text-review.md`, SHA256
`EF8A4FACCC97345741C967CDBBAD0A8A1EE2D5A37E0AD18ADB290F532B584B72`.
This recheck updates the P5 body identity to the current hash above; it does
not present the earlier body hash as current.

## Exact change and read extents

The file remains 523 physical lines. The only changed expression is at line
211:

```diff
- at most \(1+\max(m(\theta),m(u),i,j)\) absent from both all-variable
+ at most \(1+\max(m(a_1(c)),m(u),i,j)\) absent from both all-variable
```

The exact new expression `m(a_1(c))` occurs once. Replacing that occurrence
with `m(\theta)` in memory and hashing the resulting bytes reproduces the
complete prior P5 body hash:
`EC93120E394DAC60169EFABCE50CB174C44AD65502674F9E704C8ADF6EFA92D2`.
This establishes the one-expression delta against the earlier fully read
snapshot without altering either file.

For the focused recheck, the reviewer read current P5 body lines 125–157 and
202–216; inherited coding lines 45–64 in
`handbook/restoration/inherited-09328-09438.tex`; and current P5 annex lines
61–90. The first review records the full earlier body/annex reads and other
dependency extents. No current topic-review report or further reviewer finding
was consulted.

## Agreement with the declared types and proof

P5 body line 128 defines `a_j(c)=e(t(c),j)`. The governing grammar puts the
matrix of a universal or existential code at argument position one:
`N_11(j, code(theta))` or `N_12(j, code(theta))`. Therefore `a_1(c)` in the
quantifier case is precisely the numerical code of the displayed matrix
`theta`.

Body lines 152–157 define `m` as the retrieved maximum-variable-index output
on a numerical expression code. Consequently `m(a_1(c))` applies that
specified description to its declared numerical argument. Together with
`m(u), i, j`, it gives exactly the matrix/replacement/index bound used by the
least-fresh search. The total projection and its default are already defined
before this use.

The unchanged annex lines 68–77 identify this search with deterministic
capture-avoiding substitution and justify that its bound includes an index
greater than every forbidden one. Lines 79–90 supply the traversal count and
result invariant. The explicit code projection agrees with both arguments.

## Preserved identities and scope

Independent hash checks reproduce all identities in the first review's final
shared snapshot: the P5 annex, both P16 files, main driver, four P5/P16 routes,
bibliography, 1002-row registry, and both final candidate notation views.
In particular:

| File | Unchanged SHA256 |
| --- | --- |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p16/finite-abduction.tex` | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |
| `handbook/main.tex` | `5EBDFF789C4DF7B7CFF7DCBFE713F63555EC2543108D17C810BCA2B0B5EE2639` |
| `handbook/bib/handbook.bib` | `1B3D00B8336DE9A654EC074F6BBA6F8542A93F609736A98FEDB25F70A41EB27A` |
| `handbook/registry/symbols.csv` | `0F2EFCA2F92E7B967F3BE3EFA137C9DC36F9AD64BA314E987A48AD4817C4A14B` |
| `tmp/edition-2026-kamp-l2-p17/symbols-tables.tex` | `5BF00255B4CFF07D66765FE472CA3963C3D1096C54F35CE787B053E2415A1BCA` |
| `tmp/edition-2026-kamp-l2-p17/symbol-index.tex` | `C889B3519CFCAA1A70CCC688EBDC4FD1609DAF11820469A139469895B3136B1B` |

The first review's open D3, proof-builder, older-predicate-consumer, GL,
broader-abduction, full-source-presentation, lookup-promotion and production
obligations remain open. This is a focused text recheck with no formal
admission or user acceptance. No tests, generators, builds or PDF renders were
run. Only this report was authored.
