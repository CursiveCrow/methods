# Round 1 — adversarial publication and terminology review

## Scope and evidence

This was a blind review of only the charter's frozen six-object snapshot and
the charter-named rendered report pages. I did not read a ledger, a chair
record, a prior-board file, another transcript, or another verdict; I did not
contact another reviewer. I did not edit a frozen artifact, run a test,
checker, repository script, TeX command, build, or handbook-PDF inspection.

I directly read every stated manuscript/source-record scope: reader lines
1--213; shared theorem lines 811--816; bibliography lines 6099--6120; complete
source note lines 1--318; compact record lines 620--630; and the relevant
narrowed open/sufficient-body ledger entries. I visually inspected, at
original detail, every rendered source page 01--48. This confirms the physical
map independently of OCR: cover (PDF 1), funding leaf (PDF 2), continuous
printed pp. 1--45 (PDF 3--47), and the repository endpoint leaf (PDF 48).

### M01 — frozen identity

All six hashes were recomputed before substantive review and exactly match the
charter.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| PDF report | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD | match |
| N-c-014 reader | 1D4E34CE6B2602BEF520146ECC6F78C492A969CE6C8FE884912DC0959AFF6713 | match |
| Shared finite-word theorem | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 | match |
| Bibliography | FAACDA885C9671FD41509F0FCB24934CBA0B4AFD8BC1E6368C2DE355E8B03DFA | match |
| Complete source note | 15165056F88D051DB0A5CB33B3C55A79F39AF2EEE62C507C756226CF851B411E | match |
| Compact record | E7DD8167EA70A32F72F09C12A478637F8C5ECCB3C7AA6E98BCC7918ECFB00285 | match |

## Blocking findings

### AP-01 — The reader replaces the printed special-output identity with a different one

- Severity: must-fix.
- Source evidence: printed report p. 7, Definition 2 (rendered PDF page 9)
  defines \(U[Y^m]\) to be a special output exactly when the propositional
  identity
  \[
    U[Y^m]\equiv U[H(Y^m,\bot^n)]
  \]
  holds. The left side is evaluated at an arbitrary transit-state vector
  \(Y^m\), not at the one constant vector \(\bot^m\).
- Frozen-manuscript locations: reader 47--56, especially 49--54; source note
  150--168, especially 152--156; compact record 624.
- Violated invariants and coverage: I6; M06, M20--M22, and M24.
- Graduate-reader harm: the frozen text writes
  \(U[\bot^m]\equiv U[H(Y^m,\bot^n)]\). This makes the left side constant while
  the right side still has free \(Y^m\), and it specifies a different, generally
  stronger property. The printed identity says that, after a false input, the
  output is unchanged by one transition from *every* transit state. That is the
  fact used to establish eventual constancy and to delimit the source's special
  output/behavior construction. A reader cannot recover the literal source
  definition from the current formula.
- Smallest exact repair: replace \(U[\bot^m]\) by \(U[Y^m]\) in the displayed
  special-output identity in reader 51, source note 155, and compact record
  624. Retain the existing \(U[H(Y^m,\bot^n)]\) right side and the typed
  explanation that follows.

### AP-02 — The finite sentence-decision account omits the false-tail guard and changes the source bound

- Severity: must-fix.
- Source evidence: printed report p. 20 (rendered PDF page 22), Corollary 1,
  first states that one may assume \(B[\bot,\bot]\), since otherwise the
  sentence is false. Only under that guard does a finite path ending at
  \(\bot\) extend to the required eventually-false state predicate. The same
  page reduces the test to a sequence \(Y_0,\ldots,Y_x\) with
  \(x\leq k\), where \(k\) is the number of states. It deletes a loop whenever
  \(x\geq k\); it does not prescribe a strict-below-\(k\) search.
- Frozen-manuscript locations: reader 139--148, especially 142--147; source
  note 207--219, especially 211--217. The compact record's high-level
  “bounded-length candidates” summary at 626 does not repair the two exact
  omissions in its underlying reader/source record.
- Violated invariants and coverage: I10; M12, M20, M21, and M24.
- Graduate-reader harm: as written, a finite path that first reaches the
  all-false state may be treated as a witness even when
  \(B[\bot,\bot]\) fails and therefore cannot be continued into the required
  special tail. For example, take a start state \(A\) with an allowed transition
  \(A\to\bot\), but no allowed \(\bot\to\bot\) transition. The stated
  abbreviated search accepts the finite path, whereas the source sentence is
  false. Independently, “shorter than that bound” can be read as excluding the
  source-permitted case \(x=k\).
