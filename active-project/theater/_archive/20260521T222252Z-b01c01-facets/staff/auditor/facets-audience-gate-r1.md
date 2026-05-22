---
report: facets-audience-gate
episode: b01c01
cycle: 1
date: 2026-05-19
phase: 5b
aggregation_rule: URI-AUDIENCE-AGGREGATION-RULE (3-of-3 ACCEPT required; single dissent fails)
membership_source: active-project/staff/showrunner/memory.md (audience: cape-fic-reader, dark-fantasy-reader, worm-canon-pedant)
specialists_used: sensory only (sensory-modality-coverage, sensory-disambiguation-pedant, sensory-old-state-reader)
stale_verdicts_quarantined: active-project/staff/audience/_stale-pre-cycle1/ (literary-snob, pulp-enthusiast from prior audience config)
status: PARTIAL — 3 of 12 facets passed; 9 routed to fixer
next: cycle-2 remediation (fixer dispatch → re-fire Phase 5 → re-fire Phase 5b on failing facets only)
cap: 3 cycles
---

# Audience-gate report — cycle 1 — b01c01

## Per-facet aggregate

| Facet / Character           | cape-fic | dark-fantasy | worm-canon-pedant / specialists | Result |
|-----------------------------|----------|---------------|----------------------------------|--------|
| location-state              | accept   | revise        | revise                           | **FAIL** |
| interest-narrator           | revise   | revise        | accept                           | **FAIL** |
| sensory (specialists)       | n/a      | n/a           | mod-cov revise / disambig accept / old-state revise | **FAIL** |
| state-updates               | revise   | revise        | revise                           | **FAIL** |
| memory                      | revise   | revise        | revise                           | **FAIL** |
| feeling                     | accept   | revise        | revise                           | **FAIL** |
| metaphor                    | accept   | accept        | accept                           | **PASS** |
| vibes                       | accept   | accept        | accept                           | **PASS** (carry-forward items noted) |
| exposition                  | revise   | accept        | accept                           | **FAIL** (audience-side ADD proposed) |
| dialogue / coll             | revise   | accept        | revise                           | **FAIL** |
| dialogue / taylor           | accept   | accept        | accept                           | **PASS** (Stage 2 seams advisory) |
| dialogue / wren             | revise   | revise        | revise                           | **FAIL** |

**Aggregate:** 3 pass / 9 fail of 12 facets. Cycle-1 fails the Phase 5b gate.

## Convergence trace

- Auditor (Phase 5 mechanical) findings: 9 total (2 HARD remediated → 0 HARD post-r2-verify; 7 SIGNAL retained as cold-start overrides)
- Audience callouts (cycle 1, deduped across reviewers): ~16 distinct entry-level + 4 file-level structural
- **Shared findings (audience + auditor both flagged the same entry):**
    - sensory FREQUENCY-BAND breach @ 12.5% (auditor FB-002; sensory-modality-coverage as secondary attack alongside thermal silent-gap)
    - exposition FREQUENCY-BAND breach @ 16.7% (auditor flagged as cold-start-justified; audience accepted breach but cape-fic added a Hook gloss seam not directly overlapping)
    - vibes warehouse-card slug-chain note (auditor r2-verify NOTE-FOR-NEXT-RUN; worm-canon-pedant cycle-1 noted same vibes:17 slug mismatch)
- **Audience-only findings (the seams the mechanical scan structurally cannot see):**
    - location-state necessity-axis attack on loc-state:3 @11 (anchor-verb licensing — both dark-fantasy + worm-canon-pedant)
    - location-state Anti-pattern-3 (persistence-as-state) on loc-state:4 @13 (dark-fantasy)
    - interest-narrator AP-001 template fire pattern (narrator:2/4/6) — pattern-recognition both cape-fic + dark-fantasy
    - interest-narrator file-level doubled-register failure (Westerosi-monument register absent across 7 entries — dark-fantasy structural attack)
    - state-updates internal contradiction between discipline-hold and passive-acquisition entries (cape-fic); social-integration too fast (dark-fantasy); canon-mechanics ambiguity around "active-holding" and "auto-initiating" (worm-canon-pedant)
    - memory file-level single-register failure (both flags Earth-Bet displacement; zero Westerosi-monument clamp fires); peak-anchor placement of mem:1 @15 (quiet-beat instrument fired at climax); mem:2 @23 missing monument card / margit referral
    - feeling first-clause OK; second clause "the turn comes one beat late" exits body-register (dark-fantasy + worm-canon-pedant)
    - sensory thermal silent-gap at @13 + sound-dominance (modality-coverage); unanchored old-states sensory:1 @1 + sensory:2 @9 (old-state-reader)
    - exposition embedded-Hook unoriented in Wren gloss — ADD requested (cape-fic-reader)
    - dialogue-coll citation-completeness gap in sidecar (both cape-fic + worm-canon-pedant); anticipatory-object ascription on "Needle's been waiting" (cape-fic)
    - dialogue-wren feel-wren:@22 citation does not resolve (feel:2 is at @21) — 3-of-3 convergence; state-wren:@22 specificity gap (dark-fantasy + worm-canon-pedant)
