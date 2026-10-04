# C6 mathematical and topic review

Date: 7 September 2026. Reviewer task: `/root/c6_topic_review`.
Target: C6 / R-002, completed P4 computation verification.

## Decision

**PASS for the assigned mathematical scope at the two frozen hashes below.**
The serialization, tagged extraction and packing, H1-H4 formulas, computation
theorem, and c.e./Sigma1 and decidable/Delta1 arguments agree with the actual
local machine and arithmetic definitions. I found no false formula, excluded
necessary witness, invalid quantifier exchange, capture defect, or circular
use of the computation theorem in this scope. No mathematical correction is
required by this review.

This is an independent topic review. I read the supplied contract, freeze,
actual target LaTeX and the four dependency files recorded below. I did not
read another C6 review or receive another reviewer's findings before filing.
I did not read the author development notes. No manuscript, symbol, registry,
provenance or generated file was edited. This report is the sole output.

| Component | Verdict | Actual target intervals |
| --- | --- | --- |
| Exact serialization and numbering compatibility | PASS | `inherited-07851-08048.tex:7-216` |
| E/E2 bounded extraction and finite packing | PASS | `inherited-08710-08876.tex:1-74` |
| History layout and stored-value versus index bounds | PASS | `inherited-08710-08876.tex:76-158` |
| H1 input formula and proof | PASS | `inherited-08710-08876.tex:160-214,323-377` |
| P5/R5, decoding chain, bitmap, full table and H2 | PASS | `inherited-08710-08876.tex:216-321,379-498` |
| Simultaneous input/table packing | PASS | `inherited-08710-08876.tex:500-531` |
| Cfg, Init, Step, H3 and conditional proof | PASS | `inherited-08710-08876.tex:533-618,678-776` |
| Output formulas, H4 and conditional proof | PASS | `inherited-08710-08876.tex:620-664,778-803` |
| Literal Comp and both computation directions | PASS | `inherited-08710-08876.tex:665-676,805-907` |
| Worked example and failure cases | PASS | `inherited-08710-08876.tex:917-956` |
| c.e./Sigma1 proof and bounded evaluator | PASS | `inherited-08710-08876.tex:958-1033` |
| Decidable/Delta1 conclusion | PASS | `inherited-08710-08876.tex:1035-1045` |
| Four ordinary-theorem hooks, observed order | PASS | `inherited-08710-08876.tex:805,958,1059,1080` |

Later hierarchy completeness/strictness citations and P5 internal
representation are outside this acceptance. External source fidelity,
candidate symbol publication, rendered publication quality, formal admission,
provenance closure and release readiness remain **UNRESOLVED by this review**;
they were not substituted for mathematical evidence or assessed here.

## Mathematical findings

### 1. Exact machine identity and enumeration

The local model has a two-way infinite tape, a total transition function on
nonhalting state/symbol pairs, and left/right moves only. Input starts at
physical cell 0. Numerical input is the canonical binary word for the
right-nested tuple code, with arity-one code equal to its entry. Numerical
output is the canonical word before the first nonnegative blank; the final
head and later tape cells are immaterial
(`inherited-07506-07677.tex:4-147`).

The new serialization fixes n, b, the width-b input bitmap and all (n-2)b
rows. The required symbols blank/0/1 receive numbers 0/1/2, and the required
states start/accept/reject receive numbers 0/1/2. The input bitmap excludes
blank and includes both digits. The row order is exactly the state blocks
0,3,...,n-1 and increasing symbols within each block. The outer pair records
the tuple length 3+(n-2)b, and the final tuple entry is its own one-entry
tail. Four pairing inversions decode each five-field row. These facts give
the claimed effective validity decision and exact recovery of the encoded
transition table and input alphabet (numbering file:22-80).

Enumeration does not require an unjustified canonical renaming. The proof
allows arbitrary role-preserving renamings of other states and symbols and
uses the stated configuration conjugacy. For a start state already halting,
the fresh start performs one unchanged-symbol right move to that same halt.
The output convention makes that move preserve the numerical behavior.
Every numerical k-ary input convention for k>=1 covers canonical binary
numerals because the tuple code is surjective; the model also explicitly
requires both digits in a numerical machine's input alphabet. Thus the
metadata step is compatible with the adequacy proof (numbering:116-210).

