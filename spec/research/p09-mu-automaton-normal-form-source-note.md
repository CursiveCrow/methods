# Modal automaton normal form: primary syntax and proof boundaries

Date: 2026-09-06.

## Outcome

Cover transitions require a separately declared constructor language;
they are not literally a syntactic restriction of the earlier
`B(Q)` grammar. The original paper makes this extension explicitly.
The normal-form and one-unfolding results must also retain their
different conclusions: semantic equivalence for normalization versus
equisatisfiability for one-unfolding.

This note supplies the source locators and the small semantic bridges
needed by the current manuscript. It does not claim to reconstruct the
deterministic trace monitor or its parity-tree factorization.

## Primary versions and locators

- **B&S:** Bradfield--Stirling, [*Modal Mu-Calculi*, 2005
  preprint](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf),
  Section 5.4, printed p. 20, PDF page 21. The cover abbreviation,
  restricted transition clauses, ANF grammar, Theorem 5.3,
  Proposition 5.4 and satisfiability discussion are all on that page.
- **JW:** Janin--Walukiewicz, [*Automata for the modal mu-calculus and
  related results*, author-hosted MFCS paper](https://www.labri.fr/perso/igw/Papers/igw-mu-aut.pdf).
  The author copy uses internal pages 1--11, equal to PDF page numbers;
  do not report these as the proceedings pagination 552--562.
- The [institutional BRICS RS-95-27
  version](https://brics.dk/RS/95/27/BRICS-RS-95-27.pdf) has the same
  numbered results below. Its cover dates the report May 1995; PDF
  page numbers for the article are internal printed pages plus two.
  Both copies were retrieved; mathematical locators below use JW.

| JW location | Content needed here |
|---|---|
| Section 2, p. 3; Definitions 2.1--2.5, p. 4 | Positive syntax, literals, well-naming, guardedness, explicit cover extension, empty Boolean operations. |
| Remark 2.6, p. 5 | Diamond and box conversion to covers. |
| Definition 4.1, p. 7 | Disjunctive grammar and binder side condition. |
| Theorem 4.4 and Lemma 4.5, p. 8 | Normalization through a deterministic bad-trace monitor and a colored finite tree with back edges. |
| Theorem 4.6, p. 8; Corollary 4.7, p. 9 | Closed disjunctive one-unfolding equisatisfiability and linear satisfiability. |
| Definitions 5.1--5.2, p. 9; Definition 5.4, p. 10 | Partial action-map automata and their runs. |
| Theorems 5.5--5.6, p. 10 | Disjunctive formula/cover-automaton translations. |

## Exact mathematical syntax, with notation separated

The source constructors `a -> A` (JW) and `(a)Gamma` (B&S) have the
same defining expression. Write it here as

\[
 \nabla_a\Gamma:=(\bigwedge_{\gamma\in\Gamma}
              \langle a\rangle\gamma)
                 \land[a](\bigvee_{\gamma\in\Gamma}\gamma),
 \qquad |\Gamma|<\omega.                              \tag{1}
\]

Use `bigwedge empty = top` and `bigvee empty = bottom`, explicitly
given in JW Definition 2.5. In particular

\[
 \nabla_a\varnothing=[a]\bot,\qquad
 \nabla_a\{\top\}=\langle a\rangle\top.              \tag{2}
\]

JW Remark 2.6 gives

\[
 \langle a\rangle\phi\equiv\nabla_a\{\phi,\top\},
 \qquad
 [a]\phi\equiv\nabla_a\{\phi\}\lor\nabla_a\varnothing.
                                                               \tag{3}
\]

B&S restricted clauses have the mathematical form

\[
 \bigvee_j\bigwedge_{a\in A_0}\nabla_a B_{j,a},
 \qquad B_{j,a}\subseteq Q\cup\{\top\},              \tag{4}
\]

for a fixed finite action set `A0`. This changes the source's letter
`Sigma` in Section 5.4 to `A0`: Section 5.3 had already used `Sigma`
for proposition letters, whereas Section 5.4 writes it as a list of
actions. Keep these two alphabets distinct.

B&S's ANF clauses, in explicit host notation, are

\[
 \phi ::= P\mid\neg P\mid X\mid\phi\lor\phi
       \mid\mu X.\phi\mid\nu X.\phi
       \mid\left(\bigwedge\Lambda\land
                      \bigwedge_{i=1}^{n}\nabla_{a_i}\Gamma_i\right),
                                                               \tag{5}
\]

where each `Gamma_i` is a finite set of ANFs, the `a_i` are pairwise
distinct, and `Lambda` is a finite set of propositional letters and
their negations, **not fixed-point variables used as conjunctive
literals**. Positivity of bound variables is retained. Formula (5)
makes the ordinary Boolean constants and the `n=0`/empty-literal cases
explicit by the empty-operation convention; these are conservative
host completions, not additional nonempty-action assumptions.

JW Definition 4.1 instead calls variables literals as well, but its
binder rule prohibits binding an `X` that occurs as a conjunctive
literal `X and gamma`; it also requires positivity. It allows only
literals and covers as special conjuncts, with at most one cover for
each action. The standing convention following Proposition 2.4 is
guarded, well-named formulas. These restrictions must not be discarded
when invoking JW Theorem 4.6. They concern cover syntax as a constructor,
not arbitrary conjunctions obtained by expanding (1).

## Why the old transition grammar needs a bridge

The current manuscript's old language is

\[
 B(Q)::=\top\mid\bot\mid\langle a\rangle q\mid[a]q
                     \mid B(Q)\land B(Q)\mid B(Q)\lor B(Q).
\]

For distinct `q,r`, formula (1) contains `[a](q or r)`, which is not
generated by this grammar. Thus the phrase "a syntactic restriction
of B(Q)" is false unless an intermediate language has been defined.

A sufficient local choice is the enriched one-step language

\[
 C(Q)::=\top\mid\bot\mid q\mid C(Q)\land C(Q)
                         \mid C(Q)\lor C(Q),
\]
\[
 B^+(Q)::=\top\mid\bot\mid\langle a\rangle C(Q)
          \mid[a]C(Q)\mid B^+(Q)\land B^+(Q)
          \mid B^+(Q)\lor B^+(Q).
\]

Now (4) is literally a restricted grammar within `B+(Q)`. In its
game semantics the model move precedes evaluation of the inner
Boolean expression. In `[a](q or r)`, the existential choice of
control may therefore depend on the successor just chosen by the
universal player. It cannot be replaced with `[a]q or [a]r`: two
successors, one satisfying only `q` and the other only `r`, separate
those expressions.

Alternatively declare covers as primitive one-step instructions with
the two obligations in (1), as JW does. Either choice is an explicit
syntax extension. A later equivalence or compilation back to the old
grammar requires its own proof; merely naming a fresh disjunction
control with an arbitrary priority is not such a proof. The parent's
already supplied scalar-formula/guarded-automaton translations offer
an indirect semantic bridge if needed, provided the enlarged
transition games are included in its formula translation.

## Partial action maps, top targets and empty action sets

JW Definition 5.1 uses

\[
 \delta:Q\longrightarrow
   \mathcal P(\Sigma_p\times(\Sigma_a\rightharpoonup\mathcal P(Q))).
                                                               \tag{6}
\]

For a selected pair `(p,f)`, the action obligations are exactly
`bigwedge_{a in dom(f)} nabla_a f(a)`, together with its current-letter
test. Thus `a notin dom(f)` means **no condition on a-successors**,
whereas `f(a)=empty` means **there are no a-successors**.

To pass from this partial-map notation to the full finite-action
conjunction (4), insert for each omitted action the tautology

\[
 \nabla_a\varnothing\lor\nabla_a\{\top\}\equiv\top  \tag{7}
\]

and distribute the finitely many disjunctions. Equation (7) splits
the zero-successor and nonzero-successor cases. Inserting only a
singleton-top cover would wrongly force a successor. When `A0` is
empty, its conjunction is `top`; letter tests and transition
alternatives remain meaningful.

The target `top` in (4) is semantically always successful, not an
unspecified ordinary control. A game may treat it as a successful
terminal at the chosen successor. If a representation insists that
every target belongs to `Q`, introduce a fresh always-successful
control with transition `top` for every letter; its single terminal
visit does not affect infinite parity. Such an encoding is a supplied
representation choice, not a target already present in (6).

One source-convention difference remains visible: JW Definition 5.4
calls a run an infinite labeled tree and states its branch parity
condition, while B&S Section 5.3 explicitly permits finite complete
branches. The local manuscript should keep its explicit finite
terminal/game rules and should not claim literal identity of the two
run definitions without a bridge for terminal continuation.

## Proof route and exact external obligations

B&S Theorem 5.3 is the modal-automaton simulation statement; its
paragraph identifies determinization as substantive. Proposition 5.4
is the restricted-automaton-to-ANF statement. Neither has a complete
construction printed in that paragraph.

JW supplies the following route, at the locators above:

\[
 \text{regular tableau}
 \longrightarrow\text{deterministic parity monitor for bad mu-traces}
 \longrightarrow\text{colored finite tree with back edges}
 \longrightarrow\text{disjunctive formula}.
\]

Lemma 4.5 supplies the colored-tree condition: existence of a mu-trace
on an infinite unfolded path is determined by the color of its
highest infinitely revisited tree node. Theorem 4.4 builds the formula
from leaves to root, assigning one variable to each backedge target
and a binder according to its color. Theorem 5.6 applies the same
tree method to the cover automaton. The printed arguments are
outlines; they do not expand the deterministic-monitor construction.

An explicit derivation of B&S's simulation statement can also compose
general automaton-to-formula equivalence, guarded normalization, JW
Theorem 4.4 and JW Theorem 5.5, followed by the alphabet and cover
representation bridges. This is not a local Boolean DNF algorithm:
the normal-form theorem contains the global bad-trace/determinization
step.

There is a useful supplied route for the parent's restricted-to-ANF
construction. Grammar (5) is closed under capture-avoiding substitution
of ANFs for **variables**. Structural induction proves this: variable
leaves are replaced, disjunctions and binders preserve the grammar,
and substitution only changes members of a cover's child set; it
does not change the propositional literal clause or merge action
labels. Consequently the Bekić elimination from the companion note
preserves ANF if every initial coordinate body is already an ANF in
the substituted variables. This prerequisite must be shown; an
arbitrary reverse automaton-to-formula translation need not return
ANF automatically.

## Exact one-unfolding satisfiability statement

JW Theorem 4.6 assumes a **closed disjunctive formula**, with the
standing guarded/well-named convention. It replaces occurrences of
mu-bound variables by `bottom` and nu-bound variables by `top`.
Remove the resulting vacuous binders. The conclusion is

\[
 \operatorname{Sat}(\alpha)
 \quad\Longleftrightarrow\quad
 \operatorname{Sat}(\operatorname{cut}(\alpha)),       \tag{8}
\]

not truth at the same state of the same model. B&S expresses the
cut as `mu X.psi(X)` becoming `psi(bottom)` and `nu X.psi(X)`
becoming `psi(top)`. For nested binders, implement this recursively
through the original well-named syntax: each variable occurrence
knows its original binder kind. It is not a rule replacing the
entire mu-subformula by `bottom` or the entire nu-subformula by
`top`; for example vacuous `mu X.P` cuts to `P`.

The printed JW proof uses the corresponding tableaux and a minimal
marking to reconstruct a regular model without mu-regenerations.
Corollary 4.7 then gives linear-time satisfiability for the disjunctive
input. These are source statements with a proof outline, not a full
reconstruction in this note.

Two supplied checks keep (8) at its proper strength.

- `nu X.nabla_a{X}` cuts to `nabla_a{top}`. A root with one edge to
  a dead end satisfies the cut but not the original; both formulas
  are nevertheless satisfiable in some model. Thus (8) is not
  semantic equivalence.
- `(mu X.(P or <a>X)) and not P` is satisfiable, but its cut is
  `P and not P`. The outer conjunction is not allowed by (5).
  Consequently (8) cannot be transferred to arbitrary formulas.

For the fixed-point-free cut, the local satisfiability calculation is
elementary: a literal-and-cover clause is satisfiable iff its literal
set is consistent and every member of each cover child set is
satisfiable. Empty child sets impose no witness requirement and are
satisfied by giving that action no successors. For the converse,
take disjoint pointed models of all required children, add a fresh
root with the specified consistent literals, and connect it to those
roots using the corresponding pairwise distinct actions. Every
successor satisfies a member of its cover, so both parts of (1)
hold. This explains why the cut has a bottom-up local satisfiability
calculation; it does not replace the proof of (8).

## Handoff boundary

Only this note was created. No manuscript or previous note was
edited, and no code, software tests, builds, source/manuscript renders
or additional agents were used. In particular the simulation theorem's
global deterministic-monitor step remains an explicitly identified
primary-source dependency, not a completed local construction.
