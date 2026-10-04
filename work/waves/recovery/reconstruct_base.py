"""Rebuild a wave's lost base commit for the guarded trees (handbook, spec/research, spec/coverage)
from its packet snapshots, without touching the working tree.

Every W2-b snapshot records the base `tree` (path -> size, mtime, sha256) and the base text of each
editable host. Starting from HEAD's tree, files absent from the base tree are dropped and files
whose content differs are restored from the recorded host text. Every guarded path of the result
is then checked against the recorded sha256 (LFS pointers by their oid). Paths outside the guarded
trees keep HEAD's content.

Usage: python -B work/waves/recovery/reconstruct_base.py WAVE TAG
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

ROOT = "C:/Dev/the-methods-of-reason"
GUARDED = ("handbook/", "spec/research/", "spec/coverage/")


def git(*args, inp=None, env=None):
    return subprocess.run(["git", "-C", ROOT, *args], input=inp, capture_output=True, check=True, env=env).stdout


def main() -> int:
    wave, tag = sys.argv[1], sys.argv[2]
    os.chdir(ROOT)
    tree, texts = None, {}
    for f in sorted(glob.glob(f"work/waves/{wave}/snapshots/{wave}-*.json")):
        d = json.load(open(f, encoding="utf-8"))
        if tree is None:
            tree = d["tree"]
        elif d["tree"] != tree:
            raise SystemExit(f"snapshot trees differ: {f}")
        for p, t in (d.get("editable_host_text") or {}).items():
            texts[p] = t
    env = {**os.environ, "GIT_INDEX_FILE": os.path.join(ROOT, "tmp", f"{wave}-base.index")}
    git("read-tree", "HEAD", env=env)
    listed = {}
    for line in git("ls-files", "-s", "--", *GUARDED, env=env).decode("utf-8").splitlines():
        meta, path = line.split("\t", 1)
        listed[path] = meta.split()[1]
    dropped = [p for p in listed if p not in tree]
    for i in range(0, len(dropped), 200):
        git("rm", "--cached", "-q", "--", *dropped[i:i + 200], env=env)
    # build products and other ignored files in the guarded trees were never committed
    unlisted = "\n".join(p for p in tree if p not in listed).encode("utf-8")
    ignored = set(subprocess.run(["git", "-C", ROOT, "check-ignore", "--stdin"], input=unlisted,
                                 capture_output=True).stdout.decode("utf-8").splitlines())
    restored, missing = [], []
    for path, meta in tree.items():
        if path in ignored:
            continue
        blob = listed.get(path)
        content = git("cat-file", "blob", blob) if blob else None
        if content is not None and content.startswith(b"version https://git-lfs"):
            oid = next(l.split(":", 1)[1] for l in content.decode().splitlines() if l.startswith("oid sha256:"))
            if oid == meta["sha256"]:
                continue
        elif content is not None and hashlib.sha256(content).hexdigest() == meta["sha256"]:
            continue
        if path not in texts:
            missing.append(path)
            continue
        data = texts[path].encode("utf-8")
        if hashlib.sha256(data).hexdigest() != meta["sha256"]:
            raise SystemExit(f"recorded host text does not match base hash: {path}")
        sha = git("hash-object", "-w", "--stdin", inp=data).decode().strip()
        git("update-index", "--add", "--cacheinfo", f"100644,{sha},{path}", env=env)
        restored.append(path)
    if missing:
        raise SystemExit(f"base content not recoverable for {len(missing)} paths, e.g. {missing[:5]}")
    tree_sha = git("write-tree", env=env).decode().strip()
    msg = (f"{wave}: reconstructed base tree for handbook/, spec/research/, spec/coverage/\n\n"
           f"Rebuilt from the {wave} packet snapshots after the original repository was lost:\n"
           f"{len(dropped)} files added during the run dropped, {len(restored)} editable hosts restored\n"
           f"from their recorded base text; every guarded path matches the snapshot sha256.\n")
    commit = git("commit-tree", tree_sha, "-p", "HEAD", "-m", msg).decode().strip()
    git("tag", "-f", tag, commit)
    print(json.dumps({"commit": commit, "dropped": len(dropped), "restored": restored}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
