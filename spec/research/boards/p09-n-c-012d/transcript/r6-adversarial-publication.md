ACCEPT

# Round-six adversarial publication and AGENTS-compliance review

## Seat, identity, scope, and method

- Stable agent identifier: `/root/r6_adversarial_publication`.
- Runtime model/version: not exposed to this seat.
- Assigned object: the round-six frozen `N-c-012.d` snapshot identified in `spec/research/boards/p09-n-c-012d/charter.md`.
- Independence: I read the charter completely before reviewing the object. I did not read `ledger.md`, `transcript/chair.md`, any round-one through round-six reviewer transcript, or any other seat's verdict; I did not contact another reviewer. I wrote only this assigned transcript.
- Method: fresh visual reading of the complete journal and conference sources, mathematical checking of the claims made about them, and line-by-line prose inspection of the five frozen reader/source-record files. I ran no test, test harness, checker, repository script, TeX command, PDF/handbook build, or handbook-PDF inspection.
- Frozen manuscript scope inspected: `handbook/parts/p09/presentations/n-c-012.tex` lines 1851--2631 in full; `handbook/parts/p09/logic-in-computer-science.tex` lines 599--809, including both shared theorems and their necessary local definitions; bibliography entries at `handbook/bib/handbook.bib` lines 2245--2274; all 1,060 lines of `spec/research/p09-sistla-clarke-1985-source-note.md`; and the complete compact `N-c-012.d` presentation at `spec/research/p09-source-presentations-lot2-3.md` lines 185--387.

## Frozen identity: all ten hashes verified

I independently computed SHA-256 for every object in the round-six snapshot. Every result exactly matched the charter:

1. `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`  
   `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
2. `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`  
   `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
3. `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`  
   `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
4. `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`  
   `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
5. `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png`  
   `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`
6. `handbook/parts/p09/presentations/n-c-012.tex`  
   `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA`
