# Independent topic review: finite probability and Kamp III.2 Lemma 1

Date: 7 September 2026. Review began at 20:25 UTC. Role: fresh independent mathematical/topic reviewer. Repository: `C:\Dev\the-methods-of-reason`; live branch `phase4-codex`; HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The working tree contains extensive existing and concurrent work, so the file hashes below identify the reviewed content.

## Verdicts

| Unit | Topic verdict | Result |
| --- | --- | --- |
| P15 finite probability, main text and proof annex | PASS | All seven theorem/proof items follow from the declared finite model. The conditioning denominators, null cases, independence qualifications, numerical examples, and almost-sure uniqueness claim are correct. |
| Kamp III.2, first supporting lemma, main text and proof annex | PASS | Both binary recursions represent their occurrence words correctly. The realization and temporal equivalences hold in both directions over the actual host class `Lin`, including unordered endpoint assignments where relevant, empty open intervals, and orders with endpoints. |

No mathematical counterexample, omitted proof case, or unresolved topic finding was found in the assigned texts. These verdicts cover the mathematical content at the recorded hashes. Source fidelity, production checks, admission, and the remaining proof of Kamp III.2 require their own evidence.

This report was prepared before reading any author conclusions or other new review reports. No manuscript file was edited. No test suite, build, or rendering was run. Numerical recomputation used exact integer fractions in an ephemeral JavaScript calculation; the broader mathematical assessment is the proof analysis recorded below.

## Read manifest and frozen inputs

All line numbers in the findings are one-based. Paths in this table are relative to the repository unless an absolute path is given. The four target files were read completely, including prose and examples, and their hashes match the assigned snapshot.

| File | Extent actually inspected for this review | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | All 168 lines | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/parts/p15/finite-probability.tex` | All 461 lines | `BD14BAB29058D7235155D827A8F11793A1D07AF119AD1B34239835EF98805AC0` |
| `handbook/annex/p15/finite-probability.tex` | All 284 lines | `D51A43CF5E2CD2DCE15CD558EF3A167AC084347BB471E2A44E657769399EAE58` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | All 202 lines | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | All 212 lines | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/parts/p09/presentations/n-c-012.tex` | Lines 1–170, especially the complete host definitions at 16–131; keyword search elsewhere. The file has 3,064 lines; a broad read was truncated and is not treated as a complete host review. | `35F9137094A285A4847D351FF868CC206EBF3A6F8F7A75DAC767F0C0AFCE2590` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | Lines 66–191 and 225–231, plus keyword locations, solely to check the target's description of the preceding normal-form result. Its proof was not reviewed. | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `C:\Users\Crow\.codex\memories\MEMORY.md` | Repository keyword hits at 844–867 and the historical workflow passage at 859–885. Used for review discipline only; no historical mathematical verdict supplies evidence for these new units. | `B6257CF8DBACA4C7D6E8BC2B0706D9DBBFEFCDD00068A955E557C0716E8EC45E` |

No primary document was needed to resolve the mathematical interpretation: the target definitions and the inspected host give explicit semantics sufficient to prove the bounded claims. Attribution to Grinstead–Snell and Kamp, source page locators, and fidelity to their wording or exact source grammar belong to the independent source review.

## Finite probability: seven theorem/proof items

References in this section use `main` for `handbook/parts/p15/finite-probability.tex` and `annex` for its corresponding proof file.

### 1. Finite probability identities and atomic representation — PASS

Main 24–75; annex 12–56. The nonempty finite outcome set and normalized nonnegative masses supply all the hypotheses used. The empty sum gives the empty-event value; adding nonnegative masses proves monotonicity and the upper bound; the disjoint decompositions prove complement and the two-event union identity. The zero-mass criterion uses nonnegativity, and the support characterization uses complement, so neither silently equates probability one with containing every outcome.

For the converse, `Q` takes finite real values in `[0,infinity)`. Applying pair additivity to two empty sets therefore legitimately gives `Q(empty)=0`. Induction yields finite additivity, singleton decomposition yields the masses and normalization, and their nonnegative sum of one bounds every atom by one. The same singleton identity forces uniqueness. The `m=0` additivity case is expressly supplied in annex 26. No countable-additivity or measure-extension premise is needed on this finite power set.

### 2. Laws, marginalization, and grouping — PASS

Main 77–111; annex 58–78. A function from nonempty `Omega` to `S` already ensures that `S` is nonempty whenever such a variable is supplied. Its fibers are disjoint and exhaustive even when some fibers are empty. The joint variable has finite value set `S x T`; summing its fibers with one coordinate fixed produces the relevant marginal. Composition by `f` groups exactly those original fibers mapped to a specified output value. Empty and unattained fibers contribute zero. The argument never assumes that a variable is injective or surjective or that a chosen value set equals its support.

