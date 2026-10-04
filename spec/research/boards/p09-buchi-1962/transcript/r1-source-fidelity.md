# R1 source-fidelity and evidence report — Büchi 1962, N-c-013.a

## Blindness and permitted evidence

I read `spec/research/boards/p09-buchi-1962/charter.md` completely before substantive review. I did not read `ledger.md`, `transcript/chair.md`, another current transcript, or any earlier board transcript, and I did not contact another reviewer. I edited only this owned transcript.

I did not run a test, test harness, automated checker, repository script, TeX command, handbook build, or handbook-PDF inspection. Evidence used here is direct reading of the frozen manuscript/source-record lines, visual reading of the charter-named source page images at original detail, citation/provenance inspection, mathematical/source reasoning, and SHA-256 identity computation.

## Frozen identity check

All six frozen hashes were recomputed before substantive review and matched the charter exactly.

| Artifact | Recomputed SHA-256 | Status |
|---|---:|---|
| `tmp/pdfs/p09-buchi-1962/logic-methodology-philosophy-science-pageplace-preview-includes-buchi-pp1-11.pdf` | `D37929230CD874D9B6E91CDDE50DD57EAF51D625BC7575878853E4018B64E089` | checked-clean |
| `handbook/parts/p09/presentations/n-c-013.tex` | `F674BDB103A3B07DEE5925A1D7F3880D92DA31C6442196FB075B2FA85F4ADD24` | checked-clean |
| `handbook/parts/p09/logic-in-computer-science.tex` | `2778CAA3D0EB741A78B9D2EA44BD157E5FCCB4E2F3034ED539D52A9788287A1B` | checked-clean |
| `handbook/bib/handbook.bib` | `748B159ED5CE40855878D3E8492DA98D0A465B73C68830E5BE11165EFF2ACA6A` | checked-clean |
| `spec/research/p09-buchi-1962-source-acquisition.md` | `90C23E094604342726B02EC78FE1A4211D56233A063532E8EDA94537676C434B` | checked-clean |
| `spec/research/p09-source-presentations-lot2-3.md` | `EBC0E39AF016B22F1BA52D7DEEB620DE6B00F5B48AA1F3E0687BB10BBC316508` | checked-clean |

## Direct manuscript and record lines read

- `handbook/parts/p09/presentations/n-c-013.tex:375-760`, the complete Büchi reader section in scope.
- `handbook/parts/p09/logic-in-computer-science.tex:817-828`, the shared Büchi theorem in scope.
- `handbook/bib/handbook.bib:2276-2288`, the Büchi bibliography record in scope.
- `spec/research/p09-buchi-1962-source-acquisition.md:1-541`, the complete source acquisition and reconstruction note.
- `spec/research/p09-source-presentations-lot2-3.md:556-569`, the compact N-c-013.a presentation, plus the consolidated ledger region showing N-c-013.a absent from the remaining open-acquisition list and present in the sufficient-body list.
- For the single-initial-state boundary expressly invoked at `n-c-013.tex:492-494`, I also read only the referenced automaton definition location enough to confirm that the handbook comparison target uses one initial state. I did not use that external definition as source evidence for any Büchi source claim.

## Visual source inspection

I visually inspected the complete charter-named source images at original detail:

| Image | Printed source content checked | Source-fidelity result |
|---|---|---|
| `frontmatter-page-04.png` | title page: *Logic, Methodology and Philosophy of Science*, proceedings of the 1960 International Congress, editors Ernest Nagel, Patrick Suppes, Alfred Tarski, Stanford University Press, Stanford, California | supports bibliographic identity |
| `frontmatter-page-05.png` | copyright page: Stanford University Press, Stanford, California; copyright 1962; first published 1962; printing line `78 77` | supports original-year and later-printing boundary |
| `contents-page-8.png` | contents p. vii: `I. MATHEMATICAL LOGIC`, `Symposium on Decision Problems`; Büchi title and author; first page 1; Julia Robinson first page 12 | supports title, author, section-heading boundary, and page endpoint |
| `buchi-1962-page-12.png` | printed p. 1: title, J. Richard Büchi, University of Michigan, SC domains/vocabulary, binary-expansion comparison, purpose, support note | supports SC identity, Nn natural-number wording, and no DOI on article opening |
| `buchi-1962-page-13.png` | printed p. 2: finite-rank congruence, multi-periodic sets, circuit motivation, Sequential Lemma motivation, formula hierarchy, bounded and infinitely-often quantifiers, `Σ_1^ω`, `Π_1^ω`, `Σ^0`, `Π^0` | supports formula-class and notation claims |
| `buchi-1962-page-14.png` | printed p. 3: state-word encoding, two-sided congruence, rank, multiperiodicity, formula/denotation overload, Lemma 1 statement and Ramsey proof, start of Lemma 2 | supports encoding, finite-word bridge, and Sequential Lemma |
| `buchi-1962-page-15.png` | printed p. 4: Lemma 2 proof provenance, behavior of `[I,J,U]`, Lemmas 3-6, Rabin-Scott proof reference | supports finite-automata proof-boundary claims |
| `buchi-1962-page-16.png` | printed p. 5: Lemmas 7-9, union/intersection devices, complement congruence definitions, `2m^2` binary distinctions | supports Boolean closure and non-determinization boundary |
| `buchi-1962-page-17.png` | printed p. 6: rank `≤ 2^{2m^2}`, homogeneous-block construction, `F_{c,d}`, complement union, effectivity ingredients for Lemma 9 | supports complement argument and rank bound |
| `buchi-1962-page-18.png` | printed p. 7: Lemma 10, Lemma 11, Theorem 1, `Σ_1^ω`/`Σ_2` collapse, free-individual extension, `SC_fin`, algorithmic-strength remark, start of decision section | supports normal-form and definability claims |
| `buchi-1962-page-19.png` | printed p. 8: Lemma 12 statement and finite stem-cycle proof, finite bound by `2^k`, effectivity of Lemmas 2, 6, and critical Lemma 9 steps | supports decision-method proof strength |
| `buchi-1962-page-20.png` | printed p. 9: Theorem 2; five consequences/comparisons; proposed axiom schema; `SC_per`; finite-semigroup outline; Theorem 3 statement | supports consequence, axiom-schema, and SC_per claims |
| `buchi-1962-page-21.png` | printed p. 10: Theorem 4, `Re/Ra/Nn/Pw` glossary, `2x` undecidability report, Gödel-attributed monadic-function report, Problems 1-3, references [1]-[6] | supports arithmetic, discrepancy, attribution, and open-problem claims |
| `buchi-1962-page-22.png` | printed p. 11: references [7]-[11], article endpoint | supports endpoint and cited-source boundary |
| `boundary-page-23.png` | next article opening: Julia Robinson, printed p. 12 | confirms Büchi endpoint at printed p. 11 and file-page boundary |

