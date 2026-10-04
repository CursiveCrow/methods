REVISE

# Round-three mathematical/proof review: N-c-012.d

## Reviewer, method, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research`.
- Assigned seat: mathematical/proof.
- Runtime model/version: not exposed to this agent.
- I read the complete updated charter before substantive review and used only its frozen round-three snapshot.
- I visually reread every journal page 733--749 and every conference page 159--168. I also inspected the enlarged p. 736 acceptable-subsequence crop, the enlarged p. 742 exponent crop, and the full p. 745 image. The primary images controlled over OCR, prior memory, and the source note.
- I read the complete frozen Sistla--Clarke reader scope, `n-c-012.tex` lines 1851--2387; the necessary shared temporal/model-checking scope in `logic-in-computer-science.tex` lines 599--809; both bibliography entries; the complete 867-line source note; and the complete N-c-012.d source-presentation entry, lines 185--257.
- I did not open `ledger.md`, `transcript/chair.md`, any r1/r2 transcript, or any other reviewer transcript. I did not contact another reviewer. Near the end of the audit, the orchestration layer automatically delivered an unsolicited completion notification from another seat into this agent context. I did not open the cited transcript or treat the notification as authority; I re-opened the controlling source images and checked every finding below directly. Because the notification itself exposed another seat's verdict, strict blind non-exposure was not perfectly preserved. This procedural exposure independently precludes an `ACCEPT` under I13--I14 and should be cured by a genuinely isolated rerun after the substantive repairs below.
- I made no manuscript, shared-file, bibliography, source-note, ledger, or board-record edit. This transcript is the only file I created. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build. Read-only SHA-256 calculation and primary-source image viewing were the only mechanical operations.

## Frozen identities

Every one of the ten round-three identities matched both before substantive review and immediately before this filing:

| Frozen object | Expected and observed SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `1F5792A97766A695A58EF5FAA259F97D8CD6E50B720FB14BEDEA358E3505E7F8` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `3C1F2DEB6D3224D61E1008B59DF353F56BE096A951E936B0060C583497E37565` |
| `spec/research/p09-source-presentations-lot2-3.md` | `414CFAEF19DB8F53B76E6A4805EA20F3D2DABFCA245FC0DD6F537FE32F8253DE` |

## Primary pages visually read

- JACM 1985: printed pp. 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, and 749. This covered the title/rights wrapper, complete journal body, Table I, conclusion, references, and receipt/revision/acceptance line.
- STOC 1982: printed pp. 159, 160, 161, 162, 163, 164, 165, 166, 167, and 168. This covered the complete predecessor body, Figure 3, bibliography, and every conference/journal comparison made by the frozen artifacts.
- Controlling enlarged evidence: the p. 736 acceptable-subsequence image visibly prints both strict signs and defines `mu(f)` before Lemma 3.3; the p. 742 crop visibly prints `2^length(f)`; the full p. 745 image visibly prints “finite or infinite,” the unrestricted index, and the even-state sentence for `N_0(True,P)`.

## Findings

