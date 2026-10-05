# w02b-p15-077 — P15 174.9, 174.10: randomized assignment as a finite SCM

Packet: `work/waves/w02b/packets/w02b-p15-077.json` (label_tag `p15-w02b-p15-077`).

## Duty addressed in this block

Assessment gap for 174.10: the host `handbook/parts/p15/factorial-inference-and-estimability.tex`
(lines 731-732) only asserted that the assignment/mechanism distinction "agrees with"
`def:p16-causal-intervention` and `def:p16-causal-identification`. Owed: a proved correspondence
between `def:p15-factorial-assignment` and the P16 finite SCM semantics (assignment as exogenous
parent with known law; under consistency, stable versions and no interference, tau equals the P16
average intervention effect and is identified from the observed assigned-arm law within a stated
model class), the failure boundary (noncompliance, interference, differential missingness), and
the application to `def:p19-proposed-factorial-design` naming the premises an empirical study must
supply.

## Files

- Body: `handbook/parts/p15/experimental-design-and-estimable-contrasts-w02b-p15-077.tex` (new chapter,
  `sec:p15-w02b-p15-077-assignment-scm`).
- Annex: `handbook/annex/p15/experimental-design-and-estimable-contrasts-w02b-p15-077.tex`.
- Symbol intake: `handbook/registry/symbols-intake-p15-experimental-design-and-estimable-contrasts-w02b-p15-077.csv`.
- Patch request (read-only host): `work/waves/w02b/patches/w02b-p15-077.json` (replace the unproved
  "agrees with" sentence of the host by a pointer to the new chapter).
- No bib intake: the only external key is `Pearl2009CausalOverview`, already in `handbook.bib`.

## Sources and locators (all seen this session in the held PDF)

Held file: `source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`
(text extracted with pdftotext; journal page headers read from the extraction).

- Definition 2 (identifiability), sec. 3.2.1, p. 109.
- sec. 3.2.2, eqs. (11)-(13), p. 109: E(Y|do(x0)) = E(Y|X=x0) from Y = f_Y(X,U_Y) and U_Y
  independent of X.
- sec. 3.5.2, pp. 122-124: noncompliance model (Fig. 5(a), p. 123); U_Z as the random assignment
  device; exclusion and independence assumptions (p. 123); treatment effect not identifiable without
  additional assumptions (p. 124).

All constructions (multi-unit model M_E, classes, functional Phi, interference iff-result,
noncompliance and missingness two-model pairs, worked example) are the handbook's own and are proved
in the annex. The NIST source of the readonly unit is not held and is not cited here.

## Existing treatments checked (A9)

- `handbook/parts/p15/factorial-inference-and-estimability.tex` sec:p15-factorial-causal (def/thm
  assignment, mechanism) — extended by \cref, not duplicated.
- `handbook/parts/p16/finite-causal-models.tex` (SCM, intervention, identification,
  positive-support identification) — used by \cref; the new identification does not follow from
  thm:p16-causal-positive-identification (positivity on all of S_N fails), stated in the body.
- Not listed in the packet's existing list: `handbook/parts/p16/finite-counterfactuals.tex`
  (`thm:p16-binary-po-bridge`, `thm:p16-po-ate-identification`): single binary treatment with a
  drawn unit; related in the Relationships paragraph, not duplicated.
- `handbook/parts/p19/evidence-methods.tex` `def:p19-proposed-factorial-design` — applied, not
  restated.

## Continuation

State after this block:

- Written: chapter body (lines 1-493) and annex (lines 1-384); unit-compile ok with 0 overfull;
  find_fused_spaces clean; check.py --tree shows no finding in these files.
- Open items for the lead: apply patch `work/waves/w02b/patches/w02b-p15-077.json` to the
  read-only host; insert `\input` lines per the packet's insertion proposal; merge the symbol
  intake. Proposed symbol decisions are in the return JSON.
- All 21 packet component ids belong to readonly units (owners w02b-p15-070, w02b-p15-075); they
  were not written here (A14).
- Not attempted: a stochastic-response version of the interference iff-result is already covered
  (class C_int allows random responses); no remaining mathematical gap known for the 174.10 duty.
  174.9 has no assessed gap in this packet; its content is the host section of w02b-p15-075.
