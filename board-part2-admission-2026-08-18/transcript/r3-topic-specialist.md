# Round 3 topic-specialist final source/content verification

### F1 — still-open
- reply: still-open
- current location: `handbook/annex/p02.tex:4-34`; `handbook/parts/p02/propositional-metatheory-supplement.tex:67-123`; `handbook/annex/p02/propositional-metatheory-supplement.tex:2-37`; `handbook/restoration/inherited-01946-02186.tex:97-115,230-240`; the six routed OPEN supplement notices already listed in F1.
- source/content verification: The substantive propositional debt has now been resolved sufficiently to permit an ordinary-attribution disposition. A separately attributed NNF-duality definition, theorem, and dictionary are routed at the body lines 67-123, and the corresponding complete annex proof is routed at annex lines 7-37. The inherited NNF and functional-basis theorems retain their complete proofs inline at inherited lines 97-115 and 230-240. Their retired historical annex backreferences are off route and have no live consumer, so they need not be recreated as aliases; the off-route fragment can be formally discarded. The annex root's claims that duality is absent and that later use still owes content are therefore stale.
- why still open: The actual reader bytes still print `OPEN`, `owes`, and `explicitly OPEN and unadmitted` at `handbook/annex/p02.tex:4-12,27-34`, and the six supplement notices still print OPEN/unadmitted status. In addition, F16 remains a source/content defect in the Hilbert addition covered by two of those notices. Thus the F1 source/content preconditions are almost closed, but the record itself is not fixed until the notices are replaced or their units unrouted.
- exact correction: After F16 is corrected, replace `annex/p02.tex:4-12` by an ordinary source-routing note: the inherited NNF and functional-basis proofs are inline, the retired historical annex fragment is discarded, and the separately attributed duality theorem/proof are routed at their current destinations. Replace each accepted supplement's OPEN notice by ordinary editorial/source/proof-status attribution; unroute any rejected pair. F2's admission records and the build, visual, human, and user gates may and should remain administratively open after those reader notices are removed.

### F3 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:106-172,175-244`; `handbook/annex/p02/higher-order-supplement.tex:87-136`.
- reasoning: The Round 2 scope mismatch is now closed. The incidence translation assumes an at-most-countable nonlogical second-order signature and imports the countable variable-stock injection at body lines 106-113. The derived relation repeats that scope at lines 175-180, and the strong-adequacy theorem quantifies only over formulas in the fixed at-most-countable signature at lines 230-238. The annex soundness direction now invokes the exact new incidence theorem, `thm:p02-sol-incidence-satisfaction`, at annex lines 93-96 rather than the inherited generic translation. Predicate-domain closure, matched schemas, tagged incidence, the collapse proof, and schema survival remain as verified in Round 2. The strongest adversarial and source-fidelity residuals therefore no longer apply.

### F6 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:21-40`; linked `handbook/registry/calculi/sol.tex:17-20`.
- reasoning: For every arity, lines 22-25 now fix an explicit enumeration `RelVar_n = {X^n_0,X^n_1,...}` and define least-fresh by the least absent index. Lines 26-38 give the arity-preserving capture-avoiding recursion, including stopping at the substituted binder, deterministic renaming of a binder for the inserted relation variable, and the predicate-constant case. The capture counterexample from Round 1 now has a unique output formula string, and the four sheet rules refer to this defined operation. This is the exact deterministic correction requested by the ledger.

### F10 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/variants.tex:406-427`.
- reasoning: The formation clause now requires `xbar=(x_1,...,x_n)` to contain pairwise distinct variables at lines 409-411. Consequently the simultaneous update in the satisfaction clause at lines 413-417 assigns each bound variable exactly one coordinate, eliminating the Round 2 repeated-variable ambiguity. The previously accepted arity, isomorphism invariance, semantic parameter, and family-indexed language remain unchanged.

