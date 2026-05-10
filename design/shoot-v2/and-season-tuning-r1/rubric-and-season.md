---
rubric: and-season
version: V1 (locked for tuning-r1)
date: 2026-05-10
source: .claude/commands/and-season.md @ git-hash cd4aa6595c701483d17ff3b90ab46fd7f11d5ca4
purpose: stable reference for audience adversarial pass + auditor 11-class scan in tuning-r1
---

# /and-season Locked Rubric — V1

This file is a verbatim lift of the season-scope review criteria from the /and-season command body, captured at the SHA above. It does not move during the tuning-r1 run. Carry-back edits land as V1.1 candidates in `H-carry-back.md` and are processed in a separate session.

The rubric covers two scopes:

1. **Phase 3 nine-pass season review** — what the command runs against the converged aggregate before split.
2. **Phase 4 interpretive split** — what the command runs to decide episode boundaries.

## Two governing rules

- **Emergent splits.** No per-episode decomposition upfront. The aggregate is one continuous flat object 1..N with no internal `# === episode: ===` delimiters. POV transitions are inline `# pov: <slug>` markers only.
- **Episode count multiple of 3.** Phase 4 must yield 3, 6, 9, 12... episodes.
- **No titles, ever.** Slugs only.

---

## Phase 3 — Nine-pass season-scope review

### S1 — Constraint audit (auditor)

Inputs: aggregate, all active condition cards, series laws, schema, harsh-SVO discipline.

Sweep:
- Per-line mechanic re-check at season scope.
- Cross-stretch constraint coherence: no stretch violates a constraint another stretch establishes; series laws and condition cards honored consistently.
- Slug + reference resolution: every actor / prop / location slug resolves to its canonical card; no stretch introduces a slug another stretch lacks setup for.

File-level: `PASS` or `FAIL`. Cross-stretch faults requiring chunk-statement revision route as `escalate`.

### S2 — Shape (dramatist) — STRICT

Inputs: aggregate, season-plan.md, series-plan.md, behavior cards (full inheritance) for active cast.

A season without an identifiable buildup, climax, and denouement is a structural failure regardless of how clean any individual stretch reads.

#### Mandatory structural identification (cite proto-line ID ranges)

- **Season buildup (rising stretch):** lines `<from>`–`<to>`. Where stakes are introduced and the season's question is posed. Absent → `NO-SEASON-BUILDUP`.
- **Season climax (peak stretch):** lines `<from>`–`<to>` + specific peak line ID. Single highest-stakes stretch where season tension turns. Cannot point to a single peak stretch → `NO-SEASON-CLIMAX`.
- **Season denouement (falling stretch):** lines `<from>`–`<to>`. Post-peak release. Absent → `NO-SEASON-DENOUEMENT`.

#### Sweep checks

- **Season-level rise-peak-fall:** stretch peaks escalate cumulatively per the season escalation spine. Terminal peak lands at the climax stretch, not earlier.
- **Cross-stretch flatlines:** long stretches without an inflection beat is a season flatline.
- **Forward-flag honor:** commitments from `season-plan.md` (e.g. "the IGNITION beat triggers an involuntary swarm rise") are visible in the corresponding stretches' proto-lines. Missing commitment is a structural fault.
- **Premature peak / late peak:** climax stretch must be in the back half of the aggregate. Earlier → `EARLY-SEASON-PEAK`. Later → `LATE-SEASON-PEAK`.
- **Pacing:** density and weight of inter-stretch transitions match the season's pacing register.

Verdict: `CLEAN` / `RE-ORDER-OR-REVISE` / `STRUCTURAL-FAILURE`. Bias: when in doubt, flag.

### S3 — Trim (audience ×3, season scope)

Inputs: aggregate, season goal pinned at top of brief, all active actor vibes, studio vibes, persona cards, behavior cards, full series-plan and season-plan prose.

Walk every numbered non-blank line. Trim test against season goal. Voice-load-bearing test still applies.

**Entertainment check (MANDATORY):** per ~10-line window:
- `ENGAGED` — taste finds this window delivers a hook the persona is paid to want.
- `TOLERATED` — functional but not entertaining in its own right.
- `BORED` — taste actively disengages.

