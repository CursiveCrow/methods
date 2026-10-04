# Full-transcription audit: Parts 9--14 and remaining shared apparatus

Date: 2026-08-11  
Scope: live Parts 9--14, their annexes, the frozen inherited source span assigned to Part 12/back matter, all P9--P14 register additions, Phase-6 apparatus, and cross-part apparatus whose completion depends on P9--P14.  
Mode: read-only audit. This note does not edit manuscript, registry, generated, or source files.

## Binding standard and classifications

The controlling amendment is `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`. In particular, the frozen inherited source must be present in full; all four registers are inclusion requirements rather than treatment ceilings; source variants must remain separate; and compression, pointers as substitutes, retirement, notation normalization, hybridization, and invented technical names are prohibited. A unit receives a passing classification or every simultaneous defect classification that applies. The former source-mapping plan explicitly authorized compression and retirement (`spec/gap-analysis.tex:363-390`), so those dispositions are superseded rather than evidence of completion.

This audit uses the contract's exact classes:

- **full and accurate**: the complete presentation is present with notation, hypotheses, rules, side conditions, proof status, proof, examples, qualifications, and attribution intact;
- **altered**: a source presentation exists, but its content or notation was changed;
- **abridged**: only a capsule, table cell, pointer, selected fragment, or shortened proof remains;
- **omitted**: the owed unit is absent or only a stub exists;
- **hybridized**: clauses from distinct presentations have been combined into one presentation or attributed as one;
- **unsupported addition**: a name, theorem, example, syntax, or claim lacks a controlling source presentation;
- **layout-only relocation**: the full, unchanged unit moved without content change.

No live P9--P14 substantive unit audited here qualifies as **full and accurate**. No asserted relocation in the Part-12 verifier qualifies yet as **layout-only relocation**, because the verifier records compression, conversion, selective rehoming, or retirement rather than a source-to-book completeness check (`spec/verification/phase4-p12.md:79-119`).

## Executive verdict

| Area | Live evidence | Verdict |
|---|---|---|
| Part 9 body and annex | `handbook/parts/p09/logic-in-computer-science.tex:1-3`; `handbook/annex/p09.tex:1-3` | **omitted**: one body stub and one annex stub replace four depth rows, twenty-six `N-c` rows, the formerly excluded but now owed `N-x-015`, and the architecture's type-systems requirement. |
| Part 10 body and annex | `handbook/parts/p10/algebraic-and-categorical-logic.tex:1-3`; `handbook/annex/p10.tex:1-3` | **omitted**: one body stub and one annex stub replace eight depth rows, twenty-four `N-d` rows, and now-owed `N-x-010`/`N-x-013`. |
| Part 11 body and annex | `handbook/parts/p11/philosophy-of-logic.tex:1-3`; `handbook/annex/p11.tex:1-3` | **omitted**: one body stub and one annex stub replace eight `N-b` rows, now-owed `N-x-008`, and the architecture's identity/schools units. |
| Part 12 inherited material | frozen `source/formal-logic-reference.tex:14095-17206`; live fragments under `handbook/parts/p12/` and `handbook/annex/p12/` | **altered/abridged/omitted**: the verifier itself says “compact,” “compressed,” “converted,” “selectively rehomed,” and “retired” (`phase4-p12.md:81-99`). |
| Part 12 new content | register rows `D-P11-001`--`D-P11-015` applicable to P12 and `N-c-031`--`N-c-040` | **omitted/abridged/hybridized**: seven new-content rows are explicit stubs; the three nonstub rows are survey composites rather than full source presentations. |
| Part 13 | `handbook/parts/p13/chronology-and-biography.tex:1-3` | **omitted**: chronology, landmark papers, biographies, and notation history are a stub; no controlling source ledger exists. |
| Part 14 master apparatus | `handbook/parts/p14/master-tables.tex:1-3` | **omitted**: every master table, glossary, list, and distinct index promised there is a stub. |
| Part 14 rule sheets | `handbook/parts/p14/rule-sheets.tex:1-77`; 55 live registry files | **altered/abridged/hybridized/omitted** by row: the inherited three sheets were rewritten; required sheets A-022/A-023 and the superposition component are absent; several authored sheets explicitly mix or normalize sources. |
| Frozen assessment/feedback | `source/formal-logic-reference.tex:15489-16742` | **omitted**: five solved qualifying problems, five additional problems, and 111 feedback units were retired. |
| Frozen bibliography/index | `source/formal-logic-reference.tex:16803-17204` | **altered**: biblatex conversion was normalized and no record-level exactness ledger exists; the source index was regenerated without a source-entry ledger. |

