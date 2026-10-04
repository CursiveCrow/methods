# Round 2 — adversarial publication and terminology review

## Scope and evidence

This is an independent blind Round 2 review. I did not read a chair record,
ledger, Round 1 transcript, another board, or another Round 2 verdict; I did
not contact another reviewer. I read every frozen scope named in the charter:
reader 1--257, shared theorem 811--816, bibliography 6099--6134, source note
1--358, compact record 620--630, and ledger 898. I recomputed every snapshot
hash before substantive review, visually read all 48 rendered report pages at
original detail, and directly read the fixed Bruyère--Hansel--Michaux--
Villemaire source at printed pp. 202--203. I did not edit a frozen artifact or
run a test, checker, repository script, TeX command, build, or handbook-PDF
inspection.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| 1959 report PDF | 18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD | match |
| N-c-014 reader | 843C9FAE64849F6AE57239B05084D7C43D41095512439F00A3AA3F0EB0B208D6 | match |
| Shared theorem | 1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8 | match |
| Bibliography | BB5705BD2223275E25B32146540391D511D907FA779F3872C9CAAB1CAB102515 | match |
| Source note | 1C7D1679188EA891D134FE7498822B365DCBB045C607FE2AD39C6610B2D362E2 | match |
| Compact record/open ledger | EDA1593FCF2F5784718086A7A9747E686E27ABAB992D399362E37F369D732FD3 | match |

No blocker or must-fix finding remains for this mandate.

## Mandatory coverage

| Item | Disposition | Evidence and result |
|---|---|---|
| R2-M01 | checked-clean | All six recomputed hashes match the charter. |
| R2-M02 | checked-clean | Original-detail visual pass confirms PDF 1 cover, 2 funding leaf, 3--47 continuous printed pp. 1--45, and 48 endpoint leaf. |
| R2-M03 | checked-clean | Report p. 7, Definition 2, is the pointwise identity \(U[Y^m]\equiv U[H(Y^m,\bot^n)]\). Reader 47--58, source note 155--173, and compact 624 correctly retain the free state vector on the left and its pointwise standing. |
| R2-M04 | checked-clean | For report p. 17 formula (2), take \(E=\top\), \(H(y,x)=y\), \(U(y)=y\). Definition 2 holds and the actual run remains \(\top\), so all special inputs are accepted. Finite weak \(r\) is eventually \(\bot\), so the printed tail condition is impossible. Reader 108--120 and source note 208--216 state the counterexample correctly. |
| R2-M05 | checked-clean | Reader 121--142/source note 218--232 prove the handbook-owned repair. A finite nonempty downward-closed \(j\) has last true point \(h\); the local clauses trace the actual tuple run through \(h\), force false input from \(h\), and test \(U(r(h))\). Pointwise Definition 2 propagates truth along the omitted tail. Conversely choose \(h\) after input extinction and eventual output truth, retain the actual run through \(h\), and make witnesses false afterwards. This includes \(h=0\), does not assume \(U(\bot^m)=\top\), and remains an existential local successor formula. |
| R2-M06 | checked-clean | Report p. 19's displayed \(s(x)\land\neg s(x+1)\) makes \(x\) the last true point; its prose calling \(x+1\) the length conflicts with p. 8. Reader 171--178/source note 234--236 adopt the coherent displayed-boundary convention, including \(x=0\). |
| R2-M07 | checked-clean | Report p. 20 first requires \(B(\bot,\bot)\), then searches paths with inclusive \(x\leq k\). Reader 180--190/source note 238--244 preserve both. \(x=0\) is included as the all-false one-state path \(Y_0=\bot\), governed by \(K(\bot)\) and the tail guard. |
| R2-M08 | checked-clean | Report p. 24's bit formula rejects genuine \((1,1)\), accepts false \((2,8)\) with \((u,v)=(2,4)\), and remains false after only \(u<v\) becomes \(u<x\), via \((0,6)\). Reader 199--210/source note 256--264 give both counterexamples exactly. |
| R2-M09 | checked-clean | Direct reading of the 1994 source p. 202 records MacNaughton's observation that Büchi's unary \(P_2\) equivalence was not correctly proved and its \(\in_2\) replacement; pp. 202--203 give the \(\in_2/V_2\) equivalence and Semenov's nondefinability of \(V_2\) in \((\mathbb N,+,P_2)\). Reader 212--220/source note 265--267 correctly assign this as later correction evidence. |
| R2-M10 | checked-clean | Report pp. 23--25 state Theorem 4 and pp. 35--36 state Theorem 9. Reader 199--223/source note 256--267 and 311--313 identify their false unary-powers converse and do not retain any dependent base-regularity consequence as sound. |
| R2-M11 | checked-clean | The sound first-order \([=,+,\operatorname{Pw}_2]\)-to-\(W.2.A.\) translation plus the sentence decision procedure proves Corollary 5; the false converse is not used. Reader 221--223/source note 267 say exactly this. |
| R2-M12 | checked-clean | Reader 144--169/source note 269--303 retain terminal \(\top^n\), false tail, and empty marker. Reader 168--169 assigns Theorem 7 analysis to the repair; Theorem 8 is obtained by combining that corrected result with the separately cited finite-automaton characterization. |
| R2-M13 | checked-clean | Report p. 41 says the binary-to-ternary converter consequence “seems to mean.” Source note 311--316 preserves this tentative status and explicitly denies a separately supplied reduction; the reader does not promote it. |
| R2-M14 | checked-clean | The reader, source note, compact record, shared theorem, bibliography, and ledger agree: report content; defective printed Theorem-2 proof plus handbook repair; false unary-powers claim plus later correction; and unreconciled journal version are distinct. Compact 630 and source note 350--358 make closure conditional on fresh blind acceptance. |
| R2-M15 | checked-clean | The terminology audit below checks all corrected names and notation locally. |
| R2-M16 | checked-clean | Report pages control 1959 wording; 1994 pp. 202--203 control later correction only. Reader 8--16 and 252--255, source note 19, 39--43, 328--329, and 350--358, compact 622 and 630, and ledger 898 preserve rights, topic-only scope, no-test/no-build, and unreconciled-journal limits. |

