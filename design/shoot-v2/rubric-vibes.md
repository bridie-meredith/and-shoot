# Vibes-Updates Rubric V1 LOCKED 2026-05-07

Tunes the **vibes-updates** facet (`active-project/theater/facets/vibes.md`).

Vibes are **persistent operator-bias tags** that stick to entities (actors, locations, props) or to scopes (episode / season / series). Each vibe is a `keyword: [token-bundle]` — keyword indexes; tokens are word-algebra read by downstream operators. Vibes are **read** by dialogue-writer / studio / NI / feeling / metaphor / behavior-pack agents before generation; they are **never rendered as prose**. They bias the writer; they do not appear on the page.

This is the loosest facet to date by sparsity (no upper ceiling). It is also the only facet authored by **showrunner** (cross-cutting all-vibe-cloud visibility is the licensing premise). Reviewer is **mechanic auditor only** — no dialect audience, because vibes are not voice-bearing.

---

## Schema content shape (V1 — schema-revision-at-ship pattern; ships same commit as Phase 5)

```
<id> [@<proto-line-id>] <target> <op> <keyword>: [<token>, <token>, ...] | licensed-by: <source>[, <source>...]
```

- `<id>` — monotonic positive integer, scoped per facet file.
- `[@<proto-line-id>]` — **optional**. Required when the vibe is licensed by an on-screen beat. Omitted when licensed by off-screen / pre-episode / inter-episode reflective context.
- `<target>` — one of:
  - `actor:<slug>` — actor card slug
  - `loc:<slug>` — location card slug
  - `prop:<slug>` — prop card slug
  - `episode` | `season` | `series` — scope target (ambient atmosphere; rare relative to entity targets)
- `<op>` — one of:
  - `+` add new vibe-keyword to target's vibe-set (token-bundle required)
  - `-` retire vibe-keyword (token-bundle omitted; form: `<target> - <keyword>`)
  - `++` extend tokens for existing keyword (token-bundle required; appended to existing)
- `<keyword>` — hyphenated index handle. Semantic. One per vibe.
- `<token>` — hyphenated word-algebra phrase. Comma-separated within `[...]`. No prose, no articles, no full sentences. Word-algebra only.
- `<source>` — one or more of:
  - `state-update:<id>` (canonical state change as licensing event)
  - `memory:<id>` (callback/recognition as licensing event)
  - `feeling:<id>` (somatic tell as licensing event)
  - `proto:<id>` (direct beat reference when no upstream facet captures)
  - `tens:<reading>` (peak-tension as supporting licensing)
  - `canon:<gloss>` (off-screen / pre-episode canon context)
  - `world-build:<gloss>` (series-baseline / world-build context)

Multi-source allowed and encouraged. ≥1 source required (no unlicensed entries).

---

## Required gates (mechanic-checkable)

1. **Target validity.** Slug exists in card library OR target is one of `episode | season | series`.
2. **Op coherence.**
   - `+` requires keyword absent from target's current vibe-set.
   - `-` requires keyword present in target's vibe-set.
   - `++` requires keyword present; new tokens must not duplicate existing tokens.
3. **Token-bundle non-empty** for `+` and `++`. Tokens are word-algebra (hyphenated phrases). No prose tokens (see AP8).
4. **Licensed-by resolvable.** Each `<source>` points to an existing facet entry, proto-line, or named canon/world-build context. No `?` placeholders.
5. **Permanence.** Vibes are permanent stickers. A vibe added in s01e01 persists to s01e02+ unless explicitly retired with `-`. Transient mood is not a vibe (see AP1).
6. **Operator-bias actionability.** The `keyword: [tokens]` must imply downstream operator behavior — dialogue voice register / studio palette / feeling somatic-bias / NI interest-pattern / behavior-pack register / metaphor licensing context. A vibe no downstream operator can act on is malformed.
7. **Cross-target fan-out coherence.** A vibe-causing event affecting multiple entities must fire across the affected entities (typically: POV character + on-stage co-witnesses + episode-scope + on-stage location if charged). Mechanic checks fan-out against the licensing event's affected-entity set.

---

## Anti-patterns

