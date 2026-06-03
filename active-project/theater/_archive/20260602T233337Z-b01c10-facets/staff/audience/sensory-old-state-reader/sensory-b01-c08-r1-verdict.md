persona: sensory-old-state-reader
facet: sensory
episode: b01c08
cycle: r1
verdict: revise
auditor-report: absent at dispatch (not yet authored)
exemplar: absent (no library or project-bound exemplar found; card-only baseline)
updated: 2026-05-31 — loc-state for b01c08 now present; prior conditional-pass verdicts re-evaluated against locked loc-state text
---

# Per-entry adversarial reading

## [sensory:1] @10 sound: feed-station-working-quiet -> wax-seal-crack

**Lineage walk — against now-present loc-state.**

Most recent loc-state entry prior to @10: loc-state:4 `@9 the-feed-station | afternoon | none | packet on intake surface`.

loc-state:4 is temporally correct and spatially present (one bone before the sensory fire, same location). The prior r1 verdict was conditional-pass pending loc-state annotation. Loc-state has now been authored. The condition has resolved.

loc-state:4 text: `the-feed-station | afternoon | none | packet on intake surface`. No sensory note. No acoustic annotation. The acoustic baseline "feed-station-working-quiet" is not in this entry's text, is not in any prior loc-state entry for the feed-station, and is not traceable to any field in the locked loc-state file.

**Attack.**

The SEAM-010 carve-out claimed loc-state was absent at sensory-R1 authoring time and invoked clause (a): series-established indoor-administrative-quiet vocabulary, corroborated by s01e01:41. That carve-out was procedurally warranted when loc-state was absent. Loc-state is now present. The carve-out's own terms govern resolution: "If loc-state contradicts either old-state, this sensory entry must be revised or deleted." It also stated: "Loc-state-side anchor expected when loc-state for b01c08 is authored."

loc-state:4 neither confirms nor contradicts "feed-station-working-quiet." But the carve-out set up a binary: ratify or correct. loc-state:4 does neither. It is acoustically silent. The loc-state author wrote the feed-station entry without supplying the expected sound annotation.

This is not a contradiction — it is an annotation gap that leaves the old-state unanchored. Under the rubric's lineage rule (Axis 1: "Anchored to a real perceptual baseline. The old-state matches the most recent location-state file's § sensory or § conditions field"), the old-state must now be HARD UNANCHORED — loc-state exists, governs the beat, and carries no text supporting "feed-station-working-quiet."

The calibration anchor (s01e01:41 — yard-quiet → wax-crack) is an analogy, not a b01c08 graph anchor. The series-class inference ("indoor-administrative-quiet") is reasonable but not a locked-graph fact for this chapter.

**Verdict on sensory:1: FAIL — UNANCHORED-OLD-STATE.** loc-state:4 @9 governs the beat; it carries no acoustic note. "Feed-station-working-quiet" is not recoverable from the locked loc-state. Fix path: add sound annotation to loc-state:4 (e.g., `sensory: enclosed-receipt-quiet`), then revise sensory:1's old-state to match. If loc-state is closed without that annotation, sensory:1 must be deleted.

---

## [sensory:2] @16 light: afternoon-stone-lane-light -> evening-lane-dusk-fall

**Lineage walk — against now-present loc-state.**

Prior loc-state entries for the hook-ward before @16:
- loc-state:2 `@3 the-hook-ward | afternoon | none | water-point occupied`
- loc-state:3 `@4 the-hook-ward | afternoon | none | lane-mouth watched`

Both confirm afternoon time-of-day. Neither carries a light-quality annotation.

loc-state entry at @16:
- loc-state:5 `@16 the-hook-ward | evening | none | water-point lit low, chandler-corner-adjacent`

This is the inflection anchor itself — loc-state:5 records the evening register established at the same beat. The new-state "evening-lane-dusk-fall" maps coherently to loc-state:5 ("evening," "water-point lit low").

**Attack — two vectors.**

**Vector A: old-state name traceability.**

"Afternoon-stone-lane-light" has two components: (1) "afternoon" — directly confirmed by loc-state:2/@3 and loc-state:3/@4 for the hook-ward; (2) "stone-lane-light" — a light-quality descriptor not present in any loc-state text. loc-state:2 and :3 record afternoon time-of-day and positional conditions but carry no light annotations.

