# Bryant 1986: ordering counts, multiplication lower bound, and experiments

## Scope and controlling source

Research date: 2026-09-06. This note supports continued authoring of `handbook/parts/p09/presentations/n-c-017.tex`; it is not a section-acceptance record. The current Bryant subsection was read before this investigation. No manuscript, build, render, software test, or other research file was changed.

The controlling primary source is [Randal E. Bryant, *Graph-Based Algorithms for Boolean Function Manipulation*, annotated electronic author version](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf). Its first-page update identifies the original publication as *IEEE Transactions on Computers* C-35(8), 677-691 (1986), and distinguishes the redrawn figures and later update footnotes. All page numbers below are the author's numbered pages, not IEEE pagination. The PDF has 28 physical pages. The relevant numbered pages coincide with the corresponding one-based physical page numbers.

The mathematical arguments below are independently written derivations. The exact-source landmarks are Section 3.2 and Figure 2, pp. 7-8; Section 3.3, p. 8; Section 5, Table 2, and Figure 11, pp. 19-21; Appendix, Theorem 2 and Lemma 4, pp. 23-24. The appendix argument is reconstructed with an unambiguous order convention and explicit integer rounding.

## 1. A cut in an ordered graph distinguishes residual functions

Fix a finite ordered variable list `v_1,...,v_N`, and an ordered Boolean function graph G. Both terminal vertices count toward graph size when they occur; every vertex is reachable from the root. Reducedness is not needed for the following lower-bound principle.

Fix a cut after `v_c`, where `0 <= c <= N`. For an assignment alpha to `v_1,...,v_c`, follow the graph through every test whose variable lies before or at the cut. Stop at the first terminal, or at the first vertex whose test lies after the cut. The rooted subgraph at that endpoint denotes the residual function obtained by fixing alpha. Consequently, two prefix assignments with distinct residual functions must reach distinct endpoints.

