# Independent integrated-publication review: Part IX presentation N-c-012

## Review scope and method

I read the complete actual LaTeX source `handbook/parts/p09/presentations/n-c-012.tex`, from line 1 through EOF at line 3020. In this workspace that repository-relative file is located at `work/formal-logic-handbook/handbook/parts/p09/presentations/n-c-012.tex`.

I also read the actual LaTeX in `handbook/parts/p09/logic-in-computer-science.tex` needed for this review: the reused inclusive LTL/past definition, the strict/inclusive bridge, the first-order and complexity theorems, the safety/liveness definition, the automata-theoretic model-checking statement, and the `\input` seam (`logic-in-computer-science.tex:602-812, 900-907`).

I did not inspect a manuscript PDF, page render, PNG, screenshot, or any other derived manuscript artifact. I did not create or run a test, checker, repository script, TeX command, or build, and I did not recompute any hash. This is only a review of the writing present in the two actual `.tex` sources. It makes no layout judgment and does not claim final-publication acceptance.

## Decision

The presentation is not publication-ready at manuscript-content level. Five concrete must-fix findings remain. One is a direct violation of the requested exclusion of internal hash/workflow language. Two concern definition-before-use and technical standing. Two occur in the new final boundary paragraph and prevent that paragraph from being an exact source/handbook boundary statement.

## Blocker and must-fix findings

### PUB-01 — Internal acquisition, hash, and reading-workflow prose remains in the reader-facing manuscript

**Classification:** blocker.

The manuscript exposes source-audit artifacts rather than limiting itself to bibliographic identity, usable locators, rights qualifications, and mathematical proof ownership:

- `n-c-012.tex:8-21` calls the dissertation an acquired file, prints its SHA-256 digest, and gives a physical-PDF-page offset.
- `n-c-012.tex:372-382` narrates the acquired Pnueli wrapper, scan provenance, and the handbook's inspection workflow.
- `n-c-012.tex:1208-1225` again gives an acquired-file SHA-256 digest and discusses embedded file metadata and byte identity.
- `n-c-012.tex:1853-1870` repeats the pattern for Sistla--Clarke, including another SHA-256 digest.
- `n-c-012.tex:2993-3007` says that a second file “was read separately,” describes a “controlling object,” and closes with access-route and republication-workflow prose.

The three literal hash blocks at `n-c-012.tex:12-15`, `1214-1217`, and `1862-1865` independently falsify the required absence of hash language. The phrases “acquired file,” “physical PDF page,” “supports inspection,” “controlling object,” and “was read separately” are likewise evidence-log or review-workflow language rather than reader-facing mathematical exposition. They are not salvaged by the fact that the surrounding copyright cautions are responsible: a normal citation, edition statement, printed-page locator, and concise rights qualification can be retained without publishing acquisition history or byte fingerprints.

The minimum repair is to remove the hashes and the acquisition/inspection narrative from the running presentation, then retain only publication-appropriate source identification, citations, printed locators, rights qualifications where editorially necessary, and the source-versus-handbook proof boundary. I found no board, checker, test-run, or rendering-pipeline statement; the ordinary verbs “tests” at `n-c-012.tex:1053` and “renders” at `2808` are semantic prose, not workflow remnants. That does not cure the explicit hash and acquisition-workflow material above.

### TERM-01 — The label P1 is used without being bound to the displayed invariant rule

**Classification:** must fix for definition-before-use.

`n-c-012.tex:492-500` introduces “the first general principle” and displays reachable-state induction, but the display has no `(P1)` label and the surrounding prose never says that this rule is P1. The first literal occurrence of `P1` is much later, at `n-c-012.tex:708`, and `n-c-012.tex:717` again says that P1 yields invariance.

The likely intended referent is easy to infer retrospectively, but publication-ready definition-before-use cannot require that inference. The repair is minimal: bind the source label `(P1)` at `492-500`, or replace the later `P1` references with an unambiguous backward description. No new theory is needed.

### TERM-02 — `K_b` lacks an exact local definition and its standing shifts between fragment and calculus

**Classification:** must fix under the workspace terminology rule.

The presentation gives a propositional future-time basis at `n-c-012.tex:830-896`. It then first names a “future-restricted \(K_b\) fragment” at `902-905`, refers to a “full-\(K_b\)” proof there, returns to the future-restricted fragment at `1027-1031`, and finally speaks of “the \(K_b\) calculus extended by the system-dependent axioms” at `1119-1124`. Nowhere does it state an exact eliminable definition of `K_b`, say whether the local name denotes precisely G1--G3 plus RT, RG, and MP, or distinguish that local system exactly from the externally cited “full-\(K_b\)” system. Its standing consequently alternates among fragment, external modal system, and extensible calculus.

Later use establishes that some distinction is needed, but necessity and use do not supply definition, standing, or nonredundancy. The manuscript must either define the exact locally used `K_b` theorem system where the name first appears and distinguish it from the full external system, or avoid the technical name and state the source-reported obligation without naming an underdefined answer. In particular, it should make the relation to ER and to the later explicitly defined systems `DX` and `DUX` unambiguous.

### BND-01 — The final boundary paragraph changes Pnueli's `\leadsto` from a statement family/relation into an “operator”

**Classification:** must fix for technical standing.

The local definition is careful: `n-c-012.tex:473-482` says that `\varphi\leadsto\psi` names Pnueli's printed temporal-implication statement family, is a relation between state assertions, and is not a primitive in the handbook's LTL grammar. The closing paragraph instead says at `n-c-012.tex:3011-3014` that “his printed leads-to operator is strict.” In a paragraph whose purpose is to prevent definitions from crossing presentation boundaries, “operator” reverses the standing that the presentation explicitly established.

