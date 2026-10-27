# Research note: section 39.6, least and partial fixed-point logics (packet w03a-p03-059)

## Source read in this session

- Held file `source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf`
  (E. Graedel, "Finite Model Theory and Descriptive Complexity", chapter 3 of
  *Finite Model Theory and Its Applications*, Springer 2007). Version: author-hosted
  pdfTeX PDF dated 25 April 2007, running pages 125-230 (PDF page = running page - 124).
  Identity with the printed Springer text is not established; the reader text says so once.
- Pages read: 136 (Def. 3.1.9, 3.1.10, convenient encoding), 152-156 (3.3 opening,
  Def. 3.3.1, Thm 3.3.2 with proof, stages, Lemma 3.3.3, Prop. 3.3.4, dual operator,
  Ex. 3.3.5, Lemma 3.3.6, Def. 3.3.7, Ex. 3.3.8, gfp/lfp formula duality p. 156),
  157 (Thm 3.3.16 Immerman-Vardi, location only), 173-174 (LFP1, Thm 3.3.43),
  176 (Thm 3.3.51 and the infinite-structure failure remark), 177-180
  (3.3.9 PFP, Ex. 3.3.53, Prop. 3.3.54, Thm 3.3.55 with proof, Thm 3.3.56), 226 (refs [2], [67]).

## Writing decisions

- Source notation kept: bold lfp/gfp/pfp constructors, roman lfp(F), gfp(F), cl(F),
  F^d, X^alpha stages, R^m pfp stages, LFP1.
- Source proofs that are only paragraph arguments (Lemma 3.3.6, Prop. 3.3.54) or
  exercises (Ex. 3.3.5) are written out in full in the annex.
- Thm 3.3.55: the source uses a simultaneous pfp induction and relies on the
  unproved remark that S-PFP collapses to PFP (p. 178). The annex avoids that
  dependence by coding the symbol relations into one relation with min/max
  code tuples (structures of size at least 2) and treating one-element structures
  by a first-order disjunct. The position count is made consistent (positions
  0..n^k-1, end markers at both ends), where the source writes m = n^k.
- Machine model bridge: the handbook's PSPACE (def:p04-resource-classes) counts work
  space with a read-only input; the annex includes the two-track single-tape
  simulation.
- Thm 3.3.51 (Immerman normal form) and Thm 3.3.56 (Abiteboul-Vianu) are stated
  with cited= the chapter; the source gives no proof of either. The easy direction
  of 3.3.56 is proved (via the ordered corollary).

## Existing treatments found

- `handbook/parts/p04/complexity.tex` def:p04-fol-lfp (LFP operator definition),
  thm:p04-immerman-vardi (cited), def:p04-captures-complexity, def:p04-resource-classes.
