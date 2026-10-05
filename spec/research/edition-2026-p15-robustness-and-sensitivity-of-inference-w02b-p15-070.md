# w02b-p15-070: robust conclusions, causal effects and robust decisions (P15 172.11, 172.12)

4 October 2026. Packet work/waves/w02b/packets/w02b-p15-070.json, label tag
p15-w02b-p15-070, heading level \chapter, toc tag `%% toc: P15 172 172.11,172.12`.

## Files

- Body: handbook/parts/p15/robustness-and-sensitivity-of-inference-w02b-p15-070.tex
- Annex: handbook/annex/p15/robustness-and-sensitivity-of-inference-w02b-p15-070.tex
- Symbol intake: handbook/registry/symbols-intake-p15-robustness-and-sensitivity-of-inference-w02b-p15-070.csv
- No bibliography intake: every cited key (SaltelliAnnoni2010Sensitivity,
  Huber1964RobustLocation, Pearl2009CausalOverview) is already in handbook/bib/handbook.bib.

## Existing treatments read before writing (A9)

Listed in the packet and read in full: parts/p15/approximate-quantitative-inference.tex,
parts/p15/global-sensitivity-and-robustness.tex, parts/p15/huber-robust-location.tex,
parts/p16/finite-causal-models.tex (plus the relevant annex items).
Not listed in the packet but found and linked rather than duplicated:
parts/p17/ambiguity-and-robust-choice.tex, def:p17-robust-dominance and
thm:p17-robust-dominance (comparison under every prior versus maxmin, finite expected
utility). The new decision theorem cites it and adds only the general-loss regret
characterization, the loss-normalization dependence of minimax, the threshold link and
the Huber minimax illustration.

## Sources opened in this session and locators used (A3, A4)

- Huber 1964, source/references/huber-robust-location-1964/huber-1964.pdf (scanned;
  pages rendered to images and read): p. 73, Sec. 1 (indeterminacy model, parameter not
  uniquely determined, three remedies); p. 82, Sec. 6 corollary and start of Sec. 7;
  p. 83, Sec. 7 (approximation (2), approximate upper bounds 0.17 / 0.021 / 0.0027 for
  (eps, k) = (0.1, 1.14), (0.01, 1.95), (0.001, 2.64); median bias; two shifted
  contaminated densities f(t-c), f(t+c) and the 2c argument).
  Cited: Sec. 1 p. 73; Sec. 7 pp. 82--83; Sec. 7 p. 83.
- Pearl 2009, source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf
  (text layer): Secs. 2.1--2.2 pp. 99--100 (associational/causal demarcation);
  Sec. 2.4 p. 101 (sensitivity to causal assumptions does not shrink with sample size);
  Definition 2 p. 109 (already used by the P16 chapter); Sec. 3.5.3 p. 124 (bounds when
  identification fails, not improvable by sample size). Page assignment checked from the
  running heads in the extracted text.
- Saltelli and Annoni 2010, source/references/p15-global-sensitivity/saltelli-annoni-2010.pdf:
  Sec. 2, p. 1509 (global approach: desired inference holds over plausible ranges;
  Leamer's credible-neighborhood / useful-interval criterion, paraphrased, not quoted).
- Mahajan 2014 was not reopened; no Mahajan-specific statement is made in the new files.

## Numerical values (all computed with mpmath at 30 digits from the closed form of m_k
in thm:p15-huber-asymmetric-bias)

- c_*(0.1, 1.14) in (0.1703, 0.1704): m(0.1702) = -0.1265312, m(0.1703) = -0.1266050,
  m(0.1704) = -0.1266789, target -0.1266667; linearized 0.1698596; A(1.14) = 0.7457137.
- c_*(0.01, 1.95) in (0.020755, 0.020765); c_*(0.001, 2.64) in (0.0026645, 0.0026650).
- k = 1: c_*(0.05) in (0.0771, 0.0772); c_*(0.1) in (0.1632, 0.1633);
  eps*(0.10) = 0.063836, eps*(0.125) = 0.078493, eps*(0.15) = 0.092668.
- B(1)/A(1)^2 = 0.5160586/0.4660649 = 1.10727.

## Mathematical decisions

- Huber's p. 83 display uses approximation (2) with the derivative replaced by its value at
  zero. For the clipped normal score the new theorem proves this always gives a strict
  lower bound for the exact c_*; at (0.1, 1.14) the exact maximum exceeds the displayed
  0.17. This is stated as a property of the approximation, which Huber himself labels
  approximate; no error is attributed to the source.
- The confounded shift model is a stipulated model with a real-valued disturbance, so it is
  outside the finite class of def:p16-finite-scm; its intervention is defined directly by
  the same equation-replacement rule and every claim is proved from the explicit equations.
- "Robust decision" is defined as optimal at every member (persistence); minimax and
  minimax-regret are separate. Robust optimality is characterized as zero maximal regret.

## Continuation

Status at return (4 October 2026):
- 172.11 US-0: body sec:p15-w02b-p15-070-signs (lines 30-365 of the body file), with
  def robust-conclusion, thm reduction, thm margins, thm linear-ranking, def
  asymmetric-family, thm contamination-margin, thm linearized-margin, example
  two-measurements, warning false-robustness, method certify; annex proofs for all five
  theorems.
- 172.12 US-0: body sec:p15-w02b-p15-070-three-claims (lines 366-653; relationships 654-687), with def
  three-claims, thm decisions, thm minimax-not-robust, thm consistency-identification,
  def confounded-shift, thm separation, example separation-numbers, method which-claim;
  annex proofs for all four theorems. Relationships and limitations section closes the
  chapter.
- unit-compile ok; tools/check.py shows no finding in these files; find_fused_spaces clean.
- Open items: integration into handbook/parts/p15.tex and handbook/annex/p15.tex (lead);
  symbol intake merge (lead).
