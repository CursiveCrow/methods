# Cook–Reckhow 1979: N-c-027-01 author return

Date: 1 October 2026. Assigned existing allocation ED26-REQ-N-c-027-01,
N-c-027-MAP-01 and MAP-04. This source/working record is separate from the
reader manuscript and is not independent admission or whole-book completion.

## Exact original source acquired and read

Stephen A. Cook and Robert A. Reckhow, *The Relative Efficiency of
Propositional Proof Systems*, Journal of Symbolic Logic 44(1), March 1979,
printed pp.36–50, DOI 10.2307/2273702. Canonical key: `CookReckhow1979`.
Acquired freely from the author's University of Toronto page:

- Author page: https://www.cs.toronto.edu/~sacook/
- Exact PDF: https://www.cs.toronto.edu/~sacook/homepage/cook_reckhow.pdf
- Local: `source/references/cook-reckhow-1979/cook-reckhow-1979-journal-author-copy.pdf`.
- 393,905 bytes; 16 physical pages: JSTOR manifestation cover plus the
  complete fifteen original journal pages.
- SHA256 `4E70FFFE43358B4F169ACC460DEFFCA7DA5B80CE7335D5DBC99C782BC926EAA3`.

Read the entire original article, Sections 1–5 and references. Printed p.39
and pp.41–49 were additionally rendered and inspected for rule shapes,
ordered contexts, PHP indexing, extension conditions, gate equations and
quantitative/substitution claims. Neither the 1974 conference paper nor the
1976 Reckhow thesis was substituted for this original article.

Cook's own page supplies the correction to Corollary4.7: its complexity
premise is coNP unequal to NP, not P unequal to NP. Full HTML capture:
`source/references/cook-reckhow-1979/cook-author-homepage.html`, 23,201 bytes,
SHA256 `4EB137D7B8F4365BE26AB13668F08EFE1C9A5D4B06C2308E4D095F796C36ACA3`.
The correction is undated; access/capture date is not its publication date.
The intake adds `CookReckhow1979AuthorCorrection`, retaining the original
paper identity rather than creating a substitute version.

## Authored files and thirteen reciprocal proof pairs

- `handbook/parts/p07/presentations/n-c-027-01.tex`.
- `handbook/annex/p07/n-c-027-01.tex`.
- `handbook/bib/intake-p07-cook-reckhow.bib`.
- `handbook/registry/symbols-intake-p07-cook-reckhow.csv`.

The 13 pairs cover map/relation paired encoding, arbitrary-language NP
certificate equivalence including the empty case, exact NP/coNP reduction,
uniform simulation and its shortest-proof distinction, same-basis Frege
template replacement, both ordered-context ND conversions, extension
soundness/line-only elimination, all three gate skeleton cases, full-
constructor line compression, cross-basis relative bounds, uniform EF-to-
substitution conversion, the actual PHP induction and compressed theorem
proof, and the complete 19-node resolution DAG with 21-occurrence unfolding.

Cook–Levin NP-completeness is explicitly retained as the existing external
prerequisite, not purportedly reproved here. Haken's result retains its
existing sketch status and no new full-Haken proof gate was invented.
Haken1985, Beame–Pitassi1998, Krajicek2019, the Reckhow thesis and Statman
paper remain separate allocations and are not claimed as read or completed.
The existing dated Frege/extended-Frege open-status statement remains its
own date/source authority; the 1979 conjecture is not promoted to a theorem.

## Source and encoding repairs made in the actual exposition

Root repaired the old shared Frege definition to finite-premise
implicational completeness and the EF definition/sheet to exclude extension
variables from hypotheses and final conclusions. This source package uses
those repaired interfaces but did not change any shared file.

The map constructed from R(w,y) reads both y and w from its proof code.
It never performs an unjustified polynomial search over possible outputs.
Simulation handles invalid codes/default conclusions as well as valid
proofs. Source ND contexts are sequences and proof lines can be reused;
the shared-sequence comparison is not silently a tree-proof claim.
Same-basis p-simulation is kept separate from cross-basis existence bounds.
Extension elimination may have exponential output formulas even when its
line count increases only linearly; substitution pruning is theorem-only.

### Atom-only count versus full constructor size

The paper defines l(A) as atom/nullary occurrences at p.39, but asserts
that full def(A) has O(l(A)) occurrences at pp.46–47. For A=neg^r P,
l(A)=1 and there are r distinct nonatomic unary subformulas, hence r gate
definitions. That intermediate bound is false without controlling unary
runs. Atom counts also do not bound long binary identifier strings.

The active manuscript preserves l, lambda, rho and encoded-string length
as separate source measures and adds **m(A), all parse-tree nodes**.
Complete defining sets and full enumeration/line-overhead claims use m(A);
maximum leaf widths retain l(A). Relative bounds are proved for
nondecreasing L(m(A)); arbitrary bounds can first use their prefix maximum.
Polynomial encoded-proof consequences are unchanged because constructor
size is bounded by encoded size, and canonical atom renaming deals with
long identifiers. This corrects the intermediate size argument without
pretending the source's sharper unrestricted atom-only numerical claims
have been independently established. The primary PDF remains unchanged.

### PHP derivation and final-proof measures

