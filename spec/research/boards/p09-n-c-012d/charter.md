# Board charter: N-c-012.d Sistla--Clarke 1985

- Artifact: `handbook/parts/p09/presentations/n-c-012.tex`, the Sistla--Clarke subsection beginning at line 1851 and ending immediately before the Alpern--Schneider subsection; `handbook/parts/p09/logic-in-computer-science.tex`, Theorems `thm:p09-ltl-pspace` and `thm:p09-ltl-model-checking` and their necessary local context; `handbook/bib/handbook.bib`, entries `SistlaClarke1982` and `SistlaClarke1985`; `spec/research/p09-sistla-clarke-1985-source-note.md`; and `spec/research/p09-source-presentations-lot2-3.md`, subsection `N-c-012.d`.
- Authorities: the complete seventeen-page JACM facsimile, printed pp. 733--749, preserved as `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`; and the distinct complete ten-page STOC predecessor, printed pp. 159--168, preserved as `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`. The page images and three enlarged journal-page derivatives are scholarly reading aids only; the PDFs control.
- Purpose: determine whether the frozen `N-c-012.d` reconstruction is source-faithful, mathematically correct, complete for its stated scope, candid about printed defects and reconstruction, publication-ready as prose, and compliant with the user's terminology rule.
- Mode: audit by direct source reading, mathematical reasoning, and prose inspection.
- Requested by: the governing handbook objective requires three independent scholarly reviews of every reader-facing topic before topic closure.
- Authorship disclosure: the frozen reader, shared integration, bibliography, source note, and source-presentation ledger were assembled or revised in the main `/root` thread. Every reviewer must judge them afresh against the page images and may not use the source note, a prior reviewer, or an earlier board verdict as self-validating authority.
- Board type: live.
- Workspace: `spec/research/boards/p09-n-c-012d`.

## Invariants

- I1: This is book writing. Review consists only of complete primary-source reading, mathematical reconstruction, and prose inspection. No tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.
- I2: Review only the exact frozen hashes below. A mismatch invalidates the verdict.
- I3: Every substantive journal claim must be checked by fresh visual reading of all seventeen printed pages 733--749. Every claimed conference/journal difference must be checked by fresh visual reading of all ten conference pages 159--168. Page images control over OCR, memory, summaries, and prior notes.
- I4: The enlarged p. 742 derivative controls the faint exponent in the sentence counting source truth sets: the journal prints `2^length(f)`, not `2^(2 length(f))`. The enlarged p. 745 page preserves the finite/infinite index defect and the even/odd example conflict.
- I5: The journal is the controlling result. Conference and journal numbering, bounds, hypotheses, proof language, and Section 5 machinery may not be interchanged. The conclusion says that a theorem used in the conference proof contained an error, but it does not identify the particular erroneous inference or a unique repairing lemma.
- I6: `L(O_1,...,O_k)`, `L-tilde(F,X)`, inclusive `U/S`, existential truth in an `R`-structure, satisfiability, and the validity column remain distinct. The article does not print a standalone validity clause; the handbook's universal interpretation clause must remain explicitly reconstructed.
- I7: `size(S)=length(init(S))+card(range(S))` is a finite measure of an infinite structure, not finite-model cardinality. `final(S)` must be the unique maximal suffix, and the acceptable-subsequence measures must remain relative to their ambient structure. The preparatory acceptable-union sentence and Lemma 3.3 both print strict inequalities which conflict with null cases and the following proof's non-strict inequalities; the causes remain unknown.
- I8: The journal's `2S(n)` next distance must not be replaced by the conference's `S(n)`. Closure cardinality `card(SF(f)) <= 2 length(f)` must not be confused with the journal's `2^length(f)` count of realized source truth sets. A `U`-formula is fulfilled before `s_j` for `j >= i`, with a right-hand witness at an index between `i` and `j` inclusive.
- I9: Theorem 4.7 requires both periodic equality and discharge of every pending `U` obligation at every periodic position. Its exact prefix and period bounds, the `Ff` move necessitated by past `S`, the initial-since condition, and the Savitch step must remain visible at their actual proof strength.
- I10: ETL's disjoint nonterminal convention, grammar-indexed formula constructor, normalization, closure, labelled tree `Gamma(S,j,N_i)`, finite-tree termination obligation, Theorems 5.3--5.4 bounds, and continuation-set search must be exact. The finite-string represented-index restriction is handbook-supplied typing. The printed parity sentence conflicts with the printed zero-based clause; no unprinted authorial repair may be chosen.
- I11: Proof sketches, asserted inductions, abbreviated cases, and brief replacements remain unequal. No automata-theoretic proof or Büchi translation may be attributed to Sistla--Clarke.
- I12: Every handbook-introduced technical name must locally supply necessity, exact eliminable definition or axiom, standing, nonredundancy, and later use. Until all five are present, prose must describe an owed artifact rather than name a hypothetical answer.
- I13: Reviewers file independently and may not inspect `ledger.md`, `transcript/chair.md`, another reviewer's transcript, or another reviewer's verdict before filing their own.
- I14: No majority vote. All three seats must independently accept the same frozen snapshot. Any failure, uncertainty, unread source page, or hash mismatch keeps `N-c-012.d` open.
- I15: Acceptance closes only `N-c-012.d` topic-level manuscript review. It does not close Alpern--Schneider, `N-c-012` as a whole, Part IX, any other part, the one final post-freeze publication build, rendered inspection, human review, final-book completion, or user acceptance.