The "stone-lane" descriptor is an extrapolation from the location type. The hook-ward is a stone lane ward — established from series geography, not from loc-state text within b01c08. This is a weaker class of extrapolation than sensory:1: the time-of-day component is locked-graph confirmed; the light-quality naming adds one descriptor beyond what the text provides.

The prior verdict held this as conditional-pass pending an afternoon light-quality annotation. No such annotation was added to loc-state:1, :2, or :3 in the now-authored loc-state file.

**Vector B: delta direction and new-state.**

The delta direction (afternoon → evening) is unambiguously ratified. loc-state:5 @16 records "evening" as the ward's time-register at exactly the sensory fire's anchor. The new-state "evening-lane-dusk-fall" is consistent with loc-state:5 ("evening," "lit low"). The inflection is real, the direction is correct, and the new-state is confirmable.

**Resolution.**

Unlike sensory:1, the old-state here has a traceable backbone: "afternoon" is a locked-graph fact for the hook-ward confirmed by two loc-state entries. The "stone-lane-light" descriptor extrapolates location type, but the location is documented in the bones file and scene-map (hook-ward, stone-lane-ward geography). This is analogical extrapolation from confirmed geography, not pure invention.

The rubric's lineage test asks: does the old-state match "the most recent location-state file's § sensory or § conditions field"? loc-state:2 and :3 do not name "stone-lane-light" in any field. Strict lineage test: FAILS. But the afternoon temporal component IS in loc-state text; the extrapolation is constrained (location type → light quality), not free-floating.

**Verdict on sensory:2: SOFT FLAG — thin lineage, delta coherent.** The delta direction and new-state are fully anchored. The old-state has a partial anchor (afternoon confirmed; stone-lane-light is extrapolation). Under strict rubric lineage testing this is a SOFT finding, not a HARD FAIL — the extrapolation is constrained and not contradicted. Recommended fix: add a light-quality annotation to at least one afternoon hook-ward loc-state entry (loc-state:2 or :3) naming the afternoon-stone-lane palette. If that annotation is added, sensory:2's lineage closes cleanly. If not added and file is closed, sensory:2 carries a weak-but-not-broken old-state — flagged but not requiring deletion.

---

# Aggregated verdict

**verdict: revise**

**sensory:1: FAIL — UNANCHORED-OLD-STATE (HARD).** loc-state:4 @9 governs the beat and is acoustically silent. "Feed-station-working-quiet" is not traceable to any locked-graph text. The SEAM-010 carve-out's own resolution condition — "loc-state-side anchor expected when loc-state for b01c08 is authored" — resolved negatively: loc-state was authored without the required annotation. This entry cannot pass at current state. Fix-or-delete required before cycle 2 accept.

**sensory:2: SOFT FLAG — thin but defensible lineage.** "Afternoon" is confirmed by loc-state:2/@3 and :3/@4. "Stone-lane-light" is extrapolation from confirmed location type. Delta direction and new-state are fully ratified by loc-state:5. Not a HARD failure; recommended loc-state annotation would close it cleanly. Does not independently block acceptance.

**Blocking finding:** sensory:1 HARD UNANCHORED-OLD-STATE drives the revise verdict. The facet cannot pass while sensory:1's old-state has no locked-graph anchor.

**Required fix path:**
1. Studio adds sound annotation to loc-state:4 @9 (the-feed-station entry) naming the baseline acoustic register. Suggested: `sensory: enclosed-receipt-quiet` or equivalent indoor-administrative-quiet vocabulary.
2. sensory:1 old-state revised to trace to that annotation (near-verbatim or verbatim match).
3. sensory:2 optional improvement: add light-quality note to loc-state:2 or :3 (hook-ward afternoon entries). Not blocking, but recommended for cycle-2 clean pass.

**Convergence trace:** Auditor report absent at dispatch; no auditor finding IDs to cross-cite. The UNANCHORED-OLD-STATE finding on sensory:1 maps to rubric Axis 1 REJECT signature "Unanchored old-state (HARD)" and was first surfaced as CONDITIONAL in the prior r1 dispatch; the loc-state authoring event resolved the condition negatively, promoting this to HARD.
