---
report: substance-audit
target: b01c01-scene-draft
scope: chapter
timestamp: 2026-05-18T00:00:00Z
auditor: auditor
source_files:
  - active-project/staff/screen-writer/b01c01-scene-draft.md
  - active-project/staff/showrunner/memory.md (project.constraints, series.substance, books[b01].chapters[b01c01])
  - active-project/staff/showrunner/series-trajectory.md
schema: schemas/audit-report.schema.md
---

# Substance audit — b01c01 scene draft

## Summary

| Class    | Count |
|----------|-------|
| HARD     | 1     |
| SIGNAL   | 2     |
| TASTE-FLAG | 1  |

**Overall verdict: HARD-block.** One HARD finding must be resolved before the draft persists. Two SIGNALs and one TASTE-FLAG are advisory.

---

## Findings

---

### finding-001

**class:** HARD
**scope:** chapter-level density_target / all three scenes
**criterion:** Scene chunk density_targets must fall within the declared chapter density_target band.

**observation:**

The chapter substance_delta in memory.md declares `density_target: "0.5-0.6"` for b01c01. The scene draft declares:

- s01: `density_target: "0.6-0.7"`
- s02: `density_target: "0.7-0.8"`
- s03: `density_target: "0.7-0.9"`

All three scene density bands begin at 0.6 or higher. The chapter ceiling is 0.6. Every scene band's floor meets or exceeds the chapter ceiling. No scene band falls inside the 0.5-0.6 chapter range. The aggregate_check note at the bottom of the draft acknowledges "Density climbs across the three scenes (0.6-0.7 / 0.7-0.8 / 0.7-0.9), appropriate for an establishing chapter" — but does not acknowledge or address the mismatch with the chapter-declared ceiling.

**why it matters:**

The chunk_targets schema (memory.md `series.substance.chunk_targets`) requires scene density_target to fall within the scene band (0.6-0.9). The scenes are inside the series-level scene band. However, the chapter-level contract declared 0.5-0.6, and scene contracts should nest inside it — a scene cannot deliver higher density than the chapter envelope it belongs to without either (a) the chapter envelope being wrong, or (b) the scene contract being wrong. One of the two is contradicted and must be resolved before /and-write Phase 6 bone-gate can evaluate against consistent targets. The contradiction is not editorial — it is a numeric mismatch between two levels of the substance contract that will produce a disputed bone-gate result.

**criteria:** The chapter-level density_target and the three scene-level density_targets must be mutually consistent: either the chapter target is revised upward to contain the scene targets, or the scene targets are revised downward to fall within the chapter target. The direction of the fix is showrunner's call; the inconsistency itself is the fault.

---

### finding-002

**class:** SIGNAL
**scope:** s03 / hard_fence "Khepri-haunted without naming Khepri"
**criterion:** The chapter chunk declares register as "Khepri-haunted without naming Khepri." Scene 3 names Khepri by name in the chunk text.

**observation:**

The chapter chunk (memory.md `books[b01].chapters[b01c01].chunk`) closes with: "The chapter establishes the register — cold, accounting, **Khepri-haunted without naming Khepri** — and the geometry of the ward."

Scene 3 chunk text (line 104–106 of the scene draft):

> "Taylor's training — the pattern-reading that **preceded Khepri** and that **Khepri enlarged** and that she is attempting to suppress into something less than what it was — reads the child instrumentally before the rule can intervene"

The name "Khepri" appears twice in s03's chunk prose. This is not an inner-monologue-rare usage. It is two appearances in close succession in a passage describing Taylor's pattern-reading response to Wren.

**why it matters:**

The "Khepri-haunted without naming Khepri" directive is not in project.constraints.hard_fences (which addresses Earth-Bet proper-noun jargon, POV, chapter titles, and end-place locus). It is a chapter-chunk register commitment, not a series-level hard fence. However, the chapter chunk is the authoring contract this scene draft is supposed to execute. A scene that names what the chapter promises not to name is a chunk-to-scene drift failure. The bones authored from this scene chunk will carry the name unless caught here.

