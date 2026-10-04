REVISE

# Round-one adversarial publication/AGENTS review: N-c-012.d

## Identity, independence, and method

- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Runtime model/version: not exposed to this reviewer.
- Role: adversarial publication and AGENTS-compliance seat.
- I read the complete board charter before substantive review and used only the frozen round-one snapshot named there.
- I did not inspect `spec/research/boards/p09-n-c-012d/ledger.md`, `transcript/chair.md`, another reviewer's transcript, or another reviewer's verdict, and I did not contact another reviewer.
- I made no manuscript, shared-file, source-note, source-ledger, bibliography, source, or build-artifact edit. This transcript is the only file I created.
- The review used visual primary-source reading, mathematical reasoning, prose inspection, and SHA-256 identity checks only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen identities verified

I computed every frozen SHA-256 before substantive review and rechecked every one after completing the source and prose audit. Both checks matched the charter exactly:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A4E1059FB5AE5BB577C76B443D05A26BF31F711449C7537B71027F7E72A958CC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `5F3903C0793116D497B86FB8DC06CE6AF2DE6B8FA71C727D74F10054F8905A14` |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `CF865B89EA3C6C5DF44E9D900D203441B015AF2977F1F383246C52431FCAB533` |
| `spec/research/p09-source-presentations-lot2-3.md` | `E2012A854194277F8C4CC964872428454B2ADEA3624DEE97536833868E37CCE9` |

## Authority-page reading record

I visually read the complete journal facsimile, printed pp. 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, and 749. I also visually read the complete conference predecessor, printed pp. 159, 160, 161, 162, 163, 164, 165, 166, 167, and 168. I separately inspected the enlarged p. 742 exponent crop and the controlling p. 745 image. The images controlled over OCR, memory, and the source note.

I then read the complete frozen reader subsection `handbook/parts/p09/presentations/n-c-012.tex:1851-2247`, the relevant shared temporal definitions and theorems in `handbook/parts/p09/logic-in-computer-science.tex:599-823` and the atlas entry at `:2216-2219`, the entire 758-line source note, the `N-c-012.d` source-ledger entry at `spec/research/p09-source-presentations-lot2-3.md:185-197`, the complete `SistlaClarke1985` bibliography entry at `handbook/bib/handbook.bib:2245-2259`, and enough adjacent GPSS and Alpern--Schneider text to test boundary collisions.

## Strongest publication-ready case

The frozen topic gets the central mathematics substantially right. It preserves the inclusive temporal clauses, existential `R`-path quantifier, validity reconstruction boundary, the strict/non-strict Lemma 3.3 defect, the distinct journal `2S(n)` and conference `S(n)` distances, the `2^length(f)` truth-set count, the inclusive fulfilled-before endpoint, Theorem 4.7's bounds and every-periodic-position discharge condition, the p. 745 finite/infinite typing and parity conflicts, the post-correction journal ETL chain, Table I, the complement route to universal-path model checking, and the absence of a Sistla--Clarke Büchi construction. The remaining defects are nevertheless substantive because this artifact advertises exact source reconstruction and complete conference/journal reconciliation.

## Findings

