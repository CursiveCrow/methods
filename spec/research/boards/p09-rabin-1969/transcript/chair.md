# Chair transcript — Rabin 1969 presentation

## Round 1 opened — 2026-08-23

The chair acquired and visually inspected the complete Rabin article and the
complete six-page Meyer ICM article used for the later complexity correction.
The reader reconstructs Rabin's successor structures, ordinary automata, both
logical translations, one worked track encoding, Theorem 3.1's product, the
ordinary/dual distinction, marked-tree and well-founded complementation,
both half-steps, finite-tree lemmas, Section 3.12's actual emptiness argument,
Chapter II applications, and the Thomas boundary. It preserves effectiveness
while withdrawing Rabin's later-refuted elementary-recursive bound.

The chair reconciled the reader, detailed source note, compact record, and
bibliography, then froze the six-object Round 1 snapshot in `../charter.md`.
Three fresh independent seats must audit the whole snapshot. They may not read
one another's reports, this chair transcript, the ledger, the staging draft, or
another board transcript, and they may not contact one another.

This remains manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 1 CLOSED — REJECT.

## Round 1 reconciliation — 2026-08-23

All three blind reports were filed independently on the unchanged Round 1
snapshot and were opened together only after every seat had filed:

- source fidelity: ACCEPT, report SHA-256
  `1E2117A5E1BC5E7D14F0A87BD00508A24282CDF8E60F6CDF1593823B59FFE021`;
- mathematical proof: REJECT — `MP-R1-01`, report SHA-256
  `F9840BA0A1F288CC38C574A3508ECE4DC20128065E4DF5A4EBC8BE1F927495C2`;
- adversarial publication: REJECT — `AP-R1-01` and `AP-R1-02`, report
  SHA-256
  `122A159396E258443465AC21460AE95BFCFE2674445CA18A7BFCE7FEC1176523`.

The source-fidelity accept does not outvote either rejection. The chair checked
the findings against Rabin's printed pp. 25, 27, 31, and 34 and independently
checked the supplied counterexamples. Round 1 is rejected on three distinct,
supported must-fixes:

1. `AP-R1-01`: Lemma 3.6 enumerates
   \(\mathcal P(S)-F-\{\varnothing\}\), which can be empty. Definition 3.6
   then makes the zero-length dual language the semantically nontrivial
   no-run case, but the reconstruction begins its induction at length one.
2. `MP-R1-01`: even at positive length, Rabin's printed p. 34 incorrectly
   requires nonempty \(H\subseteq U_k\) and nonempty
   \(U_0\subseteq U_1\). The empty choices are required respectively when
   the shorter dual condition already holds and when no run exists. The
   handbook must preserve the printed branch but label the completion as a
   handbook-owned repair.
3. `AP-R1-02`: the compact record's sole use of `full-frontiered` invents an
   undefined redundant synonym for Rabin's defined term `frontiered` and must
   be deleted.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used in the review or reconciliation.

## Round 2 opened — 2026-08-23

The chair integrated every supported Round 1 repair. The reader and detailed
note now normalize Lemma 3.6's possible zero-length pair sequence to the exact
one-pair impossible path type \(\Omega^\dagger=((S,S))\). The emptiness
recursion now ranges over the required empty \(H\) branch and permits the
\(m=0,\ U_0=\varnothing\) no-run base branch, while preserving Rabin's printed
nonempty branches and identifying both completions as handbook-owned. The
compact record now uses Rabin's defined term `frontiered` and records the
repairs and rejected Round 1 status without claiming admission.

The six revised objects were frozen under the exact hashes in the Round 2
table of `../charter.md`. The charter's corrected R13, R14, R18, and R19 and new
R29 govern the fresh round. Three different blind seats must audit the whole
snapshot, independently recompute the hashes, and visually inspect every Rabin
and Meyer source page. Earlier reports, the ledger, this transcript, staging
material, other board records, and conversation history are forbidden.

This remains manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 2 OPEN.

## Round 2 reconciliation — 2026-08-23

All three fresh blind reports were filed independently on the unchanged Round
2 snapshot and were opened together only after every seat had filed:

- source fidelity: ACCEPT, report SHA-256
  `715A3DFC44D7A70B664EBCCDF58E90D8A1A2506B08B4BDA7E5E6B6AEF21E58A8`;
