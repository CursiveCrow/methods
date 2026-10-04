# Part VI admission board, round 1: set-theory / descriptive-set-theory topic specialist

## Mandate and method

I reviewed the complete live reader route rooted at `handbook/parts/p06.tex` and `handbook/annex/p06-route.tex`: the 23 exact-source wrappers in their routed order, every routed body supplement, and the three routed annex supplements. I did not read another Part VI seat's transcript. I made no manuscript, control, test, or generated-file edit. I did not build the book or run tests. This is therefore a source/content verdict, not a build, visual, human, or final-admission verdict.

The charter's controlling requirements are exact mathematical hypotheses, definition before use, honest theorem/proof status, all four lots, and no reader-visible OPEN/unadmitted prose (`board-part6-admission-2026-08-21/charter.md:3-16,20-30`).

## Findings

### F1 — blocker — a routed reader section explicitly says that it is OPEN and unadmitted

- **Location:** `handbook/parts/p06.tex:3-6` routes the file; `handbook/parts/p06/zfc-axiom-table-supplement.tex:15-18` prints the heading “OPEN ZFC axiom-table apparatus,” “OPEN and unadmitted,” and the assertion that it closes no source/content/register/acceptance gate.
- **Defect:** This is not a source comment or hidden workflow marker. It is reader-visible text in the admitted route, directly contrary to the charter's no-OPEN invariant (`charter.md:14`). The table beneath it is substantive and otherwise usable, so the problem cannot be dismissed as an unreachable historical remnant.
- **Concrete harm:** A reader is told inside the handbook that a routed Part VI artifact is not admitted and that its content status is unresolved. Consequently Part VI cannot truthfully be admitted as free of reader construction debt.
- **Exact correction:** Once the table has been accepted, replace lines 15-18 by an ordinary descriptive heading and, if provenance is needed, a neutral attribution sentence. Preserve the table and its formal side conditions. Do not merely delete the notice while leaving the table unreviewed; alternatively, if the table is not accepted, unroute the entire supplement.
- **Status:** **open; blocks admission.**

### F2 — must-fix — the relativized-derivation theorem quantifies undefined index-zero objects

- **Location:** `handbook/restoration/inherited-11104-11126.tex:6-18`, especially lines 14 and 16. The declared lists are (v_1,\ldots,v_m) and \(\varphi_1,\ldots,\varphi_k\), but the displayed conjunctions are \(\bigwedge_{j\le m}v_j\in L\) and \(\bigwedge_{i\le k}\varphi_i^L\). The proof consistently refers to the lists (u_1,\ldots,u_r) and (v_1,\ldots,v_m), never to index zero (`handbook/restoration/inherited-11127-11199.tex:2-10,68-71`).
- **Minimal counterexample:** Put (m=k=1). Under the standard natural-number reading of (j\le1) and (i\le1), the conclusion contains the undeclared (v_0\in L) and undeclared \(\varphi_0^L\). Thus the display is not the theorem described in its own hypotheses. The special convention at lines 20-21 handles only (m=0) or (k=0); it does not repair positive indices.
- **Exact correction:** Replace the two bounds by
  \[
    \bigwedge_{1\le j\le m}v_j\in L,
    \qquad
    \bigwedge_{1\le i\le k}\varphi_i^L,
  \]
  or by \(\bigwedge_{j=1}^{m}\) and \(\bigwedge_{i=1}^{k}\). Because exact inherited bytes are an invariant, the admissible campaign repair is an immediate reader-visible editorial erratum/corrected theorem surface between the statement wrapper and its proof, rather than silently changing the inherited source unit.
- **Status:** **open.**

### F3 — must-fix — the definition of (L) applies a nonempty-domain satisfaction convention to the empty structure

