# Rado 1964: complete original theorem presentation

Authoring checkpoint: 1 October 2026. Requirement family: N-a-002;
presentation: the original Rado 1964 article. This note records completion
of authoring and local source checks. It does not grant independent admission,
publication acceptance, build acceptance, or rendered-manuscript acceptance.

## Exact source and reading extent

Richard Rado, *Universal graphs and universal functions*, Acta Arithmetica
9(4) (1964), 331-340, DOI `10.4064/aa-9-4-331-340`.

- Local source: `source/references/rado-1964/rado-1964-universal-graphs-functions.pdf`.
- SHA-256: `F484D5935DE4E3710AF7FDBC2CCE8D78BB46E8E7B774D903F6225A17781059F7`.
- Size: 1,948,597 bytes; six physical scanned spreads. PDF 1.4, unencrypted.
- Physical page 1 contains printed page 331 on the right; pages 2-5
  contain printed pairs 332-333, 334-335, 336-337 and 338-339; physical
  page 6 contains Rado's final page 340 on the left. The neighbouring
  Erdős-Ingham article on the right is outside this source presentation.
- All ten printed pages were read from the saved source spreads, including
  every theorem, proof, footnote and the final questions. The empty text
  extraction is not evidence of an empty source: this is a scan.
- [Publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/9/4/95477/universal-graphs-and-universal-functions)
  confirms the title, year, journal, page range and DOI. Its free-download
  link is labelled CC-BY. This is the observed publisher statement, rather
  than a separate rights-admission verdict.
