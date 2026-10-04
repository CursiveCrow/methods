# Part VI admission board, round 2: set-theory / descriptive-set-theory topic specialist

## Scope and verdict

I rechecked the current live reader graph rooted at `handbook/parts/p06.tex` and `handbook/annex/p06-route.tex`, with focused attention to every R1 finding, the new Choice-to-Zorn proof, the Aronszajn construction, the master strength table/figure, and repair fallout. I read no other seat transcript, edited no manuscript/control/test/generated file, ran no build, and ran no tests.

**Current source/content verdict: accept.** R1 F1-F5 are fixed. Two mathematical defects and one generated-register omission surfaced while this verification was in progress; all three were repaired in the live bytes and were rechecked before this transcript was filed. No current mathematical or source-content blocker remains. Build, visual, human, and user gates remain external.

## R1 dispositions

### F1 — accept-fixed — reader-visible OPEN/unadmitted notice

- `handbook/parts/p06/zfc-axiom-table-supplement.tex:16-20` now has the ordinary heading “ZFC axiom reference table” and a neutral reader note that correctly gives the exact source ownership of the axioms.
- The axiom formulas and formal side conditions remain intact at `:23-128`.
- No reader-visible assertion that the routed table is OPEN or unadmitted remains. The remaining historical/control prose is in source comments, not the rendered reader surface.

### F2 — accept-fixed — one-based relativization indices

- The exact inherited statement remains byte-preserved, and `handbook/parts/p06.tex:73-75` now places the correction between that statement and its proof.
- `handbook/parts/p06/relativization-index-erratum.tex:1-14` explicitly replaces both malformed bounds by
  \(
    \bigwedge_{1\le j\le m}v_j\in L
  \)
  and
  \(
    \bigwedge_{1\le i\le k}\varphi_i^L
  \), names the otherwise undeclared \(v_0\) and \(\varphi_0\), preserves the empty-conjunction cases, and observes correctly that the following source proof uses only the declared one-based lists.
- This is an adequate invariant-preserving editorial correction: the reader encounters it before the proof and is given one unambiguous corrected theorem.

### F3 — accept-fixed — \(\operatorname{Def}(\varnothing)\) and the nonempty-domain convention

- `handbook/parts/p06/constructibility-base-erratum.tex:1-17`, routed immediately after the exact definition at `handbook/parts/p06.tex:58-59`, gives the eliminable base clause
  \[
    \operatorname{Def}(\varnothing)=\{\varnothing\},
  \]
  restricts the satisfaction-based display to nonempty \(A\), and derives \(L_1=\{\varnothing\}\).
- `handbook/parts/p06/relativization-index-erratum.tex:17-23`, immediately before the preserved exact proof, explicitly supersedes that proof's bad empty-domain phrase by \(\varnothing\in L_1\subseteq L\). It does not silently broaden the global semantics to empty structures.
- The later successor recursion is typed: \(L_1\ne\varnothing\), and for a nonempty level the parameter-free contradiction defines the empty subset, so subsequent \(\operatorname{Def}(L_\alpha)\) levels remain nonempty.

### F4 — accept-fixed — ccc/name-counting forcing scope and notation

- `handbook/parts/p06/constructibility-forcing-supplement.tex:96-116` renews the exact forcing context for the new section: externally countable transitive \(M\models\mathsf{ZFC}\), \(\mathbb P\in M\), stronger-is-smaller order, external \(M\)-generic \(G\), and ground-model cardinal computations.
- The same convention states that bare \(p\forces\varphi(\bar\nu)\) is the cited recursive assertion and that \(p\forces^{\mathrm{sem}}_{M,\mathbb P}\varphi(\bar\nu)\) is the external semantic relation, with their equivalence imported from the forcing theorem rather than re-proved.
- The nice-name theorem and many-Cohen-real corollary invoke that convention explicitly at `:140-163`; the reciprocal annex imports the same meanings at `handbook/annex/p06/constructibility-forcing-supplement.tex:13-18`.
- The proof arguments still check under the restored context: ccc bounds the deciding antichains, the truth lemma supplies the needed condition, genericity meets the dense sets below it, and ccc preservation keeps the ground-model counting cardinal a cardinal.

### F5 — accept-fixed — set-sized Boolean existential

- `handbook/parts/p06/forcing-variants-supplement.tex:146-165` now defines
  \[
    S_{\varphi,\bar{\mathbf v}}
      =\{b\in\mathbb B:\exists\mathbf u\in V^{\mathbb B}\,
        b=\operatorname{Bool}_{\mathbb B}
          (\varphi(\mathbf u,\bar{\mathbf v}))\}
  \]
  as a subset of the set \(\mathbb B\), states its sethood by Separation, and takes the Boolean join of that set. The proper class \(V^{\mathbb B}\) is no longer used as a primitive join index.
