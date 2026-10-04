# P5 internal arithmetic prerequisites: blind publication-text review

Date: 7 September 2026. Reviewer: fresh publication-text review context, assigned at 21:33 UTC. Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.

## Verdict and scope

**PASS for the frozen prerequisite unit's publication text. PT-1 remains OPEN. The current downstream assertion that the previously selected PA predicate satisfies D2 and D3, and the GL claims using that exact predicate, do not pass integration review.**

All three assigned manuscript files were read in full, together with the complete edition contract. This review found no new blocking error in their definitions, standing, proof dependencies, or local proof placement. The specified PA graph construction, invariant corollary, bounded-evidence construction, D1 lemma, and numerical modus-ponens constructor are presented with the appropriate limits. Their local acceptance does not establish the standard internal PA checker or confer formal admission.

The review was filed without reading either other new prerequisite review or the author's research/conclusion note. Search output incidentally exposed filenames and isolated lines from the disjoint new `standard-pa-proof-predicate.tex` files; those files were neither opened nor assessed and supply no evidence for this verdict. No manuscript, driver, symbol, bibliography, provenance, or other review file was edited. No build, render, regression test, or formal checker was run. The only output owned by this reviewer is this report.

| Scope | Result | Evidence and limit |
| --- | --- | --- |
| Complete read and assigned snapshot identity | PASS | All three target extents and SHA-256 values match the assignment. The route, canonical symbols, and two isolated candidate views also match. |
| Definitions, types, and order of prerequisites | PASS | Fixed descriptions and graph clauses precede their theorem; arithmetic is established before sequence extension; sequence extension precedes recursion and finite collection; evidence clauses precede their verification. |
| Q versus PA, and numerical versus internal assertions | PASS | The cited Q theorem, PA induction proofs, standard-model checker theorem, and D1 implication retain separate and explicit strengths. |
| Fixed description versus uniform evaluator | PASS | Both body and annex explicitly restrict the construction to separately fixed finite descriptions. The evidence construction is likewise for a fixed formula. |
| Internal arithmetic proof dependencies | PASS | No use of internal sequence coding, a total evaluator, or a checker invariant is silently assumed to prove the prerequisite that would supply it. This is a mathematical text assessment, not formal proof checking. |
| D1 and numerical modus-ponens presentation | PASS | D1 uses an actual standard proof code and numeralwise representation. The constructor is for the certified numerical relation and respects the actual body premise order and certificate order. |
| Root annex route, proof scope, and reference targets | PASS | The route inputs the new annex before the existing depth supplement. The numerical constructor proof lies inside `annexitem`; the arithmetization theorem anchor is supplied by the Part V driver. Build/reference-output validation remains separate. |
| Required symbol amendment and all appended rows in both candidate views | PASS | Canonical line 56 and lines 934–942 agree with the corresponding table and index entries, including the standing and remaining obligations. This does not validate rendered geometry or admit those generated views. |
| Local statement of remaining checker, D2, D3, and proof-builder obligations | PASS | Annex lines 474–524 expressly leave the exact checker formula and its internal invariants to be supplied. |
| Existing PT-1 integration: previously fixed PA predicate and downstream GL use | FAIL; OPEN | The live derivability chapter and GL chapter still assert/use properties not established for the arbitrary numeralwise representative fixed by the earlier definition. See the finding below. |
| Restoration provenance, source-fidelity admission, static/build/visual gates, and publication admission | UNRESOLVED in this review | They require their separate evidence. The two enlarged restoration files are being handled separately for provenance; this report does not accept their wrappers' historical exactness. |

## Findings

### PT-1: the standard-predicate integration remains open

**Status: existing integration failure, confirmed current; not a new defect introduced by the prerequisite proofs.**

At `handbook/restoration/inherited-09328-09438.tex:474–493`, the proof-predicate definition still selects a particular Sigma-one formula only through numeralwise representation in Q. It explicitly acknowledges that the numerical checker does not establish the internal derivability conditions for that chosen formula. The new D1 proof at lines 496–521 supplies the first condition and does not claim the latter two.

