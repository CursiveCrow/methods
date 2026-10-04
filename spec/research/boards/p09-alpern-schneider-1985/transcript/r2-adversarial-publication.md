# Round two: adversarial publication and terminology seat

## Blindness, scope, and evidence declaration

This is a fresh blind round-two review. I read the board charter in full and
used only its frozen round-two seven-object snapshot. I did not read
`ledger.md`, `transcript/chair.md`, any round-one transcript, any other
round-two transcript, or any earlier Part IX board record. I did not inspect a
handbook PDF and did not run a test, checker, repository script, TeX command,
build, or automated review harness.

I visually read `journal-page-1.png` through `journal-page-5.png` and
`tr-page-01.png` through `tr-page-11.png` at original detail. The five journal
images cover printed pp. 181--185. The report images cover its outer cover,
title/abstract leaf, and internally numbered body pp. 1--9. I then read every
line of each frozen manuscript/source scope specified in the charter.

## M01: independently recomputed round-two identities

All seven SHA-256 values were recomputed before substantive review and match
the charter byte for byte.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `4E58F17BC534504C5D43DE2EADBD365CE01B8D029CE8A67B2BBAFBF2DAD75736` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `786B63163F0EF1456561B974D1D4A38578A06AF619C4DAB0ADE05FFCC0D7EE13` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `915ECD5D1451D24E336A60616AF5F93EBE300774A1D29FABABD0531035F4838E` | match |

## Findings

### R2-AP-01 — must-fix — the repaired leads-to discussion still misstates which source claim is unqualified

- **Author / round / status:** adversarial publication and terminology seat;
  round two; open must-fix.
- **Exact manuscript locations:**
  `handbook/parts/p09/presentations/n-c-012.tex:2769-2775`;
  `spec/research/p09-alpern-schneider-1985-source-note.md:276-286`;
  `spec/research/p09-source-presentations-lot2-3.md:467-470`.
- **Exact source locations:** journal p. 183, right column, leads-to paragraph;
  technical report body p. 5 (file page 7), leads-to paragraph.
- **Claim and evidence:** all three records say, in substance, that the source
  claims without qualification that a leads-to property is live and not
  absolutely live. The printed source does not leave both assertions
  unqualified. Immediately after defining leads-to, it conditions the liveness
  assertion on \(E_2\) being satisfiable. It then gives the non-absolute claim
  and witness without the further existence assumptions needed for that
  witness. The journal and report agree on this split.
- **Violated invariants:** I6 (source text and handbook repair must remain
  distinct), I10 (source claims at exact strength), and the source-truth portion
  of M10, M19, and M21.
- **Concrete graduate-reader harm:** the present wording falsely enlarges the
  identified source defect. A reader is told that Alpern and Schneider omitted
  even the condition on liveness, when the actual defect is in the subsequent
  unqualified non-absolute separation. This corrupts both the historical record
  and the rationale for the handbook-owned three-hypothesis repair.
- **Smallest exact correction:** in each of the three records, say separately:
  “The source says that a leads-to property is live when \(E_2\) is
  satisfiable, but says without the needed further qualifications that it is
  not absolutely live.” In the main reader, introduce the next sentence with
  “In the handbook's state-set rendering, let \(E_1,E_2\subseteq S\) ...” so
  the change from source event types to state sets is visibly handbook-owned.
  Retain the three displayed state-set hypotheses and the existing witnesses.

### R2-AP-02 — must-fix — the “exact” repaired witnesses are not typed under the reader's declared sequence operations

- **Author / round / status:** adversarial publication and terminology seat;
  round two; open must-fix.
- **Exact manuscript locations:** the declared concatenation signature is
  `handbook/parts/p09/presentations/n-c-012.tex:2643-2646`; the first undefined
  constant-stream notation and ill-typed concatenation occur at
  `n-c-012.tex:2781-2786`; the same undeclared constant-stream notation and a
  state used where a finite prefix is required recur at `n-c-012.tex:2935-2947`.
  The parallel source-record uses are
  `spec/research/p09-alpern-schneider-1985-source-note.md:297-303` and
  `:516-529`; the compact record uses \(\{a^\omega\}\) at
  `spec/research/p09-source-presentations-lot2-3.md:519-524` without defining
  \(a^\omega\) there.
