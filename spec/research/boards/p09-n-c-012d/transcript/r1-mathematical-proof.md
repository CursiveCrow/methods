REVISE

# Round-one mathematical/proof review: N-c-012.d

## Identity, independence, and method

- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Runtime model/version: not exposed.
- Seat: mathematical/proof.
- I read the complete board charter before substantive review and reviewed only the frozen round-one snapshot named there.
- I did not inspect `spec/research/boards/p09-n-c-012d/ledger.md`, `transcript/chair.md`, another reviewer transcript, or another reviewer verdict, and I did not contact another reviewer.
- I made no manuscript, shared-surface, bibliography, source-note, source-ledger, or authority edit. This transcript is the only file I created.
- I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build. The work consisted of SHA-256 identity checks, direct visual source reading, mathematical reconstruction, and prose inspection.

## Frozen identities

The following SHA-256 identities were recomputed before substantive review and again immediately before this transcript was filed; every value matched the charter:

| Frozen object | SHA-256 |
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

## Complete visual source record

I visually read `journal-page-01.png` through `journal-page-17.png`, corresponding one-for-one to every printed journal page 733--749. I also visually read `conference-page-01.png` through `conference-page-10.png`, corresponding one-for-one to every printed conference page 159--168. I separately read the enlarged p. 742 exponent crop and the full enlarged p. 745 image. No journal or conference page was unread or uncertain.

The journal page pass covered the title, identity, rights notice, abstract, introduction, syntax and semantics, `R`-structures and the existential path problem, all of Section 3, all of Section 4, all of the corrected Section 5, Table I, conclusion, references, and receipt history. The conference pass covered the complete predecessor syntax and semantics, its expressly printed satisfiability and validity clauses, Section 3 bounds, its `S(n)` computation-distance sentence, its weaker periodic theorem and proof outline, its abbreviated extended-logic proof, summary figure, references, and rights notice.

## Findings

### MP-F1 — Major — the reader assigns one instantaneous description to the wrong graph unit

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2049-2055`, especially line 2051: “each path through a diamond codes one instantaneous description.”
- **Authority:** journal Figure 2 and Lemma 4.4, printed p. 741. The graph has `S(n)` diamonds in a cyclic chain. Each diamond is one tape-cell position and has one vertical vertex for each possible composite/plain tape symbol. The source says: “Each subpath between BI and EI represents an id of M”; a path beginning at BI therefore represents a sequence of instantaneous descriptions. The journal's following sentence uses `2S(n)` `X` operators to relate a tape cell in successive descriptions.
- **Defect:** a path through one diamond selects the symbol for one cell; it does not code an entire instantaneous description. An entire BI-to-EI subpath through the full `S(n)`-diamond chain codes one instantaneous description.
- **Harm:** the frozen sentence changes the combinatorial unit of the PSPACE-hardness construction and obscures why corresponding cells in consecutive BI-to-EI blocks are `2S(n)` positions apart. This is not merely stylistic compression of Figure 2.
- **Exact correction:** replace the sentence by source-exact prose such as: “Each diamond represents one tape-cell position; a subpath from BI through the entire `S(n)`-diamond chain to EI selects one symbol at every position and therefore represents one instantaneous description, while repeated traversals represent a sequence of descriptions.” Retain the separate journal `2S(n)`/conference `S(n)` distinction.

### MP-F2 — Major — the exact source definition of an ultimately periodic structure is omitted and formula-type equality is left to look like the model-periodicity clause

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:2093-2110` and `2192-2201`; `spec/research/p09-sistla-clarke-1985-source-note.md:458-477`; first-use integration prose at `handbook/parts/p09/logic-in-computer-science.tex:781-785` and `794-800`.
- **Authority:** immediately before Lemma 4.6 on printed p. 742, the source defines `S=(s,xi)` to be ultimately periodic with starting index `i` and period `m` iff, for every `k >= i`, `xi(s_k)=xi(s_{k+m})`; Lemma 4.6 separately types the period by `p>0`. Theorem 4.7 on printed p. 743 then requires an ultimately periodic structure **and**, separately, `[s_k]_{S,f}=[s_{k+p}]_{S,f}` plus discharge of every pending `U` formula for every `k>=i`. Theorem 5.3 on printed pp. 746--747 inherits model periodicity and adds its own every-position type equality and both kinds of fulfilment.
- **Defect:** the reader and source note name an “ultimately periodic structure” without ever giving the source's valuation-periodicity definition or explicitly typing `i` and positive `p`. They do print the additional `SF(f)`-truth-set equality. Those are not the same clause: `[s_k]_{S,f}` records only closure formulas relevant to `f`, whereas source model periodicity equates the complete valuations `xi(s_k)` and `xi(s_{k+p})`. The shared integration also uses “ultimately periodic counterexample” before any exact finite-prefix/nonempty-loop definition appears in the handbook.
- **Harm:** the frozen account omits one of the two distinct periodicity requirements in the literal theorem architecture, leaves the domain of the period implicit, and violates the local definition-before-use requirement. It also permits a reader to mistake equality of formula types for the source's definition of periodic structure.
- **Exact correction:** before the first Sistla--Clarke periodic lemma/theorem, state: “For `i in N` and `p in N_{>0}`, `S=(s,xi)` is ultimately periodic with starting index `i` and period `p` iff `forall k>=i, xi(s_k)=xi(s_{k+p})`.” Preserve the separately stated equality of source truth sets and fulfilment obligations in Theorems 4.7 and 5.3. Add the same exact definition with printed-p. 742 locator to the source note. At the earlier shared first use, either define an ultimately periodic word as a finite prefix followed by endlessly repeated nonempty finite loop (`uv^omega`, `v` nonempty) or use that eliminable description instead of the undefined name.

