# w02b-p15-074 — P15 chapter 173, section 173.12: finite-precision computation and simulation evidence

Packet: work/waves/w02b/packets/w02b-p15-074.json. Label tag: p15-w02b-p15-074.

## Provenance

- Held sources opened in this session:
  - source/references/p12-numerical-error/oracle-819-3693-goldberg.html (held-sources.json entry;
    bib key GoldbergOracle8193693). Read Sections D.3.2 "Relative Error and Ulps" (decimal format
    with base 10 and precision 3 used throughout that section; half-ulp nearest rounding; relative
    error, wobble, machine epsilon) and D.3.4 "Cancellation" (catastrophic versus benign
    cancellation; an exact subtraction exposes earlier rounding errors).
  - source/references/p12-simulation-evidence/NASA-STD-7009B-2024-03-05.pdf (held-sources.json entry;
    bib key NASA7009B2024). Read via pdftotext: Section 4.2.3 (M&S 15, M&S 16; implementation versus
    solution verification; solution verification each time the M&S is used), Section 4.2.4
    recommendation b (record numerical error estimates, listing numerical approximations,
    insufficient discretization, insufficient iterative convergence and finite-precision
    arithmetic), Appendix E.3.3 (solution verification: numerical errors from hardware, software,
    tolerances, discretization), Appendix E.4.4 (uncertainty characterization: input sources,
    numerical errors in implementation, propagation to outputs as three separate aspects).
- Handbook derivations, not attributed to either source: the error ledger and its telescoping
  certificate, the regime-enclosure corollary, the four-threshold worked example, the Euler
  threshold example (built on thm:p12-simulation-decay-euler and
  thm:p12-simulation-arithmetic-propagation), the Monte Carlo indicator-band theorem and the
  decimal tie example. All numbers were checked with exact rational and decimal (precision 3,
  round-half-even) arithmetic in Python during this session.
- No new bibliography keys (both keys are already in handbook.bib).

## Gap addressed (section 173.12)

Assessment gap: chapter 173 had no section connecting approximate quantitative conclusions (signs,
orderings, thresholds, regime checks) to finite-precision arithmetic error or simulation results,
and no cross-reference to sec:p12-numerical-error-and-inference or
sec:p12-simulation-results-as-evidence. The new chapter file supplies that section.

Existing treatment found and linked, not rewritten: thm:p12-numerical-certification (sign/order
certificate), thm:p12-numerical-data-budget (input versus arithmetic), def/thm:p12-simulation-error-chain
(four-term chain without an approximant), thm:p15-approximation-certificates, thm:p15-approximation-rational,
def:p15-approximation-procedure, def:p12-numerical-inference-procedure.

## Written (section 173.12)

Body handbook/parts/p15/measurement-dimensional-constraints-and-approximate-inferenc-w02b-p15-074.tex
(sec:p15-w02b-p15-074): purpose, inputs/conclusions, dependencies (lines 1-50);
def:p15-w02b-p15-074-ledger (55-92); thm:p15-w02b-p15-074-ledger (105-130);
thm:p15-w02b-p15-074-regime (149-162); thm:p15-w02b-p15-074-four-thresholds (182-212) and
def:p15-w02b-p15-074-four-reading (214-243); thm:p15-w02b-p15-074-euler (263-280);
thm:p15-w02b-p15-074-sampled (306-328); thm:p15-w02b-p15-074-tie (341-353);
def:p15-w02b-p15-074-limits (364-392); def:p15-w02b-p15-074-procedure (401-427);
relationships and sources (429-457). Annex proofs for all six results in
handbook/annex/p15/measurement-dimensional-constraints-and-approximate-inferenc-w02b-p15-074.tex.
Explicit cross-references: part:p12, sec:p12-numerical-error-and-inference,
sec:p12-simulation-results-as-evidence and the P12 results listed above.

Patch request: work/waves/w02b/patches/w02b-p15-074.json (route from the end of
def:p15-approximation-procedure in the host to the new chapter).

## Continuation

- State: body, annex, symbol intake and empty bib intake written; unit-compile ok (4 small overfull
  boxes: theorem heading 0.3 pt, two annex number paragraphs about 2 pt, and the Goldberg
  bibliography entry); check.py --tree handbook reports no finding in these files.
- Units ED26-SCI-JCGM2008-001, ED26-SCI-Mahajan2014-001 and ED26-SCI-Mahajan2014-002 are readonly
  for this packet (owners w02b-p15-042, w02b-p15-073, w02b-p15-070); their components were not
  written here.
- Lead actions: input the body after parts/p15/approximate-quantitative-inference in
  handbook/parts/p15.tex (and after the w02b-p15-073 input if that has been placed there), the
  annex likewise in handbook/annex/p15.tex; apply the patch; merge the symbol intake.
- Symbol decision: E_model, E_input, E_disc, E_arith reuse the P12 row (def:p12-simulation-error-chain)
  with the same role; B here is an input enclosure (same role as the input box B of
  sec:p15-w02b-p15-073); rho is a regime bound locally; omega(E) is a band probability.
