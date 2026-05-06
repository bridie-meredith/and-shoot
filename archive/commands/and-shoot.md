---
description: Run a full episode shoot: expand the active episode chunk to a bullet plan, then write the show file line by line. Produces the raw show file. Phase 0 auto-archives the previous shot episode. Wrap is opt-in (run /and-wrap later, single or bulk). Usage: /and-shoot [episode-slug]
---

Takes the active episode chunk from showrunner memory and produces a raw show file in `active-project/theater/show.md`. Covers two phases: episode start (plan) and shoot (show file). Wrap is a separate command.

You are the orchestrator for this command. You dispatch subagents directly — coach, impersonator, studio, screen-writer, audience, dramatist. Do not dispatch showrunner. Showrunner is not in the orchestration chain here.

**All dispatches use the Agent tool.** Inline generation is not a valid substitute. An impersonator not spawned in its own isolated context will not produce character-true output — it will produce the orchestrator's voice wearing a label.

## Args

- `$1` — optional episode slug (e.g., `s01e01`). If omitted, shoots the episode currently marked active in `active-project/staff/showrunner/memory.md`. If provided, must match a slug in the season plan.

---

## Phase 1 — Validate

Read `active-project/staff/showrunner/memory.md`. Confirm:
- `active.season` is set
- `active.episode` is set (or matches `$1` if provided)
- The episode's status in the season plan is `planned` (not already `complete` or `wrapped`)
- The season plan file for the active season exists

Read the active season plan file (path is in memory under `routing.season_plan`) and the series plan (`routing.series_plan`). Both must be in context before episode planning begins.

If anything is missing or the episode is not in `planned` status, print the problem and stop.

Also check: if `active-project/theater/show.md` already exists with content beyond the header (more than 4 lines), stop and print:
```
show.md already has content — episode may have been interrupted mid-shoot.
Review active-project/theater/shoot-log.md to see which bullets completed.
Delete show.md and shoot-log.md manually to restart from scratch, then re-run /and-shoot.
```

**Archive integrity check.** For every episode in the season plan whose status is `shot` or `wrapped`, verify a corresponding archive directory exists at `active-project/theater/<slug>-archive/` containing at minimum `show.md` and `shoot-log.md`. If any are missing, stop and print:
```
Archive missing for <slug>. Previous episode theater files were not preserved.
This is the skip-wrap drop-the-floor failure mode — show.md was overwritten by a later episode prep.
Recover from git history before starting a new shoot:
  git log -- active-project/theater/show.md       # find the end-of-shoot commit for <slug>
  git show <sha>:active-project/theater/<file>    # extract each file into theater/<slug>-archive/
```
Do not override this guard by deleting the half-state.

---

## Phase 0 — Auto skip-wrap (default)

**Wrap is opt-in. The default flow is shoot → shoot → shoot, with /and-wrap deferred for bulk wrapping later.** When /and-shoot starts, the previous episode's theater files are still sitting in `active-project/theater/`. Phase 0 archives them before Phase 1 runs.

Sequence:

1. Read `active-project/staff/showrunner/memory.md`. Find the most recent episode with status `shot` (not yet `wrapped`). Call this `<prev-slug>`.
2. If `<prev-slug>` exists and `active-project/theater/<prev-slug>-archive/` does **not** exist:
   - Create `active-project/theater/<prev-slug>-archive/`.
   - Move all four theater working files into the archive: `show.md`, `shoot-log.md`, `episode-plan.md`, `episode-plan-log.md`. Use `git mv` so history follows.
   - Commit with message: `skip-wrap: archive <prev-slug> theater files; advance to <new-slug>`.
3. If no `shot` episode exists (first episode of the project) or its archive already exists, Phase 0 is a no-op.

Phase 0 must succeed before Phase 1's archive integrity check runs. If Phase 0 detects ambiguity (e.g., multiple `shot` episodes without archives, or theater files that don't match any `shot` episode), stop and surface the state to the human rather than guessing.

Wrap is invoked explicitly with /and-wrap (single episode) or in bulk later. /and-shoot never calls wrap.

---

---

## Phase A — Episode Start

At each step that dispatches a subagent, record the result in the log file for that step before continuing. A missing log file means the step did not run.

