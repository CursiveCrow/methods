# Stone duality and countable atomless Boolean algebras

Date: 2026-09-06.

## Mathematical content supplied

The actual Part X host now includes two complete developments:

- handbook/parts/p10/stone-duality.tex;
- handbook/parts/p10/countable-atomless.tex.

Their full proofs are in the matching files under handbook/annex/p10,
both included by the active annex driver.

The first development replaces the previous short Stone proof with
ultrafilter dichotomy and avoiding-element extension; compactness of
the ultrafilter topology for arbitrary open covers; the Boolean
representation isomorphism onto every clopen; reconstruction of each
Stone space from its clopen algebra; and both inverse-image functors.
It proves the composition laws, naturality equations, inverse
identities, and recovery of a unique Boolean homomorphism from every
continuous map between dual spaces.

The two assertions formerly combined in the Stone theorem are retained
as adjacent representation and functorial-duality statements, each
with a complete proof. The general proofs use ZF + BPIT, with no
additional Choice hidden in selecting basic neighborhoods. The
one-element Boolean algebra and empty Stone space correspond, including
their maps. Proper filters explicitly exclude zero.

The second development supplies finite Boolean atom decomposition,
finite-subalgebra splitting extensions, and back-and-forth uniqueness
of the nontrivial countable atomless algebra. It constructs the clopen
algebra of Cantor space, proves compactness by a bad-cylinder recursion,
establishes its finite levels and direct-limit universal property,
and gives an explicit homeomorphism from Cantor space to the Stone
space of every such algebra. The general atom/isolated-point
correspondence has a separate proof.

Nontriviality is now explicit. Under the definition allowing trivial
Boolean algebras, the trivial algebra is vacuously atomless and would
otherwise be a counterexample to the unqualified uniqueness/Cantor
claim. The finite and countable proofs work in ZF; the arbitrary
atom/isolated-point statement specifies BPIT.

## Stable theorem/proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-ultrafilter-separation | annex:p10.stone.1 |
| thm:p10-stone-representation | annex:p10.stone.2 |
| thm:p10-stone-space-reconstruction | annex:p10.stone.3 |
| thm:p10-stone-duality | annex:p10.stone.4 |
| thm:p10-atomless-extension | annex:p10.atomless.1 |
| thm:p10-countable-atomless-uniqueness | annex:p10.atomless.2 |
| thm:p10-cantor-cylinder-algebra | annex:p10.atomless.3 |
| thm:p10-countable-atomless-stone | annex:p10.atomless.4 |
| thm:p10-atoms-isolated | annex:p10.atomless.5 |

## Source and review

Primary source: the acquired Burris--Sankappanavar Millennium Edition,
2012 update. IV §§3–4, printed pp. 127–141, supplies the
filter/ultrafilter and object-representation results. The source places
the morphism constructions in IV §4 Exercises 9–10, p. 140; the
manuscript supplies their proofs and the naturality calculations.
Countable uniqueness is IV §1 Exercise 5, p. 121. The countably
infinite free Boolean algebra/Cantor connection is IV §4 Exercise 3,
p. 140, and atoms/isolated points is Exercise 11, p. 141.

The complete source locators and source-scope review are in
p10-stone-duality-source-note-2026-09-06.md and
p10-stone-duality-source-review-2026-09-06.md.
Independent actual-LaTeX mathematical reviews found no defect in
either body and its full annex proof sequence. The countable source
review requested the explicit phrase “countably infinite free Boolean
algebra”; this was incorporated and read back.

These bounded reviews support the supplied mathematical statements.
They do not establish complete reconstruction of every registered
Stone/Boolean source or whole-book publication acceptance.

## Integration and remaining work

The active Part X theorem/definition register was regenerated with
40 rows. The named-theorem index was updated from generator output
for Part X only, including all nine proof links. Thirteen notation
rows were added, and the existing symbol formatter regenerated its
two reader tables with 728 rows. The scoped git whitespace check
passed.

No software tests, manuscript build, or manuscript renders were used
in this authoring pass. Broader source acquisition, complete
presentation coverage, navigation consistency outside the updated
scope, final compilation/layout, and publication acceptance remain
unverified. The full manuscript goal remains active.