### 3. Conditional measure, multiplication, and successive conditioning — PASS

Main 116–167; annex 80–119. `P(B)>0` is fixed before either the ratio or the conditional mass is used. Nonnegative masses summing to one also lie individually in `[0,1]`; their sum on `A` is exactly `P(A intersect B)/P(B)`. The chain rule requires positivity precisely for the prefixes used as denominators, `B_0` through `B_(n-1)`. It includes `n=1` and allows the final intersection `B_n` to be null. The proof explicitly withholds the product when an earlier required prefix is null.

For successive conditioning, `P(B intersect C)>0` implies both `P(B)>0` and `P_B(C)>0`; cancellation is therefore legal. The null-event example at main 159–166 correctly permits nonempty null events and shows why multiplication by zero does not define their conditional probabilities.

### 4. Total probability, Bayes, and odds — PASS

Main 169–212; annex 121–149. The partition is finite, exhaustive, disjoint, and nonempty. Null hypotheses are omitted from the likelihood sum through `J`; their intersection probabilities vanish by monotonicity. Consequently neither the sum nor its proof contains a hidden product of zero with an undefined conditional probability. Positive evidence supplies the posterior denominator, and the sum of posterior numerators is that same evidence probability.

The two-hypothesis assumptions `0 < pi < 1` define both likelihoods. The additional `q_0 > 0` makes `(1-pi)q_0` positive, which establishes positive evidence and a positive complement posterior. Thus the likelihood ratio, prior odds, and posterior odds are all ordinary real numbers. The proof covers `q_1=0`; it makes no claim requiring division by a zero likelihood.

### 5. Independence criteria and the product construction — PASS

Main 217–274; annex 151–200. The equivalence with an unchanged conditional probability uses precisely the hypothesis `P(B)>0`. Null events are handled directly with the product identity. Complement preservation uses subtraction and symmetry without dividing by event probabilities, covering probability zero and one.

Factoring the joint mass implies independence of every pair of value-set events by finite double summation. Choosing singleton value sets proves the converse. The product construction normalizes by distributivity, has the prescribed marginals, and factors its joint law by construction. The definition of mutual independence checks every nonempty subfamily and therefore does not collapse to the full intersection or to pairwise independence.

In the four-point example, `A={10,11}`, `B={01,11}`, and `C={00,11}`. Every pairwise intersection is `{11}` and has mass `1/4`; the triple also has mass `1/4`, which differs from `1/8`. Given `C`, the two remaining outcomes each have conditional mass `1/2`, yielding `P(A|C)=P(B|C)=1/2` and `P(A intersect B|C)=1/2`. All claims at main 255–274 are correct.

### 6. Expectation, linearity, and independent products — PASS

Main 343–393; annex 202–249. Every real-valued variable on finite `Omega` has finite real values and finite range. Grouping by fibers proves the formula for `E[f(X)]`; the indicator identity follows directly. Finite distributivity and normalization prove affine linearity, including `n=0`, without an independence premise. Nonnegative weighted differences prove monotonicity.

For independent `X,Y`, applying the already established grouping identity to their joint variable and multiplication map is legitimate. Joint-mass factorization gives `E[XY]=E[X]E[Y]`. The indicator example correctly demonstrates that repeated dependent summands still satisfy linearity while the product factorization can fail: the product mean is `1/2`, and the product of means is `1/4`. No converse from uncorrelatedness to independence is asserted.

### 7. Conditional means, total expectation, and uniqueness — PASS

Main 395–432; annex 251–284. Event conditional expectations are defined only for positive-probability events. The function `g` chooses zero on null `Y` fibers as a representative value; this is expressly separated from conditioning on those fibers. Because `T` is finite, their union is null, and arbitrary alternative finite real values change `g(Y)` only on that null union.

The partition identity omits null blocks before forming any conditional expectation. On each positive `Y` fiber, constancy of `g(Y)` and the event conditional-mean definition give the averaging identity. On each null fiber every atom has zero mass, so both finite sums vanish. Summing over any `D` gives the stated property, and choosing `D=T` gives total expectation.

The uniqueness proof uses the full family of averaging equalities for every `D`, together with the stated restriction to variables of the form `h(Y)`. Taking `D={y}` forces `h(y)=g(y)` at each positive fiber by division by `p_Y(y)>0`; the remaining fibers form a null event. Thus uniqueness is almost sure, with exactly the necessary qualification.

## Recomputed probability examples and boundary probes

