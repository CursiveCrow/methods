# Round three — adversarial publication and terminology seat

## Scope, blindness, and evidence boundary

This is an independent blind review of the round-three seven-object snapshot
named in the board charter. I read the charter in full before reviewing the
snapshot. I did not read the ledger, chair transcript, an earlier Part IX board
record, another current transcript, or contact another seat. No frozen artifact
was edited. No test, checker, script, TeX command, handbook build, or
handbook-PDF rendering was used. The only non-reading operation was the
charter-permitted SHA-256 identity check below.

## Snapshot identity confirmation

All seven SHA-256 values were recomputed with the platform file-hash command
and match the round-three charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `0C72F461A83E421AAFF950E2CBA03FD386EEA088BAC70E9D8E30E86052E977D2` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `75D66211C3520522D7530C609221AB20C0409EBBA6CBCD29BD9C3CD9B8D8DD27` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `C2526F8FF7FAFFE4DB2902799BB968E0B21491B57CCC40F6548EEB6BAA534031` | match |

## Direct source and frozen-text reading record

### Visual source inspection at original detail

- `journal-page-1.png` through `journal-page-5.png`, the complete controlling
  journal article, were visually inspected at original detail. These are
  printed pp. 181--185. In particular, this pass read the p. 181 title block,
  authors, venue, date, receipt/revision dates, copyright notice, and execution
  convention; the exact safety and liveness clauses on p. 182; the uniform,
  absolute, leads-to, predictive, and until material on p. 183; the topology,
  Theorems 1--2, both corollaries, and closure paragraph on p. 184; and the
  qualified conclusion and references on p. 185.
- `tr-page-01.png` through `tr-page-11.png`, every file page of the comparison
  report, were visually inspected at original detail. This includes the outer
  cover; the dated title/abstract leaf; internally numbered body pp. 1--8; and
  the references leaf. The report's source form of the exact clauses, examples,
  theorem proofs, the two corollaries, and its conclusion were compared with the
  journal. Its second corollary also says *closed under intersection*.

### Frozen manuscript and source-record reading

- `handbook/parts/p09/presentations/n-c-012.tex`, every in-scope line
  2632--3011.
- `handbook/parts/p09/logic-in-computer-science.tex`, every in-scope line
  710--718.
- `handbook/bib/handbook.bib`, every in-scope line 6056--6080.
- `spec/research/p09-alpern-schneider-1985-source-note.md`, every line 1--681.
- `spec/research/p09-source-presentations-lot2-3.md`, every in-scope line
  395--552.

The journal title block and the official DOI citation record agree with the
frozen bibliography and source note on title, authors, *Information Processing
Letters* 21(4), 7 October 1985, pp. 181--185, and
`10.1016/0020-0190(85)90056-0`. The source note's distinct TR 85-650 entry
agrees with the report cover and title leaf: 30 October 1984, revised 20
February 1985. The source note preserves receipt 5 November 1984 and revision
20 February 1985 from journal p. 181. See source note lines 10--34, 46--49,
645--670; bibliography lines 6056--6080; and compact record lines 397--415.

## Round-three correction audit

| Required correction | Evidence and disposition |
|---|---|
| Distinguish conditional source liveness from the unqualified source non-absolute claim for leads-to | Checked clean. Journal p. 183 and report body p. 5 condition the liveness sentence on satisfiable \(E_2\), then make the non-absolute claim without that qualification. The reader records both source strengths and labels the three-hypothesis state-set result as a handbook repair: `n-c-012.tex`:2773--2805; source note:281--324; compact record:470--483. |
| Type one-state finite words, constant executions, concatenations, and cylinders before use | Checked clean. `n-c-012.tex`:2635--2656 declares \(S\ne\varnothing\), \(S^*\), \(S^\omega\), the typed concatenation, finite prefix, \(\langle s\rangle\), \(s^\omega\), and \(\preceq\) before their later witnesses and cylinders. The cylinder is defined at 2840--2845 before \([\langle b\rangle]\) occurs at 2966. The same sequence appears in source note:97--140 and compact record:423--429, 491--493. |
| Use the source-exact name *until* | Checked clean. The journal p. 183 and report body p. 6 print **Until**. The reader uses “until” at `n-c-012.tex`:2831, source note:357, and compact record:488; it introduces no “strong-until” name. |
| Put the leads-to defect in the source-critical table | Checked clean. `p09-alpern-schneider-1985-source-note.md`:634--641 includes AS-06, identifies journal p. 183 and report body p. 5, states the two different source strengths, and requires the explicit handbook repair. |
| Limit the Plotkin decomposition to a reported, independently unverified private communication | Checked clean. The source pages identify Plotkin as private communication (journal p. 184; report body p. 7). The reader calls the claim source-reported, unproved in the article, and independently unverified at `n-c-012.tex`:2905--2909; source note:468--472 and 594--599; compact record:512--516. |

