REVISE

# Round-two mathematical/proof review: N-c-012.d Sistla--Clarke 1985

## Reviewer identity, runtime, and independence

- Stable reviewer identity: `/root/schmidt_smolka_1991_research`.
- Seat: mathematical/proof.
- Exact runtime model/version: not exposed to this reviewer.
- I read the complete updated board charter before substantive review and used only its frozen round-two snapshot.
- I did not inspect `spec/research/boards/p09-n-c-012d/ledger.md`, `transcript/chair.md`, either other reviewer's round-two transcript or verdict, or any earlier transcript. I did not contact another reviewer.
- I created or edited only this assigned transcript. I made no manuscript, shared-section, bibliography, source-note, source-ledger, authority, or board-record edit.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. The only mechanical operations were read-only line retrieval and SHA-256 identity hashing. Primary-page images/PDFs were read as scholarship.

## Frozen identities

Every round-two identity was computed before substantive review and recomputed immediately before this filing. Both passes matched the charter byte-for-byte:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `48D2F8F946AFFC394613D7895E89175099CC9FA73800BDA36A3C5F63353C6AD5` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `D7E85E5AC951C56F607099A5756C1AA5CEEC02DB8D0CC3EC359E17EBE2450FCD` |
| `spec/research/p09-source-presentations-lot2-3.md` | `D5BD9F8BA7A12AFD7A8A08CDAAFB2E0E4C0E0B48E0BD83D5BDC06AA08D2E8353` |

No frozen identity changed during review.

## Complete primary-source visual-read record

I visually read every journal body page and every conference page, not merely OCR or the source note.

### Journal authority, printed pp. 733--749

- p. 733: printed identity, author order and affiliations, abstract, introduction, ACM notice, descriptors, and keywords.
- p. 734: introduction completed; exact source notation and primitive/derived formula formation.
- p. 735: restricted fragment, structures and interpretations, inclusive `X/U/S` semantics, `SF`, total `R`-structures and existential path problem; at the foot of the page, the unique maximal-suffix definitions of `init`, `final`, `range`, and `size`.
- p. 736: Lemmas 3.1 and 3.2; ordinary and acceptable subsequences; the source's ambient-structure-relative definitions of `init(t)`, `final(t)`, `range(t)`, and `size(t)` for acceptable subsequences; the acceptable-union size fact; `mu(f)`; and the exact Lemma 3.3 statement with its literal strict bound.
- p. 737: the remainder of the Lemma 3.3 induction, its non-strict proof inequalities, Theorem 3.4 and its `PROOF SKETCH`, and Theorem 3.5's statement.
- p. 738: Figure 1, 3-SAT hardness, the bounded-prefix/strongly-connected-set witness, and the NP procedure.
- p. 739: Theorem 3.5 completed; exact Lemma 3.6 quantifiers; Theorem 3.7; and Theorem 4.1.
- p. 740: the one-state duplication construction, Lemmas 4.2--4.3, and the exact pure-`U` replacement cases.
- p. 741: Lemma 4.4's deterministic one-tape machine, absorbing terminal configurations, Figure 2, and the cell/instantaneous-description encoding.
- p. 742: completion of the computation reduction; journal `2S(n)`; the source truth-set definition; the controlling `2^length(f)` count; fulfilled-before with `j >= i` and an inclusive endpoint; valuation periodicity; Lemmas 4.5--4.6 begin.
- p. 743: Lemma 4.6's nontrivial `U/S` induction and literal Theorem 4.7 statement, including every-periodic-position obligations.
- p. 744: Theorem 4.7's counting proof and bounds; the type-guessing proof of Theorem 4.1, including the initial-since condition and local recurrences.
- p. 745: Savitch step; ETL grammar and constructor; finite/infinite index defect; parity example conflict; exact extended closure; exact labelled tree `Gamma`; Lemma 5.1 begins.
- p. 746: Lemma 5.1 completed; finite-tree depth fulfillment; Lemma 5.2; Theorem 5.3 begins.
- p. 747: Theorem 5.3's every-position obligations and proof; Theorem 5.4, encoded-input premise, and continuation-set algorithm.
- p. 748: Theorem 5.4 completed; complete Table I; conclusion and calibrated conference-error notice; references begin.
- p. 749: references and receipt/revision/acceptance dates.