## Criteria

- C1: exact work identity, author order, plural title, issue/date/pages/DOI/ISSN, receipt history, archive provenance, separate conference object, file identities, and rights boundary;
- C2: exact syntax, fragment standing, inclusive temporal semantics, structures and interpretations, existential `R`-truth quantifier, universal-program counterexample relation, and reconstructed validity boundary;
- C3: exact Section 3 structure and ambient-relative subsequence definitions, Lemmas 3.1--3.3, both printed strict/non-strict inequality conflicts, Theorems 3.4--3.7, chain-of-diamonds reduction, definition-before-use for `SF(f)`, a bound start symbol, every Theorem 3.5 labelling rule with current-position-inclusive `F`, the literal recurrent-set check, its loopless-singleton gap, the separately owned handbook correction, formula measures, and proof granularity;
- C4: exact Section 4 reduction chain, the full Lemma 4.3 formula construction and two pure-`U` cases, stuttering boundary, journal/conference next-distance distinction and p. 741 pinpoint, source truth-set definition and count, fulfillment definition, exact Lemma 4.5 deletion and both Lemma 4.6 conclusions, Theorem 4.7 bounds and obligations, and all five directional Theorem 4.1 search recurrences;
- C5: exact ETL grammar semantics with one consistently bound terminal/argument arity, finite/infinite typing conflict, parity conflict, closure, tree, Lemmas 5.1--5.2 including both inherited conclusions, distinct fulfillment obligations, Theorem 5.3 bound, Theorem 5.4 positive rule and negative frontier update, input encoding and continuation sets, and correction-notice calibration;
- C6: exact Table I rows, Theorem 4.1/Table I distinction for `L(U,X)`, the containment proof used in the shared theorem, and complement passage from existential counterexample search to universal model checking;
- C7: complete and accurate conference/journal reconciliation without importing conference theorem numbers or treating the journal additions as a uniquely identified repair;
- C8: source-accurate bibliography, citation locators, source-note page map and proof-status table, source-presentation ledger consistency, and no rights overclaim;
- C9: independently worded prose, definitions before use, exact types and quantifiers, compliance with I1--I15, and no unsupported addition, omitted qualification, or terminology-rule failure.

## Mandatory checks retained in every round

