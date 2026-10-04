# Kamp Lemma 2 and finite preferences: source fidelity R2 recheck

Date: 7 September 2026 Pacific time; recheck began 8 September 2026 at 00:35:46 UTC. Reviewer: `/root/kamp_preferences_source_review`. Repository: `C:\Dev\the-methods-of-reason`. This is the assigned focused recheck of the two source-reading repairs and their final source/bibliography/route/notation integration.

## Verdict

**PASS for the corrected Kamp Lemma 2 source fidelity scope.** SF-K2-01 and SF-K2-02 are resolved on the current identities below. The first report's unaffected Kamp component assessments remain applicable: the main definitions, finite recurrences, past/future splices, crossing repairs and Lin boundary have not changed.

**PASS retained for the bounded P17 finite-preference source scope.** Both P17 manuscript files and its held source PDF retain their previously reviewed hashes. The newly inspected source identity, bibliography, body/annex routes and 21 notation rows pass this scoped textual integration assessment.

There are no remaining FAIL or UNRESOLVED findings within this focused source fidelity and inspected integration scope. This does not supply topic-review, publication-review, static/build/visual or formal-admission evidence. It does not establish the rest of Kamp III.2, the complete Rubinstein book, all P17-D1, or the complete nineteen-part edition.

The predecessor report is `spec/verification/edition-2026-kamp-l2-preferences-source-review.md`, SHA-256 `C7370459FD74D57089ED9D440A29BE5A497A276E919B46C702D3FE1E8731FBB2`. Its original failure verdict remains the correct historical verdict for its original frozen files. This report supplies the subsequent decision for the repaired identities; it does not overwrite that evidence.

## Actual R2 reading and exact change verification

The repaired Kamp body was read completely, 1-212, and the repaired annex was read completely, 1-312. A combined output was truncated within the annex, so the annex was then retrieved separately and read through its final `end{annexitem}`. The original body and annex were already read completely in R1. The complete original-to-current author-note diff was read independently with `git diff --no-index`; exit code 1 indicated that the two files differ, not a failed diagnostic. Both the repair note and integration note were read completely.

No standalone original body/annex copy existed. Following the lead's explicit instruction, I reversed the known text changes **in memory only** and hashed the resulting UTF-8/LF strings. The recovered full-file hashes match the R1 originals exactly:

| Manuscript | Current SHA-256 | Hash after reversing the inspected repair hunks in memory |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma2.tex` | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` | `22ED607B6D7D0C93DAD7A6301FBA9E72BFA2B7F7F54F0603495A0B303E4696AA` |
| `handbook/annex/p09/kamp-iii2-lemma2.tex` | `75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2` | `07D126F8E22240DFC82C7F15BE9F9A5E85CE6D2E02E425F6F858E60B92958726` |

The body's four inverse replacement groups cover: the source-base attribution paragraph; the example label/title/introduction; the single formula-name change from the old literal-variant notation to CurF_A; and the final comparison explanation. The annex's six groups cover: its opening comment; the comparison paragraph heading; the formula-name change; the sentence instantiating the comparison formula; the sentence naming its temporal expression; and the final source/comparison distinction. The exact recovered hashes establish that no other manuscript text, formula, recurrence or splice changed. No original manuscript files were recreated on disk.

The PDF skill was reread completely. The complete retained 300 dpi images of Kamp printed pages 66 and 70 were inspected again with original image detail. They still visibly show `P_i(z)` and `u < z < v`, respectively. The original thesis PDF hash was recomputed and remains unchanged. This R2 primary reading adds two repeated page inspections, not a new claim to have read the full dissertation. The R1 source reading manifest remains the extent of the broader direct source comparison.

## Repair dispositions

| Finding | R2 disposition | Current evidence |
| --- | --- | --- |
| SF-K2-01: false source current-point future base | PASS / resolved | Body 86-89 now explicitly says both source bases test the predicate at the quantified witness. The new `def:p09-kamp-current-point-comparison` at line 183 introduces CurF_A as an additional handbook comparison. Its witness/current-point distinction and example are correct. Annex 286-305 uses the neutral name and removes the source-literal claim. The actual source p. 66 has P_i(z). |
| SF-K2-02: false correction of the p. 70 endpoint | PASS / resolved | Current author-note row 87 records `u < z < v` as the actual source and identifies the former y reading as the author's error. The active Bp_1 matrix and the original complete splice were preserved. The actual source p. 70 already has endpoint v. |
| Dependent source claims and historical evidence | PASS | The complete note diff updates the saved identities, overview, read-manifest description, source-disposition table, mapping, example calculation, notation intake and satisfaction summary. It records the prior wrong readings as superseded author errors. The preserved original note's SHA-256 is exactly the original `3363CA8A...` hash. |
| Residual false attribution in active scoped text | PASS | Targeted reading/search of both manuscript files, the current author note, repair note, integration note and symbol registry finds no remaining claim that the extra current-point formula is Kamp's literal future base. Remaining mentions of the old readings explicitly identify the error or its removal. |
| Mathematical comparison and unaffected construction | PASS retained | CurF_A's matrix, its temporal expression, endpoint treatment and real-order counterexample are unchanged apart from the neutral formula name and explanations. Exact inverse-hash verification preserves the complete main construction and the independent R1 assessments of indexing, Bf membership, full crossing ranges/equality, future direction and Lin/Com boundaries. |

## Source and provenance identities

All following hashes were computed directly in R2.

