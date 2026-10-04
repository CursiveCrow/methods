# Focused review of editorial alias expansion

Date: 7 September 2026 Pacific time; 8 September 2026 UTC.
Reviewer: `/root/kamp_preferences_publication_review`.
Repository: `C:\Dev\the-methods-of-reason`.

## Verdict

**PASS. The four repaired manuscript files preserve the complete previous
text under the four exact expansions below. The specific inherited-scope
guard failures caused by these aliases are closed for the repaired files
and the changed registry/candidate entry.**

For each manuscript file, reversing only the declared literal expansions
in memory reproduced its full previous SHA256. The replacement counts and
current hashes match the assignment. The same complete inverse comparison
passed for the CSV and both candidate projections, each with precisely one
changed glyph. No mathematical statement, hypothesis, proof step, example,
label, citation, or semantic notation changed in those seven files.

The check preserves prior mathematical and source evidence only through
this verified identity of content and printed notation. It does not create
a new source or topic verdict. In particular, the P16 examination here is
mechanical preservation of its previously reviewed text; it is not a new
whole-unit P16 review. This report does not establish a successful TeX
build, rendered-page quality, complete production acceptance, formal
admission, or user acceptance.

## Guarded definitions and exact expansions

The actual `handbook/handbook.sty` definitions were read at 815-854 and
1067-1072. Each of the four aliases checks `\ifhb@inheritedrestoration`
and raises a PackageError when used outside the guarded source scope.
The emitted mathematical expressions are exactly these:

| Source-only alias | Definition / expansion line | Literal replacement |
| --- | --- | --- |
| `\Prop` | 824-829 | `\mathsf{Prop}` |
| `\True` | 842-847 | `\mathbf{T}` |
| `\False` | 848-853 | `\mathbf{F}` |
| `\R` | 1067-1072 | `\mathbb{R}` |

The P16 and P17 body drivers and annex drivers were read completely. They
input the repaired fragments as ordinary editorial material. The old
source-only commands therefore invoked an inappropriate scope guard at
those locations. The replacements use exactly the mathematical expressions
emitted by the definitions, without changing their fonts, letters, or
mathematical meanings. No change to the guard or to its protection of
inherited restoration was needed.

The style hash remains
`1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288`,
identical to the style identity read in the preceding publication review.
No style change was needed to close this finding.

## Complete inverse preservation

Each current file was read completely as UTF-8 text. The inverse operation
replaced its declared literal expansions with the original aliases only
in memory, encoded the resulting complete string as UTF-8, and computed
SHA256. No reconstructed manuscript file was written. Every resulting
digest equaled the previous complete-file digest from the author intake
or the preceding P17 review. This compares every character of the file,
including the unaffected text and line endings; it is not a sample of
selected lines.