- M01: visually verify the p. 742 exponent as `2^length(f)` and reject every attribution of `2^(2 length(f))` to the article;
- M02: verify that no formal validity clause appears on pp. 734--735 and that the handbook labels its universal clause as reconstruction;
- M03: verify the source's `j >= i` definition of a fulfilled `U`-formula, including the inclusive witness endpoint;
- M04: verify the literal `<` in both the preparatory acceptable-union sentence and Lemma 3.3, their null-sequence failures, every following proof use of `<=`, and Theorem 3.4's non-strict conclusion;
- M05: verify journal `2S(n)` against conference `S(n)` directly from both page images;
- M06: verify every quantifier and bound in Theorems 4.7 and 5.3, including every-periodic-position fulfillment;
- M07: verify the p. 745 finite/infinite sentence and unrestricted index, and distinguish the handbook's represented-position restriction from printed text;
- M08: verify the p. 745 `N_0 -> a_1 a_2 N_0` example and the mismatch between the printed even-state sentence and zero-based odd offsets;
- M09: verify the exact ETL closure and every edge condition in `Gamma(S,j,N_i)`, including the separation of terminal productions from continuation edges;
- M10: verify the finite-tree depth definition, its distinction from until fulfillment, and the continuation-nonterminal set becoming empty within the guessed period;
- M11: verify that the correction notice does not identify the precise bad inference or a uniquely repairing new lemma;
- M12: verify every proof-status qualification and the absence of a Sistla--Clarke Büchi construction;
- M13: verify `L(U) subset L(U,X) subset L(U,S,X)` supplies the exact hardness/upper-bound classification used by the shared theorem;
- M14: verify that universal-path model checking is obtained from existential truth of the negated formula and polynomial-space closure under complement, not by changing the source problem's quantifier;
- M15: apply the five-part terminology rule locally to acceptable subsequence, the handbook's subscripted ambient-parameter disambiguation, source truth set, fulfilled-before obligations, the ETL constructor, and `Gamma`.

## Mandatory round-two repair checks

- M16: verify the page map places `init`, `final`, `range`, and `size` on printed p. 735, places the conclusion only on p. 748, and assigns references to pp. 748--749;
- M17: verify conference p. 160's formal validity definition is now recorded while the identical handbook clause remains explicitly reconstructed relative to journal pp. 734--735; verify the correction notice is limited to an unidentified theorem used in the conference proof;
- M18: verify the exact hypotheses and conclusions of Lemmas 3.2, 3.3, and 3.6, including the zero-prefix condition, acceptable input and output subsequences, every-intermediate-supersequence quantifiers, surviving-position scope, finite subsequence containing the current state, and the separately disclosed strict/non-strict Lemma 3.3 conflict;
- M19: verify each Figure 2 diamond represents one tape-cell position, a complete BI-to-EI traversal represents one instantaneous description, repeated traversals represent a computation, and journal terminal configurations persist forever without tape changes; verify the comparison records the conference's halting language;
- M20: verify that, for `i in N` and positive `p`, source model periodicity is exactly `xi(s_k)=xi(s_(k+p))` for every `k>=i`, and that this equality of complete valuations remains distinct from source-truth-set equality and both obligation-discharge conditions;
- M21: verify the shared model-checking text returns a finite product path plus a nonempty product cycle whose infinite unfolding is the counterexample, without using an undefined periodicity name;
- M22: verify the reader, source note, source-presentation ledger, and charter call `Gamma(S,j,N_i)` only the source's labelled tree (or `Gamma`) and introduce no unsupported proof-tree, derivation-tree, or continuation-tree synonym;
- M23: verify every round-one finding is actually repaired on the frozen round-two hashes and that no repair weakens C1--C9, I1--I15, or M01--M15.

## Mandatory round-three repair checks

- M24: verify the p. 735 unique maximal suffix, exact `s=init(S).final(S)` decomposition, and structure-level `range` and `size` definitions occur before use;
- M25: verify p. 736's acceptable-subsequence `init`, `final`, `range`, and `size` are defined relative to the ambient structure; verify the reader's subscript \(S\) is explicitly eliminable, metalinguistic, necessary, nonredundant, and later used;
- M26: verify the p. 736 preparatory sentence literally prints a strict acceptable-union inequality, the null/null counterexample, and the following proof-supported non-strict subadditivity inequality; verify \(\mu(f)\) is defined before Lemma 3.3 as the number of \(F\)-occurrences;
- M27: verify Theorem 3.5's certificate has `length(p') <= length(f) card(N)`, a subset `C` whose restricted graph is strongly connected, the connecting edge, the printed labelling procedure on every node of `p'` or `C`, and acceptance exactly when `f` occurs in the start label;
- M28: verify `SistlaClarke1982` has a distinct, accurate conference bibliography record and that every direct conference claim resolves to that record while journal claims resolve separately to `SistlaClarke1985`;
- M29: verify every round-two finding is repaired on the frozen round-three hashes, the newly disclosed preparatory strict-sign conflict is source-exact, and no repair weakens C1--C9, I1--I15, or M01--M23.

