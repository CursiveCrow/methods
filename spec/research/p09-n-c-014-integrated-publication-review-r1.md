REJECT

# N-c-014 integrated adversarial publication and terminology review — Round 1

## Scope and evidence discipline

This is a blind review of the actual reader source, not of a rendered handbook. I read `handbook/parts/p09/presentations/n-c-014.tex` directly from line 1 through line 1596, including every display, comment, blank-line boundary, citation, and source/handbook ownership sentence. I also read `handbook/parts/p09/logic-in-computer-science.tex` lines 836--945, including the host theorem statements and the `n-c-014` input at line 936.

The only supporting records consulted were the five permitted source notes, the `N-c-014` section and consolidated open-source bullets in `spec/research/p09-source-presentations-lot2-3.md`, and the relevant bibliography entries in `handbook/bib/handbook.bib`. No ambiguity required consultation of an original historical-source page.

I did **not** open or inspect any manuscript PDF, PNG, rendered page, page image, or other manuscript derivative. I did **not** run TeX, a build, a test, a checker, a repository script, a hash, or any automated validation. I did **not** open any dedicated prior review, admission record, board file or board ledger, charter, transcript, chair report, or linked independent-review record. Prior-round prose embedded inside the expressly permitted source notes and compact status record was not used as evidence for this verdict.

## Verdict

The source and handbook ownership boundaries are unusually careful, and the presentation is admissible in substance at the stated source-bounded strength. It is nevertheless **not publication-admissible in its present LaTeX form**. Four definition/terminology defects and one locator defect remain in operative claims. The first two affect central proof presentations; all five are mechanically local to repair, but none can be waived under the supplied definition-before-use rule.

The open Büchi 1960 journal reconciliation and Thomas 1997 final-chapter reconciliation are **not** reasons for rejection. The manuscript accurately limits those presentations to the acquired 1959 and 1996 precursors. The rejection rests only on defects in the actual LaTeX.

## Must-fix findings

### 1. Elgot's corrected infinite-sequence equality introduces unbound arities and an undefined semantic operator

**Lines:** `n-c-014.tex` 403--461, specifically 405--416, 419--430, and 432--448.

The passage defines the restricted formula shape

\[
\exists\mathbf s\,\forall x\,M(\mathbf a,\mathbf b,\mathbf s,x)
\]

and defines the window length `n`, but it never binds `m`, `m'`, or `r` as the lengths of the displayed tuples. Line 425 then first introduces

