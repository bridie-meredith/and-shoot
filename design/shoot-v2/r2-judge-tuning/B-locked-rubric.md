---
phase: B — locked R2 rubric
project: R2 hybrid judge tuning
date: 2026-05-10
status: LOCKED — do not soften before Phase F audience verdict on a re-run corpus
parent: design/shoot-v2/r2-judge-tuning/A-corpus.md
---

# Phase B — Locked R2 Rubric

This is the discipline R2 (the graph-aware hybrid judge) must honor at every layer (R2.1–R2.4 in `and-facets-r2.md`), regardless of which facet is being judged. It sits **on top of** each facet's content rubric — R2 inherits the facet rubric for content, applies these gates for judge-mode discipline.

The four gates correspond to the four failure modes in Phase A.

## Gate G1 — Form re-test on REVISE outcomes

**Rule:** every R2 revision (whether REVISE-from-DELETE-candidate or REVISE-of-existing-KEEP-with-issue) receives a **mandatory blind §Form + Q1 + Q2 re-test** before round close. The re-test is performed against the entry **as if encountering it fresh**, not against the seam the revision was authored to answer.

**What §Form + Q1 + Q2 means per facet:**
- Each facet rubric has a §Form section (anti-patterns, forbidden vocabulary, voice/register fences). For facets without an explicit §Form section, the equivalent is the rubric's anti-pattern list (e.g., AP1–AP17 across facets).
- Q1 is each rubric's primary affirmative gate (e.g., somatic-tell-card-match for feeling; monument-grade callback for memory; perceptual-access for narrator-interest).
- Q2 is each rubric's secondary affirmative gate (e.g., multi-justification ≥3 of 5 for feeling; NI-spine co-citation for memory; spotlight-density for narrator-interest).

**Why:** F-R2-1. Single confirmed regression (feel:10 Phase-E.c) is structural — every R2 revision is exposed without this gate.

**Mechanic:** R2 author logs each revision with three lines: `§Form: PASS/FAIL <reason>`, `Q1: PASS/FAIL <reason>`, `Q2: PASS/FAIL <reason>`. A FAIL on any of the three is a revision-failure; the entry is logged for cap-refusal and the original (pre-revision) state is preserved as DELETE if the original was a DELETE candidate, or KEEP-WITH-CAVEAT if original was KEEP.

**Severity classification:** HARD on §Form. SIGNAL on Q1/Q2 (downstream audience adjudication is the final gate).

## Gate G2 — Multi-justification at-rest test on ADD outcomes

**Rule:** every R2-add must pass its facet's multi-justification gate **using only entry-at-rest evidence** (the proto-line at the anchor point + cards + persona stack). Graph evidence (other facets co-cited, the next-or-prior proto-line's content) is **not admissible** as multi-justification evidence at R2-add time.

