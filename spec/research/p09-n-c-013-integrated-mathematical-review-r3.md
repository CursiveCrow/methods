ACCEPT

REGISTER STATUS: OPEN

# Fresh blind mathematical/proof audit of N-c-013, round 3

## Judgment

The current actual LaTeX is mathematically publication-admissible at the source-bounded strength it explicitly claims. I found no false definition, mistimed transition, invalid bound, unsound theorem, missing premise in an asserted proof, convention collision, or host-integration error requiring correction. In particular, the text does not turn any unread registered body into evidence for a body-dependent theorem: its detailed Safra construction is assigned to the 1995 author-hosted expansion, its detailed Thomas construction is assigned to the May 1996 report precursor, and the McNaughton presentation remains expressly nontechnical.

The register nevertheless remains open because several literal registered-body obligations are still unavailable or unreconciled. Those provenance obligations are listed separately at the end; under the stipulated verdict semantics, they do not defeat mathematical admission of the bounded claims actually printed.

## Audit basis and exclusions

I read the current files directly:

- `handbook/parts/p09/presentations/n-c-013.tex`, lines 1--1409;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 723--945;
- the five N-c-013 source notes for B\"uchi 1962, McNaughton 1966, Vardi--Wolper 1986, Safra 1988/the 1995 expansion, and Thomas 1996/the 1997 boundary;
- compact-ledger row N-c-013;
- `handbook/parts/p09/presentations/n-c-018.tex`, lines 615--647, solely for the explicit least-recurring-priority parity seat; and
- the relevant bibliography entries.

One concrete ambiguity required recourse to original historical source pages: Sistla--Clarke 1985, journal pp. 734--735. Those pages define “truth in an R-structure” by asking whether **there is a path** from the supplied state satisfying the formula and state the PSPACE-completeness classification for the relevant temporal logics. That directly settles the lower-bound attribution used at N-c-013 lines 271--279 and host lines 828--833.

I did not open a prior review, admission record, board file, transcript, charter, or independent-review record. I did not inspect any manuscript PDF, manuscript page image, PNG render, or handbook render. I did not run a build, test, checker, repository script, hash, TeX command, or automated validation. No manuscript or source-record file was edited.

## Exhaustive exact-line findings

### 1. Vardi--Wolper syntax, word timing, and permitted-start conversion: N-c-013 lines 17--100

1. **Lines 17--42: ACCEPT.** The computation type, point-zero convention, next clause, and non-strict until clause agree. The witness may be the current point, and the interval on which the left operand is required is exactly \(i\leq k<j\). No strict/non-strict semantics is conflated.

2. **Lines 44--62: ACCEPT.** The source tuple, set-valued transition, permitted initial set, run indexing, B\"uchi recurrence clause, semideterministic condition, and deterministic strengthening are mutually consistent. Semideterminism permits a partial single-valued transition and multiple starts; determinism adds exactly the singleton-start requirement used by the source.

3. **Lines 64--85: ACCEPT.** The fresh-state conversion is language preserving, including the empty-start case. For an old run
   \[
   q_0,q_1,q_2,\ldots,
   \qquad q_0\in Q_0,
   \]
   the new run is
   \[
   q_*,q_1,q_2,\ldots.
   \]
   Conversely, a first transition from \(q_*\) to \(q_1\) supplies some witness \(q_0\in Q_0\) with \(q_1\in\Delta(q_0,a_0)\). The two runs differ only in their position-zero state, so their infinitely recurring old states coincide. Taking \(q_*\notin F_*\), forbidding transitions back to \(q_*\), and retaining all old transitions therefore preserve B\"uchi acceptance. If \(Q_0=\varnothing\), the new start has no first successor and accepts no word, exactly as required. The state cost is exactly one.

4. **Lines 87--100: ACCEPT.** The effective \(2^{O(|\varphi|)}\) LTL-to-B\"uchi statement, its attribution to Wolper--Vardi--Sistla 1983, Appendix-B construction status, and the separately cited B\"uchi-emptiness bounds remain distinct. No proof or lower bound is attributed to the wrong paper.

### 2. Appendix B local component, eventualities, product, projection, and batching: N-c-013 lines 102--222

