export const meta = {
  name: 'tmor-backlog-integrate',
  description: 'W0: readiness of saved/off-route backlog drafts (returns for collect), decisions for routed-group adoption, unclassified off-route files',
  phases: [
    { title: 'Readiness', detail: 'Opus checks each off-route draft and writes a collect-ready return', model: 'opus' },
    { title: 'Fix', detail: 'Opus fixes mechanical defects in its own draft files', model: 'opus' },
    { title: 'Decisions', detail: 'Opus drafts the adoption decisions JSON for routed groups', model: 'opus' },
    { title: 'Classify', detail: 'Opus classifies unclassified off-route files', model: 'opus' },
  ],
}
// args: {items:[{stem, part, bodies:[...], annexes:[...], symbol_intakes:[...], bibliography_intakes:[...], note, origin}],
//        decisions_manifest, unclassified:[paths], maxConcurrent}
const LIMIT = Math.min(12, args.maxConcurrent || 10)
let active = 0; const waiters = []
const acquire = () => active < LIMIT ? (active++, Promise.resolve()) : new Promise(r => waiters.push(r))
const release = () => { const n = waiters.shift(); if (n) n(); else active-- }
const run = async (p, o) => { await acquire(); try { return await agent(p, o) } finally { release() } }
const ROOT = 'C:/Dev/the-methods-of-reason'
const RULES = `Repository ${ROOT} (Windows; Git Bash; TeX Live 2025 via tools/texlive.latexmkrc or C:/texlive/2025/bin/windows). Other agents work concurrently on other backlog items: touch ONLY the files of your item (its bodies, annexes, intakes, note) and the return file named below. Never edit drivers (handbook/main.tex, handbook/parts/pNN.tex, handbook/annex/pNN*.tex), handbook/bib/handbook.bib, handbook/registry/symbols.csv or symbol-scopes.json, generated/, restoration/, tools/. No git write commands. Never change mathematics or claims; fixes are mechanical (labels, backlinks, cite keys present in the intake, TeX syntax, fused spaces, missing intake rows). Hintikka (p15-hintikka) and Abelian (p10-abelian) are excluded by user decision and must not be touched.`
const READY = { type: 'object', properties: {
  stem: { type: 'string' }, verdict: { type: 'string', enum: ['route', 'fix', 'continue_authoring', 'duplicate', 'exclude'] },
  reason: { type: 'string' }, return_path: { type: 'string' }, defects: { type: 'array', items: { type: 'string' } },
  sections_served: { type: 'array', items: { type: 'string' } },
}, required: ['stem', 'verdict', 'reason', 'defects', 'sections_served'] }

function readinessPrompt(it) {
  return `${RULES}
TASK: readiness check for backlog item ${it.stem} (part ${it.part}; origin ${it.origin}). Files: bodies ${JSON.stringify(it.bodies)}, annexes ${JSON.stringify(it.annexes)}, symbol intakes ${JSON.stringify(it.symbol_intakes || [])}, bibliography intakes ${JSON.stringify(it.bibliography_intakes || [])}, note ${it.note || 'none'}.
1. Read the files in full. Determine which planned sections (spec/proposed-table-of-contents.json ids like "52.8") the treatment serves, from the note, %% toc tags and content.
2. Check for overlap with text already on the route (grep labels/titles; a draft that duplicates routed material is "duplicate").
3. Mechanical checks: every body result's proved=annex:<id> has a matching annexitem backlink and vice versa; labels unique across handbook/ (python -B tools/check.py --tree handbook, filtered to these files); every \\cite key exists in handbook/bib/handbook.bib or the item's intake bib; python -B tools/find_fused_spaces.py <files> clean; no \\newcommand/\\def; balanced environments; unit compile: build a scratch driver under tmp/backlog-builds/${it.stem}/ (book class, \\usepackage{handbook}, biblatex with bib/handbook.bib plus the intake bib, \\input{bib/inherited-keys}, \\setcounter{part}{<printed ordinal-1>}, \\hbpartidentity{<pNN>}\\part{x}, a \\chapter/\\section wrapper matching the body's first heading level, \\input{<body>}, \\hbannexsetup, \\hbannexchapter{<n>}{x}, \\input{<annex>}, \\hbannexfinish, \\printbibliography) and compile from handbook/ with C:/texlive/2025/bin/windows/pdflatex.exe -no-shell-escape -interaction=nonstopmode -output-directory=<abs tmp dir> plus biber and two more passes. Printed ordinals: p01-p10 = 1-10, p15-p19 = 11-15, p11-p14 = 16-19.
4. Verdict: "route" if clean (or clean after trivial fixes you make in this step within the item's own files), "fix" if mechanical defects remain that need more work, "continue_authoring" if the draft is visibly unfinished (stubs, missing promised proofs, truncated), "duplicate" if it duplicates routed text, "exclude" only for Hintikka/Abelian.
5. For "route" (and "fix" after you fixed it), write the return file spec/research/edition-2026-${it.stem}-return.json for tools/integrate_wave.py collect: {"stem":"${it.stem}","part":"${it.part}","bodies":[...],"annexes":[...],"symbol_intakes":[...],"bibliography_intakes":[...],"note":"<note path>","label_tag":"<dominant label prefix>","placement":{"body":{"host":"<the part's route host file>","after_input":"<existing \\input path in that host after which to insert, at the planned contents position>"},"annex":{"host":"<annex route host>","after_input":"<...>"}},"proposed_decisions":{}}. Choose the route host and anchor from the item's note (recommended seam) and the planned contents order; for P13 bodies are under parts/p13/presentations/ and annex files are flat annex/p13/<slug>.tex; annex/p01.tex, annex/p05.tex, annex/p06.tex are not on route (use annex/p01-route.tex, p05-route.tex, p06-route.tex). Never choose an anchor inside an \\AddToHook ... \\RemoveFromHook bracket.
Return the structured verdict.`
}