- **AP1 transient-as-vibe.** Mood / weather / scene-tone / momentary feeling. These belong to sensory / feeling / tens facets. Vibes are permanent. Test: would this still be true at s01e02 open? If no, refuse.
- **AP2 state-restated-as-vibe.** Canonical state-update or condition-card content restated as vibe. State-updates writes facts; vibes derive *qualitative consequences* from facts. Example: state-updates fires `taylor.administrative-status: child-or-ward → provisional-labor-eligible`. Vibes does NOT write `+provisional-labor-eligible`. Vibes writes `+the-naming: [function-given-aloud, irrevocable, no-going-back-in-this-direction, the-form-fits]` — the *qualitative-consequence* layer.
- **AP3 feeling-as-vibe.** Somatic tells (`+heart-racing`, `+breath-held`) are feeling-flags, not vibes. Vibes are durable; somatic tells are momentary.
- **AP4 unlicensed-vibe.** No `licensed-by:` source. Refuse.
- **AP5 duplicate-add.** Target already carries the keyword. Use `++` to extend; `+` is malformed.
- **AP6 wrong-target.** Locating a vibe on an entity not affected by the licensing event (e.g., the-yard-as-witness on an actor who left the yard before the witness-event occurred; charring on actor:fire-survivor instead of loc:burned-tower).
- **AP7 vague-token.** Tokens like `intense`, `bad`, `strong`, `important`, `meaningful`. These do not encode operator behavior. Tokens must resolve to a specific bias.
- **AP8 prose-token.** Full-sentence tokens, articles (`the-`, `a-` are fine as compound-prefixes; `the cart was outside` is not), soft connectives, narrator-voice prose. Tokens are hyphenated word-algebra only. Multi-clause-as-token forbidden. Maximum: a noun-phrase or short clausal compression bound by hyphens.
- **AP9 abstract-scope-when-entity-fits.** Writing `episode +haunted` when really `loc:harrenhal +haunted` is the entity-bound truth. Prefer entity targets; reserve scope targets for genuinely ambient atmosphere.
- **AP10 op-misuse.** `-` on absent keyword; `++` without prior `+` on this target; `=` (no replace op exists).
- **AP11 token-overlap on `++`.** Tokens appended via `++` that duplicate tokens already in the existing bundle. Token-set difference required.
- **AP12 fan-out-skipped.** A vibe-causing event that demonstrably affects N entities only writes against M < N (typical sin: write only against POV actor; skip co-witnesses or scope target). Mechanic enforces fan-out coherence.
- **AP13 prose-narration-in-tokens.** Token reads as a sentence the narrator might say (`the-officer-was-efficient-and-she-knew-it`). Compress: `efficient-not-hostile`. Word algebra is compression, not narration.

---

## Sparsity / volume

- **No upper ceiling.** Vibes do not appear in prose; cost-per-fire is structurally lower than any other facet.
- **Floor:** 0. (Zero-fires episode is technically valid but vanishingly rare in plot-bearing episodes.)
- **Expected s01e01 yield:** ~12-25 entries.

Per-target stratification (informative):
- Entity-target adds (`actor:` / `loc:` / `prop:`): 70-90% of entries
- Episode-scope adds: 10-25%
- Season-scope adds: 0-3 per s01e01-class
- Series-scope adds: 0-1 per s01e01-class
- Removals (`-`): 0-2 per episode (rare; only for genuine reversal events)
- Extensions (`++`): 0-3 per episode (when an existing vibe deepens via new event)

---

## Functional registers (informative; mechanic checks coherence)

Each vibe biases at least one downstream operator. Registers describe *which* operator the vibe biases:

- **trauma / mark / handicap** — biases dialogue-writer fork voice + feeling somatic-tells + behavior-pack tics on target actor.
- **reputation / standing / signature** — biases NPC dialogue-writer forks toward target; biases NI fork interest-patterns.
- **haunting / atmosphere / charge** — biases studio environmental palette + sensory flag selection on target location.
- **avoidance / association / orientation** — biases studio location-routing + behavior-pack approach/avoid for target.
- **aesthetic / texture / register** — biases studio descriptive palette + dialogue-writer descriptive register.
- **arc / position / role-shift** — biases all operators on target's narrative positioning (e.g., the-naming biases everyone reading taylor as labeled-asset).

The mechanic does not score register-fit per se; it checks that *some* downstream operator could act on the vibe (gate 6).

---

## Cross-facet contract

