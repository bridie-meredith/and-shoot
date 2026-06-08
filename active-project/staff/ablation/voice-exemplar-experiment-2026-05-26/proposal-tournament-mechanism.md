---
purpose: Proposal sketch — exemplar-tournament mechanism for Tier-1 consumers
authored-by: claude (in-session, 2026-05-26; user-requested during voice-exemplar experiment)
status: PARTIALLY CODIFIED 2026-05-26 — Phase 1 (renderer-voice) landed in .claude/commands/and-stitch.md under URI-STITCH-MULTI-ARM / URI-STITCH-TOURNAMENT / URI-STITCH-COUNTERWEIGHT / URI-STITCH-CHERRY-PICK / URI-EXEMPLAR-POV-FENCE. Phase 2 (impersonator-tournament at per-character per-book scope) + Phase 3 (audience-tournament) deferred. Admin process-critic formalization into staff/admin/process-proposals.md still pending for the remaining phases.
basis: 2026-05-26 voice-exemplar experiment + 2026-05-26 taste-aligned voice-exemplar tournament (load-bearing counterweight finding) + 2026-05-26 impersonator-experiment + 2026-05-26 audience-experiment + 2026-05-26 critic-experiment
codification-refs:
  - .claude/commands/and-stitch.md § Args (--max-arms / --include-pov-mismatch / --cherry-pick)
  - .claude/commands/and-stitch.md § Phase 0 step 4a (URI-STITCH-MULTI-ARM + URI-EXEMPLAR-POV-FENCE + URI-STITCH-COUNTERWEIGHT)
  - .claude/commands/and-stitch.md § Phase 0.5 pre-flight summary (multi-arm fields)
  - .claude/commands/and-stitch.md § Phase 1 — multi-arm dispatch (URI-STITCH-MULTI-ARM)
  - .claude/commands/and-stitch.md § Phase 1.5 — Per-scene tournament selection (URI-STITCH-TOURNAMENT + URI-STITCH-CHERRY-PICK)
  - staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md (judge-prompt template)
  - active-project/theater/voice-exemplar-b01-c02.md (V1 market-observational; tournament winner)
  - active-project/theater/voice-exemplar-b01-c02.alt-1.md (V4 fisherwoman-parallel-tracks; second arm)
---

# Exemplar-tournament mechanism — sketch

## The problem

Tier-1 exemplar consumers (impersonator, audience, renderer voice — per CLAUDE.md Rule 16) currently load **one** exemplar per dispatch — the project-bound override if present, else the library default, else nothing. This single-path resolution assumes the resolved exemplar is the best fit for the consumer in this context. The voice-exemplar experiment on c02 scene-A (2026-05-26) disproved that assumption empirically:

| Variant | Rank | Notes |
|---------|------|-------|
| Septon-Halvard (cross-persona transfer; pausal cadence) | 1 | Won — surface-fence held; cadence-fit best |
| Criston-Cole (cross-persona transfer; terse cadence) | 2 | Best percussion discipline; POV-fence leak |
| Robinson (the wired default voice-exemplar.md) | 3 | Long-sentence cadence suffocated the peak bone |
| (none — baseline) | 4 | Worst — paragraph-architecture undirected |

**Three findings of operational significance:**

1. **The default exemplar may not be the best exemplar for a given chapter / scene / role.** Single-path resolution silently locks in a prime that may rank below an available alternative.
2. **Cross-persona transfer works.** The winning prime for the renderer on this chapter was an *impersonator* exemplar (Septon-Halvard) used in a renderer role — out of class but in format. The library is bigger than its current per-role wiring suggests.
3. **The cost of finding the winner is low at the renderer-minimal layer** (~5 dispatches for the c02 experiment, ~175K tokens). The cost would be prohibitive at the full-/and-stitch layer (~30+ dispatches × N variants = 100+ dispatches per tournament).

## The proposal

**Run a tournament at the cheap layer (renderer-minimal / impersonator-prime / audience-review-prime), cache the winner at the resolution point the production layer reads, fire the production layer once with the winner.**

