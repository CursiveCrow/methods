"""Assemble the authored TOC segments; no manuscript routing or scope changes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/"spec/toc-proposal"
files=["p01-p03.md","p04-p06.md","p07-p08.md","p09-p10-p12.md","p15-p17.md","p18-p19-p11.md","p13-p14-front-back.md"]
order=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P15","P16","P17","P18","P19","P11","P12","P13","P14"]
romans=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX"]
parts={}
pins=[]
cleanups={
    "Higher-kinded types and the mapped families of typed lambda calculi":"Higher-kinded types and families of typed lambda calculi",
    "Many-one, one-one and other mapped reducibilities":"Many-one, one-one and other reducibilities",
    "Algorithmic randomness and the mapped incompressibility connections":"Algorithmic randomness and incompressibility",
    "Concrete interpretations between mapped arithmetical theories":"Concrete interpretations between arithmetical theories",
    "Core-model constructions and the mapped toolbox":"Core-model constructions and methods",
    "Connections to the planning and decision theory of P17":"Planning and decision theory (Part XIII)",
    "Connections with the univalent foundations of P7":"Univalent foundations (Part VII)",
    "Bridges to P8 nonclassical systems and P9 probabilistic verification":"Nonclassical systems (Part VIII) and probabilistic verification (Part IX)",
    "Bridges to P12 finite-precision computation and simulation evidence":"Finite-precision computation and simulation evidence (Part XVII)",
    "Bridges to P16 causal identification and P19 empirical reasoning studies":"Causal identification (Part XII) and empirical reasoning studies (Part XV)",
    "Connections to P15 confirmation and P11 philosophy of logic":"Confirmation (Part XI) and philosophy of logic (Part XVI)",
    "Bridges to P8 conditional logics without conflating semantics":"Conditional-logic interpretations and their semantic differences (Part VIII)",
    "Bridges to P17 sequential decision problems":"Sequential decision problems (Part XIII)",
    "Source-specific knowledge-representation treatments and bridges to P9 action logics":"Knowledge representation and action logics (Part IX)",
    "Links to P15 subjective Bayesianism and updating":"Subjective Bayesianism and updating (Part XI)",
    "Links to P15 lower previsions and robustness":"Lower previsions and robustness (Part XI)",
    "Bridges to P19 empirical decision-making accounts":"Empirical accounts of decision making (Part XV)",
    "Bridges to P9 planning encodings and P12 search algorithms":"Planning encodings (Part IX) and search algorithms (Part XVII)"
}
for filename in files:
    path=HERE/filename
    raw=path.read_text(encoding="utf-8-sig")
    pins.append({"path":path.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    text=re.sub(r"<!--[\s\S]*?-->","",raw)
    current=None
    chapter=None
    for line_number,line in enumerate(text.splitlines(),1):
        h=re.match(r"^# (P\d+|FRONT|ANNEX|BACK)\s+[—–-]\s+(.+)$",line)
        if h:
            part_id,title=h.groups()
            if part_id in parts:raise SystemExit("Duplicate authored part "+part_id)
            current={"stable_part_id":part_id,"title":title,"chapters":[],"source_file":filename}
            parts[part_id]=current
            chapter=None
        elif line.startswith("### "):
            # An unnumbered integration note in a segment is not a book chapter.
            chapter=None
        elif line.startswith("## ") and current:
            chapter={"title":line[3:].strip(),"sections":[],"source_line":line_number}
            current["chapters"].append(chapter)
        elif line.startswith("- ") and chapter is not None:
            section=line[2:].strip()
            chapter["sections"].append(cleanups.get(section,section))
expected=set(order)|{"FRONT","ANNEX","BACK"}
assert set(parts)==expected,(set(parts)-expected,expected-set(parts))
for part in parts.values():
    assert part["chapters"],part["stable_part_id"]
    for ch in part["chapters"]:
        assert ch["sections"],ch["title"]
        assert not any(re.search(r"\b(?:TODO|TBD)\b",s) for s in [ch["title"]]+ch["sections"])

# This is a reader-facing title proposal, not a change to the stable ID/driver.
parts["P1"]["title"]="Foundations and Formal Methods"
chapter_number=0
section_count=0
for ordinal,part_id in enumerate(order,1):
    p=parts[part_id]
    p["printed_part_ordinal"]=ordinal
    p["printed_part_roman"]=romans[ordinal-1]
    for local,ch in enumerate(p["chapters"],1):
        chapter_number+=1
        ch["number"]=chapter_number
        ch["part_local_number"]=local
        ch["numbered_sections"]=[{"number":f"{chapter_number}.{i}","title":s} for i,s in enumerate(ch["sections"],1)]
        section_count+=len(ch["sections"])

lead=["# The Methods of Reason","","## Proposed Complete Table of Contents","",
"**A Reference Handbook of Logic and Reasoning**","",
f"This proposal contains nineteen parts, {chapter_number} numbered chapters and {section_count:,} main sections, followed by the extended proof annex, bibliography and indexes. It follows the completed edition coverage map and the seventeen additional source treatments selected during gap analysis.","",
"The numbering describes the proposed book. It does not claim that these chapters are already written or that the manuscript has been reorganized. Page numbers will be assigned after composition. Individual definitions, rules, theorems, examples and source-specific proof steps sit within the listed sections rather than appearing as separate TOC lines.","",
"The contents are organized for consultation by logical system, subject and reasoning task. Distinct source presentations retain their own treatments where their definitions, hypotheses, methods or conclusions differ.","",
"[Chapter-only contents](C:/Dev/the-methods-of-reason/spec/PROPOSED-TABLE-OF-CONTENTS-CHAPTERS.md) · [Editorial placement notes](C:/Dev/the-methods-of-reason/spec/PROPOSED-TABLE-OF-CONTENTS-NOTES.md)","",
"## Front Matter",""]
full=list(lead)
compact=["# The Methods of Reason","","## Proposed Table of Contents — Parts and Chapters","",
f"Nineteen parts; {chapter_number} chapters. The [full contents](C:/Dev/the-methods-of-reason/spec/PROPOSED-TABLE-OF-CONTENTS.md) include all {section_count:,} main section headings. This is the proposed complete structure, without provisional page numbers.","",
"## Front Matter",""]
for ch in parts["FRONT"]["chapters"]:
    full += ["### "+ch["title"],""]+["- "+s for s in ch["sections"]]+[""]
    compact += ["- "+ch["title"]]
compact.append("")
summary=[]
for part_id,roman in zip(order,romans):
    p=parts[part_id]
    heading=f"## Part {roman} — {p['title']}"
    full += [heading,""]
    compact += [heading,""]
    for ch in p["chapters"]:
        full += [f"### {ch['number']}. {ch['title']}",""]
        full += [f"- {s['number']} {s['title']}" for s in ch["numbered_sections"]]+[""]
        compact.append(f"{ch['number']}. {ch['title']}")
    compact.append("")
    summary.append({"stable_part_id":part_id,"printed_part":roman,"title":p["title"],"chapters":len(p["chapters"]),"main_sections":sum(len(ch["sections"]) for ch in p["chapters"]),"first_chapter":p["chapters"][0]["number"],"last_chapter":p["chapters"][-1]["number"]})
full += ["## Extended Proofs and Derivations",""]
compact += ["## Extended Proofs and Derivations",""]
for i,ch in enumerate(parts["ANNEX"]["chapters"],1):
    full += [f"### P.{i} {ch['title']}",""]+["- "+s for s in ch["sections"]]+[""]
    compact.append(f"- P.{i} {ch['title']}")
compact.append("")
full += ["## Bibliography and Indexes",""]
compact += ["## Bibliography and Indexes",""]
for ch in parts["BACK"]["chapters"]:
    full += ["### "+ch["title"],""]+["- "+s for s in ch["sections"]]+[""]
    compact += ["### "+ch["title"],""]+["- "+s for s in ch["sections"]]+[""]

notes=["# Editorial Notes to the Proposed Table of Contents","",
"This document records the organization proposed in response to the user's request for a complete table of contents. It does not change manuscript drivers, source-unit identities, proof requirements, source records or completed-coverage flags.","",
"## Level and numbering","",
f"The proposal includes {chapter_number} chapters and {section_count:,} named main sections. Chapters are numbered consecutively through the nineteen parts. The proof annex uses its own P.1–P.{len(parts['ANNEX']['chapters'])} navigation labels. These are proposal labels, not a rewrite of existing LaTeX identifiers.","",
"The main section hierarchy is the complete proposed reader outline at that level. It is not a line-by-line index of the21,367 mapped content components. Full source treatments, distinct versions, proof branches and examples remain within these headings at their required scope.","",
"## Stable part and chapter allocation","","| Printed part | Stable ID | Chapters | Main sections | Chapter range |","| --- | --- | ---: | ---: | --- |"]
for p in summary:
    notes.append(f"| {p['printed_part']} | {p['stable_part_id']} | {p['chapters']} | {p['main_sections']} | {p['first_chapter']}–{p['last_chapter']} |")
notes += ["","P1's proposed display title is Foundations and Formal Methods. The P11, P13 and P14 display titles make their fuller mapped subject content visible. The stable nineteen-part order is retained, including P15–P19 before P11–P14.","",
"## Primary homes and explicit bridges","",
"- P2 provides elementary/classical systems; P3 develops model-theoretic methods; P9 owns computational specification, logic/automata translations, queries and verification procedures.",
"- P4 provides computation, reductions and complexity; P5 covers arithmetic theories and their consequences; P7 owns the principal proof transformations, interpretations and type-theoretic foundations.",
"- P7 houses full lambda/type/HoTT/cubical foundations and diagrammatic proof calculi. P10 provides algebraic, categorical, domain and quantum-structure semantics. P12 covers implementation, proof checking and mechanization.",
"- P8 houses formal nonclassical systems and formal reference/discourse semantics. P11 develops their philosophical questions; P18 develops argument, dialogue and question-inference methods.",
"- P15 provides uncertainty and statistical inference. P16 provides explanation and causal methods. P17 owns decision, planning, task networks, strategic reasoning and aggregation. P19 covers the selected empirical studies of reasoning.",
"- P13 preserves the full selected historical treatments and biographical reference. Historical chapters retain their distinctive source arguments; their modern technical results link to the appropriate subject chapters.","",
"## Legacy proposed-path discrepancies","",
"The TOC work found several source-shard paths left over from a different part-number scheme. For example, source001 model theory points to p04, set theory to p05 and recursion theory to p06. Some source001 proof-theory/incompleteness entries point to p03, while source055 Agda and source056 HoTT point to p04. The proposed reader organization uses the governing subject identities: model theory P3; computability P4; arithmetic P5; set theory P6; proof and type theory P7; categorical logic P10; proof-assistant practice P12.","",
"These are recorded routing corrections for the proposal. No manuscript files have been moved, and this TOC does not establish that every old proposed path is an implemented destination. The detailed source-unit corrections in toc-proposal/p01-p03-coverage.md and the segment integration notes remain available for the later routing pass.","",
"## Scope preservation","",
"All seventeen newly selected reasoning treatments have explicit homes. Existing diagrammatic logic, constraints, planning, argument appraisal, historical logic and empirical reasoning retain their mapped scope. General design/prototyping subjects excluded during the scope correction are not introduced as new chapters. Front matter contains reader guidance and notation, without the retired graduate-level framing or duplicated Formal Logic title.","",
"No chapter title grants permission to collapse materially different calculi, source editions or proof regimes. The scope map, source allocations and completion queue remain the authority for the exact content within each heading.","",
"## Construction evidence","",
"The assembly reads only the seven authored TOC segment files. Its structural check requires all nineteen stable parts once, all front/back groups, nonempty sections for each chapter, and no TODO/TBD placeholders. It assigns consecutive numbers and records input hashes. No manuscript build, PDF rendering or independent proof review forms part of this TOC task.",""]
notes=[s.replace("the21,367","the 21,367") for s in notes]
outputs={"spec/PROPOSED-TABLE-OF-CONTENTS.md":full,"spec/PROPOSED-TABLE-OF-CONTENTS-CHAPTERS.md":compact,"spec/PROPOSED-TABLE-OF-CONTENTS-NOTES.md":notes}
for path,lines in outputs.items():
    (ROOT/path).write_text("\n".join(lines),encoding="utf-8")
structured={"status":"proposed_reader_organization","date":"2026-09-09","book_title":"The Methods of Reason","subtitle":"A Reference Handbook of Logic and Reasoning","input_files":pins,"main_part_order":order,"parts":[parts[p] for p in order],"frontmatter":parts["FRONT"],"proof_annex":parts["ANNEX"],"backmatter":parts["BACK"],"summary":summary,"chapters":chapter_number,"main_sections":section_count,"manuscript_reorganization_performed":False,"individual_source_components_retained_by_scope_map":True}
(ROOT/"spec/proposed-table-of-contents.json").write_text(json.dumps(structured,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
receipt={"created_utc":datetime.now(timezone.utc).isoformat(),"chapters":chapter_number,"main_sections":section_count,"main_parts":len(order),"parts":summary,"inputs":pins,"outputs":[{"path":p,"sha256":hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in list(outputs)+["spec/proposed-table-of-contents.json"]],"checks":{"nineteen_parts_once":True,"all_chapters_have_main_sections":True,"consecutive_chapter_and_section_numbers":True,"no_todo_placeholders":True},"scope":"Proposed table of contents; no current manuscript or coverage-map mutation"}
(HERE/"assembly-receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"chapters":chapter_number,"main_sections":section_count,"parts":summary,"outputs":list(outputs)},ensure_ascii=False))
