export const meta = {
  name: 'iterate-to-best-summary',
  description: 'Black box: given a prompt + max iterations, generate a story/series summary, then loop[independent harsh critic -> fresh reviser] up to max times. Returns the full history of every summary and every critique; best is assumed to be the last summary.',
  phases: [
    { title: 'Generate' },
    { title: 'Iterate' },
    { title: 'Final-score' },
  ],
}

// ----------------------------------------------------------------------------
// BLACK BOX: prompt + maxIterations  ->  history of {summary, critique}, best = last
//
// Topology (exactly as specified):
//   1. a FORK generates an initial summary from the prompt
//   2. loop up to maxIterations:
//        a. a NEW independent FORK reviews the current summary VERY HARSHLY and
//           returns structured feedback aimed at the creative/generator
//        b. a NEW FORK (receiving old summary + that feedback) writes a revised summary
//   3. one final independent critic scores the last summary so the history is complete
//   Output: { prompt, mode, iterations:[{summary, critique, revised}], finalSummary, ... }
//
// Every fork is a fresh subagent (independence is structural). The critic
// self-escalates: each pass is told to raise its bar above the previous one.
// The rubric is the 10-criterion brutal L3 scale distilled from the pitch-lab run.
// ----------------------------------------------------------------------------

const PROMPT = (args && args.prompt) ||
  'A retired vault-architect is blackmailed into breaking into the floating treasury she designed, one step ahead of the apprentice who upgraded her own traps.'
const MODE = (args && args.mode) || 'story'        // 'story' | 'series'
const MAX = Math.max(1, (args && args.maxIterations) || 3)

const RUBRIC = `
TEN CRITERIA, score each 0-5 (50 max). BRUTAL scale: 5 = definitive/unimprovable (essentially never for a pitch); 4 = actively defeats a skeptic (rare); 3 = competent but resting on an UNPROVEN idea (the DEFAULT); 2 = flawed; 1 = deficient; 0 = absent.
  C  Concreteness/Followability - a naive reader can reconstruct the physical action; no abstraction/bookkeeping engine.
  PS Plot Structure - genuine REVERSAL(s), not one-note escalation; a real second gear; sustainable across length.
  ST Stakes - what is actually at risk (personal AND external); do stakes escalate; is the worst outcome unavoidable by the world's own rules.
  CO Cost/Substance - what is actually PAID on-page + an antagonist with a competing WILL (not a mechanism/weather/legal-system).
  CR Creativity/Originality - novelty of mechanism AND shape AND world AND voice. The "clever mechanism whose USE is the tragic cost / road-to-hell irony" template is itself a cliche and caps CR even when the mechanism is new.
  IN Interestingness - would a reader keep turning pages; intrigue and freshness of the reading EXPERIENCE.
  AC Action/Momentum - the protagonist DRIVES events rather than only absorbing them; things happen.
  HK Hook - a logline + opening image/question that grabs immediately and repeats in one breath.
  AL Aliveness/Voice - an earned, specific, NON-sentimental image (not stock pathos: dying sibling, starving city, dead child); pulse and voice.
  MK Marketability - a nameable audience, genre fit, plausible comp titles, breakout potential.
BANDS (/50): BEST 40-50 / GOOD 32-39 / MEDIOCRE 24-31 / BAD 14-23 / AWFUL 0-13.
`

const SUMMARY_SCHEMA_TEXT = `
Write the summary in EXACTLY these fields, no prose outside them (~200-300 words):
LOGLINE: <one sentence>
ENGINE: <2-3 sentences: the CONCRETE physical mechanism - what literally happens a naive reader could picture. No abstraction/bookkeeping as the subject.>
PROTAGONIST ARC: <start -> end across the moving axes; what they DO, not just feel>
ANTAGONIST (with a WILL): <a specific person/agent with competing goals who LOSES something if the protagonist wins, and escalates against them - not a system or weather>
STAKES: <what is at risk, personal AND external, and how it escalates; why the worst outcome cannot simply be sidestepped>
COST PAID: <what the protagonist actually pays ON-PAGE, escalating; who suffers and what valued thing is lost>
PLOT STRUCTURE: <4-6 beats containing at least ONE genuine REVERSAL (direction changes, not just intensifies) and a second gear; sustainable, not one transaction repeated>
HOOK IMAGE (staged in a beat): <one concrete, unforgettable, non-sentimental image placed AT a named beat above, not as detached metadata>
RANGE/TONE: <name the tone (e.g. heist/comic/adventure/mystery/ambiguous/tragic) and avoid defaulting to solemn tragic-irony; a protagonist who can WIN is allowed>
MARKETABILITY: <audience + 1-2 comp titles + why it sells>
NOVELTY: <the one thing not done this exact way; be honest if it recombines known parts>
`

