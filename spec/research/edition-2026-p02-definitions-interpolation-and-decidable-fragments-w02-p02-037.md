# w02-p02-037 — sections 21.2 (Craig interpolation, shared vocabulary) and 21.3 (Beth definability)

Packet: `work/waves/w02/packets/w02-p02-037.json` (label_tag `p02-w02-p02-037`).

## Files

- Body: `handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02-p02-037.tex`
  (`sec:p02-w02-p02-037-craig`, `sec:p02-w02-p02-037-beth`; insertion proposal:
  `handbook/parts/p02/first-order-logic.tex` after `\input{parts/p02/first-order-depth}`, so the
  two sections fall inside the chapter `sec:p02-first-order-depth`, i.e. the first-order chapter that
  the duties name).
- Annex: `handbook/annex/p02/definitions-interpolation-and-decidable-fragments-w02-p02-037.tex`
  (five annex items; insertion proposal: `handbook/annex/p02.tex` after
  `\input{annex/p02/first-order-completeness-remainder}`).
- Bib intake: no new keys. Symbol intake: 7 rows.
- Patch requests: `work/waves/w02/patches/w02-p02-037.json` (three replacements in the read-only host
  `handbook/parts/p02/first-order-depth.tex`: the disclaimer paragraph at lines 153-156 and the
  Craig and Beth rows of `tab:p02-fol-metatheorems`).
- Editable hosts (`handbook/parts/p03/preservation-abstract-logic.tex`,
  `handbook/annex/p03/editorial-proofs.tex`): not changed. A one-sentence back-pointer was added to
  the P3 body and then removed again, because the verification run after that edit was refused by
  the environment's permission classifier; the host is byte-identical to its prior state.

## Sources

The packet's source presentations are handbook-internal (`handbook-mathematical-presentation:D-P3-004`,
`D-P3-005`); `units[].held_paths` is empty, and `held-sources.json` holds no file for Craig1957,
Beth1953, Hodges1993 or RobinsonJointConsistency1956. The text cites Craig1957, Beth1953 and
RobinsonJointConsistency1956 for attribution only, with no locator, and states that the proofs
relied on are the book's own. Open item: no page locator for these three works was verified.

