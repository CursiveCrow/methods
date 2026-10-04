"""Wrap the two bare math fragments in the notes of symbols.csv line 6388 in \\( \\)."""
BS = "\\"
p = "handbook/registry/symbols.csv"
lines = open(p, encoding="utf-8", newline="").read().split("\n")
old = lines[6387]
a = "glyph: " + BS + "vdash_" + BS + "ell declarative"
b = "glyph: " + BS + "(" + BS + "vdash_" + BS + "ell" + BS + ") declarative"
c = "relation; " + BS + "operatorname{Cn}_" + BS + "ell declarative"
d = "relation; " + BS + "(" + BS + "operatorname{Cn}_" + BS + "ell" + BS + ") declarative"
assert old.count(a) == 1 and old.count(c) == 1, "fragments not found exactly once"
lines[6387] = old.replace(a, b).replace(c, d)
open(p, "w", encoding="utf-8", newline="").write("\n".join(lines))
print("row 6388 fixed")
