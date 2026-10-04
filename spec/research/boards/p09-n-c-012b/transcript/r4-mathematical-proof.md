REVISE

# Round-four mathematical/proof review — N-c-012.b

Reviewer: `/root/p09_math_proof_review`  
Seat: mathematical and proof correctness  
Runtime model/version: the harness did not expose an exact runtime model or version.

## Verdict basis

The frozen presentation is substantially stronger than the preceding snapshot: the program and path types, two fairness standings, full/partial attachment distinction, attachment-size parameters, finite-system validity, internal-edge SCC characterization, Theorem 5 proof boundary, and Appendix B attribution split are now clear. It nevertheless retains four must-fix mathematical defects and one local type defect. In particular, the zero-rank extension makes literal P2 unsound for a reason independent of the already recorded strict-future counterexample, and the claimed S4 completeness is not completeness for the linear execution semantics that the manuscript has just defined. Under the charter, either defect alone requires `REVISE`.

## Findings

### MP-F1 — must-fix — the zero-rank typing extension leaves P2 unsound even under inclusive eventuality

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:501-536`; `spec/research/p09-pnueli-1977-source-note.md:139-179`; `spec/research/p09-source-presentations-lot2-3.md:157,165`; printed source p. 49.
- **Claim presently made:** the manuscript extends the second argument of \(A\) to \(0\), quantifies rule instances by \(n>0\), and treats the remaining defect as the conflict between current-state \(\psi(s)\) and strict \(j>i\).
- **Evidence and derivation:** the displayed premises also admit
  \[
    S=\{a,b\},\quad s_0=a,\quad
    R=\{(a,b),(b,b)\},
  \]
  with \(\varphi\) true only at \(a\), \(\psi\) false everywhere, and \(A\) true exactly at \((a,1)\) and \((b,0)\). The first premise holds. For the only positive-ranked antecedent, \(A(a,1)\land R(a,b)\), the disjunct \(A(b,0)\) makes the second premise true; all other positive-rank antecedents are false. Nevertheless no state on the unique execution satisfies \(\psi\). Thus the displayed P2 is invalid even if “eventually” includes the present. The source's statement that the rank is positive does not supply a truth value for the printed \(A(s',n-1)\) at \(n=1\); the handbook's totalization supplies that value but supplies no false-at-zero boundary.
- **Mathematical harm:** P2 is not a valid well-founded-ranking rule as typed. The current prose incompletely diagnoses the source/repair boundary by recording only the current-state/strict-future counterexample.
- **Exact correction:** retain the existing strictness counterexample, and add this independent zero-rank counterexample and source-gap disclosure in all three evidence surfaces. If the reader also wishes to display a sound handbook repair, add the explicitly handbook-supplied premise
  \[
    \forall s\in S\;\neg A(s,0),
  \]
  or replace the decrease disjunct by
  \[
    (n>1\land A(s',n-1))\lor\psi(s).
  \]
  Do not attribute either boundary condition to p. 49, which prints neither.

### MP-F2 — must-fix — R4 and metarule I are not typed by the preceding definition of a state assertion

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:458-460,538-588`; `spec/research/p09-pnueli-1977-source-note.md:108-112,181-202`; ledger summary `spec/research/p09-source-presentations-lot2-3.md:157`; printed source pp. 49-50.
- **Claim presently made:** a state assertion has type \(S\to\{\mathsf{false},\mathsf{true}\}\), after which R4 forms \(\exists u\,p\) and metarule I forms \(p(0),p(n),p(n+1)\).
- **Evidence:** a map \(p:S\to 2\) has neither a free object variable \(u\) nor a natural-number argument. The stated free-variable hygiene for \(q\) is necessary but does not construct the missing parameter domain, assignment semantics, pointwise existential, or natural-indexed family. Therefore R4 and I are not formulas/rules over the type just defined.
- **Mathematical harm:** the existential rule, the induction metarule, and the R4 step in Theorem 1's proof chain are not well-formed in the reader's own semantics.
- **Exact correction:** type the special uses without inventing an unexplained name. For R4, fix a nonempty domain \(U\), take \(p:S\times U\to2\) and \(q:S\to2\), put \(p_u(s)=p(s,u)\), and define
  \[
    (\exists_U p)(s)\Longleftrightarrow\exists u\in U\;p(s,u).
  \]
  State that the premise is a derivation uniform in the arbitrary \(u\) and that \(q\) is independent of \(u\). For I, take \(p:S\times\mathbb N_0\to2\), define \(p_n(s)=p(s,n)\), and state the base, successor-under-hypothesis, and arbitrary-\(n\) conclusion with those maps. Then the later existential is the already typed pointwise map \(s\mapsto\exists n\,p(s,n)\). An alternative is a full first-order assertion syntax plus assignment semantics, but merely saying “\(u\) is not free in \(q\)” is not a type repair.