Maehara1960 is held (`source/references/acq-r1-ACQ-2026-10-0277/Maehara-1960-Craig-interpolation.pdf`,
J-STAGE scan of Sugaku 12(4) 235-237, 3 PDF pages) and was opened in block 2. Locators read there and
used in the body: p. 236 §2 (Beth's theorem in renamed-copy form, one-place predicate, copy written
with a second predicate symbol Q, provability; definition of "parameter" = symbols other than bound
variables and logical symbols, so free object variables are parameters); p. 236 §3 (Craig's theorem:
interpolant contains as parameters only common parameters; extra clause: if no predicate symbol is a
common parameter, then not-A or B is provable); p. 236 §4 (derivation of Beth from Craig: finiteness
of axioms used, fresh object variable a, Craig applied to A(P) and P(a) => (A(Q) => Q(a)), then Q
replaced by P throughout the derivation); pp. 236-237 §5 (generalized partition statement for
sequents Gamma -> Theta split into Gamma1,Gamma2 / Theta1,Theta2, proof by cases on a cut-free LK
derivation; Gentzen's Hauptsatz excludes Cut). The body describes these in prose only; no formula
from the source is reproduced, so no source notation enters the symbol intake.

Handbook authorities read in this session: FOL syntax (`restoration/inherited-03038-03104.tex`,
`-03105-03165.tex`), substitution and alpha-equivalence (`-03240-03428.tex`), satisfaction, coincidence,
substitution lemma, alpha-invariance, validity (`-03519-03680.tex`), term-substitution
(`-03429-03518.tex`), reduct invariance (`-03927-04061.tex`), theories (`-03729-03907.tex`), soundness
(`-04109-04213.tex`), compactness (`-04921-04967.tex`), P7 Craig/Beth statements
(`-11914-11960.tex`) and proofs (`annex/p07/interpolation-supplement.tex` 300-620), P3 Robinson/Beth
(`parts/p03/preservation-abstract-logic.tex` 95-370) and `annex/p03/editorial-proofs.tex` 290-356.

## Provenance of the proofs

- Formula-form Craig: the annex reduces to the sentence case of `thm:craig-interpolation` (whose
  sentence case is proved in annex:p7.interp.3 before and independently of its free-variable
  paragraph) or the sentence case in annex:p3.abstract.5. The reduction is written at the level of
  the Part II substitution definition (closed-term substitution never renames), a bound-renaming
  claim proved by induction, and a constant-to-variable replacement `eta{v/c}` with the identity
  `eta{v/c}[c/v] = eta` when `v` does not occur in `eta`.
- Equality exemption lemma: own example and proof (truth value of an equality-free,
  vocabulary-free formula is constant over nonempty domains).
- Beth: renaming lemma and equivalence of the P2 renamed-copy formulation with the model formulation
  are proved here; the forward direction then calls `thm:p03-beth-definability` or `thm:beth`
  (both proved, both under ambient Choice), converts derivability to entailment by
  `thm:fol-soundness`, and changes the variable tuple by an explicit equality construction.

## Existing treatments found

All listed in the packet. Also relevant and not listed: `handbook/restoration/inherited-11914-11960.tex`
(the reader-facing statements `thm:craig-interpolation`, already with the free-variable clause, and
`thm:beth`); `handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex` and
`handbook/parts/p07/cut-elimination-and-interpolation.tex` (`thm:p07-craig-interpolation`,
cited=Craig1957; `thm:p07-maehara-partition` is declared in both of these files);
`handbook/parts/p07/proof-complexity.tex` 254-257 (navigation links to INTERP.3/INTERP.4);
`handbook/parts/p09/logic-in-computer-science.tex` 101 and
`handbook/parts/p14/expressiveness-and-representation.tex` 458 (references to
`thm:p02-craig-interpolation`).

## Notes for the lead

- The disclaimer at first-order-depth.tex 156 ("do not claim ... free-variable variants") contradicts
  the new section in the same chapter until patch 1 is applied.
- Symbol choices: the constant instance is written `phi^{\mathrm c}` and the renamed structure
  `N^{\mathrm{ren}}` to avoid the global `{}^*` closure row and the global rho formula-metavariable row.
- New labels resolve only after the body and annex are input by the drivers.

## Continuation

Block 2 (2026-10-04): the assessment's hard guard failures (G1) name eight files under
`spec/research/` belonging to packets w02-p02-054, -042, -044 and -045. They are not in this packet's
owned or editable set and were not written by this packet: the 042/044/045 files carry timestamps
04:01-04:11, after this packet's block-1 return (03:56), and the 054 files are absent from the tree.
They were left untouched (editing them would itself violate A8); the lead must re-attribute or
clear these guard hits. Added in block 2: body 21.3 third proof route (Maehara's derivation via the
formula form of Craig, body 298-319) with verified Maehara1960 locators; equality bullet in the 21.2
limits warning now records Maehara's equality-free clause (body 186-193); relationships paragraph
with Maehara locators (body 368-385); annex second proof of implicit-to-explicit from
thm:p02-w02-p02-037-craig-formula (annex 432-523). Unit compile ok (two overfull annex headings as
before); fused-space check clean; check.py shows no finding in these files.

Block 1 state:
State at return (2026-10-04): 21.2 formula-form Craig with both conditions, procedure, proof routes,
worked example, equality-exemption limitation with proof, limits warning; 21.3 renaming lemma,
equivalence of formulations, Beth corollary in the P2 formulation with finite subtheory, proof
routes (P7 and P3, Robinson route), worked example and non-example, scope warning. Unit compile ok
(two overfull annex headings caused by the long annex ids); fused-space check clean on both files;
`check.py --tree handbook` shows no finding in these files. Remaining: lead inserts the two input
lines and applies `work/waves/w02/patches/w02-p02-037.json`; locators for Craig1957/Beth1953 are not
verified (sources not held).
