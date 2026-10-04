REJECT

# Round 3 adversarial publication and terminology review: integrated N-c-014

## Scope and evidence discipline

I reviewed the repaired 1,770-line source file `handbook/parts/p09/presentations/n-c-014.tex` directly from line 1 through EOF, and then reviewed `handbook/parts/p09/logic-in-computer-science.tex` lines 836--946, including the input at host line 937. I did not inspect a manuscript PDF, page image, crop, render, or other derivative. I did not run TeX, a build, a test, a checker, a repository script, a hash operation, or automated validation.

Permitted corroboration was limited to the five named source notes, the `N-c-014` and consolidated open-source portions of `spec/research/p09-source-presentations-lot2-3.md`, and the relevant entries in `handbook/bib/handbook.bib`. I did not open a prior N-c-014 review, admission record, board record, ledger, chair record, or agent/thread status. No original historical-source page had to be consulted: the permitted notes resolved the source and version questions relevant to this publication review.

The bounded source architecture is generally strong. The manuscript separates B\"uchi's 1959 report precursor from the unreconciled 1960 journal article; makes Elgot's 1961 article controlling, keeps UMR1342 separate, and assigns the substantive correction to the 1962 errata; keeps Trakhtenbrot's 1961 announcement and 1962 expansion at distinct source strengths; keeps Rabin's 1969 proof architecture separate from Thomas's later game route; and confines every Thomas locator to the May 1996 report precursor rather than the unreconciled 1997 chapter. The revised Elgot construction at lines 375--433 now handles the empty prefix with `d\in D`, every first input with the nonempty `I_\infty(a)` tests, and every later prefix with compatible stable triples. I found no remaining defect in that repaired fixed-point construction.

The source/reconstruction/repair distinctions, rights boundary, bibliography identities, and host placement are also publication-sound at the stated bounded strength. In particular, the manuscript reproduces no source scan or page image and makes no open-licence or redistribution claim; the relevant bibliography entries preserve distinct report, article, errata, expansion, correction, and precursor identities; and the input at host line 937 occurs after the finite-word, S1S, S2S, and finite-ranked-tree context and before the model-checking section. The still-open B\"uchi 1960 and Thomas 1997 reconciliations are accurately bounded and are not grounds for this rejection.

The rejection instead rests on the following local definition-before-use, symbol-standing, and type defects in the actual integrated LaTeX. Each is a publication must-fix under the supplied naming rule.

## Must-fix findings

### 1. Thomas's finite-word logic names are used before their structures and variable ranges are defined

At lines 991--993, `\operatorname{MSO}[S]` first appears as the logic characterizing finite-automaton languages, but the manuscript never defines what the bracketed `S` denotes, which word structure is being interpreted, which letter predicates are present, or the ranges of the first- and second-order variables. The host's modern sentence at lines 837--850 does not define Thomas's notation and does not supply the missing letter-predicate signature. Lines 1000--1022 subsequently describe the singleton-set translation and some atomic forms, but that later material cannot retroactively define `\operatorname{MSO}[S]` at first use. At lines 1022--1024, `WS1S` is likewise named without being expanded or assigned its one-successor structure and finite-set quantifier range. This matters because finite-word MSO over a finite position domain and the weak monadic theory of one successor over `\mathbb N` are different objects even though the same automata construction relates them.

Minimum repair: before Theorem 3.1 is stated, define the finite-word structure for `w=a_0\cdots a_{n-1}` (position domain, successor relation, and the predicates `P_a^w`), state the individual and monadic variable ranges, and declare that this is Thomas's `\operatorname{MSO}[S]`. Keep the existing `\operatorname{MSO}_0` singleton-set translation, but attach it to that defined logic. At the first `WS1S` occurrence, expand it as the weak monadic second-order theory of one successor on `\mathbb N`, with monadic variables ranging over finite subsets, and explicitly distinguish it from the finite word-position structure.

### 2. The domain symbol in Rabin's infinitely-often operator is unbound and collides with an earlier source object

