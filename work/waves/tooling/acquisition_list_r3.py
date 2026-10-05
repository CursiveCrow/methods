"""Compile acquisition list r3 from work/waves/w02b/scout3/out-*.verified.jsonl (or out-*.jsonl when a
shard had no candidates) into the machine record and the list for the user's approval.

Each scouted request's state in spec/coverage/edition-2026/acquisition-requests.jsonl becomes
  candidate_verified        identity confirmed by the independent verifier (url, host, version
                            match and full-body evidence recorded),
  needs_user_supplied_file  no lawful free copy found,
  unresolved                a candidate whose identity the verifier rejected or left unresolved.
A corrected citation from the scout is kept in "identity_corrected". Requests are rewritten in place
(same order); nothing is downloaded. Writes work/waves/w02b/ACQUISITION-LIST-r3.md.
Usage: python -B work/waves/tooling/acquisition_list_r3.py"""
import glob
import json
import os

D = "work/waves/w02b/scout3"
REQ = "spec/coverage/edition-2026/acquisition-requests.jsonl"

scouted = {}
for path in sorted(glob.glob(f"{D}/out-*.jsonl")):
    if path.endswith(".verified.jsonl"):
        continue
    verified = path.replace(".jsonl", ".verified.jsonl")
    for line in open(verified if os.path.exists(verified) else path, encoding="utf-8"):
        if line.strip():
            rec = json.loads(line)
            scouted[rec["acq_id"]] = rec

rows = [json.loads(l) for l in open(REQ, encoding="utf-8") if l.strip()]
ready, differs, none, unresolved = [], [], [], []
for row in rows:
    rec = scouted.get(row["acq_id"])
    if rec is None or row.get("state") != "unresolved":
        continue
    if rec.get("identity_corrected") and rec["identity_corrected"] != "same":
        row["identity_corrected"] = rec["identity_corrected"]
    cand = rec.get("candidate") or {}
    ver = rec.get("verification") or {}
    if rec.get("state") == "candidate" and ver.get("identity") == "confirmed":
        row.update(state="candidate_verified", url=cand.get("url"), host=cand.get("host"),
                   host_kind=cand.get("host_kind"), size=cand.get("size"),
                   version_match=ver.get("version_match") or cand.get("version_match"),
                   full_body=ver.get("full_body") or cand.get("full_body"),
                   verification_notes=f"r3 scout + independent verification: {ver.get('notes', '')}".strip())
        (ready if row["version_match"] == "exact" and row["full_body"] == "yes" else differs).append(row)
    elif rec.get("state") == "candidate":
        row["verification_notes"] = f"r3 candidate {cand.get('url')} not confirmed: {ver.get('notes', '')}".strip()
        unresolved.append(row)
    else:
        row.update(state="needs_user_supplied_file",
                   verification_notes="r3 search found no lawful free copy; searched: " + "; ".join(rec.get("search_log") or [])[:600])
        none.append(row)
with open(REQ, "w", encoding="utf-8", newline="\n") as fh:
    for row in rows:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def cite(r):
    return (r.get("identity_corrected") or r["work"]).replace("|", "/")


def secs(r):
    return ", ".join(r.get("sections") or [])


lines = ["# Acquisition list r3 (2026-10-05)", "",
         "Sources the W2-a, W0 and W2-b assessments found missing. Each candidate was found by one agent and its identity "
         "checked by an independent one; nothing has been downloaded. Approve by ACQ id; each file is verified on arrival "
         "(identity, version, page sequence, hash).", ""]
if ready:
    lines += ["## Ready: identity confirmed, exact version, full body", "",
              "| ACQ | Work | Sections | URL | Host |", "|---|---|---|---|---|"]
    lines += [f"| {r['acq_id']} | {cite(r)} | {secs(r)} | {r['url']} | {r.get('host_kind') or r.get('host')} |" for r in ready]
    lines += [""]
if differs:
    lines += ["## Confirmed, but the version differs or the full body is unconfirmed (approve only if acceptable)", "",
              "| ACQ | Work | Sections | URL | Version match | Full body |", "|---|---|---|---|---|---|"]
    lines += [f"| {r['acq_id']} | {cite(r)} | {secs(r)} | {r['url']} | {r.get('version_match')} | {r.get('full_body')} |" for r in differs]
    lines += [""]
if none:
    lines += ["## No free copy found: needs a file from you", "",
              "Save the file into `source/references/acq-r3-<ACQ id>/` and tell me; it is then verified and its sections unblocked.", "",
              "| ACQ | Work | Sections |", "|---|---|---|"]
    lines += [f"| {r['acq_id']} | {cite(r)} | {secs(r)} |" for r in none]
    lines += [""]
if unresolved:
    lines += ["## Candidate not confirmed (stays unresolved)", "", "| ACQ | Work | Note |", "|---|---|---|"]
    lines += [f"| {r['acq_id']} | {cite(r)} | {r['verification_notes'][:200]} |" for r in unresolved]
    lines += [""]
open("work/waves/w02b/ACQUISITION-LIST-r3.md", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print(f"ready {len(ready)}, version differs {len(differs)}, needs user file {len(none)}, unresolved {len(unresolved)}; "
      f"scouted {len(scouted)}")
