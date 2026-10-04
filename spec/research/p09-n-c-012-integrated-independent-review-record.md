# N-c-012 integrated independent direct-LaTeX review record

## Admission scope

This record admits the integrated reader-facing presentation in
`handbook/parts/p09/presentations/n-c-012.tex` at its stated source and
mathematical strength. The admitted unit contains five deliberately distinct
presentations: Kamp on strict tense expressiveness, Pnueli on transition-system
proof methods, GPSS on strict temporal expressiveness and proof systems,
Sistla--Clarke on operator-sensitive decision complexity, and
Alpern--Schneider on semantic safety and liveness properties. The relevant
integration passages in
`handbook/parts/p09/logic-in-computer-science.tex` are included in the scope.

This is a narrow manuscript-content admission. It does not admit Part IX as a
whole, another presentation, another handbook part, final typesetting, human or
user review, final-book completion, or publication.

## Direct-source review protocol

Three fresh blind seats independently read the complete actual manuscript
source, `n-c-012.tex` lines 1--3060, and the relevant actual host-chapter
LaTeX. No seat used a manuscript PDF, page image, PNG render, build, test,
checker, repository script, or hash. Layout was outside the round and supplied
no evidence. The source-fidelity seat compared the LaTeX with the current
presentation source notes; those records resolved every question, so it did
not need to reopen a historical-source file.

The target LaTeX and host-chapter integration remained unchanged throughout
the round. The three reports were kept separate until every seat had filed:

| Seat | Report | Verdict |
|---|---|---|
| source fidelity and integration | `p09-n-c-012-integrated-source-review-r5.md` | **ACCEPT** |
| mathematical and proof coherence | `p09-n-c-012-integrated-mathematical-review-r5.md` | **ACCEPT** |
| adversarial publication and terminology | `p09-n-c-012-integrated-publication-review-r5.md` | **ACCEPT** |

Each report was then read completely by the chair. None contains a blocker,
qualification disguised as acceptance, unread manuscript passage, or reliance
on a rendered manuscript artifact.

## Integrated review history

The final acceptance was not carried forward from an earlier manuscript state.

1. Round 1 exposed defects in the final cross-presentation boundary and in
   publication terminology.
2. Round 2 retained a publication rejection for residual workflow language and
   an underdefined regular-operator presentation.
3. Round 3 exposed the missing exact standing of bare \(K_b\) and the
   unhandled empty-emission case in the ETL proof surface.
4. Round 4 accepted the then-current source and mathematical repairs but found
   that the Sistla--Clarke NP certificate still assigned one truth set per
   graph node although a repeated prefix node can have different temporal truth
   at different occurrences.
5. Round 5 reviewed the occurrence-sensitive repair, all earlier repairs, and
   the complete integrated presentation directly in LaTeX. All three seats
   returned **ACCEPT**.

## Controlling determinations

- Kamp's two translation directions retain their unequal order hypotheses,
  and the repaired sparse-square induction is labelled as handbook-owned.
- Pnueli's \(K_b\) is exactly the pure theorem system with derived \(F\),
  G1--G3, and RT/RG/MP. It does not silently contain the system-dependent rule
  E. The source's skeletal claim that \(K_b\) subsumes ER is therefore recorded
  as under-specified rather than promoted to a proved embedding.
- GPSS's strict operators, result domains, unprinted proof steps, external
  referrals, and conflicting \(U^0\) displays remain separate from the
  handbook's inclusive discrete bridge.
- Sistla--Clarke's NP witness uses one \(\mathcal L_i\) for each prefix
  occurrence and a separate \(\mathcal L_C(x)\) for each recurrent node. The
  repeated-node counterexample proves that distinction necessary. Inclusive
  eventuality, the directed-cycle repair, the recurrent suffix visiting every
  node of \(C\) infinitely often, structural induction, and the polynomial
  certificate count form one coherent argument.
- The ETL reconstruction is explicitly limited to nonempty emissions because
  the printed proof rules supply no epsilon case. One-terminal normalization
  and the PSPACE statement are confined to that repaired domain.
- Alpern--Schneider's objects remain semantic subsets of \(S^\omega\), not
  formula classes. The topology arguments, cardinality hypothesis, and printed
  Corollary 2.1 defect retain their exact source and handbook ownership.
- The closing five-way boundary prevents any presentation from retroactively
  supplying another's syntax, semantics, proof rules, theorem strength, or
  terminology.

## Disposition

Integrated `N-c-012` is admitted for source fidelity, mathematical and proof
coherence, terminology, and reader-facing manuscript content. Part IX remains
open. The manuscript PDF will be built and inspected only once, after all
fourteen parts are text-frozen, solely for publication layout.