7. `handbook/parts/p09/logic-in-computer-science.tex`  
   `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
8. `handbook/bib/handbook.bib`  
   `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`
9. `spec/research/p09-sistla-clarke-1985-source-note.md`  
   `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B`
10. `spec/research/p09-source-presentations-lot2-3.md`  
    `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5`

There was no identity mismatch.

## Complete fresh visual source reading

I visually read every journal image `journal-page-01.png` through `journal-page-17.png`, corresponding to every printed page 733--749, and every conference image `conference-page-01.png` through `conference-page-10.png`, corresponding to every printed page 159--168. No source page was skipped or left unread. The frozen PDFs above control the source identity; the images were used only as the required reading aids.

I also visually inspected all three frozen enlarged aids at the points where the ordinary page image is most vulnerable to misreading:

- the p. 736 acceptable-subsequence crop, which visibly prints the strict union inequality and is consistent with the strict sign in Lemma 3.3;
- the p. 742 bound crop, which visibly prints `2^length(f)`, with only `length(f)` in the exponent;
- the enlarged p. 745 image, which visibly preserves the finite/infinite index problem and the `N_0 -> a_1 a_2 N_0` even/zero-based-odd conflict.

The journal reading covered: identity, plural title, author order, affiliations, issue/date/pages and rights notice on p. 733; syntax and fragment notation on p. 734; structures, inclusive `U/S`, closure, existential `R`-truth, and the beginning of Section 3 on p. 735; all Section 3 definitions, lemmas, strict/non-strict conflicts, Theorems 3.4--3.7, and Figure 1 on pp. 736--739; the full Section 4 reduction and stuttering lemma on p. 740; Figure 2 and the literal `2S(n)` statement on p. 741; source truth sets, the `2^length(f)` count, fulfillment, and Lemmas 4.5--4.6 on pp. 742--743; Theorem 4.7 and the Theorem 4.1 search on pp. 743--745; the complete corrected ETL chain on pp. 745--748; Table I and the correction notice/conclusion on p. 748; and the references and receipt/revision/acceptance history on p. 749.

The conference reading covered: the separate 1982 identity and rights notice on p. 159; its formal validity definition on p. 160; its Section 3 ordering, statements, sketches, and bounds on pp. 161--163; the literal `S(n)` next-distance statement and halting formulation on p. 164; the weaker periodic machinery and Theorem 4.6 on p. 165; the uncorrected Section 5 argument and its `n^2` encoded-input estimate on p. 166; its summary table and bibliography on pp. 167--168. The conference and journal were not interchanged.

## Criteria C1--C9

### C1 — checked clean

The frozen presentation preserves the exact controlling work: A. Prasad Sistla before Edmund M. Clarke; the plural title; *Journal of the ACM* 32(3), July 1985, pp. 733--749; DOI `10.1145/3828.3837`; ISSN `0004-5411`; and the April 1982 / October 1984 / January 1985 receipt history. Evidence is the journal title/rights page and p. 749, reader lines 1853--1877, source-note lines 35--56 and 107--117, and bibliography lines 2260--2274. The distinct STOC 1982 object, pp. 159--168 and DOI `10.1145/800070.802189`, is separately recorded at bibliography lines 2245--2258. File identities, the CMU archive-link defect, public-reading provenance, conditional ACM rights notice, and absence of a republication licence are accurately bounded at source-note lines 58--117. No rights overclaim or scan republication occurs.

### C2 — checked clean

Reader lines 1883--1990 accurately give the journal grammar, the standing of `L(O_1,...,O_k)`, derived `F/G`, the single-negation closure and its bound, distinct-state source structures, inclusive `X/U/S` clauses with exact quantifiers, the restricted `L-tilde(F,X)` syntax, the finite total `R`-structure type, the existential path problem, and the universal counterexample relation. The conference's formal validity clause is correctly located at p. 160, while the identical all-structures/all-points clause remains explicitly labelled a reconstruction relative to journal pp. 734--735. No existential/universal quantifier is switched.

### C3 — checked clean

Reader lines 1992--2225 preserve the unique maximal recurring suffix; the exact `s = init(S).final(S)` split; structure-level `range` and finite description `size`; exact Lemma 3.2 zero-prefix hypothesis; acceptable-subsequence definition and ambient-relative measures; the preparatory strict union sign and its proof-supported non-strict counterpart; `mu(f)` before Lemma 3.3; the exact acceptable-input/extracted-output and every-intermediate-supersequence quantifiers of Lemma 3.3; the second strict/non-strict conflict; Theorem 3.4's non-strict bound and sketch status; the Figure 1 3-SAT reduction; the fully bound Theorem 3.5 certificate, all four labelling rules, current-position-inclusive `F`, literal strong-connectivity and entry-edge checks, concrete loopless-singleton false acceptance, and separately owned directed-cycle correction; and the full Lemma 3.6 statement. `SF(f)` is defined at lines 1905--1920, before the certificate first uses it at lines 2156--2159. No finite-description bound is presented as finite-model cardinality.

### C4 — checked clean

Reader lines 2227--2446 preserve the exact three-language Theorem 4.1 statement; all of Lemma 4.3's `P_1/P_2`, `g_1/g_2/g_3`, `f_x`, `h_1/h_2/h_3`, `f'`, and `f''` construction; the `L(F,X)` preservation; both self-loop-sensitive pure-`U` replacements and their dependence on Lemma 4.2; the computation-history reduction, persistent terminal configuration, diamond unit, complete-description traversal, and journal `2S(n)`/conference `S(n)` distinction; the source-truth-set definition and exact `2^length(f)` count; inclusive fulfillment before `s_j`; Lemma 4.5's exact deletion while retaining `s_j`; every hypothesis and both conclusions of Lemma 4.6; valuation periodicity with `i in N` and positive `p`; all bounds, every-periodic-position truth-set equality, and every-periodic-position `U` discharge in Theorem 4.7; the `Ff` move for past `S`; all Boolean, `X`, `U`, direction-sensitive `S`, initial-since, loop-entry, within-period discharge, storage, and Savitch steps. Proof granularity is not strengthened.

### C5 — checked clean

Reader lines 2448--2598 preserve the disjoint-nonterminal convention, grammar form, normalization, one terminal-count/constructor-arity symbol `n`, exact constructor semantics, explicit handbook-owned finite-word represented-index restriction, parity conflict, ETL closure, exact labelled tree `Gamma(S,j,N_i)`, separation of continuation and terminal productions, Lemma 5.1, finite-tree maximum-depth fulfillment, all inherited Lemma 5.2 hypotheses and conclusions, Theorem 5.3 bounds and obligations, and both Theorem 5.4 rules. The source's reused input-length `n` is consistently alpha-renamed to `ell_in` in the reader at lines 2547--2556, source note at lines 826--837, and compact presentation at lines 313--321. It is exactly defined as complete formula-and-grammar encoded input length, is eliminable and metalinguistic, is distinguished from constructor arity `n` and `L(O_1,...,O_k)`, and is actually used in `card(SF(f)) <= 2 ell_in`. There is no second binding collision. The correction notice remains calibrated: it does not identify a precise bad inference or a unique repairing lemma.