The old `N-x` “excluded” notes do not survive the binding amendment. The contract says the registers are inclusion requirements and expressly revokes treatment ceilings (`FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:32-34,137-139`). Thus `N-x-008`, `N-x-010`, `N-x-013`, and `N-x-015` are classified **omitted**, not legitimately excluded.

## Exact source-to-book ledger for the frozen Part-12/back-matter span

The frozen file contains the only inherited material assigned to Parts 12 and 14. The line ranges below are exhaustive from the Part-12 source part through the end of the document.

| Frozen source locator | Exact source unit | Asserted/live home | Class and defect | Patch-ready restoration |
|---:|---|---|---|---|
| 14095--14146 | Part/chapter opening; derivation-search method; numbered procedure; mixed-search example | `parts/p12/formal-workflow.tex:12-25` | **abridged** | Transcribe the whole span, including its list and example, as one attributed inherited unit. Keep any newer method box only as a separately labelled editorial aid. |
| 14147--14169 | propositional countervaluation method and example | `formal-workflow.tex:27-36` | **abridged** | Restore the exact method and example; do not replace either with a checklist capsule. |
| 14170--14202 | first-order semantic-refutation method, numbered steps, example | `formal-workflow.tex:38-71` | **abridged** | Restore all steps and the complete example. The live two-element example is not a substitute for the source example unless an exact identity ledger proves it. |
| 14203--14230 | metatheoretic-proof method, numbered steps, warning | `formal-workflow.tex:60-71` | **abridged** | Restore method and warning verbatim in mathematical content and status. |
| 14231--14270 | failure analysis plus `ex:formal-practice-01` and `ex:formal-practice-02` | `formal-workflow.tex:179-215`; P12 verifier dispositions | **abridged** | Restore the complete failure analysis and both exercises at stable labels; restore their full feedback at 16594--16614. |
| 14271--14350 | automated-reasoning opening; clause semantics; unit propagation; pure-literal elimination; displayed DPLL listing; theorem; complete proof | `parts/p12/sat-and-certificates.tex:12-64`; `annex/p12/sat-and-certificates.tex:3-38` | **altered** | Restore 14271--14350 as the inherited DPLL presentation, including the listing at 14315--14326 and pure-literal definition. Retain the repaired residual-state proof only as a separately labelled handbook correction, never as the inherited transcript. |
| 14351--14400 | equivalence/equisatisfiability definition, Tseitin discussion and worked example | P2 pointer; P12 audit prose | **abridged** | Restore the complete source unit at one physical home. A cross-reference passes only after the P2 audit proves the entire source unit is unchanged there. |
| 14401--14434 | unification procedure, definitions, occurs-check example | P2 pointer; `first-order-automation.tex:5-21` | **abridged** | Restore the entire source presentation and example; then add each Martelli--Montanari and other source presentation separately. |
| 14435--14479 | exact resolution/factoring rules; soundness theorem and proof; equality-free completeness statement and qualifications | P2 pointer; `first-order-automation.tex:23-64` | **abridged** | Restore 14435--14479 in full, including proof 14459--14468 and every qualification. Registry rendering can be a layout relocation, but cannot replace the prose, theorem, proof, or attribution. |
| 14480--14495 | equality/superposition boundary and warning | `first-order-automation.tex:171-193` | **abridged** | Restore the warning in full, then add the exact distinct superposition presentations owed by `D-P11-003`/`N-c-036`. |
| 14496--14521 | SMT definition, SMT-LIB/TPTP roles, practical interfaces | `smt-and-exchange-formats.tex:5-215` | **altered** | Restore the inherited source presentation separately. Do not treat the expanded live survey or current protocol versions as its transcript. |
| 14522--14560 | complexity/practical-status discussion and automated-result audit list | P2/P4 pointers; `formal-workflow.tex:73-121` | **abridged** | Restore the complete source discussion and list; cross-links may be added without deleting it. |
| 14562--14589 | `ex:automated-reasoning-01`--`03` | converted examples/pointers (`phase4-p12.md:107-109`) | **altered** | Restore all three exercises exactly and restore their feedback at 16615--16639. Keep worked examples separately if useful. |
| 14591--14628 | mechanization opening; proof-term, kernel, elaboration, tactic definitions | `interactive-proof.tex:5-35` | **altered** | Restore every source definition separately; do not merge them into the handbook taxonomy `def:p12-mechanization-layers`. |
| 14629--14660 | propositions-as-types discussion and numbered correspondence | `interactive-proof.tex:111-123` and P7 pointer | **abridged** | Restore the entire correspondence unit; source and P7 presentations may be linked but not collapsed. |
| 14661--14690 | trusted-base definition, explanation, numbered audit list | `interactive-proof.tex:7-35` and workflow tables | **altered** | Restore the source definition/list separately from the newer result-relative “trusted base” definition. |
| 14691--14728 | small propositions-as-types example, warning, `ex:mechanization-01`/`02` | `interactive-proof.tex:111-123`, `37-74`; verifier conversion | **abridged** | Restore the exact example, warning, and both exercises; restore their feedback at 16640--16685. |
| 14729--14778 | academic-prose section and both lists | `formal-workflow.tex:141-177` | **abridged** | Restore the full prose and lists; method boxes may follow as editorial navigation. |
| 14779--14814 | one-symbol/one-role section | P1 registry and `formal-workflow.tex:154-165` | **altered** | Restore the source section unchanged. Register source-specific local roles without collision-driven renaming. |
| 14815--14850 | complete before/after formalization | no complete live counterpart | **omitted** | Restore both the “before” and “after” displays and all explanation. |
| 14851--14870 | LaTeX structure section | `formal-workflow.tex:143-177` | **abridged** | Restore the full source section. |
| 14871--14931 | source/render audit; complete theorem source, proof, rendered-claim analysis, five-step audit | no complete live counterpart | **omitted** | Restore all of 14871--14931, including theorem/proof listing 14882--14894 and the complete audit sequence. |
| 14932--14945 | rule-display section | registry pointer | **abridged** | Restore the full source prose and example policy; a registry link is additional navigation only. |
| 14946--14975 | worked correction of an invalid rule application | no complete live counterpart | **omitted** | Restore the complete invalid derivation, diagnosis, and corrected derivation. |
| 14976--14990 | citation-practice section | further-reading/workflow fragments | **abridged** | Restore the full section and its qualifications. |
| 14991--15029 | revision audit, numbered list, `ex:latex-style-01`/`02` | audit method; exercises retired | **abridged** | Restore section, list, both exercises, and feedback at 16686--16709. |
| 15030--15050 | research-workflow opening and theorem-status table | `formal-workflow.tex:217-247` | **altered** | Restore exact table and surrounding prose; newer status fields remain a separate editorial record. |
| 15051--15068 | counterexample-first testing | `formal-workflow.tex:179-215` | **abridged** | Restore full source unit. |
| 15069--15077 | reproducible computational supplements | `formal-workflow.tex:217-247` | **abridged** | Restore full source unit. |
| 15078--15091 | independent review and warning | `formal-workflow.tex:179-215` | **abridged** | Restore the exact review unit and warning. |
| 15093--15206 | appendix transition; registered-notation appendix, table, structure convention, natural-numbers convention | P1 registry; deliberately retired (`phase4-p12.md:93`) | **altered** | Restore the `\appendix` transition and the complete appendix in source notation. Generated registry tables may index it, not normalize or replace it. |
| 15207--15239 | binding and precedence appendix | P1 precedence; deliberately retired (`phase4-p12.md:94`) | **altered** | Restore the full source appendix, then add separate presentation-specific precedence tables. |
| 15240--15488 | complete inherited ND, LK, and K rule-sheet chapter | registry/P14; deliberately retired (`phase4-p12.md:95`) | **altered** | Restore all three inherited sheets exactly as their own attributed presentations. Repaired or differently named registry calculi must remain separate variants. |
| 15489--15619 | five qualifying problems and five supplied solutions | retired (`phase4-p12.md:96,115-119`) | **omitted** | Restore all five problems and complete supplied solutions at original labels. |
| 15620--15637 | five additional qualifying problems | retired | **omitted** | Restore all five prompts; do not turn the proof-assistant prompt into an audit-table row. |
| 15638--16742 | exercise-feedback chapter: 111 labelled feedback/key units in twelve sections | globally retired (`phase4-p12.md:97`) | **omitted** | Restore all 111 units and their bidirectional links. Section counts are 9, 12, 19, 11, 5, 10, 7, 7, 11, 6, 9, and 5 for source starts 15648, 15722, 15832, 16022, 16132, 16187, 16306, 16374, 16447, 16539, 16592, and 16710. |
| 16743--16801 | four-section release checklist | `formal-workflow.tex:249-343`; converted (`phase4-p12.md:98`) | **altered** | Restore the complete inherited checklist; retain the newer release table as a separately identified editorial apparatus. |
| 16803--17196 | backmatter and 64 manual bibliography records | `bib/handbook.bib`; normalized biblatex conversion | **altered** | Create a 64-record field ledger proving exact retention of authors, titles, editions, publication facts, DOI/URL, retrieval/version data, and qualifications. Reformatting may be layout-only; normalization or field deletion may not. |
| 17198--17204 | source index production | one live subject index | **altered** | Preserve every inherited index entry and cross-reference, then add the new subject/symbol/person/theorem indexes separately. |
| 17206 | document terminator | `main.tex` | **layout-only relocation** | No content restoration needed. |

