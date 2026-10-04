# Part IX presentation N-c-012: integrated source review, Round 2

## Scope and inspection declaration

I conducted this Round 2 review afresh against the current manuscript source. I read the complete actual LaTeX file `handbook/parts/p09/presentations/n-c-012.tex`, directly from line 1 through line 3000 and EOF. I also directly reread the current shared Part IX LaTeX needed for integration: `handbook/parts/p09/logic-in-computer-science.tex:604-720` (the reused LTL and past syntax, strict/inclusive bridge, discrete-word expressiveness theorem, PSPACE theorem, and safety/liveness definition), `:763-811` (model-checking method and theorem), and `:899-905` (the presentation input seam).

This was a source review, not a PDF or render review. I did not inspect or create a manuscript PDF, PNG, page render, screenshot, test, checker, repository script, TeX-engine invocation, or build; I did not compute or recompute a hash. I did not read another review report. The judgment below is based on the current actual `.tex`, not on the Round 1 verdict.

## Result

No blocker or must-fix finding remains. The five presentations are source-distinct; their temporal conventions, model domains, theorem strengths, semantic/formula levels, and proof ownership are separated accurately. The current final boundary paragraph correctly states the two distinctions implicated by the former IS-01 and IS-02 points, and the shortened source/audit prose retains a sufficient source and rights boundary for every work.

## Recheck of the former finding points

### Former IS-01 point: Pnueli's `\leadsto` standing is now correct

The presentation defines `\varphi\leadsto\psi` locally as Pnueli's printed temporal-implication **statement family**, explicitly saying that it is a relation between state assertions and not a primitive of the handbook LTL grammar (`n-c-012.tex:461-470`). Its witness is strictly later, `j>i` (`:466-470`). The later future-only grammar instead gives inclusive `F` and `G` clauses (`:819-845`), and the manuscript preserves rather than harmonizes the paper's strict/inclusive tensions (`:668-676`).

The closing paragraph now calls `\leadsto` “his printed leads-to relation between state assertions” and contrasts its strict later witness with the later inclusive `F,G` usage (`:2989-2992`). It no longer gives the relation the false standing of an object-language operator. The local definition, its metalinguistic standing, its nonredundancy from LTL, and its use are all explicit.

### Former IS-02 point: the GPSS bridge and its ownership are now correct

The GPSS section distinguishes three things without conflation:

- `\mathsf U_s` is the handbook's unambiguous notation for GPSS's printed strict future-until clause (`n-c-012.tex:1249-1258`).
- GPSS mentions a past counterpart but prints no grammar or semantics for it; `\mathsf S_s` is therefore expressly the **handbook-supplied** order dual (`:1259-1271`).
- The exact bridge is limited to `\omega`-models and relates strict `U_s,S_s` to inclusive strong `U,S` only while discrete next/previous `\mathsf X,\mathsf Y` remain available (`:1292-1313`).

The current closing paragraph mirrors all three limits: it says that the handbook performs the discrete-time comparison, calls the strict past dual handbook-supplied, and says that `\mathsf X` and `\mathsf Y` remain necessary for the exact two-way bridge (`:2992-2996`). The shared chapter states the same domain and translations over `\mathbb N`, including both recursive directions and operand order (`logic-in-computer-science.tex:638-680`), then expressly denies that inclusive `U,S` alone are being credited with next/previous expressiveness (`:681-684`). Thus neither the past operator nor the bridge proof is attributed to GPSS.

## Five-presentation source and semantic boundary

### 1. Kamp 1968

Kamp's presentation is kept at the level of first-order and temporal expressiveness over order structures. The four order classes are exactly defined and distinguished, including the fact that `\mathsf{Com}` is order completeness and may include discrete orders and endpoints (`n-c-012.tex:16-40`). The temporal clauses use strict witnesses, open intervals, and Kamp's original argument order (`:74-98`). The easy temporal-to-first-order direction is stated over every binary structure (`:100-131`), while the converse construction is restricted to complete strict linear orders (`:133-155`); the rational counterexample prevents extension of the same four-operation basis to all linear orders (`:157-165`).

Proof ownership is unusually clear. The sparse-square clause as printed is refuted (`:272-278`), the added parity premise and its proof are marked as handbook-supplied (`:280-341`), and the conclusion again distinguishes Kamp's intended but invalid induction from the handbook repair (`:356-361`). The final boundary accurately summarizes this presentation as first-order expressiveness over classes of linear orders with strict witness/open-interval operators (`:2987-2989`).

### 2. Pnueli 1977

