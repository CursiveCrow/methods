"""Minimal assessment-only packets (mode accounting) for sections served by routed groups, with
per-section assessment_keys and the queue units' required components.
Usage: python -B ... WAVE MANIFEST.json SECTIONS_MAP.json   (SECTIONS_MAP: {stem: [section ids]})"""
import glob, json, os, sys

wave, manifest, smap = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3], encoding="utf-8"))
sys.path.insert(0, "tools")
import waves  # noqa: E402

rows = {}
for f in glob.glob("spec/coverage/edition-2026/current-fulfillment/*.jsonl"):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            rows[r["section_id"]] = r
queue = {}
for line in open("spec/coverage/edition-2026/completion-work-queue.jsonl", encoding="utf-8"):
    if line.strip():
        u = json.loads(line)
        queue[u["unit_id"]] = u
groups = {g["stem"]: g for g in json.load(open(manifest, encoding="utf-8"))["groups"]}
os.makedirs(f"work/waves/{wave}/packets", exist_ok=True)
out = []
for stem, secs in smap.items():
    g = groups[stem]
    sel = [rows[s] for s in secs]
    unit_ids = sorted({fc["unit_id"] for r in sel for fc in r.get("source_facets") or []})
    files = ["handbook/" + p if not p.startswith("handbook/") else p
             for k in ("bodies", "annexes", "rule_sheets") for p in g.get(k) or []]
    pid = f"{wave}-acc-{stem}"
    packet = {"id": pid, "wave": wave, "part": sel[0]["part"], "mode": "accounting",
              "sections": waves._packet_summary_sections(sel, queue),
              "units": [{"unit_id": u, "title": queue[u].get("title"),
                         "required_components": queue[u].get("required_components")} for u in unit_ids if u in queue],
              "owned_files": [], "editable_hosts": [], "readonly_hosts": files,
              "note": "Assessment-only packet: the listed files were routed in this wave; assess the route as it stands."}
    path = f"work/waves/{wave}/packets/{pid}.json"
    json.dump(packet, open(path, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    out.append({"id": pid, "path": path, "part": packet["part"], "mode": "accounting", "sections": secs, "max_blocks": 0})
print(json.dumps(out, ensure_ascii=False))
