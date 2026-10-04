# P16 graph-uniform identification and modified Tian algorithm: author return

Date: 8 September 2026 UTC. Author block began 13:14:09 UTC;
deadline 13:59:09 UTC. The three assigned output paths were absent at
intake. Only these new files were edited. The user-directed workflow
remains all manuscript changes before consolidated independent reviews.

## Complete written extent

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/graph-uniform-identification.tex` | 317 lines; quantified definitions, both algorithms, nine results, source-regime boundary | `89427D5F437B232FAFCF99CCC67CE87B2E9D73C8916BD83EE4D9E390A1B72AE1` |
| `handbook/annex/p16/graph-uniform-identification.tex` | 508 lines; nine complete proofs | `8E60602797EC6B45D4F62BB378DCC5BFB5258280116CF49DB78A6AA7AED76E7C` |

The complete actual LaTeX body and annex were read back mathematically,
including the final corrections. No scoped scanner, build, new test,
acceptance check or independent review was run, following the parent's
explicit instruction during this block. Line counts and hashes are
handoff identifiers, not acceptance evidence.

The nine reciprocal suffixes have body prefix `thm:p16-` and annex
prefix `annex:p16.`:

| Suffix | Full written proof |
| --- | --- |
| `graph-uniform-equivalences` | Quantifier over all finite nonempty observed alphabet families; equivalence of uniform identification, ID success, no hedge for the full query, and uniform finite do-calculus derivability. |
| `graph-uniform-all-effects` | Every query is uniformly identified iff no directed edge has endpoints in one maximal district. |
| `graph-uniform-action-scope` | Positive bow-followed-by-chain countermodels for P_a(Y), and a proof for every positive finite model that P_{a,m}(Y)=P(Y given m). |
| `tian-component-invariant` | Exhaustive branch order, unique selected district, exact non-strict inclusions, Q-kernel meaning, all fixed parameters, normalization and positive denominator invariants. |
| `tian-component-soundness` | Decrease of |T|-|C|, depth bound, every returning branch's soundness, and the preceding source do-calculus utility derivations as the separate proof route. |
| `tian-outer-soundness` | Empty response, full-graph district inputs, termination, product/sum target identity, independence of unused parameters, support, and uniform do-calculus derivation. |
| `tian-failure-hedge` | Original action intersection of the final failed T; explicit common-root edge-subgraph forests; original-query and standalone-component hedge extraction. |
| `tian-completeness` | Graph-uniform outer completeness, equality of success/failure decisions with ID, all-effects consequence, and standalone c-identify completeness including fixed nonconstant finite domains. |
| `tian-worked` | Positive examples with T'=C and T'=A; every recursive step; complete front-door return and values 19/32, 25/32; unequal unpruned root sets and correct common-root pruning. |

## The completed quantifier distinction

The graph-uniform positive-law question fixes G, X and Y, then quantifies
over every family of finite nonempty observed alphabets. Within each
family it compares models on that same family with equal positive observed
laws. One positive four-valued countermodel pair disproves this outer
universal property. Success gives a formula schema and finite do-calculus
derivation valid on every finite nonempty alphabet family. Hence the
graph-uniform positive-law ID/hedge/do-calculus theorem is complete now.

For one fixed family, the outer alphabet quantifier is absent. A witness
on four values does not settle every binary or ternary family. Singleton
elimination applies to a specified family; it must not erase a vertex
from the graph-uniform question, which also quantifies over families
where that vertex is nonconstant. These distinctions are explicit in
the reader-facing definition and equivalence theorem.

The modified Tian algorithm now has the same graph-uniform completeness
result. Its standalone component subproblem targets the full nonaction
set C, so a failed component's roots already lie in the response. The
positive binary witness therefore additionally proves that standalone
failure is informative on every prescribed nonconstant finite alphabet
family. This statement quantifies over possible input laws; it does not
claim a countermodel reproducing any one externally prescribed kernel.

## Exact primary reading and correction provenance

Used the held published AAAI 2006 paper:
`source/references/shpitser-pearl-joint-identification-2006/aaai06-191.pdf`,
SHA256 `33B1FAAB38522381DE79C8A92CBDCD03F25336BD43BA917CB1677634062929BC`.
The verified publisher capture URL is
<https://cdn.aaai.org/AAAI/2006/AAAI06-191.pdf>.
The existing bibliography key is `ShpitserPearl2006JointIdentification`.
No new source capture or bibliography item was created.
This is the published Figure 5 modification. Tian's 2002 dissertation
was not acquired or read, and its distinct full treatment is not claimed.

This block read the complete exact model/support definitions on page 1220,
identifiability and witness definitions on 1221, the Figure 5 algorithms,
Theorems 5-7 and Corollaries 2-4 on 1225, and the Theorem 7 continuation,
Theorem 8 and Corollary 5 on 1226. The complete page images of 1225 and
1226 were also read. All eight source pages and the complete Theorem 4
parity/lifting passage had already been read in the preceding author
blocks. Research and PDF skills guided primary-source reading and this
source note. No manuscript PDF was generated or inspected.

The active text directly uses the mathematically valid statements:

- Figure 5 component base: sum the supplied q_T=Q[T], with its outside
  arguments retained, rather than introduce an undefined input P.
- Figure 5 recursive district: C is contained in T', T' is contained in
  A, and A is strictly contained in the old T. T'=C and T'=A are both
  possible; worked positive examples establish both cases.
- Figure 5 outer sum binds D minus the actual response set Y. The source
  display prints D minus S without defining S in that procedure's input.
- Theorem 8: T=An(C) does not imply equality of the unpruned sink sets.
  The graph a -> t -> b with C={a,b} supplies a direct example. Common
  roots are constructed by selecting directed routes and deleting the
  appropriate outgoing edges. Only C is known to lie in the original
  post-action ancestor set; the failed T meets the original actions.
- The full query's hedge conditions are retained. The source Corollary 3
  wording allowing arbitrary smaller action sets is not adopted as an
  unconditional enlargement principle. In A -> M -> Y with A <-> M,
  the bow hedge obstructs P_a(Y), but P_{a,m}(Y)=P(Y given m) is identified.
  The body gives all positive observed masses and the exact discrepancy.

These are correction provenance and scope explanations. The active body
does not print an incorrect formula and ask the reader to repair it.

## Source support regime and remaining work

The source explicitly permits nonpositive observed laws. It separately
requires positive conditioning masses and writes the action condition
P(x given Pa(X) minus X)>0. Our full positive-law hypothesis is expressly
identified as a handbook execution domain, not attributed to that source.
The body gives one explicit parent-stratum interpretation for a further
theorem: for every b with p(b)>0, require p(x,b)>0. It does not claim that
the paper supplies that missing quantifier or that this premise alone
proves all recursive ratios admissible.

Positive hedge witnesses satisfy the displayed action-support condition,
so the negative obstruction applies to any broader regime containing
them. Successful execution and completeness on the source's nonpositive
regime still require a precise support domain and a complete proof for
every reached expression. General fixed-binary/ternary completeness at
the remaining core/relay intersections is also separate, as specified
in the preceding hedge component. Neither remaining obligation blocks
the graph-uniform positive-law completeness theorems written here.

## Integration

Input each new file after its `hedges-and-completeness.tex` counterpart.
The parent owns all shared drivers, prior boundary updates, bibliography,
registry and later consolidated reviews. Principal new notation is the
family-indexed map Phi(G,X,Y,S), the uniform formula/derivation concept,
component C/T/A/T-prime with q_T and Ext, the explicit c-identify and
identify procedures, outer D/D_i/T_i and the common-root set K.
The examples define their own named variables and masses before using
them. All proof destinations are written in the paired annex file;
shared navigation and admission remain the integrator's responsibility.
