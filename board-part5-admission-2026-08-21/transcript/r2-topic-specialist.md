# Round 2 blind repair verification — arithmetic/proof-theory topic specialist

## Verdict

**Do not yet admit the repaired Part V at source/content level.** The repair
pass closes R1 F1, F2, F3, and F7; supplies the in-scope body/annex apparatus
from F6; and supplies the registered Paris--Harrington, Goodstein/hydra,
Tennenbaum, and Rosser-pointer material from F5. The new mathematical objects
and most theorem statements are correct.

Three substantive residuals remain:

1. the newly proved Sigma-one-completeness result begins with a prenex
   conversion that does not handle unbounded existential quantifiers beneath
   bounded universal quantifiers in the handbook's closure-style
   \(\Sigma^0_1\) class;
2. the repaired \(\mathsf{ATR}_0\) recursion schema omits the stage variable
   from the defining formula; and
3. the new Rosser entry builds bounded comparisons from the fixed
   merely-\(\Sigma^0_1\) formula \(\mathsf{Proof}_T\), which does not make the
   displayed predicates \(\Sigma^0_1\) as claimed.

There is also one proof-status cleanup: Goodstein termination is tagged cited
but immediately followed by a paragraph labeled “Proof” whose load-bearing
descent lemma is only sketched.

I re-read only my R1 transcript and the current live Part V body/annex route.
I did not read another seat's transcript, edit manuscript/control/test/generated
files, run a build, or run tests.

## R1 finding dispositions

### F1 — accept-fixed

The rendered OPEN/unadmitted notices are gone.
handbook/parts/p05/models-and-interpretability-supplement.tex:18-26 now gives
ordinary attribution, separately-authored standing, source control, and the
annex location. handbook/annex/p05/depth-completion-supplement.tex:12-15 gives
the reciprocal note for a completed proof. The routes likewise describe
separately authored/completed material without reader workflow prose. This is
real content repair, not notice deletion alone. F8 below concerns the new proof.

### F2 — accept-fixed as to the objects and mathematics

The Goodstein family is unique at
handbook/parts/p05/independence-catalog.tex:94-117:

- hereditary base \(b\) recursively rewrites every exponent;
- \(g^m_0=m\);
- stage \(s\) uses base \(s+2\), replaces it by \(s+3\), subtracts one when
  positive, and leaves zero fixed.

The R1 \(m=4\) ambiguity is gone. The rank \(o_b(n)\) obtained by replacing
\(b\) with \(\omega\) is below \(\varepsilon_0\), and
\[
 o_{b+1}(B_{b\to b+1}(n)-1)<o_b(n)\qquad(n>0)
\]
is the correct descent. Recursive borrowing lowers the first changed
Cantor-normal-form position, so an infinite positive sequence would yield an
impossible descending ordinal sequence. F9 concerns only status presentation.

