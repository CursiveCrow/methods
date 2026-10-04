# W3C OWL 2 Profiles (Second Edition, 2012): primary-source note for N-c-010

Prepared 2026-08-22 (America/Los_Angeles). This note is confined to the dated W3C Recommendation that controls N-c-010, the two dated normative OWL 2 documents needed to type its syntax and inference tasks, and the primary papers needed to distinguish the Recommendation's profile names from their description-logic lineages. It does not update the 2012 complexity claims from later literature.

## 1. Reading contract, terminology, and claim standing

The controlling body is *OWL 2 Web Ontology Language: Profiles (Second Edition)*, W3C Recommendation 11 December 2012. I read its dated HTML body in full, including the status material, Sections 1--7, acknowledgments, and normative and nonnormative references. The Structural Specification was consulted only at the opening conditions of Section 3, Sections 3.1 and 3.4, Sections 5.1--5.8.1, Section 7 and its admitted-constructor subsections, Sections 8.4.1--8.4.2, Sections 9.3.5, 9.4--9.5, and Section 11; Direct Semantics was consulted only at Sections 1, 2.4, and 2.5. These are the normative locations needed here to type an ontology and axiom closure, entity IRIs and literals, data-range arity, data restrictions, datatype definitions, keys, inherited restrictions, and inference tasks. [Profiles, title/status and contents](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/), [Structural Specification, ontology conditions](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontologies), [Structural Specification, axiom closure](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Imports), [Structural Specification, entities and typing](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Entities.2C_Literals.2C_and_Anonymous_Individuals), [Structural Specification, data ranges and restrictions](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Data_Ranges), [Structural Specification, global restrictions](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Global_Restrictions_on_Axioms_in_OWL_2_DL), [Direct Semantics, inference problems](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Inference_Problems).

All constructor names in CamelCase below are W3C functional-style-syntax names, not handbook coinages. **Class**, **Datatype**, **ObjectPropertyExpression**, **DataPropertyExpression**, **ClassExpression**, **DataRange**, and **Axiom** likewise denote source grammar nonterminals. *Ax* denotes the source's axiom closure: all axioms in the import closure, with anonymous individuals in different imported ontologies standardized apart. [Profiles, Section 1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Introduction), [Structural Specification, Section 3.4](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Imports).

This note uses one eliminable metalinguistic abbreviation, **profile-legal axiom shape**. Its five-part standing is supplied here:

- **Necessity:** “accepted syntax” alone would ambiguously conflate a single production with the ontology-wide typing and global restrictions.
- **Definition:** a displayed axiom shape is profile-legal exactly when there exists an ontology axiom closure containing an instance of that shape that satisfies the profile's entity, datatype, grammar, OWL 2 DL typing, and inherited and profile-specific global restrictions. A shape is profile-illegal when the cited production or explicit restriction rules it out.
- **Standing:** this is a metalinguistic abbreviation about source grammar membership, not a class, property, ontology entity, semantic relation, or new logical object.
- **Nonredundancy:** profile legality is neither semantic satisfiability nor entailment; a legal axiom can participate in an inconsistent ontology, and an illegal shape can express a meaningful formula outside the profile.
- **Use:** the abbreviation is used only for the requested legal/illegal examples and the pairwise non-subset witnesses in Sections 4--7 below.

In every displayed example, IRIs beginning with a colon are illustrative. Required class/property declarations are assumed, as are absence of unrelated axioms that would violate a global restriction. The Structural Specification itself omits declarations in examples when types are clear, but its axiom closure still must declare every class, datatype, object-property, data-property, and annotation-property occurrence in the appropriate type; property types are pairwise disjoint, and class and datatype types are disjoint. Individual declarations are optional. [Structural Specification, Section 5.8.1](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Typing_Constraints_of_OWL_2_DL).

The evidential labels **source-verified**, **derived**, and **printed inconsistency** are also eliminable metalinguistic annotations:

- **Necessity:** an unqualified “claim” would not distinguish a statement printed by W3C from this note's grammar check or from a defect in the printed body.
- **Definition:** source-verified means stated in the cited primary body; derived means obtained by a direct membership or nonmembership check against cited productions and not presented as a W3C-authored example or theorem; printed inconsistency means a literal conflict or malformed production in the dated Recommendation and not an official erratum or permission to rewrite that body.
- **Standing:** all three labels classify claims about sources; none names an ontology entity, a semantic relation, a class of OWL interpretations, or a new logical object.
- **Nonredundancy:** source-verified reports what the source says; derived reports what follows by checking its grammar; printed inconsistency reports why those two operations do not yield one coherent result at a particular location.
- **Use:** the first two labels govern the examples and non-subset witnesses in Sections 4--7; the third governs the defects isolated in Section 11.

## 2. Exact version, status, editors, stable URLs, and rights boundary

### 2.1 Controlling Recommendation

The exact title is *OWL 2 Web Ontology Language: Profiles (Second Edition)*. Its status line is “W3C Recommendation 11 December 2012.” The dated “This version” URL is <https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/>; the series URL is <https://www.w3.org/TR/owl2-profiles/>; the generic latest-Recommendation URL printed by the edition is <https://www.w3.org/TR/owl-profiles>; and its previous version is the Proposed Edited Recommendation of 18 October 2012. The Recommendation says there were no substantive changes from that previous version, describes itself as stable and citable, and warns that later documents may supersede it. [Profiles, document header and Status of This Document](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#w3c_status).

The six editors, in printed order, are Boris Motik (University of Oxford), Bernardo Cuenca Grau (University of Oxford), Ian Horrocks (University of Oxford), Zhe Wu (Oracle), Achille Fokoue (IBM Corporation), and Carsten Lutz (University of Bremen). [Profiles, document header](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/).

The informative change log distinguishes this Second Edition from the 27 October 2009 Recommendation: XSD 1.1-dependent OWL 2 features became required; Section 5's computational-properties presentation was edited for clarity and precision; a redundant `ReflexiveObjectProperty` production was removed from the RL Appendix grammar; and listed minor typographical errors were corrected. The dated 2012 edition, not the 2009 edition, controls every grammar and Table 10 claim in this note. [Profiles, Section 7.1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Changes_Since_Recommendation).

The two dated normative companions used here are:

- *OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)*, W3C Recommendation 11 December 2012, edited by Boris Motik, Peter F. Patel-Schneider, and Bijan Parsia; dated URL <https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/>. [Structural Specification, header](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/).
- *OWL 2 Web Ontology Language: Direct Semantics (Second Edition)*, W3C Recommendation 11 December 2012, edited by Boris Motik, Peter F. Patel-Schneider, and Bernardo Cuenca Grau; dated URL <https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/>. [Direct Semantics, header](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/).

### 2.2 Lawful public access and reuse boundary

All three dated W3C bodies were retrieved by anonymous HTTPS GET from the W3C technical-report namespace. Each carries “Copyright © 2012 W3C (MIT, ERCIM, Keio), All Rights Reserved” and links W3C document-use rules. The archived 2002 W3C Document License says it applied to W3C documents published before 31 January 2015; it permits copying and distribution, in whole or part, without fee or royalty when the original URL, pre-existing copyright notice, and document status are carried, but did not generally grant modification or derivative-specification rights. Its archive banner says the 2015 license was later applied to documents previously under that license. The header's current document-use redirect resolves to the 2023 license, which also permits copying/distribution with attribution and status and still restricts publication of derivative W3C technical specifications. These facts establish a public right to read and cite and a conditioned right to copy; they do **not** make the Recommendation public domain or authorize an altered substitute specification. [Profiles, copyright notice](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/), [W3C 2002 Document License](https://www.w3.org/copyright/document-license-2002/), [W3C 2023 Document License](https://www.w3.org/copyright/document-license-2023/).

The four research-paper copies were retrieved from an author/institutional site or the conference site linked by W3C. They retain their respective publisher or conference rights; the SROIQ copy expressly states AAAI copyright and “All rights reserved,” and the DL-Lite copy states Springer Science + Business Media copyright. They are used here only to identify their own syntax, theorem scope, and historical relationship, not to republish their bodies. [SROIQ, PDF p. 1](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf), [DL-Lite, journal p. 385 / PDF p. 1](https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf).

### 2.3 Capture manifest

Acquisition date for all entries is 2026-08-22 local time. W3C HTML is unpaginated, so section/table anchors, not synthetic page numbers, are the controlling locators. PDF page counts are physical PDF pages reported by `pdfinfo`. Text files are deterministic `pdftotext -layout` derivatives and are not independent authorities.

