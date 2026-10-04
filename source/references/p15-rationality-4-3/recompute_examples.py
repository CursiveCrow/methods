"""Exact arithmetic for the finite Merin-chapter realizations.

These calculations check examples and construction domains; they are not
proofs of the general theorems, empirical reanalyses, or manuscript tests.
"""

from fractions import Fraction as F
from itertools import product


def branch_model(weight, inside, outside):
    law = {}
    for branch, rates in ((1, inside), (0, outside)):
        branch_mass = weight if branch else 1 - weight
        for bits in product((0, 1), repeat=len(rates)):
            mass = branch_mass
            for bit, rate in zip(bits, rates):
                mass *= rate if bit else 1 - rate
            law[(branch, *bits)] = mass
    return law


def probability(law, predicate):
    return sum((mass for world, mass in law.items() if predicate(world)), F(0))


def conditional(law, target, source):
    den = probability(law, source)
    if den <= 0:
        raise ValueError("Ratio conditional requires positive support")
    return probability(law, lambda w: target(w) and source(w)) / den


def report_law(name, law):
    total = sum(law.values(), F(0))
    if total != 1 or any(p < 0 for p in law.values()):
        raise ValueError((name, "invalid law", total))
    print(name, "normalized; minimum atom", min(law.values()))


def measures(law, source, target):
    h = probability(law, target)
    q = conditional(law, target, source)
    a = conditional(law, source, target)
    b = conditional(law, source, lambda w: not target(w))
    lr = a / b if b else ("+inf" if a else "neutral")
    return {"prior": h, "posterior": q, "D": q - h, "Q": q / h, "L": lr}


def covariance(law, first, second):
    return probability(law, lambda w: first(w) and second(w)) - (
        probability(law, first) * probability(law, second)
    )


law = {(0,): F(1, 3), (1,): F(1, 3), (2,): F(1, 3)}
a, b, c = lambda w: w[0] == 0, lambda w: w[0] != 2, lambda w: w[0] == 1
print("Nontransitive covariance chain:", covariance(law, a, b),
      covariance(law, b, c), covariance(law, a, c))

law = branch_model(F(1, 2), (F(4, 5), F(4, 5)), (F(1, 5), F(1, 5)))
report_law("Screening/Simpson realization", law)
a, c = lambda w: bool(w[1]), lambda w: bool(w[2])
print("P(A), P(C), P(AC), P(C|A):", probability(law, a),
      probability(law, c), probability(law, lambda w: a(w) and c(w)),
      conditional(law, c, a))

for name, hs, qs in (
    ("Ranking I", (F(3, 5), F(1, 10)), (F(9, 10), F(3, 10))),
    ("Ranking II", (F(1, 5), F(4, 5)), (F(1, 2), F(19, 20))),
    ("Equal likelihood/Q construction", (F(1, 5), F(3, 10)), (F(2, 5), F(3, 5))),
):
    e = F(1, 5)
    outside = tuple((h - e * q) / (1 - e) for h, q in zip(hs, qs))
    law = branch_model(e, qs, outside)
    report_law(name, law)
    print("Outside marginals:", outside)
    for j in (1, 2):
        print("Target", j, measures(law, lambda w: bool(w[0]),
                                   lambda w, j=j: bool(w[j])))

law = branch_model(F(1, 2), (F(2, 25), F(7, 10)), (F(1, 50), F(3, 10)))
report_law("Direction counterexample", law)
for j in (1, 2):
    src = lambda w, j=j: bool(w[j])
    tgt = lambda w: bool(w[0])
    print("Source", j, "forward", measures(law, src, tgt),
          "reverse D", conditional(law, src, tgt) - probability(law, src))

inside = (F(0), F(1, 100), F(4, 5), F(19, 100))
outside = (F(1, 200), F(1, 200), F(159, 200), F(39, 200))
law = {(h, cell): (F(1, 2) * row[cell])
       for h, row in ((1, inside), (0, outside)) for cell in range(4)}
report_law("Raven model", law)
for cell in (1, 2):
    print("Specimen cell", cell, measures(law, lambda w, cell=cell: w[1] == cell,
                                        lambda w: bool(w[0])))

prior = (F(2, 100), F(18, 100), F(48, 100), F(32, 100))
post = (F(1, 10), F(1, 20), F(7, 10), F(3, 20))
e = F(1, 10)
law = {(1, j): e * post[j] for j in range(4)}
law.update({(0, j): prior[j] - e * post[j] for j in range(4)})
report_law("Linda-structured nested targets", law)
for name, cells in (("BF", (0,)), ("B", (0, 1)), ("F", (0, 2))):
    print(name, measures(law, lambda w: bool(w[0]), lambda w, cells=cells: w[1] in cells))

law = {(1, 0): F(3, 50), (1, 1): F(3, 50), (1, 2): F(2, 25),
       (0, 0): F(7, 50), (0, 1): F(6, 25), (0, 2): F(21, 50)}
report_law("MDHD equality construction", law)
for name, cells in (("H1", (0,)), ("H1 union J", (0, 1)), ("J", (1,))):
    print(name, measures(law, lambda w: bool(w[0]), lambda w, cells=cells: w[1] in cells))

law = branch_model(F(3, 10), (F(49, 90), F(3, 5)), (F(1, 10), F(1, 5)))
report_law("MCIE prior-change construction", law)
source, target = lambda w: bool(w[2]), lambda w: bool(w[0])
print("Before E1:", measures(law, source, target))
e1 = probability(law, lambda w: bool(w[1]))
updated = {w: p / e1 for w, p in law.items() if w[1]}
report_law("After E1", updated)
print("After E1:", measures(updated, source, target))

print("Fair-card MDHD:", "D(H)=-1/52; D(H union red)=", F(1, 2) - F(27, 52),
      "Q(H union red)=", F(1, 2) / F(27, 52))
print("Source-negation L values:", F(3, 5) / F(1, 5),
      (1 - F(3, 5)) / (1 - F(1, 5)))
print("Extreme finite odds multiplier:", (F(999, 1000) / F(1, 1000)) ** 2)
print("Z slopes at h=.3 and h=.5:", (1 / F(3, 10), 1 / F(7, 10)), (F(2), F(2)))

for a, b in ((F(2, 5), F(1, 5)), (F(3, 4), F(1, 4)), (F(4, 5), F(2, 5))):
    one = a / b
    both = one * one
    union = (2 * a - a * a) / (2 * b - b * b)
    xor = (2 * a - 2 * a * a) / (2 * b - 2 * b * b)
    print("Compound likelihoods", (a, b), "single/union/both/xor:", one, union, both, xor)

h = F(3, 10)
aa, bb = (F(3, 10), F(2, 5)), (F(1, 10), F(2, 5))
source_mass = tuple(h * a + (1 - h) * b for a, b in zip(aa, bb))
print("Disjoint mixture weights D/Q and L:", source_mass[0] / sum(source_mass), bb[0] / sum(bb))
print("Disjoint union posterior/D/Q/L:", h * sum(aa) / sum(source_mass),
      h * sum(aa) / sum(source_mass) - h, sum(aa) / sum(source_mass), sum(aa) / sum(bb))
