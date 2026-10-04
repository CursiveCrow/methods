"""High-recall fusion candidates for the Codex-era sweep (work aid, not a guard).

Masks TeX like tools/find_fused_spaces.py, builds a prose vocabulary from the whole
handbook, and flags in the given files:
  W  rare tokens (corpus frequency <= 2, length >= 7) that split into two common
     corpus words (each frequency >= 5, length >= 2), e.g. "separatefromunheld";
  N  letter/digit mixtures not caught by the guard ("selects8", "Block1", "All79");
  P  punctuation glued to a following digit or word in prose (",12", ":18", "pre1325");
  M  a word glued to inline math ("stage\\(n+1\\)").
Output: JSON list of {path, line, cls, token, context}. Candidates need human/LLM
judgment; many are legitimate identifiers.

Usage: python -B work/waves/tooling/fusion_candidates.py FILELIST OUT.json
       python -B work/waves/tooling/fusion_candidates.py --selftest
"""
import collections, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
import find_fused_spaces as ffs  # noqa: E402

WORD = re.compile(r"[A-Za-z]+")
MIX = re.compile(r"(?<![\w\\/.:-])(?=[A-Za-z]*\d)(?=\d*[A-Za-z])[A-Za-z0-9]{3,}(?![\w/])")
PUNCT = re.compile(r"(?<=[A-Za-z]),(?=\d)|(?<=[A-Za-z]):(?=\d)|(?<=[a-z])-(?=\d{4}\b)")
GLUED_MATH = re.compile(r"[A-Za-z]{2,}(?=\\\()")
ALLOW_MIX = re.compile(r"^(\d+(st|nd|rd|th)|[A-Z]{1,4}\d{1,3}[A-Za-z]?|[a-z]\d|\d+[a-z]|[A-Z][a-z]?\d+|SHA\d+|UTF\d|ISO\d+|\d+D)$")


def prose(text):
    return ffs._mask_tex(text)


def vocab(paths):
    c = collections.Counter()
    for p in paths:
        try:
            c.update(w.lower() for w in WORD.findall(prose(Path(p).read_text(encoding="utf-8", errors="replace"))))
        except OSError:
            pass
    return c


PREFIX = re.compile(r"^(non|sub|un|re|counter|pseudo|over|under|multi|inter|intra|pre|post|de|dis|in|im|ir|il|mis|out|semi|self|super|anti|co|meta|hyper|quasi|trans|bi|tri|uni|poly|mono|auto|cross|extra|micro|macro|ultra|infra|proto|neo|pan)")
SUFFIX = re.compile(r"(ness|ment|ments|ability|ibility|ization|isation|ically|ing|ings|ed|er|ers|ly|less|ful|ship|wise|like|able|ible)$")


def split_two(tok, voc, strict=False):
    t = tok.lower()
    if strict and (PREFIX.match(t) or SUFFIX.search(t)):
        return None
    lo = 20 if strict else 5
    for i in range(2, len(t) - 1):
        a, b = t[:i], t[i:]
        if len(a) >= 2 and len(b) >= 2 and voc[a] >= lo and voc[b] >= lo:
            return a, b
    return None


def candidates(path, text, voc):
    masked = prose(text)
    lines = text.split("\n")
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln) + 1
    out = []

    def add(idx, cls, tok):
        line = max(i for i, s in enumerate(starts) if s <= idx)
        out.append({"path": path, "line": line + 1, "cls": cls, "token": tok, "context": lines[line].strip()[:200]})

    for m in WORD.finditer(masked):
        tok = m.group()
        if len(tok) >= 8 and voc[tok.lower()] <= 2 and split_two(tok, voc, strict=True):
            add(m.start(), "W", tok)
        elif re.fullmatch(r"[A-Z]{2,}[a-z]{3,}", tok) and voc[tok[len(re.match(r"[A-Z]+", tok).group()) - 0:].lower()] >= 5:
            add(m.start(), "A", tok)
    for m in MIX.finditer(masked):
        if not ALLOW_MIX.match(m.group()):
            add(m.start(), "N", m.group())
    for m in PUNCT.finditer(masked):
        add(m.start(), "P", masked[max(0, m.start() - 8):m.start() + 6])
    for m in GLUED_MATH.finditer(text):
        if masked[m.start():m.end()] == text[m.start():m.end()]:
            add(m.start(), "M", m.group())
    return out


def selftest():
    voc = collections.Counter({"separate": 29, "from": 50, "unheld": 6, "source": 40, "the": 99, "items": 30})
    assert split_two("separatefrom", voc) == ("separate", "from")
    c = candidates("x.tex", "We separatefrom it; selects8 items, students,12 and stage\\(n+1\\) CRAitems.\n", voc)
    kinds = {h["cls"] for h in c}
    assert {"W", "N", "P", "M", "A"} <= kinds, c
    assert not candidates("y.tex", "See \\cite[p.~97]{Rubinstein2015LectureNotes} and $x2$.\n", voc)
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit(0)
    files = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
    root = Path(__file__).resolve().parents[3]
    allfiles = [str(p) for p in (root / "handbook").rglob("*.tex") if "restoration" not in p.parts and "generated" not in p.parts]
    voc = vocab(allfiles)
    res = []
    for f in files:
        p = root / f
        if p.exists():
            res += candidates(f, p.read_text(encoding="utf-8", errors="replace"), voc)
    Path(sys.argv[2]).write_text(json.dumps(res, ensure_ascii=False, indent=0), encoding="utf-8", newline="\n")
    print(len(res), "candidates;", collections.Counter(h["cls"] for h in res))
