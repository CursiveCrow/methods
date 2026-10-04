"""List handbook parts/annex .tex files that are off the main.tex input route and belong to no
W0 backlog item, no retained pinned set, no excluded draft and no wave packet (W0 classifier input)."""
import glob, json, os, sys
from pathlib import Path

sys.path.insert(0, "tools")
import integrate_wave as iw  # noqa: E402
import check  # noqa: E402

counts, _errs = iw.static_input_counts(Path("handbook"))
routed = {c if c.endswith(".tex") else c + ".tex" for c in counts}
retained = set(check.HB_RETAINED_UNREACHABLE_READER_FILES)
items = json.load(open("work/waves/w00/items.json", encoding="utf-8"))
owned = {p[len("handbook/"):] for it in items for p in it["bodies"] + it["annexes"]}
excluded = {"parts/p15/hintikka-inductive-logic.tex", "annex/p15/hintikka-inductive-logic.tex",
            "parts/p10/abelian-categories-and-exact-sequences.tex",
            "annex/p10/abelian-categories-and-exact-sequences.tex"}
off, wave_files = [], []
for f in glob.glob("handbook/parts/**/*.tex", recursive=True) + glob.glob("handbook/annex/**/*.tex", recursive=True):
    rel = f.replace(os.sep, "/")[len("handbook/"):]
    if rel in routed or rel in retained or rel in owned or rel in excluded:
        continue
    (wave_files if "-w0" in rel else off).append(rel)
print(len(routed), "routed;", len(off), "unclassified off-route;", len(wave_files), "wave-packet files (not classified here)")
print(off)
json.dump(["handbook/" + r for r in off], open("work/waves/w00/unclassified.json", "w", encoding="utf-8"), indent=1)
