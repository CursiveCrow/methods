export const meta = {
  name: 'tmor-w02a-integrate',
  description: 'W2-a integration: per-host patch application, intake repair + adoption decisions, rule-display fix',
  phases: [
    { title: 'Hosts', detail: 'Opus applies verified patch requests, one agent per shared host', model: 'opus' },
    { title: 'Adopt', detail: 'Opus repairs W2 intake CSVs and drafts the adoption decisions to a clean dry run', model: 'opus' },
    { title: 'Rules', detail: 'Opus moves rule displays out of body files into calculus sheets', model: 'opus' },
  ],
}
const LIMIT = 10
let active = 0; const waiters = []
const acquire = () => active < LIMIT ? (active++, Promise.resolve()) : new Promise(r => waiters.push(r))
const release = () => { const n = waiters.shift(); if (n) n(); else active-- }
const run = async (p, o) => { await acquire(); try { return await agent(p, o) } finally { release() } }
const ROOT = 'C:/Dev/the-methods-of-reason'
const COMMON = `Repository ${ROOT} (Windows; Git Bash; TeX Live 2025 at C:/texlive/2025/bin/windows). Lead integration of authoring wave W2-a. Other agents edit OTHER files concurrently. No git write commands. Never edit handbook/restoration/**, handbook/generated/**, drivers (handbook/main.tex, handbook/parts/pNN.tex, handbook/annex/pNN*.tex), handbook/handbook.sty, handbook/bib/handbook.bib, handbook/registry/symbols.csv, handbook/registry/symbol-scopes.json, tools/**. Never change mathematics or claims beyond what a request explicitly specifies.`
const HOST = { type: 'object', properties: { host: { type: 'string' }, applied: { type: 'integer' }, skipped: { type: 'integer' },
  skipped_reasons: { type: 'array', items: { type: 'string' } } }, required: ['host', 'applied', 'skipped'] }

phase('Hosts')
const hostJobs = args.hosts.map(h => () => run(`${COMMON}
TASK: apply the author patch requests for ONE shared host: ${h.host}. Requests: ${h.file} (each item: patch_file, index, request {host, anchor_quote or anchor, operation insert_after|replace|..., text, reason}). You own ONLY ${h.host} in this task.
For each request: (1) locate the anchor quote exactly once in the host (if absent or ambiguous, skip with reason); (2) judge whether the change is a correct, minimal, consistent edit (cross-reference, link, short added sentence, label alignment, corrected statement the request justifies with a source); skip requests that would duplicate content already present, conflict with another applied request, introduce workflow language, add proof environments in a parts/ body file, use undefined labels or bib keys, or change mathematics without justification; (3) apply in order with minimal edits preserving the file's line endings; (4) record each decision. After applying, run python -B tools/find_fused_spaces.py ${h.host} and fix its hits in your edits; run python -B tools/check.py --tree handbook and make sure no NEW finding names ${h.host} (duplicate labels, dangling refs, annex-bidir, bib-key except keys that the W2 intakes add).
Write work/waves/w02/host-patches/applied-${h.host.replace(/[\\/]/g, '__')}.json with [{patch_file, index, decision: applied|skipped, reason}]. Return counts.`,
  { model: 'opus', effort: 'high', schema: HOST, label: `host:${h.host.split('/').slice(-1)[0]}`, phase: 'Hosts' }))

const adoptJob = () => run(`${COMMON}
TASK: make the W2-a adoption clean. Run \`python -B tools/integrate_wave.py adopt --manifest spec/research/edition-2026-authoring-batch-intake-9.json --decisions work/waves/w02/decisions-w02a.json\` (dry run; create the decisions file as {} first). There are about 160 errors (CSV parse failures, refused rows whose glyph cell mixes math delimiters and prose like '\\(X,Y,R\\) (Def. 2.1.28)', unresolved bindings) and decisions-needed items.
1. Repair the W2 intake files themselves (handbook/registry/symbols-intake-p0*-*-w02-*.csv and handbook/bib/intake-p0*-*-w02-*.bib — you may edit ONLY these): fix CSV quoting; split mixed cells (glyph = bare TeX, e.g. X,Y,R; move prose like 'Def. 2.1.28' to notes); one row per role; scopes must be labels or named scopes (never PNN.k); first_use must be a label declared on the route inside the scope (the new W2 files are now routed). Check each row against the actual body/annex text.
2. Draft work/waves/w02/decisions-w02a.json (schema per integrate_wave: overrides, row_edits, drop_rows, canonical_row_edits, extend_scopes, citation_aliases, bib_keep_canonical) for every decision-needed item: prefer typed overrides with source and reason when a named source presentation keeps its own notation; citation_aliases to an existing canonical key only for the same work and version; never narrow a canonical row's meaning without a written reason.
3. Iterate the dry run until it reports 0 errors and 0 decisions-needed. Do NOT pass --apply. Return a short report: rows repaired, decisions, remaining issues (if any cannot be resolved, list them precisely).`,
  { model: 'opus', effort: 'high', label: 'adopt:w02a', phase: 'Adopt' })

const ruleJob = () => run(`${COMMON}
TASK: python -B tools/check.py --tree handbook reports 17 rule-outside-registry findings (\\frac-based rule shapes) in handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02-p02-005.tex (around lines 970-1000). House convention (handbook/CONVENTIONS.md): rule displays live only in calculus sheets under handbook/registry/calculi/, which the body \\input's or references via \\showcalculus. Move these rule displays into a new sheet file handbook/registry/calculi/p02-w02-p02-005-rules.tex (study an existing sheet such as handbook/registry/calculi/hilbert-cpl.tex for the \\calculussheet/\\hbrule format) and replace them in the body with the sheet reference used elsewhere, preserving every rule, side condition and label. You own only the body file, its annex and the new sheet. Afterwards check.py must show 0 rule-outside-registry findings for that file and no new findings; compile the unit with python -B tools/waves.py unit-compile work/waves/w02/packets/w02-p02-005.json. Return a short report.`,
  { model: 'opus', effort: 'high', label: 'rules:w02-p02-005', phase: 'Rules' })

const results = await parallel([...hostJobs, adoptJob, ruleJob])
const hostResults = results.slice(0, args.hosts.length).filter(Boolean)
return { hosts: hostResults.length, applied: hostResults.reduce((n, r) => n + (r.applied || 0), 0), skipped: hostResults.reduce((n, r) => n + (r.skipped || 0), 0),
  adopt: typeof results[args.hosts.length] === 'string' ? results[args.hosts.length].slice(-2500) : results[args.hosts.length],
  rules: typeof results[args.hosts.length + 1] === 'string' ? results[args.hosts.length + 1].slice(-1200) : results[args.hosts.length + 1] }
