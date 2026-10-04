# Packet w02-p02-038 (P2, sections 22.1, 22.2, 22.3): many-sorted reduction, coverage, two-way correspondence, empty and overlapping sorts

Date: 2026-10-04. Label tag: `p02-w02-p02-038`.

## Inputs read in this session

- Packet `work/waves/w02/packets/w02-p02-038.json` (unit ED26-REQ-D-P3-007-01; components D-P3-007-C01, GOAL-01, GOAL-02, GOAL-03).
- `handbook/parts/p02/variants.tex` 1-210 (sec:p02-many-sorted: def:p02-many-sorted-signature, def:p02-many-sorted-structure, def:p02-many-sorted-translation, def:p02-ms-variable-guard, thm:p02-many-sorted-translation and the following paragraph; start of sec:p02-free-logic).
- `handbook/annex/p02/higher-order-supplement.tex` 1-60 (annex:p2.hol.5).
- `handbook/restoration/inherited-03519-03680.tex` (sec:fol-semantics-02: one-sorted satisfaction clauses with connectives bottom, not, and, or, implies; lem:fol-coincidence; consequence definition) and `handbook/restoration/inherited-04921-04967.tex` (thm:fol-compactness, which assumes the Axiom of Choice).
- `handbook/parts/p10/first-order-categorical-semantics.tex` 140-200 (thm:p10-doctrine-tarski and the empty-sort paragraph) and `handbook/parts/p10/adjoint-first-order-calculus.tex` 90-115.
- Held source `citations/Pitts - Categorical Logic (1995, May 18 draft, DVI-derived PDF).pdf` (held-sources.json entry, May 18 draft): Example 2.3.2 read on printed page 11 (PDF page 12), the empty-sort example with sorts bool and hegel, credited there to Goguen and Meseguer 1985.
- `spec/coverage/edition-2026/held-sources.json`: searched for Manzano, Enderton, Ebbinghaus, many-sorted, empty domain, free logic: no held many-sorted textbook. All mathematics here is an in-book development from the handbook definitions; the only external citation is Pitts Example 2.3.2, p. 11, for the empty-sort phenomenon.

## Existing treatments (A9)

Listed in the packet: variants.tex sec:p02-many-sorted, annex:p2.hol.5. Extended, not replaced: the new section supplies explicit clauses, the coverage convention, the full two-way proof (whose clause (iii) is the equivalence of thm:p02-many-sorted-translation), and the empty-sort and overlapping-sort variants.

Found, not listed in the packet:
- `handbook/parts/p10/first-order-categorical-semantics.tex` thm:p10-doctrine-tarski and the paragraph after it (contextual semantics with possibly empty sort carriers; context removal fails). Linked from the empty-sort subsection.
- `handbook/parts/p10/doctrine-quantifiers.tex` 264 and `handbook/parts/p10/powerset-quantifiers.tex` 218-234 (powerset doctrine permits empty sorts). Not linked individually; the p10 theorem above is the entry point.
- `handbook/parts/p14/directory-of-logical-systems.tex` 137-141 (directory card mentions that overlapping sorts change the presentation).
- `handbook/parts/p03/feferman-vaught-composition.tex` 25 and `handbook/parts/p03/maps-elementarity.tex` 17 (many-sorted signatures with nonempty sort domains, used only as a convention).

## Heading level

The packet's computed heading level is `\chapter` (inherited from sibling `variants.tex`, which opens chapter 22). The insertion is after `parts/p02/variants`, inside chapter 22, and the following input continues chapter 22. A `\chapter` heading would split chapter 22 against the toc tag `P2 22 22.1,22.2,22.3`, so the body opens with `\section`, as the sibling packet w02-p02-039 did. The lead should confirm.

## Design notes

- One general notion of sorted structure (carriers possibly empty, possibly overlapping) with context-relative assignments; strict, empty-sort and overlapping-sort semantics are the three restrictions. Two general lemmas (restriction of a one-sorted model; transport of a sorted structure along injections with an arbitrary fill for ill-typed inputs) carry every case; each instance (tagged union with junk point, tagged union with defaults for coverage, plain union with junk point) is checked explicitly.
- Junk point: in the tagged construction it is the pair (Sort, Sort); in the plain-union construction it is the union U itself. Foundation makes both fresh without any choice.
- Coverage: no first-order coverage axiom exists for infinitely many sorts (compactness argument, uses AC through thm:fol-compactness).
- Choice: used in the comparison theorem only where stated (extension of contextual assignments to total ones over strict structures with infinitely many sorts); the closed-term case is choice-free given a fixed injection of the at most countable symbol set into the natural numbers.

## Continuation

- Body and annex written (body 728 lines, annex 659 lines); per-component state is in the return file. Self-checks: fused spaces none, unit-compile ok, check.py no finding on these files.
- Patch requests: `work/waves/w02/patches/w02-p02-038.json` (three cross-links: variants.tex 67-68, a coverage note at thm:p02-many-sorted-translation, and annex:p2.hol.5). Not applied (read-only hosts).
- 2026-10-04 follow-up: guard G14 hit at body line 681 ("cross-sort equality is admitted") reworded to "cross-sort equality is part of the language"; guard function now reports no workflow word in the body file. Re-ran fused spaces (none), unit-compile (ok, 0 errors), check.py tree (no finding on these files).
- Guard G1 hits name spec/research files of packets w02-p02-042, 044, 045 and 054. They are not owned by this packet and were not written in this session; left untouched (A8). Lead to attribute them to their own packets.