### DPLL is not an exact migration

The source DPLL presentation uses clause set `S`, original-variable set `V`, unit propagation, optional pure-literal elimination, the literal pseudocode listing, and the theorem/proof at `source/formal-logic-reference.tex:14281-14350`. The live presentation introduces a named “residual state,” changes the data to `(G,u)`, removes the source listing, excludes pure-literal elimination from the displayed logical core, reformulates the theorem, and substitutes a longer repaired proof (`handbook/parts/p12/sat-and-certificates.tex:14-64`; `handbook/annex/p12/sat-and-certificates.tex:3-38`). The verifier confirms that the proof was repaired and expanded (`spec/verification/phase4-p12.md:146-163`). The correct patch is two presentations, not a winner:

1. the inherited DPLL presentation in full, exactly scoped and attributed to its source span; and
2. the repaired handbook DPLL variant, explicitly identified as an editorial correction with a change ledger and independent proof.

## Part 9 register ledger

The target architecture requires finite/database connections, description logics, logic programming, program logics, model checking, and type systems (`spec/gap-analysis.tex:327-332`). The live chapter and annex are only stubs. Therefore every row below is **omitted**.

For each semicolon-delimited citation below, restoration means a separate, fully attributed presentation retaining that work's notation, definitions, hypotheses, result strength, proof status, examples, and qualifications. A later survey or monograph may be included as its own presentation, but may not stand in for an original primary presentation.

