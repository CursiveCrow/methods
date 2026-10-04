# Independent source-fidelity repair recheck: SF-A1

Date: 7 September 2026, local time. Recheck began 8 September 2026 at 00:08:30 UTC. Reviewer: the independent `pa_abduction_source_review` context. Repository: `C:\Dev\the-methods-of-reason`. The reviewer did not author the repair and has seen no other current review findings.

## Verdict

**PASS: the current repair closes SF-A1 at source/text scope.** The body now specifies the exact seven-entry cons-list, calls the previously defined total entry description, explicitly retains its zero out-of-range value, and places that particular selector in the prescribed bounded fold. The exact-description selection issue reported in Round 1 is resolved.

Combined with the unchanged source/text findings in [the first review](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-pa-abduction-source-review.md), the assigned PA checker scope now passes this source-fidelity review. The SF-A1-dependent uncertainty about the selected-description MP theorem is discharged at this same review scope. The prior finite-abduction source/text PASS is preserved.

This report does not grant specialist mathematical acceptance, publication acceptance, formal admission, D3, the remaining proof builders, or wider source/subject completion. No tests, manuscript build/render, manuscript edits, shared-file edits, or other reviewer consultation were performed in this recheck. Only this assigned Round 2 report was written.

## Exact current difference

Current body: `handbook/parts/p05/pa-checker-arithmetization.tex`, 523 lines, SHA-256 `EC93120E394DAC60169EFABCE50CB174C44AD65502674F9E704C8ADF6EFA92D2`.

The only body change replaces old lines 282-285 with current lines 282-292. The current hunk reads:

```tex
\begin{aligned}
 Q_7&\defeq[q_1,q_2,q_3,q_4,q_5,q_6,q_7],\\
 \mathsf{Ax}_{19}(a)&\defeq\mathsf{Sent}(a)
       \mathsf{sg}\!\left(B(a)+\sum_{j<7}E(a,e(Q_7,j))\right).
\end{aligned}
\]
The constant \(Q_7\) expands to the displayed seven-entry cons-list, and
\(e(Q_7,j)\) uses the previously fixed total entry description, including
its zero value when \(j\geq7\).  The sum uses the declared bounded fold
with this particular selector.  Each of the seven \(q_j\) constants inserts
its exact finite constructor expression in
```

The continuing cross-reference and sentence are unchanged at current lines 293-294. Replacing this hunk with the exact four old lines **in memory only**, while preserving the file's bytes and newline convention elsewhere, gives SHA-256 `33195DFF4BB6D2D7BD898E0AF9D8EC1980A1272593139624AA17577E132C15F5`, exactly the Round 1 body hash. This verifies the complete difference and establishes that all other body text is unchanged. No inverse patch was written to disk.

## Why the repair closes the description gap

