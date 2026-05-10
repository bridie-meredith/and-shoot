---
description: Season-scope orchestrator. Expands season content beats into continuous bones, runs the five-pass SVO pipeline + 10-pass season-scope review (S1, S2, S3, S3.5, S4, S5, S6, S7, S8, S9) including the URI-026 bone-gate against provisional cut windows, gets judged at Phase 6 (orchestrator-critic), then writes the split out mechanically as the final step. Episode count multiple of 3. Usage - /and-season [season-slug]
---

The season is the natural authoring unit. Content beats from `/and-season-plan` are the continuous spine; Phase 2 expands them into bones. Episode boundaries are *outputs* of this command — they are decided after season-scope review converges and after the orchestrator-critic verdict, by mechanical write-out against the converged bones.

You are the orchestrator. All work routes through subagent dispatches.

**Governing rules** (saved to memory; restated here for orchestration clarity):
- **Bones, not "an aggregate."** Phase 2 expands content beats into continuous bones in `<season-slug>.bones.md`, continuously numbered 1..N. There is no separate "aggregate" authoring concept — the content beats already provide the season's continuous structure; Phase 2 is bone expansion, not aggregation. No `# === episode: ===` delimiters.
- **Split is mechanical and last.** No split is authored during review. The dramatist proposes *provisional* cut windows inside Phase 3's bone-gate pass purely as review windows for shape verification — no per-episode files are written, no episode slugs are committed. The actual split runs as Phase 7, after Phase 6 verdict, as a mechanical write-out with no review loop.
- **Episode count multiple of 3.** Phase 7 split must yield an episode count that is a multiple of 3 (3, 6, 9, 12...). The dramatist's Phase 3 bone-gate proposal is the basis for the Phase 7 cut.
- **No titles, ever.** No `title:` field is authored on the season or on any episode. Slugs only.

## Args

- `$1` — optional. Season slug (e.g. `s01`). If omitted, use `active.season` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve season slug.
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Season exists in `seasons[]` with status `active`.
   - `season-<slug>-plan.md` exists with season chunk + season drama statement + content beats (continuous content guidance, no per-episode boundaries).
3. Determine resume point:
   - **No bones file exists** (`active-project/theater/proto-lines/<season-slug>.bones.md` absent) → start at Phase 2 Pass 1.
   - **Bones exist, season status `active`, no `protolines_complete` field** → resume at the appropriate phase based on which audit reports already exist under `active-project/staff/auditor/season-<slug>-pass-*`.
   - **`season.protolines_complete` set** → abort; the season has already run through this pipeline.
   - Season status `wrapped` → abort.
4. Print:

```
Season: <slug>
Bones: <absent | exists @ <path>>
Resume point: <Phase 2 Pass 1 | Phase 2 Pass <n> | Phase 3 Pass S<n> | Phase 6 verdict | Phase 7 split write-out>
```

---

## Phase 1 — REMOVED

Phase 1 (per-episode decomposition) is removed. The season's continuous structure is already provided by the content beats in `season-<slug>-plan.md`. Phase 2 expands those beats into bones directly; no separate "aggregate" object is authored.

---

## Phase 2 — Bone expansion

Phase 2 expands season content beats into continuous bones. The content beats are the spine; Phase 2 puts bone on it. There is no "aggregate authoring" step — the beats are already the season's continuous form.

### Output path

`active-project/theater/proto-lines/<season-slug>.bones.md`

### Format

```
# Season Bones — <season-slug>
# schema: schemas/proto-line.schema.md
# Continuous flat numbering 1..N. Episode boundaries are written out by Phase 7.
# POV transitions are inline (interlude beats are flagged inline, not as section breaks).

1 ...
2 ...
3 ...
...
N ...
```

POV transitions are flagged inline at the proto-line where the switch occurs, using a comment line of the form `# pov: <slug>` immediately preceding the first proto-line of the new POV stretch. The Phase 7 split must not cut across a POV-coherent stretch.

### Execution shape

Phase 2 runs as: **Pass 1 (serial inventory) → Review Sweep (parallel, one Agent block) → Collation (serial) → Fix Routing (serial, line-range-ordered) → Re-fire (parallel, scoped to invalidation).** Iterate sweep→fix→re-fire to convergence. Cap: 3 full cycles.

#### Pass 1 — Inventory write (serial, single dispatch)

Single SVO-writer dispatch. Inputs: the season chunk, the season drama statement, ALL content beats from `season-<slug>-plan.md` (continuous content guidance), all active condition cards, behavior cards for the season's full active cast, series + season vibe-clouds. Output: the bones file with continuous SVO from start of season to end. The writer is explicitly told **NOT to insert episode delimiters** and **NOT to honor pre-existing slug labels** on the content beats. Continuous flat numbering 1..N.

**Gate before Review Sweep:** bones file exists and parses against `schemas/proto-line.schema.md`. If not, escalate to user.

#### Review Sweep (parallel, fire as one Agent block, 6 forks)

| Fork | Agent | Brief | Output report |
|---|---|---|---|
| 2-A | auditor #1 | constraint sweep against condition cards, series laws, harsh-SVO discipline | `season-<slug>-pass-2-constraint.md` |
| 2-B | dramatist | per-stretch dramatic shape AND season-wide escalation arc | `season-<slug>-pass-2-shape.md` |
| 2-C | audience persona-A | per-stretch ENGAGED/TOLERATED/BORED + season-wide entertainment-density | `season-<slug>-pass-2-trim-{personaA}.md` |
| 2-D | audience persona-B | (same brief) | `season-<slug>-pass-2-trim-{personaB}.md` |
| 2-E | audience persona-C | (same brief) | `season-<slug>-pass-2-trim-{personaC}.md` |
| 2-F | auditor #2 | continuity sweep — cross-season state, prop chains, POV transitions, reachability | `season-<slug>-pass-2-continuity.md` |

**Discipline:** all six dispatches fire as parallel tool calls in **one assistant turn**. No fork waits on another. No fork reads another fork's output. If the main session breaks this — staggers dispatches across turns, reads a report mid-sweep, lets one fork's verdict bias another's brief — the sweep has not run as specified. Disclose the deviation per honesty discipline.