| Row | Owed presentation(s) recorded by the register |
|---|---|
| `N-c-001` | Ebbinghaus--Flum 1995; Libkin 2004 |
| `N-c-002` | Glebskii et al. 1969; Fagin 1976; Libkin 2004 |
| `N-c-003` | Hanf 1965; Gaifman 1982; Libkin 2004 |
| `N-c-004` | Fagin 1974; Vardi 1982; Immerman 1986; Immerman 1999 |
| `N-c-005` | Lewis 1979; Börger--Grädel--Gurevich 1997 |
| `N-c-006` | Mortimer 1975; Grädel--Kolaitis--Vardi 1997 |
| `N-c-007` | Andréka--van Benthem--Németi 1998; Grädel 1999 |
| `N-c-008` | Löwenheim 1915; Behmann 1922; Börger--Grädel--Gurevich 1997 |
| `N-c-009` | Schmidt-Schauß--Smolka 1991; Baader et al. 2003; Baader--Horrocks--Lutz--Sattler 2017 |
| `N-c-010` | Baader--Brandt--Lutz 2005; Calvanese et al. 2007; Baader--Horrocks--Lutz--Sattler 2017 |
| `N-c-011` | Schild 1991 |
| `N-c-012` | Kamp 1968; Pnueli 1977; Gabbay--Pnueli--Shelah--Stavi 1980; Sistla--Clarke 1985 |
| `N-c-013` | Büchi 1962; McNaughton 1966; Vardi--Wolper 1986; Safra 1988; Thomas 1997 |
| `N-c-014` | Büchi 1960; Elgot 1961; Trakhtenbrot 1961; Rabin 1969; Thomas 1997 |
| `N-c-015` | Thatcher--Wright 1968; Comon et al. 2007 |
| `N-c-016` | Clarke--Emerson 1981; Queille--Sifakis 1982; Emerson--Halpern 1986; Clarke--Grumberg--Peled 1999; Baier--Katoen 2008 |
| `N-c-017` | Bryant 1986; Burch et al. 1992; McMillan 1993; Biere--Cimatti--Clarke--Zhu 1999; Clarke et al. 2003 |
| `N-c-018` | Kozen 1983; Emerson--Jutla 1991; Bradfield--Stirling 2007 |
| `N-c-019` | Floyd 1967; Hoare 1969; Dijkstra 1975; Cook 1978; Apt 1981 |
| `N-c-020` | O'Hearn--Reynolds--Yang 2001; Reynolds 2002; Calcagno et al. 2011; O'Hearn 2019 |
| `N-c-021` | Pratt 1976; Fischer--Ladner 1979; Kozen--Parikh 1981; Harel--Kozen--Tiuryn 2000 |
| `N-c-022` | Kowalski 1974; van Emden--Kowalski 1976; Clark 1978; Apt--van Emden 1982; Lloyd 1987 |
| `N-c-023` | Gelfond--Lifschitz 1988; Marek--Truszczyński 1999; Brewka--Eiter--Truszczyński 2011 |
| `N-c-024` | Chandra--Merlin 1977; Vardi 1982; Abiteboul--Hull--Vianu 1995 |
| `N-c-025` | Feder--Vardi 1998; Bulatov 2017; Zhuk 2017 |
| `N-c-026` | Cook 1971; Stockmeyer--Meyer 1973; Ladner 1977; Papadimitriou 1994 |
| `N-c-028` | McMillan 2003 |
| `N-x-015` | Halpern 2003; Baier--Katoen 2008. The old “excluded” note is revoked; probabilistic/stochastic model checking and probability logics require full treatment. |

