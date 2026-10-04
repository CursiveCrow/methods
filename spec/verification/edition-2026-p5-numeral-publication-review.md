# NOW-03a / PT-1: independent numeral-builder publication-text review

Date: 7 September 2026, America/Los_Angeles; 8 September UTC.
Review started: 2026-09-08 02:46:37 UTC. Assigned maximum block: 30 minutes.
Review completed: 2026-09-08 02:58:08 UTC, before the 15-minute checkpoint.
Reviewer: fresh publication-review agent `/root/pa_numeral_publication_review`.
Author role: none. Ownership: this report only.

## Retrieved Content

The following are verbatim excerpts from the actual files read. The complete
read extents and the review assessment appear separately below. All paths are
relative to the authoritative `C:/Dev/the-methods-of-reason` checkout.

### Source 1: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 78–102

```tex
\begin{hblemma}{thm:p05-builder-nocapture}{proved=annex:p5.builder-nocapture}{Internal substitution identities needed by the builders}
In \(\PA\), if \(\mathsf{nc}(c,i,u)=1\), the table output has the
input expression's term or formula type and
\[
 \mathsf{sub}(c,i,u)=\mathsf{ns}(c,i,u),\qquad
 1\leq\mathsf{cost}(c,i,u)\leq2\mathsf{nodes}(c).
\]
Thus its table equations are internal equations for the selected substitution
machine on these inputs. If \(u\) is a term with no variable occurrences,
the first field is one for every valid \(c\). It is also one for every
quantifier-free valid expression and every term \(u\).

In particular \(\PA\) proves that \(\nu(j)\) is a variable-free term
and, assuming \(\mathsf{Tm}(t)=1\), that
\(\mathsf{it}(s(t),j)=\mathsf{it}(t,Sj)\). With universal numerical
closure it also proves the guarded numeral-invariance assertion
\[
 \mathsf{Tm}(u)=1\ \longrightarrow
 \bigl(\mathsf{ns}(\nu(n),i,u)=\nu(n)\land
        \mathsf{sub}(\nu(n),i,u)=\nu(n)\bigr).
\]
The finite open-term axiom instances used below satisfy the same
table test; their only surviving inner binder has index 1 and their outer
replacement contains no variable of that index.
\end{hblemma}
```

### Source 2: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 92–98

```tex
For an invalid replacement, \(\mathsf{Tm}(u)=0\), the original type guards
instead give \(\mathsf{nc}(c,i,u)=\mathsf{ns}(c,i,u)=
\mathsf{cost}(c,i,u)=0\) and \(\mathsf{sub}(c,i,u)=0\) for every \(c\).
For example, the numerical input \(u=0\) is an empty-list code, not the
zero-term code \(\nu(0)=N_1()=C(1,0)=2\). At \(n=i=u=0\), both
substitution outputs are therefore zero, while \(\nu(0)=2\). These
unchanged failure values explain the replacement-term hypothesis.
```

### Source 3: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 418–425

```tex
Under the stated term domain and the premises \(\mathsf{Tree}(R)=1\),
\(k>b\) and \(f(R)=\mathsf{Eq}(\mathsf{it}(t,k),\nu(b))\), the
contradiction constructor has successful rows, root \(\mathsf{bc}\), and
retains its input open leaves together with unmarked \(q_1,q_2\) leaves.
These are internal checker invariants, including
zero numeral arguments, a zero peeling bound, equal comparison endpoints,
and the premise-free identity case.
\end{hbtheorem}
```

### Source 4: `handbook/parts/p05/pa-numeral-proof-builders.tex`, lines 474–501

