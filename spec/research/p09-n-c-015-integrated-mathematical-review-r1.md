# N-c-015 integrated mathematical review — Round 1

**Review date:** 2026-08-24  
**Seat:** fresh blind mathematical correctness and definedness review  
**Reviewed manuscript:** handbook/parts/p09/presentations/n-c-015.tex, lines 1--160  
**Reviewed host:** handbook/parts/p09/logic-in-computer-science.tex, lines 877--944

VERDICT: REJECT

## Evidence read

I read the complete actual LaTeX presentation, from line 1 through line 160, and the complete actual host interval, lines 877--944. The only supporting records read were:

- spec/research/p09-tata-2008-source-note.md;
- spec/research/p09-thatcher-wright-1968-acquisition-note.md;
- the compact N-c-015 portion of spec/research/p09-source-presentations-lot2-3.md, lines 751--775; and
- the ComonEtAl2007 and ThatcherWright1968 entries in handbook/bib/handbook.bib.

I used only the source, mathematical, version, and acquisition content of those permitted records. I did not use review or admission history appearing in, or linked from, a permitted record. The notes resolved the source questions; no original historical-source page was needed.

## Prohibitions observed

I did not open or use a manuscript PDF, historical review PDF, PNG, page image, render, or rendered handbook. I did not run LaTeX, a PDF build, a test, test harness, checker, repository script, automated validator, or hash operation. I did not open or use p09-tata-2008-independent-review-record.md, anything under spec/research/boards/p09-tata-2008/, any earlier or parallel integrated N-c-015 report, or any other review or admission record. I did not ask, list, or message another agent. I did not alter the manuscript, host, notes, compact record, ledger, bibliography, or any file other than this report.

## Line-specific must-fix

### [M1] Lines 73--80 and 85--91 leave the WSkS branching parameter unbound and make the displayed inclusion automaton ill-ranked at the stated generality

The presentation declares WSkS for arbitrary \(k\geq1\) at lines 49--52 and then states at lines 65--66 that every encoding symbol containing a \(0\) or \(1\) has arity \(k\). The \(k=2\) qualification at line 67 is grammatically local to the worked Example 3.3.3; the intervening bridge at lines 73--83 returns to an arbitrary finite ranked tree.

Nevertheless, the displayed automaton at lines 85--91 gives each nonnullary rule exactly two child states:

\[
00(q,q)\to q,\quad 01(q,q)\to q,\quad 11(q,q)\to q,\quad
\bot0(q,q)\to q,\quad \bot1(q,q)\to q.
\]

Those are well-ranked rules only after specializing the WSkS successor degree to \(k=2\). For \(k=1\), \(k=3\), or any other value, each of those label symbols has arity \(k\), so a transition with two children is not a transition over the alphabet defined at lines 62--66. The two coordinates in 00, 01, and so on are the two set-variable tracks \(X,Y\); they do not determine the number of tree children. Thus the display cannot, as currently introduced, be the atomic construction for the arbitrary \(k\) fixed at line 49.

The same missing parameter binding is visible one paragraph earlier. To translate an arbitrary finite ranked alphabet \(F\) into the successor structure, the presentation must choose a WSkS degree satisfying

\[
k\geq \max\{\operatorname{arity}(f):f\in F\},
\]

with any \(k\geq1\) when every symbol is nullary. Only then is every child atom \(y=xi\) at line 78 typed by one of the available successors \(i\in\{1,\ldots,k\}\).

This is a local repair, but it is required for definedness. A source-faithful minimal correction would:

1. bind \(k\) to at least the maximum rank before the finite-tree coding at lines 73--80; and
2. introduce the Figure 3.9 transition list explicitly as the \(k=2\) instance, or replace every pair \((q,q)\) by a \(k\)-tuple of copies of \(q\).

Until one of those repairs is made, the displayed automaton is not a well-typed ranked-tree automaton under the presentation's own general \(k\)-ary encoding.

## Remaining mathematical and definedness audit

No additional must-fix was found.

### Finite terms, runs, and decision operations

Lines 6--30 maintain the 2008-release boundary and keep TATA's finite terms separate from Rabin's infinite labelled input tree. Lines 12--16 define nullary terms and recursively formed \(n\)-ary ground terms before using finite ordered trees. Lines 16--30 give the complete source tuple, transition type, bottom-up run, root acceptance, recognizable-language standing, and the literal source-to-host notation map. The host definition at lines 884--913 has the same data in the advertised different tuple order.

The run at presentation lines 32--37 is valid: the two nullary rules license the leaf states and the one binary rule licenses the final root state. Removing the binary rule leaves the same ground term without a run. Lines 39--47 state determinism as uniqueness of the target for one symbol/child-state tuple, give the same-language reachable-subset construction, state Boolean closure at theorem strength rather than inventing a new construction, and give the correct least-fixed-point emptiness test. If the ranked alphabet has no nullary symbol, the marking seed is empty and no final state can become marked, matching the fact that the ground-term algebra is empty.

### WSkS domains and finite-set encoding

Lines 49--60 correctly distinguish word-valued first-order variables from finite-set-valued monadic variables and give the singleton-set reduction's four atomic forms. In \(X=Yi\), \(i\) is one of the fixed successor letters, and the sentence correctly describes the unique-word meaning. The root atom \(X=\epsilon\) has the corresponding singleton-root meaning.

Lines 62--71 correctly encode a tuple of finite sets. A coordinate is \(1\) at a member, \(0\) at a proper prefix that extends to a member, and \(\bot\) outside that finite prefix closure. The all-\(\bot\) vector is nullary, while any vector carrying \(0\) or \(1\) is branching. The worked labels for
\(S_1=\{\epsilon,11\}\), \(S_2=\varnothing\), and \(S_3=\{11,22\}\) are correct, including the all-\(\bot\) padding leaves required to terminate the finite full binary shape.

