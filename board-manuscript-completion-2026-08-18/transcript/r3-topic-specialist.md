# Round 3 topic-specialist verification

### F6 — still-open (equality-rule residual only)
- reply: still-open
- current location: `handbook/registry/calculi/mltt-intensional.tex:4-34`; `handbook/parts/p07/lambda-calculi-and-type-theories.tex:398-448`
- fixed portion: The context and structural rules are now displayed at sheet lines 6-10, and the universe judgment, Russell elimination, cumulativity, and universe-closure rules at lines 29-34 derive the advertised hierarchy without the former circular premise. The body at lines 400-422 now consistently identifies the sheet as the selected formal calculus while withholding normalization and decision claims for the full selection. The stale contradictory owed-artifact prose from Round 2 is gone.
- residual: Judgmental equality is still not exactly generated. Sheet line 14 uses undefined metavariables `c(\bar a)` and `C` and delegates the essential dependent hypotheses to “ordinary dependent typing premises.” That does not determine, for example, how the codomains in application congruence are transported when equal arguments produce definitionally equal but not literally identical dependent result types. The displayed computation rules at lines 19, 24, and 28 also have no formation or typing premises, so as written they license equality conclusions for untyped raw expressions. This falls short of I3 and of Round 2's requirement to display the structural and judgmental-equality rules of the selected calculus.
- exact correction: Keep the repaired structural and universe rules. Replace the generic congruence line by explicit, typed congruence rules for each displayed type and term constructor (or one fully defined metavariable schema whose domain, dependent substitutions, and result types are exact), and add the required context/type/term premises to the Pi-beta, Sigma-beta, and J-beta computation rules. If that exact equality-generation surface is not supplied, withdraw the claim that the sheet fixes the combined calculus and restore an owed-artifact boundary for it.

### F8 — still-open (notation/reduction residual only)
- reply: still-open
- current location: `handbook/registry/calculi/omega-arithmetic.tex:4-15`; `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:326-369`
- fixed portion: The linked equality calculus and the Q1-Q8/atomic-truth initial schemas now fix the former undisplayed arithmetic base at sheet lines 4-14. The omega rule at line 15 explicitly preserves uniform free parameters, and body lines 332-336 explain how a finitary induction instance with parameters is replaced by all numeral derivations followed by that rule. Those two Round 2 gaps are fixed.
- residual: The ordinal data used to state the cited decrease theorem are still not exact. Body lines 344-350 give a Cantor-normal-form grammar and comparison, but “the standard fundamental sequences obtained recursively from the last exponent” omits the recursive successor/limit clauses and the indexing convention. Lines 351-355 then refer to “Schütte's rank/height assignment,” a subsidiary index, and a natural-sum treatment of finite or countable branching without defining any of them or locating the exact imported construction. Consequently the assertion at lines 362-367 that every principal, commutative, structural, and omega-rule case decreases under *that* assignment is not checkable for the locally selected calculus. This remains the ordinal-notation/reduction part of F8, not a defect in the repaired arithmetic axioms or parameter embedding.
- exact correction: Define the fundamental-sequence operation on the displayed notation grammar clause by clause, including its numeral indexing convention, and either display the derivation assignment and reduction/decrease cases used by the theorem or cite an exact theorem/section and state the translation showing that its calculus, parameter convention, and notation operations are the ones fixed here. Otherwise retain the arithmetic sheet but restore an explicit owed-artifact boundary instead of the current cut-elimination/decrease claim.

### F20 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p11/philosophy-of-logic.tex:62-93`
- reasoning: The revision takes the permitted Round 2 boundary route. Lines 63-67 say expressly that TB, CT, KF, and FS are non-unique literature abbreviations and use them only as retrieval labels. The table at lines 71-76 identifies each family's distinguishing commitment and lists the base, language/coding, induction, constructor, rule-domain, and fixed-point choices that must be supplied before any theorem is stated. Lines 80-85 give necessity, metalinguistic standing, nonredundancy, sole later use, and a survey source; lines 89-93 keep conservativity variant-specific and do not promote a bare acronym to a formal result. No local theory is now purportedly defined, so complete coded axiom schemes are no longer owed at this survey boundary.

## Round disposition

- accept-fixed: F20.
- still-open: F6 (exact judgmental-equality generation only), F8 (exact notation/reduction binding only).
- needs-evidence: none.

This focused round inspected only F6, F8, and F20 and made no manuscript or control-file edits.