### MP-F3 — Minor but required for an exact source record — the source note gives the Conclusion the wrong terminal page

- **Artifact location:** `spec/research/p09-sistla-clarke-1985-source-note.md:141-144`, especially “Conclusion, pp. 748--749.”
- **Authority:** printed p. 748 contains all of Section 6, “Conclusion,” and then begins `REFERENCES`; printed p. 749 contains references 3--10 and the receipt/revision/acceptance line, but no continuation of Section 6.
- **Defect:** the section map overextends the Conclusion by one printed page, even though the row-by-row page map at lines 138--139 correctly assigns p. 749 to references and dates.
- **Harm:** C8 requires an exact source-note page map, and the source note is internally inconsistent about the terminal locator.
- **Exact correction:** change the section-division sentence to “Conclusion, p. 748; references, pp. 748--749.”

### MP-F4 — Moderate — the claimed complete conference/journal reconciliation omits the predecessor's formal validity definition

- **Artifact location:** `spec/research/p09-sistla-clarke-1985-source-note.md:653-681`, read with the journal reconstruction boundary at lines 227--261. The reader itself correctly labels its clause as reconstruction at `handbook/parts/p09/presentations/n-c-012.tex:1959-1967`.
- **Authority:** conference printed p. 160 explicitly says that `f` is valid iff, for all structures `S=(s,xi)` and all `i>=0`, `S,s_i |= f`. Journal printed pp. 734--735 define formulas, interpretations, temporal truth, satisfiability context, and existential `R`-truth, but print no corresponding standalone validity clause; journal Table I on p. 748 nevertheless includes a validity column.
- **Defect:** the source note correctly reports the journal omission and correctly treats the handbook clause as reconstructed, but its table claims to give the material conference/journal reconciliation and does not record that the formal validity clause was printed in the predecessor and omitted in the journal.
- **Harm:** this is a material definition/proof-ownership difference directly relevant to M02 and to why the frozen handbook must not attribute its displayed universal clause to journal p. 735.
- **Exact correction:** add a reconciliation row: conference p. 160 formally defines validity by all structures and all positions; journal pp. 734--735 omit that definition and journal p. 748 only reports its complexity column; the handbook's identical universal quantifier is therefore explicitly reconstructed for the controlling journal presentation, with the conference wording recorded only as predecessor evidence.