#### Collation (serial, single main-session step)

Read all six reports. Build a fault list: `{report-id, fault-class, line-range, severity, routing}`. Audience ≥2-persona threshold applied here (not inside forks). Sort by line-range; group adjacent or overlapping ranges (5-line buffer).

#### Fix Routing (serial, fault-list driven)

For each fault group, in line-range order:
- **Fixer** dispatch for surgical line edits (slug fix, mechanic recast, single-line continuity patch).
- **Screen-writer** dispatch for stretch regenerations (REGEN-REPLACE / ADD / BOTH per URI-026), one stretch per dispatch.

Parallel fix dispatches allowed only when their target line ranges are disjoint with the 5-line buffer. Overlapping or adjacent groups serialize.

#### Re-fire (parallel, scoped to invalidation)

After fixes land, identify reviews whose scope intersects touched lines. Re-fire only those forks as a parallel Agent block sized to the invalidation set.

**Convergence:** Review Sweep returns all-clean with no fixes between. **Cap:** 3 full sweep→fix→re-fire cycles. Non-convergence escalates with a failing-fork list.

### Why no internal delimiters

- The writer sees the whole season at once and is *not* asked to retrofit cross-section consistency.
- Pre-baked episode boundaries pull the writer into honoring section closes and opens that may not be where the bones actually want to break. Removing the delimiters lets the bones breathe; the cuts are written out by Phase 7 against the bones that exist, not against where boundaries were predicted before any bone was written.
- Review operates on the bones as a single continuous object, matching how a reader consumes the season.

### Relationship to `/and-protolines-v2`

`/and-protolines-v2` remains the per-episode standalone authoring command for ad-hoc work or single-episode revision after the Phase 7 write-out. Its five passes are the *template* for Phase 2's sub-passes here, scaled up to season scope. /and-season does not invoke /and-protolines-v2 per episode at any point.

---

## Phase 3 — Comprehensive season-scope review

After Phase 2 produces converged bones, run the **ten-pass season-scope review** against the bones. Same reviewer roles as per-episode review, scaled up: the criteria are season-scope (cross-stretch coherence, season escalation arc, season-wide entertainment density, etc.).

In the pass briefs below, references to "chapters" / "sections" / "episodes" inside the bones are *interpretive*: a stretch of bones a reviewer treats as a coherent unit for evaluation. They do not correspond to authored delimiters (there are none). Reviewers identify stretches by reading; the writer never authored them as such.

**Provisional cut identification.** The dramatist may propose cut points at any time during Phase 3 review — this is the natural way to evaluate per-stretch shape, run the bone-gate, and verify split-feasibility. Proposed cuts are *provisional review windows only*; no per-episode files are written and no episode slugs are committed during Phase 3. Per-stretch bone regen may reshape where the eventual cuts land. The actual split write-out is Phase 7.

### Execution shape

Phase 3 runs as: **Sweep A (parallel, independent reviews) → Sweep B (parallel, bone-gate per provisional window) → Collation (serial) → Fix Routing (serial, line-range-ordered) → Re-fire (parallel, scoped to invalidation).** Iterate sweep→fix→re-fire to convergence. Cap: 3 full cycles.

The per-pass briefs in the sections below (`### Pass S1` through `### Pass S10`) are the **fork reference content** — what each fork in Sweep A or Sweep B is told to do. The orchestration layer above them is what governs *when* and *how* the forks fire.

#### Sweep A — Independent reviews (parallel, fire as one Agent block, 18 forks)

| Fork | Agent | Pass brief | Output |
|---|---|---|---|
| S1 | auditor | per `### Pass S1` | `season-<slug>-pass-S1-constraint.md` |
| S2 | dramatist | per `### Pass S2` (STRICT) | `season-<slug>-pass-S2-shape.md` |
| S3-A | audience persona-A | per `### Pass S3` (entertainment cap) | `season-<slug>-pass-S3-trim-{personaA}.md` |
| S3-B | audience persona-B | (same) | `season-<slug>-pass-S3-trim-{personaB}.md` |
| S3-C | audience persona-C | (same) | `season-<slug>-pass-S3-trim-{personaC}.md` |
| S3.5 | auditor | per `### Pass S3.5` (ruleset, idiom-depletion) | `season-<slug>-pass-S3.5-ruleset.md` |
| S4 | auditor | per `### Pass S4` (continuity) | `season-<slug>-pass-S4-continuity.md` |
| S5 | dramatist | per `### Pass S5` (voice register) | `season-<slug>-pass-S5-voice-coherence.md` |
| S6-A | audience persona-A | per `### Pass S6` (vibe alignment) | `season-<slug>-pass-S6-vibe-{personaA}.md` |
| S6-B | audience persona-B | (same) | `season-<slug>-pass-S6-vibe-{personaB}.md` |
| S6-C | audience persona-C | (same) | `season-<slug>-pass-S6-vibe-{personaC}.md` |
| S7 | auditor | per `### Pass S7` (facet-readiness) | `season-<slug>-pass-S7-facet-readiness.md` |
| S8a | dramatist | per `### Pass S8` §S8a (character plausibility) | `season-<slug>-pass-S8a-plausibility-character.md` |
| S8b | auditor | per `### Pass S8` §S8b (event plausibility) | `season-<slug>-pass-S8b-plausibility-event.md` |
| S9-A | audience persona-A | per `### Pass S9` (comprehensibility) | `season-<slug>-pass-S9-comp-{personaA}.md` |
| S9-B | audience persona-B | (same) | `season-<slug>-pass-S9-comp-{personaB}.md` |
| S9-C | audience persona-C | (same) | `season-<slug>-pass-S9-comp-{personaC}.md` |
| S10.1 | dramatist | per `### Pass S10` Step 1 (provisional cut proposal) | `season-<slug>-pass-S10-cut-proposal.md` |

