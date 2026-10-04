# P16 hedges and completeness: author return

Date: 8 September 2026 UTC. Author block began 12:40:04 UTC;
deadline 13:25:04 UTC. The three assigned paths were absent at intake.
This is manuscript authoring under the all-changes-before-consolidated-
reviews instruction. Only the two new LaTeX files and this note were edited.

## Written extent and exact scope

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/hedges-and-completeness.tex` | 321 lines; five definitions/boundaries and nine results | `0D52159D2D0791FDD2F643C41B2FBDA8852A65C686C953B1DE4D2799585785C3` |
| `handbook/annex/p16/hedges-and-completeness.tex` | 630 lines; nine full proofs | `F56575BC752856D8CD4DF1B5695B8606755C6D4AE6B401E7D81EC44438819A3E` |

The actual complete body and annex were read back, including the final
coordinate-elimination refinement. These are complete proofs of the
stated results; they do not claim unrestricted fixed-binary/ternary or
zero-support completeness.

The nine reciprocal suffixes use body prefix `thm:p16-` and annex
prefix `annex:p16.`:

| Suffix | Proven content |
| --- | --- |
| `hedge-singleton-reduction` | Exact structural removal/restoration of constant coordinates, equality of every retained intervention law, positivity and identification equivalence. |
| `hedge-failure-extraction` | Failure-path normal form; at most one district split; raw failure meets the original action set; common directed forests and an extended bidirected spanning tree give an original-query hedge. |
| `hedge-positive-parity` | Two binary forest models with the same full strictly positive law and root-parity intervention probabilities 1/2 versus epsilon. |
| `hedge-alphabet-lift` | Positive-weight fibers of a surjective decoder, explicit finite private inputs, equal positive lifted observations, and exact decoded intervention laws. |
| `hedge-binary-routing` | Independent graph extension and noisy external parity transport to the original response, preserving equal positive observations. |
| `hedge-four-state-routing` | Full core/relay construction for arbitrary hedge-to-response routes; legal total equations, positive equal pair laws, original-query discrepancy, and removal of unused coordinates. Only traversed nonroot forest vertices need four values; other vertices need two. |
| `hedge-completeness` | Positive-law ID/do-calculus completeness when all nonconstant domains have at least four values; completeness for full nonaction responses on every nonconstant finite domain; further individual failure certificates under the proved routing/cardinality condition. |
| `hedge-all-effects` | For all nonconstant finite domains, every effect is identified iff no directed edge lies inside a maximal district, after singleton reduction. |
| `hedge-worked` | Full split/ancestor/failure trace, selected forests, all 16 common observed masses, original-response discrepancy 1/2 versus 3/8, a 3-by-3 positive alphabet lift, and the constant-treatment correction. |

## Source reading and the retained source proof routes

The exact held published source is
`source/references/shpitser-pearl-joint-identification-2006/aaai06-191.pdf`,
SHA256 `33B1FAAB38522381DE79C8A92CBDCD03F25336BD43BA917CB1677634062929BC`.
Its verified publisher URL is
<https://cdn.aaai.org/AAAI/2006/AAAI06-191.pdf>.
Bibliography key: `ShpitserPearl2006JointIdentification`.
No additional primary capture or bibliography entry was needed.

All eight pages, 1219-1226, had been read completely in the foundation
author block. This block reread Definitions 5-6, Theorems 4-6 and their
lifting/completeness arguments, Corollaries 2-4, and Theorem 7 and its
continuation. The relevant complete page images at 1222, 1223 and 1225
were read again. Actual predecessor body statements and the relevant
algorithm annex proofs were read; the previous utility proofs remain
the do-calculus premises. The governing conventions and edition contract
were also read fully. Research and PDF skills guided primary reading and
the durable source note; manuscript PDFs were not generated or inspected.

Source Theorem 4: the parity construction is retained. The annex proves
the tree incidence bijection and separately proves uniformity/independence
of the smaller forest and its outside coordinates in model 2. It therefore
proves equality of the full observed laws, rather than relying on an
unexpanded injectivity assertion. Epsilon zero recovers the source's
even-root-parity support; positive epsilon gives a full-support witness.
General response transport is supplied by explicit equations. Routes
can reenter the old forest in the core/relay construction, with the extra
observed cardinality kept explicit.

Source Theorem 5 remains the preceding complete seven-branch soundness
proof. Source Theorem 6 is implemented through the saved trace: after
initial ancestral restriction and nonancestor action insertion, the
nonaction set is the original post-action ancestor set A. A split selects
one original district D of A; afterwards only branches 2 and 7 recurse.
If a failed random set avoided the original actions, its ancestry would
put it in A, and district maximality would force it inside D, contradicting
the proper failed pair. Common roots and directed pruning are constructed
explicitly. This corrects the proof shortcut that local actions/responses
are automatically subsets of the original inputs.

The source's subsequent independent-extension and parity-transport routes
are made into explicit positive structural constructions at the original
query. Nonidentification is not propagated by merely asserting that an
unknown child factor remains unknown after a sum or product. The source
Theorem 7 consequence uses the already supplied Lemma 4-8 do-calculus
derivations and is asserted only on the completeness classes proved here.

## Exact remaining obligation

The general strictly positive fixed-domain theorem is still owed when
some unchanged domains have size two or three and no chosen hedge/routing
construction meets the local cardinality condition. In the present
construction the only residual double-coordinate vertices are
`I = (T minus K) intersect H`: nonroot forest vertices traversed by a
selected post-action route. A further proof must either choose a hedge
and routes avoiding the small-domain intersections, or replace those
double-coordinate equations by legal equations on the unchanged small
domains while retaining equal positive full observed laws and a different
original response law. Merely merging or randomly forgetting the two
coordinates does not establish that their causal uses remain available.

This is narrower than a missing positive forest witness, an arbitrary
larger-alphabet lift, a singleton issue, or an untracked recursive query:
all those steps are proved here. No counterexample is claimed to show
that fixed-binary or fixed-ternary completeness is false.

An unrestricted zero-support execution theorem also remains separate.
It needs an exact recoverable action/support domain and a proof of all
ratios used by recursion. The source's phrase about an unsupported action
being undefined is not adopted as structural semantics.

## Integration and notation

Input both files after their `identification-algorithm.tex` counterparts.
Root owns shared drivers, prior forward-boundary updates, bibliography,
registry and admission. No existing file beyond these owned new outputs
was altered, and no independent review, new test or manuscript render ran.

New typed notation includes `\mathbf S`, `\mathcal M^+(G,\mathbf S)`,
constant set C and reduced N-star/X-star/Y-star/G-star; forests F/F-prime
with vertex sets T/S and directed sink roots K; original X0/Y0 and
post-action ancestor set A; tree bits U-e and private parity bit E;
prototype alphabets B-i, observed prototype W-i, fiber decoder d-i,
weights w-i and private choices R-i,b; external routing vertices H and
sinks J; core/relay coordinates C-i/L-i, local four-value set I, and their
noise parameters. All roles are defined before use and remain local.

The existing scoped editorial scan has 25 labels, nine proof statuses,
nine annex items, nine reciprocal pairs and no findings. Its four external
references resolve in the existing foundation/algorithm body files, with
no label collision. The cited bibliography key is present. These are
author structural checks, not independent acceptance or a manuscript build.