5. **Lines 102--130: ACCEPT.** The closure has at most twice the formula length; \(N_L\) imposes exactly-one-of-\(\psi,\neg\psi\) and conjunction consistency; and \(N_\varphi\) is exactly the permitted local initial set. The names introduced here are eliminable set abbreviations with declared standing. Although \(B_\varphi=2^{cl(\varphi)}\) is the raw candidate-letter powerset, the later condition \(a=u\) with \(u\in N_L\) ensures that only locally complete, Boolean-consistent letters occur on runs. Thus no inconsistent raw alphabet symbol creates an accepting computation.

6. **Lines 132--151: ACCEPT.** The local transition consumes the current closure type and moves to the next one. Its timing is correct:
   \[
   X\psi\in u_i\iff \psi\in u_{i+1},
   \]
   and
   \[
   \xi U\psi\in u_i
   \iff
   \psi\in u_i\lor(\xi\in u_i\land \xi U\psi\in u_{i+1}).
   \]
   These are precisely the one-step fixed-point equations for non-strict until. The prose correctly notes that the equations alone allow a perpetually pending until and therefore need the separate eventuality component.

7. **Lines 153--178: ACCEPT.** The batching transition has the right direction and timing. When the current obligation set is empty, every currently true until formula whose right operand is currently false is forced into the next set. While a batch is nonempty, a member remains forced exactly until its right operand becomes true; newly encountered eventualities need not be added during that batch. The relation permits surplus obligations, but acceptance is existential and an accepting run may always choose the least required successor set. This nondeterminism is harmless.

   The recurrence proof is sound. If an unsatisfied \(\xi U\psi\) is true at a collection point, local consistency propagates it and \(\xi\) forward until \(\psi\); the eventuality rule simultaneously prevents its removal from the batch while \(\psi\) is false. Since the empty set must recur, \(\psi\) must eventually occur. Conversely, for a semantically correct closure-type word, choose only the currently required obligations. Each finite batch has a finite latest discharge point, so the empty set recurs. An until formula first encountered during a nonempty batch cannot disappear unsatisfied: the local until equation carries it to the next empty collection point unless its right operand has already become true. This verifies both batching directions.

8. **Lines 180--205: ACCEPT.** The synchronous product uses the same current closure letter in both factors, its permitted-start and B\"uchi sets have the displayed types, and
   \[
   |N_M|\leq 2^{|cl(\varphi)|}2^{|e(\varphi)|}\leq 2^{3|\varphi|}
   \]
   follows from \(|cl(\varphi)|\leq2|\varphi|\) and \(|e(\varphi)|\leq|\varphi|\). The single-start conversion adds one state without disturbing the asymptotic theorem.

9. **Lines 206--222: ACCEPT.** Projection is correctly defined by existentially unioning all closure letters with the required atomic valuation. Because the local factor requires the current raw letter to equal its current local state, the projected automaton guesses exactly a locally consistent type extending the observed valuation. Projection changes transitions and alphabet but not product states, starts, or acceptance. Together with the local truth induction and the batch argument above, this gives both language inclusions at the strength claimed. The text accurately labels the absence of a source-printed line-by-line induction and worked formula as a proof-boundary fact, not a mathematical omission in the handbook’s stated theorem.

### 3. Finite-program product timing, correctness, example, and complexity: N-c-013 lines 224--301

10. **Lines 224--246: ACCEPT.** The finite program has a total transition relation, so every finite prefix extends to an infinite path. Its automaton consumes the label of the current program state while selecting the next program state. The noted source tuple-order inconsistency is syntactic only; the typed data are unambiguous, and designating all program states makes every legal infinite program run accepting.

11. **Lines 248--279: ACCEPT.** The equivalence
    \[
    L(A_P)\subseteq L(A_\varphi)
    \iff
    L(A_P)\cap L(A_{\neg\varphi})=\varnothing
    \]
    is exact because the translation is applied directly to the syntactic negation. Both directions of the counterexample correspondence are stated. The ordinary two-B\"uchi intersection needs an acceptance scheduler, but the program factor accepts every state, so the specialized product needs only \(|W||S'|\) states. The source’s time and space upper bounds, and the separate Sistla--Clarke lower-bound provenance, are not conflated.

12. **Lines 281--301: ACCEPT.** In the worked calculation, the first program label omits \(p\), so the negation automaton remains in \(q\); choosing \(b\) yields the accepting lasso \((s_0,q)(b,q)^\omega\), whereas choosing \(g\) reads a \(p\)-letter and reaches the rejecting sink \(d\). Its projection is exactly the program path \(s_0b^\omega\). The example respects the same consume-current-label timing as the general construction.

