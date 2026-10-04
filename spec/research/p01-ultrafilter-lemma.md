# Part 1 research note: Ultrafilter Lemma and Choice

Purpose: calibrate the citation required by defect S-005 when the
Ultrafilter Lemma is migrated from an unstatused definition to a cited
theorem.

## Verified source

J. D. Halpern and A. Lévy, “The Boolean prime ideal theorem does not imply
the axiom of choice,” in Dana S. Scott (ed.), *Axiomatic Set Theory, Part 1*,
*Proceedings of Symposia in Pure Mathematics*, vol. XIII, Part I, American
Mathematical Society, 1971, pp. 83–134, MR0284328.

- [AMS chapter record](https://www.ams.org/books/pspum/013.1/0284328)
- [AMS volume and contents](https://bookstore.ams.org/pspum-13-1/)
- [Primary scan at p. 83](https://books.google.com/books?id=TVi2AwAAQBAJ&pg=PA83)

## Claim ceiling

The opening pages define an extension SP of ZF and announce a forcing proof
that consistency of ZF implies consistency of SP.  Among the theorems of SP
are the Boolean Prime Ideal Theorem and the existence of a Dedekind-finite
dense set of reals, hence failure of Choice.  The supported calibration is

\[
\operatorname{Con}(\mathsf{ZF})
\Longrightarrow
\operatorname{Con}(\mathsf{ZF}+\mathsf{BPI}+\neg\mathsf{AC}).
\]

Together with the ZF proof that AC implies BPI, this supports the usual
relative non-implication/strictness statement.  It does **not** support an
unconditional assertion of consistency or the phrase “absolute
independence.”  The handbook theorem must retain this conditional wording.

Over ZF, the Ultrafilter Lemma and BPI are the choice-principle formulations
being compared here; the handbook should not call the Ultrafilter Lemma a
second name for AC.
