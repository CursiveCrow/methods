# Round 3 — adversarial-publication

## Original-finding dispositions

- F1 — accept-fixed. The six caption-level `A-...` strings are removed, and the current reader graph contains no OPEN/unadmitted/internal register/workflow token.
- F2 — external. Provenance/admission, build, visual, human, administrative, and user gates remain deliberately outside this source/content ruling.
- F3 — accept-fixed. All five editorial body/annex seams retain visible authorship, sources, proof standing, and nonreplacement notes.
- F4 — accept-fixed. `thm:p05-sigma-one-completeness` is `proved=annex:p5.sigma.1`; `handbook/annex/p05/depth-completion-supplement.tex:18-157` supplies the normal-form conversion, bounded-formula induction, primitive-recursive proof constructors, substitution invariant, PA verification, formalized implication, and external Q proof.
- F5 — accept-fixed. Paris--Harrington now has the indicator/nonstandard-cut architecture and the precise full-induction \(\mathsf{ACA}\) versus \(\mathsf{ACA}_0\) upper calibration.
- F6 — accept-fixed for registered coverage. Goodstein has a fixed base schedule and local \(\varepsilon_0\)/Cantor-normal-form dependency; the exact Kirby--Paris hydra/regrowth relation, termination, and PA-unprovability statements are present.
- F7 — accept-fixed. Rosser provability, strict/non-strict witness comparison, its distinction from ordinary provability, and the Guaspari--Solovay \(R\) pointer are defined, sourced, registered, and generated.
- F8 — accept-fixed. The GL chapter links `sheet:hilbert-gl`, states theorem-only necessitation, defines the oriented Kripke semantics, fixes the PA realization/Solovay hypotheses, uses a labeled proof boundary, and supplies the modal/arithmetic dictionary.
- F9/F10 — accept-fixed. The Q/PA, decidable-arithmetic, provability dictionary, independence, and reverse-mathematics tables are captioned, labeled, complete for their registered columns, and free of internal apparatus IDs; the Big Five figure is present with exact non-cover/non-exhaustiveness qualifications.
- F11 — accept-fixed for source content. Part V has grouped Further Reading, and `handbook/parts/p05.tex:42-51` now routes `generated/audit-p05` from a reachability-based generator. The register's own missing table identity is the new blocker below.
- F12 — accept-fixed. Exact \(\mathsf{Prov}_T\), Rosser provability, fixed and presentation-indexed consistency, and the \(\mathcal N/\mathcal N_{\mathrm{ar}}\) source convention agree across the CSV, generated symbol table, generated symbol index, and manuscript.
- F13 — accept-fixed. Source-safe hooks and generated named-index rows expose Arithmetization of syntax and Undecidability of theoremhood without editing inherited bytes.
- F14/F15 — accept-fixed. Solovay, Tennenbaum, Goodstein descent, and hydra rank/unprovability are now labeled `proofboundary`/`hbmethod` entries; the cited theorem statuses no longer masquerade as local QED proofs.

## Integrated publication verification

- Reader route: 47 reachable files through 45 noncomment input edges, with no missing or duplicate target.
- Navigation: 103 explicit/typed labels, no duplicate. All 48 references resolve when the registered specialized calculus label `sheet:hilbert-gl` is included.
- Sources: all 81 parsed citation keys exist.
- Proof status: the sole Part V `proved=` body result has exactly one reciprocal annex item; exact inline/source statuses remain separately classified.
- Reader debt: zero noncomment OPEN/unadmitted/D-/N-/A-/R-/workflow/finalizer hits.
- Lookup generation: `tools/audit_tables.py:52-74` traverses the live part input graph rather than scanning retained historical files; lines 77-105 and 159-230 recover exact source metadata/status and editorial status forms; lines 345-370 define deterministic freshness comparison. `handbook/generated/audit-p05.tex` consequently lists 83 live theorem/definition-class rows with inherited and editorial statuses kept distinct. The generator deliberately excludes unadmitted system-card metadata rather than publishing parsed draft fields.
- New tables and figure: the Q/PA, decidable-arithmetic, provability dictionary, independence, reverse-calibration, and theorem-definition register are routed once; the reverse-mathematics Big Five figure and Part V Further Reading are present. Build/visual behavior remains external.

## Blocking objection — F16 [must-fix] The generated register has no table identity

- location: `spec/registers/apparatus.csv:114, :185`; `handbook/parts/p05.tex:42-51`; `handbook/generated/audit-p05.tex:1-95`; `tools/audit_tables.py:108-124, :303-322`
- exact defect: The generated register is a `longtable`, but neither the generated file nor `longtable()`/`render_part()` emits a `\caption` or table `\label`. The body supplies only the surrounding section label `sec:p05-theorem-definition-register`. Thus the routed surface is readable, but the table itself has no numbered identity, cannot be referenced as a table, and cannot appear in the list of tables. A-113 classifies the per-part audit register as a table, while A-184 requires the list of tables to cover every register/comparison table.
- concrete failure path: A reader, apparatus checker, or list-of-tables consumer can reach the section but cannot retrieve a table number or `tab:` destination. This repeats the anonymous-table failure repaired for A-054/A-056 and leaves A-113 publication-incomplete despite correct row harvesting.
- exact correction: Extend the generator so each per-part audit `longtable` emits a reader title and stable label—for Part V, for example, `\caption{Theorem and definition register for Part V}` followed by `\label{tab:p05-theorem-definition-register}\\` before the first header. Regenerate the audit files, retain the existing section destination, and verify the generated source contains exactly one caption/label per part. Actual numbering, list-of-tables entry, pagination, and continuation layout remain later build/visual checks.

## Boundary

F2 and all administrative/build/reference-index/visual/human/user gates remain external. I inspected frozen source, registry, generator, and generated TeX text only; ran no generator, checker, test, TeX build, or PDF build; inspected no rendered layout; edited no manuscript/control/test/generated file; and read no other Part V seat transcript.

reject
