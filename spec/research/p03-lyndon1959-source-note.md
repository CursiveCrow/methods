# Lyndon 1959 preservation: source and authoring record

Unit: `ED26-REQ-N-a-011-02`; parent requirement `N-a-011`; allocated
subcomponents `N-a-011-MAP-03` through `N-a-011-MAP-06`. Authoring block:
2 October 2026 UTC (1 October Pacific time). Shared drivers, canonical
bibliography, canonical symbol registry, coverage-map and queue records
are owned by the lead and have not been edited by this writer.

## Actual held sources and reading

The predecessor writer acquired two distinct publisher originals. Their
PDFs and acquisition receipt were retained, not reacquired or overwritten.
I read the complete mathematical text and reference pages of both originals
from their full physical-page extraction, and inspected the actual page
images for the equations identified below.

- `source/references/p03-lyndon1959/lyndon-1959-preservation.pdf`:
  Roger C. Lyndon, *Properties Preserved under Homomorphism*, Pacific
  Journal of Mathematics 9(1), 1959, printed pp. 143--154; DOI
  `10.2140/pjm.1959.9.143`; 15 physical pages including cover and journal
  back matter. SHA-256
  `B7610FBAFAE210B7B978EA9ABD4BD2010914E316CC262CB2F87BF301DB78E46C`.
- `source/references/p03-lyndon1959/lyndon-1959-interpolation.pdf`:
  *An Interpolation Theorem in the Predicate Calculus*, same journal issue,
  printed pp. 129--142; DOI `10.2140/pjm.1959.9.129`; 17 physical pages
  including cover and journal back matter. SHA-256
  `58E0D3C7BAEC2297BF35EA126CF751C06A38BAAA69794254522DDAFCB9195888`.
- Publisher URLs, acquisition time, readable-text hashes, byte counts,
  normal-TLS receipt and full-page capture identities remain in
  `source/references/p03-lyndon1959/acquisition.json`. The matching
  `.reading.txt` files are full physical-page extractions, not facsimiles.
  The older rotated-text extraction issue was already repaired by plain
  extraction, but displayed formulas still require visual reading.
- Source images inspected: preservation physical page 4 (printed 145),
  physical page 11 (printed 152); interpolation physical pages 11--13
  (printed 138--140), under `tmp/pdfs/p03-lyndon1959/`. The only new
  rendering in this block was preservation physical page 4. These are
  source-page inspections, not manuscript builds or manuscript renders.

## Written destinations and source-component mapping

Body: `handbook/parts/p03/presentations/n-a-011-02.tex`, entry
`sec:p03-n-a-011-02`. Annex:
`handbook/annex/p03/n-a-011-02.tex`, section
`sec:annex-p03-n-a-011-02`. The `annex:p3.n-a-011.2.*` items are
reciprocal to the body's exact `proved=` statements.

| Source locator | Written result / content |
| --- | --- |
| 143--144 | Onto-image convention, functions, positive syntax, commutativity and cancellation, original historical qualifications, wider elementary classes, explicit distinct interpolation import |
| 144--145 | Polarity, priming, relation-inclusion theory, Propositions 1 and 2, Corollary 2.1; complete structural-induction and interpolation proof |
| 145--147 | Star duality, Q-maps, congruence quotient, complete expanded diagram, Proposition 3 with named embedding and relabeling |
| 147--148 | Theorem 4, consistency construction and reverse implication, Corollaries 4.1 and 4.2 |
| 148--150 | Auxiliary binary e versus genuine identity; all three Theorem 5 cases; enlargement/projection factorization; mixed-direction generalization boundary |
| 150--151 | Corollaries 5.1--5.3, strengthened two-system elementary-extension observation, Theorem 5' and all relative corollaries, torsionfree-group example |
| 151--153 | Non-elementary finite-set class; non-elementary homomorphic-image class; S and S_n, p.152 matrix/Boolean-substitution reasoning and its constructive import; decreasing natural-number counterexample |
| 153 | Full finite-axiomatization/recursive-singleton-test undecidability reduction, including both source examples and their external undecidability premises |
| Allocated MAP-05--06 | Explicit arbitrary-map / existential-positive versus onto-map / positive separation; universal-quantifier counterexample; formula-to-sentence constants bridge; falsum and all-structure/finite-only boundaries |

## Mathematical clarifications and correction provenance

1. The freely interpreted binary `e` and newly named `e_A` are not logical
   equality until the relevant congruence quotient is taken. Thus an
   auxiliary elementary extension of a genuine-identity system need not
   itself have identity on its new elements. This is why Theorem 5's
   quotient step remains essential.
