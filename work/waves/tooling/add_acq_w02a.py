"""Acquisition records for W2-a source blockers that had no record of their own (for list r3).
Idempotent by acq_id."""
import glob, json

E = "spec/coverage/edition-2026/"
rows = {}
for f in glob.glob(E + "current-fulfillment/*.jsonl"):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            rows[r["section_id"]] = r
units = lambda secs: sorted({fc["unit_id"] for s in secs for fc in rows[s].get("source_facets") or []})  # noqa: E731
NEW = [
    ("ACQ-2026-10-0616", "HalpernLevy1971", ["3.7", "3.8"],
     "J. D. Halpern and A. Levy, 'The Boolean prime ideal theorem does not imply the axiom of choice', in Axiomatic Set Theory, Proc. Symp. Pure Math. 13 Part I (AMS 1971), pp. 83-134",
     "Published proceedings version", "pp. 83-134 (complete)"),
    ("ACQ-2026-10-0617", "Skura2011", ["13.6", "13.7"],
     "T. Skura, 'Refutation systems in propositional logic', Handbook of Philosophical Logic 2nd ed., vol. 16 (Springer 2011), pp. 115-157, DOI 10.1007/978-94-007-0479-4_2",
     "Springer 2011 chapter", "pp. 115-157 (complete chapter)"),
    ("ACQ-2026-10-0618", "Mendelson1997", ["17.4"],
     "E. Mendelson, Introduction to Mathematical Logic, 4th ed. (Chapman & Hall 1997), chapter 2 (first-order theories, axioms A1-A5, Gen, deduction theorem)",
     "4th edition (1997)", "chapter 2 (first-order theories through the deduction theorem)"),
    ("ACQ-2026-10-0619", "BaazEglyLeitsch2001", ["18.6"],
     "M. Baaz, U. Egly and A. Leitsch, 'Normal form transformations', in A. Robinson and A. Voronkov (eds.), Handbook of Automated Reasoning vol. 1 (Elsevier 2001), pp. 273-333, DOI 10.1016/B978-044450813-3/50007-2",
     "Elsevier 2001 chapter", "pp. 273-333 (complete chapter)"),
]
path = E + "acquisition-requests.jsonl"
have = {json.loads(l)["acq_id"] for l in open(path, encoding="utf-8") if l.strip()}
with open(path, "a", encoding="utf-8", newline="\n") as fh:
    for acq, key, secs, work, version, extent in NEW:
        if acq in have:
            continue
        fh.write(json.dumps({"acq_id": acq, "category": "D", "key": key, "census_verdict": "not_held",
                             "units": units(secs), "sections": secs, "work": work, "version": version,
                             "extent": extent, "url": None, "host": None, "host_kind": None,
                             "version_match": None, "full_body": None, "size": None,
                             "verification_notes": "Raised by W2-a assessments; not yet searched.",
                             "state": "unresolved"}, ensure_ascii=False) + "\n")
print("ok")
