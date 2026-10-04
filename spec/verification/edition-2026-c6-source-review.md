# C6 / R-002: independent source and compatibility review

Date: 7 September 2026. Reviewer task: `/root/c6_source_review`.

**Verdict: PASS for the assigned C6 source-preservation and local-compatibility scope.** The supplied serialization and E/E2/H1–H4/Comp construction preserve the inherited machine, tuple, input/output, and standard-model hierarchy roles. I found no omitted substantive component or qualification in the two assigned archival extents. The formerly unspecified serialization and literal formulas are presented as this handbook's construction. The surviving external-source, mathematical-specialist, publication, provenance, and admission gates receive no acceptance from this report.

The four ordinary theorems remain in their original order. Their later hierarchy citations and the separate P5 internal-arithmetic obligations retain their stated boundaries. Detailed component verdicts and the limits of this conclusion follow.

## Snapshot, independence, and review method

Root: `C:/Dev/the-methods-of-reason`. The live branch read was `phase4-codex`, with HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. HEAD identifies the checkout; the current file hashes below identify the reviewed text. The two target hashes matched the requested freeze when first checked and when checked again before filing. The frozen source comparison artifact likewise had the same hash at those checks.

This reviewer read the actual complete LaTeX targets, the complete four named P4 dependency fragments, the P5 boundary fragments listed below, and the designated archival source extents. No other C6 review was read and no findings were exchanged before filing. This task did not author the manuscript changes. The author preparation note supplied file-location leads; its verdicts and descriptions were not treated as acceptance evidence. Initial search matches from the other author notes were also locating material only.

The checks were textual and mathematical reading of the supplied arguments, together with read-only hash and line comparisons. No manuscript build, render, software test, external acquisition, source edit, registry edit, or provenance edit formed part of this review. The only authored repository artifact is this report. File-specific write permission was obtained for it. Git initially rejected the sandbox account's ownership; the branch and HEAD reads succeeded using a command-local `safe.directory` setting, without changing Git configuration.

The available reviewer metadata identify an independent Codex task context, not a named human expert or separately verified model/version. This report cannot certify human review, reviewer credentials, model diversity among the three seats, or the provenance of other reviewers.

## Exact reading and hashes

All line extents are one-based physical file lines, including blank lines. Paths in the following ledger are relative to the root stated above. Hashes cover the whole file even where the read extent is partial.

| File | Actual read extent | SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1–168, complete | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-c6-review-freeze.md` | 1–85, complete | `04E1075E9EF200726F36C781C463380F7701B82C7C5FB8FB1DFE1E7F656D4732` |
| `handbook/restoration/inherited-07851-08048.tex` | 1–261, complete; **numbering** below | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| `handbook/restoration/inherited-08710-08876.tex` | 1–1104, complete; **history** below | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |
| `handbook/restoration/inherited-07506-07677.tex` | 1–172, complete; **machine** below | `EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D` |
| `handbook/restoration/inherited-07753-07843.tex` | 1–91, complete; **c.e. dependency** below | `E2B7284BEABCA82F440BB921D779243F1615F8D7077ABA73DFF6CBDE28458B00` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–133, complete; **syntax** below | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–271, complete; **pairing/prefix** below | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |
| `source/formal-logic-reference.tex` | 7851–8048 and 8710–8876, both complete designated archival extents | `0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC` |
| `handbook/restoration/inherited-09262-09327.tex` | 1–66, complete | `75A27E87080116A235A904DAEDABE2A70DFF472BA27CA8A454C448DFD4B58BB6` |
| `handbook/restoration/inherited-09328-09438.tex` | 1–111, complete | `F5A14F098311611F5942A7E0F9F5B348B52C1AADFCA2E1FF129E5F63A977F6A0` |
| `handbook/restoration/inherited-09750-09816.tex` | 1–67, complete | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` |
| `handbook/parts/p04.tex` | 1–84, complete | `19C6CB01DE3F19F24430EDBFE623F466C55DDEA50AF006864B6B1B8EC964A509` |
| `handbook/parts/p05.tex` | 1–52, complete | `068B90E56BFCF4538AFF14F0DBBF428A228A34B12736CA55484B1E3D5E64B326` |
| `handbook/restoration/scope-SRC-07851-08048.tex` | 1–3, complete | `7FD00B6A8140B749C94538B9055F2E6F4CDB82FCFB4647AA863AB8DEB38AA61B` |
| `handbook/restoration/scope-SRC-08710-08876.tex` | 1–3, complete | `874744040E6B3C1A1FEE5C71ECA68548315678D9FDAC856A561FDAA813C91462` |
| `spec/research/edition-2026-c6-arithmetic-preparation.md` | 16–28 and 182–198, plus initial search matches; locating leads only | `4AFF64BB834FCEB5425AF53F08D811EE41C6EFA59C63931F42798C884BE5DA42` |

