# and-shoot

---

## purpose
author creative fiction for entertainment, minimal human orchestration, all else ai

> **human role:** gatekeeper at series-level audit only. season and episode loops run agent-to-agent with no required human checkpoints unless an audit escalates past season scope.

---

## principles

### modular
every component is independently composable. agents, cards, critic configs, and commands are discrete units that can be combined without coupling. the system is built from parts, not a monolith. swap an impersonator persona, change a critic config, replace a season plan — nothing else breaks.

### in threes
the system's native rhythm is three.
- three planning levels: **series / season / episode**
- three constraint types: **law / lore / behavior**
- three plot components: **reason / elements / shape**
- three authoring roles: **screen-writer / audience / dramatist**
- three tries per prompt before proceeding

when something isn't working, three attempts is the budget. then move on.

### planning granularity
planning zooms in as scope narrows:

| level | scale | detail |
|-------|-------|--------|
| **series** | vague, large | broad arc, general themes, rough beginning / middle / end. a horizon, not a map. |
| **season** | general, medium | significant arc defined, key events sketched, cast established. |
| **episode** | specific, small | line-by-line plan, active cast, props and locations identified. |

**horizon rule:** plan the current season in full. keep at most a general sketch of the next season. do not plan beyond one season ahead.

**continuity rule:** when detailing an episode, the series plan and season plan are always held in context. episode decisions must be consistent with both. the episode is small and specific, but it serves the large and the general.

---

## general info

**cards:** atomic context units. four classes: **persona**, **location**, **prop**, **condition**. agents consume cards rather than raw files. schema authority: `schemas/card.schema.md`. import from brighid-creative-writing. (Gacha-element class is deferred and out of scope for and-shoot.)

**vibe-cloud:** a vibes snapshot scoped to the current level (series / season / episode). captures mood, tone, atmosphere, and thematic register. built at the start of each level, updated on significant shift. import schemas: `vibes.schema.md` + `vibe-delta.schema.md` from brighid-creative-writing.

**margit's workshop:** houses assets for crafting, improving, and pruning cards.

**active-project:** sole active project directory. modeled as a film studio. only one project is active at a time — at project activation, the previous active-project is moved to `projects/` as a named subdirectory before the new studio is built.

**projects:** completed series archive. each subdirectory is a closed project received from active-project at conclusion.

### active-project structure

```
active-project/
  actors/       — actor housing: persona card + memory for each cast member
  hopefuls/     — pool of candidate personas not yet cast; available for selection
  warehouse/    — locations, props, special effects (condition cards)
  audience/     — audience personas used by the audience critic config
  staff/        — showrunner, studio, auditor, fixer, margit, editor configs and memory
  theater/      — the show file lives here; where the episode is written
  polish/       — wrap artifacts: flagged draft, editor output, final closed manuscript
```

each directory maps to a role in the production. agents load from their home directory and write back to it. nothing lives outside the studio during an active project.

---

## planning levels

### series
vague and large. the broadest course from story beginning to conclusion. establishes the thematic reason, the world's constraints, and the rough shape of the whole. over-specifying here is a mistake — leave room for seasons to breathe.

### season
general and medium. a significant arc within the series. establishes the season's specific vibe-cloud, its cast, its key events, and its contribution to the series arc. the current season is always planned in detail. the next season gets a sketch, nothing more.

### episode
specific and small. a single chapter within a season. fully detailed: an ordered bullet plan driving the show file line by line, active impersonators, props, locations. always written with the series plan and season plan in view.

---

## planning patterns

planning follows the same shape at every level. the difference is scale, not structure. at each level: establish drama, break it into chunks, make each chunk a statement of what it does for the level above it.

**chunk:** a named unit one level below the current scope. seasons are the chunks of a series. episodes are the chunks of a season. a chunk statement is one or two sentences: what happens in this chunk and what dramatic work it does.

---

### pattern: project activation
*fires once, at the start of a new project.*

**0. scaffold active-project**
*Use `/and-project <project-title-slug> <audience-slug-1> <audience-slug-2> <audience-slug-3>` — it handles all of the following automatically. Run it before any other activation step.*

