"""Direct finite-term critical-pair recomputation for Klop1987 Table12.

This is mathematical enumeration/certificate data, not a prose test suite.
The handbook proof states the exhaustiveness and verifies the joining paths.
"""
import json

def E(): return ("e", ())
def I(x): return ("I", (x,))
def M(x, y): return (".", (x, y))

x, y, z = "x", "y", "z"
RULES = [
    (1, M(E(), x), x),
    (2, M(I(x), x), E()),
    (3, M(M(x, y), z), M(x, M(y, z))),
    (4, M(I(x), M(x, z)), z),
    (8, M(y, E()), y),
    (9, I(I(y)), y),
    (10, I(E()), E()),
    (11, M(y, I(y)), E()),
    (12, M(y, M(I(y), x)), x),
    (15, I(M(x, y)), M(I(y), I(x))),
]

def apply(term, subst):
    if isinstance(term, str):
        return apply(subst[term], subst) if term in subst else term
    return (term[0], tuple(apply(a, subst) for a in term[1]))

def occurs(var, term):
    return term == var if isinstance(term, str) else any(occurs(var, a) for a in term[1])

def unify(left, right):
    pending, subst = [(left, right)], {}
    while pending:
        s, t = pending.pop()
        s, t = apply(s, subst), apply(t, subst)
        if s == t:
            continue
        if isinstance(s, str):
            if occurs(s, t): return None
            subst[s] = t
        elif isinstance(t, str):
            if occurs(t, s): return None
            subst[t] = s
        elif s[0] != t[0] or len(s[1]) != len(t[1]):
            return None
        else:
            pending.extend(zip(s[1], t[1]))
    return {var: apply(value, subst) for var, value in subst.items()}

def renamed(term, prefix):
    if isinstance(term, str): return prefix + term
    return term[0], tuple(renamed(a, prefix) for a in term[1])

def positions(term, prefix=()):
    if isinstance(term, str): return
    yield prefix
    for j, arg in enumerate(term[1], 1):
        yield from positions(arg, prefix + (j,))

def at(term, pos):
    for j in pos: term = term[1][j - 1]
    return term

def replace(term, pos, value):
    if not pos: return value
    args = list(term[1])
    args[pos[0] - 1] = replace(args[pos[0] - 1], pos[1:], value)
    return term[0], tuple(args)

def match(pattern, term, subst=None):
    subst = {} if subst is None else subst
    if isinstance(pattern, str):
        if pattern in subst: return subst if subst[pattern] == term else None
        subst[pattern] = term
        return subst
    if isinstance(term, str) or pattern[0] != term[0] or len(pattern[1]) != len(term[1]):
        return None
    for p, t in zip(pattern[1], term[1]):
        if match(p, t, subst) is None: return None
    return subst

def normalize(term):
    trace = []
    for _ in range(10000):
        selected = None
        for pos in positions(term):
            target = at(term, pos)
            for number, lhs, rhs in RULES:
                subst = match(lhs, target)
                if subst is not None:
                    selected = number, pos, replace(term, pos, apply(rhs, subst))
                    break
            if selected: break
        if selected is None: return term, trace
        number, pos, new = selected
        trace.append({"rule": number, "position": list(pos), "term": new})
        term = new
    raise RuntimeError("Normalization exceeded the explicit computation bound")

def canonical(terms):
    mapping = {}
    def visit(term):
        if isinstance(term, str):
            if term not in mapping: mapping[term] = f"v{len(mapping) + 1}"
            return mapping[term]
        return term[0], tuple(visit(a) for a in term[1])
    return [visit(t) for t in terms]

def latex(term):
    if isinstance(term, str): return "x_{" + term[1:] + "}"
    if term[0] == "e": return "e"
    if term[0] == "I": return "I(" + latex(term[1][0]) + ")"
    return "(" + latex(term[1][0]) + r"\mathbin{.}" + latex(term[1][1]) + ")"

def main():
    attempts = unifiable = trivial = 0
    records, overlaps = [], []
    for outer, left, right in RULES:
        lo, ro = renamed(left, "o_"), renamed(right, "o_")
        for inner, li, ri in RULES:
            li, ri = renamed(li, "i_"), renamed(ri, "i_")
            for pos in positions(lo):
                attempts += 1
                subst = unify(at(lo, pos), li)
                if subst is None: continue
                unifiable += 1
                peak, a, b = canonical([apply(lo, subst), apply(ro, subst), apply(replace(lo, pos, ri), subst)])
                overlaps.append({"outer": outer, "inner": inner,
                                 "position": list(pos), "trivial": a == b})
                if a == b:
                    trivial += 1
                    continue
                na, ta = normalize(a)
                nb, tb = normalize(b)
                if na != nb: raise RuntimeError(f"Unjoined pair {outer}/{inner}/{pos}: {a} {b}")
                records.append({"outer": outer, "inner": inner, "position": list(pos),
                                "peak": peak, "left": a, "right": b,
                                "normal_form": na, "left_trace": ta, "right_trace": tb})
    print(json.dumps({"attempts": attempts, "unifiable": unifiable,
                      "trivial": trivial, "nontrivial": len(records),
                      "overlaps": overlaps, "pairs": records}))

if __name__ == "__main__": main()
