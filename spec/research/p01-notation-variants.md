# A-025 research: representative historical notation variants

Status: source-verified mapping for a compact handbook comparison table. This note records one named work and edition per column; it does **not** claim that any notation was universal for an author, school, period, or later edition.

## Recommended table

The first column is only the handbook's modern comparison key. Historical cells preserve the cited source's argument order and variable letters.

| Role (handbook key) | Whitehead--Russell, *Principia Mathematica* I (1910) | Łukasiewicz, *Elementy logiki matematycznej* (1929) | Hilbert--Ackermann, *Grundzüge* (1st ed., 1928) | Gentzen, “Untersuchungen … I” (1935) |
|---|---|---|---|---|
| negation (\(\neg A\)) | \(\sim p\) | \(Np\) | \(\overline{X}\) | \(\neg A\) |
| conjunction (\(A\land B\)) | \(p.q\) | \(Kpq\) | \(X\mathbin{\&}Y\) | \(A\mathbin{\&}B\) |
| inclusive disjunction (\(A\lor B\)) | \(p\lor q\) | \(Apq\) | \(X\lor Y\) | \(A\lor B\) |
| conditional / implication (\(A\to B\)) | \(p\supset q\) | \(Cpq\) | \(X\to Y\) | \(A\supset B\) |
| biconditional / equivalence (\(A\leftrightarrow B\)) | \(p\equiv q\) | \(Epq\) | \(X\sim Y\) | \(A\supset\subset B\), **defined abbreviation**, not an admitted primitive formula-former |
| universal quantification (\(\forall x\,A\)) | \((x).\,\phi x\) | \(\Pi p\,\varphi(p)\) | \((x)A(x)\) | \(\forall x\,A\) |
| existential quantification (\(\exists x\,A\)) | \((\exists x).\,\phi x\) | \(\Sigma p\,\varphi(p)\) | \((E x)A(x)\) | \(\exists x\,A\) |

## Primary-source support

### Whitehead--Russell (the representative “Peano/Russell” column)

