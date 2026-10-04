ACCEPT

# Blind integrated publication and terminology audit — R3

## Verdict basis

The current actual LaTeX is publication-admissible at the explicit source-bounded strength it claims. No publication-blocking defect was found in definition-before-use, technical-name discipline, notation scope, source/handbook ownership, citation and locator practice, cross-source parity disclosure, version boundaries, or host integration.

This verdict is deliberately narrower than register closure. It admits the reader-facing synthesis supported by the acquired Vardi--Wolper author preprint, the complete B\"uchi 1962 article, McNaughton's contemporary Project MAC summary, Safra's author-hosted expanded manuscript, and Thomas's May 1996 report precursor. It does not represent the unread registered bodies as read, and it does not promote source-internal sketches, referrals, promises, or open problems into completed proofs.

The audit read `handbook/parts/p09/presentations/n-c-013.tex` lines 1--1409 and `handbook/parts/p09/logic-in-computer-science.tex` lines 723--945 directly from the current tree. It consulted only the five authorized N-c-013 source notes, the compact register row, `handbook/parts/p09/presentations/n-c-018.tex` lines 615--647 for the parity source seat, and the relevant bibliography entries. No prior review, admission, record, transcript, board, or charter artifact was opened. No manuscript render, PDF, PNG, page image, build, test, checker, script, hash, or automated validation was used.

## Exact-line findings

### 1. Definition-before-use and technical-name discipline: no finding

The presentation does not rely on unexplained hypothetical terminology where a definition or an owed artifact is required.

- The Vardi--Wolper source language, computation type, temporal clauses, automaton tuple, run, acceptance condition, and source meanings of semi-determinism and determinism are fixed before use at `n-c-013.tex:17--62`. The distinction between several starts and one start is both stated and used. The handbook's one-start conversion is fully typed and justified at `n-c-013.tex:64--85`.
- The closure, eventuality, and product abbreviations are introduced by displayed definitions at `n-c-013.tex:102--130`, `n-c-013.tex:132--178`, and `n-c-013.tex:180--222`. Lines 128--130 explicitly state that the names are eliminable abbreviations rather than logical primitives. The projection map and projected transition are defined before the projected automaton is invoked at lines 206--218.
- The three extended temporal languages are distinguished by their actual acceptance clauses and assigned the standing of formula languages at `n-c-013.tex:303--328`. The probabilistic path space, cylinder events, sigma-algebra, probability measure, formula event, almost-sure satisfaction clause, and finite support-size parameter are defined at `n-c-013.tex:330--389`. The replacement of the source's overloaded event notation is explicitly motivated at lines 378--387.
- The temporal fragments, ordinary and length-`k` limit equivalence, and probabilistic fairness are given their constructors or eliminable definitions, their standings, their differences from nearby notions, and their immediate uses at `n-c-013.tex:402--472`. The concurrent probabilistic tuple is presented only at the source's displayed strength, with the promised algorithm left deferred at lines 482--505.
- B\"uchi's `SC` is assigned the standing of an interpreted language with its individual and monadic domains at `n-c-013.tex:530--558`. The formula classes, infinitely-often quantifier, and recurrent existential class are defined before the normal-form results use them at `n-c-013.tex:560--606`. The modern finite-data comparison is explicitly eliminable, typed, and distinguished from the article's own terminology at `n-c-013.tex:608--640`.
- The regular-formula class, finite-word congruence, rank, and multiperiodic language class are defined and distinguished before the Sequential Lemma and finite-word bridge use them at `n-c-013.tex:642--730`. `SC_fin`, the ultimately periodic assignment condition, and `SC_per` are each given an exact standing and an immediate use at `n-c-013.tex:833--872`. The source phrase “arithmetically equivalent” is not laundered into a new handbook relation: its missing definition is made explicit and the phrase is not used inferentially at `n-c-013.tex:874--892`. The two formalism variants in the closing problems are defined at the point of use at lines 899--908.
- McNaughton's phrases “regular omega-event” and “finite-state” are handled as unresolved source quotations rather than introduced predicates. Their missing exact definitions and the owed article-body artifacts are stated at `n-c-013.tex:929--946`. This is the required owed-artifact form, not premature terminology.
- Safra's ordered vocabulary tree, determinization state, label invariants, corrected traversal order, and the eliminable meaning and standing of “specific” are supplied at `n-c-013.tex:997--1036`. The definition is then used for the live-node bound at lines 1076--1079. The rejecting sink is introduced only for the demonstrated empty-root case, is distinguished from a tree node, and receives complete transition and acceptance behavior at `n-c-013.tex:1081--1107`. The auxiliary encoding symbol is likewise defined as an encoding value rather than a node or automaton component at lines 1159--1170. “Deterministic in the limit” receives its exact accepting-run definition, contrast with full determinism, and corollary use at lines 1182--1192.
- Thomas's run recurrence set and all four acceptance modes are defined before use at `n-c-013.tex:1204--1266`. Infinite concatenation is defined so that empty factors cannot counterfeit an infinite word at lines 1268--1280. The later Safra-tree tuple is assigned the standing of a determinized word-automaton state and its name, label, and mark components are explicitly distinguished at `n-c-013.tex:1291--1313`. The empty absorbing state, persistent-name allocation, Rabin-pair sets, and current-update mark semantics are defined and justified at lines 1329--1369. Weak MSO is defined at the point of the corollary at lines 1393--1396.
- In the host, deterministic parity and deterministic Rabin word automata are fully typed, their acceptance data are defined, and each is distinguished from B\"uchi acceptance and from tree-automaton standing at `logic-in-computer-science.tex:723--765`. The formula-relevant proposition set and state-label map are defined and type-motivated before the product uses them at `logic-in-computer-science.tex:786--819`.

