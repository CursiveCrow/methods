# Syllogistic S and S-dagger authoring record

Date: 9 September 2026. Unit: ED26-P02-syllogistic-0001. The authoring scope
is the modern two-fragment calculus selected by the completed edition map.
The lead explicitly assigned the `syllogistic-inference` slug, superseding the
earlier proposed `categorical-syllogistic` path for this body/annex pair.

## Exact primary source

Ian Pratt-Hartmann and Lawrence S. Moss, *Logics for the Relational Syllogistic*,
arXiv:0808.0521v1, submitted 4 August 2008 at 22:26:38 UTC. The primary version
record is https://arxiv.org/abs/0808.0521v1 and the exact PDF endpoint is
https://arxiv.org/pdf/0808.0521v1. The original TeX was obtained separately from
https://arxiv.org/src/0808.0521v1. The selected contribution comprises the
Section 2 definitions and direct-system material needed for S/S-dagger and the
complete Section 3, ending before Section 4 on printed p. 18.

Local originals are under `source/references/pratt-hartmann-moss-2008-v1/`:

| Artifact | Identity and SHA-256 |
| --- | --- |
| `0808.0521v1.pdf` | 442252 bytes, 43 pages, unencrypted; `fbd2ccc0fc5366ddb44e57c6ba5ccb189b550d7e2a9be51c7bc4b533ab206b0e` |
| `0808.0521v1-source.tar` | 48599 bytes; `6d25af678c3877888a1d7b4d4159cc8dbcb1008f92dc9be59b6a082ed7b0ec1c` |
| `relsyll.tex` | 147829 bytes; `307765b10f74be4062f3371cf668bab63632b1b318dd70ecfede9ba039d30ffe` |

The PDF header identifies v1 and 4 August 2008. Its producer metadata dates
the PDF generation to 29 October 2018; that is not a revised research-version
date. The arXiv page separately links the 2009 journal publication,
Review of Symbolic Logic 2(4), 647–683, DOI10.1017/S1755020309990086.
That publication was not substituted for the selected preprint.

The archive member list was inspected before extraction. It contains
`relsyll.tex`, `relsyll.bbl`, `proof.sty`, and four source diagram files.
The selected body was read from the PDF with pypdf, then checked directly
against original TeX, including every Section 3 line (approximately
relsyll.tex 985–1472). Source pp. 3–11 were read for syntax, semantics,
identifications, direct derivations and the distinction from reductio.
No manuscript PDF was built or rendered. The PDF skill supported read-only
source acquisition and extraction; no PDF artifact was authored.

## Complete source-to-manuscript binding

| Source item | Body label | Proof annex label |
| --- | --- | --- |
| Section 2 syntax/semantics and identifications | `def:p02-syllogistic-language`, `def:p02-syllogistic-semantics`, `def:p02-syllogistic-identifications`, `thm:p02-syllogistic-semantic-identifications` | `annex:p2.syllogistic.identifications` |
| Section 3 full S and S-dagger rules; Lemma 3.1; D1 redundancy | `def:p02-syllogistic-derivation`, `thm:p02-syllogistic-rules`; both source rule sheets | `annex:p2.syllogistic.rules` |
| Lemma 3.2, all three parts | `thm:p02-syllogistic-separation` | `annex:p2.syllogistic.separation` |
| Lemmas 3.3 and 3.4; union-closure observation | `def:p02-syllogistic-literal-closure`, `thm:p02-syllogistic-closure` | `annex:p2.syllogistic.closure` |
| Lemma 3.5, including nonempty seed and singleton interpretation | `thm:p02-syllogistic-extension` | `annex:p2.syllogistic.extension` |
| Theorem 3.6, three satisfiable cases and inconsistent premises | `thm:p02-syllogistic-sdagger-completeness` | `annex:p2.syllogistic.sdagger` |
| Theorem 3.7, forbidden forms and minimal inconsistent subset | `thm:p02-syllogistic-s-completeness` | `annex:p2.syllogistic.s` |
| Section 2 Lemma 2.1 specialized to these fixed unary calculi; explicit lookup procedure | `def:p02-syllogistic-saturation`, `thm:p02-syllogistic-saturation` | `annex:p2.syllogistic.saturation` |

The saturation proof includes the no-fresh-atom substitution argument and a
finite bound of eight times the square of the input atom count before formula
identifications. It asserts polynomial time, not the sharper complexity results
proved for other fragments elsewhere in the source. The separate finite-model
observation is not used as a claimed polynomial brute-force model search.

## Source reconstruction choices and direct corrections

The original rule-instance proof illustrates D and calls the remaining cases
similar. The written proof expands B by all legal polarity regimes, then A,
T, I, X and N, and explicitly embeds D1/D2/D3 into the dagger D rule.
Soundness is supplied for every rule instead of leaving it implicit.

The source's closure-definition sentence prints `S^Phi` where the subsequent
notation and defining set require `V^Phi`. The active text consistently uses
the corrected V notation. This provenance remains here, outside the derivation.
Source applications of A using implicit universal contraposition are written
as the actual A step followed by the declared formula identification. The
universal-case completeness proof enumerates all ordered conflict choices.
The existential case includes both targets coming from one witness literal
and from different witness literals. The restricted-fragment proof treats
only nodes actually connected to the final conclusion of a derivation tree.

The worked categorical cases were calculated directly: oak/tree/plant
inclusion, explicit oak existence, a positive/negative witness chain, a
singleton with empty predicates, the empty-universe failure of N, and
inconsistent categorical premises. No software test suite was created.

## Integration and current standing

Written files:

- `handbook/parts/p02/syllogistic-inference.tex`
- `handbook/annex/p02/syllogistic-inference.tex`
- `handbook/registry/calculi/p02-syllogistic-s.tex`
- `handbook/registry/calculi/p02-syllogistic-sdagger.tex`
- `handbook/bib/intake-p02-syllogistic.bib`
- `handbook/registry/symbols-intake-p02-syllogistic.csv`

The body inputs its two uniquely owned sheets. The lead must route body and
annex through the P2 drivers and merge the unique intakes. Canonical records
and drivers were not edited by this writer. The complete author read-through
covered the written body, both sheets and every annex proof; it corrected a
relative example reference and made the first-order translation metavariables
explicit. The source and all selected proof components are authored; this
standing is not independent source, specialist or publication acceptance.

The explicit existing compactness dependency is `thm:fol-compactness` in
`handbook/restoration/inherited-04921-04967.tex`, already used on the P2 route.
Historical reader navigation currently links Part13. The exact separately
mapped history obligations are ED26-SRC-063-0102, *Aristotle's early logic*,
and ED26-SRC-063-0103, *Aristotle's underlying logic*, with proposed
`handbook/parts/p13/presentations/src063-0102.tex` and `src063-0103.tex`.
Once those treatments are integrated, their specific reader labels should
replace or supplement the broad Part13 link. No unchanged identification of
the modern calculi with Aristotle is made, and those complete historical
source presentations remain separately owed.

All eight proved statuses have complete reciprocal annex items. Independent
reviews and whole-manuscript build/output checks remain part of the later
consolidated change-set review, as directed by the user.