const out = { readiness: [], decisions: null, classify: null }
phase('Readiness')
const ready = await pipeline(args.items,
  it => run(readinessPrompt(it), { model: 'opus', effort: 'high', schema: READY, label: `ready:${it.stem}`, phase: 'Readiness' }),
  (r, it) => (r && r.verdict === 'fix') ? run(`${RULES}
TASK: fix the remaining mechanical defects of backlog item ${it.stem} within its own files: ${JSON.stringify(r.defects)}. Then rerun the checks from the readiness step (backlinks, labels, cite keys, fused spaces, unit compile under tmp/backlog-builds/${it.stem}/) and, if clean, write/update the return file spec/research/edition-2026-${it.stem}-return.json (same format as the readiness instructions: stem, part, bodies, annexes, intakes, note, label_tag, placement {body:{host, after_input}, annex:{host, after_input}}, proposed_decisions). Return the structured verdict (route if now clean).`,
    { model: 'opus', effort: 'high', schema: READY, label: `fix:${it.stem}`, phase: 'Fix' }) : r)
out.readiness = ready.filter(Boolean)

phase('Decisions')
if (args.decisions_manifest) {
  out.decisions = await run(`${RULES}
TASK: draft the adoption decisions for the routed backlog groups. Run \`python -B tools/integrate_wave.py adopt --manifest ${args.decisions_manifest} --decisions <a temp file containing {}>\` (dry run) and read every decision-needed item. Write work/waves/w00/decisions-backlog-a.json in the decisions schema the tool documents (overrides, row_edits, drop_rows, canonical_row_edits, extend_scopes, citation_aliases, bib_keep_canonical). Use these user-approved defaults for the six glyph overlaps: (1) \\leq Gitik native order vs canonical ordering: typed override on the Gitik comparison scope, broader_scope = the canonical row's current (migrated) scope, source = the Gitik bib key; (2) \\mu PCF binder vs the P10 monolith row: narrow the canonical monolith row to its declaring subsection (canonical_row_edits); (3) P turtle position vs production set in p09 development: narrow each row to the heading of its own first use, typed override only if both are declared in the same region; (4) dQ erotetic search vs question evocation: drop the incoming row and reuse the generalized def:p18-ei-setting row; (5) \\$ two roles in p09 recombination iteration: typed override in the same region (source = the HFL/Paun key); (6) \\to PCF arrow type vs operational step: typed override in the same region (source = the Gunter key). For foreign annex items use extend_scopes; for duplicate works and key conflicts prefer citation_aliases to the existing canonical key when the records are the same work and version, otherwise keep both keys with distinct identities (bib_keep_canonical as needed) and explain. Every override needs source and reason. Rerun the dry run with your file until it reports 0 errors and 0 decisions needed (do NOT pass --apply). Return a short report: decisions made, remaining issues.`,
    { model: 'opus', effort: 'high', label: 'decisions:backlog-a', phase: 'Decisions' })
}

phase('Classify')
if (args.unclassified && args.unclassified.length) {
  out.classify = await run(`${RULES}
TASK: classify each of these off-route handbook files: ${JSON.stringify(args.unclassified)}. For each: is it reachable from handbook/main.tex? which planned sections does it serve? does routed text already supersede it? Is it referenced by a tool (grep tools/)? Verdict per file: route (ready content, give host and after_input), keep (retained evidence or tool-referenced; leave in place), propose_retire (superseded duplicate; the user decides), continue_authoring. Do not move or edit any file. Write work/waves/w00/unclassified-offroute.json with {path, verdict, reason, sections, placement?}. Return a short summary.`,
    { model: 'opus', effort: 'high', label: 'classify:offroute', phase: 'Classify' })
}
return out