Manual steps if not using the command:

1. **Do not archive.** Do not move or rename the existing `active-project/` directory. Start fresh scaffold in place.
2. **Create directory tree:**
   ```
   active-project/
     actors/
     hopefuls/
     warehouse/
     audience/
       <persona-slug-1>/
       <persona-slug-2>/
       <persona-slug-3>/
     staff/
       showrunner/
       studio/
       auditor/
       fixer/
       margit/
       editor/
     theater/
     polish/
   ```
3. **Create stub files** (all schema-minimal at creation; populated during activation):
   | File | Schema |
   |------|--------|
   | `active-project/staff/showrunner/memory.md` | `schemas/showrunner-memory.schema.md` |
   | `active-project/staff/showrunner/series-plan.md` | (prose; empty stub) |
   | `active-project/staff/studio/ltm.md` | `schemas/memory.schema.md` (LTM section) |
   | `active-project/staff/studio/stm.md` | `schemas/memory.schema.md` (STM section) |
   | `active-project/staff/studio/state.md` | `schemas/memory.schema.md` (State section) |
   | `active-project/staff/studio/vibes.md` | `schemas/memory.schema.md` (Vibe-Cloud section) |
   | `active-project/staff/margit/margit.memory.md` | (free-form; empty stub) |
   | `active-project/audience/<slug>/memory.md` × 3 | (one per persona; free-form; empty stub) |
   | `active-project/staff/showrunner/world-notes.md` | (free-form; written by showrunner in step 1a) |
   | `active-project/staff/showrunner/open-questions.md` | (free-form; written by showrunner in step 1a) |
4. **Audience slugs required.** Audience membership is defined at project activation (rule 6 — does not change mid-episode). The three slugs must be known before this step is complete. If genuinely unknown, leave `audience/` empty and add working dirs when membership is confirmed; do not proceed to step 1a without them.
5. **Confirm card library:** verify `cards/personas/INDEX.md` and `cards/locations/INDEX.md` are readable before continuing.

**1. brief expansion** *(fires before world-building)*
Screen-writer receives the brief and maps the concept-space it opens — not a plan, a field. Three outputs: (1) 4–6 alternative framings (other stories this brief could be telling); (2) 8–12 building blocks (themes, tensions, structural ingredients — raw concepts, not plot beats); (3) adjacent concepts (semantic clusters around each core term). Written to `active-project/staff/showrunner/brief-expansion.md`. Screen-writer receives this file at every subsequent planning dispatch so it draws from the full space, not only the first-order reading.

**2. world-building** — four agent-to-agent phases. fires after brief expansion. blank-slate and partial-brief projects both pass through all four phases; the difference is how much is already settled when phase 1a begins.

**1a. partial brief intake**
*Internal — showrunner does not surface this step to the human. Output is two working documents written to `active-project/staff/showrunner/`. Showrunner proceeds immediately to 1b.*

showrunner reads the human brief and produces two explicit lists:
- **decided constraints** — things already settled: world laws, character rules, arrival mechanisms, any explicit "this is how it works." no deliberation needed. go directly into world notes.
- **open questions** — things undecided that the story requires a ruling on before it can be planned. each open question becomes an input to phase 1b. ordered by dependency — questions whose answers are inputs to later questions come first.

these are written to `active-project/staff/showrunner/world-notes.md` (decided constraints) and `active-project/staff/showrunner/open-questions.md` (OQ list). they are working documents for showrunner and the planning agents, not human-facing output.

if no brief is provided (blank slate), showrunner generates the open question list from scratch: archetype, reason, elements, shape. same loop, different starting point.

for reference — story archetypes to draw from when archetype is open:

