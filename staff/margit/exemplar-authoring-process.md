# Persona-Exemplar Authoring + QC Process

Margit-owned process for authoring, validating, and storing persona-exemplars (the live-channel voice prime introduced by PROP-0005 / DEC-0016 + PROP-0005-A / DEC-0017).

Schema authority: `schemas/persona-exemplar.schema.md`.

---

## Origin × Usage matrix

Where an exemplar lives depends on where its persona comes from and where the exemplar is consumed:

| Persona origin | Consumed in | Exemplar location | Authoring trigger |
|---|---|---|---|
| Library persona (no variant) | Library reuse, any project | `cards/persona-exemplars/<slug>.md` | First time the persona is dispatched in production. Author at /and-cast Phase 4 (or at audience selection during /and-project) if absent. |
| Library persona | Active project (no project-bound override needed) | Library entry serves | No authoring; reuse library exemplar. |
| Library persona | Active project + voice tuning specific to project | `active-project/persona-exemplars/<slug>.md` | Authored at /and-cast Phase 4 (or by principal directive) when the library exemplar doesn't fit the project's voice register. |
| Project variant (`variant-of: <base>`) | Active project | `active-project/persona-exemplars/<slug>.md` | Authored at /and-cast Phase 4 when the variant is provisioned. Base persona's library exemplar is consulted but not reused — variant voice tells differ. |
| Project-original (no library precedent) | Active project | `active-project/persona-exemplars/<slug>.md` | Authored at /and-cast Phase 4 alongside the new card. |
| Project-original earning reuse | Promotion to library | Move `active-project/persona-exemplars/<slug>.md` → `cards/persona-exemplars/<slug>.md` | Margit promotion routine. Triggered when the persona is identified as a library candidate (cross-project value). |

**Dispatch resolution order** (per schema): project-bound override beats library. The library entry is the always-present fallback for library personas; project-bound exists for tuning, not redundancy.

---

## Authoring workflow

For each new exemplar:

### 1. Inputs

Read in this order:

- The persona card (`<card-path>`) — full read. Voice section, forbidden registers, taste, hot-buttons, hard fences, action costs, signature moves, vibe seeds where present.
- Any LTM the persona has, if relevant to voice (e.g. accumulated tics from prior usage).
- The persona's prior exemplar if one exists (you may be revising, not authoring fresh).
- The consuming agent's definition (`.claude/agents/<impersonator|audience>.md`) for context on how the exemplar will be used.

### 2. Identify load-bearing features

Pull 2-3 specific voice features from the card that the exemplar must demonstrate. Not a comprehensive list — the load-bearing ones. Examples:

- Impersonator: a syntactic tic (Taylor's recursive filing cadence: "X, which was Y, which meant Z"); a behavioral tell (her body acting before her analytical voice reasserts); a forbidden-register the exemplar must visibly avoid (no Earth-Bet proper nouns).
- Audience: a noticing-pattern (cape-fic-reader's tactical mid-paragraph interruptions: "Wait."); a hot-button firing form (the precise way they call out an unearned reveal); a fatigue signal (skim-cue when the prose stalls).

If you cannot name 2-3 specific features after reading the card, the card is thinner than it looks and the exemplar will under-deliver. Flag this back to the principal before authoring; the right move is often to thicken the card first.

### 3. Choose the scene/context

The exemplar's content must be **distinct from any artifact the consumer is likely to be working on**.

- Impersonator exemplars: scene NOT in any active chapter. A moment from the character's life, in-period, in-setting, but not adjacent to current production. For projects with no prior chapters, invent a hypothetical that fits the character's established arc shape.
- Audience exemplars: a hypothetical artifact the persona is reviewing. Generic enough to demonstrate stance, specific enough to demonstrate hot-button firing. Do not use the active project's actual chapters.
- Voice exemplars (PROP-0003-A — separate format): content adjacent-to-but-not-from the project. High content-match wins per the v16 vs v17 experimental finding, but adjacency without overlap is the discipline.

### 4. Draft the passage

150-350 words. Show the voice in motion. Resist:

- Meta-commentary describing the character ("She was always the one to notice...").
- Exposition of the character's psychology.
- Sentences that name the features rather than executing them.

Demonstrate. The exemplar's whole job is to be the voice, not to describe it. The card already describes it.

### 5. Author the frontmatter

Per `schemas/persona-exemplar.schema.md`. Required fields:

- `name`, `persona-ref`, `class: persona-exemplar`
- `purpose` — one-line statement
- `content-match` — high / medium / low with one-line scene description
- `authored-by` — honest attribution
- `length` — approximate word count
- `fences` — minimum two: no-content-import + what-transfers-vs-what-doesn't

Optional but required-when-applicable:

- `dispatch-status: excluded` + `excluded-by` + `excluded-reason` — for exemplars retained as design artifacts but failing experimental validation.
- `supersedes` / `superseded_by` — for revisions.

### 6. Save to the right location

Per the origin × usage matrix above. Default: `cards/persona-exemplars/<slug>.md` for library personas; `active-project/persona-exemplars/<slug>.md` for project-bound.

### 7. Margit validation

After save, margit runs the QC checklist (next section). Validation failures route back to the author for revision. No invalid exemplar enters dispatch resolution.

---

## QC checklist

Margit runs this on every new or revised exemplar before promotion to dispatch eligibility.

### Frontmatter validation

- [ ] All required fields present per schema.
- [ ] `name` is unique within `cards/persona-exemplars/` (or `active-project/persona-exemplars/` if project-bound).
- [ ] `persona-ref` resolves to an existing persona card (library or project).
- [ ] `class: persona-exemplar` (literal).
- [ ] `content-match` value is one of {high, medium, low}.
- [ ] `length` is within 150-350 words (count the body, not frontmatter). Tolerances: ±10% acceptable; ±20% requires a justification in `purpose` or a flag to principal.
- [ ] `fences` has at least two entries, covering content-import and what-transfers-vs-what-doesn't.
- [ ] If `dispatch-status: excluded`: `excluded-by` and `excluded-reason` are populated.
- [ ] If `supersedes` is set: prior version exists at the named path and is preserved (not deleted).

### Body validation

- [ ] Body opens with `# Exemplar — <persona display name>` header.
- [ ] Passage demonstrates 2-3 load-bearing voice features from the card.
- [ ] No content overlap with active chapter / target artifact (margit cross-references against `active-project/theater/` and `active-project/draft/` where relevant).
- [ ] No violation of card hard fences. Special check: forbidden-registers section of the card MUST NOT appear in the exemplar. E.g. an exemplar for `taylor-hebert-kl-122ac` containing Earth-Bet proper nouns is a HARD reject.
- [ ] No meta-commentary in passage body — no sentences describing the persona instead of being the persona.
- [ ] For audience persona exemplars: the full output shape (live-read + verdict + flags + what-worked) is demonstrable from the exemplar OR the exemplar explicitly demonstrates a representative subset with a `purpose` note explaining the choice.
- [ ] For impersonator exemplars: voice in motion, not described. Body opens with action or perception, not interior analysis (per impersonator prose-posture rules).

### Consumer-fit validation

- [ ] If exemplar is for an impersonator: a sample 3-line generation against an unrelated prompt could pattern-match this exemplar without leaking exemplar content.
- [ ] If exemplar is for an audience persona: a sample review against the chapter currently in active-project would pattern-match this exemplar without using the exemplar's specific hypothetical-artifact details.
- [ ] If exemplar is for a Tier-2 (deferred) consumer: HARD reject. Tier-2 exemplars require a separate experiment per DEC-0017 before authoring proceeds. The orchestrator-critic design artifact at `cards/persona-exemplars/orchestrator-critic.md` is the canonical exclusion model.

### Promotion gate (active-project → library)

When promoting a project-bound exemplar to the library:

- [ ] The persona itself is library-promotable (cross-project value, no project-specific content in the card).
- [ ] The exemplar's content-match dimension is general enough that a different project consuming this persona would still benefit. Heavy project-specific texture in the exemplar means it stays project-bound.
- [ ] Prior library exemplar (if any) is preserved via `supersedes`.

---

## Failure modes margit watches for

The following patterns recur and have been observed in authored exemplars:

1. **Cadence over-fit** — exemplar's specific structural tic (e.g. "two-out-of-three" tally form) becomes a template the consuming agent copies wholesale across unrelated reviews. Fix: add a `fences` rule prohibiting form-copying, vary the exemplar's structural tic deliberately so no single shape dominates.
2. **Performative theatricality** — exemplar drifts into "what the persona would *sound* like" performance rather than executing flat. Fix: ruthlessly cut adjectives, italics, and rhetorical flourishes from the passage. The persona should be unselfconscious in the exemplar.
3. **Prescription atrophy (audience exemplars)** — exemplar over-emphasizes the *reading* and under-emphasizes the *prescription* (what the author should do). Fix: ensure the verdict + flags sections in the exemplar carry concrete, actionable language ("Cut by a third"; "Promote it"; "Move the timestamp").
4. **Voice-fidelity preservation hurting Pass 2 / revision (renderer-style only)** — a renderer authored to match an exemplar may resist trimming sentences that match the exemplar even when they should be cut. Fix: when authoring renderer voice exemplars, include at least one short arrival sentence among the long branching ones, so the consuming renderer learns the short-sentence is also voice-fidelity.
5. **Tier-leak** — an exemplar gets authored for a Tier-2 consumer by mistake. HARD reject; the existing experimental evidence is that Tier-2 exemplars in current form actively regress consumer output.

---

## Authoring cadence

- At `/and-project` activation: audience trio exemplars must exist (library or authored). Margit checks at Phase 1c and blocks activation if any audience persona lacks an exemplar.
- At `/and-cast` Phase 4 (provisioning): every actor provisioned must either have a library exemplar OR get a project-bound exemplar authored before /and-cast Phase 5 (audit checkpoint). Margit gates Phase 5 on exemplar completeness.
- At `/and-series` (voice exemplar — separate format per PROP-0003-A): the series voice exemplar is optional but recommended; absence means stitcher Phase 1 forks run un-primed.
- On card revision: margit flags the paired exemplar for review. Revision is not auto-triggered but is recommended on any voice-section update.
- On dispatch failure / quality regression in production: principal may flag the exemplar for revision; margit routes back through this process.

---

## Out of scope (do not author)

- Exemplars for Tier-2 consumers (orchestrator-critic, dramatist, auditor, editor). The `cards/persona-exemplars/orchestrator-critic.md` file exists as a design artifact and is marked `dispatch-status: excluded`. Do not author additional Tier-2 exemplars without principal directive + a fresh experimental basis.
- Exemplars for Tier-3 consumers (showrunner, margit, fixer). No voice/output-shape channel exists for these agents.
- Exemplars for non-persona assets (cards/locations, cards/props, cards/conditions, cards/behaviors). These have their own representation discipline; exemplars are a persona-only concept.
