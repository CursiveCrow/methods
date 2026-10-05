export const meta = {
  name: 'tmor-wave-integrate',
  description: 'Wave-end lead integration: per-host and per-capture patch application, lead tool/style/frontmatter requests, intake adoption decisions',
  whenToUse: 'After collect + route of a wave; args name the grouped patch files (work/waves/<wave>/host-patches, lead/ request files)',
  phases: [
    { title: 'Hosts', detail: 'Opus applies verified author patch requests, one agent per handbook host', model: 'opus' },
    { title: 'Captures', detail: 'Opus applies correction requests to restoration captures (v4 records written by the lead afterwards)', model: 'opus' },
    { title: 'Lead', detail: 'Opus implements requested tool, stylesheet and frontmatter changes', model: 'opus' },
    { title: 'Adopt', detail: 'Opus repairs intakes and drafts adoption decisions (incl. canonical registry edits) to a clean dry run', model: 'opus' },
  ],
}

// args: {wave, hosts:[{host,file}], captures:[{host,file,pid,schema}], tools?:{file}, sty?:{file},
//        frontmatter?:{file}, adopt?:{manifest, decisions, registry_file?}}
const CAP = 10
let active = 0; const waiters = []
const acquire = () => active < CAP ? (active++, Promise.resolve()) : new Promise(r => waiters.push(r))
const release = () => { const n = waiters.shift(); if (n) n(); else active-- }
const run = async (p, o) => { await acquire(); try { return await agent(p, o) } finally { release() } }
const W = `work/waves/${args.wave}`
const slug = h => h.replace(/[\\/]/g, '__')
const COMMON = `Repository C:/Dev/the-methods-of-reason (Windows; Git Bash; TeX Live 2025 at C:/texlive/2025/bin/windows; never MiKTeX). Lead integration of authoring wave ${args.wave}. Other agents edit OTHER files concurrently: edit only the file(s) this task names. No git write commands; never build handbook/main.tex. Never change mathematics or claims beyond what a request explicitly specifies and justifies.`
const JUDGE = `For each request: (1) locate its anchor quote exactly once in the current file (if absent or ambiguous, look for the same passage after earlier edits; skip only if it is truly gone, with the reason); (2) judge whether the change is a correct, minimal, consistent edit (cross-reference, link, short added sentence, label alignment, corrected statement the request justifies with a source or a proof on the route); skip requests that duplicate content already present, conflict with another applied request, introduce workflow language (review, ledger, assessor, author, wave, packet, intake) into reader text, add proof environments to a parts/ body file, use undefined labels or bib keys, or change mathematics without justification; when two requests touch the same passage, merge them into one coherent edit; (3) apply in order with minimal edits, preserving the file's line endings; (4) record each decision. A request whose "Apply only after" condition names files that are now routed (grep the drivers) is applicable.`
const HOST = { type: 'object', properties: { host: { type: 'string' }, applied: { type: 'integer' }, skipped: { type: 'integer' },
  skipped_reasons: { type: 'array', items: { type: 'string' } } }, required: ['host', 'applied', 'skipped'] }

const hostJobs = (args.hosts || []).map(h => () => run(`${COMMON}
TASK: apply the author patch requests for ONE handbook host: ${h.host}. Requests: ${h.file} (items: patch_file, index, request {host, anchor_quote or anchor, operation insert_after|replace, text, reason}). You own ONLY ${h.host}.
${JUDGE}
After applying, run python -B tools/find_fused_spaces.py ${h.host} and fix its hits in your edits; run python -B tools/check.py --tree handbook and make sure no NEW finding names ${h.host} (duplicate labels, dangling refs, annex-bidir, bib-key except keys that this wave's intakes add).
Write ${W}/host-patches/applied-${slug(h.host)}.json with [{patch_file, index, decision: applied|skipped, reason}]. Return counts.`,
  { model: 'opus', effort: 'high', schema: HOST, label: `host:${h.host.split('/').slice(-1)[0]}`, phase: 'Hosts' }))