| File | Lines | Verified replacements | Previous full hash reproduced by the inverse | Current full hash |
| --- | --- | --- | --- | --- |
| `handbook/parts/p16/finite-abduction.tex` | 340 | 5 Prop, 4 True, 2 False | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` | `19E88AF8C80B63A7125FE61B3FE9CE192564CA02456A61020570AD4C6B7B9BC9` |
| `handbook/annex/p16/finite-abduction.tex` | 283 | 4 Prop, 2 True, 2 False | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` | `9965EE04CE9F0D7F9A6CC786CEE9355BC0E7B1403803A61AF745087C1C06D893` |
| `handbook/parts/p17/finite-preferences.tex` | 330 | 11 R | `7C70F6C3428EFD358BDFDD99BA03911699DD7A4A16179033B408B9F9BE2AD988` | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` |
| `handbook/annex/p17/finite-preferences.tex` | 324 | 5 R | `30FAEDDD5023D3F64A565FA669C47980DE325A2BFECB6F96ACAED9398E204FE1` | `DFA00CC716098DA6BF6076FEF0258A4180DD868358561AC56E12CF96B925D9DF` |

All changed lines were also inspected in their actual notation contexts:

- P16 body: 25, 51, 58, 87, 91, 186, 197, 240.
- P16 annex: 15, 16, 21, 32, 38, 274, 279.
- P17 body: 97, 135, 164, 168, 173, 179, 183, 247.
- P17 annex: 70, 132, 193, 203.

Several listed lines contain two replacements. The totals are 19 P16
replacements and 16 P17 replacements. A corrected token-boundary search
over the four repaired files found no remaining `\Prop`, `\True`,
`\False`, or `\R` command. The search distinguishes a complete command
from a longer control-word spelling.

These observations close the identified scope-guard failure in the actual
edited locations. They do not independently repeat or certify the lead's
broader static-scanner result.

## Registry and projected entries

The sole CSV change is the glyph at physical line 987, from
`\(u,v:X\to\R\)` to `\(u,v:X\to\mathbb{R}\)`. The macro field
remains `u,v`, the role remains real-valued ordinal representations, the
scope and first-use fields remain P17.1, and the interpretation-boundary
note remains identical.

The candidate table projects this glyph at line 1228 under
`entry:symbol-registry-00987`. The candidate index projects it at line 914
and links to that same identifier. Both actual entries were read. The
typed role, scope, notes, and navigation agree with the CSV.

For each complete file below, reversing just that exact glyph string
reproduced its complete previous SHA256. Each file contained exactly one
copy of the replacement glyph. Thus the regeneration changed no other
candidate or registry text in this comparison.

| File | Lines | Previous full hash reproduced by the inverse | Current full hash |
| --- | --- | --- | --- |
| `handbook/registry/symbols.csv` | 1,003 physical lines: header plus 1,002 data rows | `0F2EFCA2F92E7B967F3BE3EFA137C9DC36F9AD64BA314E987A48AD4817C4A14B` | `0F404DB829E704A9166A4B219498003AB1217A72EB5B7F579E65B5C402774C47` |
| `tmp/edition-2026-kamp-l2-p17/symbols-tables.tex` | 1,261 | `5BF00255B4CFF07D66765FE472CA3963C3D1096C54F35CE787B053E2415A1BCA` | `ADDDA71CDCBFFED7AF0F4B25AD44ACDC4CE7D3B1936FF6EDADB3BF0123A68D91` |
| `tmp/edition-2026-kamp-l2-p17/symbol-index.tex` | 1,003 | `C889B3519CFCAA1A70CCC688EBDC4FD1609DAF11820469A139469895B3136B1B` | `5A672FEB30559F607FE5876BF73A71C1B4E5AA2A746619795CA065077866AA4A` |

The candidate files retain their candidate standing. This review neither
generated nor promoted a lookup surface.

## Dependency and evidence boundary

Direct hashes confirmed that `handbook/main.tex`, `handbook/bib/handbook.bib`,
the P17 body/annex drivers, and both Kamp Lemma 1 and Lemma 2 body/annex
pairs still match the identities in the preceding publication review.
Those unaffected components require no mathematical reopening from this
alias repair. No conclusion about a separate P5 change is made here.

The complete inverse comparison also preserves all body status fields and
annex backreferences inside the four edited manuscript files. The lead
reported that its existing scanners, symbol/bibliography checks, fifteen
reciprocal proof-pair checks, and generator passed. Those reported runs
were not rerun or adopted as independently executed evidence by this
reviewer. The result here rests on the actual guard definitions, exact
whole-file inverse digests, token search, and changed-entry inspection.

The separate mechanical FAIL recorded in the initial Kamp/P17
publication-text report is resolved by the current P17 body, annex, CSV,
and candidate hashes above. Its earlier independent content verdict is
preserved through the demonstrated exact expansion. Any valid prior P16
source or topic evidence is likewise preserved through exact unchanged
content and notation, within that evidence's original scope; this review
does not independently decide whether a separate prior verdict was valid.

## Auxiliary read manifest and execution boundary

The four complete manuscript contents and the three complete registry or
candidate contents were consumed for inverse comparisons; the source
locations inspected for meaning are listed above. Complete-file hash
comparison is distinguished from rereading the entire P16 exposition.

| Additional file | Actual inspection | SHA256 |
| --- | --- | --- |
| `handbook/handbook.sty` | 815-854 and 1067-1072; current full hash | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `spec/research/edition-2026-p16-c1-finite-abduction.md` | Exact old-hash rows 16-17 | `EB9249557B75E8CD6B2C1E43237E4A01C66DCAAC44778EB06A6D120F69B5B8B6` |
| `handbook/parts/p16.tex` | Full 1-4 | `B8462255C289FBCA14A9296EE8F7567C524A7ABFAC44FC5BB5F681AA3997C64E` |
| `handbook/annex/p16.tex` | Full 1-3 | `F60E8A47B426A42C69DFC8D903F308FA7654269A7E8CEFD95FF03B9B85D0883D` |
| `handbook/parts/p17.tex` | Full 1-4 | `94B1A39026E95CECE627D0025CA86D6FA1F799712235A32F410A114B92F0D3F2` |
| `handbook/annex/p17.tex` | Full 1-3 | `CDFB2B0555402278C57DCBDCCD060D79BFEFA37186288DCEB73F503A92868F85` |
| `handbook/main.tex` | Full-file hash comparison only | `5EBDFF789C4DF7B7CFF7DCBFE713F63555EC2543108D17C810BCA2B0B5EE2639` |
| `handbook/bib/handbook.bib` | Full-file hash comparison only | `1B3D00B8336DE9A654EC074F6BBA6F8542A93F609736A98FEDB25F70A41EB27A` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | Full-file hash comparison only | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | Full-file hash comparison only | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex` | Full-file hash comparison only | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| `handbook/annex/p09/kamp-iii2-lemma2.tex` | Full-file hash comparison only | `75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2` |

Only this assigned report was written, after exact-path permission was
obtained. No manuscript, style, checker, registry, generator output, or
other review report was edited. No other current reviewer report was read.
No tests, build, render, source-PDF inspection, or formal admission was
performed. No remaining repair is required within this focused alias
preservation scope.