Pnueli's presentation begins with a transition system and infinite executions, including nondeterministic interleaving and the precise program-state types (`n-c-012.tex:372-431`). State assertions and reachability are kept separate from tense formulas (`:433-478`). The presentation records the exact strength of P1, literal P2, and ER; typing additions, counterexamples, and possible repairs are consistently labelled as handbook work rather than silently attributed to Pnueli (`:480-676`). In particular, Theorem 1 remains a source soundness/completeness claim with an expressly sketched proof and identified source-proof gaps (`:618-666`).

The later `F,G` calculus, system-dependent rules, finite-system semantics, and appendix decision route remain distinct layers (`:819-1117`, `:1150-1197`). External ownership of Appendix A's T2/T3 is separated from Pnueli's locally printed six-step lemma (`:1119-1148`). The closing boundary's “transition systems and proof rules” description therefore does not import Kamp's order-theoretic theorem, GPSS's strict-until calculus, Sistla--Clarke's complexity classification, or Alpern--Schneider's semantic property classes (`:2989-2992`).

### 3. GPSS 1980

GPSS's base models are arbitrary linear orders with atomic truth sets (`n-c-012.tex:1212-1227`). The presentation records the printed erroneous direction in the formal `F` clause and labels the coherent strict-future reading and endpoint totalization as handbook repairs (`:1228-1247`). It then maintains the strict `U_s` convention through the program formulas, response conditions, precedence abbreviation, and proof systems (`:1249-1471`, `:1647-1834`). It does not silently identify GPSS's strict operators with the later inclusive convention.

The four first-order result domains are stated separately: point zero of `\omega`-models, future formulas at every point of discrete complete orders, the past/future separation theorem over discrete complete orders, and the source-reported arbitrary-order result with additional but undefined symbols (`:1473-1539`). The proof passage is accurately called an outline, and its dependence on external manuscripts and its omitted core are not promoted to a locally complete proof (`:1541-1645`). Likewise, `DX/DUX` soundness and weak theoremhood completeness remain source claims supported only by the printed outline (`:1647-1772`), and the conflicting `U^0` definition/recursion is preserved as a conflict rather than normalized (`:1774-1827`). The final boundary's discrete bridge is therefore a handbook integration device, not an inflation of GPSS's theorem or proof ownership.

### 4. Sistla--Clarke 1985

This presentation fixes the controlling journal version and separates it from the noninterchangeable conference predecessor (`n-c-012.tex:1838-1861`). Its temporal semantics are inclusive: the witnesses for `U` and `S` may be the present position (`:1863-1923`). Its restricted language names are metalinguistic operator-basis classes, and the positive fragment `\widetilde L(F,X)` is distinguished because it lacks arbitrary negation and hence cannot recover `G` (`:1876-1930`).

The two decision problems are kept apart. “Truth in an `R`-structure” is existential over paths, while universal correctness is obtained through the complement problem; the journal table's validity column is explicitly typed by a reconstruction whose predecessor-source standing is disclosed (`:1932-1970`). The PSPACE theorem names exactly `L(F,X)`, `L(U)`, and `L(U,S,X)`, while the journal classification table separately includes `L(U,X)` and preserves the NP rows (`:2207-2218`, `:2580-2610`). Source proof sketches, abbreviated inductions, the handbook's necessary directed-cycle repair, and the journal's repaired regular-operator development all retain their respective ownership (`:2177-2205`, `:2420-2578`).

The shared PSPACE theorem selects the inclusive `L(U,X)` row and explicitly prevents transfer to another basis (`logic-in-computer-science.tex:695-710`). The shared universal-path model-checking theorem derives its complexity from the corresponding existential problem plus closure of deterministic polynomial space under complement (`:798-810`); it does not attribute the separate automata-theoretic construction to Sistla and Clarke. The final boundary correspondingly names satisfiability, validity, and **existential** path truth for restricted inclusive bases (`n-c-012.tex:2996-2998`).

### 5. Alpern--Schneider 1985

This presentation works over a nonempty state set and the full execution space `S^\omega`; a property is an arbitrary subset of that space, and satisfaction is membership rather than formula evaluation (`n-c-012.tex:2612-2654`). Safety and liveness are given by their exact finite-prefix quantifiers (`:2656-2684`), with an express warning that relativizing to one transition system would change both the continuations and topology (`:2706-2709`). Uniform and absolute liveness are separately defined semantic subclasses and used to establish their strict quantifier distinctions (`:2711-2808`).

The safety/closed and liveness/dense equivalences are kept at full-space semantic standing (`:2820-2839`). Theorem 1 is an existence decomposition, not a syntactic, uniqueness, or complexity theorem (`:2841-2883`). Theorem 2 retains `|S|>1`, and the defective Corollary 2.1 is repaired only under an explicitly handbook-owned hypothesis correction, with a counterexample to the printed version (`:2891-2951`). The source/proof paragraph distinguishes the article's printed theorem proofs from handbook-supplied details (`:2973-2982`). The final boundary therefore correctly says that Alpern and Schneider classify arbitrary subsets of `S^\omega` semantically, not formulas by syntax (`:2998-3000`).

