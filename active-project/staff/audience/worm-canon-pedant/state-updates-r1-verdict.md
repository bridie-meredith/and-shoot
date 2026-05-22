---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

Running the tally.

State:11 @5 — `actor:taylor-hebert-kl-122ac.capability-deployment-history: dormant-never-deployed-in-kl -> deployed-defensive-flea-bottom`. First deployment in King's Landing. The prior value `dormant-never-deployed-in-kl` is the correct baseline if this is her first use in this setting. "Defensive-flea-bottom" is a reasonable characterization for insect-routing that routes a watch patrol around Wren. Power mechanics: using swarm positioning to redirect foot traffic is canon-Taylor's wheelhouse — no limit exceeded, no range or Manton-effect issue visible. This one tracks.

State:2 @5 — studio's corresponding env write. Consistent with state:11. No issue.

State:10 @12 — `actor:coll-net-mender-flea-bottom.stats.taylor_pattern_registered: not-yet -> registered-as-anomaly`. Here is where I stop. The trailing comment reads: "substrate-level registration, non-declarative — the glance lifts once and accumulates as presence-data, no model built, nothing named (hard fence 1/2 honored)."

"Substrate-level" is shard-architecture language. In Worm, the substrate is parahuman territory — the layer at which shards operate and communicate. Using "substrate-level registration" to describe a Westerosi net-mender's passive noticing either (a) assigns Coll shard-derived detection capability not established anywhere in the chapter or character file, or (b) uses the term metaphorically without flagging the metaphorical use. Either reading is a problem. If (a): Coll does not have a cape card; power mechanics that exceed established limits without acknowledged reason is my flag. If (b): the Worm-specific term is being used incorrectly, which is also my flag.

More pressingly: "hard fence 1/2 honored." There are two hard fences. One is honored. The comment moves on. The one that is not honored — what is it, and what does it mean that it is not honored? This is a power-mechanics constraint claim with an unresolved compliance gap baked into the entry comment. A state-update that notes its own partial compliance is not a state-update I can accept as canon-clean.

State:12 @15 — `actor:taylor-hebert-kl-122ac.social-tether-wren: peripheral-permitted-attachment -> crystallized-observer-bond`. One encounter. One shared watch-sweep deflection. Taylor does not crystallize social bonds on single encounters. This is the attachment-formation speed problem. Canon Taylor's trigger event and school history made her hyper-vigilant about social attachment and observer dynamics — she is acutely aware of when she is being watched, and acutely aware of the cost of being attached to people. "Crystallized-observer-bond" after one deployment event where Wren watched her command flies is too fast for the character on record. The character who spent years eating lunch alone, who catalogued social dynamics from outside, who was slow to trust the Undersiders — that character does not crystallize bonds at this rate.

The `social-tether-wren` field is a field extension on Taylor's actor-state. Whether the extension is licit is the auditor's call. My call is whether the value it reaches is canon-consistent. It is not.

State:13 @25 — `knowledge.flea-bottom-social-physics: observational-sweep-pattern -> categorical-structural`. The synthesis is fast but Taylor's information-processing capacity (canon) makes fast synthesis plausible. Her bug-sense provides massive parallel data intake; she can build tactical models quickly. One watch-sweep with bugs deployed gives her granular pedestrian-movement and official-movement data simultaneously. The categorical reclassification is aggressive but within the character's documented ability profile. Not flagging — this one I let through.

Remaining entries (state:1, state:3-9, state:14, state:15) are either env/prop writes or Wren's actor-state. State:15 @15 (Wren) is the Wren fork's authority and doesn't raise power-mechanics questions. The field value question (is "attachment-crystallized-deliberate-observer" the right characterization of a Westerosi smallfolk's response to witnessing Taylor) is another reviewer's territory; I'm tracking canon mechanics only.

Two findings. State:10 has a "substrate-level" language problem and an unresolved fence-compliance gap. State:12 has a crystallization-speed problem relative to canon Taylor's documented attachment formation pattern.

# Entry-level callouts

[state-updates:10] @12 — "substrate-level registration" uses shard-architecture vocabulary for a non-cape character's passive noticing. If this is intended as Worm-universe terminology indicating Coll has shard-derived detection, that is an undeclared power mechanic on a character without a cape card. If it is intended as metaphor, the term is incorrect for the register — metaphorical shard-language contamination is a different kind of error but still an error. Additionally: "hard fence 1/2 honored" is an unresolved compliance claim. Which fence is the un-honored one? If a power-mechanics fence is partially satisfied, that is a constraint violation pending clarification. I do not accept entries that acknowledge their own partial non-compliance without naming what is deferred and why.

[state-updates:12] @15 — `social-tether-wren: peripheral-permitted-attachment -> crystallized-observer-bond`. Crystallization speed is wrong for canon Taylor. Her social attachment formation is slow, surveilling, and costly-to-her in ways she is aware of. One deployment event where Wren witnesses her capability does not produce crystallized attachment in canon Taylor's pattern. The field value overclaims the speed of bond formation for this character. `forming-deliberate-tether-wren` or `tether-emerging-observer-recognized` would be more canon-consistent.

# Convergence trace

- [state-updates:10] "substrate-level" language: the auditor's Earth-Bet constraint scan (CN-001, CN-002, fault-001) covers proper-noun fences. It does not audit for Worm-specific terminology misapplied to non-cape characters; that is the seam I am attacking. The auditor's CONSTRAINT class does not catch vocabulary-register contamination that doesn't involve proper nouns.

- [state-updates:10] hard-fence notation: the auditor's flag-003 (CONTRADICTION class) examined the @5 entries co-occurring with the deployment sequence and found no contradiction. The auditor's CONSTRAINT class produced CN-001 and CN-002 on a separate matter (glossed-terms register). The hard-fence compliance notation in state:10's comment was not examined under any auditor finding — it falls in the seam between the mechanical form checks and the constraint-compliance content review.

- [state-updates:12] crystallization speed: the auditor's RUBRIC-FIDELITY pass (RF-001, RF-002, RF-003) checked the NI co-citation requirement and density. It did not evaluate whether the field value's implied timeline is consistent with canon character behavior. That is not a rubric check; it is a canon-pedantry check that lives in my lane, not the auditor's.
