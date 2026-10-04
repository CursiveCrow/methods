export const meta = {
  name: 'tmor-authoring-wave',
  description: 'One authoring wave: lanes of Opus author blocks, Opus first assessment (guards + coverage), independent Opus confirmation of upgrades',
  whenToUse: 'After `python -B tools/waves.py packetize wNN ...` wrote work/waves/wNN/args.json and the lead took the wave snapshot',
  phases: [
    { title: 'Author', detail: 'Opus author blocks on owned files only', model: 'opus' },
    { title: 'Assess', detail: 'Opus first assessor runs guards + unit compile and assesses coverage', model: 'opus' },
    { title: 'Confirm', detail: 'fresh Opus context independently confirms any section proposed as fully covered', model: 'opus' },
  ],
}

// args: {wave:'w02', root:'work/waves/w02', maxConcurrent:12, agentBudget:940,
//        lanes:[{packets:[{id, path, part, sections:[ids], max_blocks}]}]}
const CAP = Math.min(12, args.maxConcurrent || 12)
const BUDGET = args.agentBudget || 940
const W = 'work/waves/' + args.wave
const ASSESS_DIR = `spec/coverage/edition-2026/assessments/${args.wave}`
let active = 0, spawned = 0
const waiters = []
const acquire = () => active < CAP ? (active++, Promise.resolve()) : new Promise(r => waiters.push(r))
const release = () => { const n = waiters.shift(); if (n) n(); else active-- }
async function run(prompt, opts) {
  if (spawned >= BUDGET) return { budget_exhausted: true }
  spawned++
  await acquire()
  try { return await agent(prompt, opts) } finally { release() }
}
// ---------------- prompts ----------------
const AUTHOR_RULES = `
A1. You are writing, not accepting. Do not state or imply that anything you wrote is complete, accepted, reviewed, admitted or done. Your return reports every component_id in your packet as exactly one of: written (file, line range, labels), partial (the exact missing item), blocked_source, blocked_math or blocked_policy, each with its reason. A component_id missing from your return is treated as not started.
A2. You may not narrow, reinterpret or drop a duty. If a component's success condition is larger than what you can supply, write what you can and report the remainder in the condition's own words. Do not use "out of scope", "by design", "not required", "beyond the scope", "for brevity", "representative", "at the scope of" or "standard" to exempt work.
A3. Write a source-specific presentation only from a held file listed in spec/coverage/edition-2026/held-sources.json (or the packet's units[].held_paths) that you have opened in this session. If the source is not held, or the held file is a different version or lacks the required pages, do not write that presentation from memory, a secondary account or another version: report blocked_source with the exact work, version and pages required. General content may be written from any held authority and cited with a locator you read.
A4. Every locator you write (page, section, theorem or equation number) must be one you saw in the held file in this session. If you cannot verify a locator, leave it out and report it as an open item. Never estimate one.
A5. Write in your own words. Do not reproduce more than ten consecutive words of a source's prose except in a marked, attributed quotation of at most two sentences. Mathematical statements and notation follow the source exactly; keep a named source's own notation and record each symbol's typed role in your symbol intake.
A6. Every proof step the duty requires is written in the annex (annexitem + proof). "Standard", "routine", "well known", "similarly", "left to the reader" and "omitted" are not proofs. Use cited= only where the duty itself names a cited boundary. No proof environments in body files; every body result carries proved=annex:<id> (or sketched=/cited= when the duty allows) with matching annex backlinks.
A7. Put a space between a word and a following number: "Theorem~4.13", "stage 0", "between 0 and 1", "3 October 2026". Run \`python -B tools/find_fused_spaces.py <your files>\` before returning and fix every hit.
A8. Edit only the files listed under owned_files and editable_hosts in your packet. You may read anything. Other agents are working in this tree: never modify their files, the ledger, handbook/bib/handbook.bib, handbook/registry/symbols.csv or symbol-scopes.json, any driver (handbook/main.tex, handbook/parts/pNN.tex, handbook/annex/pNN*.tex), handbook/handbook.sty, citations/, source/, handbook/restoration/ or handbook/generated/. Changes to read-only hosts go into patch-request files under ${W}/patches/ (format: {"host","anchor_quote","operation":"insert_after|replace","text","reason"}). Never run git commands that write, and never build handbook/main.tex.
A9. Before writing, read the packet's "existing" list and search the handbook for existing treatment of each component. Extend or link it; do not write a second treatment. Report any existing treatment you found that was not listed.
A10. Reader text contains no workflow language (review, admission, ledger, assessor, author, block, wave, intake, "this record"). Provenance goes in your spec/research note.
A11. For empirical findings, state the task, population, design, measures, reported uncertainty, competing explanations and replication or generalization limits. Do not turn a descriptive finding into a recommendation.
A12. Do not invent a system, axiom, name, notation or result to fill a template field. If a reference-entry field does not apply, give the reason, citing the source.
A13. Never write a placeholder for content you cannot supply: no contents listing, outline, "see the source" pointer or stub section for a source-specific presentation whose source is not held. Write nothing for it and report blocked_source. If a duty needs changes outside your owned files (drivers, canonical registries, generated files, restoration captures, tools), do not attempt it: report it as blocked_policy with the exact change needed (the lead executes those).
A14. Units listed in your packet's "readonly_units" (unit -> owner packet) are written by their owner packet in this wave. Do not write their components; where your sections need them, \\cref the owner's existing labels or state the dependency in one sentence. Report nothing about them as your gap.
Conventions: read handbook/CONVENTIONS.md and an exemplar such as handbook/parts/p17/finite-expected-utility.tex with its annex. Environments take the label as first argument (hbtheorem/hblemma/hbcorollary: thm:, status, title; hbdefinition/hbconvention/hbmethod/hbexample/hbwarning/proofboundary: def:, title). Every label uses your packet's label_tag (e.g. thm:<label_tag>-...). Citations use \\cite[locator]{Key} with exact locators; new keys go in your intake bib; new symbols in your symbol intake CSV (header glyph,macro,role,scope,precedence,first_use,notes; scope = a sec:/def: label or named scope, NEVER PNN.k). Each new file starts with the packet's toc_tag comment line and the heading level the packet specifies.
Checkpoint: save files as you go; update the "## Continuation" section of your spec/research note after each finished component (and at least every ~15 minutes); stop after about 45 minutes of work and return.
Self-check before returning: \`python -B tools/waves.py unit-compile <packet path>\` must report ok; \`python -B tools/check.py --tree handbook\` filtered to your files must show no new hard finding other than bib-key for keys in your own intake.
Write the return file spec/research/edition-2026-<part>-<slug>-return.json (placement for body and annex per the packet's insertion proposal, label_tag, proposed_decisions for any symbol overlap you know of).`

