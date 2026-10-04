# Standard PA checker and finite argumentation: independent publication-text review

Date: 2026-09-07. Reviewer: fresh blind publication-text/integration context, `standard_pa_argumentation_publication_review`. Repository: `C:\Dev\the-methods-of-reason`; branch `phase4-codex`; HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The reviewed artifact is the live manuscript snapshot, including uncommitted files, identified by the hashes below.

**VERDICT: FAIL for the combined publication-text/integration scope.** Two bounded publication-convention defects remain in the P18 body: its new chapter label uses a forbidden prefix, and three new definitions bypass the registered editorial definition sign. The PA numerical treatment passes this review. The P18 definitions, statements, full proofs, six example calculations, and acceptance-query boundary pass the substantive text assessment. Neither finding identifies a mathematical counterexample.

The full edition contract and all four assigned targets were read before filing. No other new review or author conclusion was read. No manuscript, shared record, driver, or generated-view file was changed. No tests, static-check command, build, render, source acquisition, or subdelegation was performed. This report was completed before the first 15-minute checkpoint of the assigned 22:15--22:45 UTC block.

## Per-unit and integration dispositions

| Scope | Result | Basis |
| --- | --- | --- |
| P5 direct PA body, 252 lines | PASS | Typed numerical constructors and recognizer; two actual `hbtheorem` statuses; explicit source-closure transport; no internal D2/D3 claim. |
| P5 direct PA annex, 315 lines | PASS | Two distinct matching `annexitem`s contain recognition/transport and numerical proof-checker/bridge proofs. |
| P18 finite argumentation body, 289 lines | FAIL | Substantive text passes; F1 and F2 below require publication corrections. |
| P18 finite argumentation annex, 201 lines | PASS | Four full matching proofs establish every listed result and calculate all six examples. Its chapter reference must follow the F1 label correction. |
| Canonical new symbol records, CSV lines 943--955 | PASS | All 13 records have the stated numerical or finite-framework roles and stable P5.1/P18.1 scopes. |
| Corresponding isolated table/index records | PASS | All 13 glyphs, scopes, notes, and entry identities agree with the canonical rows. This is text inspection of the isolated views. |
| Reader notation convention | FAIL | F2: three literal `:=` definitions in new editorial P18 text conflict with the registered `\defeq` convention. |
| Stable part ownership and bounded input routes | PASS | P5 and P18 retain stable IDs; their new inputs occur once in the inspected drivers, and the P18 annex uses stable number 18. |
| New label grammar | FAIL | F1: `ch:p18-finite-argumentation` is not in the permitted editorial prefix taxonomy. |
| Theorem-status/annex correspondence | PASS | All six body results and six annex items have exact reciprocal targets, listed below. |
| PA source/canonical boundary and P18 guarded-query attribution | PASS | The manuscript states the transports and distinguishes its own guarded query convention from Dung's extension semantics. Independent primary-source fidelity remains a different review. |
| PT-1 arithmetic selector, internal D2/D3, and GL | UNRESOLVED | Explicitly outside the proved numerical construction; no acceptance is granted here. |
| Admission, active lookup promotion, and full book production | UNRESOLVED | This review supplies no admission, static/build/visual, or release evidence. |

## Findings

### F1 — P2: the new P18 chapter label violates the active editorial label grammar

Location: `handbook/parts/p18/finite-argumentation.tex:3`, with dependent references at `handbook/annex/p18/finite-argumentation.tex:5` and `handbook/parts/p08/relevance-linear-supplement.tex:714`.

The chapter declares `\label{ch:p18-finite-argumentation}`. `handbook/CONVENTIONS.md:63--67` permits `part:`, `sec:`, `entry:`, `def:`, `thm:`, `tab:`, `fig:`, `sheet:`, `rule:`, and `annex:` and explicitly says "Nothing else." The live implementation retains exactly that prefix list in `tools/check.py:181--182`. Its plain-label scan at lines 1227--1240 flags labels outside this taxonomy unless they belong to a provenance-authorized restoration. This new P18 chapter is reached directly from `parts/p18.tex:4`, outside such a restoration scope.

Consequence: the new label is outside both the documented grammar and the actual checker's accepted prefixes. Its two references are textually resolvable at this snapshot, but resolution does not cure the grammar violation. This conclusion follows from reading the checker; no check execution is claimed.

Required correction: give this new editorial chapter a permitted label, for example `sec:p18-finite-argumentation`, and update both dependent references. Recheck that the new label occurs exactly once and both references resolve on the active route. There is no need to broaden the global taxonomy to repair this chapter.

### F2 — P3: three editorial definitions bypass the registered definition sign