### Read side — vibes-updates consume

- `state-update:<id>` — canonical state changes are *the* primary vibe-source. State change → derived qualitative consequence as vibe. Anchor source for most fires.
- `memory:<id>` — callbacks/recognitions trigger vibe-fires (a recognition is itself a memorable event-class).
- `feeling:<id>` — somatic costs accumulate as vibes (e.g., `+cost-made-visible` after a feeling-fire that exposes interior cost).
- `proto:<id>` — direct beat citation when no upstream facet captures.
- `tens:<reading>` — supporting; peak-tension co-cites tighten licensing.
- `canon:<gloss>` — off-screen / pre-episode events.
- `world-build:<gloss>` — series-baseline; rare during episode authoring.

### Write side — vibes-updates bias

- **dialogue-writer fork** reads target actor's vibe-set before voice/dialogue generation.
- **studio** reads location's vibe-set before environmental description; reads prop's vibe-set before prop-state description.
- **feeling fork** reads target actor's vibe-set before somatic-tell selection.
- **NI fork** reads POV actor's vibe-set before interest-pattern selection.
- **metaphor / sensory authors** read relevant vibe-sets as licensing context.
- **behavior-pack consumers** read actor's vibe-set as register-modifier.

The vibe-update is the *write* side; downstream operator's reads are ambient and not facet-captured.

---

## Author privilege

**Author: showrunner only.** Cross-cutting all-vibe-cloud visibility is the licensing premise. No per-character forks (which would defeat the design). Mechanic auditor verifies the showrunner's privilege is *used*: entries demonstrate cross-target fan-out coherence, scope-target appropriateness, and licensing-chain visibility.

---

## Cross-facet contract — specific to vibes vs adjacent facets

- **vs state-updates.** State-updates writes the *fact* of state change. Vibes writes the *qualitative consequence* of the state change. Both fire on the same event but never duplicate content. Mechanic enforces token-content non-overlap.
- **vs memory-flags.** Memory-flags fires on POV recognition of a prior monument. Vibes can co-fire (`+the-yard-as-witness` after a recognition-event), licensing through `memory:<id>`. Distinguish: memory is the *recognition*; vibes is the *durable consequence*.
- **vs feeling-flags.** Feeling fires on a somatic tell at a beat. Vibes accumulate the *durable consequence* of repeated/load-bearing feeling-events. Distinguish: feeling is the moment; vibes is the residue.
- **vs sensory-flags.** Sensory is per-beat perceptual delta. Vibes are not sensory. No overlap.
- **vs metaphor / NI.** Metaphor and NI *consume* vibes (read-side). Vibes is upstream. Vibes does not cite NI/metaphor (unless rare retroactive case).

---

## Inter-episode authoring (showrunner reflective passes)

The showrunner may author vibes-updates between episodes — a reflective pass that captures off-screen / aggregate / canon-derived vibes. These entries omit the `@<proto-line-id>` anchor and license through `canon:<gloss>` or `world-build:<gloss>` or aggregate `proto:<range>` references. The Phase 0 corpus includes both on-screen-anchored and reflective-pass entries.

---

## Phase 0 corpus expectations for s01e01

Five vibe-causing events identified across the 77-beat episode. Expected ~16-20 entries fanned across affected entities:

| Event | Beats | Keyword | Affected targets | Expected fires |
|---|---|---|---|---|
| E1: officer-arrives-and-processes-census | @11-@48 | `the-machinery-arrives` | actor:taylor, actor:mira, actor:edric, actor:census-officer, episode | 5 |
| E2: letter-presented-and-returned | @28-@45 | `the-letter` | actor:taylor, episode | 2 |
| E3: name-entered-as-provisional-labor-eligible | @47-@48 | `the-naming` | actor:taylor, episode | 2 |
| E4: septon-does-not-emerge | @31-@33 | `the-septon-as-absence` | actor:taylor, actor:septon-dying-protector, episode | 3 |
| E5: yard-witnesses-decline-help | @51-@57 | `the-yard-as-witness` | actor:taylor, actor:mira, actor:edric, episode | 4 |

Plus possible:
- `loc:westerosi-smallfolk-village-common` `+the-machinery-arrives` (location absorbs episode-event) — optional.
- `prop:oc-letter` extension or vibe — optional (the letter-as-useless-object vibe).
- 1-2 `++` extensions where pre-existing keywords get new tokens from s01e01 events.

