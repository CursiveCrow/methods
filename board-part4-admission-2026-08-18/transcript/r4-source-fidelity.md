# Part IV admission board — round 4 narrow source-fidelity verification

- seat: source-fidelity/evidence
- scope: corrected frontiers body/annex headers and drift from the accepted r3 source snapshot only
- boundary: read-only; no other Part IV transcript read; no manuscript, source, provenance, control, registry, generated, or test edit; no build or test

## Corrected frontiers headers — accept

The body summary at `handbook/parts/p04/frontiers-of-computability.tex:2` now says “Frontiers survey with cited results and proved Omega/computable-structure results.” This accurately covers both annex-backed results: `thm:p04-omega-halting` at `handbook/parts/p04/frontiers-of-computability.tex:357-365` / `annex:p4.frontiers.2` at `handbook/annex/p04/frontiers.tex:25-58`, and `thm:p04-rational-order-uniform-index` at `handbook/parts/p04/frontiers-of-computability.tex:618-627` / `annex:p4.frontiers.1` at `handbook/annex/p04/frontiers.tex:3-23`.

The annex summary at `handbook/annex/p04/frontiers.tex:1` now says “Proofs for the separately authored Omega and computable-structure results.” It therefore states the file's two proof roles exactly and no longer describes only the computable-structure corollary.

## No-drift verification — accept

Only those two comment lines changed from the accepted r3 snapshot:

- Current body SHA-256 is `68E283F1CD364779BA7E0A525923B0C16FCE962519C8BEDEAAF087BA0AD20CB4`. Replacing only the corrected line 2 in memory with its prior text reproduces the accepted r3 hash `057D4B23BBD4427A72A03CEEE776C861A4D0B3087B9F116A3A85389B42A16429` exactly.
- Current annex SHA-256 is `622F507B7A8FBA1389A2A3EE0403102E79AD335C17E36DDD37F0EF5E4AC15D57`. Replacing only the corrected line 1 in memory with its prior text reproduces the accepted r3 hash `90025FC53C9605880615065FBE86737922BBB32BBFF751022B583BF403B4E8A1` exactly.
- Every other hash in the accepted focused snapshot remains unchanged: the Part IV body/annex drivers, complexity chapter, degree body/annex, Part III finite-model chapter, registry, both generated symbol surfaces, generated theorem index, and bibliography.

## Verdict

**accept.** The narrow header residual is closed and no source/content drift was introduced. F2 provenance/control admission and the build, visual, human, and final-user gates remain explicitly external and are not closed or inferred by this verdict.