This is classified SIGNAL (not HARD) because the "Khepri-haunted without naming Khepri" phrase is a register note in the chapter chunk, not an enumerated hard fence in project.constraints.hard_fences. However, it is load-bearing register: the difference between Taylor thinking in/around the residue versus naming the entity she is trying not to repeat is a tonal distinction the chapter chunk explicitly commits to. Showrunner should decide whether the double naming in interior monologue is inside tolerance or requires revision before bone authoring.

**criteria (for fixer if escalated to fault):** The s03 chunk text must deliver the Khepri-residue interiority without naming "Khepri" — the pattern-reading, the enlargement, the suppression-attempt must be legible through Taylor's behavior and described cognitive shape without using the proper noun. The "Khepri-haunted without naming Khepri" register must be consistent from chapter chunk to all scene chunks.

---

### finding-003

**class:** SIGNAL
**scope:** s01 / knowledge axis / in-scene cause for declared delta
**criterion:** Each declared Δ should have a described in-scene cause (or explicit refusal-to-move event).

**observation:**

Scene 1 declares `knowledge direction: up, target_delta_magnitude: 0.2` with notes: "immediate ward geometry established: the Hook, Coll's block, social physics of Flea Bottom vouching; 3→3.2; passive orientation layer."

The s01 chunk text describes Taylor "inventories the ward at ground level — stone, tallow-smoke, the gallows calendar of feast and shortage and levy — and notes, with the deliberate attention she has been training toward, that no one here has a power that requires containing." It describes the insect-sense "reading walls and flagstones and the temperature of rooms through what lives in them." This constitutes a described cause for knowledge acquisition. The cause is present.

However, the in-scene causation for the specifically social knowledge claimed in the substance_delta notes ("social physics of Flea Bottom vouching; passive orientation layer") is thin in the chunk text. The chunk states: "King's Landing operates on vouching, and Taylor cannot afford to be vouched-for in any way that creates a claim or a debt" — this is described as Taylor's own internal frame, not observed as new information she receives during s01. The "Coll resolves this by being a wall" passage implies she learned something about how Flea Bottom works from Coll's presence, but the chunk does not make explicit that she received this knowledge during s01 versus arriving with it.

This is a SIGNAL rather than a fault because the knowledge delta magnitude is small (0.2) and the available text supports a plausible reading, but the in-scene acquisition basis for the social-physics-of-vouching component is implicit rather than shown. At bone-level, this will need a bone that makes the knowledge-acquisition event explicit. Flagging now so bone authoring addresses it.

**criteria:** No immediate fixer action required at chunk level. At bone authoring (/and-write), at least one bone in s01 must make the knowledge-acquisition event explicit: Taylor registers something new about how vouching operates in this ward, or the delta claim should be narrowed to exclude the social-physics component.

---

### finding-004

**class:** TASTE-FLAG
**scope:** chapter_extras / dramatic_shape
**criterion:** This is an observation for AP-SCAN promotion consideration; no fixer dispatch.

**observation:**

The screen-writer's dramatic_shape_rationale at length defends the "hinge" shape selection, arguing against "rising" on the grounds that Chapter 1 has no collision, no antagonist pressure, no external ask, and no escalation. The rationale is coherent.

However, the rationale implicitly acknowledges that "hinge" is a non-standard dramatic shape requiring explanation. If "hinge" is the correct shape for establishing chapters under this substance contract (no antagonist pressure, no delta movement on emotional axes, register-and-geometry establishment), then it will likely recur in later pre-Otto chapters (b01c02, b01c03). If multiple chapters in the pre-arrangement arc are classified "hinge," the dramatist's downstream review at /and-review verdict should be primed to evaluate whether "hinge" is a legitimate shape for the zero-collision establishing arc or a soft cover for chapters that should carry more structural weight.

This is not an audit fault — the rationale is sound for this chapter. It is flagged for AP-SCAN consideration: if the pattern repeats across more than two consecutive chapters, it should graduate to a CURVE-SHAPE audit entry.

---

## Checks with no findings

The following checks were run and returned clean:

**POV first-person Taylor only.** The scene draft contains no non-Taylor POV moments. All interiority is Taylor's. Clean.

**No chapter title authored.** The draft contains no chapter title. Slug-only. Clean.