Expected baseline yield: **~16-20 entries**. Range tolerance: 12-30 (mechanic does not enforce a hard ceiling).

Calibration anchors (used for both writer and reviewer):
- **C1** `actor:taylor +the-machinery-arrives` — multi-target fan-out anchor (the most-fanned-out event).
- **C2** `actor:septon-dying-protector +the-septon-as-absence` — non-POV co-target on E4 (does the showrunner remember to write against the absent actor?).
- **C3** `actor:mira +the-yard-as-witness` — non-POV co-target on E5 (the witness-from-the-other-side fan-out).
- **C4** `episode +the-naming` — episode-scope target distinct from any entity (does the showrunner stratify scope correctly?).

---

## Status

V1 LOCKED 2026-05-07. Schema content-shape revision queued for ship at Phase 5 (per metaphor / sensory / feeling precedent: schema text revised same commit as facet file).

Pre-Phase-0 user nudges absorbed (this run, before Phase 0 dispatch):
1. Vibes are permanent stickers, not drifting tone-clouds.
2. Vibes attach to entities (actors / locations / props), not only abstract scopes.
3. Vibes are independent of screen time (off-screen-licensed entries valid).
4. Vibes are liberal compared to other facets (no upper ceiling).
5. Vibes are not rendered in prose; they bias operators.
6. Format is `keyword: [token-bundle]` machine-readable word-algebra (not human prose).

Six nudges absorbed pre-Phase-0. Pattern continues from sensory/feeling/metaphor.
# Vibes-Updates Rubric — V1.1 Patch

Applied to: `design/shoot-v2/rubric-vibes.md` (V1 LOCKED 2026-05-07)
Patch authored: Phase 4 (post-RF-001 resolution + Phase 3 seam findings)
Ship protocol: V1.1 text ships same commit as Phase 5 facet file, per schema-revision-at-ship pattern.

---

## Patch 1 — §"Required gates" gate 2 amendment: pre-seeded project behavior

**Location:** §"Required gates", gate 2 (Op coherence), after the existing three-bullet list.

**Add the following sub-clause:**

> **Pre-seeded projects.** Where world-build or project-activation populates vibe-cloud files (`actors/*/vibes.md`, `staff/studio/vibes.md` EPISODE_N_VIBES / SEASON_N_VIBES / SERIES_VIBES sections) prior to the first episode's facet authoring, those bundles constitute authoritative existing state at the time of facet authoring. Gate 2 applies to all targets without exception — including episode-scope, season-scope, and series-scope targets. Pre-loaded = present. `+` on a pre-loaded keyword is AP5 regardless of whether the pre-loading occurred via world-build or via prior episode authoring.
>
> In pre-seeded projects, the predominant episode-facet operations are:
> - `++` — extend a pre-loaded keyword with genuinely on-screen-licensed non-duplicate tokens
> - `+` — fresh add on targets whose vibe-sets do not yet carry the keyword (empty entity vibe-sets: locations, props, actors not yet pre-loaded)
> - skip — if the pre-loaded bundle already covers the event's full qualitative-consequence range and on-screen beats add no non-duplicate tokens
>
> The showrunner must check each target's cloud file before firing any `+` entry. The check is required for actor targets AND episode/season/series scope targets. Failure to extend the gate-2 check to episode-scope targets is the specific failure mode identified in Phase 2 (RF-001).

---

## Patch 2 — §"Anti-patterns" AP8 amendment: sentence-parsability as the formal test

**Location:** §"Anti-patterns", AP8 entry. Replace the current AP8 text with:

> **AP8 prose-token.** Full-sentence tokens, soft connectives, narrator-voice prose. Tokens are hyphenated word-algebra only. Multi-clause-as-token forbidden.
>
> **The formal test is sentence-parsability, not token length.** A token is AP8 if it can be parsed as a complete sentence with a standalone subject, finite verb, and object — regardless of how it is hyphenated. Length is a heuristic signal, not a gate. Long word-algebra compressions are not automatically AP8. Examples:
>
> - `the-cost-of-what-she-built-made-visible-to-strangers` (9 segments) — noun-phrase with participial modifier; reads as a noun-phrase not a sentence; PASS.
> - `the-door-she-can-open-after-the-machine-leaves` (9 segments) — noun-phrase with relative + temporal clause compressed; no standalone main predicate; reads as a noun-phrase; PASS.
> - `the-officer-was-efficient-and-she-knew-it` — sentential; subject (`the-officer`) + finite verb (`was`) + coordinate clause; FAIL.
> - `efficient-not-hostile` (3 segments) — compressed predicate-nominative; PASS.
>
> **Advisory for long tokens (8+ segments):** The token must be a single noun-phrase with compressed modifiers (participial, prepositional, relative, as-predicate). A sequence of two independent compressed clauses joined by a hyphen is AP8 even if individually each clause is short. The test is always: "Can this token be parsed as a sentence with a main predicate?" If yes, refuse.
>
> **AP13 cross-reference:** AP13 (prose-narration-in-tokens) is a stricter form of the same gate — a token that reads as a sentence the narrator might say fails AP8 by construction. AP8 is the formal gate; AP13 is the prose-register sub-test.

---

## Patch 3 — §"Anti-patterns" AP11 amendment: formal/advisory split

**Location:** §"Anti-patterns", AP11 entry. Replace the current AP11 text with:

> **AP11 token-overlap on `++`.** Tokens appended via `++` that duplicate tokens already in the existing bundle.
>
> **Formal gate (mechanic-checkable):** string-overlap. The token-set difference required is exact-string. A new token that shares no string with any existing bundle token passes the formal AP11 gate.
>
> **Advisory (author responsibility, not a mechanic gate):** Where new tokens are semantically adjacent to existing tokens — same qualitative register, different event-frame — the author should verify that the event-frames are genuinely distinct and that a downstream operator would generate different behavior from the new token versus the existing one. If the operator would generate identical behavior, the new token is a semantic duplicate and should be refused even though it passes the string test. When semantic-adjacency is present, authors may add a comment-line justifying the event-frame distinction.
>
> The formal string-overlap test governs mechanic review. The semantic-adjacency advisory governs authoring quality and Phase 5 review. A token that passes string-overlap but fails semantic-adjacency advisory is a soft flag, not a formal fault.

---

## Patch 4 — §"Cross-facet contract" addition: pre-render hazard clause

**Location:** §"Cross-facet contract", end of the section (after the final existing bullet). Add:

> **Pre-render hazard — `++` extensions from locked upstream facets.**
>
> `++` extensions authored in the vibes-updates facet may derive their licensing events from locked upstream facets (state-updates, memory-flags, feeling-flags). These upstream facets were authored BEFORE the vibes-updates facet. The question: do vibes-updates `++` extensions retroactively require those locked facets to be re-run?
>
> **No.** The vibes-updates facet is a write-side product; it records operator-bias state. The locked upstream facets are content-layer authority for their own scope. The two layers do not conflict:
>
> - Locked upstream facets (state-updates, memory, feeling) are authoritative for what happened on-screen in the episode.
> - The vibes-updates facet is authoritative for what operator-bias state each target carries after the episode.
> - A stitcher reading both simultaneously receives content-layer authority (from locked facets) and bias-layer context (from vibes-updates). Where they address the same event, they address different aspects of it. No retroactive invalidation occurs.
>
> `++` extensions do NOT retroactively change what locked upstream facets should have produced. The `++` extension is a write-side bias for FUTURE renders and FUTURE episode operators (s01e02+). It does not alter the s01e01 locked facet record.
>
> The locked facets remain canonical for s01e01. Showrunner does not re-run, re-review, or re-file locked facets on the basis of vibes-updates `++` extensions.

---

## Summary of changes

| Patch | Location | Type | Seam resolved |
|---|---|---|---|
| 1 | §"Required gates" gate 2 | Addition (sub-clause) | RF-001 — world-build pre-load behavior |
| 2 | §"Anti-patterns" AP8 | Replacement | SEAM 6 — AP8 formal test commitment |
| 3 | §"Anti-patterns" AP11 | Replacement | SEAM 4 — string-overlap vs semantic-overlap split |
| 4 | §"Cross-facet contract" | Addition | SEAM 7 — pre-render hazard clause |

No other V1 text is changed. All V1 gates, anti-patterns, functional registers, sparsity/volume guidelines, and author-privilege clauses remain in force.
