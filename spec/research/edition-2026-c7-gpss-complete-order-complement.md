# C7 author handoff: corrected complete-order target and original counterproof

8 September 2026. Block began 14:22 UTC. The dispatch initially inferred
U-only future completeness on all complete orders. Exact source checking
showed that target is false; root explicitly redirected authoring to the
correct original nonexpressibility proof. The owned new body and annex now
supply that proof and the valid language distinction. They do not leave
the impossible theorem as an unfinished promise.

## Files and acquisition

Owned new files:

- handbook/parts/p09/presentations/gpss-complete-order-complement.tex
- handbook/annex/p09/gpss-complete-order-complement.tex
- This note.

All three were absent at dispatch. Only these manuscript/research files were
edited. Root separately authorized the following source acquisition.

Primary: Yoram Hirshfeld and Alexander Rabinovich, Future temporal logic
needs infinitely many modalities, author version dated 6 March 2003,
16 numbered pages. The author's
[publication list](https://www.cs.tau.ac.il/~rabinoa/journal1.html)
links the [unchanged compressed PostScript](https://www.cs.tau.ac.il/~rabinoa/future1.ps.gz).
The associated journal record is Information and Computation 187(2),
196–208, published 15 December 2003,
DOI 10.1016/S0890-5401(03)00163-9. The held body is the dated author
version, not a claimed byte-identical copy of the journal's thirteen pages.

| Object | Bytes | SHA256 |
| --- | ---: | --- |
| source/references/hirshfeld-rabinovich-future-2003/future1.ps.gz | 89843 | E08DF9241BB4E738B99AEA70A94884CC53CB20756BA068D45D197E013C9D35C0 |
| source/references/hirshfeld-rabinovich-future-2003/future1.received.ps | 229739 | EF30DCFD8C2821F398BFEF350125AFE19D1990C6439A537313F0A23DFDEA2EB1 |
| tmp/pdfs/p09-hirshfeld-rabinovich-2003/future1-raw.ps | 229739 | EF30DCFD8C2821F398BFEF350125AFE19D1990C6439A537313F0A23DFDEA2EB1 |
| tmp/pdfs/p09-hirshfeld-rabinovich-2003/future1.pdf | 248864 | 80F0D790519877E0510F9F0AD8DE1476B909DFFC51152D3D1E0AA0CF6CC06B9C |

The initial HTTP client automatically decoded the compressed response,
yielding the PostScript saved as future1.received.ps. A raw download then
preserved the actual compressed object. Its decompressed payload has exactly
the same hash as that first PostScript. The PDF is a Ghostscript reading
derivative, not an original source PDF or manuscript output. Its extracted
text and source-page images are in the same tmp reading folder. Text extraction
loses some glyphs; the relevant displayed formulas were read from page images.

Personally read the complete sixteen-page primary: definitions and scope,
ordinal Lemmas 3.1–3.5 and Theorem 3.6, real construction and Lemmas 4.2–4.5,
Theorem 4.1, concluding qualifications, and the entire game appendix.
The limit hierarchy on p. 10 was checked visually against its source formula.
The complete held GPSS pp. 169–171 were also reread. Their announced
complete-order modification concerns Kamp's S/U result; the discrete
Theorem 2.2 does not become a U-only theorem over arbitrary complete orders.

The research/PDF skills guided source reading and provenance. All four
agent slots were occupied. The saved LaTeX received an author whole-batch
read-back; there were no independent reviews, review waits, scanners,
tests, manuscript builds or manuscript renders.

## Eight complete proof pairs

| Result | Reciprocal annex |
| --- | --- |
| thm:p09-hr-ordinal-game | annex:p9.hr.ordinal.game |
| thm:p09-hr-ordinal-tail | annex:p9.hr.ordinal.tail |
| thm:p09-hr-limit-separator | annex:p9.hr.limit.separator |
| thm:p09-hr-continuous-models | annex:p9.hr.continuous.models |
| thm:p09-hr-modal-invariance | annex:p9.hr.modal.invariance |
| thm:p09-hr-no-finite-future-basis | annex:p9.hr.no.finite.future.basis |
| thm:p09-gpss-until-complete-order-obstruction | annex:p9.gpss.until.complete.order.obstruction |
| thm:p09-hr-guarded-future | annex:p9.hr.guarded.future |

The ordinal-game proof is supplied rather than delegated to the source's
external Ehrenfeucht citation. It proves the stronger interval statement
omega^n alpha + rho versus omega^n beta + rho, rho < omega^n, using
nonzero finite Cantor polynomials alpha,beta. Every first-move location,
repeated point, left/right subgame and quantifier-depth consequence is proved.
This gives the exact ordinal equivalence required by the source.

The ordinal tail isomorphisms imply homogeneity for predicate-free future
formulas. The corrected future separator retains its reference point x
inside every limit operation. Its nth limit holds at precisely the positive
ordinal points whose last n coefficients vanish, giving threshold k>n
in omega^k. Predicate restriction carries this to the marked real models.

The real model is C_k = omega^k times [0,1), lexicographically ordered,
with P at the zero coordinate of every block. Completeness, a countable
dense subset, and a back-and-forth plus completion construction prove the
isomorphism with the nonnegative real line. Both marked and unmarked tail
types are treated. The ordinal game lifts by copying the second coordinate,
preserving order, equality and colour at every round.

For arbitrary temporal nesting with truth-table depth at most d, operand
truth sets reduce uniformly to true, false, P or not-P in every k>d.
Substitution adds no depth; the two class-wide sentences use exactly one
additional quantifier. The comparison is therefore applied at d+1, with
the integer margin k,m>=d+1 made explicit.

The resulting finite-basis contradiction proves the original real theorem,
the ordinal theorem and the rational extension. Every basis modality has
finite arity and a first-order future truth table. A finite basis has a
finite depth bound; no restriction is placed on the nesting depth of its
formulas. Extra proposition letters are handled by fixing them false.
Full real and rational lines follow by prepending an arbitrary fixed past
and applying the proved future scope.

For U alone there is an additional direct four-by-four truth-set table,
valid in every C_k. It shows that already the rank-three future formula
P(x) AND exists future marked t approached from below by marked points
separates C_1,C_2 while every U-only formula agrees there. This is a smaller
worked counterinstance than the general depth argument's phi_3^P.

The corollary also proves that the enlarged left-labelled bounded
decomposition class is not closed under every relative complement over Com.
Assuming that closure would complete the exact GPSS regional induction via
the already proved positive operations and ray translation, contradicting
the explicit real U-only counterinstance. This rules out the former
general final-gap target in that grammar, not just one proposed algorithm.

## Direct mathematical/source corrections

Source p. 10 defines psi_(n+1) as the left limit of psi_n, but prints
phi_n = exists t>t0 psi_(n+1)(t) while asserting the threshold k>n.
That displayed formula has the next threshold. The manuscript directly uses
the nth limit and proves the stated k>n threshold.
The source also says no point of omega^n satisfies psi_n, despite the
vacuity of its universal limit at zero. The new L_n(x,t) includes x<t
for positive levels; the positive witness and reference-point scope are
explicit, so no exceptional zero is misclassified.

The manuscript preserves the source's vacuous K-minus convention:
forall r<t exists u in (r,t) A(u). It is true at a first point and
differs from a nonvacuous past limit. The language of arbitrary U,K-minus
formulas is distinguished from its Boolean/atomic fragment in which every
K-minus lies under strict U. The entire guarded fragment is proved future
by induction at points strictly beyond a retained initial point. The
past-limit subformulas themselves need not be future.

## Remaining exact source obligations and positive basis

The core original nonexpressibility construction is complete. The following
are distinct further source claims, not missing steps of the proved result:

- Section 5 item 1 states a wider obstruction for an arbitrary order
  containing a dense-in-itself subset (Theorem 5.2), without its full proof.
- Section 5 item 2 refers to a positive U-only result under finite variability,
  explicitly saying that its proof is not given there.
- Section 5 item 3 attributes completeness of the guarded U,K-minus
  fragment to Gabbay–Hodkinson–Reynolds Theorem 10.3.20. Its full positive
  proof is not in this acquired paper.
- Section 5 item 4 conjectures an almost-future completeness result.
  A later separate primary is Pardo–Rabinovich, No Future without (a hint of)
  Past, author PDF https://www.cs.tau.ac.il/~rabinoa/pub/no-future.pdf,
  published Information and Computation 247 (2016), 203–216.
  Its introductory definitions and exact positive theorem were consulted
  online to locate the error and original 2003 source. Its whole proof was
  not acquired/read or silently substituted for the 2003 presentation.

The exact GPSS SS/G2 manuscript bodies remain unacquired. None of these
boundaries is a promise of U-only completeness on arbitrary complete orders.
The valid Kamp S/U theorem and all ten preceding local boundary results
retain their actual hypotheses and proofs.

## Root integration and corrected prior paragraphs

Route the new body and annex after gpss-complete-order-boundaries.
Add bibliography key HirshfeldRabinovich2003Future. Suggested metadata:
authors Yoram Hirshfeld and Alexander Rabinovich; title Future temporal logic
needs infinitely many modalities; journal Information and Computation;
year 2003; volume 187; number 2; pages 196--208;
DOI 10.1016/S0890-5401(03)00163-9; author URL as above;
note that the held author version is dated 6 March 2003 and manuscript
source locators use its sixteen-page pagination.

The prior reader paragraphs requiring direct correction were:

1. gpss-complete-order-boundaries.tex opening paragraph: its claimed
   complete-order future extension and upper-boundary continuation.
2. The same file, def:p09-gpss-complete-boundary-continuation: “The full
   extension still requires ... Only after that step can negation close
   the full regional induction” and its final promise of the “full
   future-completeness extension”.
3. gpss-decomposition-complement.tex, the final paragraph of
   thm:p09-gpss-discrete-future-completeness: the statement that the
   arbitrary-complete conclusions merely require more boundary work.
4. n-c-012.tex, the paragraph near the announced complete-order
   modification, if read as promising that same future-only basis.

Root had already corrected all four live paragraphs by the author read
at 14:45 UTC. They now retain discrete U-only scope and the actual
Kamp S/U announcement. They can now link
thm:p09-gpss-until-complete-order-obstruction for the completed negative proof.
No further edits to those shared/prior files were made by this author.

Local notation intake: FTL_d, O_k, ordinal padding alpha/beta/rho,
equiv_n and the finite-round game, L_n(x,t), phi_n and phi_n^P,
C_k and P_k, the four truth sets, K-minus with its explicit endpoint
convention, and the guarded fragment of A. No shared macro was added.
