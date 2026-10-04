# NOW-03a independent mathematical review

Date: 7 September 2026, America/Los_Angeles. Reviewer: fresh independent topic
review context `pa_numeral_topic_review`. Assignment: all six results in the
frozen numeral-builder body and annex, with the actual selected PA graph,
checker and numerical definitions. This report owns no manuscript or shared
record changes.

## Verdict

**FAIL as printed: one missing domain hypothesis in the numeral-substitution
corollary.** The explicit equality in annex lines 82–85 is false on the
defined invalid-replacement inputs. The required correction is to retain
`Tm(u)=1` in that assertion and its body statement. The no-renaming execution
invariant itself is valid under its stated `nc=1` premise. The five remaining
result constructions pass their mathematical checks on their stated domains;
their uses of this corollary all have the needed replacement-term property.

The finding does not exhibit an invalid successful numeral/literal output.
It does prevent accepting every printed assertion in the unchanged unit.
No verdict was taken from the author assessment or another review. The report
does not grant text acceptance, formal admission, production acceptance, D3,
PT-1 closure, GL completeness or the bounded-formula compiler.

## Frozen identity and actual reading

Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. The working tree contains substantial
existing work; the review uses the live files and the identities below.
Line ranges are inclusive. Whole-file hashes identify partial reads as well
as complete reads; partial ranges are not represented as complete reading.

| File relative to repository | Actual read extent | Whole-file SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Complete, 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/EDITION-2026-WORK-PACKAGES.md` | 233–278 of 794 | `F49DE88FC33093390FD0CC377E7647019F74FD0529F7DCC07B503E559545160E` |
| `spec/research/edition-2026-p5-numeral-proof-builders.md` | Complete, 1–214; dependency locator and author intake only | `61BF33E44BF1706AB84786B899F964707B896C3C6F5933BC15925291CF9BD25D` |
| `handbook/parts/p05/pa-numeral-proof-builders.tex` | Complete, 1–490 | `E805B3D17CC04419E9105BDC98A5B42483E91DE90137358669019D0F23D4858F` |
| `handbook/annex/p05/pa-numeral-proof-builders.tex` | Complete, 1–628 | `576AD536A4F7484FF2E2968B3C32FB6D685C0288B16A9007B4E89A7234B0B65A` |
| `handbook/parts/p05/pa-checker-arithmetization.tex` | Complete, 1–523 | `993418B3EB3343525C0922274CA6794F5B4FED13FFB35CB146E9995D88391DFA` |
| `handbook/annex/p05/pa-checker-arithmetization.tex` | Complete, 1–537 | `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | Complete, 1–252 | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | Complete, 1–315 | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09262-09327.tex` | Complete, 1–253 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/restoration/inherited-09328-09438.tex` | Complete, 1–546 | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/annex/p05/internal-proof-predicate.tex` | Complete, 1–524 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-08306-08438.tex` | 1–70 of 133 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-09112-09149.tex` | Complete, 1–38 | `23A060D7646D1BBB54480F35833F2D40A78180E67A36232CF8406D7E71B3FBAE` |
| `handbook/restoration/inherited-07678-07752.tex` | Complete, 1–75; initial-function, arity and recursion conventions | `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD` |
| `handbook/restoration/inherited-08439-08709.tex` | 1–115 of 271; actual pairing and beta formulas and surrounding context | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |

The target was read in full as body 1–490 and annex 1–330, 331–628. The seven
required mathematical dependencies were read completely in individually
numbered ranges. The extra arity and beta reads were used to check the actual
initial-function convention and graph formulas. No source or mathematical
coverage claim depends on the unread remainder of either partial context file.

## Located finding and required repair

### M1 — Preserve the replacement-term hypothesis in numeral invariance

**FAIL, local statement/proof repair required.** Locations:

- Body `handbook/parts/p05/pa-numeral-proof-builders.tex:90–93` states that
  substitution leaves a numeral unchanged, and explicitly qualifies the
  adjacent iterate assertion but supplies no corresponding replacement-term
  hypothesis for numeral invariance.
- Annex `handbook/annex/p05/pa-numeral-proof-builders.tex:82–85` explicitly
  claims `ns(nu(n),i,u)=nu(n)` and then transfers it to `sub`.
- The same body at 55–57 makes the entire table row zero whenever `u` is
  not a term. The selected checker body at 229–233 also returns zero when
  the replacement type test fails. Invalid syntax metadata are zero by that
  body's syntax definition at 136–157.

Take numerical inputs `n=0`, `i=0`, `u=0`. Under the governing cons coding,
`0` is the empty-list code and is not a term. The code of the zero term is
`nu(0)=o=N_1()=C(1,0)=2`. The displayed failure clauses therefore give

```
Tm(0) = 0,
ns(nu(0), 0, 0) = 0,
sub(nu(0), 0, 0) = 0,
nu(0) = 2.
```

Thus the printed unqualified equality becomes `0=2`. This is a counterexample
using the selected descriptions themselves, without executing a replacement
implementation. Its finite defining equations are also available in PA, so
the problem is present in the asserted internal theorem.

Required repair: state and prove, with universal numerical closure,

```
Tm(u)=1 ->
  (ns(nu(n),i,u)=nu(n) and sub(nu(n),i,u)=nu(n)).