Comp checks the raw decoded machine. The output-cleaning wrapper justifies
partial computability of an indexed function; it is not silently substituted
for the raw transition table. The separate universal-computation sketch and
parameter theorem at numbering:218-261 are not used to prove the concrete
Comp equivalence.

### 2. Extraction, bounds and capture

The actual dependency formula P is the doubled Cantor pairing equation;
both projections are at most the pair code. B uses the unique projections
(t,m) of its first argument and the remainder modulo 1+(i+1)m. The divisor
is always positive, including m=0. Its quotient and remainder bounds are
valid, and its finite-sequence packing uses pairwise coprime moduli
(`inherited-08439-08709.tex:1-83`).

For u=a+b, pair(a,b) < (u+1)^2, also at u=0. Thus the strict polynomial
bounds in E and E2 contain their unique index witnesses. Neither index must
be bounded by s. For a concrete check, s=8 decodes as pair(1,2). Therefore
beta(8,i)=1 for every i. E(8,13,0,1) uses index pair(13,0)=91>8, which is
still below 14^2. E2(8,9,3,5,1) uses inner index 41<9^2 and outer index
1316<51^2. The revised history summary correctly distinguishes these
indices from stored values.

Finite packing fixes each tag's positional arity, pairs positions within a
two-dimensional family, and then pairs with the tag. Injectivity separates
every distinct assigned position. Filling the finite initial segment through
the largest resulting index and applying beta packing realizes the whole
assignment. This construction fixes indices before s is chosen and therefore
has no self-reference. The empty assignment and beta at zero are covered.

All formula abbreviations require fresh bound-variable renaming before term
substitution. Their free-variable arities agree at every call. E2 first binds
its inner position and E then binds a fresh outer index. P5's three tails
are bounded by rho; all five projections inherit that bound. R5 alone does
not claim membership. In the table check u*b+a ranges over exactly i<m; in
Step the witness is explicitly quantified i<m. Values in padding cannot
supply a transition.

All displayed quantifiers are marked bounded in the declared arithmetic
syntax. Bounds use only 0, S, + and multiplication; no variable occurs in
its own bound after the prescribed fresh renaming. The bound for an E lookup
may involve the already bound inner position in E2. That is legitimate.
The arithmetic-language convention counts marked bounds before their
eliminable logical expansion (`inherited-08306-08438.tex:28-94`). Lt and Le
use their own bounded witnesses within matrices, rather than an unmarked
comparison that would introduce an unbounded existential.

### 3. H1 and H2

H1 requires L=lambda+1, a common first bit/prefix, the full digit and prefix
families, the recurrence through precisely L-1 edges, and the final value x.
The zero branch requires the single digit 0. The positive branch requires
first digit 1. These conditions give the canonical word, including x=1 and
the empty recurrence range. Monotonicity bounds every actual prefix by x.
The converse's last-position witness is below the stored L, hence at most s.

H2 fixes n=nu+2 with nu>0, b>=3, m=nu*b, k=3+m and k=lambda+1. D requires
every pairing equation for i<k-1 and identifies the last description entry
with the last decoding tail. Consequently no zero terminator, extra counted
row, different length or different outer program code can pass. M's terminal
B_b=0 and backward recurrence fix exactly the stated bitmap width; its
distinguished bits are inside that width because b>=3.

For every i<m, division by b gives exactly one pair (u,a) with u<nu and a<b.
K forces source q=0 at u=0 and q=u+2 otherwise. Thus it supplies each allowed
key exactly once and checks the target state, written symbol and direction.
The n=3 case correctly has a single state-0 block. The auxiliary nu, m and
lambda witnesses are bounded respectively by stored n, k and k. The actual
row fields and tails are bounded by their stored row code. These facts cover
all existential bounds in the reverse implication.

