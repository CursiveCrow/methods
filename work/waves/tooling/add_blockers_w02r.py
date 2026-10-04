"""Record the w02r blocked_policy questions (blockers.jsonl) and the conditional Trakhtenbrot 1950
source (acquisition-requests.jsonl, for the next acquisition list). Idempotent by id."""
import json, os

E = "spec/coverage/edition-2026/"
UTC = "2026-10-04T00:00:00Z"
POL = [
    {"id": "POL-2026-10-0001", "kind": "blocked_policy", "sections": ["21.2"],
     "units": ["ED26-REQ-D-P3-004-01", "ED26-REQ-D-P3-005-01"],
     "question": "Section 21.2 (Craig interpolation) carries the parked scope note 'Broader source/version, other-calculus or whole-facet allocation/admission is not inferred.' The bounded classical first-order Craig treatment is complete at its hypotheses. Does 21.2 owe anything beyond the required components of D-P3-004/D-P3-005 (a named source version, other calculi, or whole-facet admission)? If so, which?",
     "raised_by": "CA-w02r-w02-p02-037-b0-21.2-first"},
    {"id": "POL-2026-10-0002", "kind": "blocked_policy", "sections": ["21.3"],
     "units": ["ED26-REQ-D-P3-004-01", "ED26-REQ-D-P3-005-01"],
     "question": "Section 21.3 (Beth definability / Robinson joint consistency) carries the same parked scope note as 21.2. The bounded Beth/Robinson treatment is complete at its hypotheses. Does 21.3 owe anything beyond the required components of D-P3-004/D-P3-005? If so, which?",
     "raised_by": "CA-w02r-w02-p02-037-b0-21.3-first"},
    {"id": "POL-2026-10-0003", "kind": "blocked_policy", "sections": ["22.3"],
     "units": ["ED26-REQ-D-P3-007-01"],
     "question": "Section 22.3 (empty sorts): (i) is any original-source presentation allocated to 22.3 (the allocation lists only the handbook presentation D-P3-007; the held Pitts 1995 draft, Example 2.3.2, is cited but not presented)? (ii) Are presentations beyond at-most-countable signatures owed (that would enlarge the governing countable variable supply of sec:fol-semantics-02)?",
     "raised_by": "CA-w02r-w02-p02-038-b0-22.3-first"},
]
ACQ = {"acq_id": "ACQ-2026-10-0615", "category": "D", "key": "Trakhtenbrot1950", "census_verdict": "not_held",
       "units": ["ED26-REQ-D-P4-010-01"], "sections": ["21.8"],
       "work": "B. A. Trakhtenbrot, 'The impossibility of an algorithm for the decision problem on finite classes', Doklady Akademii Nauk SSSR 70 (1950), 569-572",
       "version": "Original 1950 Doklady note", "extent": "pp. 569-572 (complete)",
       "url": None, "host": None, "host_kind": None, "version_match": None, "full_body": None, "size": None,
       "verification_notes": "Owed only if 21.8's 'finite-validity/decidability source developments' include Trakhtenbrot's original; the handbook's own proof is self-contained. Not yet searched.",
       "state": "unresolved"}

path = E + "blockers.jsonl"
have = set()
if os.path.isfile(path):
    have = {json.loads(l)["id"] for l in open(path, encoding="utf-8") if l.strip()}
with open(path, "a", encoding="utf-8", newline="\n") as f:
    for rec in POL:
        if rec["id"] not in have:
            f.write(json.dumps({**rec, "state": "awaiting_user_decision", "raised_utc": UTC}, ensure_ascii=False) + "\n")
acq = E + "acquisition-requests.jsonl"
ids = {json.loads(l)["acq_id"] for l in open(acq, encoding="utf-8") if l.strip()}
if ACQ["acq_id"] not in ids:
    with open(acq, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(ACQ, ensure_ascii=False) + "\n")
print("ok")