**Discipline:** all 18 dispatches fire as parallel tool calls in **one assistant turn**. No fork waits on another; no fork reads another's output. Audience persona-A runs three separate forks (S3, S6, S9) — single-purpose per the per-persona discipline choice (URI follow-on, 2026-05-10). The cut proposal S10.1 fires in the same block as the others; the proposal does not gate Sweep A's other forks.

#### Sweep B — Bone-gate per provisional window (parallel, fire as one Agent block, ~5N–6N forks)

Triggered once Sweep A's S10.1 cut proposal exists. For **N provisional windows** (typically 3–6, multiple of 3 by S10 constraint):

| Per window | Agent | Brief | Output |
|---|---|---|---|
| tens (1× per window) | dramatist (fork mode, rubric-only) | per `### Pass S10` Step 2 | `tensometer-<season-slug>-window-{NN}.md` |
| taste-A (1× per window) | audience persona-A | per `### Pass S10` Step 3 §audience taste | `season-<slug>-pass-S10-taste-window-{NN}-{personaA}.md` |
| taste-B (1× per window) | audience persona-B | (same) | `season-<slug>-pass-S10-taste-window-{NN}-{personaB}.md` |
| taste-C (1× per window) | audience persona-C | (same) | `season-<slug>-pass-S10-taste-window-{NN}-{personaC}.md` |
| mechanic (1× per window) | auditor (narrow-scope: AP-SCAN+CURVE+FREQ) | per `### Pass S10` Step 3 §mechanic | `season-<slug>-pass-S10-mechanic-window-{NN}.md` |
| boundary (1× per boundary, N-1 boundaries) | auditor | per `### Pass S10` Step 4 (boundary-carry) | `season-<slug>-pass-S10-boundary-{NN→NN+1}.md` |

For N=6: 6 tens + 18 audience + 6 mechanic + 5 boundary = **35 parallel forks in one Agent block.**

#### Collation (serial, single main-session step)

Read all reports from Sweeps A + B. Build fault list: `{report-id, fault-class, line-range, severity, routing}`. Apply audience ≥2-persona threshold here (not inside forks). Per-window verdicts compose from Sweep B reports per S10 Step 3's combined-verdict rule. Sort by line-range; group adjacent or overlapping ranges (5-line buffer).

#### Fix Routing (serial, fault-list driven)

For each fault group, in line-range order:
- **Fixer** dispatch for surgical line edits (slug fix, mechanic recast, single-line continuity patch).
- **Screen-writer** dispatch for stretch regenerations (REGEN-REPLACE / ADD / BOTH per URI-026), one stretch per dispatch.
- **Cut faults** (S10 `WINDOW-REVISE-cut-{reason}`) route to a new S10.1 dispatch with the named cut feedback.
- **Drift faults** (S6 non-localizable vibe drift) route to a season-scope screen-writer pattern pass.

Parallel fix dispatches allowed only when their target line ranges are disjoint with the 5-line buffer. Overlapping or adjacent groups serialize.

#### Re-fire (parallel, scoped to invalidation)

After fixes land, identify reviews whose scope intersects touched lines. Re-fire only those forks as a parallel Agent block sized to the invalidation set. S10 Sweep B re-fires per-window — only the touched window's sub-forks re-fire, not all of Sweep B. Broad changes (cross-stretch restructure) re-fire all of Sweep A and all of Sweep B.

**Per-window iteration cap: 2** (URI-026). After 2 inner regen iterations on the same window without convergence, the residual is a `tens-gate-residual-HARD` finding routed to Phase 6 (F7-bone).

---

### Per-pass briefs (fork reference content)

The sections below define what each fork in Sweep A or Sweep B is told to do. They are read by the orchestrator when constructing per-fork dispatch briefs. They are **not** an execution order — the orchestration layer above governs that.

### Pass S1 — Constraint audit (auditor #season-1)

Inputs: the season aggregate, all active condition cards under `active-project/warehouse/`, series laws and lore from showrunner memory, schema + harsh-SVO discipline.

Brief: every line must remain legal under SVO mechanics AND constraint-coherent across the season. Sweep:
- Per-line mechanic re-check at season scope (catches drift a smaller-scope review missed).
- Cross-stretch constraint coherence: no stretch violates a constraint another stretch establishes; series laws and condition cards honored consistently.
- Slug + reference resolution: every actor / prop / location slug resolves to the canonical card; no stretch introduces a slug another stretch lacks setup for.

Output: `active-project/staff/auditor/season-<slug>-pass-S1-constraint.md`. File-level: `PASS` or `FAIL` with classified findings. Faults route to fixer; cross-stretch faults requiring chunk-statement revision route as `escalate`.

### Pass S2 — Shape (dramatist, season scope) — STRICT

Inputs: the season aggregate, `season-<slug>-plan.md`, `series-plan.md`, behavior cards (full inheritance) for the season's active cast.

You are a **strict** structural critic at season scale. A season without an identifiable buildup, climax, and denouement is a structural failure regardless of how clean any individual stretch reads.

#### Mandatory structural identification (must be filled in)

Cite **proto-line ID ranges** — not chapter numbers, since the aggregate is undelimited:

- **Season buildup (rising stretch):** lines `<from>`–`<to>`. Where season stakes are introduced and the season's question is posed. If absent, flag `NO-SEASON-BUILDUP`.
- **Season climax (peak stretch):** lines `<from>`–`<to>`, with the specific peak line ID. The single highest-stakes stretch where season tension turns. If you cannot point to a single peak stretch, flag `NO-SEASON-CLIMAX`.
- **Season denouement (falling stretch):** lines `<from>`–`<to>`. The post-peak release. If absent, flag `NO-SEASON-DENOUEMENT`.

#### Sweep checks

