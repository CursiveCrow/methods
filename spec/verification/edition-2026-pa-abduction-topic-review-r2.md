# Focused topic recheck: explicit matrix-code argument

Date: 7 September 2026, America/Los_Angeles. Reviewer: `/root/pa_abduction_topic_review`.

**PASS. The optional P3 notation clarification in the original topic report is closed. All unchanged bounded P5 and P16 mathematical PASS findings are preserved.**

## Exact change verification

The current `handbook/parts/p05/pa-checker-arithmetization.tex` has 523 lines and SHA256 `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA`.

Its fresh-search bound at line 211 now uses `m(a_1(c))`. The complete changed fragment occurs exactly once. I reversed precisely this substitution in memory, without writing the manuscript, and computed the reconstructed bytes' SHA256:

```text
Current fragment:  \max(m(a_1(c)),m(u),i,j)
Previous fragment: \max(m(\theta),m(u),i,j)
Reconstructed previous SHA256:
EC93120E394DAC60169EFABCE50CB174C44AD65502674F9E704C8ADF6EFA92D2
```

The reconstructed digest is the exact body digest reviewed in the original report. This verifies that the current file differs from that snapshot by the indicated single substitution.

## Mathematical and definedness check

At `handbook/parts/p05/pa-checker-arithmetization.tex:128`, `a_j(c)` is defined as `e(t(c),j)`. The constructor at line 131 is `N_k(b_0,...,b_(r-1)) = C(k,[b_0,...,b_(r-1)])`. Hence the argument list for a quantified formula code is `[binder index, matrix code]`.

The actual grammar at `handbook/restoration/inherited-09328-09438.tex:58-59` gives universal and existential formula codes as `N_11(i,code(phi))` and `N_12(i,code(phi))`. Therefore, in the quantified case at current body lines 208-213, `a_1(c)` is exactly the code of `theta`. The new metadata call receives the declared numerical input and calculates the same maximum matrix-variable index used in the original mathematical argument. It selects the matrix rather than the binder index or the whole formula code.

The fresh-search bound, forbidden indices, least-choice rule, failure default and renaming command therefore retain their intended values. The existing existence argument for a fresh index and the existing substitution command-count proof need no changed hypothesis or step. The code brackets already present in the renaming command at line 213 are well typed and require no further edit.

## Preserved evidence and scope

The unchanged P5 annex still has SHA256 `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5`; the P16 body and annex still have SHA256 `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` and `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9`. The five specifically assigned PA prerequisite files also retain the hashes recorded in `edition-2026-pa-abduction-topic-review.md`.

The original bounded PASS findings for finite descriptions, syntax machines, direct axioms, row cases, selected graphs, internal joining, D1/D2 and all five finite-abduction results remain applicable with this explicit metadata argument. There is no remaining concern from the optional P3 clarification. The original report is preserved as the record of its reviewed snapshot.

This focused recheck writes only this report. It uses no new test, manuscript build or render, and reads no other reviewer's current report. D3, its proof builder, dependent GL consequences, broader abduction and formal admission retain their previous open standing.
