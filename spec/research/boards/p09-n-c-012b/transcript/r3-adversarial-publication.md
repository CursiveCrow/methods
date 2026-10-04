REVISE

# Round-three blind adversarial publication/AGENTS review: N-c-012.b

## Opening position and steel-man

This snapshot repairs much of the mathematically dangerous material.  Against
the controlling images I confirmed the exact physical/printed page map; the
typed transition systems; reflexive reachability; clean execution; the strict
`j>i` temporal implication; literal P2, its zero-rank typing repair, and its
two-state counterexample; ER and metarule I; Theorem 1's expressiveness and
pointwise finite-branching hypotheses and its deadlock-vacuity gap; the
positive-capacity producer--consumer algebra; recursive inclusive F/G; the
initial-state present; G1--G3, F2--F3, and Q1--Q4; the literal `j>=i` action
tail; I1/I2/E/N and DI/DN; finite seriality, proper executions, P/MRG, and both
Theorem 5 clauses; Appendix A's local/external split; and all six Appendix B
language clauses.  The manuscript also keeps Pnueli's strict implication,
inclusive F, A2, and Theorem 3 representation visibly separate and does not
retroject X/U, the later LTL-to-Buchi translation, safety/liveness syntax, or
PSPACE results.

The snapshot nevertheless is not publication-ready.  Seven must-fix findings
remain.  Four concern exact local standing under the five-part technical-name
rule, and three concern the source/reconstruction/proof-ownership boundary.

## Findings