| category | examples |
|----------|---------|
| overcoming the monster | hero vs. external evil or force |
| rags to riches | rise from nothing, often with a fall before the final rise |
| the quest | journey toward a goal; the road is the story |
| voyage and return | into a strange world and back, changed |
| comedy (star-crossed) | obstacles between two people who belong together |
| tragedy (star-crossed) | obstacles that cannot be overcome; love destroyed |
| rebirth | villain or lost soul redeemed through transformation |
| coming of age | identity formed under pressure |
| revenge | wrong must be answered; cost of the answer is the drama |
| the underdog | outmatched contender earns what the favorite cannot |
| redemption | past sin drives present action toward atonement |
| sacrifice | something precious given up for something larger |
| forbidden | desire for what cannot or should not be had |
| rivalry | two forces defined by opposition; one or both changed by it |
| survival | strip everything away; what remains? |
| discovery | truth hidden; finding it changes everything |
| heist / caper | plan, execute, improvise; the team is the story |
| fish out of water | character in the wrong world reveals both worlds |
| escape | trapped; the trap is the world |
| power and corruption | ascent changes the one ascending |

**1b. open question resolution**
*Fully agent-to-agent. Human is not consulted. Showrunner resolves all open questions before proceeding to 1c.*

for each open question (in dependency order from the OQ list), showrunner runs a deliberation loop:
1. showrunner passes the question to screen-writer with context: what the story needs, what the dramatic stakes are, what constraints are already decided
2. screen-writer proposes 2–3 options, each with a one-line dramatic trade-off, and advocates for one — the option it judges most dramatically productive
3. dramatist and audience review in parallel:
   - dramatist: structural consequence of each option — which opens the most interesting arcs, which closes too much off
   - audience: entertainment value of each option — which is most compelling, which is most interesting to watch
4. showrunner synthesizes feedback and decides — screen-writer's advocacy + dramatist's structural read + audience's entertainment read all inform the call, but showrunner has final authority
5. decision recorded to `world-notes.md` as a settled constraint; carries forward into subsequent questions

3-try budget applies. if three attempts produce no acceptable option, showrunner decides from the most recent set. if the decision has series-scope consequences that showrunner cannot resolve (e.g., the options represent fundamentally different story premises and the brief gives no basis for preference), escalate to human — this is the one exception.

open questions must be resolved before phase 1c. later questions may use earlier decisions as input — resolve in dependency order.

**1c. candidate menu + cast selection**
showrunner dispatches margit with the world scope and settled constraints. margit produces a **candidate menu** — a comprehensive enumeration of all plausible candidates for this project, drawn from knowledge of the source material. the menu is not limited to what cards currently exist in the library.

each menu entry:
- proposed slug
- one-line description (role, capabilities, notable traits)
- canon status (confirmed canon / AU variant / original character)
- card status: **exists** (path) or **not yet authored**

when a candidate without a card is selected: margit authors the card immediately (full quality if source material supports it, scant if not), validates, stores, and returns it. the library is a fulfillment cache — selection triggers authoring when needed.

showrunner reads the menu and proposes a starter cast based on settled constraints and dramatic needs. screen-writer reviews for dramatic range (enough conflict vectors, enough role coverage). dramatist checks structural viability (can this cast carry the arc shape in view). standard 3-try/accept loop.

same process runs for location and condition candidates. the menu covers all three.

**1d. world-law finalization**
once open questions are resolved and cast is provisionally selected, margit authors the constraint cards:
- **law** — non-standard physics, world rules, hard limits
- **lore** — background facts that govern what is true in this world before the story begins
- **behavior** — character-level constraints spanning the series

auditor runs a constraint-consistency check on the full constraint card set before the series plan is written. clear → proceed to step 2. flag → fixer patches. escalate → showrunner decides.

this step ensures the series plan is written against real constraint cards, not informal notes.

**2. series plan** *(vague, large)*
- build series vibe-cloud
- establish series drama: the central conflict or question that spans the whole story
- showrunner passes series constraints + drama to screen-writer; screen-writer writes a chunk statement for each season; audience and dramatist review in parallel until both accept or three attempts exhausted