The complete source file has 17,206 physical lines; this review does not claim to have read the rest of it. The other three development notes named in the freeze were not read in full, and no claim in this report relies on their acceptance of any formula or proof. A small memory lookup supplied prior review discipline only; all manuscript facts reported here were checked from the current files.

## Component verdicts

| Component | Verdict | Concrete source and compatibility basis |
| --- | --- | --- |
| Designated machine roles and exact serialization | PASS | Numbering 7–80 supplies state and tape counts, width-limited input bitmap, five-field row code, full lexicographic row order, and length-prefixed right-nested tuple. These respect machine 4–79 and the archival normalization at source 7857–7882. |
| Tuple application, invalid indices, and raw program semantics | PASS | Numbering 82–109 preserves the everywhere-divergent meaning of invalid indices, valid-output restriction, wrapper interface, and fixed-arity application convention from source 7871–7897. Machine 81–147 supplies canonical binary words, tuple coding, output semantics, and computable decoding. |
| E/E2 extraction and simultaneous finite packing | PASS | History 1–74 explicitly bounds paired indices by arithmetic terms, preserves unique beta values bounded by the history code, fixes positional arity per tag, and packs consistent finite assignments through pairing/prefix 37–83. |
| Fourteen-tag layout and H1 input | PASS | History 76–158 and 160–214/323–377 preserve clause (h1), with the required canonical-zero and positive-first-bit conditions. Every stored family and header role is specified. |
| H2 exact metadata and full ordered table | PASS | History 216–320/379–531 certifies the exact outer code and tuple tail convention, all bitmap conditions, and every nonhalting key exactly once. The raw program identity is retained. |
| H3 configurations and transitions | PASS | History 533–618/678–776 checks initial placement, both head moves, scanned-cell writing, and preservation of every other tape cell. The finite-window extension matches the full two-sided tape model. |
| H4 output, explicit Comp, and both computation directions | PASS | History 620–915 implements the original accepting-state and first-blank canonical-output rule, conjoins H1–H4 literally, and supplies finite packing and decoding directions with explicit bounds. |
| c.e./Sigma-1 and decidable/Delta-1 content | PASS | History 958–1045 preserves the two inherited set characterizations and their standard-model role, and supplies the domain-to-index argument, bounded evaluator, exhaustive witness search, and complement argument. |
| Theorem identities/order, retained qualifications, and attribution | PASS | Ordinary theorem openings are at history 805, 958, 1059, and 1080. The driver hooks at p04 56–66 still attach to the third/fourth theorems. The retained hierarchy suffix and numbering's universal/parameter text agree line-for-line with the corresponding archival passages. |
| P5 compatibility and absence of internal-arithmetic upgrade | PASS | History 909–915 expressly preserves the standard-model boundary. The active P5 representation, syntax, and derivability fragments continue to require their separate numeralwise and internal arguments. |
| External primary-source proof acceptance, independent topic/publication review, and production/admission | UNRESOLVED by this seat | No external cited book/paper body, candidate notation artifact, build, rendered page, formal admission record, or other review was evaluated here. The PASS above is confined to the specified local text and source comparison. |

## Evidence and reasoning

### 1. New serialization preserves the inherited numbering contract

The archive already designated blank/digit symbols as 0/1/2 and start/accept/reject states as 0/1/2, required a full lexicographically ordered table, permitted noncanonical renamings of other states/symbols, and used a length-prefixed tuple. It did not specify all metadata fields or the exact row serialization (source 7857–7882). Numbering 22–63 supplies these missing choices explicitly: `n,b,A`, followed by `(n-2)b` rows, with each row a right-nested five-tuple and direction bit 0/1. The index remains `pair_N(k,code_k(...))`, with `k=3+(n-2)b`.

Numbering 65–80 gives finite decoding and checks the actual metadata, including the bitmap's high-bit exclusion, rather than treating a row list alone as a complete machine. The one-entry tail remains its entry, with no zero terminator; descriptions shorter than six entries are invalid. The unrestricted numerical tuple convention at machine 92–109 therefore survives. Input arity is fixed by the type, while the program-description tuple stores its length; these are different uses of the same tuple machinery.

