"""Group lead-owned patch requests (group_patches.py lead backlogs of one or more waves) into the
request files tmor-wave-integrate.js takes: one per restoration capture, plus tools, sty,
frontmatter and registry. Requests whose text is already present in the target are dropped
(listed as already_applied). Drivers and route insertions are left to integrate_wave route.
Usage: python -B work/waves/tooling/group_lead.py WAVE BACKLOG.json... > args fragment on stdout"""
import collections
import json
import os
import re
import sys

wave, backlogs = sys.argv[1], sys.argv[2:]
out_dir = f"work/waves/{wave}/lead"
os.makedirs(out_dir, exist_ok=True)
groups, already, other = collections.defaultdict(list), [], []
for path in backlogs:
    for it in json.load(open(path, encoding="utf-8")):
        req = it.get("request")
        if not isinstance(req, dict):
            other.append({**it, "why": "no request object"})
            continue
        host = (req.get("host") or "").replace("\\", "/")
        if host and not host.startswith(("handbook/", "tools/")):
            host = "handbook/" + host
        text = (req.get("text") or "").strip()
        if host and os.path.isfile(host) and text and text in open(host, encoding="utf-8").read():
            already.append({**it, "host": host})
            continue
        if host.startswith("handbook/restoration/inherited-"):
            key = "capture:" + host
        elif host.startswith("tools/"):
            key = "tools"
        elif host == "handbook/handbook.sty":
            key = "sty"
        elif host == "handbook/frontmatter.tex":
            key = "frontmatter"
        elif host.startswith("handbook/registry/symbol"):
            key = "registry"
        else:
            other.append({**it, "host": host, "why": "driver, generated view or unparsed request"})
            continue
        groups[key].append({**it, "source_backlog": path})
frag = {"captures": []}
for key, items in sorted(groups.items()):
    if key.startswith("capture:"):
        host = key.split(":", 1)[1]
        rng = re.search(r"inherited-(\d{5}-\d{5})\.tex$", host).group(1)
        pid = next(f[:-5] for f in sorted(os.listdir("spec/provenance")) if f.endswith(f"-{rng}.json"))
        schema = json.load(open(f"spec/provenance/{pid}.json", encoding="utf-8"))["schema_version"]
        f = f"{out_dir}/requests-{pid}.json"
        json.dump(items, open(f, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        frag["captures"].append({"host": host, "file": f, "pid": pid, "schema": schema})
    else:
        f = f"{out_dir}/requests-{key}.json"
        json.dump(items, open(f, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
        frag["registry_file" if key == "registry" else key] = f if key == "registry" else {"file": f}
json.dump({"already_applied": already, "other": other}, open(f"{out_dir}/ungrouped.json", "w", encoding="utf-8", newline="\n"),
          ensure_ascii=False, indent=1)
print(json.dumps(frag, indent=1))
print(f"captures {len(frag['captures'])}, requests {sum(len(v) for v in groups.values())}, "
      f"already applied {len(already)}, other {len(other)}", file=sys.stderr)
