# Part IX presentation N-c-012: integrated mathematical review, Round 2

## Scope and method

I performed this Round 2 review from the current manuscript source rather than carrying forward an earlier verdict. I read the complete current actual LaTeX file `handbook/parts/p09/presentations/n-c-012.tex` directly, beginning at line 1 and continuing through EOF at line 3000. I also reread the relevant current actual LaTeX in `handbook/parts/p09/logic-in-computer-science.tex`, including the LTL definition, strict/inclusive bridge, first-order theorem, complexity theorem, safety/liveness definition, automata-theoretic model-checking theorem, synopsis, and input seam (`logic-in-computer-science.tex:604--811`, `899--906`, `2242--2245`). I did not read another review report.

This is a source-level mathematical and proof-coherence review. I did not inspect or create a manuscript PDF, PNG, page render, screenshot, or other rendered form. I did not run or create a test, checker, repository script, TeX command, build, or hash computation. I did not edit either manuscript source.

## Result

No blocker or must-fix finding was identified. The current integration preserves the five presentations' different semantics, model domains, quantifiers, operator conventions, theorem strengths, and proof ownership. The Round 2 changes specifically named in the assignment are mathematically and typographically coherent.

## Review of the named Round 2 changes

### P1 is now bound to one exact rule

The Pnueli subsection first defines the reachable set `X` from the reflexive--transitive closure of `R` and types a state assertion as a Boolean-valued map on states (`n-c-012.tex:433--450`). It then says explicitly that the source's first general principle is `(P1)` and displays reachable-state induction with all variables bound:

- the base premise is `p(s_0)`;
- the step premise universally quantifies `s,s'` and uses `p(s) and R(s,s') -> p(s')`; and
- the conclusion is `forall s in X, p(s)` (`n-c-012.tex:480--489`).

That rule is sound by induction on the finite `R`-path witnessing membership in `X`. The later sequential-program application now has an unambiguous antecedent: substituting the location attachment into this displayed P1 yields precisely the initial obligation and the universally quantified per-instruction preservation obligation (`n-c-012.tex:678--711`). No induction rule, transition domain, or reachability quantifier is borrowed from ER or from the later LTL calculus.

### The local meaning of K_b is exact and nonmigrating

Pnueli's inclusive future semantics is fixed before the calculus: `F` and `G` quantify over `t >= n`, `F` is the dual of `G`, and the absolute present is the initial state for a system formula (`n-c-012.tex:819--845`). The current text then defines local `K_b` exactly as the pure propositional future theorem system consisting of derived `F := not G not`, G1--G3, and RT, RG, MP (`n-c-012.tex:847--898`). At the same location it supplies the term's standing and nonredundancy: `K_b` is a theorem system, not a formula class or model class, and is distinct from GPSS's later `DX` and `DUX`. It is subsequently required by the statements of Pnueli's Theorems 3 and 5 (`n-c-012.tex:1020--1028`, `1112--1117`). This satisfies the workspace rule for a technical name.

The local definition does not overstate adequacy. The following paragraph still proves that the cited S4 route does not establish completeness for the displayed linear-execution semantics and therefore leaves Theorem 2 as a source assertion with an unresolved model class (`n-c-012.tex:900--928`). Theorem 3 remains a skeletal source claim that embeds the strict leads-to notation as the later inclusive formula `p -> Fq`, with no ER derivations printed (`n-c-012.tex:1020--1028`). Theorem 5 remains a source adequacy assertion for the system extension of `K_b`, while Appendix B addresses only decidability (`n-c-012.tex:1096--1117`). The new definition therefore fixes reference and typing without upgrading theorem strength or proof ownership.

### Removing acquisition and hash prose did not alter mathematical content

