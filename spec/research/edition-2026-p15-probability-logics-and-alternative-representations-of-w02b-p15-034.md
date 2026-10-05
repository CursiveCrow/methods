# w02b-p15-034: partition updates and conglomerability (165.6)

Packet: `work/waves/w02b/packets/w02b-p15-034.json`, label tag
`p15-w02b-p15-034`, block 1. Unit `ED26-METHOD-imprecise-probability`,
gap C03 as stated by the independent assessment: the host
`handbook/parts/p15/imprecise-probability.tex` (lines 384-389) asserted with
a citation only that unconditional coherence is insufficient for joint
conditional claims on infinite partitions and that conglomerability matters.

## Source used (held, opened this session)

- `source/references/p15-imprecise-probability/miranda-survey-lirmm.pdf`
  (SHA-256 B8C24C2E...4C879E, 44 PDF pages), bib key
  `MirandaCoherentLowerPrevisionsCapture` (already in handbook.bib).
  Extracted with pdftotext -layout; printed page numbers read from the page
  footers. Locators used and verified:
  - §3.1, p. 17: contingent/updated readings, updating principle, (SC1)-(SC2), eq. (9).
  - p. 18: dependence on values in B only, eq. (10) for G(f|B) and G(f|\mathcal B), (C1)-(C3) for linear domains with constants.
  - §3.2, p. 19: conglomerative principle; joint coherence condition (11).
  - p. 20: Remark 1 (weak coherence); §3.2.1 natural extension, eq. (12).
  - pp. 20-21: the three infinite-partition defects (citing Walley §§6.6.6-6.6.10, 8.1.3); Example 3 on p. 21 (not reproduced; it is stated with "it can be checked").
  - §3.3, p. 22: (JC1), (JC2), the generalized Bayes rule.
  - p. 23: B-conglomerability definition and the existence equivalence; justification continues p. 24.
  - p. 24: full conglomerability; tie to countable additivity for linear previsions; vacuous model least at P(B)=0.
  - §5.1, p. 31: de Finetti rejects conglomerability.
  - §5.2, p. 32: Williams' condition (13); comparison with (11); W-coherence need not be conglomerable.
- No Walley 2014 StatsRef body is held (packet `held_paths: []` for the
  METHOD unit). Nothing here is presented as that article's content.

## What was written

- Body `handbook/parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-034.tex`
  (chapter, toc tag `%% toc: P15 165 165.6`).
- Annex `handbook/annex/p15/probability-logics-and-alternative-representations-of-w02b-p15-034.tex`
  with five annex items, all full proofs.
- Declared partition-update semantics: `def:p15-w02b-p15-034-semantics`
  (separately coherent on L(Omega) + JC1/JC2 with the test sets of (11)).
- Proved: cellwise lemma; necessity (JC => GBR on positive cells and
  B-conglomerability); existence iff conglomerable with the least update
  (GBR on positive cells, vacuous on null cells); explicit finitely additive
  counterexample on N+ x {0,1} (P = (mu + nu_1)/2, P(B_n) = 2^{-n-1},
  P(Y_1) = 3/4, cellwise 1/2, sure loss -1/2 from the infinite portfolio);
  W-coherence (13) holds for the same assessments.
- The counterexample's own construction is original to this text (a
  mixture of a countably additive and a purely finitely additive part); it is
  not attributed to the source. The finitely additive nu comes from the
  existing representation theorem applied to liminf (Choice as already
  assumed in sec:p15-imprecise-probability).
- Patch request `work/waves/w02b/patches/w02b-p15-034.json`: replace the
  citation-only paragraph in the read-only host with pointers to the new
  results (anchor verified to match once).

## Not settled / open

- MP-0: the selected Walley 2014 StatsRef article body remains unheld;
  source matching for the METHOD unit stays blocked_source.
- Not proved and not used: several partitions at once, restricted domains,
  natural extension on infinite partitions (source pp. 20-21 reports), and
  joint coherence of any more informative choice (e.g. cellwise regular
  extension) on infinitely many null cells. The reader text says so.
- RAT2021 4.7 unit is readonly here (owner w02b-p15-032).

## Checks run

- `python -B tools/waves.py unit-compile work/waves/w02b/packets/w02b-p15-034.json`: ok, no errors, no undefined refs/cites.
- `python -B tools/find_fused_spaces.py` on both tex files: no hits.
- `python -B tools/check.py --tree handbook`: no finding naming these files.

## Round 2 (block 1): C04 and C05 mathematical gaps

