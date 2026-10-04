"""Normalize author return JSONs into the placement shape integrate_wave collect expects
({body|annex: {host, after_input, input}}). Writes copies; author files are untouched.
Usage: python -B work/waves/tooling/normalize_returns.py OUTDIR RETURN.json..."""
import json, os, re, sys

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


def rel_input(path):
    p = path.replace("\\", "/")
    if p.startswith("handbook/"):
        p = p[len("handbook/"):]
    return p[:-4] if p.endswith(".tex") else p


def inputs_in(host):
    lines = open(host, encoding="utf-8").read().split("\n")
    return [m.group(1) for line in lines if not line.lstrip().startswith("%") for m in [INPUT_RE.search(line)] if m]


def fix(pl, problems, where):
    if not isinstance(pl, dict):
        return pl
    pl = dict(pl)
    if not pl.get("input") and pl.get("file"):
        pl["input"] = rel_input(pl["file"])
    if not pl.get("after_input") and pl.get("before_input"):
        host = pl.get("host", "")
        seq = inputs_in(host) if os.path.isfile(host) else []
        tgt = rel_input(pl["before_input"])
        if tgt in seq and seq.index(tgt) > 0:
            pl["after_input"] = seq[seq.index(tgt) - 1]
        else:
            problems.append(f"{where}: cannot convert before_input {tgt}")
    if pl.get("after_input"):
        pl["after_input"] = rel_input(pl["after_input"])
    for key in ("host", "input", "after_input"):
        if not pl.get(key):
            problems.append(f"{where}: lacks {key}")
    return pl


def main(outdir, paths):
    os.makedirs(outdir, exist_ok=True)
    problems = []
    for p in paths:
        r = json.load(open(p, encoding="utf-8"))
        groups = r["groups"] if isinstance(r.get("groups"), list) else [r]
        for i, g in enumerate(groups):
            pl = g.get("placement")
            if isinstance(pl, dict):
                for k, files in (("body", g.get("bodies")), ("annex", g.get("annexes"))):
                    if isinstance(pl.get(k), dict) and not pl[k].get("input") and files:
                        pl[k] = dict(pl[k], input=rel_input(files[0]))  # W0 returns: the group's own file
                g["placement"] = {k: (fix(v, problems, f"{os.path.basename(p)}:{k}") if k in ("body", "annex") else v)
                                  for k, v in pl.items()}
        out = os.path.join(outdir, os.path.basename(p))
        json.dump(r, open(out, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print(len(paths), "returns normalized;", len(problems), "problems")
    for x in problems:
        print("  -", x)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
