# w02b-p15-040: P15 166.1 Entropy of discrete distributions and its characterization

Packet: work/waves/w02b/packets/w02b-p15-040.json. label_tag p15-w02b-p15-040.
Owned files: handbook/parts/p15/information-and-description-based-inference-w02b-p15-040.tex,
handbook/annex/p15/information-and-description-based-inference-w02b-p15-040.tex, the intake bib
and symbol CSV, this note and the return JSON.

## Source opened in this session

Shannon, "A Mathematical Theory of Communication", 55-page corrected reprint,
source/references/acq-r1-ACQ-2026-10-0320/shannon-1948-mathematical-theory-communication.pdf
(SHA 256 digest begins 6e4e3411; listed in spec/coverage/edition-2026/held-sources.json; PDF page = printed page).
Pages read and rendered: 1-2 (Introduction: semantic aspects irrelevant to the engineering problem;
logarithmic base = unit; bits, decimal digits, natural units), 10-12 (Section 6: three requirements,
Fig. 6 example, Theorem 2, K = unit, H(x) labelling convention, properties 1-6), 13 (start of Sec. 7,
confirming Sec. 6 ends on p. 12), 28-29 (Appendix 2 derivation), 35-38 (Section 20, nine properties).

Locators used in reader text: pp. 1-2, 10, 11, 12 (via sibling labels only), 28-29.

Source observations recorded for provenance:
- Theorem 2 (p. 11) requires "monotonic increasing"; Appendix 2 uses only A(s^m) <= A(t^n) <= A(s^{m+1}),
  i.e. nondecreasing, plus A(s) > 0 to divide; strictness is what makes K positive. Recorded as
  item 3 of thm:p15-w02b-p15-040-characterization.
- Appendix 2 uses requirement (3) only with uniform second-stage choices; the theorem is stated
  with (S3u) and the general grouping (S3) is derived in item 2.
- Section 20 item 8 (p. 37): the first display for H(y) lacks the leading minus sign required by the
  definition; the following display H(y) = H(x) - int p log J(x/y) is consistent with the definition.
  Section 20 item 9 (p. 38) writes log|a_ij| with |a_ij| a determinant; the absolute value of the
  determinant is what enters. Both are handled in w02b-p15-041's 166.2 text (thm:p15-w02b-p15-041-coordinates).

## Existing treatments found (A9)

Listed in packet: rationality-4-1 (thm:p15-rat41-indifference: uniform maximizes H in bits),
strong-law-applications (def:p15-finite-alphabet-source, thm:p15-finite-alphabet-entropy: H in nats,
0 <= H <= log m).
Not listed in packet, found in this session:
- handbook/parts/p15/information-and-description-based-inference-w02b-p15-041.tex (166.2, packet
  w02b-p15-041) with its annex: finite joint/marginal/conditional entropies, subadditivity, chain
  rule, conditioning bound, averaging (Section 6 properties 3-6), and all nine Section 20 properties
  (density entropy with existence condition, Gibbs for densities, bounded volume, joint/conditional,
  averaging, change-of-variables premise as proofboundary def:p15-w02b-p15-041-cov, coordinates,
  linear case, difference invariance, Gaussian and half-line maxima). 166.1 links to it instead of
  writing a second treatment.
- handbook/parts/p15/information-and-description-based-inference-w02b-p15-044.tex (166.7): Gibbs
  inequality, Shannon's Gaussian and half-line maxima, reference-measure dependence.
- thm:p15-rmdl-gibbs (Rissanen chapter): countable Gibbs inequality, used for item 5 of the domain theorem.
- measurement-uncertainty.tex lines 225-228: differential entropy definition in natural units.

## Component map

- ED26-METHOD-entropy-C01: def:p15-w02b-p15-040-entropy, thm:p15-w02b-p15-040-domain (+annex).
- C02: thm:p15-w02b-p15-040-characterization with full Appendix 2 proof in annex; Section 6
  properties 1-2 in thm:p15-w02b-p15-040-domain items 4-5; properties 3-6 linked to 166.2 labels.
