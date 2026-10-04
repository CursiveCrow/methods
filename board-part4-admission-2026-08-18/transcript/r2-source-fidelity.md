# Part IV admission board — round 2 source-fidelity verification

- seat: source-fidelity/evidence
- round: r2 deliberation and live-fix verification
- scope: the current live graph rooted at `handbook/parts/p04.tex` and `handbook/annex/p04.tex`, all 17 exact restoration artifacts, the changed body/annex supplements, bibliography records, symbol registry, theorem hooks, and the generated symbol/theorem reader surfaces named in the brief
- independence: I did not open another Part IV seat transcript
- boundary: read-only review; I made no manuscript, source, provenance, control, registry, generated, or test edit and ran no build or test

## R1 findings

### F1 — accept-fixed

The routed editorial units now use ordinary attribution and state their nonreplacement boundaries without printing construction/admission debt. The body route is explicit at `handbook/parts/p04.tex:34-41,75-78`, and the annex route is explicit at `handbook/annex/p04.tex:3-5`. Representative reader-facing notices are now clean at `handbook/parts/p04/machines-effective-procedures-supplement.tex:5-10`, `handbook/parts/p04/universal-reductions-supplement.tex:5-10`, `handbook/parts/p04/decision-hierarchy-apparatus-supplement.tex:4-8`, `handbook/parts/p04/degrees-and-priority-continuation.tex:14-18`, and `handbook/annex/p04/degrees-and-priority-continuation.tex:15-17`. The remaining `OPEN` at `handbook/parts/p04.tex:80-83` is comment-only and concerns an intentionally unrouted historical audit; the rendered uses of “open” at `handbook/parts/p04/complexity.tex:309-405` are genuine open complexity questions. No routed editorial notice still exposes an internal workflow ID or source/build/visual/acceptance gate.

### F2 — still-open, deliberately external

The administrative admission boundary has not been promoted by these source findings. Representative exact records still say `handbook_destination.status = open/missing` and retain pending completeness/independent-source/build/visual fields at `spec/provenance/SRC-07494-07505.json:39-75` and `spec/provenance/SRC-08898-09079.json:46-83`. The reviewed-unit and reviewed-obligation arrays remain empty at `spec/provenance/reviewed-handbook-unit-records.json:5` and `spec/provenance/reviewed-register-obligation-records.json:6`. This is the separate provenance/control boundary established by F2; build, visual, human, and user gates also remain outside this source/content verdict.

### F3 — accept-fixed

The reader order and notation ownership are now coherent. The minimization/formalisms supplement is routed after the exact machine chapter and before the exact universal-computation chapter at `handbook/parts/p04.tex:33-35`; its normal-form result at `handbook/parts/p04/machines-effective-procedures-supplement.tex:67-88` uses ordinary equality plus an explicit domain clause and does not redefine Kleene equality. The sole active definition of `\simeq` remains the exact one at `handbook/restoration/inherited-07851-08048.tex:49-52`. The universal supplement at `handbook/parts/p04/universal-reductions-supplement.tex:12-24` uses that source notation and no longer introduces the redundant `\sim_m`; mutual many-one reducibility remains the exact `\equiv_m` at `handbook/restoration/inherited-08898-09079.tex:153-157`. The live registry now records the exact-source roles and scopes for `\simeq`, `\chi_A`, `\chi_R`, `U(e,x)`, and `\equiv_m` at `handbook/registry/symbols.csv:49,232-237,252`. The Kleene--Post and priority constructions use the fixed `\varphi_e^B`/characteristic-function notation at `handbook/parts/p04/degrees-and-priority-continuation.tex:84-108,124-164` rather than creating another functional notation.

### F4 — accept-fixed

Part IV no longer duplicates the public computable-presentation definition. It points to `def:p03-computable-presentation` and `def:p03-computably-categorical` and introduces only the coding-dependent index of a presentation at `handbook/parts/p04/frontiers-of-computability.tex:606-616`. The new uniform corollary is exactly scoped to valid indices at `handbook/parts/p04/frontiers-of-computability.tex:618-627`, has status `proved=annex:p4.frontiers.1`, and its reciprocal annex proof at `handbook/annex/p04/frontiers.tex:3-23` gives the alternating effective back-and-forth, the total compiler, and the explicit invalid-index qualification.

### F5 — accept-fixed

