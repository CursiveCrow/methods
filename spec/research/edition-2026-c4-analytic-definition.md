# Edition 2026, C4: analytic derivation defined at the chapter opening

Date: 7 September 2026. Requirement S-013. This is authoring evidence, not
independent acceptance or completion of the full cut-elimination development.

The active chapter `handbook/restoration/inherited-11711-11740.tex` began with
the title Cut Elimination and Analytic Derivations and immediately discussed
cut measures. Its later fragments used analytic derivations without defining
the phrase. The definition in the former
`parts/p07/cut-elimination-and-interpolation.tex:91-104` is inactive and did not
satisfy the requirement.

The new editorial definition `def:p07-analytic-derivation` is inserted after the
active chapter heading and label, before its first section. It states the
propositional cut-free/subformula meaning and the first-order meaning modulo
capture-avoiding term substitution and bound-variable renaming. It explicitly
explains variables released by removal of outer quantifiers, the language of
allowed terms/eigenparameters, and retention of each inference's freshness
conditions. Subformulas use the selected calculus's primitive syntax, including
expansion of declared abbreviations.

## Evidence and limits

Before authoring, the lead read the entire active initial fragment, the
subformula definition, lemma and first-order qualification in
`inherited-11824-11881.tex`, and the consequences/warning in
`inherited-11882-11913.tex`. The selected notation remains the active source's
LK/LJ notation. The qualification also agrees with the active solution's
closing paragraph in `inherited-15489-15619.tex:125-129`.

The example P(t) as an instance of the subformula P(x) of a universally
quantified formula explains the required distinction; it does not assert that
arbitrary term instances satisfy eigenvariable side conditions. The definition
does not upgrade the existing cut-elimination sketch or prove the corresponding
theorem for equality, modal, induction or other extended calculi.

Baseline initial-fragment SHA256:
`4c6f8be640199f18188ceaac918574a1a2a23973a5e4cd7193b207e53e1f471e`.
The insertion preserves the original chapter title, label and remaining source
text. The frozen archive is unchanged. Current provenance comparison must
record this editorial addition rather than claim a byte-exact transcription.

Independent source/topic/publication review, current provenance admission and
output checks remain open. No software tests, build or render was used to
substitute for the definition's mathematical review.