- **Auditor-only findings (not surfaced by audience this cycle):** FREQUENCY-BAND signals on state-updates (high) and vibes (in-band) were not re-attacked by audience at this granularity; CONSTRAINT findings cleared at r2-verify all held.
- **Bidirectional loop verdict:** **validated** — multiple shared findings across the two paths (sensory density, exposition breach-high cold-start, vibes slug-chain note); audience surfaced significant additional surfaces the mechanical scan structurally cannot reach.

## Cycle-1 process notes

- All 12 reviewer-set dispatches completed; one-shot (no stalls, no payload trimming required).
- Stray verdict files from prior session attempts (when audience was literary-snob / pulp-enthusiast instead of the current trio) quarantined to `active-project/staff/audience/_stale-pre-cycle1/` to prevent off-canon aggregation contamination.
- Sensory specialists fired cleanly; the 3-specialist set is now load-bearing and replaces fallback for sensory.
- Vibes passed but with 3 carry-forward items flagged for next-run queue (slug-chain rename, schema edge on off-anchor entry header, stitcher-pass awareness for vibes:4 register).

## Routing — cycle 2 remediation

Per /and-facets command body lines 475-481:

1. **Aggregate revise/fail callouts across all reviewers** — captured above per facet.
2. **Dispatch fixer** with consolidated callouts + facet rubrics. Per-facet routing:
    - **location-state**: fixer can strip loc-state:3 (necessity-axis fail) and re-evaluate loc-state:4 (persistence-as-state) — small edits to studio's facet file.
    - **interest-narrator**: AP-001 template recurrence requires re-author of narrator:2/4/6; dispatching impersonator (taylor) in narrator-judge mode is the cleaner route. File-level displaced-child fire at Wren-adjacency requires ADD (impersonator) at @20-@24.
    - **sensory**: thermal silent-gap @13 requires sensory ADD by studio (cross-author). Unanchored old-states require sensory-note additions to loc-state:1 (cross-facet — studio).
    - **state-updates**: 3-of-3 dissent on multiple entries — entries 10/11/12/13/15/17 require re-evaluation. This is a facet-author re-author, not a fixer micro-edit. Dispatching impersonators (per-character) in state-judge mode.
    - **memory**: single-register file-level shape failure requires ADD of Westerosi-monument fires; mem:1 @15 needs relocation to quiet-beat slot (@16-@17); mem:2 @23 needs monument card via margit referral. Impersonator-taylor in memory-judge mode + margit referral.
    - **feeling**: feel:1 @23 second clause cut — fixer micro-edit.
    - **exposition**: cape-fic Hook ADD — exposition-author runs in audience-side-ADD mode.
    - **dialogue-coll**: citation-completeness gap in sidecar — fixer documents the R2 facet-license resolution; "Needle's been waiting" anticipatory-object ascription — dialogue-writer defense-or-revise mode.
    - **dialogue-wren**: feel-wren citation mismatch — either sidecar correction or R2 ADD of feeling entry at @22; state-wren:@22 specificity requires re-evaluation.
3. **Re-fire Phase 5** (full mechanical scan) after fixer changes land.
4. **Re-fire Phase 5b** on the 9 failing facets only; passes (metaphor, vibes, dialogue-taylor) do not re-fire.
5. **Increment cycle counter to 2.**

Cycle cap: 3.

## RUBRIC-FIDELITY promotion candidates (per CLAUDE.md rule 11)

Patterns surfaced at this audience-gate that could graduate into the relevant facet rubric's REJECT / anti-pattern / cross-facet contract section:

- `rubric-location-state.md` § necessity-axis: anchor-verb-licensing check (dexterity-stillness verbs do not license a loc-state fire unless first-beat-in-new-location or with `continuity-from` token).
- `rubric-narrator-interest.md`: AP-001 "X is what Y" inverted-predicate template — frequency cap or REJECT after N fires in-file.
- `rubric-narrator-interest.md`: file-level doubled-register check (both Earth-Bet shadow AND Westerosi-monument fires required when both registers are bone-supported).
- `rubric-memory-flags.md`: file-level doubled-register check (analogous) + peak-anchor refusal (memory fires are quiet-beat instruments; default-refuse on peak bones).
- `rubric-memory-flags.md`: target-reference must resolve to a monument card via margit referral; bare gloss text is SIGNAL-class.
- `rubric-feeling.md`: one-clause form discipline; compound somatic-tells that exit body-register fail.
- `rubric-sensory.md`: modality silent-gap check (if loc-state names a thermal/sonic/olfactory event at a bone, sensory must fire that modality at or near the anchor or document the silence).
- `rubric-sensory.md`: old-state anchoring requirement (every old-state must resolve to a prior loc-state sensory baseline OR a prior sensory entry's new-state).
- `staff/exposition-author/rubric-exposition.md`: embedded-noun gloss-completeness (proper-noun frames inside a gloss must themselves be glossed or already in the cross-episode glossed-terms register).
- `staff/dialogue-writer/rubric-dialogue.md`: per-entry facet-license citation completeness (sidecar's R2 mandate is per-entry, not per-block).

These are taste-flag → RUBRIC-FIDELITY promotion candidates per the chain in CLAUDE.md rule 11. Whether to promote now (before cycle 2) or after cycle resolution is an orchestrator-critic decision.

## Per-reviewer verdict files (canonical citations)

### location-state
- active-project/staff/audience/cape-fic-reader/location-state-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/location-state-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/location-state-r1-verdict.md

### interest-narrator
- active-project/staff/audience/cape-fic-reader/interest-narrator-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/interest-narrator-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/interest-narrator-r1-verdict.md

### sensory (specialists)
- active-project/staff/audience/sensory-modality-coverage/sensory-r1-verdict.md
- active-project/staff/audience/sensory-disambiguation-pedant/sensory-r1-verdict.md
- active-project/staff/audience/sensory-old-state-reader/sensory-r1-verdict.md

### state-updates
- active-project/staff/audience/cape-fic-reader/state-updates-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/state-updates-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/state-updates-r1-verdict.md

### memory
- active-project/staff/audience/cape-fic-reader/memory-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/memory-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/memory-r1-verdict.md

### feeling
- active-project/staff/audience/cape-fic-reader/feeling-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/feeling-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/feeling-r1-verdict.md

### metaphor (PASS)
- active-project/staff/audience/cape-fic-reader/metaphor-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/metaphor-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/metaphor-r1-verdict.md

### vibes (PASS)
- active-project/staff/audience/cape-fic-reader/vibes-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/vibes-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/vibes-r1-verdict.md

### exposition
- active-project/staff/audience/cape-fic-reader/exposition-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/exposition-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/exposition-r1-verdict.md

### dialogue / coll-net-mender-flea-bottom
- active-project/staff/audience/cape-fic-reader/dialogue-coll-net-mender-flea-bottom-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/dialogue-coll-net-mender-flea-bottom-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/dialogue-coll-net-mender-flea-bottom-r1-verdict.md

### dialogue / taylor-hebert-kl-122ac (PASS)
- active-project/staff/audience/cape-fic-reader/dialogue-taylor-hebert-kl-122ac-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/dialogue-taylor-hebert-kl-122ac-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/dialogue-taylor-hebert-kl-122ac-r1-verdict.md

### dialogue / wren-stitch-maker-flea-bottom-ward
- active-project/staff/audience/cape-fic-reader/dialogue-wren-stitch-maker-flea-bottom-ward-r1-verdict.md
- active-project/staff/audience/dark-fantasy-reader/dialogue-wren-stitch-maker-flea-bottom-ward-r1-verdict.md
- active-project/staff/audience/worm-canon-pedant/dialogue-wren-stitch-maker-flea-bottom-ward-r1-verdict.md