## Mandatory round-four repair checks

- M30: verify the journal `2S(n)` sentence is pinpointed to printed p. 741, while the conference `S(n)` sentence remains on p. 164 and the journal's broader reduction locator remains pp. 741--742;
- M31: verify Theorem 3.5's labels start empty, process `SF(f)` in increasing length, implement the atomic, negation, conjunction, and `F` iff rules exactly, and accept iff `f` is in the start label; verify the reader and source record preserve the paper's literal strong-connectivity and entry-edge checks, give the concrete loopless-singleton false acceptance, and identify the directed-cycle condition solely as a handbook correction;
- M32: verify Lemma 4.3's exact `P_1/P_2`, `g_1/g_2/g_3`, `f_x`, `h_1/h_2/h_3`, `f'`, and `f''` construction, its `L(F,X)` preservation, both self-loop-sensitive pure-`U` replacements, and the exact use of Lemma 4.2;
- M33: verify Lemma 4.5 deletes `s_i,...,s_(j-1)` while retaining `s_j` and preserves every common state token's truth set; verify every hypothesis and both conclusions (a) and (b) of Lemma 4.6;
- M34: verify Theorem 4.1's exact Boolean, `X`, `U`, and direction-sensitive `S` recurrences, initial-since rule, loop-entry equality, within-period `U` discharge, storage claim, and Savitch step;
- M35: verify Lemma 5.2's additional negated-grammar fulfillment hypothesis and both inherited Lemma 4.6 conclusions; verify Theorem 5.4's positive continuation/terminal iff rule, singleton initialization, exact present-to-next nonterminal update, and within-period emptiness requirement;
- M36: apply the terminology rule to `label`, the Lemma 4.3 auxiliary formula names, the successive guessed sets `A,B`, and the source's `varphi` continuation set: each must be exactly defined, eliminable and metalinguistic in standing, distinguished from nearby semantic objects, and actually used;
- M37: verify every supported round-three finding is repaired on the common frozen round-four hashes, no unsupported strengthening or silent source repair was introduced, and no criterion, invariant, or earlier mandatory check was weakened.

## Mandatory round-five repair checks

- M38: verify `SF(f)` is exactly defined before Theorem 3.5 first uses it, including ordinary subformulas, single-negation mates, double-negation elimination, the `card(SF(f)) <= 2 length(f)` bound, and its distinction from the later `2^length(f)` realized-truth-set count;
- M39: verify the supplied `R`-structure start state is explicitly bound to the Theorem 3.5 start symbol before the prefix and acceptance rules use it in the reader, source note, and compact source presentation;
- M40: verify the Theorem 3.5 prefix `F` rule allows a witness at the current prefix occurrence as required by inclusive `F`; preserve the paper's printed word “after,” explain from pp. 735 and 737 why it must be read non-strictly or identify any non-strict repair as handbook-owned, and keep this issue distinct from the directed-cycle correction;
- M41: verify the ETL terminal count and formula-argument arity remain one consistently bound symbol through the constructor, `Gamma`, Lemma 5.2, Theorem 5.4, the source note, and the compact source presentation; every tuple abbreviation must satisfy the terminology rule locally;
- M42: verify every supported round-four finding is repaired on the common frozen round-five hashes, no source wording is silently strengthened, and no criterion, invariant, or earlier mandatory check is weakened.

## Mandatory round-six repair checks

- M43: verify `n` remains the terminal-count and constructor-arity symbol through the constructor, `Gamma`, Lemma 5.2, and both Theorem 5.4 rules; verify the source's separate Theorem 5.4 use of `n` for total encoded input length is alpha-renamed consistently to `ell_in` in the reader, source note, and compact source presentation, with exact definition, eliminable metalinguistic standing, distinction from arity `n` and fragment notation `L(O_1,...,O_k)`, actual use in `card(SF(f)) <= 2 ell_in`, and no rebinding;
- M44: verify the single supported round-five arity/input-length collision is repaired on the common frozen round-six hashes and that no criterion, invariant, or earlier mandatory check is weakened.

## Review protocol

- Source rule: claims about the authorities cite printed pages read from the source images; claims about the artifact cite exact file lines. OCR is a locator only.
- Verdict rule: the first line must be exactly `ACCEPT` or `REVISE`. `ACCEPT` requires exhaustive checked-clean coverage of C1--C9, I1--I15, and every mandatory check M01--M44. Any blocker, must-fix item, uncertainty, unread page, or identity mismatch requires `REVISE`.
- Evidence rule: each transcript must state the stable agent identifier, runtime model/version if exposed or that it was not exposed, all frozen hashes verified, every journal and conference page visually read, criterion-by-criterion disposition, mandatory-check disposition, and precise evidence locators.
- Independence rule: each seat may create or edit only its assigned transcript. It must not contact another reviewer or read another transcript, the ledger, or the chair record before filing.
- Consensus rule: no finding may be outvoted. If any seat returns `REVISE`, the chair records every supported defect, the manuscript is repaired, and all three seats rereview a new frozen snapshot.

## Round-one roster

- source-fidelity seat: `/root/schmidt_smolka_1991_research/gpss_primary_pass`; complete journal/conference correspondence, provenance, printed defects, omissions, and rights boundary; assigned transcript `transcript/r1-source-fidelity.md`.
- mathematical/proof seat: `/root/schmidt_smolka_1991_research`; semantics, complexity reductions, counts, periodic-model arguments, ETL proof chain, and shared theorem strength; assigned transcript `transcript/r1-mathematical-proof.md`.
- adversarial publication/AGENTS seat: `/root/mcnaughton_1966_research`; omissions, unsupported additions, cross-file consistency, source-versus-reconstruction ownership, terminology, and publication risk; assigned transcript `transcript/r1-adversarial-publication.md`.

## Round-one outcome

- source fidelity: `REVISE`, transcript SHA-256 `E8663895D6C83386791A9787337C6D9A866925226BC58E661338B969FA33FB07`;
- mathematical/proof: `REVISE`, transcript SHA-256 `F7AF2686F50692E8A139A68E9927377B810A9A95F1817F434AE5B5DE3412FB5F`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256 `18005B767EEA69476F7BA8550C78742151FC8694115DEC9D59C74995202699AF`.

Every supported finding is admitted in `ledger.md`. The round-one snapshot is rejected.

## Round-two roster

- source-fidelity seat: `/root/schmidt_smolka_1991_research/gpss_primary_pass`; assigned transcript `transcript/r2-source-fidelity.md`;
- mathematical/proof seat: `/root/schmidt_smolka_1991_research`; assigned transcript `transcript/r2-mathematical-proof.md`;
- adversarial publication/AGENTS seat: `/root/mcnaughton_1966_research`; assigned transcript `transcript/r2-adversarial-publication.md`.

## Round-three roster

- source-fidelity seat: `/root/schmidt_smolka_1991_research/gpss_primary_pass`; assigned transcript `transcript/r3-source-fidelity.md`;
- mathematical/proof seat: `/root/schmidt_smolka_1991_research`; assigned transcript `transcript/r3-mathematical-proof.md`;
- adversarial publication/AGENTS seat: `/root/mcnaughton_1966_research`; assigned transcript `transcript/r3-adversarial-publication.md`.

## Round-four roster

- source-fidelity seat: `/root/r4_source_fidelity`; assigned transcript `transcript/r4-source-fidelity.md`;
- mathematical/proof seat: `/root/r4_mathematical_proof`; assigned transcript `transcript/r4-mathematical-proof.md`;
- adversarial publication/AGENTS seat: `/root/r4_adversarial_publication`; assigned transcript `transcript/r4-adversarial-publication.md`.

All three are fresh direct children of the chair, have no inherited turn
history, own disjoint transcript files, and were instructed not to read or
contact any other seat. Cross-seat verdicts or completion notices are not to be
delivered before all three transcripts are filed.

## Round-three outcome

- source fidelity: `REVISE`, transcript SHA-256
  `654A0FE0D6A6E48CACE30E44790D95D60016FB50CD1111267D8C2BD202D0F194`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `95C1207C5916C68D7953426CBD629966807F0B864AC0ED00E303E0A56F7AC535`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `7A439DF17BCB7649DC9FCE807B05C8E4CFBE7D172C22851FCF314B3F75394BCD`.

Every supported finding is admitted in `ledger.md`. The round-three snapshot
is rejected.

## Round-four outcome

- source fidelity: `ACCEPT`, transcript SHA-256
  `061B66571802596C38CC5D003FF21EFC7FF8F11804FF429F5C53DDC3F3A59E14`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `16D5A0017A558868D10D95F62BB4161F34C2124897358462BEB24D9618FCDE73`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `A4647E76D2F62C7CF25F8193111B5A1D500CA177C150DAA0211AC9ECDADAD6B4`.

The chair read all three transcripts completely. The acceptance does not
override either supported rejection. The round-four snapshot is rejected and
every supported finding is admitted in `ledger.md`.

## Round-five roster

- source-fidelity seat: `/root/r5_source_fidelity`; assigned transcript `transcript/r5-source-fidelity.md`;
- mathematical/proof seat: `/root/r5_mathematical_proof`; assigned transcript `transcript/r5-mathematical-proof.md`;
- adversarial publication/AGENTS seat: `/root/r5_adversarial_publication`; assigned transcript `transcript/r5-adversarial-publication.md`.

All three are fresh direct children of the chair with no inherited turn
history. They own disjoint transcript files and may not read or contact any
other seat. No cross-seat verdict or completion notice is to be delivered
before all three transcripts are filed.

## Round-five outcome

- source fidelity: `REVISE`, transcript SHA-256
  `B657B256C1A13125341BB7F45F00F09F01D152B43A02C88E124D5B33BFEFA6AB`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `A58167217B11596CFADD945109B71B4EC327FC1DAB84DF21197BAEA9B87E3C17`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `E87CEF5BEF71921FA64C5C8F2F65C23039D9E29ACFA5B8C173CA21BFB28AD5FB`.

The chair read all three transcripts completely. All three independently
identified the same supported defect: the round-five reader and source note
bound `n` as terminal/constructor arity and then rebound it as total encoded
input length immediately before Theorem 5.4 reused the constructor tuple.
The round-five snapshot is rejected and the finding is admitted in
`ledger.md`.

## Round-six roster

- source-fidelity seat: `/root/r6_source_fidelity`; assigned transcript `transcript/r6-source-fidelity.md`;
- mathematical/proof seat: `/root/r6_mathematical_proof`; assigned transcript `transcript/r6-mathematical-proof.md`;
- adversarial publication/AGENTS seat: `/root/r6_adversarial_publication`; assigned transcript `transcript/r6-adversarial-publication.md`.

All three are fresh direct children of the chair with no inherited turn
history. They own disjoint transcript files and may not read or contact any
other seat. No cross-seat verdict or completion notice is to be delivered
before all three transcripts are filed.

## Round-six outcome

- source fidelity: `ACCEPT`, transcript SHA-256
  `30C808BE930AE34892BA0B2D27A6A4B850E87D9F1D0ADF47E5F575B2450C39E3`;
- mathematical/proof: `ACCEPT`, transcript SHA-256
  `39B341A10610CDB93D68ED7E3C1C97192BDED250A5D80F22000466A2C830A0F9`;
- adversarial publication/AGENTS: `ACCEPT`, transcript SHA-256
  `7220F7C25BA966668D0C02E8C74FC5CF5B4389A744DC7D639B59B5C941AC7CF3`.

The chair read all three transcripts completely and independently confirmed
that the ten frozen hashes remained unchanged. Every seat reports exhaustive
checked-clean coverage of C1--C9, I1--I15, and M01--M44, with no blocker,
must-fix item, uncertainty, unread source page, or identity mismatch. No vote
or carried-forward verdict is involved. The exact round-six snapshot is
unanimously accepted for `N-c-012.d` topic-level manuscript review only.

## Frozen round-one SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `handbook/parts/p09/presentations/n-c-012.tex`: `A4E1059FB5AE5BB577C76B443D05A26BF31F711449C7537B71027F7E72A958CC`
- `handbook/parts/p09/logic-in-computer-science.tex`: `5F3903C0793116D497B86FB8DC06CE6AF2DE6B8FA71C727D74F10054F8905A14`
- `handbook/bib/handbook.bib`: `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `CF865B89EA3C6C5DF44E9D900D203441B015AF2977F1F383246C52431FCAB533`
- `spec/research/p09-source-presentations-lot2-3.md`: `E2012A854194277F8C4CC964872428454B2ADEA3624DEE97536833868E37CCE9`

