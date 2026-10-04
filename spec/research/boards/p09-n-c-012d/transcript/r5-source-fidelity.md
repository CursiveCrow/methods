REVISE

# Round-five source-fidelity review: `N-c-012.d`

- Stable reviewer identifier: `/root/r5_source_fidelity`
- Runtime model/version: not exposed to this reviewer.
- Review date: 2026-08-23.
- Scope: the exact round-five ten-object snapshot named in `spec/research/boards/p09-n-c-012d/charter.md`.
- Independence: I did not inspect `ledger.md`, `transcript/chair.md`, any round-one through round-five reviewer transcript, or any other reviewer's verdict. I did not contact another reviewer.
- Method: direct visual source reading, mathematical comparison, and line-by-line prose inspection only. I ran no test, test harness, automated checker, repository script, TeX command, PDF build, handbook-PDF inspection, or build. Hash computation and ordinary read-only file inspection were the only machine operations used to identify and read the frozen scholarly object.

## Frozen-object verification

I independently computed SHA-256 for all ten frozen objects. Every digest matched the round-five charter exactly:

| Frozen object | Computed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C760B8B413937A9002F017704956EBFFB2AF7ED44AD8AD8FF0EC4366E526EC79` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | exact match |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` | exact match |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `79E0677D27769153BC5C078242CDD77916350B926C87B25F91F78A9C943F0F19` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `9739EBEE2BBE5F24857B9C900F831B7F9783F5BAA00652E02E3F5DD755E08D22` | exact match |

No identity mismatch occurred.

## Complete visual source coverage

I freshly and visually read every page image, with no unread or illegible page:

- Journal: `journal-page-01.png` through `journal-page-17.png`, corresponding one-for-one to printed pp. 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, and 749.
- Conference: `conference-page-01.png` through `conference-page-10.png`, corresponding one-for-one to printed pp. 159, 160, 161, 162, 163, 164, 165, 166, 167, and 168.
- Required enlarged journal readings: `journal-page-04-acceptable-crop.png` for printed p. 736's acceptable-union strict sign and ambient-relative definitions; `journal-page-10-bound-crop.png` for printed p. 742's exponent; and the frozen enlarged `journal-page-13.png` for printed p. 745's finite/infinite-index and parity conflict.

The controlling visual readings directly confirmed, among other things, printed p. 742's `2^length(f)` rather than `2^(2 length(f))`; p. 741's journal `2S(n)` rather than conference p. 164's `S(n)`; the two p. 736 strict inequalities and p. 737's following non-strict proof uses; p. 742's inclusive fulfilled-before endpoint; Theorem 4.7's every-periodic-position condition on pp. 743--744; and the two p. 745 ETL defects.

I then read the complete reader subsection `handbook/parts/p09/presentations/n-c-012.tex:1851--2622`, the relevant shared context and both named theorems in `handbook/parts/p09/logic-in-computer-science.tex:602--809` (plus the summary row at lines 2219--2222), bibliography entries `handbook/bib/handbook.bib:2245--2274`, all 1,052 lines of `spec/research/p09-sistla-clarke-1985-source-note.md`, and the complete compact `N-c-012.d` presentation at `spec/research/p09-source-presentations-lot2-3.md:185--375`.

## Must-fix finding

### F1. The round-five ETL arity repair reuses its supposedly stable arity symbol for input length

The journal keeps the two quantities distinguishable. On printed p. 745 it first binds terminal count and constructor arity as (n) in (a_1,\ldots,a_n) and (N_j(f_1,\ldots,f_n)). Its later tree and induction prose uses a fresh local arity letter (q). In Theorem 5.4 on printed p. 747, the paper uses (n) for the **total input length** while continuing to write the constructor tuple with arity (q). Thus the source does not equate total input length with grammar-terminal count or constructor arity.

The frozen reader says that it alpha-renames the source's later (q) to (n) throughout the constructor, `Gamma`, Lemma 5.2, and Theorem 5.4 (`handbook/parts/p09/presentations/n-c-012.tex:2457--2463`). It consistently writes (N_j(f_1,\ldots,f_n)) through the tree and loop rules (`:2464--2479`, `:2495--2524`, and `:2551--2574`). But immediately before the Theorem 5.4 rule it rebinds the same symbol:

