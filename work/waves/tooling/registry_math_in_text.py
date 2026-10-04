"""List symbol-registry text cells (role, notes) that use math-only TeX commands or
Unicode math characters outside math delimiters (they break pdflatex in the tables)."""
import csv, re, sys

TEXT_OK = {"emph", "textit", "textbf", "texttt", "textsc", "textrm", "textsf", "cite", "parencite", "textcite",
           "ref", "cref", "Cref", "eqref", "pageref", "S", "ldots", "dots", "_", "&", "%", "#", "allowbreak",
           "detokenize", "url", "href", "hyperref", "mbox", "enquote", "textquotedblleft", "textquotedblright",
           "o", "L", "l", "ss", "ae", "AE", "aa", "AA", "textendash", "textemdash", "nobreakspace", "relax"}
MATH = re.compile(r"\\\(.*?\\\)|\$[^$]*\$|\\\[.*?\\\]|\\ensuremath\{[^{}]*\}", re.S)
CMD = re.compile(r"\\([A-Za-z]+)")

rows = list(csv.reader(open("handbook/registry/symbols.csv", encoding="utf-8-sig", newline="")))
head = rows[0]
bad = []
for n, r in enumerate(rows[1:], start=2):
    for col in ("role", "notes"):
        cell = r[head.index(col)]
        outside = MATH.sub(" ", cell)
        cmds = {c for c in CMD.findall(outside) if c not in TEXT_OK}
        uni = {ch for ch in outside if ord(ch) > 0x2000 or 0x370 <= ord(ch) <= 0x3FF}
        if cmds or uni:
            bad.append((n, col, sorted(cmds), sorted(uni)))
print(len(bad), "cells")
for b in bad[:40]:
    print(b)
