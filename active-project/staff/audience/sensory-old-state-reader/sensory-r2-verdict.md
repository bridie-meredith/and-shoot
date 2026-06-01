---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01-c09
date: 2026-06-01
verdict: accept
---

# Sensory Old-State Reader — Cycle 2 Verdict

## Re-verify scope

Cycle-1 issued REVISE on two HARD findings (old-state lineage absent) and one SOFT flag (informal lineage). Fixer remedy was upstream-edit-first: add sensory-baseline fields to the loc-state facet at the prescribed entries. This pass re-reads the updated loc-state against the sensory file's old-state fields only. I do not relitigate disambiguation, modality, magnitude, or audience-side perceptibility — those axes were accepted by other cycle-1 specialists and are outside my scope.

No exemplar loaded. Baseline card behavior only.

---

## Per-finding re-walk

### [sensory:1] @8 — thermal old-state "stone-lane-late-morning-warmth"

**Cycle-1 finding:** HARD — unanchored old-state. No loc-state thermal field in any scene-A entry. No prior sensory-thermal entry in b01c09.

**Fixer addition:** loc-state:1 @1 now carries `sensory-baseline: stone-lane retained late-morning warmth (thermal; scene-A baseline — anchors sensory:1 @8 old-state)`.

**Lineage re-walk:**

loc-state:1 @1 is the first scene-A entry (oc-hook-precinct | late-morning). It precedes @8. The named baseline — "stone-lane retained late-morning warmth" — is verbatim-equivalent to the sensory old-state "stone-lane-late-morning-warmth." Modality match: thermal. No subsequent scene-A loc-state entry contradicts or overwrites the thermal baseline before @8. The inheritance direction is structurally sound: Taylor is in the hook-precinct lane area during scene-A (late morning, warm stone ambient), then crosses into the Dragonpit-margin lane at @8 (evening, hill-lane cool). The old-state describes where she was; the new-state describes where she arrives.

Rubric Axis 1 ACCEPT signature 3: "Anchored to a real perceptual baseline — the old-state matches the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality." Both the modality and the named baseline now trace to a specific, prior loc-state entry. The lineage is clean.

**Finding status: CLOSED.**

---

### [sensory:3] @11 — light old-state "lane-ambient-empty-distribution"

**Cycle-1 finding:** HARD — unanchored old-state. No loc-state light/visual field in scene-B prior to @11. No prior sensory-light entry in b01c09. SEAM-012 in the sensory file flagged this explicitly.

**Fixer addition:** loc-state:3 @8 now carries `sensory-baseline: evening ambient lane visual distribution, no non-baseline body present (light/visual; scene-B baseline — anchors sensory:3 @11 old-state)`.

**Lineage re-walk:**

loc-state:3 @8 is the scene-B entry beat (oc-dragonpit-margin | evening). It fires at @8, before @11. The named baseline — "evening ambient lane visual distribution, no non-baseline body present" — is semantically exact to the old-state "lane-ambient-empty-distribution." Modality match: light/visual. The inheritance direction is correct: the scene-B visual baseline at @8 is empty distribution (no body-form in the feed's lane return); at @11 the spike fires as Corwick resolves into that field.

No loc-state entry between @8 and @11 contradicts the baseline. loc-state:4 @11 (courier-at-stone-post) names the new condition — Corwick's presence — which is the sensory entry's new-state, not its old-state. The gap the cycle-1 attack named — "no loc-state entry at or before this anchor establishing a baseline" — is now filled. loc-state:3 @8 is that entry.

Rubric Axis 1 ACCEPT signature 3: the old-state now resolves to a named loc-state sensory field at a prior beat, same location, correct modality.

**Finding status: CLOSED.**

---

### [sensory:2] @23 — tactile old-state "wax-soft-warm"

**Cycle-1 finding:** SOFT FLAG — physically entailed by @19 bone action, not fictive, but lacked formal loc-state lineage. Rubric enumerates two permitted sources (loc-state sensory field; prior sensory entry on same modality); physical-entailment is not enumerated. Not a blocking finding; recommended formal remedy.

**Fixer addition:** loc-state:5 @17 now carries `tactile-prop-baseline: sealing-wax at station is pliable-warm pre-application (anchors sensory:2 @23 old-state)`.

**Lineage re-walk:**

loc-state:5 @17 is the feed-station entry, prior to @23. The named baseline — "sealing-wax at station is pliable-warm pre-application" — is verbatim-equivalent to the old-state "wax-soft-warm." Modality match: tactile (prop-level). No entry between @17 and @23 contradicts or modifies the wax-state. The derivation the author intended — wax is necessarily soft-warm at application — is now formally recorded in the upstream loc-state entry.

The cycle-1 concern was not that the old-state was fictive (it was physically grounded) but that it lacked the formal loc-state field the rubric requires. That field now exists.

**Finding status: CLOSED (from SOFT to clean).**

---

## Cross-facet silent-gap check

The fixer additions to loc-state name discrete sensory conditions (thermal baseline, visual distribution, tactile-prop state). I check whether these additions create a cross-facet silent-gap obligation: per the rubric's "Cross-facet modality silent-gap" clause, a loc-state sensory note that names a discrete perceptual event must be accompanied by a sensory-flag at the same anchor OR the loc-state author must downgrade the note to non-event ambient language.

The three additions are baseline notes, not event notes — they describe persistent conditions (retained warmth, ambient distribution, pliable-warm wax), not change-events. None of the three additions asserts that a modality changed at the anchor beat; they establish the prior state that sensory fires downstream are measured against. The rubric's silent-gap clause targets event-naming (a discrete change at the anchor), not baseline-establishing. No new silent-gap obligations arise.

---

## Summary

| finding | cycle-1 severity | cycle-1 status | fixer addition | cycle-2 status |
|---------|-----------------|----------------|----------------|----------------|
| sensory:1 @8 thermal old-state | HARD | open | loc-state:1 @1 thermal baseline added | CLOSED |
| sensory:3 @11 light old-state | HARD | open | loc-state:3 @8 visual baseline added | CLOSED |
| sensory:2 @23 tactile old-state | SOFT | open | loc-state:5 @17 tactile-prop baseline added | CLOSED |

All three findings resolve. No new old-state lineage findings introduced. The sensory file's content is unchanged and was already accepted on all other axes by other cycle-1 specialists. The cross-facet contract (loc-state → sensory old-state anchor) now holds for all three fires.

---

## Verdict

**ACCEPT**

Both HARD findings from cycle-1 close on the fixer's loc-state additions. The SOFT flag closes as well. No new objections within my mandate (old-state lineage only).
