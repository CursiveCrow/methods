# Exact LJ cut elimination: completed authoring return

Date: 1 October 2026. This record concerns the assigned chapter and annex,
not independent admission of the chapter or completion of the historical
Gentzen presentations.

## Authored scope and files

The chapter proves elimination of both Cut and Mix for the actual
`handbook/registry/calculi/lj.tex`: finite-multiset antecedents, exactly one
succedent, uncontexted identity, explicit left weakening/contraction,
split-context implication left, the six displayed logical constructors,
defined negation, total capture-avoiding substitution and the stated
eigenvariable conditions. It includes no equality or nonlogical initial
sequents. The exact target sheet hash is
`A2D33FDC3103FFC3A2B3588150B8DC9E93A40031CCEB11E8C6D6AACF978F3FC7`.

Completed authoring artifacts:

- `handbook/parts/p07/intuitionistic-cut-elimination.tex`: 264 lines;
  SHA256 `C9693AF8BB74F7406AF1B40F1C595C855D07F5F3BDD68E91D6A2D65DA8F758D2`.
- `handbook/annex/p07/intuitionistic-cut-elimination.tex`: 657 lines;
  SHA256 `74187B20B77888F30674D890ADE963E1BFD9A07AF2EAFBCDFF4A01EB64AA9BF8`.
- `handbook/registry/symbols-intake-p07-intuitionistic-cut-elimination.csv`:
  11 notation records;
  SHA256 `468A5FA08B8AFC95E5D0DEE1044BD10ADBE3B1676891693BB1428A6B6B8FE784`.
- `handbook/bib/intake-p07-intuitionistic-cut-elimination.bib`: enriches the
  existing `Gentzen1935b` key; adds no new key;
  SHA256 `0B30D4FCC47685759B99DF1EB785FDCF2A64A5491AA8AB8F7EA39A9AE2EB32AA`.

The root integrator owns all driver insertion and canonical-record merges.
No driver, canonical bibliography, canonical notation, style or generated
file was changed by this assignment.

## Proof inventory and dependency order

Twelve complete body/annex pairs are written. Their common body prefix is
`thm:p07-lj-`; their corresponding annex prefix is `annex:p7.lj.`.

| Result suffix | Construction supplied |
| --- | --- |
| alpha-substitution | Bound-occurrence/free-variable invariance, common fresh representatives, simultaneous substitution congruence, temporary-variable and weak-quantifier composition identities, height-preserving substitution for every cut-free rule, fresh eigenparameters |
| context-collapse | Exact finite contractions of designated repeated supplied contexts, retaining all other occurrences |
| bottom-replacement | Every possible cut-free last-inference case for replacing a bottom succedent; no right weakening or Cut |
| marked-multicut | All initial, left commuting, right structural, right logical and principal/principal cases by formula-rank/height-sum induction |
| alpha-identity | Literal cut-free identities between alpha-equivalent formulas, covering all constructors and both directions |
| literal-realization | Every cut-free alpha-rule realized at arbitrary prescribed literal endsequent representatives |
| exact-cut-elimination | Original-tree recursion normalizes all Cut/Mix premises, then uses multicut and one final literal realization |
| analyticity | Every formula occurrence traced to the endsequent, with first-order instance and propositional literal distinctions |
| consistency | Last-inference impossibility for the empty-antecedent bottom sequent |
| disjunction-property | Empty-antecedent last-inference extraction; full height-induction counterargument for extracting a summand from an assumed disjunction |
| existence-property | Last-inference extraction of a term witness, grounding with an available ground term and a closed conclusion, and a no-ground-term signature counterexample |
| quantifier-free-conservativity | Analyticity excludes all quantified principal formulas, leaving exactly the quantifier-free rules and literal subformulas |

The selected-occurrence multicut allows unselected copies of the same formula
in either retained context. A selected contracted occurrence selects both
predecessors. A zero-selection call is derived weakening, not a new primitive
Mix rule. Residual same-rank occurrences are removed from the original right
premises before any lower-rank principal reductions. The implication reduction
keeps exactly one succedent in each intermediate proof. The two quantifier
principal cases substitute only after the relevant freshening/cleanup, and
any subsequent call on a manufactured proof has smaller formula rank.

Literal capture avoidance uses the first-order syntax chapter's fixed
least-fresh operation. The local height induction therefore operates on
alpha-classes. Literal alpha-identity and realization are proved independently
of multicut and used after normalization; they make no height-preservation
claim. No semantic completeness theorem is used to prove Cut admissibility.
Neither the classical empty-sequent consequence nor any classical interpolation,
midsequent or Herbrand theorem is imported into the LJ result.

