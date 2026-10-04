# P16/P17: independent production preservation review

## Retrieved Content

### Source 1: `source/formal-logic-reference.tex`, line 101

```tex
\newcommand{\B}{\mathbb{B}}
```

### Source 2: `handbook/handbook.sty`, lines 1388–1399

```tex
\newenvironment{inheritedrestorationscope}[1]{%
  \ifhb@inheritedrestoration
    \PackageError{handbook}{nested inherited restoration scope}%
      {Inherited restoration scopes must be balanced and non-nested.}%
  \else
    \def\hb@restorationprovenance{#1}%
    \ifx\hb@restorationprovenance\hb@empty
      \PackageError{handbook}{inherited restoration scope has an empty
        provenance id}%
        {Supply the exact spec/provenance record identifier.}%
    \fi
    \hb@inheritedrestorationtrue
```

### Source 3: `handbook/handbook.sty`, lines 1554–1556

```tex
    % LaTeX's global \B accent is untouched.  Only this environment group
    % receives the frozen source's exact Boolean-domain abbreviation.
    \def\B{\mathbb{B}}%
```

### Source 4: `handbook/parts/p16/finite-abduction.tex`, lines 50–55

```tex
\begin{hbdefinition}{def:p16-abduction-models}{Finite valuations and explanatory entailment}
Use the truth values \(\mathbb{B}=\{\mathbf{F},\mathbf{T}\}\) and the recursive
truth clauses of \cref{sec:prop-syntax-semantics-02}. Put
\[
 \mathsf{Val}(V)\defeq\{v:v\text{ is a function }V\to\mathbb{B}\}.
\]
```

### Source 5: `handbook/annex/p16/finite-abduction.tex`, lines 238–244

```tex
\paragraph{Consistency constraint.}
The four candidates for \(\mathcal P_{\rm constraint}\) are
\[
 \varnothing,\{a\},\{b\},\{a,b\}.
\]
The candidate
\(\{a\}\) is consistent: choose \(a,m\) true and \(b\) false.
```

### Source 6: `handbook/parts/p16/finite-abduction.tex`, lines 168–170

```tex
This is the source's single-deletion characterization
\cite[prop.~2.1, p.~11]{EiterGottlobAbductionManuscript}.
It also holds for the extended input convention used here.
```

### Source 7: `handbook/bib/handbook.bib`, lines 6598–6606

```bibtex
@unpublished{EiterGottlobAbductionManuscript,
  author  = {Eiter, Thomas and Gottlob, Georg},
  title   = {The Complexity of Logic-Based Abduction},
  note    = {Undated manuscript, with an unnumbered title page followed by
             pages 1--45; TU Wien institutional copy. The local pagination
             is distinct from the 1995 Journal of the ACM publication},
  url     = {https://dbai.tuwien.ac.at/staff/pichler/complexity/eiter1995.pdf},
  urldate = {2026-09-07},
}
```

### Source 8: `handbook/parts/p16.tex`, lines 1–7, complete

```tex
% P16: explanation, abduction and causation, developed in bounded units.
\hbpartidentity{p16}
\part{Explanation, Abduction and Causation}\label{part:p16}
\begingroup
\emergencystretch=1.5em
\input{parts/p16/finite-abduction}
\endgroup
```

### Source 9: `handbook/annex/p16.tex`, lines 1–6, complete

```tex
% Proof annex for the supplied finite logical-abduction foundation.
\hbannexchapter{16}{Explanation, Abduction and Causation}\label{annex:p16}
\begingroup
\emergencystretch=1.5em
\input{annex/p16/finite-abduction}
\endgroup
```

---

## Supplementary Notes

**Verdict: PASS for preservation of the accepted P16/P17 content through the specified local production edits.** Reversing only the stated edits, in memory, recovers every changed body's or annex's accepted whole-file SHA-256 exactly. The P17 body is byte-identical to its accepted snapshot. The P16 driver inverses also recover their previously recorded whole-file hashes, and both P17 drivers retain their recorded hashes. No additional mathematical, empirical, example, hypothesis, qualification, citation-target or proof-step change is hidden among these local edits.

Review conducted on 8 September 2026 UTC, 7 September Pacific time, by the independent `p16_p17_production_preservation` context. Checkout: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. HEAD identifies the checkout; the hash-pinned acceptance records supply the comparison baseline. The checkout contains substantial existing work. This review creates only this report.

### Exact content identities and read extents

All four current bodies and annexes were read completely, including every definition, theorem, proof, example, citation and closing scope statement. Extents below count physical source lines. Files use UTF-8 without a byte-order mark and LF line endings; inverse hashing preserved the final newline and all bytes outside the named substitutions.