Nevertheless, `handbook/restoration/inherited-09750-09816.tex:41–44` continues to assert all three conditions for PA and its fixed proof predicate. Its preceding lines 7–11 identify that predicate with the earlier definition. The new annex states the outstanding construction at `handbook/annex/p05/internal-proof-predicate.tex:474–524`: fix the PA axiom/certificate convention, select the actual checker description and arithmetic formula, prove internal row-shifting and certificate invariants, and construct and verify the evidence-to-proof builders. The universal arithmetic proof needed for D2 is not the numerical implication proved in the new constructor lemma. Bounded arithmetic evidence alone is not the ND proof code needed for D3.

The same exact-predicate dependency remains live in `handbook/parts/p05/provability-logic-gl.tex:45–64`, which instantiates the earlier definition and claims GL arithmetic soundness from its derivability conditions. Lines 86–111 state the arithmetical-completeness result for that exact predicate, and lines 176–202 use D2, D1, D3, and the completeness theorem in the dictionary. The citations to standard provability results do not, merely by appearing there, identify the unspecified earlier representative with the predicate whose required properties are proved in those results.

**Consequence:** the current reader route still exceeds the established predicate construction at these downstream statements. None of the local PASS judgments closes PT-1, establishes D2/D3 for `mathsf{Prov}_PA`, or accepts the GL instantiation. The necessary correction is the promised exact predicate construction and verified connection to its consumers, followed by review of the affected claims. Relabeling the numerical theorem or bounded evidence as that construction would not supply the missing proof.

### No new local publication-text blocker found

The following checks explain the positive local verdict and its extent.

1. **Representation strength is explicit.** `inherited-09262-09327.tex:4–29` distinguishes numeralwise relation representation from functional representation. Lines 31–48 retain the Q theorem's cited status. The new section at lines 67–158 gives the specified PA construction and its stronger universal totality/uniqueness and defining equations. It does not derive those equations from external primitive recursiveness or from agreement in the standard model. The addition example's proof in Q uses finitely many numeral equations; the later graph arguments explicitly use PA induction.

2. **The graph recursion has a noncircular foundation.** The description grammar refers to the earlier primitive-recursion definition, whose zero functions include arity zero. Empty composition and nullary cases are explicitly handled at body lines 94–95 and annex lines 236–237. The annex establishes elementary PA arithmetic, division, and the actual pairing/beta graph before beta extension. Its finite-congruence proof uses an induction on two accumulated natural values and an arithmetic target relation, rather than presupposing a coded sequence or factorial. Beta extension then supports finite evidence collection and the recursion graph's existence and defining equations. The restriction direction reuses a prefix of one beta code and does not assume a unique code for a finite sequence.

3. **Formula complexity follows the actual hierarchy definition.** `inherited-08306-08438.tex:61–94` defines the syntactic Sigma-one class by closure under conjunction, disjunction, marked bounded quantifiers, and unbounded existential quantification after a fixed negation-normal-form conversion. The recursion graph uses exactly those operations. The annex's complexity argument at lines 278–285 does not perform an invalid bounded-universal/unbounded-existential interchange. The beta-entry formula used is the fixed bounded formula at `inherited-08439-08709.tex:27–69`; the new PA pairing/division proof supplies its internal strength rather than importing that strength from the earlier standard-model lemma.

4. **Finite evidence is defined and proved before its proposed proof-theoretic use.** The bounded-evidence theorem is stated at body lines 235–253 and proved by explicit clauses at annex lines 312–405. A whole bounded subformula takes the first clause, removing ambiguity with the connective clauses. The construction handles both strict and non-strict marked bounds, fresh auxiliary variables, dependent witnesses, and the empty strict bound. Internal finite collection handles the bounded-universal converse. The final paragraph and the separate boundary explain that an evidence value has not yet become a checked ND derivation.

