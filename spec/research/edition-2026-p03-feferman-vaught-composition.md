# Feferman–Vaught reduced-product and bounded-power continuation

This is the authoring/provenance record for the disjoint continuation of planned section **27.6, Feferman–Vaught composition and Boolean powers**. It is not an independent review, admission record, coverage-ledger edit, or whole-source completion claim. The original allocation remains **ED26-SRC-048-0009**, Hodges (1993), Chapter 9, with C006 §9.6 pp.458–466 and C007 §9.7 pp.466–473. Original Feferman–Vaught (1959) and Frayne–Morel–Scott (1962, with its 1963 correction) remain separate identities. Nothing below substitutes a later presentation for either original.

## Current-reader evidence for replacing a stale absence observation

The existing body `handbook/parts/p03/feferman-vaught-and-boolean-powers.tex` is already included by `handbook/parts/p03.tex:30`; its reciprocal proof file is included by `handbook/annex/p03.tex:6`. Both were read completely in this block, not inferred from a title or search hit.

Existing body SHA-256: `a2bed5bd6821a9b3645ecbcb43996deeee6d27c91447c956f722803286696cea`.
Existing annex SHA-256: `ce3fbb2ad0484df34b6812b804942c1d12ed2eabc78dd63d1feb8525cc6fa1c7`.

The actual current anchors and extent are:

| Existing reader anchor / line | Reciprocal proof anchor / line | Supplied content |
| --- | --- | --- |
| `def:p03-fv-standing`, body19; `def:p03-fv-product`, body38 | `annex:p03-fv-coordinate-terms`, annex61 | Finitary many-sorted product, nonempty sorts, indexed AC, empty-index case, coordinate term evaluation and atomic truth criterion. |
| `def:p03-fv-boolean-language`, body64; `def:p03-fv-reduction`, body85; `thm:p03-fv-direct-reduction`, body130 | `annex:p03-fv-direct-reduction`, annex257 | Explicit effective recursive reduction to the first-order Boolean algebra of index sets, including all signed patterns, zero cells, fresh binders, and an actual chosen existential witness. |
| `thm:p03-fv-worked-existential`, body147 | `annex:p03-fv-worked-existential`, annex76 | Worked global-negation existential condition, not coordinatewise universal negation. |
| `def:p03-fv-partition-power`, body161; `thm:p03-fv-power-structure`, body187 | `annex:p03-fv-power-structure`, annex95 | Finite labeled partitions modulo common-refinement equality, operations, relations, and arbitrary factor-formula values. |
| `thm:p03-fv-power-reduction`, body197 | `annex:p03-fv-power-reduction`, annex130 | The same reduction with genuine finite base witnesses; no infinite Boolean joins or indexed witness choice. |
| `thm:p03-fv-power-representations`, body221 | `annex:p03-fv-power-representations`, annex169 | Finite-range represented powers and bounded continuous Stone powers, including empty Stone spaces. |
| `thm:p03-fv-power-elementarity`, body237 | `annex:p03-fv-power-elementarity`, annex204 | Base/coefficient elementary embeddings, elementary equivalence, and the finite-range elementary subpower. |
| `thm:p03-fv-patching-characterization`, body249 | `annex:p03-fv-patching-characterization`, annex237 | Constants, clopen equalizers, and binary clopen patching characterize the bounded power. |
| `thm:p03-fv-boundaries`, body262 | `annex:p03-fv-boundaries`, annex3 | Product negation, non-elementary diagonal, noncompact locally constant maps, ring-idempotent distinction, and the missing-choice witness family. |

Therefore a record saying this whole planned section has no substantive manuscript treatment is contradicted by the actual routed reader. The supported replacement is **substantial partial treatment / original-source obligations still open**, not source-complete or independently accepted. The existing nine pairs were preserved unchanged. The earlier raw intake hashes remain `8f2174ddbdd8c4ae55afa776aaf45de4907c665757b816a05126708fbee3a8c8` (symbols) and `deff3cee644f702a8a1d868f7e371535f444b5309f8d56f28fdefffc3629ac81` (bibliography).