- **Season-level rise-peak-fall:** stretch peaks escalate cumulatively per the season escalation spine. Terminal peak lands at the climax stretch, not earlier.
- **Cross-stretch flatlines:** long stretches without an inflection beat is a season flatline.
- **Forward-flag honor:** commitments from `season-plan.md` (e.g. "the IGNITION beat triggers an involuntary swarm rise") are visible in the corresponding stretches' proto-lines. Missing commitment is a structural fault.
- **Premature peak / late peak:** climax stretch must be in the back half of the aggregate. Earlier flags `EARLY-SEASON-PEAK`; later flags `LATE-SEASON-PEAK`.
- **Denouement share (URI-008, 2026-05-10).** The post-climax stretch must not exceed **40% of the aggregate's total numbered-line count**. If denouement share exceeds 40%, S2 issues a `LATE-WEIGHT` flag for human review. Tone-law-mandated long-cost structures qualify for a `LATE-WEIGHT-LICENSED-{condition-card}` exception **only when** the season-plan explicitly designates the post-peak arc as cost-bearing AND names the cost-bearing arc with its expected share. A generic "long cost" reference in §B drama is not sufficient; the exception requires the plan to name the specific stretch and its proportion.
- **Pacing:** density and weight of inter-stretch transitions match the season's pacing register.

Output: `active-project/staff/auditor/season-<slug>-pass-S2-shape.md`. Verdict: `CLEAN` / `RE-ORDER-OR-REVISE` / `STRUCTURAL-FAILURE`. Reorders may move beats inside the aggregate (no chapter boundaries to respect) and route to fixer with line-range scope. `STRUCTURAL-FAILURE` cannot be cleared by reorders alone — escalate to user.

Bias: when in doubt, flag.

### Pass S3 — Trim (audience ×3, season scope)

Inputs: the season aggregate; the **season goal** (distilled by orchestrator from `season-plan.md` season chunk + season drama + content beats — pinned at top of brief as north star); all active actor vibes, studio vibes, persona cards, behavior cards; full series-plan and season-plan prose.

Brief: walk every numbered non-blank line. Apply the trim test against the **season goal**. A line that serves a local stretch but distracts from the season arc is a deletion candidate. Voice-load-bearing test still applies.

**Entertainment check (MANDATORY).** You are a strict entertainment critic at season scale. The aggregate has no chapter delimiters — instead, log entertainment verdicts per **~10-line window** continuously across the season:
- **ENGAGED** — your taste finds this window delivers a hook your persona is paid to want.
- **TOLERATED** — functional but not entertaining in its own right.
- **BORED** — your taste actively disengages.

Cap: at most ~10% of windows TOLERATED, zero BORED. Two consecutive BORED windows OR three consecutive TOLERATED → REVISE with reason `season-attention-flatline-{line-range}`.

**S3 vs S9 — different purposes (URI-013, 2026-05-10).** S3 (Trim) is the **entertainment cap** — what the audience would pay to read; threshold ~10% TOLERATED + zero BORED + consecutive-run rules. S9 (Comprehensibility) is the **attention floor** — what the audience can sustain reading; threshold ≥30% B-or-T in any 100-line stretch. The two passes can return non-aligned verdicts and both are valid: entertainment cap can be passed while attention floor fails (slow-but-engaging), and vice versa. Do not collapse the two thresholds; they evaluate different reader-states.

Apply persona-specific taste hard. ≥2-persona threshold for auto-accept deletion. File-level verdict per persona: `ACCEPT` or `REVISE-{one-clause-reason}`.

Bias: when in doubt, REVISE.

Output: `active-project/staff/auditor/season-<slug>-pass-S3-trim-{persona}.md` × 3.

If all three personas ACCEPT → terminate. If any REVISE → named entertainment problem routes to screen-writer for stretch-level regeneration in the aggregate; affected stretch rewritten in place; Pass S3 re-runs.

### Pass S3.5 — Ruleset compliance (auditor #season-3, dedicated)

The mechanic-strictness pass. Re-checks the entire aggregate against the harsh-SVO ruleset to catch verbs that survived stretch-level review by reading borderline in isolation but as a season-wide compliance-drift pattern.

Inputs: aggregate; `schemas/proto-line.schema.md`; full SVO discipline (`svo-writer-pass1-brief.md` §"SVO discipline"); the 15 ambiguity calls (`svo-split-notes.md`).

Brief — explicit ruleset checklist:
- Walk every numbered non-blank line.
- Evaluate each against the **non-action-verb deny-list**: `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`, `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`, `contains`, `houses`, `occupies`, `inhabits`, `consists of`, `comprises`, `lies`, `sits`, `stands` (position-naming), and disallowed `holds` uses.
- For each `holds` instance: license-check (body-part-object or physical-object-resisting-pressure). Otherwise FAULT-FORM-NON-ACTION-VERB.
- Re-check harsh-SVO discipline mechanically: copulas, negations, perception verbs, modifiers, conjunctions, abstractions-as-objects.
- Drift-pattern report: a verb appearing 5+ times across the season as a borderline state-verb is a *pattern*; flag for systematic recast.
- **Idiom-depletion check (URI-007, 2026-05-10).** For any **physical-stasis idiom** (e.g., `holds the feet`, `holds the eyes`, `holds the chin`, `presses the temple`) appearing **10+ times across the aggregate**, at minimum **25% of instances** must carry a contextual differentiator that allows a reader to distinguish cost-register from patience-register. Differentiators include: preceding scene density (high-stakes scene context); following board-change (the stasis precedes a state-shift); direct proximity to a season-plan-named cost-bearing beat (e.g., shard-load); paired bone with a specific cost-marker (`presses the temple` after the idiom). Idioms below the 25% differentiation rate trigger `IDIOM-DEPLETION-{idiom}-{instance-count}` flag and route to **screen-writer for systematic recast** at the named instances.
- This check operates **above the schema's per-instance narrow license**: the schema's `holds` narrow license (body-part-object or physical-object-resisting-pressure) is satisfied per instance, but cumulative depletion at scale is a separate fault. Per-instance license satisfaction does not exempt season-scope depletion.

Output: `active-project/staff/auditor/season-<slug>-pass-S3.5-ruleset.md`. File-level: `RULESET-CLEAN` or `RULESET-FAIL`.

### Pass S4 — Continuity (auditor #season-2)

Inputs: post-trim post-shape aggregate; season chunk; series laws; active location cards.

