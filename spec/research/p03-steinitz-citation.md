# S-011 research check: the Steinitz citation for \(\mathsf{ACF}_p\)

Research date: 2026-08-10.

## Verdict

The primary source required by S-011 is Ernst Steinitz, “Algebraische
Theorie der Körper,” *Journal für die reine und angewandte Mathematik* 137
(1910), 167--309, DOI
[10.1515/crll.1910.137.167](https://doi.org/10.1515/crll.1910.137.167).
The authoritative article record and scan are supplied by the
[Göttingen State and University Library](https://resolver.sub.uni-goettingen.de/purl?GDZPPN002167042).

Steinitz proves the classification at the level needed here: algebraically
closed fields have one isomorphism type for each fixed characteristic and
absolute transcendence degree. He then records separately, as an easy
cardinality consequence, that an uncountable field has cardinality equal to
its absolute transcendence degree. The modern statement that
\(\mathsf{ACF}_p\) is \(\kappa\)-categorical for every uncountable
\(\kappa\) is the combination of those two facts; it is not a
model-theoretic theorem stated in that terminology in the 1910 paper.

The current `cited=Marker2002` is a mathematically adequate modern secondary
locator, but it does not supply the requested *Steinitz citation*. Read in
isolation, the acceptance sentence “The result is labeled with status and
citation” could be satisfied by any citation; read as part of the complete
S-011 row, whose remedy says “with the Steinitz citation,” Marker alone is
insufficient. Add the primary `Steinitz1910` record and make it the status
citation. Marker may remain as an additional modern exposition.

## Verified primary record

| Field | Verified value |
|---|---|
| Author | Ernst Steinitz |
| Title | *Algebraische Theorie der Körper* |
| Publication | *Journal für die reine und angewandte Mathematik* |
| Original volume | 137 |
| Year | 1910 |
| Pages | 167--309 |
| DOI | [10.1515/crll.1910.137.167](https://doi.org/10.1515/crll.1910.137.167) |
| Authoritative scan/catalog | [SUB Göttingen article PURL](https://resolver.sub.uni-goettingen.de/purl?GDZPPN002167042) |

The original scan identifies the journal as “Bd. 137.” The current
De Gruyter/Crossref deposit instead serializes the archival scheme as
`volume=1910, issue=137`. For an historical bibliography matching standard
citations to the original publication, use `volume={137}` and `year={1910}`;
do not turn 137 into an issue number.

## Claim-to-source map

All page numbers below are the printed journal pages in the primary scan.

| Claim needed by the handbook | Primary-source locator | Exact support and ceiling |
|---|---|---|
| Algebraic closures exist and are unique up to an isomorphism extending the base-field isomorphism. | Steinitz 1910, §21(9), p. 287 (proof continues on the following page). | Steinitz states that every field can be extended algebraically to an algebraically closed field, essentially in only one way, and proves invariance under isomorphism of the base field. This is the algebraic-closure ingredient, not yet the classification by transcendence degree. |
| A purely transcendental extension is determined over its base field by the cardinality of a transcendence basis. | Steinitz 1910, §22(5), p. 289. | A bijection between the algebraically independent generating systems induces an isomorphism of the corresponding rational-function fields over the base. |
| Absolute transcendence degree and the classes indexed by characteristic \(c\) and absolute transcendence degree \(t\) are defined. | Steinitz 1910, §23, pp. 299--300. | Steinitz defines transcendence degree as the cardinality of an irreducible (algebraically independent) system, defines the absolute degree over the prime field, and allows \(c=0\) or prime and \(t\) finite or any transfinite cardinal. |
| For each fixed characteristic and absolute transcendence degree there is exactly one algebraically closed field type. | Steinitz 1910, §23(6), pp. 300--301, especially p. 301. | This is the substantive Steinitz classification. In modern notation: if \(K\) and \(L\) are algebraically closed, then \(K\cong L\) exactly when they have the same characteristic and \(\operatorname{trdeg}_{P}K=\operatorname{trdeg}_{P}L\), where \(P\) is their (corresponding) prime field. It does **not** classify countable algebraically closed fields by characteristic and cardinality alone. |
| Algebraic extension does not enlarge the cardinality of an infinite field; if \(t>\aleph_0\), every field in the characteristic/transcendence-degree class has cardinality \(t\). Hence an uncountable field's cardinality equals its absolute transcendence degree. | Steinitz 1910, §24, p. 301. | Steinitz explicitly presents this as a further easy consequence of cardinal arithmetic. It is the bridge from equal uncountable cardinality to equal transcendence degree, not the classification theorem itself. |
| Algebraically closed fields of fixed characteristic and fixed uncountable cardinality are isomorphic. | Derived from Steinitz 1910, §23(6) and §24, p. 301. | This is a corollary of the preceding two rows. Steinitz illustrates it at p. 301 for characteristic \(0\) and continuum cardinality; the same stated class calculation applies to every characteristic and every \(t>\aleph_0\). |

## Exact modern scope for the handbook result

Fix \(p=0\) or a prime and an uncountable cardinal \(\kappa\). Let
\(K,L\models\mathsf{ACF}_p\) with \(|K|=|L|=\kappa\). Their prime fields
are correspondingly isomorphic (\(\mathbb Q\) when \(p=0\), and
\(\mathbb F_p\) when \(p\) is prime). If \(B_K,B_L\) are transcendence
bases over those prime fields, then

\[
  |K|=\max(\aleph_0,|B_K|),\qquad
  |L|=\max(\aleph_0,|B_L|).
\]

Because \(\kappa>\aleph_0\), both bases have cardinality \(\kappa\).
A bijection \(B_K\to B_L\) induces an isomorphism of the purely
transcendental subfields, and uniqueness of algebraic closures extends it to
\(K\cong L\). Existence at size \(\kappa\) follows by taking a set \(B\)
of size \(\kappa\) and an algebraic closure of \(P(B)\). Therefore
\(\mathsf{ACF}_p\) is \(\kappa\)-categorical.

This argument uses the well-ordering/Choice background employed explicitly by
Steinitz in §§23--24 and already assumed in the handbook's model-theory
part. The uncountability hypothesis is essential: algebraic closures of
\(P\) and of \(P(t)\) are both countable models of \(\mathsf{ACF}_p\), but
their transcendence degrees are respectively \(0\) and \(1\), so they are
not isomorphic.

## Ready-to-use BibLaTeX record

Recommended key: `Steinitz1910`.

```bibtex
@article{Steinitz1910,
  author       = {Steinitz, Ernst},
  title        = {Algebraische Theorie der K{\"o}rper},
  journaltitle = {Journal f{\"u}r die reine und angewandte Mathematik},
  volume       = {137},
  pages        = {167--309},
  year         = {1910},
  doi          = {10.1515/crll.1910.137.167},
  url          = {https://resolver.sub.uni-goettingen.de/purl?GDZPPN002167042},
  urldate      = {2026-08-10},
  langid       = {german},
}
```

Recommended use for S-011: `cited=Steinitz1910` on the labeled
uncountable-categoricity result, with `\cite{Steinitz1910,Marker2002}` in the
explanatory paragraph if the modern Marker locator is retained.