- C03: linked to 166.2 continuous section (w02b-p15-041); worked coordinate change
  def:p15-w02b-p15-040-coordinates computed both directly and through the Jacobian.
- C04: def:p15-w02b-p15-040-not-truth and def:p15-w02b-p15-040-contrast (computed contrasts).
- C05: def:p15-w02b-p15-040-dependence (two joint tables on the same marginals) and
  def:p15-w02b-p15-040-coordinates (y = -log x).
- ED26-BM-RAT2021-4-1: readonly, owner w02b-p15-022; not touched. The assessment dispute about
  Hajek-Staffel p. 247 KL figures (0.438, 0.572) concerns that owner.
- ED26-P15-CH-strong-law-applications C001-C016: open=false in the packet; strong-law-applications.tex
  is a readonly host here; not modified.

## Continuation

- Session 1 (4 October 2026): wrote body (426 lines) and annex (218 lines); intake bib entry copied
  verbatim from the w02b-p15-041 intake (same key) for merge dedup; symbol intake rows scoped to
  this chapter's labels. unit-compile ok (3 overfull boxes: two from long annex labels in headings,
  one 0.12pt). check.py on owned files: only bib-key for Shannon1948MathematicalTheory (intake key).
  find_fused_spaces: no hits.
- Open: none in owned files. Dependency: C02 properties 3-6 and C03 rely on w02b-p15-041's
  166.2 labels; if that packet renames them, the \cref targets in sec:p15-w02b-p15-040-worked and
  def:p15-w02b-p15-040-method must follow. The multivariable change-of-variables theorem is a stated
  premise there (def:p15-w02b-p15-041-cov), not proved in the handbook.
- Session 2 (4 October 2026): the only remaining gaps relayed were the ED26-BM-RAT2021-4-1
  C03/C04 (Hajek-Staffel p. 247 KL repair figures 0.438/0.572 summing to 1.01, not stated beside
  the handbook's (3/7, 4/7)) and C05 (dependent-source set; Savage/Bolker, Lewis/Skyrms diachronic
  Dutch book and converse, van Fraassen Reflection, Easwaran expected accuracy, Pettigrew on the
  Principal Principle, Armendt/Skyrms for Jeffrey conditioning, De Bona-Staffel log-inaccuracy)
  disputes. That unit is a readonly unit of this packet, owned by w02b-p15-022 (active in this
  run), and its host rationality-4-1.tex (body and annex) is a readonly host here; nothing was
  written for it and no patch request was filed, so the owner's work is not duplicated. Owned files
  unchanged; re-ran unit-compile (ok, 3 overfull), check.py (only bib-key for the intake key
  Shannon1948MathematicalTheory), find_fused_spaces (no hits); all \cref targets resolve.
- Session 3 (4 October 2026): relayed hard guards. G8 fixed: the digest note on line 12 now reads
  "SHA 256 digest begins 6e4e3411" (find_fused_spaces: no hits on all owned files). G1: the four
  flagged files (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json} and
  spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json})
  are untracked notes owned by packets w02b-p01-014 and w02b-p02-036; this packet never wrote them and
  may not modify or remove them (A8), so the guard attribution must be resolved by the lead. Owned
  reader files unchanged; unit-compile ok (3 overfull); check.py only bib-key for the intake key.
- Session 4 (4 October 2026): the same four G1 files were relayed again. Re-checked with read-only git
  status: all four are still untracked (??) notes belonging to packets w02b-p01-014 and w02b-p02-036;
  this packet did not create or edit them and A8 forbids modifying or deleting them, so the guard
  cannot be cleared from this packet. Lead action needed: attribute those files to their owner packets
  (or exclude untracked files of other packets from this packet's G1 diff). Owned reader files
  unchanged; unit-compile ok (3 overfull); check.py only bib-key for the intake key
  Shannon1948MathematicalTheory; find_fused_spaces no hits; every \cref target in body and annex
  resolves to a label in handbook/parts or handbook/annex.
