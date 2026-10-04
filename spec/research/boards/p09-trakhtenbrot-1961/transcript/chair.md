# Chair transcript — Trakhtenbrot 1961/1962 presentation

## Round 1 opened — 2026-08-23

The chair froze the seven-object source/manuscript snapshot identified in
../charter.md and seated three independent reviewers for source fidelity and
language, mathematical proof, and adversarial publication/terminology review.

Reviewers are blind to one another's reports and to the chair's reconciliation.
They may read only the charter, frozen review artifacts, official source
records, and the rendered source pages identified by the charter.  They may not
edit a frozen artifact.

The source-fidelity seat must disclose its source-language competence and
evidence.  The board does not presuppose or advertise Russian-specialist
certification.  Inadequate linguistic evidence requires a rejection or an
explicit not-checked item, not an inferred accept from neighboring sources.

This is scholarly manuscript review.  No test, test harness, automated checker,
repository script, TeX compilation, interim handbook build, handbook-PDF
inspection, or build is authorized.

Status: ROUND 1 CLOSED — REJECT.

## Round 1 reconciliation — 2026-08-23

All three reports were filed independently on the unchanged Round 1 snapshot:

- source fidelity: REJECT, `SF-R1-01` through `SF-R1-04`, report SHA-256
  `C2DB0A225B0C08F2A3ADA770570001F96009DA5DB6C055AF07D8D81A089B3C57`;
- mathematical proof: REJECT, `F1` through `F5`, report SHA-256
  `5DC4AF8449C9E6A97F74850DE160FCBDFB58592897DA30F327DA69D4CE35CBC6`;
- adversarial publication: ACCEPT, report SHA-256
  `D4CD0230DA155C7F536B801E5CD59547FC08E466FF00ED19FDE0AB1622725549`.

The accept does not outvote either reject.  The board therefore rejects Round
1 on nine supported must-fixes.  The chair reconciled all nine without
downgrading or merging them away:

1. the 1961 Л/1962 \(A\) notation boundary is now explicit;
2. announcement Theorem 1 is located on p. 327, with p. 326 retained for its
   terminology;
3. the expansion's finite-preperiod use of “periodic” is rendered as ultimately
   periodic;
4. the Math-Net rights and no-redistribution boundary is recorded;
5. the continuous-graph and general-solution statements now carry their
   \(\mathcal I\)-definability hypotheses;
6. the recurrence displays its free input, bound-state and choice predicates,
   and fixed initial basis state;
7. the finite-word action is typed length by length, proved independent of
   infinite extension, made prefix-compatible, and used for both source word
   notions;
8. special beginnings are defined exactly, the existence/effectivity split is
   restored, and the source's Büchi attribution is stated; and