The source has n pigeons and n-minus-one holes. Its clause family excludes
functionality clauses; the new text gives the explicit one-index shift to
the existing handbook family. All smaller-row and collision cases of the
source B_ij substitution are supplied. Fresh Q-stage atoms avoid expanding
the three-branch formula tree at every level.

The compressed clause derivation has O(n^4) lines and O(n) maximum leaf
count. Its final tautology neg(conj original clauses) has Theta(n^3) leaves,
so the smaller width bound cannot apply to every line of the full theorem
proof. The actual exposition uses a guarded derivation and a balanced
defining-circuit congruence bridge to obtain O(n^5 log(n+2)) encoded bits.
The bridge's summed subtree size is O(N log n), N=Theta(n^3), and its
largest/final line is allowed the necessary Theta(n^3) leaves. Naive
expanded-tree growth is not a minimum Frege lower bound.

The exact small resolution example has all nine input clauses and ten
derived clauses. Its only duplicated inputs on unfolding are the first
two pigeon rows, giving eleven leaves plus ten internal nodes. The
19-versus-21 counts are for that displayed proof and its own unfolding,
not an asserted optimality or exponential tree/DAG separation.

## Integration and remaining verification

Root owns routing, old statuses, canonical bibliography/symbol merge and
apparatus. No manuscript build, PDF layout inspection, consolidated review,
source admission or publication acceptance was run. A focused check with
the existing grammar found 13 matching body/annex pairs, initially 30
well-formed symbol rows and no own-file argument, pairing, body-proof or
first-use errors. A thirty-first row records the source's sigma/tau
substitution role with an exact global sentence-role override below.
Direct clause computation verified all ten resolution pivots, the empty
final clause, 19 DAG nodes and 21 unfolded-tree occurrences. These are
author calculations of actual finite objects, not prose-test software.
The final independent source-fidelity, topic and adversarial reviews remain
due after all authoring changes. The local source package does not solve
P/NP, NP/coNP, Frege lower bounds or the whole handbook completion goal.

### Exact proposed symbol bindings

Install after routing. Bare L has three separately typed roles, and bare
R has verifier and schematic-rule roles. These aliases use actual disjoint
regions, not a blanket collision override. The source's sigma/tau
substitution functions receive one exact, evidence-bound exception to the
broader global sentence-metavariable row.

```json
{
  "scopes": {
    "P7 Cook Reckhow source": {
      "presentation": "CookReckhow1979 encoded proof framework, measures, source calculi, gate constructions and PHP example",
      "regions": [
        {"anchor": "sec:p07-cook-reckhow-source"},
        {"file": "annex/p07/n-c-027-01.tex"}
      ]
    },
    "P7 Cook abstract proof languages": {
      "presentation": "Target string language L for an abstract source proof map",
      "regions": [
        {"anchor": "def:p07-cr-proof-map"},
        {"anchor": "thm:p07-cr-map-relation"},
        {"anchor": "thm:p07-cr-np-languages"},
        {"anchor": "annex:p7.cr.map-relation"},
        {"anchor": "annex:p7.cr.np-languages"},
        {"anchor": "annex:p7.cr.np-conp"}
      ]
    },
    "P7 Cook certificate relation": {
      "presentation": "Polynomial relation R on explicitly stored certificate and conclusion",
      "regions": [
        {"anchor": "thm:p07-cr-map-relation"},
        {"anchor": "annex:p7.cr.map-relation"}
      ]
    },
    "P7 Cook schematic rules": {
      "presentation": "R is a sound schematic calculus rule, not the verifier relation",
      "regions": [
        {"anchor": "annex:p7.cr.frege-comparison"},
        {"anchor": "annex:p7.cr.nd-comparison"},
        {"anchor": "annex:p7.cr.gate-compression"},
        {"anchor": "annex:p7.cr.substitution-simulation"}
      ]
    },
    "P7 Cook ordered ND": {
      "presentation": "L is an ordered-context source natural-deduction line",
      "regions": [
        {"anchor": "def:p07-cr-source-nd"},
        {"anchor": "annex:p7.cr.nd-comparison"}
      ]
    },
    "P7 Cook relative extension bounds": {
      "presentation": "L is a nondecreasing line bound on full constructor size",
      "regions": [
        {"anchor": "thm:p07-cr-ef-relative-bounds"},
        {"anchor": "annex:p7.cr.ef-relative-bounds"}
      ]
    },
    "P7 Cook formula substitutions": {
      "presentation": "CookReckhow1979 simultaneous formula substitutions and their composition",
      "regions": [
        {"anchor": "annex:p7.cr.frege-comparison"},
        {"anchor": "annex:p7.cr.nd-comparison"},
        {"anchor": "annex:p7.cr.gate-compression"}
      ],
      "overrides": [{
        "glyph": "\\(\\sigma,\\tau\\)",
        "local_role": "simultaneous source formula substitutions",
        "first_use": "annex:p7.cr.frege-comparison",
        "broader_scope": "global",
        "broader_role": "sentence metavariables",
        "source": "CookReckhow1979",
        "reason": "Source Definition2.1 and the actual substitution lemma bind sigma and tau as maps simultaneously replacing propositional atoms by formulas. The current annex constructs and composes those maps; they are not sentences in the global first-order metavariable convention."
      }]
    }
  }
}
```
