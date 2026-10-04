# P2 22.1-22.2: one-sorted reduction at every cardinality (w02b-p02-033)

## Provenance

- Packet: work/waves/w02b/packets/w02b-p02-033.json; unit ED26-REQ-D-P3-007-01 (components D-P3-007-C01, GOAL-01, GOAL-02, GOAL-03).
- Gap closed: the reduction and correspondences were stated only for at most countable Sort, F, R (variants.tex 33-40), while def:p02-fol-signature allows F, R of any size.
- Source: the unit's source presentation is the handbook itself (variants.tex, higher-order-supplement.tex, the w02-p02-038 files). No external source-specific presentation is required; Manzano1996 is not in held-sources.json and is not cited with a locator. No new bib keys.
- Handbook dependencies used and opened: def:p02-fol-signature (first-order-syntax-semantics.tex 19-38), lem:reduct-invariance (restoration/inherited-03927-04061.tex 69-81), thm:fol-compactness (restoration/inherited-04921-04967.tex 5-15, holds for every signature under AC), host defs/lemmas of w02-p02-038.

## Mathematical design

- Parameter form: free sorted variables become fresh constants n_v = (W,v) (fresh by Foundation); bound variables are renamed per formula through finite injective environments (least unused x_k). Premises: Ax_sort (Ne/Ct/Cl/Dj) + ParGuard + tr^n[Gamma]; no coverage axiom; Cov for finite Sort. Holds for every cardinality of Sort, F, R; no choice.
- Variable form: for any injective renaming iota (exists iff Var_MS countable), a bridge lemma derives thm:p02-many-sorted-translation and clauses 1-3 of thm:p02-w02-p02-038-strict-correspondence and thm:p02-w02-p02-038-coverage-reduction for F, R of any cardinality.
- Impossibility: Sort uncountable => no injective renaming; any non-injective renaming breaks the equivalence (same-sort merge: u=w becomes valid; cross-sort merge: guards contradict Dj).
- Coverage-not-elementary (host) proof places no bound on Sort/F/R; noted in body.

## Existing treatment found

- Listed: variants.tex sec:p02-many-sorted; higher-order-supplement annex:p2.hol.5; w02-p02-038 body/annex. Extended, not duplicated.
- Not listed in the packet but relevant: the empty-sort comparison clause 4 (thm:p02-w02-p02-038-empty-comparison, host body ~line 596; annex ~551) uses countability of the symbol set for a choice-free selection. Not part of this unit's components; left unchanged. Lead may route it if the empty-sort variant is to be extended to uncountable symbol sets.

## Continuation

- Written: body handbook/parts/p02/many-sorted-and-alternative-first-order-w02b-p02-033.tex; annex handbook/annex/p02/many-sorted-and-alternative-first-order-w02b-p02-033.tex; host pointer added at w02-p02-038 body, Inputs paragraph.
- Patch request: work/waves/w02b/patches/w02b-p02-033.json (replace variants.tex 33-40 restriction). Not applied (read-only host).
- Driver inputs needed (lead): p02.tex after parts/p02/many-sorted-and-alternative-first-order-w02-p02-039; annex/p02.tex after annex/p02/many-sorted-and-alternative-first-order-w02-p02-039.
- Self-checks: see return file.
- Self-checks run: find_fused_spaces (no hits), unit-compile ok (12 small overfull boxes, largest 19.9pt from long theorem titles), check.py --tree handbook (no finding on these files). Return file written.
- Pitts1995Draft locators used (verified in held PDF, printed pages = PDF page minus 1): Section 2, p. 5 (per-sort countable variable sets); Section 2.1, Definition 2.1.1, p. 6 (single countable Var, sorts in contexts); Section 2.3, p. 10 (signature Sg_C with the objects of C as sorts; a set only for small C).