## Shared definitions, theorem strength, and input seam

The shared chapter is consistent with the five source presentations:

- The Part IX definition reuses inclusive future LTL and adds inclusive past `\mathsf Y,\mathsf S` as pointed-word formula constructors, not branching-state operators (`logic-in-computer-science.tex:604-625`).
- It preserves Kamp's exact general-order domain boundary before specializing the bridge to `\mathbb N` (`:627-638`). Both translation maps are given recursively and proved positionwise, rather than asserted by surface-symbol identification (`:638-684`).
- The public first-order theorem is expressly about pointed infinite words and gives the equivalent strict and inclusive-with-`X,Y` bases (`:686-693`). It does not promote the arbitrary-order GPSS symbols `U',S'` into defined operators.
- The public PSPACE theorem states satisfiability for the inclusive `X,U` language and lists the distinct fragment classifications at their exact strength (`:695-710`).
- Safety and liveness are defined as semantic word-property classes and are explicitly said not to coincide with individual surface operators (`:712-720`).
- The model-checking method and theorem keep existential counterexample search separate from universal satisfaction and distinguish fixed-formula linear data complexity from combined PSPACE-completeness (`:763-811`).
- The presentation is included once, after the shared temporal-logic and automata material and before the subsequent model-checking section, at `logic-in-computer-science.tex:903`; the adjacent inputs are separate (`:899-908`).

## Source and rights boundaries after the prose repair

No necessary source or rights boundary has been lost:

- Kamp's controlling institutional dissertation copy, printed-page citation convention, reproduction restriction, and independent-prose standing are all stated at `n-c-012.tex:8-14`.
- Pnueli's author-hosted FOCS copy, wrapper/version distinction, printed pagination, absence of a republication licence, and independent wording are stated at `:365-370`.
- GPSS's author-archive provenance, printed-page authorship control, publication metadata, ACM copying notice, and independent-reconstruction status are stated at `:1201-1210`.
- Sistla--Clarke's controlling journal article, catalogue/facsimile discrepancy, complete-scan provenance, ACM rights notice, independent reconstruction, and repaired journal/conference boundary are stated at `:1838-1861`.
- Alpern--Schneider's journal/report relationship and proof boundary are stated at `:2973-2982`, while the controlling copyright notice and independent-reconstruction status are explicit at `:2984-2985`.

These passages identify the controlling bodies and prevent an access copy, wrapper, scan, technical report, or predecessor from being mistaken for permission to republish or for a silently interchangeable source. Their concise form is sufficient for the integrated presentation.

## AGENTS technical-name rule

The current integration satisfies the local-necessity rule. Its potentially collision-prone names receive exact standing and are then used: Kamp's order classes and `D` translation (`n-c-012.tex:16-72`, `:100-131`); Pnueli's `\leadsto`, `K_b`, proper-execution satisfaction relation, and execution language (`:461-478`, `:887-928`, `:1030-1062`, `:1150-1197`); GPSS's `U_s/S_s`, `\operatorname{Pr}`, and theorem-system names (`:1249-1313`, `:1418-1455`, `:1647-1688`); Sistla--Clarke's operator-basis classes, formula closure, truth sets, and grammar-indexed constructor (`:1876-1930`, `:2280-2303`, `:2428-2479`); and Alpern--Schneider's live-for relation, uniform/absolute subclasses, and `L_P` factor (`:2656-2684`, `:2711-2751`, `:2841-2868`). Each is defined or explicitly held at source-reported standing, distinguished from nearby objects, and used in a later formula, theorem, proof, or boundary.

The manuscript also handles source terms that lack sufficient formal standing in the correct direction: GPSS's `U',S'` are reported only as undefined symbols and are not imported (`:1532-1539`), and its event expressions are identified as an omitted part of the proof outline rather than adopted as handbook machinery (`:1621-1632`). The final five-source paragraph (`:2987-3000`) introduces no new technical name; every distinction there eliminates to definitions already given in the presentation or the shared chapter.

## Rationale for acceptance

The integrated source now has a stable three-level separation: historical claims remain attached to their controlling source and exact theorem domain; handbook reconstructions, type repairs, counterexamples, bridges, and proof completions are labelled as such; and the public Part IX definitions and theorems select only the portions needed for the shared narrative. The final boundary paragraph is both accurate and sufficient because it states the decisive cross-source distinctions—order versus transition-system versus word versus property semantics, strict versus inclusive time, restricted operator bases, existential path truth, and nontransfer of definitions/proofs/terminology—without inventing a sixth unifying source vocabulary.

VERDICT: ACCEPT