> “If the total encoded input length is (n), the paper uses \(\operatorname{card}(\operatorname{SF}(f))\le2n\)” (`handbook/parts/p09/presentations/n-c-012.tex:2545--2549`).

After that rebinding, the displayed rule still writes (N_j(f_1,\ldots,f_n)) (`:2551--2561`) and the continuation-set rule repeats that tuple (`:2563--2574`). The text therefore makes (n) denote both total input length and formula-constructor arity at the exact point where those quantities are generally unequal.

The source note repeats the defect. It declares that the p. 745 arity letter (q) is alpha-renamed to (n) throughout Section 5 and through Theorem 5.4 (`spec/research/p09-sistla-clarke-1985-source-note.md:730--744`), then rebinds (n) to total input length at `:826--830`, while its positive and negative Theorem 5.4 rules still use (N_j(f_1,\ldots,f_n)) at `:831--860`. The compact presentation correctly gives its local tuple abbreviation \(\bar f=(f_1,\ldots,f_n)\) necessity, definition, standing, nonredundancy, and use at `spec/research/p09-source-presentations-lot2-3.md:306--331`, but it cannot remove the ambiguity already present in the controlling reader and complete source note.

This is not cosmetic. It defeats the claimed eliminable alpha-renaming and leaves the constructor ill-typed unless a reader silently restores the source's (q) or invents another scope convention. It fails the exact one-symbol arity requirement in M41, the round-five repair requirement in M42, ETL exactness in C5/I10, cross-record consistency in C8, and definition-before-use/terminology precision in C9/I12.

Required repair: give input length a symbol distinct from the terminal-count/constructor-arity symbol (or choose a third stable arity symbol and use it through the constructor, `Gamma`, Lemma 5.2, Theorem 5.4, the source note, and the compact tuple abbreviation). State the two bindings locally and preserve \(\operatorname{card}(SF(f))\le2L\) for total encoded length (L), without changing the source theorem. Freeze new hashes and rereview the new snapshot.

I found no second must-fix source-fidelity defect on this snapshot.

## Criteria C1--C9

| Criterion | Disposition | Evidence and reasoning |
|---|---|---|
| C1 | **PASS** | Exact plural title, author order, JACM 32(3), July 1985, pp. 733--749, DOI, ISSN, receipt history, CMU provenance, journal/conference file identities, and rights limits are accurately separated at reader `:1853--1881`, bibliography `:2245--2274`, and source note `:35--117`. Journal pp. 733 and 749 and conference pp. 159 and 168 were read directly. |
| C2 | **PASS** | Syntax, `L(O_1,...,O_k)`, `\widetilde L(F,X)`, inclusive `U/S/F`, structures, interpretations, existential `R`-truth, satisfiability, universal counterexample relation, and reconstructed-only journal validity are exact at reader `:1883--1990`; compare journal pp. 734--735 and conference p. 160. |
| C3 | **PASS** | The complete Section 3 definitions, ambient-relative acceptable subsequences, Lemmas 3.1--3.3, both strict/non-strict conflicts, Theorems 3.4--3.7, both diamond/certificate issues, `SF(f)` definition before first certificate use, `q_0:=\delta`, inclusive prefix `F`, and the separately owned directed-cycle correction are present at reader `:1992--2225` and source note `:272--518`. |
| C4 | **PASS** | Lemmas 4.2--4.6, full Lemma 4.3 formula construction and both pure-`U` cases, p. 741 `2S(n)`, p. 742 truth-set count, exact fulfillment, deletion, loop hypotheses/conclusions, Theorem 4.7 bounds and obligations, `Ff`, all five directional recurrences, initial-since, storage, and Savitch are preserved at reader `:2227--2446`. |
| C5 | **REVISE** | The journal Section 5 content, finite/infinite typing disclosure, parity conflict, closure, labelled tree, Lemmas 5.1--5.2, Theorems 5.3--5.4, and continuation search are otherwise exact at reader `:2448--2589`; however, F1 makes constructor arity ambiguous in Theorem 5.4. |
| C6 | **PASS** | Table I is complete at reader `:2591--2621`; the `L(U,X)` Table-I/Theorem-4.1 distinction and containment proof are exact at shared lines `:693--708`; universal model checking is obtained from existential truth of the negated formula and complement closure at shared lines `:796--808`. |
| C7 | **PASS** | The journal controls, conference claims are separately cited, numbering and bounds are not interchanged, and the p. 748 correction notice is not overread as identifying a bad inference or unique repairing lemma. See reader `:1853--1881`, `:2290--2298`, `:2583--2589`, and source note `:933--972`. |
| C8 | **REVISE** | Bibliography, page map, proof-status table, locators, and rights boundary are otherwise exact (`handbook.bib:2245--2274`; source note `:119--145`, `:906--927`; compact presentation `:185--375`). F1 makes the reader/source-note ETL notation internally inconsistent with their own stated alpha-renaming and with the source's distinct input-length binding. |
| C9 | **REVISE** | The prose is independently worded and all other mandatory technical names receive local definition, standing, distinction, necessity, and use. F1 is an exact-binding and eliminability failure under the user's terminology rule. |

