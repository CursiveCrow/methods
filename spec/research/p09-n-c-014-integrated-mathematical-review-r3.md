ACCEPT

# Integrated N-c-014 mathematical and proof review, Round 3

## Scope and evidentiary boundary

I reviewed the actual LaTeX presentation
`handbook/parts/p09/presentations/n-c-014.tex` from line 1 through its current
end at line 1770, followed by the actual host
`handbook/parts/p09/logic-in-computer-science.tex` lines 836--946, including
the input at host line 937.  The reviewed presentation is the repaired
1770-line snapshot: in particular, its Elgot construction is the current block
at presentation lines 375--433, not an earlier formulation.

The source comparison used only the permitted five source notes, the
`N-c-014` and consolidated open-source portions of
`spec/research/p09-source-presentations-lot2-3.md`, and the relevant entries of
`handbook/bib/handbook.bib`.  No prior integrated N-c-014 review, admission
record, board record, ledger, chair record, Round 1 report, or Round 2 report
was opened or used.  No historical-source page had to be consulted: every
concrete issue material to this mathematical verdict was resolvable from the
permitted source notes and the actual LaTeX.  I did not inspect a manuscript
PDF, render, PNG, page image, crop, or other manuscript derivative, and I did
not run TeX, a build, a test, a checker, a repository script, a hash operation,
or automated validation.

This is therefore a mathematical/proof and internal-coherence verdict on the
actual source, at the source strengths expressly claimed by that source.  It
is not a compilation verdict, render verdict, independent source-language
certification, final-publication verdict, or human/user approval.

## Verdict

The integrated N-c-014 mathematical content is publication-admissible at its
explicitly bounded strength.  The host states the modern finite-word
MSO/regular-language equivalence and Rabin decidability theorem accurately;
the presentation then keeps the historically different source objects and
proof packages separate.  Every handbook-owned correction on which a claimed
theorem depends is stated as a correction, has the needed edge cases, and is
mathematically sufficient.  The repaired Elgot greatest-fixed-point block now
correctly handles the empty prefix and every possible first input letter, so
the defect that would otherwise break Lemma 6.1 and Theorem 8.1 is absent from
this snapshot.

The two explicitly open source reconciliations remain bounded source-register
obligations, not defects in the claims actually made here: the Büchi material
is asserted only at complete 1959-report-precursor strength pending comparison
with the registered 1960 journal body, and the Thomas material is asserted
only at complete May 1996 report-precursor strength pending comparison with the
registered 1997 chapter.  The manuscript never silently upgrades either body.

## Host theorems and integration

### Finite-word theorem

Host lines 836--850 state that, for a finite alphabet \(\Sigma\), a language
\(L\subseteq\Sigma^*\) is regular exactly when it is MSO-definable on word
positions with order, equivalently successor with definable endpoints.  This
is the correct modern theorem.  The integrated presentation supplies the
operative word signature rather than leaving “definable” as an unlabeled
length-only notion: presentation lines 1003--1021 define the position domain,
the unary letter predicates \(P_a^w\), singleton tracks, and successor tracks.
Over finite paths, successor is first-order definable from order, while order
is MSO-definable from successor; the endpoint formulas also behave correctly
on the empty word.  Thomas's Theorem 3.1 reconstruction at presentation lines
979--1027 supplies effective translations in both directions and separately
handles the empty word.  Thus the host statement is neither missing the letter
labels needed for non-unary alphabets nor substituting a one-way theorem.

Host lines 843--850 correctly mark the displayed theorem as a modern
formulation and deny that the identical sentence is printed in each named
historical source.  That qualification agrees with the actual source-specific
developments: Büchi's terminal-marker finite-predicate encoding, Elgot's
canonical finite-set encodings and design calculus, and Trakhtenbrot's broader
operator/topological package are not conflated.

### S2S theorem

Host lines 874--877 state decidability of the MSO theory of the full binary
successor tree.  Presentation lines 1069--1091 give Rabin's exact successor
structures and retain the source's distinction between the two orders;
lines 1153--1242 give both logical translations and the reduction of a closed
sentence to automaton nonemptiness; lines 1285--1584 reconstruct the actual
ordinary/dual complement and emptiness dependencies.  Thomas's later
game-theoretic route is separately attributed at lines 1616--1770 and is not
projected backward onto Rabin.  The host theorem therefore has the claimed
Rabin route and does not rely on the neighboring finite ranked-tree theorem at
host lines 879--929.

## Büchi precursor mathematics

### Types, semantics, and acceptance

