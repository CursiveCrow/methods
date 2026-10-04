# Round 5 mathematical and proof correctness review — Rabin 1969

## Review result and scope

I find no mathematical, proof-theoretic, logical, definitional, attributional, or scope defect within the Mathematical and proof correctness mandate.  In particular, no blocker, must-fix, should-fix, consider, discard, or unresolved-user finding survives this review.  The conclusion applies only to the frozen `N-c-014.d` manuscript content.  It does not accept the rest of `N-c-014`, Part IX, any rendered handbook page, any build, any other part, the book, or human/user review.

This was a fresh whole-snapshot review.  I read the charter in full and used only the six Round 5 frozen objects and the two authorized original-detail render sets.  I did not read any earlier report, partial or unfiled Round 4 work, another Round 5 report, `ledger.md`, `transcript/chair.md`, another board or transcript, the staging draft, the layout extraction as controlling evidence, or conversation history.  I did not communicate with another reviewer.  I ran no test, automated checker, repository script, TeX command, interim build, handbook-PDF inspection, or build.

## Frozen identities

I recomputed each identity directly from the file bytes with the operating system's native SHA-256 file-hash facility before substantive review.  Every observed digest equals the Round 5 digest in the charter.

| Frozen object | Charter SHA-256 | Recomputed SHA-256 | Result |
|---|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121` | `78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E` | `E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E` | exact match |

## Evidence inspected

I visually inspected the complete authorized Rabin render set at original detail: `page-01.jpg`, `page-02.jpg`, `page-03.jpg`, `page-04.jpg`, `page-05.jpg`, `page-06.jpg`, `page-07.jpg`, `page-08.jpg`, `page-09.jpg`, `page-10.jpg`, `page-11.jpg`, `page-12.jpg`, `page-13.jpg`, `page-14.jpg`, `page-15.jpg`, `page-16.jpg`, `page-17.jpg`, `page-18.jpg`, `page-19.jpg`, `page-20.jpg`, `page-21.jpg`, `page-22.jpg`, `page-23.jpg`, `page-24.jpg`, `page-25.jpg`, `page-26.jpg`, `page-27.jpg`, `page-28.jpg`, `page-29.jpg`, `page-30.jpg`, `page-31.jpg`, `page-32.jpg`, `page-33.jpg`, `page-34.jpg`, `page-35.jpg`, and `page-36.jpg`.  These are physical PDF pp. 1--36: the custody cover and all printed Rabin pp. 1--35.

I also visually inspected the complete authorized Meyer render set at original detail: `page-485.png`, `page-486.png`, `page-487.png`, `page-488.png`, `page-489.png`, and `page-490.png`.  These are physical PDF pp. 485--490 and printed Meyer pp. 477--482.

I read the complete frozen manuscript file, the complete detailed source note, the complete compact record with particular attention to `N-c-014.d` at lines 660--672 and its adjacent authority boundaries, and the frozen bibliography with particular attention to the Rabin, Meyer, Thatcher--Wright, McNaughton, and Thomas records.  The mathematical reconstruction audited below is the Rabin portion of the frozen manuscript at lines 908--1437.  Formulae, symbols, numbering, pagination, and printed claims were checked against the original-detail source pages, not against OCR or layout extraction.

## Independent mathematical reconstruction

### 1. Structures, trees, ordinary automata, and the logical translations

At frozen manuscript lines 914--963, the root is Rabin's `\(\Lambda\)`, not an editorial `\(\epsilon\)`.  The manuscript defines the initial-segment order by `\(y=xz\)`, the successor maps by `\(r_a(x)=xa\)`, and the predecessor with the special root equation `\(\operatorname{pd}(\Lambda)=\Lambda\)`.  Its Definition 1.1 display quantifies over every `\(0<n\leq\omega\)`, gives `\(T_n=n^*=\{i:i<n\}^*\)`, and includes the successor family and both the initial-segment and lexicographic orders.  The qualification that both orders can be eliminated in favor of the successors for finite `\(n\)`, but not in the `\(T_\omega\)` case, agrees with Rabin printed pp. 4--5.  The displayed types make all concatenations and maps defined.

At lines 965--1014, the tree may be rooted at any `\(x\in T\)`, with `\(T_x=\{y:x\preccurlyeq_{\mathrm{is}}y\}\)`.  The path clauses give one successor at every visited node and preserve predecessors back to `\(x\)`, so they describe an infinite branch of the rooted full binary subtree.  The transition table and automaton are correctly separated:

* the table is `\(\langle S,M\rangle\)` with `\(M:S\times\Sigma\to\mathcal P(S\times S)\)`;
* the ordinary automaton is `\(\langle S,M,S_0,F\rangle\)` with `\(S_0\subseteq S\)` and `\(F\subseteq\mathcal P(S)\)`.

For a branch-state map, `\(\operatorname{In}\)` is the set of states with infinite inverse image.  A run is a single global map satisfying both-child transitions at every node.  Thus the acceptance display at lines 997--1005 has exactly the ordinary prefix
`\(\exists r\,[r(x)\in S_0\land\forall\pi\,(\pi\text{ path}\Rightarrow\operatorname{In}(r|\pi)\in F)]\)`.
The later pair sequence is not substituted for `\(F\)`.  The arbitrary-root scope and the distinction between a possibly nontotal table and an automaton match Rabin printed pp. 5--7.

The closure dependencies at lines 1016--1023 are sufficient and no stronger than the source.  Lemma 1.2 gives a one-start normalization.  Theorem 1.3 gives union and intersection.  Theorem 1.4 is described in its two directions: deleting one coordinate by projection and adding a wholly unconstrained coordinate.  Theorem 1.5 supplies complement and Theorem 1.6 supplies the language-emptiness decision.  This is the dependency set used by the sentence decision on Rabin printed pp. 6--10; the manuscript does not insert an unnamed operation or a basis theorem.

The track construction at lines 1027--1046 is typed coordinatewise.  Given `\(\bar A\in\mathcal P(T)^n\)`, `\(v_{\bar A}(x)\in\{0,1\}^n\)` records exactly the `\(n\)` characteristic values at `\(x\)`.  Conversely each full-root `\(\{0,1\}^n\)`-valuation uniquely determines the `\(n\)` subsets by its coordinates.  Hence `\(\tau\)` really is the asserted bijection, and the displayed Theorem 1.7 equivalence has matching domains on both sides.

The principal formula at lines 1048--1065 has a finite list of words `\(w_j\)`, membership or nonmembership signs, and one node witness `\(x\)`.  Its truth is determined by a finite initial subtree large enough to include every `\(xw_j\)`.  Section 3.10's finite-tree construction supplies that local language, Lemma 3.12 lifts it, Boolean connectives use the stated closures, existential set quantification removes one bit coordinate, and universal set quantification is obtained by complementing around projection.  These are separate construction steps, as on Rabin printed pp. 7--9 and 30--31.

The handbook-owned example at lines 1067--1077 is correct.  For `\(P(A,B)=\exists x(x\in A\land r_0(x)\in B)\)`, the two coordinate bits at `\(x\)` and `\(x0\)` give precisely the two conjuncts.  A finite full-branching initial tree may be chosen with both nodes outside its frontier, so both are labelled.  The example does not claim to reproduce a Rabin transition table and makes no additional logical assumption.

For the converse at lines 1079--1091, choose enough monadic bit tracks to code the finite state set after the one-start normalization.  The root code is fixed to the initial state.  At a node whose code is a legal state, the transition clause forces both child codes to be legal successor states; induction from the root therefore excludes stray bit codes without requiring a separate global legality axiom.  The path variable `\(C\)` is universally quantified, while the run-code tracks are existentially quantified, so the prefix `\(\exists B_1\cdots\exists B_m\,\forall C\)` and the claimed set-quantifier-free matrix reproduce Theorem 1.10 on Rabin printed pp. 9--10.

Finally, the closed-sentence argument at lines 1093--1098 is exactly a nonemptiness reduction.  Writing the sentence as `\(\exists A_1F(A_1)\)`, Theorem 1.7 gives an automaton for the satisfying assignments to `\(F\)`, and the sentence is true iff that language is nonempty.  Theorem 1.6 decides that question.  Nothing in the implication requires a regular-tree witness or a basis theorem.

### 2. Theorem 3.1 product and infinite-occurrence indexing

At lines 1102--1139, write the second-coordinate run along a branch as `\(s_0,s_1,\ldots\)`.  With the deterministic Muller word automaton `\(\langle U,K,u_0,H\rangle\)`, define `\(q_0=u_0\)` and `\(q_{n+1}=K(q_n,s_n)\)`.  The tree product begins at `\((q_0,s_0)\)` and sends both children of `\((q_n,s_n)\)` to first coordinate `\(q_{n+1}\)`, with their second coordinates selected from `\(M(s_n,a)\)`.  Thus one global product run contains, on every branch, exactly the unique deterministic word-automaton history for the branch's tree-state word.  Determinism also ensures that branches sharing a prefix share the same first-coordinate history.

The product acceptance family is correctly typed as
`\(\{C\subseteq U\times S:p_1(C)\in H\}\)`.
Because both state sets are finite,
`\(p_1(\operatorname{In}((q_n,s_n)_n))=\operatorname{In}((q_n)_n)\)`:
if a first-coordinate state occurs infinitely often, at least one of its finitely many second-coordinate partners occurs infinitely often; the converse is immediate.  Depending on the convention for whether the word automaton records the initial state before or after the first input, the displayed product shifts the word-state sequence by one finite position.  Deleting or adding finitely many positions cannot change its infinitely recurring set.  The construction and its use of McNaughton's external deterministic-word result therefore prove exactly the branch-language claim of Rabin printed pp. 17--19.

### 3. Ordinary versus dual semantics and the zero-length case

The definitions at lines 1143--1188 preserve the relevant quantifier reversal.  For positive length `\(k\)`, a path map has type `\(\Omega=((L_i,U_i))_{1\le i\le k}\)` iff some pair has an infinitely recurring state in `\(U_i\)` and none in `\(L_i\)`.  The additional `\(\Omega\)`-empty condition concerns the whole range avoiding one lower set and is not silently substituted for type.  Dual acceptance is
`\(\forall r\,[r\text{ rooted at }s\Rightarrow\exists\pi\,r|\pi\in[\Omega]]\)`.
Because the transition table need not admit a run rooted at `\(s\)`, this implication is correctly allowed to be vacuously true.  This is the complement-side `\(\forall r\,\exists\pi\)` construction of Definitions 3.5--3.6 and Lemma 3.6 on Rabin printed pp. 24--26, not ordinary Muller acceptance.

I separately derived the omitted zero-length branch at lines 1190--1213.  Lemma 3.6 enumerates the nonempty subsets of `\(S\)` that are not in `\(F\)`.  That enumeration has length zero exactly when every nonempty possible infinitely-recurring set is designated.  Since a map from an infinite path into a finite nonempty state set has a nonempty infinitely-recurring set, ordinary acceptance in that situation is equivalent to existence of a rooted run.  Its complement is therefore precisely the absence of a rooted run.

For the empty pair sequence no path map satisfies its existential pair clause, so `\([\langle\rangle]=\varnothing\)` and dual acceptance holds exactly when there is no rooted run.  For `\(\Omega^\dagger=((S,S))\)`, every infinite path map has a nonempty infinitely-recurring set contained in `\(S\)`.  Such a set cannot simultaneously meet `\(S\)` and avoid `\(S\)`, so `\([\Omega^\dagger]=\varnothing\)` as well.  Therefore
`\(D(\mathfrak A_0,\Omega^\dagger,s)=D(\mathfrak A_0,\langle\rangle,s)\)`
for every current table and root state.  The replacement is an exact one-pair normalization into the source's positive-length induction, not a changed acceptance condition.

### 4. Complementation architecture, well-foundedness, and pair lengths

At lines 1215--1257 and 1296--1303, the manuscript retains the finite-state content that a generic reference to transfinite induction would lose.  Marked-tree obligations activate local copies; simultaneous runs keep those copies coherent; equal local automaton/state copies may be merged because their remaining obligations are identical; and Theorem 3.1 checks the residual path language.  These are necessary to turn the local obligation system into one finite tree automaton, as in Rabin printed pp. 19--24.

The mapping `\(h\mapsto H_h\)` is well founded exactly when it admits no infinite chain `\(h_{m+1}\in H_{h_m}\)`.  The ordinal decomposition assigns every member of `\(H_h\)` to a strictly lower stratum than `\(h\)`, which proves that descending obligation chains stop.  The transfinite induction is correctly localized to Lemma 3.3 and the converse construction in Lemma 3.11; it does not replace the marked-tree or finite-state constructions.

The pair-sequence bookkeeping is also sound.  Lemma 3.7 preserves the current length.  Lemma 3.8 preserves the length while making the final lower set empty.  Lemmas 3.9--3.10 then expose a problem for the shorter sequence `\(\Omega_{k-1}\)`.  Lemma 3.11 handles an arbitrary sequence through well-founded deferrals before the same-length last-empty reduction.  After the explicit zero-length normalization, the proof genuinely has two different half-steps: arbitrary length `\(k\)` to last-lower-set-empty length `\(k\)`, then that case to length `\(k-1\)`.  No circular induction on `\(k\)` or unproved collapse of the arbitrary case occurs.

### 5. Finite trees, frontier typing, and the three finite-tree roles

The exact Section 3.10 object appears at frozen lines 1259--1294, controlled by Rabin printed pp. 30--32.  A finite tree is a finite predecessor-closed `\(E\subseteq T\)`.  Its frontier is
`\(\operatorname{Ft}(E)=\{x\in E:x0\notin E\land x1\notin E\}\)`.
The separately stated frontiered condition requires both successors for every node outside that frontier.  This is a property of `\(E\)`, and it is not redundant with predecessor closure: a predecessor-closed set can contain exactly one child of a node.  The later finite automaton and compactness constructions need the stronger full-branching property.  A finite-tree valuation is correctly restricted to `\(E\setminus\operatorname{Ft}(E)\)`.

The finite-tree automaton has the tuple `\(\langle S,M,s_0,f\rangle\)`, with `\(f\notin S\)` and
`\(M:S\times\Sigma\to\mathcal P((S\times S)\cup\{(f,f)\})\)`.
The only permitted frontier pair is `\((f,f)\)`, and `\(f\)` is a distinguished external frontier value rather than an ordinary state.  Thus the transition codomain, the root state, and frontier values are all correctly separated.

The three subsequent results are not conflated.  Lemma 3.12 lifts an automaton-definable finite initial witness language to infinite valued trees, and Corollary 3.13 closes the principal-formula gap.  Lemma 3.14 is the compactness/König step converting a universal infinite-run hitting condition into a finite set of obligations; Corollary 3.15 automatonizes that finite condition for the complementation base.  Section 3.12 later reuses finite witnesses in the emptiness decision.  The weak monadic theory invoked to decide the finite witness statement remains an external base theorem; none of these facts turns the infinite input tree finite or turns full `\(S2S\)` into weak monadic logic.

### 6. Emptiness, restricted tables, both repaired empty branches, and termination

The reduction at frozen lines 1305--1333 is exact.  After one-start normalization, erase the alphabet by setting
`\(M^\bullet(s,\bullet)=\bigcup_{a\in\Sigma}M(s,a)\)`.
Given an original labelled run, erasing its labels produces a run of the one-letter table.  Conversely, at each node of a one-letter run its selected transition belongs to `\(M(s,a)\)` for at least one `\(a\in\Sigma\)`; choosing such a label nodewise recovers an original valuation with the same run.  Hence original nonemptiness is equivalent to acceptance of the unique one-letter full tree.

Theorem 1.5 first constructs an ordinary automaton `\(\mathfrak C\)` for the complement of that one-tree language.  Applying Lemma 3.6 to `\(\mathfrak C\)` yields a dual language equal to the complement of `\(T(\mathfrak C)\)`, namely the original one-tree language.  Original emptiness is therefore exactly the membership question for one specified tree, current finite transition table, current root state, and current pair sequence.  This projection/complement/dual route is Rabin's printed Section 3.12 route on pp. 32--34; it introduces no regular-tree basis theorem.

Definition 3.7 is represented correctly at lines 1343--1351.  For `\(R'\subseteq R\)`, the restricted table keeps `\(R\)` as its formal state set and sets `\(N_{R'}(s)=N(s)\cap(R'\times R')\)`.  Consequently the children of the root and every later state lie in `\(R'\)`, while the root itself is still permitted to be the queried state `\(s\in R\setminus R'\)`.  Replacing the formal state set by `\(R'\)` would make the later calls from states in `\(H\)` undefined; the manuscript does not make that error.

I re-derived the last-empty-lower-set split at lines 1361--1371.  For `\(L_k=\varnothing\)` and `\(k>1\)`, an exhaustive split must range over every `\(H\subseteq U_k\)`.  If `\(H=\varnothing\)`, no new state is required to recur for the final pair, and the condition is exactly the direct current-table dual question for `\(\Omega_{k-1}\)`.  If `\(H\ne\varnothing\)`, forbidding `\(H\)` below the root through Definition 3.7 and asking the shorter dual question from each state in `\(H\cup\{s_0\}\)` expresses that every run either supplies the shorter type or reaches the selected final recurring set.  Thus the empty and nonempty branches are semantically different and jointly exhaustive.  Rabin printed p. 34 states nonempty `\(H\)` in display (3.5) but then ranges over the power set; the manuscript both identifies this source omission and supplies the minimum mathematical completion.

The base at lines 1373--1389 likewise must permit `\(m=0\)` and `\(U_0=\varnothing\)`.  When `\(m>0\)`, the finite frontiered witnesses `\(E_0,\ldots,E_m\)` express the source's universal hitting condition from the listed states.  When `\(m=0\)`, that universal condition says that the sole `\(E_0\)` has no compatible run rooted at `\(s_0\)`, because no run can hit the empty set below the root.  Such a finite obstruction exists iff there is no infinite rooted run: one direction is immediate, and the converse follows by applying König's Infinity Lemma to the finitely branching tree of compatible finite partial runs.  This is exactly dual acceptance's vacuous no-run branch.  Rabin printed p. 34's `nonempty` restriction omits it; the handbook correctly labels and supplies the edge completion while preserving the printed nonempty branch and the Doner/Thatcher--Wright weak-theory dependency.

The arbitrary half-step terminates effectively because its `\(H_0,H_1,\ldots\)` are pairwise disjoint subsets of the current finite state set.  At most `\(|R|\)` of them can be nonempty.  The last-empty half-step strictly lowers positive `\(k\)`, and the repaired `\(k=1\)` branch is decided by a finite-tree sentence.  The zero-length normalization supplies a positive start when Lemma 3.6 returns no pair.  Hence the recursive decision has a base, each reduction has a decreasing finite measure, and all queries retain their current table, state set, root state, and pair sequence.

### 7. Effectiveness, complexity, applications, and source boundaries

Rabin printed pp. 1 and 4 make the historical elementary-recursive claim.  Meyer printed p. 478 states a non-elementary tower lower bound, and printed p. 479 explicitly includes “the theory of two successors and prefix” with the Meyer--Stockmeyer attribution.  The latter is a literal sublanguage of the displayed binary structure: it uses the same two successor functions and initial-segment relation while omitting the lexicographic relation.  Any elementary-recursive worst-case decision bound for the full displayed language would restrict to one for this sublanguage, contradicting the lower bound.  The manuscript at lines 941--963 and 1392--1400 therefore correctly rejects the historical complexity bound while retaining the constructive reductions, decidability, and effectiveness.  It neither turns a lower bound into undecidability nor promises an unsupported upper bound.

The application synopsis at lines 1402--1421 has the correct class-level strengths from Rabin printed pp. 10--17: countable linear orders, the weak theory of all linear orders, countable well-orders, countable unary-function structures and the corresponding weak all-structure result, the stated Cantor-space and interval languages, countable Boolean algebras with ideal quantification and arbitrary Boolean algebras with distinguished ideals, and the `\(F_\sigma\)` Gale--Stewart determinacy encoding.  It does not silently strengthen an individual-structure result into a class theory or exchange full and weak quantification.

Lines 1423--1437 accurately declare what is reconstructed and what remains in Rabin's complete article.  McNaughton's deterministic-word theorem is identified as an external ingredient in Theorem 3.1.  Thomas's later presentation, including its regular-tree basis route, is expressly separated from Rabin's Section 3.12 argument.  The relevant frozen bibliography records identify Rabin, Meyer, Thatcher--Wright, McNaughton, and Thomas consistently with those uses.  No later proof route is laundered into the 1969 source.

## Display, implication, and proof-obligation audit

I checked every mathematical display and every surrounding quantifier, case split, implication, equivalence, and claimed proof dependency in frozen manuscript lines 908--1437.  The following register records the controlling checks; none generated a finding.

| Frozen manuscript location | Controlling printed source | Check and result |
|---|---|---|
| lines 914--963 | Rabin pp. 1, 3--5; Meyer pp. 478--479 | `\(\Lambda\)`, word operations, both orders, predecessor, `\(0<n\le\omega\)`, finite/omega qualification, and complexity correction are exact. |
| lines 965--1014 | Rabin pp. 5--7 | Arbitrary roots, paths, table/automaton tuples, `\(\operatorname{In}\)`, run condition, `\(\exists r\forall\pi\)`, and `\(F\subseteq\mathcal P(S)\)` are well typed and equivalent to the source definitions. |
| lines 1016--1023 | Rabin pp. 6--7 | Theorems 1.3--1.6 are used with their distinct closure, projection/converse-coordinate, complement, and emptiness roles. |
| lines 1027--1065 | Rabin pp. 7--9, 30--31 | Track map is a bijection; formula equivalence, principal formulas, finite lift, Boolean operations, projection, and complement are each justified. |
| lines 1067--1077 | Rabin pp. 7--9, 30--31 | Worked two-track witness is a correct handbook instance and is not misattributed as a printed table. |
| lines 1079--1098 | Rabin pp. 9--10 | Run encoding, one-start normalization, `\(\exists\bar B\forall C\)`, converse equivalence, and closed-sentence nonemptiness reduction are exact; no basis step is inserted. |
| lines 1102--1139 | Rabin pp. 17--19; McNaughton dependency | Word transition type, product state and initial set, child update, designated family, shared deterministic histories, and harmless finite index shift are correct. |
| lines 1143--1188 | Rabin pp. 24--26 | Type/type-empty clauses and all set intersections/ranges are typed; dual `\(\forall r\exists\pi\)` and no-run vacuity are preserved. |
| lines 1190--1213 | Rabin p. 25 (Lemma 3.6) and the positive-length development on pp. 26--32 | Empty enumeration is possible; its dual language is no-run; `\(((S,S))\)` has the same empty path language and is an exact positive-length normalization. |
| lines 1215--1257, 1296--1303 | Rabin pp. 19--32 | Marked trees, simultaneous runs, same-state merging, path check, well-founded strata, transfinite loci, Lemmas 3.7--3.11, and both half-steps retain their distinct proof obligations and lengths. |
| lines 1259--1294 | Rabin pp. 30--32 | Finite/predecessor-closed and frontiered/full-branching conditions are distinguished; valuation domain, external `\(f\)`, transition codomain, lift, complement compactness, and base roles are exact. |
| lines 1305--1333 | Rabin pp. 32--34 | Alphabet erasure is bidirectionally valid; complement then Lemma 3.6 yields the original one-tree language; emptiness is the resulting dual membership question. |
| lines 1335--1351 | Rabin pp. 32--33 | Each recursive question supplies its current table and sequence; Definition 3.7 retains formal `\(R\)` and constrains only states strictly below the root. |
| lines 1353--1371 | Rabin pp. 33--34 | Finite disjoint-stratum computation terminates; `\(H=\varnothing\)` is the direct shorter question; every nonempty `\(H\)` uses the correctly restricted table; the two branches are exhaustive. |
| lines 1373--1400 | Rabin p. 34 | `\(m\ge0\)`, empty `\(U_0\)`, sole no-run witness `\(E_0\)`, König equivalence, nonempty source branch, weak-theory dependency, and effectiveness/complexity separation are correct. |
| lines 1402--1437 | Rabin pp. 10--17 and 35; Thomas as later source | Application strengths, reconstruction boundary, omitted-detail disclosure, later route, and external dependency attribution are all correctly bounded. |

## Mandatory-invariant register

Every invariant assigned to this seat is satisfied:

| Invariant | Status | Decisive frozen manuscript/source locus |
|---|---|---|
| R01 | satisfied | lines 914--917; Rabin pp. 4--5 |
| R02 | satisfied | lines 918--963; Rabin pp. 4--5 |
| R03 | satisfied | lines 965--1014; Rabin pp. 5--7 |
| R04 | satisfied | lines 1007--1011 and 1141--1188; Rabin pp. 6, 24--26 |
| R05 | satisfied | lines 1016--1023 and 1093--1098; Rabin pp. 6--10 |
| R06 | satisfied | lines 1027--1065; Rabin pp. 7--9, 30--31 |
| R07 | satisfied | lines 1067--1077; Rabin pp. 7--9, 30--31 |
| R08 | satisfied | lines 1079--1098; Rabin pp. 9--10 |
| R09 | satisfied | lines 1100--1139; Rabin pp. 17--19 |
| R10 | satisfied | lines 1141--1188; Rabin pp. 24--26 |
| R11 | satisfied | lines 1215--1225; Rabin pp. 19--24 |
| R12 | satisfied | lines 1227--1233 and 1296--1303; Rabin pp. 19--32 |
| R13 | satisfied | lines 1235--1256 and 1335--1390; Rabin pp. 26--34 |
| R14 | satisfied | lines 1259--1283; Rabin p. 30 |
| R15 | satisfied | lines 1284--1294 and 1397--1400; Rabin pp. 30--32, 34 |
| R16 | satisfied | lines 1305--1333; Rabin pp. 32--34 |
| R17 | satisfied | lines 1335--1351; Rabin pp. 32--33 |
| R18 | satisfied | lines 1353--1371; Rabin pp. 33--34 |
| R19 | satisfied | lines 1373--1389; Rabin p. 34 |
| R20 | satisfied | lines 941--963 and 1392--1400; Rabin pp. 1, 4; Meyer pp. 478--479 |
| R21 | satisfied | lines 1402--1421; Rabin pp. 10--17 |
| R22 | satisfied | lines 910--912, 1114--1139, and 1423--1437; Rabin pp. 17--19, 35 |
| R23 | satisfied | lines 908--1437; Rabin printed pp. 1--35 and Meyer printed pp. 477--482 |
| R26 | satisfied | editorial order subscripts at lines 918--927, `\(\operatorname{pd}\)` at 932--940, `\(\tau\)` at 1027--1046, marked trees at 1218--1225, well-founded mapping at 1227--1233, `frontiered` at 1259--1271, `\(M^\bullet\)` at 1307--1322, and all later uses; controlling Rabin pp. 4--34 |
| R27 | satisfied | ordinary/dual split at lines 996--1013 and 1141--1213; finite/weak/full split at 1259--1294 and 1392--1400; effectivity/complexity and source/later-route split at 941--963 and 1423--1437 |
| R28 | satisfied | acceptance is expressly limited in this report to frozen `N-c-014.d` manuscript content |
| R29 | satisfied | lines 1190--1213 and 1340--1342; Rabin pp. 25--34 |

## Finding register and limitations

No findings.  Accordingly there is no finding identifier, severity, defective frozen manuscript location, controlling printed page, or repair to register.  The two defects actually present in Rabin's printed p. 34 argument—the omitted `\(H=\varnothing\)` branch and omitted `\(U_0=\varnothing\)`/`\(m=0\)` base branch—are explicitly identified as source defects in the frozen manuscript, are repaired by the minimum sufficient cases, and do not survive as manuscript defects.  Likewise, the potentially zero-length Lemma 3.6 enumeration is explicitly and exactly normalized before the positive-length induction.

This is a manuscript-content judgment based on the hash-pinned textual objects and complete original-detail source renders.  It supplies no evidence about compilation, TeX integrity, rendered layout, cross-part integration beyond the frozen records, human acceptance, or the book as a whole.

VERDICT: ACCEPT