- mathematical proof: ACCEPT, report SHA-256
  `298044FCF617E1221910A9774125B8AF0D910F926D57C6CD799D71524ECD19AB`;
- adversarial publication: REJECT — `R2-AP-01` and `R2-AP-02`, report
  SHA-256
  `1EBDFEFB017881E9AEDD49F71AC288AF43EEDFD5CEEFF2E87161D973C96A6573`.

The two accepts do not outvote the rejection. The chair checked both findings
against the frozen prose, Rabin's printed p. 30, and the repository terminology
rule. Both are supported must-fixes:

1. `R2-AP-01`: Rabin's term `frontiered` names the property of a finite
   predecessor-closed node set that every nonfrontier node has both binary
   successors. The reader displays the property without attaching the source
   name, standing, or nonredundancy before later use; the detailed note uses the
   name before its display; and the compact record does not locally distinguish
   it from predecessor closure. The first-use gate therefore remains unmet.
2. `R2-AP-02`: the reader correctly requires the distinguished frontier symbol
   (f\notin S\) and then incorrectly calls it a `frontier state`. It is not a
   member of the state set. Its exact standing as the external run value used
   on terminal-frontier nodes must be stated.

Round 2 is rejected. The repaired zero-length, empty-\(H\), and
\(m=0,\ U_0=\varnothing\) mathematics remains accepted by both relevant seats
and survived the adversarial review; it is not reopened by these terminology
findings. A new snapshot and a fresh blind round are required after the two
minimum prose repairs are integrated consistently.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used in the review or reconciliation.

Status: ROUND 2 CLOSED — REJECT.

## Round 3 opened — 2026-08-23

The chair integrated both supported Round 2 repairs consistently across the
reader, detailed source note, and compact record. At first use, `frontiered`
now has Rabin's exact definition, is identified as a property of the finite
tree rather than a second object, is distinguished from predecessor closure,
and is tied to the finite-tree automaton, lift, and emptiness base that require
the distinction. The symbol \(f\notin S\) is now identified throughout as the
distinguished external value assigned at the terminal-node frontier, never as
an ordinary state.

The six revised objects were frozen under the exact hashes in the Round 3
table of `../charter.md`. Three fresh blind seats must audit the complete
snapshot, independently recompute all hashes, and visually inspect every Rabin
and Meyer source page. All earlier reports, the ledger, this transcript,
staging material, other board records, and conversation history are forbidden.

This remains manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 3 OPEN.

## Round 3 reconciliation — 2026-08-23

All three fresh blind reports were filed independently on the unchanged Round
3 snapshot and were opened together only after every seat had filed:

- source fidelity: ACCEPT, report SHA-256
  `15C31C7E12D6C26AF14FEFA3E9E0D79BA1332CCA3E45CA492B545688B0535585`;
- mathematical proof: ACCEPT, report SHA-256
  `1B489B5685273CD0D3B341FD807F23DA0CA4E32DF05D9DD251C22438457D0112`;
- adversarial publication: REJECT — `AP-01`, report SHA-256
  `44806ED69A43F2FE00B79A33C20A238240146FD5830DCCD432B9CE6F5BC233C9`.

The two accepts do not outvote the rejection. `AP-01` is supported: the source
note's admission-history paragraph names `frontiered` and the finite-tree
symbol \(f\) before the later passages that supply their complete first-use
definitions and claim to be their first use. The minimum repair is to remove
both technical names from that history paragraph and refer generically to the
two finite-tree terminology defects. The later definitions, standing,
nonredundancy explanations, and uses are accepted as source-exact and complete.

No mathematical, source-fidelity, complexity, rights, or completion-status
defect was found. The zero-length normalization, both p. 34 empty branches,
the finite-tree reconstruction, and the Meyer correction remain accepted and
are not reopened by this narrow history-language defect.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used in the review or reconciliation.

Status: ROUND 3 CLOSED — REJECT.

## Round 4 opened — 2026-08-23

The chair made the minimum supported Round 3 repair. The source note's opening
review history now refers generically to the two finite-tree terminology
defects and leaves both technical objects to their later complete first-use
introductions. The reader's substantive definitions and the mathematical
reconstruction were unchanged. During the closed-round editing window, the
adjacent TATA record in the shared compact file was also reconciled to its
controlling source; no Rabin claim was altered by that adjacent update.

