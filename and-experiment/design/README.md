# Bones-first ingest — design notes

**Status:** manual prototype (no command yet). Goal: run the reverse-derivation by
hand on one real narrated story, learn what the narration must capture, then codify
into `/and-ingest` + a seed schema.

**Decisions (2026-06-04):**
- Full substance reverse-derivation (not polish-only). The signature — state axes,
  cost ledger, per-scene `substance_delta`/`scene_conflict`, actor baselines — is
  inferred from the narrated bones so the substance bone-gate and the
  substance-awareness inside facets/stitch all run as designed.
- Prototype manually first; codify after one real run.

---

## The inversion

Stock chain is top-down: `substance → write → bones → facets → stitch`.
Bones-first inverts the top half only. Everything **below** the bones file is
direction-agnostic — `/and-review bones`, `/and-facets`, `/and-stitch` consume the
bones file + apparatus and don't care how the bones were authored. So:

- **Reused unchanged:** `/and-review bones`, `/and-facets`, `/and-stitch`, all staff
  agents (margit, screen-writer, auditor, showrunner, studio, audience, editor).
- **Net-new:** a front-end that ingests narration and back-fills apparatus, then
  hands off at `/and-review bones`.

`/and-write` is *generative* (contracts → bones). The bones-first front-end is
*reconstructive* (bones → contracts). It reuses `/and-write`'s Phase 2–5 SVO
cleanup discipline and Phase 7 emit, but replaces Phase 1 decomposition + Phase 6
gate with reverse-derivation + a reconciliation check.

---

## Two stages

### Stage 1 — Narrate (any session; "regular cloud")
Free narration → captured into a loose **story seed** doc (plain markdown, portable).
No schema discipline yet; faithful capture + one cleanup pass.

### Stage 2 — Ingest + polish (in and-shoot, own scratch project)
`/and-ingest <seed>` (eventual). Manual steps for the prototype:

| Step | Agent | Output | Maps to stock |
|------|-------|--------|---------------|
| 2a entity extraction | margit + screen-writer | persona/location/prop/condition cards; `actors/` + `warehouse/` | `/and-project` 1a–1d + `/and-cast` 4 |
| 2b bible synthesis | screen-writer | series chunk + structure + laws + lore | `/and-series` |
| 2c substance reverse-derivation | screen-writer + auditor | `state_axes[]`, `cost_ledger[]`, `antagonist_pressure[]`, `actor_baselines[]`, per-scene `substance_delta` + `scene_conflict` | `/and-substance series`+`book`+`chapter` (INVERTED) |
| 2d bones cleanup | SVO passes from `/and-write` 2–5 + 7 | schema bones file + dialogue files + scene-map | `/and-write` |
| 2e reconcile | auditor | bones↔derived-contract consistency (replaces forward bone-gate) | `/and-write` Phase 6 (inverted) |
| 2f memory write | showrunner | showrunner memory looks like a normal project | continuous |
| → handoff | — | enter stock `/and-review bones → /and-facets → /and-stitch` | unchanged |

---

## Provisional seed format (to be validated/revised by the manual run)

The narration must carry enough signal for 2c to infer axes without hallucinating.
First guess at required capture per scene:

```
# <story title>
premise: <2–3 sentences — what the story is about>
pov: <whose head we're in> | <1st|3rd> | <past|present>

## cast
- <name>: <one-line who they are; what they want; what they can't do>

## world
- setting: <where/when>
- laws: <hard rules of the world the prose must not violate>

## scenes (in order)
### s01 — <one-line>
- where: <location>  when: <time>
- present: <names>
- beats:
  - <plain-language beat: who does what to whom, what changes>
  - <...>
- what-changes: <the ONE thing different by scene end — the candidate axis move>
- pushes-for / pushes-back: <protagonist force vs opposing force>   # seeds scene_conflict
- cost (if any): <what was given up to get the change>              # seeds cost_ledger
```

**Open questions the manual run must answer:**
- OQ1 — Can axes be inferred from `what-changes` lines alone, or does the narrator
  need to name the axis vocabulary up front?
- OQ2 — Cost ledger is the hardest inference. Is `cost (if any)` per scene enough,
  or do we need an explicit "this cost that" link?
- OQ3 — Granularity: does the narrator give scenes, or a continuous stream we have
  to segment? (Segmentation = a new step if so.)
- OQ4 — How much cast/world detail is load-bearing vs. inventable by margit?
- OQ5 — Does reconcile (2e) catch enough, or do we need a human checkpoint on the
  derived signature before spending on facets?

## Scratch project location
Manual prototype runs under `and-experiment/design/run-01/` — NOT `active-project/`
(which is live, b01 shipped through c16).
