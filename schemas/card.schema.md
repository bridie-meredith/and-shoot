# Card Schema

Cards are the atomic context units. Every card is a markdown file with frontmatter and class-specific body sections. Margit owns all writes, merges, and taxonomy.

Schema authority: this file. Source: stripped from brighid-creative-writing/schemas/card.schema.md — removed gacha, zone taxonomy, workshop-artifact, and overlays not used in and-shoot.

---

## Frontmatter (all cards)

```yaml
---
name: {{unique slug, kebab-case}}
class: {{one of the four classes below}}
subclass: {{see §Subclass values, optional}}
scope: library | project | archived | tombstone
project: {{project slug, required if scope=project}}
world: {{root-location slug, optional — absent means universe-agnostic}}
overrides: {{parent card name, optional — project cards only}}
composes: {{list of source cards, optional — set when this card is a merge/fusion}}
supersedes: {{list of card slugs this card replaces, optional}}
superseded_by: {{single card slug that replaces this one, optional}}
variant-of: {{base card slug, optional — see §Variant cards}}
variant-reason: {{one-line reason, required when variant-of is set}}
variant-project: {{project slug that originated this variant, optional}}
references: {{list of other card names this card depends on, optional}}
persona-purpose: {{list — persona class only: on-stage-character | audience}}
paired-agent: {{agent name — agent-persona subclass only}}
display-name: {{human-readable label — agent-persona subclass only, optional}}
aliases: {{list of name slugs — persona class only, optional}}
portability: {{fixed | portable — prop class only}}
origin: {{harvested | authored | promoted}}
quality: scant | full
tier: lead | supporting | minor
---
```

---

## Classes

Four classes: **persona, location, prop, condition**.