These passages satisfy the supplied technical-name test: each genuinely new name is necessary for an actual distinction, has an exact definition or explicitly bounded unresolved standing, is assigned a kind, is distinguished from neighboring terms, and is used by the later construction or theorem. Ordinary descriptive prose is not converted into a speculative named apparatus.

### 2. Scope and notation ownership: no finding

The manuscript repeatedly prevents source-specific conventions from being merged merely because later literature uses the same broad name.

- Vardi--Wolper's permitted-start-set convention and the handbook's one-start convention are separated at `n-c-013.tex:44--85`; the source's tuple-order inconsistency is diagnosed without inventing a second convention at lines 224--245.
- Universal-path satisfaction, counterexample-language emptiness, and measure-one satisfaction remain distinct at `n-c-013.tex:248--279` and `n-c-013.tex:330--400`. The probabilistic section expressly refuses to replace a possibly nonempty null counterexample set by ordinary language emptiness at lines 370--377.
- B\"uchi's formula classes, their denotations, finite-word behavior, and modern automaton comparison retain separate standings at `n-c-013.tex:560--680` and `n-c-013.tex:779--789`. The manuscript also prevents the undefined source label `Sigma_2^0` from being conflated with the earlier regular-formula class at lines 822--831.
- Safra's good/bad Rabin-pair order is fixed at `n-c-013.tex:965--995`; Thomas's later excluding/recurring pair order is independently fixed at lines 1241--1266. The two determinization presentations, their node-name reservoirs, update conventions, and pair counts are explicitly kept separate at `n-c-013.tex:1195--1202`.
- Safra's rejecting sink at `n-c-013.tex:1081--1107` and Thomas's empty absorbing automaton state at lines 1329--1339 are each assigned exact local standing. Neither is misdescribed as a live tree node.