const AUTHOR_SCHEMA = { type: 'object', properties: {
  components: { type: 'array', items: { type: 'object', properties: {
    component_id: { type: 'string' },
    state: { type: 'string', enum: ['written', 'partial', 'blocked_source', 'blocked_math', 'blocked_policy', 'not_started'] },
    where: { type: 'string' }, remaining: { type: 'string' }, blocker: { type: 'string' } },
    required: ['component_id', 'state'] } },
  files_written: { type: 'array', items: { type: 'string' } },
  patch_requests: { type: 'array', items: { type: 'string' } },
  crosslink_requests: { type: 'array', items: { type: 'string' } },
  acquisition_needs: { type: 'array', items: { type: 'object', properties: {
    source_id: { type: 'string' }, work: { type: 'string' }, version: { type: 'string' }, pages: { type: 'string' }, why: { type: 'string' } },
    required: ['work', 'why'] } },
  unit_compile_ok: { type: 'boolean' },
  continuation: { type: 'string' },
}, required: ['components', 'files_written', 'unit_compile_ok', 'continuation'] }

function authorPrompt(p, k, gaps, mode) {
  return `You are the author for packet ${p.id} (part ${p.part}; sections ${(p.focus || p.sections || []).join(', ') || 'none'}${p.units && p.units.length ? '; queue units without a section row: ' + p.units.join(', ') : ''}), block ${k} of the edition-2026 authoring wave ${args.wave} in C:/Dev/the-methods-of-reason (Windows; Git Bash; TeX Live 2025 for any TeX run).
Read your packet first: ${p.path}. It lists the sections, their recorded remaining duties, the queue units with required components (description, success_condition, failure_condition), held source paths, existing treatments, owned files, editable hosts, label_tag, heading level, toc_tag and the insertion proposal. Then read your spec/research note's "## Continuation" section if it exists.
${mode === 'redirect' ? 'REDIRECT: two blocks made no verified progress. Attack the exact missing dependency named below first, or return a precise blocked_math/blocked_source with the exact missing step or source.\n' : ''}${gaps ? 'An independent assessment of the current text found these remaining gaps; close them now, in this order:\n' + gaps + '\n' : 'Start with the component that others depend on.'}
Write a complete, rigorous reference treatment for a graduate reader: purpose, inputs and conclusions, definitions and assumptions, rules or procedure with side conditions, results with full annex proofs, worked example, failure case or limitation, relationships, and exact sources.
${AUTHOR_RULES}`
}