```tex
\begin{hbtheorem}{thm:p05-fixed-term-literal-builders}{proved=annex:p5.fixed-term-literal-builders}{Fixed-term evaluation and literal transport inside PA}
For each fixed term \(t\), \(\PA\) proves that
\(\mathsf{pack}(R_t(\bar m))\) satisfies the selected checker with root
\[
                 \mathsf{Eq}(t^\nu(\bar m),\nu(t^\#(\bar m))).
\]
For each fixed literal \(\lambda\) just specified, with final builder
description \(d_\lambda\) and literal numeral-instance code
\(\lambda^\nu(\bar m)\), it proves
\[
 \forall\bar m\,\bigl(\lambda(\bar m)\to
   \exists p\,(\Gamma_{d_\lambda}(\bar m,p)\land
                \mathsf{Prf}^{19}_{\PA}(p,\lambda^\nu(\bar m)))\bigr).
\]
In this arithmetic implication \(\lambda(\bar m)\) denotes the original
fixed formula at the numerical parameters, not its code or an internal truth
predicate. All code-valued applications are eliminated through their specified
graphs. The positive-bottom instance has contradictory antecedent.
\end{hbtheorem}

\paragraph{The next construction.}
The next component combines these literal builders through the connectives and
marked bounded quantifiers of each fixed bounded formula. It must still
construct finite case enumeration, convert it to a quantified derivation, and
verify dependent substitutions and all discharge/freshness conditions. The
literal construction above supplies its arithmetic leaves. It does not itself
establish the bounded-formula compiler, the evidence-to-proof theorem, D3 or
the remaining provability-logic results.
```

### Source 5: `handbook/annex/p05/pa-numeral-proof-builders.tex`, lines 612–621

```tex
The final root is a sentence. It is also the literal numeral-instance code
\(\lambda^\nu(\bar m)\). For a comparison, the existential binder was
the least index absent from the original two terms when that abbreviation
was expanded. Those indices and that code were fixed at that stage.
Numeral substitution does not rename this binder, and the construction
retains its supplied index \(i\), even if index zero becomes available
after substitution. Thus there is no silent replacement of the target by
an alpha-equivalent code. For a signed equality there is no comparison
binder to retain. The outer negation, when present, is likewise preserved
literally by (9).
```

### Source 6: `handbook/parts/p05/pa-checker-arithmetization.tex`, lines 396–417

```tex
\begin{hbdefinition}{def:p05-selected-direct-pa-graph}{The selected direct arithmetic proof formula}
Decode \(p\) by requiring \(p=N_{19}(d,0)\), \(d=N_{15}(R)\),
with exact arities.  The binary characteristic description \(\chi_{19}(p,x)\)
returns zero if these outer tests fail.  Otherwise it returns
\[
 \mathsf{Tree}(R)\mathsf{Sent}(\mathsf{root}(R))E(x,\mathsf{root}(R))
     \prod_{v<\ell(\mathsf{open}(R))}
       \mathsf{Ax}_{19}(f_R(e(\mathsf{open}(R),v))).
\]
Let \(d_{19}\) be the finite formation tree obtained by the stated
expansions of this description and all its preceding library calls.  Select
the actual arithmetic formulas
\[
 \mathsf{Prf}^{19}_{\PA}(p,x)\defeq\Gamma_{d_{19}}(p,x,\bar1),
 \qquad
 \mathsf{Prv}^{19}_{\PA}(x)\defeq
                   \exists p\,\mathsf{Prf}^{19}_{\PA}(p,x).
\]
The \(\Gamma\) construction uses its fixed fresh-variable convention at
every expansion.  These formulas are selected by a finite description,
without selecting an arbitrary formula having the same standard values.
\end{hbdefinition}
```

### Source 7: active input routes

`handbook/parts/p05.tex`, lines 21–23:

```tex
\input{parts/p05/standard-pa-proof-predicate}
\input{parts/p05/pa-checker-arithmetization}
\input{parts/p05/pa-numeral-proof-builders}
```

`handbook/annex/p05-route.tex`, lines 14–19:

```tex
\hbannexchapter{5}{Arithmetic and Incompleteness}\label{annex:p05}
\input{annex/p05/internal-proof-predicate}
\input{annex/p05/standard-pa-proof-predicate}
\input{annex/p05/pa-checker-arithmetization}
\input{annex/p05/pa-numeral-proof-builders}
\input{annex/p05/depth-completion-supplement}
```

---

## Supplementary Notes

### Verdict and scope

**PASS for the assigned NOW-03a publication-text review**, including the two
actual target files, their mathematical dependency/navigation interfaces, the
nineteen appended symbol-registry entries, and their candidate TeX projections.
No blocking missing definition, omitted promised proof case, invalid local
proof route, or false completion claim was found in this scope.

This is one independent review context. It does not grant the author's own
acceptance, the other two independent review gates, admission, or PT-1 closure.
No build, render, test, static checker, generated-file promotion, or admission
mutation was performed by this reviewer. Publication layout and the final
reader-facing generated lookup remain separate production gates. The candidate
projections reviewed here are identified below and are not represented as
already published generated files.

