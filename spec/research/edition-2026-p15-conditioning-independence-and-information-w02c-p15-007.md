# Packet w02ca-p15-007: provenance note

Part P15, chapter 159 (sections 159.3, 159.4, 159.5, 159.6); unit
ED26-P15-CH-conditional-expectation; label tag `p15-w02c-p15-007`.

## Owned files

- handbook/parts/p15/conditioning-independence-and-information-w02c-p15-007.tex
- handbook/annex/p15/conditioning-independence-and-information-w02c-p15-007.tex
- handbook/registry/symbols-intake-p15-conditioning-independence-and-information-w02c-p15-007.csv
- spec/research/edition-2026-p15-conditioning-independence-and-information-w02c-p15-007.md (this note)
- spec/research/edition-2026-p15-conditioning-independence-and-information-w02c-p15-007-return.json
- Patch requests: work/waves/w02ca/patches/w02ca-p15-007.json

No bibliography intake file: the only key cited is DurrettPTEAuthor2019,
already in handbook/bib/handbook.bib.

## Source held and opened

source/references/durrett-probability-2019-01-11/PTE5_011119.pdf (Durrett,
Probability: Theory and Examples, author version 5, 11 January 2019), opened
in this session with pdftotext.

- Printed p. 205 (PDF 213): setting (Omega, F_o, P), sigma-field F in F_o,
  definition of E(X|F) by (i) F-measurability and (ii) the event identity.
  Chapter notation: Durrett's F_o is the handbook's F_0, Durrett's F is the
  handbook's G.
- Printed p. 207 (PDF 215): existence. Durrett takes mu = P (on the smaller
  sigma-field), nu(A) = int_A X dP for A in F, applies Radon-Nikodym, and
  writes int_A X dP = nu(A) = int_A (dnu/dmu) dP. The density's integral is
  written with respect to P without comment; that is the identification
  supplied by thm:p15-w02c-p15-007-restricted-integral. The general case is
  X = X+ - X- with Y1 = E(X+|F), Y2 = E(X-|F).

## Gap addressed (ED26-P15-CH-conditional-expectation-C002)

Assessment: annex:p15.conditional-existence (handbook/annex/p15/
conditional-expectation.tex lines 23-39) applies Radon-Nikodym on
(Omega, G, P|_G) and then uses P-integrals of the densities without proving
int_A W d(P|_G) = int_A W dP for G-measurable W.

Supplied in owned files:

- def:p15-w02c-p15-007-restricted-probability (restriction, measurability
  transfer, meaning of the integrals).
- thm:p15-w02c-p15-007-restricted-integral with annex proof
  annex:p15-w02c-p15-007-restricted: nonnegative identity by
  G-simple dyadic approximation (thm:p15-measurable-limits applied on the
  probability space (Omega, G, P|_G)) and monotone convergence on both
  spaces; absolute-value and signed cases; equivalence of the two a.e.
  notions for G-measurable comparisons; second derivation from
  thm:p15-expectation-law-integral with the identity map.
- thm:p15-w02c-p15-007-density-version with annex proof: the density
  construction of thm:p15-conditional-existence carried out in full against
  P-integrals (finite measures nu_pm on G, absolute continuity, P-integrability
  of Z_pm, G-measurable null infinity set, the event identity).
- def:p15-w02c-p15-007-two-cell (worked computation).
- thm:p15-w02c-p15-007-restriction-sigma-finite with annex proof (failure
  case: restriction of Lebesgue measure to the trivial sigma-algebra; no
  density exists).

The host annex is read-only for this packet. Patch request
work/waves/w02ca/patches/w02ca-p15-007.json asks the lead to cite the new
lemma and theorem at the point of the swap in annex:p15.conditional-existence.

Related existing use not listed in the packet: annex:p15.density-martingale
(handbook/annex/p15/density-martingales-and-product-measures.tex lines 6-9)
writes "restriction of the integration space gives" for the same
identification with F_n in place of G, for a measure nu. The lemma here is
stated for a probability measure; that host's nu is a finite measure of
total mass c, so the lemma does not apply verbatim there. No patch is
requested for it.

## Continuation

- 2026-10-10: body, annex, symbol intake, patch request and return written.
  Remaining for the lead: insert the two driver lines (placement in the
  return) and apply the patch request. Self-checks recorded in the return.
- 2026-10-10 (continuation run): reopened Durrett PTE5_011119.pdf PDF pp. 213-215
  and confirmed the locators p. 205, pp. 205-206 and p. 207 written in the body.
  Annex wording in the proof of item 2 of
  thm:p15-w02c-p15-007-restricted-integral made explicit for W^- (no
  "similarly"). unit-compile ok; check.py shows no finding in owned files;
  find_fused_spaces no hits. Return updated with line ranges for the
  pre-existing components and a note on guard G1: the flagged P2 research note
  was last written at 06:41, before any file of this packet, and is not owned
  by this packet; it was not touched here.