### MP-F3 — must-fix — the mutex-deadlock calculation uses an indicator implication that the repaired list omits

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:725-739,756-763`; `spec/research/p09-pnueli-1977-source-note.md:283-315`; ledger `spec/research/p09-source-presentations-lot2-3.md:159`; printed source pp. 51-52, especially p. 52's continuation of the deadlock proof.
- **Claim presently made:** lines 733-739 say that the listed indicator consequences are *all* those used. The proof then obtains \(m_{3-i}=1\) from the first invariant and concludes that the other process is in its critical region and hence is not blocked.
- **Evidence:** the list supplies “critical-region membership implies \(m_i=1\)” and “blocked on MUTEX implies \(m_i=0\) and \(\mu=0\).” Neither licenses the reverse step \(m_{3-i}=1\Rightarrow\) critical-region membership. Printed p. 52 explicitly makes that additional interpretation: after obtaining \(m_2=1\), it says this means processor 2 is in its critical section and cannot be waiting on a semaphore operation.
- **Mathematical harm:** as written, the exclusion of the mutex/mutex deadlock case contains an unsupported converse, and the cross-file claim that every used indicator fact is stated is false.
- **Exact correction:** add, at the existing list, the source-supplied fact that \(m_i=1\) means process \(i\) is at its critical-section location and therefore is not waiting on a semaphore operation. Keep this weaker implication-level statement; do not invent an unprinted complete support set. Mirror the repair in the source note and ledger.

### MP-F4 — must-fix — Theorem 2's S4 referral does not prove completeness for the preceding linear execution semantics

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:767-845`; `spec/research/p09-pnueli-1977-source-note.md:317-371`; ledger `spec/research/p09-source-presentations-lot2-3.md:161`; printed source pp. 52-53.
- **Claim presently made:** after defining \(F,G\) on a single linearly ordered execution, the manuscript reports the G1-G3/RT/RG/MP basis and says Theorem 2 calls that pure propositional fragment complete in the absolute sense, with an S4 correspondence.
- **Evidence:** G1-G3 with necessitation and modus ponens are the S4 basis, complete for reflexive-transitive Kripke frames, not for the narrower class of linear futures just defined. For example,
  \[
   (Fp\land Fq)\Rightarrow
   \bigl(F(p\land Fq)\lor F(q\land Fp)\bigr)
  \]
  is valid on every linear future: compare a future \(p\)-position with a future \(q\)-position, and use whichever comes first. It fails on the reflexive-transitive branching frame having a root with two incomparable reflexive terminal successors, one satisfying only \(p\) and the other only \(q\). Hence it is not an S4 theorem. Printed p. 53 itself makes the S4 identification and refers the completeness proof outward; it does not reconcile that modal frame class with p. 52's single-execution semantics.
- **Mathematical harm:** the reader leaves the model class of “complete” unstated at the exact point where the two possible readings have different valid formulas. A reader can incorrectly infer a completeness theorem for the displayed execution semantics.
- **Exact correction:** state Theorem 2 only as the source's referred, model-class-sensitive completeness assertion. Explicitly say that the S4 referral establishes no completeness result for the preceding linear-word semantics and that the paper does not reconcile the two readings. Do not repair the linear calculus by adding a new axiom or later theorem unless a primary authority for that separate result is introduced and its standing is kept distinct.