## Criterion-by-criterion disposition

- **C1 — checked clean.** Journal p. 733 visually confirms Sistla-before-Clarke, the plural title, JACM volume 32 number 3, July 1985, printed start page 733, ACM notice, and identifier. Journal p. 749 confirms terminal page 749 and receipt April 1982, revision October 1984, acceptance January 1985. Conference p. 159 confirms the distinct STOC object, author order, pp. 159--168 body, and 1982 ACM notice. The DOI/ISSN, CMU provenance, separate hashes, and no-open-licence boundary in the manuscript, bibliography, source note, and ledger are consistent.
- **C2 — checked clean.** Reader lines 1882--1968 match journal pp. 734--735: the full grammar, `F/G` abbreviation standing, operator-sensitive fragments, `L-tilde(F,X)` atomic-negation restriction, distinct state tokens, inclusive `U/S` endpoints, total finite `R`-structure, and existential path quantifier are exact. The universal-program relation uses absence of an existential path for the negated requirement. The reader expressly marks the universal validity clause as reconstruction. MP-F4 concerns the predecessor comparison record, not a wrong reader semantic clause.
- **C3 — checked clean.** Reader lines 1970--2034 match journal pp. 735--739. `final`, `init`, `range`, and `size` retain the finite-description/infinite-model distinction; acceptable subsequence is defined with its all-same-valuation final-token condition and used by Lemma 3.3; the literal `<` defect, zero/zero atomic basis, proof-supported `<=`, and Theorem 3.4 conclusion are candid. The chain-of-diamonds 3-CNF reduction and Theorems 3.5--3.7 have the right languages, problems, bounds, and proof granularity.
- **C4 — REVISE.** The journal `2S(n)` distance, stuttering boundary, truth-set count, inclusive fulfilment endpoint, every-position obligation, `Ff` move, initial-since check, and Savitch step are correct. MP-F1 misstates the Figure 2 encoding unit. MP-F2 omits the model-level periodicity definition and positive-period typing that the source places before Lemma 4.6 and Theorem 4.7.
- **C5 — checked clean subject to the inherited periodic-definition repair in MP-F2.** Reader lines 2131--2214 match journal pp. 745--748: disjoint grammar nonterminals, grammar-indexed constructor, constant-factor normalization, finite/infinite source conflict and handbook typing, parity defect without an invented repair, exact `SF` enlargement, every `Gamma(S,j,N_i)` continuation edge, terminal-production separation, Lemma 5.1, finite-tree-depth fulfilment, Lemma 5.2, Theorem 5.3 bounds and every-position obligations, input-encoded grammars, `card(SF(f))<=2n`, and continuation-set emptiness within the period.
- **C6 — checked clean.** Reader Table I lines 2216--2246 matches journal p. 748. Shared lines 693--708 correctly use `L(U) subseteq L(U,X) subseteq L(U,S,X)`, with hardness inherited from the left and the upper bound from the right, without falsely putting `L(U,X)` in the literal statement of Theorem 4.1. Shared lines 794--805 correctly complement existential truth of `not A` to obtain universal-path model checking and use deterministic polynomial-space closure under complement; the source path quantifier is not changed.
- **C7 — REVISE.** The numbering, Section 3 bound changes, journal `2S(n)` versus conference `S(n)`, conference recurring-type condition versus journal fulfilment, strengthened journal Theorem 4.7, corrected journal Section 5, and non-unique-repair qualification are all accurate. MP-F4 identifies one omitted material predecessor/journal definition difference in a table presented as complete.
- **C8 — REVISE.** The bibliography entry, identities, hashes, rights boundary, journal physical/printed page map, proof-status table, and pre-admission ledger status are otherwise accurate. MP-F3 is an incorrect section terminal locator; MP-F4 is an omitted material version difference; MP-F2 omits a literal p. 742 source definition from the exhaustive note.
- **C9 — REVISE.** Prose is independently worded, and the five names singled out by M15 are locally defined and used correctly. MP-F1 is a mathematical description error. MP-F2 leaves a source technical term and its typed quantifiers undefined before use in both the reader and earlier shared integration.