The six objects were frozen under the exact hashes in the Round 4 table of
`../charter.md`. Three fresh blind seats must audit the complete snapshot,
independently recompute all hashes, and visually inspect every Rabin and Meyer
source page. All earlier reports, the ledger, this transcript, staging
material, other board records, and conversation history are forbidden.

This remains manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 4 OPEN.

## Round 4 withdrawn before filing — 2026-08-23

Before any Round 4 seat filed a report, the chair found a separate literal R26
defect in the frozen snapshot. The reader at line 1017 and the detailed note at
line 230 use Rabin's source-defined operation name `cylindrification` without
giving its definition at either first occurrence. Rabin printed p. 7 defines
the \(\Sigma_2\)-cylindrification of \(B\subseteq V_{\Sigma_1}\) as the
largest \(A\subseteq V_{\Sigma_1\times\Sigma_2}\) with \(p_1(A)=B\).
The minimum economical repair is to replace the undefined name in both records
by plain prose saying that an unconstrained second label coordinate is added.

All three seats were interrupted before filing, and no partial work is treated
as a verdict or review report. The Round 4 snapshot is withdrawn rather than
admitted or reconciled. A new hash-pinned round is required after repair.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used.

Status: ROUND 4 CLOSED — WITHDRAWN BEFORE FILING.

## Round 5 opened — 2026-08-23

The chair made the pre-filing Round 4 repair before opening a new round. The
reader and detailed source note now describe Theorem 1.4 directly: one label
coordinate is projected away and, conversely, a coordinate left unconstrained
at every node is added. The undefined operation name has been removed. The
source note's opening review history also remains generic, so it does not name
technical objects before their complete first-use introductions.

The six revised objects were frozen under the exact hashes in the Round 5
table of `../charter.md`:

- Rabin source PDF:
  `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3`;
- Meyer source PDF:
  `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D`;
- reader presentation:
  `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695`;
- bibliography:
  `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0`;
- detailed source note:
  `78A859CC0069879650417FC27C3E07467D88BA2FB3DDA647574817561A878121`;
- compact source-presentation record:
  `E4C3EDA02743632864D1A056B36A6292667C9F1A23DB06AF88057A530C6D893E`.

Three entirely fresh blind seats must audit the complete Round 5 snapshot,
independently recompute all six identities, and visually inspect every page of
both original-detail source render sets. All earlier reports, all partial and
unfiled Round 4 work, the ledger, this transcript, staging material, other
board records, and conversation history are forbidden.

This remains manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 5 OPEN.

## Round 5 filing recovery — 2026-08-23

The source-fidelity seat sent a completion notice naming its assigned report
path. In reliance on that notice, the chair opened the mathematical and
adversarial reports together, then discovered that the named source-fidelity
file had not materialized in the shared workspace. The chair stopped before
reconciliation, made no frozen-object edit, and disclosed no finding or
verdict to the source-fidelity seat. The same already-completed blind seat was
asked only to restore its report at the assigned path, without reading another
report or any new evidence. It then filed the report on the same unchanged
snapshot.

This was an administrative filing failure, not a substantive independence
breach. The reviewer had completed and announced its blind review before the
chair opened any report; the seat remained isolated from the other reports;
and no manuscript or source object changed. The incident is recorded rather
than hidden. Because Round 5 is rejected on a supported source finding in any
event, no admission depends on this procedural judgment.

## Round 5 reconciliation — 2026-08-23

The three reports on the unchanged Round 5 snapshot are:

- source fidelity: REJECT — `SF-R5-01`, report SHA-256
  `D9654319A63B48AAE03A885E1C804508B515B43913144BB3863D852051DAA9F5`;
- mathematical proof: ACCEPT, report SHA-256
  `8331FBA9C901EDA356C4545E2B628AFF1D394C75B581A6D77BABC1FA3230E631`;
- adversarial publication: ACCEPT, report SHA-256
  `7908C0B8F38853623B6706F2EF56D8F5E9A2E41DE280B9D669EE6DBC31F32BC5`.

The two accepts do not outvote the rejection. `SF-R5-01` is supported by
Rabin printed pp. 30--31 and the frozen records. In the compact presentation
at line 670, two phrases assign Lemma 3.14 a frontiered-finite-tree role.
Printed Lemma 3.12 supplies the finite-tree lift, Corollary 3.13 applies it to
principal formulas, Lemma 3.14 is instead the intervening compactness result
extracting a finite subfamily of infinite-run obligations, and Corollary 3.15
returns to the frontiered-tree machinery for complementation. The reader and
detailed note already preserve that division of labor; only the compact
record requires repair.