Input and program certificates occupy disjoint families except for values
that explicitly agree. Adding any finite compatible configuration/output
assignment therefore preserves the packing argument. It does not presuppose
that the program halts.

### 4. H3, H4 and the finite-window converse

H3 ties k,n,b,L to the same uniquely extracted header values as H1/H2, and
forces H=T, W=L+2T+1 and W=mu+1. Cfg checks every time t<=T and every column
j<W, the state/head ranges, each base-b digit, each prefix recurrence and
the last tape code. Leading zeros are valid for these fixed-width tapes.
Init writes Sd_i at H+i and blanks every other column; the two blank-region
inequalities cover exactly the complement of that input interval.

Step reads the old symbol at h, chooses an actual table row, stores its next
state and written symbol, and requires h=h'+1 for left or h'=h+1 for right.
Both heads remain in range through Cfg. The universal condition preserves
every j<W other than h, including the new head cell when it differs from the
old one. Blank extension outside the window preserves all remaining physical
cells because the scanned cell lies inside. The nonhalting source checks
exclude an earlier halt. Induction therefore recovers precisely the raw
machine's deterministic initial run.

In the converse, after t transitions the physical head lies in [-t,t].
The initial input cells and every subsequently written cell through time T
are contained in [-T,max(T,L-1)]. The chosen window represents [-T,L+T],
so it includes every such cell and both heads at each transition. The cell
L+T is blank throughout because L>=1 makes it greater than T and L-1.
Thus the first nonnegative blank in the accepting output satisfies
ell<=L+T, giving H+ell<=W-1<W. A left move at an intermediate time cannot
leave the window because h_t>=T-t>0 for t<T. No necessary computation is
lost at either boundary.

H4 requires final state 1, a positive output length, binary nonblank symbols
at precisely the output-prefix positions, and a blank at H+ell. Its prefix
recurrence and zero/first-bit branches certify exactly bin(y). It imposes
the original output convention without an additional final-head condition.
Its last-position witness is below stored ell. The complete history packs
all of this finite data before choosing s; every stored value is then at
most s. Derived m, mu and last positions have the explicitly proved bounds.

The literal conjunction H1 and H2 and H3 and H4 therefore has both directions
claimed in bounded verification. T=0 leaves H3's step range empty but cannot
pass H4, since normalized start state 0 differs from accepting state 1.
Rejecting halts, empty outputs, output non-digits, and leading-zero numerals
fail the corresponding final clauses. Invalid program indices fail H2.

### 5. c.e., Sigma1, and Delta1

The forward c.e. argument starts from the actual domain definition
(`inherited-07753-07843.tex:9-12`), applies the proved enumeration theorem,
and uses the specific bounded Comp construction. It does not invoke the
earlier sketched characterization by a decidable history relation or a
generic T-predicate. Substitution of the fixed numeral e and negation-normal
form conversion preserve boundedness. Existential quantification over s then
gives the required Sigma1 formula.

For the converse, the evaluator explicitly covers terms, bottom, equality,
Boolean connectives and both forms of marked finite bounds. The quantified
variable is absent from its bound, so each loop has a fixed finite range.
Empty existential ranges return false and empty universal ranges return
true. Structural descent through a fixed formula together with finite loops
proves termination. Finite-control return points, delimited assignment and
scratch blocks, scans and binary increment implement the procedure in the
stated machine model. Writing one truth-value bit at cell 0 and blank at
cell 1 supplies a valid numerical output despite later scratch data.

The actual prefix-normal-form dependency, including its finite bound
collection proof, is given at `inherited-08439-08709.tex:89-270`. Its use here
is only semantic equivalence in N. A finite existential block is enumerated
by bounded-coordinate stages; each stage terminates and every witness tuple
appears. A vacuous existential covers the no-witness-variable case. The
resulting partial function outputs 0 exactly on the defined set, and runs
forever otherwise, including for the empty set. This supplies the domain
definition directly and introduces no representability assumption.

