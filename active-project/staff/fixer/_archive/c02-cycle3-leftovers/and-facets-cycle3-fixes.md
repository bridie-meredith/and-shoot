# /and-facets b01c02 — Phase 5b cycle-3 fix log
date: 2026-05-22
session: facets-b01c02-cycle3-remediation
fixer: claude-sonnet-4-6
callouts-received: 2 (Callout A — interest-narrator narrator:6 AP-10; Callout B — sensory:2 anchor-invalid)

---

## Callout A — interest-narrator narrator:6 @28

disposition: FIXED-DIRECT

### What was wrong

narrator:6 @28 contained the text: "the hand stays where it is — the reach is cleared, the body could close it, and the not-closing is the only line tonight she is sure of."

The clause "the not-closing IS the only line" is an AP-10 inverted-predicate ("the X is the Y") at sentence-final position. narrator:2 @5 already consumed the single licensed AP-10 instance (cap ≤1); narrator:6 was the second instance, a cap violation per rubric §Anti-patterns 10.

### Fix applied

narrator:6 @28 recast to: "the hand stays where it is — the reach is cleared, the body could close it — and tonight she is certain only of the not-closing."

Content elements preserved:
- (a) physical observation: "the hand stays where it is" — unchanged
- (b) capability confirmation: "the reach is cleared, the body could close it" — unchanged
- (c) restraint-as-only-certainty: expressed as "she is certain only of the not-closing" — states the condition directly; terminates on the content noun "not-closing"; no X-into-Y collapse; no trailing elective preposition

AP-10 instance 2 eliminated. File-scope cap now 1 (narrator:2 only).

### Files touched

- active-project/theater/facets/interest-narrator.md — line 11, narrator:6 body recast

### Proto-line citation moved

No. narrator:6 token remains at @28.

---

## Callout B — sensory:2 anchor-invalid

disposition: DELETED-CYCLE-3-NO-ADD-BUDGET

### Proto-line walk — evaluation of non-sound non-fire candidates

Per the callout instructions, a genuine walk of b01c02 bones for non-sound sensory inflection beats before confirming deletion. Evaluation criteria: disambiguation gate pass (not action-verb self-charged), anchored old-state, real perceptible inflection beat (not settled-state), full rubric compliance.

The episode's only non-sound perceptual inflection is the dark-to-lit transition at @22 ("lights the lamp"). The structural problem is architectural: the inflection beat IS the self-charged verb. "Lights" names the light event. There is no proxy anchor before the inflection (pre-transition darkness is a sustained baseline, not an inflection beat) and no proxy anchor at the inflection itself that is not self-charged. Every bone after @22 is inside the settled lamp-lit state.

Other bone candidates surveyed:

- @19 ("wren speaks to taylor"): speech event, no perceptible non-sound modality inflection
- @20 ("taylor speaks to wren"): speech event, same
- @25 ("strikes the line"): physical manipulation, no temperature/smell/touch/light inflection; line-striking is not a sensory-modality event
- @26 ("underlines the entry"), @27 ("sets the pen"), @28 ("holds the hand"), @29 ("closes the ledger"): all inside the settled lamp-lit state; accounting gestures; no non-sound sensory inflection
- @6 ("wren enters the alley"): arrival event — possible visual but the visual delta (Wren's figure appearing at threshold) is already carried by loc-state:4 @6 as a location-state entry (sustained-state domain); no sensory-inflection not already owned by loc-state
- @1 through @5: alley exterior, morning; insect-mass deployment is a visual event but the rubric's action-verb self-charge test applies — "the insects fill the lane" / "the insects close the lane-mouths" are the inflection verbs; the same architectural trap applies (fill, close = action-verb self-charge on the visual inflection)

Conclusion: no genuine non-sound sensory inflection exists in b01c02 that satisfies the full rubric. Relocation is not viable. Per A3, no ADD budget remains. Deletion is the correct resolution.

### Deletion record

sensory:2 deleted. Canonical deletion marker written to sensory.md:

`# DELETED sensory:2 @23 - no valid anchor (inflection beat @22 is action-verb self-charge; post-beats settled-state); cycle-3 A3 no-ADD-budget (cap-burn cycle 3, 2026-05-22)`

### Files touched

- active-project/theater/facets/sensory.md — sensory:2 entry replaced by canonical deletion marker
- active-project/theater/proto-lines/b01-c02.md — `[sensory:2]` removed from @23 line
- active-project/theater/facets/_cite-index.md — sensory:2 row removed; deletion note added; state:5 @23 co-citations updated (sensory:2 stripped); exposition:5 @23 co-citations updated (sensory:2 stripped); totals updated (55 → 54 entries)

### Proto-line citation moved

No move — citation removed entirely. `[sensory:2]` was at @23; it is now absent.

### Cite-index changes

- `### sensory (2 entries)` → `### sensory (1 entry)`
- `sensory:2 @23 back=Y co=[exposition:5, state:5]` → deleted (deletion comment added)
- `state:5 @23 co=[exposition:5, sensory:2]` → `co=[exposition:5]`
- `exposition:5 @23 co=[sensory:2, state:5]` → `co=[state:5]`
- totals line: 55 → 54 facet entries

### Modality-floor trade-off — ACCEPTED AT CAP-BURN

The deletion leaves sensory.md with 1 entry on 1 modality (sound only: sensory:1 @7). The rubric modality floor is ≥2. This is a modality-floor breach.

This breach is an accepted cap-burn trade-off. The cycle-3 A3 constraint prohibits adding a new entry that fails pre-validation. No genuinely earned non-sound fire exists. Manufacturing a fire to hit the floor is explicitly prohibited by the callout and by rubric. The breach is documented and accepted; it is not chased with an ADD.

The sensory facet is in a cap-burn-bound state: it holds the correct terminal form (sound-only, sensory:2 deleted, modality-floor breach documented) and is ready for cap-burn resolution or acceptance as-is.

### loc-state:11 @22 conditions note

loc-state:11 @22 carries a conditions note added in cycle-2 as the old-state anchor for sensory:2: "interior-darkness baseline before @22 — lodging-interior unlit, night scene-open (time-skip blank @21); this is the unlit-lodging-interior old-state (anchor for sensory:2 old-state at @23)." With sensory:2 deleted, the back-reference to sensory:2 is unreferenced. Per callout instructions, the conditions note is left in place as harmless environmental context. It accurately describes the pre-lamp state of the lodging interior and may be useful to stitcher or reader as environmental grounding. No edit made.

---

## Summary

| Callout | Disposition | Files touched | Citation moved | Terminal state |
|---------|-------------|---------------|----------------|----------------|
| A — narrator:6 AP-10 | FIXED-DIRECT | interest-narrator.md | No | Clean pass-eligible |
| B — sensory:2 anchor | DELETED-CYCLE-3-NO-ADD-BUDGET | sensory.md, proto-lines/b01-c02.md, _cite-index.md | Removed (not moved) | Cap-burn-bound (modality-floor breach) |