Depth crosswalks are also **omitted**: `D-P10-010` (full Büchi/LTL model checking, coordinated without collapsing `N-c-013`), `D-P11-006` (SLD, soundness/completeness, negation as failure, Prolog; coordinated with `N-c-022`), `D-P11-007` (ASP and Datalog; keep `N-c-023` and `N-c-024` distinct), and `D-P11-008` (Hoare/weakest preconditions and separation logic; keep `N-c-019` and `N-c-020` distinct). Register locators: `spec/registers/depth-gaps.csv:94,133-135`; `spec/registers/new-content.csv:108-135,186`.

## Part 10 register ledger

The target architecture is at `spec/gap-analysis.tex:333-338`; the live body/annex are stubs. Every row below is **omitted**. The same separate-full-presentation rule applies to every cited work.

| Row | Owed presentation(s) recorded by the register |
|---|---|
| `N-d-001` | Birkhoff 1935; Birkhoff 1944; Burris--Sankappanavar 1981 |
| `N-d-002` | Birkhoff 1935; Burris--Sankappanavar 1981 |
| `N-d-003` | Halmos 1963; Bell--Slomson 1969; Koppelberg 1989 |
| `N-d-004` | Stone 1936; Halmos 1963; Johnstone 1982; Givant--Halmos 2009 |
| `N-d-005` | Tarski 1935; Rasiowa--Sikorski 1963 |
| `N-d-006` | Priestley 1970; Davey--Priestley 2002 |
| `N-d-007` | Johnstone 1982; Marker 2002 |
| `N-d-008` | Heyting 1930; McKinsey--Tarski 1946; Rasiowa--Sikorski 1963; Balbes--Dwinger 1974 |
| `N-d-009` | Esakia 1974; Chagrov--Zakharyaschev 1997 |
| `N-d-010` | Johnstone 1982; Picado--Pultr 2012; the old pointer ceiling is revoked |
| `N-d-011` | Jónsson--Tarski 1951; Goldblatt 1989; Blackburn--de Rijke--Venema 2001; Venema 2007 |
| `N-d-012` | McKinsey--Tarski 1944; Rasiowa--Sikorski 1963; van Benthem--Bezhanishvili 2007 |
| `N-d-013` | Chang 1958; Chang 1959; Mundici 1986; Cignoli--D'Ottaviano--Mundici 2000 |
| `N-d-014` | Ono--Komori 1985; Galatos--Jipsen--Kowalski--Ono 2007 |
| `N-d-015` | Hájek 1998; Cignoli--Esteva--Godo--Torrens 2000; Jenei--Montagna 2002 |
| `N-d-016` | Henkin--Monk--Tarski 1971; Henkin--Monk--Tarski 1985; Monk 2000; the former survey ceiling is revoked |
| `N-d-017` | Tarski 1941; Tarski--Givant 1987; Maddux 2006 |
| `N-d-018` | Blok--Pigozzi 1989; Font 2016; the old pointer ceiling is revoked |
| `N-d-019` | Mac Lane 1998; Awodey 2010 |
| `N-d-020` | Lawvere 1963; Adámek--Rosický--Vitale 2011 |
| `N-d-021` | Lambek 1980; Lambek--Scott 1986 |
| `N-d-022` | Lawvere 1969; Pitts 2000 |
| `N-d-023` | Lawvere 1970; Lambek--Scott 1986; Mac Lane--Moerdijk 1992; Johnstone 2002; the former overview ceiling is revoked |
| `N-d-024` | Tierney 1972; Mac Lane--Moerdijk 1992; the old pointer ceiling is revoked |
| `N-x-010` | Font--Jansana--Pigozzi 2003; Font 2016. Full abstract algebraic logic is owed. |
| `N-x-013` | Jacobs 1999; Lurie 2009. Fibrations, sketches, and infinity-topoi are owed as distinct source presentations. |

