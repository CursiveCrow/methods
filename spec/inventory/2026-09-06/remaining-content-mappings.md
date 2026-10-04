# Remaining content mappings

Completed 2026-09-07 09:10:52 UTC. All four requested mappings are resolved; no IDs remain unexamined.

| Requirement | Current source state | Proof standing | Required action |
|---|---|---|---|
| N-x-014 | Related left-c.e./Ω material exists; TTE and Weihrauch development absent | Local proof for the narrower Ω result only | Supply the required computable-analysis treatment |
| D-P10-019 | Explicit MP statement and status reached from P8 | Cited theorem | No remaining statement/status or routing component |
| D-P2-007 | P12 Tseitin discussion exists; P2 CNF forward reference absent | Attributed general assertion and one worked gate | Add an exact active statement/forward route |
| D-P2-010 | Congruence remains an exercise with feedback; promoted pair inactive | Solution sketch | Promote the exact CPL substitution/replacement results |

## Method and scope

Read exact original rows in new-content.csv and depth-gaps.csv; their E/T/S/P treatment ceilings and the old domain-x exclusion do not limit the current full-compendium contract.

Used the current transitive 841-file reader graph rooted at handbook/main.tex and handbook/handbook.sty, including input/include/showcalculus routes. Searched all handbook TeX with --no-ignore, then filtered hits to this active graph. A preliminary default-ignore search omitted restoration files; it was discarded and replaced by the no-ignore searches recorded here.

Read the mapped statements, cross-part targets, exercise feedback and pertinent alternate-scope proofs. Fresh SHA-256 hashes at this task's end matched the reader graph at every active evidence file.

No primary-source acquisition or external theorem revalidation was performed; cited_only identifies the book's actual evidence level, not a new verification of the cited author's proof.

Only the two assigned new inventory outputs were written. No manuscript/register edits, tests, builds, renders, acquisitions or unrelated source work were performed.

The Markov row asks for a statement and status. It does not ask for a proof of the full MP scheme in HA; the active cited result says HA does not derive that scheme. Its absence as a local HA proof is therefore not a defect in this requirement.

The former P2 syntax/semantics file is inactive even though its own prose says that the old theorems fill D-P2-007 and D-P2-010. Those claims are locating leads only. The current driver includes the restored chapter and the metatheory supplement instead.

## N-x-014 — computable analysis and computability over the reals (TTE, Weihrauch degrees)

Original row: [spec/registers/new-content.csv:185](C:/Dev/the-methods-of-reason/spec/registers/new-content.csv:185). Target: P4. Domain: x. Current content state: mixed; proof state: mixed; completion verified for this requirement: no.

Original register fields:

```json
{
  "id": "N-x-014",
  "domain": "x",
  "target_part": "P4",
  "chapter": "--",
  "item": "computable analysis and computability over the reals (TTE, Weihrauch degrees)",
  "treatment": "P",
  "priority": "--",
  "effort": "--",
  "sources": "Weihrauch 2000; Pour-El-Richards 1989",
  "notes": "excluded: separate subject with its own reference literature"
}
```

- Computability over the reals: **partial**. The active frontiers chapter defines left-c.e. reals and Omega and gives a local halting-information/noncomputability argument. It does not define a general representation of real numbers or real functions.
- TTE and represented-space computation: **absent**. Full no-ignore handbook TeX searches, filtered to the complete active reader route, found no TTE, Type-Two Effectivity, represented-space or Cauchy-name development.
- Weihrauch reducibility and degrees: **absent**. No active Weihrauch occurrence, definition, reduction operation, degree comparison or theorem was located.
- Source-specific introductory treatment of the two named books: **absent_from_active_text**. No active TTE/Weihrauch or Pour-El treatment was located. Source holdings/acquisition were outside this task; their availability is not inferred.

Proof classification: A local proof is present for the Omega theorem, using the cited noncomputability of prefix complexity. No TTE or Weihrauch theorem/proof is present. Mixed records this component distinction; it is not generic verification uncertainty.

Current read evidence:

