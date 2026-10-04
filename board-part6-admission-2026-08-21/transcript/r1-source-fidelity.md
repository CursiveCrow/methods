# Part VI admission board — blind round 1 source-fidelity findings

- seat: source-fidelity/evidence
- round: r1 blind opening
- scope: complete current live graph rooted at `handbook/parts/p06.tex` and `handbook/annex/p06-route.tex`; 23 exact wrappers/artifacts; every routed body/annex addition; Part VI bibliography, notation, new-content, depth, and apparatus records needed for source standing
- independence: I did not read another Part VI seat transcript or speculate about another seat's conclusions
- boundary: read-only review; no manuscript, source, provenance, control, registry, generated, or test edit; no build or test

### F1 [blocker] [open] The live ZFC apparatus prints OPEN/unadmitted workflow debt

- author: source-fidelity r1
- location: route `handbook/parts/p06.tex:4-6`; rendered supplement `handbook/parts/p06/zfc-axiom-table-supplement.tex:15-18`
- claim: The table supplement visibly prints the heading `OPEN ZFC axiom-table apparatus`, `OPEN and unadmitted`, and a list of source/content/AI/build/visual/register/acceptance gates. This violates the charter's no-reader-debt invariant. The other occurrences of `OPEN`, phase IDs, and apparatus IDs in Part VI are comment-only and are not the rendered part of this finding.
- evidence: The file is input between exact intervals `SRC-10089-10271` and `SRC-10272-10352`; it is not dormant control evidence.
- exact correction: Resolve F3-F8 first. Then replace lines 15-18 by ordinary source attribution explaining that the separately authored table summarizes but does not replace the exact ZF/ZFC axiom statements. Keep unresolved admission/build/visual/user gates in controls, not reader prose.
- status: open.

### F2 [blocker] [open-external] All exact destinations and Part VI obligation admissions remain administratively open

- author: source-fidelity r1
- location: all 23 records `spec/provenance/SRC-10060-10088.json` through `spec/provenance/SRC-11338-11353.json`; `spec/provenance/reviewed-handbook-unit-records.json:5`; `spec/provenance/reviewed-register-obligation-records.json:6`; relevant open rows of `spec/register-obligation-closure.csv`
- claim: Exact source identity is clean, but no admission record yet binds the final Part VI reader graph or this board's results. All 23 destinations remain `open/missing`, all 23 independent-source fields remain pending, all 253 completeness fields remain pending, and both reviewed-record arrays are empty.
- evidence: Direct current parsing produced `records=23`, `open=23`, `independent_pending=23`, and `completeness_pending=253`. Those controls are not replaced by the exact comparison reported below.
- exact correction: After source/content repairs freeze, regenerate the construction snapshot/live inventory and add hash-bound reviewed-unit and reviewed-obligation records for body, annex, bibliography, registry, tables, figures, and generated audit. Update the 23 exact records individually. Preserve build, visual, human-compatibility, and final-user gates as later boundaries.
- status: open external boundary.

### F3 [must-fix] [open] Historical-derivative headers claim fewer edits than the live slices contain

- author: source-fidelity r1
- location: `handbook/parts/p06/zfc-axiom-table-supplement.tex:2-14`; retained evidence `handbook/parts/p06/axioms-hierarchy.tex:52-156`; `handbook/parts/p06/ordinal-rank-supplement.tex:1-14`; retained ordinal evidence `handbook/parts/p06/axioms-hierarchy.tex:288-460,505-514,530-564`
- claim: The ZFC supplement says historical lines 52-156 differ only at the stale ordered-pair and omega consumers. Direct slice comparison finds a third undeclared change: the table caption drops the rendered `(apparatus A-058)` text. The ordinal supplement says its three historical slices are exact apart from surrounding control comments and one descriptive section boundary. Direct comparison finds additional caption edits deleting `A-060`, `A-129`, and `A-130` from the ordinal-law and two figure captions. The removals are sensible reader cleanup, but the “only/exactly” lineage claims are false until those deltas are declared.
- evidence: ZFC comparison differences are at current `zfc-axiom-table-supplement.tex:32-34,59-60,94-95`; ordinal differences are at `ordinal-rank-supplement.tex:65-66,184-187,238-241`. The controlling historical captions remain in the cited retained file.
- exact correction: Do not restore internal apparatus IDs. Amend each derivative header/provenance delta list to enumerate every intended caption/navigation edit, then re-pin the derivative hashes. Apply the same audit to the other “exact historical slice” derivatives before admission; an undeclared cleanup is still a lineage defect.
- status: open.

### F4 [blocker] [open] The registered proof of Choice-to-Zorn remains an explicit sketch with omitted construction obligations

