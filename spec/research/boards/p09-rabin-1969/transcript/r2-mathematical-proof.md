# Round 2 mathematical and proof-correctness review: Rabin 1969

Date: 2026-08-23

Seat: mathematical and proof correctness

Artifact: N-c-014.d, Michael O. Rabin (1969), together with the later Albert R. Meyer complexity correction

## Outcome

I found no blocker, must-fix, should-fix, consider, discard, or unresolved-user finding in the frozen Round 2 snapshot. The reconstruction is mathematically coherent at the source's stated strength; its three handbook-owned edge completions are necessary and sufficient; and it keeps existence, effectivity, complexity, weak/full logic, finite/infinite trees, ordinary/dual acceptance, and Rabin/Thomas proof routes distinct.

## Frozen-object identity

I recomputed SHA-256 for all six frozen objects before substantive review. Every observed digest matched the Round 2 charter exactly.

| Frozen object | Expected SHA-256 | Independently observed SHA-256 | Result |
|---|---|---|---|
| tmp/pdfs/p09-rabin-1969/rabin-1969.pdf | CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3 | CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3 | match |
| tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf | 9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D | 9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D | match |
| handbook/parts/p09/presentations/n-c-014.tex | 370C563CA4019E1EF266013ADBC910C231D2A07064EE91DC3E7BCCDD32BF3B5E | 370C563CA4019E1EF266013ADBC910C231D2A07064EE91DC3E7BCCDD32BF3B5E | match |
| handbook/bib/handbook.bib | 408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0 | 408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0 | match |
| spec/research/p09-rabin-1969-source-note.md | D2B3C0293D4012A262726708F082E0B6F7C4A0CE33D623821687F2CB22B97192 | D2B3C0293D4012A262726708F082E0B6F7C4A0CE33D623821687F2CB22B97192 | match |
| spec/research/p09-source-presentations-lot2-3.md | 02C9C6A01DBCC5F876781EE8C13E7235D26C04EB61DD19A811DC8649C6DECF33 | 02C9C6A01DBCC5F876781EE8C13E7235D26C04EB61DD19A811DC8649C6DECF33 | match |

## Source-page inspection

I visually inspected every source page at original detail.

- Rabin: rendered physical page 1, the custody-and-use cover, and rendered physical pages 2--36, corresponding one-to-one to every printed article page 1--35.
- Meyer: rendered physical PDF pages 485--490, corresponding one-to-one to printed article pages 477--482.
- The Rabin and Meyer PDFs named in the identity table controlled. The renders were used only to inspect the controlling PDF pages at original detail. No OCR or layout extraction controlled any formula, symbol, wording, or pagination judgment.

The relevant visual checkpoints included Rabin's main-result and historical complexity claim on printed p. 1; Definition 1.1 on pp. 3--5; ordinary tree automata and acceptance on pp. 5--7; the formula translations and sentence reduction on pp. 7--10; all Chapter II application pages 10--17; Theorem 3.1 on pp. 17--19; every page of the marked-tree and well-founded construction on pp. 19--24; every dual-language and two-half-step page on pp. 24--32; the finite-tree machinery on pp. 30--32; Definition 3.7 and the emptiness reduction on pp. 32--34; the p. 34 nonempty-\(H\) and nonempty-\(U_0\) clauses; and the final reference page. For Meyer I inspected the theorem and tower display on printed p. 478, the complete list and the Meyer--Stockmeyer attribution on p. 479, and the remaining argument and reference pages 480--482.

## Evidence boundary and whole-snapshot coverage

I read only the charter, the six frozen Round 2 objects, and the two authorized original-detail render sets. I did not read any Round 1 report, any other Round 2 report, the ledger, the chair transcript, any other board transcript, the staging draft, or the layout extraction as evidence. I did not contact another reviewer.

The four frozen text objects were read in full, not sampled:

