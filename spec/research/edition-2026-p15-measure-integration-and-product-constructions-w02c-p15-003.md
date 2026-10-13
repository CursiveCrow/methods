# w02ca-p15-003: Stieltjes endpoint limits, ray-determined laws, counting-measure summation

Packet `work/waves/w02ca/packets/w02ca-p15-003.json`; label tag `p15-w02c-p15-003`;
P15 chapter 158, sections 158.1, 158.2, 158.5, 158.8.

## Duties addressed

- ED26-P15-CH-measure-extension-C008 (158.1, 158.2, 158.8): the upper-end limit
  elided at `handbook/annex/p15/measure-extension.tex` line 296 ("reversed
  argument"), the b = infinity truncation identity of lines 383-393, and
  finiteness on all bounded intervals asserted at body lines 211-212.
  Written in the owned supplement:
  - body `handbook/parts/p15/measure-integration-and-product-constructions-w02c-p15-003.tex`
    def:p15-w02c-p15-003-extended-limits (53-81), thm:p15-w02c-p15-003-endpoint-limits
    (83-104), thm:p15-w02c-p15-003-bounded-finite (112-131), example
    def:p15-w02c-p15-003-exponential (138-156), warning def:p15-w02c-p15-003-monotone-premise (158-168);
  - annex `handbook/annex/p15/measure-integration-and-product-constructions-w02c-p15-003.tex`
    annex:p15-w02c-p15-003-endpoint-limits (12-136): both ends, finite and infinite
    cases, integer sequences, truncation shape, and the supremum identity in three
    cases (both finite; F(b) = infinity; F(a) = -infinity) with no infinite subtraction;
    annex:p15-w02c-p15-003-bounded-finite (147-214): bound via (-n,n], Borel-ness of
    each bounded interval, and the five interval measures through F(c-).
- ED26-P15-CH-measure-extension-C012 (158.1, 158.8): body thm:p15-w02c-p15-003-ray-laws
  (180-205), example def:p15-w02c-p15-003-two-point (216-232), warning
  def:p15-w02c-p15-003-ray-limits (234-254); annex annex:p15-w02c-p15-003-ray-laws
  (216-313): identity variable on (R, B(R), nu) is a real random variable with law nu;
  closed-ray pi-system uniqueness (thm:p15-borel-generators + thm:p15-measure-uniqueness)
  and the alternative route through thm:p15-cdf-laws applied to identity variables;
  F(-inf) = 0 and F(inf) = 1 from the limit lemma; law(Q_F) = mu_F using only the
  random-variable and ray-equivalence conclusions of thm:p15-cdf-existence (their proof
  in annex:p15.cdf-existence lines 481-512 precedes and does not use the law step);
  uniqueness for measures with given ray values and for laws of real random variables.
- ED26-P15-CH-product-measures-C013 (158.5): rewritten in place in the editable host
  `handbook/annex/p15/product-measures.tex`, annex:p15.absolute-iterated-series, series
  half now at lines 506-626: nonnegative counting identity (term-by-term integration,
  simple integrals, monotone convergence for the infinite value); signed counting
  identity for absolutely summable real sequences; F(n,y) = f_n(y) product measurable;
  identification of the hypothesis with Fubini's first iterated absolute premise,
  of H with H_2 (so N = N_2), of S with I_2F, and of n -> int f_n with I_1F (N_1 empty),
  giving the exchange from Fubini's equality.

## Read-only host patch requests

`work/waves/w02ca/patches/w02ca-p15-003.json` (five replace operations on
`handbook/annex/p15/measure-extension.tex`): the "reversed argument" sentence (line 296),
the "endpoint-limit argument" sentence (line 385), the sigma-finite closing sentence
(lines 410-411, adding the bounded-finite pointer), the thm:p15-cdf-laws step of
annex:p15.cdf-existence (lines 513-516), and the opening sentence of
annex:p15.cdf-existence (lines 472-473). Each anchor quote was checked to occur exactly once.

## Source locators (read this session in the held file)

Held file: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
(Durrett, Probability: Theory and Examples, author version 11 January 2019;
bib key DurrettPTEAuthor2019).
- Theorem 1.1.4 statement: printed p. 3 (PDF page 11).
- Proof of Theorem 1.1.4, opening remark that the end limits exist and the interval
  assignment makes sense: printed p. 5 (PDF page 13); proof continues on p. 6.
- Theorem 1.2.2: printed p. 11 (PDF page 19).
- Equal-in-distribution remark relying on Theorem 1.1.4: printed pp. 11-12 (PDF 19-20).
The source asserts the end limits without proof; the proofs supplied here are general
real analysis written for this handbook, not a source transcription.

## Existing treatments found

Listed in the packet: measure-extension body/annex, product-measures body/annex,
measurable-probability, integration-expectation (not listed but read: definitions of
simple, nonnegative and signed integrals, thm:p15-monotone-integral,
thm:p15-nonnegative-integral-laws, thm:p15-signed-integral-laws in
`handbook/parts/p15/integration-expectation.tex`). No prior handbook proof of the
counting-measure summation identity was found (grep for "counting measure" in
handbook/parts and handbook/annex).

## Trace generation for the density assembly

- ED26-P15-CH-density-and-product-exercises-C006 (158.8): the sigma-finite assembly of
  annex:p15.countably-generated-radon-nikodym (`handbook/annex/p15/density-and-product-exercises.tex`
  line 182) asserted that the traces E_j cap D_i generate the restricted sigma-field.
  Written in the owned supplement, new third section (chapter retitled "Endpoint Limits,
  Stieltjes Laws and Trace Sigma-Fields"):
  - body lines 270-449: sec:p15-w02c-p15-003-trace-sigma-fields, def:p15-w02c-p15-003-trace-sigma-field,
    thm:p15-w02c-p15-003-trace-generation (parts 1-4), corollary thm:p15-w02c-p15-003-block-data,
    example def:p15-w02c-p15-003-trace-example, warning def:p15-w02c-p15-003-trace-limits;
  - annex lines 321-465: annex:p15-w02c-p15-003-trace-generation (trace is a sigma-field; D in F
    gives F_D subset F and restricted measures; both inclusions of F_D = sigma_D(E_j cap D), the
    first by minimality, the second by the good-set sigma-field H = {A : A cap D in G}; gluing
    measurability) and annex:p15-w02c-p15-003-block-data (finite mu|_D, probability lambda,
    mu|_D << lambda).
  Two further replace requests for the read-only host density-and-product-exercises.tex were
  added to `work/waves/w02ca/patches/w02ca-p15-003.json` (the line-182 sentence and the
  "piecewise function is measurable" sentence); anchors checked unique.
  Source locator read this session: Durrett Exercise 4.3.7, printed p. 234 (PDF page 242); it
  poses the countably generated sigma-finite case and does not discuss blocks.

## Continuation

All assigned duties, including the C006 trace-generation gap, have text in the owned files.
unit-compile reports ok with the three earlier small overfull boxes; find_fused_spaces and
check.py --tree show no finding in the owned files. C006 stays partial until the lead applies
the two density-and-product-exercises.tex patch requests; the five measure-extension.tex
requests also await the lead. Body line numbers quoted in the first list above shifted by +5 after the chapter-introduction sentence was added; the return file carries the current ranges.

Resumed run (after the usage-limit halt): guard G1 named
`spec/research/edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md`.
That file is a P02 note outside this packet; this packet never wrote it (no command in
either run touched it). At resume, `git diff --quiet` against HEAD reports it identical to
the committed version (exit 0) and `git status` does not list it as modified; only its
mtime (15:55, after this packet's last write at 15:13) changed, consistent with another
agent's activity. No edit was made to it here, since editing it would itself violate A8.
Re-ran checks: unit-compile ok (3 small overfull boxes), find_fused_spaces no hits on the
owned files and product-measures.tex, check.py --tree no hard finding in the owned files
(the product-measures.tex notation-scope warnings at lines 141 ff. lie outside the edited
range 506-626 and predate this packet). Component states are unchanged from the return file.

Run r4 (C006 sigma-finite assembly): the assessor found that the per-block identity
int_{A cap D_i} f dnu = mu(A cap D_i) and the passage from lambda_i-null to nu-null sets had no
written support. Added to the owned body the lemma thm:p15-w02c-p15-003-block-integrals (transfer of
nonnegative integrals from (D, F_D, nu|_D/nu(D)) to Omega via zero extension, proved from the
simple-function supremum definition without approximation sequences, plus scaling and null sets) and
the theorem thm:p15-w02c-p15-003-assembly (measurability, per-block identity, summation by part (4) of
thm:p15-nonnegative-integral-laws, finite a.e.), with annex proofs, an extension of the four-point
example, and an infinite-mass paragraph in the warning. Two further patch requests for
density-and-product-exercises.tex (summing sentence, finite-a.e. sentence) were added to
work/waves/w02ca/patches/w02ca-p15-003.json. Symbol rows added for bar g, I^+/c_i/N_i and the annex-local
L_D/L_Omega/t_D/N_infty. Checks: unit-compile ok (3 small overfull boxes as before), find_fused_spaces
no hits, check.py --tree no finding in owned files. C006 remains partial only for the host edit.
