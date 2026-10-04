# Round 3 mathematical and proof-correctness review — TATA 2008 (`N-c-015.b`)

## Mandate, independence, and evidence completed

I reviewed the complete Frozen Round 3 snapshot from the mathematical-and-proof-correctness seat. I used only the charter, the nine frozen objects, the twenty-seven named TATA renders, and the five named Thomas identity/page-map renders. I did not consult a prior-round report, another Round 3 report, the board ledger, the chair transcript, another board, conversation history, memory, web results, staging or layout material, or a handbook PDF, and I did not contact another reviewer.

Before making a substantive judgment, I independently recomputed all nine SHA-256 identities with a native read-only hash operation. All nine values agree byte-for-byte with the Round 3 charter:

| Frozen object | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | 2,292,046 | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | match |
| `handbook/parts/p09/presentations/n-c-015.tex` | 9,443 | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | 119,151 | `392E4123928A4DF4E40099104A85466D326E7DC548D43C36751C381778A9AA47` | match |
| `handbook/bib/handbook.bib` | 207,104 | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | match |
| `spec/research/p09-tata-2008-source-note.md` | 10,711 | `E8BB8448B3AAA119575EBC6EE16BD79A5F4F50A584875234513A61FC627FA948` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | 228,295 | `0A1E5537F20DC16D6421FE6FC21B846180B6548F8AA9B5B6A2CC5942FC0524B3` | match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | 4,134 | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | match |
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | 478,293 | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | match |
| `spec/research/p09-thomas-1996-report-source-note.md` | 4,369 | `00401B053476E6F776FBBB92321D780E01F4F6F8E6A3FFE96B8DBF7168C557D2` | match |

I then read all seven textual objects completely: the 161-line TATA presentation, the 2,387-line shared Part IX file, the 6,284-line bibliography, the 197-line TATA source note, the 916-line compact record, the 82-line Thatcher--Wright acquisition note, and the 93-line Thomas version/custody note.

I visually inspected every named render at original detail. The TATA set was `core-rendered/page-001.png`, `page-002.png`, `page-012.png`--`page-014.png`, `page-020.png`--`page-028.png`, `page-031.png`, `page-041.png`, and `page-044.png`, plus `relevant-rendered/page-088.png`--`page-097.png`. The Thomas set was `inspect-title-01.png`, `inspect-title-02.png`, `inspect-title-03.png`, `inspect-body-start-04.png`, and `inspect-body-end-75.png`. Thus the visual judgment below rests on all twenty-seven required TATA pages and all five required Thomas pages, including the formulae and symbols as rendered rather than on extraction.

No test, test harness, automated checker, repository script, TeX command, build, or handbook-PDF inspection was run.

## Finding

### TATA-R3-MP-01 — must-fix — the Thomas custody note silently replaces the report's prospective handbook title with the later publication title

The Thomas version/custody note says, as a claim about what the acquired report's abstract says, that a modified version “would become a chapter of the *Handbook of Formal Languages*” (`spec/research/p09-thomas-1996-report-source-note.md:51--56`). The controlling unnumbered abstract, physical PDF page 2 (`inspect-title-02.png`), instead prints the prospective title *Handbook of Formal Language Theory*. The former is the title of the eventual registered 1997 publication family, as the note itself records separately at lines 5--11 and the bibliography records at `handbook/bib/handbook.bib:2358--2366`; it is not the wording printed in the 1996 report abstract.

This does not undermine the well-supported conclusion that the acquired object is the May 1996 Kiel report precursor: the report title page, abstract, contents, printed first page, and printed endpoint establish that conclusion. It does, however, silently normalize the precursor's own prospective-publication wording to the later publication title inside the very record whose purpose is to keep those versions distinct. That is a source-wording and cross-version mismatch under T20, and the charter makes a source mismatch at least a must-fix. Repair should report *Handbook of Formal Language Theory* as the abstract's literal prospective title and then, in a separate sentence, identify the eventual registered chapter in *Handbook of Formal Languages*. No other frozen statement needs to be broadened, and the 1997 body and reconciliation must remain open.

## Independent mathematical reconstruction and stress test

Apart from TATA-R3-MP-01, I found no mathematical, typing, quantifier, theorem-strength, ownership, or terminology defect in the frozen TATA reconstruction.

### Finite ranked terms, runs, determinization, closure, and emptiness

