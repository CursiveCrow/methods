# Edition 2026 P15 158.4/158.5 packet w02b-p15-005: Hahn partitions and Stieltjes representations

Date: 4 October 2026. Packet: work/waves/w02b/packets/w02b-p15-005.json
(mode accounting; label_tag p15-w02b-p15-005).

## Source read in this session

Durrett, Probability: Theory and Examples, author version 5 dated
11 January 2019, key DurrettPTEAuthor2019, held file
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
Printed pp. 466-469 (PDF pages 474-477) extracted with pdftotext; printed
p. 468 (PDF page 476) also rendered as an image and read, to confirm the
displayed inclusion {x : f(x) > 0} subset A subset {x : f(x) >= 0} a.e.,
the definition "B subset C a.e. means mu(B cap C^c) = 0", the statement
that two Hahn decompositions differ by null sets, and the start of the
Remark on finite signed measures and the difference F - G (continuing on
p. 469). Source writes alpha_+, alpha_- for Jordan components; the handbook
chapter sec:p15-radon-nikodym uses alpha^+, alpha^-, and the new text
follows the existing handbook notation.

Locators written: p. 468 (twice), pp. 468--469. All seen in the held file.

## Gaps addressed

- ED26-P15-CH-radon-nikodym-C006: radon-nikodym.tex:94 asserted Hahn
  non-uniqueness with no witness. New thm:p15-w02b-p15-005-hahn-partitions
  (all Hahn partitions = signed-null modifications; uniqueness iff no
  nonempty signed-null set; Jordan components partition-independent) and
  thm:p15-w02b-p15-005-density-hahn (source variant p. 468 for Example
  A.4.1; signed-null criterion; witnesses (1/2,1], [1/2,1], (1/2,1] cup C
  for f = 2x-1). The converse direction (every signed-null modification is
  Hahn) is an extension, so marked in the reader text.
- ED26-P15-CH-radon-nikodym-C009: radon-nikodym.tex:149-150 asserted the
  Stieltjes measures need not be Jordan components with no witness. New
  thm:p15-w02b-p15-005-stieltjes-excess (common excess measure rho,
  equivalence with mutual singularity and minimal total mass, converse
  parametrization, witnesses F=G=1_[0,inf) and the 2x/x pair). Extension
  beyond the source remark, marked as such.
- Patch requests (host radon-nikodym.tex body and annex are read-only):
  work/waves/w02b/patches/w02b-p15-005.json links the two host claims and the
  annex aside at radon-nikodym annex 623-624 to the new results.

## Ownership note

The packet lists ED26-P15-CH-radon-nikodym under readonly_units with owner
w02b-p15-002, yet the computed task assigned these two gaps here. The owner
packet has no editable host for radon-nikodym.tex. The lead should check that
the owner did not also write a witness for C006/C009 (none found in the tree
at writing time; grep for "Hahn" and "need not be unique").

## Existing treatment search

grep over handbook/parts and handbook/annex for Hahn, "need not be unique",
minimal Jordan: only radon-nikodym.tex body and annex treat the topic. No
unlisted existing treatment found.

## Continuation

- Written: body handbook/parts/p15/measure-integration-and-product-constructions-w02b-p15-005.tex
  (258 lines), annex handbook/annex/p15/measure-integration-and-product-constructions-w02b-p15-005.tex
  (224 lines), symbol intake CSV, patch file. No intake bib (no new keys).
- unit-compile ok (5 overfull boxes, from long environment titles/labels).
- find_fused_spaces: no hits. check.py --tree: no finding naming these files.
- Product-measures components C001-C016 and the other radon-nikodym
  components: no gap assigned; existing treatment located and reported.
- Remaining: lead to insert driver lines (parts/p15.tex after line 36,
  annex/p15.tex after line 35) and apply the three patch requests.
- r2 block 1 (C009 confirm dispute: host proof lacks an F=G nonzero witness):
  added part (6) to thm:p15-w02b-p15-005-stieltjes-excess (body item after
  part (5)) with annex proof paragraph (6): every nonzero admissible F with
  G=F represents the zero signed measure, Jordan parts zero, mu_F=mu_G=rho
  nonzero. Added an insert_after patch for the host annex proof
  annex:p15.signed-cdf-variation carrying a self-contained witness paragraph,
  and rewrote the C009 body patch to state the witness inline. Anchors
  verified unique in both hosts. unit-compile ok; fused-spaces no hits;
  check.py --tree no finding naming these files.
- Remaining for C009: lead applies the patch file entries and inserts the
  driver lines (blocked_policy).