**3. first season plan** *(general, medium)*
- inherit series constraints and vibe-cloud; derive season-specific vibe-cloud
- establish season drama: the specific source of conflict or transformation driving this season
- showrunner passes season constraints + drama to screen-writer; screen-writer writes a chunk statement for each episode; audience and dramatist review in parallel until both accept or three attempts exhausted
- sketch the following season in broad strokes only — one chunk statement, not a plan

**4. audit** — showrunner dispatches audience + dramatist; auditor reviews
- constraints: lore is accurate, laws are obeyed, characters have motivations
- plot: is it plausible, is it entertaining, is it dramatic
- **human checkpoint:** series-level audit is the one gate requiring human sign-off. season and episode audits are agent-resolved unless escalated.
- **if rejected:** determine whether the problem is story, elements, or constraints. story → feedback to showrunner for correction at series or season level. elements or constraints → revise cards or constraint documents, re-brief showrunner.

**5. first episode plan** — see pattern: episode start

---

### pattern: season start
*fires at the beginning of each new season.*

- revisit the series plan; confirm or revise the season's chunk statement
- establish season drama: source of conflict, tension, or transformation
- derive season vibe-cloud; note deltas from series vibe-cloud
- assemble cast and constraint cards relevant to this season
- showrunner passes season constraints + drama to screen-writer; screen-writer writes a chunk statement for each episode; audience and dramatist review in parallel until both accept or three attempts exhausted
- write a loose chunk statement for the following season (horizon only)

output: season plan with episode chunk list, vibe-cloud, active cast, relevant constraint cards.

---

### pattern: episode start
*fires at the beginning of each episode.*

- take the episode's chunk statement from the season plan
- showrunner passes the episode chunk statement and active constraints to screen-writer
- screen-writer expands into a detailed episode plan: an ordered bullet list, scene by scene. each bullet is one thing that happens and generates one line in the show file. **bullet format: action beats only — `[subject] [verb] [object/location]`. no motivation clauses, no because/since/wanting-to, no internal state embedded. the impersonator supplies interiority; the bullet supplies the beat.**
- audience and dramatist review in parallel (persistent subagents); both must accept or three screen-writer attempts are exhausted
- every bullet should be legible against both the series plan and the season plan
- **prep cast:** spawn impersonators for active characters; load persona cards
- **prep studio:** load location, prop, and condition cards; establish environment state
- **prep show file:** open fresh show file; write scene context header
- **prep audience:** confirm audience critic config is ready

output: episode plan (bullet list), active impersonator set, loaded cards, open show file.

---
### **law** — universal rules of the world; non-standard physics, magic systems, hard limits
### **lore** — background and history; what happened before the story began
### **behavior** — how persons act in general and specifically; motivations, limits, voice

---

## plot
### (why) **reason** — the thematic and narrative purpose of the story
### (what) **elements** — the people, places, objects, and forces at play
### (how) **shape** — the structure and pacing of how events unfold

---

## agents

### **showrunner** (process director)
governs the production process. holds the plan, the constraints, and the sequence of who does what next. the only agent that talks directly to the human. persists across episodes and seasons �� not session-scoped.

responsibilities:
- holds series memory, season plan, and active episode plan across sessions
- reads the episode plan bullet by bullet and identifies the recipient (actor or studio)
- passes each bullet to coach, who translates it into a prompt for the recipient
- receives audience verdict and, on reject, dispatches coach with feedback to rework the prompt
- manages the three-try budget per line
- escalates to human only when a fault cannot be resolved at season scope
- does not translate feedback into prompts directly — that is coach's job
> maps to: naomi-equivalent, extended with long-horizon memory at series scope.

### **screen-writer**
generates the bullet plan at each planning level. works with dramatist and audience (as parallel persistent subagents) to produce a plan both will accept.

- receives a general prompt and constraints from showrunner (format TBD)
- produces a plan: at series level, bullets are season chunks; at season level, bullets are episode chunks; at episode level, bullets are lines
- audience and dramatist review in parallel, each persisting their own memory in active-project
- both provide feedback on what worked and what didn't; screen-writer revises
- iterates until audience and dramatist both accept, or until three screen-writer attempts are exhausted
- if three attempts hit without agreement: proceed with most recent plan, flag for human review

