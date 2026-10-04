# P3 research: model-theory migration and new content

Status: source-backed research note for the Phase-4 P3 visit. This file is an
inventory and evidence ledger, not handbook prose. It does not change the
registers, assign a row `done`, add bibliography or symbol records, or by
itself satisfy any treatment ceiling.

The migrated substrate is the frozen `v1.1-verified` revision of
`source/formal-logic-reference.tex`. All source line numbers in this note are
lines of that revision, not the audit-line coordinates retained in
`defects.csv`. External research was checked on 2026-08-10.

## Evidence policy and visit boundary

- **Source-verified** means the claim occurs in the frozen v1.1 source at the
  cited line range.
- **Externally verified** means the formulation or bibliographic metadata was
  checked against a primary publication, publisher page, author-hosted text,
  or an authoritative modern reference at the locator given.
- **Derived in the annex** means the result may receive `proved=` or
  `sketched=` only if the stated derivation is actually written in the P3
  annex. Research notes and citations do not constitute that derivation.
- **Claim ceiling** is the strongest wording licensed jointly by the register
  treatment (`E`, `T`, `S`, or `P`) and the located evidence.
- **Do not claim** records a tempting strengthening, a language-sensitive
  statement, or a result whose needed hypotheses were not verified.

The visit owns P3 body and annex material only. It must not silently repair or
rewrite the P2b Lindström or Robinson pointers; it should make the P3 entries
agree with them. Under `handbook/CONVENTIONS.md`, body results use exactly
`proved=annex:<id>`, `sketched=annex:<id>`, or `cited=<bibkey>`; proofs occur
only in `annex/`; and every `proved=`/`sketched=` target participates in the
bidirectional one-body-result/one-annex-item check.

The live cross-part contracts are in
`handbook/parts/p02/first-order-depth.tex`: the Robinson pointer is lines
289--295; the fixed definition of regular abstract logic is lines 313--328;
and the exact Lindström pointer statement/evidence is lines 404--413. These
are constraints on P3, not P3 deliverables that may be independently renamed.

The current P3 skeleton consists of `handbook/parts/p03.tex`, which inputs only
`parts/p03/model-theory.tex`, and `handbook/annex/p03.tex`, whose stub names
Łoś, back-and-forth, and the Tier-2 proof compressions. The implementation may
split the body/annex into chapter fragments, but the drivers must ultimately
input all fragments and the part driver must end with the generated P3 audit
table. The P5 pilot's operative pattern is one body result with an exact status
target for each `annexitem`, and `\sketchnote` inside every sketch listing the
specific missing steps.

### Live depth rows homed in P3

These are the exact live row fields from `spec/registers/depth-gaps.csv`:

| id | item | treatment | priority | effort | implementation consequence |
|---|---|---:|---:|---:|---|
| `D-P3-005` | Robinson joint consistency theorem | E | should | S | full entry; coordinate with the P2b pointer |
| `D-P4-001` | Ehrenfeucht--Fraïssé games with inexpressibility applications | E | must | M | full entry, theorem, and worked applications |
| `D-P4-002` | Preservation theorems (Łoś--Tarski; Chang--Łoś--Suszko) | E | should | M | full entry plus `A-042` |
| `D-P4-003` | Keisler--Shelah isomorphism theorem (statement) | S | should | S | exact cited statement only |
| `D-P4-004` | Compactness via ultraproducts drawn as a corollary of Łoś | S | should | S | statement plus the requested annex derivation |
| `D-P4-005` | Prime and atomic models with the omitting-types connection | E | must | M | definitions, exact countability hypotheses, theorem package |
| `D-P4-006` | Vaught two-cardinal theorem (statement) | S | could | S | explicit `\hbstub{D-P4-006: ...}`; do not fill in Phase 4 |
| `D-P4-007` | Indiscernibles and Ehrenfeucht--Mostowski models (statement level) | S | should | S | define order indiscernibles; cited theorem statement |
| `D-P4-008` | Stability, forking, and simplicity survey | S | should | M | survey ceiling; define every dividing-line term used |
| `D-P4-009` | NIP and o-minimality survey | S | should | M | survey ceiling; define both properties and give calibrated examples |
| `D-P4-010` | Finite model theory: 0--1 laws and Fagin's theorem | S | should | M | both statused statements; link to P9 only in prose |
| `D-P4-011` | Computable model theory pointer | P | could | S | explicit `\hbstub{D-P4-011: ...}`; do not fill in Phase 4 |
| `D-P4-012` | Lindström's theorem repositioned to model theory with abstract model theory context | S | should | S | cited restatement using the already fixed P2b notion of regular abstract logic |

The two `could` rows remain open after a correct Phase-4 visit. A stub is
honest accounting, not completion.

### Exact Phase-4 apparatus rows for P3

| id | priority / effort | exact required substance |
|---|---|---|
| `A-040` | must / L | First-order-theories master table: DLO, ACF, RCF, Presburger, PA, true arithmetic, and ZFC by completeness, decidability, QE, and categoricity spectrum. |
| `A-041` | must / M | QE catalog: per-theory QE status, eliminating extensions, definable Skolem functions/model completeness, and DLO/ACF/RCF witnesses. |
| `A-042` | must / S | Preservation table: Łoś--Tarski, Chang--Łoś--Suszko, and Lyndon, pairing syntax with preservation. |
| `A-043` | should / M | Stability/NIP/o-minimality overview with defining conditions and canonical examples. |
| `A-044` | should / S | Finite-model-theory table: zero--one laws, Fagin, Trakhtenbrot, and finite-versus-unrestricted contrast. |
| `A-122` | should / M | EF-game board for two small structures and a fixed-round Duplicator strategy. |
| `A-162` | must / S | Model-theory symbol subtable: elementary substructure/equivalence, Diag/ElDiag, type spaces, ultraproducts, and isomorphism notation. |

`A-162` is already represented in the live symbol registry; see the symbol
audit below. It still needs a rendered/placed subtable if that is the row's
deliverable.

## Frozen v1.1 Part IV: exhaustive source inventory

Part IV occupies lines 6049--7493. Its global assumptions at lines 6055--6059
are load-bearing: ambient Choice, single-sorted first-order signatures with
equality, and nonempty domains. The text notes that the map definitions extend
to many-sorted signatures by sort preservation. The evidence convention at
6061--6068 distinguishes complete proofs, proof sketches with named missing
verification, and cited theorems. Do not omit that evidence calibration during
compression.

There are 24 status-bearing results: 17 marked complete proof, one marked
proof sketch, and six marked cited theorem. The tables below include every
definition, status-bearing result, proof/proof-plan block, method, convention,
remark, warning, example, and exercise in the part. A blank label means the
source environment has no `\label`.

The exact structural map is: Part IV 6049--7493; Chapter “Maps,
Substructures, and Elementarity” 6052--6509, with sections beginning at 6070,
6138, 6243, 6332, and 6432; Chapter “Types, Saturation, and Ultraproducts”
6510--7149, with sections beginning at 6513, 6694, 6792, 6855, and 6942; and
Chapter “Quantifier Elimination and Categoricity” 7150--7493, with sections
beginning at 7153 and 7295.

### Chapter: Maps, Substructures, and Elementarity (6052--6509)