- [handbook/parts/p04.tex:1](C:/Dev/the-methods-of-reason/handbook/parts/p04.tex:1), lines 1–83 fully read; active_reader_route. SHA-256 9e1cd4671fa9e1a5d5d951305116d1f728591f689fb66b83c3dc47585f50312d. Route: handbook/main.tex:27 → handbook/parts/p04.tex.
- [handbook/parts/p04/frontiers-of-computability.tex:340](C:/Dev/the-methods-of-reason/handbook/parts/p04/frontiers-of-computability.tex:340), lines 340–365 fully read; active_reader_route. SHA-256 68e283f1cd364779ba7e0a525923b0c16fce962519c8bedeaaf087ba0ad20cb4. Route: handbook/main.tex:27 → handbook/parts/p04.tex:77 → handbook/parts/p04/frontiers-of-computability.tex.
- [handbook/annex/p04/frontiers.tex:25](C:/Dev/the-methods-of-reason/handbook/annex/p04/frontiers.tex:25), lines 25–58 fully read; active_reader_route. SHA-256 622f507b7a8fba1389a2a3ee0403102e79ad335c17e36ddd37f0ef5e4ac15d57. Route: handbook/main.tex:46 → handbook/annex/p04.tex:5 → handbook/annex/p04/frontiers.tex.

Full-route search evidence:

- Scope: All handbook *.tex, with --no-ignore, intersected with the 841-file active reader graph. Patterns: word-bounded TTE; Weihrauch; computable analysis; computability over the reals; type.two.effect; represented.space; Cauchy; Pour.El; effective analysis; oracle/real combinations. Result: No required-subject body hit.
- Scope: All handbook *.tex, with --no-ignore, intersected with the same graph. Patterns: computab.{0,50}real and real.{0,50}computab. Result: The related Omega theorem at frontiers-of-computability.tex:358; its entire definition/result/proof route was then read.

Remaining: Supply the missing computable-analysis foundation, TTE/representations and Weihrauch reduction/degree development with exact source attribution and appropriate proofs or cited results. The earlier domain-x exclusion/treatment P is superseded by the full-compendium contract. The Omega proof is a related subtopic, not completion of this subject.

The remaining components are concrete content/routing/proof omissions, not an unresolved destination lookup.

## D-P10-019 — Markov's principle: statement and status

Original row: [spec/registers/depth-gaps.csv:103](C:/Dev/the-methods-of-reason/spec/registers/depth-gaps.csv:103). Target: P8.1. Domain: depth. Current content state: substantive_present; proof state: cited_only; completion verified for this requirement: yes.

Original register fields:

```json
{
  "id": "D-P10-019",
  "source_part": "X",
  "item": "Markov's principle: statement and status",
  "target_home": "P8.1",
  "treatment": "S",
  "priority": "could",
  "effort": "S",
  "depends": "",
  "notes": ""
}
```

- Explicit Markov scheme with its decidability hypothesis: **present**. def:p07-markov-principle gives the universal closure of forall x(phi(x) or not phi(x)) -> (not not exists x phi(x) -> exists x phi(x)); the decidability premise is explicitly part of the scheme.
- Status in relation to HA and number realizability: **cited**. thm:p07-markov-realizability-boundary, cited to TroelstraVanDalen1988, says ordinary Kleene number realizability validates the instances under the classical metatheory, while HA does not derive the full scheme. The commentary distinguishes the separate nonderivability model argument.
- Usable P8-to-P7 route: **present**. The active P8 paragraph at 401–405 references both exact active P7 labels and excludes an inference to the choice-sequence/continuity schemes.
- Honest local-proof classification: **present**. The P7 annex expressly identifies the Markov boundary as cited, with no local annex proof. The only proof in that annex is the cut-free LJ disjunction last-rule lemma.

Proof classification: Cited theorem, not a local proof of MP, HA soundness, or nonderivability. This satisfies the original statement-and-status requirement.

Current read evidence:

- [handbook/parts/p08/intuitionistic-supplement.tex:389](C:/Dev/the-methods-of-reason/handbook/parts/p08/intuitionistic-supplement.tex:389), lines 389–405 fully read; active_reader_route. SHA-256 b91a31e23ff7237bb2302767d1ec5ef03ed742bc8ed7a83592d5694ffa8c8018. Route: handbook/main.tex:32 → handbook/parts/p08.tex:14 → handbook/parts/p08/intuitionistic-supplement.tex.
- [handbook/parts/p07/functional-interpretations.tex:168](C:/Dev/the-methods-of-reason/handbook/parts/p07/functional-interpretations.tex:168), lines 168–217 fully read; active_reader_route. SHA-256 5d35142e54f4ac9561a18f1f2e106a5a9c32dcc7b3ccb4b353548f721aa97d22. Route: handbook/main.tex:30 → handbook/parts/p07.tex:116 → handbook/parts/p07/functional-interpretations.tex.
- [handbook/parts/p07/functional-interpretations.tex:269](C:/Dev/the-methods-of-reason/handbook/parts/p07/functional-interpretations.tex:269), lines 269–323 fully read; active_reader_route. SHA-256 5d35142e54f4ac9561a18f1f2e106a5a9c32dcc7b3ccb4b353548f721aa97d22. Route: handbook/main.tex:30 → handbook/parts/p07.tex:116 → handbook/parts/p07/functional-interpretations.tex.
- [handbook/parts/p07/arithmetic-proof-theory-supplement.tex:207](C:/Dev/the-methods-of-reason/handbook/parts/p07/arithmetic-proof-theory-supplement.tex:207), lines 207–217 fully read; active_reader_route. SHA-256 f2342aac46524540986157a2693ddf34dba6df480b26881e1c53dd10d8ca1130. Route: handbook/main.tex:30 → handbook/parts/p07.tex:115 → handbook/parts/p07/arithmetic-proof-theory-supplement.tex.
- [handbook/annex/p07/functional-interpretations.tex:1](C:/Dev/the-methods-of-reason/handbook/annex/p07/functional-interpretations.tex:1), lines 1–37 fully read; active_reader_route. SHA-256 81a9c33214b7a1e53c9d03fa516a406ff21a5e7c0c7797a3f5d64e45387c541e. Route: handbook/main.tex:49 → handbook/annex/p07.tex:12 → handbook/annex/p07/functional-interpretations.tex.

