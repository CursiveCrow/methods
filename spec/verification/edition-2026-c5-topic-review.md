# C5 independent mathematical and topic review

Date: 7 September 2026. Reviewer context: `/root/c5_topic_review`, an independent Codex subagent assigned the mathematical/topic role. The runtime identifies the assistant as Codex; an exact backend model identifier, version and build were not exposed to this reviewer and are not inferred. Author notes were used as locators. No other new C5 review was read, and no other review author was contacted before this report was filed.

Authoritative checkout: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The checkout contains extensive existing modifications and untracked files. The identities below are hashes of the actual working files. The reviewer owns only this report.

## Decisions and scope

| Unit | Topic decision | Extent of decision |
| --- | --- | --- |
| ACF categoricity, active restoration lines 177–218 | PASS | The stated classification application, existence claim, isomorphism argument and countable qualification are mathematically correct under the explicit Choice hypothesis and cited field-theoretic dependencies. |
| Tseitin body and both complete annex proofs | PASS | The primitive construction, extension and projection theorem, CNF encoding, size bounds and worked and failure examples are correct under their stated conventions. |
| Retained DLO substring | PASS for preservation | Its exact protected bytes match the freeze. Its unchanged proof is not reopened by this review. |

No mathematical correction is requested for these frozen units. This is a text review. It supplies neither six-gate admission nor a source-acquisition, build, render, visual, provenance-migration or publication acceptance record. The source-reading limitation below remains explicit; in particular, the ACF decision does not promote cited field classification or algebraic-closure results into proofs supplied by the manuscript.

## Frozen identities and actual read extent

The entire Tseitin body and annex were read. The ACF target and the necessary categoricity definition were read; surrounding later material was also visible but is not accepted by this report. The protected DLO interval was extracted and hashed without reopening its proof. Intervals below are inclusive physical lines. Hashes are whole-file SHA256 unless explicitly described as a substring.

| File | Read interval used in this review | SHA256 |
| --- | --- | --- |
| `handbook/parts/p02/tseitin-transformation.tex` | 1–188, complete | `9E09805F966C64DF13CFDC0471C40AE0E0DCC9B2DC187B68E915E5E5A334E0D5` |
| `handbook/annex/p02/tseitin-transformation.tex` | 1–167, complete | `975195E565E2AE77F128EDA22568BF728555380F03E360006D4A5D67C4D19561` |
| `handbook/restoration/inherited-07295-07468.tex` | Target 177–218; dependency/context 1–40 and 219–250; DLO 108–176 hash only | `A133AD43A7AF91BEC6DC90B1AC5335F0524C1447869CB382B05175138A9C0505` |
| `handbook/restoration/inherited-01661-01816.tex` | 1–156, complete: grammar, abbreviations, association and unique readability | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` |
| `handbook/restoration/inherited-01817-01898.tex` | 1–82, complete: truth clauses, coincidence and semantic notions | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |
| `handbook/parts/p02/propositional-substitution.tex` | 1–181, complete; the required occurrence definition is 66–86 | `5B39B8DC52B60442850707C6D4DF2C7E853929FC52541F85D839986BFD8DC146` |
| `handbook/restoration/inherited-01946-02186.tex` | 1–244, complete; clause interpretation and semantics 4–95, forward link 210–212 | `185C35156F2E1983B1BEF028888C3FF2A0DFFF333366CFF1A3D2769225E37468` |
| `handbook/restoration/inherited-07150-07294.tex` | 125–145; ACF characteristic and language at 137–144 | `CCB19227218A479328D04079082C149BBD9ACF4B587C45D13FFF49A07548EFF8` |
| `handbook/restoration/inherited-14351-14400.tex` | 1–50, complete: existing Part 12 root and conjunction example | `A7A70819ADFAD23F3B5F16285E253E63D9F6FA0914AE58F1D80E8F0F2BFCF355` |
| `handbook/parts/p02.tex` | 1–67, complete | `77811CDF11B5E6E2FBB3B56A45B229D973BA39815926DE29D49823D3F2FA7854` |
| `handbook/annex/p02.tex` | 1–18, complete | `CB924992058BF0846B4D83CB35E24165A2DB7BDC8B0BA1A974FC770F0ACF13D6` |
| `handbook/parts/p03.tex` | 40–65 | `3694A5CDE0762B4CF489AA640AECA2F00B9216BF16FE4BFA2A43E0FD4583BA69` |
| `handbook/bib/handbook.bib` | Required records 4000–4011 and 5354–5361 | `84FF6BDD200A86DB3D82B84B0405376C98F395C7E504DA6CC38F52EFF340B7CC` |
| `handbook/handbook.sty` | 338–352 and 461–495 | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |

The three-line active restoration wrappers were also read completely:

| Wrapper under `handbook/restoration/` | SHA256 |
| --- | --- |
| `scope-SRC-01661-01816.tex` | `DCE9A9D142AAAFF4DDD0E5746CB5B53609BCBC96D0A2E90752D18AD16378CFD4` |
| `scope-SRC-01817-01898.tex` | `ABCC08C992478EBE863CA4C0E76D18BE4E7A719B69592AB195C168134249F683` |
| `scope-SRC-01946-02186.tex` | `9A32F4BF05D529A3A51242256A17213A1779F96F0AC70341C642F06D6DFB5E0A` |
| `scope-SRC-07150-07294.tex` | `8D98CD2AC8394A84099454D5C736DAE61FA941D4C118604D75676C8C555F1DC3` |
| `scope-SRC-07295-07468.tex` | `AC350CD043C0F1CBFED3E6003DEF20533D424AE428B482F8C94ED41587437A48` |

Governing and author materials were read completely:

| Material | Lines | SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-c5-integration.md` | 1–78 | `AD1D03DFE3CC1869EDC67AA4F6B237153953C5543AEC5203230DDDACBDA39216` |
| `spec/research/edition-2026-c5-acf-attribution.md` | 1–85 | `99F8A383D3F31255087CDF24610A9B4E3766A942A40536EF1FC090FE30FC448E` |
| `spec/research/edition-2026-c5-tseitin.md` | 1–148 | `E53375773B51FBE002ED316477D6B20FED63DD29022D6AA9152B8157FF18B48D` |