- **Claim and evidence:** the reader defines concatenation only for
  \(u\in S^*\) and \(y\in S^\omega\). It later chooses
  \(e_1\in E_1\subseteq S\) and writes
  \(e_1\mathbin{\smallfrown}c^\omega\). Under the declared types, \(e_1\) is a
  state, not a finite sequence. Likewise, cylinder notation was defined only
  for \(u\in S^*\), but the countermodel says that \([b]\) misses \(Q\) after
  choosing \(b\in S\). The notations \(e_2^\omega,c^\omega\), and
  \(a^\omega\) are used before any local definition of the constant execution;
  the source note explains \(a^\omega\) only after its first displayed use and
  never repairs the one-state-prefix coercions.
- **Violated invariants:** I3 (definition before use and exact standing), I4
  (new notation must receive a local eliminable definition and standing), and
  the exactness requirements in M05, M10, M17, and M20.
- **Concrete graduate-reader harm:** the central witness for the repaired
  leads-to defect and the cylinder witness for the Corollary 2.1 countermodel
  are literally outside the domains of the operations previously declared. A
  reader cannot type-check the advertised “exact” repair without silently
  inventing both a singleton-sequence coercion and a constant-stream notation.
- **Smallest exact correction:** before the first such use, define, for
  \(s\in S\), \(\langle s\rangle\in S^1\subseteq S^*\) to be the one-state
  sequence and \(s^\omega\in S^\omega\) by \(s^\omega(n)=s\) for every
  \(n\in\omega\). Then replace
  \(e_1\mathbin{\smallfrown}c^\omega\) by
  \(\langle e_1\rangle\mathbin{\smallfrown}c^\omega\) and replace \([b]\) by
  \([\langle b\rangle]\). Mirror the same definitions/corrections in the
  source note, and define or eliminate \(a^\omega\) at its compact-record use.

### R2-AP-03 — must-fix — “strong-until” is an unnecessary, source-inconsistent technical name

- **Author / round / status:** adversarial publication and terminology seat;
  round two; open must-fix.
- **Exact manuscript location:**
  `handbook/parts/p09/presentations/n-c-012.tex:2817-2825`, especially line
  2818. The companion records correctly say “until” at
  `spec/research/p09-alpern-schneider-1985-source-note.md:344-360` and
  `spec/research/p09-source-presentations-lot2-3.md:480-481`.
- **Exact source locations:** journal p. 183, “Until” example; technical report
  body p. 6 (file page 8), “Until” example. Neither frozen source calls the
  example “strong-until.”
- **Claim and evidence:** the main reader calls this “the source's
  strong-until example.” The source names it only “Until” and states directly
  that \(E_2\) eventually occurs and all preceding events have type \(E_1\).
  The added adjective is neither needed later nor locally distinguished from a
  weak-until notion.
- **Violated invariants:** I4's necessity, nonredundancy, and use tests; I6's
  source-versus-handbook ownership boundary; and M12, M20, and M21.
- **Concrete graduate-reader harm:** a reader is invited to import a modern
  strong/weak-until taxonomy and to attribute the stronger label to the 1985
  source, although no such comparison is made or needed. This is precisely the
  kind of unnecessary technical naming that the AGENTS rule forbids.
- **Smallest exact correction:** replace “strong-until” with “until.” The
  following sentence already states the exact eventual-\(E_2\) semantics, so no
  new terminology or expansion is needed.

### R2-AP-04 — should-fix — the source-critical findings index omits the leads-to source defect

- **Author / round / status:** adversarial publication and terminology seat;
  round two; open should-fix.