The original reader's active 192-line restoration `handbook/restoration/inherited-06942-07134.tex` was also read completely. It supplies the actual ultraproduct construction, term induction, full Łoś induction, diagonal elementarity, and its Choice standing. The current `types-ultraproducts-supplement.tex` was read; its additional compactness proof and cited Keisler–Shelah statement are not reduced-product composition. Search located other product/Horn mentions only to orient this block; a search miss was not used to claim global absence.

## Sources actually read

1. **Burris and Sankappanavar, author-hosted Millennium 2012 update**, `source/references/p03-feferman-vaught/burris-sankappanavar-2012.pdf`, SHA-256 `73b9caad7441f372a2f309a498e68271a9b16cabd0caf4973c5f25972aa39549`. Read all IV§5, printed pp.141–144 and the Exercise4 continuation on p.145, corresponding to PDF pages155–159. The source's starred power, Stone-space star, coefficient operation `B_1*B_2`, filter congruence `theta_F`, and clopen equalizer notation are retained with their types. The source is the corrected 2012 author body, not the 1981 bytes. Source landing page: [author's universal-algebra page](https://math.uwaterloo.ca/~snburris/htdocs/ualg.html); [actual 2012 body](https://math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf).
2. **D'Aquino–Macintyre arXiv:2307.10465v1, 19 July 2023**, held at `source/references/p03-feferman-vaught/daquino-macintyre-2023-v1.pdf`, SHA-256 `befd92796753ae1ba51edcf657828c8bdde14883a810ad88a18ac574b95c1619`. Read actual pp.6–11 in this block, covering Axioms2–5, local Boolean values, witness choice, complete partitions, patching, and Theorem2.10's inductive construction. Its ring/idempotent hypotheses are not silently attributed to arbitrary signatures. [Exact preprint](https://arxiv.org/pdf/2307.10465v1).
3. **Saeed Ghasemi, arXiv:1411.0794v3**, acquired as `source/references/p03-feferman-vaught/ghasemi-metric-fv-2016-v3.pdf`, 269,968 bytes, SHA-256 `821ed15c69f19a39a181e5ae741267080d35d1e35a3c08daae6b182de5df23ca`. The actual PDF has the arXiv header **5 April 2016** and an internal title-page date **9 October 2018**; both are recorded, not normalized away. Read p.1 and all pp.6–14: discrete classical scope statement, §2.3 construction, atomic lemma, Definitions3.1/3.2, entire Theorem3.3 proof, and Proposition3.6 through its ending. Theorem3.7 and the start of §4 were also encountered on p.14; no additional content credit is claimed for them. [Exact v3 body](https://arxiv.org/pdf/1411.0794v3).

The new ordinary two-valued reduced-product theorem is a separately supplied exact construction/proof using the current finite-pattern recursion and the quotient-Boolean/finite-exception mechanism. It is **not** a transcription of Ghasemi's approximate real-valued theorem, a claim that arbitrary classical formulas are coordinate limsups, or a claim that the original 1959/1962 proofs were read. The two-valued discrete atomic comparison is explicitly proved from values zero/one. Source notation `Omega` for indices, `I` for the ideal, `A_gamma`, `A_I`, `pi_I`, and `[S]_I` is retained; its `I` role is explicitly distinguished from the earlier direct-product index set.

PowerShell's normal HTTPS downloader failed certificate authentication for the new source. A standard Python `urllib.request.urlopen` request, with default certificate verification and an HTTPS final URL, succeeded for the arXiv PDF; no TLS exception, HTTP downgrade, user-agent challenge bypass, login or payment was used. The downloaded bytes were checked as a PDF and hashed. A separately found author-hosted Will Boney note could not be read: the direct HTTPS request returned403, and web fetching timed out. It supplies no manuscript content or source-reading credit. The publisher/EuDML originals remain unheld; this block did not repeat insecure-redirect or challenge-bypass attempts.

## New owned manuscript and proof interface

- Body: `handbook/parts/p03/feferman-vaught-composition.tex`.
- Annex: `handbook/annex/p03/feferman-vaught-composition.tex`.
- Intake: `handbook/registry/symbols-intake-p03-feferman-vaught-composition.csv` (27 rows).
- New bibliography record: `handbook/bib/intake-p03-feferman-vaught-composition.bib` (`Ghasemi2016MetricFVv3` only).

Nine new body/proof pairs share the `p03-fv-` stem and the suffixes:
`finite-partition-lift`, `reduced-well-defined`, `reduced-reduction`,
`reduced-elementarity`, `reduced-example`, `source-power-products`,
`iterated-power`, `power-quotient`, `power-cardinality`.

The new reduction includes exact representatives of quotient partitions; finite unions of all availability failures; actual factor witnesses off that exceptional ideal set; arbitrary filled values on it; equality of the recovered truth classes; all atomic/connective/quantifier cases and the zero-list case. It states the proper-ideal/nonempty-index boundary. Its counterexample has alternating empty/universal predicates modulo the finite-set ideal, showing directly why arbitrary Łoś transfer fails for a proper non-ultrafilter. Factorwise elementary embeddings and elementary equivalence are derived from the computed condition rather than asserted by analogy.

The bounded-power continuation reconstructs Theorem5.4(a–e) with its trivial/empty-space qualifications, including the previously unsupplied two product isomorphisms (d,e). Exercise1 is given an actual finite-rectangle currying proof, preserving the discrete topology on the inner function algebra. Exercise2 is supplied with a complete coefficient-quotient construction, proof of the Boolean congruence, kernel computation, finite-partition surjectivity, and both proper/improper filter cases. Exercise3 has both cardinal bounds under Choice, with the necessary two-element-base and nontrivial-coefficient hypotheses. Its source's module/polynomially-equivalent-algebra Exercise4 is **not** completed by this block.

All proofs are new annex proofs; no body proof or new calculus sheet was introduced. `C(X,A)` and `N_b` are declared in the body before their proof use. The symbol intake distinguishes the index ideal from the earlier index set, Boolean classes from lifted index sets, coefficient filters from the proper index filter, Stone-space stars from clopen-algebra stars, and the external coefficient algebra from base structures. No shared macro is added.

## Integration seam and remaining duties

Root should include this body immediately **after** `feferman-vaught-and-boolean-powers` in the existing P3 product chapter and add its annex after the existing reciprocal file. It is a section continuation, not another chapter. Existing reduction/finite-partition and P10 Stone representation/reconstruction anchors are prerequisites. Root owns all input routes, canonical bibliography, canonical symbol scopes and coverage edits. The saved new files are off-route until root integrates them.

The previous body's mathematical boundary at `def:p03-fv-source-boundary` still says filtered/reduced products require a separate construction; after integration root should point that clause to `thm:p03-fv-reduced-reduction`, while retaining restricted-support and enriched-Boolean distinctions and all original-source duties. No unsolicited edit to that frozen file was made here.

Still open are full acquisition and source-exact reading/reconstruction of Hodges§9.6/§9.7, all their original examples/exercises/corrections; original Feferman–Vaught1959 and Frayne–Morel–Scott1962 plus correction comparison; restricted-support and enriched-Boolean variants with their distinct predicates and domains; other original Horn/products/presentations/word constructions of Hodges Chapter9; and the Burris§5 module exercise. No whole Chapter9, complete original presentation, or metric reduced-product source is credited by these nine new proof pairs.

Author inspection consisted of reading the actual saved body/annex, checking the mathematical dependencies and explicit edge cases, and inspecting owned file hashes. No independent reviewers, software tests, checker run, manuscript build, manuscript render, canonical merge or fulfillment-map update was performed. Those remaining activities are not represented as successful.