### F15 — accept-fixed
- reply: accept-fixed
- current location: `handbook/parts/p02/first-order-completeness-remainder.tex:56-67`; `handbook/bib/handbook.bib:955-963`.
- reasoning: For the narrow question assigned to this seat, the citation now identifies the right theorem-bearing work. The warning cites `Skolem1923SetTheory`, whose entry is Skolem's *Einige Bemerkungen zur axiomatischen Begründung der Mengenlehre*, published in the 1923 report of the 1922 Helsinki congress at pages 217-232. That is the set-theory paper containing the Löwenheim-Skolem discussion and the paradox, unlike the former 1934 number-sequence paper. The title and proceedings-container accents are also now valid TeX at bibliography lines 957-958. Authoritative scholarly records corroborate the work, publication setting, pages, and its Skolem-paradox content: [Original Sources / van Heijenoort](https://www.originalsources.com/Document.aspx?DocID=4SMYN6BFJ693S9G), [Springer bibliographic record](https://link.springer.com/article/10.1007/s10992-026-09839-5).

### F16 — still-open
- reply: still-open
- current location: `handbook/registry/calculi/hilbert-fol.tex:10-19`; `handbook/parts/p02/first-order-calculi-supplement.tex:47-93,168-183`; `handbook/annex/p02/first-order-calculi-supplement.tex:22-40`.
- reasoning: The source attribution is now literal and the sheet correctly replaces the former zero-premise second existential schema by Kleene's dependency-sensitive rule: from `phi -> psi` infer `exists x phi -> psi`, with `x` absent from `psi` and every dependency of the premise line (`hilbert-fol.tex:18`). The body notices and comparison row now attribute Mendelson/Kleene by component. However, the selected calculus is not yet exact after that replacement. The dependency-annotated derivation definition at body lines 47-70 licenses only a premise, an axiom instance, MP, and Gen; it has no clause for the new existential-elimination rule or its inherited dependency set. The sheet identity at line 10 likewise says that lines arise only by MP or Gen. The deduction-theorem annex proof at lines 22-40 handles premises, axioms, MP, and Gen but has no existential-elimination induction case. Therefore the displayed rule is not part of the body-defined derivability relation, while the comparison table treats it as part of the calculus, and the proved deduction theorem does not cover every displayed inference.
- exact correction: (1) Add existential elimination to the sheet identity and to `def:p02-hilbert-fol-dependencies`: from a prior pair `(alpha -> beta,D)`, infer `(exists x alpha -> beta,D)` exactly when `x` is free in neither `beta` nor any member of `D`. (2) Add its deduction-theorem induction case. If the discharged formula `tau` is absent from `D`, reuse the traced derivation and A1. If `tau` is in `D`, the rule gives `x` absent from `tau`; use the induction result `tau -> (alpha -> beta)`, propositional permutation to obtain `alpha -> (tau -> beta)`, apply existential elimination to get `exists x alpha -> (tau -> beta)`, and permute back to `tau -> (exists x alpha -> beta)`. (3) Retain the current split attribution and then state or prove the existential-duality/strong-completeness transfer for this exact dependency-annotated rule surface.

## Notice-replacement decision

- The accepted F1 duality/annex repair, F3, F6, F10, and F15 fixes are sufficient on their own topics.
- They do **not yet permit every F1 notice to be replaced**, because F16 remains a source/content defect inside the routed Hilbert body/annex pair.
- Once the exact F16 derivation and deduction-theorem repair above is applied and independently verified, the Part II source/content findings in this focused agenda permit all accepted F1 notices to be replaced by ordinary attribution. F2 provenance/admission controls and the build, reference-resolution, visual, human, and user gates should remain administratively open and must not be inferred from that notice replacement.

## Round disposition

- accept-fixed: F3, F6, F10, F15.
- still-open: F1 (notice replacement and F16 dependency); F16 (exact derivation/rule/deduction-theorem mismatch).
- new findings: none outside direct repair fallout; the F16 residual is caused directly by replacing the former schema with Kleene's rule without updating the calculus definition and proof induction.

This round read the ledger, chair record, all Round 1 and Round 2 transcripts, and the latest live agenda files. It made no manuscript, control, test, or generated-file edit and ran no build.