## Invariant-by-invariant disposition

- **I1:** complied with; scholarship/prose review only.
- **I2:** complied with; every frozen identity matched before review and immediately before filing.
- **I3:** complied with; all seventeen journal and all ten conference printed pages were freshly read visually.
- **I4:** checked clean. The controlling p. 742 crop reads `2^length(f)`. The enlarged p. 745 image confirms both printed ETL defects.
- **I5:** checked clean. Journal statements, numbering, bounds, and repaired machinery control; no unique erroneous inference or unique repairing lemma is asserted.
- **I6:** checked clean in the reader/shared statement. Languages, inclusive operators, satisfiability, existential `R`-truth, and reconstructed validity remain distinct. MP-F4 is the incomplete predecessor reconciliation.
- **I7:** checked clean. The size measure, acceptable subsequence, and Lemma 3.3 defect are exact.
- **I8:** checked clean. `2S(n)`, `card(SF(f))<=2 length(f)`, `2^length(f)`, `j>=i`, and `i<=l<=j` are all kept distinct and correct.
- **I9:** REVISE for MP-F2. The exact numerical bounds, every-position type equality and discharge, `Ff`, initial-since check, and Savitch step are present, but the model-periodicity definition they presuppose is omitted.
- **I10:** checked clean subject to MP-F2's inherited model-periodicity definition. Every specifically ETL obligation is exact.
- **I11:** checked clean. Sketches, asserted inductions, abbreviated cases, and brief pure-`U` replacement retain their unequal status, and no Büchi proof is attributed to Sistla--Clarke.
- **I12:** REVISE for MP-F2. The named constructions singled out in M15 satisfy the five-part rule, but “ultimately periodic” first appears without its exact eliminable definition and typed period.
- **I13:** complied with; blind independent filing.
- **I14:** applied; the presence of supported defects forces REVISE regardless of any other seat.
- **I15:** preserved; this verdict concerns only N-c-012.d topic-level review and asserts no wider closure.

## Mandatory-check disposition