### C6 — checked clean

Reader lines 2600--2630 reproduce all Table I rows and distinguish satisfiability, validity, and existential `R`-truth. Shared theorem `thm:p09-ltl-pspace` at `logic-in-computer-science.tex` lines 693--708 accurately derives the `L(U,X)` classification from `L(U) subset L(U,X) subset L(U,S,X)` without silently changing the operator basis. Shared model-checking lines 761--809 return a finite product path plus a nonempty product cycle and obtain universal model checking from existential truth of the negated formula and deterministic polynomial-space closure under complement. No source problem quantifier is changed.

### C7 — checked clean

The conference/journal comparison at source-note lines 941--980 is complete for the material differences claimed by the frozen object and agrees with the fresh reading of all 27 pages: syntax presentation, validity clause, closure, restricted-fragment body results, Section 3 bound and ordering, Section 4 numbering and stuttering lemma, next distance, terminal machine behavior, periodic invariant, proof label/detail, finite/infinite ETL wording, grammar normalization, corrected Section 5 chain and bounds, conclusion/table form, and references. Journal numbering, bounds, hypotheses, and proof language control. The p. 748 notice is not enlarged into identification of the error or a unique repair.

### C8 — checked clean

The two bibliography records are distinct and source-accurate at `handbook.bib` lines 2245--2274. Journal claims cite `SistlaClarke1985`; direct conference claims cite `SistlaClarke1982`. The complete source-note page map at lines 119--145 puts `init/final/range/size` on p. 735, the conclusion only on p. 748, and references on pp. 748--749. Its proof-status table at lines 914--935 accurately distinguishes printed proof, asserted induction, sketch, abbreviated cases, and brief replacement. The compact presentation at lines 185--387 is cross-file consistent and leaves round-six review and later publication gates open. Rights/provenance claims remain limited to scholarly inspection.

### C9 — checked clean

The prose is independently organized, publication-quality at the frozen source level, definition-before-use, exact in its types and quantifiers, and candid about source defects and handbook reconstruction. I found no omitted qualification, unsupported addition, silent strengthening, hidden source repair, cross-file contradiction, or five-part terminology failure. The terminology audit below records the required local dispositions.

## Five-part terminology rule

Every required technical expression supplies necessity, definition or source standing, standing as object/relation/metalinguistic notation, nonredundancy, and later use at the same local introduction:

- **Acceptable subsequence:** reader lines 2036--2040 give the exact source condition, identify it as a condition on a subsequence rather than a temporal model, distinguish it from an ordinary subsequence, and use it in Lemma 3.3 at lines 2088--2109.
- **Ambient subscripts:** reader lines 2042--2067 define `init_S`, `final_S`, `range_S`, and `size_S`, state that the subscript is eliminable and metalinguistic, explain the otherwise hidden ambient parameter and the difference from the source typography, and use it in the extraction and union bounds.
- **`SF(f)`:** reader lines 1905--1920 define the exact single-negation closure and bound, state its metalinguistic standing, distinguish it from both ordinary subformulas and state truth sets, and use it in the certificate and periodic arguments.
- **Certificate start `q_0`:** reader lines 2143--2147 bind it exactly to the supplied start state `delta`, state its eliminable metalinguistic standing and non-node status, explain the alignment need, and use it in the prefix and acceptance clauses.
- **Certificate `label`:** reader lines 2156--2195 define initialization and every membership rule, give finite metalinguistic standing, distinguish these sets from `[s_i]_{S,f}`, and use them for acceptance.
- **Lemma 4.3 auxiliary formula letters:** reader lines 2233--2262 define every formula, state that the names are eliminable and metalinguistic rather than operators, distinguish their respective roles, and use them to assemble `f''`.
- **Source truth set:** reader lines 2300--2315 give the exact set definition and standing, distinguish it from closure size and independent power-set choice, and use it in Lemmas 4.5--4.6 and Theorem 4.7.
- **Until fulfillment:** reader lines 2316--2323 give the inclusive endpoint definition, state finite-witness/metalinguistic standing, distinguish it from truth-set membership and a connective, and use it in loop closure.
- **Successive guesses `A,B`:** reader lines 2402--2408 state their exact intended values, eliminable bookkeeping standing, need for directional one-step checks, distinction from realized source truth sets, and actual use in all five recurrences.
- **ETL constructor:** reader lines 2451--2482 bind terminal count and arity, give exact finite/infinite semantics, state grammar-indexed formula-constructor standing, distinguish it from ordinary `U`, and use it throughout the ETL results.
- **`Gamma(S,j,N_i)`:** reader lines 2501--2512 define its root and every continuation edge, state labelled-tree standing, distinguish it from a model, automaton, proof-calculus object, and terminal production, and use it in Lemma 5.1 and finite-tree fulfillment.
- **Negated-grammar fulfillment:** reader lines 2514--2524 define it from maximum finite-tree depth, distinguish it from until fulfillment, and use it in Lemma 5.2 and Theorem 5.3.
- **`ell_in`:** reader lines 2547--2556, source-note lines 826--837, and compact lines 313--321 define it exactly, state eliminable metalinguistic size standing, explain necessity, distinguish it from `n` and fragment notation, and use it in the encoded-input closure bound.
- **Continuation set `varphi`:** reader lines 2572--2592 define initialization and update, state eliminable metalinguistic finite-set standing, distinguish it from the valuation and `Gamma`, and use it in the within-period emptiness check.
- **Compact tuple abbreviation:** compact lines 322--326 define `bar f` exactly as `(f_1,...,f_n)`, state eliminable metalinguistic tuple standing, distinguish it from a constructor and the guessed sets, explain its local legibility need, and use it only in the two displayed production rules.

