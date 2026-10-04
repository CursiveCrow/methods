# Propositional IPL Kripke soundness and strong completeness

Authoring return, 9 September 2026. Owner: nonclassical_mapping. The mathematical proof package is complete as an author draft. Routing, canonical intake integration, changes to the original theorem and its status, and later independent admission belong to the lead.

## Exact target and source allocation

The bounded target is `ED26-FLRV1-U00869-01`, component `FLRV1-U00869`, the frozen theorem at `source/formal-logic-reference.tex:13068–13078`. It states soundness and strong completeness for every formula set and formula, plus a finite rooted countermodel when the premise set is finite. The controlling frozen source SHA-256 is `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.

The active theorem and sketch were read in full in `handbook/restoration/inherited-13058-13099.tex`. The exact language, finite-support lifting from finite-multiset LJ sequents, partial-order frame, valuation, and forcing clauses were read in `inherited-12989-13045.tex`; the persistence argument was read in `inherited-13046-13057.tex`; the introduction and controlling citations were read in `inherited-12970-12988.tex`. The reciprocal omission record is `handbook/annex/p08/source-sketch-map.tex`, item `annex:p8.ipl.source`, pointing to `thm:p08-source-ipl-adequacy`.

Related records are `ED26-REQ-R-041-01` (the corrected primeness condition is derivability from the theory, equivalently membership after closure) and `ED26-REQ-S-016-01` (the original sketch's missing inline source citation). Their historical observations were preserved. The new proof makes the primeness condition explicit and includes primary citations. These records were not edited or promoted by the author.

The current `intuitionistic-supplement.tex` separately defines a nonempty preorder presentation and permits an arbitrary specified atom set. The older `intuitionistic-and-intermediate.tex` also contains a preorder presentation but is not used as authority for moving the active theorem. The new treatment preserves the original partial-order class and separately proves the same consequence equivalence for all preorders and rooted partial orders.

The entire current `handbook/registry/calculi/lj.tex` was read. The proof uses exactly its thirteen propositional schemes: Id, bottom-left, WL, CL, conjunction-left/right, disjunction-left, both disjunction-right rules, implication-left/right, Cut, and Mix for each finite n >= 1. Quantifier rules are excluded. Id is uncontexted; antecedents are finite multisets; conjunction-right and disjunction-left share their remaining contexts; implication-left splits contexts; the succedent always contains exactly one formula. No Hilbert calculus was substituted.

## Primary source bodies acquired and read

### Kripke 1965

Canonical identity: Saul A. Kripke, “Semantical Analysis of Intuitionistic Logic I,” *Formal Systems and Recursive Functions*, Studies in Logic and the Foundations of Mathematics 40 (1965), pp. 92–130; DOI `10.1016/S0049-237X(08)71685-9`. The existing `Kripke1965` bibliography record is retained.

Free university-hosted PDF: <https://www.princeton.edu/~hhalvors/restricted/kripke_intuitionism.pdf>. The server returned the document directly; no access control was bypassed. Local file: `source/references/p08-intuitionistic-completeness/kripke-1965-princeton.pdf`. SHA-256: `ec03a4a21623ba7ad878f50ee9eb3ff2b3025392d20a9b92b43bb4b010851515`.

This local scan has 38 physical pages and no extractable text layer. The selected semantic extent, printed pp. 93–95, was read in the actual scanned pages (physical pages 2–4), with printed pp. 92 and 96 read for context. Source-page images are `tmp/p08-intuitionistic-completeness/kripke-source-01.png` through `-05.png`. These are images of the acquired primary source, not manuscript renders. The scan is not admitted here as a verified complete copy of all printed pp. 92–130.

The directly read source defines a distinguished-world structure `(G,K,R)` with reflexive/transitive R, persistent atomic truth, local conjunction/disjunction, and future-world implication/negation. It explicitly uses classical reasoning in its metalanguage. It treats primitive negation in a different primitive signature from the handbook's falsum-and-defined-negation LJ presentation. The new chapter cites these pages for the semantic starting point and supplies its own full proofs for the precise handbook signature and calculus. It does not attribute its Zorn construction or its finite truth-profile filtration verbatim to this bounded reading, and it does not retire Kripke's separately allocated full historical presentation.

### Guo, Chen, and Bentzen 2023, version 1

Primary paper: Huayu Guo, Dongheng Chen, Bruno Bentzen, “Verified completeness in Henkin-style for intuitionistic propositional logic,” arXiv `2310.01916v1`, 3 October 2023. Exact PDF: <https://arxiv.org/pdf/2310.01916v1>. Local file: `source/references/p08-intuitionistic-completeness/guo-chen-bentzen-2023-v1.pdf`. SHA-256: `0baf71d3f59da245313afe676c62876f0d1fe3ffc0187acd5881a5ed702b0682`. The document has 12 physical pages, a readable text layer, and its complete paper text was read, with Sections 2–3 the pertinent extent.

The paper uses countably many atoms indexed by natural numbers and a Hilbert presentation. Section 3 explains the repeated-disjunction construction, prime extension, the inclusion model, the truth lemma's implication step, and strong completeness. It identifies Troelstra and van Dalen's 1988 Volume I, definition 6.2 and lemma 6.3, and van Dalen's 2013 alternative. The paper's Lean implementation is reported by its authors; it was not run or accepted as verification of the new manuscript. The prose on p. 4 contains a relation-description mismatch (“symmetric”) while its displayed structure actually requires reflexivity/transitivity and valuation monotonicity; the handbook retains its own explicitly declared order conditions.

The new bibliography key `GuoChenBentzen2023IPL` serves an explicit comparison paragraph only. Its countable Hilbert theorem is not used to discharge the arbitrary-atom LJ theorem. The latter is proved from its own rules in the supplied annex.

### Existing book citations

The canonical identities `TroelstraVanDalen1988` and `TroelstraSchwichtenberg2000` were inspected. The available `source/references/troelstra-schwichtenberg-2000/web-indexed-excerpts-2026-09-09.txt` is an excerpt capture concerning normalization, not a full source body for the present semantic proof. Neither complete book was acquired or read in this block. No book-specific historical source unit is marked acquired or completed here. All inference, extension, truth, soundness, compactness, filtration, and decision obligations of the assigned mathematical theorem are proved within the new package, without an external omitted-lemma dependency.

## Proofs supplied

All thirteen body results have a complete reciprocal annex proof. Their suffixes after `annex:p8.ipl.complete.` are:

| Suffix | Body result | Supplied content |
| --- | --- | --- |
| `persistence` | `thm:p08-ipl-completeness-persistence` | All five formula-construction cases; arbitrary premise-set persistence. |
| `soundness` | `thm:p08-ipl-completeness-soundness` | All thirteen exact propositional LJ schemes, including both disjunction-right cases, split-context implication-left, persistence in implication-right, Cut and n-fold Mix. |
| `finite-support` | `thm:p08-ipl-finite-support-operations` | Identity, monotonicity, finite character, substitution by finitely many Cuts, closure idempotence, deduction in both directions, every connective operation needed by primeness and truth. |
| `maximal-prime` | `thm:p08-ipl-maximal-is-prime` | Target-preserving disjunct extension; closure, consistency, target omission and primeness of maximal avoidance. |
| `prime-extension` | `thm:p08-ipl-prime-extension` | Zorn construction with set-sized formula universe, nonempty poset, union of every nonempty chain, finite-support contradiction, empty-chain and empty-support cases. |
| `enumerated-extension` | `thm:p08-ipl-enumerated-extension` | Unique classical ZF recurrence on a supplied enumeration; union avoidance, maximality and primeness; no decidability or hidden choice assertion. |
| `failed-implication` | `thm:p08-ipl-failed-implication` | Deduction gives nonderivability of the consequent after adjoining the antecedent; prime extension supplies the future witness. |
| `truth` | `thm:p08-ipl-canonical-truth` | Canonical cone is a set, nonempty rooted partial order, with persistent atoms; all five truth-induction cases and both implication directions; all prime extensions remain available. |
| `strong` | `thm:p08-ipl-strong-completeness-full` | Every arbitrary premise set lies in a prime root, with all its members forced and the target omitted; separate equality of the partial-order, preorder and rooted-partial-order consequences. |
| `compactness` | `thm:p08-ipl-semantic-compactness` | Consequence compactness and satisfiability compactness from finite support; no simultaneous choice of finite-model witnesses. |
| `filtration` | `thm:p08-ipl-filtration-truth` | Representative independence, partial-order quotient, persistent valuation on the full atom set, bound 2^|Sigma|, root preservation and every forcing case. Implication preservation uses inclusion of the implication formula's own truth membership. |
| `finite-model` | `thm:p08-ipl-finite-rooted-countermodel` | Exact finite-premise finite rooted countermodel claim, including empty premises and explicit subformula bound. |
| `decision` | `thm:p08-ipl-finite-input-decision` | Finite input model search, complete enumeration bounds, finite forcing evaluation, both answer directions, effective atom-encoding hypothesis. |

The two worked examples calculate the two-world failures of excluded middle and double-negation elimination, and a persistent-premise implication composition. In the latter, the local atom `t` is declared before use.

## Metatheory and source distinctions

The general theorem is stated in classical ZFC for any set of atoms and any premise subset. Zorn's lemma is an explicit sufficient choice assumption, not a claim of minimal foundational strength. The enumerated-language proof works in classical ZF from a supplied enumeration, for an arbitrary premise subset of that language. It does not treat classical derivability tests as effective operations. The finite-input decision procedure separately requires finite effective formulas with decidable atom-name equality.

The prime model consists of all prime extensions of the selected root; it is not restricted to theories omitting the root target. Such a restriction would invalidate the needed failed-implication extension step. In the filtration, order is inclusion of all relevant formula truth sets. An existential relation between representatives is not silently assumed to preserve implication.

## Exact symbol scopes for lead integration

The 25-row intake uses math-delimited glyph cells and actual display operators in the macro column (`\\derives`, `\\forces`, `\\entails`, `\\Rightarrow`, etc.). Source-guarded `\\Prop`, `\\Fm`, and `\\IPL` are not called by editorial prose. All scope keys are labels that exist in the new body or annex, with the following schema-compatible additions extending shared vocabulary to its exact proofs. The remaining four proof/example scope keys already denote their single existing labeled regions.

```json
{
  "schema_version": 1,
  "scopes": {
    "sec:p08-ipl-kripke-completeness": {
      "presentation": "Common vocabulary of the exact propositional LJ Kripke completeness treatment",
      "regions": [
        {"anchor": "sec:p08-ipl-kripke-completeness"},
        {"file": "annex/p08/intuitionistic-kripke-completeness.tex"}
      ],
      "overrides": [
        {"glyph": "\\(u,v,w\\)", "local_role": "worlds of the specified intuitionistic Kripke model", "first_use": "def:p08-ipl-completeness-semantics", "broader_scope": "global", "broader_role": "finite words or valuation", "source": "FLRV1-U00869", "reason": "The semantic definition declares u, v and w as worlds before their first use; the proof preserves that role."}
      ]
    },
    "sec:p08-ipl-prime-extension": {
      "presentation": "Deductive closure and target-avoiding premise sets",
      "regions": [
        {"anchor": "sec:p08-ipl-prime-extension"},
        {"anchor": "annex:p8.ipl.complete.finite-support"},
        {"anchor": "annex:p8.ipl.complete.maximal-prime"},
        {"anchor": "annex:p8.ipl.complete.prime-extension"},
        {"anchor": "annex:p8.ipl.complete.enumerated-extension"},
        {"anchor": "annex:p8.ipl.complete.failed-implication"}
      ]
    },
    "thm:p08-ipl-enumerated-extension": {
      "presentation": "Supplied formula enumeration and the uniquely specified avoiding-set sequence",
      "regions": [
        {"anchor": "thm:p08-ipl-enumerated-extension"},
        {"anchor": "annex:p8.ipl.complete.enumerated-extension"}
      ]
    },
    "sec:p08-ipl-canonical-countermodel": {
      "presentation": "The canonical cone model above a prime theory",
      "regions": [
        {"anchor": "sec:p08-ipl-canonical-countermodel"},
        {"anchor": "annex:p8.ipl.complete.truth"},
        {"anchor": "annex:p8.ipl.complete.strong"},
        {"anchor": "annex:p8.ipl.complete.finite-model"}
      ]
    },
    "sec:p08-ipl-finite-filtration": {
      "presentation": "Finite subformula profiles, quotient worlds and filtration order",
      "regions": [
        {"anchor": "sec:p08-ipl-finite-filtration"},
        {"anchor": "annex:p8.ipl.complete.filtration"},
        {"anchor": "annex:p8.ipl.complete.finite-model"},
        {"anchor": "annex:p8.ipl.complete.decision"}
      ]
    }
  }
}
```

## Routing handoff and completion standing

The lead can place the new body section after the existing IPL semantic statement and before the next independent section. The original theorem's `annex:p8.ipl.source` record can become a reciprocal proof that explicitly invokes `thm:p08-ipl-strong-completeness-full` for its first claim and `thm:p08-ipl-finite-rooted-countermodel` for its second claim, preserving the original stable theorem identity and all its quantifiers. Its hook/status and `entry:p08-ipl` changes remain lead-owned. The two new theorem labels each already point to their own exact complete proofs; no many-to-one annex back-reference is requested.

Body: `handbook/parts/p08/intuitionistic-kripke-completeness.tex`, SHA-256 `cc2ea927fc3ecfacabf90520bf9d74c367d4da827deca0a532a435c421df50d1`.

Annex: `handbook/annex/p08/intuitionistic-kripke-completeness.tex`, SHA-256 `6b209dea009bd97c49865226fd5846487b0b44251fa3cdb89582d04b846a2003`.

Bibliography intake: `handbook/bib/intake-p08-intuitionistic-completeness.bib`, SHA-256 `8cee9e60184c1b16ce3df34d2dffb4daed8dd58cc7ace7128781bab0cc6bf5d9`.

Symbol intake: `handbook/registry/symbols-intake-p08-intuitionistic-completeness.csv`, SHA-256 `d931870a096f8cefe701dae592561bb79c6a4a0d377bb2ac5370b8c1674c616a`.

The author read the entire written body and annex once, including the derivation substitutions, empty-support cases, implication witness, both filtration directions, and the finite search argument. This is an authoring record. No software tests, independent review, manuscript build, manuscript render, or production/admission run was performed. No mathematical component of the assigned theorem remains omitted in this draft. The separately owed complete historical source presentations and consolidated manuscript admission remain outside this bounded completion claim.