Negation exchanges Sigma1 and Pi1 definability with a bounded negated matrix.
The Delta1 conclusion then uses the earlier decidability characterization
(`inherited-07753-07843.tex:78-90`). Its operational content is sound directly
from domain machines: dovetail a partial domain machine for A and one for
its complement; exactly one has a valid accepting numerical halt, determining
the characteristic bit. Conversely, a total characteristic computation can
be followed by acceptance on the desired bit and an infinite loop on the
other bit. Thus this dependency does not introduce circular reliance on the
new Comp construction or on P5.

## Independent arithmetic and boundary probes

I recomputed the worked program's nested Cantor row codes using exact integer
arithmetic: 1034, 26564 and 582659. Four inverse pairings recover respectively
(0,0,1,0,1), (0,1,1,1,1) and (0,2,1,2,1). Decoding its outer index and
six-entry tuple recovers length 6 and (3,3,6,1034,26564,582659); its index has
352 decimal digits. The example tape prefixes are 0,2,7,21,63, and bitmap
tails are 6,3,1,0, as stated. I also checked the strict pairing bound on all
0<=a,b<=100; the general proof, rather than this finite check, establishes
the unrestricted statement.

For a one-step identity machine on input 0, L=1,T=1,H=1,W=4 gives tape
(0,1,0,0), output length 1 and blank at column 2. A left accepting move has
shifted heads (1,0), and a right accepting move has heads (1,2); both satisfy
the respective Step equations and the original output convention. A proposed
left move from column 0 has no natural h' solving 0=S h'. Changing any other
in-window cell violates the unchanged-cell conjunct. Changing an out-of-table
padding row cannot supply i<m. The zero word (0,0) fails the required length
and a positive word starting in 0 fails the required first digit, even when
their numerical recurrences happen to hold. None supplies a counterexample
to the frozen construction.

No software regression suite, build, render, formal checker or external source
review was run. The arithmetic operations above are bounded mathematical
recomputations, not additional acceptance claims.

## Exact read record and observed metadata

Repository: `C:/Dev/the-methods-of-reason`. Observed branch: `phase4-codex`.
Observed HEAD: `35d537c692bb74b532dc4aa750da381a7fe4daf2`.
The two target files appeared as untracked in the scoped Git status. These
are current filesystem reviews; HEAD alone does not identify their content.
Git was read with a command-local safe.directory setting after the initial
ownership diagnostic. No Git configuration was changed.

All line ranges below were actually read in full, inclusive. SHA256 values
and sizes were obtained from the current files. The initial target hashes
match the freeze. A final target hash check accompanies filing.

| File relative to repository | Read lines | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1-168 | 9361 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-c6-review-freeze.md` | 1-85 | 4905 | `04E1075E9EF200726F36C781C463380F7701B82C7C5FB8FB1DFE1E7F656D4732` |
| `handbook/restoration/inherited-07851-08048.tex` | 1-261 | 13700 | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| `handbook/restoration/inherited-08710-08876.tex` | 1-1104 | 51440 | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |
| `handbook/restoration/inherited-07506-07677.tex` | 1-172 | 7334 | `EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D` |
| `handbook/restoration/inherited-07753-07843.tex` | 1-91 | 3884 | `E2B7284BEABCA82F440BB921D779243F1615F8D7077ABA73DFF6CBDE28458B00` |
| `handbook/restoration/inherited-08306-08438.tex` | 1-133 | 6179 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08439-08709.tex` | 1-271 | 13527 | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |

Observed target last-write times were respectively
`2026-09-07T16:41:49.3975304Z` and `2026-09-07T17:33:16.7870480Z`.
The first explicit local time observation during reading was
`2026-09-07T10:38:27.5268415-07:00`; the pre-filing observation was
`2026-09-07T10:41:28.1153734-07:00`. The review and filing completed within
the assigned 45-minute work block. No 15-minute boundary was reached before
the completed findings were ready to file.

The tool interface identified this as the independent task named above. It
did not supply an actual model/version identifier for this review, and no
such identifier is asserted. Prior historical acceptance was not used as
evidence for any current mathematical verdict.