### 4. Temporal extensions and probabilistic semantics: N-c-013 lines 303--512

13. **Lines 303--328: ACCEPT.** Past-time semantics is not silently substituted for future-time semantics. The three extended temporal-language acceptance modes distinguish finite-prefix success, existence of an infinite run, and recurrent acceptance. Their formula-language standing and the source-bounded \(O(\exp(|\varphi|^2))\) statement are explicit.

14. **Lines 330--389: ACCEPT.** The Markov-chain rows are stochastic, the path space retains exactly positive-support paths, and the legal prefix cylinders generate its Borel sigma-algebra. The cylinder assignment
    \[
    \prod_{i=0}^{n-1}P(w_i,w_{i+1})
    \]
    is consistent and determines the standard path measure. Restricting the carrier to positive-support paths removes only measure-zero impossible cylinders and does not alter qualitative probability-one semantics. The LTL event is measurable (equivalently, it is the inverse image of an omega-regular, hence Borel, word language under the finite labelling map). The text correctly distinguishes almost-sure satisfaction from universal-path satisfaction.

15. **Lines 380--389: ACCEPT.** The support-size parameter counts exactly positive matrix entries. For finite qualitative probability-one checking, only the support graph matters; positive magnitudes do not change which finite bottom components and fairness events have probability one. The parameter is therefore mathematically appropriate and does not omit a required bit-complexity claim, since no quantitative probability is being computed.

16. **Lines 391--400: ACCEPT.** The Streett clause is the universal implication “\(L\) recurrent implies \(U\) recurrent.” The pair \((S,F)\) indeed gives B\"uchi acceptance because every infinite run over finite \(S\) has some recurrent state. The manuscript identifies the source’s contradictory direction label rather than treating it as a theorem.

17. **Lines 402--505: ACCEPT.** The four restricted fragments, limit and \(k\)-limit equivalence, probabilistic fairness, time/space bounds, and deferred-proof boundaries are correctly scoped. The fairness condition is a property of a path and is expressible by Streett obligations. The factor-window length \(k\) is sufficient when there are \(k-1\) next occurrences. The pure-past semideterminism result uses the previously defined multiple-start/single-valued distinction. The concurrent Markov tuple distinguishes stochastic from nondeterministic rows and does not claim the deferred full algorithm.

18. **Lines 507--512: ACCEPT.** The closing proof-boundary paragraph accurately separates constructed, cited, sketched, and deferred material. No incomplete source sketch is upgraded to a handbook proof.

### 5. B\"uchi 1962: formula classes, finite data, closure, effectivity, and decision proof: N-c-013 lines 514--920

19. **Lines 514--559: ACCEPT.** The source identity, full-domain standing of \(SC\), variable domains, successor notation, and set-assignment/infinite-word encoding are exact. “Sequential calculus” is kept descriptive and is not introduced as an unnecessary second formal object.

20. **Lines 560--640: ACCEPT.** The \(\Sigma_n\), \(\Pi_n\), infinitely-often, and \(\Sigma_1^\omega\) schemata have the correct quantifier polarity and recurrence clause. The handbook-owned automata comparison is extensionally exact: \(\mathbf r(n)\) supplies state \(q_n\), the input letter \(\mathbf i(n)\) is consumed by the constraint from \(q_n\) to \(q_{n+1}\), \(A\) supplies the permitted starts, and \(C\) supplies the recurrent set. Nondeterminism is preserved because the propositional transition matrix may admit several next codes. The fresh-start conversion from lines 64--85 applies with exactly the same timing.

21. **Lines 642--730: ACCEPT.** The regular finite-word schema constrains exactly \(x\leq t<y\), so its truth depends only on the displayed half-open input factor. Congruence, rank, multiperiodicity, and the Sequential Lemma have the correct standing. The Ramsey coloring yields homogeneity for every pair \(p<q\), not merely adjacent blocks. The deterministic finite-state-recursion bridge and its referred proof dependencies are not confused with nondeterministic omega-word acceptance.

22. **Lines 732--760: ACCEPT.** The conjunction scheduler reduces two recurrent conditions to one. For complementation, two reachability bits for each of \(m^2\) ordered state pairs give at most \(2^{2m^2}\) congruence classes. The homogeneous-block argument supports a finite union of stem/repeated-block sets. Requiring the repeated blocks to be nonempty is equivalent to requiring the concatenated prefix lengths to diverge; empty factors, when present in a factorization, may be deleted.

