# w02ca-p02-008 (P2 ch. 13, sections 13.1-13.3), block 1

Packet: work/waves/w02ca/packets/w02ca-p02-008.json. label_tag p02-w02c-p02-008 (no new labels were needed; all changes are inside existing labelled environments of the w02b-p02-010 host files).

## Gaps addressed (from the independent assessment of D-P2-001-GOAL-03)

1. ND side, labelled discharge. sheet:nd-cpl (handbook/registry/calculi/nd-cpl.tex line 16 and rows 23, 24, 26, 29) and the inherited derivation definition (handbook/restoration/inherited-02193-02340.tex lines 14-27) discharge exactly the open occurrences marked with the application's label, possibly some but not all occurrences of the formula. Changes:
   - def:p02-w02b-p02-010-setting item 2 (body lines 46-64): discharge restated by labels; the "applies to all open occurrences" clause removed.
   - annex:p02-w02b-p02-010-nd-to-hilbert (annex lines 443-545): the equalities oa(D) = Gamma_1 minus {alpha} etc. replaced by the inclusion (*): Gamma_k is a subset of oa(D) when the last application discharges nothing in D_k, and of oa(D) u {delta} when it discharges occurrences of delta in D_k; proved from the path definition of openness. The or-E, to-I, neg-I and RAA cases go through Theta = tr_H[oa(D)], monotonicity and DT (thm:p02-hilbert-deduction is stated for every premise set, so it applies when tr_H(delta) already lies in Theta).
   - annex:p02-w02b-p02-010-nd-structural part (3) (annex lines 256-281): the grafting argument is now explicit about labels (replaced occurrences are open, hence undischarged; copy labels are reserved and fresh; unlabelled leaves are never discharged; each application keeps exactly its nonempty discharged set). This is the step behind Corollary thm:p02-w02b-p02-010-hilbert-equivalence(1), right to left.
   - annex:p02-w02b-p02-010-hilbert-to-nd (annex lines 353-441): A1 case split removed; one derivation ([phi]^1, [psi]^2, and-I, and-E1, to-I label 2, to-I label 1) works for every phi, psi including phi = psi. A2 and A3 justifications restated by labels. The theorem's rule list in the body no longer names and-E2, which no axiom derivation now uses.
   - def:p02-w02b-p02-010-vacuous (body lines 433-462): the false claim that the padding detour fails for P -> (P -> P) is removed. The warning now says the detour works on the sheet because of the labels, would fail under an all-occurrence reading of discharge (which the sheet does not adopt), and that partial discharge is why the map into H uses an inclusion.
   - def:p02-w02b-p02-010-procedure (body lines 325-364): A1 case split removed; side conditions restated by labels; the ND-to-H step notes that a partly discharged formula is put back by monotonicity.
   - def:p02-w02b-p02-010-example (body lines 414-427, new paragraph): a derivation that discharges one of two occurrences of P, with oa(D) = {P}, mapped to {P} |-_H P -> P.
   - Comparison paragraph (body lines 103-121): hypotheses as set members (H, removed only by DT), as labelled occurrences (ND), and as antecedent multiset occurrences with no discharge (LK; Cut versus Mix).

2. LK side, Mix. sheet:lk has the Mix row (handbook/registry/calculi/lk.tex, rule:lk-mix).
   - def:p02-w02b-p02-010-setting item 3 (body lines 65-79): the LK_CPL rule set is stated exactly as all rows of sheet:lk except the four quantifier rows, Mix included, with the Mix display and its side condition.
   - annex:p02-w02b-p02-010-lk-to-hilbert (annex lines 626-680): new paragraph "Removing Mix". Each Mix becomes m-1 C_R steps, n-1 C_L steps and one Cut with the same conclusion; then the Mix-free construction of annex:p7.calculi.3 applies.
   - annex:p7.calculi.3 (handbook/annex/p07/calculi-and-cut-elimination-supplement.tex lines 87-95 and 147): Mix case added to the LK-to-ND translation. Both translations depend on supports only, so the translated Mix premises are the translated premises of the Cut on the Mix formula. The exhaustiveness sentence now names Mix.
   - The statement of thm:p02-w02b-p02-010-lk-to-hilbert and step 4 of the procedure mention Mix.

## Existing treatment checked
I read every entry in the packet's "existing" list. No second treatment was written. A-006 (Hilbert sheet with a named deduction theorem) is already on handbook/registry/calculi/hilbert-cpl.tex lines 8-27 and was not edited.

## Readonly unit
ED26-SRC-008-001 (Sundholm, Systems of Deduction) belongs to w02c-p02-006 and is not written here.

## Build evidence
The owned w02c-p02-008 body and annex files were not created, because no new content needed a separate file and creating them would duplicate or stub. The packet's own unit-compile therefore cannot build. A scratch packet with the same template, pointed at the edited host pair (w02b-p02-010 body and annex), compiled ok with no errors and no undefined references or citations. A scratch P7 build of the p07 supplement body and annex had no TeX errors. The only items it flagged are pre-existing \ref targets to sheet:* labels; \calculussheet defines those labels and the label scanner does not index them. find_fused_spaces found nothing. check.py --tree handbook reported no findings in the edited files.

## Continuation
All three gaps listed for D-P2-001-GOAL-03 now have body text and annex proofs. Nothing is pending in this block.
