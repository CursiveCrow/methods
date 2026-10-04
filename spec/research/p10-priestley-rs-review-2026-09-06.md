# Priestley duality and Rasiowa–Sikorski: actual-text review

Date: 2026-09-06. Review began 2026-09-07 02:51:58 UTC.

## Scope and result

Read in full the actual body and annex files for `priestley-duality` and `rasiowa-sikorski` under `handbook/parts/p10` and `handbook/annex/p10`. Checked the precise Part II arbitrary-variable compactness dependency and the relevant primary Ciesielski source pages. No other review was consulted. Only this note was written; no manuscript edits, tests, builds, renders, or new agents.

**All mathematical arguments pass after the explicit BPIT hypothesis was added to the functorial Priestley theorem during review.** One small citation-locator alignment was reported separately below.

## Reported corrections

1. **Resolved and read back:** `thm:p10-priestley-functors` initially omitted BPIT even though its arbitrary-lattice object representation depends on BPIT. The body now explicitly begins that theorem with “Assume BPIT.” The reconstruction proof also now identifies the elementary Hausdorff argument as BPIT-free, so its own statement can correctly remain a ZF result for an already given Priestley space.

2. **Resolved and read back:** the source sentence immediately before the Priestley-space subsection mentions the prime-filter theorem **and its Heyting application**, while its citation initially named only Moraschini's Prime Filter Theorem and Corollary 2.14, p41. The author added Theorem 2.26, pp47–48, and the amended actual file was checked during the following Heyting review. The source-locator alignment is now correct.

## Prime-filter separation

The generated-filter formula G[a]={d: some g∈G has g∧a≤d} is correct. If a filter maximal while avoiding I contained a∨b but neither disjunct, both one-element extensions would meet I. Taking the two witnesses and distributing their meet with a∨b produces an element belonging to both the filter and I. Properness follows from 0∈I. Maximality among filters also required to contain F is sufficient: any extension of the resulting filter automatically contains F.

For finite D, there is a maximal member of the finite nonempty set of filters extending F and avoiding I; no choice principle is needed. The finite-generation argument for bounded distributive sublattices is correct: finite joins of finite meets of the m generators give at most 2^(2^m) forms, including the bounds by empty join/meet.

Every finite part of the propositional encoding mentions only finitely many lattice elements. The bounded sublattice they generate is finite. Intersections F∩D_0 and I∩D_0 are indeed a filter and ideal there, contain the same bounds, and remain disjoint. Their finite separation yields a characteristic valuation satisfying all the selected clauses. Extending unused proposition values by 0 requires no choice.

The cited `thm:p02-arbitrary-prop-compactness-bpi` explicitly provides compactness for every set of proposition letters and every set of finitary formulas under BPIT, so the possibly uncountable alphabet {p_a:a∈D} is covered. That theorem is currently an explicitly cited dependency, not claimed here to have a new local proof. The model of the full lattice equations yields the required bounded lattice homomorphism to 2 and hence the prime filter, with all F-memberships and I-exclusions enforced. No Heyting implication preservation is imposed on this characteristic map.

For countable D, the recursion tests avoidance of the **entire** ideal at every stage. Its union is a filter disjoint from I. If an element never enters, the extension rejected when that element was enumerated remains a subfilter of every later hypothetical extension containing it, so that hypothetical extension meets I. Thus the union has exactly the maximality needed for primeness. Every step is a uniquely specified case distinction, not a sequence of arbitrary witness choices. The countable conclusion is therefore correctly proved in ZF. Finite nonempty lattices can be enumerated with repetitions. The trivial lattice has no disjoint filter/ideal pair, so its separation assertion is vacuous.

## Priestley representation and compactness

Finite positive membership conditions combine by meet and finite negative conditions by join, so the differences â\b̂ form the announced clopen basis. Inclusion of prime filters is a partial order, and a failed inclusion is separated by a clopen upset in the required direction. The same elementary argument gives the Hausdorff property without BPIT.

The arbitrary-cover proof forms all basic refinements rather than choosing a neighborhood at every point. A finite basic refinement cover would give a finite original cover using only finite choices. Consequently each finite collection of avoidance clauses p_a→p_b has a characteristic prime-filter valuation outside its selected basic sets; that valuation satisfies every lattice clause in Π_D as well. Propositional compactness then contradicts the full cover. This argument uses the pure Π_D of lattice equations, not the separate F/I constraints from the extension theorem.

