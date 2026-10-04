# Editorial reference types: bounded independent review

## Retrieved Content

### Source 1: `handbook/handbook.sty`, lines 461–504

```tex
% \hb@beginresult{<Name>}{<label>}{<status>}{<title>}{<bodyfont>}{<index 0/1>}
\long\def\hb@beginresult#1#2#3#4#5#6{%
  \par\addvspace{\medskipamount}%
  \hbparsestatus{#3}%
  \refstepcounter{hbitem}%
  \hb@splittitle{#4}%
  \noindent{\bfseries #1~\thehbitem\ (\hbTitleDisp).}%
  \label{#2}%
  \ifnum#6=1\relax
    \expandafter\index\expandafter{\hb@titleindex}%
  \fi
  \hb@requirepartidentity
  \immediate\write\hb@statusout{#2|\hb@statusform|\hb@statustarget|\hbcurrentpartid}%
  \enspace#5\ignorespaces}
\def\hb@endresult{%
  \par\nobreak
  {\noindent\small\itshape\hb@taglinetext\par}%
  \addvspace{\medskipamount}}

% \hb@beginplain{<Name>}{<label>}{<title>}{<bodyfont>}{<index 0/1>}
\long\def\hb@beginplain#1#2#3#4#5{%
  \par\addvspace{\medskipamount}%
  \refstepcounter{hbitem}%
  \hb@splittitle{#3}%
  \noindent{\bfseries #1~\thehbitem\ (\hbTitleDisp).}%
  \label{#2}%
  \ifnum#5=1\relax
    \expandafter\index\expandafter{\hb@titleindex}%
  \fi
  \enspace#4\ignorespaces}
\def\hb@endplain{\par\addvspace{\medskipamount}}

% Each editorial environment shares hbitem for numbering but records its own
% reference kind.  The local alias is set before refstepcounter and ends with
% the environment group; it changes neither source counters nor proof status.
\newenvironment{hbtheorem}[3]{\crefalias{hbitem}{theorem}\hb@beginresult{Theorem}{#1}{#2}{#3}{\itshape}{1}}{\hb@endresult}
\newenvironment{hblemma}[3]{\crefalias{hbitem}{lemma}\hb@beginresult{Lemma}{#1}{#2}{#3}{\itshape}{0}}{\hb@endresult}
\newenvironment{hbcorollary}[3]{\crefalias{hbitem}{corollary}\hb@beginresult{Corollary}{#1}{#2}{#3}{\itshape}{0}}{\hb@endresult}
\newenvironment{hbdefinition}[2]{\crefalias{hbitem}{definition}\hb@beginplain{Definition}{#1}{#2}{\upshape}{1}}{\hb@endplain}
\newenvironment{hbconvention}[2]{\crefalias{hbitem}{convention}\hb@beginplain{Convention}{#1}{#2}{\upshape}{0}}{\hb@endplain}
\newenvironment{hbmethod}[2]{\crefalias{hbitem}{method}\hb@beginplain{Method}{#1}{#2}{\upshape}{0}}{\hb@endplain}
\newenvironment{hbexample}[2]{\crefalias{hbitem}{example}\hb@beginplain{Example}{#1}{#2}{\upshape}{0}}{\hb@endplain}
\newenvironment{hbwarning}[2]{\crefalias{hbitem}{warning}\hb@beginplain{Warning}{#1}{#2}{\upshape}{1}}{\hb@endplain}
\newenvironment{proofboundary}[2]{\crefalias{hbitem}{proofboundary}\hb@beginplain{Proof boundary}{#1}{#2}{\upshape}{1}}{\hb@endplain}
```

### Source 2: `handbook/handbook.sty`, lines 510–524

```tex
\newenvironment{definition}[1][]{%
  \ifhb@inheritedrestoration\else
    \PackageError{handbook}{source definition environment outside an inherited
      restoration scope}%
      {Editorial definitions use hbdefinition.  The source environment is
       reserved for unchanged, provenance-scoped inherited artifacts.}%
  \fi
  \par\addvspace{\medskipamount}%
  \crefalias{hbitem}{definition}%
  \refstepcounter{hbitem}%
  \noindent{\bfseries Definition~\thehbitem
    \if\relax\detokenize{#1}\relax.\else\ (#1).\fi}%
  \if\relax\detokenize{#1}\relax\else\index{#1}\fi
  \enspace\upshape\ignorespaces
}{\hb@endplain}
```

### Source 3: `handbook/handbook.sty`, lines 1807–1845

