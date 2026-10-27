# Defined-negation LK: author proof completion

Date: 2026-10-26. Standing: author completion and bounded verification;
not independent acceptance, source admission, or book completion.

The active body is `handbook/parts/p07/calculi-and-derivability-supplement.tex`.
Its reciprocal annex is
`handbook/annex/p07/calculi-and-cut-elimination-supplement.tex`. The similarly
named files without `-supplement` are not the active route and were not edited.

## Material inspected

- `source/formal-logic-reference.tex`, original Part VIII, lines 11379--11626:
  finite multisets, the defined-negation rule surface, total substitution,
  eigenvariable conditions, derivations, and the explicit soundness sketch.
- Current `handbook/registry/calculi/lk.tex` and `lk-defneg.tex`, including
  their exact Mix side conditions. The canonical sheet has 20 rules; the
  defined-negation sheet has 18.
- `handbook/restoration/inherited-03519-03680.tex`: the actual coincidence
  and substitution results invoked in the soundness proof.
- `annex:p02-w02-p02-028-st-lk-translation`, in the P2 Herbrand annex:
  the already complete forward translation, including free/all-variable
  preservation and commutation with deterministic capture-avoiding substitution.
- The existing later P7 LK--ND and completeness proofs, to preserve their
  dependency direction and prevent circular use of the comparison result.

No new external primary source or bibliography entry is claimed. The original
soundness source is explicitly a sketch; the new argument is separately
authored reconstruction for the registered calculus. The frozen source and
the separate `thm:p07-source-lk-soundness` route remain unchanged.

## Completed arguments

`thm:p07-lkd-soundness` now has a complete derivation-height proof at
`annex:p7.calculi.1`. It checks every rule using an antecedent-true,
succedent-false counterexample, including both structural contractions,
split contexts, Mix with repeated formulas and further side occurrences,
all six connective rules and all four quantifier rules. The two eigenvariable
cases explicitly allow the sheet's legal case `y = x`; when the variables
differ, freshness and coincidence justify the assignment change. Empty
contexts are included.

`thm:p07-lk-presentation-equivalence` now has a complete proof at
`annex:p7.calculi.2`. The forward translation covers every canonical rule;
the reverse embedding simulates split implication-left by weakening the
premises to shared contexts. Embedding alone yields only the translated
sequent, a missing step in the former sketch. The new strong induction
constructs both formula bridges, from each formula to its defined-negation
translation and back, for atoms, falsity, negation, all binary connectives
and both quantifiers. Occurrencewise Cuts then recover the original sequent
and its exact multiplicities. The atomic clause of the body definition is
now explicit.

Only these two editorial result statuses changed from `sketched` to `proved`.
All labels are preserved. The comparison still asserts neither equality of
proof objects nor preservation of Cut occurrences, cut-freeness, height or
size. It does not add equality rules or infer intuitionistic soundness.
The later `CALCULI.3` and `CALCULI.4` proofs are unchanged.

## Verification

The final applied files were built with TeX Live 2025 through
pdflatex/biber/pdflatex/pdflatex: all passes exited zero, producing 23 pages.
There are no TeX errors. Thirteen overfull warnings remain in existing
tables, headings and sheet material; three overfull prose lines introduced
by the new proof were corrected. Eleven external reference warnings are
expected in this isolated unit. Its new proof dependencies were separately
checked to resolve uniquely on the actual full reader route.

Both changed files have balanced environments; the two proved body results
and their reciprocal annex items occur uniquely on the active route. The
exact 18/20 rule counts were checked against the sheets. This structural
audit does not replace mathematical review. The new proof pages were rendered
and inspected, including the eigenvariable argument, the formula bridges,
and the occurrencewise Cut step; pages 15 and 16 were reinspected after the
line-overflow corrections.

Exact build and structural evidence is saved in the task workspace under
`p03-finite/p07-calculi-build-applied/report.json` and
`p03-finite/p07-calculi-verification.json`. The final body SHA-256 is
`403f0d84ac1dcda20b8f3908b090818db6ddc78184a10263de9c6ea6696d2f8a`;
the final annex SHA-256 is
`d870f4b12c835b72b98ba7b08d2779524e8a97af8a5fe68f4c680ef224c2ea74`.

Five navigation surfaces outside the assigned pair still described these
proofs as sketches when inspected: the two rule-sheet footers, the P14
classical-calculi comparison, the P7 proof-complexity navigation table, and
P2 packet w02b-p02-009. Exact wording corrections, preserving the absence
of a cut-free-preservation claim, were staged as `p07-navigation.patch` with
input hashes for the parent integrator. Their application belongs to the
integration record, not this author's proof-status claim.