No other source, mathematical, terminology, complexity, rights, or
completion-status defect survived the three reviews. The minimum repair is to
replace both inclusive `Lemmas 3.12--3.14` phrases in the compact record with
the exact four-result division above, then freeze a new snapshot for a fresh
blind round.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used in the review, filing recovery, or reconciliation.

Status: ROUND 5 CLOSED — REJECT.

## Round 6 opened — 2026-08-23

The chair made the one supported Round 5 repair. The compact record now
assigns the finite-tree lift to Lemma 3.12, its principal-formula application
to Corollary 3.13, the intervening compactness argument to Lemma 3.14, and the
return to frontiered-tree machinery for complementation to Corollary 3.15. The
reader and detailed source note already had that division; no other Rabin
substantive claim was changed.

During the closed-round editing window, the adjacent TATA record in the shared
compact file was reconciled to its controlling source and reader. Those edits
clarify TATA notation, proof scope, examples, the weak/full logic boundary, and
the abstract-only Thatcher--Wright boundary; they do not supply or alter a
Rabin claim beyond the exact Round 5 repair.

The six objects are frozen under the Round 6 table's exact hashes:

- Rabin source PDF:
  `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3`;
- Meyer source PDF:
  `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D`;
- reader presentation:
  `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695`;
- bibliography:
  `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0`;
- detailed source note:
  `29DAF36E123A2900620D49F018BD5F76BC4EE2FE0AAA7E3F85AAB50B23F37D7B`;
- compact source-presentation record:
  `BB5D7220F75298C6DF3A1934D0DE36F25B9BD64AC5B2B71A141C2A41D3536236`.

Three entirely fresh blind seats must audit the complete Round 6 snapshot,
independently recompute all six identities, and visually inspect every page of
both original-detail source render sets. All earlier reports, all partial and
unfiled Round 4 work, the ledger, this transcript, staging material, other
board records, and conversation history are forbidden.

This is manuscript scholarship. No test, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build
is authorized.

Status: ROUND 6 OPEN.

## Round 6 chair scope clarification — 2026-08-23

After opening the round, the chair reread the adjacent TATA source page while
preparing the next source visit and found a non-Rabin compact-record omission:
the `N-c-015.b` paragraph at line 698 gives TATA's automaton tuple without its
ranked-alphabet component. TATA printed p. 20 and the already-integrated reader
give the literal tuple `A=(Q,F,Q_f,\Delta)`. The compact sentence must receive
the same `F` component before the TATA snapshot is frozen.

This is outside the `N-c-014.d` Rabin target and its Rabin/Meyer evidence set;
it neither supplies nor changes a Rabin claim. The six Round 6 objects remain
unchanged while the Rabin seats work, and no reviewer has been contacted. The
minimum TATA repair is deferred until Round 6 closes, when the shared compact
file is no longer frozen. It will be completed before any TATA review opens.

No test, checker, repository script, TeX command, build, or rendered-handbook
inspection was used.

Status: ROUND 6 REMAINS OPEN FOR `N-c-014.d`.

## Round 6 reconciliation — 2026-08-23

All three reports were physically filed before reconciliation:

- source fidelity: ACCEPT, report SHA-256
  `7C0E4B06E5904B560299C8C187F01E9FAF4789DA9E1FDAF2EAD3C1E8A92CD3D1`;
- mathematical proof: ACCEPT, report SHA-256
  `C2BFA669DB092242953645143F987300DBCB7D79C1485A000FC9A62721A263E6`;
- adversarial publication and terminology: REJECT — `AP6-01`, report SHA-256
  `5B3F8761C255636D03565E02F37CB436AAD0BE401CB102991651D5E1EEAC2266`.

Each seat independently matched all six frozen Round 6 identities and inspected
every required Rabin and Meyer source page. The two accepts do not outvote the
rejection. `AP6-01` is supported by Rabin printed p. 19, Definition 3.2 and
Lemma 3.3. For a nonempty set \(H\), Rabin fixes a mapping
\(h\mapsto H_h\subseteq H\) and calls it well founded exactly when no infinite
sequence satisfies \(h_{m+1}\in H_{h_m}\) for every \(m\); Lemma 3.3 gives the
equivalent lower-ordinal-stratum characterization.

