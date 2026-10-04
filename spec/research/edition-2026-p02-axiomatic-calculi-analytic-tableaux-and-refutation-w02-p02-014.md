# w02-p02-014 — propositional and first-order tableau metatheory (P2 13.4, 13.5; 13.6, 13.7 blocked)

Packet: work/waves/w02/packets/w02-p02-014.json; label_tag p02-w02-p02-014.

## Files

- handbook/parts/p02/axiomatic-calculi-analytic-tableaux-and-refutation-w02-p02-014.tex (body, lines 1-850)
- handbook/annex/p02/axiomatic-calculi-analytic-tableaux-and-refutation-w02-p02-014.tex (annex, lines 1-760)
- handbook/registry/calculi/tableaux-cpl.tex (editable host; identity text of line 11 extended)
- handbook/registry/symbols-intake-p02-axiomatic-calculi-analytic-tableaux-and-refutation-w02-p02-014.csv
- handbook/bib/intake-p02-axiomatic-calculi-analytic-tableaux-and-refutation-w02-p02-014.bib (comment only; no new keys)
- work/waves/w02/patches/w02-p02-014.json (ten patch requests for read-only hosts; entries 6-10 are the first-order ones)

## Provenance

- Smullyan1968 is not held (no entry in spec/coverage/edition-2026/held-sources.json). The section cites it
  only as the attribution already made on the sheet, with no locator. All definitions and proofs are
  editorial, written for the retained-occurrence / marked-position format of sheet:tableaux-cpl, and are not
  transcriptions. No locator was written for any source.
- Semantics used: inherited definitions in handbook/restoration/inherited-01817-01898.tex
  (sec:prop-syntax-semantics-02: valuation, \widehat v, satisfaction, satisfiable, valid, consequence) and
  grammar/unique readability in handbook/restoration/inherited-01661-01816.tex (thm:prop-unique-readability;
  top is the abbreviation neg-bottom).
- First-order contrast uses def:p02-fol-tableau and thm:p02-fol-tableau-adequacy
  (handbook/parts/p02/first-order-calculi-supplement.tex 100-150, cited status there) and the on-route
  thm:fol-validity-undecidable (handbook/restoration/inherited-08248-08305.tex, cited Church1936). The
  label thm:p04-fol-validity-undecidable exists only in an off-route file and was not used.
- Notation decision: |B| was avoided because the registry reserves |.| for cardinality; \operatorname{fm}(B)
  is used for the formula set of a branch.

## Design decisions

- Branches are formalised as (list, set of marked positions); a tableau is the last member of an expansion
  sequence of branch lists. The sheet's "append on every open branch through it" is a finite run of single-
  branch steps (children keep positions). This makes saturation determinate: terminal formulas p, neg p,
  bottom, neg bottom need no mark (the gap noted for neg-bottom).
- Termination measure mu(B) = sum over unmarked expandable positions of 3^sz; each step lowers it by at
  least 3^(n-1); the construction tree bound gives at most 2^(mu0+1) - 2 steps.
- The existing thm:p02-tableau-adequacy (read-only host, cited=Smullyan1968) is not duplicated: the new
  lemmas prove its clauses, and the patch file proposes switching its status to
  proved=annex:p02-w02-p02-014-tableau-adequacy with an assembling annex item in
  handbook/annex/p02/propositional-hilbert.tex. The status patch and the annex patch must be applied
  together and only after the new body and annex files are input by the drivers.

## Existing treatments found

- Listed: propositional-hilbert-tableaux.tex (on route), sheet:tableaux-cpl, first-order-calculi-supplement.tex,
  p14 classical-and-constructive-calculi.tex (prose saying the theorem is cited; patch proposed).
- Not listed in the packet: handbook/parts/p02/propositional-calculi.tex and first-order-calculi.tex carry
  duplicate copies of def:p02-cpl-tableau / thm:p02-tableau-adequacy / thm:p02-fol-tableau-adequacy; they are
  off the p02 driver route and were not edited or cited. handbook/parts/p02/propositional-rejection-and-refutation.tex
  (sec:p02-classical-rejection, Citkin2013JankovRefutation) is the on-route rejection treatment; linked as a
  relationship only.

## Blocked: 13.6 and 13.7 (ED26-SRC-022-002, Skura, Refutation Systems in Propositional Logic)

Required work: Tomasz Skura, "Refutation Systems in Propositional Logic", Handbook of Philosophical Logic,
2nd edition, Volume 16 (Springer, copyright 2011), pp. 115-157, DOI 10.1007/978-94-007-0479-4_2.
The packet's held paths are tmp/src022/RuysWinterScope.pdf (Ruys and Winter, "Quantifier Scope in Formal
Linguistics", a different chapter) and tmp/src022/front-canonical.pdf (volume front matter, which lists
the chapter but contains none of its text). The other SRC-022 held file is Avron-Zamansky's
non-deterministic semantics chapter, also a different chapter. tmp/src022/full-ch2.pdf exists on disk but
is not registered as held for SRC-022 and was not opened as a source. Nothing was written for 13.6/13.7.