| File | Accepted extent / bytes | Accepted SHA-256 | Current extent / bytes | Current SHA-256 | Independent comparison |
| --- | --- | --- | --- | --- | --- |
| `handbook/parts/p16/finite-abduction.tex` | 1–340 / 15,993 | `19E88AF8C80B63A7125FE61B3FE9CE192564CA02456A61020570AD4C6B7B9BC9` | 1–342 / 16,024 | `0F7D93E64D6EAB11CD2904C509DB168621ADB93D9D5A9AE3F448D62BF7E1C6B6` | PASS: exact inverse |
| `handbook/annex/p16/finite-abduction.tex` | 1–283 / 15,238 | `9965EE04CE9F0D7F9A6CC786CEE9355BC0E7B1403803A61AF745087C1C06D893` | 1–286 / 15,280 | `D027F796A1A887DD7217C412DDF95FAC42F69A34CCE4F1DCFECB224C76E1A4B4` | PASS: exact inverse |
| `handbook/parts/p17/finite-preferences.tex` | 1–330 / 13,925 | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` | 1–330 / 13,925 | `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C` | PASS: unchanged bytes |
| `handbook/annex/p17/finite-preferences.tex` | 1–324 / 16,662 | `DFA00CC716098DA6BF6076FEF0258A4180DD868358561AC56E12CF96B925D9DF` | 1–324 / 16,672 | `B141A371731E7A0A3BEFF1C88C839F98720BE4F894A2D475CAF098A61159202C` | PASS: exact inverse |

The accepted hashes and line extents come from `spec/verification/edition-2026-pa-abduction-text-acceptance.md:8–15` and `spec/verification/edition-2026-kamp-l2-preferences-text-acceptance.md:7–14`. Prior byte counts were independently computed from the exact recovered UTF-8 strings. Both acceptance records were read completely, 85 and 81 lines respectively. They remain bounded source/text acceptances with their existing content and admission limits.

### Exact inverse operations and their meaning

The following are the complete inverse operations. They were applied to freshly read current strings without writing reconstructed manuscript files. Matching whole-file hashes establish that these operations account for every changed byte in the scoped content files.

| Current file and locations | In-memory inverse | Result and content check |
| --- | --- | --- |
| P16 body, lines 51 and 54 | Replace exactly two literal `\mathbb{B}` occurrences by `\B`. | PASS. Frozen source line 101 and actual style line 1556 give exactly `\mathbb{B}` as the Boolean-domain expansion. |
| P16 body, lines 107 and 147 | Remove exactly two complete `\par\nobreak` lines, including their LF terminators. | PASS. The preceding environment declarations at lines 106 and 146 retain their complete titles, IDs and theorem proof target. No statement words change. |
| P16 body, line 169 | Replace `prop.~2.1, p.~11` by `prop.~2.1, manuscript p.~11` once. | PASS. The citation command, key, proposition number and page number are identical; only the redundant manifestation word was removed. |
| P16 annex, lines 14, 15 and 67 | Replace exactly three literal `\mathbb{B}` occurrences by `\B`. | PASS. Both valuation codomains and the empty-function codomain use the same Boolean domain. |
| P16 annex, lines 13, 73 and 186 | Replace `\textbf{Agreement with the book's semantics.}\enspace`, `\textbf{Qualified monotonicity.}\enspace`, and `\textbf{Inconsistent background.}\enspace` by their respective `\paragraph{...}` forms, retaining each complete argument literally. | PASS. The words, apostrophe, capitalization and periods match exactly. Each changed command occurs immediately after `\begin{proof}`. |
| P16 annex, lines 240–243 | Replace the display block and following `The candidate` line by `\(\varnothing,\{a\},\{b\},\{a,b\}\). The candidate`. | PASS. All four sets, their order and the following period are preserved. The existing line 244 follows unchanged. This exact inverse reduces the extent by three lines and recovers the accepted hash. |
| P17 annex, lines 14 and 69 | Replace `\textbf{Relations on alternatives.}\enspace` and `\textbf{Necessity.}\enspace` by their respective `\paragraph{...}` forms, retaining each complete argument literally. | PASS. Both complete headings and all subsequent proof text are preserved. |

Here `\paragraph{...}` in the inverse-operation descriptions denotes the complete same literal heading argument just given; it is notation describing an operation, not a shortened quotation of the source. No replacement was made to later paragraph headings: P16 annex lines 54, 80, 103, 193, 202, 210, 238 and 255, and P17 annex lines 35, 47, 77, 89, 123 and 171 remain their accepted commands and words. No heading removed here contains a label or citation.

The Boolean check concerns the source's intended Boolean-domain abbreviation. It does not assert that the accepted editorial bytes had previously rendered successfully: the restoration-local Boolean meaning is the one established by the source and style. The actual style preserves guarded source environments and aliases. The `definition` guard was read at style lines 510–524; guarded `Prop`, `CPL`, `Sub`, `True` and `False` definitions at lines 824–858; scope activation at 1388–1399, exact local meanings at 1516–1566, and balanced shutdown at 1574–1600 were inspected. The production content now uses the literal expansion, and neither driver establishes an inherited restoration scope around editorial P16 content.

### Driver preservation and local spacing scope

All four maintained drivers were read completely. The exact inverse for each P16 driver removes the consecutive `\begingroup` and `\emergencystretch=1.5em` lines and its `\endgroup` line, including those LF terminators. This leaves its original input route and all original identity, title and label commands byte-for-byte. The recovered hashes match `spec/verification/edition-2026-editorial-alias-expansion-review.md:153–156`; those rows also record the unchanged P17 driver hashes.

| Driver | Prior extent / bytes and SHA-256 | Current extent / bytes and SHA-256 | Verdict |
| --- | --- | --- | --- |
| `handbook/parts/p16.tex` | 1–4 / 189; `B8462255C289FBCA14A9296EE8F7567C524A7ABFAC44FC5BB5F681AA3997C64E` | 1–7 / 235; `E6E476F0F0EAB035C28A3FCD964E0789C02250BE4D9E4B90DB8169F6558BEF8D` | PASS: exact inverse |
| `handbook/annex/p16.tex` | 1–3 / 178; `F60E8A47B426A42C69DFC8D903F308FA7654269A7E8CEFD95FF03B9B85D0883D` | 1–6 / 224; `42C1195029286D35850C346B06DB4705EB2595CB7308BA3553B03414E9D1A55E` | PASS: exact inverse |
| `handbook/parts/p17.tex` | 1–4 / 183; `94B1A39026E95CECE627D0025CA86D6FA1F799712235A32F410A114B92F0D3F2` | 1–4 / 183; `94B1A39026E95CECE627D0025CA86D6FA1F799712235A32F410A114B92F0D3F2` | PASS: unchanged |
| `handbook/annex/p17.tex` | 1–3 / 169; `CDFB2B0555402278C57DCBDCCD060D79BFEFA37186288DCEB73F503A92868F85` | 1–3 / 169; `CDFB2B0555402278C57DCBDCCD060D79BFEFA37186288DCEB73F503A92868F85` | PASS: unchanged |

The P16 body driver's part identity, part heading and part label precede the group; the P16 annex driver's annex chapter and label also precede its group. The inserted assignment has no global prefix, and the balanced group contains only that assignment and the respective input. It therefore supplies local paragraph-spacing latitude without changing a formula, source route, result status or proof target. The current style's identity and annex controls were inspected at lines 430–444 and 1698–1718.

The internal QA driver was read completely, lines 1–28. Its lines 13–17 similarly group the two actual P2 scope-wrapper inputs with `\emergencystretch=1.5em`; its P16/P17 and annex inputs remain at lines 20–24. This is an observation of the actual internal driver. No historical driver hash was supplied for an independent before/after comparison of that QA-only grouping.

### Dependencies and citation identities

Both P2 prerequisite artifacts were read completely: `inherited-01661-01816.tex:1–156` and `inherited-01817-01898.tex:1–82`. Their three-line scope wrappers were also read completely. The grammar and abbreviation target is `sec:prop-syntax-semantics-01` at the first fragment's line 2, with defined connectives at lines 48–58. The truth-clause target is `sec:prop-syntax-semantics-02` at the second fragment's line 2, with truth values and valuation at lines 4–27, `lem:prop-coincidence` at lines 29–40 and semantic consequence at lines 42–60. These are the actual dependencies used by the P16 body and its extension/restriction proof.

| Current dependency | SHA-256 | Actual inspection |
| --- | --- | --- |
| `handbook/handbook.sty` | `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44` | Relevant source definitions, guards, scope and driver controls as specified above; full-file hash |
| `source/formal-logic-reference.tex` | `0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC` | Lines 96–104; full-file hash |
| `handbook/restoration/inherited-01661-01816.tex` | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` | Complete 1–156 |
| `handbook/restoration/inherited-01817-01898.tex` | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` | Complete 1–82 |
| `handbook/restoration/scope-SRC-01661-01816.tex` | `DCE9A9D142AAAFF4DDD0E5746CB5B53609BCBC96D0A2E90752D18AD16378CFD4` | Complete 1–3 |
| `handbook/restoration/scope-SRC-01817-01898.tex` | `ABCC08C992478EBE863CA4C0E76D18BE4E7A719B69592AB195C168134249F683` | Complete 1–3 |
| `handbook/bib/handbook.bib` | `716394DAA6C90F1DD84DF53902A8E5A200E8D48870E45CE0382119E0AB32BD8B` | Complete two entries at 6598–6606 and 6608–6620; full-file hash |
| `tmp/pdfs/edition-2026-abduction-preferences/abduction-preferences-review.tex` | `D7967E49C17B8D26500FDAC91908C42903B99E6AED6954C80E068D870E5F2D27` | Complete 1–28 |

The two canonical bibliography entries were independently compared as literal strings with their original intake entries in `spec/research/edition-2026-p16-c1-finite-abduction.md` and `spec/research/edition-2026-p17-d1-finite-preferences.md`; each matches exactly, and each key occurs in exactly one entry. Entry-only UTF-8 hashes, including the closing brace's LF, are `178ABB84505C679D1779E781DC4811BD710301BBE5453DA20666D40B7582F401` for Eiter–Gottlob and `9651E4F7BC89D44E27472729F7CABA9B8425101773654BD9C99DADC13DCD5B41` for Rubinstein.

The retained Eiter–Gottlob source is `source/references/eiter-gottlob-abduction/eiter-gottlob-abduction-jacm-manuscript.pdf`, 419,030 bytes, freshly hashed as `E2A021C45BCDC6D2D1BC7AAC9972E75FEC697E3609094060CA92AFFCB694F265`. This equals the prior source identity. The bounded source review, `edition-2026-pa-abduction-source-review.md:88–109`, records Proposition 2.1 on printed page 11 / physical page 12 and the manuscript's distinct pagination. The current body retains the same source-specific key throughout; other citations still explicitly say manuscript, and the canonical entry itself supplies that manifestation. Removing the single word at body line 169 does not replace the source with the journal version or alter the locator.

The retained Rubinstein source is `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`, 1,431,428 bytes, freshly hashed as `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`. This equals the prior source identity. The unchanged canonical entry specifies the 2012 second edition and author-hosted revision dated 11 January 2015. `edition-2026-kamp-l2-preferences-source-review.md:64–79` records its selected printed/physical page mapping: 5–8 / 19–22, 12–14 / 26–28, and 30–31 / 44–45. All P17 citation text remains unchanged by the exact whole-file comparisons.

The primary PDFs were hashed only in this review. Their pages and the prior mathematical/source comparisons were not reread or rendered here. The prior review records supply their historical source-reading scope; their preservation to current source bytes is verified independently above.

### Evidence records and limits

`spec/research/edition-2026-p16-p17-production-repairs.md` was read completely, lines 1–39, SHA-256 `C0442B3C58B7EC85A72453E0E94C86E67CC8E0BB466BB8AB6061905EB41BE78B`. Every listed current content and maintained-driver hash matches the actual files. The original acceptance records have current hashes `7CCCEA9847FD11E44596536961BFDAA0B0C1ED536C0B06933571B0DB71008EE9` and `F89568AFB14D0F9D6A6941B468E09CFB73FEE176AF9E2EED2B4C4ADD058E81EE`, respectively.

The separate shared-style review, `spec/verification/edition-2026-editorial-reference-types-review.md`, was read completely, lines 1–330, SHA-256 `D54BE0952FEB0173CD9955E1C000C0A61906B44766C2C02145466D63331D59A8`. Its reviewed style hash equals the actual style hash above. Its PASS is evidence for that separate reference-kind correction; it supplies no proof that these local manuscript edits preserve content. The exact inverses in this report supply that local preservation evidence.

The root's `spec/verification/edition-2026-p16-p17-scoped-production.md` was read as the separate production record. The root reports the completed internal 45-page build and visual inspection there. This reviewer ran no build, test, rendering or manuscript-PDF inspection and makes no independent visual or historical build-failure reproduction claim.

There are no FAIL or UNRESOLVED findings within the specified local content-preservation comparison. The QA driver's historical byte delta and the root's build/visual results remain outside this review's independent before/after proof. The exact recovered accepted hashes permit the earlier bounded P16/P17 source/text findings to apply through the verified preservation mapping. This report grants no formal unit admission, whole-part completion, complete source coverage, final integrated-book readiness, or final editorial acceptance; those existing gates remain open.