Cap: at most ~10% of windows TOLERATED, zero BORED. Two consecutive BORED OR three consecutive TOLERATED → REVISE with reason `season-attention-flatline-{line-range}`.

≥2-persona threshold for auto-accept deletion. File-level per persona: `ACCEPT` or `REVISE-{one-clause-reason}`. Bias: when in doubt, REVISE.

### S3.5 — Ruleset compliance (auditor, dedicated)

Re-checks the aggregate against the harsh-SVO ruleset. Drift-pattern report: a verb appearing 5+ times across the season as a borderline state-verb is flagged for systematic recast.

Non-action-verb deny-list: `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`, `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`, `contains`, `houses`, `occupies`, `inhabits`, `consists of`, `comprises`, `lies`, `sits`, `stands` (position-naming), and disallowed `holds` uses.

Verdict: `RULESET-CLEAN` or `RULESET-FAIL`.

### S4 — Continuity (auditor)

Four sweeps at season scope:
- **Reachability:** season-start state → season-end state per `season-plan.md` season chunk; surviving aggregate must traverse the delta.
- **State:** every prop and actor across the season. Props introduced are consumed/released or persist coherently. Actor entries and exits coherent.
- **Reference:** every slug resolves; no orphan introductions.
- **POV:** narrator transitions inside the aggregate are honest — narrator-switch position is reachable from prior bones. Inline `# pov:` comment at the switch line is required.

Verdict: `SEASON-CONTINUITY-OK` or `SEASON-CONTINUITY-FAIL`. Reachability faults route as `escalate`.

### S5 — Voice register coherence (dramatist, second invocation)

Each actor's voice register stays consistent across the aggregate per their behavior card. Verbs an actor takes match the actor's voice signature; out-of-register acts flagged; no drift between an actor's first-stretch voice and last-stretch voice (modulo arc-driven change).

Verdict: `VOICE-COHERENT` or `VOICE-DRIFT`.

### S6 — Vibe and theme alignment (audience ×3, second invocation)

Read aggregate as a tonal arc. Each stretch's beats honor active vibe-cloud; series.theme propagates into stretch-level beats; tonal register consistent.

**Per-window vibe verdict (MANDATORY):** per ~10-line window: `VIBE-ALIGNED` or `VIBE-DRIFT-{reason}`.

≥2-persona threshold for accepting drift flags. Bias: when in doubt, flag drift.

### S7 — Facet-readiness (auditor, dedicated)

For each load-bearing beat, verify a citable bone exists for each facet author downstream (location-state, state-updates, tensometer, dialogue, narrator-interest, etc.). Flag over-dense stretches (10+ beats per scene without inflection) and under-dense stretches (a chunk-implied beat with zero supporting bones).

Verdict: `FACET-READY` or `FACET-GAPS`.

### S8 — Plausibility (dramatist + auditor hybrid)

- **S8a — Character-action plausibility (dramatist).** For every named-actor action, ask: would this character actually *do* that, given their behavior card, persona card, vibes, and prior-stretch actions?
- **S8b — Event-in-world plausibility (auditor).** For every beat: plausible in-world given active condition cards, series laws, lore?

Per-beat: `PLAUSIBLE` / `IMPLAUSIBLE-CHARACTER-{slug}` / `IMPLAUSIBLE-EVENT-{condition-or-law}`. File-level: `PLAUSIBLE` or `IMPLAUSIBLE`. Structural implausibility routes as `escalate`.

### S9 — Comprehensibility (audience ×3, third invocation)

Per-beat:
- If the beat were missed by the reader, would the rest cohere? A beat whose absence breaks comprehension is **load-bearing** — flag for emphasis, parallel anchoring, or relocation.
- Is the cause-effect chain to the next beat legible without exposition? If reader-comprehension requires interiority, narrator-summary, or off-stage knowledge, the chain is **fragile**.
- Does the proto-line carry enough information for a reader to know *what happened* and *who did what to whom*? Ambiguous slugs, under-specified verbs, pronoun-equivalent referents flagged.

Per-window entertainment check (~10 lines): `ENGAGED` / `TOLERATED` / `BORED`. Two consecutive BORED OR three consecutive TOLERATED OR ≥30% of any 100-line stretch BORED-or-TOLERATED → file-level `COMPREHENSIBILITY-RISK-attention-{detail}`.