Brief — four sweeps at season scope:
- **Reachability:** season-start state → season-end state per `season-<slug>-plan.md` season chunk; the surviving aggregate must traverse the delta.
- **State:** every prop and actor across the season. Props introduced are consumed/released or persist coherently. Actor entries and exits coherent.
- **Reference:** every slug resolves; no orphan introductions.
- **POV:** narrator transitions inside the aggregate are honest — the narrator-switch position is reachable from prior bones. Inline `# pov:` comment at the switch line is required.

Output: `active-project/staff/auditor/season-<slug>-pass-S4-continuity.md`. File-level: `SEASON-CONTINUITY-OK` or `SEASON-CONTINUITY-FAIL`. Reachability faults at season scope route as `escalate`.

### Pass S4.5 — REMOVED

The post-split continuity check has been folded into **Pass S10 — Bone-gate (split-shape verification)** below. Under the deferred-split rule, no per-episode files exist during Phase 3, so a "post-split" check has nothing to read. S10 runs the dramatist's provisional cut proposal + tens authoring + audience+mechanic verdict against the *bones* (using line-range windows as proxies for episode boundaries), and the boundary-carry test (`eN close state visible as active constraint in eN+1 open`) runs as part of S10's per-window verdict. Faults route to in-place bone regen, exactly as before, but no per-episode file is written until Phase 7.

### Pass S5 — Voice register coherence (dramatist, second invocation)

Inputs: aggregate; behavior cards (full inheritance) for every active actor; per-actor vibes.

Brief: each actor's voice register stays consistent across the aggregate per their behavior card. The verbs an actor *takes* should match the actor's voice signature; out-of-register acts flagged; no drift between an actor's first-stretch voice and last-stretch voice (modulo arc-driven change).

Output: `active-project/staff/auditor/season-<slug>-pass-S5-voice-coherence.md`. Verdict: `VOICE-COHERENT` or `VOICE-DRIFT`.

### Pass S6 — Vibe and theme alignment (audience ×3, second invocation)

Inputs as for S3, plus per-actor vibes and studio vibes for each setting.

Brief: read the aggregate as a tonal arc. Each stretch's beats honor the active vibe-cloud; series.theme propagates into stretch-level beats; the season's tonal register is consistent.

**Per-window vibe verdict (MANDATORY)** logged per ~10-line window: `VIBE-ALIGNED` or `VIBE-DRIFT-{reason}`.

Per-persona output: `season-<slug>-pass-S6-vibe-{persona}.md`. ≥2-persona threshold for accepting drift flags. Bias: when in doubt, flag drift.

**Drift-resolution routing (URI-015, 2026-05-10).** When ≥2-persona drift threshold is met:
- **Localizable drift** (e.g., `VIBE-DRIFT-procedural-recurrence-{line-range}`) — drift concentrated to a specific stretch — routes to **screen-writer for stretch regeneration** in the aggregate. The fix is in-pass; downstream passes re-run from the changed point.
- **Non-localizable / season-wide drift** (e.g., `VIBE-DRIFT-shard-load-suppressed`, `VIBE-DRIFT-organism-texture-underweight`) — drift dispersed across many stretches — routes to a **season-scope screen-writer pass** on the named pattern (a targeted regeneration of flagged instances per a contextual-differentiator criterion), OR to **carry-back queue** if no V1 mechanic exists for the specific drift form.
- **Carry-forward** (declaring the drift acknowledged but not corrected within the run) is permitted **only when** the season-plan acknowledges the pattern explicitly. A generic "audience carry-forward" tag is not sufficient; the plan must name the specific drift category. Otherwise the drift must be resolved in-pass per the routes above.

### Pass S7 — Facet-readiness (auditor #season-4, dedicated)

Inputs: aggregate; `schemas/facet.schema.md`, `schemas/dialogue.schema.md`; locked facet rubrics under `design/shoot-v2/`.

Brief — for each load-bearing beat, verify a citable bone exists for each facet author downstream (location-state, state-updates, tensometer, dialogue, narrator-interest, etc.). Flag over-dense stretches (10+ beats per scene without inflection) and under-dense stretches (a chunk-implied beat with zero supporting bones).

Output: `season-<slug>-pass-S7-facet-readiness.md`. Verdict: `FACET-READY` or `FACET-GAPS`.

### Pass S8 — Plausibility (dramatist + auditor hybrid)

**S8a — Character-action plausibility (dramatist).** For every named-actor action, ask: would this character actually *do* that, given their behavior card, persona card, vibes, and prior-stretch actions? Sharper than voice register — voice asks "does this sound like the character?", plausibility asks "is this what the character would *do*?".

**S8b — Event-in-world plausibility (auditor).** For every beat: plausible in-world given active condition cards, series laws, lore? An event that doesn't violate a constraint but would not realistically occur given how the world works is flagged.

Inputs: aggregate; all behavior cards; all condition cards; series-plan + season-plan; active actor vibes.

Output: `season-<slug>-pass-S8-plausibility.md`. Per-beat verdicts: `PLAUSIBLE` / `IMPLAUSIBLE-CHARACTER-{slug}` / `IMPLAUSIBLE-EVENT-{condition-or-law}`. File-level: `PLAUSIBLE` or `IMPLAUSIBLE`. Structural implausibility routes as `escalate`.

