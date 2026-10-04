# Edition 2026 C7: Kamp's primitive-recursive translation

Date: 8 September 2026. Author: /root/kamp_lemma7_author.
Repository: C:\Dev\the-methods-of-reason. Block: 09:30-10:15 UTC.
Standing: authored quantitative construction and proof; consolidated reviews remain deferred.

## New artifacts

Both manuscript paths and this note were checked unused before writing.
Only these three assigned files were created.

| Artifact | Lines / bytes | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-primitive-recursive-translation.tex | 263 / 13,085 | 2B22A93879A9490F071CD193890A6C015D9CFF44520E199E09AE5B208ED1546E |
| handbook/annex/p09/kamp-primitive-recursive-translation.tex | 412 / 22,787 | AECB975FB40620D2F83441DCFABC93BE02C40D250718353AF1E6F5066E34E184 |

Four complete reciprocal pairs cover finite syntax coding, nonrecursive
operation envelopes, the full Lemma 8 recursion bound, and the complete
primitive-recursive translation. The final pair is
thm:p09-kamp-primitive-recursive-translation /
annex:p9.kamp.primitive.recursive.translation.

## Exact primary source

Kamp, *Tense Logic and the Theory of Linear Order*, UCLA, 1968; Kamp1968.
Held PDF: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf.
[Institutional source](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Verified unchanged SHA256:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.

Complete printed pp. 21-30 were personally read in this block, including
the exact defining-formula convention on p. 21, exact n-place schema
condition on p. 23, strict SINCE/UNTIL definitions on p. 26, and the
primitive-recursive Exp statement on p. 28. Physical pages are printed
pages plus 9. The source gives the assertion and points to the Chapter III
construction; the numerical encodings and bounds in the new text are
explicit handbook details implementing the already written corrected proof.
Fresh source-page images are retained in the old task workspace under
tmp/pdfs/kamp-pr-source/. No manuscript PDF was rendered.

The actual Lemma 8 localization/assembly implementation, original-node
normal-form procedure, and subsequent full translation were read from the
current LaTeX. Research and PDF skill instructions were reread personally.
The author was the parent's assigned researcher; no subagent or independent
review was launched. The PDF-authoring marker was inapplicable to source reading.

## Quantitative construction supplied

The natural-number encoding uses nil=0 and cons(a,b)=2^a(2b+1).
Explicit prefix tags encode the full source first-order connectives and
the original temporal language. A decoded token list of weight
1 + length + sum of tokens has code below 2^weight. Parsing, binder
tracking, freshening, substitution and all finite enumerations have
bounded primitive-recursive implementations. Operation/frame tags,
evaluation phases, order of children, masks, relation matrices and
fresh-name policies are specified; malformed numerical inputs have a
fixed total-function default.

For a pure Lemma 8 family, structural mass retains every At tree and
basic predicate word. One child has mass at most (M+3)(s+1).
At a fixed maximum length, multiplicity falls at every edge, so a level
lasts no longer than its entry mass. Its exit mass is bounded by
(M+3)^(2(s+1)). Explicit ordinary primitive recursion over at most M+1
levels gives B, a bound for every family mass, and h, a depth bound.
At most 33 regional computations each have at most 2^(M B) cut tuples;
each tuple is compiled once before output-package products are distributed.
This yields c for immediate branching and z=(c+1)^(h+1) for the entire tree.
The one fresh child predicate increases the branch maximum index by one;
it does not use an uncontrolled global counter across unrelated outputs.

R(t)=2^(2^(2^((t+16)^4))) and its explicit 32(t+1)^2-fold iteration A
bound nonrecursive frozen-input sweeps. The proof accounts for candidate
enumeration, copied labels, fresh indices, Boolean products, fusions,
substitution expansion and code-arithmetic loops. Explicit u_i bounds
then include every returned child representation before parent assembly.
L_8 bounds the complete recursive evaluator, not merely one descending path.

The fixed functions J,S,C,V,W bound the outer original-node services,
primitive-region conversion and maximal-proper-region restoration.
They are compositions or ordinary iterations of already defined functions;
there is no assumption that arbitrary lexicographic recursion is primitive
recursive. The final T(n) covers initial expansion, standard form,
elementary construction, temporal construction, schema padding and the
literal D-image. Bounded iteration of the specified primitive-recursive
transition followed by output projection supplies the numerical Exp function.

The worked code example is Exp(7)=3 for P_0(t_0) and q_0. The family
example has M=3 and mass 7; its actual whole-interval child is the two-atom
family {P_0,P_4} of mass 5, and the uniform one-edge bound is 48.
The whole-level bound 6^16 is verified separately from the actual
one-edge maximum-level behavior of this small example.

## Exact source arity and necessary boundary

The source's n-place defining formula contains every P_0,...,P_(n-1),
and its n-place schema contains every q_0,...,q_(n-1), not merely a subset.
The output therefore receives a tautological conjunct for each missing
permitted proposition letter. This is primitive recursive and preserves
the Com truth condition and original strict S/U syntax.

The source says "some number n" without stating a zero-arity convention
at that passage. If n=0 is included literally, no zero-place TL_1 schema
exists: every formula contains a proposition letter, by induction on its
positive-arity grammar. The active theorem states the exact positive-arity
result and proves this syntactic exception. Zero-predicate one-free-variable
inputs receive an equivalent unary schema independent of q_0, explicitly
labelled as such. Gapped signatures have the deterministic numerical
extension n=1+maximum predicate index. No nullary schema or new language
constant is fabricated.

## Verification and root handoff

The complete authored body and annex were read back; later typing and
dispatch clarifications were checked. The existing scanner reports zero
findings, four reciprocal proof pairs, 17 labels and valid bibliography
keys. No test, manuscript build/render, generator, commit or review was
performed. Prior manuscript files were not edited. The frozen original
remains 0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC.

Input the body and matching annex after kamp-iii2-completion.tex in their
respective root-owned routes. Kamp1968 already supplies all references.
Notation intake, local P9.4: list code #, weight w, prefix and frame tags;
R,A and iteration f^[k]; family mass mu; bounds b_i,B,h,c,z,s_*,u_i,L_8,L;
outer bounds J,S,C,V,W,n_i,T; the numerical Exp function and its decoded
formula use; source schema arity and padding. These are mathematical
construction bounds, not practical performance estimates.

The positive-arity Chapter II Theorem 2 strengthening is now supplied in
the authored text, with the nullary boundary explicitly handled. The
required next activity for these files is integration with the remaining
writing followed by the user's consolidated assessment; no per-lemma
review wait was introduced.