### MP-F1 — Must fix — the explicit `2S(n)` sentence has the wrong printed-page locator

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2173--2176`.
- **Frozen claim:** the sentence correctly says that the journal uses `2S(n)` nested next operators, but it attaches `\cite[p.~742]{SistlaClarke1985}`.
- **Authority evidence:** the literal sentence “Using `2S(n)` X operators, the relation between the contents of a tape cell in successive ids can be asserted” appears on printed p. 741, below Figure 2. Printed p. 742 begins with the continuation of the pure-`U` formula and does not contain the `2S(n)` sentence. The conference predecessor's distinct `S(n)` sentence is correctly located on printed p. 164.
- **Harm:** the mathematical value and version distinction are correct, but the pinpoint citation is false. It fails C8 and the exact-locator part of M05/M28.
- **Exact correction:** change only the journal pinpoint attached to the `2S(n)` sentence from `\cite[p.~742]{SistlaClarke1985}` to `\cite[p.~741]{SistlaClarke1985}`. Preserve the adjacent conference p. 164 citation and the broader pp. 741--742 citation for the whole reduction.

### MP-F2 — Must fix — the promised exact Theorem 3.5 certificate omits the printed bottom-up labelling procedure

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:2126--2138`; `spec/research/p09-sistla-clarke-1985-source-note.md:423--433`; `spec/research/p09-source-presentations-lot2-3.md:235--239` and its delivery claim at lines 243--255.
- **Frozen claim:** the reader and source note say only that the machine runs “the source's recursive subformula-labelling rules.” They do not state the rules, their evaluation order, or the exact `F` case. The ledger nevertheless calls the certificate infrastructure repaired, and M27 requires the exact procedure.
- **Authority evidence:** printed pp. 738--739 specify the certificate construction and algorithm. A satisfying path is decomposed as `q=q'·q''`, with `q''` the unique maximal suffix whose occurring states recur infinitely. Lemma 3.3 supplies a subsequence `u` of `q'` of length at most `length(f)`; `p'` must contain `u` and be obtained from `q'` by deleting cycles, yielding `length(p') <= length(f) card(N)`. For every `x` in `p'` or `C`, the source initializes `label(x)` to the empty set, processes `g in SF(f)` in increasing order of `length(g)`, and prints four rules:
  1. for `g=P`, add `g` exactly when `P in eta(x)`;
  2. for `g=not g_1`, add `g` exactly when `g_1` is absent from `label(x)`;
  3. for `g=g_1 and g_2`, add `g` exactly when both conjuncts are in `label(x)`;
  4. for `g=F g_1`, add `g` exactly when either some `y in C` has `g_1 in label(y)`, or `x in p'` and some later `y in p'` has `g_1 in label(y)`.
  Printed p. 739 accepts exactly when `f in label(q_0)`.
- **Harm:** the omitted fourth rule is the mathematical link between the finite prefix/SCC certificate and eventuality semantics; “recursive rules” is not an exact reconstruction and does not let a reader verify the NP procedure. The omission directly fails C3 and M27, and makes the source note's proof-chain closure overstate its contents.
- **Exact correction:** put the decomposition/extraction relationship, initialization, increasing-length order, all four iff rules, and final acceptance test in the reader. Put the same exact procedure in the source note. The compact ledger may point to that complete reconstruction, but it must not claim the exact certificate repaired until the reader/note actually contain it.

### MP-F3 — Must fix — the stated Theorem 3.5 certificate does not ensure that its guessed `C` supports an infinite suffix

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:2132--2138`; `spec/research/p09-sistla-clarke-1985-source-note.md:427--433`; `spec/research/p09-source-presentations-lot2-3.md:235--239`. Compare the handbook's own explicit cycle condition for the later Büchi product at `handbook/parts/p09/logic-in-computer-science.tex:782--787`.
- **Frozen claim:** the reconstructed certificate checks only that the restricted graph on `C` is strongly connected and that the last node of `p'` has an edge into `C`; it then asserts that the infinite witness can remain in `C` and visit every member infinitely often.
- **Authority evidence and source boundary:** printed p. 738 itself prints only the strong-connectivity and entry-edge checks. It does not separately require an edge or directed cycle inside a singleton `C`, and it does not define “strongly connected” using positive-length self-reachability. Under the standard reflexive-reachability definition, a one-vertex graph with no self-loop is strongly connected but cannot support an infinite path confined to that vertex.
- **Concrete counterexample:** let the total graph have nodes `q_0,c,d`, edges `q_0 R c`, `c R d`, and `d R d`. Let `P` hold at `q_0,c` and fail at `d`. From `q_0` the only infinite path falsifies `G P`, equivalently `not F not P`. Nevertheless the printed/frozen checks can choose `p'=(q_0)` and `C={c}`: the singleton restricted graph is strongly connected in the standard sense, the entry edge exists, and the printed labels make `F not P` absent and hence `G P` present at `q_0`. The procedure therefore accepts without a genuine infinite suffix through `C`.
- **Harm:** as reconstructed, the NP-membership certificate is unsound under the handbook's ordinary SCC convention. The shared product construction's separate “contains a cycle” condition confirms that strong connectivity alone is not being used elsewhere as a synonym for cyclicity. This is a source-level proof omission/ambiguity that the handbook currently silently inherits, contrary to its treatment of the strict-sign and ETL defects.
- **Exact correction:** preserve the literal p. 738 source check, disclose the missing singleton-cycle condition, and supply a clearly handbook-owned repair: additionally require that `R intersect (C times C)` contain a directed cycle (equivalently, for singleton `C`, require its self-loop; for larger strongly connected `C`, no extra condition is needed). Then the finite strongly connected restricted graph supports an infinite walk visiting every node infinitely often. Do not attribute this extra condition to the printed paper unless a source definition establishing positive-length self-reachability is acquired.

