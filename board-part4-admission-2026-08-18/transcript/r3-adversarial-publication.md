# Round 3 — adversarial-publication

### F5 — accept-fixed
- current evidence: `handbook/parts/p04/degrees-and-priority-continuation.tex:84-110`; `handbook/annex/p04/degrees-and-priority-continuation.tex:39-96`
- response: The Kleene--Post construction now uses the fixed oracle-program numbering and typed requirements
  \[
    R_e:\chi_A\not\simeq\varphi_e^B,
    \qquad
    S_e:\chi_B\not\simeq\varphi_e^A.
  \]
  The annex explicitly identifies the enumerated candidate with the target characteristic function, defines finite-oracle convergence, and retains the complete diagonalization, totality, \(\varnothing'\)-reducibility, incomparability, and strict-degree verification. The former set-versus-partial-function mismatch is closed without weakening the proof.

### F7 — accept-fixed
- current evidence: `handbook/registry/symbols.csv:49, :229, :232, :237, :247, :252, :283, :307-309`; `handbook/generated/symbols-tables.tex:239, :260, :263, :268, :278, :283, :314, :338-340`; `handbook/generated/symbol-index.tex:80, :107, :282, :286, :351, :360, :366, :411, :506, :524`; `handbook/parts/p04/frontiers-of-computability.tex:314-335`; `handbook/parts/p04/complexity.tex:188-224`
- response: The current CSV and both regenerated reader surfaces agree. They retain exact source \(U(e,x)\), \(\chi_A\), and \(\equiv_m\); scope Kleene equality through P4.5; describe \(\mathsf{Comp}\) as the bounded formula supplied by the inherited theorem without invented canonicality; and contain no \(\mathsf{Acc}\) row. The new \(\mathsf{Run}_{U_K}\) entry states its fixed-machine/string standing and primitive-recursive relationship to \(\mathsf{Comp}\). The fixed-width \(\operatorname{bin}_m\) address is defined before succinct use and registered, and CVP/SCVP/STQBF plus the universal analytical relations appear consistently in the CSV, generated table, and generated index. No stale Part IV symbol row remains on this seam.

### F14 — accept-fixed
- current evidence: `handbook/parts/p03/finite-model-theory.tex:96-100`; `handbook/parts/p04/complexity.tex:465-469`; `handbook/parts/p09/logic-in-computer-science.tex:83-84`; `handbook/generated/named-theorem-index.tex:128, :341`
- response: Part III now links the exact inherited `thm:trakhtenbrot` statement instead of declaring `thm:p03-trakhtenbrot`, and the generated theorem index has one Trakhtenbrot row. Part IV and Part IX continue to link the single `thm:p03-fagin` statement, and the index has one Fagin row. The two duplicate public identities are closed without editing the exact source theorem.

### F15 — still-open-source
- repaired portion: `handbook/parts/p04/degrees-and-priority-continuation.tex:1-9`; `handbook/parts/p04/decision-hierarchy-apparatus-supplement.tex:1-8`
- response: The two headers named in round 2 now accurately identify an independently revised degree continuation and separately authored hierarchy apparatus rather than claiming derivative standing.
- residual defect: The later frontier repair made two other headers stale. `handbook/parts/p04/frontiers-of-computability.tex:2` says the file contains cited results and “one proved computable-structure corollary,” but `thm:p04-omega-halting` at line 357 is now also `proved=annex:p4.frontiers.2`. Correspondingly, `handbook/annex/p04/frontiers.tex:1` calls the file only the proof for the computable-structure corollary, while lines 25--58 contain the complete \(\Omega\) proof. These are nonprinting source comments, not reader-status defects, but they misstate the authorship/proof inventory of the frozen files.
- exact correction: Replace the two singular headers by accurate plural descriptions covering the separately authored computable-structure and algorithmic-information results/proofs. No reader prose, theorem status, or admission field needs to change.

## Integrated focused check

- route placement: accept-source-stable. `handbook/parts/p04.tex:33-41, :73-78` keeps the machine supplement immediately after its exact chapter, the universal bridge after its exact chapter, and the hierarchy/degree/frontier/complexity sequence in the intended order. The two roots reach 45 files through 43 noncomment input edges with no missing or duplicate target.
- reader standing: accept-source-stable. Every editorial body/annex seam retains its visible reader note, and a noncomment scan finds zero `OPEN:`/unadmitted/internal-ID/finalizer/workflow tokens. The driver-only audit-generator comment remains nonprinting and accurate.
- apparatus: accept-source-stable. The machine-equivalence, arithmetical, degree, analytical, completeness, class-ladder, descriptive-complexity, Kolmogorov, and undecidability tables remain routed; the arithmetical, analytical, degree, and complexity figures remain present with exact evidence captions. The P/EXPTIME/EXPSPACE complete problems and higher analytical complete relations retain definitions and indexed theorem rows.
- theorem retrieval: accept-source-stable. The six exact-source theorem/lemma hooks remain at their governed boundaries, the enumerability corollary has a durable reference, and the generated named-theorem index contains 364 rows with no raw sort delimiter and one Fagin/Trakhtenbrot identity each.
- labels/references/citations: accept-static-source. The route currently has 158 explicit/typed labels with no duplicate, 129 parsed references with no unresolved destination, and 158 parsed citations with no missing bibliography key.
- annex reciprocity: accept-source-stable. Six `proved=` results have exactly the six matching annex items: local-numbering range, jump extensivity, Kleene--Post, Friedberg--Muchnik, uniform effective back-and-forth, and the \(\Omega\) information theorem. Every annex item has the corresponding body back-reference.

## Round-3 disposition and boundary

- accept-fixed: F5, F7, and F14.
- still-open-source: F15, solely for the two inaccurate nonprinting frontier headers above.
- external by charter/brief: F2 admission/provenance, TeX/reference/index compilation, PDF/visual inspection, human review, administrative closure, and user acceptance.
- verification limit: I inspected the frozen source, registry, and generated TeX text only. I did not run a generator, restoration checker, test, TeX/reference/index build, or PDF build; inspect rendered pages, floats, bookmarks, links, glyphs, or sorting; edit manuscript/control/test/generated files; or read another Part IV seat transcript.
