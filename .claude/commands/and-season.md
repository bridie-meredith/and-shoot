---
description: Season-scope orchestrator. Authors one continuous SVO aggregate covering the whole season, iterates the five-pass SVO pipeline + 10-pass season-scope review (S1, S2, S3, S3.5, S4, S4.5, S5, S6, S7, S8, S9) against that aggregate, then splits to per-episode files by interpretive cut (ideal size + dramatic shape; episode count must be a multiple of 3). Run is judged at Phase 6 against staff/orchestrator-critic/card.md — PASS/PASS-WITH-NOTES/FAIL gate. Usage - /and-season [season-slug]
---

The season is the natural authoring unit. Episode boundaries are *outputs* of this command, not inputs — they are decided at Phase 4 by interpretive cut against ideal size and dramatic shape, not by pre-segmented per-episode chunks.

You are the orchestrator. All work routes through subagent dispatches.

**Two governing rules** (saved to memory; restated here for orchestration clarity):
- **Emergent splits.** No per-episode decomposition is authored upfront. Phase 2 produces ONE flat aggregate covering the whole season, continuously numbered 1..N, with no `# === episode: ===` delimiters. Per-episode chunk paragraphs in `season-<slug>-plan.md` (or its successor "content beats") are *content guidance* for the writer — not section boundaries the writer must honor.
- **Episode count multiple of 3.** Phase 4 split must yield an episode count that is a multiple of 3 (3, 6, 9, 12...). The Phase 4 dramatist proposes the count.
- **No titles, ever.** No `title:` field is authored on the season or on any episode. Slugs only.

## Args

- `$1` — optional. Season slug (e.g. `s01`). If omitted, use `active.season` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve season slug.
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Season exists in `seasons[]` with status `active`.
   - `season-<slug>-plan.md` exists with season chunk + season drama statement + content beats (the latter as continuous content guidance, no longer interpreted as per-episode boundaries).
3. Determine resume point:
   - **No aggregate file exists** (`active-project/theater/proto-lines/<season-slug>.aggregate.md` absent) → start at Phase 2 Pass 1.
   - **Aggregate exists, season status `active`, no `protolines_complete` field** → resume at the appropriate phase based on which audit reports already exist under `active-project/staff/auditor/season-<slug>-pass-*`.
   - **`season.protolines_complete` set** → abort; the season has already run through this pipeline.
   - Season status `wrapped` → abort.
4. Print:

```
Season: <slug>
Aggregate: <absent | exists @ <path>>
Resume point: <Phase 2 Pass 1 | Phase 2 Pass <n> | Phase 3 Pass S<n> | Phase 4 split>
```

---

## Phase 1 — REMOVED

Phase 1 (per-episode decomposition) has been removed under the emergent-split rule. The season is authored as one continuous object; per-episode `episode-plan.md` files are produced (if needed at all) only at Phase 4 split, derived from the converged aggregate. Aggregate authoring proceeds directly from the season-plan content beats.

---

## Phase 2 — Aggregate proto-line authoring

Phase 2 produces a single flat SVO aggregate covering the entire season. Continuous numbering 1..N. **No internal episode delimiters.** No header naming an episode slug. The aggregate is the canonical artifact through review and revision.

### Output path

`active-project/theater/proto-lines/<season-slug>.aggregate.md`

### Format

```
# Season Aggregate Proto-Lines — <season-slug>
# schema: schemas/proto-line.schema.md
# Continuous flat numbering 1..N. Episode boundaries decided at Phase 4 split.
# POV transitions are inline (interlude beats are flagged inline, not as section breaks).

1 ...
2 ...
3 ...
...
N ...
```

POV transitions inside the aggregate (e.g. an interlude beat where the narrator switches from Taylor to Mira) are flagged inline at the proto-line where the switch occurs, using a comment line of the form `# pov: <slug>` immediately preceding the first proto-line of the new POV stretch. The Phase 4 split must not cut across a POV-coherent stretch.

### Sub-passes (mirror of `/and-protolines-v2`'s five-pass pipeline, run against the aggregate as one object)