2. In genuine-identity systems, a noninjective congruence projection is a
   `{e}`-map, not an auxiliary empty-set-map reflecting identity. Source
   p.149's projection terminology can otherwise be read inconsistently
   with its p.146 definition. The body makes this stage distinction
   explicit and the annex proves the induced quotient map directly.
3. Proposition 2's proof on p.145 calls its finite conjunction C positive,
   although no such assumption is present in its statement. No extra
   hypothesis is needed: the right-hand interpolated implication alone
   excludes negative occurrences of selected q in the interpolant. The
   annex proves the statement as actually quantified.
4. Removal of named constants from the Theorem 4 interpolant is justified
   by replacing the finitely many constants by fresh variables and
   universally closing. The relation polarity theorem alone does not
   assert that arbitrary operation symbols are shared. This step and the
   removal of the fresh relation `e_A` are distinguished explicitly.
5. The backward Q-map argument cannot simply identify different domains.
   The annex supplies either the direct onto-map induction or the source's
   common-domain enlargement argument after pulling target relations back
   along the onto map.
6. On preservation p.152 the dot notation places `r(x,y)` as a conjunct
   outside `r(x,z) -> (r(x,t) and r(z,t))`. Placing it inside the antecedent
   makes the source's intended chain assertion vacuous when that edge is
   absent. The written S and Skolem matrix have the verified grouping.
7. The corollary-5.2 inclusion needed for the converse is Pi-models inside
   Gamma-models; the source's repeated same-direction inclusion does not
   prove equality. The annex uses both correct directions.
8. The p.152 chain example now also has an explicitly distinguished
   supplementary elementary-diagram verification. It proves the exact
   original conclusion and does not replace the source's retained
   positive-matrix / atomic-Boolean-substitution derivation.
9. The reconstruction uses plain A, B, C for the source's Fraktur structure
   letters. The source named constants w_a, V,W,R,rho,Q, star duality,
   e,e_A, and source truth constants retain their declared roles. Structure
   interpretations are typed explicitly rather than identifying auxiliary
   congruence semantics with genuine-identity semantics.

## Exact dependency boundary and outstanding work

The preservation article imports the polarity interpolation theorem; it
does not supply its proof. The body reproduces that exact sentence-level
sign restriction as `cited=Lyndon1959Interpolation`, not `proved=`. It
also states the separate article's constructive Main Theorem used by the
p.152 example, again as a cited import, with its exact Skolemization,
duplication, specialization, and per-matrix atom-injectivity definitions.
No complete proof of the separate
14-page interpolation article is claimed supplied by this block, and no
other queue unit receives duplicate whole-article credit from these imports.

There is a specific source-proof issue for a future full interpolation
reconstruction. On printed p.138 the term transformation is defined by
`chi(eta sigma' y_r^(delta i)) = chi(eta sigma_0 y_r^(delta i))`, with
copy-indexed fresh Skolem symbols on the right. Equal instantiated old
Skolem terms from distinct copies can make two left-hand sides identical
while their prescribed right-hand sides have distinct fresh heads. The
printed proof does not explicitly establish consistency of these clauses.
For example, an existential variable preceding all universal variables
has an old zero-ary Skolem term s. In two duplicated copies the left
side is chi(s) in both clauses, whereas actual reskolemization uses
different copy-indexed heads s_0^1 and s_0^2 on the right. No choice of
the substitution for universal variables separates that old constant.
This exhibits the well-definedness problem for such a multi-copy step;
it does not prove that the intended construction admits no repair.
The images were read, including the second transformation on p.139 and
the injectivity argument on p.140. I have not established a full repair
of this well-definedness issue. It is not a counterexample to the
interpolation theorem itself. Citing its established theorem is distinct
from newly asserting this particular term-transformation proof complete.
The separately supplied diagram proof of the chain boundary avoids relying
on that construction for the newly marked proved chain statement.

Accordingly the preservation-paper proofs, original examples, and the
allocated comparison cases are authored, with the imported source boundary
explicit. Any independently promised full source-native interpolation
derivation remains unsupplied and must not be retired by these two cited
statements. The lead must determine that dependency's mapped ownership,
reconcile the two intakes, and route the body/annex pair. No independent
admission, source review, publication review, manuscript build, manuscript
render, or prose test occurred in this block.

Intakes retained for lead reconciliation:
`handbook/bib/intake-p03-lyndon-preservation.bib` and
`handbook/registry/symbols-intake-p03-lyndon-preservation.csv`.

Author check: read through the actual saved body and all annex proofs;
checked all theorem directions and quotient stages against the originals;
checked the concrete cancellation map, descending-chain counterexample,
singleton truth-assignment procedure, relative endpoint restriction, and
falsum case by direct mathematical calculation. These are authoring checks,
not independent acceptance. The two PDF hashes were recomputed locally and
match the held acquisition receipt.