- all 1,428 lines of handbook/parts/p09/presentations/n-c-014.tex, including the entire Rabin reconstruction at lines 908--1428 and its adjacent presentation boundaries;
- all 6,272 lines of handbook/bib/handbook.bib;
- all 614 lines of spec/research/p09-rabin-1969-source-note.md; and
- all 915 lines of spec/research/p09-source-presentations-lot2-3.md, including the N-c-014.c--e boundaries and the Rabin record at lines 660--672.

The detailed note and compact record are treated as authored claim sets, not substitutes for the printed sources. I ran no test, automated checker, repository script, TeX command, interim build, or handbook-PDF inspection.

## Independent mathematical reconstruction

### 1. Successor structures, ordinary acceptance, and logical coding

The reader's lines 914--963 preserve \(\Lambda\), define the two editorially disambiguated orders, type every successor, state Definition 1.1 for \(0<n\leq\omega\), and retain the exact finite-\(n\) versus \(T_\omega\) qualification. This agrees with Rabin printed pp. 3--5. No \(\epsilon\) substitution or binary-only distortion is present.

At reader lines 965--1014, a valued tree may be rooted at any \(x\), the transition table is \(\langle S,M\rangle\), and the ordinary automaton is the distinct tuple \(\langle S,M,S_0,F\rangle\), with \(F\subseteq\mathcal P(S)\). If \(\operatorname{Run}(r)\) says that \(r\) satisfies the local transition table, ordinary acceptance is
\[
 \exists r\left(
   \operatorname{Run}(r)\land r(x)\in S_0
   \land
   \forall\pi\,
      [\operatorname{Path}_x(\pi)\Rightarrow
       \operatorname{In}(r\!\upharpoonright\!\pi)\in F]
 \right).
\]
Thus its quantifier polarity is genuinely \(\exists r\,\forall\pi\). The finite pair list used later is not an ordinary acceptance component.

The bit-track map at lines 1026--1045 is bijective: each tuple of sets determines one coordinatewise characteristic labeling, and each \(\{0,1\}^n\)-labeling recovers the tuple by taking the inverse image of 1 in each coordinate. Projection of a track is therefore exactly existential set quantification. Boolean closure and complementation give the remaining propositional and universal-set steps. The principal-formula form at lines 1047--1064 has the exact finite successor-word shape needed for the finite-tree lift.

The worked formula at lines 1066--1076 is correct. Its two requirements concern the label at \(x\) and at \(x0\). A finite predecessor-closed frontiered tree can make both nodes nonfrontier nodes by including the required siblings and children, so both labels lie in the finite valuation domain. The text properly identifies this as a handbook calculation, not a Rabin-printed transition table.

For Theorem 1.10, finitely many monadic tracks encode a state at every node. After the one-initial-state normalization, the local formula enforces the root state and every parent/child move; the universal path-set track \(C\) checks the Muller family. Hence the set-quantifier prefix at lines 1078--1090 is exactly \(\exists\bar B\,\forall C\), with the run tracks existential and the tested path universal.

The sentence reduction at lines 1092--1097 is exact. For any closed \(G\), one may take a dummy monadic variable \(A_1\) and \(F(A_1)=G\); the monadic set domain is nonempty, so \(G\) is equivalent to \(\exists A_1F(A_1)\). Theorem 1.7 then gives an automaton whose language is nonempty exactly when \(G\) is true, and Theorem 1.6 decides that question. No basis theorem is logically needed or textually inserted.

### 2. Theorem 3.1 product

Let a branch have tree-table states \(s_n=r(x_n)\). Define the deterministic word states by
\[
 u_0\text{ initial},\qquad u_{n+1}=K(u_n,s_n).
\]
The product transition at reader lines 1120--1126 sends a node in state \((u_n,s_n)\) to children whose first coordinate is \(K(u_n,s_n)=u_{n+1}\) and whose second coordinates are an allowed pair from \(M(s_n,a)\). The two children necessarily share the word-state history up to their split, while determinism gives one continuation on each later branch. The initial set \(\{u_0\}\times S\) is therefore correct.

