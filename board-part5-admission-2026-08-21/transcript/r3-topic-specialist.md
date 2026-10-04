# Round 3 final arithmetic/proof-theory verification

## Verdict

All R1/R2 arithmetic and proof-theory findings are now closed in the frozen
Part V body/annex bytes. I found no remaining mathematical or source-content
defect in the instructed scope.

I read only my own prior transcripts and the current Part V route/body/annex.
I did not read another seat, edit manuscript/control/test/generated files,
build, or run tests.

## F8 — accept-fixed: full closure-style Sigma-one completeness

The annex no longer assumes a false pure-logical prenex conversion.
handbook/annex/p05/depth-completion-supplement.tex:19-24 explicitly retains
the closure-style \(\Sigma^0_1\) syntax and identifies the dependent-witness
case under bounded universals.

The proof now has the required layers:

1. Lines 26-38 give primitive-recursive term evaluation and Q proof-code
   constructors.
2. Lines 40-76 prove positive and negative numeral-instance completeness for
   every bounded formula, including bounded existential and universal cases.
   The finite case split uses the already complete Q bounded-case lemma.
3. Lines 78-115 state the substitution/proof-code invariant and verify it in
   PA. The proof operations appended by the constructors are exactly the
   finite operations checked by the fixed proof predicate.
4. Lines 117-154 recursively assign one bounded evidence formula
   \(E_\varphi(\vec x,e)\) to every formula in the full closure-style
   \(\Sigma^0_1\) class. Pair codes handle conjunction/disjunction and ordinary
   existential witnesses. At a bounded universal, the beta code stores a
   separate evidence object for each bounded index:
   \[
   E_\varphi(\vec x,e)\equiv
   \forall y\le t(\vec x)\,\exists v<Se\,
   \bigl(\mathsf B(e,y,v)\land E_\psi(y,\vec x,v)\bigr).
   \]
   Every newly introduced quantifier is bounded, so \(E_\varphi\) is bounded.
5. The formation inductions at lines 156-169 correctly give
   \(\mathsf Q\vdash E_\varphi\to\varphi\) and
   \(\mathsf{PA}\vdash\varphi\to\exists eE_\varphi\).
6. The only nonlogical existence step is made explicit at lines 171-191.
   PA proves finite collection by induction on the bound: encode one witness
   at zero, extend the beta sequence at the successor, and bound each entry by
   the resulting code. The beta extension is primitive recursive and PA proves
   its defining equations/totality. This handles a different witness at every
   bounded index; it does not smuggle in countable choice or a single uniform
   witness.
7. Lines 193-212 turn bounded evidence into a PA proof code and derive
   \(\sigma\to\mathsf{Prov}_{\mathsf{PA}}(\ulcorner\sigma\urcorner)\).
   Lines 214-221 construct ordinary finite evidence from standard truth and
   derive the external Q clause.

The R2 counterexample
\(\exists z\,\forall u\le z\,\exists x\,\rho(z,u,x)\) is now handled:
the inner \(x\)-evidence is stored separately for every \(u\) in the beta
sequence. The theorem's proved-annex status is justified.

## F4 — accept-fixed: second-order base and transfinite recursion

handbook/parts/p05/reverse-mathematics.tex:55-66 now defines
\(\mathsf Z_2\) as \(\mathsf{RCA}_0\) augmented by full induction and full
comprehension, so the Q number axioms and set extensionality are retained.

The \(\mathsf{ATR}_0\) clause at lines 80-88 now has the stage-dependent
schema
\[
  Y_i=\{n:\theta(i,n,Y^{<i},\bar A)\},
\]
with \(Y^{<i}\) the coded earlier sections. It therefore permits arbitrary
arithmetical dependence on the current well-order stage, including
\(Y_i=\{i\}\), rather than merely iterating a fixed operator.

The repaired RCA schemes, WKL tree clause, ACA comprehension, strong
well-order comparability, and sequence-indexed well-founded-tree
comprehension remain exact. The calibration table, strict ladder, and Big Five
figure are licensed by these definitions and preserve their coding,
non-exhaustion, and no-cover caveats.

## F5 — accept-fixed: relation-first Rosser complexity

