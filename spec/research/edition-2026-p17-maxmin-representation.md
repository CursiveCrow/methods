# General maxmin representation: author return for P17 / D2

## Delivered result

Saved:

- handbook/parts/p17/maxmin-representation.tex
- handbook/annex/p17/maxmin-representation.tex

The unit has 16 complete result/proof pairs. It supplies the original Theorem 1 representation in both directions, utility and prior uniqueness, Lemmas 3.1–3.5 and their actual functional dependencies, the corrected bounded-act extension, the two-clause product/independence construction, Proposition 4.2 with its missing extreme-face and finite-restriction steps supplied, and worked examples and failure cases.

States and outcomes are arbitrary nonempty sets; Sigma is an algebra, not silently a sigma algebra; L0 consists of finite-step lottery acts; priors are finitely additive. No finite state surrogate, countable-additivity upgrade or assumed compactness replaces the original domain.

One complete author read-through of the actual body and annex was performed in chunks, including the initially truncated middle portion. The annex was mechanically reordered to follow the body/source dependency order. Local type and degenerate-case corrections were saved. No independent reviewer, scanner, test, build or manuscript rendering was used. Root owns shared integration; this author return is not independent acceptance.

## Exact unchanged primary

Itzhak Gilboa and David Schmeidler, Maxmin Expected Utility with Non-Unique Prior, Journal of Mathematical Economics 18(2) (1989), 141–153. DOI 10.1016/0304-4068(89)90018-9. Submitted December 1987; accepted August 1988.

- Original: source/references/gilboa-schmeidler-maxmin/Gilboa-Schmeidler-MMEU.pdf
- Direct author-hosted URL: https://www.tau.ac.il/~igilboa/pdf/Gilboa_Schmeidler_MMEU.pdf
- Author page that supplies the link: https://www.tau.ac.il/~igilboa/Personal/Journal_Articles.html
- SHA256: 627AF622F540003F8041CBB00BB383E000D0C9AE2C8868E436E3EFEEBA701B3F
- Size: 1418381 bytes; 13 physical pages.
- Physical page = printed page minus 140.
- Existing key: GilboaSchmeidler1989Maxmin.

The preceding ambiguity block personally read original pp. 141–145. This block personally read every remaining original page, 146–153, as images, including all formulas in Lemmas 3.2–3.5, the complete Theorem 1 proof and uniqueness passage, the exact level-measurability definition, Proposition 4.1, both independence clauses, the product construction, Proposition 4.2 and its whole proof through p. 152, and the references. Thus the complete original has now been read across the two blocks.

Reading images: tmp/pdfs/p17-ambiguity/gs89-01.png through gs89-05.png and gs89-proof-06.png through gs89-proof-13.png. The extraction gilboa-schmeidler-mmeu.txt has missing glyphs and was not used as a substitute for these source-formula readings.

## Sixteen proof pairs and the source map

Every body suffix below follows thm:p17-mmeu-.

