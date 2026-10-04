"""Assessment-only (accounting) packets own no files, so assessors filed authoring gaps in routed
files as lead_owned. Reclassify: a lead_owned item whose substance is writing in a handbook body or
annex becomes a writable gap (sections: open_gaps; units: kind writable); a note that only says the
packet owns nothing (META_PREFIXES, read by the lead) is dropped; items about lead records
(held-sources bindings, destination naming US-2) stay lead_owned. Writes a copy.
Usage: python -B ... IN.json OUT.json"""
import json, sys

KEEP = ("held-sources.json", "US-2")
META_PREFIXES = (  # whole-item notes with no gap content (W0 re-assessment)
    "Packet has no owned files or editable hosts. Every gap",
    "Packet has no owned or editable files (readonly hosts only",
    "The packet owns no files and has no editable hosts.",
    "handbook/parts/p19/language-categories-and-reasoning.tex is a read-only host for this packet",
    "handbook/parts/p19/language-categories-and-reasoning.tex is read-only for this packet",
)


def classify(text):
    text = text.strip()
    if any(k in text for k in KEEP):
        return "lead_owned"
    if text.startswith(META_PREFIXES):
        return "drop"
    return "writable"


d = json.load(open(sys.argv[1], encoding="utf-8"))
log = {"to_gap": 0, "dropped": 0, "kept": 0, "units_to_writable": 0}
for r in d["results"]:
    for s in r.get("sections") or []:
        blocked = []
        for b in s.get("blocked") or []:
            if b.get("kind") != "lead_owned":
                blocked.append(b)
                continue
            kind = classify(b.get("detail", ""))
            if kind == "writable":
                s.setdefault("gaps", []).append(b["detail"])
                log["to_gap"] += 1
            elif kind == "drop":
                log["dropped"] += 1
            else:
                blocked.append(b)
                log["kept"] += 1
        s["blocked"] = blocked
    for u in r.get("units") or []:
        for c in u.get("open_components") or []:
            if c.get("kind") == "lead_owned" and classify(c.get("gap", "")) != "lead_owned":
                c["kind"] = "writable"
                log["units_to_writable"] += 1
json.dump(d, open(sys.argv[2], "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(log)
