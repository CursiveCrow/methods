ACCEPT

**Message verdict:** ACCEPT — the actual integrated LaTeX is publication-admissible at the source strengths it expressly claims.

**Report path:** `spec/research/p09-n-c-014-integrated-source-review-r2.md`

# N-c-014 integrated Round 2 — fresh blind source-fidelity review

## Scope, method, and evidence boundary

I read `handbook/parts/p09/presentations/n-c-014.tex` directly from line 1 through line 1671, its actual EOF. I separately read `handbook/parts/p09/logic-in-computer-science.tex` lines 836--946, including the live `\input{parts/p09/presentations/n-c-014}` at host line 937. The verdict is about those actual reader sources, not about a rendered surrogate.

For source comparison I used only the permitted current source-status summary in `spec/research/p09-source-presentations-lot2-3.md`, the five permitted source notes, the relevant compact register row, and the relevant entries in `handbook/bib/handbook.bib`. The source-status summary was used only to establish current acquisition and open-body boundaries; none of its statements about earlier review outcomes supplied review evidence here. The substantive comparison used:

- `spec/research/p09-buchi-1960-source-note.md`;
- `spec/research/p09-elgot-1961-source-note.md`;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`;
- `spec/research/p09-rabin-1969-source-note.md`; and
- `spec/research/p09-thomas-1996-report-source-note.md`.

I did not open or inspect any prior N-c-014 review or admission report, independent-review record, board record, board ledger, charter, transcript, or chair file. I did not inspect a manuscript PDF, manuscript page image, PNG, render, or other manuscript derivative. I did not run TeX, a build, a test, a checker, a repository script, a hash command, or any automated validation. No historical-source page visit was needed: the actual LaTeX and the permitted detailed source notes settled every source/version question material to this verdict.

## Verdict standard and result

The acceptance question is bounded. It is not whether the current presentation is a transcription of the unavailable 1960 B\"uchi journal body or of Thomas's unavailable final 1997 chapter. It is whether the actual LaTeX is publishable at the strengths it states: B\"uchi's complete 1959 report precursor, Elgot's controlling 1961 article plus the 1962 published errata with the 1959 report kept as a precursor, Trakhtenbrot's distinct 1961 announcement and 1962 expansion, Rabin's complete 1969 article with the separately attributed later complexity correction, and Thomas's complete May 1996 report precursor.

On that standard, there is no blocking or must-fix source-fidelity finding. The presentation accurately types the source objects, does not silently identify versions, gives locators only to bodies that control them, distinguishes source statements from handbook repairs and later corrections, keeps the original presentations separate from the modern synthesis, and discloses the two still-unreconciled registered publication bodies. The host insertion preserves those boundaries.

## Complete actual-LaTeX audit

### File opening and structural standing — lines 1--6

- Line 1 correctly identifies the source-presentation register row.
- Lines 3--4 give the presentation a unique subsection and label.
- Line 6 accurately describes the immediately following B\"uchi, Elgot, and Trakhtenbrot bodies as three original predicate-and-automata presentations. Thomas is introduced later as a modern report route, and Rabin receives a separate infinite-tree subsection; the heading therefore does not merge five unlike sources into one alleged original theorem.

### B\"uchi presentation — lines 8--229

#### Source identity, object standing, and definitions — lines 8--71

- Lines 8--16 state the exact authority boundary: the registered item is the 1960 journal article, while every present report-page and theorem locator is controlled by the complete September 1959 UMR1083 precursor. The text expressly refuses to infer identical journal wording, numbering, examples, or proof detail. `Buchi1959WeakReport` and `Buchi1960` therefore have different evidentiary standings rather than serving as interchangeable citations.
- Lines 18--29 give the report's interpreted (W.2.A.) correctly: individuals range over (\mathbb N), zero and successor are primitive, and predicate quantifiers range over eventually-false Boolean predicates, equivalently finite subsets. The manuscript explicitly distinguishes an interpreted semantic system from a deductive calculus and finite-set weakness from quantifier-alternation weakness or later full-set infinite-word logic.
- Lines 31--46 state the report's literal finite propositional automaton data (E^m,H^m[Y^m,X^n]) and the induced, uniquely typed transit recursion. The finite formula tuple, a time-indexed input predicate, and a time-indexed transit predicate are not conflated with a modern nondeterministic tuple.
- Lines 47--58 state the exact special-output identity (U[Y^m]\equiv U[H(Y^m,\bot^n)]) and its consequence after an eventually-false input. The identity is pointwise in the state variables and is not replaced by the stronger and false condition (U(\bot^m)=\top).
- Lines 59--71 define the behavior as a set of special assignments on which the output is eventually permanently true. The manuscript then states the distinct standings of finite propositional data, predicates on time, and the behavior set. This satisfies the local necessity, definition, standing, nonredundancy, and use requirements for the source terminology.

#### Theorem strength, proof defect, and handbook repair — lines 73--142

- Lines 73--93 give Lemma 1's local successor normal form and Theorem 1's effective synthesis direction. The proof summary assigns complement, expanded disjunctive presentation, and existential input-track removal their correct roles instead of invoking a generic later automata theorem.
- Lines 95--108 state Theorem 2 at its advertised existential local-normal-form strength.
- Lines 109--120 identify the actual failure in printed formula (2): its finite transit witness eventually becomes all false, thereby imposing (U(\bot^m)=\top), which printed Definition 2 does not entail. The one-state-bit counterexample is typed and valid.
- Lines 121--141 give an exact handbook-owned correction. The finite cutoff predicate is required to be nonempty and downward closed; the run witness is constrained only through its last true cutoff point; the input is false from that point onward; and the output is tested at the boundary. The following prose proves both directions and explains how special-output invariance supplies the omitted tail. The text does not attribute the corrected clauses to B\"uchi's printed formula.
- Line 142 supplies report-page and theorem locators that cover the source statement and printed proof context.

#### Finite words, decision procedure, and arithmetic correction — lines 144--229

- Lines 144--157 reproduce the source's word-to-special-predicate map, including the (\top^n) terminal marker and the empty-word convention. The marker is not silently replaced by an abstract endpoint.
- Lines 158--169 distinguish arbitrary-output string behavior from eventual special-output behavior and state Theorems 6--8 at the four-condition strength supported by the report. The text explicitly says that the analysis half relies on the proved handbook correction rather than on the invalid printed formula (2).
- Lines 171--190 preserve Theorem 3's actual boundary formula while disclosing the report's conflicting length prose. The closed-sentence procedure includes the necessary (B(\bot,\bot)) tail guard, the source's inclusive (x\leq k) search, an ending all-false state, and the loop-deletion proof of finite search.
- Lines 192--229 distinguish the sound ultimate-periodicity result and the sound first-order-to-(W.2.A.) direction from the false converse arithmetic claim. The displayed bit-occurrence counterexamples are correct. The later relation (\in_2) and equivalent (V_2) presentation are defined, typed as later correction evidence, and cited to the later source; they are not projected backward into the report. The text accurately preserves the surviving decidability consequence while withdrawing the false exact unary-powers characterization.

No B\"uchi locator in these lines is presented as a journal-page locator. The explicit closing boundary at lines 924--926 confirms that this section stands only at 1959 report-precursor strength.

### Elgot presentation — lines 231--522

#### Authority order and finite-set correspondence — lines 231--343

- Lines 231--236 make the complete 1961 article controlling, the 1959 UMR1342 report a primary precursor, and the 1962 errata controlling for corrected formulae. No version is silently selected.
- Lines 238--256 give the source (I)-automaton with the correct types: (I) is the finite nonempty input alphabet, (S) is the finite nonempty internal-state set, (f:I\times S\to S), (d\in S), and (D\subseteq S). The unique run and empty-word convention are exact.
- Lines 258--286 state the grammar and finite-set interpretation of (L_1^1), the characteristic-column map, the canonical truncation at the last nonzero column, the empty assignment's (\Lambda) encoding, the admissible language (U_r^*U_r^0\cup\{\Lambda\}), and the standing of (T_r(A)).
- Lines 288--313 state both effective directions of Theorem 5.3 and give the actual constructor-level proof of the forward direction: quantifier ordering, local successor matrices, regular Boolean operations, coordinate deletion, and the essential right truncation of newly terminal zero columns.
- Lines 315--329 give the reverse construction rather than merely asserting it. Extra Boolean coordinates encode automaton states; the start set, terminal set, and local relation are typed; existential projection removes the state tracks; and the empty word is handled separately.
- Lines 331--343 give the correct decision and arithmetic consequences without treating them as alternative automaton definitions or as a blanket arithmetic decidability result.

#### Design theory, erratum, and negative boundary — lines 345--522

- Lines 345--372 define the distinct (A/B)-automaton with output map (g:S\to B), its synchronous finite behavior, and Theorem 7.1's four exact conditions: regularity, source-sense openness/prefix closure, output functionality, and input totality. The proof summary explains the product construction and the role of functionality and totality.
- Lines 374--393 define (A)-extendability and strong (A)-extendability before Lemma 6.1 and Theorem 8.1 use them. The deletion criterion, maximal stable language, lexicographic selection, vacuous uniqueness case, and formula encoding of a fixed transducer are stated without inventing a new automaton species. The unitalicized proof prose at line 380 does not introduce a reusable technical object; the operative deletion condition is stated in the same sentence.
- Lines 395--401 keep Theorem 7.3 in its proper standing as a causal synchronous behavior theorem, not a B\"uchi acceptance theorem.
- Lines 403--442 define every variable and restriction in the arbitrary-set specification, define the characteristic-column stream language (T_d^\infty(C)), and state why the exact term restrictions, rather than quantifier-freeness alone, yield a bounded window.
- Lines 443--465 disclose the article's false single-relation sentence and state the published erratum's finite union with explicitly typed (n)-ary relations, fields, prefix sets, and infinite relation sequences.
- Lines 466--482 give the erratum-owned disjoint-tag construction in general arity and prove that overlap forces a constant tag.
- Lines 484--495 separately supply the (n=1) promotion as a handbook-owned completion. It is neither omitted nor falsely credited to the erratum. Only after both arity cases are proved does the text invoke the corrected synthesis reduction.
- Lines 497--510 state Chapter IV's exact negative boundary: finite-predicate satisfiability is recursively enumerable but undecidable with maximal recursively enumerable degree, and fixed-automaton satisfaction is decidable while existence of some satisfying automaton is not. The positive design results are therefore not overgeneralized.
- Lines 512--522 record the precise precursor/article/errata comparison and assign correction ownership to the published errata even where the report independently has a corrected symbol.

The closing source boundary at lines 927--928 correctly says that Elgot's article, precursor, and errata are source-controlled independently.

### Trakhtenbrot presentation — lines 524--930

#### Two source bodies, formal system, and operator taxonomy — lines 524--640

- Lines 524--534 distinguish the registered four-page 1961 announcement from the complete 1962 expansion, preserve their different official English title renderings, and assign each source its own pagination and theorem standing.
- Lines 536--556 state that (\mathcal I) is an editorial rendering of the source's Cyrillic system name and define its standing as an interpreted formal language. The positive-natural-number domain, unrestricted monadic predicates, successor grammar, and eliminable conveniences are explicit. The text also distinguishes (\mathcal I) from B\"uchi's weak finite-set system.
- Lines 558--585 define semantic fictitiousness, both controlled classes, upper and lower (t)-formulae, their syntactic restrictions, their separate semantic dependence consequences, and the normal-form proof moves. No semantic consequence is substituted for the syntactic definition.
- Lines 587--615 define a typed stream operator, anticipation (p), finite memory, the whole-future suffix arguments, weight, and the reason finite memory does not imply bounded lookahead or recursiveness.
- Lines 616--631 define finite operator and its finite-window form, distinguish the announcement's Cyrillic class letter from the expansion's Latin (A), explain the normalization, and separate zero anticipation, finite memory, finite operator, and the automaton-realizable zero-anticipation class.
- Lines 633--640 identify the source's “periodic” streams as ultimately periodic and preserve the source's undecidability boundary for overly broad primitive-recursive synthesis schemes.

#### Portions, homogeneity, source defect, and exact converse — lines 642--790

- Lines 642--666 define one-coordinate and coordinatewise tuple portions, state the announcement/expansion empty-portion convention difference, define homogeneity degree and a finite basis, and state the standing of the resulting transition data. Concatenation and shifting are explicitly coordinatewise.
- Lines 668--694 define Cantor-product closedness, operator graphs, common output prefixes, tail removal, and the residual operator (T_u). The exact graph-portion identity supplies the new notation's definition, standing, nonredundancy from broad memory states, and later use. The paragraph expressly identifies these as handbook-owned exactifications.
- Lines 696--732 state the source's false numerical homogeneity bound and provide a complete handbook-owned counterexample: the operator, two-state whole-future presentation, exact state invariant, proof that one state is impossible, and four distinct all-prefix portions. The text preserves the unaffected closedness claim and gives the correct residual-map qualification.
- Lines 733--780 preserve the singleton/ultimate-periodicity example, the countability obstruction to definability, and both directions of the definability theorem. The recurrent formula assigns exact standings to the free input predicate, bound basis-state predicates, bound choice predicate, and quantifier-free local matrix. The nonempty covering construction is proved to generate the closure, and the empty-set case is separately repaired by contradiction rather than being forced through an impossible total-image construction. Both repairs are labeled handbook-owned.
- Lines 782--790 keep the internal-transition effectiveness distinct from the conditional output-selection step and preserve the source's stated Putnam qualification.

#### Finite realization, general solutions, and finite-word boundary — lines 791--930

- Lines 791--813 distinguish a formula that defines exactly an operator graph from an operator whose graph merely solves a relation. The continuous-operator theorem, finite-memory-only theorem, closed-relation existence form, zero-anticipation form, and open-relation no-bound qualification retain their unequal hypotheses and conclusions.
- Lines 815--849 define a general (A)-solution by both necessary clauses, give the corresponding zero-anticipation standing, state the closed relation hypothesis, preserve the conditional deletion construction, and keep the fixed-(p) extension separate for each bound rather than claiming one unbounded parametrization.
- Lines 851--864 define explicit synthesis and accurately state the finite residual-formula construction and worked-example locator.
- Lines 866--877 define the finite-word maps (T_t:A^t\to B^t) from zero anticipation and prove extension independence and prefix compatibility.
- Lines 879--902 define automaton-enumerability and automaton-decidability with their exact positive-length types. The text preserves the sound direction and identifies the empty-language counterexample to the printed converse. Nonemptiness is labeled a handbook-owned repair and is shown to supply the source construction's missing lengthwise seed.
- Lines 904--913 define the weak eventually-zero system (\mathcal I'), define a special beginning, and state the existence/effectivity distinction with the source's B\"uchi attribution.
- Lines 915--930 explicitly refuse to quote the modern finite-word equivalence as the four-page announcement's literal theorem, preserve the wider operator/topology/synthesis source package, distinguish historical comparisons from priority adjudication, and disclose that no complete line-by-line translation is claimed.

### Thomas finite-word report route — lines 932--969

- Lines 932--945 identify the May 1996 report as the controlling modern source for this passage, rename only the alphabet and transition relation, define the finite-word automaton and its (n+1)-state run, and state Theorem 3.1's effective two-way equivalence.
- Lines 947--962 correctly separate the two proof directions. The automaton-to-formula direction uses disjoint state tracks, treats the final transition separately, and retains the empty-word guard. The formula-to-automaton direction names the actual singleton-set atomic cases and the closure/projection operations. The input-free (WS1S) and finite-carry Presburger consequences retain their report locators.
- Lines 964--969 state the ownership and non-substitution boundary: this modern construction is not substituted for B\"uchi's special-predicate encoding, Elgot's design calculus, Trakhtenbrot's operator theory, or their separately controlled source bodies.

### Rabin presentation — lines 971--1524

#### Structures and ordinary acceptance — lines 971--1086

- Lines 971--980 name Rabin 1969 as controlling and preserve the source root symbol (\Lambda).
- Lines 981--1011 introduce editorial subscripts only to disambiguate the source's two order symbols, define both orders' standings, define every successor and the predecessor, and give Definition 1.1 for every (0<n\leq\omega).
- Lines 1012--1026 state (SnS), finite-(n) definability of the orders, Theorems 1.1 and 1.12, and the exact complexity correction. Rabin's historical elementary-recursive claim is quoted as history but not retained; the later Meyer lower bound is separately attributed and does not weaken decidability or effectiveness.
- Lines 1028--1036 define rooted subtrees, paths, valued subtrees, and the set (V_\Sigma), including the predecessor condition.
- Lines 1037--1077 distinguish a transition table from an ordinary automaton, state possible transition partiality, define (\operatorname{In}), define one global run, and give ordinary acceptance with the essential (\exists r\,\forall\pi) prefix and (F\subseteq\mathcal P(S)). The text expressly separates the later pair sequence from ordinary acceptance and preserves arbitrary-root language standing.
- Lines 1079--1086 state the exact effective union, intersection, coordinate, complement, and emptiness dependencies and their proof locus.

#### Formula tracks and both directions — lines 1088--1177

- Lines 1088--1109 define the characteristic-track bijection and Theorem 1.7's exact representation condition.
- Lines 1111--1128 state the source normal form, define every component of a principal formula, identify the deferred Section 3.10/Corollary 3.13 construction, and assign Boolean closure and set-track projection their proper roles.
- Lines 1130--1144 define the required finite witness object before use: (E\) is finite, root-containing, and predecessor-closed; (\operatorname{Ft}(E)) is its terminal-node frontier; “frontiered” is exactly the two-children property; and a finite valuation labels only nonfrontier nodes. The text states the term's standing, its nonredundancy from predecessor closure, and the later lift that requires it.
- Lines 1146--1156 give a correctly typed handbook-worked principal-formula instance and explicitly deny that it is a Rabin-printed transition table.
- Lines 1158--1170 give Theorem 1.10's converse state-track encoding and exact set-quantifier prefix.
- Lines 1172--1177 preserve Rabin's actual sentence-to-nonemptiness reduction and expressly exclude a later regular-tree-basis step.

#### Path product, dual acceptance, and complementation — lines 1179--1397

- Lines 1179--1218 state Theorem 3.1 with a typed path sequence, deterministic Muller word automaton, product state, transition, and designated family. The text explains why determinism supplies coherent shared histories before branch separation and marks McNaughton's equivalence as an external dependency rather than as a Rabin proof.
- Lines 1220--1267 define the pair sequence (\Omega), the type and type-empty predicates, and dual acceptance with the exact (\forall r\,\exists\pi) standing and permitted vacuity. The manuscript explicitly says the pair sequence belongs to complementation, not to the ordinary field (F).
- Lines 1269--1292 identify the omitted zero-length case and define the handbook-owned one-pair normalization (\Omega^\dagger=((S,S))). The proof that its path type is impossible and that its dual language equals the empty-sequence dual language is complete. The notation's necessity, definition, standing, nonredundancy, and later use are all local.
- Lines 1294--1336 give the actual marked-tree, simultaneous-run, well-founded-obligation, dual-reduction, two-half-step, and induction-on-pair-length architecture. The source's well-founded mapping is defined by the absence of an infinite dependency descent; its standing and use in Lemmas 3.3, 3.4, and 3.11 are explicit.
- Lines 1338--1388 restate frontiered finite trees where the detailed finite-tree machinery begins, define the finite-tree automaton and external frontier value (f\notin S), give the exact run and acceptance types, distinguish it from both infinite Rabin runs and host bottom-up ranked-tree runs, and assign Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15 their correct and noninterchangeable roles.
- Lines 1390--1397 locate transfinite induction precisely and refuse to use it as a slogan replacing the finite-state proof architecture.

#### Actual emptiness proof, applications, and proof boundary — lines 1399--1524

- Lines 1399--1427 give Rabin's one-letter input erasure, complement, and dual-language reduction. The equivalence is typed and does not invoke a regular-tree basis theorem.
- Lines 1429--1445 define the current finite recursion data and Definition 3.7's restricted transition table, including the exact fact that restriction applies strictly below the root.
- Lines 1447--1465 give the finite collapse of the transfinite stage construction and the exhaustive (H\subseteq U_k) reduction. The missing (H=\varnothing) branch is labeled handbook-owned and is given its exact shorter-question role.
- Lines 1467--1484 give the (k=1) base with (m\geq0), allowing (U_0=\varnothing). The no-run finite obstruction and K\"onig argument cover the permitted vacuous branch. The text identifies the source's printed nonempty restriction and refuses to retain it as an exhaustive equivalence.
- Lines 1486--1494 state exactly which three handbook completions are needed, retain only source effectiveness rather than the false complexity qualification, and preserve the external finite-tree/weak-theory dependency without turning full (S2S) into weak logic.
- Lines 1496--1515 map Rabin's Chapter II applications at their actual theorem strengths.
- Lines 1517--1524 disclose the reconstruction boundary: the key architecture is reconstructed, while every transition table and induction in the fourteen-page development remains in the cited complete source.

### Thomas infinite-tree report route — lines 1526--1671

- Lines 1526--1551 identify the later, post-1969, game-theoretic route and define the report's Muller tree automaton, full-tree run, and (\exists r\,\forall\pi) acceptance. The examples' B\"uchi/Muller separation is attributed to the report.
- Lines 1553--1573 define the strict Rabin chain, its path condition, and the “order-vector with hit” as a permutation plus the prior position of the new state. Its standing as finite state memory, nonredundancy from the input tree and run, and later Muller-recovery use are explicit.
- Lines 1575--1604 identify the concrete partial-transition/game-premise gap and supply a typed handbook-owned completion. (\mathcal A^\bot) is defined as a chain tree automaton, not a game or run; its necessity, difference from (\mathcal A), language-preservation proof, and subsequent use are all stated. A path trapped in the fresh state satisfies no chain pair, so no successful run can use an added transition.
- Lines 1606--1608 explicitly announce the harmless notational reuse of (\mathcal A) and (\Delta) only after completion.
- Lines 1609--1637 define the Automaton/Pathfinder game, memoryless standing, finite local instruction type, strategy-tree encoding, complement construction, independence from the particular input tree, determinacy proof architecture, and finite-game effectivity. The completed nonempty-outdegree premise is carried throughout.
- Lines 1639--1649 define a regular input tree as a finite direction-word generator with output, state that this is an input-tree property rather than an acceptance mode, and give the effective emptiness/regular-member route after the same completion.
- Lines 1651--1664 state both MSO/automaton directions and the resulting (S2S) decision at report strength, with the regular-model consequence kept as a report consequence.
- Lines 1666--1671 explicitly separate Thomas's later route from Rabin's Section 3.12 proof and disclose that every Thomas locator belongs to the May 1996 report precursor, not the unreconciled final chapter.

## Host integration audit — `logic-in-computer-science.tex` lines 836--946

- Lines 836--851 present the finite-word equivalence as a modern handbook formulation. The theorem's source field includes the B\"uchi report and registered article identity, Elgot's article, both Trakhtenbrot bodies, and the Thomas report. Lines 843--850 immediately disclaim verbatim occurrence in each source and state the different encodings and result packages. The title is therefore a modern synthesis label, not a false quotation or priority adjudication.
- Lines 853--872 are adjacent S1S material outside this N-c-014 source package. They were read to test integration only. Their explicit handbook-owned modern-automata boundary prevents the N-c-014 B\"uchi weak finite-word presentation from being silently replaced by B\"uchi's distinct full-set infinite-word system.
- Lines 874--877 give the appropriately narrow host theorem for Rabin: decidability of the monadic second-order theory of the full binary successor tree. The detailed source presentation supplies the proof and source boundaries without changing this host statement.
- Lines 879--929 are adjacent finite-ranked-tree definitions and theorem material outside this N-c-014 source package. For integration, they are typed as finite bottom-up ranked-tree objects and explicitly distinguished from Rabin's infinite-tree construction. The N-c-014 presentation repeats that nonconflation at its own lines 1373--1377.
- Lines 931--933 contain only prior figure pointers and introduce no N-c-014 source claim.
- Lines 935--938 show the actual input order. The N-c-014 file is inserted exactly once at line 937, after N-c-012 and N-c-013 and before N-c-015.
- Lines 940--946 cleanly begin the next model-checking section; no N-c-014 definition or environment is left open across the boundary.

## Citation, locator, and bibliography audit

The actual citations track their controlling bodies correctly:

- B\"uchi report claims use `Buchi1959WeakReport` with report pages and theorem numbers. `Buchi1960` is used for registered identity and historical attribution, never as a journal-page locator for unread body text. `BruyereEtAl1994` is used only for the later arithmetic-correction history.
- Elgot journal claims use `Elgot1961` at printed article pages 21--51; report-comparison claims use `Elgot1959Report`; corrections use `Elgot1962Errata` at pp. 558--559.
- The announcement and expansion claims use `Trakhtenbrot1961` at pp. 326--329 and `Trakhtenbrot1962Expanded` at pp. 103--131 without interchanging titles, numbering, or pagination.
- Rabin claims use `Rabin1969` at the correct chapter/page loci. The later complexity correction uses `Meyer1975Complexity` at pp. 478--479. McNaughton's theorem is marked as an external dependency and cited separately rather than presented as a result proved by Rabin.
- Every Thomas technical locator uses `Thomas1996Report`, including Section 3.1 and report pp. 43--59. The manuscript never assigns those report locators to `Thomas1997`.

The relevant bibliography entries preserve the identities and source boundaries needed by the LaTeX: B\"uchi UMR1083 and the 1960 article are separate; Elgot's article page range is 21--51 and the report and errata are separate entries; the two Trakhtenbrot titles and publications are separate; Rabin and Meyer are separate; and Thomas's 1996 report and 1997 chapter are separate entries.

## Source ownership, cross-source imports, and technical-name rule

Every material repair is owned where it occurs:

- B\"uchi's printed Theorem 2 witness is refuted and replaced by a proved handbook formula; the length conflict is disclosed; the false unary-powers equivalence is separated from later correction evidence.
- Elgot's finite-union repair is owned by the 1962 errata, while the unary-window promotion is explicitly handbook-owned.
- Trakhtenbrot's false weight/portion bound, residual-operator exactification, empty covering case, and nonempty finite-word converse repair are explicitly handbook-owned.
- Rabin's zero-pair normalization and the missing empty (H) and (U_0) branches are explicitly handbook-owned.
- Thomas's rejecting-state completion is explicitly handbook-owned and proved language-preserving.

No modern route is substituted for an earlier source. Lines 964--969 isolate Thomas's finite-word proof from B\"uchi, Elgot, and Trakhtenbrot. Lines 1172--1177 and 1399--1494 preserve Rabin's actual nonemptiness proof. Lines 1526--1528 and 1666--1671 identify Thomas's tree proof as later work rather than projecting it backward onto Rabin. Later Meyer and Bruy\`ere corrections are separately attributed. McNaughton's word result and the finite-tree weak-theory base are expressly external dependencies.

The AGENTS technical-name condition is met. Source terms are either defined exactly where introduced or used only after a local definition. Editorial names and symbols have eliminable definitions and declared standings. In particular, (T_d^\infty(C)), (T_u), (\Omega^\dagger), (M^\bullet), (N_{R'}), (\mathcal A^\bot), the order-vector with hit, the game, memoryless strategy, and regular generated tree each have an exact type or eliminable definition, an explanation of why an existing source object does not state the needed distinction, and a later proof use. `frontiered` is defined as a property of (E), distinguished from predecessor closure, and used by the finite-tree automaton, lift, complementation, and emptiness arguments. The presentation does not assign a speculative chain, stage, next, before, or constitutional object merely to fill an outline.

## Open-body and completion boundaries

The two unresolved publication reconciliations do not defeat the bounded manuscript verdict:

- Lines 8--16 and 924--926 say that the complete 1959 B\"uchi report controls the current reconstruction and that literal 1960 journal reconciliation remains open.
- Lines 1666--1671 say that the complete May 1996 Thomas report controls every current locator and that the final 1997 chapter is not in the present source basis.

The permitted compact register records `OBL::new-content::N-c-014` as OPEN. That status is consistent with the consolidated source-status bullets: the B\"uchi journal body/reconciliation and Thomas final-chapter reconciliation remain independently owed, and the broader Part IX and publication gates are not closed by this manuscript-level verdict. ACCEPT therefore admits only the actual integrated LaTeX at its expressly bounded source strength; it does not close the source register, certify a render or build, or establish Part IX, book, human, or user acceptance.

REGISTER STATUS: OPEN
