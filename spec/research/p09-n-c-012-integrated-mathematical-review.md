# Part IX presentation N-c-012: integrated mathematical review

## Review scope and method

I read the complete actual LaTeX source `handbook/parts/p09/presentations/n-c-012.tex`, from line 1 through its EOF at line 3020. I also read the actual LaTeX in `handbook/parts/p09/logic-in-computer-science.tex` that fixes the reused LTL standing, the strict/inclusive bridge, the first-order and complexity theorems, the safety/liveness definition, the automata-theoretic model-checking theorem, the later complexity synopsis, and the `\input` seam (especially lines 602--812, 900--907, and 2243--2246).

This was a source-level mathematical and proof-coherence review. I did not inspect a manuscript PDF, page render, image, screenshot, or any other rendered form. I did not run TeX, a build, a checker, a repository script, a test, or a hash computation.

## Result

No blocker or must-fix finding was identified. The integrated presentation keeps the five historical presentations at their own semantic and proof-theoretic standings, and the main overview uses only explicitly justified bridges between them.

## Semantic reconstruction

### 1. Kamp: strict witnesses, open intervals, and order classes

The Kamp presentation fixes four classes of strict linear orders and does not conflate density, discreteness, or order-theoretic completeness (`n-c-012.tex:23--47`). In particular, the conditional predecessor/successor clauses do not import endpointlessness, and the examples distinguishing `Com` from `Den` are mathematically compatible with the displayed definitions.

The clauses for Kamp's prefix `S(A,B)` and `U(A,B)` have exactly the required shape: a strict witness carries the first argument, while the second argument holds only on the open interval (`n-c-012.tex:81--105`). The first-order translation preserves all three features---strictness, open interval, and operand order (`n-c-012.tex:107--138`). The converse is not promoted from complete orders to all linear orders: the use of cuts is confined to `Com`, and the rational counterexample is retained (`n-c-012.tex:140--172`). Thus neither the discrete-word theorem nor the later complexity material is used to widen Kamp's source theorem.

The main overview repeats that exact limitation (`logic-in-computer-science.tex:628--637`). Its discrete equations

- `U B A = X(A U B)` and `S B A = Y(A S B)`, and
- inclusive `A U B = B or (A and U B A)` and its past dual

are correct on `N` (`logic-in-computer-science.tex:639--649`). A direct witness check verifies them: a strict witness after the current point becomes an inclusive witness from the next position, while the reverse equation separates the current-witness case from the later-witness case. The recursive translations preserve the same operand order and define next/previous by forcing the open interval to satisfy false (`logic-in-computer-science.tex:651--683`). The resulting one-free-variable first-order theorem is therefore stated over pointed discrete words with exactly `X,Y` and inclusive strong `U,S`, not over an unqualified order class (`logic-in-computer-science.tex:687--694`).

### 2. Pnueli: transition systems and the strict/inclusive tension

Pnueli's section begins with a transition system and infinite executions from its designated initial state, then separately specializes to sequential and interleaved concurrent programs (`n-c-012.tex:384--443`). Its printed leads-to family is explicitly typed as a relation between state assertions and uses `j>i`, hence strict futurity (`n-c-012.tex:445--490`). It is not added to the handbook LTL grammar.

The presentation does not normalize the source's inconsistent proof systems. It records both the zero-rank defect and a counterexample to combining rule P2 with strict leads-to (`n-c-012.tex:501--552`). It also isolates the two further completeness-sketch gaps: changing from executions beginning at `s_0` to arbitrary starting states, and using infinite-execution quantification without seriality (`n-c-012.tex:629--677`). Most importantly for integration, it states that later `F,G` include the present (`n-c-012.tex:830--856`) and explicitly notes that A2, P2, and the later representation `p -> Fq` do not reconcile with the printed strict leads-to clause (`n-c-012.tex:679--687`, `1027--1035`). No main theorem relies on ER soundness under the strict reading.

The finite-system material remains path-sensitive: proper executions start at `s_0` and satisfy the stated action-occurrence condition (`n-c-012.tex:1037--1069`). This is not transferred to Alpern--Schneider's full word space. The later main model-checking theorem independently quantifies over all paths of its finite total structure and explains the complement from Sistla--Clarke's existential path problem (`logic-in-computer-science.tex:764--812`).

### 3. GPSS: strict future operators and the discrete inclusive bridge

The GPSS presentation fixes a strict future language and flags the source's isolated past-pointing inequality as conflicting with the surrounding strict-future clauses (`n-c-012.tex:1227--1262`). The local notation `U_s` is exactly defined with a strict future witness and open interval. Its past dual `S_s` is expressly identified as handbook-supplied rather than source-transcribed (`n-c-012.tex:1264--1291`). This satisfies the workspace naming rule: necessity, definition, standing, nonredundancy, and subsequent use are given together.

On omega-models, the translation

- `A U_s B = X(A U B)`, and
- `A U B = B or (A and A U_s B)`

and the corresponding past equations are correct (`n-c-012.tex:1307--1328`). The text correctly warns that the interdefinition requires discrete next/previous; it does not credit inclusive `U,S` alone with next-time expressiveness. These equations coincide with the main overview after accounting for Kamp's reversed prefix operand order.