The author intake was read as the assignment's declaration of intended scope.
Its author PASS was not treated as review evidence. No prior reviewer reports,
other reviewers' conclusions, or historical review-memory content were read.
The author's intake records older 490/628-line file identities. This review
binds the live 501/644-line targets specified by the lead and verified below.

### Complete reading and frozen identities

Each mathematical source in the first table was read from its first through
its last line, including every definition and proof. Range reads were joined
without missing intervening lines. These are actual content reads rather than
label searches counted as full reading. SHA256 values are whole-file hashes.

| File | Actual read extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p05/pa-numeral-proof-builders.tex` | Complete, 1–501 | `413117B591123F5B12C78124D1EC13ACE9B15CB3CBB61445DBE9CB6ED8F97BD0` |
| `handbook/annex/p05/pa-numeral-proof-builders.tex` | Complete, 1–644 | `3ABD15F81D47E8D5078C46B496DFBE4361ECBF36C25C54CB589CD9D7DC84237E` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | Complete, 1–523 | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | Complete, 1–537 | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | Complete, 1–252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | Complete, 1–315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/annex/p05/internal-proof-predicate.tex` | Complete, 1–524 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-09262-09327.tex` | Complete, 1–253 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | Complete, 1–546 | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-08306-08438.tex` | Complete, 1–133; comparison conventions at 28–59 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-09112-09149.tex` | Complete, 1–38 | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |
| `handbook/restoration/inherited-09099-09111.tex` | Complete, 1–13; source Q axioms | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09175-09187.tex` | Complete, 1–13; source PA induction | `0DB98B87928AA115C82883993E2E25B18286779E7DED0399C7148633C0178430` |
| `spec/research/edition-2026-p5-numeral-proof-builders.md` | Complete, 1–214; author intake only | `61BF33E44BF1706AB84786B899F964707B896C3C6F5933BC15925291CF9BD25D` |
| `spec/EDITION-2026-CONTRACT.md` | Complete, 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | Assignment context only, 216–290 | `F49DE88FC33093390FD0CC377E7647019F74FD0529F7DCC07B503E559545160E` |

The remaining reads are explicitly limited to navigation, macro definitions,
and the relevant new notation rows. No full reading of the registry or either
complete generated projection is claimed.

| File | Actual read extent | SHA256 |
| --- | --- | --- |
| `handbook/main.tex` | Complete, 1–74; P5 inputs at 28 and 52 | `E9CB5F4EC7A0F0A5A24DAC385B7FC796AE88C2153FD47FD9FD93FA66996D94C7` |
| `handbook/parts/p05.tex` | Complete, 1–55; target input at 23 | `CEDC8587C90D6B1F9A769464156306670C6886F7B6515977EAC946B40F4CCFD2` |
| `handbook/annex/p05-route.tex` | Complete, 1–19; target input at 18 | `DF0556D27BBA393EB40950CC6F18F6559B7FD0458B2A1C628087F1686D44032F` |
| `handbook/restoration/scope-SRC-09262-09327.tex` | Complete, 1–3 | `65DCDECA00CACDD15A4483691054AB980AF87F178750B5852B358BBD16D12604` |
| `handbook/restoration/scope-SRC-09328-09438.tex` | Complete, 1–3 | `3D56970059846AE57BC9A1C4E150224B1D4A80F7EB7CC497BB65E33F529BD6A3` |
| `handbook/handbook.sty` | 300–360 and 1585–1646; targeted environment locator matches at 496–497 | `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44` |
| `handbook/registry/symbols.csv` | All nineteen appended physical lines 1025–1043; selected existing P5 matches | `6D8CF296B7CA8A007D8A493B6B9617F1CCC2E03746BF011DE16B462111DCF300` |
| `tmp/edition-2026-p5-numeral/symbols-tables.tex` | 450–483; all nineteen new projections at 462–480 | `936FCA81EF62F6E29932A9147B515CF5F703D7DAD261C797A640E62FEC49C621` |
| `tmp/edition-2026-p5-numeral/symbol-index.tex` | All nineteen corresponding rows: 352, 467, 505, 506, 508, 517, 534, 537, 538, 541, 545, 557, 606, 617, 812, 866, 867, 920, 960 | `75FB1AB940067DFC72E9EE06BC6DD76BDF7521DB99872E2B21984CFA9E872B99` |