| kind | source lines | title / label | evidence or migration role |
|---|---:|---|---|
| convention | 6061--6068 | Status of results | defines the three source evidence classes |
| definition | 6076--6094 | Homomorphism | migrate exact constants/functions/relations clauses |
| definition | 6096--6107 | Embedding | relation reflection and injectivity are substantive |
| definition | 6109--6112 | Isomorphism and automorphism | isomorphism is a surjective embedding |
| lemma | 6114--6123 | Preservation of terms; `lem:term-preservation` | complete proof |
| proof | 6125--6130 | term induction | supports 6114--6123 |
| warning | 6132--6136 | untitled | homomorphisms need not preserve arbitrary formulas |
| definition | 6147--6157 | Substructure | migrate function/constant closure and relation restriction |
| example | 6168--6179 | A substructure that is not elementary | evidence against conflating substructure and elementary substructure |
| lemma | 6181--6192 | Isomorphism invariance of satisfaction; `lem:iso-invariance` | complete proof |
| proof | 6193--6208 | formula induction | supports 6181--6192 |
| lemma | 6210--6222 | Image of an embedding; `lem:embedding-image` | complete proof |
| proof | 6223--6241 | factorization through the image | supports 6210--6222; later reused by repaired model-completeness reduction |
| definition | 6246--6256 | Elementary map | exact parameter/formula clause |
| definition | 6258--6263 | Elementary substructure | uses the inclusion map |
| remark | 6265--6269 | untitled | relation among the map notions |
| theorem | 6271--6283 | Tarski--Vaught test; `thm:tarski-vaught` | complete proof |
| proof | 6289--6322 | induction using witnesses from the substructure | supports 6271--6283 |
| example | 6324--6330 | Applying the test | worked use of Tarski--Vaught |
| definition | 6336--6348 | Constants for parameters; `def:parameter-expansion` | fixes the expanded language and structure |
| definition | 6350--6366 | Atomic and elementary diagrams; `def:diagrams` | keep Diag and ElDiag distinct |
| theorem | 6368--6381 | Diagram tests for embeddings; `thm:diagram-tests` | complete proof |
| proof | 6383--6408 | constant interpretation gives the required map | supports 6368--6381 |
| example | 6413--6420 | The two diagrams make different tests | embedding versus elementary embedding |
| exercise | 6422--6430 | `ex:maps-elementarity-01` | diagram application |
| definition | 6435--6442 | Elementary chain | linearly ordered elementary inclusions |
| theorem | 6444--6450 | Elementary chain theorem; `thm:elementary-chain` | complete proof |
| proof | 6452--6485 | union structure plus formula induction/Tarski--Vaught | supports 6444--6450 |
| warning | 6487--6492 | A frequent chain error | union domains alone do not supply coherent interpretations |
| exercise | 6494--6500 | `ex:maps-elementarity-02` | elementary-chain application |
| exercise | 6502--6508 | `ex:maps-elementarity-03` | map/chain application |

### Chapter: Types, Saturation, and Ultraproducts (6510--7149)

| kind | source lines | title / label | evidence or migration role |
|---|---:|---|---|
| definition | 6520--6537 | Type | consistency/realizability context and parameter language are substantive |
| definition | 6539--6562 | Types over a theory and type spaces; `def:type-space` | includes complete types and Stone topology |
| theorem | 6564--6570 | Compactness of type spaces; `thm:type-space-compact` | complete proof; repaired by `R-028` |
| proof | 6572--6616 | finite-intersection argument plus completion to a complete type | supports 6564--6570; retain lines 6603--6612 in substance |
| example | 6618--6628 | A finite type space | concrete topology/example |
| exercise | 6630--6638 | `ex:types-ultraproducts-01` | type-space application |
| definition | 6640--6645 | Realization | tuple realizes a type over parameters |
| example | 6647--6659 | A finitely satisfiable type not realized | separates finite satisfiability from realization |
| definition | 6661--6670 | Saturation | cardinal parameter and size bound must survive |
| remark | 6672--6677 | untitled | saturation convention/context |
| theorem | 6679--6686 | Existence of saturated elementary extensions; `thm:saturated-extension` | cited theorem; no annex item |
| definition | 6698--6709 | Homogeneity; `def:homogeneity` | parameter/domain size conditions are substantive |
| theorem | 6711--6716 | Saturation supplies homogeneity; `thm:saturation-homogeneity` | complete proof; repaired by `R-029` |
| proof | 6718--6769 | extension of a partial elementary map | supports 6711--6716; explicit compactness step at 6731--6756 |
| example | 6773--6781 | What homogeneity adds | contrasts realization with automorphic transport |
| exercise | 6783--6790 | `ex:types-ultraproducts-02` | homogeneity application |
| definition | 6796--6813 | Principal and nonprincipal types; `def:principal-type` | terminology must coordinate with “isolated” in new prime-model entry |
| theorem | 6815--6822 | Omitting types theorem; `thm:omitting-types` | cited theorem; countable-language and nonprincipality hypotheses are load-bearing |
| example | 6831--6844 | A type that a countable model omits | concrete omitted type |
| exercise | 6846--6853 | `ex:types-ultraproducts-03` | omitting-types application |
| definition | 6858--6872 | Filter | proper filter and ultrafilter clauses |
| lemma | 6878--6892 | Existence of nonprincipal ultrafilters; `lem:nonprincipal-ultrafilter` | complete proof; repaired by `R-036` |
| proof | 6894--6940 | Fréchet filter, application of the assumed Ultrafilter Lemma, finite-set induction, nonprincipality | supports 6878--6892 |
| definition | 6960--6976 | Ultraproduct | equivalence relation and quotient interpretations |
| lemma | 6978--6983 | unnamed well-definedness lemma | complete proof |
| proof | 6985--6992 | representatives do not affect functions/relations | supports 6978--6983 |
| lemma | 6994--7009 | Term evaluation in an ultraproduct; `lem:los-terms` | complete proof |
| proof | 7011--7017 | induction on terms | supports 6994--7009 |
| theorem | 7019--7035 | Łoś's theorem; `thm:los` | complete proof; **Tier-1 method result** |
| proof | 7039--7105 | formula induction, including existential witness choice | supports 7019--7035; **Tier-1 annex source** |
| corollary | 7107--7112 | Diagonal elementary embedding; `cor:diagonal-ultrapower` | complete proof |
| proof | 7114--7118 | immediate Łoś application to constant functions | supports 7107--7112 |
| example | 7120--7127 | An infinite ultraproduct of finite structures | compactness-style application |
| warning | 7129--7133 | First-order scope | Łoś is first-order; preserve this boundary |
| exercise | 7135--7141 | `ex:types-ultraproducts-04` | ultraproduct application |
| exercise | 7143--7148 | `ex:types-ultraproducts-05` | ultraproduct application |

### Chapter: Quantifier Elimination and Categoricity (7150--7493)

| kind | source lines | title / label | evidence or migration role |
|---|---:|---|---|
| definition | 7156--7166 | Quantifier elimination | theory-relative equivalence to quantifier-free formulas |
| method | 7168--7175 | One-quantifier reduction | migrate as a method box, not as a statused theorem |
| theorem | 7177--7183 | Dense linear orders; `thm:dlo-qe` | cited theorem; no annex item |
| remark | 7185--7197 | Construction underlying the cited theorem | finite-order-type analysis, not a supplied proof |
| example | 7199--7207 | Eliminating one quantifier in DLO | worked witness |
| definition | 7209--7229 | Deductive completeness, semantic completeness, and model completeness; `def:theory-completeness` | preserve three distinct notions; repaired context for `R-015` |
| lemma | 7231--7238 | Reduction to substructure inclusions; `lem:model-completeness-reduction` | complete proof; repair `R-015` |
| proof | 7239--7259 | factor arbitrary embeddings through their images | supports 7231--7238 |
| corollary | 7261--7265 | unnamed QE-to-model-completeness corollary | proof sketch, not complete |
| proof plan | 7267--7284 | missing verification identified | this is the sole source sketch; preserve omissions if migrated |
| theorem | 7286--7291 | Algebraically closed fields | cited theorem; explicitly `ACF_p` in the ring language |
| definition | 7298--7303 | Categoricity | cardinal-specific definition |
| warning | 7305--7316 | untitled | first-order categoricity limitations/context |
| definition | 7318--7322 | Finite partial isomorphism | domain/range induced finite structures |
| method | 7324--7335 | Back-and-forth; `method:back-and-forth` | **Tier-1 method entry** |
| theorem | 7337--7352 | Back-and-forth test; `thm:back-and-forth-test` | complete proof; repaired by `R-016`; **Tier-1 method result** |
| proof | 7354--7369 | alternating extension enumeration | supports 7337--7352; **Tier-1 annex source** |
| corollary | 7373--7379 | Countable saturated structures | complete proof |
| proof | 7381--7400 | constructs extension families using saturation | supports 7373--7379 |
| theorem | 7402--7407 | Countable categoricity of dense linear order; `thm:dlo-countable-categorical` | complete proof |
| proof | 7409--7425 | back-and-forth application | supports 7402--7407; application, not the Tier-1 core |
| example | 7427--7435 | Uncountable categoricity of algebraically closed fields | characteristic and transcendence-degree hypotheses matter |
| theorem | 7437--7449 | Ryll--Nardzewski | cited theorem; no annex item |
| theorem | 7453--7458 | Morley's categoricity theorem | cited theorem; no annex item |
| warning | 7462--7467 | Completeness versus categoricity | do not conflate syntactic completeness and cardinal categoricity |
| exercise | 7469--7473 | `ex:qe-categoricity-01` | QE application |
| exercise | 7475--7480 | `ex:qe-categoricity-02` | categoricity application |
| exercise | 7482--7492 | `ex:qe-categoricity-03` | categoricity application |

### Evidence-preserving annex plan

The two named Tier-1 methods are unambiguous:

1. **Łoś:** body `hbmethod` from 7019--7035 and a statused theorem backed by a
   full annex proof compressed from 7039--7105. The induction must still cover
   atomic formulas, Boolean connectives, and quantifiers; the existential step
   must state both witness directions and where choice of representatives is
   used. If those pieces are omitted, the status must be `sketched=`, not
   `proved=`.
2. **Back-and-forth:** body `hbmethod` from 7324--7335 and the exact test from
   7337--7352, backed by 7354--7369. The conclusion must say that **every
   initial finite partial isomorphism in the family extends to the resulting
   isomorphism**. That clause is the `R-016` repair.

All six cited theorems remain `cited=` unless a genuinely complete independent
proof is supplied: saturated extensions, omitting types, DLO QE, ACF\(_p\) QE,
Ryll--Nardzewski, and Morley. The QE-to-model-completeness corollary remains a
sketch if migrated with only the source proof plan. Other source-complete
results may have compressed annex proofs only if every substantive step still
appears; compression percentage is not permission to upgrade or hollow out a
proof.

Thus the non-Tier-1 complete-proof inventory (the candidate Tier-2 annex
pool) is exactly: term preservation; isomorphism invariance; image of an
embedding; Tarski--Vaught; diagram tests; elementary chains; compactness of
type spaces; saturation supplies homogeneity; nonprincipal-ultrafilter
existence; ultraproduct well-definedness; ultraproduct term evaluation;
diagonal elementary embedding; model-completeness reduction; the countable-
saturated-structures corollary; and countable categoricity of DLO. If a body
result from this list is retained as `proved=`, it needs its own annex item;
otherwise cite, downgrade, or deliberately retire it with an accounting note.

## Repair trace: Phase-2 changes that must survive

The `defects.csv` coordinates below are audit coordinates at `v1.0-audit`;
the v1.1 coordinates are the authoritative migration locators.

| repair | original defect | v1.1 locus | exact preservation obligation |
|---|---|---|---|
| `R-015` | model completeness quantified over arbitrary embeddings while the old proof handled inclusions only | definition 7209--7229; reduction lemma 7231--7238; proof 7239--7259 | Factor an arbitrary embedding through its image, use that the image is a substructure, and transport elementarity back through the isomorphism. Do not restate the criterion only for literal inclusions while retaining the broader definition. |
| `R-016` | the back-and-forth corollary used extension of the original map although the theorem statement only promised some isomorphism | method 7324--7335; theorem 7337--7352; proof 7354--7369 | The theorem conclusion at 7348--7350 says each starting map extends to an isomorphism. Retain that clause in both the body statement and annex construction. |
| `R-028` | compactness of type spaces omitted completion of a consistent partial type to a complete type | theorem 6564--6570; proof 6572--6616, especially 6603--6612 | After compactness supplies consistency, explicitly extend the partial type to a complete type (the Lindenbaum/maximal-consistent step) before identifying a point of `S_n(T)`. |
| `R-029` | saturation-implies-homogeneity silently invoked compactness | theorem 6711--6716; proof 6718--6769, especially 6731--6756 | Display finite satisfiability of the extension type, invoke compactness, then use saturation at the correct cardinal bound. Do not jump directly from a partial map to a realizing element. |
| `R-036` | nonprincipal-ultrafilter existence was unlabeled prose with an unexecuted induction | lemma 6878--6892; proof 6894--6940 | Keep the labeled statused lemma, invoke the explicitly assumed Ultrafilter Lemma for extension, and preserve the finite-set induction and nonprincipality argument; otherwise downgrade or cite the whole result. Ambient Choice was declared at 6055. |

Execution notes record that `R-015` and `R-016` were rechecked against the
exact string-valued definitions and Part-IV maps and needed no further edit.
That verification is not a license to paraphrase away their repaired clauses.

## New depth research and calibrated entry specifications

### `D-P3-005` — Robinson joint consistency (E)

Let (L_0=L_1\cap L_2), and let (T_i) be consistent (L_i)-theories.
The full entry may use either of the following equivalent presentations, but
must state which one it uses:

1. if there is no (L_0)-sentence \(\sigma\) such that
   (T_1\vdash\sigma) and (T_2\vdash\neg\sigma), then
   (T_1\cup T_2) is consistent; or
2. if (T_1) and (T_2) both extend one complete (L_0)-theory, then their
   union is consistent.

