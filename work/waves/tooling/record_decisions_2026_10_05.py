"""Record the policy decisions of 2026-10-05. The user delegated them to the lead ("use your best
judgement"); each follows the governing requirement (the queue unit's required components, its
version requirement, and the integrity rules), never convenience. POL records in
spec/coverage/edition-2026/blockers.jsonl get state "decided" with the decision and its reason;
the published Opfer & Siegler chapter gets its own acquisition request. Idempotent."""
import json

E = "spec/coverage/edition-2026/"
WHEN = "2026-10-05T00:00:00Z"
BY = "lead, by user delegation in chat on 2026-10-05 ('use your best judgement'); the user may overturn"
DECISIONS = {
    "POL-2026-10-0001": (
        "Nothing beyond the required components of D-P3-004/D-P3-005. The parked note ('broader source/version, "
        "other-calculus or whole-facet allocation/admission is not inferred') records that a wider scope was not "
        "inferred; it is not a duty. 21.2 is assessed against those components only."),
    "POL-2026-10-0002": (
        "As POL-2026-10-0001: 21.3 owes exactly the required components of D-P3-004/D-P3-005."),
    "POL-2026-10-0003": (
        "(i) No original-source presentation is owed: the allocation lists only the handbook presentation D-P3-007; "
        "Pitts 1995 stays a citation. (ii) Signatures beyond the countable are not owed: every D-P3-007 component "
        "is required 'under the declared mathematical conventions', which fix a countable variable supply "
        "(sec:fol-semantics-02); 22.1 and 22.2 are complete on the same basis. 22.3 is assessed against D-P3-007."),
    "POL-2026-10-0004": (
        "No. The unit requires the published chapter (Oxford Handbook of Thinking and Reasoning, 2012, ch. 30, "
        "pp. 585-605); the held 2011 author draft is a different version, and a source-specific presentation may "
        "not be written from a different version. The published chapter must be acquired (ACQ-2026-10-0636); "
        "until then the source-specific items are blocked_source."),
    "POL-2026-10-0005": (
        "No, for the same reason as POL-2026-10-0004: the published chapter (ch. 28) is required "
        "(ACQ-2026-10-0354, needs a user-supplied file); the draft-relative gaps stay blocked_source."),
    "POL-2026-10-0006": (
        "164.6 owes what Logical Foundations of Probability (1950) develops, and an explicit statement that Carnap "
        "defers the quantitative-language confirmation function and the comparative vindication of c* to a planned "
        "second volume. Material the source does not contain cannot be presented from it."),
    "POL-2026-10-0007": (
        "164.6 owes the m*-limit results exactly as Carnap states them, under the monadic restriction of sec. 110 "
        "(pp. 566-567), and an explicit statement that the general relational case is not established by the "
        "source. No new result is owed: inventing one would break integrity rule A12."),
}

path = E + "blockers.jsonl"
lines = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
for rec in lines:
    if rec.get("id") in DECISIONS and rec.get("state") != "decided":
        rec.update(state="decided", decision=DECISIONS[rec["id"]], decided_by=BY, decided_utc=WHEN)
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    for rec in lines:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

acq = E + "acquisition-requests.jsonl"
rows = [json.loads(l) for l in open(acq, encoding="utf-8") if l.strip()]
if not any(r["acq_id"] == "ACQ-2026-10-0636" for r in rows):
    base = next(r for r in rows if r["acq_id"] == "ACQ-2026-10-0333")
    rows.append({"acq_id": "ACQ-2026-10-0636", "category": "D", "key": "OpferSiegler2012Published",
                 "census_verdict": "held_wrong_version", "units": base.get("units"), "sections": ["222.9"],
                 "work": "J. E. Opfer and R. S. Siegler, 'Development of Quantitative Thinking', in K. J. Holyoak and "
                         "R. G. Morrison (eds.), The Oxford Handbook of Thinking and Reasoning (Oxford University Press "
                         "2012), ch. 30, pp. 585-605",
                 "version": "Published 2012 chapter (the held ACQ-2026-10-0333 copy is the 2011 author draft)",
                 "extent": "pp. 585-605 (complete chapter)", "url": None, "host": None, "host_kind": None,
                 "version_match": None, "full_body": None, "size": None,
                 "verification_notes": "Raised by decision POL-2026-10-0004; the publisher copy is closed access.",
                 "state": "needs_user_supplied_file"})
    with open(acq, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print("ok")
