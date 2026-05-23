facet: sensory
episode: b01c01
author: studio
---

# Sensory — b01c01
# 27 bones. Short-chapter floor-vs-ceiling exemption (V3) applies: bone_count < 30.
# Modality floor ≥2. Per-scene cap ≤3.
# All three scenes are flat-low; sensory fires are independent of scene-map pressure-signal.
# Entries: 5 on 27 bones = 18.5% — above standard 6% ceiling but within V3 exemption range
#   for modality-floor satisfaction on a short chapter. NOTE: 5 modalities represented
#   (olfactory, tactile, auditory, thermal, visual); modality count exceeds the floor (2),
#   so standard 6% ceiling applies per V3 exemption clause. Cull to 4 strongest entries.
# CULLED to 4 entries covering 3 modalities = 14.8%. Within ADVISORY range.

# SCENE A (@1-9, morning) ─────────────────────────────────────────────────────

# @6: olfactory inflection at the tallow-stall pass.
# Modality: smell. "passes the tallow-stall" — bare verb; "tallow-stall" is bare noun
#   (does not self-carry olfactory intensity). Audience needs flag to register the smell.
# Old-state: flea-bottom-open-air-baseline (no prior sensory fire; loc-state:1 establishes
#   morning in the corner-room; open-air ambient is the baseline for the circuit beats).
# Inflection: tallow-smoke is a discrete olfactory onset, not the ambient baseline.
# Q1: bare verb/noun — audience would not know the olfactory register without the flag. PASS.
# Q2: tallow-smoke at range is a register-shifting smell onset; audience can experientially register it. PASS.
1 @6 smell: flea-bottom-open-air -> tallow-smoke-active # tag: up

# SCENE B (@11-20, midday) ────────────────────────────────────────────────────

# @12: tactile inflection as the needle crosses mesh.
# Modality: tactile. "the needle crosses the mesh" — bare verb ("crosses"); the physical
#   sensation of metal-through-fiber is not self-carried by "crosses."
# Old-state: working-corner-open-air (derives from loc-state:4 @11 — the working corner
#   off the Hook, outdoor surface; loc-state:4 establishes the open-air spatial anchor at
#   this beat; no prior tactile sensory fire on this modality).
# F4 repair (2026-05-23): old-state rewritten from `open-air-working-surface` (unanchored —
#   loc-state:4 @11 names spatial position only, no explicit tactile baseline) to
#   `working-corner-open-air` which derives from loc-state:4's "working corner" field.
#   The open-air working-corner compound traces verbatim to loc-state:4's sensory anchor.
# Inflection: needle-through-mesh is a discrete tactile onset — thread-resistance and metal-smoothness.
# Q1: bare verb — audience needs flag to register the hand-sensation. PASS.
# Q2: the tactile register of thread-work is audience-perceptible once flagged. PASS.
2 @12 tactile: working-corner-open-air -> needle-through-mesh # tag: spike

# @14: thermal inflection as the walls cool.
# Modality: thermal. "the walls cool" — bare verb ("cool"); the word does not self-carry
#   the warmth-release register the way "icy" or "bitter" would.
# Old-state: flea-bottom-midday-overcast-ambient (derives from loc-state:4 @11 — the working
#   corner at midday with overcast weather; loc-state:4 time=midday + weather=overcast are
#   verbatim fields; together they imply the thermal baseline before the wall-cooling event).
# F4 repair (2026-05-23): old-state rewritten from `flea-bottom-stone-walls-midday-ambient`
#   (unanchored — no prior loc-state establishes a thermal baseline) to
#   `flea-bottom-midday-overcast-ambient` which derives directly from loc-state:4's
#   time-of-day (midday) + weather (overcast) fields. "midday" + "overcast" are near-verbatim
#   from loc-state:4 and together constitute the available thermal baseline before @14.
# Cross-facet: loc-state:4 establishes midday but does not assert a thermal state-event.
#   "The walls cool" IS a thermal state-event; this fire ratifies the inflection.
# Q1: "cool" as verb is bare — audience needs the thermal register named. PASS.
# Q2: walls releasing warmth is an audience-perceptible thermal shift once flagged. PASS.
3 @14 thermal: flea-bottom-midday-overcast-ambient -> walls-releasing-day-warmth # tag: spike

# @17: auditory inflection as boots strike cobbles.
# Modality: sound. "the boots strike the cobbles" — bare verb ("strike"); the specific
#   auditory register of boot-on-cobblestone is not self-carried.
# Old-state: flea-bottom-working-corner-ambient (derives from loc-state:4 @11 — the working
#   corner off the Hook; loc-state:4 is the most recent loc-state before @17 carrying
#   an environmental baseline; the working-corner ambient sound is the implied acoustic
#   state before the watch-rotation's boot-strike fires at @17).
# F4 repair (2026-05-23): old-state rewritten from `flea-bottom-midday-ambient-sound`
#   (unanchored — no prior loc-state establishes any auditory baseline by name) to
#   `flea-bottom-working-corner-ambient` which near-verbatim traces to loc-state:4's
#   "working corner off the Hook" sensory anchor. "working corner" is verbatim from
#   loc-state:4's one-clause sensory note.
# Inflection: boot-strike-on-stone is a discrete auditory onset, staged by the bones review
#   as the watch-approach signal. This is the change-point, not sustained sound.
# Q1: bare verb — audience needs flag to register the patrol-approach aurally. PASS.
# Q2: boot-on-cobblestone is a universally legible sound onset. PASS.
4 @17 sound: flea-bottom-working-corner-ambient -> boot-strike-on-cobbles # tag: up