- author: source-fidelity r1
- location: contract `spec/registers/depth-gaps.csv:2` (`D-P1-001`); body `handbook/parts/p06/cardinals-choice-supplement.tex:123-164`; annex `handbook/annex/p06/cardinals-choice-supplement.tex:14-47`
- claim: D-P1-001 requires Zorn's lemma with a proof from Choice and equivalence noted. The body is `sketched=annex:p6.choice.1`; the annex's `sketchnote` explicitly omits set-coding and Replacement in the Hartogs-stopping recursion, the Hausdorff/Tukey reductions, Tychonoff, and the compact-Hausdorff/BPI calibration. It gives a useful AC-to-Zorn architecture and a partial implication cycle, but it is not the registered complete proof.
- evidence: The missing set recursion is load-bearing: the transfinite sequence of chosen strict upper bounds must exist as a set before Hartogs can stop it. The remaining equivalences are merely delegated to the cited source while the body theorem asserts all seven as one equivalence theorem.
- exact correction: Complete the Hartogs-bounded recursion with the required Replacement/coding and supply full reciprocal proof coverage for the body theorem, or split the statement so only a genuinely proved subtheorem carries `proved=` and the remaining equivalences carry citation status. D-P1-001 cannot be discharged by the present `sketched=` item without an explicit contract change.
- status: open.

### F5 [should-fix] [open] The registered Silver/PCF entry contains Silver but no reader-facing PCF pointer

- author: source-fidelity r1
- location: contract `spec/registers/new-content.csv:37` (`N-a-036`); comment-only promise `handbook/parts/p06/cardinal-arithmetic-supplement.tex:18-20`; live endpoint `handbook/parts/p06/cardinal-arithmetic-supplement.tex:226-234`; remote further-reading mention `handbook/parts/p06/determinacy.tex:126-127`
- claim: N-a-036 requires a Silver theorem statement and a PCF pointer. The Silver theorem is present and correctly scoped to singular cardinals of uncountable cofinality. The cardinal-arithmetic chapter then ends without naming PCF, explaining its relationship to the countable-cofinality gap, or citing Shelah. A comment says the row remains a stub; the only rendered Shelah reference is a distant item in the final determinacy chapter, unattached to Silver's boundary.
- exact correction: Add a bounded paragraph immediately after Silver identifying PCF as the excluded theory addressing singular-cardinal arithmetic, especially countable cofinality, and cite `Shelah1994Cardinal`. State explicitly that no PCF theorem is imported.
- status: open.

### F6 [must-fix] [open] Registered primary and method sources are missing or unattached at their Part VI claims

- author: source-fidelity r1
- location: source contracts `spec/registers/new-content.csv:45-49,68-69` (`N-a-044`--`N-a-048`, `N-a-067`, `N-a-068`) and bibliography intake `spec/registers/apparatus.csv:183`; live claims `handbook/parts/p06/constructibility-forcing-supplement.tex:18-29`, `handbook/parts/p06/forcing-variants-supplement.tex:95-170`, `handbook/parts/p06/large-cardinals-absoluteness.tex:19-25,86-107,140-206,225-389`, `handbook/parts/p06/descriptive-set-theory.tex:234-241`
- claim: The live text has strong modern sources, but several explicitly registered historical/method roles were never entered or attached. `Levy1965`, `Shoenfield1961`, `Levy1960`, `Devlin1984`, `ScottSolovay1967`, and `Sacks1990` are absent as bibliography keys and at the claims they are registered to support. `Ulam1930` and `Keisler1962` exist in the bibliography but are not attached to measurability/ultrapower history. The fine-structure sentence calls itself a pointer without a Devlin/Jensen locator; the Boolean-valued presentation calls only on Bell despite the registered Scott--Solovay role; the lightface bridge omits Sacks.
- evidence: Lévy's primary hierarchy source is *A Hierarchy of Formulas in Set Theory*, Memoirs AMS 57 (1965), 76 pp. ([AMS record](https://bookstore.ams.org/MEMO/1/57)); Devlin's registered monograph is *Constructibility* (Springer, 1984). Bell's authoritative modern account explicitly describes the Boolean-valued method as developed by Scott and Solovay ([OUP book record](https://doi.org/10.1093/acprof:oso/9780198568520.001.0001)).
- exact correction: Add exact records (using an honest `@unpublished`/historical-note standing where the Scott--Solovay material was circulated rather than formally published) and cite each only at the concrete role it supports. Attach Ulam and Keisler at the measurable/ultrapower history. Retain Jech/Kanamori/Moschovakis/Bell as modern formulation sources; primary attribution does not replace modern theorem support.
- status: open.