### MP-F4 — Must fix for the charter's exact Section 4 scope — Lemmas 4.5--4.6 and the Theorem 4.1 recurrence checks are only gestured at

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:2213--2214` and `2252--2259`; `spec/research/p09-sistla-clarke-1985-source-note.md:526--560`.
- **Frozen claim:** the artifacts say that Lemma 4.5 “handles deletion,” that Lemma 4.6 “uses” fulfilment when a segment is repeated, and that the search checks Boolean/`X`/`U`/`S` consistency. They omit the exact hypotheses/conclusions and the directional recurrence clauses. C4 requires those exact statements and search conditions.
- **Authority evidence, Lemma 4.5 (printed p. 742):** if `[s_i]_{S,f}=[s_j]_{S,f}` and `S'` is obtained by replacing the sequence with `(s_0,...,s_{i-1},s_j,s_{j+1},...)` and restricting the valuation, then every state token present in both sequences has the same source truth set in `S` and `S'`. The precise retained endpoint and common-state quantifier are part of the statement.
- **Authority evidence, Lemma 4.6 (printed pp. 742--743):** for `p>0`, assume `[s_i]_{S,f}=[s_{i+p}]_{S,f}` and every `U`-formula in `[s_i]_{S,f}` is fulfilled before `s_{i+p}`. Let `S'` be ultimately periodic from `i` with period `p` and agree with `S` in valuation at every `k<i+p`. Then, for every `g in SF(f)`, (a) at every `k<i+p`, `S,s_k |= g` iff `S',s'_k |= g`; and (b) at every `k>=i`, `S',s'_k |= g` iff `S',s'_{k+p} |= g`.
- **Authority evidence, Theorem 4.1 search (printed p. 744):** with present and next guessed source truth sets, the paper checks
  - `X f_1` present iff `f_1` is next;
  - `f_1 U f_2` present iff `f_2` is present or both `f_1` is present and `f_1 U f_2` is next;
  - `f_1 S f_2` is next iff `f_2` is next or both `f_1` is next and `f_1 S f_2` is present;
  - conjunction present iff both conjuncts are present;
  - negation present iff its operand is absent.
  At the initial point it separately checks `f_1 S f_2` present iff `f_2` is present, and during the loop it discharges every `U` obligation recorded at the loop entry.
- **Harm:** the omitted directions are mathematically load-bearing, especially the asymmetric `S` recurrence and the two conclusions of Lemma 4.6. The current prose does not meet C4's “exact ... Lemmas 4.5--4.6 ... and Theorem 4.1 search conditions” requirement, even though its theorem bounds and high-level proof description are correct.
- **Exact correction:** state the two lemmas with their exact typed maps, inequalities, retained positions, and both conclusions; then print the five local recurrence/Boolean iff checks and retain the already correct initial-since, loop-equality, fulfilment, linear-space, and Savitch qualifications. Record the same exact statements in the source note's proof chain.

