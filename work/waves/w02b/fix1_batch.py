"""Merge the W2-b fix-round intakes (handbook/registry/symbols-intake-w02b-fix1-<k>.csv) and their
decision files into adoption batch 12. Decision lists are concatenated; dict sections merged
(a key decided twice must agree). Usage: python -B work/waves/w02b/fix1_batch.py"""
import glob
import json
import os
import re

groups, merged = [], {}
for path in sorted(glob.glob("handbook/registry/symbols-intake-w02b-fix1-*.csv")):
    k = re.search(r"fix1-(\d+)\.csv$", path).group(1)
    manifest = json.load(open(f"tmp/fix1-{k}-manifest.json", encoding="utf-8"))
    groups.append({**manifest["groups"][0], "integration_status": "routed-awaiting-canonical-merge",
                   "routing_note": "Lead fix-round intake: registers notation the W2-b check found unregistered or out of scope."})
    dec_path = f"work/waves/w02b/fix1/decisions-{k}.json"
    decisions = json.load(open(dec_path, encoding="utf-8")) if os.path.isfile(dec_path) else {}
    for key, value in decisions.items():
        if isinstance(value, list):
            merged.setdefault(key, []).extend(value)
        elif isinstance(value, dict):
            target = merged.setdefault(key, {})
            for sub, item in value.items():
                if sub in target and target[sub] != item:
                    raise SystemExit(f"conflicting decisions for {key}/{sub} (bucket {k})")
                target[sub] = item
        else:
            raise SystemExit(f"unexpected decisions value {key} in {dec_path}")
manifest = {"standing": "W2-b lead fix-round symbol intakes; integration, source admission and independent acceptance remain separate.",
            "wave": 12, "groups": groups}
json.dump(manifest, open("spec/research/edition-2026-authoring-batch-intake-12.json", "w", encoding="utf-8", newline="\n"),
          ensure_ascii=False, indent=2)
json.dump(merged, open("work/waves/w02b/fix1/decisions-merged.json", "w", encoding="utf-8", newline="\n"),
          ensure_ascii=False, indent=1)
print(len(groups), "groups;", {k: len(v) for k, v in merged.items()})
