# Independent source-fidelity recheck: quantified-matrix code argument

Date: 7 September 2026, local time. Recheck started 8 September 2026 at 00:32:12 UTC. Reviewer: independent `pa_abduction_source_review` context. Scope: the single notation clarification at `handbook/parts/p05/pa-checker-arithmetization.tex:211`. The reviewer did not author this change and has seen no other review findings about it.

## Verdict

**PASS. The clarification preserves the checked description and source meaning under the existing constructor-field expansion convention.** It explicitly passes the quantified matrix's numerical code to the maximum-index function. The previous PA and finite-abduction source/text verdicts are retained at their unchanged scopes. No content is formally admitted by this recheck.

## Exact change and verification

The current PA body has 523 lines and SHA-256 `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA`.

At line 211, the bound changed from

```tex
1+\max(m(\theta),m(u),i,j)
```

to

```tex
1+\max(m(a_1(c)),m(u),i,j)
```

The current file contains exactly one occurrence of `m(a_1(c))`. Replacing only that occurrence by `m(\theta)` in memory yields SHA-256 `EC93120E394DAC60169EFABCE50CB174C44AD65502674F9E704C8ADF6EFA92D2`, exactly the body reviewed in Round 2. This proves the complete body difference. No inverse edit was written to disk.

## Constructor and source relation

The body at 56-64 makes a newly introduced constructor field name an abbreviation for its argument projection. At 128 it defines `a_j(c)=e(t(c),j)`, and at 130-131 it gives the exact constructor test and cons encoding. The source constructor grammar at `handbook/restoration/inherited-09328-09438.tex:57-59` codes a quantified formula as `N_11(j,code(theta))` or `N_12(j,code(theta))`. Its matrix is therefore the second argument, `a_1(c)`; the first argument is the binder index.

The maximum-index function `m` is the numerical metadata function defined at body 148-157. Consequently the clarified argument `a_1(c)` is precisely the code required by that function. Under the already declared field-to-projection expansion, the earlier matrix shorthand denotes this same projection. The clarification exposes that existing expansion in the display and introduces no new selector or fresh-variable choice.

Body 202-213 retains its valid-expression and replacement-term requirements, stopped-binder case, nonconflicting-binder case, least search, zero failure value, and rename/continuation commands. The source substitution implementation at `handbook/restoration/inherited-09328-09438.tex:172-185` chooses the least variable absent from the matrix, replacement term, and the two named indices, with a bound one above their largest index. Using `m(a_1(c))` expresses the matrix contribution to exactly that bound. It leaves the all-variable tests, forbidden indices, candidate order, and continuation unchanged.

Thus the same matrix code supplies the maximum-index bound and the renaming command's matrix argument at body 213. The previously checked finite expansion, substitution behavior, and source correspondence are preserved.

## Retained evidence and scope limits

The following directly relevant files were rehashed and match the prior review:

| File | SHA-256 |
| --- | --- |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-03240-03428.tex` | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/parts/p16/finite-abduction.tex` | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |

Reading in this recheck covered body 56-64, 125-134, 148-157 and 202-220, and source grammar/substitution lines 55-60 and 172-185. The inverse-substitution hash verified all other body bytes. Complete prior read extents remain recorded in [Round 1](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-pa-abduction-source-review.md), with the SF-A1 repair result in [Round 2](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-pa-abduction-source-review-r2.md).

The unrelated P17/Kamp shared integration changes were outside this assignment and were not reviewed. Prior integration hashes describe their earlier snapshots; this recheck supplies no new whole-integration verdict. No tests, builds, renders, manuscript/shared-file edits, or new review scope were undertaken. Only this report was written. Independent admission and all previously stated remaining proof and publication obligations stay separate.