Assessment disputes addressed: C04 relied on Part 14 cross-references; C05
had no decision that needs an independence judgement; C03 chapter is off
route (driver insertion is the lead's, see return); C01-C05 source matching
(MP-0, Walley 2014 StatsRef) still unheld -- re-checked this session:
`held-sources.json` has no Walley entry, `source/` has no Walley file, the
only Walley bib key is `R47Walley1991` (the 1991 monograph, not held).

Sources opened this session (held): Miranda survey
`source/references/p15-imprecise-probability/miranda-survey-lirmm.pdf`
(printed page = PDF page, verified from footers and by rendering p. 30).
New locators used and verified:
- §4, p. 25 (start; positive-lower-probability simplification);
  §4.1 p. 26 (epistemic irrelevance); §4.2 p. 27 (epistemic independence);
  §4.3 p. 28 (independent envelope / independence in the selection);
  §4.4 p. 29 (strong independence); p. 30 (implication chain
  strong => selection => epistemic independence => irrelevance, equivalent
  in the precise case; rendered image confirms arrow direction).
- §5.5 p. 34: belief functions as completely monotone lower probabilities
  on a finite space; 2-monotone coherent; static embedding without updating
  or combination.
- p. 35: Dempster's rule eq. (15); Walley's criticism that the derived
  conditioning rule may fail coherence with the unconditional model unless
  extra conditional independence assumptions are made.
- §6 p. 37: possible indecision between two alternatives; criteria listed
  include maximality and Gamma-maximinity.

Written (body `...-w02b-p15-034.tex` lines 363-650 and the Relationships
paragraph; annex lines 283-706):
- thm belief-extension: Bel coherent, C_m in M(Bel), natural extension =
  focal-minimum sum = min over allocations = Choquet value (layer-cake proof,
  self-contained).
- cor belief-not-prevision: host example C/D of thm:p15-ip-event-separation;
  its event lower probability is Bel_m with m = 1/10 singletons, 1/5 pairs,
  1/10 whole space; E_m(f) = 1/2, D gives 7/10.
- thm strict-classes: necessity proper subclass of belief functions.
- def Dempster conditioning (via def:p15-r47-combination with m^B) and thm
  dempster: Pl formula, possibility ratio rule; two examples (positive and
  zero lower probability) where the Dempster value is not jointly coherent
  (via thm:p15-ip-conditional-bounds).
- def two-binary, thm independence-models, thm independence-decision:
  M_mg (marginals only) [0,1], M_ei (largest epistemically independent
  model, proved) [2/5,3/5], M_str (strong product) [12/25,13/25] for
  f = I{X=Y}; against the constant 9/20 the robust comparison is decided
  only under M_str; under M_ei and M_mg the pair is unranked (retained
  imprecision), maxmin chooses the constant. p^- is an extreme non-product
  point of M_ei.
- All examples are constructed for this chapter (stated in reader text);
  none is attributed to the source.
- Patch requests added (work/waves/w02b/patches/w02b-p15-034.json): pointer
  paragraphs in imprecise-probability.tex after the C04 paragraph and after
  thm:p15-ip-independence-boundary.

Checks: unit-compile ok (0 errors, 0 overfull, no undefined refs/cites);
find_fused_spaces no hits; check.py --tree: no finding naming these files.

## Round 3 (block 1): RAT2021 4.7 assessment disputes

The assessment listed five gaps against unit ED26-BM-RAT2021-4-7 (C02 decision
rules and sure-thing principle at p. 313; C02 disjoint-pair superadditivity
contrast at p. 313; C03 Ellsberg urn at pp. 311, 313; C05 GPL locators
depending on Dubois-Prade-Schockaert 2017; C05 finite dependent-source set).
That unit is a readonly unit of this packet (owner w02b-p15-032), and the
cited lines are in the read-only host rationality-4-7.tex. Not written here.
Checked the owner's file
handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-032.tex: it
already carries def:p15-w02b-p15-032-rules, thm:p15-w02b-p15-032-ellsberg
(maxmin vs difference comparison, pasting/sure-thing condition, three-colour
urn), thm:p15-w02b-p15-032-disjoint (pairwise superadditivity of lower
envelopes) and sec:p15-w02b-p15-032-sources (dependent-work table, with GPL
completeness as cited only, R47DuboisPradeSchockaert2017 not held). The GPL
locators at rationality-4-7.tex 216-246 are in a read-only host; any
correction there is the owner's or the lead's.
Done here (allowed by the readonly-unit rule): two cross-link sentences in
the Relationships paragraph of the body (lines 664-669 and 679-687) linking
thm:p15-w02b-p15-034-strict-classes to thm:p15-w02b-p15-032-disjoint and
thm:p15-w02b-p15-034-independence-decision to def:p15-w02b-p15-032-rules and
thm:p15-w02b-p15-032-ellsberg. Checks: unit-compile ok (0 errors, 0
overfull, no undefined refs/cites); find_fused_spaces no hits; check.py
--tree no finding naming these files.

## Continuation

Round 2 block 1 wrote the C04 and C05 mathematical content above. Nothing
further is writable for C01-C05 in the owned files until the Walley 2014
StatsRef article (DOI 10.1002/9781118445112.stat01581, complete article) is
held: MP-0 source matching stays blocked_source. Lead actions: place the
body input (packet proposal: after `parts/p15/rationality-5-3`; better
reading order: directly after `parts/p15/imprecise-probability`) and the
annex input likewise, apply the three patch requests, merge the symbol
intake.

Round 3: no owned-file work remains for ED26-BM-RAT2021-4-7 (owner
w02b-p15-032); the cross-links depend on the owner's file being placed on
the route by the lead.

## Round 4 (block 2)

- G14: body line 659 "kind admitted by" replaced by "kind allowed by"
  (no other workflow word in the body or annex reader text; "author
  manuscript" at lines 17-18 is the bibliographic version name of the held
  Miranda file).
- G1: the four files named (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json},
  spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json})
  were not written by this packet; they are untracked files of packets
  w02b-p01-014 and w02b-p02-036 working in the same tree. Not touched
  (deleting or editing another packet's files is outside the edit rule).
- MP-0 re-checked: held-sources.json has no Walley entry; no Walley file
  under source/; source/references/p15-imprecise-probability holds only the
  Miranda survey and De Bock-De Cooman 2015. Still blocked_source.
- Route: the chapter is still not \input in handbook/parts/p15.tex or
  handbook/annex/p15.tex (driver files, lead only); blocked_policy part
  unchanged.
- Checks: unit-compile ok (0 errors, 0 overfull, no undefined refs/cites);
  find_fused_spaces no hits; check.py --tree no finding naming these files.

## Continuation

No owned-file writing remains that the held sources allow. Remaining: (1)
acquire Walley 2014 StatsRef (DOI 10.1002/9781118445112.stat01581, complete
article) and match C01-C05 definitions, coherence, natural extension and
conditioning to it or record the version difference; (2) lead adds the body
and annex \input lines and applies the three patch requests.