| Obligation | Result | Exact evidence |
| --- | --- | --- |
| The seven constants have one declared order and code | PASS | Current body 283 and 288-292 explicitly form `Q_7=[q_1,q_2,q_3,q_4,q_5,q_6,q_7]`. Body 85-86 expands this notation to seven nested calls of the specified C description with final tail zero. Each q constant expands through the literal constructor expression at `handbook/parts/p05/standard-pa-proof-predicate.tex:15-35`. |
| The counter selector is total and has the specified default | PASS | Current body 285 and 289-290 use exactly `e(Q_7,j)`. Its description is `e(c,j)=h(T(c,j))` at body 89-93, with zero out-of-range entries at 99-100. The new text expressly includes the zero default for j at least seven. It therefore selects one total function description on every natural counter value. |
| The bounded sum has an actual primitive recursive step | PASS | Body 66-80 fixes the fold expansion. The sum's update is the particular expression `A(v,E(a,e(Q_7,j)))`, with parameter a, counter j, and accumulated value v in the declared order; its initial value is zero and its bound is seven. Every invoked description is already declared, and the Q_7 constant expands through the stated cons and q expressions. No new selector choice or unbounded search remains. |
| Numerical axiom recognition is preserved | PASS | The list has length seven, and its entries at j=0,...,6 are respectively q_1,...,q_7 by the existing entry equations. Thus the seven tested equality values are exactly the previously reviewed seven literal axiom tests in the same order. The B(a), Sent(a), sign and sum structure is preserved. Canonical induction recognition and all row tests are outside the sole changed hunk. |
| The exact Gamma dependency now closes | PASS at source/text scope | Current body 405-416 expands all preceding library calls to d_19 and selects Gamma at output one. The repaired selector supplies the previously missing finite formation-tree branch. The governing description and fresh-variable construction at `handbook/restoration/inherited-09262-09327.tex:76-114` is unchanged. The repair chooses the entry-description expansion directly. |
| The existing annex arguments remain applicable | PASS for source/dependency closure | The unchanged annex at 11-34 expands the finite acyclic library, and at 103-113 identifies the same seven literal tests. Its internal list equations at 141-185 prove cons length and entry behavior, including the zero default. The joining proof at 479-507 reuses the same Ax_19 description on identical leaf-formula arguments; the repaired fixed description satisfies this premise. |
| The MP description uses the repaired checker | PASS | Current body 445-465 includes chi_19 in its guard at 454, and its expansion convention inserts the now-specified checker description. No row shift, argument order, discharge, parent-count, sentence or leaf-product clause changed. The selected-description uncertainty caused solely by SF-A1 is removed. |

The rest of the description conventions, grammar, substitution, alpha comparison, canonical induction, all twenty rows, numerical proof meaning, internal-library source dependencies, and stated D1/D2/D3 boundaries retain the complete reading and source comparisons recorded in Round 1.

## Verified unchanged scope

Every file/hash row in the Round 1 report's two manifests was rehashed. The body above is the sole changed file among those 26 rows. All other 25 file hashes match the first review, including the complete PA annex and listed graph/numerical/ND/syntax dependencies, both abduction files, all reviewed routes, and the canonical bibliography.

Principal retained hashes:

| File | SHA-256 |
| --- | --- |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-09262-09327.tex` | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/annex/p05/internal-proof-predicate.tex` | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/parts/p16/finite-abduction.tex` | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |

The abduction primary PDF was additionally rehashed and remains `E2A021C45BCDC6D2D1BC7AAC9972E75FEC697E3609094060CA92AFFCB694F265`. Its required reading and physical/printed page identifications from Round 1 remain valid; no additional PDF reading or rendering was needed for this repair.

The appended symbol row was read at `handbook/registry/symbols.csv:982`. It identifies Q_7 and e(Q_7,j) as the fixed seven-axiom cons-list and its total selector with zero beyond its seven positions. The whole registry hash is `F903FAD8C3A59673AD805F26960B9BFDB2D115A25291603BF0DB1C0FEB7868C4`. Hashing the prefix before this appended row reproduces the prior complete registry hash `7B813370086D8B0009B4FA43243B69098D19CEA57F3EEF0A81DFC1B599DE1766`, verifying that the earlier registry content is unchanged. The registry has 981 data rows plus its header.

The lead's isolated regenerated symbol outputs and their generation checks were not independently inspected or rerun here. They are not required to decide SF-A1's source-text correction, and this report grants no generated-output or notation-check acceptance.

## Reading extent and remaining gates

This recheck read the exact current changed hunk with surrounding body lines 259-302, the directly reused list description at 84-101, selected-graph clauses at 405-417, and MP description at 445-465. It verified the complete body difference by the inverse-hunk hash. Unchanged content retains the full reading extents recorded in Round 1; it was not represented as a fresh full reread. All prior source findings outside SF-A1 remain in place.

There is no remaining source-text defect identified in this repair scope. D3, evidence-to-proof builders, wider source coverage, the other independent review gates, integration/output verification, and formal admission retain their separately stated requirements. The first report remains unchanged as the historical record of the failed snapshot; this report records the successful correction against the current body hash.