Locations: `handbook/parts/p18/finite-argumentation.tex:30`, `:32`, and `:56`.

The attacker set, attacked-target set, and characteristic operator are defined with literal `:=`. The global registry record at `handbook/registry/symbols.csv:32` assigns definitional abbreviation to `\defeq`, whose editorial rendering is `:\equiv` in `handbook/handbook.sty:202`. `handbook/CONVENTIONS.md:224--226` retains that glyph ruling. The style's explicit restoration override at `handbook/handbook.sty:1513--1517` confines the inherited source's `:=` convention to its grouped provenance scope. P18 is new editorial text outside that scope, and it declares no separately typed source-local definition-sign convention.

Consequence: the chapter introduces a second, unregistered editorial definition sign while the symbol apparatus advertises the canonical one. The definitions themselves are unambiguous and mathematically correct; this is a publication-notation defect.

Required correction: use `\defeq` at these three definition sites. If an exact source-local convention is intentionally required instead, supply its explicit standing and registry record; the current text supplies neither. Revalidate the affected displayed formulas when the corrected chapter is built and rendered.

## Substantive text assessment

The PA body fixes variable and zero codes, all seven arithmetic axiom constants, sorted free-index lists, closure construction, deterministic substitution, the induction constructor, direct axiom recognition, and the direct proof-code sort before their uses. The seven displayed codes decode to the seven active Q axioms under the stated literal variable choice. The induction construction retains shadowing, permits an absent induction variable, and closes exactly the remaining free indices. The recognizer's reconstruction test rules out noncanonical closures without confusing failure of literal axiomhood with failure of derivability.

The first PA annex proves the literal self-substitution identity, both induction substitution/free-variable identities, the all-variable identity needed by the stronger existential-elimination condition, bounded recovery of the induction matrix/index, and both directions of closure transport. The whole-derivation insertion argument addresses surviving open occurrences, unmarked replacement leaves, preservation of discharge witnesses, the universal-introduction free-variable condition, and existential elimination's all-occurrence condition. Its finite row construction supplies a primitive-recursive transport bound. The reverse transport chooses a source closure with exactly the free parameter set, which is necessary for the stated occurrence-set argument.

The second PA annex preserves the inherited twenty-rule checker. Its premise-arity and parameter-length lists agree, entry by entry, with `restoration/inherited-09328-09438.tex:237--307`, including body-order implication elimination, premise-free identity introduction, explicit alpha comparison, and formula-specific nonvacuous discharge. The parent-count requirement supplies a connected actual tree; the final open-list axiom test handles temporary assumptions and the empty context correctly. The two one-row examples agree with those record conventions. The c.e.-certificate bridge proves proof existence in both directions and explicitly avoids claiming a bounded certificate search for an arbitrary source index. Distinct outer tags 19 and 16 separate the positive code sorts.

The numerical/internal boundary is stated at PA body lines 4--9 and 243--252 and annex lines 304--314. The text does not select an arithmetic representative merely because a numerical relation is primitive recursive. The existing graph-formula definition is a forward dependency for the remaining construction, not an already fulfilled selector. No claim here completes PT-1, internal D2/D3, or GL's arithmetic interpretation.

The P18 body defines attack direction, the empty argument set, self-attacks, conflict-freeness, defense, the power-set type of the characteristic operator, admissibility, and all four extension semantics before using them. It distinguishes inclusion maximality from maximum cardinality and leastness from minimality. Its grounded iteration proves a least fixed point among all fixed points, including potentially conflicting ones; conflict-freeness is then established through the admissibility invariant. The equality-index bound `k <= |A|` and the evaluation-count bound `|A| + 1` are consistent, including the empty framework.

The inclusion proofs establish stable implies preferred implies complete, preferred existence above every admissible set, and the stable-set complement characterization. All six examples were checked against their complete attack lists and the annex's admissible-set calculations. The self-attack case distinguishes no stable extension from the empty framework's one empty stable extension. The unequal-size case correctly witnesses inclusion maximality. The shared-argument case correctly has complete family `{empty, {a,d}, {b,d}}`, preferred/stable family `{{a,d}, {b,d}}`, and preferred intersection `{d}` strictly above its empty grounded extension.

At P18 body lines 251--274, nonemptiness is expressly part of this chapter's skeptical-query convention. The text separates it from unguarded universal membership over an empty family, from the family containing the empty extension, and from Dung's use of "skeptical" for grounded semantics. The framework-interpretation warning at lines 276--289 prevents extension membership from being promoted to premise truth, attack correctness, speaker credibility, or empirical adequacy. The finite chapter explicitly leaves the wider subject open.

## Proof-link manifest

