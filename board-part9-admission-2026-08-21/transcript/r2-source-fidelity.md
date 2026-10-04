REJECT

# Part IX admission board, round 2: source-fidelity/evidence

Author: source-fidelity/evidence seat  
Decision scope: current live reader graph rooted at handbook/parts/p09.tex and handbook/annex/p09.tex; live cross-part destinations; the five Part IX calculus sheets routed in Part XIV; bibliography, symbol, named-result, generated-audit, and P9 register obligations  
Review mode: source/content review only; no manuscript, annex, bibliography, registry, generator, generated-source, or test edit; no test and no TeX/PDF build

## Independence disclosure

This report was independently derived from the current manuscript, registry, and authority files. During a late search for the binding-amendment text, an intended transcript-exclusion glob failed on Windows and emitted a few matched snippets from Part IX R1 transcripts. That accidental exposure occurred after the current-file findings below had been established. I stopped immediately, did not use those snippets as evidence or as substitutes for current inspection, and re-ground every disposition below in current live locations and authorities. No other reviewer transcript was intentionally opened or read.

## Frozen snapshot reviewed

| Live file | Lines | SHA-256 |
|---|---:|---|
| handbook/parts/p09.tex | 3 | a414f249cb2d46013d902176d09bbd11a176551775929f2837d62dab4fc3b0d1 |
| handbook/parts/p09/logic-in-computer-science.tex | 1385 | 906eb3f4fabbd5ba280d20eca62cb5ce165b6ebd87586a16e1722a3b22f5e2d2 |
| handbook/annex/p09.tex | 3 | 4d4da30f2f3b5c2f730da6b8081a14c36af88eb7f1614f1ba832f9ffde529876 |
| handbook/annex/p09/proofs.tex | 196 | aae6e781ef8294141fc189f61a2b86b8815684b1d085dd4577b22303eb6e5f57 |
| handbook/generated/audit-p09.tex | 80 | 200fb92f53d7510dbe277a2c556329ddd83f75c2e2d08ee6a64d22fa34196184 |
| handbook/parts/p14/rule-sheets.tex | 114 | 76352929817beadaf24d20398bcfd05a2b08857e9cbb2314d47fb20b6f5b6181 |
| handbook/registry/symbols.csv | 679 | 526a3a789d1e7fee37afaf402397bc42feb86ef7975af1c61e40556209bf681e |
| handbook/bib/handbook.bib | 5812 | 9b3f8299c984b91b2d1a762a462c4276ec0c62248650bd50cba8d6cb25e8b602 |

The verdict is a source/content rejection, not a build, visual, provenance, human, or user-gate ruling. The current route is much more complete than a survey stub: it has 1,385 body lines, four reciprocal annex proofs, five live sheets, 64 generated audit rows, 45 contiguous P9 symbol rows, and no reader-visible OPEN/owed notice. Nevertheless, the following current defects require correction before source/content admission.

## Findings

### SF9-R2-F1 [blocker] [open] The printed ALC tableau never initializes the tested concept or ABox concept assertions

Location: handbook/parts/p09/logic-in-computer-science.tex:257-292; handbook/registry/calculi/tableaux-alc.tex:2-20; handbook/annex/p09/proofs.tex:3-55; generated status row handbook/generated/audit-p09.tex:23-24; obligation N-c-009 at spec/registers/new-content.csv:116.

Claim: The theorem says that the registered completion procedure has a complete open branch exactly when the finite concept/TBox/ABox input is satisfiable.

Evidence: The method creates one node per ABox individual, declared role edges, and a fresh tested-concept root at handbook/parts/p09/logic-in-computer-science.tex:265-267. It then says only that every node label contains internalized GCIs at lines 268-269. It never inserts a tested concept \(C\) into the tested root and never inserts an ABox assertion \(D(a)\) into \(\mathcal L(a)\). The sheet likewise has a global-GCI rule and the four ordinary expansion rules at handbook/registry/calculi/tableaux-alc.tex:11-16, but no initialization clause for either datum.