**Why:** F-R2-2. 7+ confirmed instances across memory + feeling. Graph evidence is what *enables* the add (R2 sees the niche); it cannot also *justify* the add (that's circular).

**Mechanic:** R2 author logs each add with the multi-justification ladder. Each justification slot must cite a source: PROTO-LINE-AT-ANCHOR / CARD-§ / PERSONA-STM / VIBE-CLOUD / TENS-RATING-AT-ANCHOR. Sources from OTHER-PROTO-LINES (next, prior, other-character POV) are **disallowed** — if those are the only sources available, the add is refused under cap.

**Severity:** HARD. Refused adds are logged for next-round consideration.

**Per-facet note:**
- For facets without an explicit multi-justification ladder (location-state, sensory, state-updates, vibes-updates), G2 reduces to: "the add must be authored against at-rest evidence only; graph-revealed niche enables but does not justify."

## Gate G3 — Lonely-entry isolation re-read

**Rule:** for any R2 outcome (KEEP, REVISE, ADD) on a **lonely entry** (no other facets co-cited at the same proto-line per cite-index), the entry is re-read **in isolation from adjacent proto-lines** before the decision finalizes. Specifically: read only the anchor proto-line + the entry itself; do not read the proto-line immediately before or after.

**Why:** F-R2-3. Lonely-entry Q2 justifications systematically lean on adjacent context.

**Mechanic:** R2 author logs lonely-entry decisions with an `at-rest-isolation: PASS/FAIL` line. FAIL means the decision changed when adjacent context was masked; the at-rest verdict is authoritative.

**Severity:** HARD on FAIL. Decision flips: KEEP→DELETE, REVISE→DELETE-with-original-preserved, ADD→refused-under-cap.

**Co-located entry exception:** entries with ≥1 co-cited facet at the anchor proto-line are exempt — co-location is the rubric's evidence that the beat is structurally load-bearing, and adjacent-context discipline is the cite-index's job, not R2's.

## Gate G4 — Cross-character + within-character pattern check

**Rule:** at the close of each R2 layer (per-facet), R2 author runs a **structural-pattern scan** across all post-decision entries within that facet:

- **Cross-character same-strategy:** ≥2 characters using the same somatic-tell category / metaphor monument-load / etc. on the same scene-window. Flagged as SIGNAL; HARD if ≥3 characters.
- **Within-character formula-repetition:** ≥2 entries from the same character within ≤3 proto-lines using the same construction template (e.g. "the body Xes the Y" twice). Flagged as SIGNAL; HARD if ≥3.
- **Cross-character vocabulary saturation:** ≥3 instances of the same low-frequency content word (e.g. "weight", "press", "hold") across characters within a scene-window. Flagged as SIGNAL.
- **Cross-character temporal-anchor formula:** ≥2 characters using the same temporal-anchor construction ("not yet", "still", "already") at scene boundaries. Flagged as SIGNAL.

**Why:** F-R2-4. Pattern blindness is structurally invisible to per-character impersonator forks; the per-facet R2 layer is the natural place to catch it because R2 holds the full facet-graph.

**Mechanic:** R2 author appends a `## Pattern Scan` section to the facet file's R2 decision log. SIGNAL findings are logged; HARD findings trigger a revision pass on the offending entries (back through G1).

**Severity:** SIGNAL by default; HARD at the named threshold counts.

## Cross-cutting rules

### Decision-log discipline

Each R2 layer produces a structured decision log appended to the facet file's frontmatter or a sibling `.r2-log.md`:

```
## R2 Decision Log
- <facet>:<id> @<proto-line>: KEEP — <reason>
- <facet>:<id> @<proto-line>: DELETE — <reason> | cascade-strips: <count>
- <facet>:<id> @<proto-line>: REVISE — <seam> | §Form: PASS | Q1: PASS | Q2: PASS
- <facet>:<id> @<proto-line>: ADD — multi-justification: [<source>, <source>, <source>] | at-rest-isolation: PASS

## Pattern Scan
- Cross-character same-strategy: <count> SIGNAL, <count> HARD
- Within-character formula-repetition: <count> SIGNAL, <count> HARD
- Cross-character vocabulary saturation: <count> SIGNAL
- Cross-character temporal-anchor formula: <count> SIGNAL

## Cap Refusals
- <facet>:<id-candidate>: <reason> (G1 §Form FAIL / G2 graph-only-evidence / G3 isolation FAIL / over-cap)
```

### Severity ordering

When two gates produce conflicting verdicts on the same entry:
1. G3 isolation FAIL is authoritative on lonely entries (overrides any KEEP).
2. G1 §Form FAIL is authoritative on revisions (overrides Q1/Q2 PASS).
3. G2 graph-only-evidence is authoritative on adds (overrides "the niche is real").
4. G4 HARD on within-character formula-repetition triggers G1 on the offending entries.

### What this rubric does NOT do

- Does not gate **content** decisions — R2 still inherits each facet's rubric for what the entry should look like.
- Does not change the add-cap (≤5 per facet, ≤3 metaphor, ≤5/character feeling).
- Does not change self-scoped deletion authority — R2 still cannot delete other facets' entries.
- Does not change the layer order (R2.1 NI → R2.2 memory → R2.3 feeling → R2.4 metaphor).
- Does not introduce a new agent class — the four R2 layer impersonators/editor are the same; they receive the locked rubric as additional discipline in their dispatch payload.

## Locking discipline

This rubric is **locked** as of 2026-05-10. Per Phase 1 of the facet-tuning template:

> Once V2 is set, do not soften it for later rounds. Lift numbers are only honest under fixed rubrics.

Revisions allowed only at Phase F (validation re-run audience verdict), and only with audience-confirmed evidence the gate is over-strict (analogous to "defending the floor" in the standard process). The four gates may have **threshold** recalibration but not **structural** removal.

## Phase C entry point

Phase C — Tightened audience attack — runs the existing s01e01 R2 outputs (memory + feeling done; the other 8 facets ran R2 against an untuned prompt and their outputs are in `active-project/theater/facets/`) through audience adjudication using **G1–G4 as the lens**, not the per-facet content rubric.

Audience question per entry: did this R2 decision honor G1 (form re-test on revisions), G2 (at-rest evidence on adds), G3 (lonely-entry isolation), G4 (pattern scan)? Per-persona verdicts, aggregated.

Output: `C-tightened-attack.md`. Estimated dispatch budget: ~6 (3 audience personas × 2 sweeps — full facet graph in 1 pass + targeted seam-pressure in 2nd pass).

That session is the natural next step.