The reader gives that definition correctly. The frozen detailed source note,
however, first names the notion in its printed-page map and later invokes it
without ever defining the no-infinite-descent condition. The frozen compact
record likewise gives only the lower-stratum consequence. The minimum repair
is local to those two records: remove the premature name from the page map and,
at each substantive first use, state the mapping, exact chain condition,
standing, nonredundancy from path acceptance and simultaneous-run merging, and
use in Lemmas 3.3--3.4 and 3.11. No reader mathematics requires alteration.

No other source-fidelity, mathematical, terminology, complexity, rights, or
completion-status defect survived the three reviews. The adjacent TATA tuple
omission recorded above remains outside this verdict and will be repaired in
the now-open editing window before any TATA review.

No test, automated checker, repository script, TeX command, interim handbook
build, handbook-PDF inspection, or build was used in the review or
reconciliation.

Status: ROUND 6 CLOSED — REJECT.

## Round 7 opened — 2026-08-23

The chair made the one supported Round 6 repair. The detailed source note now
removes the technical name from its early page map and, at first substantive
use, defines Rabin's mapping on a nonempty obligation set by the exact absence
of an infinite dependency chain. The compact record gives the same local
definition. Both records state why the condition is needed, distinguish it
from path acceptance and simultaneous-run merging, give Lemma 3.3's equivalent
lower-stratum form, and identify the uses in Lemmas 3.4 and 3.11. The reader's
accepted mathematical reconstruction was unchanged.

During the closed-round editing window, the chair also completed the previously
recorded adjacent TATA repair in the shared compact file: the source tuple now
reads `A=(Q,F,Q_f,\Delta)`, including the ranked alphabet. This edit is outside
the `N-c-014.d` target and changes no Rabin claim.

The six objects are frozen under the Round 7 table's exact hashes:

- Rabin source PDF:
  `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3`;
- Meyer source PDF:
  `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D`;
- reader presentation:
  `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695`;
- bibliography:
  `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0`;
- detailed source note:
  `73A700E83218BD1E0460CD836E72FB7EE86914C52D70D865B903CE367400C944`;
- compact source-presentation record:
  `0EE7C6EAD01590636652D409EA51FD7A34555F410E3277121B165932A233D41F`.

Three entirely fresh blind seats must audit the complete Round 7 snapshot,
independently recompute all six identities, and visually inspect every page of
both original-detail source render sets. All earlier reports, all partial and
unfiled Round 4 work, the ledger, this transcript, staging material, other board
records, and conversation history are forbidden.

This is manuscript scholarship. No test, automated checker, repository script,
TeX command, interim handbook build, handbook-PDF inspection, or build is
authorized.

Status: ROUND 7 OPEN.

## Round 7 reconciliation — 2026-08-23

All three reports were physically filed before reconciliation:

- source fidelity: REJECT — `R7-SF-01`, report SHA-256
  `B162D9230C7D3204EA2F4AAF897CA87B05EEA6EA70FEA83B05F8B04F32B94089`;
- mathematical proof: REJECT — `R7-MP-01`, report SHA-256
  `12F707D40C6876C2A274F7A896817028C7C92C6C2CFC34A62E71DCA77FBA926F`;
- adversarial publication and terminology: REJECT — `AP7-01`, report SHA-256
  `0EA43F0D02F2EFFA503830A9417F716DAB39DD492E47C202510CB8149825C486`.

Each seat independently matched all six frozen Round 7 identities, read the
complete textual snapshot, and visually inspected every required Rabin and
Meyer source page. All three rejections identify one and the same defect, here
consolidated as `R7-STATUS-01`: the detailed source note's opening correctly
records the completed Round 6 and requires Round 7, while its final integration
heading and closing paragraph still describe the pre-Round-6 state. In
particular, frozen line 618 says “after Rounds 1--4,” lines 649--651 omit Round
6, and lines 658--660 direct three fresh Round 6 reviews to begin. Those
statements contradict the same note's lines 18--39, the compact record's Round
7 status, and the controlling Round 7 charter.

No vote or majority rule is involved. The three differently named findings are
one convergent supported must-fix, not three independent defects. Its minimum
repair is confined to the detailed note's review history and the corresponding
pending-round status in the detailed and compact records. The concluding
instruction should be made round-neutral where possible so that the same stale
status is not recreated.