```tex
\RequirePackage[hidelinks,pdfusetitle]{hyperref}
\RequirePackage[nameinlink,noabbrev]{cleveref}
\crefname{definition}{definition}{definitions}
\Crefname{definition}{Definition}{Definitions}
\crefname{theorem}{theorem}{theorems}
\Crefname{theorem}{Theorem}{Theorems}
\crefname{lemma}{lemma}{lemmas}
\Crefname{lemma}{Lemma}{Lemmas}
\crefname{corollary}{corollary}{corollaries}
\Crefname{corollary}{Corollary}{Corollaries}
\crefname{convention}{convention}{conventions}
\Crefname{convention}{Convention}{Conventions}
\crefname{method}{method}{methods}
\Crefname{method}{Method}{Methods}
\crefname{example}{example}{examples}
\Crefname{example}{Example}{Examples}
\crefname{warning}{warning}{warnings}
\Crefname{warning}{Warning}{Warnings}
\crefname{proofboundary}{proof boundary}{proof boundaries}
\Crefname{proofboundary}{Proof boundary}{Proof boundaries}
\crefname{annexitem}{proof item}{proof items}
\Crefname{annexitem}{Proof item}{Proof items}
\crefname{hbsourcetheorem}{theorem}{theorems}
\Crefname{hbsourcetheorem}{Theorem}{Theorems}
\crefname{hbsourcelemma}{lemma}{lemmas}
\Crefname{hbsourcelemma}{Lemma}{Lemmas}
\crefname{hbsourcecorollary}{corollary}{corollaries}
\Crefname{hbsourcecorollary}{Corollary}{Corollaries}
\crefname{hbsourceconvention}{convention}{conventions}
\Crefname{hbsourceconvention}{Convention}{Conventions}
\crefname{hbsourceremark}{remark}{remarks}
\Crefname{hbsourceremark}{Remark}{Remarks}
\providecommand\theHchapter{\arabic{chapter}}
% overwrite the kernel-provided \theH* (defined by \newcounter since 2022)
\def\theHhbitem{\theHchapter.item.\arabic{hbitem}}
\def\theHhbsysentry{\theHchapter.entry.\arabic{hbsysentry}}
\def\theHannexitem{\theHchapter.annexitem.\arabic{annexitem}}
\def\theHhbsheet{sheet.\arabic{hbsheet}}
\def\theHhbrule{rule.\arabic{hbrule}}
```

### Source 4: installed `C:/Program Files/MiKTeX/tex/latex/cleveref/cleveref.sty`, lines 1277–1278

```tex
\newcommand\crefalias[2]{%
  \expandafter\def\csname cref@#1@alias\endcsname{#2}}%
```

### Source 5: installed `cleveref.sty`, lines 2044–2062

```tex
    \let\cref@old@H@refstepcounter\H@refstepcounter%
    \def\H@refstepcounter#1{%
      \cref@old@H@refstepcounter{#1}%
      \cref@constructprefix{#1}{\cref@result}%
      \@ifundefined{cref@#1@alias}%
        {\def\@tempa{#1}}%
        {\def\@tempa{\csname cref@#1@alias\endcsname}}%
      \protected@edef\cref@currentlabel{%
        [\@tempa][\arabic{#1}][\cref@result]%
        \csname p@#1\endcsname\csname the#1\endcsname}}%
    \let\refstepcounter@noarg\cref@old@refstepcounter%
    \def\refstepcounter@optarg[#1]#2{%
      \cref@old@refstepcounter{#2}%
      \@ifundefined{cref@#1@alias}%
        {\def\@tempa{#1}}%
        {\def\@tempa{\csname cref@#1@alias\endcsname}}%
      \protected@edef\cref@currentlabel{%
        \expandafter\cref@override@label@type%
          \cref@currentlabel\@nil{\@tempa}}}%
```

### Source 6: installed `C:/Program Files/MiKTeX/tex/latex/firstaid/latex2e-first-aid-for-external-files.ltx`, lines 208–220

```tex
      \AddToHook{begindocument}[cleveref]{%
         \def\label@noarg#1{%
          \cref@old@label{#1}%
          \@bsphack%
          \protected@edef\@tempa{{page}{\the\c@page}}%   <--- should be protected
          \setcounter{page}{1}%
          \protected@edef\@tempb{\thepage}%              <--- should be protected
          \expandafter\setcounter\@tempa%
          \cref@constructprefix{page}{\cref@result}%
          \protected@write\@auxout{}%
            {\string\newlabel{#1@cref}{{\cref@currentlabel}%
            {[\@tempb][\arabic{page}][\cref@result]\thepage}{}{}{}}}% <----- five
          \@esphack}%
```