- Smallest exact repair: in reader 142--148 and source note 211--217, state:
  first test \(B[\bot,\bot]\); if it fails, the sentence is false. Otherwise
  decide whether there are \(x\leq k\) and states
  \(Y_0,\ldots,Y_x\) with \(K[Y_0]\), all consecutive \(B\)-transitions, and
  \(Y_x=\bot\). Explain that a witness with \(x\geq k\) has a repeated state,
  so loop deletion yields one with \(x\leq k\). The compact summary may remain
  high-level once those controlling accounts are corrected.

## Mandatory coverage disposition

Every mandatory point was checked. A clean disposition means only that no
additional defect was found in the stated point; AP-01 and AP-02 remain
unresolved must-fixes and therefore control the verdict.

| Point | Status | Evidence and adversarial disposition |
|---|---|---|
| M01 | checked-clean | The independent hashes above equal the frozen charter values. |
| M02 | checked-clean | Original-detail visual review of all 48 pages confirms cover, funding leaf, continuous printed pp. 1--45, bibliography pp. 44--45, and endpoint leaf. |
| M03 | checked-clean | Cover p. 1 and source note 23--39 support the September 1959 UMR1083 report. Bibliography 6099--6120 and compact record 622 distinguish it from the 1960 journal article, its DOI, and the access-controlled 1990 reprint. The no-licence research-copy boundary is express in source note 19 and 41--53. |
| M04 | checked-clean | Report pp. 2--4 visibly give all variable sorts, \(0\), successor, special predicates as eventually false, \(n\)-predicates, and the no-deductive-structure qualification. Reader 18--29 and source note 87--101 preserve the interpreted-theory standing. |
| M05 | checked-clean | Report pp. 6--7, Definition 1, gives formula data \(E^m,H^m[Y^m,X^n]\), its transition recursion, and binary output. Reader 31--48 and source note 128--149 correctly present deterministic formula-defined bit-state data rather than a modern tuple. |
| M06 | finding-linked: AP-01 | The source definition is literal and visually legible on p. 7. The frozen reader/source note/compact record substitute \(\bot^m\) for its free \(Y^m\) on the left side. |
| M07 | checked-clean | Report pp. 7--8, Definition 3, quantifies only over special inputs and requires eventual permanent truth of the output. Reader 57--69 and source note 160--168 distinguish input predicate, output predicate, and behavior set. |
| M08 | checked-clean | Report pp. 5--6 prints Lemma 1 and the five-stage architecture. Source note 103--126 records zero elimination, successor normalization, prenexing, Behmann movement, and finite-initial-segment replacement without calling the lemma an automaton theorem. |
| M09 | checked-clean | Report pp. 8--14 separates complement (Lemma 2), expanded form (Lemma 3), guessed track/look-ahead (Lemmas 4--5), existential input removal (Lemma 6), and local base automaton (Lemma 7). Reader 84--91 and source note 170--179 preserve their different roles. |
| M10 | checked-clean | Report pp. 16--17 constructs Theorem 1 from Lemma 1, the local base, expanded form, alternating complement, and special-track removal. Reader 84--91 and source note 181--190 describe that construction rather than collapsing it into generic closure. |
| M11 | checked-clean | Report pp. 17--18 explicitly converts the cutoff number to a finite initial-segment predicate and uses special output to restrict the transit witness. Reader 93--112 and source note 191--205 report the substantive special-witness step. |
| M12 | finding-linked: AP-02 | Report pp. 18--20 supports Definition 5, Theorem 3, and Corollary 1, but p. 20 requires both the false-tail guard and the \(x\leq k\) convention omitted/misstated in reader 139--148 and source note 211--217. |
| M13 | checked-clean | Report pp. 20--21 proves both directions of ultimate periodicity and says phase/period are effectively found. Reader 150--152 and source note 219--220 maintain that exact strength. |
| M14 | checked-clean | Report pp. 23--25 gives the finite-predicate binary map, carry formula, power-of-two bit predicate, both translations, and Corollary 5. Reader 150--160 and source note 221--231 keep the map typed rather than identifying predicates with numbers. |
| M15 | checked-clean | Report pp. 30--31 gives data positions through \(h\), terminal \(\top^n\) at \(h+1\), false tail, and the empty marker at zero. Reader 114--137 and source note 233--256 retain all endpoint conventions. |
| M16 | checked-clean | Report pp. 31--32, Definition 6 and Theorem 6, distinguishes arbitrary-output string behavior from eventual special-output behavior and proves both directions. Reader 128--137 and source note 254--256 preserve that distinction. |
| M17 | checked-clean | Report pp. 32--33 states effective Theorem 7 and all four Theorem 8 conditions, explicitly referring to the already cited regular-language result. Reader 128--137 and source note 258--265 neither promotes the dependency into a new source proof nor drops a condition. |
| M18 | checked-clean | Report pp. 34--41 defines regular relations in Theorem 8′/Definition 7 and develops binary/base-\(k\) regularity and its consequences. Source note 267--280 reports them accurately. The compact reader does not falsely attribute an unprinted modern relation theorem; its bounded presentation does not rely on any omitted base-conversion claim. |
| M19 | checked-clean | Report pp. 41--42 identifies union, concatenation, and star at the formula level and identifies finite-set quantification with feedback. Reader 160--165 and source note 277--280 give the same limited conceptual claim. |
| M20 | finding-linked: AP-01, AP-02 | The reader, complete source note, and compact record otherwise reconcile identity, source level, version, rights, word encoding, and theorem strength. The special-output formula is repeated incorrectly in all three, and the two controlling decision accounts share AP-02. |
| M21 | finding-linked: AP-01, AP-02 | Page/theorem locators were checked against every rendered source page. The relevant failures are exact formula/edge-condition transcription defects, not locator defects: Definition 2 p. 7 and Corollary 1 p. 20. |
| M22 | finding-linked: AP-01 | \(W.2.A.\), special predicate, \(n\)-predicate, transit predicate, output predicate, behavior, string behavior, and regular relation receive necessary standing and use. “Special output” is the one named distinction whose supplied definition is not its exact source definition. |
| M23 | checked-clean | Reader 8--16, 179--210; source note 1--3, 31--39, 282--290, and 310--318; and compact record 622 and 630 all retain the report/article/reprint boundary. “Closed” is explicitly limited to 1959-report reconstruction/source strength, while journal fidelity and independent scholarly review remain separate. |
| M24 | finding-linked: AP-01, AP-02 | AP-01 makes a displayed identity type-ambiguous; AP-02 hides a material tail hypothesis and makes the bound susceptible to an off-by-one reading. No additional material prose ambiguity was found. |
| M25 | checked-clean | Rights are limited to a research copy (source note 19); scope is report-strength only (reader 8--16 and 189--210; source note 310--318); and the no-test/no-build boundary is express at reader 212--213 and source note 318. |