### MP-F5 — Must fix for the charter's exact Section 5 scope — Lemma 5.2 and the Theorem 5.4 grammar checks remain underspecified

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:2328--2350`; `spec/research/p09-sistla-clarke-1985-source-note.md:657--684`.
- **Frozen claim:** the artifacts accurately identify the additional finite-tree obligation and say that Theorem 5.4 tracks continuation nonterminals until the set becomes empty, but they omit Lemma 5.2's exact inherited conclusions and both exact update conditions printed for the search.
- **Authority evidence, Lemma 5.2 (printed p. 746):** take `S,i,p,f` and `S'` exactly as in Lemma 4.6, add the hypothesis that every subformula of the form `not N_u(f_1,...,f_q)` in `[s_i]_{S,f}` is fulfilled before `s_{i+p}`, and then conclusions (a) and (b) of Lemma 4.6 hold for ETL as well.
- **Authority evidence, positive grammar check (printed p. 747):** `N_j(f_1,...,f_q)` is in the guessed current truth set iff either (1) a continuation production `N_j -> a_k N_l` exists, `f_k` is current, and `N_l(f_1,...,f_q)` is next, or (2) a terminal production `N_j -> a_k` exists and `f_k` is current.
- **Authority evidence, negative continuation update (printed pp. 747--748):** for each negated grammar formula at the beginning of the period, initialize its tracked set to `{N_j}`. Update it to the set of all `N` for which some production `N_p -> a_k N` has `N_p` in the current tracked set and `f_k` in the current truth set. Require that set to become empty at some point in the period. Together with the positive consistency checks, this excludes finite and infinite witnesses as Lemma 5.1 requires.
- **Harm:** the current prose preserves the main idea but not the exact algorithm or Lemma 5.2 statement required by C5/I10. A reader cannot reconstruct which production form consults the next truth set, which consults only the current set, or the exact frontier transition.
- **Exact correction:** add the exact Lemma 5.2 hypothesis/conclusions, the positive iff rule, the singleton initialization, the exact set-comprehension update, and the within-period emptiness test. Keep the already correct encoded-input bound, `card(SF(f))<=2n`, proof-status qualification, and journal-versus-conference correction boundary.

## Criterion-by-criterion disposition

- **C1 — clean.** The plural title, author order, JACM 32(3), July 1985, pp. 733--749, DOI, ISSN, printed affiliations, receipt/revision/acceptance history, CMU provenance, two distinct source objects and hashes, and cautious rights boundary all agree with pp. 733/749 and conference p. 159.
- **C2 — clean.** The source grammar, `L(O_1,...,O_k)` standing, restricted `L-tilde(F,X)`, inclusive `U/S`, structures, total `R`-structures, existential path quantifier, universal-program counterexample relation, and explicitly reconstructed validity clause are correctly separated. The full atom/Boolean clauses are present in the source note and the shared reused-LTL boundary is explicit.
- **C3 — REVISE.** The ambient definitions, Lemmas 3.1--3.3, both strict defects, Theorems 3.4/3.6/3.7, Figure 1, and formula measures are correct. MP-F2 omits the exact Theorem 3.5 labelling algorithm, and MP-F3 identifies an undisclosed soundness condition/source gap in that certificate.
- **C4 — REVISE.** Stuttering, the structure-to-satisfiability reduction, computation encoding, `2S(n)` value, type count, fulfilment, periodicity, Theorem 4.7 bounds/obligations, `Ff` move, initial-since condition, and Savitch step are correct. MP-F1 repairs the pinpoint locator; MP-F4 supplies the exact Lemma 4.5/4.6 statements and recurrence checks currently omitted.
- **C5 — REVISE.** The grammar semantics, finite/infinite typing disclosure, parity disclosure, closure, `Gamma` edges, two distinct fulfilment notions, Theorem 5.3 bounds, encoded-input bound, and correction calibration are clean. MP-F5 supplies the exact Lemma 5.2 and Theorem 5.4 rules required for completeness.
- **C6 — clean.** Table I is transcribed correctly; `L(U,X)` is distinguished from Theorem 4.1's displayed list; `L(U) subseteq L(U,X) subseteq L(U,S,X)` correctly transfers hardness and membership; and the shared universal model-checking theorem uses complement of existential truth rather than changing the source quantifier.
- **C7 — clean.** The ten-page conference and seventeen-page journal versions are kept separate. The conference `S(n)`, journal `2S(n)`, changed terminal behavior, theorem renumbering/strengthening, closure change, and corrected Section 5 are accurately reconciled. No unique bad inference or uniquely repairing lemma is invented.
- **C8 — REVISE.** Work identity, bibliography, page map, citation keys, rights language, and proof-status table are otherwise clean. MP-F1 is a false pinpoint, and MP-F2/MP-F4/MP-F5 mean the source note and ledger overstate exact proof-chain closure.
- **C9 — REVISE.** The prose is independently worded and generally definition-before-use; the handbook's subscripted ambient notation satisfies the terminology rule. The exact-procedure omissions and undisclosed singleton-cycle gap prevent complete mathematical/proof acceptance.