## Invariants I1--I15

| Invariant | Disposition | Evidence and reasoning |
|---|---|---|
| I1 | **PASS** | Review used only direct source reading, mathematical comparison, prose inspection, hashes, and ordinary read-only inspection; no prohibited test/build activity occurred. |
| I2 | **PASS** | All ten round-five hashes match exactly, as listed above. |
| I3 | **PASS** | Every journal page 733--749 and conference page 159--168 was freshly visually read. Images were treated as reading aids to the exact hashed PDFs, not as authority over a mismatched source object. |
| I4 | **PASS** | Enlarged p. 742 shows `2^length(f)`; enlarged p. 745 preserves the finite/infinite-index and parity conflicts. |
| I5 | **PASS** | Journal and conference numbering, bounds, proof language, and Section 5 are kept distinct; the correction notice is properly calibrated. |
| I6 | **PASS** | Language classes, restricted fragment, inclusive semantics, existential `R` truth, satisfiability, and validity remain distinct; the journal validity clause is expressly reconstructed. |
| I7 | **PASS** | `size`, unique maximal `final`, ambient-relative acceptable measures, both strict defects, and unknown causes are all preserved. |
| I8 | **PASS** | Journal `2S(n)`, closure cardinality, realized truth-set count, and inclusive fulfillment are all distinct and exact. |
| I9 | **PASS** | Theorem 4.7 has periodic equality plus every-position obligation discharge, exact bounds, `Ff`, initial-since, and Savitch. |
| I10 | **REVISE** | ETL's substantive machinery is otherwise exact, but F1 destroys the required consistently bound terminal/argument arity through Theorem 5.4. |
| I11 | **PASS** | Sketches, asserted inductions, abbreviated cases, and brief replacements remain differentiated; no Sistla--Clarke Büchi construction is invented. |
| I12 | **REVISE** | All other introduced names/abbreviations satisfy the five-part rule. The expressly introduced alpha-renaming of arity to (n) is not exactly eliminable after (n) is rebound to input length; its standing and later use become ambiguous. |
| I13 | **PASS** | Independence restrictions were obeyed. |
| I14 | **PASS** | The detected must-fix item yields `REVISE`; no vote or prior verdict was used. |
| I15 | **PASS** | Neither reader nor records overclaim closure of Part IX, publication build/inspection, human review, final-book completion, or user acceptance. |

## Mandatory checks M01--M15