The tournament is amortized: it runs once per chapter (or once per character per book, or once per project), and the winner is cached for every subsequent dispatch at that scope. The /and-stitch pipeline itself runs once per chapter, not N times.

### Architecture by role

| Role | Tournament layer | Cache scope | Variants per tournament |
|------|------------------|-------------|------------------------|
| **Renderer voice** (`/and-stitch` Phase 0 step 4a) | renderer-minimal on one representative scene | per-chapter file: `active-project/theater/voice-exemplar-<book>-<chapter>.md` (current per-chapter override slot) | 3-4 candidates + 1 baseline |
| **Impersonator** (per character per dispatch) | impersonator on one representative scenario from character's chunk | per-character per-book file: `active-project/persona-exemplars/<slug>-<book>.md` | 2-3 candidates + 1 baseline |
| **Audience** (per phase-5b cycle) | audience on one representative facet entry | per-persona per-book file: `active-project/audience/<slug>/exemplar.md` | 1 + 1 baseline (most audience personas have only 1 library exemplar today) |

The renderer-voice path is the highest-value first deployment because (a) the experiment showed the largest variance between candidates there, (b) the per-chapter cache slot already exists in `/and-stitch` Phase 0 step 4a, and (c) renderer-minimal is the lightest tournament-arm subagent in the toolbox.

### Tournament procedure

1. **Candidate set construction** — read all `cards/persona-exemplars/*.md` with `dispatch-status: active` matching the role's POV requirement (e.g. first-person for first-person bones header), plus the no-prime baseline. Cap at 4 candidates per tournament (cost discipline).
2. **Parallel render** — fan out renderer-minimal (or impersonator, or audience-fork) dispatches in parallel, one per candidate, rendering the same representative scene/scenario.
3. **Blind cold-read ranking** — dispatch ONE general-purpose agent with the candidate outputs at position labels P1-PN. The judge ranks against role-specific criteria (see § Role-fit criteria below). Position→variant mapping revealed after ranking is finalized.
4. **Cache the winner** — write the winning exemplar's content to the per-scope cache file (e.g. `active-project/theater/voice-exemplar-<book>-<chapter>.md`). Stamp the tail with `selected-via: tournament @<date>` for traceability.
5. **Production dispatch reads the cached winner** — `/and-stitch` Phase 0 step 4a finds the per-chapter override (the cache) and uses it; existing resolution order unchanged.

### Role-fit criteria (judge inputs)

The judge needs role-specific criteria — what "winning" looks like differs per consumer:

| Role | Criteria the judge applies |
|------|----------------------------|
| Renderer voice | Bone-faithfulness, register-fit to bones-header narrator, percussion discipline against scene-map rhythm-shape, surface-fence compliance (no exemplar-content leak), POV-match (no third-person slip on first-person bones header) |
| Impersonator | Character-card fence compliance (no forbidden registers), behavior-card cadence-fit, scenario-objective delivery, Earth-Bet-fence compliance, audience-trio-modeled vs over-priming |
| Audience review | Persona-card stance compliance, hot-button firing accuracy, fatigue-signaling fidelity, prescription discipline (verdict + actionable directive), no over-engagement |

These should be standardized as judge-prompt templates at `staff/admin/exemplar-tournament-judge-prompts/<role>.md` for consistency across tournaments.

### When to fire the tournament

| Trigger | Rationale |
|---------|-----------|
| **Cold start** (first invocation of role × scope) | Default behavior. The cached winner gets reused for every subsequent dispatch at the same scope. |
| **Cache stale** (e.g. exemplar library updated, or `/and-substance` revised the chunk that the cache was tuned for) | Re-fire to confirm the cached winner still wins; surface stale-warning at /and-stitch Phase 0 if cache > N days old. |
| **Gate failure routes to revise** (Phase 9 FAIL, audience REVISE on facet, post-op convergence flag) | The cached winner may no longer fit if the upstream content changed; re-fire on the next invocation. |
| **User-explicit flag** (`--exemplar-tournament=force`) | Override cache for experimental purposes. |

