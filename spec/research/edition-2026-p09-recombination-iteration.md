# P9 finite-rule iterated splicing closure

Authoring record for the separately owned iteration packet. The first recombination/development packet and all shared drivers, canonical records, coverage, and queues remain frozen/unchanged.

## Source and reading

Exact allocated source: ED26-SRC-046-0007, Thomas Head, Gheorghe Paun, Dennis Pixton, *Language Theory and Molecular Genetics: Generative Mechanisms Suggested by DNA Recombination*, Handbook of Formal Languages 2, pp. 295-360, DOI 10.1007/978-3-662-07675-0_7. Held copy `source/references/p09-recombination-models/hfl-volume2-institutional.pdf`, SHA256 CF68AD2A00723DFFA55E8B7D2751B98070AADC240E6A49AE2F91BD49D40242BD. It explicitly identifies a softcover reprint of the hardcover first edition 1997, not an original first-impression copy. No reacquisition occurred.

Current exact proof scope is Lemma 3.14 and Remark 3.1, printed pp. 307-313 / physical pp. 323-329. All seven source-page images were rendered at 140 dpi into `source/references/p09-recombination-iteration/hfl2-iteration-source-323.png` through `-329.png` and read, alongside the OCR. These are source-reading evidence, not manuscript rendering or independent review. The following Lemma 3.15 begins on printed 313 and is not implicitly credited by reading the end of Lemma 3.14.

## Direct correction provenance from pixels

- Printed p. 310 explicitly sets `S_r($)=empty set` and says the corresponding prefix/suffix sets are empty. Literal language quotient by the empty set yields the empty set, contradicting the same paragraph's `L_$($,$)=L`. The neutral language must be `{epsilon}`. The active construction will use that explicit correction; the historical source is unchanged.
- The same page prints the double quotient as `P_r(s) backslash L_r / S_r(s)` in the definition of `L_r(s,t)`. Its subsequent cases and Fact 3.5 use the right-boundary t-index, so the active definition must instead use `S_r(t)`. This is not attributed as an exact unmodified formula.
- Printed p. 312's first ordinary-site trimming case omits the unchanged prefix x in the displayed resultant word although its later cases keep it. The active argument will retain the whole prefix.
- Printed p. 312 refers to `F_r($,t)` in the short terminal case, although the actual defined terminal set and preceding case are `F_r(t,$)`. The active proof will use the defined orientation.

The construction retains alpha_r, gamma_r, beta_r, J, N, E, F_r, S_r, P_r, L_r, and K as source-local typed roles. Published doubled round brackets and square brackets are retained; any editorial token aliases will be declared explicitly rather than misrepresented as the source's glyphs.

## Current mechanism and remaining work

The target is the actual finite-rule/full-AFL iteration theorem, not repeated one-step closure. The auxiliary history language J uses nests that erase their entire contents. It need not lie in the target family. Finite rule labels and bounded short fragments produce regular prefix/suffix sets; regular quotient and substitution build K in the family. The proof must establish both `E(J) subset K` and `K subset E(J)`, not merely define K or assume the desired saturation property.

The source's left/right dual cases will be supplied by an explicit word-reversal/rule-swap isomorphism. Its abbreviated two-sided embedding case will be expanded with trimming that preserves the opposite context. Whole 66+63-page duties and any remaining radius/multiset/source cases remain intact.

## Saved result

Saved reader 224 lines / 10,401 bytes, SHA256 `82B77D8F92C8810E59C17726C3A9BBC6E9CF6C59998BDA0C2D4DBFC9D60E8207`; annex 476 lines / 25,534 bytes, SHA256 `50578394EDC6435D343E3564DBB1A355D4D8CE329579093D7EEF0D4E156C3AEB`. The first packet is untouched. Placement is immediately after its iteration/supply subsection, or as a disjoint continuation under planned 127.6; root owns final routes.

Four complete reciprocal authoring proof pairs, with reader/annex start lines:

- `thm:p09-recombination-full-afl-iteration` / `annex:p09.recombination-full-afl-iteration`, 28/5. The proof supplies E(J)=ordinary closure, maximal-nest peeling/exchange, explicit reversal, bracket-adjacency promotion, bounded regular descriptors, visible-block birth/peeling trace for E(J) subset K, uniform right and left trimming preserving opposite contexts, full two-sided quotient witnesses, compatible-piece assembly for K subset E(J), and regular-substitution membership. It assumes only the three stated source closure properties, not arbitrary increasing unions or reversal closure of FA. Semantic finite occurrence tables are not mislabeled an effective discovery algorithm.
- `thm:p09-recombination-nest-domain` / `annex:p09.recombination-nest-domain`, 54/450. Full grammar and nonregularity argument for the source history domain, with the necessary nonempty-R qualification; R empty gives V*.
- `thm:p09-recombination-regular-iteration` / `annex:p09.recombination-regular-iteration`, 162/340. Regular quotient/substitution automata justify the specialization and H(REG,FIN)=REG.
- `thm:p09-recombination-radius-hierarchy` / `annex:p09.recombination-radius-hierarchy`, 178/363. Both directions of exact L_k generation, every short-site form with fixed 4k b-count parasitic outputs, and strict endpoints through the source's wrapper construction specialized to L=a+. This does not claim the complete general restricted-morphism lemma or Table 2 reconstruction.

Bibliography intake has one key, `HeadPaunPixton1997IterationIntake`, 13 lines / 943 bytes, SHA256 `3028F7A7A4277B169BC24A993B90378A4B4AAD9F1682A891B0CBC681FDF5A605`; root should deduplicate the same underlying chapter with the first packet's key. Symbol intake has 28 rows plus header, 29 lines / 5,770 bytes, SHA256 `F0A20DBE7D103A075970A612FB61AF3197D0CA7326160CCC121A23CD1B02D688`.

## Exact reading and still-open work

This block fully read text and pixels on printed pp. 307-313 and 315-319. Printed 314 was not read in this block. The beginning/end of the universal-machine lemma visible on 313/315 is not its complete proof. Table 2 and coding theorem 3.5 were read but are not fully reconstructed here. The consuming multiset transition on 319 is represented only as a precise semantics boundary, including two-copy availability and both complementary outputs; no regularity/completeness theorem is asserted for it. Unlimited multiplicity alone does not identify that two-output transition with an arbitrary oriented one-output set scheme.

The whole 129-page allocation stays partial. Still owed are complete uniterated/classification and universal-machine arguments, full general restricted-morphism separation, regular-language coding construction, multiset expressiveness and trajectories, simple/extended/circular/mixed H systems, computing-by-splicing and appendix; plant original residuals are unchanged. The active corrected source reconstruction is not an exact unmodified historical capture. Source admission, independent reviews, static/build/visual gates, and canonical routing remain open. No children, acquisition retries, dependency installations, tests, independent reviews, builds, or manuscript renders occurred.

Next useful source case: read the complete Lemma 3.15 on printed 313-315, including the currently unread 314, and prove the actual finite-axiom/regular-rule simulation plus terminal extraction in both directions. Alternatively the already read coding theorem 3.5 on 317-318 can be reconstructed separately; it changes the observed alphabet by coding and is not a contradiction of the radius separation.

Source-image identities below are reading evidence only (all in the owned source-evidence folder):

- iteration-323: `FC2E725737FFC5EF620982BED23E9EE12B1D796869B3D0D63F515FE0506E5458`
- iteration-324: `C3E6BF729C595AE0DF97D8654A6ACD1CD851A1C610C581C7A0E9902DBE65DE54`
- iteration-325: `C4E59AC0B066728B5885F6131618E92EB2E69458B7F702527AEF6B7AE9E349DA`
- iteration-326: `4226D8B5660A0C6E70B77A1CE935524677F132D92F6BCEED9281FF2178D56372`
- iteration-327: `1B2B52E9A8BF21C0EE6AF91D623CDA648CE90BB8646E4A5F47C9AC221FF69E56`
- iteration-328: `57DA5A77F04F0221CFCDE252416DF3BF64AABC8C7C270782EE4B860EDAF6E8EB`
- iteration-329: `6CDFAF18ACE5C096C717A8C1A2CA8F28FDB042D5E1B37A2E8C3649DA68927F74`
- radius-331: `EC35573BB7320C5819D352C95385C8F5425C5F72006DFF2C6C636741E4EFD0A2`
- radius-332: `53F6B5E3C1599E36012C63C79176D55577F4DC48C8B8F014451ADB69950E7085`
- radius-333: `0AB828FF5CF55FD31FC5FB4ECFAB72BFAD6758AC9034437F8D4533F16E647583`
- radius-334: `22CC9CC88139C5DA85DBDA20029E4D7FA7DD880EDE8D571888C271CC66D9DD52`
- radius-335: `9709AC60227E0F528C2761B98C32944ACDDC402094F89C6E7E01E1B6CF6ED89C`