The normalization exception for machines whose start state is already halting remains explicit at numbering 91–94 and 181–189. Its surrogate start step preserves the output tape and is compatible with the output rule that ignores the final head position. Numbering 168–209 retains the enumeration argument and supplies the metadata in its final encoding step. Kleene remains parallel reading for this bespoke numbering (212–216), and the separate universal-computation sketch and parameter theorem retain their original statuses at 218–261. Direct textual comparison found numbering 218–261 identical, line for line, to source 8004–8047.

The output-cleaning wrapper at numbering 98–101 establishes partial-computable behavior for the indexed function. H2 expressly verifies the exact raw table at history 315–320; it does not silently replace that table with the wrapper. This distinction is needed because Comp must refer to the indexed program's actual accepting run.

### 2. Extraction, bounds, and the complete input/table contract

E and E2 use the exact pairing graph and beta relation already defined in pairing/prefix 1–83. Their fresh-variable convention is explicit at history 14–16. The proof at 42–58 covers zero arguments and establishes the strict square bounds for each paired index. The finite-packing proof separates tag families, fixes one positional arity per tag, and constructs the finite flattened index assignment before choosing its beta code (60–73). This avoids treating an index as a stored value bounded by `s`.

The final history summary at 152–157 correctly distinguishes stored values, row projections, paired indices, and derived witnesses. It replaces the archive's broader auxiliary-value sentence at source 8741–8743 with the qualifications actually needed by the supplied construction. The edit is an authorized correction/completion under the governing contract; the active text should consequently not be described as unchanged archival transcription.

The local syntax definition distinguishes marked bounded quantifiers from the unbounded expansion of a bare comparison (syntax 28–59). History 168–180 supplies bounded Lt and Le for comparisons inside matrices. The displayed H1/H2 formulas and their helper expansions use that convention, arithmetic-term bounds, fresh variable renaming, and the previously bounded E/E2/P/B formulas. Exponentiation, arrays, and tuple construction remain metatheoretic descriptions, with explicit relational formulas where the arithmetic syntax needs them.

H1's zero case forces precisely the one-digit word 0, while positive inputs require first digit 1 (history 204–212). The recurrence and quotient/remainder argument then recover the canonical binary word; prefix bounds alone would not suffice. The proof treats the one-digit and empty-successor-loop cases. The worked failure word `(0,1)` at 950–953 demonstrates the missing property that the first-bit condition supplies.

H2 fixes `n=nu+2`, positive `nu`, `b>=3`, `m=nu*b`, and `k=3+m`, matches the outer pairing to `e`, and ties the same header values to the first three description fields (295–312). The decoding chain ends with equality of the final tuple entry and tail. Bitmap M fixes the terminal tail at zero and the blank/digit membership bits at 0/1/1. Table K ranges over each `(u,a)` with `u<nu`, `a<b`, and selects row `u*b+a`; its source states are exactly `0,3,...,n-1`. History 459–475 proves coverage, unique row position, field ranges, and absence of extra rows. R5 alone is explicitly given no table-membership meaning (234–240), and later transitions impose `i<m`.

### 3. Full tape behavior and output agree with the inherited machine

The fourteen-tag layout fixes the meaning and ranges of all input, metadata, configuration, and output families (history 83–117). Cfg records every cell in a width-specified tape row and the complete base-`b` expansion, allowing leading blank/zero tape symbols. Init translates numerical bits 0/1 into tape-symbol numbers 1/2 and blanks all other window cells (540–571).

Step selects an actual row with `i<m`, matches the current state and scanned symbol, forbids halting source states, applies `h=Sh'` for a left move or `h'=Sh` for a right move, writes the selected symbol at the old head, and preserves every other window cell (577–594). The proof at 729–760 extends each stored tape by blanks outside the fixed window. Since the scanned cell and both heads are inside, it establishes exactly the full transition relation of machine 44–63, including all outside cells.

The converse construction chooses origin `H=T` and width `W=L+2T+1`, bounds the physical head between `-t` and `t`, and shows that the rightmost represented physical cell `L+T` remains blank (history 837–875). This places the first nonnegative blank after the output within the window. The construction then assigns all actual run data before invoking finite packing. The auxiliary lengths and row projections receive explicit witness bounds at 889–896. The case `T=0` is discussed at 901–906: H3 permits the initial segment, while H4 fails because normalized start and accepting states differ.

