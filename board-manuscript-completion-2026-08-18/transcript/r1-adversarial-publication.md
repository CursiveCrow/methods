### F1 [blocker] [open] The named-theorem index is a selected list, not the required index
- author: adversarial-publication r1
- location: handbook/parts/p14/master-tables.tex:212-243; spec/registers/apparatus.csv:160; handbook/parts/p05/provability-logic-gl.tex:36-64; handbook/parts/p09/logic-in-computer-science.tex:51-111; handbook/parts/p10/algebraic-and-categorical-logic.tex:32-59
- criterion: C3, "the requested register topics represented by each former stub are substantively present, not merely renamed"; invariant I6, "No reader-facing stub, unsupported addition, collapsed variant, undefined reference, or uncited external claim may remain."
- claim: The apparatus calls an eighteen-row selection the named-theorem index even though the controlling register requires all named theorems and lemmas and both statement and annex-proof destinations. This leaves readers unable to retrieve most of the newly added results through the book's declared theorem-index surface.
- evidence: The table at lines 224-241 contains eighteen rows and has only Result, Label, and Page columns. A read-only extraction of the eighteen `hbtheorem` labels in the four audited Part V files plus Parts IX-X found only three in that table (`thm:p09-fagin`, `thm:p10-stone-representation`, and `thm:p10-yoneda`); fifteen are absent, including all eight Part V theorem labels. The controlling row at `spec/registers/apparatus.csv:160` says "Index of all named theorems and lemmas" and requires pointers to statement and annex proof.
- correction: Generate the table from every live named theorem and lemma, add separate statement-page and annex-proof destination fields (using an explicit no-annex marker when applicable), and do not close A-159 until a completeness check compares the generated index against all live theorem/lemma labels.

### F2 [must-fix] [open] The symbol-index destination and contents do not match the registered obligation
- author: adversarial-publication r1
- location: handbook/parts/p14/master-tables.tex:245-255; handbook/parts/p01/symbol-registry.tex:2-4; handbook/parts/p01/symbol-registry.tex:22-32; handbook/generated/symbols-tables.tex:6-17; spec/registers/apparatus.csv:158
- criterion: C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"
- claim: The apparatus sends the reader to the Rule Sheets chapter for the symbol registry, although the registry is in Part I, and the generated table does not contain the page-of-registration and principal-use destinations required of the symbol index.
- evidence: `master-tables.tex:248-250` points to `sec:p14-rule-sheets`; the actual symbol-registry chapter label is `sec:p01-symbol-registry` at `symbol-registry.tex:2-4`. The generated table's columns are Glyph, Macro, Role, Scope, Prec, First, and Notes (`symbols-tables.tex:6-17`), whereas A-157 at `spec/registers/apparatus.csv:158` requires every registered symbol with its page of registration and principal uses.
- correction: Point the apparatus to `sec:p01-symbol-registry`, and generate page-linked registration and principal-use destinations for every registry row before describing this surface as the symbol index.

### F3 [should-fix] [open] The claimed alphabetized capsule person index is not alphabetized
- author: adversarial-publication r1
- location: handbook/parts/p14/master-tables.tex:245-255; handbook/parts/p13/chronology-and-biography.tex:91-118; spec/registers/apparatus.csv:159
- criterion: C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"
- claim: The apparatus says the person index is an "alphabetized capsule sequence," but the capsule sequence begins Aristotle, Chrysippus, Leibniz, Boole, De Morgan, Frege and is neither surname- nor given-name-alphabetical.
- evidence: The claim is at `master-tables.tex:250-252`; the contrary sequence is visible at `chronology-and-biography.tex:94-118`. A-158 requires an accented-name-aware sorted person index linked to capsules, not merely a topical/chronological capsule section.
- correction: Either alphabetize the capsule sequence with stable accent-aware sort keys, or state that the alphabetized person-name entries live in the unified index and verify that each links back to its capsule; remove the false description in either case.

### F4 [must-fix] [open] MV-algebra is named without an exact definition
- author: adversarial-publication r1
- location: handbook/parts/p10/algebraic-and-categorical-logic.tex:203-216
- criterion: C5, "the prose is graduate-reference quality, definition-before-use, and does not hide an open obligation behind a new name"; invariant I4 requires colocated necessity, exact definition or axiom, standing, nonredundancy, and later use.
- claim: The purported definition of an MV-algebra delegates its defining content to "the standard Chang equations" without displaying or otherwise fixing those equations, then immediately uses the class in a completeness claim.
- evidence: Lines 203-211 specify the signature and one standard example but never state the equational basis. A repository-wide read-only search found no other occurrence supplying the Chang equations; the next use is Chang completeness at lines 215-216.
- correction: State a complete equational basis (including the carrier convention) in the definition and identify the displayed standard algebra as an example, or remove the named definition and record the exact definition as an owed artifact until it is supplied.