### Source 7: installed first-aid file, lines 237–256

```tex
       \newcommand\firstaid@cref@smugglelabel{\let\cref@currentlabel\cref@gcurrentlabel@temp}
       \newcommand\firstaid@cref@updatelabeldata[1]{%
        \cref@constructprefix{#1}{\cref@result}%
         \@ifundefined{cref@#1@alias}%
           {\def\@tempa{#1}}%
           {\def\@tempa{\csname cref@#1@alias\endcsname}}%
         \protected@xdef\cref@gcurrentlabel@temp{%
           [\@tempa][\arabic{#1}][\cref@result]%
           \csname p@#1\expandafter\endcsname\csname the#1\endcsname}%
         \aftergroup\firstaid@cref@smugglelabel
           }
       \newif\iftag@
       \AddToHook{label}[firstaid/cleveref]
         {\ifx
           \@currentcounter\@empty
          \else
           \iftag@\else
           \firstaid@cref@updatelabeldata{\@currentcounter}%
           \fi
          \fi}
```

### Source 8: installed `C:/Program Files/MiKTeX/tex/latex/base/latex.ltx`, lines 15563–15572

```tex
\protected\def\begin#1{%
  \UseHook{env/#1/before}%
  \@ifundefined{#1}%
    {\def\reserved@a{\@latex@error{Environment #1 undefined}\@eha}}%
    {\def\reserved@a{\def\@currenvir{#1}%
        \edef\@currenvline{\on@line}%
        \@execute@begin@hook{#1}%
        \csname #1\endcsname}}%
  \@ignorefalse
  \begingroup\@endpefalse\reserved@a}
```

### Source 9: installed `latex.ltx`, lines 15601–15610

```tex
\@namedef{end }#1{%
  \romannumeral
    \IfHookEmptyTF{env/#1/end}%
        {\expandafter\z@}%
        {\z@\UseHook{env/#1/end}}%
    \csname end#1\endcsname\@checkend{#1}%
    \endgroup
    \UseHook{env/#1/after}%
    \if@ignore\@ignorefalse\ignorespaces\fi
}
```

### Source 10: `tmp/pdfs/edition-2026-abduction-preferences/reference-types-check.aux`, lines 8–42

