# C6 publication-text review R2: six notation-note repairs

Date: 7 September 2026. Reviewer context: `/root/c6_publication_review`.
Scope: the repaired note cells at canonical CSV lines 864, 865, 866, 868,
870 and 873, their isolated candidate table/index representations and anchors,
and the updated candidate README. This is the bounded follow-up to
`edition-2026-c6-publication-text-review.md`; it does not reopen unrelated
registry rows or undertake a new C5 proof review.

## Decision

**PASS at the assigned repair scope. C6-PUB-01 is closed.** The C6 tuple-code
note now uses the intended inline operator notation. The five related C5 note
encodings also pass: each repaired mathematical expression is correctly
delimited and agrees with the actual local manuscript notation. All six notes
are reproduced correctly in both candidate surfaces, with their existing row
anchors and corresponding index targets preserved.

The first-round manuscript publication-text pass remains supported by the
unchanged target hashes. Combining that unchanged evidence with this repair
recheck, the C6 publication text/candidate review now has a **PASS** at its
bounded content, notation-text and source-anchor scope. Admission, active-view
promotion and all remaining production and external-source gates remain
unresolved by these reviews.

| Component | Verdict | Evidence |
| --- | --- | --- |
| C6-PUB-01, canonical row 873 | PASS; closed | The prose `code_5` is now `\(\operatorname{code}_5\)`, matching the actual serialization formula. |
| Related C5 note encodings, rows 864/865/866/868/870 | PASS | `Z_\varphi`, `z_a`, `r_\epsilon`, `V\cup Z_\varphi`, `S_\varphi` and the numerical subscripts are all inside balanced inline math. |
| Six candidate table entries | PASS | The notes preserve those delimiters and mathematical commands; the macro-column spellings remain inside their existing `detokenize` treatment. |
| Six candidate index entries and registration anchors | PASS | Every index target points to the matching canonical-row anchor in the candidate table. |
| Candidate README identity and status | PASS | It identifies the current canonical hash and 886 data rows, names the six-cell repair, and retains the isolated pre-admission status. |
| Full C5 mathematical/publication acceptance | UNRESOLVED by R2 | The assigned C5 recheck concerns the five note encodings only. |
| Build, render, visual quality, source acquisition/fidelity, rights, provenance, admission, active-view promotion and release | UNRESOLVED by R2 | No such gate was executed or granted. |

## Cell-by-cell inspection

The row numbers below are physical CSV lines, including the header at line 1.
Each table entry has the label `entry:symbol-registry-` followed by its
five-digit row number. Each listed index entry uses that exact label in its
`hyperref` and `pageref`.

| CSV row | Repaired note content inspected | Candidate table line | Candidate index line | Local notation check |
| --- | --- | --- | --- | --- |
| 864 | `\(Z_\varphi\)`, `\(V\)`, `\(z_a\)` | 207 | 885 | `parts/p02/tseitin-transformation.tex:29–45` defines the original variable set, fresh variables and their set, including the alias convention. |
| 865 | `\(z_a\)` and `\(r_\epsilon\)` | 208 | 728 | The root is exactly `\epsilon` at line 32; representatives are defined at 47–53 and the root clause uses `r_\epsilon` at 75. The repair preserves that glyph. |
| 866 | `\(V\cup Z_\varphi\)` | 209 | 350 | The displayed union has the intended variable-set meaning; both constituent sets are defined at 29–40. This replaces the earlier prose spelling of the same union. |
| 868 | `\(S_\varphi\)` | 211 | 94 | The clause set is defined at 73–78, and lines 80–89 distinguish the emitted list from the set. |
| 870 | `\(N\)`, `\(M\)`, `\(L\)`, `\(n_0\)`, `\(n_1\)`, `\(n_2\)` | 213 | 572 | N and M are defined at 35–37, L at 135–137; `annex/p02/tseitin-transformation.tex:112–114` gives exactly the bottom/negation/binary-connective counts in the note. |
| 873 | `\(\operatorname{code}_5\)` | 359 | 739 | `restoration/inherited-07851-08048.tex:36–61` uses this operator for the same five fields in the same order. |