I separately inspected the enlarged p. 742 derivative and confirmed the exponent is literally `2^length(f)`. I separately inspected the complete enlarged p. 745 page and confirmed both the finite/infinite unrestricted-index defect and the printed even/zero-based-odd conflict.

### Conference predecessor, printed pp. 159--168

- p. 159: title, authors, Harvard affiliation, abstract, introduction, conference rights notice.
- p. 160: operator grammar, point semantics, the formal all-structures/all-positions validity definition, and the start of the `R`-structure definition.
- p. 161: total `R`, paths and existential `R`-truth; Section 3 definitions; conference Theorem 3.1 and Lemmas 3.2--3.3.
- p. 162: conference Lemma 3.4 and proof sketch, model-theorem proof sketch, and Theorem 3.5.
- p. 163: Figure 1, NP hardness and membership algorithms.
- p. 164: Theorem 4.1; Lemmas 4.2--4.3; the deterministic machine that halts in accept or reject; Figure 2 with `S(n)` next distance.
- p. 165: acceptance formula; type reduction; valuation-period definition; recurring-type condition; conference Theorem 4.6 and proof outline.
- p. 166: periodic search continued; regular-operator grammar and semantics; alternating example; conference closure and unnumbered extension argument; conclusion begins.
- p. 167: conclusion, Figure 3 classification, and bibliography begins.
- p. 168: bibliography completed.

## Findings

### MP-F1 — MUST FIX — the reader and source record omit the source's acceptable-subsequence measure definitions, leaving Lemma 3.3 ill-typed

**Artifact locations.** `handbook/parts/p09/presentations/n-c-012.tex:1974-1984,2010-2020`; `spec/research/p09-sistla-clarke-1985-source-note.md:269-280,308-318`.

**Frozen claim.** The reader defines `size(S)` only for a structure, later defines when a subsequence is acceptable, and then states the Lemma 3.3 bound `size(u)<mu(f)` for an acceptable subsequence `u`. The reader never defines `init(t)`, `final(t)`, `range(t)`, or `size(t)` for an acceptable subsequence. The source note likewise gives the structure-level operations and then uses `size(u)` without recording the distinct ambient-structure-relative definitions printed immediately before Lemma 3.3.

**Authority evidence.** Printed p. 735 first selects the unique maximal suffix `s''` of `s` in which every valuation occurring there recurs infinitely often, writes `s=s' . s''`, and defines `init(S)=s'`, `final(S)=s''`, `range(S)={xi(s_k) | s_k is in s''}`, and `size(S)=length(init(S))+card(range(S))`. Printed p. 736 then supplies a second, indispensable definition for an acceptable subsequence `t` relative to the ambient structure `S`: `init(t)` is the longest prefix of `t` that is a subsequence of `init(S)`; `final(t)` is the remaining suffix beginning with the state immediately after `init(t)`; and `range(t)` and `size(t)` are defined as for a structure, with all four operations understood relative to `S`. The same paragraph also states that the statewise union of two acceptable subsequences is acceptable and has size at most the sum of their sizes, the fact used in the conjunction induction.

**Harm.** In the reader, `final(S)` is used at lines 2011--2012 without ever being named or defined, and `size(u)` at line 2020 applies a structure-only operation to a sequence. More importantly, the omitted p. 736 definition is not obtained merely by applying the structure definition to `u`: `init(u)` is explicitly the longest prefix of `u` lying within the ambient `init(S)`, so the ambient structure is part of the definition. The exact Lemma 3.3 statement, its induction, and the strict/non-strict diagnosis are therefore not well-typed as printed in the handbook. This fails C3 and C9, I7 and I12, and M15, M18, and M23; it also makes the source note incomplete under C8.

**Exact correction.** Before the acceptable-subsequence lemma, the reader must:

1. state the p. 735 maximality and uniqueness condition; write `s=s' . s''`; and define `init(S)`, `final(S)`, `range(S)`, and `size(S)` explicitly;
2. after defining acceptable `t`, reproduce the p. 736 ambient-relative definitions of `init(t)`, `final(t)`, `range(t)`, and `size(t)` before any occurrence of `size(u)`; and
3. where the induction is summarized, record the acceptable-union construction and its non-strict subadditivity, because it is the printed step supporting the conjunction case.

The source note must add the same p. 736 acceptable-subsequence definitions (and the union fact in its proof-chain record) before its statement of Lemma 3.3. A harmless eliminable notation such as `size_S(t)` may be used to expose the ambient dependence, provided it is explicitly identified as handbook disambiguation of the source's context-dependent `size(t)`, not attributed as new source notation.

### MP-F2 — MUST FIX — `mu(f)` is used before it is defined in the reader

**Artifact location.** `handbook/parts/p09/presentations/n-c-012.tex:2015-2020,2035-2040`.

**Frozen claim.** The first displayed occurrence of `mu(f)` is the literal Lemma 3.3 bound at line 2020. Only seventeen lines later does the defect paragraph say that `mu(f)` counts occurrences of `F`.

**Authority evidence.** Printed p. 736 defines `mu(f)` as the number of occurrences of the symbol `F` before the statement of Lemma 3.3. The frozen source note correctly follows that order at lines 312--318.

**Harm.** The reader presents an undefined measure in the theorem statement, contrary to C9's definition-before-use requirement and I12/M15's local technical-name rule. The later explanation does not repair the first reading point.

**Exact correction.** Move the exact definition of `mu(f)` to the paragraph before the Lemma 3.3 hypotheses and bound. The defect paragraph may then refer back to that already defined measure.

## Criterion-by-criterion disposition

- **C1 — checked clean.** The reader, bibliography, source note, and source ledger preserve the plural title, printed author order, journal/issue/date/pages, DOI and ISSN, receipt history, CMU provenance, distinct conference object, hashes, and conditional ACM rights boundary. Evidence: journal pp. 733, 748--749; conference pp. 159, 168; reader lines 1853--1880; source-note lines 3--145; bibliography entry `SistlaClarke1985`; source-ledger lines 185--189.
- **C2 — checked clean.** Grammar, derived `F/G`, restricted-fragment standing, distinct state tokens, inclusive `U/S`, total `R`, existential path truth, universal-program counterexample relation, and the journal-versus-conference validity boundary are exact. Evidence: journal pp. 734--735 and 748; conference p. 160; reader lines 1882--1972; source-note lines 147--265.
- **C3 — failed by MP-F1 and MP-F2.** Lemmas 3.2, 3.3, and 3.6 otherwise have their exact hypotheses, quantifiers, surviving positions, and bounds; the strict/non-strict defect, Theorems 3.4--3.7, Figure 1, and proof-status boundaries are accurate. But the extraction measure used in Lemma 3.3 is not defined on acceptable subsequences in either the reader or source note, `final(S)` is undefined in the reader, and `mu` is used before definition.
- **C4 — checked clean.** The stuttering boundary, Lemmas 4.3--4.6, Figure 2's graph unit, terminal persistence, journal `2S(n)` versus conference `S(n)`, closure/type count distinction, fulfilled-before endpoints, valuation periodicity, Theorem 4.7 bounds and every-position obligations, `Ff` step, local search conditions, and Savitch invocation agree with journal pp. 740--745.
- **C5 — checked clean.** The grammar forms and disjoint-name convention, finite/infinite typing disclosure, parity conflict, extended closure, exact `Gamma` edge condition, Lemmas 5.1--5.2, distinct tree-depth obligation, Theorem 5.3 bounds/quantifiers, Theorem 5.4 encoded-input and continuation-set search, and nonunique repair boundary agree with journal pp. 745--748.
- **C6 — checked clean.** The reader transcribes every Table I row, preserves Theorem 4.1's shorter displayed list, and correctly derives `L(U,X)` from `L(U) subseteq L(U,X) subseteq L(U,S,X)`. Shared lines 693--708 give that exact containment. Shared lines 761--809 preserve existential counterexample search, universal complement, polynomial-space closure under complement, a finite product prefix, and a nonempty accepting cycle.
- **C7 — checked clean.** The source note's complete reconciliation agrees with all ten conference pages: formal validity at p. 160, `S(n)`, literal halting language, the weaker conference periodic invariant, grammar wording, and the uncorrected extension proof remain distinct from the journal additions. The conclusion is correctly limited to an unidentified theorem used in the conference proof.
- **C8 — failed only to the extent stated in MP-F1.** Identity, hashes, URLs, page map, proof-status table, bibliography, rights boundary, and source-ledger status are otherwise accurate. The page map now correctly puts the four base operations on p. 735, conclusion on p. 748, and references on pp. 748--749. The source note's missing p. 736 acceptable-subsequence measure definitions prevent its Section 3 record from being complete.
- **C9 — failed by MP-F1 and MP-F2.** The rest of the prose is independently worded, operator-sensitive, precisely typed, and avoids unsupported names. The undefined `final(S)`, untyped `size(u)`, and late definition of `mu` violate definition-before-use and the local five-part rule.