### F5 [must-fix] [open] Four truth-theory abbreviations are not fixed as formal theories
- author: adversarial-publication r1
- location: handbook/parts/p11/philosophy-of-logic.tex:62-78
- criterion: C5, "the prose is graduate-reference quality, definition-before-use, and does not hide an open obligation behind a new name"; invariant I4 requires an exact definition or explicit axiom and clear standing.
- claim: `TB`, `CT`, `KF`, and `FS` are introduced as formal theories using only one-line descriptions, with no fixed base theory, language, axiom/rule schemes, or induction package; their identity and proof-theoretic strength therefore remain variant-dependent.
- evidence: Lines 63-70 say only "over an arithmetical base theory" and themselves warn that the packages have different strength and must be used with a declared base, but no base or package is declared. These are the only occurrences of the four abbreviations in the handbook.
- correction: For each abbreviation, fix the base, expanded language, exact truth axioms or inference rules, and induction scheme at this location, or replace the abbreviations by an explicit owed-artifact statement and retain only the nontechnical survey comparison.

### F6 [must-fix] [open] The biographical apparatus contains forty uncited external claim clusters
- author: adversarial-publication r1
- location: handbook/parts/p13/chronology-and-biography.tex:4-8; handbook/parts/p13/chronology-and-biography.tex:91-286
- criterion: C1, "claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary"; invariant I6 forbids an uncited external claim.
- claim: The chapter says the capsules are keyed to works cited elsewhere, but none of the forty biographical capsules supplies a citation or an exact cross-reference to authority for its dates, attributions, or interpretive distinctions.
- evidence: A read-only scan of lines 91-286 counted forty `\paragraph` capsules and zero `\cite` commands. Examples include the uncited historical claims about Aristotle and Chrysippus at lines 94-102, Leibniz at 104-107, and De Morgan at 114-116. A general statement that works are cited elsewhere does not let a reader identify which source supports which capsule.
- correction: Add one or more authoritative citations to every capsule's factual claim cluster, or add exact cross-references to a cited passage that supports that cluster; keep interpretive cautions separately attributable where the cited historical evidence does not entail them.

### F7 [must-fix] [open] New calculus sheets leave inheritance dependencies unresolved in reader text
- author: adversarial-publication r1
- location: handbook/registry/calculi/affine-ill.tex:2-4; handbook/registry/calculi/omega-arithmetic.tex:1-5; handbook/handbook.sty:1651-1658
- criterion: C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"; invariant I6 forbids undefined references and collapsed variants.
- claim: The affine sheet exposes the internal token `sheet:imll` as plain reader text rather than a destination, while the omega-rule sheet refers only to "the selected finitary arithmetic sequent rules" and "the underlying arithmetic sheet" without naming any calculus at all. A reader therefore cannot recover either inherited rule base reliably.
- evidence: `affine-ill.tex:2-3` prints `sheet:imll` four times with no `\ref` or `\hyperref`; `\calculussheet` typesets its third argument directly at `handbook.sty:1657`. `omega-arithmetic.tex:4` supplies no label, name, or link for its underlying finitary/equality rules.
- correction: Replace every raw dependency token by a human-readable, linked sheet reference, and bind the omega calculus to one exact named base sheet (or reproduce its base rules and side conditions locally); do not state a completeness or ordinal claim until that identity is fixed.

### F8 [must-fix] [open] Ordered superposition hides a rule obligation behind "standard" side conditions
- author: adversarial-publication r1
- location: handbook/registry/calculi/ordered-superposition.tex:1-6; handbook/parts/p12/first-order-automation.tex:224-246
- criterion: C4, "notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook"; C5 requires definition-before-use rather than a hidden obligation.
- claim: The Equality Factoring rule omits part of its formal rule by saying only "the standard ordering side conditions hold," although the body theorem makes ordering and eligibility hypotheses essential to refutational completeness.
- evidence: The omitted conditions occur in the rule's side-condition field at `ordered-superposition.tex:6`; the body says the calculus differs through explicit ordering/selection constraints (`first-order-automation.tex:224-235`) and that deleting a listed hypothesis changes the theorem (`:239-245`). Thus "standard" is neither exact nor eliminable and can collapse inequivalent superposition variants.
- correction: Display every ordering, maximality, selection, and eligibility condition for Equality Factoring in the sheet, and cross-check the resulting exact rule set against the cited presentation used by the completeness theorem.