| Body result | Body line | Exact status target | Annex line |
| --- | ---: | --- | ---: |
| `thm:p05-direct-pa-axioms` | 111 | `annex:p5.direct-pa-axioms` | 1 |
| `thm:p05-standard-pa-numerical-proof` | 224 | `annex:p5.standard-pa-checker` | 223 |
| `thm:p18-defense-properties` | 66 | `annex:p18.defense-properties` | 9 |
| `thm:p18-grounded-iteration` | 110 | `annex:p18.grounded-iteration` | 42 |
| `thm:p18-extension-relations` | 139 | `annex:p18.extension-relations` | 81 |
| `thm:p18-example-extensions` | 195 | `annex:p18.example-extensions` | 120 |

Every listed body status is `proved=` and every listed annex item names exactly its corresponding body result. The PA prose is retained within the two actual annex items; the P18 proofs use ordinary proof environments inside their annex items.

## Notation and route details

The new CSV records and both isolated views were read in full for the following corresponding entries. "PASS" here concerns their content and correspondence, independently of F2's definition-sign convention.

| CSV line | Content assessed | Table line | Index line | Result |
| ---: | --- | ---: | ---: | --- |
| 943 | Variable, zero, and seven numerical axiom codes | 439 | 880 | PASS |
| 944 | Increasing free-index list and universal closure | 440 | 175 | PASS |
| 945 | Governing capture-avoiding code substitution | 441 | 569 | PASS |
| 946 | Base, step, induction core, closed induction code | 442 | 77 | PASS |
| 947 | Numerical axiom recognizer and canonical PA axiom set | 443 | 442 | PASS |
| 948 | Direct tag-19 proof sort and numerical predicate | 444 | 608 | PASS |
| 949 | Finite framework, argument identifiers, attack relation | 1172 | 375 | PASS |
| 950 | Attackers and attacked targets, with local subscript omission | 1173 | 641 | PASS |
| 951 | Characteristic operator and its power-set type | 1174 | 478 | PASS |
| 952 | Grounded extension, stages, equality and evaluation bounds | 1175 | 189 | PASS |
| 953 | Complete/preferred/stable families and empty stable family | 1176 | 661 | PASS |
| 954 | All six explicit framework constants | 1177 | 378 | PASS |
| 955 | Chosen query family and nonemptiness guard | 1178 | 374 | PASS |

The records distinguish numerical codes from expressions, direct proof checking from an arithmetic formula, complete-extension `Comp` from arithmetic computation notation, the argumentation operator from temporal future notation, and families of extensions from individual extensions. Existing derivation-row fields `J,U` retain their declared list-field roles in row 899; applied `J(m,i),U(P,c)` receive their distinct function roles in rows 944 and 946.

`parts/p05.tex:19--21` closes the inherited syntax input and removes its inherited theorem hook before inputting the new PA section. `annex/p05-route.tex:14--17` exposes the P5 annex heading and the two new proof items through their file once. `parts/p18.tex:2--4` declares stable `p18`, prints one part heading, and inputs the finite chapter. Its annex uses `\hbannexchapter{18}`. The style's observed-ordinal mechanism preserves stable ownership while reflecting the construction's current printed order.

`main.tex:23--40` currently contains 16 part drivers, with P18 after P15; P16, P17, and P19 are absent and identified as pending. Its annex route at lines 46--58 follows the corresponding available body order. This is a bounded integration state and does not complete the approved nineteen-part edition. The P8 forward pointer lies at `relevance-linear-supplement.tex:712--715`, after the historical derivative block ends at line 710; P8 reaches that file at `parts/p08.tex:57`. Its destination and substantive boundary are appropriate, subject to F1.

The active lookup inputs remain `generated/symbols-tables` at `parts/p01/symbol-registry.tex:46` and `generated/symbol-index` at `parts/p14/master-tables.tex:275`. They do not input the isolated candidate directory. The inspected candidate views are not evidence of active promotion.

The bibliography contains the reused `Dung1995` article record at lines 2155--2166, with journal, volume/issue, pages, year, DOI, institutional URL, and access date. The manuscript uses source locators and distinguishes its added finite illustrations and guarded query convention. Verification of the primary PDF and exact source claims belongs to the independent source review and is not certified by this metadata inspection.

## Read and hash manifest

All hashes are SHA-256. The four assigned target hashes, canonical CSV hash, bibliography hash, and two isolated-view hashes match the supplied freeze values. The canonical CSV has 954 data rows and 955 physical lines including its header.