handbook/parts/p05/provability-logic-gl.tex:114-160 now separates:

- the metalinguistic primitive-recursive relation
  \(\operatorname{ProofRel}_T\);
- the primitive-recursive negation-code function;
- the primitive-recursive bounded-comparison relation
  \(\operatorname{RProofRel}_T\); and
- its chosen object-language \(\Sigma^0_1\) representative
  \(\mathsf{RProof}_T\).

Only after forming the primitive-recursive relation does the text define
\(\mathsf{RProv}_T(x)\equiv\exists p\,\mathsf{RProof}_T(p,x)\). Thus bounded
search is performed on the relation, not by negating an arbitrary
\(\Sigma^0_1\) representing formula. The claimed \(\Sigma^0_1\) complexity
now follows from representability. The strict comparison uses “no opposing
proof of code at most \(p\),” while the non-strict version uses “none below
\(p\)”; both orientations are correct. The Guaspari--Solovay \(R\) sentence
remains a bibliographic pointer, not a second local calculus.

## F9 — accept-fixed: Goodstein and hydra proof boundaries

Goodstein termination remains correctly tagged cited. The local descent
paragraph is now the explicit proof-boundary environment
def:p05-goodstein-descent-boundary at
handbook/parts/p05/independence-catalog.tex:139-160. It states the rank,
strict-decrease architecture, and exactly which recursive borrowing and
well-foundedness details remain in the cited sources. It no longer claims a
second complete local proof.

The hydra material has the same honest structure. Definition
def:p05-kirby-paris-hydra fixes the exact stage-dependent copying rule;
thm:p05-hydra is cited; and def:p05-hydra-boundary fixes the node rank,
propagation of strict decrease, and recursive-strategy calibration while
explicitly leaving the full induction/source proof to Kirby--Paris. The
mathematics and proof standing agree.

## Recheck of all earlier clean areas

- Q and PA axioms, both complete bounded-Q lemmas, compactness and downward
  Löwenheim--Skolem, numeralwise representability, coding, proof predicates,
  diagonalization, Gödel I, both Rosser branches, theoremhood undecidability,
  D1--D3, Löb, Gödel II, and Tarski are unchanged and remain correct at their
  complete/cited/sketch ceilings.
- The finite-distance block/order type, overspill and standard-cut example,
  Tennenbaum theorem, and effective interpretation transfer retain all prior
  hypotheses.
- The Paris--Harrington indicator route still separates the nonstandard cut
  construction from the coloring. Full-induction \(\mathsf{ACA}\), not
  conservative \(\mathsf{ACA}_0\), carries the uniform Ramsey upper
  calibration.
- The Goodstein recurrence begins at base 2, increments the base exactly once
  per stage, rewrites exponents hereditarily, fixes zero, and decreases the
  epsilon-zero rank.
- The Kirby--Paris hydra rule retains the original decapitated subtree and
  adds exactly \(s\) copies at stage \(s\); its sorted Cantor rank decreases
  for every head choice.
- The Tennenbaum method still obtains a nonstandard disjointness stage,
  internally codes the prime product, and computes the standard trace by the
  terminating quotient/residue search, yielding the forbidden separator.
- GL retains theorem-only necessitation, the correct frame direction,
  converse-well-founded unrestricted semantics, modal fixed points, the fixed
  PA realization, exact Solovay hypotheses, and a nonconflating modal/
  arithmetical dictionary.
- Presburger and Skolem arithmetic retain their exact reducts, decision
  methods, and published complexity boundaries.
- The Q/PA, independence, decidable-arithmetic, provability-dictionary, and
  reverse-calibration tables and the Big Five figure remain reader-visible.
- No rendered OPEN/unadmitted marker survives. The one proved body theorem and
  its annex item remain reciprocal.

## Final source/content conclusion

The finite-evidence proof now covers the entire closure-style
\(\Sigma^0_1\) class, including PA finite collection. The corrected
\(\mathsf Z_2/\mathsf{ATR}_0\) schemes, relation-first Rosser construction, and
Goodstein/hydra proof boundaries are exact. No repair introduced fallout in
the previously clean inherited or editorial mathematics. Administrative,
build, visual, generated-harvest, human, and user gates remain external.

accept