5. **D1 has the right quantifiers and hypotheses.** At `inherited-09328-09438.tex:496–521`, the proof starts from an actual metatheoretic derivation, obtains a standard numerical proof code from the coding theorem, invokes the positive numeralwise-representation clause in Q, uses Q's inclusion in T, and applies the actual existential-introduction rule. It claims a metatheoretic implication for every fixed sentence, with no additional internal uniformity claim.

6. **The numerical modus-ponens constructor is tied to the encoded calculus.** The body fixes all twenty rules, nonvacuous formula-specific discharge, explicit alpha conversion, the stronger all-variable freshness condition for existential elimination, and the body order for implication elimination. These agree with the inspected substitution, deduction, and rule-sheet dependencies. In the annex, the first input proves the implication and the second its antecedent; the output places the antecedent rows first, shifts only the implication tree's premise indices, appends rule tag 8, and concatenates certificates in the resulting open-leaf order. Input lengths are positive before decrementing root indices. Formula/term parameters and discharge labels are not row references. Label collisions across the two input trees cannot create a new discharge, because their new common ancestor discharges nothing. The constructor's preliminary checks do not call T's axiom test, so its stated independence from T is respected. Its theorem explicitly uses the certified numerical convention; the optional finite-axiom alternative is not silently substituted.

7. **References and physical proof scope are coherent in the inspected source.** `handbook/parts/p05.tex:11–20` reads the representation unit first and installs the arithmetization label on the first theorem of the coding unit. That unit's only theorem is the intended arithmetization theorem, so the new D1 reference resolves at source level. The body references the correct annex label and the specific new pairing lemma. `handbook/annex/p05-route.tex:13–15` supplies one Part V annex heading and inputs the prerequisite annex before `depth-completion-supplement`. The new `annexitem` spans lines 4–472, including the complete numerical constructor proof at lines 423–471. This meets the proof-environment scope requirement visible at `handbook/handbook.sty:1610–1641`. The following `proofboundary` contains no `proof` environment.

8. **The shared symbols preserve standing.** Canonical line 56 explains numeral bars and typed argument tuples. Appended lines 934–942 distinguish the description, denoted function, specified arithmetic graph, local triangular value, congruence abbreviation, fixed-formula bounded evidence, numerical proof constructor, local concatenation, and the remaining predicate/proof-builder targets. The descriptions of `mathsf{mp}` and `rho,P_rho,B_sigma` explicitly withhold PA D2/D3. Every required row appears with the corresponding symbol-registry target in the candidate table and alphabetical index. No field makes a uniform-evaluator or completed-checker claim.

## Snapshot and read manifest

SHA-256 values below are of the whole files. Read extents describe the actual text inspected, rather than implying that a whole-file hash is a whole-file content review. Paths are relative to `C:\Dev\the-methods-of-reason` unless otherwise stated. Lines count blank lines.

### Assigned artifacts

| Artifact | File lines | Read extent | SHA-256 |
| --- | ---: | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 168 | Full | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/restoration/inherited-09262-09327.tex` | 253 | Full | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | 546 | Full | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | 524 | Full | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/annex/p05-route.tex` | 15 | Full | `CB9713160EDEB4AFC683ECB9D7D456A284BBC24F3B3A31A4AD600BEAEEF8A07F` |
| `handbook/registry/symbols.csv` | 942 | Header; lines 50–58 and all appended lines 934–942; targeted symbol searches | `264BDA8982448B5AC31919B136F35BE66767198930E437B3B7EFF4BAB9FA2C8A` |
| `tmp/edition-2026-p5-prerequisites-candidate/symbols-tables.tex` | 1152 | Line 260; lines 428–440, including all appended entries at 430–438 | `4B5AFA27752DA5A82A12D68449633E6F183570C3E10A9571C16668CE6CF71508` |
| `tmp/edition-2026-p5-prerequisites-candidate/symbol-index.tex` | 942 | Lines 4, 47, 80, 83, 121, 451, 466, 503, 785, 832 | `C19DEABE432213035A96C9F31B4DF9B6B91AF771EFB4DDCE60D9CE8B5EE3EB86` |

The canonical CSV has 941 data rows plus its header. The cited line numbers 934–942 are physical CSV lines, matching the generated `entry:symbol-registry-00934` through `00942` targets.