1. **Pass 1 — Inventory write.** Single SVO-writer dispatch. Inputs: the season chunk, the season drama statement, ALL content beats from `season-<slug>-plan.md` (treated as continuous content guidance, NOT section boundaries), all active condition cards, behavior cards for the season's full active cast, series + season vibe-clouds. Output: the aggregate file with continuous bones from start of season to end of season. The writer is explicitly told **NOT to insert episode delimiters** and **NOT to honor pre-existing slug labels** on the content beats. Continuous flat numbering 1..N.
2. **Pass 2 — Constraint audit.** Auditor fork. Sweep against condition cards, series laws, harsh-SVO discipline.
3. **Pass 3 — Shape.** Dramatist. Per-stretch dramatic shape AND season-wide escalation arc.
4. **Pass 4 — Trim.** Audience ×3. Per-stretch ENGAGED/TOLERATED/BORED + season-wide entertainment-density check.
5. **Pass 5 — Continuity.** Auditor #2 fork. Cross-season state, prop chains, POV transitions, reachability.

Faults route to fixer (line edits) or screen-writer (stretch regenerations or cross-stretch restructures). Each fix invalidates downstream passes for the affected scope; downstream re-runs from the changed point.

Convergence cap: **3 full pipeline iterations.** Non-convergence aborts the chain and surfaces for human review with the failing-pass list.

### Why aggregate-first / why no internal delimiters

- The writer sees the whole season at once and is *not* asked to retrofit cross-section consistency.
- Pre-baked episode boundaries pull the writer into honoring section closes and opens that may not be where the bones actually want to break. Removing the delimiters lets the bones breathe; the cuts are decided by Phase 4 against the bones that exist, not against where boundaries were predicted before any bone was written.
- Review operates on a single object, matching how a reader consumes the season.

### Relationship to `/and-protolines-v2`

`/and-protolines-v2` remains the per-episode standalone authoring command for ad-hoc work or single-episode revision after split. Its five passes are the *template* for Phase 2's sub-passes here, scaled up to season scope. /and-season does not invoke /and-protolines-v2 per episode at any point.

---

## Phase 3 — Comprehensive season-scope review

After Phase 2 produces a converged aggregate, run the **nine-pass season-scope review** against the single aggregate. Same reviewer roles as per-episode review, scaled up: the criteria are season-scope (cross-stretch coherence, season escalation arc, season-wide entertainment density, etc.).

In the pass briefs below, references to "chapters" / "sections" / "episodes" inside the aggregate are *interpretive*: a stretch of bones a reviewer treats as a coherent unit for evaluation. They do not correspond to authored delimiters (there are none in the aggregate). Reviewers identify stretches by reading; the writer never authored them as such.

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

### Pass S4.5 — Post-split continuity (auditor, runs after Phase 4 split is finalized) (URI-012, 2026-05-10)

S4 covers continuity *inside* the aggregate. S4.5 covers continuity *across* the post-split episode boundaries, where a reader experiencing the split as discrete episodes meets a different surface than a reader experiencing the aggregate continuously.

**S4.5 runs after Phase 4 Step 3** (per-episode files exist) and before Phase 5 persistence. It is one of the nine passes for season-scope review only when the split has been performed; on Phase 3 iterations before the split it is skipped.

Inputs: per-episode proto-line files; aggregate; season-plan; behavior cards for active cast.

Brief — for each episode boundary `eN → eN+1`, verify that **state-changes in eN's close region (last 20 bones)** are visible as **active constraints in eN+1's open region (first 10 bones)**. Specifically, for each board-change in eN's last 20 bones that introduces a new state (apprentice-mark, pastoral-claim, surveillance-record, debt, letter-event, monument callback, prop handoff), the eN+1 open must carry at least one bone signaling that state as active in the POV character's working state — **physical-register, not exposition**.

Per-boundary verdict: `BOUNDARY-CARRIES` or `BOUNDARY-DROPS-{state}`.

Output: `active-project/staff/auditor/season-<slug>-pass-S4.5-post-split-continuity.md`. File-level: `POST-SPLIT-CONTINUITY-OK` or `POST-SPLIT-CONTINUITY-FAIL-{boundary-list}`.

