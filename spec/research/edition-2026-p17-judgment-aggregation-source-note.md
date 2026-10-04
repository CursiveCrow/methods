# Judgment aggregation: exact source and completed authoring

Date: 9 September 2026. Unit: `ED26-P17-judgment-aggregation-0001`.

## Source acquisition and reading

The exact author PDF was acquired from
<https://personal.lse.ac.uk/LIST/PDF-files/AGG1.pdf> and preserved at
`tmp/pdfs/p17-judgment-aggregation/AGG1.pdf`.

- Size: 208,891 bytes.
- SHA-256: `BDA8CA72D36B601F1756F39FC84CF7318B9E867EA23A6F7E9938622627CC7B05`.
- Physical pages: 33; the printed page numbers are 1–33.
- First page: Christian List and Philip Pettit, *Aggregating Sets of Judgments:
  An Impossibility Result*, revised 9 October 2001; marked forthcoming in
  *Economics and Philosophy*.
- PDF metadata title: `Microsoft Word - AGG2.DOC`; author `list`; metadata
  creation and modification on 9 October 2001. The body's identity controls.
- The related 2002 journal article is *Economics and Philosophy* 18(1), 89–110,
  DOI `10.1017/S0266267102001098`. No identity with that publication is assumed.

All 33 pages were read in three uninterrupted source-page ranges: 1–11, 12–25
and 26–33. This covers all four sections, conclusion, complete appendix proof,
references and all eight notes. Poppler `pdfinfo` confirmed the physical document
properties. The bundled `pdftotext` executable was absent, so pypdf extracted the
actual acquired pages for reading. No manuscript PDF was built or rendered.

## Source-to-text allocation

| Source scope | Body treatment | Completed proof |
| --- | --- | --- |
| pp. 2–5: judgments, credences, preferences and institutional aggregation | Opening distinctions and final institutional scope paragraph | Type distinctions; no empirical or normative theorem invented |
| pp. 5–9, 12–13: doctrinal, workplace and majority profiles | `def:p17-ja-doctrinal-profile`, `thm:p17-ja-paradox` | `annex:p17.ja-paradox` |
| pp. 11, 26–27; note 3 on p. 31 | `def:p17-ja-agenda`, `def:p17-ja-rational`, `thm:p17-ja-models` | `annex:p17.ja-models` |
| pp. 13–15, 27–29: U, A, S and Theorem 1 | `def:p17-ja-uas`, `thm:p17-ja-counts`, `thm:p17-ja-impossibility` | `annex:p17.ja-counts`, `annex:p17.ja-impossibility` |
| pp. 16–19: convergence, alignment, Theorem 2 and five-person example | `def:p17-ja-aligned`, `thm:p17-ja-median` | `annex:p17.ja-median` |
| pp. 19–23: authority and priority, including incomplete priority outputs | `def:p17-ja-priority-procedure`, `thm:p17-ja-authority-priority` | `annex:p17.ja-authority-priority` |
| pp. 23–24: unanimity, strict supermajorities and Theorem 3 | `thm:p17-ja-unanimity`, `def:p17-ja-finite-issues`, `thm:p17-ja-supermajority` | `annex:p17.ja-unanimity`, `annex:p17.ja-supermajority` |
| pp. 24–26: relaxing consistency/closure and the six-strategy comparison | `sec:p17-ja-escapes`, `thm:p17-ja-boundaries` | `annex:p17.ja-boundaries` |
| note 4, pp. 31–32: systematicity relative to an equivalence relation | `def:p17-ja-relative-systematicity` | Precisely defined source variation; no unsupported general impossibility claimed |
| notes 5–8: ties, scope and attribution | Even/odd theorem statement, full original proof and source-version opening | n=2 and all odd n handled explicitly; List's authorship retained |