### AP-F1 — HIGH — “Ultimately periodic” is used as a load-bearing technical condition but never defined

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:2093-2112`; `handbook/parts/p09/logic-in-computer-science.tex:781-785,794-800`; `spec/research/p09-sistla-clarke-1985-source-note.md:442-489`; source: journal p. 742, with Theorem 4.7 on pp. 743-744.
- **Claim:** The reader, source note, and shared model-checking theorem repeatedly use “ultimately periodic,” while no handbook occurrence supplies an eliminable definition. The source itself defines the condition: for `S=(s,xi)`, starting index `i`, and a positive period `m`, `xi(s_k)=xi(s_{k+m})` for every `k>=i`. That valuation-period condition is not the same statement as equality of formula truth sets, and neither condition by itself discharges pending `U` obligations.
- **Evidence:** Reader lines 2093-2104 introduce “ultimately periodic structure” and immediately state bounds, but define neither the repeated finite prefix/cycle representation nor valuation periodicity. Shared lines 785 and 799 promise an “ultimately periodic counterexample” without defining what the returned witness contains. The source-note theorem block at lines 458-489 also assumes the term. Journal p. 742 prints the valuation-based definition before the loop lemmas; pp. 743-744 add the separate type-equality and until-discharge requirements.
- **Publication harm:** A first-time reader cannot tell whether periodicity concerns states, valuations, closure types, or discharged obligations. The shared algorithm also promises a counterexample representation it never types. This is a definition-before-use failure and violates the five-part rule's Definition, Standing, and Nonredundancy requirements.
- **Exact correction:** Before the first scoped use, define an ultimately periodic temporal structure as an infinite valuation sequence with a finite prefix and a nonempty repeated cycle, equivalently with `xi(s_k)=xi(s_{k+p})` for all `k>=i` for specified `i` and positive `p`. State explicitly that this is valuation periodicity; Theorem 4.7 separately requires source-truth-set equality and every pending-until discharge. In the shared product method, say that the returned lasso is a finite path to a nonempty product cycle whose infinite unfolding supplies the counterexample.

### AP-F2 — HIGH — The Section 3 presentation omits the exact quantified statements that make the pruning proof work

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:1985-2034`; `spec/research/p09-sistla-clarke-1985-source-note.md:282-370`; source: journal pp. 736-739, especially Lemmas 3.2, 3.3, and 3.6.
- **Claim:** The reader says that equal prefixes/ranges are indistinguishable and that Lemma 3.3 selects a bounded acceptable subsequence, but it omits the source's load-bearing hypotheses and preservation quantifiers. Lemma 3.2 requires equal initial lengths, pointwise equal initial valuations, a special equal-first-valuation clause when both initial lengths are zero, and equal recurring ranges. Lemma 3.3 quantifies over an acceptable input subsequence, a negation-normal `L(F,G)` formula satisfied at the relevant retained positions, an acceptable output subsequence, and every intermediate structure obtained by placing a sequence between the selected subsequence and the original while restricting the valuation; its guarantee applies at the surviving relevant positions. The literal strict bound and proof-supported non-strict repair belong to that exact statement. Lemma 3.6 likewise requires a finite selected subsequence containing the current state and preserves truth in every intermediate supersequence, not merely “a linear number of next-sensitive positions.”
- **Evidence:** Reader lines 1985-1995 reduce Lemmas 3.1-3.3 to prose slogans, then discuss the inequality at lines 1997-2007; lines 2031-2034 mention Lemma 3.6 only as preserving next-sensitive positions. The source-note dependency list at lines 287-300 and 354-359 confirms the omitted clauses but also stops short of giving the reader their exact quantified form. The printed statements and proof architecture are on journal pp. 736-739.
- **Publication harm:** Without the intermediate-supersequence quantifier, the extraction lemma looks like ordinary model thinning and does not justify inserting selected witnesses back into a larger sequence during the induction. Omitting Lemma 3.2's zero-prefix case conceals a necessary boundary case. A reader cannot reconstruct why the size argument yields Theorems 3.4, 3.5, and 3.7. This fails C3's requirement of exact Lemmas 3.1-3.3 and the source presentation's own “exact proof chain” standing.
- **Exact correction:** Add compact, fully quantified statements of Lemmas 3.2, 3.3, and 3.6 before using their consequences. Preserve the source's sequence/subsequence typing, valuation restriction, all intermediate-supersequence quantifiers, and position scope. In Lemma 3.3 display the literal `< mu(f)` first, then separately give the proof-supported `<= mu(f)` repair already explained at lines 1997-2007.

### AP-F3 — MEDIUM — The claimed complete conference/journal reconciliation omits the predecessor's printed validity definition

- **Location:** `spec/research/p09-sistla-clarke-1985-source-note.md:653-681`; `handbook/parts/p09/presentations/n-c-012.tex:1959-1968`; `spec/research/p09-source-presentations-lot2-3.md:191`; sources: conference p. 160 and journal pp. 734-735.
- **Claim:** The journal correctly is reported as printing no standalone formal validity clause, and the handbook correctly labels its universal clause as reconstruction. But conference p. 160 expressly defines satisfiable by an existential structure/point quantifier and valid by a universal structure/point quantifier. The source note calls its table a complete list of material conference/journal differences while omitting this change.
- **Evidence:** Source-note lines 653-658 assert complete material reconciliation; no row at lines 660-681 records the predecessor's validity clause. Reader lines 1959-1968 and ledger line 191 discuss only the journal omission. Visual comparison of conference p. 160 with journal pp. 734-735 establishes the version difference.
- **Publication harm:** The current wording makes the handbook's reconstruction appear to have no source precedent and makes the “complete” version comparison false. It also hides a useful explanation for why Table I retains a validity column after the formal clause disappeared from the journal exposition.
- **Exact correction:** Add a reconciliation row: the conference p. 160 formally defines both satisfiability and validity; journal pp. 734-735 define satisfiability and the two principal decision problems but do not restate validity. Add one reader boundary sentence making clear that its displayed universal clause agrees with the predecessor's printed definition but remains a reconstruction relative to the controlling journal text.