| File | SHA-256 |
| --- | --- |
| `spec/research/edition-2026-c7-kamp-iii2-lemma2.md` | `5CAE553AA5269730EB0569D99EB03C53C9DC95831E08E86CFD6E5C1D02C2EB89` |
| `spec/research/history/edition-2026-c7-kamp-iii2-lemma2.author-3363ca8a.md` | `3363CA8AC3673DE152C6D1D96745ED192B299C527CA3716F74AACCC1F74EA1C1` |
| `spec/research/edition-2026-kamp-l2-source-reading-repair.md` | `210465541155DA03D7E3EC8CB0B05EF66FA8AB0DB5D33CEC9929F9AD23B4715A` |
| `spec/research/edition-2026-kamp-l2-p17-integration.md` | `05985EE14F4AB84878DED0744B1C15C1A00352D2BC1DC8318CAAE7C841799199` |
| `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf` | `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA` |
| `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf` | `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8` |
| `handbook/parts/p17/finite-preferences.tex` | `7C70F6C3428EFD358BDFDD99BA03911699DD7A4A16179033B408B9F9BE2AD988` |
| `handbook/annex/p17/finite-preferences.tex` | `30FAEDDD5023D3F64A565FA669C47980DE325A2BFECB6F96ACAED9398E204FE1` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |

The current and historical notes are distinguished correctly. The preserved original author note documents the erroneous first reading and its original manuscript identities; its existence does not make those historical claims current source evidence. The active source claims are governed by the direct primary reading and explicit repair.

## Final scoped integration assessment

| Inspected item | Disposition | Actual evidence |
| --- | --- | --- |
| Kamp source key | PASS for identity/linkage | `handbook/bib/handbook.bib:2271-2280` retains Kamp1968 with the correct author, dissertation title, institution and 1968 date. The manuscript cites this key and uses the inspected printed pages. This recheck does not independently renew the inherited hosting/reproduction-rights statement. |
| Rubinstein revision-specific bibliography | PASS | `handbook/bib/handbook.bib:6608-6620` records the correct title/subtitle, Ariel Rubinstein, second edition, Princeton University Press, Princeton/Oxford, 2012 year, exact ISBN and the author-hosted revision dated 11 January 2015. Its 2007 URL filename is not represented as an edition date. These fields agree with the R1-inspected source leaves and held source hash. |
| Kamp body/annex route | PASS | `n-c-012.tex:149-150` inputs Lemma 1 and then Lemma 2. `annex/p09.tex:7-8` uses the corresponding order. The existing reciprocal lemma/annex IDs remain unchanged. |
| P17 body/annex route and stable identity | PASS | The complete four-line `parts/p17.tex` sets hbpartidentity p17, the decision/strategic title and finite-preference input. The complete three-line annex wrapper uses stable annex identity 17 and the corresponding proof input. |
| Main-driver placement | PASS for this insertion | Complete main.tex read. Body input line 37 and annex input line 59 place P17 after P16 and before P18. Eighteen active parts follow P1-P10, P15-P18, P11-P14. The explicit P19-absent construction boundary remains correct; this is not the complete nineteen-part edition. |
| Twenty-one appended typed symbol rows | PASS for source/role consistency | All 21 rows were read directly, at CSV lines 983-1003. Twelve are scoped P17.1 and nine P9.4. Their typed roles preserve the source glyph direction, diagonal completeness, quotient/alternative distinction, rank counting, attained-domain uniqueness, finite-menu hypotheses, strict limiting witnesses and the new CurF_A handbook role. Import-Csv reports 1,002 data rows. |
| Generated symbol candidates and output | UNASSESSED production gate | The lead's note reports isolated candidate generation and checks. This reviewer did not run those checks, inspect candidate rendering, or treat their reported success as publication acceptance. The textual registry assessment above concerns the actual inspected source rows. |

Exact shared-file identities verified against the integration freeze:

| File | SHA-256 |
| --- | --- |
| `handbook/main.tex` | `5EBDFF789C4DF7B7CFF7DCBFE713F63555EC2543108D17C810BCA2B0B5EE2639` |
| `handbook/parts/p17.tex` | `94B1A39026E95CECE627D0025CA86D6FA1F799712235A32F410A114B92F0D3F2` |
| `handbook/annex/p17.tex` | `CDFB2B0555402278C57DCBDCCD060D79BFEFA37186288DCEB73F503A92868F85` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `D234631589FA3B60FF1CD150713AA66CD0DBE61C8BA4F00D73462A5B3089966C` |
| `handbook/annex/p09.tex` | `B7291B20AA9147D94206FD4EFF3C33C334B5017848B73954444338CDCD31D39B` |
| `handbook/bib/handbook.bib` | `1B3D00B8336DE9A654EC074F6BBA6F8542A93F609736A98FEDB25F70A41EB27A` |
| `handbook/registry/symbols.csv` | `0F2EFCA2F92E7B967F3BE3EFA137C9DC36F9AD64BA314E987A48AD4817C4A14B` |

## Return and remaining boundary

The two required source repairs are resolved and the requested source/bibliography/route/typed-row integration is verified on the stated snapshot. The original R1 primary-page extents and P17 bounded source verdict remain unchanged. No other reviewer findings were read for this decision.

The only R2 repository write by this reviewer is this report. No manuscript edits, tests, manuscript static checks, builds, manuscript renders, source PDF writes or admission actions occurred. Exact in-memory reversal and hashing were read-only change-verification diagnostics. The two retained Kamp source-page images remain available at the R1 report's paths.

Return this R2 report to the lead. All later changes must be assessed for their actual effect on these source identities and claims. Final production and formal admission remain separate requirements.