The lead supplied final route and notation hashes before closure; direct local
hash reads agreed. A broad environment-locator search produced truncated
unrelated matches; it was followed by the focused style reads above. That
search is not counted as a complete read of any additional file.

### Located findings and coverage

In this table, **body** and **annex** mean the two target numeral-builder files.
Each PASS concerns the assigned text promise, not a build or formalized proof.

| Requirement | Standing | Exact evidence and assessment |
| --- | --- | --- |
| Selected checker and proof sort | PASS | Body 4–10, 42–45 and 474–491 identify the direct tag-19 selected graph. The owning definition is checker body 396–417. Packing remains `N_19(N_15(R),0)`; the proof uses the stated characteristic factors and unique graph outputs. No internal equality with the earlier arbitrary representative is asserted. |
| Definition before use, domains, total values | PASS | Body 12–76 defines local constructor operations, the numerical guard expansions, iteration, packaging, and the three-field substitution table. Body 104–179 fixes join arities, parameter projections, failed-pattern defaults and the separately fixed congruence contexts. Body 287–290 restricts open-term success to the stated numeral/variable/successor domain. Body 315–338 supplies every Clash success premise. |
| No-renaming substitution prerequisite | PASS | The entire body assertion at 78–102 is proved by annex 4–118. The proof supplies the continuation/value-stack execution equation at 33–72 for the actual machine, uses its absorbing completed state and concrete bound, then proves both success-domain clauses and guarded numeral invariance at 74–98. Checker body 181–233 supplies every command, type guard and bound used. The invalid replacement example prevents an unguarded assertion on code zero. |
| Raw joins, repeated copies and open leaves | PASS | Body 104–198 and annex 120–213 supply disjoint offsets, preservation of old row bits, exact filtered open-list updates and parent counts. The existing offset and row induction at checker annex 317–454 is actually applicable without a sentence-root premise at its intermediate stages. The new proof explicitly adds the required last-row local test. A copied row receives one parent; repetitions duplicate trees. |
| Exact rule parameters and equality operations | PASS | Body 128–179 specifies the actual tag-13/14/15/16, tag-7/9/10, and tag-18/19 templates, including matrices, terms, indices and labels. Compare checker body 343–373. Annex 182–201 checks equality premise order, fresh holes, positive-before-negative contradiction, and nonvacuous discharge. The generic templates carry side-condition hypotheses instead of declaring every numerical call a successful proof. |
| Arithmetic leaves and canonical induction | PASS | Body 200–264 gives complete `A_j` instance chains, both matrices, both `IndAx` leaves, and the explicit `D_Z,D_L` records. Annex 215–301 checks the base, step, parameter prefix, literal roots, one surviving temporary assumption per step, and the final nine-entry leaf list. Standard-PA body 24–34 and 45–82 supply the exact seven constants and canonical constructor; checker body 259–295 supplies its selected description. Source PA at inherited-09175-09187 2–11 permits the used full-induction matrices. |
| Numeral arithmetic and both addition orientations | PASS | Body 266–313 and annex 303–381 provide all four recurrences and their Safe invariant. Addition and multiplication use the displayed recursion on the second argument. Right/left open-term equations are raw formula-root invariants until later closed. The only extra arithmetic leaves are the two explicit induction axioms. |
| Equality, disequality, both signs of both comparisons | PASS | Body 315–425 and annex 383–521 supply each listed success branch and failure value. Peeling retains the original marked equality; weak and strict positive cases name their witnesses; negative cases use `i+3`, marked major/minor assumptions, the appropriate right/left addition orientation, tag 16 and tag 9. The all-variable test at checker body 361–368 is checked against the major, bottom, and every surviving open formula at annex 470–499. |
| Literal comparison convention and binder retention | PASS | Body 351–355 agrees literally with inherited-08306-08438 28–59: weak witnesses are left addends and strict successor witnesses are right addends. Body 452–465 and annex 585–621 retain the binder chosen for the original terms and use a distinct fresh equality hole. Numeral substitution does not recompute the least available binder or merely preserve an alpha-equivalence class. |
| Fixed terms, literal antecedents, dependent numerical outputs | PASS | Body 427–492 and annex 523–644 specify a separate finite description for each fixed term/literal, its numerical value, its literal code and its raw proof. Both equality-elimination transports are explicit. Annex 568–583 identifies numerical A and M with the PA term operations before deriving the table condition from the original arithmetic antecedent. The graph construction is inherited-09262-09327 76–158, with the full internal proof at internal-proof-predicate 229–310. |
| Zero, empty and malformed boundaries | PASS | Body 54–75 and annex 92–98 handle invalid expression/replacement types. The arithmetic zero recurrences are body 271, 274, 279 and 282. Annex 415–422 handles zero peeling; 434–437 handles equality; 509–519 handles negated bottom, empty leaves, equal endpoints and the `m=n=0` comparison. Body 470–491 and annex 629–638 handle positive bottom and the empty parameter tuple without claiming a successful proof on the false case. Empty raw records remain invalid. |
| Six complete proof routes | PASS | The reciprocal routes are listed below. Main 28/52 reaches the two P5 routes, whose target inputs follow their immediate checker prerequisites. The actual style creates forward links at handbook.sty 340–346 and back-links at 1613–1623. All six annex items contain their promised proof content. |
| Typed notation intake and candidate lookup text | PASS | Registry 1025–1043 covers all new constructor groups, table fields, joins, derived records, comparisons, recurrence names, Safe, fixed descriptions and execution notation. Candidate table 462–480 preserves those meanings and anchors; all nineteen index entries name the corresponding anchors 01025–01043. Escaped ampersand/hash signs and the displayed math wrappers are preserved in the inspected TeX source. |
| No false D3, GL or PT-1 closure | PASS | Body 494–501 and annex 634–642 leave bounded connective/quantifier construction and evidence-to-proof work open. The selected checker already makes the same boundary at its body 507–523 and annex 531–536. NOW-03a is therefore a prerequisite component; no text here supplies or claims PT-1, GL, or Solovay completion. |

