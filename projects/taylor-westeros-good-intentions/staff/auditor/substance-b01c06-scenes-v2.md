# Substance-contract integrity audit — b01c06 scene chunks v2
# Auditor: /and-substance chapter b01c06 Phase 4 leg
# Target: active-project/staff/showrunner/_drafts/b01c06-draft-2026-05-30-v2.md
# Against: memory.md b01c06 chapter contract + series.substance.cost_ledger + b01c05 handoff_out
# Produced: 2026-05-30

---

## Verdict: CLEAN (1 FLAG, 0 FAULTS, 0 HARD findings)

cl-d06 confirmed present. No fabricated anchors (cl06a / cl06b do not appear anywhere in v2 draft).

---

## Findings

### flag-001 — Second cl-d06 tranche unanchored (non-blocking)
- **id:** flag-001
- **type:** flag
- **what:** s01 substance_delta notes name "second +1.0 anchors at b01c08-b01c10" for the remaining relational_anchor_status tranche of cl-d06. The cost_ledger entry cl-d06 has `gain: "relational_anchor_status +2"`. This chapter settles +1.0 (first tranche confirmed). The notes identify b01c08-b01c10 as the downstream anchor range, but no chapter in that range currently carries a cl-d06 cost_ledger_anchor on relational_anchor_status. b01c08 handoff_in/out shows relational_anchor_status held at rank 3; b01c09 narrows the range further. The second tranche is named in the draft but is not yet anchored in any chapter contract.
- **why:** Unanchored second tranches are a recurring auditor finding on this project (the worm-canon-pedant flag pattern documented in the task briefing). If b01c08-b01c10 proceeds without a scene-level cl-d06 anchor on relational_anchor_status, the ledger gain of +2 will be partially unaccounted-for at the /and-write Phase 6 bone-gate, which checks against the finest-grained populated anchor field. This is a soft planning gap, not a current chapter violation.
- **criteria:** n/a (flag, not fault). Resolving chapter (b01c08 or b01c09 per the candidate range) must add `cost_ledger_anchor: cl-d06` to its relational_anchor_status axes_in_motion entry when the +1.0 second tranche lands.

---

## Check-by-check results

### 1. Cost-ledger anchoring
PASS. Both axes_in_motion entries that carry a cost_ledger_anchor in v2 use `cl-d06` exclusively:
- s01: relational_anchor_status up +1.0 → `cost_ledger_anchor: cl-d06` (gain side)
- s03: moral_framework down -1.0 → `cost_ledger_anchor: cl-d06` (cost side)
- s03: moral_legibility_to_self up +0.5 → `cost_ledger_anchor: null` (correct; no ledger entry exists for this axis in the cl-d06 entry)

The fabricated anchors cl06a and cl06b appear nowhere in the v2 draft. This is the correct chapter.

Ledger entry cl-d06 confirmed in memory.md:
```
id: cl-d06
gain: "relational_anchor_status +2"
cost: "moral_framework -1"
anchor: { book: b01, chapter: null, scene: null }
```

Direction match: s01 gain side (relational_anchor_status up) matches `gain: relational_anchor_status +2`. s03 cost side (moral_framework down) matches `cost: moral_framework -1`. Both correct.

### 2. Roll-up verification
PASS. Per-scene axis moves sum to chapter-level targets:

- moral_framework: s01 held, s02 held, s03 down -1.0 → sum = -1.0. Chapter target = -1.0. EXACT.
- relational_anchor_status: s01 up +1.0, s02 held, s03 held → sum = +1.0. Chapter target = +1.0. EXACT.
- moral_legibility_to_self: s01 held (rationale: accounting hasn't run yet), s02 held, s03 up +0.5 → sum = +0.5. Chapter target = +0.5. EXACT.

All three moving axes roll up exactly. No rounding gaps.

s02 empty axes_in_motion: LEGAL. Schema field notes permit `axes_in_motion: []` at scene level when the scene's work is held-axis load-bearing. s02 carries seven axes_held entries with rationales, and its scene_conflict.stakes_axis (moral_framework) is in its axes_held list. This is structurally valid per schema field-notes: "scene_conflict.stakes_axis may resolve to either axes_in_motion[] (the axis the conflict moves) or axes_held[] (the axis the conflict holds) — both are valid stakes."

### 3. cl-d06 partial settlement — second tranche anchor
FLAG (flag-001 above). First tranche: s01 notes confirm "+1.0 of +2 ledger gain; second +1.0 anchors at b01c08-b01c10." The draft names the downstream anchor range. The second tranche is not yet anchored in any chapter contract within that range. Non-blocking at this chapter level; resolving chapter must carry the anchor forward.

### 4. Held axes — genuine hold, no silent drift
PASS. Each held axis at each scene carries a rationale. Checking the four chapter-contract-held axes against each scene's held entries:

- **capability:** All 3 scenes carry capability in axes_held with rationale: s01 "coverage-maintenance walk; no new network expansion"; s02 "coverage-recall, not new feed deployment"; s03 "the send uses the coverage architecture already in place." No narrative content in any scene chunk suggests capability expansion. CLEAN.
- **position-prot-rise:** All 3 scenes carry position-prot-rise in axes_held with rationale: s01 "no patron-tier visibility event; the Wren exchange is ward-layer"; s02 "the request arrives through Jarvis, not a new formalization event"; s03 "the delivery is within the existing arrangement." Chapter chunk contains no formalization event. CLEAN.
- **political_register-prot:** All 3 scenes carry political_register-prot in axes_held with rationale naming that resentment does not advance in the Flea Bottom register. s02 rationale notes "resentment color is present from c05 but does not advance in the compilation register." This is consistent with the chapter contract. The chapter chunk itself contains no court-tier content that would advance the resentment beyond c05's handoff_out state (rank 2.5). CLEAN.
- **social_tether-prot-rise:** All 3 scenes carry social_tether-prot-rise in axes_held. s01 rationale is the most load-bearing: "the Wren contact is explicitly kept OUT of the deliverable tether layer; the omission from the contact-source field is the mechanism of that exclusion; tether holds — no new structural addition; social_tether-prot-rise moves when a contact enters the arrangement layer, which Wren does not." This is mechanically consistent with the chapter contract's axes_held rationale ("the Wren contact is explicitly kept OUT of the deliverable tether layer"). CLEAN.

### 5. Handoff continuity
PASS. b01c05 handoff_out:
- "political_register-prot: resentment color now present in all court-tier feed interpretation" → confirmed carried in s02 rationale ("resentment color is present from c05")
- "Wren: in coverage map; anchor rank 2" → s01 substance_delta notes confirm this is the "first spoken exchange," consistent with anchor rank 2 (seen-not-spoken) upgrading to active-protection-register in s01; s01 pov chunk and chunk description confirm she is "seen-not-spoken" at chapter open, consistent with handoff_in "one seen-not-spoken contact; anchor rank 2"
- "cf-d10-courier-face: courier body in Taylor's memory" → s03 holds this as a background element (the Jarvis delivery mechanism); not disturbed
- "Flea Bottom intelligence routing: continuing" → the Otto elder-list ask arrives through Jarvis, consistent

Chapter handoff_in from memory.md:
- "Wren: in coverage map; one seen-not-spoken contact; anchor rank 2" — s01 opens with the Wren exchange as first-spoken, consistent
- "Taylor: political_register-prot rank 2.5; moral_framework cracked" — s02/s03 both carry political_register-prot held and moral_framework held until s03 delivery, consistent with opening at "cracked" level

Chapter handoff_out (memory.md):
- "Wren: first spoken exchange; omitted from deliverable; anchor rank 3" — s01 delivers first spoken exchange + deliberate omission from contact-source field; s03 echoes the contrast ("the four names went. Wren's name did not go"). Consistent.
- "moral_framework rank 0 (rationalized breach on record)" — s03 substance_delta notes confirm -1.0 full delivery in this scene; the handoff_out rank of 0 implies this is the chapter where moral_framework hits its chapter-floor; consistent with -1.0 delivering here.
- "relational_anchor_status rank 3" — s01 moves ras from rank 2 to rank 3 (+1.0); consistent.
- "moral_legibility rank 5" — s03 delivers +0.5; consistent with prior rank 4.5 + 0.5 = 5.

No continuity faults. The resentment color held correctly across c05 → c06 without advancement. The Wren "seen-not-spoken" status from c05 handoff_out correctly upgrades to "first spoken exchange" at c06 s01 open. CLEAN.

### 6. Schema compliance
PASS WITH NOTE. Scene entries carry: slug, seq, status, pov_narrator, chunk (with URI-CHUNK-TAG-PROTOCOL inline tags), substance_delta (axes_in_motion + axes_held + density_target), scene_conflict (protagonist_force, opposing_force, stakes_axis).

Schema field `dramatic_shape` at scene level: the schema shows `dramatic_shape` as a chapter-level field (`chapters[].dramatic_shape`). Scenes do not have a per-scene dramatic_shape field in the schema. The v2 draft does not carry per-scene dramatic_shape. This is schema-compliant — dramatic_shape is chapter-scope only, and the chapter carries `dramatic_shape: climax` in the memory.md contract.

Schema also notes chapter-level `goal` and `handoff_in/out` are required; these are in the chapter record in memory.md (not in the scene-chunk draft file), which is the correct location per schema structure.

All required scene-level fields present. CLEAN.

### 7. stakes_axis union check
PASS.

- s01: `stakes_axis: relational_anchor_status` — this axis is in s01.axes_in_motion (direction: up, target +1.0). Stakes axis is a moving axis. LEGAL.
- s02: `stakes_axis: moral_framework` — this axis is in s02.axes_held (rationale: "the list is compiled but not sent; no delivery is complete in this scene; the moral weight of the act lands at the send, not at the compile"). Stakes axis is a held axis. LEGAL per schema field notes: "scene_conflict.stakes_axis may resolve to either axes_in_motion[] or axes_held[]."
- s03: `stakes_axis: moral_framework` — this axis is in s03.axes_in_motion (direction: down, target -1.0). Stakes axis is a moving axis. LEGAL.

All three stakes_axis references resolve correctly against their respective scene's substance_delta.

---

## Summary table

| Check | Result | Finding |
|---|---|---|
| 1. Cost-ledger anchoring (cl-d06 present; no cl06a/cl06b) | PASS | — |
| 2. Roll-up (scene sums = chapter targets) | PASS | — |
| 3. cl-d06 partial settlement — second tranche | FLAG | flag-001 (non-blocking) |
| 4. Held axes — no silent drift | PASS | — |
| 5. Handoff continuity (c05 in; c07 out) | PASS | — |
| 6. Schema compliance | PASS | — |
| 7. stakes_axis union check | PASS | — |

**cl-d06 confirmed.** cl06a and cl06b do not appear in this draft. This is the correct chapter.
