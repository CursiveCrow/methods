# N-c-012.b blind opening audit — adversarial publication and AGENTS compliance

## Seat, scope, and independence

- Seat: `/root/mcnaughton_1966_research`.
- Role: adversarial publication and AGENTS-compliance reviewer.
- Round: blind opening audit.
- Frozen presentation: `handbook/parts/p09/presentations/n-c-012.tex`, especially lines 370–618 and 1023–1027, read in the context of the complete 1,027-line file.
- Shared surfaces read: `handbook/parts/p09/logic-in-computer-science.tex` lines 599–825 and 2140–2175; the complete `spec/research/p09-pnueli-1977-source-note.md`; `spec/research/p09-source-presentations-lot2-3.md` lines 151–161; and `handbook/bib/handbook.bib` entry `Pnueli1977`, lines 2226–2236.
- Authority read visually: the archival wrapper and all twelve printed pages 46–57 in the frozen scholarly render of the author-hosted PostScript.
- Independence: I read the charter first, did not inspect the board ledger, chair record, another seat's transcript, or another reviewer's output, and did not contact another reviewer.
- Mutation boundary: this transcript is the only file I created. I made no manuscript, source-note, ledger, bibliography, or other workspace edit.
- Prohibited operations: I ran no tests, automated checkers, repository scripts, TeX, handbook-PDF inspection, or build. The only PDF inspected was the permitted scholarly source render.

## Steel-man

The frozen presentation gets the central historical boundary right. It distinguishes the paper's strict printed temporal implication from its inclusive `F`, records the unreconciled A2/Theorem 3 tension instead of silently modernizing it, separates the pure future-only calculus from the system-dependent rules, avoids retrojecting `X/U`, Büchi translation, safety/liveness syntax, or PSPACE, and gives honest external-proof boundaries for Theorems 2, 4, and 5. The source identity, author-hosted access route, May 1981 wrapper boundary, printed pagination, bibliography identity, and open IEEE-direct comparison are also mutually consistent.

That strong framework does not make the current snapshot complete. The following findings are substantive and each independently requires revision under the charter.

## Findings

### AP-F1 — The provenance record lacks the required rights boundary and complete derived-render identity

- **Severity:** must-fix
- **Exact location:** `spec/research/p09-pnueli-1977-source-note.md:12–31`; `handbook/parts/p09/presentations/n-c-012.tex:372–378`; `spec/research/p09-source-presentations-lot2-3.md:153`; `handbook/bib/handbook.bib:2234–2236`.
- **Claim:** The surfaces establish a public author-hosted access route and correctly avoid calling the file IEEE-supplied, but none says what rights were or were not granted. The source note also records hashes for the compressed and decompressed PostScript but not the frozen 13-page scholarly PDF render used for visual adjudication.
- **Evidence:** The visually inspected wrapper contains the title, author, and “May 1981”; printed p. 46 begins the conference paper; neither the wrapper nor printed pp. 46–57 displays a Creative Commons notice, public-domain dedication, or reproduction license. Public hosting supplies lawful reading provenance, not an inferred right to redistribute the scan. The frozen PDF has SHA-256 `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` and 13 physical pages: wrapper page 1, then printed pp. 46–57 on physical pages 2–13.
- **Harm:** A future editor can mistake “author-hosted” for reproduction permission or fail to identify the exact derived object on which visual claims were checked. That fails C1's explicit rights-language and page-map requirements.
- **Exact correction:** Add a rights statement at the source-note acquisition block: no reproduction license or public-domain statement was observed; the public first-party route supports inspection only; no right to reproduce the photographed pages is inferred; the handbook uses independent prose. Record the derived PDF's exact hash, 13-page count, physical-to-printed page map, and render-only/non-authoritative status. Carry a short rights boundary into the presentation or ledger rather than leaving “author-hosted” to bear that meaning alone.

### AP-F2 — The ranking principle moves the target test to the wrong point and omits its exact quantification

