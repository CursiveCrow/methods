# Modal algebra completeness: independent actual-text review

Date: 2026-09-06. Review began 2026-09-07 02:16:27 UTC.

## Result and scope

**Scoped pass. No concrete mathematical defect or necessary citation correction found.**

Read in full the live files:

- `handbook/parts/p10/modal-algebra-completeness.tex` (220 lines at the reviewed snapshot);
- `handbook/annex/p10/modal-algebra-completeness.tex` (278 lines).

Checked the relevant current Part VIII derivability and canonical-frame definitions, the declared Jónsson–Tarski/general-frame dependencies, the `Venema2005Preprint` bibliography entry, and all cited passages in the held primary-source extraction `tmp/src025/venema-chapter6.txt`. No author/reviewer research outputs were consulted. Only this review note was written; no manuscript edits, tests, builds, renders, or additional agents.

## Fixed language and local rules

The language has one normal box, with diamond its Boolean dual. The theorem set L contains the classical tautologies and distribution, and is closed under modus ponens, uniform substitution, and theorem necessitation. The separate derivability relation from Γ uses premises, L-theorems, and modus ponens. It therefore neither necessitates a premise-dependent line nor substitutes freely in fixed local premises. This matches the actual finite-sequence convention in `def:p08-modal-derivability`.

The algebraic box laws □1=1 and □(a∧b)=□a∧□b are the correct dual form of a normal additive unary diamond. The annex verifies monotonicity and modal distribution and explains preservation of theorem validity by the logic's closure rules.

## Quotient congruence and arbitrary valuations

In `annex:p10.modal-algebra.1`, propositional reasoning makes provable equivalence an equivalence relation compatible with the Boolean constructors. Necessitating the two theorem implications and applying distribution proves compatibility with box. No premise-sensitive necessitation is used here. The quotient Boolean identities and both normal box laws are proved correctly.

The equivalence [χ]=1 iff χ∈L follows from tautologies relating χ and χ↔⊤. The canonical assignment evaluates each formula to its own equivalence class.

For arbitrary valuations in F_L, the proof selects formula representatives only for variables in the one selected theorem λ. Leaving every other variable fixed gives a total simultaneous substitution. The subformula induction evaluates λ as the class of its substitution instance, which is again in L. This is sufficient to prove F_L∈Alg(L), without a simultaneous choice of representatives for infinitely many classes. It also proves all displayed theoremhood/validity equivalences, including the stated canonical countervaluation.

If ⊥∈L, propositional explosion makes L the full formula set; its quotient is trivial. Conversely a trivial quotient equates ⊥ with ⊤. An algebra validating this L must have 0=1, and every trivial normal modal algebra validates every formula. These cases are handled exactly as claimed.

## Canonical relation, truth, and maximal consistent sets

For consistent L, F_L is nontrivial, so BPIT applied to a proper Boolean filter makes X_L nonempty. The Jónsson–Tarski embedding gives the Boolean and modal homomorphism into the full complex algebra, with its image the Stone clopens. This establishes the general-frame closure requirements.

The diamond and box definitions of accessibility are equivalent by ultrafilter complement dichotomy. The two contradiction arguments in the annex have the correct orientations: a missing diamond value gives the box of the complement, and a successor omitting a boxed element contains its complement.

Every admissible valuation has a unique preimage valuation in F_L because the Stone map is a bijection onto its image. Defining that function by uniqueness requires no choice of syntactic representatives. Structural induction then identifies the truth set with the Stone image of the algebraic value. This proves validity of every L-theorem under every admissible valuation and, at the canonical assignment, the full canonical truth lemma.

A non-theorem has nonzero complement class. BPIT extends its principal filter to an ultrafilter, yielding the canonical point counterexample. Thus validity on the one canonical general frame is precisely theoremhood.

The correspondence with maximal consistent sets is also complete. An ultrafilter yields a deductively closed, complement-deciding, consistent set. Conversely, maximal consistency gives closure under finite derivations, complement decision by the propositional deduction/case argument, conjunction closure, and invariance under provable equivalence. The displayed order criterion [φ]≤[ψ] iff ⊢L φ→ψ supplies upward closure. These maps are inverse, and the box accessibility clause becomes exactly the actual Part VIII canonical relation. This is an identification of frames and the membership valuation, not an assertion that the underlying frame validates every L-axiom under unrestricted valuations.

