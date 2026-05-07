# Pass 1 — Inventory Brief (screen-writer)

Dispatch template for the inventory pass of the svo-writer pipeline. Run by `/and-protolines-v2` against the active episode.

## Role

**Agent:** screen-writer.
**Mode:** inventory authoring (not script bullets, not prose, not facet citations).
**Output:** `active-project/theater/proto-lines.md` — complete file including header.

## Bias

Coverage > economy. Over-generate. Pass 4 will trim. A missed beat is a worse failure than a redundant one because adding lines requires routing back to you; pass 4 deletes are cheap and atomic.

## Inputs to load

**Episode-specific (orchestrator substitutes per dispatch):**
- `narrator` slug (e.g. `taylor-hebert-westeros`)
- `goal` (one-sentence statement of what this chapter shows)
- Episode `chunk` (verbatim from `active-project/theater/episode-plan.md`)
- Episode `change` (start vs. end delta; verbatim)
- Active cast roster (slug list from episode-plan `actors` field)

**Reference (load once):**
- `schemas/proto-line.schema.md` — output schema.
- The harsh-SVO rules below (this file's §"SVO discipline").
- `design/shoot-v2/svo-split-notes.md` — 15 ambiguity calls, especially perception-verb deny-list and holds-as-positive-SVOs.
- Active constraint card slugs (from episode-plan `constraints` field). Slug list only.
- Active location cards under `active-project/warehouse/loc-*.card.md` — full content, used as set authority (what props are present, what exits exist, what hazards constrain action).

**Showrunner memory (one-liners only):**
- `series.theme`, `series.laws`, `series.lore`, `series.behaviors` — load as the brief one-line entries from `active-project/staff/showrunner/memory.md`. Do not load the full prose of `series-plan.md` or `season-plan.md`.

## Inputs FORBIDDEN

You must not read:
- `active-project/theater/show.md` (any prose show file).
- `active-project/theater/s01e*-archive/` (archived prose show files).
- `active-project/theater/proto-lines/s01e0*.md` (rough-pass extracted reference proto-lines for previous episodes).
- The script section of `active-project/theater/episode-plan.md` (deprecated v1 shoot bullets). Read `chunk`, `change`, `theme`, `actors`, `constraints` only.
- Behavior cards (`cards/dialects/`).
- Actor vibes (`active-project/actors/<slug>/vibes.md`).
- Audience persona cards.
- Series-plan or season-plan full prose.

These are either downstream-pass inputs or shoot-artifact contamination. Reading them biases your authoring toward what already exists rather than what the chunk requires.

## SVO discipline

A proto-line is **a subject doing something, optionally to object(s)**. Subject action, never subject non-action.

- **Subject** — exactly one named entity (actor slug from cast roster, prop slug from a location card, or `the <noun>` for unnamed environment elements).
- **Verb** — exactly one concrete physical action.
- **Object(s)** — zero or more named or quantified things acted upon. Multiple objects under one verb only when the action acts on the set as one physical event (`Plumm gathers the page, the stylus, the seal`); otherwise split.
- **Object-as-subject form permitted** when the actor is unknown / ambient / unspecified (`the page tears`, `the door swings open`, `the bell rings`); optional `by <slug>` tail when naming the actor matters.
- **No modifiers** — no adjectives, no adverbs, **no prepositional padding of any kind.** This rule is the most over-violated. Phase 2 of pipeline tuning showed the most common writer failure is leaking prepositional phrases of *place, destination, source, direction, instrument, or accompaniment* onto otherwise-clean SVOs (`moves to the yard`, `lift from the bell tower`, `steps through the gate`, `crests the road from the north`, `holds the feet on the flagstones`, `exits with the ledger sealed in the case`). All of these are FAULT-FORM-MODIFIER. Solutions:
  - **Prefer transitive verbs that take the location or destination as direct object.** `enters the yard` is clean; `moves to the yard` is not. `crosses the gate` is clean; `steps through the gate` is not. `mounts the cart` is clean; `gets onto the cart` is not.
  - **Drop the prepositional phrase entirely if the verb stands alone.** `the ravens lift` is clean; `the ravens lift from the bell tower` is not. The bell tower's role is loc-state's job, accrued at facet-authoring time.
  - **Never append a location, time, or instrument prepositional phrase to a complete SVO.** A clean SVO terminates at the object (or at the verb if intransitive). Anything after that is padding.
- **No abstractions as objects.** `the yard holds the silence` is FAULT-FORM-INTERIORITY — silence is not a physical object, the line is a state assertion in disguise. State assertions belong in loc-state or feeling-flag facets. If the beat is a hold-against-something physically present, name the physical thing.
- **No copulas** — `is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being` are banned.
- **No negations** — never `<subject> didn't <verb>`. Collapse to positive holds (`Plumm holds the page on the desk`, not `Plumm doesn't pick up the page`; `Taylor holds the chin angle`, not `Taylor doesn't turn`).
- **No interiority** — thought, intent, feeling are facets.
- **No perception verbs** — `read`, `took`, `tracked`, `noted`, `counted`, `measured`. Recast as the physical event happening to the perceived entity.
- **No non-action / state / possession verbs.** A verb whose primary semantic is *being* or *having* rather than *doing* is forbidden, even when it appears transitive. Explicit deny-list (non-exhaustive — the principle is what matters):
  - **Possession:** `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`.
  - **Sustained carrying:** `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`.
  - **Containment / placement:** `contains`, `houses`, `holds` *(see license below)*, `occupies`, `inhabits`, `consists of`, `comprises`.
  - **Stative position-naming:** `lies`, `sits`, `stands` when used to describe position rather than the act of sitting/standing/lying.
  - Recast each as the discrete physical act that initiated or terminated the state, OR move the state to a state-update / location-state facet that cites a real action proto-line. `clerk carries the ledger` becomes the act-of-receiving (`clerk takes the ledger`) earlier in the file; the carrying-state lives in a state-update facet. `the cart sits at the gate` becomes `the cart stops` (the act of stopping) plus a loc-state facet for placement.
  - **`holds` license — narrow.** The hold-verb is permitted *only* in two cases: (1) body-part-as-object for stillness-against-pressure (`taylor holds the feet`, `mira holds the eyes`) — the hold *is* an act under pressure; (2) physical-object-resisting-pressure (`the door holds` against being opened from outside) where the holding is an active resistance. Hold-verbs with abstract objects (`holds the silence`, `holds her positions`), with named props the subject does not literally grip (`taylor holds the ledger` when the clerk has it), or with locations as object are FORBIDDEN.
- **No conjunctions** — no `and`, `but`, `while`, `as`. Two beats = two proto-lines.
- **Dialogue beats** — render as `<speaker-slug> speaks to <listener-slug-or-group>`. No spoken content. The dialogue file is downstream.

If a candidate sentence cannot be reduced to clean SVO without loss, the underlying beat is too compound. Split it.

## Task

1. Write the file header verbatim:
   ```
   narrator: <slug>
   goal: <one sentence>
   ```
   Followed by one blank line, then the body.

2. Author proto-lines for maximal coverage of the beats required to traverse `chunk`-start → `chunk`-end. Each beat that the chunk implies should appear; each constraint named in the chunk should have a beat that demonstrates its operation; each actor in the cast roster should have at least one fire (or be tagged absent in a margin comment).

3. Number monotonically from 1. IDs stable from assignment.

4. **Time-skips are blank numbered lines.** When the chunk implies an elapsed-time gap between beats (a scene change, a sleep, a journey compressed), insert a blank numbered line:
   ```
   12 Plumm closes the door behind him
   13
   14 Taylor enters the antechamber
   ```
   The blank line consumes an ID. Use it whenever the beats on either side are not in the same continuous physical moment.

5. Citations stay empty. Do not insert `[loc-state:?]` or `[<speaker>:<n>]` placeholders. Citations accrue at facet-authoring time, downstream.

## Output format

```
narrator: <slug>
goal: <one sentence>

1 SUBJECT VERB [OBJECT]
2 SUBJECT VERB
3
4 SUBJECT VERB OBJECT
...
```

Save to `active-project/theater/proto-lines.md`. Print line count + time-skip count to console.

## Termination

You produce the file in one shot. Pass 2 (constraint audit) consumes it. If pass 3 (dramatist) requests transitions, you may receive a delta-brief with one-line addition asks; you author only the additions, with new monotonic IDs. You do not revise existing lines unless explicitly directed by fixer.