- At a fixed formula-recursion stage, the truth value for the proper subformula is already available as a definable class function, so the displayed Separation instance is legitimate. Completeness supplies the resulting set-indexed join, including the empty-set case.

## Focused new-material verification

### Complete Choice-to-Zorn proof — accept

- Body status and hypotheses are exact at `handbook/parts/p06/cardinals-choice-supplement.tex:171-177`; the proof is reciprocal at `handbook/annex/p06/cardinals-choice-supplement.tex:14-54`.
- The empty-chain hypothesis first yields \(P\ne\varnothing\). Choice supplies a well-order of \(P\). The recursion on the set ordinal \(h(P)\) is single-valued, and Replacement/Separation supply the stage set and its strict-upper-bound set (`:16-35`).
- If every stage continued, \(\alpha\mapsto x_\alpha\) would inject \(h(P)\) into \(P\), contradicting Hartogs (`:37-40`). At the first stopping stage, the prior values form a chain with no strict upper bound (`:41-44`). A chain upper bound \(u\) must then lie in the chain and be greatest; any \(y>u\) would again be a strict upper bound, so \(u\) is maximal (`:46-52`).
- No unmentioned choice is used after the one well-order supplied by AC, and the proof covers the empty-poset edge through the explicit empty-chain hypothesis.

### Special Aronszajn-tree construction — accept

- `handbook/parts/p06/infinitary-combinatorics.tex:219-248` keeps the theorem cited and adds a method that supplies the actual level recursion and branch obstruction without pretending to reproduce all bookkeeping.
- The invariant is sufficient: levels consist of selected strictly increasing rational sequences with rational supremum; every earlier node can be extended to a higher countable level with a prescribed larger rational supremum. Successor stages remain countable. At a countable limit \(\alpha\), the prior tree and the pairs \((s,q)\) are countable, and a cofinal \(\omega\)-sequence in \(\alpha\) lets the construction take a union with the required supremum (`:226-239`). Downward closure inherited from the chosen chain gives one predecessor at each earlier level.
- Proper end-extension strictly raises the rational supremum. Hence a branch of order type \(\omega_1\) would inject \(\omega_1\) into \(\mathbb Q\), while every level is nonempty and countable (`:241-247`). This is the standard rational-sequence construction; compare the construction in Jech's *Set Theory*, Theorem 9.16, and the cited `Kurepa1935,Todorcevic1984Trees`.

### Master consistency/proof-strength table and figure — accept after live repair

