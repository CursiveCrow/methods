# C7 author handoff: constructive GPSS complementation

Root integration: the body and annex are connected immediately after the
special-normal-form pair. The predecessor's negation boundary and the
main GPSS clauses now state the proved endpoint scopes directly and link
the full discrete future theorem. Historical source omissions and referral
numbering remain provenance, rather than instructions for the reader to
repair a missing active proof.

Date: 8 September 2026. Author: `/root/kamp_lemma7_author`.
The bounded and future-ray complement constructions are fully written,
with an explicit proof that the broader formal-left-endpoint reading is
false in the unchanged future-label class. Independent reviews remain deferred.

## Saved files

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/gpss-decomposition-complement.tex` | 261 | 12620 | `DD0E6B5F12DAB2F806065A3A2C7C146FD0175A7F5E5595BF24E95EB70B1BE492` |
| `handbook/annex/p09/gpss-decomposition-complement.tex` | 806 | 24573 | `13C897FC7DE8D9D30E2F8280CC68AEEC2C1C4B9515DF78EF1276FAF2E52A71DF` |

All three owned paths were unused at dispatch. Only these two files and
this note were written. All prior author files and shared files were preserved.

Primary source: the held GPSS 1980 paper, printed pp. 170–171, including the
decomposition definition, Main Lemma, Proposition 2.4 and entire event-expression
outline. These pages were personally reread. Held PDF:
`tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf`, SHA256
`2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2`.
The research/PDF instructions were personally read. No unsuccessful external
search was replayed; no external full proof was substituted for the source.

The exact existing decomposition, future-label and suffix definitions were
read in the actual preceding LaTeX pair, with hashes:
body `FC8A0651DB37E774DF630821F9AF07AB9C9C545A6A0DAEBC9089E9A0AD341F72`;
annex `C722ACBC9C74C6CB26DB66EB77EF624D40E06D77C35309D5E69D120FBAF7707B`.

## Constructive bounded-interval proof

1. Bounded intervals in discrete complete orders are proved finite by iterating
   the unique successor and applying completeness and the predecessor of the
   alleged supremum if the iteration never reaches the upper endpoint.
2. The auxiliary event grammar has strict First/Last selectors and singleton
   Test selectors. It has complete partial semantics: undefined bounds,
   unordered bounds, empty occurrence sets, and false tests are all explicit.
   Undefined is not a point. Tests are applied only to internal event terms,
   so no label is introduced at the external endpoints.
3. A canonical positive-chain test uses future-only suffix-viability labels
   built by explicit nested strict U. First selectors are still bounded by the
   actual upper endpoint. The selected chain is proved valid and coordinatewise
   earliest whenever any valid bounded chain exists. The initial gap is checked
   by a last-failure selector; no current-point label at the lower endpoint is
   assumed.
4. For a rank-r decomposition, take the last failure of its final gap label.
   If absent, the canonical positive chain decides the whole formula. If
   present, split at that point in every possible gap position and every
   possible equality with an internal witness. Prefix subproblems have smaller
   rank; remaining suffix chains use the canonical test. Gap positions retain
   the gap label at the cut, while equality positions retain only the required
   point label. This is the complete finite determining-list recursion.
5. Every status assignment and weak order on the finite event values is
   explicitly compiled. Defined extrema give point labels and absence on the
   relevant interval; undefined extrema with good bounds give absence on the
   whole search interval. Tests give equality plus a positive point label or
   a negative point label. Universal interval labels are transferred to all
   merged gaps and all covered inserted points. This gives one exact GPSS
   decomposition per consistent case, with all auxiliary terms eliminated.
6. Retain the cases whose finite Boolean decision is false. This produces
   precisely `(x<y) AND NOT D(x,y)`, with equality/undefined cases and empty
   intervals included. No satisfiability oracle is used to discard label
   contradictions; such output words may remain unsatisfiable.

All event labels are finite L(U) formulas, independent of the endpoint
parameters. A Last event is metalinguistic bounded selection, not a past
temporal operator inserted into a point label. The finite node recurrence
in the annex bounds new event nodes with shared endpoint subterms; it does
not claim a bound on expanded label syntax.

## Future rays and complete discrete future result

For `D(x,+infinity)` with actual x, use its previously proved L(U) translation
B and negate it. Its outer Boolean skeleton contains strict future modalities
and constants, with no exposed current atom. At a nonlast point, its immediate
successor s evaluates the explicit unfolded label L_E. The output word chooses
s by a false first-gap label, puts L_E at s, and has a true final gap. If the
negated formula is true at a last point, add the zero-point false-gap word.
This handles all source cofinal conjuncts through their exact `F psi AND GF psi`
translation. The method is a proved alternate construction for this endpoint
case; it does not rely on an unbounded last-occurrence term.

The bounded and ray results complete both signs of every regional stage with
an actual lower endpoint. Positive closure supplies the constructor step;
finite intersections of single-word complements handle a negated disjunction.
The previous present/future normal form and suffix translation then prove
Theorem 2.2 at every point of every discrete complete model. Relativizing
arbitrary first-order quantifiers to `>= x` at x = 0 in omega-models proves
the exact Theorem 2.1 corollary. No all-points claim for unrestricted formulas
on omega, and no Lin-wide or arbitrary-complete complement theorem, is inferred.

## Necessary endpoint correction: prefix and whole-order closure fail

The exact future-labelled prefix grammar is not closed under complement,
even on Z. Its legal one-point word
`D(-infinity,y) = exists z<y forall u<z q0(u)`
has point label true, first gap q0, final gap true. The whole-order version
with unrestricted z is legal as well. Their complements have no finite
disjunction of decompositions in the same future-label class.

The proof fixes y = 0 and the nonnegative future tail true, and varies q0(-n)
as an arbitrary binary sequence; every other predicate is fixed false. At a
fixed integer, any future-only label depends on finitely many varying bits.
For a fixed decomposition witness tuple, all its conditions therefore form
an intersection of closed cylinder sets. Existential quantification over
countably many integer tuples gives a countable union of closed sets.
Future-cofinal conditions in whole-order words are constant on the fixed-tail
slice, so the same conclusion holds there.

The displayed D holds exactly when there are finitely many zero bits. Its
complement has infinitely many zeros. The annex gives an explicit nested-cylinder
diagonal proving that this latter set is not a countable union of closed sets.
Thus the failed formal-left-endpoint cases are resolved by a proved counterexample,
not left as an unproved stronger claim or replaced by past-dependent labels.
This does not obstruct Theorems 2.1–2.2, whose future construction has an actual
lower endpoint. A past-dual or coinitially enlarged grammar is a different task.

## Reciprocal results and integration

| Body result | Annex item |
| --- | --- |
| `thm:p09-gpss-finite-bounded-interval` | `annex:p9.gpss.finite.bounded.interval` |
| `thm:p09-gpss-canonical-prefix` | `annex:p9.gpss.canonical.prefix` |
| `thm:p09-gpss-determining-events` | `annex:p9.gpss.determining.events` |
| `thm:p09-gpss-bounded-complement` | `annex:p9.gpss.bounded.complement` |
| `thm:p09-gpss-suffix-complement` | `annex:p9.gpss.suffix.complement` |
| `thm:p09-gpss-prefix-complement-obstruction` | `annex:p9.gpss.prefix.complement.obstruction` |
| `thm:p09-gpss-discrete-future-completeness` | `annex:p9.gpss.discrete.future.completeness` |

Root should input this pair immediately after `gpss-special-normal-form`.
Replace the earlier `def:p09-gpss-negation-boundary` content with the direct
completed bounded/future-ray result and its link to
`thm:p09-gpss-discrete-future-completeness`. Its old requirement to complement
every formal-endpoint configuration in the unchanged future-label grammar
must be replaced by the exact obstruction theorem above. In `n-c-012.tex`,
the Main Lemma and Proposition 2.4 paragraphs should state the actual-lower-endpoint
scope of the completed future construction; the source outline remains
historical provenance in research notes. Link the Theorem 2.1/2.2 statements
to the new complete proof, while retaining their different evaluation scopes.

New local notation: W and rank r for a labelled word; First_A, Last_A, Test_A,
Def and undefined statuses; future formulas Lambda_i; canonical event values
mu_i and tests V_m/V^j; prefix words W_j; final-gap event ell; decision T_W
and finite list E_W; node bound B(r); compiled cases C_i; suffix Boolean value
e_last and unfolded label L_E; binary sequence w, cylinders, closed sets C_n
and the infinitely-many-zeros class I in the endpoint counterproof. All event
terms and statuses are metalinguistic and eliminated from output formulas.
The counterproof uses the GPSS predicate q0, not Kamp's differently named P0.

## Author read-back and remaining obligations

The full mathematical body and annex were read back as one authoring batch;
the small truncated display extent was separately read to completion. No
scoped scanner, acceptance check, test, build, manuscript render or independent
review was run in this block, following the latest workflow instruction.
The line counts and hashes above are handoff metadata, not acceptance evidence.

The requested discrete-complete future complement component is fully written.
The broader formal-left-endpoint interpretation is corrected by its explicit
failure theorem. Remaining distinct obligations are the source's separation
Theorem 2.3/direct syntactic presentation, arbitrary complete orders requiring
nonattainment/cut boundary constructions, and arbitrary-order gap operators and
Theorem 2.5. The exact external [SS]/[G2] manuscript bodies were not newly
acquired, and no claim of reproducing them is made. Consolidated independent
review and admission remain deferred until writing and corrections finish.