Presentation lines 18--71 correctly distinguish the interpreted weak
second-order language, finite-set predicate variables, finite propositional
automaton data \((E,H,U)\), time predicates \(i,r,u\), and the behavior set
\(\beta(E,H,U)\).  The special-output identity
\[
U(Y)=U(H(Y,\bot^n))
\]
is pointwise in the current state and is exactly what is needed to propagate
an output value along an all-false input tail.  It neither silently assumes
\(U(\bot^m)=\top\) nor turns the output formula into an accepting-state set.

### Corrected analysis theorem

Lines 95--142 accurately expose why the report's printed finite-run witness is
insufficient: weakly quantified \(r\) is eventually all false, so the printed
tail formula would impose the unjustified condition
\(U(\bot^m)=\top\).  The one-bit counterexample at lines 113--119 satisfies
the printed special-output identity and accepts every special input while
refuting that witness formula.

The handbook-owned replacement at lines 121--140 is correct, including the
case in which the last true cutoff point is zero.  From \(j(0)\), finiteness,
and \(j(t+1)\rightarrow j(t)\), the witness \(j\) is a nonempty finite initial
segment with a last point \(h\).  The guarded recursion makes finite \(r\)
agree with the actual run through \(h\); the clause
\(\neg j(t+1)\rightarrow i(t)=\bot^n\) makes the real input false starting at
\(h\); and the boundary test \(U(r(h))\), together with the special-output
identity, propagates truth over the omitted real tail.  Conversely, for an
accepted special input, choosing \(h\) no earlier than both the input-extinction
point and the eventual-truth point, copying the actual run through \(h\), and
making the finite witness false afterward satisfies every displayed clause.
All clauses are local in \(t,t+1\), so the advertised existential local normal
form follows.

### Words, empty case, decision, and arithmetic boundary

Lines 144--169 state the terminal-marker encoding explicitly.  The empty word
has its marker at zero, nonempty words have the marker immediately after their
last data letter, and acceptance is read at the typed terminal state.  The
marker makes the finite-word assignment unambiguous even when a data letter is
itself \(\top^n\).

The decision proof at lines 171--190 includes both obligations needed for a
finite predicate: \(B(\bot,\bot)\) validates the infinite false tail, and a
finite state path reaches \(\bot\).  Loop deletion justifies the finite search
bound.  The treatment of the free-individual boundary includes \(x=0\) and
does not repeat the source's inconsistent prose convention.

Lines 192--230 also keep the arithmetic claims at their true strengths.  The
two displayed counterinstances show that the report's bit-occurrence formula
is false, including after the tempting one-character change.  The manuscript
does not claim the resulting unary-power signature equivalence; it assigns the
correct automatic/weak-monadic correspondence to the later bit-occurrence or
\(V_2\) signature while retaining only the sound decidability direction for
\((\mathbb N,+,\operatorname{Pw}_2)\).

## Elgot mathematics

### Finite-set encoding and both translations

Lines 239--330 correctly type the input alphabet, state set, deterministic
transition, run, accepting subset, empty-word convention, admissible
characteristic-column encoding, and the language \(T_r(A)\).  In the forward
direction, Boolean operations are relative to the regular admissible universe,
and existential deletion of a finite-set track is followed by the necessary
right truncation of exposed terminal zero columns.  In the reverse direction,
extra Boolean tracks encode a finite state, and the displayed start,
adjacency, and terminal conditions reproduce exactly an accepting run; the
empty word is separately restored.  Nothing identifies a formula, assignment,
column word, run, or language.

### Repaired greatest fixed point for design

The current lines 375--420 give a correct finite greatest-fixed-point
construction for the largest strongly \(A\)-extendable sublanguage of a
regular specification \(\gamma\).  The mathematical roles of all pieces are:

- \(M_0=A\times B\times D\) contains only triples whose current automaton state
  accepts the current nonempty prefix.
- The descending update at lines 386--393 retains a triple exactly when every
  possible next input letter has some output and accepting successor triple
  surviving the preceding stage.  Finiteness gives stabilization.
- The set \(I_\infty(a)\) at lines 396--400 is precisely the set of output
  letters whose first transition on input \(a\) enters a stable triple.
- The test \(d\in D\) is exactly the missing empty-prefix membership condition.
  The family of tests \(I_\infty(a)\ne\varnothing\) for every \(a\in A\) is
  exactly empty-prefix input-totality.  Requiring merely one surviving initial
  triple would not suffice; the actual snapshot does not make that error.