- **Exact manuscript locations:** the defect is analyzed at
  `spec/research/p09-alpern-schneider-1985-source-note.md:276-314`, but the
  table headed “Current source-critical findings” at `:611-619` contains only
  AS-01 through AS-05 and has no leads-to entry.
- **Violated invariants:** I6 and the cross-record reconciliation required by
  M10 and M21.
- **Concrete graduate-reader harm:** the detailed prose records a second
  source-level qualification defect, while the source note's own defect index
  makes it disappear. A later reader who uses that table as the source-critical
  handoff will miss both the provenance and the required treatment.
- **Smallest exact correction:** add one row identifying journal p. 183 / TR
  body p. 5, the source's conditional liveness clause, the insufficiently
  qualified non-absolute claim, and the handbook-owned exact state-set repair.

### R2-AP-05 — should-fix — the reader omits the source's separately attributed temporal-logic expressibility report

- **Author / round / status:** adversarial publication and terminology seat;
  round two; open should-fix.
- **Exact manuscript locations:** the gap is between
  `handbook/parts/p09/presentations/n-c-012.tex:2883-2890` and `:2892-2917`.
  The source note mentions inaccessible Plotkin private communications only in
  general at `spec/research/p09-alpern-schneider-1985-source-note.md:576-578`;
  the compact record passes directly from Corollary 1.1 to Theorem 2 at
  `spec/research/p09-source-presentations-lot2-3.md:499-504`.
- **Exact source locations:** journal p. 184, between Corollary 1.1 and Theorem
  2; technical report body p. 7 (file page 9), same position.
- **Claim and evidence:** after its conditional Corollary 1.1 discussion, the
  article reports, on Plotkin's 1983 private communication, that every
  temporal-logic-expressible property can be written as a conjunction of two
  temporal-logic-expressible liveness properties. The reader correctly warns
  that Theorem 1 alone gives no syntax-preservation result, but never records
  this distinct attributed source claim.
- **Violated invariant:** I10's exact-strength account of the source argument,
  with M14, M19, and M21 implicated.
- **Concrete graduate-reader harm:** the omission collapses two different
  points: what Theorem 1 proves semantically and what the authors separately
  report about temporal logic on private-communication authority. A reader
  cannot recover the source's actual transition from Corollary 1.1 to Theorem
  2 or the evidence limitation of that syntax-level assertion.
- **Smallest exact correction:** add one paraphrased sentence stating that
  Alpern and Schneider report the temporal-logic expressibility result and
  cite Plotkin's private communication for it, followed immediately by the
  existing limitation that this board did not independently verify the private
  communication. Do not promote it to a handbook theorem.

## Focused stress test of the four repaired areas

### Fully typed compact safety formula

Checked clean. In the compact record at lines 423--442, \(P\subseteq S^\omega\)
is stated before the formula, \(x\in S^\omega\), \(n\in\omega\), and
\(y\in S^\omega\) are all bound at the correct scopes, and the prefix and
finite--infinite concatenation operations are announced before use. The order

\[
 \forall x\;\bigl(x\notin P\Rightarrow
 \exists n\;\forall y\;(x{\upharpoonright}n)\mathbin{\smallfrown}y\notin P\bigr)
\]

matches the visually read formula on journal p. 182 and report body p. 2. It
supports exactly the finite irremediable-prefix reading and does not restrict
the bad event's content.

### Satisfiable but insufficient intersection-closure hypothesis

Checked clean apart from the notation defect in R2-AP-02. Both source images
visibly print “closed under intersection.” The family
\(\mathcal F=\{S^\omega,E_a,E_b,Q,\varnothing\}\), with
\(Q=\{a^\omega\}\), really is intersection-closed:
\(Q\cap E_a=Q\), \(Q\cap E_b=\varnothing\), and
\(E_a\cap E_b=\varnothing\), with intersections involving the whole and empty
sets immediate. Its live members are exactly \(S^\omega,E_a,E_b\); \(Q\)
misses the one-\(b\)-prefix cylinder and the empty set is not dense. Pairwise
intersections of the live members therefore never give \(Q\). Thus the printed
hypothesis is jointly satisfiable and genuinely insufficient, not merely
unhelpful for the authors' construction. Union closure makes
\(P\cup E_a\) and \(P\cup E_b\) expressible; complement plus intersection also
suffices by De Morgan.