For a finite ranked alphabet (F=\bigsqcup_{n\geq0}F_n), the ground terms are the least set containing each (a\in F_0) and closed under (f(t_1,\ldots,t_n)) for (f\in F_n). This makes the inputs finite ordered trees. The manuscript states exactly this at `n-c-015.tex:12--16`, and the shared definition supplies the same least-set and nullary-leaf clauses at `logic-in-computer-science.tex:845--854`.

For (A=(Q,F,Q_f,\Delta)), a bottom-up run assigns one state to every position and licenses a parent state (q) only through a rule (f(q_1,\ldots,q_n)\to q) matching the symbol and ordered child states. For (n=0), the same clause is the nullary rule (a\to q); there are no child premises. Acceptance is exactly final state at the root, and recognizability is existence of such an automaton accepting exactly the language. The reader states these clauses at `n-c-015.tex:18--30`, the shared definition at `logic-in-computer-science.tex:856--867`, and the controlling source gives the tuple, reduction, run, and successful-root clauses on printed pp. 20--22 (physical pages 21--23).

The determinization can be reconstructed by assigning to each ground term

\[
 S(t)=\{q\in Q:t\text{ has a bottom-up run with root state }q\}.
\]

For (t=f(t_1,\ldots,t_n)), its deterministic target is

\[
 \{q\in Q:\exists q_i\in S(t_i)\; f(q_1,\ldots,q_n)\to q\in\Delta\}.
\]

At arity zero this is the set of targets of the nullary symbol, including the empty subset when no source rule exists. Hence the reachable deterministic states are exactly the subsets (S(t)) reached by ground terms, the transition target is unique for every fixed symbol/child-subset tuple for which a transition is retained, and (t) is accepted exactly when (S(t)\cap Q_f\ne\varnothing). This proves same-language determinization without assuming completeness or reachability of every subset. It agrees with `n-c-015.tex:39--41`, the shared theorem at `logic-in-computer-science.tex:883--884`, and Theorem 1.1.9 and its algorithm on printed pp. 25--27 (physical pages 26--28).

Union is obtained by disjoint union or a complete product construction, intersection by product, and complement after effective determinization and completion. The manuscript claims only effective Boolean closure (`n-c-015.tex:41--47`; `logic-in-computer-science.tex:883--888`), matching Theorem 1.3.1 on printed p. 30 (physical page 31).

For emptiness, let (M) be the least state set containing the targets of all nullary rules and closed under every transition whose child states are already in (M). Induction on term height proves (q\in M) exactly when some ground term reaches (q). Therefore nonemptiness is exactly (M\cap Q_f\ne\varnothing), including partial transition tables and automata containing unreachable states. Maintaining an unmet-child count or the equivalent Horn fixed point visits the finite representation linearly. This is the exact route stated at `n-c-015.tex:43--46`, `logic-in-computer-science.tex:884--886`, and `p09-tata-2008-source-note.md:67--72`, and printed in Theorem 1.7.4 and its proof on p. 40 (physical page 41).

The handbook-owned run at `n-c-015.tex:32--37` is correct: the two nullary rules label the leaves of (f(a,b)), the displayed binary rule uniquely licenses the final root, and deleting that root rule leaves no matching transition and hence no run. Its ownership is stated at `n-c-015.tex:154--160`; it is not passed off as a source-printed example.

For Exercise 1.4, assume a deterministic recognizer for (L=\{f(t,t):t\in T(F)\}), with (F=\{a^{(0)},f^{(2)}\}). Every (t) must have a run, since an accepting run on (f(t,t)) restricts to a run on each occurrence of (t). If distinct (t,u) reached the same state (q), the final transition used above the pair ((q,q)) in the accepting run on (f(t,t)) would also accept (f(t,u)), which is not in (L). The infinitely many terms would therefore require distinct states, contradicting finiteness. This handles partial deterministic tables and the previously easy-to-miss existence-of-a-run premise. It matches `n-c-015.tex:120--129` and the exact exercise statement on printed p. 43 (physical page 44); the proof is correctly labelled handbook-owned at lines 158--160.

### WSkS encoding and both logical directions