The DLO interval 108–176, encoded as its existing UTF-8 LF bytes including the trailing blank line before ACF, has length 3,539 bytes and SHA256 `9AC556285A7ABB3F42E7652606A28BE92EE3C50102F5F045FB9805A20617A213`. This exactly matches the protected substring in the integration freeze.

## Tseitin mathematical findings

### Primitive clauses and assignment domains

The grammar contains exactly variable leaves, bottom, negation, conjunction, disjunction and implication. The body at 15–24 explicitly expands defined connectives before construction and gives finite valuations their own supported evaluation convention. The occurrence definition agrees with the inherited root-to-node words: children of a position `a` are `a1` and `a2`. Every nonvariable occurrence, including bottom, receives a fresh distinct variable; original variable leaves are reused (body 28–58). Equal subformula strings at different nonvariable positions therefore remain different tree occurrences.

Every displayed gate at body 61–70 has the claimed truth function. Independent case checking gives the following outputs, with `F,T` for falsity and truth:

| Inputs `(x,y)` | Conjunction output | Disjunction output | Implication output |
| --- | --- | --- | --- |
| `(F,F)` | F | F | T |
| `(F,T)` | F | T | T |
| `(T,F)` | F | T | F |
| `(T,T)` | T | T | T |

The two negation clauses permit precisely `(z,x)=(T,F)` and `(F,T)`; the bottom unit forces `z=F`. When both binary representatives are the same variable, the same checks restrict to the diagonal rows and remain correct. In particular, the implication gate for `P -> P` forces its representative true. Set removal of duplicate literals and clauses does not change any truth condition. The annex at 13–48 establishes both directions for every primitive gate.

The existence definition at annex 50–65 uses the value of each original subformula under `v`; it is noncircular. Freshness and distinctness prevent conflicting assignments. The leaf-to-root induction at 67–86 forces every auxiliary value, proving uniqueness exactly on `V union Z_phi`. An atomic input has no auxiliary variables, and the extension is `v` itself; a variable-free input has the empty input valuation. Body 117–123 correctly avoids claiming uniqueness outside that finite union or treating an already total valuation as still free on its assigned auxiliary symbols.