- The compatible triple sequences at lines 403--413 are genuine runs from
  \(d\), have every nonempty prefix in \(\gamma\), and retain a stable
  continuation for every next input.  Conversely, run triples belonging to
  any strongly extendable sublanguage satisfy both initial tests and survive
  every pruning stage by induction.

Consequently the constructed language is regular, is contained in \(\gamma\),
is strongly \(A\)-extendable, and is maximal.  Theorem 8.1 at lines 421--433
then follows with no empty-word or first-input gap: a total synchronous
transducer behavior is contained in \(\gamma\) exactly when this language is
nonempty, and a fixed output order gives an effective selection.  The vacuous
uniqueness convention when no realizing automaton exists is also logically
correct.

### Erratum-controlled infinite synthesis and negative boundary

Lines 443--542 give the exact restricted syntax needed for bounded windows;
they do not use “local” as an undefined substitute.  The finite-union
correction retains the relation arity, fields, prefix sets, and characteristic
stream type.  For \(n\ge2\), overlap of consecutive tagged windows forces one
constant tag.  For \(n=1\), the handbook-owned promotion
\[
\widehat R_j=R_j\times R_j,
\qquad
\widehat E_j=(E_j\cap R_j)\times R_j
\]
is exact: binary windows force every letter into \(R_j\), and the promoted
prefix condition retains precisely the original first-letter test, including
the empty-relation case.  The tagged construction may therefore be applied
without attributing this unary completion to the published erratum.

Lines 544--569 keep Elgot's undecidability boundary and version ownership
separate from the positive restricted algorithms.  In particular, fixed-machine
satisfaction is not conflated with existence of some satisfying machine, and
the 1962 publication, not the precursor report, owns the journal corrections.

## Trakhtenbrot mathematics

### Language and operator hierarchy

Lines 571--632 correctly distinguish the two source bodies, the interpreted
system \(\mathcal I\), its primitive grammar, its eliminable conveniences, the
syntactic upper/lower classes, and their separate semantic dependence
consequences.  Lines 634--687 then keep bounded anticipation, finite memory,
finite operator, the zero-anticipation automaton-realizable class, and weight
noninterchangeable.  In particular, the finite-memory update is allowed to
inspect a whole suffix, so finite memory alone supplies neither a causal state
after a prefix nor bounded anticipation.

### Portions, the weight counterexample, and definability

Lines 689--741 type one-coordinate and tuple portions coordinatewise and define
the residual maps \(T_u\) before they are used.  The identity
\((G_T)_{(u,v)}=G_{T_u}\) for the unique consistent output prefix and the empty
set otherwise follows directly from zero anticipation.  It also explains why
the residual maps are not the states of a broad future-dependent memory
presentation.

The handbook-owned counterexample at lines 743--779 is correct.  The two-state
equations give
\(q(t)=X(1)\mathbin{\mathsf{xor}}X(t)\), and the output equation then gives
identity output when \(X(1)=1\) and constant-zero output when \(X(1)=0\).
A one-state presentation would have to use the same suffix function at every
time; its forced time-one behavior contradicts time two on a word beginning
\(01\).  The original graph, constant-zero residual graph, identity residual
graph, and inconsistent empty portion are four distinct all-prefix portions,
with three nonempty portions, so neither the printed \(k\) bound nor a
\(k+1\) patch is available from broad weight.

Lines 784--836 correctly preserve the positive results.  A nonempty
homogeneous set has at least one permitted next bit at every nonempty residual;
the choice-stream construction produces exactly its closure, hence the set
itself when it is closed.  A total map cannot have empty image, so the empty
set is correctly handled by a contradictory initial clause rather than by the
nonempty covering construction.  The conditional-algorithm qualifier remains
attached to residual-emptiness decisions.

### Synthesis and finite words

Lines 838--896 distinguish a formula that defines exactly an operator graph
from a relation merely solved by an operator, and distinguish existence of one
solution from a general solution parametrizing all and only solutions of the
named class.  The fixed-lookahead theorem is stated separately for each fixed
bound and is not inflated to one uniform parametrization over all bounds.

Lines 898--960 type the induced finite-word maps and their prefix compatibility.
The empty-language objection to the printed enumeration converse is decisive:
a total length-preserving operator has a nonempty image at every positive
length.  Adding nonemptiness to prefix closure and proper extendibility supplies
both shorter prefixes and arbitrarily long extensions, hence a member at every
positive length.  The special-beginning condition is also stated as an
eventually-zero boundary, not as an arbitrary finite prefix.

## Rabin mathematics

### Structures, ordinary acceptance, and logical translations

