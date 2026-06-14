# Counterfactual-Baseline Process — negative-space worldbuilding

**What this is.** A reusable runbook for building the **counterfactual ordinary life** of a
character — the life they would have lived if they were *not* the protagonist (or not the
plot-bearing figure they are) — and slotting it into the project scaffolding as durable source
material. Distilled from the run that produced `design/counterfactual-life/` (Gael's princess life),
2026-06-08. Generalizes to any character in any project.

**Why a project needs it.** A plot-bearing character's pages are dominated by their *deviations* — the
heist, the secret, the mask, the escape. But a deviation is only legible against the **norm it departs
from**. If the norm is never built, scenes default to a generic backdrop (a castle, a school, an
office) and the deviation loses its specific friction. Counterfactual baselining builds the norm — the
ordinary day, the ordinary people, the ordinary expectations — so the prose can ground every strange
act in the real life it is hiding inside. It is **negative-space worldbuilding**: you draw the figure
by carving out the ground.

**What it is NOT.**
- Not plot. The baseline asserts no beat. When the outline contradicts the baseline, the outline wins
  and the contradiction *is the deviation you were trying to make legible.*
- Not a rewrite of premises. It never overrides a ratified GUARD or outline beat; it furnishes the
  room they happen in. (If your derivation seems to *require* changing a premise, stop — that's an
  `/and-reoutline` intake question, not a baseline question.)
- Not a card-build. It produces *design-reference* (the well cards draw from). Promotion to cards is a
  separate, on-demand step (see Phase 5).

**Trigger phrases:** "what would <character>'s life have been like" · "build the ordinary
life / the everyday detail / the lived texture for <character>" · "more real-life detail to draw from"
· "the life they'd have had if they weren't the MC."

---

## When to reach for it (and when not)

**Use it when:** a character spends most of their page-time *deviating* from an unstated norm
(a hidden operator, a secret-keeper, a fish-out-of-water, an impostor, a reluctant heir); the project
keeps grounding scenes in a generic backdrop; or you want richer source material before continuing to
scaffold.

**Don't use it when:** the character's ordinary life *is* the story (a slice-of-life protagonist —
their day is already on the page); the norm is already fully built elsewhere; or you're mid-chapter
and need a single fact (use `design/run-NN/idea-inbox.md`, not a baseline run).

---

## The four design principles

1. **The cage is the attendant, not the door.** For a confined or constrained character, the binding
   force is usually *people and routine*, not architecture. Build the watchers and the timetable
   before the floor-plan. (Adapt the noun: for an office character it's the meetings and the manager;
   for a soldier it's the duty roster and the NCO.)
2. **Time over space.** The durable substrate is the **schedule** — who is present at which hour, and
   where the gaps open. A deviation is an hour subtracted and accounted-for. Author the horarium.
3. **The seam is the deliverable.** The point of the baseline is the **seam map**: for every ordinary
   element, where the plot hides in it / exploits it / subverts it. A baseline with no seam map is
   inert lore. The seam map is what makes it *scaffolding*, not *trivia*.
4. **Counterfactual, not canonical.** Author the *un-lived* default. Flag — don't assert — where the
   plot departs from it. Provenance discipline (below) keeps the baseline from being mistaken for
   plot.

---

## Process

### Phase 0 — Scope & ground (read before writing)
- **Identify the character and the counterfactual.** "If <character> were not <their plot role>, what
  ordinary life would they have?" Name the role being subtracted (MC / the chosen one / the impostor /
  the operator).
- **Pin the live layer.** Read the *current ratified* names, era, family, and laws — NOT stale cards.
  In this project: `intake/GUARDS-register.md` + `intake/tentative-outline.md` +
  `design/run-NN/timeline-and-family-tree.md`. **Write to the live layer; flag any card drift loudly
  at the top of the output (a naming/era note).** (Gael run: cards still said Saerys/Viserys-father;
  the output's INDEX opens with a drift table.)
- **Harvest existing texture.** Read the institutional bedrock and any relevant cards so you *extend*
  rather than duplicate. In this project: `run-01/constraints.md` (the offices, the laws, the
  loopholes), the location cards (spatial layout), the handler cards (e.g. the septa). Note what's
  already established so the baseline is consistent and additive.

### Phase 1 — Decompose into the three domains
Almost every "ordinary life" decomposes into three docs. Build them in this order:
- **The people** (`the-household` / the establishment / the unit) — everyone in the character's daily
  orbit, by *function and rank*, in concentric rings (closest = most daily contact). Name where
  invented (placeholders, overridable). For each: what they do *to* and *for* the character, when
  present, the gaps between them, their loyalty/economy.
- **The routines** (`the-day`) — the hour-by-hour timetable, broken into **life-phases** if the grip
  changes with age/status. Plus the weekly rhythm, the annual calendar, and standing routines
  (meals, dress/body, sleep). Frame each as a *surveillance/availability schedule*: who watches when,
  where the gap opens.
- **The expectations** (`the-script`) — the explicit rubric the character is graded on, the
  ideological frame (here: the Faith's gender-script), the institutional machine that drives the plot
  (here: the dynasty/marriage clock), the social meaning of their defining trait (here:
  dragonlessness), and the **calibrated reward/punishment ladders** that enforce it all. Include the
  *unsaid* rules — expectations enforced by never being stated.

### Phase 2 — Build the seam map (the production tool)
A single table in the INDEX: **ordinary element → where the plot uses/subverts it**, with outline
citations. This is the highest-value artifact; write it last (you need all three docs first) and write
it densest. Weave shorter "the seam:" notes through each doc at the point of each element. Rule of
thumb: if you can't name the seam for an element, ask whether the element earns its place.

### Phase 3 — Triage forward-pointers
- **Candidate cards.** List (don't build) the elements that would warrant a card *if* a beat makes
  them load-bearing. Mark class/scope. Note any character who is a *co-protagonist, not furniture*
  and therefore out of scope for this library (e.g. the maid — name it a principal call, describe only
  the *pool she's drawn from*).
- **Canon-uncertain.** List anything to verify against canon/source in a future fidelity pass (era
  holders, projected devices, generalized-from-instances norms). Mirror the cultivation-library's
  `[canon-uncertain]` practice.
- **Open questions.** The principal decisions the baseline surfaced (naming, which slot a future
  character fills, how populated a set is). Don't decide them; queue them.

### Phase 4 — Slot into scaffolding (provenance-disciplined)
Make the library *findable* without disturbing the live state:
- **Author as a library** under `design/<name>/` with an `INDEX.md` (orientation + use-this-when +
  seam map + candidate cards + canon-uncertain + open questions), mirroring `cultivation-library/`.
- **Register in showrunner memory** (`staff/showrunner/memory.md` → `routing:`) as a named pointer,
  the way `cultivation_library` is registered — a one-line "first-stop reference for X" note.
- **Point from the digest** (`staff/showrunner/world-notes.md`) — a short section linking the library
  as the *lived-texture expansion* of the institutional bedrock.
- **Carry it through re-baselines.** Add it to the `intake/INTAKE-RUNBOOK.md` artifact manifest as
  **KEEP / reference** so any `/and-reoutline` migration carries it forward, frozen and additive.
- **Provenance discipline:** never edit the frozen baseline (`convergence/`); flag drift, don't fix
  cards inline (that's the migration's job); keep the output clearly marked as *counterfactual
  reference*, not plot.

### Phase 5 — Promote on demand (optional, later)
When a beat makes a baseline element load-bearing, promote it to a card via margit (`/and-cast`-style
provisioning or a direct margit dispatch), using the candidate-card list as the spec. Mind the
project's name-novelty caution (CLAUDE.md "Not in scope") when naming originals. Until then, the
baseline stays reference.

### Phase 6 — Exit summary (one block)
Report: character + counterfactual framed · the three docs created · seam-map entry count · candidate
cards flagged · open questions queued · where it was slotted (routing + world-notes + intake manifest)
· suggested next step.

---

## Decision rules
- **Live layer beats cards.** Always author to ratified premises; flag card drift, never silently
  inherit a stale name/era.
- **Functions are durable; names are placeholders.** Author the *role*; offer names as overridable
  (naming may be a principal/margit call).
- **The seam earns the element.** Every ordinary detail must connect to a deviation, a cover, an
  obstacle, or a cost — or it's trivia. The seam map is the test.
- **Counterfactual, never canonical.** The baseline is the un-lived default. The outline always wins a
  contradiction, and the contradiction is the point.
- **Reference first, cards later.** Produce design-reference; promote to cards only when a beat demands
  it.
- **Provenance is sacred.** Archive/flag, never overwrite; mark the output as reference; carry it
  through migrations as KEEP.

---

## Reusable scaffold (copy for a new character)

```
design/<character>-life/                 (or design/counterfactual-<character>/)
  INDEX.md          — naming/era note · use-this-when · SEAM MAP · candidate cards · canon-uncertain · OQs
  the-establishment.md   (people — rings, functions, the economy, where a future character is drawn from)
  the-day.md             (routines — phased horaria · weekly · annual · meals/body/sleep · the gaps)
  the-script.md          (expectations — rubric · ideological frame · the driving machine · the trait's meaning · the ladders · the unsaid)
```
Slots: `memory.md` routing pointer · `world-notes.md` section · `INTAKE-RUNBOOK.md` manifest row
(KEEP/reference).

---

*Authored 2026-06-08 alongside `design/counterfactual-life/`. Peer process docs:
`design/convergence-process.md` (outline convergence), `intake/INTAKE-RUNBOOK.md` (outline
re-baseline). This one is the **source-material derivation** process.*
