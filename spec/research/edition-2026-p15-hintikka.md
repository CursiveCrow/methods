# Hintikka inductive logic: source and authoring record

Allocation: planned 164.8, `ED26-SRC-063-1009`, Ilkka Niiniluoto,
*The Development of the Hintikka Program*, HHL10 chapter 9, published2011,
pp311–356. This record does not update the fulfillment ledger or admit a
source as independently reviewed. Authoring is bounded and unreviewed.

## Held sources and versions

1. `source/references/p15-hintikka/niiniluoto-hintikka-program-author-copy.pdf`
   was acquired2026-10-03 from the editor's public original HTTP route,
   <http://www.stephanhartmann.org/wp-content/uploads/2016/02/HHL10_Niiniluoto.pdf>.
   HTTPS normal certificate validation failed with a name mismatch; no
   certificate bypass was used. The HTTP route returned504704bytes,
   46physical pages, printed311–356. SHA256
   `0328A41E4D8C1CD0D740DA422988CAC718610E237630A5B4D72896BAE920D876`.
   Metadata creation/modification2009-10-05 and copyright footer2009.
   This is the editor-hosted author reading copy, not verified final2011
   publisher-byte identity. Direct text reading: complete pp311–356,
   including sections1–12 and bibliography. Pages316,320,337 visually
   inspected: parameter endpoints, empty-constituent weights and utility
   definitions are present in the actual pages, not OCR artifacts.

2. `source/references/p15-hintikka/hintikka-1953-distributive-normal-forms.pdf`
   was acquired from the Finnish National Library's displayed direct PDF
   link at <https://digi.kansalliskirjasto.fi/teos/binding/1954942?page=1>.
   *Distributive Normal Forms in the Calculus of Predicates*, Acta
   Philosophica FennicaVI, Helsinki1953. Title/printing leaves confirm
   the1953original. 78physical pages; numbered exposition7–71.
   SHA256 `7F706C43955D8DBC77D1D400E868A162B87A4A2D026D3E0FE93D074094B1A977`.
   Direct reading: title/printing/preface/contents, introduction7–9,
   syntax/formation setup10–12, complete section3 pp28–39 (subsections16–21).
   Other exposition is held but unread. The Philosophical Society's
   official archive page states that the digitized series is supplied
   through permissions under CC-BY-NC. This original provides the actual
   normal-form machinery; it is not an original probability paper.

## Original probability-source dependency

The1965 Jerusalem paper pp274–288,1965 Combined System pp21–30,
1966 Two-Dimensional Continuum pp113–132, and1976 axiomatization/1980
postscript are separately identified originals, not acquired/read here.
The1966 publisher DOI is10.1016/S0049-237X(08)71666-5; its exposed summary
is not the chapter body. Archive catalogue searches found1966/1967 copies
in encrypted in-library/print-disabled holdings; those were not accessed.
The official Acta archive's openly readable series search did not expose
the1965volume18 paper; absence in that result is not a proof of global
unavailability. The1953 original and Niiniluoto's later account must not
be promoted to reading or closing these probability originals.

## Textual qualifications that affect reconstruction

- Held history p316 eq(2) is `(ni+lambda/K)/(n+lambda)`, but prose calls
  lambda=infinity the straight rule and lambda=4 the equal-state rule.
  Direct limits give lambda=0 and lambda=infinity respectively. Preserve
  the discrepancy, do not copy those prose statements as correct math.
- P319 counts2^K constituents, calls widthzero contradictory on a
  nonempty domain, then p320 eq(18) assigns all1/2^K. A normalized
  nonempty-domain measure cannot give the contradiction positive mass.
  The authored nonempty-domain reconstruction conditions away the empty
  constituent, explicitly giving1/(2^K-1), not pretending the source
  printed that normalization.