### Root, formula encoding and counterexamples

Body 73–89 adds the root for every input, including an atom. The annex at 88–106 proves that the unique defining extension satisfies that clause exactly when the original input is true. Thus its restriction/extension argument establishes the stated model projection, equisatisfiability, and enlarged-vocabulary entailment from `T_phi` to `phi`.

The list/set distinction is exact. Preorder fixes the gate order, the row order fixes emissions, and the root is appended last. Duplicate clause emissions remain in the list, while individual clauses are sets. The inherited literal code and right-associated conjunction make the resulting formula string determinate once the fresh-variable choices have been made. Because satisfaction ignores repetition, the proof transfers from the emitted list to its underlying set correctly. There is always at least one emitted clause, so the empty-conjunction convention causes no hidden case here.

The worked input `((P and Q) -> not P)` has three labelled nonvariable occurrences and emits `3 + 3 + 2 + 1 = 9` clauses. With `(P,Q)=(F,T)`, the labels `(z_1,z_2,z_epsilon)` have values `(F,T,T)`; with `(T,T)`, they have `(T,F,F)`. Both calculations at body 149–170 are correct.

The body supplies valid counterexamples to the possible overstatements. For `phi=bottom`, the unrooted definitions have the model `z_epsilon=F`, whereas the rooted output contains the contradictory units and has none (174–180). For `phi=not P`, assigning both `P` and its fresh root `F` makes the input true and the output false (182–187). This also supplies a total countervaluation by arbitrary extension outside these two variables. The manuscript therefore correctly declines general logical equivalence.

### Every size claim

For `n_0` bottom occurrences, `n_1` negations and `n_2` binary occurrences, the pre-deduplication counts are `n_0 + 2 n_1 + 3 n_2 + 1` clauses and `n_0 + 4 n_1 + 7 n_2 + 1` literal slots. Since `M=n_0+n_1+n_2`, the bounds `3M+1` and `7M+1` follow. Every clause has width at most three. Parentheses, polarity and connectives add bounded token cost per literal or clause, so the stated token bound holds. Deduplication can only lower these counts (annex 112–129).

The linear emission claim explicitly assumes a parsed tree, supplied fresh names, stored child references and unit-cost name comparisons (body 131–133; annex 131–136). Under those assumptions a preorder traversal and bounded-width sorting have linear operation count. The text makes no unconditional linear bit-time claim.

Writing `d=|V|`, the inequality `d <= N-M` ensures at least `N-d >= M` unused symbols among `p_0,...,p_(N-1)`. Hence the deterministic first-unused policy really can give every auxiliary index a value below `N`, including the cases `M=0` and `d=0` (annex 138–144). No scan to the largest original index is required.

Each original variable leaf contributes at most two literal copies in its parent block, or one root literal for an atomic input. Its potentially long binary name therefore contributes only a constant multiple of its original input length. Auxiliary occurrences number `O(N)` and use `O(log(N+1))` bits each. This proves `O(L + N log(N+1))` output length. Candidate scanning, parsing, constant-width sorting and output writing are polynomial in `L`, since the primitive occurrence count is bounded by the encoded input length up to a fixed coding constant (annex 146–165). The stipulated expansion and tree convention correctly includes repeated subformulas and does not measure a compressed abbreviation or a shared DAG.

### Proof and reference routes

The active P2 driver places the body at line 10 immediately after the normal-form restoration wrapper; the latter links to the new section and theorem at 210–212. The P2 annex includes the new proof file at line 13. The two body statuses point to `annex:p2.prop.tseitin` and `annex:p2.prop.tseitin-size`, and the two complete annex items point back to the corresponding body labels. The existing Part 12 three-clause conjunction example and root assertion match the bounded comparison made by this body.

## ACF mathematical findings and dependency boundary

The active categoricity definition at restoration 4–8 requires both existence and isomorphism uniqueness. The new theorem at 177–184 supplies both. It fixes characteristic zero or a prime and states ambient Choice before quantifying over uncountable cardinals. These are sufficient hypotheses for the use of transcendence bases, algebraic closures and infinite cardinal arithmetic.

