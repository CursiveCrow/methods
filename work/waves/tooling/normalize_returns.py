"""Normalize author return JSONs into the placement shape integrate_wave collect expects
({body|annex: {host, after_input, input}}). Writes copies; author files are untouched.
Usage: python -B work/waves/tooling/normalize_returns.py OUTDIR RETURN.json..."""
import json, os, re, sys

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


def rel_input(path):
    m = INPUT_RE.search(path)  # some returns give the whole \input{...} line
    p = (m.group(1) if m else path).replace("\\", "/")
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
    # patch-request shape: {host, operation: insert_after, anchor_quote: "\input{A}", text: "\input{B}"}
    if pl.get("operation", "insert_after") == "insert_after" and not pl.get("after_input") and INPUT_RE.search(pl.get("anchor_quote") or ""):
        pl["after_input"] = pl["anchor_quote"]
    if not pl.get("input") and INPUT_RE.search(pl.get("text") or ""):
        pl["input"] = pl["text"]
    if not pl.get("input") and pl.get("file"):
        pl["input"] = rel_input(pl["file"])
    if pl.get("input"):
        pl["input"] = rel_input(pl["input"])
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
                # collect reads body/annex placements (and a note); other keys move aside
                extra = {k: v for k, v in pl.items() if k not in ("body", "annex", "note")}
                if extra:
                    g["placement_extra"] = extra
                g["placement"] = {k: (fix(v, problems, f"{os.path.basename(p)}:{k}") if k in ("body", "annex") else v)
                                  for k, v in pl.items() if k in ("body", "annex", "note")}
        # files_written entries annotated with prose ("path (lines 3-9 ...)") keep only the path
        if isinstance(r.get("files_written"), list):
            r["files_written"] = [w.split()[0] for w in r["files_written"] if isinstance(w, str) and w.strip()]
        # note must name the research note file; prose goes to note_text
        note = r.get("note")
        if isinstance(note, str) and not os.path.isfile(note):
            default = p.replace("-return.json", ".md")
            r["note_text"], r["note"] = note, (default.replace("\\", "/") if os.path.isfile(default) else None)
            problems.append(f"{os.path.basename(p)}: note was prose; moved to note_text")
        out = os.path.join(outdir, os.path.basename(p))
        json.dump(r, open(out, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    print(len(paths), "returns normalized;", len(problems), "problems")
    for x in problems:
        print("  -", x)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
