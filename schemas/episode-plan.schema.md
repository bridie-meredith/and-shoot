# Episode Plan Schema

The episode plan is the script-level prep for one episode (or chapter, under shoot-v2 season-decomposition). It lives at `active-project/theater/<slug>/episode-plan.md` and is written by screen-writer, reviewed by audience and dramatist, and approved by showrunner before the proto-line authoring pipeline runs.

Schema authority: this file. Under shoot-v2, the script-bullet body is **deprecated** — the proto-line file (per `schemas/proto-line.schema.md`) replaces both the old script section and the show file.

---

## Format (shoot-v2)

```markdown
# Episode Plan

chunk: <chunk statement from season plan — what this episode delivers to the season arc>
change: <expected change by end of episode — what is different from the start>
theme: <episode theme — one line>
actors: [<actor-slug>, <actor-slug>, ...]
constraints: [<constraint slug or one-line statement>, ...]
narrator: <actor-slug>
goal: <one sentence — what this episode shows the audience>
interlude: <true | false>
```

All eight fields are **required** under shoot-v2. Default narrator is the series protagonist (`taylor-hebert-westeros` for the active project) in first person; any chapter whose narrator is not the protagonist must set `interlude: true`. Interlude chapters are read by the dramatist and audience as deliberate POV deviations and are exempt from the cross-chapter narrator-consistency check that otherwise enforces protagonist POV. The `narrator` and `goal` fields propagate to the proto-line file's header (per `schemas/proto-line.schema.md`).

A legacy `## Script` section may exist in older episode-plans (s01e01–s01e06 from shoot-v1). It is read for header content only; the body bullets are deprecated and ignored by shoot-v2 dispatches.

---

## Field notes

**chunk** — goes first. The single thing this episode must accomplish for the season plan. If the episode doesn't deliver this, it has failed regardless of its quality. Pulled verbatim from the season plan's per-episode chunk paragraph.

**change** — the expected delta. What is true at end that was not true at start, or vice versa. At least one meaningful change must be achievable from this plan. Used by dramatist to check the episode delivers its chunk.

**theme** — the emotional or thematic register of this episode. One line. Used by screen-writer, studio, and impersonators as a vibe-orienting anchor.

**actors** — list of actor slugs active in this episode. These are the impersonators that will be spawned. Actors not on this list do not appear. Studio is always implicitly active and does not appear in this list.

**constraints** — active constraints from law, lore, or behavior cards that specifically impact this episode's actors and set. Not the full series constraint list — only the ones relevant here. Auditor checks against these at Pass 2.

**narrator** — single actor slug. The POV character for this episode. Pass 5 (continuity) enforces narrator-consistency: lines whose content cannot be observed from this POV fault. The proto-line file inherits this header verbatim.

**goal** — one sentence. The episode's north star. Pass 4 (trim) walks every line against this goal; lines that don't serve it are deletion candidates. The proto-line file inherits this header verbatim.

---

## Authoring (shoot-v2)

1. **Series/season planning** establishes the episode's chunk in `season-<slug>-plan.md`.
2. **Screen-writer (in season-decomposition mode)** authors the episode-plan with all seven required fields. Inputs: series-plan, season-plan, series.theme + laws + lore, active cast roster, active stage_elements, the per-episode chunk paragraph. Forbidden: past shoot artifacts.
3. **Dramatist** reviews structural integrity — rise-peak-fall, meaningful change, chunk delivery, narrator/goal coherence. Strict bias: if the chapter has no identifiable buildup/climax/denouement structure, dramatist flags `STRUCTURAL-FAILURE` and routes back to screen-writer.
4. **Audience** is not invoked at episode-plan authoring under shoot-v2 — taste calls happen at proto-line review (Pass 4).
5. **Approved plan → orchestrator.** `/and-protolines` reads this file and runs the five-pass proto-line pipeline against it.

---

## What the legacy `## Script` section is (and why it's deprecated)

Under shoot-v1, the script body was a bullet-list of `STUDIO: ...` and `<actor-slug>: ...` lines that showrunner walked during `/and-shoot`. Each bullet → exactly one show file line. This pattern is replaced under shoot-v2 by the proto-line file: the SVO bone-structure of the episode, authored through a five-pass pipeline, with facets attached at facet-authoring time. Show file authoring becomes a stitcher pass over proto-lines + facets, not a sequential impersonator-coach loop.

Existing s01e01–s01e06 episode-plans retain their `## Script` sections as historical record. They are not consumed by shoot-v2 dispatches and are explicitly forbidden inputs to writer dispatches. New episode-plans authored under shoot-v2 do not include a `## Script` section.