This is falsified internally without relying on a source convention. With empty TBox and ABox and tested concept \(\bot\), the printed procedure creates an unlabelled fresh root, performs no rule, finds no clash, and accepts an unsatisfiable concept. With tested concept \(\top\), empty TBox, and ABox \(\{A(a),\neg A(a)\}\), it creates the named root but never places either assertion in its label, and again accepts an unsatisfiable knowledge base. The annex completeness direction assumes exactly the missing facts when it concludes at handbook/annex/p09/proofs.tex:52-53 that named roots satisfy the ABox and the tested root satisfies the tested concept. The standard source construction begins concept satisfiability with an initial assertion \(C_0(x_0)\); see the author-hosted [Baader--Horrocks--Lutz--Sattler description-logic text](https://www.cs.ox.ac.uk/people/ian.horrocks/dlbook/main.pdf), Chapter 4.

Exact correction: define initialization before expansion and duplicate it exactly on the sheet. For every named individual \(a\),
\[
\mathcal L(a)=
\{\operatorname{nnf}(D):D(a)\in\mathcal A\}
\cup\mathsf{Glob}(\mathcal T),
\]
retain an \(r\)-edge for every \(r(a,b)\in\mathcal A\), label the tested root by
\(\{\operatorname{nnf}(C)\}\cup\mathsf{Glob}(\mathcal T)\), and give a TBox-only anonymous root the global set. State whether the concept test is conjoined with knowledge-base consistency. Then repair the proof invariant at annex lines 15-30 and make lines 52-53 cite those initialization clauses. Regenerate the audit only after the theorem is true.

Disposition: blocking mathematical/proof-status defect. The reciprocal proved= route exists, but its proof proves a stronger initialized procedure than the one the reader is given.

### SF9-R2-F2 [blocker] [open] Two results have duplicate live public identities instead of exact cross-part reuse

Locations:

- Trakhtenbrot: handbook/parts/p09/logic-in-computer-science.tex:57-63,1277-1280; handbook/parts/p03/finite-model-theory.tex:96-100; exact inherited anchor handbook/parts/p04.tex:42-50; handbook/generated/audit-p09.tex:16; handbook/generated/named-theorem-index.tex:424-425.
- ROBDD: handbook/parts/p09/logic-in-computer-science.tex:593-610; live Part XII definition/theorem handbook/parts/p12/sat-and-certificates.tex:122-154, reached through handbook/parts/p12.tex:45 and handbook/parts/p12/automation-and-mechanization.tex:4; handbook/generated/audit-p09.tex:43-44; handbook/generated/named-theorem-index.tex:348-349.

Claim: The board requires one public identity per result and exact cross-part reuse.

Evidence: Part III explicitly says that the single public Trakhtenbrot identity is exact inherited Theorem thm:trakhtenbrot and that another chapter must use it without creating a second statement identity. Part IX nevertheless creates thm:p09-trakhtenbrot with the same finite-signature statement and publishes both identities side by side in the named index.

Part IX also defines def:p09-robdd and proves thm:p09-robdd-canonicity. The live Part XII route independently defines def:p12-robdd and publishes thm:p12-robdd-canonicity. The two theorem statements are equivalent formulations of Bryant canonicity under one fixed variable order, use the same source, and appear as consecutive duplicate titles in the named-result index. This is semantic duplication even though each label individually has exactly one generated index row.

Exact correction:

1. Delete the local Part IX Trakhtenbrot theorem environment and replace every P9 use, including the complexity table, by Theorem thm:trakhtenbrot. Remove the P9 audit/named row on regeneration.
2. Choose one ROBDD definition and one canonicity theorem as canonical. On the current route, the narrowest repair is to make Part IX cross-reference def:p12-robdd and thm:p12-robdd-canonicity before explaining their symbolic-model-checking use, and delete the P9 duplicate identities. If ownership is instead moved to Part IX because N-c-017 is a P9 obligation, then Part XII must be changed to cross-reference the P9 identities. Keeping both is not an admissible option.

Disposition: blocking public-identity and exact-reuse defect.

### SF9-R2-F3 [blocker] [open] The prefix-class paragraph makes a false Skolemization claim and does not supply the registered Löwenheim source role

Location: handbook/parts/p09/logic-in-computer-science.tex:171-220, especially 187-206 and 215-220; cross-part table handbook/parts/p02/first-order-depth.tex:199-223; bibliography records handbook/bib/handbook.bib:5465-5474 and 5607-5616; obligations N-c-005 and N-c-008 at spec/registers/new-content.csv:112,115.

Claim: “Skolemization may introduce constants but not positive-arity functions in the rows above.”

Evidence: The table itself prints the Ackermann prefix \(\exists^*\forall\exists^*\) and the Gödel--Kalmár--Schütte prefix \(\exists^*\forall^2\exists^*\). Standard Skolemization of
\(\forall x\,\exists y\,R(x,y)\), an Ackermann-row sentence with an empty leading block, introduces \(y=f(x)\); standard Skolemization of
\(\forall x\forall z\,\exists y\,R(x,z,y)\) introduces \(y=f(x,z)\). Thus positive-arity Skolem functions do arise from the trailing existential blocks. Only the leading existential witnesses in the Bernays--Schönfinkel--Ramsey row become constants. The cited [Börger--Grädel--Gurevich book](https://link.springer.com/book/9783540423249) is the governing classification source; the printed sentence confuses a function-free input vocabulary with the vocabulary of its Skolem form.

The next phrase says validity uses a prefix “reversed.” Negating a prenex sentence dualizes each quantifier in place; it does not reverse the positional order of the quantifiers. That wording should be made exact.

The registered monadic item is specifically Löwenheim--Behmann decidability and names both historical sources. P9 cites Behmann1922 but not Lowenheim1915 at lines 177-178, while the reused P2 table controls only the exact modern Lewis1980 complexity row. The primary Löwenheim record already exists at handbook/bib/handbook.bib:5465-5474 and matches the [Springer record for the 1915 paper](https://link.springer.com/article/10.1007/BF01458217); it is simply not given a P9 claim role.

Exact correction: replace lines 217-220 by three separate clauses: (i) all displayed input vocabularies are relational/function-free; (ii) BSR leading existentials can be represented by constants, whereas Skolemizing the trailing Ackermann/GKS existentials creates unary/binary Skolem functions and does not keep the formula inside the original function-free input class; and (iii) validity is reduced by negation and in-place quantifier dualization. Add a narrowly historical sentence citing Lowenheim1915 and Behmann1922, while leaving Lewis1980 responsible only for the modern exact complexity bound.

Disposition: blocking false mathematical statement plus an open registered source role.

### SF9-R2-F4 [major] [open] The description-logic table equates source logics with standardized OWL profiles without the normative source

Location: handbook/parts/p09/logic-in-computer-science.tex:314-348, especially 325-342; handbook/bib/handbook.bib:5618-5667 and 5711-5727; obligation N-c-010 and apparatus A-095 at spec/registers/new-content.csv:117 and spec/registers/apparatus.csv:96.

Claim: The rows identify “EL++ / OWL 2 EL,” “DL-Lite_R / OWL 2 QL,” and “SROIQ / OWL 2 DL” while citing only pre-standard or DL-reasoning papers.

Evidence: The normative [W3C OWL 2 Profiles Recommendation](https://www.w3.org/TR/owl2-profiles/) defines each profile by a grammar and global restrictions. It says OWL 2 EL has its basis in the EL family and cites EL++; it says OWL 2 QL is based on the DL-Lite family and that DL-Lite_R provides its logical underpinning. Those are source/underpinning relations, not literal identity. The Recommendation also distinguishes ontology consistency, class satisfiability/subsumption, instance checking, and conjunctive-query answering, and separates combined from data complexity. There is no W3C OWL 2 source record in the current bibliography.

Exact correction: replace each slash identity by a typed relation: “EL++ source family; OWL 2 EL is the distinct standardized profile,” “DL-Lite_R logical underpinning; OWL 2 QL is the distinct standardized profile,” and “SROIQ(D) logical foundation/direct-semantics relation; OWL 2 DL retains its own structural restrictions.” Add and cite the relevant W3C Recommendation record, with its editors in editor roles, for profile syntax and mapping. Keep BaaderBrandtLutz2005, CalvaneseEtAl2007, HorrocksKutzSattler2006, and Kazakov2008 responsible only for their DL language/reasoning claims. State the exact reasoning problem and data/combined measure separately for the standardized profile.

Disposition: source-family transfer and source-role blocker under charter lines 12-16.

### SF9-R2-F5 [major] [open] Three cited/source-controller surfaces do not match the complete printed claim

Locations:

- Status grammar: handbook/CONVENTIONS.md:60-72.
- PDL theorem: handbook/parts/p09/logic-in-computer-science.tex:751-764; sheet handbook/registry/calculi/hilbert-pdl.tex:2-12; audit handbook/generated/audit-p09.tex:50-51.
- CQ theorem: handbook/parts/p09/logic-in-computer-science.tex:1160-1180,1318-1320; audit handbook/generated/audit-p09.tex:72-73.
- Hoare source control: handbook/parts/p09/logic-in-computer-science.tex:22-29,785-829; sheet handbook/registry/calculi/hoare-while.tex:2-10; obligation N-c-019 at spec/registers/new-content.csv:126.

Claim: A cited=<bibkey> token means the named source carries the proof of the complete statement.

Evidence:

1. thm:p09-pdl-adequacy is statused cited=KozenParikh1981 but bundles calculus completeness, an exponential finite-model bound, and EXPTIME-completeness. Kozen and Parikh's [author-hosted paper and abstract](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf) carry completeness of the Segerberg axioms. The manuscript itself assigns the finite-model/complexity clause to FischerLadner1979 inline; the [publisher record](https://www.sciencedirect.com/science/article/pii/0022000079900461) describes the exponential upper and lower decision bounds. One status source does not control the bundled statement.
2. thm:p09-cq-complexity is statused cited=Vardi1982 but bundles fixed-query uniform AC0, combined evaluation NP-completeness, and containment NP-completeness. Vardi's [primary paper](https://www.cs.rice.edu/~vardi/papers/stoc82.pdf) introduces data, expression, and combined evaluation complexity. The Chandra--Merlin source, already used for the adjacent homomorphism theorem, is the primary conjunctive-query evaluation/containment source; see the [IBM publication record](https://research.ibm.com/publications/optimal-implementation-of-conjunctive-queries-in-relational-data-bases). The containment clause is not controlled by the single Vardi status.
3. The Hoare sheet prints both partial rules and an integer-variant total-while rule but lists only Floyd1967, Hoare1969, and Cook1978 as controlling sources. The body source-standing paragraph names Apt1981, and N-c-019 expressly assigns Apt a role. Apt's institutional [Ten Years of Hoare's Logic record](https://ir.cwi.nl/pub/10268) and paper distinguish partial from total correctness and print a refined total-while rule. The sheet currently gives that source no role and does not explain that its displayed direct variant rule is a derived presentation.

Exact correction:

- Split PDL completeness from finite-model/decision complexity into separately statused results, cited respectively to KozenParikh1981 and FischerLadner1979, or use a single verified source that actually carries every retained clause.
- Split CQ evaluation complexity from CQ containment complexity. Assign the fixed/data/combined evaluation claims to a verified controller and assign containment to ChandraMerlin1977; do not leave the complete bundle under Vardi1982. Regenerate table, audit, and named-result rows after the split.
- Add Apt1981 to the Hoare sheet with an explicit role. Either print Apt's exact \(p(n)\)-style total rule, or retain the current decreasing-integer-variant rule and state its derivation/equivalence to the cited schema. Keep Cook1978 responsible only for relative completeness of partial correctness.

Disposition: exact status/source-role blocker. These are not requests for more citations; they are corrections to which source proves which displayed record.

### SF9-R2-F6 [blocker] [open] The SLD/SLDNF treatment violates definition-before-use and omits the mandatory Prolog boundary

Location: handbook/parts/p09/logic-in-computer-science.tex:988-1010,1035-1091,1207-1235; sheet handbook/registry/calculi/sld-resolution.tex:2-8; symbol row handbook/registry/symbols.csv:670; obligation N-c-022 at spec/registers/new-content.csv:129 and D-P11-006 at spec/registers/depth-gaps.csv:133.

Claim: The SLD theorem quantifies over a “correct logical answer,” and Comp(P) is defined using “Clark's equality theory.”

Evidence: Computed answers are defined exactly at lines 988-1002, but “correct logical answer” first appears in the theorem at lines 1005-1008 with no eliminable definition. Clark completion prints the predicate biconditionals at lines 1064-1077, then makes Clark's equality theory part of Comp(P) without listing its axioms or routing an exact defined destination. The symbol-registry row repeats the same undefined component. Under the binding AGENTS rule, neither technical name has sufficient local definition and standing.

D-P11-006 additionally requires SLD resolution, negation as failure, and Prolog. The current body and sheet supply the first two, but there is no reader-facing Prolog operational boundary anywhere in the live P9 route. In particular, the fair SLD-tree enumeration used for completeness at lines 999-1009 is not Prolog's usual leftmost, program-order, depth-first operational control and must not be silently identified with it.

Exact correction:

1. Define a correct answer for initial goal \(\leftarrow A_1,\ldots,A_n\): a substitution \(\eta\), restricted to the initial variables, is correct exactly when
\[
P\models\forall\bigl((A_1\land\cdots\land A_n)\eta\bigr),
\]
with the closure and instance convention stated. Then the factorization \(\eta=\theta\rho\) is typed.
2. Give the exact signature-relative Clark equality theory: equality congruence plus the disjointness, injectivity, and acyclicity/occur-check axioms for the active function symbols, or route one exact public definition that lists those axioms. Merely naming the theory or citing a chapter is insufficient under the local technical-name rule.
3. Add a bounded Prolog operational note/card: leftmost literal selection, textual clause order, and depth-first search; explicitly show that this control may diverge before an existing refutation and therefore does not inherit the fair-enumeration completeness conclusion. Attach Lloyd1987 or another verified Prolog-operational source to that exact claim.

Disposition: blocking reconstructibility, AGENTS technical-name, and literal must-register defect.

### SF9-R2-F7 [major] [open] The newly live probabilistic record leaves the scheduler class untyped

Location: handbook/parts/p09/logic-in-computer-science.tex:623-681,710-728,1310-1312; symbol rows handbook/registry/symbols.csv:650-655; formerly excluded N-x-015 at spec/registers/new-content.csv:186, treated as live by the binding board amendment.

Claim: \(\Pr_s^{\min}\) and \(\Pr_s^{\max}\) range over “history-dependent schedulers,” and the theorem uses Bellman min/max equations.

Evidence: The text says only that a scheduler resolves action choices from finite history. It does not type the transition kernel as a partial action-indexed distribution, define enabled actions, or say whether schedulers are deterministic or randomized. Those choices define different mathematical objects. Baier--Katoen's [Principles of Model Checking](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/) treats scheduler classes explicitly; its general scheduler and finite-memory specializations are typed functions on finite paths. The current prose cannot determine the set over which its infimum/supremum is taken.

Exact correction: define
\[
\mathsf{Act}(s)=\{a:P(s,a,\cdot)\text{ is defined}\}\ne\varnothing
\]
and choose one exact scheduler class. For the deterministic history-dependent convention matching the printed Bellman extrema, define
\(\sigma:\operatorname{Paths}_{\mathrm{fin}}(\mathcal M)\to\mathsf{Act}\) with
\(\sigma(\pi)\in\mathsf{Act}(\operatorname{last}\pi)\), define the induced path measure, and quantify \(\inf_\sigma/\sup_\sigma\) over that set. If randomized schedulers are intended, type the codomain as distributions over enabled actions instead. State the finite-MDP fact that the PCTL reachability extrema used by the Bellman equations are attained by deterministic memoryless schedulers. Propagate the chosen type into the definition, table, theorem, and symbol note.

Disposition: source/content blocker for the amended live record; the quantitative material is substantively present, but its central semantic quantifier is not exact.

### SF9-R2-F8 [major] [open] The mandatory temporal-source record does not route the distinct Kamp theorem or the registered comparison table

Location: handbook/parts/p09/logic-in-computer-science.tex:351-381,485-493; live cross-part destinations handbook/parts/p08/temporal-epistemic-supplement.tex:273-300,406-439; obligation N-c-012 at spec/registers/new-content.csv:119 and apparatus A-079 at spec/registers/apparatus.csv:80.

Claim: N-c-012 requires both Kamp and Gabbay--Pnueli--Shelah--Stavi expressive-completeness statements, with their variants separated.

Evidence: P9 correctly states the discrete non-strict theorem over \((\mathbb N,<)\) under cited=GabbayPnueliShelahStavi1980. The live Part VIII route separately defines Kamp's strict \(U,S\) and states thm:p08-kamp: one direction over all chains and the converse over Dedekind-complete chains, with Stavi operators needed over arbitrary gappy orders. P9 neither cites nor cross-references that public result. Similarly, lines 491-493 route the Büchi and CTL figures but omit the live temporal comparison Table tab:p08-temporal-comparison required by A-079.

Exact correction: immediately before thm:p09-ltl-fo, cross-reference def:p08-tense-until-since and thm:p08-kamp, and say explicitly that their strict witness/order theorem is distinct from P9's non-strict discrete \(\mathbb N\) theorem. Add Table tab:p08-temporal-comparison to the existing Figure routes at lines 491-493 rather than creating another comparison identity.

Disposition: registered source/variant/navigation blocker; repair is exact cross-part reuse, not a new theorem.

## Register and apparatus disposition

The following dispositions are against current reader bytes; the CSV control fields themselves remain administratively open and were not edited in this review.

| Record(s) | Current source/content disposition |
|---|---|
| N-c-001 | Open only for the duplicate Trakhtenbrot identity in F2; finite/unrestricted content and the P3 table route are otherwise present. |
| N-c-002 | Checked clean: single P3 zero--one identity, exact vocabulary/distribution hypotheses, extension-axiom/random-graph route. |
| N-c-003 | Checked clean at stated theorem/survey ceiling: Gaifman and bounded-degree Hanf variants and applications are separated. |
| N-c-004 | Checked clean: Fagin and Immerman--Vardi use their existing public identities; finite/order hypotheses remain printed. |
| N-c-005 | Open: false Skolemization and imprecise dual-prefix prose, F3. |
| N-c-006 | Checked clean through the exact P2 two-variable row. |
| N-c-007 | Checked clean through the exact P2 guarded row and P9 modal bridge. The contributor order Andréka, Németi, van Benthem at handbook/bib/handbook.bib:5607-5616 matches the [Springer article record](https://link.springer.com/article/10.1023/A%3A1004275029985). |
| N-c-008 | Open only for the missing Löwenheim historical source role, F3; the modern exact complexity row remains correctly assigned to Lewis1980. |
| N-c-009 | Blocking: tableau initialization/proof mismatch, F1. |
| N-c-010 / A-095 | Open: OWL profile/source-family mapping, F4. |
| N-c-011 | Checked clean: ALC/multimodal K is explicitly limited to no global TBox. |
| N-c-012 / A-079 | Open: Kamp and comparison-table cross-part routes, F8. |
| N-c-013 / D-P10-010 | Checked clean: nondeterministic Büchi reuse, parity/Rabin variants, closure/complementation boundary, LTL translation/model-checking route. |
| N-c-014 | Checked clean: finite-word BET, S1S, and S2S are distinct statements with distinct sources. |
| N-c-015 | Checked clean at pointer ceiling: finite ranked tree automata are not inferred from word-automaton tuples. |
| N-c-016 | Checked clean: total CTL labelling clauses, \(O((|S|+|R|)|A|)\) bound, and reciprocal annex proof. |
| N-c-017 | Open only for duplicate ROBDD identities, F2; symbolic/BMC/CEGAR content is present. |
| N-c-018 | Checked clean: exact P8 modal-mu reuse and P9 alternation specialization. |
| N-c-019 / A-022 / A-096 / D-P11-008 | Substantive rules, semantics, wp/wlp, example, and full annex proof are present; exact total-rule source lineage remains open under F5. |
| N-c-020 | Checked clean: heap semantics, locality, variable side condition, frame sheet, theorem, tools/bi-abduction boundary. |
| N-c-021 | Open only for the bundled PDL status/source control, F5; grammar and sheet are otherwise reconstructible. |
| N-c-022 / A-023 / D-P11-006 | Blocking: undefined correct-answer/CET terms and absent Prolog control boundary, F6. |
| N-c-023 / D-P11-007 | Checked clean: finite-ground stable semantics and exact existence/credulous/skeptical boundaries; ASP solver ecosystems are not claimed. |
| N-c-024 | Open only for CQ evaluation/containment source control, F5; CQ, canonical database, homomorphism, Datalog, and data/combined distinctions are present. |
| N-c-025 | Checked clean at pointer ceiling: fixed-template CSP is distinguished from combined homomorphism. |
| N-c-026 | Checked clean: exact P4 theorem route plus a distinct proved P9 polynomial-size TQBF simulation with reciprocal annex proof. |
| N-c-028 | Checked clean at pointer ceiling: exact Craig-interpolation destination and McMillan source. |
| Amended N-x-015 | Substantively delivered, but open for the scheduler semantic type in F7. |
| A-036, A-044, A-052 | Checked clean as exact cross-part tables; P9 does not create replacement identities. |
| A-051 | The P9 local complexity table contributes exact P9 problem/input rows. Literal all-book harvesting remains a global apparatus task and is not established by this P9 source review. |
| A-097 | Checked clean as a live comparison table, subject to F6's missing definitions/Prolog boundary. |
| A-113 | Checked clean mechanically: 64 live rows and one reader route at handbook/parts/p09/logic-in-computer-science.tex:1382-1385. |
| A-157, A-160, A-165, A-193 | P9 rows handbook/registry/symbols.csv:635-679 appear in generated symbols-tables.tex and symbol-index.tex. This mechanical retrieval does not cure the undefined CET component or scheduler class in F6-F7. |
| A-186 | Checked clean: reader-facing source navigation/further reading at body lines 1363-1380. |
| A-189 | Body-to-sheet and body-to-annex routes are live; the missing Kamp/table route remains F8. |

## Checked-clean evidence

- Source and presentation standing is explicit at handbook/parts/p09/logic-in-computer-science.tex:11-34: the chapter is editorial synthesis, the formerly Part-IX-titled exact source material is rehomed under the named Part II chapters, and no false derivative lineage is asserted.
- The five new calculus sheets are each routed exactly once at handbook/parts/p14/rule-sheets.tex:81,84-87. The P14 preface at lines 4-8 correctly calls them attributed navigation apparatus rather than inherited rule displays.
- Every one of the four proved= statuses in the body has exactly one reciprocal annex item: ALC, CTL, Hoare, and TQBF at handbook/annex/p09/proofs.tex:3,58,96,125. CTL, Hoare, and TQBF proof bodies were checked and no status upgrade or source substitution was found. ALC reciprocity is mechanically correct but substantively blocked by F1.
- The live P8 Büchi definition reused at P9 lines 398-400 is genuinely nondeterministic: handbook/parts/p08/temporal-epistemic-supplement.tex:353-380 types \(\delta:Q\times\Sigma\to\mathcal P(Q)\), defines runs by membership, and uses existential acceptance. P9's product construction therefore reuses the exact convention rather than a deterministic surrogate.
- All 34 P9 theorem-like result labels have one generated named-result row, and all 64 theorem/definition audit rows are reachable. F2 is a semantic duplicate check that those local cardinality checks cannot detect.
- Across the body, annex, and five sheets, 66 distinct citation/status keys resolve to bibliography records; no missing key was found. The open issues are claim-to-source roles, not unresolved keys.
- No reader-visible OPEN, TODO, TBD, stub, owed, placeholder, or internal register-row prose was found in the live P9 body/annex/sheets.

## Four-lot coverage

1. Finite-model theory, descriptive complexity, decidable fragments, prefix classes: fully checked. Open source/content defects are the duplicate Trakhtenbrot identity and F3's prefix/historical-source errors.
2. Description logics and ontology/query boundaries: fully checked, including body, ALC sheet, annex proof, family table, bibliography, symbols, and generated rows. Open defects are F1 and F4.
3. Temporal/automata/model-checking/modal-mu/complexity: fully checked, including live P8 reuse and the amended probabilistic branch. Open defects are ROBDD duplication, untyped schedulers, and missing Kamp/A-079 routes.
4. Hoare/PDL/separation logic, logic programming/databases/CSP, complexity, navigation and apparatus: fully checked. Open defects are the exact status/source controllers in F5 and the reconstructibility/Prolog failures in F6.

Not checked and deliberately external: TeX compilation, PDF rendering, float placement, overfull boxes, hyperlink behavior in a built PDF, bibliography rendering, index collation, provenance closure, visual review, human review, and user acceptance. None of those external gates can repair the current source/content defects, and this rejection does not purport to decide them.

Final source/content disposition: REJECT until SF9-R2-F1 through SF9-R2-F8 receive the exact corrections above.