Faults at this pass route to **screen-writer** for targeted bone additions at the failing eN+1 open (typically 1–2 physical-register bones; the state is signaled, not narrated). The aggregate is updated; a re-split may be required if the bone additions shift line counts beyond Phase 4 Step 1(a) tolerance.

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

### Convergence

Phase 3 converges when **all season-scope review passes return clean verdicts in a single end-to-end run** (S1, S2, S3, S3.5, S4, S5, S6, S7, S8, S9 — plus S4.5 once Phase 4 split has produced per-episode files). Same iteration loop as Phase 2: a change at any pass invalidates downstream passes; downstream re-runs from the changed point. Cap: **3 full season-scope iterations.** Non-convergence ships with a header comment + escalates to user.

### Iteration cap relationship

Phase 2 and Phase 3 each have an independent cap of 3 iterations. They are sequential. Phase 3 fault routing flows back into the aggregate; a Phase 3 fix that requires regenerating a stretch invokes screen-writer in stretch-regeneration mode — does NOT restart Phase 2's five-pass pipeline. Worst-case combined budget: 6 full-pipeline iterations.

---

## Phase 4 — Interpretive split (ideal size + dramatic shape)

Run after Phase 3 converges. **Interpretive, not mechanical** — the aggregate has no internal delimiters; the splits must be authored against the bones that exist.

### Step 1 — Dramatist proposes splits

Dispatch **dramatist** with:
- The converged season aggregate.
- `season-<slug>-plan.md` (season drama, content beats — for context, not as cut-points).
- `series-plan.md`.
- Behavior cards for active cast.
- The two split criteria: **(a) ideal episode size, (b) dramatic shape.**