### MP-F5 — should-fix — the atomic Appendix B language is not literally in the declared concatenation domain

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:1084-1095`; `spec/research/p09-pnueli-1977-source-note.md:572-584`; printed source p. 57.
- **Claim presently made:** the manuscript defines concatenation only for \(U\subseteq S^*\) and \(V\subseteq S^\omega\), but defines \(\llbracket p\rrbracket\subseteq S\) and immediately writes \(L(p)=\llbracket p\rrbracket S^\omega\).
- **Evidence:** without an explicit one-letter-word identification, the first factor has type \(\mathcal P(S)\), not the stated concatenation input type \(\mathcal P(S^*)\).
- **Mathematical harm:** the attempt to make p. 57's informal regular-expression notation typed still contains one missing coercion.
- **Exact correction:** state explicitly that each \(s\in S\) is identified with the one-letter word \((s)\in S^1\subseteq S^*\), or replace the first factor by \(\{(s)\in S^1:p(s)\}\). No new technical name is required.

## Mandatory F27-F35 fresh checks

- **F27 — checked clean:** manuscript lines 848-904 use \(a,c\subseteq S\times S\) as action relations; the producer-consumer load is the separately typed \(b:S\to\mathbb Z\). The raw-path counterexample satisfies the partition equations and both N premises while violating the conclusion without the action condition.
- **F28 — checked clean:** lines 664-686 give a typed \(h_{ij}:D\to2\), the exact double-indexed full-attachment formula, its metalinguistic standing, its distinction from partial attachment, and immediate use in the size comparison.
- **F29 — not resolved:** MP-F3 identifies the one source-supplied implication still used but omitted.
- **F30 — not fully resolved:** the base state assertion is defined before ordinary use, but MP-F2 shows that its type does not cover R4 or I. I found no separate redundant one-off technical name.
- **F31 — checked clean:** lines 955-979 distinguish arbitrary-start action-satisfying paths, initial-state proper executions, and the system/formula relation \(\models_{\rm prop}\); Theorems 4-5 and Appendix B use the intended standing consistently.
- **F32 — checked clean:** lines 688-719 distinguish two-process sum-size syntax, product expansion, and process-count exponential growth, and retain initial-state and per-transition invariant obligations.
- **F33 — checked clean:** lines 992-1011 give the exact internal-edge condition \(a\cap(C\times C)\ne\varnothing\) for every action and explicitly mark both directions as handbook-supplied. The repeated closed-walk and condensation-DAG arguments are correct.
- **F34 — checked clean:** lines 1029-1034 say the paper merely asserts adequacy and gives no general derivation; lines 1067-1113 limit Appendix B to semantic routes for decidability.
- **F35 — checked clean:** lines 1073-1110 keep three standings separate: Pnueli's local unproved proper-execution acceptor assertion, reference 32's imported omega-regular/closure machinery, and reference 33's inclusion decision.

## Criterion-by-criterion coverage

- **C1 — checked clean:** wrapper provenance, 1977 body identity, physical/printed page map, DOI/access route, rights language, author-copy standing, and open IEEE comparison agree across manuscript 372-382 and 1519-1526, source note 7-52, ledger 153, and the bibliography entry.
- **C2 — checked clean:** the tuple, sequential and concurrent transition equations, atomic interleaving, infinite execution, reflexive \(R^*\), reachable set, invariant/clean-execution distinction, strict temporal implication, and informal-enabled versus formal-action fairness distinction are correctly typed and source-located at manuscript 384-490. The later arbitrary-start/initial-path distinction is also correct.
- **C3 — revise:** P1, literal current-state P2, strict counterexample, A1-A2/R1-R3, pointwise finite branching, König step, and Theorem 1's deadlock-vacuity gap are accurately reconstructed. MP-F1 and MP-F2 remain fatal defects in P2's zero boundary and R4/I typing.
- **C4 — revise:** the sequential Floyd obligations, finite-path A1/R2 composition, full and partial concurrent attachments, and attachment-size parameterization are correct. MP-F3 leaves one producer-consumer inference unsupported; all other displayed arithmetic steps, including \(0\le b\le C\) and the positive-capacity contradiction, check.
- **C5 — revise:** recursive inclusive \(F/G\), absolute present, G1-G3, F2-F3, Q1-Q4 strengths, unresolved quantifier semantics, RG restriction, finite action tail with \(j\ge i\), I1/I2/E/N, DI/DN, and Theorem 3's skeletal proof boundary are accurate. MP-F4 leaves Theorem 2's completeness model class mathematically unresolved.
- **C6 — revise only for MP-F5's local type:** finite seriality, proper execution, reachable-state refinement, SCC iff proof, P/MRG separation, both Theorem 5 clauses, Appendix A's proof ownership, and Appendix B's two semantic routes all check. The language recursion is semantically right after the missing one-letter coercion is supplied.
- **C7 — revise:** the bibliography and shared Part IX surfaces are internally consistent and later results remain separately attributed, but each of MP-F1 through MP-F5 is repeated or summarized on an evidence surface that must be repaired with the manuscript.
- **C8 — revise:** the prose is independently worded, narrow in closure, and generally complies with the five-part technical-name rule. The failures are mathematical/type failures rather than prose reuse; MP-F2 also prevents the claimed definition-before-use discipline from being complete.

## Invariant-by-invariant coverage

- **I1 satisfied:** I performed source-image reading, mathematical reconstruction, and prose review only. I ran no tests, automated checker, repository script, TeX, handbook-PDF inspection, or build.
- **I2 satisfied:** every round-four identity matched both before substantive review and at the second gate immediately before filing; exact values are recorded below.
- **I3 satisfied:** I visually read the provenance wrapper and every printed body page 46-57. The page images, not OCR or memory, controlled source readings.
- **I4 failed:** MP-F1, MP-F2, MP-F3, MP-F4, and MP-F5 are remaining rule-boundary, type, premise, theorem-strength, or local-language defects.
- **I5 satisfied:** strict temporal implication, A2, inclusive F, and Theorem 3's representation remain explicitly distinct, with no silent normalization.
- **I6 satisfied:** no next/until grammar, later LTL-to-Büchi construction, safety/liveness syntax, or PSPACE result is attributed to Pnueli 1977.
- **I7 satisfied except for the type failure in MP-F2:** the newly introduced reader names otherwise have local necessity, exact definition, standing, nonredundancy, and use. The exact repair to MP-F2 can be made without naming a new construct.
- **I8 satisfied:** author-copy reconstruction and the still-open IEEE comparison are distinct.
- **I9 satisfied:** the ledger keeps the topic open pending fresh unanimity; this verdict supplies no majority override.
- **I10 satisfied:** the stated closure boundary is only N-c-012.b topic review and leaves N-c-012, Part IX, builds, handbook visual review, human/user review, and final publication open.

## Identity gates, authority reading, and independence

The following identities matched the charter before substantive reading and again after the complete review, immediately before this transcript was filed:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex` — `B015988618D84AA836D35D3AA0A1D484438C65910B78BB94CB74577A9FB02C9E`
- `handbook/parts/p09/logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib` — `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md` — `C3EE541610841D57A6FB6729C482919431660CFF896276FDABB330D9D21ADE54`
- `spec/research/p09-source-presentations-lot2-3.md` — `32F11A80F21E9C33AF3E664EBDEEB778E36B4B81E7A772C5BD91589090962AA0`

I visually read physical page 1 only for wrapper provenance and physical pages 2-13 as printed authority pages 46-57. I read the complete round-four manuscript scope (`n-c-012.tex:370-1114,1519-1526`), shared scope (`logic-in-computer-science.tex:599-823`), full source note, ledger 151-167, the three scoped bibliography entries, and adjacent boundaries needed to exclude conflation.

I did not inspect the board ledger, chair record, any r1/r2/r3 transcript, or any other r4 transcript; I did not contact another reviewer or use another reviewer's conclusions. I edited only this assigned transcript. No test, checker, harness, repository script, TeX command, handbook-PDF inspection, or build was run. Source-image viewing and SHA-256 identity hashing were the only mechanical operations.

## Narrow closure boundary

This `REVISE` applies only to the round-four N-c-012.b snapshot at the identities above. It neither adjudicates an IEEE-direct copy nor closes another N-c-012 presentation, Part IX, a build/visual gate, human review, user acceptance, or final publication.

REVISE