// explicit per-section keys (args packet field `keys`): both assessors judge exactly the same items
function keyBlock(p, sections) {
  const ks = sections.filter(s => p.keys && p.keys[s])
  if (!ks.length) return sections.length ? `\nREQUIRED KEYS. Each section entry in the packet has "assessment_keys" {components, duties}. Your assessment file for that section MUST contain exactly one components[] entry per listed component_id (copy the id exactly; judge it against the handbook route wherever it is treated) and exactly one duties[] entry per listed duty, with "duty_id" copied exactly. Do not omit a listed key. Any further scope check you add goes in duties[] with a duty_id starting "X-".\n` : ''
  return `\nREQUIRED KEYS. For each section below, your assessment file MUST contain exactly one components[] entry per listed component_id (copy the id exactly; judge it against the handbook route wherever it is treated) and exactly one duties[] entry per listed duty, with "duty_id" copied exactly. Do not omit a listed key and do not leave its verdict unset. Any further scope check you add goes in duties[] with a duty_id starting "X-".\n` +
    ks.map(s => `${s}: components [${p.keys[s].components.join(', ')}]; duties ${p.keys[s].duties.length ? p.keys[s].duties.map(d => `{duty_id "${d.duty_id}": ${JSON.stringify(d.duty)}}`).join('; ') : 'none recorded'}`).join('\n') + '\n'
}