At lines 1115--1119, the manuscript writes `\phi:D\to S` and defines `\operatorname{In}(\phi)`, but no set `D` is introduced or quantified in the Rabin block. Earlier, `D` denoted Elgot's accepting subset at lines 241--257, so leaving the new occurrence implicit is not harmless symbol reuse. The same unbound-domain presentation recurs at lines 1291--1309 in the definition of the `\Omega` types.

Minimum repair: at line 1115 say, for example, "For any set `D` and any map `\phi:D\to S`," or choose a fresh domain letter and type it explicitly. Then refer back to that definition at line 1291 rather than silently reintroducing the same unbound symbol. This one local repair should make clear that `D` is merely the domain of a map and is neither Elgot's accepting set nor Rabin's dual-language constructor `D(\mathfrak A_0,\Omega,s)`.

### 3. Rabin's displayed principal-formula schema leaves two indices without standing

At lines 1178--1186, the display uses `k` and `i_j` before stating their ranges. The range `1\leq j\leq k` does not tell the reader whether the conjunction may be empty, and nothing says that each `A_{i_j}` is one of the displayed free tracks `A_1,\ldots,A_n`. The manuscript does type `w_j` and `\eta_j`, so the remaining omissions are conspicuous in a passage presented as the exact normal-form schema.

Minimum repair: state that the conjunction is a specified finite conjunction (and state whether the empty conjunction is allowed) and that every `i_j\in\{1,\ldots,n\}`. Keep the already supplied declarations `w_j\in T` and `\eta_j\in\{\in,\notin\}`. This completes the standing of every symbol in the schema before Corollary 3.13 is invoked for it.

### 4. "Automaton-definable" path language and the deterministic Muller word automaton lack an eliminable definition

At lines 1249--1256, Theorem 3.1 starts from an "automaton-definable" language `B\subseteq S^\omega`, but no word-automaton model or acceptance relation has yet been assigned to that technical adjective. Lines 1258--1264 then introduce `\mathfrak B=\langle U,K,u_0,H\rangle` without saying that `U` is finite, that `u_0\in U`, how its run on an `S`-word is generated, or that acceptance means that the set of infinitely recurring `U`-states belongs to `H`. The product at lines 1265--1279 relies on exactly those omitted facts. Citing McNaughton's external equivalence does not define the object being selected.

Minimum repair: at the first use, define "automaton-definable" as recognition by a finite omega-word automaton, and immediately give the deterministic Muller presentation actually used: finite state set `U`, initial state `u_0\in U`, total transition `K:U\times S\to U`, run recurrence on an `S`-stream, and acceptance iff the run's infinitely recurring state set lies in `H\subseteq\mathcal P(U)`. Then state that McNaughton's equivalence permits this deterministic presentation for `B`. The existing product proof can remain unchanged.

### 5. The one-letter emptiness recursion asks whether the node set `T` belongs to a language of valued trees

The manuscript defines `T=\{0,1\}^*` as a node set at line 1093 and defines members of `V_\Sigma` as pairs `(v,T_x)` at lines 1099--1101. Lines 1477--1495 refer in prose to the unique one-letter-valued full tree, but never give that valued tree a symbol. Consequently the formal clause at lines 1541--1544, `T\in D(\langle R,N\rangle,\Omega_{k-1},s_0)`, is ill-typed: `T` is only the node set, whereas the dual language contains valued-tree pairs.

Minimum repair: define the unique valuation `v_\bullet:T\to\{\bullet\}` and name the full valued tree, for example `\mathbf t_\bullet=(v_\bullet,T)`, when the one-letter reduction is introduced. Use that pair in the acceptance equivalence, in the reduction to the dual language, and especially in the direct shorter question at line 1543. Do not overload bare `T` with a second standing.

### 6. Thomas's branch variable changes from a node set to a direction stream, making the restriction notation ill-typed

Rabin's earlier path variable is explicitly a subset of `T_x`, so `r\mathbin{\upharpoonright}\pi` is a restriction of a node map. Thomas's later block instead quantifies `\pi\in\{0,1\}^\omega` at lines 1634--1638. Such a `\pi` is a direction stream, not a subset of the node domain `T`, so `r\mathbin{\upharpoonright}\pi` is not a defined map. The same undefined expression is used in the chain condition at lines 1651--1655. This is precisely the kind of cross-source notational conflation that the surrounding presentation otherwise avoids.