- **Severity:** blocker
- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:439–442`; `spec/research/p09-pnueli-1977-source-note.md:94–98`.
- **Claim:** “Each transition either decreases the rank or reaches the target” is not the premise printed in P2. It suggests that the transition reaches a target at the successor. The printed disjunction tests the current state instead, and the presentation omits the `n>0` standing and the displayed rule.
- **Evidence:** Printed p. 49 introduces `A(s,n)` for a state `s` and natural number `n>0` and prints the two premises
  \[
    \varphi(s)\Rightarrow\exists n\,A(s,n),
    \qquad
    A(s,n)\land R(s,s')\Rightarrow A(s',n-1)\lor\psi(s),
  \]
  with conclusion `\varphi\leadsto\psi`. The target disjunct is `\psi(s)`, not `\psi(s')`.
- **Harm:** The current prose changes the proof obligation and leaves a first-time reader unable to reconstruct the well-founded argument. It fails C3 and the definition-before-use requirement.
- **Exact correction:** Replace the paraphrase with the exact typed P2 display, including `n>0`, all state and rank quantifiers, and the fact that either the current state already satisfies `\psi` or the successor receives rank `n-1`. If a prose gloss remains, say “while `\psi(s)` is false, every transition lowers the rank.”

### AP-F3 — ER's load-bearing induction metarule is invoked but never stated

- **Severity:** blocker
- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:444–491`; `spec/research/p09-pnueli-1977-source-note.md:100–109`.
- **Claim:** The presentation lists A1, A2, R1–R4 and first-order theorems, then says “the displayed induction” derives `P(s,n)\leadsto q`; no induction display exists. Ordinary first-order predicate-calculus theorems do not supply this integer-induction metarule.
- **Evidence:** Printed p. 50 says that the general integer induction scheme yields the special induction principle `(I)`: a base `p(0)\leadsto q` together with a derivation of `p(n+1)\leadsto q` from `p(n)\leadsto q` yields the conclusion for arbitrary `n`; R4 is then used to infer `(\exists n\,p(n))\leadsto q`. Theorem 1's eight-step completeness sketch explicitly uses `(I)` between its recurrence step and existential generalization.
- **Harm:** The handbook claims an exact ER reconstruction while omitting the rule that closes its completeness sketch. A reader cannot verify the transition from the bounded recurrence to all ranks, and the claim that the proof architecture has been delivered is false.
- **Exact correction:** Add `(I)` immediately after A1–A2/R1–R4, identify it as an integer-induction metarule rather than a new object-language connective, and state its use before R4. Then replace “the displayed induction” with an exact reference to `(I)`. Record the same rule and proof position in the source note.

### AP-F4 — The text announces quantified tense formulas but omits every printed quantifier axiom and the generalization restriction

- **Severity:** blocker
- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:539–555` and `557–597`; `spec/research/p09-pnueli-1977-source-note.md:120–143`.
- **Claim:** Line 540 says formulas use quantifiers, but the reconstructed calculus contains only the propositional G1–G3 basis, classical tautologies, modus ponens, and unrestricted-looking necessitation. It omits the source's Q1–Q4 family and its warning that generalization must be restricted when present-state facts are introduced by means other than the pure tautology rule.
- **Evidence:** Printed p. 53 gives
  \[
  \begin{aligned}
    G(\forall x\,p)&\equiv\forall x\,G(p) &&({\rm Q1}),\\
    F(\exists x\,p)&\equiv\exists x\,F(p) &&({\rm Q2}),\\
    F(\forall x\,p)&\Rightarrow\forall x\,F(p) &&({\rm Q3}),\\
    \exists x\,G(p)&\Rightarrow G(\exists x\,p) &&({\rm Q4}).
  \end{aligned}
  \]
  Printed p. 52 separately warns that rule RG (`\vdash A` to `\vdash GA`) is justified in the pure system only while present facts arise through the classical-tautology route, and must be restricted when other present-state premises are admitted.
- **Harm:** The syntax claims a quantified language for which no quantified proof theory is given, while the apparently unrestricted rule can be misapplied to system-specific or initial-state facts. This fails C5 and first-time-reader sufficiency.
- **Exact correction:** Insert Q1–Q4 exactly as source axiom schemata, state their syntactic standing, and distinguish them from Theorem 2's expressly propositional completeness claim. State RG's pure-system scope and the source's restriction warning before adding system-dependent axioms. Do not silently import a later Kripke-domain convention not specified by Pnueli.

### AP-F5 — The finite-state theorem package drops its path hypothesis, proof-system extension, generalization side condition, and adequacy clause

- **Severity:** blocker
- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:599–617`; `spec/research/p09-pnueli-1977-source-note.md:145–164`; `spec/research/p09-source-presentations-lot2-3.md:157`.
- **Claim:** The finite-state paragraph states action fairness and decidability, but it omits four load-bearing source clauses: the simplifying assumption excluding halting states and deadlocks; the initial-state axiom `(P)`; the modified generalization rule `(MRG)`; and Theorem 5's adequacy assertion for the extended system. It also changes the source's sufficient check over `p`-states into “reachable A-states” without identifying that refinement as handbook reasoning.
- **Evidence:** Printed p. 55 assumes no halting states or deadlocks so that only infinite execution paths are considered. Before Theorem 5 it adds the initial-state rule
  \[
    \frac{p(s_0)}{\vdash p}\ ({\rm P})
  \]
  and replaces RG by MRG: infer `GA` from a proof of `A` only when that proof did not use `(P)`. Theorem 5 then states both decidability of arbitrary tense-formula validity on a finite-state system and adequacy of the extended `K_b` system for all valid propositional tense formulas. Printed p. 55 describes checking each `p`-state in the graph as a sufficient route; it does not print the manuscript's reachability refinement.
- **Harm:** The theorem is presented without the conditions that keep its infinite-path semantics and generalization sound, and half of its conclusion is absent. The unlabelled reachability optimization further blurs source statement and handbook reconstruction. This fails C6 and the claimed proof-system completeness in C7.
- **Exact correction:** State the no-halting/no-deadlock assumption at the start of the specialization or explicitly totalize finite paths and label that as a handbook adaptation. Display `(P)` and `(MRG)` with the no-use-of-`(P)` proof side condition. State Theorem 5's decidability and adequacy clauses separately. Either follow the printed all-`p`-state sufficient check or label and justify restriction to states reachable from `s_0` as a handbook-derived optimization.

### AP-F6 — First-reader terminology and application coverage remain incomplete under the five-part name rule

- **Severity:** must-fix
- **Exact location:** `handbook/parts/p09/presentations/n-c-012.tex:392–400`, `407–425`, and `517–525`; `spec/research/p09-pnueli-1977-source-note.md:53–62`, `66–76`, and `111–118`.
- **Claim:** Three reader-facing qualifications are lost. First, the presentation calls the sequential model deterministic without reporting the source's explicit statement that determinism is only a notational simplification. Second, “clean execution” is listed as a technical category without definition, standing, nonredundancy, or later use. Third, “partial attachment” is named only by a possible sum-size benefit; its exact assertion form and the source's caveat that verification conditions may regain exponential complexity are absent.
- **Evidence:** Printed p. 47 says the restriction to deterministic programs is not essential and is made only to simplify notation. Printed p. 48 explains clean execution by excluding illegal intermediate operations such as zero division, overflow, and out-of-range subscripts. Printed p. 51 defines the two-process partial attachment in the form
  \[
    q(\pi_1,\pi_2;u)=
    \bigwedge_i((\pi_1=i)\Rightarrow p_i(\pi_2,u))\land
    \bigwedge_j((\pi_2=j)\Rightarrow q_j(\pi_1,u)),
  \]
  permits dependence on the other process's location, and warns that high interaction can force consideration of all opposite-process locations in the verification conditions, regaining exponential complexity.
- **Harm:** A first-time reader is left with an apparently scope-limiting determinism assumption and two technical names that fail the locally required necessity/definition/standing/nonredundancy/use package. The simplified partial-attachment claim also overstates the reliable complexity improvement. This fails C2, C4, and C8.
- **Exact correction:** Add the source's nonessential-determinism qualification. Either remove “clean execution” or define it locally as the invariant avoidance of specified illegal intermediate states and explain how it differs from partial correctness. Define partial attachment with the exact assertion family, its metalinguistic standing, its contrast with full attachment, its later role in the complexity comparison, and the high-interaction caveat. If those distinctions are not used later, describe the owed/source content without promoting unused names.

### AP-F7 — The disposition and ledger claim completion that the frozen presentation has not earned

- **Severity:** blocker
- **Exact location:** `spec/research/p09-pnueli-1977-source-note.md:3–4` and `166–179`; `spec/research/p09-source-presentations-lot2-3.md:161`; compare `handbook/parts/p09/presentations/n-c-012.tex:439–617`.
- **Claim:** The ledger says the reader presentation now defines the proof-system rules and Theorems 2–5 with their boundaries and “closes the body-level reader reconstruction.” AP-F2–AP-F6 establish that the current presentation omits or misstates several of those exact artifacts. Neither status surface distinguishes acquired-body/source reconstruction from the still-pending unanimous topic-review gate.
- **Evidence:** The ledger's line 161 makes the completion claim; the source note's disposition says the mathematical presentation is closed. The frozen presentation lacks P2's exact premise, induction `(I)`, Q1–Q4, RG/MRG restrictions, `(P)`, Theorem 5 adequacy, and the finite-path hypothesis. Charter invariants I9–I10 say N-c-012.b remains open unless every seat accepts the repaired snapshot and that even acceptance cannot close the larger row, part, build, human review, or user acceptance.
- **Harm:** The research record would certify a topic whose reader-facing proof system is incomplete, making later source audits trust a false closure boundary and inviting accidental propagation into larger completion claims.
- **Exact correction:** Change the current disposition to distinguish: (1) author-hosted printed body acquired and visually read; (2) IEEE-direct comparison open; (3) reader reconstruction and N-c-012.b topic review open pending repair and unanimous acceptance. After repair and unanimous acceptance, record only N-c-012.b topic-review closure and expressly preserve every larger open boundary in I10.

## Criterion-by-criterion coverage

- **C1 — FAIL (AP-F1).** Checked clean: registered identity, title, author, venue, year, DOI, printed pp. 46–57, NYU first-party route, compressed/decompressed hashes, wrapper/body distinction, and open IEEE-direct comparison. Not clean: explicit rights boundary and complete local-render identity/page map.
- **C2 — FAIL (AP-F5, AP-F6).** Checked clean: `\Sigma=\langle S,R,s_0\rangle`, infinite executions, possibly infinite states, nondeterministic transitions, sequential control/data split, concurrent location vector and shared data, one-statement atomic interleaving, scheduler fairness, reachable-state invariance, strict temporal implication, total correctness, accessibility, responsiveness, and the two-case scope boundary. Not clean: determinism qualification, clean-execution definition, and the finite-state no-halting/no-deadlock hypothesis.
- **C3 — FAIL (AP-F2, AP-F3).** Checked clean: invariant induction; A1, A2, R1–R4; the handbook-supplied R4 free-variable side condition and its disclosure; first-order-axiom standing; Theorem 1 sound/complete wording; proof-sketch label; expressiveness, bounded-branching, and König-lemma assumptions; and the strict/A2 tension. Not clean: exact P2 and induction `(I)`.
- **C4 — FAIL (AP-F6).** Checked clean: sequential full annotation, per-instruction verification conditions, finite-path intermittent-assertion route, concurrent full-attachment product growth, global-invariant producer–consumer example, mutual exclusion, buffer bound, deadlock argument, and later accessibility example. Not clean: exact partial-attachment standing/form and its interaction caveat.
- **C5 — FAIL (AP-F4).** Checked clean: `H(t,p)` standing; inclusive `F/G`; future-only syntax; absence of later `X/U`; G1–G3; dual `F`; classical rules; Theorem 2's propositional, external-proof boundary; I1, I2, E, N; action/fairness dependency; two-phase proof architecture; Theorem 3 representation and relative-completeness corollary; and the strict/inclusive separation. Not clean: Q1–Q4 and RG's restriction.
- **C6 — FAIL (AP-F5).** Checked clean: finite action-labelled graph, action-fair proper paths, Theorem 4 eventuality form, target deletion and SCC route, Theorem 5 decidability, and Appendix B's MSO-successor and omega-regular inclusion routes as cited sketches rather than complete constructions. Not clean: infinite-path hypothesis, `(P)`, `(MRG)`, adequacy, and disclosure of the reachability refinement.
- **C7 — FAIL (AP-F1, AP-F5, AP-F7).** Checked clean: manuscript/source-note/ledger/bibliography identity and version boundary; strict/inclusive warning; separation from GPSS, modern reused LTL, Sistla–Clarke, Büchi translation, safety/liveness, and PSPACE; no contradiction with the shared LTL/automata definitions. Not clean: provenance/rights completeness, theorem-package correspondence, and status honesty.
- **C8 — FAIL (AP-F2–AP-F7).** Checked clean: independently worded prose; exact local standing and nonredundancy for `\leadsto`, `H`, source `F/G`, designated actions, and proper executions; no silent modern repair of the source tension; no later-language retrojection; and the larger open boundaries at `n-c-012.tex:1023–1027`. Not clean: definition-before-use and five-part standing for the items identified above, plus premature closure.

## Premortem

Assume this shipped and later failed scholarly review. The failure would be traced to presenting a polished list of ER and tense axioms as if it were the complete 1977 proof apparatus while silently omitting the induction metarule, quantified axiom family, generalization restrictions, and finite-state proof-system extension; the mislocated target in P2 would then make an attempted reconstruction fail mathematically. The ledger's closure language would magnify the problem by causing later editors to stop checking the source. The ordinary C3, C5, and C6 checks caught the individual omissions; the premortem additionally exposed their systemic consequence for C7 status honesty. No separate eighth finding is needed.

## Frozen hashes rechecked after review

All charter hashes matched before substantive review and matched again after the review:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `0DADDC029C1ED7574B14BA6A48ACEBE712F93A125AD7641747E336FAE2788C19`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2`
- `spec/research/p09-pnueli-1977-source-note.md`: `539E0CEBE721A1F75D87223C41E6DEA2F139543E86EEF016750E56D169DE2D16`
- `spec/research/p09-source-presentations-lot2-3.md`: `C3ACAF3670EF0BCDB58C67138FBA68565817814F19307DF5E25F329D093D2A35`

The harness did not expose an exact runtime model/version.

## Verdict

REVISE
