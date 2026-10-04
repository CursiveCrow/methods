# Independent mathematical review: C3, C4, and C5

Reviewed on 2026-09-07 in `C:/Dev/the-methods-of-reason`. Work began at 13:49 UTC; the completed findings and unchanged primary hashes were checked at 13:53 UTC, before the 15-minute checkpoint and within the 45-minute limit.

| Correction | Verdict | Scope of verdict |
| --- | --- | --- |
| C3 / INV-CTL-001 / A-146 | PASS | The explicitly negative root and all four CTL verdicts on the specified infinite total tree. |
| C4 / R-032 | PASS | The arithmetic signature, seven closed axioms, full semantics, finite conjunction, and placement before the reduction's use of the notation. |
| C5 / R-030 | PASS | The complete DLO countable-categoricity proof, including extension cases, the union construction, and countable-model existence. |

These verdicts concern the mathematics of the identified corrections. No mathematical defect or missing inference was found within those scopes. They do not constitute source-fidelity review, formal admission, publication acceptance, or acceptance of other results in the surrounding chapters.

## Reviewer and method

Reviewer: the Codex collaborator `/root/edition_small_topic_review`, working independently from the other topic reviewers. The precise backend model identifier and reasoning configuration were not exposed to this reviewer; both are unavailable. This is an agent review, not a human review.

The review used the actual manuscript and input drivers. No correction provenance note, other review output, or author conclusion was used to decide the mathematical verdicts. The three primary files matched the SHA-256 values specified in the assignment. No manuscript file was edited. No tests, builds, renders, formal proof checker, or external source comparison were run.

## C3 / INV-CTL-001 / A-146 — PASS

Primary evidence: `handbook/parts/p08/temporal-epistemic-supplement.tex:46–104` and `329–353`.

The definition at lines 46–56 requires a nonempty state set and a successor at every state, with paths indexed by the natural numbers. The next clauses at lines 69–74 inspect immediate successors. The strong-until clauses at lines 80–99 allow the witness index to be zero. The previously routed abbreviation `F A = top U A` is at `handbook/restoration/inherited-13340-13409.tex:56–60`; `handbook/parts/p08.tex:22,32` places that inherited material before this supplement. Thus the figure's eventualities expand as `EF p = E(top U p)` and `AF p = A(top U p)`.

The diagram explicitly labels the root `w: not p` at line 332, its left successors `u:p`, `u_1:p` at lines 333 and 335, and its right successors `v:not p`, `v_1:not p` at lines 334 and 336. The two labelled dotted tails at lines 337–338, with the continuation statement at lines 349–351, specify an infinite all-positive left branch and an infinite all-negative right branch. They are part of the structure, so the calculation includes the continuing tails.

| Evaluation state | EF p | AF p | EX p | AX p |
| --- | --- | --- | --- | --- |
| Root `w` | true | false | true | false |
| Every state of the continuing left branch | true | true | true | true |
| Every state of the continuing right branch | false | false | false | false |

At `w`, the left path witnesses `EF p` at index 1. The entire right path `w,v,v_1,...` has no occurrence of `p`, including at index 0, and therefore witnesses failure of `AF p`. The immediate successor `u` witnesses `EX p`; the immediate successor `v` refutes `AX p`. These are exactly the four displayed verdicts at lines 346–347. At a left-branch state, eventuality already holds at index 0 and its successor satisfies `p`; at a right-branch state, neither its current state nor any successor satisfies `p`.

The explicit negative root closes the relevant zero-index issue: if `p` held at the root, the given strong-until semantics would make `AF p` true there regardless of later right-branch labels. The present text excludes that interpretation.

## C4 / R-032 — PASS

Primary evidence: the complete `handbook/parts/p02/pa2-definition.tex:1–42` and the active seam at `handbook/parts/p02.tex:49–53`.

Lines 4–8 identify the first-order nonlogical signature `{0,S,+,times}` and logical equality. The constant, unary successor, and two binary arithmetic operations have the required arities; lines 26–30 make the domain nonempty and the function interpretations total. Unary relation-variable quantification is permitted by the preceding syntax at `handbook/restoration/inherited-12262-12289.tex:4–21`.

There are exactly seven closed conjuncts:

1. Zero is not a successor, at line 11.
2. Successor is injective, at line 13.
3. One second-order induction sentence, at lines 14–16.
4. Addition at zero, at line 17.
5. Addition at a successor, at line 19.
6. Multiplication at zero, at line 20.
7. Multiplication at a successor, at lines 22–23.