### F9 [blocker] [open] The inherited bibliography conversion has no completed semantic field review
- author: adversarial-publication r1
- location: spec/provenance/inherited-bibliography-field-ledger.csv:1-65; spec/provenance/SRC-16803-17196.json:37-71
- criterion: C1, "claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary"; invariant I2 requires inherited artifacts to remain byte-faithful and editorial changes to remain separately identified.
- claim: All sixty-four inherited bibliography conversions pass only the mechanical field check; every row's semantic-field-review state remains `pending`, while the provenance record still marks the reconstructed destination open/missing and independent-source, build, visual, and human checks pending. The bibliography conversion therefore cannot yet support a publication-safe fidelity claim.
- evidence: Rows 2-65 of the ledger end `pass,pending`. `SRC-16803-17196.json:37` records `open/missing`, and lines 52-71 keep all completeness dimensions plus independent source, build, visual, and human review pending. The command `python tools/check.py --tree handbook --strict` passed and reported 512 bibliography entries, but that static result does not perform or supersede the ledger's semantic review.
- correction: Perform and record a row-by-row semantic comparison of every converted field against the inherited `\bibitem`, resolve discrepancies without overwriting the retained authority artifact, and keep the destination unadmitted until the independent-source and later build/visual/human gates are separately completed.

### F10 [must-fix] [open] S1S and S2S appear as undefined one-use technical names
- author: adversarial-publication r1
- location: handbook/parts/p09/logic-in-computer-science.tex:213-222
- criterion: C5, "the prose is graduate-reference quality, definition-before-use, and does not hide an open obligation behind a new name"; invariant I4 requires necessity, exact definition, standing, nonredundancy, and later use for a new technical name.
- claim: The acronyms S1S and S2S are introduced without expansion, structures, syntax, semantics, or a later use, so a first-time reader cannot tell what theories the two decidability claims concern.
- evidence: They occur only at lines 219 and 221; a repository-wide read-only search found no other occurrence defining either acronym.
- correction: Define the exact monadic second-order structures/languages before stating their decidability, with citations for the two results, or delete the unused acronyms and state the bounded automata correspondence descriptively.

## Coverage note

- Lot 1 (Part V): finding-linked (F1). All four named files were read line by line; their public route through `handbook/parts/p05.tex` and their labels, references, citations, longtable source, and reader-facing proof statuses were checked. No additional adversarial-publication finding was established.
- Lot 2 (Parts IX--XI and annexes): finding-linked (F1, F4, F5, F10). All three body files and all three annex files were read line by line; annex/body proof-location claims and public routes were checked. No fresh rendered-page inspection was performed.
- Lot 3 (Parts XIII--XIV): finding-linked (F1, F2, F3, F6). All three named files were read line by line; table/index claims and public routes were checked. Longtable/tabular source was inspected statically, not visually in a fresh build.
- Lot 4 (closed former stubs and new sheets): finding-linked (F7, F8), partially checked. Public-driver routing, reader-facing stub search, all changed/new calculus sheets, and the strict static gate were checked. The very large changed chapter corpus under Parts II, III, VI, VII, VIII, and XII was not reread line by line in this opening-round timebox; mathematical completeness and source fidelity in those unreviewed passages are not approved here.
- Lot 5 (backmatter/source accounting): finding-linked (F9), partially checked. The sixty-four-row bibliography ledger, the named terminal/preamble/control records' status boundaries, bibliography-key/static coverage, and pending-vs-passed category separation were checked. The 512-entry bibliography was not independently compared to external primary sources, and the restoration bytes were not manually reverified beyond the recorded/static checks.
- Reproducible static check: `python tools/check.py --tree handbook --strict` passed with 569 symbol rows, 512 bibliography entries, zero pending inherited references, no reported routed stubs, and all hard checks passed. This is static evidence only; no final compilation, fresh PDF render, page-by-page visual review, mathematical approval, human review, or user acceptance is claimed.