For the product run \(q_n=(u_n,s_n)\),
\[
 p_1(\operatorname{In}(q))
   =\operatorname{In}(u).
\]
The forward inclusion is immediate. Conversely, if \(u\) occurs infinitely often, finiteness of \(S\) forces some pair \((u,s)\) to occur infinitely often. Therefore the designated family
\[
 \{C\subseteq U\times S:p_1(C)\in H\}
\]
accepts exactly when the deterministic word run has Muller set in \(H\). If one chooses the alternative convention in which a word-run state is displayed after consuming the current input symbol, the two word-state sequences differ only by a one-position shift, which cannot change an infinitely-occurring-state set. No finite-prefix property is claimed here. The construction at lines 1099--1138 is consequently well typed and semantically exact.

### 3. Dual semantics and the zero-length case

At lines 1142--1165, \(\phi\in[\Omega]\) means that one indexed pair has an upper set met infinitely often and a lower set avoided infinitely often; \(\phi\in[\Omega,e]\) adds an entire-range avoidance condition. These are different conditions, and the reader keeps them different.

For a named root state \(s\), dual acceptance at lines 1166--1187 is
\[
 \forall r\,
   [\operatorname{Run}_s(r)\Rightarrow
      \exists\pi\;\operatorname{Type}_\Omega(r\!\upharpoonright\!\pi)].
\]
Its polarity is \(\forall r\,\exists\pi\). If there is no rooted run, the universal implication is true. That vacuity is not optional: it is part of Definition 3.6 and is used by the empty branches in the emptiness argument.

For the empty list, the existential choice of a pair index has an empty domain, so
\[
 [\langle\rangle]=\varnothing.
\]
It follows directly that
\[
 D(\mathfrak A_0,\langle\rangle,s)
 \iff
 \forall r\,[\operatorname{Run}_s(r)\Rightarrow\bot]
 \iff
 \neg\exists r\,\operatorname{Run}_s(r).
\]

Now take the reader's \(\Omega^\dagger=((S,S))\). The named state \(s\in S\) makes \(S\) nonempty, and every infinite path map into finite \(S\) has a nonempty infinitely recurring set. Its sole type clause would require
\[
 \operatorname{In}(\phi)\cap S\ne\varnothing
 \quad\text{and}\quad
 \operatorname{In}(\phi)\cap S=\varnothing
\]
simultaneously. Thus \([\Omega^\dagger]=\varnothing\), and the same calculation gives
\[
 D(\mathfrak A_0,\Omega^\dagger,s)
 =
 D(\mathfrak A_0,\langle\rangle,s).
\]
The normalization at lines 1189--1212 is therefore an exact representation of the empty path language inside the positive-length induction. It neither changes Definition 3.6 nor introduces a third acceptance convention.

There is also a direct complement check. Lemma 3.6 enumerates the nonempty subsets of \(S\) outside \(F\). If this enumeration is empty, then \(F\) contains every possible infinite-occurrence set. Every existing run is consequently ordinary-accepting on every branch, and the complement consists exactly of trees with no rooted run. That is precisely the dual language of both the empty list and \(\Omega^\dagger\).

### 4. Marked obligations, well-foundedness, and the two half-steps

The simultaneous-run mechanism at lines 1217--1224 is finite-state for the stated reason: at one node, copies of the same finite local automaton that reach the same state have identical future obligations and can be merged. Theorem 3.1 then absorbs the residual path condition. The reader does not replace this construction by an untyped appeal to transfinite induction.

For Definition 3.2, put \(g\prec h\) exactly when \(g\in H_h\). If there is no infinite \(\prec\)-descent, well-founded recursion assigns
\[
 \rho(h)=\sup\{\rho(g)+1:g\in H_h\},
\]
so every member of \(H_h\) lies in a strictly lower ordinal stratum. Conversely, an infinite descent would produce an impossible infinite strictly descending sequence of ordinals. This verifies the equivalence summarized at lines 1226--1232 and the transfinite loci stated at lines 1287--1294.

The lengths in the two half-steps remain distinct and correct:

1. Lemma 3.7 preserves the current pair-list length.
2. Lemma 3.8 also preserves that length while arranging an empty final lower set.
3. With \(L_k=\varnothing\), Lemmas 3.9--3.10 expose questions for the shorter list \(\Omega_{k-1}\).
4. Lemma 3.11 handles arbitrary length \(k\) through a well-founded deferral family, after which Lemma 3.8 supplies the last-empty case.
5. The positive-length induction first proves the last-empty half-step from \(k-1\), then proves the arbitrary half-step at \(k\).

The zero-list normalization is what makes this induction genuinely exhaustive. The reader's lines 1234--1256 neither collapse the two half-steps nor silently assume \(k>0\).

### 5. Finite-tree machinery

Reader lines 1258--1275 correctly define the source's finite tree as finite and predecessor closed, with every nonfrontier node having both binary successors. The valuation domain is \(E\setminus\operatorname{Ft}(E)\), not all of \(E\). The frontier state satisfies \(f\notin S\), and the transition codomain
\[
 \mathcal P((S\times S)\cup\{(f,f)\})
\]
permits exactly ordinary state pairs or the two-frontier marker pair. The source term “frontiered” is used only after this exact property is supplied; no undefined replacement term is introduced.

The three finite-tree roles at lines 1276--1285 remain separate:

- Lemma 3.12 lifts an accepted finite initial witness to an infinite-tree language;
- Corollary 3.13 supplies the deferred principal-formula case;
- Lemma 3.14 extracts a finite obstruction/hitting set by König compactness, with Corollary 3.15 supplying the complement base.

Nothing in those uses changes the infinite input tree into a finite one or changes full monadic set quantification into weak set quantification.

### 6. One-letter reduction and recursive emptiness

At lines 1298--1313, the one-letter transition table takes the union over the old alphabet. Restricting any old run to the one-letter label gives a run of the union table. Conversely, for every selected transition in the union table, one can choose a witnessing old letter (for example, the least one in a fixed finite ordering) independently at that node, thereby recovering a valued old-alphabet tree. Hence old nonemptiness is exactly acceptance of the unique one-letter full tree.

Complementing that one-tree language and then applying Lemma 3.6 to the complement returns a dual presentation of the original language, as shown at lines 1314--1324. This is a double-complement calculation, not an invocation of a regular-tree basis theorem.

Each recursive question at lines 1326--1333 explicitly supplies a current finite table, a current state set, a current state, and a current pair list. If the list is empty it is normalized first, so the recursion starts at \(k\geq1\).

