# Independent topic review: direct PA checker and finite abduction

Date: 7 September 2026, America/Los_Angeles. Reviewer: `/root/pa_abduction_topic_review`.
Review began at 00:10 UTC on 8 September; the blind report was completed within the assigned 35-minute block.

## Verdict and scope

**P5 topic/mathematical verdict: PASS for the stated graph-meaning, internal-library, D1 and D2 results.** The numerical descriptions implement the specified direct checker, and the internal joining proof works for its selected description graphs. I found no mathematical counterexample or missing induction step that blocks those results. One local formula/code notation clarification is recorded below.

**P16 topic/mathematical verdict: PASS for all five stated results, the exhaustive procedure and the six complete example families.** All stated inconsistent and empty input cases are included.

These are findings on the frozen body/annex content and the prerequisites inspected below. D3, the evidence-to-proof builder, the standard provability-logic consequences requiring D3, and broader abduction remain explicitly open. Publication production and formal admission are separate obligations. This report issues no admission.

The governing `spec/EDITION-2026-CONTRACT.md` was read completely. I read no other current review or verdict, spawned no agent, wrote no test, and built or rendered no manuscript PDF. The only repository file written by this reviewer is this report. The author/source note for P16 was used to locate the held source; its conclusions were checked against the actual body, annex and source pages. A progress checkpoint was sent to the lead before 15 minutes.

## Frozen artifacts and actual reading

The four target hashes matched the assignment at initial inspection and at the concluding recheck. Extents below count all physical text lines, including blank lines.

| Artifact | Read extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | 1-523, complete | `EC93120E394DAC60169EFABCE50CB174C44AD65502674F9E704C8ADF6EFA92D2` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | 1-537, complete | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p16/finite-abduction.tex` | 1-340, complete | `AB9195BA7C823075CAFBF3EAD98EFCC5CB754696F0C42D27EF108A5B9303A5FF` |
| `handbook/annex/p16/finite-abduction.tex` | 1-283, complete | `35B9C51F77801CBFFC7B372B7DD9BB67FAFC2033E29BE5F29453DB756C8EA2B9` |

All five specifically assigned PA prerequisite files were read completely:

| Prerequisite | Read extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | 1-252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | 1-315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09262-09327.tex` | 1-253 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | 1-546 | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 1-524 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |

Additional dependency reading was targeted to the actual definitions: `handbook/restoration/inherited-03240-03428.tex:1-125` for deterministic substitution and alpha conversion; `inherited-07678-07752.tex:1-75` for initial functions, nullary arities and primitive recursion; `inherited-08306-08438.tex:40-133` for marked bounds and the syntactic hierarchy; and `inherited-08439-08709.tex:1-164` for the actual pairing and beta formulas. These files' inspected hashes were respectively `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC`, `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD`, `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8`, and `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A`.

For the P16 source comparison, I read all of physical pages 10-12, printed pages 9-11, of `source/references/eiter-gottlob-abduction/eiter-gottlob-abduction-jacm-manuscript.pdf` as extracted text and page images. The held file has SHA256 `E2A021C45BCDC6D2D1BC7AAC9972E75FEC697E3609094060CA92AFFCB694F265`. Those pages include Definitions 2.1-2.5, Proposition 2.1 and its proof, the subset/cardinality discussion, and the surrounding restrictions. Other source pages were not read in this review. This targeted comparison supports the mathematical definitions used here; a separate full source-fidelity review retains its assigned scope.

## P5 component findings

In this section, "body" and "annex" mean the two frozen `pa-checker-arithmetization.tex` files.

