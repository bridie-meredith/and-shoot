# Card Schema

Cards are the atomic context units. Every card is a markdown file with frontmatter and class-specific body sections. Margit owns all writes, merges, and taxonomy.

Schema authority: this file. Source: stripped from brighid-creative-writing/schemas/card.schema.md — removed gacha, zone taxonomy, workshop-artifact, and overlays not used in and-shoot.

---

## Biography / exemplar split (persona class only)

Per PROP-0005 / DEC-0016 (2026-05-26) — narrowed by PROP-0005-A / DEC-0017 — persona representation is two-layered:

- **Biography (this schema, `cards/personas/<slug>.card.md`)** — identity, voice description, taste, hot buttons, hard fences, action costs, fiction-role overlay. The **describing** layer. Authoritative for what the persona *is* and what they *cannot* do.
- **Exemplar (separate schema, `cards/persona-exemplars/<slug>.md`)** — a concrete demonstration of the persona's voice/output in known-good form. The **demonstrating** layer. Authoritative for *how* the persona renders in motion.

Tier-1 consumers (impersonator, audience, renderer voice) are dispatched with both. Tier-2 (orchestrator-critic, dramatist, auditor, editor) and Tier-3 (showrunner, margit, fixer) receive only the biography. See `schemas/persona-exemplar.schema.md` for the exemplar schema; `staff/margit/exemplar-authoring-process.md` for the authoring and QC process; PROP-0005 / PROP-0005-A in `staff/admin/process-proposals.md` for the architectural rationale.