23. **Lines 762--789: ACCEPT.** The normal-form theorem’s dependence on Lemma 11 and repeated effective complementation is accurately bounded. The modern language/automaton equivalence is a valid handbook corollary: one direction turns the recurrent existential formula into finite automaton data; the converse bit-encodes any finite automaton state, excludes unused codes, and enforces initial, transition, and recurrent conditions propositionally. The source does not receive modern tuple wording or an unstated state bound.

24. **Lines 791--820: ACCEPT.** Lemma 12’s stem-cycle criterion is necessary and sufficient. From any satisfying sequence, a recurrent \(L\)-state \(U\) supplies a finite stem and a nonempty return path; conversely, repeating that return path produces an infinite satisfying sequence. With \(2^k\) truth-value states, loop deletion bounds a simple stem by at most \(2^k\) edges and a shortest nonempty return cycle by at most \(2^k\) edges. The subsequent finite enumeration and congruence-class test make the earlier normalization effective. The text correctly claims decidability and no modern complexity classification.

25. **Lines 822--908: ACCEPT.** The post-Theorem-2 consequences, the undefined source notation \(\Sigma_2^0\), definability comparisons, finite-set restriction, candidate axiom schema, ultimately periodic restriction, Theorems 3--4, arithmetic abbreviation discrepancy, and three open problems all remain at their printed strength. The new handbook abbreviation \(SC_{\mathrm{per}}\) has an exact eliminable definition, declared standing, nonredundancy, and immediate use. The synthesis problem is correctly distinguished from verification of a supplied implementation.

26. **Lines 910--920: ACCEPT.** The proof-ownership summary correctly itemizes printed proofs, referred lemmas, an outlined theorem, and handbook-owned modern packaging. No determinization or translation-complexity result is retrojected into the 1962 article.

### 6. McNaughton source boundary: N-c-013 lines 921--947

27. **Lines 921--947: ACCEPT.** The text asserts only what the acquired contemporary first-person report supports: the standing of an omega-event and the reported finite-state/regular equivalence. It explicitly leaves the article’s definitions, tuple, acceptance mechanism, constructions, examples, and proof open. It also keeps the separate game memo and its acknowledged fallacy outside the journal article. No unavailable body-dependent theorem is used elsewhere in the host section.

### 7. Safra’s 1995 expanded-manuscript construction: N-c-013 lines 948--1202

28. **Lines 948--963: ACCEPT.** The broad 1988 abstract claims and the detailed 1995 expanded-manuscript claims are assigned to different source objects. The text neither calls the expansion a proceedings facsimile nor promotes its “to appear” note into a journal-publication claim.

29. **Lines 965--995: ACCEPT.** The set-valued input transition may be empty, while the target deterministic convention is total and singleton-valued. B\"uchi, Muller, and Safra-order Rabin acceptance are correct. In Safra’s pair order, \(L_i\) is recurrent/good and \(U_i\) is eventually absent/bad; the text explicitly prevents a swap with Thomas’s \((E_i,F_i)\) notation.

30. **Lines 997--1042: ACCEPT.** The ordered vocabulary tree, parent and sibling data, label/color maps, proper-subset and branch-disjointness invariants, corrected left-to-right relation, and inclusive-path specificity relation are defined with exact standing. Proper containment gives each live node a state absent from all child labels; containment and branch disjointness make that state specific to exactly that node. Hence nodes inject into \(Q\), which is the later bound actually needed. Fixing the least initial vocabulary name is a canonical representative choice, not a new semantic component.

31. **Lines 1044--1079: ACCEPT.** This Safra variant has the correct order: advance every old label; create youngest accepting children from the advanced labels; remove duplicate responsibility to the right; remove empty subtrees; collapse saturated old nodes and record colors; then canonically rename surviving temporary nodes. The total traversal and least-unused-name rule turn “some unused name” into a genuine transition function. A name allocated to a new node is red in its creation state, then persists as white except on later green collapse events. At most \(n\) nodes survive, so the \(n\)-element persistent vocabulary suffices.

