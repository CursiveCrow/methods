# w02-p01-003: section 1.5 (changing a calculus, a language, or a semantic class)

Provenance note for packet `work/waves/w02/packets/w02-p01-003.json`, label tag
`p01-w02-p01-003`. Session date 2026-10-04.

## Gap addressed

Assessment gap for 1.5: the active reader route needs an explicit case where
the formal language L itself changes, with what must be re-specified and the
formulas on which old and new systems are compared. The host example
`handbook/restoration/inherited-00798-00852.tex` lines 46-54 (FLRV1-U00059,
source lines 843-851) changes only C and S. The host is read-only and was not
edited; the new section completes it and links back to `sec:levels-01`.

## Inputs opened this session (held source FLRV1, Version 1.0)

`source/formal-logic-reference.tex` (packet held path), read at lines:
- 173-193 title page (title, Version 1.0, 9 August 2026);
- 798-851 chapter "Levels, Objects, and Consequence", section "Formal logic and
  a logical system" (definitions and the example of FLRV1-U00059);
- 915-960 definitions "Semantic consequence", "Derivability";
- 3038-3130 chapter "First-Order Syntax": "First-order signature" (disjointness),
  "Term" (least set), "First-order formula";
- 3166-3180 "Variables occurring in a term";
- 3240-3330 "Capture-avoiding substitution" (fresh variable = least variable
  outside Var(psi) u Var(t) u {x,y}), "Alpha-equivalence" (least congruence);
- 3425-3475 chapter "Structures, Satisfaction, and Translation": "First-order
  structure" (nonempty domain), "Signature extension, expansion, and reduct";
- 3519-3535 "Satisfaction"; 3600-3672 "Truth, validity, and semantic consequence";
- 3729-3770 chapter "Theories and Axiomatization"; 3820-3907 definitional
  extension example and theorem "Conservativity of definitional extensions"
  (`thm:definitional-conservativity`) with derivability transfer remark;
- 3927-4015 chapter "First-Order Deduction": section "Natural-deduction rules for
  quantifiers and equality", "First-order derivability", lemma "Invariance under
  reduct" (`lem:reduct-invariance`);
- 4105-4125 "Soundness of first-order natural deduction" (`thm:fol-soundness`);
- 4505-4527, 4555 Henkin--Lindenbaum lemma, expanded signature L^H by new
  constant symbols; 4712-4735 "Strong completeness" (`thm:fol-completeness`, AC
  hypothesis); 4921-4950 "First-order compactness" (`thm:fol-compactness`,
  L^H-structure and reduct).
Handbook routes confirmed: these labels live in restoration files
`inherited-03729-03907`, `03927-04061`, `04109-04213`, `04713-04920`,
`04921-04967`, all input by `handbook/parts/p02.tex`.

## Existing treatment search (A9)

- Listed: `handbook/restoration/inherited-00798-00852.tex` (sec:levels-01) and the
  P14 glossary pointers. Extended by linking, not duplicated.
- Not listed but found: `thm:definitional-conservativity`
  (`handbook/restoration/inherited-03729-03907.tex` lines 109ff), a theory-level
  language change by one relation symbol with defining axiom; the new section
  cites it as the conservative contrast to the failure lemma. Also
  `def:p02-fol-expansion-reduct` in `handbook/parts/p02/first-order-syntax-semantics.tex`
  line 271 (not on the p02 driver route); not cited because off route; the
  restoration definition is cited through the source locator instead.
- No handbook file states the comparison of consequence/derivability for a
  signature extension of the logic itself (grep for reduct/expansion/
  conservative across handbook/*.tex).

## Decisions

- Case chosen: first-order signature extension, because the held source supplies
  every definition needed (extension, expansion, reduct, reduct invariance,
  soundness, completeness). Comparison results and proofs are editorial
  completions; the reader text and bib note say so.
- Per-signature notation (`\entails_{\Lang}`, `\mathsf{ND}_{\mathsf{FOL}}[\Lang]`)
  introduced as a convention because the source's relations are implicitly
  relative to one fixed signature and its own text (host lines 40-44) requires
  explicit subscripts when several systems are active. Recorded in the symbol
  intake.
- Derivability converse is proved only under AC (through completeness); stated
  in the reader text as a limitation, not claimed in ZF.
- Corollary on a common sub-signature: the reader text states that whether
  Fm(L1) n Fm(L2) exceeds Fm(L0) is not settled (needs unique readability).
- New bib key `FrozenFormalLogicLanguageChange` in the intake bib (the existing
  `FrozenFormalLogicFoundationsClosure` note is specific to other intervals).
- Source macros guarded outside restoration (\set, \tuple, \restr, \Fm, \Sent,
  \Meta, \ND, \FOL) are replaced by the registered editorial forms.

## Continuation

Component FLRV1-U00059 / gap 1.5 language-change case: written.
Files: body `handbook/parts/p01/languages-logical-systems-and-levels-of-w02-p01-003.tex`,
annex `handbook/annex/p01/languages-logical-systems-and-levels-of-w02-p01-003.tex`,
bib and symbol intakes. Unit compile ok (2 overfull boxes, both in the
bibliography entry rendering). check.py: only bib-key for the intake key.
Open for the lead: insert the two `\input` lines per the packet's insertion
proposal (drivers read-only here); merge intakes.