The Stone-style map preserves bounds, meets, and joins, and prime-filter separation reflects order, yielding injectivity. Surjectivity onto **all clopen upsets** uses two finite-cover arguments correctly. For P∈K and Q∉K, upset closure gives P⊈Q, so complements of â for a∈P cover the complement of K. A finite subcover gives a finite meet belonging to P whose represented upset is contained in K. All such represented upsets cover K, and a second finite subcover gives the representing finite join. This avoids a simultaneous choice indexed by all P∈K. Empty K and the trivial lattice are treated by the empty join and empty space.

## Reconstruction, negative memberships, and maps

Point evaluation is a prime filter of the clopen-upset lattice. It preserves and reflects order by Priestley separation, hence is injective. For an arbitrary prime filter P, the proof correctly includes both its positive members and complements of every clopen upset absent from P in the closed family. The latter lattice elements form an ideal. An empty finite intersection would put a finite join of absent elements into P, contradicting primeness; empty positive or negative lists are correctly covered by the lattice bounds. Compactness therefore gives a point with **exactly** P's memberships, proving surjectivity.

The evaluation map is continuous on the defining subbasis. Its target is Hausdorff by the elementary argument that does not use BPIT. A compact-to-Hausdorff continuous bijection is a homeomorphism; the annex supplies the finite-neighborhood proof that compact subsets of a Hausdorff space are closed, with no implicit infinite choice. The empty-space/trivial-lattice reconstruction works directly.

For h:D→E, prime-filter inverse image is well defined and order preserving, and X(h)⁻¹[â]=h(a)^ proves continuity. For continuous monotone g:X→Y, inverse image preserves clopen upsets and all bounded lattice operations. Both functors reverse composition. Both displayed naturality equations have the correct domains and codomains, and the two elementwise reconstruction identities prove the claimed contravariant equivalence. The trivial/empty objects and their possible arrows are compatible with these inverse-image formulas. The three-element-chain example correctly has two ordered prime filters, three clopen upsets, and four underlying clopens.

## Rasiowa–Sikorski and exact choice assumptions

The order convention makes stronger conditions smaller. Density does not imply downward closure, and the body expressly does not require such closure. The filter definition is nonempty, upward closed, and downward directed.

The stated prescribed-start form of DC is appropriate. On N×P, the relation advancing the first coordinate and selecting a stronger member of D_n is serial. DC from (0,p) produces the required descending sequence with p_(n+1)∈D_n. Its upward closure contains p, is upward closed, and is directed because a later term lies below any two chosen witness terms. It meets every dense set at the appropriate sequence term.

For an onto enumeration of P, the least suitable index exists by density and gives a uniquely defined recursion in ZF. It need not be algorithmically computable. For any nonempty countable family of requirements, selecting one enumeration is a single existential choice, not countable choice. The empty family is handled separately.

For a finite family of dense sets, finite successive choices are available in ZF. The principal upward set of the last chosen condition is the filter; it contains earlier witness conditions, so it meets each dense set even if that dense set is not downward closed. For the empty family the principal upward set of p suffices.

For finite P, a minimal element below p has no strictly stronger condition. Every dense subset must contain it. Its principal upward set therefore meets **all** dense subsets simultaneously, without enumerating a family. This claim is correct in ZF.

The manuscript asserts only that DC suffices for the arbitrary-poset/countable-family result; it makes no unsupported implication from BPIT and no unsupported optimality/equivalence claim about choice principles.

## Source checks

Ciesielski's author-hosted *Set Theory for the Working Mathematician* was checked directly: §8.1, printed pp130–132, has the same dense-set, stronger-condition, and filter directions; **Theorem 8.1.2, pp132–133**, is explicitly named the Rasiowa–Sikorski lemma and constructs a descending sequence whose upward closure meets the prescribed countable dense family. Source URL: <https://community.wvu.edu/~kciesiel/ProfessionalStuff/Other/ElectronicReprints/B2IntSetThe.pdf>. The manuscript's additional DC/finite/countable refinements are supported by its own proofs rather than incorrectly attributed as verbatim source assertions.

The revised reference to Priestley's 2019 slides 17–20 matches the inspected author presentation of hom-functors and full duality. The citation to Bezhanishvili's thesis pp33–37 supports the identified Heyting/order-topological specialization, without claiming that it is the original 1970 body. The source's ordinary dense-set lemma is now kept distinct from prime-filter separation, as required.
