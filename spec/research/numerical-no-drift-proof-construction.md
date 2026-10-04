# Round-to-even no-drift proof construction

Date: 9 September 2026. Author: historical_first_half, assisting the numerical
chapter author thinking_gaps_practical. This is a proof construction for the
current manuscript, not an independent review or reproduction of an unread
Reiser–Knuth proof.

## Exact target and source

The target is Theorem 5 in Section D.3.5.1 of the retained *Numerical Computation
Guide*, Sun Studio 11, part 819-3693-10, November 2005, Revision A. Its edited
Goldberg presentation states that repeated exactly rounded subtraction and
addition of the same floating-point value cannot continue to drift under
round-to-even.

Held PDF: source/references/p12-numerical-error/oracle-819-3693.pdf, physical
page 195, printed D-13. SHA-256 reverified:
352F4A6CCD78C8A458872981668F53B7270CD182AC4E7C77684FA73CC2119304.

The exact theorem and preceding rounding convention were read in the held
HTML companion, source/references/p12-numerical-error/oracle-819-3693-goldberg.html,
anchor 14697. The numerical author's actual definitions were read in
handbook/parts/p12/numerical-error-and-inference.tex. Their target format has
even radix beta >= 2, precision p >= 2 and unrestricted integer exponents for
the mathematical proofs. A finite implementation inherits the result only
under the chapter's explicit normal-range and exactly rounded operation
conditions. No claim about overflow, underflow, NaNs or flush-to-zero is added.

Proposed labels supplied by the numerical author:
thm:p12-numerical-no-drift and annex:p12.numerical.no-drift.

Write F for the set of format values and RN for its nearest rounding with ties
to an even last retained digit. The required claim is, for arbitrary signed
x,y in F,

\[
 T_y(x)=\operatorname{RN}(\operatorname{RN}(x-y)+y),
 \qquad T_y(T_y(x))=T_y(x).
\]

Consequently the iteration is constant after its first step. The first step
may already equal x. The operators in this claim are exactly rounded; the
chapter's one-guard-digit addition/subtraction model is insufficient.

## Elementary format facts used in the proof

These facts follow directly from the specified format; their derivations are
included so that the proof does not import an unspecified rounding theorem.

1. Every nonzero float has immediate predecessor and successor floats. Zero
   is an accumulation point in this unrestricted-exponent model, so it is
   handled separately. On the positive interval [beta^k,beta^(k+1)), the
   spacing is beta^(k-p+1). The gap between any two consecutive nonzero
   floats is therefore an integer power of beta. The negative gaps follow
   by reflection.

2. Except at values of the form plus or minus beta^k, a float's two adjacent
   gaps are equal. If the common gap is d, its nearest-rounding cell is
   [z-d/2,z+d/2] when its retained integer significand is even, and the
   open interval with the same endpoints when it is odd. Neighboring
   retained significands have opposite parity. This also holds for the
   two neighbors of a radix-power boundary: its predecessor has significand
   beta^p-1, the boundary has significand beta^(p-1), and its successor has
   significand beta^(p-1)+1. The middle significand is even because beta is
   even and p >= 2.

3. At the positive boundary z=beta^k, define

   \[
    q=\beta^{k-p+1},\qquad a=q/\beta=\beta^{k-p}.
   \]

   Its left gap is a and its right gap is q. Its rounding cell is precisely
   [z-a/2,z+q/2], including both endpoints because z is even.

4. RN fixes every format value and is sign-symmetric. Negating a real input
   negates both its nearest candidates, preserves their distances, and
   preserves the parity used to resolve a tie. Thus RN(-t)=-RN(t).

5. A real t has RN(t)=0 only when t=0 in this unrestricted-exponent model.
   For t != 0, there are nonzero format values of its sign closer to t than
   zero; for example scale a radix power to lie between |t|/beta and |t|.

No probabilistic assumption about rounding errors or the frequency of ties is
used.

## Complete derivation

Fix arbitrary signed format values x and y, and set

\[
 z=\operatorname{RN}(x-y),\qquad
 e=z-(x-y),\qquad
 s=z+y=x+e,
\]
\[
 x'=\operatorname{RN}(s),\qquad \eta=x'-s.
\]

Because x itself is a format value competing for the nearest rounding of s,

\[
 |\eta|\leq|s-x|=|e|. \tag{1}
\]

The next subtraction has exact real value

\[
 x'-y=z+\eta. \tag{2}
\]

If x'=x, the desired idempotence is immediate: the next evaluation has exactly
the original input. If z=0, format fact 5 gives x=y, so s=y=x and this immediate
case applies. Hence we may assume z != 0; we retain the easy x'=x case whenever
it occurs below.

### Case 1: the two adjacent gaps at z are equal

Let the common gap be d. Since RN(x-y)=z, format fact 2 gives |e|<=d/2,
with a strict inequality when z is odd. Equation (1) then places z+eta in
the same symmetric rounding cell: endpoints are allowed when z is even, and
cannot be reached when it is odd. Consequently

