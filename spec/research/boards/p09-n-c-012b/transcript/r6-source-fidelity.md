ACCEPT

# Round-six blind source-fidelity review: N-c-012.b

## Opening position

I found no source-fidelity blocker, must-fix defect, unsupported source
attribution, or unresolved evidentiary uncertainty in the complete round-six
scope.  The verdict applies only to the eight round-six identities listed in
the charter and only to the narrow N-c-012.b topic-review gate.

Reviewer seat: `/root/schmidt_smolka_1991_research` (source fidelity).

Runtime model/version: the review harness did not expose a runtime model or
version.

## Independence and method record

- I read the charter before substantive work and used only its round-six
  repaired snapshot as the controlling scope.
- I did not inspect `spec/research/boards/p09-n-c-012b/ledger.md`,
  `transcript/chair.md`, any earlier-round transcript, or either other
  round-six transcript.  I did not contact another reviewer.
- I visually read the provenance wrapper and all twelve printed body pages
  46--57 from the source images.  The images, not OCR or memory, controlled
  every substantive comparison.
- I read the complete frozen reader scope at
  `handbook/parts/p09/presentations/n-c-012.tex:370--1204,1610--1617`, the
  complete shared scope at
  `handbook/parts/p09/logic-in-computer-science.tex:599--823`, the entire
  source note, the presentation ledger at lines 151--167, the complete
  `Pnueli1977`, `McNaughton1966`, and `Landweber1969` bibliography entries,
  and adjacent presentation text on both sides of N-c-012.b.
- I made no manuscript, source-note, ledger, bibliography, or shared-surface
  edit.  This transcript is the only file I created.  I ran no tests, test
  harnesses, automated checkers, repository scripts, TeX, handbook-PDF
  inspection, or build.  The only executable inspection was ordinary
  read-only file reading and SHA-256 identity hashing, as the charter requires.

## Hash verification before review and immediately before filing

All eight identities matched the round-six charter both before substantive
review and immediately before this transcript was filed:

| Frozen object | SHA-256 |
|---|---|
| `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz` | `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB` |
| `tmp/pdfs/p09-pnueli-1977/focs77.ps` | `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F` |
| `tmp/pdfs/p09-pnueli-1977/focs77.pdf` | `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `3A4ECE9251B46ACAD8925FFCD34162BE3F9741C09DF912B70967C8FAAB7BE1BC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394` |
| `handbook/bib/handbook.bib` | `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9` |
| `spec/research/p09-pnueli-1977-source-note.md` | `86EA6E1F4934B61D5D7E517C01466D6CDA98F80348B1233D52F953F9B1A821CA` |
| `spec/research/p09-source-presentations-lot2-3.md` | `05931057A05C0DCD81507394AF6152B02C3BC12B7E5A7E7AAB757A84A4B1F5C9` |

## Authority pages visually read

- Wrapper, physical page 1: title and author with the archival date “May
  1981.”  It is provenance packaging and contains no replacement mathematical
  body.
- Printed p. 46, physical page 2: title, author, affiliations, summary,
  partial correctness, clean execution, termination/eventuality motivation,
  and the beginning of the dynamic-system model.
- Printed p. 47, physical page 3: the dynamic discrete system, infinite
  initial-state execution, exact sequential transition equation, exact
  concurrent interleaving equation, nonessential determinism qualification,
  atomic-step granularity, and enabled-processor scheduling prose.
- Printed p. 48, physical page 4: the time-variable hierarchy, reachable-state
  invariance and clean execution, strict temporal implication with `j>i`, and
  the specification hierarchy and exclusions.
- Printed p. 49, physical page 5: P1, literal P2 with positive rank,
  decrement to rank zero, and current-state `psi(s)`, together with ER A1--A2
  and R1--R4.
- Printed p. 50, physical page 6: predicate-calculus axioms, induction
  metarule I, Theorem 1 and its labelled completeness proof sketch,
  finite-branching/König step, sequential attachment, Floyd obligations, and
  the finite-path ER account.
- Printed p. 51, physical page 7: concurrent full and partial attachment,
  the interaction/size discussion, and the producer--consumer example and
  three invariants.
- Printed p. 52, physical page 8: completion of the positive-capacity
  producer--consumer calculation, future-tense motivation, inclusive F/G
  semantics, absolute present at `s_0`, G1--G3, F2--F3, RT/RG/MP, and the RG
  warning.
- Printed p. 53, physical page 9: Q1--Q4, Theorem 2 and its external
  completeness/decidability referrals, I1/I2/E, the finite action partition,
  the literal action-occurrence tail condition, and N.
- Printed p. 54, physical page 10: N examples, Theorem 3 and its skeletal
  proof, relative-completeness corollary, DI/DN, and the mutual-exclusion
  accessibility example.
- Printed p. 55, physical page 11: finite serial systems, proper executions,
  Theorem 4 and the SCC decision route, P/MRG, both Theorem 5 clauses, and the
  Appendix B referral.
- Printed p. 56, physical page 12: discussion, scope qualifications, and
  references 1--20.
- Printed p. 57, physical page 13: references 21--33, Appendix A's externally
  owned T2/T3 package and local six-step lemma proof, and Appendix B's two
  decision routes, atomic-language recursion, and references 32--33.

The source note's physical/printed map and visual-locator table at lines 25--52
match this fresh image inspection exactly.

## Findings

No `SF-F*` finding is opened.  The complete source correspondence is checked
clean below.

## Mandatory F27--F43 fresh checks

### F27--F35

- **Action/load typing:** reader lines 937--997 use `a,c` only as binary
  action relations and give a well-typed raw-path counterexample.  Reader lines
  781--828 separately use `b:S\to\mathbb Z` for buffer load.  There is no
  symbol-standing collision.  Printed pp. 51--53 support the two independent
  source contexts.
- **Full attachment:** reader lines 724--746 give the exact pair-indexed typed
  formula, state its metalinguistic standing, distinguish it from partial
  attachment, and use that distinction immediately in the size comparison at
  lines 748--779.  This matches printed p. 51.
- **Producer indicators:** reader lines 781--827 state only the indicator
  consequences actually used on printed pp. 51--52.  In particular, lines
  794--800 include both critical membership implying `m_i=1` and the source's
  later use of `m_i=1` to infer critical-section membership and nonwaiting.
  No complete unprinted support set is fabricated.
- **State-assertion standing:** reader lines 459--462 type a state assertion
  before the rules use one.  Parameterized assertions, tense formulas, action
  relations, program variables, and metalinguistic abbreviations remain
  distinct throughout.
- **Path standings:** reader lines 1037--1069 distinguish an arbitrary-start
  infinite action-satisfying path, a proper execution beginning at `s_0`, and
  the system/formula relation `\Sigma\models_{\rm prop}A`.  All three are
  defined before their later use and agree with the initial-state standing of
  printed pp. 47, 52, and 55.
- **Attachment-size parameterization:** reader lines 768--779 correctly give
  the two-process sum versus product comparison and reserve exponential growth
  for a varying number of processes.  It retains the initial and per-transition
  invariant obligations rather than treating concise global notation as a
  proof.  This is the warranted reading of printed p. 51.
- **SCC reconstruction:** reader lines 1071--1101 identify the source's
  component-label sentence, explicitly mark the internal-edge formula and both
  proof directions as handbook-supplied, and prove the finite SCC criterion
  correctly.  Printed p. 55 does not receive unprinted proof ownership.
- **Theorem 5 boundary:** reader lines 1119--1124 state both literal clauses,
  disclose that the adequacy construction is not printed, and restrict
  Appendix B to the decidability clause.  This matches printed p. 55.
- **Appendix B ownership:** reader lines 1157--1204 keep three standings
  separate: Pnueli's local but unproved proper-execution acceptor assertion,
  reference 32's imported infinite-word regularity/closure route, and reference
  33's inclusion decision.  Printed p. 57 and bibliography entries
  `McNaughton1966` and `Landweber1969` support those boundaries.

### F36--F40

- **P2:** reader lines 501--552 preserve the literal current-state target and
  strict `j>i` conclusion, disclose only a typing totalization at rank zero,
  and demonstrate two independent failures.  In the first two-state system,
  `A(a,1)` and `A(b,0)` satisfy the premises although the false target is never
  reached; the unprinted `\forall s\,\neg A(s,0)` boundary is sufficient only
  for inclusive eventuality.  In the second system, current `psi(a)` discharges
  the premise while no strictly later target exists.  Both counterexamples are
  valid, and printed p. 49 is neither strengthened nor silently repaired.
- **Typed R4:** reader lines 554--606 use one family
  `\widehat p:S\times U\to\{false,true\}`, define its sections and pointwise
  existential, state that the latter is a state assertion rather than a tense
  constructor, and disclose the uniform arbitrary-parameter and
  consequent/open-assumption independence conditions as handbook typing.  This
  is a faithful typed reconstruction of printed pp. 49--50.
- **Typed metarule I:** reader lines 608--627 specialize that same family to
  `\mathbb N_0`, distinguish the temporary-hypothesis derivation from the
  arbitrary-index conclusion, and apply typed R4 only after induction.  The
  Theorem 1 account at lines 629--648 uses the same state-assertion standing.
- **Producer implication:** reader lines 791--800 include the source's actual
  `m_i=1` inference without inventing an indicator support table; the resulting
  mutex and deadlock deductions at lines 811--827 are exactly those printed on
  pp. 51--52.
- **Theorem 2 model-class qualification:** reader lines 830--905 first give
  the inclusive linear-execution semantics and literal source/referral status.
  Lines 907--935 then demonstrate, rather than merely assert, the
  linear-versus-branching mismatch.  The qualification is neither stronger nor
  weaker than the evidence permits.
- **One-letter typing:** reader lines 1174--1187 identify each state with a
  one-letter word, type finite-prefix/infinite-tail concatenation, and thereby
  make `L(p)=\llbracket p\rrbracket S^\omega` exact.  This is a disclosed typed
  rendering of printed p. 57, not a new source claim.

### F41: Theorem 1's unreachable-state gap

Reader lines 629--648 faithfully report the printed p. 50 proof sketch:
`p\leadsto q` is defined over executions beginning at `s_0`, while the proof's
`P(s,n)` quantifies over executions beginning at an arbitrary state `s`.  The
new reader counterexample at lines 650--665 is correct:

- `R={(s_0,s_0),(u,u)}` is serial, and every state has exactly one successor,
  so it is pointwise finitely branching.
- `p` holds only at unreachable `u`; hence the sole system execution from
  `s_0` never triggers `p`, so the printed `p\leadsto q` clause is true.
- `q` is false everywhere; the unique path beginning at `u` is
  `u,u,\ldots`, so no finite bound reaches `q` and every `P(u,n)` is false.

The three missing-boundary alternatives at reader lines 663--665 are each
sufficient for this reachability mismatch: require `S=X`, restrict the
assertion/rule semantics consistently to `X`, or quantify the theorem's
execution semantics over every start state.  The prose attributes none to
Pnueli and does not claim that any repairs the separate deadlock problem.

### F42: independence from deadlock vacuity

Reader lines 667--677 give a different counterexample: at a deadlocked state
with no infinite execution and false `q`, the universal English `P(d,0)` is
vacuously true although the proof's base implication is false.  The
unreachable-state example is already serial and therefore survives elimination
of deadlocks; conversely, restricting to reachable states does not manufacture
an infinite execution at a reachable deadlock.  The two failures and their two
repair families are therefore genuinely independent.  The reader explicitly
says “Even after the first gap is repaired” and labels both as source-proof
gaps rather than theorem hypotheses supplied by the handbook.

### F43: complete S4 countermodel

Reader lines 907--935 and source-note lines 437--469 give a complete Kripke
model, not a bare frame:

`M=(W,\rho,V)`, `W={r,u,v}`,
`\rho={(r,r),(u,u),(v,v),(r,u),(r,v)}`,
`V(p)={u}`, and `V(q)={v}`.

The displayed relation is reflexive and transitive.  The root `r` satisfies
neither atom but accesses both a `p`-world and a `q`-world, so it satisfies
`Fp\land Fq`.  At `u`, no `q`-world is accessible; at `v`, no `p`-world is
accessible; and `r` satisfies neither atom.  Consequently no accessible world
satisfies `p\land Fq` or `q\land Fp`, so both consequent F-disjuncts are false
at the root.  The displayed formula is independently valid on every linear
inclusive future by comparing witness positions.  This proves exactly the
handbook's stated model-class warning and does not attribute the countermodel
to printed p. 53.

### Neutral fairness comparison

Reader lines 439--443 report the early printed-p. 47 enabled-processor prose.
Reader lines 937--953 separately give the printed-p. 53 finite action partition
and literal `j\ge i` occurrence condition.  The presentation calls them
“distinct” and says only that the paper proves no equivalence; it makes no
unproved stronger/weaker claim and invents no typed correspondence between a
processor-enabled predicate and a binary action relation.  Source-note lines
92--95 and 478--496 and presentation-ledger lines 155 and 161 agree.

## Criterion-by-criterion coverage

### C1 — identity, provenance, page map, rights, and version

Checked clean.  Reader lines 372--382, source-note lines 7--40, ledger line
153, and bibliography lines 2226--2237 agree on author, title, FOCS 1977,
printed pages 46--57, DOI, author-hosted URL, retrieval standing, and the absence
of an observed republication licence.  The wrapper's May 1981 date is correctly
kept as archival packaging rather than a second edition.  The physical map
1=wrapper and 2--13=printed 46--57 is exact.  Reader lines 1610--1617 keep the
IEEE-direct comparison open.

### C2 — program model, executions, atomicity, fairness, and hierarchy

Checked clean against printed pp. 46--49.  Reader lines 384--443 reproduce the
typed sequential and concurrent transition equations, nondeterministic
processor selection, unchanged nonselected control coordinates, nonessential
determinism qualification, and atomic-granularity caveat.  Lines 445--490 give
reflexive finite-path reachability, state assertions, invariance, partial versus
clean correctness, invariant examples, strict temporal implication, and the
scope exclusions.  The enabled prose and formal action condition remain
separate as recorded above.

### C3 — P1/P2, ER, Theorem 1, and proof assumptions

Checked clean against printed pp. 49--50.  Reader lines 492--552 preserve P1
and literal P2 while disclosing every handbook typing/counterexample boundary.
Lines 554--627 give all six ER forms A1--A2/R1--R4, predicate-calculus standing,
typed parameter side conditions, and I.  Lines 629--687 give the literal
Theorem 1 strength, proof-sketch status, expressive assertion-language premise,
pointwise finite branching rather than a uniform bound, König dependency, both
independent proof gaps, and the unresolved strict/inclusive source tension.

### C4 — sequential and concurrent applications

Checked clean against printed pp. 50--52.  Reader lines 689--722 correctly
treat Floyd conditions as premises and finite-path composition as A1/R2 work.
Lines 724--779 type full and partial attachments and calibrate their size
claims.  Lines 781--828 reproduce the complete source example at the warranted
indicator granularity and use positive capacity in the final contradiction.

### C5 — tense language, proof systems, quantifiers, and Theorems 2--3

Checked clean against printed pp. 52--55.  Reader lines 830--896 give
recursive inclusive F/G semantics, ordinary Boolean recursion, absolute present
at `s_0`, no next/until operator, G1--G3, RT/RG/MP, F2--F3, and exact Q1--Q4
directions while leaving the source's schema range unresolved.  Lines 898--935
keep RG's warning, Theorem 2's literal pure/propositional/future scope, external
proof and decision referrals, unquantified complexity sentence, and the
model-class defect distinct.  Lines 937--1025 give the finite action partition,
literal tail quantifier, I1/I2/E/N, N's restricted execution class, and derived
DI/DN with exact premises.  Lines 1027--1035 preserve Theorem 3's “at least as
strong” wording, skeletal proof, and relative-completeness corollary without
inventing the missing ER derivations.

### C6 — finite-state package and appendices

Checked clean against printed pp. 55--57.  Reader lines 1037--1101 distinguish
finite seriality, arbitrary-start action-satisfying paths, proper executions,
restricted system validity, Theorem 4, and the handbook-supplied exact SCC
criterion/proof.  Lines 1103--1124 give P, MRG's exact no-P-use side condition,
both Theorem 5 clauses, and the unprinted adequacy-construction boundary.
Lines 1126--1155 preserve Appendix A's cited T2/T3 ownership and Pnueli's local
six-step lemma proof.  Lines 1157--1204 type every Appendix B recursion clause
and keep both decision routes and all three proof-ownership boundaries exact.

### C7 — cross-surface consistency

Checked clean.  The complete source note, ledger lines 151--167, and reader
agree on every literal rule, theorem strength, handbook repair, defect,
proof/referral boundary, source locator, rights qualification, and open status.
The three bibliography entries reproduce the registered bibliographic
identities and the source's references 32--33.  Shared Part IX lines 599--823
define the handbook's inclusive LTL and modern automata material separately;
the N-c-012.b reader explicitly refuses to attribute those later results to
Pnueli.  Adjacent reader lines 350--369 and 1206 onward keep Kamp and GPSS in
separate source presentations, and lines 1596--1608 keep Alpern--Schneider's
safety/liveness result outside the Pnueli presentation.

### C8 — exposition, definition order, technical names, and closure

Checked clean.  The exposition is independently worded and does not reproduce
source images.  Every reconstruction-specific name has a local necessity,
exact eliminable definition, standing, nonredundancy explanation, and later
use: especially state assertion, full/partial attachment,
`\Sigma\models_{\rm prop}`, and `L_{\rm prop}(\Sigma)`.  Source terms are not
multiplied speculatively.  Strict implication, inclusive F, A2, and Theorem 3's
representation remain visibly distinct.  No later X/U grammar, LTL-to-Büchi
translation, safety/liveness syntax, or PSPACE classification is retrojected.
The reader, note, and ledger all preserve the narrow open status.

## Invariant-by-invariant coverage

- **I1:** satisfied.  This was source scholarship and prose reasoning only;
  no prohibited mechanical or publication gate was run.
- **I2:** satisfied.  The eight hashes matched before review, immediately
  before filing, and on the post-filing recheck recorded below.
- **I3:** satisfied.  The wrapper and every printed page 46--57 were freshly
  read visually; no page was unread or accepted from OCR.
- **I4:** satisfied.  Types, quantifiers, definitions, rule premises and side
  conditions, theorem strength, proof status, and external ownership were all
  checked at the line/page granularity recorded above.
- **I5:** satisfied.  Reader lines 473--483, 523--552, 554--606, 679--687,
  830--856, and 1027--1032 preserve the strict/inclusive tension without
  normalization.
- **I6:** satisfied.  Reader lines 852--853 and 1200--1203 and ledger line 165
  explicitly exclude the later grammar, translation, and complexity results.
- **I7:** satisfied.  Each genuinely needed reconstruction name meets the
  five-part rule locally; no owed artifact is disguised as an established
  technical object.
- **I8:** satisfied.  Author-hosted body-level reconstruction and the still
  absent IEEE-direct comparison remain separate at reader lines 372--382 and
  1610--1617, source-note lines 34--40 and 721--730, and ledger lines 153/167.
- **I9:** satisfied.  No majority inference is made; all status surfaces say
  that one hash-pinned snapshot still needs three independent acceptances.
- **I10:** satisfied.  This verdict can close only this seat's round-six review
  of N-c-012.b.  It does not close neighboring presentations, N-c-012 as a
  whole, Part IX, IEEE comparison, build, handbook visual inspection, human
  review, final-book completion, or user acceptance.

## Post-filing frozen-identity recheck

Immediately after filing, I recomputed all eight frozen-object hashes.  Every
identity still matched the round-six values in the table above.  The transcript
hash is necessarily reported in the filing handoff rather than embedded in the
file whose hash it would change.

## Narrow closure and final verdict

The complete round-six N-c-012.b snapshot is source-faithful at the assigned
source-fidelity seat.  This is one blind seat's verdict only; unanimity and every
external gate named above remain independently open.

ACCEPT
