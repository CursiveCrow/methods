# Ordered lattices, Heyting completeness, and intermediate logics

Date: 2026-09-06.

The actual Part X host and annex now include matching body/proof files
for priestley-duality, rasiowa-sikorski, heyting-completeness,
esakia-duality, and intermediate-algebras.

## Fifteen complete proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-prime-filter-separation | annex:p10.priestley.1 |
| thm:p10-priestley-representation | annex:p10.priestley.2 |
| thm:p10-priestley-reconstruction | annex:p10.priestley.3 |
| thm:p10-priestley-functors | annex:p10.priestley.4 |
| thm:p10-rasiowa-sikorski | annex:p10.rs.1 |
| thm:p10-heyting-examples | annex:p10.heyting.1 |
| thm:p10-heyting-completeness | annex:p10.heyting.2 |
| thm:p10-heyting-prime-representation | annex:p10.heyting.3 |
| thm:p10-ipc-prime-kripke-completeness | annex:p10.heyting.4 |
| thm:p10-esakia-objects | annex:p10.esakia.1 |
| thm:p10-heyting-prime-lift | annex:p10.esakia.2 |
| thm:p10-esakia-functors | annex:p10.esakia.3 |
| thm:p10-heyting-equational | annex:p10.intermediate.1 |
| thm:p10-intermediate-algebra-completeness | annex:p10.intermediate.2 |
| thm:p10-intermediate-variety-correspondence | annex:p10.intermediate.3 |

Prime-filter separation is proved using finite distributive lattices
and BPIT-based propositional compactness. The countable lattice case
has a separate ZF enumeration proof. Priestley duality includes
arbitrary-cover compactness, surjectivity onto all clopen upsets,
exact positive/negative membership reconstruction, and the morphisms
and naturality identities.

The Rasiowa--Sikorski dense-set lemma is now correctly distinguished
from prime-filter separation. Its proof states DC for an arbitrary
poset, and gives ZF proofs for an enumerated countable poset, a finite
dense family, and a finite poset.

Heyting completeness is proved from the actual propositional LJ
rules, including Cut and Mix. The quotient residual and distributivity
are derived, and the prime-filter implication witness yields strong
local Kripke completeness. BPIT is explicit for arbitrary variable
sets; countable languages use the countable separation theorem in ZF.
The algebraic arrow notation is explicitly identified with the
source's residual notation and the existing Part VIII convention.

Esakia duality includes all-clopen down-closure, the prime-filter
lifting argument for a Heyting homomorphism, and the continuous
p-morphism correspondence. The finite monotone-only counterexample
shows why the back condition is required. Empty spaces and trivial
algebras are included explicitly.

The intermediate-logic section proves finite equations for Heyting
algebras, general intermediate-L quotient completeness, and the
order-reversing correspondence between IPC-to-CPL and BA-to-HA.
Both empty-family endpoint conventions are explicit. Canonical
identity theories avoid a choice of axiomatizations for a family.

## Source and review

The original Esakia 1974 Russian article was acquired from MathNet:
tmp/pdfs/p10-priestley-heyting/esakia-1974-topological-kripke-models-ru.pdf.
Its perfect-topological-model formulation is distinguished from
the modern Priestley/prime-filter presentation. Other acquired
primary sources include Nick Bezhanishvili's 2006 thesis,
Moraschini's author notes dated 31 May 2023, and Priestley's 2019
author slides. Ciesielski's author-hosted book supplies the named
dense-set lemma. Exact metadata and locators are recorded in
p10-priestley-heyting-source-note-2026-09-06.md.

The original Priestley 1970 article body and Rasiowa--Sikorski 1963
book body remain unacquired. No complete reconstruction of those
unread manifestations is claimed.

Independent actual-LaTeX reviews passed after adding the explicit
BPIT hypothesis to the functorial Priestley theorem and correcting
the Moraschini application locator. The remaining source and
mathematical reviews found no concrete defect in the scoped texts.
Records:

- p10-priestley-rs-review-2026-09-06.md;
- p10-heyting-completeness-review-2026-09-06.md;
- p10-esakia-review-2026-09-06.md;
- p10-intermediate-algebras-review-2026-09-06.md.

## Integration

The active Part VIII intuitionistic supplement points readers to
the full Part X arguments. The Part X theorem/definition register
was regenerated with 90 rows. The named-theorem index contains all
fifteen proof links. Nineteen notation rows were added; the existing
formatter regenerated the symbol tables with 773 rows. The scoped
git whitespace check passed.

No software tests, manuscript build, or manuscript page renders were
used. The full publication goal remains active. These additions do
not establish whole-book source coverage, complete presentation
acceptance, final build/layout, or readiness for publication.
