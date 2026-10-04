"""Report (or, with --apply, escape) bare TeX specials outside math in the text cells
(role, notes) of handbook/registry/symbols.csv. Cells are LaTeX-valued by convention
(tools/symbols2tex.py), so a bare _ # & % or ^ outside \\(..\\) / $..$ breaks the
generated tables. Edits are minimal substring replacements inside the raw line, so
quoting and every other byte of the CSV are preserved."""
import csv, io, re, sys

PATH = "handbook/registry/symbols.csv"
MATH = re.compile(r"\\\(.*?\\\)|\$[^$]*\$|\\\[.*?\\\]", re.S)
SPECIAL = re.compile(r"(?<!\\)([_#&%^])")


def escape_outside_math(cell):
    out, pos = [], 0
    for m in MATH.finditer(cell):
        out.append(SPECIAL.sub(lambda s: "\\" + s.group(1) + ("{}" if s.group(1) == "^" else ""), cell[pos:m.start()]))
        out.append(m.group())
        pos = m.end()
    out.append(SPECIAL.sub(lambda s: "\\" + s.group(1) + ("{}" if s.group(1) == "^" else ""), cell[pos:]))
    return "".join(out)


def main(apply):
    raw = open(PATH, encoding="utf-8", newline="").read()
    lines = raw.split("\n")
    header = next(csv.reader([lines[0]]))
    idx = [header.index("role"), header.index("notes")]
    changed = []
    for n, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        fields = next(csv.reader(io.StringIO(line)))
        new_line = line
        for i in idx:
            cell = fields[i]
            fixed = escape_outside_math(cell)
            if fixed != cell:
                for old, new in ((f'"{cell}"', f'"{fixed}"'), (cell, fixed)):
                    if new_line.count(old) == 1:
                        new_line = new_line.replace(old, new)
                        break
                else:
                    raise SystemExit(f"line {n}: cannot locate cell uniquely: {cell!r}")
        if new_line != line:
            assert next(csv.reader(io.StringIO(new_line)))[:idx[0]] == fields[:idx[0]]
            changed.append((n, line, new_line))
            lines[n - 1] = new_line
    print(len(changed), "rows with bare specials in role/notes")
    for n, a, b in changed[:8]:
        print(n, "|", b[-160:])
    if apply and changed:
        open(PATH, "w", encoding="utf-8", newline="").write("\n".join(lines))
        print("applied")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        assert escape_outside_math("path u_i and \\(u_i\\)") == "path u\\_i and \\(u_i\\)"
        assert escape_outside_math("already \\_ ok, 5% & #1") == "already \\_ ok, 5\\% \\& \\#1"
        print("selftest ok")
    else:
        main("--apply" in sys.argv)