**NOT** every dispatch. Running a tournament every dispatch would multiply spend by N × dispatch-count without commensurate benefit — most dispatches at a given scope share the same winner.

### Cost model

For the renderer-voice role at the per-chapter scope:
- 1 tournament per chapter (not per scene; the representative scene is enough)
- 4 candidates × 1 renderer-minimal dispatch per chapter ≈ 4 dispatches (~112K tokens)
- 1 cold-read ranking dispatch (~32K tokens)
- **Total per-chapter overhead: ~5 dispatches, ~144K tokens** — confirmed empirically on c02 scene-A

Compared to:
- A full /and-stitch run: ~30+ dispatches per chapter
- A re-stitch after a Phase 9 fail: another ~30+ dispatches

**Tournament overhead is ~17% of a single stitch run.** Cheap by any reasonable measure, and the winner persists across all subsequent revises until something invalidates the cache.

For the impersonator role at per-character-per-book scope:
- 1 tournament per character per book (not per dispatch)
- 3 candidates × 1 impersonator dispatch ≈ 3 dispatches
- 1 cold-read = 4 dispatches total per character per book
- **Total per-book overhead for 6 active characters: ~24 dispatches** — cheap

For the audience role:
- Currently each persona has 1 library exemplar; tournament collapses to 1-vs-baseline (2 candidates)
- 2 candidates × 1 audience dispatch + 1 cold-read = 3 dispatches per persona per book
- **Total per-book overhead for 3 audience personas: ~9 dispatches** — trivially cheap

### Schema additions

| File | Addition |
|------|----------|
| `schemas/persona-exemplar.schema.md` | Optional `tournament-eligible: <boolean>` field (default true for active exemplars). Exemplars marked `tournament-eligible: false` skip the tournament (e.g. when an exemplar is being staged for a specific role and the user does not want it competed). |
| `schemas/persona-exemplar.schema.md` | Optional `role-fit-criteria: <freeform>` block — author-supplied notes on what winning looks like for this exemplar's intended role (default: inherit from role's standard criteria). |
| `cards/persona-exemplars/INDEX.md` | New column: `tournament-status: untested | winner-at-<scope> | runner-up | excluded` — populated by tournament dispatches as side-effect. |
| `schemas/stitch-profile.schema.md` | Optional `voice-exemplar.tournament: { enabled: bool, candidates: [<slugs>], representative-scene: <label> }` block. Default `enabled: true` once the mechanism lands; opt-out per project. |
| Per-chapter cache file (`active-project/theater/voice-exemplar-<book>-<chapter>.md`) | Tail comment: `<!-- selected-via: tournament @<date>; candidates: [<slug1>, <slug2>, ...]; ranked-by: cold-read; verdict-path: <staff/ablation path> -->` |

### Library impact

Today the persona-exemplar library has 14 active entries (3 audience + 11 impersonator + 1 renderer voice). Cross-persona transfer means each Tier-1 dispatch potentially has 14+1 candidates competing. Capping per tournament at 4 (the recommended pool size for a single cold-read pass) requires a pre-tournament shortlist:

1. **POV pre-filter** (mechanical) — exclude any exemplar whose POV doesn't match the bones-header `narrator:` field. Closes the Criston-Cole third-person-slip failure mode.
2. **Setting-adjacency pre-rank** (lightweight) — exemplars whose `content-match` field marks a setting-adjacent register rank higher (Flea Bottom > court > generic Westeros > generic prose) for King's-Landing chapters.
3. **Register-target pre-rank** (lightweight) — exemplars whose `voice-target` matches the bones-header narrator's documented register beat win the tie.
4. **Always include the no-prime baseline** as the control.

A pre-filter selects 3 candidates + 1 baseline = the standard tournament size.

### Risk profile