## Sources read and historical boundary

The exact rule sheet, affected saved body and annex, the complete constructive
helper `spec/research/p07-intuitionistic-cut-construction.md`, the relevant
context/derivation and mix-measure declarations, and the first-order syntax,
alpha-equivalence, substitution and free-variable definitions were read.
The completed body and annex received a full author read-through, including
the constructor, quantifier, contraction, shared-context and split-context
cases. This is an author's check, not an independent review.

The original source is Gerhard Gentzen, *Untersuchungen über das logische
Schließen II*, *Mathematische Zeitschrift* 39 (1935), pp.405–431,
DOI [10.1007/BF01201363](https://doi.org/10.1007/BF01201363).
The held institutional source is the Göttingen Digitisation Centre article
[GDZPPN002375605](https://resolver.sub.uni-goettingen.de/purl?GDZPPN002375605),
in volume `PPN266833020_0039`, `LOG_0042`, preserved as 27 original TIFFs.
Its acquisition receipt is retained separately; the receipt's old temporary
paths do not change the matching hashes of the held `source/references` copies.

The author visually read the following exact original pages for the limited
historical attribution in this chapter:

- Part I p.177, Übersicht §2: announces the Hauptsatz for both classical and
  intuitionistic predicate logic and places its statement/proof in section III.
  Held image SHA256
  `48B1BB61A9CDC17C5AFE3BD2299FC09CEC157B9FF96481155B9F704C7B12C011`.
- Part I p.178, Übersicht §4: Part I contains sections I–III; Part II contains
  sections IV–V. Held image SHA256
  `94103239887996E56FBCC384668C24B16BB23478982B3268AFFEC674AB58CA2E`.
- Part II p.405, IV§1.1: consistency application using the empty sequent.
  Held image SHA256
  `1A1A39A3558D676FAC6A10B070D9D3F2D4A16A52CFF4BC0EF2ED22AC152B0E8B`.
- Part II p.407, IV§1.3: excluded-middle nonderivability and the general
  intuitionistic disjunction property in the parenthetical final paragraph.
  The argument explicitly considers right weakening with the empty sequent
  as premise. Held image SHA256
  `D0A0B92C691F535D361B1DEB5BB483629E05CE82C0122EF8CE2C03052D956A01`.

A source helper independently located the same boundaries. These pages verify
that the original presentation admits an empty succedent. The handbook's
exactly-one-succedent sheet has its own bottom-left rule and receives its own
complete proof in this chapter. The proof is an explicit mathematical
adaptation, not an assertion that the original source used this sheet or its
literal substitution convention.

The saved draft's attribution of the grade/height cut-reduction proof to
Part II was corrected directly to the actual consistency/disjunction
applications, with the exact IV§1.1/§1.3 citation. No claim is made to have read
the full historical Part I Hauptsatz proof or the full 27-page Part II article.
No original Gentzen source unit is closed by this authoring return. In
particular, the existence-property construction here is supplied by its
annex proof, not attributed to those Part II application pages.

Source-support files, unchanged by this assignment:

- `source/references/gentzen-1935-II/gentzen-II-acquisition-receipt.json`:
  SHA256 `1016EECD0B23EE969D6B4F8B3E6D2E5EC371AF9B4C204C61BCDB6D6A03DF8D12`.
- `source/references/gentzen-1935-II/PPN266833020_0039.mets.xml`:
  SHA256 `2FB163C0547EDD30B81529C00F6C477EE18291C4F91C4488BBA90AA7138B6345`.

## Integration return and verification status

All twelve `proved=` targets were checked against the actual reciprocal
`annexitem` labels/back-references. Both sides contain complete text and
ordinary proof wrappers. The two notation records whose first-use labels had
pointed to statements without the glyphs (`z` and `t_0`) now point to their
actual introducing annex items.

Ready for root integration: route the body/annex, merge the existing-key
bibliographic enrichment and 11 symbol records, and supply the exact local
scope bindings. The main theorem is `thm:p07-lj-exact-cut-elimination`, with
proof `annex:p7.lj.exact-cut-elimination`; analyticity is
`thm:p07-lj-analyticity`. The older shared cut-elimination chapter and calculus
comparison table still call the LJ component a sketch. Their updates belong
to the integrator, together with the classical author's separate result.

No mathematical component in this assigned exact-sheet treatment remains
unwritten. Its independent mathematical/source/publication reviews, global
integration validation, manuscript compilation and rendered-page inspection
are pending. No manuscript build, render, test suite or independent review
wave was run during this authoring block.