```tex
\newlabel{def:fixture-definition}{{1.1}{1}{Reference Metadata Check}{hbitem.1.item.1}{}}
\newlabel{def:fixture-definition@cref}{{[definition][1][1]1.1}{[1][1][]1}{}{}{}}
\newlabel{thm:fixture-theorem}{{1.2}{1}{Reference Metadata Check}{hbitem.1.item.2}{}}
\newlabel{thm:fixture-theorem@cref}{{[theorem][2][1]1.2}{[1][1][]1}{}{}{}}
\newlabel{thm:fixture-lemma}{{1.3}{1}{Reference Metadata Check}{hbitem.1.item.3}{}}
\newlabel{thm:fixture-lemma@cref}{{[lemma][3][1]1.3}{[1][1][]1}{}{}{}}
\newlabel{thm:fixture-corollary}{{1.4}{1}{Reference Metadata Check}{hbitem.1.item.4}{}}
\newlabel{thm:fixture-corollary@cref}{{[corollary][4][1]1.4}{[1][1][]1}{}{}{}}
\newlabel{def:fixture-convention}{{1.5}{1}{Reference Metadata Check}{hbitem.1.item.5}{}}
\newlabel{def:fixture-convention@cref}{{[convention][5][1]1.5}{[1][1][]1}{}{}{}}
\newlabel{def:fixture-method}{{1.6}{1}{Reference Metadata Check}{hbitem.1.item.6}{}}
\newlabel{def:fixture-method@cref}{{[method][6][1]1.6}{[1][1][]1}{}{}{}}
\newlabel{def:fixture-example}{{1.7}{1}{Reference Metadata Check}{hbitem.1.item.7}{}}
\newlabel{def:fixture-example@cref}{{[example][7][1]1.7}{[1][1][]1}{}{}{}}
\newlabel{def:fixture-warning}{{1.8}{1}{Reference Metadata Check}{hbitem.1.item.8}{}}
\newlabel{def:fixture-warning@cref}{{[warning][8][1]1.8}{[1][1][]1}{}{}{}}
\newlabel{def:fixture-boundary}{{1.9}{1}{Reference Metadata Check}{hbitem.1.item.9}{}}
\newlabel{def:fixture-boundary@cref}{{[proofboundary][9][1]1.9}{[1][1][]1}{}{}{}}
\newlabel{thm:fixture-theorem-after-plain}{{1.10}{1}{Reference Metadata Check}{hbitem.1.item.10}{}}
\newlabel{thm:fixture-theorem-after-plain@cref}{{[theorem][10][1]1.10}{[1][1][]1}{}{}{}}
\newlabel{annex:fixture-theorem}{{1.1}{1}{Reference Metadata Check}{annexitem.1.annexitem.1}{}}
\newlabel{annex:fixture-theorem@cref}{{[annexitem][1][1]1.1}{[1][1][]1}{}{}{}}
\newlabel{annex:fixture-lemma}{{1.2}{2}{Reference Metadata Check}{annexitem.1.annexitem.2}{}}
\newlabel{annex:fixture-lemma@cref}{{[annexitem][2][1]1.2}{[1][1][]2}{}{}{}}
\newlabel{annex:fixture-corollary}{{1.3}{2}{Reference Metadata Check}{annexitem.1.annexitem.3}{}}
\newlabel{annex:fixture-corollary@cref}{{[annexitem][3][1]1.3}{[1][2][]2}{}{}{}}
\@writefile{toc}{\contentsline {section}{\numberline {1.1}Alphabet and grammar}{2}{section.1.1}\protected@file@percent }
\newlabel{sec:prop-syntax-semantics-01}{{1.1}{2}{Alphabet and grammar}{section.1.1}{}}
\newlabel{sec:prop-syntax-semantics-01@cref}{{[section][1][1]1.1}{[1][2][]2}{}{}{}}
\newlabel{lem:paren-count}{{1.14}{3}{Parenthesis counting}{hbsourcelemma.1.item.14}{}}
\newlabel{lem:paren-count@cref}{{[hbsourcelemma][14][]1.14}{[1][3][]3}{}{}{}}
\newlabel{thm:prop-unique-readability}{{1.15}{4}{Unique readability}{hbsourcetheorem.1.item.15}{}}
\newlabel{thm:prop-unique-readability@cref}{{[hbsourcetheorem][15][]1.15}{[1][3][]4}{}{}{}}
\newlabel{def:fixture-after-source}{{1.17}{4}{Reference Metadata Check}{hbitem.1.item.17}{}}
\newlabel{def:fixture-after-source@cref}{{[definition][17][1]1.17}{[1][4][]4}{}{}{}}
```

### Source 11: `reference-types-check.hbstatus`, lines 1–4

```text
thm:fixture-theorem|proved|annex:fixture-theorem|p02
thm:fixture-lemma|proved|annex:fixture-lemma|p02
thm:fixture-corollary|proved|annex:fixture-corollary|p02
thm:fixture-theorem-after-plain|proved|annex:fixture-theorem|p02
```

### Source 12: `reference-types-check.log`, lines 667–669

