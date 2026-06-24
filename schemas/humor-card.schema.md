# Humor Card Schema

Schema authority for **humor cards** — the cards that live in the library's humor hall (`cards/humor/`).

A humor card is **not** a story-facing card. It is a **library reference resource**: a catalog of one comedic *mechanism* (a category of joke / a way of being funny) with a bank of faceted exemplars. The dialogue-writer fork (and any future joke-generation step) consults a humor card the way it consults a `behavior` card — as raw material aimed at, not a runtime persona embodied. Humor cards are consulted, never cast.

This makes `humor` a **sixth card class**, registered alongside the five story-facing classes in `schemas/card.schema.md` (persona, location, prop, condition, behavior). It is explicitly a resource/reference class — see `schemas/card.schema.md` §Classes and CLAUDE.md Rule 8 for the taxonomy note. Margit owns all writes, merges, indexing, and validation, exactly as for the other classes.

**Relationship to `comedy-register` (behavior class).** A behavior card like `comedy-register` describes *a particular character's or project's tonal register* — how *this speaker* sounds when being funny. A humor card describes *a portable comedic mechanism* — the structural engine of a kind of joke, demonstrated across many settings and tellers, available to *any* project. Behavior = whose voice. Humor = which mechanism. They compose: a dialogue-writer fork loads the speaker's behavior card for voice and may pull a humor card for the comedic move.

---

## Frontmatter

```yaml
---
name: {{unique slug, kebab-case — the mechanism, e.g. gallows-humor, wordplay-pun}}
class: humor
scope: library | project | archived | tombstone
project: {{project slug, required if scope=project}}
mechanism: {{one-line — the core comedic engine in a phrase, e.g. "laughing in the face of death / suffering"}}
family: {{one of the comedic-engine families below — incongruity | superiority | relief | wordplay | observational | character}}
register: {{tonal range — e.g. "warm↔cruel", "light↔bleak", "gentle↔savage"}}
references: {{list of behavior / persona card slugs this mechanism pairs well with, optional}}
supersedes: {{list, optional}}
superseded_by: {{single slug, optional}}
variant-of: {{base humor slug, optional}}
variant-reason: {{required when variant-of is set}}
origin: harvested | authored | promoted
quality: scant | full
tags: {{list — include facet keywords for retrieval, e.g. [dark, death, coping, deadpan-adjacent]}}
---
```

`family` buckets the mechanism by its underlying comedic engine. The standard families (a working taxonomy, extensible by margit):

- **incongruity** — humor from a violated expectation / collision of frames (absurdism, surrealism, non-sequitur, bathos).
- **superiority** — humor from a target made smaller (mockery, sarcasm, put-downs, satire, schadenfreude — *and* self-deprecation, where the target is the self).
- **relief** — humor that discharges tension (gallows humor, taboo-breaking, bawdy/ribald, nervous comedy).
- **wordplay** — humor from the language itself (puns, double-entendre, malapropism, spoonerism, witty epigram).
- **observational** — humor from recognition of the shared ordinary ("it's funny because it's true").
- **character** — humor that lives in *how a person is* (deadpan, the straight man, the fool, persona-driven running bits).

A mechanism may lean on more than one engine; `family` names the *primary* one and the body notes secondary engines.

---

## Body sections

### Mechanism (required)
How the joke actually works — the cognitive move it runs on the listener. Two or three sentences naming the setup → turn → payoff structure and *why* it produces laughter (the released expectation, the asserted superiority, the discharged tension, etc.). This is the load-bearing description: the exemplars *show* the mechanism; this section *names* it.

### Facet axes (required)
The dimensions every exemplar is tagged along, so dialogue generation can retrieve by setting and teller (the "gallows humor england 18th century" use case). Standard axes:

- **setting** — era + place + social context (e.g. `england-18thc-gallows`, `wwi-trench`, `modern-office`, `medieval-tavern`, `secondary-world-court`). For fiction, the in-world setting slug.
- **teller** — who is making the joke: social class / role / temperament / relationship to the target (e.g. `condemned-prisoner`, `world-weary-soldier`, `court-fool`, `grieving-widow`, `child`).
- **target** — what the joke is aimed at: `self` / `other` / `power` / `the-situation` / `death` / `no-target` (pure play).
- **delivery** — `spoken-aside` / `retort` / `bit` / `interior` / `written` / `performed`. How it surfaces in a scene.