Subject to the parameter repair in [M1], lines 73--83 give the right finite-tree bridge. The finite position set \(D\), its symbol-label subsets, and the source arity constraints describe one ground term. Label atoms become membership in \(X_f\), child atoms become successor equations, first-order quantifiers are relativized to \(D\), and monadic quantifiers are relativized to subsets of \(D\). The ambient infinite prefix tree is consequently a coding structure; it is not passed to the bottom-up automaton as an infinite input.

### Atomic inclusion automaton and logical constructors

After specializing the display to \(k=2\), the rule list at lines 88--91 is mathematically correct and complete for \(X\subseteq Y\). The missing two-track symbols are exactly:

- \(10\), where the current position belongs to \(X\) but not \(Y\);
- \(1\bot\), where it belongs to \(X\) but lies outside the prefix closure of \(Y\); and
- \(0\bot\), where a descendant belongs to \(X\) while the current position lies outside the prefix closure of \(Y\).

The all-\(\bot\) symbol is correctly nullary. The remaining five nonnullary symbols are precisely the compatible binary-tree labels. Lines 93--96 state the needed coordinate extension before union, complement for negation, and existential track projection at the operative outline strength attributed to Lemma 3.3.4.

### Accepting-run formula, including the nullary case

The local clause at lines 98--110 is correct; it is not a must-fix. The quantified state-position sets partition exactly the encoded finite domain \(D\), and the root disjunction requires the root's unique state to be final. For a symbol \(f\) of arity \(s>0\), the clause says that a node labelled \(f\) and assigned state \(q\) must have child states matching at least one rule \(f(q_1,\ldots,q_s)\to q\).

For a nullary symbol, \(s=0\). Under the standard finite-connective conventions

\[
\bigwedge_{i=1}^{0}\varphi_i=\top,
\qquad
\bigvee_{\varnothing}\varphi=\bot,
\]

the right side is true exactly when \(\Delta\) contains at least one rule \(f\to q\), and false when it contains none. No nonexistent child term \(xi\) is demanded. Therefore a nullary \(f\)-node can bear precisely the states licensed by nullary transitions, exactly as a bottom-up run requires. The same empty-disjunction convention correctly makes the final-root condition false when \(Q_f=\varnothing\).

An implication, rather than a biconditional, is sufficient: the label sets select exactly one \(f\) at each position, the \(Y_q\) sets partition \(D\), and the conjunction over all \(f,q\) therefore activates exactly the clause for the node's actual label and state.

### Exact logical directions and the closed-sentence rule

Lines 85--96 provide the restricted-formula-to-automaton induction, while lines 98--110 existentially describe an accepting run for the converse. Lines 112--118 correctly refuse to treat Theorem 3.3.7's slogan as more precise than those two lemmas. For a closed sentence there is one empty tuple of free-track assignments. Under the explicit source convention it is represented by the one-node tree labelled by the nullary symbol \(\top\). A run on that tree consists of one transition \(\top\to q\), so truth of the sentence is equivalent to the existence of \(\top\to q_f\) for some \(q_f\in Q_f\). No all-zero track or nontrivial path is silently introduced.

### Copying language

Lines 120--129 give a sound proof under the exact ranked alphabet
\(F=\{a^{(0)},f^{(2)}\}\). Determinization is available by Theorem 1.1.9. Every term \(t\) must have a run state because the required term \(f(t,t)\) is accepted. If distinct \(t,u\) reached the same deterministic state \(q\), the transition that accepts \(f(t,t)\) from child tuple \((q,q)\) would give \(f(t,u)\) the same final root state. Since \(f(t,u)\notin L\), distinct terms require distinct states. The ground-term set is infinite, contradicting finiteness of the state set.

### Weak/full and historical-source boundaries

Lines 131--139 correctly distinguish WSkS finite-set assignments from full SkS assignments over arbitrary subsets of the infinite successor tree. Weak and full monadic quantification coincide only after the input domain itself is finite. That fact neither changes the root-down infinite-input automata needed for full SkS nor identifies them with finite bottom-up automata.

Lines 141--160 obey the technical-name rule at the unavailable-source boundary. “Finite algebras” is reported only as abstract language, not assigned a hypothetical formal definition. The missing Thatcher--Wright algebraic signature, recognition relation, logic, coding, theorems, examples, and proofs are stated as owed artifacts. The TATA reconstruction is separately attributed and its proof-reproduction boundary is explicit. The unavailable Thatcher--Wright body therefore remains an open source-register obligation but is not itself the reason for this mathematical rejection.

### Host consistency and technical-name rule

The host at lines 884--934 agrees with the presentation on ranked-symbol arities, nullary leaves, bottom-up transition types, root acceptance, subset determinization, Boolean closure, and nullary-upward emptiness. Its finite-domain weak/full statement and explicit separation from Rabin's S2S construction match presentation lines 131--139. The only host-facing definedness break is [M1]: the presentation has not typed its general WSkS branching degree and its displayed binary rules consistently.

Apart from [M1], new technical names satisfy the repository rule. “Ground term,” “finite ordered \(F\)-tree,” “bottom-up automaton,” “run,” “recognizable,” “WSkS,” and “full SkS” are locally defined, assigned their mathematical standing, distinguished from neighboring notions, and used later. The Thatcher--Wright paragraph correctly describes an owed artifact instead of naming a hypothetical reconstruction.

REGISTER STATUS: OPEN