> new agent. audience and dramatist are parallel persistent subagents during planning; see their entries below.

### **coach**
translates a bullet point and any feedback into an actionable prompt for an impersonator. sits between showrunner and the impersonator on every line.

**flow during episode shoot:**
1. showrunner reads bullet, identifies recipient impersonator, passes bullet to coach
2. coach composes a prompt suited to the impersonator's persona and the scene context; sends to impersonator
3. impersonator performs: appends line to show file
4. audience watches and reacts: accept → next bullet. reject → showrunner deletes last line from show file, dispatches coach with original bullet + audience feedback
5. coach revises the prompt accounting for what failed and why; sends updated prompt to impersonator
6. repeat up to three total attempts

**impersonator rejection:** if the impersonator rejects the prompt as impossible or out of character, they note reasons. coach receives the rejection + original bullet and reformulates. this consumes from the shared three-try budget.

coach does not perform. coach does not judge quality. coach turns intent + feedback into the clearest possible prompt for the recipient.

> new agent.

### **impersonator** (episode sub-agent)
character primitive. one impersonator per active character in an episode. spawned at episode start, persists through episode close, then released.

each impersonator:
- loads its persona card (voice, behavior, motivations, limits)
- receives prompts from coach and responds in character
- appends response to the show file; records any state changes it is responsible for

**the impersonator does not know they are narrating.** when prompted to describe surroundings or environment, they describe what is interesting or notable to them from their own perspective. expository quality is an artifact of their character, not a mode they are placed in. the editor handles the prose in wrap.

**impersonator rejection:** if a prompt asks for something impossible or out of character, the impersonator rejects with reasons. coach receives the rejection and reformulates. consumes from the three-try budget.

**limited agency:** impersonators act within their persona constraints. they do not drive plot.

> import and adapt from brighid-creative-writing impersonator agent.

### **audience** (persistent subagent)
reader-surrogate personas that watch the show and report what they feel. persistent memory in active-project across the episode.

**during planning:** parallel subagent to dramatist. reviews screen-writer's bullet plan and provides feedback on entertainment shape — what lands, what falls flat, what is confusing or boring. memory persists so feedback builds across iterations.

**during shoot:** watches each new line as it is written. accept → next bullet. reject → feedback to showrunner, line deleted, coach dispatched with feedback to rework prompt.

**during wrap:** reviews the full flagged show file for lines that are inert, off-register, or actively bad. flags with reason; does not automatically trigger rewrite.

> import and adapt from `audience-critic` config in brighid-creative-writing. needs review for format changes.

### **dramatist** (persistent subagent)
structural critic. applies form categorically to arc — escalation shape, rise-peak-fall, problem resolution, dramatic viability. persistent memory in active-project.

**during planning:** parallel subagent to audience. reviews screen-writer's bullet plan for structural integrity. provides feedback on what the structure is doing well and where it fails. memory persists across iterations.

**during wrap:** checks the episode against drama thresholds (see and-wrap).

> import and adapt from `dramatist-critic` config in brighid-creative-writing. needs review for format changes.

### **auditor**
constraint and consistency checker. fires at defined audit gates (series plan, season plan, episode wrap) and on-demand when showrunner suspects a problem.

**what auditor checks:**
- law: are universal rules of the world obeyed?
- lore: is the history and background accurate and internally consistent?
- behavior: do characters act within their established motivations and limits?
- plot: is it plausible, entertaining, dramatic?
- state: does the show file reflect what the state and memory records say is true?

**how auditor works:**
auditor runs as a fork — showrunner context is preserved before dispatch, audit findings are returned as a report, fork is discarded. findings do not bloat showrunner's working memory.

findings are classified:
- **pass** — no action
- **flag** — noted for editor or future reference, does not block
- **fault** — routed to fixer with specific scope and reason
- **escalate** — problem is at a higher scope than the current level; routed to showrunner for human decision

> new agent, no direct import. design informed by brighid-creative-writing system-critic config.

### **fixer**
targeted correction agent. receives a fault from auditor with scope and reason, makes the minimum change required to resolve it.