Per-card content may add a card-specific axis (e.g. a `darkness` axis for gallows humor) and notes which axes most strongly gate whether the mechanism lands for a given speaker.

### Exemplars (required — the load-bearing bank)
The bank of demonstrations. **Multiple required; ten is better than three.** Deliberately spread across settings, eras, cultures, classes, and teller-types — the same mechanism shown working *by various people in various settings*. A humor card with one setting or one teller-type is incomplete.

Each exemplar:

```
> EX-{{nn}} [setting: <slug> | teller: <type> | target: <type> | delivery: <type>]
> "<the line, joke, or beat>"
> — Why it lands: <one line on the mechanism at work here>.
> — Deploy: <one line on how a dialogue-writer adapts the *structure* to a new speaker/setting>.
```

Exemplars are **illustrative of the mechanism, not a clip library.** They show the structural move so it can be re-built in-fiction. See §Surface-convention fence.

### When it lands / When it fails (required)
- **Lands** — the scene conditions, relationships, and stakes that make this mechanism work.
- **Fails / misfires** — when it reads as cruel, flat, anachronistic, try-hard, or tonally wrong. Each misfire is a usable warning for the dialogue-writer fork and a check the audience reviewer can run.

### Pairs with (optional, recommended)
Behavior cards, persona archetypes, and other humor cards this mechanism composes well with (e.g. gallows-humor pairs with `westeros-northern` understatement; deadpan pairs with a straight-man behavior). Card-ref slugs.

### Anti-patterns / fences (required)
Hard "do not" rules. The most important is the surface-convention fence (below). Also: register fences (e.g. "never punches *down* on a powerless target in a sympathetic-POV scene"), anachronism fences ("modern idiom in a period setting flags as wrong"), and overuse fences ("more than N per scene reads as the author being funny, not the character").

### Dialogue-generation hooks (required)
Explicit guidance for the future dialogue-writer / joke-generation integration:
- **Retrieval keys** — the facet combinations that should surface this card (e.g. `target:death + setting:*gallows* + register:bleak`).
- **Applicability test** — a one-line check the generator runs to decide whether a joke is *appropriate* at this anchor (a joke is pulled only when it fits the beat, the speaker's behavior card, and the scene's tonal license — never inserted for its own sake).
- **Adaptation rule** — how to transform an exemplar into an in-fiction line (transfer mechanism + structure; re-skin content into the speaker's voice and setting; obey the speaker's behavior-card fences).

---

## Surface-convention fence (non-negotiable)

**Only the comedic *mechanism* and *structure* transfer. The exemplar's content does not.** A dialogue-writer fork that pulls this card must NOT paste, paraphrase, or lightly-reskin a specific exemplar joke into the prose. It learns *how the joke is built* — the setup/turn/payoff shape, the timing, the relationship between teller and target — and constructs a fresh line in the speaker's voice, period, and idiom. This mirrors the persona-exemplar surface-convention fence (`schemas/persona-exemplar.schema.md`): exemplars prime the *form*, never supply the *substance*. Importing exemplar content verbatim (especially a real-world or copyrighted joke into a fictional mouth) is a hard violation the auditor / audience reviewer flags.

---

## Quality gate

- **scant** — mechanism + a handful of exemplars on too-narrow a spread of settings/tellers; enough to consult, not enough to anchor varied deployment.
- **full** — mechanism, all required sections, and an exemplar bank spread across multiple eras / cultures / classes / teller-types with deploy notes; the dialogue-generation hooks populated.

A humor card consulted by a live dialogue-writer integration should be `full`.

---

## Authoring notes

- Humor cards are a **cross-project resource**: `scope: library` is the default. A project may author a `scope: project` humor card for a setting-specific comedic register, or a `variant-of:` an existing card.
- One card = one mechanism. Resist bundling (don't fold sarcasm + irony + satire into one card if they run on distinguishable moves; cross-reference instead via §Pairs with).
- Margit indexes every humor card in `cards/humor/INDEX.md` by `family` and by facet keyword, and validates against this schema on every store.
- The integration that makes dialogue generation pull from these cards is **not yet wired** — these cards are authored ahead of that consumer so the bank exists when the integration lands. The §Dialogue-generation hooks section is the contract that integration will read.