The GPSS theorem domains remain separate: point zero of omega-models, arbitrary points for future formulas on discrete complete orders, past/future separation on discrete complete orders, and the source-reported arbitrary-order theorem with undefined additional symbols are itemized as four different hypothesis packages (`n-c-012.tex:1488--1554`). The latter symbols are not imported into the handbook. The final source convention is also handled honestly: the printed inclusive `U^0` equation conflicts with its recursion, and the presentation refuses to adopt it as a coherent operator or transfer its completeness claim (`n-c-012.tex:1789--1849`). Consequently, the clean discrete strong-until bridge used by Part IX is a stated handbook bridge, not a silent repair of the conflicting source `U^0`.

### 4. Sistla--Clarke: inclusive words and operator-sensitive problems

The Sistla--Clarke subsection gives inclusive clauses for `U` and `S`; each witness may be the current position, and derived `F` is therefore inclusive (`n-c-012.tex:1883--1949`). It separately types satisfiability, validity, and existential truth along a path in a finite total `R`-structure (`n-c-012.tex:1952--1990`). In particular, existential path truth is not silently restated as universal model checking.

The operator bases remain load-bearing throughout. The richer-basis PSPACE theorem lists `L(F,X)`, `L(U)`, and `L(U,S,X)` (`n-c-012.tex:2227--2238`), while the complete source table separately includes `L(U,X)` and keeps the `L(F)` and positive `tilde-L(F,X)` NP rows distinct (`n-c-012.tex:2600--2630`). The main PSPACE theorem states the inclusive `L(U,X)` problem and justifies it by the exact inclusions `L(U) subset L(U,X) subset L(U,S,X)` (`logic-in-computer-science.tex:696--710`). The main universal-path model-checking result then obtains its complexity from the complement of the source's existential-path problem and notes closure of deterministic polynomial space under complement (`logic-in-computer-science.tex:799--811`). No fragment, path quantifier, or operator basis migrates silently.

### 5. Alpern--Schneider: semantic subsets of the full execution space

The Alpern--Schneider presentation explicitly takes a nonempty state set, defines finite prefixes and all infinite executions, and identifies a property with an arbitrary subset of the full `S^omega` (`n-c-012.tex:2632--2674`). Program behavior is a separate subset whose satisfaction relation is inclusion. Safety and liveness then quantify over all infinite continuations and all finite prefixes in that full space (`n-c-012.tex:2676--2729`); they are not relativized to paths of Pnueli's or Sistla--Clarke's transition systems.

The prefix-topology equivalences and the closure construction are coherent (`n-c-012.tex:2840--2888`). In particular, the proposed liveness factor is dense because any nonempty open subset of `closure(P) minus P` would yield a strictly smaller closed superset of `P`. The text correctly limits the conclusion to existence and separately states the additional closure assumptions needed for syntactic expressibility (`n-c-012.tex:2890--2909`). The two-liveness-factor construction and the counterexample to the source's printed intersection-only corollary are set-theoretically sound (`n-c-012.tex:2911--2971`). The main overview's short definition preserves the same full-extension quantifier pattern and says explicitly that safety/liveness are semantic classes rather than surface operators (`logic-in-computer-science.tex:713--721`).

## Notation, theorem ownership, and the input seam

The integration uses visibly and semantically distinct notation where reuse would be dangerous: Kamp's prefix `U,S`; GPSS's local `U_s,S_s`; the overview's sans-serif inclusive `U,S`; Pnueli's relational leads-to; Sistla--Clarke's source language classes; and Alpern--Schneider's subsets of `S^omega`. New local names are either exactly eliminable and immediately used or are explicitly reported as undefined source artifacts that are not imported. Representative compliance points are the tense-defining-formula standing (`n-c-012.tex:49--59`), the GPSS convention warning (`1264--1291`), the operator-restricted language classes (`1896--1903`), and the constructed liveness factor (`2861--2873`).

The `\input{parts/p09/presentations/n-c-012}` seam occurs at `logic-in-computer-science.tex:904`, after the inclusive LTL definitions and relevant theorems and before the later source presentations (`logic-in-computer-science.tex:900--907`). The presentation therefore inherits the intended Part IX context without being inserted into a proof, definition, or theorem environment, and its final paragraph closes the file before the next input.

## Line-by-line review of the final boundary paragraph

- `n-c-012.tex:3009` correctly announces a boundary among the five presentations; it does not introduce a sixth theory or theorem.
- `n-c-012.tex:3010--3011` accurately limits Kamp to first-order expressiveness over linear-order classes with strict witnesses and open intervals. This matches lines 23--172 and the main restriction at `logic-in-computer-science.tex:628--637`.
- `n-c-012.tex:3011--3014` accurately keeps Pnueli in a transition-system/proof-rule setting, identifies strict printed leads-to, and says that the later inclusive `F,G` uses do not resolve the paper's tensions. This matches the explicit counterexamples and warning at lines 501--552 and 679--687.
- `n-c-012.tex:3014--3016` accurately summarizes the GPSS strict future language and the discrete bridge. Read with lines 1264--1328 and 1789--1849, it neither imports the handbook-supplied past dual as source text nor suppresses the separate defective `U^0` display.
- `n-c-012.tex:3016--3017` accurately preserves all three Sistla--Clarke decision problems and their explicitly restricted inclusive operator bases; the complete table at lines 2600--2630 supplies the exact rows.
- `n-c-012.tex:3018--3019` accurately identifies Alpern--Schneider's objects as arbitrary semantic subsets of the full execution space, not formula classes.
- `n-c-012.tex:3019--3020` is supported by the preceding local definitions and ownership warnings: no presentation supplies another's definitions, proof completion, model domain, or terminology retroactively.

## Findings

No blocker or must-fix finding.

VERDICT: ACCEPT