## First-order session (block 2)

- Written: body lines 319-850 (sec:p02-w02-p02-014-fol-contrast, -fol-calculus, -fol-herbrand,
  -fol-systematic, relations), annex lines 301-760 (sec:annex-p02-w02-p02-014-fol and nine annex items).
- Design: first-order branches are (list, done-task set D); tasks <i>, <i,t>, <=,t>, <i,j,phi>; limit branches
  of paths through infinite expansion sequences; saturation = every available task done, which is the
  "fair and saturated" of def:p02-fol-tableau. Equality calculus T^= adds reflexivity (any closed term) and
  one-occurrence left-to-right replacement on atomic sentences, the tableau forms of =I/=E on sheet:nd-fol
  (thm:p02-equality-laws). Not taken from any held source; no locator written.
- Model: quotient Herbrand structure M_H over CT_Gamma / ~_H with r ~_H u iff identical or r=u in H; for
  equality-free H it is literally M_{B+at} of thm:p02-fol-tableau-adequacy. Truth lemma by strong induction
  on rho = 2c (negations) or 2c+1 (others), because c(neg phi) can equal c(phi -> psi) when psi is atomic.
- On-route dependencies used: thm:fol-substitution, lem:term-substitution (via S), lem:substitution-complexity,
  lem:substitution-fv, lem:reduct-invariance, thm:fol-unique-readability, sec:fol-semantics-02 (consequence),
  thm:fol-validity-undecidable (cited, used only in the closing boundary remark), lem:fol-truth (comparison).
- Procedure: staged fair expansion; stage n performs all tasks with positions present at stage start and
  term index <= n; halts on all-closed (unsatisfiable) or on a finite open saturated branch (satisfiable).
  Infinite branch construction by a Koenig-style "good branch" argument written in the annex (the on-route
  thm:p06-konig-infinity covers only the binary tree, so it was not cited).
- Patch requests 6-10 (work/waves/w02/patches/w02-p02-014.json): thm:p02-fol-tableau-adequacy status to
  proved=annex:p02-w02-p02-014-fol-tableau-adequacy with an assembling annex item in
  handbook/annex/p02/first-order-calculi-supplement.tex; supplement equality paragraph and comparison-table row;
  p14 classical-and-constructive-calculi commentary. Apply only after the body and annex inputs exist.
- Not done (policy): no registry sheet for T^= (a new file handbook/registry/calculi/tableaux-fol-eq.tex plus
  a showcalculus line in handbook/parts/p14/rule-sheets.tex would be needed; neither is an owned file).
- Overlap: packet w02-p02-025 (sections 17.5, 17.6) also lists D-P3-002-GOAL-02..04; its files did not exist at
  this session. Proposed decision: 025 links to these labels instead of writing a second treatment.

## Continuation

- Done in earlier session: GOAL-01, propositional half of GOAL-03, propositional half of GOAL-04, A-015-C01..C03.
- Done in this session: GOAL-02 (def:p02-w02-p02-014-fol-equality, def:p02-w02-p02-014-fol-branch: quantifier and
  equality rules with freshness, instantiation and fairness), first-order half of GOAL-03 (fol-soundness,
  congruence, herbrand-truth, saturated-hintikka, fol-extraction, fol-completeness), first-order half of GOAL-04
  (fol-procedure, fol-semidecision with infinite branch construction; boundary rewritten).
- Remaining for this packet: lead applies patch requests 1-10 after the driver inputs; optional tableaux-fol-eq
  registry sheet (policy); Skura chapter acquisition for 13.6/13.7 (ED26-SRC-022-002, unchanged blocker).
- Checks at stop: unit-compile ok (4 overfull boxes, all annex headings with long annex ids); find_fused_spaces
  no hits; check.py --tree handbook shows no finding in these files.

### Block 3 (4 October 2026)

- G1 guard hits on spec/research/edition-2026-p02-unit-accounting-w02-p02-042*.{md,json} and -044*: not files of this
  packet, never touched by it; left alone (they belong to packets w02-p02-042 and w02-p02-044). Explained in the return's
  guard_note.
- Re-checked the Skura acquisition: still not held, so 13.6/13.7 remain blocked_source; no text written for them.
- Re-ran unit-compile (ok), find_fused_spaces (no hits), check.py --tree filtered (no findings), forbidden-word scan (clean).
- No content changes this block; remaining items unchanged (lead patches 1-10 and driver inputs; Skura acquisition;
  optional T^= registry sheet, policy).