## Invariant-by-invariant disposition

- **I1 — complied.** Scholarship/prose review only; no prohibited execution.
- **I2 — complied.** All ten hashes matched twice before filing.
- **I3 — complied.** All 27 printed source pages were freshly read visually.
- **I4 — clean.** The controlling p. 742 crop reads `2^length(f)`; p. 745 shows both ETL conflicts.
- **I5 — clean.** Journal controls; source does not identify a unique conference error or repair.
- **I6 — clean.** All language, problem, and validity distinctions remain separate.
- **I7 — clean.** Unique maximal suffix, decomposition, ambient-relative measures, both strict defects, null counterexamples, and proof-supported non-strict bounds are exact.
- **I8 — clean apart from MP-F1's citation.** The mathematical `2S(n)`/`S(n)` distinction, closure/type distinction, and inclusive fulfilment endpoint are correct.
- **I9 — REVISE through MP-F4.** The bounds, every-position obligations, `Ff`, initial-since, and Savitch clauses are present and correct; the exact local recurrence machinery is not.
- **I10 — REVISE through MP-F5.** Grammar/closure/tree/bounds/conflicts are correct; exact Lemma 5.2 and continuation update machinery are incomplete.
- **I11 — clean.** Proof sketches, asserted inductions, abbreviated cases, brief `U` replacement, and printed proofs remain distinguished; no Sistla--Clarke Büchi construction is claimed.
- **I12 — clean.** The source terms and handbook ambient subscripts have local definition, standing, nonredundancy, necessity, and use. No unsupported hypothetical name was added.
- **I13 — procedural blocker disclosed above.** No prohibited transcript/record was opened and no reviewer was contacted, but an unsolicited orchestration notification exposed another verdict; rerun in an isolated context is required for literal blind closure.
- **I14 — complied.** No majority reasoning was used; defects require `REVISE`.
- **I15 — clean.** The ledger keeps the narrow downstream closure boundary open.

## Mandatory-check disposition