## Strong local consequence and BPIT

The finite deduction property follows from the stated premise rules: every derivation is finite, L-theorem lines can be used independently of premises, and the ordinary propositional deduction argument internalizes the finitely many used premises into a conjunction antecedent. Conversely, that conjunction is derivable from its members and modus ponens gives the conclusion. The empty conjunction is correctly ⊤.

If Γ does not derive φ, every finite premise meet conjoined with ¬[φ] is nonzero. Otherwise the corresponding finite implication would be an L-theorem, contrary to the deduction property. This ensures that the filter generated by all premise classes and the complement of the conclusion is proper. Finite meets omitting the complement are nonzero as well, since adjoining the complement would otherwise still give zero.

BPIT supplies a single ultrafilter containing all generators. The truth lemma makes every premise true at the same canonical point and makes φ false there. Thus arbitrary infinite premise sets are covered, with no illicit necessitation, arbitrary infinite meet, or assertion that all premises hold throughout the frame.

Soundness uses only validity of the L-theorems and preservation of truth by modus ponens at the fixed point. For inconsistent L all formulas are derivable, and there is no nonempty general frame validating ⊥. Hence Gen(L) is empty and semantic consequence over it is vacuous. The argument respects Part VIII's nonempty-frame convention.

The final algebraic clarification is correct: for a finite local premise set, the relevant condition is the inequality between the meet of its values and the conclusion value, equivalently validity of the implication. Merely designating 1 for all premises gives a different relation in modal algebras. In particular v(p)=1 entails v(□p)=1 by normality, but on the displayed two-world frame p is true at w while □p is false there. The example properly illustrates the distinction.

## Canonicity boundary

The fixed-language condition requires the underlying canonical frame to validate L under all subset valuations. It is correctly presented as an additional condition beyond the canonical general frame's admissible validity.

Under that fixed-language condition, the same counterexample supplied by strong general-frame completeness is an ordinary-frame counterexample: the canonical valuation is also an allowed subset valuation, satisfaction clauses are unchanged, and the underlying frame belongs to Fr(L). This proves strong local completeness in the fixed language.

Closure of Alg(L) under canonical extensions is a sufficient condition because F_L belongs to Alg(L), and its full complex extension then validates L under every algebra valuation. These are exactly the ordinary subset valuations on the underlying canonical frame. The annex explicitly declines to infer the converse from validity of this one frame to closure of the whole algebra class.

For varying variable sets, the body defines the schematic extension L(Y) before stating the all-variable-set canonicity convention. This separates the source's logical/algebraic equivalence from the weaker hypothesis sufficient for the actual strong-completeness theorem. The empty-variable case still has ground formulas because ⊥ is in the grammar, so schematic instances are defined there as well. No claim about the present status of the source's historical countable-variable question is made.

## Citation verification

All four citation groups match the held preprint's numbering and local pagination:

- Definitions 3.14/3.16, Proposition 3.15, and Theorems 3.13/3.17, pp10–11: provable equivalence, the quotient, congruence, algebraization, and validity in the Lindenbaum algebra.
- Example 5.13, p20, and Definition 5.24, p22: the ultrafilter presentation of the canonical frame and the general-frame admissible-algebra construction.
- Definition 6.10, p31: logical canonicity quantified over all variable sets.
- Definition 6.9 and Theorem 6.12, p31: canonical algebra classes and the implication to Kripke completeness. The final sentence correctly qualifies the separate equivalence of Theorem 6.11 by the all-variable-set convention.

The strong local theorem is supported by the manuscript's own full proof; the prose does not misrepresent the cited theorem-level algebraization result as already stating arbitrary-premise local completeness. The bibliography entry correctly identifies the 19 October 2005, 86-page preprint and expressly uses its own pagination rather than the different pagination of the 2007 published chapter.