| Suffix | Exact annex label | Completed content |
| --- | --- | --- |
| utility | annex:p17.mmeu.utility | Source Lemma 3.1: strict/weak axiom bridge, A.3 calibration, finite-prize construction and consistent finite-support patch to arbitrary outcomes, affine uniqueness and nondegeneracy. |
| certainty | annex:p17.mmeu.certainty | Source Lemma 3.2: constant bounds, complete calibration, J and its uniqueness, with coefficient-versus-utility distinction. |
| simple-functional | annex:p17.mmeu.simple.functional | Source Lemma 3.3: well-defined utility-simple functional, scaling independent of normalization, all real cash translations, equal-value and general superadditivity. |
| uniform-extension | annex:p17.mmeu.uniform.extension | Source Lemma 3.4: uniform function completion with the original algebra, 1-Lipschitz extension, every retained property, product and continuous functional calculus. |
| hahn-banach | annex:p17.mmeu.hahn.banach | Full dominated linear extension: one-dimensional interval, both scalar signs, chain union and Zorn; normalized positive touching functional. |
| charges-compactness | annex:p17.mmeu.charges.compactness | Finite-partition integral, uniform extension, positive-functional/charge correspondence; ultrafilter extension and coordinate limits; compactness, topology and attained minima. |
| support | annex:p17.mmeu.support | Source Lemma 3.5's exact D1/D2 sets, convexity/interiors/disjointness, normalized separator, selected prior hull, every sign case and intrinsic dominance set. |
| finite-separation | annex:p17.mmeu.finite.separation | Finite-coordinate separation on arbitrary algebras, including the Euclidean nearest-point argument and an actual simple separating function. |
| representation | annex:p17.mmeu.representation | Theorem 1, both directions, all six axiom consequences, utility uniqueness, complete prior uniqueness proof and exact degenerate/trivial-algebra boundary. |
| extension | annex:p17.mmeu.extension | Corrected Proposition 4.1: original acts retained inside a convex uniform-utility completion; existence, uniqueness using constant equivalents and simple brackets, sigma-algebra equality and restriction remark. |
| domain-boundaries | annex:p17.mmeu.domain.boundaries | Original extension domain not convex on an algebra; genuinely finitely additive prior; failure of monotonicity-only uniqueness; nonclosed representing prior set. |
| extreme-geometry | annex:p17.mmeu.extreme.geometry | Minimal compact face, extreme-point existence and closed hull; extreme projection lift; compact-generator converse with its finite-coordinate grouping proof. |
| exposed-points | annex:p17.mmeu.exposed.points | Full exposed-point closed-hull consequence needed in the source, proved by farthest points and finite-dimensional separation. |
| product-priors | annex:p17.mmeu.product.priors | Rectangle algebra and unique product charge; continuity/compactness; correct marginal images; extreme products and both independence clauses. |
| product-representation | annex:p17.mmeu.product.representation | Proposition 4.2: common utility, candidate marginal prior identification, both inclusions, exposed marginal priors, common minimizing face, extreme lift, finite-subalgebra transfer and arbitrary-algebra conclusion. |
| product-examples | annex:p17.mmeu.product.examples | Four-corner product hull and exact values, a correlated mixture inside it, and separate counterexamples to dropping either independence clause. |

## Direct corrections and exact scope

### Algebra and extension domain, pp. 149–150

The source defines bounded level-measurable acts by requiring both strict and weak comparison level sets to belong to Sigma, then says this act set is convex. This is false for a general algebra.

The saved counterexample uses the finite/cofinite algebra on positive integers and binary-lottery utility functions

    a(n)=1/2+1/(4n)
    b(n)=1/2-1/(4n)+(-1)^n/(8n^2).

Both have all their strict/weak upper level sets in the algebra. Their average has its upper level set at 1/2 equal to the even integers, which is not in that algebra.

The active reader definition therefore uses B as the uniform completion of Sigma-simple functions and the convex utility-bounded act domain L_u with u composed with f in B. The original level-measurable bounded acts are explicitly proved to be contained in L_u, so no original act is discarded. The source's extension formula is fully proved on this enlarged convex domain, and its restriction to the original acts is forced. If Sigma is a sigma algebra the two domains coincide; that stronger hypothesis is not imposed on the general theorem.

The source's statement that monotonicity alone forces the unique extension is also too strong. A free-ultrafilter order on convergent utility sequences agrees with the finite/cofinite simple-act order, is complete and monotone, but ranks 1/n above zero. It fails A.3. The active uniqueness theorem retains all required axioms and proves the constant-equivalent and bracket steps.

### Prior uniqueness and degeneracy, pp. 145 and 149

Nondegeneracy makes the closed convex prior set unique. If all acts are indifferent, every nonempty closed convex prior set represents them. The source's unconditional iff wording needs the trivial-algebra exception: when Sigma={empty,S}, the prior space has only one member even in the degenerate case. The reader theorem states and proves every case.

### Product proof, p. 152

The source chooses a common minimizing P0 in C', obtains C' contained in the closed convex hull C of products, and then treats P0 as a product. Membership in that convex hull does not imply product form.

The active proof takes an extreme point of the nonempty common minimizing face of C'. The full compact-face theorem is supplied, so this point exists and is extreme in C'; the stochastic-independence clause then makes it a product. Exposed marginal functionals identify its two factors. A worked correlated mixture inside the product hull demonstrates why the original inference was invalid.

The source's finite-subalgebra restriction also needs a lift argument for extreme points of the projected prior set. The active proof supplies that lift via a compact face fiber, so both independence clauses genuinely pass to the finite restrictions. Equality on all finite rectangle-generated subalgebras then proves equality of the original prior sets using finite-coordinate separation. No finite surrogate is substituted.

The complement direction in the source's final Step 2 contradiction is corrected to the inclusion still being proved.

### Independence events on an algebra

The original probability expression must refer to events in its algebra. The active definition explicitly quantifies over Borel utility preimages that belong to Sigma, namely each utility function's measurable event algebra. This includes every original strict and weak level event. For sigma-algebra measurable functions it is the usual full Borel-event independence condition. It does not assign probabilities to undefined sets or silently close Sigma under countable unions.

