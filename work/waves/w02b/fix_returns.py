"""W2-b placement fixups applied to the normalized returns (run after normalize_returns.py).
Returns of packets that created no body/annex file get a null placement (their edits are in
editable hosts); returns lacking an input or anchor get it from their own insert line, the
author's stated preferred anchor or the packet default. Writes FIXUPS.json as the record."""
import json

D = "work/waves/w02b/returns-normalized/"
NO_FILES = [
    "p01-symbol-registry-w02b-p01-014",
    "p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036",
    "p15-bayesian-model-comparison-computation-and-criticism-w02b-p15-056",
    "p15-conditioning-independence-and-information-w02b-p15-009",
    "p15-probability-logics-and-alternative-representations-of-w02b-p15-033",
    "p15-probability-logics-and-alternative-representations-of-w02b-p15-038",
]
FILL = {  # stem -> (body after_input, annex after_input, why); None keeps the return's anchor
    "p15-inductive-logic-and-confirmation-w02b-p15-027": (
        "parts/p15/popper-hypothetico-deductive-reasoning", "annex/p15/popper-hypothetico-deductive-reasoning",
        "author's preferred anchor (after the Popper chapter)"),
    "p15-information-and-description-based-inference-w02b-p15-045": (None, None, "input from the return's insert line"),
    "p15-sequential-evidence-and-multiple-testing-w02b-p15-063": (None, None, "input from the return's insert line"),
    "p15-statistical-learning-and-generalization-w02b-p15-066": (
        "parts/p15/bounded-concentration-learning", "annex/p15/bounded-concentration-learning", "packet default anchor"),
}


def path(stem):
    return f"{D}edition-2026-{stem}-return.json"


log = {}
for stem in NO_FILES:
    r = json.load(open(path(stem), encoding="utf-8"))
    r["placement_original"], r["placement"] = r.get("placement"), {"body": None, "annex": None}
    json.dump(r, open(path(stem), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    log[stem] = "no new body/annex file: in-place editable-host edits only, nothing to route"
for stem, (body_after, annex_after, why) in FILL.items():
    r = json.load(open(path(stem), encoding="utf-8"))
    name = stem.split("-", 1)[1]
    for key, after, top in (("body", body_after, "parts"), ("annex", annex_after, "annex")):
        r["placement"][key]["input"] = r["placement"][key].get("input") or f"{top}/p15/{name}"
        if after:
            r["placement"][key]["after_input"] = after
    json.dump(r, open(path(stem), "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    log[stem] = why
json.dump(log, open(D + "FIXUPS.json", "w", encoding="utf-8", newline="\n"), indent=1)
print(len(log), "fixups")