### Exact result and annex mapping

| Body result and full statement extent | Reciprocal proof item and full extent |
| --- | --- |
| `thm:p05-builder-nocapture`, 78–102 | `annex:p5.builder-nocapture`, 4–118 |
| `thm:p05-builder-row-templates`, 182–198 | `annex:p5.builder-row-templates`, 120–213 |
| `thm:p05-builder-left-addition`, 247–264 | `annex:p5.builder-left-addition`, 215–301 |
| `thm:p05-numeral-arithmetic-builders`, 293–313 | `annex:p5.numeral-arithmetic-builders`, 303–381 |
| `thm:p05-numeral-literal-builders`, 400–425 | `annex:p5.numeral-literal-builders`, 383–521 |
| `thm:p05-fixed-term-literal-builders`, 474–492 | `annex:p5.fixed-term-literal-builders`, 523–644 |

### Nonblocking publication clarification

**PUB-01 — Make the MP argument exchange explicit when the prose is next
edited.** Body 196–197 and annex 203–208 identify the packed raw join with
the selected `mp_19`. The raw template at body 141–142 accepts the antecedent
tree first and the implication tree second; the existing checker definition
at checker body 452–465 accepts the implication proof first and antecedent
proof second. Under the stated sentence/axiom hypotheses, the precise interface
equation is

```text
pack(MP_row(R,S)) = mp_19(pack(S),pack(R)).
```

This displayed equation is a reviewer recommendation, not a source quotation.
The present definitions and proof already fix both orders correctly, so the
observation does not invalidate a constructor or require reopening the frozen
body for this review. It would make reuse of the two adjacent APIs easier.

### Required next action

The lead should combine this independently returned verdict with the other
required fresh reviews, keeping their conclusions independent until submission.
If all content gates pass at the same frozen identities, promote the reviewed
notation projections through the existing shared workflow and perform the
separate scoped static/build/render/visual and admission gates. Any substantive
change to a target or its used dependency requires review of the affected
scope. NOW-03b may use only the resulting accepted literal-constructor
interface; its finite-case and bounded-quantifier proof records remain owed.

Publication output and admission: **UNRESOLVED in this report's scope**.
PT-1, D3, and later GL/Solovay completion: **UNRESOLVED; not supplied by
NOW-03a**. No source, shared route, symbol registry, generated projection,
restoration, or acceptance record was changed by this reviewer.