| Check | Disposition | Direct disposition |
|---|---|---|
| M01 | **PASS** | Enlarged journal p. 742 prints `2^length(f)`; reader `:2303--2315` and source note `:600--614` reject `2^(2 length(f))` attribution. |
| M02 | **PASS** | Journal pp. 734--735 contain no standalone validity definition; reader `:1977--1990` and source note `:261--270` label the universal clause reconstructed. |
| M03 | **PASS** | Journal p. 742 prints `j >= i` and `i <= l <= j`; reader `:2316--2323` is inclusive. |
| M04 | **PASS** | P. 736 prints `<` in the union sentence and Lemma 3.3; the null failures, p. 737 `<=` proof uses, and Theorem 3.4's non-strict result are disclosed at reader `:2067--2122`. |
| M05 | **PASS** | Journal p. 741 prints `2S(n)` and conference p. 164 prints `S(n)`; reader `:2290--2293` keeps them separate. |
| M06 | **PASS** | Theorem 4.7 at reader `:2380--2400` and Theorem 5.3 at `:2535--2544` preserve every bound and every-periodic-position quantifier. |
| M07 | **PASS** | P. 745's finite/infinite statement and unrestricted index are disclosed; reader `:2468--2479` labels represented-position restriction handbook-supplied. |
| M08 | **PASS** | P. 745's `N_0 -> a_1 a_2 N_0` and even/zero-based-odd conflict are preserved at reader `:2484--2493`. |
| M09 | **PASS** | ETL closure and every `Gamma(S,j,N_i)` continuation edge are exact at reader `:2495--2512`; terminal productions remain separate finite witnesses. |
| M10 | **PASS** | Maximum tree depth and its distinct fulfillment are at reader `:2514--2517`; continuation-set initialization/update/within-period emptiness are at `:2563--2583`. |
| M11 | **PASS** | Journal p. 748 does not identify a precise inference or unique repair; reader `:1874--1881` and `:2583--2589` does not invent one. |
| M12 | **PASS** | Proof-status qualifications are exact at reader `:2440--2446` and source note `:906--927`; no Büchi proof is attributed. |
| M13 | **PASS** | Shared theorem `:693--708` uses `L(U) subset L(U,X) subset L(U,S,X)` for the exact hardness/upper classification. |
| M14 | **PASS** | Reader `:1967--1976` keeps source truth existential; shared theorem `:796--808` obtains universal checking from `neg A` and deterministic-space complement closure. |
| M15 | **PASS** | Acceptable subsequence (`:2036--2040`), ambient subscripts (`:2042--2066`), source truth set/fulfilled-before (`:2303--2323`), constructor (`:2457--2482`), and `Gamma` (`:2501--2512`) each receive definition, standing, nonredundancy/necessity, and later use. F1 is separately charged under M41. |

## Mandatory checks M16--M29

| Check | Disposition | Direct disposition |
|---|---|---|
| M16 | **PASS** | Source-note page map `:119--145` puts `init/final/range/size` on p. 735, conclusion only on p. 748, and references on pp. 748--749. |
| M17 | **PASS** | Conference p. 160's formal validity clause is recorded while the identical journal-relative clause remains reconstructed; the correction notice remains unidentified. See reader `:1977--1990`. |
| M18 | **PASS** | Exact Lemma 3.2 at reader `:2015--2034`, Lemma 3.3 at `:2088--2122`, and Lemma 3.6 at `:2217--2225` retain zero-prefix, acceptable input/output, all intermediate supersequences, surviving-position scope, current-state containment, and strict-sign disclosure. |
| M19 | **PASS** | Reader `:2281--2298` identifies one diamond per tape cell, full BI-to-EI traversal per ID, repeated traversals per computation, journal persistent terminal configurations, and conference halting wording. |
| M20 | **PASS** | Reader `:2366--2378` binds (i\in\mathbb N), (p>0), and full-valuation equality for every (k\ge i), distinct from truth-set equality and discharge. |
| M21 | **PASS** | Shared method/theorem `:761--809` returns a finite product path and nonempty product cycle whose unfolding is the infinite counterexample, with no undefined periodicity label. |
| M22 | **PASS** | Reader `:2501--2512`, source note `:781--793`, and compact record `:329--331` call `Gamma` only the source's labelled tree/tree; no proof-tree, derivation-tree, or continuation-tree synonym is introduced. |
| M23 | **PASS** | Every M01--M22 issue was independently rechecked on the round-five hashes; no earlier repair was weakened apart from the later arity failure isolated under M41/M42. |
| M24 | **PASS** | Reader `:1992--2013` gives the p. 735 unique maximal suffix, exact decomposition, and structure-level range/size before use. |
| M25 | **PASS** | Reader `:2036--2066` gives ambient-relative subsequence measures and all five facts about the eliminable subscript (S). |
| M26 | **PASS** | Reader `:2067--2122` gives the preparatory strict statement, null counterexample, proof-supported non-strict inequality, and defines `mu(f)` before Lemma 3.3. |
| M27 | **PASS** | Reader `:2143--2195` gives prefix bound, `C`, strong connectivity, entry edge, empty labels, every exact rule including current-inclusive `F`, and acceptance at the bound start. |
| M28 | **PASS** | Distinct conference bibliography is exact at `handbook.bib:2245--2258`; journal record is `:2260--2274`; direct conference claims in the reader cite `SistlaClarke1982`, not the journal entry. |
| M29 | **PASS** | M24--M28 and all retained earlier checks are repaired without silently changing the two strict source signs or weakening the stated criteria. |

