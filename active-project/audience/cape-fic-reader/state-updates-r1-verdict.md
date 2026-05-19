---
reviewer: cape-fic-reader
facet: state-updates
episode: b01c01
cycle: r1
date: 2026-05-19
verdict: revise
---

# Cape-Fic Reader — State-Updates Adversarial Reading

## Persona frame

Pattern-hungry, lore-tracking, tactically engaged. Reads state-updates as the canonical record of who-knows-what-when. Every `knowledge.*` entry is a legibility event: the board just changed, the character just learned something, the faction-geometry just shifted. If a knowledge entry fires when the character had no in-world path to acquire it, or if a persistent-state entry fires on a beat that looks like a glance rather than a commitment, this reader calls it out mid-track.

Fatigue trigger: eye-glaze on unmotivated knowledge entries — if a field-change registers information the character collected off-screen or through a path the proto-lines don't establish, this reader stops trusting the state file.

---

## Per-entry adversarial pass

**[state-updates:1] @1 `prop:oc-corner-room.occupancy: vacant -> taylor-occupant`**
Prop change fires at entry. Taylor enters; occupancy flips. Persistent past the beat. Field-extension documented. `CLEAN`

**[state-updates:2] @2 `prop:oc-corner-room.rent-status: unpaid -> paid`**
Rent-paid is the social-license credential. Fires at the payment beat. Persistent. `CLEAN`

**[state-updates:3] @5 `prop:oc-needle.held-by: coll-net-mender-flea-bottom -> taylor-hebert-kl-122ac`**
Needle passes hands at @5. Field-extension documented. Persistent through @17. `CLEAN`

**[state-updates:4] @13 `studio.thermal: ambient-day -> walls-cooling`**
Environmental ambient-temperature shift. Persistent through Scene-B remainder. `CLEAN`

**[state-updates:5] @18 `prop:oc-nets.worked-state: in-progress -> set-down`**
Work session ends at @18. Persistent into Scene-C. `CLEAN`

**[state-updates:6] @3 `actor:coll-net-mender-flea-bottom.block_baseline_new_faces: none-this-week -> one-new-face-fish-gate-lane`**
Non-interpretive accumulation of presence data. Deferral comment (pattern registration to ~d06) is exactly the limit-tracking this reader wants. Fires at first verbal contact. `CLEAN`

**[state-updates:7] @2 `actor:taylor-hebert-kl-122ac.social-tether.coll-block-presence: none -> paying-resident-at-corner-room`**
Payment at @2 establishes social standing. Fires at the transaction beat. Consistent with prop entry 2 on same beat (different target). `CLEAN`

**[state-updates:8] @3 `actor:taylor-hebert-kl-122ac.knowledge.coll-as-vouching-vector: unmapped -> registered-as-block-fixture-with-verbal-contact`**