| Component | Status | Evidence and mathematical check |
| --- | --- | --- |
| Finite description language, arities and defaults | PASS | Body 10-82 and annex 11-42 specify argument order, projections, composition, scalar list states, ordered cases, bounded folds and searches. Each later operation has a finite dependency order. Initial zero functions include arity zero in the inspected PR definition. Wrong states, commands, expression types, row shapes and outer tags have total failure values. |
| Raw list library | PASS | Body 84-134; annex 141-256. The head/tail double sums exploit unique inverse components below a positive cons. Tail iteration reaches zero by its code bound. Length, entries, reversal and concatenation follow by the displayed inductions. In particular, `V` prepends input entries, so reversing before the second fold restores their original order in concatenation. The empty cases agree. |
| Table and syntax recurrences | PASS | Body 136-179; annex 258-304. Tables append one row per counter and consult only earlier accumulator entries. Proper expression children and binder indices lie below their enclosing constructor codes. Type, node-count, maximum-index, all-variable and free-variable cases agree with the complete grammar in `inherited-09328-09438.tex:45-64`. The free-index bound is proved internally, and the implication sentence lemma follows from both the formula and free-variable row equations. |
| Substitution and alpha machines | PASS | Body 181-257; annex 61-101. The substitution stack preserves left/right order; stopped binders return their whole subtree. Preliminary renaming stops beneath a binder of the old name, uses a name absent from the whole matrix, preserves shape, and is followed by the original request. Inserted replacement terms are returned without becoming main input. Consequently at most `n` main visits and `n` renaming passes of at most `n` visits give the stated quadratic command bound. The alpha environment uses the nearest matching binder, distinct free/bound tags, and binder assembly of arity one. Its linear bound and initial formula test include all required cases. See the notation clarification below. |
| Exact direct axioms and seven-entry selector | PASS | Body 259-295. `Q_7` is the literal seven-entry cons-list; the loop reads positions 0 through 6 using the previously fixed total `e`, whose value is zero at positions at least 7. The seven constructor constants were checked individually against `standard-pa-proof-predicate.tex:24-41`. Prefix stripping recovers the induction core, and complete reconstruction checks its base, step, matrix, binder and canonical prefix. Invalid matrices return zero. |
| Twenty row cases and tree test | PASS | Body 297-394; inherited coding 224-319. Both arity lists agree entry by entry. Tags 0-19 have the actual conclusion patterns and parameter types. Tags 6, 7, 9, 12 and 16 apply branch-specific, formula-specific discharge and strict length decrease. Tag 15 tests free occurrences; tag 16 tests all occurrences after minor discharge and includes the major open list. Tag 8 has antecedent before implication. Tag 18 has no premise. The global row-bit product rejects an earlier failed row even if later rows consult its zero default. Parent counts require exactly one parent for every nonlast row and none for the last. |
| Selected graph and its prerequisites | PASS | Body 396-443; annex 131-139; `inherited-09262-09327.tex:76-158`. The selected predicate is the graph of the expanded `d_19` at output 1. The inspected prerequisite proves beta extension and finite collection inside PA before using them to prove recursive graph totality, uniqueness and defining equations. Its beta formula is the actual bounded formula in `inherited-08439-08709.tex:27-54`. Sigma-one status follows from the declared syntactic closure under marked bounded quantifiers and existential quantification. |
| Offset and open-occurrence induction | PASS | Body 445-466; annex 325-424. The first block remains unchanged; the second has every premise index increased by the first block's length. Formula codes, markers and parameters remain unchanged. Every open index is an assumption index at most its row. The second-block induction treats all rule cases, proves filter/shift commutation with the same removal bit, preserves strict nonvacuity, and checks both freshness conventions. Coincident labels in different copied blocks cause no new removal because old discharges inspect their named premise open lists. |
| Parent counts and final row | PASS | Annex 426-508. The proof splits the defining parent sums into the two old intervals and final row. Cancellation identifies shifted contributions; the intervals are disjoint. The two old roots receive one new reference each and the final row receives none. Positivity of both input lengths justifies every predecessor index. The final row is tag 8, its consequent is a sentence by the internal subformula lemma, and its open list is the first root's list followed by the shifted second root's list. |
| Reused syntax and axiom calls inside PA | PASS | Annex 387-417 and 479-507. The copied rows call substitution, alpha, free-variable, all-variable and axiom descriptions with literally unchanged numerical arguments. Their unique graph outputs therefore agree inside PA. This argument needs no additional internal semantic correctness theorem for substitution or alpha. The final axiom product follows from map/concatenation entries and bounded-product induction, including empty lists. |
| D1 and D2 for the selected predicate | PASS | Body 468-495; annex 510-529. D2 instantiates the universal internal joining theorem, then eliminates the two existential proof witnesses and introduces the joined witness. D1 uses a standard direct proof code from numerical proof meaning and a finite numeral computation in this exact graph. Neither derivation silently substitutes the earlier arbitrary numeralwise representative. |
| Identity example and scope boundary | PASS | Body 497-523; annex 310-314 and 531-536. The one-row identity proof has parent count zero, a sentence root and an empty axiom product. D3 and the evidence-to-proof invariant are expressly reserved. No GL consequence requiring D3 is established by this unit. |

The full numerical PA prerequisite was also checked. Its induction substitutions by zero and `S x_i` never trigger binder renaming; its free-variable and all-occurrence calculations support the exact canonical closure. The actual quantifier transports use self-substitution and universal introduction from a closed open axiom. When transports are inserted at surviving leaves, the new leaves' all-variable sets are subsets of the old sets, which preserves the inherited existential-elimination side condition (`handbook/annex/p05/standard-pa-proof-predicate.tex:45-90,141-215`). The source/direct proof-meaning directions therefore supply the numerical fact used in D1.

### Local notation clarification, severity P3

Location: `handbook/parts/p05/pa-checker-arithmetization.tex:208-213`, particularly line 211.

The fresh-search bound is printed as `1 + max(m(theta), m(u), i, j)`, while `m` was declared on numerical expression codes at lines 136-157 and the command at line 213 explicitly uses the matrix's code. The quantifier case makes the intended matrix argument recoverable: it is `a_1(c)`, equivalently the code of `theta`. Thus this produces no competing algorithm or counterexample in the mathematical reading, but an explicit projection would make the promised description expansion easier to check without a formula/code coercion.