| Captured file | Provenance / identity | Bytes | Pages | SHA-256 |
|---|---|---:|---:|---|
| `REC-owl2-profiles-20121211.html` | dated W3C Profiles Recommendation | 182,784 | unpaginated HTML | `1599D792A39FE30000913822DEFFD78CB0905542C3EE3D956EFC9E51A7273C05` |
| `REC-owl2-syntax-20121211.html` | dated W3C Structural Specification Recommendation | 480,916 | unpaginated HTML | `2849F489758F82DF474536D66DDD86BCA8CF96F67500CE063FAA172DC29EBF7A` |
| `REC-owl2-direct-semantics-20121211.html` | dated W3C Direct Semantics Recommendation | 69,981 | unpaginated HTML | `282DB71227A69895C6113E4141AC32AA8DFD5DD1E87420FA57245898F7B89022` |
| `BaaderBrandtLutz-IJCAI-05.pdf` | *Pushing the EL Envelope*, TU Dresden author/institutional copy | 170,023 | 6 | `4C9CAA8C224506123B7EE06CFCC8F5759D3537F4C241BB7E6BDDCB89E0727A5A` |
| `BaaderBrandtLutz-OWLED-2008.pdf` | *Pushing the EL Envelope Further*, W3C-linked OWLED site copy | 154,998 | 10 | `D68DE99A3E6D613B116D405B562EC7F8030CDFA75B2449820D10240EB1868C99` |
| `CalvaneseEtAl-JAR-2007.pdf` | *Tractable Reasoning and Efficient Query Answering in Description Logics: The DL-Lite Family*, author/institutional copy | 878,072 | 45 | `3ADF046934B01EAEDB9783F406B129C414515E6A187F2EC7E52008F072AA8164` |
| `HorrocksKutzSattler-KR-2006.pdf` | *The Even More Irresistible SROIQ*, Oxford author copy | 281,733 | 11 | `21235D525BD45B8DE924EE6700BD974E6AF1B8BE89C10F7B0A4E7C6EBC28ED0A` |
| `BaaderBrandtLutz-IJCAI-05.txt` | extraction of the identically named PDF | 46,380 | n/a | `8EF7D7100BC9B0BFEEE675BCEADE1BBBAA9FA0C524DD4FF1434463326DC5E710` |
| `BaaderBrandtLutz-OWLED-2008.txt` | extraction of the identically named PDF | 31,483 | n/a | `41DFA72483C39FFFA1248C6A7A20C18B0925EBACC6ACB92581D1AF70E7C7EA40` |
| `CalvaneseEtAl-JAR-2007.txt` | extraction of the identically named PDF | 148,459 | n/a | `F9350B186A8F2121E7C4CBF5E64C127D98FA0921740D849CF86359A80188C2DE` |
| `HorrocksKutzSattler-KR-2006.txt` | extraction of the identically named PDF | 80,903 | n/a | `F3814D6AAD841A478248A5BFF354C05B69BF5CDA2E5D2394D90ABA3873414E8E` |
| `Calvanese-publications.html` | Diego Calvanese institutional publication index establishing the hosted JAR copy | 288,502 | unpaginated HTML | `3C92389F10AED30EAB0FBBA8D2183925D7A542F4EC9C76A69D587D22BD5C350E` |
| `Calvanese-JAR-2007-bibliography.html` | institutional bibliographic page for the JAR article | 2,700 | unpaginated HTML | `996AE3AEAA41CD12BBB97C6FC63F08C7571C81EEE1CFA7417D55B396C2BFE82D` |
| `W3C-document-license-2002.html` | archived license applicable at 2012 publication | 28,387 | unpaginated HTML | `73101ED2E566DE5DAC8FF8F438FC24EF32D206687330AEF7B2B640416D60AF7E` |
| `W3C-document-use-rules.html` | current document-use redirect, 2023 license | 27,941 | unpaginated HTML | `BAF4BD39646BCA6636F035E16AEFD82B2AE0A04AE1AA58DED96922C3C1BCD752` |
| `OWL2-errata.html` | current W3C OWL 2 errata page | 35,195 | unpaginated HTML | `FF1CC1B56B2A3A956D54E7D99FD97DA2389A3B3829D010750473238483253EE1` |

All captures are under `tmp/sources/p09-w3c-owl2-profiles-2012/`.

## 3. What a profile restricts, and what every profile inherits

The Recommendation calls profiles “fragments” and defines them by restrictions on OWL 2 ontology structure. It says the restrictions are expressed by modifying functional-style-syntax productions and, where necessary, adding global restrictions; a profile ontology may nevertheless be serialized in any OWL 2 syntax. The three profile definitions are independent: the Recommendation explicitly says none is a subset of another. [Profiles, Abstract and Section 1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Introduction).

Profile membership is checked over the whole axiom closure, not an isolated visible file. Every EL, QL, and RL ontology must satisfy the OWL 2 DL typing rules and Structural Specification Section 11 restrictions; EL adds one more range/chain condition. [Profiles, Sections 2.2.6, 3.2, and 4.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Global_Restrictions), [Structural Specification, Sections 5.8.1 and 11](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Global_Restrictions_on_Axioms_in_OWL_2_DL).

Several inherited OWL 2 structural conditions apply before Section 11's global restrictions:

- An ontology may have a version IRI only if it has an ontology IRI; neither IRI may use reserved vocabulary in OWL 2 DL. Every directly imported ontology must itself satisfy the OWL 2 ontology conditions. [Structural Specification, Section 3 opening](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontologies), [Structural Specification, Section 3.1](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Ontology_IRI_and_Version_IRI).
- Reserved-vocabulary IRIs may identify entities only in the built-in positions allowed in Sections 5.1--5.6, and every literal's lexical form must belong to its datatype's lexical space. [Structural Specification, Sections 5.1--5.7](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Entities.2C_Literals.2C_and_Anonymous_Individuals).
- A datatype introduced as the subject of `DatatypeDefinition` must be explicitly declared. Such a defined datatype has an empty lexical space and therefore cannot type a literal; it supports no facets and therefore cannot occur as the datatype in `DatatypeRestriction`. The profile grammars already omit `DatatypeRestriction`, but the literal prohibition remains substantive because EL, QL, and RL admit literal-bearing forms. [Structural Specification, Section 9.4](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Definitions).
- Every data range explicitly defined by OWL 2 is unary. Datatypes and `DataOneOf` are unary, and `DataIntersectionOf` requires equal-arity operands and preserves that arity. A `DataSomeValuesFrom` or `DataAllValuesFrom` with *n* data-property expressions requires a data range of arity *n*; `DataPropertyRange` and `DatatypeDefinition` require unary data ranges. Consequently, although the EL and RL productions print a one-or-more data-property list, every standard profile expression of either form has exactly one data property, because every data range admitted by EL, QL, or RL is unary. [Structural Specification, Section 7 opening, Sections 7.1 and 7.4, Sections 8.4.1--8.4.2, Section 9.3.5, and Section 9.4](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Data_Ranges).
- A `HasKey` grammar permits two individually empty property lists, but the ontology condition requires at least one object- or data-property expression in total. [Structural Specification, Section 9.5](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Keys).

The inherited Section 11 global conditions are, independently restated:

1. **Axiom-closure scope.** Imports are included and anonymous individuals from different ontology documents are standardized apart. [Structural Specification, Sections 3.4 and 11](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Imports).
2. **`owl:topDataProperty`.** It may occur only as the super-data-property expression of `SubDataPropertyOf`. [Structural Specification, Section 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#The_Restrictions_on_the_Axiom_Closure).
3. **Datatype definitions.** Every datatype in the closure must be `rdfs:Literal`, a member of the OWL 2 datatype map, or the subject of exactly one `DatatypeDefinition`; a strict partial order must orient every referenced datatype below the datatype being defined, so definitions are acyclic. [Structural Specification, Section 11.2, “Restrictions on Datatypes”](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#The_Restrictions_on_the_Axiom_Closure).
4. **Simple object properties, with the source predicates eliminated.** For an object-property expression `OPE`, `INV(OPE)` swaps a named `OP` with `ObjectInverseOf(OP)`. `AllOPE(Ax)` is the smallest set containing `OP` and `INV(OP)` for every named object property `OP` occurring in `Ax`. `OPE` is **composite in `Ax`** exactly when (i) it is `owl:topObjectProperty` or `owl:bottomObjectProperty`; (ii) `Ax` contains a length-greater-than-one chain inclusion whose target is `OPE` or `INV(OPE)`; or (iii) `Ax` contains `TransitiveObjectProperty(OPE)` or `TransitiveObjectProperty(INV(OPE))`. The source relation `->` is the smallest relation on `AllOPE(Ax)` generated by ordinary subproperty axioms; both directions of equivalent-property axioms; `OPE1 -> INV(OPE2)` and `INV(OPE2) -> OPE1` for inverse-property axioms; `OPE -> INV(OPE)` for symmetric-property axioms; and the closure rule `OPE1 -> OPE2` implies `INV(OPE1) -> INV(OPE2)`. Its reflexive-transitive closure is `->*`. An expression `OPE` is **simple in `Ax`** exactly when every `OPE'` with `OPE' ->* OPE` is noncomposite. Cardinality restrictions and `ObjectHasSelf`, plus `FunctionalObjectProperty`, `InverseFunctionalObjectProperty`, `IrreflexiveObjectProperty`, `AsymmetricObjectProperty`, and `DisjointObjectProperties`, may mention only simple object properties. These are metalinguistic predicates on `Ax`, not OWL entities or constructors; `->*` is the ontology-generated hierarchy used to define simplicity. [Structural Specification, Sections 11.1 and 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Property_Hierarchy_and_Simple_Object_Property_Expressions).
5. **Regular property hierarchy.** A strict partial order `<` on `AllOPE(Ax)` must exist. It must satisfy `OP1 < OP2` if and only if `INV(OP1) < OP2` for all source-quantified object properties `OP1` and `OP2`, and `OPE1 < OPE2` implies that `OPE2 ->* OPE1` does not hold. Every chain inclusion `SubObjectPropertyOf(ObjectPropertyChain(OPE1 ... OPEn) OPE)` with `n >= 2` must then have exactly one of the allowed shapes: target `owl:topObjectProperty`; `n = 2` and `OPE1 = OPE2 = OPE`; every chain member strictly below the target; the target first followed only by lower properties; or only lower properties followed by the target. The witness order `<` is not the hierarchy `->*`: it must not reverse `->*` and is used to certify the legal recursive shapes. [Structural Specification, Section 11.2, “Restriction on the Property Hierarchy”](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#The_Restrictions_on_the_Axiom_Closure).
6. **Anonymous individuals.** None may occur in same/different-individual or negative-property assertions, nor inside `ObjectOneOf` or `ObjectHasValue`. The anonymous-individual graph of `Ax` has the anonymous individuals occurring in `Ax` as vertices and an undirected edge between `_:x` and `_:y` for every `ObjectPropertyAssertion(OPE _:x _:y)` in `Ax`. This graph must be a forest; for each pair of anonymous individuals joined by an edge of this graph, `Ax` may contain at most one object-property assertion between the pair in either direction; and every tree must contain at least one anonymous vertex having at most one object-property assertion to a named individual, in either direction. [Structural Specification, Section 11.2, “Restrictions on the Usage of Anonymous Individuals”](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#The_Restrictions_on_the_Axiom_Closure).

EL and QL disallow anonymous individuals outright, making item 6 vacuous for those profiles. RL retains the Structural Specification's named/anonymous alternative, subject to item 6. [Profiles, Sections 2.2.1, 3.2.1, 4.2.1 and Appendix Sections 6.1--6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Appendix:_Complete_Grammars_for_Profiles).

## 4. OWL 2 EL: independent grammar reconstruction

### 4.1 Entities, datatypes, properties, data ranges, and class expressions

EL admits named individuals only and all predefined classes and properties. Its admitted **predefined** datatype IRIs are `rdf:PlainLiteral`, `rdf:XMLLiteral`, `rdfs:Literal`, `owl:real`, `owl:rational`, `xsd:decimal`, `xsd:integer`, `xsd:nonNegativeInteger`, `xsd:string`, `xsd:normalizedString`, `xsd:token`, `xsd:Name`, `xsd:NCName`, `xsd:NMTOKEN`, `xsd:hexBinary`, `xsd:base64Binary`, `xsd:anyURI`, `xsd:dateTime`, and `xsd:dateTimeStamp`. The Recommendation expressly forbids `xsd:double`, `xsd:float`, `xsd:nonPositiveInteger`, `xsd:positiveInteger`, `xsd:negativeInteger`, `xsd:long`, `xsd:int`, `xsd:short`, `xsd:byte`, `xsd:unsignedLong`, `xsd:unsignedInt`, `xsd:unsignedShort`, `xsd:unsignedByte`, `xsd:language`, and `xsd:boolean`. A nonreserved IRI may still name a declared custom datatype defined exactly once by a legal `DatatypeDefinition`; the whitelist and prohibition concern the predefined datatype vocabulary, while the Structural datatype-definition restrictions in Section 3 govern custom names. [Profiles, Sections 2.2.1 and 2.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Entities), [Structural Specification, Sections 5.2, 9.4, and 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Definitions).

| Grammar position | EL-admissible forms |
|---|---|
| Object property expression | a named object property only; no inverse expression |
| Data property expression | a named data property |
| Data range | an admitted datatype; intersection of two or more EL data ranges; or a one-literal `DataOneOf` |
| Class expression | a class; intersection of two or more EL class expressions; a one-individual `ObjectOneOf`; `ObjectSomeValuesFrom` with an EL class filler; `ObjectHasValue`; `ObjectHasSelf`; `DataSomeValuesFrom` whose printed production contains one or more data properties and an EL data range (the inherited arity condition in Section 3 leaves exactly one property in a standard OWL 2 ontology); or `DataHasValue` |

This is the complete constructor inventory produced by Section 2.2 and Appendix 6.1, not merely the informal feature overview. [Profiles, Sections 2.2.2--2.2.4](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Property_Expressions), [Profiles, Appendix 6.1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_EL_2).

### 4.2 Axiom positions

| Axiom family | EL-admissible forms and position restrictions |
|---|---|
| Class axioms | `SubClassOf`, `EquivalentClasses`, and `DisjointClasses`, with the single EL class-expression grammar in every class-expression position; no `DisjointUnion` |
| Object-property axioms | simple or chained `SubObjectPropertyOf`; `EquivalentObjectProperties`; object-property domain and range with an EL class expression; `ReflexiveObjectProperty`; `TransitiveObjectProperty` |
| Data-property axioms | `SubDataPropertyOf`; `EquivalentDataProperties`; data-property domain with an EL class expression; data-property range with an EL data range; `FunctionalDataProperty`; no `DisjointDataProperties` |
| Datatype and key axioms | `DatatypeDefinition` with an EL data range; `HasKey` with an EL class expression and object/data-property-expression lists (and the inherited requirement that at least one key property be present) |
| Assertions | `SameIndividual`, `DifferentIndividuals`, `ClassAssertion` with an EL class expression, positive and negative object-property assertions, and positive and negative data-property assertions; individuals are named because of the entity grammar |
| Nonlogical forms | declarations and annotation axioms |

[Profiles, Section 2.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms), [Profiles, Appendix 6.1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_EL_2), [Structural Specification, Section 9.5](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Keys).

### 4.3 EL-only range/chain restriction

EL says that *Ax* imposes class-expression range *CE* on object property `OP1` when a (possibly length-zero, when the displayed integer is one) sequence of ordinary, nonchain `SubObjectPropertyOf(OPi OPi+1)` axioms carries `OP1` to `OPk` and `ObjectPropertyRange(OPk CE)` is present. If *Ax* contains `SubObjectPropertyOf(ObjectPropertyChain(OP1 ... OPn) OP)` and imposes range *CE* on `OP`, then *Ax* must also impose that range on the final chain property `OPn`. The condition is vacuous for an ordinary, nonchain `SubObjectPropertyOf` axiom. Reflexive and transitive properties may have ranges if this condition is met. [Profiles, Section 2.2.6](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Global_Restrictions).

Thus the set containing

    SubObjectPropertyOf(ObjectPropertyChain(:r :s) :t)
    ObjectPropertyRange(:t :C)

fails the EL-specific global condition unless the closure also imposes range `:C` on `:s`; adding `ObjectPropertyRange(:s :C)` is one direct way to meet it. This is a derived global-membership example, not an example printed by W3C.

### 4.4 Required legal/illegal shapes

- **Derived profile-legal:** `SubClassOf(:A ObjectSomeValuesFrom(:r :B))`. Both sides are EL class expressions and no forbidden property constructor occurs. [Profiles, Section 2.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions).
- **Derived profile-illegal:** `SubClassOf(:A ObjectAllValuesFrom(:r :B))`. `ObjectAllValuesFrom` is absent from the EL class-expression production and is explicitly listed as unsupported. [Profiles, Sections 2.1 and 2.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview).

## 5. OWL 2 QL: independent grammar reconstruction

### 5.1 Entities, datatypes, properties, and data ranges

QL admits named individuals only and all predefined classes and properties. Its admitted and forbidden **predefined** datatype lists are exactly the EL lists in Section 4.1 above: in particular, `owl:real` and `owl:rational` are admitted, while floating-point datatypes, the finite-width integral datatypes, `xsd:boolean`, and the other explicitly listed finite-value-space datatypes are forbidden. The source says this choice makes every intersection of admitted datatype value spaces either empty or infinite. As in EL, a nonreserved, declared datatype IRI may be defined exactly once by a QL-legal `DatatypeDefinition`; it is not another predefined datatype. [Profiles, Sections 3.2.1 and 3.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Entities_2), [Structural Specification, Sections 5.2, 9.4, and 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Definitions).

An object-property expression is either a named object property or `ObjectInverseOf` applied to a named object property. A data-property expression is named. A data range is an admitted datatype or an intersection of two or more QL data ranges; `DataOneOf`, datatype union, datatype complement, and datatype restriction are absent. [Profiles, Sections 3.2.2 and 3.2.4](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Property_Expressions_2), [Profiles, Appendix 6.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_QL_2).

### 5.2 Position-sensitive class grammar

QL has no single freely substitutable class-expression production. Its two source nonterminals have the following standing and exact expansions:

| Position | QL-admissible forms |
|---|---|
| Subclass position | a class; `ObjectSomeValuesFrom` whose filler is exactly `owl:Thing` and whose property may be named or inverse; or `DataSomeValuesFrom` with a QL data range. Section 3.2.3 inherits the Structural one-or-more-property production, Appendix 6.2 prints exactly one, and the inherited unary-arity condition permits exactly one in a standard OWL 2 ontology. |
| Superclass position | a class; intersection of two or more superclass expressions; complement of a **subclass** expression; `ObjectSomeValuesFrom` with a named-or-inverse property and an **atomic Class** filler; or `DataSomeValuesFrom`, subject to the same main-body/Appendix property-count mismatch and inherited unary-arity result stated in the preceding row |

The subclass/superclass distinction is a source grammar distinction required downstream by class axioms and property-domain/range positions; it is not a new handbook ontology term. [Profiles, Section 3.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_2).

### 5.3 Axiom positions

| Axiom family | QL-admissible forms and position restrictions |
|---|---|
| `SubClassOf` | one subclass expression followed by one superclass expression |
| `EquivalentClasses`, `DisjointClasses` | two or more **subclass** expressions; superclass-only intersections, complements, and qualified existential fillers cannot be inserted merely because they are permitted on the right of `SubClassOf`; no `DisjointUnion` |
| Object-property axioms | ordinary (nonchain) `SubObjectPropertyOf`; equivalence; disjointness; inverse-property axioms; domain and range with a superclass expression; reflexive, symmetric, and asymmetric property axioms. Functional, inverse-functional, and transitive property axioms are absent. The irreflexive mismatch is treated separately in Section 11. |
| Data-property axioms | subproperty, equivalence, disjointness, domain with a superclass expression, and range with a QL data range; no functional-data-property axiom |
| Assertions | `DifferentIndividuals`; `ClassAssertion` with an **atomic Class** only; positive object-property and data-property assertions. `SameIndividual` and both negative-property assertions are absent. |
| Other axioms | declarations, `DatatypeDefinition` with a QL data range, and annotation axioms; no `HasKey` |

[Profiles, Section 3.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_2), [Profiles, Appendix 6.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_QL_2).

QL inherits Structural Specification Section 11 with no extra profile-specific global condition. Its simple-object-property condition remains substantive: disjointness and asymmetry require simple object properties. The separate regular property-hierarchy condition remains inherited but is automatically witnessed by the empty strict order because QL forbids every property-chain axiom. [Profiles, Sections 3.1--3.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Profile_Specification_2), [Structural Specification, Section 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#The_Restrictions_on_the_Axiom_Closure).

### 5.4 Required legal/illegal shapes

- **Derived profile-legal:** `SubClassOf(ObjectSomeValuesFrom(:r owl:Thing) ObjectSomeValuesFrom(ObjectInverseOf(:s) :B))`. The left is the special unqualified subclass existential; the right is a superclass existential with an atomic class filler; inverse object properties are admitted. [Profiles, Section 3.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_2).
- **Derived profile-illegal:** `SubClassOf(:A ObjectSomeValuesFrom(:r ObjectIntersectionOf(:B :C)))`. A QL superclass existential requires an atomic `Class` filler, not an intersection. [Profiles, Section 3.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_2).

The Recommendation separately explains that QL omits `SameIndividual` because adding equality assertions would destroy first-order rewritability at the advertised data complexity. It describes equality-closure preprocessing in LOGSPACE as a way to handle an otherwise-QL ontology, but that preprocessing does **not** make `SameIndividual` part of the QL grammar. [Profiles, Section 3.1, final paragraph](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview_2).

## 6. OWL 2 RL: independent grammar reconstruction

### 6.1 Entities, datatypes, and properties

RL uses the Structural Specification's individual grammar and therefore admits named and anonymous individuals, subject to the inherited anonymous-individual restrictions. It admits `owl:Nothing` and `owl:Thing`, although the latter is position-restricted below. It expressly excludes the four predefined top/bottom properties `owl:topObjectProperty`, `owl:bottomObjectProperty`, `owl:topDataProperty`, and `owl:bottomDataProperty`. [Profiles, Section 4.2.1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Entities_3).

The admitted **predefined** RL datatypes are `rdf:PlainLiteral`, `rdf:XMLLiteral`, `rdfs:Literal`, `xsd:decimal`, `xsd:integer`, `xsd:nonNegativeInteger`, `xsd:nonPositiveInteger`, `xsd:positiveInteger`, `xsd:negativeInteger`, `xsd:long`, `xsd:int`, `xsd:short`, `xsd:byte`, `xsd:unsignedLong`, `xsd:unsignedInt`, `xsd:unsignedShort`, `xsd:unsignedByte`, `xsd:float`, `xsd:double`, `xsd:string`, `xsd:normalizedString`, `xsd:token`, `xsd:language`, `xsd:Name`, `xsd:NCName`, `xsd:NMTOKEN`, `xsd:boolean`, `xsd:hexBinary`, `xsd:base64Binary`, `xsd:anyURI`, `xsd:dateTime`, and `xsd:dateTimeStamp`. `owl:real` and `owl:rational` are expressly forbidden. A nonreserved, declared datatype IRI may be defined exactly once by an RL-legal `DatatypeDefinition`, subject to the Structural restrictions in Section 3. [Profiles, Sections 4.2.1 and 4.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Entities_3), [Structural Specification, Sections 5.2, 9.4, and 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Datatype_Definitions).

Object-property expressions are named properties or inverses of named properties; data-property expressions are named. A data range is an admitted datatype or an intersection of at least two RL data ranges. [Profiles, Sections 4.2.2 and 4.2.4](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Property_Expressions_3), [Profiles, Appendix 6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).

### 6.2 Three position-sensitive class grammars

| Position | RL-admissible forms |
|---|---|
| Subclass expression | an atomic class other than `owl:Thing`; recursive intersection or union of two or more subclass expressions; `ObjectOneOf`; `ObjectSomeValuesFrom` with a subclass-expression filler or the special filler `owl:Thing`; `ObjectHasValue`; `DataSomeValuesFrom`; or `DataHasValue` |
| Superclass expression | an atomic class other than `owl:Thing`; recursive intersection of two or more superclass expressions; complement of a subclass expression; `ObjectAllValuesFrom` with a superclass-expression filler; `ObjectHasValue`; object maximum cardinality exactly 0 or 1, optionally qualified by a subclass expression (with a separately printed `owl:Thing` alternative); `DataAllValuesFrom`; `DataHasValue`; or data maximum cardinality exactly 0 or 1, optionally qualified by an RL data range |
| Equivalence expression | an atomic class other than `owl:Thing`; recursive intersection of two or more equivalence expressions; `ObjectHasValue`; or `DataHasValue` |

`ObjectOneOf` here is the Structural Specification form with one or more individuals, but inherited Section 11 prevents anonymous individuals inside it. The printed `DataSomeValuesFrom` and `DataAllValuesFrom` productions retain the Structural Specification's one-or-more data-property argument list followed by a data range; the inherited arity condition in Section 3 means that a standard OWL 2 RL ontology can use exactly one such property. [Profiles, Section 4.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_3), [Profiles, Appendix 6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2), [Structural Specification, Sections 8.4.1--8.4.2 and 11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Data_Property_Restrictions).

### 6.3 Axiom positions

| Axiom family | RL-admissible forms and position restrictions |
|---|---|
| `SubClassOf` | subclass expression on the left; superclass expression on the right |
| `EquivalentClasses` | two or more equivalence expressions only |
| `DisjointClasses` | two or more subclass expressions; no `DisjointUnion` |
| Object-property axioms | every Structural Specification object-property-axiom form except `ReflexiveObjectProperty`: simple or chained subproperty, equivalence, disjointness, inverse properties, domain/range with a superclass expression, functional, inverse-functional, irreflexive, symmetric, asymmetric, and transitive property axioms |
| Data-property axioms | all Structural Specification forms: subproperty, equivalence, disjointness, domain with a superclass expression, range with an RL data range, and functionality |
| Assertions | every Structural Specification assertion form; the positive `ClassAssertion` position is narrowed to a superclass expression. Thus same/different-individual, positive/negative object-property, and positive/negative data-property assertions remain, subject to inherited anonymous-individual restrictions. |
| Keys | `HasKey` with a subclass expression and lists of object/data-property expressions; the inherited at-least-one-key-property requirement remains |
| Other axioms | declarations, `DatatypeDefinition` with an RL data range, and annotation axioms |

[Profiles, Section 4.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_3), [Profiles, Appendix 6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).

RL inherits Structural Specification Section 11 without an additional RL-only global condition. This is substantive: cardinality-0/1 expressions and functional, inverse-functional, irreflexive, asymmetric, and disjoint-property axioms may use only simple object properties, and chains must be regular. [Profiles, Section 4.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Profile_Specification_3), [Structural Specification, Sections 11.1--11.2](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Property_Hierarchy_and_Simple_Object_Property_Expressions).

### 6.4 Required legal/illegal shapes

- **Derived profile-legal:** `SubClassOf(ObjectUnionOf(:A :B) ObjectAllValuesFrom(:r ObjectComplementOf(:C)))`. The left is a subclass union; the right is a universal restriction whose filler is a superclass complement of the subclass expression `:C`. [Profiles, Section 4.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_3).
- **Derived profile-illegal:** `SubClassOf(:A ObjectSomeValuesFrom(:r :B))`. RL permits an object existential in subclass position but does not include it in the superclass production; an existential conclusion would require generation of an unnamed witness, which the profile's syntactic discipline is designed to avoid. [Profiles, Sections 4.1 and 4.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview_3).

### 6.5 RL/RDF rules and the exact completeness boundary

The RL syntax and the RL/RDF rules are different artifacts. Section 4.2 defines the syntactic profile under Direct Semantics. Section 4.3 gives a **partial** first-order axiomatization of OWL 2 RDF-Based Semantics over a ternary triple predicate `T`, organized as list expansion (Table 3), equality (Table 4), property axioms (Table 5), classes (Table 6), class axioms (Table 7), datatypes (Table 8), and schema vocabulary (Table 9). The rule set deliberately omits RDF/RDFS axiomatic triples and some RDFS entailment rules; a conforming implementation may add them. [Profiles, Sections 4.2--4.3 and Tables 3--9](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules).

For arbitrary RDF graphs, the Recommendation promises soundness of derived entailments but explicitly withholds completeness, especially when built-in vocabulary is used unusually. Theorem PR1 supplies an if-and-only-if only under all of these hypotheses: both inputs are RL ontologies; neither uses an IRI for more than one entity type; the premise ontology has no annotation-subproperty/domain/range axioms; and every conclusion axiom is an atomic named-individual class assertion, named object-property assertion, named data-property assertion, or `SameIndividual` assertion. Under those conditions, Direct-Semantics entailment of the conclusion ontology is equivalent to ordinary first-order entailment from the RDF translation of the premise plus the RL/RDF rules. [Profiles, Section 4 introduction and Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1).

The printed proof is explicitly a proof sketch. It assumes depth-at-most-one normalization, translates the premise to DLP rules, transforms derivation trees between DLP and Tables 3--8, and uses the no-punning hypothesis to keep `owl:sameAs` from identifying a class/property IRI with an individual. It is not a proof that Tables 3--9 are complete for arbitrary RDF graphs, arbitrary conclusions, annotation entailment, or every RDF-Based-Semantics inference problem. [Profiles, Theorem PR1 proof sketch](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1).

## 7. Exact non-subset claims and derived witnesses

The source statement is “none of the profiles is a subset of another”; it does not say that the profiles are disjoint. The following profile-legal one-axiom witnesses (with declarations and inherited restrictions understood as in Section 1) independently establish every directed failure of inclusion. [Profiles, Section 1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Introduction).

| Direction that fails | Derived witness in the first profile | Why excluded from the second profile |
|---|---|---|
| EL is not a subset of QL | `TransitiveObjectProperty(:r)` | QL omits transitivity |
| QL is not a subset of EL | `InverseObjectProperties(:r :s)` | EL object-property expressions are named only and its object-property-axiom list omits inverse-property axioms |
| EL is not a subset of RL | `ReflexiveObjectProperty(:r)` | RL explicitly excludes reflexive-property axioms |
| RL is not a subset of EL | `FunctionalObjectProperty(:r)` with `:r` simple | EL excludes functional object properties |
| QL is not a subset of RL | `ReflexiveObjectProperty(:r)` | admitted by the QL grammar, excluded by RL |
| RL is not a subset of QL | `TransitiveObjectProperty(:r)` | admitted by RL, excluded by QL |

[Profiles, EL axioms](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms), [Profiles, QL axioms](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_2), [Profiles, RL axioms](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_3).

Each profile is a structural restriction of OWL 2, but that fact must not be collapsed into “OWL 2 Full.” The Direct Semantics is defined on structural OWL 2 axioms and is the semantics used for the profile-ontology tasks and PR1's left-hand entailment. RDF-Based Semantics also assigns meaning to RDF graphs outside the OWL 2 DL/profile structural restrictions. Table 10 consequently has distinct “OWL 2 Direct Semantics” and “OWL 2 RDF-Based Semantics” rows; neither row is a fourth syntactic profile. [Profiles, Abstract, Sections 1, 4, and 5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Direct Semantics, Section 1](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Introduction).

## 8. Exact lineage distinctions: EL++, DL-Lite, SHOIQ/SROIQ, and OWL 2

### 8.1 OWL 2 EL is not a renaming of the 2005 EL++ paper

The Recommendation says OWL 2 EL is designed as a subset of OWL 2 and cites the 2005 EL++ paper and its 2008 update. It does not assert syntactic identity. [Profiles, Section 2 opening](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_EL).

The 2005 paper's EL++ concept language has top, bottom, singleton nominals, conjunction, existential role restrictions, and predicates from selected concrete domains. Its constraint box contains general concept inclusions and role inclusions; role inclusions express ordinary role hierarchies, transitivity, and right-identity rules. Its Theorem 4 proves polynomial-time subsumption for p-admissible concrete domains. [Baader--Brandt--Lutz 2005, PDF pp. 1--4, Table 1, Sections 2--3, Theorem 4](https://lat.inf.tu-dresden.de/research/papers/2005/BaaderBrandtLutz-IJCAI-05.pdf).

The 2008 update extends that EL++ presentation with reflexive roles, domain/range restrictions, assertions, and the exact final-chain range condition later used by OWL 2 EL. It proves that dropping the condition makes subsumption undecidable (Theorem 1), that even acyclic right identities with range restrictions are PSPACE-hard (Theorem 2), and that symmetric roles make the relevant extension EXPTIME-complete (Theorem 4). [Baader--Brandt--Lutz 2008, PDF pp. 1--5, Sections 1--4; pp. 7--9, Theorems 1--4](http://www.webont.org/owled/2008dc/papers/owled2008dc_paper_3.pdf).

OWL 2 EL instead uses the OWL entity/datatype system, functional-style axiom families, data-property restrictions, self and value restrictions, assertions, keys, annotations, the OWL 2 DL global restrictions, and its enumerated datatype whitelist. Its concrete-data treatment is therefore not the 2005 paper's arbitrary p-admissible concrete-domain parameter, and its legal ontology grammar is broader in some OWL axiom dimensions while excluding constructors that the paper shows to be intractable. “Based on EL++” is the supported historical relationship; “identical to EL++” is not. [Profiles, Sections 2.1--2.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview), [Baader--Brandt--Lutz 2005, PDF pp. 2--4](https://lat.inf.tu-dresden.de/research/papers/2005/BaaderBrandtLutz-IJCAI-05.pdf).

### 8.2 OWL 2 QL is based on DL-Lite_R, not identical to “DL-Lite” as a family

The Recommendation says the DL-Lite family has several variants and names DL-Lite_R as QL's logical underpinning. It says DL-Lite_R does not require the unique-name assumption because that assumption does not change its semantic consequences. More expressive DL-Lite_A adds functional properties and can add keys, but retaining LOGSPACE query answering then requires the unique-name assumption and extra global interaction restrictions; QL chooses the DL-Lite_R basis to avoid that practical requirement. [Profiles, Section 3 opening](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_QL).

The 2007 primary paper defines a family: DL-Lite_core; DL-Lite_R, which adds role inclusions and role disjointness; and DL-Lite_F, which instead adds role functionality. Its formal semantics on constants explicitly enforces the unique-name assumption. It proves, for DL-Lite_R and DL-Lite_F, LOGSPACE data complexity and PTIME combined complexity for knowledge-base satisfiability (Theorem 26); PTIME TBox reasoning and LOGSPACE-data/PTIME-combined instance checking (Theorem 27); first-order reducibility of union-of-conjunctive-query answering for DL-Lite_R (Theorem 41); and NP-complete combined query complexity (Theorem 44). [Calvanese et al. 2007, journal pp. 388--391 / PDF pp. 4--7, Sections 2.1--2.2; pp. 410--411 / PDF pp. 26--27, Theorems 26--27; pp. 421--422 / PDF pp. 37--38, Theorems 41--44](https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf).

Therefore the W3C profile does not inherit every convention of the paper: it does not adopt the paper's unique-name assumption, excludes functionality and keys, and expresses its fragment through OWL's position-sensitive grammar and global restrictions. Conversely, its grammar names OWL axiom forms, such as reflexivity and symmetry, that are not the 2007 paper's three-family syntax. Table 10's “in AC0” entries are W3C's 2012 claims; the cited 2007 paper itself states LOGSPACE and first-order reducibility and cannot by itself be cited as the complete proof of every QL table cell. [Profiles, Sections 3.1--3.2 and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Calvanese et al. 2007, Abstract and Theorems 26--27, 41--44](https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf).

### 8.3 SHOIQ, SROIQ, OWL 1 DL, and OWL 2 Direct Semantics

The SROIQ paper starts from SHOIN, which it identifies as the description logic underlying OWL-DL, and from SHOIQ, which it defines there as SHOIN plus qualified number restrictions. It extends SHOIQ with complex role inclusions, disjoint roles, reflexive/irreflexive/asymmetric roles, a universal role, local self restrictions, negative role assertions, and qualified number restrictions, subject to regularity and simple-role restrictions. Its Theorem 17 establishes decidability of its tableau procedure, but its Outlook explicitly leaves the exact computational complexity of SROIQ for future work. [Horrocks--Kutz--Sattler 2006, PDF pp. 1--4, Abstract, Introduction, Definitions 2--5; p. 11, Theorem 17 and Outlook](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf).

The dated Direct Semantics says its semantics is strongly related to and **extends** SROIQ. It gives the reason: the cited SROIQ definition does not provide datatypes or punning, so OWL 2 semantics is defined directly on Structural Specification constructs; for constructs present in SROIQ, the semantics corresponds. Thus “SROIQ is the logical basis” does not license replacing the OWL 2 structural grammar or datatype/punning semantics with the 2006 paper. [Direct Semantics, Abstract and Section 1](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Introduction).

Table 10 separately reports OWL 1 DL and OWL 2 Direct Semantics. Its OWL 1 DL basic-task bounds are NEXPTIME-complete taxonomically and combined; its OWL 2 Direct-Semantics bounds are N2EXPTIME-complete, subject to the printed NFA condition. The 2006 SROIQ paper cannot be the proof source for that latter exact bound because it expressly left SROIQ's exact complexity open. [Profiles, Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Horrocks--Kutz--Sattler 2006, PDF p. 11, Outlook](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf).

### 8.4 Full structural OWL 2 versus the profiles

Full structural OWL 2 offers constructor and axiom productions excluded or position-restricted by every profile; an OWL 2 DL ontology additionally must satisfy typing and Section 11 global restrictions. EL, QL, and RL are therefore proper syntactic fragments of that structural language, but their pairwise relation is overlap without inclusion, not a nested ladder. Direct Semantics applies to the structural axioms and profiles; RDF-Based Semantics is a separate semantic account for RDF graphs. “Full OWL 2,” “OWL 2 DL,” “OWL 2 under Direct Semantics,” and arbitrary graphs under “OWL 2 RDF-Based Semantics” are not interchangeable labels. [Profiles, Abstract, Section 1, and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Introduction), [Structural Specification, Sections 5.8.1 and 11](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Global_Restrictions_on_Axioms_in_OWL_2_DL), [Direct Semantics, Section 1](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Introduction).

## 9. Reasoning tasks and four complexity axes (definitions before results)

### 9.1 Reasoning tasks

Let an ontology be interpreted under the Direct Semantics with its chosen datatype map and vocabulary. The five Table 10 tasks have the following source-defined standing:

- **Ontology consistency:** existence of a model of the ontology.
- **Class-expression satisfiability:** existence of a model of the ontology in which the class expression has a nonempty extension.
- **Class-expression subsumption:** inclusion of the first class expression's extension in the second's in every model of the ontology.
- **Instance checking:** membership of the named individual's denotation in the class expression's extension in every model of the ontology.
- **Boolean conjunctive-query answering:** a Boolean conjunctive query is a closed existentially quantified conjunction of atoms of the forms `C(s)`, `OP(s,t)`, and `DP(s,u)`, with the source's individual and literal variable discipline; it is an answer exactly when it is true in every model according to first-order semantics.

[Direct Semantics, Section 2.5](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Inference_Problems).

The Direct Semantics additionally requires simple object properties in cardinality and self restrictions occurring in checked expressions when decidability is claimed. That is a checked-input condition, not another Table 10 task. [Direct Semantics, Section 2.5, final restriction](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Inference_Problems).

### 9.2 Four input-size axes

The Recommendation defines all four axes before Table 10:

1. **Taxonomic complexity:** vary the total size of ontology axioms other than assertions.
2. **Data complexity:** vary the total size of ontology assertions.
3. **Query complexity:** vary the total size of the conjunctive query; this axis is defined only for conjunctive-query answering.
4. **Combined complexity:** vary the total size of ontology axioms and assertions, plus the conjunctive query for query answering, plus the checked expression or expressions for class satisfiability, subsumption, or instance checking.

[Profiles, Section 5, list immediately before Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).

### 9.3 Entry legend and exact qualification

- **Decidability open** means the source reports that decidability itself was unknown.
- **Decidable, but complexity open** means the source reports decidability but not the exact class; a parenthetical class such as “NP-Hard” is only a lower bound.
- **X-complete** means both membership in X and X-hardness. By contrast, bare **in X** records membership only and must not be upgraded to completeness.
- **Not Applicable** occurs when the input axis is not defined for that task grouping.
- Every result is worst-case. The table does not assert that every implementation or typical input exhibits the bound.
- The NFA parenthetical is a conditional result: it applies only “if the property hierarchy can be translated into a polynomially-sized nondeterministic finite automaton.” Section 5 gives no operational test, automaton construction, size convention, or proof for this condition.
- “Atomic class expressions” is the source's unelaborated qualifier on the RL combined-complexity cell. Section 5 does not define it. Elsewhere, the QL axiom section says class assertions contain only atomic classes and immediately narrows their grammar position to the `Class` nonterminal; that is evidence for reading “atomic” as an unconstructed `Class`, but the Recommendation does not explicitly cross-reference that passage from Table 10. This note preserves the printed qualifier and does not silently broaden it.

[Profiles, Section 5, entry legend and paragraph before Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Profiles, Section 3.2.5 `ClassAssertion`](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_2).

The source sketches N2EXPTIME, NEXPTIME, PSPACE, NP, PTIME, LOGSPACE/NLOGSPACE, and AC0 at this location. It does **not** separately define EXPTIME or co-NP even though Table 10 uses both. This note therefore preserves those labels without pretending the Recommendation supplied the missing definitions. [Profiles, Section 5, complexity-class list and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).

## 10. Complete Table 10 reconstruction

This is an independent row-by-row reconstruction of the dated Recommendation's Table 10. Task groupings, all four axes, membership-only “in,” completeness, conditions, open entries, lower bounds, and nonapplicability are preserved. Capitalization is normalized only in prose around the table; the mathematical status of no cell is strengthened. [Profiles, Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).

| Language / semantics | Reasoning task(s) | Taxonomic | Data | Query | Combined |
|---|---|---|---|---|---|
| OWL 2, RDF-Based Semantics | Ontology consistency; class-expression satisfiability; class-expression subsumption; instance checking; conjunctive-query answering | Undecidable | Undecidable | Undecidable | Undecidable |
| OWL 2, Direct Semantics | Ontology consistency; class-expression satisfiability; class-expression subsumption; instance checking | N2EXPTIME-complete; NEXPTIME-complete if the property hierarchy has a polynomial-size NFA translation | Decidable, exact complexity open; NP-hard | Not applicable | N2EXPTIME-complete; NEXPTIME-complete under the same polynomial-size-NFA condition |
| OWL 2, Direct Semantics | Conjunctive-query answering | Decidability open | Decidability open | Decidability open | Decidability open |
| OWL 2 EL | Ontology consistency; class-expression satisfiability; class-expression subsumption; instance checking | PTIME-complete | PTIME-complete | Not applicable | PTIME-complete |
| OWL 2 EL | Conjunctive-query answering | **in EXPTIME**; PTIME-complete if the property hierarchy has a polynomial-size NFA translation | PTIME-complete | NP-complete | **in EXPTIME**; PSPACE-complete under the same polynomial-size-NFA condition |
| OWL 2 QL | Ontology consistency; class-expression satisfiability; class-expression subsumption; instance checking | NLOGSPACE-complete | **in AC0** | Not applicable | NLOGSPACE-complete |
| OWL 2 QL | Conjunctive-query answering | NLOGSPACE-complete | **in AC0** | NP-complete | NP-complete |
| OWL 2 RL | Ontology consistency | PTIME-complete | PTIME-complete | Not applicable | PTIME-complete |
| OWL 2 RL | Class-expression satisfiability; class-expression subsumption; instance checking | PTIME-complete | PTIME-complete | Not applicable | co-NP-complete; PTIME-complete when the checked class expressions are atomic |
| OWL 2 RL | Conjunctive-query answering | PTIME-complete | PTIME-complete | NP-complete | NP-complete |
| OWL 1 DL | Ontology consistency; class-expression satisfiability; class-expression subsumption; instance checking | NEXPTIME-complete | Decidable, exact complexity open; NP-hard | Not applicable | NEXPTIME-complete |
| OWL 1 DL | Conjunctive-query answering | Decidability open | Decidability open | Decidability open | Decidability open |

Two fidelity cautions are essential. First, “in EXPTIME” and “in AC0” are membership upper bounds, not completeness claims. Second, the atomic-class-expression parenthetical narrows only the RL combined-complexity cell for class satisfiability, subsumption, and instance checking; it does not alter the RL consistency or query-answering rows. [Profiles, Section 5 legend and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).

## 11. Printed defects and their exact adjudication

### 11.1 QL conflicts

The QL feature overview says that QL supports irreflexive object properties and names `IrreflexiveObjectProperty` in its supported list. The profile grammar in Section 3.2.5, however, lists reflexive, symmetric, and asymmetric object-property axioms but omits `IrreflexiveObjectProperty`; the complete QL grammar in Appendix 6.2 repeats that omission. Because the Recommendation says profile restrictions are specified by modifying grammar productions, the dated body does not supply a single consistent answer: the prose includes the construct while both grammar locations exclude it. [Profiles, Section 3.1 supported-feature list](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview_2), [Profiles, Section 3.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_2), [Profiles, Appendix 6.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_QL_2).

The same feature overview first admits subclass-position `ObjectSomeValuesFrom` with filler `owl:Thing` and subclass-position `DataSomeValuesFrom` in Table 1, then lists “existential quantification to a class expression or a data range (`ObjectSomeValuesFrom` and `DataSomeValuesFrom`) in the subclass position” as unsupported. The object part can be read as excluding arbitrary non-`owl:Thing` fillers, but the printed data-range part contradicts Table 1 and the `subClassExpression` production unless an unstated qualification is added. Section 5.2 of this note follows the explicit productions and discloses the overview conflict rather than using the unsupported-feature bullet as a ban. [Profiles, Section 3.1, Table 1 and unsupported-feature list](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview_2), [Profiles, Section 3.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_2).

There is also a production-text mismatch in the number of data properties. Section 3.2.3 references `DataSomeValuesFrom` without replacing the Structural production, whose surface syntax permits one or more data-property expressions; Appendix 6.2 instead prints exactly one. The inherited arity conditions eliminate any difference in standard profile membership because all QL data ranges are unary and the number of properties must equal the range arity. The two printed productions are nonetheless different, so Section 5.2 reports both. [Profiles, Section 1 production method and Section 3.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_2), [Profiles, Appendix 6.2](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_QL_2), [Structural Specification, Sections 7 and 8.4.1](https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/#Existential_Quantification_2).

The current W3C OWL 2 errata page says the Second Edition addressed all reported First Edition errata and explains that listed later proposals do not change a Recommendation without Working Group and Advisory Committee approval. Its current table contains no Profiles entry resolving any of these QL conflicts. Accordingly, this note does not silently insert `IrreflexiveObjectProperty` into QL, does not call the omissions or conflicts official errata, and does not use irreflexivity as a legality example or non-subset witness. The exact source-verified result is that the dated Recommendation contains unresolved printed inconsistencies at these locations. [W3C OWL 2 errata, introductory status and current table](https://www.w3.org/2001/sw/wiki/OWL_Errata).

### 11.2 RL grammar defects

Four defects are literal in the dated RL presentation:

1. In both Section 4.2.5 and Appendix 6.3, the `ObjectPropertyAxiom` alternatives print `SymmetricObjectProperty | AsymmetricObjectProperty` and then `TransitiveObjectProperty` on the next line without the required separating vertical bar. Each of the latter productions is nevertheless separately defined, and the feature overview says both asymmetry and transitivity are supported. [Profiles, Section 4.1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Feature_Overview_3), [Profiles, Section 4.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Axioms_3), [Profiles, Appendix 6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).
2. Appendix 6.3 makes `superClassExpression` refer to an undefined `superComplementOf`, while the immediately following production defines `superObjectComplementOf`. Section 4.2.3 consistently uses and defines `superObjectComplementOf`. [Profiles, Section 4.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_3), [Profiles, Appendix 6.3, `superClassExpression`](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).
3. Appendix 6.3 ends the sole `superDataMaxCardinality` alternative with a vertical bar, although no following alternative exists. Section 4.2.3 prints the same production without that trailing bar. [Profiles, Section 4.2.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_3), [Profiles, Appendix 6.3, `superDataMaxCardinality`](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).
4. Section 4.2.3's introductory prose calls the third class-position production `equivClassExpressions` (plural), while the displayed production, the Section 4.2.5 axiom productions, and Appendix 6.3 use `equivClassExpression` (singular). The reconstruction uses the displayed singular nonterminal and records the prose mismatch here. [Profiles, Sections 4.2.3 and 4.2.5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Class_Expressions_3), [Profiles, Appendix 6.3](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#OWL_2_RL_2).

The reconstructions in Sections 6.2--6.3 use the unambiguous Section 4.2 productions together with the separately defined alternatives and disclose every departure from the malformed Appendix typography here. That is a reader-verifiable local reconstruction, not a claim that W3C issued a correction. The current errata page has no Profiles entry for these defects. [W3C OWL 2 errata](https://www.w3.org/2001/sw/wiki/OWL_Errata).

### 11.3 Complexity-table presentation gaps

Section 5 introduces N2EXPTIME, NEXPTIME, PSPACE, NP, PTIME, LOGSPACE, NLOGSPACE, and AC0 before Table 10, but the table additionally uses EXPTIME and co-NP without defining them there. It also states the polynomial-size-NFA condition without defining a translation algorithm, representation-size convention, or test for when the condition holds. These are limitations of the presentation, not evidence that the associated table cells are false. This note therefore preserves the labels and condition literally at the level of logical force and does not add a later convention or inferred completeness claim. [Profiles, Section 5 and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).

## 12. Proof ownership and referral boundaries

Table 10 is a summary in the W3C Recommendation, not a proved theorem inside it. Section 5 defines the axes, gives a short complexity-class legend, and prints the table, but supplies no row-specific citations, reductions, algorithms, or proofs. Its normative reference at that location is the Direct Semantics for the inference-task definitions, not a proof source for the complexity classifications. The only other citation in the section is Papadimitriou's textbook for a general introduction to computational complexity, not for any particular table row. No primary paper is explicitly cited by Table 10 and no Table 10 proof is delegated to a named paper. [Profiles, Section 5 and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Profiles, normative references](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Normative_References), [Profiles, nonnormative reference `Papadimitriou`](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#ref-papa).

The Recommendation's profile introductions cite the EL++, DL-Lite, and SROIQ papers as nonnormative background. Those papers can establish only their own formal systems and theorem scopes:

- the 2005 EL++ paper proves polynomial-time subsumption for its stated p-admissible concrete-domain setting, and the 2008 paper proves the named range-chain and extension results summarized in Section 8.1;
- the 2007 DL-Lite paper proves the results stated for its DL-Lite variants and its own unique-name convention, not every W3C QL grammar or Table 10 cell;
- the 2006 SROIQ paper proves decidability of its tableau and expressly leaves exact complexity open, so it cannot own Table 10's later N2EXPTIME classification for OWL 2 Direct Semantics.

[Profiles, nonnormative references](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Non-normative_References), [Baader--Brandt--Lutz 2005, Theorem 4](https://lat.inf.tu-dresden.de/research/papers/2005/BaaderBrandtLutz-IJCAI-05.pdf), [Baader--Brandt--Lutz 2008, Theorems 1--4](http://www.webont.org/owled/2008dc/papers/owled2008dc_paper_3.pdf), [Calvanese et al. 2007, Theorems 26--27 and 41--44](https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf), [Horrocks--Kutz--Sattler 2006, Theorem 17 and Outlook](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf).

The one proof attached to a profile-specific reasoning result in this Recommendation is the proof sketch for Theorem PR1. Its ownership is narrow: it relates Direct-Semantics entailment for the specified RL premise/conclusion class to first-order entailment from the RDF translation plus the RL/RDF rules, under every hypothesis listed in Section 6.5. It does not prove Table 10 as a whole. [Profiles, Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1).

The RL introduction cites DLP and pD* as design inspirations, while the PR1 proof sketch specifically invokes a DLP translation and matching derivation trees. Those citations do not make either system identical to OWL 2 RL and do not transfer a completeness theorem beyond PR1's explicit boundary. Because Table 10 itself does not delegate proof to them, this task did not treat those papers as missing proof bodies. [Profiles, Section 4 opening, Section 4.3, Theorem PR1, and nonnormative references](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Theorem-PR1).

## 13. Qualifications and claims the source does not support

The following boundaries are source-verified or immediate consequences of the cited source organization:

1. The 2012 Recommendation is the controlling historical presentation here. This note does not claim that Table 10 reflects post-2012 complexity results or implementation practice. [Profiles, dated header and status](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#w3c_status).
2. A profile-membership check is syntactic and global; it is not a proof of ontology consistency, satisfiability, entailment, useful modeling, or fast behavior on a particular input. [Profiles, Sections 1--5](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).
3. “None is a subset of another” does not mean pairwise disjointness. The profiles overlap, and the Recommendation does not present them as a linear hierarchy. [Profiles, Section 1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Introduction).
4. The profile grammars do not define arbitrary RDF graphs as profile ontologies. RL/RDF rules can be applied to arbitrary RDF graphs, but soundness is the general promise and PR1 is the stated completeness bridge only for its restricted ontology/conclusion class. [Profiles, Sections 4.2--4.3 and Theorem PR1](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Reasoning_in_OWL_2_RL_and_RDF_Graphs_using_Rules).
5. The `in EXPTIME` and `in AC0` Table 10 cells are not completeness results; the NP-hard annotations are not exact classifications; “decidability open” is not a decidability theorem; and “Not Applicable” is not a zero-complexity claim. [Profiles, Section 5 legend and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties).
6. The Recommendation does not prove Table 10 cell by cell, define an operational NFA condition, repair the printed grammar defects in Section 11, or make EL, QL, or RL identical to the cited description-logical systems. [Profiles, Sections 2--6](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/), [W3C OWL 2 errata](https://www.w3.org/2001/sw/wiki/OWL_Errata).
7. The Direct-Semantics definitions used in Section 9 do not by themselves define the RDF-Based-Semantics tasks. Table 10 reports the RDF-Based row separately and makes every listed axis undecidable, but this note did not read or reconstruct the separate RDF-Based Semantics Recommendation. [Profiles, Section 5 and Table 10](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/#Computational_Properties), [Direct Semantics, Section 1](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Introduction).

For handbook integration, the safe source-faithful order is: identify the dated Recommendation and semantic regime; define the relevant profile grammar and inherited global restrictions; define the reasoning task and input-size axis; then state exactly the corresponding Table 10 cell with every condition and status marker. The QL conflicts and malformed RL productions must be disclosed if the affected inventory is presented. This order introduces no new logical object; it simply follows the dependencies in Sections 1--5 of the Recommendation.

## 14. Primary bodies and exact locator policy

- Boris Motik, Bernardo Cuenca Grau, Ian Horrocks, Zhe Wu, Achille Fokoue, and Carsten Lutz (editors), *OWL 2 Web Ontology Language: Profiles (Second Edition)*, W3C Recommendation, 11 December 2012. Dated body: <https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/>. Use named sections, numbered tables, Appendix 6.x, and Theorem PR1 as locators; the HTML has no source pagination.
- Boris Motik, Peter F. Patel-Schneider, and Bijan Parsia (editors), *OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)*, W3C Recommendation, 11 December 2012. Dated body: <https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/>. Relevant locators here: the opening ontology conditions and Sections 3.1, 3.4, 5.1--5.8.1, 7, 8.4.1--8.4.2, 9.3.5, 9.4--9.5, and 11.
- Boris Motik, Peter F. Patel-Schneider, and Bernardo Cuenca Grau (editors), *OWL 2 Web Ontology Language: Direct Semantics (Second Edition)*, W3C Recommendation, 11 December 2012. Dated body: <https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/>. Relevant locators here: Sections 1, 2.4, and 2.5.
- Franz Baader, Sebastian Brandt, and Carsten Lutz, “Pushing the EL Envelope,” *Proceedings of IJCAI 2005*, pp. 364--369. Institutional copy: <https://lat.inf.tu-dresden.de/research/papers/2005/BaaderBrandtLutz-IJCAI-05.pdf>.
- Franz Baader, Sebastian Brandt, and Carsten Lutz, “Pushing the EL Envelope Further,” *Proceedings of the OWLED 2008 DC Workshop on OWL: Experiences and Directions*, 10-page conference-site PDF. W3C-linked copy: <http://www.webont.org/owled/2008dc/papers/owled2008dc_paper_3.pdf>.
- Diego Calvanese, Giuseppe De Giacomo, Domenico Lembo, Maurizio Lenzerini, and Riccardo Rosati, “Tractable Reasoning and Efficient Query Answering in Description Logics: The DL-Lite Family,” *Journal of Automated Reasoning* 39(3) (2007), 385--429, DOI 10.1007/s10817-007-9078-x. Institutional copy: <https://www.inf.unibz.it/~calvanese/papers/calv-etal-JAR-2007.pdf>.
- Ian Horrocks, Oliver Kutz, and Ulrike Sattler, “The Even More Irresistible SROIQ,” *Proceedings of KR 2006*, pp. 57--67. Author copy: <https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2006/HoKS06a.pdf>.
- W3C, “OWL 2 Errata.” Current page consulted 2026-08-22: <https://www.w3.org/2001/sw/wiki/OWL_Errata>.
- W3C, “W3C Document License--2002,” and “W3C Document License--2023.” <https://www.w3.org/copyright/document-license-2002/> and <https://www.w3.org/copyright/document-license-2023/>.