const captureJobs = (args.captures || []).map(c => () => run(`${COMMON}
TASK: apply the correction requests for ONE restoration capture: ${c.host} (provenance record spec/provenance/${c.pid}.json, schema ${c.schema}). Requests: ${c.file}. You own ONLY ${c.host} and the rationale file ${W}/lead/rationale-${c.pid}.md.
Policy: handbook/CONVENTIONS.md "Correction policy (2026-09-06)" and spec/EDITION-2026-CONTRACT.md "Reader-facing content and corrections" permit correcting known errors directly in active restoration files and replacing forward pointers or deferrals with links to the routed proofs. The frozen source/formal-logic-reference.tex is never edited. ${c.schema === 1 || c.schema === 4 ? 'Do NOT edit the provenance record: the lead regenerates it as a version-4 corrected-reader record from your edited capture with tools/restoration_correct.py.' : `This capture's record is schema ${c.schema} (an appendix-layout capture): tools/restoration_correct.py cannot record a correction for it, so do NOT edit ${c.host}. For each request, decide whether the same correction can be made in an adjacent non-restoration handbook file that already discusses the passage (name the file and the exact text; do not edit it), or record it as blocked_policy with the exact change needed.`}
Keep every \\label, every \\begin/\\end pair and the scope structure intact; do not renumber or move material; keep the file UTF-8 without BOM.
${JUDGE}
After editing run python -B tools/find_fused_spaces.py ${c.host}; run python -B tools/check.py --tree handbook and make sure no new finding names ${c.host} other than the expected restoration-scope staleness of ${c.pid} (the lead's record rewrite clears it).
Write ${W}/lead/rationale-${c.pid}.md beginning with the line "## ${c.pid}" followed by one paragraph per applied edit: what was wrong or deferred, what the corrected text says, and the justification (source locator, or the routed label that proves it). Write ${W}/lead/applied-${c.pid}.json with [{patch_file, index, decision: applied|skipped|redirect|blocked_policy, reason, redirect_file?, redirect_text?}]. Return counts.`,
  { model: 'opus', effort: 'high', schema: HOST, label: `capture:${c.pid}`, phase: 'Captures' }))

const leadJob = (key, file, owns, extra) => () => run(`${COMMON}
TASK: implement the requested lead-owned ${key} changes listed in ${file} (items: patch_file, index, request {host, anchor_quote, operation, text, reason}). You own ONLY: ${owns}.
${JUDGE}
${extra}
Write ${W}/lead/applied-${key}.json with [{patch_file, index, decision, reason}] and return a short report (what changed, tests run and their result, anything left undone with the exact reason).`,
  { model: 'opus', effort: 'high', label: `lead:${key}`, phase: 'Lead' })

const leadJobs = []
if (args.tools) leadJobs.push(leadJob('tools', args.tools.file, 'tools/check.py, tools/symbols2tex.py, tools/symbol_registry.py and their test files',
  `These requests add enforcement that the duties named in their reasons require (e.g. a generated-table staleness check, a notation lint, a first_use check, generator layout). Implement them as one coherent change, not as literal text substitution if the anchors moved. Each new check has a self-test under the tool's --selftest; run python -B tools/check.py --selftest, python -B tools/symbols2tex.py --selftest (if it exists) and python -B tools/symbol_registry.py --selftest (if it exists) and make them pass. New finding categories that the requests define as non-hard stay non-hard (hard only under --strict). Then run python -B tools/check.py --tree handbook, and report the counts of the new categories it now emits. Do not regenerate handbook/generated/ (the lead does).`))
if (args.sty) leadJobs.push(leadJob('sty', args.sty.file, 'handbook/handbook.sty',
  `Before and after the edit, compile a scratch document that inputs each restoration scope using the changed macros (the requests name them), under tmp/sty-check/ with latexmk -r C:/Dev/the-methods-of-reason/tools/texlive.latexmkrc -pdf, from a copy of handbook/ preamble; report whether every scope compiles and how the output changed. If a change breaks a scope, fix it within handbook.sty or leave that request skipped with the reason.`))
if (args.frontmatter) leadJobs.push(leadJob('frontmatter', args.frontmatter.file, 'handbook/frontmatter.tex', 'Keep the reader text free of workflow language.'))

const adoptJob = args.adopt ? () => run(`${COMMON}
TASK: make the ${args.wave} adoption clean. Run \`python -B tools/integrate_wave.py adopt --manifest ${args.adopt.manifest} --decisions ${args.adopt.decisions}\` (dry run; create the decisions file as {} first if missing).
1. Repair this wave's intake files themselves (the handbook/registry/symbols-intake-*.csv and handbook/bib/intake-*.bib that the manifest lists; you may edit ONLY these and the decisions file): fix CSV quoting; split mixed cells (glyph = bare TeX; prose such as 'Def. 2.1.28' goes to notes); one row per role; scopes are labels or named scopes (never PNN.k); first_use is a label declared on the route inside the scope. Check each row against the routed body/annex text.
2. Draft ${args.adopt.decisions} (schema per integrate_wave: overrides, row_edits, drop_rows, canonical_row_edits, extend_scopes, citation_aliases, bib_keep_canonical) for every decision-needed item: typed overrides with source and reason when a named source presentation keeps its own notation; citation_aliases only for the same work and version; never narrow a canonical row's meaning without a written reason.${args.adopt.registry_file ? `
3. The author requests in ${args.adopt.registry_file} ask for canonical edits to handbook/registry/symbols.csv (corrected roles, first_use anchors, typed relations). Verify each against the routed text it cites and express each correct one as a canonical_row_edits entry in the decisions file (never edit symbols.csv directly); record skipped ones with reasons in ${W}/lead/applied-registry.json ([{patch_file, index, decision, reason}]).` : ''}
Iterate the dry run until it reports 0 errors and 0 decisions-needed. Do NOT pass --apply. Return a short report: rows repaired, decisions, canonical edits, remaining issues (precisely).`,
  { model: 'opus', effort: 'high', label: `adopt:${args.wave}`, phase: 'Adopt' }) : null

const jobs = [...hostJobs, ...captureJobs, ...leadJobs, ...(adoptJob ? [adoptJob] : [])]
log(`${args.wave} integrate: ${hostJobs.length} hosts, ${captureJobs.length} captures, ${leadJobs.length} lead jobs, adopt ${adoptJob ? 'yes' : 'no'}`)
const results = await parallel(jobs)
const nH = hostJobs.length, nC = captureJobs.length, nL = leadJobs.length
const sum = rs => rs.filter(Boolean).reduce((a, r) => ({ applied: a.applied + (r.applied || 0), skipped: a.skipped + (r.skipped || 0) }), { applied: 0, skipped: 0 })
const missing = results.map((r, i) => r ? null : i).filter(i => i !== null)
if (missing.length) log(`MISSING RESULTS for job indexes ${missing.join(', ')} (agent failed): rerun them`)
return { hosts: sum(results.slice(0, nH)), captures: sum(results.slice(nH, nH + nC)),
  lead: results.slice(nH + nC, nH + nC + nL).map(r => typeof r === 'string' ? r.slice(-2500) : r),
  adopt: adoptJob ? (typeof results[jobs.length - 1] === 'string' ? results[jobs.length - 1].slice(-2500) : results[jobs.length - 1]) : null,
  missing_jobs: missing }