The biography layer remains the source of truth for identity and fences. The exemplar augments by showing voice in action. A persona MAY exist with biography only; a persona MUST NOT exist with exemplar only.

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
character: {{persona slug — behavior class, per-character subclass only, required}}
inherits: {{parent behavior slug — behavior class only, optional}}
period: {{era slug — behavior class only, optional — e.g. hotd, main-canon, post-conquest}}
region: {{region slug — behavior class only, optional — e.g. north, dorne, riverlands, free-cities}}
social-class: {{class slug — behavior class only, optional — e.g. smallfolk, noble, maester, septon}}
origin: {{harvested | authored | promoted}}
quality: scant | full
tier: lead | supporting | minor
---
```

---

## Classes

Five classes: **persona, location, prop, condition, behavior**.

All five are story-facing. Persona/location/prop/condition compose the cast, the stage, and the ambient state. Behavior carries voice samples *and* non-verbal tics *and* memory-monument register for shoot-v2 dialogue authoring and review. No system-facing card class exists in and-shoot (margit's workshop operates on cards directly, not on a separate class).

(The `behavior` class supersedes the previous `dialect` class. *Dialect* — voice samples and verbal patterns — is one section of the broader behavior card, alongside non-verbal tics and memory monuments. Existing `class: dialect` cards should be migrated to `class: behavior`. Margit handles migration on touch.)

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
- **Threshold Discipline** (URI-017, 2026-05-10) — what the persona does when rubric thresholds permit a defense the persona's taste rejects. Three rules apply uniformly across audience personas; per-card content names the persona's specific traps:
  1. **Rubric arithmetic is advisory; taste is authoritative.** If the count says "within tolerance" but the bones read wrong, the bones read wrong. Window-percentage budgets, instance counts, and "back half" thresholds backstop the audience's read; they do not exempt a unit from attack.
  2. **Season-plan / tone-law / project-condition citations cover what the rubric explicitly licenses, not what the persona's lens registers as a fault.** A defense that cites a tone-law clause to defeat a structural seam is rejected unless the cited clause specifically licenses the structural form the persona is attacking.
  3. **Carry-forwards are open until adjudicated clean.** "Previously identified / known residual" parking does not close a seam. A carry-forward acknowledged but not corrected within a season-plan-licensed pattern remains attackable.
- **Season-Scope Adversarial** (URI-014, 2026-05-10) — categories the persona presses across multi-stretch arcs. Distinct from per-line and per-episode habits (implicit in Voice / Hot Buttons / Fatigue Signals). Per-card content names 3–5 specific attack categories: e.g., for an atmosphere-focused persona — atmospheric drift across multi-episode arcs, procedural recurrence, cost-not-landing, tonal flatline; for a momentum-focused persona — board-change density collapse across arcs, close-earns-next quality at boundaries, ratchet-immediacy; for a fidelity-focused persona — voice-fidelity drift across arcs, idiom depletion, source-material register erosion.

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

### behavior

A behavior bank — voice samples, verbal patterns, non-verbal tics, and memory-monument register. The raw material for authoring dialogue or interiority *and* the structural anchor reviewers use to evaluate whether a character's behavior is in-register for their period × region × class. Used by the shoot-v2 dialogue-writer fork and the audience reviewer. Not a runtime persona; the behavior card is consulted, not embodied.

A behavior card describes how a class of speakers (or one specific speaker) sounds, moves, and weights cultural memory. *Dialect* (verbal register) is one of three primary axes; the other two are *non-verbal* (physical tics) and *memory monuments* (cultural anchors weighted by what is or isn't named).

#### Subclass values

- **`shared-behavior`** — describes a class of speakers, not a specific person. Composition card: a per-character behavior card may `inherits:` from one shared-behavior card and `references:` others. Frontmatter: `character:` is omitted (or set to the sentinel `<shared>`).
- **`per-character-behavior`** — describes one specific speaker. Frontmatter: `character:` is required.

If `subclass:` is unset on a `class: behavior` card, default to per-character.

#### Frontmatter additions

- **`character:`** — required for per-character subclass. Slug of the persona card this behavior belongs to. One persona may have multiple behavior variants (e.g. one per project).
- **`inherits:`** — optional. Slug of a parent behavior card (typically shared-behavior) whose samples, tics, and monument register feed in beneath this one. Chain depth capped at 1 by default; see Composition note below.
- **`period:`** — optional. Era slug. E.g. `hotd` (95–130 AC Westeros), `main-canon` (~298 AC Westeros), `pre-gold-morning` (Worm).
- **`region:`** — optional. Region slug. E.g. `north`, `dorne`, `riverlands`, `free-cities`, `dothraki-sea`.
- **`social-class:`** — optional. Class/role slug. E.g. `smallfolk`, `noble`, `maester`, `septon`, `cape-protagonist`.

A shared-behavior card typically sets one or more of `period / region / social-class` and omits `character:`. A per-character card sets `character:` and may set the period/region/class fields to anchor where this character sits.

#### Body sections

Required (load-bearing):

- **Direct samples** — verbatim quotes (or interior-prose excerpts). Source-material excerpts, prior-episode lines, anything that demonstrates the voice. Each sample tagged with origin (e.g. `worm canon, ch12`, `s01e02`, `synthesized`). Multiple samples encouraged; ten is better than two. A behavior card with no direct samples is incomplete.

Strongly recommended:

- **Cadence** — rhythm, sentence length, pause habits. Where the voice breathes. How it ends sentences (period, em-dash, trailing fragment).
- **Vocabulary** — signature words / forbidden words. What the character (or class) reaches for, what they refuse to say. Includes register markers (formal / vulgar / clinical / archaic).
- **Syntax** — sentence-shape patterns. Subordination habits, fragment use, parallelism, comma-splice tolerance, run-on tendencies.
- **Voice tells** — interiority cues for POV / narrator use. How the inner voice sounds when the character is the lens. What the character notices, what they refuse to look at directly.
- **Non-verbal tics** — physical and behavioral patterns that travel with the voice. Posture, gesture, eye-line, the things the body does at moments of stress, comfort, formality. Studio and impersonator deploy these; the dialogue-writer fork should not write them into the spoken-line file. Listed on the behavior card so the behavior is fully described.
- **Memory monuments** — shared events, traumas, and cultural anchors that weigh on the speaker's mind whether named or not. Each monument has a register-rule: how it surfaces in voice, what is or is not said of it, what behavior it produces when adjacent. For shared-behavior cards (period × region × class), this section is the *register-around* the monument — a separate `cards/conditions/memory-monuments/` card describes the monument itself. For per-character behavior cards, this section names what the character carries personally.

Per-character cards may omit shared-card-overlapping sections that are fully covered by the parent (with an `(inherited)` note); the omission is then resolved at composition time.

#### Composition

A per-character behavior card composes with one or more shared-behavior cards along the period × region × class axes. Loading order:

1. Universal-mannerisms behavior card (e.g. `westeros-grrm-mannerisms`) if the project has one.
2. Region-shared behavior card (e.g. `westeros-northern`).
3. Class-shared behavior card (e.g. `westeros-noble-courtly`).
4. Per-character behavior card (e.g. `eddard-stark`).

The current schema's chain-depth-1 cap on `inherits:` is too shallow for full period × region × class composition. Until the cap is revised, per-character cards should `inherits:` from one parent (typically the most-specific class card or the most-character-shaping card) and reference the rest in `references:`. Loading agents (dialogue-writer fork, audience reviewer) compose the stack from `inherits` + `references` together.

#### Authoring notes

Behavior cards are reviewed by margit and used by audience critics during line review. They are not loaded by line-time impersonators (shoot-v1 — being retired); they replace the impersonator's persona-roleplay framing in shoot-v2 with a target-behavior description that the dialogue-writer fork explicitly aims at and the audience reviewer evaluates against.

The card answers four questions about the speaker: *how do they sound, how do they move, what do they refuse to name, and what do they reach for that no one else in the scene would?* The first is dialect. The second is non-verbal. The third is the negative space of memory monuments. The fourth is the positive space of vocabulary and reach.

A behavior card with no direct samples is incomplete — the samples are the load-bearing section; the descriptive sections describe patterns, samples *show* them. An agent authoring against a sample-empty behavior card is generating in the void.

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