- The generalized combined formulas(15')–(20) are handled as their own
  declared family. They are not obtained by silently substituting a
  width-dependent lambda into every occurrence in eq(17).
- P337 utility(54) gives truth payoff1-P(g), false payoff-qP(g).
  Its expectation is not eq(55) P(g/e)-qP(g), except whenq=1.
  The body retains the exact payoff distinction and supplies arithmetic.
- P333 eq(42) uses evidence-relative implication with eq(40)'s minimum
  over all hypothesis disjuncts. The body/annex gives the valid global
  entailment inequality and the explicit local-entailment failure:
  e=C1, h1=C1-or-C2, h2=C1 yields corroborations0 and1 despite the
  evidence-relative implication. Conditioning away refuted disjuncts
  would change the definition and is not silently attributed to it.

## Authoring scope and continuation

The packet reconstructs monadic constituents and the actually read1953
normal-form construction, finite/coherent and countably infinite
constituent-conditioned probability construction, constant-lambda and
combined likelihoods, posterior calculations, support-generalization
convergence, parameter boundaries, comparisons and explicit failure
cases. History applications and axiomatization remain distinctly cited
where their full derivations are not supplied. No whole1950Carnap,
wholeHintikka program, or whole allocated history-source closure is claimed.

Remaining primary work: acquire/read the original1965/1966 probability
papers and1976/1980 axiomatization (including postscript); reconcile the
empty-domain convention and original alpha/width parameterization;
complete the K-dimensional necessity/representation proof, relational
and identity extensions, similarity/error constructions, theoretical
systematization, and all historical application proofs on their own
conditions. The final2011 historical publisher version remains a distinct
version-comparison dependency.

## Saved packet and integration seam

- Body: `handbook/parts/p15/hintikka-inductive-logic.tex`.
- Reciprocal annex: `handbook/annex/p15/hintikka-inductive-logic.tex`.
- Bibliography intake: `handbook/bib/intake-p15-hintikka.bib`, two new
  source-role-distinct keys.
- Seven-field symbol intake: `handbook/registry/symbols-intake-p15-hintikka.csv`,
  nineteen data rows plus header.
- Twelve `proved=annex:` theorem/proof pairs. The supporting constructions
  include all finite K in their declared classification setting, an
  explicit countable named-domain realization, and arbitrary observed
  cell-frequency trajectories with eventually fixed support. They are
  not merely one two-cell illustration and do not assert the unproved
  full relational probability extension.
- Suggested reader seam: after `reichenbach-probability-logic` and before
  `goodman-projectibility`, planned164.8. Matching annex input at the
  analogous seam. Root owns all drivers/canonical registries/maps; none
  were edited here.
- No reviewers, tests, build, compiler or manuscript render were run.
  PDF page PNGs are source-reading derivatives, not handbook previews.
  Only owned new packet/source files were modified.
- Exact original probability-source closure remains open. The held1953
  monograph section supplies a genuine primary language construction;
  probability formulas are explicitly reconstructed from the separately
  held historical author account. Neither source role is promoted to the
  unheld original probability paper or final2011 published chapter.


## 26 October continuation: explicit observation-error construction

The lead reread the complete saved body and all twelve reciprocal annex
arguments, and directly read the held historical author's pp.340–343.
The source explicitly requires report probabilities on report histories,
but the saved packet only named that need. The new declared fixed-channel
construction supplies those likelihoods by summing latent words, an exact
latent-count recursion, a countable joint realization preserving constituent
masses, posterior and predictive formulas, and positivity/nonidentification
results. The one-counterreport calculation gives 1/15 for the specified
ten-percent symmetric error channel; identical channel columns leave all
support priors unchanged. This is an explicitly attributed editorial
reconstruction with additional independence assumptions, not a recovered
proof from the unheld 1997 original or the full historical error program.

One reciprocal proof pair and seven typed symbol rows were added. Original
probability-source acquisition, the K-dimensional necessity theorem and
the remaining separately allocated source presentations stay open. The
prior report's twelve-pair count describes the earlier saved state; the
current packet has thirteen. Author calculations/build results are recorded
separately and confer no independent-review or source-admission status.