The Kirby--Paris object is now exact at lines 163-179: tree, stage, selected
leaf, root-parent case, grandparent, retained decapitated parent subtree, and
exactly \(s\) additional copies are fixed. The rank at lines 188-198 is
correct. Deleting a head lowers the parent rank; at its grandparent any finite
multiple of the new \(\omega^{\alpha'}\) term remains below the old
\(\omega^\alpha\) term; strict decrease propagates to the root. The theorem
correctly separates arbitrary external strategies from the first-order
recursive-strategy statement.

### F3 — accept-fixed

handbook/parts/p05/provability-logic-gl.tex:45-59 fixes only PA and its exact
instantiated standard provability predicate; it covers no generic \(T\).
The Solovay theorem at lines 86-101 quantifies over exactly those realizations
and records the ambient \(\mathcal N\models\mathsf{PA}\) basis for consistency
and \(\Sigma^0_1\)-soundness. Changing theory, numbering, or predicate is
expressly excluded. The frame orientation, converse-well-foundedness, modal
fixed-point side condition, and proof boundary are coherent.

### F4 — still-open, narrowed to the \(\mathsf Z_2/\mathsf{ATR}_0\) definitions

Most of F4 is fixed. handbook/parts/p05/reverse-mathematics.tex:15-53 gives
the two-sorted signature, Q number axioms, set extensionality,
\(\Sigma^0_1\)-induction with number/set parameters, and the exact
\(\Delta^0_1\)-comprehension premise/freshness condition. The table at lines
102-153 now uses exact coded representatives: countable rational-open-cover
Heine--Borel, injection ranges, strong well-order comparability, and
sequence-indexed well-founded-tree sets. Those are the standard reversals.

Two definition defects remain:

- At lines 55-66, \(\mathsf Z_2\) is said to “consist of” full induction and
  comprehension, but the axiom clause does not include the Q number axioms and
  set extensionality from \(\mathsf{RCA}_0\). Define \(\mathsf Z_2\) as that
  common basic theory with full induction/comprehension, or as
  \(\mathsf{RCA}_0\) augmented by those schemes.
- At lines 80-88, the \(\mathsf{ATR}_0\) clause requires
  \[
    Y_i=\{n:\theta(n,Y^{<i},\bar A)\},
  \]
  but \(i\) is absent from \(\theta\). Standard arithmetical transfinite
  recursion permits \(\theta(i,n,Y^{<i},\bar A)\). As written it only iterates
  a stage-independent operator and cannot directly state the elementary
  recursion \(Y_i=\{i\}\). Add the stage argument to the formula and displayed
  section equation.

The ATR table row and strict-ladder theorem become locally licensed once that
schema is corrected.

### F5 — still-open only through the repaired Rosser entry

The formerly missing registered content is present:

- provability-logic-gl.tex:114-139 gives the Guaspari--Solovay \(R\) pointer;
- independence-catalog.tex:37-61 supplies the Paris--Harrington
  indicator/nonstandard-cut architecture;
- lines 63-92 distinguish arithmetically conservative \(\mathsf{ACA}_0\) from
  full-induction \(\mathsf{ACA}\), and correctly assign the uniform Ramsey
  upper calibration only to the latter; and
- the Goodstein/hydra ceiling is present and mathematically correct.

The Rosser entry nevertheless makes a false syntactic-complexity inference.
At provability-logic-gl.tex:114-128 it defines
\[
 \mathsf{RProv}_T(x)\equiv
 \exists p\bigl(\mathsf{Proof}_T(p,x)\land
   \forall q\le p\,\neg\mathsf{Proof}_T(q,\mathsf{Neg}(x))\bigr)
\]
and says this and the witness-comparison variants are \(\Sigma^0_1\). But
def:fixed-proof-predicate fixed \(\mathsf{Proof}_T\) only as a particular
\(\Sigma^0_1\) formula representing the primitive-recursive proof relation.
If \(\mathsf{Proof}_T(q,y)\equiv\exists w\,\delta(q,y,w)\), bounding \(q\)
does not bound \(w\); after negation the display has an unbounded universal
component and need not be \(\Sigma^0_1\).

The exact repair is to define the underlying primitive-recursive relation
\[
 \mathsf{RProofRel}_T(p,x)\iff
 \mathsf{ProofRel}_T(p,x)\ \&\
 \forall q\le p\,\neg\mathsf{ProofRel}_T(q,\mathsf{Neg}(x)),
\]
then choose a \(\Sigma^0_1\) representative by the representability theorem
and define \(\mathsf{RProv}_T(x)\equiv\exists p\,\mathsf{RProof}_T(p,x)\).
Alternatively supply a bounded proof formula and prove equivalence to the
fixed predicate. The strict/non-strict \(q\le p\) versus \(q<p\) orientations
themselves are correct.

### F6 — accept-fixed for the in-scope body/annex apparatus

The live body now supplies:

- A-053 at models-and-interpretability-supplement.tex:28-58;
- A-054 at independence-catalog.tex:276-325;
- A-055 at decidable-arithmetics.tex:81-115;
- A-056 at reverse-mathematics.tex:102-146;
- A-057 at provability-logic-gl.tex:141-184; and
- A-128 at reverse-mathematics.tex:170-199.

The GL body also points to a complete local rule sheet and states theorem-only
necessitation exactly. Because this round was expressly limited to Part V
body/annex bytes, the registry sheet itself was not re-audited; that
registry-owned A-012 byte check is not evidence for or against this body.

### F7 — accept-fixed

models-and-interpretability-supplement.tex:256-259 now points only to the
external Visser survey and says no local interpretability-logic calculus is
introduced. The false destination to the independence chapter is gone.

## New direct-repair findings

### F8 [blocker] [open] The complete Sigma-one annex begins with an invalid normal-form conversion

- **Location:** body complete status at
  handbook/parts/p05/models-and-interpretability-supplement.tex:139-160;
  conversion at handbook/annex/p05/depth-completion-supplement.tex:19-37;
  later use at annex lines 130-155.
- **Evidence:** the annex says variable renaming, negation pushing, and pulling
  existentials through only \(\land,\lor\), while bounded quantifiers remain in
  the matrix, produces a bounded \(\delta\) and a purely logical proof
  \(\sigma\leftrightarrow\exists\vec x\,\delta\) for every closed
  \(\Sigma^0_1\) sentence. This fails for the handbook's closure-style class,
  which is closed under marked bounded quantifiers. For example,
  \[
    \exists z\,\forall u\le z\,\exists x\,\rho(z,u,x)
  \]
  is \(\Sigma^0_1\) for bounded \(\rho\). The inner witness may depend on
  \(u\). Leaving the bounded universal in the matrix leaves an unbounded
  existential there; pulling one \(x\) in front changes the formula. A single
  witness requires a coded finite witness sequence/bounded collection, not the
  pure logical identities at lines 23-29.
- **Harm:** equations (1) and (5), hence the formalized clause and external Q
  conclusion at lines 130-155, are not proved for the theorem's full domain.
  The theorem is true and the bounded-formula/proof-code induction at lines
  39-128 is otherwise well designed, but the complete status overstates it.
- **Correction:** either restrict the body theorem to an already-prenex
  syntactic subclass, or handle the full closure class. For the latter, prove
  external Q completeness by structural evaluation with actual standard
  witnesses, and formalized PA completeness by structural proof-code
  constructors or a PA-verified bounded-collection/\(\beta\)-code conversion
  allowing a different witness per bounded index. Do not call that conversion
  pure logic or Q-provable without the coding principle.

### F9 [must-fix] [open] A cited Goodstein theorem is followed by a locally labeled but incomplete proof

- **Location:** handbook/parts/p05/independence-catalog.tex:135-155.
- **Evidence:** thm:p05-goodstein-termination is tagged cited=Goodstein1944,
  meaning the source carries the proof. Lines 139-155 then begin “Proof” and
  claim descent (G), but only assert the structural induction and recursive
  borrow cases. This is correct proof architecture, not a complete local proof.
- **Harm:** the reader gets incompatible evidence signals: a cited theorem and
  a local paragraph typographically claiming to be its proof.
- **Correction:** relabel the paragraph “Proof architecture” or an explicit
  proof-boundary/commentary and retain cited status; or move a genuinely
  complete induction to a reciprocal annex and change the theorem to proved.

## Deep checks that came back clean

### Paris--Harrington and ACA

The relative-largeness condition remains exact. The indicator entry separates
the cut-producing device from the coloring and records the right contradiction
architecture: a proper PA initial segment contains the parameters/coloring code
but omits the least witness. The repair correctly distinguishes
\(\mathsf{ACA}_0\), conservative over PA for arithmetic sentences, from
full-induction \(\mathsf{ACA}\). Full induction supports uniform induction on
Ramsey dimension, and the infinite-to-finite compactness route yields
Paris--Harrington. No false \(\mathsf{ACA}_0\) upper bound survives.

### Goodstein and hydra

Starting base, hereditary recursion, schedule, zero convention, and universal
closure are exact. The epsilon-zero and Cantor-rank objects are correctly
typed. Every positive Goodstein step decreases its ordinal. The hydra rule
matches Kirby--Paris, and its ordinal decreases for every head choice. The
theorem correctly separates external arbitrary strategies from the
first-order recursive-strategy statement.

### Solovay and GL

GL's K axiom, theorem-only necessitation, Löb axiom, Kripke direction, finite
transitive irreflexive frames, converse-well-founded unrestricted formulation,
and modal fixed-point condition are exact. Realizations and completeness are
confined to the fixed PA predicate with the ambient standard-model hypothesis.
The dictionary maps D1--D3, Löb, fixed points, and Solovay without conflating
accessibility and proof codes.

### Tennenbaum

independence-catalog.tex:208-243 now gives the full method. Overspill provides a
nonstandard stage preserving internal disjointness; the internal prime product
has a standard trace containing \(A\) and avoiding \(B\). Standard primes and
numerals are computable from the transported operations. Simultaneous search
for a quotient and one of finitely many standard residues terminates by PA
division with remainder for a fixed standard prime. Divisibility therefore
gives the forbidden computable separator.

### Reverse equivalences

RCA's repaired schemes include parameters/freshness. WKL is stated for coded
binary trees and the countable rational-open-cover Heine--Borel reversal.
Injection-range existence is the standard ACA reversal. Strong comparability
of coded well-orders is the standard ATR representative once F4 is repaired.
Sequence-indexed well-founded-tree sets are the standard
\(\Pi^1_1\)-comprehension representative. The strict ladder/figure retain the
non-exhaustion and no-cover caveats.

## Precise repair checklist

1. **P0:** repair the full-\(\Sigma^0_1\) normal-form step or narrow the theorem
   domain, then re-audit equations (1), (4), and (5) before retaining the
   proved-annex status (F8).
2. **P0:** change ATR to
   \(Y_i=\{n:\theta(i,n,Y^{<i},\bar A)\}\) and make \(\mathsf Z_2\)
   explicitly extend the common basic theory (F4).
3. **P0:** define the primitive-recursive Rosser proof relation first and then
   choose its \(\Sigma^0_1\) representative (F5).
4. **P1:** relabel the Goodstein paragraph as cited proof architecture or move
   a complete proof to an annex (F9).
5. **External to this round:** verify the registry-owned A-012 GL sheet; the
   instructed body/annex scope did not authorize that byte check.
6. Re-run the focused source/content review. Administrative, build, visual,
   generated-harvest, human, and user gates remain separate.

## Scope conclusion

R1 F1, F2, F3, and F7 are **accept-fixed**. F6 is **accept-fixed for the
in-scope Part V body/annex apparatus**, with registry A-012 not checked by
instruction. F4 and F5 are **still-open only in the narrowed forms above**.
New F8 blocks complete-proof acceptance; F9 is an exact proof-status
correction. All other named repairs and the unchanged inherited core are clean
at their declared source/proof ceilings.
