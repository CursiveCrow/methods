# C7 author handoff: GPSS Theorem 2.3 and its exact complete-order comparison

8 September 2026. Author /root/kamp_lemma7_author; block began 15:18 UTC.
The assigned separation algorithm, both scope bridges and counterinstance
are fully written with six reciprocal proofs. Consolidated independent
reviews remain deferred.

## Owned files and exact source reading

- handbook/parts/p09/presentations/gpss-past-future-separation.tex
- handbook/annex/p09/gpss-past-future-separation.tex
- This note.

All three paths were absent before authoring. Exact-path permission was
granted and only these three files were written with apply_patch.
No shared routes, bibliography, symbols or previous units were edited.

Personally reread the complete GPSS Theorem 2.3 statement and its surrounding
referral on printed p. 170, and the exact G2 bibliographical entry on p. 173.
Held primary:
tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf,
SHA256 2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2.
The source statement is over discrete complete models and says Boolean
combinations of L(S) and L(U) formulas. G2 is Dov Gabbay, The Separation
Property of Tense Logics, manuscript, September 1979. Its body remains
unacquired. This proof uses the complete first-order route and does not
claim to reconstruct that manuscript's direct syntactic derivation.

Read the actual current source-language clauses in n-c-012.tex, the full
GPSS special-normal-form body, the discrete future-completeness interface,
the typed Kamp reversal definitions, the guarded-completeness interface,
and the current C1/C2 construction, until table and guarded-fragment
semantics in gpss-complete-order-complement.tex.

The research and PDF skills supplied primary reading and this note. The
whole saved body and annex were read as one author mathematical batch.
No independent reviews, review waits, scanners, tests, builds or manuscript
renders were run. No new primary acquisition or bibliography key was needed.

## Six complete result/proof pairs

| Result | Annex |
| --- | --- |
| thm:p09-gpss-separation-translation | annex:p9.gpss.separation.translation |
| thm:p09-gpss-separation-dual | annex:p9.gpss.separation.dual |
| thm:p09-gpss-past-future-separation | annex:p9.gpss.past.future.separation |
| thm:p09-gpss-guarded-separation-dual | annex:p9.gpss.guarded.separation.dual |
| thm:p09-gpss-complete-order-separation | annex:p9.gpss.complete.order.separation |
| thm:p09-gpss-pure-separation-obstruction | annex:p9.gpss.pure.separation.obstruction |

The first-order translation supplies both strict modal clauses, every
Boolean/atomic case, capture-free copying, and the source/Kamp operand
bridge. In infix notation the interval operand remains first and the
witness operand second. Derived F/P, G/H and successor/predecessor X/Y
are expanded and their missing-witness behavior is proved. Pure L(U)
and L(S) locality includes the current point.

The reversal proof separately types first-order assignments and temporal
current points. Equality and unary predicates are unchanged; order atoms
reverse; U and S exchange without swapping operand positions. The proof
includes all quantifiers and modal cases, involution, commutation with
the first-order translation, and preservation of linearity, discreteness
and both Dedekind-completeness clauses. First/last points and neighbors
exchange roles.

The exact regional-stage induction maps a bounded Bet_G,n(a,b) with
actual endpoint variables to Bet_G,n(b,a), while before and after ray
components exchange their omitted guards. Formal infinities remain
notation and never become predicate arguments. Both signs and empty
child families are retained.

The discrete algorithm takes A to A*(x), applies the already complete
special normal form on the declared parameter list (x), groups each
clause into before/current/after lists, and uses the actual finite future
translator for every after component. A before component beta becomes
the temporal dual of the future translation of its first-order dual.
The proof explicitly passes through the discrete complete opposite model.
It never applies the disproved future-label complement rule at a formal
left endpoint in the original order.

Finite Boolean assembly gives the original GPSS conclusion at every
point of every discrete complete model. Current literal formulas belong
to both pure operator fragments. Empty factors, the empty outer list,
constants, first and last points and singleton orders are all included.
The procedure uses supplied finite constructions rather than search.