9. the open-relation analogue after Theorem \(4'\) is included without a weight
   bound.

No test, checker, script, TeX command, build, or rendered-handbook inspection
was used in the reconciliation.

## Round 2 opened — 2026-08-23

The chair froze the new seven-object snapshot in the Round 2 table of
`../charter.md`.  The reader, source note, and compact record have new hashes;
the two primary scans, shared theorem, and bibliography are unchanged.  The
three seats must audit the whole new snapshot independently.  They may not read
the Round 1 reports, this chair reconciliation, the ledger, or another Round 2
report, and they may not contact one another.

This remains scholarly manuscript review.  No test, automated checker,
repository script, TeX command, interim handbook build, handbook-PDF
inspection, or build is authorized.

Status: ROUND 2 CLOSED — REJECT.

## Round 2 reconciliation — 2026-08-23

All three independent reports were filed on the unchanged Round 2 snapshot:

- source fidelity: ACCEPT, report SHA-256
  `6C8DF41B6F5DC2E7DEF8D59073BCA8B85E65628FC95D9826B8F71E509718DC83`;
- mathematical proof: REJECT — `R2-MP-01`, report SHA-256
  `5A10A01B19917E857B6EFF3A7BBD0AFA16E2461507B53FAEDAE519824CFCF2D4`;
- adversarial publication: REJECT — `AP-R2-01`, report SHA-256
  `0C85CF97FE439C5C3A807B00B78810139033F0847044131EB33ED4685EDC5099`.

The source-fidelity accept cannot outvote the two supported must-fixes.  Round
2 is rejected.  `R2-MP-01` identifies a source-inherited empty-language defect:
the printed finite-word converse omits nonemptiness even though a total
length-preserving enumerator has nonempty range at every positive length and
the printed proof requires a first word of each length.  `AP-R2-01` identifies
a definition-before-use defect: the reader names and uses solution/general
solution before giving the source's graph-containment and bidirectional
parameterization definitions.

No test, checker, script, TeX command, build, or rendered-handbook inspection
was used in this reconciliation.

## Round 3 opened — 2026-08-23

The chair corrected both Round 2 defects in the source-facing prose.  The
reader now defines solution before Theorem \(4'\), first names general solution
at its bidirectional parameterization definition, and no longer pre-announces
that vocabulary in the operator-version paragraph or heading.  The reader,
source note, and compact record now expose the printed empty-language defect,
state the corrected nonempty converse, prove why the added hypothesis supplies
the missing lengthwise seed, and identify it as handbook-owned.

The chair froze the seven-object Round 3 snapshot in `../charter.md`.  The two
primary scans, shared theorem, and bibliography are unchanged; the reader,
source note, and compact record have new hashes.  Three independent seats must
audit the whole snapshot and may not read an earlier report, the ledger, this
chair transcript, or another Round 3 report.

This remains manuscript scholarship.  No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 3 CLOSED — REJECT.

## Round 3 reconciliation — 2026-08-23

All three independent reports were filed on the unchanged Round 3 snapshot:

- source fidelity: ACCEPT, report SHA-256
  `5026F8BDB57A8FF23C8ECC165B1AE9AF91F005F11A42D7FAE4D7915D50C26075`;
- mathematical proof: REJECT — `R3-MP-01`, report SHA-256
  `285B269C687A78B8F3603F9AE694B822FF23754590813D77AD7709D1565FC3F5`;
- adversarial publication: REJECT — `AP3-F01`, report SHA-256
  `19AFECC81269B82ADE3EEC8E3B64E5F12D9CE3467BA5786C8639A0F85BD357B1`.

The source-fidelity accept does not outvote either supported must-fix.  Round
3 is rejected.  `R3-MP-01` identifies a source-inherited off-by-one defect:
under the manuscript's all-prefix definition, a weight-\(k\) causal operator
has at most \(k\) nonempty residual graph portions plus the empty portion, so
the exact bound is \(k+1\).  The weight-one constant-zero operator supplies the
minimal counterexample to the printed \(k\) claim.  `AP3-F01` identifies an
overbroad rights paraphrase: Math-Net permits the named individual users to
print copies for noncommercial teaching or research, not generic
medium-neutral “copies.”

No test, checker, script, TeX command, build, or rendered-handbook inspection
was used in this reconciliation.

## Round 4 opened — 2026-08-23

The chair corrected both Round 3 defects.  The reader, source note, and compact
record now distinguish the source's printed \(k\) claim from the exact
all-prefix \(k+1\) bound, give the empty-portion derivation and constant-zero
counterexample, and identify the correction as handbook-owned.  The source
note and compact record now state Math-Net's print-copy exception at its exact
user, medium, and purpose scope and retain the no-open-licence and
no-redistribution boundaries.

The chair froze the seven-object Round 4 snapshot in `../charter.md`.  Three
new independent seats must audit the whole snapshot.  They may not read an
earlier report, the ledger, this chair transcript, or another Round 4 report,
and they may not contact one another.

This remains manuscript scholarship.  No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 4 CLOSED — REJECT.

## Round 4 reconciliation — 2026-08-23

All three independent reports were filed on the unchanged Round 4 snapshot:

- source fidelity: REJECT — `R4-SF-01` and `R4-SF-02`, report SHA-256
  `31F9B592D8EB5E67A240C93FA2AD2E9E41E78EFD9DE3CF890AD4D96E04B251E3`;
- mathematical proof: ACCEPT, report SHA-256
  `8EF3BA903E5DBBAB59A8D1661C86220EC483382625A7095DE5D58C82CC405A6F`;
- adversarial publication: REJECT — `R4-AP-01`, report SHA-256
  `9EA2F0B7A7476B64E3141AA42A762693CCF5D27BDA14C65367C91FF2CE4D086F`.

The mathematical accept cannot outvote the source-fidelity counterexample or
the adversarial convention finding.  Its residual-count derivation assumes
that a state after a finite input prefix is determined by that prefix, whereas
the source's finite-memory equations permit the state update to inspect the
whole future suffix.  The adversarial report correctly requires disclosure
that the 1961 announcement permits empty portions while the 1962 expansion
defines a portion only after a nonempty prefix intersection; its further
defence of the expansion's printed \(k\) bound is defeated by the same explicit
counterexample.

The chair reconciled the supported findings without preserving either false
numerical bound:

1. the reader and records now distinguish the announcement's all-prefix
   convention from the expansion's nonempty-prefix convention and state which
   convention the handbook uses;
2. the printed \(k\) claim and the Round 3 \(k+1\) replacement are both
   withdrawn, an explicit weight-two zero-anticipation operator is given with
   three nonempty residual graph portions and four all-prefix portions, and
   only the safe residual-operator count is retained; and
3. the covering construction is restricted to nonempty closed homogeneous
   sets, while the empty set is handled separately by an inconsistent
   recurrent formula.

No test, checker, script, TeX command, build, or rendered-handbook inspection
was used in this reconciliation.

## Round 5 opened — 2026-08-23

The chair repaired all Round 4 defects in the reader, detailed source note,
and compact record.  The new text distinguishes the announcement's
all-prefix portion convention from the expansion's nonempty convention;
withdraws both the source's \(k\) graph-degree bound and the Round 3 \(k+1\)
replacement; gives an explicit zero-anticipation operator with exact broad
weight two, three nonempty portions, and four all-prefix portions; and states
the safe suffix-induced-operator conclusion without a broad-state bound.  It
also restricts the source covering construction to nonempty sets and handles
the empty set by an inconsistent formula of the same recurrent shape.

The chair froze the seven-object Round 5 snapshot in `../charter.md`.  Three
fresh independent seats must audit the whole snapshot.  They may not read an
earlier report, the ledger, this chair transcript, or another Round 5 report,
and they may not contact one another.  Each must independently check the
counterexample and empty-set argument rather than treating the charter as a
proof.

This remains manuscript scholarship.  No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 5 CLOSED — REJECT.

## Round 5 reconciliation — 2026-08-23

All three independent reports were filed on the unchanged Round 5 snapshot:

- source fidelity: ACCEPT, report SHA-256
  `D0382FF4F24DF74D580785EC8E53C29A9E957212BE321374F798861AC023EDB6`;
- mathematical proof: ACCEPT, report SHA-256
  `DA404C640733DE4D2A10C58344D9017A527A9123D4A07287FE0302A45A3E91D5`;
- adversarial publication: REJECT — `AP5-01`, `AP5-02`, `AP5-03`, and
  `AP5-04`, report SHA-256
  `59FBB1550901537193DEEF2B9FE92659D20D29B5B36237EA7DE6A8C7594E6313`.

The two accepts do not outvote the four supported publication must-fixes.
Round 5 is rejected.  The mathematical substance repaired after Round 4 is
clean: the weight-two counterexample, its three nonempty and four all-prefix
portions, the failure of both numerical bounds, and the nonempty-covering versus
empty-set distinction were all independently rederived.  The remaining defects
are exact-definition and ownership defects:

1. `AP5-01`: the reader gives the interpretation and conveniences of
   \(\mathcal I\) but not its primitive term, atomic-formula, and formula-
   formation grammar;
2. `AP5-02`: the reader substitutes the semantic dependence consequences of
   lower and upper \(t\)-formulae for the source's stricter syntactic classes,
   weakening the stated effective normal form;
3. `AP5-03`: equal-length tuple portions and the handbook-owned suffix operator
   used in the graph counterexample lack exact typed eliminable definitions;
   and
4. `AP5-04`: the reader and compact record do not explicitly say that the
   nonempty restriction and separate empty-set recurrence are handbook-owned.

No test, checker, script, TeX command, build, or rendered-handbook inspection
was used in this reconciliation.

## Round 6 opened — 2026-08-23

The chair repaired all four Round 5 publication defects in the reader,
detailed source note, and compact record.  The revised text now gives the
primitive term, atomic-formula, and formula-formation grammar of
\(\mathcal I\); defines the source's controlled and lower/upper syntactic
classes before stating their semantic dependence consequences; types
equal-length coordinate portions and the residual stream maps \(T_u\) with the
exact paired graph-portion equation; and explicitly identifies the nonempty
covering restriction and empty-set recurrence as handbook-owned.

The chair froze the seven-object Round 6 snapshot in `../charter.md`.  Three
fresh independent seats, none used in Round 5, must audit the whole snapshot.
They may not read an earlier report, the ledger, this chair transcript, or
another Round 6 report, and they may not contact one another.  Each must
independently check the four repaired fault lines and the complete mathematical
presentation rather than treating the charter as proof.

This remains manuscript scholarship.  No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 6 OPEN.

## Round 6 reconciliation — 2026-08-23

Status: ROUND 6 CLOSED — ACCEPT.  `N-c-014.c` manuscript content is admitted.

All three fresh independent reports were filed on the unchanged Round 6
snapshot and were read together only after every seat had filed:

- source fidelity: ACCEPT, report SHA-256
  `991F05346A8F6D52B60BE1CFA73238B329E4AC40CAF3EE72A7B65BE9DA4FB16D`;
- mathematical proof: ACCEPT, report SHA-256
  `82E9D92309EFB960C3A5B41189038E02B90E86F1FB7DF40B9C410128E00B0CBC`;
- adversarial publication: ACCEPT, report SHA-256
  `6CCA067E54049F5A046545086879EE86C54E1996FBAA30C29CFE91A7BE55BD2E`.

Every seat independently recomputed the same seven frozen identities and
visually inspected all four announcement pages and all twenty-nine expansion
pages at original detail.  No seat found a blocker, must-fix, or lesser
publication finding.  Their independent derivations agree on the primitive
grammar and lower/upper syntax; whole-suffix finite-memory type; typed tuple
portions and residual operators; the weight-two counterexample and its three
nonempty/four all-prefix portions; the withdrawal of the false printed
numerical bound; the handbook-owned nonempty-covering/empty-set split; the
handbook-owned nonempty finite-word repair; the exact continuity,
closedness, effectiveness, and fixed-lookahead boundaries; terminology; source
strength; rights; and admission scope.

The mathematical seat disclosed that one display of the assigned frozen
`n-c-014.tex` object extended past the Trakhtenbrot block through adjacent
lines 908--930.  Those lines belong to the same frozen assigned object, were
not used as evidence, and no separate Rabin draft or source note was inspected.
The disclosure does not compromise the blind Trakhtenbrot verdict.

The charter's consensus rule is satisfied: three ACCEPT verdicts, one
unchanged hash-pinned snapshot, and no unresolved blocker or must-fix.  The
admission is limited to the source-faithful manuscript reconstruction of the
distinct 1961 announcement and complete 1962 expansion for `N-c-014.c`.  It
does not admit `N-c-014` as a whole, Rabin, Part IX, a rendered handbook page,
a publication build, human or user acceptance, another part, or the completed
book.

No test, checker, repository script, TeX command, interim build, or rendered-
handbook inspection was used in the review or reconciliation.