Every object-variable occurrence is bound. The only relation variable is `X`, bound by `forall X`, and its unary arity is explicitly stated at line 26. The induction antecedent asserts that `X` contains zero and is closed under successor; its consequent asserts that `X` contains the entire object domain. Lines 26–31 correctly give `X` the full powerset range, agreeing with `handbook/restoration/inherited-12290-12355.tex:4–29`. This is one closed second-order sentence and does not introduce an infinite induction scheme.

The first three axioms agree with the displayed successor axioms in `handbook/restoration/inherited-12356-12414.tex:4–21`. Its proof at lines 29–53 obtains the bijection `f:N -> M` by iterating successor, using injectivity and zero's exclusion from the successor range for injectivity of `f`, and applying full induction to the actual range of `f` for surjectivity. Its expanded-signature assertion at lines 55–58 is supported by the four new recursion equations: induction on `m` gives `f(n+m) = f(n) +^M f(m)`, then gives `f(n*m) = f(n) times^M f(m)`. The addition base and step are conjuncts 4–5; the multiplication base and step are conjuncts 6–7 together with the addition identity. Since every domain element is an `f(m)`, the equations determine the operations everywhere. The standard natural-number structure satisfies all seven axioms under full semantics.

The driver first inputs the syntax and full semantics, then the successor-categoricity section, then this definition, and then `scope-SRC-12415-12536`. Each of the three relevant inherited wrappers was read and directly inputs its named body. Consequently `PA_2` is explicitly defined before the use at `handbook/restoration/inherited-12415-12536.tex:35–51`. Lines 36–39 of the new definition correctly state that `PA_2 -> sigma` is a single second-order sentence with a fixed finite antecedent, for a first-order sentence `sigma` in this signature.

The definition supports the intended full-categoricity equivalence: every model of its antecedent is isomorphic to the standard arithmetic structure, and that standard structure itself satisfies the antecedent. The later passage still labels itself a proof sketch and expressly leaves the reduction/effectiveness and computability proof unreproduced at lines 49–51. This review does not upgrade that later proof to complete.

## C5 / R-030 — PASS

Primary evidence: the complete `handbook/restoration/inherited-07295-07468.tex:1–217`, with the DLO theorem and proof at lines 108–175. The ambient DLO signature and nonempty-domain assumption are explicitly stated in `handbook/restoration/inherited-07150-07294.tex:28–34`.

The proof begins with a finite order-preserving bijection `g:A -> B` and a fresh domain element `a` at lines 123–125. Its sets `L` and `U` at lines 127–128 partition `B`: every old domain element is strictly below or strictly above `a`, and injectivity excludes overlapping images. Order preservation ensures that every member of `L` precedes every member of `U`.

All four finite-cut cases at lines 135–146 are valid:

- If both sets are nonempty, their finite extrema satisfy `max L < min U`, and density supplies a point strictly between them.
- If only `L` is nonempty, absence of a greatest element supplies a point above `max L`.
- If only `U` is nonempty, absence of a least element supplies a point below `min U`.
- If both sets are empty, `B` is empty, and the nonempty-domain convention supplies a point.

The freshness argument at lines 148–150 is sufficient. A point strictly above all of `L` and strictly below all of `U` cannot belong to either set; in the empty case, there is no old image to collide with. The extended map is therefore injective and maps onto `B union {b}`. For every old element, the new comparison is correct in both directions, as stated at lines 151–154. Old comparisons persist. Moreover, an injective order-preserving map between subsets of strict linear orders reflects order: a reversed preimage comparison would force the reversed image comparison, and equality cannot account for a strict image comparison. Thus inversion is justified.

At lines 156–161, the odd stages apply the same valid extension construction to the inverse map, with the two structures interchanged, and then invert back. This extends the old map and inserts the selected target element into its range. The proof correctly invokes density and endpoint assumptions in the structure that now receives the new image.

The increasing union at lines 163–169 is a function, because every later map extends earlier assignments, and is injective, because any two assigned pairs appear together at a finite stage. Selecting the first unused enumerated element at successive even and odd stages reaches every element of both enumerations, giving totality and surjectivity. Each pair of domain elements appears together at a finite stage, where preservation and reflection have already been established. The union is therefore an isomorphism in the signature `{<}`. Nonempty linear orders without endpoints are infinite, so no finite stage exhausts a model; choices of witnesses can also be taken by first suitable element of the given enumeration.