The root's scope-only annex adjustment was independently checked without writing another manuscript: removing the closing `annexitem` line currently at 472 and reinserting that exact line immediately before current line 406 recovers the supplied author SHA-256 `C653BF3E1A42E541310435AAA9082238DF6B78EEDD349400DD252ED26A5083F2`. This establishes the reported relocation relation between the two byte sequences. It does not establish restoration provenance or publication output.

### Manuscript and routing dependencies inspected

| Artifact | Read extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p05.tex` | Full, 52 lines | `068B90E56BFCF4538AFF14F0DBBF428A228A34B12736CA55484B1E3D5E64B326` |
| `handbook/restoration/scope-SRC-09262-09327.tex` | Full, 3 lines | `65DCDECA00CACDD15A4483691054AB980AF87F178750B5852B358BBD16D12604` |
| `handbook/restoration/scope-SRC-09328-09438.tex` | Full, 3 lines | `3D56970059846AE57BC9A1C4E150224B1D4A80F7EB7CC497BB65E33F529BD6A3` |
| `handbook/main.tex` | Lines 19–52 | `E4ED41CD71B429DC5113A1F75B381686C9D03574E20DCE6846426CDCB891B000` |
| `handbook/handbook.sty` | Lines 1595–1645 and proofboundary definition search at 501 | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `handbook/restoration/inherited-07678-07752.tex` | Full, 75 lines | `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD` |
| `handbook/restoration/inherited-08306-08438.tex` | Full, 133 lines | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08439-08709.tex` | Full, 271 lines | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |
| `handbook/restoration/inherited-08710-08876.tex` | Lines 805–865; checked the cited statement and initial proof dependencies, not its complete proof | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |
| `handbook/restoration/inherited-09099-09111.tex` | Full, 13 lines | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09112-09149.tex` | Full, 38 lines | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |
| `handbook/restoration/inherited-09150-09174.tex` | Full, 25 lines | `7C36BE695AAF1AA32F9DFA45AF894C9C5413F02254B1BA3C9142B1C878156DDD` |
| `handbook/restoration/inherited-09175-09187.tex` | Full, 13 lines | `0DB98B87928AA115C82883993E2E25B18286779E7DED0399C7148633C0178430` |
| `handbook/restoration/inherited-02193-02340.tex` | Lines 1–65 | `5BA27894EDF744D288008B613ADF93EAC3D65385F745135DE776D5B6011316A3` |
| `handbook/restoration/inherited-03240-03428.tex` | Full, 189 lines | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/restoration/inherited-03927-04061.tex` | Full, 135 lines | `2AD2846970D4976177B0FBB8AC59FF8106253F5D155A5E4861956F7F651BF480` |
| `handbook/registry/calculi/nd-fol.tex` | Full, 29 lines | `F25549BC18FC4AAE212EEA32CADC9FFFD08E03D712F5DF10E9DA62F660BE5370` |
| `handbook/restoration/inherited-09750-09816.tex` | Full, 67 lines | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` |
| `handbook/parts/p05/provability-logic-gl.tex` | Full, 205 lines | `9AD6D30124B666C8845B421FA40BED296CC59621D0F733C7053581C870EF183E` |

Search-only navigation through other LaTeX files located named definitions and references; it is not an assessment of those files. The existing depth-completion supplement was located as the second route input, but its content was not re-reviewed. No primary bibliography source was acquired or audited in this publication-text context.

The mandatory memory quick pass used `C:\Users\Crow\.codex\memories\MEMORY.md:861–862` only for the earlier review/admission discipline. Every current manuscript claim above rests on the inspected live files. No old content-acceptance conclusion was reused.

## Handoff

This is a bounded publication-text PASS for the exact prerequisite snapshot in the manifest, with the existing PT-1 integration failure preserved. The report's own SHA-256 is returned in the filing message, outside the file to avoid a self-referential hash. Separate source, topic, provenance, static/build, rendered-page, and admission evidence remain governed by the edition contract.