### AP-F1 — must-fix — one symbol has incompatible types in the same presentation

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:698` and
  `:865-869`.
- **Claim:** Line 698 fixes `b:S->Z` as the producer--consumer load.  Lines
  865--869 then redefine the same `b` as the action relation `{(s,s)}` and put
  it in the relation family `\mathcal A={a,b}`.  No scope boundary or explicit
  reuse separates the two declarations.
- **Evidence:** The load notation belongs to the reconstruction of printed
  pp. 51--52.  The later two-state model is a handbook counterexample to N,
  not source notation that must retain the letter `b`; printed p. 53 uses an
  action family `A_i`.
- **Harm:** A first-time reader is asked to treat `b` simultaneously as a
  state-to-integer map and a binary relation on states.  That is an actual type
  collision, not harmless formula metavariable reuse, and violates exact
  standing and definition-before-use.
- **Exact correction:** Rename the second action relation, for example
  `c={(s,s)}`, and use `\mathcal A={a,c}` throughout that counterexample.

### AP-F2 — must-fix — “full attachment” has no exact eliminable definition

- **Location:** manuscript `n-c-012.tex:661-693`; source note
  `p09-pnueli-1977-source-note.md:248-266`; ledger
  `p09-source-presentations-lot2-3.md:159`; authority printed p. 51.
- **Claim:** The manuscript says only that a full attachment has one assertion
  for every tuple and immediately uses that technical name to contrast product
  size with partial attachment.  It supplies an exact typed formula only for
  partial attachment.  The source note and ledger nevertheless characterize
  the delivery as typed full and partial attachment.
- **Evidence:** Printed p. 51 explicitly writes the two-process full form with
  one local assertion `q_ij(u)` for each pair of locations before writing the
  partial form.  The current prose omits the family type and the global
  conjunction that eliminate “full attachment.”
- **Harm:** Necessity and later use are present, but the user's Definition and
  Standing conditions are not.  The reader cannot formally compare the full
  representation with the exact partial formula, and the note/ledger overstate
  what the manuscript supplies.
- **Exact correction:** Before the partial form, introduce a collision-free
  family such as
  `r_ij:D->{false,true}` and define
  `q_full(pi_1,pi_2;u)` as the conjunction over `i in I,j in J` of
  `((pi_1=ell_i) and (pi_2=m_j)) => r_ij(u)`.  State that this is the
  metalinguistic full representation and then make the product-versus-sum
  comparison.  Keep the source note and ledger claim only after that typed
  definition exists.

### AP-F3 — must-fix — the producer--consumer characteristic maps are typed but not defined

- **Location:** manuscript `n-c-012.tex:695-729`; source note
  `p09-pnueli-1977-source-note.md:268-294`; ledger line 159; authority printed
  pp. 51--52.
- **Claim:** Lines 699--700 call `m_i,r_i,s_i` “the three source
  characteristic maps for the specified location sets,” but no location sets
  have been specified in this presentation and the source figure is neither
  reproduced nor independently reconstructed.  The subsequent proof uses the
  unstated support facts that critical-region membership forces `m_i=1`, a
  mutex wait forces `m_i=0`, and the producer/consumer semaphore waits force
  the relevant `r_i` values to zero.
- **Evidence:** Printed p. 51 introduces these as characteristic functions of
  program-location sets and then uses their location meanings in the mutual
  exclusion, bound, and deadlock argument continued on p. 52.  The current
  manuscript gives their codomains and equations but not their supports.
- **Harm:** The algebra from the three invariants is readable, but the semantic
  steps from a program-control situation to the indicator values are not
  independently checkable.  The technical maps therefore lack an exact local
  definition and the claimed “every step” reconstruction is incomplete.
- **Exact correction:** Independently reconstruct and define the three support
  sets for each process, or give an exact location/indicator table containing
  every support fact used by the proof.  If the full location reconstruction is
  intentionally outside scope, eliminate the named maps and present the
  equations plus the required indicator implications explicitly as the
  source-supplied certificate.  Update the source note/ledger delivery language
  to match whichever boundary is chosen.

### AP-F4 — must-fix — one load-bearing name is first used without a type, and one redundant name is introduced once

- **Location:** manuscript `n-c-012.tex:458-472`, `:535`, `:732-758`, and
  `:800-803`; shared scope `logic-in-computer-science.tex:599-823`; authority
  printed pp. 48 and 52.
- **Claim:** “State assertion” first appears at line 458 and supplies the atoms
  for the later tense grammar, but no local declaration states its exact type.
  The first explicit `S->{false,true}` declaration for ordinary state
  assertions occurs only in the finite-state paragraph at lines 926--929.
  Separately, line 800 introduces the one-off phrase “pure homogeneous system”
  although “pure propositional basis” has just been defined by its axioms and
  rules and is the only distinction later needed.
- **Evidence:** Printed p. 48 treats `p(s)` as a predicate on states; printed
  p. 52 distinguishes the pure tense basis from later present-only facts.  The
  scoped shared Part IX surface defines modern LTL and automata, but it does not
  provide an earlier exact definition of Pnueli's state-assertion type or of a
  “pure homogeneous system.”
- **Harm:** The first defect is definition-after-use in a grammar-bearing term.
  The second fails necessity, exact definition, nonredundancy, and later use
  under I7.
- **Exact correction:** At the first invariant discussion define a state
  assertion once as a map `S->{false,true}` (or an exactly equivalent subset of
  `S`) and reuse that standing.  Replace “pure homogeneous system” with “the
  pure propositional basis just listed”; do not create a second name.

### AP-F5 — must-fix — the exact SCC test is a handbook formalization but is presented as literal source content

- **Location:** manuscript `n-c-012.tex:938-951`; source note
  `p09-pnueli-1977-source-note.md:437-455`; ledger line 163; authority printed
  p. 55.
- **Claim:** The internal-edge condition
  `a intersect (C x C) != empty` and the two-direction condensation-graph proof
  are mathematically correct.  The printed source, however, gives an informal
  instruction to label an SCC node by actions on edges of its constituent
  nodes, followed by “not difficult to see”; it neither prints the internal-
  edge formula nor the converse proof.  The manuscript calls its version “the
  exact SCC criterion behind the source's semantic decision route” without
  identifying the formula and proof as handbook formalization/disambiguation.
- **Evidence:** Printed p. 55 contains the informal component-label sentence
  and the asserted iff.  In particular, the word “internal” and the displayed
  set condition are not source text; requiring internal edges is what makes the
  recurrent-component argument correct.
- **Harm:** The result is correct but its proof ownership is inflated.  A
  reader cannot tell which precise condition was printed and which precision
  the handbook supplied, contrary to I4 and the mandatory source/repair split.
- **Exact correction:** Introduce the display with an explicit boundary such
  as: “Interpreting the source's component-label sentence by edges internal to
  the recurrent component, the exact handbook formalization is ...”.  Label
  the following two-direction argument as handbook-supplied.  Mirror that
  boundary in the source note and ledger.

### AP-F6 — must-fix — Appendix B does not support the proof-system adequacy clause as the prose implies

- **Location:** manuscript `n-c-012.tex:969-971` and `:1004-1047`; source note
  `p09-pnueli-1977-source-note.md:423-476` and `:505-550`; ledger line 163;
  authority printed pp. 55 and 57.
- **Claim:** Theorem 5 indeed prints two clauses: semantic decidability and
  adequacy of the extended Kb calculus.  The manuscript then says Appendix B
  gives “two proof routes for Theorem 5.”  Both routes actually described on
  printed p. 57 are semantic decision routes: reduction to monadic second-order
  successor, or the omega-language inclusion decision.  Appendix B prints no
  construction of a P/MRG derivation and no completeness argument for the
  adequacy clause.
- **Evidence:** Printed p. 55 asserts both clauses and refers to Appendix B.
  Printed p. 57 develops only validity decision.  The earlier p. 55 remark that
  a proof is “not difficult” concerns the special eventuality procedure and is
  not a printed adequacy proof for every propositional tense formula.
- **Harm:** A skeptical reader is led to think both clauses receive proof
  routes.  That closes a genuine proof-status gap by phrasing rather than
  evidence.
- **Exact correction:** State after Theorem 5 that its adequacy clause is
  asserted without a printed derivation.  Retitle/rewrite the Appendix B lead
  as “two semantic decision routes for Theorem 5's decidability clause.”  Make
  the same proof-status boundary explicit in the source note and ledger.

### AP-F7 — must-fix — Appendix B overassigns the locally asserted acceptor construction to McNaughton

- **Location:** manuscript `n-c-012.tex:1013-1047`; source note
  `p09-pnueli-1977-source-note.md:514-549`; ledger line 163; bibliography
  `handbook.bib:2262-2281`; authority printed p. 57.
- **Claim:** Lines 1016--1017 correctly say Pnueli locally asserts that a
  finite-state infinite-word acceptor `A_Sigma` can be constructed and prints
  neither tuple nor acceptance condition.  Lines 1038--1044 then say Pnueli
  assigns “the acceptor construction and effective closure facts” to
  McNaughton [32].  Printed p. 57 itself introduces the `A_Sigma` construction
  as Pnueli's observation; the [32] marker accompanies the subsequent
  omega-regular-language apparatus.  Landweber [33] is the explicit owner of
  the final inclusion decision.
- **Evidence:** The ordering and citation placement on printed p. 57 distinguish
  the local `A_Sigma` assertion, the [32]-supported omega-regular construction
  and closure step, and the [33]-supported decision step.  The three relevant
  bibliography entries have the correct identities, but bibliography identity
  does not move the locally asserted observation into McNaughton's paper.
- **Harm:** The manuscript, note, and ledger contradict their own correct
  statement that Pnueli asserts `A_Sigma`, and misstate proof ownership at the
  exact boundary this round was required to audit.
- **Exact correction:** Separate the three standings everywhere: Pnueli locally
  asserts `A_Sigma` and omits its construction; [32] supports the imported
  omega-regular machinery/closure route at the point cited; [33] owns the
  inclusion-decision result.  Do not say [32] owns the `A_Sigma` construction
  unless a direct, independently verified McNaughton locator is added and the
  statement is recast as a handbook external verification rather than Pnueli's
  printed attribution.

## Criterion-by-criterion audit

- **C1 — checked clean.** The work identity, DOI, author-hosted route, May 1981
  wrapper boundary, physical-to-printed page map, independent-wording policy,
  and no-inferred-republication-right language agree across manuscript, note,
  ledger, and `Pnueli1977`.
- **C2 — checked clean apart from AP-F4's missing state-assertion type.** The
  sequential and concurrent transition maps and interleaving equation are
  typed correctly; nondeterminism and atomicity qualifications are preserved;
  reflexive reachability, clean execution, specification hierarchy, and the
  enabled-processor/action-occurrence distinction are accurate.
- **C3 — checked clean.** P1, literal P2, zero-rank repair, current-state
  `psi(s)`, strict-future counterexample, A1--A2/R1--R4, R4 hygiene, metarule I,
  Theorem 1's assumptions, proof-sketch status, and deadlock-vacuity gap all
  match printed pp. 49--50.
- **C4 — fails AP-F2 and AP-F3.** The sequential obligations, typed partial
  attachment, product/sum caveat, and positive-capacity algebra are otherwise
  accurate; the full representation and indicator supports remain
  reader-incomplete.
- **C5 — checked clean except AP-F1 and AP-F4.** Inclusive recursive F/G,
  initial present, G1--G3/F2--F3, Q1--Q4 and unresolved range, RG restriction,
  the finite action family and literal `j>=i` tail, I1/I2/E/N, DI/DN, and
  Theorems 2--3 are at their printed strengths.  The N counterexample is sound
  after its relation letter is made type-safe.
- **C6 — fails AP-F5--AP-F7.** Finite seriality, proper execution, the
  mathematical internal-edge test, P/MRG, both Theorem 5 clauses, Appendix A,
  and the six Appendix B recursion clauses are correct.  The remaining defects
  are disclosure and proof/external ownership, not the displayed mathematics.
- **C7 — fails AP-F2, AP-F3, AP-F5--AP-F7.** Source note and ledger repeat the
  overbroad “typed full attachment,” complete producer reconstruction, literal
  SCC, whole-Theorem-5 proof-route, and McNaughton-ownership claims.  The three
  bibliography identities themselves are consistent with printed references
  32--33.
- **C8 — fails AP-F1--AP-F4 and AP-F5--AP-F7.** The prose is independently
  worded and the later-result/version boundaries are otherwise excellent, but
  definitions, standing, nonredundancy, and source/handbook ownership are
  publication conditions, not optional polish.

## Invariant-by-invariant audit

- **I1:** complied with.  I used visual source reading, ordinary read-only text
  inspection, and SHA-256 identity hashing only.  I ran no tests, harnesses,
  automated checkers, repository scripts, TeX, handbook-PDF inspection, or
  builds.
- **I2:** complied with.  Every round-three identity matched both before
  substantive review and immediately before this filing.
- **I3:** complied with.  I visually read wrapper physical page 1 for
  provenance and physical pages 2--13, i.e. every printed page 46--57, for
  substance.  Images, not OCR or memory, controlled all source findings.
- **I4:** fails AP-F2--AP-F7; the remaining rule premises, types, quantifiers,
  side conditions, theorem statements, and locators checked clean.
- **I5:** checked clean.  Strict temporal implication, A2, inclusive F, and the
  Theorem 3 representation remain expressly unreconciled.
- **I6:** checked clean.  No X/U grammar, later Buchi translation,
  safety/liveness syntax, or PSPACE classification is attributed to Pnueli.
- **I7:** fails AP-F1--AP-F4.  Other introduced names (`leadsto`, clean
  execution, partial attachment, proper execution, `L_prop`, prefix
  concatenation, and the eliminable omega-regular label) have local standing
  and actual use.
- **I8:** checked clean.  The author-hosted body is sufficient for this
  reconstruction while IEEE-direct comparison remains open.
- **I9:** checked clean.  Manuscript, note, and ledger keep the topic open and
  do not invoke majority rule.
- **I10:** checked clean.  The status does not claim closure of the rest of
  N-c-012, Part IX, builds, handbook visual review, human review, user
  acceptance, or final publication.

## Mandatory fresh-check inventory

I independently checked the wrapper; every page locator; rights/version
language; both transition models; R-star; clean execution; both fairness
formulations; P2 and its counterexample; ER/I/Theorem 1; both attachment
styles; the complete displayed producer algebra; recursive F/G and the initial
present; G1--G3/F2--F3/Q1--Q4; RG; action partition and inclusive tail; all six
system-dependent/derived rules; Theorems 2--3; finite seriality/proper paths;
SCC recurrence; P/MRG; both Theorem 5 clauses; every Appendix A formula and the
six-step local lemma; both Appendix B routes, all six recursion clauses and
their set types; omega-regular standing; references 32--33; all scoped shared
Part IX surfaces; all three bibliography entries; and adjacent Kamp, GPSS, and
Sistla--Clarke boundaries.  No additional unlisted uncertainty was used to
support this verdict.

## Premortem

If this topic shipped unchanged and failed scholarly review, the likeliest
cause would be that its equations looked exact while the prose quietly claimed
more: an undefined full-attachment representation and indicator semantics, an
Appendix that appeared to prove adequacy but only decided validity, and an
external attribution broader than the printed citation placement.  An ordinary
formula-only checklist would miss all three; the standing-and-proof-ownership
pass exposed them.

## Identity verification

The following eight hashes matched the charter before substantive review and
again immediately before filing:

- `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
  — `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`
