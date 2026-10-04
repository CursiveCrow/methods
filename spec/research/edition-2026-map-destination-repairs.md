# Destination defects recorded during coverage mapping

Date: 9 September 2026. This records remaining integration work found by
reading the current LaTeX and its environment definitions. It does not
report a compilation, mathematical review, or publication decision.

## Undefined proof environment

The active handbook package, handbook/handbook.sty, defines annexitem with
three arguments at line 1632. Its proof environment is restricted to the
annex treatment at lines 1645 onward. No hbproof definition occurs in the
package or any current .tex, .sty, or .cls source searched beneath handbook/.

Four drafted, routed annex files instead use a two-argument hbproof wrapper:

- handbook/annex/p15/huber-information-game.tex
- handbook/annex/p15/huber-joint-endpoints.tex
- handbook/annex/p15/huber-remaining-methods.tex
- handbook/annex/p19/mental-rotation-and-spatial-reasoning.tex

Their derivation text is present in the actual files. The existing named-entry
parser does not recognize this wrapper, so the first destination export does
not enumerate these derivations as annex items. Its earlier interpretation
that all four were retained inside recognized enclosing annex text was wrong:
the rotation file, for example, starts a chapter and immediately opens hbproof.

Required integration repair after the map phase: convert each wrapper to the
established annexitem/proof form, preserving the exact target and back-reference
identities and supplying an accurate proof title. Reconcile the body proof
targets with those actual labels. Success requires every affected derivation
to be reachable through the maintained proof interface; failure includes an
undefined environment, a discarded derivation, or a target that names a
different result. The consolidated production checks remain pending.

## Preserved unpublished continuations

The standard small-clause body and optimization body/annex remain unrouted.
The standard body promises thirteen proof destinations, but its annex is
unwritten. The optimization author's final read-through is unfinished.
These drafts must remain partly authored in the map. The source-specific
checkpoint is spec/research/edition-2026-p12-small-clause-standard-checkpoint.md.

P17.19 epistemic-nash-conditions and P19.11 explanatory-preferences are routed.
Their combined bibliography and symbol intakes still require canonical
integration. Neither a routed chapter nor an existing proof text establishes
that this integration or the final content review has passed.