The P2b pointer already requires a fixed common signature and exactly this
choice between a complete-common-theory formulation and a no-separating-
sentence formulation. Reuse it. The source is Abraham Robinson, “A Result on
Consistency and its Application to the Theory of Definition,” *Proceedings of
the Koninklijke Nederlandse Akademie van Wetenschappen, Series A* 59 (1956),
47--58, [DOI 10.1016/S1385-7258(56)50008-X](https://doi.org/10.1016/S1385-7258(56)50008-X),
already keyed `RobinsonJointConsistency1956`.

**Claim ceiling:** full definitions/context and exact cited theorem statement,
`cited=RobinsonJointConsistency1956`. An E treatment does not require an annex
proof.

**Do not claim:** agreement merely on the intersection (T_1\cap T_2) is not
the separating-sentence hypothesis. Do not omit consistency of each (T_i),
the common sublanguage, or the distinction between theorem consistency and
model-theoretic amalgamation over a specified common structure.

### `D-P4-001` — Ehrenfeucht--Fraïssé games (E) and `A-122`

Fix two structures (\mathcal A,\mathcal B) in the same finite relational
signature.
In the (k)-round game, each round consists of Spoiler choosing an element in
one structure and Duplicator choosing an element in the other. After (k)
rounds, Duplicator wins exactly when the pairing of chosen elements is a
partial isomorphism. Define quantifier rank recursively before stating the
theorem.

**Externally verified theorem.** For structures in the same fixed finite
relational vocabulary,

\[
  \mathcal A\equiv_k\mathcal B
  \quad\Longleftrightarrow\quad
  \text{Duplicator has a winning strategy in the (k)-round EF game},
\]

where (\equiv_k) means agreement on first-order sentences of quantifier rank
at most (k). Leonid Libkin, *Elements of Finite Model Theory* (Springer,
2004), [DOI 10.1007/978-3-662-07003-1](https://doi.org/10.1007/978-3-662-07003-1),
Chapter 3, gives the game at pp. 24--25 (Definition 3.5 for partial
isomorphism), quantifier rank at p. 31 (Definition 3.8), and the theorem at
p. 31 (Theorem 3.9), followed by the inexpressibility criteria (Corollaries
3.10--3.11). The author-hosted text is
[available here](https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf). The
primary game source already keyed `Ehrenfeucht1961` is Andrzej Ehrenfeucht,
“An Application of Games to the Completeness Problem for Formalized
Theories,” *Fundamenta Mathematicae* 49 (1961), 129--141,
[DOI 10.4064/fm-49-2-129-141](https://doi.org/10.4064/fm-49-2-129-141).
`Fraisse1954` is also already present for the precursor back-and-forth
characterization.

**Inexpressibility pattern:** to show that no first-order sentence defines a
property (P), for every (k) produce (\mathcal A_k\in P) and
(\mathcal B_k\notin P) on which Duplicator wins (k) rounds. Libkin's
Corollary 3.12 applies this to parity/even cardinality over finite linear
orders; the family uses orders of sizes (2^k) and (2^k+1). A second safe
application is nondefinability of graph connectivity over finite graphs,
provided the chosen pair and Duplicator invariant are actually supplied or a
source is cited.

**Claim ceiling:** full E entry with game definition, quantifier rank, EF
theorem, the general inexpressibility criterion, and at least one fully
explained application. The theorem should be cited, not presented as proved by
an informal picture.

**`A-122` design:** use a genuinely small illustration, for example a two-
round position on 3- and 4-element linear orders. Label each selected pair and
show that the partial order type is preserved after each response. State
prominently that this one board illustrates a fixed-round strategy; it does
not prove the parity result, which requires a family indexed by (k).

**Do not claim:** agreement through rank (k) is not elementary equivalence.
Do not use the relational-signature formulation unchanged for function
symbols without explaining relationalization/partial substructure closure, or
silently drop the finite-vocabulary hypothesis used by the selected source.

### `D-P4-002` — preservation theorems (E) and `A-042`

The entry and table must distinguish four semantic operations and their
different syntactic fragments.

| theorem | semantic condition over all structures | exact syntactic conclusion | safe source locator |
|---|---|---|---|
| Łoś--Tarski, substructure form | an elementary class is closed under substructures | it is axiomatizable by universal sentences | Martin Speirs, notes from Thomas Scanlon's *Math 225A Model Theory* course, §20.2, Theorem 20.1, [course notes](https://math.berkeley.edu/~scanlon/mn13.pdf); also Chang--Keisler, 3rd ed. |
| Łoś--Tarski, extension dual | a sentence is preserved under extensions | it is equivalent to an existential sentence | same references; make clear this is the sentence-level dual |
| Chang--Łoś--Suszko | an elementary class is closed under unions of chains | it has a universal--existential (`∀*∃*`) axiomatization | Benno van den Berg, *Model Theory* notes, §2, Definitions 2.3--2.4 and Theorem 2.5, [UvA notes](https://staff.fnwi.uva.nl/b.vandenberg3/Onderwijs/Model_theory_2015/modeltheory_notes.pdf); Paul Bankston, “The Chang--Łoś--Suszko theorem in a topological setting,” *Archive for Mathematical Logic* 45(1) (2006), 97--112, [DOI 10.1007/s00153-004-0238-y](https://doi.org/10.1007/s00153-004-0238-y) for an authoritative restatement |
| Lyndon positivity | a first-order formula is preserved under surjective homomorphisms | it is equivalent to a positive formula | Roger C. Lyndon, “Properties Preserved under Homomorphism,” *Pacific Journal of Mathematics* 9 (1959), 143--154, [DOI 10.2140/pjm.1959.9.143](https://doi.org/10.2140/pjm.1959.9.143); modern statement in Benjamin Rossman, *Homomorphism Preservation Theorems*, Theorem 1.2, [author-hosted paper](https://www.math.toronto.edu/rossman/hpt-jacm.pdf) |
| homomorphism preservation (separate optional row) | a formula is preserved under arbitrary homomorphisms | it is equivalent to an existential-positive formula | Rossman, Theorem 1.1, same locator |

Define **positive formula** at the table: built from atomic formulas using
(\land,\lor,\forall,\exists), without negated relation atoms (equality
conventions must follow the selected reference). Define **existential-positive**
separately. This prevents the common but false merger of Lyndon's positivity
theorem with the homomorphism-preservation theorem.

**Claim ceiling:** full E entry with exact definitions of preservation under
substructures, extensions, chain unions, and the chosen homomorphism notion;
status each theorem `cited=`. The source Part IV elementary-chain theorem may
be used to explain why chain unions are natural, but it does not prove the
converse preservation theorem.

**Do not claim:** the Łoś--Tarski substructure theorem fails when restricted
to finite structures, so every row must say “over all structures.” Do not
state the theory form when only a sentence form has been sourced. Do not
replace “unions of chains” by arbitrary unions. Do not label arbitrary-
homomorphism preservation “Lyndon” without the distinct existential-positive
conclusion.

### `D-P4-003` — Keisler--Shelah isomorphism theorem (S)

For structures (\mathcal M,\mathcal N) in the same signature,

\[
  \mathcal M\equiv\mathcal N
  \quad\Longleftrightarrow\quad
  \text{some ultrapowers of (\mathcal M) and (\mathcal N) are isomorphic}.
\]

The forward implication is Shelah's theorem. The reverse implication follows
from Łoś plus isomorphism invariance. The primary source is Saharon Shelah,
“Every Two Elementarily Equivalent Models Have Isomorphic Ultrapowers,”
*Israel Journal of Mathematics* 10(2) (1971), 224--233,
[DOI 10.1007/BF02771574](https://doi.org/10.1007/BF02771574). The Hebrew
University publication record confirms volume, issue, pages, date, DOI, and
the no-GCH abstract:
[institutional record](https://cris.huji.ac.il/en/publications/every-two-elementarily-equivalent-models-have-isomorphic-ultrapow/).

**Claim ceiling:** one exact cited statement, `cited=Shelah1971Ultrapowers`,
plus the one-sentence reverse implication. No proof of the forward implication
at S treatment.

**Do not claim:** the theorem does not say that a fixed nonprincipal
ultrafilter on (\omega) works for every pair. Do not fix the index set,
ultrafilter, or cardinal bounds unless the stronger version is separately
sourced. Do not replace “some ultrapowers” with “the structures are
isomorphic.”

### `D-P4-004` — compactness via ultraproducts (S with annex derivation)

Let (\Gamma) be finitely satisfiable and let (I) be the set of finite
subsets of (\Gamma). For each (\Delta\in I), choose
(\mathcal M_\Delta\models\Delta). For each (\sigma\in\Gamma), put

\[
 I_\sigma=\{\Delta\in I: \sigma\in\Delta\}.
\]

The family (\{I_\sigma:\sigma\in\Gamma\}) has the finite-intersection
property, so its generated proper filter extends to an ultrafilter
(\mathcal U). Łoś then gives
(\prod_{\Delta\in I}\mathcal M_\Delta/\mathcal U\models\Gamma).
Brent Cody's *The Compactness Theorem* notes, §6, pp. 15--16, give this
construction explicitly:
[author-hosted notes](https://brentcody.github.io/syllabi/compactness_notes_4-8-2014.pdf).
Chang and Keisler, *Model Theory*, 3rd ed. (North-Holland, 1990), is the
existing authoritative book reference.

**Claim ceiling:** the body statement can say that first-order compactness is
derived from Łoś relative to the ultrafilter-extension principle. The requested
annex item must display the index family, finite-intersection argument,
ultrafilter extension, and Łoś step. If any of those are merely named, use
`sketched=` and enumerate them in `\sketchnote`; use `proved=` only if the
derivation is complete at the declared ambient Choice assumptions.

**Do not claim:** this is choice-free compactness. Part IV explicitly assumes
Choice, and the proof invokes ultrafilter extension. Do not use a bare
nonprincipal ultrafilter on (\mathbb N); the correct index set is built from
finite subsets of (\Gamma).

### `D-P4-005` — prime and atomic models, OTT, and Ryll--Nardzewski (E)

Fix a complete theory (T) in a countable language.

- A complete type (p\in S_n(T)) is **isolated** (the source's “principal”)
  if some formula (\theta(\bar x)\in p) entails every formula of (p)
  modulo (T).
- A model (M\models T) is **atomic** if every finite tuple from (M)
  realizes an isolated complete type over the empty set.
- A model (M\models T) is **prime** if it elementarily embeds into every
  model of (T).

For countable (M\models T), (M) is prime iff it is atomic. The
prime-to-atomic direction uses the omitting-types theorem; the atomic-to-prime
direction constructs an elementary embedding by enumerating the countable
model and realizing isolating formulas. Moreover, (T) has a prime model iff
isolated types are dense in every (S_n(T)). These countability and
completeness assumptions must remain visible.

Source locators:

- David Marker, *Model Theory: An Introduction* (Springer, 2002),
  [DOI 10.1007/b98860](https://doi.org/10.1007/b98860), §4.2,
  pp. 125--137 (omitting types, atomic and prime models), and §4.4,
  pp. 155--158 (Ryll--Nardzewski/countable models). Existing key
  `Marker2002`.
- Martin Speirs, notes from Thomas Scanlon's *Math 225A Model Theory* course,
  §24.2, pp. 127--129,
  [course notes](https://math.berkeley.edu/~scanlon/225af13lectures/ModelTheoryNotes.pdf),
  for the atomic/prime package.
- Martin Bays, *Logik II: Model Theory*, Theorem 8.30,
  [author-hosted notes](https://people.maths.ox.ac.uk/bays/logikII/latest/logikII-17-en.pdf),
  for the Ryll--Nardzewski equivalences.

The existing source theorem at 7437--7449 can be restated next to this entry:
for countable complete (T) with infinite models, (\aleph_0)-categoricity
is equivalent to finiteness of (S_n(T)) for each (n), equivalently every
complete (n)-type is isolated. Consequently, the unique countable model is
both prime and saturated. Keep the theorem cited under the existing
`RyllNardzewski1959`, `Engeler1959`, and `Svenonius1959` references.

**Claim ceiling:** full E entry with definitions, the countable prime/atomic
equivalence, the OTT connection, the prime-model existence criterion, and the
Ryll--Nardzewski consequence. These are cited results unless complete annex
proofs are actually supplied.

**Do not claim:** an arbitrary atomic model is prime. Countability is essential
to the displayed equivalence. Do not call a type isolated merely because one
of its formulas is consistent. Do not infer saturation from primeness outside
the (\aleph_0)-categorical setting.

### `D-P4-007` — indiscernibles and Ehrenfeucht--Mostowski models (S)

A linearly ordered sequence ((a_i)_{i\in I}) is a sequence of **order
indiscernibles** in (M) if for every (n), all increasing (n)-tuples of
indices determine tuples with the same complete type over the chosen parameter
set (empty unless explicitly stated).

**Externally verified statement:** if (T) has infinite models and
((I,<)) is a linear order, then (T) has a model containing a sequence of
order indiscernibles indexed in order type (I). The primary source is
Andrzej Ehrenfeucht and Andrzej Mostowski, “Models of Axiomatic Theories
Admitting Automorphisms,” *Fundamenta Mathematicae* 43 (1956), 50--68,
[DOI 10.4064/fm-43-1-50-68](https://doi.org/10.4064/fm-43-1-50-68).
Marker, *Model Theory*, §5.2, pp. 178--185 is the modern locator. George
McNulty's model-theory notes give the statement in a directly checkable form:
[author-hosted notes](https://people.math.sc.edu/mcnulty/762/modeltheory.pdf).

**Claim ceiling:** define order indiscernibility and give a cited statement,
`cited=EhrenfeuchtMostowski1956`, with one sentence identifying compactness/
Ramsey as the construction ingredients. Do not supply an ersatz proof at S
treatment.

**Do not claim:** the resulting model is generated as a Skolem hull by the
indiscernibles, or that a coherent EM blueprint has been constructed, unless
Skolemization and the blueprint theorem are actually stated. “Contains
indiscernibles indexed by (I)” is the supported ceiling here.

### `D-P4-008` — stability, dividing/forking, and simplicity (S)

The survey needs a minimal definitional chain; merely listing field names does
not meet S treatment.

1. A formula (\varphi(x;y)) has the **order property** in (T) if in some
   model there are tuples ((a_i),(b_j)) such that
   (\varphi(a_i;b_j)) holds exactly when (i<j). A complete theory is
   **stable** iff no formula has the order property.
2. A formula (\varphi(x;b)) **divides over** (A) if there is an
   (A)-indiscernible sequence ((b_i)_{i<\omega}) with (b_0=b) such that
   (\{\varphi(x;b_i):i<\omega\}) is inconsistent.
3. A formula **forks over** (A) if it entails a finite disjunction of
   formulas that divide over (A). A complete type forks when it contains a
   forking formula.
4. At survey ceiling, define a theory as **simple** by the local-character
   condition for forking, with an explicit cardinal bound: for each complete
   type (p(x)) over (B), some (A\subseteq B) with
   (|A|\le |T|+|x|) is a nonforking base (hence (|A|\le |T|) for a
   finite tuple in the usual infinite-cardinal convention). Say which
   equivalent definition the cited source uses.

Safe orientation facts are: stable theories are simple; the random graph is
simple but unstable; and in simple theories forking supplies the standard
symmetry/transitivity independence calculus. Sources:

- Saharon Shelah, “Stability, the f.c.p., and Superstability; Model Theoretic
  Properties of Formulas in First Order Theory,” *Annals of Mathematical
  Logic* 3(3) (1971), 271--362,
  [DOI 10.1016/0003-4843(71)90015-5](https://doi.org/10.1016/0003-4843(71)90015-5),
  with metadata and published text on the
  [author's publication page](https://shelah.logic.at/papers/10/).
- Katrin Tent and Martin Ziegler, *A Course in Model Theory* (Cambridge
  University Press, 2012),
  [DOI 10.1017/CBO9781139015417](https://doi.org/10.1017/CBO9781139015417),
  Chapter 7, pp. 99--128 (simple theories), and Chapter 8, pp. 129--156
  (stable theories).
- Byunghan Kim, “Forking in Simple Unstable Theories,” *Journal of the London
  Mathematical Society* 57(2) (1998), 257--267,
  [DOI 10.1112/S0024610798005985](https://doi.org/10.1112/S0024610798005985),
  for forking equals dividing and the simple-theory calculus.

**Claim ceiling:** one survey entry and `A-043`; definitions plus a small
implication/example map. Use citations rather than theorem-proof status claims
for the research-level facts.

**Do not claim:** forking equals dividing in every theory, or that every
unstable theory is nonsimple. Do not introduce ranks, canonical bases, or the
full independence theorem at this ceiling. Do not use “stable” to mean merely
“few models” without fixing the cardinal/type-count formulation and its
hypotheses.

### `D-P4-009` — NIP and o-minimality (S)

For a formula (\varphi(x;y)), the family
(\{\varphi(M;b):b\in M^{|y|}\}) **shatters** a finite set (A\subseteq
M^{|x|}) if every subset of (A) is its trace for some parameter (b).
The formula is **NIP** if it does not shatter arbitrarily large finite sets;
a complete theory is NIP if every formula is NIP.

An expansion (M) of a dense linear order is **o-minimal** if every
parameter-definable subset of its domain is a finite union of points and
intervals (allowing unbounded endpoints). Safe orientation facts:

- stable theories are NIP;
- o-minimal theories are NIP;
- DLO is o-minimal and NIP but unstable;
- the random graph has the independence property;
- a theory that is both simple and NIP is stable;
- real closed fields are o-minimal (and have QE in the ordered-ring language).

Sources:

- Pierre Simon, *A Guide to NIP Theories* (Cambridge University Press, 2015),
  Lecture Notes in Logic 44,
  [DOI 10.1017/CBO9781107415133](https://doi.org/10.1017/CBO9781107415133),
  Chapter 2, especially Definitions 2.1 and 2.10; the publisher-hosted
  [excerpt](https://assets.cambridge.org/97811070/57753/excerpt/9781107057753_excerpt.pdf)
  contains the definitions and examples.
- Lou van den Dries, *Tame Topology and O-minimal Structures* (Cambridge
  University Press, 1998), LMS Lecture Note Series 248,
  [DOI 10.1017/CBO9780511525919](https://doi.org/10.1017/CBO9780511525919),
  Introduction and Chapter 1 for the definition; Chapter 5 for the VC/NIP
  property.
- Anand Pillay and Charles Steinhorn, “Definable Sets in Ordered Structures.
  I,” *Transactions of the American Mathematical Society* 295(2) (1986),
  565--592,
  [DOI 10.1090/S0002-9947-1986-0833697-X](https://doi.org/10.1090/S0002-9947-1986-0833697-X),
  for the foundational o-minimal theory.

**Claim ceiling:** S survey plus `A-043`; exact definitions, implications, and
canonical examples. No proofs are required or licensed by the ceiling.

**Do not claim:** NIP is the same as stability; all NIP theories are
o-minimal; or o-minimal theories are stable. Keep formula-level IP/NIP distinct
from theory-level NIP. Do not omit “with parameters” from o-minimality.

### `D-P4-010` — finite model theory: zero--one law and Fagin (S)

Fix a finite purely relational signature (\sigma), with no constant or
function symbols. Put the uniform distribution on labeled (\sigma)-structures
with universe ([n]=\{0,\ldots,n-1\}). For every first-order (\sigma)-sentence
(\varphi),

\[
 \lim_{n\to\infty}\Pr[\mathcal A_n\models\varphi]\in\{0,1\}.
\]

This is the first-order zero--one law of Glebskiĭ--Kogan--Liogon'kiĭ--Talanov
and independently Fagin. Libkin, *Elements of Finite Model Theory*, Chapter
12, pp. 235--248, gives the probability space (beginning p. 235), Definition
12.1, and the first-order law as Corollary 12.3. Existing keys are
`GlebskiiEtAl1969` and `Fagin1976`. Fagin's primary paper is “Probabilities on
Finite Models,” *The Journal of Symbolic Logic* 41(1) (1976), 50--58,
[DOI 10.2307/2272945](https://doi.org/10.2307/2272945).

**Fagin's theorem:** over finite relational structures, an isomorphism-closed
property is in NP iff it is definable by an existential second-order sentence.
Libkin states this as Theorem 9.6 after fixing finite-structure encoding in
Chapter 9. The primary source is Ronald Fagin, “Generalized First-Order
Spectra and Polynomial-Time Recognizable Sets,” *Complexity of Computation*,
SIAM--AMS Proceedings 7 (1974), 43--73, existing key `Fagin1974`.

The table should place these beside Trakhtenbrot's theorem already cited in
the source: for every finite relational signature containing a binary relation,
finite satisfiability is computably enumerable but undecidable, while the set
of finite validities is not computably enumerable. The existing v1.1 statement
is at 8290--8298 and key `Trakhtenbrot1950`.

**Finite/unrestricted contrast for `A-044`:** unrestricted first-order
validity is computably enumerable by completeness; finite validity is not.
Compactness holds over arbitrary structures and fails over finite structures.
The zero--one law is asymptotic and does not decide finite validity.

**Claim ceiling:** two separately statused cited statements (zero--one and
Fagin) plus the comparison table. The row explicitly names both; supplying
only the zero--one law is partial.

**Do not claim:** the zero--one law in a vocabulary with a built-in linear
order, successor, constants, or function symbols. Libkin explicitly notes that
constants/functions can destroy the law, and order/successor are standard
counterexamples. Do not say “NP equals existential first-order”; Fagin uses
existential **second-order** logic.

### `D-P4-012` — Lindström, relocated (S)

P2b has already fixed the relevant notion of a **regular abstract logic** in a
relational presentation: isomorphism invariance, finite occurrence/reduct,
renaming, extension of relational first-order logic, closure under negation
and conjunction, fresh-constant abstraction, and unary relativization to a
nonempty induced substructure. P3 must reuse that definition verbatim or point
back to it; introducing a second notion of “abstract logic” would make the two
statements incomparable.

At that fixed standing, the target statement is:

> A regular abstract logic extending relational first-order logic that is
> countably compact and has the downward Löwenheim--Skolem property to
> countable models is no more expressive than first-order logic.

The primary source is Per Lindström, “On Extensions of Elementary Logic,”
*Theoria* 35(1) (1969), 1--11,
[DOI 10.1111/j.1755-2567.1969.tb00356.x](https://doi.org/10.1111/j.1755-2567.1969.tb00356.x),
existing key `Lindstrom1969`. Heinz-Dieter Ebbinghaus, Jörg Flum, and Wolfgang
Thomas, *Mathematical Logic*, 2nd ed. (Springer, 1994),
[DOI 10.1007/978-1-4757-2355-7](https://doi.org/10.1007/978-1-4757-2355-7),
Chapter 13, pp. 261--276, is the existing authoritative modern treatment
(`EbbinghausFlumThomas1994`).

**Claim ceiling:** cited statement and abstract-model-theory context,
`cited=Lindstrom1969`; no annex item. “Has a countable model” must mean every
satisfiable sentence has a countable model in the already fixed definition.

**Do not claim:** a theorem about arbitrary informal “logics,” or a version
with only ordinary compactness when the P2b statement fixes countable
compactness. Do not write a second proof or change the closure axioms during
relocation.

## Apparatus specifications

### `A-040` — first-order theories master table

Use theory names with their languages and parameters fixed in the first
column. The following is the safe classification ceiling.

| theory as named | complete? | decidable? | literal QE? | categoricity spectrum / caution |
|---|---|---|---|---|
| DLO in `{<}` | yes | yes | yes | (\aleph_0)-categorical; not categorical in uncountable cardinals |
| `ACF_p` in `{0,1,+,-,\cdot}` for fixed (p=0) or prime | yes | yes | yes | categorical in every uncountable cardinal; not (\aleph_0)-categorical |
| RCF in ordered-ring language `{0,1,+,-,\cdot,<}` | yes | yes | yes | not categorical in any infinite cardinal |
| Presburger arithmetic `Th(N;0,1,+,<)` | yes | yes | not in the bare language; yes after adding congruence/divisibility predicates | not categorical in any infinite cardinal |
| `Th(N;S)` | yes | yes | no in `{S}`; yes after naming `0` | uncountably categorical; not (\aleph_0)-categorical |
| atomless Boolean algebras in the standard Boolean-algebra language | yes | yes | yes | (\aleph_0)-categorical; not uncountably categorical |
| PA in its standard first-order arithmetic language | no, assuming consistency | no | no | not categorical in any infinite cardinal |
| true arithmetic `Th(N,+,\cdot,0,1,<)` | yes by definition | no; not computably enumerable | no | not categorical in any infinite cardinal; has nonstandard elementary equivalents |
| ZFC in `{\in}` | no if consistent (incompleteness) | no | no | not categorical in any infinite cardinal, conditional on consistency/models |

The register's exact `A-040` list omits `Th(N;S)` and atomless Boolean
algebras, but the Phase-4 handover explicitly requires both in the flagship QE
catalog. Include them in `A-041`, and either add them to `A-040` as clearly
additional rows or keep `A-040` literal and cross-point to `A-041`.

Critical qualifications:

- “ACF” without a fixed characteristic is not complete. Write `ACF_p`.
- RCF eliminates quantifiers in the **ordered-ring** language, not literally
  in the pure ring language.
- Presburger QE is language-sensitive; it needs the congruence/divisibility
  expansion.
- `Th(N;S)` does not eliminate quantifiers in the bare successor language;
  naming the initial point repairs it. The UvA
  [Model Theory exercise sheet 6](https://staff.fnwi.uva.nl/b.vandenberg3/Onderwijs/Model_theory_2015/exercise_sheet_6.pdf),
  Exercise 2(d), records the negative base-language result; Joel David
  Hamkins's expert exposition
  [“Theory of successor”](https://jdh.hamkins.org/tag/quantifier-elimination/)
  gives the explicit `{0,S}` axioms and elimination argument.
- PA/ZFC entries must state their consistency conditional rather than silently
  assuming a model.

The DLO and ACF rows are licensed directly by v1.1 lines 7177--7197 and
7286--7291. RCF and Presburger may cite Marker or standard decision/QE
references already used elsewhere; the arithmetic negative rows should point
to the P4/P5 incompleteness/undecidability entries rather than duplicate their
proofs.

### `A-041` — QE catalog and complexity

The table should separate four questions that are often collapsed:

1. Does the theory eliminate quantifiers in the named base language?
2. If not, what **definitional expansion** has QE?
3. Is the theory model-complete?
4. What is known about the decision problem or the size/time of QE output?

“Definable Skolem functions” is a fifth independent column: every formula
(\exists y\,\varphi(x,y)) admits a definable choice function on its nonempty
fibers. It is not synonymous with QE or model completeness. Do not fill that
column by inference alone; for DLO and ACF the answer is no (automorphisms
prevent a definable choice respectively above a point and between conjugate
roots), while RCF has definable choice. Presburger and the successor/Boolean
rows need an explicit cited source before a yes/no is printed.

| theory | eliminating language / witness | model-complete? | calibrated complexity note |
|---|---|---|---|
| DLO | base `{<}`; eliminate one existential by finite order-type cases | yes | validity is PSPACE-complete; Dexter Kozen, *Theory of Computation* (Springer, 2006), Lecture 21, Theorem 21.2, [DOI 10.1007/1-84628-477-5](https://doi.org/10.1007/1-84628-477-5) |
| `ACF_p` | base ring language; algebraic geometry/resultants are the witness family | yes | Grigor'ev gives a parameter-sensitive QE algorithm polynomial in (L^{n^{2a+1}}), where (L) is formula size, (n) variables, and (a) quantifier alternations; do not compress this to one misleading class label |
| RCF | ordered-ring language; sign conditions/Tarski--Seidenberg | yes | QE output can require doubly exponential space and time; this is an output lower bound, not by itself an exact decision-complexity classification |
| Presburger | add congruence predicates (or divisibility predicates) and use Cooper-style elimination | yes | Fischer--Rabin gives a doubly exponential lower bound under its model; do not report it without the formula-size/model qualification |
| `Th(N;S)` | add the initial-point constant `0`; predecessor existence becomes `x\ne0` | no in the bare language; yes in the `{0,S}` eliminating expansion | the first-order theory of one successor is PSPACE-complete in the Ferrante--Rackoff analysis; state the exact language |
| atomless Boolean algebras | standard Boolean language; split finite Boolean combinations into atoms | yes | Kozen gives completeness for the Berman alternating class (\bigcup_{c<\omega}\mathrm{STA}(*,2^{cn},n)), including the atomless subclass; define the class if printed |

The negative model-completeness entry for bare `Th(N;S)` is also directly
checkable: the shift (n\mapsto n+1) embeds ((\mathbb N,S)) onto its tail,
but the image's first element has no predecessor inside the tail and does have
a predecessor in the ambient structure. Naming `0` blocks that embedding.

Complexity sources and locators:

- D. Yu. Grigor'ev, “The Complexity of the Decision Problem for the First
  Order Theory of Algebraically Closed Fields,” *Mathematics of the
  USSR-Izvestiya* 29(2) (1987), 459--475,
  [DOI 10.1070/IM1987v029n02ABEH000979](https://doi.org/10.1070/IM1987v029n02ABEH000979).
  The [MathNet record](https://www.mathnet.ru/eng/im1566) gives the exact
  parameterized bound in its abstract.
- James H. Davenport and Joos Heintz, “Real Quantifier Elimination Is Doubly
  Exponential,” *Journal of Symbolic Computation* 5(1--2) (1988), 29--35,
  [DOI 10.1016/S0747-7171(88)80004-X](https://doi.org/10.1016/S0747-7171(88)80004-X).
- Michael J. Fischer and Michael O. Rabin, “Super-Exponential Complexity of
  Presburger Arithmetic,” *Complexity of Computation*, SIAM--AMS Proceedings
  7 (1974), 27--41, existing key `FischerRabin1974`.
- Jeanne Ferrante and Charles W. Rackoff, *The Computational Complexity of
  Logical Theories*, Lecture Notes in Mathematics 718 (Springer, 1979),
  Chapter “Integer addition,” pp. 47--54, and additional upper bounds,
  [DOI 10.1007/BFb0062837](https://doi.org/10.1007/BFb0062837).
- Dexter Kozen, “Complexity of Boolean Algebras,” *Theoretical Computer
  Science* 10(3) (1980), 221--247,
  [DOI 10.1016/0304-3975(80)90048-1](https://doi.org/10.1016/0304-3975(80)90048-1).

**Unsupported formulations to avoid:** “RCF is 2-EXPTIME-complete” does not
follow from the Davenport--Heintz output lower bound. “ACF is polynomial time”
without fixing the variables/alternations does not follow from Grigor'ev's
parameterized bound. Do not call the Berman class PSPACE. Do not label bare
Presburger arithmetic as having literal QE.

### `A-043` — classification-theory overview

A compact table can use these columns: dividing line; exact defining witness;
canonical positive example; canonical negative example; implication. Safe
rows are:

| row | defining witness | positive example | negative example / relation |
|---|---|---|---|
| stable | no formula has the order property | ACF | DLO is unstable |
| simple | forking has local character (under the fixed complete-theory convention) | random graph; every stable theory | random graph shows simple does not imply stable |
| NIP | no formula shatters arbitrarily large finite sets | DLO, RCF, all stable theories | random graph has IP |
| o-minimal | unary definable sets are finite unions of points and intervals | DLO, RCF | implies NIP, not stability |

Do not put “forking” in a cell without the dividing/forking definitions in the
nearby entry.

### `A-044` — finite-model-theory comparison

| result | scope | exact conclusion | contrast |
|---|---|---|---|
| first-order zero--one law | fixed finite relational vocabulary; uniform labeled structures on `[n]` | every FO sentence has limiting probability 0 or 1 | fails with common built-in order/successor enrichments |
| Fagin | isomorphism-closed properties of finite relational structures | NP iff existential second-order definable | not existential first-order |
| Trakhtenbrot | finite relational signature with a binary relation | finite satisfiability c.e. undecidable; finite validity not c.e. | unrestricted validity is c.e. by completeness |
| finite compactness | finite models only | compactness fails | ordinary first-order compactness permits infinite models |

### `A-162` — symbol registry audit

The live `handbook/registry/symbols.csv` already has:

| live glyph | role / scope | consequence |
|---|---|---|
| `\mathcal M\equiv\mathcal N` | elementary equivalence, global, first use P2.2 | use `\equiv` only in this role; formula equivalence remains `\Leftrightarrow` |
| `\mathcal M\preccurlyeq\mathcal N` | elementary substructure, global, first use P2.2 | the apparatus's `\preceq` is deliberately normalized to the manuscript's `\preccurlyeq` |
| `\operatorname{Diag}(\mathcal M)` | atomic diagram, P3 | already registered |
| `\operatorname{ElDiag}(\mathcal M)` | elementary diagram, P2.2--P3 | already registered |
| `S_n(T)` | type space, P3 | already registered |
| `\prod_{i\in I}\mathcal M_i/\mathcal U` | ultraproduct, P3.3 | already registered |
| `\mathcal M\cong\mathcal N` | isomorphism, global | use this, not `\simeq`, for isomorphism |
| `\simeq` | Kleene equality, P4 | the apparatus wording is stale if it intends isomorphism |

No P3 symbol intake is needed for these seven roles. If the new entries use
new persistent notation such as (\equiv_k), IP/NIP, or the forking symbol,
either define it locally without treating it as a global glyph or propose a
scoped symbol-intake row. Do not create a second forcing-like or equivalence
macro ad hoc. In particular, `A-162` must not reassign `\simeq` to
isomorphism.

## Bibliography audit and intake plan

### Existing keys sufficient as-is

`ChangKeisler1990`, `Hodges1993`, `Marker2002`, `Los1955`,
`RyllNardzewski1959`, `Engeler1959`, `Svenonius1959`, `Fraisse1954`,
`Ehrenfeucht1961`, `Lindstrom1969`, `EbbinghausFlumThomas1994`,
`RobinsonJointConsistency1956`, `Libkin2004`, `GlebskiiEtAl1969`,
`Fagin1976`, `Fagin1974`, `Trakhtenbrot1950`, and `FischerRabin1974` are
present in `handbook/bib/handbook.bib`. Do not duplicate them in an intake.

### New verified keys needed if the recommended claims are used

The following metadata was checked against the linked publisher,
institutional, or author records. These are proposals for `bib/intake-p03.bib`,
not edits made by this research visit.

```bibtex
@article{Shelah1971Ultrapowers,
  author       = {Shelah, Saharon},
  title        = {Every Two Elementarily Equivalent Models Have Isomorphic Ultrapowers},
  journaltitle = {Israel Journal of Mathematics},
  volume       = {10},
  number       = {2},
  pages        = {224--233},
  year         = {1971},
  doi          = {10.1007/BF02771574},
}

@article{EhrenfeuchtMostowski1956,
  author       = {Ehrenfeucht, Andrzej and Mostowski, Andrzej},
  title        = {Models of Axiomatic Theories Admitting Automorphisms},
  journaltitle = {Fundamenta Mathematicae},
  volume       = {43},
  number       = {1},
  pages        = {50--68},
  year         = {1956},
  doi          = {10.4064/fm-43-1-50-68},
}

@article{Shelah1971Stability,
  author       = {Shelah, Saharon},
  title        = {Stability, the f.c.p., and Superstability; Model Theoretic Properties of Formulas in First Order Theory},
  journaltitle = {Annals of Mathematical Logic},
  volume       = {3},
  number       = {3},
  pages        = {271--362},
  year         = {1971},
  doi          = {10.1016/0003-4843(71)90015-5},
}

@book{TentZiegler2012,
  author       = {Tent, Katrin and Ziegler, Martin},
  title        = {A Course in Model Theory},
  series       = {Lecture Notes in Logic},
  number       = {40},
  publisher    = {Cambridge University Press},
  year         = {2012},
  doi          = {10.1017/CBO9781139015417},
}

@article{Kim1998,
  author       = {Kim, Byunghan},
  title        = {Forking in Simple Unstable Theories},
  journaltitle = {Journal of the London Mathematical Society},
  volume       = {57},
  number       = {2},
  pages        = {257--267},
  year         = {1998},
  doi          = {10.1112/S0024610798005985},
}

@book{Simon2015,
  author       = {Simon, Pierre},
  title        = {A Guide to NIP Theories},
  series       = {Lecture Notes in Logic},
  number       = {44},
  publisher    = {Cambridge University Press},
  year         = {2015},
  doi          = {10.1017/CBO9781107415133},
}

@book{VanDenDries1998,
  author       = {van den Dries, Lou},
  title        = {Tame Topology and O-minimal Structures},
  series       = {London Mathematical Society Lecture Note Series},
  number       = {248},
  publisher    = {Cambridge University Press},
  year         = {1998},
  doi          = {10.1017/CBO9780511525919},
}

@article{PillaySteinhorn1986,
  author       = {Pillay, Anand and Steinhorn, Charles},
  title        = {Definable Sets in Ordered Structures. I},
  journaltitle = {Transactions of the American Mathematical Society},
  volume       = {295},
  number       = {2},
  pages        = {565--592},
  year         = {1986},
  doi          = {10.1090/S0002-9947-1986-0833697-X},
}

@article{Lyndon1959,
  author       = {Lyndon, Roger C.},
  title        = {Properties Preserved under Homomorphism},
  journaltitle = {Pacific Journal of Mathematics},
  volume       = {9},
  number       = {1},
  pages        = {143--154},
  year         = {1959},
  doi          = {10.2140/pjm.1959.9.143},
}

@book{Kozen2006,
  author       = {Kozen, Dexter C.},
  title        = {Theory of Computation},
  series       = {Texts in Computer Science},
  publisher    = {Springer},
  year         = {2006},
  doi          = {10.1007/1-84628-477-5},
}

@book{FerranteRackoff1979,
  author       = {Ferrante, Jeanne and Rackoff, Charles W.},
  title        = {The Computational Complexity of Logical Theories},
  series       = {Lecture Notes in Mathematics},
  number       = {718},
  publisher    = {Springer},
  year         = {1979},
  doi          = {10.1007/BFb0062837},
}

@article{Grigoriev1987,
  author       = {Grigor'ev, D. Yu.},
  title        = {The Complexity of the Decision Problem for the First Order Theory of Algebraically Closed Fields},
  journaltitle = {Mathematics of the USSR-Izvestiya},
  volume       = {29},
  number       = {2},
  pages        = {459--475},
  year         = {1987},
  doi          = {10.1070/IM1987v029n02ABEH000979},
}

@article{DavenportHeintz1988,
  author       = {Davenport, James H. and Heintz, Joos},
  title        = {Real Quantifier Elimination Is Doubly Exponential},
  journaltitle = {Journal of Symbolic Computation},
  volume       = {5},
  number       = {1--2},
  pages        = {29--35},
  year         = {1988},
  doi          = {10.1016/S0747-7171(88)80004-X},
}

@article{Kozen1980,
  author       = {Kozen, Dexter C.},
  title        = {Complexity of Boolean Algebras},
  journaltitle = {Theoretical Computer Science},
  volume       = {10},
  number       = {3},
  pages        = {221--247},
  year         = {1980},
  doi          = {10.1016/0304-3975(80)90048-1},
}
```

`Bankston2006` is optional if the Chang--Łoś--Suszko row cites only
`ChangKeisler1990` plus the nearby table prose; add it only if it is actually
cited. Do not create bibliography entries for web course notes unless the
handbook itself cites them; the stable books/articles above should carry the
printed claims.

## Unsupported or overstrong formulations: rejection list

The verifier should reject any P3 draft containing one of these unless new
evidence and hypotheses are supplied:

1. `ACF` is complete without fixing characteristic.
2. RCF has QE in the pure ring language.
3. Presburger arithmetic has literal QE in its bare standard language.
4. `Th(N;S)` has QE without naming the initial point.
5. The EF theorem is stated across different signatures or as full elementary
   equivalence after one fixed finite game.
6. A single small EF board is presented as the proof of a uniform
   inexpressibility result.
7. Łoś--Tarski is asserted over finite structures.
8. Lyndon positivity is conflated with existential-positive homomorphism
   preservation.
9. Keisler--Shelah is stated using one fixed nonprincipal ultrafilter on
   (\omega), or as (\mathcal M\cong\mathcal N).
10. Compactness via ultraproducts is called choice-free or indexes only by
    (\mathbb N) without justification.
11. Every atomic model is called prime; countability/completeness are absent.
12. An EM model is claimed to be generated by its indiscernibles without a
    stated Skolem-hull/blueprint construction.
13. Forking equals dividing in arbitrary theories, or every unstable theory is
    called nonsimple.
14. NIP is identified with stability, or o-minimality with stability.
15. The zero--one law is stated for ordered/function-symbol vocabularies.
16. Fagin's theorem is misstated as existential first-order logic.
17. Lindström is stated for an undefined informal class of “logics,” or with a
    different closure package from the existing P2b entry.
18. `\simeq` is reused for isomorphism despite the registry reserving it for
    Kleene equality.
19. Davenport--Heintz is cited as an exact 2-EXPTIME classification of RCF
    decision, or Grigor'ev as an unqualified polynomial-time theorem.
20. Any of the six v1.1 cited theorems is upgraded to `proved=` without a new
    complete annex proof.

## Visit implementation and adversarial verification checklist

### Migration accounting

- Account explicitly for all three source chapters and every row in the
  inventory. Examples/exercises may be deliberately retired, but the reason
  should be recorded rather than silently losing them.
- Preserve the 17/1/6 status distribution in substance. A compressed proof may
  be downgraded; it may never be upgraded.
- Put Łoś and back-and-forth in `hbmethod` boxes and keep their exact statused
  theorem statements nearby. `hbmethod` itself does not carry the theorem
  status grammar.
- Retain `R-015`, `R-016`, `R-028`, `R-029`, and `R-036` at the precise loci
  above.
- Keep every rule-like display out of the body; P3 should need no new calculus
  sheet.
- Put `\index` tags at definition sites for elementary map/substructure,
  diagram, type/type space, saturation, homogeneity, filter/ultrafilter,
  ultraproduct, QE, categoricity, EF game, prime/atomic, stability/forking/
  simplicity, NIP, and o-minimality.

### Required depth outcome

- Fill all eleven `must`/`should` rows at their exact ceilings.
- Leave `D-P4-006` and `D-P4-011` as explicit row-named stubs.
- Build all seven apparatus rows `A-040`, `A-041`, `A-042`, `A-043`, `A-044`,
  `A-122`, and `A-162`; do not mark an apparatus row done merely because a
  research table exists here.
- Cite only real bibliography keys that are live or added through
  `bib/intake-p03.bib`; avoid placeholder metadata.

### Minimum fidelity sample for the deliberate second pass

The required twelve-entry sample should include at least:

1. homomorphism/embedding definitions (6076--6107);
2. Tarski--Vaught statement and witness hypotheses (6271--6322);
3. diagram tests (6350--6408);
4. elementary-chain theorem and coherent-union warning (6435--6492);
5. type-space compactness with `R-028` completion (6539--6616);
6. saturation/homogeneity with `R-029` compactness use (6661--6769);
7. omitting types exact countability/nonprincipality hypotheses (6796--6822);
8. nonprincipal ultrafilter lemma with `R-036` (6858--6940);
9. **Łoś Tier-1** statement and all induction cases (6994--7105);
10. model-completeness reduction with `R-015` (7209--7259);
11. **back-and-forth Tier-1** extension clause with `R-016` (7318--7369);
12. Ryll--Nardzewski hypotheses and equivalences (7437--7449).

Add direct checks of every newly written theorem statement against the sources
above, especially: EF signature/rank; prime/atomic countability; zero--one
vocabulary; `ACF_p` characteristic; Presburger and successor languages; and
Keisler--Shelah's unrestricted “some ultrapowers.”

## External source ledger

All links were retrieved or rechecked 2026-08-10.

| topic | authority and stable locator |
|---|---|
| EF games | Ehrenfeucht 1961, DOI 10.4064/fm-49-2-129-141; Libkin 2004, Chapter 3, DOI 10.1007/978-3-662-07003-1 |
| preservation | Speirs/Scanlon course notes §20.2; van den Berg §2; Lyndon 1959, DOI 10.2140/pjm.1959.9.143; Rossman Theorems 1.1--1.2 |
| Keisler--Shelah | Shelah 1971, *Israel J. Math.* 10(2), 224--233, DOI 10.1007/BF02771574 |
| ultraproduct compactness | Cody §6, pp. 15--16; Chang--Keisler 3rd ed. |
| prime/atomic/RN | Marker 2002 §§4.2, 4.4, DOI 10.1007/b98860; Speirs/Scanlon course notes §24.2; Bays Theorem 8.30 |
| Lindström | Lindström 1969, DOI 10.1111/j.1755-2567.1969.tb00356.x; Ebbinghaus--Flum--Thomas 2nd ed., Chapter 13, DOI 10.1007/978-1-4757-2355-7 |
| indiscernibles/EM | Ehrenfeucht--Mostowski 1956, DOI 10.4064/fm-43-1-50-68; Marker §5.2 |
| stability/simple | Shelah 1971, DOI 10.1016/0003-4843(71)90015-5; Tent--Ziegler Chapters 7--8, DOI 10.1017/CBO9781139015417; Kim 1998, DOI 10.1112/S0024610798005985 |
| NIP/o-minimal | Simon 2015 Chapter 2, DOI 10.1017/CBO9781107415133; van den Dries 1998, DOI 10.1017/CBO9780511525919; Pillay--Steinhorn 1986, DOI 10.1090/S0002-9947-1986-0833697-X |
| finite model theory | Libkin Chapters 9 and 12; Fagin 1974/1976; Glebskiĭ et al. 1969; Trakhtenbrot 1950 |
| QE complexity | Kozen 2006 Lecture 21; Ferrante--Rackoff 1979; Grigor'ev 1987; Davenport--Heintz 1988; Fischer--Rabin 1974; Kozen 1980 |