The following exact fraction calculations independently reproduce the quantities printed in main 276–338 and 434–445.

| Quantity | Recomputed value |
| --- | --- |
| Alert probability | `(90+495)/10000 = 117/2000` |
| Defect posterior after one alert | `90/585 = 2/13` |
| Complement posterior after one alert | `495/585 = 11/13` |
| Likelihood ratio; prior odds; posterior odds | `18`; `1/99`; `2/11` |
| Posterior with prior defect probability `1/10` | `(9/100)/(9/100+9/200) = 2/3` |
| Defect and two-alert joint mass in the conditional product model | `81/10000` |
| No-defect and two-alert joint mass | `99/40000` |
| Two-alert probability | `423/40000` |
| Defect posterior after two alerts | `(324/40000)/(423/40000) = 36/47` |
| Total expectation from the two one-alert fibers | `(585/10000)(90/585) + (9415/10000)(10/9415) = 1/100` |

In the two-alert model, the eight masses, in order `(h,u,v)=000,001,010,011,100,101,110,111`, are

`35739/40000, 1881/40000, 1881/40000, 99/40000, 1/10000, 9/10000, 9/10000, 81/10000`.

They sum to one. Conditional on either value of `h`, they give the specified product law. The unconditional joint alert probability `423/40000` differs from the product of unconditional alert probabilities `13689/4000000`, confirming why the text carefully states conditional independence. In the alternative copied-alert model, `E_1 intersect E_2=E_1`; the two-report posterior remains `2/13`. The one-alert marginals therefore do not justify squaring the likelihoods.

Additional boundary probes confirm the load-bearing hypotheses rather than contradict the target:

- On a singleton probability space, the law, conditioning on the full space, product, and expectation identities all reduce correctly to their constant or zero cases.
- With masses `(1,0,0)`, a nonempty null conditioning set has no ratio-defined conditional probability, while an almost-sure event can omit two outcomes. This matches main 159–166.
- For a partition containing a prior-null cell, that cell contributes zero to total probability and receives zero posterior after positive evidence, without ever defining its likelihood.
- For a constant `Y` on a two-point space with equal masses, `X=0` and `W` taking values `-1,1` satisfy the same averaging equalities over `Y` events, but `W` is not of the form `h(Y)`. The theorem's restriction to `h(Y)` therefore matters and is correctly present.
- With one positive and one null `Y` fiber, changing the representative value on the null fiber can change the random variable pointwise. The theorem correctly promises only almost-sure uniqueness.

## Kamp III.2 Lemma 1: mathematical analysis

References in this section use `main` for `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` and `annex` for its corresponding proof file.

### Host interpretation and substitution — PASS

The actual host at `n-c-012.tex` 16–40 makes `Lin` the class of nonempty strict linear orders: asymmetry, transitivity, and comparison of distinct points are available; density, completeness, and the absence of endpoints are not imposed. Lines 42–72 give the unary-predicate first-order language and the current-point variable. Lines 74–131 define the temporal language, witness-first argument order for strict `S` and `U`, and the translation `D` with capture-avoiding substitutions.

Main 11–28 adopts those meanings explicitly. Both recurrence displays and both translated induction steps agree with them: the first temporal argument holds at a strictly earlier or later witness; the second holds only on the intervening open interval. The current endpoint letter is supplied by the external conjunction. No inclusive-until convention enters either proof.

### Recursive associations, words, and free variables — PASS

Main 30–132; annex 18–31 and 86–98. The past constructor prepends an endpoint predicate and its following interval predicate to the constituent word. The future constructor appends the preceding interval predicate and final endpoint predicate. Each adds exactly two predicate occurrences to the three-occurrence base, giving `2n+1` occurrences and `n` intervals at stage `n`. Repeated predicate letters still contribute repeated occurrences.

At the past step the constituent has free endpoints `z,y`; at the future step it has `x,z`. Fresh binding of `z`, fresh binding of the universal interval variable, and the new endpoint condition leave precisely `x,y` free in either case. The guarded closures then leave precisely their displayed current endpoint. The `x != y` qualifications are explicitly about distinct variable names, not an undeclared equality predicate in `L`.

Every alternating predicate word of the stipulated length can be assembled in each association by recursively removing or adding the first or last endpoint/interval pair. This is a finite syntactic construction for every finite word. The stages are exact stages; neither the definition nor the proof assumes that earlier stage formulas are retained literally in a later stage.

### Binary realization equivalence in both directions — PASS

