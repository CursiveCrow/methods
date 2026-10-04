# Standard PA and finite argumentation: bounded publication-text R2

Date: 2026-09-07. Reviewer: `standard_pa_argumentation_publication_review`. Read/check interval: approximately 22:33--22:37 UTC, within the assigned 15-minute block. Repository: `C:\Dev\the-methods-of-reason`.

**VERDICT: PASS for closure of R1 F1 and F2 in P18 and for the added P15 correction scope at the final hashes below.** The P18 chapter label, both reference consumers, and all three definition signs are corrected. The analogous P15 label correction passes. This recheck found one malformed P15 control word, recorded as F3 below; the integrator corrected it during the block, and the independent final recheck closes F3. Exact inverse hashes pass for all five affected files, including the final P15 body with its one required command delimiter.

This is a bounded correction recheck. The existing R1 substantive assessment is retained for the unchanged mathematical content of its four targets. P15's earlier content acceptance was supplied as two baseline hashes; this reviewer checked the exact correction delta and its editorial behavior and did not independently rereview the entire P15 treatment.

## Finding closure and added scope

| Scope | Result | Evidence |
| --- | --- | --- |
| R1 F1: P18 chapter-label grammar | CLOSED / PASS | Body line 3 now declares `sec:p18-finite-argumentation`; it is an allowed `sec:` label and occurs once. |
| R1 F1: dependent P18 references | CLOSED / PASS | P18 annex line 5 and P8 supplement line 714 now name that exact label. No old `ch:p18-finite-argumentation` label/reference remains in the searched handbook TeX files. |
| R1 F2: P18 definition sign | CLOSED / PASS | Body lines 30, 32, and 56 contain three actual `\defeq` tokens, with no literal `:=` and no longer `\defeq...` control word. |
| Added P15 chapter-label correction | PASS | Body line 3 declares `sec:p15-finite-probability`, and annex line 7 names it. The separate preexisting `sec:p15-finite-probability-space` label is preserved. |
| Added P15 definition-sign correction | CLOSED / PASS after F3 correction | The final body has 21 actual `\defeq` control words, including the delimited `\defeq a(x)b(y)` at line 253. There is no longer control word beginning `\defeq` and no literal `:=`. |
| Exact inverse preservation, all five affected files | PASS | In-memory reversal of only the specified edits recovers all five supplied prior SHA-256 hashes. |
| R1 PA targets and shared notation/bibliography/candidate views | PASS, unchanged | Current hashes equal the R1 hashes listed below. |

### F3 — P1, CLOSED: the initial P15 sign replacement absorbed the following variable into a control word

Location: `handbook/parts/p15/finite-probability.tex:253`, initially supplied SHA-256 `76921D7B125F1FAD4DC08DBAFE25DB6ECA67478133D5653A779138F7AD72EBC3`.

The initially supplied snapshot contained:

```latex
finite nonempty sets, the assignment \(p(x,y)\defeqa(x)b(y)\) is a mass
```

TeX reads the consecutive letters after the backslash as the control word `\defeqa`. The intended sequence is the registered `\defeq` followed by the function name `a`. The handbook's `.tex`/`.sty` search finds this occurrence and no definition of `\defeqa`; the style defines `\defeq` at `handbook/handbook.sty:202`. The result is an undefined control sequence at this mathematical statement, and the intended `a` is part of that malformed command token.

Required correction: delimit the command, for example `p(x,y)\defeq a(x)b(y)` or `p(x,y)\defeq{}a(x)b(y)`, and verify its tokenization and exact inverse hash.

The other 20 P15 sites are bounded by a backslash, brace, or other nonletter, so this scan found no second merged control word. No compilation was run in this review; the finding is established by the actual source and TeX's control-word syntax.

**Independent closure at approximately 22:37 UTC:** the integrator changed line 253 to `p(x,y)\defeq a(x)b(y)`. The final body SHA-256 is `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1`. This reviewer read that exact line, verified 21 complete `\defeq` tokens, zero `\defeq`-prefixed longer control words, zero literal `:=` signs, and exactly one `\defeq a(x)b(y)` site. Reversing this one delimiter as well as the declared sign and exact chapter-label changes recovers the prior accepted body hash `130943C2394584116D11FD6F794FA12B3DBD1588DC84FF5AB242C12741CF9905`. F3 is closed for that final body. The integrator's separate scoped P15 output validation must use this corrected hash.

## Exact inverse-hash evidence

All transformations occurred in memory. Raw file bytes were decoded as UTF-8, the complete braced chapter-label/reference name was reversed, and only in the two body files the `\defeq` replacement substrings were changed back to `:=`. In the final P15 body, the one delimited `\defeq a(x)b(y)` occurrence was first returned to `:=a(x)b(y)`. The transformed bytes were hashed without writing a reconstructed manuscript file. Full label names were matched through their closing brace, preserving P15's longer `...-space` label.

For the supplied P15 snapshot, changing the substring `\defeq` back to `:=` also reconstructs the original adjacent `:=a` at line 253. This explains how byte preservation can pass while the current TeX control word is malformed.