- `handbook/parts/p09/presentations/n-c-004-03.tex` thm:p09-immerman1986-capture
  (proved ordered PTIME capture in Immerman's syntax) - not in the packet's list.
- `handbook/parts/p08/sources/src-025-501.tex` thm:p08-bvb501-mu-constructions
  (Knaster-Tarski for the modal mu-calculus) - not in the packet's list.
- `handbook/parts/p09/presentations/n-c-002.tex` (Libkin zero-one law for PFP; listed).

## Continuation

### Continuation (block 1, 2026-10-11)

- Written: body (561 lines) and annex (686 lines, 12 annexitems). unit-compile ok; check.py shows only the
  bib-key finding for Graedel2007FMTDC (own intake).
- Hypotheses made explicit in def:p03-w03-p03-059-good-encoding: (a) codes decidable and atoms/size
  computable in polynomial time, (b) codes computable from tables in polynomial time, (c) |code| >= |A|.
  The source uses these implicitly; its convenient encoding (p. 136) satisfies them.
- Remaining for MP-0: proof of Thm 3.3.51 (Immerman normal form; try Immerman 1986, Information and
  Control 68, Elsevier open archive, plus a stage-comparison source) and of the direction
  P = PSPACE => LFP = PFP on unordered finite structures (Abiteboul-Vianu; locate an open copy).
- Components ED26-SRC-050-0001/0002-*: readonly (owner w03-p03-054), not written here.

### Continuation (block 1 re-run, 2026-10-12)

- The assessment gaps (PFP syntax/semantics and results; operator development; normal-form and
  LFP-vs-PFP statements) were judged on the routed text (complexity.tex). The present body/annex
  files already carry them; they are not yet input by the drivers (placement in the return file).
- Re-verified every locator against the held PDF this session: pp. 136-137, 152-157, 173, 176-180.
- Added: PFP-in-PSPACE for formulas with free variables (body thm:...-pfp-pspace, annex last
  paragraph), matching the source's "every formula" wording (p. 178).
- Added to editable host handbook/parts/p04/complexity.tex (after def:p04-fol-lfp body) a forward
  link to sec:p03-w03-p03-059-fixed-point-logics; it resolves once the body file is input.
- Still open: proofs of Thm 3.3.51 (Immerman normal form) and of P = PSPACE => LFP = PFP on all
  finite structures (Thm 3.3.56 hard direction). The source gives neither proof; no proof source
  (Immerman 1986; Gurevich-Shelah 1986; Abiteboul-Vianu) was read.

### Continuation (block 2, 2026-10-12)

- Source read this session: held `source/references/acq-r1-ACQ-2026-10-0203/ACQ-2026-10-0203.pdf`
  (Immerman 1986, Information and Control 68, pp. 86-104; publisher version of record per
  held-sources.json). Read pp. 86-100 (text extraction), with page images checked for pp. 97-100.
  Locators used: Thm 2 pp. 87, 94; constant assumption p. 89; Lemma 4.1 pp. 95-96 (no-constant
  pair-tag variant p. 96); Lemma 4.2 p. 96; Cor 4.3 p. 97; rank, <=_phi, <_phi and Fact 4.4 p. 97;
  stage comparison equations, Claim, Lemma 4.5 p. 98 (finite-only remark pp. 97-98); Lemma 4.6
  pp. 98-99; Lemma 4.7 p. 99 with proof to p. 100; closing remark and infinite-structure remark p. 100.
  Graedel Thm 3.3.43 (simultaneous fixed points notation) p. 174 re-read.
- Written: thm:p03-w03-p03-059-immerman-normal-form now proved=annex (body lines 258-478; annex
  items pos-basic, stage-comparison, immerman-normal-form at annex lines 249-821). New body labels:
  def:...-simultaneous-lfp, thm:...-pos-basic, def:...-rank, thm:...-stage-comparison,
  def:...-non-reachability (example). Warning def:...-normal-form-boundary extended (where
  finiteness enters). Exact-sources paragraph and chapter opening updated.
- Proof organisation (decision): an auxiliary class Pos[sigma] (negation on literals only, nested
  simultaneous lfp with parameters). Item 1: induction on LFP formulas carrying chi+ and chi-;
  lfp/gfp steps use positive stage comparison for operators given by a pair (theta+, theta-) in
  which R may occur with both signs; this absorbs Immerman's Lemma 4.7 problem (his p. 100 remark).
  Item 2: parameter absorption (slices), Bekic principle for transitivity (Immerman 4.2 general
  form), pair-tag merge of simultaneous inductions (Immerman 4.1 no-constant variant; >= 2
  elements), one-element structures by unfolding, final case split. Stage comparison clauses are a
  variant of Immerman p. 98 (complement named by lt(z, .); second clause quantifies z with le(z,z));
  proved directly by the stage claim.
- Not claimed: Immerman's sharper single-application form (needs his constant assumption).
- Still open in 39.6: proof of the direction P = PSPACE => LFP = PFP on all finite structures
  (Graedel Thm 3.3.56, hard direction); no proof source read.
- Checks: unit-compile ok (overfull 22); check.py: only bib-key Graedel2007FMTDC (own intake);
  find_fused_spaces: no hits.

## Author proof audit and correction, 2026-10-26

Relation substitution is now explicitly capture-avoiding. Distinct inner
relation binders are alpha-renamed before substitution, and replacement
affects only occurrences free for the selected outer relation. The annex
proves the semantic renaming claim by structural induction, including
fixed-point stages. This is necessary in the greatest-fixed-point duality
and positive replacement arguments: substituting into a locally rebound
relation would change its operator and can violate its positivity condition.

The stage comparison, parameter absorption, simultaneous-system flattening,
pair-tag encoding and singleton boundary were reread. Immerman 1986 running
pages 97--100 were checked in the held publisher PDF, including rendered
pages 98 and 100 where text extraction obscures the formulas. The finite-only
boundary remains explicit. The ordered PFP/PSPACE simulation was reread as
an author proof audit, not reattributed to a newly acquired primary proof.
The hard unordered implication P = PSPACE implies LFP = PFP remains cited
only; it was not supplied by these corrections.

The scoped four-pass TeX Live build succeeded: 41 pages, 22 overfull warnings,
and three external references unresolved in the isolated unit. Canonical
citation alias changes were preserved when the correction was applied.

These are author corrections and bounded verification, not independent
review, source admission, complete-source coverage, or book completion.
