"""File ScienceDirect PDFs from ~/Downloads (named 1-s2.0-<PII>-main*.pdf) into their request folders.
The PII comes from each request's ScienceDirect URL or Elsevier DOI (10.1016/<issn>(<yy>)<item> -> the
alphanumerics). Unmatched PDFs are listed, not moved. Usage: python -B work/waves/tooling/file_elsevier.py"""
import glob, hashlib, json, os, re, shutil

def pii_of(url):
    m = re.search(r"/pii/([A-Za-z0-9]+)", url)
    if m:
        return m.group(1).upper()
    m = re.search(r"10\.1016/([^/?#]+)", url)
    if m and not m.group(1).lower().startswith("j."):
        return re.sub(r"[^A-Za-z0-9]", "", m.group(1)).upper()
    return None

rows = json.load(open("tmp/user-downloads.json", encoding="utf-8"))
by_pii = {p: r for r in rows if (p := pii_of(r["url"]))}
for path in sorted(glob.glob(os.path.expanduser("~/Downloads/*.pdf"))):
    m = re.match(r"1-s2\.0-([A-Za-z0-9]+)-main", os.path.basename(path))
    r = by_pii.get(m.group(1).upper()) if m else None
    if not r:
        continue
    data = open(path, "rb").read()
    if not (data[:5] == b"%PDF-" and b"%%EOF" in data[-4096:]):
        print("INCOMPLETE", r["acq"], os.path.basename(path)); continue
    os.makedirs(r["folder"], exist_ok=True)
    target = os.path.join(r["folder"], r["acq"] + ".pdf")
    shutil.copyfile(path, target); os.remove(path)
    print("filed", r["acq"], len(data), hashlib.sha256(data).hexdigest()[:12])
need = [r["acq"] for r in rows if pii_of(r["url"]) or "sciencedirect" in r["url"]]
missing = [a for a in need if not any(f.endswith(".pdf") for f in os.listdir(next(x["folder"] for x in rows if x["acq"] == a)))] if need else []
print("Elsevier still missing:", len(missing), missing)