The selected source supplies the original impossibility proof. The annex
reconstructs that exact profile and case split, filling the support-vector
realizability and smallest-electorate details. The source states the two positive
theorems and gives the median intuition; this authoring supplies their complete
proofs, not an invented assertion that the preprint contains those full proofs.
The individual axioms and examples come from this source rather than Arrow's
preference-aggregation theorem or a later analogous result.

## Technical choices and explicit boundaries

The source's `Phi_i` notation is replaced locally by defined `J_i`; this is only
a notation bridge. The agenda follows the actual appendix's opposing-formula
condition. It is not silently expanded to the full propositional language, and
it is not falsely declared finite in the impossibility theorem. Closure is
`cl_X`, semantic consequence restricted to the agenda.

Weak consistency means exclusion of a literal formula/negation pair. The proof
that weak consistency plus closure implies satisfiability uses an available
literal opposing pair, handling an empty agenda separately; it does not assume an unproved finite-agenda
equivalence. Complete rational sets are then characterized as valuation truth
sets restricted to the agenda. This gives genuine admissible inputs for every
vector and every row of the impossibility construction.

For even electorates the shared count is n/2. For odd n=2m+1 the source profile
gives m+1 supporters to each of p, q and not(p and q), and m supporters to their
conjunction. Both possible common acceptance values are contradicted. No
monotonicity, Pareto condition or unanimity preservation is imported.

The support theorem has a separate finite agenda with disjoint issue pairs.
It uses support **strictly greater** than (k-1)/k, following the source's prose
immediately before Theorem 3. The source's running agenda has at least three
issues; the supplied proof works for k at least two. It does not assert the
false extension with k=1 and threshold zero. At most k accepted propositions
have coalitions whose complements each contain fewer than n/k people. Their
intersection contains an individual whose coherent judgments include all the
accepted propositions, proving joint satisfiability and the consistency of the
closure. An inclusive two-thirds boundary on the three-issue paradox fails this
guarantee.

The four-person profiles used to demonstrate failure of closure and of
systematicity after closure are explicit editorial witnesses for the source's
stated qualifications. Both have conjunction-support vector (1,1,0,0), while
the closed supermajority output accepts the conjunction in one and not the other.

Priority's completeness claim includes the missing determination condition:
independent prioritized questions guarantee a satisfiable closed output, but do
not settle every larger-agenda issue unless they determine those issues. Voting
only on a rejected conjunction leaves both atomic questions unsettled. The body
does not promote a conclusion-only decision to a complete judgment set on the
larger agenda.

All six source escapes identify their changed conditions. In particular,
closing majority judgments can lose systematicity as well as consistency;
the source's categories are not treated as a claim that only one condition ever
changes. The constant-full-set example and the one-person/independent-atom
boundaries are explicitly proved logical illustrations, not source policy
recommendations. The note-4 relative-systematicity question is not presented as
a current open problem or as a theorem applying to every partition.

## Files and remaining integration

Owned body: `handbook/parts/p17/judgment-aggregation.tex`.

Owned annex: `handbook/annex/p17/judgment-aggregation.tex`.

Bibliography intake: `handbook/bib/intake-p17-judgment-aggregation.bib`.

Symbols intake: `handbook/registry/symbols-intake-p17-judgment-aggregation.csv`.

All four mapped components are written, including nine complete reciprocal
body/annex proof pairs. The lead still owns routing, canonical bibliography and
symbol integration. This note records authoring and source reading, not
independent source acceptance, publication review, build or visual approval.

The author read the complete written body and annex and the two intakes. That
read-through made rational-input assumptions explicit in the median theorem,
typed the aggregation domain, and generalized the elementary truth-set lemma
to every opposing-pair agenda, including the empty boundary. Direct arithmetic
calculations confirmed the doctrinal output and its closure, both four-person
supermajority outputs/closures, and the original source profile counts for
electorates of sizes 2–9. The general results are established by the written
proofs, not by those finite calculations. A bounded structural check found nine
reciprocal theorem/annex pairs, nine complete annex proof environments and zero
body proof environments. No prose-mirroring test suite was created.