H4 requires acceptance, a nonempty canonical binary output prefix at physical cell 0, its first following blank, and exact value/prefix certificates (642–659). It adds no output restriction on the final head, negative cells, or cells beyond that blank (662–664 and 801–802). This matches machine 111–123, including the valid single-digit zero output and the invalid empty output, malformed symbols, and leading-zero words. The theorem at history 805–907 consequently preserves both inherited claims at source 8746–8763: exact history recognition and existence of a history iff the indexed function is defined.

### 4. Hierarchy claims retain their exact logical standing

The c.e. definition is a domain definition (c.e. dependency 9–12). The forward proof at history 967–980 uses that definition, the in-document enumeration theorem, and the new Comp construction. It does not assume the c.e./Sigma-1 theorem as a premise for Comp.

The reverse direction supplies a terminating evaluator for each fixed bounded formula, including bottom, Boolean operations, both marked bounded quantifiers, and the false/true answers for empty existential/universal ranges (982–1014). It describes realization on the fixed single-tape machine model and writes the required canonical numerical answer. Prefix normal form is invoked with its standard-structure satisfaction scope, after which finite stage-by-stage tuple search yields a domain machine (1016–1033). The argument includes the empty set and adds a vacuous existential if needed.

The Delta-1 conclusion uses complement duality and the earlier decidability characterization (1035–1044). That dependency's proof is explicitly printed at c.e. dependency 78–90; the separate four-way equivalence at 56–76 retains its proof-sketch status. This source review confirms compatibility with the dependency as supplied and does not promote that entire four-way equivalence to a complete newly reviewed result. The syntactic/boldface distinction from syntax 96–123 remains intact throughout.

The four theorem statements are, in order: bounded verification; the c.e./Sigma-1 and decidable/Delta-1 theorem; hierarchy classifications of domains and totality; hierarchy strictness. Added helpers use definition and lemma environments, preserving the theorem-count hooks at p04 56–66. Direct comparison found history 1047–1104 identical, line for line, to source 8818–8875. The many-one completeness qualification, prefix-form transfer qualifications, cited statuses, and warning about upper bounds therefore survive intact.

### 5. Attribution and P5 boundary

History 909–915 attributes the literal numerical serialization and tagged layout to the handbook, points to Shoenfield and Boolos–Burgess–Jeffrey for other coding constructions, and explicitly identifies the proved result as truth equivalence in the standard structure. The new text does not claim those authors supplied these exact formulas or import a generic T-predicate as a proof of this Comp. Pairing/prefix 71–82 retains the Chinese remainder theorem as an explicit mathematical dependency for beta packing.

P5 distinguishes numeralwise representation from a universally quantified decision assertion at inherited-09262-09327 4–17 and keeps the representability theorem cited at 31–48. Its syntax-arithmetization theorem remains a sketch at inherited-09328-09438 46–63. Its proof predicate at 65–84 is a separately chosen primitive recursive relation and a chosen representing formula. The common beta apparatus described there is compatible with reusing extraction/coding machinery; it does not identify the program serialization and the syntax/proof numbering as the same numerical map.

Inherited-09750-09816 7–47 continues to distinguish the metatheoretic first derivability condition from the internal second and third schemes, citing separate proof-concatenation and verification arguments for PA. Nothing in C6 supplies or upgrades those internal claims. Their acceptance remains a separate obligation.

## Remaining evidence limits and disposition

There is no required source-compatibility repair identified within this frozen C6 assignment. The reader receives the previously promised serialization, literal history checks, and both computation directions, while the archival mathematical roles and qualifications survive.

The source comparison is against the actual frozen local artifact and the stated local dependencies. External books and papers cited for alternate coding methods, CRT background, universal computation, the parameter theorem, later hierarchy completeness/strictness, and P5 representation/internal proof operations were not acquired or independently verified in this seat. Their existing citations are not new evidence of full source acquisition or full-proof admission.

The active restoration files contain authorized additions/corrections. Historic wrapper or driver comments about exact inherited transcription do not establish correction provenance or waive the amendment's admission requirements. The frozen source hash remained unchanged across this review's checks; a whole archival-provenance audit was outside the read extent.

Candidate symbol tables/indexes and the canonical symbol registry were not inspected here. No claim about their acceptance, rendered notation, page layout, compilation, source-rights clearance, final register closure, formal admission, board consensus, or user acceptance follows from this report. A content or dependency change affecting this scope requires a new review against its new hashes.