This does not require a new name. Replace “operator” by the already established “statement family” or “relation between state assertions.” The strict `j>i` content itself is accurate.

### BND-02 — The final boundary paragraph attributes the exact strict/inclusive bridge to GPSS rather than to the handbook

**Classification:** must fix for proof ownership and source fidelity.

At `n-c-012.tex:3014-3016`, the grammatical subject is Gabbay, Pnueli, Shelah, and Stavi: they are said to “give a strict future language and, over discrete time, a translation to inclusive word operators.” That overstates what the presentation has just established.

The presentation says that the past constructor `\mathsf S_s` used for the convention bridge is handbook-supplied, not source-transcribed (`n-c-012.tex:1274-1286`). It then states the exact discrete strict/inclusive equations at `1307-1328`. More decisively, its source-ownership analysis at `1789-1816` shows that GPSS's printed inclusive `\mathsf U^0` equation conflicts with its own recursion, so the handbook refuses to adopt it as one coherent defined operator. The parent text makes ownership explicit: `logic-in-computer-science.tex:639-685` supplies the exact two recursive metalinguistic translations `\tau` and `\sigma` and proves their intended truth-preservation standing by structural induction.

The closing sentence can be made accurate without introducing terminology: for example, “GPSS presents a strict future language; over discrete time, the handbook bridges its strict operators to the inclusive word operators reused here.” That wording preserves the source's strict language while leaving the exact bridge and its past completion with the handbook.

## Interfaces and distinctions that do pass review

The following checks found no additional must-fix defect:

- **Parent definition and input seam.** `logic-in-computer-science.tex:605-626` defines the reused inclusive past operators; `628-685` gives the strict/inclusive bridge; `687-721` states the first-order, PSPACE, and safety/liveness interfaces; and `904` inputs N-c-012 only after those definitions and the relevant automata/model-checking statements. N-c-012 therefore does not rely on a later presentation to define those interfaces. The following inputs at `905-907` preserve the intended five-presentation placement inside “Temporal logic and automata.”
- **Strict versus inclusive semantics.** Kamp's witness-strict, open-interval argument order is explicit at `n-c-012.tex:81-105`; Pnueli's strict `\leadsto` and inclusive `F,G` are separately stated at `473-490`, `830-856`, and `679-687`; GPSS's strict `\mathsf U_s` and the discrete inclusive bridge are explicit at `1227-1328`; and Sistla--Clarke's inclusive current-point witnesses are explicit at `1883-1950`. These agree with `logic-in-computer-science.tex:605-693` once the ownership defect in BND-02 is corrected.
- **Model-domain signposting.** Kamp's `\mathsf{Lin}`/`\mathsf{Com}` scope and rational counterexample are separated at `n-c-012.tex:23-47`, `140-172`; Pnueli's initial-state executions, arbitrary-start continuations, and proper executions are distinguished at `629-687`, `1037-1069`; GPSS separates point zero on omega-models, future formulas on discrete complete models, and arbitrary linear orders with undefined extra symbols at `1488-1554`; Sistla--Clarke separates word satisfiability, validity, and existential `R`-path truth at `1952-1990`; and Alpern--Schneider explicitly works over full `S^\omega` and warns that transition-system relativization changes the definitions at `2632-2674`, `2726-2729`.
- **Safety/liveness correspondence.** The exact bad-prefix and continuation quantifiers at `n-c-012.tex:2676-2704` support the concise parent definition at `logic-in-computer-science.tex:713-721`. The presentation also correctly distinguishes source classification lists from semantic definitions at `n-c-012.tex:1358-1363`, and it does not import Pnueli's or GPSS's formula vocabulary into Alpern--Schneider's property classes.
- **Theorem interfaces.** The discrete-word expressiveness statement at `logic-in-computer-science.tex:687-694`, the operator-sensitive PSPACE statement at `696-711`, and universal-path model-checking statement at `799-812` match the corresponding source-domain qualifications developed in N-c-012. In particular, N-c-012 preserves Sistla--Clarke's existential path problem rather than silently calling it universal model checking (`n-c-012.tex:1952-1990, 2600-2630`).
- **Proof ownership in the body.** Apart from BND-02, the presentation repeatedly marks handbook repairs, counterexamples, and expanded proofs as handbook-supplied and distinguishes them from source proofs, sketches, assertions, and external referrals. Representative load-bearing examples are Kamp's repaired parity induction (`n-c-012.tex:279-348`), Pnueli's P2 and completeness counterexamples (`528-552`, `650-687`), GPSS's proof-outline boundary (`1556-1660`, `1705-1787`), Sistla--Clarke's directed-cycle repair (`2197-2214`), and Alpern--Schneider's Corollary 2.1 repair (`2938-2971`).
- **Final unit coverage.** The final paragraph does account for all five presentations in their actual order, and its Kamp, Sistla--Clarke, and Alpern--Schneider contrasts are accurate. It introduces no new symbol, formula class, or named technical object. Once BND-01 and BND-02 are corrected, it will close the unit without transferring one source's definitions or proofs to another.
- **Terminology generally.** Most local technical names satisfy the workspace rule by giving definition, standing, distinction, and immediate use. Clear examples include “tense-defining formula” (`n-c-012.tex:49-79`), `\models_{\rm prop}` (`1058-1069`), `L_{\rm prop}(\Sigma)` (`1163-1172`), the local strict warnings `\mathsf U_s,\mathsf S_s` (`1264-1328`), and uniform versus absolute liveness (`2731-2771`). TERM-01 and TERM-02 are bounded exceptions, not evidence that the entire terminology layer must be redesigned.

VERDICT: REJECT -- PUB-01, TERM-01, TERM-02, BND-01, BND-02
