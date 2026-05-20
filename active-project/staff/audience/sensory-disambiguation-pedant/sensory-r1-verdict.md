---
reviewer: sensory-disambiguation-pedant
facet: sensory
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

Two entries. One clears the disambiguation gate. One does not.

sensory:1 @3 `light: corner-room-dim -> overcast-yard-diffuse` — proto-line is `taylor-hebert-kl-122ac crosses the yard`. "Crosses" is a bare locomotion verb. No charged word is present. The audience reads physical movement, not the light-register of the transition, from the proto-line alone. The flag does work the language does not: it names the modality-specific inflection (enclosed dim → open diffuse) that "crosses the yard" doesn't supply. No action-verb self-charge applies — "crosses" does not name a light event the way "opens the shutter" names one. Modality choice (light) matches the spatial transition. Gate clears. ACCEPT.

sensory:2 @16 `thermal: wall-daytime-ambient-warmth -> wall-surface-cooling` — proto-line is `the walls cool`. Stop there. "Cool" is the thermal event. This is not a bare verb; it is an action-verb self-charge: the verb's semantic content IS the sensory inflection, identical in structure to "lights the lamp" or "ignites" or "extinguishes." The flag `thermal: ... -> wall-surface-cooling` restates in delta-form exactly what "cool" already tells the audience. No disambiguation work is being done; the proto-line is not bare with respect to thermal modality — the word "cool" charges it. Firing a thermal flag on top of "the walls cool" is redundant intensity-restatement. REJECT. Cut sensory:2.

Secondary note on sensory:1: the old-state "corner-room-dim" is an inference from loc-state:1's "door-shadow across the entry" — it names an ambient light level loc-state:1 does not explicitly declare. That question belongs to the old-state-reader specialist; I flag it as a border case but do not anchor my verdict on it. The disambiguation gate itself is the cleaner pass.

# Entry-level callouts

[sensory:2] @16 — `the walls cool` — "cool" is the thermal event; the verb self-charges the inflection. `thermal: wall-daytime-ambient-warmth -> wall-surface-cooling` adds nothing the proto-line does not already carry. Action-verb-self-charge; charged-verb redundancy. Cut.

# Convergence trace

- [sensory:2] @16 — convergent with auditor S-008 (r1, FREQUENCY-BAND: sensory 7.4% vs ceiling 6%; breach-high). Striking sensory:2 resolves the frequency-band breach by dropping to 1 entry (3.7%), inside the band. Independently arrived at through the charged-verb gate, not the density metric.
- [sensory:2] @16 — convergent with URI-FACETS-CYCLE-1 rubric promotion (rubric-sensory.md §1, 2026-05-19): the unanchored old-state note was promoted to HARD from prior audience-gate cycle-1 attacks on old-state quality. My charged-verb finding is an independent attack surface on the same entry, distinct from the old-state problem.
