# Round 2 adversarial publication and terminology review

## Scope and method

I reviewed only the Round 2 charter, the seven hash-pinned Round 2 objects, and
the twenty-seven original-detail renders enumerated by the charter. I read all
six textual frozen objects completely. I did not use any Round 1 work, ledger,
chair transcript, other reviewer report, other board material, conversation
history, memory, staging or layout material, web result, automated checker,
repository script, TeX command, build, or handbook PDF.

The complete visual visit comprised the following original-detail images:

- core physical pages 001, 002, 012--014, 020--028, 031, 041, and 044; and
- relevant physical pages 088--097.

These are twenty-seven images in total. I treated the hash-pinned PDF as the
controlling object and the images only as the chartered page-reading aids. The
physical/printed relation was confirmed visually: after the added HAL cover,
physical page `n+1` is printed page `n` in the numbered body.

## Independently recomputed frozen identities

Native SHA-256 recomputation produced the following values. Every value agrees
exactly with the Round 2 charter.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | match |
| `spec/research/p09-tata-2008-source-note.md` | `5D31699B3219A9340435D41B0B8B74770EA405B70C3E58C1059CB95D09F434A9` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0E693D15418B828B650FC4A9F8310484B8121E806C45AEA07701311727DCB93F` | match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | match |

## Finding

### TATA-R2-AP-01 — must-fix — the unacquired Thatcher--Wright object is prematurely named and structurally reconstructed

**Manuscript locators.** The compact record first correctly says that only
metadata/abstract evidence was acquired and that the body-dependent algebraic
signature and recognition relation remain open
(`spec/research/p09-source-presentations-lot2-3.md:686-690`). It then reverses
that boundary in the very next paragraph:

- line 688 says that the abstract establishes a “finite-tree” presentation,
  although the bounded abstract description recorded in the acquisition note
  does not establish that input/domain claim;
- line 690 asserts that the source is about “finite-tree recognition”;
- line 692 instructs the future reconstruction to “Define the generalized
  automaton as a finite algebra over a ranked signature,” then prescribes a
  finite-tree/term coding and a “non-word ranked-algebra example”; and
- the consolidated entry at line 909 again treats
  “generalized-automaton definitions” as an already identified source object.

The detailed source note repeats the speculative name at
`spec/research/p09-tata-2008-source-note.md:192-194`. This is not merely a
stylistic difference among records. The controlling acquisition note says that
the registered body has not been acquired and prohibits reconstruction from an
abstract, a later textbook, or modern tree-automata notation
(`spec/research/p09-thatcher-wright-1968-acquisition-note.md:5-7`). It bounds the
available abstract evidence to finite algebras replacing conventional finite
automata, closure results, generalized Kleene regularity, and a positive
second-order decision problem; it expressly says that the exact algebra
signature, recognition map, weak-set coding, examples, and proofs are not
exposed (`:29-34`). Its source-neutral owed artifact is stated at `:74-80`, and
line 81 explicitly records that “[n]o hypothetical technical name is
introduced in advance of that evidence.” The reader itself obeys the boundary
at `handbook/parts/p09/presentations/n-c-015.tex:141-152`; the compact and
detailed records do not.

**Controlling printed-source locator.** TATA printed p. 95 (physical page 096),
Theorem 3.3.8, prints the historical citation `[TW68]` next to “WSkS is
decidable” and then gives TATA's own modern finite-tree-automaton reduction. It
does not expose or define Thatcher--Wright's algebraic signature, a source term
“generalized automaton,” a ranked-signature standing, the old paper's coding,
or a source example. The registered Thatcher--Wright article is pp. 57--81,
but no page of that technical body is present in the frozen evidence; the
acquisition note records the whole body as unavailable. Consequently there is
no inspected Thatcher--Wright printed page that can control the claims at
compact-record lines 688, 690, 692, or 909. TATA p. 95 can control the fact of
the citation only, not silently supply the cited paper's definitions.

**Five-part terminology audit at actual first use.** In the detailed note the
first use is “generalized-automaton definitions” at lines 192--193; in the
compact record the operative first use is the command “Define the generalized
automaton” at line 692. Both fail the charter's rule:

1. **Necessity:** neither location explains why the source-attested phrases
   “finite algebra” and “recognizability relation” cannot state the owed
   distinction.
2. **Definition or source standing:** line 692 supplies an asserted
   ranked-signature gloss, but it cannot be an exact eliminable definition or
   source introduction because the source body and exact signature are
   explicitly unavailable. The detailed note supplies no definition at all.
3. **Standing:** line 692 prematurely treats the name as an object whose
   standing is a ranked finite algebra; the frozen evidence establishes no such
   exact source standing.
4. **Nonredundancy:** no source-controlled distinction among “generalized
   automaton,” the abstract's finite algebra, and TATA's modern bottom-up tree
   automaton is proved or explained.
5. **Use:** the name is used only to label a future acquisition obligation; no
   admitted definition or theorem requires it.

The same paragraph also fixes ranked signature, finite-tree/term coding, weak
set-quantifier range, and a ranked-algebra example before the body visit. Those
are precisely the hypothetical answers that T19 says an open owed artifact
must not name and the body-dependent matters that the acquisition note leaves
unseen.

**Boundary and admission effect.** This is simultaneously:

- a historical/modern substitution risk, because TATA's modern ranked-tree
  presentation is being used to prefigure the missing 1968 construction;
- an acquisition/admission failure, because an open visit has been converted
  into a prescribed technical answer;
- a terminology failure at first use; and
- a cross-record contradiction between the compact/detailed records and the
  acquisition note (while the reader uses the correct narrower boundary).

It therefore fails mandatory invariants T19, T20, and T21. Under the charter's
seat mandate, a premature technical name, hidden source substitution, or
cross-record contradiction is at least a must-fix. The fact that `N-c-015.a`
remains labelled open does not cure the content claim: “open” status and a
speculatively fixed answer can coexist, and T19 forbids the latter expressly.

**Required correction.** The compact record at lines 688, 690, 692, and 909
and the detailed note at lines 192--194 must be reduced to the abstract-level
scope actually recorded at acquisition-note lines 29--34. The owed artifact
may require acquisition of the paper's exact finite-algebra definition,
recognizability relation, logic, coding, results, examples, and proof boundary,
but it must not decide in advance that the paper's object is a “generalized
automaton,” that its exact signature is ranked, that its domain/coding is the
modern finite-tree one, or what example the body contains. Because these are
frozen objects, any correction requires a newly hash-pinned blind round.

## Mandatory invariant disposition

| ID | Disposition | Adversarial result |
|---|---|---|
| T01 | PASS | The HAL cover and internal title, the 18 November 2008 footers, bibliography entry at `handbook/bib/handbook.bib:5835-5840`, reader lines 6--10, detailed note, and compact lines 696--698 agree on title, full author order, 2008 fixed release, evolving-work 2007 label, HAL route, and 263/262-page custody. |
| T02 | PASS | Physical page 001 demonstrates an authorized HAL public deposit, not a Creative Commons or blanket republication licence. The frozen records keep the PDF/renders as research evidence rather than handbook assets. |
| T03 | PASS | TATA printed pp. 11--13 explicitly limits the treatment to finite trees and excludes infinite-tree automata. Reader lines 6--10 and 131--139 and main lines 868--872 and 889--890 preserve the distinction. |
| T04 | PASS | TATA printed pp. 19--20 and reader lines 12--30 give ranked finite terms, nullary leaves, positive arities, source tuple `A=(Q,F,Q_f,Delta)`, and the explicit nonconflicting handbook symbol map. |
| T05 | PASS | TATA printed pp. 20--22 and reader lines 18--27 type transition rules and bottom-up runs at all arities, including nullary rules, with final-root acceptance and exact recognizable-language standing. |
| T06 | PASS | TATA printed pp. 22--27 and reader lines 32--37 retain “at most one target,” same-language determinization, and reachable subset states without claiming every source table. |
| T07 | PASS | TATA printed p. 30 (Theorem 1.3.1) and p. 40 (Theorem 1.7.4), reader lines 39--47, and main lines 883--888 agree on effective Boolean closure and upward marking, with nonemptiness exactly when a final state is marked and the linear-time claim kept at the source representation boundary. |
| T08 | PASS | Reader lines 32--37 give a correct handbook-owned run on `f(a,b)` and explain that deleting the root rule removes every root-compatible run. |
| T09 | PASS | TATA printed pp. 87--90 and reader lines 49--60 preserve word-valued first-order variables, finite word-set variables, Proposition 3.3.1, and all four restricted atoms. |
| T10 | PASS | TATA printed pp. 90--91 and reader lines 62--71 agree on arities, coordinate meanings, Example 3.3.3's three sets, named labels, and nullary bottom padding rather than an all-zero slogan. |
| T11 | PASS | Reader lines 73--83 explicitly define the finite domain `D`, label sets, label/child translations, and both quantifier restrictions; the ambient successor prefix tree remains a coding structure rather than an infinite automaton input. |
| T12 | PASS | TATA printed pp. 91--93 and reader lines 85--96 preserve Figure 3.9's complete one-state list for inclusion, missing-coordinate cylindrification, union, complement, and projection. |
| T13 | PASS | TATA printed p. 94 and reader lines 98--110 quantify one state-position set per state, partition exactly the encoded domain, require a final root label, and state the local implication with a disjunction over matching transitions and children directed into their assigned state sets. |
| T14 | PASS | TATA printed p. 95 and reader lines 112--118 retain the “not very precise” qualification and the two controlling lemmas. The closed case uses the empty track alphabet or its sole nullary `top`, and validity reduces to a rule into a final state. |
| T15 | PASS | TATA printed p. 43 and reader lines 120--129 retain exactly `{a^(0),f^(2)}` and `{f(t,t):t in T(F)}`. The handbook-owned deterministic proof establishes reachability for every term before using the collision/crossed-pair contradiction. |
| T16 | PASS | TATA printed pp. 95--96 and reader lines 131--139 distinguish finite-set WSkS from full SkS, arbitrary possibly infinite sets, root-down infinite-input automata, and the different complement problem. Weak/full coincidence is asserted only on actually finite structures. |
| T17 | PASS | Shared main definition `handbook/parts/p09/logic-in-computer-science.tex:845-874` and theorem `:876-891` agree with the reader on finite ranked trees, bottom-up recognition, finite-tree MSO, effective operations, and Rabin nonconflation. |
| T18 | PASS | Reader lines 154--161 accurately calls the delivery an operative constructive outline, identifies the small run and Exercise 1.4 proof as handbook-owned, and does not claim to reproduce every source table or proof. |
| T19 | **FAIL — TATA-R2-AP-01** | Compact lines 688, 690, and 692 infer a finite-tree/ranked-signature answer and lines 692 and 909 name a hypothetical “generalized automaton” despite the unacquired body. TATA printed p. 95 supports only the `[TW68]` attribution. |
| T20 | **FAIL — TATA-R2-AP-01** | Bibliographic identity (`handbook/bib/handbook.bib:5993-6002`) is correct, but compact lines 688--692/909 and detailed-note lines 192--194 contradict the narrower evidence and no-hypothetical-name boundary at acquisition-note lines 5--7, 29--34, and 74--82. |
| T21 | **FAIL — TATA-R2-AP-01** | “Generalized automaton” fails necessity, exact source standing, object standing, nonredundancy, and later-use requirements at its actual first uses. The open obligation has been assigned speculative terminology and structure. |
| T22 | PASS | Reader line 161 and compact line 706 keep independent review/admission open; the records do not claim build, visual handbook, human, user, book, publication, `N-c-015.a`, or overall `N-c-015` completion. This report rejects rather than broadens the exact admission scope. |

## Boundary stress-test summary

The finite/infinite, weak/full, source/handbook, access/licence, and
proof/outline boundaries survived adversarial comparison with the controlling
printed pages. Bibliographic identity and the TATA release boundary also agree.
The historical/modern and acquisition/admission boundaries do not survive:
the frozen records correctly call the Thatcher--Wright body unavailable but
nevertheless import a modern ranked-tree answer and speculative technical name
into its owed reconstruction. That single must-fix defect prevents admission
on this seven-object snapshot even though the reader-facing TATA construction
otherwise passes T01--T18 and T22.

VERDICT: REJECT — TATA-R2-AP-01