The semantic domains are correct: first-order variables range over words in \(\{1,\ldots,k\}^*\), while second-order variables range over finite sets of those words (`n-c-015.tex:49--52`; printed pp. 87--88). Proposition 3.3.1's restricted atoms are exactly (X\subseteq Y), \(\operatorname{Sing}(X)\), (X=Yi), and (X=\epsilon), with (X=Yi) relating the unique words by right-appending (i) (`n-c-015.tex:52--60`; printed pp. 89--90).

For a tuple of finite sets, a coordinate is (1) at a member, (0) at a proper prefix of a member that is not itself a member, and \(\bot\) otherwise. Any vector containing (0) or (1) has arity (k); (\bot^n) is nullary. The worked labels in `n-c-015.tex:62--71` agree with Figure 3.7 and Example 3.3.3 on printed pp. 90--91: root (1\bot0), positions (1,2) labelled (0\bot0,\bot\bot0), positions (11,22) labelled (1\bot1,\bot\bot1), and every added padding leaf labelled (\bot\bot\bot). In particular, the empty second set produces a \(\bot\) second track everywhere and does not become an all-zero encoding.

For the restricted-formula-to-automaton direction, the complete one-state transition list for (X\subseteq Y) is

\[
 \bot\bot\to q,\;00(q,q)\to q,\;01(q,q)\to q,\;11(q,q)\to q,
 \;\bot0(q,q)\to q,\;\bot1(q,q)\to q.
\]

These are exactly the six coordinate pairs compatible with inclusion; the omitted (10), (0\bot), and (1\bot) cases violate it. The source's Figure 3.9 on printed p. 92 (physical page 93) controls the symbols, and the transcription at `n-c-015.tex:85--92` is exact. For disjunction, cylindrification supplies unconstrained tracks for variables absent from a disjunct before union; negation uses effective complement; and existential set quantification projects the quantified track (`n-c-015.tex:93--96`; Lemma 3.3.4, printed pp. 91--93).

For the automaton-to-formula direction, one monadic variable (Y_q) per state partitions exactly the encoded finite position domain, the root belongs to some final-state set, and for each symbol (f) and state (q) the local implication is

\[
 \forall x\left((x\in X_f\land x\in Y_q)\Rightarrow
 \bigvee_{f(q_1,\ldots,q_s)\to q\in\Delta}
 \bigwedge_{i=1}^{s}xi\in Y_{q_i}\right).
\]

The implication direction is correct: the node's already chosen state and label force one transition whose ordered child states match the partition. If no transition matches, the disjunction is false. If (s=0), the child conjunction is empty and therefore true exactly when a matching nullary rule appears in the disjunction. The partition makes every encoded node receive exactly one state, and the final-root disjunction makes the run accepting. This matches `n-c-015.tex:98--110` and Lemma 3.3.6 on printed pp. 94--95 (physical pages 95--96).

The closed-sentence case is also exact. After all free tracks are removed, the source's precise convention leaves the sole nullary symbol (\top). There is only one possible ground input, so validity is equivalent to the existence of a rule (\top\to q_f) with (q_f\in Q_f), not to a zero-track or padded infinite-tree claim. The reader records both the source's informal “empty alphabet” wording and the precise singleton-constant convention at `n-c-015.tex:112--118`, matching Theorems 3.3.7--3.3.8 on printed p. 95 (physical page 96).

### Finite-tree MSO bridge, weak/full boundary, and ownership

For a finite ranked tree, let (D) be its finite position domain and (X_f\subseteq D) the label class for each symbol. The term clauses enforce one label per node, prefix closure, and the exact children demanded by arity. A label atom becomes (x\in X_f), and the (i)-th-child atom becomes (y=xi). When a finite-tree MSO formula is interpreted in the ambient successor structure, every element quantifier is guarded by membership in (D), and every monadic quantifier is restricted to a subset of (D). Conversely, the state sets above partition exactly (D). Thus the prefix tree is only the coding structure; the automaton input remains the finite encoded term. These are the explicit clauses at `n-c-015.tex:73--83` and `logic-in-computer-science.tex:876--882`, supported by the term encoding and Lemmas 3.3.4/3.3.6 on printed pp. 89--95.

Theorem 3.3.7 is correctly presented only as TATA's “not very precise” slogan; the two lemmas retain control of the coded directions (`n-c-015.tex:112--114`; printed p. 95). Full SkS instead permits arbitrary, possibly infinite subsets of the infinite successor tree and calls for root-down automata on infinite inputs and a different complementation proof. Weak and full monadic quantification coincide on an actually finite domain because every subset of that domain is finite; this observation neither changes the domain of WSkS nor converts a finite bottom-up automaton into Rabin's infinite-tree device. The reader and shared theorem state exactly this boundary at `n-c-015.tex:131--139` and `logic-in-computer-science.tex:881--890`, agreeing with printed pp. 95--96.