Remaining: No remaining source-level statement/status or routing component in this depth row. The citation's external proof was not reread or reconstructed in this inventory. The row requires stating MP and its status; it does not require, and must not be interpreted as requiring, an HA proof of the full MP scheme.

Only the exact registered MP statement/status and active cross-part route. External cited proofs and whole-book acceptance were not rechecked.

## D-P2-007 — Tseitin CNF transformation: statement and cross-reference from the CNF section

Original row: [spec/registers/depth-gaps.csv:14](C:/Dev/the-methods-of-reason/spec/registers/depth-gaps.csv:14). Target: P2.1. Domain: depth. Current content state: mixed; proof state: mixed; completion verified for this requirement: no.

Original register fields:

```json
{
  "id": "D-P2-007",
  "source_part": "II",
  "item": "Tseitin CNF transformation: statement and cross-reference from the CNF section",
  "target_home": "P2.1",
  "treatment": "S",
  "priority": "should",
  "effort": "S",
  "depends": "",
  "notes": "exists at 11945 but unreferenced from the CNF section"
}
```

- Statement of Tseitin CNF conversion: **partial**. Active P12 states the fresh-subformula-variable construction, truth constraints, root unit clause, expanded-signature equisatisfiability and possible linear size, citing Tseitin1968. It supplies the conjunction gate's exact clauses and unique extension calculation. It is not a numbered full general transformation theorem with all constructor cases.
- Cross-reference from the active propositional CNF section: **absent**. The complete active Normal forms section, inherited-01946-02186.tex:1–241, contains no Tseitin forward reference. P12 instead points backwards to the P2 CNF definitions.
- Distinguish equivalence from equisatisfiability: **present**. The active P12 section states this distinction explicitly. The active first-order normal-form table also warns that Tseitin conversion is equisatisfiable, but its generic see Part 2.1 reference does not reach a current P2 Tseitin theorem.
- Promoted former theorem as current evidence: **inactive**. thm:p02-tseitin, including its general linear transformation and unique-extension assertion, occurs in the inactive former propositional-syntax-semantics.tex file. It cannot fill the current route.

Proof classification: The active general assertion is attributed to Tseitin; the local calculation treats one conjunction gate and the root condition. No full generic conversion proof was found. The longer theorem is inactive, and the existing P2 CNF proof proves same-signature normal forms rather than the requested Tseitin expansion.

Current read evidence:

- [handbook/parts/p02.tex:1](C:/Dev/the-methods-of-reason/handbook/parts/p02.tex:1), lines 1–18 fully read; active_reader_route. SHA-256 f0083d69ed260951b95df228b6fa108cf62df048f4874da2e08a6d386c9f923f. Route: handbook/main.tex:25 → handbook/parts/p02.tex.
- [handbook/restoration/inherited-01946-02186.tex:1](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-01946-02186.tex:1), lines 1–241 fully read; active_reader_route. SHA-256 9a98bdf593c6331925a87701f3410f1d27312e73b3c32587be7cf5a2e839c09e. Route: handbook/main.tex:25 → handbook/parts/p02.tex:7 → handbook/restoration/scope-SRC-01946-02186.tex:2 → handbook/restoration/inherited-01946-02186.tex.
- [handbook/restoration/inherited-14351-14400.tex:1](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-14351-14400.tex:1), lines 1–50 fully read; active_reader_route. SHA-256 a7a70819adfad23f3b5f16285e253e63d9f6fa0914ae58f1d80e8f0f2bfcf355. Route: handbook/main.tex:36 → handbook/parts/p12.tex:10 → handbook/restoration/scope-SRC-14351-14400.tex:2 → handbook/restoration/inherited-14351-14400.tex.
- [handbook/parts/p12/sat-and-certificates.tex:1](C:/Dev/the-methods-of-reason/handbook/parts/p12/sat-and-certificates.tex:1), lines 1–17 fully read; active_reader_route. SHA-256 5ed4ab927a1e6fe8469cb932895d1fc667f3aad00fc067ccb513c4da41f4543a. Route: handbook/main.tex:36 → handbook/parts/p12.tex:45 → handbook/parts/p12/automation-and-mechanization.tex:4 → handbook/parts/p12/sat-and-certificates.tex.
- [handbook/parts/p02/first-order-normal-forms-supplement.tex:95](C:/Dev/the-methods-of-reason/handbook/parts/p02/first-order-normal-forms-supplement.tex:95), lines 95–112 fully read; active_reader_route. SHA-256 63e7bed495463332d2f4f8f8fdb92a044e70a1ceccbe4dfc019c8459b7aaf92b. Route: handbook/main.tex:25 → handbook/parts/p02.tex:46 → handbook/parts/p02/first-order-logic.tex:2 → handbook/parts/p02/first-order-normal-forms-supplement.tex.
- [handbook/parts/p02/propositional-syntax-semantics.tex:388](C:/Dev/the-methods-of-reason/handbook/parts/p02/propositional-syntax-semantics.tex:388), lines 388–414 fully read; inactive_not_reached_by_current_drivers. SHA-256 94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56.

Full-route search evidence:

- Scope: All handbook *.tex with --no-ignore, filtered to the active reader graph. Patterns: Tseitin and normal-form/clauses references. Result: Active targets are the P12 source section, P12 SAT reference paragraph and first-order table; the old P2 theorem is inactive. The full active P2 normal-form section was read to verify the missing forward reference.

Remaining: Add the required active forward link from the propositional CNF section to an exact active transformation statement. Complete or accurately cite the general construction and its scope as needed; the P12 conjunction-gate example alone is not a full constructor-by-constructor proof. Reconcile the misleading generic Part 2.1 pointer in the first-order table.

The remaining components are concrete content/routing/proof omissions, not an unresolved destination lookup.

## D-P2-010 — Substitution and replacement congruence theorems promoted from exercise to stated results

Original row: [spec/registers/depth-gaps.csv:17](C:/Dev/the-methods-of-reason/spec/registers/depth-gaps.csv:17). Target: P2.1. Domain: depth. Current content state: mixed; proof state: source_sketch; completion verified for this requirement: no.

Original register fields:

```json
{
  "id": "D-P2-010",
  "source_part": "II",
  "item": "Substitution and replacement congruence theorems promoted from exercise to stated results",
  "target_home": "P2.1",
  "treatment": "S",
  "priority": "should",
  "effort": "S",
  "depends": "",
  "notes": ""
}
```

- State uniform substitution and preservation of validity/equivalence: **inactive**. The definition and thm:p02-uniform-substitution exist at 186–203 of the former P2 syntax/semantics file, explicitly tagged as filling this row, but that file is inactive.
- Promote logical-equivalence congruence and selected-occurrence replacement: **absent_from_active_result_surface**. The active P2 text still asks for equivalence/congruence in ex:prop-metatheory-09; the selected-occurrence Replacement theorem is only in the inactive file.
- Supply corresponding proof material: **feedback_sketch_only**. The active solution gives the equal-input/equal-output truth-function argument and asks the reader to check unary and binary cases separately. It is labelled Solution sketch and has not been promoted to a theorem/proof.
- Distinguish different substitution/congruence results: **present_but_different_scope**. The active ND lemma grafts derivations into open assumptions; the FOL substitution lemma replaces a term for a variable and changes assignments; the P10 modal Lindenbaum theorem concerns provable equivalence for a normal modal logic. These do not state the requested two CPL semantic theorems or promote the exercise.

Proof classification: The exact requested active equivalence-congruence material is exercise feedback explicitly labelled a sketch. The inactive promoted pair is cited to Kleene1952. Other active local proofs have different syntax and operations and are not counted as this promotion.

Current read evidence:

- [handbook/restoration/inherited-01817-01898.tex:1](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-01817-01898.tex:1), lines 1–82 fully read; active_reader_route. SHA-256 499fec700936d0625769d7c09aa2bc5fd1f6d976b9eab1a9cbc8edfe8cafb9c4. Route: handbook/main.tex:25 → handbook/parts/p02.tex:5 → handbook/restoration/scope-SRC-01817-01898.tex:2 → handbook/restoration/inherited-01817-01898.tex.
- [handbook/restoration/inherited-02933-03021.tex:60](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-02933-03021.tex:60), lines 60–71 fully read; active_reader_route. SHA-256 ec910182f4db775f35fe3fa1a23f4f12f3cf31282e8dd761b208d0cad38d5b61. Route: handbook/main.tex:25 → handbook/parts/p02.tex:17 → handbook/restoration/scope-SRC-02933-03021.tex:2 → handbook/restoration/inherited-02933-03021.tex.
- [handbook/restoration/inherited-15638-16742.tex:161](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-15638-16742.tex:161), lines 161–167 fully read; active_reader_route. SHA-256 993a3153c9ca856f761b5650c312e85e2be78fa23b8afc8edcd4e87a7b2983bf. Route: handbook/main.tex:36 → handbook/parts/p12.tex:42 → handbook/restoration/scope-SRC-15638-16742.tex:2 → handbook/restoration/inherited-15638-16742.tex.
- [handbook/parts/p02/propositional-syntax-semantics.tex:186](C:/Dev/the-methods-of-reason/handbook/parts/p02/propositional-syntax-semantics.tex:186), lines 186–215 fully read; inactive_not_reached_by_current_drivers. SHA-256 94338430c4e87cf1b9228274b15adbac052c704eb0b4e81a48b4587a59217b56.
- [handbook/restoration/inherited-02193-02340.tex:123](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-02193-02340.tex:123), lines 123–147 fully read; active_reader_route. SHA-256 5ba27894edf744d288008b613adf93eac3d65385f745135de776d5b6011316a3. Route: handbook/main.tex:25 → handbook/parts/p02.tex:9 → handbook/restoration/scope-SRC-02193-02340.tex:2 → handbook/restoration/inherited-02193-02340.tex.
- [handbook/restoration/inherited-03519-03680.tex:60](C:/Dev/the-methods-of-reason/handbook/restoration/inherited-03519-03680.tex:60), lines 60–95 fully read; active_reader_route. SHA-256 b1f502609bb084acff222a7431e05caed5273acd19c367b45cbdccb63f306897. Route: handbook/main.tex:25 → handbook/parts/p02.tex:25 → handbook/restoration/scope-SRC-03519-03680.tex:2 → handbook/restoration/inherited-03519-03680.tex.
- [handbook/parts/p10/modal-algebra-completeness.tex:50](C:/Dev/the-methods-of-reason/handbook/parts/p10/modal-algebra-completeness.tex:50), lines 50–84 fully read; active_reader_route. SHA-256 ff35b6ab05f34bfbcd797e29135d841562d0910a4117b738b70fd5b4f7dc9048. Route: handbook/main.tex:34 → handbook/parts/p10.tex:3 → handbook/parts/p10/algebraic-and-categorical-logic.tex:128 → handbook/parts/p10/modal-algebra-completeness.tex.
- [handbook/annex/p10/modal-algebra-completeness.tex:5](C:/Dev/the-methods-of-reason/handbook/annex/p10/modal-algebra-completeness.tex:5), lines 5–20 fully read; active_reader_route. SHA-256 b4ead3da9e4d5166b97cd5ee976d3f109bcc4f8a7e18ca767009e3168208f33b. Route: handbook/main.tex:52 → handbook/annex/p10.tex:32 → handbook/annex/p10/modal-algebra-completeness.tex.

Full-route search evidence:

- Scope: All handbook *.tex with --no-ignore, filtered to the active reader graph. Patterns: uniform substitution; substitution/replacement congruence; replacement of equivalents; theorem/lemma/definition titles and labels containing substitut/replac/congruen. Result: No active promoted CPL pair. Active alternatives are ND, FOL, typed, equational, doctrine and modal results with different objects/operations. The full current P2 semantic and normal-form text and the exact exercise feedback were inspected.

Remaining: State the two exact CPL results on the active reader route, define their uniform-substitution and selected-occurrence operations, and attach appropriate proof/status/source evidence. The inactive pair can locate the intended scope, but should not be blindly restored without current notation/source review. The feedback may support a proof but is currently only a sketch.

The remaining components are concrete content/routing/proof omissions, not an unresolved destination lookup.

## Handoff

The [spec/inventory/2026-09-06/remaining-content-mappings.json](C:/Dev/the-methods-of-reason/spec/inventory/2026-09-06/remaining-content-mappings.json) companion contains all four rows and their hashes/routes. Replace the former generic unverified proof-state descriptions with these component findings. The result closes the destination checks; it does not add book content, reconstruct cited proofs, or admit a publication artifact.

