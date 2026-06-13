---
description: Training harness for a tunable agent. Generates N config variants of a target agent (current + mutations), runs each against an evidence battery, has the arbiter judge the outputs, and promotes the winner. Pre-wired targets - editor, fixer (revisor). Subsumes brighid's editor-persona-tuning + critic-persona-tuning. Winners become save-as-new mutations (oskar) / proposals (admin); the arbiter is the judge (not general-purpose). On-demand or dispatched by /and-tend when an agent's tuning is due. Usage - /and-forge <agent-slug> [--target <config-path>] [--cases <battery-path>] [--variants N]
---

# /and-forge

A **training harness**. Does the target agent's current configuration actually produce the best output it can? The harness tests that by pitting the live config against mutated candidates over a fixed battery of cases, letting the **arbiter** judge blind, and promoting the winner.

This is the "harness to improve the editor and revisor." It is **agent-parameterized** — `editor` and `fixer` (the revisor) are pre-wired targets, but any tunable NON-PERSONA agent or rubric is a valid target.

**Persona fence.** A persona target (on-stage persona card, audience persona card) may be *judged* but its winning content may NOT be auto-promoted — persona content is the principal's non-delegable lane. Forge against a persona target stops at the scorecard + an ESCALATE recommendation.

**Read-only against the live config.** Mutations are authored save-as-new (oskar). The live agent `.md` / card / rubric is never overwritten by the harness; promotion is a separate, recorded step.

---

## Phase 0 — Validate & assemble

1. Parse `<agent-slug>`. Resolve the **target config** to tune:
   - `editor` → `.claude/agents/editor.md` (prose-economy pass).
   - `fixer` → `.claude/agents/fixer.md` (the revisor — targeted correction).
   - else `--target <path>` (an agent `.md`, a card, or a rubric e.g. `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md`).
2. **Persona check.** If the target is a persona card or an audience persona, set `persona_fence: true` (judge-only; no auto-promote).
3. **Evidence battery.** `--cases <path>` names a battery file (a set of representative inputs the target processes). If absent, assemble a default battery:
   - `editor` → 3–5 stitched-draft excerpts (or bones+facets→prose slices) spanning registers, drawn from `active-project/draft/` + recent reviews.
   - `fixer` → 3–5 `{auditor-finding → required-criteria}` cases drawn from recent `active-project/staff/auditor/*-audit.md`.
   - critic/rubric targets → an evidence pack of known-good + known-bad cases with expected verdicts (the brighid critic-persona-tuning shape; success metric = catch-rate).
4. **Parking-lot scan (Rule 14).** Items matching `/and-forge` + this target.
5. Build the working dir `staff/forge/<agent-slug>-<timestamp>/`.

---

## Phase 1 — Variant generation (oskar)

Dispatch **oskar** to author the candidate set: the **current** config (verbatim) plus `N−1` mutations (default `--variants 3`, so 2 mutations). Each mutation is a save-as-new sibling under the working dir, tagged with a change class (enrich / tighten / loosen / rewrite / add-section) and a one-line hypothesis ("tighten the hollow-prose list — predict fewer false cuts"). The live config is never edited. Confirm each variant file exists (Rule 19).

---

## Phase 2 — Run variants against the battery

For each case × each variant, dispatch the **target agent** under that variant's config and collect the output to `<work-dir>/case-<C>-variant-<V>.md`. (Fan out in parallel where the agent is stateless.) Validate every expected output exists (Rule 19); re-dispatch a failed cell once, then abort with the failed list.

---

## Phase 3 — Arbiter judges (judge mode)

For each case, dispatch the **arbiter** in `mode: judge`:
- `rubric_path` — the target's evaluation rubric (editor: prose-economy + hollow-prose + the no-ledger fence DEC-0115; fixer: criteria-met + minimum-change + no-overcorrection; critic: catch-rate vs. expected verdicts).
- `variants[]` — the per-case outputs, **anonymized** (the harness keeps the label↔variant map).
- `scorecard_schema: schemas/tournament-scorecard.schema.md`.
- `output_path: <work-dir>/scorecard-case-<C>.md`.

The arbiter returns winner + ranking + tuning-flags per case. Aggregate across cases: which variant wins most cases, by what margin, and the union of tuning-flags. Confirm each scorecard on disk (Rule 19).

---

## Phase 4 — Promote (or don't)

Read the aggregate. Three outcomes:

1. **A mutation beats current decisively** (wins a majority of cases at `clear`+ margin):
   - Non-persona target → **oskar** writes the winning mutation as the recommended replacement (save-as-new); **ingrid** greenlights the agent-`.md`/rubric edit under delegated authority (or **margit** reconciles if it's a card). Record the promotion in the run report.
   - `persona_fence: true` → do NOT promote. Emit an ESCALATE recommendation to the principal with the scorecard.
2. **Current wins / no lift** (ceiling): log "no improvement this battery"; record the ceiling so `/and-tend` doesn't re-forge this target until new signal accrues.
3. **The gap is upstream of the config** (arbiter flagged `rewards-no-arm-hit` / `peeves-firing-on-every-arm` — no variant could fix it): the rubric is blind or the failure is upstream. Hand to **admin** process-critic to author a proposal (rubric gap) or to **oskar** to route upstream (`/and-write` / `/and-substance` revise).

---

## Phase 5 — Persist + process-critic (always fires)

1. Write the run report `active-project/staff/reviews/forge-<agent-slug>-<timestamp>.md` (or `staff/forge/` if no project active): target, battery, variant hypotheses, per-case scorecards, aggregate winner, promotion decision, ceiling/upstream flags.
2. Dispatch **admin** `mode: process-critic` (like `/and-ablate` Phase 5): `trigger.reason: on-demand`, `trigger.source_report: <report path>`, `trigger.source_verdict: forge:<agent>:<outcome>`, `gate_path: .claude/commands/and-forge.md#phase-3`. Admin logs `OK` / `PROCESS-CHANGE-PROPOSED`.
3. Update `staff/oskar/patterns.md` if the forge surfaced a recurring pattern; update `staff/ingrid/stm.md` with the tuning outcome.
4. Print the summary: target, winner, promotion decision, report path.

---

## What this command does not do

- Overwrite the live agent `.md` / card / rubric directly (mutations are save-as-new; promotion is a recorded, authorized edit).
- Auto-promote persona content (judge-only; escalates).
- Use `general-purpose` to score — the **arbiter** is the judge, for consistency across runs.
- Gate the chapter chain. Forge is improvement, not a ship gate.

## Cost shape

Per run: 1 oskar (variant gen) + (cases × variants) target dispatches + cases × 1 arbiter judge + 1 admin process-critic + promotion routing. For the default 4 cases × 3 variants: ~16–18 dispatches. Run an agent's forge when its tuning is *due* (new signal since last forge), not reflexively.