Depth rows also **omitted**: `D-P2-009`, `D-P10-022`, `D-P10-034`, and `D-P10-039`--`D-P10-043` (`spec/registers/depth-gaps.csv:16,106,118,123-127`). Their overlaps with `N-d-003`--`005`, `N-d-013`--`014`, `N-d-016`--`017`, and `N-d-021`--`023` are cross-references, not permission to manufacture one merged account.

## Part 11 register ledger

The target architecture is at `spec/gap-analysis.tex:339-343`; the live body/annex are stubs. Every row below is **omitted**.

| Row | Owed presentation(s) recorded by the register |
|---|---|
| `N-b-019` | Tarski 1935; Tarski 1944 |
| `N-b-020` | Kripke 1975; Martin 1984; Halbach 2011 |
| `N-b-021` | Herzberger 1982; Gupta--Belnap 1993 |
| `N-b-022` | Friedman--Sheard 1987; Feferman 1991; Halbach 2011; Horsten 2011 |
| `N-b-023` | Curry 1942; Yablo 1993; Priest 2006; Beall--Glanzberg--Ripley 2018 |
| `N-b-024` | Fine 1975; Williamson 1994; Keefe 2000; Smith 2008 |
| `N-b-034` | Tarski 1936; Prawitz 1974; Etchemendy 1990; Sher 1991; Dummett 1991 |
| `N-b-035` | Quine 1970; Boolos 1984; Boolos 1985; Shapiro 1991 |
| `N-x-008` | Carnap 1950. The “philosophy-of-science” exclusion is revoked; inductive logic and confirmation theory are owed. |

