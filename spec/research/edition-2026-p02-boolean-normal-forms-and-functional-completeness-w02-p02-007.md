# w02-p02-007 research note (P2 sections 11.1, 11.2, 11.3)

Provenance and decisions for packet w02-p02-007. Reader text carries none of this.

## Sources opened in this session

- Kleene, Introduction to Metamathematics, held file
  `source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf`
  (1974 reprint; bib key Kleene1952 already in handbook.bib). PDF page = printed page + 10.
  Page images rendered and read in this session:
  - p. 113 (PDF 123): section 26 "Equivalence, replacement": A ~ B abbreviates
    (A > B) & (B > A); "equivalent" means provable equivalence in the formal system;
    Theorem 5 *12, *13 (contraposition), *14, *15 (contraposition with double negations
    suppressed), as deducibility relations; *14 and *15 carry the degree sign.
  - p. 118 (PDF 128): section 27 Theorem 7: *31-*34 associative/commutative, *35, *36
    distributive, *37, *38 idempotent, *39, *40 "elimination laws" (absorption).
  - p. 119 (PDF 129): *49 double negation (degree sign), *59 A > B ~ -A v B (degree sign),
    *62 (degree sign), *63 De Morgan's laws with Kleene's attribution to De Morgan 1847.
  - p. 101 (PDF 111, text extraction only): the degree sign marks results whose given
    demonstration is valid for the classical system only.
  Kleene's notation: & for conjunction, a horseshoe for implication, ~ for the object-language
  equivalence, and "equivalent" for provable equivalence. The handbook statements are the
  semantic relation of the active route (\equiv, every valuation agrees) in the active
  route's connectives; Kleene is cited only for the deductive counterparts.
- Active-route captures read: `inherited-01661-01816.tex` (alphabet, primitive constructors,
  top and biconditional as abbreviations, finite conjunction/disjunction conventions),
  `inherited-01817-01898.tex` (valuations, coincidence lemma, \equiv definition),
  `inherited-01946-02186.tex` (whole file), `inherited-02810-02914.tex` 1-30 (tautological
  clauses), `inherited-01554-01579.tex` (writing example using material implication,
  De Morgan and double negation as unlabeled steps).
- Editorial on-route files read: `propositional-substitution.tex` (thm:p02-uniform-substitution,
  thm:p02-replacement), `propositional-metatheory-supplement.tex` (duality section),
  `free-boolean-algebra-and-completeness.tex` 1-200 (thm:p02-fbc-quotient),
  `tseitin-transformation.tex` 1-20, 90-125.
- Off-route: `propositional-syntax-semantics.tex` 195-268 (thm/tab:p02-equivalence-laws,
  not input by parts/p02.tex). Not relied on; labels not reused.

## Existing treatment found that the packet did not list

- `handbook/restoration/inherited-01554-01579.tex` lines 8-15 (sec:writing-foundations-05):
  uses material implication, De Morgan and double negation as unlabeled rewrite steps.
- `handbook/parts/p02/free-boolean-algebra-and-completeness.tex` 150-164
  (thm:p02-fbc-quotient): Boolean laws for the provable-equivalence quotient.
- `handbook/parts/p02/propositional-substitution.tex` 120-141 (thm:p02-replacement), used by
  the application method.

## Decisions

- Notation: the active route writes semantic equivalence as \equiv (registered row for
  "source CPL semantic formula equivalence"); the new section keeps it. Truth values are
  written \mathbf F, \mathbf T because the source macros \True/\False are fenced to restoration
  scopes.
- Law labels are individual lemma labels (thm:p02-w02-p02-007-...), one per law group, each
  with its own annex item; the table cites each label.
- The table includes the further Boolean laws (commutativity, associativity, idempotence,
  units, annihilation, complementation, negated implication) so the apparatus is complete for
  NNF/CNF/DNF rewriting; the six required groups are separate lemmas.
- Limitation result proved in full: the 2^n clause lower bound for CNFs equivalent to
  the disjunction of n conjunctions of distinct variables.

## Continuation

- Written (not assessed): body, annex, symbol intake, bib intake (no new keys), return file.
  Annex ids shortened (dm, dist, abs, dn, mi, cp, lat, bd, ni, taut, cnf) to remove
  overfull annex headings. unit-compile ok with 0 overfull; find_fused_spaces no hits;
  check.py --tree shows no finding on these files.
- FLRV1-U00155..U00166 are pre-existing restoration text (inherited-01946-02186.tex), not
  edited; reported with their line ranges.
- Driver insertion is for the lead (body after parts/p02/propositional-metatheory-supplement,
  annex after annex/p02/propositional-metatheory-supplement).
- Block 2 (2026-10-04): content of body and annex unchanged; re-ran unit-compile (ok, 0 overfull),
  find_fused_spaces (no hits), check.py --tree (no finding on these files). Verified every
  referenced label is defined in a routed file. Remaining gap is route activation only:
  patch request work/waves/w02/patches/w02-p02-007.json (insert_after the
  propositional-metatheory-supplement inputs in parts/p02.tex and annex/p02.tex).
  A-027-C01/C02 reported blocked_policy until the lead applies it.
- G1 guard entries (spec/research files for w02-p02-042/044/045/054) are not this packet's
  files and were not touched here.