Brief — propose episode boundaries against:
- **(a) Ideal episode size.** Default target band: each episode 80–160 proto-lines (configurable by orchestrator if the aggregate's total line-count makes the band infeasible). All proposed episodes should fall within the band; no single episode may exceed 2× the band's lower bound or fall below half it.
- **(b) Dramatic shape.** Each cut must close on a beat that earns its own next-open. An episode close on a flat beat is a fault. Adjacent episodes' shape arcs must compose into the season's overall rise-peak-fall.
- **Hard constraint: episode count must be a multiple of 3** (3, 6, 9, 12...). The dramatist must select a count from the multiples-of-3 set that best fits the bone density and dramatic shape of the converged aggregate. If no multiple-of-3 count fits without violating (a) or (b), surface as `SPLIT-INFEASIBLE` and escalate to user.
- **POV honor.** No cut may bisect a POV-coherent stretch (identified by inline `# pov:` comments). Interlude stretches must be wholly contained within a single episode.

Dramatist outputs a proposed split plan: a list of cut-points (proto-line IDs where episode N ends and N+1 begins) and a one-line rationale per cut.

Output: `active-project/staff/auditor/season-<slug>-split-proposal.md`.

### Step 1.5 — Tens authoring per proposed episode (URI-026, 2026-05-10) — BONE-GATE

The bones-first principle: the proto-lines are load-bearing. Audience review at Step 2 must judge tens-rated bones, not bare bones — bare-bone review cannot catch flatlined stretches or false peaks adversarially. Step 1.5 produces per-proposed-episode tens ratings that Step 2 reads.

**Position:** runs after Step 1 (split proposal exists with cut-points) and before Step 2 (audience review). The split is still provisional — Step 1.5's tens-rating is also provisional in the sense that if Step 2 rejects the split, the next split iteration re-fires Step 1.5 on the revised boundaries.

**Dispatch:** **dramatist** in fork-mode, one fork per proposed episode, in parallel.

**Fork-discipline brief (identical to `/and-facets-r1` Layer 1a:88):**
- **Read inputs:** the proposed-episode bone stretch (proto-line IDs `<from>`–`<to>` from the split proposal); `design/shoot-v2/rubric-tensometer.md` (the locked tens rubric); `schemas/facet.schema.md`.
- **Forbid loading:** behavior cards, vibes, audience personas, source prose. The dramatist rates the bones mechanically against the rubric, not aesthetically.
- **Output path:** `active-project/theater/facets/tensometer-<season-slug>e<NN>.md` (slug-suffixed to avoid collision with `/and-facets-r1`'s canonical `tensometer.md`; the `<NN>` is the proposed episode index at this iteration).
- **Output format:** per-rubric (rung-1 / rung-2 / rung-3 entries, back-cite `[tens:N]` discipline, scene-shape verdict). Same shape `/and-facets-r1` Layer 1a produces; only the path differs.

**Rubric scope:** the tens rubric is calibrated per-episode (~150-line corpus, unique-climax-per-episode clause, scene-boundary by location-state inheritance with TBD-boundary fallback). Per-proposed-episode invocation here matches the calibrated scope.

**Dispatch budget:** 1 per proposed episode (3–6 per season). Parallel; wall-clock dominated by slowest fork.

**Failure handling:** a dramatist refusal (rubric self-flag) propagates as `TENS-AUTHORING-REFUSED-<episode>` and routes to dramatist re-dispatch with the named refusal context. Cap: 2 retries per episode.

### Step 2 — Audience review of the split (EXTENDED — bones+tens, shared-reviewer per URI-026)

Dispatch the three audience personas in parallel against the proposed split. Each persona fork reads **bones + the per-proposed-episode tens-rating file** authored at Step 1.5, plus the standard inputs (persona card with `Threshold Discipline` + `Season-Scope Adversarial` body sections; series-plan; season-plan; active vibes).

**Shared-reviewer principle.** The audience taste discipline + mechanic class library used here is the **same** as `/and-facets-audit.md`'s TASTE-FLAG + AP-SCAN + CURVE-SHAPE + FREQUENCY-BAND surface. The audience produces a taste verdict; the auditor (dispatched in narrow-scope mode below) produces a mechanic verdict against the same class library `/and-facets-audit.md` defines. **No `/and-season`-specific reimplementation.** Patterns surfaced here that escape the mechanic rubric feed TASTE-FLAG → AP-SCAN graduation in the shared auditor over time.

**Per-persona report structure** — two **separately named, owner-attributed** sections, in addition to the existing SPLIT-{ACCEPT,REVISE} verdict:

- **§ Audience taste verdict** (`OWNER: audience`) — ENGAGED / TOLERATED / BORED per stretch + persona-specific tens-attack findings. Tens-attack categories the persona may raise (carried in the dispatch brief until promoted to persona-card body in Phase 1.5):
  - `RUNG-DISTRIBUTION-FLATLINE-{line-range}` — long contiguous run of tens=1 with no rung-2 inflection.
  - `FALSE-PEAK-{line}` — tens=3 with no rung-2 precursor in the preceding ~5-bone window.
  - `DENOUEMENT-FLAT-{episode}` — post-peak window with zero tens=3 and zero board-changes.
  - `RUNG-CLUSTER-OVERSATURATION-{line-range}` — multiple tens=3 adjacent without release.
- **§ Mechanic arithmetic verdict** (`OWNER: rubric`) — auditor narrow-scope dispatch (see below). Class library is `/and-facets-audit.md`'s; the auditor is invoked with a per-episode tens-only payload.

Brief: read each proposed episode's stretch as a unit. Per-episode verdicts (mechanic-bearing per URI-011, 2026-05-10):

- **OPEN-ENGAGES** — the episode's first 10 numbered-line bones must contain at least one of:
  - (i) a **board-change beat** (a state-change or board-state shift visible at bone level — e.g., a slug enters or exits, an item changes hands, a named action lands);
  - (ii) a **tension-bearing image carrying forward state** from the prior episode's close (the inherited state must be specifically signaled, not merely scenically continuous);
  - (iii) a **season-plan-designated establishing-register beat** (e.g., the early-baseline ecological uncanny). This option requires explicit `season-<slug>-plan.md` designation; a beat is not "establishing-register" unless the plan names it as such.
  
  If none of (i)/(ii)/(iii) is present in the first 10 bones, flag `OPEN-ENGAGES-FAIL`.

- **CLOSE-EARNS-NEXT** — the episode's final 5 numbered-line bones must contain at least one of:
  - (i) an **unresolved board-change** (a state-change or pressure that is open at episode-close and earns a specific next-open);
  - (ii) a **forward-momentum image** (active subject + forward verb that creates a specific reader expectation for the next episode).
  
  If the episode's last board-change is more than 20 bones before the close, flag `CLOSE-EARNS-NEXT-AFTERMATH-DRIFT-{N}` where N is the bone-count between last board-change and close. Aftermath-drift > 20 bones is a fault regardless of how the close itself reads.

- **SHAPE-COHERENT** — the episode's interior bone-density of board-changes must produce a recognizable rise/peak/fall scaled to episode size:
  - The episode peak (the highest-stakes board-change line) must land in the back two-thirds of the episode body.
  - If any 30-bone window contains fewer than 1 board-change, flag `SHAPE-COHERENT-FLATLINE-{line-range}`.
  - If the post-peak section exceeds 50% of episode length AND contains fewer than 2 board-changes, flag `SHAPE-COHERENT-FLAT-AFTERMATH-{episode}` (HARD). 40-50% with <2 board-changes is SIGNAL.
  - The mechanic operates on bone-level data and is independent of season-plan defenses; citing season-plan mandate does not override a structural verdict (the plan licenses the register, not the shape).

**Mechanic-arithmetic dispatch (narrow-scope auditor).** In parallel with the three audience-persona forks, dispatch the **auditor** once per proposed episode with a narrow-scope payload (per-episode tens file + the proposed-episode bones + the relevant rubric classes from `/and-facets-audit.md`). The auditor runs only the tens-relevant subset of its 11-class library:

- **FREQUENCY-BAND** (tens-only): rung-1 / rung-2 / rung-3 distribution against the band 60-75% / 20-30% / 5-10%; per-rubric breach-low / breach-high flags.
- **CURVE-SHAPE** (per `and-facets-audit.md:81–87`): scene-level peak presence; 1→3 jump candidates; 3→3 release-after-peak checks; flatlining (30+ contiguous beats with no rung-2-or-3); episode-level act structure verdict `SHAPE-OK` / `SHAPE-FAIL`.
- **AP-SCAN** (tens-only): AP1 ambient-escalation, AP2 speech-beat-default, AP3 climax-bleed, AP4 plot-importance-inflation, AP5 stillness-inflation (per rubric).

Output: `active-project/staff/auditor/season-<slug>-pass-S4-split-mechanic-{episode-slug}.md`. File-level: `MECHANIC-CLEAN` or `MECHANIC-FAIL-{class-list}`. Findings carry `OWNER: rubric` tag.

**Audit command provenance.** The mechanic-arithmetic auditor reads the same rubric classes defined in `.claude/commands/and-facets-audit.md`; the dispatch brief cites those class definitions by reference. The audit command itself is **not** modified — the shared surface is the class library, consumed from both pipelines.

**Combined per-episode verdict.** For each proposed episode:

- **`SPLIT-ACCEPT`** if ≥2-of-3 personas ACCEPT (the original threshold) AND `MECHANIC-CLEAN` AND no `SHAPE-COHERENT-FLAT-AFTERMATH-{episode}` HARD AND no `OPEN-ENGAGES-FAIL` AND no `CLOSE-EARNS-NEXT-AFTERMATH-DRIFT-{N>20}`.
- **`SPLIT-REVISE-bones-{line-range}`** if a `RUNG-DISTRIBUTION-FLATLINE` / `FALSE-PEAK` / `DENOUEMENT-FLAT` / `SHAPE-COHERENT-FLATLINE` / `MECHANIC-FAIL-CURVE-SHAPE-SHAPE-FAIL` is localized to a specific stretch within the proposed episode (regen the stretch in the aggregate, not the split).
- **`SPLIT-REVISE-cut-{reason}`** if the failure is the cut itself (open/close/aftermath-drift) — re-propose boundaries.

**Bone-regen routing (REGEN-mode discipline per URI-026):**

- **`REGEN-REPLACE`** — replace existing bones in the named window in-place. Preserve aggregate IDs of surviving bones per URI-010 stable-overrides-monotonic; new replacements re-use vacated IDs only if surviving bone deletes are explicit. Default routing for `RUNG-DISTRIBUTION-FLATLINE` and `FALSE-PEAK`.
- **`REGEN-ADD`** — add bones to the named window without replacing survivors. New bones receive next-available IDs in the 900-range (legal-survivor pattern). Default routing for `DENOUEMENT-FLAT` and `SHAPE-COHERENT-FLATLINE` when the fix is increasing rung-2-or-3 density.
- **`REGEN-BOTH`** — both replace and add. Routed only when audience explicitly cites both flatline and oversaturation in the same window.

The screen-writer regen brief MUST carry the `REGEN-{REPLACE,ADD,BOTH}` instruction explicitly, the affected line range, position-aware-mapping discipline (URI-010), and inline `# pov:` marker preservation.

Per-persona output: `season-<slug>-split-review-{persona}.md` — now carries both § Audience taste verdict and § Mechanic arithmetic verdict sections per the structure above. File-level: `SPLIT-ACCEPT` or `SPLIT-REVISE-{reason}`. ≥2-persona threshold for the audience component; mechanic component is independent.

If any per-episode verdict is `SPLIT-REVISE-bones-{line-range}`, the regen routes to **screen-writer** (with REGEN-mode + line range + URI-010 + `# pov:` preservation) for in-aggregate stretch regeneration. After regen: Step 1.5 re-fires for the affected proposed-episode tens-rating, then Step 2 audience+mechanic re-fires for that episode only (not the whole split).

If any per-episode verdict is `SPLIT-REVISE-cut-{reason}`, the dramatist re-proposes boundaries and the full Step 1.5 + Step 2 re-runs.

**Per-window iteration cap: 2** (tightened from the 3 of the surrounding Phase 4 outer loop, per URI-026 bone-gate budget discipline). After 2 inner regen iterations on the same window without convergence, escalate: the residual is a `tens-gate-residual-HARD` finding routed to Phase 6 (orchestrator-critic F7).

### Step 3 — Mechanical write-out

Once split is accepted:
1. Number the resulting episodes `<season-slug>e01`, `e02`, ... in season order. (No titles.)
2. For each episode, write `active-project/theater/proto-lines/<season-slug>e<NN>.md` containing:
   - Header (seven required fields, in order):
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
       - **`episode:`** — the episode slug (matches filename). Facet authors lift verbatim into facet-file `episode:` frontmatter.
       - **`narrator:`** — the **plan-designated narrator** for the chunk. Set at planning time before any line generation, held consistent across the chunk. When `season-<slug>-plan.md` POV rulings designate an interlude narrator for a content beat (e.g., `INTERLUDE narrator: <slug>`), that designation is authoritative — it is **not** overridden by raw line-count dominance after authoring. The dominant inline `# pov:` marker inside the stretch is informational and may be cross-checked against the plan; if they disagree, the plan wins. (Per URI-009, 2026-05-10.)
       - **`goal:`** — orchestrator distills from the stretch's beats and the dramatist's per-episode rationale.
       - **`cast:`** — comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener anywhere in this episode's bones. Computed by orchestrator at split time via slug-grep over the episode's proto-lines (no inference, no card lookup). Order: by first-appearance ID. Listener-only slugs (someone spoken to but never speaking or acting) included plain (no suffix).
       - **`locations:`** — comma-separated location slugs the studio fork must load to author location-state. Derived from slug-grep over proto-line OBJECTs and SUBJECTs (e.g. `taylor enters the yard` → `the-yard`); orchestrator resolves `the <noun>` references against the active warehouse's loc cards. Studio fork may discover additional implicit locations during loc-state authoring; those are recorded as feedback signals, not back-edited into this header.
       - **`prior_episode:`** — slug of the previous episode in season order, or `none` for e01. Used by `/and-shoot-v2` Phase 0 to know which prior-episode state files to snapshot for handoff baseline.
       - **`aggregate_range:`** — the contiguous aggregate-id range covered by this episode (e.g. `1-87`). Replaces per-line `# aggregate-id:` comments. Computed from Step 3.2 renumbering.
     A blank line follows the header before the body.
   - Body: the proto-lines from the stretch, **renumbered 1..M** starting at 1 per episode. The aggregate's continuous numbering is preserved by the `aggregate_range:` header field (single line). **Per-line `# aggregate-id:` comments are not authored** — fixers compute the aggregate-id by `aggregate_range_start + episode_id - 1` when routing faults back to the aggregate. The body remains comment-clean per the proto-line schema's no-decoration rule (POV markers excepted; copied through from the aggregate).
     **Position-aware mapping (URI-010, 2026-05-10).** Aggregate files MAY contain non-monotonic IDs as legal artifacts of pass-level reordering — IDs are stable per `schemas/proto-line.schema.md` ("once assigned, never reused, never reassigned"; "re-ordering preserves IDs"); the aggregate's IDs reflect their assignment history, not their current narrative position. When the aggregate range covered by an episode contains non-monotonic IDs, the shortcut formula `aggregate_id = aggregate_range_start + episode_id - 1` does NOT produce correct mappings. Fixers must use **position-aware mapping** (file-line position within the aggregate) to resolve `episode_id → aggregate_id`. The shortcut formula is valid only when the per-episode file maps to a contiguous monotonic ID range in the aggregate.
3. Validate: each per-episode file has `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`, contiguous numbering 1..M, no orphan content. `cast` matches the slug-grep over the episode's bones (sanity check, not gate). `aggregate_range` is contiguous and non-overlapping with sibling episodes' ranges; the union of all episodes' ranges equals 1..N (the aggregate's full range, accounting for legal ID-deletion gaps).
4. The aggregate is preserved as the canonical pre-split artifact under its original path; per-episode files are derived. Downstream revision of a stretch should edit the aggregate and re-run Phase 4 (the split itself may shift if the revision changes shape).
5. **Tens-file finalization (URI-026, 2026-05-10).** The slug-suffixed `tensometer-<season-slug>e<NN>.md` files written by Step 1.5 are now finalized. Per-episode tens files are the bone-gate's deliverable and travel with each per-episode proto-line file:
   - The provisional-iteration suffix is dropped if the final accepted split's episode indexes match; otherwise the relevant tens files are renamed to match the final episode slugs.
   - When `/and-shoot` Phase 0 starts an episode, it renames `theater/facets/tensometer-<season-slug>e<NN>.md` → `theater/facets/tensometer.md` for the current-episode working surface. The slug-suffixed copy remains as canonical archive.
   - `/and-facets-r1` Layer 1 (legacy tens authoring at `theater/facets/tensometer.md`) is **not** edited by this session; it remains operational. There is no path collision because /and-season writes to slug-suffixed paths.

---

## Phase 5 — Persist

1. Update `active-project/staff/showrunner/memory.md`:
   - Write `seasons[<slug>].episodes[]` with the actual split — one entry per produced episode. Each entry (existing fields first, /and-shoot-v2-handoff fields appended):
     - `slug`
     - `status: protolined`
     - `narrator`
     - `interlude` flag if applicable
     - `chunk` (orchestrator distills a one-paragraph chunk from the bones — this is post-hoc content guidance, not a plan)
     - `proto_lines_path`
     - `cast` — same comma-separated slug list as the file header. Mirrored into memory so showrunner can answer "who's in episode N" without opening the file.
     - `locations` — same as header.
     - `prior_episode` — same as header.
     - `aggregate_range` — same as header.

     **No title field.**
   - Add `seasons[<slug>].protolines_complete` with timestamp + comprehensive audit path.
   - Set `active.episode: <season-slug>e01` (the new first-episode slug after split).
   - Season status remains `active` until `/and-wrap`.
2. Print summary:

```
--- SEASON PROTO-LINES COMPLETE: <season-slug> ---

Aggregate proto-lines: <total count>
Episodes after split: <count, multiple of 3>
Split iterations: <n of 3 max>

Phase 2 (aggregate authoring, 5-pass pipeline):
  iterations to converge: <n of 3 max>
  Pass 1 inventory:  WRITTEN
  Pass 2 constraint: <CLEAN | FAIL>
  Pass 3 shape:      <CLEAN | RE-ORDER-OR-REVISE>
  Pass 4 trim:       <ALL-ACCEPT | REVISE-{persona}>
  Pass 5 continuity: <CLEAN | FAIL>

Phase 3 (season-scope review, 9 passes):
  S1   constraint:        <PASS | FAIL>
  S2   shape:             <CLEAN | RE-ORDER-OR-REVISE | STRUCTURAL-FAILURE>
  S3   trim ×3:           <ALL-ACCEPT | REVISE-{persona}>
  S3.5 ruleset:           <RULESET-CLEAN | RULESET-FAIL>
  S4   continuity:        <SEASON-CONTINUITY-OK | SEASON-CONTINUITY-FAIL>
  S4.5 post-split-cont:   <POST-SPLIT-CONTINUITY-OK | POST-SPLIT-CONTINUITY-FAIL-{boundary-list} | (skipped, no split yet)>
  S5   voice:             <VOICE-COHERENT | VOICE-DRIFT>
  S6   vibe ×3:           <VIBE-ALIGNED | VIBE-DRIFT-{reason}>
  S7   facet-readiness:   <FACET-READY | FACET-GAPS>
  S8   plausibility:      <PLAUSIBLE | IMPLAUSIBLE>
  S9   comprehensibility ×3: <COMPREHENSIBLE | COMPREHENSIBILITY-RISK-{reason}>
  iterations to converge: <n of 3 max>
  file-level: <SEASON-CONVERGED | SEASON-FAIL with failing pass names>

Phase 4 (interpretive split):
  dramatist proposal:           <proto-line IDs of cuts>
  Step 1.5 tens-authoring:      <PASS | RETRIES:<n>> (URI-026 bone-gate)
  Step 2 audience review:       <ALL-ACCEPT | REVISE-{persona}>
  Step 2 mechanic verdict:      <ALL-MECHANIC-CLEAN | MECHANIC-FAIL-{episode}:{classes}>
  Step 2 inner regen iters:     <n of 2 max per window>
  Tens-gate convergence:        <PASS | NEEDS-ITER | FAIL — residual HARD>
  episodes produced:            <count, multiple of 3>

Files:
  active-project/theater/proto-lines/<season-slug>.aggregate.md (canonical pre-split)
  active-project/theater/proto-lines/<season-slug>e<NN>.md (× N, post-split)
  active-project/theater/facets/tensometer-<season-slug>e<NN>.md (× N, post-split — URI-026 bone-gate)
  active-project/staff/auditor/season-<slug>-pass-S{1,2,3-{persona},3.5,4,4.5,5,6-{persona},7,8,9-{persona}}.md
  active-project/staff/auditor/season-<slug>-pass-S4-split-mechanic-{episode-slug}.md (× N, URI-026)
  active-project/staff/auditor/season-<slug>-split-proposal.md
  active-project/staff/auditor/season-<slug>-split-review-{persona}.md (× 3)
  active-project/staff/auditor/season-<slug>-orchestrator-verdict.md (Phase 6)

Orchestrator verdict (Phase 6, per staff/orchestrator-critic/card.md):
  <VERDICT: PASS | PASS-WITH-NOTES — <notes> | FAIL — <failure summary>>

Next: facet authoring per episode (/and-locstate, /and-dialogue, etc.) or /and-shoot for performance pass, or /and-wrap for season close.
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

## Notes

- This command **mirrors but does not invoke** /and-protolines-v2's five-pass pipeline. /and-protolines-v2 remains the standalone per-episode authoring command for ad-hoc work or single-episode revision after split.
- Phase 1 (per-episode decomposition) was removed under the emergent-split rule. The season is one continuous object until Phase 4.
- Phase 4 is *interpretive*. There are no delimiters in the aggregate to scan for. The split is authored against the bones that exist by dramatist + audience review, against ideal-size + dramatic-shape criteria, with episode count constrained to a multiple of 3.
- Per-episode files are derived from the aggregate at split time. The aggregate is the canonical pre-split artifact and is preserved; downstream revision of a stretch edits the aggregate and re-runs Phase 4.
- Subsequent-season equivalent: season N+1 must first be planned via `/and-season-plan <slug>`, which authors `season-<slug>-plan.md` with content beats (continuous content guidance) and registers the season as `active`. Once the prerequisite is met, `/and-season <slug>` runs identically.