## Mandatory checks M30--M42

| Check | Disposition | Direct disposition |
|---|---|---|
| M30 | **PASS** | Reader `:2290--2298` pinpoints journal `2S(n)` to p. 741, conference `S(n)` to p. 164, and the broader journal construction to pp. 741--742. |
| M31 | **PASS** | Reader `:2148--2214` has empty initialization, increasing length, atom/negation/conjunction/current-inclusive-`F` iff rules, start-label acceptance, literal strong-connectivity/entry checks, concrete loopless-singleton false acceptance, and handbook-only cycle condition. |
| M32 | **PASS** | Reader `:2233--2279` preserves exact `P_1/P_2`, `g_1/g_2/g_3`, `f_x`, `h_1/h_2/h_3`, `f'`, `f''`, `L(F,X)` preservation, both pure-`U` replacements, and Lemma 4.2's role. |
| M33 | **PASS** | Reader `:2324--2364` deletes exactly (s_i,\ldots,s_{j-1}), retains (s_j), preserves common-token types, and states every Lemma 4.6 hypothesis plus conclusions (a),(b). |
| M34 | **PASS** | Reader `:2402--2438` gives Boolean, `X`, `U`, direction-sensitive `S`, initial-since, loop-entry equality, within-period `U`, storage, and Savitch exactly. |
| M35 | **PASS** | Reader `:2517--2544` states Lemma 5.2's extra hypothesis and both inherited conclusions; `:2545--2583` gives the positive rule, singleton initialization, exact frontier update, and within-period emptiness. The notation defect in those otherwise accurate rules is charged under M41. |
| M36 | **PASS** | `label` at reader `:2190--2195`, Lemma 4.3 auxiliaries at `:2259--2262`, `A,B` at `:2403--2407`, and `varphi` at `:2576--2580` are exact, eliminable, metalinguistic, distinguished, and used. |
| M37 | **PASS** | Every supported round-three content repair represented by M30--M36 and retained earlier checks remains present; no silent source strengthening was found there. |
| M38 | **PASS** | Reader `:1905--1920` defines `SF(f)` before Section 3/Theorem 3.5, with ordinary subformulas, single-negation mates, double-negation elimination, `card <= 2 length`, and distinction from `2^length` realized types. |
| M39 | **PASS** | Reader `:2143--2155`, source note `:428--436`, and compact presentation `:249--260` bind `q_0:=delta` before prefix and acceptance use. |
| M40 | **PASS** | Reader `:2169--2189`, source note `:456--466`, and compact presentation `:257--266` preserve “after,” explain the non-strict reading from pp. 734--735 and 737, give a strict-reading counterexample, label the reconstruction, and separate it from the cycle correction. |
| M41 | **FAIL -- MUST FIX** | F1: reader `:2457--2463` and source note `:730--744` promise one alpha-renamed terminal/argument arity (n), but reader `:2545--2574` and source note `:826--860` rebind that (n) to total input length while continuing to use (f_n) as the constructor's last argument. The compact tuple abbreviation itself satisfies the five-part rule at `p09-source-presentations-lot2-3.md:313--331`, but cross-file arity is not consistently bound. |
| M42 | **FAIL -- MUST FIX** | Because M41 fails, the supported round-four unbound/inconsistent-arity finding is not completely repaired on the common round-five hashes. The other three round-five repairs (M38--M40) are clean, but M42 requires all of them. |

## Final disposition

The exact frozen snapshot is not acceptable. All source pages were read, all hashes matched, and the substantive mathematical reconstruction is otherwise source-faithful, but the ETL arity/input-length collision is an explicit round-five mandatory-check failure. Under the charter's no-uncertainty/no-must-fix acceptance rule, the verdict is `REVISE`.