```text
) (C:\Program Files\MiKTeX\tex/latex/cleveref\cleveref.sty
Package: cleveref 2018/03/27 v0.21.4 Intelligent cross-referencing
Package cleveref Info: `hyperref' support loaded on input line 2370.
```

### Source 13: `reference-types-check.log`, line 688

```text
==> First Aid for cleveref.sty applied!
```

### Source 14: `reference-types-check.log`, lines 843–844

```text
Output written on C:/Dev\the-methods-of-reason\tmp\pdfs\edition-2026-abduction-
preferences\reference-types-check.pdf (4 pages, 266421 bytes).
```

---

## Supplementary Notes

**Verdict: PASS for the specified editorial reference-type correction.** All nine public editorial environments establish their semantic alias before the shared counter is stepped and retain it through the label write. No defect or unresolved condition was found within this correction's scope.

Review date: 2026-09-07 America/Los_Angeles, with checks completed on 2026-09-08 UTC. Checkout: `C:/Dev/the-methods-of-reason`, branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The checkout contains substantial pre-existing work; HEAD is identification only, not the correction's baseline.

The reviewed style SHA-256 is `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44`. A read-only, in-memory inverse removed exactly nine aliases at the starts of the editorial environments, one three-line comment, and 18 name-registration lines for theorem, lemma, corollary, convention, method, example, warning, proofboundary, and annexitem. Encoding the resulting text back to UTF-8 produced the supplied baseline SHA-256 exactly: `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288`. The two definition name registrations already existed and were retained. This verifies the exact change boundary without treating unrelated repository changes as part of this correction.

### Mechanism and invariants

The installed `cleveref` alias implementation uses a local `\def`, not a global assignment. The installed LaTeX environment implementation opens a group before calling the environment's begin macro and closes it after its end macro. Therefore each added alias is local under the documented `\begin{...}` / `\end{...}` interface. Each subsequent environment also sets its own alias explicitly. The existing source `definition` environment uses the same alias-before-counter pattern.

The active hyperref integration reads `cref@hbitem@alias` when it constructs `\cref@currentlabel`; the number still comes from `\arabic{hbitem}`, its prefix, and `\thehbitem`. The installed first-aid patch also recomputes label metadata from the current counter and active alias at label time. Both shared begin helpers call `\label` before the environment closes, so that patch sees the intended alias. Its five-field label writer explains the additional empty fields in the actual auxiliary records.

The exact inverse confirms that the correction does not alter the shared counter definitions at style lines 377–382, the counter-step calls at lines 465 and 483, the label arguments at lines 468 and 486, the stable part-identity logic at lines 397–459, the result-status parsing and output at lines 464 and 472–473, or the hyperlink formulas at lines 1839–1845. Source definitions and the guarded source wrappers are likewise outside the changed bytes. The alias changes the reference kind; it does not select a new numbering counter, label key, status target, or part owner.

### Observed fixture evidence

The existing 27-line fixture was read in full. Its lines 7–15 exercise all nine editorial kinds; line 16 repeats a theorem after the plain forms. Lines 17–18 exercise mixed lower-case references and an upper-case theorem reference. Lines 19–22 exercise annex targets and their plural reference. Lines 23–26 include the actual `restoration/scope-SRC-01661-01816` wrapper, then an editorial definition and a reference to the inherited lemma. The wrapper itself was read and contains the inherited restoration scope and input of `restoration/inherited-01661-01816`.

Auxiliary lines 8–27 preserve the shared sequence 1.1 through 1.10 and `hbitem.1.item.N` anchors while recording the nine distinct semantic kinds. Lines 37–40 retain both `hbsourcelemma` and `hbsourcetheorem`, including their source anchor prefixes, after the editorial entries. Lines 41–42 then record the following editorial definition as `definition` at 1.17. The source lemma wrapper at style lines 668–676 remains guarded and delegates to `hbsourcelemma`; its declaration at line 551 still shares `hbitem`.

The status output retains all four result IDs, their supplied proof targets, and `p02` ownership. The fixture's repeated theorem deliberately shares a proof target; this review treats that record as metadata exercise, not proof acceptance.

The existing fixture log reports MiKTeX 26.5 and LaTeX2e 2026-06-01, loads the local `handbook.sty`, records cleveref v0.21.4 with hyperref and amsthm support, and reports successful four-page output. A complete text search of the log for `^!`, `Warning`, `undefined`, `multiply defined`, and `destination with the same` returned no matches. The fixture was not rerun during this independent review.

Fixture SHA-256 values: TEX `F56A3750B81D91DF6EC88B5D38A926B59919007C772C2DEF4F6FF1E4223D902E`; AUX `E45CF52651A33561EA1733E5F9730546C90D47266B1240F59EA06ED76B84E8AE`; LOG `988D079E2258DAD5A522B28E9F76796F45447087582F1F5D76EA470777B94743`. The style's modification time was 2026-09-08 01:29:30 UTC; the fixture TEX was modified at 01:30:46 UTC, and its AUX and LOG at 01:30:53 UTC.

### Conditions and evidence limits

This conclusion applies to the documented environment interface, the reviewed style bytes, and the installed package/kernel implementation. It does not cover direct invocation of environment begin macros without LaTeX grouping or later user redefinitions of the reference machinery.

The actual fixture exercises all nine lower-case kinds, one upper-case kind, theorem repetition, annex references, and the source/editorial transition. The remaining capitalized and plural names were checked directly in the registrations; this fixture does not independently exercise every formatting combination. The existing source `definition` pattern was inspected directly, while its unlabeled inherited instances do not supply separate source-definition label records in this fixture.

No preserved pre-correction reference fixture AUX or LOG was found among the reference/baseline files in this fixture directory. Consequently the reported historical count of 11 `hbitem` editorial labels and historical warnings was not treated as independently observed output. The exact inverse and the package implementation support the cause of that reported defect; the current fixture independently verifies the corrected output.

This review creates only this report. No style/manuscript edit, new test, full-book build, or manuscript PDF inspection was performed. The verdict establishes this shared-style correction's reference metadata behavior only; it does not establish manuscript or full-book readiness, mathematical acceptance, visual acceptance, or admission.