### F7 [should-fix] [open] The Aronszajn construction promised by N-a-040 is reduced to a cited existence statement

- author: source-fidelity r1
- location: contract `spec/registers/new-content.csv:41` (`N-a-040`); live definitions/theorem `handbook/parts/p06/infinitary-combinatorics.tex:190-245`, especially `:219-224`
- claim: N-a-040 asks for trees, the Kőnig lemma, an Aronszajn-tree construction, and a Suslin-independence survey. The binary Kőnig proof and Suslin survey are present. The Aronszajn entry only states existence, says the cited construction verifies countable levels/no cofinal branch, and provides no construction architecture at all. Calling the source a “cited construction” does not supply the registered construction.
- exact correction: Add a status-honest construction method at survey depth: specify the tree objects/levels and the recursive step that keeps levels countable while excluding a cofinal branch, with Kurepa/Todorcevic attached to their roles. If only the existence theorem is intended, explicitly downgrade the register wording from “construction” to “statement.”
- status: open.

### F8 [blocker] [open] Mandatory Part VI master/audit apparatus is absent, and the large-cardinal ladder stops short of its literal apparatus contract

- author: source-fidelity r1
- location: contracts `spec/registers/apparatus.csv:66,70,114,135` (`A-065`, `A-069`, `A-113`, `A-134`); live ladder `handbook/parts/p06/large-cardinals-absoluteness.tex:391-422`; explicit absence `:4-6,437-442`; route `handbook/parts/p06.tex:37-38`
- claim: A-058--A-064, A-066--A-068 and figures A-129--A-133/A-135 are substantively present and source-safe. But A-113's generated Part VI audit remains expressly unrouted and untrustworthy. The master consistency-strength table A-069 and matching figure A-134 are absent. The local A-065 table stops at supercompact while its literal apparatus row asks for “inaccessible through supercompact and beyond”; the file itself says the chart stops and contains no beyond-supercompact row.
- exact correction: Repair the audit generator to traverse the live Part VI graph and route the generated register with an ordinary caption/label. Build A-069/A-134 in their declared whole-book/master location with exact nonlinearity/conditional-existence caveats. Either add the intended beyond-supercompact calibration to A-065 with a source and treatment ceiling or amend that apparatus contract to “through supercompact.” Do not infer completion from the existing local ladder alone.
- status: open.

## Checked-clean and not-checked coverage

### Whole route, exact artifacts, lineage, references, and statuses

- **Checked clean:** `handbook/parts/p06.tex:3-36` routes exactly 23 wrappers once each in contiguous authority order `SRC-10060-10088` through `SRC-11338-11353`. `handbook/annex/p06-route.tex:13-16` routes only the three nonoverlapping annex additions and preserves the declared P6/P7 transition.
- **Checked clean:** all 23 wrappers contain one matching restoration scope/artifact. Direct comparison with `source/formal-logic-reference.tex:10060-11353` found 23/23 records, 1,294/1,294 lines, zero mismatch. No exact inherited unit is duplicated or altered.
- **Checked clean with F3 exceptions:** the routed historical derivatives preserve their declared source-slice order and exclude overlapping historical bodies/annexes. The confirmed undeclared caption deltas are isolated in F3; no active statement identity is duplicated by a retained historical file.
- **Checked clean statically:** the rooted body/annex graph has 166 active statement/navigation/annex identities with no duplicate; all 63 distinct references resolve; all 34 inline citation keys and all 23 editorial `cited=` keys exist; and all eight `proved`/`sketched` targets have exactly eight reciprocal annex items, with no missing target or orphan.
- **Checked clean:** the notation registry and both generated symbol surfaces contain 586 one-to-one rows with no duplicate stable ID. P6 source/editorial variants such as ordinal versus Baire `\omega^\omega`, P-name versus Boolean-name hierarchies, Boolean versus formula connectives, forcing orientation, partition arrows, diagonal intersection, diamond/square/modal glyphs, lightface/projective/Lévy/Borel classes, and choice principles are explicitly separated.

### Lot 1 — exact axioms, hierarchy/rank, ordinals, cardinals, Choice

