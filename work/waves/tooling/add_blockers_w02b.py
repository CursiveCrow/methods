"""Records for W2-b post-routing blockers that had none: acquisition requests for sources the
w02br assessors found missing (for acquisition list r3) and two policy questions on 164.6.
Bibliographic details come from the assessors' duty texts and are to be verified when scouted.
Idempotent by id."""
import glob
import json
import os

E = "spec/coverage/edition-2026/"
UTC = "2026-10-05T00:00:00Z"
rows = {}
for f in glob.glob(E + "current-fulfillment/*.jsonl"):
    for line in open(f, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            rows[r["section_id"]] = r


def units(secs):
    return sorted({fc["unit_id"] for s in secs for fc in rows[s].get("source_facets") or []})


ACQ = [
    ("ACQ-2026-10-0625", "Carnap1945InductiveLogic", ["164.6"],
     "R. Carnap, 'On Inductive Logic', Philosophy of Science 12 (1945), pp. 72-97, section 15 (the variety-of-instances demonstration referred to in Logical Foundations of Probability sec. 110I)",
     "Original 1945 journal article", "section 15 (complete article preferred)"),
    ("ACQ-2026-10-0626", "Zabell2011CarnapPublisher", ["164.6"],
     "S. L. Zabell, 'Carnap and the Logic of Inductive Inference', in D. M. Gabbay, S. Hartmann and J. Woods (eds.), Handbook of the History of Logic vol. 10: Inductive Logic (Elsevier 2011), ch. 8, pp. 265-309",
     "Publisher 2011 version (the held copy carries a 2009 Elsevier footer)", "pp. 265-309 (complete chapter)"),
    ("ACQ-2026-10-0627", "HintikkaNiiniluoto1980", ["164.6"],
     "J. Hintikka and I. Niiniluoto, 'An axiomatic foundation for the logic of inductive generalization' (1976/1980 versions), characterization of the Hintikka-Niiniluoto systems cited by Zabell 2011",
     "Version cited by Zabell 2011", "complete paper"),
    ("ACQ-2026-10-0628", "Kuipers1978", ["164.6"],
     "T. A. F. Kuipers, Studies in Inductive Probability and Rational Expectation (Reidel 1978), the characterization cited by Zabell 2011",
     "Reidel 1978", "chapters containing the characterization theorem"),
    ("ACQ-2026-10-0629", "Zabell1996Confirming", ["164.6"],
     "S. L. Zabell, 'Confirming universal generalizations', Erkenntnis 45 (1996), the extended continuum of inductive methods",
     "Original 1996 article", "complete article"),
    ("ACQ-2026-10-0630", "Pitman1995Partitions", ["164.6"],
     "J. Pitman, 'Exchangeable and partially exchangeable random partitions', Probability Theory and Related Fields 102 (1995), the species-sampling characterization",
     "Original 1995 article", "complete article"),
    ("ACQ-2026-10-0631", "Zabell1997Continuum", ["164.6"],
     "S. L. Zabell, 'The continuum of inductive methods revisited', in J. Earman and J. D. Norton (eds.), The Cosmos of Science (1997), the three-parameter characterization",
     "Original 1997 chapter", "complete chapter"),
    ("ACQ-2026-10-0632", "DiaconisFreedman1980Finite", ["164.6"],
     "P. Diaconis and D. Freedman, 'Finite exchangeable sequences', Annals of Probability 8 (1980), the quantitative finite de Finetti approximation",
     "Original 1980 article", "complete article"),
    ("ACQ-2026-10-0633", "SanfilippoPfeiferGilio2017", ["165.2", "165.11"],
     "G. Sanfilippo, N. Pfeifer and A. Gilio, 'Generalized probabilistic modus ponens', ECSQARU 2017, LNCS 10369 (Springer 2017), pp. 480-490",
     "Springer LNCS 2017 version", "pp. 480-490 (complete paper)"),
    ("ACQ-2026-10-0634", "GilioSanfilippo2014", ["165.2", "165.11"],
     "A. Gilio and G. Sanfilippo, 'Conditional random quantities and compounds of conditionals', Studia Logica 102(4) (2014), pp. 709-729",
     "Original 2014 article", "pp. 709-729 (complete article)"),
    ("ACQ-2026-10-0635", "RubinStern1994", ["168.9", "168.10", "168.11"],
     "D. B. Rubin and H. S. Stern, 'Testing in latent class models using a posterior predictive check distribution', in A. von Eye and C. C. Clogg (eds.), Latent Variables Analysis: Applications for Developmental Research (Sage 1994), pp. 420-438",
     "Original 1994 chapter", "pp. 420-438 (complete chapter): the Dirichlet prior parameters and the mixture simulation"),
]
POL = [
    {"id": "POL-2026-10-0006", "kind": "blocked_policy", "sections": ["164.6"], "units": units(["164.6"]),
     "question": "Carnap 1950 (Logical Foundations of Probability) defers the quantitative-language confirmation function and the comparative vindication of c* to a planned second volume. Does section 164.6 (duty MP-0) owe these from the 1950 allocation, or only what the 1950 text itself develops?",
     "raised_by": "CA-w02br-w02b-p15-029-b0-164.6-first"},
    {"id": "POL-2026-10-0007", "kind": "blocked_policy", "sections": ["164.6"], "units": units(["164.6"]),
     "question": "Carnap 1950 asserts the existence and effective evaluation of m*-limits only under the monadic restriction of sec. 110 (pp. 566-567). Does 164.6 (MP-0) owe limit existence and effective evaluation for general sentences of the relational language L_infinity? That is an unproved step the source does not assert.",
     "raised_by": "CA-w02br-w02b-p15-029-b0-164.6-first"},
]

acq_path = E + "acquisition-requests.jsonl"
have = {json.loads(l)["acq_id"] for l in open(acq_path, encoding="utf-8") if l.strip()}
with open(acq_path, "a", encoding="utf-8", newline="\n") as fh:
    for acq, key, secs, work, version, extent in ACQ:
        if acq not in have:
            fh.write(json.dumps({"acq_id": acq, "category": "D", "key": key, "census_verdict": "not_held",
                                 "units": units(secs), "sections": secs, "work": work, "version": version,
                                 "extent": extent, "url": None, "host": None, "host_kind": None,
                                 "version_match": None, "full_body": None, "size": None,
                                 "verification_notes": "Raised by the W2-b post-routing re-assessment (w02br); bibliographic details from the assessor's text, to be verified when scouted.",
                                 "state": "unresolved"}, ensure_ascii=False) + "\n")
pol_path = E + "blockers.jsonl"
have = {json.loads(l)["id"] for l in open(pol_path, encoding="utf-8") if l.strip()} if os.path.isfile(pol_path) else set()
with open(pol_path, "a", encoding="utf-8", newline="\n") as fh:
    for rec in POL:
        if rec["id"] not in have:
            fh.write(json.dumps({**rec, "state": "awaiting_user_decision", "raised_utc": UTC}, ensure_ascii=False) + "\n")
print("ok")