Register locators: `spec/registers/new-content.csv:91-96,106-107,179`. The architecture's identity unit and schools units have no controlling presentation packet; that absence is a source-critical blocker, not authorization to write synthetic capsules.

## Part 12 register ledger and attribution defects

| Row | Live class | Exact defect and required split |
|---|---|---|
| `D-P11-001` / `N-c-032` | **omitted** | The live CDCL vocabulary/table/figure and explicit stub (`sat-and-certificates.tex:192-324`) are not the five source presentations: Marques-Silva--Sakallah 1999; Moskewicz et al. 2001; Eén--Sörensson 2003; Marques-Silva--Lynce--Malik 2009; Wetzler--Heule--Hunt 2014. Restore each separately, including its algorithm, exact learned-clause/certificate mechanism, invariants, status, and examples. |
| `D-P11-002` / `N-c-035` | **omitted** | The occurs-check example and stub (`first-order-automation.tex:14-21,184-189`) omit Robinson 1965; Huet 1973; Goldfarb 1981; Martelli--Montanari 1982; Baader--Snyder 2001. Do not collapse first-order, equational/AC, and higher-order unification. |
| `D-P11-003` / `N-c-036` | **omitted** | The warning/stub (`first-order-automation.tex:171-193`) omits Bachmair--Ganzinger 1994 and Nieuwenhuis--Rubio 2001 as separate calculi/presentations, including rules, orders, redundancy, saturation, and model-construction status. |
| `D-P11-004` | **abridged** | `first-order-automation.tex:66-169` compresses ordered resolution, Robinson hyperresolution, Slagle semantic resolution, Wos--Robinson--Carson set of support, and subsumption into a taxonomy. Restore each primary presentation in full; keep the comparison table only as navigation. |
| `D-P11-005` | **hybridized** | `thm:p12-nelson-oppen` (`smt-and-exchange-formats.tex:62-108`) is cited only to Nelson--Oppen 1979, but the construction note says the displayed stable-infiniteness/convexity boundary comes from a later Barrett--Tinelli survey (`spec/research/p12-new-content.md:351-367`). Restore Nelson--Oppen 1979 separately; restore Nieuwenhuis--Oliveras--Tinelli 2006 DPLL(T), Dutertre--de Moura 2006 simplex, de Moura--Bjørner 2008, and Barrett--Sebastiani--Seshia--Tinelli 2009 separately. |
| `D-P11-009` | **abridged** | `sat-and-certificates.tex:113-190` supplies short BDD/#SAT/MaxSAT entries and a QBF pointer. Restore Bryant 1986, the QBF source presentation, Valiant 1979, and the declared MaxSAT source separately and fully. |
| `D-P11-011` | **abridged** | The landscape table (`interactive-proof.tex:247-320`) is a current-product comparison, not full source presentations for Agda, HOL Light, HOL4, PVS, Mizar, ACL2, Metamath, Lean, Rocq, and Isabelle. Each exact official foundation/checker presentation must precede the comparison. |
| `D-P11-012` / `N-c-031` | **hybridized** | `interactive-proof.tex:125-245` combines Barendregt 1992 PTS/lambda cube, Coquand--Huet 1988 CoC, and Paulin--Mohring's CIC/pCIC account. Restore the three presentations separately in their original notation; do not call Lean a Coq/CIC presentation. |
| `D-P11-013` | **omitted** | The stub at `interactive-proof.tex:369-373` is not content. The revoked pointer ceiling cannot substitute for the full source-specific HoTT/univalence presentations routed through P7. |
| `D-P11-014` / `N-c-038` | **hybridized** | `interactive-proof.tex:7-109` combines de Bruijn 1970, Gordon--Milner--Wadsworth 1979, Pollack 1998, and Harrison 2009 into a house taxonomy. Restore each separately. |
| `D-P11-015` | **abridged** | `interactive-proof.tex:322-367` reduces five formalizations to one table row each. Restore the Four Color, Odd Order, Flyspeck, CompCert, and seL4 primary presentations separately; the table becomes navigation. |
| `N-c-033` | **abridged** | P12 gives a P2 pointer plus a random-SAT sentence (`sat-and-certificates.tex:99-111`). Restore Aspvall--Plass--Tarjan 1979, Dowling--Gallier 1984, and Mitchell--Selman--Levesque 1992 separately; upgrade to layout-only only if the P2 ledger proves exact full retention. |
| `N-c-034` | **omitted** | The explicit stub at `smt-and-exchange-formats.tex:217-221` admits the E-level internals/proof are absent. Restore all five register sources separately rather than upgrading the current S-level survey. |
| `N-c-037` | **omitted** | `rewriting.tex:1-9` is only a stub. Restore Newman 1942; Knuth--Bendix 1970; Huet 1980; Dershowitz 1982; Baader--Nipkow 1998 as separate presentations, including complete proofs/status exactly as supplied. |
| `N-c-039` | **omitted** | Stub at `interactive-proof.tex:374-379`; restore Paulin--Mohring 1989 and Letouzey 2003 separately and fully. |
| `N-c-040` | **omitted** | Stub at `interactive-proof.tex:380-382`; the revoked pointer ceiling does not satisfy the row. Restore Paulson--Blanchette 2010 and Blanchette et al. 2016 separately and fully. |