**fixer scope:**
- *line:* rewrite or patch a specific line in the show file
- *line:* revise a bullet in the episode plan and re-run the affected impersonator prompt
- *episode:* structural revision to the episode plan; may require partial reshoot
- *escalate:* fault cannot be resolved at episode scope → returned to showrunner for season-level decision

fixer does not editorialize. it resolves the specific fault it was handed and reports back. if fixing one fault would introduce another, fixer flags both and waits for direction rather than chaining repairs autonomously.

> new agent, no direct import.

### **margit** (librarian)
card warehouse. preserves, indexes, validates, and composes cards. no destructive overwrite — pre- and post-mutation both kept.
> direct import from brighid-creative-writing.

### **studio** (oskar, redefined)
set and environment manager. handles all on-scene changes and state that are not owned by an actor impersonator.

**departure from brighid-creative-writing:** in and-shoot, studio does not administrate trailers, memory schemas, or process. that was oskar's prior role. studio here is narrower and more concrete: it owns the physical and environmental layer of the scene.

**what studio owns:**
- props (position, state, availability)
- locations (layout, access, ambient conditions)
- conditions (lighting, weather, time of day, environmental events)
- any state change that no impersonator is responsible for

**set formation:**
showrunner holds a general idea of what the set looks like — rough, intentional, directorial. studio receives that general idea and gives it actual form: detailed spatial layout, sensory specifics, prop placement, ambient conditions. that detailed form is written to memory and state (not directly to the show file) and becomes the prompt plan for how the set is described.