Both original clauses are retained: a common minimizing prior, and stochastic independence under every extreme prior. Independence is not required under every mixture in C, which would exclude the source's own product construction. Its invariance under positive affine utility changes is proved.

## Foundations used and proved

The main construction uses the source's strict A.2 and mixture A.3 exactly. It does not substitute the older finite chapter's neighborhood continuity. The arbitrary-outcome utility representation is proved by finite-support calibration and a consistent patch, so no global best/worst outcome or bounded consequence utility is assumed.

The source's D1/D2 separator is produced by a fully proved Hahn–Banach dominated-extension construction. Finitely additive integration is constructed directly from finite partitions and uniform completion; no countably additive Riesz theorem is imported.

Compactness of the prior space is proved by ultrafilter limits of all event coordinates. Eventwise and weak-star topology are identified on the normalized positive prior space by uniform approximation; no unqualified assertion about arbitrary unbounded families of signed functionals is needed.

The complete active interface thm:p06-ac-to-zorn was read in handbook/parts/p06/cardinals-choice-supplement.tex and its full annex proof, and its live input at handbook/parts/p06.tex was confirmed. The chapter explicitly works in ZF+AC. The active bounded-function completeness result thm:p17-sequential-contraction and the independence-only mixture comparison thm:p17-mixture-comparison are reused at their exact scopes.

The source's Straszewicz appeal is supplied through the exact closed-convex-hull consequence required in the finite-algebra step. A direct farthest-point proof establishes it fully. This does not claim the separate complete Straszewicz1935 article or Dunford–Schwartz1957 source presentation has been acquired/reconstructed.

## Worked examples

The product of the two binary prior intervals [1/4,3/4] is the convex hull, in state order (00,01,10,11), of

    (9,3,3,1)/16, (3,9,1,3)/16,
    (3,1,9,3)/16, (1,3,3,9)/16.

The marginal success values are 1/4; joint success has value 1/16. Half the first and last priors is (5,3,3,5)/16, with fair marginals but joint-success probability 5/16, so it is correlated. The middle-two-prior segment preserves the marginal intervals and extreme stochastic independence but lacks a common success-minimizing prior.

With singleton fair marginals, the diagonal/antidiagonal coupling segment has common minima for all marginal acts but fails extreme stochastic independence. These isolate the necessity of both clauses.

The infinite-state free-ultrafilter example has singleton masses zero and total mass one, proving the need to retain finite additivity. The finite-support prior set has the same minimum on every simple function as all finitely additive priors but is not closed, proving the closedness qualification.

## Integration and notation

Integrated on 9 September 2026 as P17.14 in both active reading drivers.
The existing GilboaSchmeidler1989Maxmin key is reused. Eleven typed notation
rows are in the canonical symbol register. The finite ambiguity chapter now
links to the full representation, extension and product treatment. The sixteen
result/proof pairs retain their authored qualifications. Consolidated reviews
and admission remain pending under the governing workflow.

Chapter: sec:p17-maxmin-representation.
Annex: sec:annex-p17-maxmin-representation.
Existing source key: GilboaSchmeidler1989Maxmin.
No new bibliography entry is required.

Local roles include arbitrary S/X, algebra Sigma, Y=Delta_f(X), L0/Lc and y-star; source A.1–A.6; consequence v and affine lottery u, utility range K and certainty functional J; B0/B, uniform norm and I; real sublinear p, linear ell/L_b; finite additive P, prior space P(Sigma), filters/ultrafilters; D1/D2, support priors P_b, closed convex C and the intrinsic set; L_lev and corrected L_u; source product algebras and product charges; marginal maps R_i and lifts; faces, Ext/Exp, finite-coordinate and exposed-point vectors; candidate C', finite subalgebras Sigma_i^0 and their projected prior sets.

Root owns shared routes, bibliography and symbols. No prior manuscript component or shared file was edited.

## Completion boundary

All required mathematical claims are supplied, with the necessary direct source corrections described above. There is no remaining open proof dependency for Theorem 1, its corrected extension, or the full product characterization on arbitrary algebras. The separate historical presentations of Fishburn's utility theorem, Dunford–Schwartz's general functional-analysis results, Straszewicz1935, and the other referenced papers remain source/version obligations; the precise prerequisites used here have complete proofs or the identified complete active interfaces.

This is author completion of the assigned source chain, not manuscript-wide completion or independent admission.