Alfred North Whitehead and Bertrand Russell, *Principia Mathematica*, vol. I (Cambridge: Cambridge University Press, 1910), first edition. The Introduction defines the propositional signs across printed pp. 6--8 and apparent-variable notation at pp. 16--17 in the [Project Gutenberg primary-text facsimile](https://www.gutenberg.org/files/78050/78050-h/78050-h.htm#Page_6). Exact formula images are available for [\(\sim p\)](https://www.gutenberg.org/files/78050/78050-h/images/58.svg), [\(p\lor q\)](https://www.gutenberg.org/files/78050/78050-h/images/59.svg), [\(p.q\)](https://www.gutenberg.org/files/78050/78050-h/images/60.svg), [\(p\supset q\)](https://www.gutenberg.org/files/78050/78050-h/images/71.svg), [\(p\equiv q\)](https://www.gutenberg.org/files/78050/78050-h/images/72.svg), [\((x).\phi x\)](https://www.gutenberg.org/files/78050/78050-h/images/149.svg), and [\((\exists x).\phi x\)](https://www.gutenberg.org/files/78050/78050-h/images/151.svg).

Scope note: this supports a column titled “Whitehead--Russell, *Principia Mathematica* I (1910),” not an undifferentiated “Peano/Russell notation.” The dot is both a logical-product sign and part of *Principia*'s scope punctuation; reproduce the displayed form rather than normalizing it silently to \(\land\).

### Łukasiewicz

Jan Łukasiewicz, *Elementy logiki matematycznej*, authorized lecture notes prepared by M. Presburger (Warsaw: Nakładem Komisji Wydawniczej Koła Matematyczno-Fizycznego Słuchaczów Uniwersytetu Warszawskiego, 1929). The primary scan defines \(N\) and \(C\) at [pp. 38--39](https://books.google.com/books?id=5VFaAAAAYAAJ&pg=PA38), \(A\) and \(K\) at [p. 55](https://books.google.com/books?id=5VFaAAAAYAAJ&pg=PA55), and \(E\) at [p. 58](https://books.google.com/books?id=5VFaAAAAYAAJ&pg=PA58). It gives the general quantifier \(\Pi\) and the prefix form \(\Pi p\varphi(p)\) at [p. 155](https://books.google.com/books?id=5VFaAAAAYAAJ&pg=PA155), then introduces the particular quantifier \(\Sigma\) and \(\Sigma p\varphi(p)\) at [p. 158](https://books.google.com/books?id=5VFaAAAAYAAJ&pg=PA158). The [scan record](https://books.google.com/books/about/Elementy_logiki_matematycznej.html?id=5VFaAAAAYAAJ) identifies the 1929, 200-page edition.

Standing caveat: in the cited Part IV passage, \(p\) is a **propositional variable**. Thus pp. 155 and 158 directly support the \(\Pi/\Sigma\) glyphs and prefix placement, but they must not be cited as if that passage itself introduced first-order individual quantification. The table is a notation comparison, not a claim that the bound-variable types coincide.

### Hilbert--Ackermann

David Hilbert and Wilhelm Ackermann, *Grundzüge der theoretischen Logik*, 1st ed., Grundlehren der mathematischen Wissenschaften 27 (Berlin: Julius Springer, 1928). Printed [p. 3](https://books.google.com/books?id=DlCP9FtlR4cC&pg=PA3) introduces \(\overline X\), \(X\&Y\), and the v-shaped inclusive-disjunction sign; [p. 4](https://books.google.com/books?id=DlCP9FtlR4cC&pg=PA4) introduces \(X\to Y\) and takes \(X\sim Y\) as its principal truth-equivalence notation. Printed [pp. 46--47](https://books.google.com/books?id=DlCP9FtlR4cC&pg=PA46) introduce the *Allzeichen* \((x)A(x)\) and *Seinszeichen* \((Ex)A(x)\). The [full-view first-edition record](https://books.google.com/books/about/Grundz%C3%BCge_der_theoretischen_logik.html?id=DlCP9FtlR4cC) supplies the edition metadata.

Encoding note: the 1928 disjunction glyph is visibly v-shaped and is stated to mean “oder”; \(\lor\) is the clean comparison-table encoding. Do not substitute modern \(\forall,\exists\) for the book's parenthesized \((x)\) and \((Ex)\). Also do not confuse its logical \(\sim\) with the later metalinguistic print abbreviation “äq,” which the book expressly says is not one of its logical symbols (p. 5).

### Gentzen

Gerhard Gentzen, “Untersuchungen über das logische Schließen. I,” *Mathematische Zeitschrift* 39 (1935): 176--210, [doi:10.1007/BF01201353](https://doi.org/10.1007/BF01201353). The official Göttingen scan is available as an [article PDF](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0039/LOG_0032.pdf). Printed [p. 178](https://images.sub.uni-goettingen.de/iiif/image/gdz:PPN266833020_0039:00000182/full/1200,/0/default.jpg) lists \(\&\), \(\lor\), \(\supset\), \(\supset\subset\), \(\neg\), \(\forall\), and \(\exists\). Printed [p. 179](https://images.sub.uni-goettingen.de/iiif/image/gdz:PPN266833020_0039:00000183/full/1200,/0/default.jpg) gives the formula formation clauses, deliberately excludes \(\supset\subset\), and defines \(A\supset\subset B\) as an abbreviation for \((A\supset B)\&(B\supset A)\). Printed [p. 180](https://images.sub.uni-goettingen.de/iiif/image/gdz:PPN266833020_0039:00000184/full/1200,/0/default.jpg) defines sequents and explicitly says that \(\to\), like the commas, is an auxiliary sign rather than a logical sign.

Critical table trap: Gentzen's object-language implication is \(\supset\), not the sequent arrow \(\to\). His equivalence mark may appear in a historical-sign inventory, but the cited grammar treats it only as a defined abbreviation.

## Claims to omit or qualify

- Do not title the first historical column simply “Peano/Russell.” Only the stated *Principia Mathematica* volume and edition were checked here; no independent Peano work was checked.
- Do not describe these as each author's notation “in general.” The mapping is work- and edition-specific.
- Do not claim common bound-variable standing. In particular, Łukasiewicz's cited \(\Pi/\Sigma\) examples bind propositional \(p\), while the other cited quantifier examples bind object variables.
- Do not list Gentzen's \(\to\) under implication, or \(\supset\subset\) as primitive.
- Do not normalize *Principia*'s dot, Hilbert--Ackermann's overbar and parenthesized quantifiers, or Polish prefix order inside the historical cells. The point of A-025 is the variant notation.

## Recommended caption

> **Representative notation in four named primary sources.** Entries reproduce the displayed forms in the cited works and editions; they compare glyph and argument placement, not the types of bound variables, primitive bases, or every notation used by the authors elsewhere.