- During verification, the first version of `handbook/parts/p06/consistency-strength-ladder.tex` incorrectly printed \(\mathsf{PRA}<\mathsf I\Sigma_1\) as a strict proof-theoretic/consistency step. Parsons' theorem says that \(\mathsf I\Sigma_1\) is \(\Pi^0_2\)-conservative over the standard \(\mathsf{PRA}\); see the fetchable scholarly statement in [Joosten, *Two proofs of Parsons' Theorem*](https://dspace.library.uu.nl/handle/1874/27022). I therefore rejected that first version.
- The current bytes close the defect. `handbook/parts/p06/consistency-strength-ladder.tex:10-21` defines the two presentations and their standing. Lines `36-43` state \(\Pi^0_2\)-conservativity, equiconsistency, and their shared usual \(\omega^\omega\) calibration, while retaining a strict proof-theoretic step only from \(\mathsf I\Sigma_1\) to \(\mathsf{PA}\). Lines `99-104` replace the false strength arrow by a dashed bidirectional conservativity/equiconsistency bridge.
- The remaining table rows preserve their comparison kinds: strict theorem inclusion for the reverse-mathematics systems (`:45-51`), first-order conservativity/equiconsistency for \(\mathsf{ACA}_0\) versus \(\mathsf{PA}\) (`:53-59`), a standard-model/interpretation implication from Zermelo set theory to full second-order arithmetic (`:61-67`), \(\mathsf{ZF}/\mathsf{ZFC}\) equiconsistency rather than Choice in ZF (`:69-75`), and conditional property implications rather than strict adjacent large-cardinal consistency gaps (`:77-84`). The figure's caption at `:139-145` explicitly denies a total order, existence, adjacent large-cardinal strictness, or exhaustiveness.

### Internal versus ambient Boolean completeness and Boolean genericity — accept after live repair

- During verification, the ambient construction at `forcing-variants-supplement.tex:102-175` was initially reused by a theorem assuming only that \(M\) computes \(\mathbb B\) complete. That is not sufficient: a Boolean algebra complete in a countable transitive ground model need not be complete in the ambient universe. The same first version called \(G\) an \(M\)-generic ultrafilter without connecting genericity to the forcing poset \(\mathbb B^+=\mathbb B\setminus\{0\}\). Standard Boolean forcing makes this distinction explicitly; see [Jackson, *Introduction to Forcing*, Lemmas 1.8-1.9](https://math.unt.edu/~sjackson/SetTheoryNotes/forcing.pdf).
- The current bytes close both points. `handbook/parts/p06/forcing-variants-supplement.tex:177-192` defines \((V^{\mathbb B})^M\), \(\operatorname{Bool}_{\mathbb B}^M\), the internal set \(S^M\), and the join computed in \(M\), and explains why the superscript is necessary.
- The quotient theorem at `:194-217` sets \(\mathbb B^+=\mathbb B\setminus\{0_{\mathbb B}\}\), fixes its stronger-is-smaller Boolean order, defines \(G\) as a poset filter meeting every \(M\)-dense subset of \(\mathbb B^+\), records the equivalent ultrafilter reading, and uses only the internal \(M\)-names and internal Boolean truth values in the quotient.

### Generated register fallout — accept-fixed

- The new internal-Boolean convention was briefly absent from the routed generated theorem/definition register after the live mathematical repair.
- The current `handbook/generated/audit-p06.tex:90` now contains `def:p06-internal-boolean-universe`, alongside the repaired/new AC-to-Zorn, Aronszajn, and PRA/\(\mathsf I\Sigma_1\) entries at `:54`, `:107`, and `:146`. This matches the claim at `handbook/parts/p06.tex:101-109` that the reader register covers the live theorem- and definition-class entries.

## Fallout check across the four lots

### Lot 1 — checked clean

- The exact ZF/ZFC schemas, set recursion, ordinal comparison/induction/recursion, hierarchy/rank, collapse, Hartogs, cardinal comparison, aleph/CH/GCH clauses, ordinal arithmetic/Cantor normal form, and choice calibrations retain their R1 mathematical content.
- The ordinary ZFC table notice, corrected constructibility base, one-based relativization statement, and complete AC-to-Zorn proof are coherent with the exact-source byte/order invariant.
- The binary König and classical fan proofs remain choice-free for the fixed binary tree; they do not silently generalize to arbitrary finite successor sets.

### Lot 2 — checked clean

- The constructible hierarchy, formula-by-formula class relativization, forcing names/evaluation, semantic and recursive forcing boundary, generic-filter construction, relative CH/negative-CH arguments, ccc preservation, nice names, and many-Cohen-real calculation remain correct under the repaired scopes.
- The forcing catalog retains its exact chain-condition/closure/preservation qualifications. The Boolean-valued presentation now separates ambient completeness from completeness computed in \(M\), and the symmetric/permutation-model material still separates ZFA from the cited transfer to pure ZF.

### Lot 3 — checked clean

- Club/stationary definitions, diagonal intersection, Fodor, Delta systems, partition relations, Ramsey/Erdős--Rado, trees/Suslin/diamond/square/MA, cardinal arithmetic, Easton, Silver, Lévy hierarchy, reflection, Shoenfield absoluteness, and the conditional large-cardinal ladder retain their exact hypotheses and proof/citation boundaries.
- The Aronszajn method and corrected master strength map add no contradiction to those results. The large-cardinal figure remains a conditional calibration and makes no existence, exhaustiveness, or adjacent strict-consistency claim.

### Lot 4 — checked clean

- The Polish/Borel/projective definitions, Borel-rank exhaustion, Suslin theorem, analytic/coanalytic regularity boundary, Gale--Stewart and Borel determinacy, AD/PD distinction, and Martin--Steel Woodin hypotheses remain as accepted in R1.
- The new statement that open/closed Gale--Stewart determinacy is provable in \(\mathsf{ZF}\) without Choice (`handbook/parts/p06/determinacy.tex:38-41`) is correct; no stronger determinacy principle is inferred from it.
- Routed tables, figures, theorem/proof statuses, source map, index entries, bibliography keys, reciprocal annex targets, and the generated theorem/definition register now match the current source/content surface.

## External gates

No build, reference-resolution run, PDF/render inspection, visual inspection, human review, or user acceptance was performed. This transcript accepts the current mathematical/source content only.

**Final R2 disposition: accept.**