- [EuDML record](https://eudml.org/doc/207488) identifies issue 4. The record
  was available in search results; direct retrieval returned HTTP 403 in
  this session. The issue is also printed in the article footer on page 337.

The PDF skill supported source reading. No manuscript PDF was created or
rendered. Existing saved drafts were read in full before revision; the
completed body and annex received an author read-through in this block.

## Authored content and source correspondence

The body is `handbook/parts/p03/presentations/rado-1964.tex`; the proof
annex is `handbook/annex/p03/rado-1964.tex`. There are twelve reciprocal
statement/proof pairs. The six original numbered theorems remain distinct.

| Original source | Complete supplied content |
| --- | --- |
| 1.1, pp331-332, Theorem 1 | Simple graphs; weak and induced embeddings; the separating two-vertex example; binary-digit graph; recursive increasing induced embedding preserving nonedges as well as edges. Finite and empty inputs are handled explicitly. |
| 1.2, pp332-333, Theorem 2 | Local finiteness; exact-step reachability with repeated walk vertices; de Bruijn's ray-and-leaves diagonal tree; nonuniversality even for weak embeddings. |
| 2.1-2.3, pp333-335, Theorem 3 and the coding lemma | Fixed-dimensional incidence complexes without a face-closure axiom; the binomial code tau; colexicographic consecutive-rank calculation and telescoping identity; full incidence and nonincidence verification. The original zero-dimensional footnote is included. |
| 2.4, p335, Theorem 4 | All nonempty finite simplex sizes; the mixed binary-subset code rho, including the empty prefix; recursive representation of every membership pattern. Membership of an empty simplex is kept outside the source domain. |
| 3, pp335-337, Theorem 5(a),(b) | Fixed-length and all-finite-length increasing colour functions; both digit identities; the two recursive embeddings and coefficient comparisons; fixed colours; the oriented/modulo-k interpretation. An additional unary boundary is explicitly distinguished from the printed ell-at-least-one part (a). |
| 4.1-4.2, p337 | Initial ordinals; original index-valued cf(n); the source predecessor convention n-1; the successor-length final-maximum domain F(l,m,S), including repetitions; full colour-retraction/arity-restriction proof. |
| Theorem 6 and 4.3 Case 1, pp338-339 | Both regular regimes, including all original GCH, arity and colour bounds; template counting; one fixed universal function; recursive choice of an increasing representation. |
| 4.3 Case 2, pp339-340 | Singular regime with the strict colour bound; successor-sized ordered blocks; exact order type of the block sum; per-block template counts; block-preserving increasing recursion; verification on every source tuple. |
| Discussion after Theorem 6, p338 | Historical questions about argument restrictions, sequence lengths and nonuniversality, with no claim about their present open status. |

The modern graph extension property, uniqueness/homogeneity, identification
with the separately supplied Fraïssé graph, free graph amalgamation and
the forest obstruction are explicitly identified as additional interfaces.
They do not replace any of the six original theorems. The Fraïssé 1954
presentation and Hodges source obligations remain separate.

## Repairs and precise boundaries

**Repeated final maxima.** The source domain on pages 337-338 is non-strict:
every earlier coordinate is at most the final coordinate. The regular
and singular proof reconstructions retain this domain. A marked prefix
template describes every occurrence of the new maximum before its image
is chosen. The template's tagged domain includes the empty prefix and
all arities below l; its evaluation rule is total once the vertex-to-template
assignment is fixed. Its encoding is injective for each arity and every
old image lies below the chosen bound. Thus no circular dependence on the
as-yet-unselected new image remains. This marked reconstruction is a
repair of the original proof scheduling, not a claim that the original
article printed the marker construction.

**Order type.** Page 337 says that m may be assumed to be an initial
ordinal. An arbitrary cardinality transfer does not preserve this ordered
argument domain. The active definition retains the specified ordinal
order type, and original Theorem 6 retains its exact initial-ordinal target.
The added full proof `thm:p03-rado64-order-type-boundary` shows that
F(2,omega+1,{0,1}) has no universal member, whereas the countable initial
ordinal case F(2,omega,{0,1}) does. Domain preservation forces the injection
to be increasing and to fix the final omega vertex; the diagonal pair
(omega,omega) then supplies a contrary colour. The reader receives a
correct domain and proved boundary, rather than an instruction to repair
an earlier incorrect theorem.

**Arity.** The added `thm:p03-rado64-arity-obstruction` proves that
F(omega,omega,{0,1}) has no universal member by diagonalizing the host's
repeated-vertex profiles across all finite lengths. This does not change
Theorem 5's strictly increasing tuple domain or Theorem 6's arity bounds.

**Published notation.** The final body uses the source tau fixed-length
code, rho mixed-length code, psi(xi) fresh digit position, index-valued
cf(n), and n-1 predecessor convention. Ordinary cardinal cofinality is
distinguished by its cardinal argument. The source proof's cardinal
estimates are retained with explicit multiplication, exponentiation,
regularity and strong-limit justifications. A helper cardinal predecessor
in the supplied proof is called zeta, leaving rho with its published
digit-code role. The old draft aliases tau-ell, sigma, c(n), n-minus and
M-xi have been replaced coherently in definitions, formulas, proofs and
the symbol intake.

The source's final discussion prints the phrase "second kind" beside its
parenthetical lambda+1. This does not authorize extending the displayed
successor-length argument domain to limit-length sequences; the precise
domain and historical-question status remain explicit.

## Intakes and root integration

- `handbook/bib/intake-p03-rado-1964.bib`: enrichment of the existing
  `Rado1964` key, including issue, source locator and language; no new
  bibliography identity.
- `handbook/registry/symbols-intake-p03-rado-1964.csv`: 32 typed rows,
  including distinct scopes for the marked-template h and the rejected
  candidate-host h in the two nonuniversality proofs.
- Add one body input and its matching annex input in the P3 drivers.
  The writer did not modify shared drivers, canonical bibliography,
  canonical symbols, scope bindings, generated files or admission records.
- The suggested exact scope bindings are:

```json
{
  "P3 Rado 1964 universal graphs and functions": {
    "presentation": "Original Rado1964 theorem presentation with explicit modern graph and nonuniversality interfaces",
    "regions": [
      {"anchor": "sec:p03-rado-1964"},
      {"file": "annex/p03/rado-1964.tex"}
    ]
  },
  "P3 Rado 1964 marked templates": {
    "presentation": "Marked-prefix template h in the corrected full final-maximum proof",
    "regions": [
      {"anchor": "def:p03-rado64-marked-template"},
      {"anchor": "annex:p03.rado64.transfinite"}
    ]
  },
  "P3 Rado 1964 nonuniversality proofs": {
    "presentation": "Candidate universal host h in the two stated repeated-argument counterexamples",
    "regions": [
      {"anchor": "annex:p03.rado64.order-type-boundary"},
      {"anchor": "annex:p03.rado64.arity-obstruction"}
    ]
  }
}
```

The local structural check found twelve body `proved=` targets, twelve
annex back-references and no reciprocal mismatches. All 32 intake
first-use labels exist in the actual body or annex. These are bounded
authoring checks, not an independent mathematical review. The arithmetic
and recursion arguments were read through branch by branch; no manuscript
build, rendering, prose test suite or review wave was run.

Final body: 376 lines, 17,578 bytes,
SHA-256 `E35B5A9E2841EBA6E5A43CD1D9CE3079567E813B3F2ACA1A57BE5011AFBFC468`.
Final annex: 448 lines, 21,945 bytes,
SHA-256 `190830C5F84886BAC45429838F82BD5E80CF391735C82701622FAEC191CA6A6E`.
Symbol intake SHA-256:
`2AEBAA5577FB960404201D468120649EE5ACC493364BC57030853411CC1C4B64`.
Bibliography intake SHA-256:
`3BFF7D992E7A78784CAEDC477FE11311F3394766F6C8923F6CAC52F33BD95BAE`.

No authoring proof gap remains in this original-source unit. Root integration
and the later consolidated independent/static/build/publication work remain.