- **Location:** `handbook/restoration/inherited-10675-10769.tex:7-30` defines \(\operatorname{Def}(A)\) through satisfaction in \((A,\in)\) for every set (A); lines 32-43 then set (L_0=\varnothing\) and (L_1=\operatorname{Def}(L_0)\). The handbook's first-order structures have nonempty domains (`handbook/parts/p02/first-order-syntax-semantics.tex:261` and `handbook/parts/p02/first-order-calculi.tex:72`). The later proof expressly acknowledges that the fixed convention excludes semantic evaluation over the empty domain, but nevertheless says that Separation proves \(\varnothing\in\operatorname{Def}(L_0)\) “whatever the satisfaction clause returns” (`handbook/restoration/inherited-11127-11199.tex:12-17`).
- **Defect:** Under the declared semantic convention, the expression \((\varnothing,\in),s\entails\varphi\) used by the displayed definition is outside the domain of the satisfaction relation. Separation cannot turn an undefined metalinguistic predicate into a formula. The later observation that every subset selected from the empty set is empty proves uniqueness of a possible value, but it does not supply the missing definition.
- **Concrete harm:** (L_1=\operatorname{Def}(\varnothing)\), hence the recursion defining all later (L_\alpha), is not defined under the handbook's own semantic types. The nonemptiness witness used in the relativization proof is therefore also not established by the printed argument.
- **Exact correction:** Add a local, eliminable base clause before the constructible recursion,
  \[
    \operatorname{Def}(\varnothing)\defeq\{\varnothing\},
  \]
  and use the satisfaction display only for nonempty (A). Equivalently, define (L_0=\varnothing), (L_1=\{\varnothing\}), and apply the displayed \(\operatorname{Def}\)-clause from (L_1) onward. Then replace the argument at `inherited-11127-11199.tex:12-17` by the direct base-clause calculation \(\varnothing\in L_1\subseteq L\). If empty-domain structures are instead to be allowed locally, the text must explicitly extend the satisfaction/assignment convention and prove that it yields the same \(\operatorname{Def}(\varnothing)\); it cannot merely appeal to a convention that excludes them.
- **Status:** **open.**

### F4 — must-fix — the later ccc/name-counting section has lost the scope that types (M,\mathbb P,G), and its plain forcing judgment

- **Location:** The exact forcing convention is expressly limited to “the remainder of this section” and fixes an externally countable transitive (M\models\mathsf{ZFC}), \(\mathbb P\in M\), and the order convention only there (`handbook/restoration/inherited-10770-10825.tex:1-18`). The exact forcing-theorem entry imports a recursive assertion but says that the manuscript has defined only the external semantic relation and introduces no local recursive relation (`handbook/restoration/inherited-11012-11052.tex:1-29,31-40`). After that section and after the exact relative-consistency section, `handbook/parts/p06/constructibility-forcing-supplement.tex:93-135` starts a new section. Its nice-name theorem assumes only that “(M) regards \(\mathbb P\) as ccc,” uses the unindexed judgment (p\forces\cdots), and concludes a statement about (M[G]) (`:118-126`). The annex likewise begins with unqualified (p\forces\cdots) (`handbook/annex/p06/constructibility-forcing-supplement.tex:23-32,53-83`).
- **Defect:** A theorem does not inherit the hypotheses of an earlier theorem, and the original convention explicitly expired at the end of its section. In the live supplement, (M) is not retyped as a transitive ZFC model, \(\mathbb P\) is not reintroduced as a forcing poset in (M), (G) is not assumed (M)-generic in the nice-name theorem, and plain \(\forces\) is not explicitly declared to be the cited recursive assertion rather than the separately defined semantic relation. The symbol registry records a rendering convention, but that does not supply the reader-visible mathematical hypotheses or define the judgment.
- **Concrete harm:** As literally quantified, “(M) regards \(\mathbb P\) as ccc” is compatible with objects for which (M[G]) and the forcing theorem are not available; the asserted consequence is therefore under-hypothesized. The annex proof's appeal to the truth lemma and genericity depends precisely on the missing context.
- **Exact correction:** At the beginning of the new section, add a convention that, throughout it, (M) is the externally countable transitive set model of \(\mathsf{ZFC}\) used by the cited forcing theorem, \(\mathbb P\in M\) is a forcing poset with the fixed orientation, and (G\subseteq\mathbb P) is (M)-generic. State explicitly that, for each fixed standard formula, (p\forces\varphi(\bar\nu)) is a metalinguistic abbreviation for the recursive assertion imported by the cited forcing theorem, while the indexed semantic notation denotes the external relation. Alternatively restate all of those hypotheses and the notation clause in each theorem and annex item. This imports notation only; it need not pretend that the recursive construction was proved locally.
- **Status:** **open.**

