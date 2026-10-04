# C5 publication-text review: bounded identifier repair recheck

Date: 7 September 2026. Recheck started at 09:54:33 PDT and completed within
the assigned ten-minute block. Reviewer: the existing independent publication
review context `/root/c5_publication_review`, following up its own filed
finding C5-PUB-01. Observed host: Codex desktop, Windows/PowerShell. The runtime
model identifier/version was not exposed, so no model version is asserted.
Observed checkout: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`,
HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.

## Decision

**C5-PUB-01: CLOSED. Tseitin publication-text scope: PASS at the repaired
hashes below.**

The two editorial example declarations now use the required part-owned `def:`
identifiers, the annex reference names the correct declaration, and the exact
byte-preservation check establishes that these three substitutions are the
entire change from the first-round reviewed files. The unchanged first-round
publication-text findings therefore carry forward. This is a bounded repair
recheck by the same reviewer, not a new complete independent review of every
line.

The earlier report,
`spec/verification/edition-2026-c5-publication-text-review.md`, remains the
record of the complete body/annex read and the original failure. This report
supersedes that failure disposition only. ACF remains PASS at its earlier
publication-text scope, and the nine candidate symbol rows/anchor pairings
remain PASS at their isolated construction scope. Their file hashes are
unchanged.

## Declarations, references and uniqueness

| Role | Former construction identifier | Repaired identifier | Actual location |
| --- | --- | --- | --- |
| Worked example declaration | `ex:p02-tseitin-worked` | `def:p02-tseitin-worked` | `handbook/parts/p02/tseitin-transformation.tex:149` |
| Root/domain boundary example declaration | `ex:p02-tseitin-root-boundary` | `def:p02-tseitin-root-boundary` | `handbook/parts/p02/tseitin-transformation.tex:173` |
| Annex example reference | `ex:p02-tseitin-root-boundary` | `def:p02-tseitin-root-boundary` | `handbook/annex/p02/tseitin-transformation.tex:105` |

A literal search across all handbook `.tex` files for all four former/current
identifier strings returned exactly those three current occurrences. Each
new identifier is declared once. The only reference to either example is the
annex reference above, which resolves textually to the unique root-boundary
example. Neither former `ex:` identifier remains in handbook LaTeX. The
historical report's old identifiers retain their evidence role.

The live naming rule was rechecked at `handbook/CONVENTIONS.md:103`,
`handbook/handbook.sty:13` and `tools/check.py:188`: editorial `hbexample`
environments own `def:` identifiers. Both repaired suffixes start `p02-` as
required for part-owned material. The annex still says `Example` and retains
the same intended countervaluation destination. No generic label-rule
weakening was introduced.

## Byte preservation and current frozen identities

The reviewer read each current file as bytes, mapped those bytes through
Latin-1 solely to perform the exact ASCII inverse replacements, then hashed
the inverse bytes. Latin-1 preserves every byte in this operation; no newline
or Unicode normalization was performed. The substitutions were made only in
memory, and no manuscript file was written.

| File | Actual current SHA256 | Actual inverse-replacement SHA256 |
| --- | --- | --- |
| `handbook/parts/p02/tseitin-transformation.tex` | `4A4646A5306D38D94A0C6743D66F3E9452D216BB7F94AEFC5D9287E3D33F1522` | `9E09805F966C64DF13CFDC0471C40AE0E0DCC9B2DC187B68E915E5E5A334E0D5` |
| `handbook/annex/p02/tseitin-transformation.tex` | `BF3A94038DCDB6B4ABD1735E0C2FB0C51E8D3F215C5F10D8F98F42553777515A` | `975195E565E2AE77F128EDA22568BF728555380F03E360006D4A5D67C4D19561` |

The body contains exactly one occurrence of each repaired identifier; the
annex contains zero occurrences of the worked-example identifier and one of
the root-boundary identifier. The two inverse hashes equal the exact
first-round reviewed hashes. This establishes preservation of all surrounding
definitions, gate clauses, theorem hypotheses, size qualifications, examples,
proof text and other references.

Additional unchanged hashes were recomputed during this recheck:

| File | SHA256 |
| --- | --- |
| `handbook/restoration/inherited-07295-07468.tex` | `A133AD43A7AF91BEC6DC90B1AC5335F0524C1447869CB382B05175138A9C0505` |
| `handbook/registry/symbols.csv` | `2B0A9C3C4740EC6CD28FDBEEC437329C8049991CDC0855B9F3AF07955D50F781` |
| `tmp/edition-2026-c5-candidate/symbols-tables.tex` | `76899033C8772705AB7592702208313CBD3DCB4A227D702D4B6AA8A88120253B` |
| `tmp/edition-2026-c5-candidate/symbol-index.tex` | `8C53E4771A7E9951098F5210C7B76E313523A197AB2F2C9EF722248D47E81073` |
| `handbook/parts/p02.tex` | `77811CDF11B5E6E2FBB3B56A45B229D973BA39815926DE29D49823D3F2FA7854` |
| `handbook/annex/p02.tex` | `CB924992058BF0846B4D83CB35E24165A2DB7BDC8B0BA1A974FC770F0ACF13D6` |
| `handbook/bib/handbook.bib` | `84FF6BDD200A86DB3D82B84B0405376C98F395C7E504DA6CC38F52EFF340B7CC` |
| `handbook/restoration/inherited-01946-02186.tex` | `185C35156F2E1983B1BEF028888C3FF2A0DFFF333366CFF1A3D2769225E37468` |
| `handbook/handbook.sty` | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `handbook/CONVENTIONS.md` | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |

## Read extent and carry-forward boundary

This recheck read current body lines 145-188 and annex lines 98-110, all
literal-search matches for the four example identifier strings across handbook
LaTeX, and the exact naming-rule lines identified above. Complete current
body/annex bytes were processed for preservation evidence. The first-round
report documents the complete textual reads and the necessary prerequisite,
source, route, bibliography and candidate-notation inspection; this bounded
recheck relies on that review plus exact byte identity outside the three
repaired strings.

The corrected identifiers do not affect ACF, its protected DLO neighbor, the
Tseitin mathematical content, bibliography, canonical symbol roles or candidate
anchor mappings. The earlier reported source-access limits remain as stated;
no primary-source acquisition was repeated or upgraded in this recheck.

Only this new report was written. No other C5 review was read during this
recheck. No manuscript/registry edit, software test, checker run, build, PDF
render, generated-view promotion or delegation occurred.

Closure of C5-PUB-01 grants only the stated publication-text disposition.
Correction provenance, the other independent review dimensions, scoped static,
build and visual evidence, formal admission, active generated lookup promotion,
whole-book integration and final user acceptance keep their own requirements.
Candidate lookup promotion remains a later admission step; this report does
not impose it as a prerequisite for the isolated candidate review or claim a
completed multi-gate admission.