**A1. Episode plan — expand chunk to bullets.**
1. Take the episode chunk statement for the active episode from the season plan.
2. Dispatch screen-writer with: the chunk, the series constraints (laws/lore/behaviors from memory), the season drama statement, and the active vibe-clouds (series + season from `active-project/staff/studio/vibes.md`). Screen-writer produces a detailed ordered bullet list — one bullet per show-file line, scene by scene. Every bullet must be legible against both the series plan and the season plan. **Bullet format: action beats only — `[subject] [verb] [object/location]`. No motivation clauses, no because/since/wanting-to, no internal state embedded. If the bullet tells the impersonator what the character is thinking or why they act, the bullet is wrong. The impersonator supplies interiority — the bullet supplies the beat.**
3. Dispatch audience and dramatist in parallel to review the bullet plan. Run accept/revise loop (3-try max).
4. Write the accepted plan to `active-project/theater/episode-plan.md`.

**Log file: `active-project/theater/episode-plan-log.md`**
One block per attempt:
```
## Attempt N
audience verdict: <accept/revise> — <one line reason>
dramatist verdict: <accept/revise> — <one line reason>

## Final verdict: accepted at attempt N  [or: exhausted — proceeding with attempt 3]
```

**A1b. Walk-on card check.**
After the bullet plan is accepted, scan all bullets for characters who appear on-stage with lines (actor bullets, not STUDIO bullets). For each named character, verify a persona card exists — either in `cards/personas/` or `active-project/actors/<slug>/card.md`. Any character introduced by screen-writer who does not have a card is a walk-on gap. Dispatch margit to create a `quality: full` persona card for each gap character before the shoot begins. A character with on-stage lines cannot be shot without a card — `quality: scant` fails the persona quality gate for on-stage use. Walk-on cards default to `tier: minor` (spawns with `model: haiku`) unless the character is pivotal enough to the episode's dramatic pressure to warrant a higher tier — in which case showrunner assigns `tier: supporting` or `tier: lead` before provisioning.

**A2. Derive episode vibe-cloud.**
Derive the episode vibe-cloud from the bullet plan and the series/season vibes. Append an episode-level section to `active-project/staff/studio/vibes.md`. Do not overwrite the series or season sections.

**A2b. Refresh actor vibes.**
For each actor active in this episode: check whether the episode vibe-cloud introduces keys that are absent from their `active-project/actors/<slug>/vibes.md`. If the episode activates something new for this character — a new location, a new relationship state, a new pressure — add the key with character-specific associations. Do not overwrite existing keys unless the character's relationship to that key has genuinely shifted. This is an additive pass, not a rebuild.

**A3. Prep cast.**
For each character active in this episode: confirm their actor dir exists at `active-project/actors/<slug>/`. Build a routing map (internal — not a file) of which characters appear in which scenes, drawn from the bullet plan. For each character, read their `tier` field from `active-project/actors/<slug>/card.md` and record the corresponding model in the routing map:
- `tier: lead` or absent → `opus`
- `tier: supporting` → `sonnet`
- `tier: minor` → `haiku`

**A4. Prep studio.**
Dispatch studio with the episode's opening location (from the bullet plan). Studio reads the relevant location card from `active-project/warehouse/`, reads any relevant prop and condition cards, and writes the initial environment state to `active-project/staff/studio/state.md`. Studio also writes the scene-open prompt plan to `active-project/staff/studio/stm.md` — the environmental detail the opening POV impersonator will be asked to perceive.

**A5. Open show file.**
Write the show file header to `active-project/theater/show.md`:
```
episode: <slug> — <Episode Title from season plan>
chunk: <chunk statement>
audience: <slug-1>, <slug-2>, <slug-3>
opened: <date>
```
Plain text only — no markdown. The show file is now open. It is append-only until shoot is complete.

**A6. Confirm audience.**
Verify all three audience persona cards exist at `active-project/audience/<slug>/card.md`. Note their slugs for the shoot loop.

---

## Phase B — Shoot

Open `active-project/theater/shoot-log.md` with a header:
```
# Shoot Log — <episode-slug>
# bullets: <total count from episode plan>
```

For each bullet in the episode plan (in order):

**B1. Identify recipient.**
- Actor line → identify which character's impersonator receives the prompt.
- Environment line → studio records the state change first; the POV impersonator perceives it after.