**Split-verdict adjudication (URI-016, 2026-05-10).** When S8a (character) and S8b (event) return divergent terminal verdicts on the same beat (e.g., S8a IMPLAUSIBLE / S8b PLAUSIBLE), the divergence triggers a `S8-SPLIT-VERDICT-{slug}-{beat-range}` flag.
- **Default resolution:** the more restrictive verdict wins. `IMPLAUSIBLE-CHARACTER` overrides `PLAUSIBLE-EVENT`; `IMPLAUSIBLE-EVENT` overrides `PLAUSIBLE-CHARACTER`. The reader does not compute character vs event separately; they read one beat.
- **Override path:** if the season-plan or a specific condition-card explicitly licenses the divergence (e.g., `cond-smallfolk-political-physics` permits a community-membrane interaction the character-card's information-suppression pattern would otherwise refuse), the override must **cite the licensing card or plan section** and the divergence converts to `S8-LICENSED-DIVERGENCE-{card-slug}`. A bare assertion of "interpretive divergence" without a cited license is not an override.

### Pass S9 — Comprehensibility (audience ×3, third invocation)

Brief: read the aggregate as a comprehensibility test for a reader who only has the bones + downstream stitched prose. **You are also the entertainment-at-every-step gate of last resort.**

Per-beat:
- If this beat were missed by the reader, would the rest cohere? A beat whose absence breaks comprehension is **load-bearing** — flag for emphasis, parallel anchoring, or relocation.
- Is the cause-effect chain to the next beat legible without exposition? If reader-comprehension requires interiority, narrator-summary, or off-stage knowledge, the chain is **fragile**.
- Does the proto-line carry enough information for a reader to know *what happened* and *who did what to whom*? Ambiguous slugs, under-specified verbs, pronoun-equivalent referents flagged.

Per-window entertainment check (~10 lines per window): `ENGAGED` / `TOLERATED` / `BORED`. Two consecutive BORED OR three consecutive TOLERATED OR ≥30% of any 100-line stretch BORED-or-TOLERATED → file-level `COMPREHENSIBILITY-RISK-attention-{detail}`.

Per-persona output: `season-<slug>-pass-S9-comprehensibility-{persona}.md`. File-level: `COMPREHENSIBLE` or `COMPREHENSIBILITY-RISK-{reason}`.

### Pass S10 — Bone-gate (split-shape verification) (URI-026, relocated 2026-05-10)

Formerly Phase 4 Steps 1, 1.5, 2 (the dramatist split proposal + per-episode tens authoring + audience+mechanic verdict). Relocated under the deferred-split rule: split identification happens during review for shape verification, but no per-episode files are written until Phase 7.

**Step 1 — Provisional cut proposal (dramatist).** Dispatch dramatist against the bones with criteria (a) ideal episode size (80–160 bones band, configurable), (b) dramatic shape, (c) episode-count multiple of 3, (d) POV honor (no cut bisects a `# pov:` stretch). Output is a list of provisional cut-point line IDs + one-line rationale per cut. **No per-episode files written. No episode slugs committed.** Path: `active-project/staff/auditor/season-<slug>-pass-S10-cut-proposal.md`.

**Step 2 — Tens authoring per provisional window.** Dramatist fork-mode, one fork per provisional window, in parallel. Inputs: the window's bone stretch + `design/shoot-v2/rubric-tensometer.md` + `schemas/facet.schema.md`. Forbid: behavior cards, vibes, audience personas, source prose. Output: `active-project/theater/facets/tensometer-<season-slug>-window-<NN>.md` (the `-window-` suffix replaces the old `e<NN>` since no episode is committed yet). Same content format as `/and-facets-r1` Layer 1a.

**Step 3 — Combined audience + mechanic verdict per window.** Audience ×3 (Threshold Discipline + Season-Scope Adversarial body sections; Tens-attack vocabulary; OPEN-ENGAGES / CLOSE-EARNS-NEXT / SHAPE-COHERENT verdicts) + narrow-scope auditor (FREQUENCY-BAND / CURVE-SHAPE / AP-SCAN against `/and-facets-audit.md` class library). Combined per-window verdict: `WINDOW-ACCEPT` (≥2-of-3 personas ACCEPT AND MECHANIC-CLEAN AND no SHAPE-COHERENT-FLAT-AFTERMATH HARD) / `WINDOW-REVISE-bones-{line-range}` (regen in place) / `WINDOW-REVISE-cut-{reason}` (dramatist re-proposes the cut).

**Step 4 — Boundary-carry check (absorbed from former S4.5).** For each provisional boundary `windowN → windowN+1`, verify that state-changes in windowN's close region (last 20 bones) are signaled as active constraints in windowN+1's open region (first 10 bones), physical-register not exposition. Per-boundary verdict: `BOUNDARY-CARRIES` / `BOUNDARY-DROPS-{state}`. Drops route to screen-writer for 1–2 physical-register bone additions at the windowN+1 open (using the existing REGEN-ADD discipline).

**Bone-regen routing (URI-026):** REGEN-REPLACE / REGEN-ADD / REGEN-BOTH carry their original semantics. Position-aware mapping (URI-010) and `# pov:` preservation remain mandatory.

**Per-window iteration cap: 2.** After 2 inner regen iterations without convergence, the residual is a `tens-gate-residual-HARD` finding routed to Phase 6 (orchestrator-critic F7-bone).

**Output:** `active-project/staff/auditor/season-<slug>-pass-S10-bone-gate-window-{NN}.md` × N (where N is the provisional window count). File-level per window: `WINDOW-ACCEPT` / `WINDOW-REVISE-{reason}` / `BOUNDARY-DROPS-{state}`.

**`SPLIT-INFEASIBLE` escalation.** If the dramatist cannot find a multiple-of-3 episode count that fits (a) + (b) + (c) + (d) without violating one, surface as `SPLIT-INFEASIBLE` and escalate to user. Bones may still be sound; the structural failure is in cut topology, which user must adjudicate.

### Convergence

Phase 3 converges when **a single sweep→fix→re-fire cycle ends with all-clean reports across both sweeps and no fixes in between**. A "cycle" is one full pass through Sweep A + Sweep B + Collation + Fix Routing + Re-fire. **Cap: 3 cycles.** Non-convergence ships with a header comment + escalates to user with the failing-fork list.

### Iteration cap relationship

Phase 2 and Phase 3 each have an independent cap of 3 cycles. They are sequential. Phase 3 fault routing flows back into the bones; a Phase 3 fix that requires regenerating a stretch invokes screen-writer in stretch-regeneration mode — does NOT restart Phase 2's pipeline. Worst-case combined budget: 6 full cycles.

### Dispatch counting note (URI-022 carry-over)

The orchestrator-critic card's dispatch-count budget (60 hard / 30 soft) counts individual subagent dispatches regardless of whether they fired in parallel or serial. A single Agent block containing 18 parallel dispatches counts as 18, not 1. The fan-out shape concentrates dispatches in time but does not change the totals the card judges against. Cycles are budgeted separately from dispatches per the card's §"Runtime budgets".

---

## Phase 4 — REMOVED (split deferred)

Phase 4 is retired under the deferred-split rule:

- **Provisional cut proposal + tens authoring + audience+mechanic bone-gate verdict** → Phase 3 Pass S10 (above). Dramatist proposes cuts as review windows during season-scope review; no per-episode files written; kickback routes to in-place bone regen.
- **Mechanical write-out of per-episode files** → Phase 7 (below), executes after Phase 5 persist + Phase 6 verdict. No review loop, no kickback.

Detailed verdict criteria (OPEN-ENGAGES / CLOSE-EARNS-NEXT / SHAPE-COHERENT, URI-011) live in S10 Step 3 by reference; the cap-and-band class definitions live in `.claude/commands/and-facets-audit.md` per the shared-reviewer principle (URI-026).

---


## Phase 5 — Persist (bones-level)

Phase 5 persists *bones-level* state — the converged bones file + the full audit report set. The per-episode split is **not** persisted here; that's Phase 7. This separation is what allows Phase 6 (orchestrator verdict) to judge the run against the bones and audit reports without the split entering the verdict surface.

1. Update `active-project/staff/showrunner/memory.md`:
   - `seasons[<slug>].bones_path`: `active-project/theater/proto-lines/<season-slug>.bones.md`
   - `seasons[<slug>].bones_complete`: timestamp + full Phase 3 audit report directory
   - `seasons[<slug>].phase_3_cycles`: n of 3 max
   - `seasons[<slug>].phase_2_cycles`: n of 3 max
   - Season status remains `active`. `active.episode` stays `~` until Phase 7.
   - **`seasons[<slug>].episodes[]` is NOT written here.** That happens in Phase 7 Step 5.

2. Print summary:

```
--- SEASON BONES COMPLETE: <season-slug> ---

Bones: <total count>
Provisional split (informational, from final S10.1 proposal): <count, multiple of 3>

Phase 2 (bone expansion, fan-out form):
  cycles to converge:    <n of 3 max>
  Pass 1 inventory:      WRITTEN
  Review Sweep:          6 forks (constraint / shape / trim×3 / continuity)
  final-cycle verdict:   <ALL-CLEAN | failing-fork list>

Phase 3 (season-scope review, fan-out form):
  cycles to converge:    <n of 3 max>
  Sweep A (18 forks):    <ALL-CLEAN | failing-fork list>
    S1 constraint, S2 shape, S3 trim×3, S3.5 ruleset, S4 continuity,
    S5 voice, S6 vibe×3, S7 facet-readiness, S8a/S8b plausibility,
    S9 comprehensibility×3, S10.1 cut proposal
  Sweep B (bone-gate, ~5N–6N forks for N provisional windows):
    tens-rating ×N:      <ALL-AUTHORED | RETRIES:<n>>
    audience taste ×3N:  <ALL-ACCEPT | REVISE-{persona-window}>
    mechanic ×N:         <ALL-MECHANIC-CLEAN | MECHANIC-FAIL-{window}:{classes}>
    boundary ×(N-1):     <ALL-CARRIES | DROPS-{boundary}>
  per-window inner cap:  <n of 2 max per window>
  Tens-gate verdict:     <CLEAN | residual HARD — F7-bone candidate>

Files (Phase 5 persists; Phase 7 will add per-episode files):
  active-project/theater/proto-lines/<season-slug>.bones.md
  active-project/staff/auditor/season-<slug>-pass-{2-*, S1, S2, S3-*, S3.5, S4, S5, S6-*, S7, S8a, S8b, S9-*, S10-*}.md
  active-project/theater/facets/tensometer-<season-slug>-window-{NN}.md (× N, provisional)

Next: Phase 6 (orchestrator verdict), then Phase 7 (split write-out) if PASS or PASS-WITH-NOTES.
```

---

## Phase 6 — Orchestrator verdict (URI-022, 2026-05-10)

After Phase 5 persists, the run is judged against the **orchestrator-critic card** at `staff/orchestrator-critic/card.md`. This is the standard `/and-season` must satisfy to be considered a successful run.

### What this phase does

Per the card's invocation protocol (§"Invocation protocol" in `staff/orchestrator-critic/card.md`):

1. The orchestrator (main session of `/and-season`) reads its own run state — the audit reports under `active-project/staff/auditor/season-<slug>-pass-*`, the split-proposal + split-review files, showrunner memory's iteration counts and dispatch counts, the per-episode files post-split, the aggregate post-Phase-3, and the session's wall-clock + dispatch totals.
2. The orchestrator scores the run against the card's three success-criteria categories (Convergence / Quality / Routing) and the runtime budgets (60-dispatch hard cap; 30 soft; 3-iteration cap per phase).
3. The orchestrator writes a run report to `active-project/staff/auditor/season-<slug>-orchestrator-verdict.md` per the §"Run report template" in the card.
4. The verdict line — `PASS` / `PASS-WITH-NOTES — <notes>` / `FAIL — <failure summary>` — is written into `seasons[<slug>].orchestrator_verdict` in showrunner memory.

### No subagent dispatch

The card is a measurement spec, not a roleplay. The orchestrator-critic does not need its own agent — main session reads the card, applies the criteria to its run state, and produces the verdict. Phase 6 is bookkeeping discipline, not a new dispatch.

### Verdict effects

- **PASS:** the run is successful; downstream work (facet authoring, /and-shoot, /and-wrap) proceeds normally.
- **PASS-WITH-NOTES:** the run is successful; the notes (high-dispatch / long-run / deep-iteration / rubric-too-soft / SLEEPERs surfaced) inform the next session's planning. No automatic re-run.
- **FAIL:** the run did NOT satisfy the orchestrator standard. Required to surface the failure to the user with the specific failure-mode citation (F1–F6 per the card). Downstream work is gated on user decision: fix the run / accept the failure-mode and update the card / escalate to a different operating mode.

### Honesty discipline

The orchestrator-critic card has the same honesty discipline as the audience Threshold Discipline section (URI-017). Specifically: PASS-WITH-NOTES is not a hand-wave; "long-run" with no hour count or "high-dispatch" with no count is not acceptable. Each note is factual and specific. FAIL is information, not punishment.

### Per-project tuning

The orchestrator-critic card is library-only (`staff/orchestrator-critic/card.md`); there is no per-project copy. Future projects that need different thresholds (e.g., a longer season with a higher dispatch budget) update the card directly via the card's §"Versioning" protocol — empirical recalibration after enough runs produce verdict-discipline data.

---

## Phase 7 — Mechanical split write-out

Runs after Phase 6 verdict. **No review loop, no kickback.** This phase is bookkeeping: take the converged bones + the final S10 cut proposal + the per-window tens files, write them to per-episode files, persist the split into showrunner memory.

If Phase 6 verdict was FAIL, do **not** run Phase 7 — escalate to user, who decides whether to fix the run or accept the failure. If PASS-WITH-NOTES, Phase 7 runs normally (notes inform next session's planning, not this one's persistence).

### Step 1 — Number episodes

Number `<season-slug>e01`, `<season-slug>e02`, … in season order against the final accepted S10 cut points. No titles.

### Step 2 — Write per-episode files

For each episode, write `active-project/theater/proto-lines/<season-slug>e<NN>.md`. Header (seven required fields, in order):

```
# proto-lines — <episode-slug>

episode: <episode-slug>
narrator: <pov-actor-slug>
goal: <one sentence — what this episode shows the audience>
cast: <slug>, <slug>, <slug>, ...
locations: <loc-slug>, <loc-slug>, ...
prior_episode: <previous-episode-slug | none>
aggregate_range: <from>-<to>
```

Field rules:
- **`episode:`** — episode slug (matches filename).
- **`narrator:`** — plan-designated narrator (URI-009 — the season-plan's POV ruling wins over raw line-count dominance inside the bones).
- **`goal:`** — orchestrator distills from the bones-stretch + dramatist's per-cut rationale.
- **`cast:`** — comma-separated actor slugs appearing as SUBJECT or `speaks to <listener>` listener anywhere in this episode's bones. Computed by slug-grep over the bones; order by first-appearance ID; no inference.
- **`locations:`** — slug-grep over OBJECTs and SUBJECTs against warehouse loc cards.
- **`prior_episode:`** — slug of previous episode in season order, or `none` for e01.
- **`aggregate_range:`** — the contiguous bones-id range covered by this episode (e.g. `1-87`). Replaces per-line `# aggregate-id:` comments.

Body: bones from the stretch, **renumbered 1..M** starting at 1 per episode. POV `# pov:` markers copied through. No per-line `# aggregate-id:` comments (URI-010 position-aware mapping handles fault routing).

### Step 3 — Validate

For each per-episode file: seven header fields present, contiguous numbering 1..M, no orphan content. `cast` matches slug-grep (sanity check, not gate). `aggregate_range` contiguous and non-overlapping with siblings; union of all ranges equals the bones file's 1..N (accounting for legal ID-deletion gaps per URI-010).

### Step 4 — Tens-file finalization (URI-026)

Rename the slug-suffixed `tensometer-<season-slug>-window-{NN}.md` files to `tensometer-<season-slug>e<NN>.md` matching the final episode slugs. These travel with each per-episode proto-line file and are the bone-gate's deliverable. `/and-shoot` Phase 0 renames the active-episode tens file to `theater/facets/tensometer.md` as its working surface; the slug-suffixed copy remains as canonical archive.

`/and-facets-r1` Layer 1 (legacy tens authoring at `theater/facets/tensometer.md`) is **not** touched; it remains operational. No path collision.

### Step 5 — Persist split into showrunner memory

Update `seasons[<slug>].episodes[]` with one entry per produced episode (`slug`, `status: protolined`, `narrator`, `interlude` flag if applicable, `chunk` (post-hoc one-paragraph distill), `proto_lines_path`, `cast`, `locations`, `prior_episode`, `aggregate_range`). No title field.

Set `active.episode: <season-slug>e01`. Season status remains `active` until `/and-wrap`.

### Step 6 — Print Phase 7 summary

```
--- SPLIT WRITE-OUT COMPLETE ---
Episodes produced: <count, multiple of 3>
Files:
  active-project/theater/proto-lines/<season-slug>e<NN>.md (× N)
  active-project/theater/facets/tensometer-<season-slug>e<NN>.md (× N)
Next: /and-shoot or /and-facets per active.episode, or /and-wrap.
```

---

## Notes

- This command **mirrors but does not invoke** /and-protolines-v2's five-pass pipeline. /and-protolines-v2 remains the standalone per-episode authoring command for ad-hoc work or single-episode revision after Phase 7 write-out.
- Phase 1 (per-episode decomposition) is removed under the emergent-split rule. The bones are one continuous object until Phase 7.
- Phase 4 is removed. Split identification (dramatist proposes provisional cuts; tens + audience+mechanic verify shape) lives inside Phase 3 as Pass S10. The actual write-out is Phase 7, after Phase 6 verdict.
- Per-episode files are derived from the bones at Phase 7 write-out. The bones file is the canonical pre-split artifact and is preserved; downstream revision of a stretch edits the bones and re-runs the affected portion of Phase 3.
- **Execution is fan-out, not sequential.** Phase 2 review and Phase 3 sweeps fire as parallel Agent blocks (one assistant turn each). The orchestration layer (Sweep A / Sweep B / Collation / Fix Routing / Re-fire) governs *when* dispatches fire; the per-pass briefs (`### Pass S1` … `### Pass S10`) are the *fork reference content* — what each dispatch is told to do.
- Subsequent-season equivalent: season N+1 must first be planned via `/and-season-plan <slug>`, which authors `season-<slug>-plan.md` with content beats. Once the prerequisite is met, `/and-season <slug>` runs identically.