Suggested repair: print `m(a_1(c))` in the bound and, if desired, use `a_1(c)` in the renaming command as well, or write the code brackets in the metadata call. This is a local notation repair. The proof's forbidden-index set and command bound already use the intended matrix and require no changed argument.

No blocking mathematical finding is recorded for P5. There is no unresolved component among its claimed results at the inspected snapshot.

## P16 component findings

Here "body" and "annex" mean the two frozen `finite-abduction.tex` files.

| Component | Status | Evidence and check |
| --- | --- | --- |
| Input and local/global semantics | PASS | Body 21-104; annex 11-69. A valuation on finite `V` extends by false outside `V`, and restriction of a global valuation preserves every formula over `V`, by structural induction. This proves both consistency and entailment equivalences. The actual source pages confirm finite `V`, positive atomic `H,M`, unrestricted overlap and coverage, finite consistent `T`, and the two-conjunct solution criterion. |
| Inconsistent and empty inputs | PASS | Body 95-103, 213-216; annex 54-67. Every augmented model is a model of `T`, so inconsistent `T` yields no explanation. For `E` empty, the criterion becomes consistency of `T` plus its entailment of `M`. Empty `M` leaves exactly the consistency test. Empty `V` has one empty valuation, while its finite theory may still contain constant formulas; the proof does not require that theory to be empty. Empty `H` has precisely one candidate. |
| Qualified monotonicity | PASS | Body 170-174; annex 73-78. Models of a larger candidate form a subset of those of the smaller candidate, preserving sufficiency. The separate consistency assumption is necessary and is explicitly included. |
| Finite minimality, cardinality and deletion | PASS | Body 122-174; annex 80-120. A finite nonempty family of explanatory subsets of a fixed explanation has a least-cardinality member, yielding a contained subset-minimal explanation. Global minimum cardinality implies subset minimality; distinct minimal members are incomparable. In the deletion converse, the deleted candidate is consistent because it is below the known explanation and sufficient because it contains the chosen smaller explanation. The known-explanation hypothesis and empty candidate case are both retained. |
| Exhaustive procedure and exact output | PASS | Body 184-233; annex 128-182. Membership vectors biject with candidates and valuation vectors with finite valuations. Both flags have explicit scan invariants. Their final combination gives soundness and completeness. Each candidate occurs and is appended at most once; subsequent filters preserve that property. The two filters are exactly the declared minimality definitions and handle an empty explanation list. Finite syntax evaluation and finite scans prove termination. The prescribed unshortened scans inspect exactly `2^(r+n)` pairs, with formula evaluation and filtering explicitly additional work. |
| Complete example families | PASS | Body 238-299; annex 184-266. Each candidate family is exhausted, as detailed below. Positive cases have models and sufficiency arguments; failed entailments have explicit countervaluations; inconsistent and ineligible cases are distinguished. |
| Nonentailment and causal boundary | PASS | Body 304-340; annex 268-283. The valuation making `a,b,c` false and `m` true satisfies the size example's background and observation while falsifying both `a` and `b and c`. The arrows have only material-implication semantics, and the input supplies no causal or probabilistic structure. The stated additional treatments remain open. |

All five named theorems have complete corresponding arguments: semantics at annex 11-69, minimality at 71-126, enumeration at 128-182, examples at 184-266, and truth boundary at 268-283.

### Complete example recomputation

The following was checked directly from the six tuple definitions, without a test program.

| Input | All explanations | Subset-minimal | Minimum cardinality | Exhaustiveness reason |
| --- | --- | --- | --- | --- |
| Inconsistent | none | none | none | Both candidates contain an inconsistent background. |
| Given observation | empty set; `{a}` | empty set only | empty set only | These are the only two candidates, and `m` is already in `T`. |
| Empty data | empty set only | empty set only | empty set only | One candidate and one valuation; both universal checks are empty. |
| Unequal sizes | `{a}`, `{a,b}`, `{a,c}`, `{a,b,c}`, `{b,c}` | `{a}`, `{b,c}` | `{a}` | Every candidate is consistent. Sufficiency holds exactly when `a` belongs to it or both `b,c` do; all three omitted candidates have the stated countervaluation. |
| Consistency constraint | `{a}` | `{a}` | `{a}` | Empty set and `{b}` have countermodels to `m`; `{a,b}` violates the constraint. |
| Permitted hypotheses | none | none | none | Both permitted candidates allow `z,m` false. `{z}` is sufficient and consistent but lies outside the candidate domain. |

The empty set in a family is one member; an empty family has no member. The body and annex preserve this distinction throughout.

No mathematical repair is required for P16 at the inspected snapshot. No unresolved component was found among the five claimed results. The broader source presentation, general hypothesis translations, complexity classifications, other preference orders and causal/probabilistic treatments are outside this unit's established conclusions and remain due where independently required.

## Handoff

The mathematical arguments for the claimed P5 and P16 results pass this fresh independent review. The P3 matrix-code notation clarification is the only suggested local repair. Any correction should receive the affected-scope recheck required by the governing contract. This report has not read the parallel source or publication conclusions and was submitted before cross-review.