## Findings

### F-SF-01 — Source note modernizes a printed word without flagging it

- Severity: consider.
- Source page: Büchi printed p. 1.
- Manuscript/source-record line: `spec/research/p09-buchi-1962-source-acquisition.md:93`.
- Invariant: I2 and I4; rendered source pages control printed wording, and source wording should remain visibly distinct from reconstruction.
- Evidence: printed p. 1 says that SC is a "fraction" of the restricted second-order theory of natural numbers. The source note says the paper calls SC a "fragment" of restricted second-order arithmetic.
- Harm: small wording drift. The mathematical standing is unaffected, but a reader could treat "fragment" as exact source wording rather than a harmless modern paraphrase of Büchi's printed "fraction."
- Minimum repair: either replace "fragment" by "fraction" in the source note, or write that Büchi describes SC as a part/fraction of the restricted second-order theory, if modernization is intended.
- Blocking status: not a blocker and not a must-fix for N-c-013.a admission; the reader-facing manuscript in `n-c-013.tex:391-400` does not rely on the word "fragment."

No blocker or must-fix finding remains within the source-fidelity mandate.

## Source-fidelity determinations

The reader keeps the source layers distinct. It presents SC as Büchi's interpreted formalism, not as an automaton or language class; presents the truth-value-word and automata comparison as a handbook-owned translation; preserves source proof/provenance boundaries for Myhill/Büchi 1960, Rabin-Scott, Lemma 11, and Theorem 3; preserves the p. 1/p. 10 `Nn` discrepancy; and does not import a modern complexity bound, determinization theorem, circuit example, or solved synthesis theorem.

The finite-data comparison is mathematically source-faithful at the stated strength. For a displayed `Σ_1^ω` formula, set `Γ={0,1}^k`, `Q={0,1}^ℓ`, `Q_0={q:A[q]}`, `Δ(q,a)={q':B[a,q,q']}`, and `F={q:C[q]}`. If the source formula is satisfied, the existential predicate tuple gives a sequence `q_0q_1...` with `q_0∈Q_0`, `q_{n+1}∈Δ(q_n,i(n))`, and infinitely many visits to `F`. Conversely, any such state sequence defines the auxiliary predicates by their bit coordinates and satisfies the source formula. This proves the stated start-set variant exactly. The source itself does not print the tuple, use later run terminology, or name "Büchi acceptance."

The converse modern comparison in the shared theorem is also source-faithful as handbook-owned content: a nondeterministic Büchi automaton's finite states can be encoded by finitely many predicate bits; propositional matrices enforce permitted initial codes, transitions, recurrent codes, and exclusion of unused bit patterns; the resulting `Σ_1^ω` formula defines exactly the accepted truth-value words. This is not attributed as Büchi's printed tuple theorem.

The AGENTS terminology rule is satisfied at source-fidelity strength. New or potentially technical names are either source names with source standing (`SC`, `Σ_n`, `Π_n`, `Σ_1^ω`, `Σ^0`, multiperiodic, `SC_fin`, `SC_per`, `SC^2`, `SC(α)`) or eliminable handbook comparisons (`Γ,Q,Q_0,Δ,F`, recurrence set/finite-data comparison). Where the reader introduces `SC_per`, it gives necessity, an eliminable definition of ultimately periodic assignments, standing as a restricted interpreted formalism, nonredundancy against full `SC`, and immediate later use in Theorem 3. I found no hypothetical technical name introduced before necessity, definition/axiom, standing, nonredundancy, and use.