\[
T^\infty_{m+m'+r}(\bigwedge_x M)
\]

without defining `T^\infty_d(C)`. The surrounding prose says that the objects are “unprojected models” and “infinite sequences,” but it does not give the eliminable definition required to determine:

- the alphabet and type of those sequences;
- how a tuple of predicate assignments becomes one characteristic-column sequence;
- whether `T^\infty_d(C)` denotes assignments, encodings, models, or a language of encodings; or
- how the subscript `d` is related to the free predicate coordinates.

The notation is not decorative. It is the left side of the erratum's central equality and the object projected in the synthesis reduction. Its standing and exact denotation are therefore proof-operative. Line 435 also uses `\operatorname{field}(R_j)` for an `n`-ary relation without defining whether “field” is the union of its coordinate projections or a common carrier already fixed for every coordinate. The coordinatewise tagging display makes an exact definition easy, but does not itself eliminate the ambiguity in the preceding carrier declaration.

This fails Definition, Standing, and definition-before-use. It also prevents the reader from checking that the finite tagged union has exactly the same semantic type as the formula model set.

**Required repair:** at lines 403--425, bind the tuple arities (for example, `\mathbf a` of length `m`, `\mathbf b` of length `m'`, and `\mathbf s` of length `r`); define `T^\infty_d(C)` as the set of infinite `d`-bit characteristic-column sequences whose associated predicate assignment satisfies `C`; and either define the field/carrier of an `n`-ary relation or state the common finite alphabet directly. Then retain the existing `S_j`, tagging, projection, and `n=1` completion.

### 2. The Rabin worked translation uses the source-specific finite-tree object before defining it

**Lines:** first operative use at `n-c-014.tex` 1092--1096; exact definition delayed until 1278--1306.

The worked principal-formula example says that “a finite tree in Section 3.10's sense” can contain the witness and its child and that a finite-tree definability fact plus Lemma 3.12 lifts the witness language. This is a substantive proof step, not a casual preview. At that point the reader has not been told that the relevant finite object is finite and predecessor-closed, that the source's `frontiered` condition requires both children at every nonterminal node, that a finite valuation labels only the complement of the terminal frontier, or that the corresponding automaton uses a distinguished external frontier value.

Those facts appear only at lines 1278--1306. The later text itself explains why the condition is nonredundant with predecessor closure and why the lift and principal-formula construction require it. That explanation confirms that ordinary-language “finite tree” cannot safely substitute for the source-specific definition at line 1092. A reference to the historical source's Section 3.10 is not a reader-local definition and does not satisfy definition-before-use.

This fails Definition-before-use and Use at the exact point where the object first supports an argument.

**Required repair:** move the minimum exact finite-tree/frontier definition and its standing/nonredundancy sentence to the worked example before line 1092, or defer the worked example until after the existing definition. Do not merely insert the adjective `frontiered` there unless its exact definition is moved with it.

### 3. “Covering operator” is used as a proof-critical technical name without a typed definition

**Lines:** `n-c-014.tex` 721--729.

The phrase “the source's covering operator” first appears while the text explains the converse for closed homogeneous sets and the separate empty-set case. The passage says only that it “follows permitted extensions among nonempty portions” and has image equal to the closure. It does not state its domain, codomain, input parameters, output coordinates, or the rule that turns a path through portions into an output stream. Yet totality and nonempty image are immediately used to show why the construction cannot handle the empty set.

The name is therefore neither an eliminable abbreviation nor an exactly defined operator at first use. Its standing is underdescribed precisely where the empty-set repair depends on that standing.

**Required repair:** either remove the technical name and describe the required typed map directly, or give its exact source definition at line 721, including domain, codomain, construction from permitted portion extensions, and image. Preserve the existing explicit statement that the nonempty restriction and empty-set case split are handbook-owned.

### 4. The Thomas conclusion introduces the class name `\Sigma^1_2` without definition, necessity, or later use

**Lines:** `n-c-014.tex` 1576--1586, specifically line 1583.

The text says that existential state tracks and a universal path set yield “the stated `\Sigma^1_2` form,” but no `\Sigma^1_2` form has been stated or defined in this Thomas passage. The notation is not assigned a standing as a formula class, its matrix restrictions are not stated locally, its difference from the already explicit `existential tracks + universal path set` description is not explained, and the name is not used again.

This fails Necessity, Definition, Standing, Nonredundancy, and Use under the supplied technical-name rule. It is especially avoidable because the preceding words already state the operative quantifier architecture without the label.

**Required repair:** delete the unused class name and retain the explicit quantifier description, or define the exact formula family at that location and identify the later result for which the distinction is needed.

### 5. Elgot's exact report/article/errata comparison lacks exact locators

**Lines:** `n-c-014.tex` 478--485.

This paragraph makes three page-level version claims: the report has the corrected projection symbol at two corresponding locations; it shares the reversed ordered pair; and it shares the false single-relation assertion. It then supplies only unlocated whole-work citations to `Elgot1959Report` and `Elgot1962Errata`.

The permitted source record supplies the exact locations: report p. 4 for the two projection-symbol occurrences, report p. 6 for the reversed pair, report p. 41 for the single-relation assertion, and errata pp. 558--559 for the published corrections. Because the paragraph's entire purpose is exact version comparison and correction ownership, whole-work citations to a fifty-page report and two-page erratum are not sufficiently precise.

**Required repair:** add the report and errata page locators to the claims at lines 478--485. No substantive rewrite is required.

## Complete line-range audit

The following range ledger records the disposition of every substantive block in the audited presentation. Display continuation lines inherit the disposition of the paragraph that introduces them.

| LaTeX lines | Publication/terminology disposition |
|---:|---|
| 1--17 | **Pass.** The title and Büchi report/article boundary are immediate and explicit. The 1959 report is identified as the reconstruction body; identical 1960 wording, numbering, proof detail, and pagination are expressly not claimed. |
| 18--71 | **Pass.** `special predicate`, `n`-predicate, `W.2.A.`, the propositional-data automaton, transit predicate, special output, and behavior are defined with distinct standings before use. “Weak” is disambiguated from alternation and full-set quantification. |
| 73--142 | **Pass.** Synthesis and analysis have explicit directions. The printed Theorem 2 failure, counterexample, repaired finite-witness clauses, proof idea, and handbook ownership are separated cleanly. |
| 144--229 | **Pass.** The terminal-marker word encoding, empty-word case, string behavior, finite-word equivalence, decision guard, periodicity consequence, false unary-powers claim, later `\in_2`/`V_2` correction, and surviving one-way decidability result are kept distinct and precisely sourced. |
| 231--401 | **Pass.** Elgot's article/report/errata authority order, acceptor and transducer types, admissible encoding, both directions of Theorem 5.3, truncation step, design predicates, prefix sense of “open,” and finite/infinite behavior distinction are reader-coherent and nonconflated. |
| 403--461 | **Fail, Finding 1.** The corrected finite-union route is mathematically described, including the `n=1` handbook completion, but its left-side semantic notation and arity variables are not defined. |
| 463--476 | **Pass.** The negative decidability boundary is stated with the exact fixed-automaton/existence distinction. |
| 478--485 | **Fail, Finding 5.** Version and ownership prose is correct, but exact comparison claims need exact report/errata locators. |
| 487--603 | **Pass.** The two Trakhtenbrot bodies, official English-title difference, `\mathcal I`, primitive grammar, eliminable conveniences, controlled/lower/upper syntactic classes, semantic dependence, anticipation, finite memory, weight, finite operator, and `A`/Л normalization are explicitly separated. |
| 605--720 | **Pass.** Portion conventions, coordinatewise tuple portions, homogeneity, basis standing, graph residuals, the handbook counterexample to the printed weight bound, and recurrence form are defined and owned. |
| 721--729 | **Fail, Finding 3.** The empty-set correction is appropriately handbook-owned, but the proof object named “covering operator” is not typed or exactly defined. |
| 731--805 | **Pass.** Definability closure, conditional `\mathcal I`-algorithm, graph-versus-solution distinction, continuous versus merely finite-memory results, general-solution clauses, fixed-`p` scope, and conditionality are explicit. |
| 807--886 | **Pass.** Explicit definition, typed finite-word maps, automaton-enumerability/decidability, the nonempty edge repair, special beginning, `\mathcal I'`, and historical-priority boundary are coherent and source-bounded. |
| 888--925 | **Pass.** Thomas's Section 3.1 route is kept at 1996-report strength, gives both effective directions and the empty-word guard, and is not substituted for the three historical finite-word presentations. |
| 927--1085 | **Pass.** Rabin's source authority, `A^*`, `\Lambda`, both orders, successors, predecessor, `SnS`, valued subtrees, paths, transition table, ordinary automaton, run, `\operatorname{In}`, acceptance family, closure dependencies, and formula-track translation are defined with correct standings. The later Meyer lower bound withdraws only the printed complexity claim. |
| 1086--1096 | **Fail, Finding 2.** The worked principal-formula instance is clear except for its proof-operative use of the source-specific finite tree before that object is defined. |
| 1098--1207 | **Pass.** The converse track encoding, exact quantifier prefix, sentence-to-emptiness route, path-language product, deterministic word dependency, dual pair sequence, `\Omega`-type and `\Omega`-empty conditions, and ordinary/dual nonconflation are explicit. |
| 1209--1276 | **Pass.** The empty-sequence normalization is defined, proved equivalent, given a precise standing, distinguished from a new acceptance condition, and used to enter the positive-length induction. Marked obligations and source well-foundedness are defined before their local uses. |
| 1278--1322 | **Pass at this later location, but too late for Finding 2.** Frontier, `frontiered`, its nonredundancy, valuation domain, external frontier value, lift, compactness, and transfinite locus are all adequately explained once reached. |
| 1324--1419 | **Pass.** The one-letter reduction, complement/dual reduction, mutable current state-set scope, restricted table, both half-steps, empty `H` repair, empty `U_0` base, finite obstruction, external weak-theory dependency, and proof status are exact and explicitly owned. |
| 1421--1449 | **Pass.** The application map and the boundary between reconstructed architecture and the fourteen-page source detail are proportionate and candid. |
| 1451--1575 | **Pass.** Thomas's later route is clearly separated from Rabin. Muller and chain automata, order-vector with hit, partial-transition completion, language-preservation proof, game roles, memorylessness, strategy encoding, determinacy, effectiveness, regular generated trees, emptiness, and basis result are defined or described before their operative uses. |
| 1576--1590 | **Fail only at line 1583, Finding 4.** The MSO/automaton construction and decision route are otherwise clear and source-bounded. |
| 1591--1596 | **Pass.** The final paragraph explicitly prevents backward projection onto Rabin and restricts every Thomas locator to the May 1996 report rather than the unreconciled 1997 chapter. |

## Host integration audit

### `logic-in-computer-science.tex` lines 836--850

**Pass.** The displayed finite-word theorem is explicitly labelled a modern formulation. The prose immediately says that the compound name does not assert verbatim occurrence in each historical source and distinguishes Büchi's marker encoding, Elgot's arithmetic/design development, and Trakhtenbrot's broader predicate/operator package. Citing both `Buchi1959WeakReport` and `Buchi1960` does not overclaim access to the journal body because the detailed input states the precursor boundary at lines 8--16.

### Lines 852--876

**Pass.** The separate `S1S` and `S2S` theorem statements do not collapse the Büchi 1962, Rabin 1969, or N-c-014 presentations. The `S2S` host theorem states only decidability and does not retain Rabin's refuted elementary-recursive complexity qualification.

### Lines 878--928

**Pass.** The ranked finite-tree object, bottom-up automaton, finite-domain weak/full coincidence, closure, and emptiness facts are defined independently of Rabin's infinite-tree runs. The final sentence explicitly denies identification with the N-c-014 infinite-tree construction.

### Lines 930--945

**Pass.** Neighboring cross-references remain outside the presentation, and the input order at lines 934--937 inserts `n-c-014` after `n-c-013` and before `n-c-015` without breaking an environment or changing section level. Line 936 points to the audited file.

## Technical-name rule audit

The following newly introduced technical distinctions satisfy the supplied five-part rule in the actual LaTeX:

- Büchi's special predicate, `n/m`-automaton, special output, behavior, string behavior, bit-occurrence relation, and `V_2` presentation;
- Elgot's `I`-automaton, admissible encoding, `T_r(A)`, `A/B`-automaton, source-specific prefix meaning of “open,” and strong `A`-extendibility;
- Trakhtenbrot's `\mathcal I`, fictitious occurrence, upper/lower `t`-formulae, anticipation, finite memory, weight, finite operator, normalized `A`/Л class, portion, homogeneity, residual operator, solution, general solution, automaton-enumerability, automaton-decidability, and special beginning;
- Rabin's two order notations, predecessor, `SnS`, valued tree, transition table, ordinary automaton, dual acceptance, `\Omega`-empty type, zero-length normalization, well-founded obligation assignment, frontiered property, external frontier value, and restricted table; and
- Thomas's chain condition, order-vector with hit, completed automaton, game, memoryless strategy, local instruction, and regular generated tree.

The failures are exactly Findings 1--4: the undefined `T^\infty_d` notation and arities, the too-late source-specific finite-tree definition, the untyped covering operator, and the unnecessary undefined `\Sigma^1_2` label. No additional speculative technical object should be invented to repair them; the existing constructions already provide the needed distinctions.

## Version, rights, ownership, proof-status, and citation audit

### Version and source strength

- **Büchi:** lines 8--16 and 880--882 limit the presentation to UMR1083 precursor strength and leave literal 1960 reconciliation open. No report locator is passed off as a journal locator.
- **Elgot:** lines 231--236 and 478--485 make the journal controlling, the report a precursor, and the published errata controlling for corrections. The only defect is the locator precision in Finding 5.
- **Trakhtenbrot:** lines 487--497 and 586--590 distinguish the 1961 announcement from the 1962 expansion, including their official English title renderings and Л/`A` terminology. No complete English translation or independent priority adjudication is claimed.
- **Rabin:** lines 927--931 and 1442--1449 keep the 1969 definitions and proof architecture controlling and state the reconstruction boundary. The Meyer correction is identified as later evidence only for the complexity claim.
- **Thomas:** lines 888--925 and 1591--1596 use only May 1996 report locators and explicitly withhold 1997 final-chapter strength.

### Rights

The permitted source records warn that public research access does not create an open-content or redistribution licence. The audited LaTeX embeds no source scan, page image, facsimile, or derivative manuscript image; it uses mathematical notation, short source terms, paraphrase, and citation. It makes no claim that any locally held research PDF may be redistributed. No rights defect appears in the audited LaTeX.

### Source versus handbook ownership

Every substantive emendation is owned correctly: Büchi's finite witness and arithmetic correction boundary; Elgot's published erratum versus the handbook's unary-window completion; Trakhtenbrot's residual-map counterexample, empty-set case, and nonempty finite-word repair; Rabin's zero-length normalization and two empty-witness repairs; and Thomas's deadlock completion. Worked examples and editorial symbols are labelled as such. No source correction is silently laundered into an original theorem.

### Proof status and cross-source nonconflation

The prose consistently distinguishes “states,” “proves,” “recovers,” “corrects,” and “handbook-owned.” It does not treat a named theorem as a proof. Rabin's original complementation/emptiness architecture is not replaced by Thomas's later game/basis route, and Thomas's finite-word proof is not projected onto Büchi, Elgot, or Trakhtenbrot. Büchi's weak finite-set language, Trakhtenbrot's arbitrary-set language, Elgot's finite-set arithmetics, and Rabin's full tree logic retain different domains and standings.

### Bibliography and locators

The relevant bibliography entries correctly distinguish the acquired precursors, registered publications, errata, later correction sources, and report/final-chapter identities. Page ranges and identifiers in the permitted records agree with the bibliography entries inspected. Claim-level locators are generally precise throughout the LaTeX. Finding 5 is the sole publication-blocking locator omission found.

## Exact exclusions and bounded conclusion

This verdict does not establish TeX compilation, reference resolution, page layout, typography, overfull-box absence, visual quality, image rights, or a final publication build; none of those checks was authorized. It does not certify the unreconciled Büchi 1960 journal body or Thomas 1997 chapter. It does not admit Part IX, the full handbook, any source asset for redistribution, or any claim outside the audited line ranges.

Once Findings 1--5 are repaired in the actual LaTeX, a fresh direct-source publication/terminology read is required. The source-register status remains independently open for the Büchi 1960 and Thomas 1997 reconciliations even if the manuscript defects are corrected.

REGISTER STATUS: OPEN