Finally, lines 169–174 supply the existence clause required by the definition of categoricity at lines 4–8. The rationals are countable by integer/positive-integer pairs, infinite because they contain the integers, dense by arithmetic means, and have neither endpoint because `q-1 < q < q+1`. Thus there is a model of cardinality aleph_0 as well as uniqueness up to isomorphism at that cardinality.

## Consulted manuscript ranges and hashes

SHA-256 values below identify the inspected snapshot. `Full` means every line of that file was read. Reading surrounding statements does not extend the mathematical verdict beyond the three scopes above.

| File | Consulted range | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p08/temporal-epistemic-supplement.tex` | Primary review: 46–104 and 329–353; adjacent 306–328 and 354–361 also read | `3028f3196a8f8fc064a06e5e7aec3366fad90aa042fceaf0645825aa70eddb56` |
| `handbook/parts/p02/pa2-definition.tex` | Full, 1–42 | `6a5467b748c91f6cb9c8484e6c7e7b122a0268ecc80fc3a8c7213b92251d4a63` |
| `handbook/restoration/inherited-07295-07468.tex` | Full, 1–217 | `1958b3363dcac80b5c7af56f446e74591b4249d23c1c8543cc9ec7de7bb93a89` |
| `handbook/restoration/inherited-12262-12289.tex` | Full, 1–28 | `c8a9e39ead545f11cea7e93d7888defa393a457c45ca8564ea9ddb4d5e304fcc` |
| `handbook/restoration/inherited-12290-12355.tex` | Full, 1–66 | `dd9a1564fa0d18d05d5a9ff0adc5f67b3accf6f9cf465a8efb1016a12d4da1b0` |
| `handbook/restoration/inherited-12356-12414.tex` | Full, 1–59 | `3b850ff37842e3e024ac32b23712aa199db010ad2249e764bb590afc2ed89a04` |
| `handbook/restoration/inherited-12415-12536.tex` | Full, 1–122; reduction focus 35–51 | `d4ff50a3145acac19b3e7a6054bcf0aef4aac1eb2e774f825ade02af2693f667` |
| `handbook/parts/p02.tex` | Full, 1–65; active seam 49–53 | `bf76eb346924365e7d06eb3596cf22b266d61ea6ff24096b6c527fd9f8151e0c` |
| `handbook/restoration/scope-SRC-12290-12355.tex` | Full, 1–3 | `55ffdcc9b8765c3a8b1f3b9a2f5960c7fb3638896fa0bd08b4b0208552e91c04` |
| `handbook/restoration/scope-SRC-12356-12414.tex` | Full, 1–3 | `bfd9ab6381d6f3363d0649d4aa8af23e203d4d387316d0e658c283bb1ff5506d` |
| `handbook/restoration/scope-SRC-12415-12536.tex` | Full, 1–3 | `64c44650d51baf9f8b3b8a879fb1144b1714f601fca05c44d5a4b511770a323e` |
| `handbook/parts/p08.tex` | Full, 1–69 | `18a9d459d89930dd02ec3e337acb806e4a1eb307938e4cc4e699d42428b0af27` |
| `handbook/restoration/scope-SRC-13340-13409.tex` | Full, 1–3 | `ab202371a4fcc71b65e35be7a2a81958d8482538442d814d83477324607601fc` |
| `handbook/restoration/inherited-13340-13409.tex` | 20–65; eventuality definition 56–60 | `d1aff8ed64d08f6ac6f751cd51bc7cc4dd81d7c77093ea51d318fe424aec1ba7` |
| `handbook/restoration/inherited-07150-07294.tex` | 23–41; DLO definition 28–34 | `ccb19227218a479328d04079082c149bbd9acf4b587c45d13fff49a07548eff8` |

All assigned primary ranges were read without an unresolved truncation. An initial broad display of the temporal supplement was truncated; the assigned semantics and figure were then reread in bounded, untruncated excerpts. No full-file review of that supplement is claimed: lines 1–45, 105–305, and 362–756 are outside the bounded reading used for this verdict. The supplemental inherited temporal file was not read at lines 1–19 or 66–70, and the supplemental DLO-definition file was not read at lines 1–22 or 42–145. Those ranges are outside the assigned corrections.

## Remaining gates

Independent source-fidelity/provenance review and any required edition admission remain separate work. No build, static check, rendering, visual inspection, formal proof checking, or human review is established here. C4 does not complete the later effective-validity reduction proof; the manuscript's explicit sketch boundary remains. Any subsequent change to the primary hashes requires checking whether these findings still apply.