### Standing and nondegeneracy of the predictive property

Checked clean. The reader explicitly gives \(A,B\subseteq S\) before defining
\(P_{A,B}\subseteq S^\omega\), states the nonemptiness of
\(A,S\setminus A,B,S\setminus B\), gives an eliminable definition, identifies
its standing as a property, explains why the name is needed to expose the
quantifier dependency, and uses it immediately. Constant eventual-\(B\) and
eventual-not-\(B\) continuations establish liveness. For any proposed common
suffix, if it is eventually always in \(B\), a non-\(A\) initial state defeats
it; otherwise an \(A\) initial state defeats it. The claimed failure of uniform
liveness is therefore correct.

### Leads-to source defect, hypotheses, witnesses, and two-state example

The repaired mathematics is correct once the sequence notation is typed. In
the state-set rendering, the conjunction

\[
 E_1\ne\varnothing,\qquad E_2\ne\varnothing,\qquad
 S\setminus(E_1\cup E_2)\ne\varnothing
\]

is exactly what makes the intended “uniformly live but not absolutely live”
separation available. A chosen \(e_2\in E_2\) supplies a common constant
suffix; if \(e_2\in E_1\cap E_2\), every occurrence is still answered by a
strictly later suffix occurrence. A chosen neutral \(c\) yields a satisfying
constant execution with no \(E_2\), and a one-\(e_1\) prefix then makes it fail.
The conditions are also materially sharp for this separation: with
\(E_1=\varnothing\) the property is the whole space and is absolute; with
\(E_1\ne\varnothing=E_2\) it is not live; and with no neutral state, every
satisfying execution must contain an \(E_2\), which makes it survive every
finite prefix and hence makes it absolute. The displayed two-state instance
\(S=\{e_1,e_2\}\), \(E_1=\{e_1\}\), \(E_2=\{e_2\}\) correctly demonstrates
that latter failure of the printed non-absolute generalization. R2-AP-01 is
about the inaccurate report of the source's already conditional liveness
sentence; R2-AP-02 is about the types of the written witnesses, not this set
theory.

## M01--M22 coverage map