function assessPrompt(p, k, sections, units) {
  const what = (sections.length ? `Sections to assess: ${sections.join(', ')}.` : '') + keyBlock(p, sections)
  const uw = units && units.length ? ` Queue units to account (no ledger section row): ${units.join(', ')}.` : ''
  return `READ-ONLY coverage assessment (you may write ONLY the assessment files named below). Repository C:/Dev/the-methods-of-reason.
Packet: ${p.path}. ${what}${uw} Block ${k}${k === 0 ? ' (initial state, before any author block in this wave)' : ''}.
Step 1 (guards): ${k === 0 ? 'skip the ownership guards for block 0 (nothing was written yet), but' : `run \`python -B tools/waves.py verify ${p.path}\` and`} run \`python -B tools/waves.py unit-compile ${p.path}\` when the packet owns body/annex files that exist; keep the JSON verdicts.
Step 2 (coverage): for EVERY required component id in the packet (description, success_condition, failure_condition) and every recorded duty (missing_pieces / unassessed_scope) of the listed sections, decide from the ACTUAL LaTeX on the handbook route (the packet's owned files, editable and read-only hosts, existing treatments it lists, and any other handbook file you find that treats it) whether it is covered, partial, absent, blocked_source or not_assessable.
S1. You assess coverage only: whether each component is present in complete form. You do not review correctness or source fidelity and you admit nothing. Record suspected errors under defect_observations; they change the verdict only if text is missing, truncated, a pointer or a stub.
S2. Do not open spec/research/*, any *-return.json, ledger prose fields (fulfillment_basis, authored_scope, read_extent) or other assessments. Find the evidence yourself.
S3. "covered" requires every element of the success_condition to be present at lines you cite and no failure_condition to hold. Cite exact paths and line ranges (and labels).
S4. A proof counts only if its steps are written. "Standard", "similarly", "left to the reader", a citation in place of an owed proof, or a sketch where a proof is owed means "partial".
S5. When a component is not covered, state the gap as a duty in the success condition's own terms. Do not soften or shorten it.
S6. For a source-specific component, confirm the source is held (spec/coverage/edition-2026/held-sources.json) and open it at two cited locators; a locator that does not show the cited content is an unsupported_locator and the verdict cannot be covered. A source-specific component whose source is not held is blocked_source (name work, version, pages).
S7. Uncertainty is not coverage. When in doubt, choose partial.
S8. Classify every non-covered item. open_gaps (sections) and open_components with kind "writable"/"partial"/"absent" (units) are ONLY gaps the packet's author can close now inside the packet's owned files/editable hosts from held sources. Everything else goes to blocked[] (sections) or gets that kind (units): "blocked_source" (required source not held, wrong version, preview only: name work, version, pages), "blocked_math" (an exact unproved step), "blocked_policy" (needs a user decision), "lead_owned" (needs changes to drivers, canonical bib/symbols, generated views, restoration captures, tools or other packets' files). Do not repeat a blocked item in open_gaps.
S9. The packet's NEW owned files are routed by the lead only at wave end. Assess their content as the content-to-be-routed: if the only reason a component or duty is not covered is that the owned file is not yet \\input on the route, treat it as covered (cite the owned file's lines) and add ONE blocked item {"kind":"lead_owned","detail":"route pending: <body file> and <annex file>"}; in that case the section's proposed_status is "partial" with empty open_gaps (the upgrade is granted by a re-assessment after routing). Never make "not routed" a writable gap. Placeholder text (contents listings, pointers to an unheld source) is not coverage and should be reported under defect_observations as a placeholder to remove.
S10. Components of units listed in the packet's "readonly_units" are written by the named owner packet in this wave. If one is not covered, classify it as a blocked item {"kind":"lead_owned","detail":"owned by <owner packet>: <gap>"}, never as an open gap of this packet (the post-routing re-assessment judges it after the owner's text is routed).
Write one assessment file per section and one per unit: ${ASSESS_DIR}/CA-${args.wave}-${p.id}-b${k}-<section_id or unit_id>-first.json with schema {"schema":"coverage-assessment/1","assessment_id","section_id" (or "unit_id"),"assessor":{"family":"anthropic","model":"opus","role":"first","context_id":"${args.wave}-${p.id}-b${k}-first"},"inputs":{"tex":[{"path","sha256"}],"sources_opened":[{"path","sha256","pages"}]},"components":[{"component_id","verdict","evidence":[{"path","line_start","line_end","label"}],"gap","blocker":{"kind","ref"}}],"duties":[{"duty","verdict","evidence":[...],"gap"}],"guards":{...},"defect_observations":[...],"not_consulted":["author notes","ledger prose","other assessments"]}.
Return the structured result: guards_hard, unit_compile_ok, sections[{section_id, proposed_status (authored_unreviewed only if every component and duty is covered), open_gaps, blocked[{kind, detail}], assessment_id}], units[{unit_id, open_components[{component_id, gap, kind}], assessment_id}], components_covered.`
}