**B2. Studio first (environment lines only).**
Dispatch studio with the state change. Studio updates `active-project/staff/studio/state.md` and returns the updated prompt plan for the POV character's perception.

**B3. Dispatch coach.**
Pass to coach: the bullet, the recipient slug, the current studio state (from `active-project/staff/studio/state.md`), the last few lines of the show file for continuity, and the recipient's STM path (`active-project/actors/<slug>/stm.md`). Coach produces a prompt addressed to the impersonator. **Coach must translate the bullet to what the character *perceives* at this scene-moment — not paraphrase the bullet text. The prompt opens with the character's experience, not a summary of the action.**

**B4. Dispatch impersonator.**
Dispatch the impersonator for the recipient character. Pass: the coach prompt, the character card (`active-project/actors/<slug>/card.md`), their LTM, their current STM and state, and the episode vibe-cloud. Use the model recorded for this character in the routing map from A3 (`opus` / `sonnet` / `haiku`). The impersonator performs and returns a line. Append the line to `active-project/theater/show.md`.

If the impersonator rejects the prompt (impossible or out of character): note the reason. Dispatch coach with the rejection + original bullet. Coach reformulates. This consumes one try.

**B5. Audience review.**
Dispatch all three audience agents in parallel. Each reads the new line in context of the last few lines of the show file. Each returns accept or reject with a one-line reason. Aggregate: if any audience agent rejects, the line is rejected.

- **Accept:** proceed to next bullet.
- **Reject:** delete the last line from `active-project/theater/show.md`. Dispatch coach with the original bullet + all three audience verdicts. Coach revises the prompt. Return to B4. This consumes one try.

**Three-try budget:** shared across all failure types for the line (audience rejects + impersonator rejects). If budget exhausted: keep the most recent line as-is, mark it `[⚑ needs edit: <reason>]` in the show file, move to next bullet.

**Append to shoot-log.md after each bullet:**
```
## Bullet N — <recipient slug> — <one-word scene label>
attempts: N | outcome: clean / retried / NEEDS_EDIT
[if retried or NEEDS_EDIT: one line per attempt — who rejected and why]
```

**Actor state after each line:** if the impersonator's action implies a state change (moved, picked up object, emotional shift), update `active-project/actors/<slug>/stm.md`. Environmental state changes go to studio → `active-project/staff/studio/state.md`.

**Inventory carry-forward is absolute.** An item in an actor's `state.md` inventory persists into every subsequent line unless the line explicitly transfers, drops, or destroys it. A wound persists and heals on a realistic timeline — it does not disappear between scenes. If the impersonator's line implies an inventory item that is not in `state.md`, add it. If the impersonator's line implies an item is gone but no action removed it, that is a continuity fault — flag it rather than silently accepting the line.

**Continue until all bullets are complete.** Do not stop for single-line problems — mark and move on.

---

## Phase C — Close and present

Mark the episode status as `shot` in `active-project/staff/showrunner/memory.md` (seasons[].episodes[].status). Do not advance `active.episode` yet — that happens in wrap.

Present to the human:

```
--- SHOOT COMPLETE: <episode-slug> ---

PLAN
  Bullets: N | Accepted at attempt: N

SHOOT
  Clean: N | Retried: N | NEEDS_EDIT: N

RAW SHOW FILE
  active-project/theater/show.md

LOG FILES
  active-project/theater/episode-plan-log.md
  active-project/theater/shoot-log.md

[Shoot complete. Theater files will auto-archive at the start of the next /and-shoot. Run /and-wrap (single or bulk) when ready to close.]
```

If there are escalations requiring human decision, present them before the closing line with: `ESCALATIONS REQUIRING YOUR DECISION:` followed by each one.

---

## Notes

- Impersonators are dispatched per-line during shoot, not pre-spawned. Route from the cast routing map built in A3.
- Studio is dispatched before coach on environment lines — coach needs updated state to compose a valid prompt.
- The show file is append-only during shoot. Rejected lines are deleted before retry. The file never accumulates failed attempts.
- Audience agents run in parallel per line. All three verdicts return before proceeding.
- The shoot log is the shoot's audit trail. Every bullet gets an entry regardless of outcome.
- Episode status is set to `shot` on return. Wrap reads this status before it will run.