32. **Lines 1081--1107: ACCEPT.** Empty image of the root is a genuine omitted definedness case because the input transition is partial. The added absorbing rejecting state is reached exactly when no original run extends the consumed prefix. Putting it in every bad/red component and no good/green component makes every suffix reject and keeps the deterministic transition total. The \(n\) pairs \((G_v,B_v)\), interpreted in Safra’s good-then-bad convention, accept exactly a name which is green infinitely often and red only finitely often.

33. **Lines 1109--1157: ACCEPT.** The lineage explanation and both proof directions are sound. For soundness, consecutive green events on an eventually nonred name provide finite original-run segments, each containing an \(F\)-visit; the finite predecessor tree has an infinite branch by K\"onig’s lemma. For the first segment, a nonroot witness was born from an accepting subset, so the path from \(q_0\) to its first selected green label also contains an \(F\)-visit. For completeness, an accepting run is always represented at the root. If root collapses stop, its later accepting visits enter a child; duplicate removal moves responsibility only leftward among a finite set of older siblings. Repeating the argument down a tree of depth at most \(n\) yields a persistent, infinitely green name.

34. **Lines 1159--1176: ACCEPT.** The total label encoding by \(f:Q\to N\cup\{\star\}\) correctly handles original states absent from all live labels. A present state’s deepest containing node determines every ancestor occurrence, so the encoding recovers all labels under the invariants. The counts
    \[
    (n+1)^n=2^{O(n\log n)},\qquad 3^n=2^{O(n)}
    \]
    preserve the \(2^{O(n\log n)}\) state bound. The factorial lower bound justifies only optimality up to a constant in the exponent, exactly as stated.

35. **Lines 1178--1202: ACCEPT.** Complementation, limit-deterministic B\"uchi, and application bounds retain their own target classes. The definition of “deterministic in the limit” quantifies only accepting runs and is therefore correctly weaker than full determinism. The text keeps Safra’s \(n\)-name/\(n\)-pair construction separate from Thomas’s \(2n\)-name/\(2n\)-pair construction.

### 8. Thomas’s 1996 report-precursor construction: N-c-013 lines 1204--1409

36. **Lines 1204--1266: ACCEPT.** Run timing uses \(r(i+1)\) after reading \(\alpha(i)\), and deterministic transitions are explicitly total. B\"uchi and Muller acceptance are standard. Thomas-order Rabin is
    \[
    \exists i\;(\operatorname{In}(r)\cap E_i=\varnothing
    \land \operatorname{In}(r)\cap F_i\neq\varnothing),
    \]
    while Streett is its universal dual. The prose correctly says recurrence of \(F_i\) requires recurrence of \(E_i\). No Safra-order pair is silently substituted.

37. **Lines 1268--1289: ACCEPT.** The finite-union \(U_jV_j^\omega\) characterization includes the empty language through \(k=0\) and defines omega-concatenation so infinitely many empty factors cannot masquerade as an infinite word. Deterministic B\"uchi nonclosure under complement and deterministic Muller complementation both use total unique runs. The later report proof is not presented as evidence for the unread McNaughton body.

38. **Lines 1291--1313: ACCEPT.** The Thomas Safra state distinguishes the ordered tree, subset labels, persistent injective names, and current-update marks. The initial state is defined. Clearing old marks before the next update is necessary and sufficient to make \(M\) denote the event “collapse occurred in the immediately preceding/current letter update”; it does not alter lineage names.

39. **Lines 1314--1328: ACCEPT.** This is intentionally a different timing variant from the 1995 expansion: first create accepting children from the current labels, then advance every label—including the new children—over the current letter, then prune and collapse. It tracks an \(F\)-visit at the pre-transition run position, whereas the expansion tracks accepting mass after transition; both shifts preserve the infinitely-often condition. Deleting a duplicate state from the younger sibling and every label in its subtree preserves descendant containment, and deleting empty nodes with descendants restores the state invariants before collapse.

40. **Lines 1329--1339: ACCEPT.** If the advanced root is empty, all represented original runs have died. The empty unmarked absorbing tree state therefore preserves rejection, uses no node name, contributes no accepting pair, and is the exact totality completion required by the later deterministic claims.

41. **Lines 1340--1359: ACCEPT.** Surviving old names persist. New names are selected outside the **entire predecessor name set**, so a deleted lineage cannot be immediately confused with a new one; same-update depth-first allocation is injective and deterministic. At most \(n\) predecessor names are withheld and at most \(n\) new nodes can require names, so \(2n\) names suffice. The Rabin pair \((E_k,F_k)\) has the Thomas/host order: eventual absence from \(E_k\) means name \(k\) is eventually always present, and recurrence in \(F_k\) means it is marked infinitely often. The empty state is rejecting because it lies in every \(E_k\) and no \(F_k\).