const ASSESS_SCHEMA = { type: 'object', properties: {
  guards_hard: { type: 'array', items: { type: 'string' } },
  unit_compile_ok: { type: 'boolean' },
  sections: { type: 'array', items: { type: 'object', properties: {
    section_id: { type: 'string' },
    proposed_status: { type: 'string', enum: ['authored_unreviewed', 'partial', 'missing'] },
    open_gaps: { type: 'array', items: { type: 'string' } },
    blocked: { type: 'array', items: { type: 'object', properties: { kind: { type: 'string' }, detail: { type: 'string' } }, required: ['kind', 'detail'] } },
    assessment_id: { type: 'string' } }, required: ['section_id', 'proposed_status', 'open_gaps', 'assessment_id'] } },
  units: { type: 'array', items: { type: 'object', properties: {
    unit_id: { type: 'string' },
    open_components: { type: 'array', items: { type: 'object', properties: {
      component_id: { type: 'string' }, gap: { type: 'string' }, kind: { type: 'string' } }, required: ['component_id', 'gap'] } },
    assessment_id: { type: 'string' } }, required: ['unit_id', 'open_components', 'assessment_id'] } },
  components_covered: { type: 'array', items: { type: 'string' } },
}, required: ['guards_hard', 'unit_compile_ok', 'sections', 'components_covered'] }

const CONFIRM_SCHEMA = { type: 'object', properties: {
  sections: { type: 'array', items: { type: 'object', properties: {
    section_id: { type: 'string' }, all_covered: { type: 'boolean' }, gaps: { type: 'array', items: { type: 'string' } },
    assessment_id: { type: 'string' } }, required: ['section_id', 'all_covered', 'gaps', 'assessment_id'] } },
}, required: ['sections'] }

function confirmPrompt(p, k, ids, unitIds) {
  const unitPart = unitIds && unitIds.length ? `, and queue units (no section row) ${unitIds.join(', ')}` : ''
  return `Independent coverage confirmation (fresh context, role "confirm") for packet ${p.path}, sections ${ids.join(', ') || 'none'}${unitPart}, block ${k}, repository C:/Dev/the-methods-of-reason. Another assessor proposed these as fully covered; for each listed unit write ${ASSESS_DIR}/CA-${args.wave}-${p.id}-b${k}-<unit_id>-confirm.json (same schema, "unit_id" instead of "section_id") and return it in sections[] with section_id=<unit_id>; you have NOT been given its reasoning and must not open other assessment files, spec/research/* notes, *-return.json files or ledger prose fields.
${keyBlock(p, ids)}For each section and each linked required component and recorded duty in the packet, read the actual LaTeX on the route (with line numbers) and decide covered/partial/absent per the rules: covered requires every element of the success_condition present at cited lines and no failure_condition; a proof counts only if its steps are written; source-specific components require the held source (spec/coverage/edition-2026/held-sources.json) opened at two cited locators; uncertainty is not coverage; when in doubt, partial. Try actively to find what is missing. You assess coverage only, not correctness, and admit nothing.
Write one file per section: ${ASSESS_DIR}/CA-${args.wave}-${p.id}-b${k}-<section_id>-confirm.json using schema coverage-assessment/1 with "assessor":{"family":"anthropic","model":"opus","role":"confirm","context_id":"${args.wave}-${p.id}-b${k}-confirm"} and the same component/duty/evidence structure (paths, line ranges, labels, sha256 of each tex input). Return all_covered=true for a section only if every component and duty is covered.`
}

