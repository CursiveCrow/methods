"""Build workflow args for a keyed re-assessment (max_blocks 0) of given sections: each packet
entry carries keys[section] = owed component ids (the row's facet units) and recorded duties
(MP-i = missing_pieces[i], US-i = unassessed_scope[i]).
Usage: python -B ... WAVE OUT.json RESULTS.json:SEC,SEC,... [RESULTS.json:SEC,...]"""
import glob, json, sys

wave, out, specs = sys.argv[1], sys.argv[2], sys.argv[3:]
rows = {}
for f in glob.glob("spec/coverage/edition-2026/current-fulfillment/*.jsonl"):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            rows[r["section_id"]] = r
comps = {}
for line in open("spec/coverage/edition-2026/completion-work-queue.jsonl", encoding="utf-8"):
    if line.strip():
        u = json.loads(line)
        comps[u["unit_id"]] = [c["component_id"] for c in u.get("required_components") or []]


def duty_text(x):
    return x.get("duty") if isinstance(x, dict) else str(x)


packets = {}
for spec in specs:
    path, secs = spec.rsplit(":", 1)
    want = set(secs.split(","))
    res = json.load(open(path, encoding="utf-8"))
    for r in res["results"]:
        for s in r.get("sections") or []:
            sid = s["section_id"]
            if sid not in want:
                continue
            want.discard(sid)
            row = rows[sid]
            owed = []
            for f in row.get("source_facets") or []:
                owed += [c for c in comps.get(f.get("unit_id"), []) if c not in owed]
            duties = [{"duty_id": f"MP-{i}", "duty": duty_text(x)} for i, x in enumerate(row.get("missing_pieces") or [])]
            duties += [{"duty_id": f"US-{i}", "duty": duty_text(x)} for i, x in enumerate(row.get("unassessed_scope") or [])]
            pid = r["id"].split(".")[0]
            found = glob.glob(f"work/waves/*/packets/{pid}.json")
            if len(found) != 1:
                sys.exit(f"packet {pid}: expected one packet file, found {found}")
            pk = packets.setdefault(pid, {"id": pid, "path": found[0].replace(chr(92), "/"), "mode": "accounting",
                                           "sections": [], "max_blocks": 0, "keys": {}})
            pk["sections"].append(sid)
            pk["keys"][sid] = {"components": owed, "duties": duties}
    if want:
        sys.exit(f"{path}: sections not found {sorted(want)}")
for pk in packets.values():
    pk["part"] = json.load(open(pk["path"], encoding="utf-8"))["part"]
args = {"wave": wave, "root": "C:/Dev/the-methods-of-reason", "maxConcurrent": 12, "agentBudget": 200,
        "lanes": [{"packets": [pk]} for pk in packets.values()]}
json.dump(args, open(out, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(len(packets), "packets,", sum(len(p["sections"]) for p in packets.values()), "sections")