function generatorPrompt(prompt, mode) {
  return `You are the GENERATOR fork in an iterate-to-best black box. Turn this ${mode === 'series' ? 'SERIES' : 'STORY'} prompt into a substance-backed ${mode === 'series' ? 'SERIES (multi-book arc)' : 'single-story'} summary.

PROMPT: "${prompt}"

${SUMMARY_SCHEMA_TEXT}

HARD LESSONS baked in (a critic will hammer you on every one):
- CONCRETENESS is law: the engine renders as physical action, never an abstraction or bookkeeping process.
- ANTAGONIST must be a WILL with competing goals who loses if the protagonist wins - never a mechanism, institution, weather, or "the system."
- PLOT STRUCTURE needs a real REVERSAL (the story changes DIRECTION), not just escalation to collapse; it must have a second gear that could sustain a novel.
- Close the trap: make the worst outcome unavoidable by the world's own rules, OR give a genuinely open ending where the protagonist might win - do not leave a lazy sidestep.
- Stage your best IMAGE inside a beat; do not save one capstone image - distribute concreteness.
- AVOID the overproduced "a magic mechanism whose very use is the tragic cost, road-to-hell irony" template. Aim for range: a hook, momentum, a protagonist who acts, a tone that isn't reflexively elegiac.
- Earn emotion; do not buy it with stock pathos (dying sibling, starving city, dead child).
- It must be MARKETABLE: a real audience and plausible comps.

Return ONLY the summary in the field format. Your text is the artifact, not a message.`
}

function criticPrompt(summary, iter, mode) {
  return `You are an INDEPENDENT, BLIND, self-escalating CRITIC fork (iteration ${iter}) in an iterate-to-best black box. You have seen no other summary and no other critic's notes. Your job is to review this ${mode} summary VERY HARSHLY and hand the creative side concrete feedback.

SELF-ESCALATION: assume any prior critic was too soft. Raise your bar ABOVE iteration ${iter - 1}. Assume this summary is OVERRATED until it proves otherwise; every time you are tempted to give a 4 or 5, stop and raise the standard.

This is a PITCH, not a story. The hard part - interiority, earned emotion, sustaining a novel, working prose - is UNPROVEN. Credit ONLY what the summary demonstrates; treat unproven payoff as a LIABILITY.

${RUBRIC}

Run these attacks and dock the relevant axis for each that lands: PITCH-NOT-STORY (names what it hasn't proven), FORMULA (the tragic-irony-mechanism template -> caps CR), SENTIMENTALITY (stock pathos -> docks AL), SUSTAINABILITY (one-move premise inflated to length -> docks PS/AC), GENERIC (derivative -> docks CR), UNAVOIDABILITY (a smarter protagonist sidesteps -> docks ST/CO), ANTAGONIST-AS-FUNCTION (no competing will -> docks CO).

Score all ten axes. Name at least THREE concrete weaknesses (a named beat/cliche/fault, never a hedge). Then give SPECIFIC, ACTIONABLE fixes the reviser can execute, and one paragraph of generator_feedback aimed at the creative process. A review that names no weakness is a failure.

THE SUMMARY:
${summary}`
}

function reviserPrompt(oldSummary, critique, mode) {
  const fixes = (critique && critique.fixes || []).map((f, i) => `  ${i + 1}. ${f}`).join('\n')
  const weaknesses = (critique && critique.weaknesses || []).map((w, i) => `  ${i + 1}. ${w}`).join('\n')
  return `You are a FRESH REVISER fork in an iterate-to-best black box. You receive the previous ${mode} summary and a harsh critic's feedback. Produce a REVISED summary that genuinely raises its quality band - do not merely patch wording; fix the structural faults named.

PREVIOUS SUMMARY:
${oldSummary}

CRITIC BAND: ${critique && critique.band} (${critique && critique.total}/50)
CRITIC WEAKNESSES:
${weaknesses}
CRITIC FIXES TO EXECUTE:
${fixes}
CRITIC FEEDBACK TO THE CREATIVE PROCESS:
${critique && critique.generator_feedback}

${SUMMARY_SCHEMA_TEXT}

Address EVERY weakness and fix above. Keep what already worked. Above all: give the antagonist a competing will, put a real REVERSAL in the plot structure (not just escalation), close the unavoidability hole or open the ending honestly, stage a non-sentimental hook image inside a beat, and break any tragic-irony-formula sameness. Return ONLY the revised summary in the field format. Your text is the artifact.`
}