The minimization types now agree. `handbook/parts/p04/machines-effective-procedures-supplement.tex:27-47` defines the partial least-zero operator, separately defines the relational least-true notation through the explicit zero-test `z_R`, and explains their type difference. The partial-recursive class is restricted to positive arities at `:49-61`. Kleene normal form at `:67-87` states the domain first and uses the relational abbreviation only on the domain. The registry's `\mu` row records the same distinction at `handbook/registry/symbols.csv:234`. The URM definition at `handbook/parts/p04/machines-effective-procedures-supplement.tex:116-145` now fixes the Shepherdson--Sturgis instruction set, the undefined zero-decrement behavior, the sole halting exit, and the preservation-style function convention. These source roles match the primary Shepherdson--Sturgis presentation recorded by `ShepherdsonSturgis1963` (JACM 10(2), 217--255, [DOI 10.1145/321160.321170](https://doi.org/10.1145/321160.321170)).

### F6 — accept-fixed

The missing lower reduction is now a separately status-bearing lemma: `handbook/parts/p04/degrees-and-priority-continuation.tex:43-53` states `A\leq_m A'`, distinguishes it from the cited diagonal nonreducibility half, and the summary row uses both at `:297-302`. The reciprocal proof at `handbook/annex/p04/degrees-and-priority-continuation.tex:19-37` constructs a total primitive-recursive query-program compiler `q` and proves `n\in A` iff `q(n)\in A'` without borrowing a sketched theorem. Together with the exact jump theorem, this licenses strict degree increase. The historical source role remains correctly assigned to [Kleene--Post 1954](https://doi.org/10.2307/1969708) and Rogers.

### F7 — accept-fixed

The Kleene--Post construction is no longer a citation-only conclusion. The body method at `handbook/parts/p04/degrees-and-priority-continuation.tex:84-108` fixes the oracle numbering, typed characteristic-function requirements, finite strings, the `\varnothing'` decision, and the distinction from c.e. finite injury; the theorem at `:110-114` is `proved=annex:p4.degrees.2`. The complete proof at `handbook/annex/p04/degrees-and-priority-continuation.tex:39-97` now explicitly wraps every oracle decider as a total `0/1` numerical program (`:48-53`), defines finite-oracle convergence (`:54-57`), reduces the finite-extension question to `K` and then to `\varnothing'` (`:59-79`), and proves permanence, totality, both diagonal requirements, reducibility to `\varnothing'`, and strictness (`:81-95`). This is the finite-extension construction belonging to [Kleene--Post 1954](https://doi.org/10.2307/1969708), not a claim that its witnesses are c.e.

### F8 — accept-fixed

Friedberg--Muchnik now has the proof standing required by the registered full construction. The method and theorem are at `handbook/parts/p04/degrees-and-priority-continuation.tex:124-171`, with `proved=annex:p4.degrees.4`. The reciprocal annex proof at `handbook/annex/p04/degrees-and-priority-continuation.tex:99-171` defines stage convergence and finite use (`:107-116`), gives the decider-to-characteristic-function wrapper covering every Turing reduction (`:118-123`), specifies finite stage state, empty restraint `0`, a fair scheduler, initialization, effective c.e. indices, and symmetric strategies (`:125-145`), and completes the finite-injury induction and strict-intermediate-degree argument (`:147-169`). No sketch note or omitted uniform-index obligation remains. The independent historical sources remain separated as Friedberg 1957 ([DOI 10.1073/pnas.43.2.236](https://doi.org/10.1073/pnas.43.2.236)) and Muchnik 1956 (`handbook/bib/handbook.bib:855-865`).

### F9 — accept-fixed

The MRDP entry now reaches the promised survey depth. `handbook/parts/p04/frontiers-of-computability.tex:426-462` gives the easy direction and the DPR/Robinson/Matiyasevich source split, displays the Pell family and its solution parameterization (`:433-440`), gives both addition recurrences with the necessary factor `d` (`:441-445`), states Robinson's growth condition and the Fibonacci-type bridge (`:447-456`), and explicitly lists the substantive omitted lemmas (`:458-462`). It remains honestly a proof survey, not a full proof. The content and ceiling correspond to Davis's authoritative exposition, [“Hilbert's Tenth Problem is Unsolvable”](https://math.umd.edu/~laskow/Pubs/713/Diophantine.pdf), and to the primary DPR/Matiyasevich records cited at the live method.

### F10 — accept-fixed

The required arithmetical-hierarchy figure is now present at `handbook/parts/p04/decision-hierarchy-apparatus-supplement.tex:50-93`. Its heavy arrows are explicitly strict inclusions licensed by the hooked exact strictness theorem (`:83-85`); its intersections are identified as definitional; and `K`, its complement, `\mathsf{TOT}`, and the higher iterated-jump pattern are tied to the hooked exact classification and Post theorems (`:86-91`). The adjacent table at `:10-48` keeps formula classes, boldface relation classes, Turing-level classification, and many-one completeness roles distinct. This closes F10 as a source/content finding; figure rendering remains a later visual gate.

### F11 — accept-fixed

The Church--Turing boundary now assigns the historical roles exactly at `handbook/parts/p04/machines-effective-procedures-supplement.tex:205-220`: Church's proposal is lambda-definability, equivalence with general recursiveness is attributed to Kleene, and Turing's role is machine analysis. The passage also keeps the formal-model equivalence separate from the informal thesis and from physical/computational-complexity extrapolations. This matches Church's primary paper, [DOI 10.2307/2371045](https://doi.org/10.2307/2371045), together with `Kleene1936` and `Turing1937Lambda`.

### F12 — accept-fixed

Both joint historical names now carry both primary roles. The Cook--Levin theorem cites Cook and Levin in its statement block at `handbook/parts/p04/complexity.tex:204-212`, and the historical-source list repeats both at `:510-520`. The semigroup result is titled Post--Markov and cites both sources at `handbook/parts/p04/frontiers-of-computability.tex:494-497`, with both repeated in the catalog/further reading. The new `Levin1973` record at `handbook/bib/handbook.bib:133-143` distinguishes English and original pagination and links the [Math-Net record](https://www.mathnet.ru/eng/ppi914); `Markov1947` at `:3631-3641` distinguishes original and English-translation containers/pages and links the authoritative Math-Net profile. These sources are attached to their concrete theorem records rather than offered as unattached bibliography additions.

### F13 — accept-fixed

The corrected bibliography roles are present exactly where requested. `Muchnik1956` has volume 108, issue 2, pages 194--197, and the Math-Net locator at `handbook/bib/handbook.bib:855-865`; `Matiyasevich1970` has volume 191, issue 2, original pages 279--282, translation pages 354--358, and its article locator at `:878-887`; `Novikov1955` now records the Steklov series/volume/pages together with Academy of Sciences of the USSR, Moscow, and the exact Math-Net record at `:3643-3653`. The current fields agree with the linked authoritative records and preserve original/translation and serial-monograph roles instead of conflating them.

## Changed dependencies and new repair-fallout records

### SF-N1 [must-fix] — still-open: generated named-theorem evidence is stale

- location: live Omega theorem `handbook/parts/p04/frontiers-of-computability.tex:357-365`; reciprocal proof `handbook/annex/p04/frontiers.tex:25-51`; retired duplicate identity boundary `handbook/parts/p03/finite-model-theory.tex:96-100`; stale generated rows `handbook/generated/named-theorem-index.tex:177,342`
- defect: The body now truthfully marks `thm:p04-omega-halting` as `proved=annex:p4.frontiers.2`, and the annex supplies the complete left-c.e./noncomputability/finite-bit proof. The generated theorem index nevertheless still prints `citation Chaitin1975` for that theorem. It also still publishes the retired `thm:p03-trakhtenbrot`, even though current Part III prose expressly identifies the hooked exact-source `thm:trakhtenbrot` as the single public statement and no longer declares a second theorem environment. Thus the live theorem bodies/hooks are correct, but the whole-book generated evidence surface states two obsolete source/status facts.
- exact correction: Regenerate `handbook/generated/named-theorem-index.tex` from the current reachable route using `tools/build_named_theorem_index.py --write`; verify that the Omega row points to `annex:p4.frontiers.2`, that `thm:p03-trakhtenbrot` disappears, that the hooked exact `thm:trakhtenbrot` remains, and that the sole Fagin identity remains `thm:p03-fagin`.
- status: still-open generated-reader blocker.

### SF-N2 [must-fix] — still-open: generated symbol tables do not reflect the corrected registry

- location: corrected registry `handbook/registry/symbols.csv:247,283`; stale public registry table `handbook/generated/symbols-tables.tex:277-278`; stale master symbol index `handbook/generated/symbol-index.tex:274,282`; reader routes `handbook/parts/p01/symbol-registry.tex:32` and `handbook/parts/p14/master-tables.tex:246`
- defect: The live CSV now says `\mathsf{Comp}` is the bounded formula supplied by the inherited theorem and expressly disclaims a canonical-first formula; it also registers `\mathsf{Run}_{U_K}` as the fixed prefix-machine/string analogue with primitively recursive intertranslation. The generated table/index still publish the deleted `\mathsf{Acc}` row and the false old “first bounded formula in length-lexicographic order” claim for `\mathsf{Comp}`, and they omit `\mathsf{Run}_{U_K}`. Because both generated files are routed to readers, the corrected registry alone has not repaired the reader surface.
- exact correction: Regenerate both outputs from current `handbook/registry/symbols.csv` with `tools/symbols2tex.py`; verify deletion of `\mathsf{Acc}`, replacement of the `\mathsf{Comp}` note, addition of `\mathsf{Run}_{U_K}`, and stable registry anchors/index links.
- status: still-open generated-reader blocker.

## Additional changed-content verification

- **Analytical universal sets — accept-fixed:** `handbook/parts/p04/frontiers-of-computability.tex:68-90` fixes an effective enumeration of valid lightface definitions, treats invalid Sigma-side codes as false, defines the Pi relation by complement, and states completeness under effective many-one reductions. The two objects are registered at `handbook/registry/symbols.csv:275-276`. This is the universal-relation role supplied by Kleene's hierarchy paper (`handbook/bib/handbook.bib:3519-3528`, [DOI 10.1090/S0002-9904-1955-09896-3](https://doi.org/10.1090/S0002-9904-1955-09896-3)); it is not presented as a new pointclass or a boldface assertion.
- **Omega status — body/annex accept-fixed, generated residual SF-N1:** The proof at `handbook/annex/p04/frontiers.tex:25-51` correctly obtains left-c.e. approximation, derives noncomputability by bounded halting, excludes the dyadic ambiguity, and proves the first-`n`-bits decision claim. Only the generated evidence row remains wrong.
- **Fixed-width succinct addressing — accept-fixed:** `handbook/parts/p04/complexity.tex:171-202` defines logspace reducibility, a padding-stable decoded encoding, `\operatorname{bin}_m(i)`, CVP, SCVP, and STQBF before use; the fixed-width address is distinguished from the machine-input numeral. `\operatorname{bin}_m`, logspace reducibility, CVP, SCVP, and STQBF are registered at `handbook/registry/symbols.csv:229,306-309`. The theorem's three source roles are stated together and cited to `Papadimitriou1994`; no additional proof is claimed.
- **Canonical Fagin identity — accept-fixed:** the only current theorem environment is `thm:p03-fagin` at `handbook/parts/p03/finite-model-theory.tex:80-90`. Part IV points back to that identity at `handbook/parts/p04/complexity.tex:465-491`, and `handbook/generated/named-theorem-index.tex:128` contains the single Fagin row. No active `thm:p04-fagin` remains.
- **Governed exact-result hooks — accept-fixed:** `handbook/parts/p04.tex:5-73` installs and removes narrowly scoped hooks. Direct environment-order inspection shows the hooks land on the first lemma and first theorem in `inherited-07753-07843.tex` (machine decidability and c.e. equivalences), the sole corollary and second theorem in `inherited-08248-08305.tex` (enumerable validity and Trakhtenbrot), the third and fourth theorems in `inherited-08710-08876.tex` (classification and strictness), and the second theorem in `inherited-08898-09079.tex` (Post). The six theorem/lemma hooks are represented in the generated named-theorem index; the corollary hook is a navigation target, not an index row. SF-N1 concerns stale non-hooked rows, not hook placement.

## Coverage and boundaries

- **Checked clean:** all 17 exact artifacts still compare line-for-line with `source/formal-logic-reference.tex:7494-9079`: 17/17 records, 1,586/1,586 lines, zero mismatch; their live route remains once each and in authority order at `handbook/parts/p04.tex:3-73`.
- **Checked clean on the rooted body/annex graph:** a comment-stripped recursive route scan found 158 active statement/navigation/annex IDs with no duplicate; 58 distinct parsed references with no missing target; 51 distinct citation keys with no missing bibliography record; and six distinct `proved`/`sketched` annex targets with six reciprocal annex items, no missing target, and no orphan. These are static source checks, not a build.
- **Lot 1:** checked clean after F1/F3/F5/F11 repairs.
- **Lot 2:** checked clean after F1/F3/F5/F10 and the exact-hook repairs; F2 remains external.
- **Lot 3:** checked clean after F3/F6/F7/F8/F13 repairs; F2 remains external.
- **Lot 4:** substantive source/content is checked clean after F4/F9/F12/F13 plus the analytical, Omega, complexity, and canonical-Fagin checks above; the two generated whole-book reader surfaces remain blocked by SF-N1/SF-N2.
- **Not checked and not inferred:** compilation, PDF destinations, counters/bookmarks/TOC, figure and table legibility, index rendering, page layout, visual inspection, legacy human review, administrative closure, and final user acceptance. F2 and these later gates must remain separate even after SF-N1/SF-N2 are regenerated.

## Round-2 source verdict

F1 and F3-F13 are **accept-fixed** on the frozen live manuscript bytes. F2 is **still-open external** by design. Source/content admission is **not yet accepted** solely because SF-N1 and SF-N2 leave obsolete source/status claims on two routed generated reader surfaces; their corrections are deterministic regeneration and verification, not new mathematical work.
