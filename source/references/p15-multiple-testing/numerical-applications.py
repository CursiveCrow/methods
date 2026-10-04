"""Evaluate Holm's normal power example by an exact finite bin recursion.

This is a mathematical calculation for the manuscript, not a prose test suite.
The recursion follows the independent normal model specified on pp.67-68.
"""
from collections import defaultdict
from itertools import product
from math import comb, sqrt
from statistics import NormalDist
import json

normal = NormalDist()
alpha = 0.05
n = 10
counts = (4, 4, 2)
means = (0.0, 6.0, 3.0)
cutoffs = [0.0] + [alpha / (n - rank + 1) for rank in range(1, n + 1)]

def p_cdf(probability, mean):
    if probability == 0:
        return 0.0
    if probability == 1:
        return 1.0
    return normal.cdf(mean - normal.inv_cdf(1.0 - probability))

states = {(0, 0, 0): 1.0}
success = 0.0
for bin_index in range(1, n + 1):
    previous, current = cutoffs[bin_index - 1], cutoffs[bin_index]
    conditional_bin = []
    for mean in means:
        old_mass = p_cdf(previous, mean)
        new_mass = p_cdf(current, mean)
        conditional_bin.append((new_mass - old_mass) / (1.0 - old_mass))
    new_states = defaultdict(float)
    for placed, probability in states.items():
        choices = [range(total - done + 1) for total, done in zip(counts, placed)]
        for added in product(*choices):
            weight = probability
            for total, done, take, chance in zip(counts, placed, added, conditional_bin):
                remaining = total - done
                weight *= comb(remaining, take) * chance ** take * (1.0 - chance) ** (remaining - take)
            if weight == 0:
                continue
            if sum(added) and sum(placed) + 1 < bin_index:
                continue  # First member of this bin fails, so the test stops.
            updated = tuple(done + take for done, take in zip(placed, added))
            if updated[2] == 2:
                success += weight  # Both designated mean-three tests are rejected.
            else:
                new_states[updated] += weight
    states = new_states

critical = normal.inv_cdf(1.0 - alpha / n)
bonferroni_both = normal.cdf(3.0 - critical) ** 2
record = {
    "model": "Ten independent N(mu,1) observations, four mu=0, four mu=6, two mu=3",
    "alpha": alpha,
    "normal_bonferroni_critical": critical,
    "bonferroni_both_mu3_power": bonferroni_both,
    "holm_both_mu3_power": success,
    "holm_source_reported": {"bonferroni": 0.439, "holm": 0.565},
    "unadjusted_20_global_null_fwer": 1.0 - (1.0 - alpha) ** 20,
    "bonferroni_20_global_null_fwer": 1.0 - (1.0 - alpha / 20) ** 20,
    "sidak_2_antithetic_null_fwer": 2.0 * (1.0 - sqrt(1.0 - alpha)),
    "data_selected_weight_fwer": 1.0 - (1.0 - 99.0 * alpha / 100.0) ** 2,
    "status": "Finite recursion evaluated in ordinary floating point; formula is supplied in the annex",
}
print(json.dumps(record, indent=2))