The claimed state-set leads-to hypotheses are also correct at the stated
strength. With \(E_2\ne\varnothing\), \(e_2^\omega\) is a common suffix; if
\(e_2\in E_1\), its next occurrence supplies the strict later response.
With a state \(c\notin E_1\cup E_2\) and \(e_1\in E_1\),
\(c^\omega\) satisfies vacuously while
\(\langle e_1\rangle\mathbin{\smallfrown}c^\omega\) fails, so the property
is not absolute. Conversely, an empty \(E_1\) makes the property the whole
space; an empty \(E_2\) leaves an \(E_1\)-prefix without a continuation; and,
with no state outside \(E_1\cup E_2\), every satisfying suffix must contain a
later \(E_2\) response and therefore works after every finite prefix. Thus the
three conditions are jointly necessary and sufficient for the reader's
uniform-but-not-absolute separation, not conditions silently attributed to the
source. This is accurately stated at `n-c-012.tex`:2781--2805 and source
note:293--324.

## Publication, proof-strength, and terminology audit

### Source ownership and publication boundary

I1 and I6--I12 are satisfied.

- The journal remains controlling throughout: `n-c-012.tex`:2993--3003,
  source note:36--49 and 82--95, and compact record:401--419 explicitly call
  the report a separate comparison witness. The visual comparison confirms the
  asserted substantive agreement and the shared defective Corollary 2.1 word.
- Source claims, handbook reconstruction, and source defects remain separate.
  The topological direction proofs are expressly reader-supplied
  (`n-c-012.tex`:2853--2859; source note:397--400), as are the exact state-set
  leads-to repair and the Corollary 2.1 repair/countermodel
  (`n-c-012.tex`:2794--2805, 2938--2971). The printed source wording is never
  overwritten.
- The source prints the proofs of Theorems 1 and 2 but states the
  safety/closed and liveness/dense equivalences; that distinction is accurately
  reported at `n-c-012.tex`:2999--3003 and source note:580--603. Theorem 1 is
  not promoted to uniqueness, low computational cost, or a syntax-preservation
  result (`n-c-012.tex`:2890--2903). The conclusion is not promoted to a
  formal correctness or uniqueness theorem (3001--3003).
- Printed p. 181's Elsevier copyright notice is kept distinct from the
  author-hosted access route. No open licence, republication right, or broader
  copyright conclusion is asserted: `n-c-012.tex`:3005--3007; source
  note:46--49; compact record:411--415.
- The section is unlettered, does not invent `N-c-012.e`, and does not claim
  topic admission, a build, rendered handbook review, human acceptance, or
  user acceptance: source note:36--39 and 673--681; compact record:414--415,
  546--552; `n-c-012.tex`:3007--3011.

### AGENTS terminology rule

No coined reader term violates the necessity, definition, standing,
nonredundancy, and use rule (I3--I4).

| Term or symbol | Local standing, definition, distinction, and use | Result |
|---|---|---|
| *live for \(P\)* | A relation of \(u\in S^*\) and \(P\subseteq S^\omega\), exactly \(\exists y\in S^\omega\;u\mathbin{\smallfrown}y\in P\); it is distinguished from universal liveness and immediately used to state it (`n-c-012.tex`:2689--2704). | checked clean |
| uniform and absolute liveness | Source semantic subclasses of properties, each given an exact quantified definition, distinguished by one suffix versus every satisfying suffix, and used in the leads-to/predictive separations (2731--2828). | checked clean |
| \(P_{A,B}\) | An eliminable displayed property name, with its state-set hypotheses, used immediately to prove live-but-not-uniform behavior (2807--2828). | checked clean |
| \(L_P\) | An eliminable metalinguistic alpha-renaming of the source's \(L\), defined by the displayed set equation and used in the Theorem 1 factorization/density proof (2861--2888). | checked clean |
| \(E_a,E_b\) | Eliminable alpha-renamings of the source's \(L_a,L_b\), exactly defined as properties of eventually constant tails and used for Theorem 2 and the Corollary 2.1 countermodel (2911--2936). | checked clean |
| \(Q,\mathcal F\) | Respectively the exact singleton property and an exact possible denotation family, used only to prove that printed intersection closure is insufficient (2951--2971). | checked clean |

The remaining \(\Sigma\) is the source's conditional variable for a notation
expressing properties, not a reader-invented technical name; its closure
hypotheses are preserved where it is used (`n-c-012.tex`:2896--2903,
2938--2949). Descriptive phrases such as “state-set rendering” and “neutral
\(c\in S\setminus(E_1\cup E_2)\)” carry their complete eliminable content in
the displayed state-set relation and are not new uneliminated technical
entities.

## Hostile-reader premortem