- **Checked clean:** exact ZF/ZFC language, all axioms/schemata and side conditions, omega construction, ordered-pair proof, set recursion status, ordinal trichotomy/transitivity, transfinite induction/recursion, cumulative hierarchy/rank, Mostowski collapse, equipotence, Hartogs, order vocabulary, the exact four-clause Choice cycle, aleph/CH/GCH boundaries, and exercises.
- **Checked clean:** the added ZFC table's formulas agree with exact source; ordinal recursion is on the right argument; noncommutativity/distributivity failures and Cantor normal form are correct; the epsilon-zero/cumulative-hierarchy figures make only schematic/conditional claims. Cardinal operations, cofinality, König, Hausdorff recursion, Easton, and Silver state their Choice, regularity, cofinality, and ground-model ceilings.
- **Checked clean:** weaker-choice definitions and implication/noncomparison diagram; countable-dependency table; choice-free binary Kőnig/fan proofs; ZF/ZFC system-variant conventions including NF's source/Lean/paper-review separation. The Wilshaw project paper itself states that Lean verifies the TTT model while Con(NF) also uses the NF--TTT equiconsistency bridge, matching the handbook's wording ([project paper](https://leanprover-community.github.io/con-nf/print/print.pdf)).
- **Findings:** F1-F5, F8.

### Lot 2 — exact constructibility/forcing and routed forcing additions

- **Checked clean:** exact Def/L hierarchy, L theorem/status, countable-transitive-set forcing convention, filters/dense/genericity, names/evaluation, semantic/recursive forcing separation, monotonicity, forcing theorem import, Cohen real, relativized derivations, relative CH/non-CH consistency, nonderivability, and ctm warnings/exercises. No editorial addition upgrades those inherited statuses.
- **Checked clean:** forcing vocabulary fixes stronger-is-smaller orientation, ccc, and `Add(omega,kappa)` before use. Condensation has its elementary-substructure hypothesis. The ccc preservation, nice-name, and many-Cohen-real claims have complete reciprocal annex proofs. Forcing, constructibility, and independence figures/tables distinguish pedagogical ctm forcing, Boolean-valued quotients, permutation/ZFA models, pure-ZF transfer, and relative-consistency directions.
- **Checked clean:** Cohen/random/collapse catalog states exact posets and avoids blanket collapse/cofinality claims; Boolean-valued names/truth are separated from P-names/two-valued forcing; the Fraenkel model's atom/pure-set boundary and citations are explicit; proper/countable-support/PFA/MM work is only a declared pointer.
- **Findings:** F2, F3, F6, F8.

### Lot 3 — combinatorics, cardinal arithmetic, large cardinals, reflection/absoluteness

- **Checked clean:** regular-uncountable club/stationary context, diagonal clubs, Fodor's stationary conclusion, delta systems, complete Cohen-ccc proof, partition-arrow types, Ramsey/Erdős--Rado scopes, exact tree/level/branch definitions, Suslin tree/line distinction, diamond/square no-thread clauses, and MA's ccc/dense/filter hypotheses. The MA iteration is honestly excluded.
- **Checked clean:** Lévy hierarchy versus projective classes, formula/base-relative equivalence caveat, bounded/Sigma1/Pi1 transfer directions, finite-family reflection, Shoenfield same-ordinals/ground-real parameter scope, and the forcing application. Large-cardinal definitions/implications are conditional, include the exact closure/critical-point/ultrafilter hypotheses, distinguish tree property from weak compactness, and do not assert existence or strict adjacent consistency gaps.
- **Findings:** F4-F8.

### Lot 4 — descriptive set theory and determinacy

- **Checked clean:** Polish/Baire definitions; countable-ordinal bold Borel hierarchy; analytic/coanalytic/projective definitions; Suslin's theorem; distinct Baire/perfect-set/universal-measurability properties; analytic ZFC regularity; the coanalytic perfect-set independence boundary; lightface pointer; and the Borel/projective table/figure operation meanings.
- **Checked clean:** Gale--Stewart game/strategy types, open/closed and Borel determinacy source statuses, AD/PD distinction, AD-versus-Choice scope, Woodin embedding definition, and the Martin--Steel sufficient-hypothesis/non-equivalence ceiling. No projective regularity or determinacy hypothesis is read back into ZFC.
- **Findings:** F2, F6, F8.

### Not checked / external gates

- No build, test, generator run, PDF inspection, counter/bookmark/TOC check, table/figure/index rendering, visual review, administrative admission, human review, or final-user acceptance was performed. Those remain separate from this source/content opening.

## Prioritized repair checklist

1. Remove the rendered OPEN/unadmitted/gate notice after the substantive source repairs freeze (F1).
2. Complete or split the Choice-to-Zorn equivalence proof so its status matches D-P1-001 (F4).
3. Correct every derivative delta declaration and re-pin the cleaned historical slices (F3).
4. Add the missing primary/method bibliography records and attach all registered source roles, using honest unpublished standing where appropriate (F6).
5. Add the local PCF pointer after Silver and the promised Aronszajn construction architecture (F5, F7).
6. Complete or contract-correct A-065, A-069, A-113, and A-134 (F8).
7. Only after the final source/content bytes freeze, close the 23 exact destinations and reviewed-unit/obligation records; do not merge those controls with build/visual/user acceptance (F2).