// one assessment step: first assessor, then independent confirmation of proposed AU sections
async function assessStep(p, k, sectionIds, unitIds) {
  const v = await run(assessPrompt(p, k, sectionIds, unitIds), { model: 'opus', effort: 'high', schema: ASSESS_SCHEMA,
    label: `${p.id} assess b${k}`, phase: 'Assess' })
  if (!v || v.budget_exhausted) return v
  const proposed = v.sections.filter(s => s.proposed_status === 'authored_unreviewed')
  const coveredUnits = (v.units || []).filter(u => !(u.open_components || []).length)
  if (proposed.length || coveredUnits.length) {
    const c = await run(confirmPrompt(p, k, proposed.map(s => s.section_id), coveredUnits.map(u => u.unit_id)),
      { model: 'opus', effort: 'high', schema: CONFIRM_SCHEMA, label: `${p.id} confirm b${k}`, phase: 'Confirm' })
    const ok = new Map(((c && c.sections) || []).map(s => [s.section_id, s]))
    proposed.forEach(s => {
      const o = ok.get(s.section_id)
      if (!o || !o.all_covered) { s.proposed_status = 'partial'; s.open_gaps = (o && o.gaps.length) ? o.gaps.map(g => 'assessment_dispute: ' + g) : ['assessment_dispute: confirmation missing'] }
      else s.confirm_assessment_id = o.assessment_id
    })
    coveredUnits.forEach(u => {
      const o = ok.get(u.unit_id)
      if (!o || !o.all_covered) u.open_components = ((o && o.gaps) || ['confirmation missing']).map(g => ({ component_id: '', gap: 'assessment_dispute: ' + g, kind: 'writable' }))
      else u.confirm_assessment_id = o.assessment_id
    })
  }
  return v
}

// ---------------- packet loop ----------------
async function runPacket(p) {
  const covered = new Set()
  const acq = [], blockers = []
  let best = -1, stall = 0, mode = p.mode === 'redirect' ? 'redirect' : 'normal', gaps = null, last = null, a = null
  const unitIds = (p.mode === 'unit_accounting') ? (p.units || []) : []
  const sectionIds = p.focus || p.sections || []
  const merge = (v) => {
    const prev = new Map(((last && last.sections) || []).map(s => [s.section_id, s]))
    v.sections.forEach(s => prev.set(s.section_id, s))
    last = { sections: [...prev.values()], units: v.units || (last && last.units) || [] }
    ;(v.components_covered || []).forEach(c => covered.add(c))
    v.sections.forEach(s => (s.blocked || []).forEach(b => blockers.push({ section_id: s.section_id, ...b })))
  }
  const openSections = () => last.sections.filter(s => s.proposed_status !== 'authored_unreviewed' && !(s.blocked && s.blocked.length && !(s.open_gaps || []).length))
  const writableKind = c => !c.kind || c.kind === 'writable' || c.kind === 'partial' || c.kind === 'absent'
  const openUnits = () => (last.units || []).filter(u => (u.open_components || []).some(writableKind))
  const gapCount = () => openSections().reduce((n, s) => n + (s.open_gaps || []).length, 0)
    + openUnits().reduce((n, u) => n + u.open_components.filter(writableKind).length, 0)
  const result = (outcome, extra) => ({ id: p.id, outcome, last, acq, blockers,
    author: a && { files: a.files_written, patches: a.patch_requests, crosslinks: a.crosslink_requests, continuation: a.continuation }, ...(extra || {}) })

  // block 0: assess the current text before anyone writes (avoids duplicating drafts the ledger has not caught up with)
  const v0 = await assessStep(p, 0, sectionIds, unitIds)
  if (!v0) return result('carry_over', { reason: 'initial_assessment_null' })
  if (v0.budget_exhausted) return result('carry_over', { reason: 'agent_budget' })
  merge(v0)
  if (!openSections().length && !openUnits().length) return result(p.mode === 'author' ? 'drafted' : 'accounted')
  gaps = openSections().map(s => `${s.section_id}: ${(s.open_gaps || []).join(' | ')}`)
    .concat(openUnits().map(u => `${u.unit_id}: ${u.open_components.map(c => c.component_id + ' - ' + c.gap).join(' | ')}`)).join('\n')

  for (let k = 1; k <= p.max_blocks; k++) {
    a = await run(authorPrompt(p, k, gaps, mode), { model: 'opus', effort: mode === 'redirect' ? 'max' : 'high',
      schema: AUTHOR_SCHEMA, label: `${p.id} author b${k}`, phase: 'Author' })
    if (!a) { stall++; if (stall >= 2) return result('carry_over', { reason: 'author_null' }); continue }
    if (a.budget_exhausted) return result('carry_over', { reason: 'agent_budget' })
    acq.push(...(a.acquisition_needs || []))
    const v = await assessStep(p, k, openSections().map(s => s.section_id), openUnits().map(u => u.unit_id))
    if (!v) { stall++; if (stall >= 2) return result('carry_over', { reason: 'assessment_null' }); continue }
    if (v.budget_exhausted) return result('carry_over', { reason: 'agent_budget' })
    merge(v)
    const stillOpen = openSections(), unitsOpen = openUnits()
    const upgraded = last.sections.filter(s => s.proposed_status === 'authored_unreviewed').length
    if (!stillOpen.length && !unitsOpen.length && !(v.guards_hard || []).length)
      return result(upgraded === last.sections.length ? 'drafted' : 'blocked', { guards_hard: v.guards_hard })
    // progress = fewer author-writable gaps or more upgraded sections (verified by the assessor, not claimed)
    const score = 3 * upgraded - gapCount()
    if (best === -1 && k === 1) best = -Infinity
    if (score > best) { best = score; stall = 0 } else stall++
    gaps = stillOpen.map(s => `${s.section_id}: ${(s.open_gaps || []).join(' | ')}`)
      .concat(unitsOpen.map(u => `${u.unit_id}: ${u.open_components.map(c => c.component_id + ' - ' + c.gap).join(' | ')}`)).join('\n')
      + ((v.guards_hard || []).length ? `\nHARD GUARD FAILURES to fix first: ${v.guards_hard.join(', ')}` : '')
    if (stall >= 2) {
      if (mode !== 'redirect' && stillOpen.length > 1)
        return result('split', { children: stillOpen.map((s, i) => ({ ...p, id: `${p.id}.${i + 1}`, focus: [s.section_id], max_blocks: 2, mode: 'author' })) })
      if (mode !== 'redirect') { mode = 'redirect'; stall = 0; continue }
      return result('nonprogress_blocked', { guards_hard: v.guards_hard })
    }
  }
  return result('carry_over', { reason: 'max_blocks', continuation: a && a.continuation })
}