42. **Lines 1360--1374: ACCEPT.** The proof summary has the correct persistent-lineage and bounded-depth invariants. The \(ab^\omega\) calculation validates mark lifetime: with create-before-advance timing, the lone visit to \(f\) produces one collapse on the following \(b\)-update; clearing that mark prevents false acceptance. The \(2^{O(n\log n)}\) state and exactly \(2n\)-pair bounds are compatible with the naming, label, tree, and mark counts. The factorial lower-bound qualification is not overstated as an exact constant.

43. **Lines 1376--1396: ACCEPT.** The B\"uchi/MSO translation directions, Boolean closure use of determinization, and track projection are correctly separated. The repaired input-free emptiness criterion requires a reachable nonempty cycle containing an \(F\)-state; this is necessary and sufficient. The displayed eventual-absence/infinitely-often schemata have the correct quantifier polarity. Bounded-prefix state tests can be expressed using finite monadic tracks, so the weak-MSO conclusion over omega-words is mathematically coherent.

44. **Lines 1398--1409: ACCEPT.** The concluding source-strength boundary is exact. It assigns the locators only to the report precursor and keeps B\"uchi 1962, McNaughton 1966, Safra 1988, Thomas 1997, and the Vardi--Wolper proceedings/preprint identities separate.

### 9. Host acceptance conventions and parity source seat: host lines 723--765; N-c-018 lines 615--647

45. **Host lines 723--745: ACCEPT.** The deterministic parity tuple is total, has one unique run, and accepts under the least priority occurring infinitely often being even. N-c-018 lines 634--647 explicitly use the same least-priority-recurring-even convention for the Bradfield--Stirling game seat. No least/greatest or min/max parity convention is swapped.

46. **Host lines 747--765: ACCEPT.** The deterministic Rabin tuple uses the Thomas order \((E_i,F_i)\): \(E_i\) is eventually absent and \(F_i\) recurrent. This agrees exactly with N-c-013 lines 1246--1252 and 1352--1359. It differs only notationally, and explicitly, from Safra’s \((L_i,U_i)\) good/bad order at N-c-013 lines 988--995 and 1092--1107. The tuple remains a word automaton; no tree-run semantics is imported.

### 10. Host LTL translation, product timing, SCC criterion, and PSPACE theorem: host lines 767--834

47. **Host lines 767--779: ACCEPT.** The theorem’s \(2^{O(|A|)}\) statement, explicit \(2^{3|A|}\) permitted-start product, projection, and one-state conversion agree with the detailed construction. Projection does not add states, and the extra start preserves the asymptotic bound.

48. **Host lines 781--784: ACCEPT.** Union and intersection closure are standard. Effective complementation is nontrivial; the cited Safra/Thomas material supplies deterministic complemented acceptance forms. The sentence does not claim that deterministic B\"uchi automata themselves are complement closed.

49. **Host lines 786--813: ACCEPT.** Product timing is exact. The fresh automaton start \(q_0\) is a pre-input state. The initial product vertices consume \(\ell_A(s_0)\), so their automaton coordinate is the state after the first word letter. Each later product edge follows \(sRt\) and consumes \(\ell_A(t)\), maintaining the same offset. Deleting the one pre-input automaton state cannot affect B\"uchi recurrence. Thus every product lasso projects to a legal path beginning at \(s_0\), and every violating program path lifts to a product run.

50. **Host lines 807--812: ACCEPT.** A reachable strongly connected component that meets \(F\) and contains a directed cycle yields a closed walk through an accepting vertex, hence an accepting lasso. Conversely, the vertices recurring in any accepting finite-graph run lie in a reachable cyclic SCC meeting \(F\). The explicit “contains a cycle” clause correctly excludes a singleton SCC with no self-loop.

51. **Host lines 814--819: ACCEPT.** For a fixed automaton, product vertices and edges are a constant-factor expansion of the explicit transition structure, so the graph check is linear in structure size. When the formula is input, the exponential translation is searched on the fly and the cited quadratic-space upper bound is polynomial in the combined encoding.

