# P15.42: Consistent learning and description length

## Completed source-based authoring

Parent U5 statistical generalization and learning. Eight complete
statement/proof groups are saved and routed in:

- handbook/parts/p15/occam-learning.tex
- handbook/annex/p15/occam-learning.tex

Body: 12,819 bytes; SHA-256
6CD3C753E8218D5DD9C622D6E1E1841E5025C7679AEA67DB7AE5E8AB000A4B1B.
Annex: 12,295 bytes; SHA-256
39CC0972F7E58BF2D3B90FF62276C4836651691F3A40976EB441D2F6F212CD98.
Chapter: sec:p15-occam-learning.
Annex: sec:annex-p15-occam-learning.

## Exact primary and reading

Anselm Blumer, Andrzej Ehrenfeucht, David Haussler and Manfred K. Warmuth,
Occam's Razor, Information Processing Letters 24(6), 377-380,
6 April 1987. DOI 10.1016/0020-0190(87)90114-1.
Key: BlumerEtAl1987Occam.

Held file:
source/references/blumer-ehrenfeucht-haussler-warmuth-1987/occam-1987.pdf.
SHA-256: B06F286C016F5E752A22278B556F2924F299DC9767A2FBD629D897944E9D891D.
Size: 456,267 bytes. Four physical pages are exactly printed pages
377-380. The image-only PDF's empty text extraction was not used as
mathematical evidence. All four pages were read as page images,
including every proof, equation, footnote, open-problem passage and
bibliography entry. The first page shows receipt February 21, 1986
and revision July 18, 1986; neither is the publication date.

Successful university copy:
https://homepages.math.uic.edu/~lreyzin/papers/blumer86.pdf

Discovery page:
https://homepages.math.uic.edu/~lreyzin/w19_eecs496-10/

Publisher identity:
https://www.sciencedirect.com/science/article/pii/0020019087901141

The course page and filename use 1986; the actual journal scan and
publisher identify the 1987 article. The old UCSC author page now
redirects to the engineering-school homepage, and the discovered
Buffalo path returned 404. Neither failed endpoint was recorded as
a source body. A text-only mirror was a retrieval lead, not the final
equation authority. The successful four-page scan supplies the exact
original rather than a later textbook exposition.

## Proof map and source scope

Each suffix has a thm:p15- statement and annex:p15. proof:

| Suffix | Content |
| --- | --- |
| occam-finite | Source Lemma 2.1, full simultaneous union bound, integer sample threshold and exponential relaxation. |
| occam-threshold-example | Four explicit functions, all wrong-hypothesis survivor events, exact inclusion-exclusion and minimal sample size. |
| occam-code-count | All-length binary-string count, prefix-free descendant count and Kraft inequality. |
| occam-compression | Full source Definition 2.2 and Theorem 2.3 implication, with both arbitrary-code and prefix-free constants and the unchanged polynomial order. |
| occam-minimum-approximation | Source a=0 case, direct improved sample bound and the explicit approximately-minimum consistent-length implication. |
| occam-weighted | Editorial countable weighted-union extension, including arbitrary and prefix-free descriptions. |
| occam-boundaries | Complete dependence, distribution-shift, post-sample class and conflicting-label examples. |
| occam-unseen-labels | Editorial finite lower bound obtained by averaging over all binary targets. |

The statistical finite/countable-class argument permits measurable input
spaces and functions. The source's computational representation framework
uses a countable input domain with finite effective encodings. Runtime
polynomial in encoded sample length is distinguished from sample count
polynomial in target size and probability tolerances. The target is
realizable, labels noiseless, and a proper consistent output is required.

## Direct mathematical corrections and clarifications

The source's Theorem 2.3 proof counts at most 2^L hypotheses represented
by binary strings of length at most L. That is not the general count
for arbitrary variable-length strings: including the empty word, the
correct count is 2^(floor(L)+1)-1. Already at L=1 the empty word, zero
and one give three possible codes. The manuscript uses this count in
the active general formula, yielding ln(2/delta) in the first split
bound. It separately proves the sharper prefix-free count and supplies
the source's displayed bound under that convention. The source's
asymptotic polynomial learnability conclusion survives unchanged.

The proof does not introduce a decoder selected after observing the
sample. Its short-code output class is fixed by the size bound n,
sample size m and original representation. The weighted extension fixes
its allocation before sampling and is not identified with a Bayesian
posterior. Empty codes, aliases, sample repetitions, both probability
tolerances and large uninformative bounds are explicit.

The threshold example has exact failure probability
2(2/3)^m-(1/3)^m. For tolerance 1/4 and failure target 1/20, its
smallest sufficient m is 10, while the generic four-function bound
gives 16. These are fully derived values, not a simulation or test.

The lower-bound random target is a proof device showing that some
fixed target has large expected error. It is not a hidden new prior
assumption in the distribution-free upper bound.

## Integration and remaining edition obligations

Root read the complete saved LaTeX body and annex once after writing,
made the input-space and encoding scope explicit, and retained the
full probability-parameter range in the asymptotic bound. Body, annex,
source key and P15.42 notation are integrated. No independent review,
scanner, test, manuscript build, manuscript render or formal admission
check ran. The source PDF skill was used only to read the original
four pages; manuscript content was written in the actual LaTeX.

This completes the paper's proved finite-class/Occam implication and
its zero-exponent specialization, with its source discussion accurately
bounded. The NP-hard consistency reductions cited by the paper, Pearl's
separate comparison, the full Valiant1984 source, later converse results,
noise and agnostic learning, VC theory, general losses and subsequent
learning methods remain separate source obligations. The 1987 open-
problem discussion is historical; it is not presented as a statement
that those problems remain open at the 2026 cutoff. The full approved
manuscript objective remains active.
