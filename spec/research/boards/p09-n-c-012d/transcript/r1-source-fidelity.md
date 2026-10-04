REVISE

# Round-one source-fidelity review: N-c-012.d

## Seat, runtime, scope, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Seat: source fidelity.
- Runtime model/version: no exact runtime model name, version, or build identifier was exposed to this seat. The surrounding role identifies the runtime only generically as Codex/GPT-5-family; that is not an exact version claim.
- Governing charter: `spec/research/boards/p09-n-c-012d/charter.md`, read completely before substantive review.
- Review method: fresh visual reading of the complete controlling journal and conference facsimiles, direct inspection of the complete frozen artifact scope, and mathematical/prose comparison. OCR was not treated as source evidence.
- Independence: I did not inspect `ledger.md`, `transcript/chair.md`, any reviewer transcript, or any reviewer verdict. I did not contact another reviewer.
- Mutation boundary: I created only this assigned transcript. I did not edit the reader, shared Part IX text, bibliography, source note, source-presentation record, charter, sources, or any other file.
- Prohibited activity: I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen-hash verification

Every frozen round-one object was verified against the charter before substantive review. All nine matched exactly. The same nine hashes were rechecked immediately before preparing this transcript and remained unchanged.

| Frozen object | Verified SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A4E1059FB5AE5BB577C76B443D05A26BF31F711449C7537B71027F7E72A958CC` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `5F3903C0793116D497B86FB8DC06CE6AF2DE6B8FA71C727D74F10054F8905A14` | exact match |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` | exact match |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `CF865B89EA3C6C5DF44E9D900D203441B015AF2977F1F383246C52431FCAB533` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E2012A854194277F8C4CC964872428454B2ADEA3624DEE97536833868E37CCE9` | exact match |

## Complete primary-source visual-read record

The journal PDF has seventeen pages corresponding one-for-one to printed pp. 733--749. I opened and visually read every page image at original detail. The conference PDF is a distinct ten-page object corresponding one-for-one to printed pp. 159--168; I likewise opened and visually read every page image at original detail. The PDFs, not OCR, control the findings below.

### JACM 1985, all seventeen printed pages

| Image | Printed page | Visual coverage recorded |
|---|---:|---|
| `journal-page-01.png` | 733 | title, printed author order and affiliations, abstract, descriptors, opening introduction, journal/rights line |
| `journal-page-02.png` | 734 | remainder of introduction and beginning of Section 2 notation/formation rules |
| `journal-page-03.png` | 735 | primitive and restricted syntax, structures, temporal truth clauses, existential truth in an `R`-structure, and the beginning of Section 3 including the complete `init`, `final`, `range`, and `size` definitions at the bottom of the page |
| `journal-page-04.png` | 736 | opening sentence “The following lemmas ...,” Lemmas 3.1--3.2, acceptable subsequence, and the beginning of Lemma 3.3 with the literal strict display and null-sequence basis |
| `journal-page-05.png` | 737 | Lemma 3.3 proof, its non-strict proof inequalities, Theorem 3.4's non-strict conclusion, and Theorem 3.5 |
| `journal-page-06.png` | 738 | chain-of-diamonds 3-SAT construction, Figure 1, and NP procedure |
| `journal-page-07.png` | 739 | completion of Theorem 3.5, Lemma 3.6, Theorem 3.7, and Theorem 4.1 |
| `journal-page-08.png` | 740 | Lemmas 4.2--4.3 and the structure-truth reduction |
| `journal-page-09.png` | 741 | Lemma 4.4, Figure 2, and the journal's literal `2S(n)` next-distance statement |
| `journal-page-10.png` | 742 | completion of Lemma 4.4, source truth sets and their count, Lemma 4.5, the `j >= i` fulfillment definition with inclusive witness endpoints, and the beginning of Lemma 4.6 |
| `journal-page-11.png` | 743 | completion of Lemma 4.6 and Theorem 4.7, including periodic equality, exact bounds, and every-position pending-`U` fulfillment |
| `journal-page-12.png` | 744 | completion of Theorem 4.7 and Theorem 4.1 proof machinery: the `Ff` move, local recurrences, initial-since condition, loop condition, fulfillment check, and Savitch step |
| `journal-page-13.png` | 745 | end of Theorem 4.1, Section 5 finite/infinite generated-string wording with unrestricted index, `N_0 -> a_1 a_2 N_0`, the printed even/odd conflict, ETL closure, and beginning of `Gamma(S,j,N_i)`/Lemma 5.1 |
| `journal-page-14.png` | 746 | completion of Lemma 5.1, finite derivation-tree depth fulfillment, Lemma 5.2, and beginning of Theorem 5.3 |
| `journal-page-15.png` | 747 | completion of Theorem 5.3 and Theorem 5.4's encoded-grammar input and continuation-set algorithm |
| `journal-page-16.png` | 748 | completion of Theorem 5.4, Table I, conclusion and its deliberately nonspecific conference-error notice, and beginning of references |
| `journal-page-17.png` | 749 | remainder of references and receipt/revision/acceptance history |

Controlling enlarged derivatives were also visually read:

- `journal-page-10-bound-crop.png`: the faint p. 742 source-truth-set bound visibly reads `2^length(f)`, not `2^(2 length(f))`.
- `journal-page-13.png`: the full enlarged p. 745 page visibly preserves both defects relevant here: finite-or-infinite strings paired with unrestricted `l >= 0`, and the example/sentence parity conflict.

### STOC 1982, all ten printed pages

| Image | Printed page | Visual coverage recorded |
|---|---:|---|
| `conference-page-01.png` | 159 | separate conference identity, title/authors, abstract/introduction, and conference rights/identifier line |
| `conference-page-02.png` | 160 | notation and temporal semantics, decision problems, and the conference's explicit standalone formal validity clause |
| `conference-page-03.png` | 161 | beginning of the conference Section 3 `L(F)` chain, including its differently numbered model theorem |
| `conference-page-04.png` | 162 | conference Section 3 lemmas/proof material and witness-bound development |
| `conference-page-05.png` | 163 | completion of the conference `L(F)`/NP discussion and transition into the general complexity argument |
| `conference-page-06.png` | 164 | Section 4 reduction material and the literal conference `S(n)` next-distance statement |
| `conference-page-07.png` | 165 | periodic preparation and conference Theorem 4.6, which lacks the journal theorem's every-periodic-position pending-`U` discharge condition |
| `conference-page-08.png` | 166 | abbreviated regular-operator/ETL treatment, including the same parity sentence and no journal finite-tree/termination machinery |
| `conference-page-09.png` | 167 | conference summary display/conclusion and beginning of its coded bibliography |
| `conference-page-10.png` | 168 | remainder of the conference bibliography |

## Frozen artifact read record

I inspected the entire artifact scope fixed by the charter, not isolated search hits:

- `handbook/parts/p09/presentations/n-c-012.tex:1851-2247`: the complete Sistla--Clarke subsection, ending immediately before the Alpern--Schneider subsection at line 2248.
- `handbook/parts/p09/logic-in-computer-science.tex:602-806`: the complete necessary local context for `thm:p09-ltl-pspace` at lines 693--708 and `thm:p09-ltl-model-checking` at lines 794--806, including the intervening automata material needed to audit attribution boundaries.
- `handbook/bib/handbook.bib:2245-2259`: the complete `SistlaClarke1985` entry.
- `spec/research/p09-sistla-clarke-1985-source-note.md:1-758`: the complete source note.
- `spec/research/p09-source-presentations-lot2-3.md:185-197`: the complete `N-c-012.d` source-presentation record.

## Must-fix source-fidelity findings

### SF-1 — the source-note page map moves four definitions from printed p. 735 to p. 736

Disposition: **must revise**.

Source evidence: printed p. 735, `journal-page-03.png`, contains the complete Section 3 definitions of `init(S)`, `final(S)`, `range(S)`, and `size(S)` at the bottom of the page. Printed p. 736, `journal-page-04.png`, begins “The following lemmas ...” and then gives Lemmas 3.1--3.3; it does not introduce those four definitions.

Artifact evidence: `spec/research/p09-sistla-clarke-1985-source-note.md:125-126` maps p. 735 merely to “Section 3 begins” and maps `init`, `final`, `range`, and `size` to p. 736. That is a definite one-page locator error in the note's advertised “Complete journal page map.” The surrounding section-range summary at lines 141--144 does not cure the erroneous row-level map.

Required repair: move `init`, `final`, `range`, and `size` to the printed-p. 735 row and remove them from the printed-p. 736 row; the p. 736 row should begin with the lemmas. This finding engages C8 and C9.

### SF-2 — the advertised exact conference/journal reconciliation omits a material validity-clause difference

Disposition: **must revise**.

Source evidence: the conference prints a standalone formal validity clause on p. 160, `conference-page-02.png`: validity is universally quantified over every structure and every `i >= 0`. The journal's notation/problem presentation on pp. 734--735, `journal-page-02.png`--`journal-page-03.png`, prints no corresponding standalone validity clause.

Artifact evidence: the reader correctly marks its universal clause as reconstruction at `handbook/parts/p09/presentations/n-c-012.tex:1959-1967`, and the note correctly records the journal omission/reconstruction boundary at `spec/research/p09-sistla-clarke-1985-source-note.md:255-260`. But the table titled “Exact material reconciliation with the 1982 conference version,” `spec/research/p09-sistla-clarke-1985-source-note.md:653-681`, contains no row for the conference's explicit clause versus the journal's omission. The table expressly claims to list the material mathematical, proof, bibliographic, and presentation differences, so this is not cured by the earlier journal-only discussion.

Required repair: add a reconciliation row that distinguishes the conference's explicit universal validity clause from the journal's omission, and state that the handbook's universal journal clause is reconstructed. Where the note says “the article does not print” at lines 255--256, “the journal article does not print” would remove the otherwise avoidable cross-version ambiguity. This finding engages C2, C7, C8, C9, I5--I6, and M02.

### SF-3 — one source-note sentence overstates what the journal's correction notice identifies

Disposition: **must revise**.

Source evidence: the conclusion on printed p. 748, `journal-page-16.png`, says only that “one of the theorems used in [9]” contained an error. It does not identify the theorem, the precise invalid inference, or a unique new lemma that repairs it.

Artifact evidence: the note accurately preserves that limit at `spec/research/p09-sistla-clarke-1985-source-note.md:24-33` and again at lines 683--690. It then contradicts that calibration at lines 715--717 by saying that “the authors identify the conference theorem as erroneous.” The definite phrase “the conference theorem” converts an unidentified theorem used in the conference proof into an identified conference theorem.

Required repair: replace that sentence with a formulation such as “the authors report that an unidentified theorem used in the conference proof contained an error”; retain the journal's corrected/expanded Section 5 as controlling without naming a unique bad theorem or unique repair. The source-presentation record at `spec/research/p09-source-presentations-lot2-3.md:185-197` is already calibrated to the non-isolation boundary. This finding engages C5, C7--C9, I5, and M11.

These three defects are independently sufficient for `REVISE`. I found no fourth source-fidelity blocker in the frozen reader, shared theorem text, bibliography entry, or source-presentation record.

## Criteria C1--C9

- **C1 — PASS.** Work identity, printed author order, plural title, *JACM* 32(3), July 1985, pp. 733--749, DOI `10.1145/3828.3837`, ISSN `0004-5411`, receipt history, distinct STOC 1982 object, file identities, archive-link defect, and the access/rights boundary are accurate. Source: journal pp. 733, 749; conference pp. 159--168. Artifact: reader lines 1853--1880; bibliography lines 2245--2259; note lines 35--117.
- **C2 — REVISE.** The reader's syntax, fragments, inclusive `X/U/S` semantics, structure interpretation, existential `R`-truth quantifier, and universal-program relation are accurate, and its journal validity clause is correctly labelled reconstruction. The cross-version record is nonetheless incomplete because SF-2 omits the conference's explicit p. 160 validity clause from the exact reconciliation. Source: journal pp. 734--735; conference p. 160. Artifact: reader lines 1882--1968; note lines 153--260 and 653--681.
- **C3 — PASS.** The reader accurately gives the Section 3 definitions, Lemmas 3.1--3.3, acceptable-subsequence condition, strict/non-strict conflict, Theorems 3.4--3.7, diamond-chain reduction, witness measure, and proof granularity. SF-1 is a locator defect in the source-note page map rather than a defect in this mathematical reconstruction. Source: journal pp. 735--739. Artifact: reader lines 1970--2034; note lines 264--376 and proof-status table lines 626--636.
- **C4 — PASS.** The reduction chain, stuttering boundary, journal `2S(n)` versus conference `S(n)`, source truth sets, `2^length(f)` count, exact fulfillment condition, Lemmas 4.5--4.6, Theorem 4.7 obligations/bounds, `Ff`, initial-since condition, and Savitch step are source-faithful. Source: journal pp. 739--745; conference pp. 164--165. Artifact: reader lines 2036--2129; note lines 378--487 and 653--681.
- **C5 — REVISE.** The reader accurately exposes the ETL finite/infinite typing defect, parity conflict, closure, `Gamma`, tree, distinct fulfillment obligations, Theorems 5.3--5.4, and continuation search. SF-3, however, violates the required correction-notice calibration in the source note. Source: journal pp. 745--748; conference p. 166. Artifact: reader lines 2131--2214; note lines 489--585, 626--647, 683--690, and 715--717.
- **C6 — PASS.** Table I is exact; Theorem 4.1 is kept distinct from the table's `L(U,X)` classification; the shared theorem uses the literal containment `L(U) subset L(U,X) subset L(U,S,X)` at `handbook/parts/p09/logic-in-computer-science.tex:693-708`; and universal model checking is obtained by existential truth of the negated formula plus closure of polynomial space under complement at lines 794--806. Source: journal pp. 739, 748.
- **C7 — REVISE.** Most journal/conference differences are exact, including numbering, `2S(n)`/`S(n)`, periodic obligations, and ETL expansion. SF-2 omits a material validity-clause difference, and SF-3 falsely sounds as if the journal identifies a particular conference theorem. Source: conference pp. 160--168; journal pp. 733--749. Artifact: note lines 653--690 and 715--717.
- **C8 — REVISE.** Bibliography, ordinary reader locators, proof-status table, source-presentation record, file identity, and rights qualification are accurate. SF-1 makes the note's “Complete journal page map” inaccurate at lines 125--126; SF-2 also makes its advertised exact reconciliation incomplete.
- **C9 — REVISE.** The reader itself is independently worded, typed, quantified, definition-before-use, and compliant with the terminology rule. The complete frozen package nonetheless contains SF-1--SF-3: an inaccurate page locator, an omitted material cross-version qualification, and an unsupported identification. Any one forbids acceptance.

## Invariants I1--I15

- **I1 — PASS.** This review was source reading, mathematical reconstruction, and prose inspection only; none of the prohibited verification substitutes was used.
- **I2 — PASS.** All nine frozen hashes matched before review and again before transcript preparation.
- **I3 — PASS.** Every journal page 733--749 and every conference page 159--168 was freshly read visually.
- **I4 — PASS.** The controlling p. 742 crop reads `2^length(f)`; the controlling p. 745 page preserves both specified ETL defects.
- **I5 — REVISE.** Journal and conference results are otherwise kept distinct, but SF-3's “the conference theorem” wording exceeds the p. 748 notice's non-identification boundary.
- **I6 — PASS, with SF-2 as a C7/C8 record omission.** The frozen reader keeps the languages, inclusive semantics, existential truth, and reconstructed universal validity distinct. The source-note reconciliation still must record the conference/journal validity-clause difference.
- **I7 — PASS.** `size(S)` is correctly a finite measure of the infinite structure; acceptable subsequence is exact; the unknown cause of Lemma 3.3's strict/non-strict conflict is not invented.
- **I8 — PASS.** Journal `2S(n)`, conference `S(n)`, `card(SF(f)) <= 2 length(f)`, `2^length(f)`, and `j >= i` with inclusive witness endpoints remain distinct.
- **I9 — PASS.** Theorem 4.7's two conditions, exact bounds, `Ff`, initial-since check, and Savitch step are retained at their printed proof strength.
- **I10 — PASS.** The ETL grammar/constructor, normalization, closure, tree, finite-depth termination, Theorems 5.3--5.4, continuation sets, reconstructed finite-position restriction, and unresolved parity conflict are accurately separated.
- **I11 — PASS.** Proof sketches, asserted inductions, abbreviated cases, and replacements remain unequal. The shared Büchi construction is not attributed to Sistla--Clarke.
- **I12 — PASS.** The five named local notions audited under M15 satisfy necessity, eliminable definition/standing, nonredundancy, and later use; no unsupported hypothetical technical name was introduced.
- **I13 — PASS.** The blind-review independence boundary was obeyed.
- **I14 — PASS.** This seat returns `REVISE`; it does not treat other seats or a majority as able to override the findings.
- **I15 — PASS.** This verdict addresses only the frozen N-c-012.d round-one artifact and makes no wider closure claim.

## Mandatory checks M01--M15

- **M01 — PASS.** The enlarged printed-p. 742 crop visibly reads `2^length(f)`. The reader states that bound at lines 2074--2081; the note distinguishes it from closure cardinality at lines 419--433. No attribution of `2^(2 length(f))` to the paper was found.
- **M02 — REVISE as a cross-version record defect.** Visual inspection confirms no standalone validity clause on journal pp. 734--735, and reader lines 1959--1967 label the universal journal clause reconstruction. Conference p. 160 does print the clause. SF-2 requires that exact difference to appear in the note's material reconciliation at lines 653--681.
- **M03 — PASS.** Printed p. 742 requires `j >= i`; the right-hand `U` witness may occur at an index from `i` through `j`, inclusive. Reader lines 2082--2089 and note lines 438--441 preserve both endpoints.
- **M04 — PASS.** Printed p. 736 displays the strict Lemma 3.3 bound and the null-sequence zero/zero basis; pp. 736--737 use non-strict inequalities throughout the induction; Theorem 3.4 on p. 737 concludes non-strictly. Reader lines 1997--2017 and note lines 297--326 report the conflict without assigning a cause.
- **M05 — PASS.** Journal p. 741 visibly prints `2S(n)` next operators; conference p. 164 visibly prints `S(n)`. Reader lines 2050--2058 and note lines 411--418/671 preserve the respective mapping.
- **M06 — PASS.** Journal Theorem 4.7, pp. 743--744, has the exact exponential prefix/period bounds and requires every `U` formula at every periodic position to be fulfilled before the next copy. Journal Theorem 5.3, pp. 746--747, has the recorded ETL bound and quantified fulfillment conditions. Reader lines 2093--2112 and 2192--2201; note lines 458--487 and 561--580.
- **M07 — PASS.** Journal p. 745 says “finite or infinite string” yet prints an unrestricted `l >= 0`. Reader lines 2144--2155 and note lines 501--514 correctly label the represented-position restriction as handbook-supplied typing rather than printed text.
- **M08 — PASS.** Journal p. 745 prints `N_0 -> a_1 a_2 N_0`; its zero-based clause puts `P` at odd offsets while the following sentence says even states. Reader lines 2160--2169 and note lines 516--533 report the conflict and choose no repair. Conference p. 166 preserves the same parity sentence.
- **M09 — PASS.** Journal pp. 745--746 support the closure and all `Gamma(S,j,N_i)` edge conditions represented at reader lines 2171--2186 and note lines 537--552. Terminal-production membership is kept separate from nonterminal continuation edges.
- **M10 — PASS.** The finite-tree fulfillment depth on p. 746 is distinct from until fulfillment; the Theorem 5.4 search requires the continuation-nonterminal set to become empty within the guessed period. Reader lines 2188--2209; note lines 553--580.
- **M11 — REVISE.** Journal p. 748 does not identify the particular theorem/inference or a unique repairing lemma. Most artifact prose says so, but note lines 715--717 overstate the notice as identifying “the conference theorem.” See SF-3.
- **M12 — PASS.** Reader lines 2123--2129 and the note's proof-status discussion/table at lines 582--647 correctly distinguish proof sketches, asserted inductions, abbreviated cases, and replacements. The automata construction in shared lines 720--792 is attributed outside Sistla--Clarke; no Sistla--Clarke Büchi translation is asserted.
- **M13 — PASS.** Shared theorem lines 693--708 explicitly use `L(U) subset L(U,X) subset L(U,S,X)` to transfer the exact lower and upper bounds and recover the Table I classification.
- **M14 — PASS.** Reader lines 1950--1958 preserve the source's existential `R`-truth problem. Shared model-checking lines 794--806 universally quantify paths by reducing a counterexample to existential truth of the negated formula and then invoke polynomial-space closure under complement; they do not silently alter the source problem's quantifier.
- **M15 — PASS.** Local terminology audit:
  - “acceptable subsequence”: needed to state Lemma 3.3's extraction constraint; exactly defined and typed for a state sequence; distinguished from arbitrary subsequence; used by Lemma 3.3/Theorem 3.4 (`n-c-012.tex:1981-2017`).
  - “source truth set”: exactly defined as the set of `SF(f)` formulas true at a source position; standing is a finite set of formulas, not a new logic or motive; distinguished from `SF(f)` itself and from a valuation; used in Lemmas 4.5--4.6 and Theorem 4.7 (`n-c-012.tex:2060-2112`).
  - “fulfilled before”: exactly defined for `U` and separately for finite-tree regular-operator obligations; standing and witness bounds are explicit; the two uses are not conflated; both feed their respective periodic/termination arguments (`n-c-012.tex:2082-2089, 2188-2209`).
  - ETL formula constructor: grammar-indexed constructor and its generated-string semantics are explicit; it is distinguished from primitive LTL syntax and then used in closure/tree/search (`n-c-012.tex:2131-2186`).
  - `Gamma(S,j,N_i)`: exact set-valued edge/continuation definition with standing fixed; terminal and nonterminal cases are separated; it is used in the derivation tree and subsequent fulfillment/search argument (`n-c-012.tex:2171-2209`).

## Verdict boundary

All source pages were read, all frozen hashes matched, and no unresolved perceptual uncertainty remains. The verdict is nevertheless **REVISE** because the frozen source record contains three definite, source-locatable defects: SF-1's false p. 735/p. 736 page map, SF-2's omitted validity-clause difference in the advertised exact conference/journal reconciliation, and SF-3's over-identification of the p. 748 conference-error notice. Acceptance requires repair and a new independently frozen review round.