52. **Host lines 821--834: ACCEPT.** The correctness theorem restates both product directions and the finite-lasso witness. Sistla--Clarke’s original truth-in-an-R-structure problem is existential over a path from a supplied state, exactly the counterexample problem used here. Their PSPACE-hardness for a future temporal logic containing the required operators transfers by the polynomial map \(B\mapsto\neg B\) to the complement of universal model checking. The upper bound is in polynomial space, and deterministic polynomial space is closed under complement; therefore the combined universal problem is PSPACE-complete. Fixing the formula leaves a fixed finite automaton and hence linear explicit-structure complexity.

### 11. Remaining host integration in the required range: host lines 836--945

53. **Host lines 836--850: ACCEPT.** The finite-word B\"uchi--Elgot--Trakhtenbrot statement is the correct modern equivalence. Order and successor are MSO-interdefinable on finite linear words (with the empty word handled by the usual separate zero-length case), and the historical-source packaging is explicitly not asserted to be verbatim.

54. **Host lines 852--871: ACCEPT.** The host B\"uchi theorem exactly matches the presentation’s source-bounded result: no free individual variable in the stated core case, recurrent existential normalization, later effectivity, the handbook-owned two-way finite-data encoding, decidability by finite stem-cycle search, and no complexity bound.

55. **Host lines 873--876: ACCEPT.** The S2S decidability statement is correct and does not depend on any N-c-013 word-automaton proof.

56. **Host lines 878--928: ACCEPT.** The ranked-tree definition, bottom-up run, root acceptance, finite-tree MSO equivalence, weak/full coincidence on finite domains, subset determinization, Boolean closure, membership, and upward-reachability emptiness are correct. The text expressly prevents these finite-tree automata from being confused with Rabin’s infinite-tree automata.

57. **Host lines 930--945: ACCEPT.** The existing-example cross-references do not substitute a new proof for N-c-013. The `\input` at line 935 places the complete bounded presentation under the host theorem and method without changing any timing or acceptance convention. The following section boundary introduces no dangling N-c-013 hypothesis.

## Cross-cutting proof conclusions requested explicitly

- **Appendix-B local/eventuality/product/projection and batching:** correct in both directions; no pending-until escape exists, and projection guesses only viable local types.
- **Permitted-start conversion:** exact one-state language-preserving conversion, including \(Q_0=\varnothing\).
- **Markov events/support size:** cylinders, Borel event, almost-sure semantics, and positive-support size are coherent; universal emptiness is not substituted for probability one.
- **B\"uchi schemata/effectivity:** formula-class standing, recurrent normal form, automata encoding, complement congruence, finite stem-cycle decision, and later effectivity are sound at the stated source strength.
- **Safra 1995 update:** advance-then-create timing, rightward responsibility deletion, collapse colors, canonical reuse of the \(n\)-name vocabulary, dead sink, proof invariant, and \(n\) Rabin pairs are sound.
- **Thomas 1996 update:** create-then-advance timing, subtree deletion, current-update marks, predecessor-name withholding, canonical \(2n\)-name allocation, empty state, and \(2n\) Rabin pairs are sound.
- **Parity/Rabin conventions:** least-recurring-even parity is consistent with the explicit source seat; Safra good/bad pairs and Thomas/host bad/good pairs are never interchanged.
- **Product timing:** the host consumes the initial structure label in its initial product set and every destination label on the corresponding edge; the offset is correct and recurrence invariant.
- **PSPACE attribution:** the cited source problem is existential path truth, its hardness supplies the counterexample lower bound, and complement closure yields the universal-path classification.

## Open register obligations, non-rejecting under the stipulated semantics

1. **McNaughton 1966:** the registered ten-page journal body remains unread. The current manuscript asserts no acceptance definition, construction, proof, example, or body-specific theorem from it.
2. **Safra 1988:** the registered nine-page FOCS body remains unread. The detailed construction is explicitly attributed only to the distinct 1995 author-hosted expanded manuscript.
3. **Thomas 1997:** the registered final handbook chapter remains unreconciled. All detailed locators and theorem numbering are explicitly attributed to the May 1996 report precursor.
4. **Vardi--Wolper 1986:** the mathematical body is available in the author preprint, but comparison against a separate printed-proceedings file remains open. The manuscript does not call the preprint a proceedings facsimile.

These are source-register/provenance obligations. No theorem presently asserted depends on pretending that any unavailable registered body was read.

REGISTER STATUS: OPEN