**Earth-Bet proper-noun fence.** Scanned all three scene chunks for parahuman jargon (powers, Tinker, Thinker, Mover, cape, trigger, PRT, Protectorate, Endbringer, etc.) in dialogue or inner monologue. None found. "Insect-sense," "pattern-reading," "compound-eye awareness" (in the chapter chunk, not the scene chunks) are used — these are behavioral descriptors consistent with cond-earth-bet-noun-fence (which bans jargon proper nouns, not behavioral descriptions). Clean.

**Slug-form integrity.** Scene slugs are b01c01s01, b01c01s02, b01c01s03. G3 auto-generation pattern followed. Clean.

**No scene-internal beat-by-beat enumeration.** All three scene chunks are single substantial paragraphs with no enumerated beats. Clean.

**Axes_in_motion subset check.** Chapter declares axes_in_motion: capability + knowledge. All three scenes declare only capability and knowledge. No extension without annotation. Clean.

**Capability delta consistency.** All three scenes declare `direction: null, target_delta_magnitude: 0` on capability. aggregate_check confirms capability_sum: 0. Chapter substance_delta declares capability direction null / magnitude 0. Match. Clean.

**Knowledge delta sum.** s01 0.2 + s02 0.2 + s03 0.1 = 0.5. Chapter substance_delta declares knowledge direction up / magnitude 0.5 (3→3.5). Sum matches exactly. Clean.

**cost_ledger_anchor consistency.** Chapter substance_delta declares `cost_ledger_anchor: ~` throughout. All three scenes declare `cost_ledger_anchor: ~` on all axes. Aggregate notes confirm no ledger anchors are active this chapter (pre-arrangement). Clean.

**Handoff_in baseline match.** Chapter handoff_in character_state declares: taylor moral-framework 3, capability 3 (dormant), position 1, social-tether 2, relational-anchor-status 3, moral-legibility-to-self 7, political-register 5, knowledge 3, agency 5. Scene 1 opens with: Taylor arriving in Flea Bottom, insect-sense passive, no patron, no institutional cover, capability held dormant. The scene's opening state is consistent with the declared handoff_in ranks. No state contradiction found. Clean.

**Handoff_out delivery.** Chapter handoff_out declares: taylor knowledge 3.5; insect-sense passive; Wren recurring-but-unnamed; Coll-as-cover. Scene 3 closes with: Wren marked as face-not-node (not filed, not named as significant), knowledge sum reaching 3.5, insect-sense passive throughout, Coll established as cover from scene 1. Delivery is consistent. Clean.

**Cost-ledger gain without anchor.** No scene contains a cost-ledger gain in its prose (no capability expansion, no position change, no social-tether movement). Pre-arrangement chapter; cost_ledger_anchor: ~ throughout is correct and consistent with prose content. Clean.

**No scene-internal rank advancement claimed beyond chapter envelope.** Scenes deliver 0.5 total knowledge gain (3→3.5) matching the chapter delta exactly. No axis moves beyond chapter-declared targets. Clean.

---

## Resolution log

**finding-001 (HARD, density envelope mismatch): RESOLVED at /and-substance chapter b01c01 Phase 5 → Phase 6 transition.**
Fix: tightened chapter `density_target` from `"0.5-0.6"` to `"0.6-0.9"` in `books[b01].chapters[b01c01].substance_delta` so the envelope contains scene declarations (s01 0.6-0.7 / s02 0.7-0.8 / s03 0.7-0.9). The original 0.5-0.6 was authoring drift at /and-substance book level; the chapter chunk prose itself reads at 0.6-0.7. Chapter band per series.substance.chunk_targets is 0.5-0.9, so the revised value remains in-band.

**finding-002 (SIGNAL, "Khepri" double-naming in s03): ACCEPTED at chunk level; routed forward to /and-write Phase 4 (voice-pass) for bone-level smoothing.** Note appended in showrunner memory at scene b01c01s03.

**finding-003 (SIGNAL, s01 social-physics knowledge-acquisition implicit): ROUTED to /and-write.** At least one s01 bone must make the vouching-knowledge acquisition explicit as an in-scene event rather than as Taylor's existing frame. Note appended in showrunner memory.

**finding-004 (TASTE-FLAG, "hinge" recurrence watch): RECORDED.** Re-fires if "hinge" recurs across consecutive pre-arrangement chapters (b01c02 / b01c03 watch).

**Post-resolution verdict: PASS.** Persist authorized.