The shortened source-boundary paragraphs still identify the controlling works, version distinctions, printed pagination where material, rights boundary, and independent-reconstruction standing: Kamp (`n-c-012.tex:8--14`), Pnueli (`365--370`), GPSS (`1201--1210`), Sistla--Clarke (`1838--1861`), and Alpern--Schneider (`2973--2985`). The complete current file contains no hash display. None of the semantic clauses, hypotheses, theorem statements, repairs, proof-status qualifications, or citations depends on a removed acquisition identifier. The deletions therefore have no mathematical, typing, domain, quantifier, or proof-ownership consequence.

## Reconstruction of the five presentations

### Kamp

Kamp's four order classes remain separately defined: linear, dense, discrete, and order-theoretically complete (`n-c-012.tex:16--40`). Completeness is not conflated with density, endpointlessness, or deductive completeness. His `S(A,B)` and `U(A,B)` retain a strict witness, the first operand at the witness, and the second operand only on the open interval (`n-c-012.tex:74--98`). The first-order translation preserves that argument order and works forward without linearity or completeness (`n-c-012.tex:100--131`); the difficult converse is confined to `Com` (`133--155`), and the rational counterexample prevents promotion to all linear orders (`157--165`).

The main Part IX bridge respects those clauses. On `N`, a strict witness becomes an inclusive witness from the next or previous point, and the reverse equations split the current-witness case from the strict-later case (`logic-in-computer-science.tex:638--649`). The recursive translations preserve operands in both directions and require `X,Y` to recover adjacency (`logic-in-computer-science.tex:650--684`). The discrete first-order theorem consequently states exactly pointed infinite words with Kamp's strict `U,S`, equivalently inclusive strong `U,S` plus `X,Y` (`logic-in-computer-science.tex:686--693`). No arbitrary-order theorem is inferred.

### Pnueli

Pnueli's model remains a transition system with infinite executions from the designated initial state, followed by typed sequential and interleaved concurrent specializations (`n-c-012.tex:363--431`). The printed leads-to notation remains a relation between state assertions with a strict later witness `j>i`, not an LTL connective (`461--478`). P2's zero-rank problem and its independent conflict with strict leads-to remain demonstrated by separate counterexamples (`490--541`). ER's completeness sketch still records the arbitrary-start and nonseriality gaps (`618--666`), and the strict/inclusive tension is stated rather than normalized (`668--676`).

The later finite-system semantics quantifies over proper executions satisfying the action-occurrence condition and keeps arbitrary-start continuations separate (`n-c-012.tex:1030--1062`). Thus neither the later inclusive `F,G` calculus nor the main universal-path model-checking theorem retroactively repairs or redefines the printed strict leads-to relation.

### GPSS

GPSS remains a strict-future presentation. The source's past-pointing inequality for `F` is retained as a printed conflict, while the handbook explicitly states its coherent strict-future repair and endpoint totalization (`n-c-012.tex:1212--1247`). Local `U_s` is the source's strict future clause; local `S_s` is expressly the handbook-supplied strict past dual, not a source transcription (`1249--1276`). On omega-models the equations with inclusive `U,S` are correct, and the text explicitly retains `X,Y` as necessary for the two-way discrete bridge (`1292--1313`).

The four first-order result domains remain disjoint: point zero on omega-models, future formulas at every point of discrete complete models, separation on discrete complete models, and the source-reported arbitrary-order result with undefined extra symbols (`n-c-012.tex:1473--1539`). The undefined symbols are not imported. The proof is still called an outline and its omitted event-expression machinery, numbering conflict, unprinted modifications, and external referrals remain visible (`1541--1645`). `DX` and `DUX` have their own exact axiom surfaces and omega-validity claims (`1647--1688`), and the source's conflicting inclusive `U^0` displays remain unadopted (`1774--1827`). Nothing from Pnueli's locally defined `K_b` migrates into these systems.

### Sistla--Clarke

Sistla--Clarke's word semantics remains inclusive: `U` and `S` permit the witness to equal the current point, and derived `F` is therefore inclusive (`n-c-012.tex:1863--1930`). Satisfiability, universal validity, and existential path truth in a finite total `R`-structure are separately quantified (`1932--1970`). In particular, existential path truth is not silently converted into universal model checking.