### AP-F4 — MEDIUM — The computation-history reconstruction omits the journal's terminal-configuration persistence convention

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:2049-2058`; `spec/research/p09-sistla-clarke-1985-source-note.md:389-457,605-616,653-681`; source: journal p. 741 and conference p. 164.
- **Claim:** Journal p. 741 explicitly assumes that after the deterministic machine enters `VA` or `VR`, it remains in that state and no longer changes the tape. That convention totalizes a halting computation into the infinite sequence of instantaneous descriptions required by temporal semantics. Conference p. 164 instead describes the machine as halting in its accepting or rejecting state. Neither the reader nor the note's “complete” version table records the journal convention or this difference.
- **Evidence:** Reader lines 2049-2057 describe paths coding successive instantaneous descriptions but never say how a halting accepting run becomes infinite. The Section 4 source-note chain and Figure 2 account similarly omit the convention, and the comparison rows at lines 660-681 contain no machine-terminal-state row. The sentence is printed immediately before the journal p. 741 reduction; the conference wording is on p. 164.
- **Publication harm:** A skeptical reader is left with a type gap: the reduction starts from a halting acceptance problem but its temporal structures are infinite. The omitted source convention is precisely what closes that gap. The omission also defeats C7's complete version reconciliation.
- **Exact correction:** Add to the reader's Lemma 4.4 paragraph the journal assumption that `VA` and `VR` are absorbing configurations with unchanged tape. Add a conference/journal comparison row distinguishing conference halting language from journal persistence. Report this as a version difference, not as the particular conference error that the authors leave unidentified.

### AP-F5 — MEDIUM — “Source proof tree” and “derivation tree” are unsupported synonyms for the source's tree `Gamma`

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:2177-2186`; `spec/research/p09-sistla-clarke-1985-source-note.md:540-552`; `spec/research/p09-source-presentations-lot2-3.md:195`; source: journal pp. 745-746.
- **Claim:** The journal introduces `Gamma(S,j,N_i)` simply as a labelled tree with the printed root and continuation-child construction. The reader upgrades it to “source proof tree” and “labelled proof tree”; the note calls it a “labelled finitely branching derivation tree”; the ledger repeats “derivation-tree edges.” No ambiguity requires these added technical names, no difference from the existing word “tree” is defined, and “proof tree” wrongly suggests a proof-calculus object.
- **Evidence:** Reader lines 2177-2184 contain both new phrases. Source-note lines 540-547 and ledger line 195 introduce the third phrase. Journal p. 745 defines `Gamma` as a tree and uses it in Lemma 5.1 on pp. 745-746; it does not give the extra proof-tree/derivation-tree taxonomy.
- **Publication harm:** The synonyms fail the five-part rule's Necessity and Nonredundancy conditions and can make readers infer an unprinted derivability semantics. Cross-file naming is also inconsistent.
- **Exact correction:** Replace all three phrases with “the labelled tree `Gamma(S,j,N_i)`” or “the tree `Gamma`.” Retain the exact root, continuation-edge, and separate finite-terminal-witness clauses; those definitions already provide its standing and use without inventing a new tree species.

### AP-F6 — LOW — The source-note page map mislocates the Section 3 sequence measures

- **Location:** `spec/research/p09-sistla-clarke-1985-source-note.md:125-127`; source: journal pp. 735-736.
- **Claim:** The page map assigns `init`, `final`, `range`, and `size` to printed p. 736. They are introduced at the bottom of printed p. 735; p. 736 begins with Lemma 3.1 and continues through the start of Lemma 3.3.
- **Evidence:** Visual inspection of journal pp. 735-736. The map's p. 735 row mentions only that Section 3 begins, while the p. 736 row claims the definitions.
- **Publication harm:** A reader following the evidentiary locator lands a page late, and C8 requires an accurate source-note page map.
- **Exact correction:** Move `init`, `final`, `range`, and `size` into the p. 735 row; make the p. 736 row begin with Lemmas 3.1-3.3.

