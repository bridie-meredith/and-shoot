---
description: Season-scope orchestrator. Authors one continuous SVO aggregate covering the whole season, iterates the five-pass SVO pipeline + nine-pass season-scope review against that aggregate, then splits to per-episode files by interpretive cut (ideal size + dramatic shape; episode count must be a multiple of 3). Usage - /and-season [season-slug]
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

Output: `active-project/staff/auditor/season-<slug>-pass-S3.5-ruleset.md`. File-level: `RULESET-CLEAN` or `RULESET-FAIL`.

### Pass S4 — Continuity (auditor #season-2)

Inputs: post-trim post-shape aggregate; season chunk; series laws; active location cards.

Brief — four sweeps at season scope:
- **Reachability:** season-start state → season-end state per `season-<slug>-plan.md` season chunk; the surviving aggregate must traverse the delta.
- **State:** every prop and actor across the season. Props introduced are consumed/released or persist coherently. Actor entries and exits coherent.
- **Reference:** every slug resolves; no orphan introductions.
- **POV:** narrator transitions inside the aggregate are honest — the narrator-switch position is reachable from prior bones. Inline `# pov:` comment at the switch line is required.

Output: `active-project/staff/auditor/season-<slug>-pass-S4-continuity.md`. File-level: `SEASON-CONTINUITY-OK` or `SEASON-CONTINUITY-FAIL`. Reachability faults at season scope route as `escalate`.

### Pass S5 — Voice register coherence (dramatist, second invocation)

Inputs: aggregate; behavior cards (full inheritance) for every active actor; per-actor vibes.

Brief: each actor's voice register stays consistent across the aggregate per their behavior card. The verbs an actor *takes* should match the actor's voice signature; out-of-register acts flagged; no drift between an actor's first-stretch voice and last-stretch voice (modulo arc-driven change).

Output: `active-project/staff/auditor/season-<slug>-pass-S5-voice-coherence.md`. Verdict: `VOICE-COHERENT` or `VOICE-DRIFT`.

### Pass S6 — Vibe and theme alignment (audience ×3, second invocation)

Inputs as for S3, plus per-actor vibes and studio vibes for each setting.

Brief: read the aggregate as a tonal arc. Each stretch's beats honor the active vibe-cloud; series.theme propagates into stretch-level beats; the season's tonal register is consistent.

**Per-window vibe verdict (MANDATORY)** logged per ~10-line window: `VIBE-ALIGNED` or `VIBE-DRIFT-{reason}`.

Per-persona output: `season-<slug>-pass-S6-vibe-{persona}.md`. ≥2-persona threshold for accepting drift flags. Bias: when in doubt, flag drift.

### Pass S7 — Facet-readiness (auditor #season-4, dedicated)

Inputs: aggregate; `schemas/facet.schema.md`, `schemas/dialogue.schema.md`; locked facet rubrics under `design/shoot-v2/`.

Brief — for each load-bearing beat, verify a citable bone exists for each facet author downstream (location-state, state-updates, tensometer, dialogue, narrator-interest, etc.). Flag over-dense stretches (10+ beats per scene without inflection) and under-dense stretches (a chunk-implied beat with zero supporting bones).

Output: `season-<slug>-pass-S7-facet-readiness.md`. Verdict: `FACET-READY` or `FACET-GAPS`.

### Pass S8 — Plausibility (dramatist + auditor hybrid)

**S8a — Character-action plausibility (dramatist).** For every named-actor action, ask: would this character actually *do* that, given their behavior card, persona card, vibes, and prior-stretch actions? Sharper than voice register — voice asks "does this sound like the character?", plausibility asks "is this what the character would *do*?".

**S8b — Event-in-world plausibility (auditor).** For every beat: plausible in-world given active condition cards, series laws, lore? An event that doesn't violate a constraint but would not realistically occur given how the world works is flagged.

Inputs: aggregate; all behavior cards; all condition cards; series-plan + season-plan; active actor vibes.

Output: `season-<slug>-pass-S8-plausibility.md`. Per-beat verdicts: `PLAUSIBLE` / `IMPLAUSIBLE-CHARACTER-{slug}` / `IMPLAUSIBLE-EVENT-{condition-or-law}`. File-level: `PLAUSIBLE` or `IMPLAUSIBLE`. Structural implausibility routes as `escalate`.

### Pass S9 — Comprehensibility (audience ×3, third invocation)

Brief: read the aggregate as a comprehensibility test for a reader who only has the bones + downstream stitched prose. **You are also the entertainment-at-every-step gate of last resort.**

Per-beat:
- If this beat were missed by the reader, would the rest cohere? A beat whose absence breaks comprehension is **load-bearing** — flag for emphasis, parallel anchoring, or relocation.
- Is the cause-effect chain to the next beat legible without exposition? If reader-comprehension requires interiority, narrator-summary, or off-stage knowledge, the chain is **fragile**.
- Does the proto-line carry enough information for a reader to know *what happened* and *who did what to whom*? Ambiguous slugs, under-specified verbs, pronoun-equivalent referents flagged.

Per-window entertainment check (~10 lines per window): `ENGAGED` / `TOLERATED` / `BORED`. Two consecutive BORED OR three consecutive TOLERATED OR ≥30% of any 100-line stretch BORED-or-TOLERATED → file-level `COMPREHENSIBILITY-RISK-attention-{detail}`.

Per-persona output: `season-<slug>-pass-S9-comprehensibility-{persona}.md`. File-level: `COMPREHENSIBLE` or `COMPREHENSIBILITY-RISK-{reason}`.

### Convergence