Minimum repair: for `\pi\in\{0,1\}^\omega`, define the induced state stream, for example `r_\pi(n)=r(\pi\mathbin{\upharpoonright}n)` with the length-zero prefix equal to `\epsilon`, or define the corresponding prefix-node path as a subset of `T`. Use `\operatorname{In}(r_\pi)` in both the Muller and strict-chain displays. State explicitly that this is Thomas's direction-stream presentation, distinct from Rabin's earlier set-of-nodes path notation.

### 7. The named game `\Gamma_{\mathcal A,t}` is not defined exactly enough for the memoryless-strategy claims that follow

At lines 1706--1713, the manuscript names `\Gamma_{\mathcal A,t}`, says only that Automaton chooses a transition and Pathfinder chooses a direction, and immediately invokes current positions, initial position, winning strategies, and memorylessness. The vertices, whose turn each vertex represents, the initial vertex, the legal-move relation, and the winning condition are never stated. The preceding rejecting-state completion proves that every resulting position has an outgoing move, but without the position and move definitions the named game is not eliminable at its first use and "depends only on the current game position" has no fixed domain.

Minimum repair: define the two position sorts and moves explicitly. For example, from an Automaton position `(u,q)`, Automaton chooses a tuple `(q,t(u),p_0,p_1)\in\Delta`; at the resulting Pathfinder position, Pathfinder chooses `i\in\{0,1\}` and play continues from `(ui,p_i)`; the initial position is `(\epsilon,q_0)`; and Automaton wins exactly when the generated state stream satisfies the already defined strict-chain condition. Then the memoryless-strategy definition, the finite instruction function, and the language-preserving completion have precise standing.

### 8. The definition of a regular labelled tree still relies on an unspecified generator operation

At lines 1737--1740, "regular" is introduced as an exact technical property, but "a deterministic finite word automaton over directions, equipped with an output map to `\Sigma`, generates its node labels" does not specify the generator tuple, total transition, initial state, or label equation. An acceptor with final states and a state-output generator are not the same object, and the later basis argument needs the latter.

Minimum repair: give the eliminable Moore-generator definition at the same location: a finite set `P`, initial state `p_0`, total transition `\delta:P\times\{0,1\}\to P`, and output `\lambda:P\to\Sigma`, with the tree label at node `u` equal to `\lambda(\delta^*(p_0,u))`. State that regularity is a property of the input labelling `t:T\to\Sigma`, as the current prose already correctly emphasizes.

### 9. Thomas's final successor-structure symbols are neither defined nor reconciled with the earlier use of `S_0`

At lines 1750--1752, the manuscript writes `\mathfrak T=(\{0,1\}^*,S_0,S_1)` without defining `S_i`. In the same presentation, `S_0` previously denoted Rabin's initial-state subset at lines 1110--1112, while Rabin's successor maps were denoted `r_i` at lines 1055--1075. The host theorem at lines 874--877 repeats `(\{0,1\}^*;S_0,S_1)` but likewise does not give the maps' types or equations. The final Thomas paragraph therefore changes both notation and standing without a local declaration.

Minimum repair: define `S_i:\{0,1\}^*\to\{0,1\}^*` by `S_i(u)=ui` for `i\in\{0,1\}`, or explicitly identify Thomas's `S_i` with the already defined successor maps `r_i`. Say that these are structure functions, not the earlier initial-state set. Theorem 6.19 and the concluding `S2S` claim can then refer to a fully typed structure.

## Publication assessment after the must-fixes

No source-strength expansion is needed to repair these findings. They are local definedness and standing repairs: the permitted source notes already contain enough information to supply them, and none requires consulting the open B\"uchi journal body or Thomas chapter. Once repaired, the manuscript's substantive historical and mathematical boundaries are positioned to support publication at exactly the strength it claims: B\"uchi 1959 precursor, Elgot 1961 plus published errata, distinct Trakhtenbrot 1961/1962 bodies without specialist-language certification, Rabin 1969 with the later Meyer complexity correction, and Thomas May 1996 report precursor. On the current source, however, the nine first-use/type defects prevent an ACCEPT verdict under the mandatory terminology rule.

REGISTER STATUS: OPEN
