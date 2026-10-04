REVISE

# Round-three blind adversarial publication/AGENTS review: N-c-012.d

## Identity, method, and independence

- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Runtime model/version: not exposed to this reviewer.
- Seat: adversarial publication and AGENTS compliance.
- I read the complete charter before substantive review and treated this round-three snapshot, not any prior verdict or memory of an earlier round, as controlling.
- I did not inspect `spec/research/boards/p09-n-c-012d/ledger.md`, `transcript/chair.md`, any round-one or round-two transcript (including this seat's earlier transcripts), or either other round-three transcript. I did not contact another reviewer.
- I made no manuscript, shared-file, source-note, source-ledger, bibliography, or authority edit. The only file created is this transcript.
- I ran no test, test harness, automated checker, repository script, TeX command, handbook-PDF inspection, or build. Review consisted only of direct source-image reading, prose and mathematics inspection, and the expressly required SHA-256 identity checks.

## Frozen identities

All ten round-three identities matched the charter before substantive review and again immediately before filing:

| Frozen object | Verified SHA-256 |
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

## Authority body and artifact coverage

I visually reread every page of the controlling seventeen-page JACM facsimile, printed pp. 733--749, and every page of the distinct ten-page STOC predecessor, printed pp. 159--168. I separately inspected the controlling p. 736 acceptable-subsequence crop, the p. 742 exponent crop, and the full p. 745 image; the images, rather than OCR or the source note, controlled symbol and inequality adjudication.

I then read the complete frozen Sistla--Clarke subsection at `n-c-012.tex:1851--2387`, its adjacent GPSS and Alpern--Schneider boundaries, the necessary shared LTL language/complexity/model-checking surfaces at `logic-in-computer-science.tex:599--809` and the complexity-atlas row at `logic-in-computer-science.tex:2219--2222`, both complete bibliography entries at `handbook.bib:2245--2274`, the complete 867-line source note, and the complete N-c-012.d source-presentation entry at `p09-source-presentations-lot2-3.md:185--257`.

## Findings

### AP-F1 — BLOCKER — Theorem 3.5's polynomial certificate still invokes an unstated labelling algorithm

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2126--2138`, especially lines 2135--2137. The source note has the same compression at `spec/research/p09-sistla-clarke-1985-source-note.md:423--433`, especially lines 429--431; the source-presentation entry likewise stops at “checked subformula labels” at `spec/research/p09-source-presentations-lot2-3.md:235--239`.
- **Claim:** The reader gives the bounded prefix, strongly connected set, connecting edge, and acceptance test, but replaces the certificate's load-bearing verifier with the phrase “the source's recursive subformula-labelling rules.” Those rules are neither defined there nor anywhere else in the scoped reader/shared files. Consequently the newly named procedure lacks an exact algorithmic definition, and a first-time reader cannot verify that the guessed prefix/SCC data are a polynomially checkable certificate for `L(F)` truth.
- **Primary evidence:** Journal p. 738 prints the actual algorithm. For every node `x` of `p'` or `C`, it initializes `label(x)` to the empty set; processes each `g` in `SF(f)` in increasing order of `length(g)`; and gives four exact update clauses: an atomic clause using `P in eta(x)`, a negation clause, a conjunction clause, and the crucial eventuality clause. For `g=F g_1`, the last clause adds `g` at `x` exactly when `g_1` occurs in some label in `C`, or when `x` is in `p'` and `g_1` occurs at a later node of `p'`. Journal p. 739 then accepts iff `f` is in `label(q_0)` and states the polynomial bound. The eventuality clause is what connects the finite prefix/SCC representation to an infinite path; it is not recoverable from the words “recursive rules” alone.
- **Publication harm:** C3 and M27 require the polynomial certificate and printed labelling procedure, not merely a pointer to an unnamed procedure in the authority. The present prose also violates I12's five-part technical-name rule: “recursive subformula-labelling rules” names a procedure with no local exact definition, no explicit standing, and no nonredundancy account. The omission hides the only non-Boolean certificate clause and makes the NP-membership explanation non-reproducible.
- **Smallest exact correction:** At lines 2135--2137, replace the placeholder with the four source clauses, including empty initialization and increasing-formula-length order. State explicitly that the labels are metalinguistic certificate data, not temporal truth sets newly postulated by the handbook; that the special `F` clause is needed because `C` represents the infinitely recurring suffix; and that these clauses are used immediately by the start-label acceptance test. Mirror the exact content in the source note and source-presentation entry, or make those records point to the complete reader display without calling their present compression complete.

### AP-F2 — MUST FIX — Lemma 4.3 collapses the `X`-based transition encoding and the distinct pure-`U` stuttering construction

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2157--2162`. Compare the more exact source-note record at `spec/research/p09-sistla-clarke-1985-source-note.md:482--497`.
- **Claim:** The reader says only that Lemma 4.3 introduces one proposition per graph state and constrains “successive labels” to follow `R`, followed by the observation that Lemma 4.2 supplies invariance for `L(U)`. That does not state how the reduction eliminates `X`, and it risks suggesting that the same immediate-successor constraint is available in the stuttering-insensitive pure-`U` language. The source uses two materially different formulas, including a self-loop/non-self-loop split, precisely because pure `U` cannot express the immediate-next constraint unchanged.
- **Primary evidence:** Journal p. 740 first builds the `X`-based clause `f_x = P_x -> (g_1 and not g_2 and X g_3)`, plus the global exactly-one/state-label constraints and the start assertion. It then replaces only `X g_3` by
  - `P_x U g_3` when `(x,x)` is not in `R`, and
  - `G(P_x) or [P_x U (g_3 and not P_x)]` when `(x,x)` is in `R`.
  Here `g_3` is the disjunction of successor-state propositions. The source explicitly explains that the first case can repeat `P_x` finitely many times and invokes Lemma 4.2 to show that this stuttering leaves every `L(U)` formula unchanged. The source note preserves this exact two-case replacement; the reader does not.
- **Publication harm:** C4 requires the exact Section 4 reduction chain and stuttering boundary. The current prose does not let a reader check the reduction's language membership, its treatment of self-loops, or the logical role of Lemma 4.2. It also weakens the presentation's otherwise careful separation of operator bases by hiding the very construction that makes the pure-`U` case different.
- **Smallest exact correction:** Expand lines 2157--2162 with the definitions of the state propositions, successor disjunction, global exactly-one/label constraints, and start assertion; then display the two-case pure-`U` replacement above and state exactly where Lemma 4.2 licenses finite repetition. Mark the formulas as source reconstruction of Lemma 4.3, not a modern model-checking encoding. This also supplies definition, standing, nonredundancy, and use for the reduction data at their first appearance.

### AP-F3 — MUST FIX — Theorem 5.4 reports only the negated-obligation tracker and omits the positive grammar-formula consistency clause

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2342--2349`; the source note similarly summarizes only continuation tracking at `spec/research/p09-sistla-clarke-1985-source-note.md:678--684`.
- **Claim:** The reader correctly states that grammars are part of the input, gives `card(SF(f)) <= 2n`, and describes the continuation-nonterminal set for a negated grammar formula. It omits the separate local consistency condition that tells the on-the-fly procedure when a positive formula `N_j(f_1,...,f_q)` belongs to the guessed truth set at the current state. Without it, “tracks ... and requires that set to become empty” is not a complete description of the modified Theorem 4.1 procedure: it checks termination of negative obligations but never states how positive grammar constructors are propagated or discharged.
- **Primary evidence:** Journal p. 747 prints both parts. Before defining the negative tracker, it requires `N_j(f_1,...,f_q)` to be in the current guessed set iff either (1) a continuation production `N_j -> a_k N_l` has `f_k` true now and `N_l(f_1,...,f_q)` true in the next guessed set, or (2) a terminal production `N_j -> a_k` has `f_k` true now. Only after that clause does the source initialize and update the sets for negated formulas and require each to become empty somewhere in the period; p. 748 uses both families of checks with Lemma 5.1.
- **Publication harm:** C5 requires exact Theorem 5.4 input encoding and continuation-set search. The missing positive clause is a different rule family from the negative finite-tree termination condition; collapsing the algorithm to the latter obscures source proof ownership and leaves the PSPACE membership procedure incomplete at the point where the reader claims to describe it.
- **Smallest exact correction:** Immediately before the negated-obligation paragraph, state the source's two-way positive membership rule with both continuation and terminal production cases. Then retain the existing negative tracker, explicitly distinguishing local positive constructor consistency from finite-tree termination of a negated constructor. State that these are metalinguistic checks on guessed subformula sets and are used together in Theorem 5.4's acceptance argument.

## What the snapshot gets right

The strongest case for admission is substantial. The snapshot now gives unusually careful source/version scholarship: it identifies the complete journal and conference objects separately; preserves the journal's inclusive `U/S` semantics and existential `R`-truth quantifier; labels the validity clause as a handbook reconstruction; defines the unique maximal recurring suffix and every ambient-relative acceptable-subsequence operation before use; discloses both strict-sign defects with the null cases and proof-supported non-strict inequalities; preserves `2^length(f)` and journal `2S(n)`; states every-periodic-position fulfillment in Theorem 4.7; and gives a source-faithful ETL finite/infinite typing repair, parity conflict, `Gamma` definition, bounds, and correction boundary. The shared theorem also correctly derives the `L(U,X)` classification by containment and obtains universal model checking by complementing the existential counterexample query rather than changing the source quantifier. The three findings above do not undermine those repaired facts; they show that three proof-critical procedures remain referenced rather than reconstructed.

## Criterion-by-criterion disposition

- **C1 — checked clean.** Journal title, author order, issue/date/pages/DOI/ISSN, receipt history, CMU provenance, seventeen-page identity, distinct ten-page STOC object, hashes, archive-link/version warning, and the conditional ACM rights boundary agree with journal pp. 733 and 749, conference pp. 159--168, the bibliography, source note, and ledger.
- **C2 — checked clean.** `L(O_1,...,O_k)`, `L-tilde(F,X)`, finite proposition alphabet, formula grammar, inclusive `X/U/S`, structures, total finite `R`-structures, existential path quantifier, satisfiability, universal-program counterexample relation, and the reconstructed validity clause are defined and not conflated. Journal pp. 734--735 and conference p. 160 support the stated version boundary.
- **C3 — REVISE.** Structure and acceptable-subsequence definitions, Lemmas 3.1--3.3, both strict-sign conflicts, Theorems 3.4--3.7, Figure 1, formula measures, and proof-status labels are otherwise accurate, but AP-F1 leaves the polynomial certificate's labelling verifier undefined.
- **C4 — REVISE.** The theorem list, stuttering boundary, Figure 2 unit, terminal-state convention, journal/conference next distance, truth-set count, fulfillment condition, periodicity, exact Theorem 4.7 bounds/obligations, `Ff`, initial-since check, and Savitch step are correct. AP-F2 omits the exact pure-`U` reduction that makes the stuttering argument work.
- **C5 — REVISE.** Grammar syntax, finite/infinite repair, parity defect, normalized closure, labelled `Gamma`, Lemmas 5.1--5.2, the distinct fulfillment condition, Theorem 5.3, encoded-input bound, negative continuation set, and non-unique correction boundary are accurate. AP-F3 omits Theorem 5.4's positive grammar-constructor consistency rule.
- **C6 — checked clean.** All Table I rows and three columns are present; Theorem 4.1's narrower displayed list is distinguished from the `L(U,X)` table row; the shared theorem uses the exact containment sandwich; universal model checking is derived from existential truth of the negation and closure of deterministic polynomial space under complement.
- **C7 — checked clean.** The conference/journal comparison keeps pagination, syntax, validity, closure, restricted-fragment proof, Section 3 bounds/numbering, stuttering lemma, `S(n)`/`2S(n)`, halting/persistent terminal behavior, periodic invariant, Section 5 repair, and conclusion wording separate. It does not name the unidentified erroneous inference or a unique repair.
- **C8 — checked clean.** Both bibliography objects resolve independently and accurately; direct conference claims cite `SistlaClarke1982`, journal claims cite `SistlaClarke1985`; page map and proof-status table match the images; source note and source-presentation ledger preserve provenance and rights limits; the ledger honestly says fresh round-three review remains pending.
- **C9 — REVISE.** The prose is independently worded and most terms meet the five-part rule, but AP-F1--AP-F3 leave proof-critical rule families as names or descriptions without local exact clauses. That is a first-time-reader and definition-before-use failure, not copyediting.

## Invariant-by-invariant disposition

- **I1:** complied with; scholarship/prose review and SHA-256 checks only.
- **I2:** complied with; all ten identities matched twice before filing.
- **I3:** complied with; all journal pp. 733--749 and conference pp. 159--168 were freshly visually read.
- **I4:** checked clean; the controlling crop shows `2^length(f)`, and p. 745 shows both source conflicts.
- **I5:** checked clean; journal controls, numbering is separated, and no unique error/repair claim appears.
- **I6:** checked clean; formula classes, inclusive semantics, existential truth, satisfiability, and reconstructed validity remain distinct.
- **I7:** checked clean; the unique maximal suffix, exact structure and subsequence measures, both literal strict signs, null counterinstances, non-strict proof uses, and unknown causes are explicit.
- **I8:** checked clean; journal `2S(n)`, closure versus realized-type count, `j >= i`, and the inclusive witness endpoint are exact.
- **I9:** checked clean; periodic valuation equality, source-type equality, every-position obligation discharge, exact bounds, `Ff`, initial-since, and Savitch are separately stated.
- **I10:** REVISE because AP-F3 leaves the Theorem 5.4 positive rule family absent; the grammar, constructor, normalization, closure, `Gamma`, finite-tree obligation, bounds, negative tracker, typing repair, and parity conflict themselves are correct.
- **I11:** checked clean; proof sketches/inductions/brief replacements are differentiated and no Sistla--Clarke Buchi construction is claimed.
- **I12:** REVISE for the unstated rule/reduction families in AP-F1--AP-F3. The explicitly audited named terms—acceptable subsequence, subscripted ambient operations, source truth set, both fulfilled-before obligations, the grammar constructor, and `Gamma`—do satisfy necessity, definition, standing, nonredundancy, and later use.
- **I13:** complied with; blind independence preserved.
- **I14:** applied; any one of AP-F1--AP-F3 requires REVISE independently of other seats.
- **I15:** preserved; this verdict concerns only the frozen N-c-012.d topic and closes nothing larger.

## Mandatory-check disposition

- **M01 — clean:** p. 742 and the crop print `2^length(f)`; the reader never attributes `2^(2 length(f))` to the source.
- **M02 — clean:** no standalone journal validity clause appears on pp. 734--735; conference p. 160 prints it; reader lines 1960--1973 disclose the journal-relative reconstruction.
- **M03 — clean:** reader lines 2205--2209 preserve `j >= i` and `i <= ell <= j`.
- **M04 — clean:** p. 736 prints `<` in the preparatory union sentence and Lemma 3.3; null/null and atomic/null refute strictness; p. 737 repeatedly uses `<=`; Theorem 3.4 concludes non-strictly. Reader lines 2050--2105 disclose both defects and the proof-supported repair.
- **M05 — clean:** conference p. 164 prints `S(n)`; journal p. 742 prints `2S(n)`; reader lines 2173--2176 cites each separately.
- **M06 — clean:** Theorem 4.7 and Theorem 5.3 bounds, positive period, equality, and every-periodic-position obligations match journal pp. 743--744 and 746--747.
- **M07 — clean:** journal p. 745 says finite or infinite but writes unrestricted `l >= 0`; reader lines 2288--2293 labels the represented-index restriction as handbook typing.
- **M08 — clean:** p. 745's alternating word and even-state sentence conflict with the zero-based second argument at odd offsets; reader lines 2298--2307 chooses no repair.
- **M09 — clean:** closure contains every same-grammar nonterminal head; `Gamma` root/depth/continuation-production edge condition is exact; terminal productions remain outside continuation edges.
- **M10 — clean:** maximum tree depth, distinct negated-grammar fulfillment, and negative continuation set becoming empty within the period are exact.
- **M11 — clean:** the conclusion identifies only an erroneous theorem used by the conference proof, not the inference or a unique repairing lemma.
- **M12 — clean:** all named proof-granularity qualifications are retained; no automata proof is imported.
- **M13 — clean:** the shared theorem uses `L(U) subseteq L(U,X) subseteq L(U,S,X)` in the correct hardness/upper directions.
- **M14 — clean:** the shared theorem keeps the source query existential and obtains universal checking by negation plus deterministic-space complement closure.
- **M15 — clean for its enumerated terms:** acceptable subsequence, ambient subscripts, source truth set, both fulfillment obligations, constructor, and `Gamma` meet all five local conditions. I12 nevertheless fails for the three separate rule-family placeholders in AP-F1--AP-F3.
- **M16 — clean:** the page map places structure measures on p. 735, conclusion on p. 748, and references on pp. 748--749.
- **M17 — clean:** conference validity and journal reconstruction are separated, and the correction notice is no stronger than the source.
- **M18 — clean:** Lemmas 3.2, 3.3, and 3.6 retain the zero-prefix clause, acceptable input/output, every-intermediate-supersequence and surviving-position quantifiers, finite subsequence containing the current state, and the disclosed strict/non-strict conflict.
- **M19 — clean:** one diamond is one cell, one BI-to-EI traversal one instantaneous description, repeated traversals a history; journal persistence and conference halting language are separate.
- **M20 — clean:** model periodicity is complete-valuation equality for every `k >= i` with positive period, distinct from type equality and both obligations.
- **M21 — clean:** shared lines 781--787 and 799--802 give a finite product path plus nonempty cycle and its infinite unfolding without an undefined periodicity term.
- **M22 — clean:** `Gamma(S,j,N_i)` is called only a labelled tree/`Gamma`; no proof-tree, derivation-tree, or continuation-tree synonym appears in scope.
- **M23 — qualified clean on admitted repairs, but not sufficient for acceptance:** the round-two targeted repairs are present without regression; AP-F1--AP-F3 are fresh publication defects in the same frozen snapshot.
- **M24 — clean:** reader lines 1975--1996 give the unique maximal suffix, exact prefix/suffix decomposition, range, and size before use.
- **M25 — clean:** reader lines 2019--2050 define the ambient-relative operations, explicitly make subscript `S` eliminable and metalinguistic, explain necessity/nonredundancy/standing, and use it below.
- **M26 — clean:** the preparatory strict sign, null/null counterinstance, proof-supported non-strict subadditivity, and the prior definition and standing of `mu(f)` are all present and source-exact.
- **M27 — REVISE:** the bound, subset, restricted strong connectivity, connecting edge, node domain, and final acceptance condition are present, but AP-F1 shows that the promised printed labelling procedure itself is not reconstructed.
- **M28 — clean:** the distinct conference entry is bibliographically accurate, and direct version claims resolve to the appropriate key.
- **M29 — REVISE overall:** the new suffix/subsequence/strict-sign/certificate metadata is source-exact and does not regress older repairs, but AP-F1--AP-F3 prevent the round-three snapshot from satisfying C1--C9, I1--I15, and M01--M29 as a whole.

## Premortem

Assume this topic shipped and later failed scholarly review. The likely failure is not a wrong headline theorem or bound; those are now carefully controlled. A reader attempts to reproduce the NP certificate, the pure-`U` graph reduction, or the ETL PSPACE verifier and discovers that each proof-critical step is represented by a label—“recursive subformula-labelling rules,” “constraining successive labels,” or negative continuation tracking—while the actual source clauses are absent. The ordinary theorem/bound/version checklist can miss this because every surrounding numerical statement is correct. The definition-before-use and proof-reproducibility checks expose it: the missing `F` label clause, self-loop-sensitive `U` replacement, and positive grammar consistency rule are precisely the nontrivial clauses. The narrow repair is to state those source rules, not to add a modern automata proof or broaden the topic.

## Narrow closure boundary

This is a REVISE verdict on only the exact frozen N-c-012.d round-three integrated unit. It says nothing adverse about the already checked source identities or the many successful round-three repairs. It does not close N-c-012.d, Alpern--Schneider, N-c-012 as a whole, Part IX, the final post-freeze build, rendered inspection, human review, final-book completion, or user acceptance.

REVISE