No hypothetical technical name is introduced in place of an owed artifact.

## Invariants I1--I15

- **I1:** satisfied. Review used only primary-source visual reading, mathematical reasoning, hash identity, and ordinary source inspection; no prohibited execution or build occurred.
- **I2:** satisfied. All ten round-six hashes match exactly.
- **I3:** satisfied. All seventeen journal pages and all ten conference pages were freshly visually read; claims were checked against printed pages rather than OCR or prior notes.
- **I4:** satisfied. The p. 742 exponent is `2^length(f)`; p. 745 preserves both the finite/infinite index defect and even/zero-based-odd conflict.
- **I5:** satisfied. The journal controls; conference numbering, bounds, proof language, and Section 5 are kept separate; no unique repair is invented.
- **I6:** satisfied. Fragment notation, ETL, inclusive temporal semantics, existential `R`-truth, satisfiability, and validity remain distinct; the validity clause is explicitly reconstructed.
- **I7:** satisfied. `size` is a finite measure of an infinite structure; `final` is the unique maximal suffix; acceptable-subsequence measures are ambient-relative; both strict/non-strict conflicts are candidly stated.
- **I8:** satisfied. Journal `2S(n)`, closure bound `2 length(f)`, realized-set count `2^length(f)`, and inclusive fulfilled-before endpoint are all distinct and exact.
- **I9:** satisfied. Theorem 4.7 includes periodic valuation equality, periodic truth-set equality, every-position obligation discharge, exact bounds, `Ff`, initial-since, and Savitch.
- **I10:** satisfied. ETL disjointness, constructor, normalization, closure, `Gamma`, finite-tree termination, Theorems 5.3--5.4, continuation search, typing reconstruction, and parity conflict are all present and exact.
- **I11:** satisfied. Sketches, asserted inductions, abbreviated cases, and brief replacements retain their printed strength; no Sistla--Clarke automata/Büchi proof is claimed.
- **I12:** satisfied. The five-part terminology audit above is clean.
- **I13:** satisfied. This seat remained independent and inspected no forbidden record or transcript.
- **I14:** satisfied. This `ACCEPT` rests on my own exhaustive checked-clean review, with no unread page, mismatch, uncertainty, or must-fix finding; it does not rely on a vote.
- **I15:** satisfied. The compact record and this disposition close at most the frozen topic-level scholarly review; they do not close Alpern--Schneider, `N-c-012`, Part IX, build, rendered inspection, human review, final-book completion, or user acceptance.

## Mandatory checks M01--M44

