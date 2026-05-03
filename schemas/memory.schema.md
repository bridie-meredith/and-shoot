# Memory Schema

Four-part memory format for actors and studio. All parts optimized for Claude consumption.

Each part lives in a separate file within the entity's working directory. Actors live under `active-project/actors/<slug>/`. Studio lives under `active-project/staff/studio/`.

---

## LTM — Long-Term Memory

File: `ltm.md`

Append-only change log. One entry per meaningful event. Oldest entries at bottom. Never truncated or pruned — this is the full history of what this actor or studio has experienced across the project.

Write authority: impersonator (for actors) at episode close, or when a single line carries genuinely accreted content (relationship shift, new residue, arc note). Studio writes at episode close for major set changes.

```
[YYYY-MM-DD] EVENT: what changed | why significant
[YYYY-MM-DD] EVENT: what changed | why significant
```

Example:
```
[2026-05-03] RELATIONSHIP: turned against Mira after the knife scene | trust broken permanently
[2026-05-02] DISCOVERY: learned the compound has a second exit | changes all prior escape planning
```

---

## STM — Short-Term Memory

File: `stm.md`

Recent and notable happenings, most recent first. Pruned to approximately 10 items at each episode close — keep only what is genuinely on top of mind going into the next scene. Overwritten (not appended) at each episode close.

Write authority: impersonator (for actors) at episode close. Studio at episode close.

```
STM:
- [most recent notable thing]
- [second most recent]
- ...
```

Example:
```
STM:
- Mira walked out of the argument without resolving it
- The east door is barred from the inside now
- Running low on ammunition — 4 rounds left
- Hasn't eaten since yesterday; starting to feel it
```

---

## State

File: `state.md`

Flat snapshot of current state. Overwritten on each change during a shoot. This is what is true right now, not a history.

Write authority: impersonator updates actor state after each line. Studio updates set state after each studio bullet.

Nothing changes without being recorded here. If the state file doesn't reflect a change, the change did not happen.

```
STATE:
  location: <location-slug>
  condition: [list of active condition slugs]
  inventory: [list of prop slugs currently held]
  stats:
    <key>: <value>
```

Stats are optional and only tracked for actors where it matters (health, ammo, stamina, etc.). Omit the stats block entirely if not needed.

Example:
```
STATE:
  location: warehouse-east-wing
  condition: [low-light, post-fight-tension]
  inventory: [glock-17, burner-phone]
  stats:
    health: wounded
    rounds_remaining: 4
```

Studio state file tracks set state rather than actor state:
```
STATE:
  active_location: <slug>
  active_conditions: [list]
  prop_positions:
    <prop-slug>: <location or "held by <actor-slug>">
  time_of_day: <value>
  weather: <value>
```

---

## Vibe-Cloud

File: `vibes.md`

Dictionary of key-things → list of associated vibes. Scoped to the planning level that created it (series, season, or episode). A new vibe-cloud is built at the start of each planning level and may be updated on significant shift.

Vibe-clouds are not personal state — they represent what the world or episode is charged with. Actors and studio receive the relevant vibe-cloud in their context.

```
VIBES:
  <key>: [vibe, vibe, vibe]
  <key>: [vibe, vibe]
```

**How agents use vibe-clouds:**
When an agent (impersonator, studio, screen-writer) receives a prompt, it checks its input and planned output against the vibe-cloud keys. If a key seems relevant — even loosely — the associated vibes are surfaced as a bias/nuance layer. The relevance match is the agent's judgment call; it acts as a scalar on how hard the vibes push. High relevance: the vibes actively shape the output. Tangential: a light tint, not a rewrite.

Vibes do not override character cards or constraints. They bias and color within what is already permitted.

Example:
```
VIBES:
  blood: [violence, tension, consequence, urgency]
  fire: [destruction, passion, recklessness, danger]
  door: [threshold, choice, irreversibility, opportunity]
  name: [identity, legacy, burden, pride]
  dark: [concealment, fear, unknown, isolation]
```

**Write authority:** Showrunner builds the vibe-cloud at each planning level. Screen-writer and showrunner may update on significant shift. Individual actors and studio do not write their own vibe-clouds — they receive and consume the current level's cloud.

**Scope:** The vibe-cloud at the episode level is the active one during shoot. It inherits from (but does not replace) the season and series clouds — all three levels' vibes are available, with the episode-level cloud taking priority on key conflicts.
