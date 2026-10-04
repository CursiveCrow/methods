# TeX syntax repairs

This log records real working-tree manuscript edits made to get
`handbook/main.tex` building with TeX Live 2025. Temporary edits inside
`tmp/build-fix/run-*/handbook` build copies are not manuscript repairs.

## 2026-10-03

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p02/free-boolean-algebra-and-completeness.tex`
  Line: 197
  Error fixed: `Illegal unit of measure (pt inserted)` / `Missing = inserted for \ifdim` after `\\` in an `array`, because the next row began with `[\gamma_1]_P` and was parsed as an optional row-spacing argument.
  Before: `[\gamma_1]_P\wedge\cdots\wedge[\gamma_n]_P\leq_L b`
  After: `{}[\gamma_1]_P\wedge\cdots\wedge[\gamma_n]_P\leq_L b`

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/presentations/har2001-c18.tex`
  Lines: 76-77
  Error fixed: `Illegal unit of measure (pt inserted)` / `Missing number, treated as zero` after `\\` in an `array`, because bracketed formula rows were parsed as optional row-spacing arguments.
  Before: `[A\lor B]&=&[A]\cup[B]&[\bot]&=&\varnothing,\\`
  After: `{}[A\lor B]&=&[A]\cup[B]&[\bot]&=&\varnothing,\\`
  Before: `[\forall x\in X.A_x]&=&\Pi x:X.[A_x]&`
  After: `{}[\forall x\in X.A_x]&=&\Pi x:X.[A_x]&`

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p07/combinatory-abstraction.tex`
  Lines: 132-137
  Error fixed: `Extra alignment tab has been changed to \cr` and display-state cascade from an unclosed display around the expansion equations.
  Before: `\begin{split} ... E(x)&=x,& E(PQ)&=E(P)E(Q),\\ ... \end{split}`
  After: `\begin{aligned} ... E(x)&=x,& E(PQ)&=E(P)E(Q),\\ ... \end{aligned}` followed by `\]`

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p07/combinatory-abstraction.tex`
  Lines: 99-105, 135-141
  Error fixed: display environment mismatch / unclosed display cascades.
  Before: `\begin{split} ... \end{split}` with multi-column alignment and missing closing display delimiter.
  After: `\begin{aligned} ... \end{aligned}` with the closing `\]` restored.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p10/presentations/n-d-023-bvm.tex`
  Line: 40
  Error fixed: `Bad math environment delimiter` cascade from prose continuing inside `\[`.
  Before: `\end{gathered}` followed immediately by prose.
  After: `\end{gathered}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p10/presentations/n-d-023-source-01.tex`
  Lines: 139, 366, 434, 1036
  Error fixed: repeated `Bad math environment delimiter` / `Missing $ inserted` cascades from unclosed display math blocks.
  Before: `\end{aligned}` followed immediately by prose.
  After: `\end{aligned}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p10/n-d-023-source-01.tex`
  Line: 726
  Error fixed: unclosed display before prose beginning `So \(h:F^*B\to A\)`.
  Before: `\end{aligned}` followed immediately by prose.
  After: `\end{aligned}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p16/rationality-4-2.tex`
  Line: 353
  Error fixed: unclosed display before prose beginning `No assertion`.
  Before: `\end{aligned}` followed immediately by prose.
  After: `\end{aligned}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p17/rationality-10-4.tex`
  Line: 191
  Error fixed: unclosed display before prose beginning `Here \(0<a<1\)`.
  Before: `\end{aligned}` followed immediately by prose.
  After: `\end{aligned}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p17/rationality-9-1.tex`
  Line: 243
  Error fixed: unclosed display before prose beginning `Eve's best replies`.
  Before: `\end{array}` followed immediately by prose.
  After: `\end{array}` followed by `\]` before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/registry/calculi/p10-operational-model.tex`
  Lines: 3-37
  Error fixed: malformed `\hbrule` arguments and side-condition text containing math outside math mode.
  Before: empty-premise rules used `{\none}` as the premises argument and side conditions included raw math such as `n\geq0`, `x\text{ fresh for }H`, and `\text{...}`.
  After: empty premises use `{}`, and side-condition formulas are wrapped in inline math or plain text while retaining `{\none}` only as the fifth argument.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p19/rationality-6-4.tex`
  Lines: 173-174
  Error fixed: guarded source macro use in inline math.
  Before: `\(v\in\R\)` and `\(c_1,c_0\in\R\)`.
  After: `\(v\in\mathbb R\)` and `\(c_1,c_0\in\mathbb R\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/grasp-and-minisat-originals.tex`
  Lines: 198, 305-306
  Error fixed: `Missing $ inserted` from raw subscripts/math commands in prose.
  Before: `x_21/x_31`; `\texttt{calcReason(\bot_{lit})}`
  After: `\(x_{21}/x_{31}\)`; `\texttt{calcReason(}\(\bot_{\mathrm{lit}}\)\texttt{)}`

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/presentations/har2001-c18-polynomial-normalizer.tex`
  Lines: 153-156
  Error fixed: raw subscripts and function equations in prose.
  Before: `Chi0=0_A, chi(one)=1_A, ... In the Nat instance chi n=n.`
  After: `\(\chi(0)=0_A\), \(\chi(\mathsf{one})=1_A\), ... In the Nat instance \(\chi(n)=n\).`

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex`
  Line: 378
  Error fixed: raw subscript in prose.
  Before: `\emph{new} K_e still has zero/one range.`
  After: `\emph{new} \(K_e\) still has zero/one range.`

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/presentations/har2001-c18-autarkic.tex`
  Lines: 297-310
  Error fixed: raw subscripts and formula fragments in prose.
  Before: `Var i`, `e_s`, `e_t`, `P(Add s t)`, `P(Mul s t)`, and `nu,mu`.
  After: `Var \(i\)`, `\(e_s\)`, `\(e_t\)`, `\(P(\operatorname{Add}\ s\ t)\)`, `\(P(\operatorname{Mul}\ s\ t)\)`, and `\(\nu,\mu\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/presentations/har2001-c18-kprime.tex`
  Lines: 382-390
  Error fixed: raw powers, inequalities, and formulas in prose.
  Before: `e with one<e and e<=7`, `S^8 k`, `S k<=O`, `k<O`.
  After: `\(e\) with \(\mathsf{one}<e\) and \(e\leq7\)`, `\(S^8 k\)`, `\(S k\leq O\)`, `\(k<O\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/presentations/har2001-c18-polynomial-normalizer.tex`
  Lines: 476-492
  Error fixed: raw subscripts and function expressions in prose.
  Before: `Q_W`, `Q_Pp=Z`, `Add(\(Q_R\) row)(\(Q_P\) s)`, `Sum(single(c,w),s)=Ins(c,w,s)`.
  After: `\(Q_W\)`, `\(Q_Pp=Z\)`, `\(\operatorname{Add}(Q_R\ \mathit{row})(Q_P\ s)\)`, `\(\operatorname{Sum}(\operatorname{single}(c,w),s)=\operatorname{Ins}(c,w,s)\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/presentations/har2001-c18-primitive-recursive-compiler.tex`
  Lines: 43-64
  Error fixed: raw subscripts and math commands in prose.
  Before: `p_e`, `K_e`, `b\_eq`, `v=0`, `v=1`, `v`.
  After: `\(p_e\)`, `\(K_e\)`, `\(\mathsf{b\_eq}\)`, `\(v=0\)`, `\(v=1\)`, `\(v\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/n-c-035-05-basic-completeness.tex`
  Lines: 3-39, 106-112, 263-282
  Error fixed: raw arrows, underscores, exponents, and equation fragments in prose.
  Before: examples include `q`, `H_q`, `x->y`, `f(x)->f(f(x))`, `s|_p`, `l->r`, `w=y`, `S={v=g(y),w=y}`.
  After: examples are wrapped as `\(q\)`, `\(H_q\)`, `\(x\to y\)`, `\(f(x)\to f(f(x))\)`, `\(s|_p\)`, `\(l\to r\)`, `\(w=y\)`, `\(S=\{v=g(y),w=y\}\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/n-c-035-05-combination.tex`
  Lines: 57-460
  Error fixed: raw subscripts and component-theory formula fragments in prose.
  Before: examples include `E_i`, `F_i`, `N_i^k`, `P_i`, `f_j`, `c_z`, and coverage equations outside math mode.
  After: those symbolic fragments are wrapped in inline math while preserving the surrounding prose.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/n-c-035-05-narrowing.tex`
  Lines: 126, 347-358
  Error fixed: raw subscripts and formula fragments in prose.
  Before: examples include `P_B`, `f(v_{k+1})=a`, `k+1`, `f(0)=f(v_k)`, `a=a`, `y-image`.
  After: those symbolic fragments are wrapped in inline math while preserving the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/n-c-035-05-ac.tex`
  Lines: 150-217
  Error fixed: raw subscripts and AC comparison formulas in prose.
  Before: examples include `Q`, `w_c`, `Dw_c=d_c`, `w_q`, `h_j`, `h_i`, `P_c`, and `((p,I)=(q,J))`.
  After: those symbolic fragments are wrapped in inline math while preserving the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p07/combinatory-abstraction.tex`
  Line: 68
  Error fixed: `Display math should end with $$` / `Bad math environment delimiter` from an extra display closer.
  Before: two consecutive `\]` lines after the `\mathcal A_x` aligned display.
  After: one `\]` closes the display before the prose.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/cdcl-uip-and-watched-literals.tex`
  Line: 154
  Error fixed: `Extra alignment tab has been changed to \cr` in a three-column `array`.
  Before: `\omega_6=\{x_5,x_6\}.&&`
  After: `\omega_6=\{x_5,x_6\}.`

## 2026-10-03 (session 2)

These eight repairs had been made only inside the `tmp/build-fix/run-6`
build copy and were absent from the working tree (fresh run-7 copy
reproduced every error). They are now applied to the real working tree;
pre-edit originals are kept in `tmp/build-fix/pre-session7-backup/`.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p05/certified-incompleteness.tex`
  Line: 5
  Error fixed: `Package handbook Error: source ND command outside an inherited restoration scope` (and same for `\FOL`).
  Before: `\(\ND_{\FOL}\)`
  After: `\(\mathsf{ND}_{\mathsf{FOL}}\)` (exactly the expansions of `\ND` and `\FOL` in handbook.sty).

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p08/presentations/n-b-007-01.tex`
  Line: 172
  Error fixed: `Missing $ inserted` / `Display math should end with $$` / `\begin{equation*} ... ended by` from an unclosed `\[`.
  Before: `\end{gathered}` followed immediately by prose.
  After: `\end{gathered}` followed by `\]`.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/presentations/n-c-035-05-hereditary.tex`
  Line: 25
  Error fixed: `Bad math environment delimiter` / `You can't use \spacefactor in math mode` / `Missing $ inserted` cascade from an unclosed `\[`.
  Before: `\end{aligned}` followed immediately by prose.
  After: `\end{aligned}` followed by `\]`.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p12/presentations/n-c-035-05.tex`
  Lines: 668, 733, 741, 805
  Error fixed: `Bad math environment delimiter` cascades (lines 668-677, 733-761, 803-812) from four unclosed `\[` displays; also the trailing `\begin{hbexample} ... ended by \end{document}` at main.tex:85.
  Before: each of the four `\end{aligned}` lines followed immediately by prose.
  After: each followed by `\]`.

- File: `C:/Dev/the-methods-of-reason/handbook/parts/p14/symbols-terminology-and-glossary.tex`
  Line: 94
  Error fixed: `Package handbook Error: source Mod/Th command outside an inherited restoration scope`.
  Before: `\(\Mod(T)\), \(\Th(\mathcal M)\) &`
  After: `\(\operatorname{Mod}(T)\), \(\operatorname{Th}(\mathcal M)\) &` (exact handbook.sty expansions; the detokenized command-name column is unchanged).

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p07/n-c-027-01.tex`
  Lines: 559-624
  Error fixed: `Missing $ inserted` for raw `^` in prose complexity bounds (lines 564-623).
  Before: raw `n-term i-row`, `n-1`, `O(n)`, `O(n^2)`, `O(n^3)`, `O(n^4)`, `n=2`, `O(m^3)`, `m=2`, `k-stage`, `k`, `m=n-k`, `F`, `H`, `O(log(n+2))`, `O(N log(n+2))`, `O(N)`, `O(n^5 log(n+2))`.
  After: each wrapped in inline math, e.g. `\(n\)-term \(i\)-row`, `\(O(n^2)\)`, `\(O(\log(n+2))\)`, `\(O(N\log(n+2))\)`, `\(O(n^5\log(n+2))\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p12/presentations/har2001-c18-frameworks.tex`
  Lines: 165-166, 174-176
  Error fixed: `Missing $ inserted` for raw subscripts in prose (165, 173).
  Before: `h_j`, `imp-intr p q f`, `h:T(p)`, `fh`, `forall-intr F f`, `z:A`, `fz`, `T(Fz)`, `fresh z`.
  After: `\(h_j\)`, `imp-intr \(p\ q\ f\)`, `\(h:T(p)\)`, `\(fh\)`, `forall-intr \(F\ f\)`, `\(z:A\)`, `\(fz\)`, `\(T(Fz)\)`, `fresh \(z\)`.

- File: `C:/Dev/the-methods-of-reason/handbook/annex/p17/hierarchical-task-network-reasoning.tex`
  Lines: 321, 326
  Error fixed: `Extra alignment tab has been changed to \cr` (split permits one `&` per row; the display has four columns).
  Before: `\begin{split}` ... `\end{split}`
  After: `\begin{aligned}` ... `\end{aligned}`
