# P3 35.9 Failures of compactness and the limits of finitary transfer (w03a-p03-041)

Packet: work/waves/w03a/packets/w03a-p03-041.json (block 1).
Label tag: p03-w03-p03-041.

## Files

- Body: handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-041.tex
- Annex: handbook/annex/p03/comparison-games-and-infinitary-languages-w03-p03-041.tex
- Bib intake: handbook/bib/intake-p03-comparison-games-and-infinitary-languages-w03-p03-041.bib
- Symbol intake: handbook/registry/symbols-intake-p03-comparison-games-and-infinitary-languages-w03-p03-041.csv

Placement (packet insertion proposal): body `\input` after line 206 of
handbook/parts/p03/classification-theory.tex (after
`parts/p03/presentations/n-a-004-02`), placed after the 35.8 file of
w03a-p03-040 when that file exists; annex `\input` after line 7 of
handbook/annex/p03.tex (after `annex/p03/feferman-vaught-composition`), in
the same order relative to the 35.1-35.8 annex files.

## Sources read in this session

Held file: tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf
(SHA-256 digest 1597918d...d77add per packet), the 92-page publisher preview of
Barwise and Feferman (eds.), Model-Theoretic Logics, Perspectives in Logic 8,
Cambridge 2017 reissue (copyright 2016 ASL; first edition Springer 1985).
Read from the reading derivative, with PDF pages rendered to check glyphs
(PDF page indices 50, 79, 80, 81):

- Barwise, Ch. I: §1.2 p. 6 (compactness and finite/infinite), §1.4 p. 7
  (strong and countable compactness; completeness usually yields
  compactness), §2.1 p. 14 (L(Q0) and L_{omega_1 omega} not countably
  compact; L_{omega_1 omega} has the Löwenheim property; Lindström), §2.3
  p. 16 (interpolation without Robinson consistency; countable compactness
  much weaker), §2.6 p. 19 (upward LS is a compactness argument).
- Ebbinghaus, Ch. II: Definition 1.2.4(i)-(ii) p. 31 (kappa-compact, "of power
  <= kappa" confirmed on the rendered page; the text derivative reads "<"),
  Definition 5.2.1 pp. 60-61 (pinning down; w_kappa; w = w_1), Example
  5.2.3(c) pp. 61-62 (mu_beta with a biconditional, the sentence "< is a
  linear ordering and forall x V{mu_beta(x) | beta < alpha}", w(L_{omega_1
  omega}) = omega_1 with the upper bound from countable admissible fragments),
  Proposition 5.2.4 with proof p. 62 (clauses (1)-(3) of Phi'), §5.3
  Examples 1-2 p. 63 (substitutes: Barwise compactness, boundedness).

Online source (block 2, 2026-10-12): Marker, Lectures on Infinitary Model
Theory, Math 512 lecture notes, UIC Fall 2013, PDF dated 10 January 2014,
163 pp., fetched now from the author's page
https://homepages.math.uic.edu/~marker/math512-F13/inf.pdf (its SHA-256 digest
equals that of the copy used by w03a-p03-039). Version:
author-hosted notes, earlier than the 2016 Cambridge book, which the
w03a-p03-039 note records as behind a paywall; the reader text says the presentation follows
the 2014 notes. Pages read (pdftotext of the fetched file, scratch copy in
tmp/agent-scratch/w03a-w03a-p03-041-b2-author/marker/): p. 39 (Definition
4.1 C0-C7, subset closure in C0), p. 43 (Theorem 4.8), pp. 51-53 (Section 4.4:
Theorem 4.27, Corollary 4.28, the proof printed after 4.28, Exercise 4.29).

## Readings and corrections recorded (not in reader text as provenance)

- Pinning-down is read on the field of <, as in Definition 5.2.1(i).
  Under that reading the ordinal 1 is never pinned down (a strict order with
  nonempty field has at least two field elements), so Example 5.2.3(c)'s
  "every countable alpha != 0" holds for alpha >= 2; the supremum is
  unaffected. Stated in the body after def:p03-w03-p03-041-pinning and after
  thm:p03-w03-p03-041-countable-ordinals.
- Proposition 5.2.4's proof relativizes to {z | Rxz}. Global nullary symbols
  are not localized by relativization, so the construction needs positive
  arities (or a prior nullary-to-unary replacement). The theorem here is
  stated for positive relational signatures (def:p03-w03-p03-041-setting,
  warning item 2).
- A sentence of L_{omega_1 omega} can bind every variable, so the
  relativization parameter is freed by the even renaming v_i -> v_{2i}
  (condition F3); the source does not discuss this.
- The source states 5.2.4 for logics in its general Chapter II sense. The
  handbook theorem is proved for sublogics of L_{omega_1 omega} satisfying
  (F1)-(F4); the general form is stated as not proved here (warning item 1).
- "< is a linear ordering" in Example 5.2.3(c) is read as a strict linear
  order of the whole domain.
- The upper bound w(L_{omega_1 omega}) <= omega_1 is reported, not proved
  (warning item 3); it depends on admissible fragments (35.7, packet
  w03a-p03-039).

## Existing treatments found (A9)

Listed in packet: variants.tex 349-406 (def:p02-lomega-one-omega,
thm:p02-lomega-one-omega-calibration, def:p02-infinitary-derivation,
thm:p02-karp-completeness); w02-p02-039 (verification of the countable
counterexample; proper fragment).

Not listed in packet, found and linked (no second treatment written):
- thm:p02-w02-p02-005-bw-extended-ls (Barwise: LS for countable sets and
  compactness failure for L_{omega_1 omega}), propositional-languages-...-w02-p02-005.tex:1551.