All non-source completions are marked as handbook-owned at the point where they enter. This includes the single-start conversion (`n-c-013.tex:64--85`), the worked product example (`n-c-013.tex:281--301`), the modern finite-data comparison for B\"uchi's recurrent formulas (`n-c-013.tex:608--640` and `779--789`), Safra's traversal, specificity, deterministic name choice, empty-root sink, and total label encoding (`n-c-013.tex:1002--1012`, `1023--1035`, `1038--1042`, `1065--1079`, `1081--1107`, and `1159--1170`), and Thomas's initial-name normalization, mark lifetime, subtree deletion, empty-root completion, deterministic name allocation, and accepting-cycle repair (`n-c-013.tex:1305--1349` and `1381--1385`). No source-owned theorem is silently strengthened by one of these completions.

### 3. Citations and locators: no finding

The citations match the source objects actually used, and the locators do not imply access to a different version.

- Vardi--Wolper locators are explicitly preprint-body and appendix locators, not proceedings pagination, at `n-c-013.tex:8--15`. The automaton, translation, Appendix B, model-checking, extended-language, probabilistic, and restricted-fragment claims carry the appropriate preprint-page or appendix locators at lines 62, 87--100, 219--222, 261--279, 323--328, 388--400, 439--447, and 482--505. The lower-bound ownership is separately assigned to Sistla--Clarke in the host theorem at `logic-in-computer-science.tex:821--834`.
- B\"uchi's identity and original printed range are fixed at `n-c-013.tex:516--528`. The mathematical exposition proceeds through bounded locators for pp. 1--10 at lines 539, 606, 680, 700, 730, 750, 777, 820, 844, 872, and 908. The bibliography entry at `handbook/bib/handbook.bib:2276--2288` correctly cites the 1962 Stanford original, pp. 1--11, and does not attach either later reprint DOI to that original.
- McNaughton's 1966 article and the distinct Project MAC report have separate bibliography entries at `handbook/bib/handbook.bib:2290--2299` and `2311--2321`. The only mathematical statement used from the report carries its printed p. 58 locator at `n-c-013.tex:929--938`; the game memo is separately localized and disclaimed at lines 940--946.
- Safra's 1988 proceedings work and the expanded manuscript have distinct entries at `handbook/bib/handbook.bib:2346--2368`. The abstract-level proceedings claim is cited only to the proceedings entry at `n-c-013.tex:948--954`; every detailed construction, proof, count, and application is cited to `Safra1995Extended` with manuscript-page locators at lines 995, 1036, 1079, 1107, 1124, 1145, 1157, 1176, and 1193.
- Thomas's 1996 report and 1997 chapter are separate entries at `handbook/bib/handbook.bib:2370--2391`. All detailed claims use the report entry and its section or page locators at `n-c-013.tex:1204--1396`; no locator is presented as though it came from the unread 1997 chapter.
- The parity definition cites the actual Bradfield--Stirling source at `logic-in-computer-science.tex:741--745`, whose bibliography identity is present at `handbook/bib/handbook.bib:5857--5868`.

### 4. Parity cross-source disclosure: no finding

The compact N-c-013 row requires B\"uchi, Rabin, and parity acceptance, closure, complementation, and the Vardi--Wolper translation (`spec/registers/new-content.csv:120`). The current host supplies each component without pretending that parity came from the five N-c-013 registered works.

- The parity tuple and least-recurring-even clause appear at `logic-in-computer-science.tex:723--740`.
- Lines 741--745 explicitly call it the handbook's deterministic-word specialization of Bradfield--Stirling, identify its later use in Section `sec:p09-presentation-n-c-018`, and cite the source. The authorized source seat at `n-c-018.tex:634--647` supplies the matching least-priority-recurring-even game convention and explains the standing of priorities.
- Rabin acceptance is separately defined from Thomas at `logic-in-computer-science.tex:747--765`; B\"uchi acceptance is explicitly reused at lines 723--725.
- Closure and complementation are stated at `logic-in-computer-science.tex:781--784` and then substantiated at bounded source strength by the Safra and Thomas presentations. The Vardi--Wolper translation is stated at lines 767--779.