The worked all-linear-order identity is:
F(P q) iff ((P q OR q) AND F true) OR F(q AND F true).
Its proof classifies the past witness before, at or after the original
current point, retaining the same future witness. The two-point and
last-point calculations explain the necessary later-point condition.

## Correct complete-order comparison and the obstruction

The valid future base is the guarded fragment of TL(U,K-minus).
Its past dual is the guarded fragment of TL(S,K-plus-v), where
K-plus-v A(t) means forall r>t exists u in (t,r) A(u), equivalently
NOT((NOT A) U_s true). The v distinguishes this vacuous right limit
from the previously defined nonempty right limit. It is true at a
last point, matching reversal of the stipulated K-minus convention.

Temporal reversal maps K-minus to K-plus-v and maps the guarded future
grammar exactly onto the guarded past grammar. The full semantic
duality proves that the latter is past-dependent only. The complete
guarded future translator therefore provides its fully typed past dual.
Replacing the two discrete translators by these two guarded translators
gives the complete-order separation algorithm. Every limit operation
has its actual S/U expansion; this is a semantic-direction comparison,
not purification into L(S) and L(U). In the discrete case, stopping at
the encountered outermost limit nodes and replacing those entire
subformulas by false reduces the guarded factors to the pure fragments.

The requested failure of the pure-operator extension is proved explicitly.
The mixed formula Xi is
true U_s (P AND NOT((NOT P) S_s true)).
Its inner negated since condition says that P-points occur arbitrarily
close to the left of the strictly future marked witness.

In C1 = omega times [0,1), every future marked point (n,0) has an
unmarked left neighborhood beginning at (n-1,1/2), so Xi is false.
In C2 = omega^2 times [0,1), the marked point (omega,0) has marked
points after every earlier cut and below it, so Xi is true.
At their least points, all pure-since formulas agree by lack of an
earlier witness; all pure-until formulas agree by the full four-set
table and structural induction already proved. Every finite Boolean
combination of the two pure fragments therefore agrees as well.

For the full-real-line claim, identify each Ck with the nonnegative
real line, place its initial point at zero and give both models the
same entirely unmarked negative real past. Pure-since locality makes
their past formulas agree at zero, and pure-until locality preserves
their future agreement. The same explicit witnesses show Xi still
distinguishes them. All unused letters are false in both models.
This proves the obstruction over the real line, not merely over a
class containing first-point models.

## Root integration and remaining source boundary

Route the new body/annex after guarded-future-completeness. Existing
GabbayPnueliShelahStavi1980 and Rabinovich2014Kamp keys suffice.
The C1/C2 proof uses the already routed definitions/proof from the
Hirshfeld–Rabinovich presentation.

In n-c-012.tex, the Theorem 2.3 item can link
thm:p09-gpss-past-future-separation as the full construction.
The later paragraph stating that Theorem 2.3 is not proved locally
should preserve the historical fact about the GPSS paper and G2
while distinguishing the now-complete handbook proof. The complete-order
comparison should link thm:p09-gpss-complete-order-separation together
with thm:p09-gpss-pure-separation-obstruction; the pure-fragment statement
must retain discrete-complete scope.

No mathematical obligation remains within this assigned separation
presentation. The exact historical G2 body, the almost-future
presentation, wider dense-subset theorem and gap-operator presentation
remain their own source/proof obligations.

Local notation: pure L(S)/L(U) operator fragments (current atoms allowed),
A*(x), first-order versus temporal superscript d, opposite model,
T_F^dc/T_P^dc, Sep_dc, current clauses C_i and regional beta/gamma lists,
A_F/A_P and their guarded F/P classes, K-plus-v, T_F^com/T_P^com, and Xi.
In the worked example P denotes the strict-past modality; in the marked
models and Xi, P is the explicitly named proposition/marked predicate.
No shared notation file or macro was changed.
