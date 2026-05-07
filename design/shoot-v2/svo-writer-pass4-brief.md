# Pass 4 — Trim Brief (audience, 3 personas)

Dispatch template for the trim pass. Three persona dispatches in parallel after pass 3 returns CLEAN.

## Role

**Agent:** audience (one dispatch per persona — pulp-enthusiast, worm-canon-pedant, dark-fantasy-reader, or whatever 3 are active in `active-project/audience/`).
**Mode:** trim-judge + entertainment verdict.
**Output:** per-persona deletion proposals + per-persona file-level verdict.

## Authority

You may **propose deletions**. You may NOT add lines, re-order, or rewrite. Each persona authors their own proposals independently; orchestrator aggregates.

## Inputs to load (per persona)

- The re-shaped file from pass 3: `active-project/theater/proto-lines.md`.
- The episode `goal` from the file header (the north star).
- `active-project/audience/<your-persona>/card.md` — your taste, your blindspots, what you are paid to want.
- `active-project/audience/<your-persona>/stm.md` — your working context (carry across iterations).
- `series.theme`, `series.behaviors` (one-liners from showrunner memory).
- Episode `theme` from `active-project/theater/episode-plan.md`.
- **Full prose** of `active-project/staff/showrunner/series-plan.md` and the active season plan (taste decisions need tonal context).
- Per-actor vibes for the active cast: `active-project/actors/<slug>/vibes.md` (which beats the actor's voice will load with meaning).
- Studio vibes: `active-project/staff/studio/vibes.md` (pacing register).
- Behavior cards: full inheritance stack for the active cast (which beats are voice-load-bearing).

## Inputs FORBIDDEN

- Raw constraint cards (already enforced).
- The harsh-SVO calls list (already enforced).
- Past shoot artifacts.

## Trim test (per line)

For each numbered, non-blank line in the body, ask:

1. **Does this line serve the chapter `goal`?** — direct contribution to what the chapter shows.
2. **If not, is it voice-load-bearing per the actor's behavior signature?** — does the actor's voice render this beat in a way that carries weight (e.g. a Taylor hold-against-pressure, a Plumm administrative gesture, a Septon Rowan ritual deflection)?

Decision tree:
- YES to (1) → keep, no proposal.
- NO to (1) and YES to (2) → keep, no proposal.
- NO to (1) and NO to (2) → propose deletion with one-clause reason.

Time-skip blank lines are not trimmed at this pass — leave them alone.

## File-level verdict

After per-line proposals, produce a file-level verdict:
- **ACCEPT** — the sequence reads as the chapter; no further deletions, no entertainment problem.
- **REVISE-{one-clause-reason}** — there is an entertainment problem the deletions alone cannot solve (a beat is missing, the rhythm fails, the chapter goal is not delivered by what's there).

REVISE verdicts route back to screen-writer (via orchestrator) for targeted addition; then pass 2 re-runs on additions; then pass 3 may re-evaluate; then pass 4 re-runs.

## Output format (per persona)

```
# Pass 4 Trim — <episode-slug> — <persona-slug>

## Deletion proposals
<line-id> | <line-content> | <one-clause reason>
...

## File-level verdict
<ACCEPT | REVISE-{reason}>
```

## Aggregation (orchestrator-side)

- ≥2 personas propose deleting the same line → auto-accept the deletion.
- 1 persona proposes a deletion → advisory; orchestrator decides (default: keep unless line is also weakly defended).
- All three personas ACCEPT at file level → pass 4 terminates.
- Any REVISE → fix the named entertainment problem; re-run pass 4. Maximum 2 revise rounds; on the third, ship the file with audience flags annotated as comments at end of file and surface for human review.

## Termination

All three personas ACCEPT in one round, with ≥2-persona deletions applied.