async function runLane(lane) {
  const q = lane.packets.slice(), out = []
  while (q.length) {
    const r = await runPacket(q.shift())
    out.push(r)
    if (r.outcome === 'split') q.unshift(...r.children)
  }
  return out
}

phase('Author')
log(`wave ${args.wave}: ${args.lanes.length} lanes, ${args.lanes.reduce((n, l) => n + l.packets.length, 0)} packets, cap ${CAP}, agent budget ${BUDGET}`)
const results = (await parallel(args.lanes.map(l => () => runLane(l)))).filter(Boolean).flat()
const tally = {}
results.forEach(r => { tally[r.outcome] = (tally[r.outcome] || 0) + 1 })
log(`outcomes ${JSON.stringify(tally)}; agents spawned ${spawned}`)
if (spawned >= BUDGET) log('AGENT BUDGET HIT: remaining work is carry_over (recorded, not dropped)')
return { wave: args.wave, tally, spawned, results: results.map(r => ({ id: r.id, outcome: r.outcome, reason: r.reason,
  sections: r.last && r.last.sections.map(s => ({ section_id: s.section_id, status: s.proposed_status, gaps: s.open_gaps, blocked: s.blocked,
    a: s.assessment_id, c: s.confirm_assessment_id })),
  units: r.last && r.last.units,
  guards_hard: r.guards_hard, acquisition: r.acq, blockers: r.blockers, author: r.author, children: r.children && r.children.map(c => c.id) })) }
