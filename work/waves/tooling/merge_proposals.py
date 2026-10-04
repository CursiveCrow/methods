"""Merge proposal previews (later files win per section) minus excluded sections, and residual
previews (later files win per (unit_id, component_id)).
Usage: python -B ... OUT_PROPOSALS OUT_RESIDUALS --exclude A,B,... --proposals P1 P2 ... --residuals R1 R2 ..."""
import argparse, json

ap = argparse.ArgumentParser()
ap.add_argument("out_proposals"); ap.add_argument("out_residuals")
ap.add_argument("--exclude", default="")
ap.add_argument("--proposals", nargs="+", default=[]); ap.add_argument("--residuals", nargs="+", default=[])
a = ap.parse_args()
skip = set(filter(None, a.exclude.split(",")))
props, res = {}, {}
for f in a.proposals:
    for line in open(f, encoding="utf-8"):
        if line.strip():
            p = json.loads(line)
            if p["section_id"] not in skip:
                props[p["section_id"]] = p
for f in a.residuals:
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            res[(r["unit_id"], r["component_id"])] = r
for path, items in ((a.out_proposals, props.values()), (a.out_residuals, res.values())):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in items)
print(len(props), "proposals;", len(res), "residual records")