## Mandatory coverage ledger

| Point | Status | Determination |
|---|---|---|
| M01 | checked-clean | All six frozen SHA-256 identities recomputed and matched before substantive review. |
| M02 | checked-clean | Charter-named frontmatter, contents, printed pp. 1-11, and boundary p. 12 images were visually inspected at original detail; page map p. 12-22 = Büchi printed pp. 1-11 and file p. 23 = Julia Robinson printed p. 12 is confirmed. |
| M03 | checked-clean | Author, title, editors, proceedings title, publisher, location, year, pp. 1-11, later Stanford printing status, later DOI separation, access route, and rights boundary are supported by the visual frontmatter/article pages and source-record provenance. |
| M04 | finding-linked | SC domains, vocabulary, quantifiers, and standing are checked-clean from printed p. 1 and manuscript lines 391-400; F-SF-01 records only a nonblocking source-note wording modernization. |
| M05 | checked-clean | Printed p. 3 supports the assignment-to-infinite-truth-value-word encoding, and the manuscript correctly avoids inserting a distinct source run at that stage. |
| M06 | checked-clean | Printed p. 2 supports the literal `Σ_1`, `Π_1`, `Σ_{n+1}`, `Π_{n+1}` clauses, the infinitely-often definition, and `Σ_1^ω`; manuscript lines 421-467 preserve formula-class standing. |
| M07 | checked-clean | The handbook-owned `Γ,Q,Q_0,Δ,F` translation is extensionally exact in both directions; `Q_0` is a permitted initial set, while the referenced modern comparison target uses one initial state. |
| M08 | checked-clean | Printed pp. 2-3 support `Σ^0`, finite-interval dependence on `i(x)...i(y-1)`, and the source-declared formula/denotation overload. |
| M09 | checked-clean | Printed p. 3 supports two-sided congruence, finite rank, multiperiodicity, and the distinction from ultimately periodic predicate sets. |
| M10 | checked-clean | Printed p. 3 supports Lemma 1's exact `p<q` block quantification and printed Ramsey coloring proof. |
| M11 | checked-clean | Printed pp. 3-4 support Lemmas 2-6, endpoint output behavior, Boolean/quantifier reductions, and the Myhill/Büchi 1960 and Rabin-Scott proof dependencies. |
| M12 | checked-clean | Printed pp. 5-6 support Lemmas 7-9, conjunction control, complement congruence, `2^{2m^2}` rank bound, homogeneous-block argument, and absence of an imported determinization construction. |
| M13 | checked-clean | Printed pp. 6-7 support Lemma 10's finite-union stem/repeated-block form. The source display does not separately spell "nonempty," but the strict cut-point construction supplying the repeated blocks makes the repeated source blocks nonempty in the derived factorization. |
| M14 | checked-clean | Printed p. 7 supports Lemma 11, Theorem 1, the `Σ_1^ω`/`Σ_2` collapse, free-individual extension, and finite-set consequence at the source's exact proof strength. |
| M15 | checked-clean | The SC-definable truth-value-word/nondeterministic Büchi-recognizable equivalence is proved in the manuscript as an explicit handbook-owned corollary; the source does not use the modern tuple or theorem name. |
| M16 | checked-clean | Printed p. 8 supports Lemma 12's initial path, recurrent state, nonempty return cycle, `2^k` finite bound, converse periodic construction, and finite enumeration. |
| M17 | checked-clean | Printed pp. 8-9 support the remaining effectivity argument and Theorem 2 as decidability only, with no modern complexity claim. |
| M18 | checked-clean | Printed p. 9 supports all five post-Theorem-2 consequences/comparisons, including `SC_fin`, `[Nn,+,Pw]`, and the disclosed standing problem around the printed `Σ_2^0` notation. |
| M19 | checked-clean | Printed p. 9 supports the proposed axiom-schema claim and the absence of a printed completeness proof. |
| M20 | checked-clean | Printed p. 9 supports `SC_per`, Theorem 3, and the finite-semigroup outline; the manuscript's explicit ultimately-periodic definition is eliminable and properly marked as reconstruction. |
| M21 | checked-clean | Printed pp. 1 and 10 support Theorem 4, the binary-expansion route, symbol glosses, and the `Nn` discrepancy. |
| M22 | checked-clean | Printed p. 10 supports the `2x` undecidability report, Gödel-attributed monadic-function report, and proof/attribution limits. |
| M23 | checked-clean | Printed p. 10 supports all three open problems, definitions of `SC^2` and `SC(α)`, and the verification-versus-synthesis distinction. |
| M24 | checked-clean | The reader, shared theorem, bibliography, complete source note, compact record, open-acquisition list, and sufficient-body ledger reconcile: N-c-013.a is source-acquired and body-sufficient, while admission remains board-controlled. |
| M25 | checked-clean | The AGENTS terminology rule, rights boundary, topic-only scope, and no-test/no-build boundary are observed in the manuscript and in this review. |

VERDICT: ACCEPT