Lines 1036--1151 define the source's root, two orders, successors, predecessor,
arbitrary rooted valued subtrees, move table, run, infinitely-recurring-state
operator, initial states, and Muller-family acceptance with the exact quantifier
order \(\exists r\,\forall\pi\).  The later pair sequence is expressly excluded
from ordinary acceptance.  The later Meyer lower bound is used only to withdraw
Rabin's elementary-recursive worst-case qualification; it does not disturb
decidability or effectivity.

Lines 1153--1242 correctly give the track bijection, principal-formula normal
form, finite-witness lift, Boolean and projection dependencies, converse run
encoding, and sentence-to-nonemptiness reduction.  The worked formula
\(\exists x(x\in A\land r_0(x)\in B)\) has exactly the stated two-track
meaning, and a sufficiently deep finite frontiered initial subtree can label
both the witness node and its child.

### Product, dual acceptance, and zero-length case

The product at lines 1244--1283 is type-correct.  Its first coordinate follows
the deterministic Muller word run on the tree-run state sequence, and
projection of the infinitely recurring product pairs recovers exactly the
infinitely recurring first-coordinate states because the second coordinate is
finite.  Determinism supplies a coherent common history before branches split.

Lines 1285--1332 give dual acceptance with the exact
\(\forall r\,\exists\pi\) implication, including vacuous truth when no run
exists.  The handbook-owned zero-length completion at lines 1334--1357 is
exact.  For \(\Omega^\dagger=((S,S))\), every infinite path map into finite
nonempty \(S\) has a nonempty infinitely recurring set; that set cannot both
meet and avoid \(S\).  Hence its path type is impossible and the dual language
is precisely the no-rooted-run language, as for the empty pair sequence.

The subsequent marked-obligation, well-founded-dependency, two-half-step, and
positive-length induction dependencies at lines 1359--1465 are stated in the
right order.  Transfinite induction is assigned only to the well-founded
stratification and the converse construction in Lemma 3.11, not used as a
substitute for the finite-state proof architecture.

### Finite trees and emptiness

At first use, lines 1195--1209 define the terminal-node frontier and define
“frontiered” as a property of a finite predecessor-closed rooted set, explain
why predecessor closure alone is weaker, and identify the later lift.  Lines
1403--1456 then type the finite valuation and external frontier value
\(f\notin S\).  The absence of mixed \((f,s)\) transitions is not silently
repaired; an otherwise valid frontiered input with one frontier child and one
internal child simply has no run at that node.

Lines 1467--1584 reproduce Rabin's actual emptiness route rather than inserting
Thomas's later basis theorem.  Erasing labels by taking the union of move
tables is exact: every original run is a one-letter run, and every one-letter
run chooses at each node a witnessing original label and so determines an
original valuation.  Complement followed by the dual conversion therefore
reduces original nonemptiness to the stated one-tree dual question.

The restricted-table definition at lines 1505--1513 correctly constrains only
states strictly below the root.  The finite table-run at lines 1515--1530 is
also correctly distinguished from both an infinite run and the earlier
external-frontier-value automaton run.  The two handbook-owned empty branches
are necessary and sufficient:

- when \(H=\varnothing\), the reduction is the direct shorter-pair question;
- when \(U_0=\varnothing\), the universal finite-run condition says that the
  chosen finite tree admits no rooted finite table-run, and König compactness
  makes such an obstruction equivalent to absence of an infinite run.

The base property is expressible in weak monadic logic over finite node sets;
that external finite-tree decision theorem does not turn the full infinite-tree
theory into weak logic.

## Thomas report-precursor mathematics

### Finite words

Lines 979--1027 give a finite nonempty state set, a typed transition relation,
an \(n+1\)-state run on a length-\(n\) word, and final-state acceptance.  The
automaton-to-formula construction handles the final letter and separately adds
the needed nonempty-position guard exactly when the automaton rejects the empty
word.  The reverse construction defines singleton and successor tracks and the
letter predicates, then uses complement, union, and nondeterministic track
projection with the correct quantifier roles.

### Tree automata, empty chains, and deadlock completion

Lines 1616--1643 correctly state Muller tree acceptance with one global run and
all paths.  Lines 1645--1670 define the strict chain and its pair condition.
For an empty chain the existential pair test is false, so every path rejects;
this is the correct endpoint when equal adjacent pairs have all been removed.
The order-vector-with-hit is identified as finite state memory and is not
confused with an input tree or a run.

The handbook-owned completion at lines 1672--1705 is correct and proof-critical.
Every missing \((q,a)\) fiber is sent to two copies of a fresh state \(\bot\),
and \(\bot\) loops on every letter.  Since \(\bot\) belongs to no \(F_i\), a
path that reaches it satisfies no chain pair.  Thus every original successful
run remains, no successful run can use an added transition, the recognized
language and strict chain are unchanged, and every game position has nonempty
finite outdegree.