| Fully read assigned target | Lines | SHA-256 |
| --- | ---: | --- |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/parts/p18/finite-argumentation.tex` | 289 | `685A2D6BF0125A07A5C85AEC0DA22CA9866B9799202750C758CA8BC1062C85AC` |
| `handbook/annex/p18/finite-argumentation.tex` | 201 | `1B70FD5FA52B42BBCBA76976D484A0E2DFD1A67EDEEDDD1BB5D88713F9509BAA` |

| Governing document or integration dependency | Extent read | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Full, 168 lines | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/CONVENTIONS.md` | Full, 251 lines | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |
| `handbook/main.tex` | Full, 69 lines | `58209C822E1344274E65E10D0E9DC41D059EC7973CB63464BD7E18666E747429` |
| `handbook/parts/p05.tex` | Full, 53 lines | `7E6022FE4FBD9DC5A28554DA88B9B6CEEC02857D51E981AC0CE7171B1FD2E0D6` |
| `handbook/annex/p05-route.tex` | Full, 17 lines | `170038165BD025BCF715B8D2E7479DE6D285E6A0E2F55D02F18847A2D773FAF0` |
| `handbook/parts/p18.tex` | Full, 4 lines | `4FE13F61D5E44269CB2BD742DEA4C4AACDEAB19385F89458DC378118F8DB1EEC` |
| `handbook/annex/p18.tex` | Full, 3 lines | `EB966D58728C13A53983BB6B413AF569A106210A56983C2E9638C173BDAE0428` |
| `handbook/parts/p08.tex` | Full, 69 lines | `18A9D459D89930DD02EC3E337ACB806E4A1EB307938E4CC4E699D42428B0AF27` |
| `handbook/parts/p08/relevance-linear-supplement.tex` | Lines 690--715 | `3BE8D33DFB3066EE682FBB77D42723681F14C2A342D80461F68306FACA1CF9D1` |
| `handbook/restoration/inherited-09099-09111.tex` | Full, 13 lines | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09175-09187.tex` | Full, 13 lines | `0DB98B87928AA115C82883993E2E25B18286779E7DED0399C7148633C0178430` |
| `handbook/restoration/inherited-09328-09438.tex` | Full, 546 lines | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-09262-09327.tex` | Lines 70--145 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/scope-SRC-09328-09438.tex` | Full, 3 lines | `3D56970059846AE57BC9A1C4E150224B1D4A80F7EB7CC497BB65E33F529BD6A3` |
| `handbook/restoration/scope-SRC-09262-09327.tex` | Full, 3 lines | `65DCDECA00CACDD15A4483691054AB980AF87F178750B5852B358BBD16D12604` |
| `handbook/handbook.sty` | Definition-sign, stable-identity/status, and annex-heading implementation excerpts | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `tools/check.py` | Prefix taxonomy and plain-label checking, with surrounding relevant grammar excerpts | `05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914` |
| `handbook/registry/symbols.csv` | All lines 943--955; context lines 28--34 and 890--942 | `68F4AC51276F2F238BC22D4549A1CFC110914961FE15401D5FF31665F72ACDBB` |
| `handbook/bib/handbook.bib` | Dung1995 record, lines 2155--2166 | `417399F8D66B5D7285B6B98DA4C2C6AF38EE1D1510E3C56273226FC936F708B7` |
| `tmp/edition-2026-standard-pa-argumentation-candidate/symbols-tables.tex` | All 13 corresponding records, with group context at lines 425--449 and 1157--1181 | `8F5ECA50181E2D4D69AEB6305033D30108F097A0AA2437D7AC8F32F7CE722403` |
| `tmp/edition-2026-standard-pa-argumentation-candidate/symbol-index.tex` | All 13 corresponding records listed above | `D7BCBC6F491988655F009F134C0D9B19F16556E54A19202C0AF00F03964A3F80` |
| `handbook/parts/p01/symbol-registry.tex` | Active generated-table input line 46 | `A95B36D13BA4C61ADEF116BE5E439E43CB21B210130F14BDFE55DA773A21C8DA` |
| `handbook/parts/p14/master-tables.tex` | Active generated-index input line 275 | `D7AC8DAC67FA6253A0020A27214AE80D5DA5FB36A2E8C7B69A3CC9C79A9BCA17` |

The read manifest distinguishes full reads from support excerpts. A repository memory lookup supplied only the general discipline of frozen-snapshot review and separation of text acceptance from production acceptance; no previous acceptance result was used as evidence for these units. The report's own hash is returned externally after writing, to avoid a self-referential hash field.

## Disposition after correction

Correct F1 and F2, freeze the affected P18 body and its reference consumers, and obtain the appropriate publication-text follow-up plus output validation. Preserve the PA substantive review evidence unless its content or dependencies change. Both the independent source and topic reviews, scoped production evidence, formal admission, active lookup promotion, and final integrated-book validation retain their own requirements. This report closes none of those gates.