File-level: `COMPREHENSIBLE` or `COMPREHENSIBILITY-RISK-{reason}`.

### Convergence

Phase 3 converges when **all nine passes return clean verdicts in a single end-to-end run**. A change at any pass invalidates downstream passes; downstream re-runs from the changed point. Cap: **3 full season-scope iterations.** Worst-case combined Phase 2 + Phase 3 budget: 6 iterations.

---

## Phase 4 — Interpretive split

### Step 1 — Dramatist proposes splits

Inputs: converged aggregate, season-plan.md (context, not cut-points), series-plan.md, behavior cards for active cast.

Criteria:
- **(a) Ideal episode size.** Default target band: each episode 80–160 proto-lines. All proposed episodes within the band; no single episode exceeds 2× lower bound or falls below half it.
- **(b) Dramatic shape.** Each cut closes on a beat that earns its own next-open. An episode close on a flat beat is a fault. Adjacent episodes' shape arcs compose into the season's overall rise-peak-fall.
- **Hard constraint:** episode count multiple of 3 (3, 6, 9, 12...). Dramatist selects from multiples-of-3 set best fitting bone density and dramatic shape. No multiple-of-3 count fits → `SPLIT-INFEASIBLE` and escalate to user.
- **POV honor.** No cut bisects a POV-coherent stretch (identified by inline `# pov:` comments). Interlude stretches wholly contained within a single episode.

### Step 2 — Audience review of the split

Per-episode verdicts:
- **OPEN-ENGAGES** — open of episode hooks; reader would read on.
- **CLOSE-EARNS-NEXT** — close lands on a beat that earns the next episode's open.
- **SHAPE-COHERENT** — episode's interior arc (rise / peak / fall scaled to episode size) reads as one unit, not a slice.

File-level per persona: `SPLIT-ACCEPT` or `SPLIT-REVISE-{reason}`. ≥2-persona threshold for ACCEPT.

If REVISE → dramatist receives feedback and produces revised split (still constrained to multiple-of-3); review re-runs. Cap: 3 split iterations.

### Step 3 — Mechanical write-out

Header (seven required fields, in order):
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

Validation:
- Each per-episode file has all seven header fields.
- Body renumbered 1..M starting at 1 per episode.
- `cast` matches slug-grep over episode bones.
- `aggregate_range` contiguous and non-overlapping with sibling ranges; union of all ranges equals 1..N (accounting for legal ID-deletion gaps).
- Body comment-clean per proto-line schema (POV markers excepted).

---

## What this rubric does NOT formalize (explicit gaps)

These are gaps the audience and auditor are likely to press in tuning-r1:

- **No quantified definition of "stretch peak"** at season scope. S2 names `rise-peak-fall` and `cross-stretch flatlines` but does not give a mechanic for identifying a peak. A reviewer must judge.
- **No quantified definition of "buildup" and "denouement" share** of the aggregate. "Back half of the aggregate" is the only cited threshold for climax position; nothing names what fraction of the aggregate buildup vs denouement should occupy.
- **No quantified entertainment-density threshold** beyond "at most ~10% of windows TOLERATED, zero BORED" for S3 and "≥30% of any 100-line stretch BORED-or-TOLERATED" for S9. The two thresholds don't agree — S3 is stricter than S9.
- **No defined "episode-shape" mechanic** for Phase 4 Step 2's `SHAPE-COHERENT` verdict. "Rise / peak / fall scaled to episode size" is the only guidance.
- **No defined "open hooks" or "close earns next" mechanic** beyond their plain-English names. Phase 4 Step 2 verdicts depend on judgment.
- **No defined "POV-coherent stretch boundary"** mechanic for Phase 4 cuts. The rule is "no cut bisects" but the inline `# pov:` markers only mark transitions, not the full stretch range — a cut in the middle of a POV stretch is forbidden but the stretch's exact start/end is not formalized.
- **No defined adversarial criteria** for the three audience personas at season scope. Per-episode and per-line review have established adversarial habits; season-scope adversarial criteria are not separately documented.
- **No defined "cross-episode continuity" check** for the post-split per-episode files. S4 covers within-aggregate continuity; nothing checks the split's effect on continuity across episode boundaries.

The above list is the surface area Phase B will press the audience to attack and Phase G will scan mechanically.