The value `registered-as-block-fixture-with-verbal-contact` is defensible — the new-value is the conservative part. But the **field name** `coll-as-vouching-vector` does more interpretive work than @3 earns. @3 is "coll speaks to taylor" — Coll is established as a block fixture with verbal contact. The vouching-vector framing encodes a second-order tactical inference (Taylor assessing Coll's social-license utility) that the proto-line does not establish. Field names are part of the canonical write-back record; a field name that implies tactical assessment before the assessment beat fires is a soft forward-projection.

`FLAG: field name [coll-as-vouching-vector] encodes vouching-valence assessment; @3 establishes contact only; consider [coll-as-block-presence] or defer the vouching-vector field name to a beat where Taylor explicitly maps Coll's utility`

Convergence-trace: no auditor r1/r2 finding covers this field-name issue. Independent call.

**[state-updates:9] @5 `actor:taylor-hebert-kl-122ac.work-role.coll-block: outside -> needle-handler-at-coll-block`**
Needle passes at @5; work-role flips. Persistent. `CLEAN`

**[state-updates:10] @8 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.active-holding: ambient-passive -> threshold-held-against-density-spike`**

Cite-index shows `state:10 @8 back=N`. The bones file at @8 carries `[narrator:2] [state:4]` — `state:4` in that notation is entry 4 (the thermal entry, @13). There is no `[state:10]` token on the @8 proto-line in the bones file. This means the @8 proto-line does not back-cite entry 10.

The rubric requires the anchor proto-line's verb to describe a transition that mutates the tracked field. @8 is "the insects cover the flagstones" — passive sensory coverage event. That verb establishes the density-spike stimulus. Whether Taylor transitions from `ambient-passive` to `threshold-held-against-density-spike` **at @8** versus **across @8–@12** is ambiguous. With `back=N` and no bones-file citation, the verification path is opaque. This reader cannot confirm the @8 beat is the transition beat rather than the onset of a gradual shift.

`FLAG: [state-updates:10] @8 back=N — no bones-file co-citation; cannot verify @8 proto-line establishes the active-holding flip; the insect-density stimulus is real but the discipline-posture transition may belong at @12 (insects fill the block, the escalated event) rather than @8 (insects cover flagstones, the initial contact)`

Convergence-trace: auditor r1/r2 do not enumerate state-updates per-entry back=N status. Independent call.

**[state-updates:11] @12 `actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively`**
@12 is "insects fill the block" — full-block insect sweep. The `passively` qualifier correctly marks acquisition mode. Board-state entry this reader most wants: Taylor is now reading the whole block through insect-sense. `CLEAN`

**[state-updates:12] @15 `actor:taylor-hebert-kl-122ac.knowledge.watch-patrol-cadence-hook: unknown -> patrol-pattern-read-passively`**
Highest-stakes knowledge acquisition in the file. @15 is "the city-watch passes the hook." Taylor reads patrol timing through ambient insect-sense. Narrator-interest co-citation present (narrator:4 @15). The `passively` qualifier is right — she's not running an active sweep, the patrol walks through her existing sense coverage. `CLEAN`

**[state-updates:13] @18 `actor:taylor-hebert-kl-122ac.work-role.coll-block: needle-handler-at-coll-block -> recurring-needle-handler-coll-block`**

@18 is "taylor drops the nets." That is the work-session-end beat. The transition to `recurring` implies Coll has signaled that Taylor is expected back — but @18 is the *completion* of the session, not a recurrence-invitation beat. What proto-line establishes the "recurring" part? If Coll invites Taylor back at @3 or during the session, that is not explicit in the bones file. The `recurring` suffix is prospective: it says the relationship will persist past this chapter. That may be accurate in the substance contract, but firing it on the work-session-end beat (dropping the nets) is a forward-projection rather than a beat-anchored state flip.

`FLAG: [state-updates:13] @18 — "recurring" is prospective; @18 (work-session-end) does not establish recurrence-intent; fire [recurring] at a beat where Coll's re-engagement signal is explicit, or hold the value at [needle-handler-at-coll-block] for this chapter and fire the recurrence transition in the next chapter where re-engagement is demonstrated`

Convergence-trace: no auditor finding covers this. Independent call.

**[state-updates:14] @22 `actor:taylor-hebert-kl-122ac.knowledge.wren-presence: unregistered -> face-with-voice-registered`**
@22 is Wren speaking to Taylor. First verbal contact. Face-and-voice registration. `CLEAN`

**[state-updates:15] @24 `actor:taylor-hebert-kl-122ac.insect-sense-discipline.pattern-reading: auto-initiating -> caught-by-rule-not-deployed`**
The chapter's hinge entry. The prohibition catches the auto-initiation of pattern-reading before deployment. Transition is persistent (Taylor does not re-deploy in this chapter). The old value `auto-initiating` accurately names the prior posture. This entry is why the state-updates file earns its keep. `CLEAN`

**[state-updates:16] @25 `actor:taylor-hebert-kl-122ac.relational-anchor-status.wren: stranger -> face-not-node`**
The `stranger -> face-not-node` distinction is a hard conceptual line drawn correctly: Wren enters the register but Taylor explicitly refuses to operationalize her as a network node. `CLEAN`

**[state-updates:17] @26 `actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper`**

@26 is "wren leaves the street." The knowledge shift to `ward-layer-deeper` implies Taylor has now synthesized Wren's presence into a deeper map of the Hook ward social structure. But the information that produces this synthesis came from the @22–@25 exchange (Wren speaks, Taylor responds, Taylor holds the pattern-read). The synthesis beat is within the conversation, not at departure. Firing `ward-layer-deeper` at @26 (exit) rather than @22–@25 (acquisition) lags the knowledge flip behind its source.

The rubric anti-pattern #7 is "pre-empting / lagging: firing the entry on a beat adjacent to the actual change-beat." This is the lag variant: the field actually flips during the conversation, not when Wren walks away.

`FLAG: [state-updates:17] @26 — knowledge lag; ward-layer information acquired during @22–@25 conversation; firing at @26 (departure) is anti-pattern #7 (lag variant); move to @22 or @25`

Convergence-trace: rubric anti-pattern #7. No auditor finding covers this specific entry. Independent call.

**[state-updates:18] @20 `actor:wren-stitch-maker-flea-bottom-ward.location: stitch-maker-household-hook-district -> flea-bottom-street-outside-coll-corner-room`**
Wren arrives at @20. Location flip at arrival beat. `CLEAN`

**[state-updates:19] @22 `actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness: unencountered -> noticed-as-presence-on-block`**
Field-extension reset from d01+ baseline correctly documented. First-registration only. `CLEAN`

**[state-updates:20] @26 `actor:wren-stitch-maker-flea-bottom-ward.location: flea-bottom-street-outside-coll-corner-room -> returning-to-stitch-maker-household-hook-district`**
Departure beat. `returning-to` correctly encodes in-transit direction rather than arrived-at. `CLEAN`

---

## File-level concern

The rubric band is 8–18% of proto-lines. On 26 bones, that is 2–4 entries. This file has 20 entries on 26 bones (77%). Even adjusted for a shorter chapter, the density is high. The auditor issued `SHAPE-OK` but the rubric's density concern applies especially to knowledge entries — this file has seven `actor:taylor.knowledge.*` or cognate discipline entries, which is legitimate for a chapter where Taylor is doing active environmental reading. This reader accepts the density as plot-justified but flags it as worth reviewing on a per-entry strip-test before lock.

---

## Verdict

`revise`

**Named revision targets:**

1. `[state-updates:8]` — field name `coll-as-vouching-vector` encodes an inference @3 does not earn; rename.
2. `[state-updates:10]` — `back=N`; @8 proto-line does not verify the active-holding flip; verify beat or move to @12.
3. `[state-updates:13]` — "recurring" suffix is a forward-projection @18 does not establish; hold or re-anchor.
4. `[state-updates:17]` — knowledge lag; ward-layer-deeper fires at departure instead of acquisition; move to @22 or @25.