The terms prime field, transcendence basis and absolute transcendence degree are introduced at 186–191 before the classification argument. For a prime field `F` and an uncountable basis `B`, the rational-function field `F(B)` has cardinality `|B|`: its elements involve only finitely many basis elements, and `B` supplies the lower bound. An algebraic extension of an infinite field has at most the same cardinality, because its elements are roots of the field's nonzero polynomials and each such polynomial has finitely many roots. Under Choice the counting steps therefore give the required equality, including singular uncountable cardinals.

Consequently, any algebraically closed field of uncountable size `kappa` has absolute transcendence degree `kappa`. Two fields of the fixed characteristic and cardinality have isomorphic prime fields and bases in bijection. Algebraic independence makes the induced rational-function-field map well defined; uniqueness of algebraic closures extends it to an isomorphism of the given algebraically closed fields. This validates the application at 195–202, conditional on the cited field theorems. Starting instead with `kappa` independent indeterminates and taking an algebraic closure gives a model of the required size, validating 204–207 and excluding vacuous categoricity.

For a finite or countably infinite basis, the rational-function field is at most countable. Its algebraic closure is at most countable by the polynomial argument and is infinite: a finite field cannot be algebraically closed, since the polynomial obtained by multiplying `(X-a)` over all its elements and subtracting one has no root. In characteristic zero the prime field is already infinite; in positive prime characteristic this argument supplies infinitude. Thus the closures of the prime field and of its one-indeterminate extension are both countably infinite and have absolute transcendence degrees zero and one, respectively. Degree is invariant under field isomorphism. These are correct nonisomorphic countable models for every allowed characteristic, proving the qualification at 208–214.

The theorem is explicitly `cited=Steinitz1910`; its surrounding application expressly reserves classification, field existence and closure theorems as cited dependencies at 215–218. The active style's result and status code preserves that distinction, and the bibliography contains the cited record. This local treatment does not claim to reproduce the proof of Steinitz's classification, the existence of transcendence bases, or the algebraic-closure theorem. It also does not use the earlier ACF quantifier-elimination theorem to smuggle in the classification. The ambient Choice hypothesis is sufficient; no minimal-choice-strength claim is made.

## Primary-source extent and limits

The reviewer independently opened the author-hosted [Harrison lecture PDF](https://www.cl.cam.ac.uk/~jrh13/slides/marktoberdorf-30jul03/slides1.pdf) through the web reader. The returned PDF has 19 physical pages; its text identifies John Harrison, the lecture title and 30 July 2003 on physical page 1. Printed slide 12, physical page 13, displays biconditional definitions and the asserted final variable. Printed slides 11 and 13 supply the nearby normal-form and clause-set context. This supports the body's narrow attribution. The reviewer did not inspect source page images, reproduce the original Tseitin paper, or identify Harrison's displayed construction with the manuscript's complete occurrence-level algorithm.

The reviewer independently read the complete primary OCR response for [Steinitz printed page 301, section 23(6) and section 24](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000305?_format=xml). Its identifiable statements give the unique algebraically closed type in a characteristic/degree class, the cardinality argument with explicit well-ordering, and equality of uncountable cardinality with absolute transcendence degree. The OCR has damaged mathematical glyphs; no source image verification is claimed.

Independent live reads of the cited pages 287, 289 and 300 failed in this review context: the web reader returned URL-access failures, and direct requests first encountered the network sandbox and then a TLS security-package failure after network permission was granted. The author note's page-specific claims are therefore not presented here as independently read passages. Exact verification of those additional source locators remains UNRESOLVED in this report and belongs to the separate source-fidelity evidence. The mathematical application above is checked with the named closure, existence and classification results as cited premises; it is not a substitute for source acquisition or source-fidelity acceptance.

## Completion record

The reviewer checked the specified primitive cases, finite domains, empty-domain and atomic cases, uniqueness, root assertion, clause-list/formula relationship, all announced size bounds, the worked assignments, and both failure examples. The ACF review checked characteristic, Choice, existence, isomorphism and the countable countermodels. A concrete checkpoint was sent to the lead during the bounded work block. The assigned files and DLO substring matched their frozen identities; no target-text change was requested. No source, manuscript, code, registry or provenance record was edited, and no software tests, builds or renders were run. Only this owned review report was added.