Every seat found the reader's mathematical reconstruction, source numbering,
result roles, formulas and quantifiers, terminology, Meyer correction, rights
boundary, and limited completion scope otherwise correct. No reader
mathematics, bibliography entry, Rabin source claim, or Meyer source claim
requires alteration.

No test, automated checker, repository script, TeX command, interim handbook
build, handbook-PDF inspection, or build was used in the review or
reconciliation.

Status: ROUND 7 CLOSED — REJECT.

## Round 8 opened — 2026-08-23

The chair made the one convergent Round 7 repair. The detailed source note now
uses a round-neutral integration heading, records all rejected rounds through
Round 7 together with the withdrawn Round 4, and states the admission rule
without making an obsolete round number its permanent instruction. Its opening
and closing identify Round 8 as the next review for this snapshot. The compact
record likewise records the Round 7 disposition and Round 8 requirement. No
reader mathematics, source reconstruction, bibliography entry, rights claim,
or wider completion boundary changed.

The six objects are frozen under the Round 8 table's exact hashes:

- Rabin source PDF:
  `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3`;
- Meyer source PDF:
  `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D`;
- reader presentation:
  `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695`;
- bibliography:
  `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0`;
- detailed source note:
  `4C7FA2AFDCED52E1076F5604A826F5AC148707EE0A4AE1772B31F704259F104A`;
- compact source-presentation record:
  `9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2`.

Three entirely fresh blind seats must audit the complete Round 8 snapshot,
independently recompute all six identities, and visually inspect every page of
both original-detail source render sets. All earlier reports, all partial and
unfiled Round 4 work, the ledger, this transcript, staging material, other board
records, and conversation history are forbidden.

This is manuscript scholarship. No test, automated checker, repository script,
TeX command, interim handbook build, handbook-PDF inspection, or build is
authorized.

Status: ROUND 8 OPEN.

## Round 8 reconciliation — 2026-08-23

All three fresh reports were physically filed before the chair opened any
report:

- source fidelity and evidence: ACCEPT, report SHA-256
  `D79C7A3D91A8664647C968432B645A2EED8BCE23230109DACEB597382B0B47B5`;
- mathematical and proof correctness: ACCEPT, report SHA-256
  `C6CFA5E0E5C180B1F1D25D498220DEF4CD1623B52F20E3C9089BEF6FED16F3D2`;
- adversarial publication and terminology: ACCEPT, report SHA-256
  `9C93AB0649A19A8635E8031E5079A4F5DBF2EA4A14C9E02B17051F1CCDF3ED24`.

The chair then read all three reports completely in separate line-numbered
passes and recomputed the six frozen identities and the three report
identities. Every value matched the Round 8 charter and the filed reports. Each
seat read all four textual frozen objects, visually inspected all thirty-six
Rabin physical pages and all six Meyer article pages at original detail, and
expressly disposed of invariants `R01`--`R29`.

All three reports contain no blocker, must-fix, should-fix, consider, advisory,
unread page, source mismatch, mathematical defect, terminology defect, rights
overclaim, status contradiction, or other actionable finding. The Round 8
snapshot is therefore admitted for source acquisition, reader-facing
reconstruction, and topic-level independent manuscript review of `N-c-014.d`
only. This does not admit another `N-c-014` presentation, `N-c-014` overall,
Part IX, any other part, a rendered handbook page, a build, human or user
review, final-book completion, or publication.

The durable admission record is
`spec/research/p09-rabin-1969-independent-review-record.md`, SHA-256
`930A84F232EC66E520D3B0FF55F936DAC95FBFC5180BA189A44D513DE148C168`.
The compact source-presentation file then received only the two status changes
that record this decision and link the durable record. Its accepted
pre-admission SHA-256 is
`9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2`;
its post-admission SHA-256 is
`EAA1CDBC5C3D388CFC7E5915F099F0FBDEE43243D80131EF5ECED0F185FBE6B8`.
No accepted reader mathematics, bibliography entry, detailed source note, or
source object changed after review.

No test, test harness, automated checker, repository script, TeX command,
interim handbook build, handbook-PDF inspection, or build was used in the
review, reconciliation, or administrative admission.

Status: ROUND 8 CLOSED — ACCEPT; `N-c-014.d` MANUSCRIPT CONTENT ADMITTED.