## Source-versus-repair boundary

The snapshot is publication-safe on the decisive attribution distinctions:

- Report p. 7 supplies Definition 2 and pp. 7--8 behavior; reader 47--71
  identifies these as source material.
- Report p. 17 supplies the Theorem 2 statement and its defective formula (2).
  Reader 108--120 calls the defect out rather than laundering the correction
  into report wording.
- Reader 121--142 and source note 218--232 label the complete finite-witness
  proof handbook-owned. The source note explicitly makes Theorem 3,
  Corollaries 1--2, and Theorems 7--8 depend on that repair; reader 168--169
  makes the essential Theorem-7 dependency visible.
- Report pp. 23--25 and 35--36 remain the source of the false unary-powers
  claims. Bruyère--Hansel--Michaux--Villemaire pp. 202--203 is visibly later
  correction history, neither reconstructed 1959 wording nor a claim about
  the unreconciled 1960 journal.
- The 1960 journal is cited for identity only. No frozen sentence claims a
  page-for-page version, correction, theorem-number, or proof reconciliation.

## Terminology and ambiguity audit

| Name or notation | Necessity, exact definition, standing, nonredundancy, and use | Result |
|---|---|---|
| Special output | Reader 47--58 defines the exact pointwise property of \(U\) relative to \(E,H\), distinct from acceptance. It is needed for eventual constancy and the repaired tail proof. | clean |
| Run, output predicate, behavior, finite witness | Reader 59--71 types behavior as a set of special inputs and distinguishes time predicates. Reader 121--142 adds the finite witness only for the handbook repair; its cutoff \(j\) and state tuple \(r\) have distinct roles. | clean |
| Cutoff \(j\) | \(j(0)\), finite quantification, and downward closure give an eliminable initial segment with last point \(h\). It is nonredundant with \(r\), is needed in both repair directions, and works at \(h=0\). | clean |
| \(\operatorname{Pw}_2,P_2,\in_2,V_2\) | The unary powers predicate is defined at reader 199--201. Reader 212--219 defines bit occurrence and \(V_2\), identifies them as later correction, and distinguishes the strictly weaker unary signature. The 1994 source writes its relation in number-first coordinate order; the reader's explicit bit-to-number orientation is a handbook convention matching report \(E(x,y)\), equivalent by variable swap, and is not presented as literal source notation. | clean |
| Last true point; string behavior | Reader 171--178 resolves source length prose by exact boundary formula. Reader 144--167 defines marker and endpoint before string behavior, distinguishing it from eventual behavior. | clean |

No completion inflation remains. “Complete” applies only to the acquired
1959 precursor body, never to correctness of every report claim, the 1960
journal version, N-c-014 admission, another presentation, or the handbook as a
whole. The compact record requires this fresh blind round before closure.

VERDICT: ACCEPT