**studio actions in the show file:**
studio does not write set description directly to the show file. instead: showrunner takes the POV impersonator (first or third person depending on the scene's perspective) and prompts that impersonator to describe the environment however seems relevant to them. the set becomes visible through the character's perception, not as a stage direction.

**studio action types:**
- *set formation:* receive showrunner's general set concept → produce detailed memory + state + prompt plan
- *state change:* record environmental or prop change triggered by a line (quake, lights cut, door opens unattended, etc.)
- *condition update:* advance time-of-day, weather, or ambient condition between scenes

studio records all changes to state and memory. nothing in the environment changes without studio recording it — same rule as impersonators for actors.

---

## state rules

### nothing moves unless recorded
**if an actor or studio did not record a change, the change did not happen.**

- character position, emotional state, physical condition, held objects — all persist unchanged until an impersonator records an action that changes them
- environmental state (lighting, weather, room layout, time of day) persists unchanged until a studio action records a change
- showrunner may not silently advance state between lines. every change must be authored by the responsible impersonator or studio action and written to the show file
- this applies equally to implied changes ("he crossed the room") and explicit ones — both must be recorded by the appropriate actor before showrunner can treat them as true
- if a line requires a state change but the responsible impersonator has not yet written it, showrunner waits or issues the prompt — it does not assume

this rule is the consistency backbone. it is what allows the audit to catch lore violations and the editor to catch continuity errors.

---

## the show file

the show file is the episode manuscript, written line by line. each bullet in the episode plan produces one line. the file is append-only during shoot.

- showrunner writes scene context headers between sections
- each line is written by either an actor impersonator or the POV impersonator (for environment changes)
- rejected lines are deleted by showrunner before the revised prompt is issued — the file never accumulates failed attempts
- lines that exhausted all tries without resolution are marked `[⚑ needs edit]` and left in place
- at episode close, the show file is the raw draft passed to wrap

---

## the three-try rule

each line gets one attempt plus up to two reworks — three total. the budget is shared across all failure types for that line:
- audience rejects the line → feedback issued, rework (consumes 1)
- impersonator rejects the prompt → revised prompt crafted, rework (consumes 1)

if the budget is exhausted: keep the most recent attempt, mark it `[⚑ needs edit]`, and move to the next bullet. do not stall the episode for a single line. problems are collected and addressed in wrap, not during shoot.

---

## episode shoot
the show file is written line by line. each bullet in the episode plan drives one line.

for each bullet:
1. showrunner reads the bullet and identifies the recipient:
   - **actor line:** an impersonator acts, speaks, or reacts
   - **environment line:** studio records the state change to memory and state; showrunner identifies the POV impersonator who will perceive and describe it
2. showrunner passes the bullet to coach; coach composes a prompt and sends it to the recipient
3. impersonator appends line to show file
4. audience reviews the new line:
   - **accept** → next bullet
   - **reject** → showrunner deletes the line from show file; dispatches coach with original bullet + audience feedback; coach revises prompt (attempt 2)
5. if impersonator rejects the prompt: reasons noted; coach receives rejection + original bullet and reformulates (attempt 2 or 3)
6. if all three attempts exhausted: mark line `[⚑ needs edit]`, move to next bullet

repeat until all bullets are written. show file is the episode draft.

---

## and-wrap

triggered when showrunner reaches the final bullet of the episode plan. the show file is complete but raw. wrap cleans, validates, and closes the episode before the next one can begin.

### 1. dramatist — structure review
dramatist checks the episode against four drama thresholds:
- **problem solves:** the episode's central problem reaches resolution (even if partial or pyrrhic)
- **end state ≠ start state:** at least one meaningful thing has changed — character, relationship, situation, world
- **builds toward season finale:** the episode advances or complicates the season arc
- **builds toward series finale:** the episode is legible in terms of the long game

if any threshold fails: flagged to showrunner for escalation decision. minor failures may be patched at episode scope; structural failures escalate to season replanning.

### 2. dramatist — scene boundary flagging
dramatist marks the show file with scene start and scene end points.

- everything **inside** the flags is episode content — kept, edited, published
- everything **outside** the flags (pre-scene setup, post-scene trailing) is cut during wrap
- **the flags themselves are not cut** — they remain as momentum anchors for the wrap process, giving the editor context on how each scene opens and closes

flagged format: `[scene-start: <brief label>]` / `[scene-end: <brief label>]`

### 3. audience — entertainment review
audience reads the flagged show file and identifies:
- lines that land flat or feel inert
- moments that break immersion or feel out of register with the vibe-cloud
- any exchanges that seem actively bad (confusing, boring, false)

flagged lines are marked `[⚑ audience: <reason>]` for possible rework. flagging does not automatically trigger a rewrite — showrunner decides whether to patch now or carry forward to editing.

### 4. auditor — constraints audit
showrunner dispatches auditor (as a fork) to compare the show file against:
- active constraints (law, lore, behavior cards)
- the episode plan (what was expected vs. what was written)
- state and memory records (does the show file reflect what actually happened?)

auditor returns a classified report: passes, flags, faults, escalations. fork is discarded; only the report travels back to showrunner.

faults are routed to fixer with scope and reason. escalations go to showrunner for decision. flags are passed to editor as advisory notes.

### 5. editor — final draft
editor receives the flagged show file with all markings intact:
- applies scene boundary cuts (removes content outside flags, preserves the flags as context)
- addresses `[⚑ needs edit]` lines from three-try failures
- considers `[⚑ audience: ...]` flags — rewrites where warranted, leaves where the flag is overcautious
- prose pass: economy, continuity, tense, blocking, voice consistency
- saves final draft of episode as the closed manuscript

editor does not add content. editor does not make plot decisions. editor tightens what is there.

### 6. memory — minimal movement
after episode close, **memory is not advanced unless there is a reason.**

showrunner verifies:
- **actor memory close (mandatory):** for each actor active this episode: append significant events (relationship shifts, discoveries, arc notes) to `active-project/actors/<slug>/ltm.md`; prune `stm.md` to ~10 items (overwrite, not append). required at every episode close per memory schema.
- **timeskip:** if the next episode picks up significantly later in time, update character state, world state, and any cards that would have changed during the gap
- **major off-scene event:** if something significant happened off-screen between episodes, record it
- **default:** no timeskip, no off-scene event → memory stays exactly where the show file left it. the next episode picks up from that state without ceremony.

this rule keeps continuity tight and prevents state drift between episodes.