| Risk | Mitigation |
|------|------------|
| Tournament winners overfit to one representative scene; the cache is mis-applied to other scenes | Per-chapter cache scope (not per-book or per-project on first deployment). Larger-scope caching deferred until the per-chapter shape proves. |
| Tournament becomes mandatory and blocks production when API outages spike | Make the tournament soft-fail: if the tournament can't complete in N minutes, fall back to the prior cache or the library default. Production runs even when tournament can't. |
| Library exemplar quality is uneven; the tournament keeps picking "least bad" rather than "good" | Reportable: the tournament's report includes the rank-1 score and the spread. If rank-1 is < threshold, surface to margit for exemplar-library improvement. |
| User loses ability to manually pin a chosen exemplar | Manual override always wins: if the per-chapter cache file's tail comment says `selected-via: manual`, no tournament fires for that scope. |
| Tournament dispatch cost compounds if every gate-failure re-fires the tournament | Add cooldown: a re-tournament can fire at most once per N chapters or per cascade-checkpoint, not per gate-failure. |

### Deployment plan

1. **Phase 1 (immediate-target):** wire the renderer-voice tournament at `/and-stitch` Phase 0 step 4a. Smallest blast radius, the cache slot already exists, the experimental evidence is concentrated here. Add a `--exemplar-tournament=skip|force|cached` flag to /and-stitch.
2. **Phase 2 (after 3+ chapters validated):** wire the impersonator-tournament at the per-character per-book scope. Requires a new `active-project/persona-exemplars/<slug>-<book>.md` cache slot.
3. **Phase 3 (deferred):** audience-tournament. Lowest variance per the existing experiments; lowest priority.
4. **Phase 4 (deferred):** auto-promote winners to project-default (`active-project/voice-exemplar.md`) after K chapters of consistent winning. Manual promotion only at first deployment.

## What this proposal does NOT do

- Does NOT mandate tournaments at Tier-2 (orchestrator-critic, dramatist, auditor, editor). The 2026-05-26 critic-experiment empirically showed exemplar priming actively regressed Tier-2 output; tournaments would amplify the regression.
- Does NOT mandate tournaments at Tier-3 (showrunner, margit, fixer). No persona/voice channel; nothing to tournament.
- Does NOT add a tournament inside the full /and-stitch pipeline. The pipeline runs once on the cached winner; tournaments live at the cheap-layer (renderer-minimal / impersonator / audience-fork) where parallelization is affordable.
- Does NOT change the manual-override path. Users who want a specific exemplar pin it via the existing per-chapter override and tournaments respect that.
- Does NOT introduce a tournament across architectures (impersonator vs renderer-minimal vs audience-fork — apples to oranges; tournaments are within-architecture).

## Open questions for the principal

1. Does the candidate pool include **cross-persona transfer** (impersonator exemplars competing for renderer-voice slots)? The c02 experiment proved the lift is real, but it expands the library's effective surface area substantially. Default: yes, with POV-pre-filter as guardrail.
2. Should the cold-read judge be a single agent or a multi-judge aggregation (audience-trio + cold reader)? Single agent matches the experiment methodology and is cheapest; multi-judge gives more signal at higher cost. Default: single agent for Phase 1 deployment; aggregate only at project-default promotion.
3. Where does the cache invalidate when the upstream content changes? Cache the bones-file-content-hash in the per-chapter cache file's tail; re-fire tournament when the hash changes.
4. Should the tournament fire **before** Phase 0.5 pre-flight (so the user sees the chosen exemplar at the pre-flight summary) or **after** (the user sees the tournament happen if cache is missing)? Default: before, with cache-hit signal in the pre-flight summary.

## Next steps

If accepted:
- Author the formalized proposal as a PROP entry in `staff/admin/process-proposals.md` (admin in process-critic mode; user can dispatch admin directly with `mode: process-critic`, `trigger.reason: on-demand`).
- Spec the renderer-voice tournament at `/and-stitch` Phase 0 step 4a as a sub-step (4a.1: resolve candidates; 4a.2: tournament if cache miss; 4a.3: use cache).
- Author the role-fit-criteria judge-prompt for renderer voice at `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md` (template for the cold-read methodology used in the c02 experiment, generalized).
- Decide cache-scope policy (per-chapter default; promotion to project-default after K consistent winners).

This proposal is **research output**, not a chain-authored process-proposal. The principal can promote it into `staff/admin/process-proposals.md` via admin process-critic dispatch (or accept it directly).
