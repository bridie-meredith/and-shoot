---
reviewer: sensory-disambiguation-pedant
facet: sensory
cycle: 2
episode: b01-c01
date: 2026-05-25
verdict: accept
---

# Prior-cycle complaint status

Cycle-1 HARD: [sensory:2] @16 — action-verb self-charge. "raises the voice" idiom self-carries louder-register; sound flag was redundant.

Fixer response: sensory:2 deleted at @16 (sound); new sensory:2 added at @9 (tactile: lane-ambient -> crowd-compression # tag: up). Modality changed, anchor moved, anti-pattern #14 pre-validation logged in carve-out header.

The cycle-1 HARD is cleared. No further action on that finding.

---

# Cycle-2 per-entry adversarial read

## sensory:1 @2 — smell: lane-ambient -> tallow-smoke-onset # tag: up

Proto-line: `the tallow smoke crosses the stitch-house lane`

Disambiguation gate (Q1): "crosses" is a bare movement verb. "Tallow smoke" names the substance, not the perceptual register of the smell. The proto-line does not self-carry olfactory inflection; a reader receives locomotion, not onset. The flag does the disambiguation work the language does not. Gate clears.

Magnitude (Q2): Tallow smoke onset in a narrow lane is not micro-grain; it is a discrete environmental change the audience can register as a perceptual shift from drain-water baseline. Gate clears.

Old-state: "lane-ambient." The carve-out governs: no loc-state exists for this chapter except the single @1 loc-state entry. loc-state:1 @1 names `drain-water trickle audible at the angle-gap pinch-point` under the sound field and does not establish an olfactory baseline. The carve-out annotation correctly identifies the old-state as scene-internal (bone 1: drain water; smoke first appears at bone 2), sourcing from the earliest viable scene-internal baseline on this modality. The claim is defensible.

Cross-facet: loc-state:1 @1 names no smell event — it establishes the location baseline for sound. No silent-gap obligation fires from loc-state toward sensory:1. No contradiction.

No charged words in `the tallow smoke crosses the stitch-house lane`. "Tallow" names the substance; "smoke" is bare as a count noun here (no self-carrying intensity adjective attached).

Verdict: CLEAN.

## sensory:2 @9 — tactile: lane-ambient -> crowd-compression # tag: up

Proto-line: `the crowd compresses`

Disambiguation gate (Q1): "compresses" is a bare physical-process verb. The proto-line describes aggregate movement; it does not surface flesh-against-flesh tactile register. A reader receives spatial contraction, not skin-pressure. The flag disambiguates the tactile channel. Gate clears.

Magnitude (Q2): Crowd-compression in a narrow Flea Bottom lane is a register-shifting tactile event — bodies pressing, yielding-space gone. This is not micro-grain; it is experientially perceptible at audience scale. Gate clears.

Old-state: "lane-ambient." Same carve-out logic as sensory:1. The carve-out header documents this explicitly: bones 1-8 establish the lane as occupied but not yet crowd-compressed; no prior tactile entry on this modality exists. The scene-internal baseline is the earliest defensible source. Anti-pattern #14 pre-validation is logged: modality identifiable (tactile); inflection class clear (up, discrete onset); bare proto-line confirmed; Q1 and Q2 cleared; audience-side perceptible (universally legible once flagged); inflection-not-sustained (onset bone, not established level). All five pre-validation points documented. The fixer process was correct.

Modality check: "crowd compresses" is a tactile / pressure event, not smell or sound. The tactile modality assignment tracks the bare word's natural perceptual axis. No modality mismatch.

Action-verb self-charge check: "compresses" does not self-charge the tactile register the way "lights" carries light-onset or "raises the voice" carries louder-register. "Compresses" describes spatial reduction; the sensory register — flesh pressure, body heat, loss of movement clearance — is not in the surface meaning of the word. This is not an action-verb-self-charge case.

Inflection-not-sustained: @9 is the onset beat. The lane was occupied but not crowd-compressed at bones 1-8. This is a change-point, not sustained state. Fire is correctly placed at the inflection, not repeated across the compression run.

Cross-facet: loc-state:1 @1 establishes no tactile note. No contradiction with the new sensory:2 entry. No silent-gap introduced by loc-state that sensory leaves unaddressed.

Verdict: CLEAN.

---

# File-level curve-shape check

Two entries on 27 bones: 7.4%. Short-chapter floor-vs-ceiling exemption (V3) applies: bone_count (27) < 30 AND modality count equals the floor (2: smell + tactile). Under the exemption, effective ceiling is max(6%, 2/27) = 7.4%. The density is at the exemption threshold, not above it. ADVISORY status, not blocking. The modality floor is met; the disambiguation gradient is preserved (two entries across 27 bones is sparse).

Modality-coverage: smell (sensory:1 @2) + tactile (sensory:2 @9). Two modalities. Floor satisfied.

Bare-not-charged audit: both fires attach to bare-verb proto-lines. Zero charged-word fires.

Inflection-not-sustained: sensory:1 is the smoke-onset beat (first smoke bone); sensory:2 is the crowd-compression onset beat. Neither is sustain-level repeat. Clean.

Inflection-pair coherence: no drop/up pairs present. Not applicable.

---

# Convergence trace

fault-C2C-001 (cycle-2 audit-confirm): two sidecar entries (dialogue, taylor-hebert-kl-122ac.drafts.md entries 1 and 2) retain sensory:2 @16 citations that fail cite-index walk. This is a dialogue-facet fault, not a sensory-facet fault. The sensory file itself is clean. The broken sidecar citations are outside this reviewer's scope (sensory facet per-entry attack only; dialogue file is not this facet). No overlap with sensory callouts.

flag-C2C-003 (prior flags carried forward): flag-C2-001 noted the carve-out header's "factual premise stale" — originally written against a zero-loc-state premise. The cycle-1 remediation added loc-state:1 @1. The carve-out header was updated for sensory:2 (@9 replacement) but carries the original framing for sensory:1 that predates the loc-state:1 add. The carve-out annotation for sensory:1 still reads "no loc-state" when loc-state:1 @1 now exists. This is a documentation inconsistency in the carve-out header comment, not in the sensory entry itself. The entry-level analysis above confirms sensory:1's old-state (smell: lane-ambient) does not contradict loc-state:1 @1 (which addresses sound/drain-water, not smell). The inconsistency is advisory; it does not introduce a rubric fault in the sensory entry. I note it for the record; it does not change my verdict.

---

# Verdict

accept

Both entries clear the full disambiguation gate. The action-verb self-charge HARD from cycle 1 is resolved. No new per-entry or file-level findings from this reviewer.