Thus, if a family of prefix assignments induces L pairwise distinct residual functions, G has at least L vertices. This remains true if some variables are skipped, or if some endpoints are terminals. It is the precise graph formulation of the information-storage argument in [Section 3.2, pp. 7-8](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf#page=7).

## 2. Exact counts for Figure 2

Let n be a positive integer. Work on `x_1 < ... < x_(2n)` and define

\[
g_n=\bigvee_{j=1}^{n}(x_{2j-1}\land x_{2j}),
\qquad
h_n=\bigvee_{j=1}^{n}(x_j\land x_{n+j}).
\]

The exact reduced-graph counts, including terminals, are

\[
|G(g_n)|=2n+2,
\qquad
|G(h_n)|=2^{n+1}.
\]

These are the families of [Section 3.2, Figure 2, pp. 7-8](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf#page=7).

### 2.1 Interleaved pairs: 2n+2 vertices

Write

\[
H_j=\bigvee_{r=j}^{n}(x_{2r-1}\land x_{2r}),
\qquad H_{n+1}=0.
\]

For each j, use an `x_(2j-1)` vertex whose low child denotes `H_(j+1)` and whose high child is an `x_(2j)` vertex. The latter has low child `H_(j+1)` and high child 1. The root denotes `H_1=g_n`.

All 2n nonterminal vertices are reachable: earlier pairs can be made false, and the odd variable of the current pair can then be chosen as needed. Both terminals are reachable. Neither vertex type has equal children: `H_(j+1)` is not constant 1, and the even-variable residual can be distinguished from `H_(j+1)` by setting the even variable to 1 while making every later pair false. All nonterminal vertices have different indices, so no two of their rooted subgraphs are isomorphic. The graph is reduced and has exactly 2n+2 vertices. Fixed-order canonicity makes this the unique reduced size.

### 2.2 Separated operand blocks: 2^(n+1) vertices

Put `y_j=x_(n+j)`. Before reading `x_i`, a prefix assignment to `x_1,...,x_(i-1)` selects a subset `A` of `{1,...,i-1}` and leaves the residual

\[
R_{i,A}=\bigvee_{j\in A}y_j
\ \lor\ \bigvee_{j=i}^{n}(x_j\land y_j).
\]

There are exactly `2^(i-1)` distinct such residuals. If two subsets differ at j, setting only `y_j=1` and every other y-variable to zero distinguishes them. Each residual depends on `x_i`: set `y_i=1`, all other y-variables to zero, and vary `x_i`. Therefore each has a distinct root at level `x_i`. The first n levels contain

\[
\sum_{i=1}^{n}2^{i-1}=2^n-1
\]

vertices.

After all x-variables have been read, every subset A of `{1,...,n}` occurs and leaves

\[
Q_A=\bigvee_{j\in A}y_j.
\]

The empty subset gives terminal 0. Every nonempty A gives one nonterminal root testing `y_(min A)`, with high child 1 and low child `Q_(A\setminus{min A})`. These `2^n-1` roots are pairwise distinct: singleton y-assignments distinguish different subsets. Their descendants introduce no other kinds of residual. All are reachable from some full x-prefix. Together with terminals 0 and 1 this gives

\[
(2^n-1)+(2^n-1)+2=2^{n+1}.
\]

In particular, n=3 gives eight vertices for g_3 and sixteen for h_3. For n=1 both counts are four. For n=0 both empty disjunctions are constant 0 and have one vertex; the displayed positive-n formulas must not be applied to that case.

## 3. Complete multiplication lower bound

### 3.1 Statement with exact order and bit conventions

Let `n >= 1`. Define unsigned n-bit integers

\[
a=\sum_{u=1}^{n}a_u2^{u-1},
\qquad
b=\sum_{v=1}^{n}b_v2^{v-1}.
\]

Let `mul_r(a_1,...,a_n,b_1,...,b_n)` be bit r of the full 2n-bit product, with bit 1 least significant. Fix any permutation of the input-variable names as a reading order

\[
w_1<\cdots<w_{2n}.
\]

There exists an output index `r in {1,...,2n-1}` such that every ordered function graph for mul_r in this reading order has at least

\[
2^{q_*}
\quad\text{vertices, where}\quad
q_*=
\left\lceil
\frac{\lceil n/2\rceil^2}{2n-1}
\right\rceil.
\tag{1}
\]

In particular it has at least `2^(n/8)` vertices. The output index may depend on the reading order. The graph need not be reduced.

This proves the appendix's Theorem 2 with explicit rounding; its diagonal-counting step is Lemma 4. [Appendix, pp. 23-24](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf#page=23).

### 3.2 Choose the data operand and the control operand

Cut the reading order after its first n variables. Let t be the number of a-bits before this cut. Then there are `n-t` b-bits before the cut, t b-bits after it, and `n-t` a-bits after it.

If `t >= n/2`, use a as the data operand and b as the control operand. Otherwise exchange their roles; multiplication is commutative. Let A be the set of significance indices of data bits before the cut, and B the set of significance indices of control bits after the cut. In either case

\[
|A|=|B|=p:=\max(t,n-t)\ge\lceil n/2\rceil.
\]

This statement uses significance indices in `{1,...,n}`, not positions in the reading order.

### 3.3 Count pairs on one output diagonal

For `1 <= r <= 2n-1`, put

\[
q_r=|\{(u,v)\in A\times B:u+v-1=r\}|.
\]

Every pair belongs to exactly one such diagonal, so

\[
\sum_{r=1}^{2n-1}q_r=p^2.
\]

Choose r with maximal q_r. Then

\[
q_r\ge
\left\lceil\frac{p^2}{2n-1}\right\rceil
\ge q_*.
\]

Moreover,

\[
\frac{p^2}{2n-1}
\ge\frac{n^2}{4(2n-1)}
>\frac n8,
\]

so the weaker inequality `q_r >= n/8` needed for the source theorem follows. No divisibility assumption on n is required.

For this chosen r, let

\[
A_r=\{u\in A:r-u+1\in B\}.
\]

For each u there is at most one matching v, so `|A_r|=q_r`.

### 3.4 Produce 2^(q_r) distinguishable prefix assignments

For every bit vector alpha indexed by A_r, assign the data bit at index u the value `alpha_u` for all `u in A_r`. Set every other variable before the cut to zero. There are `2^(q_r)` such prefix assignments.

Take two distinct assignments alpha and beta and choose u where they differ. Let `v=r-u+1`, which belongs to B. Give both prefixes the same suffix assignment: set the control bit at significance index v to 1 and every other variable after the cut to zero.

All control bits before the cut were already set to zero. The complete control operand is therefore exactly `2^(v-1)`. Integer multiplication by it is a left shift, and

\[
\operatorname{mul}_r
=\operatorname{data}_{r-v+1}
=\operatorname{data}_u.
\]

The two completed assignments give different outputs. Hence alpha and beta induce different residual Boolean functions after the cut. The cut principle of Section 1 forces at least `2^(q_r)` distinct graph vertices, proving (1).

The proof uses no assumptions about carries in general multiplication: its distinguishing suffixes make one operand one-hot, so ordinary binary shifting is exact. The n=1 case is covered: A and B are singletons, r=1, and q_r=1. No n=0 statement is made because there are then no product output bits.

### 3.5 Quantifier boundary

The proved statement has the order

\[
\forall\text{ input orders }\omega\quad
\exists r\in\{1,\ldots,2n-1\}\quad
\forall\text{ ordered graphs }G\text{ for }\operatorname{mul}_r,
\quad |G|\ge2^{n/8}.
\]

It does not exchange the first two quantifiers. The annotated appendix's final update points to a later 1991 result concerning fixed output bits; that is a separate source and is not needed for this proof. The proof above also does not claim exponential size for every multiplication output: for example the least significant output is simply `a_1 and b_1`.

## 4. Two useful structural comparisons from Section 3.1

These are mathematical complements to the ordering and multiplication examples, not experimental claims. The source states the parity size and quadratic symmetric-function bound in [Section 3.1, p. 7](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf#page=7).

### 4.1 Parity has exactly 2n+1 vertices

For n>=1, odd parity has one residual at the first level and two at every later level: parity of the remaining variables or its complement, according to the already-read prefix parity. Both occur from level 2 onward. They are distinct, nonconstant, and depend on the next variable. There are therefore `1+2(n-1)` nonterminal vertices and two terminals, giving `2n+1`. The same count holds for even parity. At n=0 each is constant and has one vertex.

For comparison, an implicant of odd parity cannot omit any input variable, since flipping an omitted variable reverses parity. There are `2^(n-1)` satisfying assignments when n>=1, so its minimum sum-of-products representation has exactly `2^(n-1)` full minterms. This count is supplied with its derivation rather than inherited from an ambiguous exponent in the source extraction.

### 4.2 Symmetry gives a quadratic upper bound in every order

Suppose `f(x_1,...,x_n)=F(x_1+...+x_n)` for a map `F:{0,...,n}->{0,1}`. After k inputs, a residual depends only on the number t of ones already read, where `0<=t<=k`. There are at most k+1 residuals before the next input. A graph can therefore store the pair `(k,t)` and branch to `(k+1,t)` or `(k+1,t+1)`; after all n inputs it returns F(t).

Identifying terminal values and then reducing gives, for n>=1,

\[
|G_f|\le\sum_{k=0}^{n-1}(k+1)+2
=\frac{n(n+1)}2+2.
\]

The argument works for every input order because Hamming weight is permutation-invariant. The bound is an explicit sufficient bound, not a claim that every symmetric function attains it. For n=0 the exact count is one.

## 5. Primary experimental facts worth adding

[Section 5, Table 2, pp. 19-20](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf#page=19) reports equivalence checking of 74181/74182-based ALUs. Timings cover construction from both gate and behavioral descriptions plus equivalence checking, on a VAX 11/780. The tested order puts five controls first, then carry-in, then least-significant-first interleaved operand bits. It is the best tested order, not a proved optimum.

| Word bits | Gates | Input patterns (source rounding) | CPU minutes | Largest graph, A=B output |
|---:|---:|---:|---:|---:|
| 4 | 52 | 1.6 x 10^4 | 1.1 | 197 |
| 8 | 123 | 4.2 x 10^6 | 2.3 | 377 |
| 16 | 227 | 2.7 x 10^11 | 6.3 | 737 |
| 32 | 473 | 1.2 x 10^21 | 22.8 | 1457 |
| 64 | 927 | 2.2 x 10^40 | 95.8 | 2897 |

The exact pattern count is `2^(2n+6)`, from two n-bit operands, five controls, and carry-in. Figure 11, pp. 20-21, contrasts four orders: interleaved low bits first; interleaved high bits first; controls last; and separate whole operands. The first three exhibit linear graph growth in that family, while operand separation causes exponential growth. These are finite experimental observations, not bounds on arbitrary circuits.

Section 3.3, p. 8, additionally reports multiplier graphs below 5,000 vertices for tested orders at n<=8, but some outputs above 100,000 vertices for n>10. Those measurements must not be identified with the appendix's asymptotic lower bound.

## 6. Current manuscript correspondence and authoring use

At the inspected snapshot, the Bryant subsection ends immediately before the Burch subsubsection and already supplies graph definitions, the canonicity induction, bottom-up reduction, Apply, restriction/quantification, composition, and satisfying-assignment operations.

- The Figure 2 paragraph gives the correct positive-n counts but only a residual-count sketch. Section 2 above supplies the full exact counts, including both sets of nonterminal levels and terminals.
- The Apply paragraph states the multiplication lower bound in one sentence. Section 3 above supplies its complete shifter/diagonal/residual proof and exact quantifiers.
- No Bryant-specific ALU experiment is currently reconstructed. Section 5 supplies the source's principal table and precisely what its timings measured.
- Section 4 supplies optional mathematically complete parity/symmetry comparisons already present in the controlling paper; they are distinct from the experiments.

## 7. Internal source reconciliation, not proposed reader prose

The appendix's permutation notation alternates between positions in a reading order and indices of operand bits. Its informal shifting paragraph also places a power `2^j` next to one-based operand-bit names, where a bit with significance index v has weight `2^(v-1)`. The proof in Section 3 avoids both ambiguities by defining reading-order names separately from significance indices and using `r=u+v-1` throughout.

The online extraction flattens exponents such as `2^(n+1)` and `2^(n/8)`. The exact Figure 2 counts above are independently derived rather than inferred from flattened typography. The appendix inequality is likewise proved with the exact integer q_r, so no uncertain exponent transcription is required for the reader-facing argument.

No later fixed-output multiplication theorem, new experimental curve values, or unproved global variable-order optimum has been imported into this note.