- **M01 — pass:** enlarged journal p. 742 visibly prints `2^length(f)`. Reader lines 2307--2315 reject the spurious doubled exponent.
- **M02 — pass:** journal pp. 734--735 contain no formal validity clause; reader lines 1977--1990 explicitly mark the universal clause as reconstruction, while recording conference p. 160.
- **M03 — pass:** journal p. 742 and reader lines 2316--2323 use `j >= i` and `i <= ell <= j`, including both endpoints.
- **M04 — pass:** journal p. 736 visibly prints `<` in the preparatory union sentence and Lemma 3.3; reader lines 2067--2083 and 2111--2122 disclose the null failures, the proof's `<=` uses on p. 737, and Theorem 3.4's non-strict conclusion.
- **M05 — pass:** journal p. 741 visibly prints `2S(n)`; conference p. 164 visibly prints `S(n)`; reader lines 2281--2298 preserve the difference.
- **M06 — pass:** reader lines 2380--2400 give every Theorem 4.7 quantifier and bound, including every `k >= i`; lines 2534--2544 give both Theorem 5.3 bounds and every-position obligations.
- **M07 — pass:** journal p. 745 visibly says finite or infinite and then uses the unrestricted index. Reader lines 2468--2479 clearly label the finite represented-position restriction as handbook-supplied typing.
- **M08 — pass:** journal p. 745 visibly prints `N_0 -> a_1 a_2 N_0` and the even-state sentence. Reader lines 2484--2493 accurately derive the zero-based odd offsets and leave the repair open.
- **M09 — pass:** reader lines 2495--2512 give the exact ETL closure and every `Gamma` edge condition, keeping terminal productions separate.
- **M10 — pass:** reader lines 2514--2517 define maximum finite-tree depth and distinguish it from until fulfillment; lines 2572--2592 require the continuation set to become empty within the guessed period.
- **M11 — pass:** journal p. 748 identifies only an erroneous theorem used in the conference proof. Reader lines 2593--2598 and source-note lines 973--980 do not identify a precise inference or unique lemma.
- **M12 — pass:** source-note lines 914--935 and reader lines 2440--2446 preserve every proof-status qualification; reader/source-note lines 2593--2598 and 870--873 exclude a Sistla--Clarke Büchi construction.
- **M13 — pass:** shared theorem lines 693--708 explicitly use `L(U) subset L(U,X) subset L(U,S,X)` for hardness and upper bound.
- **M14 — pass:** shared method/theorem lines 761--809 use an accepting product for `neg A`, a finite prefix plus nonempty cycle, and complement closure to obtain universal model checking.
- **M15 — pass:** acceptable subsequence, ambient subscripts, source truth set, both fulfillment notions, ETL constructor, and `Gamma` all pass the five-part terminology audit above.
- **M16 — pass:** source-note page map lines 119--145 puts `init/final/range/size` on p. 735, conclusion only on p. 748, and references on pp. 748--749.
- **M17 — pass:** conference p. 160's validity definition is recorded, the journal-relative handbook clause remains reconstructed, and the p. 748 correction notice remains unidentified; reader lines 1977--1990 and 1873--1881.
- **M18 — pass:** reader lines 2015--2034, 2088--2109, and 2217--2224 preserve the zero-prefix condition, acceptable input/output, every intermediate supersequence, surviving-token scope, finite `u` containing `s_i`, and both strict/non-strict disclosures.
- **M19 — pass:** reader lines 2281--2298 state one tape-cell position per diamond, one BI-to-EI traversal per instantaneous description, repeated traversals per computation, persistent terminal configurations without tape changes, and distinguish the conference halting formulation in the source-note comparison at lines 960--962.
- **M20 — pass:** reader lines 2366--2378 bind `i in N`, `p > 0`, and complete-valuation equality for every `k >= i`, distinct from truth-set equality and obligation discharge.
- **M21 — pass:** shared method/theorem lines 781--787 and 796--808 return a finite product path and nonempty cycle; no undefined periodicity name is used.
- **M22 — pass:** the reader, source note, and compact presentation call `Gamma` only the source's labelled tree or `Gamma`; none uses proof-tree, derivation-tree, or continuation-tree as a synonym.
- **M23 — pass:** every earlier requirement M01--M15 and every round-two repair check is present at full strength on this frozen snapshot; no later edit weakens it.
- **M24 — pass:** reader lines 1992--2013 give the unique maximal suffix, exact decomposition, and structure-level definitions before use.
- **M25 — pass:** reader lines 2036--2067 give ambient-relative acceptable-subsequence measures and the subscript's exact eliminable metalinguistic standing, necessity, distinction, and use.
- **M26 — pass:** reader lines 2067--2122 preserve the preparatory strict sign, null counterexample, proof-supported non-strict subadditivity, and define `mu(f)` before Lemma 3.3.
- **M27 — pass:** reader lines 2143--2191 give the prefix bound, subset `C`, literal strong connectivity, entry edge, empty initialization, all four iff rules including current-position `F`, and acceptance exactly at the bound start state.
- **M28 — pass:** bibliography lines 2245--2274 give distinct accurate 1982 and 1985 entries; citations resolve direct claims to the correct object.
- **M29 — pass:** all round-three repairs and earlier requirements remain present, including the newly disclosed preparatory strict-sign conflict; no weakening was found.
- **M30 — pass:** reader lines 2289--2298 pinpoint journal `2S(n)` to p. 741, conference `S(n)` to p. 164, and the broader journal reduction to pp. 741--742.
- **M31 — pass:** reader lines 2156--2195 give empty labels, increasing-length order, exact atomic/negation/conjunction/`F` iff rules, and start-label acceptance; lines 2197--2214 preserve the literal source check, concrete false acceptance, and solely handbook-owned directed-cycle correction.
- **M32 — pass:** reader lines 2233--2279 reproduce every Lemma 4.3 auxiliary, both pure-`U` cases, `L(F,X)` preservation, and exact Lemma 4.2 use.
- **M33 — pass:** reader lines 2324--2364 give the exact Lemma 4.5 deletion/retention and every Lemma 4.6 hypothesis plus both conclusions.
- **M34 — pass:** reader lines 2402--2438 give all five directional recurrence families, initial since, loop-entry equality, within-period `U` discharge, storage, and Savitch.
- **M35 — pass:** reader lines 2517--2544 give Lemma 5.2's additional negated-grammar hypothesis, both inherited conclusions, and Theorem 5.3; lines 2557--2592 give Theorem 5.4's exact positive and negative updates, singleton initialization, and within-period emptiness.
- **M36 — pass:** `label`, all Lemma 4.3 formula names, `A/B`, `varphi`, and the compact `bar f` tuple satisfy all five terminology conditions at the locators in the terminology audit.
- **M37 — pass:** every supported round-three issue summarized by M30--M36 is repaired without silent source strengthening or weakening of any earlier check.
- **M38 — pass:** `SF(f)` is exactly defined at reader lines 1905--1920 before Theorem 3.5 uses it, including ordinary subformulas, single-negation mates, double-negation elimination, `<= 2 length(f)`, and separation from the later exponential truth-set count.
- **M39 — pass:** reader lines 2143--2147, source-note lines 428--436, and compact lines 249--260 bind the supplied start state to `q_0` before all prefix and acceptance uses.
- **M40 — pass:** reader lines 2169--2189 make the prefix `F` witness current-position-inclusive, preserve the paper's word “after,” explain the source-context non-strict reading from pp. 735 and 737, give the strict-reading counterexample, and keep it separate from the cycle correction.
- **M41 — pass:** `n` remains terminal count and tuple arity through the constructor, `Gamma`, Lemma 5.2, and both Theorem 5.4 rules in all three records. The compact-only `bar f` abbreviation is fully defined and used only locally.
- **M42 — pass:** every round-four repair summarized by M38--M41 remains present at full strength; no source wording is silently strengthened.
- **M43 — pass:** the arity symbol remains `n`; the source's independent Theorem 5.4 encoded-input length is consistently `ell_in` in the reader, source note, and compact presentation. Each location gives its exact definition, eliminable metalinguistic standing, distinction from arity `n` and `L(O_1,...,O_k)`, necessity, and use in `card(SF(f)) <= 2 ell_in`. No second redefinition or collision appears.
- **M44 — pass:** the sole round-five arity/input-length collision is repaired on all three frozen records. All C1--C9, I1--I15, and M01--M43 remain intact.

## Final disposition

The frozen round-six snapshot is source-faithful, mathematically correct within its candidly stated source/reconstruction boundary, complete for its declared scope, cross-file consistent, publication-ready at the prose/source level, and compliant with the five-part terminology rule. I found no blocker, uncertainty, unread source page, hash mismatch, unsupported strengthening, omitted qualification, rights/provenance defect, or must-fix item. This acceptance is confined to `N-c-012.d` topic-level scholarly review under I15.
