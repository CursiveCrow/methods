"""File browser downloads into source/references. The browser saves each PDF into ~/Downloads, first as
<uuid>.tmp and later renamed <ACQ-id>.pdf; files are matched to requests by exact size (recorded from
the in-page fetch) or by name, checked as complete PDFs (%PDF header, %%EOF in the last 2 KiB) and
copied to the request's folder. A Downloads file that has been renamed to its ACQ id is removed after
filing. Usage: python -B work/waves/tooling/file_downloads.py SIZES.json
SIZES.json: {"<size>": "ACQ-2026-10-NNNN", ...}"""
import glob, hashlib, json, os, shutil, sys

DL = os.path.expanduser("~/Downloads")
sizes = {int(k): v for k, v in json.load(open(sys.argv[1], encoding="utf-8")).items()}
folders = {r["acq"]: r["folder"] for r in json.load(open("tmp/user-downloads.json", encoding="utf-8"))}
for path in sorted(glob.glob(os.path.join(DL, "*.tmp")) + glob.glob(os.path.join(DL, "ACQ-2026-10-*.pdf"))):
    data = open(path, "rb").read()
    name = os.path.basename(path)
    acq = name[:16] if name.startswith("ACQ-2026-10-") else sizes.get(len(data))
    if not acq:
        continue
    if not (data[:5] == b"%PDF-" and b"%%EOF" in data[-2048:]):
        print("INCOMPLETE", acq, name, len(data)); continue
    dest = folders.get(acq) or f"source/references/acq-r3-{acq}/"
    os.makedirs(dest, exist_ok=True)
    target = os.path.join(dest, acq + ".pdf")
    if not os.path.isfile(target):
        shutil.copyfile(path, target)
        print("filed", acq, len(data), hashlib.sha256(data).hexdigest()[:12])
    if name.startswith("ACQ-2026-10-"):
        os.remove(path)