For Definition 3.7, the restricted transition
\[
 N_{R'}(s)=N(s)\cap(R'\times R')
\]
retains \(R\) as the formal state set. The transition out of the root forces both children into \(R'\); induction down the tree forces every strict descendant into \(R'\). Nothing forces the root state itself into \(R'\). Conversely, any old run whose strict descendants lie in \(R'\) uses only restricted transitions. Reader lines 1334--1342 therefore state the exact boundary.

In the arbitrary half-step, the finite-state ordinal construction can add only disjoint nonempty strata of states. It must stop after at most \(|R|\) such additions. The claim at lines 1344--1350 is a finite termination argument, not an assumption that the underlying source ordinals are finite.

### 7. The required \(H=\varnothing\) branch

When \(L_k=\varnothing\), a path of type \(\Omega\) either already has a type from \(\Omega_{k-1}\) or realizes the last pair by recurring in \(U_k\). The source's printed p. 34 nonempty-\(H\) formulation misses the case in which every run already supplies the shorter type. Setting \(H=\varnothing\) removes the “reach \(H\) below the root” disjunct and leaves exactly
\[
 T\in D(\langle R,N\rangle,\Omega_{k-1},s_0).
\]
For nonempty \(H\), restricting strict descendants to \(R\setminus H\) converts the failure to revisit \(H\) into the shorter dual questions for the states in \(H\cup\{s_0\}\). This validates the split at lines 1352--1362.

As an independent necessity check, take
\[
\begin{aligned}
 R&=\{s,a,u,b\},\\
 N(s)&=\{(a,a)\},\quad N(a)=\{(a,a)\},\\
 N(u)&=\{(b,b)\},\quad N(b)=\{(b,b)\},\\
 \Omega&=((\varnothing,\{a\}),(\varnothing,\{u\})).
\end{aligned}
\]
The unique run from \(s\) has an \(\Omega_1\)-type path, so the length-two dual question is true. The only nonempty \(H\subseteq U_2=\{u\}\) is \(\{u\}\), but the run rooted at \(u\) immediately remains in \(b\), has no \(\Omega_1\)-type path, and never reaches \(u\) strictly below the root. Thus every nonempty choice fails while \(H=\varnothing\) gives the correct direct shorter question. The handbook-owned branch is necessary, not merely cosmetically more general.

### 8. The \(m=0\), \(U_0=\varnothing\) finite obstruction

In the base \(k=1,\ L_1=\varnothing\), allowing \(m=0\) makes
\[
 U_0=\{s_1,\ldots,s_m\}=\varnothing.
\]
The universal condition for \(E_0\) then says that every finite run rooted at the current \(s_0\) reaches an element of the empty set below the root. This is equivalent to saying that \(E_0\) admits no such run.

The equivalence with the absence of an infinite run is exact. Consider the tree whose level-\(n\) nodes are compatible runs on the complete finite binary tree of depth \(n\), ordered by restriction. It is finitely branching because the state set and transition table are finite. If compatible finite runs exist at every depth, König's Infinity Lemma gives a coherent infinite run. Contrapositively, if no infinite run exists, some finite depth admits no run and supplies \(E_0\). The converse is immediate because every infinite run would restrict to a run on \(E_0\).

The empty branch is independently necessary. For example, take
\[
 R=\{s,u,a\},\qquad
 N(s)=\varnothing,\quad
 N(u)=\{(a,a)\},\quad
 N(a)=\{(a,a)\},
\]
and \(\Omega=((\varnothing,\{u\}))\). Dual acceptance from \(s\) is vacuous because there is no rooted run. The only nonempty candidate \(U_0\subseteq U_1=\{u\}\) is \(\{u\}\), but every run rooted at \(u\) moves to and remains in \(a\), so no finite tree can force a strict-descendant visit to \(u\). With \(U_0=\varnothing\), a finite tree requiring one transition out of \(s\) admits no run and is the needed obstruction. Reader lines 1364--1380 correctly preserve the printed nonempty branch while adding and owning this missing case.

The weak monadic theorem enters only to decide existence of these finite witnesses. It neither weakens the original \(S2S\) input nor turns its infinite tree into a finite one.

### 9. Meyer consequence

Rabin printed p. 1 claims elementary-recursive procedures in Kalmár's sense. Meyer printed p. 478 states a lower bound whose tower height grows with input length, and printed p. 479 explicitly lists “the theory of two successors and prefix,” credited to Meyer and Stockmeyer.

The signature of that listed theory is directly contained in the displayed binary successor structure: \(r_0\), \(r_1\), and the initial-segment/prefix relation are already symbols of \(\mathfrak N_2\); the lexicographic relation can simply go unused. Therefore any elementary-recursive worst-case decision procedure for the displayed \(S2S\) theory would, by restriction to that literal sublanguage, give an elementary-recursive procedure for Meyer's listed problem. The growing-tower lower bound rules that out. The inference at reader lines 952--960 and 1383--1387 is valid.

This consequence changes only the worst-case complexity qualification. It neither supplies an undecidability result nor invalidates Rabin's effective decision construction. The reader correctly retains decidability and effectivity.

## Mandatory-invariant trace

| Invariant | Exact frozen manuscript location | Controlling printed page(s) | Mathematical assessment |
|---|---|---|---|
| R01 | n-c-014.tex 914--917 | Rabin 3--5 | Pass. \(\Lambda\) is retained and explicitly distinguished from editorial \(\epsilon\). |
| R02 | 918--963 | Rabin 3--5, 10--11 | Pass. The full \(0<n\leq\omega\) structure, both orders, finite definability qualification, \(T_\omega\) exception, and interpretation consequence are exact. |
| R03 | 965--1014 | Rabin 5--7 | Pass. Arbitrary roots, distinct tuples, \(F\subseteq\mathcal P(S)\), and \(\exists r\,\forall\pi\) are correct. |
| R04 | 1142--1187 | Rabin 24--26 | Pass. The pair sequence is dual-only, the prefix is \(\forall r\,\exists\pi\), and no-run vacuity is explicit. |
| R05 | 1016--1022 | Rabin 6--10, 32--34 | Pass. Theorems 1.3--1.6 have exactly their closure, complement, and emptiness roles. |
| R06 | 1026--1064 | Rabin 7--9, 30--31 | Pass. The track map is typed and bijective; principal formulas, finite lift, Boolean closure, projection, and complement remain separate steps. |
| R07 | 1066--1076 | Rabin 7--9, 30--31 | Pass. The example is correct and visibly handbook-owned. |
| R08 | 1078--1097 | Rabin 9--10 | Pass. The run tracks, one-start normalization, \(\exists\bar B\,\forall C\) prefix, and sentence-to-nonemptiness reduction are exact; there is no basis insertion. |
| R09 | 1099--1138 | Rabin 17--19 | Pass. The deterministic Muller tuple, transition type, product, initial set, update, and designated projection family are well typed; only infinite-occurrence acceptance makes a possible one-place convention shift harmless. |
| R10 | 1142--1187 | Rabin 24--26 | Pass. Type and type-empty are distinct; the dual reversal and complement role are exact. |
| R11 | 1217--1224 | Rabin 19--24 | Pass. Markers, simultaneous copies, same-state merging, and Theorem 3.1's path check are all retained as finite-state construction steps. |
| R12 | 1226--1232 and 1287--1294 | Rabin 19--24, 29--30 | Pass. No-infinite-descent and lower ordinal strata are equivalent; transfinite induction is placed at Lemmas 3.3 and 3.11 only. |
| R13 | 1234--1256 | Rabin 26--32 | Pass. Lemmas 3.7--3.11 preserve the exact \(k\), last-empty \(k\), and shorter \(k-1\) roles; the two half-steps and positive-\(k\) induction stay distinct. |
| R14 | 1258--1275 | Rabin 30--31 | Pass. Finite, predecessor-closed, frontiered shape; nonfrontier valuation; \(f\notin S\); and transition codomain are exact. |
| R15 | 1276--1285 and 1388--1391 | Rabin 30--34 | Pass. Lemmas 3.12--3.14 retain distinct principal-formula, complement, and compactness roles; weak finite-tree logic is not conflated with the full input theory. |
| R16 | 1296--1324 | Rabin 32--34 | Pass. The alphabet is erased to one letter, that language is complemented, the complement is dualized, and membership is decided. No regular-tree basis theorem appears. |
| R17 | 1326--1342 | Rabin 32--34, especially Definition 3.7 on 33 | Pass. Every recursive datum is bound; the formal state set remains \(R\), strict descendants lie in \(R'\), and the root may be outside \(R'\). |
| R18 | 1344--1362 | Rabin 33--34 | Pass. Finite strata terminate; all \(H\subseteq U_k\) are included; the empty and nonempty branches have the correct shorter-question meanings and ownership. |
| R19 | 1364--1380 | Rabin 30--34, especially 34 | Pass. \(m\geq0\), empty \(U_0\), \(E_0,\ldots,E_m\), the \(m=0\) no-run witness, König equivalence, and external weak-theory dependency are exact. |
| R20 | 952--960 and 1383--1387 | Rabin 1, 4; Meyer 478--479 | Pass. The historical claim is reported but not retained; the direct sublanguage argument validates the later non-elementary correction without weakening decidability. |
| R21 | 1393--1412 | Rabin 10--17 | Pass. Linear orders, unary functions, Cantor/\(F_\sigma\) structures, Boolean algebras/ideals, and the encoded determinacy statement are kept at class-level source strength. |
| R22 | 1414--1428 | Rabin 1--35; Thomas boundary is separately attributed | Pass. The reconstruction/omission boundary is explicit, and neither Thomas's basis route nor McNaughton's external word result is laundered into Rabin. |
| R23 | 908--1428, with principal anchors above | Rabin 1--35; Meyer 477--482 | Pass. Numbering, notation, locators, theorem strength, and attribution are coherent throughout. |
| R24 | source note 1--614; compact record 660--672; bibliography 2290--2299, 2346--2355, 5938--5947, 5973--6002 | Rabin 1--35; Meyer 477--482 | Checked beyond this seat's mandatory set. The four frozen records agree on identity, correction, dependencies, and pending-review status. |
| R25 | source note 28--89 | Rabin custody cover; Meyer public proceedings route | Checked beyond this seat's mandatory set. Access is not inflated into an open-content or republication licence. |
| R26 | representative first uses at 918--940, 1026--1038, 1101--1133, 1142--1165, 1189--1212, 1217--1232, 1258--1273, and 1298--1339 | Rabin 3--34 | Pass. Technical names are source terms or exact eliminable editorial disambiguations; necessity, definition/standing, nonredundancy, and later use are supplied. No hypothetical answer is prematurely named. |
| R27 | 965--1014, 1140--1212, 1258--1294, 1296--1391, 1423--1428 | Rabin 5--34; Meyer 478--479 | Pass. All listed finite/infinite, weak/full, ordinary/dual, existence/effectivity, route, and complexity distinctions survive. |
| R28 | reader 1414--1428; source note 18--26 and 576--614; compact record 672 | Scope/status records rather than one source theorem | Pass. Any acceptance is expressly only an N-c-014.d manuscript-content decision and cannot be read as another completion gate. |
| R29 | 1189--1212 and 1331--1333 | Rabin 24--26, 32--34 | Pass. The zero-length possibility is real, its no-run dual semantics is derived, and \(((S,S))\) is extensionally identical and explicitly handbook-owned. |

## Cross-object and bibliographic consistency

The complete reader, detailed source note, and compact record agree on the ordinary/dual distinction, the empty pair-list normalization, the two p. 34 empty branches, Definition 3.7's root boundary, the weak-theory dependency, the Meyer correction, the Thomas nonconflation boundary, and pending rather than completed review status.

The complete bibliography contains the identities needed by the reconstruction:

- McNaughton1966 at lines 2290--2299: Information and Control 9(5), 521--530, DOI 10.1016/S0019-9958(66)80013-X;
- Thomas1997 at lines 2346--2355: Handbook of Formal Languages, volume 3, 389--455, DOI 10.1007/978-3-642-59126-6_7;
- Meyer1975Complexity at lines 5938--5947: ICM Vancouver 1974, volume 2, 477--482, Canadian Mathematical Congress, 1975, with the official IMU URL;
- Rabin1969 at lines 5973--5982: Transactions of the AMS 141, 1--35, 1969, the AMS DOI, and the inspected research-scan URL; and
- ThatcherWright1968 at lines 5993--6002: Mathematical Systems Theory 2(1), 57--81, DOI 10.1007/BF01691346.

No cross-record inconsistency affects the mathematical reconstruction.

## Limitations and scope of acceptance

This is a source-bounded mathematical manuscript review. The frozen snapshot does not contain the complete external McNaughton, Doner, Thatcher--Wright, or Thomas bodies. I checked that their roles are typed, bounded, and attributed as external dependencies or later routes; I did not claim an independent body-level re-verification of those external works. The Rabin and Meyer bodies themselves were inspected completely.

I did not assess a built or rendered handbook page, TeX compilation, typography after typesetting, accessibility, release packaging, human review, or user acceptance. An ACCEPT here concerns only the unchanged N-c-014.d Round 2 manuscript-content snapshot and does not admit all N-c-014, Part IX, another part, or the book.

## Findings

None.

VERDICT: ACCEPT
