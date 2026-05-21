---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

The environment and prop entries are mechanically sound. No Worm-power-mechanics claims. The non-Taylor actor entries (Coll's work-cycle, Wren's location and social-engagement pairs) are clean — correct targets, correct fields, correct persistence reads. The Taylor-side entries are structurally sound on the entries themselves: position, lodging-payment, inventory cycles, knowledge accumulations, social-state pivots — all within what the character's power-state at this point permits (insect-sense at-passive, no deployment, no cross-insect-network access, no multi-shard behavior). The capability-silence discipline is correctly maintained. The cull decision at @15 (insect-feed density not a state-flip but a perception of baseline) and @18 (watch-passage a NON-event because deployment-threshold uncrossed) are both canonically correct reads. Taylor suppressing output without suppressing input is exactly how passive insect-sense works; the distinction is honored.

What tracks, then. What doesn't: the consolidated file (`state-updates.md`) does not carry the `# rubric-carve-out` annotation block at the position required by the auditor's fault-001 finding. The block exists in `state-updates-taylor-hebert-kl-122ac.md`. It did not propagate to the consolidated file between the frontmatter close and `# source: env`. The auditor is correct. The gate is blocked.

The reason this reviewer specifically cares, beyond the structural compliance point: the rubric-carve-out for the taylor-state entries is the record that justifies capability-consistent interpretation of the co-citation pattern. Two entries in the taylor-state section — knowledge.coll-pattern at @20 and social-state.with-wren at @25 — are knowledge.* and social-state.* class, which the rubric requires NI co-citation for. Their exemption rests on the band-ceiling collision defense: adding NI co-citations to satisfy mechanical state pairing would breach the frequency-band ceiling. That is a canon-accurate call (the chapter has zero peak-bones and a substance contract of mechanical-establishment — Taylor's shard is not doing anything noteworthy). But if the defense is not in the consolidated file, anyone reading canonical state for the next chapter will see knowledge-state entries with no co-citation and no explanation. The next author might infer that the knowledge-state was acquired through suppressed shard activity rather than ordinary observation — which is the wrong reading. The carve-out annotation is not just a compliance artifact; it is a Worm-canon accuracy record for downstream authoring.

There is one additional observation, not a blocking callout: the consolidated file's source block for taylor-hebert-kl-122ac (lines 39-107 of state-updates.md) does embed the rubric-carve-out annotation. It is present in the source slice within the consolidated file — the annotation block appears between the source header comment and entry 9 @1. The auditor's fault-001 is that it needs to be at the top-of-file position, between the consolidated frontmatter close and `# source: env`, not embedded inside a source slice. This matters because the top-of-file position is where the gate's automated checks look, and where any reader of the consolidated file will encounter the defense before encountering the entries it defends. The fix is a position fix, not an authoring fix. The content already exists.

# Entry-level callouts

[state-updates:state:11] @6 — `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped`
The one taylor knowledge entry with NI co-citation (narrator:2 @6). Correct. The "hook-block-route-mapped" value is specific and clean — she has mapped a route, not the entirety of Flea Bottom. Frugality honored. This entry tracks.

[state-updates:state:8] @20 — `actor:taylor-hebert-kl-122ac.knowledge.coll-pattern: unread -> day-cycle-pattern-read`
knowledge.* field, requires NI co-citation per rubric. NI-absent. Defense in source file: flat-low scene-B close, third NI fire would breach band ceiling, NI:4 @18 carries the cost register. The defense is correct — this is a routine observational accumulation (watching a person work for a day), not a shard-mediated insight. The value "day-cycle-pattern-read" is appropriately granular: she knows Coll's working-day pattern, not a comprehensive behavioral model. Frugality holds. The co-citation defense is sound but not in the consolidated file at the required position.

[state-updates:state:17] @25 — `actor:taylor-hebert-kl-122ac.social-state.with-wren: unknown-ward -> spoken-once`
social-state.* field, requires NI co-citation per rubric. NI-absent. Defense in source file: speech-act IS the delta-producer; NI:6 @27 resolves interior register two beats later. "Spoken-once" is exactly the right granularity for a first contact — it does not overclaim knowledge or social integration. This is the entry that most matters for the series arc (the goal statement names the ward explicitly). Its canon-accuracy is sound; its NI-defense needs to be visible in the consolidated file.

[state-updates — capability-silence at @15, @18, @22] — NON-events, correctly held.
@15: insect-feed density is Taylor's baseline perception of a crowded environment, not a tracked-field flip. Correct silence.
@18: city-watch passage is a potential trigger (social-pressure event, stranger-proximity) but the deployment threshold is not crossed — she notices without deploying. Correct silence. This is canon-consistent: Taylor in the early arcs registers threats without always acting on them.
@22: wren approach — NI:5 fires ("a girl comes in through the swarm before she comes in through the door"), which is the perception event. The state-update on social-state fires at @25 when the speech-act constitutes the state-change. The sequencing is correct: registration at @22 (NI territory), state-flip at @25 (state-updates territory). Correct.

# Convergence trace

[state-updates:state:8] @20 — directly overlaps fault-001 (F-006 UNRESOLVED from auditor r2). The auditor's criteria (b) name knowledge.coll-pattern as one of the two "accepted-with-defense" entries the carve-out must classify explicitly. The auditor's criteria (c) require §Anti-patterns #9 (density-on-flat) citation. Neither criterion is met in the consolidated file at the required position.

[state-updates:state:17] @25 — directly overlaps fault-001 criteria (b): social-state.with-wren is the second "accepted-with-defense" entry. The auditor's full criteria list: (a) rubric §Cross-facet contract scope citation, (b) per-entry classification, (c) §Anti-patterns #9 citation, (d) explicit statement that the carve-out resolves F-006. All four criteria apply to the consolidated file annotation. None are present at the required position in that file.

[state-updates — file-level] — fault-001 is the direct auditor finding. This reviewer's verdict tracks it exactly. The carve-out content exists in the per-character source file and in the embedded source slice within the consolidated file; it is absent from the top-of-file position in the consolidated deliverable. The fix is a position correction, not an authoring task.