- thm:p02-w02c-p02-003-infinitary-rule (finitary-proof boundary: no sound
  finitary relation complete for countable theories), w02c-p02-003.tex:883.
- def:p02-w02c-p02-003-hinf, thm:p02-w02c-p02-003-infinitary-completeness,
  thm:p02-w02c-p02-003-hinf-soundness (countably many premises),
  thm:p02-w02c-p02-003-hinf-uncountable (countability cannot be dropped),
  w02c-p02-003.tex:1142-1320.
- thm:p02-w02c-p02-003-interpolation, thm:p02-w02c-p02-003-beth.
- def:p03-lindstrom-ordinal / thm:p03-lindstrom-ordinal-code (eta_alpha,
  equivalent to the source's mu_beta in strict linear orders).
- thm:p03-lindstrom (preservation-abstract-logic.tex:458).

Off-route labels avoided: thm:p02-fol-compactness, thm:p02-upward-ls
(first-order-completeness.tex) and thm:p03-los (types-ultraproducts.tex)
are reported dangling by check.py (files not on the static input route);
replaced by thm:p03-compactness-ultraproduct and
thm:p02-upward-ls-elementary-extension, and the ultraproduct in the Łoś
clause is shown infinite directly.

## Component accounting

All twelve packet component ids belong to units ED26-SRC-049-0008 (owner
w03-p03-039, section 35.7) and ED26-SRC-049-0009 (owner w03-p03-040,
section 35.8), which the packet lists as readonly_units. They are not
written here. The section points to those sections in words because
their labels did not exist at writing time.

## Continuation

State (block 2 rerun, 2026-10-13):
- Guard G1 (spec/research/edition-2026-authoring-batch-intake-13.json
  changed outside the owned set): that file was created by the lead's
  commit 6de06cc3 (w02ca route of batch 13); it does not mention this
  packet and this session did not write it. Nothing in it is reverted here
  (it is not an owned file; A8).
- Body item 1 of sec:p03-w03-p03-041-established: the stale claim that
  w03-p03-039 records upward LS failure only as a remark is replaced by
  links to thm:p03-w03-p03-039-upward-ls-failure and part 1 of
  thm:p03-w03-p03-039-ultraproducts (both now in the 039 file).
- After thm:p03-w03-p03-041-transfer: one paragraph distinguishing clause 2
  from 039 ultraproducts part 1 (no second treatment).
- 039 still has no Barwise compactness theorem; 040 has no file. Open
  items 1-2 below unchanged.

Earlier state:

State (block 2, 2026-10-12):
- Guard fixes: body line 178 "with every formula admitted" -> "with every
  formula included" (G14); note line 23 hash label rewritten as "SHA-256 digest" (G8).
- New subsection sec:p03-w03-p03-041-upper-bound (body, after the worked
  example): thm:p03-w03-p03-041-undefinability (Marker Thm 4.27),
  thm:p03-w03-p03-041-bounded (Marker Cor 4.28; w(L_{omega_1 omega}) =
  w_{aleph_0}(L_{omega_1 omega}) = omega_1), warning
  def:p03-w03-p03-041-marker-gaps (three completions of the printed proof:
  subset closure for C0; room above the last placed constant and the m = 0
  case of (*); Cor 4.28 derivation not printed). Annex items
  annex:p03-w03-p03-041-undefinability (full C0-C7 verification) and
  annex:p03-w03-p03-041-bounded.
- Intro conclusions, the paragraph after thm countable-ordinals, warning item
  3, Relationships (047 bounded-omega, 039 extended model existence, 039
  L_{omega_1 omega_1} well-orders) and Exact sources updated.
- This closes former open item 1 (w <= omega_1) by Marker's route. The
  admissible-fragment inequality Ebbinghaus cites remains unproved here.
Open items:
1. Ebbinghaus Proposition 5.2.4 in his general-logic form not proved.
2. The countable admissible fragment inequality behind Ebbinghaus's own
   derivation of the upper bound is not proved (needs Barwise compactness,
   readonly unit ED26-SRC-049-0008, owner w03-p03-039; 039 now has KP and
   admissible sets, no Barwise compactness label).

Earlier state (block 1 rerun):

State (block 1 rerun, 2026-10-12): the assessment gap X-1 ("owned files do
not exist") was stale; the body and annex exist with the hashes recorded in
the wave snapshot. This pass re-read the held source (Ebbinghaus II pp. 31,
60-63 rendered from PDF pages 51, 81, 82; Barwise I pp. 6, 7, 14, 16, 19 in
the reading derivative) and made these changes to the body:
- sec:p03-w03-p03-041-established now links the 35.5-35.7 file
  (thm:p03-w03-p03-039-compactness-failure, -extended-model-existence,
  -downward-ls) and notes that transfer clause 3 proves the upward LS
  failure that 039 records only as a remark.
- The prose pointers to an admissible-fragment section and to a 35.8
  section were removed: neither exists (039 reports Nadel ch. VIII as
  blocked_source; 040 has no file). The text now says Barwise compactness,
  Hanf numbers and larger-language LS bounds are not stated or proved here
  and nothing depends on them.
- Warning item 3: the source asserts the admissible-fragment inequality
  without proof at p. 62; wording corrected.
unit-compile ok; find_fused_spaces clean; check.py shows no finding in the
owned files.
Open items:
1. w(L_{omega_1 omega}) <= omega_1 not proved (needs admissible fragments).
2. Ebbinghaus Proposition 5.2.4 in his general-logic form not proved.
3. If w03a-p03-039 later publishes Barwise compactness or w03a-p03-040
   publishes Hanf-number / LS-bound labels, add \cref links in
   sec:p03-w03-p03-041-established and warning item 3.
