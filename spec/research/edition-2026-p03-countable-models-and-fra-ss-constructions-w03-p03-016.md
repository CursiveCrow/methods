# w03a-p03-016 research note (P3, sections 26.5, 26.6, 26.7)

Label tag: `p03-w03-p03-016`. Packet: `work/waves/w03a/packets/w03a-p03-016.json`.

## Sources read in this session

- Vaught 1961, held: `source/references/p03-vaught1961-original/vaught-1961-denumerable-models.pdf`
  and its extraction `vaught-1961-extracted.txt`. Read: p. 303 (n. 1: complete implies consistent),
  p. 304 (introduction: Section 6 answers Robinson's question; n. 5: letters i,...,r range over omega;
  Section 1 conventions), pp. 305-306 (standing assumption: T complete with infinite models, p. 306),
  pp. 318-321 (Section 6 entire, n. 23, references [14] Skolem 1920). Page 319 was also checked as a
  rendered image to confirm "n = 4, 5, ..." for T_n.
- Gonzalez, Rossegger, Turetsky, arXiv:2606.15205v2 (26 August 2026), held:
  `source/references/p03-vaught-never-two-status/gonzalez-rossegger-turetsky-2026-v2.pdf`.
  Read pp. 1-7: p. 1 (VC attributed to [Vau61]; open for sixty years), p. 2 (Vaught ordinal; countable
  vo equivalent to satisfying VC; counterexample has vo = omega_1), p. 4 (omega-VC of Gonzalez and
  Montalban: countable vo for every theory and vo <= alpha+omega for Pi^in_alpha theories; Martin's
  conjecture translation; Corollary 4.10), p. 5 (Definition 1.1 of Sigma/Pi^in classes; negation swaps),
  p. 6 (precise vo definition; "see Proposition 2.2"), p. 7 (Proposition 2.2 and its proof via Silver's theorem).

No online sources were used.

## What this block changed

Editable host `handbook/parts/p03/presentations/n-a-004-01.tex`:
- lines 4-22: Robinson's question (p. 304; p. 318 with n. 23), Theorem 6.1 over n in omega (n. 5), consistency of complete theories (n. 1).
- lines 130-158: Vaught's Cantor (p. 318) and Skolem [14] (p. 319) justifications; Vaught's T'_3 completeness sketch (pp. 319-320) in prose.
- lines 160-178: thm:p03-w03-p03-016-source-routes (both source routes, proved in owned annex).
- lines 180-194: thm:p03-w03-p03-016-theorem-6-1 (n in omega, n = 0 witness) and its relation to the p. 306 standing assumption.
- lines 203-211: the Robinson example paragraph, replacing the "positivity essential" claim.
- lines 216-250: exact quotation of the conjecture (p. 320), "unresolved", "a number of people", denumerable count, scope; the aleph_1-without-CH problem; GRT p. 1 attribution contrasted; separation from never-two; Baldwin-Lachlan consequence for complete theories via thm:p03-baldwin-lachlan (cited result already in the handbook).
- lines 307-341: vo definition now follows GRT p. 6 (Pi^in types); omega-VC as on GRT p. 4; equivalence of countable vo with VC (GRT pp. 2, 6); omega-VC strengthens VC.

Owned body `handbook/parts/p03/countable-models-and-fra-ss-constructions-w03-p03-016.tex` (chapter):
thm:p03-w03-p03-016-vo-cardinal (countable vo implies cardinal dichotomy; omega-VC bound implies countable vo;
CH makes the bare cardinal reading of the converse equivalent to "every sentence has countable vo"),
def:p03-w03-p03-016-independent-predicates (worked example, vo = 0), def:p03-w03-p03-016-vo-limits.

Owned annex `handbook/annex/p03/countable-models-and-fra-ss-constructions-w03-p03-016.tex`: proofs
annex:p03-w03-p03-016-source-routes, annex:p03-w03-p03-016-theorem-6-1, annex:p03-w03-p03-016-vo-cardinal
(including verification of the example).

Patch requests: `work/waves/w03a/patches/w03a-p03-016.json` (driver inputs for the owned body and annex;
attribution sentence for the read-only annex `handbook/annex/p03/n-a-004-01.tex`).

## Open items

- The direction "Vaught's conjecture (infinitary) implies a countable Vaught ordinal" is reported from
  GRT (pp. 2, 6; Prop. 2.2 p. 7 via Silver's theorem) and not proved in the handbook. Silver 1980 was not read.
- Skolem 1920 [14] was not read; the handbook cites Vaught's attribution only.
- Morley 1970 body still not held (prior block's acquisition receipt, 2026-10-11); N-a-004-MAP-03 remains blocked_source.

## Continuation

Block 1 finished the three listed gaps of ED26-REQ-N-a-004-01 (C01 items 1-5, MAP-02, MAP-04) in the files above.
unit-compile ok; check.py shows no findings on these files; find_fused_spaces clean.
Next: lead to apply patch requests (driver inputs, annex attribution). Nothing else pending for this unit in this block.
