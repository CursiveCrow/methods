# Esakia duality: actual-text mathematical review

Date: 2026-09-06, local time. Review began at 2026-09-07 02:57:40 UTC.

## Scope and outcome

Read the actual esakia-duality.tex body and all three annex proofs.
Checked their interfaces directly against priestley-duality.tex and
heyting-completeness.tex, including the live prime-filter separation,
implication witness, reconstruction, and functor statements.

**Scoped pass. No mathematical repair is required in the inspected
statements, proofs, or finite counterexample.**
No other reviewers' conclusions were read. This review does not
independently re-audit the historical source translations.

## Objects and the implication identity

The prime-filter implication witness gives exactly
\[
 P\notin\widehat{a\Rightarrow b}
 \quad\Longleftrightarrow\quad
 \exists Q\supseteq P\quad a\in Q,\ b\notin Q.
\]
With inclusion as the order, this is the stated downward-closure
identity. The order direction is correct.

The live Priestley topology has basic sets
\(\widehat a\setminus\widehat b\), including the empty-meet and
empty-join cases. Compactness writes every clopen as a finite
union of these sets. Since downward closure commutes with unions,
the argument proves the Esakia condition for all clopens, not
merely clopen upsets.

Conversely, \(X\setminus\downarrow(U\setminus V)\) is clopen
and upward closed, and the proof establishes its residual law
against every upset \(T\). Restricting \(T\) to clopen upsets
therefore proves the required Heyting operation. Priestley
surjectivity supplies all clopen upsets, and the same identity
upgrades the lattice isomorphism to a Heyting isomorphism.

## Prime-filter lifting

The complement of the prime filter \(G\) is an ideal. The actual
sets
\[
 E=\{k:\exists f\in F,\ g\in G,\ f\wedge h(g)\leq k\},
 \qquad
 J=\{k:\exists b\notin G,\ k\leq h(b)\}
\]
are exactly the stated generated filter and ideal: finite
meets or joins of their generators combine into one displayed
witness using the corresponding homomorphism law.

If they met, residuation and implication preservation would give
\(f\leq h(g\Rightarrow b)\). This places \(g\Rightarrow b\)
in \(h^{-1}[F]\subseteq G\), hence \(b\in G\), contradicting
the ideal witness. Thus separation applies; in particular \(E\)
is proper. The resulting prime filter includes all images of
members of \(G\) and excludes all images of its complement,
proving equality of the inverse image with \(G\), not only
one inclusion. No injectivity or surjectivity of \(h\) is assumed.

## Arrows and reconstruction

The homomorphism lifting lemma supplies precisely the order back
condition for the prime-filter inverse-image map. For a continuous
monotone map satisfying back, monotonicity proves one implication
in preservation of upset implication, and lifting a violating
future point proves the other. Thus inverse image preserves the
Heyting residual, as well as lattice operations and bounds.

Back conditions compose in the stated order. The object
reconstruction maps are Heyting isomorphisms and order
homeomorphisms; an order isomorphism and its inverse both satisfy
back. The actual Priestley naturality and reconstruction identities
have the correct directions and remain identities after restricting
to the extra Heyting/Esakia structure. This yields the claimed
contravariant equivalence.

## Empty cases and finite example

The trivial Heyting algebra has no proper prime filter and
corresponds to the empty Esakia space. Its clopen-upset algebra
has one element. Pointwise order and back conditions on empty
domains are vacuous. Maps from a nonempty space to the empty
space do not exist, matching the absence of bounded
homomorphisms from the trivial algebra to a nontrivial one.

For the displayed map from a singleton to the bottom point of
the discrete two-point chain, back fails at the upper point.
With \(U=\{1\}\) and \(V=\varnothing\), the codomain residual
is empty, while the residual of the two empty inverse images
is the whole singleton. The example is therefore correct.

All dependencies named in the inspected proofs are available
under the promised live labels. Only this optional review note
was added and read back. No manuscript edits, tests, builds,
or renders were performed.