const CRITIC_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['scores', 'total', 'band', 'weaknesses', 'fixes', 'generator_feedback', 'verdict'],
  properties: {
    scores: {
      type: 'object',
      additionalProperties: false,
      required: ['C', 'PS', 'ST', 'CO', 'CR', 'IN', 'AC', 'HK', 'AL', 'MK'],
      properties: {
        C: { type: 'integer', minimum: 0, maximum: 5 },
        PS: { type: 'integer', minimum: 0, maximum: 5 },
        ST: { type: 'integer', minimum: 0, maximum: 5 },
        CO: { type: 'integer', minimum: 0, maximum: 5 },
        CR: { type: 'integer', minimum: 0, maximum: 5 },
        IN: { type: 'integer', minimum: 0, maximum: 5 },
        AC: { type: 'integer', minimum: 0, maximum: 5 },
        HK: { type: 'integer', minimum: 0, maximum: 5 },
        AL: { type: 'integer', minimum: 0, maximum: 5 },
        MK: { type: 'integer', minimum: 0, maximum: 5 },
      },
    },
    total: { type: 'integer', minimum: 0, maximum: 50 },
    band: { type: 'string', enum: ['AWFUL', 'BAD', 'MEDIOCRE', 'GOOD', 'BEST'] },
    weaknesses: { type: 'array', items: { type: 'string' }, minItems: 3 },
    fixes: { type: 'array', items: { type: 'string' }, minItems: 2 },
    generator_feedback: { type: 'string' },
    verdict: { type: 'string' },
  },
}

// --- run -------------------------------------------------------------------

phase('Generate')
log(`black box: mode=${MODE} maxIterations=${MAX}`)
let current = await agent(generatorPrompt(PROMPT, MODE), { label: 'generate:v0', phase: 'Generate' })

const history = []
phase('Iterate')
let converged = false
let i = 0
while (i < MAX) {
  i++
  const critique = await agent(criticPrompt(current, i, MODE), { label: `critique:i${i}`, phase: 'Iterate', schema: CRITIC_SCHEMA })
  if (!critique) { break }                                   // critic fork died; stop cleanly
  if (critique.band === 'BEST') {                            // already best; record and stop
    history.push({ iteration: i, summary: current, critique, revised: null })
    converged = true
    log(`iteration ${i}: ${critique.band} ${critique.total}/50 — converged`)
    break
  }
  const revised = await agent(reviserPrompt(current, critique, MODE), { label: `revise:i${i}`, phase: 'Iterate' })
  history.push({ iteration: i, summary: current, critique, revised: revised || null })
  log(`iteration ${i}: ${critique.band} ${critique.total}/50 -> revised`)
  if (!revised) { break }                                    // reviser died; keep last good summary
  current = revised
}

// Final independent score on the last summary so the history is complete and
// the "best = last" claim is checkable.
phase('Final-score')
const finalCritique = converged
  ? history[history.length - 1].critique
  : await agent(criticPrompt(current, MAX + 1, MODE), { label: 'critique:final', phase: 'Final-score', schema: CRITIC_SCHEMA })

// --- persist the full history to disk (the box's output artifact) ----------
function bandStr(c) { return c ? `${c.band} ${c.total}/50` : 'n/a' }
let md = `# Black box demo run — iterate-to-best\n\n`
md += `**Prompt:** ${PROMPT}\n\n`
md += `**mode:** ${MODE} · **maxIterations:** ${MAX} · **converged:** ${converged}\n\n`
md += `**Trajectory:** ` + history.map((h) => `i${h.iteration} ${bandStr(h.critique)}`).join('  →  ') + `  →  final ${bandStr(finalCritique)}\n`
for (const h of history) {
  md += `\n---\n\n## Iteration ${h.iteration}\n\n### Summary going in\n\n${h.summary}\n\n`
  md += `### Independent critic — ${bandStr(h.critique)}\n\n`
  md += `Scores: \`${JSON.stringify(h.critique.scores)}\`\n\n`
  md += `**Weaknesses:**\n` + h.critique.weaknesses.map((w) => `- ${w}`).join('\n') + `\n\n`
  md += `**Fixes handed to the reviser:**\n` + h.critique.fixes.map((f) => `- ${f}`).join('\n') + `\n\n`
  md += `**Feedback to the generator:** ${h.critique.generator_feedback}\n`
}
md += `\n---\n\n## FINAL SUMMARY (best assumed = last)\n\n${current}\n\n`
md += `### Final critic — ${bandStr(finalCritique)}\n\n`
if (finalCritique) {
  md += `Scores: \`${JSON.stringify(finalCritique.scores)}\`\n\n`
  md += `Verdict: ${finalCritique.verdict}\n`
}

await agent(
  `Use the Write tool to create the file /home/user/and-shoot/pitch-lab/blackbox/demo-run.md with EXACTLY the content between the BEGIN and END markers below — verbatim, no edits, no added commentary, do not include the markers themselves.\n\n<<<BEGIN>>>\n${md}\n<<<END>>>`,
  { label: 'persist-history', phase: 'Final-score' }
)

return {
  prompt: PROMPT,
  mode: MODE,
  maxIterations: MAX,
  converged,
  bestIsLast: true,
  trajectory: history.map((h) => ({ i: h.iteration, band: h.critique.band, total: h.critique.total })),
  finalBand: finalCritique ? finalCritique.band : null,
  finalTotal: finalCritique ? finalCritique.total : null,
  persisted: 'pitch-lab/blackbox/demo-run.md',
}