No underscore in any of these six repaired note cells remains outside its
inline mathematical expression. The names and subscripts are valid LaTeX in
that context. The corresponding table and index prose cells preserve the same
expressions. The original C6 failure therefore has no remaining occurrence in
the assigned canonical note or either of its candidate representations.

The six current rows retain their previously read glyph, macro, role, scope,
precedence, first-use field and row identity. The repair changes the affected
note spellings while preserving their meanings. The unchanged part of the
registry was not rereviewed. Reading the CSV as records returned 886 data rows;
no generator or test suite was run.

## Exact current inputs and actual read extent

All paths are relative to `C:/Dev/the-methods-of-reason`. Hashes are SHA256 of
whole files. The normal read returned the assigned current identities on this
recheck, so an escalated read to resolve a stale view was unnecessary.

| Artifact | Actual read extent | SHA256 |
| --- | --- | --- |
| `spec/research/edition-2026-c6-notation-repair.md` | Complete 1–32 | `A2C649B07F0EDA4E89295582BF5559394AD76C96132AA6E84935F9B00D163FF4` |
| `handbook/registry/symbols.csv` | Exactly the six repaired rows for content; record count only for the remainder | `F8E907A8322C9584AAB6A8ED59FC25AE5200EE4FBE941AA77ED20AC58226EFDE` |
| `tmp/edition-2026-c6-candidate/symbols-tables.tex` | Lines 207, 208, 209, 211, 213 and 359 | `6D2166E7EA09A6DEB9682B2275008255832AB0D0BE5DC6886F3359EE33B6C19D` |
| `tmp/edition-2026-c6-candidate/symbol-index.tex` | Lines 94, 350, 572, 728, 739 and 885 | `3D1753BA052288216F8EF32E7F11B6CEC9DD1BC55C255F10C5B985355C984B0D` |
| `tmp/edition-2026-c6-candidate/README.md` | Complete 1–21 | `BA86B8FE99CCEDE1E5BF0CEA5200F693B1F6584A8902AE692109897107B2B47D` |
| `handbook/parts/p02/tseitin-transformation.tex` | 28–89 and 125–148; targeted symbol-location search also returned contextual occurrences | `4A4646A5306D38D94A0C6743D66F3E9452D216BB7F94AEFC5D9287E3D33F1522` |
| `handbook/annex/p02/tseitin-transformation.tex` | 110–140; targeted symbol-location search also returned contextual occurrences | `BF3A94038DCDB6B4ABD1735E0C2FB0C51E8D3F215C5F10D8F98F42553777515A` |
| `handbook/restoration/inherited-07851-08048.tex` | 36–61 reread; whole-file hash matches the first-round complete reading | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| `handbook/restoration/inherited-08710-08876.tex` | Whole-file hash reverified; first-round complete reading retained | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |

## Standing and retained boundaries

This review closes the identified C6 encoding defect and accepts the five
related C5 note encodings in the current isolated candidates. It does not
accept the older C5 projections retroactively, certify every other registry
row, or infer any unchanged-file claim beyond the fingerprints and prior
scoped evidence identified above.

The standard-model P4 theorem remains distinct from P5 numeralwise
representation and internal proof transformations. Universal-machine and
parameter/compiler proof boundaries and later hierarchy completeness and
strictness retain their earlier status. External source-body review and rights,
correction provenance and restoration preservation, scoped static/build/visual
evidence, admission, active generated views and final integrated publication
remain separate obligations. Candidate semantic and encoding review is valid
before admission; no promotion is required to establish this repair result.

No source, manuscript, registry, projection, provenance or tooling edit was
performed by this reviewer. This R2 report is the sole write. No tests,
generator execution, build, render or delegation was performed. The runtime
model identifier/version remains independently unverified. No page appearance,
compiled link destination, final publication readiness or user acceptance is
claimed.