```

Retain `Tm(u)=1` as an induction parameter in the annex's zero and successor
cases. It licenses the table's zero-term branch at the base, the successor
branch at the step, and `nc(nu(n),i,u)=1` when applying execution equation (1).
Add the same domain qualification to the body statement. For precision the
annex's variable-free-replacement sentence at 74–76 should likewise retain
the term assumption already present in the corresponding body clause.

Every later replacement used by the reviewed builders is proved to be a
term: numerals, `v_y`, `s(v_y)`, their successor iterates, or a fixed term's
closed numeral instance. Therefore the repair preserves their intended
claims and does not require changing their constructors. Recheck the corrected
statement and these typed invocations before accepting the unit.

## Component findings

| Result | Status | Mathematical finding |
| --- | --- | --- |
| `thm:p05-builder-nocapture` | **FAIL as printed; execution invariant PASS under `nc=1`** | M1 affects the unqualified numeral-invariance consequence. The actual machine equation, cost bound, valid-input type preservation and no-renaming branches are proved. |
| `thm:p05-builder-row-templates` | **PASS** | Fixed joins preserve successful rows, exact open-list updates and the parent-count equation. Equality templates use the required premise order and actual substitution matrix. |
| `thm:p05-builder-left-addition` | **PASS** | `D_Z` and `D_L` are explicit trees using canonical `I_Z` and `I_L` leaves, with the required nonvacuous step discharges and final universal introductions. |
| `thm:p05-numeral-arithmetic-builders` | **PASS on the declared domains** | Addition, multiplication and both successor-string recurrences have exact roots and PA induction base/step arguments for their descriptions. |
| `thm:p05-numeral-literal-builders` | **PASS on the declared success conditions** | Equality/disequality, four comparison cases, successor peeling and negated bottom preserve the precise code and satisfy the actual discharge/freshness tests. |
| `thm:p05-fixed-term-literal-builders` | **PASS on the declared domains** | Separate finite term descriptions, internal value identification and two specified equality eliminations yield the literal original numeral instance with its retained binder. All substitution calls satisfy the guard missing in M1. |

### 1. Actual no-renaming machine and finite descriptions

The new table's row update reads earlier child rows only; the initial syntax
test excludes wrong tags, arities and child types. Invalid replacements give
the stated three zero fields. Its bound `Sc` is fixed before the fold. The
positive row costs are one at leaves or stopped binders, two plus one child
cost at unary/continued binders, and two plus both child costs at binary nodes.
These give `1 <= cost <= 2 nodes(c)` by the stated strong PA induction.

Annex 33–72 proves an equation for the selected machine's actual update, with
arbitrary continuation and value lists. The initial state contains exactly
the four-field substitution command. A binary node runs left, then right,
then assembly; the latter pops right before left. At a distinct binder the
`AV(u,j)=0` factor selects exactly command 4 after the child, and no renaming
or after-renaming command is entered. Universally quantifying the continuation
and old stack makes the child induction hypotheses applicable at these nested
calls. The iteration composition equation and absorbing completed state
justify using the actual `20(n(c)+1)^2` final extraction. `nodes` in the new
body explicitly names the earlier syntax-node-count description, called `n`
in the checker body at 148–157; no alternative traversal is substituted.

The description order is acyclic. `it` has one fixed parameter and a final
recursion counter; `nu` is its composition at `o`. `R_+`, `R_times`,
`R_right`, and `R_left` recurse on their final numerical input. Multiplication
calls the earlier addition builder. The five-argument peeling recursion has
counter last, is evaluated at the supplied bound `b`, and has an explicit
stationary branch for `j>=b`. Each one-hole context is a separate constructor
expression. Nullary constants and descriptions are allowed by the actual
initial-function convention. Malformed FE/MP/equality patterns and the
literal guards have their stated total defaults. None is a proof-search call.

### 2. Exact joins and equality transport

For premise block `j`, the new root reference is `t_j+D(l_j)`; nonemptiness
makes this the last row of that block. The sum of earlier block lengths puts
each block in a disjoint interval. Formula, parameter and marker fields remain
unchanged while premise references receive precisely that interval offset.
The existing row induction uses only these fields and the corresponding
shifted open indices, so the new raw-tree version does not require a sentence
premise. Discharge filters preserve literal formula and label tests and their
strict length decrease. The existential-elimination case retains its actual
filtered-minor-before-major open-list order.

The new parent count at an old index is the old count plus
`E(v,D(l_j))`; the new row has count zero. This proves the whole tree test,
including arity zero, without assuming that an external decoded proof is a
PA proof of that test. Separate copies ensure distinct root references even
when the input trees have equal numerical codes.

The equality row has parameters `[t,u,c,i]`, equality premise first and the
corresponding matrix instance second. Symmetry uses `x_j=t`, transitivity
uses `t=x_j` with the second equality first, and congruence uses
`g(t)=g(x_j)` plus the premise-free identity at `g(t)`. The maximum-index
choice excludes the hole from every fixed context term. These operations
therefore yield the literal required roots, with only the copied old leaves.

### 3. Constructed induction records

For `m_Z`, the free-index list is `[0]`, so `I_Z` has no parameter prefix.
Its base is `0+0=0`, and its step consequent is exactly `0+Sx_0=Sx_0`.
`Z_s` chains the actual `q_5` instance with successor congruence of the
single marked `m_Z` leaf. Tag 7 removes that leaf nonvacuously; tag 15 sees
only closed `q_5` leaves. The conjunction and actual `I_Z` implication give
`All(0,m_Z)` by tag 8.

For `m_L`, the free-index list is `[0,1]`, the induction index is 1, and
the canonical prefix is `[0]`. The base chains `Sx_0+0=Sx_0` with the
symmetry of `S(x_0+0)=Sx_0`. The step's three equations are exactly those
at annex 255–259. Its one marked `m_L` occurrence survives the equality
joins and is then removed by tag 7. Universal introduction at 1 has only
closed axiom leaves. FE applied to `I_L` with `v_0` removes its parameter
binder without renaming the internal binder 1. Tag 8 gives `All(1,m_L)`;
the final tag 15 gives `All(0,All(1,m_L))`.

As an independent symbolic audit of the finite expressions, `D_Z` contains
14 rows and `D_L` contains 31. Their final open formula lists, including
multiplicity and order, are respectively `[q_4,q_5,I_Z]` and
`[q_4,q_4,q_5,q_5,I_L]`. Every marker there is zero. Their canonical
induction leaves and the seven fixed axiom constants have all-variable
indices contained in `{0,1}`. A later use of either derived conclusion
copies its full tree and adds FE rows; it is never promoted to an axiom leaf.

### 4. Arithmetic and successor peeling

The addition base is a real `q_4` leaf followed by FE. Its step chains a
real two-FE `q_5` instance with successor congruence and uses
`A(m,Sn)=S(A(m,n))` to identify the final numeral code. Multiplication
starts with a `q_6` instance; its step uses a `q_7` instance, congruence
of the preceding product under right addition by `nu(m)`, and the already
proved `R_+(M(m,n),m)`. The last numerical equality is the selected
recurrence `M(m,Sn)=A(M(m,n),m)`.

The right successor-string builder has root `t+nu(n)=it(t,n)`; its left
counterpart has root `nu(n)+t=it(t,n)` and uses the constructed `D_Z,D_L`
instances. The allowed open variable indices are at least 3, so the outer
axiom substitutions cannot conflict with inner binder 1. Their roots may be
open, while the surviving axiom leaves stay closed.

For peeling, the PA invariant at `j<=b` has root
`it(t,L(k,j))=nu(L(b,j))`. Under `j<b` and `k>b`, both lengths are
positive, and the specified `q_2` instance removes precisely one successor
from each side. At `b`, the positive remainder `L(k,b)` gives the exact
successor term contradicted by the `q_1` instance. Tag 10 has positive
equality before its negation. A zero bound performs no peeling update and
still yields the correct `q_1` contradiction. The input marked occurrence
is copied once at every step and survives for the eventual discharge.

These are arithmetic inductions in `Safe` or the displayed root/open-list
formulas, using the proved graph equations and full PA induction. The graph
totality theorem supplies outputs; it is not used to infer an invariant from
external numerical correctness. `A` agrees internally with object-language
addition, and the corresponding induction for `M` supplies multiplication.
The selected `L`, equality and order tests are identified using predecessor,
the arithmetic order laws and their own recursion equations.

### 5. Literal cases and all-variable freshness

Disequality peels the larger numeral against the smaller; the reversed case
first applies the explicit symmetry tree. In both cases the one leaf later
discharged is the original equality with stored marker 1. The conclusion is
its original literal negation. Equality at equal inputs uses the tag-18 row
with empty open list.

The weak expansion is `exists x_i (x_i+t=u)`. Its positive witness is
`nu(n-m)` and its addition builder is ordered `(n-m,m)`. The strict
expansion is `exists x_i (t+Sx_i=u)`; its positive witness is
`nu(D(n-m))` under `m<n`. The root of `R_+(m,n-m)` is exactly the
required witness-instance equality. These calls retain the supplied binder.

For negative weak comparison, symmetry of the right-addition proof and the
minor equality give `S^m x_y=nu(n)`, with `m>n`. For negative strict
comparison, symmetry of the left-addition proof gives
`S^m(Sx_y)=nu(n)`, identified with `it(v_y,Sm)=nu(n)` and licensed by
`Sm>n`. No unstated commutativity inference is needed in these raw records.

At tag 16, the minor stored marker 2 corresponds to discharge label 1 and
its formula is precisely `sub(c,i,v_y)`. It survives once and is removed
nonvacuously. Every remaining minor leaf belongs to the explicit fixed axiom
list and has no variable index above 1. With `y=i+3`, the eigenvariable is
at least 3 and distinct from the only index `i` in the major's all-variable
set. Bottom has no variables. This checks all factors of the actual stronger
freshness test, including bound occurrences and the surviving major leaf.
Tag 9 then discharges the one marker-1 major assumption. Earlier label-0
discharges inside copied `D_Z,D_L` trees remain confined to their branches.

At equal endpoints, weak comparison uses witness zero and strict comparison
is refuted by one remaining successor after peeling. This covers `m=n=0`
and binder `i=0`. `R_neg_bottom` has exactly two rows: marked bottom,
then negation introduction discharging it. The parent counts are one and
zero, and the final open list is empty.

### 6. Fixed terms and exact original literal codes

Metainduction on each fixed term constructs its three separate descriptions.
Zero and variables use identity. Successor uses congruence. Sum and product
first normalize the left child with the right child fixed, then normalize
the right child with the normalized left fixed, then apply the relevant
numeral arithmetic tree. The intermediate term codes agree literally.
The induction yields an actual PA theorem with tuple parameters, and each
numeral-instance term is variable-free. There is no uniform evaluator over
term descriptions. The empty tuple has the permitted nullary description.

For a signed equality or comparison, `Sym(R_u)` transports the normalized
first argument to `u^nu` using the first displayed matrix, and `Sym(R_v)`
then transports the second argument. Their common hole index is greater
than the original comparison binder and absent from all closed argument
terms. The guarded numeral-substitution consequence in M1 is applicable at
every one of these calls. The no-renaming theorem also treats the optional
outer negation and the existing existential binder.

The comparison binder was fixed at the original abbreviation expansion,
before free variables were replaced by numerals. It remains that same index
through both equality eliminations, even when index zero later becomes
available. Thus the output is the literal target code rather than merely
an alpha-equivalent sentence. The arithmetic value identification and the
fixed order definitions turn each original signed antecedent into the
numerical guard used by its builder. Existential introduction of the graph
output, implication introduction and tuple closure give the stated final
PA formula. Positive bottom has contradictory antecedent and a constant-zero
builder; its conditional correctness does not claim a proof of bottom.

## Scope and return

The bounded-formula compiler and its finite-case enumeration, evidence-to-proof
construction, D3, consumer repair and separately owed GL/Solovay developments
remain **UNRESOLVED outside this assignment**. The explicit statements at the
end of both targets preserve those boundaries.

Only this report was written. No manuscript edit, other current reviewer
finding, test, build, render, subagent or formal admission was used. File
hashing and the row-count calculations above are source-identity checks and
symbolic mathematical checks, respectively. The sole required mathematical
repair returned to the integrator is M1. The unchanged target hashes were
rechecked at return.