| Affected file | Reviewed current SHA-256 | Exact inverse SHA-256 | Matches prior |
| --- | --- | --- | --- |
| `handbook/parts/p18/finite-argumentation.tex` | `82F4470C79926E92CE483A17109781F776EDBCFCE608CCC279A6C1EC711DB39B` | `685A2D6BF0125A07A5C85AEC0DA22CA9866B9799202750C758CA8BC1062C85AC` | Yes, R1 body |
| `handbook/annex/p18/finite-argumentation.tex` | `99CCF0F45660A81136F10841BC2FBE4CA2687463367E23F3B884B798839508BD` | `1B70FD5FA52B42BBCBA76976D484A0E2DFD1A67EDEEDDD1BB5D88713F9509BAA` | Yes, R1 annex |
| `handbook/parts/p08/relevance-linear-supplement.tex` | `D6AD525EF6FAB84C26F80E10BA8E4AC4DA24EB9EB0FCE8F4C828AE18538E1BCD` | `3BE8D33DFB3066EE682FBB77D42723681F14C2A342D80461F68306FACA1CF9D1` | Yes, R1 pointer consumer |
| `handbook/parts/p15/finite-probability.tex`, initial supplied snapshot | `76921D7B125F1FAD4DC08DBAFE25DB6ECA67478133D5653A779138F7AD72EBC3` | `130943C2394584116D11FD6F794FA12B3DBD1588DC84FF5AB242C12741CF9905` | Yes, supplied accepted body; F3 initially open |
| `handbook/parts/p15/finite-probability.tex`, final corrected snapshot | `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1` | `130943C2394584116D11FD6F794FA12B3DBD1588DC84FF5AB242C12741CF9905` | Yes, supplied accepted body; F3 closed |
| `handbook/annex/p15/finite-probability.tex` | `7CE651CE52FE8BFA66E5BEC221BDF48EE6318538E6A99B8E987E18C90D6B67F3` | `EA7BD4AA1783E4D94AB92B209E80517E62723524ADF4F1EEC4650B1D40DDDDB0` | Yes, supplied accepted annex |

Therefore no additional byte changes to statements, proofs, numbers, examples, or surrounding prose occur in the five affected files beyond the specified label and definition-sign substitutions and the final one-space TeX command delimiter. Both final chapters' substitutions have the intended TeX tokenization. This preservation check and F3 closure supply correction evidence; output acceptance remains a separate check.

## Actual editorial definition-sign behavior

The unchanged `handbook/handbook.sty:202` defines `\defeq` as `\mathrel{:\equiv}`. Its inherited-source override to `\mathrel{:=}` occurs inside the standard LaTeX environment `inheritedrestorationscope`, introduced at line 1385; lines 1513--1517 explicitly localize that override and restore the editorial meaning on group exit. The global symbol record remains `handbook/registry/symbols.csv:32`.

P18's direct part driver inputs the chapter outside a restoration scope. P15's complete seven-line body driver declares stable `p15` and uses an ordinary group solely for `\emergencystretch`; it introduces no definition-sign override. Its six-line annex driver likewise adds only the layout group. Consequently the actual `\defeq` tokens at the final reviewed sites invoke the registered editorial relation. The initial `\defeqa` defect is removed by the verified delimiter correction.

The live label grammar in `tools/check.py:181--182` still permits `sec:` and excludes `ch:`. The two chapter labels are unique, and the three known dependent chapter references name their corrected targets. This inspection does not claim execution of the static checker.

## Unchanged dependencies and read manifest

The R2 read scope comprises every changed site in the five affected files, the global occurrence search for the exact old/new chapter labels and references, the complete P15 body/annex drivers, the definition-sign and restoration-scope implementation excerpts, and the label-prefix implementation. All five affected files were consumed in full as raw bytes for the exact inverse-hash calculation. Their mathematical prose was not reread in full in R2.

The following current hashes match R1:

| File | SHA-256 |
| --- | --- |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/registry/symbols.csv` | `68F4AC51276F2F238BC22D4549A1CFC110914961FE15401D5FF31665F72ACDBB` |
| `handbook/bib/handbook.bib` | `417399F8D66B5D7285B6B98DA4C2C6AF38EE1D1510E3C56273226FC936F708B7` |
| `tmp/edition-2026-standard-pa-argumentation-candidate/symbols-tables.tex` | `8F5ECA50181E2D4D69AEB6305033D30108F097A0AA2437D7AC8F32F7CE722403` |
| `tmp/edition-2026-standard-pa-argumentation-candidate/symbol-index.tex` | `D7BCBC6F491988655F009F134C0D9B19F16556E54A19202C0AF00F03964A3F80` |
| `handbook/handbook.sty` | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `tools/check.py` | `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914` |

The newly inspected P15 driver hashes are:

| File | SHA-256 |
| --- | --- |
| `handbook/parts/p15.tex` | `234902D78F435603CC88523F5D7B19C21CA7E444730A92BAC91B8871C4AB0781` |
| `handbook/annex/p15.tex` | `E8EC3BEEAEDAEFAA4E17F4C69EC6E3F48D44E3EC37046EFD2455DF408107D5AA` |

Only this R2 report was written by the reviewer. No manuscript edit, broad test, build, render, generated-view promotion, or subagent was used by this reviewer. R1 F1/F2 close for P18 at the listed corrected hashes, and F3 closes for the final P15 body hash. The initial supplied P15 body remains recorded as the defective intermediate snapshot. Formal admission, complete-part status, PT-1's arithmetic selector/internal D2/D3/GL, and full-book production remain outside this bounded result. The report's own SHA-256 is returned after filing.