\[
 \operatorname{RN}(x'-y)=\operatorname{RN}(z+\eta)=z.
\]

The following addition returns RN(z+y)=x'. Therefore T_y(x')=x'.

### Case 2: z is a radix-power boundary

By sign symmetry, replacing (x,y) by (-x,-y) negates every intermediate and
output value. We may therefore take z=beta^k>0; no assumption on the individual
signs of x or y is introduced. Use q and a from format fact 3.

If e>=0, then x-y=z-e lies on the lower side of z's rounding cell, so
0<=e<=a/2. Equation (1) puts eta in [-a/2,a/2], a subset of [-a/2,q/2].
Thus RN(z+eta)=z and the preceding fixed-point argument applies.

It remains to consider e=-r<0. The upper half of z's rounding cell gives

\[
 0<r\leq q/2,\qquad s=x-r,\qquad |\eta|\leq r. \tag{3}
\]

If eta>=-a/2, then eta<=r<=q/2 also, and again RN(z+eta)=z.

The only exceptional subcase is

\[
 \eta<-a/2. \tag{4}
\]

Put l=x'=RN(s). By (4), l<s. Let u be the next format value above l. Since l
is a nearest float below s, there can be no format value strictly between l
and s; hence l<s<u. Equality s=u would round exactly to u, contrary to l<s.
The relevant predecessor/successor exists: s=0 would give eta=0, and nonzero
values lie in locally discrete portions of the format.

Write D=u-l for the gap and d=s-l=-eta. Nearest rounding to l entails

\[
 d\leq u-s=D-d,\qquad d\leq D/2. \tag{5}
\]

Together with (4), this gives D>=2d>a. D and a are integer powers of beta,
so the next possible larger spacing is beta*a=q:

\[
 D\geq q. \tag{6}
\]

Because x is a format value and x>s by (3), while u is the least format value
above s, x>=u. Combining all bounds,

\[
 \frac q2\ \geq\ r=x-s\ \geq\ u-s
       \ \geq\ \frac D2\ \geq\ \frac q2. \tag{7}
\]

Every inequality is therefore an equality. In particular,

\[
 D=q,\quad r=q/2,\quad x=u,\quad d=q/2,
 \quad\eta=-q/2. \tag{8}
\]

The second subtraction's exact result is now

\[
 v=z+\eta=z-q/2
   =\left(\beta^p-\frac\beta2\right)\beta^{k-p}. \tag{9}
\]

This is a format value. Its coefficient is an integer because beta is even;
it is less than beta^p and at least beta^(p-1), because p>=2 and beta>=2.
It therefore has at most p radix digits and a permitted unrestricted exponent.
Thus RN(x'-y)=v exactly. Moreover,

\[
 v+y=z-q/2+y=s-q/2=l=x',
\]

so the following addition is exact as well:

\[
 \operatorname{RN}(\operatorname{RN}(x'-y)+y)
       =\operatorname{RN}(x')=x'.
\]

This settles the exceptional boundary case and completes the proof for all
signed x,y in the stated even-radix format. Induction immediately gives
x_j=x_1 for every j>=1. If x_1=x_0, the sequence is constant from its start.

## Why the exceptional branch must be retained

A proof that asserts RN(x'-y)=z in every case is too strong. The boundary
branch above allows the second subtraction to change from z to the exactly
representable z-q/2; the following addition nevertheless returns x'. The
correct target is idempotence of the two-operation map, not necessarily
stabilization of every intermediate after the first subtraction.

The two principal mechanisms are therefore distinct: an ordinary symmetric
rounding cell returns the same rounded difference, while the only possible
escape from the asymmetric boundary cell forces a tie and then an exact
representable difference. Neither mechanism can be inferred from sampled
binary calculations or a generic relative-error bound.

## Source and implementation boundaries

Reiser and Knuth's original paper, *Evading the Drift in Floating-Point
Addition*, Information Processing Letters 3(3), 84–87 (1975), DOI
10.1016/0020-0190(75)90022-8, and its 1975 erratum at 3(5), 164 were identified
but their bodies were not obtained during this construction. Knuth's
[author-maintained collection page](https://cs.stanford.edu/~knuth/da.html)
identifies a later reprint as Chapter 23 of *Selected Papers on Design of
Algorithms*. That reprint was not acquired or substituted for the original.

The derivation above is an independent author proof of the exact theorem in
the held Oracle/Goldberg presentation, using the numerical chapter's declared
format. It must not be attributed as a transcription or source-fidelity
verification of the unread 1975 proof or erratum.

The finite-range transfer uses the numerical author's already declared
representability conditions and exact RN operations. No additional hardware
behavior is assumed. No manuscript file, test, build, renderer or independent
review was run by this proof-construction worker.
