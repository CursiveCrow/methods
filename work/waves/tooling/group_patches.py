"""Group a wave's author patch requests by target host. Lead-owned targets (restoration
captures, generated views, canonical registries, tools, drivers, main/sty) go to a lead
backlog; every other host gets one request file for a host-patch agent.
Usage: python -B work/waves/tooling/group_patches.py wNN"""
import collections, glob, json, os, sys

wave = sys.argv[1]
root = f"work/waves/{wave}"
by, lead = collections.defaultdict(list), []


def lead_owned(h):
    if h.startswith(("handbook/restoration/", "handbook/generated/", "handbook/registry/symbol", "tools/")):
        return True
    if h in ("handbook/main.tex", "handbook/handbook.sty", "handbook/frontmatter.tex"):
        return True
    parts = h.split("/")
    return len(parts) == 3 and parts[1] in ("parts", "annex") and parts[2].startswith("p")  # part/annex drivers


for f in sorted(glob.glob(f"{root}/patches/*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        lead.append({"patch_file": f, "reason": "unparseable"})
        continue
    items = d if isinstance(d, list) else d.get("patches", d.get("requests", [d]))
    for i, it in enumerate(items):
        if not isinstance(it, dict):
            continue
        h = (it.get("host") or "").replace(os.sep, "/").replace(chr(92), "/")
        if h and not h.startswith(("handbook/", "tools/")):
            h = "handbook/" + h
        rec = {"patch_file": f, "index": i, "request": it}
        (lead.append({**rec, "reason": "lead-owned host"}) if (not h or lead_owned(h)) else by[h].append(rec))
os.makedirs(f"{root}/host-patches", exist_ok=True)
hosts = []
for h, recs in sorted(by.items()):
    slug = h.replace("handbook/", "").replace("/", "__")
    json.dump(recs, open(f"{root}/host-patches/{slug}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    hosts.append({"host": h, "file": f"{root}/host-patches/{slug}.json", "n": len(recs)})
json.dump(lead, open(f"{root}/lead-backlog-patches.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(hosts, open(f"{root}/host-patches/index.json", "w", encoding="utf-8"), indent=1)
print(len(hosts), "hosts;", sum(x["n"] for x in hosts), "requests; lead-owned", len(lead))