| Point | Status | Adversarial publication/terminology disposition |
|---|---|---|
| M01 | checked-clean | All seven round-two hashes independently recomputed before review and matched; values are recorded above. |
| M02 | checked-clean | Journal pp. 181--185 and all eleven TR file pages were visually read at original detail. |
| M03 | checked-clean | Title, authors, journal, volume 21(4), 7 October 1985, pp. 181--185, DOI record, David Gries communication line, 5 November 1984 receipt, 20 February 1985 revision, TR 85-650, outer/inner report dates, Cornell routes, and printed copyright/no-open-licence boundary are mutually consistent. |
| M04 | checked-clean | The page maps match the images. The revised report and journal agree substantively; corollaries are unnumbered in the report and numbered 1.1/2.1 in the journal. Both visibly print “intersection” in the second corollary. |
| M05 | finding-linked | \(S\ne\varnothing\), \(S^*,S^\omega\), empty sequence, prefix, property/program standing, membership, satisfaction, and terminal padding are correct. R2-AP-02 catches later violations of the declared concatenation/cylinder operand types. |
| M06 | checked-clean | Exact safety quantifier order and finite bad-prefix interpretation agree across reader, shared definition, source note, compact record, and both source versions. |
| M07 | checked-clean | “Live for \(P\)” is locally defined as a finite-prefix/property relation, distinguished from universal liveness, used immediately, and correctly implies property nonemptiness via the empty prefix. Full-space rather than fixed-system scope is explicit. |
| M08 | checked-clean | Proof-method motivation, failed-continuation maximality argument, examples, and stuttering qualification are accurately calibrated and not promoted to decision procedures or uniqueness/correctness theorems. |
| M09 | checked-clean | Uniform and absolute liveness have exact property standing, local definitions, necessity/nonredundancy explanations, immediate use, and the correct inclusion chain. |
| M10 | finding-linked | Leads-to mathematics and two-state counterexample are correct, but R2-AP-01 corrects the source's conditional/unqualified split and R2-AP-02 corrects the typed witnesses. R2-AP-05 records an omitted attributed source claim. |
| M11 | checked-clean | The predictive property has explicit \(A,B\subseteq S\), all four nondegeneracy hypotheses, a correct liveness proof, and a correct no-uniform-suffix argument. |
| M12 | finding-linked | Until and total-correctness decompositions and rejection of a dichotomy are correct; R2-AP-03 removes the unnecessary source-inconsistent “strong-until” name. |
| M13 | checked-clean | Cylinder basis and both directions of safety iff closed and liveness iff dense are correct, with \(S\ne\varnothing\) supplying nonempty cylinders. Handbook ownership of the direction proofs is stated. |
| M14 | finding-linked | Theorem 1's algebra, least-closed-superset contradiction, density, and nonuniqueness/cost/syntax boundaries are correct. R2-AP-05 concerns the separate attributed temporal-logic claim omitted after those boundaries. |
| M15 | checked-clean | Corollary 1.1 retains complement, intersection, and topological-closure hypotheses and makes no unconditional temporal-language claim. |
| M16 | finding-linked | Theorem 2's alpha-renaming, eventual-constant definitions, density, disjointness, factorization, and \(\lvert S\rvert>1\) materiality are correct. R2-AP-02 requires the constant-execution and singleton-prefix notation used around this construction to be typed. |
| M17 | finding-linked | Printed Corollary 2.1, its genuinely insufficient intersection-closure hypothesis, the denotation-family countermodel, and both union/Boolean repairs are mathematically correct. R2-AP-02 fixes the written \(a^\omega\) and one-\(b\)-prefix notation. |
| M18 | checked-clean | Every Boolean-table entry is correct at the stated “in general” strength; arbitrary closed intersections, finite closed unions, dense unions, and the whole-space-only overlap are correctly separated from syntax closure. |
| M19 | finding-linked | The manuscript correctly distinguishes printed theorem proofs, merely stated topological equivalences, and handbook proofs. R2-AP-05 supplies the missing exact content/evidence boundary for the reported Plotkin result. |
| M20 | finding-linked | Required standings for live-for, uniform, absolute, \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\) are otherwise exact and eliminable. R2-AP-02 catches undeclared sequence notation; R2-AP-03 catches an unnecessary new technical name. |
| M21 | finding-linked | Core claims reconcile across the five records. R2-AP-01 is a repeated three-record attribution error, R2-AP-03 is a reader/companion terminology mismatch, R2-AP-04 is a source-note index omission, and R2-AP-05 is an omitted source report. |
| M22 | checked-clean | Unlettered `N-c-012` standing, copyright/access boundary, topic-only status, open review gate, and no-test/no-build/no-rendered-handbook boundary are explicit and appropriately limited. |

No mandatory coverage point was left unchecked.

## Publication premortem

If this snapshot were admitted unchanged, the earliest hostile-source check
would compare the leads-to paragraph with p. 183 and show that the handbook
misreported a printed condition. The earliest formal-reading check would apply
the declared concatenation signature and find that a state is being
concatenated as though it were a finite sequence. A terminology editor would
then find a source-attributed “strong-until” label that neither source nor the
companion records use. Those are small local corrections, but all three attack
express source-truth or definition-before-use invariants and therefore remain
publication-gate must-fixes.

VERDICT: REJECT — R2-AP-01, R2-AP-02, R2-AP-03