The complexity claims remain operator-sensitive. The source theorem lists PSPACE-completeness for `L(F,X)`, `L(U)`, and `L(U,S,X)` (`n-c-012.tex:2207--2213`), while the complete table separately includes `L(U,X)` and keeps the NP fragments distinct (`2580--2610`). The main theorem states the inclusive `L(U,X)` problem and justifies its class by the exact fragment inclusions (`logic-in-computer-science.tex:695--710`). The main universal-path model-checking theorem explicitly takes the complement of Sistla--Clarke's existential-path problem and invokes closure of deterministic polynomial space under complement (`logic-in-computer-science.tex:798--810`). No operator basis or path quantifier is strengthened silently.

### Alpern--Schneider

Alpern--Schneider still classifies arbitrary semantic subsets of the full execution space `S^omega`, with nonempty state set `S`, rather than temporal formulas or paths already restricted by a transition relation (`n-c-012.tex:2612--2654`). Safety quantifies over every continuation after a bad prefix, and liveness quantifies over every finite prefix and permits a prefix-dependent infinite suffix (`2656--2684`). The text explicitly warns that restricting these quantifiers to one transition system would be a separate relativization (`2706--2709`).

The prefix-topology characterizations and closure decomposition remain correct (`n-c-012.tex:2820--2868`). The liveness factor is dense because any nonempty open subset of `closure(P) minus P` would produce a strictly smaller closed superset of `P`. Syntactic expressibility is kept conditional (`2870--2889`). The two-liveness-factor construction and the counterexample to the printed intersection-only corollary remain set-theoretically sound (`2891--2951`). The main short definition preserves the same full-extension reading and describes safety/liveness as semantic classes, not surface operators (`logic-in-computer-science.tex:712--720`).

## Final Pnueli/GPSS boundary and input seam

The rewritten final paragraph is accurate line by line:

- `n-c-012.tex:2987--2989` confines Kamp to first-order expressiveness over order classes with strict witnesses and open intervals.
- `n-c-012.tex:2989--2992` says exactly that Pnueli's state-assertion leads-to relation is strict while his later `F,G` are inclusive and unresolved against it. This matches lines 461--478 and 668--676.
- `n-c-012.tex:2992--2996` now assigns the exact discrete bridge to the handbook, identifies the strict past dual as handbook-supplied, and retains `X,Y` as necessary. This matches lines 1249--1313 and the main bridge at `logic-in-computer-science.tex:638--684`; it does not attribute the supplied past semantics or bridge proof to GPSS.
- `n-c-012.tex:2996--2998` preserves Sistla--Clarke's three decision problems and restricted inclusive bases.
- `n-c-012.tex:2998--3000` preserves Alpern--Schneider's full semantic powerset domain and denies retroactive transfer of definitions, proofs, or source terminology.

The current input seam is `logic-in-computer-science.tex:903`. It follows the inclusive LTL definitions, bridges, theorem statements, safety/liveness definition, and automata results, and precedes the next three presentation inputs (`logic-in-computer-science.tex:899--906`). The presentation ends cleanly at its boundary paragraph before the next input; no theorem, definition, or proof environment is crossed.

## Workspace technical-name rule

The relevant new or locally disambiguated names satisfy the rule at their points of introduction. P1 is bound to its exact displayed rule and used later. `K_b` receives necessity, exact definition, theorem-system standing, distinction from `DX/DUX`, and immediate theorem uses (`n-c-012.tex:887--898`, `1020--1028`, `1112--1117`). `U_s,S_s` receive exact clauses, source/handbook ownership, nonredundancy against inclusive `U,S`, and later use (`1249--1313`). Undefined source artifacts such as GPSS's `U',S'` and event expressions are explicitly withheld from handbook standing rather than being named as hypothetical solutions (`1532--1539`, `1621--1632`).

## Findings

No blocker or must-fix finding.

VERDICT: ACCEPT