## Criterion-by-criterion disposition

- **C1 — checked clean.** Work identity, printed plural title and author order, volume/issue/date/pages, DOI, ISSN, receipt history, separate STOC object, institutional acquisition, file identities, and the limited rights-to-read boundary agree with the two facsimiles and bibliography.
- **C2 — checked clean.** The syntax, fragment standing, inclusive `U/S`, structures, existential `R`-truth quantifier, universal-program counterexample route, and journal-validity reconstruction are correct. AP-F3 concerns the omitted predecessor comparison, not a false journal clause.
- **C3 — REVISE.** AP-F2 omits exact load-bearing hypotheses and quantifiers from Lemmas 3.2, 3.3, and 3.6. The printed Lemma 3.3 conflict, Theorem 3.4 bound, NP classifications, and both diamond/witness routes otherwise check clean.
- **C4 — REVISE.** The reduction chain, stuttering scope, `2S(n)`, closure/count distinction, fulfillment endpoint, Theorem 4.7 bounds/obligations, `Ff` move, initial-since check, and Savitch step are correct, but AP-F1 leaves “ultimately periodic” undefined.
- **C5 — REVISE.** Grammar semantics, finite/infinite typing disclosure, parity conflict, closure, edge conditions, terminal/continuation separation, Lemmas 5.1-5.2, Theorems 5.3-5.4, continuation-set emptying, and correction calibration are mathematically correct. AP-F5 introduces unsupported and inconsistent names for `Gamma`.
- **C6 — checked clean.** Table I rows, the Theorem 4.1/Table I distinction, `L(U) subseteq L(U,X) subseteq L(U,S,X)`, existential-counterexample complement route, and the shared PSPACE theorem are correct.
- **C7 — REVISE.** AP-F3 and AP-F4 are material omissions from a comparison expressly claimed complete. The manuscript otherwise does not transfer conference numbering or claim a uniquely identified repair.
- **C8 — REVISE.** Bibliography, citations, proof-status table, source-ledger status, provenance, and rights language are sound, but AP-F6 gives an incorrect page-map locator and AP-F3/AP-F4 make the completeness claim too strong.
- **C9 — REVISE.** The prose is generally independent and source-candid, but AP-F1, AP-F2, and AP-F5 are definition-before-use, first-reader sufficiency, exactness, and five-part-name failures.

## Invariant-by-invariant disposition

- **I1 — satisfied.** Scholarship/prose method only; prohibited test/build activity was not performed.
- **I2 — satisfied.** Every frozen identity matched before and after review.
- **I3 — satisfied.** All 17 journal pages and all 10 conference pages were visually read; images controlled.
- **I4 — satisfied.** The p. 742 exponent is `2^length(f)`; the p. 745 typing and parity conflicts are preserved.
- **I5 — satisfied.** The journal controls, numbering is separated, and no unique bad conference inference or uniquely repairing lemma is claimed.
- **I6 — satisfied.** Languages, inclusive operators, existential truth, satisfiability, and reconstructed validity remain distinct.
- **I7 — REVISE through AP-F2.** The size measure and acceptable-subsequence definition are correct, and the strict/non-strict defect is candid, but the exact extraction lemma's quantifier architecture is not visible.
- **I8 — satisfied.** Journal `2S(n)`, `card(SF(f)) <= 2 length(f)`, `2^length(f)`, and inclusive fulfilled-before witnesses remain distinct.
- **I9 — satisfied subject to AP-F1's missing base definition.** Theorem 4.7's exact numerical bounds, periodic-position discharge, `Ff` move, initial-since condition, and Savitch step are all present at source strength.
- **I10 — REVISE through AP-F5.** ETL typing, normalization, closure, exact `Gamma` edges, finite termination, Theorems 5.3-5.4, and continuation sets are present, but unsupported proof-tree/derivation-tree names violate the terminology boundary.
- **I11 — satisfied.** Proof sketches, asserted inductions, abbreviated cases, and brief replacements are not inflated; no Büchi translation is attributed to the paper.
- **I12 — REVISE.** AP-F1 fails Definition/Standing/Nonredundancy for “ultimately periodic”; AP-F5 fails Necessity/Nonredundancy for the added tree names.
- **I13 — satisfied.** Review independence and file ownership were maintained.
- **I14 — satisfied.** This verdict does not defer to majority rule; the defects keep the snapshot open.
- **I15 — satisfied.** No claim closes Alpern--Schneider, N-c-012 as a whole, Part IX, publication build/render inspection, human review, final-book completion, or user acceptance.