Lines 1706--1735 then use the completion within the exact game hypothesis.
The nodewise finite instruction functions encode a Pathfinder strategy without
making it depend only on the input letter globally: the instruction label may
vary from node to node.  The complement automaton depends only on the source
automaton, and the empty-chain game is the correct trivial Pathfinder win.

Lines 1737--1763 correctly separate “regular input tree” from an acceptance
mode.  After input-label guessing, a memoryless winning strategy in the finite
game supplies a finite deterministic label generator.  Language preservation
under completion transfers both emptiness and the regular-member conclusion to
the original possibly partial automaton.  Formula induction then uses effective
complement only after the same completion, and the sentence case reduces to
successful-run existence.  This proves the claimed later S2S route without
replacing Rabin's source proof.

## Technical-name rule

The actual snapshot satisfies the supplied technical-name rule for every
handbook-introduced distinction material to this verdict.

- \(I_\infty(a)\) (lines 396--420) is defined as a subset of possible first
  output letters, is needed to state input-totality at the empty prefix, differs
  from the stable triple set \(M_\infty\), and is used immediately in the two
  initial tests and maximality proof.
- The residual stream map \(T_u\) (lines 720--741) has a typed eliminable
  definition, is identified as an operator rather than a state, differs from a
  broad future-dependent memory state, and is required by the graph-portion
  correction and counterexample.
- \(\Omega^\dagger\) (lines 1334--1357) is an exactly defined one-pair sequence,
  not a new acceptance semantics, differs from the empty sequence only in
  representation, and is needed to enter the source's positive-length
  induction.
- “Finite table-run” (lines 1515--1530) has an exact map type and local
  transition clause, is distinguished from both neighboring run notions, and
  is used in the repaired emptiness base.
- \(\mathcal A^\bot\) (lines 1672--1705) is the exactly specified completed
  chain tree automaton, not a game or run; it differs only on missing
  state-letter transitions, is necessary for the nonempty-outdegree premise,
  and is used throughout the later game construction.

The source-owned names are likewise introduced with their standing and actual
use: special predicate/output/behavior, admissible word, strongly
\(A\)-extendable word, anticipation/memory/finite operator, portion and
homogeneity, solution and general solution, automaton-enumerable/decidable
language, ordinary and dual tree acceptance, frontieredness, and regular input
tree are not treated as interchangeable labels.  No hypothetical new
mathematical object is named in place of an owed definition or proof.

## Source and bibliography boundaries

The bibliography entries used by the presentation have the correct roles and
do not silently transfer locators between versions: `Buchi1959WeakReport` and
`Buchi1960` are separate; `Elgot1961`, `Elgot1959Report`, and
`Elgot1962Errata` are separate; the two Trakhtenbrot bodies retain their
distinct official English titles and page ranges; `Rabin1969` and the later
`Meyer1975Complexity` have separate roles; and `Thomas1996Report` is separate
from `Thomas1997`.  The McNaughton theorem is identified as an external
word-automata dependency rather than reproduced or silently reassigned.

The explicit open reconciliations are mathematically harmless at the stated
strength:

- presentation lines 8--16 and 971--973 restrict the Büchi reconstruction to
  the complete 1959 precursor and expressly leave the 1960 journal comparison
  open;
- presentation lines 1029--1034 and 1765--1770 restrict every Thomas locator
  to the complete May 1996 report and expressly leave the registered 1997
  chapter comparison open.

No theorem in the reviewed snapshot requires those unreconciled bodies to be
identical to the acquired precursors.

## Separate verification categories

- **Mathematical proof and internal coherence:** accepted at the bounded
  strengths described above.  The literal definitions, quantified claims,
  constructions, edge cases, repairs, and theorem dependencies checked in this
  report support the host conclusions.
- **Source fidelity:** checked only against the permitted source-note evidence
  and actual LaTeX.  The two precursor/final-version reconciliations remain
  explicitly open, and no Russian-language-specialist certification is made.
- **Compilation/static validation:** not performed and not implied.
- **Rendered-page or visual-layout inspection:** not performed and not implied;
  no manuscript derivative was inspected.
- **Agent review:** this file records one fresh mathematical/proof review of
  the repaired actual-LaTeX snapshot.
- **Human or user review:** not performed and not implied.

There is no mathematical must-fix finding on this snapshot.

REGISTER STATUS: OPEN
