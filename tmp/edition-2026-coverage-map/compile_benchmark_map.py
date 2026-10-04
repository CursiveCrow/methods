"""Compile explicit benchmark selections into finite coverage-map records."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "spec/coverage/edition-2026"

def rows(path):
    return [json.loads(s) for s in path.read_text(encoding="utf-8-sig").splitlines() if s.strip()]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def output(name, values):
    path = DEST / name
    if path.exists():
        raise SystemExit("Preserve prior projection: " + str(path))
    path.write_text("".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) + "\n" for x in values), encoding="utf-8")
    return {"path":path.relative_to(ROOT).as_posix(), "rows":len(values), "sha256":digest(path)}

with (DEST / "benchmark-contents-decisions.tsv").open(encoding="utf-8", newline="") as stream:
    contents = list(csv.DictReader(stream, delimiter="\t"))
with (DEST / "oxford-2012-component-selections.tsv").open(encoding="utf-8", newline="") as stream:
    oxford_components = {r["chapter"]:r for r in csv.DictReader(stream, delimiter="\t")}
if len(contents) != 106 or len(oxford_components) != 40:
    raise SystemExit(f"Incomplete declared contents: {len(contents)} rows, {len(oxford_components)} Oxford selections")

facts = {str(r["chapter"]):r for r in json.loads((DEST / "oxford-2012-publisher-identities.json").read_text(encoding="utf-8"))["chapters"]}
# This publisher search result was independently read after the first metadata
# compilation; the exact original URL and pagination are retained here.
facts["22"] = {"chapter":22, "title":oxford_components["22"]["reasoning_question"],
    "publisher_url":"https://academic.oup.com/edited-volume/34559/chapter-abstract/293250067",
    "doi":"10.1093/oxfordhb/9780199734689.013.0022", "pages":"433–455",
    "online_publication_date":"2012-11-21", "accessed_extent":"publisher identity and abstract", "body_read":False}
facts["19"]["pages"] = "364–389"  # Publisher page, directly read; metadata extractor missed a same-line marker.

known_urls = {"2":"293245943", "3":"293246043", "5":"293246351", "7":"293246715", "8":"293246950", "10":"293247461", "11":"293247631"}
current = rows(DEST / "current-reasoning-units.jsonl")
current_by_id = {r["unit_id"]:r for r in current}
original = rows(DEST / "requirements-units.jsonl")
original_titles = [(r["unit_id"], r["title"]) for r in original]

# These are explicit thematic comparisons, not new whole-source obligations.
# The exact selected keys prevent an indiscriminate all-P8 or all-P2 join.
thematic = {
 "3.1":{"original_pattern":r"propositional|first.order|natural deduction|sequent|completeness|substitution|Tseitin|Post"},
 "5.1":{"original_pattern":r"epistemic|doxastic|knowledge|belief logic"},
 "5.2":{"original_pattern":r"belief revision|AGM|revision.*belief"},
 "6.1":{"original_pattern":r"conditional logic|counterfactual|Lewis|Stalnaker", "current_stems":["finite-counterfactuals"]},
 "7.1":{"current_domains":["P16-C3","P16-C4","P16-C5"]},
 "8.1":{"current_stems":["finite-preferences","finite-expected-utility","finite-subjective-probability","maxmin-representation"]},
 "8.2":{"current_stems":["finite-expected-utility","finite-subjective-probability","risk-aversion","ambiguity-and-robust-choice"]},
 "11.1":{"original_pattern":r"deontic|contrary.to.duty|dyadic obligation"},
 "11.4":{"current_stems":["lis-and-burdens","prakken-sartor-is-1996","prakken-sartor-dynamic-priorities","prakken-sartor-dynamic-game-completeness"]}
}

units = []
crosswalk = []
for entry in contents:
    bm, number = entry["benchmark"], entry["row"]
    obligations = entry["assignment_or_family"].split(";")
    row = {"benchmark_id":bm, "contents_row":number, "source_title":entry["title"],
        "contents_start_page":int(entry["start_page"]) if entry["start_page"] else None,
        "source_end_page_inferred":False, "assigned_domains_or_families":obligations,
        "reasoned_scope_decision":entry["decision"], "unit_ids":[],
        "mapping_state":"resolved", "content_state":"missing", "evidence":["spec/coverage/edition-2026/benchmark-role-manifest.json"]}
    if bm == "RAT2021" and number in thematic:
        rule = thematic[number]
        selected = []
        if rule.get("original_pattern"):
            selected += [uid for uid,title in original_titles if re.search(rule["original_pattern"],title,re.I)]
        for unit in current:
            stem = Path(unit["destination"]["body"]["path"]).stem
            if stem in rule.get("current_stems",[]) or set(unit["initial_assignment_ids"]) & set(rule.get("current_domains",[])):
                selected.append(unit["unit_id"])
        row.update({"disposition":"thematic_comparison_to_required_treatments", "unit_ids":sorted(set(selected)),
            "content_state":"mixed", "comparison_required":True,
            "success_condition":"Compare the benchmark's stated reasoning question with these exact mandatory unit components and assumptions; retain every underlying unfulfilled source-specific obligation.",
            "failure_condition":"A related title alone is credited as the benchmark's complete source presentation or hides an unmet underlying requirement.",
            "source_body_obligation":"No new full-chapter reconstruction is added solely by this breadth comparison. Existing full-source obligations remain mandatory."})
        if not selected:
            row["mapping_state"] = "unresolved"
            row["unresolved_questions"] = ["Resolve exact existing unit destinations for this thematic comparison."]
        crosswalk.append(row)
        continue
    if bm == "RAT2021" and number == "9.2":
        row.update({"disposition":"existing_exact_source_treatment", "unit_ids":["ED26-P17-CH-epistemic-game-theory"],
            "content_state":"authored", "evidence":["spec/research/edition-2026-p17-epistemic-game-theory.md"]})
        crosswalk.append(row)
        continue
    uid = "ED26-BM-" + bm + "-" + number.replace(".", "-")
    if bm == "OHTR2012":
        selection = oxford_components[number]
        part = selection["part"].lower()
        stem = selection["proposed_stem"]
        question = selection["reasoning_question"]
        descriptions = [s.strip() for s in selection["selected_components"].split(";") if s.strip()]
        identity = facts[number] if number in facts else {"chapter":int(number), "publisher_url":"https://academic.oup.com/edited-volume/34559/chapter/" + known_urls[number],
            "pages":None, "doi":None, "accessed_extent":"Complete publisher contents and specific editorial scope decision; chapter metadata/body access still due", "body_read":False}
        identity["title"] = entry["title"]
        source = {"benchmark_id":bm, "title":entry["title"], "version":"Oxford University Press 2012 numbered chapter " + number,
            "extent":"Complete identified chapter body, figures, notes and references for the selected reasoning question; cited works become dependencies only for claims actually used.",
            "identity":identity}
    else:
        first = obligations[0]
        part = (first.split("-")[0] if first.startswith("P") else {"CF-01":"P19","CF-04":"P17","CF-06":"P11","CF-08":"P15","CF-12":"P18"}[first]).lower()
        stem = "rationality-" + number.replace(".", "-")
        question = entry["decision"]
        # These are finite editorial obligations for an exact complete chapter,
        # not claims that an unread body contains any particular theorem.
        descriptions = [entry["decision"],
            "Reconstruct the identified source's definitions, distinctions and complete argument or method for this question.",
            "Present its actual examples and the assumptions limiting its conclusions; distinguish normative, formal, historical and empirical claims.",
            "Compare the source-specific treatment with the linked handbook units, preserving material differences and objections.",
            "Account for every promised proof or evidence claim in the selected source extent; fix the finite dependent-source set before authoring those claims."]
        source = {"benchmark_id":bm, "title":entry["title"], "version":"MIT Press 2021 numbered chapter " + number,
            "extent":"Complete identified chapter, including its source-specific argument, examples, notes and references; references do not automatically add whole-book obligations.",
            "contents_start_page":row["contents_start_page"], "end_page":None,
            "evidence":"source/references/knauff-spohn-2021/toc-publisher.pdf",
            "publisher_url":"https://mitpress.mit.edu/9780262045070/the-handbook-of-rationality/"}
        if number == "intro":
            source["version"] = "MIT Press 2021 introductory framework, nine identified subsections"
            descriptions = json.loads((DEST / "benchmark-role-manifest.json").read_text(encoding="utf-8"))["benchmarks"][1]["introductory_subsections"]
        if number == "8.5":
            source.update({"local_path":"source/references/knauff-spohn-2021/s039900-mpg-copy.pdf", "printed_pages":"505-515",
                "source_sha256":"4311a58ad7062f1a763382fd3abfc0f9455fba6a8ee166e6bce420d2b298b70c"})
        if number == "2.1":
            stem = "reasons-and-rationality"
            part = "p11"
            source.update({"local_path":"source/references/knauff-spohn-2021/s006400-reasons-and-rationality.pdf", "printed_pages":"129-136",
                "source_sha256":"203eee694b54376e7ed1a6892623b4f461371e656ea7d3fbd1cc93445a944459",
                "author_note":"spec/research/edition-2026-p11-reasons-and-rationality.md"})
    dest = f"handbook/parts/{part}/{stem}.tex"
    empirical = part == "p19"
    kind = "empirical_treatment" if empirical else "philosophical_argument" if part == "p11" else "historical_treatment" if part == "p13" else "comparative_treatment"
    prerequisites = ["P19-E1 evidence design, uncertainty, corpus selection and generalization standards"] if empirical else []
    if any(x.startswith(("P15", "P16", "P17")) for x in obligations):
        prerequisites.append("P15-U1 probability assumptions used by this source; add only the actual dependent definitions/results")
    prerequisites += ["The exact existing component interfaces linked by the assigned domains; resolve these named interfaces to unit IDs during global prerequisite reconciliation"]
    components = [{"component_id":f"{uid}-C{i:02}", "description":description,
        "required_source_extent":source["extent"],
        "success_condition":"Supply this specified component under the source's actual assumptions, with explicit justification and a worked contrast or limitation; empirical claims retain study/task/population/uncertainty and conflict boundaries.",
        "failure_condition":"Omitted component, wrong source/version, unspecified assumptions, a descriptive finding promoted to a normative conclusion, or unsupported transfer between tasks or populations."}
        for i,description in enumerate(descriptions,1)]
    existing = bm == "RAT2021" and number == "2.1"
    unit = {"unit_id":uid, "kind":kind, "title":entry["title"], "reasoning_question":question,
        "original_requirement_ids":[], "inherited_source_ordinals":[], "source_presentations":[source],
        "required_components":components, "prerequisites":prerequisites,
        "destination":{"body":{"path":dest,"standing":"existing" if existing else "precise proposed destination; no empty manuscript file created"},
            "annex":{"path":f"handbook/annex/{part}/{stem}.tex","standing":"Create only for actual formal derivations required by the source treatment; otherwise justification is the body's full argument/evidence record"},
            "lookup":{"subject":entry["title"],"task":question,"success_and_failure_cases_required":True}},
        "content_state":"authored" if existing else "missing", "source_state":"identified_held" if source.get("local_path") else "identified_missing",
        "scope_state":"resolved", "scope_resolution_extent":"The exact chapter and finite editorial components are selected. Missing source acquisition, technical reading and writing remain work; no source findings are accepted from an abstract.",
        "evidence":row["evidence"] + ([source["identity"]["publisher_url"]] if bm == "OHTR2012" else [source["evidence"]]),
        "remaining_work":(["Check the existing treatment against its exact source components in the final consolidated review."] if existing else ["Obtain and read the exact full required chapter extent using free access.", "Freeze the claim-level dependent-source and empirical evidence set within the edition cutoff.", "Write all selected components and resolve actual prerequisite interfaces.", "Integrate its subject/task lookup cases, then perform consolidated reviews."]),
        "unresolved_questions":[], "global_overlap_and_prerequisite_reconciliation_pending":True}
    units.append(unit)
    row.update({"disposition":"existing_exact_source_treatment" if existing else "included_bounded_source_treatment",
        "unit_ids":[uid], "content_state":unit["content_state"], "required_component_ids":[c["component_id"] for c in components], "destination":dest})
    crosswalk.append(row)

if len({(r["benchmark_id"],r["contents_row"]) for r in crosswalk}) != 106:
    raise SystemExit("Duplicate or missing contents identity")
products = [output("benchmark-content-units.jsonl",units), output("benchmark-crosswalk.jsonl",crosswalk)]
receipt = {"purpose":"Coverage-map construction, not source-body acceptance or manuscript review",
    "outputs":products,"contents_rows":106,"rationality_numbered_chapters":65,"rationality_introductory_frameworks":1,
    "oxford_numbered_chapters":40,"new_or_separately_recorded_source_units":len(units),
    "components":sum(len(u["required_components"]) for u in units),
    "crosswalk_states":{state:sum(r["mapping_state"] == state for r in crosswalk) for state in ["resolved","unresolved"]},
    "unresolved_rows":[r for r in crosswalk if r["mapping_state"] == "unresolved"],
    "global_overlap_and_prerequisite_reconciliation_complete":False,"map_complete":False}
(DEST / "benchmark-map-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt,ensure_ascii=False))