The cross-source seat is therefore disclosed rather than silently imported, and the source list is not rewritten to suggest historical parity coverage that the registered works do not supply here.

### 5. Host integration: no finding

The host definitions and theorem statements precede the presentation input and agree with its conventions.

- The word-automaton acceptance definitions occupy `logic-in-computer-science.tex:723--765`; the LTL-to-B\"uchi theorem is at lines 767--779; closure/complementation at lines 781--784; the model-checking method and its correctness/complexity theorem at lines 786--834; and the B\"uchi `SC` theorem package at lines 852--871.
- The product convention in `logic-in-computer-science.tex:786--819` consumes the initial-state label before entering the stored automaton coordinate and consumes each successor-state label on the corresponding product edge. This matches the source-state labeling discussed at `n-c-013.tex:224--259` and supports the path-plus-cycle counterexample statement at `logic-in-computer-science.tex:821--834`.
- The host explicitly includes `n-c-013` after `n-c-012` and before `n-c-014` at `logic-in-computer-science.tex:934--937`. The presentation's cross-references to `def:p09-ltl`, `def:p09-ltl-model-checking`, `thm:p09-ltl-model-checking`, and the earlier B\"uchi definition therefore have an identifiable owner and role; no local redefinition competes with the host theorem package.
- The host's `SC` theorem at `logic-in-computer-science.tex:852--871` preserves the presentation's crucial ownership statement: B\"uchi's recurrent normal form and decision method are source results, while the modern tuple and two-way language packaging are handbook corollaries.

## Open bodies and source-internal boundaries retained without rejection

The following are real open boundaries, but none is disguised or needed for the narrower claims admitted by this verdict.

1. **Vardi--Wolper proceedings comparison.** The accessible file is identified as an author preprint and not a facsimile of the ten proceedings pages at `n-c-013.tex:8--15`. Appendix B's compact proof boundary and the source's cited or deferred results remain visible at lines 96--100, 219--222, 327--328, 439--447, 468--472, 482--512, and 1408--1409.
2. **McNaughton 1966 body.** The ten-page article body remains unread; the publisher/open-archive access state and the narrow Project MAC evidence are stated at `n-c-013.tex:921--946`. No acceptance tuple, construction, proof, example, or modern theorem wording is inferred from the missing body.
3. **Safra 1988 proceedings body.** The proceedings abstract and bibliographic record are separated from the complete author-hosted expanded manuscript at `n-c-013.tex:948--963`. The detailed account is attributed only to the expansion, and lines 1195--1202 expressly refuse proceedings-facsimile or journal-publication status.
4. **Thomas 1997 chapter body.** The detailed source is the May 1996 report precursor. The final chapter is excluded from the source basis at `n-c-013.tex:1398--1407`, so report section numbers, proof repairs, and examples are not represented as verified 1997 chapter content.
5. **B\"uchi's source-internal open material.** The proposed complete axiom system is reported only as a proposal without a soundness-and-completeness theorem at `n-c-013.tex:846--852`; Theorem 3's proof strength is limited to the printed finite-semigroup outline at lines 864--872; and the three historical open problems remain questions at lines 899--908. The complete 1962 article body itself is not open.

The final boundary paragraph at `n-c-013.tex:1405--1409` correctly states the controlling consequence: admission is only of the bounded presentation actually printed, and it does not close McNaughton 1966, Safra 1988, Thomas 1997, or the Vardi--Wolper proceedings-file comparison.

## Publication conclusion

There are no adverse exact-line findings. The exposition consistently defines or explicitly withholds technical names, preserves source-specific conventions, labels handbook repairs, uses version-correct citations, discloses parity's cross-source seat, and integrates coherently with the host definitions and theorem statements. The remaining work is source acquisition and comparison, not a repair prerequisite for publication of this explicitly bounded synthesis.

REGISTER STATUS: OPEN