## Invariant-by-invariant disposition

- **I1:** satisfied; scholarship/prose inspection only.
- **I2:** satisfied; both pre-review and immediate pre-filing hash passes matched all nine frozen identities.
- **I3:** satisfied; all seventeen journal and all ten conference pages were visually read.
- **I4:** satisfied; both controlling derivatives were directly inspected and the two mandated readings confirmed.
- **I5:** satisfied; the journal controls and no unique correction step is invented.
- **I6:** satisfied; all language, semantics, decision-problem, and reconstructed-validity distinctions are preserved.
- **I7:** not satisfied because MP-F1 leaves the acceptable-subsequence size operation undefined, although the reader correctly says structure size is not finite-model cardinality and correctly diagnoses the printed strict bound.
- **I8:** satisfied; `2S(n)`, `2^length(f)`, closure size, `j >= i`, and the inclusive witness endpoint are exact.
- **I9:** satisfied; all three periodic conditions, exact bounds, `Ff`, initial since, and Savitch are visible.
- **I10:** satisfied; ETL standing, closure, `Gamma`, both obligations, bounds, continuation search, and both source conflicts are exact.
- **I11:** satisfied; proof sketches, asserted inductions, abbreviated cases, and the brief pure-`U` replacement remain unequal; no Büchi proof is attributed to this paper.
- **I12:** not satisfied because of MP-F1 and MP-F2; other audited technical names meet the five local requirements.
- **I13:** satisfied; blind independence preserved.
- **I14:** satisfied by this `REVISE`; no uncertainty was converted into acceptance.
- **I15:** satisfied; the narrow closure boundary is preserved below.

## Mandatory-check disposition

