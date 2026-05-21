# and-facets b01c01 — cycle-3 fix report
date: 2026-05-20
cycle: 3 (last cycle before cap = 3)
fixer-session: facets-b01c01-cycle3

---

## Summary

Cycle-3 addresses 2 actionable facet failures from audience-gate cycle-2. Memory is explicitly skipped per cap-burn ruling.

---

## F-014: interest-narrator — NI-6 @27 rewrite

**Finding:** dark-fantasy-reader revise verdict; NI-6 @27 rendered the name-withholding rule as a policy declaration rather than as a gap-narration cost. Anti-pattern 9 (Mask-too-perfect): zero displacement-trigger fires across 6 entries in a chapter whose declared goal is the child the chapter will fail to protect.

**Minimum-change path identified by dark-fantasy-reader:** rewrite NI-6 @27 in-place toward gap-narration pattern; no new entry; no band-ceiling impact.

**Change applied:**

File: `active-project/theater/facets/interest-narrator.md`, entry 6 body.

Before: `she will not write the name above the block, not in the feed and not on the page she keeps for herself.`

After: `the threshold holds and what is on the other side stays the size she will not name.`

**Criteria check:**
- (a) Policy-declaration register eliminated: yes — "she will not write" replaced with "the threshold holds"; no rule stated
- (b) Displacement-trigger register through refusal-to-look channel: yes — "what is on the other side stays the size she will not name" renders the gap (the child's weight not-named under the Wren proximity trigger)
- (c) Cold-utilitarian Taylor voice: yes — declarative, no affect, pure observation of threshold-state
- (d) Band ceiling not breached: yes — still 6/27 = 22.2%; no entry added or removed

**Proto-lines impact:** none — [narrator:6] token at @27 unchanged; body edit, no cite cascade. _inflight-r2/proto-lines-narrator.md unchanged.

---

## F-015b: location-state — loc-state:1 light-level field

**Finding:** sensory-old-state-reader revise verdict; sensory:1 @3 old-state "corner-room-dim" has no explicit light-level field in loc-state:1; inference required two steps (geometry cue "door-shadow across the entry" → dim interior); flagged as moderate-revise.

**Change applied:**

File: `active-project/theater/facets/location-state.md`, entry 1 @1, field list extended.

Added: `light: threshold-dim, interior-corner dim under overcast morning backlight`

Full entry 1 now: `flea-bottom | morning | rain-recent | threshold-open | the door-shadow across the entry marks where the building-keeper stands | light: threshold-dim, interior-corner dim under overcast morning backlight`

**Criteria check:**
- Explicit light-level field present on loc-state:1: yes
- sensory:1 @3 "corner-room-dim" traces near-verbatim to declared light field: yes ("threshold-dim" / "interior-corner dim" directly supports "corner-room-dim")
- Lineage resolution: single-step (not two-step inference); rubric's old-state anchoring requirement met

**Proto-lines impact:** none — loc-state:1 was already cited at @1; field-add is internal to the entry; no cite token change.

---

## F-015a: sensory — sensory:3 sound entry at @17

**Finding:** sensory-modality-coverage fail; file is single-modality (light only after sensory:2 @16 deletion at cycle-2 F-009); ≥1 sound entry required; @15 ("the insects fill the block") or @17 ("the boots strike the cobbles") identified as clean anchors.

**Change applied:**

File: `active-project/theater/facets/sensory.md`, new entry.

Added: `3 @17 sound: street-quiet-of-mid-afternoon -> bootfall-on-cobbles-from-the-Hook-bend`

@17 chosen: proto-line "the boots strike the cobbles" is bare (no prior sensory citation; no cite conflict). Entry body is studio-voice, ≤1 line, no narrative or moralization.

ID: 3 (next-available; ID 2 gap preserved per F-009 cycle-2 deletion; no renumber per dispatch constraint).

**Proto-lines updated:**
- Canonical `active-project/theater/proto-lines/b01-c01.md` @17: added [sensory:3]
- Created `active-project/theater/facets/_inflight-r2/proto-lines-sensory.md` with [sensory:3] at @17 (new file; no prior sensory inflight annotated copy existed)

**Criteria check:**
- ≥1 sound entry present: yes (sensory:3 @17)
- Studio-voice: yes — field-transition format, no narrative
- ID 2 gap preserved: yes
- Canonical and inflight proto-lines updated: yes
- Modality floor met: yes — light (@3) + sound (@17) = 2 modalities

---

## Memory: SKIPPED — cap-burn

**Rationale:** Memory facet has 3 revise on feel-as-spine defense (cycle-2 verdict). All three remediation paths have unacceptable costs:
- Add NI @9: band-ceiling breach (exceeds 25% cap)
- Delete mem:1: SHAPE-FAIL single-register (mem:3 alone cannot carry both fires)
- Rubric authority ruling: out of scope for this run

Dispatch explicitly rules: leave `active-project/theater/facets/memory.md` UNCHANGED. Orchestrator-critic verdict will document memory as cap-burned with rationale. `memory.md` is not touched.

---

## Files modified

| File | Change |
|------|--------|
| `active-project/theater/facets/interest-narrator.md` | NI-6 @27 body rewritten to gap-narration pattern |
| `active-project/theater/facets/location-state.md` | loc-state:1 @1 light-level field appended |
| `active-project/theater/facets/sensory.md` | sensory:3 @17 sound entry added (already present from prior partial session) |
| `active-project/theater/proto-lines/b01-c01.md` | [sensory:3] added at @17 |
| `active-project/theater/facets/_inflight-r2/proto-lines-sensory.md` | created; [sensory:3] at @17 |

## Files NOT modified (per constraints)

| File | Reason |
|------|--------|
| `active-project/theater/facets/memory.md` | cap-burn skip per dispatch |
| `active-project/theater/facets/_inflight-r2/proto-lines-narrator.md` | NI-6 body change only; no cite cascade; [narrator:6] token unchanged |
| `active-project/theater/facets/_inflight-r2/proto-lines-loc-state.md` | field-add internal to loc-state:1 entry; no cite token change |