All four are story-facing — they compose the cast, the stage, and the ambient state. No system-facing card class exists in and-shoot (margit's workshop operates on cards directly, not on a separate class).

---

### persona

A person. Anyone — real, fictional — who has a voice, taste, and pet peeves.

#### Core sections (all personas)

- **Description** — one-line read of who this persona is.
- **Voice** — how they sound. Register, speech patterns, tells.
- **Taste** — what they like. What lands for them.
- **Pet Peeves** — what they hate. Each peeve: name, description, severity (blocker / strong / soft).
- **Stats** — optional. Attribute bag: numeric or categorical.
- **Relationships** — optional. Key directional connections to other personas.

#### Vibe Seeds (optional, high-value)

`## Vibe Seeds` — accumulated history, private associations, and tonal weight this character carries into any deployment. Not a runtime vibe-cloud — a source document that the 1c vibe-population step reads to generate the project-scoped vibe-cloud. Without it, vibe generation draws only from the card's structural content (voice, taste, hard fences), which is insufficient for characters with significant prior-story weight.

Two sub-sections:
- **Accumulated history to register** — what has this character already done, survived, lost, and done to others. Bullet list. Each bullet is a fact about who they are by the time any story opens.
- **Private associations** — how this character specifically holds each key they activate. Named-key: one-line gloss of what the key means *for them*, not in the abstract.

Authoring note: Vibe Seeds are written once and carried forward. They accumulate across projects as understanding of the character deepens. Margit preserves them on all card mutations. They are never cleared on revision — only extended.

#### Role overlays (optional)

A persona carries only the overlays it can actually perform. Impersonator refuses casts into roles the persona doesn't carry an overlay for.

**Fiction role** — persona appears in the story as a character. Adds:
- **Thematic Purpose** — what this character is for in the story.
- **Look** — appearance, physical tells.
- **Hard Fences** — inviolable canon facts. Treated as binding.
- **Default Stance** — how they enter a scene.
- **Action Menu** — things they reach for.
- **Action Costs** — what each menu item costs when used.
- **Triggers** — what pulls them toward or away from action.
- **Off-Screen Cadence** — what they do when not on stage.
- **Inventory** — project scope only. Prop card refs currently carried.

**Audience role** — persona reacts to the show as an audience member. Adds:
- **Voice** — (core section, read through audience lens) how they actually chime in.
- **Hot Buttons** — what makes them react hard, positive or negative.
- **Fatigue Signals** — how they telegraph boredom.

---

### location

A discrete place where action can happen. Locations nest via optional `parent:` frontmatter field.

Body sections:
- **Geography** — where this location sits, how big, what kind of place.
- **Layout** — internal structure, what's visible from where.
- **Sensory Vocabulary** — palette of smells/sounds/textures/light. Default ambient state.
- **Fixed Props** — card refs to props with `portability: fixed` that belong here.
- **Exits** — where characters can go and how.
- **Hazards** — environmental pressures available for escalation.
- **Ambient Interruption Hooks** — things that can intrude without author invention.

---

### prop

Any tangible object in the fiction. One card per object. At any moment a prop sits in exactly one bucket: a location's fixed-props list or a character's inventory. Bucket assignment is runtime state (recorded in actor state files), not a field on the card.

Body sections:
- **Physical Description** — what it looks like.
- **Affordances / Uses** — what characters can do with it.
- **Sensory Hooks** — for impersonator to pull from.
- **Portability** — prose detail when the frontmatter key is insufficient.
- **Carry State** — when carried: concealment, weight, noise.
- **Functional State** — every aspect critical to the prop actually working. Tracked in runtime state, not on the card atom.

---

### condition

An ambient state modifier that colors one or more locations during a scene. Conditions stack.

Body sections:
- **Description** — one-line summary.
- **Sensory Impact** — what this condition changes about sensory vocabulary.
- **Duration** — temporary or persistent; how likely to change mid-scene.
- **Interaction Notes** — illustrative (not exhaustive) combinations with common partners.

---

## Subclass values

`subclass:` narrows the card's role. Recognized values:

- **`agent-persona`** — a persona card paired with a framework agent. Requires `paired-agent:`. Lives under `staff/<slug>/`.

No other subclass values are in use in and-shoot.

---

## Scope enum

- **`library`** — canonical card available across all projects.
- **`project`** — scoped to a specific project; `project:` field required.
- **`archived`** — permanently preserved for provenance; not loaded for new work.
- **`tombstone`** — superseded. Carries `superseded_by:`. Margit auto-follows the chain on fetch.

---

## Persona quality gate

Any persona used on-stage must be `quality: full`. Scant + used = blocking rescue before cast entry.

- **Scant** — skeleton card. Enough to load without errors; not enough for rich output.
- **Full** — all required sections populated. Can anchor a scene.

Scant remains valid for locations, props, and conditions at margit's discretion.

---

## Persona tier

`tier:` is persona-class only. Controls which model is used when the persona is spawned as an impersonator. Unset defaults to `lead`.

- **`lead`** — protagonist or major character. Spawned with `model: opus`. Richest characterization, widest creative range.
- **`supporting`** — recurring secondary character with meaningful scenes. Spawned with `model: sonnet`.
- **`minor`** — background, walk-on, or single-scene character. Spawned with `model: haiku`.

Set by margit at cast selection or card authoring. Margit proposes upgrade when a minor or supporting character accumulates scenes warranting richer fidelity.

---

## Override semantics

Project cards with `overrides: <parent>` layer on top of the library card at load time. Margit performs the merge.

Merge rules:
- Same-name section in override → replaces parent section entirely.
- New section in override → added to effective card.
- Frontmatter — override fields replace parent fields; `references` merges as union.

---

## Supersede chain

When a revision is radical enough that old and new shouldn't coexist:
- Old card sets `superseded_by: <new-slug>`.
- New card sets `supersedes: [<old-slug>, ...]`.
- Fetch auto-follows to the tip. Superseded cards stay in library for provenance.

---

## Variant cards

A variant is a coexisting alternative. `variant-of:` does not retire the base card.

- **`variant-of:`** — required. Points to base card slug. Base is untouched.
- **`variant-reason:`** — required. One-line explanation.
- **`variant-project:`** — optional. Project that originated this variant.

Chain depth capped at 1. Base card must not itself carry `variant-of:`.

---

## Card quality

- **Scant** — minimum viable content.
- **Full** — richly developed, can anchor a scene.

Usage-driven: a character who carries scenes needs full. A character who appears in one beat needs scant. Margit proposes promotion from scant to full when usage warrants it.

---

## Memory and state

Actor memory and state do not live on card atoms. They live in the actor's working directory under `active-project/actors/<slug>/` and follow `schemas/memory.schema.md`.

## Vibe-cloud

Actor vibe-clouds live at `active-project/actors/<slug>/vibes.md`. See `schemas/memory.schema.md` §Vibe-cloud.
