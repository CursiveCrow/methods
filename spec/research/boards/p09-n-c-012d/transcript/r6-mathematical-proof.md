ACCEPT

# Round-six mathematical/proof-correctness transcript

- Stable agent identifier: `/root/r6_mathematical_proof`.
- Runtime model/version: not exposed to this seat.
- Seat: fresh, isolated mathematical/proof-correctness reviewer.
- Frozen object: the common round-six snapshot in
  `spec/research/boards/p09-n-c-012d/charter.md`.
- Verdict basis: direct visual reading of every source page, mathematical
  reconstruction, counterexample analysis, and line-by-line prose inspection.
- Independence: I did not read `ledger.md`, `transcript/chair.md`, any reviewer
  transcript from any round, or any other reviewer's verdict; I did not contact
  another reviewer. I wrote no file other than this transcript.
- Prohibited operations: I ran no test, test harness, automated checker,
  repository script, TeX command, build, or handbook-PDF inspection. Hash
  computation and ordinary read-only source inspection were the only
  mechanical operations.

## Frozen identity

I computed SHA-256 before substantive inspection and again after completing
the source and artifact passes. All ten values matched the charter on both
passes:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B` |
| `spec/research/p09-source-presentations-lot2-3.md` | `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5` |

No identity mismatch occurred.

## Complete visual source pass

I freshly and visually read, in order, every image
`journal-page-01.png` through `journal-page-17.png`, corresponding to printed
pp. 733--749, and every image `conference-page-01.png` through
`conference-page-10.png`, corresponding to printed pp. 159--168. No page was
skipped or unread. I also separately inspected the chartered enlarged views:

- `journal-page-04-acceptable-crop.png`, confirming the preparatory strict
  acceptable-union sign on printed p. 736;
- `journal-page-10-bound-crop.png`, confirming the faint count on printed
  p. 742 is (2^{\operatorname{length}(f)});
- `journal-page-13.png`, confirming the complete printed p. 745 ETL clause,
  example, closure, labelled-tree construction, and beginning of Lemma 5.1.

The journal PDF identity controls; the page sequence, printed pagination,
title page, continuations, theorem numbering, Table I, conclusion, references,
and receipt history were continuous with that controlling object. The distinct
conference PDF identity and printed pagination likewise controlled the
conference/journal comparison.

I then read the complete frozen reader subsection
`handbook/parts/p09/presentations/n-c-012.tex:1851-2631`; the relevant shared
Part IX definition, theorem, automata-method, and model-checking context at
`handbook/parts/p09/logic-in-computer-science.tex:599-708` and
`:720-809`; both bibliography records at
`handbook/bib/handbook.bib:2245-2274`; the complete 1,060-line source note;
and the complete compact `N-c-012.d` presentation at
`spec/research/p09-source-presentations-lot2-3.md:185-387`.

## Criterion dispositions

| Criterion | Disposition and evidence |
|---|---|
| C1 | **Checked clean.** Printed p. 733 confirms plural title, Sistla--Clarke order, JACM volume/issue/date/pages, affiliations, and rights notice; p. 749 confirms receipt/revision/acceptance. The reader records the controlling journal and distinct conference boundary at `n-c-012.tex:1853-1881`; source identity, provenance, hashes, and rights limits are complete at source-note lines 1--145; the two separate bibliography objects are exact at `handbook.bib:2245-2274`. DOI/ISSN, dates, pagination, and no-republication overclaim are consistent across the frozen records. |
| C2 | **Checked clean.** Syntax, fragment standing, inclusive current-point (U,S,F), structures, interpretations, existential (R)-truth, universal counterexample relation, and the reconstructed journal-relative validity clause are exact at `n-c-012.tex:1883-1990`. They agree with journal pp. 734--735 and Table I; conference p. 160, not the journal definition pages, prints the formal validity clause. |
| C3 | **Checked clean.** The complete Section 3 definitions and ambient-relative measures occur at `n-c-012.tex:1992-2122`; Theorems 3.4--3.7 and the exact Theorem 3.5 certificate occur at `:2124-2225`. I independently checked the two null-sequence strict-sign counterexamples, the proof-supported non-strict repair, the prefix length and start-state binding, every label rule, inclusive-current (F), the literal strong-connectivity check, the loopless-singleton false acceptance, and the separately owned directed-cycle correction. |
| C4 | **Checked clean.** The exact Lemma 4.3 formulas and both pure-(U) replacements are at `n-c-012.tex:2233-2279`; the computation-history reduction and journal/conference distance distinction at `:2281-2298`; truth-set count, fulfilment, Lemmas 4.5--4.6, and periodicity at `:2300-2378`; Theorem 4.7 and all five directional/Boolean Theorem 4.1 recurrences, initial-since condition, loop closure, within-period (U) discharge, storage, and Savitch step at `:2380-2438`. Quantifiers, endpoints, and bounds agree with journal pp. 740--745. |
| C5 | **Checked clean.** ETL grammar semantics, normalization, disjoint nonterminals, one terminal/constructor arity, finite/infinite typing disclosure, parity conflict, closure, labelled tree, Lemmas 5.1--5.2, both fulfilment notions, and Theorem 5.3 are exact at `n-c-012.tex:2448-2544`. Theorem 5.4's independent encoded-input length, positive rule, negative frontier update, singleton initialization, and within-period emptiness are exact and well typed at `:2545-2598`. The source-note treatment at lines 728--873 and compact treatment at lines 306--341 are consistent. |
| C6 | **Checked clean.** The reader reproduces every Table I row at `n-c-012.tex:2600-2630`. Shared theorem `thm:p09-ltl-pspace` at `logic-in-computer-science.tex:693-708` correctly derives the (L(U,X)) classification from (L(U)\subseteq L(U,X)\subseteq L(U,S,X)). Shared model checking at `:761-809` preserves existential counterexample search and passes to universal checking by negation and PSPACE complement closure. |
| C7 | **Checked clean.** The complete ten-page/fourteen-page-content comparison is not conflated: the seventeen-page journal controls. Source-note lines 941--980 accurately distinguish formal validity, closure, restricted fragment, bounds, numbering, stuttering, (S(n)) versus (2S(n)), terminal behavior, periodic obligations, ETL proof machinery, and proof strength. The conclusion on journal p. 748 identifies only an erroneous theorem used in the conference proof, not the bad inference or a unique new repairing lemma. |
| C8 | **Checked clean.** Bibliography, citation locators, source-note page map, proof-status table, compact presentation, archive provenance, and rights boundary agree. Key evidence is `handbook.bib:2245-2274`, source-note lines 119--145, 914--980, and 1035--1060, and compact lines 185--387. |
| C9 | **Checked clean.** The reader is independently worded, definitions precede use, types and quantifiers are explicit, proof sketches remain sketches, and no unsupported automata proof is attributed to Sistla--Clarke. The five-part terminology rule is locally met for the terms and metalinguistic abbreviations inspected below. No unsupported addition, omitted qualification, or terminology blocker remains. |

## Invariant dispositions

| Invariant | Disposition |
|---|---|
| I1 | **Satisfied.** Review used only complete primary-source visual reading, mathematical reasoning, prose inspection, and hash/source identity checks; no prohibited build or test activity occurred. |
| I2 | **Satisfied.** All ten round-six hashes matched before and after review. |
| I3 | **Satisfied.** All 17 journal and 10 conference page images were freshly read; source claims were checked against those pages rather than OCR, memory, or prior verdicts. |
| I4 | **Satisfied.** Enlarged p. 742 shows (2^{\operatorname{length}(f)}); p. 745 preserves both the finite/unrestricted-index conflict and the even/odd conflict. |
| I5 | **Satisfied.** Journal numbering, bounds, hypotheses, and Section 5 machinery control; conference material is used only for explicit comparison, and no unique repair is invented. |
| I6 | **Satisfied.** Fragment notation, restricted fragment, inclusive semantics, existential truth, satisfiability, and reconstructed validity remain distinct. |
| I7 | **Satisfied.** `size` is a finite measure of an infinite structure; `final` is the unique maximal suffix; subsequence measures retain the ambient parameter; both strict/non-strict conflicts are disclosed without invented cause. |
| I8 | **Satisfied.** Journal (2S(n)), closure cardinality, realized truth-set count, and inclusive fulfilment witnesses are all kept separate and exact. |
| I9 | **Satisfied.** Theorem 4.7 retains periodic equality, every-periodic-position (U) discharge, exact bounds, the (Ff) move, initial-since condition, and Savitch step at source proof strength. |
| I10 | **Satisfied.** ETL conventions, typing, closure, tree, termination, Theorems 5.3--5.4, continuation search, and both printed p. 745 conflicts are exact. |
| I11 | **Satisfied.** Assertions, sketches, abbreviated cases, and brief replacements are not upgraded; no Büchi construction is attributed to the article. |
| I12 | **Satisfied.** Every introduced technical name or abbreviation inspected has local necessity, exact definition, standing, nonredundancy, and later use. |
| I13 | **Satisfied.** This seat remained blind and isolated. |
| I14 | **Satisfied.** This verdict is independent and is conditioned on this exact frozen snapshot; no majority reasoning was used. |
| I15 | **Satisfied.** The frozen records explicitly limit any acceptance to `N-c-012.d`; no broader book, build, rendered, human, or user gate is claimed closed. |

## Mandatory-check dispositions

| Check | Disposition and precise locator |
|---|---|
| M01 | **Pass.** Enlarged journal p. 742 prints (2^{\operatorname{length}(f)}); reader `:2303-2315`, source note 600--614, compact 200--213. No attribution of (2^{2\operatorname{length}(f)}) remains. |
| M02 | **Pass.** No formal validity clause appears on journal pp. 734--735; conference p. 160 does print it. Reader `:1977-1989` explicitly calls the universal clause a reconstruction relative to the journal. |
| M03 | **Pass.** Journal p. 742 and reader `:2316-2323` use (j\ge i) and witness (i\le\ell\le j), including both endpoints. |
| M04 | **Pass.** Journal p. 736 prints `<` in both the preparatory union sentence and Lemma 3.3; p. 737 uses `<=`, as does Theorem 3.4. Reader `:2067-2083` and `:2111-2131` records both null failures and the non-strict proof-supported result. |
| M05 | **Pass.** Journal p. 741 prints (2S(n)); conference p. 164 prints (S(n)). Reader `:2281-2298` gives the correct separate locators. |
| M06 | **Pass.** Theorem 4.7's (i\in\mathbb N), (p>0), (i\le2^{1+\operatorname{length}(f)}), (p\le4^{1+\operatorname{length}(f)}), and every (k\ge i) obligations are exact at reader `:2380-2400`. Theorem 5.3's (l\le2^{1+\operatorname{card}(SF(f))}), (p\le c^{\operatorname{card}(SF(f))}), and every (k\ge l) obligations are exact at `:2535-2544`. |
| M07 | **Pass.** Journal p. 745 says finite or infinite and then uses an unrestricted nonnegative index. Reader `:2468-2479` clearly owns the represented-index restriction as handbook-supplied typing. |
| M08 | **Pass.** Journal p. 745 prints (N_0\to a_1a_2N_0), says “even,” while the zero-based clause puts (P) at odd offsets. Reader `:2484-2493` preserves the conflict and chooses no authorial repair. |
| M09 | **Pass.** Exact ETL closure and every continuation edge of the labelled tree are at reader `:2495-2512`; terminal productions remain in the separate finite-witness condition. |
| M10 | **Pass.** Maximum depth and its distinct negated-grammar fulfilment are at reader `:2514-2517`; the one-layer continuation set and required emptiness within the period are at `:2572-2592`. |
| M11 | **Pass.** Journal p. 748 and reader `:2593-2598` do not identify the bad conference inference or a unique repairing lemma. |
| M12 | **Pass.** Reader `:2440-2446`, source-note proof table 914--935, and source-note 870--873 preserve all proof qualifications and deny a Sistla--Clarke Büchi construction. |
| M13 | **Pass.** Shared theorem `logic-in-computer-science.tex:693-708` uses exactly (L(U)\subseteq L(U,X)\subseteq L(U,S,X)), with hardness from the left and the upper bound from the right. |
| M14 | **Pass.** Shared model-checking theorem `:796-808` complements existential truth of the negated formula and uses deterministic polynomial-space closure under complement; it does not change the source quantifier. |
| M15 | **Pass.** Acceptable subsequence and the ambient subscripts are exact at reader `:2036-2066`; source truth sets and (U)-fulfilment at `:2300-2323`; the ETL constructor and labelled tree at `:2448-2512`. Each has definition, standing, distinction, necessity, and use. |
| M16 | **Pass.** Source-note page map 119--145 places `init`, `final`, `range`, and `size` on p. 735, conclusion only on p. 748, and references on pp. 748--749. |
| M17 | **Pass.** Conference p. 160's validity definition and the journal-relative reconstruction are recorded at reader `:1977-1989`; the correction notice is limited as required at `:1873-1881` and `:2593-2598`. |
| M18 | **Pass.** Lemma 3.2's zero-prefix condition and full conclusion are at reader `:2015-2034`; Lemma 3.3's acceptable input/output and every-intermediate-supersequence/surviving-position quantifiers at `:2085-2122`; Lemma 3.6's finite subsequence containing the current state and every-intermediate-supersequence conclusion at `:2217-2225`. |
| M19 | **Pass.** Reader `:2281-2298` states one diamond per tape cell, one complete BI-to-EI traversal per instantaneous description, repeated traversals per computation, and journal persistence without tape changes. Source-note comparison 960--961 distinguishes the conference halting language. |
| M20 | **Pass.** Reader `:2366-2378` gives exactly (i\in\mathbb N), (p>0), and complete-valuation equality for all (k\ge i), distinct from truth-set equality and both fulfilment conditions. |
| M21 | **Pass.** Shared method/theorem `logic-in-computer-science.tex:761-809` returns a finite product path plus a nonempty product cycle; infinite repetition yields the counterexample. No undefined periodicity name is used. |
| M22 | **Pass.** Reader `:2501-2508`, source-note 781--788, and compact 338--341 call `Gamma(S,j,N_i)` only the source's labelled tree (or `Gamma`); no proof-tree, derivation-tree, or continuation-tree synonym occurs. |
| M23 | **Pass.** Without consulting prior transcripts or the ledger, I rechecked every retained round-one criterion and M01--M15 against the frozen source and current artifacts. All are repaired/preserved, with no weakening. |
| M24 | **Pass.** The unique maximal suffix, exact decomposition, and structure-level measures precede use at reader `:1992-2013`, matching journal p. 735. |
| M25 | **Pass.** Ambient-relative acceptable-subsequence `init`, `final`, `range`, and `size`, plus the subscript's eliminable metalinguistic status, necessity, distinction, and later use, are complete at reader `:2036-2066`. |
| M26 | **Pass.** Preparatory strict sign, null/null counterexample, non-strict subadditivity, and definition of μ before Lemma 3.3 are at reader `:2067-2088`. |
| M27 | **Pass.** Theorem 3.5 prefix bound, subset (C), strong connectivity, connecting edge, empty initialization, increasing-length processing, every rule, and start-label acceptance are at reader `:2143-2195`. |
| M28 | **Pass.** Distinct conference and journal records are exact at `handbook.bib:2245-2274`; conference and journal citations resolve separately throughout the reader and source note. |
| M29 | **Pass.** The round-three artifact retains the source-exact preparatory strict-sign conflict and all M01--M28 dispositions; no repaired point was weakened. |
| M30 | **Pass.** Reader `:2290-2298` pins journal (2S(n)) to p. 741, conference (S(n)) to p. 164, and the broader journal reduction to pp. 741--742. |
| M31 | **Pass.** Exact label initialization and atomic/negation/conjunction/current-inclusive-(F) iff rules are at reader `:2156-2189`; acceptance, literal source check, concrete loopless-singleton false acceptance, and handbook-only directed-cycle condition are at `:2190-2214`. |
| M32 | **Pass.** Exact (g_1^x,g_2^x,g_3^x,f_x,h_1,h_2,h_3,f',f''), (L(F,X)) preservation, both self-loop-sensitive pure-(U) cases, and Lemma 4.2 use are at reader `:2233-2279`. |
| M33 | **Pass.** Lemma 4.5 removes (s_i,\ldots,s_{j-1}), retains (s_j), and preserves every common token's truth set at reader `:2324-2338`; every Lemma 4.6 hypothesis and conclusions (a),(b) are at `:2340-2364`. |
| M34 | **Pass.** Exact Boolean, (X), direction-sensitive (U/S) recurrences, initial-since, loop-entry equality, within-period (U) discharge, storage, and Savitch are at reader `:2402-2438`. |
| M35 | **Pass.** Lemma 5.2's additional negated-grammar condition and both inherited conclusions are at reader `:2517-2535`; Theorem 5.4's positive continuation/terminal iff, singleton frontier, exact present-to-next update, and within-period emptiness are at `:2557-2592`. |
| M36 | **Pass.** `label` is locally defined and distinguished at reader `:2156-2195`; the Lemma 4.3 auxiliary formula names at `:2233-2262`; successive (A,B) at `:2402-2407`; and φ at `:2572-2589`. Each is eliminable, metalinguistic, nonredundant, and used. |
| M37 | **Pass.** All supported round-three repair obligations retained in M24--M36 are present without source strengthening or silent repair; all earlier criteria/invariants/checks remain intact. |
| M38 | **Pass.** `SF(f)` is exactly defined at reader `:1905-1920`, before Theorem 3.5 first appears at `:2134`; it includes ordinary subformulas, single-negation mates, double-negation elimination, and the (2\operatorname{length}(f)) bound, distinct from the later exponential truth-set count. |
| M39 | **Pass.** The supplied start state is bound by (q_0:=\delta) before prefix and acceptance use at reader `:2143-2147`; the same binding is present in source-note 428--436 and compact 249--261. |
| M40 | **Pass.** Reader `:2179-2189` preserves the printed word “after,” explains the non-strict source-context reading from inclusive (F), gives the strict-reading (A\land FA) counterexample, and keeps it separate from the directed-cycle repair. |
| M41 | **Pass.** In the reader, (n) is terminal count and constructor arity at `:2450-2467` and remains (n) through closure, `Gamma`, Lemma 5.2, and both Theorem 5.4 rules at `:2495-2583`. Source-note 728--868 and compact 306--341 use the same arity. Compact `\bar f` is defined and fully typed at lines 322--326. |
| M42 | **Pass.** Every round-four repair obligation in M38--M41 is present, source wording remains candidly qualified, and no earlier criterion, invariant, or mandatory check is weakened. |
| M43 | **Pass.** The independent variables are now fully separated. Reader `:2457-2467` keeps (n) as terminal/constructor arity; `:2545-2556` defines (\ell_{\mathrm{in}}) exactly as total encoded formula-and-grammar input length, gives its eliminable metalinguistic standing, distinguishes it from arity (n) and fragment parameter (k), and uses it in (\operatorname{card}(SF(f))\le2\ell_{\mathrm{in}}). Both Theorem 5.4 schemas at `:2562-2583` remain (n)-ary and well typed. The same separation is explicit in source-note 826--868 and compact 306--341, with no rebinding. |
| M44 | **Pass.** The sole supported round-five arity/input-length collision is repaired across all three required records on the common round-six hashes. Fresh rechecking of C1--C9, I1--I15, and M01--M43 found no regression or weakening. |

## Mathematical stress tests and proof-strength conclusion

I explicitly tested the source and reconstruction against the three disclosed
local counterexamples rather than accepting their prose labels:

1. The empty/empty acceptable-union case and the atomic Lemma 3.3 basis give
   (0<0), confirming both printed strict signs fail and the later non-strict
   inequalities are the proof-supported statements.
2. On (q_0Rd), (dRd), with (A) true only at (q_0), the formula
   (A\land FA) confirms that the prefix `after` must include the current
   occurrence under the printed inclusive semantics.
3. On (q_0Rc), (cRd), (dRd), with (P) true at (q_0,c), the literal
   singleton (C=\{c\}) check falsely accepts (GP) under reflexive strong
   connectivity, confirming the need and exact scope of the handbook-owned
   positive-length directed-cycle condition.

I also reconstructed the loop arguments independently: complete valuation
periodicity, restricted truth-set equality, until discharge, and negated-ETL
tree termination are genuinely distinct obligations; the displayed Lemma 4.6
and Lemma 5.2 hypotheses are sufficient for their two inherited conclusions;
and the Theorem 4.1 and 5.4 on-the-fly searches enforce the direction-sensitive
recurrences and period obligations at the stated space strength. The ETL
constructor remains (n)-ary while (\ell_{\mathrm{in}}) measures the full
encoding, so every argument selector (f_k), continuation head, closure bound,
and frontier update is typed without collision.

No blocker, uncertainty, unread page, unsupported strengthening, omitted
quantifier, counterexample to the repaired handbook claims, or must-fix item
remains on this exact snapshot. This acceptance is only the independent
mathematical/proof-correctness disposition for `N-c-012.d` and makes none of
the broader closure claims excluded by I15.