Annex 33–98. The base equivalence is asserted under `a<b`, so its two endpoints themselves form the required strictly increasing realization. At the past step a witness `a<c<b` and the constituent realization from `c` to `b` concatenate to the whole chain. Conversely the first interior point of a realizing chain supplies exactly that witness and leaves a constituent realization. At the future step the argument uses the last interior point instead. Both new interval predicates are checked on exactly their intended open intervals.

For same-word equivalence at unordered endpoint assignments, stage one gives identical endpoint/interval formulas up to fresh bound-variable names. At every stage at least two, the outer strict interior witness entails `x<y` by transitivity; if the endpoints are equal or reversed, both associated formulas are false. Thus the claimed all-assignment equivalence is justified without extending the realization equivalence beyond its ordered-endpoint hypothesis.

### Guarded closures in both directions — PASS

Annex 100–124. An existential endpoint witness and the binary equivalence give a realization ending or beginning at the designated current point. Conversely a realization has at least two strictly ordered points because `n>=1`; its other endpoint supplies the guarded existential witness. The proof therefore never infers a strict endpoint from a stage-zero singleton, and never invents an interior point unavailable in the underlying order.

### Temporal recurrences in both directions — PASS

Main 134–170; annex 126–185. The past induction invariant is realization of the initial word ending at the current point. The seed `L_0` has a one-point realization. At step `i`, strict since supplies the penultimate point, whose initial subchain comes from induction, together with the last interval condition and current endpoint predicate. Reversing this construction selects the penultimate point from a realizing chain and verifies every conjunct of the translation.

The future invariant is realization of the terminal word beginning at the current point. The seed `R_n` is correct. At each descending step strict until supplies the second point and a realizing tail; prepending the current point gives the required whole realization. Conversely the second point of a realization verifies the until witness and tail, with the first interval and current endpoint verifying the remaining conjuncts. The indices `B_i` in the past recurrence and `B_(i+1)` in the future recurrence match exactly those intervals.

Combining these invariants with the guarded closure equivalences proves the two displayed `Lin` equivalences. All formulas use only the supplied unary predicates and their corresponding temporal proposition letters. Each recurrence adds one temporal constructor and one conjunction while using the previous formula once; after `n` steps it is finite. The host's infinite stock of variable names supplies fresh names for each finite translated formula, and the final renaming preserves the sole free endpoint.

### Endpoint, emptiness, and finite-construction probes — PASS

Main 172–202; annex 187–210. The following small structures directly challenge the cases most likely to be lost by a wrong strictness convention or an invalid reassociation:

- On the singleton order, every guarded basic closure of every positive stage is false, as are the corresponding temporal formulas. There is no strict temporal witness.
- On the two-point order `0<1`, take the base endpoint predicates true at their designated points and the interval predicate empty. The binary base at `(0,1)` and the appropriate one-piece closure are true because the open interval is empty. This verifies that the interval predicate is not accidentally required at either endpoint.
- On that same order with all predicates true everywhere, every two-piece closure is false: three increasing points cannot be supplied. The nested strict temporal formulas are false for the same reason, exactly as stated in main 186–191.
- On a three-point order with all predicates true, the two-piece past formula holds only at the last point, and the two-piece future formula holds only at the first point. Their witnesses recover the unique three-point chain.
- At equal or reversed endpoints, the binary base may be true if the endpoint predicates hold. It still has no strictly increasing two-endpoint realization. The proof avoids this false unguarded equivalence by explicitly requiring ordered endpoints in annex 34–43.
- On any order, later-stage binary patterns at equal or reversed endpoints are false because their outer interior witness would force ordered endpoints. This supplies the missing distinction between the base and later stages in the same-word argument.
- Reusing the same unary predicate at several or all word positions leaves both inductions intact. They use occurrences and memberships, with no assumption that predicates are distinct or disjoint.
- A dense order with an empty interval predicate supplies no two distinct endpoints with a satisfying intervening interval, while an adjacent pair in a discrete order can do so. Both outcomes follow from the same universal open-interval clause. The proof does not rely on density or its negation.

The target's description of the preceding III.1 result agrees with the inspected component and standard-form definitions and theorem statement at `kamp-iii1-normal-form.tex` 66–191. The final paragraph correctly locates the further regional expressibility result and complete III.2 proof outside this first lemma. This review establishes neither that later result nor the preceding theorem's full proof anew.

## Required corrections and remaining boundaries

Required mathematical corrections in the assigned units: none identified. Unresolved mathematical/topic findings within the assigned scope: none identified.

The review supplies an independent topic verdict for each frozen unit. Separate source fidelity and adversarial publication review, scoped static/build/visual evidence, dependency control, and a subsequent admission record remain governed by the edition contract. Changes to any reviewed mathematical definition, statement, proof, or relevant host dependency require reassessment of the affected verdict.