### F5 — should-fix for exact definition — the Boolean-valued existential uses a proper-class-indexed join without constructing a set of Boolean values

- **Location:** `handbook/parts/p06/forcing-variants-supplement.tex:97-120` makes \(V^{\mathbb B}\) a proper-class union and defines the Boolean truth map. The existential clause is
  \[
    \operatorname{Bool}_{\mathbb B}(\exists x\,\varphi(x))
      =\mathop{\bigvee}^{\mathbb B}_{\mathbf u\in V^{\mathbb B}}
        \operatorname{Bool}_{\mathbb B}(\varphi(\mathbf u))
  \]
  at lines 141-143, while lines 98-99 and 146-147 justify joins only by completeness, defined there as existence of joins for every **subset** of \(\mathbb B\).
- **Defect:** \(V^{\mathbb B}\) is a proper class, so the displayed subscript is not itself a set-sized index. Completeness of a Boolean algebra supplies joins of sets of elements, not a primitive proper-class join. The standard definition is recoverable, but the required sethood bridge is absent from the exact definition as printed.
- **Concrete harm:** The existential clause is not typed by the immediately preceding definition: the reader cannot infer from “(V^{\mathbb B}\) is a class” and “every subset of \(\mathbb B\) has a join” that the displayed class-indexed operator is an allowed operation without first replacing it by a set of attained values (or proving an equivalent rank bound).
- **Exact correction:** For each already-recursed subformula and parameter tuple, define by Separation
  \[
    S_{\varphi,\bar{\mathbf v}}
      \defeq\{b\in\mathbb B:\exists\mathbf u\in V^{\mathbb B}\,
        b=\operatorname{Bool}_{\mathbb B}(\varphi(\mathbf u,\bar{\mathbf v}))\},
  \]
  state that this is a set, and define the existential value as \(\bigvee^{\mathbb B}S_{\varphi,\bar{\mathbf v}}\). A standard rank-bounded definition plus a proof of independence from the bound is an equivalent repair. Bell's Boolean-valued-model treatment, already cited locally as `Bell2005`, is the appropriate scholarly source for this construction.
- **Status:** **open.**

## Checked-clean coverage

### Lot 1 — checked, subject to F1-F3

- **Checked clean:** the exact ZF/ZFC axiom statements, schema parameters and functionality condition for Replacement, set/class distinction, ordered-pair and natural-number constructions, transfinite induction and recursion, ordinal comparison and arithmetic, cumulative hierarchy and rank consequences, Mostowski collapse, Hartogs, cardinal comparison, alephs/CH/GCH, and the stated AC-equivalence cycle.
- **Checked clean:** the routed table's individual axiom formulas and side conditions; its defect is the admission notice in F1, not a false axiom row.
- **Checked clean:** the weaker-choice implication table at its asserted strengths, binary König lemma, classical fan theorem, and their reciprocal annex proofs. The Zorn entry is honestly marked as sketched and its annex identifies the imported parts rather than silently claiming a complete local proof.
- **Residuals:** F2's malformed finite-conjunction indices and F3's empty-domain constructibility base case.

### Lot 2 — checked, subject to F4-F5

