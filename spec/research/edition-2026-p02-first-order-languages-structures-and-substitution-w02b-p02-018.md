# Edition 2026, P2 sections 16.5-16.7: eliminating a defined relation symbol (w02b-p02-018)

## Provenance

- Packet: work/waves/w02b/packets/w02b-p02-018.json (label_tag p02-w02b-p02-018, heading level \chapter, toc tag `%% toc: P2 16 16.5,16.6,16.7`).
- Gap addressed: D-P3-010-GOAL-02, satisfaction translation. The existence and uniqueness of the expansion, the definition of the definitional extension (GOAL-01) and conservativity (GOAL-03) are in handbook/restoration/inherited-03729-03907.tex lines 90-178 (example "Definitions inside a theory", thm:definitional-conservativity and its proof, derivability transfer paragraph).
- Source presentation for D-P3-010 is the handbook's own mathematical presentation (packet: "handbook-mathematical-presentation:D-P3-010"); no external source is used, no external locator is written, and the intake bib carries no key.
- Handbook results relied on (all read in this session): thm:fol-unique-readability (inherited-03105-03165), def. of formulas, Var, FV, complexity c (inherited-03166-03239), capture-avoiding substitution with least-fresh-variable choice, lem:substitution-complexity, lem:substitution-fv (inherited-03240-03428), structures, expansion/reduct, assignment update, term value, term coincidence (unlabelled), lem:term-substitution (inherited-03429-03518), satisfaction, lem:fol-coincidence, thm:fol-substitution, consequence for formulas (inherited-03519-03680), lem:reduct-invariance (inherited-03927-04061), thm:fol-soundness (inherited-04109-04213), thm:fol-completeness (inherited-04713-04920), defined biconditional (inherited-01661-01816).

## Existing treatments found

- Listed: inherited-03729-03907.tex (on route).
- Not listed: handbook/parts/p02/first-order-syntax-semantics.tex lines 502-544 (def:p02-fol-definitional-extension, thm:p02-definitional-conservativity) with annex handbook/annex/p02/first-order-syntax-semantics.tex annex:p2.2.syn.11. Neither file is input by handbook/parts/p02.tex or handbook/annex/p02.tex (off route). It contains no satisfaction translation either. The new chapter links only to the on-route labels.

## Design decisions

- Simultaneous instance phi(t_1,...,t_n) is defined in two stages (rename x_i to fresh z_i, then insert t_i for z_i) using the handbook's single capture-avoiding substitution, with z_1..z_n the least variables outside Var(phi), the x_i and Var(t_i). Renaming first is needed when an argument contains a later defining variable (worked in the warning).
- The translation theorem is proved for every L-structure M (not only models of T), with the model-of-T specialization stated explicitly in the theorem, as the duty words it.
- Notation: R^{M}_{phi} for the defined relation (already registered in symbols.csv row for "relation defined by a formula", which avoids R^*), M_phi for the expansion, psi^* for the translation (the duty's own notation). Star overlap with the global Kleene-star row is recorded as a proposed decision in the return.
- Placement: the packet's insertion point (after restoration/scope-SRC-03927-04061 in parts/p02.tex) sits inside ch:fol-deduction (its sec:fol-deduction-02 and -03 follow); a \chapter there would detach those sections from their chapter. Proposed placement: after restoration/scope-SRC-03908-03926 (end of ch:fol-theories, before ch:fol-deduction). The forward references to lem:reduct-invariance, thm:fol-soundness and thm:fol-completeness match the forward references already in the inherited proof.

## External citation

- Kleene, Introduction to Metamathematics, held as the 1974 seventh reprint (source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf). Read in this session: \S 74 "Eliminability of descriptive definitions", printed p. 405, the definition of eliminability by the elimination relations (I)-(III) and the consequences (IV)-(V). Cited as \cite[\S\,74, p.~405]{Kleene1952}; summarized in own words, no symbol of Kleene's reproduced.

## Continuation

- Body written: handbook/parts/p02/first-order-languages-structures-and-substitution-w02b-p02-018.tex (1-392).
- Annex written: handbook/annex/p02/first-order-languages-structures-and-substitution-w02b-p02-018.tex (1-362), four annex items matching the four body results.
- Corollary clause 3/4 generalized to arbitrary premise sets Gamma of L_R-formulas (T u {delta_R} u Gamma |= psi iff T u Gamma* |= psi*), which gives the counterparts of Kleene's three elimination relations.
- Checks run: find_fused_spaces no hits; unit-compile ok; check.py --tree shows no finding on these files.
- Open for the lead: driver insertion (body after parts/p02.tex line 67, annex after annex/p02.tex line 30). FLRV1 units were closed before this packet; SRC-001-001 and SRC-007-001 belong to w02b-p02-001.