- **M01 PASS:** controlling p. 742 prints `2^length(f)`; no scoped artifact attributes `2^(2 length(f))` to the article.
- **M02 PASS:** no formal validity clause occurs on journal pp. 734--735; reader lines 1959--1971 label the universal clause as reconstruction and cite conference p. 160 as predecessor evidence.
- **M03 PASS:** reader lines 2132--2135 give `j >= i` and `i <= ell <= j` exactly.
- **M04 PASS:** literal `<`, zero/zero basis, proof-supported `<=`, and Theorem 3.4's non-strict bound are separately disclosed. MP-F1 concerns the missing type of `size(u)`, not the correctly diagnosed inequality conflict.
- **M05 PASS:** reader/source note record journal `2S(n)` and conference `S(n)` exactly.
- **M06 PASS:** Theorems 4.7 and 5.3 have exact prefix/period bounds and every-`k` type equality and discharge clauses.
- **M07 PASS:** finite/infinite string and unrestricted-index conflict is exact; represented-index typing is explicitly handbook-supplied.
- **M08 PASS:** the grammar and the even/zero-based-odd mismatch are exact; no repair is selected.
- **M09 PASS:** the extended closure and every `Gamma(S,j,N_i)` continuation edge are exact; terminal productions remain outside those edges.
- **M10 PASS:** maximum tree depth, distinct fulfillment standing, and within-period continuation-set emptiness are exact.
- **M11 PASS:** correction notice is calibrated to an unidentified theorem/inference and no new lemma is singled out as the repair.
- **M12 PASS:** result-by-result proof status and absence of a Sistla--Clarke Büchi construction are accurate.
- **M13 PASS:** shared lines 693--708 give the exact two inclusions and the correct hardness/upper-bound transfer.
- **M14 PASS:** shared lines 796--808 obtain universal model checking by complementing existential truth of `not A`, use deterministic polynomial-space closure under complement, and retain the source's existential quantifier.
- **M15 FAIL:** acceptable subsequence is relationally distinguished, but its source-defined measure operations are omitted; `mu` is used before definition. The source truth set, both fulfilled-before obligations, ETL constructor, and `Gamma` otherwise satisfy necessity, definition, standing, nonredundancy, and use.
- **M16 PASS:** source-note lines 119--145 place the base Section 3 operations on p. 735, conclusion only on p. 748, and references on pp. 748--749.
- **M17 PASS:** conference p. 160 validity is recorded while the reader's identical clause remains a journal-relative reconstruction; the error notice remains unidentified.
- **M18 FAIL only for the typing defect in MP-F1:** the zero-prefix clause, acceptable input/output, every-intermediate-supersequence quantifier, surviving-position scope, finite `u` containing `s_i`, and strict/non-strict disclosure are otherwise exact.
- **M19 PASS:** each diamond is one tape cell, a full BI--EI traversal is one instantaneous description, repeated traversals form the computation, journal terminal configurations persist without tape changes, and conference p. 164 is accurately described as halting in accept/reject.
- **M20 PASS:** `i` is nonnegative, `p` positive, complete valuation equality holds for every `k >= i`, and it remains distinct from type equality and both obligation kinds.
- **M21 PASS:** shared lines 785--787 and 801--802 return a finite product path plus a nonempty product cycle and describe its infinite unfolding; no undefined periodicity name is used there.
- **M22 PASS:** the reader, source note, source ledger, and charter use only the source's `labelled tree` or `Gamma`; no proof-tree, derivation-tree, or continuation-tree synonym occurs.
- **M23 FAIL:** the listed round-one repairs visible in M16--M22 are present and do not weaken the earlier criteria, but MP-F1 and MP-F2 remain on the exact round-two snapshot, so the snapshot cannot pass the complete fresh audit.

## Checked-clean mathematical summary

Apart from the two Section 3 definition-order/typing defects, I found no mismatch in the repaired mathematics. In particular: Lemma 3.2's zero-prefix boundary is logically equivalent to the source's redundant unconditional first-valuation premise; Lemmas 3.3 and 3.6 preserve truth over every intermediate supersequence at exactly the surviving state tokens; Figure 2 is now described at the cell and full-traversal levels; the terminal-machine assumption correctly converts a halting computation into an infinite temporal history; the p. 742 type count is not inflated by negation closure; valuation periodicity, restricted source-type equality, until discharge, and negated-grammar discharge remain four distinct notions; Theorems 4.7 and 5.3 quantify at every periodic position; and the shared universal model-checking result is the complement of the source's existential path problem, not a quantifier rewrite.

## Narrow closure boundary

This verdict applies only to the nine frozen round-two identities and to N-c-012.d's assigned reader, shared-theorem/model-checking context, bibliography entry, complete source note, source-presentation entry, and two primary authorities. Because MP-F1 and MP-F2 are must-fix findings, N-c-012.d remains open and requires a new frozen rereview. Nothing here closes Alpern--Schneider, N-c-012 as a whole, Part IX, the final publication build, rendered-page inspection, human review, final-book completion, or user acceptance.

REVISE
