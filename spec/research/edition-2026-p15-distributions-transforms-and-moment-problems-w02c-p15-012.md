# P15 160.5-160.8: essential-bound consequence and urn parameter conditions (packet w02ca-p15-012)

## Provenance

Sources opened in this session (held paths from the packet):

- Durrett, PTE5 author PDF, `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
  Printed p. 142 = PDF p. 150 (Theorem 3.3.25, Carleman remark); printed p. 143 = PDF p. 151
  (Theorem 3.3.26: moments of F_n converge to mu_k and limsup mu_{2k}^{1/2k}/2k < infinity give weak
  convergence to the unique law; Exercise 3.3.24: G(x)=P(|X|<x), Lambda=sup{x:G(x)<1}, nu_k=E|X|^k,
  show nu_k^{1/k} -> Lambda, "so the assumption of Theorem 3.3.26 holds if Lambda < infinity").
- Feller II, second edition, `source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf`.
  Printed p. 229 = PDF p. 244 (VII.4, Examples (a): Polya urn with b black and r red balls, c balls of the
  drawn colour added); printed p. 230 = PDF p. 245 (display (4.7) for c_n, exchangeability, identification
  as the beta distribution with parameters mu=b/c and nu=r/c).

## What was written

- Body: `handbook/parts/p15/distributions-transforms-and-moment-problems-w02c-p15-012.tex`
  (chapter `sec:p15-w02c-p15-012-bounds-and-urns`).
- Annex: `handbook/annex/p15/distributions-transforms-and-moment-problems-w02c-p15-012.tex`
  (section `sec:annex-p15-w02c-p15-012-bounds-and-urns`).
- Corollary `thm:p15-w02c-p15-012-bound-gives-growth`: Lambda < infinity gives |X| <= Lambda a.s.,
  m_{2k}^{1/(2k)} -> Lambda, m_{2k}^{1/(2k)}/(2k) <= Lambda/(2k), limsup = 0 < infinity, hence the
  hypothesis of thm:p15-criteria-moment-method (Durrett Theorem 3.3.26) and uniqueness via
  thm:p15-criteria-analytic-determinacy with r=0; moment convergence then gives weak convergence to the law
  of X. Worked example (uniform grids), limitation warning (Lambda = infinity decides nothing; lambda=2 vs
  lambda=1/2 from thm:p15-criteria-generalized-gamma).
- Urn: definition with b,r >= 0, b+r>0, c>0 (uniform construction); lemma on word probabilities and
  exchangeability; theorem with b>0, r>0, c>0 explicit (beta finiteness proof shows where r>0 is used);
  theorem for b>0=r and b=0<r (point masses, beta integral diverges); worked example b=2,r=1,c=1 and
  contrast r=0; limitation warning (c=0 and b=r=0 point to thm:p15-polya-parameter-boundaries).

## Existing treatment found but not listed in the packet

- `handbook/parts/p15/polya-urns-and-beta-prediction.tex`, `thm:p15-polya-parameter-boundaries`
  (lines about 202-218): treats r=0<g, g=0<r and c=0 for the path-level urn (green/red notation).
  Linked, not duplicated: the new theorem treats the one-zero-weight cases inside Feller's moment
  (Hausdorff) route, which that theorem does not.
- `thm:p15-polya-beta-limit` and `thm:p15-polya-worked-prediction` in the same file (linked).

## Patch requests

`work/waves/w02ca/patches/w02ca-p15-012.json`: (1) make r>0 explicit in thm:p15-feller-polya-moments;
(2) add a pointer there to the one-colour theorem; (3) correct the criteria-chapter sentence that claims
all of Exercise 3.3.24 and point to the new corollary. All three require the new files on the input route
first (insertion proposal: after the w02b-p15-012 inputs in handbook/parts/p15.tex and handbook/annex/p15.tex).

## Continuation

All four sections' listed duties have text written in the owned files. Checks run: find_fused_spaces
(clean), unit-compile ok (remaining overfull boxes are long annex-id headings in the unit build and two
bibliography URLs), check.py --tree filtered to these files (no finding). Nothing outstanding in the
owned files; the patch requests and driver inputs are for the lead.

Block 2 (w02ca r2): guard G1 named
`spec/research/edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md` as
changed outside this packet's set. This packet did not write that file and did not edit it now: its
mtime is 2026-10-10 06:41, before this packet's first output (10:02), and its diff (ignoring line
endings, 9 insertions, 2 deletions) is a P02 locator correction (Boger p. 160 -> p. 166) with a
"w02ca (block 1)" entry, i.e. the work of packet w02ca-p02-002, whose owned files are that chapter's
body and annex. Reverting it would destroy that packet's provenance record and would itself be an edit
outside this packet's files (A8); the lead should attribute it to w02ca-p02-002 (the note is not in
that packet's owned_files list either). Locators re-verified this session in the held PDFs: Durrett
PTE5 PDF p. 150 = printed 142 (Theorem 3.3.25), PDF p. 151 = printed 143 (Theorem 3.3.26,
Exercises 3.3.24-3.3.25); Feller II PDF p. 244 = printed 229 (VII.4 Examples (a)), PDF p. 245 =
printed 230 (display (4.7), beta with parameters b/c, r/c). One wording change in the body warning
(line 106: the normal-law gloss now reads "for instance, X centred normal"). Checks rerun: fused
spaces clean, unit-compile ok, check.py filtered to owned files clean. Nothing in progress.