- `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
  — `tmp/pdfs/p09-pnueli-1977/focs77.ps`
- `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
  — `tmp/pdfs/p09-pnueli-1977/focs77.pdf`
- `80F9D4B96FEEBD329F683D5048E31544EDD4A97B3922752AC3D17DAB851D9219`
  — `handbook/parts/p09/presentations/n-c-012.tex`
- `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
  — `handbook/parts/p09/logic-in-computer-science.tex`
- `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
  — `handbook/bib/handbook.bib`
- `BC88DE02A62B27112B723548D1483D2E8525CFB0EF175273DE4D15A3EAAB5BBF`
  — `spec/research/p09-pnueli-1977-source-note.md`
- `5FF3CCC5C8B88882D9218BB4221AEFAEB313EFF15657BCDB427C25F9F6852714`
  — `spec/research/p09-source-presentations-lot2-3.md`

## Independence, authority, and runtime record

I read the complete charter and its appended round-three snapshot before
substantive review.  I did not inspect `ledger.md`, `transcript/chair.md`, any
round-one or round-two transcript (including my own), or any other seat's
round-three transcript.  I did not contact another reviewer.  I made no edit
outside this assigned transcript.

Authority visually read: wrapper physical page 1 for provenance, then printed
pp. 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, and 57 in physical pages
2--13.  The runtime harness did not expose an exact model/version identifier.

## Final verdict

REVISE