Register locators: `spec/registers/depth-gaps.csv:128-142`; `spec/registers/new-content.csv:138-147`.

### Invented names and source-status upgrades in live Part 12

1. `def:p12-de-bruijn-criterion` explicitly invents the technical name “operational de Bruijn criterion” and admits that de Bruijn did not use the phrase (`handbook/parts/p12/interactive-proof.tex:89-99`; construction instruction at `spec/research/p12-new-content.md:404-409`). Classification: **unsupported addition**. Patch: give de Bruijn 1970 and Pollack 1998 their own exact presentations; if a house audit condition remains, call it an editorial checklist condition, not a source technical term or theorem.
2. `thm:p12-lcf-boundary` is a handbook-formulated theorem carrying `cited=GordonMilnerWadsworth1979` (`interactive-proof.tex:102-109`), while the research note only supports defining the LCF architecture from that source (`p12-new-content.md:399-403`). Classification: **unsupported addition**. Patch: transcribe the source's architecture claims; if the closure-under-sound-constructors statement is wanted, state and prove it as a separately attributed handbook lemma rather than a cited source theorem.
3. `def:p12-dpll-state` introduces the named “residual state” while replacing the inherited DPLL presentation (`sat-and-certificates.tex:14-39`). Classification: **altered**. Patch: keep the source presentation intact and place the residual-state repair separately.
4. `thm:p12-nelson-oppen` is the concrete hybrid-attribution defect described above. Classification: **hybridized**, not merely shortened.