- **M01 — clean:** p. 742 visibly prints `2^length(f)`.
- **M02 — clean:** no formal validity definition occurs on journal pp. 734--735; the reader marks its clause reconstructed and cites conference p. 160 separately.
- **M03 — clean:** `j>=i` and `i<=l<=j` are exact.
- **M04 — clean:** both literal `<` signs, null failures, subsequent `<=` uses, and Theorem 3.4's non-strict result are preserved.
- **M05 — REVISE only as locator:** journal value `2S(n)` and conference value `S(n)` are correct, but MP-F1 fixes journal p. 741.
- **M06 — clean:** Theorems 4.7 and 5.3 have exact bounds and every-periodic-position obligations.
- **M07 — clean:** finite/infinite source wording and handbook-supplied represented-index typing are candid.
- **M08 — clean:** the even/odd mismatch is exactly disclosed without choosing a repair.
- **M09 — clean:** `SF` expansion and every `Gamma(S,j,N_i)` continuation-edge condition are exact; terminal productions remain separate.
- **M10 — REVISE for exact algorithmic completion:** the depth obligation and within-period emptiness requirement are present, but MP-F5 supplies the missing initialization and transition rule.
- **M11 — clean:** no precise conference bad inference or unique repair is asserted.
- **M12 — clean:** proof status and absence of a Büchi construction are accurate.
- **M13 — clean:** the containment chain gives the exact Table I classification used by the shared theorem.
- **M14 — clean:** universal model checking is the complement of existential truth for the negated formula, with deterministic PSPACE closure.
- **M15 — clean:** all listed terminology passes the five-part local rule.
- **M16 — clean:** the page map puts base measures on p. 735, conclusion on p. 748, and references on pp. 748--749.
- **M17 — clean:** conference validity and the unidentified correction notice are exact.
- **M18 — clean:** Lemmas 3.2, 3.3, and 3.6 have the exact boundary conditions and every-intermediate-supersequence scopes.
- **M19 — clean:** one diamond is one tape cell; one BI--EI traversal is one instantaneous description; repeated traversals form a computation; the journal persistence and conference halting wordings are separate.
- **M20 — clean:** model periodicity is exact complete-valuation equality for natural `i`, positive `p`, and every `k>=i`, distinct from type equality and obligations.
- **M21 — clean:** the shared product requires an accepting SCC containing a cycle and returns a finite path plus nonempty cycle. That correct condition also exposes MP-F3 in the Theorem 3.5 reconstruction.
- **M22 — clean:** `Gamma` is called only the labelled tree/`Gamma`; no unsupported tree synonym appears.
- **M23 — clean for the charter-enumerated repairs, subject to the fresh defects above:** no weakening of the repaired definitions, bounds, version separation, or source-defect disclosures was found.
- **M24 — clean:** unique maximal suffix, `s=init(S)·final(S)`, `range`, and `size` precede use.
- **M25 — clean:** every acceptable-subsequence measure is ambient-relative; the reader's `S` subscript is explicitly eliminable, metalinguistic, necessary, nonredundant, and used.
- **M26 — clean:** the preparatory strict sign, null/null counterexample, non-strict subadditivity, and prior definition of `mu` as the number of `F` occurrences are exact.
- **M27 — REVISE:** the prefix/SCC/entry skeleton and acceptance slogan are present, but the exact printed labelling procedure is omitted (MP-F2), and the asserted infinite suffix needs the disclosed cycle repair (MP-F3).
- **M28 — clean apart from MP-F1:** `SistlaClarke1982` is a distinct accurate entry and direct conference claims use it; the one journal pinpoint is wrong by one page, not by source key.
- **M29 — REVISE:** the round-three snapshot is improved and the new strict-sign disclosure is source-exact, but MP-F1--MP-F5 and the procedural exposure prevent closure.

## Checked-clean mathematical record

For avoidance of doubt, I found no further mismatch in the following material: source/version identity and rights; exact general and restricted grammars; inclusive `X/U/S` semantics; existential `R`-truth and reconstructed validity; `final/init/range/size`; Lemmas 3.1--3.3 and 3.6 quantifiers; Theorems 3.4, 3.5, 3.7 result strengths; Figure 1 reduction; journal terminal-machine persistence; Figure 2's graph unit; p. 742 type count; fulfilment endpoint; valuation periodicity; Theorem 4.7's prefix/period bounds and every-position obligations; the `Ff` proof move; ETL grammar normalization; finite/infinite and parity defects; exact `SF` closure; `Gamma` edge typing; Lemma 5.1; the finite-tree depth obligation; Theorems 5.3--5.4 result strengths; Table I; the conference/journal difference table; the two bibliography records; and the shared containment/complement arguments.

## Narrow closure boundary and verdict

This verdict concerns only the frozen N-c-012.d integrated unit. Repair and a new isolated three-seat review would still close only N-c-012.d topic-level manuscript review. It would not close Alpern--Schneider, N-c-012 as a whole, Part IX, any build, rendered inspection, human review, final-book completion, or user acceptance.

REVISE