- **Checked clean:** \(\operatorname{Def}(A)\) for nonempty (A), the successor/limit architecture of (L) after a valid base case is supplied, formula-by-formula relativization rather than a class truth predicate, the cited (L\models\mathsf{ZFC}+\mathsf{GCH}+V=L) boundary, and the explicit warning that a countable transitive model is stronger than mere \(\mathsf{Con}(\mathsf{ZFC})\).
- **Checked clean:** forcing-poset orientation, poset filters/dense sets/genericity, names, evaluation, semantic forcing, monotonicity, the cited forcing-theorem boundary, the one-Cohen-real construction, and the relative CH/negative-CH conclusions at the hypotheses actually stated in the exact source.
- **Checked clean:** the ccc-preservation, nice-name, and many-Cohen-real proof arguments once their missing common context is restored; the delta-system/antichain counting and the cardinal/cofinality bounds are mathematically sound.
- **Checked clean:** the forcing catalog distinguishes Cohen/random/collapse behavior, the symmetric-model material states ZFA/ZF transfer boundaries, and the independence table does not silently turn relative consistency into absolute existence.
- **Residuals:** F4's expired hypotheses/forcing notation and F5's Boolean existential sethood bridge.

### Lot 3 — checked clean

- Clubs, closure, stationary sets, diagonal intersection, normality, and Fodor are all stated over a regular uncountable cardinal where that hypothesis is load-bearing.
- The delta-system and \(\operatorname{Add}(\omega,\kappa)\)-ccc proofs are complete at the printed level. Partition-arrow notation, infinite Ramsey, Erdős--Rado, \(\omega_1\)-trees, Aronszajn/Suslin trees, \(\Diamond\), \(\square\), and Martin's axiom keep their stated parameters and relative-status boundaries.
- Cardinal arithmetic, cofinality/regularity/singularity, König's theorem, Hausdorff's successor recursion, Easton's regular-cardinal constraints, and Silver's singular-cardinal hypothesis are not overclaimed.
- The Lévy hierarchy, bounded/one-quantifier absoluteness, finite-family reflection, Shoenfield absoluteness, and the inaccessible/Mahlo/weakly compact/measurable/supercompact entries have the required hypotheses. The large-cardinal table presents conditional implications and cited consistency calibrations rather than asserting unconditional existence.

### Lot 4 — checked clean

- Polish/Baire-space definitions, the boldface Borel hierarchy, Borel-rank exhaustion, analytic/coanalytic/projective definitions, Suslin's theorem, and the regularity-property definitions are coherent and definition-before-use.
- The ZFC regularity claims for analytic sets and the coanalytic boundary correctly separate Baire property/universal measurability from the perfect-set property.
- Gale--Stewart games, open/closed determinacy, Borel determinacy, AD versus Choice, PD, Woodin-cardinal terminology, and the finite/infinite Martin--Steel calibrations retain their required hypotheses. In particular, the manuscript distinguishes “(n) Woodin cardinals below a measurable” for the corresponding finite projective level from infinitely many Woodins below a measurable for full PD; the cited scholarly theorem is Martin--Steel (`MartinSteel1989`).
- The routed figures, tables, index entries, bibliographic keys, theorem-status labels, and reciprocal annex targets inspected in this graph are present. The only reader-visible OPEN/unadmitted marker found is F1; other occurrences are source comments or ordinary mathematical uses of “open.” The current NF consistency-status table also distinguishes the formal Lean construction from the paper-level NF/TTT reduction rather than claiming that the English reduction was itself machine checked.

## Not checked / external gates

- No book build, citation compiler run, generated-register regeneration, PDF/render inspection, visual inspection, human review, or user acceptance was performed. Those are external to this source/content round under `charter.md:15-16`.
- I did not audit unrouted historical duplicates or the intentionally unrouted generated Part VI audit as reader content; they are outside the charter's live reader graph.

## Prioritized repair checklist

1. Resolve F1 and remove or unroute the reader-visible “OPEN and unadmitted” section.
2. Add the invariant-preserving corrected relativization display for F2, with both indices starting at 1.
3. Supply the explicit \(\operatorname{Def}(\varnothing)\) base clause and replace the invalid empty-domain satisfaction appeal in F3.
4. Restore the full (M,\mathbb P,G) context and distinguish imported recursive forcing from semantic forcing in the new ccc/name-counting section (F4).
5. Replace the class-indexed Boolean existential join by a join of a proved set of attained Boolean values (F5).

**Round-one source/content verdict: not admissible while F1-F4 remain open; F5 is an exact-definition repair that should be closed in the same pass.**