## Mandatory-check disposition

- **M01 — checked clean:** the enlarged p. 742 image prints `2^length(f)`, not `2^(2 length(f))`; reader lines 2073-2080 are exact.
- **M02 — checked clean:** journal pp. 734-735 contain no formal validity clause; reader lines 1959-1967 explicitly mark the universal clause as handbook reconstruction. AP-F3 separately records the omitted conference difference.
- **M03 — checked clean:** journal p. 742 uses `j>=i`, and the right witness ranges inclusively from `i` through `j`; reader lines 2082-2089 preserve both.
- **M04 — checked clean:** journal pp. 736-737 literally print `<`; the zero/zero atomic basis and all proof uses support `<=`; Theorem 3.4 is non-strict. Reader lines 1997-2007 disclose rather than silently repair it.
- **M05 — checked clean:** journal p. 742 prints `2S(n)` and conference p. 165 prints `S(n)`; reader lines 2052-2054 preserve the version split.
- **M06 — checked clean:** Theorem 4.7 has `i<=2^(1+length(f))`, `p<=4^(1+length(f))`, and fulfillment for every `k>=i`; Theorem 5.3 has `l<=2^(1+card(SF(f)))`, `p<=c^card(SF(f))`, and both obligation families at every periodic position.
- **M07 — checked clean:** p. 745 says finite or infinite and prints the unrestricted nonnegative index; reader lines 2150-2155 label the represented-position restriction as handbook-supplied typing.
- **M08 — checked clean:** p. 745 prints `N_0 -> a_1 a_2 N_0`, says even states, and its zero-based clause places the second argument at odd offsets; reader lines 2160-2169 preserves the unresolved conflict.
- **M09 — checked clean modulo AP-F5:** the ETL closure, `Gamma` root, continuation-production child condition, and separate terminal-production witness are exact. The remaining defect is the unsupported name attached to the correctly defined tree.
- **M10 — checked clean:** finite-tree maximum depth is kept distinct from until fulfillment, and the continuation-nonterminal set must become empty within the guessed period.
- **M11 — checked clean:** p. 748 says the conference proof used an erroneous theorem but does not isolate the inference or a unique new repair; reader lines 2209-2213 is calibrated.
- **M12 — checked clean:** all proof-status qualifications match the printed source; the article contains no Sistla--Clarke Büchi construction.
- **M13 — checked clean:** the exact containment supplies PSPACE hardness and membership for the Table I `L(U,X)` row without inventing a numbered theorem.
- **M14 — checked clean:** universal-path model checking is the complement of existential truth for the negated formula, with polynomial-space closure under complement; the source problem's quantifier is not changed.
- **M15 — REVISE through AP-F5:** acceptable subsequence, source truth set, both fulfilled-before obligations, and the ETL constructor each receive necessity, definition, standing, nonredundancy, and use. `Gamma` itself is exactly constructed and used, but “source proof tree,” “labelled proof tree,” and “derivation tree” are unnecessary, undefined extra names.

## Premortem

Assume this snapshot shipped and then failed scholarly review. The likely cause would not be the headline PSPACE classification; those bounds are unusually well checked. It would be a source-critical reader noticing that an advertised exact presentation uses an undefined loop notion, suppresses the quantifiers that make the Section 3 induction valid, and calls a conference/journal comparison complete while omitting two differences that close real semantic gaps. A theorem-number-and-bound checklist could miss all three. The five-part technical-name audit also catches the quieter failure: “proof tree” and “derivation tree” import a proof-calculus standing the source never supplies. These are publication defects, not copyediting preferences.

## Narrow closure boundary

The frozen snapshot remains open pending correction of AP-F1 through AP-F6 and a fresh independent review of one newly frozen identity. Even a later acceptance could close only N-c-012.d topic-level AI review. It would not close Alpern--Schneider, N-c-012 as a whole, Part IX admission, the final post-freeze publication build, rendered inspection, human review, final-book completion, or user acceptance.

REVISE
