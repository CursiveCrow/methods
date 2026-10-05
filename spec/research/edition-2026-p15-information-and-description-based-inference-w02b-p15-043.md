# Packet w02b-p15-043: provenance note

Part P15, chapter 166, section 166.6 ("Maximum-entropy inference under declared
constraints"). Label tag `p15-w02b-p15-043`. Heading level `\chapter`.
toc tag `%% toc: P15 166 166.6`.

## Owned files

- Body: `handbook/parts/p15/information-and-description-based-inference-w02b-p15-043.tex`
- Annex: `handbook/annex/p15/information-and-description-based-inference-w02b-p15-043.tex`
- Bib intake: `handbook/bib/intake-p15-information-and-description-based-inference-w02b-p15-043.bib`
  (one key, `Jaynes1957InformationTheory`)
- Symbol intake: `handbook/registry/symbols-intake-p15-information-and-description-based-inference-w02b-p15-043.csv`

## Source held and opened in this session

- E. T. Jaynes, "Information Theory and Statistical Mechanics", Phys. Rev. 106 (1957)
  620-630, author offprint scan,
  `source/references/acq-r1-ACQ-2026-10-0336/jaynes-1957-information-theory-statistical-mechanics.pdf`
  (sha256 2e0f7780..., listed in spec/coverage/edition-2026/held-sources.json).
  Image-only; every page rendered with PyMuPDF at 150 dpi and read in this session.
  Printed pages 620-630 all read. Locators used in the reader text:
  - p. 620: abstract (least-biased, maximally noncommittal estimate; subjective statistical
    mechanics); Sec. 1 begins.
  - p. 621: Sec. 1 aims; the reversal of reasoning made possible by Shannon; equal a priori
    probabilities, ergodicity and metric transitivity as the hypotheses to be dispensed with;
    stationary states only; density matrix and irreversible processes deferred.
  - p. 622: Sec. 2, eqs. (2-1), (2-2), "n-2 more conditions"; insufficient reason and its
    change-of-variables paradoxes (footnote 7); footnote 6 (only the discrete case
    considered); objective and subjective schools; the posed problem is of the subjective
    type; eq. (2-3) and the reference to Appendix A.
  - p. 623: the principle; eqs. (2-4)-(2-15); extension of insufficient reason; positive
    weight to every situation not excluded; the -sum p^2 alternative and why Shannon's
    measure is preferred (composition law); Sec. 3 begins (Boltzmann distribution).
  - p. 624: eqs. (3-1)-(3-8); restriction to equilibrium prediction from quantities
    observed constant in time; metric transitivity remark.
  - p. 625: enumeration of states as the only contact with physics; model (3-9) with
    density of states rho(x)=x^n/epsilon; problems (A) and (B); eqs. (3-10), (3-11).
  - p. 626: Figs. 1-2; eqs. (3-12)-(3-14); Sec. 4; definite predictions only from sharp
    distributions.
  - p. 627: macroscopic uniformity; failed sharp prediction as evidence about the
    enumeration of states; prediction versus interpretation; Sec. 5, eqs. (5-1)-(5-3).
  - p. 628: heat bath, thermometer, eqs. (5-4)-(5-10); footnote 18 (argument lacks rigor).
  - p. 629: pressure ensemble (5-11); nuclear polarization (5-12)-(5-18); Sec. 6 begins.
  - p. 630: Sec. 6 conclusion; Appendix A, conditions (1)-(3), eqs. (A-1)-(A-5); the
    uniqueness of the solution of (A-3) is referred to Shannon's paper, not proved there.

## Existing treatments found (A9)

- `handbook/parts/p15/measurement-uncertainty.tex` thm:p15-measurement-asymmetric-model
  (bounded interval, single mean). Linked; the copper-coefficient multiplier is computed in
  the worked example here (lambda = 7.7177..., sd 0.10826).
- `handbook/parts/p15/rationality-4-1.tex` thm:p15-rat41-indifference and the factory
  example. Linked.
- Not listed in the packet: `thm:p15-rmdl-gibbs` (countable Gibbs inequality, Rissanen
  chapter); `thm:p15-pushforward-laws`. Linked, not duplicated.
- Concurrent overlap: packet w02b-p15-044 (section 166.7) records in its note that it is
  writing general maximum-entropy mathematics (entropy identity, weak duality, multipliers,
  finite existence, failure cases, reference-measure change). Its files were not on disk
  when this packet was written, so no labels could be linked. Recorded in the return file
  for the lead.

## Numerical values (mpmath, 20 digits)

- Copper coefficient (a=0.12, b=0.40): lambda = 7.7177049528, variance 0.0117197844
  (formula ab-(b-a)/lambda agrees), sd 0.1082580, Z = 0.3212187, P(T<=0) = 0.6150312.
  Uniform: sd 0.1501111.
- Example: sqrt(6 pi)/2 = 2.1708038; ln 3 + 1 = 2.0986123; 1-e^{-1/2} = 0.3934693;
  1-2/e = 0.2642411; 1-e^{-1/6} = 0.1535183.

## Continuation

- C01: body lines 33-134 (problem, conventions, partition-function definitions).
- C02: body 136-295, annex 17-412 (Gibbs identity and dual bound, optimality,
  no-constraint corollary, uniqueness, partition lemma, interior lemma, existence
  bijection, finite case with support characterization, four failure cases).
- C03: body 297-397 (multipliers/normalization discussion, method, transport theorem).
- C04: body 399-533 (premises J1-J5 with locators, Appendix A theorem, statistical-
  mechanics boundaries, warning); annex 462-504 (Appendix A proof including the
  A(n)=K ln n uniqueness step Jaynes refers to Shannon for).
- C05: body 535-650 (power-family theorem = Jaynes problems A/B; reference-measure
  change n=0 vs n=1; constraint change E[x]=2 -> E[x^2]=6; copper coefficient computed);
  annex 505-555.
- Checks: unit-compile ok; find_fused_spaces clean; check.py only own bib-key.
- Patch requests: work/waves/w02b/patches/w02b-p15-043.json (links from
  measurement-uncertainty.tex and rationality-4-1.tex).
- Sibling chapters 040, 041, 042, 044 appeared on disk during the session; linked
  from Relationships. Possible content overlap of transport theorem parts 1-2 with
  042's reference-change results is recorded in the return file.
- Open: none of the five components has a known missing item. Readonly units
  (RAT2021 4-1, JCGM) not written here.