The reconstruction boundary is honest. The reader gives the operative constructions needed by the shared theorem but does not claim to reproduce every source transition table or every proof of Theorems 1.1.9, 1.3.1, and 1.7.4 (`n-c-015.tex:154--160`). The source exercise remains a source exercise, while the small run and deterministic separation proof are expressly handbook-owned. The Thatcher--Wright technical body remains unacquired and is not reconstructed from TATA (`n-c-015.tex:141--152`; `p09-thatcher-wright-1968-acquisition-note.md:64--82`; `p09-tata-2008-source-note.md:187--197`).

## Mandatory invariant disposition

- **T01 — PASS.** The eight-author title-page order, title, HAL identity, release date, 263/262-page custody map, and evolving-work 2007 versus fixed-release 2008 distinction agree across the HAL cover and internal title (physical TATA pp. 1--2), the 18 November 2008 footers, `n-c-015.tex:6--10`, `handbook.bib:5847--5853`, `p09-tata-2008-source-note.md:14--29`, and `p09-source-presentations-lot2-3.md:694--696`.

- **T02 — PASS.** The HAL cover (physical TATA p. 1) establishes an authorized deposit, while the records claim neither Creative Commons status nor blanket republication rights and keep the PDF/renders as evidence (`p09-tata-2008-source-note.md:31--34`).

- **T03 — PASS.** The operative objects are finite ranked terms, and the exclusion of infinite-tree automata remains explicit in the reader and shared definition (`n-c-015.tex:6--16`; `logic-in-computer-science.tex:868--872`), matching TATA's printed introduction pp. 11--13.

- **T04 — PASS.** Ranked arities, nullary and positive-arity formation, finite ordered-tree standing, literal TATA tuple (A=(Q,F,Q_f,\Delta)), and the nonconflicting (F_{\mathrm{TATA}}\mapsto\Sigma), (Q_f\mapsto F_{\mathrm{handbook}}) map are explicit at `n-c-015.tex:12--30` and `logic-in-computer-science.tex:845--867`, matching printed pp. 20--22.

- **T05 — PASS.** Transition typing, bottom-up node assignment, final-root acceptance, recognizability, and the empty child tuple for nullary rules are correct at `n-c-015.tex:20--27` and `logic-in-computer-science.tex:856--867`, matching printed pp. 20--22.

- **T06 — PASS.** Determinism is target uniqueness for a fixed symbol/child-state tuple; the powerset state associated with a term is well typed, only reachable subsets need be retained, and same-language strength is preserved (`n-c-015.tex:39--41`; `p09-source-presentations-lot2-3.md:698`; Theorem 1.1.9, printed pp. 25--27).

- **T07 — PASS.** Effective union/intersection/complement and bottom-up marking are exact; nullary targets seed the least fixed point, unreachable states do not matter, and nonemptiness is exactly a marked final state. The reader limits linear time to the automaton representation and source route (`n-c-015.tex:41--47`; `p09-tata-2008-source-note.md:67--72`; printed pp. 30 and 40).

- **T08 — PASS.** The run on (f(a,b)), the missing-root-rule no-run case, and handbook ownership are all explicit (`n-c-015.tex:32--37,154--160`), with the run semantics controlled by printed pp. 20--22.

- **T09 — PASS.** Word and finite-word-set ranges and all four restricted atoms are exact (`n-c-015.tex:49--60`; `p09-tata-2008-source-note.md:82--86`; printed pp. 87--90).

- **T10 — PASS.** The (0/1/\bot) meanings, arities, empty second track, five named nonpadding labels, and nullary (\bot^3) padding agree with Definition 3.3.2/Figure 3.7/Example 3.3.3 (`n-c-015.tex:62--71`; printed pp. 90--91).

- **T11 — PASS.** (D), the symbol-label subsets, label and child translations, both quantifier restrictions, and the coding/input distinction are explicit (`n-c-015.tex:73--83`; `logic-in-computer-science.tex:876--882`; printed pp. 89--95).