## Frozen round-two SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `handbook/parts/p09/presentations/n-c-012.tex`: `48D2F8F946AFFC394613D7895E89175099CC9FA73800BDA36A3C5F63353C6AD5`
- `handbook/parts/p09/logic-in-computer-science.tex`: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
- `handbook/bib/handbook.bib`: `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `D7E85E5AC951C56F607099A5756C1AA5CEEC02DB8D0CC3EC359E17EBE2450FCD`
- `spec/research/p09-source-presentations-lot2-3.md`: `D5BD9F8BA7A12AFD7A8A08CDAAFB2E0E4C0E0B48E0BD83D5BDC06AA08D2E8353`

## Frozen round-three SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png`: `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`
- `handbook/parts/p09/presentations/n-c-012.tex`: `1F5792A97766A695A58EF5FAA259F97D8CD6E50B720FB14BEDEA358E3505E7F8`
- `handbook/parts/p09/logic-in-computer-science.tex`: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
- `handbook/bib/handbook.bib`: `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `3C1F2DEB6D3224D61E1008B59DF353F56BE096A951E936B0060C583497E37565`
- `spec/research/p09-source-presentations-lot2-3.md`: `414CFAEF19DB8F53B76E6A4805EA20F3D2DABFCA245FC0DD6F537FE32F8253DE`

## Frozen round-four SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png`: `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`
- `handbook/parts/p09/presentations/n-c-012.tex`: `45E2B1F4A97B1049247FD198CDF69C67794D129AEB28582FE595DC34EDF7ABD8`
- `handbook/parts/p09/logic-in-computer-science.tex`: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
- `handbook/bib/handbook.bib`: `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `1E734EF089EEA077DE90229411726D85708A102D914EFE4F7956B7DDE9EE9094`
- `spec/research/p09-source-presentations-lot2-3.md`: `40F0AE94BB9B763F941B421F63854B17A426C1989084F6262ACD59071C0A7E8D`

The repaired reader subsection spans lines 1851--2589. Round four reviews
this exact ten-object snapshot. No manuscript or source-record file in the
snapshot may change before all three independent verdicts are filed.

## Frozen round-five SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png`: `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`
- `handbook/parts/p09/presentations/n-c-012.tex`: `C760B8B413937A9002F017704956EBFFB2AF7ED44AD8AD8FF0EC4366E526EC79`
- `handbook/parts/p09/logic-in-computer-science.tex`: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
- `handbook/bib/handbook.bib`: `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `79E0677D27769153BC5C078242CDD77916350B926C87B25F91F78A9C943F0F19`
- `spec/research/p09-source-presentations-lot2-3.md`: `9739EBEE2BBE5F24857B9C900F831B7F9783F5BAA00652E02E3F5DD755E08D22`

The repaired reader subsection spans lines 1851--2622. Round five reviews
this exact ten-object snapshot. No manuscript or source-record file in the
snapshot may change before all three independent verdicts are filed.

## Frozen round-six SHA-256 snapshot

- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf`: `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5`
- `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf`: `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png`: `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png`: `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1`
- `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png`: `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`
- `handbook/parts/p09/presentations/n-c-012.tex`: `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA`
- `handbook/parts/p09/logic-in-computer-science.tex`: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`
- `handbook/bib/handbook.bib`: `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`
- `spec/research/p09-sistla-clarke-1985-source-note.md`: `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B`
- `spec/research/p09-source-presentations-lot2-3.md`: `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5`

The repaired reader subsection spans lines 1851--2631. Round six reviews
this exact ten-object snapshot. No manuscript or source-record file in the
snapshot may change before all three independent verdicts are filed.