Phase 3 converges when **all nine passes return clean verdicts in a single end-to-end run**. Same iteration loop as Phase 2: a change at any pass invalidates downstream passes; downstream re-runs from the changed point. Cap: **3 full season-scope iterations.** Non-convergence ships with a header comment + escalates to user.

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

### Step 2 — Audience review of the split

Dispatch the three audience personas in parallel against the proposed split.

Brief: read each proposed episode's stretch as a unit. Per-episode verdicts:
- **OPEN-ENGAGES** — the open of the episode hooks; you would read on.
- **CLOSE-EARNS-NEXT** — the close lands on a beat that earns the next episode's open.
- **SHAPE-COHERENT** — the episode's interior arc (rise / peak / fall scaled to episode size) reads as one unit, not a slice.

Per-persona output: `season-<slug>-split-review-{persona}.md`. File-level: `SPLIT-ACCEPT` or `SPLIT-REVISE-{reason}`. ≥2-persona threshold for ACCEPT.

If REVISE → dramatist receives the feedback and produces a revised split (still constrained to multiple-of-3); review re-runs. Cap: 3 split iterations.

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
       - **`narrator:`** — POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch.
       - **`goal:`** — orchestrator distills from the stretch's beats and the dramatist's per-episode rationale.
       - **`cast:`** — comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener anywhere in this episode's bones. Computed by orchestrator at split time via slug-grep over the episode's proto-lines (no inference, no card lookup). Order: by first-appearance ID. Listener-only slugs (someone spoken to but never speaking or acting) included plain (no suffix).
       - **`locations:`** — comma-separated location slugs the studio fork must load to author location-state. Derived from slug-grep over proto-line OBJECTs and SUBJECTs (e.g. `taylor enters the yard` → `the-yard`); orchestrator resolves `the <noun>` references against the active warehouse's loc cards. Studio fork may discover additional implicit locations during loc-state authoring; those are recorded as feedback signals, not back-edited into this header.
       - **`prior_episode:`** — slug of the previous episode in season order, or `none` for e01. Used by `/and-shoot-v2` Phase 0 to know which prior-episode state files to snapshot for handoff baseline.
       - **`aggregate_range:`** — the contiguous aggregate-id range covered by this episode (e.g. `1-87`). Replaces per-line `# aggregate-id:` comments. Computed from Step 3.2 renumbering.
     A blank line follows the header before the body.
   - Body: the proto-lines from the stretch, **renumbered 1..M** starting at 1 per episode. The aggregate's continuous numbering is preserved by the `aggregate_range:` header field (single line). **Per-line `# aggregate-id:` comments are not authored** — fixers compute the aggregate-id by `aggregate_range_start + episode_id - 1` when routing faults back to the aggregate. The body remains comment-clean per the proto-line schema's no-decoration rule (POV markers excepted; copied through from the aggregate).
3. Validate: each per-episode file has `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`, contiguous numbering 1..M, no orphan content. `cast` matches the slug-grep over the episode's bones (sanity check, not gate). `aggregate_range` is contiguous and non-overlapping with sibling episodes' ranges; the union of all episodes' ranges equals 1..N (the aggregate's full range, accounting for legal ID-deletion gaps).
4. The aggregate is preserved as the canonical pre-split artifact under its original path; per-episode files are derived. Downstream revision of a stretch should edit the aggregate and re-run Phase 4 (the split itself may shift if the revision changes shape).

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
  S5   voice:             <VOICE-COHERENT | VOICE-DRIFT>
  S6   vibe ×3:           <VIBE-ALIGNED | VIBE-DRIFT-{reason}>
  S7   facet-readiness:   <FACET-READY | FACET-GAPS>
  S8   plausibility:      <PLAUSIBLE | IMPLAUSIBLE>
  S9   comprehensibility ×3: <COMPREHENSIBLE | COMPREHENSIBILITY-RISK-{reason}>
  iterations to converge: <n of 3 max>
  file-level: <SEASON-CONVERGED | SEASON-FAIL with failing pass names>

Phase 4 (interpretive split):
  dramatist proposal:   <proto-line IDs of cuts>
  audience review:      <ALL-ACCEPT | REVISE-{persona}>
  episodes produced:    <count, multiple of 3>

Files:
  active-project/theater/proto-lines/<season-slug>.aggregate.md (canonical pre-split)
  active-project/theater/proto-lines/<season-slug>e<NN>.md (× N, post-split)
  active-project/staff/auditor/season-<slug>-pass-S{1,2,3-{persona},3.5,4,5,6-{persona},7,8,9-{persona}}.md
  active-project/staff/auditor/season-<slug>-split-proposal.md
  active-project/staff/auditor/season-<slug>-split-review-{persona}.md (× 3)

Next: facet authoring per episode (/and-locstate, /and-dialogue, etc.) or /and-shoot for performance pass, or /and-wrap for season close.
```

---

## Notes

- This command **mirrors but does not invoke** /and-protolines-v2's five-pass pipeline. /and-protolines-v2 remains the standalone per-episode authoring command for ad-hoc work or single-episode revision after split.
- Phase 1 (per-episode decomposition) was removed under the emergent-split rule. The season is one continuous object until Phase 4.
- Phase 4 is *interpretive*. There are no delimiters in the aggregate to scan for. The split is authored against the bones that exist by dramatist + audience review, against ideal-size + dramatic-shape criteria, with episode count constrained to a multiple of 3.
- Per-episode files are derived from the aggregate at split time. The aggregate is the canonical pre-split artifact and is preserved; downstream revision of a stretch edits the aggregate and re-runs Phase 4.
- Subsequent-season equivalent: season N+1 must first be planned via `/and-season-plan <slug>`, which authors `season-<slug>-plan.md` with content beats (continuous content guidance) and registers the season as `active`. Once the prerequisite is met, `/and-season <slug>` runs identically.