## Terminology and hostile-reader audit

Apart from the AP-01 definition defect, every new or source-derived technical
designation in scope satisfies the AGENTS rule: it is necessary, is defined or
declared at first use, has a stated standing, is distinguished from adjacent
objects, and has later use.

| Designation | Necessity, exact standing, nonredundancy, and use | Result |
|---|---|---|
| \(W.2.A.\) | Source name defined at reader 18--29 as an interpreted theory with finite-set predicate quantification, not a calculus or alternation fragment; used in the two correspondence directions. | clean |
| Special predicate and \(n\)-predicate | Exact eventual-false/finite-set and tuple definitions at 19--24; required to distinguish source witnesses from arbitrary infinite predicates and to type behavior. | clean |
| Automaton data, transit predicate, output predicate, and behavior | Formula tuple, deterministic recursion, time predicate, and accepted set have separate definitions and standings at 31--69; each is used in Theorems 1--2 and the finite-word bridge. | clean except AP-01's special-output identity |
| Expanded form, string behavior, regular relation | Each is source-defined or explicitly cross-referenced as source-defined; none is used to silently replace the other. Their different roles are recorded in source note 170--179 and 233--267. | clean |
| \(\Sigma_n\), terminal marker, and phase/period | The finite alphabet and marker receive an exact eliminable encoding at 114--127. The phase/period statement is source-controlled and used only for Corollary 2. | clean |
| Modern finite-word MSO correspondence | Reader 194--210 labels it a modern construction and expressly refuses to substitute it for the special-predicate encoding or unreconciled journal bodies. The shared theorem 811--816 is a public theorem statement, not a claim of literal report wording. | clean |

The principal hostile-reader attacks otherwise fail: the reconstruction does
not equate weak finite-set quantification with later full-set infinite-word
logic; does not attribute a nondeterministic set/function tuple to the report;
does not confuse behavior with string behavior; does not claim a report/journal
page reconciliation; does not infer a redistribution licence; and does not
promote source acquisition or precursor reconstruction into topic admission.

The two listed findings are publication-blocking because they alter the
source's central special-output definition and its literal finite decision
procedure. They require correction and a new frozen blind round before this
seat can accept the snapshot.

VERDICT: REJECT — AP-01, AP-02