- **T12 — PASS.** The inclusion automaton's six rules are complete, and cylindrification, union, complement, and projection have their correct inductive roles (`n-c-015.tex:85--96`; Lemma 3.3.4 and Figure 3.9, printed pp. 91--93).

- **T13 — PASS.** The state sets partition exactly the finite encoded domain, the root is final, and the local implication has the correct transition-target and ordered child-state directions, including the nullary empty-conjunction case (`n-c-015.tex:98--110`; Lemma 3.3.6, printed pp. 94--95).

- **T14 — PASS.** The “not very precise” qualification, lemma-controlled directions, empty/free-track boundary, sole nullary (\top), and (\top\to q_f) criterion are all preserved (`n-c-015.tex:112--118`; Theorems 3.3.7--3.3.8, printed p. 95).

- **T15 — PASS.** The exact ranked alphabet and copying language are retained, and the handbook proof establishes both existence of a reached state for every term and injectivity forced by the crossed-pair argument (`n-c-015.tex:120--129`; Exercise 1.4, printed p. 43).

- **T16 — PASS.** Arbitrary-set full SkS, finite-set WSkS, root-down infinite-input automata, different complementation, finite-domain weak/full coincidence, and the prohibition on turning the input infinite are all separated (`n-c-015.tex:131--139`; `logic-in-computer-science.tex:881--890`; printed pp. 95--96).

- **T17 — PASS.** The shared definition and theorem agree with the reader on finite ranked terms, bottom-up runs, recognition, MSO equivalence, determinization, Boolean closure, emptiness, and Rabin nonconflation (`logic-in-computer-science.tex:845--891`; TATA printed pp. 20--22, 25--27, 30, 40, and 89--96).

- **T18 — PASS.** Source definitions, source theorem constructions, source exercise, handbook run, and handbook proof retain their actual ownership and reproduced-proof strength (`n-c-015.tex:154--160`; `p09-tata-2008-source-note.md:61--78,104--125`; printed pp. 20--22, 25--27, 30, 40, and 43).

- **T19 — PASS.** The reader, detailed note, compact record, and acquisition note keep TATA's printed p. 95 citation historically separate from the uninspected Thatcher--Wright body. RC-1713 is only a lead, every body-dependent object/result remains owed, and no hypothetical technical answer is named (`n-c-015.tex:141--152`; `p09-source-presentations-lot2-3.md:684--692,910`; `p09-thatcher-wright-1968-acquisition-note.md:27--34,64--82`; `p09-tata-2008-source-note.md:187--197`).

- **T20 — FAIL (TATA-R3-MP-01).** The TATA bibliography, numbering, notation, page locators, ownership, and status records otherwise agree, and the Thomas object is correctly classified as a May 1996 report precursor with the 1997 body/reconciliation open. But `p09-thomas-1996-report-source-note.md:51--56` misstates the prospective handbook title printed on the Thomas report's unnumbered abstract, physical p. 2, thereby importing the later registered title into a purported report-wording claim.

- **T21 — PASS.** Actual mathematical first uses locally define or source-type ranked alphabets, terms, automata, runs, recognizability, WSkS, restricted atoms, finite encodings, and full SkS before reliance (`logic-in-computer-science.tex:845--872`; `n-c-015.tex:12--30,49--71,131--139`). The missing Thatcher--Wright body is described as an owed source visit rather than assigned a speculative technical name (`p09-thatcher-wright-1968-acquisition-note.md:64--82`; `p09-source-presentations-lot2-3.md:688--692`).

- **T22 — PASS.** The frozen records consistently distinguish acquisition, reconstruction, review, and admission. They keep `N-c-015.a`, `N-c-015` overall, Part IX, builds, rendered-handbook review, human/user review, the book, and publication outside this board's possible completion claim (`n-c-015.tex:154--161`; `p09-tata-2008-source-note.md:3--12,178--185`; `p09-source-presentations-lot2-3.md:706,900--916`). The rejection below closes nothing.

## Decision

The finite-tree and WSkS mathematics is correct and source-strength-calibrated on the frozen hashes. Nevertheless, Round 3 makes the adjacent Thomas version correction a mandatory invariant, and TATA-R3-MP-01 is a source-wording/version-boundary must-fix in that frozen correction. Admission of `N-c-015.b` on this snapshot therefore cannot be recommended.

VERDICT: REJECT — TATA-R3-MP-01