| Plausible publication failure | Concrete exposure check | Result |
|---|---|---|
| A reader mistakes a handbook repair for source text. | Follow each non-source proof or correction to its ownership label and to the printed page. | No failure: reader-owned proofs/repairs and the two printed defects are visibly labelled; the journal stays controlling. |
| A reviewer alleges a false “all leads-to properties” theorem. | Separate the source's conditional liveness sentence from its unqualified non-absolute sentence, then test the three degenerate state-set cases. | No failure: the text preserves the source discrepancy and proves the exact conditional repair, including necessity. |
| A one-state finite word or an infinite constant execution is silently substituted for the other. | Trace \(\langle e_1\rangle\), \(c^\omega\), \(e_2^\omega\), concatenation, and \([\langle b\rangle]\) back to their declarations. | No failure: every object is typed before use and the finite/infinite distinction is explicit. |
| A modern or invented temporal-logic label is laundered into the 1985 source. | Compare the heading and prose of the source's example with the reader wording. | No failure: both witnesses print *Until*; the reader uses only *until*. |
| Theorem/proof language exaggerates what the article establishes. | Compare p. 184 and report body pp. 6--8 with the reader's claims about proofs, topology, Corollary 2.1, and Plotkin. | No failure: printed proofs, stated equivalences, reader proofs, a defective corollary, and the private communication remain separately classified. |
| A new name hides an undefined object or changes its logical type. | Apply I3--I4 to every named relation, semantic class, property, factor, and denotation family in the reader. | No failure: the table above locates exact eliminable definitions, standing, nonredundancy, and actual use. |
| Author-hosting is mistaken for an open licence or source access is mistaken for admission. | Check the p. 181 copyright notice against rights/status wording in all three frozen records. | No failure: the notice is preserved; no licence, republication, completion, build, or acceptance claim is made. |

## Mandatory coverage

| Point | Status | Evidence |
|---|---|---|
| M01 | checked-clean | All seven hashes recomputed and matched above. |
| M02 | checked-clean | Original-detail visual reading of journal pp. 181--185 and report file pages 1--11 recorded above. |
| M03 | checked-clean | Journal p. 181; report cover/title leaf; source note:10--34, 46--49, 645--670; bibliography:6056--6080; compact record:397--415. |
| M04 | checked-clean | Both visual page maps and source note:51--95 establish separate status, substantive agreement, and the identical Corollary 2.1 wording. |
| M05 | checked-clean | `n-c-012.tex`:2635--2663; source note:97--162; compact record:423--451. |
| M06 | checked-clean | Exact safety quantifiers and bad-prefix reading at `n-c-012.tex`:2677--2688; source note:164--194. |
| M07 | checked-clean | Prefix/property relation, universal liveness closure, nonemptiness, and full-space boundary at `n-c-012.tex`:2689--2729; source note:196--225. |
| M08 | checked-clean | Motivation, maximality boundary, examples, and stuttering qualification at `n-c-012.tex`:2706--2724; source note:154--157, 188--194, 220--225. |
| M09 | checked-clean | Exact uniform/absolute definitions, standing, distinction, use, and chain at `n-c-012.tex`:2731--2771; source note:227--279. |
| M10 | checked-clean | Source/reader leads-to distinction and fixed-suffix conclusion at `n-c-012.tex`:2773--2805; source note:281--324; journal p. 183 and report body p. 5. |
| M11 | checked-clean | Predictive property, all four nondegeneracy hypotheses, liveness, and non-uniformity at `n-c-012.tex`:2807--2828; source note:326--353. |
| M12 | checked-clean | Source-exact until, total correctness, and rejection of a dichotomy at `n-c-012.tex`:2830--2838; source note:355--371. |
| M13 | checked-clean | Cylinder basis and both direction proofs at `n-c-012.tex`:2840--2859; source note:373--400. |
| M14 | checked-clean | Theorem 1 construction, algebra, minimality/density proof, and precise limits at `n-c-012.tex`:2861--2894; source note:402--452. |
| M15 | checked-clean | Corollary 1.1's complement/intersection/closure requirements at `n-c-012.tex`:2896--2903; source note:454--466. |
| M16 | checked-clean | Theorem 2 alpha-renamings, density, disjointness, factorization, and \(|S|>1\) at `n-c-012.tex`:2911--2936; source note:474--507. |
| M17 | checked-clean | Printed Corollary 2.1, its countermodel, and union/Boolean repair at `n-c-012.tex`:2938--2971; source note:509--559; journal p. 184 and report body p. 8. |
| M18 | checked-clean | Every Boolean closure entry and the only-both claim at `n-c-012.tex`:2973--2991; source note:561--578. |
| M19 | checked-clean | Printed proofs, stated equivalences, and handbook-supplied arguments are distinguished at `n-c-012.tex`:2853--2859, 2993--3003; source note:580--603. |
| M20 | checked-clean | Full AGENTS audit above; exact definitions occur before every subsequent use. |
| M21 | checked-clean | Reader, shared definition, bibliography, source note, and compact presentation agree on standing, source status, semantics, corrections, and boundaries. |
| M22 | checked-clean | Unlettered standing, rights, topic-only status, and no-test/no-build boundary at `n-c-012.tex`:2993--3011; source note:36--49, 673--681; compact record:411--415, 546--552. |

## Finding records

No R3-AP finding record is filed. I found no blocker or must-fix under the
adversarial publication and terminology mandate; the potential failures above
are addressed by the frozen text rather than left implicit.

VERDICT: ACCEPT