- **M01 — PASS.** Enlarged journal p. 742 visibly prints `2^length(f)`. Reader lines 2073--2081, source-note lines 419--433, and ledger line 193 reject `2^(2 length(f))` as a source attribution.
- **M02 — PASS in the reader; source-record REVISE under MP-F4.** Journal pp. 734--735 contain no standalone validity definition. Reader lines 1959--1967 label the all-structure/all-position clause as handbook reconstruction. Conference p. 160 does print that clause, which the reconciliation table must record.
- **M03 — PASS.** Journal p. 742 prints `j>=i` and witness `i<=l<=j`; reader lines 2082--2089 are exact.
- **M04 — PASS.** Journal p. 736 literally prints `size(u)<mu(f)` and the null basis; p. 737 prints `<=` in every induction estimate and Theorem 3.4. Reader lines 1997--2017 and source-note lines 310--326 preserve the conflict and do not guess its cause.
- **M05 — PASS.** Journal p. 741 visibly says `2S(n) X operators`; conference p. 164 visibly says `S(n) X operators`. Reader lines 2052--2055 and the source-note reconciliation retain that difference. MP-F1 concerns the adjacent encoding-unit description.
- **M06 — REVISE for MP-F2.** Journal p. 743 confirms `i<=2^(1+length(f))`, `p<=4^(1+length(f))`, and both conditions for every `k>=i`. Journal pp. 746--747 confirm `l<=2^(1+card(SF(f)))`, `p<=c^card(SF(f))`, and both kinds of fulfilment at every periodic position. The frozen numerical bounds and every-`k` clauses are exact, but the inherited quantifier types and valuation-periodicity definition are absent.
- **M07 — PASS.** Journal p. 745 says “finite or infinite string” and then universally quantifies `l>=0`. Reader lines 2144--2155 clearly marks the represented-index restriction for a finite word as handbook-supplied typing.
- **M08 — PASS.** Journal p. 745 prints `N_0 -> a_1 a_2 N_0` and says `N_0(True,P)` checks even states. Its zero-based clause checks the second argument at offsets 1,3,... . Reader lines 2160--2169 records the conflict and chooses no authorial repair.
- **M09 — PASS.** On journal p. 745, `Gamma(S,j,N_i)` has root `N_i(f_1,...,f_q)`; a depth-`l` node headed by `N_k` receives an `N_r` child exactly for a continuation production `N_k -> a_p N_r` with `S,s_{j+l}|=f_p`. Reader lines 2171--2186 includes the exact closure and edge condition and keeps terminal productions outside continuation edges.
- **M10 — PASS.** Journal p. 746 defines negated-grammar fulfilment from maximum finite-tree depth `d` by every `m>=j+d`; this is distinct from an until witness. Journal pp. 747--748 initializes and updates the continuation-nonterminal set and requires it to become empty during the periodic part. Reader lines 2188--2209 is faithful.
- **M11 — PASS.** Journal p. 748 says only that one theorem used in the conference proof contained an error and that the journal submissions independently corrected it. Reader lines 1873--1880 and 2209--2213 and source-note lines 24--33, 683--690 do not identify a bad inference or unique repairing lemma.
- **M12 — PASS.** The proof-status table and reader lines 2009--2034, 2123--2129, and 2209--2213 preserve every inspected sketch/assertion/abbreviation boundary. All twenty-seven source pages contain no Sistla--Clarke Büchi construction, and none is attributed.
- **M13 — PASS.** The shared theorem's exact inclusions give PSPACE-hardness from `L(U)` and membership from `L(U,S,X)`. This correctly explains the Table I `L(U,X)` row without altering Theorem 4.1's literal three-language list.
- **M14 — PASS.** Journal p. 735 defines existential path truth. Shared lines 794--805 use an existential witness for `not A` and complement it, with PSPACE closure under complement, to obtain universal-path model checking. The source problem is never silently universalized.
- **M15 — PASS for all five specified names.** Reader lines 1985--1995 gives necessity, exact definition, standing, nonredundancy, and use for acceptable subsequences; lines 2060--2091 does so for source truth sets and until fulfilment; lines 2131--2158 for the grammar-indexed ETL constructor; and lines 2171--2192 for `Gamma` and the finite-tree fulfilment obligation. MP-F2 is a separate omitted source definition not cured by those five clean checks.

## Checked-clean mathematical reconstruction

Beyond the four findings, the source-to-reader mathematics is consistent. In particular: the source closure bound and p. 742 truth-set count are not conflated; the `2^length(g)` count used in Theorem 4.7 is mathematically justified by truth assignments to actual subformulas with single-negation mates dependent; the inclusive fulfilment endpoint is preserved; the prefix and period bounds follow from the repeated-type reductions; past `S` explains the move to `g=Ff`; Theorems 4.7 and 5.3 retain obligations at every periodic position; the ETL finite-tree/König argument and continuation-set termination condition are correctly separated; `L(U,X)` is classified by exact syntactic containment; and universal model checking is the complement of existential truth for the negated formula, not a redefinition of the source problem.

The four corrections above are finite and local, but they affect an exact complexity reduction, a literal theorem definition/quantifier boundary, and two claimed-exact source-record surfaces. Under I14 and the charter verdict rule, this snapshot cannot be accepted.

REVISE
