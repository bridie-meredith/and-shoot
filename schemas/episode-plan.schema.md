# Episode Plan Schema

The episode plan is the script for one episode. It lives at `active-project/theater/episode-plan.md` and is written by screen-writer, reviewed by audience and dramatist, and approved by showrunner before shoot begins.

---

## Format

```markdown
# Episode Plan

chunk: <chunk statement from season plan — what this episode delivers to the season arc>
theme: <episode theme — one line>
actors: [<actor-slug>, <actor-slug>, ...]
change: <expected change by end of episode — what is different from the start>
constraints: [<constraint slug or one-line statement>, ...]

---

## Script

- STUDIO: <set formation or state change description>
- <actor-slug>: <action or dialogue — one line>
- <actor-slug>: <action or dialogue — one line>
- STUDIO: <environmental change>
- <actor-slug>: <action or dialogue>
...
```

---

## Field notes

**chunk** — goes first. This is the single thing this episode must accomplish for the season plan. If the episode doesn't deliver this, it has failed regardless of its quality. Pulled verbatim from the season plan's episode chunk statements.

**theme** — the emotional or thematic register of this episode. One line. Used by screen-writer, studio, and impersonators as a vibe-orienting anchor.

**actors** — list of actor slugs active in this episode. These are the impersonators that will be spawned. Actors not on this list do not appear. Studio is always implicitly active and does not appear in this list.

**change** — the expected delta. What is true at end that was not true at start, or vice versa. At least one meaningful change must be achievable from this plan. Used by dramatist to check the episode delivers its chunk.

**constraints** — active constraints from law, lore, or behavior cards that specifically impact this episode's actors and set. Not the full series constraint list — only the ones relevant here. Auditor checks against these.

---

## Script format

Each bullet in the script = exactly one line in the show file.

**Line types:**
- `STUDIO: <description>` — studio records a state change to the set and environment. Studio writes to its own state files. Showrunner then identifies the POV actor and issues a perception prompt through coach. The actor describes the environment through their own perception. Studio does not write directly to the show file.
- `<actor-slug>: <content>` — actor performs a dialogue line or action. Impersonator appends to show file.

**Granularity rule:** Each bullet is a single beat — one thing that happens. Not a scene, not a paragraph. One dialogue exchange, one action, one environmental change. If a bullet describes multiple things, split it.

**Ordering:** Script bullets are in sequence. Showrunner executes them in order. No skipping, no reordering during shoot.

---

## How episode plans are built

1. Showrunner passes the episode's chunk statement and active constraints to screen-writer.
2. Screen-writer expands the chunk into a detailed script (bullet list, scene by scene).
3. Audience and dramatist review in parallel:
   - Audience reviews for entertainment shape — what lands, what falls flat.
   - Dramatist reviews for structural integrity — rise-peak-fall, meaningful change, chunk delivery.
4. Screen-writer revises based on feedback. Both must accept, or three attempts are exhausted.
5. If three attempts exhausted: proceed with most recent plan, flag for human review.
6. Approved plan → showrunner. Showrunner reads bullets and begins shoot.
